"""Versión corregida de vulnerable_app.py.

Configuración por variables de entorno:
    APP_API_KEY          clave de API (obligatoria)
    APP_ADMIN_PASSWORD   contraseña inicial del admin (obligatoria)
"""
import hashlib
import hmac
import logging
import os
import sqlite3
import secrets

from flask import Flask, jsonify, request

log = logging.getLogger("secure_app")


def _hash(password: str, salt: bytes) -> bytes:
    return hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 200_000)


def _require_env(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        raise RuntimeError(f"Falta la variable de entorno {name}")
    return value


def validate_credentials(data):
    """Devuelve (username, password, error)."""
    if not isinstance(data, dict):
        return None, None, "JSON inválido"
    username, password = data.get("username"), data.get("password")
    if not isinstance(username, str) or not 1 <= len(username) <= 50:
        return None, None, "username inválido"
    if not isinstance(password, str) or not 1 <= len(password) <= 128:
        return None, None, "password inválido"
    return username, password, None


def create_app():
    api_key = _require_env("APP_API_KEY")  # [FIX-1] secretos fuera del código
    admin_password = _require_env("APP_ADMIN_PASSWORD")  # [FIX-2]

    app = Flask(__name__)
    logging.basicConfig(level=logging.INFO)

    db = sqlite3.connect(":memory:", check_same_thread=False)
    db.execute("CREATE TABLE users (username TEXT PRIMARY KEY, salt BLOB, pwd_hash BLOB)")
    salt = os.urandom(16)
    db.execute("INSERT INTO users VALUES (?, ?, ?)", ("admin", salt, _hash(admin_password, salt)))

    @app.post("/login")
    def login():
        username, password, error = validate_credentials(request.get_json(silent=True))
        if error:  # [FIX-3] validación de entradas
            return jsonify(error=error), 400

        # [FIX-3b] consulta parametrizada
        row = db.execute("SELECT salt, pwd_hash FROM users WHERE username = ?", (username,)).fetchone()
        if row and hmac.compare_digest(_hash(password, row[0]), row[1]):
            # [FIX-4] no se registran secretos; solo el usuario y el resultado
            log.info("login exitoso user=%s", username)
            return jsonify(token=secrets.token_urlsafe(32)), 200
        log.warning("login fallido user=%s", username)
        return jsonify(error="credenciales inválidas"), 401

    @app.get("/users")
    def users():
        provided = request.headers.get("X-API-Key", "")
        if not hmac.compare_digest(provided, api_key):  # comparación en tiempo constante
            return jsonify(error="no autorizado"), 401
        return jsonify([r[0] for r in db.execute("SELECT username FROM users")]), 200

    return app


if __name__ == "__main__":
    # [FIX-6] sin debug y escuchando solo en localhost
    create_app().run(host="127.0.0.1", debug=False)
