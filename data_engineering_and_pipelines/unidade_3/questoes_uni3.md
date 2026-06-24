# Questionário — Unidade 3

- **Disciplina:** Data Engineering and Pipelines
- **Professor-conteudista:** Afonso Cesar Lelis Brandão

## Orientações

- **20 questões** padrão ENADE: **10 asserção-razão** + **10 de interpretação**.
- Cada questão tem **5 alternativas (a–e)**; a correta é prefixada por `*` (ex.: `*c. ...`).
- Distribuição da alternativa correta: rotação **a, b, c, d, e, a, b, c, d, e...** (4 questões para cada letra).

---

## Questões

### Questão 1 (Asserção-Razão)

> **Asserção I:** O Data Warehouse adota armazenamento colunar para acelerar consultas analíticas (OLAP), reduzindo drasticamente o volume de dados varridos e o custo de cada consulta.
>
> **porque**
>
> **Razão II:** Em uma consulta de agregação como `SELECT SUM(valor) FROM vendas`, o formato colunar lê apenas a coluna requerida e aproveita a semelhança dos valores de uma mesma coluna para aplicar alta compressão (run-length e dictionary encoding).

A respeito dessas asserções, assinale a opção correta:

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 2 (Asserção-Razão)

> **Asserção I:** A arquitetura Lakehouse consegue rodar BI, SQL ad hoc e treino de modelos de machine learning sobre uma cópia única dos dados, sem manter um Data Lake e um Data Warehouse separados.
>
> **porque**
>
> **Razão II:** O Apache Iceberg, formato de tabela aberto originado no Netflix, oferece evolução de esquema e de partição, além de snapshots, sendo neutro em relação à engine de processamento.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 3 (Asserção-Razão)

> **Asserção I:** Na separação entre armazenamento e computação dos Data Warehouses em nuvem, múltiplos clusters podem ler os mesmos dados sem competir por recursos, e armazenamento e processamento são cobrados de forma independente.
>
> **porque**
>
> **Razão II:** No modelo de cobrança on-demand do BigQuery, paga-se por hora de cluster provisionado, independentemente da quantidade de bytes que a consulta efetivamente varre.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 4 (Asserção-Razão)

> **Asserção I:** A arquitetura Inmon parte de data marts dimensionais independentes por área, construídos com esquema estrela, sem qualquer camada corporativa integrada e normalizada.
>
> **porque**
>
> **Razão II:** A arquitetura Inmon é top-down e propõe primeiro um Data Warehouse corporativo único e normalizado (3FN), que só depois alimenta os data marts — sendo a abordagem bottom-up por marts dimensionais característica de Kimball.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 5 (Asserção-Razão)

> **Asserção I:** Um Data Lake garante automaticamente governança, catálogo e qualidade dos dados, de modo que jogar qualquer arquivo bruto no repositório nunca traz riscos de virar um data swamp.
>
> **porque**
>
> **Razão II:** O formato Apache Parquet, por si só, já implementa transações ACID, time travel e operações `MERGE`/`UPDATE`/`DELETE` sobre os arquivos, dispensando qualquer formato de tabela aberto como Delta, Iceberg ou Hudi.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

### Questão 6 (Asserção-Razão)

> **Asserção I:** Na arquitetura Medallion, o dado flui de bronze para gold ganhando qualidade e perdendo volume a cada etapa, até chegar a tabelas agregadas e modeladas prontas para BI e features de ML.
>
> **porque**
>
> **Razão II:** A camada bronze guarda os dados brutos como chegaram da fonte (histórico fiel e auditável), a silver entrega dados limpos, deduplicados e conformados, e a gold consolida dados curados para consumo direto do negócio.

A respeito dessas asserções, assinale a opção correta:

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 7 (Asserção-Razão)

> **Asserção I:** O dbt (data build tool) traz práticas de engenharia de software para a transformação de dados, com modelos versionados em Git, lineage automático, testes declarativos e documentação gerada.
>
> **porque**
>
> **Razão II:** O Fivetran é uma ferramenta SaaS de ingestão gerenciada que oferece centenas de conectores prontos e sincronização incremental, cobrando por MAR (Monthly Active Rows).

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 8 (Asserção-Razão)

> **Asserção I:** O particionamento por uma coluna de data, combinado com clustering pelas colunas de filtro frequente, ativa o partition pruning e o block pruning, reduzindo drasticamente os bytes varridos por uma consulta.
>
> **porque**
>
> **Razão II:** O comando `SELECT *` em um Data Warehouse colunar é a forma mais econômica de consulta, pois ler todas as colunas garante o melhor aproveitamento da compressão colunar e o menor custo por consulta.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 9 (Asserção-Razão)

> **Asserção I:** O data mesh é apenas mais uma ferramenta de software que substitui o dbt e o Fivetran, instalada para centralizar todos os dados da empresa em um único time de dados.
>
> **porque**
>
> **Razão II:** O data mesh é um paradigma organizacional que descentraliza a responsabilidade pelos dados, apoiado nos princípios de propriedade orientada a domínio, dados como produto, plataforma self-service e governança federada computacional.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 10 (Asserção-Razão)

> **Asserção I:** Em uma tabela fato de um esquema estrela devem ser guardados os atributos descritivos (nome do produto, cidade do cliente, nome da loja), enquanto as tabelas dimensão guardam exclusivamente as métricas numéricas como quantidade e valor.
>
> **porque**
>
> **Razão II:** O armazenamento por linha (row-oriented) é o mais indicado para consultas analíticas OLAP que agregam grandes volumes, ao passo que o armazenamento colunar é o mais indicado para o OLTP de muitas escritas pequenas em um único registro.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

### Questão 11 (Interpretação)

**Estímulo:**

> Uma tabela de eventos tem **10 TB**, particionada por dia, com 365 dias de dados (~27,4 GB/dia). Sem particionamento e com `SELECT *`, uma consulta varre os 10 TB e custa, a US\$ 6,25 por TB, cerca de **US\$ 62,50**. Com particionamento por dia e seleção de apenas 1 das 50 colunas, a mesma consulta varre uma fração mínima e custa cerca de **US\$ 0,0034**.

Considerando os conceitos da Unidade 3, qual leitura é **mais adequada**?

*a. Modelagem física (particionamento, clustering) e disciplina de SQL (selecionar só as colunas necessárias, filtrar pela coluna de partição) podem alterar o custo da mesma consulta em ordens de grandeza, tornando otimização e FinOps parte do trabalho do engenheiro de dados.
b. O custo da consulta depende apenas do preço por TB cobrado pela plataforma, sendo impossível ao engenheiro influenciá-lo por meio de modelagem ou SQL.
c. A diferença de custo é desprezível e não justifica esforço de particionamento ou clustering.
d. Para baratear a consulta, a melhor estratégia é sempre usar `SELECT *` em colunar, pois ler tudo evita reprocessamentos.
e. O particionamento só funciona em bancos transacionais OLTP por linha, não em Data Warehouses colunares.

### Questão 12 (Interpretação)

**Estímulo:**

> Comparação de custo para guardar 100 TB de histórico por um ano: em Data Warehouse na nuvem com armazenamento gerenciado (~R\$ 100,00 por TB/mês), o custo chega a R\$ 120.000,00/ano. Em Lakehouse sobre object storage com tiering quente/frio (20% quente a ~R\$ 120,00/TB-mês e 80% frio a ~R\$ 6,00/TB-mês), o custo cai para cerca de R\$ 34.560,00/ano.

A conclusão **mais bem suportada** pelos dados é:

a. Manter todo o histórico no armazenamento gerenciado do DW é sempre a opção mais barata.
*b. Manter o histórico bruto em object storage barato, com tiering quente/frio, reduz drasticamente o custo de armazenamento (~70%) — esse é o argumento econômico central do Lakehouse.
c. Object storage é tecnicamente inviável para guardar dados históricos em volume.
d. O tiering quente/frio aumenta o custo, pois exige duas cópias completas dos dados.
e. A economia obtida é irrelevante diante do custo de processamento das consultas.

### Questão 13 (Interpretação)

**Estímulo:**

A tabela compara três Data Warehouses em nuvem:

| Atributo | BigQuery (Google) | Snowflake | Redshift (AWS) |
| --- | --- | --- | --- |
| Modelo | Serverless puro | Virtual warehouses | Clusters provisionados + Serverless |
| Nuvem | Google Cloud | Multi-cloud (AWS, Azure, GCP) | AWS |

Uma empresa que **quer um DW serverless puro, sem clusters a gerenciar e com escala automática**, deve preferir:

a. Redshift, pela integração nativa com o ecossistema AWS.
b. Snowflake, pela disponibilidade multi-cloud.
*c. BigQuery, por ser serverless puro, sem infraestrutura a administrar e com escala automática.
d. Qualquer banco transacional OLTP por linha.
e. Nenhum dos três, pois DW em nuvem não oferece modelo serverless.

### Questão 14 (Interpretação)

**Estímulo:**

> "Logs de servidores, JSON de APIs, imagens, áudios, sensores de IoT: nada disso cabe bem em colunas e linhas pré-definidas. O Data Warehouse clássico sofre com esquema rígido (schema-on-write), custo de armazenamento alto e variedade limitada — justamente os dados 'difíceis' que mais interessam à ciência de dados e ao machine learning."

A leitura **mais correta** do texto é:

a. O Data Warehouse clássico acolhe igualmente bem dados estruturados e não estruturados, sem qualquer limitação.
b. Dados não estruturados não têm valor e devem ser descartados.
c. O schema-on-write torna o DW a melhor opção para dados que mudam de forma com frequência.
*d. Os limites do DW clássico (schema-on-write, custo alto, baixa variedade) motivam o uso de repositórios como o Data Lake, com schema-on-read, para acolher dados brutos e variados que alimentam ciência de dados e ML.
e. A solução para o problema é migrar todos os dados não estruturados para um banco transacional OLTP por linha.

### Questão 15 (Interpretação)

**Estímulo:**

> Uma rede de varejo precisa preservar o histórico de endereço dos clientes para análise temporal correta: quando um cliente muda de cidade, é preciso saber em que cidade ele estava em cada venda passada, sem perder o registro anterior.

A estratégia de modelagem **mais adequada** para essa dimensão é:

a. SCD Tipo 1 (sobrescrever o valor antigo), pois manter histórico é desnecessário em análise temporal.
b. Eliminar a dimensão Cliente e guardar a cidade diretamente na tabela fato sem dimensão.
c. Converter a tabela fato em um banco OLTP por linha para suportar a mudança.
d. Usar exclusivamente esquema floco de neve, que dispensa o tratamento de mudanças de dimensão.
*e. SCD Tipo 2 (criar um novo registro preservando o histórico), de modo que cada venda possa ser associada à cidade vigente no momento, mantendo a análise temporal correta.

### Questão 16 (Interpretação)

**Estímulo:**

> "Dois relatórios mostram 'receita' com números diferentes porque cada analista calculou à sua maneira."

Na Modern Data Stack, o recurso que **melhor resolve** esse problema é:

*a. A camada semântica, que define métricas e dimensões de forma centralizada e única — "receita líquida" é definida uma vez e todas as ferramentas de BI consomem a mesma definição.
b. Criar mais relatórios paralelos para "ter mais fontes de comparação".
c. Migrar todos os dados para planilhas individuais por analista.
d. Trocar o Data Warehouse por um banco transacional OLTP.
e. Desativar a governança de dados, já que ela é a causa das divergências.

### Questão 17 (Interpretação)

**Estímulo:**

> "A Modern Data Stack é modular, SaaS, em nuvem e centrada no warehouse/lakehouse. O fio condutor é o ELT: primeiro carrega o dado bruto no DW barato e elástico, e só depois transforma lá dentro com SQL."

A leitura **mais coerente** com o texto é:

a. A MDS é uma plataforma monolítica única que dispensa qualquer integração entre ferramentas.
*b. A MDS compõe a stack com a melhor ferramenta de cada categoria (ingestão, armazenamento, transformação, BI, observabilidade), seguindo o padrão ELT — carrega o bruto primeiro e transforma dentro do DW.
c. A MDS segue o ETL clássico, transformando o dado antes de carregá-lo no DW.
d. A MDS elimina a necessidade de armazenamento, pois processa tudo apenas em memória.
e. A MDS é incompatível com Data Warehouses em nuvem e exige servidores on-premises.

### Questão 18 (Interpretação)

**Estímulo:**

| Formato | Origem | Destaque |
| --- | --- | --- |
| Delta Lake | Databricks | ACID, time travel, `MERGE`, forte no Spark |
| Apache Iceberg | Netflix | Evolução de esquema/partição, neutro em engine |
| Apache Hudi | Uber | Upserts eficientes, ingestão incremental, foco em CDC |

Uma equipe precisa de **upserts eficientes e ingestão incremental para um pipeline de CDC (Change Data Capture)**. O formato **mais alinhado** a esse requisito é:

a. Delta Lake, por ser exclusivo de cargas batch sem suporte a atualização.
b. Apache Iceberg, por não permitir evolução de esquema.
*c. Apache Hudi, projetado para upserts eficientes e ingestão incremental, com foco em CDC.
d. Apache Parquet puro, que já oferece transações ACID nativas para CDC.
e. Nenhum formato de tabela aberto suporta CDC; é preciso usar um DW gerenciado.

### Questão 19 (Interpretação)

**Estímulo:**

> Estimativa de TCO mensal de uma Modern Data Stack de médio porte: ferramentas (Fivetran, BigQuery, dbt Cloud, Power BI, Monte Carlo) somam R\$ 17.000,00/mês; somam-se 1 engenheiro de dados + 1 analytics engineer a ~R\$ 18.000,00/mês de custo total cada.

O TCO **mensal** aproximado da stack é:

a. R\$ 17.000,00.
b. R\$ 36.000,00.
c. R\$ 44.000,00.
*d. R\$ 53.000,00.
e. R\$ 636.000,00.

> **Cálculo:** ferramentas R\$ 17.000 + pessoas (2 × R\$ 18.000 = R\$ 36.000) = R\$ 53.000/mês. O valor de R\$ 636.000 corresponde ao TCO anual (R\$ 53.000 × 12).

### Questão 20 (Interpretação)

**Estímulo:**

> Uma fintech tem todos os dados analíticos em um PostgreSQL transacional: relatórios pesados travam a produção, dados não estruturados (logs, eventos de clique, JSON de APIs de crédito) não cabem bem e o time de ciência de dados reclama da falta de histórico. Há dois consumidores: BI (exige confiabilidade e esquema) e ciência de dados (exige flexibilidade e histórico bruto).

A arquitetura **mais adequada** para esse cenário é:

a. Manter tudo no PostgreSQL transacional, apenas adicionando índices, pois ele atende igualmente BI e ciência de dados.
b. Adotar somente um Data Warehouse clássico com schema-on-write, descartando os dados não estruturados.
c. Migrar para planilhas em object storage, eliminando a necessidade de banco de dados.
d. Adotar somente um Data Lake sem governança, jogando todos os dados brutos sem catálogo nem camadas.
*e. Adotar uma arquitetura Lakehouse sobre object storage com formato de tabela aberto (Delta ou Iceberg) e camadas Medallion (bronze/silver/gold), atendendo BI e ciência de dados com uma cópia única, confiável e flexível.

## Feedbacks

### Questão 1

- **a.** *Correta!* Ambas verdadeiras e a II justifica a I. O DW de fato usa colunar para OLAP; a Razão explica diretamente **por que** o colunar acelera e barateia: lê só a coluna necessária e comprime muito (run-length, dictionary encoding).
- **b.** Incorreta. A Razão justifica diretamente a Asserção.
- **c.** Incorreta. A Razão é verdadeira.
- **d.** Incorreta. A Asserção é verdadeira.
- **e.** Incorreta. Ambas são verdadeiras.

### Questão 2

- **a.** Incorreta. A Razão não justifica a Asserção — descreve um formato específico, não o motivo da cópia única.
- **b.** *Correta!* As duas proposições são verdadeiras: o Lakehouse roda BI, SQL e ML sobre uma cópia única; e o Iceberg, originado no Netflix, oferece evolução de esquema/partição, snapshots e neutralidade de engine. Mas a Razão descreve **um** formato de tabela aberto, não explica **por que** o Lakehouse dispensa cópias duplicadas — são informações independentes.
- **c.** Incorreta. A Razão é verdadeira.
- **d.** Incorreta. A Asserção é verdadeira.
- **e.** Incorreta. Ambas são verdadeiras.

### Questão 3

- **a.** Incorreta. A Razão é falsa.
- **b.** Incorreta. A Razão é falsa.
- **c.** *Correta!* A Asserção é verdadeira: a separação storage/compute permite múltiplos clusters lendo os mesmos dados sem conflito e cobrança independente. A Razão é falsa: no modelo **on-demand** do BigQuery cobra-se por **TB varrido** (bytes lidos), não por hora de cluster provisionado — esse último é o modelo de slots/capacidade reservada.
- **d.** Incorreta. A Asserção é verdadeira.
- **e.** Incorreta. A Asserção é verdadeira.

### Questão 4

- **a.** Incorreta. A Asserção é falsa.
- **b.** Incorreta. A Asserção é falsa.
- **c.** Incorreta. A Razão é verdadeira.
- **d.** *Correta!* A Asserção é falsa: a descrição (data marts dimensionais independentes, bottom-up, esquema estrela) é de **Kimball**, não de Inmon. A Razão descreve corretamente Inmon: top-down, DW corporativo único e normalizado (3FN) que depois alimenta os marts.
- **e.** Incorreta. A Razão é verdadeira.

### Questão 5

- **a.** Incorreta. Ambas são falsas.
- **b.** Incorreta. Ambas são falsas.
- **c.** Incorreta. A Razão também é falsa.
- **d.** Incorreta. A Asserção também é falsa.
- **e.** *Correta!* As duas proposições são falsas. Um Data Lake **não** garante governança automaticamente: sem catálogo, qualidade e disciplina, vira **data swamp**. E o Parquet **não** implementa ACID/time travel/`MERGE` por si só — essas garantias vêm dos **formatos de tabela abertos** (Delta, Iceberg, Hudi) construídos por cima dos arquivos.

### Questão 6

- **a.** *Correta!* Ambas verdadeiras e a II justifica a I. O dado flui de bronze a gold ganhando qualidade; a Razão detalha exatamente **o que** cada camada faz (bronze bruto/auditável, silver limpo/conformado, gold curado), justificando por que o volume cai e a qualidade sobe.
- **b.** Incorreta. A Razão justifica diretamente a Asserção.
- **c.** Incorreta. A Razão é verdadeira.
- **d.** Incorreta. A Asserção é verdadeira.
- **e.** Incorreta. Ambas são verdadeiras.

### Questão 7

- **a.** Incorreta. A Razão não justifica a Asserção — trata de outra camada da stack.
- **b.** *Correta!* As duas proposições são verdadeiras: o dbt traz versionamento, lineage, testes e documentação à transformação; e o Fivetran é SaaS de ingestão com conectores prontos cobrando por MAR. Mas a Razão fala da **ingestão** (Fivetran), não justifica as práticas de engenharia de software do **dbt** (transformação) — são camadas distintas da MDS, independentes entre si.
- **c.** Incorreta. A Razão é verdadeira.
- **d.** Incorreta. A Asserção é verdadeira.
- **e.** Incorreta. Ambas são verdadeiras.

### Questão 8

- **a.** Incorreta. A Razão é falsa.
- **b.** Incorreta. A Razão é falsa.
- **c.** *Correta!* A Asserção é verdadeira: particionamento (partition pruning) + clustering (block pruning) reduzem muito os bytes varridos. A Razão é falsa: `SELECT *` em colunar é o **oposto** de econômico — cada coluna lida custa, e selecionar tudo maximiza os bytes varridos e a fatura.
- **d.** Incorreta. A Asserção é verdadeira.
- **e.** Incorreta. A Asserção é verdadeira.

### Questão 9

- **a.** Incorreta. A Asserção é falsa.
- **b.** Incorreta. A Asserção é falsa.
- **c.** Incorreta. A Razão é verdadeira.
- **d.** *Correta!* A Asserção é falsa: o data mesh **não** é uma ferramenta nem substitui dbt/Fivetran, e propõe **descentralizar** (não centralizar) a propriedade dos dados. A Razão descreve corretamente o data mesh como paradigma organizacional com seus quatro princípios (domínio, dado como produto, self-service, governança federada).
- **e.** Incorreta. A Razão é verdadeira.

### Questão 10

- **a.** Incorreta. Ambas são falsas.
- **b.** Incorreta. Ambas são falsas.
- **c.** Incorreta. A Razão também é falsa.
- **d.** Incorreta. A Asserção também é falsa.
- **e.** *Correta!* As duas proposições são falsas. Na modelagem dimensional os papéis são **invertidos** no enunciado: a **fato** guarda as métricas + chaves estrangeiras, e as **dimensões** guardam os atributos descritivos. E a Razão inverte o uso dos formatos: o **colunar** é ideal para OLAP analítico (agregações em grande volume) e o **por linha** para OLTP de muitas escritas pequenas.

### Questão 11

- **a.** *Correta!* O caso mostra a mesma consulta variando de US\$ 62,50 para ~US\$ 0,0034 conforme a modelagem física e o SQL — exatamente o ponto da Aula 11: otimização e FinOps são parte do trabalho do engenheiro de dados.
- **b.** Incorreta. O engenheiro influencia o custo fortemente via particionamento, clustering e seleção de colunas.
- **c.** Incorreta. A diferença chega a ordens de grandeza (~18.000×), longe de desprezível.
- **d.** Incorreta. `SELECT *` em colunar **aumenta** o custo, não o reduz.
- **e.** Incorreta. Particionamento é técnica central justamente em DWs colunares na nuvem.

### Questão 12

- **a.** Incorreta. O armazenamento gerenciado do DW sai bem mais caro (R\$ 120 mil vs R\$ 34 mil/ano).
- **b.** *Correta!* O object storage barato com tiering quente/frio reduz o custo de armazenamento em ~70% — é o argumento econômico central do Lakehouse, mantendo o histórico bruto no storage e reservando o DW/gold para o que precisa de desempenho.
- **c.** Incorreta. Object storage (S3/GCS) é precisamente a base de Data Lakes e Lakehouses para grandes volumes.
- **d.** Incorreta. O tiering reduz o custo ao mover dados frios para classe mais barata; não exige cópias duplicadas.
- **e.** Incorreta. A economia de ~70% no armazenamento é significativa e é o cerne do argumento.

### Questão 13

- **a.** Incorreta. Redshift se destaca pela integração com AWS, não por ser serverless puro.
- **b.** Incorreta. Snowflake usa virtual warehouses e brilha pelo multi-cloud, não pelo serverless puro.
- **c.** *Correta!* O BigQuery é serverless puro: sem clusters a gerenciar, escala automática e zero administração de infraestrutura — exatamente o requisito do enunciado.
- **d.** Incorreta. Banco OLTP por linha é inadequado para consultas analíticas.
- **e.** Incorreta. DWs em nuvem oferecem modelos serverless; o BigQuery é o exemplo.

### Questão 14

- **a.** Incorreta. O DW clássico justamente **não** acolhe bem dados não estruturados.
- **b.** Incorreta. Dados não estruturados são os mais valiosos para ciência de dados e ML.
- **c.** Incorreta. O schema-on-write penaliza dados que mudam de forma; é uma limitação, não vantagem.
- **d.** *Correta!* Os limites do DW (schema-on-write, custo alto, baixa variedade) motivam o Data Lake com schema-on-read, que acolhe dados brutos e variados para ciência de dados e ML.
- **e.** Incorreta. Banco OLTP por linha não resolve o problema de variedade e volume desses dados.

### Questão 15

- **a.** Incorreta. SCD Tipo 1 sobrescreve e **perde** o histórico, inviabilizando a análise temporal correta.
- **b.** Incorreta. Eliminar a dimensão e colocar a cidade na fato quebra a modelagem dimensional e não preserva contexto histórico.
- **c.** Incorreta. Migrar para OLTP por linha não tem relação com o tratamento de mudança de dimensão.
- **d.** Incorreta. O floco de neve é apenas uma normalização da dimensão; não dispensa o tratamento de SCD.
- **e.** *Correta!* SCD Tipo 2 cria um novo registro preservando o histórico, permitindo associar cada venda à cidade vigente naquele momento — a escolha indicada para análise temporal correta.

### Questão 16

- **a.** *Correta!* A camada semântica define métricas e dimensões de forma centralizada e única, garantindo uma fonte única da verdade para os números e eliminando definições divergentes entre relatórios.
- **b.** Incorreta. Mais relatórios paralelos **agravam** a divergência.
- **c.** Incorreta. Planilhas individuais aumentam a inconsistência, não a resolvem.
- **d.** Incorreta. O problema é de definição de métrica, não de tipo de banco; OLTP não resolve.
- **e.** Incorreta. Governança é parte da solução; desativá-la pioraria o caos.

### Questão 17

- **a.** Incorreta. A MDS é justamente modular, não monolítica, e depende de integração entre ferramentas.
- **b.** *Correta!* A MDS compõe a melhor ferramenta por categoria (ingestão, armazenamento, transformação, BI, observabilidade) seguindo o ELT — carrega o bruto no DW e transforma depois lá dentro.
- **c.** Incorreta. A MDS segue ELT (transforma depois), não o ETL clássico (transforma antes).
- **d.** Incorreta. A MDS é centrada no DW/Lakehouse; não elimina o armazenamento.
- **e.** Incorreta. A MDS é, por definição, em nuvem e centrada em DWs/Lakehouses na nuvem.

### Questão 18

- **a.** Incorreta. O Delta Lake suporta `MERGE`/upserts; a afirmação de que é só batch sem atualização é falsa.
- **b.** Incorreta. O Iceberg **permite** evolução de esquema; a justificativa está errada.
- **c.** *Correta!* O Apache Hudi (origem Uber) é projetado para upserts eficientes e ingestão incremental, com foco em CDC — exatamente o requisito.
- **d.** Incorreta. Parquet puro **não** oferece ACID nativo; isso vem dos formatos de tabela abertos.
- **e.** Incorreta. Os formatos de tabela abertos (Delta, Iceberg, Hudi) suportam CDC; não é necessário um DW gerenciado.

### Questão 19

- **a.** Incorreta. R\$ 17.000 é apenas o custo das ferramentas, sem as pessoas.
- **b.** Incorreta. R\$ 36.000 é apenas o custo das duas pessoas, sem as ferramentas.
- **c.** Incorreta. Soma incorreta dos componentes.
- **d.** *Correta!* TCO mensal = ferramentas (R\$ 17.000) + pessoas (2 × R\$ 18.000 = R\$ 36.000) = R\$ 53.000/mês.
- **e.** Incorreta. R\$ 636.000 é o TCO **anual** (R\$ 53.000 × 12), não o mensal.

### Questão 20

- **a.** Incorreta. O PostgreSQL transacional já trava com relatórios pesados e não acolhe dados não estruturados; índices não resolvem.
- **b.** Incorreta. O DW clássico com schema-on-write descartaria os dados não estruturados valiosos para a ciência de dados.
- **c.** Incorreta. Planilhas não oferecem confiabilidade, escala nem governança para esse cenário.
- **d.** Incorreta. Um Data Lake sem governança vira data swamp, sem confiabilidade para o BI.
- **e.** *Correta!* O Lakehouse sobre object storage, com formato de tabela aberto (Delta/Iceberg) e camadas Medallion (bronze/silver/gold), atende tanto o BI (confiabilidade, esquema) quanto a ciência de dados (flexibilidade, histórico bruto) com uma cópia única.
