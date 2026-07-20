# Roteiros Estendidos Hands-on (15–20 minutos) — Unidade 2: Ingestão e Processamento de Dados

- **Disciplina:** Data Engineering and Pipelines
- **Conteudista:** Afonso Cesar Lelis Brandão
- **Videoaulas:** 5 a 8
- **Formato:** roteiro de gravação **hands-on em GitHub Codespaces** — fala em citação (>), código executado na demonstração. Duração-alvo: **15 a 20 minutos** por aula.

> **Convenções:** **[TELA]** slide/Codespace · **[CÓDIGO]** digitar/colar · **[EXECUTAR]** rodar e mostrar saída · **[CHECKPOINT]** resultado esperado.
> **Preparação da unidade:** o Codespace deve estar com a Unidade 1 concluída (`data/raw` com os nove CSVs e `olist.duckdb` com o schema `raw`). A imagem do devcontainer deve incluir Java 17. Antes da Aula 6, execute `pip install "pyspark==3.5.6"`. Antes da Aula 8, instale o Airflow com o comando e o arquivo de constraints indicados no roteiro.

---

## Roteiro da Videoaula 5 — "ETL vs ELT: criação do projeto dbt do Olist"

**Duração-alvo:** 17 a 19 minutos.

### 1. Abertura (0:00 – 1:15)

**[TELA]** Slide de capa; Codespace ao lado.

> "Na Unidade 1, os nove arquivos CSV foram carregados no schema `raw` por scripts Python. Nesta aula, esse processo será organizado em um projeto **`dbt_olist`**, segundo o padrão ELT. Serão criados modelos de staging e uma carga incremental, com atenção à idempotência, propriedade que permite repetir uma execução sem alterar indevidamente o resultado."

### 2. ETL × ELT: as duas filosofias (1:15 – 3:45)

**[TELA]** Slide: tabela ETL × ELT.

> "Primeiro, o conceito que organiza a aula. **Ingestão** é mover dado da fonte ao destino — no nosso caso, dos 9 CSVs para o `olist.duckdb`. É a primeira fronteira do pipeline, e a mais frágil. E há duas filosofias para isso. **ETL** — *Extract, Transform, Load*: extrai, transforma num servidor **intermediário** e só então carrega o dado já refinado. Nasceu quando armazenamento era caro. O problema: se você descobre depois que precisava de uma coluna que descartou — o `seller_id` que jogou fora — precisa **reextrair da fonte**. **ELT** — *Extract, Load, Transform*: inverte — carrega o **bruto** no destino e transforma **lá dentro**, com o poder do warehouse. É o nosso padrão: os CSVs entram crus no `raw`, e o dbt transforma em SQL declarativo."

> "O ELT venceu porque armazenar ficou barato — os 120 megabytes crus do Olist custam frações de centavo, fizemos essa conta na Aula 1 — e porque os motores ficaram poderosos. Carregar o bruto primeiro significa **guardar a fonte da verdade**: errou a transformação? Re-roda `dbt run`. Sem reextração, sem drama. E guarda o princípio recorrente do curso: **o que roda local com DuckDB e dbt migra para a nuvem trocando só o profile — os conceitos são os mesmos**."

### 3. Demonstração prática: criando o projeto dbt (3:45 – 7:15)

**[TELA]** Terminal do Codespace.

> "Vamos criar o projeto. O **dbt** — *data build tool* — é a ferramenta que transforma SQL solto em projeto de engenharia: versionado, testável, documentado. Já instalamos o `dbt-duckdb` lá na Aula 1; agora é usar."

**[CÓDIGO]** Criar o projeto e o profile:

```bash
dbt init dbt_olist --skip-profile-setup
cd dbt_olist
rm -rf models/example
```

**[CÓDIGO]** Criar `dbt_olist/profiles.yml` e informar explicitamente ao dbt onde está o arquivo:

```yaml
dbt_olist:
  target: dev
  outputs:
    dev:
      type: duckdb
      path: ../olist.duckdb
      schema: main
      threads: 4
```

**[EXECUTAR]**

```bash
export DBT_PROFILES_DIR="$PWD"
dbt debug
```

**[CHECKPOINT]**

> "`All checks passed!` — o dbt encontrou o projeto, o profile e conectou no nosso `olist.duckdb`. Observe na elegância: o `profiles.yml` diz apenas 'tipo duckdb, caminho do arquivo'. Se um dia esse projeto for para o BigQuery ou o Snowflake, **só esse arquivo muda** — os modelos SQL ficam idênticos. É a portabilidade que eu prometi."

> "Agora, o primeiro conceito de organização do dbt: os **sources**. Nós declara as tabelas do schema `raw` como fontes nomeadas — assim o dbt conhece a origem, consegue testá-la e desenha a **linhagem** do dado."

**[CÓDIGO]** Criar `models/staging/_olist__sources.yml`:

```yaml
version: 2
sources:
  - name: olist_raw
    schema: raw
    tables:
      - name: orders
      - name: order_items
      - name: order_payments
      - name: order_reviews
      - name: products
      - name: customers
      - name: sellers
```

> "Sete das nove tabelas viram source agora — `geolocation` e a tradução de categorias entram na Unidade 3, quando enriquecermos as dimensões. Aliás, a tradução de categorias — 71 linhas que quase nunca mudam — nem vai ser 'ingerida': ela vai virar um **seed**, um CSV pequeno e estável versionado junto do código, que o `dbt seed` materializa como tabela. Cada coisa com o mecanismo do seu tamanho."

### 4. Os modelos staging (7:15 – 10:00)

**[TELA]** Editor.

> "E agora a primeira camada de transformação: os modelos **staging** — `stg_*`. A regra do staging é ascética: **um para um com a fonte** — renomeia, casta tipos, limpa; **sem join, sem agregação**. É a fundação sobre a qual tudo se constrói. Vamos escrever três."

**[CÓDIGO]** Criar `models/staging/stg_orders.sql` — o mais importante, já **incremental**:

```sql
{{ config(materialized='incremental', unique_key='order_id') }}

select
    order_id,
    customer_id,
    order_status,
    cast(order_purchase_timestamp as timestamp)      as purchased_at,
    cast(order_delivered_customer_date as timestamp) as delivered_at
from {{ source('olist_raw', 'orders') }}
{% if is_incremental() %}
  where order_purchase_timestamp > (select max(purchased_at) from {{ this }})
{% endif %}
```

**[CÓDIGO]** Criar `models/staging/stg_order_items.sql` e `models/staging/stg_customers.sql`:

```sql
-- stg_order_items.sql
select
    order_id,
    order_item_id,
    product_id,
    seller_id,
    cast(price as double)         as price,
    cast(freight_value as double) as freight_value
from {{ source('olist_raw', 'order_items') }}
```

```sql
-- stg_customers.sql
select
    customer_id,
    customer_unique_id,
    customer_city,
    customer_state
from {{ source('olist_raw', 'customers') }}
```

> "Observe na sintaxe do `stg_orders`, porque cada pedaço conta uma história. O `config`: **materialized incremental** com **unique_key order_id** — já explico o poder disso. O corpo: renomeia `order_purchase_timestamp` para `purchased_at` e **casta** para timestamp — chega de string fingindo ser data. E o bloco `is_incremental()`: **na primeira execução ele é ignorado** e a carga é full; **das próximas em diante**, só entram pedidos **mais novos** que o máximo já carregado. Um modelo, dois comportamentos, zero código duplicado."

### 5. Dbt run — e a prova da idempotência (10:00 – 13:00)

**[EXECUTAR]**

```bash
dbt run
```

**[CHECKPOINT]**

> "Observe o log: três modelos, três `OK` — `stg_orders` criado como **incremental**, os outros como view. O dado do Olist agora está limpo, tipado e renomeado dentro do banco. E agora, o teste que separa pipeline amador de pipeline profissional. Pergunta: o que acontece se eu rodar **de novo**?"

**[EXECUTAR]**

```bash
python -c "import duckdb; print(duckdb.connect('../olist.duckdb').sql('select count(*) as pedidos from main.stg_orders'))"
dbt run
python -c "import duckdb; print(duckdb.connect('../olist.duckdb').sql('select count(*) as pedidos from main.stg_orders'))"
```

**[CHECKPOINT]**

> "Contagem antes: **99.441**. Rodei o pipeline inteiro de novo... Contagem depois: **99.441**. Idênticos! Isso é **idempotência**: executar dez vezes produz o mesmo estado que executar uma. E não é mágica — é o `unique_key`: o dbt faz um *merge*, um upsert por `order_id`, por baixo dos panos. Por que isso salva madrugadas? Porque **pipeline falha — é certeza, não possibilidade**. E quando falha às 3 da manhã e o retry dispara, o pipeline idempotente se recupera sozinho sem duplicar um pedido sequer. O não-idempotente duplica tudo e o relatório da diretoria amanhece dobrado. Guarda essa palavra: ela volta na Aula 8, no backfill do Airflow."

> "E a conta que justifica o incremental: o Olist tem 99.441 pedidos; a média é 135 por dia. Recarregar tudo toda execução versus carregar só o dia: **736 vezes** mais barato. Aqui, é a diferença entre 2 segundos e 3 milésimos — irrelevante. Mas projeta o 'Olist vezes mil' de um marketplace grande: a full passa de meia hora; a incremental continua em segundos. Arquitetura certa não é a que funciona hoje — é a que sobrevive ao crescimento."

### 6. CDC: e se o Olist fosse um banco vivo? (13:00 – 14:30)

**[TELA]** Slide: CDC/Debezium lendo o WAL.

> "Última peça conceitual: e se, além de inserts, eu precisasse capturar **updates e deletes** da fonte? A carga incremental por timestamp não vê um delete — a linha simplesmente some. A resposta é o **CDC** — *Change Data Capture*: em vez de consultar a tabela, lê-se o **log de transações** do banco-fonte — o WAL do PostgreSQL — e replica-se cada INSERT, UPDATE e DELETE como evento. Como o nosso Olist é CSV estático, o CDC fica teórico — mas guarda a ponte: **se o Olist fosse um Postgres na demonstração, plugaríamos o Debezium no WAL e cada pedido novo viraria um evento emitido em tempo real**. Evento. Tempo real. É exatamente o assunto da Aula 7. Nada nesta disciplina é por acaso."

### 7. Commit + atividade e preparação para a próxima aula (14:30 – 16:30)

**[CÓDIGO]**

```bash
cd ..
git add dbt_olist
git commit -m "feat(dbt): projeto dbt_olist com sources e staging incremental idempotente"
git push
```

> "A atividade proposta: reproduzir o projeto — `dbt init`, profile, sources e os três `stg_*`; rodar `dbt run` **duas vezes** e provar com o `count` que a idempotência segura a contagem em 99.441; e documentar em três linhas por que o Olist é ELT e não ETL. E na próxima aula, com o dado limpo, vem a pergunta de negócio pesada: faturamento por categoria — juntar e agregar 112 mil linhas. É o **processamento em lote**: o Apache Spark na teoria — MapReduce, shuffle, lazy evaluation — e o DuckDB na prática, com os dois rodando lado a lado na nossa tela."

---

## Roteiro da Videoaula 6 — "Processamento em lote: Spark na teoria, DuckDB na prática"

**Duração-alvo:** 16 a 18 minutos.

### 1. Abertura (0:00 – 1:15)

**[TELA]** Slide de capa.

> "O dado do Olist está limpo nos modelos staging. Agora, a pergunta de negócio: **qual o faturamento por categoria?** Responder exige **juntar** itens com produtos e **agregar** sobre 112 mil linhas — isso é **processamento em lote**, e o nome mais famoso desse mundo é **Apache Spark**. Hoje você entende a ideia fundadora — o MapReduce do Google —, a arquitetura do Spark, por que ele é 'preguiçoso' e qual operação custa mais caro. E rodamos **os dois lado a lado no Codespace**: o mesmo job em PySpark e em DuckDB, com cronômetro."

### 2. MapReduce: a ideia que fundou tudo (1:15 – 3:30)

**[TELA]** Slide: map → shuffle → reduce, com o exemplo Olist.

> "A revolução tem data: **2004**, quando o Google publicou o paper do **MapReduce** — que está no material complementar, e vale ler o original. A ideia genial numa frase: **em vez de levar terabytes de dados até um supercomputador, leve o código até onde os dados já estão** — espalhados em milhares de máquinas baratas. Duas fases: no **map**, cada máquina aplica uma função ao seu pedaço e emite pares chave-valor; no **reduce**, os pares de mesma chave se encontram e são combinados. Aplicado ao Olist: para faturar por categoria, o map emite `(categoria, preço)` para cada item; o reduce soma os preços por categoria. Simples assim — e foi essa simplicidade que escalou o Google."

> "O **Hadoop** popularizou o modelo no mundo open source — mas com um vício: gravava os resultados intermediários **em disco** entre cada etapa. Custo brutal. E aí nasceu o **Spark**, com uma pergunta: e se os intermediários ficassem **em memória**? Ganhos de ordens de grandeza. É o motor de lote dominante até hoje."

### 3. Arquitetura e abstrações do Spark (3:30 – 5:45)

**[TELA]** Slide: driver + executors + cluster manager; RDD → DataFrame → Dataset.

> "Como um job Spark se organiza? O **driver** é o cérebro: hospeda o contexto, monta o plano de execução — um DAG de operações — e distribui tarefas. Os **executors** são os músculos: processos espalhados pelo cluster que executam as tasks e guardam dados em memória. E um **cluster manager** — YARN, Kubernetes — negocia os recursos. O trabalho é fatiado em **tasks**, uma por partição de dados, agrupadas em **stages**."

> "E você conversa com o Spark por três abstrações, em ordem de conforto: o **RDD** — a coleção distribuída original, de baixo nível, resiliente porque registra a própria linhagem e se reconstrói após falha; o **DataFrame** — dados em colunas nomeadas, como uma tabela, que passa pelo otimizador **Catalyst**: é o que você usa 90% do tempo, e é exatamente como já pensamos a nossa `fct_order_items`; e o **Dataset**, o tipado, para Scala e Java. Para nós, engenheiros pragmáticos: **DataFrame**."

### 4. Demonstração prática: o job em PySpark (5:45 – 9:30)

**[TELA]** Editor + terminal (PySpark já instalado antes da gravação).

**[CÓDIGO]** Criar `processing/batch_spark.py`:

```python
from pyspark.sql import SparkSession, functions as F
from pyspark.sql.functions import broadcast

spark = SparkSession.builder.appName("olist_batch").getOrCreate()
items    = spark.read.parquet("data/bronze/order_items.parquet")
products = spark.read.parquet("data/bronze/products.parquet")

faturamento = (
    items.join(products, "product_id")          # wide -> shuffle
         .groupBy("product_category_name")      # wide -> shuffle
         .agg(F.sum("price").alias("receita"))
         .orderBy(F.desc("receita"))
)

faturamento.explain()      # mostra o plano ANTES de executar
faturamento.show(10)       # a ACAO que dispara tudo
```

**[EXECUTAR]**

```bash
mkdir -p processing
python processing/batch_spark.py
```

**[CHECKPOINT]**

> "Duas coisas para observar na saída. Primeiro, o **plano** que o `explain()` imprimiu **antes** de qualquer execução — e procura comigo a palavra **`Exchange`**: apareceu **duas vezes**. Exchange é o nome do **shuffle** no plano — e o nosso job tem dois: o `join` por `product_id` e o `groupBy` por categoria. Segundo: o ranking de receita — beleza e saúde, relógios, cama mesa e banho — batendo com o que calculamos na Aula 3. Mesma estrela, outro motor."

> "E aqui os dois conceitos-chave do Spark, que você acabou de ver na demonstração. Um: ele é **lazy** — o `join` e o `groupBy` não executaram nada; só anotaram nós no plano. Foi o `show()`, uma **ação**, que disparou o DAG — e essa preguiça é virtude: o Catalyst enxerga o pipeline inteiro antes de rodar e otimiza — reordena filtros, poda colunas. Dois: o **shuffle** é a operação mais cara do mundo distribuído — dados da mesma chave precisam se **encontrar** na mesma partição, e isso significa redistribuição massiva pela rede. Otimizar Spark é, acima de tudo, **domar o shuffle**."

**[CÓDIGO]** A otimização clássica — *broadcast join* (adicionar ao script e rodar de novo):

```python
faturamento_broadcast = (
    items.join(broadcast(products), "product_id")   # products: só ~33k linhas!
         .groupBy("product_category_name")
         .agg(F.sum("price").alias("receita"))
)
faturamento_broadcast.explain()
```

> "A `products` tem só 33 mil linhas — cabe na memória de qualquer executor. O `broadcast` manda uma **cópia inteira dela para cada nó**, e o join acontece localmente, **sem shuffle**. Observe o novo plano: o Exchange do join **sumiu** — sobrou só o do groupBy. Um shuffle a menos, sem custo adicional de licenciamento. Regra de bolso: dimensão pequena, broadcast sempre."

### 5. O mesmo job no DuckDB — com cronômetro (9:30 – 12:00)

**[CÓDIGO]** Rodar o equivalente DuckDB medindo o tempo:

```bash
python - <<'EOF'
import duckdb, time
t0 = time.time()
con = duckdb.connect("olist.duckdb")
print(con.sql("""
    SELECT p.product_category_name AS categoria,
           ROUND(SUM(i.price), 2)  AS receita
    FROM   raw.order_items i
    JOIN   raw.products    p USING (product_id)
    GROUP  BY p.product_category_name
    ORDER  BY receita DESC
    LIMIT 10
"""))
print(f"tempo: {time.time() - t0:.3f} s")
EOF
```

**[CHECKPOINT]**

> "Mesmo ranking. E observe o cronômetro: **frações de segundo** — contra os vários segundos que o Spark levou só para subir a sessão. E essa é a mensagem central da aula, que eu quero que você leve para a carreira: **o DuckDB resolve o Olist no laptop; o Spark entra quando o Olist vira 'Olist vezes dez mil'** e não cabe mais numa máquina. Usar cluster para dado que cabe na memória é pagar caro pelo overhead da distribuição. O bom engenheiro dimensiona o motor pelo dado — não pelo hype. Mas os **conceitos** — lazy, shuffle, broadcast, partições — são idênticos nos dois mundos: você aprendeu Spark de verdade rodando DuckDB."

### 6. A Lei de Amdahl: por que mais máquina não resolve tudo (12:00 – 14:00)

**[TELA]** Slide com a conta de Amdahl.

> "E fecho a parte conceitual com a lei que todo engenheiro de dados deveria recitar antes de pedir cluster maior: a **Lei de Amdahl**. Suponha que o nosso join-agregação leve 60 segundos num core. Em 8 cores, o ideal seriam 60 sobre 8: **7,5 segundos**. Mas o paralelismo nunca é perfeito — o shuffle final, juntar os parciais por categoria, é **serial**. Se 20% do trabalho é serial, o ganho máximo com 8 cores é 1 sobre 0,2 mais 0,8 sobre 8: **3,33 vezes** — tempo real de uns **18 segundos**, não 7,5. E com 100 cores? O teto continua sendo 1 sobre 0,2: **5 vezes**. Nunca mais que isso."

> "A lição gravada em pedra: **adicionar máquinas tem retorno decrescente; reduzir a fração serial — o shuffle! — rende mais que comprar hardware**. Filtre antes de juntar, use broadcast, particione pela chave certa. No Olist, o DuckDB faz tudo em menos de um segundo — Amdahl só morde quando o dado é mil vezes maior. Mas quando morder, você já sabe onde dói."

### 7. Commit + atividade e preparação para a próxima aula (14:00 – 16:00)

**[CÓDIGO]**

```bash
git add processing/batch_spark.py
git commit -m "feat(processing): job batch em PySpark com broadcast join + equivalente DuckDB"
git push
```

> "A atividade proposta: rodar o job PySpark, usar o `.explain()` e **contar os Exchange** no plano — antes e depois do broadcast; e rodar o equivalente DuckDB com cronômetro, anotando a diferença. Sinta na pele o custo do overhead distribuído."

> "Na próxima aula, passaremos do processamento de um conjunto finito para o processamento contínuo de eventos. A demonstração simulará um produtor que publica pedidos e um consumidor que calcula contagens em janelas de um minuto. O resultado permitirá identificar o intervalo de maior volume no conjunto de dados."

---

## Roteiro da Videoaula 7 — "Streaming: os pedidos do Olist em tempo real"

**Duração-alvo:** 16 a 18 minutos.

### 1. Abertura (0:00 – 1:15)

**[TELA]** Slide de capa.

> "Até aqui, tratamos o Olist como ele é: 99 mil pedidos **parados** num CSV — e processamos em lote: roda, termina, entrega. Mas imagina esses pedidos chegando **agora**, um a um, no marketplace — e o gerente de operações querendo um painel de 'pedidos por minuto' e um alerta de fraude em tempo real. Há decisões que **não esperam o próximo lote**. Hoje entramos no **streaming**: a mensageria e o Kafka, tópicos, partições e offsets, janelas e garantias de entrega — e, claro, mão na massa: vamos **simular o stream do Olist** em Python e descobrir na demonstração qual foi o minuto mais movimentado da história do marketplace."

### 2. Batch × streaming: dois modelos mentais (1:15 – 3:15)

**[TELA]** Slide comparativo.

> "A diferença envolve o **modelo de processamento**, além da velocidade. No **batch**, o dado é **finito**: 'qual foi o faturamento de outubro de 2017?' — roda, termina, responde. No **streaming**, o dado é um **fluxo infinito**: registros chegam o tempo todo, e a pergunta vira 'quantos pedidos estão entrando **agora**, nos últimos 60 segundos?'. E o infinito traz desafios próprios: o dado **nunca acaba**; pode chegar **fora de ordem** — um pedido atrasado pela rede; e obriga a distinguir **tempo do evento** — quando a compra aconteceu, o `order_purchase_timestamp` — de **tempo de processamento** — quando o evento chegou ao consumidor. Essa distinção parece filosófica e é a causa dos bugs mais sutis do streaming."

### 3. Kafka: o log distribuído (3:15 – 6:00)

**[TELA]** Slide: produtor → tópico (partições/offsets) → consumidores.

> "No coração do streaming está a **mensageria**: um intermediário que **desacopla** produtor de consumidor — um não conhece o outro; ambos só conhecem o meio. Isso permite escalar os dois lados independentemente e absorver picos. E o padrão de fato é o **Apache Kafka**, nascido no LinkedIn em 2011. E atenção ao conceito, porque ele é mais profundo que 'fila': o Kafka é um **log distribuído e durável** — as mensagens **não somem quando lidas**; ficam gravadas por um período de retenção, e múltiplos consumidores leem o mesmo fluxo, cada um no seu ritmo. O painel lê agora; o reprocessamento lê do começo; ninguém atrapalha ninguém."

> "Três palavras técnicas para dominar. **Tópico**: a categoria nomeada de mensagens — o nosso será `olist.orders`. **Partição**: cada tópico se divide em partições, distribuídas entre os servidores e lidas **em paralelo** — é dali que vem a escalabilidade; e o Kafka garante ordem **apenas dentro de uma partição**. **Offset**: o número sequencial imutável de cada mensagem dentro da partição — o consumidor sabe 'já li até o offset tal', o que permite retomar após falha ou reprocessar do zero. E o truque de ouro: mensagens com a **mesma chave** caem sempre na **mesma partição** — usa `customer_id` como chave, e todos os pedidos daquele cliente ficam ordenados entre si."

### 4. Demonstração prática: o stream do Olist na demonstração (6:00 – 10:30)

**[TELA]** Editor + terminal.

> "O Olist é histórico — então nós vamos **simular**: um produtor lê os pedidos ordenados pelo timestamp de compra e os emite como **eventos JSON** num mock do tópico; um consumidor agrega em **janelas de 1 minuto**. E no fim, o script revela os minutos mais movimentados da história do marketplace."

**[CÓDIGO]** Criar `ingestion/stream_orders.py`:

```python
# produtor + consumidor (mock do topico olist.orders)
import duckdb, json
from collections import defaultdict
from datetime import datetime

con = duckdb.connect("olist.duckdb")
pedidos = con.execute("""
    SELECT order_id, customer_id, order_purchase_timestamp
    FROM raw.orders
    ORDER BY order_purchase_timestamp
""").fetchall()

contagem = defaultdict(int)

def consume(evento):                    # o "consumidor"
    e = json.loads(evento)
    ts = datetime.fromisoformat(e["ts"])
    janela = ts.replace(second=0, microsecond=0)   # tumbling de 60 s
    contagem[janela] += 1

def emit(topico, evento):               # mock: seria producer.send(topico, ...)
    consume(evento)                     # entrega direta ao consumidor

for order_id, customer_id, ts in pedidos:
    emit("olist.orders", json.dumps({
        "order_id": order_id, "customer_id": customer_id, "ts": str(ts)
    }))

print(f"eventos processados: {len(pedidos):,}")
print("\njanelas de 1 minuto mais movimentadas do Olist:")
top = sorted(contagem.items(), key=lambda kv: kv[1], reverse=True)[:10]
for janela, n in top:
    print(f"  {janela}  ->  {n} pedidos")
```

**[EXECUTAR]**

```bash
python ingestion/stream_orders.py
```

**[CHECKPOINT]**

> "99.441 eventos processados — e observe o ranking das janelas! Os minutos mais movimentados da história do Olist estão concentrados em. **24 de novembro de 2017**. Que dia foi esse? **A Black Friday!** Nós acabou de descobrir, com um stream simulado e uma janela tumbling, o pico histórico do marketplace — dezenas de pedidos num único minuto, contra uma média de 135 **por dia**. Observe na anatomia do código: o `emit` é o produtor — na vida real seria um `producer.send` do Kafka; o `consume` recebe o evento, trunca o timestamp no minuto — esse é o *bucket* da **janela tumbling** — e incrementa. Trinta linhas, e todos os conceitos do streaming estão aí dentro."

### 5. Janelas e garantias de entrega (10:30 – 13:00)

**[TELA]** Slide: tumbling × sliding × sessão; at-most/at-least/exactly-once.

> "Formalizando o que o código fez. Como agregar um fluxo que nunca termina? **Recortando-o no tempo, com janelas.** A **tumbling** — a nossa: blocos fixos e contíguos, sem sobreposição — cada evento cai em exatamente uma janela: 'pedidos por minuto'. A **sliding**: janela fixa que **desliza** — 'faturamento da última hora, recalculado a cada 5 minutos' — um evento pertence a várias. E a de **sessão**: fecha por inatividade — perfeita para navegação de usuário. E para os eventos **atrasados**, os motores de produção usam *watermarks* — marcas que decidem 'até quando espero um retardatário antes de fechar a janela'."

> "E se a rede falhar no meio? As **garantias de entrega**, em três níveis. **At-most-once**: pode perder, nunca duplica — barato, para métricas descartáveis. **At-least-once**: **nunca perde**, mas pode duplicar — o padrão prático. **Exactly-once**: o ideal platônico — sem perda nem duplicação — mas caro: exige produtores idempotentes e transações. E a regra de engenharia madura, guarda: **at-least-once mais consumo idempotente**. Observe ela de novo — a **idempotência** da Aula 5! Se o consumidor é idempotente, a duplicata do at-least-once é inofensiva: processar o mesmo pedido duas vezes dá no mesmo. A idempotência é o fio que costura esta disciplina."

> "E em produção de verdade, quem roda isso? Motores dedicados: o **Apache Flink** — *streaming-first*, latência de milissegundos, watermarks nativos — e o **Spark Structured Streaming** — o mesmo Spark da aula passada, em micro-batches de segundos. No projeto, mantemos o Spark no lote e o stream simulado — porque a regra é: **não pague o custo do streaming sem o negócio exigir tempo real**."

### 6. Kappa, e a conta das partições (13:00 – 15:00)

**[TELA]** Slide: Lambda × Kappa + a conta.

> "E como o stream conviveria com o batch que já temos? Duas arquiteturas. A **Lambda**: dois caminhos paralelos — o batch lento e completo, que é o nosso dbt, e um *speed layer* rápido e aproximado — reconciliados no fim. Funciona, mas é **duas bases de código**. A **Kappa** simplifica: **tudo é stream** — o histórico é apenas o log reprocessado do começo; lembra que o Kafka guarda tudo? Para o Olist, o caminho natural seria Kappa: o mesmo log `olist.orders` alimenta o painel na demonstração **e**, reprocessado, os marts. A estrela continua a mesma — muda só a forma de alimentá-la."

> "E a conta de capacidade: o Olist médio são 135 pedidos **por dia** — 0,0016 evento por segundo; **uma partição sobra** com folga cômica. Mas projeta a Black Friday que descobrimos na demonstração, mil vezes a média comprimida numa hora: 135 mil pedidos por hora — uns **37,5 eventos por segundo**. Se cada consumidor processa 10 por segundo: teto de 37,5 sobre 10 — **4 partições**, no mínimo. Grava: **o número de partições é o teto do paralelismo de consumo** — é uma das decisões de capacidade mais importantes do Kafka."

### 7. Pausa para reflexão + commit e preparação para a próxima aula (15:00 – 17:00)

**[TELA]** O desafio do painel + alerta de fraude.

> "**Pausa para reflexão** para você resolver em casa: o Olist virou marketplace na demonstração, e você precisa do painel 'pedidos por minuto', do 'faturamento da última hora' — e de um **alerta** quando um mesmo cliente faz **5 pedidos em 2 minutos**: suspeita de fraude. Pense: que **chave** de partição mantém os pedidos do cliente ordenados? Que **janela** detecta '5 em 2 minutos' — tumbling ou sliding? E que **garantia** você escolhe para o alerta — e por que **duplicar** um alerta de fraude é menos grave que **perder** um? Esboça a arquitetura num parágrafo e diz: Lambda ou Kappa?"

**[CÓDIGO]**

```bash
git add ingestion/stream_orders.py
git commit -m "feat(streaming): simulacao do stream olist.orders com janela tumbling de 1 min"
git push
```

> "E na próxima aula, a peça que falta — a que **amarra tudo**: quem garante que a ingestão roda antes do dbt, que o teste roda depois, que o retry dispara sozinho às 3 da manhã? A **orquestração**. Vamos subir o **Apache Airflow aqui dentro do Codespaces**, com a interface web naquela porta 8080 que deixamos configurada desde a Aula 1 — e montar o DAG `olist_pipeline` rodando ponta a ponta na tela. É a aula mais aguardada da unidade."

---

## Roteiro da Videoaula 8 — "Airflow no Codespaces: o olist_pipeline ponta a ponta"

**Duração-alvo:** 18 a 20 minutos.

### 1. Abertura (0:00 – 1:15)

**[TELA]** Slide de capa.

> "Nas aulas anteriores, executamos separadamente a ingestão, o processamento em lote e a simulação de streaming. Nesta aula, utilizaremos o Apache Airflow para representar dependências, agendamento, repetição após falhas e acompanhamento das execuções. O DAG `olist_pipeline` organizará as etapas de ingestão, transformação, teste e exportação da camada gold."

### 2. Por que orquestrar + o que é um DAG (1:15 – 3:30)

**[TELA]** Slide: o emaranhado de crons × o orquestrador; o grafo do olist_pipeline.

> "O problema que a orquestração resolve: no Olist, só se roda o dbt **depois** de ingerir; só se testa **depois** de transformar; só se exporta o gold **depois** de testar. Sem orquestrador, isso vira um emaranhado de crons frágeis — e a falha silenciosa clássica: o mart amanhece **vazio** e ninguém percebe até a diretoria abrir o dashboard. O **orquestrador** centraliza tudo: a **ordem**, o **agendamento**, os **retries**, os **logs** e a **recuperação**. E o Airflow — criado no Airbnb em 2014 — trouxe a filosofia que mudou o jogo: **pipeline como código**. O fluxo é descrito em **Python** — logo é versionado, revisado e testado como qualquer software."

> "E a estrutura central é o **DAG** — *Directed Acyclic Graph*: grafo **dirigido** — as setas têm sentido — e **acíclico** — nada depende de si mesmo; e a aciclicidade é o que **garante que o pipeline termina**. Cada nó é uma **task**, instância de um **operator**: o `PythonOperator` roda uma função Python; o `BashOperator`, um comando de shell; sensors esperam condições. O nosso DAG, você já conhece de tanto eu anunciar: `ingest_csv_to_duckdb >> dbt_run >> dbt_test >> export_gold`."

### 3. Demonstração prática: subindo o Airflow no Codespaces (3:30 – 6:30)

**[TELA]** Terminal (instalação feita antes de gravar; mostrar o comando e rodar o standalone na demonstração).

**[CÓDIGO]** Instalação (rodada antes da gravação — mostrar na tela):

```bash
pip install "apache-airflow==2.10.5" \
  --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.10.5/constraints-3.11.txt"
```

> "Um comentário sobre esse comando, porque ele tem uma sutileza importante: o Airflow tem **centenas de dependências**, e instalar sem o arquivo de **constraints** — que congela as versões testadas pela comunidade — é receita para conflito. Sempre, sempre instale Airflow com constraints. Eu rodei antes da gravação porque leva alguns minutos; agora vamos ligá-lo na demonstração:"

**[CÓDIGO]** Apontar o Airflow para a nossa pasta e subir tudo:

```bash
export AIRFLOW_HOME="$PWD/airflow"
export PIPELINE_HOME="$PWD"
airflow standalone
```

**[CHECKPOINT]**

> "O comando `airflow standalone` inicializa o banco de metadados, cria um usuário administrativo e inicia o servidor web na porta 8080. A senha inicial é apresentada no log e registrada em `airflow/standalone_admin_password.txt`. Como essa porta foi declarada em `forwardPorts` no devcontainer, o Codespaces permite abrir a interface no navegador. A variável `AIRFLOW_HOME` indica a pasta que contém o banco de metadados, os logs e o diretório `dags`."

### 4. Escrevendo o DAG olist_pipeline (6:30 – 10:30)

**[TELA]** Editor.

**[CÓDIGO]** Criar o script de exportação `ingestion/export_gold.py`:

```python
import duckdb, os

os.makedirs("data/gold", exist_ok=True)
con = duckdb.connect("olist.duckdb")
con.sql("""COPY (SELECT * FROM main.stg_orders)
           TO 'data/gold/orders_gold.parquet' (FORMAT PARQUET)""")
print("gold exportado: data/gold/orders_gold.parquet")
```

**[CÓDIGO]** Criar `airflow/dags/olist_pipeline.py`:

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
import pendulum, duckdb, os

BASE = os.environ.get("PIPELINE_HOME", "/workspaces/pipeline-olist")

def ingest_csv_to_duckdb():
    con = duckdb.connect(f"{BASE}/olist.duckdb")
    con.execute("CREATE SCHEMA IF NOT EXISTS raw")
    con.execute(f"""CREATE OR REPLACE TABLE raw.orders AS
                    SELECT * FROM read_csv_auto('{BASE}/data/raw/olist_orders_dataset.csv')""")

with DAG(
    dag_id="olist_pipeline",
    start_date=pendulum.datetime(2016, 9, 1, tz="UTC"),
    schedule="@daily",
    catchup=False,
    default_args={"retries": 2, "retry_delay": pendulum.duration(minutes=5)},
) as dag:

    ingest = PythonOperator(task_id="ingest_csv_to_duckdb",
                            python_callable=ingest_csv_to_duckdb)
    dbt_run  = BashOperator(task_id="dbt_run",
                            bash_command=f"cd {BASE}/dbt_olist && dbt run --profiles-dir .")
    dbt_test = BashOperator(task_id="dbt_test",
                            bash_command=f"cd {BASE}/dbt_olist && dbt test --profiles-dir .")
    export_gold = BashOperator(task_id="export_gold",
                            bash_command=f"cd {BASE} && python ingestion/export_gold.py")

    ingest >> dbt_run >> dbt_test >> export_gold
```

> "Vamos ler o DAG juntos, porque cada linha é uma decisão. O `BASE`: caminho absoluto do projeto — o Airflow executa as tasks fora da nossa pasta, então **nada de caminho relativo**; no Codespaces, o repositório vive em `/workspaces/pipeline-olist`. A função `ingest_csv_to_duckdb`: recria o `raw.orders` — observe, `CREATE OR REPLACE`, **idempotente**. No `DAG`: `schedule='@daily'` — roda todo dia; `catchup=False` — não sai executando o passado inteiro sozinho; e os `default_args` com **retries 2** e **5 minutos** de espera — resiliência automática contra falha transitória. As quatro tasks: um `PythonOperator` e três `BashOperator`. E a última linha é o pipeline inteiro numa expressão: `ingest >> dbt_run >> dbt_test >> export_gold`. E observe na ordem pedagógica: o **teste vem antes do export** — só publicamos o gold **se a qualidade passar**. Hoje o `dbt test` passa vazio, porque ainda não escrevemos testes — ele ganha dentes na Unidade 4. A vaga já está reservada no pipeline."

### 5. Rodando na interface: grafo, logs e o teste de falha (10:30 – 14:00)

**[TELA]** UI do Airflow no navegador.

> "Agora, a interface. O `olist_pipeline` apareceu na lista — o Airflow escaneia a pasta `dags/` sozinho. Ativo o DAG no botão, clico em **Trigger**. E vamos para a **Graph View**: observe o nosso grafo, os quatro nós, as setas — e as cores mudando na demonstração: verde-claro rodando. E verde-escuro, **success**, um por um, na ordem exata. Clico numa task, **Logs**: aqui está a saída real do `dbt run` — os três modelos, os OKs. Isso é **observabilidade**: eu não *acho* que o pipeline rodou — eu **vejo**."

> "E agora o teste que vale a aula: **vamos quebrar de propósito**. Edito a função de ingestão para apontar para um CSV que não existe — `olist_orders_INEXISTENTE.csv` — e disparo de novo. Observe a Graph View: o `ingest` ficou **amarelo** — *up_for_retry*: falhou, e o Airflow, sozinho, **agendou nova tentativa** em 5 minutos, porque dissemos `retries=2`. Ninguém foi acordado. Se fosse uma oscilação transitória, a segunda tentativa passaria e o pipeline seguiria. Como o erro é permanente, após as 2 tentativas ele marca **failed** — vermelho — e aí sim: alerta, e-mail, Slack. Conserto o caminho de volta. Re-disparo. Verde. Esse ciclo que você acabou de ver — falha, retry, recuperação, tudo visível — é o que separa um pipeline profissional de um script no cron."

### 6. Agendamento, backfill e a conta do SLA (14:00 – 16:30)

**[TELA]** Slide: data interval + a conta do SLA.

> "Três conceitos de operação para fechar. **Data interval**: cada execução do Airflow está ligada a um **período de dados** — a 'data lógica' — e não ao relógio de quando disparou. É isso que torna o reprocessamento determinístico: cada run *sabe* qual dia do Olist processa. **Backfill**: reexecutar o passado — `airflow dags backfill` num intervalo, e o Airflow roda uma execução por data lógica; quer popular o histórico 2016–2018 do Olist? Backfill. E o que torna o backfill **seguro**? A velha amiga **idempotência** da Aula 5: reprocessar um dia não duplica pedidos, porque o `unique_key` segura. Terceira vez que ela salva o dia — eu avisei que era a palavra da disciplina."

> "E o **SLA** — a conta que fecha a unidade. Nossos tempos médios: ingestão 4 minutos, dbt run 3, test 2, export 1 — caminho crítico normal: **10 minutos**. Pior caso, com todos os retries estourados: 4 mais 10 de retries, 3 mais 5, 2 mais 5, 1 mais 5 — **35 minutos**. Se os marts precisam estar prontos às **8h**, o DAG deve partir, no pior caso, até 7h25. Com margem: agenda **às 7h** — `0 7 * * *` — e configura **SLA de 35 minutos**: estourou, o Airflow alerta, e o time age **antes** de alguém abrir um dashboard vazio. Operação madura é isso: o pior caso calculado, não torcido."

### 7. Commit + atividade + encerramento da unidade (16:30 – 18:30)

**[CÓDIGO]**

```bash
git add airflow/dags/olist_pipeline.py ingestion/export_gold.py
git commit -m "feat(airflow): DAG olist_pipeline ponta a ponta (ingest >> dbt run >> test >> gold)"
git push
```

> "A atividade proposta: subir o Airflow no seu Codespace, criar o DAG com as quatro tasks e a ordem certa; **forçar a falha** no ingest e assistir ao retry na interface — errar de propósito é o melhor jeito de aprender operação; e rodar um backfill de 3 dias provando com o `count` do `stg_orders` que a idempotência impediu duplicação."

> "E observe o que você construiu na Unidade 2: a ingestão **ELT com dbt** e idempotência; o **lote** com a lente do Spark e a prática do DuckDB; o **stream simulado** que descobriu a Black Friday de 2017; e agora o **`olist_pipeline` orquestrado ponta a ponta**, com retry e SLA. O dado do Olist entra, é processado e está governado por um DAG. Na Unidade 3, paramos de **mover** e aprendemos a **guardar bem**: o data warehouse em camadas com dbt — staging, core, marts —, o SCD Tipo 2 com `dbt snapshot` no vendedor que muda de cidade, o lakehouse **Medallion** em Parquet, e como esse mesmo projeto rodaria no BigQuery ou Snowflake **trocando um único arquivo**."
