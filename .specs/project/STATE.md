# Room — State

## Session: 2026-05-27 (Session 1 — Ended)

**Status:** ✅ Paused (ready for Session 2)
**Current focus:** Milestone 2 — Integração produção local (UBS/IDS) — Specify
**Handoff:** H002 (`.specs/handoffs/H002--setup.md`) — ✅ Active
**Session handoff:** `.specs/HANDOFF.md`
**Resume trigger:** "Continuar projeto Room. Carregar handoff de .specs/HANDOFF.md"

## Decisions

| # | Decision | Rationale | Date |
|---|----------|-----------|------|
| 1 | Stack: Next.js + FastAPI + PostgreSQL/PostGIS | Frontend moderno + backend Python para dados + dados georreferenciados | 2026-05-27 |
| 2 | SDD workflow (tlc-spec-driven) | Rastreabilidade e adaptação por complexidade | 2026-05-27 |

## Blockers

None.

## Lessons

| # | Lesson | Context | Date |
|---|--------|---------|------|
| L-001 | PAT token precisa do escopo `workflow` para commitar CI files | Push rejeitado ao tentar enviar `.github/workflows/ci.yml` | 2026-05-27 |
| L-002 | setuptools flat-layout conflita com `app/` e `migrations/` juntos | Adicionado `[tool.setuptools.packages.find]` com `include = ["app*"]` | 2026-05-27 |
| L-003 | Handoff chain precisa ser o primeiro arquivo lido pelo próximo agente | HANDOFF.md na raiz `.specs/` serve como checkpoint de sessão | 2026-05-27 |

## Deferred Ideas

- [ ] Avaliar necessidade de configurar git user.name e user.email globalmente (commits atuais usaram valores automáticos)
- [ ] Investigar se `AGENTS.md` e `CLAUDE.md` gerados pelo create-next-app são úteis ou podem ser removidos
- [ ] Planejar licença do projeto (MIT? Pública?)

## Todo

- [x] Milestone 1 — Foundation (Setup)
- [ ] Milestone 2 — Specify: Integração produção local (UBS/IDS)

## References

- INIT.md v1 — Full initialization record with Q&A, decisions, principles, and next steps

## Preferences

- Tlc-spec-driven skill loaded for SDD workflow
- User prefers stack recommendation over pre-defined choices
