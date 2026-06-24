# Unidade 1 — Fundamentos de Engenharia de Dados

- **Disciplina:** Data Engineering and Pipelines
- **Conteudista:** Afonso Cesar Lelis Brandão
- **Videoaulas desta unidade:** 1 a 4

## Vídeo introdutório + Relação da disciplina com a atuação profissional

Você já reparou que **toda aplicação moderna que você usa — Netflix, iFood, Nubank, Spotify — é, no fundo, uma máquina de mover dados**? Quando o Netflix te recomenda uma série, alguém precisou coletar seu histórico, mover esse dado de um servidor para outro, limpá-lo, juntá-lo com o de milhões de outros usuários e entregá-lo, em segundos, para o modelo que faz a recomendação. Esse "alguém" é o **engenheiro de dados** — e essa cadeia de coleta, transporte e transformação é o **pipeline de dados**. É exatamente isso que você vai aprender a construir nesta disciplina.

E não vamos aprender no abstrato. **Esta disciplina inteira é um projeto único, construído do zero:** um **pipeline de dados real sobre o dataset Olist** — pedidos verdadeiros de um marketplace brasileiro (cerca de 99 mil pedidos entre 2016 e 2018, distribuídos em 9 arquivos CSV). A cada aula você ENSINA um conceito E CONSTRÓI mais uma camada desse pipeline, usando uma **stack 100% local, gratuita e portável** que roda no seu próprio laptop: **Python** para ingestão, **DuckDB** como motor analítico, **dbt** para transformação SQL e **Apache Airflow** para orquestração. Ao final, você terá um pipeline de ponta a ponta para colocar no portfólio.

A engenharia de dados é hoje uma das carreiras mais bem pagas e mais demandadas da área de tecnologia. Enquanto o cientista de dados ganha as manchetes treinando modelos de IA, é o engenheiro de dados quem constrói a fundação invisível sobre a qual todo modelo, dashboard e relatório dependem. Sem dado limpo, organizado e disponível, não há ciência de dados, não há BI, não há IA. Por isso costuma-se dizer que **80% do esforço de qualquer projeto de dados é engenharia de dados** — e quem domina essa parte se torna indispensável. Uma mensagem vai se repetir nas 16 aulas: *o que roda local com DuckDB + dbt migra para a nuvem trocando o profile do dbt; os conceitos são os mesmos.*

### Roteiro do vídeo introdutório (até 2 min)

**Abertura (0:00 – 0:20):**
> "Olá! Eu sou o professor Afonso Brandão. Seja muito bem-vindo(a) à disciplina Data Engineering and Pipelines. Aqui a gente não estuda dado no abstrato: nós vamos construir, do zero, um pipeline de dados real sobre o dataset Olist — pedidos de um marketplace brasileiro de verdade."

**Conexão com o mercado (0:20 – 0:55):**
> "Engenharia de dados é uma das carreiras que mais cresce em tecnologia. Antes de qualquer cientista de dados treinar um modelo, alguém precisa coletar, mover e organizar o dado. Esse alguém é o engenheiro de dados — e o mercado paga muito bem por essa habilidade, porque sem ela nada funciona."

**Conteúdo e diferencial (0:55 – 1:25):**
> "A gente começa do zero com os 9 CSVs do Olist e vai subindo: ingestão para Parquet e DuckDB, modelagem em estrela com dbt, processamento batch e streaming, orquestração com Airflow, qualidade, governança e LGPD, e fecha com um modelo de machine learning. Tudo local, grátis, no seu laptop — e tudo migrável para a nuvem."

**Benefício para o aluno (1:25 – 1:45):**
> "Ao final, você não só entende os conceitos: você tem um **pipeline Olist completo no GitHub** — ingestão, dbt, Airflow, testes e dashboard. Diferencial real, palpável, para quem está entrando no mercado de dados."

**Encerramento (1:45 – 2:00):**
> "Bora! Engenharia de dados é a fundação invisível de tudo que é digital. Na Aula 1 a gente apresenta o projeto Olist e desenha a arquitetura-alvo. Te espero lá!"

---

## Aula 1 — O que é Engenharia de Dados? Papel, ciclo de vida e diferença para a Ciência de Dados

Imagine que você quer cozinhar um prato sofisticado. O chef (cientista de dados) só consegue brilhar se alguém comprou os ingredientes, lavou, cortou e deixou tudo organizado na bancada. Esse trabalho de bastidor — comprar, transportar, limpar e organizar — é a **engenharia de dados**. Nesta aula você vai entender o que é essa disciplina e, mais importante, vamos **apresentar o projeto que nos acompanhará o curso inteiro**: construir, do zero, o pipeline de dados do **Olist**. Você verá o ciclo de vida do dado mapeado sobre esse marketplace real, a arquitetura-alvo e o primeiro passo concreto — montar o repositório.

### O profissional de dados e suas fronteiras

A **engenharia de dados** é a disciplina que projeta, constrói e mantém os sistemas que **coletam, armazenam, transportam e transformam dados** em escala, de forma confiável, deixando-os prontos para consumo. O produto final do engenheiro de dados não é um modelo nem um gráfico — é o **dado disponível, íntegro e organizado** que outras pessoas vão consumir.

O engenheiro de dados opera na fronteira entre dois mundos: de um lado, os **sistemas-fonte** (aplicações, bancos transacionais, APIs, sensores) que produzem dados; do outro, os **consumidores** (cientistas de dados, analistas, dashboards, modelos de machine learning). No nosso projeto, o sistema-fonte é o **marketplace Olist** — quando um cliente compra, o app gera registros de pedido, item, pagamento e avaliação; esses registros chegam até nós como os **9 CSVs** que vamos transformar em um pipeline.

![Computação em nuvem — base da infraestrutura moderna de engenharia de dados](https://commons.wikimedia.org/wiki/Special:FilePath/Cloud_computing.svg)

### O ciclo de vida da engenharia de dados (sobre o Olist)

O livro *Fundamentals of Data Engineering* (Reis & Housley, O'Reilly) popularizou um modelo de **ciclo de vida** que organiza tudo que o engenheiro de dados faz. Veja-o já mapeado sobre o nosso projeto:

| Etapa | No ciclo de vida | No projeto Olist |
| --- | --- | --- |
| **Geração** | O dado nasce nos sistemas-fonte | Compras no marketplace → 9 CSVs (Kaggle) |
| **Ingestão** | O dado é coletado e movido | Python/DuckDB lê os CSVs → camada bronze (Parquet) e schema `raw` |
| **Transformação** | O dado é limpo, validado, agregado | dbt: staging → estrela (`fct_order_items`, `dim_*`) |
| **Armazenamento** | O dado é persistido | `olist.duckdb` + Parquet (bronze/silver/gold) |
| **Disponibilização** | O dado é servido | Marts para BI (Metabase) e modelo de ML |

Atravessando todas essas etapas estão as **correntes transversais** (undercurrents): **segurança**, **governança e qualidade de dados**, **gestão de metadados**, **orquestração** e **engenharia de software**. Elas não são uma "etapa" — são preocupações de **todas** as etapas. No nosso pipeline, a orquestração será o **Airflow**, a qualidade virá de **dbt tests + Great Expectations**, e a governança aparecerá quando discutirmos a **LGPD** (o Olist já vem anonimizado).

### A arquitetura-alvo do pipeline Olist

É para cá que estamos indo nas próximas 16 aulas. Guarde este desenho:

> **9 CSVs (Olist)** → **Python/DuckDB** (ingestão) → **DuckDB schema `raw`** + **Parquet bronze** → **dbt** (staging → core estrela → marts) → **gold (Parquet)** → **BI (Metabase) / ML (scikit-learn)** — tudo **orquestrado pelo Airflow**.

O layout do repositório que vamos preencher gradualmente:

```
pipeline-olist/
├── data/raw/                # 9 CSVs do Olist           [Aula 1-2]
│   └── bronze/ silver/ gold/  # Parquet (Medallion)     [Aula 2,10]
├── ingestion/load_raw.py    # CSV -> DuckDB schema raw   [Aula 2-3]
├── olist.duckdb             # banco DuckDB local
├── dbt_olist/               # projeto dbt (adapter duckdb)[Aula 5,9]
├── airflow/dags/olist_pipeline.py                       [Aula 8]
└── ml/train_delivery_delay.py                           [Aula 16]
```

### O setup do projeto (mãos à obra)

Antes de qualquer aula prática, prepare o ambiente local. Crie um ambiente virtual isolado e instale a stack:

```python
# 1) ambiente virtual e instalação da stack
# python -m venv .venv && source .venv/bin/activate   (Linux/Mac)
# python -m venv .venv && .venv\Scripts\activate       (Windows)
# pip install duckdb dbt-duckdb apache-airflow great-expectations

import duckdb

con = duckdb.connect("olist.duckdb")          # cria/abre o banco local
print(con.sql("SELECT 'pipeline Olist no ar!' AS status"))
con.close()
```

Depois, baixe o **Brazilian E-Commerce Public Dataset by Olist** do Kaggle (link nos materiais) e descompacte os 9 CSVs em `data/raw/`. Pronto: o sistema-fonte está na sua máquina.

### Engenheiro de dados vs cientista vs analista

A confusão entre esses três papéis é o erro mais comum de quem entra na área. No nosso projeto Olist fica claro quem faz o quê:

| Aspecto | Engenheiro de dados | Cientista de dados | Analista de dados |
| --- | --- | --- | --- |
| **Foco** | Mover e preparar o dado | Criar modelos preditivos | Explicar o que aconteceu |
| **Entrega Olist** | `fct_order_items` confiável | Prever atraso de entrega | Dashboard de vendas |
| **Pergunta** | "Como levo o CSV até a estrela?" | "Esse pedido vai atrasar?" | "Quanto vendemos por UF?" |
| **Ferramentas** | DuckDB, dbt, Airflow, SQL, Python | scikit-learn, ML | SQL, Metabase, Power BI |

A relação é de dependência: o **engenheiro de dados é a base**. Sem a estrela do Olist limpa e disponível, ninguém prevê atraso nem desenha dashboard. Há um ditado: "garbage in, garbage out" — se o dado que entra é lixo, o modelo também será. Garantir que não seja lixo é, em grande parte, trabalho de engenharia.

### ETL vs ELT e o conceito de pipeline

Um **pipeline de dados** é uma sequência automatizada de passos que move o dado da origem ao destino, aplicando transformações no caminho. Dois padrões clássicos:

- **ETL (Extract, Transform, Load)** — transforma **antes** de carregar. Comum quando o destino é caro/limitado.
- **ELT (Extract, Load, Transform)** — carrega o dado bruto e transforma **depois**, dentro do destino. Padrão moderno, viável porque armazenamento ficou barato e os motores (como o DuckDB) ficaram poderosos.

Nosso pipeline Olist é **ELT**: vamos carregar os 9 CSVs crus primeiro (camada bronze e schema `raw`) e só então transformar com dbt. Guardar o cru dá flexibilidade total para reprocessar.

### Exemplo numérico: dimensionar o Olist justifica o ELT

O dataset Olist tem **9 tabelas, cerca de 99 mil pedidos e 112 mil itens, ocupando aproximadamente 120 MB em CSV**. Guardar esse volume bruto num armazenamento de objetos na nuvem custa quase nada. A um preço típico de $0{,}023$ dólar por GB ao mês, e como $120\,\text{MB} \approx 0{,}117\,\text{GB}$:

$$
0{,}117\,\text{GB} \times 0{,}023\,\text{US\$/GB} \approx 0{,}0027\,\text{US\$/mês}
$$

Menos de **um centavo de dólar por mês** para guardar o Olist inteiro cru. E no nosso laptop, com DuckDB e Parquet, o custo é literalmente **zero**. É justamente esse custo irrisório de armazenar o dado bruto que torna o padrão **ELT** economicamente óbvio: carregue tudo, transforme depois.

### Atividade prática

Monte o esqueleto do projeto na sua máquina:

1. Crie a pasta `pipeline-olist/` com a estrutura `data/raw/`, `ingestion/`, `dbt_olist/`.
2. Crie e ative o ambiente virtual e rode `pip install duckdb dbt-duckdb apache-airflow great-expectations`.
3. Baixe o dataset Olist do Kaggle e descompacte os **9 CSVs** em `data/raw/`. Liste-os e confira os nomes (`olist_orders_dataset.csv`, `olist_order_items_dataset.csv`, ...).
4. Rode o `python` mínimo que abre `olist.duckdb` e imprime "pipeline Olist no ar!". Em uma frase, **mapeie cada etapa do ciclo de vida** sobre o Olist.

### Pontos-chave

- **Engenharia de dados** projeta e mantém os sistemas que coletam, movem, transformam e disponibilizam dados; o produto é o **dado confiável**, não o modelo.
- O **ciclo de vida** (geração → ingestão → transformação → armazenamento → disponibilização) mapeia perfeitamente o projeto Olist: do CSV no Kaggle ao dashboard/ML.
- A **arquitetura-alvo** é CSVs → Python/DuckDB → schema `raw`/Parquet → dbt (estrela) → BI/ML, orquestrada por **Airflow** — tudo local e portável.
- O **engenheiro de dados é a base**: sem a estrela do Olist limpa, não há ciência de dados nem análise.
- Guardar o Olist cru custa **frações de centavo** (zero no laptop) — é o que justifica adotar **ELT** no nosso pipeline.

### Para saber mais

- **Brazilian E-Commerce Public Dataset by Olist (Kaggle):** https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce
- **DuckDB — documentação oficial (Python API):** https://duckdb.org/docs/api/python/overview
- **Why DuckDB? (visão geral do motor analítico):** https://duckdb.org/why_duckdb
- **Engenharia de dados (Wikipedia, em inglês):** https://en.wikipedia.org/wiki/Data_engineering

## Aula 1 — Roteiro da Videoaula 1: "O que é Engenharia de Dados? Papel, ciclo de vida e diferença para a Ciência de Dados"

### 1. Abertura (0:00 – 0:45)

> "Bem-vindo à Aula 1! E mais do que uma aula, este é o pontapé de um projeto que vai durar a disciplina inteira: a gente vai construir, do zero, um pipeline de dados real sobre o dataset Olist — pedidos de um marketplace brasileiro de verdade, 99 mil deles. Hoje a gente entende o papel do engenheiro de dados e desenha a arquitetura-alvo desse pipeline."

### 2. Desenvolvimento — parte 1 (0:45 – 4:00)

> "Engenharia de dados constrói a tubulação dos dados — da origem ao consumo. O produto não é gráfico nem modelo; é o dado disponível e íntegro. Olha o ciclo de vida mapeado no Olist: geração, que é a compra no marketplace virando 9 CSVs; ingestão, que é o Python e o DuckDB lendo esses CSVs; transformação com dbt; armazenamento em DuckDB e Parquet; e disponibilização para BI e machine learning. Atravessando tudo, as correntes transversais: segurança, governança, metadados, orquestração e engenharia de software."

### 3. Desenvolvimento — parte 2 (4:00 – 6:45)

> "Essa é a arquitetura-alvo: 9 CSVs, Python e DuckDB para ingerir, schema raw e Parquet bronze, dbt transformando em estrela, e no fim BI e ML, tudo orquestrado pelo Airflow. E olha a confusão clássica: o engenheiro move e prepara o dado; o cientista cria modelos — no Olist, prever se um pedido vai atrasar; o analista explica o que aconteceu — quanto vendemos por UF. O engenheiro é a base. Garbage in, garbage out."

### 4. Desenvolvimento — parte 3 (6:45 – 9:00)

> "Vamos ao setup, mão na massa: cria o ambiente virtual, instala duckdb, dbt-duckdb, apache-airflow e great-expectations, baixa o Olist do Kaggle e descompacta os 9 CSVs em data barra raw. Quatro linhas de Python já abrem o olist.duckdb. E por que ELT e não ETL? Porque guardar o Olist inteiro cru custa frações de centavo por mês — zero no seu laptop. Armazenamento barato é o que torna o ELT a escolha óbvia: carrega tudo cru, transforma depois."

### 5. Encerramento (9:00 – 9:50)

> "Você já entende o papel, o ciclo de vida e tem o repositório do projeto montado. Na próxima aula, a gente classifica os 9 CSVs do Olist por tipo e formato e faz a primeira ingestão de verdade: converter CSV para Parquet com DuckDB e medir a compressão real. A bronze nasce na Aula 2. Te espero!"

---

## Aula 2 — Tipos, formatos e fontes de dados

Na Aula 1 apresentamos o projeto Olist, desenhamos a arquitetura-alvo e montamos o repositório. Agora vamos olhar a **matéria-prima** que acabamos de baixar: os 9 CSVs. Dado não é tudo igual — tem dado arrumadinho em tabela e tem texto livre, como os comentários das avaliações. Escolher o formato certo pode ser a diferença entre um pipeline que custa centavos e um que custa milhares. Nesta aula você constrói esse vocabulário **e faz a primeira ingestão real**: converte um CSV do Olist em Parquet (a camada bronze) e mede a compressão.

### Dados estruturados, semi-estruturados e não estruturados

A primeira grande classificação do dado é pelo **grau de estrutura**:

| Tipo | Definição | Exemplos | No Olist |
| --- | --- | --- | --- |
| **Estruturado** | Tabela com colunas e tipos | Tabela de pedidos, planilha | `orders`, `order_items`, `payments`, `geolocation` |
| **Semi-estruturado** | Estrutura flexível e aninhada | JSON, XML, logs | (surge quando emitimos eventos na Aula 7) |
| **Não estruturado** | Sem esquema fixo | Texto livre, imagem, áudio | `review_comment_message` (comentário do cliente) |

Estima-se que **cerca de 80% dos dados do mundo sejam não estruturados**. No Olist, a esmagadora maioria é estruturada (são tabelas), mas há uma ilha não estruturada importante: o campo `review_comment_message`, o texto livre que o cliente escreve ao avaliar o pedido. Saber distinguir isso já indica que esse campo pediria outra abordagem (NLP) que as colunas numéricas não pedem.

### Formatos de arquivo: CSV, JSON, Parquet, Avro

Dentro do dado estruturado e semiestruturado, o **formato de arquivo** importa muito:

- **CSV** — texto puro separado por vírgula. Simples, universal, legível. Mas **sem tipos** (tudo é texto), sem compressão nativa e ineficiente em escala. **É como o Olist vem do Kaggle.**
- **JSON** — texto hierárquico (chave-valor), ótimo para APIs. Flexível, mas **verboso**. Usaremos JSON na Aula 7 para simular o stream de pedidos.
- **Parquet** — formato **colunar e comprimido**, binário. Padrão de analytics. **É para onde vamos converter o Olist** (camada bronze).
- **Avro** — formato **por linha (row-based)** binário, com esquema embutido. Excelente para **ingestão e streaming**.

A regra prática: **CSV/JSON para troca e ingestão; Parquet para analytics; Avro para streaming**. Nosso pipeline segue exatamente isso — entra CSV, vira Parquet.

![Comparação esquemática entre armazenamento orientado a linhas e armazenamento orientado a colunas em bancos de dados](https://commons.wikimedia.org/wiki/Special:FilePath/Row_and_column_major_order.svg)

### Classificando os 9 CSVs do Olist

Vamos catalogar a fonte. Cada CSV é estruturado, mas com papéis diferentes no modelo:

- **Fatos/eventos:** `olist_orders_dataset` (~99k pedidos), `olist_order_items_dataset` (~112k itens), `olist_order_payments_dataset` (~104k pagamentos), `olist_order_reviews_dataset` (~99k avaliações — com o texto livre).
- **Entidades/dimensões:** `olist_products_dataset` (~33k produtos), `olist_customers_dataset` (~99k linhas), `olist_sellers_dataset` (~3k vendedores).
- **Apoio:** `olist_geolocation_dataset` (~1 milhão de linhas de CEP) e `product_category_name_translation` (~71 categorias traduzidas).

### Schema-on-read vs schema-on-write

- **Schema-on-write** — você define o esquema **antes** de gravar; o banco rejeita dado fora do formato. Garante qualidade na entrada, mas é rígido (banco relacional clássico).
- **Schema-on-read** — você grava o dado bruto **sem** esquema e o interpreta só na leitura. Flexível, ideal para data lakes.

O DuckDB lendo os CSVs do Olist é um caso de **schema-on-read**: ao usar `read_csv_auto`, ele **infere os tipos no momento da leitura**, sem exigir que tenhamos declarado o esquema antes. É flexível e perfeito para uma camada bronze.

### A primeira ingestão: CSV → Parquet (camada bronze)

Hora de construir. Com o DuckDB, converter um CSV do Olist para Parquet é **uma linha de SQL**:

```sql
-- ingestão bronze: CSV cru do Olist -> Parquet colunar comprimido
COPY (
    SELECT * FROM read_csv_auto('data/raw/olist_order_items_dataset.csv')
) TO 'data/bronze/order_items.parquet' (FORMAT PARQUET);
```

Em Python, dá para varrer todos os 9 CSVs de uma vez:

```python
import duckdb, glob, os

con = duckdb.connect("olist.duckdb")
os.makedirs("data/bronze", exist_ok=True)
# varre TODOS os CSVs da pasta: 8 no padrão olist_*_dataset.csv
# + o product_category_name_translation.csv (sem prefixo/sufixo) = 9
for csv in glob.glob("data/raw/*.csv"):
    nome = (os.path.basename(csv)
            .replace("olist_", "")
            .replace("_dataset", "")
            .replace(".csv", ""))
    con.sql(f"COPY (SELECT * FROM read_csv_auto('{csv}')) "
            f"TO 'data/bronze/{nome}.parquet' (FORMAT PARQUET)")
con.close()
```

Acabamos de criar a **camada bronze** do nosso lakehouse local.

### Exemplo numérico: a compressão real do Olist

Pegue a tabela de itens. O `olist_order_items_dataset.csv` ocupa cerca de $15\,\text{MB}$ em CSV. Após a conversão, o Parquet correspondente fica em torno de $4\,\text{MB}$. O **fator de compressão** é:

$$
\text{fator} = \frac{15\,\text{MB}}{4\,\text{MB}} \approx 3{,}75\times
$$

Mais do que o tamanho: o ganho colunar aparece na **leitura seletiva**. A tabela de itens tem 7 colunas; uma consulta de faturamento usa só `price` e `freight_value` (2 colunas). A fração de colunas lidas é:

$$
\frac{2}{7} \approx 0{,}29
$$

Combinando compressão e leitura colunar, a consulta toca apenas:

$$
4\,\text{MB} \times 0{,}29 \approx 1{,}1\,\text{MB}
$$

Ou seja: em vez de varrer os $15\,\text{MB}$ do CSV, a consulta lê cerca de $1{,}1\,\text{MB}$ — uma redução de aproximadamente **13 vezes** no volume lido. Multiplique isso pelas 9 tabelas e por consultas diárias e você entende por que **toda camada analítica do nosso pipeline será Parquet**.

### Atividade prática

Construa e meça a sua camada bronze:

1. Rode o script Python que converte os **9 CSVs** do Olist em Parquet na pasta `data/bronze/`.
2. Compare, no explorador de arquivos, o **tamanho de cada CSV** com o do Parquet correspondente. Monte uma tabelinha CSV × Parquet × fator.
3. Classifique cada um dos 9 CSVs como **estruturado, semi-estruturado ou não estruturado** (lembre do `review_comment_message`).
4. No DuckDB, rode `DESCRIBE SELECT * FROM read_csv_auto('data/raw/olist_orders_dataset.csv')` e observe os tipos **inferidos** — esse é o schema-on-read em ação.

### Pontos-chave

- Dados se classificam em **estruturados, semi-estruturados e não estruturados**; no Olist, quase tudo é estruturado, mas `review_comment_message` é texto não estruturado.
- Os quatro formatos essenciais: **CSV** (como o Olist vem), **JSON** (stream da Aula 7), **Parquet** (nossa camada bronze) e **Avro** (streaming).
- O DuckDB lê os CSVs do Olist em **schema-on-read**, inferindo os tipos na leitura — flexível e ideal para a bronze.
- A primeira ingestão do pipeline é **CSV → Parquet** com um `COPY ... TO ... (FORMAT PARQUET)` no DuckDB.
- No Olist, a compressão colunar reduz a tabela de itens de ~15 MB para ~4 MB, e a leitura seletiva derruba o volume lido em cerca de **13×**.

### Para saber mais

- **Apache Parquet — documentação oficial:** https://parquet.apache.org/docs/
- **DuckDB — importação e leitura de CSV:** https://duckdb.org/docs/data/csv/overview
- **DuckDB — leitura e escrita de Parquet:** https://duckdb.org/docs/data/parquet/overview
- **Apache Avro — documentação oficial:** https://avro.apache.org/docs/

## Aula 2 — Roteiro da Videoaula 2: "Tipos, formatos e fontes de dados"

### 1. Abertura (0:00 – 0:45)

> "Na Aula 1 a gente montou o repositório e baixou os 9 CSVs do Olist. Hoje a gente olha de perto essa matéria-prima: que tipo de dado é cada CSV, que formato escolher — e faz a primeira ingestão de verdade, convertendo CSV em Parquet e medindo a compressão. A camada bronze nasce nesta aula."

### 2. Desenvolvimento — parte 1 (0:45 – 3:45)

> "Primeira classificação: estruturado, semiestruturado e não estruturado. No Olist, quase tudo é estruturado — orders, items, payments são tabelas. Mas tem uma ilha não estruturada: o review_comment_message, o texto que o cliente escreve. Esse campo pediria NLP; as colunas numéricas não. Cerca de 80% do dado do mundo é não estruturado, então saber distinguir isso é essencial."

### 3. Desenvolvimento — parte 2 (3:45 – 6:45)

> "Os formatos: CSV é simples mas sem tipos, é como o Olist vem; JSON é flexível mas verboso, vamos usar no stream da Aula 7; Parquet é colunar e comprimido, é para onde vamos converter agora; Avro é por linha, ótimo para streaming. E quando o DuckDB lê o CSV com read_csv_auto, ele infere os tipos na hora — isso é schema-on-read, perfeito para uma camada bronze flexível."

### 4. Desenvolvimento — parte 3 (6:45 – 9:10)

> "Mão na massa: um COPY com FORMAT PARQUET converte cada CSV do Olist em bronze. Com um loop em Python, varremos os 9 de uma vez. E o resultado em números: a tabela de itens cai de 15 megabytes em CSV para uns 4 em Parquet — quase quatro vezes menor. E como uma consulta de faturamento usa só duas das sete colunas, ela acaba lendo cerca de 1 megabyte em vez de 15. Treze vezes menos. Por isso toda camada analítica do pipeline será Parquet."

### 5. Encerramento (9:10 – 9:55)

> "A bronze do Olist está construída e medida. Na próxima aula, a gente entra nos bancos de dados de verdade: o modelo relacional do Olist, com diagrama ER e chaves, carregar tudo no schema raw do DuckDB e rodar joins reais — além de ACID, NoSQL e o teorema CAP. Te espero!"

---

## Aula 3 — Bancos de dados para engenharia: relacional vs NoSQL

Na Aula 2 transformamos os CSVs do Olist em Parquet (bronze) e medimos a compressão. Mas para **consultar e juntar** essas tabelas — descobrir qual produto vendeu mais, qual vendedor entregou mais rápido — precisamos de um **banco de dados**. Por décadas, "banco de dados" significava "banco relacional". A explosão da web trouxe casos que o modelo relacional não atendia bem, e nasceu o **NoSQL**. Nesta aula você entende os dois mundos, carrega o Olist no **schema `raw` do DuckDB**, roda **joins reais** entre as tabelas, e aprende ACID, as famílias NoSQL e o teorema CAP — sempre com exemplos do Olist.

### O modelo relacional e o SQL

O **modelo relacional**, proposto por Edgar F. Codd em 1970, organiza os dados em **tabelas (relações)** com linhas e colunas. Cada tabela representa uma entidade, cada linha é um registro, cada coluna um atributo. As tabelas se conectam por **chaves**: a **chave primária** identifica unicamente cada linha; a **chave estrangeira** referencia outra tabela.

A linguagem para manipular bancos relacionais é o **SQL** — provavelmente a habilidade mais duradoura e valiosa de toda a área de dados. O DuckDB, nosso motor, fala SQL padrão e se comporta como um banco relacional analítico. O modelo relacional brilha quando os dados têm estrutura bem definida e a **integridade** é crítica — e o Olist é fortemente relacional.

![Diagrama de um banco de dados relacional mostrando chaves primárias e estrangeiras ligando tabelas](https://commons.wikimedia.org/wiki/Special:FilePath/Relational_key_SVG.svg)

### O modelo relacional do Olist (diagrama ER e chaves)

Veja como as 9 tabelas do Olist se conectam — este é o ER que vamos materializar:

- `orders` é o centro: **order_id** é a chave primária; **customer_id** é chave estrangeira para `customers`.
- `order_items` referencia `orders` (**order_id**), `products` (**product_id**) e `sellers` (**seller_id**).
- `order_payments` e `order_reviews` referenciam `orders` por **order_id**.
- `customers` e `sellers` ligam-se a `geolocation` por **zip_code_prefix**.
- `products` liga-se a `product_category_name_translation` por **product_category_name**.

Resumindo a espinha dorsal: `order_id` costura `orders ↔ order_items ↔ order_payments ↔ order_reviews`; `customer_id`, `product_id` e `seller_id` ligam os itens às entidades.

### Carregando o Olist no schema `raw` do DuckDB

Vamos do Parquet/CSV para tabelas SQL nomeadas. Criamos um schema `raw` e materializamos cada fonte:

```sql
CREATE SCHEMA IF NOT EXISTS raw;

CREATE TABLE raw.orders AS
    SELECT * FROM read_csv_auto('data/raw/olist_orders_dataset.csv');
CREATE TABLE raw.order_items AS
    SELECT * FROM read_csv_auto('data/raw/olist_order_items_dataset.csv');
CREATE TABLE raw.products AS
    SELECT * FROM read_csv_auto('data/raw/olist_products_dataset.csv');
```

Agora o Olist mora num banco relacional local. Hora do **join real** — faturamento por categoria de produto, juntando 3 tabelas:

```sql
SELECT p.product_category_name        AS categoria,
       COUNT(*)                       AS itens_vendidos,
       ROUND(SUM(i.price), 2)         AS faturamento
FROM raw.order_items i
JOIN raw.orders   o USING (order_id)
JOIN raw.products p USING (product_id)
GROUP BY p.product_category_name
ORDER BY faturamento DESC
LIMIT 10;
```

Esse join sobre ~112 mil itens roda em **frações de segundo** no DuckDB, no seu laptop. É o coração do que faremos com dbt mais à frente.

### Propriedades ACID

O que torna um banco relacional confiável para transações é o conjunto **ACID**:

| Letra | Propriedade | O que garante | No Olist |
| --- | --- | --- | --- |
| **A** | Atomicidade | Tudo ou nada | Pedido + pagamento gravam **juntos** ou nada |
| **C** | Consistência | Estado válido → estado válido | Item sempre aponta para um pedido existente |
| **I** | Isolamento | Transações simultâneas não interferem | Duas compras paralelas não se misturam |
| **D** | Durabilidade | Confirmado sobrevive a falhas | Pedido aprovado não some numa queda |

No sistema-fonte do Olist, registrar um **pedido com seu pagamento** é uma transação que precisa ser **atômica**: ou as duas coisas acontecem, ou nenhuma — não pode existir pedido pago sem registro de pagamento. É por isso que marketplaces rodam sobre bancos ACID na operação.

### As famílias NoSQL (onde caberiam no Olist)

**NoSQL** ("Not Only SQL") reúne bancos que abrem mão de parte da rigidez relacional por **escala, flexibilidade ou desempenho**. As quatro famílias, pensadas sobre o Olist:

- **Chave-valor** (Redis, DynamoDB) — pares `chave → valor`, extremamente rápido. No Olist: guardar o **carrinho de compras** ativo do cliente antes de virar pedido.
- **Documento** (MongoDB) — documentos JSON flexíveis. No Olist: armazenar as **avaliações** (`review`), que têm campos opcionais e texto livre, casaria bem com um documento.
- **Coluna larga** (Cassandra) — otimizado para **escrita massiva**. No Olist: ingerir o **stream de cliques/eventos** do marketplace.
- **Grafo** (Neo4j) — entidades e **relações**. No Olist: mapear a rede "cliente → comprou de → vendedor" para recomendação.

Não existe "NoSQL melhor que SQL". Numa arquitetura real, **convivem**: o relacional para os pedidos, o documento para reviews, o colunar para eventos, o grafo para recomendação.

### Teorema CAP e consistência

Quando um banco é **distribuído**, surge o dilema do **teorema CAP**: na presença de uma **partição de rede** (P, falha de comunicação entre nós), garante-se só **uma** entre:

- **C — Consistência:** toda leitura retorna o dado mais recente.
- **A — Disponibilidade:** toda requisição recebe resposta.
- **P — Tolerância a partição:** o sistema segue operando apesar da falha de rede.

Como partições são **inevitáveis** em sistemas distribuídos, o P é obrigatório. A escolha real é entre **CP** (consistência, sacrificando disponibilidade na partição) e **AP** (disponibilidade, aceitando inconsistência temporária). Pense no Olist numa **Black Friday do marketplace**: o registro de **pagamento** exige consistência (CP — não pode cobrar errado), enquanto a **contagem de visualizações** de um produto pode tolerar consistência eventual (AP — se atrasar alguns segundos, ninguém se importa).

### Exemplo numérico: throughput de escrita num pico do marketplace

O Olist tem **~99 mil pedidos** ao longo de cerca de 2 anos, o que dá uma média de aproximadamente **135 pedidos/dia**. Mas picos não são a média. Suponha uma Black Friday em que o marketplace concentre, num minuto de pico, **5 000 pedidos/min**:

$$
\frac{5\,000\,\text{pedidos}}{60\,\text{s}} \approx 83\,\text{escritas/s}
$$

Um banco relacional com ACID completo numa única instância suporta confortavelmente essa carga (na faixa de $5\,000$ a $10\,000$ escritas/s), então o Olist **não** precisaria de NoSQL para os pedidos. Agora imagine capturar **cliques**: se cada um dos pedidos veio de ~50 visualizações, são cerca de $83 \times 50 \approx 4\,150$ eventos/s só nesse minuto — e aí um banco **colunar distribuído** (Cassandra), que escala horizontalmente, passa a fazer sentido. A lição: **o padrão de acesso decide**, não a moda.

### Pausa para reflexão (Desafio)

> No sistema-fonte do Olist, registrar um pedido e seu pagamento é uma transação **atômica** (ACID): ou ambos são gravados, ou nada — não pode existir pedido pago sem pagamento. Já a contagem de quantas pessoas **visualizaram** um produto pode ficar alguns segundos desatualizada sem problema algum. **Desafio:** escolha **três operações** do marketplace Olist (ex.: criar pedido, atualizar status de entrega, registrar avaliação, contar visualizações, atualizar estoque do vendedor) e classifique cada uma como **CP** (precisa de consistência forte) ou **AP** (tolera consistência eventual). Justifique pela natureza do negócio: o que é pior nessa operação — mostrar dado errado por um instante, ou ficar indisponível?

### Atividade prática

Coloque o Olist num banco relacional e explore as relações:

1. No DuckDB, crie o schema `raw` e carregue **pelo menos 4 tabelas** do Olist (`orders`, `order_items`, `products`, `customers`).
2. Rode o **join de faturamento por categoria** e identifique as **3 categorias** que mais faturam.
3. Faça um segundo join para descobrir o **número de pedidos por UF** (`orders` × `customers`, agrupando por `customer_state`). Confirme se SP concentra a maior fatia.
4. Para cada uma das **4 famílias NoSQL**, aponte um campo/uso do Olist onde ela caberia melhor que o relacional, e justifique em uma frase.

### Pontos-chave

- O **modelo relacional** (tabelas + chaves + SQL) é ideal para o Olist; no DuckDB, o schema `raw` materializa as 9 tabelas e permite **joins reais** em frações de segundo.
- No Olist, `order_id` costura `orders ↔ items ↔ payments ↔ reviews`; `customer_id`, `product_id` e `seller_id` ligam os itens às entidades.
- As propriedades **ACID** garantem que pedido + pagamento gravem de forma **atômica** no sistema-fonte do marketplace.
- As **4 famílias NoSQL** têm lugares naturais no Olist: carrinho (chave-valor), reviews (documento), eventos (colunar), recomendação (grafo).
- O **teorema CAP** aparece na Black Friday do Olist: pagamento é **CP**, contagem de visualizações é **AP** — o **padrão de acesso** decide.

### Para saber mais

- **Kleppmann, M.** *Designing Data-Intensive Applications*. O'Reilly, 2017 — capítulos 2, 5 e 9 (modelos, replicação e consistência).
- **DuckDB — importação de CSV (carga do schema `raw`):** https://duckdb.org/docs/guides/import/csv_import
- **Teorema CAP (Wikipedia):** https://pt.wikipedia.org/wiki/Teorema_CAP
- **MongoDB Manual (família documento):** https://www.mongodb.com/docs/manual/

## Aula 3 — Roteiro da Videoaula 3: "Bancos de dados para engenharia: relacional vs NoSQL"

### 1. Abertura (0:00 – 0:45)

> "Na Aula 2 a gente virou os CSVs do Olist em Parquet. Mas para juntar essas tabelas e descobrir qual produto vendeu mais, a gente precisa de banco de dados. Hoje a gente carrega o Olist no schema raw do DuckDB, roda joins de verdade entre as tabelas, e entende relacional contra NoSQL, ACID e o teorema CAP — tudo com exemplos do próprio Olist."

### 2. Desenvolvimento — parte 1 (0:45 – 3:45)

> "O modelo relacional, do Codd em 1970, organiza tudo em tabelas ligadas por chaves, e a gente fala com ele em SQL. No Olist, o order_id é a espinha dorsal: ele costura orders, items, payments e reviews; e customer_id, product_id e seller_id ligam os itens às entidades. A gente cria um schema raw no DuckDB, carrega as tabelas com read_csv_auto, e roda um join de faturamento por categoria sobre 112 mil itens — que executa em frações de segundo no laptop."

### 3. Desenvolvimento — parte 2 (3:45 – 6:45)

> "O que torna isso confiável na origem é o ACID. No Olist, registrar pedido e pagamento é atômico: ou os dois entram, ou nenhum — não existe pedido pago sem pagamento. E o NoSQL? Quatro famílias, cada uma com um lugar no Olist: chave-valor para o carrinho, documento para os reviews com texto livre, coluna larga para os eventos de clique, e grafo para a recomendação cliente-vendedor. Não existe melhor; existe o certo para cada padrão de acesso."

### 4. Desenvolvimento — parte 3 (6:45 – 9:10)

> "O teorema CAP: com partição de rede, que é inevitável, você escolhe entre consistência e disponibilidade. Pensa na Black Friday do Olist: o pagamento é CP, precisa estar certo; a contagem de visualizações é AP, tolera atraso. E o número: 99 mil pedidos em dois anos dão 135 por dia na média, mas num pico de 5 mil por minuto são uns 83 pedidos por segundo — que um banco relacional aguenta. Já os cliques, milhares por segundo, é onde o Cassandra entra. O padrão de acesso decide."

### 5. Encerramento (9:10 – 9:55)

> "Agora o Olist mora num banco relacional e a gente já junta as tabelas. Na próxima aula, a gente sobe para a modelagem analítica: vamos desenhar o star schema do Olist — a fato de itens de pedido e as dimensões — e ver SCD Tipo 2 num vendedor que muda de cidade. É como o dado do Olist vira insight. Te espero!"

---

## Aula 4 — Modelagem de dados: OLTP, OLAP e modelagem dimensional

Na Aula 3 carregamos o Olist no schema `raw` do DuckDB e rodamos joins entre as 9 tabelas normalizadas. Mas rodar aquele join de 3 ou 4 tabelas toda vez que alguém faz uma pergunta é lento e repetitivo. Existe um jeito melhor de organizar o dado **para análise**: a **modelagem dimensional** de Ralph Kimball, padrão de data warehouse até hoje. Nesta aula você entende OLTP vs OLAP e **modela o star schema do Olist** — a fato `fct_order_items` e suas dimensões — além de ver SCD Tipo 2 num vendedor que muda de cidade.

### OLTP vs OLAP (no Olist)

São dois propósitos opostos para um banco:

| Aspecto | OLTP (transacional) | OLAP (analítico) |
| --- | --- | --- |
| **Objetivo** | Operar o negócio | Analisar o negócio |
| **No Olist** | Registrar o pedido 1234 | Faturamento por categoria no ano |
| **Operação** | Inserir/atualizar 1 registro | Agregar milhões de registros |
| **Modelagem** | Normalizada (as 9 tabelas) | Dimensional (estrela) |
| **Tecnologia** | PostgreSQL, MySQL | DuckDB, BigQuery, Snowflake |

A regra: você **não** roda relatórios pesados no banco OLTP de produção. No Olist, as 9 tabelas normalizadas são a forma OLTP; nós **copiamos** esse dado para uma forma OLAP (a estrela) onde a análise acontece rápido. Construir essa cópia é o trabalho de engenharia — e é o que faremos com dbt na Unidade 2.

![Esquema estrela (star schema) com uma tabela de fatos central ligada a várias tabelas de dimensão](https://commons.wikimedia.org/wiki/Special:FilePath/Star-schema.png)

### Normalização e desnormalização

**Normalização** elimina redundância dividindo os dados em várias tabelas — exatamente como o Olist vem (9 tabelas, cada coisa em seu lugar). É ótimo para o OLTP: a cidade de um vendedor fica num só lugar.

No OLAP queremos o oposto: **desnormalização**. Juntar dados em poucas tabelas largas reduz os *joins* que uma consulta analítica precisa fazer. No Olist, em vez de juntar 4 tabelas a cada pergunta, vamos pré-juntar os itens com pedido, produto e vendedor numa única **fato larga**. Aceitamos a redundância em troca de velocidade — o coração da modelagem dimensional.

### Esquema estrela e floco de neve

- **Esquema estrela (star schema)** — uma **fato central** ligada diretamente a **dimensões desnormalizadas**. Simples, rápido, padrão.
- **Esquema floco de neve (snowflake)** — dimensões **normalizadas**, quebradas em subtabelas. Economiza espaço, mas exige mais joins.

No Olist, a categoria de produto poderia virar um floco (`produto → categoria → tradução`), mas vamos preferir a **estrela**: armazenamento é barato e simplicidade de consulta vale mais.

### O star schema do Olist (fatos e dimensões)

Eis o desenho que vamos construir. **Grão = um item de pedido** (a granularidade mais fina, de onde tudo se agrega):

- **Fato `fct_order_items`** — uma linha por item; métricas **`price`** e **`freight_value`**; chaves para as dimensões.
- **`dim_customers`** — cliente (cidade, UF, `customer_unique_id`).
- **`dim_products`** — produto (categoria, peso, dimensões).
- **`dim_sellers`** — vendedor (cidade, UF).
- **`dim_dates`** — calendário derivado de `order_purchase_timestamp` (dia, mês, trimestre, ano).

O SQL conceitual que **desnormaliza** as tabelas do Olist numa fato — pré-juntando itens, pedidos, produtos e vendedores:

```sql
-- star schema do Olist: a fato no grão de item de pedido
CREATE TABLE fct_order_items AS
SELECT i.order_id,
       i.product_id,
       i.seller_id,
       o.customer_id,
       CAST(o.order_purchase_timestamp AS DATE) AS date_key,
       i.price,
       i.freight_value
FROM raw.order_items i
JOIN raw.orders o USING (order_id);
```

A consulta analítica típica agora **filtra e agrupa pelas dimensões** e **soma as métricas da fato**: "some `price` (fato), agrupando por categoria (`dim_products`) e por mês (`dim_dates`)". Um único join leve, em vez de quatro.

### Slowly Changing Dimensions (SCD) — um vendedor do Olist que muda de cidade

E quando um atributo de dimensão **muda**? No Olist, imagine que o vendedor `seller_123` **mudou de São Paulo (SP) para Campinas (SP)**. Como registrar isso sem corromper a história das vendas antigas?

| Tipo | Estratégia | Efeito |
| --- | --- | --- |
| **SCD Tipo 0** | Nunca muda | Atributo fixo |
| **SCD Tipo 1** | Sobrescreve | Perde a história; vendas antigas passam a "mentir" a cidade |
| **SCD Tipo 2** | Cria nova linha | Preserva a história, com datas de validade |
| **SCD Tipo 3** | Guarda valor anterior em coluna | Só a versão anterior e a atual |

O **Tipo 2** é o mais importante: ao mudar a cidade do `seller_123`, você **fecha** a linha antiga (data de fim) e cria uma **nova** (data de início), com um indicador de "linha atual". Assim, uma venda feita quando ele estava em São Paulo continua atribuída a São Paulo. Sem SCD Tipo 2, um relatório de "vendas por cidade do vendedor" ficaria errado retroativamente. **Implementaremos isso com `dbt snapshot` na Aula 9.**

### Exemplo numérico: tamanho da fato do Olist e a projeção de escala

A fato `fct_order_items` tem o grão de item: o Olist tem **~112 650 itens**. Suponha que cada linha da fato ocupe $80\,\text{bytes}$:

$$
112\,650 \times 80\,\text{bytes} \approx 9\,012\,000\,\text{bytes} \approx 9\,\text{MB}
$$

São apenas **9 MB** — o Olist inteiro cabe folgado na memória do laptop, e por isso o DuckDB o resolve em segundos. Mas imagine o Olist na **escala da Amazon**, mil vezes maior:

$$
112\,650 \times 1\,000 \approx 1{,}13 \times 10^{8}\ \text{(itens)} \times 80\,\text{bytes} \approx 9\,\text{GB}
$$

E num cenário de 1 milhão de vezes (alguns anos de um marketplace global), seriam **bilhões de linhas** e terabytes de fato. É exatamente esse crescimento que justifica **formato colunar** (Parquet, da Aula 2) e **bancos OLAP** distribuídos: rodar `GROUP BY` sobre bilhões de linhas é a carga para a qual o data warehouse foi desenhado.

### Atividade prática

Modele e construa o star schema do Olist:

1. Desenhe no papel a **estrela do Olist**: a fato `fct_order_items` no centro, ligada a `dim_customers`, `dim_products`, `dim_sellers` e `dim_dates`. Marque as **chaves** e as **métricas** (`price`, `freight_value`).
2. No DuckDB (com o schema `raw` da Aula 3), rode o `CREATE TABLE fct_order_items` mostrado e confira o número de linhas (deve ficar próximo de **112 650**).
3. Escreva uma consulta sobre a fato que responda: **ticket médio do item** (`AVG(price)`) — confirme que fica em torno de R$ 120.
4. Pense no vendedor que muda de cidade: explique em duas frases por que **SCD Tipo 2** preserva a história e o **Tipo 1** a destrói.

### O que você verá na próxima unidade

Na **Unidade 2 — Ingestão e Processamento de Dados**, a gente sai do papel e **implementa** o que modelamos aqui. Vamos criar o projeto **dbt** do Olist (com o adapter DuckDB), transformar o schema `raw` em modelos **staging** e materializar a estrela — incluindo carga **incremental** e idempotência. Depois, processamento em escala: o equivalente local em DuckDB ao **Apache Spark** sobre o Olist, **streaming** simulando os pedidos como eventos JSON, e a **orquestração** do pipeline ponta a ponta num DAG do **Airflow**. Resumindo: nesta unidade modelamos a estrela e o relacional do Olist; na próxima, vamos **implementar a ingestão e o processamento** e colocar tudo rodando.

### Pontos-chave

- **OLTP** opera o negócio (as 9 tabelas normalizadas do Olist); **OLAP** analisa (a estrela) — e o dado é copiado de um para o outro.
- A **desnormalização** pré-junta itens + pedido + produto + vendedor numa **fato larga**, trocando redundância por velocidade de consulta.
- O star schema do Olist tem a fato **`fct_order_items`** (grão = item; métricas `price`, `freight_value`) e as dimensões `dim_customers`, `dim_products`, `dim_sellers`, `dim_dates`.
- **SCD Tipo 2** preserva a história quando um vendedor do Olist muda de cidade; o Tipo 1 reescreveria o passado (implementação com dbt na Aula 9).
- A fato do Olist tem só ~9 MB hoje, mas projetada à escala Amazon vira **bilhões de linhas** — daí colunar + OLAP distribuído.

### Para saber mais

- **Kimball Group — técnicas de modelagem dimensional:** https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/
- **dbt — snapshots (implementação de SCD Tipo 2):** https://docs.getdbt.com/docs/build/snapshots
- **Esquema estrela (Wikipedia):** https://pt.wikipedia.org/wiki/Esquema_estrela
- **Slowly Changing Dimension (Wikipedia, em inglês):** https://en.wikipedia.org/wiki/Slowly_changing_dimension

## Aula 4 — Roteiro da Videoaula 4: "Modelagem de dados: OLTP, OLAP e modelagem dimensional"

### 1. Abertura (0:00 – 0:45)

> "Na Aula 3 a gente carregou o Olist no schema raw e rodou joins. Mas rodar um join de quatro tabelas toda vez que alguém faz uma pergunta é lento. Hoje a gente modela o star schema do Olist — a fato de itens de pedido e as dimensões — que é o jeito certo de organizar o dado para análise. E vê SCD Tipo 2 num vendedor do Olist que muda de cidade."

### 2. Desenvolvimento — parte 1 (0:45 – 3:45)

> "OLTP versus OLAP. As 9 tabelas normalizadas do Olist são a forma OLTP — ótimas para registrar um pedido. Mas para analisar, a gente copia isso para uma forma OLAP: a estrela. No OLTP a gente normaliza; no OLAP a gente desnormaliza — pré-junta os itens com pedido, produto e vendedor numa fato larga. Aceita redundância para ganhar velocidade. Essa troca consciente é o coração da modelagem dimensional do Kimball."

### 3. Desenvolvimento — parte 2 (3:45 – 6:45)

> "O star schema do Olist: no centro, a fato fct_order_items, grão de um item de pedido, com as métricas price e freight_value. Em volta, as dimensões: dim_customers, dim_products, dim_sellers e dim_dates. Olha o SQL: um CREATE TABLE que junta order_items com orders e já traz product_id, seller_id, customer_id, a data e os valores. Agora a pergunta de faturamento por categoria e mês vira um join leve, não quatro."

### 4. Desenvolvimento — parte 3 (6:45 – 9:10)

> "E quando um atributo muda? O vendedor 123 do Olist muda de São Paulo para Campinas. SCD Tipo 1 sobrescreve e faz as vendas antigas mentirem a cidade. SCD Tipo 2 fecha a linha antiga e abre uma nova com data de validade — a venda passada continua atribuída a São Paulo. A gente implementa isso com dbt snapshot lá na Aula 9. E o número: a fato do Olist tem só uns 9 megabytes hoje, mas na escala da Amazon, mil vezes maior, vira 9 gigabytes — e em alguns anos, bilhões de linhas. Por isso colunar e OLAP."

### 5. Encerramento (9:10 – 9:55)

> "Com isso você fecha os fundamentos: papel, formatos, bancos e modelagem — e já tem a bronze, o schema raw e a estrela desenhada do Olist. Na Unidade 2, a gente sai do papel e implementa: cria o projeto dbt, a ingestão com staging e carga incremental, processamento batch e streaming, e orquestra tudo no Airflow. A teoria vira tubulação rodando. Te espero na Unidade 2!"

---

## Quiz não avaliativo

### Questão 1

No nosso pipeline do **Olist**, a primeira ingestão converte os CSVs crus em **Parquet** (camada bronze) e só depois o dado é transformado com dbt dentro do DuckDB. Sobre a diferença entre os padrões **ETL** e **ELT** que essa escolha representa, assinale a alternativa **correta**:

- [ ] a. ETL e ELT são exatamente o mesmo processo, apenas com nomes comerciais diferentes adotados por fornecedores distintos.
- [x] b. No ETL, o dado é transformado **antes** de ser carregado no destino; no ELT — padrão do nosso pipeline Olist — o dado bruto é carregado primeiro (bronze/`raw`) e transformado **depois**, dentro do próprio destino (DuckDB), aproveitando o baixo custo de guardar o dado cru.
- [ ] c. No ELT, o dado nunca é transformado, sendo sempre consumido em estado bruto pelos analistas.
- [ ] d. O ETL só funciona com dados não estruturados, enquanto o ELT só funciona com dados estruturados.

**Resposta correta:** `b`

**Feedback:** A alternativa (b) descreve corretamente a diferença essencial — a **ordem do "T"**. No nosso pipeline Olist adotamos **ELT**: carregamos os 9 CSVs crus na bronze e no schema `raw` (custo de armazenamento irrisório, frações de centavo) e só transformamos depois, com dbt, dentro do DuckDB. A (a) ignora a diferença real de ordem. A (c) é falsa: o ELT transforma, só que depois de carregar — é o que faremos com a estrela. A (d) inventa uma relação com tipos de dado que não existe.

### Questão 2

Considere o **teorema CAP** aplicado a uma versão distribuída e ao vivo do marketplace **Olist** durante uma Black Friday. Assinale a alternativa **correta**:

- [ ] a. O teorema CAP afirma que um banco distribuído sempre garante simultaneamente Consistência, Disponibilidade e Tolerância a partição.
- [ ] b. Como partições de rede quase nunca acontecem na prática, a escolha entre Consistência e Disponibilidade é puramente teórica e irrelevante.
- [x] c. Na presença de uma partição de rede (inevitável em sistemas distribuídos), o sistema escolhe entre **Consistência (CP)** e **Disponibilidade (AP)** — no Olist, o **pagamento** de um pedido tende a CP (não pode cobrar errado), enquanto a **contagem de visualizações** de um produto tolera AP (consistência eventual).
- [ ] d. O teorema CAP só se aplica a bancos relacionais, sendo irrelevante para qualquer banco NoSQL.

**Resposta correta:** `c`

**Feedback:** A alternativa (c) descreve corretamente o teorema e o ancora no Olist: como a tolerância a partição (P) é obrigatória em sistemas distribuídos, a escolha real é **CP** ou **AP** durante a falha. No marketplace, registrar pagamento exige consistência forte (CP); contar visualizações pode tolerar atraso (AP). A (a) contradiz o teorema. A (b) é falsa: partições são inevitáveis em escala. A (d) inverte a aplicação — o CAP é central para entender NoSQL distribuído como o Cassandra que poderia ingerir os cliques do Olist.

---

## Atividade Verificadora (AAI — Atividade Avaliativa Individual)

**Pergunta:**

> Você assumiu como engenheiro(a) de dados do projeto do nosso curso: o **pipeline do Olist**. Hoje, os dados do marketplace existem como **9 arquivos CSV** (pedidos, itens, pagamentos, avaliações, produtos, clientes, vendedores, geolocalização e tradução de categorias), cerca de 120 MB no total. O time de negócio começou a pedir análises pesadas — "faturamento por categoria de produto", "vendas por UF", "ticket médio do item", "desempenho de entrega por vendedor" — mas hoje isso exige juntar várias tabelas manualmente a cada pergunta, e ninguém quer rodar essas consultas direto sobre o banco transacional que opera o marketplace. Há ainda o desejo futuro de capturar o **stream de cliques** do app (milhões de eventos por dia).
>
> Estruture sua resposta em três partes:
>
> 1. **Diagnóstico** — explique, com os conceitos de **OLTP vs OLAP**, por que rodar essas análises sobre as 9 tabelas normalizadas (forma transacional) é inadequado, e o que muda ao copiá-las para uma forma analítica.
> 2. **Arquitetura proposta** — descreva o pipeline Olist que você construiria com a **stack local (Python + DuckDB + dbt + Airflow)**: de onde o dado sai, como ele se move (**ETL ou ELT?**), em que **formato** você o guarda (camadas) e que **modelagem** usa no destino analítico (cite a fato e as dimensões do Olist).
> 3. **Escolha de tecnologia** — para o **stream de cliques** futuro, que **tipo de banco/tecnologia** você recomendaria, justificando pelo **padrão de acesso** (escrita massiva) e pelo **teorema CAP**.

**Resposta esperada:**

> Uma resposta exemplar começa pelo **diagnóstico OLTP vs OLAP**: as 9 tabelas do Olist estão **normalizadas** (forma OLTP, ótima para registrar um pedido), mas as perguntas de negócio ("faturamento por categoria", "vendas por UF") precisam **agregar milhares a milhões de linhas** com `GROUP BY` e somas — carga **OLAP**, pesada e que disputaria recursos com a operação do marketplace se rodasse na fonte. A solução é **copiar** o dado das 9 tabelas para uma forma analítica **desnormalizada** (estrela), onde a análise roda rápido sem tocar a produção. Na **arquitetura**, espera-se o pipeline do nosso curso: o dado **sai dos 9 CSVs** (sistema-fonte), é ingerido com **Python/DuckDB** no padrão **ELT** (carrega o cru primeiro — camada **bronze em Parquet** e schema **`raw`** —, transforma depois), e é transformado com **dbt** (staging → estrela) dentro do **DuckDB**, armazenando as camadas em **Parquet (bronze/silver/gold)**. O destino analítico usa **modelagem dimensional**: a fato **`fct_order_items`** (grão = item de pedido; métricas `price` e `freight_value`) ligada às dimensões **`dim_customers`, `dim_products`, `dim_sellers` e `dim_dates`**. Assim, "faturamento por categoria no mês" vira um join leve sobre a estrela. Tudo orquestrado pelo **Airflow**. Para o **stream de cliques**, a resposta deve reconhecer o **padrão de escrita massiva e contínua** (milhões de eventos/dia, milhares por segundo nos picos): recomenda-se **ingestão por streaming** (ex.: Apache Kafka) e armazenamento num banco otimizado para escrita, como um **NoSQL colunar (Cassandra)**, ou direto no data lake. Pelo **teorema CAP**, para cliques a **disponibilidade (AP)** importa mais que a consistência imediata — perder consistência por instantes numa contagem de cliques é aceitável; ficar fora do ar não é —, então **consistência eventual** é uma troca razoável (diferente do **pagamento**, que seria CP). A resposta de qualidade conecta cada decisão a um conceito da unidade (OLTP/OLAP, ELT, Parquet/Medallion, estrela do Olist, CAP) e à nossa stack local, evitando "jogar tecnologia" sem justificar pelo padrão de acesso.

---

## Material complementar

### Direto da fonte — livro da Biblioteca Virtual

> Esta é, hoje, a obra de referência para entrar em engenharia de dados começando do conceito e chegando à prática. O capítulo de abertura define a disciplina e apresenta o **ciclo de vida da engenharia de dados** com suas correntes transversais — exatamente a espinha dorsal que mapeamos sobre o Olist nesta Unidade 1 (do CSV no Kaggle ao dashboard/ML). Leitura **essencial** para fixar o vocabulário antes de partir para a implementação com DuckDB e dbt na Unidade 2.

- **Nome do livro:** *Fundamentals of Data Engineering*
- **Capítulo:** Capítulo 1 — *Data Engineering Described* e Capítulo 2 — *The Data Engineering Lifecycle*
- **Organizador:** Joe Reis e Matt Housley
- **Editora:** O'Reilly Media
- **Link de acesso (BV):** https://learning.oreilly.com/library/view/fundamentals-of-data/9781098108298/
- **Aula em que entra:** Aulas 1 a 4

### Para mergulhar no assunto

> Para entender por dentro o motor que vamos usar o curso inteiro, recomendo explorar **"Why DuckDB?"** e a documentação oficial do DuckDB. O DuckDB é o "warehouse no laptop" que sustenta todo o nosso pipeline Olist: lê CSV e Parquet nativamente, fala SQL padrão e roda joins sobre os ~112 mil itens do Olist em frações de segundo, sem servidor. Entender por que ele é tão rápido (execução vetorizada, colunar) ilumina metade das decisões de arquitetura desta disciplina.

- **Link(s):** https://duckdb.org/why_duckdb (e a documentação completa em https://duckdb.org/docs/)
- **Aula em que entra:** Aulas 2 e 3 (ingestão e carga do Olist no DuckDB)

### Podcast (curadoria, até 45 min)

> O canal **DuckDB no YouTube** traz palestras e demonstrações da equipe e da comunidade sobre o motor que é a espinha do nosso pipeline. É ótimo para ver, na prática, o DuckDB lendo Parquet e rodando análises locais como as que fazemos sobre o Olist — o vocabulário da unidade aplicado por quem desenvolve a ferramenta.

- **Nome do podcast/canal:** DuckDB — canal oficial no YouTube
- **Tema recomendado:** Ingestão e análise local com DuckDB (CSV/Parquet, como no pipeline Olist)
- **Link:** https://www.youtube.com/@DuckDB
- **Aula em que entra:** Aula 2

### Artigo científico

> Este é o artigo **fundador** de toda a teoria de bancos de dados relacionais. Publicado por Edgar F. Codd em 1970, ele propõe o modelo relacional — tabelas, relações, álgebra relacional — que é exatamente o que usamos na Aula 3 ao carregar o Olist no schema `raw` do DuckDB e juntar `orders`, `order_items` e `products` por suas chaves. Ler o original dá perspectiva histórica e mostra que cada join que fazemos no Olist nasceu de uma ideia teórica precisa.

- **Link:** https://doi.org/10.1145/362384.362685 (DOI)
- **Aula em que entra:** Aula 3
- **Referência bibliográfica do artigo no formato ABNT:**
  > CODD, Edgar Frank. **A relational model of data for large shared data banks**. *Communications of the ACM*, v. 13, n. 6, p. 377-387, 1970.
