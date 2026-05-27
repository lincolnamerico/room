---
title: "H00N: [stage name]"
handoff_id: H00N
handoff_chain_position: N
status: active
date: [ISO date]
author: [agent name]
next_agent: [next role]
next_stage: "[next milestone or feature]"
---

# H00N: [Stage Name]

> Handoff #N da cadeia. [1-sentence summary of what was done].

---

## Context Snapshot

| Field | Value |
|-------|-------|
| Project | Room |
| Feature | [feature name] |
| Stage | [Specify / Design / Tasks / Execute] |
| Branch | `[branch name]` |
| Last Commit | `[hash]` — `[message]` |

---

## Completed ✓

- [x] [Item completed]
- [x] [Item completed]

## In Progress

- [ ] [Item in progress, if any]

## Pending / Next

1. [Next immediate step for the next agent]
2. [Following step]

---

## Files Changed

| File | Change |
|------|--------|
| `path/to/file.ext` | [summary of change] |

---

## Relevant Decisions

| ID | Decision | Impact |
|----|----------|--------|
| AD-NNN | [decision] | [impact] |

See STATE.md for full decision records.

---

## Blockers

| ID | Description | Impact | Workaround |
|----|-------------|--------|------------|
| B-NNN | [desc] | [impact] | [workaround] |

---

## Git State

| | |
|-|-|
| Branch | `[branch]` |
| Uncommitted | [files] |
| Last commit | `[hash]` |
| Remote | `origin [url]` |

---

## Next Agent: Exact Instructions

### Load this

- `H00N--*.md` (this file) — mandatory
- `INDEX.md` — chain position
- Feature-specific files listed below

### Do this

```bash
[exact commands to run]
```

### Done when

- [Verification criteria 1]
- [Verification criteria 2]

### Then create

- `H0NN--next-stage.md`
- Update `INDEX.md`:
  - Set H00N → 📦 Archived
  - Add H0NN → ✅ Active
  - Update `current` and `total_handoffs`

---

## Token Budget

| File | Tokens | Required? |
|------|--------|-----------|
| This file | ~250 | ✅ Yes |
| INDEX.md | ~100 | ✅ Yes |
| [other file] | ~N | 🔄 If relevant |
| **Total** | **~N** | |
