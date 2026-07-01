# Unidade 3 — Armazenamento e Arquitetura de Dados

- **Disciplina:** Data Engineering and Pipelines
- **Conteudista:** Afonso Cesar Lelis Brandão
- **Videoaulas desta unidade:** 9 a 12

> **Recap da Unidade 2:** no nosso **pipeline do Olist** já implementamos a ingestão com dbt (ELT) — os modelos `staging` `stg_orders`, `stg_order_items`, `stg_order_payments`, `stg_order_reviews` etc. já leem o schema `raw` do DuckDB, limpam e castam tipos, com carga incremental por `order_purchase_timestamp`. Vimos processamento em lote (DuckDB vetorizado como equivalente local do Spark), streaming simulado (`stream_orders.py`) e orquestramos tudo num DAG do Airflow (`olist_pipeline`: `ingest_csv_to_duckdb` → `dbt_run` → `dbt_test` → `export_gold`). Os ~99 mil pedidos já entram, são processados e orquestrados — mas **onde eles ficam guardados** e **com que arquitetura**? É o que esta unidade responde: vamos construir o **Data Warehouse do Olist em camadas**, organizar o storage em **Lakehouse Medallion**, ver o mesmo dbt rodando **na nuvem** e fechar montando a **Modern Data Stack** completa do projeto.

---

## Aula 9 — Data Warehouse e modelagem dimensional aplicada

Na Unidade 2 deixamos pronta a camada `staging` do Olist: nove modelos `stg_*` que leem o schema `raw` do DuckDB e entregam dados limpos e tipados. Mas `staging` ainda é espelho da fonte — não responde perguntas de negócio. Quando a diretoria do marketplace pergunta "qual o faturamento por categoria de produto, por UF, no último trimestre?", consultar os CSVs crus ou o `raw` seria lento e confuso. O **Data Warehouse** existe para isso: um repositório otimizado para **responder perguntas analíticas**. Nesta aula vamos transformar o `staging` do Olist no **DW em camadas com dbt** — `staging` → `core` (estrela `dim_*`/`fct_*`) → `marts` de negócio — e implementar **SCD2** com `dbt snapshot` em `dim_sellers`.

### O conceito de Data Warehouse aplicado ao Olist

Um **Data Warehouse (DW)** é um repositório central, **orientado a assunto, integrado, não volátil e variante no tempo**, projetado para apoiar decisão. A definição clássica é de Bill Inmon. Sobre o Olist os quatro adjetivos viram concretos:

- **Orientado a assunto:** organizamos por temas (vendas, logística, reviews), não por arquivo CSV de origem.
- **Integrado:** as nove tabelas do Olist (`orders`, `order_items`, `payments`, `reviews`, `products`, `customers`, `sellers`, `geolocation`, `category_translation`) viram um modelo único, com nomes e tipos padronizados.
- **Não volátil:** um pedido de 2017 continua no DW; nada é sobrescrito.
- **Variante no tempo:** guardamos o histórico de set/2016 a out/2018, e a evolução das dimensões (um seller que muda de UF — SCD2).

A diferença essencial para um banco transacional (OLTP) é o propósito: o **OLTP — Online Transaction Processing** registra muitas escritas pequenas (cada pedido novo do marketplace), enquanto o DW é **OLAP — Online Analytical Processing** (poucas consultas que varrem os ~112 mil itens para agregar).

![Diagrama de um esquema estrela (star schema) com uma tabela fato central conectada a tabelas de dimensão, base da modelagem dimensional em Data Warehouses](https://commons.wikimedia.org/wiki/Special:FilePath/Star-schema.png)

### Inmon vs Kimball — e o que usamos no Olist

| Aspecto | Inmon (top-down) | Kimball (bottom-up) |
| --- | --- | --- |
| **Ponto de partida** | DW corporativo único, normalizado (3FN) | Data marts dimensionais por área |
| **Modelagem** | Entidade-relacionamento normalizada | Modelagem dimensional (estrela) |
| **Integração** | Centralizada antes dos marts | Barramento de dimensões conformadas |
| **Tempo até valor** | Mais lento (constrói a base primeiro) | Mais rápido (entrega marts incrementalmente) |

No projeto Olist adotamos uma **abordagem híbrida pragmática, com sabor Kimball**: a camada `core` é um core integrado (uma estrela conformada com `dim_customers`, `dim_sellers`, `dim_products`, `dim_dates`), e os `marts` analíticos são recortes por área (vendas, entregas). É o padrão recomendado pelo próprio dbt para estruturar projetos.

### Camadas no dbt: staging → core → marts

Um DW maduro tem **três camadas lógicas**, e elas mapeiam 1:1 nas pastas do nosso `dbt_olist/`:

1. **Staging** (`models/staging/`, já feito na Aula 5): `stg_*` limpa e renomeia uma fonte por vez. Descartável e fina.
2. **Core** (`models/marts/core/`): o coração do DW, onde integramos as fontes na **estrela** — dimensões e fatos como **fonte única da verdade**.
3. **Marts analíticos** (`models/marts/analytics/`): recortes temáticos para consumo direto — `mart_sales_by_category`, `mart_delivery_performance`.

O fluxo **staging → core → marts** separa responsabilidades: ingestão isolada da integração, integração isolada do consumo. No dbt isso vira o lineage automático via `{{ ref(...) }}`.

### A estrela do Olist em SQL (dbt)

Na camada `core` materializamos a dimensão de clientes e o fato de itens. Repare no uso de `ref` (encadeia o lineage) e em como o **fato** carrega só chaves + métricas, enquanto a **dimensão** carrega o contexto descritivo:

```sql
-- models/marts/core/dim_customers.sql
select
    customer_id,
    customer_unique_id,
    customer_zip_code_prefix,
    customer_city,
    upper(customer_state) as customer_state
from {{ ref('stg_customers') }}
```

```sql
-- models/marts/core/fct_order_items.sql  (grão = 1 item de pedido)
select
    i.order_id,
    i.order_item_id,
    i.product_id,
    i.seller_id,
    o.customer_id,
    cast(o.purchased_at as date) as date_key,
    i.price,
    i.freight_value
from {{ ref('stg_order_items') }} i
join {{ ref('stg_orders') }} o using (order_id)
```

`fct_order_items` tem grão de **um item**; `fct_orders` (grão de **um pedido**) agrega pagamento e status. As métricas `price` e `freight_value` vivem na fato; tudo que é "quem/o quê/quando/onde" mora nas dimensões.

### SCD2 com dbt snapshot em dim_sellers

E quando um **seller muda de cidade/UF**? Se sobrescrevermos (SCD Tipo 1), perdemos o histórico e atribuímos vendas antigas à cidade nova. Para análise temporal correta usamos **SCD Tipo 2**: cada versão vira uma linha, com janela de validade. No dbt isso é declarativo — um `snapshot` com `strategy='check'`:

```sql
-- snapshots/sellers_snapshot.sql
{% snapshot sellers_snapshot %}
{{ config(
    target_schema='snapshots',
    unique_key='seller_id',
    strategy='check',
    check_cols=['seller_city', 'seller_state']
) }}
select seller_id, seller_zip_code_prefix, seller_city, seller_state
from {{ ref('stg_sellers') }}
{% endsnapshot %}
```

Ao rodar `dbt snapshot`, o dbt adiciona `dbt_valid_from` e `dbt_valid_to`: a versão antiga ganha data de fim e a nova entra como vigente. A `dim_sellers` final lê desse snapshot, preservando o histórico dos 3.095 vendedores.

### Armazenamento colunar vs por linha

A virada de desempenho dos DWs é o **armazenamento colunar**. Bancos transacionais guardam **por linha** (todos os campos de um pedido juntos), ótimo para escrever um pedido inteiro. DWs analíticos guardam **por coluna**. O DuckDB é colunar e vetorizado — por isso resolve agregações no Olist em segundos. Uma consulta `SELECT SUM(price) FROM fct_order_items` lê **só a coluna `price`**, ignorando dezenas de outras, e ainda comprime muito (valores parecidos numa coluna). Formatos como **Parquet** levam o mesmo princípio ao disco.

### Exemplo numérico: economia colunar na fct_order_items

A `fct_order_items` do Olist tem ~112.650 linhas. Enriquecida com atributos das dimensões (produto, categoria, datas), ela chega a ~14 colunas — bem mais que as 7 da tabela bruta de itens vista na Unidade 1 —, das quais `price` e `freight_value` são as métricas de interesse, e uma análise de faturamento só precisa de `price` (1 de 14 colunas). Lendo a tabela inteira por linha o motor varreria as 14 colunas; no colunar lê a fração:

$$
\text{fração lida} = \frac{1}{14} \approx 0{,}071 = 7{,}1\%
$$

Com compressão colunar típica de fator 4 sobre essa coluna, o volume efetivamente lido cai para:

$$
\frac{0{,}071}{4} \approx 0{,}018 = 1{,}8\%\ \text{do tamanho original}
$$

Ou seja, somar o faturamento dos R\$ 13,2 milhões em itens do Olist toca menos de 2% dos bytes da tabela — a base do desempenho analítico que torna o DuckDB instantâneo no laptop.

### Atividade prática

No seu `dbt_olist/`:

1. Crie `models/marts/core/dim_products.sql` lendo de `{{ ref('stg_products') }}` e juntando a tradução de categoria (`stg_category_translation`).
2. Crie `mart_sales_by_category.sql` agregando `sum(price)` por `product_category_name_english`, com `ref` para `fct_order_items` e `dim_products`.
3. Rode `dbt run --select marts.core+` e confira a ordem de execução no lineage.
4. Aponte **uma dimensão** do Olist (além de `dim_sellers`) que poderia exigir **SCD2** e justifique.

### Pontos-chave

- O **DW do Olist** é orientado a assunto, integrado, não volátil e variante no tempo — voltado a OLAP, não ao OLTP do marketplace.
- No dbt, as camadas **staging → core → marts** viram pastas: `stg_*` (Aula 5) → `dim_*`/`fct_*` → `mart_*`.
- A **estrela** carrega métricas (`price`, `freight_value`) na fato e contexto nas dimensões, encadeadas por `{{ ref(...) }}`.
- **SCD2** com `dbt snapshot` (`strategy='check'`) historiza `dim_sellers` quando um vendedor muda de UF.
- O **colunar** (DuckDB/Parquet) lê só as colunas necessárias e comprime muito — base do desempenho do DW.

### Para saber mais

- **Kimball Group — Dimensional Modeling Techniques:** https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/
- **dbt — How we structure our dbt projects (staging/core/marts):** https://docs.getdbt.com/best-practices/how-we-structure/1-guide-overview
- **dbt — Snapshots (SCD2):** https://docs.getdbt.com/docs/build/snapshots
- **Documentação Apache Parquet:** https://parquet.apache.org/docs/

## Aula 9 — Roteiro da Videoaula 9: "Data Warehouse e modelagem dimensional aplicada"

**Duração:** 9 a 10 minutos.

### 1. Abertura (0:00 – 0:45)

> "Na Unidade 2 deixamos prontas as nove tabelas de staging do Olist no dbt. Mas staging é só espelho da fonte. Quando a diretoria do marketplace pergunta 'faturamento por categoria e por UF no trimestre', precisamos de algo mais: um Data Warehouse. Hoje vamos construir o DW do Olist em camadas com dbt — staging, core com a estrela, e marts de negócio — e historizar os vendedores com SCD2."

### 2. Desenvolvimento — parte 1 (0:45 – 4:00)

> "Começo pela definição de Inmon aplicada ao Olist: orientado a assunto, integrado, não volátil, variante no tempo — a palavra-chave é OLAP, contra o OLTP do marketplace. Comparo Inmon e Kimball e digo qual escolhemos no projeto: híbrido com sabor Kimball, exatamente como o dbt recomenda estruturar. Aí mostro as três camadas virando pastas: models/staging que já temos, models/marts/core com dim e fct, e marts analíticos com os mart_."

### 3. Desenvolvimento — parte 2 (4:00 – 6:45)

> "Agora a estrela em SQL real. Abro o dim_customers e o fct_order_items: repare que o fato carrega só chaves e as métricas price e freight_value, com grão de um item, encadeado por ref. Tudo que é contexto — quem, o quê, quando, onde — vai para as dimensões. Esse ref é o que monta o lineage automático do dbt, ligando staging a core a marts."

### 4. Desenvolvimento — parte 3 (6:45 – 9:00)

> "E quando um seller muda de cidade? Se sobrescrevermos, perdemos o histórico. Mostro o SCD Tipo 2 com dbt snapshot e strategy check nas colunas seller_city e seller_state: o dbt cria dbt_valid_from e dbt_valid_to automaticamente. Fecho com o número: somar o faturamento da fct_order_items, 112 mil itens, toca menos de 2% dos bytes graças ao colunar do DuckDB. É por isso que a agregação roda instantânea no laptop."

### 5. Encerramento (9:00 – 9:45)

> "Temos o DW do Olist em camadas com a estrela e SCD2. Mas e os dados que não cabem na estrela — o texto livre dos reviews, arquivos brutos, histórico que queremos versionar? Na próxima aula organizamos o storage do Olist em Lakehouse, com Parquet em camadas bronze, silver e gold particionado por ano e mês. Te espero!"

---

## Aula 10 — Data Lake e Data Lakehouse

Na Aula 9 montamos o DW do Olist em camadas no DuckDB — ótimo para o que é tabular e limpo. Mas nem tudo no Olist cabe bem numa estrela: o `review_comment_message` é texto livre, queremos guardar os CSVs crus de forma auditável, e seria valioso "ver o Olist como estava mês passado". Para acomodar essa variedade e versionar o histórico, surge o **Data Lake** — e sua armadilha, o **data swamp**. Nesta aula vamos organizar o storage do Olist na **arquitetura Medallion** (bronze/silver/gold em Parquet), com o DuckDB lendo **Parquet particionado por ano/mês** como um **lakehouse local**, e entender, na teoria, como Delta e Iceberg dariam ACID e **time travel** ao projeto.

### Os limites do Data Warehouse

O DW clássico tem três limitações que a era do Big Data expôs e que sentimos no Olist:

1. **Esquema rígido (schema-on-write):** você define a estrutura **antes** de gravar. O texto dos reviews e payloads que mudam de forma sofrem.
2. **Custo de armazenamento:** guardar petabytes de histórico bruto em formato proprietário sairia caro.
3. **Variedade limitada:** texto livre, imagens, JSON não se encaixam bem no relacional.

Justamente os dados "difíceis" (o comentário do review) são valiosos para ciência de dados — e o DW não os acolhe bem.

### O Data Lake e o risco do data swamp

Um **Data Lake** armazena dados **em formato bruto e nativo**, sem exigir esquema prévio (**schema-on-read** — a estrutura é aplicada na leitura). Tipicamente vive sobre armazenamento de objetos barato como **Amazon S3, Google Cloud Storage ou Azure Data Lake Storage**. No nosso projeto local, o "object storage" é simplesmente a pasta `data/` com os CSVs e Parquets do Olist.

A vantagem é a flexibilidade: jogue tudo lá, decida depois. O perigo é esse mesmo: sem governança, catálogo e qualidade, o lago vira um **data swamp** — arquivos sem documentação, sem dono e sem confiabilidade. Se largássemos os 9 CSVs do Olist soltos sem padronizar nomes, tipos e camadas, ninguém saberia qual `order_items` é o oficial.

![Centro de dados em nuvem: o tipo de infraestrutura de armazenamento de objetos de baixo custo sobre a qual Data Lakes e Lakehouses são construídos](https://commons.wikimedia.org/wiki/Special:FilePath/CERN_Server_03.jpg)

### Formatos de tabela abertos (Delta, Iceberg, Hudi) — teoria sobre o Olist

O problema histórico do Data Lake era a ausência de garantias **ACID**. Escrever num lago de Parquet podia deixar leituras inconsistentes no meio de uma atualização. Os **formatos de tabela abertos** resolvem com uma **camada de metadados transacional** sobre os arquivos:

| Formato | Origem | Destaques |
| --- | --- | --- |
| **Delta Lake** | Databricks | Transações ACID, time travel, `MERGE`, forte no ecossistema Spark |
| **Apache Iceberg** | Netflix | Evolução de esquema/partição, snapshots, neutro em relação a engine |
| **Apache Hudi** | Uber | Upserts eficientes, ingestão incremental, foco em CDC |

Para o Olist, o ganho concreto desses formatos seria o **time travel**: poder consultar "como estava a tabela de pedidos no fechamento de janeiro/2018" — auditável, sem manter cópias manuais. Nosso lake local em Parquet puro não tem isso nativamente; Delta/Iceberg adicionariam essa máquina do tempo.

### A arquitetura Lakehouse

A **arquitetura Lakehouse** (termo da Databricks) une o melhor dos dois mundos:

- A **flexibilidade e o baixo custo** do Data Lake (object storage, qualquer tipo de dado, formatos abertos).
- A **confiabilidade e o desempenho** do Data Warehouse (ACID, governança, esquema, otimização de consulta).

No nosso projeto, o **DuckDB lendo Parquet** já é um **lakehouse local**: o motor analítico SQL roda direto sobre os arquivos do lake, sem precisar carregar tudo para dentro de um DW separado. É a mesma cópia única servindo BI, SQL ad hoc e (na Aula 16) treino de ML.

### Arquitetura Medallion aplicada ao Olist (bronze/silver/gold)

Para organizar o lakehouse e fugir do swamp, a Databricks popularizou a **arquitetura Medallion**, com três camadas de qualidade crescente — e é exatamente assim que estruturamos o `data/` do Olist:

- **Bronze (`data/bronze/`):** os CSVs do Olist convertidos para Parquet, crus e fiéis à fonte (já fizemos na Aula 2). Histórico auditável.
- **Silver (`data/silver/`):** o resultado dos modelos `staging` materializado em Parquet — limpo, deduplicado, tipado.
- **Gold (`data/gold/`):** os `marts` exportados em Parquet, prontos para BI e ML.

O dado **flui de bronze para gold**, ganhando qualidade e perdendo volume. É o equivalente lakehouse das camadas staging/core/marts do dbt — bronze ↔ raw, silver ↔ staging, gold ↔ marts.

### DuckDB lendo Parquet particionado por ano/mês

A chave de desempenho do lake é o **particionamento**. Exportamos os pedidos do gold particionados pelo ano e mês de `order_purchase_timestamp`; assim, uma análise de um mês lê **só aquela pasta**, não os 25 meses do Olist (partition pruning físico):

```sql
-- exporta gold particionado por ano/mês (DuckDB)
COPY (
  SELECT *,
         year(date_key)  AS year,
         month(date_key) AS month
  FROM   fct_orders
) TO 'data/gold/orders'
  (FORMAT PARQUET, PARTITION_BY (year, month), OVERWRITE_OR_IGNORE);
```

E para ler de volta, o DuckDB usa hive partitioning e poda as partições no `WHERE`:

```sql
SELECT count(*)
FROM read_parquet('data/gold/orders/**/*.parquet', hive_partitioning = true)
WHERE year = 2018 AND month = 1;
```

### Exemplo numérico: particionamento reduz o scan

O Olist cobre set/2016 a out/2018 — aproximadamente **25 meses**. Se uma análise precisa de **um único mês** (digamos, jan/2018) e os ~99.441 pedidos estão distribuídos de forma aproximadamente uniforme, a leitura particionada toca:

$$
\frac{99\,441}{25} \approx 3\,978\ \text{pedidos}\ \ (\approx 4{,}0\%\ \text{do total})
$$

Sem particionamento, a mesma consulta varreria os 99.441 pedidos para depois filtrar. O fator de redução de scan é:

$$
\frac{1}{25} = 0{,}04 \ \Rightarrow\ \text{varre}\ \sim\!25\times\ \text{menos dados}
$$

E o custo de manter esse lakehouse local é **R\$ 0,00**: roda no laptop com DuckDB + Parquet, sem DW gerenciado.

### Atividade prática

No seu projeto Olist:

1. Materialize a camada **silver** exportando `stg_order_items` para `data/silver/order_items.parquet`.
2. Exporte `fct_orders` para `data/gold/orders` particionado por `year` e `month` (use o `COPY ... PARTITION_BY` acima).
3. Rode a consulta de contagem de um mês com `hive_partitioning=true` e compare com a contagem total.
4. Escreva, em duas linhas, **como o Delta Lake** daria *time travel* a essa tabela gold — e que pergunta de auditoria do Olist isso responderia.

### Pontos-chave

- O **DW** sofre com esquema rígido, custo e variedade — por isso o Olist também ganha um **lake** (texto de reviews, histórico bruto).
- O **Data Lake** acolhe dados brutos (schema-on-read), mas sem governança vira **data swamp**.
- **Delta, Iceberg e Hudi** trazem ACID e **time travel** ao lago — no Olist, "ver a tabela como estava mês passado".
- O **DuckDB lendo Parquet** é um **lakehouse local**: SQL analítico sobre a mesma cópia única, de graça.
- A **Medallion** organiza `data/` em **bronze → silver → gold**, espelhando raw → staging → marts; **Parquet particionado por ano/mês** poda o scan.

### Para saber mais

- **Databricks — What is a Data Lakehouse?:** https://www.databricks.com/glossary/data-lakehouse
- **Databricks — Medallion Architecture:** https://www.databricks.com/glossary/medallion-architecture
- **DuckDB — Reading and writing Parquet:** https://duckdb.org/docs/data/parquet/overview
- **DuckDB — Partitioned writes (PARTITION_BY):** https://duckdb.org/docs/data/partitioning/partitioned_writes

## Aula 10 — Roteiro da Videoaula 10: "Data Lake e Data Lakehouse"

**Duração:** 9 a 10 minutos.

### 1. Abertura (0:00 – 0:45)

> "Na Aula 9 montamos o DW do Olist em camadas no DuckDB, ótimo para o que é tabular. Mas o texto livre dos reviews não cabe na estrela, queremos guardar os CSVs crus de forma auditável e poder ver o Olist como estava mês passado. Hoje organizamos o storage do Olist em Lakehouse: Parquet em bronze, silver e gold, particionado por ano e mês, com o DuckDB lendo direto como um lakehouse local."

### 2. Desenvolvimento — parte 1 (0:45 – 4:00)

> "Começo pelos limites do DW: esquema rígido, custo e variedade. Aí entra o Data Lake, schema-on-read sobre object storage barato — no nosso caso, a pasta data com os CSVs e Parquets do Olist. Mostro a vantagem da flexibilidade e o perigo: sem governança, os nove CSVs soltos viram um data swamp onde ninguém sabe qual order_items é o oficial."

### 3. Desenvolvimento — parte 2 (4:00 – 6:45)

> "Como resgatar a confiabilidade? Formatos de tabela abertos: Delta da Databricks, Iceberg do Netflix, Hudi do Uber, todos com ACID e time travel. Para o Olist, o ganho concreto é o time travel — consultar a tabela de pedidos como estava no fechamento de janeiro de 2018. Em cima disso defino o Lakehouse, e mostro que o DuckDB lendo Parquet já é o nosso lakehouse local: SQL direto sobre a mesma cópia única."

### 4. Desenvolvimento — parte 3 (6:45 – 9:00)

> "Para organizar e fugir do swamp, a Medallion aplicada ao data do Olist: bronze são os CSVs convertidos em Parquet, silver é o staging materializado, gold são os marts. Mostro o COPY com PARTITION_BY ano e mês exportando os pedidos, e a leitura com hive_partitioning podando o WHERE. O número: o Olist tem 25 meses; ler um mês toca cerca de 4% dos pedidos, varre 25 vezes menos dados, e custa zero no laptop."

### 5. Encerramento (9:00 – 9:45)

> "Temos o lakehouse local do Olist em Medallion, particionado e de graça. Mas e quando o Olist crescer e precisar de nuvem? A boa notícia: o mesmo dbt migra trocando o profile. Na próxima aula pego os nossos modelos stg, dim e fct e mostro como rodariam num Data Warehouse na nuvem — BigQuery — com partição, clustering e o impacto no custo. Te espero!"

---

## Aula 11 — Data Warehouses na nuvem (BigQuery, Snowflake, Redshift)

Até aqui o pipeline do Olist roda 100% local: DuckDB + dbt + Parquet, de graça no laptop. Isso é perfeito para aprender e para volumes como os ~120 MB do Olist. Mas e quando o marketplace virar "Olist × 1000" e os dados não couberem num laptop? A resposta da indústria são os **Data Warehouses na nuvem** — **BigQuery, Snowflake e Redshift** — apoiados numa ideia poderosa: **separar armazenamento de computação**. A melhor parte, e a mensagem central desta aula: **o mesmo projeto dbt do Olist migra para a nuvem trocando o adapter e o `profiles.yml`** — os modelos `stg_*`, `dim_*` e `fct_*` continuam idênticos. Vamos demonstrar (sem precisar de conta) e medir o impacto de **particionamento + clustering** no custo.

### Separação de armazenamento e computação

No DW tradicional (on-premises), **armazenamento e processamento eram acoplados** — escalar um exigia escalar o outro. A nuvem **desacoplou**:

- **Armazenamento:** os dados ficam em object storage barato e elástico (como nosso Parquet, só que gerenciado).
- **Computação:** clusters/motores são acionados sob demanda para processar consultas.

As consequências: **múltiplos clusters lendo os mesmos dados** sem conflito (BI e ML não competem), **escalar** para uma consulta pesada e desligar depois, e **pagar storage e compute separadamente**. O DuckDB local já antecipa essa ideia (motor sobre arquivos Parquet); a nuvem só a industrializa e a torna elástica.

![Servidores em um data center em nuvem: a infraestrutura elástica que sustenta a separação entre armazenamento e computação nos DWs em nuvem](https://commons.wikimedia.org/wiki/Special:FilePath/Wikimedia_Foundation_Servers-8055_35.jpg)

### BigQuery, Snowflake e Redshift

| Atributo | BigQuery (Google) | Snowflake | Redshift (AWS) |
| --- | --- | --- | --- |
| **Modelo** | Serverless puro (sem clusters a gerenciar) | Virtual warehouses (clusters lógicos) | Clusters provisionados + Serverless |
| **Cobrança padrão** | Por TB varrido (on-demand) ou slots | Por segundo de compute ativo | Por hora de cluster (ou por uso no serverless) |
| **Nuvem** | Google Cloud | Multi-cloud (AWS, Azure, GCP) | AWS |
| **Diferencial** | Zero administração, escala automática | Separação total storage/compute, sharing | Integração nativa com ecossistema AWS |

Para o Olist usaremos o **BigQuery** na demonstração (serverless, cobra por TB varrido — ótimo para mostrar custo). O ponto pedagógico vale para os três: nenhum exige reescrever nossos modelos dbt.

### ClickHouse: OLAP colunar de alta performance (com conta na nuvem)

BigQuery, Snowflake e Redshift não são as únicas opções. O **ClickHouse** é um banco **colunar** open-source famoso pela **velocidade** em consultas analíticas — agregações sobre bilhões de linhas em frações de segundo —, muito usado como camada de *analytics* quase em tempo real. Diferente das demonstrações anteriores (que rodam sem conta), aqui vale **colocar a mão na massa na nuvem de verdade**: o **ClickHouse Cloud** oferece um *trial* gratuito com conta online.

Roteiro mão na massa (≈15 min): crie a conta gratuita no **ClickHouse Cloud** (`clickhouse.com/cloud`), exporte a `fct_order_items` do Olist para CSV/Parquet e carregue-a numa tabela com o motor **`MergeTree`** (o coração colunar do ClickHouse), usando `ORDER BY (product_category_name, order_purchase_date)` — que faz, de uma vez, o papel de partição e de clustering. Rode então a mesma agregação de faturamento por categoria que fizemos no DuckDB: a query que varre a categoria inteira volta praticamente instantânea, o efeito de um motor colunar projetado para OLAP. *A lição: a separação storage/compute e o pruning colunar não são exclusivos dos três grandes — são o padrão de todo DW analítico moderno.*

### Trocar o adapter: dbt-duckdb → dbt-bigquery

A migração do Olist para a nuvem é, na prática, **trocar o adapter do dbt e o `profiles.yml`**. Hoje temos:

```yaml
# profiles.yml — local (DuckDB)
dbt_olist:
  target: dev
  outputs:
    dev:
      type: duckdb
      path: olist.duckdb
      schema: marts
```

Para a nuvem, instalamos `dbt-bigquery` e apontamos para o projeto/dataset — **os modelos `stg_orders`, `dim_customers`, `fct_order_items` não mudam uma linha**:

```yaml
# profiles.yml — nuvem (BigQuery)
dbt_olist:
  target: prod
  outputs:
    prod:
      type: bigquery
      method: service-account
      project: olist-analytics
      dataset: marts
      keyfile: ~/.gcp/olist-sa.json
      location: US
      threads: 4
```

É a materialização da mensagem do curso: *o que roda local com DuckDB+dbt migra para a nuvem trocando o profile; os conceitos são os mesmos.*

### Particionamento e clustering no fct_order_items

Na nuvem que cobra por **byte lido**, duas técnicas derrubam o custo — e o dbt as expõe via `config()` no próprio modelo. Particionamos a `fct_order_items` por data de compra e clusterizamos pela categoria mais filtrada:

```sql
-- models/marts/core/fct_order_items.sql (config p/ BigQuery)
{{ config(
    materialized='table',
    partition_by={'field': 'order_purchase_date', 'data_type': 'date'},
    cluster_by=['product_category_name']
) }}
select
    order_id, order_item_id, product_id, seller_id, customer_id,
    cast(purchased_at as date) as order_purchase_date,
    product_category_name,
    price, freight_value
from {{ ref('fct_order_items_base') }}
```

- **Particionamento** por `order_purchase_date`: um `WHERE order_purchase_date = '2018-01-15'` lê **só aquela partição** (partition pruning) — o mesmo conceito do Parquet particionado da Aula 10.
- **Clustering** por `product_category_name`: ordena dentro da partição e deixa o motor pular blocos sem a categoria buscada (block pruning).

### Custo por dado lido e FinOps

Entender a cobrança evita sustos. No **on-demand** do BigQuery você paga por **byte lido** (referência da ordem de **US\$ 6,25 por TB**). A disciplina de FinOps no Olist seria: particionar por padrão, exigir filtro na coluna de partição, evitar `SELECT *` e usar o **dry run** (estimativa de bytes antes de rodar). A mesma query pode custar centavos ou centenas de dólares dependendo da modelagem — e isso é responsabilidade do engenheiro de dados.

### Exemplo numérico: custo de uma query no "Olist × 1000"

O Olist real é pequeno demais para gerar custo relevante na nuvem (uma query nele lê megabytes). Para enxergar o efeito, projete **Olist × 1000** — cerca de **100 milhões de itens**, uma `fct_order_items` de aproximadamente **2 TB**, com 25 meses particionados. Um analista filtra **um mês** e seleciona poucas colunas.

**Sem partição, com `SELECT *`** (lê os 2 TB):

$$
2\,\text{TB} \times 6{,}25 = \text{US\$ }12{,}50\ \text{por consulta}
$$

**Com partição por mês** (1 de ~25 meses) **e seleção de ~10% das colunas:**

$$
2 \times \frac{1}{25} \times 0{,}10 \times 6{,}25 = 0{,}008 \times 6{,}25 = \text{US\$ }0{,}05\ \text{por consulta}
$$

Uma diferença de **~250×** na mesma pergunta. Com 20 analistas rodando 30 consultas/dia em 22 dias úteis, a versão ingênua custaria

$$
20 \times 30 \times 12{,}50 \times 22 = \text{US\$ }165\,000\ \text{/mês}
$$

contra **~US\$ 660/mês** na versão particionada e enxuta. É a diferença entre um projeto inviável e um trivial — sem trocar uma linha da lógica dos modelos.

### Pausa para Reflexão

> Antes de olhar a conta acima, faça a estimativa de cabeça no "Olist × 1000": se a `fct_order_items` tem ~2 TB e você varre a tabela inteira contra uma única partição de mês, quantas vezes menos dados a versão particionada lê? E se ainda selecionar só 10% das colunas? Anote seu palpite em uma frase e compare com os 250× do exemplo — perceber essa ordem de grandeza *antes* de rodar a query é exatamente a intuição de FinOps que separa o engenheiro que controla o custo do que recebe a fatura no fim do mês.

### Atividade prática

Sem precisar de conta na nuvem:

1. Crie um `profiles.yml` com um segundo target `prod` do tipo `bigquery` (preencha `project`/`dataset` fictícios) e mantenha o `dev` DuckDB.
2. Adicione o bloco `config(partition_by=..., cluster_by=...)` ao topo de `fct_order_items.sql`.
3. Rode `dbt parse` (ou `dbt compile --target dev`) e confirme que os modelos **compilam sem alteração de lógica**.
4. Estime, com a fórmula de US\$ 6,25/TB, o custo de uma query que varre 1 mês de uma `fct_order_items` de 5 TB particionada por mês.

### Pontos-chave

- A **separação storage/compute** torna o DW em nuvem elástico — o DuckDB local já antecipa a ideia sobre Parquet.
- **BigQuery** (serverless), **Snowflake** (virtual warehouses), **Redshift** (AWS) e **ClickHouse** (colunar open-source, com ClickHouse Cloud) têm filosofias distintas; nenhum exige reescrever os modelos dbt.
- Migrar o Olist é **trocar o adapter e o `profiles.yml`** (`dbt-duckdb` → `dbt-bigquery`); `stg_*`/`dim_*`/`fct_*` ficam idênticos.
- **Particionar** por `order_purchase_date` + **clusterizar** por `product_category_name` ativa pruning e derruba o custo por byte.
- No "Olist × 1000", a mesma query pode custar **US\$ 12,50 ou US\$ 0,05** — **otimização e FinOps** são parte do trabalho.

### Para saber mais

- **dbt — BigQuery configs (partition + cluster):** https://docs.getdbt.com/reference/resource-configs/bigquery-configs
- **BigQuery — Partitioned tables:** https://cloud.google.com/bigquery/docs/partitioned-tables
- **BigQuery — Clustered tables:** https://cloud.google.com/bigquery/docs/clustered-tables
- **ClickHouse Cloud — trial gratuito e início rápido (OLAP colunar):** https://clickhouse.com/cloud

## Aula 11 — Roteiro da Videoaula 11: "Data Warehouses na nuvem (BigQuery, Snowflake, Redshift)"

**Duração:** 9 a 10 minutos.

### 1. Abertura (0:00 – 0:45)

> "Até aqui o pipeline do Olist roda 100% local: DuckDB, dbt e Parquet, de graça no laptop. Perfeito para os 120 MB do Olist. Mas e quando virar Olist vezes mil e não couber no laptop? A resposta da indústria são os Data Warehouses na nuvem. E a melhor notícia: o mesmo projeto dbt migra trocando o adapter. Hoje pego os nossos modelos e mostro como rodariam no BigQuery, com partição, clustering e o impacto no custo."

### 2. Desenvolvimento — parte 1 (0:45 – 4:00)

> "Começo pela separação storage e compute: no on-premises eram acoplados; na nuvem, dados ficam em object storage barato e a computação é acionada sob demanda. Nosso DuckDB sobre Parquet já antecipa isso. Comparo os três grandes — BigQuery serverless, Snowflake com virtual warehouses, Redshift na AWS. E não para neles: mostro também o ClickHouse, um colunar open-source absurdamente rápido pra OLAP, com um ClickHouse Cloud gratuito onde dá pra botar a mão na massa — criar conta, carregar a fct_order_items numa tabela MergeTree e sentir a velocidade. E aí o ponto central: nenhum deles exige reescrever nossos modelos dbt do Olist."

### 3. Desenvolvimento — parte 2 (4:00 – 6:45)

> "Mostro na tela: o profiles.yml local é type duckdb apontando para olist.duckdb. Para a nuvem, troco para type bigquery com project e dataset — e os modelos stg_orders, dim_customers, fct_order_items não mudam uma linha. Essa é a mensagem do curso inteira. Depois adiciono o config no fct_order_items: partition_by por order_purchase_date e cluster_by por product_category_name — o mesmo conceito do Parquet particionado da aula passada, agora ativando pruning na nuvem."

### 4. Desenvolvimento — parte 3 (6:45 – 9:00)

> "O Olist real é pequeno demais para custar na nuvem, então projeto Olist vezes mil: uma fct de 2 TB. Sem partição e com SELECT estrela, 12 dólares e 50 por consulta. Com partição por mês e poucas colunas, 5 centavos — 250 vezes menos. Com 20 analistas, isso é a diferença entre 165 mil dólares por mês e 660. Tudo isso sem trocar uma linha da lógica dos modelos. Otimização e FinOps são trabalho de engenheiro de dados."

### 5. Encerramento (9:00 – 9:45)

> "Vimos que o dbt do Olist sobe para a nuvem trocando só o profile, com partição e clustering controlando o custo. Já temos onde guardar, local e na nuvem. Falta juntar tudo num ecossistema coerente. Na próxima aula, que fecha a unidade, montamos a Modern Data Stack completa do Olist: ingestão, dbt com docs e lineage, o warehouse, e um dashboard no Metabase. Te espero!"

---

## Aula 12 — Modern Data Stack e arquitetura de dados na nuvem

Nas aulas desta unidade construímos as peças do Olist: o DW em camadas (Aula 9), o lakehouse Medallion (Aula 10) e a ponte para a nuvem (Aula 11). Mas como tudo isso vira um **ecossistema coerente** que uma empresa realmente opera? A resposta tem nome: **Modern Data Stack (MDS)** — um conjunto modular de ferramentas plugáveis, centrado no DW/Lakehouse. Nesta aula que fecha a unidade vamos **montar a MDS do Olist de ponta a ponta**: ingestão → transformação com dbt (gerando **docs e lineage**) → storage no DuckDB/DW → **BI com um dashboard no Metabase**. E discutimos o **data mesh**, tratando cada domínio do Olist (vendas, logística, reviews) como um data product.

### O que é a Modern Data Stack

A **Modern Data Stack** arquiteta a plataforma com **ferramentas modulares, gerenciadas e centradas no warehouse/lakehouse**, conectadas por padrões abertos — você compõe a melhor ferramenta de cada categoria. O fio condutor é o **ELT**: primeiro **carrega** o bruto, **depois transforma** com SQL. Mapeada no nosso projeto Olist, a stack já existe quase inteira:

1. **Ingestão** (`ingestion/load_raw.py`, ou Airbyte/Fivetran na nuvem) → CSVs do Olist no schema `raw`.
2. **Armazenamento** (DuckDB local, ou BigQuery/Snowflake) → o coração.
3. **Transformação** (**dbt**: `stg_*` → `dim_*`/`fct_*` → `mart_*`) → modela dentro do warehouse.
4. **BI** (**Metabase**, Power BI, Looker) → dashboards do Olist ao usuário final.
5. **Orquestração e observabilidade** (Airflow `olist_pipeline`; observabilidade vem na Unidade 4) → cola e monitora.

![Servidores e cabeamento de um data center: a infraestrutura em nuvem sobre a qual a Modern Data Stack conecta ingestão, armazenamento, transformação e BI em módulos plugáveis](https://commons.wikimedia.org/wiki/Special:FilePath/Datacenter-telecom.jpg)

### Ingestão gerenciada (Fivetran, Airbyte)

Escrever conectores para cada fonte é repetitivo. Ferramentas de ingestão gerenciada resolvem com **conectores prontos**:

- **Fivetran:** SaaS comercial, centenas de conectores, sincronização incremental automática; cobra por **MAR (Monthly Active Rows)**.
- **Airbyte:** alternativa open source (com cloud), conectores customizáveis; atrai quem quer controle e custo menor.

No Olist local, esse papel é do nosso `load_raw.py` (lê os CSVs do Kaggle para o `raw`). Se o Olist fosse um Postgres ao vivo, um conector Airbyte/Fivetran substituiria o script — é o "L" (Load) do ELT industrializado, sem código de extração.

### Transformação com dbt: docs e lineage do Olist

O **dbt** já é o "T" da nossa stack desde a Unidade 2, e agora colhemos dois recursos poderosos: **documentação** e **lineage**. Com um comando, o dbt gera um catálogo navegável e o grafo de dependências de todo o pipeline do Olist:

```bash
# gera o catálogo + lineage e sobe o site de docs do Olist
dbt docs generate
dbt docs serve --port 8080
```

No site, o **DAG de lineage** mostra `stg_orders` → `fct_orders` → `mart_delivery_performance`, com descrições e testes de cada modelo. Isso é a espinha dorsal da MDS: o dbt traz **modelos versionados em Git, lineage automático, testes e docs** — práticas de engenharia de software aplicadas à análise, materializando as camadas silver/gold da Medallion.

### Camada semântica e BI: dashboard do Olist no Metabase

Aqui mora um problema clássico: dois relatórios mostram "faturamento" diferente porque cada analista calculou à sua maneira. A **camada semântica** define **métricas e dimensões de forma centralizada** — "faturamento líquido" é definido uma vez (como um modelo/mart no dbt) e todo o BI consome a mesma definição.

Sobre essa camada vem o **BI**. No projeto Olist conectamos o **Metabase ao DuckDB** (driver community) e montamos um dashboard sobre os marts:

- **Vendas por categoria** (de `mart_sales_by_category`): top categorias do Olist.
- **Performance de entrega** (de `mart_delivery_performance`): % no prazo, atraso médio por UF.
- **Reviews**: distribuição das notas 1–5 (média ≈ 4,0).

Metabase, Power BI, Looker e Superset são opções; o Metabase é open source e lê o DuckDB direto, mantendo o projeto 100% local e grátis.

### Data mesh: o Olist em domínios

Conforme a empresa cresce, um time central de dados vira gargalo. O **data mesh** (proposto por Zhamak Dehghani) descentraliza a responsabilidade, com quatro princípios — e o Olist ilustra bem cada domínio como **data product**:

1. **Propriedade orientada a domínio:** o domínio **Vendas** é dono de `fct_order_items`/`mart_sales_by_category`; **Logística**, de `mart_delivery_performance`; **Reviews**, dos dados de avaliação.
2. **Dados como produto:** cada mart vira um produto com dono, SLA, documentação (a do `dbt docs`) e qualidade (os testes).
3. **Plataforma self-service:** o mesmo `dbt_olist/` + DuckDB serve a todos os domínios.
4. **Governança federada computacional:** padrões globais (nomenclatura `stg_`/`dim_`/`fct_`/`mart_`, testes obrigatórios) aplicados de forma automatizada.

Data mesh é **mudança organizacional**, não ferramenta; para um projeto do porte do Olist, uma stack centralizada já basta — mas o vocabulário de "dados como produto" guia boas decisões.

### Exemplo numérico: TCO do "Olist em produção" vs local

Estime o **TCO (Custo Total de Propriedade)** mensal se o Olist virasse produção na nuvem:

| Componente | Ferramenta | Custo mensal (R\$) |
| --- | --- | --- |
| Ingestão | Airbyte Cloud (volume baixo) | 1.500,00 |
| Armazenamento + compute | BigQuery (on-demand + storage) | 2.500,00 |
| Transformação | dbt Cloud (2 desenvolvedores) | 1.000,00 |
| BI | Metabase (open source, self-host) | 500,00 |
| **Total ferramentas** | | **5.500,00** |

$$
\text{TCO ferramentas (nuvem)} = 1\,500 + 2\,500 + 1\,000 + 500 = \text{R\$ }5\,500{,}00\ \text{/mês}
$$

Agora compare com a **stack local do curso** (DuckDB + dbt-core + Airflow + Metabase open source no laptop): praticamente **R\$ 0,00 de ferramentas** — só o custo do hardware já existente. Para o volume do Olist (~120 MB), a stack local entrega o mesmo resultado de graça; a MDS na nuvem só passa a valer a pena quando o volume e a concorrência de usuários crescem. A lição: **comece local e barato; suba para a MDS na nuvem quando o problema justificar.**

### Atividade prática

Monte a **MDS do Olist** no papel e na prática:

1. Rode `dbt docs generate && dbt docs serve` e navegue pelo **lineage** de `mart_delivery_performance` até as fontes.
2. Conecte o **Metabase ao DuckDB** (driver community) e crie **um gráfico** de vendas por categoria a partir de `mart_sales_by_category`.
3. Liste os **três domínios** do Olist (vendas, logística, reviews) e o **data product** (mart) de cada um.
4. Compare o **TCO** da versão local (~R\$ 0) com a versão na nuvem (~R\$ 5,5 mil/mês) e diga **a partir de que volume** migrar.

### O que você verá na próxima unidade

Na **Unidade 4**, vamos do "como armazenar e arquitetar" para o "como confiar e governar". O foco será **Qualidade, Governança e DataOps**: adicionaremos **testes de qualidade** ao pipeline do Olist (dbt tests no `schema.yml` — `not_null` em `order_id`, `relationships` de `fct` para `dim` — e **Great Expectations** validando `review_score` entre 1 e 5 e datas de entrega ≥ compra); trataremos **governança e LGPD** (o Olist já é pseudonimizado — IDs hash, geolocalização por prefixo de CEP — caso real da Lei 13.709/2018, com mascaramento e lineage como base do direito de exclusão); e aplicaremos **DataOps** (CI/CD com GitHub Actions rodando `dbt build` a cada PR, write-audit-publish), fechando com **IA** (um modelo scikit-learn lendo o gold para prever atraso de entrega). É a hora de transformar um pipeline que **funciona** em um pipeline em que se pode **confiar**.

### Pontos-chave

- A **MDS do Olist** já existe quase inteira: `load_raw.py` (ingestão) + **dbt** (transformação) + DuckDB/DW (storage) + **Metabase** (BI) + Airflow (orquestração).
- **Fivetran** (SaaS) e **Airbyte** (open source) substituiriam o `load_raw.py` se o Olist fosse uma fonte ao vivo — o "L" do ELT sem código.
- **`dbt docs generate`** entrega catálogo e **lineage** (`stg_orders` → `fct_orders` → `mart_*`) — testes, docs e versionamento como num projeto de software.
- O **Metabase sobre o DuckDB** dá um dashboard do Olist (vendas, entregas, reviews) de graça; a **camada semântica** padroniza métricas.
- **Data mesh** trata cada domínio do Olist (vendas, logística, reviews) como **data product**; comece local (~R\$ 0) e suba para a nuvem quando o volume justificar.

### Para saber mais

- **dbt — About documentation (docs & lineage):** https://docs.getdbt.com/docs/build/documentation
- **Metabase — Documentação oficial:** https://www.metabase.com/docs/latest/
- **dbt Labs — What is data mesh?:** https://www.getdbt.com/blog/what-is-data-mesh-the-definition-and-importance-of-data-mesh
- **Martin Fowler — Data Mesh Principles:** https://martinfowler.com/articles/data-mesh-principles.html

## Aula 12 — Roteiro da Videoaula 12: "Modern Data Stack e arquitetura de dados na nuvem"

**Duração:** 9 a 10 minutos.

### 1. Abertura (0:00 – 0:45)

> "Nesta unidade construímos as peças do Olist: o DW em camadas, o lakehouse Medallion e a ponte para a nuvem. Mas como tudo isso vira um ecossistema coerente que uma empresa opera? A resposta tem nome: Modern Data Stack. Hoje, fechando a unidade, montamos a MDS do Olist de ponta a ponta: ingestão, dbt com docs e lineage, o warehouse e um dashboard no Metabase. E falamos de data mesh."

### 2. Desenvolvimento — parte 1 (0:45 – 4:00)

> "A Modern Data Stack é modular, centrada no warehouse e baseada em ELT: carrega o bruto, transforma depois. E o legal: a stack do Olist já existe quase inteira. Mostro as camadas: load_raw.py na ingestão, DuckDB no armazenamento, dbt na transformação, Metabase no BI, Airflow na orquestração. Explico a ingestão gerenciada: Fivetran e Airbyte com conectores prontos substituiriam nosso script se o Olist fosse um Postgres ao vivo — o L do ELT, sem código de extração."

### 3. Desenvolvimento — parte 2 (4:00 – 6:45)

> "O dbt já é o T da nossa stack desde a Unidade 2. Agora colho dois recursos: docs e lineage. Rodo dbt docs generate e dbt docs serve e mostro o DAG: stg_orders puxa fct_orders que puxa mart_delivery_performance, com descrições e testes. Depois a camada semântica, que resolve dois relatórios com faturamentos diferentes, e conecto o Metabase ao DuckDB para um dashboard do Olist: vendas por categoria, entregas por UF, distribuição das notas de review."

### 4. Desenvolvimento — parte 3 (6:45 – 9:00)

> "Quando a empresa cresce, o time central vira gargalo. Aí entra o data mesh: cada domínio do Olist como data product — vendas dona do mart de vendas, logística do de entregas, reviews dos seus dados. É mudança organizacional, não ferramenta. E o número: o TCO do Olist em produção na nuvem dá cerca de 5,5 mil reais por mês; a nossa stack local com DuckDB e dbt-core entrega o mesmo para 120 megabytes, de graça. A lição: comece local e barato, suba para a nuvem quando o volume justificar."

### 5. Encerramento (9:00 – 9:45)

> "Fechamos a unidade de armazenamento e arquitetura: o pipeline do Olist está construído, da estrela ao lakehouse, da nuvem ao dashboard. Na próxima unidade vamos do 'como armazenar' para o 'como confiar': qualidade com dbt tests e Great Expectations, governança e LGPD sobre os dados pseudonimizados do Olist, DataOps com CI/CD, e o fechamento com um modelo de IA prevendo atrasos de entrega. Te espero!"

---

## Quiz não avaliativo

### Questão 1

Sobre a construção do **Data Warehouse do Olist com dbt** (camadas `staging` → `core` → `marts`) e o tratamento de **dimensões que mudam**, assinale a alternativa **correta**:

- [ ] a. No esquema estrela do Olist, a fato `fct_order_items` deve guardar os atributos descritivos (cidade do cliente, nome da categoria) e as dimensões guardam as métricas `price` e `freight_value`.
- [x] b. A fato `fct_order_items` guarda as métricas (`price`, `freight_value`) e as chaves para as dimensões; quando um seller muda de UF, usar **SCD2** com `dbt snapshot` preserva o histórico criando uma nova versão com `dbt_valid_from`/`dbt_valid_to`.
- [ ] c. Como o Olist é histórico e não muda, não faz sentido usar `dbt snapshot`; basta sobrescrever `dim_sellers` a cada execução (SCD Tipo 1).
- [ ] d. As camadas `staging`, `core` e `marts` devem ser todas materializadas como views para economizar disco, pois o dbt não permite materializar a `core` como tabela.

**Resposta correta:** `b`

**Feedback:** A (b) está correta: na estrela, a **fato** carrega métricas + chaves estrangeiras e as **dimensões** carregam o contexto; **SCD2** via `dbt snapshot` com `strategy='check'` historiza `dim_sellers` adicionando `dbt_valid_from`/`dbt_valid_to`. A (a) inverte fato e dimensão. A (c) é falsa: mesmo num dataset histórico, mudanças nas dimensões (um seller que muda de cidade entre 2016 e 2018) exigem SCD2 para atribuir vendas à localização correta de cada época. A (d) é falsa: o dbt permite escolher a materialização (`view`, `table`, `incremental`) por modelo — a `core` costuma ser `table`.

### Questão 2

No pipeline do Olist, você organizou o storage em **Medallion** e exportou `fct_orders` em **Parquet particionado por ano/mês** lido pelo DuckDB. Um analista precisa contar os pedidos de **janeiro/2018**. Qual abordagem **reduz mais** os dados varridos?

- [ ] a. Ler todos os Parquets de `data/gold/orders` para um DataFrame e só então filtrar por janeiro/2018 em memória, garantindo que nada seja perdido.
- [ ] b. Reverter a Medallion e voltar a consultar diretamente os 9 CSVs crus do Olist, que são mais rápidos por não terem metadados de partição.
- [x] c. Consultar com `read_parquet(..., hive_partitioning=true)` filtrando `WHERE year = 2018 AND month = 1`, para o DuckDB ler **apenas a pasta daquele mês** (partition pruning) — cerca de 1/25 dos pedidos.
- [ ] d. Carregar tudo num banco transacional por linha (OLTP), que é mais eficiente para varreduras analíticas de grandes volumes.

**Resposta correta:** `c`

**Feedback:** A (c) está correta: com `hive_partitioning=true` e filtro nas colunas de partição (`year`, `month`), o DuckDB faz **partition pruning** e lê só a pasta de jan/2018 — em ~25 meses, cerca de 1/25 dos dados. A (a) varre tudo antes de filtrar, anulando a vantagem do particionamento. A (b) é o oposto da Medallion: CSV cru não tem poda por partição e é mais lento para análise. A (d) é falsa: OLTP por linha é ruim para varreduras analíticas — o colunar particionado do lakehouse vence.

---

## Atividade Verificadora (AAI — Atividade Avaliativa Individual)

**Pergunta:**

> Você construiu o pipeline do Olist localmente com **DuckDB + dbt + Parquet** (DW em camadas, lakehouse Medallion, dashboard no Metabase), rodando de graça no laptop. O dataset tem ~99 mil pedidos e ~120 MB. Agora a empresa fictícia "Olist Analytics" cresceu: o volume vai para a casa dos **terabytes** (escala "Olist × 1000"), dezenas de analistas consultarão ao mesmo tempo e a diretoria pede uma proposta de **arquitetura na nuvem** com governança de custo.
>
> Estruture sua resposta em três partes:
>
> 1. **Arquitetura proposta** — DW na nuvem, Lakehouse ou ambos? Justifique pela variedade (texto dos reviews + dados tabulares) e pelos casos de uso (BI + ciência de dados). Indique as camadas (bronze/silver/gold ↔ staging/core/marts) e onde entra o **time travel**.
> 2. **Migração do dbt** — explique por que os modelos `stg_*`/`dim_*`/`fct_*` **não precisam ser reescritos** e o que de fato muda ao trocar `dbt-duckdb` por `dbt-bigquery`. Cite particionamento e clustering da `fct_order_items`.
> 3. **Controle de custo (FinOps)** — quais decisões de modelagem (formato colunar/Parquet, particionar por `order_purchase_date`, clusterizar por `product_category_name`, evitar `SELECT *`, dry run) e de governança você adotaria, e qual o **TCO mensal** aproximado.

**Resposta esperada:**

> Uma resposta de qualidade reconhece que, **no volume atual do Olist (~120 MB), a stack local DuckDB+dbt já basta** e migrar seria desperdício — o gatilho é o crescimento para terabytes e a concorrência de usuários. Para esse cenário, recomenda uma **arquitetura Lakehouse** (ou DW em nuvem + lake): há **variedade** (texto livre do `review_comment_message` + dados tabulares de pedidos/itens) e **dois consumidores** (BI exige confiabilidade e esquema; ciência de dados exige flexibilidade e histórico bruto). As camadas seguem a **Medallion** já implementada no Olist — **bronze** (CSVs em Parquet, auditável), **silver** (staging materializado), **gold** (marts) —, equivalente a raw → staging → marts do dbt; o **time travel** (Delta/Iceberg) responde auditorias como "o faturamento como estava no fechamento de jan/2018". Na **migração do dbt**, a resposta deve deixar claro o ponto central do curso: **os modelos `stg_orders`, `dim_customers`, `fct_order_items` ficam idênticos** — o que muda é só o `profiles.yml` (adapter `duckdb` → `bigquery`, com `project`/`dataset`/credenciais). Deve citar adicionar `config(partition_by={'field':'order_purchase_date'...}, cluster_by=['product_category_name'])` à `fct_order_items` para ativar partition/block pruning. No **FinOps**, espera-se: **Parquet/colunar**, **particionar por `order_purchase_date`** e **clusterizar** por categoria, **evitar `SELECT *`** (cada coluna lida custa), usar **dry run** (estimativa de bytes antes de rodar), e regras de governança (partição obrigatória, limites de custo por consulta, painéis de custo por time). Um **TCO** plausível para o "Olist em produção" fica em torno de **R\$ 5–6 mil/mês** de ferramentas (Airbyte + BigQuery + dbt Cloud + Metabase self-host), bem abaixo dos R\$ 17 mil de uma stack corporativa pesada — e a resposta deve contrastar com o **~R\$ 0 da versão local**. Deve demonstrar **pensamento de trade-off** (local vs nuvem; on-demand vs capacidade; quente vs frio) e **priorizar valor incremental** — migrar quando o volume justificar, não "tudo de uma vez".

---

## Material complementar

### Direto da fonte — livro da Biblioteca Virtual

> Este é o livro de cabeceira da Unidade 3: Kimball e Ross consolidam, em linguagem acessível, tudo o que aplicamos ao construir o **DW do Olist** — tabelas fato e dimensão, esquema estrela, Slowly Changing Dimensions (exatamente o SCD2 que usamos em `dim_sellers` via `dbt snapshot`) e o desenho de Data Warehouses que respondem às perguntas do negócio. É a referência canônica por trás das nossas camadas `staging → core → marts`.

- **Nome do livro:** *The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling* (3ª edição)
- **Capítulo:** Capítulo 1 — *Data Warehousing, Business Intelligence, and Dimensional Modeling Primer*
- **Organizador/Autores:** Ralph Kimball e Margy Ross
- **Editora:** Wiley
- **Link de acesso (BV):** https://plataforma.bvirtual.com.br/
- **Aula em que entra:** Aulas 9 a 12

### Para mergulhar no assunto

> Para fixar o **SCD Tipo 2** que implementamos em `dim_sellers`, recomendo o artigo clássico do **Kimball Group** sobre Slowly Changing Dimensions. Ele explica, com exemplos, por que (e quando) preservar o histórico de uma dimensão criando novas versões — exatamente o que o `dbt snapshot` automatiza no nosso pipeline quando um vendedor do Olist muda de cidade ou UF. É leitura curta e direta, da própria fonte que cunhou a técnica.

- **Link(s):** https://www.kimballgroup.com/2008/08/slowly-changing-dimensions/
- **Aula em que entra:** Aula 9

### Podcast (curadoria, até 45 min)

> O canal **dbt (dbt Labs)** no YouTube traz palestras e demonstrações diretas da fonte sobre **modelagem em camadas, testes, docs e lineage** — exatamente o que usamos para construir o DW do Olist (Aulas 9 e 12). Assistir a um vídeo de fundamentos do dbt reforça como o `staging → core → marts` e o `dbt docs` se encaixam na Modern Data Stack que montamos.

- **Nome do podcast/canal:** dbt (dbt Labs — canal oficial no YouTube)
- **Tema recomendado:** "How we structure dbt projects" / fundamentos de modelagem, testes e lineage
- **Link:** https://www.youtube.com/@dbt-labs (YouTube)
- **Aula em que entra:** Aulas 9 e 12

### Artigo científico

> Artigo seminal que define os fundamentos de **data warehousing e tecnologia OLAP** — da arquitetura em camadas à modelagem multidimensional e às técnicas de servidor OLAP. É a base conceitual sobre a qual a Aula 9 (e boa parte da unidade) está construída: por que separamos o DW analítico do Olist do OLTP do marketplace e por que o colunar do DuckDB é tão eficiente.

- **Link:** https://doi.org/10.1145/248603.248616 (DOI)
- **Aula em que entra:** Aula 9
- **Referência bibliográfica do artigo no formato ABNT:**
  > CHAUDHURI, Surajit; DAYAL, Umeshwar. **An overview of data warehousing and OLAP technology**. *ACM SIGMOD Record*, v. 26, n. 1, p. 65-74, mar. 1997.
