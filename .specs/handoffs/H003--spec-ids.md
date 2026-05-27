---
title: "H003: M2 — Specify: Integração Produção Local (UBS/IDS)"
handoff_id: H003
handoff_chain_position: 3
status: active
date: 2026-05-27
author: DeepSeek (via opencode)
next_agent: Feature agent (Specify → Discuss)
next_stage: M2 — Discuss: resolver áreas cinzentas do IDS
---

# H003: M2 — Specify: IDS Integration

> Handoff #3 da cadeia. Spec da M2 criado com contexto de Pinhais, modelo territorial e indicadores iniciais. Próximo passo: Discuss para resolver áreas cinzentas.

---

## Context Snapshot

| Field | Value |
|-------|-------|
| Project | Room |
| Feature | M2 — Integração produção local (UBS/IDS) |
| Stage | Specify (spec.md created) |
| Branch | `main` |
| Last Commit | `0d628c9` — docs(session): end session 1 with HANDOFF.md checkpoint |

---

## Completed ✓

- [x] Contexto de Pinhais capturado: 12 UBS, bairros com territorialização N:N
- [x] Modelo territorial definido: Município → Bairro (N:N UBS) → Microárea
- [x] Indicadores iniciais: Consultas, Visitas ACS, Exames
- [x] Periodicidade: diária | Dados: sumarizados (agregados)
- [x] IDS em nuvem, contato de suporte disponível para investigação
- [x] `spec.md` criado com stories P1 (ETL + API multi-nível + Painéis), P2 (painéis), P3 (exportação)
- [x] Gray areas identificadas para Discuss

## In Progress

- Nothing. Aguardando Discuss.

## Pending / Next

1. **Discuss** — Resolver áreas cinzentas com o usuário:
   - Mecanismo de integração com IDS (API? DB? Export?)
   - Catálogo completo de indicadores
   - Modelagem territorial (N:N UBS-bairro no banco)
   - Janela de execução do ETL diário
2. **Design** — Arquitetura dos conectores e schemas
3. **Tasks** — Desdobramento em tarefas atômicas
4. **Execute** — Implementação

---

## Files Changed

| File | Change |
|------|--------|
| `.specs/features/ids-integration/spec.md` | Created — full specification for M2 |

---

## Relevant Decisions

| ID | Decision | Impact |
|----|----------|--------|
| AD-003 | Alvo: Pinhais — 12 UBS | Dados reais de município concreto |
| AD-004 | Modelo territorial hierárquico com N:N UBS-bairro | DB schema precisa suportar relação many-to-many |
| AD-005 | ETL diário com dados sumarizados | Pipeline batch, sem dados sensíveis |
| AD-006 | IDS em nuvem + contato de suporte | Mecanismo de integração TBD na Discuss |

See STATE.md for full decision records.

---

## Blockers

None.

---

## Git State

| | |
|-|-|
| Branch | `main` |
| Uncommitted | `.specs/features/` (new) |
| Last commit | `0d628c9` |
| Remote | `origin/main` (up to date) |

---

## Next Agent: Exact Instructions

### Load these (in order)

1. `HANDOFF.md` — session checkpoint (first)
2. `INDEX.md` — chain position
3. `H003--spec-ids.md` (this file) — context
4. `features/ids-integration/spec.md` — the specification
5. `STATE.md` — decisions and blockers

### What to do next

```
M2 — Discuss (Specify → Discuss)
─────────────────────────────────
1. Present the gray areas from spec.md to the user:
   a. Mecanismo de integração com IDS
   b. Catálogo completo de indicadores
   c. Modelagem territorial (N:N UBS-bairro)
   d. Janela de execução do ETL diário

2. For each area, ask concrete questions with options
3. Scope guardrail: discuss HOW, never WHAT (no new features)
4. Write context.md with implementation decisions
5. Proceed to Design if approved
```

### Run the project (if needed for testing)

Não necessário para Discuss — fase de especulação.

### Done when

- [ ] `features/ids-integration/context.md` created with decisions
- [ ] User approved context.md
- [ ] Ready for Design phase

### Then create

- `H004--design-ids.md` (or next in chain)
- Update `INDEX.md`:
  - Set H003 → 📦 Archived
  - Add H004 → ✅ Active
  - Update `current` and `total_handoffs`

---

## Token Budget

| File | Tokens | Required? |
|------|--------|-----------|
| This file | ~300 | ✅ Yes |
| INDEX.md | ~100 | ✅ Yes |
| `features/ids-integration/spec.md` | ~300 | ✅ Yes |
| STATE.md | ~250 | ✅ Yes |
| **Total** | **~950** | |
