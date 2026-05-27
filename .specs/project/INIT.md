---
title: Room Project Initialization
type: initialization-record
version: 1
date: 2026-05-27
status: active
agents: this document captures the full genesis of the project — use it to understand context, decisions, and requirements before starting any feature work
skills: tlc-spec-driven
---

# Room — Initialization Record

> Documento de fundação do projeto. Contém o registro completo da sessão
> inicial de descoberta, perguntas e respostas, justificativas técnicas,
> e os próximos passos. **Todo agente ou skill que atuar neste projeto
> deve ler este documento primeiro** para entender o contexto completo.

---

## 1. Session Overview

| Field | Value |
|-------|-------|
| Date | 2026-05-27 |
| Facilitator | DeepSeek (via opencode) |
| Workflow | Spec-Driven Development (tlc-spec-driven) |
| Project | Room |
| Status | Initialized (greenfield) |

---

## 2. Project Genesis (Q&A Record)

### 2.1 What is being built?

> "Um site que funciona como uma Sala de Situação em Saúde do Município,
> apresentando painéis de indicadores de saúde baseados em:
> a) produção local (via prontuário de saúde utilizado pelas Unidades Básicas de Saúde);
> b) consolidação de indicadores já organizados pela Secretaria Estadual de Saúde do Paraná - SESA/PR;
> c) consolidação de indicadores já organizados pelo Ministério da Saúde.
> Sendo possível que todos esses indicadores permitam a consulta em diferentes
> níveis de agregação (município, bairro, microárea, etc.)."

### 2.2 Who is it for?

> "Cidadão de qualquer parte do território, usuário comum, pesquisadores,
> gestores de saúde, profissionais, auditores, conselheiros municipais de saúde,
> profissionais que atuam no controle social, controle externo, controle interno
> do Município, jornalistas."

**User personas identified:**

| Persona | Need |
|---------|------|
| Cidadão comum | Acesso transparente a indicadores de saúde do seu território |
| Gestor municipal | Tomada de decisão baseada em dados consolidados |
| Pesquisador | Extração e exportação de dados para análise |
| Profissional de saúde | Acompanhamento de indicadores da sua região de atuação |
| Auditor / Controle interno | Verificação e validação de indicadores |
| Conselheiro municipal | Fiscalização e participação social |
| Jornalista | Reportagem baseada em dados públicos |

### 2.3 What problem does it solve?

> **Visualização integrada** — centralizar indicadores de saúde dispersos em
> múltiplas fontes (IDS produção local, SESA/PR, MS, IBGE, Fiocruz, etc.)
> em uma única plataforma com consulta em múltiplos níveis territoriais.

### 2.4 Core requirements (extracted verbatim)

> "Todo o ciclo de construção, integração, interoperabilidade, consulta,
> importação, exportação, extração, salvamento em diferentes formatos
> e demais rotinas de leitura e acesso possam ser executadas por
> **homens e máquinas**."

### 2.5 Scope v1

> "Múltiplos níveis, iniciando com produção local (via software da Empresa IDS)
> com integração de fontes de dados externas (SESA/PR, MS, IBGE, e demais Bases
> Temáticas mantidas por diferentes Entes Governamentais, como Fiocruz, etc.)."

### 2.6 Constraints

> Nenhuma restrição crítica declarada (prazo, técnica ou orçamento).

---

## 3. Tech Stack — Recommendation & Decision

### 3.1 Decision record

| Decision | Chosen | Rationale | Alternatives considered | Date |
|----------|--------|-----------|------------------------|------|
| D-001 | Next.js + TypeScript | Framework React moderno com SSR, tipagem segura | Create React App, Vue, Svelte | 2026-05-27 |
| D-002 | ECharts + Leaflet | ECharts: visualização de dados rica; Leaflet: mapas leves e flexíveis | Recharts, D3.js, MapLibre, Google Maps | 2026-05-27 |
| D-003 | Tailwind CSS | Estilização rápida e consistente | CSS Modules, Styled Components | 2026-05-27 |
| D-004 | FastAPI (Python) | Performance, tipagem automática, OpenAPI nativo, ecossistema Python para dados | Node.js/Express, Django REST, Flask | 2026-05-27 |
| D-005 | PostgreSQL + PostGIS | Dados georreferenciados, consultas espaciais nativas, maturidade | MySQL, MongoDB, SQLite | 2026-05-27 |
| D-006 | Python (pandas, SQLAlchemy, httpx) | Ecossistema dominante para ETL e integração com dados governamentais | Node.js, Go, R | 2026-05-27 |
| D-007 | API REST + OpenAPI | Documentação automática, geração de clientes, padrão amplo | GraphQL, gRPC | 2026-05-27 |

### 3.2 Complete stack diagram

```
┌────────────────────────────────────────────────────┐
│                   FRONTEND                         │
│  Next.js + TypeScript + Tailwind CSS               │
│  ECharts (gráficos) + Leaflet (mapas)              │
└────────────────┬───────────────────────────────────┘
                 │ HTTP/REST
┌────────────────▼───────────────────────────────────┐
│                   BACKEND                          │
│  FastAPI (Python) + OpenAPI/Swagger                │
│  pandas + SQLAlchemy + httpx                       │
│  Formatos: CSV, JSON, XLSX, PDF, GeoJSON           │
└────────────────┬───────────────────────────────────┘
                 │ SQL + PostGIS
┌────────────────▼───────────────────────────────────┐
│                   DATABASE                         │
│  PostgreSQL + PostGIS                              │
└────────────────────────────────────────────────────┘
                 ▲
   ┌─────────────┼─────────────┐
   │             │             │
   ▼             ▼             ▼
 Produção     SESA/PR      MS + IBGE
 Local IDS   (API/Site)   (Datasus)  + Fiocruz
```

---

## 4. Architectural Principles

Extracted from requirements and decisions:

1. **API-first** — Toda funcionalidade deve estar disponível via API REST,
   permitindo consumo por humanos (UI) e máquinas (scripts, integrações)
2. **Separation of concerns** — Frontend (Next.js) e backend (FastAPI) como
   projetos independentes comunicando via HTTP
3. **Data sovereignty** — Cada fonte de dados mantém seu pipeline de ETL
   independente; dados são normalizados no banco central
4. **Exportability** — Todo dado consultável deve ser exportável em pelo
   menos um formato padrão (CSV, JSON, XLSX)
5. **Multi-level query** — Toda consulta deve suportar filtro por nível
   territorial (município → bairro → microárea)
6. **Open by default** — API documentada e acessível; dados públicos
   exceto onde houver restrição legal

---

## 5. Feature Roadmap Summary

| Milestone | Description | Status |
|-----------|-------------|--------|
| M1 | Fundação (setup Next.js + FastAPI + PostGIS + CI) | Pending |
| M2 | Integração produção local (UBS/IDS) — ETL + API + painéis | Pending |
| M3 | Integração fontes externas (SESA/PR, MS, IBGE, Fiocruz) | Pending |
| M4 | Visualização e interação (mapas, gráficos, filtros) | Pending |
| M5 | Exportação e API pública (formatos + auth) | Pending |

Full details in [ROADMAP.md](./ROADMAP.md).

---

## 6. Next Steps (suggested)

### Immediate (top priority)

1. **Setup do repositório** — Inicializar monorepo com frontend e backend
2. **Feature: Produção Local (M2)** — Começar pela fonte de dados mais
   crítica e controlada pelo município
3. **Modelagem de dados** — Definir schema inicial de indicadores e níveis
   territoriais

### Short-term

4. **Conector SESA/PR** — Integrar segunda fonte de dados
5. **Painéis básicos** — ECharts + Leaflet com dados reais

### Technical setup needed

6. Definir estrutura do repositório (monorepo com `apps/` e `packages/`)
7. Docker Compose para ambiente local (PostgreSQL + PostGIS + apps)
8. CI básico (lint, testes, build)
9. Autenticação (JWT simples para v1)

---

## 7. Context Loading Strategy (for Agents and Skills)

> **Regra de ouro:** Sempre começar pelo handoff atual, não pelo INIT.md.
> O handoff contém o contexto mínimo necessário. Só carregue INIT.md
> se precisar do genesis completo.

```markdown
<!-- INSTRUCTION FOR AGENTS -->

### Priority order for loading context

1️⃣ **Load handoff first** (`.specs/handoffs/INDEX.md` + current `HXXX--*.md`)
   → Contains: what was done, what's next, git state, token budget
   → Typical cost: ~300-500 tokens

2️⃣ **Load STATE.md** (`.specs/project/STATE.md`)
   → Contains: active decisions, blockers, lessons
   → Load "Decisions" section only if relevant to the task

3️⃣ **Load feature-specific files** (`.specs/features/[feature]/*.md`)
   → Only if you're working on that specific feature

4️⃣ **Load INIT.md only when**:
   - You're the very first agent (no handoff chain exists yet)
   - You need to understand WHY a decision was made (not just WHAT)
   - Architectural principles are being challenged

### When NOT to load

- ❌ Archived handoffs (they're history, not context)
- ❌ PROJECT.md (unless you need stack details)
- ❌ ROADMAP.md (unless you're planning milestones)
- ❌ Full INIT.md on every session (use handoff instead)

### Handoff cycle enforcement

Every agent MUST end its work by:
1. Committing all changes to git
2. Pushing to GitHub
3. Creating the next handoff file
4. Updating INDEX.md
5. Updating STATE.md "Current Work"

This guarantees the chain is always observable and the next agent
starts with minimal context.

<!-- END INSTRUCTION FOR AGENTS -->
```

---

## 8. Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1 | 2026-05-27 | DeepSeek (opencode) | Initial project initialization session |
