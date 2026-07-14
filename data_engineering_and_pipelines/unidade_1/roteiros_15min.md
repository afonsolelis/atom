# Roteiros Estendidos Hands-on (15–20 minutos) — Unidade 1: Fundamentos de Engenharia de Dados

- **Disciplina:** Data Engineering and Pipelines
- **Conteudista:** Afonso Cesar Lelis Brandão
- **Videoaulas:** 1 a 4
- **Formato:** roteiro de gravação **hands-on em GitHub Codespaces** — o texto em citação (>) é a fala; os blocos de código são **executados ao vivo** na tela durante a gravação. Duração-alvo: **15 a 20 minutos** por aula, já contando o tempo de digitar/rodar os comandos.

> **Convenções deste roteiro:**
> - **[TELA]** — o que deve estar visível (slide ou Codespace).
> - **[CÓDIGO]** — bloco a digitar/colar no editor ou terminal do Codespace, narrando enquanto digita.
> - **[EXECUTAR]** — rodar e mostrar a saída na tela.
> - **[CHECKPOINT]** — resultado esperado; confira em voz alta antes de seguir.
> - **100% offline:** a disciplina inteira roda **sem nenhuma conta, chave de API ou serviço externo** — os dados são gerados por um script próprio (`gerar_dados.py`, com seed fixa e números determinísticos) no mesmo formato do dataset público do Olist. Só o `pip install` usa a internet.
> - Antes de gravar cada aula, deixe o Codespace **já aberto e aquecido**. Instalações longas: rode antes, mostre o resultado.

---

## Roteiro da Videoaula 1 — "O que é Engenharia de Dados? + Setup do projeto no Codespaces"

**Duração-alvo:** 17 a 19 minutos.

### 1. Abertura (0:00 – 1:30)

**[TELA]** Slide de capa da aula 1.

> "Olá! Eu sou o professor Afonso Brandão, e seja muito bem-vindo, muito bem-vinda à Aula 1 — que é mais do que uma aula: é o pontapé de um **projeto que vai durar a disciplina inteira**. Nós vamos construir, do zero, um pipeline de dados completo sobre o **Olist** — um marketplace brasileiro com **99 mil pedidos** distribuídos em **9 arquivos CSV**: pedidos, itens, pagamentos, avaliações, produtos, clientes, vendedores, geolocalização e categorias. E nada de depender de cadastro em site nenhum: nós vamos **gerar esses dados com um script próprio**, no mesmo formato do famoso dataset público do Olist — o que significa que qualquer pessoa, em qualquer máquina, reproduz o curso inteiro sem criar uma única conta externa."

> "E não vai ser no papel: vai ser **na tela, comigo, código por código**, dentro do **GitHub Codespaces** — um ambiente de desenvolvimento completo que roda no navegador, de graça. Ao final da disciplina, você terá um pipeline completo — ingestão, DuckDB, dbt, Airflow, testes e ML — **no seu GitHub**, pronto para mostrar em entrevista. Hoje a gente faz duas coisas: entende **o que é engenharia de dados** — papel, ciclo de vida, diferença para ciência de dados — e depois, **mão no teclado**: cria o repositório, sobe o Codespace, gera os dados e deixa o projeto respirando. Bora."

### 2. O que é engenharia de dados + o ciclo de vida (1:30 – 4:30)

**[TELA]** Slide: definição + tabela do ciclo de vida sobre o Olist.

> "A definição: **engenharia de dados** é a disciplina que projeta, constrói e mantém os sistemas que **coletam, armazenam, transportam e transformam dados** em escala, de forma confiável. E atenção ao produto final: não é um gráfico, não é um modelo — é o **dado disponível, íntegro e organizado** que outras pessoas vão consumir. Pensa no chef de cozinha: o cientista de dados é o chef que brilha no prato final; o engenheiro de dados é quem comprou, lavou, cortou e organizou os ingredientes na bancada. Sem essa base, ninguém cozinha."

> "E o trabalho se organiza no **ciclo de vida da engenharia de dados**, do livro *Fundamentals of Data Engineering* — olha ele mapeado no nosso projeto: **geração** — a compra no marketplace virando os 9 CSVs; **ingestão** — Python e DuckDB lendo esses CSVs para a camada bronze e o schema `raw`; **transformação** — o dbt limpando e montando a modelagem em estrela; **armazenamento** — o banco `olist.duckdb` e os Parquet em bronze, silver e gold; e **disponibilização** — os marts servindo BI e machine learning. E atravessando todas as etapas, as **correntes transversais**: segurança, governança e qualidade, metadados, orquestração — que será o Airflow — e engenharia de software. Esse mapa é a disciplina inteira numa tabela; a gente vai preenchê-lo célula por célula."

> "E a confusão clássica que eu quero matar hoje: engenheiro, cientista e analista. O **engenheiro** move e prepara — a entrega dele no Olist é a `fct_order_items` confiável. O **cientista** cria modelos — 'esse pedido vai atrasar?'. O **analista** explica o que aconteceu — 'quanto vendemos por UF?'. E a relação é de dependência: **o engenheiro é a base**. Garbage in, garbage out: se o dado que entra é lixo, o modelo e o dashboard também serão."

### 3. A arquitetura-alvo do pipeline Olist (4:30 – 6:30)

**[TELA]** Slide com a arquitetura-alvo + layout do repositório.

> "Antes de codar, o mapa do tesouro — a **arquitetura-alvo** que vamos construir em 16 aulas. Guarda este desenho: **9 CSVs** → **Python/DuckDB** fazendo a ingestão → **schema `raw` no DuckDB** e **Parquet na camada bronze** → **dbt** transformando em staging, depois na estrela, depois nos marts → **camada gold** → **BI e ML** — tudo **orquestrado pelo Airflow**. E o layout do repositório espelha isso: `data/raw` com os 9 CSVs; `data/bronze`, `silver` e `gold` com os Parquet; `ingestion/` com os scripts; `dbt_olist/` com o projeto dbt; `airflow/dags/` com o DAG; e `ml/` com o modelo final."

> "E uma decisão de arquitetura que eu já anuncio e justifico daqui a pouco com números: nosso pipeline é **ELT**, não ETL. No **ETL** clássico, transforma-se **antes** de carregar. No **ELT**, carrega-se o dado **cru** primeiro e transforma-se **depois, dentro do destino**. Vamos carregar os 9 CSVs brutos primeiro — e só então transformar com dbt. Por quê? Porque armazenamento ficou barato demais para não guardar o cru — e guardar o cru dá liberdade total de reprocessar. A conta vem no fim da aula."

### 4. Mão na massa: criando o repositório e o Codespace (6:30 – 9:00)

**[TELA]** Navegador no GitHub → criar repositório → abrir Codespace.

> "Chega de slide — bora para o GitHub. Primeiro passo: criar o repositório do projeto. No GitHub, **New repository**, nome **`pipeline-olist`**, público — porque isso aqui vai ser seu portfólio —, com README. Criou? Agora o pulo do gato desta disciplina: o botão verde **Code → aba Codespaces → Create codespace on main**. O GitHub sobe para a gente uma máquina virtual com VS Code no navegador — Linux, Python, git, tudo pronto. É o nosso laboratório: o mesmo para todo mundo, independente do seu computador."

**[CÓDIGO]** No terminal do Codespace, criar a estrutura de pastas:

```bash
mkdir -p data/raw data/bronze data/silver data/gold ingestion dbt_olist airflow/dags ml
touch ingestion/.gitkeep airflow/dags/.gitkeep
ls -R --ignore=".git"
```

> "Olha a estrutura nascendo: `data` com as quatro camadas, `ingestion`, `dbt_olist`, `airflow/dags` e `ml`. Agora vamos configurar o ambiente como gente grande: com um **devcontainer**, que é a receita da máquina — assim, qualquer pessoa que abrir esse repositório num Codespace ganha o ambiente idêntico ao meu."

**[CÓDIGO]** Criar `.devcontainer/devcontainer.json`:

```json
{
  "name": "pipeline-olist",
  "image": "mcr.microsoft.com/devcontainers/python:3.11",
  "postCreateCommand": "pip install -r requirements.txt",
  "forwardPorts": [8080],
  "customizations": {
    "vscode": { "extensions": ["ms-python.python"] }
  }
}
```

**[CÓDIGO]** Criar `requirements.txt`:

```text
duckdb
dbt-duckdb
pandas
```

> "Traduzindo o devcontainer: imagem oficial de Python 3.11; ao criar o container, instala o `requirements.txt`; e já deixo a **porta 8080 encaminhada** — ela vai servir a interface do Airflow lá na Aula 8. No requirements, o núcleo da nossa stack: **duckdb**, o motor analítico; **dbt-duckdb**, o dbt com adapter para o DuckDB; e **pandas**. O Airflow e as ferramentas de qualidade a gente instala nas aulas em que entram."

**[CÓDIGO]** Instalar agora (sem esperar rebuild) e criar o `.gitignore`:

```bash
pip install -r requirements.txt
printf "data/\n*.duckdb\n__pycache__/\nlogs/\n.env\n" > .gitignore
```

> "E repara no `.gitignore`: a pasta `data` e o banco `.duckdb` **não vão para o git** — dado não se versiona em repositório de código; código sim, dado não. Essa é a primeira boa prática de engenharia de software aplicada a dados da disciplina."

### 5. Gerando o dataset Olist — sem conta, sem API (9:00 – 12:00)

**[TELA]** Editor + terminal.

> "Agora, a matéria-prima — e aqui vem a decisão de design do curso. O dataset público do Olist mora no Kaggle, e baixá-lo exige conta e chave de API. Nós vamos por um caminho melhor para uma disciplina: **gerar os dados nós mesmos**, com um script Python que produz os **9 CSVs no mesmo formato e nas mesmas ordens de grandeza** do dataset real — 99.441 pedidos, 112.650 itens, 96.096 clientes únicos, 3.095 vendedores, 1 milhão de linhas de geolocalização. Com **seed fixa**: todo mundo que rodar gera **exatamente os mesmos números** que eu. E tem mais: o gerador planta, de propósito, as características que vamos explorar nas aulas — uma Black Friday em novembro de 2017, e até uns defeitos de dados escondidos que só vamos caçar na Unidade 4. Se um dia você quiser trocar pelo dataset real, é só baixar manualmente no navegador e substituir os arquivos — **o pipeline é idêntico**, porque o formato é o mesmo."

> "O script está nos materiais da aula — são umas cem linhas; eu colo no editor e a gente lê as partes importantes juntos:"

**[CÓDIGO]** Criar `ingestion/gerar_dados.py` (colar do material de apoio):

```python
# gera os 9 CSVs no formato do dataset publico do Olist — sem APIs, 100% local
import csv, os, random
from datetime import datetime, timedelta

random.seed(42)                                   # mesma seed = mesmos dados
os.makedirs("data/raw", exist_ok=True)
BASE = datetime(2016, 9, 4)                       # inicio do historico
DIAS = 774                                        # ate out/2018

def uid(k=32):
    return "".join(random.choices("0123456789abcdef", k=k))

UFS = (["SP"]*42 + ["RJ"]*13 + ["MG"]*12 + ["RS"]*5 + ["PR"]*5 + ["SC"]*4 +
       ["BA"]*4 + ["DF"]*2 + ["GO"]*2 + ["ES"]*2 + ["PE"]*2 + ["CE"]*2 +
       ["PA","MT","MA","MS","PB","RN","AL","SE","TO","AM","RO","PI"])
CIDADE = {"SP":"sao paulo","RJ":"rio de janeiro","MG":"belo horizonte",
          "RS":"porto alegre","PR":"curitiba","SC":"florianopolis","BA":"salvador"}
STATUS = (["delivered"]*97 + ["shipped","canceled","invoiced"])
FRASES = ["chegou antes do prazo","produto veio errado","excelente vendedor",
          "recomendo","veio com defeito","entrega rapida","produto de qualidade",""]

# --- categorias (71) e traducao -------------------------------------------
TOP = [("beleza_saude","health_beauty",14),("relogios_presentes","watches_gifts",12),
       ("cama_mesa_banho","bed_bath_table",11),("esporte_lazer","sports_leisure",8),
       ("informatica_acessorios","computers_accessories",8),
       ("moveis_decoracao","furniture_decor",7),("utilidades_domesticas","housewares",6),
       ("automotivo","auto",5),("brinquedos","toys",4),("cool_stuff","cool_stuff",4)]
CATS  = [c for c, _, _ in TOP] + [f"categoria_{i:02d}" for i in range(1, 62)]
PESOS = [p for _, _, p in TOP] + [0.35]*61
with open("data/raw/product_category_name_translation.csv","w",newline="") as f:
    w = csv.writer(f); w.writerow(["product_category_name","product_category_name_english"])
    for c,(en) in zip(CATS,[en for _,en,_ in TOP]+[f"category_{i:02d}" for i in range(1,62)]):
        w.writerow([c, en])

# --- sellers (3.095) e products (32.951) ----------------------------------
sellers = [uid() for _ in range(3095)]
with open("data/raw/olist_sellers_dataset.csv","w",newline="") as f:
    w = csv.writer(f); w.writerow(["seller_id","seller_zip_code_prefix","seller_city","seller_state"])
    for s in sellers:
        u = random.choice(UFS); w.writerow([s, random.randint(1000,99990), CIDADE.get(u,"interior"), u])
produtos = [(uid(), random.choices(CATS, weights=PESOS)[0]) for _ in range(32951)]
with open("data/raw/olist_products_dataset.csv","w",newline="") as f:
    w = csv.writer(f); w.writerow(["product_id","product_category_name","product_name_lenght",
        "product_description_lenght","product_photos_qty","product_weight_g",
        "product_length_cm","product_height_cm","product_width_cm"])
    for p, c in produtos:
        w.writerow([p, c, random.randint(20,60), random.randint(100,3000),
                    random.randint(1,6), random.randint(50,30000),
                    random.randint(10,100), random.randint(2,100), random.randint(6,100)])

# --- orders (99.441, com Black Friday 24/11/2017) + customers --------------
N = 99441; BF = datetime(2017,11,24)
unicos = [uid() for _ in range(96096)]
fo = open("data/raw/olist_orders_dataset.csv","w",newline=""); wo = csv.writer(fo)
fc = open("data/raw/olist_customers_dataset.csv","w",newline=""); wc = csv.writer(fc)
wo.writerow(["order_id","customer_id","order_status","order_purchase_timestamp",
             "order_approved_at","order_delivered_carrier_date",
             "order_delivered_customer_date","order_estimated_delivery_date"])
wc.writerow(["customer_id","customer_unique_id","customer_zip_code_prefix",
             "customer_city","customer_state"])
pedidos = []                                       # (order_id, prazo, frete_medio_flag)
for i in range(N):
    oid, cid = uid(), uid()
    if i < 1300:                                   # pico da Black Friday
        compra = BF + timedelta(hours=random.randint(19,23), minutes=random.choice(range(0,60,5)))
    else:
        compra = BASE + timedelta(days=int(DIAS*random.random()**0.7),
                                  hours=random.randint(0,23), minutes=random.randint(0,59))
    status = random.choice(STATUS)
    prazo  = random.randint(10,40)
    estim  = compra + timedelta(days=prazo)
    frete  = round(random.uniform(8,45), 2)
    if status == "delivered":
        if i < 18:                                 # 18 defeitos plantados p/ Aula 13
            entrega = compra - timedelta(days=random.randint(1,3))
        else:                                      # atraso correlacionado c/ features
            desvio = -10 + 0.12*(frete-26) + 0.3*(25-prazo) + random.gauss(0,7)
            entrega = estim + timedelta(days=desvio)
        wo.writerow([oid, cid, status, compra, compra, compra+timedelta(days=2), entrega, estim])
    else:
        wo.writerow([oid, cid, status, compra, compra, "", "", estim])
    u = random.choice(UFS)
    wc.writerow([cid, unicos[i] if i < 96096 else random.choice(unicos),
                 random.randint(1000,99990), CIDADE.get(u,"interior"), u])
    pedidos.append((oid, compra, frete))
fo.close(); fc.close()

# --- items (112.650), payments e reviews -----------------------------------
fi = open("data/raw/olist_order_items_dataset.csv","w",newline=""); wi = csv.writer(fi)
wi.writerow(["order_id","order_item_id","product_id","seller_id",
             "shipping_limit_date","price","freight_value"])
totais = {}
for i,(oid, compra, frete) in enumerate(pedidos):
    n_itens = 2 if i < 13209 else 1               # 99.441 + 13.209 = 112.650 itens
    total = 0
    for k in range(1, n_itens+1):
        preco = round(min(random.lognormvariate(4.54, 0.7), 6735), 2)
        total += preco + frete
        p, _ = random.choice(produtos)
        wi.writerow([oid, k, p, random.choice(sellers), compra+timedelta(days=4), preco, frete])
    totais[oid] = round(total, 2)
fi.close()
with open("data/raw/olist_order_payments_dataset.csv","w",newline="") as f:
    w = csv.writer(f); w.writerow(["order_id","payment_sequential","payment_type",
                                   "payment_installments","payment_value"])
    for i,(oid, _, _) in enumerate(pedidos):
        tipo = random.choices(["credit_card","boleto","voucher","debit_card"],[74,19,5,2])[0]
        w.writerow([oid, 1, tipo, random.randint(1,10) if tipo=="credit_card" else 1, totais[oid]])
        if i < 4445: w.writerow([oid, 2, "voucher", 1, 10.0])
with open("data/raw/olist_order_reviews_dataset.csv","w",newline="") as f:
    w = csv.writer(f); w.writerow(["review_id","order_id","review_score",
        "review_comment_title","review_comment_message","review_creation_date","review_answer_timestamp"])
    for oid, compra, _ in pedidos:
        nota = random.choices([5,4,3,2,1],[57,19,8,4,12])[0]
        w.writerow([uid(), oid, nota, "", random.choice(FRASES),
                    compra+timedelta(days=25), compra+timedelta(days=27)])

# --- geolocation (~1 milhao de linhas) -------------------------------------
with open("data/raw/olist_geolocation_dataset.csv","w",newline="") as f:
    w = csv.writer(f); w.writerow(["geolocation_zip_code_prefix","geolocation_lat",
                                   "geolocation_lng","geolocation_city","geolocation_state"])
    for _ in range(1000163):
        u = random.choice(UFS)
        w.writerow([random.randint(1000,99990), round(random.uniform(-33.7,2.5),6),
                    round(random.uniform(-73.9,-34.8),6), CIDADE.get(u,"interior"), u])

print("9 CSVs gerados em data/raw — pipeline Olist pronto para comecar.")
```

**[EXECUTAR]**

```bash
python ingestion/gerar_dados.py
ls -lh data/raw
```

**[CHECKPOINT]**

> "Alguns segundos… e confere comigo na listagem: **9 arquivos CSV** — `olist_orders_dataset.csv`, `olist_order_items_dataset.csv`, pagamentos, reviews, produtos, clientes, vendedores, o gigante `olist_geolocation_dataset.csv` com 1 milhão de linhas, e a tradução de categorias. E repara nos detalhes de engenharia do gerador enquanto ele passou na tela: a **seed 42** — determinismo total, seus números serão idênticos aos meus; os pesos por UF — SP com a maior fatia, como no Brasil real; as categorias com pesos — beleza e saúde no topo; a **Black Friday de 24/11/2017** plantada com 1.300 pedidos concentrados; e umas linhas misteriosas marcando '18 defeitos' que eu não vou explicar hoje — guarda a curiosidade para a Unidade 4. O sistema-fonte está na sua máquina, e você é dono dele de ponta a ponta."

### 6. O primeiro código do pipeline (12:00 – 14:00)

**[TELA]** Editor + terminal.

> "E agora, o momento solene: o primeiro código do nosso pipeline. Quatro linhas que abrem o banco DuckDB local e provam que a stack está viva."

**[CÓDIGO]** Criar `ingestion/hello_pipeline.py`:

```python
import duckdb

con = duckdb.connect("olist.duckdb")   # cria/abre o banco local
print(con.sql("SELECT 'pipeline Olist no ar!' AS status"))
print(con.sql("SELECT COUNT(*) AS pedidos FROM read_csv_auto('data/raw/olist_orders_dataset.csv')"))
con.close()
```

**[EXECUTAR]**

```bash
python ingestion/hello_pipeline.py
```

**[CHECKPOINT]**

> "Duas saídas na tela: o status **'pipeline Olist no ar!'** — e olha a segunda: o DuckDB **leu o CSV de pedidos direto do disco** e contou… **99.441 pedidos**. Exatamente o número que o gerador prometeu — determinismo funcionando. Sem servidor, sem importação prévia: uma linha de SQL sobre um arquivo. Esse é o motor que vai sustentar a disciplina inteira: o DuckDB é um warehouse analítico que roda **dentro do processo Python**, no Codespace — e é absurdamente rápido, porque é colunar e vetorizado. Você acabou de rodar sua primeira consulta de engenharia de dados."

### 7. Por que ELT: a conta do armazenamento (14:00 – 15:30)

**[TELA]** Slide com a conta do custo de armazenamento.

> "E agora eu pago a promessa da arquitetura: por que **ELT**? Com números. O nosso Olist tem 9 tabelas, 99 mil pedidos, 112 mil itens — cerca de **120 megabytes** em CSV. Quanto custa guardar isso cru num armazenamento de objetos na nuvem? O preço típico é 2,3 centavos de dólar por gigabyte ao mês. 120 megabytes são 0,117 gigabytes: 0,117 vezes 0,023… **0,27 centavos de dólar por mês**. Menos de um centavo. E no nosso Codespace, com DuckDB e Parquet, o custo é literalmente **zero**."

> "É esse custo irrisório que torna o ELT economicamente óbvio: **carregue tudo cru, transforme depois**. Guardar o bruto compra um seguro valioso: errou uma transformação? Reprocessa do cru, quantas vezes quiser. E no nosso caso, tem um seguro ainda melhor: perdeu tudo? `python ingestion/gerar_dados.py` e o mundo renasce idêntico. No mundo do ETL antigo, o dado que você não carregou está perdido para sempre. No ELT, o cru é o backup eterno da verdade."

### 8. Commit e fechamento do setup (15:30 – 16:30)

**[CÓDIGO]** Versionar o esqueleto:

```bash
git add .
git commit -m "chore: estrutura do projeto, devcontainer, gerador de dados e primeiro script DuckDB"
git push
```

> "E fecha a aula com a disciplina de sempre: **commit e push**. Repara que o `gerar_dados.py` **vai** para o git — ele é código, e é a nossa 'fonte' reprodutível — enquanto a pasta `data/` fica de fora. A partir de agora, **toda aula termina com um commit**: ao final da disciplina, o histórico do seu repositório conta a história do pipeline sendo construído — e recrutador adora ler histórico de commit."

### 9. Atividade + encerramento e gancho (16:30 – 17:30)

**[TELA]** Enunciado da atividade.

> "Sua missão até a próxima aula: reproduzir **tudo** o que fiz hoje no seu próprio repositório — criar o `pipeline-olist`, subir o Codespace com devcontainer, rodar o `gerar_dados.py` e conferir os **99.441 pedidos** com o script de contagem. E mais: escreve, no README, **uma frase para cada etapa do ciclo de vida** mapeada no Olist. Quem termina a Aula 1 com o ambiente rodando não trava nunca mais na disciplina — o setup é a única barreira, e você acabou de vencê-la."

> "Na próxima aula, a gente olha de perto a matéria-prima: os tipos e formatos de dado — e faz a **primeira ingestão de verdade**: converter os 9 CSVs em **Parquet**, criando a camada **bronze**, e medir a compressão real na tela. Te espero na Aula 2. Um abraço!"

---

## Roteiro da Videoaula 2 — "Tipos, formatos e fontes de dados: nasce a camada bronze"

**Duração-alvo:** 16 a 18 minutos.

### 1. Abertura (0:00 – 1:15)

**[TELA]** Slide de capa; Codespace aberto ao lado.

> "Olá! Bem-vindo, bem-vinda de volta. Na Aula 1 montamos o laboratório: o Codespace está de pé, os 9 CSVs do Olist estão em `data/raw` — gerados pelo nosso script, sem depender de ninguém — e o DuckDB já contou 99.441 pedidos. Hoje a gente olha de perto essa matéria-prima — porque **dado não é tudo igual**: tem dado arrumadinho em tabela e tem texto livre; tem formato que custa caro para ler e formato que voa. E a aula termina com a **primeira ingestão real do pipeline**: os 9 CSVs convertidos em **Parquet** — a camada **bronze** nascendo na sua tela, com a compressão medida em números. Bora."

### 2. Estruturado, semiestruturado, não estruturado (1:15 – 3:30)

**[TELA]** Tabela dos três tipos, com a coluna "No Olist".

> "Primeira classificação: o **grau de estrutura**. Dado **estruturado**: tabela com colunas e tipos — no Olist, quase tudo: `orders`, `order_items`, `payments`, `geolocation`. Dado **semiestruturado**: estrutura flexível e aninhada — JSON, XML, logs; no nosso projeto ele vai surgir na Aula 7, quando emitirmos os pedidos como **eventos JSON** para simular streaming. E dado **não estruturado**: sem esquema — texto livre, imagem, áudio. Estima-se que **80% do dado do mundo** seja não estruturado."

> "E o Olist tem uma ilha não estruturada escondida — deixa eu mostrar ao vivo."

**[CÓDIGO]** No terminal, espiar o campo de texto livre:

```bash
python -c "
import duckdb
print(duckdb.sql(\"\"\"
    SELECT review_score, review_comment_message
    FROM read_csv_auto('data/raw/olist_order_reviews_dataset.csv')
    WHERE review_comment_message IS NOT NULL
    LIMIT 5
\"\"\"))"
```

**[CHECKPOINT]**

> "Olha na tela: o `review_comment_message` — o texto que o cliente escreveu ao avaliar: 'chegou antes do prazo', 'produto veio errado'… Isso é **texto livre, não estruturado**, morando dentro de um CSV estruturado. E saber classificar já orienta a engenharia: essas colunas numéricas ao lado se agregam com SQL; esse texto pediria **NLP**. Mesma tabela, dois mundos."

### 3. Os quatro formatos: CSV, JSON, Parquet, Avro (3:30 – 6:00)

**[TELA]** Slide comparando os 4 formatos + esquema linha × coluna.

> "Segunda classificação: o **formato de arquivo** — e aqui mora dinheiro. **CSV**: texto puro separado por vírgula. Universal, legível… e **sem tipos** — tudo é texto — sem compressão, ineficiente em escala. É como a nossa fonte entrega. **JSON**: texto hierárquico de chave e valor, a língua das APIs — flexível, porém **verboso**; vamos usá-lo na Aula 7 para o stream. **Parquet**: formato **binário, colunar e comprimido** — o padrão absoluto de analytics; é para onde vamos converter o Olist agora. E **Avro**: binário **por linha**, com esquema embutido — excelente para ingestão e streaming."

> "E a diferença conceitual que explica tudo: **orientação a linha versus orientação a coluna**. O CSV guarda linha por linha — para ler uma coluna, você atravessa todas as linhas inteiras. O Parquet guarda **coluna por coluna** — uma consulta que usa só `price` lê **só o bloco do `price`** e ignora o resto do arquivo. Para analytics, que vive de agregar poucas colunas sobre muitas linhas, é a arquitetura perfeita. A regra prática para a vida: **CSV e JSON para troca e ingestão; Parquet para analytics; Avro para streaming**. Nosso pipeline segue à risca: entra CSV, vira Parquet."

### 4. Mão na massa: a primeira ingestão CSV → Parquet (6:00 – 9:30)

**[TELA]** Editor + terminal do Codespace.

> "Chega de teoria — vamos construir a **camada bronze**. E olha que bonito: no DuckDB, converter um CSV em Parquet é **uma linha de SQL** — um `COPY` para fora. Mas nós somos engenheiros: em vez de repetir nove vezes, escrevemos o script que varre a pasta inteira."

**[CÓDIGO]** Criar `ingestion/to_bronze.py`:

```python
import duckdb, glob, os

con = duckdb.connect("olist.duckdb")
os.makedirs("data/bronze", exist_ok=True)

# varre TODOS os CSVs de data/raw: 8 no padrao olist_*_dataset.csv
# + product_category_name_translation.csv = 9 arquivos
for csv in sorted(glob.glob("data/raw/*.csv")):
    nome = (os.path.basename(csv)
            .replace("olist_", "")
            .replace("_dataset", "")
            .replace(".csv", ""))
    con.sql(f"COPY (SELECT * FROM read_csv_auto('{csv}')) "
            f"TO 'data/bronze/{nome}.parquet' (FORMAT PARQUET)")
    print(f"bronze ok: {nome}")

con.close()
```

**[EXECUTAR]**

```bash
python ingestion/to_bronze.py
ls -lh data/bronze
```

**[CHECKPOINT]**

> "Nove linhas de 'bronze ok' e — olha o `ls` — **nove arquivos Parquet** em `data/bronze`: `orders.parquet`, `order_items.parquet`, `customers.parquet`… Repara no que aconteceu conceitualmente: acabamos de executar o **E** e o **L** do nosso ELT — extraímos da fonte e carregamos **cru**, sem transformar nada, num formato analítico. Isso é a camada bronze de um lakehouse: o dado bruto, imutável, preservado. E repara no loop: o script normaliza os nomes — tira o `olist_` e o `_dataset` — porque nomes limpos agora poupam dor de cabeça depois."

### 5. Medindo a compressão ao vivo (9:30 – 12:00)

**[TELA]** Terminal, comparação de tamanhos lado a lado.

**[CÓDIGO]** Comparar CSV × Parquet:

```bash
ls -lh data/raw/olist_order_items_dataset.csv data/bronze/order_items.parquet
ls -lh data/raw/olist_geolocation_dataset.csv data/bronze/geolocation.parquet
```

**[CHECKPOINT]**

> "Compara os pares na tela: o Parquet de itens ficou **várias vezes menor** que o CSV — anota o fator exato que apareceu aí na sua execução. E olha o caso da geolocalização, com 1 milhão de linhas: a diferença é ainda mais gritante, porque coluna com valores repetidos — UF, cidade — comprime maravilhosamente bem no formato colunar. No dataset real do Olist, o fator típico da tabela de itens chega perto de **4 vezes**; nos nossos dados sintéticos vai variar um pouco — os IDs aleatórios comprimem menos que dados reais — e essa variação é, ela mesma, uma lição: **compressão depende da natureza do dado**."

> "Mas o ganho de verdade é mais profundo que o tamanho — é a **leitura seletiva**. A tabela de itens tem 7 colunas. Uma consulta de faturamento usa só duas: `price` e `freight_value` — menos de um terço das colunas. Combinando compressão com leitura colunar, uma consulta analítica sobre o Parquet toca uma **fração pequena** dos bytes que o CSV obrigaria a varrer — no dataset real, a redução chega à casa de **13 vezes menos dados lidos**. Agora multiplica por 9 tabelas e por centenas de consultas diárias de um time de dados… e você entende por que **toda camada analítica do nosso pipeline será Parquet** — e por que o mundo inteiro de analytics padronizou nesse formato."

### 6. Schema-on-read ao vivo (12:00 – 14:00)

**[TELA]** Terminal.

> "Último conceito da aula, demonstrado ao vivo: **schema-on-read versus schema-on-write**. No **schema-on-write** — o banco relacional clássico — você define o esquema **antes** de gravar, e o banco rejeita o que não couber: qualidade na entrada, rigidez como preço. No **schema-on-read**, você grava o cru **sem** esquema e interpreta na leitura: flexibilidade total, ideal para data lakes. E o DuckDB lendo nossos CSVs é schema-on-read puro — olha ele **inferindo** os tipos em tempo real:"

**[CÓDIGO]**

```bash
python -c "
import duckdb
print(duckdb.sql(\"DESCRIBE SELECT * FROM read_csv_auto('data/raw/olist_orders_dataset.csv')\"))"
```

**[CHECKPOINT]**

> "Olha a mágica na tela: `order_id` virou **VARCHAR**, `order_purchase_timestamp` virou **TIMESTAMP** — ninguém declarou nada; o DuckDB **olhou os dados e deduziu**. Isso é o schema-on-read em ação: perfeito para a bronze, onde queremos flexibilidade. Lá na frente, quando o dbt materializar a estrela, aí sim vamos **impor** esquema e testes — cada abordagem no seu andar da arquitetura."

### 7. Commit + atividade + gancho (14:00 – 16:00)

**[CÓDIGO]**

```bash
git add ingestion/to_bronze.py
git commit -m "feat(ingestion): camada bronze - 9 CSVs Olist convertidos a Parquet"
git push
```

> "Commit da aula: a bronze está no ar e o script está versionado. Sua missão até a próxima aula: primeiro, rodar o `to_bronze.py` e montar uma **tabelinha CSV × Parquet × fator de compressão** para as 9 tabelas — os fatores variam, e o porquê é interessante: repetição comprime bem, aleatoriedade comprime mal. Segundo, classificar cada um dos 9 arquivos como estruturado, semi ou não estruturado — lembra do `review_comment_message`. E terceiro, rodar o `DESCRIBE` sobre outros CSVs e conferir os tipos inferidos."

> "Na próxima aula, o Olist ganha um **banco relacional de verdade**: vamos criar o **schema `raw`** no DuckDB, carregar as 9 tabelas, entender o diagrama ER com suas chaves — e rodar **joins reais**: faturamento por categoria juntando três tabelas em frações de segundo. E de quebra: ACID, as famílias NoSQL e o teorema CAP, tudo com exemplos do Olist. Te espero na Aula 3. Um abraço!"

---

## Roteiro da Videoaula 3 — "Bancos de dados: o Olist no schema raw e os primeiros joins"

**Duração-alvo:** 17 a 19 minutos.

### 1. Abertura (0:00 – 1:15)

**[TELA]** Slide de capa; Codespace ao lado.

> "Olá! Bem-vindo, bem-vinda de volta. Na Aula 2, viramos os 9 CSVs em Parquet — a bronze existe. Mas para **juntar** essas tabelas e responder perguntas — qual produto vendeu mais? qual vendedor entrega mais rápido? — a gente precisa de um **banco de dados**. Hoje o Olist vai morar num banco relacional: vamos carregar o **schema `raw`** no DuckDB, entender como as 9 tabelas se conectam pelas chaves, rodar **joins reais** ao vivo — e por cima disso entender ACID, as quatro famílias NoSQL e o teorema CAP, sempre com o Olist como exemplo. Aula cheia de código. Bora."

### 2. O modelo relacional e o ER do Olist (1:15 – 4:00)

**[TELA]** Slide: diagrama ER do Olist com as chaves.

> "O **modelo relacional** — proposto por Edgar Codd em 1970, num artigo que está no material complementar — organiza dados em **tabelas** ligadas por **chaves**: a **chave primária** identifica unicamente cada linha; a **chave estrangeira** aponta para outra tabela. E a língua desse mundo é o **SQL** — provavelmente a habilidade mais duradoura e valiosa de toda a área de dados: modas passam, SQL fica."

> "Olha o diagrama ER do Olist — decora essa espinha dorsal: **`orders` é o centro** — `order_id` é a chave primária, e `customer_id` aponta para `customers`. **`order_items`** referencia três tabelas: `orders` pelo `order_id`, `products` pelo `product_id` e `sellers` pelo `seller_id`. `order_payments` e `order_reviews` penduram em `orders` pelo `order_id`. `customers` e `sellers` ligam-se a `geolocation` pelo prefixo de CEP. E `products` liga na tradução de categorias. Resumindo numa frase: **`order_id` costura pedidos, itens, pagamentos e reviews; `customer_id`, `product_id` e `seller_id` ligam os itens às entidades**. Com esse mapa na cabeça, todo join da disciplina fica óbvio."

### 3. Mão na massa: carregando o schema raw (4:00 – 7:00)

**[TELA]** Editor + terminal.

> "Bora materializar. Vamos criar um script que monta o schema `raw` e carrega **as 9 tabelas** de uma vez — aproveitando o mesmo loop da aula passada, porque engenheiro bom é preguiçoso do jeito certo."

**[CÓDIGO]** Criar `ingestion/load_raw.py`:

```python
import duckdb, glob, os

con = duckdb.connect("olist.duckdb")
con.sql("CREATE SCHEMA IF NOT EXISTS raw")

for csv in sorted(glob.glob("data/raw/*.csv")):
    nome = (os.path.basename(csv)
            .replace("olist_", "")
            .replace("_dataset", "")
            .replace(".csv", ""))
    con.sql(f"CREATE OR REPLACE TABLE raw.{nome} AS "
            f"SELECT * FROM read_csv_auto('{csv}')")
    n = con.sql(f"SELECT COUNT(*) FROM raw.{nome}").fetchone()[0]
    print(f"raw.{nome:<40} {n:>10,} linhas")

con.close()
```

**[EXECUTAR]**

```bash
python ingestion/load_raw.py
```

**[CHECKPOINT]**

> "Olha o censo do Olist na tela: `raw.orders` com **99.441** linhas, `raw.order_items` com **112.650**, `raw.order_payments` com ~104 mil, `raw.customers` 99 mil, `raw.products` ~33 mil, `raw.sellers` só **3.095** — e o gigante `raw.geolocation` com **1 milhão** de linhas de CEP. Nove tabelas, um banco relacional local, carregado em segundos. E repara no `CREATE OR REPLACE`: rodou duas vezes, dá o mesmo resultado — isso se chama **idempotência**, e vai ser tema sério na Unidade 2."

### 4. Os primeiros joins reais (7:00 – 10:00)

**[TELA]** Terminal — as consultas e seus resultados.

> "E agora o momento que justifica tudo: **juntar** as tabelas. Pergunta de negócio número um: **faturamento por categoria de produto** — exige juntar itens, pedidos e produtos. Três tabelas, um SQL:"

**[CÓDIGO]** Criar `ingestion/consultas_aula3.sql` e rodar:

```sql
-- faturamento por categoria (3 tabelas)
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

```bash
python -c "
import duckdb
con = duckdb.connect('olist.duckdb')
print(con.sql(open('ingestion/consultas_aula3.sql').read()))"
```

**[CHECKPOINT]**

> "Olha o ranking na tela: **beleza e saúde, relógios e presentes, cama, mesa e banho** brigando no topo do faturamento — a distribuição realista que semeamos no gerador, espelhando o Olist verdadeiro. E o mais importante: esse join sobre **112 mil itens** rodou em **frações de segundo**, no Codespace gratuito. Segunda pergunta, ao vivo: **pedidos por estado** — `orders` com `customers`:"

**[CÓDIGO]**

```bash
python -c "
import duckdb
con = duckdb.connect('olist.duckdb')
print(con.sql('''
    SELECT c.customer_state AS uf, COUNT(*) AS pedidos
    FROM raw.orders o
    JOIN raw.customers c USING (customer_id)
    GROUP BY uf ORDER BY pedidos DESC LIMIT 5
'''))"
```

**[CHECKPOINT]**

> "**SP disparado na frente** — mais de 40% dos pedidos — seguido de RJ e MG. O e-commerce brasileiro desenhado num `GROUP BY`. Esses dois joins que acabamos de rodar são, conceitualmente, o coração do que o dbt vai automatizar e testar nas próximas unidades. Você já sabe fazer na mão; falta industrializar."

### 5. ACID: por que a fonte é confiável (10:00 – 12:00)

**[TELA]** Slide: tabela ACID com exemplos Olist.

> "Agora, um passo atrás conceitual: o que torna o banco relacional confiável para **operar** um marketplace? O conjunto **ACID**. **A de Atomicidade**: tudo ou nada — no Olist, pedido e pagamento gravam **juntos** ou nada grava; não pode existir pedido pago sem registro de pagamento. **C de Consistência**: o banco só transita entre estados válidos — item sempre aponta para um pedido existente. **I de Isolamento**: duas compras simultâneas não se misturam. **D de Durabilidade**: o pedido confirmado sobrevive a queda de energia. É por isso que a operação de qualquer marketplace roda sobre banco ACID — e é dessa fonte confiável que os nossos 9 CSVs nasceriam, num sistema real."

### 6. NoSQL e o teorema CAP no Olist (12:00 – 15:00)

**[TELA]** Slide: as 4 famílias NoSQL + CP × AP.

> "E o **NoSQL** — *Not Only SQL*: a família de bancos que abre mão de parte da rigidez relacional em troca de **escala, flexibilidade ou velocidade**. Quatro famílias, cada uma com um lugar natural no Olist. **Chave-valor** — Redis, DynamoDB: pares chave-valor ultrarrápidos; no Olist, o **carrinho de compras** ativo antes de virar pedido. **Documento** — MongoDB: JSONs flexíveis; no Olist, as **avaliações**, com campos opcionais e texto livre, casariam perfeitamente. **Coluna larga** — Cassandra: escrita massiva; no Olist, o **stream de cliques** do app. E **grafo** — Neo4j: relações; no Olist, a rede 'cliente comprou de vendedor' para recomendação. A lição: não existe NoSQL 'melhor que' SQL — numa arquitetura real, eles **convivem**, cada um no seu padrão de acesso."

> "E quando o banco é **distribuído**, entra o **teorema CAP**: na presença de uma **partição de rede** — e partições são inevitáveis — você garante só uma entre **Consistência** e **Disponibilidade**. A escolha real é **CP ou AP**. Pensa na Black Friday do Olist: o **pagamento** é CP — não pode cobrar errado nunca, melhor ficar indisponível um instante que inconsistente. A **contagem de visualizações** de um produto é AP — se atrasar uns segundos, ninguém morre. E o número que aterrissa isso: o Olist tem 99 mil pedidos em dois anos — média de 135 por dia. Mas num pico de Black Friday com **5 mil pedidos por minuto**, são uns **83 por segundo** — carga que um banco relacional ACID aguenta tranquilamente numa instância só. Agora os **cliques**: se cada pedido veio de 50 visualizações, são **4 mil e tantos eventos por segundo** — aí sim o Cassandra entra. Moral: **o padrão de acesso decide, não a moda**."

### 7. Pausa para reflexão + commit (15:00 – 16:30)

**[TELA]** O desafio CP × AP.

> "**Pausa para reflexão**, para você resolver depois da aula: escolhe **três operações** do marketplace — criar pedido, atualizar status de entrega, registrar avaliação, contar visualizações, atualizar estoque — e classifica cada uma como **CP ou AP**, justificando pela pergunta de negócio: o que é pior **nesta** operação — mostrar dado errado por um instante, ou ficar fora do ar? Não existe resposta única; existe justificativa boa."

**[CÓDIGO]**

```bash
git add ingestion/load_raw.py ingestion/consultas_aula3.sql
git commit -m "feat(ingestion): schema raw com 9 tabelas + joins de faturamento e UF"
git push
```

### 8. Atividade + encerramento e gancho (16:30 – 17:30)

> "Sua missão: carregar o schema `raw` completo, rodar o join de faturamento e anotar as **3 categorias campeãs**; rodar o join de pedidos por UF e confirmar a liderança de SP; e, para cada família NoSQL, apontar **um uso no Olist** com justificativa de uma frase. Tudo no seu Codespace, tudo commitado."

> "E na próxima aula, o último degrau dos fundamentos: **modelagem dimensional**. Rodar join de quatro tabelas a cada pergunta é lento e repetitivo — existe um jeito melhor: o **star schema**. Vamos desenhar e **construir ao vivo** a fato `fct_order_items` do Olist, entender OLTP versus OLAP, e ver o que acontece quando um vendedor muda de cidade — o famoso SCD Tipo 2. Te espero na Aula 4. Um abraço!"

---

## Roteiro da Videoaula 4 — "Modelagem dimensional: construindo a estrela do Olist"

**Duração-alvo:** 16 a 18 minutos.

### 1. Abertura (0:00 – 1:15)

**[TELA]** Slide de capa; Codespace ao lado.

> "Olá! Bem-vindo, bem-vinda à última aula dos fundamentos. Na Aula 3, o Olist ganhou um banco relacional e rodamos joins de três tabelas. Funciona — mas pensa na rotina de um time de dados: **toda pergunta** exigindo juntar três, quatro tabelas, todo dia, toda hora? Lento, repetitivo e sujeito a erro. Existe um jeito melhor de organizar o dado **para análise**, inventado por Ralph Kimball e padrão de data warehouse até hoje: a **modelagem dimensional**. Hoje você entende OLTP versus OLAP e — claro, mão na massa — **constrói a estrela do Olist ao vivo**: a fato `fct_order_items` no centro, as dimensões em volta. E ainda resolve o enigma do vendedor que muda de cidade. Bora."

### 2. OLTP × OLAP (1:15 – 3:30)

**[TELA]** Tabela comparativa OLTP × OLAP.

> "Dois propósitos opostos para um banco. **OLTP** — *transacional*: **operar** o negócio. Registrar o pedido 1234, atualizar um status — inserções e updates de **um registro por vez**, milhares de vezes por dia. É o mundo das 9 tabelas **normalizadas** do Olist, rodando em PostgreSQL ou MySQL na produção do marketplace. **OLAP** — *analítico*: **analisar** o negócio. Faturamento por categoria no ano — **agregações sobre milhões de linhas**. Modelagem dimensional, motores como DuckDB, BigQuery, Snowflake."

> "E a regra de ouro da casa: **você não roda relatório pesado no banco OLTP de produção** — o `GROUP BY` gigante do analista disputaria recursos com o cliente tentando fechar o carrinho. A solução universal: **copiar** o dado da forma OLTP para uma forma OLAP, onde a análise roda à vontade. Construir e manter essa cópia **é o trabalho do engenheiro de dados** — é literalmente o nosso pipeline. E a forma OLAP tem um desenho ótimo: a estrela."

### 3. Normalizar × desnormalizar e a estrela (3:30 – 5:45)

**[TELA]** Slide: estrela do Olist — fato central + 4 dimensões.

> "No OLTP, **normaliza-se**: cada coisa num só lugar, zero redundância — a cidade do vendedor mora numa única linha. Ótimo para escrever. No OLAP, fazemos o **oposto**: **desnormalizamos** — pré-juntamos os dados em poucas tabelas largas, aceitando redundância em troca de **velocidade de consulta**. É uma troca consciente: armazenamento é barato; o tempo do analista, não."

> "E o desenho canônico é o **esquema estrela**: uma **tabela fato** central — os eventos mensuráveis do negócio — cercada de **dimensões** — os contextos pelos quais se analisa. Existe o primo **floco de neve**, com dimensões normalizadas em subtabelas — economiza uns bytes, custa joins; nós vamos de **estrela**, simplicidade acima de tudo. A estrela do Olist: no centro, a fato **`fct_order_items`** — **grão: um item de pedido**, a granularidade mais fina, de onde tudo se agrega — com as métricas **`price`** e **`freight_value`**. Em volta: **`dim_customers`** — cidade, UF; **`dim_products`** — categoria, peso; **`dim_sellers`** — cidade, UF; e **`dim_dates`** — o calendário derivado do timestamp da compra. Pergunta analítica típica: 'some o `price` da fato, agrupando por categoria da `dim_products` e mês da `dim_dates`'. Um join leve, em vez de quatro."

### 4. Mão na massa: construindo a fato ao vivo (5:45 – 9:15)

**[TELA]** Editor + terminal.

**[CÓDIGO]** Criar `ingestion/build_star.py`:

```python
import duckdb

con = duckdb.connect("olist.duckdb")

# fato no grao de item de pedido: desnormaliza itens + pedidos
con.sql("""
CREATE OR REPLACE TABLE fct_order_items AS
SELECT i.order_id,
       i.product_id,
       i.seller_id,
       o.customer_id,
       CAST(o.order_purchase_timestamp AS DATE) AS date_key,
       i.price,
       i.freight_value
FROM raw.order_items i
JOIN raw.orders o USING (order_id)
""")

print(con.sql("SELECT COUNT(*) AS linhas_fato FROM fct_order_items"))
print(con.sql("SELECT ROUND(AVG(price), 2) AS ticket_medio_item FROM fct_order_items"))
con.close()
```

**[EXECUTAR]**

```bash
python ingestion/build_star.py
```

**[CHECKPOINT]**

> "Dois números para conferir comigo. Linhas da fato: **112.650** — exatamente o número de itens do Olist; o grão bateu, uma linha por item, como projetado. E o **ticket médio do item: por volta de 120 reais** — o preço médio que semeamos no gerador, espelhando o marketplace real. Quando o grão da fato bate com a contagem da origem, a modelagem está honesta — essa conferência simples evita as duplicações de join que assombram iniciante."

> "E agora prova o valor da estrela — a consulta analítica que antes precisava de três joins, agora com **um**:"

**[CÓDIGO]**

```bash
python -c "
import duckdb
con = duckdb.connect('olist.duckdb')
print(con.sql('''
    SELECT strftime(date_key, '%Y-%m') AS mes,
           ROUND(SUM(price), 2)        AS faturamento
    FROM fct_order_items
    GROUP BY mes ORDER BY mes DESC LIMIT 6
'''))"
```

**[CHECKPOINT]**

> "Faturamento mês a mês, direto da fato, **sem join nenhum** — porque a data já mora nela como `date_key`. Está aí a modelagem dimensional entregando o que promete: a pergunta do negócio virou um `GROUP BY` trivial."

### 5. SCD: o vendedor que mudou de cidade (9:15 – 12:15)

**[TELA]** Slide: tabela dos tipos de SCD + linha do tempo do seller_123.

> "E agora o enigma clássico das dimensões: **atributos mudam**. Imagina que o vendedor `seller_123` do Olist **muda de São Paulo para Campinas**. Como registrar isso na `dim_sellers` sem corromper a história? As opções têm nome: **Slowly Changing Dimensions** — SCD. **Tipo 0**: nunca muda — para atributos imutáveis. **Tipo 1**: **sobrescreve** — simples, mas perigoso: todas as vendas antigas passam a 'mentir' que saíram de Campinas; o relatório histórico de vendas por cidade **reescreve o passado**. **Tipo 3**: guarda só o valor anterior numa coluna — história rasa, de um passo."

> "E o **Tipo 2** — o que importa: em vez de sobrescrever, **cria-se uma nova linha**. A linha antiga é **fechada** com data de fim; a nova nasce com data de início e um marcador de 'linha atual'. Resultado: a venda feita em 2017, quando ele estava em São Paulo, **continua atribuída a São Paulo** — para sempre. A dimensão vira um **histórico versionado** do vendedor. Sem SCD Tipo 2, o relatório 'vendas por cidade do vendedor' fica retroativamente errado a cada mudança — e ninguém percebe, que é o pior tipo de erro. E o spoiler bom: não vamos implementar isso na mão — o **dbt tem o `snapshot`**, que faz SCD Tipo 2 automaticamente, e é exatamente o que faremos na Aula 9."

### 6. O exemplo numérico: da fato de 9 MB à escala Amazon (12:15 – 14:15)

**[TELA]** Slide com a conta de escala.

> "E para calibrar a noção de escala: quanto pesa a nossa fato? 112.650 linhas vezes uns 80 bytes por linha… **cerca de 9 megabytes**. Nove! O Olist inteiro analítico cabe dentro da memória de qualquer laptop — por isso o DuckDB responde em milissegundos. Agora projeta: o Olist na escala da **Amazon**, mil vezes maior — 113 milhões de itens: **9 gigabytes** de fato. Ainda tratável. Um milhão de vezes — alguns anos de um marketplace global: **bilhões de linhas, terabytes** de fato. É exatamente esse crescimento que justifica tudo o que estudamos: o **formato colunar** da Aula 2, e os bancos **OLAP distribuídos** — BigQuery, Snowflake — que vamos conhecer na Unidade 3. A arquitetura é a mesma da nossa; só o motor muda de tamanho. Quem aprende a estrela no DuckDB está pronto para o warehouse de qualquer empresa."

### 7. Commit + atividade (14:15 – 15:45)

**[CÓDIGO]**

```bash
git add ingestion/build_star.py
git commit -m "feat(model): primeira versao da fct_order_items (grao = item de pedido)"
git push
```

> "Commit — e olha o seu repositório ao fim da Unidade 1: devcontainer, gerador de dados, ingestão bronze, schema raw e a primeira fato. Quatro aulas, quatro commits, um pipeline nascendo — e **tudo reprodutível do zero, sem uma única conta externa**. Sua missão: desenhar **no papel** a estrela do Olist com chaves e métricas — desenhar fixa; rodar o `build_star.py` e conferir os **112.650**; escrever a consulta do **ticket médio** e confirmar os ~120 reais; e explicar em duas frases por que o Tipo 2 preserva a história e o Tipo 1 a destrói."

### 8. Encerramento da unidade + gancho (15:45 – 17:00)

**[TELA]** Slide de fechamento + teaser da U2.

> "E com isso fechamos a Unidade 1 — os fundamentos, todos com código rodando: o **papel** do engenheiro e o ciclo de vida; os **formatos** e a bronze em Parquet com compressão medida; o **relacional** com o schema raw e joins reais; e hoje a **modelagem dimensional** com a estrela materializada. Seu Codespace já é um mini data warehouse."

> "E na Unidade 2, a coisa fica séria: entra o **dbt** — a ferramenta que transforma esses nossos scripts soltos em um projeto de transformação **versionado, testado e documentado**; entra o processamento **batch** e o **streaming** — vamos simular os pedidos do Olist como eventos JSON chegando em tempo real, e descobrir nos dados o minuto mais movimentado da história do marketplace; e entra a estrela da disciplina: o **Airflow**, que vai orquestrar o pipeline inteiro num DAG — direto no nosso Codespaces, com a interface web na porta 8080 que deixamos configurada lá na Aula 1. Nada foi por acaso. Te espero na Unidade 2. Um abraço!"
