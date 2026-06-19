# Unidade 4 — Qualidade, Governança e DataOps

- **Disciplina:** Data Engineering and Pipelines
- **Conteudista:** Afonso Cesar Lelis Brandão
- **Videoaulas desta unidade:** 13 a 16

## Aula 13 — Qualidade e observabilidade de dados

Um pipeline que move terabytes por dia, mas entrega números errados, é pior do que pipeline nenhum: ele dá **confiança falsa**. Decisões são tomadas, relatórios são assinados, modelos são treinados — tudo sobre areia. Nas três primeiras unidades você aprendeu a **mover** o dado (ingestão, armazenamento, transformação, orquestração). Esta unidade muda o foco: como garantir que o dado movido é **confiável**, **governado** e **operável**. Começamos pelo alicerce de tudo — **qualidade e observabilidade de dados**. A pergunta-guia da aula é simples e brutal: *como você sabe, sem ninguém te avisar, que o dado de hoje está certo?*

### As dimensões da qualidade de dados

Qualidade de dados não é "achismo": é mensurável por **dimensões** padronizadas. As seis clássicas (modelo DAMA-DMBOK) são:

- **Completude (completeness):** faltam valores? Que percentual de campos obrigatórios está nulo?
- **Acurácia (accuracy):** o dado reflete a realidade? Um CEP existe de fato?
- **Consistência (consistency):** o mesmo fato aparece igual em fontes diferentes? O total de vendas no ERP bate com o do data warehouse?
- **Unicidade (uniqueness):** há registros duplicados? Quantos clientes têm o mesmo CPF?
- **Validade (validity):** o dado respeita o formato/regra esperada? Datas em `YYYY-MM-DD`, valores positivos onde deveriam ser?
- **Pontualidade (timeliness):** o dado chegou a tempo de ser útil? O batch das 6h rodou às 6h ou às 11h?

Cada dimensão vira **métrica numérica** e **threshold** (limiar) acordado com o negócio. Não existe "100% de qualidade" — existe qualidade **suficiente para a decisão** que o dado vai sustentar.

![Ciclo PDCA aplicado à melhoria contínua da qualidade de dados](https://commons.wikimedia.org/wiki/Special:FilePath/PDCA_Cycle.svg)

### Testes de dados e contratos de dados

Há duas armas complementares contra dado ruim. A primeira são os **testes de dados**: asserções automáticas que rodam **dentro do pipeline** (`coluna X nunca é nula`, `valor entre 0 e 1`, `chave única`). Falhou o teste, o pipeline para — melhor barrar o lixo na porta do que limpá-lo no relatório.

A segunda é o **contrato de dados (data contract)**: um acordo **formal e versionado** entre quem **produz** e quem **consome** o dado. O contrato declara schema (nomes, tipos), regras de qualidade (SLAs de completude, frescor), semântica (o que cada campo significa) e política de versionamento (como o produtor sinaliza uma mudança que quebra o consumidor). Em arquiteturas modernas (Data Mesh), o contrato é o que torna o **dado um produto**: o time produtor assume responsabilidade pública pelo que entrega. Sem contrato, toda mudança de schema no sistema-fonte vira incêndio silencioso a jusante.

### Data observability: os 5 pilares

**Observabilidade de dados** é a capacidade de **entender a saúde do dado em produção** por sinais que o próprio sistema emite — inspirada na observabilidade de software (logs, métricas, traces). O modelo popularizado por Barr Moses (Monte Carlo) define **5 pilares**:

1. **Frescor (freshness):** o dado está atualizado? Quando a tabela foi escrita pela última vez?
2. **Volume:** o número de linhas está dentro do esperado? Caiu de 1 milhão para 12 mil?
3. **Distribuição (schema/values):** os valores estão na faixa normal? Apareceu `-1` num campo de idade?
4. **Esquema (schema):** a estrutura mudou? Uma coluna sumiu, um tipo virou texto?
5. **Linhagem (lineage):** se uma tabela quebrou, **quais relatórios e modelos** dependem dela? Quem avisar?

A diferença entre teste e observabilidade: o **teste** verifica regras que você **antecipou**; a **observabilidade** detecta o que você **não previu**, monitorando o comportamento estatístico ao longo do tempo.

### Detecção de anomalias e data downtime

**Data downtime** é o período em que o dado está ausente, errado ou parcial — e o custo dele é exatamente análogo ao *downtime* de um sistema. A fórmula prática de Monte Carlo:

$$
\text{Data downtime} = \text{N.\,de incidentes} \times (\text{TTD} + \text{TTR})
$$

onde **TTD** é o *time to detection* (quanto leva para descobrir) e **TTR** é o *time to resolution* (quanto leva para corrigir). Observabilidade ataca diretamente o **TTD**: em vez de o diretor financeiro descobrir o erro na reunião, um alerta dispara minutos após a anomalia. A **detecção de anomalias** automatiza isso comparando a métrica de hoje com a faixa histórica esperada (média móvel, desvio-padrão, modelos sazonais), disparando alerta quando o valor escapa do envelope.

### Ferramentas (Great Expectations, dbt tests)

| Ferramenta | O que faz | Quando usar |
| --- | --- | --- |
| **dbt tests** | Testes declarativos no `schema.yml` (`not_null`, `unique`, `accepted_values`, `relationships`) + testes SQL customizados | Já usa dbt para transformar; quer testes baratos junto do modelo |
| **Great Expectations** | Suítes de "expectativas" reutilizáveis, *data docs* automáticos, validação em qualquer ponto do pipeline | Validação rica, fora ou dentro do dbt, com documentação para auditoria |
| **Soda / Elementary** | Checks declarativos (YAML/SoQL) e monitoração de anomalias sobre o dbt | Observabilidade contínua com pouco código |
| **Monte Carlo / Bigeye** | Observabilidade gerenciada (5 pilares + ML de anomalia + linhagem) | Operação grande, muitas tabelas, equipe enxuta |

Um teste dbt típico cabe em três linhas de YAML; uma *expectation* do Great Expectations como `expect_column_values_to_be_between(min=0, max=1)` documenta a regra e gera evidência. O princípio: **automatize a verificação onde o dado é produzido**, não onde ele é consumido.

### Exemplo numérico: o custo do dado ruim

Uma fintech roda análise de risco de crédito sobre uma tabela de score. Um campo de renda mensal começou a chegar **em centavos** (multiplicado por 100) após uma mudança não comunicada no sistema-fonte — um problema de **validade**.

- **Sem observabilidade:** o erro passou despercebido por 9 dias. Nesse período, $4\,200$ propostas foram aprovadas com limite indevido. A inadimplência adicional gerou perda média de R\$ 380 por proposta defeituosa, das quais cerca de 6% viraram prejuízo: $4\,200 \times 0{,}06 \times \text{R\$}\,380 = \text{R\$}\,95\,760$.
- **TTD sem monitoração:** $9$ dias. **TTR:** $1$ dia. Data downtime do incidente: $1 \times (9 + 1) = 10$ dias de dado comprometido.
- **Com observabilidade:** um teste de validade (renda entre R\$ 500 e R\$ 200 mil) barraria o lote no primeiro dia. TTD cai para $0{,}1$ dia; o prejuízo evitável seria $\approx 90\%$ do total, ou seja $\approx \text{R\$}\,86\,000$ poupados.
- **Custo da prevenção:** 3 horas de um(a) engenheiro(a) (R\$ 120/h) para escrever os testes $=$ R\$ 360. **Retorno: cerca de 240×** no primeiro incidente evitado.

A lição numérica é clássica em qualidade: a **regra 1-10-100** — custa R\$ 1 prevenir, R\$ 10 corrigir e R\$ 100 conviver com o dado ruim em produção.

### Atividade prática

Escolha uma tabela real (ou um CSV) que você conheça e construa um **mini-cartão de qualidade**:

1. Liste as **6 dimensões** e, para cada uma, escreva **uma regra mensurável** aplicável à tabela (ex.: "completude: coluna `email` < 2% de nulos").
2. Para 3 dessas regras, escreva o **teste dbt** (`not_null`, `unique`, `accepted_values`) ou a *expectation* equivalente do Great Expectations.
3. Defina o **threshold** de cada regra e o que deve acontecer ao falhar (parar o pipeline? alertar e seguir?).
4. Estime o **TTD atual** desse dado: se ele estivesse errado hoje, quanto tempo levaria até alguém perceber?

### Pontos-chave

- Qualidade de dados é **mensurável** por 6 dimensões: completude, acurácia, consistência, unicidade, validade e pontualidade.
- **Testes** verificam regras antecipadas dentro do pipeline; **observabilidade** detecta o imprevisto monitorando o comportamento ao longo do tempo.
- Os **5 pilares** de observabilidade são frescor, volume, distribuição, esquema e linhagem.
- **Data contracts** transferem responsabilidade pelo schema para quem produz o dado, evitando quebras silenciosas a jusante.
- **Data downtime $=$ N.\ de incidentes $\times$ (TTD $+$ TTR)**; observabilidade ataca o TTD, e a regra 1-10-100 mostra que prevenir é o mais barato.

### Para saber mais

- **Great Expectations — documentação oficial:** https://docs.greatexpectations.io/
- **dbt — Tests:** https://docs.getdbt.com/docs/build/data-tests
- **Barr Moses — "What is Data Observability?" (Monte Carlo blog):** https://www.montecarlodata.com/blog-what-is-data-observability/
- **DAMA-DMBOK — Data Quality (Wikipedia):** https://en.wikipedia.org/wiki/Data_quality

## Aula 13 — Roteiro da Videoaula 13: "Qualidade e observabilidade de dados"

### 1. Abertura (0:00 – 0:40)

> "Imagina que o relatório de faturamento de hoje veio com um zero a mais. Ninguém percebeu. A diretoria decidiu com base nele. Quem é o culpado? Spoiler: não foi o dado — foi a **ausência de monitoração**. Hoje a gente fecha o circuito: aprendemos a mover dado nas unidades anteriores, agora vamos garantir que o dado movido é **confiável**. Bem-vindo à Unidade 4."

### 2. Desenvolvimento — parte 1 (0:40 – 4:00)

> "Qualidade de dados não é achismo, é número. Existem seis dimensões clássicas: completude, acurácia, consistência, unicidade, validade e pontualidade. Cada uma vira uma métrica e um limiar. Repara: ninguém busca 100% de qualidade — a gente busca qualidade **suficiente para a decisão**. E o jeito de defender essa qualidade é com duas armas: o **teste de dados**, que roda dentro do pipeline e barra o lixo na porta, e o **contrato de dados**, que é um acordo formal e versionado entre quem produz e quem consome. Sem contrato, qualquer mudança de schema lá na origem vira incêndio aqui na ponta."

### 3. Desenvolvimento — parte 2 (4:00 – 7:00)

> "Teste verifica o que você previu. Mas e o que você **não** previu? Aí entra a observabilidade de dados, com cinco pilares: frescor — o dado está atualizado?; volume — o número de linhas faz sentido?; distribuição — os valores estão na faixa normal?; esquema — a estrutura mudou?; e linhagem — se essa tabela quebrar, quem depende dela? A observabilidade detecta anomalia comparando o hoje com o histórico, e dispara alerta antes de o problema chegar no relatório."

### 4. Desenvolvimento — parte 3 (7:00 – 9:00)

> "Vamos colocar preço nisso. Data downtime é igual a número de incidentes vezes a soma do tempo pra detectar mais o tempo pra resolver. Numa fintech, um campo de renda chegou multiplicado por cem e ninguém viu por nove dias — quase R\$ 96 mil de prejuízo. Um teste de validade de três horas de trabalho teria barrado o lote no primeiro dia. Retorno de 240 vezes. É a regra 1-10-100: R\$ 1 pra prevenir, R\$ 10 pra corrigir, R\$ 100 pra conviver. Na prática, você usa dbt tests pra regra barata junto do modelo, Great Expectations pra validação rica com documentação, e plataformas como Monte Carlo quando a operação é grande."

### 5. Encerramento (9:00 – 11:00)

> "Resumo: qualidade é mensurável em seis dimensões; teste cobre o previsto e observabilidade cobre o imprevisto, com os cinco pilares; e tudo isso se paga com folga no primeiro incidente evitado. Tarefa: pegue uma tabela que você conhece e monte um cartão de qualidade com uma regra por dimensão. Na próxima aula a gente sobe um nível: dado confiável também precisa ser dado **governado e seguro** — entramos em governança e LGPD em pipelines. Te vejo lá."

---

## Aula 14 — Governança, segurança e LGPD em pipelines

Dado confiável que vaza, ou que ninguém sabe onde está, é um passivo. Na Aula 13 garantimos que o dado está **certo**; agora garantimos que ele está **sob controle**: quem pode vê-lo, de onde ele veio, por quanto tempo fica guardado e como tratá-lo dentro da lei. Esta aula conecta engenharia de dados a um tema que virou inegociável no Brasil desde 2020 — a **LGPD**. Um *data breach* hoje não é só problema de TI: é manchete, multa e perda de confiança do cliente. A boa notícia: governança bem-feita não trava o pipeline, ela o torna **defensável**.

### O que é governança de dados

**Governança de dados** é o conjunto de **políticas, papéis, processos e métricas** que define como o dado é tratado em toda a organização. Ela responde a perguntas estruturais: *Quem é dono de cada dado? Quem pode acessar o quê? Como classificamos o que é sensível? Quanto tempo guardamos? Como provamos conformidade a um auditor?*

Os papéis-chave são o **data owner** (responsável de negócio por um domínio de dados — ex.: o diretor de RH é dono dos dados de funcionários), o **data steward** (zelador operacional da qualidade e do significado) e o **data custodian** (o time técnico que opera a infraestrutura). Governança é menos sobre tecnologia e mais sobre **responsabilidade clara**: sem dono, ninguém responde pelo dado.

![Cadeado simbolizando segurança, privacidade e governança de dados (LGPD)](https://commons.wikimedia.org/wiki/Special:FilePath/Padlock.svg)

### Catálogo de dados e linhagem (lineage)

Não dá para governar o que não se enxerga. O **catálogo de dados** é o "Google interno" dos dados: um inventário pesquisável de todas as tabelas, com schema, descrição de campos, dono, classificação de sensibilidade e estatísticas de uso. Ferramentas como **DataHub**, **OpenMetadata**, **Amundsen** e **Apache Atlas** automatizam isso.

A **linhagem (data lineage)** mapeia o **fluxo do dado**: de qual fonte ele veio, por quais transformações passou e em quais dashboards/modelos termina. Linhagem responde a duas perguntas críticas e opostas: a *jusante* — "se eu mudar esta coluna, o que quebra?" (análise de impacto) — e a *montante* — "este número estranho no relatório, de onde ele saiu?" (análise de causa-raiz). É também requisito de conformidade: para atender um pedido de exclusão da LGPD, você precisa saber **todos os lugares** onde um dado pessoal pousou.

### Controle de acesso e mascaramento

O princípio fundamental é o do **menor privilégio**: cada pessoa ou serviço acessa **apenas** o dado necessário para sua função. Os mecanismos principais:

- **RBAC (Role-Based Access Control):** permissões atreladas a papéis (analista, engenheiro, executivo), não a indivíduos.
- **Controle por coluna e por linha (column/row-level security):** o analista de SP vê só as linhas de SP; o estagiário vê a tabela, mas não a coluna salário.
- **Mascaramento (data masking):** exibir `***.456.789-**` em vez do CPF completo para quem não precisa do valor real.
- **Tokenização e criptografia:** substituir o dado sensível por um *token* reversível só com chave (tokenização) ou cifrar em repouso e em trânsito (criptografia).
- **Anonimização e pseudonimização:** remover ou substituir identificadores para que o titular não seja (re)identificável.

A distinção LGPD importa: **dado anonimizado** sai do escopo da lei (não é mais dado pessoal); **dado pseudonimizado** continua dentro, porque a reidentificação ainda é possível com a chave.

### LGPD aplicada a pipelines de dados

A **Lei Geral de Proteção de Dados (Lei 13.709/2018)** rege o tratamento de dados pessoais no Brasil, fiscalizada pela **ANPD**. Para o pipeline, os pontos práticos são:

- **Base legal:** todo tratamento precisa de uma das 10 bases legais (consentimento, execução de contrato, obrigação legal, legítimo interesse etc.). O pipeline deve saber **por que** processa cada dado.
- **Minimização:** só colete e armazene o que for necessário ao propósito. Ingerir a base inteira "por garantia" é violação.
- **Direitos do titular:** acesso, correção, portabilidade e **eliminação**. Seu pipeline precisa de um caminho técnico para *deletar* todos os rastros de um titular — o que exige linhagem.
- **Dados sensíveis:** saúde, biometria, raça, orientação, opinião política exigem proteção reforçada.
- **Registro e *Data Protection Impact Assessment* (relatório de impacto):** documentar fluxos de dados pessoais é exigência da lei.

Engenharia de dados materializa a lei: **classificar** campos pessoais no catálogo, **mascarar** por padrão, **registrar** linhagem e **automatizar** a exclusão são tarefas do pipeline, não do jurídico.

### Retenção e ciclo de vida do dado

Dado não é vinho: não melhora parado. Toda tabela com dado pessoal precisa de uma **política de retenção** que define por quanto tempo é guardado e o que acontece depois (exclusão, anonimização ou arquivamento frio). O **ciclo de vida** vai de criação $\rightarrow$ uso ativo (*hot*) $\rightarrow$ acesso esporádico (*warm*) $\rightarrow$ arquivo (*cold*) $\rightarrow$ exclusão. Além da conformidade, retenção bem definida **reduz custo de armazenamento** e **diminui a superfície de ataque**: dado que você não guarda é dado que não vaza. Políticas de *lifecycle* em data lakes (mover para camadas mais baratas após N dias, expirar após M anos) automatizam o ciclo.

### Exemplo numérico: risco e multa

Uma empresa de e-commerce de médio porte sofre um vazamento por um *bucket* de dados mal configurado, expondo dados de clientes.

- **Faturamento anual no Brasil:** R\$ 80.000.000,00.
- **Multa LGPD:** a sanção é de até **2% do faturamento**, limitada a **R\$ 50 milhões por infração**. No teto percentual: $0{,}02 \times \text{R\$}\,80\,\text{milhões} = \text{R\$}\,1\,600\,000$.
- **Custo de notificação e remediação:** $1\,500\,000$ titulares afetados, com custo médio de resposta a incidente estimado em R\$ 9,00 por titular (notificação, suporte, monitoramento de crédito) $= \text{R\$}\,13\,500\,000$.
- **Perda de receita por *churn*:** estima-se 3% de evasão de clientes pós-vazamento; com receita média de R\$ 220/cliente/ano sobre 600 mil clientes ativos, $0{,}03 \times 600\,000 \times \text{R\$}\,220 = \text{R\$}\,3\,960\,000$/ano.
- **Impacto total no primeiro ano:** $1{,}6 + 13{,}5 + 3{,}96 \approx \text{R\$}\,19\,060\,000$.
- **Prevenção:** revisão de permissões de *bucket*, mascaramento e auditoria $\approx$ R\$ 60 mil. **A multa sozinha já é $\approx 27\times$ o custo de prevenir.**

A multa, repare, é a **menor** das parcelas — o estrago de reputação e *churn* costuma superar a sanção da ANPD.

### Atividade prática

Para um pipeline que você conheça (ou o do exemplo):

1. **Classifique** os campos em: público, interno, confidencial e **dado pessoal/sensível** (LGPD).
2. Para cada campo pessoal, defina a **base legal** plausível e a **estratégia de proteção** (mascaramento, tokenização, criptografia).
3. Desenhe o **caminho técnico de exclusão** de um titular: liste todas as tabelas onde o dado dele pousaria (use o raciocínio de linhagem).
4. Escreva uma **política de retenção** de uma frase para cada tabela sensível (ex.: "logs de acesso: 12 meses, depois anonimizar").

### Pontos-chave

- **Governança** define políticas, papéis (owner, steward, custodian) e processos; sem dono, ninguém responde pelo dado.
- **Catálogo** torna o dado descobrível; **linhagem** habilita análise de impacto, causa-raiz e a exclusão exigida pela LGPD.
- **Menor privilégio** + RBAC + mascaramento + criptografia formam a base do controle de acesso; **anonimizar** tira o dado do escopo da LGPD, **pseudonimizar** não.
- A **LGPD** exige base legal, minimização, atendimento a direitos do titular e retenção definida — e a engenharia de dados é quem materializa isso no pipeline.
- A **multa** chega a 2% do faturamento (teto R\$ 50 mi/infração), mas reputação e *churn* costumam custar muito mais; prevenir é ordens de grandeza mais barato.

### Para saber mais

- **LGPD — texto oficial (Lei 13.709/2018, Planalto):** https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm
- **ANPD — Autoridade Nacional de Proteção de Dados (gov.br):** https://www.gov.br/anpd/pt-br
- **DataHub — catálogo e linhagem de dados (open source):** https://datahubproject.io/
- **Governança de dados (Wikipedia):** https://pt.wikipedia.org/wiki/Governan%C3%A7a_de_dados

## Aula 14 — Roteiro da Videoaula 14: "Governança, segurança e LGPD em pipelines"

### 1. Abertura (0:00 – 0:40)

> "Dado certo que vaza é manchete. Dado certo que ninguém sabe onde está é passivo. Na aula passada a gente garantiu que o dado está correto; hoje a gente garante que ele está **sob controle** — quem vê, de onde veio, quanto tempo fica e como tratar dentro da lei. E no Brasil, a partir de 2020, isso tem nome: LGPD."

### 2. Desenvolvimento — parte 1 (0:40 – 4:00)

> "Governança não é tecnologia, é responsabilidade clara. Tem três papéis: o data owner, dono de negócio do dado; o data steward, zelador da qualidade e do significado; e o data custodian, o time técnico que opera. Pra governar, você precisa enxergar — e aí entram duas ferramentas. O **catálogo** é o Google interno dos dados: inventário pesquisável com schema, dono e classificação. E a **linhagem** mostra o caminho do dado: de onde veio, por onde passou, onde termina. Linhagem responde duas perguntas opostas: se eu mudar isso, o que quebra? E: esse número estranho, de onde saiu?"

### 3. Desenvolvimento — parte 2 (4:00 – 7:00)

> "Segurança começa no menor privilégio: cada um acessa só o que precisa. Isso vira RBAC por papel, controle por coluna e por linha, e mascaramento — o estagiário vê a tabela mas não vê o salário, vê o CPF com asterisco. Pra LGPD tem uma distinção que vale ouro: dado **anonimizado** sai da lei, porque não dá pra reidentificar; dado **pseudonimizado** continua na lei, porque com a chave dá. A própria LGPD exige base legal pra cada tratamento, minimização — só colete o necessário — e um caminho técnico pra deletar todos os rastros de um titular. E olha: pra deletar tudo, você precisa de linhagem. Tudo se conecta."

### 4. Desenvolvimento — parte 3 (7:00 – 9:00)

> "Quanto custa errar? E-commerce com R\$ 80 milhões de faturamento, bucket mal configurado, vaza. A multa é até 2% do faturamento: R\$ 1,6 milhão. Notificar 1,5 milhão de clientes: R\$ 13,5 milhões. Churn de 3%: quase R\$ 4 milhões por ano. Total no primeiro ano: cerca de R\$ 19 milhões. Prevenir — revisar permissão, mascarar, auditar — custava R\$ 60 mil. Repara: a multa é a **menor** parcela; o estrago de reputação é o que dói."

### 5. Encerramento (9:00 – 11:00)

> "Recapitulando: governança é dono, catálogo e linhagem; segurança é menor privilégio, mascaramento e criptografia; LGPD é base legal, minimização, direitos do titular e retenção — e quem materializa tudo isso no pipeline é você, engenheiro de dados. Tarefa: classifique os campos de um pipeline em público, interno, confidencial e pessoal, e desenhe o caminho de exclusão de um titular. Na próxima aula a gente entra na cultura que faz tudo isso rodar de forma confiável e repetível: DataOps e CI/CD para pipelines."

---

## Aula 15 — DataOps e CI/CD para pipelines de dados

Você já tem pipeline confiável (Aula 13) e governado (Aula 14). Falta o último ingrediente para virar **operação profissional**: a capacidade de **mudar o pipeline com segurança e frequência**, sem rezar a cada deploy. Pipelines de produção evoluem toda semana — nova fonte, nova regra de negócio, correção de bug. Se cada mudança é manual, arriscada e dolorosa, a equipe trava por medo. **DataOps** importa as práticas de DevOps — automação, testes, integração contínua — para o mundo dos dados. Esta é a aula que separa o script de notebook bagunçado do pipeline industrial.

### DataOps: princípios

**DataOps** é uma metodologia que aplica princípios ágeis e de DevOps ao ciclo de vida do dado, com o objetivo de entregar dado **confiável e rápido**. Os pilares:

- **Automação ponta a ponta:** do código ao deploy, sem passos manuais propensos a erro.
- **Testes em toda etapa:** testa-se o **código** (lógica de transformação) **e** o **dado** (qualidade do resultado).
- **Colaboração:** engenheiros, analistas e cientistas trabalham no mesmo fluxo versionado.
- **Monitoração e feedback contínuos:** observabilidade (Aula 13) fecha o *loop*.
- **Iteração rápida:** mudanças pequenas e frequentes, em vez de grandes lançamentos arriscados.

A métrica-norte do DataOps é a mesma do DevOps de elite (estudo DORA): **frequência de deploy alta** com **baixa taxa de falha de mudança**. Entregar pouco e seguro, muitas vezes.

![Ciclo contínuo de integração e entrega representando o fluxo DevOps/DataOps de código a operação](https://commons.wikimedia.org/wiki/Special:FilePath/Devops-toolchain.svg)

### Versionamento de código e de dados

Em DataOps versiona-se **duas coisas**. O **código** vai para Git como qualquer software: scripts de transformação, modelos dbt, DAGs do Airflow, IaC — tudo com *branches*, *pull requests* e revisão por pares. Isso dá histórico, rollback e colaboração.

Mas dado também muda, e aí entra o **versionamento de dados**. Ferramentas como **DVC** (Git para datasets/modelos de ML), **lakeFS** (Git para o data lake inteiro, com *branch* e *merge* de dados) e o *time travel* de formatos como **Delta Lake**, **Apache Iceberg** e **Apache Hudi** permitem consultar o dado "como ele estava ontem". Versionar dado habilita reprodutibilidade (treinar o modelo com o snapshot exato de uma data), testes seguros (criar um *branch* do lake, testar a transformação, descartar) e auditoria.

### Testes automatizados de pipeline

A pirâmide de testes de software ganha uma camada de dados:

| Nível | O que testa | Exemplo |
| --- | --- | --- |
| **Unitário** | Uma função de transformação isolada | `normaliza_cpf("123.456.789-00")` retorna `12345678900` |
| **Integração** | Componentes juntos | A DAG lê do S3, transforma e escreve no warehouse |
| **De dados** | Qualidade do resultado (Aula 13) | `not_null`, `unique`, distribuição dentro da faixa |
| **End-to-end** | Pipeline completo num ambiente de staging | Dados sintéticos entram, números esperados saem |

A regra de ouro: rode os testes **antes** do deploy, em ambiente isolado, com **dados sintéticos ou amostrados** — nunca a primeira validação em produção.

### CI/CD e deploy de pipelines

**CI/CD** automatiza a ponte do código ao ambiente. A **Integração Contínua (CI)** dispara a cada *push*: linter, testes unitários, testes dbt, *build*. Se algo falha, o *merge* é bloqueado — o erro morre no *pull request*, não em produção. A **Entrega/Implantação Contínua (CD)** promove o que passou para os ambientes em sequência:

$$
\text{dev} \;\rightarrow\; \text{staging} \;\rightarrow\; \text{produção}
$$

Ferramentas comuns: **GitHub Actions**, **GitLab CI**, **Jenkins**. Estratégias para reduzir risco do deploy de dados incluem *blue-green* (dois ambientes idênticos, troca de tráfego instantânea) e o **write-audit-publish (WAP)**: escreve numa tabela temporária, **audita** com testes de qualidade e só **publica** (promove) se passar — assim o consumidor nunca vê dado intermediário quebrado.

### Infraestrutura como código (IaC)

Clicar no console da nuvem para criar buckets, clusters e permissões é frágil, não documentado e impossível de reproduzir. **Infraestrutura como Código (IaC)** declara a infraestrutura em arquivos versionados. Com **Terraform** (multi-nuvem, declarativo), **Pulumi** (IaC em linguagem de programação) ou **CloudFormation** (AWS), você escreve "quero um bucket S3 com versionamento e retenção de 90 dias" e a ferramenta aplica e mantém esse estado. Benefícios: ambientes idênticos (dev = staging = prod), recriação em minutos após desastre, e a própria configuração de governança (políticas de acesso, retenção da Aula 14) virando código revisável.

### Exemplo numérico: frequência de deploy

Uma equipe de dados migra de processo manual para CI/CD.

- **Antes (manual):** $2$ deploys/mês. Cada deploy consome $4$ h de engenheiro (R\$ 120/h) $= \text{R\$}\,480$ por deploy. Taxa de falha de mudança (*change failure rate*) de $30\%$: $0{,}30 \times 2 = 0{,}6$ incidente/mês, cada um custando $6$ h de correção $+$ impacto $\approx$ R\$ 3.500 $\Rightarrow$ $0{,}6 \times \text{R\$}\,3\,500 = \text{R\$}\,2\,100$/mês em incidentes. **Custo mensal $\approx 2 \times 480 + 2\,100 = \text{R\$}\,3\,060$.**
- **Depois (CI/CD):** $20$ deploys/mês (10× mais), cada um com $0{,}3$ h de supervisão humana $= \text{R\$}\,36$. Taxa de falha cai para $5\%$ (testes barram a maioria): $0{,}05 \times 20 = 1$ incidente/mês $\times \text{R\$}\,3\,500 = \text{R\$}\,3\,500$ — mas o **MTTR** despenca (rollback automático), reduzindo o impacto por incidente para R\$ 900: $1 \times \text{R\$}\,900 = \text{R\$}\,900$/mês. **Custo mensal $\approx 20 \times 36 + 900 = \text{R\$}\,1\,620$.**
- **Resultado:** **10× mais deploys** por **R\$ 1.440/mês a menos**, com a *change failure rate* caindo de $30\%$ para $5\%$. O segredo não é fazer menos deploy — é deixar o deploy **barato e seguro**.

### Pausa para reflexão (Desafio)

Pense no pipeline mais crítico que você já viu (ou imagine um que rode o faturamento da empresa). **Se você precisasse fazer uma mudança nele hoje, às 17h de uma sexta-feira, você faria?** Provavelmente não — e *esse medo* é o sintoma exato que o DataOps cura. Liste **três coisas** que tornam esse deploy assustador (sem testes? sem rollback? sem staging? deploy manual?) e, para cada uma, escreva a prática de DataOps que a neutralizaria. A meta de uma equipe madura é simples e radical: **deploy na sexta às 17h é rotina, não coragem.** O que falta no seu cenário para chegar lá?

### Atividade prática

Esboce um **pipeline de CI/CD** para um projeto dbt (ou Airflow) hipotético:

1. Desenhe o fluxo `dev → staging → produção` e diga **o que** roda em cada passagem.
2. Liste os **gates de CI** que devem bloquear o *merge* (linter, teste unitário, teste dbt) e escreva um deles como passo de GitHub Actions (pseudo-YAML).
3. Aplique a estratégia **write-audit-publish** a uma tabela: descreva os três passos concretos.
4. Escreva **três linhas de IaC** (pseudo-Terraform) declarando um recurso do pipeline (bucket, warehouse ou role).

### Pontos-chave

- **DataOps** aplica DevOps ao dado: automação, testes (de código **e** de dado), colaboração e iteração rápida.
- Versiona-se **código** (Git) **e** dado (DVC, lakeFS, *time travel* de Delta/Iceberg/Hudi) para reprodutibilidade e testes seguros.
- A pirâmide de testes ganha a camada de **testes de dados**; valide sempre em staging com dados sintéticos, nunca a primeira vez em produção.
- **CI** barra o erro no *pull request*; **CD** promove `dev → staging → prod`; **write-audit-publish** garante que o consumidor nunca veja dado quebrado.
- **IaC** (Terraform/Pulumi) torna a infraestrutura — e a própria governança — versionável e reproduzível; a meta DORA é deploy frequente com baixa taxa de falha.

### Para saber mais

- **DataOps (Wikipedia):** https://en.wikipedia.org/wiki/DataOps
- **DORA — Accelerate State of DevOps (Google Cloud):** https://dora.dev/
- **Terraform — documentação oficial (HashiCorp):** https://developer.hashicorp.com/terraform/docs
- **dbt — Deploying with CI/CD:** https://docs.getdbt.com/docs/deploy/continuous-integration

## Aula 15 — Roteiro da Videoaula 15: "DataOps e CI/CD para pipelines de dados"

### 1. Abertura (0:00 – 0:40)

> "Pergunta direta: você faria uma mudança no pipeline de faturamento às cinco da tarde de uma sexta? Se a resposta é 'de jeito nenhum', você tem um problema de processo, não de coragem. Hoje a gente aprende a transformar deploy assustador em rotina entediante — e isso tem nome: DataOps."

### 2. Desenvolvimento — parte 1 (0:40 – 4:00)

> "DataOps é DevOps aplicado a dado. Os pilares são automação ponta a ponta, testes em toda etapa — e aqui vem a sacada, você testa o código E o dado —, colaboração no mesmo fluxo versionado, e iteração rápida. A métrica que importa, do estudo DORA, é deploy frequente com baixa taxa de falha. E pra isso, você versiona duas coisas: o código, que vai pro Git como qualquer software, com branch e pull request; e o dado, com ferramentas tipo DVC, lakeFS e o time travel do Delta e do Iceberg, que deixam você consultar o dado como ele estava ontem. Versionar dado é o que dá reprodutibilidade."

### 3. Desenvolvimento — parte 2 (4:00 – 7:00)

> "A pirâmide de testes do software ganha uma camada nova: testes de dados. Unitário testa uma função de transformação; integração testa os componentes juntos; teste de dados verifica qualidade do resultado; e end-to-end roda o pipeline inteiro em staging. Regra de ouro: teste antes do deploy, com dado sintético, num ambiente isolado — a primeira validação nunca pode ser em produção. Aí entra o CI/CD: a integração contínua roda linter e testes a cada push e bloqueia o merge se falhar; a entrega contínua promove dev, staging, produção, nessa ordem. E uma estratégia linda pra dado é o write-audit-publish: escreve numa tabela temporária, audita com testes, e só publica se passar. O consumidor nunca vê dado quebrado."

### 4. Desenvolvimento — parte 3 (7:00 – 9:00)

> "Última peça: infraestrutura como código. Clicar no console da nuvem é frágil e não reproduzível. Com Terraform você escreve 'quero um bucket com versionamento e retenção de 90 dias' e a ferramenta aplica e mantém. Agora os números: equipe manual fazia 2 deploys por mês, 30% de falha, custava cerca de R\$ 3.060 por mês. Com CI/CD: 20 deploys por mês, falha cai pra 5%, rollback automático, custo cai pra R\$ 1.620. Dez vezes mais deploy, mil e quatrocentos a menos por mês. O segredo não é fazer menos deploy — é deixar o deploy barato e seguro."

### 5. Encerramento (9:00 – 11:00)

> "Fechando: DataOps automatiza e testa código e dado; você versiona os dois; CI barra o erro no pull request, CD promove pelos ambientes, e write-audit-publish protege o consumidor; e IaC versiona até a governança. Desafio da aula: liste três coisas que tornam um deploy assustador e a prática de DataOps que cura cada uma — porque numa equipe madura, deploy na sexta às 17h é rotina. Na última aula a gente junta tudo: tendências, o engenheiro de dados na era da IA, e um projeto integrador de ponta a ponta. Te vejo no encerramento."

---

## Aula 16 — Tendências e projeto integrador: do dado à IA

Chegamos à **última aula** da disciplina. Em quinze aulas você saiu de "o que é um pipeline" até qualidade, governança e DataOps. Agora vamos olhar para **frente** — para onde a engenharia de dados está indo na era da IA — e para **trás**, costurando as quatro unidades num **projeto integrador** que conecta tudo o que você construiu. Esta aula tem duas missões: te mostrar a fronteira (feature stores, MLOps, *streaming-first*, *real-time*) e te entregar uma síntese de ponta a ponta que você pode levar para uma entrevista, uma diretoria ou seu próximo emprego.

### O engenheiro de dados na era da IA

A explosão da IA generativa (2022 em diante) não tornou o engenheiro de dados obsoleto — fez o oposto. **IA roda sobre dados**, e modelo só é tão bom quanto o pipeline que o alimenta. O papel está se expandindo em três frentes: (1) **o engenheiro de dados como provedor de dados para IA** — alimentando *feature stores* e bases vetoriais para RAG (*Retrieval-Augmented Generation*); (2) **o engenheiro que usa IA como ferramenta** — *copilots* que geram SQL, dbt e testes, acelerando o próprio trabalho; e (3) **a fronteira AI-as-data** — pipelines que extraem dado estruturado de texto, imagem e áudio com LLMs. A habilidade-chave não envelhece: **dado confiável, governado e bem-modelado** é o pré-requisito de qualquer IA que funcione. "Garbage in, garbage out" virou regra de ouro de ML.

![Rede neural artificial — base dos modelos de machine learning](https://commons.wikimedia.org/wiki/Special:FilePath/Colored_neural_network.svg)

### Feature stores e MLOps

Um problema clássico de ML: o cientista treina o modelo com uma *feature* (ex.: "média de compras dos últimos 90 dias") calculada de um jeito num notebook, e em produção ela é recalculada de outro — gera o **training-serving skew**, e o modelo decai. A **feature store** (ex.: **Feast**, Tecton, Vertex AI Feature Store) resolve isso: é um repositório central de *features* versionadas, servidas **com a mesma lógica** para treino (*offline*, histórico) e produção (*online*, baixa latência).

**MLOps** é o DataOps (Aula 15) aplicado ao ciclo de vida do **modelo**: versionar dado, código *e* modelo; pipelines de treino reproduzíveis; deploy automatizado; e — crucial — monitoração de **data drift** e **model drift** (quando os dados de produção se afastam dos de treino e a acurácia cai). Repare: tudo o que você aprendeu nesta unidade (qualidade, linhagem, CI/CD) é **pré-requisito** de MLOps. O engenheiro de dados é a fundação do time de ML.

### Real-time analytics

O *batch* (processar lotes a cada hora ou dia) resolve a maioria dos casos, mas há decisões que **não podem esperar**: detecção de fraude em pagamento, recomendação durante a navegação, alerta de sensor industrial. **Real-time analytics** processa o dado em **segundos ou milissegundos** desde o evento. A infraestrutura usa bancos analíticos otimizados para ingestão e consulta em tempo real — **Apache Druid**, **ClickHouse**, **Apache Pinot** — alimentados por *streams*. A decisão *batch vs. real-time* é de **negócio**, não de tecnologia: pergunte sempre "qual o custo de esperar 1 hora por este dado?". Se for alto, é real-time; se não, *batch* é mais barato e simples — não pague por latência que ninguém usa.

### Arquiteturas streaming-first

Por décadas o *batch* foi o padrão e o *streaming* a exceção. A tendência **streaming-first** inverte isso: o **fluxo de eventos é a fonte primária da verdade**, e o *batch* vira um caso particular ("um *stream* que você decidiu olhar em janelas"). O conceito unificador é o **log de eventos imutável** (Apache Kafka como espinha dorsal), com processamento via **Apache Flink** ou **Spark Structured Streaming**. As vantagens: dado fresco por padrão, uma só base de código para *streaming* e *batch*, e reprocessamento por *replay* do log. É a evolução natural das arquiteturas Lambda (dois caminhos) para a **Kappa** (um caminho de *streaming* só). Nem toda empresa precisa disso hoje — mas é para onde a fronteira aponta.

### Carreira e certificações

A engenharia de dados é uma das carreiras mais demandadas em tecnologia. Um roteiro pragmático de desenvolvimento:

- **Fundamentos inegociáveis:** **SQL** (de verdade, com *window functions* e otimização) e **Python**. Ninguém contrata sem isso.
- **Modelagem e warehouse:** dimensional (Kimball), dbt, um data warehouse na nuvem (BigQuery, Snowflake, Redshift).
- **Orquestração e *big data*:** Airflow, Spark, Kafka.
- **Cloud e IaC:** ao menos uma nuvem a fundo (AWS, GCP ou Azure) + Terraform.
- **Certificações que o mercado valoriza:** *AWS Certified Data Engineer*, *Google Professional Data Engineer*, *Databricks Data Engineer Associate*, *Astronomer Airflow Certification*.
- **Soft skills:** comunicação com áreas de negócio — o melhor pipeline é inútil se ninguém entende o que ele entrega.

Construa **portfólio**: um projeto público no GitHub com ingestão, transformação dbt, testes de qualidade e orquestração vale mais que dez certificados sem prática.

### Síntese: o pipeline de ponta a ponta

Agora costuramos as quatro unidades num único fluxo coerente — o **pipeline de referência** que você deve saber desenhar de memória:

$$
\text{Fontes} \rightarrow \text{Ingestão} \rightarrow \text{Lake/Warehouse} \rightarrow \text{Transformação} \rightarrow \text{Servir} \rightarrow \text{BI/ML}
$$

| Unidade | O que dominou | No pipeline |
| --- | --- | --- |
| **U1 — Fundamentos** | Papel do dado, arquiteturas, batch vs. stream | Define **por que** e **como** o dado flui |
| **U2 — Ingestão e armazenamento** | Conectores, data lake/warehouse, formatos, modelagem | Traz e **guarda** o dado de forma consultável |
| **U3 — Transformação e orquestração** | ETL/ELT, dbt, Spark, Airflow | **Transforma** o dado cru em dado útil, no tempo certo |
| **U4 — Qualidade, governança, DataOps** | Testes, observabilidade, LGPD, CI/CD | Garante que tudo é **confiável, seguro e operável** |

As três primeiras unidades **constroem** o pipeline; a quarta o torna **profissional**. Um engenheiro júnior faz o dado chegar; um sênior faz o dado chegar **confiável, governado e com deploy seguro** — e é nesse lado que você termina a disciplina.

### Atividade prática

**Projeto integrador (portfólio).** Escolha um domínio real (e-commerce, saúde, logística, esporte — o que te motiva) e **projete um pipeline de ponta a ponta** usando as quatro unidades:

1. **U1:** defina a fonte, o caso de uso e a decisão *batch vs. real-time* (justifique pelo custo de esperar).
2. **U2:** escolha o destino (lake e/ou warehouse), o formato (Parquet/Delta) e esboce o modelo dimensional (fato + dimensões).
3. **U3:** liste as transformações (dbt), a orquestração (DAG do Airflow) e a periodicidade.
4. **U4:** defina **3 testes de qualidade**, a classificação LGPD dos campos sensíveis, a política de retenção e o fluxo de CI/CD.
5. Entregue um **diagrama de uma página** + um parágrafo de justificativa. Este é o artefato que você leva para entrevistas.

### Pontos-chave

- A IA **amplificou** o papel do engenheiro de dados: modelo só é tão bom quanto o pipeline que o alimenta ("garbage in, garbage out").
- **Feature stores** eliminam o *training-serving skew*; **MLOps** é o DataOps aplicado ao modelo, com monitoração de *data/model drift*.
- *Batch vs. real-time* é decisão **de negócio** (qual o custo de esperar?); **streaming-first** torna o log de eventos a fonte primária da verdade.
- A carreira exige **SQL e Python** como base, modelagem, orquestração, cloud + IaC e portfólio público — certificações ajudam, prática decide.
- O pipeline de referência é **Fontes → Ingestão → Lake/Warehouse → Transformação → Servir → BI/ML**; U1-U3 constroem, U4 profissionaliza.

### Para saber mais

- **Feast — Feature Store (documentação oficial):** https://docs.feast.dev/
- **Reis, J.; Housley, M. — *Fundamentals of Data Engineering* (O'Reilly):** https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/
- **Apache Kafka — documentação oficial:** https://kafka.apache.org/documentation/
- **MLOps (Wikipedia):** https://en.wikipedia.org/wiki/MLOps

### Encerramento da disciplina

Você terminou **Data Engineering and Pipelines** — uma disciplina densa que, há poucos anos, era território exclusivo de especialistas em grandes empresas de tecnologia.

Em 16 aulas você percorreu o caminho completo. Na **Unidade 1**, fundamentou o ofício: o que é dado, o papel do engenheiro de dados, as arquiteturas de referência e a divisão *batch* vs. *streaming*. Na **Unidade 2**, aprendeu a **trazer e guardar** o dado: conectores e ingestão, data lakes e warehouses, formatos colunares e modelagem dimensional. Na **Unidade 3**, dominou a **transformação e a orquestração**: ETL vs. ELT, dbt, Spark e Airflow, fazendo o dado cru virar dado útil no tempo certo. E nesta **Unidade 4**, você profissionalizou tudo: qualidade e observabilidade, governança e LGPD, DataOps e CI/CD — o que separa um script de notebook de um pipeline de produção.

Você sai com:

- **Vocabulário técnico completo** — ETL/ELT, data lake, warehouse, Parquet, dbt, Airflow, Spark, Kafka, lineage, data contract, observabilidade, IaC, MLOps.
- **Ferramentas mentais** para diagnosticar e desenhar pipelines de ponta a ponta.
- **Consciência de qualidade, segurança e custo** — o dado certo, protegido e operável, não só o dado que chega.
- **Visão de futuro** sobre engenharia de dados na era da IA.

Os fundamentos que você aprendeu **não envelhecem** — as ferramentas mudam de nome, mas modelar bem, garantir qualidade e automatizar com segurança serão valiosos por toda a sua carreira. Continue construindo: faça o projeto integrador, publique no GitHub, acompanhe a comunidade, mantenha SQL e Python afiados.

A indústria precisa de gente que faça o dado chegar **confiável**. Você terminou esta disciplina exatamente desse lado. Boa carreira — e vai longe.

## Aula 16 — Roteiro da Videoaula 16: "Tendências e projeto integrador: do dado à IA"

### 1. Abertura (0:00 – 0:40)

> "Última aula da disciplina. A gente vai olhar pra frente — pra onde a engenharia de dados está indo na era da IA — e pra trás, costurando as quatro unidades num projeto integrador que você leva pra entrevista. Em quinze aulas você saiu de 'o que é pipeline' até qualidade, governança e DataOps. Hoje a gente fecha o ciclo."

### 2. Desenvolvimento — parte 1 (0:40 – 4:00)

> "A IA generativa não aposentou o engenheiro de dados — fez o contrário. Modelo só é tão bom quanto o pipeline que alimenta ele: garbage in, garbage out. O papel se expande em três frentes: provedor de dados pra IA, com feature stores e bases vetoriais; usuário de IA como ferramenta, com copilots que geram SQL e dbt; e a fronteira de extrair dado estruturado de texto e imagem com LLM. E aí entra a feature store: ela resolve o training-serving skew, servindo a mesma feature, com a mesma lógica, pro treino e pra produção. MLOps é o DataOps que você viu na aula passada, aplicado ao modelo — com monitoração de drift. Tudo o que você aprendeu nesta unidade é pré-requisito de MLOps."

### 3. Desenvolvimento — parte 2 (4:00 – 7:00)

> "Sobre tendências: real-time analytics processa o dado em segundos, pra decisões que não podem esperar — fraude, recomendação, alerta de sensor — com bancos tipo Druid e ClickHouse. Mas atenção: batch versus real-time é decisão de negócio, não de tecnologia. Pergunte sempre: qual o custo de esperar uma hora por esse dado? Se for alto, real-time; se não, batch é mais barato. E a fronteira é streaming-first: o log de eventos, com Kafka, vira a fonte primária da verdade, e o batch vira caso particular. É a evolução da arquitetura Lambda pra Kappa. Sobre carreira: SQL e Python são inegociáveis, mais modelagem, orquestração, uma cloud a fundo e IaC. E portfólio público vale mais que certificado sem prática."

### 4. Desenvolvimento — parte 3 (7:00 – 9:00)

> "Agora a síntese, e quero que você grave esse fluxo de memória: Fontes, Ingestão, Lake ou Warehouse, Transformação, Servir, BI ou ML. A Unidade 1 te deu o porquê e o como do dado fluir. A Unidade 2 trouxe e guardou o dado. A Unidade 3 transformou e orquestrou. E a Unidade 4 garantiu que tudo é confiável, seguro e operável. As três primeiras constroem o pipeline; a quarta profissionaliza. Júnior faz o dado chegar; sênior faz o dado chegar confiável, governado e com deploy seguro. E é desse lado que você termina."

### 5. Encerramento (9:00 – 11:00)

> "Tarefa final, e é a mais importante: o projeto integrador. Escolhe um domínio que te motiva e desenha um pipeline de ponta a ponta com as quatro unidades — fonte e batch versus real-time da U1, lake e modelo da U2, transformação e DAG da U3, e testes, LGPD e CI/CD da U4. Um diagrama de uma página mais um parágrafo. Esse é o artefato que você apresenta numa entrevista. Você terminou uma disciplina densa, com vocabulário completo, ferramentas mentais e visão de futuro. Os fundamentos não envelhecem — as ferramentas trocam de nome, mas modelar bem, garantir qualidade e automatizar com segurança valem a carreira inteira. A indústria precisa de gente que faça o dado chegar confiável. Você terminou desse lado. Boa carreira, e vai longe."

---

## Quiz não avaliativo

### Questão 1

Sobre a diferença entre **testes de dados** e **observabilidade de dados**, assinale a alternativa **correta**:

- [ ] a. São sinônimos: ambos verificam apenas regras de schema definidas pelo produtor do dado.
- [x] b. Testes verificam regras que você **antecipou** (ex.: `not_null`, valor entre 0 e 1) dentro do pipeline, enquanto observabilidade detecta o **imprevisto** monitorando frescor, volume, distribuição, esquema e linhagem ao longo do tempo.
- [ ] c. Observabilidade só funciona em pipelines de streaming, e testes só em batch.
- [ ] d. Testes de dados substituem completamente a observabilidade, tornando-a desnecessária em pipelines maduros.

**Resposta correta:** `b`

**Feedback:** A (b) captura a complementaridade correta: o **teste** verifica regras antecipadas e barra o dado ruim na porta; a **observabilidade** (os 5 pilares: frescor, volume, distribuição, esquema, linhagem) detecta anomalias que você não previu, comparando o comportamento atual ao histórico. A (a) confunde os dois conceitos. A (c) é falsa — ambos servem batch e streaming. A (d) inverte a relação: as duas abordagens são complementares, não substitutas.

### Questão 2

No contexto de **DataOps e LGPD**, considere uma empresa com faturamento anual de R\$ 80 milhões que sofreu um vazamento de dados. Sobre as consequências e práticas envolvidas, assinale a alternativa **correta**:

- [ ] a. A multa máxima da LGPD por infração é fixa em R\$ 1.000, independentemente do faturamento.
- [ ] b. Como o dado estava pseudonimizado, ele sai automaticamente do escopo da LGPD e não há qualquer sanção possível.
- [x] c. A multa pode chegar a 2% do faturamento (R\$ 1,6 milhão neste caso, limitada a R\$ 50 milhões por infração), mas o custo de reputação e *churn* costuma ser ainda maior; práticas como menor privilégio, mascaramento e IaC versionando a governança reduzem drasticamente esse risco.
- [ ] d. A estratégia write-audit-publish (WAP) serve para impedir multas da LGPD publicando os dados pessoais diretamente em produção sem auditoria.

**Resposta correta:** `c`

**Feedback:** A (c) está correta: a sanção administrativa da LGPD chega a **2% do faturamento** (limitada a R\$ 50 mi/infração), e em 80 milhões dá R\$ 1,6 milhão — mas reputação e *churn* normalmente superam a multa, daí a importância de prevenção (menor privilégio, mascaramento, IaC). A (a) é falsa (a multa é percentual, não fixa). A (b) confunde **pseudonimização** (continua no escopo da LGPD) com **anonimização** (sai do escopo). A (d) distorce o WAP, que é uma técnica de **deploy seguro de dados** (escreve → audita → publica), não relacionada a publicar dados pessoais sem controle.

---

## Atividade Verificadora (AAI — Atividade Avaliativa Individual)

**Pergunta:**

> Você assumiu como engenheiro(a) de dados de uma *healthtech* que opera um aplicativo de telemedicina. O pipeline ingere dados de consultas (incluindo **dados sensíveis de saúde**), alimenta dashboards executivos e um modelo de ML que prioriza atendimentos. Hoje o pipeline **não tem testes**, ninguém sabe **de onde vem** cada número, os deploys são **manuais e arriscados**, e a diretoria está preocupada com a **LGPD** após um quase-incidente.
>
> Elabore uma resposta dissertativa estruturada em três partes:
>
> 1. **Qualidade e observabilidade:** que dimensões e quais testes/pilares você implementaria primeiro, e como mediria o impacto (use a lógica de *data downtime* / regra 1-10-100)?
> 2. **Governança e LGPD:** como classificaria e protegeria os dados sensíveis de saúde, e qual caminho técnico garantiria o **direito de exclusão** de um paciente?
> 3. **DataOps:** como tornaria os deploys seguros e frequentes (CI/CD, testes, IaC, write-audit-publish), e qual métrica usaria para provar a melhoria à diretoria?

**Resposta esperada:**

> Uma resposta de qualidade demonstra que o(a) estudante integra as quatro aulas da unidade num plano coerente e priorizado. **(1) Qualidade e observabilidade:** deve começar pelas dimensões mais críticas para saúde — **acurácia, completude e validade** —, escrevendo testes (`not_null` em identificadores e diagnósticos, `accepted_values` em códigos clínicos, faixas válidas em sinais vitais), e ativando observabilidade nos 5 pilares (especialmente frescor e volume). Boa resposta quantifica: estima TTD atual (dias sem monitoração), mostra que observabilidade reduz o TTD para minutos, e invoca a regra 1-10-100 para justificar prevenir em vez de remediar. **(2) Governança e LGPD:** classifica os campos (dado de saúde é **sensível**, proteção reforçada), aplica mascaramento/criptografia por padrão e menor privilégio (RBAC + row/column-level), define base legal, e — ponto central — explica que o direito de exclusão exige **linhagem completa** para localizar todos os lugares onde o dado do paciente pousou (lake, warehouse, features do modelo, backups), descrevendo um processo automatizado de eliminação ou anonimização. **(3) DataOps:** propõe CI (linter + testes unitários + testes dbt bloqueando o merge), CD promovendo dev → staging → prod, **write-audit-publish** para nunca expor dado clínico intermediário, e IaC (Terraform) versionando inclusive as políticas de acesso e retenção. Para provar melhoria à diretoria, usa métricas DORA — **frequência de deploy, change failure rate e MTTR** — além do TTD/data downtime. A resposta excelente conecta os três blocos (qualidade alimenta governança que habilita exclusão; DataOps automatiza e protege tudo) e **não vende mágica**: reconhece que é jornada incremental, prioriza o sensível primeiro e fala em números e prazos realistas.

---

## Material complementar

### Direto da fonte — livro da Biblioteca Virtual

> Este é **o** livro de referência moderno da área — escrito por dois praticantes para ensinar engenharia de dados como disciplina, não como coleção de ferramentas. O capítulo sobre o ciclo de vida do dado e os "*undercurrents*" (segurança, gestão de dados, DataOps, arquitetura) é a coluna vertebral conceitual desta Unidade 4: qualidade, governança e DataOps aparecem ali como as correntes que atravessam **todas** as etapas do pipeline, exatamente como tratamos nas Aulas 13 a 16.

- **Nome do livro:** *Fundamentals of Data Engineering: Plan and Build Robust Data Systems*
- **Capítulo:** Capítulo 2 — *The Data Engineering Lifecycle* (com foco nos *undercurrents*: Data Management, DataOps, Security)
- **Organizador:** Joe Reis e Matt Housley
- **Editora:** O'Reilly Media
- **Link de acesso (BV):** https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/
- **Aula em que entra:** Aulas 13 a 16

### Para mergulhar no assunto

> Para entender por que governança e *data products* (contratos de dados, donos claros) viraram tendência, leia o livro **"Data Mesh"** de Zhamak Dehghani — ela cunhou o termo e propõe tratar dado como produto com responsabilidade descentralizada, conectando diretamente com os data contracts da Aula 13 e a governança da Aula 14. Como alternativa visual e gratuita, o blog da Monte Carlo sobre *data observability* (incluindo o conceito de *data downtime*) é leitura curta e prática.

- **Link(s):** https://www.oreilly.com/library/view/data-mesh/9781492092384/ — e https://www.montecarlodata.com/blog-what-is-data-observability/
- **Aula em que entra:** Aulas 13 e 14

### Podcast (curadoria, até 45 min)

> O canal **Data Engineering Podcast** (Tobias Macey) entrevista praticantes sobre os temas exatos desta unidade. Recomendo episódios sobre **data quality / observability** e **DataOps**, que trazem casos reais de como times grandes operam qualidade e CI/CD em produção. Ótimo para ouvir o vocabulário da unidade aplicado por quem vive o dia a dia.

- **Nome do podcast/canal:** Data Engineering Podcast (Tobias Macey)
- **Tema recomendado:** Data observability, data quality e DataOps na prática
- **Link:** https://www.youtube.com/@DataEngineeringPodcast (YouTube)
- **Aula em que entra:** Aulas 13 e 15

### Artigo científico

> Artigo seminal do Google que cunhou o termo "**dívida técnica oculta em ML**" — argumenta que apenas uma fração minúscula de um sistema de ML é o código do modelo; o resto é infraestrutura de dados (coleta, validação, *feature extraction*, monitoração, configuração). É a justificativa científica para tudo o que esta unidade defende: qualidade, governança e DataOps são o que sustenta IA em produção, conectando diretamente com a Aula 16 (engenheiro de dados na era da IA, MLOps, *data/model drift*).

- **Link:** https://dl.acm.org/doi/10.5555/2969442.2969519 (NIPS 2015)
- **Aula em que entra:** Aula 16
- **Referência bibliográfica do artigo no formato ABNT:**
  > SCULLEY, D. *et al*. **Hidden technical debt in machine learning systems**. In: ADVANCES IN NEURAL INFORMATION PROCESSING SYSTEMS (NIPS), 28., 2015, Montreal. *Proceedings* [...]. Cambridge: MIT Press, 2015. p. 2503-2511.
