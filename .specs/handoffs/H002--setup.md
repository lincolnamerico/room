---
title: "H002: Milestone 1 — Foundation (Setup)"
handoff_id: H002
handoff_chain_position: 2
status: active
date: 2026-05-27
author: DeepSeek (via opencode)
next_agent: Feature development agent
next_stage: M2 — Integração produção local (UBS/IDS) — Specify
---

# H002: Milestone 1 — Foundation (Setup)

> Handoff #2 da cadeia. Projeto Room scaffoldado com frontend, backend,
> Docker e CI. Pronto para começar a primeira feature de negócio.

---

## Context Snapshot

| Field | Value |
|-------|-------|
| Project | Room |
| Stage | Milestone 1 — Foundation ✅ Complete |
| Branch | `main` |
| Last Commit | `833128d` feat(setup): scaffold project structure |
| GitHub | https://github.com/lincolnamerico/room |
| Remote | `origin/main` |

---

## Completed ✓

- [x] Frontend Next.js 16 + TypeScript + Tailwind + ECharts + Leaflet
- [x] Backend FastAPI + SQLAlchemy + Alembic + pandas + Ruff
- [x] PostgreSQL + PostGIS via Docker Compose
- [x] Docker Compose with health checks and named volume
- [x] CI pipeline (GitHub Actions): frontend build + lint, backend ruff
- [x] .gitignore, .env.example, project structure

---

## Files Changed (this milestone)

```
frontend/          → Next.js app (src/app/, public/)
backend/           → FastAPI app (main.py, config.py, database.py)
docker-compose.yml → PostgreSQL + PostGIS + backend + frontend
docker/            → Dockerfile.backend, Dockerfile.frontend
database/init/     → 001_create_extensions.sql (postgis, uuid-ossp)
.github/workflows/ → ci.yml
```

---

## Project Structure (current)

```
room/
├── frontend/
│   ├── src/app/         ← Next.js pages (App Router)
│   ├── package.json     ← echarts, leaflet installed
│   └── next.config.ts
├── backend/
│   ├── app/
│   │   ├── main.py      ← FastAPI entry (health check)
│   │   ├── config.py    ← Settings (DATABASE_URL via env)
│   │   ├── database.py  ← SQLAlchemy engine + session
│   │   ├── models/
│   │   ├── routers/
│   │   ├── schemas/
│   │   └── services/
│   └── pyproject.toml   ← dependencies + ruff config
├── database/init/       ← SQL init scripts (PostGIS)
├── docker/              ← Dockerfiles
├── docker-compose.yml   ← Full stack
├── .github/workflows/ci.yml
└── .specs/              ← SDD artifacts
```

---

## Relevant Decisions

| ID | Decision | Impact |
|----|----------|--------|
| AD-001 | Next.js + FastAPI + PostgreSQL/PostGIS | Two apps, Docker Compose |
| AD-003 | Direct Docker Compose (not monorepo tool) | Simpler setup, compose controls all |
| AD-004 | CI with separate frontend/backend jobs | Parallel checks, clear failure isolation |

See STATE.md for full decision records.

---

## Blockers

None.

---

## Next Agent: Exact Instructions

### What to do next

```
Milestone 2 — Integração produção local (UBS/IDS)
─────────────────────────────────────────────────
1. Follow SDD workflow:
   a. SPECIFY (this handoff + spec.md)
   b. DESIGN (if needed)
   c. TASKS (if needed)
   d. EXECUTE

2. The goal is to define the data model and API for
   health indicators from the local IDS system:
   - What indicators exist?
   - How do territorial levels work? (município, bairro, microárea)
   - What's the integration mechanism with IDS software?
```

### Token budget for your session

| File | Tokens | Required? |
|------|--------|-----------|
| `H002--setup.md` (this file) | ~300 | ✅ Yes |
| `INDEX.md` | ~100 | ✅ Yes |
| `STATE.md` | ~200 | ✅ Yes |
| `INIT.md` (genesis + principles) | ~500 | ✅ First time on features |
| `PROJECT.md` (scope) | ~200 | 🔄 If scope clarification needed |
| **Total** | **~1300** | |

### Run the project

```bash
docker compose up -d          # Start all services
# Frontend: http://localhost:3000
# Backend:  http://localhost:8000/docs
# DB:       postgresql://room:room@localhost:5432/room
```

### When done

1. `git add -A && git commit -m "feat(ids-integration): [summary]"`
2. `git push`
3. Create `H003--spec-ids.md` (or next in chain)
4. Update `INDEX.md`:
   - Set H002 → 📦 Archived
   - Add H003 row → ✅ Active
   - Update `current: H003`, `total_handoffs: 3`
5. Update `STATE.md`

---

## Git State

| | |
|-|-|
| Branch | `main` |
| Uncommitted | None |
| Last commit | `833128d` |
| Remote | `origin/main` (up to date) |
