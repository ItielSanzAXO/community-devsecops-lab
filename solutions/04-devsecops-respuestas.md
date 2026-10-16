# 🔒 Respuestas – Lab 4: "Token filtrado en GitHub" (facilitadores)

## 1. ¿Qué riesgo existe?
- **Confidencialidad:** lectura de datos de clientes del contenedor `reportes`.
- **Integridad:** el SAS tenía `rwdlac`: se pueden modificar/borrar blobs (ransomware, sabotaje).
- **Disponibilidad y costos:** borrado masivo, minado/abuso de almacenamiento, facturas inesperadas.
- **Cumplimiento:** posible brecha de datos personales (notificación obligatoria, multas).
- Bots escanean GitHub en **segundos**: se debe asumir que el token ya está comprometido.

## 2. GitHub Secret Scanning
- Detecta patrones de tokens de socios (incluye Azure) en el código y el historial; alerta a administradores (*Security → Secret scanning*) y notifica al proveedor cuando es *partner pattern*.
- Con **Push Protection** habilitado, **bloquea el push** antes de que llegue el secreto (la dev puede omitirlo con justificación, que queda auditada).
- No revoca automáticamente en todos los casos: **hay que rotar manualmente**.

## 3. Dependabot
- **No detecta secretos.** Cubre dependencias vulnerables (alertas, PRs de actualización, security updates).
- Aporte indirecto: reduce otras vías de ataque; sirve para contrastar "qué herramienta cubre qué" (pregunta trampa).

## 4. Equipo DevSecOps (Detectar → Contener → Erradicar → Recuperar → Aprender)
| Fase | Acciones |
|---|---|
| Contener (minutos) | **Revocar/rotar** el SAS (regenerar la clave de la cuenta o la política de acceso almacenada); marcar la alerta como revocada |
| Investigar | Revisar logs de acceso desde el commit; alcance de datos expuestos; ¿IPs desconocidas? |
| Erradicar | Quitar el secreto del código; limpiar historial (`git filter-repo`/BFG) **después** de rotar; invalidar forks/cachés |
| Recuperar | Restaurar datos si hubo cambios; nuevas credenciales vía **Key Vault** / identidades administradas |
| Aprender | Post-mortem sin culpas; activar Push Protection; capacitar; SAS con mínimo privilegio y expiración corta; pre-commit hooks (gitleaks) |

## 5. Microsoft Sentinel
- No ve el código, ve la **telemetría**: conecta *Azure Storage logs*, *Entra ID*, *Azure Activity* y *GitHub audit log* (conector GitHub).
- **Regla analítica** (KQL) para SAS usado desde IPs nuevas/volumen anómalo (ver `04-devsecops/README.md`) → crea **incidente**.
- Correlación: alerta de GitHub + accesos anómalos al storage = incidente de alta severidad.
- **Playbook (Logic Apps / SOAR):** notificar en Teams, abrir issue, bloquear IP, rotar claves, deshabilitar acceso público.
- Enriquecimiento con Threat Intelligence y UEBA; *hunting* retroactivo.

## 6. Controles preventivos (ejemplos)
1. Push Protection + Secret Scanning activados a nivel organización.
2. Secretos en GitHub Secrets / Key Vault; identidades administradas / OIDC en Actions.
3. SAS con mínimo privilegio y expiración corta; ramas protegidas; pre-commit con gitleaks.
