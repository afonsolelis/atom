# Questionário — Unidade 1

- **Disciplina:** Data Engineering and Pipelines
- **Professor-conteudista:** Afonso Cesar Lelis Brandão

## Orientações

- **20 questões** padrão ENADE: **10 asserção-razão** + **10 de interpretação**.
- Cada questão tem **5 alternativas (a–e)**; a correta é prefixada por `*` (ex.: `*c. ...`).
- Distribuição da alternativa correta: rotação **a, b, c, d, e, a, b, c, d, e...** (4 questões para cada letra).

---

## Questões

### Questão 1 (Asserção-Razão)

> **Asserção I:** No padrão ELT (Extract, Load, Transform), o dado bruto é carregado primeiro no destino e só depois transformado, dentro do próprio data warehouse ou data lake.
>
> **porque**
>
> **Razão II:** O barateamento do armazenamento de objetos na nuvem (na ordem de US$ 0,023 por GB ao mês) e o aumento da capacidade de processamento dos data warehouses modernos tornaram economicamente viável guardar todo o dado cru e transformá-lo sob demanda.

A respeito dessas asserções, assinale a opção correta:

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 2 (Asserção-Razão)

> **Asserção I:** O formato de arquivo Parquet é o padrão de mercado para cargas analíticas, pois reduz drasticamente o volume de dados lido em consultas que usam poucas colunas.
>
> **porque**
>
> **Razão II:** A linguagem SQL, proposta a partir do modelo relacional de Edgar F. Codd, é frequentemente apontada como uma das habilidades mais duradouras e valiosas de toda a área de dados.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 3 (Asserção-Razão)

> **Asserção I:** As propriedades ACID (atomicidade, consistência, isolamento e durabilidade) tornam um banco confiável para transações financeiras, como uma transferência bancária em que debitar e creditar precisam acontecer juntos.
>
> **porque**
>
> **Razão II:** A atomicidade garante que, em caso de queda do sistema no meio de uma transação, apenas a operação de débito seja desfeita, mantendo o crédito já efetivado para preservar o saldo do destinatário.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 4 (Asserção-Razão)

> **Asserção I:** No teorema CAP, a tolerância a partição (P) é uma escolha opcional do arquiteto, podendo ser totalmente descartada em sistemas distribuídos para que se garantam, ao mesmo tempo, consistência e disponibilidade plenas.
>
> **porque**
>
> **Razão II:** Em um sistema distribuído real, partições de rede são inevitáveis, de modo que, durante a falha de comunicação, a escolha prática se reduz a priorizar consistência (CP) ou disponibilidade (AP).

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 5 (Asserção-Razão)

> **Asserção I:** O modelo dimensional de Kimball recomenda manter as tabelas de fatos sempre na 3ª Forma Normal (3FN), pois a normalização das métricas reduz a quantidade de junções necessárias nas consultas analíticas.
>
> **porque**
>
> **Razão II:** No data warehouse, a normalização das dimensões em subtabelas (esquema floco de neve) é sempre preferível ao esquema estrela, porque a economia de espaço resultante torna as consultas analíticas mais rápidas.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

### Questão 6 (Asserção-Razão)

> **Asserção I:** O Change Data Capture (CDC) é uma técnica de extração mais eficiente que o snapshot completo para manter um destino analítico quase em tempo real a partir de um banco transacional.
>
> **porque**
>
> **Razão II:** O CDC lê o log de transações do banco-fonte e captura apenas as mudanças (inserções, atualizações e exclusões), evitando recopiar a tabela inteira a cada execução do pipeline.

A respeito dessas asserções, assinale a opção correta:

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 7 (Asserção-Razão)

> **Asserção I:** Cerca de 80% dos dados gerados no mundo são não estruturados — fotos, vídeos, áudios e documentos de texto livre.
>
> **porque**
>
> **Razão II:** O ciclo de vida da engenharia de dados, popularizado por Reis e Housley, organiza o trabalho em cinco etapas: geração, ingestão, transformação, armazenamento e disponibilização.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 8 (Asserção-Razão)

> **Asserção I:** Não se deve rodar relatórios analíticos pesados diretamente sobre o banco OLTP de produção, copiando-se o dado para um ambiente OLAP dedicado.
>
> **porque**
>
> **Razão II:** O banco OLTP é otimizado para leituras analíticas que agregam milhões de linhas, enquanto o ambiente OLAP foi desenhado para escritas pequenas e rápidas, registro a registro.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 9 (Asserção-Razão)

> **Asserção I:** O formato JSON é a melhor escolha para armazenar grandes volumes de dados destinados a consultas analíticas frequentes, porque é binário, colunar e altamente comprimido.
>
> **porque**
>
> **Razão II:** O JSON é um formato de texto hierárquico (chave-valor), flexível e adequado a dados semiestruturados e respostas de APIs, mas verboso, pois repete os nomes dos campos em cada registro.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 10 (Asserção-Razão)

> **Asserção I:** Em modelagem dimensional, a estratégia SCD Tipo 1 (sobrescrever o atributo) é a forma recomendada de preservar todo o histórico de mudanças de uma dimensão, mantendo a venda passada atribuída ao valor que o atributo tinha na época.
>
> **porque**
>
> **Razão II:** A tabela de fatos guarda o contexto descritivo do negócio (nome, cidade, segmento do cliente), enquanto a tabela de dimensão armazena as métricas numéricas mensuráveis (quantidade, valor, custo) dos eventos.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

### Questão 11 (Interpretação)

**Estímulo:**

> "O produto final do engenheiro de dados não é um modelo nem um gráfico — é o dado disponível, íntegro e organizado que outras pessoas vão consumir. Há um ditado no mercado: 'garbage in, garbage out' — se o dado que entra é lixo, qualquer modelo ou relatório também será lixo."

A leitura mais alinhada ao texto é:

*a. A entrega do engenheiro de dados é a base confiável sobre a qual cientistas e analistas trabalham, de modo que a qualidade do dado de entrada condiciona diretamente a qualidade de modelos e relatórios a jusante.
b. O engenheiro de dados é o responsável por treinar os modelos preditivos e gerar os dashboards finais consumidos pela diretoria.
c. O ditado "garbage in, garbage out" indica que a qualidade do dado é irrelevante, pois o modelo de IA corrige automaticamente quaisquer erros da fonte.
d. Como a entrega do engenheiro é apenas o dado bruto, a integridade e a organização não fazem parte das suas responsabilidades.
e. O papel do engenheiro de dados e o do cientista de dados são idênticos, já que ambos entregam exatamente o mesmo produto final.

### Questão 12 (Interpretação)

**Estímulo:**

> Uma tabela de eventos com 10 milhões de linhas e 20 colunas ocupa 4 GB em CSV. Uma consulta usa apenas 3 colunas. Em CSV, o motor precisa ler os 4 GB inteiros. Em Parquet, com compressão típica de 5×, o arquivo cai para 0,8 GB; lendo apenas as 3 de 20 colunas (fração de 0,15), a leitura efetiva é de cerca de 120 MB.

Que conclusão é **mais bem suportada** pelos dados?

a. CSV e Parquet leem exatamente o mesmo volume nessa consulta, pois ambos guardam todas as colunas misturadas em cada linha.
*b. O armazenamento colunar comprimido reduz o volume lido de 4 GB para cerca de 120 MB (aproximadamente 33×), o que, como o custo de consulta na nuvem costuma ser proporcional ao dado lido, significa pagar cerca de 33 vezes menos pela mesma resposta.
c. O Parquet é mais lento porque, sendo colunar, precisa reconstruir todas as 20 colunas mesmo quando a consulta usa apenas 3.
d. A vantagem do Parquet vem só da compressão de 5×, sendo irrelevante o fato de ele ler apenas as colunas necessárias.
e. Para essa consulta, o CSV é preferível, pois 4 GB são lidos mais rápido do que 120 MB em formato colunar.

### Questão 13 (Interpretação)

**Estímulo:**

> Uma plataforma de IoT recebe leituras de 50.000 sensores, cada um enviando 1 medição por segundo. Um banco relacional com garantias ACID completas suporta tipicamente de 5.000 a 10.000 escritas por segundo em um único nó (cerca de 8.000 escritas/s por nó). Um banco colunar distribuído como o Cassandra suporta na ordem de 50.000 escritas por segundo em poucos nós, com escalabilidade horizontal.

A leitura **mais adequada** do cenário é:

a. Um único nó relacional resolve o problema, pois 50.000 escritas por segundo estão dentro da faixa de 5.000 a 10.000 suportada por nó.
b. O padrão de acesso é irrelevante: deve-se escolher sempre o banco relacional, por ser tecnicamente superior em qualquer cenário.
*c. Para esse perfil de escrita massiva e contínua (50.000 escritas/s), um banco colunar distribuído como o Cassandra é a escolha natural — não por ser "melhor" em absoluto, mas por casar com o padrão de acesso, ao passo que a solução relacional exigiria cerca de 7 nós.
d. O Cassandra é a escolha porque oferece garantias ACID completas mais fortes do que qualquer banco relacional.
e. Como o relacional é ACID, ele deve ser usado mesmo que demande dezenas de nós, pois NoSQL nunca é adequado para IoT.

### Questão 14 (Interpretação)

**Estímulo:**

> "MongoDB e HBase tendem a CP; Cassandra e DynamoDB tendem a AP, oferecendo consistência eventual (o dado fica consistente 'em algum momento'). Pense no Instagram: se a contagem de curtidas de uma foto ficar alguns segundos desatualizada, ninguém se importa — o que não pode é o app sair do ar."

A leitura mais correta do texto é:

a. Sistemas AP, como o Cassandra, garantem que toda leitura sempre retorne o dado mais recente, mesmo durante uma partição de rede.
b. A consistência eventual significa que o dado nunca chega a ficar consistente, permanecendo permanentemente divergente entre os nós.
c. Para a contagem de curtidas do Instagram, o ideal é priorizar consistência (CP), pois exibir um número desatualizado por instantes é inaceitável.
*d. Em um caso como a contagem de curtidas, priorizar disponibilidade (AP) com consistência eventual é uma troca razoável, pois é pior o app sair do ar do que exibir, por alguns segundos, um valor levemente desatualizado.
e. CP e AP descrevem a mesma garantia, de modo que a escolha entre MongoDB e Cassandra é indiferente para a natureza do negócio.

### Questão 15 (Interpretação)

**Estímulo:**

> Uma rede varejista tem 500 lojas que processam, em média, 2.000 vendas por loja por dia. Cada venda tem, em média, 4 itens, e a granularidade da tabela de fatos é um item por linha.

Quantas linhas a tabela de fatos recebe **por dia**?

a. 1.000.000 de linhas.
b. 2.000.000 de linhas.
c. 3.000.000 de linhas.
d. 8.000.000 de linhas.
*e. 4.000.000 de linhas.

### Questão 16 (Interpretação)

**Estímulo:**

> "Schema-on-write: você define o esquema antes de gravar; o banco rejeita qualquer dado fora do formato — qualidade garantida na entrada, mas rígido. Schema-on-read: você grava o dado bruto sem esquema e o interpreta apenas na hora de ler — flexível, ideal para data lakes, mas transfere a responsabilidade da qualidade para o momento da leitura."

A leitura mais coerente com o texto é:

*a. As duas abordagens fazem uma troca: o schema-on-write prioriza qualidade na entrada ao custo de rigidez, enquanto o schema-on-read prioriza flexibilidade ao custo de adiar a validação para o momento da leitura.
b. O schema-on-read é sempre superior, pois garante a qualidade do dado já no instante da gravação.
c. O schema-on-write é incompatível com data warehouses, que nasceram exclusivamente schema-on-read.
d. Ambas as abordagens validam o esquema no mesmo momento, sendo apenas nomes comerciais distintos para o mesmo processo.
e. O schema-on-read elimina por completo a necessidade de qualquer validação de qualidade ao longo do ciclo de vida do dado.

### Questão 17 (Interpretação)

**Estímulo:**

> Uma startup de delivery roda todo o sistema em um único PostgreSQL transacional. O time de produto começou a pedir relatórios pesados ("faturamento por bairro no trimestre"), e essas consultas estão deixando o app lento para os clientes, porque competem com a operação no mesmo banco.

A interpretação técnica **mais adequada** do problema é:

a. O app ficou lento porque o PostgreSQL é um banco NoSQL inadequado para registrar pedidos, devendo ser substituído por um banco relacional.
*b. Consultas analíticas que agregam milhões de linhas (carga OLAP) disputam CPU, memória e I/O com a operação OLTP no mesmo banco; a solução é separar os mundos, copiando o dado para um ambiente OLAP dedicado.
c. A lentidão é causada por falta de índices, e basta criar mais chaves estrangeiras na tabela de pedidos para resolvê-la.
d. O problema some ao migrar o relatório para uma planilha de Excel conectada diretamente ao banco de produção.
e. A solução é desligar as garantias ACID do PostgreSQL para acelerar tanto a operação quanto os relatórios simultaneamente.

### Questão 18 (Interpretação)

**Estímulo:**

> "Em uma arquitetura moderna, convivem vários bancos: o relacional para transações, o documento para catálogos com JSON aninhado, o colunar para sensores e séries temporais, e o grafo para relacionamentos como redes sociais e detecção de fraude. A pergunta-guia é sempre: qual o padrão de acesso?"

A leitura mais coerente com o texto é:

a. Toda empresa moderna deve padronizar tudo em um único banco relacional, eliminando NoSQL.
b. O banco de grafo é universalmente superior e deve substituir relacional, documento e colunar em qualquer cenário.
*c. Não existe um banco "melhor" em absoluto: cada família é otimizada para um padrão de acesso, de modo que relacional e NoSQL coexistem em arquiteturas reais, escolhidos pela natureza da carga.
d. A escolha do banco deve seguir a moda do mercado, e não o padrão de acesso do problema.
e. O banco colunar deve ser usado para transações financeiras, por oferecer as garantias ACID mais fortes.

### Questão 19 (Interpretação)

**Estímulo:**

> Um e-commerce registra 2 milhões de eventos por dia, cada um ocupando, em média, 1,5 KB no formato bruto.

Qual o volume bruto gerado **por dia**?

a. 1,5 GB/dia.
b. 2 GB/dia.
c. 2,5 GB/dia.
*d. 3 GB/dia.
e. 30 GB/dia.

### Questão 20 (Interpretação)

**Estímulo:**

> "E quando um atributo de dimensão muda? Por exemplo, um cliente muda de cidade. No SCD Tipo 2, ao mudar a cidade, você fecha a linha antiga (com data de fim) e cria uma nova (com data de início), mantendo um indicador de 'linha atual'. Assim, uma venda feita no passado continua atribuída à cidade correta na época."

A leitura mais alinhada ao texto é:

a. O SCD Tipo 2 sobrescreve o valor antigo, perdendo o histórico e mantendo apenas a cidade atual do cliente.
b. O SCD Tipo 2 impede qualquer alteração no atributo, sendo indicado apenas para dados imutáveis, como a data de nascimento.
c. Com o SCD Tipo 2, vendas passadas passam a ser reatribuídas à cidade nova, reescrevendo a história do cliente.
d. O SCD Tipo 2 guarda apenas a versão anterior e a atual em colunas distintas da mesma linha, sem criar novos registros.
*e. O SCD Tipo 2 preserva o histórico completo criando uma nova linha a cada mudança, com datas de validade e um indicador de linha atual, de modo que cada venda permanece associada à cidade vigente na época.

---

## Feedbacks

### Questão 1

- **a.** *Correta!* Ambas verdadeiras e a II justifica a I. A Asserção descreve corretamente o ELT (carrega o bruto primeiro, transforma depois, dentro do destino), e a Razão explica precisamente **por que** isso se tornou viável: o armazenamento de objetos na nuvem ficou barato (≈ US$ 0,023/GB/mês) e os warehouses, poderosos — exatamente a causa econômica do ELT.
- **b.** Incorreta. A Razão **justifica** diretamente a Asserção (é a causa econômica do ELT).
- **c.** Incorreta. A Razão é verdadeira.
- **d.** Incorreta. A Asserção é verdadeira.
- **e.** Incorreta. Ambas são verdadeiras.

### Questão 2

- **a.** Incorreta. A Razão não justifica a Asserção — tratam de temas distintos.
- **b.** *Correta!* As duas proposições são individualmente verdadeiras: o Parquet é, de fato, padrão de analytics por ler menos colunas e comprimir bem; e o SQL é, de fato, uma das habilidades mais duradouras da área. Mas a Razão (sobre SQL/modelo relacional) **não explica** por que o Parquet é eficiente em analytics — são fatos independentes.
- **c.** Incorreta. A Razão é verdadeira.
- **d.** Incorreta. A Asserção é verdadeira.
- **e.** Incorreta. Ambas são verdadeiras.

### Questão 3

- **a.** Incorreta. A Razão é falsa.
- **b.** Incorreta. A Razão é falsa.
- **c.** *Correta!* A Asserção é verdadeira: o ACID torna o banco confiável para transações, e a transferência bancária é o exemplo clássico. A Razão é **falsa**: a atomicidade garante que a transação aconteça **toda ou nada** — se o sistema cai no meio, **nada** acontece (o débito é desfeito **e** o crédito não é aplicado), e não "mantém o crédito" como afirmado.
- **d.** Incorreta. A Asserção é verdadeira.
- **e.** Incorreta. A Asserção é verdadeira.

### Questão 4

- **a.** Incorreta. A Asserção é falsa.
- **b.** Incorreta. A Asserção é falsa.
- **c.** Incorreta. A Razão é verdadeira.
- **d.** *Correta!* A Asserção é **falsa**: a tolerância a partição (P) **não** é opcional — partições de rede são inevitáveis em sistemas distribuídos, então P é obrigatório na prática e não se pode garantir C e A plenas ao mesmo tempo durante a partição. A Razão é verdadeira e descreve corretamente a escolha real entre CP e AP.
- **e.** Incorreta. A Razão é verdadeira.

### Questão 5

- **a.** Incorreta. Ambas são falsas.
- **b.** Incorreta. Ambas são falsas.
- **c.** Incorreta. A Razão também é falsa.
- **d.** Incorreta. A Asserção também é falsa.
- **e.** *Correta!* Ambas são falsas. A Asserção inverte a modelagem dimensional: tabelas de fatos **não** ficam em 3FN — o data warehouse usa **desnormalização** para reduzir junções, e a 3FN é típica do OLTP. A Razão também é falsa: o esquema **estrela** (dimensões desnormalizadas), e não o floco de neve, costuma vencer pela simplicidade e velocidade; a economia de espaço do floco de neve vem ao custo de **mais** junções e consultas mais lentas.

### Questão 6

- **a.** *Correta!* Ambas verdadeiras e a II justifica a I. O CDC é de fato mais eficiente que o snapshot para manter o destino quase em tempo real, e a Razão explica **por quê**: ele lê o log de transações e captura apenas as mudanças, em vez de recopiar a tabela inteira — exatamente a causa da eficiência afirmada.
- **b.** Incorreta. A Razão justifica diretamente a Asserção.
- **c.** Incorreta. A Razão é verdadeira.
- **d.** Incorreta. A Asserção é verdadeira.
- **e.** Incorreta. Ambas são verdadeiras.

### Questão 7

- **a.** Incorreta. A Razão não justifica a Asserção.
- **b.** *Correta!* As duas proposições são verdadeiras: cerca de 80% dos dados mundiais são de fato não estruturados; e o ciclo de vida da engenharia de dados tem, de fato, as cinco etapas citadas. Porém, a Razão (etapas do ciclo de vida) **não explica** o percentual de dados não estruturados — são informações independentes, sem relação de causa.
- **c.** Incorreta. A Razão é verdadeira.
- **d.** Incorreta. A Asserção é verdadeira.
- **e.** Incorreta. Ambas são verdadeiras.

### Questão 8

- **a.** Incorreta. A Razão é falsa.
- **b.** Incorreta. A Razão é falsa.
- **c.** *Correta!* A Asserção é verdadeira: rodar relatórios pesados no OLTP de produção sobrecarrega a operação, e a prática correta é copiar o dado para um ambiente OLAP. A Razão é **falsa** porque **inverte** as otimizações: o OLTP é otimizado para escritas/leituras pequenas e rápidas, e o OLAP para leituras analíticas agregando milhões de linhas — exatamente o contrário do que ela afirma.
- **d.** Incorreta. A Asserção é verdadeira.
- **e.** Incorreta. A Asserção é verdadeira.

### Questão 9

- **a.** Incorreta. A Asserção é falsa.
- **b.** Incorreta. A Asserção é falsa.
- **c.** Incorreta. A Razão é verdadeira.
- **d.** *Correta!* A Asserção é **falsa**: o JSON é texto verboso (não binário, não colunar) e **não** é o ideal para grandes volumes analíticos — esse papel é do **Parquet** (colunar e comprimido). A Razão é verdadeira: o JSON é mesmo um formato de texto hierárquico, flexível para semiestruturado e APIs, porém verboso por repetir os nomes dos campos.
- **e.** Incorreta. A Razão é verdadeira.

### Questão 10

- **a.** Incorreta. Ambas são falsas.
- **b.** Incorreta. Ambas são falsas.
- **c.** Incorreta. A Razão também é falsa.
- **d.** Incorreta. A Asserção também é falsa.
- **e.** *Correta!* Ambas são falsas. A Asserção confunde os tipos de SCD: quem **preserva** o histórico é o **Tipo 2** (cria nova linha com validade); o **Tipo 1** sobrescreve e **perde** a história. A Razão **inverte** os papéis das tabelas: a tabela de **fatos** guarda as métricas numéricas (quantidade, valor, custo), e a tabela de **dimensão** guarda o contexto descritivo (nome, cidade, segmento).

### Questão 11

- **a.** *Correta!* É exatamente a tese do texto: a entrega do engenheiro é o dado confiável que sustenta o trabalho a jusante, e o ditado "garbage in, garbage out" mostra que a qualidade da entrada condiciona a qualidade de modelos e relatórios.
- **b.** Incorreta. Treinar modelos é do cientista de dados; gerar dashboards, do analista — não do engenheiro de dados.
- **c.** Incorreta. O ditado afirma o oposto: dado ruim na entrada produz resultado ruim na saída; o modelo não "corrige" a fonte.
- **d.** Incorreta. O texto define a entrega como dado **disponível, íntegro e organizado** — integridade e organização são responsabilidades centrais.
- **e.** Incorreta. Os papéis são distintos e complementares; entregam produtos diferentes (pipeline/dado x modelo).

### Questão 12

- **a.** Incorreta. Só o CSV lê tudo; o Parquet, sendo colunar, lê apenas as colunas necessárias.
- **b.** *Correta!* A leitura cai de 4 GB para ≈ 120 MB (cerca de 33×). Como o custo de consulta na nuvem costuma ser proporcional ao dado lido, paga-se cerca de 33 vezes menos pela mesma resposta — o argumento central a favor do colunar.
- **c.** Incorreta. O Parquet lê só as 3 colunas pedidas; não reconstrói as 20 desnecessárias.
- **d.** Incorreta. A vantagem combina **dois** efeitos: a compressão (5×) **e** a leitura apenas das colunas necessárias (fração de 0,15).
- **e.** Incorreta. Ler 120 MB é muito mais barato e rápido do que ler 4 GB; o CSV não é preferível aqui.

### Questão 13

- **a.** Incorreta. 50.000 escritas/s excedem em muito a faixa de 5.000–10.000 por nó relacional.
- **b.** Incorreta. O padrão de acesso é justamente o critério de escolha; nenhum banco é "superior em qualquer cenário".
- **c.** *Correta!* Para escrita massiva e contínua (50.000 escritas/s), o colunar distribuído (Cassandra) casa com o padrão de acesso; a solução relacional exigiria cerca de 7 nós (50.000 ÷ 8.000 ≈ 6,25 → 7).
- **d.** Incorreta. Bancos colunares como o Cassandra abrem mão de ACID completo (tendem a AP/consistência eventual); a escolha não é por garantias ACID mais fortes.
- **e.** Incorreta. NoSQL pode, sim, ser adequado para IoT; insistir no relacional com dezenas de nós ignora o padrão de acesso.

### Questão 14

- **a.** Incorreta. Sistemas AP priorizam disponibilidade e admitem dados temporariamente desatualizados (consistência eventual).
- **b.** Incorreta. Consistência eventual significa que o dado fica consistente "em algum momento", não que permaneça divergente para sempre.
- **c.** Incorreta. Para curtidas, exibir um valor levemente desatualizado por instantes é aceitável; o crítico é não sair do ar — logo, AP.
- **d.** *Correta!* É a leitura correta: em um caso como a contagem de curtidas, prioriza-se disponibilidade (AP) com consistência eventual, pois é pior o app cair do que mostrar, por segundos, um número levemente defasado.
- **e.** Incorreta. CP e AP descrevem garantias diferentes; a escolha depende diretamente da natureza do negócio.

### Questão 15

- **a.** Incorreta. 1.000.000 ignora o número de itens e o de lojas/vendas corretos.
- **b.** Incorreta. 2.000.000 corresponde apenas a 500 × 2.000 × 2, com fator de itens errado.
- **c.** Incorreta. 3.000.000 não decorre dos fatores do enunciado.
- **d.** Incorreta. 8.000.000 dobra indevidamente o resultado (usaria 8 itens por venda).
- **e.** *Correta!* 500 lojas × 2.000 vendas × 4 itens = 4.000.000 de linhas por dia — a granularidade é um item por linha.

### Questão 16

- **a.** *Correta!* O texto descreve uma troca: schema-on-write prioriza qualidade na entrada (rígido); schema-on-read prioriza flexibilidade, adiando a validação para a leitura — exatamente o contraste apresentado.
- **b.** Incorreta. Quem valida na gravação é o schema-on-write, não o schema-on-read.
- **c.** Incorreta. Data warehouses tendem ao schema-on-write; data lakes nasceram schema-on-read — não há incompatibilidade absoluta.
- **d.** Incorreta. As abordagens validam o esquema em **momentos** diferentes (escrita x leitura); não são o mesmo processo.
- **e.** Incorreta. O schema-on-read **adia** a validação, mas não elimina a necessidade de qualidade ao longo do ciclo de vida.

### Questão 17

- **a.** Incorreta. O PostgreSQL é relacional (não NoSQL) e é adequado para registrar pedidos; o problema não é a escolha do banco transacional.
- **b.** *Correta!* É o diagnóstico OLTP vs OLAP: consultas que agregam milhões de linhas (carga OLAP) disputam CPU, memória e I/O com a operação OLTP no mesmo banco; a solução é separar os mundos, copiando o dado para um ambiente OLAP dedicado.
- **c.** Incorreta. Criar chaves estrangeiras não resolve a contenção de recursos entre carga analítica e operacional.
- **d.** Incorreta. Conectar uma planilha ao banco de produção mantém (ou agrava) a disputa de recursos.
- **e.** Incorreta. Desligar o ACID compromete a integridade das transações e não resolve a contenção OLTP x OLAP.

### Questão 18

- **a.** Incorreta. O texto defende a coexistência de vários bancos, não a padronização em relacional.
- **b.** Incorreta. O grafo é ótimo para relacionamentos, mas não substitui as outras famílias em todo cenário.
- **c.** *Correta!* É a tese central: não há banco "melhor" em absoluto — cada família é otimizada para um padrão de acesso, e relacional e NoSQL coexistem em arquiteturas reais, escolhidos pela natureza da carga.
- **d.** Incorreta. O texto diz o oposto: o padrão de acesso (e não a moda) deve guiar a escolha.
- **e.** Incorreta. Transações financeiras pedem banco relacional com ACID, não colunar.

### Questão 19

- **a.** Incorreta. 1,5 GB usaria 1 milhão de eventos, não 2 milhões.
- **b.** Incorreta. 2 GB não corresponde ao produto 2.000.000 × 1,5 KB.
- **c.** Incorreta. 2,5 GB não decorre dos valores do enunciado.
- **d.** *Correta!* 2.000.000 × 1,5 KB = 3.000.000 KB = 3 GB/dia.
- **e.** Incorreta. 30 GB resultaria de um erro de uma ordem de grandeza (10×).

### Questão 20

- **a.** Incorreta. Sobrescrever e perder o histórico é o SCD Tipo 1, não o Tipo 2.
- **b.** Incorreta. Impedir qualquer alteração é o SCD Tipo 0 (atributo fixo), não o Tipo 2.
- **c.** Incorreta. O Tipo 2 **não** reescreve a história: vendas passadas seguem atribuídas à cidade vigente na época.
- **d.** Incorreta. Guardar apenas valor anterior e atual em colunas é o SCD Tipo 3, não o Tipo 2.
- **e.** *Correta!* É exatamente o SCD Tipo 2: preserva o histórico completo criando uma nova linha a cada mudança, com datas de validade e indicador de linha atual, mantendo cada venda associada à cidade da época.
