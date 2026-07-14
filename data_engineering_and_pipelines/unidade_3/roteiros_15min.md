# Roteiros Estendidos Hands-on (15–20 minutos) — Unidade 3: Armazenamento e Arquitetura de Dados

- **Disciplina:** Data Engineering and Pipelines
- **Conteudista:** Afonso Cesar Lelis Brandão
- **Videoaulas:** 9 a 12
- **Formato:** roteiro de gravação **hands-on em GitHub Codespaces** — fala em citação (>), código executado ao vivo. Duração-alvo: **15 a 20 minutos** por aula.

> **Convenções:** **[TELA]** slide/Codespace · **[CÓDIGO]** digitar/colar · **[EXECUTAR]** rodar e mostrar saída · **[CHECKPOINT]** resultado esperado.
> **Preparação da unidade:** Codespace com as Unidades 1–2 concluídas (`raw` carregado, `dbt_olist` com os `stg_*`, Airflow instalado). Para a Aula 12, rode `pip install plotly` **antes** de gravar. **Nenhuma aula desta unidade exige conta, chave de API ou serviço externo.**

---

## Roteiro da Videoaula 9 — "Data Warehouse em camadas: a estrela do Olist no dbt (com SCD2 ao vivo)"

**Duração-alvo:** 18 a 20 minutos.

### 1. Abertura (0:00 – 1:15)

**[TELA]** Slide de capa; Codespace ao lado.

> "Olá! Bem-vindo, bem-vinda à Unidade 3 — a unidade em que o dado do Olist ganha uma **casa bem arquitetada**. Na Unidade 2 deixamos prontos os modelos staging: dados limpos e tipados. Mas staging é só espelho da fonte — ele **não responde perguntas de negócio**. Quando a diretoria pergunta 'faturamento por categoria, por UF, no trimestre', precisamos de algo mais: um **Data Warehouse**. Hoje construímos o DW do Olist **em camadas, no dbt**: staging → core com a estrela → marts de negócio. E o ponto alto da aula: vamos **mudar a cidade de um vendedor ao vivo** e assistir ao `dbt snapshot` preservar a história com SCD Tipo 2 — aquele conceito que desenhamos no papel lá na Aula 4, agora rodando de verdade. Bora."

### 2. O que é um DW + Inmon × Kimball (1:15 – 3:45)

**[TELA]** Slide: os 4 adjetivos de Inmon sobre o Olist + tabela Inmon × Kimball.

> "A definição clássica é de **Bill Inmon**: um Data Warehouse é um repositório **orientado a assunto, integrado, não volátil e variante no tempo**. Quatro adjetivos abstratos que ficam concretos no Olist: **orientado a assunto** — organizamos por vendas, logística, reviews, não por arquivo CSV; **integrado** — as 9 tabelas viram um modelo único com nomes padronizados; **não volátil** — o pedido de 2017 nunca é sobrescrito; **variante no tempo** — guardamos o histórico inteiro, inclusive das dimensões: o seller que muda de UF. E o propósito é **OLAP** — poucas consultas que varrem os 112 mil itens para agregar — contra o **OLTP** do marketplace, muitas escritas pequenas."

> "E há duas escolas para construir DW. **Inmon**, top-down: primeiro o warehouse corporativo normalizado, depois os marts — sólido, lento. **Kimball**, bottom-up: data marts dimensionais entregues incrementalmente, integrados por dimensões conformadas — rápido ao valor. No projeto Olist, adotamos o **híbrido pragmático com sabor Kimball** — que é exatamente o padrão que o próprio dbt recomenda: uma camada `core` com a estrela conformada, e marts por área em cima. E essas três camadas lógicas viram, literalmente, **pastas do projeto**: `models/staging` — já temos —, `models/marts/core` — a estrela — e `models/marts/analytics` — os marts. Bora criar."

### 3. Mão na massa: completando o staging e o seed (3:45 – 6:15)

**[TELA]** Editor + terminal.

> "Antes da estrela, dois staging que faltavam e o nosso primeiro **seed**. Rápido:"

**[CÓDIGO]** Criar `models/staging/stg_sellers.sql` e `models/staging/stg_products.sql`:

```sql
-- stg_sellers.sql
select seller_id, seller_zip_code_prefix, seller_city, seller_state
from {{ source('olist_raw', 'sellers') }}
```

```sql
-- stg_products.sql
select product_id, product_category_name, product_weight_g
from {{ source('olist_raw', 'products') }}
```

**[CÓDIGO]** O seed — a tradução de categorias (71 linhas estáveis) versionada no repositório:

```bash
cp ../data/raw/product_category_name_translation.csv seeds/
dbt seed
```

**[CHECKPOINT]**

> "Olha o log do `dbt seed`: a tabela `product_category_name_translation` materializada com **71 linhas**. Lembra da regra da Aula 5: CSV pequeno e estável não merece pipeline de ingestão — vira **seed**, mora no Git junto do código, e o dbt materializa. Cada dado com o mecanismo do seu tamanho."

### 4. A estrela no core: dimensões e fato (6:15 – 10:00)

**[CÓDIGO]** Criar `models/marts/core/dim_customers.sql`:

```sql
select
    customer_id,
    customer_unique_id,
    customer_zip_code_prefix,
    customer_city,
    upper(customer_state) as customer_state
from {{ ref('stg_customers') }}
```

**[CÓDIGO]** Criar `models/marts/core/dim_products.sql` (já com a tradução do seed):

```sql
select
    p.product_id,
    p.product_category_name,
    t.product_category_name_english,
    p.product_weight_g
from {{ ref('stg_products') }} p
left join {{ ref('product_category_name_translation') }} t
       using (product_category_name)
```

**[CÓDIGO]** Criar `models/marts/core/fct_order_items.sql` — o coração do DW:

```sql
{{ config(materialized='table') }}

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

**[CÓDIGO]** E o primeiro mart analítico, `models/marts/analytics/mart_sales_by_category.sql`:

```sql
select
    d.product_category_name_english        as categoria,
    count(*)                               as itens,
    round(sum(f.price), 2)                 as faturamento
from {{ ref('fct_order_items') }} f
join {{ ref('dim_products') }}   d using (product_id)
group by 1
order by faturamento desc
```

**[EXECUTAR]**

```bash
dbt run --select marts
```

**[CHECKPOINT]**

> "Quatro modelos, quatro OKs — e repara na **ordem** em que o dbt executou: dimensões e fato antes do mart. Ninguém declarou essa ordem — o dbt a **deduziu dos `ref`**: o `mart_sales_by_category` referencia `fct_order_items` e `dim_products`, então roda depois. Esse é o **lineage automático** — o grafo de dependências que o `ref` constrói sozinho. E olha a arquitetura conceitual do que escrevemos: a **fato** carrega só chaves e as **métricas** — `price`, `freight_value` — no grão de um item; as **dimensões** carregam o contexto — quem, o quê, quando, onde. E o mart responde a pergunta da diretoria num `select` simples. Confere o resultado:"

**[EXECUTAR]**

```bash
python -c "import duckdb; print(duckdb.connect('../olist.duckdb').sql('select * from main.mart_sales_by_category limit 5'))"
```

> "`bed_bath_table`, `health_beauty`, `computers_accessories`… — o ranking agora em inglês, graças ao seed, pronto para o dashboard da Aula 12."

### 5. SCD2 ao vivo: o vendedor muda de cidade (10:00 – 14:30)

**[TELA]** Editor + terminal — o momento-show da aula.

> "E agora, o experimento que eu prometi desde a Aula 4. **O que acontece quando um seller muda de cidade?** Se sobrescrevermos — SCD Tipo 1 — as vendas antigas passam a mentir a cidade. A resposta certa é o **SCD Tipo 2**: cada versão vira uma linha com janela de validade. E no dbt, isso é **declarativo** — um snapshot:"

**[CÓDIGO]** Criar `snapshots/sellers_snapshot.sql`:

```sql
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

**[EXECUTAR]** Primeira foto:

```bash
dbt snapshot
python -c "import duckdb; print(duckdb.connect('../olist.duckdb').sql('select count(*) from snapshots.sellers_snapshot'))"
```

**[CHECKPOINT]**

> "**3.095 linhas** — uma por vendedor, todas com `dbt_valid_to` nulo: todas vigentes. Essa é a foto inicial. E agora… **vamos mudar a vida de um vendedor ao vivo.** Pego um `seller_id` qualquer de São Paulo e o mudo para Campinas, direto na fonte:"

**[CÓDIGO]** Simular a mudança na fonte e tirar a segunda foto:

```bash
python -c "
import duckdb
con = duckdb.connect('../olist.duckdb')
sid = con.sql(\"select seller_id from raw.sellers where seller_city='sao paulo' limit 1\").fetchone()[0]
print('seller escolhido:', sid)
con.sql(f\"update raw.sellers set seller_city='campinas' where seller_id='{sid}'\")
"
dbt snapshot
```

**[CÓDIGO]** Ver o histórico do vendedor:

```bash
python -c "
import duckdb
con = duckdb.connect('../olist.duckdb')
print(con.sql(\"\"\"
    select seller_id, seller_city, dbt_valid_from, dbt_valid_to
    from snapshots.sellers_snapshot
    where seller_id in (select seller_id from raw.sellers where seller_city='campinas')
    order by dbt_valid_from
\"\"\"))"
```

**[CHECKPOINT]**

> "Olha na tela — **o SCD Tipo 2 aconteceu diante de nós**: o mesmo `seller_id` agora tem **duas linhas**. A antiga — São Paulo — ganhou um `dbt_valid_to`: foi **fechada** com a data de hoje. E a nova — Campinas — nasceu com `dbt_valid_from` agora e `dbt_valid_to` **nulo**: é a vigente. Ninguém escreveu `MERGE`, ninguém escreveu lógica de datas — o dbt fez tudo a partir daquela declaração: `strategy='check'` nas colunas `seller_city` e `seller_state`. E o efeito analítico: uma venda de 2017 desse vendedor continua **atribuída a São Paulo, para sempre** — porque a `dim_sellers` que lê deste snapshot sabe qual versão valia em cada data. A história está protegida. Esse é um dos momentos mais bonitos da engenharia de dados — e cabe num arquivo de 10 linhas."

### 6. Colunar: por que é tão rápido (14:30 – 16:00)

**[TELA]** Slide: linha × coluna + a conta.

> "E por que tudo isso roda instantâneo? O segredo estrutural do DW moderno: **armazenamento colunar**. O banco transacional guarda **por linha** — todos os campos de um pedido juntos: ótimo para gravar um pedido. O DW guarda **por coluna** — e uma consulta `SUM(price)` lê **só a coluna price**, ignorando as outras. A nossa `fct_order_items` enriquecida chega a ~14 colunas; a análise de faturamento usa **1**: fração lida de 7%. Com compressão colunar de fator 4, o volume efetivamente lido cai para **menos de 2% dos bytes** da tabela. Somar os 13 milhões de reais em itens do Olist tocando 2% dos dados — essa é a mágica do colunar, e é a mesma do Parquet que reencontramos na próxima aula."

### 7. Commit + atividade + gancho (16:00 – 18:00)

**[CÓDIGO]**

```bash
cd ..
git add dbt_olist
git commit -m "feat(dw): camadas core+marts com estrela do Olist e SCD2 via dbt snapshot"
git push
```

> "Sua missão: completar a estrela criando a `dim_products` com a tradução do seed; criar o `mart_sales_by_category`; rodar `dbt run --select marts.core+` e observar a ordem do lineage; refazer o experimento do SCD2 com **outro** vendedor; e apontar **uma outra dimensão** do Olist que mereceria SCD2 — com justificativa."

> "E na próxima aula: nem tudo cabe na estrela. O texto livre dos reviews, os CSVs crus auditáveis, o desejo de 'ver o Olist como estava mês passado'… é o mundo do **Data Lake** — e da sua armadilha, o *data swamp*. Vamos organizar o nosso `data/` na arquitetura **Medallion** — bronze, silver, gold — e exportar o gold **particionado por ano e mês**, medindo ao vivo a poda de partições. O lakehouse local do Olist, de graça. Te espero na Aula 10. Um abraço!"

---

## Roteiro da Videoaula 10 — "Data Lake e Lakehouse: a Medallion do Olist com Parquet particionado"

**Duração-alvo:** 16 a 18 minutos.

### 1. Abertura (0:00 – 1:15)

**[TELA]** Slide de capa.

> "Olá! Bem-vindo, bem-vinda de volta. Na Aula 9, montamos o DW do Olist — perfeito para o que é tabular e limpo. Mas confessa comigo três desejos que a estrela não atende: guardar o **texto livre** dos reviews, que não cabe bem no relacional; manter os **CSVs crus** de forma auditável, como chegaram; e poder **ver o Olist como estava mês passado**. Para essa variedade e esse versionamento existe o **Data Lake** — e a sua armadilha famosa, o **data swamp**, o pântano de dados. Hoje organizamos o storage do Olist na arquitetura **Medallion** — bronze, silver e gold em Parquet — exportamos o gold **particionado por ano e mês**, e medimos ao vivo o efeito da poda de partições. Ao final, você terá um **lakehouse local** rodando de graça no Codespace. Bora."

### 2. Limites do DW e o Data Lake (1:15 – 3:45)

**[TELA]** Slide: 3 limites do DW → lake → swamp.

> "Primeiro, por que o DW sozinho não basta. Três limites clássicos: o **esquema rígido** — *schema-on-write*: define a estrutura antes de gravar; o texto dos reviews e payloads que mudam de forma sofrem. O **custo**: petabytes de histórico bruto em formato proprietário saem caros. E a **variedade**: texto livre, imagem, JSON não se encaixam no relacional. E o irônico: são justamente esses dados 'difíceis' — o comentário do review! — os mais valiosos para ciência de dados."

> "A resposta é o **Data Lake**: armazenar dados **em formato bruto e nativo**, sem esquema prévio — *schema-on-read*, a estrutura aplicada só na leitura, lembra da Aula 2? Tipicamente sobre object storage barato — S3, GCS, Azure. E no nosso projeto local? O 'object storage' é simplesmente… a pasta `data/`. Mas atenção ao perigo que dá nome ao slide: sem governança, catálogo e qualidade, o lago vira **data swamp** — arquivos sem dono, sem documentação, sem confiança. Se largássemos os 9 CSVs soltos, com cópias e versões espalhadas, em seis meses ninguém saberia qual `order_items` é o oficial. A flexibilidade do lake **exige** a disciplina que vem a seguir."

### 3. Delta, Iceberg, Hudi e o conceito de Lakehouse (3:45 – 6:15)

**[TELA]** Slide: tabela dos 3 formatos + definição de lakehouse.

> "O problema histórico do lake era a falta de **ACID** — escrever num lago de Parquet podia deixar leituras inconsistentes no meio de uma atualização. A solução moderna: os **formatos de tabela abertos**, que colocam uma camada de **metadados transacional** sobre os arquivos. Três nomes: **Delta Lake**, da Databricks — ACID, time travel, MERGE, forte no mundo Spark; **Apache Iceberg**, do Netflix — evolução de esquema e partição, neutro de engine; **Apache Hudi**, do Uber — upserts e CDC. Para o Olist, o ganho concreto seria o **time travel**: consultar 'a tabela de pedidos **como estava** no fechamento de janeiro de 2018' — auditoria sem cópias manuais. Nosso lake local em Parquet puro não tem isso nativo; Delta ou Iceberg adicionariam a máquina do tempo."

> "E a síntese dos dois mundos tem nome de marketing e substância real: o **Lakehouse** — a flexibilidade e o custo do lake, com a confiabilidade e o desempenho do warehouse. E aqui a boa notícia do dia: **o nosso projeto já é um lakehouse**. O DuckDB lendo Parquet é exatamente isso — um motor SQL analítico rodando **direto sobre os arquivos do lake**, sem carregar nada para um DW separado. A mesma cópia única servindo BI, SQL ad hoc e, na Aula 16, o treino de ML."

### 4. Mão na massa: a Medallion do Olist (6:15 – 9:00)

**[TELA]** Slide rápido: bronze ↔ raw, silver ↔ staging, gold ↔ marts; depois, terminal.

> "E como organizar o lake para nunca virar pântano? Com a arquitetura **Medallion**: três camadas de qualidade crescente. **Bronze**: o cru fiel à fonte — os nossos CSVs convertidos em Parquet, feitos lá na Aula 2. **Silver**: o limpo e tipado — o staging materializado. **Gold**: o pronto para consumo — os marts. O dado **flui de bronze a gold, ganhando qualidade e perdendo volume** — e repara no espelhamento perfeito com o dbt: bronze é o raw, silver é o staging, gold são os marts. Duas linguagens, uma arquitetura. Vamos materializar o que falta:"

**[CÓDIGO]** Silver — exportar o staging materializado:

```bash
python -c "
import duckdb, os
os.makedirs('data/silver', exist_ok=True)
con = duckdb.connect('olist.duckdb')
con.sql(\"\"\"COPY (SELECT * FROM main.stg_order_items)
           TO 'data/silver/order_items.parquet' (FORMAT PARQUET)\"\"\")
print('silver ok')"
```

**[CÓDIGO]** Gold — exportar a fato **particionada por ano e mês**:

```bash
python -c "
import duckdb
con = duckdb.connect('olist.duckdb')
con.sql(\"\"\"
COPY (
  SELECT *,
         year(date_key)  AS year,
         month(date_key) AS month
  FROM   main.fct_order_items
) TO 'data/gold/order_items'
  (FORMAT PARQUET, PARTITION_BY (year, month), OVERWRITE_OR_IGNORE)
\"\"\")
print('gold particionado ok')"
```

**[EXECUTAR]** Ver a estrutura que nasceu:

```bash
ls data/gold/order_items/
ls data/gold/order_items/year=2018/
```

**[CHECKPOINT]**

> "Olha a árvore de pastas: `year=2016`, `year=2017`, `year=2018` — e dentro de cada uma, `month=1`, `month=2`… O `PARTITION_BY` do DuckDB criou o **particionamento hive**: os dados fisicamente organizados por ano e mês no disco. Cada pasta é um pedaço independente do dataset. E é essa organização física que compra o desempenho que vamos medir agora."

### 5. Partition pruning ao vivo (9:00 – 12:00)

**[CÓDIGO]** A consulta que poda partições:

```bash
python -c "
import duckdb
con = duckdb.connect()
print(con.sql(\"\"\"
    SELECT count(*) AS pedidos_jan_2018
    FROM read_parquet('data/gold/order_items/**/*.parquet', hive_partitioning = true)
    WHERE year = 2018 AND month = 1
\"\"\"))
print(con.sql(\"\"\"
    SELECT count(*) AS total
    FROM read_parquet('data/gold/order_items/**/*.parquet', hive_partitioning = true)
\"\"\"))"
```

**[CHECKPOINT]**

> "Duas contagens: janeiro de 2018, alguns milhares de itens; e o total, 112 mil. E aqui está o conceito de **partition pruning**: com `hive_partitioning = true`, o DuckDB olha o filtro `WHERE year = 2018 AND month = 1` e **nem abre** os arquivos das outras pastas — ele poda as partições pela estrutura de diretórios, antes de ler um único byte de dado. A conta: o Olist tem ~25 meses; ler um mês toca cerca de **1/25 dos dados — 4%**. A mesma consulta sem particionamento varreria os 99 mil pedidos inteiros para depois filtrar. **Vinte e cinco vezes menos dados lidos**, só pela organização física em pastas."

> "E o custo desse lakehouse local — bronze, silver, gold, particionado, com poda? **Zero reais**. DuckDB mais Parquet mais uma convenção de pastas. Guarda essa conclusão, porque na próxima aula ela vira dinheiro grande: **na nuvem, esse mesmo pruning é literalmente a diferença entre uma consulta de centavos e uma de dezenas de dólares** — porque lá se paga por byte lido."

### 6. Commit + atividade + gancho (12:00 – 14:30)

**[CÓDIGO]**

```bash
git add ingestion/ && git status
git commit -am "feat(lakehouse): medallion do Olist - silver e gold particionado por ano/mes"
git push
```

> "Sua missão: materializar a silver do `stg_order_items`; exportar o gold particionado e explorar a árvore de pastas; rodar a contagem de um mês com `hive_partitioning` e comparar com o total; e responder em duas linhas: **como o Delta Lake daria time travel** a essa tabela gold, e que pergunta de auditoria do Olist isso responderia?"

> "E na próxima aula, a pergunta inevitável: e quando o Olist crescer mil vezes e não couber mais no laptop? A resposta da indústria: os **Data Warehouses na nuvem** — BigQuery, Snowflake, Redshift — e um convidado veloz, o **ClickHouse**. E a melhor notícia da disciplina inteira: o nosso projeto dbt migra para qualquer um deles **trocando um único arquivo** — e eu vou provar isso na tela, **sem precisar de conta em nuvem nenhuma**. De quebra, mostro como uma mesma consulta pode custar 12 dólares e 50… ou 5 centavos. Te espero na Aula 11. Um abraço!"

---

## Roteiro da Videoaula 11 — "DW na nuvem: o mesmo dbt no BigQuery — e a conta do FinOps"

**Duração-alvo:** 17 a 19 minutos.

### 1. Abertura (0:00 – 1:15)

**[TELA]** Slide de capa.

> "Olá! Bem-vindo, bem-vinda de volta. Até aqui, o pipeline do Olist roda **100% local e grátis**: DuckDB, dbt, Parquet. Para os 120 megabytes do Olist, é perfeito — e essa foi uma escolha pedagógica deliberada. Mas e quando o marketplace virar '**Olist vezes mil**' — terabytes, dezenas de analistas simultâneos — e não couber mais no laptop? A resposta da indústria são os **Data Warehouses na nuvem**: BigQuery, Snowflake, Redshift. E hoje eu cumpro a promessa que venho fazendo desde a Aula 1: vou provar, na tela, que **o nosso projeto dbt inteiro migra para a nuvem trocando um único arquivo** — e mostrar por que a mesma consulta pode custar 12 dólares e meio… ou 5 centavos. Bora."

### 2. Separação storage/compute + os três grandes (1:15 – 4:15)

**[TELA]** Slide: storage ⊥ compute + tabela BigQuery × Snowflake × Redshift.

> "A ideia que fundou o DW em nuvem: **separar armazenamento de computação**. No DW tradicional, os dois eram acoplados — escalar consulta exigia comprar disco junto. A nuvem desacoplou: os **dados** ficam em object storage barato e elástico — o mesmo conceito do nosso Parquet, só que gerenciado —; a **computação** é acionada sob demanda para cada consulta. Consequências: múltiplos motores lendo os mesmos dados sem conflito — o BI e o ML não brigam; escala para a consulta pesada e desliga depois; e paga-se storage e compute **separadamente**. E repara: o nosso DuckDB lendo Parquet **já antecipa exatamente essa arquitetura** — motor de um lado, arquivos do outro. A nuvem só industrializa."

> "Os três grandes, em um fôlego cada. **BigQuery**, do Google: *serverless* puro — não existe cluster para gerenciar; você manda o SQL, ele executa; cobra por **terabyte varrido**. **Snowflake**: os *virtual warehouses* — clusters lógicos que você liga e desliga por segundo, multi-cloud, forte em compartilhamento de dados. **Redshift**, da AWS: clusters provisionados ou serverless, integração total com o ecossistema Amazon. Filosofias diferentes — e um ponto em comum que é a tese da aula: **nenhum dos três exige reescrever nossos modelos dbt**."

### 3. A prova: trocando o profile ao vivo (4:15 – 7:30)

**[TELA]** Editor — `profiles.yml`.

> "Hora da prova. O nosso `profiles.yml` hoje diz: tipo **duckdb**, caminho `olist.duckdb`. Para migrar para o BigQuery, eu **adiciono um target** — sem apagar o local:"

**[CÓDIGO]** Editar `dbt_olist/profiles.yml` — acrescentar o target `prod`:

```yaml
dbt_olist:
  target: dev
  outputs:
    dev:
      type: duckdb
      path: ../olist.duckdb
      schema: main
      threads: 4
    prod:
      type: bigquery
      method: service-account
      project: olist-analytics
      dataset: marts
      keyfile: ~/.gcp/olist-sa.json
      location: US
      threads: 4
```

**[EXECUTAR]** Provar que os modelos não mudam:

```bash
cd dbt_olist
dbt compile --target dev | tail -5
dbt parse 2>&1 | tail -3
```

**[CHECKPOINT]**

> "Compilou e parseou **sem tocar em um único modelo**. Olha o que acabou de acontecer conceitualmente: `stg_orders`, `dim_customers`, `fct_order_items`, os marts — **nenhum mudou uma linha**. A migração inteira mora nesse bloco de YAML: tipo, projeto, dataset, credencial. Com uma conta real do Google Cloud e uma service account, `dbt run --target prod` materializaria a mesma estrela no BigQuery. Essa é a frase-mantra do curso, agora demonstrada: **o que roda local com DuckDB e dbt migra para a nuvem trocando o profile — os conceitos são os mesmos.** É também por isso que essa disciplina te ensinou no laptop sem medo: você estava aprendendo BigQuery o tempo todo."

### 4. Partição e clustering no modelo (7:30 – 9:45)

**[CÓDIGO]** Adicionar o config de nuvem ao `fct_order_items.sql`:

```sql
{{ config(
    materialized='table',
    partition_by={'field': 'date_key', 'data_type': 'date'},
    cluster_by=['product_id']
) }}
```

**[EXECUTAR]**

```bash
dbt compile --target dev | tail -3
```

> "Adicionei ao `config` do modelo duas chaves que o **adapter do BigQuery** entende: `partition_by` pela data da compra e `cluster_by`. No target local, o DuckDB simplesmente as ignora — compila normal, como você viu. Na nuvem, elas ativam as duas armas do custo: o **particionamento** — um `WHERE date_key = '2018-01-15'` lê **só aquela partição**; exatamente o mesmo pruning que medimos ao vivo na aula passada com as pastas do Parquet, agora gerenciado —; e o **clustering** — ordena os dados dentro da partição pela coluna mais filtrada, e o motor **pula blocos** que não contêm o valor buscado. Partição poda pastas; clustering poda blocos. E a dupla derruba a conta — vamos ver quanto."

### 5. A conta do FinOps: US$ 12,50 ou US$ 0,05 (9:45 – 12:30)

**[TELA]** Slide com a conta completa.

> "No modo *on-demand* do BigQuery, paga-se por **byte lido** — referência: **6,25 dólares por terabyte**. O Olist real lê megabytes — custo zero vírgula nada. Então vamos projetar o **Olist × 1000**: 100 milhões de itens, uma `fct_order_items` de uns **2 terabytes**, 25 meses. Um analista quer **um mês**, poucas colunas."

> "**Consulta ingênua** — sem partição, `SELECT *`: varre os 2 TB inteiros. 2 vezes 6,25: **12 dólares e 50 por consulta**. **Consulta bem modelada** — partição de um mês entre 25, e 10% das colunas, porque colunar: 2 TB vezes 1/25 vezes 0,10 vezes 6,25… **5 centavos**. A mesma pergunta, a mesma resposta: **250 vezes mais barato**. E agora escala o time: 20 analistas, 30 consultas por dia, 22 dias úteis. Versão ingênua: **165 mil dólares por mês**. Versão particionada: **660 dólares**. É a diferença entre um projeto de dados inviável e um trivial — **sem trocar uma linha de lógica**. FinOps não é planilha do financeiro: é modelagem. É trabalho **nosso**."

### 6. Bônus: medindo o pruning localmente — e o mundo além dos três grandes (12:30 – 15:00)

**[TELA]** Slide rápido do ClickHouse; depois, terminal.

> "E os três grandes não são as únicas opções. Deixa eu te apresentar, conceitualmente, o **ClickHouse**: um banco **colunar open source** famoso por uma coisa — **velocidade absurda** em OLAP: agregações sobre bilhões de linhas em frações de segundo. O coração dele é o motor **MergeTree**, em que um `ORDER BY (categoria, data)` na criação da tabela faz, de uma vez, o papel de **partição e clustering** — a ordenação física dos dados é a otimização. Fica o registro: existe serviço gerenciado com trial, mas — fiel à regra desta disciplina — **nada aqui exige conta externa**; quem quiser explorar depois, por conta própria, encontra o link nos materiais."

> "E em vez de nuvem, vamos **medir o mecanismo em casa** — porque o pruning que vale dinheiro no BigQuery é exatamente o que já temos no nosso lakehouse da Aula 10. Cronômetro na mão:"

**[CÓDIGO]** O experimento local de poda (varre tudo × poda 1 mês):

```bash
python - <<'EOF'
import duckdb, time
con = duckdb.connect()
consultas = [
  ("varre TUDO      ", "SELECT SUM(price) FROM read_parquet("
     "'data/gold/order_items/**/*.parquet', hive_partitioning=true)"),
  ("poda 1 mes      ", "SELECT SUM(price) FROM read_parquet("
     "'data/gold/order_items/**/*.parquet', hive_partitioning=true) "
     "WHERE year=2018 AND month=1"),
]
for nome, q in consultas:
    t0 = time.time(); con.sql(q).fetchall()
    print(f"{nome}: {time.time()-t0:.3f} s")
EOF
```

**[CHECKPOINT]**

> "Olha os dois tempos na tela: a consulta que **poda** um mês roda visivelmente mais rápido que a que varre os 25 — porque leu ~25 vezes menos arquivos. No laptop, essa diferença são milissegundos e ninguém paga a conta. **Na nuvem, esse mesmo delta é a fatura**: cada byte que a poda evita ler é dinheiro que não sai. A lição que unifica a aula: **pruning colunar e separação storage-compute não são exclusividade dos três grandes — são o padrão de todo warehouse analítico moderno**, incluindo o DuckDB que roda de graça na sua máquina. Aprendeu num, sabe todos."

### 7. Commit + atividade + gancho (15:00 – 17:00)

**[CÓDIGO]**

```bash
cd ..
git add dbt_olist
git commit -m "feat(cloud): target prod bigquery no profile + partition/cluster no fct"
git push
```

> "Sua missão: adicionar o target `prod` fictício ao seu profile e provar com `dbt parse` que nada quebra; adicionar o `config` de partição e clustering ao `fct_order_items`; rodar o **experimento local de poda** e anotar os dois tempos; e calcular, com a fórmula dos 6,25 dólares por TB, o custo de varrer 1 mês de uma fato de **5 TB** particionada por mês."

> "E na próxima aula, fechamos a unidade juntando **todas** as peças num ecossistema com nome: a **Modern Data Stack**. Vamos gerar a **documentação e o lineage** do projeto com um comando — o mapa navegável de tudo o que construímos — e criar o **primeiro dashboard do Olist**: um HTML interativo gerado em Python, direto dos nossos marts, **sem nenhuma ferramenta externa**. E ainda: data mesh e a conta do TCO. Te espero na Aula 12. Um abraço!"

---

## Roteiro da Videoaula 12 — "Modern Data Stack: docs, lineage e o dashboard do Olist (100% offline)"

**Duração-alvo:** 17 a 19 minutos.

### 1. Abertura (0:00 – 1:15)

**[TELA]** Slide de capa.

> "Olá! Bem-vindo, bem-vinda à aula que fecha a Unidade 3. Nas últimas três aulas construímos as peças: o DW em camadas, o lakehouse Medallion, a ponte para a nuvem. Hoje a pergunta é outra: como tudo isso vira um **ecossistema coerente** que uma empresa de verdade opera no dia a dia? A resposta tem nome e sobrenome: **Modern Data Stack**. E a aula é generosa em demonstração: vamos gerar a **documentação e o lineage** do projeto com um comando, e criar o **primeiro dashboard do Olist** — vendas por categoria, direto dos nossos marts, num HTML interativo gerado em Python, fiel à regra do curso: **sem conta, sem serviço externo**. Fecha com data mesh e a conta de quanto tudo isso custaria em produção. Bora."

### 2. A MDS — e a revelação: você já construiu uma (1:15 – 3:30)

**[TELA]** Slide: as 5 camadas da MDS mapeadas no projeto.

> "A **Modern Data Stack** é uma filosofia de arquitetura: ferramentas **modulares e plugáveis**, centradas no warehouse ou lakehouse, conectadas por padrões abertos — você compõe a melhor de cada categoria, e o fio condutor é o **ELT**. E aqui a revelação que dá gosto de dizer: **você já construiu uma MDS inteira nesta disciplina**. Confere o mapa: **ingestão** — o nosso `load_raw.py`; **armazenamento** — o DuckDB, e vimos ontem que poderia ser BigQuery; **transformação** — o dbt com staging, core e marts; **BI** — que entra hoje, com um dashboard gerado em Python; em produção, esse papel seria de um Metabase, Power BI ou Looker; **orquestração** — o Airflow com o `olist_pipeline`. Cinco camadas, cinco módulos, todos plugáveis. A stack de uma startup de dados séria — rodando no seu Codespace de graça."

> "Só um módulo tem versão 'industrializada' que ainda não citei: a **ingestão gerenciada**. Escrever conector para cada fonte é repetitivo — e ferramentas como **Fivetran** — SaaS, centenas de conectores prontos, cobra por linha ativa — e **Airbyte** — open source, customizável — resolvem isso. Se o Olist fosse um Postgres ao vivo, um conector Airbyte substituiria o nosso script: o 'L' do ELT sem escrever código de extração. No nosso caso, com 9 CSVs estáticos, o script honesto ganha."

### 3. Mão na massa: docs e lineage com um comando (3:30 – 7:00)

**[TELA]** Terminal → navegador.

> "E agora, um dos comandos de melhor custo-benefício de toda a stack:"

**[CÓDIGO]**

```bash
cd dbt_olist
dbt docs generate
dbt docs serve --port 8081
```

**[CHECKPOINT]** (Codespaces oferece abrir a porta 8081 no navegador)

> "O Codespaces detectou a porta e abriu o site — e olha o que o dbt gerou **sozinho, a partir do código que já tínhamos**: um **catálogo navegável** de todos os modelos — cada `stg_`, cada `dim_`, cada `fct_`, cada mart, com colunas e tipos. E agora o botão mais importante, aqui embaixo à direita — o **lineage graph**: clico… e aqui está o **mapa do nosso pipeline inteiro**: os sources `olist_raw` à esquerda, fluindo para os staging, os staging para a estrela, a estrela para os marts. Clico em `mart_sales_by_category` e peço os ancestrais: `fct_order_items`, `dim_products`, o seed da tradução, lá atrás até o CSV. **Toda essa genealogia veio dos `ref` que escrevemos** — nenhum diagrama foi desenhado à mão, e ele **nunca fica desatualizado**, porque nasce do código."

> "E isso tem um nome no mercado: **linhagem de dados** — a resposta para as duas perguntas mais caras de um time de dados: 'de onde vem esse número?' e 'se eu mudar essa tabela, o que quebra?'. Guarda essa tela: na Unidade 4, a LGPD vai transformá-la de conveniência em **obrigação legal**."

### 4. Mão na massa: o dashboard do Olist em Python (7:00 – 11:30)

**[TELA]** Editor + terminal → navegador (porta 8082).

> "E agora, a camada que a diretoria vê: o **BI**. Em produção, esse papel é de um Metabase, Power BI ou Looker apontado para o warehouse. Aqui, fiéis à regra do curso — nada de conta, nada de serviço externo — vamos construir o dashboard com o que já dominamos: **Python lendo os marts do DuckDB e gerando um HTML interativo** com a biblioteca plotly. E repara que o conceito é rigorosamente o mesmo do BI industrial: o gráfico **consome o mart**, nunca o dado cru."

**[CÓDIGO]** Criar `bi/dashboard_olist.py`:

```python
import duckdb
import plotly.express as px

con = duckdb.connect("olist.duckdb")

vendas = con.sql("select * from main.mart_sales_by_category limit 12").df()
fig1 = px.bar(vendas, x="categoria", y="faturamento",
              title="Olist — Faturamento por categoria (gold)")

ufs = con.sql("""
    select c.customer_state as uf, count(*) as pedidos
    from raw.orders o join raw.customers c using (customer_id)
    group by 1 order by 2 desc limit 10
""").df()
fig2 = px.bar(ufs, x="uf", y="pedidos", title="Olist — Pedidos por UF")

with open("bi/dashboard_olist.html", "w") as f:
    f.write("<h1>Dashboard Olist</h1>")
    f.write(fig1.to_html(full_html=False, include_plotlyjs="inline"))
    f.write(fig2.to_html(full_html=False, include_plotlyjs=False))

print("dashboard gerado: bi/dashboard_olist.html")
con.close()
```

**[EXECUTAR]**

```bash
cd .. && mkdir -p bi
pip install plotly
python bi/dashboard_olist.py
python -m http.server 8082 --directory bi
```

**[CHECKPOINT]** (o Codespaces oferece abrir a porta 8082 no navegador)

> "Abro a porta 8082… e aqui está: **o primeiro dashboard do Olist** — duas visualizações **interativas**: passa o mouse e o valor aparece, dá zoom, esconde série. No topo, o faturamento por categoria — cama, mesa e banho, beleza e saúde, relógios — o ranking que calculamos por SQL na Aula 3, agora em barras que uma diretoria entende em três segundos. Embaixo, os pedidos por UF com SP na liderança. E repara no caminho completo do dado que cada barra representa: **CSV gerado → bronze Parquet → schema raw → staging dbt → estrela → mart → dashboard**. Cada aula da disciplina está dentro desse gráfico."

> "E uma nota conceitual importante: o mart é a nossa **camada semântica** embrionária — o 'faturamento' foi definido **uma vez**, no SQL do `mart_sales_by_category`, e todo consumidor lê a mesma definição. É assim que se evita o clássico 'dois relatórios, dois faturamentos diferentes'. Quando você plugar um Metabase ou Power BI na vida real, o princípio é idêntico: **o BI aponta para o mart — a definição mora no dbt**."

### 5. Data mesh: quando o time central vira gargalo (11:30 – 13:30)

**[TELA]** Slide: os 4 princípios sobre os domínios do Olist.

> "Uma pausa conceitual para a pergunta organizacional: e quando a empresa cresce e o time central de dados vira **gargalo** — todo mundo esperando na fila do mesmo squad? A resposta em alta é o **data mesh**, de Zhamak Dehghani: descentralizar a responsabilidade. Quatro princípios, ancorados no Olist: **propriedade por domínio** — o time de Vendas é dono do `mart_sales_by_category`; Logística, do `mart_delivery_performance`; Reviews, dos dados de avaliação. **Dados como produto** — cada mart com dono, SLA, documentação — a do dbt docs! — e qualidade. **Plataforma self-service** — o mesmo `dbt_olist` e o DuckDB servindo todos os domínios. E **governança federada** — padrões globais, como a nossa nomenclatura `stg_/dim_/fct_/mart_`, aplicados automaticamente. E a dose de realismo: data mesh é **mudança organizacional**, não ferramenta — para o porte do Olist, a stack centralizada basta. Mas o vocabulário de 'dado como produto' já melhora qualquer decisão."

### 6. A conta do TCO + commit (13:30 – 15:30)

**[TELA]** Slide: tabela de TCO.

> "E quanto custaria o 'Olist em produção' na nuvem? A conta de TCO — custo total de propriedade — por mês: Airbyte Cloud para ingestão, uns 1.500 reais; BigQuery com storage e compute, 2.500; dbt Cloud para dois desenvolvedores, 1.000; Metabase self-hosted, 500. Total: **5.500 reais por mês**. E a nossa stack local — DuckDB, dbt-core, Airflow e o dashboard em Python? **Zero reais** de ferramentas. Para os 120 megabytes do Olist, ela entrega **o mesmo resultado de graça**. A lição de arquiteto que fecha a unidade: **comece local e barato; suba para a nuvem quando o volume e a concorrência de usuários justificarem** — e não antes, por moda."

**[CÓDIGO]**

```bash
git add -A
git commit -m "feat(mds): dbt docs + lineage e dashboard HTML do Olist (plotly + DuckDB)"
git push
```

### 7. Atividade + encerramento da unidade e gancho (15:30 – 17:30)

**[TELA]** Enunciado + teaser da U4.

> "Sua missão: gerar o `dbt docs` e **navegar o lineage** do `mart_sales_by_category` até os CSVs de origem; rodar o `dashboard_olist.py` e **adicionar um terceiro gráfico** — sugestão: a distribuição das notas de review, 1 a 5; listar os **três domínios** do Olist e o data product de cada um; e comparar o TCO local contra a nuvem, respondendo: **a partir de que volume você migraria?**"

> "E fechamos a Unidade 3 com o pipeline do Olist **arquitetado de ponta a ponta**: a estrela no DW, a Medallion no lake, a ponte para a nuvem num arquivo YAML, e a MDS completa com docs, lineage e dashboard. Mas repara numa coisa: o pipeline **funciona** — e ainda não provamos que se pode **confiar** nele. É exatamente o tema da Unidade 4, a última: **testes de qualidade** no dbt e Great Expectations; **governança e LGPD** sobre os dados pseudonimizados do Olist; **DataOps** com CI/CD no GitHub Actions rodando a cada pull request — no mesmo GitHub onde nosso projeto já mora; e o gran finale: um **modelo de machine learning** lendo o nosso gold para prever atraso de entrega. Te espero na Unidade 4. Um abraço!"
