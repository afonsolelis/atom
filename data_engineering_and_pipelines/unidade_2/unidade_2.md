# Unidade 2 — Ingestão e Processamento de Dados

- **Disciplina:** Data Engineering and Pipelines
- **Conteudista:** Afonso Cesar Lelis Brandão
- **Videoaulas desta unidade:** 5 a 8

> **Recap da Unidade 1:** na Unidade 1 conhecemos o projeto que nos acompanha o curso inteiro — o **pipeline de dados do Olist** (marketplace brasileiro, ~99 mil pedidos reais de 2016 a 2018, 9 arquivos CSV) — e fizemos o trabalho de fundação: mapeamos o ciclo de vida sobre o Olist, carregamos os CSVs no schema `raw` do **DuckDB** e **modelamos a estrela**: o fato `fct_order_items` (grão = 1 item de pedido, métricas `price` e `freight_value`) cercado por `dim_customers`, `dim_products`, `dim_sellers` e `dim_dates`. Tínhamos o desenho — agora vamos colocar o dado **em movimento**. Nesta unidade você **implementa a ingestão** do Olist com dbt (Aula 5), **processa em lote** o join+agregação pesado com a lente do Spark e a execução real em DuckDB (Aula 6), **simula um stream** dos pedidos do Olist (Aula 7) e **orquestra** o pipeline inteiro num DAG do **Apache Airflow** (Aula 8). Saímos da unidade com o pipeline `olist_pipeline` rodando ponta a ponta.

---

## Aula 5 — ETL vs ELT: a ingestão de dados

Na Unidade 1 desenhamos a estrela do Olist no papel e despejamos os 9 CSVs no schema `raw` do DuckDB com um `read_csv_auto` bruto. Funciona uma vez — mas não é um pipeline: não renomeia colunas, não casta tipos, não trata nulos e, pior, recarrega os ~99 mil pedidos toda vez. Nesta aula transformamos aquele carregamento manual numa **ingestão de verdade**, criando o projeto **`dbt_olist/`** no padrão **ELT**. Você vai entender as duas filosofias de movimentação de dados (**ETL** e **ELT**), a diferença entre carregar tudo (**full**) e só o que mudou (**incremental/CDC**), e por que a palavra **idempotência** vai te salvar muitas madrugadas — tudo enquanto constrói os modelos `stg_*` do Olist.

### O que é ingestão de dados

**Ingestão** é o ato de mover dados de uma ou mais **fontes** (sistemas operacionais, APIs, arquivos, bancos transacionais, filas) para um **destino** onde serão armazenados e processados. No nosso projeto, a fonte são os 9 CSVs do Olist (`olist_orders_dataset`, `olist_order_items_dataset`, `olist_order_payments_dataset`, etc.) e o destino é o DuckDB local (`olist.duckdb`). É a primeira fronteira do pipeline — e, portanto, o ponto onde a qualidade dos dados é mais frágil.

A ingestão pode ser **push** (a fonte empurra, como um webhook) ou **pull** (o pipeline busca, como nossa leitura agendada dos CSVs). Pode ser **batch** (lotes periódicos — é o caso do Olist) ou **streaming** (registro a registro — veremos na Aula 7). E carrega decisões de schema: validamos na entrada (*schema-on-write*) ou só na leitura (*schema-on-read*)?

![Logo do Apache Airflow, ferramenta de orquestração frequentemente usada para coordenar tarefas de ingestão de dados](https://commons.wikimedia.org/wiki/Special:FilePath/AirflowLogo.png)

### ETL clássico

**ETL** significa **Extract, Transform, Load** — extrair, transformar e **só então** carregar. A transformação acontece num servidor intermediário (historicamente Informatica, Talend ou Pentaho) **antes** de o dado tocar o destino. Aplicado ao Olist, seria: ler os CSVs, limpar e agregar fora do DuckDB, e gravar só o resultado refinado.

A lógica do ETL nasceu quando armazenamento e processamento eram caros. Vantagem: o dado entra já limpo e conforme regras de governança. Desvantagem: a transformação vira gargalo, exige infraestrutura própria e, se você descobre depois que precisava de uma coluna que descartou (digamos, o `seller_id` que jogou fora), tem de reextrair da fonte.

### ELT moderno

**ELT** inverte a ordem: **Extract, Load, Transform** — extrai, **carrega o dado bruto** no destino e transforma *lá dentro*, usando o poder do warehouse moderno (BigQuery, Snowflake) ou, no nosso caso, do **DuckDB** orquestrado pelo **dbt**. É exatamente o que faremos: os CSVs entram crus no schema `raw`, e o dbt os transforma em SQL declarativo.

O ELT venceu porque armazenamento ficou barato e os motores ficaram absurdamente paralelos. Carregar o bruto primeiro significa que você **guarda a fonte da verdade** e pode re-transformar quantas vezes quiser sem reextrair — guardar os 120 MB crus do Olist custa praticamente nada. É a mensagem que repetiremos o curso inteiro: *o que roda local com DuckDB+dbt migra para a nuvem trocando só o profile do dbt; os conceitos são os mesmos*.

| Aspecto | ETL | ELT (nosso projeto) |
| --- | --- | --- |
| **Onde transforma** | Servidor intermediário | Dentro do DuckDB (via dbt) |
| **O que chega ao destino** | Dado já refinado | CSV cru no schema `raw` + modelos |
| **Reprocessar** | Reextrai da fonte | Re-roda `dbt run` |
| **Melhor para** | Dados sensíveis, regras na entrada | Nuvem, grande volume, flexibilidade |

### O projeto dbt do Olist: sources e staging

Criar o projeto é `dbt init dbt_olist` com o adapter `dbt-duckdb`. O `profiles.yml` aponta o dbt para o nosso arquivo DuckDB:

```yaml
# ~/.dbt/profiles.yml
dbt_olist:
  target: dev
  outputs:
    dev:
      type: duckdb
      path: ../olist.duckdb
      schema: main
      threads: 4
```

Em seguida, declaramos as tabelas `raw` como **sources** no grupo `olist_raw` — assim o dbt conhece a origem e pode testá-la e rastrear a linhagem:

```yaml
# models/staging/_olist__sources.yml
version: 2
sources:
  - name: olist_raw
    schema: raw
    tables:
      - name: orders          # olist_orders_dataset
      - name: order_items     # olist_order_items_dataset
      - name: order_payments
      - name: order_reviews
      - name: products
      - name: customers
      - name: sellers
```

Cada fonte ganha um modelo **staging** (`stg_*`): uma camada 1:1 que **renomeia, casta tipos e limpa nulos**, sem ainda fazer joins ou agregações. É a base de tudo que vem depois.

### Carga incremental e idempotência no `stg_orders`

Independentemente de ELT, a extração tem dois modos. **Carga full:** lê a tabela inteira toda vez — simples, mas cara conforme cresce. **Carga incremental:** lê apenas o que mudou desde a última execução, usando uma coluna marcadora. No Olist, a marca natural é `order_purchase_timestamp`. Configuramos o `stg_orders` como **incremental** com `unique_key='order_id'`, o que dá **idempotência**: rodar duas vezes não duplica pedidos.

```sql
-- models/staging/stg_orders.sql
{{ config(materialized='incremental', unique_key='order_id') }}

select
    order_id,
    customer_id,
    order_status,
    cast(order_purchase_timestamp as timestamp) as purchased_at,
    cast(order_delivered_customer_date as timestamp) as delivered_at
from {{ source('olist_raw', 'orders') }}
{% if is_incremental() %}
  where order_purchase_timestamp > (select max(purchased_at) from {{ this }})
{% endif %}
```

Pipelines falham — é certeza, não possibilidade. Uma operação é **idempotente** quando executá-la dez vezes produz o mesmo estado final que executá-la uma. O dbt nos dá isso de graça com `unique_key` (faz um *MERGE*/upsert por baixo). Quando até linhas *deletadas* precisam ser capturadas, usa-se **CDC (Change Data Capture)**: ler o **log de transações** do banco-fonte (o WAL do PostgreSQL) e replicar cada `INSERT/UPDATE/DELETE`. Como o Olist é um conjunto de CSVs estáticos, o CDC fica teórico: *se o Olist fosse um Postgres ao vivo, plugaríamos o Debezium para emitir cada novo pedido como evento — exatamente a ponte para o streaming da Aula 7*.

### Exemplo numérico: incremental vs full no Olist

O Olist acumula $99\,441$ pedidos. Uma carga **full** relê todos toda execução. Com a média histórica de $\approx 135$ pedidos/dia, um dia novo traz pouquíssimas linhas. O fator de economia da carga incremental sobre a full é:

$$
\text{fator} = \frac{99\,441}{135} \approx 736
$$

Ou seja, reprocessar **um dia** do Olist (~135 pedidos) é cerca de **736 vezes** mais barato que recarregar a base inteira a cada execução. Em segundos de relógio, a uma taxa de $50\,000$ linhas/s, a diferença é $99\,441/50\,000 \approx 2{,}0\ \text{s}$ (full) contra $135/50\,000 \approx 0{,}003\ \text{s}$ (incremental). Parece pouco aqui — mas projete "Olist × 1000" (escala de um marketplace grande) e a full passaria de meia hora enquanto a incremental continua em segundos.

### Atividade prática

Use os CSVs do Olist já carregados no schema `raw` (Unidade 1).

1. Rode `dbt init dbt_olist` com o adapter `dbt-duckdb` e configure o `profiles.yml` apontando para `olist.duckdb`.
2. Declare o source `olist_raw` e escreva `stg_orders`, `stg_order_items` e `stg_customers` (renomeie e caste tipos). Rode `dbt run`.
3. Torne `stg_orders` **incremental** por `order_purchase_timestamp` com `unique_key='order_id'`. Rode `dbt run` **duas vezes** seguidas e prove com `select count(*) from stg_orders` que o total não mudou — idempotência funcionando.
4. Documente em três linhas: por que o Olist é um caso de **ELT** e não ETL?

### Pontos-chave

- **Ingestão** é a primeira e mais frágil etapa; o Olist entra cru no schema `raw` do DuckDB (ELT).
- **ETL** transforma antes de carregar; **ELT** carrega o bruto e transforma no destino com **dbt** — o padrão do nosso projeto.
- O projeto **`dbt_olist`** define o source `olist_raw` e os modelos **`stg_*`** (renomeiam, castam, limpam).
- **Carga incremental** por `order_purchase_timestamp` + **`unique_key='order_id'`** dá **idempotência** — rodar duas vezes não duplica.
- **CDC** (ex.: Debezium no WAL) capturaria deletes se o Olist fosse um banco ao vivo — ponte para o streaming da Aula 7.

### Para saber mais

- **Modelos incrementais no dbt (documentação oficial):** https://docs.getdbt.com/docs/build/incremental-models
- **Sources no dbt (declarar a origem `raw`):** https://docs.getdbt.com/docs/build/sources
- **Documentação do Debezium (CDC):** https://debezium.io/documentation/

## Aula 5 — Roteiro da Videoaula 5: "ETL vs ELT: a ingestão de dados"

**Duração:** 9 a 10 minutos.

### 1. Abertura (0:00 – 0:45)

> "Na Unidade 1 a gente desenhou a estrela do Olist e jogou os 9 CSVs cru no DuckDB com um read_csv_auto. Funciona uma vez — mas não é pipeline. Hoje a gente transforma aquilo numa ingestão de verdade: cria o projeto dbt do Olist, no padrão ELT, e fala de carga incremental, CDC e a palavra que salva noites: idempotência."

### 2. Desenvolvimento — parte 1 (0:45 – 4:00)

> "Ingestão é mover dado da fonte para o destino. No nosso caso, fonte são os CSVs do Olist, destino é o olist.duckdb. E aqui surge a grande bifurcação: ETL e ELT. No ETL clássico você extrai, transforma num servidor no meio e só então carrega. No ELT moderno você inverte: extrai, carrega o dado bruto e transforma lá dentro. É o que a gente faz: os CSVs entram crus no schema raw, e o dbt transforma em SQL. O ELT ganhou porque armazenar ficou barato — guardar os 120 MB crus do Olist não custa nada — e você nunca perde a fonte da verdade. Guarde esta frase do curso: o que roda local com DuckDB e dbt migra para a nuvem trocando só o profile."

### 3. Desenvolvimento — parte 2 (4:00 – 6:50)

> "Vamos montar o projeto. dbt init dbt_olist com o adapter duckdb, o profiles.yml aponta para o nosso arquivo. Aí declaro as tabelas raw como sources, no grupo olist_raw, e crio um modelo staging para cada fonte: stg_orders, stg_order_items, stg_customers. Staging é a camada um-para-um que renomeia coluna, casta tipo, limpa nulo — sem join ainda. É a fundação de tudo que vem nas próximas unidades."

### 4. Desenvolvimento — parte 3 (6:50 – 9:00)

> "Agora, full ou incremental? Full relê os 99 mil pedidos toda vez. Incremental lê só o que mudou, olhando o order_purchase_timestamp. No stg_orders eu configuro materialized incremental com unique_key igual a order_id. Isso me dá idempotência: o dbt faz um merge por baixo, então rodar duas vezes não duplica pedido nenhum. E quando eu precisaria capturar até o que foi deletado? CDC, lendo o log de transações do banco. O Olist é CSV estático, então isso fica teórico — mas se ele fosse um Postgres ao vivo, eu plugaria o Debezium para emitir cada pedido novo como evento. Segura essa ideia, que ela volta na aula de streaming."

### 5. Encerramento (9:00 – 9:50)

> "Fiz a conta: reprocessar um dia do Olist, uns 135 pedidos, é umas 736 vezes mais barato que recarregar os 99 mil toda vez. Guarde o tripé: ELT como filosofia, incremental com unique_key como técnica, idempotência como rede de segurança. Saímos daqui com o dbt_olist de pé e os stg de pé. Na próxima aula, com o dado já dentro, a gente processa em lote o join e a agregação pesada do Olist — Apache Spark na teoria, DuckDB na prática. Te espero!"

---

## Aula 6 — Processamento em lote com Apache Spark

Na Aula 5 montamos o `dbt_olist` e os modelos `stg_*`: o dado do Olist está limpo e tipado. E agora? Para responder perguntas de negócio — *qual o faturamento por categoria e por mês?* — precisamos **juntar** `stg_orders` × `stg_order_items` × `stg_products` × `stg_order_payments` e **agregar** sobre as ~112 mil linhas de itens. Isso é **processamento em lote**, e seu nome mais importante é **Apache Spark**. Nesta aula você entende a ideia fundadora (**MapReduce**), como o Spark organiza um cluster (**driver e executors**), suas abstrações (**RDD, DataFrame, Dataset**), por que é **lazy** e qual operação custa mais caro — o **shuffle** — e roda o equivalente real no DuckDB, que resolve o Olist em segundos no laptop.

### O paradigma MapReduce

A revolução começou em 2004, quando o Google publicou o paper do **MapReduce**: em vez de levar os dados até um supercomputador, leve o **código** até onde os dados já estão, em milhares de máquinas baratas. No **map**, cada nó aplica uma função a um pedaço dos dados, emitindo pares chave-valor. No **reduce**, os pares com a mesma chave são agrupados e combinados.

Aplicado ao Olist: para faturar por categoria, o map emitiria `(product_category, price)` para cada item; o reduce somaria os preços por categoria. O Hadoop popularizou o modelo, mas gravava resultados intermediários em disco entre cada etapa — custo brutal. O Spark nasceu para resolver exatamente isso.

![Logo do Apache Spark, motor de processamento distribuído em memória para grandes volumes de dados](https://commons.wikimedia.org/wiki/Special:FilePath/Apache_Spark_logo.svg)

### Arquitetura do Spark (driver e executors)

Um job Spark roda num **cluster** com papéis bem definidos. O **driver** é o cérebro: hospeda o `SparkContext`, constrói o plano (o DAG de operações) e distribui tarefas. Os **executors** são os músculos: processos espalhados pelos nós que executam tarefas e guardam dados em memória. Um **cluster manager** (YARN, Kubernetes ou standalone) negocia recursos.

O trabalho é fatiado em **tasks** (uma por partição), agrupadas em **stages**, num **job**. O salto do Spark sobre o Hadoop é manter intermediários **em memória** entre stages — ganhos de ordens de grandeza em pipelines iterativos. Para o Olist no laptop, porém, não precisamos de cluster: o **DuckDB** é um motor vetorizado *single-node* que faz o mesmo join+agregação em segundos.

### RDD, DataFrame e Dataset

O Spark oferece três abstrações, em ordem crescente de comodidade:

- **RDD (Resilient Distributed Dataset):** a coleção distribuída original, de baixo nível. Resiliente porque registra sua linhagem (*lineage*) e se reconstrói após falha. Poderoso, mas verboso e sem otimização automática.
- **DataFrame:** dados em colunas nomeadas, como uma tabela — exatamente como pensamos o `fct_order_items`. É a abstração mais usada, pois passa pelo otimizador **Catalyst** e pelo motor **Tungsten**. API em Python (PySpark), Scala, Java e R.
- **Dataset:** DataFrame com tipagem forte em tempo de compilação (Scala/Java).

Para a maioria dos engenheiros, o **DataFrame** é o ponto de partida: legível, otimizado e portável.

### O mesmo job em PySpark e em DuckDB

Veja a agregação "faturamento por categoria" do Olist nas duas ferramentas. Primeiro o **PySpark**, lendo a camada bronze em Parquet:

```python
from pyspark.sql import SparkSession, functions as F

spark = SparkSession.builder.appName("olist_batch").getOrCreate()
items = spark.read.parquet("data/bronze/order_items.parquet")
products = spark.read.parquet("data/bronze/products.parquet")

faturamento = (
    items.join(products, "product_id")                 # wide -> shuffle
         .groupBy("product_category_name")             # wide -> shuffle
         .agg(F.sum("price").alias("receita"))
         .orderBy(F.desc("receita"))
)
faturamento.show(10)
```

E o **equivalente em DuckDB**, que rodamos de fato no projeto (e que o dbt usará como mart na Unidade 3):

```sql
SELECT p.product_category_name AS categoria,
       SUM(i.price)            AS receita
FROM   raw.order_items i
JOIN   raw.products    p USING (product_id)
GROUP  BY p.product_category_name
ORDER  BY receita DESC
LIMIT 10;
```

Mesma lógica, mesma estrela. A mensagem do curso: **DuckDB resolve o Olist em segundos no laptop; o Spark entra quando o Olist vira "Olist × 10.000"** e não cabe mais numa máquina.

### Transformações, ações e shuffle

O Spark separa **transformações** (`filter`, `select`, `groupBy`, `join`) de **ações** (`count`, `show`, `write`). Transformações são **lazy**: não executam nada — só acrescentam um nó ao plano. Só uma **ação** dispara o DAG, deixa o Catalyst otimizá-lo (reordena filtros, elimina colunas não usadas) e roda. Essa preguiça é virtude: o motor enxerga o pipeline inteiro antes de executar.

Os dados vivem repartidos em **partições**, processadas em paralelo. Operações *narrow* (`filter`, `map`) mantêm cada partição independente — rápidas. Já operações *wide* (`groupBy`, `join`, `distinct`) exigem que dados da mesma chave se encontrem na mesma partição, forçando um **shuffle**: redistribuição massiva pela rede. No nosso job, **ambos** o `join` por `product_id` e o `groupBy` por categoria são wide → dois shuffles. O **shuffle é a operação mais cara** do Spark. Otimizar é domá-lo: filtrar antes de juntar, usar *broadcast join* quando um lado é pequeno (a `dim_products` do Olist tem só ~33 mil linhas — perfeita para broadcast) e particionar pela chave de junção.

### Exemplo numérico: paralelismo e a Lei de Amdahl no Olist

O join+agregação do Olist envolve $112\,650$ itens. Suponha que processar esse lote num único core leve $T_1 = 60\ \text{s}$ (hipótese para a conta). Distribuindo em $8$ cores, o tempo *ideal* cairia para:

$$
T_8 = \frac{60}{8} = 7{,}5\ \text{s}
$$

Mas o paralelismo não é perfeito: o **shuffle** final (juntar os parciais por categoria) é serial. Suponha $20\%$ de trabalho serial. Pela **Lei de Amdahl**, o ganho máximo com $8$ cores é:

$$
S_{8} = \frac{1}{0{,}20 + \dfrac{0{,}80}{8}} = \frac{1}{0{,}20 + 0{,}10} = 3{,}33
$$

Logo o tempo real fica $\approx 60 / 3{,}33 = 18\ \text{s}$ — bem acima dos $7{,}5\ \text{s}$ ideais. A lição: adicionar cores tem retorno decrescente, e **reduzir a fração serial (o shuffle!) rende mais que comprar mais máquinas**. No Olist, na verdade, o DuckDB faz tudo isso em menos de um segundo — Amdahl só morde de verdade quando o dataset é mil vezes maior.

### Atividade prática

Você pode usar PySpark (`pip install pyspark`) ou rodar tudo direto no DuckDB.

1. Exporte `stg_order_items` e `stg_products` do Olist para Parquet (camada bronze) e carregue num **DataFrame** PySpark.
2. Encadeie `join` + `groupBy("product_category_name").agg(F.sum("price"))` e confirme que **nada roda** até `.show()`.
3. Use `.explain()` e **localize o shuffle** (`Exchange`). Quantos há no plano?
4. Reescreva o join com `broadcast(products)` (a dimensão é pequena) e compare o plano. Depois rode o **SQL DuckDB equivalente** e compare a sensação de velocidade.

### Pontos-chave

- O **MapReduce** levou o código até os dados; o **Spark** o aprimorou mantendo intermediários **em memória**.
- Arquitetura: **driver** (planeja) + **executors** (executam) + **cluster manager** (aloca).
- **DataFrame** é a abstração padrão (otimizada pelo Catalyst); o **DuckDB** faz o mesmo join+agregação do Olist em segundos, *single-node*.
- Transformações são **lazy**; só uma **ação** dispara o DAG; o **join** e o **groupBy** do Olist são operações **wide** → geram **shuffle**.
- O **shuffle** é o maior custo — *broadcast join* da `dim_products` (~33 mil linhas) e filtrar antes de juntar valem mais que somar máquinas (Amdahl).

### Para saber mais

- **Documentação oficial do Apache Spark:** https://spark.apache.org/docs/latest/
- **Guia de tuning de performance do Spark (shuffle, broadcast):** https://spark.apache.org/docs/latest/sql-performance-tuning.html
- **Consultando Parquet com DuckDB (motor vetorizado local):** https://duckdb.org/2021/06/25/querying-parquet.html

## Aula 6 — Roteiro da Videoaula 6: "Processamento em lote com Apache Spark"

**Duração:** 9 a 10 minutos.

### 1. Abertura (0:00 – 0:45)

> "Na aula passada a gente montou o dbt do Olist e os modelos staging: o dado está limpo. Mas para responder 'qual o faturamento por categoria e por mês', eu preciso juntar pedidos, itens, produtos e pagamentos e agregar sobre 112 mil linhas. Isso é processamento em lote. Hoje você conhece o Apache Spark na teoria e roda o equivalente real em DuckDB."

### 2. Desenvolvimento — parte 1 (0:45 – 3:50)

> "Tudo começa em 2004, com o paper do MapReduce, do Google. A ideia genial: em vez de levar terabytes até um supercomputador, leve o código até onde os dados já estão. Map aplica função e emite chave-valor; reduce agrupa por chave e combina. No Olist, para faturar por categoria, o map emite categoria-preço e o reduce soma. O Hadoop popularizou, mas gravava tudo em disco entre as etapas — lento. O Spark chegou e disse: e se eu mantiver os intermediários em memória? Daí o salto de performance."

### 3. Desenvolvimento — parte 2 (3:50 – 6:50)

> "Como o Spark se organiza? Driver, o cérebro que monta o plano; executors, os músculos que processam e guardam em memória; cluster manager que aloca. E você fala com ele por três abstrações: RDD, baixo nível; DataFrame, a tabela com colunas que passa pelo otimizador Catalyst — é o que você usa 90% do tempo, e é como a gente já pensa o fct_order_items; e Dataset, o tipado. Agora o ponto prático: o mesmo job de faturamento por categoria eu escrevo em PySpark com join e groupBy, ou em SQL no DuckDB com JOIN USING product_id e GROUP BY. Mesma estrela, mesma lógica. E o DuckDB resolve o Olist em segundos no laptop — o Spark entra quando o Olist vira Olist vezes dez mil."

### 4. Desenvolvimento — parte 3 (6:50 – 9:00)

> "O pulo do gato: o Spark é lazy. Filter, join, groupBy não rodam — ele só anota no plano. Só quando você chama uma ação, show ou write, ele monta o DAG, o Catalyst otimiza e roda. E cuidado com o shuffle: no nosso job, tanto o join por product_id quanto o groupBy por categoria são operações wide — obrigam dados da mesma chave a se encontrarem, redistribuindo tudo pela rede. É a operação mais cara. A dim_products do Olist tem só 33 mil linhas, então dá para fazer broadcast join e matar um dos shuffles. Otimizar Spark é, acima de tudo, domar o shuffle."

### 5. Encerramento (9:00 – 9:50)

> "E a Lei de Amdahl: se 20% do trabalho é serial, dobrar para 8 cores não dá 8 vezes mais rápido — dá só 3,3. Filtre antes de juntar, use broadcast, escolha bem as partições. No Olist o DuckDB faz isso em menos de um segundo; Amdahl só morde quando o dado é mil vezes maior. Já temos o lote. Mas e quando o pedido do Olist não pode esperar o próximo lote — quando a gente quer contá-lo no instante em que nasce? Próxima aula: a gente simula um stream dos pedidos do Olist. Te espero!"

---

## Aula 7 — Processamento em tempo real e streaming

Até agora tratamos o Olist como ele é: um **histórico** de ~99 mil pedidos parados em CSV. Mas imagine que esses pedidos estivessem chegando **agora**, um a um, no marketplace — e que precisássemos contar "pedidos por minuto" ou "faturamento da última hora" em tempo real. Há decisões que não esperam o próximo lote. Nesta aula entramos no **processamento em tempo real**: vamos **simular um stream** dos pedidos do Olist com um produtor e um consumidor Python (mock de Kafka), entendendo **tópicos, partições e offsets**, agregando o fluxo com **janelas** e escolhendo as **garantias de entrega** — e fechando com a arquitetura **Kappa**, em que stream e batch coexistem.

### Batch vs streaming

No **batch**, o dado é processado em **lotes finitos** — foi o que fizemos na Aula 6 com o join do Olist. No **streaming**, o dado é um **fluxo infinito e contínuo**: registros chegam o tempo todo e são processados quase no instante em que surgem.

A diferença não é só de velocidade, é de **modelo mental**. No batch perguntamos "qual foi o faturamento do Olist em outubro de 2017?". No streaming perguntamos "quantos pedidos estão entrando *agora*, nos últimos 60 segundos?". Streaming traz desafios próprios: o dado nunca "acaba", pode chegar **fora de ordem** (um pedido atrasado pela rede) e exige distinguir **tempo do evento** (`order_purchase_timestamp`) de **tempo de processamento** (quando chegou ao consumidor).

![Logo do Apache Kafka, plataforma distribuída de streaming de eventos](https://commons.wikimedia.org/wiki/Special:FilePath/Apache_kafka.svg)

### Mensageria e o Apache Kafka

No coração do streaming está a **mensageria**: um intermediário que **desacopla** quem produz de quem consome. O produtor não conhece o consumidor; ambos só conhecem o intermediário. Isso permite escalar os dois lados de forma independente e absorver picos.

O **Apache Kafka**, criado no LinkedIn em 2011, é o padrão de fato. Mais do que uma fila, é um **log distribuído e durável**: as mensagens não somem quando lidas — ficam gravadas por um período de retenção, e múltiplos consumidores leem o mesmo fluxo em ritmos diferentes. Um cluster Kafka tem **brokers** (servidores que armazenam) e organiza tudo em **tópicos**. No nosso projeto, o tópico será `olist.orders`.

### Tópicos, partições e offsets

Um **tópico** é uma categoria nomeada de mensagens — o nosso é `olist.orders`. Cada tópico se divide em **partições**, e é nelas que mora a escalabilidade: partições são distribuídas entre os brokers e lidas em paralelo. Dentro de uma partição, cada mensagem recebe um número sequencial imutável — o **offset**. O Kafka garante **ordem apenas dentro de uma partição**. O consumidor controla **até qual offset já leu** (o *committed offset*), o que permite reprocessar do começo, retomar após falha ou avançar. Mensagens com a mesma **chave** vão sempre para a mesma partição — se usarmos `customer_id` como chave, todos os pedidos de um cliente ficam ordenados.

### Simulando o stream do Olist (produtor e consumidor)

O Olist é histórico, então **simulamos** o stream: um produtor lê os pedidos ordenados por `order_purchase_timestamp` e os emite como eventos JSON num mock de tópico; um consumidor agrega por **janela**. O script vive em `ingestion/stream_orders.py`.

```python
# ingestion/stream_orders.py — produtor (mock do tópico olist.orders)
import duckdb, json, time

con = duckdb.connect("olist.duckdb")
pedidos = con.execute("""
    SELECT order_id, customer_id, order_purchase_timestamp
    FROM raw.orders
    ORDER BY order_purchase_timestamp
""").fetchall()

def emit(topico, evento):           # mock: aqui seria producer.send(topico, ...)
    print(f"[{topico}] {evento}")

for order_id, customer_id, ts in pedidos:
    emit("olist.orders", json.dumps({
        "order_id": order_id, "customer_id": customer_id, "ts": str(ts)
    }))
    time.sleep(0.001)               # acelera o tempo: 1 ms por pedido
```

```python
# consumidor: janela tumbling de 60 s contando pedidos
from collections import defaultdict
from datetime import datetime

contagem = defaultdict(int)

def consume(evento):
    ts = datetime.fromisoformat(json.loads(evento)["ts"])
    janela = ts.replace(second=0, microsecond=0)   # bucket de 1 minuto
    contagem[janela] += 1                           # idempotência: ver texto
```

### Janelas e garantias de entrega

Como agregar um fluxo que nunca termina? Recortando-o no tempo, com **janelas**. **Tumbling (fixa, sem sobreposição):** blocos contíguos iguais — "pedidos do Olist a cada 60 s"; cada evento cai em exatamente uma janela (é o que o consumidor acima faz). **Sliding (deslizante):** janela fixa que avança — "faturamento da última 1 h, recalculado a cada 5 min"; um evento pode pertencer a várias. Há ainda janelas de **sessão**, por inatividade. Lidar com dados atrasados pede *watermarks*.

E as **garantias de entrega**: **at-most-once** pode perder, nunca duplica (barato); **at-least-once** nunca perde, mas pode duplicar (o padrão — por isso o **consumo idempotente** da Aula 5 brilha de novo); **exactly-once** processa uma vez só, sem perda nem duplicação, mas é caro (produtores idempotentes + transações). A regra prática: **at-least-once + processamento idempotente**.

### Lambda e Kappa: como o stream coexiste com o batch

Se construíssemos o Olist em tempo real, como a camada de streaming conviveria com o batch que já temos? Duas arquiteturas respondem. A **Lambda** mantém *dois* caminhos: um batch (lento, completo, é o nosso dbt) e um speed layer (rápido, aproximado) — e reconcilia. A **Kappa** simplifica: **tudo é stream**; o histórico é apenas o log reprocessado do começo. Para o Olist, o caminho natural seria Kappa — o mesmo log `olist.orders` alimenta tanto a contagem ao vivo quanto, reprocessado, os marts. *Mensagem: a estrela continua a mesma; muda só a forma de alimentá-la.*

### Exemplo numérico: taxa de eventos e partições do Olist

O Olist tem $\approx 135$ pedidos/dia em média. Em eventos por segundo, isso é irrisório:

$$
\lambda = \frac{135}{86\,400} \approx 0{,}0016\ \text{eventos/s}
$$

Uma única partição resolve com folga absurda. Mas projete a **Black Friday** do marketplace, com um pico $1000\times$ a média, comprimido em 1 hora: seriam $\approx 135\,000$ pedidos numa hora, ou $\approx 37{,}5$ eventos/s. Se cada consumidor processa $10$ eventos/s, o número mínimo de partições é:

$$
N = \left\lceil \frac{37{,}5}{10} \right\rceil = 4\ \text{partições}
$$

Por isso o número de partições é uma das decisões de capacidade mais importantes no Kafka: define o **teto de paralelismo** do consumo.

### Pausa para reflexão (Desafio)

> Imagine que o Olist virou um marketplace **ao vivo** e você precisa de um painel "pedidos por minuto + faturamento da última hora" atualizando em tempo real, além de um **alerta** quando um mesmo `customer_id` faz 5 pedidos em 2 minutos (suspeita de fraude). Pergunte-se: que **chave** você usaria no tópico `olist.orders` para manter os pedidos de um cliente ordenados? Que tipo de **janela** detecta "5 pedidos em 2 minutos" — tumbling ou sliding? Que **garantia de entrega** você escolhe para o alerta, e por que duplicar um alerta de fraude é menos grave que **perder** um pedido? Esboce, em um parágrafo, a arquitetura (tópico, partições, janelas, garantia) e diga se ela é Lambda ou Kappa.

### Atividade prática

Você pode simular tudo em Python puro (sem instalar Kafka).

1. Rode o produtor `stream_orders.py` lendo `raw.orders` do Olist ordenado por `order_purchase_timestamp` e emitindo eventos JSON.
2. Escreva o consumidor com **janela tumbling de 60 s** contando pedidos por minuto; imprima as 10 janelas mais movimentadas do Olist.
3. Adicione uma **janela sliding** de 1 h (passo 5 min) somando `payment_value` por janela (junte com `stg_order_payments`).
4. (Opcional) Suba um Kafka local com Docker (`apache/kafka`), crie o tópico `olist.orders` com **3 partições** usando `customer_id` como chave, e inspecione os **offsets** com `kafka-consumer-groups.sh --describe`.

### Pontos-chave

- **Batch** processa lotes finitos (Aula 6); **streaming** processa um fluxo infinito quase em tempo real.
- O **Kafka** é um **log distribuído e durável** que desacopla produtor de consumidor; nosso tópico é `olist.orders`.
- Simulamos o stream do Olist com `stream_orders.py` (produtor lê `raw.orders` ordenado e emite JSON; consumidor agrega por janela).
- **Janelas** (tumbling, sliding) recortam o fluxo; **at-least-once + consumo idempotente** é a escolha prática.
- Na arquitetura **Kappa**, o mesmo log `olist.orders` alimenta a contagem ao vivo e, reprocessado, os marts — a estrela é a mesma.

### Para saber mais

- **Documentação oficial do Apache Kafka:** https://kafka.apache.org/documentation/
- **Apache Kafka — guia de design e conceitos (log, partições, offsets):** https://kafka.apache.org/intro
- **"Turning the database inside out", de Martin Kleppmann (log como fonte da verdade):** https://martin.kleppmann.com/2015/03/04/turning-the-database-inside-out.html

## Aula 7 — Roteiro da Videoaula 7: "Processamento em tempo real e streaming"

**Duração:** 9 a 10 minutos.

### 1. Abertura (0:00 – 0:45)

> "Até agora a gente tratou o Olist como ele é: 99 mil pedidos parados em CSV. Mas e se esses pedidos estivessem chegando agora, um a um, e a gente quisesse contar pedidos por minuto em tempo real? Hoje a gente simula um stream dos pedidos do Olist — produtor e consumidor em Python, mock de Kafka — e entra no mundo do tempo real."

### 2. Desenvolvimento — parte 1 (0:45 – 3:50)

> "No batch, o dado é finito: roda, termina, entrega — foi o join da aula passada. No streaming, o dado é um fluxo infinito, processado em milissegundos. Muda o modelo mental: em vez de 'quanto o Olist faturou em outubro', você pergunta 'quantos pedidos estão entrando agora, nos últimos 60 segundos'. E o coração disso é a mensageria: um intermediário que desacopla produtor de consumidor. O Kafka é o padrão. E é mais que uma fila: é um log durável — a mensagem não some quando lida. Nosso tópico vai se chamar olist.orders."

### 3. Desenvolvimento — parte 2 (3:50 – 6:50)

> "Três palavras: tópico, partição, offset. Tópico é a categoria, olist.orders. Cada tópico se divide em partições, e daí vem o paralelismo. Dentro da partição, cada mensagem ganha um offset sequencial, e o Kafka garante ordem só dentro da partição. Se eu uso customer_id como chave, todos os pedidos de um cliente caem na mesma partição, em ordem. Agora, na prática: como o Olist é histórico, eu simulo. O stream_orders.py lê raw.orders ordenado por order_purchase_timestamp e emite cada pedido como evento JSON. Um consumidor pega esses eventos e agrega numa janela tumbling de 60 segundos — pedidos por minuto."

### 4. Desenvolvimento — parte 3 (6:50 – 9:00)

> "Como agregar um fluxo que nunca acaba? Com janelas. Tumbling: blocos fixos, pedidos do Olist a cada minuto. Sliding: janela que desliza, faturamento da última hora recalculado a cada 5 minutos. E as garantias: at-most-once pode perder; at-least-once nunca perde mas pode duplicar — e por isso o consumo idempotente da aula 5 volta a brilhar; exactly-once é o ideal mas custa caro. Minha recomendação: at-least-once com processamento idempotente. E como isso conviveria com o batch que já temos? Na arquitetura Kappa: tudo é stream, e o histórico é só o log reprocessado. O mesmo olist.orders alimenta o painel ao vivo e, reprocessado, os marts."

### 5. Encerramento (9:00 – 9:50)

> "Fiz a conta: o Olist tem 135 pedidos por dia, fração de evento por segundo — uma partição sobra. Mas numa Black Friday mil vezes maior, comprimida numa hora, dá uns 37 eventos por segundo, e aí eu já preciso de 4 partições. Partição é o teto do seu paralelismo. Agora você tem batch e streaming no cinto. Mas falta a peça que amarra tudo: quem garante que a ingestão roda antes do dbt, que o teste roda depois, que o retry dispara se algo falhar? Última aula da unidade: orquestração com Apache Airflow, montando o DAG do pipeline Olist. Te espero!"

---

## Aula 8 — Orquestração de pipelines com Apache Airflow

Você já sabe ingerir (Aula 5), processar em lote (Aula 6) e simular um stream (Aula 7) do Olist. Mas até agora rodamos cada passo **na mão**: `dbt run` num terminal, o script de stream noutro. Um pipeline real tem tarefas que dependem umas das outras, em horários certos, com tratamento de falha e prazos. Nesta aula montamos o **DAG `olist_pipeline`** no **Apache Airflow** — `ingest_csv_to_duckdb` → `dbt_run` → `dbt_test` → `export_gold` — e aprendemos a modelar pipelines como **DAGs**, usar **operators**, **agendar**, fazer **backfill** de períodos passados, configurar **retries** e monitorar **SLAs**. É o **primeiro pipeline do Olist orquestrado ponta a ponta**.

### Por que orquestrar pipelines

Um pipeline é uma sequência de passos com **dependências**: no Olist, você só roda o dbt depois de ingerir os CSVs; só testa depois de transformar; só exporta o gold depois de testar. Sem orquestração, isso vira um emaranhado de `cron`s frágeis e falhas silenciosas — o mart sai vazio e ninguém percebe.

Um **orquestrador** gerencia num só lugar: a **ordem** das tarefas, o **agendamento**, o **tratamento de falhas** (retries, alertas), a **observabilidade** (logs, status) e a **recuperação**. O Airflow, criado no Airbnb em 2014, popularizou a filosofia **"pipelines como código"**: você descreve o fluxo em **Python** — então versiona, testa e revisa o pipeline como qualquer software (exatamente o que faremos com o Olist na Unidade 4, com CI/CD).

![Logo do Apache Airflow, plataforma de orquestração de workflows como código](https://commons.wikimedia.org/wiki/Special:FilePath/AirflowLogo.png)

### DAGs, tasks e operators

No Airflow, um pipeline é um **DAG (Directed Acyclic Graph)** — **dirigido** (as setas têm sentido) e **acíclico** (nada depende de si mesmo). Cada nó é uma **task**; as arestas são as dependências. O nosso DAG é exatamente: `ingest_csv_to_duckdb >> dbt_run >> dbt_test >> export_gold`.

Uma task é uma instância de um **operator** — um modelo que sabe executar um tipo de trabalho:

| Operator | O que faz | Uso no `olist_pipeline` |
| --- | --- | --- |
| `PythonOperator` | Executa uma função Python | `ingest_csv_to_duckdb` |
| `BashOperator` | Executa um comando de shell | `dbt run`, `dbt test`, `export_gold` |
| `SQLExecuteQueryOperator` | Roda uma query num banco | (alternativa para o export) |
| Sensors | Esperam por uma condição | (ex.: chegada de um CSV novo) |

A aciclicidade **garante que o pipeline termina** — um grafo com ciclo poderia rodar para sempre.

### O DAG `olist_pipeline`

Aqui está o esqueleto real do DAG, em `airflow/dags/olist_pipeline.py`:

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
import pendulum, duckdb

def ingest_csv_to_duckdb():
    con = duckdb.connect("olist.duckdb")
    con.execute("CREATE SCHEMA IF NOT EXISTS raw")
    con.execute("""CREATE OR REPLACE TABLE raw.orders AS
                   SELECT * FROM read_csv_auto('data/raw/olist_orders_dataset.csv')""")

with DAG(
    dag_id="olist_pipeline",
    start_date=pendulum.datetime(2016, 9, 1, tz="UTC"),
    schedule="@daily",
    catchup=False,
    default_args={"retries": 2, "retry_delay": pendulum.duration(minutes=5)},
) as dag:

    ingest = PythonOperator(task_id="ingest_csv_to_duckdb",
                            python_callable=ingest_csv_to_duckdb)
    dbt_run  = BashOperator(task_id="dbt_run",  bash_command="cd dbt_olist && dbt run")
    dbt_test = BashOperator(task_id="dbt_test", bash_command="cd dbt_olist && dbt test")
    export_gold = BashOperator(task_id="export_gold",
        bash_command="cd dbt_olist && dbt run-operation export_gold")  # marts -> Parquet

    ingest >> dbt_run >> dbt_test >> export_gold
```

Note que `dbt_run` reaproveita os modelos `stg_*` da Aula 5 e que `dbt_test` (Unidade 4) garante qualidade *antes* de publicar o gold — a ordem não é casual.

### Agendamento, data interval e dependências

Cada DAG tem um `schedule`: uma expressão `cron` (`0 6 * * *` = todo dia às 6h), um preset (`@daily`) ou um intervalo. O Airflow trabalha com **data interval**: cada execução está ligada a um *período de dados* (a "data lógica"), não ao relógio de quando disparou. É isso que torna o reprocessamento determinístico — cada run do `olist_pipeline` "sabe" qual dia do Olist está processando. As dependências usam `>>` (montante → jusante); tasks sem dependência entre si rodam **em paralelo**.

### Backfill e retries

Duas funcionalidades fazem o Airflow brilhar. O **backfill** executa o pipeline para **períodos passados** — quando você cria o `olist_pipeline` e quer popular o histórico de 2016–2018, roda um backfill por todo o intervalo. Como cada execução está atrelada a uma data lógica, o Airflow sabe qual janela reprocessar — e aqui a **idempotência** da Aula 5 (`unique_key='order_id'`) é o que torna o backfill seguro: reprocessar um dia do Olist não duplica pedidos.

Os **retries** automatizam a resiliência: definimos `retries=2` e `retry_delay` (idealmente com *backoff exponencial*). Uma falha transitória — o disco ocupado, uma leitura de CSV que oscilou — se resolve sozinha, sem acordar ninguém.

### Monitoramento e alertas

O Airflow oferece uma **interface web** rica: visão em grafo do `olist_pipeline`, *grid view* com o histórico colorido por status, logs de cada task e re-disparo manual. Integra **alertas**: `email_on_failure`, *callbacks* (`on_failure_callback`) para Slack/plantão, e métricas para Prometheus/Grafana. Observabilidade é o que separa um pipeline que "deveria estar funcionando" de um que você *sabe* que está.

### Exemplo numérico: caminho crítico e SLA do `olist_pipeline`

Suponha estes tempos médios para o pipeline Olist e suas janelas de retry:

| Task | Tempo médio | Retries × delay |
| --- | --- | --- |
| `ingest_csv_to_duckdb` | $4$ min | $2 \times 5$ min |
| `dbt_run` | $3$ min | $1 \times 5$ min |
| `dbt_test` | $2$ min | $1 \times 5$ min |
| `export_gold` | $1$ min | $1 \times 5$ min |

O **caminho crítico** em condições normais (sem falhas) é a soma sequencial:

$$
T_{normal} = 4 + 3 + 2 + 1 = 10\ \text{min}
$$

No **pior caso**, com todos os retries acionados:

$$
T_{pior} = (4 + 2\cdot5) + (3 + 1\cdot5) + (2 + 1\cdot5) + (1 + 1\cdot5) = 14 + 8 + 7 + 6 = 35\ \text{min}
$$

Se os marts do Olist (vendas por categoria, performance de entrega) devem estar prontos às **8h00**, o DAG deve iniciar, no pior caso, até $08{:}00 - 35\ \text{min} = 07{:}25$. Para margem, agenda-se às **7h00** (`0 7 * * *`) com um **SLA de 35 min**: se atrasar, o Airflow dispara o alerta — e o time age *antes* de alguém abrir um dashboard vazio.

### Atividade prática

Suba o Airflow localmente (via `docker compose` oficial ou `astro dev start` da Astronomer).

1. Crie o DAG `olist_pipeline` com `schedule="@daily"` e as quatro tasks: `ingest_csv_to_duckdb` (`PythonOperator`), `dbt_run`, `dbt_test` e `export_gold` (`BashOperator`).
2. Declare a ordem: `ingest_csv_to_duckdb >> dbt_run >> dbt_test >> export_gold` e confira o grafo na UI.
3. Configure `retries=2` e `retry_delay`; force uma falha no `ingest` (ex.: aponte para um CSV inexistente) e observe o retry na interface.
4. Defina um `sla` no `export_gold` e dispare um **backfill** de 3 dias passados (`airflow dags backfill`). Confirme — contando `order_id` em `stg_orders` — que a **idempotência** impediu duplicação.

### Pontos-chave

- A **orquestração** coordena ordem, agendamento, falhas, observabilidade e recuperação do pipeline Olist.
- No Airflow, o pipeline é um **DAG**; o nosso é `olist_pipeline`: `ingest_csv_to_duckdb >> dbt_run >> dbt_test >> export_gold`.
- O **agendamento** usa `@daily`/`cron` e o **data interval** (data lógica), o que torna o reprocessamento determinístico.
- **Backfill** reexecuta o histórico do Olist (2016–2018); **retries** com backoff resolvem falhas transitórias — ambos exigem a **idempotência** da Aula 5.
- **SLA**, alertas e a UI dão a **observabilidade** que torna o `olist_pipeline` confiável de verdade.

### Para saber mais

- **Documentação oficial do Apache Airflow:** https://airflow.apache.org/docs/
- **Conceitos centrais do Airflow (DAGs, operators):** https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/operators.html
- **Agendamento e parâmetros de DAG (schedule, retries, SLA):** https://www.astronomer.io/docs/learn/airflow-dag-parameters/

### O que você verá na próxima unidade

Na **Unidade 3 — Armazenamento e Arquitetura de Dados**, paramos de **mover** o dado do Olist e focamos em **onde** e **como** guardá-lo bem. O dado do Olist já entra (Aula 5), é processado (Aula 6), poderia ser transmitido (Aula 7) e está orquestrado pelo `olist_pipeline` (Aula 8) — agora vamos **armazenar e arquitetar**. Você vai construir o **data warehouse do Olist em camadas com dbt** (staging → core → marts, com as dimensões e fatos da estrela e SCD2 em `dim_sellers`), organizar o storage em **Medallion** (bronze/silver/gold em Parquet, lendo o Olist como um **lakehouse local**), ver como o **mesmo dbt** rodaria na nuvem (BigQuery/Snowflake) trocando só o `profiles.yml`, e montar a **Modern Data Stack** com BI sobre o DuckDB. É hora de dar à torrente de dados do Olist uma **casa bem arquitetada**.

## Aula 8 — Roteiro da Videoaula 8: "Orquestração de pipelines com Apache Airflow"

**Duração:** 9 a 10 minutos.

### 1. Abertura (0:00 – 0:45)

> "Você já sabe ingerir, processar em lote e simular um stream do Olist. Mas até agora a gente rodou cada passo na mão: dbt run num terminal, o stream noutro. Um pipeline real amarra tudo isso. Hoje a gente monta o DAG olist_pipeline no Airflow: ingerir, dbt run, dbt test, exportar o gold. O primeiro pipeline do Olist orquestrado ponta a ponta."

### 2. Desenvolvimento — parte 1 (0:45 – 3:50)

> "Sem orquestração, o pipeline vira um monte de crons frágeis e o mart sai vazio sem ninguém perceber. O orquestrador resolve num lugar só: ordem, agendamento, retries, logs, recuperação. O Airflow, do Airbnb em 2014, trouxe a filosofia pipeline como código: você descreve o fluxo em Python. No Airflow o pipeline é um DAG: grafo dirigido e acíclico. Dirigido porque as setas têm sentido; acíclico porque nada depende de si mesmo — é isso que garante que termina. O nosso é direto: ingest_csv_to_duckdb, seta, dbt_run, seta, dbt_test, seta, export_gold."

### 3. Desenvolvimento — parte 2 (3:50 – 6:50)

> "Cada nó é uma task, instância de um operator. O ingest é um PythonOperator que conecta no DuckDB e recria o raw.orders a partir do CSV. O dbt_run e o dbt_test são BashOperator rodando dbt run e dbt test — repare que o teste vem antes de exportar o gold: a gente só publica o mart se passar na qualidade. O agendamento é @daily, e o conceito-chave é o data interval: cada execução está ligada a um período de dados, uma data lógica, não ao relógio. É isso que torna o reprocessamento determinístico — cada run sabe qual dia do Olist está processando."

### 4. Desenvolvimento — parte 3 (6:50 – 9:00)

> "Duas joias da operação: backfill e retries. Backfill reexecuta o histórico — quero popular 2016 a 2018 do Olist? Backfill no intervalo inteiro. E aqui a idempotência da aula 5 volta: o unique_key igual a order_id faz com que reprocessar um dia não duplique pedido. Retries automatizam a resiliência: retries igual a 2, retry_delay com backoff, e a leitura de CSV que oscilou se resolve sozinha. E não esqueça da observabilidade: a UI mostra o grafo do olist_pipeline, o histórico colorido, os logs; configure alerta no e-mail ou Slack e um SLA de tempo de entrega."

### 5. Encerramento (9:00 – 9:50)

> "Fechei com a conta de SLA: o olist_pipeline tem caminho crítico de 10 minutos, 35 no pior caso com todos os retries, então eu agendo às 7h para entregar os marts às 8h com folga. Esse é o cinto completo da Unidade 2: ingerir, processar em lote, simular o stream e orquestrar. Agora o dado do Olist já entra, é processado e está orquestrado. Na próxima unidade a gente para de mover e aprende a guardar bem — data warehouse em camadas com dbt, lakehouse com Medallion, nuvem. Te espero!"

---

## Quiz não avaliativo

### Questão 1

No projeto do Olist, configuramos o modelo `stg_orders` no dbt como `materialized='incremental'` com `unique_key='order_id'`. Sobre **ETL vs ELT** e essa escolha, assinale a alternativa **correta**:

- [ ] a. A configuração descreve um pipeline ETL, pois a transformação dos pedidos ocorre num servidor intermediário antes de tocar o DuckDB.
- [x] b. É um pipeline **ELT**: os CSVs do Olist entram crus no schema `raw` e o **dbt** transforma dentro do DuckDB; o `unique_key='order_id'` garante **idempotência** (rodar duas vezes não duplica pedidos).
- [ ] c. O `unique_key` serve para ordenar os pedidos por data, não tem relação com idempotência ou duplicação.
- [ ] d. A carga incremental do Olist relê os ~99 mil pedidos a cada execução; o ganho está apenas em comprimir os dados.

**Resposta correta:** `b`

**Feedback:** A (b) está correta: no nosso projeto os CSVs do Olist entram crus no `raw` e o **dbt** os transforma *dentro* do DuckDB — padrão **ELT**. O `unique_key='order_id'` faz o dbt aplicar um *MERGE*/upsert por pedido, dando **idempotência**: reprocessar não duplica. A (a) inverte os conceitos (não há servidor intermediário; a transformação é no destino). A (c) erra a função do `unique_key` (é a chave do upsert, base da idempotência). A (d) descreve carga full, não incremental — a incremental lê só os pedidos novos (`order_purchase_timestamp` maior que o máximo já carregado).

### Questão 2

No produtor `stream_orders.py`, emitimos cada pedido do Olist no tópico `olist.orders` usando `customer_id` como chave. Sobre **tópicos, partições e offsets** no Kafka, assinale a alternativa **correta**:

- [ ] a. Usar `customer_id` como chave não influencia em nada o particionamento; os pedidos do mesmo cliente caem em partições aleatórias.
- [ ] b. O Kafka garante ordem total entre todas as partições de `olist.orders`, então a sequência global dos pedidos é sempre preservada.
- [x] c. A escalabilidade vem das **partições**; mensagens com a mesma chave (`customer_id`) vão para a **mesma partição**, onde a **ordem** é garantida, e o **offset** controla até onde o consumidor já leu.
- [ ] d. Aumentar o número de partições de `olist.orders` reduz o paralelismo de consumo, pois cada consumidor precisa ler todas as partições.

**Resposta correta:** `c`

**Feedback:** A (c) está correta: partições são a unidade de paralelismo; usar `customer_id` como **chave** envia todos os pedidos de um cliente para a **mesma partição** (mantendo a ordem deles), e o **offset** é o índice sequencial que permite ao consumidor retomar, reprocessar ou avançar. A (a) é falsa — a chave determina a partição (mesma chave → mesma partição). A (b) é falsa — o Kafka garante ordem **apenas dentro de uma partição**, nunca total entre elas. A (d) inverte o conceito: mais partições **aumentam** o teto de paralelismo do consumo.

---

## Atividade Verificadora (AAI — Atividade Avaliativa Individual)

**Pergunta:**

> A diretoria do Olist pediu duas coisas ao time de dados, sobre o **mesmo** fluxo de pedidos: (1) um **painel de operação em tempo real** que mostre "pedidos por minuto" e dispare um **alerta** quando um mesmo `customer_id` fizer 5 pedidos em 2 minutos; e (2) os **marts analíticos diários** (`mart_sales_by_category`, `mart_delivery_performance`), que precisam estar prontos todo dia até as **8h**, sem duplicar nem perder pedidos.
>
> Estruture sua resposta em três partes, usando a stack do nosso projeto (DuckDB, dbt, Airflow, mock de Kafka):
>
> 1. **Arquitetura de ingestão e processamento** — para cada requisito, escolha entre **batch** e **streaming**, justifique e nomeie o componente do projeto que o atende (ex.: produtor/consumidor `stream_orders.py` no tópico `olist.orders`; modelos `stg_*` + marts via dbt; DAG `olist_pipeline` no Airflow).
> 2. **Confiabilidade** — que **garantia de entrega** você adotaria no fluxo de tempo real e como garantiria que os marts diários **não duplicam nem perdem** pedidos (cite explicitamente **idempotência** via `unique_key='order_id'` e o papel do **CDC** se o Olist fosse um banco ao vivo).
> 3. **Operação** — como você orquestraria e monitoraria os marts diários no `olist_pipeline` (`schedule`, `retries`, `SLA`, `backfill`) para cumprir as 8h mesmo com falhas transitórias.

**Resposta esperada:**

> Uma resposta de qualidade separa os dois caminhos. Para o **painel em tempo real**, escolhe **streaming**: os pedidos como eventos no tópico `olist.orders`, **particionado por `customer_id`** (garantindo ordem por cliente), com o produtor/consumidor `stream_orders.py`; o alerta "5 pedidos em 2 minutos" usa uma **janela sliding** (deslizante, porque a contagem precisa ser contínua, não em blocos fixos); justifica que batch é inviável pelo requisito de tempo real. Para os **marts diários**, escolhe **batch**: os modelos `stg_*` e os marts (`mart_sales_by_category`, `mart_delivery_performance`) construídos pelo **dbt** dentro do DuckDB, **orquestrados pelo DAG `olist_pipeline`** no Airflow. Em **confiabilidade**, no fluxo de tempo real adota **at-least-once com consumo idempotente** (perder um pedido é pior que contá-lo duas vezes; exactly-once é caro e desnecessário se o consumo é idempotente); para os marts, garante ausência de perda e duplicação via **carga incremental + idempotência** — o `stg_orders` com `unique_key='order_id'` faz upsert por pedido, então reprocessar não duplica — e menciona que, **se o Olist fosse um Postgres ao vivo**, um **CDC** (Debezium no WAL) capturaria inserts/updates/deletes em quase tempo real. Em **operação**, descreve o `olist_pipeline` com `schedule` (`cron`/`@daily`) calculado a partir do **caminho crítico** somado aos **retries** (com backoff), define um **SLA** com margem para entregar antes das 8h, configura **alertas** (e-mail/Slack) em falha e violação de SLA, e usa **backfill** idempotente para reprocessar dias com problema. A melhor resposta demonstra **pensamento sistêmico**: streaming e batch coexistem sobre o **mesmo** fluxo de pedidos (arquitetura **Kappa** — o log `olist.orders` alimenta o painel ao vivo e, reprocessado, os marts), e a **idempotência** é o fio que costura confiabilidade e reprocessamento em todas as camadas. Deve evitar "usar Spark para tudo" (o DuckDB resolve o Olist no laptop) ou "exactly-once em tudo" sem justificar custo/benefício.

---

## Material complementar

### Direto da fonte — livro da Biblioteca Virtual

> Este é o livro de cabeceira da engenharia de dados moderna e cobre, em um só lugar, todo o coração desta unidade: ingestão (ETL vs ELT, batch vs CDC), o ciclo de vida do dado e a orquestração com DataOps. Reis e Housley são pragmáticos e atemporais — explicam *princípios* que sobrevivem à troca de ferramentas, exatamente os que aplicamos ao montar o `dbt_olist`, o stream do Olist e o DAG `olist_pipeline`. Leitura direta sobre tudo o que destrinchamos nas Aulas 5 a 8.

- **Nome do livro:** *Fundamentals of Data Engineering: Plan and Build Robust Data Systems*
- **Capítulo:** Capítulos 7 (Ingestão), 8 (Consultas, modelagem e transformação) e 2 (Ciclo de vida da engenharia de dados)
- **Organizador:** Joe Reis e Matt Housley
- **Editora:** O'Reilly Media
- **Link de acesso (BV):** https://learning.oreilly.com/library/view/fundamentals-of-data/9781098108298/
- **Aula em que entra:** Aulas 5 a 8

### Para mergulhar no assunto

> Recomendo a leitura **"Turning the database inside out"**, de Martin Kleppmann (autor de *Designing Data-Intensive Applications*). Kleppmann mostra como **logs de eventos** — a ideia central do Kafka e do nosso tópico `olist.orders` — reorganizam toda a arquitetura de dados. É uma daquelas leituras que "viram a chave" sobre streaming, CDC e a arquitetura Kappa que discutimos na Aula 7: por que tratar o histórico do Olist como um log reprocessável muda tudo. Combine com o livro *Designing Data-Intensive Applications* para aprofundar.

- **Link(s):** https://martin.kleppmann.com/2015/03/04/turning-the-database-inside-out.html — livro: *Designing Data-Intensive Applications*, Martin Kleppmann (O'Reilly, 2017)
- **Aula em que entra:** Aulas 5 e 7

### Podcast (curadoria, até 45 min)

> O canal **Databricks (YouTube)** mantém uma série excelente de explicações curtas e palestras sobre Apache Spark, structured streaming e arquiteturas lakehouse, direto de quem criou o Spark. Ótimo para fixar os conceitos das Aulas 6 e 7 — o mesmo join+agregação que rodamos em DuckDB no Olist, agora explicado em escala de cluster, com demonstrações reais de produção.

- **Nome do podcast/canal:** Databricks
- **Tema recomendado:** "Apache Spark fundamentals / Structured Streaming"
- **Link:** https://www.youtube.com/@Databricks (YouTube)
- **Aula em que entra:** Aulas 6 e 7

### Artigo científico

> O artigo fundador de toda a engenharia de dados distribuída moderna. Dean e Ghemawat, do Google, descrevem o modelo **MapReduce** que inspirou o Hadoop e, indiretamente, o Apache Spark da Aula 6. Ler o original é entender de onde vêm as ideias de *map*, *reduce*, paralelismo de dados e tolerância a falhas — as mesmas que aparecem quando o nosso `groupBy` por categoria do Olist gera um *shuffle*. Um paper de 2004 que ainda molda as ferramentas que usamos hoje.

- **Link:** https://doi.org/10.1145/1327452.1327492 (DOI)
- **Aula em que entra:** Aula 6
- **Referência bibliográfica do artigo no formato ABNT:**
  > DEAN, Jeffrey; GHEMAWAT, Sanjay. **MapReduce: simplified data processing on large clusters**. *Communications of the ACM*, v. 51, n. 1, p. 107-113, jan. 2008.
