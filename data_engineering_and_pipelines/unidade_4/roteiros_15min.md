# Roteiros Estendidos Hands-on (15–20 minutos) — Unidade 4: Qualidade, Governança e DataOps

- **Disciplina:** Data Engineering and Pipelines
- **Conteudista:** Afonso Cesar Lelis Brandão
- **Videoaulas:** 13 a 16
- **Formato:** roteiro de gravação **hands-on em GitHub Codespaces** — fala em citação (>), código executado na demonstração. Duração-alvo: **15 a 20 minutos** por aula.

> **Convenções:** **[TELA]** slide/Codespace · **[CÓDIGO]** digitar/colar · **[EXECUTAR]** rodar e mostrar saída · **[CHECKPOINT]** resultado esperado.
> **Preparação da unidade:** Codespace com as Unidades 1–3 concluídas. Antes de gravar, execute `pip install "great_expectations==1.8.0" "scikit-learn==1.7.1"`. As versões são fixadas porque a API do Great Expectations varia entre lançamentos. Nenhuma aula exige conta ou chave de API; o CI da Aula 15 é executado pelo GitHub Actions.

---

## Roteiro da Videoaula 13 — "Qualidade e observabilidade: validação do pipeline com dados inválidos"

**Duração-alvo:** 18 a 20 minutos.

### 1. Abertura (0:00 – 1:30)

**[TELA]** Slide de capa.

> "Nas três primeiras unidades, construímos a ingestão dos arquivos CSV, a modelagem dimensional, o DAG, as camadas do lakehouse e o dashboard. Nesta aula, acrescentaremos verificações que permitam avaliar se os dados publicados em `mart_sales_by_category` atendem aos critérios definidos. Serão utilizados testes do dbt e do Great Expectations. Um registro inválido será inserido de forma controlada para demonstrar a detecção, a correção e uma nova validação."

### 2. As 6 dimensões DAMA no Olist (1:30 – 4:00)

**[TELA]** Slide: as 6 dimensões instanciadas no Olist.

> "Primeiro, o vocabulário: qualidade de dados **não é achismo — é mensurável**, pelas seis dimensões do DAMA. Cada uma instanciada numa tabela real do nosso projeto. **Completude**: quantos pedidos não têm review? Milhares, no Olist. **Acurácia**: o dado reflete a realidade? Existe entrega com data **anterior** à compra? — fisicamente impossível, e vamos caçar isso hoje. **Consistência**: o pagamento somado por pedido bate com o total do fato? **Unicidade**: `order_id` é único no `stg_orders`? **Validade**: `review_score` está entre 1 e 5? O frete é sempre não-negativo? O `order_status` pertence ao conjunto conhecido? E **pontualidade**: o DAG rodou no horário e o gold está fresco para o dashboard das 8h?"

> "Cada dimensão vira **métrica numérica com limiar** acordado com o negócio. E uma verdade libertadora: **não existe 100% de qualidade — existe qualidade suficiente para a decisão**. O trabalho do engenheiro é saber qual é o suficiente, e medi-lo automaticamente."

### 3. Demonstração prática: dbt tests no schema.yml (4:00 – 7:00)

**[TELA]** Editor.

> "E a alternativa inicial de menor custo mora **ao lado do modelo**: os testes do dbt, declarados em YAML. Quatro tipos genéricos que resolvem 80% dos casos:"

**[CÓDIGO]** Criar `dbt_olist/models/marts/core/schema.yml`:

```yaml
version: 2
models:
  - name: fct_order_items
    columns:
      - name: order_id
        tests: [not_null]
      - name: product_id
        tests:
          - not_null
          - relationships:
              to: ref('dim_products')
              field: product_id
  - name: stg_orders
    columns:
      - name: order_id
        tests: [unique, not_null]
      - name: order_status
        tests:
          - accepted_values:
              values: ['delivered','shipped','canceled','invoiced',
                       'processing','approved','created','unavailable']
```

**[EXECUTAR]**

```bash
cd dbt_olist && dbt test
```

**[CHECKPOINT]**

> "Observe o log: seis testes, seis **PASS**. A leitura mostra o que acabamos de garantir, sem custo adicional de licenciamento: `order_id` **nunca nulo** e **único** — unicidade; todo `product_id` do fato **existe** na `dim_products` — o `relationships`, a integridade referencial fato-dimensão; e `order_status` só assume os **oito valores conhecidos** — o `accepted_values`. Meia página de YAML, e o pipeline ganhou um porteiro. E lembra da Aula 8: o `dbt test` já tem **vaga reservada no DAG** — a task que passava vazia acabou de ganhar dentes: agora, se um teste falhar, o `olist_pipeline` **para antes de publicar o gold**."

### 4. Teste controlado com um registro inválido (7:00 – 11:00)

**[TELA]** Terminal — o experimento central da aula.

> "E agora, o experimento. Vou fazer o papel do **bug**: injetar na fonte um pedido com um status que não existe — simulando aquele deploy do sistema transacional que criou um status novo sem avisar o time de dados. Acontece **toda semana** no mundo real:"

**[CÓDIGO]** Inserir um registro inválido na fonte:

```bash
python -c "
import duckdb
con = duckdb.connect('../olist.duckdb')
con.sql(\"\"\"
INSERT INTO raw.orders VALUES
('pedido_sabotado_001', 'cliente_fake', 'status_hackeado',
 now(), now(), now(), now(), now())
\"\"\")
print('sabotagem concluida: 1 pedido com status invalido na fonte')"
```

**[EXECUTAR]** Rodar o pipeline como o Airflow rodaria:

```bash
dbt run --select stg_orders
dbt test --select stg_orders
```

**[CHECKPOINT]**

> "Acompanhe a sequência. O `dbt run` **aceitou** o pedido — a carga incremental viu um timestamp novo e o trouxe; ingestão não julga, ingere. Mas o `dbt test`. **FAIL!** Observe na tela: `accepted_values_stg_orders_order_status — Got 1 result` — o teste encontrou **exatamente 1 linha** com status fora da lista. O lixo entrou no staging, mas **não passa dali**: no DAG, essa falha bloqueia o `export_gold` — o dashboard das 8h **nunca vê** o registro inválido. Isso é a rede de proteção funcionando: a falha foi **detectada em segundos, automaticamente**, no lugar certo. Sem esse teste? O status inválido escorreria até o mart, o KPI da diretoria sairia errado, e alguém descobriria semanas depois — talvez o cliente. Agora vamos remover o registro de teste:"

**[CÓDIGO]** Reverter:

```bash
python -c "
import duckdb
duckdb.connect('../olist.duckdb').sql(
  \"delete from raw.orders where order_id = 'pedido_sabotado_001'\")
print('fonte limpa')"
dbt run --select stg_orders --full-refresh
dbt test --select stg_orders
```

> "Deletei da fonte, `--full-refresh` no staging para reconstruir do zero, testes. **verdes de novo**. Ciclo completo: teste controlado, detecção automática, correção, verificação. Você acabou de operar um incidente de qualidade de dados — em ambiente seguro."

### 5. Great Expectations: as regras de negócio (11:00 – 14:00)

**[TELA]** Editor + terminal.

> "O dbt cobre estrutura. Para **regras ricas de negócio** — faixas, comparações entre colunas — entra o **Great Expectations**, que ainda gera documentação de auditoria. As três expectations que todo pipeline Olist merece: review entre 1 e 5; **entrega nunca antes da compra**; frete não-negativo. Vamos rodar sobre os dados reais:"

**[CÓDIGO]** Criar `quality/expectations_olist.py`:

```python
import duckdb
import great_expectations as gx

con = duckdb.connect("olist.duckdb")
df = con.sql("""
    select o.order_purchase_timestamp, o.order_delivered_customer_date,
           r.review_score, i.freight_value
    from raw.orders o
    left join raw.order_reviews r using (order_id)
    left join raw.order_items   i using (order_id)
""").df()

context = gx.get_context()
batch = context.data_sources.pandas_default.read_dataframe(df)

r1 = batch.expect_column_values_to_be_between(
        column="review_score", min_value=1, max_value=5)
r2 = batch.expect_column_pair_values_a_to_be_greater_than_b(
        column_A="order_delivered_customer_date",
        column_B="order_purchase_timestamp", or_equal=True)
r3 = batch.expect_column_values_to_be_between(
        column="freight_value", min_value=0)

for nome, r in [("review 1-5", r1), ("entrega >= compra", r2), ("frete >= 0", r3)]:
    print(f"{nome}: success={r.success}  "
          f"unexpected={r.result.get('unexpected_count', 0)}")
con.close()
```

**[EXECUTAR]**

```bash
cd .. && python quality/expectations_olist.py
```

**[CHECKPOINT]**

> "observe os resultados sobre os nossos dados: review entre 1 e 5 — passa. Frete não-negativo — passa. E a comparação de datas. Observe no `unexpected_count`: **18**! Dezoito registros com **entrega registrada antes da compra** — fisicamente impossível, o erro de acurácia clássico. E agora eu pago uma promessa antiga: lembra, lá na **Aula 1**, daquelas linhas misteriosas do `gerar_dados.py` marcadas com '18 defeitos plantados'? **Eram exatamente estes.** O gerador reproduziu, de propósito, o tipo de defeito que existe no dataset real do Olist e em toda fonte de dados do mundo — digitação, bug de sistema, fuso trocado — e o Great Expectations acabou de **caçá-los automaticamente** no meio de 99 mil pedidos. Quinze aulas de convivência com esses dados e você nunca os viu; três expectations, e eles apareceram. E a diferença conceitual para fechar: **teste pega o que você previu; observabilidade pega o que você não previu** — se o volume diário de pedidos despencar de 135 para 12, nenhum `not_null` acusa, mas um monitor de volume e frescor, sim. Testes mais observabilidade: as duas metades da confiança."

### 6. A regra 1-10-100 (14:00 – 15:30)

**[TELA]** Slide com a conta.

> "E quanto vale isso em dinheiro? A **regra 1-10-100**: custa **1 real prevenir** o defeito — escrever o teste; **10 corrigi-lo** no pipeline; **100 conviver** com ele em produção. Nos nossos 18 registros de 'entrega antes da compra': prevenir custou o teste que escrevemos — **18 reais**, na metáfora. Conviver — deixar os 18 vazarem para o `mart_delivery_performance` e contaminarem o KPI de prazo que a diretoria apresentou — custa **1.800**: cem vezes mais, em refação, retratação e confiança perdida. E o melhor: a expectation escrita **uma vez** barra o defeito em **todo run futuro** do DAG. Moral gravada: **automatize a verificação onde o dado é produzido, não onde é consumido.**"

### 7. Commit + atividade e preparação para a próxima aula (15:30 – 17:30)

**[CÓDIGO]**

```bash
git add dbt_olist quality/
git commit -m "feat(quality): dbt tests no schema.yml + expectations GE sobre o Olist"
git push
```

> "A atividade proposta: escrever uma regra mensurável para **cada** dimensão DAMA sobre tabelas reais do Olist; implementar os três testes dbt e rodar a teste controlado no seu Codespace — quebrar de propósito ensina mais que dez leituras; rodar as duas expectations e anotar o `unexpected_count` das datas; e estimar o **TTD** — se o frete viesse negativo hoje, em quanto tempo alguém perceberia **sem** os testes?"

> "E na próxima aula, subimos da qualidade para a **lei**: dado certo também precisa ser dado **governado**. E o Olist guarda um presente didático raro: ele **já vem pseudonimizado** — IDs em hash, localização por prefixo de CEP. É um caso real de **LGPD** aplicada, e vamos dissecá-lo: mascaramento, RBAC, e o lineage do dbt virando a planta baixa do direito de exclusão."

---

## Roteiro da Videoaula 14 — "Governança e LGPD: o Olist como caso real de pseudonimização"

**Duração-alvo:** 16 a 18 minutos.

### 1. Abertura (0:00 – 1:15)

**[TELA]** Slide de capa.

> "Na aula anterior, foram definidos controles de qualidade. Nesta aula, trataremos de governança: responsabilidade pelos dados, controle de acesso, origem, retenção e conformidade. O conjunto Olist não contém nomes ou CPF e emprega identificadores substitutos e prefixos de CEP. Essas características permitem discutir pseudonimização, generalização geográfica, mascaramento, controle de acesso baseado em papéis e linhagem de dados no contexto da LGPD."

### 2. Governança: papéis e distinções fundamentais (1:15 – 4:15)

**[TELA]** Slide: owner/steward/custodian + anonimizado × pseudonimizado.

> "**Governança de dados** é o conjunto de políticas, papéis e processos que responde: quem é **dono** de cada dado? Quem **acessa** o quê? O que é **sensível**? Quanto tempo **guardamos**? Como **provamos** conformidade a um auditor? E mesmo no Olist anonimizado, os três papéis clássicos existem: o **data owner** — o responsável de negócio por cada domínio: vendas, logística, reviews; o **data steward** — quem zela pelo **significado** dos campos: qual a diferença entre `customer_id` e `customer_unique_id`? — pergunta que o steward responde; e o **data custodian** — o time que opera o DuckDB, o dbt e o Airflow: nós. Sem dono, ninguém responde pelo dado — e dado sem dono apodrece."

> "É necessário distinguir anonimização de pseudonimização. A LGPD define dado anonimizado em função do uso de meios técnicos razoáveis e disponíveis no momento do tratamento, e não como uma garantia abstrata de impossibilidade absoluta. Na pseudonimização, informações adicionais mantidas separadamente ainda permitem associar o dado a uma pessoa. No conjunto Olist, o `customer_unique_id` permite relacionar compras atribuídas ao mesmo identificador e, por isso, deve ser tratado com cautela; sem documentação do processo de publicação, não se deve afirmar que ele seja um hash irreversível. O prefixo de CEP constitui uma redução de granularidade geográfica. A classificação dos campos deve considerar a possibilidade de associação e reidentificação no contexto concreto."

### 3. Demonstração prática: mascaramento e RBAC (4:15 – 7:30)

**[TELA]** Editor + terminal.

> "Mesmo sobre dado já pseudonimizado, aplicamos **defesa em profundidade** — camadas de proteção redundantes. Camada um: o **mascaramento**. Quando o analista não precisa do prefixo de CEP completo, entregamos menos:"

**[CÓDIGO]** Rodar o mascaramento na demonstração:

```bash
python -c "
import duckdb
con = duckdb.connect('olist.duckdb')
print(con.sql(\"\"\"
    select customer_id,
           customer_zip_code_prefix                                as zip_original,
           left(customer_zip_code_prefix::varchar, 3) || 'XX'      as zip_masked,
           customer_state
    from raw.customers limit 5
\"\"\"))"
```

**[CHECKPOINT]**

> "Compare os valores antes e depois: `14409` virou `144XX`. O analista de marketing continua sabendo a **região** — que é o que ele precisa para o estudo — mas perdeu dois dígitos de granularidade de localização. Privacidade não é tudo-ou-nada: é **dosagem** — cada consumidor recebe a granularidade mínima suficiente. Em produção, esse mascaramento viraria um modelo dbt — a versão mascarada do staging — servida por padrão, com o valor cheio restrito."

> "Restrito a quem? Camada dois: o **RBAC** — *Role-Based Access Control*: permissões por **papel**, nunca por pessoa, sob o princípio do **menor privilégio**. No Olist: o papel *analista de marketing* enxerga só os marts agregados; o *cientista de dados* enxerga o gold, para treinar modelo; e **somente** o *custodian* — o engenheiro — toca o schema `raw`. Complementos: *column-level security* — a coluna sensível sumindo para quem não deve vê-la; *row-level* — o analista regional de SP vendo só linhas de SP; e **criptografia** em repouso e em trânsito, o pano de fundo de tudo."

### 4. Lineage como instrumento jurídico: o direito de exclusão (7:30 – 10:30)

**[TELA]** Navegador — dbt docs, lineage do customer_unique_id.

> "E agora uma relação importante da unidade — onde uma ferramenta de engenharia vira instrumento jurídico. A LGPD, fiscalizada pela **ANPD**, garante ao titular o **direito de eliminação**: 'apaguem os meus dados'. Pergunta de engenheiro: para apagar **todos** os rastros de um `customer_unique_id`. Você precisa saber **todos os lugares onde ele pousou**. E quem sabe disso, no nosso projeto? Abre comigo o `dbt docs` que geramos na Aula 12:"

**[EXECUTAR]** (com o `dbt docs serve` no ar)

```bash
cd dbt_olist && dbt docs generate && dbt docs serve --port 8081
```

> "No lineage graph, sigo o `customer_unique_id`: ele nasce em **`raw.customers`**, flui para **`stg_customers`**, entra na **`dim_customers`**, é referenciado pela **`fct_order_items`** via `customer_id`, e desagua nos marts. **Este grafo é a planta baixa do processo de exclusão**: chegou um pedido da ANPD? A lista de tabelas a limpar está desenhada — gerada automaticamente dos `ref()` que escrevemos desde a Aula 5. E o lineage responde as duas perguntas opostas da governança: *a jusante* — 'se eu remover este titular, quais marts mudam?' — o impacto; e *a montante* — 'este número estranho no dashboard, de onde saiu?' — a causa-raiz. Em escala de empresa, essa função vira um **catálogo de dados** dedicado — o **DataHub**, open source, ou o **Atlan** — centralizando metadados, dicionário e linhagem de todos os times. Mas o princípio você já domina, porque ele mora no seu projeto."

### 5. Minimização, base legal, retenção — e a conta do vazamento (10:30 – 13:30)

**[TELA]** Slide: os 3 princípios + a conta do vazamento.

> "Três princípios práticos da LGPD que o pipeline materializa. **Minimização**: só ingira o necessário — o Olist já removeu nomes na origem; dado que você não coleta é dado que não vaza. **Base legal**: todo tratamento precisa apoiar-se numa das dez bases da lei — execução de contrato, legítimo interesse, consentimento. 'porque é útil' **não** é base legal. E **retenção**: toda tabela com dado pessoal precisa de prazo de guarda — dado que você não guarda além do prazo é risco que expira sozinho. Observe na tese da aula: **quem materializa a lei é a engenharia** — classificar no catálogo, mascarar por padrão, registrar lineage, automatizar exclusão são tarefas do pipeline, não do departamento jurídico."

> "E quanto custa errar? A conta, num marketplace como o Olist com faturamento de 80 milhões, **sem** a pseudonimização que o dataset já traz, sofrendo um vazamento: **multa LGPD** — até 2% do faturamento, teto de 50 milhões por infração: **1,6 milhão**. **Notificação e remediação** dos 96 mil clientes únicos, a 9 reais por titular: **865 mil**. **Churn** pós-vazamento — 3% de evasão a 220 reais por cliente-ano: **634 mil**. Total no primeiro ano: **cerca de 3,1 milhões de reais**. E a prevenção — mascaramento, RBAC, auditoria de lineage? Uns **60 mil**. A multa sozinha paga a prevenção **27 vezes**. E observe a sutileza final: a multa é a **menor** das parcelas — reputação e churn doem mais e duram anos. O Olist fez, na origem, a coisa mais barata e poderosa que existe: **pseudonimizou antes de publicar**. Privacidade por design não é slogan — é a engenharia que você está vendo."

### 6. Commit + atividade e preparação para a próxima aula (13:30 – 16:00)

**[CÓDIGO]**

```bash
cd .. && git add -A
git commit -m "docs(lgpd): mascaramento de zip e analise de pseudonimizacao do Olist"
git push
```

> "A atividade proposta: **classificar** os campos de `customers`, `orders` e `reviews` em público, interno, confidencial e pessoal/pseudonimizado; escrever o SQL de **mascaramento** do CEP e dizer qual papel RBAC veria o valor cheio; gerar o **lineage** e listar todos os modelos tocados pelo `customer_unique_id` — o caminho de exclusão; e escrever uma política de **retenção** de uma frase para duas tabelas."

> "E na próxima aula, a pergunta que fecha o ciclo de maturidade: seu pipeline é confiável e governado. Mas você consegue **mudá-lo sem medo**? Se um colega abrir um pull request mexendo no `fct_order_items` numa sexta às 17h, você faz merge tranquilo? Vamos curar esse medo com **DataOps**: o GitHub Actions rodando `dbt build` a cada PR — no mesmo GitHub onde o nosso projeto mora desde a Aula 1. CI/CD de dados, na demonstração."

---

## Roteiro da Videoaula 15 — "DataOps e CI/CD: dbt build em cada pull request"

**Duração-alvo:** 17 a 19 minutos.

### 1. Abertura (0:00 – 1:30)

**[TELA]** Slide de capa.

> "Seu pipeline Olist já é **confiável** — Aula 13 — e **governado** — Aula 14. Falta o último ingrediente da operação profissional: a capacidade de **mudar o pipeline com segurança e frequência**, com menor risco operacional. E eu te faço a pergunta-teste, de forma objetiva: se um colega abrisse um pull request alterando o `fct_order_items` às **cinco da tarde de uma sexta-feira**. Você daria merge sem medo? Se a resposta é 'de jeito nenhum' — e ela é —, você tem um problema de **processo**, não de coragem. E esse risco pode ser reduzido com: **DataOps**. Hoje colocamos o **GitHub Actions** para rodar `dbt build` a cada pull request do nosso repositório — e vamos assistir o robô barrar um erro **antes** de ele chegar em produção."

### 2. DataOps: os pilares no repo Olist (1:30 – 3:45)

**[TELA]** Slide: pilares DataOps + o que vai/não vai pro Git.

> "**DataOps** é a importação das práticas de DevOps — Git, automação, testes, integração contínua — para o mundo dos dados. Os pilares, traduzidos no nosso projeto: **automação ponta a ponta** — do `git push` ao `dbt build`, zero passo manual; **testes de código E de dado** — o CI roda a lógica dos modelos e os mesmos `dbt test` da Aula 13; **colaboração** — todo o `pipeline-olist` num repo com branches e pull requests, como fazemos desde a Aula 1; e **iteração rápida** — mudanças pequenas e frequentes. A métrica-norte vem do estudo **DORA**, o mesmo do DevOps de elite: **frequência de deploy alta com taxa de falha baixa**. Não é escolher entre velocidade e segurança — é ter as duas, porque uma alimenta a outra."

> "E a fronteira do que se versiona, que já praticamos: **vão para o Git** os modelos, os `schema.yml` com testes, o DAG do Airflow, as expectations — o **código**. **Não vão**: o `olist.duckdb` e os Parquet do gold — isso é **dado**, e mora no `.gitignore` desde a Aula 1. Para versionar dado existem ferramentas próprias — DVC, lakeFS, o time travel do Delta —; no projeto, versionamos o código que **gera** o dado, que é o que importa: dado se regenera do cru; código perdido, não."

### 3. Demonstração prática: a fixture de CI e o workflow (3:45 – 8:00)

**[TELA]** Editor + terminal.

> "Agora a parte central da aula. O plano: a cada pull request, o GitHub Actions vai montar um ambiente **do zero**, carregar uma **amostra** dos dados, rodar `dbt build` — que é `run` mais `test` em uma única execução — e **bloquear o merge se qualquer coisa falhar**. Primeiro problema a resolver: o runner do Actions não tem os 120 MB do Olist — os dados não estão no Git, conforme a prática adotada no projeto. A solução profissional: uma **fixture** — uma amostra pequena, committada, só para o CI exercitar a lógica:"

**[CÓDIGO]** Criar `ingestion/make_sample.py`, gerar e versionar a amostra:

```python
import duckdb, glob, os

con = duckdb.connect("olist.duckdb")
os.makedirs("data/sample", exist_ok=True)
for csv in sorted(glob.glob("data/raw/*.csv")):
    nome = os.path.basename(csv)
    con.sql(f"COPY (SELECT * FROM read_csv_auto('{csv}') LIMIT 2000) "
            f"TO 'data/sample/{nome}' (HEADER)")
    print(f"sample ok: {nome}")
```

```bash
python ingestion/make_sample.py
# liberar data/sample no .gitignore:
printf '!data/sample/\n' >> .gitignore
```

**[CÓDIGO]** Parametrizar o `ingestion/load_raw.py` (pasta e banco como argumentos):

```python
import duckdb, glob, os, sys

raw_dir = sys.argv[1] if len(sys.argv) > 1 else "data/raw"
db_path = sys.argv[2] if len(sys.argv) > 2 else "olist.duckdb"

con = duckdb.connect(db_path)
con.sql("CREATE SCHEMA IF NOT EXISTS raw")
for csv in sorted(glob.glob(f"{raw_dir}/*.csv")):
    nome = (os.path.basename(csv).replace("olist_", "")
            .replace("_dataset", "").replace(".csv", ""))
    con.sql(f"CREATE OR REPLACE TABLE raw.{nome} AS "
            f"SELECT * FROM read_csv_auto('{csv}')")
print(f"raw carregado de {raw_dir} em {db_path}")
```

**[CÓDIGO]** E o workflow — `.github/workflows/dbt-ci.yml`:

```yaml
name: dbt CI (Olist)
on:
  pull_request:
    branches: [main]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.11" }
      - name: Instalar stack
        run: pip install duckdb dbt-duckdb
      - name: Carregar fixture no DuckDB de staging
        run: python ingestion/load_raw.py data/sample olist.duckdb
      - name: dbt build (run + test)
        working-directory: dbt_olist
        run: |
          dbt seed
          dbt build
```

> "Lê o workflow comigo, porque ele é o contrato da qualidade: dispara **em todo pull request** contra a main; sobe um Ubuntu limpo; instala só o essencial; carrega a **fixture** num DuckDB **descartável** — que nasce e morre dentro do runner, nunca o de produção; e roda `dbt build` — modelos e testes, tudo. Se **um** modelo quebrar ou **um** teste falhar, o check fica vermelho e o **merge é bloqueado**. O erro morre no PR — não em produção, não no dashboard da diretoria."

### 4. Validação do workflow em um pull request (8:00 – 12:00)

**[TELA]** Terminal → navegador (GitHub).

**[CÓDIGO]** Abrir um PR de verdade:

```bash
git checkout -b feat/ci-dataops
git add -A
git commit -m "feat(dataops): CI com dbt build em PR + fixture de amostra"
git push -u origin feat/ci-dataops
```

> "Push feito — agora no GitHub: **Compare & pull request**, abro o PR. E observe a aba de **checks**: o `dbt CI (Olist)` está **rodando sozinho**, disparado pelo PR. Acompanhe na aba Actions: checkout. Python. Fixture carregada. `dbt build`. E **verde**: 12 modelos construídos, testes passando, na amostra, num banco descartável. **Este PR está validado pelo conjunto de verificações automatizadas para merge** — não porque eu confio em mim, mas porque o robô verificou. Merge sem medo — numa sexta, se for preciso."

> "E o cenário oposto, que fica de exercício sabotador para você: edita o `stg_orders` na branch, remove uma coluna que o `fct_order_items` usa, push — e assiste ao check ficar **vermelho** e o merge travar. A quebra que, sem CI, você descobriria em produção às 6 da manhã, morre no PR às 17h05 da sexta. **Isso** é a redução do risco operacional."

### 5. WAP, dev→prod e IaC (12:00 – 14:15)

**[TELA]** Slide: write-audit-publish + targets + Terraform.

> "Três conceitos completam a operação. Um: a promoção **dev → produção** no dbt é trocar o **target** — mesmos modelos, banco diferente; exatamente o mecanismo do `profiles.yml` que montamos na Aula 11. Dois: o padrão **write-audit-publish** — WAP — a elegância operacional para dados: o pipeline **escreve** os marts numa área de auditoria, **audita** com `dbt test` e Great Expectations, e **só então publica** — promove para o schema de produção. O dashboard de vendas **nunca** enxerga um `mart_sales_by_category` intermediário quebrado: ou vê a versão anterior íntegra, ou a nova aprovada. Três: **IaC** — infraestrutura como código: quando o Olist for para a nuvem, o bucket do gold, o dataset do warehouse e até as **políticas de acesso da Aula 14** não nascem de cliques no console — nascem de **Terraform versionado, revisado em PR**. A governança inteira vira código auditável."

### 6. A conta do DORA + commit (14:15 – 16:00)

**[TELA]** Slide: antes × depois.

> "E o valor em números. **Antes**, no processo manual: 2 deploys por mês, 4 horas de engenheiro cada, 30% de taxa de falha — custo total na casa de **3.060 reais por mês**, e medo permanente. **Depois**, com o CI que acabamos de montar: **20 deploys por mês** — dez vezes mais —, meia hora de supervisão cada, falha caindo para **5%** porque o `dbt build` barra a maioria no PR — custo: **1.620 por mês**. Dez vezes mais entregas, pela metade do custo, com um sexto da taxa de falha. E a moral que resume o DataOps numa frase: **o segredo não é fazer menos deploy — é tornar o deploy barato e seguro a ponto de virar rotina.**"

**[CÓDIGO]** (após o merge do PR)

```bash
git checkout main && git pull
```

### 7. Atividade e preparação para a próxima aula (16:00 – 17:30)

> "A atividade proposta: montar o CI completo no seu repositório — fixture, workflow, PR aberto com check verde; fazer a **teste controlado inversa** — quebrar um modelo na branch e ver o merge travar; descrever os três passos do **write-audit-publish** para o `mart_sales_by_category`; e responder a pausa para reflexão: liste **três coisas** que tornavam o merge de sexta assustador no seu projeto — e a prática de DataOps que neutraliza cada uma."

> "E na próxima aula. A última da disciplina. A etapa de integração: fechar o ciclo **do dado à IA**. Vamos treinar um modelo de **machine learning** — um RandomForest do scikit-learn — lendo o gold do nosso DuckDB para **prever quais pedidos do Olist vão atrasar**. O dado que entrou como CSV cru na Aula 1 vai sair como **predição** na Aula 16. E costuramos as quatro unidades no diagrama que vira o seu portfólio."

---

## Roteiro da Videoaula 16 — "Do dado à IA: prevendo atrasos do Olist (projeto integrador)"

**Duração-alvo:** 18 a 20 minutos.

### 1. Abertura (0:00 – 1:30)

**[TELA]** Slide de capa.

> "Esta é a última aula de Data Engineering and Pipelines. O repositório desenvolvido ao longo da disciplina contém ingestão idempotente, modelagem dimensional, orquestração com Airflow, camadas Medallion, documentação, linhagem, dashboard, testes de qualidade e integração contínua. Nesta aula, utilizaremos os dados da camada gold para treinar um modelo de classificação de atrasos e relacionaremos o resultado às etapas construídas nas quatro unidades."

### 2. O engenheiro de dados na era da IA (1:30 – 3:30)

**[TELA]** Slide: IA sobre dados + as 3 frentes.

> "Primeiro, a leitura de cenário. A explosão da IA generativa **não** aposentou o engenheiro de dados — fez o oposto: **IA roda sobre dados**, e o modelo é exatamente tão bom quanto o pipeline que o alimenta. No nosso projeto isso é concreto e literal: o modelo de atraso que vamos treinar daqui a pouco **só existe** porque antes você garantiu datas acuradas — lembra das entregas antes da compra que o GE pegou? —, um gold confiável e um lineage auditável. *Garbage in, garbage out* deixou de ser ditado e virou lei de ML. E o papel se expande em três frentes: **provedor de dados para IA** — alimentando feature stores; **usuário de IA como ferramenta** — os copilots que geram SQL e dbt; e a fronteira: **extrair estrutura de texto com LLMs** — classificar o sentimento dos `review_comment_message` do Olist, aquele nosso campo não estruturado da Aula 2, seria o passo seguinte natural deste projeto."

### 3. Feature store: as features do Olist (3:30 – 5:30)

**[TELA]** Slide: training-serving skew + as features.

> "Antes do treino, um conceito de arquitetura de ML que todo engenheiro precisa ter: a **feature store**. O problema que ela resolve: o cientista calcula uma feature de um jeito no notebook, e a produção a recalcula de **outro** jeito — o *training-serving skew*: o modelo treina com uma realidade e opera em outra, e decai silenciosamente. A feature store — Feast, Tecton — serve **a mesma feature, com a mesma lógica**, para treino e produção. E as features naturais do nosso problema saem do gold: o **prazo estimado** — a diferença entre a data estimada de entrega e a compra; o **frete** — frete alto sugere distância e complexidade; o **número de parcelas**; o número de itens; a categoria; a UF. No nosso projeto local, a 'feature store' é honestamente uma view do dbt sobre o fato e as dimensões — e o conceito é **idêntico** ao da ferramenta gerenciada: definição única, consumo múltiplo."

### 4. Demonstração prática: treinando o modelo na demonstração (5:30 – 10:30)

**[TELA]** Editor + terminal.

**[CÓDIGO]** Criar `ml/train_delivery_delay.py`:

```python
import duckdb
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

con = duckdb.connect("olist.duckdb")
df = con.sql("""
    select
        datediff('day', o.order_purchase_timestamp,
                        o.order_estimated_delivery_date)          as prazo_estimado,
        pay.payment_installments,
        it.freight_value,
        (o.order_delivered_customer_date >
         o.order_estimated_delivery_date)::int                    as is_late
    from raw.orders o
    join (select order_id, max(payment_installments) as payment_installments
          from raw.order_payments group by 1) pay using (order_id)
    join (select order_id, sum(freight_value) as freight_value
          from raw.order_items group by 1) it using (order_id)
    where o.order_delivered_customer_date is not null
""").df()
con.close()

print(f"pedidos entregues: {len(df):,}  |  taxa de atraso: {df.is_late.mean():.1%}")

X = df[["prazo_estimado", "freight_value", "payment_installments"]]
y = df["is_late"]
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=200, random_state=42).fit(X_tr, y_tr)
proba = model.predict_proba(X_te)[:, 1]
print("AUC:", round(roc_auc_score(y_te, proba), 3))

# lift no decil de maior risco
import pandas as pd
avaliacao = pd.DataFrame({"proba": proba, "real": y_te.values})
decil = avaliacao.nlargest(len(avaliacao)//10, "proba")
print(f"precisao no decil de maior risco: {decil.real.mean():.1%}")
print(f"lift sobre a taxa base: {decil.real.mean()/y_te.mean():.1f}x")
```

**[EXECUTAR]**

```bash
python ml/train_delivery_delay.py
```

**[CHECKPOINT]**

> "Acompanhe as saídas, porque cada linha conta uma história. Primeira: **~96 mil pedidos entregues, com taxa de atraso na casa de 8 a 10%** — a taxa base do problema. Segunda: a **AUC** — e aqui uma beleza do nosso setup: como os dados nascem de uma **seed fixa** e o split usa `random_state=42`, o seu número deve bater **exatamente** com o meu; anote o valor que aparecer — bem acima do 0,5 do puro acaso, para um modelo de três features escrito em vinte linhas. E a terceira é a que interessa ao negócio: no **decil de maior risco** — os 10% de pedidos que o modelo aponta como mais perigosos — a precisão sobe bem acima da taxa base: um **lift na casa de 2 a 3 vezes**."

> "E agora para o momento e observe o que aconteceu conceitualmente: **o dado que entrou nesta disciplina como um CSV cru gerado na Aula 1 acabou de sair como uma predição** — uma probabilidade de atraso por pedido. O ciclo se fechou: geração, ingestão, transformação, armazenamento, disponibilização. E **uso**. E observe na honestidade do fluxo: o modelo leu o banco que **nós** garantimos — as datas que o GE validou, o gold que os testes protegem, o pipeline que o CI vigia. Sem as 15 aulas anteriores, essas 20 linhas de scikit-learn seriam lixo estatístico sobre dado sujo. **MLOps**, aliás, é exatamente isso: o DataOps da aula passada aplicado ao modelo — versionar dado, código e modelo; treino reproduzível; monitorar drift. Você já tem os pré-requisitos todos."

### 5. O valor de negócio do lift (10:30 – 12:15)

**[TELA]** Slide: a conta do lift.

> "Vamos traduzir o lift em operação. O Olist tem uns 96 mil pedidos entregues; 8% atrasam — cerca de **7.700 atrasos**. Sem modelo, a logística que quisesse agir preventivamente escolheria pedidos **ao acaso** — e acertaria 8 em cada 100. Com o modelo, mirando o decil de maior risco, ela acerta **24 em cada 100 — três vezes mais**. Na prática: o time aciona a transportadora, prioriza a expedição ou **avisa o cliente proativamente** — 'seu pedido pode atrasar' — exatamente nos pedidos certos. Cliente avisado reclama menos, avalia melhor — e lembra que review baixo era dor real desse marketplace. **Esse é o valor de negócio que o seu pipeline entrega de ponta a ponta**: não é o modelo que vale — é o caminho confiável do CSV até ele."

### 6. O diagrama de referência: as 4 unidades num fluxo (12:15 – 14:15)

**[TELA]** Slide: o diagrama + a tabela das unidades.

> "E agora, costura final. Grava este diagrama de memória, porque ele é a disciplina inteira numa linha: **9 CSVs → Python/DuckDB → Lake/DW em Parquet → dbt → gold → BI e ML.** E onde entrou cada unidade: a **Unidade 1** definiu o *porquê* e o *como* — o ciclo de vida e a estrela. A **Unidade 2** trouxe, processou e **orquestrou** — dbt, lote, stream, Airflow. A **Unidade 3** armazenou e **arquitetou** — DW em camadas, Medallion, nuvem, MDS. E a **Unidade 4** tornou tudo **confiável, seguro e operável** — testes, LGPD, CI/CD — e serviu a IA. Em uma frase: **as três primeiras unidades constroem o pipeline; a quarta o torna profissional.** Quem sabe desenhar esse diagrama e defender cada caixa dele numa entrevista está pronto para o mercado."

### 7. Commit final + o projeto de portfólio (14:15 – 16:30)

**[CÓDIGO]** O último commit da disciplina:

```bash
git add ml/
git commit -m "feat(ml): modelo de previsao de atraso lendo o gold - fecha o pipeline Olist"
git push
```

> "E este commit fecha o repositório — observe o `git log` da disciplina: estrutura e devcontainer. Gerador de dados. Bronze. Schema raw. Estrela. Dbt staging. Stream. Airflow. DW em camadas. Medallion. Nuvem. Docs e dashboard. Qualidade. LGPD. CI. E o modelo. **Dezesseis aulas, um pipeline.** E agora a tarefa final, a mais importante de todas: transformar isso em **portfólio**. Capricha no README: o diagrama de referência no topo, instruções de como rodar — que são triviais, porque há um devcontainer! —, um print do DAG do Airflow, um do dashboard, e os números do modelo. Esse repositório público responde, sozinho, a pergunta que toda entrevista de dados faz: 'você já construiu um pipeline de verdade?' — **Sim. Está aqui. Roda num Codespace em dois minutos.** Poucos candidatos têm isso na mão."

### 8. Encerramento da disciplina (16:30 – 18:30)

**[TELA]** Slide de fechamento.

> "E assim terminamos **Data Engineering and Pipelines**. Você sai daqui com três patrimônios. Primeiro, **um projeto real no GitHub**: ingestão Python, transformação dbt em camadas, DAG do Airflow, testes de qualidade, CI com GitHub Actions, dashboard e modelo de ML — construído, commit a commit, pelas suas mãos. Segundo, o **vocabulário e as ferramentas** do mercado: DuckDB, dbt, Airflow, Parquet e Medallion, Great Expectations, lineage, LGPD, CI/CD, feature store. E terceiro — o mais durável — a **mensagem que atravessou o curso**: *o que roda local com DuckDB e dbt migra para a nuvem trocando o profile; os conceitos são os mesmos.* As ferramentas vão trocar de nome — modelar bem, garantir qualidade e automatizar com segurança valem a carreira inteira."

> "Sobre a carreira, o roteiro pragmático que deixo: **SQL e Python inegociáveis**; modelagem dimensional e dbt; Airflow; uma nuvem a fundo com Terraform; e a consciência de qualidade e governança que esta unidade te deu. Certificações ajudam — mas o que **decide** é portfólio. E o seu está pronto."

> "A indústria brasileira — e mundial — precisa de gente que faça o dado chegar **confiável** do outro lado. Você terminou esta disciplina exatamente desse lado, com um pipeline completo nas mãos para provar. Foi uma honra construir isso com você, aula a aula, commit a commit. Publica o repositório, escreve o README. E vai buscar a vaga. Boa carreira — e vai longe. Um grande abraço!"
