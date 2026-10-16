# 🚀 Comunidad & DevSecOps: Estrategias de Integración y Seguridad con GitHub & Sentinel

[![CI](../../actions/workflows/ci.yml/badge.svg)](../../actions/workflows/ci.yml)
![Duración](https://img.shields.io/badge/duraci%C3%B3n-90%20min-blue)
![Nivel](https://img.shields.io/badge/nivel-b%C3%A1sico--intermedio-green)
![Licencia](https://img.shields.io/badge/licencia-MIT-lightgrey)

Taller hands-on de **90 minutos** para estudiantes universitarios con conocimientos básicos de programación y GitHub. Aprenderás a usar **GitHub Copilot**, colaborar con **GitHub Flow**, detectar vulnerabilidades y entender cómo **GitHub** y **Microsoft Sentinel** se integran en un ciclo **DevSecOps**.

> ⚠️ Este repositorio incluye código **vulnerable a propósito** (`03-security`). Todas las credenciales son ficticias. No lo uses en producción.

## 🎯 Objetivos
Al terminar serás capaz de:
1. Usar Copilot para generar, documentar y revisar código (prompt engineering básico).
2. Colaborar con Fork, Branch, Commit, Push y Pull Request.
3. Identificar vulnerabilidades comunes (secretos, validación, logs, dependencias) y corregirlas.
4. Explicar qué hacen Secret Scanning, Dependabot, el equipo DevSecOps y Microsoft Sentinel ante un incidente.
5. Participar en comunidades de aprendizaje (Student Ambassadors, Campus Experts).

## 🗓️ Agenda (90 min)
| Min | Actividad | Dificultad | Carpeta |
|---|---|---|---|
| 0-5 | Bienvenida y configuración | – | este README |
| 5-20 | **Lab 1** – API REST con GitHub Copilot (15 min) | ⭐ Básico → ⭐⭐ | [`01-copilot`](01-copilot/README.md) |
| 20-35 | **Lab 2** – GitHub Flow (15 min) | ⭐ Básico | [`02-github-flow`](02-github-flow/README.md) |
| 35-55 | **Lab 3** – Seguridad: encuentra y corrige (20 min) | ⭐⭐ Intermedio | [`03-security`](03-security/README.md) |
| 55-70 | **Lab 4** – DevSecOps: "Token filtrado en GitHub" (15 min) | ⭐⭐ Intermedio | [`04-devsecops`](04-devsecops/README.md) |
| 70-85 | **🏆 Desafío final** por equipos (15 min) | ⭐⭐ Intermedio | [abajo](#-desafío-final) |
| 85-90 | Presentaciones relámpago y cierre | – | [`resources`](resources/learn-links.md) |

## ✅ Requisitos
- Cuenta de GitHub (gratis) y acceso a **GitHub Copilot** (gratis para estudiantes vía [GitHub Education](https://education.github.com/))
- [Git](https://git-scm.com/), [Python 3.11+](https://www.python.org/) y [VS Code](https://code.visualstudio.com/) con la extensión *GitHub Copilot*
- Conocimientos básicos de Python y de la terminal

## ▶️ Cómo ejecutar los laboratorios
```bash
# 1. Fork en GitHub y clonar
git clone https://github.com/<tu-usuario>/community-devsecops-lab.git
cd community-devsecops-lab

# 2. Entorno virtual e instalación
python -m venv .venv
.venv\Scripts\activate          # Windows   (macOS/Linux: source .venv/bin/activate)
pip install -r 03-security/requirements.txt

# 3. Verificar que todo funciona
pytest tests

# 4. Ejecutar la API del Lab 1 (solución de referencia)
python 01-copilot/solution.py
```
Cada carpeta tiene su propio `README.md` con instrucciones paso a paso y checklist.

## 🗂️ Estructura
```
01-copilot/       Lab 1: starter.py (con TODOs) y solution.py
02-github-flow/   Lab 2: guía, ejercicios y ejemplos de PRs
03-security/      Lab 3: código vulnerable vs. seguro, dependencias
04-devsecops/     Lab 4: escenario y diagrama de arquitectura
resources/        Enlaces de aprendizaje
solutions/        Material de facilitadores (respuestas y rúbricas)
tests/            Pruebas automáticas ejecutadas por el CI
.github/          Plantillas de issues/PR, CI y Dependabot
```

## 🏆 Desafío final
**Equipos de 3-4 personas · ⭐⭐ Intermedio · 15 min (+ tarea opcional)**

Simulen un ciclo completo de desarrollo seguro:

1. **Completar una API con Copilot:** extiendan `01-copilot/starter.py` (por ejemplo `PUT /tasks/<id>` y `DELETE /tasks/<id>`) usando prompts.
2. **Crear una rama:** `feature/<equipo>-api`.
3. **Commit:** mensajes claros y pequeños.
4. **Abrir un Pull Request** con la plantilla y el CI en verde.
5. **Identificar vulnerabilidades:** revisen `03-security/vulnerable_app.py` y listen las que encuentren (¡con Copilot como revisor!).
6. **Proponer controles DevSecOps:** al menos 5, indicando la fase (Plan, Code, Build, Deploy, Operate).
7. **Explicar cómo Microsoft Sentinel podría detectar el incidente** del escenario "Token filtrado": fuentes de logs, regla/consulta KQL, incidente y playbook.

**Entregable:** el PR + un comentario en él con los puntos 5-7 (máx. 1 minuto de exposición por equipo).

**Evaluación:** funcionalidad de la API (20) · flujo Git/PR (20) · vulnerabilidades (25) · controles (20) · Sentinel (15).

## 📚 Más recursos
Ver [`resources/learn-links.md`](resources/learn-links.md). Para contribuir: [CONTRIBUTING.md](CONTRIBUTING.md). Seguridad: [SECURITY.md](SECURITY.md). Licencia [MIT](LICENSE).
