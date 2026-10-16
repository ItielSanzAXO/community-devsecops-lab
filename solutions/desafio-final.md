# 🔒 Desafío final – Rúbrica y respuestas (facilitadores)

## Rúbrica (100 pts)
| Criterio | Pts |
|---|---|
| API completa (GET, POST, validación, errores JSON) con Copilot | 20 |
| Rama + commits claros + PR con plantilla completa y CI en verde | 20 |
| Vulnerabilidades identificadas (≥ 4 de 6) con riesgo y solución | 25 |
| Controles DevSecOps propuestos (≥ 5, mapeados a fase del ciclo) | 20 |
| Explicación de detección con Sentinel (logs, regla, incidente, playbook) | 15 |

## Vulnerabilidades en `vulnerable_app.py`
1. API key hardcodeada (y devuelta en `/login`) 2. Contraseña hardcodeada/en texto plano 3. Sin validación + SQL Injection 4. Logging de secretos 5. Dependencias antiguas 6. `debug=True` en `0.0.0.0`.

## Controles esperados
| Fase | Control |
|---|---|
| Plan | Modelado de amenazas, requisitos de seguridad |
| Code | Push Protection, Secret Scanning, revisión de PR, Copilot para revisión |
| Build | CodeQL, Dependabot, `pip-audit`, pruebas |
| Deploy | Secretos en Key Vault/GitHub Secrets, OIDC, ramas protegidas, entornos con aprobación |
| Operate | Logs centralizados, Sentinel, alertas |
| Respond | Playbooks, rotación de credenciales, post-mortem |

## Detección con Sentinel (ejemplo)
- Fuentes: logs de la app (Azure Monitor / App Service), Entra ID, GitHub audit log.
- Regla KQL ejemplo — muchos logins fallidos o intentos SQLi:
```kusto
AppServiceHTTPLogs
| where TimeGenerated > ago(15m) and CsUriStem == "/login"
| summarize Fallos = countif(ScStatus == 401), Sospechosos = countif(CsUriQuery contains "'" or CsUriQuery contains "--") by CIp
| where Fallos > 20 or Sospechosos > 0
```
- Acción: incidente → playbook que bloquea la IP, notifica por Teams y abre un issue en GitHub.
