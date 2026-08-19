# Unidade 4 — Qualidade, Governança e DataOps

- **Disciplina:** Data Engineering and Pipelines
- **Conteudista:** Afonso Cesar Lelis Brandão
- **Videoaulas desta unidade:** 13 a 16

> **Recap da Unidade 3:** guardamos o pipeline do Olist com **arquitetura**. Construímos o **Data Warehouse em camadas** (staging → core → marts, com a estrela `fct_orders`/`fct_order_items` + dimensões), organizamos o storage em **Lakehouse Medallion** (bronze/silver/gold), vimos o mesmo dbt rodando **na nuvem** (BigQuery/Snowflake/Redshift) com particionamento e controle de custo, e fechamos montando a **Modern Data Stack** completa do projeto. O dado do Olist agora está **guardado, modelado e barato de consultar** — mas dá para **confiar** nele, **governá-lo** e **operá-lo** com segurança? É o que esta unidade ataca.

## Aula 13 — Qualidade e observabilidade de dados

Nas três primeiras unidades nós **construímos** o pipeline do Olist do zero: ingerimos os 9 CSVs do marketplace, modelamos a estrela (`fct_orders`, `fct_order_items`, `dim_customers`, `dim_products`, `dim_sellers`, `dim_dates`), processamos em lote, orquestramos com o DAG `olist_pipeline` no Airflow e organizamos o storage em Medallion (bronze/silver/gold) num lakehouse local com DuckDB. O dado **anda**. Esta unidade muda a pergunta: como garantir que o dado que anda é **confiável**, **governado** e **operável**? Começamos pelo alicerce — **qualidade e observabilidade**. A pergunta-guia é brutal: *como você sabe, sem ninguém te avisar, que o `mart_sales_by_category` de hoje está certo?* Hoje adicionamos a primeira rede de proteção ao pipeline Olist: testes do dbt e do Great Expectations.

### As 6 dimensões da qualidade (DAMA) aplicadas ao Olist

Qualidade de dados não é "achismo": é mensurável por **dimensões** padronizadas. As seis clássicas do **DAMA-DMBOK**, instanciadas no Olist:

- **Completude (completeness):** quantos pedidos não têm review? No Olist, ~99k pedidos para ~99k reviews — milhares de pedidos ficam sem nota.
- **Acurácia (accuracy):** o dado reflete a realidade? Existe `order_delivered_customer_date` **anterior** ao `order_purchase_timestamp`? Entrega antes da compra é impossível.
- **Consistência (consistency):** o `payment_value` somado por `order_id` em `stg_order_payments` bate com o total esperado em `fct_orders`?
- **Unicidade (uniqueness):** `order_id` é único em `stg_orders`? `review_id` se repete em `olist_order_reviews_dataset`?
- **Validade (validity):** `review_score` está entre 1 e 5? `freight_value` é sempre `>= 0`? `order_status` pertence ao conjunto conhecido?
- **Pontualidade (timeliness):** o DAG `olist_pipeline` rodou no horário e o `gold/` está fresco para o dashboard das 8h?

Cada dimensão vira **métrica numérica** e **threshold** acordado com o negócio. Não existe "100% de qualidade" — existe qualidade **suficiente para a decisão**.

![Ciclo PDCA aplicado à melhoria contínua da qualidade de dados](https://commons.wikimedia.org/wiki/Special:FilePath/PDCA_Cycle.svg)

### dbt tests no `schema.yml` do projeto Olist

A arma mais barata vive ao lado do modelo. No `dbt_olist/`, declaramos testes no `schema.yml`: `not_null`, `unique`, `relationships` (integridade referencial fato→dimensão) e `accepted_values`. Falhou o teste, o `dbt test` quebra — barramos o lixo na porta, antes de chegar no mart.

```yaml
# models/marts/core/schema.yml
version: 2
models:
  - name: fct_order_items
    columns:
      - name: order_id
        tests: [not_null]
      - name: product_id
        tests:
          - not_null
          - relationships:
              to: ref('dim_products')
              field: product_id
  - name: stg_orders
    columns:
      - name: order_id
        tests: [unique, not_null]
      - name: order_status
        tests:
          - accepted_values:
              values: ['delivered','shipped','canceled','invoiced',
                       'processing','approved','created','unavailable']
```

### Great Expectations: regras de negócio do Olist

O dbt cobre estrutura; o **Great Expectations (GE)** cobre **regras ricas de negócio** com documentação para auditoria. Three expectations que todo pipeline Olist deveria ter: `review_score` entre 1 e 5; entrega nunca antes da compra; frete não-negativo.

```python
# great_expectations/ — expectations sobre o gold do Olist (DuckDB)
batch.expect_column_values_to_be_between(
    column="review_score", min_value=1, max_value=5)
batch.expect_column_pair_values_a_to_be_greater_than_b(
    column_A="order_delivered_customer_date",
    column_B="order_purchase_timestamp",
    or_equal=True)
batch.expect_column_values_to_be_between(
    column="freight_value", min_value=0, max_value=None)
```

O GE não está sozinho: o **Soda** (com a *Soda Checks Language*, declarada em YAML) cobre o mesmo terreno — checagens de qualidade e **alertas de anomalia** — de forma leve e fácil de plugar no CI. GE e Soda competem na mesma categoria; basta escolher um.

A diferença entre teste e **observabilidade**: o teste verifica regras que você **antecipou**; a observabilidade detecta o que você **não previu**, monitorando frescor, volume, distribuição, esquema e linhagem ao longo do tempo. Se o volume diário de pedidos do Olist cair de ~135 para 12, nenhum `not_null` acusa — observabilidade sim.

### A regra 1-10-100 no pipeline Olist

Custa **R\$ 1** prevenir o defeito (escrever o teste), **R\$ 10** corrigi-lo no pipeline e **R\$ 100** conviver com ele em produção. Um `accepted_values` de três linhas no `order_status` é o R\$ 1; descobrir que o `mart_delivery_performance` contou status inexistente depois que a diretoria apresentou o número é o R\$ 100. **Automatize a verificação onde o dado é produzido**, não onde é consumido.

### Exemplo numérico: o defeito real "entrega antes da compra" no Olist

Suponha que, ao validar o gold, o GE encontre $N_{def} = 18$ pedidos com `order_delivered_customer_date` anterior ao `order_purchase_timestamp` — um erro de **acurácia** clássico em datas. Sobre os $99\,441$ pedidos do Olist, a taxa de defeito é baixa, mas o custo de conviver com ela não é:

$$
\text{taxa} = \frac{18}{99\,441} \approx 0{,}018\%
$$

Aplicando a regra 1-10-100, com custo unitário de prevenção $c_{prev} = \text{R\$}\,1$:

$$
C_{prevenir} = 18 \times 1 = \text{R\$}\,18 \qquad C_{conviver} = 18 \times 100 = \text{R\$}\,1\,800
$$

Ou seja, a mesma falha custa **100×** mais se vazar para o `mart_delivery_performance` e contaminar o KPI de prazo de entrega. Um único `expect_column_pair_values_a_to_be_greater_than_b` — escrito uma vez — barra os 18 registros em todo *run* futuro do DAG.

### Atividade prática

Adicione a primeira rede de qualidade ao seu projeto Olist:

1. Escreva, para **cada uma das 6 dimensões DAMA**, uma regra mensurável sobre uma tabela real do Olist (ex.: "validade: `review_score` ∈ [1,5]").
2. Implemente **3 testes dbt** no `schema.yml` (`unique` em `order_id`, `relationships` de `fct_order_items` → `dim_products`, `accepted_values` em `order_status`) e rode `dbt test`.
3. Escreva **2 expectations** do Great Expectations sobre o gold (frete `>= 0` e entrega `>=` compra) e gere os *data docs*.
4. Estime o **TTD** (*time to detection*): se hoje o `freight_value` viesse negativo, quanto tempo até alguém perceber **sem** esses testes?

### Pontos-chave

- Qualidade é **mensurável** pelas 6 dimensões DAMA — completude, acurácia, consistência, unicidade, validade, pontualidade — instanciadas em tabelas reais do Olist.
- **dbt tests** (`not_null`, `unique`, `relationships`, `accepted_values`) cobrem estrutura barata no `schema.yml`; **Great Expectations** (ou o **Soda**, em YAML) cobre regras de negócio (review 1–5, entrega ≥ compra, frete ≥ 0) com documentação.
- **Testes** pegam o previsto; **observabilidade** pega o imprevisto (volume, frescor, distribuição) monitorando o histórico.
- A **regra 1-10-100** mostra que prevenir no `schema.yml` é ~100× mais barato que conviver com o defeito no mart.
- Esta é a **primeira camada de confiança** sobre o pipeline Olist que já existia — o `dbt test` agora roda dentro do DAG `olist_pipeline`.

### Para saber mais

- **Great Expectations — documentação oficial:** https://docs.greatexpectations.io/docs/
- **dbt — Data tests:** https://docs.getdbt.com/docs/build/data-tests
- **Soda — checks e monitoramento de qualidade de dados:** https://docs.soda.io/
- **Qualidade de dados / DAMA (Wikipedia):** https://en.wikipedia.org/wiki/Data_quality
- **Barr Moses — "What is Data Observability?" (Monte Carlo):** https://www.montecarlodata.com/blog-what-is-data-observability/

## Aula 13 — Roteiro da Videoaula 13: "Qualidade e observabilidade de dados"

### 1. Abertura (0:00 – 0:45)

> "Nas três primeiras unidades a gente construiu o pipeline do Olist inteiro: ingeriu os nove CSVs, modelou a estrela, orquestrou no Airflow, organizou o lakehouse. O dado anda. Mas deixa eu te fazer uma pergunta que tira o sono: como você sabe, sem ninguém te avisar, que o `mart_sales_by_category` de hoje está certo? Bem-vindo à Unidade 4. Hoje a gente coloca a primeira rede de proteção no pipeline Olist."

### 2. Desenvolvimento — parte 1 (0:45 – 4:00)

> "Qualidade de dados não é achismo, é número — e o padrão são as seis dimensões do DAMA. Vou instanciar cada uma no Olist: completude, milhares de pedidos sem review; acurácia, será que tem entrega com data anterior à compra?; consistência, o pagamento somado bate com o fato?; unicidade, `order_id` é único?; validade, `review_score` está entre 1 e 5, frete é maior ou igual a zero?; e pontualidade, o DAG rodou no horário? Cada uma vira métrica e limiar. E ninguém busca 100% de qualidade — busca qualidade suficiente pra decisão."

### 3. Desenvolvimento — parte 2 (4:00 – 7:00)

> "Agora a parte prática. A arma mais barata mora ao lado do modelo: dbt tests no `schema.yml`. Quatro tipos: `not_null` no `order_id`, `unique`, `relationships` ligando `fct_order_items` ao `dim_products` — integridade referencial — e `accepted_values` listando os status válidos do pedido. Rodou `dbt test`, falhou, o pipeline para. Pra regra de negócio mais rica entra o Great Expectations — ou o Soda, que faz o mesmo em YAML: review entre 1 e 5, entrega maior ou igual à compra, frete não-negativo. E ainda tem a observabilidade, que é diferente do teste: teste pega o que você previu; observabilidade pega o que você não previu — se o volume de pedidos despencar de 135 por dia pra 12, nenhum `not_null` acusa, mas a observabilidade sim."

### 4. Desenvolvimento — parte 3 (7:00 – 9:15)

> "Vamos colocar preço. Imagina que o Great Expectations achou 18 pedidos com entrega antes da compra — impossível, é erro de acurácia. Sobre 99 mil pedidos é uma fração minúscula, mas olha a regra 1-10-100: custa 1 real prevenir, 10 corrigir, 100 conviver. Prevenir os 18 custa 18 reais; deixar vazar pro mart de entrega e contaminar o KPI de prazo custa 1.800 — cem vezes mais. E o melhor: um único `expect` de comparação de datas, escrito uma vez, barra esses 18 registros em todo run futuro do DAG."

### 5. Encerramento (9:15 – 9:55)

> "Resumo: seis dimensões medem a qualidade; dbt tests cobrem estrutura barata, Great Expectations cobre regra de negócio, observabilidade cobre o imprevisto; e prevenir é cem vezes mais barato que remediar. Sua tarefa: adicione três testes dbt e duas expectations ao seu projeto Olist. Na próxima aula a gente sobe um nível — dado confiável também precisa ser dado governado e dentro da lei. E o Olist tem um detalhe lindo pra isso: ele já vem anonimizado. Entramos em governança e LGPD. Te vejo lá."

---

## Aula 14 — Governança, segurança e LGPD em pipelines

Na Aula 13 garantimos que o dado do Olist está **certo** (testes do dbt e do GE rodando no DAG). Agora garantimos que ele está **sob controle**: quem pode vê-lo, de onde veio, por quanto tempo fica e como tratá-lo dentro da lei. E o Olist nos dá um presente didático raro: ele **já vem anonimizado**. Os IDs de cliente, pedido, produto e vendedor são *hashes*; nomes foram removidos; a geolocalização é por **prefixo de CEP**, não por endereço. Isso é, na prática, um caso real de **pseudonimização** sob a **LGPD** — exatamente o que esta aula disseca. Governança bem-feita não trava o pipeline Olist; ela o torna **defensável**.

### O que é governança de dados

**Governança de dados** é o conjunto de **políticas, papéis, processos e métricas** que define como o dado é tratado. Ela responde: *quem é dono de cada dado, quem acessa o quê, o que é sensível, quanto tempo guardamos, como provamos conformidade a um auditor?* No Olist, mesmo anonimizado, esses papéis existem: o **data owner** (responsável de negócio pelos domínios — vendas, logística, reviews), o **data steward** (zela pelo significado de cada campo, ex.: o que é `customer_unique_id` vs `customer_id`) e o **data custodian** (o time que opera o DuckDB, o dbt e o Airflow). Sem dono, ninguém responde pelo dado.

![Cadeado simbolizando segurança, privacidade e governança de dados (LGPD)](https://commons.wikimedia.org/wiki/Special:FilePath/Padlock.svg)

### O Olist como caso real de pseudonimização

A distinção da LGPD vale ouro. **Dado anonimizado** sai do escopo da lei (não há como reidentificar o titular). **Dado pseudonimizado** continua dentro, porque a reidentificação ainda é possível com a chave de correspondência. O Olist mistura os dois: o `customer_unique_id` é um *hash* que **liga compras do mesmo comprador** ao longo do tempo — isso é pseudonimização, não anonimização plena, porque quem tivesse a tabela de-para original poderia reidentificar. Já o `customer_zip_code_prefix` (5 dígitos) é uma **generalização** geográfica que reduz a granularidade de localização. Mapear essa PII potencial é o primeiro passo da governança: classificar cada campo do Olist como público, interno ou pessoal/pseudonimizado.

### Mascaramento do `zip_code_prefix` e RBAC

Mesmo já pseudonimizado, aplicamos **defesa em profundidade**. O `customer_zip_code_prefix` pode ser **mascarado** para reduzir ainda mais a granularidade quando o analista não precisa do prefixo cheio:

```sql
-- mascaramento de localização no staging do Olist
select
    customer_id,
    customer_unique_id,
    left(customer_zip_code_prefix::varchar, 3) || 'XX' as zip_masked,
    customer_state
from {{ source('olist_raw','customers') }}
```

O controle de acesso segue o **menor privilégio** via **RBAC (Role-Based Access Control)**: permissões por papel, não por pessoa. O analista de marketing vê `mart_sales_by_category` agregado; o cientista de dados vê o gold para treinar modelo; só o engenheiro custodian acessa o schema `raw`. Some-se a isso **column/row-level security** (o analista de SP vê só linhas de SP) e **criptografia** em repouso e trânsito.

### Lineage do dbt como base do direito de exclusão

A **LGPD (Lei 13.709/2018)**, fiscalizada pela **ANPD**, garante ao titular o **direito de eliminação**. Para apagar todos os rastros de um `customer_unique_id`, você precisa saber **todos os lugares** onde ele pousou — e é aqui que o `dbt` brilha. Cada modelo declara suas dependências com `ref()` e `source()`, e o `dbt docs generate` produz o **grafo de lineage** automaticamente. Rastreando `customer_unique_id` no Olist:

$$
\text{raw.customers} \rightarrow \text{stg\_customers} \rightarrow \text{dim\_customers} \rightarrow \text{fct\_orders} \rightarrow \text{mart\_payment\_analysis}
$$

A linhagem responde às duas perguntas opostas: *a jusante* — "se eu remover este titular, quais marts mudam?" (impacto) — e *a montante* — "este número estranho, de onde saiu?" (causa-raiz). É também a planta baixa do processo de exclusão automatizada.

O lineage do dbt vive dentro do projeto; em escala de organização, **catálogos de dados** dedicados centralizam **metadados**, **dicionário de dados** (o significado de cada campo) e a linhagem ponta a ponta entre times e ferramentas. Os mais usados são o **DataHub** (open source) e o **Atlan** (comercial) — é onde um `customer_unique_id`, e tudo que depende dele, ficaria catalogado, classificado e governado.

### Minimização, base legal e retenção

Três princípios práticos da LGPD para o pipeline Olist: **minimização** (só ingerir o necessário — o Olist já remove nomes e comentários identificáveis); **base legal** (todo tratamento precisa de uma das 10 bases — execução de contrato, legítimo interesse etc.); e **retenção** (toda tabela com PII precisa de política de tempo de guarda — dado que você não guarda é dado que não vaza). Engenharia de dados **materializa** a lei: classificar no catálogo, mascarar por padrão, registrar lineage e automatizar a exclusão são tarefas do pipeline, não do jurídico.

### Exemplo numérico: o custo de um vazamento sob a LGPD

Imagine que a empresa por trás de um marketplace como o Olist — faturamento anual no Brasil de $\text{R\$}\,80\,000\,000$ — sofresse um vazamento se **não** tivesse a pseudonimização que o dataset já traz.

- **Multa LGPD:** até **2% do faturamento**, limitada a **R\$ 50 milhões por infração**. No teto percentual: $0{,}02 \times 80\,000\,000 = \text{R\$}\,1\,600\,000$.
- **Notificação e remediação:** sobre os $96\,096$ clientes únicos do Olist, a R\$ 9,00 por titular: $96\,096 \times 9 = \text{R\$}\,864\,864$.
- **Churn pós-vazamento:** 3% de evasão, receita média de R\$ 220/cliente/ano: $0{,}03 \times 96\,096 \times 220 \approx \text{R\$}\,634\,234$/ano.
- **Impacto no 1º ano:** $1\,600\,000 + 864\,864 + 634\,234 \approx \text{R\$}\,3\,099\,098$.
- **Prevenção** (mascaramento + RBAC + auditoria de lineage) $\approx \text{R\$}\,60\,000$ — a multa sozinha já é $\approx 27\times$ o custo de prevenir.

A lição: o Olist **já** aplicou a medida mais barata e poderosa — pseudonimizar na origem. A multa é a **menor** das parcelas; reputação e *churn* doem mais.

### Atividade prática

Para o pipeline Olist (que você construiu):

1. **Classifique** os campos das tabelas `customers`, `orders` e `reviews` em: público, interno, confidencial e **pessoal/pseudonimizado** (LGPD).
2. Para o `customer_zip_code_prefix`, escreva o SQL de **mascaramento** (prefixo + `XX`) e diga **qual papel RBAC** veria o valor cheio.
3. Gere o **lineage** com `dbt docs generate` e liste todos os modelos tocados por `customer_unique_id` — esse é o **caminho de exclusão**.
4. Escreva uma **política de retenção** de uma frase para `stg_customers` e `mart_payment_analysis`.

### Pontos-chave

- O **Olist já é anonimizado/pseudonimizado** (IDs *hash*, geolocation por prefixo de CEP) — um caso real de tratamento sob a **LGPD (Lei 13.709/2018)**.
- **Anonimizar** tira o dado do escopo da LGPD; **pseudonimizar** não (o `customer_unique_id` ainda liga compras do mesmo titular).
- **Mascaramento** do `zip_code_prefix`, **RBAC** por papel e **column/row-level security** aplicam menor privilégio mesmo sobre dado já pseudonimizado.
- O **lineage do dbt** (`dbt docs generate`) é a base técnica do **direito de exclusão**: rastreia `customer_unique_id` de `raw` ao mart; em escala, **catálogos** como **DataHub** (open source) ou **Atlan** centralizam metadados e linhagem.
- A **multa** chega a 2% do faturamento (teto R\$ 50 mi/infração), mas reputação e *churn* custam mais; pseudonimizar na origem é a prevenção mais barata.

### Para saber mais

- **LGPD — texto oficial (Lei 13.709/2018, Planalto):** https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm
- **ANPD — Autoridade Nacional de Proteção de Dados (gov.br):** https://www.gov.br/anpd/pt-br
- **Lei Geral de Proteção de Dados Pessoais (Wikipédia):** https://pt.wikipedia.org/wiki/Lei_Geral_de_Prote%C3%A7%C3%A3o_de_Dados_Pessoais
- **DataHub — catálogo e linhagem de dados (open source):** https://github.com/datahub-project/datahub

## Aula 14 — Roteiro da Videoaula 14: "Governança, segurança e LGPD em pipelines"

### 1. Abertura (0:00 – 0:45)

> "Na aula passada a gente garantiu que o dado do Olist está certo. Hoje a gente garante que ele está sob controle — quem vê, de onde veio, quanto tempo fica, e como tratar dentro da lei. E o Olist nos dá um presente didático raro: ele já vem anonimizado. IDs são hashes, nomes foram removidos, a localização é por prefixo de CEP. Isso é, na prática, um caso real de pseudonimização sob a LGPD. Vamos dissecar."

### 2. Desenvolvimento — parte 1 (0:45 – 3:45)

> "Governança é responsabilidade clara: data owner, dono de negócio dos domínios do Olist — vendas, logística, reviews; data steward, que zela pelo significado dos campos; e data custodian, o time que opera o DuckDB e o dbt. Agora a distinção que vale ouro na LGPD: dado anonimizado sai da lei, porque não dá pra reidentificar; dado pseudonimizado continua na lei. E o Olist mistura os dois: o `customer_unique_id` é um hash que liga as compras do mesmo comprador ao longo do tempo — isso é pseudonimização. Já o prefixo de CEP de cinco dígitos é uma generalização geográfica. Classificar essa PII é o primeiro passo."

### 3. Desenvolvimento — parte 2 (3:45 – 7:00)

> "Mesmo já pseudonimizado, a gente aplica defesa em profundidade. Mascaramento: pego o `customer_zip_code_prefix` e deixo só os três primeiros dígitos mais um XX — reduzo a granularidade pra quem não precisa do prefixo cheio. Controle de acesso por menor privilégio, com RBAC: o analista de marketing vê o mart agregado, o cientista vê o gold pra treinar modelo, e só o engenheiro custodian toca no schema raw. E agora a peça central: o direito de exclusão da LGPD. Pra apagar todos os rastros de um titular, você precisa saber onde ele pousou — e o lineage do dbt te dá isso de graça. O `customer_unique_id` vai de raw.customers, pra stg_customers, pra dim_customers, pra fct_orders, pra mart_payment_analysis. Esse grafo é a planta baixa da exclusão. E quando isso cresce pra empresa inteira, entra um catálogo de dados — o DataHub, que é open source, ou o Atlan — pra centralizar metadados, dicionário de campos e lineage de todos os times num lugar só."

### 4. Desenvolvimento — parte 3 (7:00 – 9:15)

> "Quanto custa errar? Imagina o marketplace com 80 milhões de faturamento, sem a pseudonimização que o Olist já traz, e vaza. Multa de até 2% do faturamento: 1,6 milhão. Notificar os 96 mil clientes únicos a 9 reais cada: quase 865 mil. Churn de 3%: mais 634 mil por ano. Total no primeiro ano: cerca de 3,1 milhões. Prevenir — mascarar, RBAC, auditar lineage — custava 60 mil. E repara: o Olist já fez a coisa mais barata e poderosa que existe — pseudonimizar na origem. A multa é a menor parcela; reputação é o que dói."

### 5. Encerramento (9:15 – 9:55)

> "Recapitulando: o Olist já é pseudonimizado — caso real de LGPD; anonimizar tira da lei, pseudonimizar não; mascaramento e RBAC aplicam menor privilégio; e o lineage do dbt é a base do direito de exclusão. Sua tarefa: classifique os campos de customers e reviews, mascare o CEP e gere o lineage do `customer_unique_id`. Na próxima aula a gente entra na cultura que faz tudo isso rodar de forma confiável e repetível — vamos versionar o repo Olist no Git e colocar GitHub Actions rodando `dbt build` a cada pull request. DataOps e CI/CD. Te vejo lá."

---

## Aula 15 — DataOps e CI/CD para pipelines de dados

Você já tem o pipeline Olist confiável (Aula 13) e governado (Aula 14). Falta o último ingrediente para virar **operação profissional**: a capacidade de **mudar o pipeline com segurança e frequência**, sem rezar a cada deploy. O projeto Olist hoje é uma pasta no seu laptop — `dbt_olist/`, `airflow/`, `ingestion/`, `great_expectations/`. E se um colega quiser contribuir com um novo mart? E se a sua alteração no `fct_order_items` quebrar o `mart_seller_scorecard`? **DataOps** importa as práticas de DevOps — Git, automação, testes, integração contínua — para o mundo dos dados. Hoje versionamos o repo Olist no Git e pomos o **GitHub Actions** rodando `dbt build` a cada *pull request*, num DuckDB de *staging*.

### DataOps: princípios sobre o repo Olist

**DataOps** aplica princípios ágeis e de DevOps ao ciclo de vida do dado, para entregar dado **confiável e rápido**. Os pilares, traduzidos para o projeto Olist:

- **Automação ponta a ponta:** do `git push` ao `dbt build`, sem passos manuais.
- **Testes de código E de dado:** o CI roda a lógica dos modelos **e** os testes de qualidade da Aula 13 (`dbt test`).
- **Colaboração:** todo o `pipeline-olist/` num repo Git, com *branches* e *pull requests*.
- **Monitoração e feedback:** a observabilidade da Aula 13 fecha o *loop*.
- **Iteração rápida:** mudanças pequenas e frequentes nos modelos dbt.

A métrica-norte (estudo **DORA**) é a mesma do DevOps de elite: **frequência de deploy alta** com **baixa taxa de falha de mudança**.

![Ciclo contínuo de integração e entrega representando o fluxo DevOps/DataOps de código a operação](https://commons.wikimedia.org/wiki/Special:FilePath/Devops-toolchain.svg)

### Git: versionando o pipeline Olist

Todo o repositório vira histórico rastreável: os modelos `stg_*`, `dim_*`, `fct_*`, os `schema.yml` com testes, o DAG `olist_pipeline.py`, as expectations do GE. *Branches* isolam o trabalho; *pull requests* trazem revisão por pares e *rollback*. O que **não** vai pro Git: o `olist.duckdb` e os Parquet do `gold/` (são dados, não código — entram no `.gitignore`). Para o dado, existe versionamento próprio (DVC, lakeFS, *time travel* de Delta/Iceberg), mas no projeto local o **código** é o que versionamos.

### GitHub Actions: `dbt build` em cada Pull Request

O coração do CI: a cada *pull request*, o GitHub Actions instala o `dbt-duckdb`, constrói o projeto num **DuckDB de staging** descartável e roda `dbt build` (que é `run` + `test` numa tacada). Se um modelo quebra ou um teste falha, o *merge* é **bloqueado** — o erro morre no PR, não em produção.

```yaml
# .github/workflows/dbt-ci.yml
name: dbt CI (Olist)
on:
  pull_request:
    branches: [main]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.11" }
      - name: Install dbt-duckdb
        run: pip install dbt-duckdb
      - name: dbt build (staging DuckDB)
        working-directory: dbt_olist
        run: |
          dbt deps
          dbt build --target ci   # run + test num olist.duckdb descartável
```

### dev → prod com targets do dbt e Write-Audit-Publish

A promoção `dev → staging → prod` no dbt é só trocar o **target** no `profiles.yml` (mesmos modelos, banco diferente). E uma estratégia elegante para dados é o **write-audit-publish (WAP)**: o pipeline Olist **escreve** os marts numa área de auditoria, **audita** com `dbt test` + Great Expectations, e só **publica** (promove o schema para produção) se passar. Assim o dashboard de vendas nunca enxerga um `mart_sales_by_category` intermediário quebrado.

$$
\text{dev} \;\rightarrow\; \text{staging} \;\rightarrow\; \text{produção}
$$

### IaC: a infraestrutura do pipeline como código

Clicar no console da nuvem para criar o *bucket* do `gold/` ou o *dataset* do warehouse é frágil e não reproduzível. **Infraestrutura como Código (IaC)** — com **Terraform**, Pulumi ou CloudFormation — declara a infra em arquivos versionados: "quero um *bucket* para o gold do Olist com retenção de 90 dias". Quando o pipeline Olist sair do laptop para a nuvem, o mesmo `profiles.yml` troca o adapter e o Terraform cria storage, warehouse e até as **políticas de acesso da Aula 14** — tudo revisável em PR.

### Exemplo numérico: frequência de deploy do pipeline Olist

A equipe do pipeline Olist migra de processo manual para CI/CD com GitHub Actions.

- **Antes (manual):** $2$ deploys/mês de novos modelos dbt. Cada um consome $4$ h de engenheiro a R\$ 120/h $= \text{R\$}\,480$. *Change failure rate* de $30\%$: $0{,}30 \times 2 = 0{,}6$ incidente/mês, cada um a R\$ 3.500 $\Rightarrow \text{R\$}\,2\,100$/mês. **Total $\approx 2 \times 480 + 2\,100 = \text{R\$}\,3\,060$/mês.**
- **Depois (CI/CD):** $20$ deploys/mês (10×), cada um com $0{,}3$ h de supervisão $= \text{R\$}\,36$. Falha cai para $5\%$ (o `dbt build` barra a maioria no PR): $0{,}05 \times 20 = 1$ incidente/mês, com *rollback* rápido reduzindo o impacto para R\$ 900. **Total $\approx 20 \times 36 + 900 = \text{R\$}\,1\,620$/mês.**
- **Resultado:** **10× mais deploys** por **R\$ 1.440/mês a menos**, com a *change failure rate* caindo de $30\%$ para $5\%$. O segredo não é fazer menos deploy — é deixar o deploy **barato e seguro**.

### Pausa para reflexão (Desafio)

Pense no seu pipeline Olist como ele está **agora**: modelos dbt na sua máquina, sem CI, deploy = você rodando `dbt run` no terminal. **Se um colega abrisse um pull request alterando o `fct_order_items` às 17h de uma sexta, você daria *merge* sem medo?** Provavelmente não — e *esse medo* é o sintoma exato que o DataOps cura. Liste **três coisas** que tornam esse *merge* assustador no projeto Olist (sem CI rodando `dbt build`? sem ambiente de staging? sem `dbt test`? `gold/` versionado errado?) e, para cada uma, escreva a prática de DataOps que a neutraliza. A meta de uma equipe madura é radical: **merge no `fct_order_items` na sexta às 17h é rotina, não coragem.** O que falta no seu repositório Olist para chegar lá?

### Atividade prática

Coloque o pipeline Olist em DataOps:

1. Inicialize um repo Git no `pipeline-olist/` e escreva o `.gitignore` (ignore `olist.duckdb`, `data/gold/`, `target/`).
2. Crie o `.github/workflows/dbt-ci.yml` que roda `dbt build --target ci` a cada PR num DuckDB de staging (use o YAML desta aula como base).
3. Descreva os **três passos concretos** do **write-audit-publish** para o `mart_sales_by_category`: onde escreve, o que audita, quando publica.
4. Escreva **três linhas de IaC** (pseudo-Terraform) declarando o *bucket* do `gold/` com versionamento e retenção.

### Pontos-chave

- **DataOps** aplica DevOps ao pipeline Olist: Git no `pipeline-olist/`, automação, testes de código **e** de dado, iteração rápida.
- **GitHub Actions** roda `dbt build` (run + test) a cada **pull request** num DuckDB de *staging* descartável — o erro morre no PR, não em produção.
- A promoção **dev → prod** é só trocar o **target** do dbt; o **write-audit-publish** garante que o dashboard nunca veja um mart intermediário quebrado.
- **IaC** (Terraform) torna a infra e a própria governança (Aula 14) versionável — essencial quando o Olist migrar para a nuvem.
- A meta **DORA** é deploy frequente com baixa taxa de falha: 10× mais deploys por menos custo, *change failure rate* de 30% → 5%.

### Para saber mais

- **DataOps (Wikipedia):** https://en.wikipedia.org/wiki/DataOps
- **DORA — State of DevOps (Google Cloud):** https://dora.dev/
- **GitHub Actions — documentação oficial:** https://docs.github.com/en/actions
- **dbt — Continuous integration:** https://docs.getdbt.com/docs/deploy/continuous-integration

## Aula 15 — Roteiro da Videoaula 15: "DataOps e CI/CD para pipelines de dados"

### 1. Abertura (0:00 – 0:45)

> "Seu pipeline Olist já é confiável e governado. Mas ele ainda é uma pasta no seu laptop. Pergunta direta: se um colega abrisse um pull request mexendo no `fct_order_items` às cinco da tarde de uma sexta, você daria merge sem medo? Se a resposta é 'de jeito nenhum', você tem um problema de processo, não de coragem. Hoje a gente versiona o repo Olist no Git e bota GitHub Actions rodando `dbt build` a cada pull request. Isso tem nome: DataOps."

### 2. Desenvolvimento — parte 1 (0:45 – 3:45)

> "DataOps é DevOps aplicado a dado. Os pilares no seu projeto Olist: automação do push ao build; testes de código E de dado — o CI roda os mesmos `dbt test` da Aula 13; colaboração, com todo o pipeline-olist num repo Git; e iteração rápida. A métrica que importa, do estudo DORA, é deploy frequente com baixa taxa de falha. Primeiro passo concreto: Git. Vão pro repositório os modelos stg, dim, fct, os schema.yml com testes, o DAG do Airflow, as expectations. O que NÃO vai: o `olist.duckdb` e os Parquet do gold — isso é dado, não código, entra no gitignore."

### 3. Desenvolvimento — parte 2 (3:45 – 7:00)

> "Agora o coração: GitHub Actions. A cada pull request, o Actions instala o dbt-duckdb, constrói o projeto num DuckDB de staging descartável e roda `dbt build` — que é run mais test de uma vez. Falhou um modelo ou um teste? Merge bloqueado. O erro morre no pull request, não em produção. A promoção dev pra prod é só trocar o target no profiles.yml — mesmos modelos, banco diferente. E tem uma estratégia linda pra dado: write-audit-publish. O pipeline escreve os marts numa área de auditoria, audita com dbt test e Great Expectations, e só publica se passar. O dashboard de vendas nunca vê um mart_sales_by_category quebrado no meio do caminho."

### 4. Desenvolvimento — parte 3 (7:00 – 9:00)

> "Última peça: infraestrutura como código. Quando o Olist sair do laptop pra nuvem, você não vai clicar no console pra criar o bucket do gold — você declara em Terraform: quero um bucket com versionamento e retenção de 90 dias, e até as políticas de acesso da aula passada viram código. Agora os números: equipe manual fazia 2 deploys por mês, 30% de falha, custava cerca de 3.060 por mês. Com CI/CD: 20 deploys por mês, falha cai pra 5% porque o `dbt build` barra no PR, rollback rápido, custo cai pra 1.620. Dez vezes mais deploy, mil e quatrocentos a menos. O segredo não é fazer menos deploy — é deixar o deploy barato e seguro."

### 5. Encerramento (9:00 – 9:55)

> "Fechando: DataOps versiona o repo Olist no Git; GitHub Actions roda dbt build a cada pull request num DuckDB de staging; dev pra prod é trocar o target; write-audit-publish protege o dashboard; e IaC versiona até a governança. Desafio da aula: olhe o seu pipeline Olist hoje e liste três coisas que tornam um merge no fct_order_items assustador, com a prática de DataOps que cura cada uma — porque numa equipe madura, merge na sexta às 17h é rotina. Na última aula a gente junta tudo: fecha o pipeline Olist completo e treina um modelo de machine learning lendo o gold pra prever atraso de entrega. Te vejo no encerramento."

---

## Aula 16 — Tendências e projeto integrador: do dado à IA

Chegamos à **última aula** da disciplina. Olhe para trás: você construiu, do zero, um **pipeline de dados completo do Olist** — ingestão dos 9 CSVs, modelagem em estrela, processamento em lote, simulação de streaming, orquestração no Airflow, lakehouse Medallion, DW na nuvem (conceitual), Modern Data Stack, e nesta unidade qualidade (dbt + GE), governança/LGPD e DataOps com CI/CD. Falta a cereja do bolo: **fechar o ciclo do dado até a IA**. Hoje treinamos um modelo `scikit-learn` que lê o **gold** do DuckDB para **prever atraso de entrega** dos pedidos Olist — e costuramos as quatro unidades no **diagrama de referência** que vira o seu **projeto de portfólio**.

### O engenheiro de dados na era da IA

A explosão da IA generativa não tornou o engenheiro de dados obsoleto — fez o oposto. **IA roda sobre dados**, e o modelo só é tão bom quanto o pipeline que o alimenta. No projeto Olist isso fica concreto: o modelo de atraso de entrega que vamos treinar **só existe** porque antes você garantiu `review_score` válido, datas acuradas e um `gold/` confiável. O papel se expande em três frentes: provedor de dados para IA (alimentando *feature stores*), usuário de IA como ferramenta (*copilots* que geram SQL/dbt) e a fronteira de extrair dado estruturado de texto — por exemplo, classificar o sentimento dos `review_comment_message` do Olist com um LLM. "Garbage in, garbage out" virou regra de ouro de ML.

![Rede neural artificial — base dos modelos de machine learning](https://commons.wikimedia.org/wiki/Special:FilePath/Colored_neural_network.svg)

### Feature store conceitual: as features do Olist

Um problema clássico de ML: o cientista calcula uma *feature* de um jeito no notebook e em produção ela é recalculada de outro — o **training-serving skew**, e o modelo decai. A **feature store** (Feast, Tecton) resolve servindo a **mesma feature com a mesma lógica** para treino (*offline*) e produção (*online*). Para prever atraso de entrega no Olist, as features naturais saem do gold: **prazo estimado** (`order_estimated_delivery_date` − `order_purchase_timestamp`), **frete** (`freight_value`), **nº de itens** do pedido, **categoria** do produto, **UF** do cliente e **parcelas** (`payment_installments`). No projeto local, a "feature store" é uma *view* do dbt sobre `fct_orders` + dimensões; o conceito é o mesmo de uma feature store gerenciada.

### Modelo scikit-learn lendo o gold do Olist

O modelo lê o gold direto do DuckDB, monta as features e treina um classificador para o alvo `is_late` (entrega real depois da estimada). É o **fechamento técnico do pipeline**: o dado que entrou como CSV cru sai como **predição**.

```python
# ml/train_delivery_delay.py
import duckdb
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

con = duckdb.connect("olist.duckdb")
df = con.sql("""
    select
        datediff('day', order_purchase_timestamp,
                        order_estimated_delivery_date) as prazo_estimado,
        freight_value, payment_installments,
        (order_delivered_customer_date >
         order_estimated_delivery_date)::int as is_late
    from marts.fct_orders
    where order_delivered_customer_date is not null
""").df()

X = df[["prazo_estimado", "freight_value", "payment_installments"]]
y = df["is_late"]
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=200, random_state=42).fit(X_tr, y_tr)
print("AUC:", roc_auc_score(y_te, model.predict_proba(X_te)[:, 1]))
```

**MLOps** é o DataOps (Aula 15) aplicado ao modelo: versionar dado, código *e* modelo; treino reproduzível; e monitorar **data/model drift**. Tudo o que você fez nesta unidade — qualidade, lineage, CI/CD — é **pré-requisito** de MLOps.

### O diagrama de referência: as 4 unidades no pipeline Olist

Agora costuramos tudo num único fluxo — o **pipeline de referência** que você deve saber desenhar de memória, instanciado no Olist:

$$
\text{9 CSVs} \rightarrow \text{Python/DuckDB} \rightarrow \text{Lake/DW (Parquet)} \rightarrow \text{dbt} \rightarrow \text{gold} \rightarrow \text{BI/ML}
$$

| Unidade | O que você construiu no Olist | No pipeline |
| --- | --- | --- |
| **U1 — Fundamentos** | Mapeou o ciclo de vida e modelou a estrela do Olist | Define **por que** e **como** o dado flui |
| **U2 — Ingestão/Processamento** | Ingeriu os CSVs, Spark/DuckDB, streaming, DAG Airflow | Traz, processa e **orquestra** o dado |
| **U3 — Armazenamento/Arquitetura** | DW em camadas, lakehouse Medallion, nuvem, MDS | **Armazena** e arquiteta de forma consultável |
| **U4 — Qualidade/Governança/DataOps** | dbt tests + GE, LGPD, CI/CD, modelo de ML | Garante **confiável, seguro, operável** — e serve IA |

As três primeiras unidades **constroem** o pipeline Olist; a quarta o torna **profissional** e o leva até a IA.

### Carreira em dados no Brasil

A engenharia de dados é uma das carreiras mais demandadas no Brasil. Um roteiro pragmático: **SQL e Python** inegociáveis; modelagem dimensional + **dbt**; orquestração (**Airflow**) e *big data* (**Spark**, **Kafka**); uma nuvem a fundo + **Terraform**; e qualidade/governança (**Great Expectations**, LGPD). Certificações ajudam (*AWS Data Engineer*, *Google Professional Data Engineer*, *Databricks*, *Astronomer Airflow*), mas o que **decide** é portfólio. E é exatamente isso que você acabou de construir.

### Exemplo numérico: pedidos atrasados no Olist e o lift do modelo

No Olist, dos pedidos efetivamente entregues, cerca de $8\%$ chegam **após** a data estimada. Sobre os $\approx 96\,478$ **pedidos** com entrega registrada (grandeza distinta dos $96\,096$ **clientes** únicos da Aula 14):

$$
N_{atraso} \approx 0{,}08 \times 96\,478 \approx 7\,718 \text{ pedidos atrasados}
$$

Sem modelo, prever "atraso" no chute teria precisão da própria taxa base, $8\%$. Suponha que o `RandomForestClassifier` atinja uma precisão de $\approx 24\%$ no decil de maior risco — o **lift** sobre o acaso é:

$$
\text{lift} = \frac{0{,}24}{0{,}08} = 3{,}0
$$

Ou seja, mirando os 10% de pedidos que o modelo aponta como mais arriscados, a logística encontra atrasos **3× mais** do que escolhendo pedidos ao acaso — o suficiente para acionar transportadora ou avisar o cliente proativamente. **Esse é o valor de negócio que o seu pipeline Olist, do CSV à predição, entrega.**

### Atividade prática

**Projeto integrador (portfólio) — feche o pipeline Olist:**

1. Crie o `ml/train_delivery_delay.py` que lê o gold do DuckDB, monta as features (prazo estimado, frete, parcelas) e treina o `RandomForestClassifier` para `is_late`.
2. Reporte a **AUC** e o **lift** no decil de maior risco; interprete o número para a logística.
3. Desenhe o **diagrama de referência de uma página**: `9 CSVs → Python/DuckDB → Lake/DW → dbt → gold → BI/ML`, marcando onde cada unidade entrou.
4. Suba o repositório `pipeline-olist/` **completo** no GitHub (ingestão + dbt + Airflow + testes + CI + ML) — este é o artefato que você leva para entrevistas.

### Pontos-chave

- A IA **amplificou** o papel do engenheiro de dados: o modelo de atraso do Olist só funciona porque o `gold/` é confiável ("garbage in, garbage out").
- A **feature store** elimina o *training-serving skew*; no Olist as features (prazo estimado, frete, itens, categoria, UF, parcelas) saem de `fct_orders` + dimensões.
- O **modelo scikit-learn** lê o gold do DuckDB e prevê `is_late` — o **fechamento** do pipeline, do CSV cru à predição; **MLOps** = DataOps aplicado ao modelo.
- O **pipeline de referência** é `9 CSVs → Python/DuckDB → Lake/DW → dbt → gold → BI/ML`; U1–U3 constroem, U4 profissionaliza e serve IA.
- O **projeto integrador** é o pipeline Olist completo no **portfólio do GitHub** — vale mais que certificado sem prática na carreira de dados no Brasil.

### Para saber mais

- **scikit-learn — RandomForestClassifier:** https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
- **Feast — Feature Store (documentação oficial):** https://docs.feast.dev/
- **Kaggle — Brazilian E-Commerce Public Dataset by Olist:** https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce
- **MLOps (Wikipedia):** https://en.wikipedia.org/wiki/MLOps

### Encerramento da disciplina

Você terminou **Data Engineering and Pipelines** — e, mais que isso, você **entregou um pipeline de dados de verdade**.

Em 16 aulas, você não só aprendeu conceitos: você **construiu o pipeline do Olist do zero**, camada por camada. Na **Unidade 1**, apresentou o projeto, mapeou o ciclo de vida sobre os 9 CSVs do marketplace e modelou a estrela (`fct_order_items`, `dim_customers` e companhia). Na **Unidade 2**, implementou a ingestão com dbt, processou em lote (DuckDB/Spark), simulou streaming dos pedidos e orquestrou o DAG `olist_pipeline` no Airflow. Na **Unidade 3**, ergueu o Data Warehouse em camadas, organizou o storage Medallion num lakehouse local, mostrou como o mesmo dbt migra para a nuvem e montou a Modern Data Stack com BI. E nesta **Unidade 4**, você **profissionalizou** tudo: qualidade com dbt tests e Great Expectations, governança e LGPD aproveitando que o Olist já é pseudonimizado, DataOps com Git e GitHub Actions, e fechou treinando um modelo de ML que prevê atraso de entrega lendo o gold.

Você sai com:

- **Um projeto real no portfólio** — o `pipeline-olist/` no GitHub: ingestão Python, transformação dbt (staging → core → marts), DAG do Airflow, testes de qualidade, CI com GitHub Actions, dashboard e modelo de ML.
- **Vocabulário e ferramentas** — DuckDB, dbt, Airflow, Parquet/Medallion, Great Expectations, lineage, LGPD, CI/CD, feature store, scikit-learn.
- **Consciência de qualidade, segurança e custo** — o dado certo, protegido e operável, não só o dado que chega.
- **A mensagem que atravessa o curso:** *o que roda local com DuckDB + dbt migra para a nuvem trocando o profile* — os conceitos são os mesmos.

Os fundamentos **não envelhecem** — as ferramentas trocam de nome, mas modelar bem, garantir qualidade e automatizar com segurança valem a carreira inteira. Agora pegue o seu pipeline Olist, publique no GitHub, escreva um bom README e apresente-o numa entrevista. A indústria precisa de gente que faça o dado chegar **confiável** — e você terminou esta disciplina com um pipeline completo nas mãos para provar que faz. Boa carreira, e vai longe.

## Aula 16 — Roteiro da Videoaula 16: "Tendências e projeto integrador: do dado à IA"

### 1. Abertura (0:00 – 0:45)

> "Última aula da disciplina. Olha pra trás um segundo: você construiu, do zero, um pipeline completo do Olist — ingestão, estrela, Airflow, lakehouse, qualidade, LGPD, CI/CD. Falta a cereja do bolo: fechar o ciclo do dado até a inteligência artificial. Hoje a gente treina um modelo scikit-learn que lê o gold do DuckDB pra prever atraso de entrega, e costura as quatro unidades no diagrama que vira o seu projeto de portfólio."

### 2. Desenvolvimento — parte 1 (0:45 – 3:45)

> "A IA não aposentou o engenheiro de dados — fez o contrário. Modelo só é tão bom quanto o pipeline que alimenta ele, e no Olist isso é concreto: o modelo de atraso só existe porque antes você garantiu review válido, datas acuradas e um gold confiável. Garbage in, garbage out. E pra alimentar o modelo entra o conceito de feature store: servir a mesma feature, com a mesma lógica, pro treino e pra produção, evitando o training-serving skew. As features do Olist saem do gold: prazo estimado, que é a estimada menos a compra; frete; número de itens; categoria; UF; e parcelas. No projeto local, essa feature store é uma view do dbt sobre o fct_orders."

### 3. Desenvolvimento — parte 2 (3:45 – 6:45)

> "Agora o fechamento técnico. O script ml/train_delivery_delay.py conecta no olist.duckdb, lê o fct_orders, monta as features e treina um RandomForest pra prever is_late — entrega depois da estimada. O dado que entrou como CSV cru sai como predição. E MLOps é só o DataOps da aula passada aplicado ao modelo: versiona dado, código e modelo, treino reproduzível, e monitora drift. Tudo o que você fez nesta unidade — qualidade, lineage, CI/CD — é pré-requisito de MLOps. Agora grava o diagrama de referência de memória: nove CSVs, Python e DuckDB, lake ou warehouse em Parquet, dbt, gold, BI ou ML. A Unidade 1 modelou; a 2 ingeriu e orquestrou; a 3 armazenou e arquitetou; a 4 garantiu qualidade e serviu a IA."

### 4. Desenvolvimento — parte 3 (6:45 – 9:00)

> "Vamos pôr número no valor. No Olist, cerca de 8% dos pedidos entregues chegam atrasados — sobre 96 mil entregas, são quase 7.700 pedidos. No chute, você acertaria 8%. Mas suponha que o modelo atinja 24% de precisão no decil de maior risco: o lift é três. Mirando os 10% que o modelo aponta como mais arriscados, a logística acha atraso três vezes mais do que no acaso — o suficiente pra acionar transportadora ou avisar o cliente antes. Esse é o valor de negócio que o seu pipeline Olist, do CSV à predição, entrega. E sobre carreira: SQL e Python inegociáveis, dbt, Airflow, uma nuvem, Terraform — mas o que decide é portfólio, e você acabou de construir um."

### 5. Encerramento (9:00 – 9:55)

> "Tarefa final, a mais importante: feche o pipeline. Escreva o train_delivery_delay.py lendo o gold, reporte a AUC e o lift, desenhe o diagrama de uma página e suba o pipeline-olist completo no GitHub — ingestão, dbt, Airflow, testes, CI e ML. Esse é o artefato que você apresenta numa entrevista. Você não só aprendeu engenharia de dados: você entregou um pipeline de dados de verdade, do CSV cru à predição. Os fundamentos não envelhecem — as ferramentas trocam de nome, mas modelar bem, garantir qualidade e automatizar com segurança valem a carreira inteira. A indústria precisa de gente que faça o dado chegar confiável. Você terminou desse lado, com um projeto pra provar. Boa carreira, e vai longe."

---

## Quiz não avaliativo

### Questão 1

No pipeline Olist, você precisa garantir que **toda** linha de `fct_order_items` aponte para um produto existente em `dim_products`, que `order_status` só assuma valores conhecidos, e que `review_score` fique entre 1 e 5. Sobre **como** implementar essas três regras, assinale a alternativa **correta**:

- [ ] a. Todas as três são `accepted_values` do dbt, pois envolvem listas fixas de valores.
- [x] b. A integridade `fct_order_items → dim_products` é um teste `relationships` do dbt; `order_status` é um `accepted_values` do dbt; e a faixa de `review_score` (1–5) é melhor expressa como uma *expectation* `expect_column_values_to_be_between` do Great Expectations — testes do dbt cobrem estrutura/integridade, o GE cobre regras de negócio com documentação.
- [ ] c. Nenhuma pode ser testada automaticamente; só observabilidade detectaria esses casos.
- [ ] d. As três devem ser implementadas como `unique`, pois qualquer regra de qualidade se resume a unicidade de chave.

**Resposta correta:** `b`

**Feedback:** A (b) mapeia cada regra à ferramenta certa: `relationships` garante integridade referencial fato→dimensão, `accepted_values` valida o conjunto de `order_status`, e a faixa numérica de `review_score` cabe numa *expectation* do Great Expectations (`expect_column_values_to_be_between`). A (a) erra ao chamar a integridade referencial de `accepted_values`. A (c) ignora que testes antecipados (dbt/GE) cobrem exatamente regras conhecidas. A (d) reduz tudo a `unique`, o que é falso — unicidade é só uma das 6 dimensões DAMA.

### Questão 2

O Olist **já vem anonimizado** (IDs *hash*, geolocalização por prefixo de CEP) e você precisa colocá-lo em DataOps com CI. Sobre **governança/LGPD** e **CI/CD** no projeto, assinale a alternativa **correta**:

- [ ] a. Como o Olist é anonimizado, ele sai 100% do escopo da LGPD; e o CI deveria rodar `dbt build` direto no banco de produção para validar com dados reais.
- [ ] b. O `customer_unique_id` torna o Olist totalmente anônimo; e o write-audit-publish significa publicar o mart primeiro e auditar depois.
- [x] c. O `customer_unique_id` (que liga compras do mesmo titular) caracteriza **pseudonimização** — ainda no escopo da LGPD —, e o **lineage do dbt** é a base do direito de exclusão; no CI, o **GitHub Actions roda `dbt build` num DuckDB de staging** a cada PR, e o **write-audit-publish** escreve → audita → só então publica.
- [ ] d. RBAC e mascaramento são desnecessários em qualquer pipeline; basta confiar no GitHub Actions para garantir LGPD.

**Resposta correta:** `c`

**Feedback:** A (c) está correta em todos os pontos: o `customer_unique_id` permite ligar compras do mesmo comprador, logo é **pseudonimização** (continua sob a LGPD), e o lineage do dbt rastreia o titular de `raw` ao mart (base do direito de exclusão); o CI roda `dbt build` num DuckDB de **staging** (nunca em produção) e o WAP é **escreve → audita → publica**. A (a) confunde pseudonimização com anonimização plena e propõe rodar CI em produção (perigoso). A (b) inverte o WAP. A (d) descarta RBAC/mascaramento, que são pilares do menor privilégio.

---

## Atividade Verificadora (AAI — Atividade Avaliativa Individual)

**Pergunta:**

> Você acabou de construir o **pipeline de dados do Olist** ao longo da disciplina: ingestão dos 9 CSVs no DuckDB, transformação com dbt (staging → core → marts) e storage Medallion, orquestrado no Airflow. Os fatos e dimensões do core são `fct_orders`, `fct_order_items`, `dim_customers`, `dim_products` e `dim_sellers`; e os marts de negócio são `mart_sales_by_category` (receita por categoria de produto), `mart_delivery_performance` (prazo e atraso de entrega), `mart_payment_analysis` (valor e parcelas de pagamento por pedido) e `mart_seller_scorecard` (desempenho de vendedores). Agora, nesta unidade, você precisa **profissionalizá-lo** e entregá-lo no portfólio.
>
> Elabore uma resposta dissertativa estruturada em quatro partes, **citando os artefatos reais do projeto**:
>
> 1. **Qualidade (Aula 13):** que **dbt tests** (`not_null`/`unique`/`relationships`/`accepted_values`) e quais **expectations do Great Expectations** você adicionaria ao Olist, e como justificaria o investimento (regra 1-10-100 / *data downtime*)?
> 2. **Governança e LGPD (Aula 14):** como o fato de o Olist **já ser pseudonimizado** muda a análise, como você mascararia o `zip_code_prefix` e aplicaria RBAC, e como o **lineage do dbt** habilita o direito de exclusão de um `customer_unique_id`?
> 3. **DataOps (Aula 15):** como colocaria o repo `pipeline-olist/` em **Git + GitHub Actions** rodando `dbt build` em PR, e como aplicaria **write-audit-publish** ao `mart_sales_by_category`?
> 4. **IA (Aula 16):** que **features do gold** alimentariam um modelo `scikit-learn` para prever atraso de entrega, e como mediria o valor de negócio (AUC/lift)?

**Resposta esperada:**

> Uma resposta de qualidade integra as quatro aulas num plano coerente, sempre **citando os artefatos reais do Olist**. **(1) Qualidade:** deve propor `unique`/`not_null` em `order_id` (`stg_orders`), `relationships` de `fct_order_items` → `dim_products`/`dim_customers`, `accepted_values` no `order_status`, e expectations do GE para `review_score` ∈ [1,5], `order_delivered_customer_date` ≥ `order_purchase_timestamp` e `freight_value` ≥ 0. Boa resposta quantifica com a regra 1-10-100 (prevenir no `schema.yml` é ~100× mais barato que conviver com o defeito no mart) e estima o TTD atual. **(2) Governança/LGPD:** reconhece que o Olist é **pseudonimizado** (o `customer_unique_id` ainda liga compras do mesmo titular, logo continua sob a LGPD — não é anonimização plena), mascara o `customer_zip_code_prefix` (`left(...,3) || 'XX'`), aplica RBAC por papel (analista vê o mart agregado, custodian vê o `raw`), e explica que o **lineage do dbt** (`dbt docs generate`) rastreia o titular de `raw.customers` → `stg_customers` → `dim_customers` → `fct_orders` → `mart_payment_analysis`, sendo a base do direito de exclusão. **(3) DataOps:** versiona o `pipeline-olist/` no Git (com `.gitignore` para `olist.duckdb` e `data/gold/`), cria `.github/workflows/dbt-ci.yml` rodando `dbt build --target ci` num DuckDB de staging a cada PR, e aplica write-audit-publish ao `mart_sales_by_category` (escreve em schema de auditoria → roda `dbt test`/GE → promove só se passar). Usa métricas DORA (frequência de deploy, change failure rate, MTTR) para provar a melhoria. **(4) IA:** extrai do gold as features prazo estimado (`order_estimated_delivery_date` − `order_purchase_timestamp`), `freight_value`, nº de itens, categoria, UF e `payment_installments`, treina um `RandomForestClassifier` para `is_late`, e mede valor com **AUC** e **lift** (ex.: ~8% de pedidos atrasados no Olist; lift de ~3× no decil de risco permite ação proativa da logística). A resposta excelente **conecta os blocos** (qualidade alimenta a governança que habilita exclusão; DataOps automatiza e protege; o gold confiável é o que torna o modelo possível) e fecha apontando o **repositório completo no GitHub como projeto de portfólio**, sem vender mágica — jornada incremental, números realistas.

---

## Material complementar

### Direto da fonte — livro da Biblioteca Virtual

> Este é **o** livro de referência moderno da área — escrito por dois praticantes para ensinar engenharia de dados como disciplina, não como coleção de ferramentas. O capítulo sobre o ciclo de vida do dado e os "*undercurrents*" (segurança, gestão de dados, DataOps, arquitetura) é a coluna vertebral conceitual desta Unidade 4: qualidade, governança e DataOps aparecem ali como as correntes que atravessam **todas** as etapas do pipeline — exatamente como aplicamos ao pipeline Olist nas Aulas 13 a 16 (testes, LGPD, CI/CD e o fechamento com ML).

- **Nome do livro:** *Fundamentals of Data Engineering: Plan and Build Robust Data Systems*
- **Capítulo:** Capítulo 2 — *The Data Engineering Lifecycle* (foco nos *undercurrents*: Data Management, DataOps, Security)
- **Organizador:** Joe Reis e Matt Housley
- **Editora:** O'Reilly Media
- **Link de acesso (BV):** consultar na Biblioteca Virtual (BV) — buscar por *"Fundamentals of Data Engineering"* (O'Reilly) no acervo da BV
- **Dataset do projeto (Kaggle):** https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce (Brazilian E-Commerce Public Dataset by Olist)
- **Aula em que entra:** Aulas 13 a 16

### Para mergulhar no assunto

> Para entender por que **observabilidade** e *data downtime* viraram tema central — exatamente o que aplicamos ao monitorar volume e frescor do gold do Olist na Aula 13 —, leia o artigo da Monte Carlo que popularizou o conceito. E para ver como ferramentas de **catálogo e lineage** funcionam na prática (a base do direito de exclusão da Aula 14, que mapeamos com o `dbt docs`), explore o **DataHub**, projeto open source de governança e linhagem.

- **Link(s):** https://www.montecarlodata.com/blog-what-is-data-observability/ — e https://github.com/datahub-project/datahub
- **Aula em que entra:** Aulas 13 e 14

### Podcast (curadoria, até 45 min)

> O canal oficial da **dbt Labs** no YouTube traz palestras do **Coalesce** e tutoriais sobre os temas exatos desta unidade — **testes de dados**, **CI/CD com dbt** e *deploy* de pipelines —, usando a mesma ferramenta (`dbt`) que você usou para transformar o Olist. Ótimo para ver, em vídeo, o `dbt build` e os testes que você implementou nas Aulas 13 e 15 rodando em produção em times reais.

- **Nome do podcast/canal:** dbt Labs (canal oficial no YouTube)
- **Tema recomendado:** dbt tests, CI/CD com dbt e deploy de pipelines (palestras do Coalesce)
- **Link:** https://www.youtube.com/@dbt-labs (YouTube)
- **Aula em que entra:** Aulas 13 e 15

### Artigo científico

> Artigo seminal do Google que cunhou o termo "**dívida técnica oculta em ML**" — argumenta que apenas uma fração minúscula de um sistema de ML é o código do modelo; o resto é infraestrutura de dados (coleta, validação, *feature extraction*, monitoração, configuração). É a justificativa científica para tudo o que esta unidade defende: qualidade, governança e DataOps são o que sustenta IA em produção — conectando diretamente com a Aula 16, em que o modelo de atraso do Olist só funciona porque o pipeline (testes, lineage, CI/CD) o sustenta.

- **Link:** https://papers.nips.cc/paper_files/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html (NIPS 2015) — e https://research.google/pubs/hidden-technical-debt-in-machine-learning-systems/
- **Aula em que entra:** Aula 16
- **Referência bibliográfica do artigo no formato ABNT:**
  > SCULLEY, D. *et al*. **Hidden technical debt in machine learning systems**. In: ADVANCES IN NEURAL INFORMATION PROCESSING SYSTEMS (NIPS), 28., 2015, Montreal. *Proceedings* [...]. Cambridge: MIT Press, 2015. p. 2503-2511.
