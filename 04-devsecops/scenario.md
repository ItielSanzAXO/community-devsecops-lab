# 🛡️ Escenario: "Token filtrado en GitHub"

**Dificultad:** ⭐⭐ Intermedio · **Duración:** 15 min · Trabajo en equipos de 3-4

## Situación
Son las 17:42 del viernes. **Laura**, desarrolladora junior del equipo de una startup, está terminando una función que sube reportes a Azure Blob Storage. Para probar rápido, pega en `config.py` un token SAS de Azure con permisos de lectura/escritura sobre la cuenta de almacenamiento de producción:

```python
# config.py  (EJEMPLO FICTICIO)
AZURE_STORAGE_SAS = "sv=2022-11-02&ss=b&srt=sco&sp=rwdlac&se=2027-01-01&sig=FAKE_EXAMPLE_TOKEN"
```

Hace `git commit` y `git push` a un repositorio **público**. Se va a casa. El repositorio contiene datos de clientes en el contenedor `reportes`.

## Preguntas para el equipo

1. **¿Qué riesgo existe?** (confidencialidad, integridad, disponibilidad, costos, cumplimiento)
2. **¿Qué haría GitHub Secret Scanning?** ¿Y Push Protection?
3. **¿Qué haría Dependabot?** (¿aplica a este caso? ¿qué sí cubre?)
4. **¿Qué haría el equipo DevSecOps?** Línea de tiempo de respuesta.
5. **¿Cómo podría intervenir Microsoft Sentinel?** ¿Qué datos/conectores y qué consulta KQL usarían?
6. **Prevención:** propongan 3 controles para que no vuelva a ocurrir.

## Formato de entrega
Una tabla de 1 página (o issue en el repo con la plantilla) con las respuestas y un diagrama de la cadena de respuesta. Usa [`architecture.png`](architecture.png) de apoyo.

## Pistas
- Un secreto borrado en un commit posterior **sigue en el historial** y en bots que rastrean GitHub en segundos.
- Piensa en *Detectar → Contener → Erradicar → Recuperar → Aprender*.
- Sentinel analiza **logs** (Azure Storage, Entra ID, Activity Log, GitHub audit log), no el código.

> Las respuestas modelo están en [`../solutions/04-devsecops-respuestas.md`](../solutions/04-devsecops-respuestas.md) (facilitadores).
