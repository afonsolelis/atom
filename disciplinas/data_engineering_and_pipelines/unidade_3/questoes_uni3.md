# Questionário — Unidade 3

- **Disciplina:** Data Engineering and Pipelines
- **Professor-conteudista:** Afonso Cesar Lelis Brandão

## Orientações

- **40 questões** padrão ENADE: **20 asserção-razão** + **20 de interpretação**.
- Cada questão tem **5 alternativas (a–e)**; a correta é prefixada por `*` (ex.: `*c. ...`).
- Distribuição da alternativa correta: rotação **a, b, c, d, e, a, b, c, d, e...** (8 questões para cada letra).

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

### Questão 21 (Asserção-Razão)

> **Asserção I:** Segundo a definição clássica de Bill Inmon, um Data Warehouse é orientado a assunto, integrado, não volátil e variante no tempo — no Olist, um pedido de 2017 permanece no DW e nada é sobrescrito.
>
> **porque**
>
> **Razão II:** A não volatilidade significa que os dados, uma vez carregados no DW, não são apagados nem alterados a cada nova carga, preservando o histórico que sustenta a análise ao longo do tempo (variância temporal).

A respeito dessas asserções, assinale a opção correta:

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 22 (Asserção-Razão)

> **Asserção I:** No projeto Olist, a `fct_order_items` tem grão de **um item de pedido**, enquanto a `fct_orders` tem grão de **um pedido**, agregando pagamento e status.
>
> **porque**
>
> **Razão II:** O DuckDB é um banco colunar e vetorizado, o que o torna equivalente local ao Apache Spark para o processamento em lote das tabelas do Olist.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 23 (Asserção-Razão)

> **Asserção I:** No Snowflake, os *virtual warehouses* são clusters de computação lógicos que podem ser ligados e desligados de forma independente, e a cobrança padrão é por segundo de compute ativo.
>
> **porque**
>
> **Razão II:** O Snowflake roda exclusivamente na infraestrutura da AWS, sendo essa a única nuvem em que seus *virtual warehouses* podem ser provisionados.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 24 (Asserção-Razão)

> **Asserção I:** No schema-on-read do Data Lake, é obrigatório definir e validar o esquema completo dos dados **antes** de gravá-los no repositório, exatamente como no Data Warehouse clássico.
>
> **porque**
>
> **Razão II:** No schema-on-read, os dados são gravados em formato bruto e nativo, e a estrutura só é aplicada no momento da leitura — é justamente essa flexibilidade que permite ao lake acolher texto livre, JSON e outros formatos variados.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 25 (Asserção-Razão)

> **Asserção I:** No esquema estrela do Olist, para consultar o faturamento por categoria basta juntar a `fct_order_items` diretamente às tabelas de staging (`stg_*`), pois a camada `core` de dimensões é dispensável quando já existe staging.
>
> **porque**
>
> **Razão II:** O comando `dbt snapshot` com `strategy='check'` sobrescreve os registros antigos da dimensão a cada execução, implementando assim uma Slowly Changing Dimension do Tipo 1.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

### Questão 26 (Asserção-Razão)

> **Asserção I:** O `dbt docs generate` seguido de `dbt docs serve` entrega um catálogo navegável e o grafo de lineage do pipeline do Olist, mostrando dependências como `stg_orders` → `fct_orders` → `mart_delivery_performance`.
>
> **porque**
>
> **Razão II:** O lineage do dbt é construído automaticamente a partir das referências `{{ ref(...) }}` entre os modelos, que encadeiam staging, core e marts em um grafo de dependências.

A respeito dessas asserções, assinale a opção correta:

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 27 (Asserção-Razão)

> **Asserção I:** O ClickHouse é um banco colunar open-source conhecido pela velocidade em consultas analíticas, e seu motor `MergeTree` usa a cláusula `ORDER BY` para cumprir, de uma vez, o papel de partição e de clustering dos dados.
>
> **porque**
>
> **Razão II:** O Airbyte é uma ferramenta de ingestão de código aberto (com oferta em nuvem) que oferece conectores customizáveis, atraindo quem busca controle e custo menor no "L" do ELT.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 28 (Asserção-Razão)

> **Asserção I:** No princípio de "dados como produto" do data mesh, cada mart do Olist (por exemplo, `mart_delivery_performance`) vira um produto com dono, SLA, documentação e testes de qualidade.
>
> **porque**
>
> **Razão II:** O data mesh, sendo um paradigma organizacional, só pode ser adotado depois de a empresa substituir o dbt e o Airflow por ferramentas proprietárias específicas de mesh, pois nenhuma ferramenta open source suporta domínios.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 29 (Asserção-Razão)

> **Asserção I:** No esquema estrela do Olist, a dimensão `dim_products` deve ser sempre totalmente normalizada em subtabelas separadas (categoria, subcategoria, tradução), pois o esquema estrela exige normalização em terceira forma normal nas dimensões.
>
> **porque**
>
> **Razão II:** No esquema floco de neve (snowflake), as dimensões são normalizadas em subtabelas relacionadas, ao passo que no esquema estrela as dimensões são desnormalizadas em uma única tabela por assunto, favorecendo consultas mais simples e rápidas.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 30 (Asserção-Razão)

> **Asserção I:** Para migrar o pipeline do Olist do DuckDB local para o BigQuery na nuvem, é preciso reescrever integralmente os modelos `stg_orders`, `dim_customers` e `fct_order_items` na sintaxe SQL específica do BigQuery, pois o dbt não abstrai diferenças entre bancos.
>
> **porque**
>
> **Razão II:** O `partition_by` e o `cluster_by` do BigQuery são configurados fora do projeto dbt, diretamente no console da nuvem, já que o `config()` do dbt não permite declarar particionamento nem clustering nos modelos.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

### Questão 31 (Interpretação)

**Estímulo:**

> "O OLTP — *Online Transaction Processing* registra muitas escritas pequenas, como cada pedido novo do marketplace Olist, enquanto o DW é OLAP — *Online Analytical Processing*: poucas consultas que varrem os ~112 mil itens para agregar."

A leitura **mais adequada** do trecho é:

*a. OLTP e OLAP têm propósitos distintos: o transacional é otimizado para muitas gravações pequenas e pontuais, e o analítico para poucas consultas que agregam grandes volumes — por isso o DW do Olist é separado do banco transacional do marketplace.
b. OLTP e OLAP são sinônimos, e usar um ou outro é apenas questão de preferência do engenheiro.
c. O OLAP é o melhor sistema para registrar cada pedido novo do marketplace em tempo real.
d. O OLTP é o mais indicado para varrer os 112 mil itens e calcular faturamento por categoria.
e. Como ambos usam SQL, tanto faz consultar o faturamento diretamente no banco transacional de produção.

### Questão 32 (Interpretação)

**Estímulo:**

> No dbt, a materialização de um modelo pode ser configurada como `view`, `table` ou `incremental`. No Olist, a camada `core` (dimensões e fatos) costuma ser materializada como `table`, enquanto modelos de `staging` finos e descartáveis podem ficar como `view`.

A conclusão **mais bem suportada** pelo trecho é:

a. O dbt obriga que todas as camadas (staging, core, marts) sejam materializadas como `view` para economizar disco.
*b. A escolha da materialização é uma decisão por modelo: `view` para camadas finas e descartáveis (staging) e `table` para o core, que é lido com frequência e se beneficia de persistência física.
c. A materialização `incremental` deve ser evitada, pois recalcula sempre a tabela inteira a cada execução.
d. Materializar a `core` como `view` é obrigatório porque o dbt não permite persistir dimensões e fatos como tabela.
e. A materialização não afeta desempenho nem custo, sendo apenas uma preferência estética.

### Questão 33 (Interpretação)

**Estímulo:**

> "Para o Olist, o ganho concreto dos formatos de tabela abertos seria o **time travel**: poder consultar 'como estava a tabela de pedidos no fechamento de janeiro/2018' — auditável, sem manter cópias manuais. Nosso lake local em Parquet puro não tem isso nativamente."

A interpretação **mais correta** é:

a. O Parquet puro já oferece time travel nativo, tornando Delta e Iceberg desnecessários no Olist.
b. Time travel significa apagar os dados antigos para liberar espaço no lake.
*c. O time travel, provido por formatos como Delta e Iceberg, permite consultar versões passadas da tabela de forma auditável, sem cópias manuais — algo que o Parquet puro do lake local não faz sozinho.
d. Para ter time travel no Olist, é obrigatório migrar todos os dados para um banco transacional OLTP por linha.
e. Time travel é um recurso exclusivo de Data Warehouses on-premises e não existe em Lakehouses.

### Questão 34 (Interpretação)

**Estímulo:**

> Na Modern Data Stack, o **Fivetran** é um SaaS comercial com centenas de conectores prontos e sincronização incremental automática, cobrando por **MAR (Monthly Active Rows)**. O **Airbyte** é a alternativa open source (com cloud), com conectores customizáveis, que atrai quem quer controle e custo menor. No Olist local, esse papel é do script `load_raw.py`.

A leitura **mais adequada** é:

a. Fivetran e Airbyte são ferramentas de transformação (o "T" do ELT) que substituiriam o dbt no pipeline do Olist.
b. O `load_raw.py` do Olist cumpre o papel de BI e dashboards, equivalente ao Metabase.
c. A cobrança por MAR do Fivetran significa que ele cobra por consulta SQL executada no warehouse.
*d. Fivetran e Airbyte cumprem o papel de ingestão (o "L" do ELT) com conectores prontos; substituiriam o `load_raw.py` se o Olist fosse uma fonte ao vivo — Fivetran cobra por MAR, Airbyte é open source e atrai quem busca controle e menor custo.
e. Airbyte, por ser open source, não possui oferta gerenciada em nuvem, ao contrário do Fivetran.

### Questão 35 (Interpretação)

**Estímulo:**

> Uma equipe do Olist precisa contar os pedidos de um único mês em Parquet particionado por ano/mês. Compara duas abordagens: (A) ler **todos** os Parquets de `data/gold/orders` para um DataFrame e só então filtrar por janeiro/2018 em memória; (B) usar `read_parquet(..., hive_partitioning=true)` com `WHERE year = 2018 AND month = 1`.

A conclusão **mais bem suportada** é:

a. A abordagem (A) é melhor, pois ler tudo antes de filtrar garante partition pruning e menor scan.
b. As duas abordagens leem exatamente a mesma quantidade de dados, pois o particionamento não influencia o scan.
c. A abordagem (A) é mais barata porque evita a sobrecarga dos metadados de partição.
d. A abordagem (B) só funciona em bancos transacionais OLTP por linha, não sobre Parquet.
*e. A abordagem (B) faz partition pruning e lê apenas a pasta daquele mês (~1/25 dos dados), enquanto a (A) varre tudo antes de filtrar, anulando a vantagem do particionamento.

### Questão 36 (Interpretação)

**Estímulo:**

> No modelo **on-demand** do BigQuery, paga-se por byte lido (referência da ordem de US\$ 6,25 por TB). A disciplina de FinOps recomenda particionar por padrão, exigir filtro na coluna de partição, evitar `SELECT *` e usar o **dry run** (estimativa de bytes antes de rodar a consulta).

A leitura **mais adequada** do trecho é:

*a. O dry run estima os bytes que a consulta vai varrer antes de executá-la, permitindo ao engenheiro prever o custo e ajustar a query (partição, colunas) — parte da disciplina de FinOps no DW em nuvem.
b. O dry run executa a consulta de fato e cobra o valor total, servindo apenas para gerar a fatura.
c. No on-demand do BigQuery cobra-se por hora de cluster provisionado, independentemente dos bytes lidos.
d. Usar `SELECT *` reduz o custo no on-demand, pois lê todas as colunas de uma só vez com desconto.
e. FinOps é irrelevante em DW na nuvem, pois o custo por consulta é fixo e não depende da modelagem.

### Questão 37 (Interpretação)

**Estímulo:**

A tabela resume a cobrança padrão de três DWs em nuvem:

| DW | Cobrança padrão |
| --- | --- |
| BigQuery | Por TB varrido (on-demand) ou slots |
| Snowflake | Por segundo de compute ativo |
| Redshift | Por hora de cluster (ou por uso no serverless) |

Uma equipe quer **integração nativa com o ecossistema AWS** e aceita **gerenciar clusters provisionados**, pagando por hora de cluster. A opção **mais alinhada** é:

a. BigQuery, por ser serverless puro e cobrar por TB varrido.
*b. Redshift, pela integração nativa com o ecossistema AWS e o modelo de clusters provisionados cobrados por hora.
c. Snowflake, por cobrar por segundo de compute e ser multi-cloud.
d. Qualquer banco transacional OLTP por linha, que atende igualmente análise e AWS.
e. Nenhum DW em nuvem oferece integração com a AWS.

### Questão 38 (Interpretação)

**Estímulo:**

> "A **camada semântica** define métricas e dimensões de forma centralizada — 'faturamento líquido' é definido uma vez (como um modelo/mart no dbt) e todo o BI consome a mesma definição. Sobre essa camada, o **Metabase** (open source) conecta-se ao DuckDB e monta o dashboard do Olist: vendas por categoria, performance de entrega por UF e distribuição das notas de review."

A leitura **mais coerente** é:

a. A camada semântica e o Metabase são a mesma coisa, ambos responsáveis por armazenar os dados brutos do Olist.
b. O Metabase substitui a necessidade de um warehouse, pois processa e guarda os dados internamente.
*c. A camada semântica centraliza a definição das métricas (fonte única da verdade), e o Metabase, como ferramenta de BI, consome essas definições para montar dashboards do Olist sobre o DuckDB.
d. A camada semântica torna o BI dispensável, pois já entrega os gráficos finais ao usuário.
e. O Metabase não consegue ler o DuckDB, exigindo migração prévia dos dados para um banco transacional.

### Questão 39 (Interpretação)

**Estímulo:**

> Uma startup roda todo o pipeline analítico do Olist localmente com DuckDB + dbt-core + Airflow + Metabase open source, com custo de ferramentas de praticamente R\$ 0,00. A diretoria pergunta se deveria migrar imediatamente para uma Modern Data Stack na nuvem (Airbyte + BigQuery + dbt Cloud + Metabase), estimada em ~R\$ 5.500,00/mês, sendo que o volume de dados atual é de ~120 MB.

A recomendação **mais bem fundamentada** é:

a. Migrar imediatamente para a nuvem, pois qualquer stack local é tecnicamente incapaz de rodar dbt e Airflow.
b. Migrar imediatamente, pois R\$ 5.500,00/mês é sempre mais barato do que manter uma stack local gratuita.
c. Descartar tanto a stack local quanto a nuvem e voltar a analisar tudo em planilhas manuais.
*d. Manter a stack local enquanto o volume (~120 MB) e a concorrência de usuários forem baixos — ela entrega o mesmo resultado de graça —, migrando para a MDS na nuvem só quando o volume e a demanda justificarem.
e. Manter a stack local para sempre, pois nenhum crescimento de volume jamais justificaria a nuvem.

### Questão 40 (Interpretação)

**Estímulo:**

> A mensagem central da Aula 11 é demonstrada assim: o `profiles.yml` local usa `type: duckdb` apontando para `olist.duckdb`; para a nuvem, instala-se o `dbt-bigquery` e troca-se para `type: bigquery` com `project` e `dataset` — e os modelos `stg_orders`, `dim_customers` e `fct_order_items` "não mudam uma linha".

A interpretação **mais correta** é:

a. Migrar o Olist para a nuvem exige reescrever toda a lógica SQL dos modelos, pois cada banco tem dialeto incompatível.
b. O `profiles.yml` contém a lógica de transformação dos dados, e por isso os modelos precisam ser reescritos junto.
c. Trocar o adapter do dbt apaga os dados do warehouse de destino a cada execução.
d. O dbt-bigquery e o dbt-duckdb são projetos incompatíveis que não compartilham nenhum modelo entre si.
*e. A portabilidade do dbt permite migrar do DuckDB local para o BigQuery trocando apenas o adapter e o `profiles.yml` (conexão), mantendo os modelos `stg_*`/`dim_*`/`fct_*` idênticos — a lógica de transformação é independente do banco.

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

### Questão 21

- **a.** *Correta!* Ambas verdadeiras e a II justifica a I. A Asserção enuncia os quatro adjetivos de Inmon (orientado a assunto, integrado, não volátil, variante no tempo); a Razão explica corretamente **o que é** a não volatilidade — dados não são apagados nem alterados a cada carga —, justificando por que o pedido de 2017 permanece intacto no DW do Olist.
- **b.** Incorreta. A Razão justifica diretamente a Asserção.
- **c.** Incorreta. A Razão é verdadeira.
- **d.** Incorreta. A Asserção é verdadeira.
- **e.** Incorreta. Ambas são verdadeiras.

### Questão 22

- **a.** Incorreta. A Razão não justifica a Asserção — são fatos independentes.
- **b.** *Correta!* As duas proposições são verdadeiras: a `fct_order_items` tem grão de um item e a `fct_orders`, de um pedido; e o DuckDB é de fato colunar/vetorizado, equivalente local do Spark no curso. Mas a Razão (natureza do motor) **não explica** a definição de grão das fatos (modelagem dimensional) — são temas independentes.
- **c.** Incorreta. A Razão é verdadeira.
- **d.** Incorreta. A Asserção é verdadeira.
- **e.** Incorreta. Ambas são verdadeiras.

### Questão 23

- **a.** Incorreta. A Razão é falsa.
- **b.** Incorreta. A Razão é falsa.
- **c.** *Correta!* A Asserção é verdadeira: os *virtual warehouses* do Snowflake são clusters de compute lógicos, liga/desliga independente, cobrados por segundo de compute ativo. A Razão é falsa: o Snowflake é **multi-cloud** (AWS, Azure e GCP), não exclusivo da AWS.
- **d.** Incorreta. A Asserção é verdadeira.
- **e.** Incorreta. A Asserção é verdadeira.

### Questão 24

- **a.** Incorreta. A Asserção é falsa.
- **b.** Incorreta. A Asserção é falsa.
- **c.** Incorreta. A Razão é verdadeira.
- **d.** *Correta!* A Asserção é falsa: definir o esquema **antes** de gravar é o schema-on-**write** do DW clássico, não o schema-on-read do lake. A Razão descreve corretamente o schema-on-read: grava-se bruto e a estrutura é aplicada só na leitura, o que dá a flexibilidade para acolher texto livre, JSON e formatos variados.
- **e.** Incorreta. A Razão é verdadeira.

### Questão 25

- **a.** Incorreta. Ambas são falsas.
- **b.** Incorreta. Ambas são falsas.
- **c.** Incorreta. A Razão também é falsa.
- **d.** Incorreta. A Asserção também é falsa.
- **e.** *Correta!* As duas proposições são falsas. A camada `core` de dimensões **não** é dispensável: ela é a fonte única da verdade que integra e conforma as fontes (o consumo direto do staging quebraria a estrela conformada). E o `dbt snapshot` com `strategy='check'` implementa **SCD Tipo 2** (cria novas versões com `dbt_valid_from`/`dbt_valid_to`, preservando histórico), **não** SCD Tipo 1 (que sobrescreve).

### Questão 26

- **a.** *Correta!* Ambas verdadeiras e a II justifica a I. O `dbt docs` entrega catálogo + lineage (`stg_orders` → `fct_orders` → `mart_delivery_performance`); a Razão explica **por que** isso é possível: o grafo é montado automaticamente a partir das referências `{{ ref(...) }}` entre os modelos.
- **b.** Incorreta. A Razão justifica diretamente a Asserção.
- **c.** Incorreta. A Razão é verdadeira.
- **d.** Incorreta. A Asserção é verdadeira.
- **e.** Incorreta. Ambas são verdadeiras.

### Questão 27

- **a.** Incorreta. A Razão não justifica a Asserção — trata de outra camada da stack (ingestão).
- **b.** *Correta!* As duas proposições são verdadeiras: o ClickHouse é colunar open-source rápido, e seu `MergeTree` usa o `ORDER BY` como partição + clustering; e o Airbyte é ingestão open source com conectores customizáveis. Mas a Razão fala do **"L" (ingestão)** da stack, não justifica o desempenho colunar do ClickHouse (armazenamento/consulta) — são camadas distintas e independentes.
- **c.** Incorreta. A Razão é verdadeira.
- **d.** Incorreta. A Asserção é verdadeira.
- **e.** Incorreta. Ambas são verdadeiras.

### Questão 28

- **a.** Incorreta. A Razão é falsa.
- **b.** Incorreta. A Razão é falsa.
- **c.** *Correta!* A Asserção é verdadeira: em "dados como produto", cada mart do Olist vira um produto com dono, SLA, documentação e testes. A Razão é falsa: o data mesh é **mudança organizacional**, não uma ferramenta — não exige substituir dbt/Airflow por software proprietário de "mesh"; a própria stack self-service (dbt + DuckDB) serve aos domínios.
- **d.** Incorreta. A Asserção é verdadeira.
- **e.** Incorreta. A Asserção é verdadeira.

### Questão 29

- **a.** Incorreta. A Asserção é falsa.
- **b.** Incorreta. A Asserção é falsa.
- **c.** Incorreta. A Razão é verdadeira.
- **d.** *Correta!* A Asserção é falsa: o esquema **estrela** usa dimensões **desnormalizadas** (uma tabela por assunto), não normalização em 3FN — normalizar as dimensões em subtabelas é característica do **floco de neve**. A Razão descreve corretamente essa distinção: floco de neve normaliza as dimensões, estrela as desnormaliza para consultas mais simples e rápidas.
- **e.** Incorreta. A Razão é verdadeira.

### Questão 30

- **a.** Incorreta. Ambas são falsas.
- **b.** Incorreta. Ambas são falsas.
- **c.** Incorreta. A Razão também é falsa.
- **d.** Incorreta. A Asserção também é falsa.
- **e.** *Correta!* As duas proposições são falsas. Os modelos `stg_*`/`dim_*`/`fct_*` **não** precisam ser reescritos: a portabilidade do dbt faz a migração DuckDB → BigQuery ser apenas troca de adapter e `profiles.yml`. E o `partition_by`/`cluster_by` são declarados **dentro** do projeto dbt, no `config()` do próprio modelo — não no console da nuvem.

### Questão 31

- **a.** *Correta!* O trecho contrasta os dois propósitos: OLTP para muitas escritas pequenas (cada pedido) e OLAP para poucas consultas que agregam grande volume — por isso o DW analítico do Olist é separado do banco transacional do marketplace.
- **b.** Incorreta. OLTP e OLAP não são sinônimos; têm propósitos e otimizações opostos.
- **c.** Incorreta. Registrar cada pedido em tempo real é papel do OLTP, não do OLAP.
- **d.** Incorreta. Varrer 112 mil itens para agregar é papel do OLAP, não do OLTP.
- **e.** Incorreta. Consultas analíticas pesadas no banco de produção travariam o OLTP — por isso se usa um DW separado.

### Questão 32

- **a.** Incorreta. O dbt **não** obriga tudo a ser `view`; a materialização é escolhida por modelo.
- **b.** *Correta!* A materialização é decisão por modelo: `view` para staging fino e descartável, `table` para o core lido com frequência, que se beneficia de persistência física — exatamente o que o trecho descreve.
- **c.** Incorreta. A materialização `incremental` justamente **evita** recalcular a tabela inteira, processando só os novos registros.
- **d.** Incorreta. O dbt permite (e recomenda) materializar a `core` como `table`.
- **e.** Incorreta. A materialização afeta diretamente desempenho e custo (leitura, disco, recomputação).

### Questão 33

- **a.** Incorreta. O Parquet puro **não** oferece time travel nativo — o próprio trecho afirma isso.
- **b.** Incorreta. Time travel é consultar versões passadas, não apagar dados antigos.
- **c.** *Correta!* Formatos como Delta e Iceberg proveem time travel: consultar versões passadas da tabela de forma auditável, sem cópias manuais — recurso que o Parquet puro do lake local não tem sozinho.
- **d.** Incorreta. Não é preciso migrar para OLTP; o time travel vem dos formatos de tabela abertos sobre o lake.
- **e.** Incorreta. Time travel é justamente um recurso de Lakehouses (Delta/Iceberg), não exclusivo de DW on-premises.

### Questão 34

- **a.** Incorreta. Fivetran e Airbyte são de ingestão (o "L"), não de transformação; o "T" é do dbt.
- **b.** Incorreta. O `load_raw.py` faz ingestão dos CSVs, não BI/dashboards (papel do Metabase).
- **c.** Incorreta. MAR (Monthly Active Rows) cobra por linhas ativas sincronizadas, não por consulta SQL no warehouse.
- **d.** *Correta!* Ambos cumprem a ingestão (o "L" do ELT) com conectores prontos e substituiriam o `load_raw.py` se o Olist fosse fonte ao vivo; Fivetran cobra por MAR (SaaS comercial) e o Airbyte é open source, atraindo quem busca controle e menor custo.
- **e.** Incorreta. O Airbyte **tem** oferta em nuvem (Airbyte Cloud), além da versão open source.

### Questão 35

- **a.** Incorreta. Ler tudo antes de filtrar (A) **anula** o partition pruning — é a abordagem que mais varre dados.
- **b.** Incorreta. O particionamento influencia fortemente o scan: (B) lê ~1/25; (A) lê tudo.
- **c.** Incorreta. Os metadados de partição são o que **permite** a poda; (A) não é mais barata.
- **d.** Incorreta. `read_parquet` com hive partitioning roda sobre Parquet no DuckDB, não exige OLTP por linha.
- **e.** *Correta!* A abordagem (B) faz partition pruning e lê só a pasta do mês (~1/25 dos dados), enquanto (A) varre tudo antes de filtrar, anulando a vantagem do particionamento.

### Questão 36

- **a.** *Correta!* O dry run estima os bytes que a consulta varreria **antes** de executá-la, permitindo prever o custo e ajustar a query (partição, colunas) — pilar do FinOps no on-demand do BigQuery.
- **b.** Incorreta. O dry run **não** executa a consulta nem cobra; apenas estima os bytes.
- **c.** Incorreta. No on-demand cobra-se por **byte lido**, não por hora de cluster provisionado.
- **d.** Incorreta. `SELECT *` lê todas as colunas e **aumenta** o custo por byte, não reduz.
- **e.** Incorreta. O custo por consulta depende fortemente da modelagem (partição, colunas), por isso FinOps é essencial.

### Questão 37

- **a.** Incorreta. BigQuery é serverless e cobra por TB varrido — não atende o requisito de clusters provisionados na AWS.
- **b.** *Correta!* O Redshift tem integração nativa com o ecossistema AWS e o modelo de clusters provisionados cobrados por hora — exatamente o requisito do enunciado.
- **c.** Incorreta. Snowflake cobra por segundo de compute e é multi-cloud; não é o mais alinhado a "clusters provisionados por hora na AWS".
- **d.** Incorreta. Banco OLTP por linha é inadequado para análise de grandes volumes.
- **e.** Incorreta. O Redshift é justamente o DW em nuvem com integração nativa à AWS.

### Questão 38

- **a.** Incorreta. Camada semântica e Metabase são coisas distintas: a primeira define métricas; o segundo é a ferramenta de BI que as consome.
- **b.** Incorreta. O Metabase consulta os dados no warehouse (DuckDB); não substitui o warehouse nem guarda os dados.
- **c.** *Correta!* A camada semântica centraliza a definição das métricas (fonte única da verdade) e o Metabase, como BI, consome essas definições para montar os dashboards do Olist sobre o DuckDB.
- **d.** Incorreta. A camada semântica define métricas; o BI (Metabase) ainda é necessário para visualizar.
- **e.** Incorreta. O Metabase lê o DuckDB via driver community; não exige migrar para um OLTP.

### Questão 39

- **a.** Incorreta. A stack local (DuckDB + dbt-core + Airflow + Metabase) roda perfeitamente e é o que o curso usa.
- **b.** Incorreta. R\$ 5.500,00/mês não é "sempre mais barato" que uma stack local gratuita que já resolve o problema.
- **c.** Incorreta. Planilhas manuais são um retrocesso, sem escala, governança nem reprodutibilidade.
- **d.** *Correta!* Enquanto volume (~120 MB) e concorrência forem baixos, a stack local entrega o mesmo resultado de graça; a MDS na nuvem só passa a valer a pena quando o volume e a demanda de usuários crescem — comece local e barato, migre quando o problema justificar.
- **e.** Incorreta. O crescimento para terabytes e alta concorrência **justificaria** a migração; "para sempre local" ignora esse gatilho.

### Questão 40

- **a.** Incorreta. A portabilidade do dbt dispensa reescrever a lógica dos modelos na migração.
- **b.** Incorreta. O `profiles.yml` guarda apenas a **conexão** (adapter/credenciais), não a lógica de transformação (que vive nos modelos).
- **c.** Incorreta. Trocar o adapter não apaga dados; apenas direciona a execução para outro destino.
- **d.** Incorreta. dbt-bigquery e dbt-duckdb são adapters do mesmo dbt e compartilham os mesmos modelos.
- **e.** *Correta!* A portabilidade do dbt permite migrar DuckDB → BigQuery trocando apenas o adapter e o `profiles.yml`; os modelos `stg_*`/`dim_*`/`fct_*` ficam idênticos, pois a lógica de transformação é independente do banco.
