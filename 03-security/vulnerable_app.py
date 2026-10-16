"""⚠️ APLICACIÓN DELIBERADAMENTE VULNERABLE – SOLO PARA FINES EDUCATIVOS ⚠️

NO la despliegues. Todas las credenciales son falsas.
Cada vulnerabilidad está marcada con [VULN-n]. Ver README.md del laboratorio.
"""
import logging
import sqlite3

from flask import Flask, jsonify, request

# [VULN-1] API Key hardcodeada
API_KEY = "123456"

# [VULN-2] Contraseña hardcodeada (credencial de administrador)
ADMIN_PASSWORD = "admin123"

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger("vulnerable_app")

app = Flask(__name__)
db = sqlite3.connect(":memory:", check_same_thread=False)
db.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
db.execute("INSERT INTO users (username, password) VALUES ('admin', ?)", (ADMIN_PASSWORD,))


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json(force=True)
    username = data["username"]  # [VULN-3] sin validación (KeyError, tipos, longitud)
    password = data["password"]

    # [VULN-4] Logging inseguro: se registra la contraseña y la API key
    log.info("Login attempt user=%s password=%s api_key=%s", username, password, API_KEY)

    # [VULN-3b] SQL Injection: concatenación de strings
    query = f"SELECT id FROM users WHERE username = '{username}' AND password = '{password}'"
    row = db.execute(query).fetchone()
    if row:
        return jsonify(message="ok", token=API_KEY)  # [VULN-1b] se filtra la clave
    return jsonify(message="invalid credentials"), 401


@app.route("/users")
def users():
    if request.headers.get("X-API-Key") == API_KEY:  # [VULN-1c] comparación simple
        return jsonify([r[0] for r in db.execute("SELECT username FROM users")])
    return jsonify(error="unauthorized"), 401


if __name__ == "__main__":
    # [VULN-6] debug=True y host abierto: consola interactiva expuesta
    app.run(host="0.0.0.0", debug=True)
