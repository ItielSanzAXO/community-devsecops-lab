# Guía de contribución

¡Gracias por participar! Este repositorio es educativo; todas las contribuciones siguen **GitHub Flow**.

## Cómo contribuir
1. Haz **fork** y clona tu copia.
2. Crea una rama: `git switch -c feature/descripcion-corta` (o `fix/`, `docs/`).
3. Haz commits pequeños con mensajes claros (`feat:`, `fix:`, `docs:`, `test:`).
4. Ejecuta las pruebas: `pip install -r 03-security/requirements.txt && pytest tests`
5. Haz push y abre un **Pull Request** usando la plantilla.
6. Atiende los comentarios de la revisión.

## Reglas
- Nunca subas secretos, tokens ni datos personales (aunque sean "de prueba" reales).
- Los archivos vulnerables (`03-security/vulnerable_app.py`, `requirements-vulnerable.txt`) lo son **a propósito**; no los "arregles" en PRs, la versión corregida es `secure_app.py`.
- Reporta problemas con la plantilla de issues. Las vulnerabilidades reales: ver [SECURITY.md](SECURITY.md).
- Sé respetuoso: se aplica el [Contributor Covenant](https://www.contributor-covenant.org/es/version/2/1/code_of_conduct/).
