"""Task Management REST API - STARTER (Lab 1).

Usa GitHub Copilot para completar los TODO. No copies la solución:
escribe un comentario o prompt, revisa la sugerencia y entiéndela antes de aceptarla.
"""
from flask import Flask, jsonify, request


def validate_task(payload):
    """Validate a task payload. Return (clean_data, error_message).

    TODO 1: 'title' obligatorio, texto, máximo 100 caracteres.
    TODO 2: 'description' opcional, texto, máximo 500 caracteres.
    """
    raise NotImplementedError


def create_app():
    app = Flask(__name__)
    tasks = {}  # almacenamiento en memoria: {id: task}

    # TODO 3: GET /tasks -> lista todas las tareas (200)

    # TODO 4: GET /tasks/<id> -> una tarea (200) o error 404 en JSON

    # TODO 5: POST /tasks -> valida con validate_task, crea la tarea (201)
    #         o responde 400 con {"error": "..."}

    # TODO 6 (⭐⭐): filtro GET /tasks?done=true|false

    # TODO 7: manejadores de error 404 y 405 que devuelvan JSON

    return app


if __name__ == "__main__":
    create_app().run(debug=False)
