# Ejercicios – GitHub Flow

## Ejercicio 1 · ⭐ Básico – Tu primer PR (5 min)
1. Crea la rama `feature/participante-<usuario>`.
2. Crea el archivo `participants/<usuario>.md` con tu nombre, universidad y un tema que quieras aprender.
3. Commit → push → abre PR hacia `main`.

## Ejercicio 2 · ⭐ Básico – Corrige un typo (5 min)
Dev A abre un issue con la plantilla ("Reporte de problema") sobre un error de ortografía en cualquier README.
Dev B crea `fix/typo-readme`, lo corrige y abre un PR que incluya `Closes #<n>` en la descripción.

## Ejercicio 3 · ⭐⭐ Intermedio – Colaboración y conflicto (10 min)
Simula dos desarrolladores que editan la misma línea:
1. Dev A y Dev B parten de `main` y crean ramas distintas: `feature/titulo-a` y `feature/titulo-b`.
2. Ambos cambian la **primera línea** de `01-copilot/README.md` con títulos distintos y hacen commit.
3. Dev A abre PR y se fusiona.
4. Dev B actualiza su rama:
   ```bash
   git fetch upstream
   git rebase upstream/main      # o: git merge upstream/main
   ```
5. Resuelve el conflicto (elige o combina ambos títulos), luego:
   ```bash
   git add 01-copilot/README.md
   git rebase --continue
   git push --force-with-lease
   ```
6. Dev B abre PR y Dev A lo revisa.

## Ejercicio 4 · ⭐⭐ Intermedio – Code review (10 min)
Revisa [`example-pull-requests.md`](example-pull-requests.md), PR #2. Escribe 3 comentarios de revisión: uno sobre seguridad, uno sobre claridad y uno positivo.

## Ejercicio 5 · ⭐⭐ Intermedio – Proteger `main` (facilitador/demo)
En *Settings → Rules → Rulesets* exige: PR antes de merge, 1 aprobación y que el check **CI** pase.

## Preguntas de reflexión
- ¿Por qué no se hace push directo a `main`?
- ¿Qué ventaja tiene un PR pequeño?
- ¿Qué pasa si subes un secreto en un commit y luego lo borras en otro?
