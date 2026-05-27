---
title: "H001: Project Initialization"
handoff_id: H001
handoff_chain_position: 1
status: active
date: 2026-05-27
author: DeepSeek (via opencode)
next_agent: First development agent
next_stage: Milestone 1 — Setup (repo, CI, Docker)
---

# H001: Project Initialization

> Handoff #1 da cadeia. Projeto Room inicializado com estrutura SDD.
> Este handoff contém tudo que o próximo agente precisa para começar
> a trabalhar sem carregar o histórico completo da conversa.

---

## Context Snapshot

| Field | Value |
|-------|-------|
| Project | Room — Sala de Situação em Saúde do Município |
| Workflow | Spec-Driven Development (tlc-spec-driven skill) |
| Stack | Next.js + TypeScript + Tailwind CSS + ECharts + Leaflet (FE) |
| | FastAPI + Python + pandas + SQLAlchemy (BE) |
| | PostgreSQL + PostGIS (DB) |
| Repository | Fresh (greenfield), no files yet |

---

## Completed ✓

- [x] Project vision and scope defined
- [x] Tech stack recommended and approved
- [x] 5 milestones defined in ROADMAP.md
- [x] State management structure created (STATE.md)
- [x] Handoff chain architecture created (this file + INDEX.md)
- [x] Architectural principles established (API-first, multi-level query, etc.)

---

## Files Created (committed to .specs/)

| File | Purpose | Load for next agent? |
|------|---------|---------------------|
| `.specs/project/INIT.md` | Full genesis Q&A + decisions + principles | **No** (too large, use this handoff instead) |
| `.specs/project/PROJECT.md` | Vision, goals, stack, scope | Yes — but only if architectural detail needed |
| `.specs/project/ROADMAP.md` | 5 milestones + tasks | Yes — reference for what to build |
| `.specs/project/STATE.md` | Decisions, blockers, todos | Yes — check for blockers |
| `.specs/handoffs/INDEX.md` | Handoff chain central index | Yes — always load |
| `.specs/handoffs/H001--init.md` | ← This file | **Yes — mandatory** |

---

## Next Agent: Exact Instructions

### What to do

```
Milestone 1 — Foundation (Setup)
───────────────────────────────
1. Initialize git repo (if not already)
2. Create .gitignore (Node + Python + Docker)
3. Scaffold project structure:
   room/
   ├── frontend/          ← Next.js + TypeScript
   ├── backend/           ← FastAPI (Python)
   ├── database/          ← Migration scripts
   └── docker/            ← Docker Compose
4. Docker Compose with PostgreSQL + PostGIS
5. CI pipeline (GitHub Actions): lint + test + build
6. Commit and push to GitHub
```

### Token budget for your session

| Load this | Tokens | Why |
|-----------|--------|-----|
| `H001--init.md` (this file) | ~300 | Context for what to do |
| `INDEX.md` | ~100 | Chain position |
| `ROADMAP.md` (Milestone 1 section only) | ~50 | Task list |
| `STATE.md` | ~200 | Active decisions/blockers |
| **Total** | **~650** | Stay under 1k |

**Do NOT load:** INIT.md, PROJECT.md, old handoff files.

### When done

1. `git add -A`
2. `git commit -m "feat(setup): scaffold project structure + CI + Docker"`
3. `git push`
4. Create `H002--setup.md` following the same template
5. Update `INDEX.md`:
   - Set H001 status → 📦 Archived
   - Add H002 row → ✅ Active
   - Update `current: H002`, `total_handoffs: 2`
6. Update `STATE.md` "Current Work" field

---

## Git State

| | |
|-|-|
| Branch | `main` (to be created) |
| Uncommitted | `.specs/` directory contents |
| GitHub | Not yet configured |

---

## Relevant Decisions (from STATE.md)

| ID | Decision | Impact |
|----|----------|--------|
| AD-001 | Next.js + FastAPI + PostgreSQL/PostGIS | Two separate apps, Docker Compose |
| AD-002 | SDD workflow (tlc-spec-driven) | All work flows through .specs/ artifacts |

---

## Blockers

None.

---

## Lessons from This Session

1. **Document decisions as they happen**, not after — STATE.md captures rationale fresh
2. **Handoff file is the context carrier** — next agent loads only the handoff, not the entire history
3. **Version in frontmatter** — `INIT.md` has version: 1, enabling change detection
