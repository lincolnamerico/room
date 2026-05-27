# Room — State

## Session: 2026-05-27 (Session 2 — Ended)

**Status:** ✅ Paused (ready for Session 3)
**Current focus:** Milestone 2 — Specify: Integração produção local (UBS/IDS)
**Handoff:** H003 (`.specs/handoffs/H003--spec-ids.md`) — ✅ Active
**Session handoff:** `.specs/HANDOFF.md`
**Resume trigger:** "Continuar projeto Room. Carregar handoff de .specs/HANDOFF.md"

## Decisions

| # | Decision | Rationale | Date |
|---|----------|-----------|------|
| 1 | Stack: Next.js + FastAPI + PostgreSQL/PostGIS | Frontend moderno + backend Python para dados + dados georreferenciados | 2026-05-27 |
| 2 | SDD workflow (tlc-spec-driven) | Rastreabilidade e adaptação por complexidade | 2026-05-27 |
| 3 | Alvo territorial: Pinhais — 12 UBS | Primeiro município concreto, com territorialização definida pela SMS | 2026-05-27 |
| 4 | Modelo territorial: Município → Bairro (N:N UBS) → Microárea | Relação N:N entre bairro e UBS conforme territorialização de Pinhais | 2026-05-27 |
| 5 | Periodicidade diária para ETL | Atualização diária dos indicadores | 2026-05-27 |
| 6 | Dados sumarizados (agregados) | Sem dados individuais/paciente — apenas totais, médias e agregados | 2026-05-27 |
| 7 | Indicadores iniciais: Consultas, Visitas ACS, Exames | Definição inicial; catálogo será expandido na Discuss com contato IDS | 2026-05-27 |
| 8 | IDS roda em nuvem, contato de suporte disponível | Mecanismo de integração será investigado na Discuss | 2026-05-27 |

## Blockers

None.

## Lessons

| # | Lesson | Context | Date |
|---|--------|---------|------|
| L-001 | PAT token precisa do escopo `workflow` para commitar CI files | Push rejeitado ao tentar enviar `.github/workflows/ci.yml` | 2026-05-27 |
| L-002 | setuptools flat-layout conflita com `app/` e `migrations/` juntos | Adicionado `[tool.setuptools.packages.find]` com `include = ["app*"]` | 2026-05-27 |
| L-003 | Handoff chain precisa ser o primeiro arquivo lido pelo próximo agente | HANDOFF.md na raiz `.specs/` serve como checkpoint de sessão | 2026-05-27 |
| L-004 | Ao encerrar sessão, gerar todos os artefatos: STATE.md + H00N + INDEX.md + HANDOFF.md + commit + push | Sessão 2 finalizada seguindo o ciclo completo do handoff chain | 2026-05-27 |

## Deferred Ideas

- [ ] Avaliar necessidade de configurar git user.name e user.email globalmente (commits atuais usaram valores automáticos)
- [ ] Investigar se `AGENTS.md` e `CLAUDE.md` gerados pelo create-next-app são úteis ou podem ser removidos
- [ ] Planejar licença do projeto (MIT? Pública?)

## Todo

- [x] Milestone 1 — Foundation (Setup)
- [ ] Milestone 2 — Specify: Integração produção local (UBS/IDS)
  - [x] spec.md criado
  - [ ] Discuss: resolver áreas cinzentas (integração IDS, catálogo indicadores, modelagem territorial)
  - [ ] Design: arquitetura dos conectores e schemas
  - [ ] Tasks: desdobramento em tarefas atômicas
  - [ ] Execute: implementação

## References

- INIT.md v1 — Full initialization record with Q&A, decisions, principles, and next steps
- `features/ids-integration/spec.md` — Specification for M2

## Preferences

- Tlc-spec-driven skill loaded for SDD workflow
- User prefers stack recommendation over pre-defined choices
- Session handoff procedure: sempre finalizar com STATE.md + H00N + INDEX.md + HANDOFF.md + commit + push
