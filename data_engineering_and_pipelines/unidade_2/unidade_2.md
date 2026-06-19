# Unidade 2 — Ingestão e Processamento de Dados

- **Disciplina:** Data Engineering and Pipelines
- **Conteudista:** Afonso Cesar Lelis Brandão
- **Videoaulas desta unidade:** 5 a 8

> **Recap da Unidade 1:** entendemos o que faz um engenheiro de dados, conhecemos o ciclo de vida da engenharia de dados (geração → ingestão → transformação → servir), discutimos batch vs streaming como filosofias de processamento e abrimos os formatos de armazenamento (CSV, JSON, Parquet) e a ideia de data lake/lakehouse. Agora vamos colocar os dados **em movimento**: nesta unidade você aprende a **ingerir** dados de fontes diversas (Aula 5), processá-los em grandes volumes com **Apache Spark** (Aula 6), tratá-los em **tempo real** com **Apache Kafka** (Aula 7) e **orquestrar** tudo isso com **Apache Airflow** (Aula 8).

---

## Aula 5 — ETL vs ELT: a ingestão de dados

Todo pipeline de dados começa com a mesma pergunta: como trago o dado de onde ele nasce para onde eu consigo trabalhar com ele? Essa etapa, a **ingestão**, é onde mais pipelines quebram na vida real — fontes mudam, registros chegam duplicados, a rede cai no meio de uma carga. Nesta aula você vai entender as duas grandes filosofias de movimentação de dados (**ETL** e **ELT**), a diferença entre carregar tudo (**batch full**) e só o que mudou (**incremental/CDC**), e por que a palavra **idempotência** vai te salvar muitas madrugadas.

### O que é ingestão de dados

**Ingestão** é o ato de mover dados de uma ou mais **fontes** (sistemas operacionais, APIs, arquivos, bancos transacionais, filas de mensagens) para um **destino** onde serão armazenados e processados (um data warehouse, um data lake, um lakehouse). É a primeira fronteira do pipeline e, portanto, o ponto onde a qualidade dos dados é mais frágil.

A ingestão pode ser **push** (a fonte empurra os dados, como um webhook) ou **pull** (o pipeline busca os dados, como uma consulta agendada). Pode ser **batch** (lotes em janelas periódicas) ou **streaming** (registro a registro, contínuo). E carrega consigo decisões de schema: o dado chega estruturado, semiestruturado ou bruto? Validamos na entrada (*schema-on-write*) ou só na leitura (*schema-on-read*)?

![Logo do Apache Airflow, ferramenta de orquestração frequentemente usada para coordenar tarefas de ingestão de dados](https://commons.wikimedia.org/wiki/Special:FilePath/AirflowLogo.png)

### ETL clássico

**ETL** significa **Extract, Transform, Load** — extrair, transformar e **só então** carregar. A transformação acontece em um servidor intermediário (historicamente uma ferramenta como Informatica, Talend ou Pentaho) **antes** de o dado tocar o destino final.

A lógica do ETL nasceu numa época em que armazenamento e processamento eram caros: limpava-se, agregava-se e modelava-se o dado *fora* do warehouse, e só o resultado refinado era carregado. Vantagens: o dado entra no destino já limpo e conforme regras de qualidade e governança (útil quando há dados sensíveis que não podem ser armazenados em bruto). Desvantagens: a transformação vira um gargalo, exige infraestrutura própria, e se você descobre depois que precisa de um campo que descartou, tem de reprocessar da fonte.

### ELT moderno

**ELT** inverte a ordem: **Extract, Load, Transform** — extrai, **carrega o dado bruto** no destino e transforma *lá dentro*, usando o poder de processamento do próprio data warehouse moderno (BigQuery, Snowflake, Redshift) ou do lakehouse. A transformação vira SQL/código executado pelo motor de destino, frequentemente orquestrado por ferramentas como o **dbt**.

O ELT venceu nos últimos anos porque armazenamento ficou barato e os motores de consulta ficaram absurdamente paralelos. Carregar o dado bruto primeiro significa que você **guarda a fonte da verdade** e pode re-transformar quantas vezes quiser sem reextrair. A contrapartida: você precisa de um destino potente e de governança sobre dados crus que ficam ali expostos.

| Aspecto | ETL | ELT |
| --- | --- | --- |
| **Onde transforma** | Servidor intermediário | Dentro do destino |
| **O que chega ao destino** | Dado já refinado | Dado bruto + transformações |
| **Reprocessar** | Reextrai da fonte | Re-roda transformação |
| **Melhor para** | Dados sensíveis, regras na entrada | Nuvem, grande volume, flexibilidade |

### Batch vs incremental (CDC)

Independentemente de ETL ou ELT, a extração tem dois modos. **Carga full (batch completo):** lê a tabela inteira toda vez — simples, mas caro e lento conforme os dados crescem. **Carga incremental:** lê apenas o que mudou desde a última execução, usando uma coluna marcadora (por exemplo `updated_at > último_carregado`).

Quando até as linhas *deletadas* e *atualizadas* precisam ser capturadas com precisão, usa-se **CDC (Change Data Capture)**: a técnica de ler o **log de transações** do banco de origem (o *binlog* do MySQL, o WAL do PostgreSQL) e replicar cada `INSERT`, `UPDATE` e `DELETE` quase em tempo real. Ferramentas como **Debezium** transformam esse log em eventos que viajam, por exemplo, pelo Kafka. O CDC é o casamento perfeito entre ingestão incremental e baixo impacto na fonte, pois não consulta a tabela de produção a cada carga.

### Idempotência e reprocessamento

Pipelines falham — é uma certeza, não uma possibilidade. A pergunta correta não é "e se cair?", mas "o que acontece quando eu rodar de novo?". Uma operação é **idempotente** quando executá-la duas (ou dez) vezes produz exatamente o mesmo estado final que executá-la uma vez.

Em ingestão, idempotência costuma ser obtida com uma **chave natural ou de negócio** e um `MERGE`/*upsert* (insere se não existe, atualiza se já existe) em vez de `INSERT` cego, ou com **partições sobrescritas por janela** (reprocessar o dia 2026-06-18 sempre apaga e regrava aquela partição inteira). O oposto é o pesadelo: um job que cai após inserir metade das linhas e, ao reiniciar, duplica essa metade. Projetar para idempotência é o que permite ativar **retries** com tranquilidade — assunto que volta na Aula 8 com o Airflow.

### Exemplo numérico: janela de carga

Uma tabela de pedidos cresce $2$ milhões de linhas por dia. A carga **full** lê toda a tabela, que já acumula $730$ milhões de registros após um ano. A uma taxa de leitura de $50.000$ linhas/s, a carga full leva:

$$
t_{full} = \frac{730.000.000}{50.000} = 14.600\ \text{s} \approx 4\ \text{h}\ 3\ \text{min}
$$

Já a carga **incremental** lê apenas as linhas do dia. Com os mesmos $2$ milhões de registros novos:

$$
t_{inc} = \frac{2.000.000}{50.000} = 40\ \text{s}
$$

A carga incremental é cerca de $365$ vezes mais rápida e, além disso, impõe carga desprezível na fonte. Mesmo que ela "perca" eventuais atualizações retroativas, basta combinar incremental diária com um reprocessamento **full mensal** (ou usar CDC) para ter o melhor dos dois mundos.

### Atividade prática

Escolha uma fonte de dados pública com endpoint paginado (por exemplo a API do IBGE de localidades ou a API pública do GitHub).

1. Implemente uma extração **full** que baixe todos os registros e grave em Parquet.
2. Adicione um marcador (`updated_at` ou um número de página/cursor persistido) e converta a carga para **incremental**.
3. Garanta **idempotência**: rode a ingestão duas vezes seguidas e prove (contando linhas) que não houve duplicação — use `MERGE` por chave ou sobrescrita de partição.
4. Documente em três linhas: ETL ou ELT? Por quê?

### Pontos-chave

- **Ingestão** é a primeira e mais frágil etapa do pipeline; pode ser push/pull e batch/streaming.
- **ETL** transforma antes de carregar; **ELT** carrega o bruto e transforma no destino — o ELT domina na nuvem.
- **Carga incremental** lê só o que mudou; **CDC** lê o log de transações para capturar até deletes em quase tempo real.
- **Idempotência** (`MERGE`/upsert, sobrescrita de partição) é o que torna **retry** e reprocessamento seguros.
- A escolha não é dogmática — depende de volume, sensibilidade do dado e poder do destino.

### Para saber mais

- **Reis, J.; Housley, M.** *Fundamentals of Data Engineering*. O'Reilly, 2022 — capítulo sobre ingestão.
- **Documentação do Debezium (CDC):** https://debezium.io/documentation/
- **dbt — transformação no padrão ELT:** https://docs.getdbt.com/docs/introduction

## Aula 5 — Roteiro da Videoaula 5: "ETL vs ELT: a ingestão de dados"

**Duração:** 9 a 11 minutos.

### 1. Abertura (0:00 – 0:40)

> "Todo pipeline começa com a mesma dor: como eu trago o dado de onde ele nasce para onde eu consigo trabalhar? Hoje vamos resolver isso de verdade — ETL, ELT, carga incremental, CDC e uma palavra que vai te salvar de noites mal dormidas: idempotência."

### 2. Desenvolvimento — parte 1 (0:40 – 4:00)

> "Ingestão é mover dado da fonte para o destino. Pode ser push, quando a fonte empurra, ou pull, quando a gente busca. E aqui surge a grande bifurcação: ETL e ELT. No ETL clássico você extrai, transforma num servidor no meio e só então carrega — limpa antes de tocar o destino. No ELT moderno você inverte: extrai, carrega o dado bruto na nuvem e transforma lá dentro, usando o poder do BigQuery, do Snowflake. O ELT ganhou porque armazenar ficou barato e os motores ficaram absurdamente paralelos — e você nunca perde a fonte da verdade."

### 3. Desenvolvimento — parte 2 (4:00 – 7:00)

> "Agora, como eu extraio? Carga full lê a tabela inteira toda vez. Funciona com pouco dato, mas vira um monstro de horas quando a tabela cresce. Carga incremental lê só o que mudou desde a última vez, olhando um campo updated_at. E quando eu preciso capturar até o que foi deletado, sem martelar o banco de produção? CDC — Change Data Capture — que lê o próprio log de transações do banco, o binlog, e transforma cada insert, update e delete em evento. Debezium faz isso e joga no Kafka."

### 4. Desenvolvimento — parte 3 (7:00 – 9:00)

> "Vou repetir uma verdade dura: pipeline cai. A pergunta certa é: o que acontece quando eu rodar de novo? Se a resposta for 'duplica metade dos dados', você tem um problema. Idempotência é a propriedade de rodar duas, dez vezes, e terminar sempre no mesmo estado. A gente consegue isso com MERGE por chave de negócio, ou sobrescrevendo a partição inteira do dia. É isso que permite ligar retry automático sem medo."

### 5. Encerramento (9:00 – 11:00)

> "Na conta que fiz, a carga incremental foi 365 vezes mais rápida que a full — 40 segundos contra mais de 4 horas. Guarde o tripé: ELT como filosofia, incremental ou CDC como técnica, idempotência como rede de segurança. Na próxima aula, depois que o dado entrou, vamos processá-lo em grande escala com o Apache Spark. Te espero!"

---

## Aula 6 — Processamento em lote com Apache Spark

O dado entrou — e agora? Quando são gigabytes ou terabytes, uma única máquina não dá conta de transformar tudo em tempo hábil. É aqui que entra o **processamento distribuído em lote**, e seu nome mais importante hoje é **Apache Spark**. Nesta aula você vai entender a ideia fundadora (**MapReduce**), como o Spark organiza um cluster (**driver e executors**), suas abstrações de dados (**RDD, DataFrame, Dataset**), por que ele é **lazy** e qual é a operação que mais custa caro: o **shuffle**.

### O paradigma MapReduce

A revolução começou em 2004, quando o Google publicou o paper do **MapReduce**: em vez de levar os dados até um supercomputador, leve o **código** até onde os dados já estão, em milhares de máquinas baratas. O modelo tem duas fases. No **map**, cada nó aplica uma função a um pedaço dos dados, produzindo pares chave-valor. No **reduce**, os pares com a mesma chave são agrupados e combinados num resultado.

O exemplo canônico é o *word count*: o map emite `(palavra, 1)` para cada palavra de um texto; o reduce soma os valores por palavra. O Hadoop popularizou esse modelo, mas tinha um custo brutal: gravava resultados intermediários em disco entre cada etapa. O Spark nasceu para resolver exatamente isso.

![Logo do Apache Spark, motor de processamento distribuído em memória para grandes volumes de dados](https://commons.wikimedia.org/wiki/Special:FilePath/Apache_Spark_logo.svg)

### Arquitetura do Spark (driver e executors)

Um job Spark roda num **cluster** com papéis bem definidos. O **driver** é o cérebro: hospeda o `SparkContext`, constrói o plano de execução (o DAG de operações) e distribui tarefas. Os **executors** são os músculos: processos espalhados pelos nós que executam as tarefas e guardam dados em memória. Um **cluster manager** (YARN, Kubernetes ou o standalone do Spark) negocia os recursos.

O trabalho é fatiado em **tasks** (uma por partição), agrupadas em **stages**, agrupados num **job**. O grande salto do Spark sobre o Hadoop é manter os dados intermediários **em memória** entre os stages sempre que possível, em vez de cuspir tudo no disco — o que rende ganhos de ordens de grandeza em pipelines com várias etapas iterativas.

### RDD, DataFrame e Dataset

O Spark oferece três abstrações de dados, em ordem crescente de comodidade:

- **RDD (Resilient Distributed Dataset):** a coleção distribuída original, de baixo nível. Resiliente porque registra sua linhagem (*lineage*) e sabe se reconstruir após falha de um nó. Poderoso, mas verboso e sem otimização automática.
- **DataFrame:** dados organizados em colunas nomeadas, como uma tabela. É a abstração mais usada porque passa pelo otimizador **Catalyst** e pelo motor de execução **Tungsten**, que geram um plano físico eficiente. API disponível em Python (PySpark), Scala, Java e R.
- **Dataset:** DataFrame com tipagem forte em tempo de compilação (Scala/Java). Combina segurança de tipos com as otimizações do Catalyst.

Para a maioria dos engenheiros de dados, o **DataFrame** é o ponto de partida: legível, otimizado e portável entre linguagens.

### Transformações e ações (avaliação lazy)

O Spark separa operações em **transformações** (`filter`, `select`, `groupBy`, `join`, `map`) e **ações** (`count`, `collect`, `write`, `show`). A chave é que **transformações são lazy**: elas não executam nada — apenas acrescentam um nó ao plano lógico. Só quando uma **ação** é chamada o Spark monta o DAG, deixa o Catalyst otimizá-lo (reordenando filtros, eliminando colunas não usadas) e dispara a execução.

Essa preguiça é uma virtude: ela permite que o motor enxergue o pipeline inteiro antes de rodar e tome decisões globais. O preço é didático — iniciantes se assustam quando um `filter` "não faz nada" até chamarem um `show`.

### Particionamento e shuffle

Os dados de um RDD/DataFrame vivem repartidos em **partições**, processadas em paralelo. Operações *narrow* (como `filter` e `map`) mantêm cada partição independente — rápidas. Já operações *wide* (como `groupBy`, `join` e `distinct`) exigem que dados com a mesma chave se encontrem na mesma partição, forçando um **shuffle**: redistribuição massiva de dados pela rede entre executors.

O **shuffle é a operação mais cara** do Spark — envolve serialização, tráfego de rede e escrita em disco. Otimizar Spark é, em grande parte, **minimizar e domar shuffles**: filtrar antes de juntar, usar *broadcast join* quando um lado é pequeno, escolher um número de partições adequado e particionar fisicamente os dados pela chave mais frequente de junção.

### Exemplo numérico: paralelismo e tempo de job

Um job processa $1\ \text{TB}$ de logs. Numa única máquina capaz de processar $50\ \text{MB/s}$, o tempo seria:

$$
t_1 = \frac{1.000.000\ \text{MB}}{50\ \text{MB/s}} = 20.000\ \text{s} \approx 5\ \text{h}\ 33\ \text{min}
$$

Distribuindo em um cluster com $40$ executors de mesma capacidade, o tempo *ideal* cai para:

$$
t_{40} = \frac{20.000}{40} = 500\ \text{s} \approx 8\ \text{min}\ 20\ \text{s}
$$

Mas o paralelismo não é perfeito. Suponha que $15\%$ do trabalho seja serial (coleta de resultados, shuffle final). Pela **Lei de Amdahl**, o ganho máximo é limitado:

$$
S_{max} = \frac{1}{0{,}15 + \frac{0{,}85}{40}} = \frac{1}{0{,}15 + 0{,}02125} \approx 5{,}8
$$

Ou seja, o tempo real fica em torno de $20.000 / 5{,}8 \approx 3.448\ \text{s} \approx 57$ min — bem acima dos $8$ min ideais. A lição: adicionar executors tem retorno decrescente, e reduzir a fração serial (o shuffle!) frequentemente rende mais que comprar mais máquinas.

### Atividade prática

Instale o PySpark localmente (`pip install pyspark`) ou use um notebook no Databricks Community Edition.

1. Carregue um arquivo CSV ou Parquet grande (use um dataset público, como *NYC Taxi*) em um **DataFrame**.
2. Encadeie transformações (`filter`, `groupBy`, `agg`) e observe que **nada roda** até você chamar `.show()` ou `.count()`.
3. Use `.explain()` para ver o plano físico e **identifique onde ocorre o shuffle** (`Exchange`).
4. Reescreva uma junção usando `broadcast()` no lado pequeno e compare o plano. Anote o que mudou.

### Pontos-chave

- O **MapReduce** levou o código até os dados; o **Spark** o aprimorou mantendo intermediários **em memória**.
- A arquitetura é **driver** (planeja) + **executors** (executam) + **cluster manager** (aloca recursos).
- **DataFrame** é a abstração padrão — otimizada pelo Catalyst; **RDD** é de baixo nível; **Dataset** é tipado.
- Transformações são **lazy**; só uma **ação** dispara a execução do DAG.
- O **shuffle** (operações wide) é o maior custo — otimizar Spark é minimizar shuffle, não só somar máquinas.

### Para saber mais

- **Chambers, B.; Zaharia, M.** *Spark: The Definitive Guide*. O'Reilly, 2018.
- **Documentação oficial do Apache Spark:** https://spark.apache.org/docs/latest/
- **Guia de tuning de performance do Spark:** https://spark.apache.org/docs/latest/sql-performance-tuning.html

## Aula 6 — Roteiro da Videoaula 6: "Processamento em lote com Apache Spark"

**Duração:** 9 a 11 minutos.

### 1. Abertura (0:00 – 0:40)

> "O dado entrou. Mas e quando são terabytes? Uma máquina só não dá conta. Hoje você vai conhecer o motor que move o mundo da engenharia de dados em lote: o Apache Spark. E vai entender por que ele é tão mais rápido que o velho Hadoop."

### 2. Desenvolvimento — parte 1 (0:40 – 4:00)

> "Tudo começa em 2004, com o paper do MapReduce, do Google. A ideia genial: em vez de levar terabytes até um supercomputador, leve o código até onde os dados já estão, em milhares de máquinas baratas. Map aplica uma função e emite chave-valor; reduce agrupa por chave e combina. O Hadoop popularizou isso, mas gravava tudo em disco entre cada etapa — lento. O Spark chegou e disse: e se eu mantiver os intermediários em memória? Daí o salto de performance."

### 3. Desenvolvimento — parte 2 (4:00 – 7:00)

> "Como o Spark se organiza? Tem o driver, o cérebro, que monta o plano e distribui tarefas; e os executors, os músculos, que processam e guardam dados em memória. O trabalho vira task, stage, job. E você fala com ele por três abstrações: RDD, o nível baixo e resiliente; DataFrame, a tabela com colunas que passa pelo otimizador Catalyst — é o que você vai usar 90% do tempo; e Dataset, o DataFrame tipado. Comece pelo DataFrame: legível e otimizado de graça."

### 4. Desenvolvimento — parte 3 (7:00 – 9:00)

> "Agora o pulo do gato: o Spark é lazy. Quando você faz filter, groupBy, select, nada acontece — ele só anota no plano. Só quando você chama uma ação, count, write, show, é que ele monta o DAG, deixa o Catalyst otimizar e roda. Por que isso importa? Porque ele vê o pipeline inteiro antes de executar. E cuidado com o shuffle: groupBy, join, distinct obrigam dados da mesma chave a se encontrarem, redistribuindo tudo pela rede. É a operação mais cara. Otimizar Spark é, acima de tudo, domar o shuffle."

### 5. Encerramento (9:00 – 11:00)

> "Lembra da Lei de Amdahl: dobrar executors não dobra a velocidade — só 15% de trabalho serial já trava o ganho num fator de 5 ou 6. Filtre antes de juntar, use broadcast join, escolha bem as partições. O Spark é o nosso canivete do batch. Mas e quando o dado não pode esperar o lote — quando ele precisa ser tratado no instante em que nasce? Essa é a próxima aula: streaming com Apache Kafka. Te espero!"

---

## Aula 7 — Processamento em tempo real e streaming

Imagine detectar uma fraude no cartão **enquanto** a compra acontece, não no relatório do dia seguinte. Ou recalcular o preço de uma corrida a cada segundo conforme a demanda muda. Há decisões que não podem esperar o próximo lote. Esta aula entra no mundo do **processamento em tempo real**: a mensageria com **Apache Kafka**, seus conceitos de **tópicos, partições e offsets**, o desafio de agregar fluxos infinitos com **janelas** e as **garantias de entrega** que diferenciam um sistema confiável de um que perde (ou duplica) dados.

### Batch vs streaming

No **batch**, o dado é processado em **lotes finitos** com início, meio e fim — você roda o job, ele termina, gera o resultado. No **streaming**, o dado é um **fluxo infinito e contínuo**: registros chegam o tempo todo e são processados quase no instante em que surgem, muitas vezes em milissegundos.

A diferença não é só de velocidade, mas de **modelo mental**. No batch você pergunta "qual foi o total de vendas ontem?". No streaming você pergunta "qual é o total de vendas *agora*, nos últimos 5 minutos, atualizado continuamente?". Streaming traz desafios próprios: o dado nunca "acaba", pode chegar **fora de ordem** (eventos atrasados pela rede) e exige raciocinar sobre **tempo do evento** (quando aconteceu) versus **tempo de processamento** (quando chegou).

![Logo do Apache Kafka, plataforma distribuída de streaming de eventos](https://commons.wikimedia.org/wiki/Special:FilePath/Apache_kafka.svg)

### Mensageria e o Apache Kafka

No coração do streaming está a **mensageria**: um intermediário que **desacopla** quem produz dados de quem os consome. O produtor não conhece o consumidor; ambos só conhecem o intermediário. Isso permite escalar produtores e consumidores de forma independente e absorver picos de carga.

O **Apache Kafka**, criado no LinkedIn em 2011, é o padrão de fato. Mais do que uma fila tradicional, o Kafka é um **log distribuído e durável**: as mensagens não somem quando lidas — ficam gravadas por um período de retenção, e múltiplos consumidores podem ler o mesmo fluxo em ritmos diferentes. Um cluster Kafka é formado por **brokers** (os servidores que armazenam os dados) e organiza tudo em torno de **tópicos**.

### Tópicos, partições e offsets

Um **tópico** é uma categoria nomeada de mensagens — por exemplo `pedidos`, `cliques`, `sensores`. Cada tópico é dividido em **partições**, e é nelas que mora a escalabilidade: partições são distribuídas entre os brokers e lidas em paralelo por consumidores diferentes.

Dentro de uma partição, cada mensagem recebe um número sequencial imutável: o **offset**. O Kafka garante **ordem apenas dentro de uma partição** (não entre partições). O consumidor controla **até qual offset já leu** (o *committed offset*), o que dá flexibilidade enorme: pode reprocessar do começo, retomar de onde parou após uma falha ou avançar para o presente. Mensagens com a mesma **chave** vão sempre para a mesma partição — útil para manter, por exemplo, todos os eventos de um cliente em ordem.

### Janelas: tumbling e sliding

Como agregar um fluxo que nunca termina? Recortando-o no tempo, com **janelas**. As duas mais comuns:

- **Tumbling (fixa, sem sobreposição):** o tempo é fatiado em blocos contíguos e iguais — por exemplo, "total de vendas a cada 5 minutos". Cada evento pertence a exatamente uma janela.
- **Sliding (deslizante, com sobreposição):** uma janela de tamanho fixo que avança de tempos em tempos — por exemplo, "média dos últimos 10 minutos, recalculada a cada 1 minuto". Um mesmo evento pode pertencer a várias janelas.

Há ainda janelas de **sessão**, que agrupam eventos por inatividade (toda a navegação de um usuário até ele ficar 30 min sem clicar). Trabalhar com janelas exige lidar com dados atrasados, geralmente via marcadores de progresso temporal (*watermarks*).

### Garantias de entrega (at-least-once, exactly-once)

Quando uma mensagem viaja entre produtor, broker e consumidor, três níveis de garantia são possíveis:

- **At-most-once (no máximo uma vez):** mensagens podem ser perdidas, mas nunca duplicadas. Rápido e barato — aceitável para métricas tolerantes a perda.
- **At-least-once (ao menos uma vez):** nenhuma mensagem é perdida, mas pode haver duplicatas (se um *ack* se perde, reenviamos). É o padrão mais comum — e por isso o **consumo idempotente** (lembra da Aula 5?) é tão importante.
- **Exactly-once (exatamente uma vez):** cada mensagem é processada uma única vez, sem perda nem duplicação. É o mais difícil e custoso; o Kafka oferece via produtores idempotentes e transações, mas com overhead.

A regra prática: prefira **at-least-once + processamento idempotente** — é mais simples e robusto que perseguir exactly-once a qualquer custo.

### Exemplo numérico: latência e vazão

Um tópico de cliques recebe $30.000$ mensagens por segundo. Cada consumidor de um grupo processa, em média, $5.000$ mensagens por segundo. Para acompanhar o fluxo sem acumular atraso, o número mínimo de consumidores (e, portanto, de partições, já que cada partição é lida por no máximo um consumidor do grupo) é:

$$
N = \frac{30.000}{5.000} = 6\ \text{consumidores / partições}
$$

Se o tópico tivesse apenas $4$ partições, a vazão máxima seria $4 \times 5.000 = 20.000$ msg/s, e o sistema acumularia $30.000 - 20.000 = 10.000$ mensagens de atraso **por segundo** — em $1$ minuto, $600.000$ mensagens de *lag*. Já com $8$ partições, sobra folga ($40.000$ msg/s de capacidade). Por isso o número de partições é uma das decisões de capacidade mais importantes no Kafka: define o teto de paralelismo do consumo.

### Pausa para reflexão (Desafio)

> Você está projetando o sistema de **detecção de fraude** de um banco. Cada transação precisa ser avaliada em **menos de 200 ms**. Pergunte-se: faz sentido usar batch aqui? Que garantia de entrega você escolheria — e por quê duplicar uma checagem de fraude é menos grave do que **perder** uma? Como você usaria janelas para detectar "5 transações do mesmo cartão em cidades diferentes em 2 minutos"? Esboce, em um parágrafo, a arquitetura de tópicos e janelas que você proporia.

### Atividade prática

Suba um Kafka local com Docker (`docker run` da imagem `apache/kafka`, ou via Confluent).

1. Crie um tópico `eventos` com **3 partições**.
2. Escreva um **produtor** simples (Python com `kafka-python` ou `confluent-kafka`) que envie eventos com uma **chave** (ex.: `id_usuario`) e observe como eventos da mesma chave caem na mesma partição.
3. Escreva um **consumidor** e inspecione os **offsets** com `kafka-consumer-groups.sh --describe`.
4. Pare o consumidor, produza mais eventos, religue-o e confirme que ele **retoma do offset** comprometido, sem perder mensagens.

### Pontos-chave

- **Batch** processa lotes finitos; **streaming** processa um fluxo infinito quase em tempo real.
- O **Kafka** é um **log distribuído e durável** que desacopla produtores de consumidores.
- A escalabilidade vem das **partições**; a ordem é garantida **dentro de uma partição**, e o **offset** controla a leitura.
- **Janelas** (tumbling, sliding, sessão) recortam o fluxo infinito para permitir agregações.
- Prefira **at-least-once + consumo idempotente**; **exactly-once** é possível, porém caro.

### Para saber mais

- **Akidau, T.; Chernyak, S.; Lax, R.** *Streaming Systems*. O'Reilly, 2018.
- **Documentação oficial do Apache Kafka:** https://kafka.apache.org/documentation/
- **Apache Kafka — guia de design e conceitos:** https://kafka.apache.org/intro

## Aula 7 — Roteiro da Videoaula 7: "Processamento em tempo real e streaming"

**Duração:** 9 a 11 minutos.

### 1. Abertura (0:00 – 0:40)

> "Detectar uma fraude enquanto a compra acontece, não no relatório de amanhã. Recalcular o preço de uma corrida a cada segundo. Tem decisão que não pode esperar o próximo lote. Bem-vindo ao mundo do tempo real — e ao seu rei: o Apache Kafka."

### 2. Desenvolvimento — parte 1 (0:40 – 4:00)

> "No batch, o dado é finito: roda, termina, entrega. No streaming, o dado é um fluxo infinito — chega o tempo todo e é processado em milissegundos. Muda o modelo mental: em vez de 'quanto vendi ontem', você pergunta 'quanto estou vendendo agora, nos últimos 5 minutos'. E o coração disso é a mensageria: um intermediário que desacopla quem produz de quem consome. O Kafka é o padrão. E é mais que uma fila: é um log durável — a mensagem não some quando lida, vários consumidores leem o mesmo fluxo no próprio ritmo."

### 3. Desenvolvimento — parte 2 (4:00 – 7:00)

> "Três palavras que você precisa dominar: tópico, partição, offset. Tópico é a categoria — pedidos, cliques, sensores. Cada tópico se divide em partições, e é daí que vem o paralelismo: cada partição pode ser lida por um consumidor diferente. Dentro da partição, cada mensagem ganha um offset, um número sequencial. O Kafka garante ordem só dentro da partição. E o consumidor controla até onde leu — pode voltar ao início, retomar de onde parou, avançar. Mensagens com a mesma chave caem sempre na mesma partição."

### 4. Desenvolvimento — parte 3 (7:00 – 9:00)

> "Como agregar um fluxo que nunca acaba? Com janelas. Tumbling: blocos fixos sem sobreposição, total a cada 5 minutos. Sliding: janela que desliza, média dos últimos 10 minutos recalculada a cada minuto. E as garantias de entrega: at-most-once pode perder; at-least-once nunca perde mas pode duplicar — e por isso o consumo idempotente da aula 5 volta a brilhar; exactly-once é o ideal, mas custa caro. Minha recomendação: at-least-once com processamento idempotente."

### 5. Encerramento (9:00 – 11:00)

> "Fiz a conta: 30 mil mensagens por segundo, consumidor de 5 mil, precisa de 6 partições no mínimo — partição é o teto do seu paralelismo. Agora você tem batch e streaming no cinto de ferramentas. Mas falta uma peça: quem coordena tudo isso? Quem garante que a ingestão roda antes do Spark, que o retry dispara quando algo falha, que o pipeline inteiro respeita um prazo? Essa é a última aula da unidade: orquestração com Apache Airflow. Te espero!"

---

## Aula 8 — Orquestração de pipelines com Apache Airflow

Você já sabe ingerir, processar em lote e processar em tempo real. Mas um pipeline real tem **dezenas de tarefas que dependem umas das outras**, em ordens precisas, em horários certos, com tratamento de falha e prazos a cumprir. Coordenar isso manualmente é insustentável. Entra a **orquestração**, e a ferramenta mais usada do mercado é o **Apache Airflow**. Nesta aula você aprende a modelar pipelines como **DAGs**, usar **operators**, **agendar** execuções, fazer **backfill** de períodos passados, configurar **retries** e monitorar **SLAs**.

### Por que orquestrar pipelines

Um pipeline é uma sequência de passos com **dependências**: você só transforma depois de ingerir; só carrega o relatório depois de transformar. Sem orquestração, isso vira um emaranhado de `cron`s frágeis e falhas silenciosas que ninguém percebe até o relatório sair vazio.

Um **orquestrador** resolve isso ao gerenciar, num só lugar: a **ordem** das tarefas, o **agendamento**, o **tratamento de falhas** (retries, alertas), a **observabilidade** (logs, status, histórico) e a **recuperação** (reprocessar um dia que deu errado). O Airflow, criado no Airbnb em 2014, popularizou a filosofia **"pipelines como código"**: você descreve o fluxo em **Python**, o que permite versionar, testar e revisar pipelines como qualquer software.

![Logo do Apache Airflow, plataforma de orquestração de workflows como código](https://commons.wikimedia.org/wiki/Special:FilePath/AirflowLogo.png)

### DAGs, tasks e operators

No Airflow, um pipeline é um **DAG (Directed Acyclic Graph)** — um grafo **dirigido** (as setas têm sentido) e **acíclico** (nenhuma tarefa depende, direta ou indiretamente, de si mesma). Cada nó é uma **task**, e as arestas são as dependências (`extrair >> transformar >> carregar`).

Uma task é uma instância de um **operator** — um modelo que sabe executar um tipo de trabalho:

| Operator | O que faz |
| --- | --- |
| `PythonOperator` | Executa uma função Python |
| `BashOperator` | Executa um comando de shell |
| `SQLExecuteQueryOperator` | Roda uma query em um banco |
| `SparkSubmitOperator` | Dispara um job Spark |
| Sensors | Esperam por uma condição (ex.: chegada de um arquivo) |

A acidicidade não é detalhe técnico: ela **garante que o pipeline termina**. Um grafo com ciclo poderia rodar para sempre.

### Agendamento e dependências

Cada DAG tem um `schedule` que define **quando** ele roda — uma expressão `cron` (`0 6 * * *` = todo dia às 6h), um *preset* (`@daily`, `@hourly`) ou um intervalo. O Airflow trabalha com o conceito de **data interval**: cada execução está associada a um *período de dados* (a "data lógica"), não ao relógio de quando o job de fato disparou. Isso é o que torna o reprocessamento determinístico.

As dependências entre tasks são declaradas com os operadores `>>` (a montante para a jusante) e `<<`. Você pode montar fluxos lineares, em leque (uma task alimenta várias) ou em funil (várias convergem para uma). Tasks sem dependência entre si rodam **em paralelo**, limitadas pela capacidade dos *workers* e por configurações de concorrência.

### Backfill e retries

Duas funcionalidades fazem o Airflow brilhar na operação. O **backfill** é a capacidade de executar o pipeline para **períodos passados** — útil quando você cria um DAG novo e quer popular o histórico, ou quando descobre um bug e precisa reprocessar a última semana. Como cada execução está atrelada a uma data lógica, o Airflow sabe exatamente qual janela de dados reprocessar (e aqui a **idempotência** da Aula 5 é o que torna o backfill seguro: reprocessar não duplica).

Os **retries** automatizam a resiliência: você define quantas vezes uma task deve tentar de novo (`retries`) e o intervalo entre tentativas (`retry_delay`), idealmente com *backoff exponencial*. Falhas transitórias (uma API que oscilou, uma conexão que caiu) se resolvem sozinhas, sem acordar ninguém de madrugada.

### Monitoramento e alertas

O Airflow oferece uma **interface web** rica: visão em grafo do DAG, *grid view* com o histórico de execuções colorido por status, logs de cada task e capacidade de re-disparar tarefas manualmente. Para além do visual, ele integra **alertas**: `email_on_failure`, *callbacks* (`on_failure_callback`) que notificam o Slack ou sistemas de plantão, e métricas exportáveis para Prometheus/Grafana. Observabilidade é o que separa um pipeline que "deveria estar funcionando" de um que você *sabe* que está.

### Exemplo numérico: SLA do pipeline

Um pipeline diário precisa entregar o dashboard executivo até as **8h00**. As tarefas têm os seguintes tempos médios e janelas de retry:

| Task | Tempo médio | Retries × delay |
| --- | --- | --- |
| Ingestão | $25$ min | $2 \times 5$ min |
| Transformação Spark | $40$ min | $1 \times 10$ min |
| Carga no warehouse | $15$ min | $2 \times 5$ min |

O **caminho crítico** em condições normais (sem falhas) é:

$$
T_{normal} = 25 + 40 + 15 = 80\ \text{min}
$$

No **pior caso**, com todos os retries acionados, somam-se os tempos de espera e as re-execuções:

$$
T_{pior} = (25 + 2\cdot5) + (40 + 1\cdot10) + (15 + 2\cdot5) = 35 + 50 + 25 = 110\ \text{min}
$$

Para entregar às 8h00 mesmo no pior caso, o DAG deve iniciar até:

$$
08{:}00 - 110\ \text{min} = 06{:}10
$$

Para ter margem, agenda-se às **6h00** (`0 6 * * *`) com um **SLA de 110 min**: se a entrega atrasar, o Airflow dispara o alerta de violação de SLA — e o time age *antes* de o executivo abrir o dashboard vazio.

### Atividade prática

Suba o Airflow localmente (via `docker compose` do projeto oficial ou `astro dev start` da Astronomer).

1. Crie um DAG `pipeline_vendas` com `schedule="@daily"` e três tasks: `ingerir` (`PythonOperator`), `transformar` (`BashOperator` ou `SparkSubmitOperator`) e `carregar`.
2. Declare as dependências: `ingerir >> transformar >> carregar`.
3. Configure `retries=2` e `retry_delay` de 1 minuto na task de ingestão; force uma falha (ex.: `raise`) e observe o retry na UI.
4. Defina um `sla` na task de carga e dispare um **backfill** de 3 dias passados (`airflow dags backfill`). Confirme que a idempotência impediu duplicação.

### Pontos-chave

- A **orquestração** coordena ordem, agendamento, falhas, observabilidade e recuperação de pipelines.
- No Airflow, um pipeline é um **DAG** (dirigido e acíclico); tasks são instâncias de **operators**.
- O **agendamento** usa `cron`/presets e o conceito de **data interval** (data lógica), o que torna o reprocessamento determinístico.
- **Backfill** reexecuta períodos passados; **retries** automatizam a resiliência — ambos exigem **idempotência**.
- **SLAs**, alertas e a UI dão a **observabilidade** que torna o pipeline confiável de verdade.

### Para saber mais

- **Documentação oficial do Apache Airflow:** https://airflow.apache.org/docs/
- **Conceitos centrais do Airflow (DAGs, operators, scheduling):** https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/
- **Reis, J.; Housley, M.** *Fundamentals of Data Engineering*. O'Reilly, 2022 — capítulo sobre orquestração e DataOps.

### O que você verá na próxima unidade

Na **Unidade 3 — Armazenamento e Arquitetura de Dados**, vamos parar de mover dados e focar em **onde** e **como** guardá-los bem. Você vai entender a diferença entre **OLTP e OLAP**, a anatomia de um **data warehouse** e seus modelos dimensionais (esquema estrela, *fato* e *dimensão*), o conceito de **data lake** e a evolução para o **lakehouse** com formatos de tabela abertos (**Delta Lake, Apache Iceberg, Hudi**), além de boas práticas de **particionamento, modelagem e governança**. É a hora de dar à torrente de dados que aprendemos a movimentar uma **casa bem arquitetada**.

## Aula 8 — Roteiro da Videoaula 8: "Orquestração de pipelines com Apache Airflow"

**Duração:** 9 a 11 minutos.

### 1. Abertura (0:00 – 0:40)

> "Você já sabe ingerir, processar em lote, processar em tempo real. Mas um pipeline real tem dezenas de tarefas que dependem umas das outras, em horários certos, com tratamento de falha. Coordenar isso na mão é insustentável. Hoje: orquestração com Apache Airflow."

### 2. Desenvolvimento — parte 1 (0:40 – 4:00)

> "Sem orquestração, seu pipeline vira um emaranhado de crons frágeis e falhas silenciosas — o relatório sai vazio e ninguém percebe. O orquestrador resolve num lugar só: ordem das tarefas, agendamento, retries, logs, recuperação. O Airflow, do Airbnb em 2014, trouxe a filosofia 'pipeline como código': você descreve o fluxo em Python. Isso é poderoso — você versiona, testa e revisa o pipeline como qualquer software. No Airflow, o pipeline é um DAG: grafo dirigido e acíclico. Dirigido porque as setas têm sentido; acíclico porque nada pode depender de si mesmo — é isso que garante que o pipeline termina."

### 3. Desenvolvimento — parte 2 (4:00 – 7:00)

> "Cada nó do DAG é uma task, instância de um operator: PythonOperator roda função Python, BashOperator roda shell, SparkSubmitOperator dispara o Spark, sensors esperam uma condição. As dependências você declara com setas: extrair >> transformar >> carregar. Tarefas sem dependência rodam em paralelo. O agendamento usa cron ou presets como @daily, e o conceito-chave é o data interval: cada execução está ligada a um período de dados, uma data lógica, não ao relógio de quando disparou. É isso que torna o reprocessamento determinístico."

### 4. Desenvolvimento — parte 3 (7:00 – 9:00)

> "Duas joias da operação: backfill e retries. Backfill reexecuta períodos passados — criou um DAG novo, quer popular o histórico? Backfill. E aqui a idempotência da aula 5 volta: reprocessar não pode duplicar. Retries automatizam a resiliência: define quantas tentativas e o intervalo, de preferência com backoff exponencial, e a API que oscilou se resolve sozinha de madrugada. E não esqueça da observabilidade: a UI mostra o grafo, o histórico colorido, os logs; configure alertas no e-mail ou Slack e um SLA de tempo de entrega."

### 5. Encerramento (9:00 – 11:00)

> "Fechei com uma conta de SLA: caminho crítico de 80 minutos, 110 no pior caso com retries, então agendo às 6h para entregar às 8h com folga. Esse é o cinto completo da Unidade 2: ingerir, processar em lote, processar em tempo real e orquestrar. Na próxima unidade a gente para de mover dados e aprende a guardá-los bem — data warehouse, data lake, lakehouse. Te espero!"

---

## Quiz não avaliativo

### Questão 1

Sobre a diferença entre **ETL** e **ELT** na ingestão de dados, assinale a alternativa **correta**:

- [ ] a. No ELT a transformação ocorre em um servidor intermediário antes de o dado tocar o destino, enquanto no ETL o dado bruto é carregado primeiro.
- [x] b. No ETL transforma-se antes de carregar (em um servidor intermediário); no ELT carrega-se o dado bruto no destino e transforma-se lá dentro, aproveitando o poder do data warehouse moderno.
- [ ] c. ETL e ELT são exatamente a mesma coisa; a única diferença é o idioma da sigla.
- [ ] d. ELT só funciona em batch, enquanto ETL só funciona em streaming.

**Resposta correta:** `b`

**Feedback:** A (b) descreve corretamente a ordem das etapas. No **ETL** a transformação acontece *antes* da carga, num estágio intermediário; no **ELT** o dado bruto é carregado primeiro e transformado dentro do destino (BigQuery, Snowflake), que é o padrão dominante na nuvem por preservar a fonte da verdade e permitir re-transformar sem reextrair. A (a) inverte os conceitos. A (c) é falsa — a ordem das operações muda a arquitetura inteira. A (d) é falsa: ambos podem operar em batch ou streaming.

### Questão 2

A respeito de **tópicos, partições e offsets** no Apache Kafka, assinale a alternativa **correta**:

- [ ] a. O Kafka garante ordem total entre todas as partições de um tópico, independentemente da chave da mensagem.
- [ ] b. Aumentar o número de partições não tem efeito sobre o paralelismo de consumo.
- [x] c. A escalabilidade vem das partições; a ordem é garantida apenas dentro de uma partição, e o offset é o número sequencial que o consumidor usa para controlar até onde já leu.
- [ ] d. O offset é definido pelo produtor para escolher manualmente em qual broker a mensagem será gravada.

**Resposta correta:** `c`

**Feedback:** A (c) está correta: partições são a unidade de paralelismo, o Kafka garante ordem **apenas dentro de uma partição** (não entre elas), e o **offset** é o índice sequencial que permite ao consumidor retomar, reprocessar ou avançar. A (a) é falsa — não há ordem total entre partições. A (b) é falsa — o número de partições define o teto de paralelismo do consumo. A (d) confunde conceitos: o offset é atribuído pelo broker dentro da partição; a partição-destino é escolhida pela chave da mensagem, não para selecionar o broker manualmente.

---

## Atividade Verificadora (AAI — Atividade Avaliativa Individual)

**Pergunta:**

> Uma fintech precisa construir, do zero, o pipeline de dados de **transações de cartão**. Há dois requisitos conflitantes: (1) um sistema **antifraude** que precisa avaliar cada transação em **menos de 300 ms**, e (2) um **relatório regulatório diário** consolidado, entregue ao Banco Central até as **9h** de cada dia, que não pode conter duplicatas nem perder transações.
>
> Estruture sua resposta em três partes:
>
> 1. **Arquitetura de ingestão e processamento** — para cada requisito, escolha entre batch e streaming, justifique e nomeie a(s) ferramenta(s) (Kafka, Spark, Airflow) e o papel de cada uma.
> 2. **Confiabilidade** — que garantia de entrega você adotaria no fluxo antifraude e como garantiria que o relatório diário não duplica nem perde transações (cite explicitamente idempotência/CDC).
> 3. **Operação** — como você orquestraria e monitoraria o relatório diário (agendamento, retries, SLA, backfill) para cumprir o prazo das 9h mesmo com falhas transitórias.

**Resposta esperada:**

> Uma resposta de qualidade separa claramente os dois caminhos. Para o **antifraude**, escolhe **streaming com Apache Kafka** (transações como eventos em um tópico particionado pela chave do cartão, garantindo ordem por cartão) com processamento em janelas (ex.: sliding para detectar N transações em curto intervalo); justifica que batch é inviável pelo limite de 300 ms. Para o **relatório regulatório**, escolhe **batch com Apache Spark** (processamento distribuído do volume diário) **orquestrado pelo Apache Airflow**. Em **confiabilidade**, no fluxo antifraude adota **at-least-once com consumo idempotente** (perder uma transação é pior que checá-la duas vezes; exactly-once é caro e desnecessário se o consumo é idempotente); para o relatório, garante ausência de perda e duplicação via **CDC/ingestão incremental** com **MERGE por chave de transação** ou **sobrescrita de partição por dia** — ou seja, idempotência ponta a ponta. Em **operação**, descreve um DAG diário com `schedule` (`cron`) calculado a partir do **caminho crítico** somado aos **retries** (com backoff), define um **SLA** com margem para entregar antes das 9h, configura **alertas** (e-mail/Slack) em falha e violação de SLA, e usa **backfill** idempotente para reprocessar dias com problema. A melhor resposta demonstra **pensamento sistêmico**: streaming e batch coexistem (arquitetura tipo Lambda/Kappa), e a idempotência é o fio que costura confiabilidade e reprocessamento em todas as camadas. Deve evitar "usar Spark para tudo" ou "exactly-once em tudo" sem justificar custo/benefício.

---

## Material complementar

### Direto da fonte — livro da Biblioteca Virtual

> Este é o livro de cabeceira da engenharia de dados moderna e cobre, em um só lugar, todo o coração desta unidade: ingestão (ETL vs ELT, batch vs CDC), o ciclo de vida do dado e a orquestração com DataOps. Reis e Housley são pragmáticos e atemporais — explicam *princípios* que sobrevivem à troca de ferramentas. Leitura direta sobre tudo o que destrinchamos nas Aulas 5 a 8.

- **Nome do livro:** *Fundamentals of Data Engineering: Plan and Build Robust Data Systems*
- **Capítulo:** Capítulos 7 (Ingestão), 8 (Consultas, modelagem e transformação) e 2 (Ciclo de vida da engenharia de dados)
- **Organizador:** Joe Reis e Matt Housley
- **Editora:** O'Reilly Media
- **Link de acesso (BV):** https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/
- **Aula em que entra:** Aulas 5 a 8

### Para mergulhar no assunto

> Recomendo a palestra clássica **"Turning the database inside out with Apache Samza"**, de Martin Kleppmann (autor de *Designing Data-Intensive Applications*), e o próprio livro *Designing Data-Intensive Applications*. Kleppmann mostra como logs de eventos (a ideia central do Kafka) reorganizam toda a arquitetura de dados — é uma daquelas leituras/vídeos que "viram a chave" sobre streaming e CDC. Visualizar essa mudança de paradigma ajuda a entender por que o ELT e o streaming venceram.

- **Link(s):** https://www.confluent.io/blog/turning-the-database-inside-out-with-apache-samza/ — livro: *Designing Data-Intensive Applications*, Martin Kleppmann (O'Reilly, 2017)
- **Aula em que entra:** Aulas 5 e 7

### Podcast (curadoria, até 45 min)

> O canal **Databricks (YouTube)** mantém uma série excelente de explicações curtas e palestras sobre Apache Spark, streaming estruturado e arquiteturas lakehouse, direto de quem criou o Spark. Ótimo para fixar os conceitos das Aulas 6 e 7 com demonstrações reais e casos de uso de produção.

- **Nome do podcast/canal:** Databricks
- **Tema recomendado:** "Apache Spark in 100 Seconds / Structured Streaming fundamentals"
- **Link:** https://www.youtube.com/@Databricks (YouTube)
- **Aula em que entra:** Aulas 6 e 7

### Artigo científico

> O artigo fundador de toda a engenharia de dados distribuída moderna. Dean e Ghemawat, do Google, descrevem o modelo **MapReduce** que inspirou o Hadoop e, indiretamente, o Apache Spark. Ler o original é entender de onde vêm as ideias de *map*, *reduce*, paralelismo de dados e tolerância a falhas que sustentam a Aula 6 — e perceber como um paper de 2004 ainda molda as ferramentas que usamos hoje.

- **Link:** https://doi.org/10.1145/1327452.1327492 (DOI)
- **Aula em que entra:** Aula 6
- **Referência bibliográfica do artigo no formato ABNT:**
  > DEAN, Jeffrey; GHEMAWAT, Sanjay. **MapReduce: simplified data processing on large clusters**. *Communications of the ACM*, v. 51, n. 1, p. 107-113, jan. 2008.
