# IDS Integration — Produção Local UBS

## Problem Statement

Os dados de produção das Unidades Básicas de Saúde (UBS) de Pinhais — consultas, visitas de Agentes Comunitários de Saúde (ACS), exames e demais procedimentos — estão registrados no sistema IDS Saúde, mas não há uma interface pública consolidada que permita consulta, cruzamento e visualização desses indicadores em múltiplos níveis territoriais. Gestores, conselheiros, pesquisadores e cidadãos não têm acesso integrado a esses dados hoje.

## Goals

- [ ] Modelar e persistir indicadores de produção local em banco georreferenciado (PostgreSQL + PostGIS) com granularidade diária
- [ ] Disponibilizar API REST para consulta dos indicadores por nível territorial (município, UBS, bairro, microárea)
- [ ] Criar pipeline ETL diário para extração dos dados do sistema IDS
- [ ] Exibir painéis básicos com os indicadores no frontend

## Out of Scope

| Item | Razão |
|------|-------|
| Dados individuais de pacientes (nominais) | Apenas dados sumarizados/agregados |
| Integração com outras fontes (SESA/PR, MS, IBGE) | Será M3 |
| Autenticação e controle de acesso | Será M5 |
| Alertas automáticos | Post-v1 |
| Dados em tempo real (real-time) | Batch diário é suficiente |

---

## Territorial Model

O município de Pinhais adota territorialização com relação N:N entre bairros e UBS:

```
Município (Pinhais)
  └── Bairro (ex: Vila das Pinhais)
        └── UBS (ex: UBS Central) — uma UBS pode atender parte de um bairro
              └── Microárea (território do ACS)
```

- Um **bairro** pode ser atendido por 1 ou mais UBS
- Uma **UBS** atende 1 ou mais bairros (parcial ou integralmente)
- A **microárea** é a unidade territorial mínima (território de um ACS)

---

## User Stories

### P1: Extrair e armazenar indicadores ⭐ MVP

**User Story**: Como gestor municipal, quero que os indicadores de produção local sejam extraídos do IDS e armazenados diariamente no banco do Room para que estejam disponíveis para consulta.

**Why P1**: Sem dados não há painel. É a fundação da feature.

**Acceptance Criteria**:

1. WHEN o pipeline ETL executar THEN o sistema SHALL extrair os indicadores configurados do IDS e inserir/atualizar no banco PostgreSQL
2. WHEN a extração for bem-sucedida THEN o sistema SHALL registrar timestamp da última atualização
3. WHEN a extração falhar THEN o sistema SHALL registrar erro sem interromper execuções futuras
4. WHEN o pipeline executar novamente THEN o sistema SHALL fazer upsert (não duplicar registros do mesmo período/unidade)

**Independent Test**: Executar o pipeline ETL e verificar os registros inseridos na tabela de indicadores.

---

### P1: Consultar indicadores por nível territorial ⭐ MVP

**User Story**: Como cidadão ou gestor, quero consultar os indicadores de produção local filtrando por município, UBS, bairro ou microárea para visualizar dados do meu território de interesse.

**Why P1**: A consulta multi-nível é o core do Room.

**Acceptance Criteria**:

1. WHEN eu consultar indicadores por município THEN a API SHALL retornar os dados agregados de Pinhais
2. WHEN eu consultar indicadores por UBS THEN a API SHALL retornar os dados da unidade específica
3. WHEN eu consultar indicadores por bairro THEN a API SHALL retornar os dados consolidados do bairro (incluindo múltiplas UBS se aplicável)
4. WHEN eu consultar indicadores por microárea THEN a API SHALL retornar os dados da área do ACS
5. WHEN eu filtrar por período (data início/fim) THEN a API SHALL retornar apenas registros no intervalo
6. WHEN a consulta não encontrar registros THEN a API SHALL retornar array vazio (status 200), não erro

**Independent Test**: Chamar `GET /api/indicators?ubs_id=1&start=2026-01-01` e verificar retorno com dados.

---

### P2: Painéis básicos de produção local

**User Story**: Como cidadão, quero visualizar os indicadores de produção local em gráficos e tabelas no navegador para acompanhar a evolução dos serviços de saúde.

**Why P2**: O valor do projeto está na visualização, mas depende da API estar pronta primeiro.

**Acceptance Criteria**:

1. WHEN eu acessar a página de produção local THEN o sistema SHALL exibir um dashboard com indicadores (consultas, visitas ACS, exames) por mês
2. WHEN eu selecionar uma UBS no filtro THEN o sistema SHALL atualizar os gráficos para aquela unidade
3. WHEN eu selecionar um bairro no filtro THEN o sistema SHALL atualizar os gráficos para aquele bairro (agregando UBS se necessário)

**Independent Test**: Abrir o dashboard, selecionar UBS, ver gráficos atualizarem.

---

### P3: Exportar indicadores

**User Story**: Como pesquisador, quero exportar os indicadores consultados em CSV ou JSON para análise em ferramentas externas.

**Why P3**: Útil, mas o core (visualização) é mais prioritário.

**Acceptance Criteria**:

1. WHEN eu solicitar exportação dos dados filtrados THEN o sistema SHALL gerar arquivo CSV com os registros
2. WHEN eu solicitar exportação em JSON THEN o sistema SHALL retornar array JSON com os mesmos dados

**Independent Test**: Filtrar indicadores, clicar em exportar, baixar CSV válido.

---

## Edge Cases

- WHEN não houver dados para o período selecionado THEN o sistema SHALL exibir "Nenhum dado disponível para o período"
- WHEN o pipeline ETL falhar por N dias consecutivos THEN o sistema SHALL notificar falha (log)
- WHEN o IDS estiver indisponível no momento da extração THEN o sistema SHALL tentar novamente em intervalo configurável (retry)
- WHEN houver dados parciais (alguns indicadores disponíveis, outros não) THEN o sistema SHALL armazenar os dados disponíveis e registrar warning para os faltantes

---

## Requirement Traceability

| ID | Story | Phase | Status |
|----|-------|-------|--------|
| IDS-01 | P1: Extrair e armazenar | Specify | Pending |
| IDS-02 | P1: Extrair e armazenar | Specify | Pending |
| IDS-03 | P1: Extrair e armazenar | Specify | Pending |
| IDS-04 | P1: Extrair e armazenar | Specify | Pending |
| IDS-05 | P1: Consultar por nível territorial | Specify | Pending |
| IDS-06 | P1: Consultar por nível territorial | Specify | Pending |
| IDS-07 | P1: Consultar por nível territorial | Specify | Pending |
| IDS-08 | P1: Consultar por nível territorial | Specify | Pending |
| IDS-09 | P1: Consultar por nível territorial | Specify | Pending |
| IDS-10 | P1: Consultar por nível territorial | Specify | Pending |
| IDS-11 | P2: Painéis básicos | Specify | Pending |
| IDS-12 | P2: Painéis básicos | Specify | Pending |
| IDS-13 | P2: Painéis básicos | Specify | Pending |
| IDS-14 | P3: Exportar | Specify | Pending |
| IDS-15 | P3: Exportar | Specify | Pending |

---

## Gray Areas (for Discuss phase)

Áreas que precisam de discussão com o usuário antes do Design:

1. **Mecanismo de integração IDS** — Como o IDS expõe os dados? (API? Banco? Exportação?)
2. **Catálogo de indicadores** — Quais indicadores exatos além de consultas, ACS, exames?
3. **Modelagem territorial** — Como representar a relação N:N entre UBS e bairro no banco?
4. **Frequência diária** — Janela ideal para execução do ETL? (madrugada?)
