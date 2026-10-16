"""Pruebas del laboratorio: API de tareas (Lab 1) y app segura (Lab 3)."""
import importlib.util
import pathlib

import pytest

ROOT = pathlib.Path(__file__).resolve().parent.parent


def load(relative_path, name):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture()
def tasks_client():
    return load("01-copilot/solution.py", "solution").create_app().test_client()


@pytest.fixture()
def secure_client(monkeypatch):
    monkeypatch.setenv("APP_API_KEY", "test-key-xyz")
    monkeypatch.setenv("APP_ADMIN_PASSWORD", "test-pass-123")
    return load("03-security/secure_app.py", "secure_app").create_app().test_client()


def test_create_and_get_task(tasks_client):
    r = tasks_client.post("/tasks", json={"title": "  Estudiar  "})
    assert r.status_code == 201 and r.get_json()["title"] == "Estudiar"
    assert tasks_client.get("/tasks/1").status_code == 200
    assert len(tasks_client.get("/tasks").get_json()) == 1


@pytest.mark.parametrize("payload", [{}, {"title": ""}, {"title": 5}, {"title": "x" * 101},
                                     {"title": "ok", "description": 1}, [1]])
def test_invalid_task_rejected(tasks_client, payload):
    assert tasks_client.post("/tasks", json=payload).status_code == 400


def test_not_found_and_filter(tasks_client):
    assert tasks_client.get("/tasks/99").status_code == 404
    assert tasks_client.get("/tasks?done=maybe").status_code == 400
    assert tasks_client.get("/tasks?done=true").get_json() == []


def test_secure_login_ok_and_fail(secure_client):
    ok = secure_client.post("/login", json={"username": "admin", "password": "test-pass-123"})
    assert ok.status_code == 200 and "token" in ok.get_json()
    assert secure_client.post("/login", json={"username": "admin", "password": "bad"}).status_code == 401


def test_secure_blocks_sqli_and_bad_input(secure_client):
    r = secure_client.post("/login", json={"username": "admin' --", "password": "x"})
    assert r.status_code == 401
    assert secure_client.post("/login", json={"username": 1}).status_code == 400


def test_secure_users_requires_key(secure_client):
    assert secure_client.get("/users").status_code == 401
    assert secure_client.get("/users", headers={"X-API-Key": "test-key-xyz"}).status_code == 200


def test_secure_app_requires_env(monkeypatch):
    monkeypatch.delenv("APP_API_KEY", raising=False)
    with pytest.raises(RuntimeError):
        load("03-security/secure_app.py", "secure_app2").create_app()
