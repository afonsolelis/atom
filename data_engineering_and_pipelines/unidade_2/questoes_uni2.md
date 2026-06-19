# Questionário — Unidade 2

- **Disciplina:** Data Engineering and Pipelines
- **Professor-conteudista:** Afonso Cesar Lelis Brandão

## Orientações

- **20 questões** padrão ENADE: **10 asserção-razão** + **10 de interpretação**.
- Cada questão tem **5 alternativas (a–e)**; a correta é prefixada por `*` (ex.: `*c. ...`).
- Distribuição da alternativa correta: rotação **a, b, c, d, e, a, b, c, d, e...** (4 questões para cada letra).

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
