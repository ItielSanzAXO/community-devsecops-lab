# Ejemplos de Pull Requests

Referencia para practicar el code review. Los ejemplos son ficticios.

---

## PR #1 ✅ Buen ejemplo – `feat: agrega filtro done a GET /tasks`

### 🎯 Objetivo
Permitir filtrar tareas completadas. Closes #12

### 🛠️ Cambios realizados
- Parámetro `?done=true|false` en `GET /tasks`
- Respuesta 400 si el valor es inválido
- 2 pruebas nuevas

### 📸 Evidencias
`pytest tests` → 12 passed · CI ✅

### 🔐 Checklist de seguridad
- [x] Sin secretos · [x] Entradas validadas · [x] Sin datos sensibles en logs

**Por qué es bueno:** pequeño, enfocado, con pruebas, enlaza el issue y completa la plantilla.

---

## PR #2 ❌ Mal ejemplo – `update`

### Descripción
"cambios varios"

### Diff (resumen)
```diff
+ API_KEY = "sk-live-9f8a7b6c5d4e3f2a1b"
+ log.info("login %s / %s", username, password)
+ query = f"SELECT * FROM users WHERE name = '{username}'"
- def validate_task(payload): ...
```

### Problemas para detectar en la revisión
1. Secreto hardcodeado (debe ir a variable de entorno y **rotarse**, ya está en el historial).
2. Se registra la contraseña en logs.
3. SQL por concatenación → SQL Injection.
4. Se elimina validación sin justificación.
5. Título y descripción no informativos; no sigue la plantilla; mezcla temas.

### Revisión de ejemplo
> 🔴 **Request changes** – Línea 1: no se pueden subir claves al repositorio; usa `os.environ` y rota esta clave. Línea 2: nunca registres contraseñas. Línea 3: usa consultas parametrizadas (`?`). ¿Podemos dividir este PR y añadir pruebas?

---

## PR #3 ✅ Ejemplo de seguridad – `fix: elimina credenciales hardcodeadas`
Cambia `ADMIN_PASSWORD = "admin123"` por `os.environ["APP_ADMIN_PASSWORD"]`, guarda hash PBKDF2 y agrega prueba que verifica que la app falla sin la variable. Incluye nota: *"Credencial anterior rotada en Azure Key Vault"*.
