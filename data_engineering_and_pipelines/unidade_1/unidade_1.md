# Unidade 1 — Fundamentos de Engenharia de Dados

- **Disciplina:** Data Engineering and Pipelines
- **Conteudista:** Afonso Cesar Lelis Brandão
- **Videoaulas desta unidade:** 1 a 4

## Vídeo introdutório + Relação da disciplina com a atuação profissional

Você já reparou que **toda aplicação moderna que você usa — Netflix, iFood, Nubank, Spotify — é, no fundo, uma máquina de mover dados**? Quando o Netflix te recomenda uma série, alguém precisou coletar seu histórico, mover esse dado de um servidor para outro, limpá-lo, juntá-lo com o de milhões de outros usuários e entregá-lo, em segundos, para o modelo que faz a recomendação. Esse "alguém" é o **engenheiro de dados** — e essa cadeia de coleta, transporte e transformação é o **pipeline de dados**. É exatamente isso que você vai aprender a construir nesta disciplina.

A engenharia de dados é hoje uma das carreiras mais bem pagas e mais demandadas da área de tecnologia. Enquanto o cientista de dados ganha as manchetes treinando modelos de IA, é o engenheiro de dados quem constrói a fundação invisível sobre a qual todo modelo, dashboard e relatório dependem. Sem dado limpo, organizado e disponível, não há ciência de dados, não há BI, não há IA. Por isso costuma-se dizer que **80% do esforço de qualquer projeto de dados é engenharia de dados** — e quem domina essa parte se torna indispensável.

Vamos começar do absoluto zero: o que é engenharia de dados, qual o ciclo de vida do dado, que formatos e bancos existem, como modelar informação para análise. Sem assumir conhecimento prévio. Mas chegando ao ponto de você entender ferramentas reais de mercado — Parquet, PostgreSQL, MongoDB, Cassandra, data warehouses — e saber **por que** cada uma existe. Ao final das quatro unidades, você será capaz de projetar e operar pipelines de ponta a ponta, exatamente como um profissional faz no mercado.

### Roteiro do vídeo introdutório (até 2 min)

**Abertura (0:00 – 0:20):**
> "Olá! Eu sou o professor Afonso Brandão. Seja muito bem-vindo(a) à disciplina Data Engineering and Pipelines. Se você quer entender como os dados saem dos sistemas, viram informação confiável e chegam aos modelos de IA e aos dashboards, você está no lugar certo."

**Conexão com o mercado (0:20 – 0:55):**
> "Engenharia de dados é uma das carreiras que mais cresce em tecnologia. Antes de qualquer cientista de dados treinar um modelo, alguém precisa coletar, mover e organizar o dado. Esse alguém é o engenheiro de dados — e o mercado paga muito bem por essa habilidade, porque sem ela nada funciona."

**Conteúdo e diferencial (0:55 – 1:25):**
> "A gente começa do zero: o que é dado, qual o ciclo de vida, que formatos e bancos existem. Depois sobe para ingestão e processamento, em batch e streaming. Na sequência, orquestração e qualidade. E, por fim, nuvem e arquiteturas modernas. Tudo com ferramentas reais — Parquet, PostgreSQL, MongoDB, Spark, Airflow."

**Benefício para o aluno (1:25 – 1:45):**
> "Ao final, você consegue **projetar** um pipeline do zero, **escolher** a tecnologia certa para cada problema e **defender** tecnicamente cada decisão de arquitetura. Diferencial real para quem está entrando no mercado de dados."

**Encerramento (1:45 – 2:00):**
> "Bora! Engenharia de dados é a fundação invisível de tudo que é digital hoje. Vem comigo entender essa fundação. Te espero na Aula 1!"

---

## Aula 1 — O que é Engenharia de Dados? Papel, ciclo de vida e diferença para a Ciência de Dados

Imagine que você quer cozinhar um prato sofisticado. O chef (cientista de dados) só consegue brilhar se alguém comprou os ingredientes, lavou, cortou e deixou tudo organizado na bancada. Esse trabalho de bastidor — comprar, transportar, limpar e organizar — é a **engenharia de dados**. Nesta aula você vai entender o que é essa disciplina, qual o ciclo de vida que o dado percorre e por que o papel do engenheiro de dados é diferente (e complementar) ao do cientista e do analista.

### O profissional de dados e suas fronteiras

A **engenharia de dados** é a disciplina que projeta, constrói e mantém os sistemas que **coletam, armazenam, transportam e transformam dados** em escala, de forma confiável, deixando-os prontos para consumo. O produto final do engenheiro de dados não é um modelo nem um gráfico — é o **dado disponível, íntegro e organizado** que outras pessoas vão consumir.

O engenheiro de dados opera na fronteira entre dois mundos: de um lado, os **sistemas-fonte** (aplicações, bancos transacionais, APIs, sensores) que produzem dados; do outro, os **consumidores** (cientistas de dados, analistas, dashboards, modelos de machine learning). Sua missão é construir a "tubulação" que liga esses dois lados de forma automatizada e resiliente. É um trabalho de engenharia de verdade: envolve software, infraestrutura, redes e bancos de dados.

![Computação em nuvem — base da infraestrutura moderna de engenharia de dados](https://commons.wikimedia.org/wiki/Special:FilePath/Cloud_computing.svg)

### O ciclo de vida da engenharia de dados

O livro *Fundamentals of Data Engineering* (Reis & Housley, O'Reilly) popularizou um modelo de **ciclo de vida** que organiza tudo que o engenheiro de dados faz. São cinco etapas principais, sustentadas por correntes transversais:

| Etapa | O que acontece |
| --- | --- |
| **Geração** | O dado nasce nos sistemas-fonte (apps, bancos, APIs, sensores) |
| **Ingestão** | O dado é coletado e movido para a plataforma de dados |
| **Transformação** | O dado é limpo, validado, agregado e enriquecido |
| **Armazenamento** | O dado é persistido (data lake, warehouse, banco) |
| **Disponibilização** | O dado é servido para análise, BI, ML e produtos de dados |

Atravessando todas essas etapas estão as **correntes transversais** (undercurrents): **segurança**, **governança e qualidade de dados**, **gestão de metadados**, **orquestração** e **engenharia de software**. Elas não são uma "etapa" — são preocupações que existem em **todas** as etapas. Por exemplo, segurança importa tanto na ingestão quanto na disponibilização.

### Engenheiro de dados vs cientista vs analista

A confusão entre esses três papéis é o erro mais comum de quem está entrando na área. A tabela esclarece:

| Aspecto | Engenheiro de dados | Cientista de dados | Analista de dados |
| --- | --- | --- | --- |
| **Foco** | Mover e preparar dado | Criar modelos preditivos | Explicar o que aconteceu |
| **Entrega** | Pipeline, tabela confiável | Modelo, previsão | Relatório, dashboard |
| **Pergunta** | "Como levo o dado até lá?" | "O que vai acontecer?" | "O que aconteceu?" |
| **Ferramentas** | Spark, Airflow, SQL, Python | Python, scikit-learn, ML | SQL, Power BI, Excel |

A relação é de dependência: o **engenheiro de dados é a base**. Sem dado confiável e disponível, o cientista não treina e o analista não analisa. Há um ditado no mercado: "garbage in, garbage out" — se o dado que entra é lixo, qualquer modelo ou relatório também será lixo. Garantir que o dado **não** seja lixo é, em grande parte, trabalho de engenharia.

### Onde os dados nascem: os sistemas-fonte

Todo dado começa em um **sistema-fonte**. Os mais comuns:

- **Bancos transacionais (OLTP)** — o banco do e-commerce, do banco, do ERP. Ex.: PostgreSQL, MySQL, Oracle.
- **APIs** — interfaces que outras empresas expõem (ex.: API de pagamento, API do clima).
- **Arquivos** — CSVs exportados, logs de servidor, planilhas.
- **Streams / eventos** — fluxos contínuos de cliques, sensores IoT, transações em tempo real.

O engenheiro de dados precisa **entender o sistema-fonte sem controlá-lo**. Geralmente quem mantém o sistema-fonte é outra equipe (desenvolvimento, produto). Mudanças no sistema-fonte — uma coluna que muda de nome, um campo que vira nulo — podem quebrar o pipeline. Por isso, parte do trabalho é negociar **contratos de dados** (data contracts) com os times de origem.

### O conceito de pipeline de dados

Um **pipeline de dados** é uma sequência automatizada de passos que move o dado da origem ao destino, aplicando transformações no caminho. Dois padrões clássicos:

- **ETL (Extract, Transform, Load)** — extrai, transforma **antes** de carregar. Modelo tradicional, comum quando o destino é caro/limitado.
- **ELT (Extract, Load, Transform)** — extrai, carrega o dado bruto e transforma **depois**, dentro do destino. Modelo moderno, viável porque o armazenamento na nuvem ficou barato e os warehouses ficaram poderosos.

A diferença está na ordem do "T". No ELT, você guarda o dado bruto primeiro (o que dá flexibilidade para reprocessar) e transforma sob demanda. É a abordagem dominante hoje em ferramentas como dbt + BigQuery/Snowflake.

### Exemplo numérico: volume e custo de dados

Suponha um e-commerce que registra **2 milhões de eventos por dia** (cliques, buscas, compras). Cada evento ocupa, em média, $1{,}5\,\text{KB}$ no formato bruto (JSON). Quanto isso gera por ano e quanto custaria armazenar?

Volume diário:

$$
2\,000\,000 \times 1{,}5\,\text{KB} = 3\,000\,000\,\text{KB} = 3\,\text{GB/dia}
$$

Volume anual:

$$
3\,\text{GB/dia} \times 365\,\text{dias} \approx 1\,095\,\text{GB} \approx 1{,}07\,\text{TB/ano}
$$

Em um armazenamento de objetos na nuvem (preço típico de $0{,}023$ dólares por GB ao mês), o custo mensal ao final do ano seria:

$$
1\,095\,\text{GB} \times 0{,}023\,\text{US\$/GB} \approx 25{,}2\,\text{US\$/mês}
$$

Repare como armazenar dado bruto é **barato**: pouco mais de 25 dólares por mês para 1 TB. É justamente esse baixo custo que torna o padrão ELT (guardar tudo cru e transformar depois) economicamente viável.

### Atividade prática

Escolha um aplicativo que você usa diariamente (Instagram, iFood, Uber, banco). Faça o exercício de "engenheiro de dados reverso":

1. Liste **três sistemas-fonte** prováveis desse app (banco de pedidos, API de mapas, stream de cliques...).
2. Para cada um, classifique como **OLTP, API, arquivo ou stream**.
3. Desenhe, em uma frase, **um pipeline** que levaria o dado de cliques desse app até um dashboard de "produtos mais vistos".
4. Indique se você usaria **ETL ou ELT** e justifique.

### Pontos-chave

- **Engenharia de dados** projeta e mantém os sistemas que coletam, movem, transformam e disponibilizam dados em escala e com confiabilidade.
- O **ciclo de vida** tem cinco etapas — geração, ingestão, transformação, armazenamento, disponibilização — sustentadas por correntes transversais (segurança, governança, metadados, orquestração, engenharia de software).
- O **engenheiro de dados é a base**: sem dado confiável, não há ciência de dados nem análise ("garbage in, garbage out").
- Dados nascem em **sistemas-fonte** (OLTP, APIs, arquivos, streams), que o engenheiro entende mas não controla.
- **ETL** transforma antes de carregar; **ELT** carrega o dado bruto e transforma depois — padrão dominante na nuvem moderna.

### Para saber mais

- **Reis, J.; Housley, M.** *Fundamentals of Data Engineering*. O'Reilly, 2022 — capítulo 1 e 2 (definição e ciclo de vida).
- **Engenharia de dados (Wikipedia, em inglês):** https://en.wikipedia.org/wiki/Data_engineering
- **dbt — What is ELT?** https://www.getdbt.com/blog/extract-load-transform
- **Vídeo (Seattle Data Guy, YouTube):** "What Does a Data Engineer Actually Do?"

## Aula 1 — Roteiro da Videoaula 1: "O que é Engenharia de Dados? Papel, ciclo de vida e diferença para a Ciência de Dados"

### 1. Abertura (0:00 – 0:40)

> "Quando o Netflix te recomenda uma série, alguém teve que coletar, mover e organizar milhões de dados antes do modelo agir. Esse alguém é o engenheiro de dados. Hoje a gente vai entender exatamente o que essa pessoa faz — e por que esse papel é a fundação de tudo em dados."

### 2. Desenvolvimento — parte 1 (0:40 – 4:00)

> "Engenharia de dados é a disciplina que constrói a tubulação dos dados — da origem ao consumo. O produto não é um gráfico nem um modelo; é o dado disponível, íntegro e organizado. Vamos olhar o ciclo de vida: geração, ingestão, transformação, armazenamento e disponibilização. E as correntes transversais que atravessam tudo: segurança, governança, metadados, orquestração e engenharia de software."

### 3. Desenvolvimento — parte 2 (4:00 – 7:00)

> "Agora a confusão clássica: engenheiro de dados, cientista de dados e analista. O engenheiro move e prepara o dado; o cientista cria modelos preditivos; o analista explica o que aconteceu. A relação é de dependência — o engenheiro é a base. Garbage in, garbage out: se o dado é lixo, o modelo também será. Garantir que não seja lixo é trabalho de engenharia."

### 4. Desenvolvimento — parte 3 (7:00 – 9:00)

> "De onde vem o dado? Dos sistemas-fonte: bancos OLTP, APIs, arquivos e streams. E como ele se move? Por pipelines. Dois padrões: ETL, que transforma antes de carregar, e ELT, que carrega o bruto e transforma depois. Hoje, com armazenamento na nuvem barato, o ELT domina — armazenar 1 TB custa cerca de 25 dólares por mês."

### 5. Encerramento (9:00 – 11:00)

> "Você já entende o papel, o ciclo de vida e as fronteiras. Na próxima aula, a gente desce um nível: os tipos, formatos e fontes de dados — estruturado, semiestruturado, não estruturado, CSV, JSON, Parquet, Avro. É o vocabulário que você vai usar todo dia. Te espero!"

---

## Aula 2 — Tipos, formatos e fontes de dados

Se na Aula 1 você entendeu o **papel** do engenheiro de dados, agora vamos olhar a **matéria-prima** com que ele trabalha: o dado em si. Dado não é tudo igual. Existe dado que vem arrumadinho em tabela e dado que é uma foto, um áudio, um texto livre. Existe arquivo que ocupa pouco e arquivo que ocupa muito. Escolher o tipo e o formato certo pode significar a diferença entre um pipeline que custa centavos e um que custa milhares. Esta aula constrói esse vocabulário essencial.

### Dados estruturados, semi-estruturados e não estruturados

A primeira grande classificação do dado é pelo **grau de estrutura**:

| Tipo | Definição | Exemplos | Onde vive |
| --- | --- | --- | --- |
| **Estruturado** | Organizado em tabela, com colunas e tipos definidos | Tabela de pedidos, planilha | Bancos relacionais |
| **Semi-estruturado** | Tem estrutura, mas flexível e aninhada | JSON, XML, logs | NoSQL, data lakes |
| **Não estruturado** | Sem esquema fixo | Texto livre, imagem, áudio, vídeo | Object storage, data lakes |

Estima-se que **cerca de 80% dos dados gerados no mundo sejam não estruturados** — fotos, vídeos, áudios, documentos. Por muito tempo esses dados foram "invisíveis" para a análise tradicional; foi a combinação de data lakes baratos e IA que os tornou utilizáveis. O engenheiro de dados precisa saber lidar com os três tipos, porque eles convivem na mesma empresa.

### Formatos de arquivo: CSV, JSON, Parquet, Avro

Dentro do dado estruturado e semiestruturado, o **formato de arquivo** importa muito. Os quatro mais usados em engenharia de dados:

- **CSV** — texto puro, linhas e colunas separadas por vírgula. Simples, universal, legível por humanos. Porém **sem tipos** (tudo é texto), sem compressão nativa e ineficiente para grandes volumes.
- **JSON** — texto hierárquico (chave-valor), ótimo para dado semiestruturado e APIs. Flexível, mas **verboso** (repete os nomes dos campos em cada registro) e lento de processar em escala.
- **Parquet** — formato **colunar e comprimido**, binário. Padrão de mercado para analytics. Guarda os dados por coluna, o que permite ler só as colunas necessárias e comprimir muito bem.
- **Avro** — formato **por linha (row-based)** e binário, com esquema embutido. Excelente para **ingestão e streaming**, onde você escreve registros completos rapidamente.

A regra prática: **CSV/JSON para troca e ingestão; Parquet para analytics; Avro para streaming e evolução de esquema**. Saber escolher é o que separa o pipeline eficiente do desperdício.

![Comparação esquemática entre armazenamento orientado a linhas e armazenamento orientado a colunas em bancos de dados](https://commons.wikimedia.org/wiki/Special:FilePath/Row_and_column_major_order.svg)

### Bancos transacionais como sistema-fonte

A fonte de dado estruturado mais comum é o **banco transacional (OLTP)** que roda por trás de uma aplicação. Quando você compra algo, uma linha é inserida na tabela `pedidos`; quando paga, outra na tabela `pagamentos`. Esses bancos são otimizados para **escritas e leituras pequenas e rápidas**.

O engenheiro de dados extrai dado desses bancos de duas formas principais: **snapshot** (uma cópia completa da tabela periodicamente) ou **CDC — Change Data Capture** (captura apenas as mudanças, lendo o log de transações do banco). CDC é mais eficiente e mantém o destino quase em tempo real, e será aprofundado na Unidade 2.

### APIs, arquivos e streams

Nem todo dado vem de banco. Três outras fontes importantes:

- **APIs (REST/GraphQL)** — você faz uma requisição HTTP e recebe, normalmente, **JSON**. Comum para integrar dados de terceiros (clima, câmbio, redes sociais). Exige tratar paginação, limites de requisição (rate limit) e autenticação.
- **Arquivos** — CSVs e logs depositados em uma pasta ou bucket. Padrão clássico de troca entre empresas (ex.: o banco envia um arquivo de extrato diário).
- **Streams** — fluxos contínuos de eventos, processados conforme chegam. Tecnologias como **Apache Kafka** transportam milhões de eventos por segundo. É a base de aplicações em tempo real (detecção de fraude, recomendação ao vivo).

### Schema-on-read vs schema-on-write

Um conceito que diferencia abordagens modernas das tradicionais:

- **Schema-on-write** — você define o esquema **antes** de gravar. O banco rejeita qualquer dado fora do formato. Garante qualidade na entrada, mas é rígido. É como o banco relacional clássico.
- **Schema-on-read** — você grava o dado bruto **sem** esquema e o interpreta apenas na hora de ler. Flexível, ideal para data lakes, mas transfere a responsabilidade da qualidade para o momento da leitura. É como guardar arquivos JSON crus e estruturá-los na consulta.

Não há vencedor absoluto: data warehouses tendem ao schema-on-write (qualidade garantida); data lakes nasceram schema-on-read (flexibilidade). Arquiteturas modernas como o *lakehouse* tentam o melhor dos dois.

### Exemplo numérico: ganho da compressão colunar

Considere uma tabela de eventos com **10 milhões de linhas** e $20$ colunas, ocupando $4\,\text{GB}$ em CSV. Você quer responder a uma consulta que usa **apenas 3 colunas**. Compare CSV com Parquet.

**Em CSV**, o motor precisa ler o arquivo inteiro, pois as linhas misturam todas as colunas:

$$
\text{Leitura CSV} = 4\,\text{GB (arquivo todo)}
$$

**Em Parquet**, armazenamento colunar lê só as 3 colunas necessárias e aplica compressão típica de $5\times$. A fração de colunas lidas é $\frac{3}{20} = 0{,}15$:

$$
\text{Tamanho Parquet} = \frac{4\,\text{GB}}{5} = 0{,}8\,\text{GB}
$$

$$
\text{Leitura efetiva} = 0{,}8\,\text{GB} \times 0{,}15 = 0{,}12\,\text{GB} = 120\,\text{MB}
$$

Resultado: a consulta lê $120\,\text{MB}$ em vez de $4\,\text{GB}$ — uma redução de cerca de **33 vezes** no volume lido. Como o custo de consulta na nuvem costuma ser proporcional ao dado lido, isso significa pagar 33 vezes menos pela mesma resposta. É por isso que Parquet é o padrão de analytics.

### Atividade prática

Pegue um conjunto de dados público pequeno (por exemplo, um CSV do portal [dados.gov.br](https://dados.gov.br)) e responda:

1. O dado é **estruturado, semi-estruturado ou não estruturado**? Justifique.
2. Liste **duas vantagens e duas desvantagens** de mantê-lo em CSV.
3. Se esse dado tivesse 100 milhões de linhas e fosse consultado todo dia em um dashboard, qual formato você escolheria (**CSV, JSON, Parquet ou Avro**) e por quê?
4. A fonte é **schema-on-read ou schema-on-write**? O que mudaria se fosse a outra?

### Pontos-chave

- Dados se classificam em **estruturados, semi-estruturados e não estruturados** — e cerca de 80% do total mundial é não estruturado.
- Os quatro formatos essenciais: **CSV** (simples, ineficiente), **JSON** (flexível, verboso), **Parquet** (colunar, ótimo para analytics), **Avro** (por linha, ótimo para streaming).
- Sistemas-fonte vêm em quatro sabores: **bancos OLTP, APIs, arquivos e streams** — cada um com sua técnica de extração.
- **Schema-on-write** garante qualidade na entrada (rígido); **schema-on-read** dá flexibilidade ao custo de validar só na leitura.
- A escolha de formato tem impacto direto no custo: o armazenamento **colunar comprimido** pode reduzir o dado lido em dezenas de vezes.

### Para saber mais

- **Apache Parquet — documentação oficial:** https://parquet.apache.org/docs/
- **Apache Avro — documentação oficial:** https://avro.apache.org/docs/
- **JSON (Wikipedia):** https://pt.wikipedia.org/wiki/JSON
- **Vídeo (Data with Zach, YouTube):** "CSV vs Parquet — Why columnar formats win"

## Aula 2 — Roteiro da Videoaula 2: "Tipos, formatos e fontes de dados"

### 1. Abertura (0:00 – 0:40)

> "Dado não é tudo igual. Tem dado arrumadinho em tabela, tem foto, áudio, texto livre. Tem arquivo que ocupa pouco e arquivo que custa caro de processar. Hoje a gente constrói o vocabulário da matéria-prima do engenheiro de dados — e isso vai te poupar muito dinheiro lá na frente."

### 2. Desenvolvimento — parte 1 (0:40 – 4:00)

> "Primeira classificação: estruturado, semiestruturado e não estruturado. Tabela, JSON e foto. Cerca de 80% do dado mundial é não estruturado. Depois, os formatos: CSV é simples mas ineficiente; JSON é flexível mas verboso; Parquet é colunar e comprimido, padrão de analytics; Avro é por linha, ótimo para streaming."

### 3. Desenvolvimento — parte 2 (4:00 – 7:00)

> "De onde vem o dado? De bancos OLTP — que extraímos por snapshot ou por CDC; de APIs, que devolvem JSON e exigem tratar paginação e rate limit; de arquivos depositados em buckets; e de streams, como o Kafka, que carregam milhões de eventos por segundo. Cada fonte tem sua técnica de captura."

### 4. Desenvolvimento — parte 3 (7:00 – 9:00)

> "Schema-on-write versus schema-on-read. No primeiro, você define o esquema antes de gravar — qualidade garantida, mas rígido. No segundo, grava o bruto e interpreta só na leitura — flexível, mas a validação fica para depois. E o exemplo que prova o poder do colunar: a mesma consulta lê 120 megabytes em Parquet contra 4 gigabytes em CSV. Trinta e três vezes menos."

### 5. Encerramento (9:00 – 11:00)

> "Agora você conhece os tipos, formatos e fontes. Na próxima aula, a gente entra nos bancos de dados de verdade: relacional contra NoSQL, ACID, as famílias NoSQL e o teorema CAP. É onde o dado realmente mora. Te espero!"

---

## Aula 3 — Bancos de dados para engenharia: relacional vs NoSQL

Toda empresa precisa **guardar** dados em algum lugar — e esse lugar é um banco de dados. Por décadas, "banco de dados" significava "banco relacional". Mas a explosão da web, das redes sociais e dos sensores trouxe casos de uso que o modelo relacional não atendia bem, e nasceu o movimento **NoSQL**. Nesta aula você vai entender os dois mundos, as propriedades que garantem confiabilidade (ACID), as famílias NoSQL e o famoso teorema CAP — que explica por que, em sistemas distribuídos, você não pode ter tudo ao mesmo tempo.

### O modelo relacional e o SQL

O **modelo relacional**, proposto por Edgar F. Codd em 1970, organiza os dados em **tabelas (relações)** com linhas e colunas. Cada tabela representa uma entidade (Clientes, Pedidos), cada linha é um registro, cada coluna um atributo. As tabelas se conectam por **chaves**: a **chave primária** identifica unicamente cada linha; a **chave estrangeira** referencia outra tabela.

A linguagem para manipular bancos relacionais é o **SQL (Structured Query Language)** — provavelmente a habilidade mais duradoura e valiosa de toda a área de dados. Exemplos de bancos relacionais: **PostgreSQL, MySQL, Oracle, SQL Server**. O modelo relacional brilha quando os dados têm estrutura bem definida e quando a **integridade** (consistência das relações) é crítica — como em sistemas financeiros.

![Diagrama de um banco de dados relacional mostrando chaves primárias e estrangeiras ligando tabelas](https://commons.wikimedia.org/wiki/Special:FilePath/Relational_key_SVG.svg)

### Propriedades ACID

O que torna um banco relacional confiável para transações é o conjunto de propriedades **ACID**. Cada letra é uma garantia:

| Letra | Propriedade | O que garante |
| --- | --- | --- |
| **A** | Atomicidade | A transação acontece toda ou nada — não há meio-termo |
| **C** | Consistência | A transação leva o banco de um estado válido a outro válido |
| **I** | Isolamento | Transações simultâneas não interferem entre si |
| **D** | Durabilidade | Uma vez confirmada, a transação sobrevive a falhas/quedas |

O exemplo clássico é uma **transferência bancária**: debitar de uma conta e creditar em outra precisam acontecer **juntos**. Se o sistema cair entre as duas operações, a atomicidade garante que **nada** aconteça (não some dinheiro). É por isso que sistemas financeiros, fiscais e de estoque dependem de bancos ACID.

### As famílias NoSQL (chave-valor, documento, coluna, grafo)

**NoSQL** ("Not Only SQL") reúne bancos que abrem mão de parte da rigidez relacional em troca de **escala, flexibilidade ou desempenho**. São quatro famílias principais:

- **Chave-valor** (Redis, DynamoDB) — guarda pares simples `chave → valor`. Extremamente rápido. Ideal para cache, sessões, contadores.
- **Documento** (MongoDB, Couchbase) — guarda documentos JSON com esquema flexível. Ideal quando os dados são aninhados e variam de registro para registro (catálogos de produtos, perfis).
- **Coluna larga / colunar** (Cassandra, HBase, ScyllaDB) — organiza por colunas e famílias de colunas, otimizado para **escritas massivas** e leituras analíticas. Ideal para séries temporais e IoT.
- **Grafo** (Neo4j, Amazon Neptune) — guarda **entidades e suas relações**. Ideal para redes sociais, detecção de fraude e mecanismos de recomendação, onde a conexão entre os dados é o que importa.

Não existe "NoSQL melhor que SQL" — existe a ferramenta certa para cada problema. Em uma arquitetura moderna, **convivem** vários: o relacional para transações, o documento para catálogos, o colunar para sensores, o grafo para relacionamentos.

### Teorema CAP e consistência

Quando um banco é **distribuído** (roda em vários servidores para aguentar escala), surge um dilema descrito pelo **teorema CAP**. Ele afirma que, na presença de uma **partição de rede** (P, falha de comunicação entre os nós), um sistema só pode garantir **uma** entre duas propriedades:

- **C — Consistência:** toda leitura retorna o dado mais recente, ou um erro.
- **A — Disponibilidade:** toda requisição recebe uma resposta (mesmo que não seja a mais recente).
- **P — Tolerância a partição:** o sistema continua operando apesar de falhas de comunicação na rede.

Como partições de rede são **inevitáveis** em sistemas distribuídos, o P é obrigatório na prática. A escolha real é entre **CP** (priorizar consistência, sacrificando disponibilidade durante a partição) e **AP** (priorizar disponibilidade, aceitando dados temporariamente inconsistentes). MongoDB e HBase tendem a CP; Cassandra e DynamoDB tendem a AP, oferecendo **consistência eventual** (o dado fica consistente "em algum momento").

### Quando escolher cada modelo

Um guia prático de decisão:

| Necessidade | Escolha típica |
| --- | --- |
| Transações financeiras, integridade rígida | Relacional (ACID) |
| Cache, sessões, ranking em tempo real | Chave-valor |
| Catálogo flexível, perfis, JSON aninhado | Documento |
| IoT, logs, séries temporais, escrita massiva | Coluna larga |
| Redes sociais, fraude, recomendação | Grafo |

A pergunta-guia é sempre: **qual o padrão de acesso?** Muitas escritas pequenas? Leituras analíticas pesadas? Relações complexas? O padrão de acesso, e não a moda, define o banco.

### Exemplo numérico: throughput de escrita

Imagine uma plataforma de IoT que recebe leituras de **50 000 sensores**, cada um enviando $1$ medição por segundo. Quantas escritas por segundo o banco precisa suportar?

$$
\text{Escritas/s} = 50\,000\,\text{sensores} \times 1\,\frac{\text{medição}}{\text{s}} = 50\,000\,\text{escritas/s}
$$

Um banco relacional típico, com garantias ACID completas, suporta tipicamente algo na faixa de $5\,000$ a $10\,000$ escritas por segundo em um único nó. Quantos nós relacionais seriam necessários?

$$
\text{Nós necessários} = \frac{50\,000}{8\,000} \approx 6{,}25 \rightarrow 7\,\text{nós}
$$

Já um banco colunar distribuído como o **Cassandra**, otimizado para escrita, suporta na ordem de $50\,000$ escritas por segundo em **poucos nós**, com escalabilidade horizontal linear. Conclusão: para esse perfil de **escrita massiva e contínua**, o NoSQL colunar é a escolha natural — não por ser "melhor", mas por casar com o padrão de acesso.

### Pausa para reflexão (Desafio)

> Pense no app do seu banco. Quando você transfere dinheiro, o saldo precisa estar **sempre correto** — nem que para isso a operação demore ou falhe (priorização da **consistência**). Agora pense no Instagram: se a contagem de curtidas de uma foto ficar alguns segundos desatualizada, ninguém se importa — o que não pode é o app sair do ar (priorização da **disponibilidade**). **Desafio:** escolha dois aplicativos que você usa e classifique cada um como "CP" ou "AP" segundo o teorema CAP. Justifique pela natureza do negócio: o que é pior nesse app, mostrar dado errado por um instante ou ficar indisponível?

### Atividade prática

Para cada cenário abaixo, escolha o **modelo de banco** mais adequado e justifique em uma frase:

1. Um sistema de carrinho de compras que precisa lembrar os itens enquanto o usuário navega (alta velocidade, dado temporário).
2. Um catálogo de produtos onde cada item tem atributos diferentes (roupa tem tamanho; eletrônico tem voltagem).
3. Uma rede de transporte que precisa achar o caminho mais curto entre estações.
4. Um sistema de folha de pagamento, onde nenhum centavo pode se perder.

Em seguida, indique quais desses precisam de **ACID** e quais podem viver com **consistência eventual**.

### Pontos-chave

- O **modelo relacional** (tabelas + chaves + SQL) é ideal para dados estruturados e integridade rígida; SQL é a habilidade mais valiosa e duradoura da área.
- As propriedades **ACID** (atomicidade, consistência, isolamento, durabilidade) tornam o banco confiável para transações financeiras e fiscais.
- O **NoSQL** tem quatro famílias — **chave-valor, documento, coluna larga e grafo** — cada uma para um padrão de acesso diferente.
- O **teorema CAP** mostra que, com partição de rede inevitável, escolhe-se entre **consistência (CP)** e **disponibilidade (AP)**.
- A escolha do banco deve seguir o **padrão de acesso** do problema, não a moda — relacional e NoSQL **convivem** em arquiteturas reais.

### Para saber mais

- **Kleppmann, M.** *Designing Data-Intensive Applications*. O'Reilly, 2017 — capítulos 2, 5 e 9 (modelos, replicação e consistência).
- **Teorema CAP (Wikipedia):** https://pt.wikipedia.org/wiki/Teorema_CAP
- **PostgreSQL — documentação oficial:** https://www.postgresql.org/docs/
- **MongoDB Manual:** https://www.mongodb.com/docs/manual/

## Aula 3 — Roteiro da Videoaula 3: "Bancos de dados para engenharia: relacional vs NoSQL"

### 1. Abertura (0:00 – 0:40)

> "Por décadas, banco de dados era sinônimo de banco relacional. Aí veio a web, as redes sociais, os sensores — e surgiu o NoSQL. Hoje a gente entende os dois mundos, o que torna um banco confiável e por que, em sistemas distribuídos, você não pode ter tudo ao mesmo tempo."

### 2. Desenvolvimento — parte 1 (0:40 – 4:00)

> "O modelo relacional, do Codd em 1970, organiza tudo em tabelas ligadas por chaves, e se fala com ele em SQL — a habilidade mais valiosa da área. O que o torna confiável é o ACID: atomicidade, consistência, isolamento e durabilidade. Pensa numa transferência bancária: debitar e creditar acontecem juntos, ou nada acontece. Por isso finanças vivem em banco relacional."

### 3. Desenvolvimento — parte 2 (4:00 – 7:00)

> "O NoSQL abre mão de parte da rigidez por escala e flexibilidade. São quatro famílias: chave-valor, como Redis, para cache; documento, como MongoDB, para JSON flexível; coluna larga, como Cassandra, para escrita massiva e IoT; e grafo, como Neo4j, para relações. Não existe melhor — existe o certo para cada padrão de acesso."

### 4. Desenvolvimento — parte 3 (7:00 – 9:00)

> "O teorema CAP: com partição de rede, que é inevitável, você escolhe entre consistência e disponibilidade. CP, como o MongoDB, prioriza dado correto; AP, como o Cassandra, prioriza estar sempre no ar, aceitando consistência eventual. E o exemplo: 50 mil sensores escrevendo por segundo precisam de 7 nós relacionais, mas poucos nós Cassandra. O padrão de acesso decide."

### 5. Encerramento (9:00 – 11:00)

> "Você já sabe onde o dado mora e como escolher. Na próxima aula, a gente sobe para a modelagem analítica: OLTP versus OLAP, esquema estrela, fatos e dimensões, e o conceito de Slowly Changing Dimensions. É como o dado vira insight. Te espero!"

---

## Aula 4 — Modelagem de dados: OLTP, OLAP e modelagem dimensional

Até aqui, falamos de dado que **opera** o negócio: o pedido sendo feito, o pagamento sendo registrado. Mas existe outro mundo: o dado que **analisa** o negócio — quanto vendemos por região no último trimestre, qual produto cresce mês a mês. Esses dois mundos exigem **modelagens diferentes**. Nesta aula você vai entender a diferença entre OLTP e OLAP e dominar a **modelagem dimensional**, criada por Ralph Kimball, que é o padrão para data warehouses até hoje.

### OLTP vs OLAP

São dois propósitos opostos para um banco de dados:

| Aspecto | OLTP (transacional) | OLAP (analítico) |
| --- | --- | --- |
| **Objetivo** | Operar o negócio | Analisar o negócio |
| **Operação típica** | Inserir/atualizar 1 registro | Agregar milhões de registros |
| **Exemplo** | "Registrar o pedido 1234" | "Total de vendas por região no ano" |
| **Otimização** | Escrita rápida, muitos usuários | Leitura analítica, agregações |
| **Modelagem** | Normalizada | Dimensional (desnormalizada) |
| **Tecnologia** | PostgreSQL, MySQL | BigQuery, Snowflake, Redshift |

A regra: você **não** roda relatórios pesados em cima do banco OLTP de produção — isso o sobrecarrega e atrapalha a operação. O dado é **copiado** do mundo OLTP para um **data warehouse** OLAP, onde a análise acontece sem afetar a operação. Construir essa cópia (com transformações) é justamente o trabalho de engenharia de dados.

![Esquema estrela (star schema) com uma tabela de fatos central ligada a várias tabelas de dimensão](https://commons.wikimedia.org/wiki/Special:FilePath/Star-schema.png)

### Normalização e desnormalização

**Normalização** é o processo de eliminar redundância dividindo os dados em várias tabelas. No mundo OLTP, ela é desejável: se o telefone do cliente está em uma só tabela, basta atualizá-lo em um lugar. A normalização evita anomalias de atualização e economiza espaço — e bancos transacionais costumam estar na **3ª Forma Normal (3FN)**.

No mundo OLAP, porém, queremos o oposto: **desnormalização**. Juntar dados em poucas tabelas largas reduz a quantidade de *joins* (junções) que uma consulta analítica precisa fazer, deixando a leitura muito mais rápida. Aceitamos a redundância em troca de velocidade de análise. Essa troca consciente é o coração da modelagem dimensional.

### Esquema estrela e floco de neve

A modelagem dimensional organiza o data warehouse em dois esquemas clássicos:

- **Esquema estrela (star schema)** — uma **tabela de fatos** central ligada diretamente a várias **tabelas de dimensão**, formando uma estrela. As dimensões são **desnormalizadas** (cada uma é uma tabela única e larga). É simples, rápido e o padrão mais usado.
- **Esquema floco de neve (snowflake schema)** — variação em que as dimensões são **normalizadas**, quebrando-se em subtabelas (a dimensão Produto se divide em Produto → Categoria → Departamento). Economiza espaço, mas exige mais joins e fica mais lento.

Na prática, o **esquema estrela vence** na maioria dos casos: armazenamento é barato e simplicidade de consulta vale mais que economia de espaço.

### Fatos e dimensões

Os dois tipos de tabela da modelagem dimensional:

- **Tabela de fatos** — guarda os **eventos mensuráveis** do negócio, com **métricas numéricas** (quantidade, valor, custo) e **chaves** que apontam para as dimensões. É longa e estreita: muitas linhas, poucas colunas. Ex.: cada linha é uma venda.
- **Tabela de dimensão** — guarda o **contexto descritivo** que dá significado aos fatos: quem, o quê, quando, onde. É curta e larga: poucas linhas, muitas colunas. Ex.: dimensão Cliente (nome, cidade, segmento), dimensão Tempo (dia, mês, trimestre, ano), dimensão Produto.

A consulta analítica típica **filtra e agrupa pelas dimensões** e **soma as métricas dos fatos**: "some o valor (fato) das vendas, agrupando por mês (dimensão Tempo) e por região (dimensão Cliente)".

### Slowly Changing Dimensions (SCD)

Um problema real: e quando um atributo de dimensão **muda**? Por exemplo, um cliente muda de cidade. Como registrar isso sem corromper a história? É o que tratam as **Slowly Changing Dimensions (SCD)**:

| Tipo | Estratégia | Efeito |
| --- | --- | --- |
| **SCD Tipo 0** | Nunca muda | Atributo fixo (ex.: data de nascimento) |
| **SCD Tipo 1** | Sobrescreve | Perde a história, fica só o valor atual |
| **SCD Tipo 2** | Cria nova linha | Preserva a história completa, com datas de validade |
| **SCD Tipo 3** | Guarda valor anterior em coluna | Mantém apenas a versão anterior e a atual |

O **Tipo 2** é o mais importante: ao mudar a cidade do cliente, você **fecha** a linha antiga (com data de fim) e cria uma **nova** (com data de início), mantendo um indicador de "linha atual". Assim, uma venda feita no passado continua atribuída à cidade correta **na época**. Sem SCD Tipo 2, você reescreveria a história — e relatórios históricos ficariam errados.

### Exemplo numérico: tamanho da tabela-fato

Uma rede varejista tem **500 lojas** que processam, em média, **2 000 vendas por loja por dia**. Cada venda tem, em média, **4 itens**, e a granularidade da tabela de fatos é **um item por linha** (fato de venda no nível de item). Cada linha ocupa $80\,\text{bytes}$. Qual o tamanho da tabela de fatos em **um ano**?

Linhas por dia:

$$
500\,\text{lojas} \times 2\,000\,\frac{\text{vendas}}{\text{loja}} \times 4\,\frac{\text{itens}}{\text{venda}} = 4\,000\,000\,\text{linhas/dia}
$$

Linhas por ano:

$$
4\,000\,000\,\frac{\text{linhas}}{\text{dia}} \times 365\,\text{dias} = 1\,460\,000\,000\,\text{linhas/ano}
$$

Tamanho em bytes e em terabytes:

$$
1\,460\,000\,000 \times 80\,\text{bytes} = 116\,800\,000\,000\,\text{bytes} \approx 116{,}8\,\text{GB} \approx 0{,}11\,\text{TB/ano}
$$

São **1,46 bilhão de linhas** e cerca de $117\,\text{GB}$ por ano — só de fatos. Esse número justifica usar **formato colunar** (Parquet, da Aula 2) e um **banco OLAP** distribuído: rodar `GROUP BY` sobre 1,46 bilhão de linhas é exatamente o tipo de carga para o qual o data warehouse foi desenhado.

### Atividade prática

Modele um **mini data warehouse** para uma rede de cinemas. Os ingressos vendidos são o evento mensurável central. No papel:

1. Defina a **tabela de fatos** "Venda de Ingresso": que **métricas** numéricas ela teria (valor, quantidade)?
2. Defina **três tabelas de dimensão** (sugestões: Filme, Sala/Cinema, Tempo). Liste 3 atributos de cada.
3. Desenhe o **esquema estrela** ligando a fato às dimensões.
4. A dimensão Cinema poderia mudar (o cinema muda de gerente, de bairro). Qual **tipo de SCD** você usaria para preservar a história? Justifique.

### O que você verá na próxima unidade

Na **Unidade 2 — Ingestão e Processamento de Dados**, a gente coloca o dado em movimento. Vamos ver como **ingerir** dados de fontes diversas (batch e streaming, com Change Data Capture e Apache Kafka), e como **processá-los** em escala com motores como o Apache Spark. Você vai entender as diferenças entre processamento **em lote** e **em tempo real**, e como construir as transformações que limpam, juntam e enriquecem o dado — o coração de qualquer pipeline. É a hora em que a teoria desta unidade vira tubulação rodando.

### Pontos-chave

- **OLTP** opera o negócio (escrita rápida, normalizado); **OLAP** analisa o negócio (leitura agregada, dimensional) — e o dado é copiado de um para o outro.
- A **normalização** evita redundância no OLTP; a **desnormalização** acelera consultas no OLAP — é uma troca consciente.
- A **modelagem dimensional** usa **tabelas de fatos** (métricas numéricas) e **tabelas de dimensão** (contexto descritivo), no **esquema estrela**.
- **Slowly Changing Dimensions (SCD)** tratam mudanças nos atributos; o **Tipo 2** preserva a história criando novas linhas com validade.
- Tabelas de fatos crescem para **bilhões de linhas** — daí o uso de formato colunar e bancos OLAP distribuídos.

### Para saber mais

- **Kimball, R.; Ross, M.** *The Data Warehouse Toolkit*. 3ª ed. Wiley, 2013 — a bíblia da modelagem dimensional.
- **Esquema estrela (Wikipedia):** https://pt.wikipedia.org/wiki/Esquema_estrela
- **Slowly Changing Dimension (Wikipedia, em inglês):** https://en.wikipedia.org/wiki/Slowly_changing_dimension
- **Vídeo (Kahan Data Solutions, YouTube):** "Star Schema vs Snowflake Schema — Dimensional Modeling explained"

## Aula 4 — Roteiro da Videoaula 4: "Modelagem de dados: OLTP, OLAP e modelagem dimensional"

### 1. Abertura (0:00 – 0:40)

> "Existe o dado que opera o negócio — o pedido sendo feito — e o dado que analisa o negócio — quanto vendemos por região no trimestre. São dois mundos com modelagens diferentes. Hoje você vai dominar a modelagem dimensional, criada pelo Kimball, que é o padrão de data warehouse até hoje."

### 2. Desenvolvimento — parte 1 (0:40 – 4:00)

> "OLTP versus OLAP. OLTP opera: escrita rápida, registro a registro, banco normalizado. OLAP analisa: leitura agregada sobre milhões de linhas, banco dimensional. Você não roda relatório pesado no banco de produção — copia o dado para um data warehouse. E aí a normalização dá lugar à desnormalização: aceitamos redundância para ganhar velocidade de leitura."

### 3. Desenvolvimento — parte 2 (4:00 – 7:00)

> "A modelagem dimensional tem dois tipos de tabela: fatos, com as métricas numéricas e as chaves, longas e estreitas; e dimensões, com o contexto descritivo — quem, o quê, quando, onde —, curtas e largas. Ligadas, formam o esquema estrela. Existe também o floco de neve, com dimensões normalizadas, mas a estrela vence pela simplicidade."

### 4. Desenvolvimento — parte 3 (7:00 – 9:00)

> "E quando um atributo muda? O cliente muda de cidade. Entram as Slowly Changing Dimensions. O Tipo 1 sobrescreve e perde a história; o Tipo 2 cria uma nova linha com validade e preserva tudo. O Tipo 2 é o mais importante. E o exemplo: uma rede de 500 lojas gera 1,46 bilhão de linhas de fato por ano, cerca de 117 gigabytes — por isso usamos colunar e OLAP distribuído."

### 5. Encerramento (9:00 – 11:00)

> "Com isso, você fecha os fundamentos: papel, tipos, bancos e modelagem. Na próxima unidade, a gente coloca o dado em movimento — ingestão e processamento, batch e streaming, com Kafka e Spark. É quando a teoria vira tubulação rodando. Te espero na Unidade 2!"

---

## Quiz não avaliativo

### Questão 1

Sobre a diferença entre os padrões **ETL** e **ELT** em pipelines de dados, assinale a alternativa **correta**:

- [ ] a. ETL e ELT são exatamente o mesmo processo, apenas com nomes comerciais diferentes adotados por fornecedores distintos.
- [x] b. No ETL, o dado é transformado **antes** de ser carregado no destino; no ELT, o dado bruto é carregado primeiro e transformado **depois**, dentro do próprio destino — padrão favorecido pelo baixo custo de armazenamento na nuvem.
- [ ] c. No ELT, o dado nunca é transformado, sendo sempre consumido em estado bruto pelos analistas.
- [ ] d. O ETL só funciona com dados não estruturados, enquanto o ELT só funciona com dados estruturados.

**Resposta correta:** `b`

**Feedback:** A alternativa (b) descreve corretamente a diferença essencial: a **ordem do "T" (transformação)**. No ELT, guarda-se o dado bruto primeiro (flexibilidade para reprocessar) e transforma-se sob demanda dentro do destino — viável porque armazenamento na nuvem ficou barato e os warehouses, poderosos. A (a) ignora a diferença real de ordem. A (c) é falsa: o ELT transforma, só que depois de carregar. A (d) inventa uma relação com tipos de dado que não existe.

### Questão 2

Considere o **teorema CAP** aplicado a bancos de dados distribuídos. Assinale a alternativa **correta**:

- [ ] a. O teorema CAP afirma que um banco distribuído sempre garante simultaneamente Consistência, Disponibilidade e Tolerância a partição.
- [ ] b. Como partições de rede quase nunca acontecem na prática, a escolha entre Consistência e Disponibilidade é puramente teórica e irrelevante.
- [x] c. Na presença de uma partição de rede (inevitável em sistemas distribuídos), o sistema precisa escolher entre **Consistência (CP)** e **Disponibilidade (AP)** — não é possível maximizar as duas ao mesmo tempo durante a partição.
- [ ] d. O teorema CAP só se aplica a bancos relacionais, sendo irrelevante para qualquer banco NoSQL.

**Resposta correta:** `c`

**Feedback:** A alternativa (c) descreve corretamente o teorema: como a tolerância a partição (P) é obrigatória em sistemas distribuídos (a rede falha), a escolha real é entre priorizar **Consistência (CP)** ou **Disponibilidade (AP)** durante a falha. A (a) contradiz o próprio teorema — não dá para ter as três plenamente sob partição. A (b) é falsa: partições de rede são inevitáveis em escala. A (d) inverte a aplicação: o CAP é justamente central para entender NoSQL distribuído.

---

## Atividade Verificadora (AAI — Atividade Avaliativa Individual)

**Pergunta:**

> Uma startup de **delivery de comida** está crescendo rápido. Hoje, todo o sistema roda sobre um único banco **PostgreSQL** (transacional), que registra pedidos, pagamentos e entregas. O time de produto começou a pedir relatórios pesados — "faturamento por bairro no último trimestre", "produtos mais pedidos por horário" — e percebeu que essas consultas estão **deixando o app lento** para os clientes, porque competem com a operação no mesmo banco. Além disso, o time quer começar a coletar o **stream de cliques** do app (milhões de eventos por dia) para entender o comportamento dos usuários.
>
> Você foi contratado(a) como engenheiro(a) de dados. Estruture sua resposta em três partes:
>
> 1. **Diagnóstico** — explique tecnicamente **por que** rodar relatórios analíticos no banco transacional de produção é uma má ideia, usando os conceitos de **OLTP vs OLAP**.
> 2. **Arquitetura proposta** — descreva um pipeline que separe a operação da análise. Diga **de onde** o dado sai, **como** ele se move (ETL ou ELT? batch ou stream?), **onde** ele é armazenado para análise, e que **formato de arquivo** e **modelagem** você usaria no destino analítico.
> 3. **Escolha de tecnologia** — para o **stream de cliques**, que **tipo de banco/tecnologia** você recomendaria e por quê, justificando com base no **padrão de acesso** (escrita massiva) e no **teorema CAP**.

**Resposta esperada:**

> Uma resposta exemplar começa pelo **diagnóstico OLTP vs OLAP**: o PostgreSQL de produção é um banco **OLTP**, otimizado para escritas e leituras pequenas e rápidas (registrar um pedido), e está **normalizado**. Consultas analíticas precisam **agregar milhões de linhas** (`GROUP BY`, somas), o que é uma carga **OLAP** — pesada, demorada e que disputa CPU, memória e I/O com a operação, deixando o app lento. A solução é **separar os dois mundos**: copiar o dado do OLTP para um ambiente OLAP dedicado, sem afetar a produção. Na **arquitetura**, espera-se um pipeline em que o dado **sai do PostgreSQL** (via snapshot ou, melhor, **CDC — Change Data Capture**, para capturar só as mudanças quase em tempo real), é **carregado** em um **data warehouse / data lake** (BigQuery, Snowflake, Redshift ou um lake com object storage) — preferencialmente no padrão **ELT** (carrega o bruto e transforma no destino), em **formato colunar Parquet** para análise eficiente, modelado de forma **dimensional (esquema estrela, com fatos e dimensões)**. A consulta "faturamento por bairro no trimestre" passa a rodar sobre fatos e dimensões, sem tocar a produção. Para o **stream de cliques**, a resposta deve reconhecer o **padrão de escrita massiva e contínua** (milhões de eventos/dia): recomenda-se **ingestão por streaming** (ex.: **Apache Kafka**) e armazenamento em um banco otimizado para escrita, como um **NoSQL colunar (Cassandra)** ou direto no data lake. Pelo **teorema CAP**, para cliques a **disponibilidade (AP)** importa mais que a consistência imediata — perder consistência por instantes em uma contagem de cliques é aceitável; ficar fora do ar não é —, então **consistência eventual** é uma troca razoável. A resposta de qualidade conecta cada decisão a um conceito da unidade (OLTP/OLAP, ETL/ELT, CDC, Parquet, modelagem dimensional, CAP) e evita "jogar tecnologia" sem justificar pelo padrão de acesso.

---

## Material complementar

### Direto da fonte — livro da Biblioteca Virtual

> Esta é, hoje, a obra de referência para entrar em engenharia de dados começando do conceito e chegando à prática. O capítulo de abertura define a disciplina e apresenta o **ciclo de vida da engenharia de dados** com suas correntes transversais — exatamente a espinha dorsal da nossa Unidade 1. Leitura **essencial** para fixar o vocabulário e ganhar autoridade no tema antes de partir para ferramentas.

- **Nome do livro:** *Fundamentals of Data Engineering*
- **Capítulo:** Capítulo 1 — *Data Engineering Described* e Capítulo 2 — *The Data Engineering Lifecycle*
- **Organizador:** Joe Reis e Matt Housley
- **Editora:** O'Reilly Media
- **Link de acesso (BV):** https://learning.oreilly.com/library/view/fundamentals-of-data/9781098108298/
- **Aula em que entra:** Aulas 1 a 4

### Para mergulhar no assunto

> Recomendo o livro **"Designing Data-Intensive Applications"**, de Martin Kleppmann (O'Reilly) — frequentemente apelidado de "o livro do javali" pela capa. É a obra que aprofunda **tudo** o que vimos sobre bancos, ACID, replicação e o teorema CAP, com o rigor de um engenheiro que trabalhou em sistemas de escala real. Para quem quer ir além do introdutório e entender o "porquê" de cada decisão de arquitetura, é leitura obrigatória de carreira.

- **Link(s):** https://dataintensive.net/ (site oficial do livro, com material e diagramas)
- **Aula em que entra:** Aula 3 (bancos, ACID e CAP)

### Podcast (curadoria, até 45 min)

> O canal **Data Engineering Podcast** no YouTube traz entrevistas com engenheiros de dados de empresas reais, discutindo ferramentas, arquiteturas e decisões de mercado em linguagem acessível. Ótimo para ouvir o vocabulário da unidade aplicado por quem está no campo todos os dias.

- **Nome do podcast/canal:** Data Engineering Podcast — canal no YouTube
- **Tema recomendado:** Fundamentos e ciclo de vida da engenharia de dados
- **Link:** https://www.youtube.com/@dataengineeringpodcast
- **Aula em que entra:** Aula 1

### Artigo científico

> Este é o artigo **fundador** de toda a teoria de bancos de dados relacionais. Publicado por Edgar F. Codd em 1970, ele propõe o modelo relacional — tabelas, relações, álgebra relacional — que é a base do SQL e de praticamente todos os bancos transacionais que usamos até hoje. Ler o original (ou seu resumo) dá perspectiva histórica e mostra que conceitos como os da Aula 3 nasceram de uma ideia teórica precisa.

- **Link:** https://doi.org/10.1145/362384.362685 (DOI)
- **Aula em que entra:** Aula 3
- **Referência bibliográfica do artigo no formato ABNT:**
  > CODD, Edgar Frank. **A relational model of data for large shared data banks**. *Communications of the ACM*, v. 13, n. 6, p. 377-387, 1970.
