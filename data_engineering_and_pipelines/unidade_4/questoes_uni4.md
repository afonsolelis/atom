# Questionário — Unidade 4

- **Disciplina:** Data Engineering and Pipelines
- **Professor-conteudista:** Afonso Cesar Lelis Brandão

## Orientações

- **20 questões** padrão ENADE: **10 asserção-razão** + **10 de interpretação**.
- Cada questão tem **5 alternativas (a–e)**; a correta é prefixada por `*` (ex.: `*c. ...`).
- Distribuição da alternativa correta: rotação **a, b, c, d, e, a, b, c, d, e...** (4 questões para cada letra).

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
