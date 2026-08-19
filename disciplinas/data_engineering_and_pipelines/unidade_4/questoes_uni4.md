# Questionário — Unidade 4

- **Disciplina:** Data Engineering and Pipelines
- **Professor-conteudista:** Afonso Cesar Lelis Brandão

## Orientações

- **40 questões** padrão ENADE: **20 asserção-razão** + **20 de interpretação**.
- Cada questão tem **5 alternativas (a–e)**; a correta é prefixada por `*` (ex.: `*c. ...`).
- Distribuição da alternativa correta: rotação **a, b, c, d, e, a, b, c, d, e...** (8 questões para cada letra).

---

## Questões

### Questão 1 (Asserção-Razão)

> **Asserção I:** A observabilidade de dados é capaz de detectar problemas que o engenheiro não havia antecipado, como uma queda abrupta no volume de linhas de uma tabela.
>
> **porque**
>
> **Razão II:** A observabilidade monitora o comportamento estatístico do dado ao longo do tempo (frescor, volume, distribuição, esquema e linhagem), comparando os valores atuais com a faixa histórica esperada e disparando alerta quando há desvio.

A respeito dessas asserções, assinale a opção correta:

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 2 (Asserção-Razão)

> **Asserção I:** A qualidade de dados pode ser medida pela dimensão da **unicidade**, que avalia, por exemplo, quantos clientes diferentes compartilham o mesmo CPF em uma tabela.
>
> **porque**
>
> **Razão II:** O modelo DAMA-DMBOK define seis dimensões clássicas de qualidade: completude, acurácia, consistência, unicidade, validade e pontualidade.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 3 (Asserção-Razão)

> **Asserção I:** Um **contrato de dados (data contract)** transfere para quem **produz** o dado a responsabilidade pública pelo schema e pelas regras de qualidade, evitando que mudanças na origem quebrem silenciosamente os consumidores a jusante.
>
> **porque**
>
> **Razão II:** O contrato de dados é um documento informal e não versionado, mantido apenas pelo time consumidor, que descreve como cada relatório deve ser desenhado no BI.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 4 (Asserção-Razão)

> **Asserção I:** Um dado **pseudonimizado** sai automaticamente do escopo da LGPD, pois deixa de ser considerado dado pessoal e dispensa qualquer proteção adicional.
>
> **porque**
>
> **Razão II:** Na LGPD, o dado **anonimizado** sai do escopo da lei porque o titular não pode mais ser reidentificado, ao passo que o dado **pseudonimizado** permanece no escopo, já que a reidentificação ainda é possível com a chave.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 5 (Asserção-Razão)

> **Asserção I:** Em DataOps, basta versionar o código de transformação no Git, pois o dado é estático e nunca precisa de versionamento ou reprodutibilidade.
>
> **porque**
>
> **Razão II:** Ferramentas como DVC, lakeFS e o *time travel* de Delta Lake e Iceberg são desnecessárias, uma vez que datasets não mudam ao longo do tempo e não exigem auditoria histórica.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

### Questão 6 (Asserção-Razão)

> **Asserção I:** A estratégia **write-audit-publish (WAP)** garante que o consumidor nunca veja dado intermediário quebrado durante um deploy de pipeline.
>
> **porque**
>
> **Razão II:** No WAP o dado é primeiro escrito em uma tabela temporária, depois **auditado** por testes de qualidade e só é **publicado** (promovido para o consumidor) se passar nas verificações.

A respeito dessas asserções, assinale a opção correta:

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 7 (Asserção-Razão)

> **Asserção I:** A **infraestrutura como código (IaC)** permite recriar ambientes idênticos (dev = staging = prod) em minutos após um desastre.
>
> **porque**
>
> **Razão II:** A LGPD (Lei 13.709/2018) é fiscalizada pela ANPD e prevê multa administrativa de até 2% do faturamento, limitada a R\$ 50 milhões por infração.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 8 (Asserção-Razão)

> **Asserção I:** A **linhagem de dados (data lineage)** é o que permite, na prática, atender ao direito de eliminação previsto na LGPD, pois mostra todos os lugares onde um dado pessoal pousou.
>
> **porque**
>
> **Razão II:** A linhagem de dados serve exclusivamente para deixar os dashboards mais bonitos na camada de BI, não tendo relação com análise de impacto, causa-raiz ou conformidade legal.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 9 (Asserção-Razão)

> **Asserção I:** A **feature store** elimina a necessidade de qualquer pipeline de dados, pois o cientista de dados passa a calcular as *features* diretamente no notebook em produção.
>
> **porque**
>
> **Razão II:** A feature store resolve o *training-serving skew* ao servir a mesma *feature*, calculada com a mesma lógica, tanto para o treino (offline, histórico) quanto para a produção (online, baixa latência).

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 10 (Asserção-Razão)

> **Asserção I:** Em uma arquitetura *streaming-first*, o *batch* deve ser completamente abolido, pois nenhuma decisão de negócio pode tolerar latência maior que alguns milissegundos.
>
> **porque**
>
> **Razão II:** A decisão entre *batch* e *real-time* é puramente tecnológica e nunca depende do custo de negócio de esperar pelo dado, devendo o engenheiro escolher sempre a menor latência possível.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

### Questão 11 (Interpretação)

**Estímulo:**

> "Numa fintech, um campo de renda mensal começou a chegar **multiplicado por 100** após uma mudança não comunicada no sistema-fonte. Sem monitoração, o erro passou despercebido por 9 dias, aprovando milhares de propostas com limite indevido. Um teste de validade de três horas de trabalho teria barrado o lote no primeiro dia — a regra 1-10-100 mostra que custa R\$ 1 prevenir, R\$ 10 corrigir e R\$ 100 conviver com o dado ruim."

A leitura mais alinhada ao texto é:

*a. O incidente foi um problema da dimensão **validade** (o dado não respeitou a faixa/regra esperada) e a observabilidade ataca diretamente o **TTD** (*time to detection*), reduzindo o tempo até a descoberta e tornando a prevenção ordens de grandeza mais barata que a remediação.
b. O caso prova que testes de dados são inúteis, pois o erro aconteceu mesmo havendo um pipeline em produção.
c. O problema descrito é de **pontualidade** (o batch atrasou) e só seria resolvido aumentando a frequência de execução do pipeline.
d. A regra 1-10-100 indica que conviver com o dado ruim é a opção mais barata, pois evita o custo de escrever testes.
e. A solução correta seria esperar o diretor financeiro identificar o erro na reunião mensal, pois a detecção humana é mais confiável que qualquer alerta automático.

### Questão 12 (Interpretação)

**Estímulo:**

> Considere a fórmula de Monte Carlo para o impacto de um incidente de dados:
>
> $$\text{Data downtime} = \text{N.\,de incidentes} \times (\text{TTD} + \text{TTR})$$
>
> Uma empresa teve **3 incidentes** no trimestre. Em média, leva **2 dias** para descobrir cada um (TTD) e **1 dia** para resolver (TTR).

Qual é o *data downtime* total e a leitura mais adequada?

a. 3 dias; a observabilidade não influencia esse número, pois atua apenas sobre o TTR.
*b. 9 dias; a observabilidade ataca principalmente o **TTD**, de modo que reduzir o tempo de detecção (por exemplo, de 2 dias para horas) derruba o *data downtime* total.
c. 6 dias; o cálculo ignora o número de incidentes, pois o que importa é apenas a soma de TTD e TTR.
d. 18 dias; deve-se multiplicar TTD e TTR entre si antes de multiplicar pelos incidentes.
e. 2 dias; basta considerar o maior dos dois tempos (TTD ou TTR), descartando o outro.

### Questão 13 (Interpretação)

**Estímulo:**

| Ferramenta | O que faz |
| --- | --- |
| **dbt tests** | Testes declarativos no `schema.yml` (`not_null`, `unique`, `accepted_values`, `relationships`) |
| **Great Expectations** | Suítes de "expectativas" reutilizáveis, *data docs* automáticos, validação em qualquer ponto |
| **Monte Carlo / Bigeye** | Observabilidade gerenciada (5 pilares + ML de anomalia + linhagem) |

Uma equipe enxuta opera **centenas de tabelas** e quer detecção automática de anomalias e mapeamento de linhagem com pouco esforço de codificação. A escolha mais adequada é:

a. Apenas `dbt tests`, pois testes declarativos como `not_null` substituem completamente a observabilidade em escala.
b. Apenas o Excel, validando as tabelas manualmente uma a uma a cada dia.
*c. Uma plataforma de observabilidade gerenciada (Monte Carlo / Bigeye), pois cobre os 5 pilares, aplica ML de anomalia e mapeia linhagem em grande escala com equipe reduzida.
d. Great Expectations isolado, abrindo mão de qualquer monitoração de frescor, volume ou linhagem.
e. Nenhuma ferramenta; em operações grandes a estratégia correta é desligar os testes para não atrasar o pipeline.

### Questão 14 (Interpretação)

**Estímulo:**

> Uma empresa de e-commerce com faturamento anual de R\$ 80 milhões sofreu um vazamento por um *bucket* mal configurado. A multa da LGPD pode chegar a 2% do faturamento, limitada a R\$ 50 milhões por infração; além disso há custos de notificação aos titulares e perda de receita por *churn*.

A leitura mais adequada do caso é:

a. A multa da LGPD é o maior componente do prejuízo e, paga essa sanção, a empresa não tem mais nenhum impacto financeiro.
b. Como o teto por infração é R\$ 50 milhões, a multa neste caso seria de R\$ 50 milhões, independentemente do faturamento.
c. O vazamento não gera consequência relevante, pois a ANPD não fiscaliza empresas de médio porte.
*d. No teto percentual, a multa seria $0{,}02 \times \text{R\$}\,80\,\text{milhões} = \text{R\$}\,1{,}6$ milhão, mas os custos de reputação e *churn* costumam superar a sanção; prevenir (revisão de permissões, mascaramento, auditoria) é ordens de grandeza mais barato.
e. A solução seria deletar o catálogo de dados para que a ANPD não consiga rastrear a origem do vazamento.

### Questão 15 (Interpretação)

**Estímulo:**

> Uma equipe de dados migrou de processo manual para CI/CD. **Antes:** 2 deploys/mês, *change failure rate* de 30%. **Depois:** 20 deploys/mês, *change failure rate* de 5%, com rollback automático.

A conclusão **mais bem suportada** por esses dados é:

a. CI/CD aumentou o número de deploys, mas piorou a confiabilidade, pois mais deploys significam mais incidentes em termos absolutos.
b. O segredo da melhoria foi fazer **menos** deploys para reduzir o risco de cada mudança.
c. A *change failure rate* é irrelevante; o único objetivo do DataOps é maximizar a quantidade de deploys, custe o que custar.
d. A migração só faz sentido se eliminar totalmente as falhas de mudança (taxa de 0%), o que não ocorreu aqui.
*e. CI/CD permitiu **10× mais deploys** com a *change failure rate* caindo de 30% para 5%, mostrando que a meta DORA é deploy frequente **com** baixa taxa de falha — o segredo é tornar o deploy barato e seguro, não fazer menos.

### Questão 16 (Interpretação)

**Estímulo:**

> "A IA generativa não tornou o engenheiro de dados obsoleto — fez o oposto. Modelo só é tão bom quanto o pipeline que o alimenta. *Garbage in, garbage out* virou regra de ouro de ML."

A leitura mais alinhada ao texto é:

*a. Dado **confiável, governado e bem-modelado** é pré-requisito de qualquer IA que funcione, de modo que qualidade, governança e DataOps (Unidade 4) são a fundação sobre a qual o MLOps se apoia.
b. A IA generativa substituiu o engenheiro de dados, que agora é desnecessário em qualquer projeto de ML.
c. A qualidade do dado é irrelevante para modelos de ML, pois algoritmos modernos corrigem automaticamente qualquer erro de entrada.
d. *Garbage in, garbage out* significa que quanto mais dado bruto for ingerido, melhor o modelo, sem necessidade de validação.
e. O papel do engenheiro de dados na era da IA se restringe a apagar dados antigos para liberar espaço de armazenamento.

### Questão 17 (Interpretação)

**Estímulo:**

> Em uma *healthtech*, um modelo de ML que prioriza atendimentos começou a perder acurácia em produção: os dados reais dos pacientes se afastaram progressivamente do perfil dos dados usados no treino.

O fenômeno descrito e a prática de MLOps adequada são:

a. *Training-serving skew*, resolvido apenas reescrevendo os dashboards de BI.
*b. *Data drift / model drift*, que exige monitoração contínua em MLOps — quando os dados de produção se afastam dos de treino e a acurácia cai, dispara-se retreino ou ajuste, apoiado em qualidade, linhagem e CI/CD.
c. *Data downtime*, que é resolvido apenas aumentando o número de deploys do modelo por mês.
d. Um problema de IaC, corrigido recriando o *bucket* de armazenamento com Terraform.
e. Pseudonimização, resolvida anonimizando todos os campos do modelo para sair do escopo da LGPD.

### Questão 18 (Interpretação)

**Estímulo:**

> "Real-time analytics processa o dado em segundos ou milissegundos desde o evento, com bancos como Druid, ClickHouse e Pinot. Mas a decisão *batch vs. real-time* é de **negócio**: pergunte sempre 'qual o custo de esperar 1 hora por este dado?'."

A leitura mais coerente com o texto é:

a. Toda empresa deve migrar imediatamente para *real-time*, pois *batch* é uma tecnologia ultrapassada e sempre mais cara.
b. *Real-time* e *batch* produzem exatamente os mesmos resultados, sendo a escolha entre eles puramente estética.
*c. A escolha entre *batch* e *real-time* deve ser guiada pelo **custo de esperar**: se for alto (fraude, recomendação, alerta de sensor), justifica-se *real-time*; se for baixo, *batch* é mais simples e barato — não se paga por latência que ninguém usa.
d. Bancos como Druid e ClickHouse devem ser usados em todos os pipelines, inclusive nos puramente analíticos em lote diário.
e. O *batch* só deve ser usado quando não houver orçamento para implementar *streaming*, sendo sempre tecnicamente inferior.

### Questão 19 (Interpretação)

**Estímulo:**

> Uma equipe migrou para CI/CD. **Antes (manual):** 2 deploys/mês, cada um com 4 h de engenheiro a R\$ 120/h. **Depois (CI/CD):** 20 deploys/mês, cada um com 0,3 h de supervisão a R\$ 120/h.

Comparando **apenas o custo de mão de obra por deploy**, qual a economia por deploy ao adotar CI/CD?

a. R\$ 36, pois é o custo total do novo processo por deploy.
b. R\$ 480, pois é o custo antigo por deploy, sem desconto do novo.
c. R\$ 516, somando o custo antigo e o novo por deploy.
*d. R\$ 444 por deploy, pois o custo cai de $4 \times \text{R\$}\,120 = \text{R\$}\,480$ para $0{,}3 \times \text{R\$}\,120 = \text{R\$}\,36$, uma redução de R\$ 444.
e. R\$ 0, pois CI/CD não altera o custo de mão de obra por deploy.

### Questão 20 (Interpretação)

**Estímulo:**

> "O pipeline de referência que você deve saber desenhar de memória:
>
> $$\text{Fontes} \rightarrow \text{Ingestão} \rightarrow \text{Lake/Warehouse} \rightarrow \text{Transformação} \rightarrow \text{Servir} \rightarrow \text{BI/ML}$$
>
> As três primeiras unidades **constroem** o pipeline; a quarta o torna **profissional**."

A leitura mais alinhada ao texto é:

a. As quatro unidades são intercambiáveis, e a ordem das etapas do pipeline pode ser qualquer uma sem impacto no resultado.
b. A Unidade 4 (qualidade, governança e DataOps) é dispensável, pois o dado já chega ao BI nas etapas anteriores.
c. Um engenheiro júnior e um sênior entregam exatamente a mesma coisa, já que ambos fazem o dado chegar ao destino.
d. As etapas de qualidade, governança e DataOps pertencem à fase de **Ingestão** e não atravessam as demais etapas do pipeline.
*e. As Unidades 1 a 3 constroem o fluxo (fontes → ingestão → lake/warehouse → transformação → servir → BI/ML) e a Unidade 4 o profissionaliza, garantindo que tudo seja **confiável, seguro e operável** — diferença entre fazer o dado chegar e fazê-lo chegar confiável, governado e com deploy seguro.

### Questão 21 (Asserção-Razão)

> **Asserção I:** No pipeline Olist, a **integridade referencial** entre `fct_order_items` e `dim_products` pode ser verificada de forma barata com um teste `relationships` declarado no `schema.yml` do dbt.
>
> **porque**
>
> **Razão II:** O teste `relationships` do dbt confere se **todo** valor de uma coluna (ex.: `product_id` no fato) existe na coluna correspondente da tabela referenciada (ex.: `product_id` em `dim_products`), acusando *órfãos* que quebrariam a junção fato→dimensão.

A respeito dessas asserções, assinale a opção correta:

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 22 (Asserção-Razão)

> **Asserção I:** No projeto Olist, o arquivo `olist.duckdb` e os Parquet do `gold/` **não** devem ser versionados no Git, entrando no `.gitignore`.
>
> **porque**
>
> **Razão II:** O DataOps trata **dado e código exatamente da mesma forma**, versionando ambos no mesmo repositório Git, já que arquivos de dados e arquivos de modelo têm o mesmo ciclo de vida e o mesmo mecanismo de versionamento.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 23 (Asserção-Razão)

> **Asserção I:** No modelo de governança do Olist, o **data steward** é a pessoa que assina os contratos com a nuvem e paga a fatura de armazenamento do `gold/`.
>
> **porque**
>
> **Razão II:** Na governança de dados, o **data steward** é o papel que zela pelo **significado** de cada campo (por exemplo, a diferença entre `customer_id` e `customer_unique_id`), garantindo a definição e a consistência semântica do dado.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 24 (Asserção-Razão)

> **Asserção I:** Na LGPD, a **minimização** exige coletar a maior quantidade possível de atributos de cada titular, pois "quanto mais dado guardado, mais seguro fica o pipeline".
>
> **porque**
>
> **Razão II:** A **retenção** é o princípio de definir por quanto tempo cada tabela com dado pessoal é mantida, apoiando-se na ideia de que **dado que não se guarda é dado que não vaza**.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 25 (Asserção-Razão)

> **Asserção I:** No pipeline Olist, o controle de acesso por **RBAC** significa dar a cada colaborador, individualmente e pelo nome, uma permissão específica em cada tabela, sem qualquer noção de papel.
>
> **porque**
>
> **Razão II:** O princípio do **menor privilégio** determina conceder o **máximo** de acesso possível a todos os usuários por padrão, liberando o schema `raw` a qualquer analista para evitar burocracia.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

### Questão 26 (Asserção-Razão)

> **Asserção I:** No CI do pipeline Olist, um único comando `dbt build` a cada *pull request* já cobre tanto a **construção** dos modelos quanto os **testes de qualidade** da Aula 13.
>
> **porque**
>
> **Razão II:** O comando `dbt build` executa `run` **e** `test` numa mesma tacada, de modo que, se um modelo quebrar ou um teste falhar, o *merge* é bloqueado e o erro morre no PR, não em produção.

A respeito dessas asserções, assinale a opção correta:

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 27 (Asserção-Razão)

> **Asserção I:** No dbt, promover o pipeline Olist de `dev` para `prod` não exige reescrever os modelos, bastando trocar o **target** no `profiles.yml`.
>
> **porque**
>
> **Razão II:** A **LGPD (Lei 13.709/2018)** é fiscalizada pela **ANPD** e assegura ao titular o direito de eliminação de seus dados pessoais.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 28 (Asserção-Razão)

> **Asserção I:** No Olist, a dimensão de qualidade **acurácia** é o que permite flagrar um registro em que `order_delivered_customer_date` é **anterior** ao `order_purchase_timestamp` — uma entrega antes da compra, impossível na realidade.
>
> **porque**
>
> **Razão II:** A dimensão **acurácia** apenas verifica se cada `order_id` aparece uma única vez na tabela `stg_orders`, não tendo qualquer relação com a coerência entre datas de um mesmo pedido.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 29 (Asserção-Razão)

> **Asserção I:** No projeto Olist, uma **feature store** gerenciada (como Feast ou Tecton) e uma *view* do dbt sobre `fct_orders` + dimensões são conceitos **totalmente distintos**, sem qualquer relação de propósito.
>
> **porque**
>
> **Razão II:** No projeto local do Olist, a "feature store" é justamente uma *view* do dbt que consolida as *features* (prazo estimado, frete, nº de itens, categoria, UF, parcelas) — o **conceito** é o mesmo de uma feature store gerenciada, que serve a mesma lógica de cálculo para treino e produção.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 30 (Asserção-Razão)

> **Asserção I:** No Olist, a dimensão de qualidade **completude** é indiferente ao fato de milhares de pedidos não possuírem `review`, pois campos ausentes nunca afetam a qualidade do dado.
>
> **porque**
>
> **Razão II:** A **consistência** entre tabelas — como o `payment_value` somado por `order_id` bater com o total esperado em `fct_orders` — é irrelevante, já que valores divergentes entre `stg_order_payments` e o fato jamais comprometem uma decisão de negócio.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

### Questão 31 (Interpretação)

**Estímulo:**

> "No Olist, se o volume diário de pedidos cair de ~135 para 12, nenhum `not_null` acusa — observabilidade sim. Testes verificam regras que você **antecipou**; a observabilidade detecta o que você **não previu**, monitorando frescor, volume, distribuição, esquema e linhagem ao longo do tempo."

A leitura mais alinhada ao texto é:

*a. Testes declarativos (como `not_null`) e observabilidade são **complementares**: os testes barram violações de regras conhecidas, enquanto a observabilidade monitora o comportamento histórico (volume, frescor, distribuição, esquema, linhagem) e captura o imprevisto, como uma queda anômala de volume.
b. Como a observabilidade cobre o imprevisto, os testes `not_null`, `unique` e `accepted_values` do dbt tornam-se dispensáveis no pipeline Olist.
c. A queda de volume de 135 para 12 pedidos é um problema de **unicidade**, resolvido por um teste `unique` no `order_id`.
d. Observabilidade e testes fazem exatamente a mesma coisa, e ter ambos é redundância que só aumenta o custo do pipeline.
e. Um teste `not_null` acusaria a queda de volume, pois volume e nulos são a mesma métrica sob nomes diferentes.

### Questão 32 (Interpretação)

**Estímulo:**

> No staging do Olist, aplica-se o seguinte mascaramento de localização:
>
> ```sql
> left(customer_zip_code_prefix::varchar, 3) || 'XX' as zip_masked
> ```
>
> O `customer_zip_code_prefix` original tem 5 dígitos.

A leitura mais adequada do efeito desse mascaramento é:

a. O comando anonimiza plenamente o dado, retirando-o do escopo da LGPD, pois nenhum dígito do CEP permanece visível.
*b. O mascaramento **reduz a granularidade** da localização (mantém 3 dígitos + `XX`), aplicando defesa em profundidade e menor privilégio para quem não precisa do prefixo cheio, sem por si só tornar o dado plenamente anônimo.
c. O mascaramento aumenta a precisão geográfica, pois `XX` acrescenta dois dígitos ao CEP original.
d. O comando viola a LGPD, já que expor qualquer parte do CEP é proibido em qualquer circunstância.
e. O mascaramento substitui a necessidade de RBAC, tornando desnecessário qualquer controle de acesso por papel.

### Questão 33 (Interpretação)

**Estímulo:**

> Rastreando um titular pelo lineage do dbt no Olist:
>
> $$\text{raw.customers} \rightarrow \text{stg\_customers} \rightarrow \text{dim\_customers} \rightarrow \text{fct\_orders} \rightarrow \text{mart\_payment\_analysis}$$
>
> Um titular exerce o **direito de eliminação** previsto na LGPD.

A leitura mais coerente com o texto é:

a. Basta apagar a linha em `raw.customers`; os modelos a jusante se corrigem sozinhos sem necessidade de conhecer a linhagem.
b. O lineage serve apenas para deixar a documentação do projeto mais bonita, não tendo utilidade para atender a um pedido de exclusão.
*c. O lineage funciona como a **planta baixa da exclusão**: mostra **todos** os modelos onde o dado do titular pousou (de `raw` ao `mart_payment_analysis`), permitindo remover o rastro em cada ponto e responder tanto a impacto (a jusante) quanto a causa-raiz (a montante).
d. A LGPD não exige rastrear onde o dado pousou; a eliminação pode ignorar `dim_customers` e `fct_orders`.
e. O direito de eliminação só se aplica a `raw.customers`, pois marts derivados deixam de ser dado pessoal automaticamente.

### Questão 34 (Interpretação)

**Estímulo:**

> "Clicar no console da nuvem para criar o *bucket* do `gold/` do Olist é frágil e não reproduzível. Com **Terraform** você declara: 'quero um *bucket* para o gold com versionamento e retenção de 90 dias' — em arquivo versionado, revisável em PR, e o mesmo código recria a infra em minutos."

A leitura mais adequada do texto é:

a. IaC serve apenas para economizar cliques no console, sem qualquer ganho de reprodutibilidade ou revisão.
b. Como o Terraform declara a infra, ele elimina a necessidade de qualquer teste de dados no pipeline Olist.
c. IaC e governança são incompatíveis: políticas de acesso da Aula 14 jamais podem ser expressas como código.
*d. A **infraestrutura como código** torna a criação da infra do Olist declarativa, versionada e revisável em PR, permitindo recriar ambientes idênticos em minutos e até codificar as políticas de acesso da governança.
e. O versionamento e a retenção de 90 dias declarados no Terraform aplicam-se ao código dbt, não ao *bucket* de armazenamento.

### Questão 35 (Interpretação)

**Estímulo:**

> No Olist, das entregas registradas, cerca de $8\%$ chegam **após** a data estimada. Um `RandomForestClassifier` treinado sobre o gold atinge precisão de $\approx 24\%$ no decil de maior risco. O *lift* sobre o acaso é:
>
> $$\text{lift} = \frac{0{,}24}{0{,}08} = 3{,}0$$

A leitura mais adequada do resultado é:

a. O modelo é inútil, pois 24% ainda é menor que 100% de precisão.
b. O *lift* de 3,0 significa que o modelo acerta 3% dos atrasos, um resultado pior que o acaso.
c. O *lift* mede a latência do pipeline em segundos, não a qualidade da predição.
d. Como a taxa-base é 8%, prever atraso no chute já daria 24% de precisão, tornando o modelo redundante.
*e. Mirando os 10% de pedidos que o modelo aponta como mais arriscados, a logística encontra atrasos **3× mais** do que escolhendo pedidos ao acaso — valor de negócio suficiente para acionar transportadora ou avisar o cliente proativamente.

### Questão 36 (Interpretação)

**Estímulo:**

> "Custa **R\$ 1** prevenir o defeito (escrever o teste), **R\$ 10** corrigi-lo no pipeline e **R\$ 100** conviver com ele em produção. Um `accepted_values` de três linhas no `order_status` é o R\$ 1; descobrir que o `mart_delivery_performance` contou um status inexistente **depois** que a diretoria apresentou o número é o R\$ 100."

A leitura mais alinhada ao texto é:

*a. A regra **1-10-100** mostra que o custo de um defeito cresce por ordem de grandeza conforme ele avança no pipeline; por isso deve-se **automatizar a verificação onde o dado é produzido** (no `schema.yml`), e não onde é consumido (no mart/BI).
b. A regra 1-10-100 recomenda conviver com o defeito, pois R\$ 100 é o menor dos três custos.
c. O melhor lugar para validar o `order_status` é o dashboard da diretoria, o mais próximo do consumidor final.
d. Escrever o `accepted_values` custa mais caro do que corrigir o defeito depois em produção.
e. A regra 1-10-100 é uma métrica de latência (frescor) do pipeline, sem relação com o custo de defeitos.

### Questão 37 (Interpretação)

**Estímulo:**

> "MLOps é o DataOps aplicado ao modelo: versionar dado, código **e** modelo; treino reproduzível; e monitorar *data/model drift*. Tudo o que você fez nesta unidade — qualidade, lineage, CI/CD — é **pré-requisito** de MLOps."

A leitura mais coerente com o texto é:

a. MLOps substitui e torna dispensáveis a qualidade, o lineage e o CI/CD construídos na Unidade 4.
*b. MLOps **estende** o DataOps ao ciclo do modelo (versionando também o modelo e monitorando *drift*), apoiando-se na fundação de qualidade, lineage e CI/CD já construída — que é pré-requisito, não concorrente.
c. MLOps trata apenas de versionar código, ignorando o versionamento de dado e de modelo.
d. *Data/model drift* é um problema de infraestrutura resolvido apenas recriando o *bucket* com Terraform.
e. MLOps dispensa treino reproduzível, pois basta reexecutar o notebook manualmente quando a acurácia cair.

### Questão 38 (Interpretação)

**Estímulo:**

> Uma organização cresce e passa a ter **centenas de modelos** espalhados por vários times e ferramentas. Precisa centralizar metadados, dicionário de dados (o significado de cada campo) e a linhagem ponta a ponta entre times, além de classificar campos com PII como o `customer_unique_id`.

A escolha mais adequada, segundo a Aula 14, é:

a. Confiar apenas no lineage interno do dbt, que já cobre metadados e linhagem entre **todos** os times e ferramentas da empresa.
b. Manter uma planilha manual de campos, atualizada por cada time à sua maneira, sem ferramenta dedicada.
*c. Adotar um **catálogo de dados** dedicado (como **DataHub**, open source, ou **Atlan**, comercial), que centraliza metadados, dicionário de dados e linhagem ponta a ponta, onde um campo com PII como `customer_unique_id` fica catalogado, classificado e governado.
d. Desligar a governança em escala, pois catálogos de dados só funcionam para uma única equipe.
e. Substituir o catálogo por um teste `not_null` no `customer_unique_id`, suficiente para classificar PII entre times.

### Questão 39 (Interpretação)

**Estímulo:**

> Considere o cálculo de impacto de um vazamento no Olist (faturamento de R\$ 80 milhões):
>
> - Multa LGPD (teto percentual): $0{,}02 \times 80\,000\,000 = \text{R\$}\,1\,600\,000$
> - Notificação: $96\,096 \times 9 = \text{R\$}\,864\,864$
> - *Churn* (1º ano): $0{,}03 \times 96\,096 \times 220 \approx \text{R\$}\,634\,234$
> - Prevenção (mascaramento + RBAC + auditoria) $\approx \text{R\$}\,60\,000$

A leitura mais adequada do caso é:

a. A multa de R\$ 1,6 milhão é o único custo relevante; notificação e *churn* podem ser ignorados.
b. Prevenir custaria mais do que o impacto total do vazamento, tornando a prevenção economicamente injustificável.
c. Como o teto por infração é R\$ 50 milhões, a multa aplicada seria de R\$ 50 milhões independentemente do faturamento.
*d. O impacto no 1º ano soma $\approx \text{R\$}\,3{,}1$ milhões (multa + notificação + *churn*), enquanto prevenir custaria $\approx \text{R\$}\,60$ mil; a **multa é a menor das parcelas** e prevenir na origem (como o Olist já faz ao pseudonimizar) é ordens de grandeza mais barato.
e. O vazamento não gera consequência porque o Olist já é pseudonimizado, tornando o cálculo de impacto irrelevante em qualquer cenário.

### Questão 40 (Interpretação)

**Estímulo:**

> "Pense no seu pipeline Olist hoje: modelos dbt na sua máquina, sem CI, deploy = você rodando `dbt run` no terminal. Se um colega abrisse um *pull request* alterando o `fct_order_items` às 17h de uma sexta, você daria *merge* sem medo? Esse **medo** é o sintoma exato que o DataOps cura."

A leitura mais alinhada ao texto é:

a. O medo do *merge* é uma questão de coragem individual, e a solução é escolher engenheiros mais destemidos.
b. A solução para o medo é **proibir** merges às sextas-feiras, reduzindo a frequência de deploy do pipeline Olist.
c. O medo é irrelevante, pois alterar o `fct_order_items` nunca poderia quebrar um mart a jusante como o `mart_seller_scorecard`.
d. A cura para o medo é versionar o `olist.duckdb` no Git, garantindo *rollback* do dado a cada deploy.
*e. O medo é um sintoma de **falta de processo**, curado por práticas de DataOps (CI rodando `dbt build`, ambiente de *staging*, `dbt test`, WAP): numa equipe madura, merge no `fct_order_items` na sexta às 17h é **rotina, não coragem**.

---

## Feedbacks

### Questão 1

- **a.** *Correta!* Ambas verdadeiras e a II justifica a I. A observabilidade detecta o imprevisto (como queda de volume) justamente porque monitora o comportamento estatístico ao longo do tempo e compara com a faixa histórica — a Razão explica diretamente **por que** a detecção descrita na Asserção é possível.
- **b.** Incorreta. A Razão **justifica** diretamente a Asserção: é o monitoramento estatístico dos pilares que viabiliza detectar o imprevisto.
- **c.** Incorreta. A Razão é verdadeira (os 5 pilares e o monitoramento histórico estão corretos).
- **d.** Incorreta. A Asserção é verdadeira (a observabilidade detecta, sim, o que não foi antecipado).
- **e.** Incorreta. Ambas são verdadeiras.

### Questão 2

- **a.** Incorreta. A Razão não justifica a Asserção: listar as seis dimensões não explica **por que** a unicidade mede CPFs duplicados.
- **b.** *Correta!* As duas proposições são verdadeiras: a unicidade de fato avalia duplicidades (vários clientes com o mesmo CPF) e o DAMA-DMBOK de fato define as seis dimensões. Porém, a Razão apenas **lista** o conjunto de dimensões; não constitui a justificativa específica da afirmação sobre unicidade — são informações verdadeiras mas independentes.
- **c.** Incorreta. A Razão é verdadeira (o DAMA-DMBOK define as seis dimensões citadas).
- **d.** Incorreta. A Asserção é verdadeira (unicidade trata de registros duplicados).
- **e.** Incorreta. Ambas são verdadeiras.

### Questão 3

- **a.** Incorreta. A Razão é falsa.
- **b.** Incorreta. A Razão é falsa.
- **c.** *Correta!* A Asserção é verdadeira: o data contract é um acordo formal e versionado que transfere a responsabilidade pelo schema e pela qualidade a quem produz o dado, evitando quebras silenciosas a jusante. A Razão é falsa: o contrato é **formal e versionado** e acordado entre produtor e consumidor — não um documento informal mantido só pelo consumidor para desenhar relatórios.
- **d.** Incorreta. A Asserção é verdadeira.
- **e.** Incorreta. A Asserção é verdadeira.

### Questão 4

- **a.** Incorreta. A Asserção é falsa.
- **b.** Incorreta. A Asserção é falsa.
- **c.** Incorreta. A Razão é verdadeira.
- **d.** *Correta!* A Asserção é falsa: é o dado **anonimizado** (não o pseudonimizado) que sai do escopo da LGPD. O dado pseudonimizado **permanece** sujeito à lei, pois a reidentificação ainda é possível com a chave. A Razão descreve corretamente essa distinção.
- **e.** Incorreta. A Razão é verdadeira.

### Questão 5

- **a.** Incorreta. Ambas são falsas.
- **b.** Incorreta. Ambas são falsas.
- **c.** Incorreta. A Razão também é falsa.
- **d.** Incorreta. A Asserção também é falsa.
- **e.** *Correta!* As duas proposições são falsas. Em DataOps versiona-se **código E dado**: o dado muda ao longo do tempo, e versioná-lo (DVC, lakeFS, *time travel* de Delta/Iceberg/Hudi) é o que habilita reprodutibilidade, testes seguros em *branch* do lake e auditoria. Logo, essas ferramentas são necessárias, não dispensáveis.

### Questão 6

- **a.** *Correta!* Ambas verdadeiras e a II justifica a I. A Razão descreve exatamente o mecanismo write → audit → publish que **causa** o efeito afirmado na Asserção: como só se publica o que passou na auditoria, o consumidor nunca vê dado intermediário quebrado.
- **b.** Incorreta. A Razão justifica diretamente a Asserção.
- **c.** Incorreta. A Razão é verdadeira (descreve corretamente o fluxo WAP).
- **d.** Incorreta. A Asserção é verdadeira.
- **e.** Incorreta. Ambas são verdadeiras.

### Questão 7

- **a.** Incorreta. A Razão não justifica a Asserção — IaC e multa da LGPD são temas independentes.
- **b.** *Correta!* As duas proposições são individualmente verdadeiras: a IaC de fato recria ambientes idênticos em minutos após desastre, e a LGPD de fato é fiscalizada pela ANPD com multa de até 2% do faturamento (teto de R\$ 50 mi/infração). Mas a Razão (sanção da LGPD) **não explica** a capacidade de reprodutibilidade da IaC — são fatos verdadeiros sem relação de causa.
- **c.** Incorreta. A Razão é verdadeira.
- **d.** Incorreta. A Asserção é verdadeira.
- **e.** Incorreta. Ambas são verdadeiras.

### Questão 8

- **a.** Incorreta. A Razão é falsa.
- **b.** Incorreta. A Razão é falsa.
- **c.** *Correta!* A Asserção é verdadeira: para atender ao direito de eliminação da LGPD é preciso saber **todos** os lugares onde o dado pessoal pousou, o que exige linhagem. A Razão é falsa: a linhagem serve para análise de impacto (a jusante), causa-raiz (a montante) e conformidade — não apenas para "embelezar dashboards".
- **d.** Incorreta. A Asserção é verdadeira.
- **e.** Incorreta. A Asserção é verdadeira.

### Questão 9

- **a.** Incorreta. A Asserção é falsa.
- **b.** Incorreta. A Asserção é falsa.
- **c.** Incorreta. A Razão é verdadeira.
- **d.** *Correta!* A Asserção é falsa: a feature store **não elimina** o pipeline — ela é um repositório central de *features* versionadas, alimentado por pipelines, e padroniza a lógica de cálculo. A Razão descreve corretamente como ela resolve o *training-serving skew*, servindo a mesma *feature* (offline para treino, online para produção).
- **e.** Incorreta. A Razão é verdadeira.

### Questão 10

- **a.** Incorreta. Ambas são falsas.
- **b.** Incorreta. Ambas são falsas.
- **c.** Incorreta. A Razão também é falsa.
- **d.** Incorreta. A Asserção também é falsa.
- **e.** *Correta!* As duas proposições são falsas. Em *streaming-first* o *batch* não é abolido — ele vira um **caso particular** do *stream* ("um stream olhado em janelas"); e a maioria dos casos é bem resolvida por *batch*. Além disso, a decisão *batch vs. real-time* é de **negócio** (custo de esperar pelo dado), não puramente tecnológica — não se deve pagar por latência que ninguém usa.

### Questão 11

- **a.** *Correta!* O caso é de **validade** (o dado violou a faixa esperada de renda), e a observabilidade reduz o **TTD**, antecipando a detecção. A regra 1-10-100 confirma que prevenir é muito mais barato que conviver com o erro — exatamente a tese da Aula 13.
- **b.** Incorreta. O caso mostra justamente a **ausência** de teste/observabilidade; o problema não desqualifica os testes, prova a falta deles.
- **c.** Incorreta. Não houve atraso de execução (pontualidade); o dado chegou no horário, porém **errado** (validade).
- **d.** Incorreta. A regra 1-10-100 indica o **oposto**: conviver (R\$ 100) é a opção mais cara, não a mais barata.
- **e.** Incorreta. Foi exatamente a dependência de detecção humana tardia que custou caro; o objetivo é o alerta automático precoce.

### Questão 12

- **a.** Incorreta. O resultado não é 3 dias, e a observabilidade atua principalmente sobre o **TTD**, não o TTR.
- **b.** *Correta!* $3 \times (2 + 1) = 9$ dias. A observabilidade ataca o **TTD**: reduzir o tempo de detecção (de 2 dias para horas) derruba diretamente o *data downtime*.
- **c.** Incorreta. O número de incidentes **não** é ignorado — ele multiplica a soma (TTD + TTR).
- **d.** Incorreta. TTD e TTR são **somados**, não multiplicados entre si.
- **e.** Incorreta. A fórmula usa a **soma** de TTD e TTR, não o maior dos dois.

### Questão 13

- **a.** Incorreta. `dbt tests` cobre regras antecipadas, mas **não** detecta anomalias estatísticas nem mapeia linhagem em escala.
- **b.** Incorreta. Validação manual em planilha não escala para centenas de tabelas nem detecta anomalias automaticamente.
- **c.** *Correta!* Para operação grande com equipe enxuta, uma plataforma de observabilidade gerenciada (Monte Carlo / Bigeye) cobre os 5 pilares, aplica ML de anomalia e mapeia linhagem com pouco código — exatamente o cenário de uso da tabela.
- **d.** Incorreta. Great Expectations valida regras, mas isolado não entrega monitoração contínua de frescor/volume/linhagem em escala.
- **e.** Incorreta. Desligar testes contraria todo o princípio da unidade — "automatize a verificação onde o dado é produzido".

### Questão 14

- **a.** Incorreta. A multa **não** é o maior componente; reputação e *churn* costumam superá-la, e o impacto persiste após a sanção.
- **b.** Incorreta. O teto de R\$ 50 mi é o **limite máximo** por infração, não o valor aplicado; aqui o teto percentual (2% de R\$ 80 mi) dá R\$ 1,6 milhão.
- **c.** Incorreta. A ANPD fiscaliza o tratamento de dados pessoais independentemente do porte da empresa.
- **d.** *Correta!* No teto percentual a multa seria $0{,}02 \times \text{R\$}\,80\,\text{mi} = \text{R\$}\,1{,}6$ milhão, mas reputação e *churn* normalmente custam mais — e a prevenção (permissões, mascaramento, auditoria) é ordens de grandeza mais barata.
- **e.** Incorreta. Destruir o catálogo seria ilícito e agravaria a situação; governança e linhagem são exigências, não algo a ocultar.

### Questão 15

- **a.** Incorreta. A confiabilidade **melhorou**: a *change failure rate* caiu de 30% para 5%.
- **b.** Incorreta. O segredo é o **oposto** — fazer mais deploys, porém baratos e seguros.
- **c.** Incorreta. A *change failure rate* é central: a meta DORA é frequência alta **com** baixa taxa de falha.
- **d.** Incorreta. A melhoria não exige taxa de 0%; reduzir de 30% para 5% já é ganho expressivo.
- **e.** *Correta!* 20 vs. 2 deploys = 10× mais, com a *change failure rate* caindo de 30% para 5% — a meta DORA é deploy frequente com baixa taxa de falha, tornando o deploy barato e seguro.

### Questão 16

- **a.** *Correta!* A tese da Aula 16 é exatamente essa: dado confiável, governado e bem-modelado é pré-requisito de qualquer IA — qualidade, governança e DataOps (Unidade 4) são a fundação do MLOps.
- **b.** Incorreta. O texto afirma o oposto: a IA **amplificou** o papel do engenheiro de dados.
- **c.** Incorreta. *Garbage in, garbage out* significa justamente que dado ruim produz modelo ruim; a qualidade é decisiva.
- **d.** Incorreta. Mais dado bruto **não** é melhor; o que importa é dado confiável e validado.
- **e.** Incorreta. O papel se expande (provedor de dados para IA, uso de copilots, extração via LLM), não se reduz a apagar dados.

### Questão 17

- **a.** Incorreta. *Training-serving skew* é a divergência de cálculo da *feature* entre treino e produção; aqui o problema é a mudança do **perfil dos dados** ao longo do tempo, e dashboards de BI não resolvem.
- **b.** *Correta!* O fenômeno é *data drift / model drift* — os dados de produção se afastam dos de treino e a acurácia cai. A prática de MLOps é monitoração contínua para disparar retreino/ajuste, apoiada em qualidade, linhagem e CI/CD.
- **c.** Incorreta. *Data downtime* é período de dado ausente/errado; não se resolve apenas aumentando deploys.
- **d.** Incorreta. Não é problema de infraestrutura; recriar o *bucket* não corrige a queda de acurácia do modelo.
- **e.** Incorreta. Pseudonimização é tema de LGPD/privacidade, sem relação com a perda de acurácia por mudança de distribuição.

### Questão 18

- **a.** Incorreta. *Batch* não é ultrapassado nem sempre mais caro; ele é mais simples e barato quando o custo de esperar é baixo.
- **b.** Incorreta. A escolha não é estética; difere em latência, custo e adequação ao caso de uso.
- **c.** *Correta!* A decisão é de negócio, guiada pelo **custo de esperar**: alto → *real-time* (fraude, recomendação, sensor); baixo → *batch*, mais simples e barato. Não se paga por latência que ninguém usa.
- **d.** Incorreta. Bancos de *real-time* (Druid/ClickHouse) não são necessários em pipelines analíticos em lote diário.
- **e.** Incorreta. *Batch* não é "inferior por falta de orçamento"; é a escolha correta quando a latência adicional não tem custo de negócio relevante.

### Questão 19

- **a.** Incorreta. R\$ 36 é o **custo novo** por deploy, não a economia.
- **b.** Incorreta. R\$ 480 é o **custo antigo** por deploy, sem descontar o novo.
- **c.** Incorreta. Deve-se **subtrair** os custos, não somá-los.
- **d.** *Correta!* Custo antigo: $4 \times \text{R\$}\,120 = \text{R\$}\,480$. Custo novo: $0{,}3 \times \text{R\$}\,120 = \text{R\$}\,36$. Economia por deploy: $480 - 36 = \text{R\$}\,444$.
- **e.** Incorreta. O custo de mão de obra por deploy cai expressivamente (de R\$ 480 para R\$ 36).

### Questão 20

- **a.** Incorreta. As etapas têm ordem lógica (fontes → … → BI/ML) e as unidades têm papéis distintos.
- **b.** Incorreta. A Unidade 4 não é dispensável: é o que torna o pipeline confiável, seguro e operável (profissional).
- **c.** Incorreta. O texto distingue júnior (faz o dado chegar) de sênior (faz o dado chegar confiável, governado e com deploy seguro).
- **d.** Incorreta. Qualidade, governança e DataOps são *undercurrents* que **atravessam todas** as etapas, não pertencem só à ingestão.
- **e.** *Correta!* As Unidades 1 a 3 constroem o fluxo de referência e a Unidade 4 o profissionaliza — garantindo confiabilidade, segurança e operabilidade, a diferença entre fazer o dado chegar e fazê-lo chegar confiável e governado.

### Questão 21

- **a.** *Correta!* Ambas verdadeiras e a II justifica a I. O teste `relationships` é exatamente o mecanismo que confere a integridade referencial afirmada na Asserção: ele valida que todo `product_id` do fato existe em `dim_products`, acusando órfãos — a Razão explica **por que** essa verificação barata garante a junção fato→dimensão.
- **b.** Incorreta. A Razão **justifica** diretamente a Asserção: é o funcionamento do `relationships` que viabiliza a verificação de integridade referencial descrita.
- **c.** Incorreta. A Razão é verdadeira (descreve corretamente o que o `relationships` do dbt faz).
- **d.** Incorreta. A Asserção é verdadeira (o `relationships` de fato cobre a integridade referencial de forma barata).
- **e.** Incorreta. Ambas são verdadeiras.

### Questão 22

- **a.** Incorreta. A Razão não justifica a Asserção — na verdade ela a **contradiz**.
- **b.** *Correta!* As duas proposições são verdadeiras: o `olist.duckdb` e os Parquet do `gold/` de fato ficam no `.gitignore` (são dado, não código). Porém a Razão é uma afirmação verdadeira e **independente** apenas em parte — o DataOps versiona dado e código, mas **não** da mesma forma nem no mesmo mecanismo (código no Git; dado com DVC/lakeFS/*time travel*). Assim, a Razão não é a justificativa correta da Asserção. *(Observação: a Asserção decorre justamente de dado e código terem versionamento distinto — o oposto do que a Razão sugere.)*
- **c.** Incorreta. A Razão, tomada isoladamente, contém a afirmação verdadeira de que o DataOps versiona ambos, ainda que por mecanismos distintos.
- **d.** Incorreta. A Asserção é verdadeira (dado não vai para o Git no projeto Olist).
- **e.** Incorreta. A Asserção é verdadeira.

### Questão 23

- **a.** Incorreta. A Razão não justifica a Asserção, pois a Asserção é falsa.
- **b.** Incorreta. A Asserção é falsa.
- **c.** *Correta!* A Asserção é falsa: assinar contratos com a nuvem e pagar a fatura não é papel do **data steward**, mas da operação/custodian e da gestão. A Razão é verdadeira: o data steward zela pelo **significado** de cada campo (ex.: `customer_id` vs `customer_unique_id`), garantindo consistência semântica.
- **d.** Incorreta. A Razão é verdadeira, mas a Asserção é falsa (inverte-se a análise).
- **e.** Incorreta. A Razão é verdadeira.

### Questão 24

- **a.** Incorreta. A Asserção é falsa.
- **b.** Incorreta. A Asserção é falsa.
- **c.** Incorreta. A Razão é verdadeira.
- **d.** *Correta!* A Asserção é falsa: a **minimização** da LGPD exige coletar **apenas o necessário**, não "o máximo possível" — mais dado guardado é mais superfície de risco, não mais segurança. A Razão é verdadeira: a **retenção** define por quanto tempo cada tabela com PII é mantida, apoiada na ideia de que dado que não se guarda é dado que não vaza.
- **e.** Incorreta. A Razão é verdadeira.

### Questão 25

- **a.** Incorreta. Ambas são falsas.
- **b.** Incorreta. Ambas são falsas.
- **c.** Incorreta. A Razão também é falsa.
- **d.** Incorreta. A Asserção também é falsa.
- **e.** *Correta!* As duas proposições são falsas. O **RBAC** concede permissões **por papel** (analista de marketing, cientista, custodian), **não** individualmente por pessoa; e o **menor privilégio** determina conceder o **mínimo** de acesso necessário — o schema `raw` fica restrito ao engenheiro custodian, jamais liberado a qualquer analista.

### Questão 26

- **a.** *Correta!* Ambas verdadeiras e a II justifica a I. O `dbt build` executa `run` + `test` numa tacada (Razão), o que **é a causa** de um único comando no PR cobrir construção e testes de qualidade (Asserção) e bloquear o merge quando algo falha.
- **b.** Incorreta. A Razão justifica diretamente a Asserção (é o `run` + `test` do build que produz a cobertura descrita).
- **c.** Incorreta. A Razão é verdadeira (o `dbt build` realmente combina `run` e `test`).
- **d.** Incorreta. A Asserção é verdadeira.
- **e.** Incorreta. Ambas são verdadeiras.

### Questão 27

- **a.** Incorreta. A Razão não justifica a Asserção — troca de target no dbt e fiscalização da LGPD pela ANPD são temas independentes.
- **b.** *Correta!* As duas proposições são individualmente verdadeiras: promover `dev → prod` no dbt é apenas trocar o **target** no `profiles.yml` (mesmos modelos, banco diferente), e a LGPD de fato é fiscalizada pela ANPD e garante o direito de eliminação. Mas a Razão (LGPD/ANPD) **não explica** a mecânica de targets do dbt — são fatos verdadeiros sem relação de causa.
- **c.** Incorreta. A Razão é verdadeira.
- **d.** Incorreta. A Asserção é verdadeira.
- **e.** Incorreta. Ambas são verdadeiras.

### Questão 28

- **a.** Incorreta. A Razão é falsa.
- **b.** Incorreta. A Razão é falsa.
- **c.** *Correta!* A Asserção é verdadeira: a **acurácia** (o dado refletir a realidade) é a dimensão que flagra "entrega antes da compra". A Razão é falsa: verificar se `order_id` aparece uma única vez é **unicidade**, não acurácia — e a acurácia tem, sim, relação com a coerência entre datas de um pedido.
- **d.** Incorreta. A Asserção é verdadeira.
- **e.** Incorreta. A Asserção é verdadeira.

### Questão 29

- **a.** Incorreta. A Asserção é falsa.
- **b.** Incorreta. A Asserção é falsa.
- **c.** Incorreta. A Razão é verdadeira.
- **d.** *Correta!* A Asserção é falsa: a *view* do dbt e a feature store gerenciada **não** são conceitos sem relação — no projeto local a *view* **é** a feature store, com o mesmo propósito. A Razão descreve corretamente que o conceito é o mesmo: servir a mesma lógica de *features* (prazo estimado, frete, itens, categoria, UF, parcelas) para treino e produção.
- **e.** Incorreta. A Razão é verdadeira.

### Questão 30

- **a.** Incorreta. Ambas são falsas.
- **b.** Incorreta. Ambas são falsas.
- **c.** Incorreta. A Razão também é falsa.
- **d.** Incorreta. A Asserção também é falsa.
- **e.** *Correta!* As duas proposições são falsas. A **completude** importa, sim: pedidos sem `review` são lacunas mensuráveis que afetam análises de satisfação. E a **consistência** entre `stg_order_payments` e `fct_orders` é decisiva: um `payment_value` que não bate contamina KPIs de receita e compromete decisões de negócio.

### Questão 31

- **a.** *Correta!* Testes e observabilidade são **complementares**: os `not_null`/`unique`/`accepted_values` barram o previsto, e a observabilidade monitora volume, frescor, distribuição, esquema e linhagem ao longo do tempo, capturando o imprevisto (como a queda de 135 para 12 pedidos).
- **b.** Incorreta. A observabilidade **não** dispensa os testes; eles cobrem o previsto de forma barata, na porta do dado.
- **c.** Incorreta. Queda de **volume** não é unicidade; nenhum `unique` no `order_id` detecta poucos pedidos no dia.
- **d.** Incorreta. Não fazem a mesma coisa nem são redundantes: um pega o previsto, o outro o imprevisto.
- **e.** Incorreta. Um `not_null` verifica nulos em um campo, não o volume de linhas da tabela — são métricas distintas.

### Questão 32

- **a.** Incorreta. Manter 3 dígitos + `XX` **não** anonimiza plenamente; o dado segue no escopo da LGPD como pseudonimizado/generalizado.
- **b.** *Correta!* O mascaramento **reduz a granularidade** (3 dígitos + `XX`), aplicando defesa em profundidade e menor privilégio a quem não precisa do prefixo cheio, sem, por si só, tornar o dado plenamente anônimo.
- **c.** Incorreta. `XX` **oculta** dígitos (reduz precisão); não acrescenta informação geográfica.
- **d.** Incorreta. Mascarar parte do CEP é justamente uma boa prática de governança, não uma violação.
- **e.** Incorreta. Mascaramento e RBAC são camadas **complementares** de defesa em profundidade; um não substitui o outro.

### Questão 33

- **a.** Incorreta. Modelos a jusante **não** se corrigem sozinhos; é preciso conhecer a linhagem para remover o rastro em cada ponto.
- **b.** Incorreta. O lineage é a base técnica do direito de eliminação, não mero enfeite de documentação.
- **c.** *Correta!* O lineage é a **planta baixa da exclusão**: revela todos os modelos onde o dado do titular pousou (de `raw` ao `mart_payment_analysis`), permitindo apagar cada rastro e respondendo a impacto (a jusante) e causa-raiz (a montante).
- **d.** Incorreta. A LGPD exige, sim, rastrear todos os lugares onde o dado pessoal está; ignorar `dim_customers`/`fct_orders` deixaria rastros.
- **e.** Incorreta. Marts derivados de dado pessoal **não** deixam de ser dado pessoal automaticamente; a exclusão os alcança.

### Questão 34

- **a.** Incorreta. IaC vai muito além de economizar cliques: entrega reprodutibilidade, versionamento e revisão em PR.
- **b.** Incorreta. IaC declara a infra; não substitui nem elimina os testes de dados do pipeline.
- **c.** Incorreta. Governança e IaC são compatíveis — as políticas de acesso da Aula 14 podem ser expressas como código Terraform.
- **d.** *Correta!* A **IaC** torna a criação da infra do Olist declarativa, versionada e revisável em PR, recria ambientes idênticos em minutos e permite codificar até as políticas de acesso da governança.
- **e.** Incorreta. O versionamento e a retenção de 90 dias declarados no Terraform aplicam-se ao **bucket** de armazenamento, não ao código dbt.

### Questão 35

- **a.** Incorreta. O modelo **não** é inútil: 24% de precisão no decil de risco contra 8% de taxa-base é um ganho real (lift 3,0).
- **b.** Incorreta. *Lift* de 3,0 significa **3× melhor** que o acaso, não "3% dos atrasos" nem pior que o acaso.
- **c.** Incorreta. *Lift* mede ganho de predição sobre o acaso, não latência do pipeline.
- **d.** Incorreta. No chute a precisão seria a própria taxa-base (8%), não 24%; o modelo triplica esse desempenho.
- **e.** *Correta!* Mirando os 10% mais arriscados, a logística acha atrasos **3× mais** do que ao acaso — valor suficiente para acionar transportadora ou avisar o cliente proativamente.

### Questão 36

- **a.** *Correta!* A regra **1-10-100** mostra que o custo do defeito cresce por ordem de grandeza conforme avança no pipeline; por isso automatiza-se a verificação **onde o dado é produzido** (`schema.yml`), não onde é consumido (mart/BI).
- **b.** Incorreta. Conviver com o defeito custa **R\$ 100** — o **maior** custo, não o menor.
- **c.** Incorreta. Validar no dashboard da diretoria é o ponto **mais caro** (consumidor final); a validação deve ocorrer na produção do dado.
- **d.** Incorreta. Escrever o `accepted_values` (R\$ 1) é muito **mais barato** que corrigir depois (R\$ 10) ou conviver (R\$ 100).
- **e.** Incorreta. A regra 1-10-100 trata do **custo de defeitos** ao longo do pipeline, não de latência/frescor.

### Questão 37

- **a.** Incorreta. MLOps **não** substitui qualidade, lineage e CI/CD — apoia-se neles como fundação.
- **b.** *Correta!* MLOps **estende** o DataOps ao ciclo do modelo (versiona também o modelo, monitora *data/model drift*), sobre a base de qualidade, lineage e CI/CD já construída, que é pré-requisito.
- **c.** Incorreta. MLOps versiona dado, código **e** modelo — não apenas código.
- **d.** Incorreta. *Drift* é mudança na distribuição dos dados/desempenho do modelo, não um problema de infraestrutura resolvido com Terraform.
- **e.** Incorreta. MLOps exige treino **reproduzível**; reexecutar um notebook manualmente é o oposto de reprodutibilidade.

### Questão 38

- **a.** Incorreta. O lineage do dbt vive **dentro do projeto**; não cobre metadados e linhagem entre **todos** os times e ferramentas da organização.
- **b.** Incorreta. Planilha manual heterogênea não escala nem padroniza a governança entre times.
- **c.** *Correta!* A escala organizacional pede um **catálogo de dados** dedicado (DataHub, open source, ou Atlan, comercial), que centraliza metadados, dicionário de dados e linhagem ponta a ponta, catalogando e classificando PII como o `customer_unique_id`.
- **d.** Incorreta. Catálogos existem justamente para governar **múltiplos** times; desligar a governança em escala é o contrário do necessário.
- **e.** Incorreta. Um `not_null` verifica ausência de nulos; não classifica PII nem centraliza metadados entre times.

### Questão 39

- **a.** Incorreta. Multa **não** é o único custo relevante; notificação e *churn* somam mais que a própria multa.
- **b.** Incorreta. Prevenir (~R\$ 60 mil) é **muito menor** que o impacto (~R\$ 3,1 mi), logo economicamente justificável.
- **c.** Incorreta. O teto de R\$ 50 mi é o **limite máximo** por infração; aqui o teto percentual (2% de R\$ 80 mi) resulta em R\$ 1,6 milhão.
- **d.** *Correta!* O impacto no 1º ano soma $\approx \text{R\$}\,3{,}1$ milhões e a prevenção $\approx \text{R\$}\,60$ mil; a **multa é a menor das parcelas** e prevenir na origem (como o Olist já faz ao pseudonimizar) é ordens de grandeza mais barato.
- **e.** Incorreta. A pseudonimização reduz o risco, mas o cálculo de impacto ilustra o custo de **não** tê-la; ela não torna qualquer vazamento inconsequente.

### Questão 40

- **a.** Incorreta. O medo não é falta de coragem individual, e sim sintoma de falta de processo.
- **b.** Incorreta. Proibir merges às sextas **reduz** a frequência de deploy — o oposto da meta DORA e da cura do DataOps.
- **c.** Incorreta. Alterar o `fct_order_items` **pode**, sim, quebrar marts a jusante como o `mart_seller_scorecard`; por isso o medo existe.
- **d.** Incorreta. Versionar o `olist.duckdb` no Git é justamente o que **não** se deve fazer (dado vai para o `.gitignore`); não é a cura do medo.
- **e.** *Correta!* O medo é sintoma de **falta de processo**, curado por DataOps (CI com `dbt build`, *staging*, `dbt test`, WAP): numa equipe madura, merge no `fct_order_items` na sexta às 17h é **rotina, não coragem**.
