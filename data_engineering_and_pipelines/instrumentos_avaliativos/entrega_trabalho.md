# Entrega de Trabalho (PBL) — Data Engineering and Pipelines

> Roteiro para elaboração com **Problem-Based Learning**.

- **Disciplina:** Data Engineering and Pipelines
- **Professor-conteudista:** Afonso Cesar Lelis Brandão

> O **CASE** existe para que o estudante entenda a aplicabilidade do conteúdo estudado na realidade do mercado de trabalho.

---

## 1. Título

**Da Planilha ao Pipeline — Projeto de uma Plataforma de Dados Ponta a Ponta para o E-commerce VemComprar em 9 Meses**

---

## 2. Desafio

> **O quê?** Um e-commerce brasileiro em rápido crescimento precisa **sair de um caos de planilhas e bancos transacionais isolados** e construir uma **plataforma de dados moderna e de ponta a ponta** — da ingestão ao BI — com governança, qualidade e LGPD, dentro de um orçamento e prazo definidos.
>
> **Quem?** A **VemComprar Comércio Digital S.A.**, marketplace e loja própria de moda, casa e eletrônicos, sediada em Barueri (SP), com 540 funcionários, faturamento (GMV) anual de **R\$ 480 milhões**, **2,3 milhões de pedidos/ano** e **3,8 milhões de clientes cadastrados**. Cresceu 140% em 24 meses e a infraestrutura de dados não acompanhou.
>
> **Quando?** Início imediato. Primeira entrega de valor (primeiros dashboards confiáveis sobre dados governados) em **3 meses**. Roadmap completo de **9 meses**.
>
> **Onde?** Operação 100% digital, com dados espalhados por: o **banco transacional do e-commerce** (PostgreSQL, plataforma VTEX/loja própria), o **ERP financeiro/fiscal** (TOTVS), o **CRM e ferramenta de e-mail marketing** (RD Station), a **plataforma de anúncios** (Google Ads + Meta Ads via API), o **gateway de pagamento** (Stripe/Pagar.me), a **transportadora/WMS** (planilhas e API dos Correios/transportadoras) e **dezenas de planilhas Google Sheets** mantidas manualmente por cada área.
>
> **Por quê?** A VemComprar **não tem data warehouse nem data lake**. Toda análise nasce de exportações manuais para Excel/Sheets, consolidadas a mão. **Indicadores atuais**:
>
> - **Nº de fontes de dados** relevantes e não integradas: **9** — bancos e ERP (PostgreSQL transacional + ERP TOTVS), APIs de terceiros (RD Station, Google Ads, Meta Ads, gateway de pagamento, transportadora/Correios), planilhas e WMS.
> - **Volume de dados:** ~**1,8 TB** acumulados; o transacional cresce **~6 GB/dia** (pedidos, eventos de navegação, logs).
> - **Tempo para fechar o relatório gerencial mensal:** **5 dias úteis** de trabalho manual de 2 analistas (consolidação de 30+ planilhas).
> - **Divergência entre fontes:** o faturamento do **ERP** e o do **e-commerce** divergem em **até 7%** todo mês — ninguém sabe qual está certo.
> - **Custo de retrabalho/consolidação manual:** 2 analistas × ~60 h/mês × R\$ 60/h = **R\$ 7,2 mil/mês = R\$ 86,4 mil/ano**, sem contar decisões atrasadas.
> - **Frescor dos dados de marketing:** o ROAS por campanha só é conhecido **com 4 dias de atraso** — verba é queimada em campanha ruim antes de alguém perceber.
> - **Incidentes de "número errado em reunião":** **~3 por mês**, gerando refação de relatório e perda de confiança da diretoria nos dados.
> - **LGPD:** dados pessoais de 3,8 milhões de clientes (CPF, e-mail, endereço, histórico de compra) circulam **em planilhas sem controle de acesso nem mascaramento** — risco regulatório direto.
>
> A VemComprar **não tem engenheiro de dados** — dos 540 funcionários, o time de dados é minúsculo: **apenas 2 analistas de BI e 1 DBA**. **Não tem orquestração, testes de dados, catálogo, linhagem nem observabilidade.** A diretoria aprovou um **investimento máximo de R\$ 900 mil** (CAPEX + 9 meses de OPEX de nuvem e ferramentas) para resolver o problema de uma vez.
>
> **Sua missão como engenheiro(a) de dados:** projetar uma **plataforma de dados completa e defensável**, de ponta a ponta — **ingestão → armazenamento (DW/Lakehouse) → transformação → orquestração → qualidade/observabilidade → governança/LGPD → BI** —, integrando os conceitos das 4 unidades da disciplina, com **arquitetura desenhada, stack justificada, orçamento realista (R\$) e cronograma de 9 meses**, e KPIs mensuráveis de sucesso.

---

## 3. Fontes de pesquisa

O estudante deverá pesquisar como outros profissionais ou empresas resolveram desafios similares:

1. **Material da disciplina** — todas as 16 aulas das 4 unidades (fundamentos; ingestão/processamento; armazenamento/arquitetura; qualidade/governança/DataOps).
2. **Reis, J. & Housley, M. — *Fundamentals of Data Engineering* (O'Reilly, 2022)** — ciclo de vida da engenharia de dados e undercurrents (segurança, governança, orquestração).
3. **Kimball, R. & Ross, M. — *The Data Warehouse Toolkit* (3ª ed., Wiley)** — modelagem dimensional, fato/dimensão, esquema estrela.
4. **Lei Geral de Proteção de Dados — Lei nº 13.709/2018 (LGPD)** e materiais da **ANPD** — https://www.gov.br/anpd/ (bases legais, minimização, direitos do titular, anonimização/pseudonimização).
5. **Documentação oficial das ferramentas da Modern Data Stack** — dbt (https://docs.getdbt.com/), Apache Airflow (https://airflow.apache.org/docs/), Great Expectations (https://docs.greatexpectations.io/), Airbyte (https://docs.airbyte.com/), BigQuery/Snowflake.
6. **Moses, B. et al. — *Data Quality Fundamentals* / blog Monte Carlo** — os 5 pilares de observabilidade e a fórmula de data downtime.
7. **DAMA-DMBOK** — dimensões de qualidade de dados e fundamentos de governança e catálogo.
8. **Casos públicos brasileiros de plataforma de dados** — engenharia de dados do **Nubank, iFood, Magazine Luiza/Luizalabs, QuintoAndar** (blogs de engenharia, palestras em conferências, vídeos no YouTube) — referências reais de Modern Data Stack em escala nacional.

**Aulas relacionadas:** todas as 16 aulas são insumo. Em ordem de relevância para o case: **Aula 5** (ETL vs ELT, CDC, idempotência), **Aula 9/10** (Data Warehouse e modelagem dimensional), **Aula 8** (orquestração com Airflow), **Aula 6** (Spark/processamento), **Aula 7** (Kafka/streaming), **Aula 11/12** (lakehouse, nuvem e formatos), **Aula 13** (qualidade e observabilidade), **Aula 14–16** (contratos de dados, governança, catálogo/linhagem e DataOps).

---

## 4. Entregável e distribuição da pontuação

**Formato da entrega:** **Documento técnico** em PDF (entre 12 e 18 páginas) **+ diagrama de arquitetura** da plataforma + **apresentação executiva** em slides (entre 10 e 15 slides) para defesa perante banca simulada (diretoria fictícia da VemComprar).

**Pontuação:**

- **20%** — **Diagnóstico do estado atual e dor prioritária:** mapeamento das 9 fontes, do fluxo manual e dos riscos (incl. LGPD), classificação da maturidade de dados e definição **fundamentada** do problema a atacar primeiro, com **impacto financeiro mensurável**.
- **25%** — **Arquitetura de referência da plataforma:** diagrama ponta a ponta (ingestão → armazenamento → transformação → orquestração → BI), camadas (staging/raw → core → marts; ou bronze/silver/gold), escolha entre DW vs Lakehouse e **modelagem dimensional** (fatos e dimensões) das tabelas analíticas centrais.
- **20%** — **Stack tecnológica justificada:** cada ferramenta escolhida com **trade-offs explícitos** (ETL vs ELT, batch vs streaming/CDC, custo, time-to-value, lock-in), incluindo ingestão, transformação, orquestração, qualidade e BI.
- **15%** — **Qualidade, observabilidade e governança/LGPD:** dimensões e testes de dados, 5 pilares de observabilidade, contratos de dados, catálogo/linhagem, controle de acesso, mascaramento/anonimização de PII e bases legais LGPD.
- **10%** — **Orçamento e cronograma de 9 meses:** fases, custos detalhados (CAPEX + OPEX) dentro do limite de **R\$ 900 mil**, e plano de implantação por fase com governança do projeto.
- **10%** — **KPIs, riscos/mitigações e visão de futuro:** metas mensuráveis (antes/depois), análise crítica de riscos e evolução de 12–24 meses da plataforma.

**Critérios qualitativos transversais** (afetam todas as notas):

- **Clareza** e organização do texto e do diagrama de arquitetura.
- **Profundidade técnica** (decisões justificadas, não jargão solto).
- **Realismo** dos números (custos de nuvem, prazos, ROI).
- **Coerência interna** (diagnóstico → arquitetura → stack → KPIs alinhados).
- **Integração** dos conceitos das 4 unidades (não tratar uma unidade só).

---

## 5. Solução

> **Atenção:** este tópico será removido antes do case ser disponibilizado ao aluno — é apenas para o professor tutor que corrigirá.

**Diagnóstico esperado:** a VemComprar está em **maturidade de dados baixa** — estágio "planilha-cêntrico": dados existem em volume, mas sem integração, sem fonte única da verdade, sem governança e com risco LGPD ativo. Não há separação entre OLTP (transacional) e OLAP (analítico) — analistas exportam direto da produção, o que é frágil e lento. A **dor prioritária** esperada é a **ausência de uma fonte única da verdade governada**: a divergência de até 7% entre ERP e e-commerce é o sintoma mais caro (mina a confiança da diretoria) e tudo o mais decorre dela.

**Impacto financeiro da dor (cálculo esperado):** retrabalho manual R\$ 86,4 mil/ano + verba de mídia mal alocada por ROAS atrasado (estimável em **R\$ 200–400 mil/ano** sobre orçamento de mídia) + decisões atrasadas/erradas (custo de oportunidade) + **risco LGPD** (multa de até 2% do faturamento, limitada a R\$ 50 mi por infração — exposição relevante). O "custo da não-plataforma" supera com folga o investimento de R\$ 900 mil já no primeiro ano.

**Arquitetura de referência esperada (Modern Data Stack, ponta a ponta):**

1. **Ingestão (U2 — Aula 5):**
   - **EL gerenciado** com **Airbyte (open-source self-hosted)** ou **Fivetran** para os SaaS/APIs (RD Station, Google Ads, Meta Ads, Stripe/Pagar.me, ERP TOTVS via conector/REST). Justificar EL gerenciado para conectores prontos e baixo custo de manutenção.
   - **CDC** do **PostgreSQL transacional** via **Debezium + Kafka** (ou conector CDC do Airbyte) — captura `INSERT/UPDATE/DELETE` do binlog/WAL com baixo impacto na produção; coerente com a Aula 5 (CDC + incremental) e Aula 7 (Kafka/streaming) para dados de pedidos/navegação quase em tempo real.
   - **Planilhas:** ingeridas via conector Google Sheets, com plano de **descomissionamento progressivo** (substituir planilha por modelo no DW).
   - Cargas **incrementais e idempotentes** (MERGE/upsert por chave de negócio; partições sobrescritas por janela) — citar idempotência da Aula 5.

2. **Armazenamento / arquitetura (U3 — Aulas 9–12):**
   - **Cloud DW: BigQuery ou Snowflake** (ELT, armazenamento colunar, separação storage/compute) **OU Lakehouse** (S3/GCS + **Delta Lake ou Apache Iceberg** + engine como Databricks/Spark). Ambos aceitáveis se **justificados**; para o porte da VemComprar, um **cloud DW (ELT)** tende a ser o caminho mais rápido e barato — o lakehouse se justifica se houver muito dado semiestruturado de navegação.
   - **Camadas:** **raw/staging (bronze) → core integrado (silver) → data marts dimensionais (gold)** — exatamente o fluxo staging → core → marts da Aula 9.
   - **Modelagem dimensional (esquema estrela):** **fato_vendas** (grão = item de pedido) com FKs para **dim_cliente, dim_produto, dim_tempo, dim_loja/canal, dim_pagamento, dim_geografia/entrega**; **fato_marketing** (gasto/ROAS por campanha/dia). Esperado citar fato/dimensão, grão, SCD (Slowly Changing Dimension type 2 para histórico de cliente/produto).

3. **Transformação (U2/U3 — ELT):**
   - **dbt** como camada de transformação (SQL versionado, modular, com testes embutidos, documentação e **linhagem** automática). Modelos staging → intermediate → marts. Para volumes pesados de eventos de navegação, **Apache Spark** (PySpark) é a alternativa/complemento (Aula 6).

4. **Orquestração (U2 — Aula 8):**
   - **Apache Airflow** (ou Dagster/Astronomer) coordenando DAGs: ingestão → dbt run → testes → publicação. Uso de **retries** (habilitados pela idempotência), SLAs, alertas de falha. Esperado conectar idempotência (Aula 5) com retries do Airflow (Aula 8).

5. **Qualidade e observabilidade (U4 — Aula 13):**
   - **Testes de dados:** **dbt tests** (`not_null`, `unique`, `accepted_values`, `relationships`) + **Great Expectations** para suítes ricas e *data docs* de auditoria.
   - **Dimensões DAMA** com thresholds (completude, acurácia, consistência ERP×e-commerce, unicidade de CPF, validade, pontualidade do batch).
   - **Observabilidade (5 pilares):** frescor, volume, distribuição, esquema, linhagem — com **Elementary/Soda** ou Monte Carlo; alertas reduzem o **TTD** dos "3 incidentes/mês". Esperado citar a fórmula `Data downtime = nº incidentes × (TTD + TTR)`.

6. **Governança e LGPD (U4 — Aulas 14–16):**
   - **Contratos de dados** entre produtores (times-fonte) e consumidores (BI/ML), versionados.
   - **Catálogo de dados + linhagem** (DataHub, OpenMetadata ou Amundsen) — descoberta, donos, glossário de negócio.
   - **LGPD:** classificação e **mascaramento/pseudonimização de PII** (CPF, e-mail), **controle de acesso por papéis (RBAC)** e por coluna/linha, base legal documentada, política de retenção, atendimento a direitos do titular (acesso/exclusão), trilha de auditoria. Tirar PII das planilhas é entrega de segurança imediata.

7. **BI / disponibilização (U1/U3):**
   - **Power BI, Looker Studio ou Metabase** consumindo os marts gold. Dashboards de faturamento conciliado (uma só verdade), ROAS quase em tempo real, funil e LTV.

**Orçamento esperado (CAPEX + OPEX 9 meses, dentro de R\$ 900 mil):**

| Item | 9 meses | Notas |
| --- | --- | --- |
| Engenheiro(a) de dados (contratação/alocação) | R\$ 270 mil | 1 sênior ~R\$ 30 mil/mês (custo total) |
| Consultoria de implantação (Modern Data Stack) | R\$ 180 mil | setup, dbt, Airflow, governança |
| Ingestão gerenciada (Airbyte Cloud/Fivetran) | R\$ 90 mil | por volume de linhas sincronizadas |
| Cloud DW + storage + compute (BigQuery/Snowflake) | R\$ 120 mil | ELT; otimizar com particionamento/clustering |
| Orquestração + observabilidade + catálogo | R\$ 70 mil | Astronomer/Elementary/OpenMetadata |
| BI (licenças Power BI/Looker) | R\$ 40 mil | usuários gerenciais |
| Capacitação dos 2 analistas + 1 DBA | R\$ 50 mil | dbt, SQL analítico, governança |
| Reserva de contingência | R\$ 80 mil | imprevistos (~9%) |
| **Total 9 meses** | **R\$ 900 mil** | **No limite do orçamento** |

**Cronograma esperado (9 meses, 4 fases):**

| Fase | Prazo | Foco |
| --- | --- | --- |
| **1. Fundação e fonte única da verdade** | M1–M3 | DW provisionado; ingestão das fontes core (PostgreSQL via CDC, ERP, gateway); camadas raw→core; primeiros marts dimensionais; **dashboard de faturamento conciliado** (resolve a divergência de 7%) |
| **2. Cobertura e orquestração** | M3–M5 | Demais fontes (marketing, CRM, WMS); Airflow orquestrando ingestão + dbt; descomissionar planilhas críticas |
| **3. Qualidade, observabilidade e LGPD** | M5–M7 | dbt tests + Great Expectations; 5 pilares de observabilidade; mascaramento de PII, RBAC, catálogo + linhagem, contratos de dados |
| **4. Otimização e self-service BI** | M7–M9 | ROAS quase em tempo real; LTV/cohort; capacitação; FinOps de nuvem; handover para o time interno |

**KPIs-alvo esperados (antes → depois):**

1. **Tempo de fechamento do relatório mensal:** 5 dias → **< 1 dia** (automático).
2. **Divergência ERP × e-commerce:** até 7% → **< 0,5%** (conciliação no DW).
3. **Frescor dos dados de marketing/ROAS:** 4 dias → **< 6 h** (ou near real-time).
4. **Incidentes de "número errado em reunião":** ~3/mês → **≤ 1/trimestre**; **TTD** de dias → **minutos**.
5. **Custo de retrabalho manual:** R\$ 86,4 mil/ano → **~R\$ 10 mil/ano** (-88%).
6. **Cobertura de testes/contratos** sobre tabelas críticas: 0% → **≥ 90%**.
7. **PII fora de planilhas / mascarada:** 0% → **100%** das tabelas com PII governadas (conformidade LGPD).
8. **Fontes integradas no DW:** de 0/9 → **9/9**.

**Riscos esperados (com mitigações):**

1. **Custo de nuvem fugir do controle** → FinOps desde o início (particionamento, clustering, jobs incrementais idempotentes, monitor de custo).
2. **Resistência das áreas a abandonar planilhas** → migrar mostrando valor (dashboards melhores), com donos e contratos de dados.
3. **Qualidade ruim na fonte contamina o DW** → testes na ingestão (barrar o lixo na porta), contratos com os times-fonte.
4. **CDC impactar o transacional** → ler do WAL/binlog (não consultar tabela de produção), réplica de leitura se necessário.
5. **LGPD subestimada** → tratar PII na Fase 1 (não deixar para o fim), DPO/jurídico no comitê.
6. **Dependência da consultoria** → capacitar o time interno e documentar tudo (handover na Fase 4).

**Visão de futuro (12–24 meses) esperada:**

- **Real-time/streaming** ampliado (Kafka) para personalização e antifraude.
- **Feature store** e suporte a **ML** (recomendação, previsão de demanda, churn) sobre o DW governado.
- **Data Mesh / dado como produto** com contratos e catálogo maduros.
- **Cultura data-driven** consolidada e **FinOps** otimizando o custo por consulta.
- Possível **reverse ETL** (devolver dado tratado ao CRM/ads para ativação).

**Resposta de alta qualidade** demonstra: arquitetura coerente ponta a ponta; trade-offs explícitos (ETL×ELT, batch×CDC, DW×lakehouse); modelagem dimensional correta (grão, fato/dimensão, SCD); LGPD tratada a sério; números de nuvem realistas; KPIs antes/depois; integração das 4 unidades.

**Resposta de baixa qualidade** comumente apresenta: "vamos usar tudo" sem justificar; ignorar governança/LGPD; confundir OLTP com OLAP (continuar puxando da produção); orçamento irreal ou estourado; nenhum KPI mensurável; tratar só uma unidade (ex.: só ferramentas, sem qualidade nem modelagem).

---

## Roteiro do Estudante

### 1. Leia o desafio

Sua primeira tarefa é entender o cenário da **VemComprar com atenção**:

- **Quem** é a empresa (porte, GMV de R\$ 480 mi, 2,3 mi de pedidos/ano, 3,8 mi de clientes, crescimento de 140%)?
- **Qual** é a dor mais cara e mais clara? (Dica: por que ninguém confia no número do faturamento?)
- **Quais** restrições foram dadas (orçamento de R\$ 900 mil, prazo de 9 meses, 9 fontes, risco LGPD)?
- **Onde** estão os dados hoje e por que o modelo de planilhas não escala?

Tome **notas estruturadas** dos indicadores: 9 fontes, 1,8 TB / 6 GB/dia, 5 dias para fechar o mês, divergência de 7%, R\$ 86,4 mil/ano de retrabalho, ROAS com 4 dias de atraso, 3 incidentes/mês, PII de 3,8 mi de clientes em planilhas. Esses números são sua **base argumentativa** — toda decisão sua deve se apoiar em um deles.

### 2. Fontes de Pesquisa

Antes de propor a solução, reúna referências e ancore seus números:

- **Releia** as Unidades 1 a 4 — todas são insumo (fundamentos, ingestão/processamento, armazenamento/arquitetura, qualidade/governança/DataOps).
- **Estude** a Modern Data Stack na documentação oficial: Airbyte/Fivetran, dbt, Airflow, BigQuery/Snowflake (ou Delta/Iceberg para lakehouse), Great Expectations.
- **Pesquise preços reais de nuvem:** quanto custa armazenar e consultar no BigQuery/Snowflake? Quanto cobra o Airbyte/Fivetran por volume? Ancore seu orçamento.
- **Leia a LGPD (Lei 13.709/2018)** e o material da ANPD: bases legais, minimização, anonimização/pseudonimização, direitos do titular.
- **Traga um exemplo concreto** de empresa brasileira que construiu plataforma de dados (Nubank, iFood, Magazine Luiza, QuintoAndar) — blogs de engenharia e palestras no YouTube.

### 3. Entrega

Estruture o **documento técnico (PDF, 12–18 páginas)** assim:

1. **Sumário executivo** (1 página) — recomendação central em 5 linhas.
2. **Diagnóstico e dor prioritária** (1–2 páginas) — 9 fontes, fluxo manual, riscos LGPD, impacto financeiro.
3. **Arquitetura de referência** (3–4 páginas) — **diagrama ponta a ponta**, camadas (raw→core→marts), DW vs lakehouse justificado, **modelagem dimensional** (fatos e dimensões, grão, SCD).
4. **Stack tecnológica justificada** (2–3 páginas) — cada ferramenta com trade-offs (ETL×ELT, batch×CDC, custo, lock-in).
5. **Qualidade, observabilidade e governança/LGPD** (2 páginas) — testes, 5 pilares, contratos, catálogo/linhagem, mascaramento de PII, RBAC.
6. **Orçamento e cronograma** (1–2 páginas) — 4 fases, custos detalhados ≤ R\$ 900 mil, governança do projeto.
7. **KPIs, riscos e visão de futuro** (1–2 páginas) — metas antes/depois, riscos com mitigação, evolução 12–24 meses.
8. **Referências** (ABNT).

Para a **apresentação executiva (10–15 slides)**:

- 1 slide com **a recomendação central**.
- 2 slides de diagnóstico (números atuais + dor prioritária e LGPD).
- 2–3 slides de arquitetura (diagrama ponta a ponta + modelagem dimensional).
- 2 slides de stack e trade-offs.
- 1 slide de qualidade/observabilidade/governança.
- 1–2 slides de orçamento e cronograma.
- 1 slide de KPIs (antes → depois).
- 1 slide de riscos e visão de futuro.
- 1 slide de pedido de aprovação e próximos passos.

**Dica final:** capriche na **defesa numérica e na coerência**. A diretoria não compra ferramenta bonita — compra uma plataforma que **resolve a divergência de 7%**, **acaba com o retrabalho de R\$ 86,4 mil/ano**, **coloca a empresa em conformidade com a LGPD** e cabe no orçamento. Cada decisão de arquitetura sua deve estar ancorada em um número do desafio ou em um conceito das 4 unidades.

Esse projeto é seu **portfólio final** de engenharia de dados — o tipo de proposta que você apresenta em entrevistas e para defender investimentos. **Capricha**.

Boa entrega!
