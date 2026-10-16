# 🤖 Laboratorio 1 – GitHub Copilot

**Dificultad:** ⭐ Básico (TODO 1-5) · ⭐⭐ Intermedio (TODO 6-7 y pruebas) · **Duración:** 15 min

## Objetivo
Usar GitHub Copilot para construir una API REST de gestión de tareas con Flask: endpoints `GET` y `POST`, validación de entradas, comentarios y documentación.

## Preparación
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate   |   macOS/Linux: source .venv/bin/activate
pip install -r 03-security/requirements.txt
```
Verifica que Copilot esté activo en VS Code (ícono en la barra de estado).

## Pasos
1. Abre [`starter.py`](starter.py).
2. Resuelve cada `TODO` con Copilot (Chat, Inline o autocompletado).
3. Ejecuta: `python 01-copilot/starter.py`
4. Prueba:
   ```bash
   curl -X POST http://127.0.0.1:5000/tasks -H "Content-Type: application/json" -d '{"title":"Estudiar DevSecOps"}'
   curl http://127.0.0.1:5000/tasks
   curl -X POST http://127.0.0.1:5000/tasks -H "Content-Type: application/json" -d '{"title":""}'   # debe dar 400
   ```
5. Compara con [`solution.py`](solution.py) **solo al final**.

## 💬 Prompts sugeridos
| Nivel | Prompt |
|---|---|
| ⭐ | `Generate a REST API in Python using Flask for task management. Include validation, comments and error handling.` |
| ⭐ | `Add a GET /tasks endpoint that returns all tasks as JSON.` |
| ⭐ | `Add a POST /tasks endpoint that validates that title is a non-empty string of max 100 chars and returns 201.` |
| ⭐⭐ | `Add a ?done=true|false query filter to GET /tasks and return 400 for invalid values.` |
| ⭐⭐ | `Write pytest tests for this Flask API using the test client, covering success and error cases.` |
| ⭐⭐ | `Review this code for security issues and input validation gaps.` |
| ⭐⭐ | `Add docstrings and explain each endpoint with comments in Spanish.` |

### Tips de prompt engineering
- Sé específico: lenguaje, framework, restricciones.
- Da contexto (abre los archivos relacionados).
- Itera: pide mejoras en vez de empezar de cero.
- **Siempre revisa** el código generado: Copilot es un asistente, tú eres el responsable.

## ✅ Criterios de éxito
- [ ] `GET /tasks` y `GET /tasks/<id>` funcionan
- [ ] `POST /tasks` valida y devuelve 201 / 400
- [ ] Errores en formato JSON
- [ ] Código comentado y con docstrings
- [ ] (⭐⭐) Pruebas con pytest: `pytest tests/`

## 🤔 Preguntas de reflexión
1. ¿Qué sugerencia de Copilot rechazaste y por qué?
2. ¿Qué validación faltó en la primera respuesta?
