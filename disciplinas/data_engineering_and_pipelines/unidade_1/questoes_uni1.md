# Questionário — Unidade 1

- **Disciplina:** Data Engineering and Pipelines
- **Professor-conteudista:** Afonso Cesar Lelis Brandão

## Orientações

- **40 questões** padrão ENADE: **20 asserção-razão** + **20 de interpretação**.
- Cada questão tem **5 alternativas (a–e)**; a correta é prefixada por `*` (ex.: `*c. ...`).
- Distribuição da alternativa correta: rotação **a, b, c, d, e** repetida ao longo das questões (**8 questões para cada letra**, totalizando 40).

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

### Questão 21 (Asserção-Razão)

> **Asserção I:** No ciclo de vida da engenharia de dados aplicado ao Olist, a **orquestração** (que faremos com o Airflow) é tratada como uma corrente transversal (undercurrent), e não como uma sexta etapa após a disponibilização.
>
> **porque**
>
> **Razão II:** As correntes transversais — segurança, governança e qualidade, gestão de metadados, orquestração e engenharia de software — atravessam **todas** as etapas do ciclo (geração, ingestão, transformação, armazenamento e disponibilização), em vez de ocorrerem em um único momento sequencial.

A respeito dessas asserções, assinale a opção correta:

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 22 (Asserção-Razão)

> **Asserção I:** No pipeline do Olist, o formato **Avro** é uma opção adequada para a ingestão de eventos em streaming, como o stream de pedidos simulado na Aula 7.
>
> **porque**
>
> **Razão II:** O modelo relacional foi proposto por Edgar F. Codd em 1970 e organiza os dados em tabelas conectadas por chaves primárias e estrangeiras.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 23 (Asserção-Razão)

> **Asserção I:** A arquitetura Medallion adotada no pipeline do Olist organiza os dados em camadas **bronze, silver e gold**, em que a bronze guarda o dado cru ingerido dos CSVs em Parquet.
>
> **porque**
>
> **Razão II:** Guardar a camada bronze crua é desnecessário no Olist, pois, uma vez construída a estrela (gold), o dado bruto original pode ser descartado sem qualquer perda de capacidade de reprocessamento.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 24 (Asserção-Razão)

> **Asserção I:** No modelo relacional do Olist, a coluna **customer_id** da tabela `orders` é uma **chave primária**, pois é ela que identifica unicamente cada linha de pedido.
>
> **porque**
>
> **Razão II:** No Olist, o **order_id** é a coluna que costura `orders`, `order_items`, `order_payments` e `order_reviews`, funcionando como a espinha dorsal que liga o pedido às suas tabelas satélites.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 25 (Asserção-Razão)

> **Asserção I:** No teorema CAP, "AP" significa que o sistema abre mão da **tolerância a partição** para garantir, simultaneamente, disponibilidade e consistência plenas durante uma falha de rede.
>
> **porque**
>
> **Razão II:** A propriedade **Isolamento** do ACID garante a **durabilidade** de uma transação confirmada, assegurando que ela sobreviva a uma queda de energia do servidor.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

### Questão 26 (Asserção-Razão)

> **Asserção I:** Ao ler os CSVs do Olist com `read_csv_auto`, o DuckDB opera em **schema-on-read**, inferindo os tipos das colunas no momento da leitura, sem exigir que o esquema tenha sido declarado antes.
>
> **porque**
>
> **Razão II:** No schema-on-read, o dado bruto é gravado sem um esquema imposto na escrita e só é interpretado na hora de ser lido, o que confere flexibilidade e é adequado a uma camada bronze de data lake.

A respeito dessas asserções, assinale a opção correta:

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 27 (Asserção-Razão)

> **Asserção I:** No Olist, a família NoSQL de **documentos** (como o MongoDB) casaria bem com o armazenamento das avaliações (`review`), que têm campos opcionais e um texto livre no `review_comment_message`.
>
> **porque**
>
> **Razão II:** Estima-se que cerca de **80% dos dados gerados no mundo** sejam não estruturados, como fotos, vídeos, áudios e documentos de texto livre.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 28 (Asserção-Razão)

> **Asserção I:** No star schema do Olist, o **grão** (granularidade) escolhido para a fato `fct_order_items` é **um item de pedido por linha**, a granularidade mais fina de onde todas as agregações partem.
>
> **porque**
>
> **Razão II:** Definir o grão da fato no nível do **pedido inteiro** (um pedido por linha) permitiria, ainda assim, calcular corretamente o faturamento por item, pois cada pedido do Olist contém sempre exatamente um único item.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 29 (Asserção-Razão)

> **Asserção I:** No pipeline do Olist, o cientista de dados é o responsável por escrever o script de ingestão que converte os 9 CSVs em Parquet e por materializar o schema `raw` no DuckDB.
>
> **porque**
>
> **Razão II:** No Olist, a entrega típica do engenheiro de dados é a fato `fct_order_items` confiável e disponível, sobre a qual o cientista de dados constrói o modelo que prevê o atraso de entrega.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 30 (Asserção-Razão)

> **Asserção I:** No Olist, a tabela `olist_geolocation_dataset`, por conter cerca de 1 milhão de linhas de CEP, é classificada como um dado **não estruturado**, uma vez que ultrapassa 100 mil registros.
>
> **porque**
>
> **Razão II:** O grau de estrutura de um dado é determinado pela **quantidade de linhas** que ele possui: acima de um certo volume, qualquer tabela passa a ser considerada semiestruturada ou não estruturada.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

### Questão 31 (Interpretação)

**Estímulo:**

> "Atravessando todas as etapas do ciclo de vida estão as **correntes transversais**: segurança, governança e qualidade de dados, gestão de metadados, orquestração e engenharia de software. Elas não são uma 'etapa' — são preocupações de **todas** as etapas. No nosso pipeline, a orquestração será o Airflow, a qualidade virá de dbt tests + Great Expectations, e a governança aparecerá quando discutirmos a LGPD."

A leitura mais alinhada ao texto é:

*a. As correntes transversais são preocupações contínuas que permeiam da geração à disponibilização; por isso, no Olist, orquestração, qualidade e governança são endereçadas ao longo de todo o pipeline, e não em uma única fase isolada.
b. As correntes transversais são uma sexta etapa do ciclo, executada somente após a disponibilização do dado ao consumidor final.
c. Governança e qualidade só importam na etapa de geração, quando o dado nasce nos sistemas-fonte, e podem ser ignoradas nas demais etapas.
d. A orquestração com Airflow substitui a necessidade de qualquer verificação de qualidade, tornando dbt tests e Great Expectations redundantes.
e. As correntes transversais são exclusivas de projetos na nuvem e não se aplicam a um pipeline local como o do Olist.

### Questão 32 (Interpretação)

**Estímulo:**

> Regra prática dos formatos: **CSV/JSON** para troca e ingestão; **Parquet** para analytics; **Avro** para streaming. No pipeline do Olist, o dado entra como CSV, vira Parquet na camada bronze, e na Aula 7 um stream de pedidos é simulado como eventos JSON.

Um estagiário propõe **guardar a camada analítica gold do Olist em CSV** para "facilitar a leitura no Excel". A avaliação técnica **mais adequada** dessa proposta é:

a. A proposta é ideal, pois o CSV é colunar e comprimido, sendo o formato de melhor desempenho para consultas analíticas que agregam milhões de linhas.
*b. A proposta é inadequada: a camada analítica deve usar **Parquet** (colunar e comprimido), que lê apenas as colunas necessárias e ocupa muito menos espaço; o CSV é texto sem tipos e sem compressão, adequado à troca e à ingestão, não ao analytics.
c. Tanto faz o formato da gold, pois CSV e Parquet têm exatamente o mesmo desempenho de leitura em consultas analíticas.
d. O correto seria guardar a gold em **Avro**, pois é o formato colunar recomendado para consultas analíticas agregadas.
e. A proposta é boa porque o CSV, por ser binário e tipado, dispensa qualquer inferência de esquema na leitura.

### Questão 33 (Interpretação)

**Estímulo:**

> "Não existe 'NoSQL melhor que SQL'. Numa arquitetura real, os bancos convivem: o relacional para os pedidos, o documento para as reviews, o colunar para os eventos de clique, e o grafo para a recomendação cliente–vendedor. A pergunta-guia é sempre: qual o padrão de acesso?"

No contexto do Olist, qual associação entre **necessidade** e **família de banco** está **corretamente** justificada pelo padrão de acesso?

a. Guardar o carrinho de compras ativo do cliente em um banco de **grafo**, por ser o mais rápido para pares chave→valor.
b. Registrar o pagamento de um pedido em um banco **colunar (Cassandra)**, por oferecer as garantias ACID mais fortes.
*c. Ingerir o stream massivo de cliques/eventos do marketplace em um banco **colunar de escrita massiva (Cassandra)**, que escala horizontalmente para o padrão de escrita contínua e de alto volume.
d. Mapear a rede "cliente → comprou de → vendedor" em um banco de **documentos (MongoDB)**, por ser o único capaz de armazenar JSON.
e. Armazenar as avaliações com texto livre em um banco **chave-valor (Redis)**, por ser o ideal para percorrer relacionamentos complexos entre entidades.

### Questão 34 (Interpretação)

**Estímulo:**

> No Olist, o vendedor `seller_123` **mudou de São Paulo (SP) para Campinas (SP)**. A equipe precisa decidir como registrar essa mudança na `dim_sellers` para que um relatório de "faturamento por cidade do vendedor" continue correto para as vendas antigas — feitas quando ele ainda estava em São Paulo.

Considerando as estratégias de Slowly Changing Dimensions, a decisão **mais adequada** é:

a. Usar **SCD Tipo 0**, mantendo a cidade fixa em São Paulo, já que atributos de vendedor nunca podem mudar.
b. Usar **SCD Tipo 1**, sobrescrevendo "São Paulo" por "Campinas", pois assim o histórico completo de mudanças fica preservado.
c. Não registrar a mudança, mantendo tudo como está, pois qualquer alteração corromperia irremediavelmente a tabela de fatos.
*d. Usar **SCD Tipo 2**, fechando a linha antiga (com data de fim) e criando uma nova (com data de início) e um indicador de linha atual, de modo que vendas passadas sigam atribuídas a São Paulo e as novas, a Campinas.
e. Usar **SCD Tipo 3**, que cria uma nova linha a cada mudança, sendo a única técnica capaz de preservar o histórico completo do vendedor.

### Questão 35 (Interpretação)

**Estímulo:**

> "Nosso pipeline Olist é **ELT**: vamos carregar os 9 CSVs crus primeiro (camada bronze e schema `raw`) e só então transformar com dbt. Guardar o cru dá **flexibilidade total para reprocessar**."

Seis meses após o pipeline no ar, o time de negócio muda a regra de cálculo do "faturamento por categoria". Qual conclusão é **mais bem suportada** pela escolha do padrão ELT?

a. Será preciso reextrair os 9 CSVs do Olist a partir do sistema-fonte, pois no ELT o dado cru é descartado logo após a transformação.
b. A mudança é impossível sem trocar o padrão para ETL, já que no ELT a lógica de transformação fica congelada e não pode ser alterada.
c. Como a transformação ocorreu antes da carga, a única saída é editar manualmente cada linha já materializada na estrela.
d. A nova regra exige migrar todo o pipeline para a nuvem, pois o reprocessamento não é viável em uma stack local com DuckDB.
*e. Como o dado cru foi preservado na bronze/`raw`, basta **reexecutar a etapa de transformação (dbt)** com a nova regra sobre o mesmo dado bruto, sem reextrair a fonte — exatamente a flexibilidade que motiva o ELT.

### Questão 36 (Interpretação)

**Estímulo:**

> Arquitetura-alvo do pipeline: **9 CSVs (Olist)** → **Python/DuckDB** (ingestão) → **DuckDB schema `raw` + Parquet bronze** → **dbt** (staging → estrela → marts) → **gold (Parquet)** → **BI (Metabase) / ML (scikit-learn)** — tudo **orquestrado pelo Airflow**.

A leitura mais coerente com a arquitetura é:

*a. O dado percorre um fluxo em camadas — da geração nos CSVs à disponibilização para BI e ML —, com o Airflow orquestrando as etapas e cada ferramenta cumprindo um papel específico (DuckDB ingere e consulta, dbt transforma, Metabase/scikit-learn consomem).
b. O Airflow é o motor que executa as consultas SQL e substitui o DuckDB na etapa de transformação da estrela.
c. O dbt é a ferramenta usada para ingerir os CSVs crus do Olist e convertê-los diretamente em Parquet bronze.
d. O modelo de machine learning em scikit-learn é treinado sobre os CSVs crus, sem passar pela camada gold da estrela.
e. A arquitetura elimina a etapa de armazenamento, pois o dado vai direto da ingestão para o BI sem persistir em Parquet ou DuckDB.

### Questão 37 (Interpretação)

**Estímulo:**

> No sistema-fonte do Olist, registrar um **pedido com seu pagamento** é uma transação que precisa ser **atômica**: ou as duas coisas acontecem, ou nenhuma — não pode existir pedido pago sem registro de pagamento. É por isso que marketplaces rodam sobre bancos ACID na operação.

Suponha que o servidor caia exatamente **entre** gravar o pedido e gravar o pagamento. A leitura **mais correta**, à luz da atomicidade, é:

a. O pedido é mantido gravado e o pagamento é aplicado depois automaticamente, pois a atomicidade garante que a segunda operação sempre se complete sozinha.
*b. A transação inteira é desfeita (rollback): nem o pedido nem o pagamento permanecem gravados, pois a atomicidade exige que a transação seja "tudo ou nada", evitando um pedido pago sem registro de pagamento.
c. O pedido é gravado e o pagamento é descartado, mas o pedido permanece válido, pois a atomicidade só se aplica à primeira operação da transação.
d. Ambos permanecem gravados de forma independente, pois cada operação é uma transação separada e a atomicidade não as vincula.
e. A atomicidade não tem efeito nesse caso, pois só a durabilidade decide o que acontece após uma queda do servidor.

### Questão 38 (Interpretação)

**Estímulo:**

> O dataset Olist tem cerca de **99 mil pedidos** distribuídos ao longo de aproximadamente 2 anos (2016–2018). Suponha, para efeito de estimativa, exatamente 730 dias no período.

Qual é a **média aproximada de pedidos por dia** no período?

a. Cerca de 50 pedidos/dia.
b. Cerca de 990 pedidos/dia.
*c. Cerca de 135 pedidos/dia.
d. Cerca de 1.350 pedidos/dia.
e. Cerca de 13 pedidos/dia.

### Questão 39 (Interpretação)

**Estímulo:**

> A fato `fct_order_items` do Olist tem grão de item: são cerca de **112.650 itens**. Suponha que cada linha ocupe 80 bytes. Hoje, isso dá cerca de 9 MB — o dataset inteiro cabe folgado na memória do laptop. Mas projete o Olist na escala da Amazon, **1.000 vezes maior** em número de itens.

Qual o tamanho aproximado da fato **nessa escala projetada**, mantido o mesmo tamanho de linha?

a. Cerca de 90 MB.
b. Cerca de 900 MB.
c. Cerca de 90 GB.
*d. Cerca de 9 GB.
e. Cerca de 9 TB.

### Questão 40 (Interpretação)

**Estímulo:**

> "No OLAP queremos o oposto do OLTP: **desnormalização**. Juntar dados em poucas tabelas largas reduz os *joins* que uma consulta analítica precisa fazer. No Olist, em vez de juntar 4 tabelas a cada pergunta, vamos pré-juntar os itens com pedido, produto e vendedor numa única **fato larga**. Aceitamos a redundância em troca de velocidade."

A leitura mais coerente com o texto é:

a. A desnormalização visa eliminar toda a redundância do modelo, seguindo rigorosamente a 3ª Forma Normal em cada tabela da estrela.
b. Pré-juntar os dados numa fato larga torna as consultas analíticas mais lentas, pois aumenta o número de joins necessários por pergunta.
c. A desnormalização é indicada para o banco OLTP de produção do Olist, onde cada pedido é registrado individualmente.
d. A redundância introduzida pela desnormalização inviabiliza qualquer consulta analítica, motivo pelo qual o Olist deve permanecer sempre normalizado.
*e. A desnormalização troca conscientemente espaço (mais redundância) por velocidade de consulta: ao pré-juntar itens, pedido, produto e vendedor numa fato larga, cada análise passa a exigir menos joins, ganhando desempenho.

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

### Questão 21

- **a.** *Correta!* Ambas verdadeiras e a II justifica a I. A orquestração (Airflow) é, de fato, uma **corrente transversal**, não uma etapa; e a Razão explica **por quê**: as correntes transversais atravessam todas as etapas do ciclo (geração → ingestão → transformação → armazenamento → disponibilização), em vez de ocorrerem num único momento — exatamente a causa da afirmação da Asserção.
- **b.** Incorreta. A Razão justifica diretamente a Asserção (é o que define uma corrente transversal).
- **c.** Incorreta. A Razão é verdadeira.
- **d.** Incorreta. A Asserção é verdadeira.
- **e.** Incorreta. Ambas são verdadeiras.

### Questão 22

- **a.** Incorreta. A Razão não justifica a Asserção — tratam de temas independentes.
- **b.** *Correta!* As duas proposições são individualmente verdadeiras: o Avro é, de fato, um formato por linha com esquema embutido, adequado a ingestão e streaming (o stream de pedidos da Aula 7); e o modelo relacional foi mesmo proposto por Codd em 1970, com tabelas ligadas por chaves. Mas a Razão (modelo relacional) **não explica** por que o Avro serve para streaming — são fatos sem relação de causa.
- **c.** Incorreta. A Razão é verdadeira.
- **d.** Incorreta. A Asserção é verdadeira.
- **e.** Incorreta. Ambas são verdadeiras.

### Questão 23

- **a.** Incorreta. A Razão é falsa.
- **b.** Incorreta. A Razão é falsa.
- **c.** *Correta!* A Asserção é verdadeira: a arquitetura Medallion organiza os dados em bronze, silver e gold, e a bronze guarda o dado cru em Parquet. A Razão é **falsa**: guardar o cru **não** é desnecessário — preservar a bronze é justamente o que dá **flexibilidade para reprocessar** a estrela sob novas regras sem reextrair a fonte; descartá-lo destruiria essa capacidade.
- **d.** Incorreta. A Asserção é verdadeira.
- **e.** Incorreta. A Asserção é verdadeira.

### Questão 24

- **a.** Incorreta. A Asserção é falsa.
- **b.** Incorreta. A Asserção é falsa.
- **c.** Incorreta. A Razão é verdadeira.
- **d.** *Correta!* A Asserção é **falsa**: em `orders`, quem identifica unicamente cada linha é o **order_id** (chave primária); o **customer_id** é **chave estrangeira** para `customers`, não chave primária. A Razão é verdadeira: o `order_id` é a espinha dorsal que costura `orders ↔ order_items ↔ order_payments ↔ order_reviews`.
- **e.** Incorreta. A Razão é verdadeira.

### Questão 25

- **a.** Incorreta. Ambas são falsas.
- **b.** Incorreta. Ambas são falsas.
- **c.** Incorreta. A Razão também é falsa.
- **d.** Incorreta. A Asserção também é falsa.
- **e.** *Correta!* Ambas são falsas. A Asserção inverte o teorema: "AP" **mantém** a tolerância a partição (P é inevitável) e, durante a partição, prioriza **disponibilidade (A)** sacrificando a consistência — não abre mão de P nem garante C e A plenas ao mesmo tempo. A Razão troca as propriedades ACID: quem garante que a transação confirmada sobrevive a falhas é a **Durabilidade**, não o **Isolamento** (que trata da não interferência entre transações simultâneas).

### Questão 26

- **a.** *Correta!* Ambas verdadeiras e a II justifica a I. O DuckDB lendo os CSVs com `read_csv_auto` é mesmo um caso de schema-on-read (infere os tipos na leitura), e a Razão explica **por quê**: no schema-on-read o dado é gravado cru, sem esquema imposto na escrita, e interpretado só na leitura — exatamente o mecanismo que torna a afirmação da Asserção verdadeira e ideal para a bronze.
- **b.** Incorreta. A Razão justifica diretamente a Asserção.
- **c.** Incorreta. A Razão é verdadeira.
- **d.** Incorreta. A Asserção é verdadeira.
- **e.** Incorreta. Ambas são verdadeiras.

### Questão 27

- **a.** Incorreta. A Razão não justifica a Asserção.
- **b.** *Correta!* As duas proposições são verdadeiras: a família documento (MongoDB) casa bem com as reviews do Olist (campos opcionais + texto livre); e é verdade que cerca de 80% dos dados do mundo são não estruturados. Porém, a Razão (percentual de dados não estruturados) **não explica** por que o documento é adequado às reviews — a adequação vem da estrutura flexível/aninhada, não do percentual global. São fatos independentes.
- **c.** Incorreta. A Razão é verdadeira.
- **d.** Incorreta. A Asserção é verdadeira.
- **e.** Incorreta. Ambas são verdadeiras.

### Questão 28

- **a.** Incorreta. A Razão é falsa.
- **b.** Incorreta. A Razão é falsa.
- **c.** *Correta!* A Asserção é verdadeira: o grão da `fct_order_items` é **um item de pedido por linha**, a granularidade mais fina. A Razão é **falsa**: um pedido do Olist tem, em média, **vários** itens (não exatamente um) — cada pedido tem em torno de 1,13 item, e há pedidos com múltiplos itens; por isso, fixar o grão no pedido inteiro **perderia** o detalhe por item, e não permitiria o faturamento por item como afirmado.
- **d.** Incorreta. A Asserção é verdadeira.
- **e.** Incorreta. A Asserção é verdadeira.

### Questão 29

- **a.** Incorreta. A Asserção é falsa.
- **b.** Incorreta. A Asserção é falsa.
- **c.** Incorreta. A Razão é verdadeira.
- **d.** *Correta!* A Asserção é **falsa**: escrever o script de ingestão (CSV → Parquet) e materializar o schema `raw` é trabalho do **engenheiro de dados**, não do cientista. A Razão é verdadeira: a entrega típica do engenheiro no Olist é a `fct_order_items` confiável e disponível, base sobre a qual o cientista treina o modelo de previsão de atraso.
- **e.** Incorreta. A Razão é verdadeira.

### Questão 30

- **a.** Incorreta. Ambas são falsas.
- **b.** Incorreta. Ambas são falsas.
- **c.** Incorreta. A Razão também é falsa.
- **d.** Incorreta. A Asserção também é falsa.
- **e.** *Correta!* Ambas são falsas. A `olist_geolocation_dataset` é uma **tabela** (colunas e tipos bem definidos): é dado **estruturado**, por mais linhas que tenha. E a Razão é falsa: o grau de estrutura **não** depende da quantidade de linhas, mas de o dado ter (ou não) um esquema fixo em colunas — volume não converte uma tabela em dado não estruturado.

### Questão 31

- **a.** *Correta!* É exatamente a tese do texto: as correntes transversais permeiam todas as etapas do ciclo de vida, de modo que orquestração, qualidade e governança são endereçadas ao longo de todo o pipeline Olist, e não numa fase isolada.
- **b.** Incorreta. O texto diz o oposto: elas **não** são uma etapa, e sim preocupações de todas as etapas.
- **c.** Incorreta. Governança e qualidade atravessam todas as etapas, não só a geração.
- **d.** Incorreta. A orquestração (Airflow) e a verificação de qualidade (dbt tests, Great Expectations) são correntes distintas e complementares; uma não anula a outra.
- **e.** Incorreta. As correntes transversais valem para qualquer pipeline, inclusive o local do Olist.

### Questão 32

- **a.** Incorreta. O CSV **não** é colunar nem comprimido; é texto puro, ruim para agregações analíticas.
- **b.** *Correta!* A camada analítica (gold) deve ser **Parquet**: colunar, comprimido e capaz de ler só as colunas necessárias. O CSV é texto sem tipos e sem compressão, próprio para troca e ingestão, não para analytics — a proposta é inadequada.
- **c.** Incorreta. CSV e Parquet têm desempenhos de leitura muito diferentes em cargas analíticas; o Parquet vence com folga.
- **d.** Incorreta. O Avro é um formato **por linha**, ótimo para streaming, não é o colunar recomendado para analytics — esse papel é do Parquet.
- **e.** Incorreta. O CSV é texto, não binário nem tipado; ao contrário, exige inferência de tipos na leitura (schema-on-read).

### Questão 33

- **a.** Incorreta. O carrinho ativo (pares chave→valor) pede um banco **chave-valor** (Redis/DynamoDB), não grafo.
- **b.** Incorreta. Bancos colunares como o Cassandra tendem a AP/consistência eventual; o pagamento pede **relacional com ACID** forte, não Cassandra.
- **c.** *Correta!* O stream de cliques/eventos é escrita massiva e contínua; um banco **colunar de escrita massiva** (Cassandra), que escala horizontalmente, casa com esse padrão de acesso.
- **d.** Incorreta. A rede "cliente → comprou de → vendedor" é caso de **grafo** (Neo4j); o MongoDB não é "o único" a armazenar JSON, e não é o ideal para percorrer relacionamentos.
- **e.** Incorreta. Percorrer relacionamentos complexos é força do **grafo**, não do chave-valor; e as reviews com texto livre casam com a família **documento**.

### Questão 34

- **a.** Incorreta. SCD Tipo 0 fixa o atributo e ignora a mudança real; o vendedor de fato mudou de cidade.
- **b.** Incorreta. O SCD Tipo 1 sobrescreve e **perde** a história — as vendas antigas passariam a mentir a cidade (Campinas em vez de São Paulo).
- **c.** Incorreta. Registrar a mudança com SCD Tipo 2 **não** corrompe a fato; ao contrário, é o que mantém os relatórios corretos.
- **d.** *Correta!* O SCD Tipo 2 fecha a linha antiga (data de fim) e cria uma nova (data de início) com indicador de linha atual, preservando o histórico: vendas passadas seguem atribuídas a São Paulo, as novas a Campinas.
- **e.** Incorreta. Quem cria nova linha a cada mudança é o Tipo **2**, não o Tipo 3 — o Tipo 3 guarda só a versão anterior e a atual em colunas da mesma linha, sem histórico completo.

### Questão 35

- **a.** Incorreta. No ELT o dado cru é **preservado** (bronze/`raw`), justamente para não precisar reextrair a fonte.
- **b.** Incorreta. A lógica de transformação do dbt é editável a qualquer momento; o ELT não a congela.
- **c.** Incorreta. Não é preciso editar linha a linha: reexecuta-se a transformação sobre o cru preservado.
- **d.** Incorreta. O reprocessamento é perfeitamente viável na stack local (DuckDB + dbt); não exige nuvem.
- **e.** *Correta!* Como o dado cru foi preservado na bronze/`raw`, basta reexecutar a etapa de transformação (dbt) com a nova regra sobre o mesmo dado bruto, sem reextrair a fonte — a flexibilidade que motiva o ELT.

### Questão 36

- **a.** *Correta!* É a leitura correta da arquitetura: o dado flui em camadas, da geração (CSVs) à disponibilização (BI/ML), com o Airflow orquestrando e cada ferramenta em seu papel (DuckDB ingere/consulta, dbt transforma, Metabase e scikit-learn consomem).
- **b.** Incorreta. O Airflow **orquestra** (agenda e coordena) as etapas; quem executa o SQL e resolve a transformação é o DuckDB/dbt.
- **c.** Incorreta. Quem ingere os CSVs e gera o Parquet bronze é o **Python/DuckDB**; o dbt entra depois, transformando o `raw` em staging e estrela.
- **d.** Incorreta. O modelo de ML consome a camada **gold** (estrela), não os CSVs crus.
- **e.** Incorreta. A etapa de armazenamento existe e é central: o dado persiste em Parquet e no DuckDB antes de chegar ao BI.

### Questão 37

- **a.** Incorreta. A atomicidade não "completa sozinha" a segunda operação; ela desfaz a transação incompleta.
- **b.** *Correta!* Pela atomicidade, a transação é "tudo ou nada": se o servidor cai no meio, faz-se rollback e **nem** o pedido **nem** o pagamento permanecem — evitando um pedido pago sem registro de pagamento.
- **c.** Incorreta. A atomicidade abrange a transação inteira, não apenas a primeira operação; manter só o pedido violaria a garantia.
- **d.** Incorreta. Pedido + pagamento formam **uma** transação atômica; não são operações independentes.
- **e.** Incorreta. A atomicidade é justamente o que decide o desfazer nesse caso; a durabilidade trata do que já foi **confirmado** persistir, não desta transação interrompida.

### Questão 38

- **a.** Incorreta. 50/dia subestima muito (usaria um denominador de dias muito maior que 730).
- **b.** Incorreta. ~990/dia resultaria de dividir por ~100 dias, não pelos ~730 do período.
- **c.** *Correta!* 99.000 ÷ 730 ≈ **135 pedidos/dia**, a média citada na unidade.
- **d.** Incorreta. ~1.350/dia seria um erro de uma ordem de grandeza (10×) sobre a média correta.
- **e.** Incorreta. ~13/dia subestima em cerca de 10× a média real.

### Questão 39

- **a.** Incorreta. 90 MB corresponderia a apenas 10× a escala, não 1.000×.
- **b.** Incorreta. 900 MB corresponderia a 100×, não 1.000×.
- **c.** Incorreta. 90 GB seria 10× além da escala pedida (erro de uma ordem de grandeza).
- **d.** *Correta!* 9 MB × 1.000 = **9 GB** (equivalente a 112.650 × 1.000 × 80 bytes ≈ 9 × 10⁹ bytes).
- **e.** Incorreta. 9 TB corresponderia a 1 milhão de vezes a escala, não mil.

### Questão 40

- **a.** Incorreta. A desnormalização faz o **oposto** de perseguir a 3FN: ela aceita redundância nas tabelas largas da estrela.
- **b.** Incorreta. Pré-juntar numa fato larga **reduz** os joins por consulta, tornando a análise mais rápida, não mais lenta.
- **c.** Incorreta. A desnormalização é para o destino **OLAP** (estrela); o OLTP de produção do Olist permanece normalizado.
- **d.** Incorreta. A redundância da desnormalização **acelera** as consultas analíticas; ela não as inviabiliza, e por isso a estrela não permanece normalizada.
- **e.** *Correta!* É a leitura correta: a desnormalização troca conscientemente mais espaço/redundância por velocidade — ao pré-juntar itens, pedido, produto e vendedor numa fato larga, cada análise exige menos joins e ganha desempenho.
