---
title: Handoff Chain Index
description: Central registry of all handoffs in the development cycle. Every step produces one entry.
total_handoffs: 1
current: H001
last_updated: 2026-05-27
---

# Handoff Chain Index

> Registro central de todos os handoffs. Cada etapa do desenvolvimento
> (Specify → Design → Tasks → Execute) produz **exatamente um handoff**.
> A corrente forma um grafo linear e observável do progresso do projeto.

## The Chain

| # | File | Stage | From | To | Date | Git Commit | Status |
|---|------|-------|------|----|------|------------|--------|
| 1 | [H001--init.md](./H001--init.md) | Project initialization | DeepSeek | Next agent | 2026-05-27 | — | ✅ Active |

## Legend

| Status | Meaning |
|--------|---------|
| ✅ Active | Current start point for next agent |
| 📦 Archived | Consumed by a subsequent handoff |
| 🔄 In Progress | Being worked on |
| ⏳ Pending | Not yet reached |

## How to Use This Chain

### For the next agent starting fresh

1. Open `INDEX.md` → find the row with status **✅ Active**
2. Open the corresponding handoff file (e.g., `H002--setup.md`)
3. The handoff file contains:
   - **Context snapshot**: what the project state is
   - **Completed work**: what was already done
   - **Next instruction**: exactly what the next agent must do
   - **Git state**: branch, last commit, pending changes
   - **Token budget**: which files to load (and which to skip) to stay lean
4. Do the work
5. Commit and push to GitHub
6. Create the next handoff file (e.g., `H003--xxx.md`)
7. Update `INDEX.md`:
   - Mark current handoff as 📦 Archived
   - Add new row as ✅ Active
   - Update `current` in frontmatter

### Context minimization rules

| Load | Skip |
|------|------|
| Previous handoff file (~200-400 tokens) | Full INIT.md (unless first time) |
| INDEX.md (~100 tokens) | Full PROJECT.md (unless needed) |
| Feature-specific files needed for the task | Old handoff files (archived) |
| STATE.md "Decisions" section only if relevant | Full ROADMAP.md (unless planning) |

**Target per new agent:** <1,000 tokens of context from `.specs/`.

---

## Chain Evolution

Handoffs are added sequentially. Branching (parallel tasks) is supported:
- Multiple handoffs with the same parent number indicate parallel work
- Merge handoff consolidates parallel branches
- Example: `H004a`, `H004b` → `H005` (merge)

---

## Git Workflow

```bash
# After completing a handoff:
git add .specs/handoffs/
git commit -m "handoff(H00N): [stage] — [summary]"
git push origin <branch>

# Update INDEX.md is always part of the handoff commit.
```
