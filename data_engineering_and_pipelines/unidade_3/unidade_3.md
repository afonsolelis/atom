# Unidade 3 — Armazenamento e Arquitetura de Dados

- **Disciplina:** Data Engineering and Pipelines
- **Conteudista:** Afonso Cesar Lelis Brandão
- **Videoaulas desta unidade:** 9 a 12

> **Recap da Unidade 2:** vimos pipelines de ingestão (batch vs streaming), conhecemos ferramentas de orquestração (Airflow, Dagster), entendemos ETL vs ELT e abrimos a discussão sobre processamento distribuído com Spark. Os dados já chegam e são transformados — mas **onde eles ficam guardados**? E **como organizá-los** para que análise e BI funcionem rápido e barato? É o que esta unidade responde: a camada de **armazenamento e arquitetura** que sustenta todo o ecossistema de dados.

---

## Aula 9 — Data Warehouse e modelagem dimensional aplicada

Imagine uma rede de varejo com 200 lojas, milhões de vendas por mês, e uma diretora que pergunta: "qual foi o faturamento por categoria de produto, por região, comparado ao mesmo trimestre do ano passado?". Se essa pergunta bater direto no banco transacional do PDV, a consulta vai travar — e o caixa da loja vai parar. O **Data Warehouse** existe exatamente para isso: um repositório otimizado para **responder perguntas analíticas** sem atrapalhar a operação. Nesta aula você vai entender o que é um DW, as duas grandes escolas de arquitetura (Inmon e Kimball), como se organizam suas camadas e o que torna o armazenamento colunar tão poderoso.

### O conceito de Data Warehouse

Um **Data Warehouse (DW)** é um repositório central, **orientado a assunto, integrado, não volátil e variante no tempo**, projetado para apoiar a tomada de decisão. A definição clássica é de Bill Inmon, considerado o "pai do Data Warehouse". Vamos destrinchar os quatro adjetivos:

- **Orientado a assunto:** organiza-se por temas de negócio (vendas, clientes, estoque), não por aplicação.
- **Integrado:** consolida dados de múltiplas fontes (ERP, CRM, e-commerce) com nomes, unidades e formatos padronizados.
- **Não volátil:** os dados não são sobrescritos — são acumulados; um registro de venda de 2021 continua lá.
- **Variante no tempo:** guarda histórico, permitindo analisar tendências ao longo de anos.

A diferença essencial em relação a um banco transacional (OLTP) é o propósito: o OLTP é **OLTP — Online Transaction Processing** (muitas escritas pequenas, rápidas), enquanto o DW é **OLAP — Online Analytical Processing** (poucas consultas, mas que varrem grandes volumes para agregar).

![Diagrama de um esquema estrela (star schema) com uma tabela fato central conectada a tabelas de dimensão, base da modelagem dimensional em Data Warehouses](https://commons.wikimedia.org/wiki/Special:FilePath/Star-schema.png)

### Arquitetura Inmon vs Kimball

Há duas filosofias clássicas para construir um DW:

| Aspecto | Inmon (top-down) | Kimball (bottom-up) |
| --- | --- | --- |
| **Ponto de partida** | DW corporativo único, normalizado (3FN) | Data marts dimensionais por área |
| **Modelagem** | Entidade-relacionamento normalizada | Modelagem dimensional (estrela) |
| **Integração** | Centralizada antes dos marts | Barramento de dimensões conformadas |
| **Tempo até valor** | Mais lento (constrói a base primeiro) | Mais rápido (entrega marts incrementalmente) |
| **Manutenção** | Mais consistente, menos redundância | Mais flexível, mais redundância controlada |

Na prática, a maioria dos projetos modernos adota uma **abordagem híbrida**: um core integrado (sabor Inmon) que alimenta data marts dimensionais (sabor Kimball). Não existe "vencedor" — existe o que serve ao contexto.

### Camadas: staging, core e data marts

Um DW maduro tem **três camadas lógicas**:

1. **Staging (área de preparação):** onde os dados brutos pousam logo após a extração. Aqui se faz limpeza, deduplicação e padronização. É descartável e temporária.
2. **Core (camada integrada):** o coração do DW, onde os dados de todas as fontes são integrados, historizados e mantidos como **fonte única da verdade**.
3. **Data marts (camada de consumo):** recortes temáticos otimizados para um departamento ou caso de uso (mart de Vendas, mart de Marketing), geralmente em formato dimensional.

Esse fluxo **staging → core → marts** garante separação de responsabilidades: ingestão isolada da integração, e integração isolada do consumo.

### Modelagem dimensional na prática

A modelagem dimensional, popularizada por Ralph Kimball, organiza os dados em **tabelas fato** e **tabelas dimensão**:

- **Tabela fato:** registra os eventos mensuráveis do negócio (uma linha por venda), com **métricas** (quantidade, valor) e **chaves estrangeiras** para as dimensões.
- **Tabela dimensão:** descreve o contexto (quem, o quê, quando, onde) — dimensão Produto, Cliente, Tempo, Loja.

O arranjo mais comum é o **esquema estrela (star schema)**: uma fato central cercada por dimensões. Quando uma dimensão é normalizada em sub-tabelas, temos o **esquema floco de neve (snowflake)**.

Um conceito crucial é o tratamento de **mudanças nas dimensões (SCD — Slowly Changing Dimensions)**. Se um cliente muda de cidade, devemos sobrescrever (SCD Tipo 1) ou criar um novo registro preservando o histórico (SCD Tipo 2)? Para análise temporal correta, o Tipo 2 costuma ser a escolha.

### Armazenamento colunar vs por linha

A grande virada de desempenho dos DWs modernos é o **armazenamento colunar**. Bancos transacionais guardam dados **por linha** (todos os campos de um registro juntos), ótimo para ler/escrever um pedido inteiro. Já os DWs analíticos guardam **por coluna** (todos os valores de uma coluna juntos).

Por que isso importa? Uma consulta analítica típica (`SELECT SUM(valor) FROM vendas`) só precisa da coluna `valor`. No formato colunar, o motor lê **apenas essa coluna**, ignorando dezenas de outras. Além disso, valores de uma mesma coluna são parecidos, o que permite **compressão muito maior** (run-length encoding, dictionary encoding). Formatos como **Parquet** e **ORC** são colunares e dominam o ecossistema analítico.

### Exemplo numérico: custo de varredura

Suponha uma tabela de vendas com 50 colunas e **2 TB** de dados. Você quer somar a coluna `valor_total`, que ocupa 2% do tamanho total.

- **Armazenamento por linha:** o motor precisa ler praticamente os **2 TB** inteiros para chegar à coluna desejada.
- **Armazenamento colunar:** lê só a coluna `valor_total`:

$$
2\,\text{TB} \times 0{,}02 = 0{,}04\,\text{TB} = 40\,\text{GB}
$$

Com compressão colunar de fator 4, isso cai para **10 GB** efetivamente lidos. Em um DW na nuvem que cobra por dados varridos a, digamos, R\$ 30,00 por TB:

$$
\text{Custo por linha} = 2 \times 30 = \text{R\$ }60{,}00
$$
$$
\text{Custo colunar} = 0{,}01 \times 30 = \text{R\$ }0{,}30
$$

Uma economia de **200×** na mesma consulta. Multiplique por milhares de consultas/mês e o impacto financeiro é enorme.

### Atividade prática

Para um cenário de varejo (real ou imaginado):

1. Liste **três perguntas analíticas** que a diretoria faria (ex.: faturamento por região/mês).
2. Desenhe um **esquema estrela** com uma tabela fato `vendas` e ao menos três dimensões (Tempo, Produto, Loja).
3. Indique **uma métrica** na fato e **dois atributos** por dimensão.
4. Identifique uma dimensão que precisaria de **SCD Tipo 2** e justifique.

### Pontos-chave

- O **Data Warehouse** é orientado a assunto, integrado, não volátil e variante no tempo — voltado a OLAP, não a OLTP.
- **Inmon** (top-down, normalizado) e **Kimball** (bottom-up, dimensional) são as duas escolas; projetos reais costumam ser híbridos.
- As camadas **staging → core → data marts** separam ingestão, integração e consumo.
- A **modelagem dimensional** usa tabelas fato (métricas) e dimensão (contexto), em esquema estrela ou floco de neve.
- O **armazenamento colunar** reduz drasticamente dados varridos e custo, base do desempenho analítico.

### Para saber mais

- **KIMBALL, R.; ROSS, M.** *The Data Warehouse Toolkit*. 3. ed. Wiley, 2013.
- **Documentação Apache Parquet:** https://parquet.apache.org/docs/
- **Wikipedia — Star schema:** https://en.wikipedia.org/wiki/Star_schema

## Aula 9 — Roteiro da Videoaula 9: "Data Warehouse e modelagem dimensional aplicada"

**Duração:** 9 a 11 minutos.

### 1. Abertura (0:00 – 0:40)

> "Imagine a diretora de uma rede de 200 lojas pedindo o faturamento por categoria, por região, comparado ao ano passado. Se essa consulta bater no caixa da loja, o caixa trava. Hoje você vai entender o sistema que existe justamente para responder perguntas analíticas sem derrubar a operação: o Data Warehouse."

### 2. Desenvolvimento — parte 1 (0:40 – 4:00)

> "Vamos começar pela definição clássica de Inmon: orientado a assunto, integrado, não volátil e variante no tempo. A palavra-chave é OLAP, em oposição ao OLTP do banco transacional. Em seguida apresento as duas escolas: Inmon, top-down e normalizado, e Kimball, bottom-up e dimensional. Mostro a tabela comparativa e explico por que projetos reais quase sempre são híbridos: um core integrado que alimenta marts dimensionais."

### 3. Desenvolvimento — parte 2 (4:00 – 7:00)

> "Agora as três camadas: staging, onde o dado bruto pousa; core, a fonte única da verdade; e data marts, os recortes por área. Com isso, entro na modelagem dimensional: tabela fato com as métricas, tabelas dimensão com o contexto, montando o esquema estrela. Falo rapidamente de snowflake e do conceito de Slowly Changing Dimensions — quando sobrescrever e quando preservar o histórico."

### 4. Desenvolvimento — parte 3 (7:00 – 9:00)

> "Por que o DW é tão rápido? Armazenamento colunar. Mostro a diferença entre guardar por linha e por coluna, e por que somar uma coluna em formato colunar lê uma fração dos dados. Trago o exemplo numérico: 2 TB de tabela, somar uma coluna de 2% — por linha lê 2 TB, colunar lê 40 GB, e com compressão, 10 GB. A diferença de custo chega a 200 vezes."

### 5. Encerramento (9:00 – 11:00)

> "O Data Warehouse resolve bem o mundo estruturado e tabular. Mas e os dados não estruturados — logs, imagens, JSON, vídeo? Na próxima aula entramos no Data Lake e no Data Lakehouse, que prometem unir o melhor dos dois mundos. Te espero!"

---

## Aula 10 — Data Lake e Data Lakehouse

O Data Warehouse é excelente para dados tabulares e limpos — mas o mundo dos dados é muito mais bagunçado que isso. Logs de servidores, JSON de APIs, imagens, áudios, sensores de IoT: nada disso cabe bem em colunas e linhas pré-definidas. Para acomodar essa variedade, surgiu o **Data Lake**. Só que ele trouxe um problema novo: a facilidade de jogar qualquer coisa dentro virou o **data swamp**, o pântano de dados. Nesta aula você vai entender os limites do DW, o que é um Data Lake, como os formatos de tabela abertos (Delta, Iceberg, Hudi) resgataram a confiabilidade e como a **arquitetura Lakehouse** combina o melhor dos dois mundos.

### Os limites do Data Warehouse

O DW clássico tem três limitações que a era do Big Data expôs:

1. **Esquema rígido (schema-on-write):** você precisa definir a estrutura **antes** de gravar. Dados semiestruturados ou que mudam de forma sofrem.
2. **Custo de armazenamento alto:** DWs guardam dados em formato proprietário e caro; armazenar petabytes de logs brutos seria proibitivo.
3. **Variedade limitada:** imagens, vídeos e texto livre não se encaixam no modelo relacional.

Em ciência de dados e machine learning, justamente esses dados "difíceis" são os mais valiosos — e o DW não os acolhe bem.

### O Data Lake e o risco do data swamp

Um **Data Lake** é um repositório que armazena dados **em formato bruto e no formato nativo**, sem exigir esquema prévio (**schema-on-read** — a estrutura é aplicada na leitura). Tipicamente vive sobre armazenamento de objetos barato como **Amazon S3, Google Cloud Storage ou Azure Data Lake Storage**.

A vantagem é a flexibilidade: jogue tudo lá, decida depois como usar. O perigo é exatamente esse: sem governança, catálogo e qualidade, o lago vira um **data swamp** — um depósito de arquivos sem documentação, sem dono e sem confiabilidade, onde ninguém sabe o que existe nem se pode confiar. Um Data Lake sem disciplina é pior que não ter Data Lake nenhum.

![Centro de dados em nuvem: o tipo de infraestrutura de armazenamento de objetos de baixo custo sobre a qual Data Lakes e Lakehouses são construídos](https://commons.wikimedia.org/wiki/Special:FilePath/CERN_Server_03.jpg)

### Formatos de tabela abertos (Delta, Iceberg, Hudi)

O grande problema histórico do Data Lake era a ausência de garantias **ACID** (atomicidade, consistência, isolamento, durabilidade). Escrever num lago de arquivos Parquet podia deixar leituras inconsistentes no meio de uma atualização. Os **formatos de tabela abertos** resolvem isso adicionando uma **camada de metadados transacional** sobre os arquivos:

| Formato | Origem | Destaques |
| --- | --- | --- |
| **Delta Lake** | Databricks | Transações ACID, time travel, `MERGE`, forte no ecossistema Spark |
| **Apache Iceberg** | Netflix | Evolução de esquema/partição, snapshots, neutro em relação a engine |
| **Apache Hudi** | Uber | Upserts eficientes, ingestão incremental, foco em CDC |

Todos trazem recursos antes exclusivos do DW: transações ACID, **time travel** (consultar como estava ontem), evolução de esquema e `MERGE`/`UPDATE`/`DELETE` sobre arquivos. São a fundação técnica do Lakehouse.

### A arquitetura Lakehouse

A **arquitetura Lakehouse** (termo cunhado pela Databricks) propõe unir o melhor dos dois mundos:

- A **flexibilidade e o baixo custo** do Data Lake (armazenamento de objetos, qualquer tipo de dado, formatos abertos).
- A **confiabilidade e o desempenho** do Data Warehouse (transações ACID, governança, esquema, otimização de consulta).

Na prática, o Lakehouse coloca um formato de tabela aberto (Delta/Iceberg/Hudi) e uma camada de metadados/catálogo sobre o object storage, permitindo que BI, SQL ad hoc e treino de ML rodem **sobre a mesma cópia única dos dados** — sem precisar manter um Data Lake e um DW separados, com cópias duplicadas.

### Arquitetura Medallion (bronze, silver, gold)

Para organizar um Lakehouse e evitar o data swamp, a Databricks popularizou a **arquitetura Medallion**, com três camadas de qualidade crescente:

- **Bronze (bruto):** dados como chegaram da fonte, sem transformação. Histórico fiel, auditável.
- **Silver (limpo/conformado):** dados filtrados, deduplicados, padronizados e validados. Junções entre fontes começam aqui.
- **Gold (curado/negócio):** dados agregados e modelados para consumo direto — tabelas dimensionais, KPIs, features de ML, prontos para BI.

O dado **flui de bronze para gold**, ganhando qualidade e perdendo volume a cada etapa. É o equivalente Lakehouse das camadas staging/core/marts do DW.

### Exemplo numérico: custo de armazenamento

Compare guardar **100 TB** de dados históricos por um ano:

- **Data Warehouse na nuvem** (armazenamento gerenciado), a ~R\$ 100,00 por TB/mês:

$$
100 \times 100 \times 12 = \text{R\$ }120\,000{,}00\text{/ano}
$$

- **Lakehouse sobre object storage** (S3/GCS), a ~R\$ 0,12 por GB/mês $\approx$ R\$ 120,00 por TB/mês na camada padrão, mas com **tiering** para classe fria (R\$ 6,00 por TB/mês) nos dados raramente acessados. Supondo 20% quente e 80% frio:

$$
(100 \times 0{,}2 \times 120 + 100 \times 0{,}8 \times 6) \times 12 = (2\,400 + 480) \times 12 = \text{R\$ }34\,560{,}00\text{/ano}
$$

A economia chega a **~70%** ao manter o histórico bruto no object storage barato, reservando o DW (ou camada gold) apenas para o que precisa de desempenho de consulta. Esse é o argumento econômico central do Lakehouse.

### Atividade prática

Para uma empresa de e-commerce (real ou imaginada):

1. Liste **quatro tipos de dado** que não caberiam bem num DW tradicional (ex.: logs de clique, fotos de produto).
2. Classifique cada um nas camadas **bronze, silver, gold** da Medallion.
3. Escolha um **formato de tabela aberto** (Delta, Iceberg ou Hudi) e justifique para o caso de CDC/upserts.
4. Aponte **dois riscos de virar data swamp** e como mitigá-los (catálogo, governança).

### Pontos-chave

- O **Data Warehouse** sofre com esquema rígido, custo alto e baixa variedade — limites da era do Big Data.
- O **Data Lake** acolhe dados brutos e variados (schema-on-read), mas sem governança vira **data swamp**.
- **Delta, Iceberg e Hudi** trazem ACID, time travel e evolução de esquema ao lago.
- A **arquitetura Lakehouse** une flexibilidade/custo do lago com confiabilidade/desempenho do DW, sobre uma cópia única.
- A **arquitetura Medallion** (bronze → silver → gold) organiza o Lakehouse em camadas de qualidade crescente.

### Para saber mais

- **Documentação Delta Lake:** https://docs.delta.io/latest/index.html
- **Apache Iceberg — documentação oficial:** https://iceberg.apache.org/docs/latest/
- **Databricks — What is a Lakehouse?:** https://www.databricks.com/glossary/data-lakehouse

## Aula 10 — Roteiro da Videoaula 10: "Data Lake e Data Lakehouse"

**Duração:** 9 a 11 minutos.

### 1. Abertura (0:00 – 0:40)

> "O Data Warehouse é ótimo para dados tabulares e limpos. Mas e logs, JSON, imagens, áudio, sensores de IoT? Nada disso cabe em colunas pré-definidas. Hoje vamos conhecer o Data Lake, o pântano de dados que ele pode virar, e a arquitetura Lakehouse, que promete unir o melhor dos dois mundos."

### 2. Desenvolvimento — parte 1 (0:40 – 4:00)

> "Começo pelos limites do DW: esquema rígido schema-on-write, custo alto de armazenamento e variedade limitada. Aí entra o Data Lake: schema-on-read, sobre object storage barato como S3. Mostro a vantagem da flexibilidade e o grande perigo: sem governança, catálogo e qualidade, o lago vira um data swamp, um depósito onde ninguém confia em nada."

### 3. Desenvolvimento — parte 2 (4:00 – 7:00)

> "Como resgatar a confiabilidade? Com os formatos de tabela abertos. Apresento a tabela: Delta Lake da Databricks, Iceberg do Netflix, Hudi do Uber. Todos trazem transações ACID, time travel, evolução de esquema e MERGE sobre arquivos. Em cima disso, defino a arquitetura Lakehouse: a flexibilidade e o custo do lago, com a confiabilidade e o desempenho do warehouse, numa cópia única dos dados."

### 4. Desenvolvimento — parte 3 (7:00 – 9:00)

> "Para organizar e fugir do swamp, a arquitetura Medallion: bronze cru, silver limpo, gold curado para o negócio. O dado flui ganhando qualidade. E o exemplo numérico: guardar 100 TB por ano. No DW gerenciado dá cerca de R$ 120 mil; no Lakehouse com tiering quente/frio, cerca de R$ 34 mil. Quase 70% de economia mantendo o histórico no object storage barato."

### 5. Encerramento (9:00 – 11:00)

> "Vimos as arquiteturas conceituais. Mas como isso se materializa em produtos reais que você usaria amanhã? Na próxima aula vamos aos Data Warehouses na nuvem — BigQuery, Snowflake e Redshift — e ao conceito que mudou tudo: a separação entre armazenamento e computação. Te espero!"

---

## Aula 11 — Data Warehouses na nuvem (BigQuery, Snowflake, Redshift)

Até pouco tempo atrás, montar um Data Warehouse significava comprar servidores caros, dimensionar para o pico, e ver tudo ocioso fora dele. A nuvem virou o jogo com uma ideia simples e poderosa: **separar armazenamento de computação**. Você guarda os dados num lugar barato e aciona poder de processamento sob demanda, pagando só pelo que usa. Esta aula apresenta os três grandes DWs em nuvem — **BigQuery, Snowflake e Redshift** —, seus modelos de preço e as técnicas de **particionamento e clustering** que separam uma fatura de R\$ 50,00 de uma de R\$ 5.000,00 na mesma consulta.

### Separação de armazenamento e computação

No DW tradicional (on-premises), **armazenamento e processamento eram acoplados** no mesmo servidor — escalar um exigia escalar o outro. A inovação dos DWs em nuvem foi **desacoplar**:

- **Armazenamento:** os dados ficam em object storage barato e elástico.
- **Computação:** clusters/motores são acionados sob demanda para processar consultas.

As consequências são profundas. Você pode ter **múltiplos clusters lendo os mesmos dados** sem conflito (o time de BI e o de ML não competem por recursos), **escalar o processamento** para uma consulta pesada e desligá-lo depois, e **pagar armazenamento e computação separadamente**. É o que torna o DW em nuvem econômico e elástico.

![Servidores em um data center em nuvem: a infraestrutura elástica que sustenta a separação entre armazenamento e computação nos DWs em nuvem](https://commons.wikimedia.org/wiki/Special:FilePath/Wikimedia_Foundation_Servers-8055_35.jpg)

### BigQuery, Snowflake e Redshift

Os três líderes têm filosofias distintas:

| Atributo | BigQuery (Google) | Snowflake | Redshift (AWS) |
| --- | --- | --- | --- |
| **Modelo** | Serverless puro (sem clusters a gerenciar) | Virtual warehouses (clusters lógicos) | Clusters provisionados + Serverless |
| **Cobrança padrão** | Por TB varrido (on-demand) ou slots | Por segundo de compute ativo | Por hora de cluster (ou por uso no serverless) |
| **Nuvem** | Google Cloud | Multi-cloud (AWS, Azure, GCP) | AWS |
| **Diferencial** | Zero administração, escala automática | Separação total storage/compute, sharing | Integração nativa com ecossistema AWS |

**BigQuery** brilha pela simplicidade serverless — você não gerencia infraestrutura nenhuma. **Snowflake** se destaca pela separação total e por recursos como data sharing e zero-copy cloning. **Redshift** é a escolha natural de quem já vive no ecossistema AWS. Não há "melhor absoluto"; há melhor para o contexto.

### Modelos de preço (on-demand vs slots)

Entender o modelo de cobrança é o que evita sustos na fatura. Há duas lógicas principais:

- **On-demand (por dados varridos):** você paga por **byte lido** pela consulta. Ótimo para uso esporádico e imprevisível. No BigQuery, por exemplo, a referência é da ordem de **US\$ 6,25 por TB** varrido.
- **Slots / capacidade reservada / virtual warehouses:** você reserva (ou aciona) uma capacidade de processamento e paga por **tempo**. Compensa em uso intenso e previsível, dando custo estável.

A regra prática: cargas pequenas e esporádicas → **on-demand**; cargas grandes, contínuas e previsíveis → **capacidade reservada**. Muitas empresas usam um híbrido.

### Particionamento e clustering

Duas técnicas reduzem drasticamente os dados varridos (e, portanto, o custo):

- **Particionamento:** divide fisicamente a tabela por uma coluna, tipicamente **data** (`data_venda`). Uma consulta com filtro `WHERE data_venda = '2026-06-01'` lê **apenas a partição daquele dia**, ignorando o resto. Isso é **partition pruning**.
- **Clustering (ou ordenação):** organiza os dados **dentro** de cada partição por colunas de filtro frequente (ex.: `id_loja`). Permite ao motor pular blocos que não contêm os valores buscados (**block pruning**).

Combinados, particionamento + clustering transformam uma varredura de tabela inteira numa leitura cirúrgica de poucos blocos.

### Otimização de consultas

Além de particionar e clusterizar, boas práticas de SQL economizam muito:

1. **Selecione só as colunas necessárias** — `SELECT *` em DW colunar é caro; cada coluna lida custa.
2. **Filtre cedo** pela coluna de partição para ativar o pruning.
3. **Evite junções desnecessárias** e materialize agregações pesadas em tabelas/views materializadas.
4. **Use a estimativa de custo** (dry run) antes de rodar consultas grandes — o BigQuery, por exemplo, mostra quantos bytes serão lidos antes da execução.

Uma cultura de "olhar o custo antes de rodar" é tão importante quanto a tecnologia.

### Exemplo numérico: custo por consulta

Uma tabela de eventos tem **10 TB**, particionada por dia, com 365 dias de dados (~27,4 GB/dia). Um analista roda uma consulta filtrando **um único dia** e selecionando apenas 1 das 50 colunas.

**Sem particionamento e com `SELECT *`** (lê tudo):

$$
10\,\text{TB} \times 6{,}25 = \text{US\$ }62{,}50 \text{ por consulta}
$$

**Com particionamento por dia + seleção de 1 coluna (2% do tamanho):**

$$
0{,}0274\,\text{TB} \times 0{,}02 \times 6{,}25 \approx \text{US\$ }0{,}0034 \text{ por consulta}
$$

A diferença é de cerca de **18.000×**. Se 30 analistas rodam 20 consultas/dia, a versão ingênua custaria

$$
30 \times 20 \times 62{,}50 \times 22 \approx \text{US\$ }825\,000 \text{/mês}
$$

contra **~US\$ 45/mês** na versão otimizada. É literalmente a diferença entre um projeto inviável e um trivial.

### Pausa para reflexão (Desafio)

> Se a mesma consulta pode custar **US\$ 62,50** ou **US\$ 0,003** dependendo de como a tabela foi modelada e do SQL escrito, de quem é a responsabilidade pela conta no fim do mês: do engenheiro de dados que projetou a tabela, do analista que escreveu a query, ou da plataforma que cobra por byte? Reflita: que **práticas de FinOps** (limites de custo por consulta, dry run obrigatório, tabelas particionadas por padrão, painéis de custo por time) você implantaria para que ninguém seja "surpreendido" pela fatura? E como equilibrar liberdade de explorar dados com disciplina de gasto?

### Atividade prática

Escolha **um** dos três DWs (BigQuery, Snowflake ou Redshift) e:

1. Liste **três vantagens** e **uma limitação** do modelo escolhido.
2. Defina **uma estratégia de particionamento** e **uma de clustering** para uma tabela de vendas.
3. Estime o custo de uma consulta que varre 1 dia de uma tabela de 5 TB particionada por dia (365 dias).
4. Proponha **duas regras de governança de custo** (FinOps) para o time.

### Pontos-chave

- A **separação entre armazenamento e computação** é a inovação que tornou o DW em nuvem elástico e econômico.
- **BigQuery** (serverless), **Snowflake** (virtual warehouses, multi-cloud) e **Redshift** (AWS) têm filosofias distintas.
- Modelos de preço: **on-demand** (por dados varridos) vs **slots/capacidade** (por tempo) — escolha pelo padrão de uso.
- **Particionamento** + **clustering** ativam pruning e reduzem drasticamente dados varridos e custo.
- A mesma consulta pode custar milhares de vezes mais ou menos; **otimização e FinOps** são parte do trabalho.

### Para saber mais

- **Documentação BigQuery:** https://cloud.google.com/bigquery/docs
- **Documentação Snowflake:** https://docs.snowflake.com/
- **Amazon Redshift — documentação:** https://docs.aws.amazon.com/redshift/

## Aula 11 — Roteiro da Videoaula 11: "Data Warehouses na nuvem (BigQuery, Snowflake, Redshift)"

**Duração:** 9 a 11 minutos.

### 1. Abertura (0:00 – 0:40)

> "Antes, montar um Data Warehouse era comprar servidor caro, dimensionar para o pico e ver tudo ocioso fora dele. A nuvem mudou isso com uma ideia simples: separar armazenamento de computação. Hoje vamos aos três grandes — BigQuery, Snowflake e Redshift — e às técnicas que separam uma fatura de R$ 50 de uma de R$ 5 mil na mesma consulta."

### 2. Desenvolvimento — parte 1 (0:40 – 4:00)

> "Começo pela separação storage/compute: no on-premises eram acoplados, escalar um exigia escalar o outro. Na nuvem, dados ficam em object storage barato e a computação é acionada sob demanda. Isso permite múltiplos clusters lendo os mesmos dados sem competir. Depois comparo os três: BigQuery serverless puro, Snowflake com virtual warehouses e multi-cloud, Redshift integrado à AWS."

### 3. Desenvolvimento — parte 2 (4:00 – 7:00)

> "Modelos de preço: on-demand cobra por byte varrido, ótimo para uso esporádico; slots e capacidade reservada cobram por tempo, melhor em uso intenso e previsível. Em seguida, as duas alavancas de economia: particionamento, que divide a tabela por data e ativa o partition pruning, e clustering, que ordena dentro da partição e ativa o block pruning. Combinados, viram uma leitura cirúrgica."

### 4. Desenvolvimento — parte 3 (7:00 – 9:00)

> "O exemplo numérico mostra o tamanho do problema: tabela de 10 TB, consulta de um dia. Sem partição e com SELECT estrela, US$ 62,50 por consulta. Com partição por dia e uma coluna, menos de um centavo. Diferença de 18 mil vezes. Com 30 analistas, isso é a diferença entre 825 mil dólares por mês e 45 dólares. Otimização de SQL e FinOps são parte do trabalho do engenheiro de dados."

### 5. Encerramento (9:00 – 11:00)

> "Já temos onde guardar e como consultar barato. Falta juntar as peças num ecossistema coerente. Na próxima aula fechamos a unidade com a Modern Data Stack: Fivetran e Airbyte para ingestão, dbt para transformação, camada semântica e BI, e o conceito de data mesh. Te espero!"

---

## Aula 12 — Modern Data Stack e arquitetura de dados na nuvem

Nas aulas anteriores montamos as peças isoladas: warehouse, lake, lakehouse, DWs em nuvem. Mas como tudo isso se combina num conjunto de ferramentas que uma empresa realmente usa hoje? A resposta tem nome: **Modern Data Stack (MDS)** — um ecossistema modular de ferramentas SaaS, plugáveis entre si, centrado no DW/Lakehouse em nuvem. Nesta aula que fecha a unidade você vai conhecer os blocos da MDS — ingestão gerenciada (Fivetran, Airbyte), transformação com dbt, camada semântica e BI — e o paradigma organizacional do **data mesh**, que descentraliza a propriedade dos dados.

### O que é a Modern Data Stack

A **Modern Data Stack** é uma forma de arquitetar a plataforma de dados baseada em **ferramentas modulares, em nuvem, gerenciadas (SaaS) e centradas no warehouse/lakehouse**. Em vez de uma plataforma monolítica única, você compõe a stack com a melhor ferramenta de cada categoria, conectadas por padrões abertos.

O fio condutor da MDS é o **ELT** (Extract, Load, Transform), não o ETL clássico: primeiro **carrega** o dado bruto no DW barato e elástico, **depois transforma** lá dentro com SQL. As camadas típicas:

1. **Ingestão** (Fivetran, Airbyte) → carrega dados das fontes no DW.
2. **Armazenamento** (BigQuery, Snowflake, Redshift, Databricks) → o coração.
3. **Transformação** (dbt) → modela os dados dentro do DW.
4. **Camada semântica / BI** (Looker, Power BI, Metabase) → expõe ao usuário final.
5. **Orquestração e observabilidade** (Airflow, Dagster, Monte Carlo) → cola e monitora tudo.

![Pilha de ferramentas em nuvem conectadas: a Modern Data Stack compõe ingestão, armazenamento, transformação e BI em módulos plugáveis sobre o data warehouse](https://commons.wikimedia.org/wiki/Special:FilePath/CERN_Server_03.jpg)

### Ingestão gerenciada (Fivetran, Airbyte)

Escrever e manter conectores para cada fonte (Salesforce, Stripe, Postgres, Google Ads) é trabalhoso e repetitivo. Ferramentas de ingestão gerenciada resolvem isso com **conectores prontos**:

- **Fivetran:** SaaS comercial, centenas de conectores mantidos, configuração quase sem código, com sincronização incremental automática. Cobra por **MAR (Monthly Active Rows)**.
- **Airbyte:** alternativa open source (com versão cloud), comunidade ativa criando conectores, permite conectores customizados. Atrai quem quer controle e custo menor.

A proposta de ambos é a mesma: você **não escreve código de extração**; configura origem e destino, e a ferramenta cuida de schema drift, reprocessos e incrementos. É o "L" (Load) do ELT industrializado.

### Transformação com dbt

O **dbt (data build tool)** é a peça mais emblemática da MDS. Ele permite transformar dados **dentro do DW usando apenas SQL** (com Jinja para reuso), trazendo práticas de engenharia de software para a análise:

- **Modelos como `SELECT`:** cada transformação é um arquivo SQL versionado em Git.
- **Lineage automático:** o dbt monta o grafo de dependências entre modelos (DAG).
- **Testes de dados:** validações declarativas (unicidade, não-nulo, integridade referencial).
- **Documentação gerada:** catálogo navegável com descrições e linhagem.
- **Ambientes:** dev, staging e produção separados.

O dbt é o "T" (Transform) do ELT e o que materializa, na prática, as camadas silver/gold da Medallion ou os data marts do DW — só que com **CI/CD, testes e documentação** como num projeto de software.

### Camada semântica e BI

Aqui mora um problema clássico: dois relatórios mostram "receita" com números diferentes porque cada analista calculou à sua maneira. A **camada semântica** resolve isso definindo **métricas e dimensões de forma centralizada e única** — "receita líquida" é definida uma vez, e todas as ferramentas de BI consomem a mesma definição.

Sobre essa camada vêm as ferramentas de **Business Intelligence**, que entregam dashboards e self-service ao usuário final:

- **Looker** (Google) — forte camada semântica (LookML).
- **Power BI** (Microsoft) — dominante no mercado corporativo.
- **Metabase / Apache Superset** — opções open source acessíveis.
- **Tableau** — referência em visualização.

A camada semântica garante **uma única fonte da verdade para os números**, evitando o caos de definições divergentes.

### Data mesh: princípios

Conforme a empresa cresce, um time central de dados vira gargalo: ele não conhece todos os domínios e não dá conta da demanda. O **data mesh** (proposto por Zhamak Dehghani) é um paradigma **organizacional** que descentraliza a responsabilidade pelos dados, apoiado em quatro princípios:

1. **Propriedade orientada a domínio:** cada domínio de negócio (vendas, logística) é dono dos seus próprios dados.
2. **Dados como produto:** cada conjunto de dados é tratado como um produto, com dono, SLA, documentação e qualidade.
3. **Plataforma de dados self-service:** infraestrutura comum que permite a cada domínio criar e servir seus produtos de dados.
4. **Governança federada computacional:** padrões e políticas globais (segurança, interoperabilidade) aplicados de forma automatizada.

Data mesh não é uma ferramenta — é uma **mudança de modelo organizacional**, indicada para empresas grandes e com muitos domínios. Para empresas menores, uma stack centralizada ainda costuma ser o melhor caminho.

### Exemplo numérico: TCO da stack

Vamos estimar o **TCO (Custo Total de Propriedade)** mensal de uma Modern Data Stack para uma empresa de médio porte:

| Componente | Ferramenta | Custo mensal (R\$) |
| --- | --- | --- |
| Ingestão | Fivetran (volume médio de MAR) | 4.000,00 |
| Armazenamento + compute | BigQuery (on-demand + storage) | 6.000,00 |
| Transformação | dbt Cloud (5 desenvolvedores) | 1.500,00 |
| BI | Power BI (50 licenças) | 3.000,00 |
| Observabilidade | Monte Carlo (plano básico) | 2.500,00 |
| **Total ferramentas** | | **17.000,00** |

Some o time: 1 engenheiro de dados + 1 analytics engineer a ~R\$ 18.000,00/mês de custo total cada = **R\$ 36.000,00**.

$$
\text{TCO mensal} = 17\,000 + 36\,000 = \text{R\$ }53\,000{,}00
$$
$$
\text{TCO anual} \approx 53\,000 \times 12 = \text{R\$ }636\,000{,}00
$$

Compare com a alternativa de **construir conectores e infraestrutura do zero**: facilmente exigiria 4–6 engenheiros (R\$ 70–100 mil/mês só de pessoal) e meses até o primeiro valor. A MDS troca **CapEx e tempo de engenharia por OpEx de SaaS** — entregando valor em semanas. Para a maioria das empresas, comprar a stack sai mais barato e rápido que construir.

### Atividade prática

Monte, no papel, a **Modern Data Stack** de uma empresa fictícia:

1. Escolha uma ferramenta para cada camada (ingestão, armazenamento, transformação, BI, observabilidade).
2. Justifique **uma escolha open source** e **uma escolha SaaS comercial** na sua stack.
3. Estime um **TCO mensal** aproximado (ferramentas + 2 pessoas).
4. Decida: a empresa deveria adotar **data mesh** agora? Justifique pelo porte e número de domínios.

### Pontos-chave

- A **Modern Data Stack** é modular, SaaS, em nuvem e centrada no DW/Lakehouse, baseada em **ELT**.
- **Fivetran** (SaaS) e **Airbyte** (open source) industrializam a ingestão com conectores prontos.
- **dbt** transforma dados no DW com SQL, trazendo testes, lineage, documentação e CI/CD à análise.
- A **camada semântica** garante uma definição única de métricas; o **BI** entrega self-service ao usuário.
- O **data mesh** descentraliza a propriedade dos dados em domínios — solução organizacional para empresas grandes.

### Para saber mais

- **Documentação dbt:** https://docs.getdbt.com/
- **DEHGHANI, Z.** *Data Mesh: Delivering Data-Driven Value at Scale*. O'Reilly, 2022.
- **Airbyte — documentação:** https://docs.airbyte.com/
- **REIS, J.; HOUSLEY, M.** *Fundamentals of Data Engineering*. O'Reilly, 2022.

### O que você verá na próxima unidade

Na **Unidade 4**, vamos do "como armazenar e organizar" para o "como confiar e governar". O foco será **Qualidade, Governança e DataOps**: como garantir que os dados são corretos e confiáveis (testes de qualidade, observabilidade, contratos de dados), como governá-los com segurança, privacidade (LGPD), catálogo e linhagem, e como aplicar práticas de DataOps — CI/CD, automação, monitoramento — para operar pipelines de dados com a mesma maturidade do desenvolvimento de software. É a hora de transformar uma plataforma que **funciona** em uma plataforma em que se pode **confiar**.

## Aula 12 — Roteiro da Videoaula 12: "Modern Data Stack e arquitetura de dados na nuvem"

**Duração:** 9 a 11 minutos.

### 1. Abertura (0:00 – 0:40)

> "Já montamos as peças: warehouse, lake, lakehouse, DWs em nuvem. Mas como tudo isso vira um conjunto de ferramentas que uma empresa usa de verdade hoje? A resposta tem nome: Modern Data Stack. Hoje você vai conhecer os blocos dessa stack e o paradigma do data mesh, fechando nossa unidade de arquitetura."

### 2. Desenvolvimento — parte 1 (0:40 – 4:00)

> "A Modern Data Stack é modular, SaaS, em nuvem, centrada no warehouse, e baseada em ELT: carrega primeiro o bruto, transforma depois lá dentro. Apresento as camadas: ingestão, armazenamento, transformação, camada semântica e BI, e observabilidade. Detalho a ingestão gerenciada: Fivetran comercial com conectores prontos, Airbyte open source com comunidade ativa. Você não escreve código de extração; configura origem e destino."

### 3. Desenvolvimento — parte 2 (4:00 – 7:00)

> "A peça mais emblemática é o dbt: transformar dados no DW com SQL, mas com práticas de engenharia de software — modelos versionados em Git, lineage automático, testes de dados, documentação gerada. Depois, a camada semântica, que resolve o problema de dois relatórios mostrarem receitas diferentes: métrica definida uma vez, consumida por todo o BI. Cito Looker, Power BI, Metabase."

### 4. Desenvolvimento — parte 3 (7:00 – 9:00)

> "Quando a empresa cresce, o time central de dados vira gargalo. Aí entra o data mesh: propriedade por domínio, dados como produto, plataforma self-service e governança federada. É mudança organizacional, não ferramenta. E o exemplo numérico do TCO: ferramentas a R$ 17 mil mais duas pessoas, dá cerca de R$ 53 mil por mês, R$ 636 mil por ano — muito menos que construir tudo do zero com seis engenheiros."

### 5. Encerramento (9:00 – 11:00)

> "Fechamos a unidade de armazenamento e arquitetura: sabemos onde guardar, como consultar barato e como montar a stack. Na próxima unidade vamos do 'como armazenar' para o 'como confiar': qualidade, governança e DataOps. É hora de transformar uma plataforma que funciona em uma plataforma em que se pode confiar. Te espero!"

---

## Quiz não avaliativo

### Questão 1

Sobre **modelagem dimensional** e **armazenamento colunar** em um Data Warehouse, assinale a alternativa **correta**:

- [ ] a. No esquema estrela, a tabela fato guarda os atributos descritivos (nome do produto, cidade do cliente) e as tabelas dimensão guardam as métricas numéricas.
- [x] b. A tabela fato guarda as métricas e as chaves para as dimensões, enquanto as dimensões guardam o contexto descritivo; o armazenamento colunar acelera consultas analíticas por ler apenas as colunas necessárias e permitir alta compressão.
- [ ] c. O armazenamento colunar é mais rápido que o por linha para transações OLTP (muitas escritas pequenas em um único registro).
- [ ] d. Modelagem dimensional e armazenamento colunar são incompatíveis: quem usa esquema estrela precisa obrigatoriamente de armazenamento por linha.

**Resposta correta:** `b`

**Feedback:** A (b) está correta: na modelagem dimensional, a **fato** contém métricas + chaves estrangeiras e as **dimensões** contêm os atributos descritivos; o **colunar** lê só as colunas requeridas e comprime muito, ideal para OLAP. A (a) inverte os papéis de fato e dimensão. A (c) é falsa: o colunar é ótimo para OLAP (leituras agregadas), enquanto o **por linha** vence em OLTP. A (d) é falsa: são justamente as duas tecnologias que se combinam nos DWs analíticos modernos.

### Questão 2

Uma empresa migra para um Data Warehouse em nuvem e quer **reduzir o custo das consultas**, que cobram por dados varridos. A tabela principal tem 8 TB e a maioria das consultas filtra por uma data específica e usa poucas colunas. Qual a estratégia **mais eficaz**?

- [ ] a. Rodar `SELECT *` sempre, pois ler todas as colunas garante que nenhum dado seja perdido na análise.
- [ ] b. Migrar a tabela para um banco transacional OLTP por linha, que é mais barato para consultas analíticas.
- [x] c. Particionar a tabela por data e clusterizar/ordenar pelas colunas de filtro frequente, além de selecionar apenas as colunas necessárias — assim o motor varre só a partição e os blocos relevantes.
- [ ] d. Duplicar a tabela em três cópias idênticas para distribuir a carga e, com isso, reduzir o custo por consulta.

**Resposta correta:** `c`

**Feedback:** A (c) está correta: **particionamento** ativa o partition pruning (lê só a partição do dia), **clustering** ativa o block pruning (pula blocos irrelevantes) e selecionar poucas colunas reduz ainda mais os bytes lidos — exatamente as alavancas de economia em DW que cobra por dados varridos. A (a) é o oposto: `SELECT *` em colunar maximiza o custo. A (b) é falsa: OLTP por linha é ruim para consultas analíticas. A (d) triplicaria o custo de armazenamento sem reduzir os bytes varridos por consulta.

---

## Atividade Verificadora (AAI — Atividade Avaliativa Individual)

**Pergunta:**

> Uma fintech de médio porte tem hoje todos os seus dados analíticos em um banco PostgreSQL transacional, que vem ficando lento: relatórios pesados travam o sistema de produção, dados não estruturados (logs de app, eventos de clique, documentos JSON de APIs de crédito) não cabem bem, e o time de ciência de dados reclama da falta de histórico. A diretoria pede a você uma proposta de **nova arquitetura de dados na nuvem**, com orçamento inicial de até R\$ 60 mil/mês (ferramentas + 2 pessoas).
>
> Estruture sua resposta em três partes:
>
> 1. **Arquitetura proposta** — DW, Data Lake ou Lakehouse? Justifique pela variedade de dados e pelos casos de uso (BI + ciência de dados). Indique as camadas (ex.: bronze/silver/gold ou staging/core/marts).
> 2. **Modern Data Stack** — escolha ferramentas para ingestão, armazenamento/compute, transformação e BI, e justifique cada escolha.
> 3. **Controle de custo (FinOps)** — quais decisões de modelagem (particionamento, clustering, formato colunar) e de governança você adotaria para manter a fatura sob controle? Estime um TCO mensal aproximado.

**Resposta esperada:**

> Uma resposta de qualidade recomenda uma **arquitetura Lakehouse** (ou, no mínimo, DW em nuvem + Data Lake) — justamente porque há **variedade de dados** (estruturados de crédito + não estruturados como logs/JSON/cliques) e **dois consumidores** (BI exige confiabilidade e esquema; ciência de dados exige flexibilidade e histórico bruto). O Lakehouse sobre object storage barato, com formato de tabela aberto (Delta ou Iceberg), atende ambos com **uma cópia única**. As camadas devem seguir a **Medallion** (bronze = bruto/auditável, silver = limpo/conformado, gold = curado para BI e features de ML), separando claramente ingestão, integração e consumo. Para a **Modern Data Stack**, espera-se algo como: ingestão com **Fivetran ou Airbyte** (conectores prontos, sem código de extração); armazenamento/compute com **BigQuery, Snowflake ou Databricks** (separação storage/compute, elasticidade); transformação com **dbt** (modelos versionados, testes, lineage, documentação — materializando silver/gold); e BI com **Power BI, Looker ou Metabase**, idealmente sobre uma **camada semântica** que padronize métricas (evitando "receitas" divergentes). No **FinOps**, a resposta deve citar: **formato colunar** (Parquet), **particionamento por data** e **clustering** por colunas de filtro (ativando pruning), **evitar `SELECT *`**, usar **dry run/estimativa de custo**, tiering quente/frio no object storage, e regras de governança (limites de custo por consulta, painéis de custo por time). Um **TCO** plausível fica em torno de R\$ 15–20 mil/mês de ferramentas + ~R\$ 36 mil/mês de duas pessoas, totalizando ~R\$ 50–56 mil/mês, dentro do orçamento. A resposta deve demonstrar **pensamento de trade-off** (comprar SaaS vs construir; quente vs frio; on-demand vs capacidade reservada) e **não** propor "implantar tudo de uma vez" — deve priorizar entregar valor incremental, começando pelo essencial.

---

## Material complementar

### Direto da fonte — livro da Biblioteca Virtual

> Este é o livro de cabeceira da Unidade 3: Kimball e Ross consolidam, em linguagem acessível, tudo o que destrinchamos sobre **modelagem dimensional** — tabelas fato e dimensão, esquema estrela, Slowly Changing Dimensions e o desenho de Data Warehouses que realmente respondem às perguntas do negócio. A obra é a referência canônica que sustentou décadas de projetos de DW e que continua válida na era do Lakehouse e da Modern Data Stack.

- **Nome do livro:** *The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling* (3ª edição)
- **Capítulo:** Capítulo 1 — *Data Warehousing, Business Intelligence, and Dimensional Modeling Primer*
- **Organizador/Autores:** Ralph Kimball e Margy Ross
- **Editora:** Wiley
- **Link de acesso (BV):** https://plataforma.bvirtual.com.br/
- **Aula em que entra:** Aulas 9 a 12

### Para mergulhar no assunto

> Recomendo o livro **"Fundamentals of Data Engineering"**, de Joe Reis e Matt Housley (O'Reilly). É a obra que melhor mapeia o ciclo de vida da engenharia de dados moderna — do armazenamento (DW, lake, lakehouse) à arquitetura na nuvem e à Modern Data Stack. Os capítulos sobre armazenamento e arquitetura conversam diretamente com tudo o que vimos nesta unidade e ajudam a enxergar as peças como um sistema coeso, não como ferramentas soltas.

- **Link(s):** https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/
- **Aula em que entra:** Aulas 10 e 12

### Podcast (curadoria, até 45 min)

> O canal **Databricks** no YouTube traz palestras e explicações diretas da fonte sobre **Data Lakehouse, Delta Lake e arquitetura Medallion** — exatamente os temas da Aula 10. Assistir a um dos vídeos de fundamentos do Lakehouse fixa os conceitos com quem cunhou o termo e mostra a tecnologia em operação real.

- **Nome do podcast/canal:** Databricks (canal oficial no YouTube)
- **Tema recomendado:** "What is a Data Lakehouse?" / fundamentos de Delta Lake e arquitetura Medallion
- **Link:** https://www.youtube.com/@Databricks (YouTube)
- **Aula em que entra:** Aula 10

### Artigo científico

> Artigo seminal que define os fundamentos de **data warehousing e tecnologia OLAP** — desde a arquitetura em camadas até modelagem multidimensional e técnicas de servidor OLAP. É a base conceitual sobre a qual toda a Aula 9 (e boa parte da unidade) está construída; leitura essencial para fundamentar argumentos sobre por que o DW existe e como ele difere do OLTP.

- **Link:** https://doi.org/10.1145/248603.248616 (DOI)
- **Aula em que entra:** Aula 9
- **Referência bibliográfica do artigo no formato ABNT:**
  > CHAUDHURI, Surajit; DAYAL, Umeshwar. **An overview of data warehousing and OLAP technology**. *ACM SIGMOD Record*, v. 26, n. 1, p. 65-74, mar. 1997.
