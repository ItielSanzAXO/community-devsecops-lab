# 🔀 Laboratorio 2 – GitHub Flow

**Dificultad:** ⭐ Básico · **Duración:** 15 min · Trabajo en parejas (Dev A y Dev B)

## Objetivo
Practicar el ciclo completo: **Fork → Branch → Commit → Push → Pull Request → Review → Merge**.

```
main ──●────────────────────●── (merge)
        \                  /
         feature/mi-cambio ●──●── PR + review
```

## Paso a paso

### 1. Fork
En GitHub, abre el repositorio del taller y pulsa **Fork** → *Create fork*.

### 2. Clonar
```bash
git clone https://github.com/<tu-usuario>/community-devsecops-lab.git
cd community-devsecops-lab
git remote add upstream https://github.com/<organizador>/community-devsecops-lab.git
```

### 3. Branch
```bash
git switch -c feature/agrega-tu-nombre
```
Convención: `feature/…`, `fix/…`, `docs/…`.

### 4. Cambios y Commit
Sigue [`exercises.md`](exercises.md). Luego:
```bash
git add <archivo>
git commit -m "docs: agrega mi nombre a la lista de participantes"
```
Buenos mensajes: imperativo, corto, con prefijo (`feat`, `fix`, `docs`, `test`, `chore`).

### 5. Push
```bash
git push -u origin feature/agrega-tu-nombre
```

### 6. Pull Request
En GitHub pulsa **Compare & pull request**, completa la plantilla (objetivo, cambios, evidencias, checklist de seguridad) y revisa que el workflow **CI** pase.

### 7. Review y Merge
Tu compañero revisa: comenta líneas, pide un cambio o aprueba (*Approve*). Luego se hace **Merge** y se elimina la rama.

### 8. Sincronizar
```bash
git switch main && git pull upstream main
```

## Simulación de colaboración
Ver [`exercises.md`](exercises.md) (ejercicios 1-4) y [`example-pull-requests.md`](example-pull-requests.md) (ejemplos de buenos y malos PRs).

## ✅ Checklist
- [ ] Hice fork y clon
- [ ] Mi rama no es `main`
- [ ] Al menos 2 commits con buenos mensajes
- [ ] Mi PR usa la plantilla y el CI está en verde
- [ ] Revisé el PR de mi compañero con al menos 1 comentario útil
