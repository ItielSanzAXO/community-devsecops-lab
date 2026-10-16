# 🔐 Laboratorio 3 – Seguridad

**Dificultad:** ⭐⭐ Intermedio · **Duración:** 20 min

> ⚠️ [`vulnerable_app.py`](vulnerable_app.py) es vulnerable a propósito. No lo despliegues. Las credenciales son ficticias.

## Actividad
1. Lee `vulnerable_app.py` e intenta **encontrar** los 6 problemas antes de leer la tabla.
2. Pídele a Copilot: `Review this file for security vulnerabilities and rank them by severity.`
3. Corrige tu propia copia y compárala con [`secure_app.py`](secure_app.py).
4. Audita dependencias: `pip install pip-audit && pip-audit -r 03-security/requirements-vulnerable.txt`
5. (Bonus) Ejecuta el ataque SQLi: en `/login` usa `username = "admin' --"` contra la versión vulnerable.

Ejecutar la versión segura:
```bash
# PowerShell
$env:APP_API_KEY = "una-clave-larga-generada"; $env:APP_ADMIN_PASSWORD = "otra-contraseña-fuerte"
python 03-security/secure_app.py
```

## Análisis de vulnerabilidades

| # | Vulnerabilidad | ¿Por qué es insegura? | Riesgo | Solución correcta |
|---|---|---|---|---|
| 1 | **API Key hardcodeada** `API_KEY = "123456"` | El secreto queda en el código y en el historial de Git; es trivial de adivinar | Acceso no autorizado a la API/servicios; fuga pública si el repo es público | Variables de entorno / GitHub Secrets / Azure Key Vault; claves aleatorias; rotar si se filtró |
| 2 | **Contraseña hardcodeada** y guardada en texto plano | Cualquiera con acceso al repo o BD la lee | Toma de cuenta admin, movimiento lateral | Secretos externos; guardar solo hashes con sal (PBKDF2/bcrypt/argon2) |
| 3 | **Falta de validación** (y SQL Injection) | Se confía en la entrada del usuario; SQL por concatenación | Bypass de autenticación, robo/borrado de datos, caídas (KeyError → 500) | Validar tipo/longitud; consultas parametrizadas |
| 4 | **Logging inseguro** | Se escriben contraseña y API key en logs | Los logs se copian a múltiples sistemas; fuga de credenciales (CWE-532) | Nunca registrar secretos; enmascarar; registrar eventos (usuario, resultado) |
| 5 | **Dependencias antiguas** (`requirements-vulnerable.txt`) | Contienen CVEs públicos | Explotación de vulnerabilidades conocidas | Actualizar, fijar versiones, Dependabot, `pip-audit` |
| 6 | **`debug=True` + `0.0.0.0`** | Consola Werkzeug permite ejecutar código | Ejecución remota de código (RCE) | `debug=False`, bind a localhost o detrás de un proxy |

## 🔗 Relación con herramientas GitHub
- **Secret Scanning + Push Protection** → detecta #1 y #2 antes del push.
- **Dependabot** → detecta y abre PRs para #5.
- **CodeQL** → detecta SQLi (#3) y logging de datos sensibles (#4).

## ✅ Checklist
- [ ] Identifiqué los 6 problemas
- [ ] Mi versión corregida no tiene secretos en el código
- [ ] Probé que la versión segura rechaza entradas inválidas
