"""Task Management REST API (reference solution for Lab 1).

Run:
    pip install -r ../03-security/requirements.txt
    python solution.py

Endpoints:
    GET  /tasks        -> list tasks (optional ?done=true|false)
    GET  /tasks/<id>   -> get one task
    POST /tasks        -> create a task  {"title": str, "description": str?}
"""
from flask import Flask, jsonify, request

MAX_TITLE = 100
MAX_DESCRIPTION = 500


def validate_task(payload):
    """Validate a task payload. Returns (clean_data, error_message)."""
    if not isinstance(payload, dict):
        return None, "El cuerpo debe ser un objeto JSON"

    title = payload.get("title")
    if not isinstance(title, str) or not title.strip():
        return None, "'title' es obligatorio y debe ser texto no vacío"
    if len(title.strip()) > MAX_TITLE:
        return None, f"'title' no puede superar {MAX_TITLE} caracteres"

    description = payload.get("description", "")
    if not isinstance(description, str):
        return None, "'description' debe ser texto"
    if len(description) > MAX_DESCRIPTION:
        return None, f"'description' no puede superar {MAX_DESCRIPTION} caracteres"

    return {"title": title.strip(), "description": description.strip()}, None


def create_app():
    app = Flask(__name__)
    tasks = {}
    counter = {"next_id": 1}

    @app.get("/tasks")
    def list_tasks():
        done = request.args.get("done")
        result = list(tasks.values())
        if done is not None:
            if done.lower() not in ("true", "false"):
                return jsonify(error="'done' debe ser true o false"), 400
            result = [t for t in result if t["done"] == (done.lower() == "true")]
        return jsonify(result), 200

    @app.get("/tasks/<int:task_id>")
    def get_task(task_id):
        task = tasks.get(task_id)
        if task is None:
            return jsonify(error="Tarea no encontrada"), 404
        return jsonify(task), 200

    @app.post("/tasks")
    def create_task():
        data, error = validate_task(request.get_json(silent=True))
        if error:
            return jsonify(error=error), 400
        task = {"id": counter["next_id"], "done": False, **data}
        tasks[task["id"]] = task
        counter["next_id"] += 1
        return jsonify(task), 201

    @app.errorhandler(404)
    def not_found(_):
        return jsonify(error="Recurso no encontrado"), 404

    @app.errorhandler(405)
    def method_not_allowed(_):
        return jsonify(error="Método no permitido"), 405

    return app


if __name__ == "__main__":
    create_app().run(debug=False)
