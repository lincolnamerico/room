# Room — Sala de Situação em Saúde

**Vision:** Painéis interativos de indicadores de saúde pública do município, integrando dados de produção local (UBS), SESA/PR, Ministério da Saúde, IBGE e demais bases temáticas governamentais, com consulta em múltiplos níveis territoriais.
**For:** Cidadãos, pesquisadores, gestores municipais de saúde, profissionais de saúde, auditores, conselheiros municipais de saúde, controle social, controle interno e externo, jornalistas.
**Solves:** Dispersão de indicadores de saúde em fontes isoladas; dificuldade de consulta integrada em diferentes níveis de agregação territorial (município, bairro, microárea).

## Goals

- Centralizar indicadores de múltiplas fontes (produção local, SESA/PR, MS, IBGE, Fiocruz, etc.) em um único painel interativo
- Permitir consulta, exportação e extração de dados em múltiplos formatos (CSV, JSON, XLSX, PDF, GeoJSON)
- Disponibilizar API REST documentada para consumo por humanos e máquinas

## Tech Stack

**Frontend:**

- Framework: Next.js + TypeScript
- Visualização: ECharts + Leaflet (mapas)
- Estilo: Tailwind CSS

**Backend:**

- Framework: FastAPI (Python)
- Documentação: OpenAPI/Swagger automático

**Database:**

- Principal: PostgreSQL + PostGIS (dados georreferenciados)

**ETL / Data Pipeline:**

- Python (pandas, SQLAlchemy, httpx/requests)

**Formatação:**

- CSV, JSON, XLSX, PDF, GeoJSON

## Scope

**v1 includes:**

- Painéis de indicadores de produção local (via software IDS)
- Integração com fontes externas (SESA/PR, MS, IBGE, Fiocruz)
- Consulta em múltiplos níveis de agregação (município, bairro, microárea)
- API REST com exportação em CSV, JSON, XLSX
- Autenticação básica e controle de acesso por perfil

**Explicitly out of scope (v1):**

- App mobile nativo (será web responsivo)
- IA/ML preditivo
- Dashboards em tempo real (atualização batch)
- Integração com sistemas proprietários além do software IDS

## Constraints

- Timeline: A definir
- Technical: Dados provenientes de fontes governamentais com formatos e periodicidade variados
- Resources: A definir
