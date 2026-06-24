# Avaliação Final — Data Engineering and Pipelines

- **Disciplina:** Data Engineering and Pipelines
- **Professor-conteudista:** Afonso Cesar Lelis Brandão

## Orientações

- **40 questões** padrão ENADE no total:
  - **15** do tipo **asserção-razão** (Q1–Q15)
  - **15** do tipo **interpretação** (Q16–Q30)
  - **10** do tipo **discursiva** (Q31–Q40, posicionadas ao final)
- Cada questão objetiva tem **5 alternativas (a–e)**, com a correta prefixada por `*`.
- Rotação das alternativas corretas: **a, b, c, d, e, a, b, c, d, e...** (6 questões para cada letra nas objetivas).
- Para cada alternativa de questão objetiva, há **feedback explicativo**.
- Feedbacks das objetivas ao final, na ordem das questões.

---

## Questões objetivas (1–30) e discursivas (31–40)

### Questão 1 (Asserção-Razão)

> **Asserção I:** No padrão ELT, o dado bruto é carregado primeiro no destino e transformado depois, dentro do próprio data warehouse ou lakehouse.
>
> **porque**
>
> **Razão II:** A queda do custo de armazenamento na nuvem e o aumento do poder de processamento dos warehouses modernos tornaram economicamente viável guardar o dado cru e transformá-lo sob demanda, preservando a fonte da verdade.

A respeito dessas asserções, assinale a opção correta:

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 2 (Asserção-Razão)

> **Asserção I:** O formato de arquivo Parquet é colunar e comprimido, sendo o padrão de mercado para cargas analíticas (OLAP).
>
> **porque**
>
> **Razão II:** O Apache Kafka, tornado open-source pelo LinkedIn em 2011, é um log distribuído e durável que desacopla produtores de consumidores no processamento de streaming.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 3 (Asserção-Razão)

> **Asserção I:** As propriedades ACID (atomicidade, consistência, isolamento e durabilidade) tornam os bancos relacionais confiáveis para transações financeiras, como uma transferência bancária.
>
> **porque**
>
> **Razão II:** A atomicidade garante que, em uma transferência, o débito de uma conta e o crédito de outra ocorram em metades independentes, de modo que, se o sistema cair, apenas o débito seja confirmado.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 4 (Asserção-Razão)

> **Asserção I:** O teorema CAP afirma que, em um sistema distribuído, é sempre possível garantir simultaneamente Consistência, Disponibilidade e Tolerância a partição em plenitude, mesmo durante uma falha de rede.
>
> **porque**
>
> **Razão II:** Como partições de rede são inevitáveis em sistemas distribuídos, a escolha prática se dá entre priorizar Consistência (CP) ou Disponibilidade (AP) durante a partição.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 5 (Asserção-Razão)

> **Asserção I:** Em um esquema estrela, a tabela de fatos guarda os atributos descritivos (nome do produto, cidade do cliente) e as tabelas de dimensão guardam as métricas numéricas (valor, quantidade).
>
> **porque**
>
> **Razão II:** A modelagem dimensional sempre exige normalização total das tabelas de dimensão até a 3ª Forma Normal para acelerar consultas analíticas.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

### Questão 6 (Asserção-Razão)

> **Asserção I:** A idempotência de uma operação de ingestão é o que torna seguro habilitar retries e reprocessamentos (backfill) em um pipeline.
>
> **porque**
>
> **Razão II:** Uma operação idempotente produz o mesmo estado final ao ser executada uma ou várias vezes, evitando duplicação de dados quando uma carga é repetida — o que costuma ser obtido com `MERGE`/upsert por chave de negócio ou sobrescrita de partição.

A respeito dessas asserções, assinale a opção correta:

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 7 (Asserção-Razão)

> **Asserção I:** No Apache Spark, o shuffle (redistribuição de dados pela rede em operações como `groupBy` e `join`) é a operação mais cara do motor.
>
> **porque**
>
> **Razão II:** As transformações no Spark são lazy: nada é executado até que uma ação (como `count` ou `write`) seja chamada, momento em que o otimizador Catalyst monta o plano físico.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 8 (Asserção-Razão)

> **Asserção I:** No Apache Kafka, a ordem das mensagens é garantida apenas dentro de uma partição, e o offset é o número sequencial que o consumidor usa para controlar até onde já leu.
>
> **porque**
>
> **Razão II:** O Kafka garante ordenação total entre todas as partições de um tópico, independentemente da chave da mensagem, atribuindo um offset global e único a cada evento do cluster.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 9 (Asserção-Razão)

> **Asserção I:** A garantia de entrega exactly-once deve ser sempre adotada em qualquer pipeline de streaming, pois é simples de implementar e não impõe nenhum custo de desempenho ao Kafka.
>
> **porque**
>
> **Razão II:** A combinação de at-least-once com consumo idempotente é, na prática, mais simples e robusta do que perseguir exactly-once a qualquer custo, já que o exactly-once exige produtores idempotentes e transações, com overhead.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 10 (Asserção-Razão)

> **Asserção I:** No Apache Airflow, um pipeline é modelado como um grafo cíclico, em que é desejável que uma tarefa dependa, direta ou indiretamente, de si mesma para permitir reprocessamento contínuo.
>
> **porque**
>
> **Razão II:** A presença de ciclos em um DAG do Airflow garante que o pipeline sempre termine sua execução em tempo finito, sendo essa a razão de o agendamento usar expressões cron.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

### Questão 11 (Asserção-Razão)

> **Asserção I:** O armazenamento colunar reduz drasticamente o volume de dados varridos e o custo de uma consulta analítica que usa poucas colunas de uma tabela larga.
>
> **porque**
>
> **Razão II:** No armazenamento colunar, os valores de uma mesma coluna ficam juntos, permitindo ler apenas as colunas necessárias e obter alta taxa de compressão, já que valores semelhantes se comprimem melhor.

A respeito dessas asserções, assinale a opção correta:

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 12 (Asserção-Razão)

> **Asserção I:** Formatos de tabela abertos como Delta Lake, Apache Iceberg e Apache Hudi trazem transações ACID e time travel a um data lake construído sobre object storage.
>
> **porque**
>
> **Razão II:** A arquitetura Medallion organiza o lakehouse em três camadas de qualidade crescente — bronze (bruto), silver (limpo) e gold (curado para o negócio).

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 13 (Asserção-Razão)

> **Asserção I:** A separação entre armazenamento e computação nos data warehouses em nuvem permite que múltiplos clusters leiam os mesmos dados sem competir por recursos e que se pague por cada camada separadamente.
>
> **porque**
>
> **Razão II:** Nos data warehouses tradicionais on-premises, armazenamento e processamento eram desacoplados, de modo que escalar um nunca exigia escalar o outro.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 14 (Asserção-Razão)

> **Asserção I:** Na Modern Data Stack, a melhor prática é escrever e manter manualmente os conectores de extração de cada fonte (Salesforce, Stripe, Postgres), pois ferramentas gerenciadas não conseguem lidar com schema drift nem cargas incrementais.
>
> **porque**
>
> **Razão II:** Ferramentas de ingestão gerenciada, como Fivetran e Airbyte, oferecem conectores prontos que cuidam de schema drift, reprocessos e incrementos, dispensando o engenheiro de escrever código de extração.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 15 (Asserção-Razão)

> **Asserção I:** Na LGPD, dado pseudonimizado sai automaticamente do escopo da lei, pois a reidentificação do titular se torna impossível em qualquer circunstância.
>
> **porque**
>
> **Razão II:** Para atender ao direito de eliminação previsto na LGPD, é dispensável conhecer a linhagem do dado, já que apagar a tabela principal garante, por si só, a remoção de todos os rastros do titular em backups, data lake e features de modelos.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

### Questão 16 (Interpretação)

**Estímulo:**

> "Há um ditado no mercado de dados: *garbage in, garbage out*. Por mais sofisticado que seja o modelo de IA ou o dashboard executivo, se o dado que entra é lixo, a saída também será lixo. Por isso costuma-se dizer que cerca de 80% do esforço de qualquer projeto de dados é, na verdade, engenharia de dados."

A leitura mais alinhada ao texto é:

*a. O engenheiro de dados é a base de qualquer iniciativa analítica: sem dado confiável, organizado e disponível, não há ciência de dados, BI ou IA que funcionem.
b. Como modelos modernos de IA corrigem automaticamente dados ruins, a etapa de engenharia de dados tornou-se dispensável.
c. O ditado significa que a qualidade do modelo não depende em nada da qualidade dos dados de entrada.
d. A engenharia de dados ocupa um esforço marginal nos projetos, sendo o trabalho do cientista de dados o que de fato importa.
e. Dashboards e modelos preditivos produzem resultados confiáveis mesmo a partir de dados inconsistentes e incompletos.

### Questão 17 (Interpretação)

**Estímulo:**

A tabela compara quatro formatos de arquivo usados em engenharia de dados:

| Formato | Característica | Melhor uso |
| --- | --- | --- |
| CSV | Texto, sem tipos | Troca simples |
| JSON | Hierárquico, verboso | APIs, semiestruturado |
| Parquet | Colunar, comprimido | Analytics (OLAP) |
| Avro | Por linha, esquema embutido | Ingestão e streaming |

Uma tabela de 100 milhões de linhas é consultada todos os dias em um dashboard que agrega poucas colunas. Qual formato é o mais indicado para o armazenamento analítico?

a. CSV, por ser legível por humanos e universal.
*b. Parquet, por ser colunar e comprimido, lendo apenas as colunas necessárias com alta compressão.
c. JSON, por ser flexível e ideal para dados aninhados.
d. Avro, por ser por linha e otimizado para escrever registros completos rapidamente.
e. Tanto faz, pois o formato de arquivo não influencia o custo nem o desempenho da consulta.

### Questão 18 (Interpretação)

**Estímulo:**

> Uma tabela de pedidos cresce 2 milhões de linhas por dia e já acumula 730 milhões de registros após um ano. A taxa de leitura é de 50.000 linhas/s. A carga **full** lê a tabela inteira; a carga **incremental** lê apenas as linhas novas do dia.

Comparando os tempos da carga full com a carga incremental, a aceleração obtida pela incremental é de aproximadamente:

a. ~2 vezes mais rápida.
b. ~30 vezes mais rápida.
*c. ~365 vezes mais rápida.
d. ~100 vezes mais rápida.
e. ~1.000 vezes mais rápida.

> **Cálculo:** full = 730.000.000 / 50.000 = 14.600 s (~4 h); incremental = 2.000.000 / 50.000 = 40 s. Razão ≈ 14.600 / 40 = 365.

### Questão 19 (Interpretação)

**Estímulo:**

> Um banco precisa avaliar cada transação de cartão em **menos de 200 ms** para detectar fraude. Os eventos chegam continuamente, em altíssimo volume, e precisam ser processados no instante em que surgem. Perder ocasionalmente um evento é menos grave do que ficar fora do ar.

A combinação de arquitetura mais adequada a esse cenário é:

a. Processamento em batch diário com carga full, pois garante consolidação completa antes da decisão.
b. Banco relacional OLTP com snapshot periódico, priorizando consistência forte (CP) acima de tudo.
c. Data warehouse colunar consultado por relatórios noturnos, com modelagem dimensional em esquema estrela.
*d. Streaming com Apache Kafka, processamento em janelas e garantia at-least-once com consumo idempotente, priorizando disponibilidade (AP).
e. ETL clássico em servidor intermediário, com reprocessamento full mensal e exactly-once obrigatório em todas as etapas.

### Questão 20 (Interpretação)

**Estímulo:**

> "No Spark, distribuir um job de 1 TB de logs entre 40 executors reduziria o tempo ideal de mais de 5 horas para cerca de 8 minutos. Mas, se 15% do trabalho for serial (coleta de resultados, shuffle final), a Lei de Amdahl limita o ganho a cerca de 5,8x com 40 executors — e a no máximo ~6,7x mesmo com infinitos nós."

A leitura mais correta do texto é:

a. Adicionar executors gera sempre ganho linear, dobrando a velocidade a cada vez que se dobra o número de máquinas.
b. A fração serial de um job é irrelevante para o tempo total quando há muitos executors.
c. O shuffle é a parte mais barata do Spark e deve ser maximizado para acelerar o job.
d. A Lei de Amdahl prova que o paralelismo nunca traz qualquer benefício em jobs distribuídos.
*e. O paralelismo tem retorno decrescente: reduzir a fração serial (o shuffle) frequentemente rende mais que apenas somar máquinas ao cluster.

### Questão 21 (Interpretação)

**Estímulo:**

> Um tópico de cliques no Kafka recebe 30.000 mensagens por segundo. Cada consumidor de um grupo processa, em média, 5.000 mensagens por segundo. Cada partição é lida por, no máximo, um consumidor do grupo.

O número mínimo de partições para acompanhar o fluxo sem acumular atraso é:

*a. 6 partições (e, portanto, 6 consumidores no grupo).
b. 2 partições, pois 2 consumidores dão conta de qualquer vazão.
c. 30.000 partições, uma por mensagem recebida por segundo.
d. 1 partição, pois o Kafka paraleliza automaticamente entre brokers.
e. 150 partições, multiplicando consumidores por mensagens.

> **Cálculo:** N = 30.000 / 5.000 = 6 consumidores/partições.

### Questão 22 (Interpretação)

**Estímulo:**

> Um pipeline diário precisa entregar o dashboard executivo até as 8h00. O caminho crítico normal é de 80 min; no pior caso, com todos os retries acionados, sobe para 110 min. Para entregar mesmo no pior caso, deseja-se uma margem de segurança.

Considerando os tempos descritos, qual decisão de agendamento e SLA é a mais coerente?

a. Agendar às 7h50, pois 10 minutos bastam para qualquer pipeline diário.
*b. Agendar às 6h00 com SLA de 110 min, garantindo entrega até as 8h00 mesmo no pior caso e disparando alerta de violação de SLA se houver atraso.
c. Agendar às 8h00 em ponto, pois o Airflow compensa retries automaticamente sem afetar o horário.
d. Não definir SLA, pois o backfill já garante que o dado chegue a qualquer momento do dia.
e. Agendar às 4h00 sem SLA, eliminando a necessidade de retries e de observabilidade.

### Questão 23 (Interpretação)

**Estímulo:**

> Uma tabela de eventos tem 10 TB, particionada por dia (365 dias). Um analista filtra **um único dia** e seleciona **apenas 1 das 50 colunas**. A cobrança é de US\$ 6,25 por TB varrido. Sem particionamento e com `SELECT *`, a consulta lê os 10 TB inteiros.

A leitura mais correta sobre o impacto de particionamento e seleção de colunas é:

a. Particionar e selecionar colunas não altera o custo, pois o motor sempre varre a tabela inteira.
b. `SELECT *` em armazenamento colunar é a forma mais barata de consultar, pois evita planejamento.
*c. Particionamento por dia (partition pruning) somado à seleção de poucas colunas reduz os bytes varridos em ordens de grandeza, derrubando o custo da mesma consulta de dezenas de dólares para frações de centavo.
d. Duplicar a tabela em três cópias é a forma mais eficaz de reduzir o custo por consulta.
e. Migrar a tabela para um banco OLTP por linha tornaria a consulta analítica mais barata.

### Questão 24 (Interpretação)

**Estímulo:**

> "A Modern Data Stack é modular, em nuvem e centrada no warehouse/lakehouse, baseada em ELT. O dbt transforma dados dentro do DW usando apenas SQL, trazendo modelos versionados em Git, lineage automático, testes de dados e documentação gerada — práticas de engenharia de software aplicadas à análise."

A função do dbt na Modern Data Stack é melhor descrita como:

a. O "E" (Extract): ele extrai dados das fontes por meio de conectores prontos.
b. O "L" (Load): ele carrega dados brutos das fontes diretamente no object storage.
c. A camada de BI: ele entrega dashboards e self-service ao usuário final.
*d. O "T" (Transform): ele materializa as camadas silver/gold (ou data marts) no warehouse via SQL, com testes, lineage e documentação versionados.
e. O orquestrador: ele substitui o Airflow no agendamento e no tratamento de falhas de todas as tarefas.

### Questão 25 (Interpretação)

**Estímulo:**

> "Não dá para governar o que não se enxerga. A linhagem (data lineage) mapeia de qual fonte o dado veio, por quais transformações passou e em quais dashboards e modelos termina. Ela responde a duas perguntas opostas: a jusante, 'se eu mudar esta coluna, o que quebra?'; a montante, 'este número estranho, de onde saiu?'."

A leitura mais alinhada ao texto é:

a. Linhagem serve apenas para gerar documentação estética, sem utilidade operacional.
b. A análise de impacto (jusante) e a de causa-raiz (montante) são a mesma pergunta com nomes diferentes.
c. Linhagem é exigida apenas em sistemas de streaming, não em pipelines em batch.
d. Conhecer a linhagem é irrelevante para atender pedidos de exclusão previstos na LGPD.
*e. A linhagem habilita análise de impacto (jusante) e de causa-raiz (montante) e é pré-requisito para localizar todos os lugares onde um dado pessoal pousou, viabilizando a exclusão exigida pela LGPD.

### Questão 26 (Interpretação)

**Estímulo:**

> "Testes verificam regras que você antecipou (`not_null`, valor entre 0 e 1) dentro do pipeline. A observabilidade detecta o que você não previu, monitorando ao longo do tempo cinco pilares: frescor, volume, distribuição, esquema e linhagem."

A leitura mais correta é:

*a. Testes e observabilidade são complementares: o teste barra o erro antecipado na porta, enquanto a observabilidade detecta anomalias imprevistas comparando o comportamento atual ao histórico.
b. Testes e observabilidade são sinônimos e verificam exatamente as mesmas regras.
c. A observabilidade só funciona em pipelines de streaming, e os testes só em batch.
d. Testes de dados tornam a observabilidade desnecessária em pipelines maduros.
e. Os cinco pilares da observabilidade dizem respeito apenas à segurança e ao controle de acesso, não à saúde do dado.

### Questão 27 (Interpretação)

**Estímulo:**

> Uma fintech rodou análise de risco sobre uma tabela cujo campo de renda passou a chegar multiplicado por 100, por uma mudança não comunicada no sistema-fonte. Sem monitoração, o erro passou despercebido por 9 dias (TTD = 9 dias), e a correção levou 1 dia (TTR = 1 dia). A regra 1-10-100 indica que custa R\$ 1 prevenir, R\$ 10 corrigir e R\$ 100 conviver com o dado ruim.

A leitura mais alinhada é:

a. O data downtime depende apenas do TTR, sendo o TTD irrelevante para o custo do incidente.
*b. A observabilidade ataca diretamente o TTD, reduzindo de dias para minutos o tempo de detecção, e a regra 1-10-100 mostra que prevenir é a opção mais barata.
c. Conviver com o dado ruim em produção é a alternativa mais econômica segundo a regra 1-10-100.
d. Um contrato de dados não teria nenhum efeito sobre mudanças de schema no sistema-fonte.
e. Como o problema é de validade, ele jamais poderia ser detectado por um teste de dados.

### Questão 28 (Interpretação)

**Estímulo:**

> Um e-commerce com faturamento anual de R\$ 80 milhões sofre um vazamento por um bucket mal configurado. A sanção da LGPD é de até 2% do faturamento, limitada a R\$ 50 milhões por infração. A revisão de permissões, mascaramento e auditoria custaria cerca de R\$ 60 mil.

Sobre o teto percentual da multa e a relação custo-benefício da prevenção, a leitura correta é:

a. A multa máxima é fixa em R\$ 1.000, independentemente do faturamento da empresa.
b. Por ser pseudonimizado, o dado sai automaticamente do escopo da LGPD e não há sanção possível.
*c. No teto percentual, a multa pode chegar a R\$ 1,6 milhão (2% de R\$ 80 milhões), cerca de 27 vezes o custo de prevenir — e reputação e churn costumam superar a própria multa.
d. A multa percentual incide sobre o lucro líquido, e não sobre o faturamento da empresa.
e. Prevenir custaria mais caro que pagar a multa, tornando a prevenção economicamente irracional.

### Questão 29 (Interpretação)

**Estímulo:**

> Uma equipe migra de processo manual para CI/CD. Antes: 2 deploys/mês, change failure rate de 30%, correções demoradas. Depois: 20 deploys/mês, change failure rate de 5%, rollback automático que reduz o impacto por incidente. A meta DORA é deploy frequente com baixa taxa de falha.

A leitura mais correta é:

a. O segredo do DataOps é fazer menos deploys para reduzir o risco de falha.
b. Aumentar a frequência de deploy sempre aumenta proporcionalmente a taxa de falha de mudança.
c. CI/CD não tem relação com a confiabilidade do pipeline, apenas com a velocidade.
*d. CI/CD torna o deploy barato e seguro: mais deploys com taxa de falha menor, pois os testes barram o erro no pull request e o rollback reduz o MTTR.
e. A change failure rate é a única métrica DORA relevante, sendo a frequência de deploy irrelevante.

### Questão 30 (Interpretação)

**Estímulo:**

> "A IA generativa não aposentou o engenheiro de dados — fez o oposto. Modelo só é tão bom quanto o pipeline que o alimenta. Tudo o que se aprende em qualidade, linhagem e CI/CD é pré-requisito de MLOps, que monitora data drift e model drift. Feature stores eliminam o training-serving skew servindo a mesma feature, com a mesma lógica, para treino e produção."

A leitura mais alinhada com o encerramento da disciplina é:

a. A IA generativa tornou obsoleto o trabalho de engenharia de dados.
b. MLOps é independente de qualidade, linhagem e CI/CD, sendo uma disciplina sem relação com engenharia de dados.
c. A feature store agrava o training-serving skew ao calcular features de formas diferentes em treino e produção.
d. Modelos de IA produzem bons resultados independentemente da qualidade do pipeline que os alimenta.
*e. A IA amplificou o papel do engenheiro de dados: dado confiável, governado e bem-modelado é pré-requisito de qualquer IA que funcione, e MLOps é o DataOps aplicado ao ciclo de vida do modelo.

---

## Questões discursivas (31–40)

### Questão 31 (Discursiva)

**Contexto:** Uma startup de delivery roda hoje todo o sistema sobre um único PostgreSQL transacional (OLTP), que registra pedidos, pagamentos e entregas. O time de produto começou a pedir relatórios pesados ("faturamento por bairro no trimestre", "produtos mais pedidos por horário") e percebeu que essas consultas deixam o app lento, pois competem com a operação no mesmo banco. Além disso, querem coletar o stream de cliques do app (milhões de eventos/dia).

**Enunciado:** Estruture sua resposta em três partes: (a) **Diagnóstico** — por que rodar análises no banco OLTP de produção é uma má ideia, usando OLTP vs OLAP; (b) **Arquitetura** — descreva um pipeline que separe operação e análise, indicando origem, como o dado se move (ETL/ELT, batch/stream, CDC), onde é armazenado, formato e modelagem; (c) **Tecnologia para o stream de cliques** — que tecnologia recomendaria e por quê, justificando pelo padrão de acesso e pelo teorema CAP.

**Resposta esperada:**

> Resposta de qualidade diagnostica que o PostgreSQL é **OLTP** (escritas/leituras pequenas e rápidas, normalizado), enquanto relatórios são carga **OLAP** (agregam milhões de linhas com `GROUP BY`), que disputa CPU, memória e I/O com a operação e deixa o app lento — daí a necessidade de **separar os dois mundos**. Na arquitetura, espera-se: o dado sai do PostgreSQL via **CDC (Change Data Capture)** ou snapshot, é carregado em um **data warehouse/lakehouse** (BigQuery, Snowflake, Redshift ou lake sobre object storage) no padrão **ELT** (carrega o bruto e transforma no destino), em **formato colunar Parquet**, modelado de forma **dimensional (esquema estrela, fatos e dimensões)** — assim "faturamento por bairro" roda sem tocar a produção. Para o **stream de cliques**, reconhece o padrão de **escrita massiva e contínua**: recomenda **streaming com Apache Kafka** e armazenamento em NoSQL colunar (Cassandra) ou no data lake; pelo **teorema CAP**, prioriza **disponibilidade (AP)** com consistência eventual, pois perder consistência por instantes em uma contagem de cliques é aceitável, mas ficar fora do ar não é. A melhor resposta conecta cada decisão a um conceito (OLTP/OLAP, ELT, CDC, Parquet, modelagem dimensional, CAP) e justifica pelo padrão de acesso, sem "jogar tecnologia".

### Questão 32 (Discursiva)

**Contexto:** Uma fintech precisa construir o pipeline de **transações de cartão** com dois requisitos conflitantes: (1) um sistema **antifraude** que avalia cada transação em menos de 300 ms; (2) um **relatório regulatório diário** entregue ao Banco Central até as 9h, sem duplicatas nem perda de transações.

**Enunciado:** Estruture a resposta em três partes: (a) **Arquitetura de ingestão e processamento** — para cada requisito, escolha batch ou streaming, justifique e nomeie as ferramentas (Kafka, Spark, Airflow) e o papel de cada uma; (b) **Confiabilidade** — qual garantia de entrega no fluxo antifraude e como garantir que o relatório não duplica nem perde transações (cite idempotência/CDC); (c) **Operação** — como orquestrar e monitorar o relatório diário (agendamento, retries, SLA, backfill) para cumprir as 9h mesmo com falhas transitórias.

**Resposta esperada:**

> Resposta de qualidade separa os dois caminhos. Para o **antifraude**, escolhe **streaming com Apache Kafka** (transações como eventos em tópico particionado pela chave do cartão, garantindo ordem por cartão), com processamento em **janelas** (ex.: sliding para detectar N transações em curto intervalo); justifica que batch é inviável pelo limite de 300 ms. Para o **relatório regulatório**, escolhe **batch com Apache Spark** (processamento distribuído do volume diário) **orquestrado pelo Apache Airflow**. Em **confiabilidade**, adota no antifraude **at-least-once com consumo idempotente** (perder transação é pior que checá-la duas vezes; exactly-once é caro e desnecessário se o consumo é idempotente); para o relatório, garante ausência de perda e duplicação via **CDC/ingestão incremental** com **MERGE por chave de transação** ou **sobrescrita de partição por dia** (idempotência ponta a ponta). Em **operação**, descreve um DAG diário com `schedule` cron calculado pelo **caminho crítico** mais os **retries** com backoff, define um **SLA** com margem para entregar antes das 9h, configura **alertas** (e-mail/Slack) em falha e violação de SLA, e usa **backfill** idempotente para reprocessar dias problemáticos. A melhor resposta demonstra pensamento sistêmico (streaming e batch coexistem, arquitetura tipo Lambda/Kappa) e evita "usar Spark para tudo" ou "exactly-once em tudo".

### Questão 33 (Discursiva)

**Contexto:** Você precisa explicar a um time júnior, com exemplos numéricos, **por que o formato colunar (Parquet) é o padrão de analytics** e por que particionar e clusterizar reduzem custo em um data warehouse em nuvem que cobra por dados varridos.

**Enunciado:** Elabore uma explicação técnica que cubra: (a) a diferença entre armazenamento por linha e colunar e por que o colunar vence em OLAP; (b) o efeito da compressão colunar; (c) como **particionamento** (partition pruning) e **clustering** (block pruning) reduzem os bytes varridos; (d) um exemplo numérico ilustrando a economia.

**Resposta esperada:**

> Resposta exemplar explica que o **armazenamento por linha** guarda todos os campos de um registro juntos (ótimo para OLTP, ler/escrever um pedido inteiro), enquanto o **colunar** guarda todos os valores de uma coluna juntos — assim uma consulta analítica como `SELECT SUM(valor)` lê **apenas a coluna `valor`**, ignorando as demais. Sobre **compressão**, destaca que valores de uma mesma coluna são semelhantes, permitindo run-length e dictionary encoding com fatores altos (ex.: 4x a 5x), reduzindo ainda mais o dado lido. Sobre as alavancas de custo: **particionamento** divide a tabela por uma coluna (tipicamente data) e ativa o **partition pruning** (lê só a partição filtrada); **clustering/ordenação** organiza os dados dentro da partição por colunas de filtro frequente e ativa o **block pruning** (pula blocos sem os valores buscados). Espera-se um **exemplo numérico**: por exemplo, uma tabela de 2 TB com 50 colunas em que somar 1 coluna (2% do tamanho) com compressão 4x lê ~10 GB em vez de 2 TB, economizando ordens de grandeza; ou a consulta de 10 TB que cai de US\$ 62,50 (sem partição, `SELECT *`) para frações de centavo (com partição por dia e 1 coluna). A melhor resposta conecta a economia ao modelo de cobrança por dado varrido e cita boas práticas (evitar `SELECT *`, filtrar pela coluna de partição, usar dry run).

### Questão 34 (Discursiva)

**Contexto:** Uma fintech de médio porte mantém todos os dados analíticos em um PostgreSQL transacional que ficou lento: relatórios travam a produção, dados não estruturados (logs, eventos de clique, JSON de APIs de crédito) não cabem bem e o time de ciência de dados reclama da falta de histórico. Orçamento de até R\$ 60 mil/mês (ferramentas + 2 pessoas).

**Enunciado:** Proponha uma **nova arquitetura de dados na nuvem** em três partes: (a) **Arquitetura** — DW, Data Lake ou Lakehouse? Justifique pela variedade de dados e pelos casos de uso (BI + ciência de dados) e indique as camadas; (b) **Modern Data Stack** — escolha ferramentas para ingestão, armazenamento/compute, transformação e BI, justificando; (c) **FinOps** — decisões de modelagem e governança para controlar a fatura, com um TCO estimado.

**Resposta esperada:**

> Resposta de qualidade recomenda **arquitetura Lakehouse** (ou, no mínimo, DW em nuvem + Data Lake), justamente porque há **variedade** (estruturados de crédito + não estruturados como logs/JSON/cliques) e **dois consumidores** (BI exige confiabilidade e esquema; ciência de dados exige flexibilidade e histórico bruto); o Lakehouse sobre object storage barato, com formato de tabela aberto (**Delta ou Iceberg**), atende ambos com **uma cópia única**, organizado pela **arquitetura Medallion** (bronze bruto, silver limpo/conformado, gold curado). Na **Modern Data Stack**: ingestão com **Fivetran ou Airbyte** (conectores prontos), armazenamento/compute com **BigQuery, Snowflake ou Databricks** (separação storage/compute), transformação com **dbt** (modelos versionados, testes, lineage, documentação, materializando silver/gold) e BI com **Power BI, Looker ou Metabase** sobre uma **camada semântica**. Em **FinOps**, cita **formato colunar Parquet**, **particionamento por data** e **clustering**, evitar `SELECT *`, **dry run**, tiering quente/frio no object storage e regras de governança (limites de custo por consulta, painéis por time). Um **TCO** plausível fica em torno de R\$ 15–20 mil/mês de ferramentas + ~R\$ 36 mil/mês de duas pessoas (~R\$ 50–56 mil/mês), dentro do orçamento. A melhor resposta demonstra pensamento de trade-off (comprar vs construir; on-demand vs capacidade reservada) e prioriza entrega incremental, sem "implantar tudo de uma vez".

### Questão 35 (Discursiva)

**Contexto:** Você assumiu como engenheiro(a) de dados de uma *healthtech* de telemedicina. O pipeline ingere **dados sensíveis de saúde**, alimenta dashboards executivos e um modelo de ML que prioriza atendimentos. Hoje **não há testes**, ninguém sabe **de onde vem** cada número, os deploys são **manuais e arriscados**, e a diretoria está preocupada com a **LGPD** após um quase-incidente.

**Enunciado:** Elabore um plano em três partes: (a) **Qualidade e observabilidade** — que dimensões e testes/pilares implementaria primeiro e como mediria o impacto (data downtime, regra 1-10-100); (b) **Governança e LGPD** — como classificaria e protegeria os dados de saúde e qual caminho técnico garantiria o **direito de exclusão** de um paciente; (c) **DataOps** — como tornaria os deploys seguros e frequentes (CI/CD, testes, IaC, write-audit-publish) e qual métrica usaria para provar a melhoria.

**Resposta esperada:**

> Resposta de qualidade integra as quatro aulas da Unidade 4 num plano priorizado. **(1) Qualidade:** começa pelas dimensões mais críticas para saúde — **acurácia, completude e validade** —, escrevendo testes (`not_null` em identificadores/diagnósticos, `accepted_values` em códigos clínicos, faixas válidas em sinais vitais) e ativando observabilidade nos 5 pilares (frescor e volume especialmente); quantifica estimando o **TTD atual** (dias sem monitoração), mostra que observabilidade reduz o TTD a minutos e invoca a **regra 1-10-100** para justificar prevenir. **(2) Governança e LGPD:** classifica os campos (dado de saúde é **sensível**, proteção reforçada), aplica **mascaramento/criptografia** por padrão e **menor privilégio** (RBAC + row/column-level), define **base legal**, e explica que o **direito de exclusão** exige **linhagem completa** para localizar todos os lugares onde o dado do paciente pousou (lake, warehouse, features, backups), com processo automatizado de eliminação/anonimização. **(3) DataOps:** propõe **CI** (linter + testes unitários + testes dbt bloqueando o merge), **CD** (dev → staging → prod), **write-audit-publish** para nunca expor dado clínico intermediário e **IaC (Terraform)** versionando inclusive políticas de acesso e retenção; prova a melhoria com métricas **DORA** (frequência de deploy, change failure rate, MTTR) e TTD/data downtime. A melhor resposta conecta os blocos (qualidade alimenta governança que habilita exclusão; DataOps automatiza e protege tudo) e reconhece que é jornada incremental, priorizando o sensível primeiro.

### Questão 36 (Discursiva)

**Contexto:** Uma empresa quer modelar um **data warehouse** para sua área de vendas e tem dúvidas sobre como tratar atributos de dimensão que mudam ao longo do tempo (por exemplo, quando um cliente muda de cidade), sem corromper relatórios históricos.

**Enunciado:** Explique: (a) a diferença entre **tabela de fatos** e **tabela de dimensão** no esquema estrela; (b) por que se usa **desnormalização** no OLAP, ao contrário do OLTP; (c) o que são **Slowly Changing Dimensions (SCD)** e a diferença entre os Tipos 1 e 2; (d) qual tipo de SCD usaria para preservar a história da cidade do cliente e por quê.

**Resposta esperada:**

> Resposta exemplar define a **tabela de fatos** como o registro dos eventos mensuráveis do negócio (uma linha por venda), com **métricas numéricas** (valor, quantidade) e **chaves estrangeiras** para as dimensões — longa e estreita; e a **tabela de dimensão** como o contexto descritivo (quem, o quê, quando, onde) — curta e larga. Explica que no **OLTP** a **normalização** (3FN) evita redundância e anomalias de atualização, mas no **OLAP** prefere-se a **desnormalização**: juntar dados em poucas tabelas largas reduz joins e acelera a leitura analítica, aceitando redundância em troca de velocidade. Sobre **SCD**, define que tratam mudanças em atributos de dimensão: o **Tipo 1 sobrescreve** o valor (perde a história, fica só o atual); o **Tipo 2 cria uma nova linha** com datas de validade e indicador de "linha atual", preservando a história completa. Para a cidade do cliente, escolhe o **SCD Tipo 2**, pois assim uma venda passada continua atribuída à cidade correta **na época** — sem isso, relatórios históricos por região ficariam errados. A melhor resposta dá um exemplo concreto da nova linha aberta/fechada por data.

### Questão 37 (Discursiva)

**Contexto:** Um data lake da empresa virou um **data swamp**: arquivos sem documentação, sem dono e sem confiabilidade, onde ninguém sabe o que existe nem se pode confiar. A diretoria quer resgatar a confiabilidade sem perder a flexibilidade e o baixo custo do lake.

**Enunciado:** Apresente um plano que cubra: (a) por que um data lake sem disciplina vira data swamp; (b) como **formatos de tabela abertos** (Delta, Iceberg, Hudi) resgatam garantias antes exclusivas do warehouse; (c) o que é a **arquitetura Lakehouse** e a **arquitetura Medallion**; (d) duas medidas de governança para evitar o reaparecimento do swamp.

**Resposta esperada:**

> Resposta de qualidade explica que o data lake armazena dados brutos sobre object storage barato com **schema-on-read** (flexibilidade), mas sem **governança, catálogo e qualidade** vira **data swamp** — depósito de arquivos sem dono, documentação ou confiabilidade. Detalha que **Delta Lake, Apache Iceberg e Apache Hudi** adicionam uma **camada de metadados transacional** sobre os arquivos Parquet, trazendo **transações ACID, time travel, evolução de esquema e MERGE/UPDATE/DELETE** — recursos antes só do DW. Define a **arquitetura Lakehouse** como a união da flexibilidade/custo do lake com a confiabilidade/desempenho do DW, sobre **uma cópia única** (BI, SQL e ML rodam sobre os mesmos dados), e a **arquitetura Medallion** (bronze bruto/auditável → silver limpo/conformado → gold curado), em que o dado ganha qualidade e perde volume a cada camada. Como medidas de governança, cita pelo menos duas: **catálogo de dados** (DataHub, OpenMetadata, Amundsen) com dono e classificação, **linhagem**, **contratos de dados**, controle de acesso por menor privilégio e políticas de retenção/lifecycle. A melhor resposta amarra a Medallion como o equivalente lakehouse das camadas staging/core/marts.

### Questão 38 (Discursiva)

**Contexto:** Um time precisa decidir, para cada um de vários cenários, entre **banco relacional (ACID)** e as famílias **NoSQL**, e ainda entre **processamento batch** e **streaming**, justificando pelo padrão de acesso.

**Enunciado:** Para os cenários a seguir, escolha o modelo de banco mais adequado e justifique: (1) folha de pagamento, onde nenhum centavo pode se perder; (2) cache de sessão de usuário; (3) catálogo de produtos com atributos variáveis; (4) plataforma de IoT com 50.000 sensores escrevendo 1 medição/s cada. Em seguida, explique quando você usaria **batch** e quando usaria **streaming**, conectando a decisão ao custo de esperar.

**Resposta esperada:**

> Resposta de qualidade justifica cada escolha pelo **padrão de acesso**: (1) **folha de pagamento** → **relacional com ACID**, pois exige integridade rígida e atomicidade (transferência toda ou nada); (2) **cache de sessão** → **chave-valor** (Redis), por ser extremamente rápido e o dado ser temporário; (3) **catálogo de produtos** com atributos variáveis → **documento** (MongoDB), por esquema flexível e dados aninhados; (4) **IoT com 50.000 sensores/s** → **NoSQL colunar/coluna larga** (Cassandra), otimizado para escrita massiva com escalabilidade horizontal — espera-se a observação de que um relacional com ACID suportaria ~5–10 mil escritas/s por nó, exigindo vários nós, enquanto o Cassandra absorve a carga em poucos nós. Sobre **batch vs streaming**, explica que **batch** processa lotes finitos (relatórios diários, consolidações), é mais simples e barato, e serve quando o custo de esperar é baixo; **streaming** processa fluxo contínuo quase em tempo real (fraude, recomendação ao vivo, alerta de sensor), quando o custo de esperar é alto. A melhor resposta afirma que a decisão é de negócio ("qual o custo de esperar 1 hora por este dado?") e que relacional e NoSQL convivem em arquiteturas reais.

### Questão 39 (Discursiva)

**Contexto:** Uma equipe de dados faz deploys manuais e arriscados; ninguém ousaria mudar o pipeline de faturamento numa sexta-feira às 17h. A liderança quer transformar deploy assustador em rotina, com a maturidade de um time de desenvolvimento de software.

**Enunciado:** Elabore um plano de **DataOps e CI/CD** cobrindo: (a) os pilares do DataOps e a métrica-norte (DORA); (b) o que versionar (código e dado) e com quais ferramentas; (c) a pirâmide de testes com a camada de testes de dados e a estratégia **write-audit-publish**; (d) o papel da **IaC**; (e) três coisas que tornam um deploy assustador e a prática que neutraliza cada uma.

**Resposta esperada:**

> Resposta exemplar define **DataOps** como DevOps aplicado ao dado, com pilares de **automação ponta a ponta, testes de código E de dado, colaboração e iteração rápida**, e métrica-norte **DORA** (alta frequência de deploy com baixa change failure rate). Sobre **versionamento**, separa **código** (Git: scripts, modelos dbt, DAGs, IaC, com branches/PRs) e **dado** (DVC, lakeFS, time travel de Delta/Iceberg/Hudi para reprodutibilidade e testes seguros). Descreve a **pirâmide de testes** acrescida da camada de **testes de dados** (unitário → integração → testes de dados → end-to-end), sempre validando em **staging com dados sintéticos**, nunca a primeira vez em produção, e detalha o **write-audit-publish** (escreve em tabela temporária → audita com testes → publica só se passar), protegendo o consumidor de dado quebrado. Explica a **IaC** (Terraform/Pulumi) como forma de declarar infraestrutura e governança (políticas de acesso, retenção) em arquivos versionáveis e reproduzíveis. Por fim, lista **três fatores** que tornam o deploy assustador e a cura de cada um: ausência de testes → testes automatizados no CI; ausência de staging → ambiente de staging com dados sintéticos; deploy manual sem rollback → CD com rollback automático. A melhor resposta conclui que a meta é "deploy na sexta às 17h é rotina, não coragem".

### Questão 40 (Discursiva)

**Contexto:** **Projeto integrador.** A direção pediu que você desenhe um **pipeline de dados de ponta a ponta** para um domínio à sua escolha (ex.: e-commerce, saúde, logística), integrando todas as quatro unidades da disciplina.

**Enunciado:** Estruture o projeto em cinco partes, seguindo o pipeline de referência *Fontes → Ingestão → Lake/Warehouse → Transformação → Servir → BI/ML*: (1) **U1** — fonte, caso de uso e decisão batch vs real-time (justifique pelo custo de esperar); (2) **U2** — ingestão (ETL/ELT, CDC, idempotência) e destino (lake/warehouse, formato Parquet/Delta, modelagem dimensional); (3) **U3** — armazenamento e arquitetura (DW, lakehouse, Medallion, Modern Data Stack, dbt/Airflow); (4) **U4** — qualidade (3 testes), governança/LGPD dos campos sensíveis, retenção e CI/CD; (5) síntese de uma página explicando como as peças se conectam.

**Resposta esperada:**

> Resposta exemplar integra **toda a disciplina** num fluxo coerente. **(1) U1:** define a fonte (ex.: app de e-commerce), o caso de uso (ex.: "produtos mais vistos" + previsão de demanda) e a decisão **batch vs real-time** justificada pelo custo de esperar (relatórios diários em batch; recomendação ao vivo em streaming). **(2) U2:** descreve a ingestão no padrão **ELT** com **CDC** do banco OLTP e **idempotência** (MERGE por chave ou sobrescrita de partição), destino em **lake/warehouse** com **Parquet/Delta** e **modelagem dimensional** (fato de vendas + dimensões Tempo, Produto, Cliente, com SCD Tipo 2 onde necessário). **(3) U3:** posiciona a arquitetura como **Lakehouse** com **Medallion** (bronze/silver/gold), montada como **Modern Data Stack** (Fivetran/Airbyte → BigQuery/Snowflake/Databricks → **dbt** → BI), orquestrada por **Airflow** com SLA e backfill. **(4) U4:** define **3 testes de qualidade** (ex.: `not_null` em chave, `unique` em id de pedido, faixa válida em valor), classifica campos sensíveis na **LGPD** com mascaramento/menor privilégio e linhagem para exclusão, define **política de retenção** e o fluxo de **CI/CD** (CI bloqueando merge, CD dev→staging→prod, write-audit-publish, IaC). **(5) Síntese:** mostra como U1–U3 **constroem** o pipeline e U4 o **profissionaliza** (confiável, governado, com deploy seguro), com diagrama de uma página e justificativa. Avaliação: clareza, profundidade técnica, realismo, coerência entre as decisões e integração dos conceitos das 16 aulas, evitando "jogar tecnologia" sem justificar pelo padrão de acesso e pelo trade-off custo/benefício.

---

## Feedbacks (questões objetivas 1–30)

### Questão 1

- **a.** *Correta!* Ambas verdadeiras e a II justifica a I. O ELT carrega o bruto e transforma no destino; a queda do custo de armazenamento e o poder dos warehouses modernos são exatamente o que viabilizou esse padrão e a preservação da fonte da verdade.
- **b.** Incorreta. A Razão **justifica** diretamente a Asserção (explica o porquê econômico do ELT).
- **c.** Incorreta. A Razão é verdadeira: armazenamento barato e warehouses potentes são o motor do ELT.
- **d.** Incorreta. A Asserção é verdadeira: o ELT de fato carrega o bruto e transforma depois, no destino.
- **e.** Incorreta. Ambas são verdadeiras.

### Questão 2

- **a.** Incorreta. A Razão não justifica a Asserção.
- **b.** *Correta!* As duas proposições são verdadeiras: Parquet é colunar/comprimido (padrão OLAP) e o Kafka é um log distribuído e durável. Mas a Razão trata de **streaming/Kafka**, não justifica por que o Parquet é o padrão de analytics — são temas independentes.
- **c.** Incorreta. A Razão é verdadeira: a descrição do Kafka está correta.
- **d.** Incorreta. A Asserção é verdadeira: o Parquet é mesmo colunar e padrão de analytics.
- **e.** Incorreta. Ambas são verdadeiras.

### Questão 3

- **a.** Incorreta. A Razão é falsa.
- **b.** Incorreta. A Razão é falsa.
- **c.** *Correta!* A Asserção é verdadeira (ACID torna o banco confiável para finanças). A Razão é falsa: a **atomicidade** garante que débito e crédito ocorram **juntos, tudo ou nada** — se o sistema cair, **nada** é confirmado; não que apenas o débito persista.
- **d.** Incorreta. A Asserção é verdadeira.
- **e.** Incorreta. A Asserção é verdadeira.

### Questão 4

- **a.** Incorreta. A Asserção é falsa.
- **b.** Incorreta. A Asserção é falsa.
- **c.** Incorreta. A Razão é verdadeira.
- **d.** *Correta!* A Asserção é falsa: o CAP afirma justamente que **não** se pode garantir C, A e P plenamente sob partição. A Razão é verdadeira: como a partição (P) é inevitável, escolhe-se entre **CP** e **AP** durante a falha.
- **e.** Incorreta. A Razão é verdadeira.

### Questão 5

- **a.** Incorreta. Ambas são falsas.
- **b.** Incorreta. Ambas são falsas.
- **c.** Incorreta. A Razão também é falsa.
- **d.** Incorreta. A Asserção também é falsa.
- **e.** *Correta!* As duas são falsas. A Asserção **inverte** os papéis: a **fato** guarda métricas e chaves; as **dimensões** guardam os atributos descritivos. A Razão também é falsa: a modelagem dimensional usa **desnormalização** (esquema estrela), não normalização total à 3FN.

### Questão 6

- **a.** *Correta!* Ambas verdadeiras e a II justifica a I. A idempotência torna retries e backfill seguros precisamente **porque** repetir a operação não altera o estado final nem duplica dados (via MERGE/upsert ou sobrescrita de partição).
- **b.** Incorreta. A Razão justifica diretamente a Asserção.
- **c.** Incorreta. A Razão é verdadeira.
- **d.** Incorreta. A Asserção é verdadeira.
- **e.** Incorreta. Ambas são verdadeiras.

### Questão 7

- **a.** Incorreta. A Razão não justifica a Asserção.
- **b.** *Correta!* Ambas verdadeiras: o shuffle é a operação mais cara do Spark e as transformações são lazy. Mas a Razão (avaliação lazy/Catalyst) **não explica** por que o shuffle é caro — o custo do shuffle vem de serialização, tráfego de rede e escrita em disco, não da preguiça das transformações. São fatos independentes.
- **c.** Incorreta. A Razão é verdadeira.
- **d.** Incorreta. A Asserção é verdadeira.
- **e.** Incorreta. Ambas são verdadeiras.

### Questão 8

- **a.** Incorreta. A Razão é falsa.
- **b.** Incorreta. A Razão é falsa.
- **c.** *Correta!* A Asserção é verdadeira: o Kafka garante ordem **apenas dentro de uma partição** e o offset controla a leitura. A Razão é falsa: **não** há ordenação total entre partições nem offset global do cluster — o offset é sequencial **dentro de cada partição**.
- **d.** Incorreta. A Asserção é verdadeira.
- **e.** Incorreta. A Asserção é verdadeira.

### Questão 9

- **a.** Incorreta. A Asserção é falsa.
- **b.** Incorreta. A Asserção é falsa.
- **c.** Incorreta. A Razão é verdadeira.
- **d.** *Correta!* A Asserção é falsa: exactly-once **não** é simples nem isento de custo — exige produtores idempotentes e transações, com overhead, e não é necessário em todo pipeline. A Razão é verdadeira: **at-least-once + consumo idempotente** é, na prática, mais simples e robusto.
- **e.** Incorreta. A Razão é verdadeira.

### Questão 10

- **a.** Incorreta. Ambas são falsas.
- **b.** Incorreta. Ambas são falsas.
- **c.** Incorreta. A Razão também é falsa.
- **d.** Incorreta. A Asserção também é falsa.
- **e.** *Correta!* As duas são falsas. Um DAG é **acíclico** (Directed Acyclic Graph): nenhuma tarefa pode depender de si mesma. E é justamente a **ausência de ciclos** que garante que o pipeline termine — ciclos poderiam rodar para sempre. A Razão inverte esse princípio.

### Questão 11

- **a.** *Correta!* Ambas verdadeiras e a II justifica a I. O colunar reduz dado varrido e custo **porque** mantém os valores de uma coluna juntos, permitindo ler só as colunas necessárias e comprimir muito bem.
- **b.** Incorreta. A Razão justifica diretamente a Asserção.
- **c.** Incorreta. A Razão é verdadeira.
- **d.** Incorreta. A Asserção é verdadeira.
- **e.** Incorreta. Ambas são verdadeiras.

### Questão 12

- **a.** Incorreta. A Razão não justifica a Asserção.
- **b.** *Correta!* Ambas verdadeiras: formatos abertos trazem ACID e time travel ao lake, e a Medallion organiza o lakehouse em bronze/silver/gold. Mas a Razão (camadas Medallion) **não explica** por que os formatos de tabela trazem ACID — são conceitos complementares, porém independentes.
- **c.** Incorreta. A Razão é verdadeira.
- **d.** Incorreta. A Asserção é verdadeira.
- **e.** Incorreta. Ambas são verdadeiras.

### Questão 13

- **a.** Incorreta. A Razão é falsa.
- **b.** Incorreta. A Razão é falsa.
- **c.** *Correta!* A Asserção é verdadeira: a separação storage/compute permite múltiplos clusters sobre os mesmos dados e cobrança independente. A Razão é falsa: no on-premises, armazenamento e processamento eram **acoplados** (escalar um exigia escalar o outro) — o desacoplamento é justamente a inovação da nuvem.
- **d.** Incorreta. A Asserção é verdadeira.
- **e.** Incorreta. A Asserção é verdadeira.

### Questão 14

- **a.** Incorreta. A Asserção é falsa.
- **b.** Incorreta. A Asserção é falsa.
- **c.** Incorreta. A Razão é verdadeira.
- **d.** *Correta!* A Asserção é falsa: a boa prática é **não** escrever conectores manuais; ferramentas gerenciadas lidam, sim, com schema drift e incrementos. A Razão é verdadeira: Fivetran e Airbyte oferecem conectores prontos que dispensam código de extração.
- **e.** Incorreta. A Razão é verdadeira.

### Questão 15

- **a.** Incorreta. Ambas são falsas.
- **b.** Incorreta. Ambas são falsas.
- **c.** Incorreta. A Razão também é falsa.
- **d.** Incorreta. A Asserção também é falsa.
- **e.** *Correta!* As duas são falsas. Dado **pseudonimizado** continua no escopo da LGPD (a reidentificação ainda é possível com a chave) — só o **anonimizado** sai. E o direito de eliminação **depende de linhagem**: apagar a tabela principal não remove rastros em backups, data lake e features de modelos.

### Questão 16

- **a.** *Correta!* É a leitura central: sem dado confiável e disponível não há ciência de dados, BI nem IA — o engenheiro de dados é a base ("garbage in, garbage out").
- **b.** Incorreta. O texto afirma o oposto: dado ruim produz saída ruim, mesmo com IA moderna.
- **c.** Incorreta. O ditado significa justamente que a saída **depende** da qualidade da entrada.
- **d.** Incorreta. O texto diz que ~80% do esforço é engenharia de dados, não marginal.
- **e.** Incorreta. Dados inconsistentes produzem resultados não confiáveis.

### Questão 17

- **a.** Incorreta. CSV não tem tipos, não comprime e é ineficiente para grandes volumes consultados diariamente.
- **b.** *Correta!* Parquet é colunar e comprimido: lê só as colunas agregadas e comprime muito, ideal para analytics recorrente sobre grandes volumes.
- **c.** Incorreta. JSON é verboso e lento de processar em escala; serve melhor a APIs e dados aninhados.
- **d.** Incorreta. Avro é por linha, ótimo para ingestão/streaming, não para leitura analítica de poucas colunas.
- **e.** Incorreta. O formato influencia diretamente custo e desempenho — é o ponto central da escolha.

### Questão 18

- **a.** Incorreta. Subestima muito a aceleração.
- **b.** Incorreta. Abaixo do valor real.
- **c.** *Correta!* Full = 730.000.000/50.000 = 14.600 s; incremental = 2.000.000/50.000 = 40 s; razão ≈ 365 vezes — coerente com ler só o dia versus o ano inteiro.
- **d.** Incorreta. Abaixo do valor real.
- **e.** Incorreta. Acima do valor real.

### Questão 19

- **a.** Incorreta. Batch diário é incompatível com decisão em menos de 200 ms.
- **b.** Incorreta. OLTP com snapshot periódico não atende latência de tempo real para fraude.
- **c.** Incorreta. Relatórios noturnos em DW são OLAP, não detecção em tempo real.
- **d.** *Correta!* Streaming com Kafka, janelas e at-least-once com consumo idempotente, priorizando disponibilidade (AP), é a combinação adequada a alta vazão, baixa latência e tolerância a perda ocasional.
- **e.** Incorreta. ETL clássico mensal e exactly-once obrigatório não casam com a latência de 200 ms.

### Questão 20

- **a.** Incorreta. O ganho não é linear — a Lei de Amdahl limita o speedup.
- **b.** Incorreta. A fração serial é decisiva: com 15% serial, o ganho fica em ~5,8x com 40 executors e não passa de ~6,7x nem com infinitos nós.
- **c.** Incorreta. O shuffle é a operação **mais cara**; deve ser minimizado, não maximizado.
- **d.** Incorreta. A Lei de Amdahl limita, mas não anula, os benefícios do paralelismo.
- **e.** *Correta!* O paralelismo tem retorno decrescente; reduzir a fração serial (o shuffle) frequentemente rende mais que apenas adicionar executors.

### Questão 21

- **a.** *Correta!* N = 30.000/5.000 = 6 consumidores/partições — o mínimo para acompanhar o fluxo sem acumular lag.
- **b.** Incorreta. 2 partições dariam 10.000 msg/s, abaixo das 30.000 necessárias.
- **c.** Incorreta. Não se cria uma partição por mensagem; a unidade de paralelismo é por capacidade do consumidor.
- **d.** Incorreta. O Kafka não paraleliza automaticamente sem partições suficientes; a partição é o teto do paralelismo de consumo.
- **e.** Incorreta. O cálculo correto é divisão (30.000/5.000), não multiplicação.

### Questão 22

- **a.** Incorreta. 7h50 não cobre o pior caso de 110 min.
- **b.** *Correta!* 8h00 − 110 min = 6h10; agenda-se às 6h00 com SLA de 110 min para ter margem e disparar alerta de violação se atrasar.
- **c.** Incorreta. O Airflow não compensa retries automaticamente sem margem de horário; iniciar às 8h00 estouraria o prazo.
- **d.** Incorreta. Backfill reprocessa períodos passados; não substitui um SLA de entrega no horário.
- **e.** Incorreta. 4h00 sem SLA e sem retries não é coerente com observabilidade e resiliência.

### Questão 23

- **a.** Incorreta. Particionar e selecionar colunas **reduz** os bytes varridos via pruning.
- **b.** Incorreta. `SELECT *` em colunar é caro: lê todas as colunas, maximizando o custo.
- **c.** *Correta!* Partition pruning (lê só o dia) + seleção de poucas colunas reduz os bytes varridos em ordens de grandeza, derrubando o custo de dezenas de dólares para frações de centavo.
- **d.** Incorreta. Triplicar a tabela aumenta o custo de armazenamento sem reduzir o varrido por consulta.
- **e.** Incorreta. OLTP por linha é ruim para consultas analíticas agregadas.

### Questão 24

- **a.** Incorreta. O "E" (extração) é função de ferramentas como Fivetran/Airbyte, não do dbt.
- **b.** Incorreta. O "L" (carga) também é da ingestão gerenciada, não do dbt.
- **c.** Incorreta. O dbt não é ferramenta de BI; quem entrega dashboards é Looker, Power BI, Metabase.
- **d.** *Correta!* O dbt é o "T" (transformação): materializa silver/gold (ou data marts) no warehouse via SQL, com testes, lineage e documentação versionados.
- **e.** Incorreta. O dbt não substitui o Airflow; a orquestração permanece com Airflow/Dagster.

### Questão 25

- **a.** Incorreta. A linhagem tem utilidade operacional central (impacto, causa-raiz, conformidade).
- **b.** Incorreta. Impacto (jusante) e causa-raiz (montante) são perguntas **opostas**, não a mesma.
- **c.** Incorreta. Linhagem é necessária em batch e em streaming.
- **d.** Incorreta. A linhagem é justamente o que viabiliza a exclusão exigida pela LGPD.
- **e.** *Correta!* A linhagem habilita análise de impacto e de causa-raiz e é pré-requisito para localizar todos os lugares onde um dado pessoal pousou, permitindo a exclusão exigida pela LGPD.

### Questão 26

- **a.** *Correta!* Testes barram o erro antecipado na porta; observabilidade detecta o imprevisto monitorando frescor, volume, distribuição, esquema e linhagem ao longo do tempo — são complementares.
- **b.** Incorreta. Não são sinônimos: um cobre o previsto; o outro, o imprevisto.
- **c.** Incorreta. Ambos servem batch e streaming.
- **d.** Incorreta. Testes não tornam a observabilidade desnecessária; as duas se complementam.
- **e.** Incorreta. Os cinco pilares dizem respeito à **saúde do dado**, não ao controle de acesso.

### Questão 27

- **a.** Incorreta. O data downtime depende de TTD **e** TTR (data downtime = nº de incidentes × (TTD + TTR)).
- **b.** *Correta!* A observabilidade reduz o TTD (de dias para minutos), e a regra 1-10-100 mostra que prevenir é o mais barato.
- **c.** Incorreta. Conviver com dado ruim é a opção mais cara (R\$ 100), não a mais econômica.
- **d.** Incorreta. Um contrato de dados disciplina e versiona mudanças de schema na origem, evitando quebras silenciosas.
- **e.** Incorreta. Um teste de validade (faixa de renda) detectaria exatamente esse problema no primeiro dia.

### Questão 28

- **a.** Incorreta. A multa não é fixa em R\$ 1.000; é percentual sobre o faturamento.
- **b.** Incorreta. Pseudonimização **não** retira o dado do escopo da LGPD (só a anonimização retira).
- **c.** *Correta!* No teto percentual, 2% de R\$ 80 milhões = R\$ 1,6 milhão (limitado a R\$ 50 mi/infração), ~27× o custo de prevenir; reputação e churn costumam superar a multa.
- **d.** Incorreta. A sanção percentual da LGPD incide sobre o **faturamento**, não sobre o lucro líquido.
- **e.** Incorreta. Prevenir (~R\$ 60 mil) é muito mais barato que a multa e o estrago de reputação.

### Questão 29

- **a.** Incorreta. O segredo é tornar o deploy **barato e seguro**, não fazer menos deploys.
- **b.** Incorreta. Com testes e rollback, mais deploys vêm com **menor** taxa de falha, não maior.
- **c.** Incorreta. CI/CD aumenta confiabilidade (barra erros, habilita rollback), não só velocidade.
- **d.** *Correta!* CI/CD deixa o deploy barato e seguro: mais deploys com menor taxa de falha, pois o CI barra o erro no pull request e o rollback automático reduz o MTTR.
- **e.** Incorreta. Frequência de deploy é métrica DORA central, junto com change failure rate e MTTR.

### Questão 30

- **a.** Incorreta. A IA generativa amplificou (não tornou obsoleto) o papel do engenheiro de dados.
- **b.** Incorreta. MLOps **depende** de qualidade, linhagem e CI/CD — é o DataOps aplicado ao modelo.
- **c.** Incorreta. A feature store **elimina** o training-serving skew servindo a mesma feature/lógica em treino e produção.
- **d.** Incorreta. Modelo é tão bom quanto o pipeline que o alimenta ("garbage in, garbage out").
- **e.** *Correta!* A IA amplificou o papel do engenheiro de dados: dado confiável, governado e bem-modelado é pré-requisito de qualquer IA, e MLOps é o DataOps aplicado ao ciclo de vida do modelo (com monitoração de data/model drift).
