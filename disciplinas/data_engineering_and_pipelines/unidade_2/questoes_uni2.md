# Questionário — Unidade 2

- **Disciplina:** Data Engineering and Pipelines
- **Professor-conteudista:** Afonso Cesar Lelis Brandão

## Orientações

- **40 questões** padrão ENADE: **20 asserção-razão** + **20 de interpretação**.
- Cada questão tem **5 alternativas (a–e)**; a correta é prefixada por `*` (ex.: `*c. ...`).
- Distribuição da alternativa correta: rotação **a, b, c, d, e, a, b, c, d, e...** (8 questões para cada letra).

---

## Questões

### Questão 1 (Asserção-Razão)

> **Asserção I:** A carga incremental, que lê apenas os registros alterados desde a última execução usando uma coluna marcadora como `updated_at`, é muito mais rápida e impõe carga muito menor à fonte do que a carga full.
>
> **porque**
>
> **Razão II:** A carga full relê a tabela inteira a cada execução, de modo que seu tempo cresce proporcionalmente ao volume total acumulado, enquanto a incremental processa apenas o delta diário.

A respeito dessas asserções, assinale a opção correta:

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 2 (Asserção-Razão)

> **Asserção I:** No padrão ELT, o dado bruto é carregado primeiro no destino e transformado lá dentro, aproveitando o poder de processamento paralelo de data warehouses modernos como BigQuery e Snowflake.
>
> **porque**
>
> **Razão II:** O Apache Kafka é um log distribuído e durável em que as mensagens não são apagadas no momento da leitura, permanecendo gravadas durante o período de retenção configurado.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 3 (Asserção-Razão)

> **Asserção I:** No Apache Spark, transformações como `filter`, `select` e `groupBy` são lazy: elas apenas acrescentam um nó ao plano lógico e nada é executado até que uma ação como `count`, `collect` ou `show` seja chamada.
>
> **porque**
>
> **Razão II:** O `groupBy` é uma operação *narrow*, que mantém cada partição independente das demais e, portanto, nunca provoca shuffle ou tráfego de dados pela rede entre os executors.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 4 (Asserção-Razão)

> **Asserção I:** No Apache Kafka, o produtor define o offset de cada mensagem para escolher manualmente em qual broker ela será fisicamente gravada.
>
> **porque**
>
> **Razão II:** O Kafka garante a ordem das mensagens apenas dentro de uma mesma partição, e mensagens que carregam a mesma chave são sempre direcionadas para a mesma partição.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 5 (Asserção-Razão)

> **Asserção I:** A garantia de entrega *exactly-once* é a opção mais simples, barata e leve do Apache Kafka, devendo ser sempre escolhida por padrão por não acrescentar nenhum overhead em relação às demais.
>
> **porque**
>
> **Razão II:** No nível *at-least-once*, mensagens podem ser perdidas mas nunca duplicadas, o que torna desnecessário qualquer cuidado com idempotência no consumo.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

### Questão 6 (Asserção-Razão)

> **Asserção I:** O CDC (Change Data Capture) consegue capturar até mesmo registros deletados e atualizados quase em tempo real, sem martelar a tabela de produção com consultas repetidas.
>
> **porque**
>
> **Razão II:** O CDC lê diretamente o log de transações do banco de origem (como o binlog do MySQL ou o WAL do PostgreSQL), transformando cada `INSERT`, `UPDATE` e `DELETE` em evento sem precisar consultar a tabela a cada carga.

A respeito dessas asserções, assinale a opção correta:

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 7 (Asserção-Razão)

> **Asserção I:** No Apache Spark, o DataFrame é a abstração recomendada para a maioria dos engenheiros de dados porque passa pelo otimizador Catalyst e pelo motor Tungsten, que geram um plano físico eficiente.
>
> **porque**
>
> **Razão II:** O paradigma MapReduce, publicado pelo Google em 2004, propõe levar o código até onde os dados já estão, dividindo o trabalho nas fases de *map* (emite pares chave-valor) e *reduce* (agrupa por chave e combina).

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 8 (Asserção-Razão)

> **Asserção I:** No Apache Airflow, um pipeline é modelado como um DAG (grafo dirigido e acíclico), e a ausência de ciclos é justamente o que garante que a execução do pipeline termina.
>
> **porque**
>
> **Razão II:** No Airflow, cada task é necessariamente uma instância do `PythonOperator`, sendo impossível executar comandos de shell, queries SQL ou jobs Spark a partir de uma task.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 9 (Asserção-Razão)

> **Asserção I:** A idempotência só é relevante em sistemas de streaming com Kafka, sendo um conceito irrelevante para cargas de ingestão em batch e para o backfill de pipelines no Airflow.
>
> **porque**
>
> **Razão II:** Uma operação idempotente produz exatamente o mesmo estado final quando executada uma ou várias vezes, o que é justamente o que torna seguros os retries e o reprocessamento de períodos passados.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 10 (Asserção-Razão)

> **Asserção I:** O shuffle é a operação mais barata do Apache Spark, pois não envolve serialização, tráfego de rede nem escrita em disco, de modo que aumentar o número de operações *wide* sempre torna o job mais rápido.
>
> **porque**
>
> **Razão II:** Pela Lei de Amdahl, quanto maior a fração serial de um job, maior o ganho que se obtém simplesmente adicionando mais executors, sem qualquer limite teórico de aceleração.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

### Questão 11 (Interpretação)

**Estímulo:**

> "No ETL clássico você extrai, transforma num servidor no meio e só então carrega — limpa antes de tocar o destino. No ELT moderno você inverte: extrai, carrega o dado bruto na nuvem e transforma lá dentro, usando o poder do BigQuery, do Snowflake. O ELT ganhou porque armazenar ficou barato e os motores ficaram absurdamente paralelos — e você nunca perde a fonte da verdade."

A leitura mais alinhada ao texto é:

*a. O ELT carrega o dado bruto antes de transformá-lo no próprio destino, o que **preserva a fonte da verdade** e permite re-transformar quantas vezes for preciso sem reextrair — vantagem que cresceu com o barateamento do armazenamento e o paralelismo dos motores na nuvem.
b. No ELT a transformação ocorre obrigatoriamente em um servidor intermediário antes de o dado tocar o destino.
c. ETL e ELT são idênticos, diferindo apenas na ordem das letras da sigla, sem qualquer consequência arquitetural.
d. O ELT venceu porque o armazenamento ficou mais caro e os motores de consulta perderam capacidade de paralelismo.
e. No ELT, como o dado refinado já chega pronto ao destino, não é possível re-transformar o dado posteriormente.

### Questão 12 (Interpretação)

**Estímulo:**

> Uma tabela de pedidos cresce 2 milhões de linhas por dia e já acumula 730 milhões de registros após um ano. A uma taxa de leitura de 50.000 linhas/s, a carga full leva cerca de 4 h 3 min, enquanto a carga incremental, lendo apenas os 2 milhões de registros do dia, leva 40 segundos.

Considerando os conceitos da Unidade 2, qual leitura é **mais adequada**?

a. A carga full deve ser sempre preferida, pois ler a tabela inteira é mais barato do que ler apenas o delta diário.
*b. A carga incremental é cerca de **365 vezes mais rápida** e impõe carga desprezível à fonte; combiná-la com um reprocessamento full periódico (ou com CDC) oferece o melhor dos dois mundos em desempenho e completude.
c. As duas estratégias levam o mesmo tempo, pois ambas precisam varrer todos os 730 milhões de registros.
d. A carga incremental é mais lenta que a full porque precisa comparar cada linha com toda a tabela histórica.
e. A diferença de tempo entre full e incremental desaparece à medida que a tabela cresce, tornando-as equivalentes.

### Questão 13 (Interpretação)

**Estímulo:**

> Um job processa 1 TB de logs. Em uma única máquina (50 MB/s) levaria cerca de 5 h 33 min. Distribuído em 40 executors, o tempo *ideal* cairia para 8 min 20 s. Porém, supondo 15% de trabalho serial, a Lei de Amdahl limita o ganho a um fator de aproximadamente 5,8 — resultando em cerca de 57 minutos reais.

Que conclusão é **mais bem suportada** por esses dados?

a. Dobrar o número de executors sempre dobra a velocidade do job, sem qualquer limite.
b. A fração serial do job é irrelevante para o tempo total quando há muitos executors.
*c. O paralelismo tem **retorno decrescente**: a fração serial (em grande parte o shuffle) limita o ganho, de modo que **reduzir essa fração** costuma render mais do que simplesmente adicionar máquinas.
d. Como o tempo ideal seria de 8 min, basta confiar nesse valor e ignorar a parcela serial do trabalho.
e. A Lei de Amdahl prova que processamento distribuído nunca acelera um job em relação a uma máquina única.

### Questão 14 (Interpretação)

**Estímulo:**

> "Dentro de uma partição, cada mensagem recebe um número sequencial imutável: o offset. O Kafka garante ordem apenas dentro de uma partição, não entre partições. O consumidor controla até qual offset já leu, o que permite reprocessar do começo, retomar de onde parou após uma falha ou avançar para o presente."

A leitura correta desse trecho é:

a. O Kafka garante ordem total entre todas as partições de um tópico, independentemente da chave.
b. O offset é apagado quando a mensagem é lida, impedindo qualquer reprocessamento posterior.
c. O produtor é quem controla até qual offset o consumidor já leu.
*d. O offset é um índice sequencial **por partição** que dá ao consumidor flexibilidade para retomar após falha, reprocessar do início ou avançar — refletindo a garantia de ordem **dentro** de cada partição.
e. A ordem é garantida entre partições, mas não dentro de uma única partição.

### Questão 15 (Interpretação)

**Estímulo:**

> Um tópico de cliques recebe 30.000 mensagens por segundo, e cada consumidor de um grupo processa, em média, 5.000 mensagens por segundo. Lembre-se de que cada partição é lida por, no máximo, um consumidor do grupo.

Qual é o número mínimo de partições (e consumidores) necessário para acompanhar o fluxo **sem acumular atraso**?

a. 3 partições.
b. 4 partições.
c. 5 partições.
d. 12 partições.
*e. 6 partições, pois $30.000 / 5.000 = 6$ consumidores/partições; com menos partições o grupo não alcança a vazão de entrada e acumula *lag*.

### Questão 16 (Interpretação)

**Estímulo:**

> "Pipeline cai — é uma certeza, não uma possibilidade. A pergunta correta não é 'e se cair?', mas 'o que acontece quando eu rodar de novo?'. Se a resposta for 'duplica metade dos dados', você tem um problema."

A leitura mais alinhada ao texto é:

*a. Projetar a ingestão para ser **idempotente** — por exemplo com `MERGE`/upsert por chave de negócio ou sobrescrita de partição por janela — é o que permite ativar retries e reprocessar sem medo de duplicar dados.
b. Como pipelines nunca falham na prática, não é necessário pensar em reexecução nem em idempotência.
c. A melhor solução para falhas é desligar permanentemente qualquer mecanismo de retry do pipeline.
d. Duplicar metade dos dados a cada falha é um comportamento aceitável e esperado em pipelines bem projetados.
e. Idempotência significa garantir que o pipeline nunca seja executado mais de uma vez sob nenhuma circunstância.

### Questão 17 (Interpretação)

**Estímulo:**

> Você projeta um sistema **antifraude** de banco em que cada transação precisa ser avaliada em menos de 200 ms. Pergunte-se: perder uma transação de fraude é pior do que checá-la duas vezes?

Qual decisão de garantia de entrega é **mais adequada** a esse cenário?

a. Usar processamento em batch diário, pois a latência de horas é tolerável em antifraude.
*b. Adotar **at-least-once com consumo idempotente**, já que perder uma transação é pior do que processá-la em duplicidade — e a idempotência neutraliza eventuais duplicatas sem o custo de perseguir exactly-once.
c. Usar at-most-once, aceitando que algumas fraudes simplesmente não sejam avaliadas.
d. Eliminar qualquer garantia de entrega, pois em tempo real elas não se aplicam.
e. Migrar todo o fluxo para CDC em batch noturno, abandonando o streaming.

### Questão 18 (Interpretação)

**Estímulo:**

> No Apache Spark, operações *narrow* (como `filter` e `map`) mantêm cada partição independente, enquanto operações *wide* (como `groupBy`, `join` e `distinct`) exigem que dados com a mesma chave se encontrem na mesma partição, forçando um **shuffle**: redistribuição massiva de dados pela rede entre executors.

A leitura mais coerente com o texto é:

a. `filter` e `map` são as operações mais caras do Spark por sempre dispararem shuffle.
b. `groupBy` e `join` nunca redistribuem dados, pois operam dentro de cada partição isolada.
*c. O **shuffle**, provocado por operações *wide*, é a operação mais cara do Spark; otimizar Spark passa por **minimizá-lo** — filtrar antes de juntar, usar *broadcast join* quando um lado é pequeno e escolher bem as partições.
d. Aumentar o número de operações *wide* é a forma garantida de acelerar qualquer job Spark.
e. Operações *narrow* e *wide* têm exatamente o mesmo custo, pois ambas trafegam dados pela rede.

### Questão 19 (Interpretação)

**Estímulo:**

> Um pipeline diário deve entregar o dashboard executivo até as 8h00. O caminho crítico normal soma 80 min (25 + 40 + 15); no pior caso, com todos os retries acionados, sobe para 110 min (35 + 50 + 25).

Para garantir a entrega às 8h00 mesmo no pior caso, em que horário o DAG deve, no máximo, iniciar?

a. 07h40.
b. 06h40.
c. 06h20.
*d. 06h10, pois $08{:}00 - 110\ \text{min} = 06{:}10$; agenda-se às 6h00 com um SLA de 110 min para ter margem e alertar em caso de atraso.
e. 05h30.

### Questão 20 (Interpretação)

**Estímulo:**

> "Backfill reexecuta períodos passados — criou um DAG novo, quer popular o histórico? Backfill. E aqui a idempotência volta: reprocessar não pode duplicar. Como cada execução está atrelada a uma data lógica (data interval), o Airflow sabe exatamente qual janela de dados reprocessar."

A leitura mais alinhada ao texto é:

a. O backfill só funciona para datas futuras, nunca para períodos já passados.
b. O conceito de *data interval* (data lógica) é irrelevante para o reprocessamento determinístico.
c. O backfill duplica inevitavelmente os dados, sendo desaconselhado em qualquer pipeline.
d. A idempotência é dispensável no backfill, pois o Airflow impede sozinho qualquer duplicação.
*e. O backfill reexecuta janelas passadas de forma determinística graças à **data lógica** atrelada a cada execução, e é a **idempotência** (`MERGE`/upsert ou sobrescrita de partição) que torna esse reprocessamento seguro contra duplicação.

### Questão 21 (Asserção-Razão)

> **Asserção I:** Declarar um CSV pequeno e estável do Olist — como as ~71 traduções de categoria de produto — como um **seed** do dbt é preferível a montar uma ingestão incremental para ele.
>
> **porque**
>
> **Razão II:** O **seed** é um arquivo versionado junto do código, materializado por `dbt seed`, adequado a dados pequenos e raramente alterados, ao passo que a ingestão incremental existe para dados grandes que mudam com frequência.

A respeito dessas asserções, assinale a opção correta:

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 22 (Asserção-Razão)

> **Asserção I:** A camada **staging** (`stg_*`) do `dbt_olist` faz uma transformação 1:1 sobre cada fonte — renomeia colunas, casta tipos e limpa nulos — sem ainda executar joins ou agregações.
>
> **porque**
>
> **Razão II:** O **DuckDB** é um motor vetorizado *single-node* que resolve o join+agregação do Olist em segundos no laptop, sem exigir um cluster.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 23 (Asserção-Razão)

> **Asserção I:** No Spark, o **RDD** se reconstrói sozinho após a falha de um nó porque registra a sua **linhagem** (*lineage*) — a sequência de transformações que o gerou.
>
> **porque**
>
> **Razão II:** O **broadcast join** só é vantajoso quando **ambos** os lados da junção são tabelas grandes, pois replica a maior das duas por todos os executors para eliminar o shuffle.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 24 (Asserção-Razão)

> **Asserção I:** No Apache Spark, os **executors** são quem constrói o plano lógico do job e distribui as tarefas, enquanto o **driver** apenas armazena blocos de dados em disco.
>
> **porque**
>
> **Razão II:** O trabalho de um job Spark é fatiado em **tasks** (uma por partição), agrupadas em **stages** separados pelas fronteiras de shuffle, dentro de um mesmo **job**.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 25 (Asserção-Razão)

> **Asserção I:** No streaming, o **tempo de processamento** (quando o evento chega ao consumidor) é sempre idêntico ao **tempo do evento** (`order_purchase_timestamp`), de modo que dados nunca chegam fora de ordem e os *watermarks* são desnecessários.
>
> **porque**
>
> **Razão II:** A janela **tumbling** e a janela **sliding** são a mesma coisa: ambas produzem blocos fixos e contíguos em que cada evento pertence a exatamente uma janela.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

### Questão 26 (Asserção-Razão)

> **Asserção I:** O **Spark Structured Streaming** consegue reaproveitar a mesma API de DataFrames do processamento em lote porque trata o fluxo como uma sequência de **micro-batches**.
>
> **porque**
>
> **Razão II:** No Structured Streaming o stream é modelado como micro-lotes sucessivos, o que permite usar as mesmas transformações de DataFrame do batch, entregando latência da ordem de segundos (quase-tempo-real).

A respeito dessas asserções, assinale a opção correta:

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 27 (Asserção-Razão)

> **Asserção I:** Na arquitetura **Kappa**, todo o histórico do Olist pode ser reconstruído reprocessando o log `olist.orders` desde o começo, dispensando um caminho de batch separado só para o histórico.
>
> **porque**
>
> **Razão II:** O **Apache Airflow** popularizou a filosofia "pipelines como código", em que o fluxo é descrito em **Python** e, portanto, pode ser versionado, testado e revisado como qualquer software.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 28 (Asserção-Razão)

> **Asserção I:** No `olist_pipeline`, colocar o `dbt_test` **antes** do `export_gold` garante que os marts só são publicados se o dado passar nos testes de qualidade.
>
> **porque**
>
> **Razão II:** No Airflow, tarefas sem qualquer dependência de ordem entre si (ligadas por `>>`) são obrigatoriamente executadas de forma estritamente sequencial, uma após a outra, nunca em paralelo.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 29 (Asserção-Razão)

> **Asserção I:** O **Apache Flink** é a escolha adequada quando a latência de milissegundos é inegociável, mas por ser *streaming-first* ele é incapaz de lidar com janelas por tempo de evento ou com eventos que chegam atrasados.
>
> **porque**
>
> **Razão II:** No modelo **push** a fonte empurra o dado para o pipeline (como um webhook), enquanto no modelo **pull** o pipeline busca o dado na fonte (como a leitura agendada dos CSVs do Olist).

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 30 (Asserção-Razão)

> **Asserção I:** O **Hadoop** original era mais rápido que o Spark em pipelines iterativos porque gravava todos os resultados intermediários em disco entre uma etapa e outra do MapReduce.
>
> **porque**
>
> **Razão II:** No Airflow, o **data interval** (a data lógica de cada execução) é irrelevante para o reprocessamento, já que cada run sempre processa o dado do instante de relógio em que foi disparado, e não uma janela de dados fixa.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

### Questão 31 (Interpretação)

**Estímulo:**

> "Pros CSVs pequenos e estáveis, tipo a tabela de tradução das categorias de produto, eu nem monto ingestão: viram *seed*, um arquivo versionado no repositório que o `dbt seed` materializa como tabela. É a fundação de tudo que vem nas próximas unidades."

A leitura mais alinhada ao texto é:

*a. Um dado **pequeno, estável e versionável** — como as ~71 traduções de categoria do Olist — é melhor tratado como **seed** (arquivo no repositório materializado por `dbt seed`) do que como uma ingestão incremental completa.
b. O seed deve ser usado justamente para as tabelas **maiores e mais voláteis** do Olist, pois é a forma mais escalável de ingestão.
c. Um seed é carregado por um produtor Kafka em tempo real, evento a evento, no tópico `olist.orders`.
d. Declarar a tradução de categorias como seed obriga a reprocessar os 99 mil pedidos a cada `dbt run`.
e. O seed substitui a camada staging (`stg_*`), tornando desnecessário renomear colunas ou castar tipos.

### Questão 32 (Interpretação)

**Estímulo:**

> No Olist, um modelo `stg_orders` renomeia colunas, casta `order_purchase_timestamp` para `timestamp` e limpa nulos, **sem** fazer joins nem agregações. Só mais adiante, em outra camada, é que `stg_orders` será cruzado com `stg_order_items` e `stg_products` para calcular faturamento por categoria.

A leitura **mais coerente** com o papel dessa camada é:

a. A camada staging já deve conter todos os joins e agregações do faturamento, para poupar trabalho às camadas seguintes.
*b. A **staging** é uma camada **1:1** de limpeza e padronização (renomear, castar, tratar nulos); joins e agregações pertencem às **camadas seguintes**, mantendo cada etapa com responsabilidade única.
c. Como a staging não agrega, ela é dispensável e os CSVs crus poderiam ir direto para o mart.
d. Castar tipos e limpar nulos é uma tarefa exclusiva de streaming, não faz sentido numa camada de batch como a staging.
e. A staging deve materializar sempre uma **agregação** por categoria, nunca uma cópia 1:1 da fonte.

### Questão 33 (Interpretação)

**Estímulo:**

> No Spark, o trabalho de um job é dividido em **tasks** (uma por partição), agrupadas em **stages**; as fronteiras entre stages coincidem com os **shuffles**. No job do Olist, tanto o `join` por `product_id` quanto o `groupBy` por categoria são operações *wide*.

A conclusão **mais bem suportada** por esse trecho é:

a. Todo o job do Olist roda num único stage, pois `join` e `groupBy` são operações *narrow* que não quebram o pipeline.
b. Cada task processa o dataset inteiro do Olist, e o número de tasks independe do número de partições.
*c. Como cada operação *wide* introduz um **shuffle**, e cada shuffle marca uma **fronteira de stage**, um job com dois shuffles (`join` + `groupBy`) tende a se dividir em **mais de um stage** — e reduzir shuffles reduz stages.
d. O número de stages é fixo em um por job, independentemente de quantos shuffles existam.
e. As tasks de um mesmo stage precisam rodar sequencialmente, uma após a outra, nunca em paralelo.

### Questão 34 (Interpretação)

**Estímulo:**

> Você precisa de dois indicadores sobre o stream do Olist: (1) "pedidos por minuto", em blocos fixos e contíguos de 60 s em que cada pedido cai em exatamente uma janela; e (2) "faturamento da última 1 hora, recalculado a cada 5 minutos", em que um mesmo pedido pode ser contado em várias janelas.

A associação **correta** entre indicador e tipo de janela é:

a. (1) usa janela **sliding** e (2) usa janela **tumbling**.
b. Ambos usam janela **tumbling**, pois toda janela de tempo é fixa e sem sobreposição.
c. Ambos usam janela **de sessão**, definida por inatividade do cliente.
*d. (1) usa janela **tumbling** (blocos fixos, sem sobreposição, um evento por janela) e (2) usa janela **sliding** (janela fixa que avança e pode conter o mesmo evento em várias posições).
e. (1) usa janela **sliding** e (2) usa janela **de sessão**, pois nenhuma janela fixa recalcula a cada 5 min.

### Questão 35 (Interpretação)

**Estímulo:**

> "Janelas por tempo de evento e *watermarks* — que fecham a janela mesmo com um evento atrasado — vivem num motor dedicado: o **Flink**, streaming puro com latência de milissegundos, ou o **Spark Structured Streaming**, o mesmo Spark do lote rodando em micro-batches. No nosso projeto o Spark fica no lote e a gente simula o stream em Python."

A leitura **mais alinhada** ao texto é:

a. O produtor/consumidor Python do projeto é um motor de stream de produção, dispensando Flink ou Spark Structured Streaming em qualquer escala.
b. O Flink e o Spark Structured Streaming são idênticos: ambos são *streaming-first* com a mesma latência e a mesma API.
c. *Watermarks* servem para acelerar o batch do Olist, não têm relação com eventos atrasados no streaming.
d. O Spark só pode ser usado em streaming, jamais em processamento em lote.
*e. Em produção, **watermarks** e janelas por *event time* pedem um **motor dedicado** (Flink, *streaming-first* de latência baixíssima, ou Spark Structured Streaming em micro-batches); no projeto Olist, porém, o mock em Python só ilustra os conceitos e o Spark permanece no lote.

### Questão 36 (Interpretação)

**Estímulo:**

> Num job Spark, o **cluster manager** (YARN, Kubernetes ou standalone) negocia recursos, o **driver** hospeda o `SparkContext` e monta o plano, e os **executors** processam as tarefas e guardam dados em memória.

A leitura **correta** dessa divisão de papéis é:

*a. São **três papéis distintos**: o **cluster manager** aloca recursos, o **driver** planeja e coordena o job, e os **executors** executam as tasks e mantêm dados em memória.
b. O driver executa as tasks e o executor monta o plano; os papéis são intercambiáveis.
c. O cluster manager é quem processa os dados em memória, dispensando os executors.
d. Sem cluster manager é impossível existir driver, pois eles são o mesmo processo.
e. Os executors constroem o `SparkContext` e distribuem tarefas ao driver.

### Questão 37 (Interpretação)

**Estímulo:**

> No `olist_pipeline` configuramos `retries=2` com `retry_delay` (idealmente com *backoff exponencial*). A ideia é que uma falha **transitória** — o disco momentaneamente ocupado, uma leitura de CSV que oscilou — se resolva sozinha, sem acordar ninguém de plantão.

A leitura **mais adequada** desse trecho é:

a. Os retries servem para corrigir **erros de lógica** no código do pipeline, que se resolvem apenas repetindo a mesma execução.
*b. Os **retries com backoff** existem para absorver falhas **transitórias**, reexecutando a task automaticamente após um intervalo crescente — o que só é seguro porque a task é **idempotente** e não duplica dados ao rodar de novo.
c. Configurar `retries` faz o Airflow ignorar permanentemente qualquer falha, mesmo as definitivas, publicando o mart mesmo assim.
d. O `retry_delay` deve ser sempre zero, para que a task reexecute instantaneamente e sobrecarregue a fonte.
e. Retries só fazem sentido em streaming; num DAG de batch como o `olist_pipeline` eles não têm efeito.

### Questão 38 (Interpretação)

**Estímulo:**

> "Observabilidade é o que separa um pipeline que 'deveria estar funcionando' de um que você *sabe* que está." O Airflow oferece *grid view* colorido por status, logs por task, `email_on_failure`, *callbacks* para Slack e métricas para Prometheus/Grafana.

A leitura **mais coerente** com o texto é:

a. A observabilidade é um luxo dispensável: se o DAG tem retries, não é preciso monitorar nem alertar.
b. Logs e alertas substituem a necessidade de definir a ordem correta das tasks no DAG.
*c. **Monitoramento e alertas** (grid view, logs, `email_on_failure`, callbacks, métricas) dão **visibilidade proativa** do estado do pipeline, permitindo agir **antes** de alguém abrir um dashboard vazio.
d. O `email_on_failure` só dispara quando o pipeline termina com **sucesso**, servindo apenas como confirmação de entrega.
e. Métricas para Prometheus/Grafana são incompatíveis com o Airflow, que só expõe status pela linha de comando.

### Questão 39 (Interpretação)

**Estímulo:**

> "Na arquitetura **Kappa**: tudo é stream, e o histórico é só o log reprocessado. O mesmo `olist.orders` alimenta o painel ao vivo e, reprocessado, os marts. A **Lambda**, ao contrário, mantém *dois* caminhos — um batch lento e completo e um *speed layer* rápido e aproximado — e precisa reconciliá-los."

A distinção **correta** entre Lambda e Kappa, segundo o texto, é:

a. Na Kappa há dois caminhos (batch + speed layer) a reconciliar; na Lambda há um só, o stream.
b. Lambda e Kappa são sinônimos: ambas mantêm um único caminho de stream sem qualquer reconciliação.
c. A Kappa exige abandonar o log `olist.orders`, pois nela o histórico não pode ser reprocessado.
*d. A **Lambda** mantém **dois caminhos** (batch completo + speed layer aproximado) que precisam ser **reconciliados**; a **Kappa** simplifica para **um único log** reprocessável, do qual saem tanto a visão ao vivo quanto os marts.
e. Na Kappa o histórico é impossível de reconstruir, enquanto na Lambda o stream nunca é usado.

### Questão 40 (Interpretação)

**Estímulo:**

> No Olist ($99\,441$ pedidos, média de $\approx 135$ pedidos/dia), reprocessar **um dia** custa cerca de $99\,441/135 \approx 736$ vezes menos que recarregar a base inteira. O mesmo job de "faturamento por categoria" pode ser escrito em PySpark (`join` + `groupBy` + `sum`) ou no DuckDB (`JOIN ... USING (product_id)` + `GROUP BY`), com **a mesma lógica**.

A conclusão **mais bem suportada** por esses dados é:

a. A carga full de um dia é ~736 vezes mais barata que a incremental, então full deve ser sempre preferida.
b. PySpark e DuckDB produzem resultados diferentes para o faturamento por categoria, pois usam APIs distintas.
c. O fator ~736 prova que o DuckDB é incapaz de rodar o job do Olist e exige obrigatoriamente um cluster Spark.
d. Como o job é idêntico nas duas ferramentas, a diferença de custo entre carga full e incremental deixa de existir.
*e. A carga **incremental** de um dia é ~**736× mais barata** que a full, e o **mesmo join+agregação** roda tanto em PySpark quanto em DuckDB com a mesma lógica — o DuckDB resolve o Olist no laptop, e o Spark só se justifica quando o volume cresce ordens de grandeza.

---

## Feedbacks

### Questão 1

- **a.** *Correta!* Ambas verdadeiras e a II justifica a I. A carga incremental é de fato mais rápida e leve (Asserção I), e a Razão II explica diretamente **por quê**: a full relê todo o histórico acumulado (730 mi de linhas), com tempo proporcional ao volume total, enquanto a incremental processa só o delta do dia.
- **b.** Incorreta. A Razão **justifica** a Asserção — ela é a causa direta da diferença de desempenho.
- **c.** Incorreta. A Razão II é verdadeira.
- **d.** Incorreta. A Asserção I é verdadeira.
- **e.** Incorreta. Ambas são verdadeiras.

### Questão 2

- **a.** Incorreta. As duas são verdadeiras, mas a Razão não justifica a Asserção — tratam de assuntos distintos.
- **b.** *Correta!* As duas proposições são individualmente verdadeiras: o ELT realmente carrega o bruto e transforma no destino paralelo (BigQuery, Snowflake); e o Kafka é, de fato, um log durável cujas mensagens persistem pela retenção. Porém a Razão II (sobre Kafka) **não justifica** a definição de ELT (ingestão) — são temas independentes.
- **c.** Incorreta. A Razão II é verdadeira.
- **d.** Incorreta. A Asserção I é verdadeira.
- **e.** Incorreta. Ambas são verdadeiras.

### Questão 3

- **a.** Incorreta. A Razão II é falsa.
- **b.** Incorreta. A Razão II é falsa.
- **c.** *Correta!* A Asserção I é verdadeira: transformações no Spark são lazy e só uma ação dispara o DAG. A Razão II é falsa: `groupBy` é uma operação **wide**, não *narrow* — ela exige que chaves iguais se encontrem na mesma partição, provocando **shuffle** (tráfego de rede entre executors).
- **d.** Incorreta. A Asserção I é verdadeira.
- **e.** Incorreta. A Asserção I é verdadeira.

### Questão 4

- **a.** Incorreta. A Asserção I é falsa.
- **b.** Incorreta. A Asserção I é falsa.
- **c.** Incorreta. A Razão II é verdadeira.
- **d.** *Correta!* A Asserção I é falsa: o offset **não** é definido pelo produtor para escolher o broker — ele é atribuído pelo broker como índice sequencial **dentro** da partição; a partição-destino é determinada pela chave da mensagem. A Razão II descreve corretamente a garantia de ordem por partição e o roteamento por chave.
- **e.** Incorreta. A Razão II é verdadeira.

### Questão 5

- **a.** Incorreta. Ambas são falsas.
- **b.** Incorreta. Ambas são falsas.
- **c.** Incorreta. A Razão II também é falsa.
- **d.** Incorreta. A Asserção I também é falsa.
- **e.** *Correta!* Ambas são falsas. O *exactly-once* é o nível **mais difícil e custoso** (exige produtores idempotentes e transações, com overhead), não o mais simples e barato. E a Razão II inverte conceitos: é o **at-most-once** que pode perder e nunca duplica; o **at-least-once** nunca perde, mas pode duplicar — justamente por isso o **consumo idempotente** é essencial nele.

### Questão 6

- **a.** *Correta!* Ambas verdadeiras e a II justifica a I. O CDC realmente captura deletes/updates quase em tempo real sem onerar a produção (Asserção I), e a Razão II explica **por quê**: ele lê o log de transações (binlog/WAL) em vez de consultar a tabela a cada carga.
- **b.** Incorreta. A Razão justifica diretamente a Asserção.
- **c.** Incorreta. A Razão II é verdadeira.
- **d.** Incorreta. A Asserção I é verdadeira.
- **e.** Incorreta. Ambas são verdadeiras.

### Questão 7

- **a.** Incorreta. As duas são verdadeiras, mas a Razão não justifica a Asserção.
- **b.** *Correta!* As duas proposições são verdadeiras: o DataFrame é mesmo a abstração recomendada por passar pelo Catalyst/Tungsten (Asserção I); e o MapReduce de 2004 leva o código aos dados via *map* e *reduce* (Razão II). Porém a Razão (origem histórica do MapReduce) **não justifica** a recomendação do DataFrame — são fatos independentes.
- **c.** Incorreta. A Razão II é verdadeira.
- **d.** Incorreta. A Asserção I é verdadeira.
- **e.** Incorreta. Ambas são verdadeiras.

### Questão 8

- **a.** Incorreta. A Razão II é falsa.
- **b.** Incorreta. A Razão II é falsa.
- **c.** *Correta!* A Asserção I é verdadeira: o pipeline é um DAG e a aciclicidade garante que ele termina. A Razão II é falsa: uma task **não** precisa ser `PythonOperator` — o Airflow tem `BashOperator`, `SQLExecuteQueryOperator`, `SparkSubmitOperator`, sensors, entre outros.
- **d.** Incorreta. A Asserção I é verdadeira.
- **e.** Incorreta. A Asserção I é verdadeira.

### Questão 9

- **a.** Incorreta. A Asserção I é falsa.
- **b.** Incorreta. A Asserção I é falsa.
- **c.** Incorreta. A Razão II é verdadeira.
- **d.** *Correta!* A Asserção I é falsa: a idempotência é central também na ingestão em batch (`MERGE`/upsert, sobrescrita de partição) e no backfill do Airflow — não se restringe a streaming. A Razão II define corretamente idempotência e explica por que ela torna seguros retries e reprocessamento.
- **e.** Incorreta. A Razão II é verdadeira.

### Questão 10

- **a.** Incorreta. Ambas são falsas.
- **b.** Incorreta. Ambas são falsas.
- **c.** Incorreta. A Razão II também é falsa.
- **d.** Incorreta. A Asserção I também é falsa.
- **e.** *Correta!* Ambas são falsas. O shuffle é a operação **mais cara** do Spark (serialização, rede e disco), e multiplicar operações *wide* tende a tornar o job mais lento. A Razão II inverte a Lei de Amdahl: **quanto maior a fração serial, menor** o ganho com mais executors — há um teto de aceleração ($S_{max}$), e o retorno é decrescente.

### Questão 11

- **a.** *Correta!* O texto afirma exatamente isso: o ELT carrega o bruto e transforma no destino, preservando a fonte da verdade e permitindo re-transformar sem reextrair, vantagem amplificada pelo armazenamento barato e pelo paralelismo na nuvem.
- **b.** Incorreta. Transformar em servidor intermediário **antes** de tocar o destino é o ETL, não o ELT.
- **c.** Incorreta. A ordem das etapas muda a arquitetura inteira; não são idênticos.
- **d.** Incorreta. O texto diz o oposto: o armazenamento ficou **barato** e os motores **mais** paralelos.
- **e.** Incorreta. No ELT o bruto permanece no destino, permitindo re-transformar quantas vezes for preciso.

### Questão 12

- **a.** Incorreta. A full relê todo o histórico e é muito mais cara; a incremental lê só o delta.
- **b.** *Correta!* A incremental é ~365× mais rápida (40 s contra ~4 h 3 min) e quase não onera a fonte; combiná-la com full periódico ou CDC captura também atualizações retroativas — o melhor dos dois mundos.
- **c.** Incorreta. Só a full varre os 730 mi de registros; a incremental lê apenas 2 mi do dia.
- **d.** Incorreta. A incremental não compara cada linha com todo o histórico; usa um marcador (`updated_at`/cursor).
- **e.** Incorreta. Ao contrário: quanto mais a tabela cresce, **maior** a vantagem da incremental.

### Questão 13

- **a.** Incorreta. O paralelismo tem retorno decrescente; dobrar executors não dobra a velocidade.
- **b.** Incorreta. A fração serial é decisiva — 15% já limitam o ganho a ~5,8×.
- **c.** *Correta!* É a lição central do exemplo: pela Lei de Amdahl, o retorno é decrescente e a parcela serial (sobretudo o shuffle) trava o ganho; reduzir essa fração costuma render mais do que comprar máquinas.
- **d.** Incorreta. Ignorar a parcela serial leva a uma estimativa irreal (8 min vs ~57 min reais).
- **e.** Incorreta. O distribuído ainda acelera (de 5 h 33 min para ~57 min); apenas não atinge o ideal.

### Questão 14

- **a.** Incorreta. Não há ordem total entre partições — só dentro de cada uma.
- **b.** Incorreta. O offset não é apagado na leitura; o consumidor pode reprocessar do início.
- **c.** Incorreta. É o **consumidor** que controla o offset comprometido, não o produtor.
- **d.** *Correta!* O offset é o índice sequencial por partição que permite ao consumidor retomar, reprocessar ou avançar — refletindo a garantia de ordem **dentro** da partição.
- **e.** Incorreta. A ordem é garantida **dentro** de uma partição, não entre partições.

### Questão 15

- **a.** Incorreta. 3 partições dão 15.000 msg/s, abaixo das 30.000 de entrada.
- **b.** Incorreta. 4 partições dão 20.000 msg/s e acumulariam 10.000 msg/s de *lag*.
- **c.** Incorreta. 5 partições dão 25.000 msg/s, ainda insuficiente.
- **d.** Incorreta. 12 partições atendem com folga, mas o **mínimo** pedido é 6.
- **e.** *Correta!* $30.000 / 5.000 = 6$ consumidores/partições é o mínimo para igualar a vazão de entrada; com menos, o grupo não acompanha e acumula atraso.

### Questão 16

- **a.** *Correta!* O texto leva exatamente a essa conclusão: projetar para idempotência (`MERGE`/upsert por chave ou sobrescrita de partição) é o que permite reexecutar e ativar retries sem duplicar dados.
- **b.** Incorreta. O texto afirma que falhas são uma certeza — é preciso pensar em reexecução.
- **c.** Incorreta. A solução não é desligar retries, mas torná-los seguros via idempotência.
- **d.** Incorreta. Duplicar metade dos dados é justamente o pesadelo que se quer evitar.
- **e.** Incorreta. Idempotência não impede reexecução; garante o **mesmo estado final** ao reexecutar.

### Questão 17

- **a.** Incorreta. Batch é inviável: a avaliação precisa ocorrer em menos de 200 ms.
- **b.** *Correta!* Como perder uma transação é pior que checá-la duas vezes, escolhe-se at-least-once; o consumo idempotente absorve duplicatas, evitando o custo do exactly-once. É a recomendação prática da Aula 7.
- **c.** Incorreta. At-most-once pode **perder** transações — inaceitável em antifraude.
- **d.** Incorreta. Garantias de entrega são centrais em streaming, não dispensáveis.
- **e.** Incorreta. CDC em batch noturno não atende ao requisito de tempo real (<200 ms).

### Questão 18

- **a.** Incorreta. `filter` e `map` são *narrow* e **baratas**, não disparam shuffle.
- **b.** Incorreta. `groupBy` e `join` são *wide* e **provocam** shuffle.
- **c.** *Correta!* O shuffle, gerado por operações *wide*, é a operação mais cara; otimizar Spark é minimizá-lo — filtrar antes de juntar, *broadcast join* no lado pequeno e bom particionamento.
- **d.** Incorreta. Mais operações *wide* significam mais shuffle e, em geral, mais lentidão.
- **e.** Incorreta. *Narrow* e *wide* têm custos muito diferentes; só as *wide* trafegam dados pela rede.

### Questão 19

- **a.** Incorreta. 07h40 só cobriria 20 min, insuficiente para os 110 min do pior caso.
- **b.** Incorreta. 06h40 dá apenas 80 min (caminho crítico normal), sem margem para retries.
- **c.** Incorreta. 06h20 dá 100 min, ainda abaixo dos 110 min do pior caso.
- **d.** *Correta!* $08{:}00 - 110\ \text{min} = 06{:}10$ é o início máximo; na prática agenda-se às 6h00 com SLA de 110 min para ter margem e alertar atrasos.
- **e.** Incorreta. 05h30 funcionaria, mas não é o **limite máximo** de início pedido (06h10).

### Questão 20

- **a.** Incorreta. O backfill serve justamente para **períodos passados**.
- **b.** Incorreta. A *data lógica* (data interval) é o que torna o reprocessamento determinístico.
- **c.** Incorreta. O backfill não duplica **quando** a idempotência é respeitada — é recomendado, não desaconselhado.
- **d.** Incorreta. O Airflow não impede duplicação sozinho; é a idempotência do pipeline que garante isso.
- **e.** *Correta!* O backfill reexecuta janelas passadas de forma determinística por estarem atreladas à data lógica, e a idempotência (`MERGE`/upsert ou sobrescrita de partição) é o que torna esse reprocessamento seguro contra duplicação.

### Questão 21

- **a.** *Correta!* Ambas verdadeiras e a II justifica a I. Usar seed para as ~71 traduções de categoria é de fato preferível (Asserção I), e a Razão II explica **por quê**: o seed é um arquivo versionado, materializado por `dbt seed`, ideal para dados pequenos e estáveis, enquanto a ingestão incremental atende a dados grandes e voláteis.
- **b.** Incorreta. A Razão **justifica** a Asserção — ela dá o critério (pequeno e estável × grande e volátil) que motiva a escolha do seed.
- **c.** Incorreta. A Razão II é verdadeira.
- **d.** Incorreta. A Asserção I é verdadeira.
- **e.** Incorreta. Ambas são verdadeiras.

### Questão 22

- **a.** Incorreta. As duas são verdadeiras, mas a Razão não justifica a Asserção — tratam de assuntos distintos.
- **b.** *Correta!* As duas proposições são individualmente verdadeiras: a staging é mesmo uma camada 1:1 de renomear/castar/limpar sem joins (Asserção I); e o DuckDB é de fato um motor vetorizado *single-node* que resolve o Olist em segundos (Razão II). Porém a Razão (sobre o motor de execução) **não justifica** o papel da camada staging — são temas independentes.
- **c.** Incorreta. A Razão II é verdadeira.
- **d.** Incorreta. A Asserção I é verdadeira.
- **e.** Incorreta. Ambas são verdadeiras.

### Questão 23

- **a.** Incorreta. A Razão II é falsa.
- **b.** Incorreta. A Razão II é falsa.
- **c.** *Correta!* A Asserção I é verdadeira: o RDD registra sua **linhagem** e se reconstrói após falha. A Razão II é falsa: o **broadcast join** é vantajoso justamente quando **um** dos lados é **pequeno** (a `dim_products` do Olist, ~33 mil linhas) — replica-se o **lado pequeno** por todos os executors para eliminar o shuffle, não os dois lados grandes.
- **d.** Incorreta. A Asserção I é verdadeira.
- **e.** Incorreta. A Asserção I é verdadeira.

### Questão 24

- **a.** Incorreta. A Asserção I é falsa.
- **b.** Incorreta. A Asserção I é falsa.
- **c.** Incorreta. A Razão II é verdadeira.
- **d.** *Correta!* A Asserção I é falsa: ela **inverte os papéis** — é o **driver** que monta o plano e distribui tarefas, e os **executors** que processam e guardam dados em memória. A Razão II descreve corretamente a hierarquia de execução: tasks (uma por partição) → stages (separados por shuffle) → job.
- **e.** Incorreta. A Razão II é verdadeira.

### Questão 25

- **a.** Incorreta. Ambas são falsas.
- **b.** Incorreta. Ambas são falsas.
- **c.** Incorreta. A Razão II também é falsa.
- **d.** Incorreta. A Asserção I também é falsa.
- **e.** *Correta!* Ambas são falsas. Tempo de processamento e tempo de evento **não** coincidem — eventos chegam **fora de ordem** (atraso de rede), e é justamente por isso que existem *watermarks*. E a Razão II confunde os conceitos: a **tumbling** é fixa e sem sobreposição (um evento por janela), enquanto a **sliding** desliza e pode conter o mesmo evento em várias janelas — não são a mesma coisa.

### Questão 26

- **a.** *Correta!* Ambas verdadeiras e a II justifica a I. O Structured Streaming reaproveita a API de DataFrames (Asserção I), e a Razão II explica **por quê**: ele modela o stream como **micro-batches** sucessivos, o que permite as mesmas transformações do batch, com latência de segundos.
- **b.** Incorreta. A Razão **justifica** diretamente a Asserção — o micro-batch é a causa do reaproveitamento da API.
- **c.** Incorreta. A Razão II é verdadeira.
- **d.** Incorreta. A Asserção I é verdadeira.
- **e.** Incorreta. Ambas são verdadeiras.

### Questão 27

- **a.** Incorreta. As duas são verdadeiras, mas a Razão não justifica a Asserção.
- **b.** *Correta!* As duas proposições são verdadeiras: na Kappa o histórico do Olist é o log `olist.orders` reprocessado, sem batch separado (Asserção I); e o Airflow realmente popularizou "pipelines como código" em Python (Razão II). Porém a filosofia do Airflow **não justifica** a definição da arquitetura Kappa — são fatos independentes.
- **c.** Incorreta. A Razão II é verdadeira.
- **d.** Incorreta. A Asserção I é verdadeira.
- **e.** Incorreta. Ambas são verdadeiras.

### Questão 28

- **a.** Incorreta. A Razão II é falsa.
- **b.** Incorreta. A Razão II é falsa.
- **c.** *Correta!* A Asserção I é verdadeira: pôr `dbt_test` antes de `export_gold` garante que o mart só é publicado após passar nos testes. A Razão II é falsa: no Airflow, tarefas **sem** dependência entre si rodam **em paralelo** — a execução sequencial ocorre apenas quando há dependência explícita (`>>`).
- **d.** Incorreta. A Asserção I é verdadeira.
- **e.** Incorreta. A Asserção I é verdadeira.

### Questão 29

- **a.** Incorreta. A Asserção I é falsa.
- **b.** Incorreta. A Asserção I é falsa.
- **c.** Incorreta. A Razão II é verdadeira.
- **d.** *Correta!* A Asserção I é falsa: por ser *streaming-first*, o Flink é **exímio** em janelas por tempo de evento e no tratamento de eventos atrasados via **watermarks** — o contrário do afirmado. A Razão II define corretamente os modos **push** (fonte empurra, ex.: webhook) e **pull** (pipeline busca, ex.: leitura agendada dos CSVs do Olist).
- **e.** Incorreta. A Razão II é verdadeira.

### Questão 30

- **a.** Incorreta. Ambas são falsas.
- **b.** Incorreta. Ambas são falsas.
- **c.** Incorreta. A Razão II também é falsa.
- **d.** Incorreta. A Asserção I também é falsa.
- **e.** *Correta!* Ambas são falsas. Gravar intermediários em disco tornava o Hadoop **mais lento**, não mais rápido — o Spark superou-o justamente por manter intermediários **em memória**. E a Razão II inverte o conceito de **data interval**: ele é **central** para o reprocessamento determinístico, pois cada run está atrelada a uma **janela de dados** (data lógica), não ao instante de relógio do disparo.

### Questão 31

- **a.** *Correta!* O texto leva exatamente a isso: dados pequenos, estáveis e versionáveis (as ~71 traduções de categoria) viram **seed** — arquivo no repositório que o `dbt seed` materializa — em vez de uma ingestão incremental.
- **b.** Incorreta. O seed é para dados **pequenos e estáveis**, não para os maiores e mais voláteis.
- **c.** Incorreta. Seed é batch versionado no repositório, não um stream Kafka evento a evento.
- **d.** Incorreta. Um seed é independente da carga dos pedidos; não força reprocessar os 99 mil a cada `dbt run`.
- **e.** Incorreta. Seed e staging são coisas distintas; o seed não substitui a camada `stg_*` que renomeia e casta.

### Questão 32

- **a.** Incorreta. Joins e agregações **não** pertencem à staging; ela é uma cópia 1:1 limpa.
- **b.** *Correta!* A staging é a camada **1:1** de padronização (renomear, castar, limpar nulos); joins e agregações ficam nas **camadas seguintes**, mantendo responsabilidade única por etapa.
- **c.** Incorreta. A staging não é dispensável — é ela que garante nomes, tipos e nulos consistentes para o restante do pipeline.
- **d.** Incorreta. Castar tipos e limpar nulos é típico de batch; não é exclusivo de streaming.
- **e.** Incorreta. A staging materializa uma **cópia 1:1** da fonte, não uma agregação por categoria.

### Questão 33

- **a.** Incorreta. `join` e `groupBy` são operações *wide*, não *narrow* — elas **quebram** o pipeline em stages.
- **b.** Incorreta. Cada task processa **uma partição**, e o número de tasks acompanha o número de partições.
- **c.** *Correta!* Cada operação *wide* gera um **shuffle**, que marca uma **fronteira de stage**; com dois shuffles (`join` + `groupBy`), o job tende a ter **mais de um stage** — logo reduzir shuffles reduz stages e custo.
- **d.** Incorreta. O número de stages **não** é fixo em um; ele cresce com o número de shuffles.
- **e.** Incorreta. As tasks de um mesmo stage rodam **em paralelo**, uma por partição.

### Questão 34

- **a.** Incorreta. A associação está **trocada**: (1) é tumbling e (2) é sliding.
- **b.** Incorreta. (2) tem sobreposição (recalcula a cada 5 min sobre 1 h), logo **não** é tumbling.
- **c.** Incorreta. Nenhum dos dois é janela **de sessão** (definida por inatividade); são janelas de tempo fixas.
- **d.** *Correta!* (1) "pedidos por minuto" em blocos fixos sem sobreposição é **tumbling** (um evento por janela); (2) "última 1 h recalculada a cada 5 min" é **sliding** (janela fixa que avança e pode conter o mesmo evento em várias posições).
- **e.** Incorreta. (2) é sliding, não de sessão; e (1) é tumbling, não sliding.

### Questão 35

- **a.** Incorreta. O mock em Python **ilustra** conceitos, mas não sustenta um fluxo de produção em escala.
- **b.** Incorreta. Flink (*streaming-first*, milissegundos) e Spark Structured Streaming (micro-batches, segundos) **não** são idênticos.
- **c.** Incorreta. *Watermarks* lidam com **eventos atrasados no streaming**, não aceleram o batch.
- **d.** Incorreta. O Spark também faz **batch** (Aula 6); não é exclusivo de streaming.
- **e.** *Correta!* Em produção, watermarks e janelas por *event time* pedem um **motor dedicado** (Flink ou Spark Structured Streaming); no projeto Olist, o mock em Python só ilustra e o Spark fica no lote.

### Questão 36

- **a.** *Correta!* São três papéis distintos: **cluster manager** aloca recursos, **driver** planeja/coordena, **executors** executam as tasks e guardam dados em memória.
- **b.** Incorreta. Os papéis **não** são intercambiáveis: quem planeja é o driver, quem executa são os executors.
- **c.** Incorreta. O cluster manager **aloca** recursos; quem processa em memória são os executors.
- **d.** Incorreta. Driver e cluster manager são componentes **distintos**, não o mesmo processo.
- **e.** Incorreta. O `SparkContext` vive no **driver**, não nos executors.

### Questão 37

- **a.** Incorreta. Retries não corrigem **erros de lógica** — repetir a mesma execução falha de novo; eles servem a falhas **transitórias**.
- **b.** *Correta!* Retries com **backoff** absorvem falhas transitórias reexecutando a task após intervalos crescentes — algo **seguro** só porque a task é **idempotente** e reprocessar não duplica dados.
- **c.** Incorreta. Retries não ignoram falhas definitivas; após esgotá-los, a task falha e o mart **não** é publicado.
- **d.** Incorreta. `retry_delay` zero sobrecarrega a fonte; o ideal é um **backoff** crescente.
- **e.** Incorreta. Retries são plenamente úteis em batch — o `olist_pipeline` é justamente um DAG de batch.

### Questão 38

- **a.** Incorreta. Observabilidade **não** é dispensável: retries não avisam quando algo dá errado de forma persistente.
- **b.** Incorreta. Logs e alertas **não** substituem a definição da ordem (dependências) das tasks.
- **c.** *Correta!* Monitoramento e alertas (grid view, logs, `email_on_failure`, callbacks, métricas) dão **visibilidade proativa**, permitindo agir **antes** de alguém abrir um dashboard vazio.
- **d.** Incorreta. `email_on_failure` dispara em **falha**, não em sucesso.
- **e.** Incorreta. O Airflow **integra** Prometheus/Grafana; não é incompatível nem limitado à linha de comando.

### Questão 39

- **a.** Incorreta. Está **invertido**: são dois caminhos na **Lambda**, e um único log na **Kappa**.
- **b.** Incorreta. Lambda e Kappa **não** são sinônimos — diferem justamente no número de caminhos e na reconciliação.
- **c.** Incorreta. A Kappa **mantém** o log `olist.orders` reprocessável — é a base do seu histórico.
- **d.** *Correta!* A **Lambda** tem **dois caminhos** (batch completo + speed layer aproximado) a **reconciliar**; a **Kappa** usa **um único log** reprocessável que alimenta tanto a visão ao vivo quanto os marts.
- **e.** Incorreta. Na Kappa o histórico é reconstruível pelo log; e na Lambda o stream (speed layer) **é** usado.

### Questão 40

- **a.** Incorreta. Está invertido: é a **incremental** (não a full) que é ~736× mais barata para um dia.
- **b.** Incorreta. PySpark e DuckDB produzem o **mesmo** resultado — mesma lógica de join+agregação.
- **c.** Incorreta. O DuckDB **resolve** o Olist no laptop; o fator ~736 nada tem a ver com exigir cluster.
- **d.** Incorreta. A equivalência de ferramentas não anula a diferença de custo entre full e incremental — são dimensões distintas.
- **e.** *Correta!* A carga **incremental** de um dia é ~**736× mais barata** que a full, e o mesmo join+agregação roda em PySpark ou DuckDB com a mesma lógica — o DuckDB basta para o Olist, e o Spark só se justifica ao crescer ordens de grandeza.
