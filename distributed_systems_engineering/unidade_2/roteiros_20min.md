# Roteiros das videoaulas 5 a 8

Duração-base: 20 minutos por videoaula (aproximadamente 2.200 a 2.700 palavras faladas).  
Disciplina: Distributed Systems Engineering — Unidade 2 — Dados distribuídos, consistência e coordenação.  
Estes roteiros são textos de narração para gravação, complementares ao texto-base de `unidade_2.md`. Priorizam demonstração, exemplo e aplicação profissional, evitando repetir literalmente o texto escrito.

---

## Videoaula 5 — “Três cópias, três respostas: qual está certa?”

**Vínculo com o plano de aprendizagem:** Aula 5 — Replicação e modelos de consistência.

**Objetivo da videoaula:** demonstrar, com um exemplo prático de leitura obsoleta, por que réplicas divergem por alguns instantes, e ensinar o estudante a escolher entre replicação síncrona, assíncrona e por quórum para diferentes tipos de dado.

### Abertura contextualizada

Olá! Seja bem-vindo a mais uma aula da nossa disciplina de Engenharia de Sistemas Distribuídos. Hoje eu quero começar com uma pergunta simples, mas que gera muita confusão em produção: se eu tenho três cópias do mesmo dado, e cada uma delas responde de um jeito diferente à mesma pergunta, qual delas está certa?

*[indicação de edição: inserir tela cheia com o texto "Três cópias, três respostas: qual está certa?" sobre fundo escuro, com transição suave para o apresentador]*

A resposta, que vamos construir juntos ao longo desses vinte minutos, é: pode ser que nenhuma esteja errada. Isso mesmo. Réplicas podem divergir por um curto período de tempo sem que isso seja, necessariamente, um defeito do sistema. O problema não é a divergência em si — é não sabermos, de antemão, se ela é aceitável ou não para aquele dado específico.

Vamos retomar o caso da NexaOrder, nossa plataforma fictícia de pedidos que estamos acompanhando desde a Unidade 1. Depois de decompor o sistema em serviços independentes, a equipe da NexaOrder replicou o banco de dados de cada serviço para ganhar disponibilidade. Só que, durante uma promoção relâmpago, um cliente consultou o preço de um produto três vezes seguidas e recebeu três valores diferentes. E pior: duas pessoas conseguiram reservar a última unidade do mesmo item. Vamos entender exatamente por que isso acontece — e como evitar.

E antes de entrar nos mecanismos, vale alinhar uma expectativa: não existe replicação sem algum tipo de compromisso. Não existe uma configuração mágica que ofereça, ao mesmo tempo, a menor latência possível, a maior disponibilidade possível e a garantia de que toda leitura sempre reflete a escrita mais recente. Essas três coisas puxam em direções opostas. O que existe é a possibilidade de escolher, dado por dado, qual combinação faz sentido — e é exatamente essa escolha que vamos praticar hoje.

### Desenvolvimento conceitual

Primeiro, por que replicamos dados? Existem quatro motivos principais: disponibilidade, porque se um nó cai, outro responde; redução de latência, porque um cliente pode ser atendido pela réplica mais próxima geograficamente; escalabilidade de leitura, porque muitas réplicas conseguem absorver muito mais consultas do que um único nó; e durabilidade, porque perder um nó não significa perder o dado.

*[indicação de edição: inserir infográfico com os quatro motivos de replicação, aparecendo um a um conforme cada um é mencionado na fala]*

Agora, existem basicamente dois jeitos de organizar essas cópias. No modelo líder-seguidor, ou primário-réplica, um único nó recebe as escritas e as propaga para os demais. É simples de raciocinar, porque nunca existem dois nós tentando decidir o valor certo ao mesmo tempo. No modelo multi-líder, mais de um nó aceita escritas — útil, por exemplo, quando você tem centros de distribuição em países diferentes, cada um escrevendo localmente para reduzir latência. O preço é que, se dois líderes recebem escritas conflitantes sobre o mesmo dado quase ao mesmo tempo, alguém precisa decidir como resolver esse conflito.

E aqui entra a segunda decisão importante: quando a escrita é considerada "pronta"? Na replicação síncrona, o líder só confirma para o cliente depois que uma ou mais réplicas já confirmaram ter recebido o dado. Isso é mais seguro, mas mais lento. Na replicação assíncrona, o líder confirma na hora e propaga em segundo plano — mais rápido, mas com uma janela de risco: se o líder cair antes de propagar, aquele dado pode se perder.

Esse intervalo entre a escrita no líder e a aplicação na réplica tem nome: atraso de réplica, ou *replication lag*. E é exatamente esse atraso que explica o caso do catálogo da NexaOrder. Cada consulta pode ter sido atendida por uma réplica diferente, cada uma em um ponto diferente da sua própria janela de atraso.

*[indicação de edição: inserir linha do tempo animada mostrando o líder confirmando uma escrita no instante zero e uma réplica aplicando essa mesma escrita 150 milissegundos depois, com uma "janela de leitura obsoleta" destacada em vermelho entre os dois pontos]*

Mas nem tudo, entre consistência forte e consistência eventual pura, precisa custar caro. Existem garantias intermediárias, chamadas de garantias centradas no cliente, que resolvem boa parte do desconforto que um usuário sentiria. A leitura das próprias escritas garante que você sempre veja as alterações que você mesmo fez, mesmo que outra pessoa, em outra réplica, ainda não veja. Leituras monotônicas garantem que, uma vez que você viu um valor mais novo, você nunca vai ver, depois, um valor mais antigo — sem essa garantia, seria possível atualizar a página e "voltar no tempo", o que é extremamente confuso para quem está usando o sistema. Escritas monotônicas garantem que as suas próprias escritas sejam aplicadas na ordem em que você as fez. E leitura de prefixo consistente garante que, se uma escrita depende causalmente de outra, ninguém observa a segunda sem ter observado a primeira. Nenhuma dessas quatro garantias exige o custo de uma consistência forte global — e, juntas, elas evitam a maior parte das reclamações de "o sistema está bugado" que, na verdade, são apenas replicação mal comunicada ao usuário.

### Demonstração, exemplo e estudo de caso

Vamos colocar números nisso. Imagine que o líder confirma uma atualização de preço no instante zero. A réplica que está mais distante, geograficamente, aplica essa mesma atualização 150 milissegundos depois. Se um cliente fizer uma leitura nessa réplica exatamente nesses 150 milissegundos, ele vai ver o preço antigo. Não é um bug. É uma consequência direta da escolha de replicação assíncrona.

Agora, como resolvemos isso sem simplesmente forçar tudo para consistência forte, que é cara em latência? Usamos quóruns. Se um dado é replicado em $N$ nós, definimos que toda escrita precisa ser confirmada por $W$ réplicas, e toda leitura precisa consultar $R$ réplicas. A regra de ouro é: $W$ mais $R$ tem que ser maior que $N$. Por quê? Porque isso garante que o conjunto de réplicas que você acabou de escrever e o conjunto de réplicas que você está lendo, obrigatoriamente, têm pelo menos um nó em comum.

Vamos a um exemplo concreto: cinco réplicas, $N$ igual a cinco. Se eu escolher $W$ igual a três e $R$ igual a três, três mais três é seis, que é maior que cinco. Então, qualquer leitura que consulte três réplicas vai necessariamente tocar em pelo menos uma réplica que participou da última escrita confirmada — e aquela réplica vai "puxar" o valor mais atual para a resposta.

*[indicação de edição: inserir diagrama animado com cinco círculos representando nós; destacar três deles em azul para o conjunto de escrita, depois destacar três em verde para o conjunto de leitura, evidenciando o nó que aparece nas duas cores]*

E não existe apenas uma forma de configurar esse quórum — existem várias, cada uma com um efeito diferente. Se eu escolher $W$ igual a um e $R$ igual a $N$, a escrita fica extremamente rápida, porque basta uma réplica confirmar, mas a leitura fica lenta e cara, porque precisa consultar todo mundo para ter certeza. Se eu inverto, $W$ igual a $N$ e $R$ igual a um, a leitura fica rápida, mas agora é a escrita que precisa esperar a confirmação de todas as réplicas — e se uma única réplica estiver fora do ar, a escrita trava. Nenhuma dessas três configurações — nem a extremamente rápida em escrita, nem a extremamente rápida em leitura, nem a equilibrada com três e três — é "a certa" em abstrato. A certa é a que atende ao padrão de uso do dado específico que você está modelando.

E o que a NexaOrder decidiu fazer, no fim das contas? Para o catálogo, a equipe aceitou consistência eventual: o preço pode demorar alguns segundos para propagar, e isso não quebra o negócio. Para o estoque, adotaram quórum com sobreposição garantida, porque vender a mesma unidade duas vezes custa muito mais caro do que uma escrita um pouco mais lenta. E para o pagamento, foram ainda mais rígidos, próximos de consistência forte, porque ali o risco de erro é financeiro e direto.

Repare que essas três decisões, lado a lado, formam um mesmo sistema, com três configurações de replicação diferentes rodando ao mesmo tempo. Isso é absolutamente normal — e, aliás, desejável. Um erro comum de quem está começando na área é achar que "o banco de dados" tem uma única configuração de consistência para o sistema inteiro. Na prática, sistemas maduros tratam isso por tipo de dado, às vezes até por operação específica dentro do mesmo serviço.

*[indicação de edição: inserir tabela-resumo com três linhas — catálogo, estoque e pagamento — e colunas para modelo de consistência, tipo de replicação e justificativa de negócio]*

### Aplicação profissional

Se você trabalha, ou vai trabalhar, com bancos de dados distribuídos, essa decisão vai aparecer o tempo todo — geralmente disfarçada de parâmetro de configuração. Bancos como o Cassandra, por exemplo, permitem configurar o nível de consistência por operação, escolhendo efetivamente quantas réplicas precisam confirmar uma escrita ou responder a uma leitura. Um engenheiro que não entende esse compromisso tende a cometer um de dois erros: ou configura tudo para o nível mais forte possível "por segurança", pagando um custo de latência desnecessário em dados que não precisam disso; ou ignora completamente o assunto, até que um incidente como o da NexaOrder aconteça em produção.

Vale a pena, inclusive, levar essa pergunta para uma reunião de definição técnica antes mesmo de escolher qual banco de dados usar: em vez de perguntar "qual banco é mais rápido?", pergunte "para os dados que eu tenho, quais garantias de consistência esse banco me deixa configurar, e com qual granularidade?". Um banco que só oferece uma configuração global de consistência para todo o sistema é bem mais limitado, na prática, do que um banco que permite ajustar isso por tipo de operação ou por coleção de dados — exatamente a flexibilidade de que a NexaOrder precisou para tratar catálogo, estoque e pagamento de formas diferentes.

A pergunta profissional certa não é "esse sistema é consistente?". É: "para este dado específico, que garantia de consistência o negócio realmente exige, e qual o custo de entregar essa garantia?"

*[indicação de edição: inserir tela com a frase em destaque: "Para este dado, que garantia de consistência o negócio realmente exige?"]*

E vale um alerta final antes de fecharmos: essa decisão não é tomada uma única vez, no início do projeto, e depois esquecida. Um dado que hoje tolera consistência eventual pode, amanhã, passar a sustentar uma nova regra de negócio que exige mais rigor — imagine, por exemplo, a NexaOrder decidindo permitir que o cliente pague parte da compra com pontos de fidelidade, tornando o saldo de pontos tão sensível quanto o saldo financeiro já é hoje. Revisitar essa escolha periodicamente, à luz de como o dado está sendo usado, é parte do trabalho contínuo de manutenção de um sistema distribuído, não um projeto que se conclui e se arquiva.

### Fechamento

Hoje vimos que replicar dados resolve disponibilidade e latência, mas cria a necessidade de escolher, conscientemente, um modelo de consistência: forte, sequencial, causal ou eventual — e um mecanismo de replicação capaz de sustentar essa escolha, seja com líder único, múltiplos líderes, ou quóruns configuráveis. Vimos também que garantias centradas no cliente, como leitura das próprias escritas e leituras monotônicas, resolvem boa parte da percepção de inconsistência a um custo bem menor do que uma consistência forte global — e que quóruns de leitura e escrita, com a regra $W + R > N$, são uma ferramenta configurável para equilibrar tudo isso, dado a dado.

Se você levar uma única pergunta desta aula para a sua prática profissional, que seja esta: antes de configurar a replicação de qualquer dado novo, pergunte que garantia esse dado específico realmente precisa — e não copie a configuração padrão de outro dado só porque "sempre foi assim". Na próxima aula, vamos dar um passo além: e se um único nó não for suficiente nem para armazenar todos os dados, e não apenas para atender a todas as leituras? Vamos falar de particionamento, hashing consistente e o teorema CAP. Até lá!

*[indicação de edição: encerrar com a vinheta padrão da disciplina e texto de chamada para a Aula 6]*

### Indicações de edição e recursos visuais

- Abertura com tela de título animada (0:00–0:10).
- Infográfico dos quatro motivos de replicação (aproximadamente 1:30).
- Linha do tempo do atraso de réplica com janela de leitura obsoleta destacada (aproximadamente 5:00).
- Diagrama animado de quórum de leitura e escrita com cinco nós (aproximadamente 9:30).
- Tela de destaque com a pergunta profissional central (aproximadamente 15:30).
- Vinheta de encerramento com chamada para a próxima aula (últimos 15 segundos).

### Fontes e links de mídia

- KLEPPMANN, Martin. *Designing Data-Intensive Applications*. Sebastopol: O'Reilly Media, 2017. Capítulo 5 — usado como referência conceitual para o roteiro, sem uso de trecho de mídia externa.
- Nenhuma mídia de terceiros com direitos autorais foi utilizada; todos os diagramas descritos devem ser produzidos originalmente pela equipe de edição a partir das indicações acima.

---

## Videoaula 6 — “Dividir para crescer: como fatiar dados sem quebrar o sistema”

**Vínculo com o plano de aprendizagem:** Aula 6 — Particionamento, CAP e escalabilidade de dados.

**Objetivo da videoaula:** demonstrar como diferentes estratégias de particionamento reagem a um crescimento desigual de carga, e explicar, de forma aplicada, o teorema CAP e sua extensão PACELC.

### Abertura contextualizada

Bem-vindo de volta! Na aula passada, resolvemos o problema de manter várias cópias do mesmo dado coerentes entre si. Hoje o problema é outro: o que fazer quando o dado inteiro já não cabe — nem em desempenho, nem em armazenamento — em um único conjunto de réplicas?

*[indicação de edição: inserir tela cheia com o texto "Dividir para crescer: como fatiar dados sem quebrar o sistema"]*

A NexaOrder passou exatamente por isso. O catálogo de produtos cresceu para milhões de itens, e o histórico de pedidos passou a acumular bilhões de registros. Copiar essa base inteira em cada nó deixou de fazer sentido. A equipe precisava dividir os dados — não apenas replicá-los. E a primeira tentativa, cortar os produtos de "A" a "M" em um nó e de "N" a "Z" em outro, pareceu razoável até uma campanha publicitária concentrar tráfego em produtos que começavam com "S". Um nó ficou sobrecarregado; o outro, ocioso. Vamos entender por quê, e como evitar esse erro.

Esse é um erro clássico, e vale a pena dizer isso claramente logo no começo: dividir dados "no olho", por uma característica visível como a letra inicial do nome, é tentador porque parece intuitivo — mas quase nunca reflete o padrão real de uso do sistema. O particionamento correto não parte de "como o dado parece", parte de "como o dado é efetivamente consultado e escrito".

### Desenvolvimento conceitual

Particionar horizontalmente — o termo técnico em inglês é *sharding* — significa dividir um conjunto de dados em fatias menores, cada uma armazenada por um subconjunto de nós diferentes. Isso é diferente de replicação: replicação copia o dado inteiro; particionamento distribui fatias diferentes do mesmo conjunto. Na prática, os dois andam juntos: você particiona os dados, e depois replica cada partição, separadamente, para ganhar disponibilidade.

Existem três estratégias clássicas de particionamento. Por faixa, você atribui intervalos contíguos de uma chave a cada partição — foi o que a NexaOrder tentou primeiro, com o alfabeto. É ótimo para consultas por intervalo, mas sofre com pontos quentes quando a distribuição real dos dados não é uniforme. Por *hash*, você aplica uma função de espalhamento à chave, o que distribui tudo de forma bem mais uniforme, mas perde a eficiência de consultas por intervalo. E por diretório, você mantém uma tabela explícita de mapeamento entre chave e partição — flexível, mas com um componente adicional que também precisa ser mantido disponível.

Pense em quando cada uma faz mais sentido. Se o seu sistema faz, o tempo inteiro, consultas do tipo "todos os pedidos de fevereiro" ou "todos os pedidos da última semana", particionamento por faixa temporal é extremamente eficiente, porque a consulta atinge só as partições relevantes daquele intervalo. Já se o seu sistema faz, principalmente, buscas por um identificador específico — "me dê o pedido número tal" —, particionamento por hash tende a ser melhor, porque distribui a carga de forma uniforme sem favorecer nenhum intervalo. E se as regras de distribuição dos dados mudam com frequência, por decisão de negócio, e não apenas por volume — por exemplo, clientes de um plano premium sempre atendidos por um cluster dedicado —, o particionamento por diretório oferece o controle explícito que as outras duas estratégias não dão.

*[indicação de edição: inserir três diagramas lado a lado, um para cada estratégia, com o mesmo conjunto de dez chaves de exemplo sendo distribuído de formas diferentes em cada uma]*

Só que particionar por *hash* simples, calculando o resto da divisão do *hash* pelo número de nós, tem um problema sério: se você adiciona ou remove um nó, o número total muda, e quase todas as chaves são redistribuídas de uma vez. Isso é caro e perigoso em produção. A solução amplamente usada é o *hashing* consistente: organizamos o espaço de *hash* como um anel, cada nó ocupa uma ou mais posições nesse anel, e uma chave pertence ao primeiro nó encontrado ao percorrer o anel a partir da posição do seu *hash*. Quando um nó entra ou sai, só as chaves entre ele e o vizinho anterior no anel se movem — o resto do anel fica intocado.

### Demonstração, exemplo e estudo de caso

Vamos ver isso em números. Se eu tenho um anel com nove nós, e adiciono um décimo, a fração aproximada de chaves que precisa ser redistribuída é um dividido por dez mais um, ou seja, cerca de dez por cento. Compare isso com o *hash* simples por módulo, em que adicionar um décimo nó a um cluster de nove pode redistribuir a esmagadora maioria das chaves, porque o resultado do módulo muda para quase todo mundo.

*[indicação de edição: inserir animação do anel de hashing consistente, mostrando um nó novo sendo inserido e apenas o segmento adjacente do anel mudando de cor, enquanto o restante do anel permanece estático]*

Mas atenção: mesmo com *hashing* consistente bem implementado, existe um problema que ele não resolve sozinho — o ponto quente causado por uma única chave extremamente popular. Foi exatamente o que aconteceu na campanha da NexaOrder: não era a letra inicial do produto que estava concentrando tráfego, era um produto específico virando um fenômeno de vendas. Hashing distribui bem chaves diferentes entre si, mas não divide a carga de uma única chave sozinha. Para isso, a equipe precisou de outra tática: sufixar artificialmente essa chave quente com um número aleatório, criando "sub-chaves" que se espalham por partições diferentes, e agregando o resultado na hora da leitura.

E existe um detalhe prático que costuma passar batido: rebalancear partições não é só mover dados de um lugar para o outro — é fazer isso enquanto o sistema continua recebendo tráfego normalmente. Durante uma migração de partição, tanto a origem quanto o destino processam, ao mesmo tempo, requisições normais e a transferência dos dados migrados. Isso pode degradar a latência das duas partições temporariamente. Por isso, times experientes limitam a velocidade dessas migrações e, sempre que o negócio permite, programam esse tipo de operação para as janelas de menor tráfego — de madrugada, por exemplo, para um sistema de e-commerce como a NexaOrder.

*[indicação de edição: inserir gráfico simples mostrando a latência da partição de origem e da partição de destino aumentando levemente durante uma janela de migração, e voltando ao normal quando a migração termina]*

Agora, vamos falar do teorema que mais aparece em entrevistas técnicas de sistemas distribuídos: o CAP. Durante uma partição de rede — quando nós perdem a capacidade de se comunicar entre si —, um sistema não consegue entregar, ao mesmo tempo, consistência total e disponibilidade total. Ele precisa escolher. Se escolhe consistência, ele recusa ou atrasa respostas do lado que não pode garantir o valor mais recente — isso é um sistema CP. Se escolhe disponibilidade, ele continua respondendo dos dois lados da partição, aceitando o risco de valores divergentes que precisarão ser reconciliados depois — isso é um sistema AP.

*[indicação de edição: inserir diagrama de dois grupos de nós separados por uma marca de rede rompida, com dois caminhos alternativos animados: um mostrando os dois lados continuando a responder (rotulado AP), outro mostrando um lado recusando respostas (rotulado CP)]*

Só que partição de rede é um evento relativamente raro. O que acontece no dia a dia, o tempo inteiro, é outro compromisso: entre latência e consistência, mesmo sem nenhuma falha de rede. É isso que o PACELC adiciona à conversa: se há partição, você escolhe entre disponibilidade e consistência; senão, você escolhe entre latência e consistência. Um sistema que exige confirmação de todas as réplicas antes de responder paga esse custo em toda escrita, não só durante incidentes.

E vale reforçar algo que já apareceu na Aula 5, mas que ganha ainda mais peso aqui: não existe "o melhor banco de dados distribuído" em abstrato. Existe o banco de dados cujas escolhas de particionamento e de posicionamento no espectro CAP e PACELC combinam melhor com o seu padrão de carga. Um mesmo banco pode ser uma excelente escolha para o catálogo de produtos da NexaOrder e uma escolha arriscada para o saldo financeiro de pagamentos, dentro do mesmo sistema.

Isso muda completamente o jeito de conduzir uma entrevista técnica ou uma revisão de arquitetura sobre esse assunto. Perguntar apenas "esse banco é CP ou AP?" é incompleto, porque isso só descreve o comportamento em um cenário relativamente raro — uma partição de rede em andamento. A pergunta mais reveladora é: "no dia a dia, sem nenhuma falha, quanto essa escolha de consistência está custando em latência de escrita?" Um sistema pode ser tecnicamente CP e, ainda assim, ter uma latência de escrita perfeitamente aceitável para o seu caso de uso — ou pode ser AP e ainda assim decepcionar, se a divergência entre réplicas gerar retrabalho constante de reconciliação.

### Aplicação profissional

Quando você avalia um banco de dados distribuído para um projeto novo, a pergunta "ele é CP ou AP?" é só o começo. A pergunta mais útil no dia a dia é sobre o comportamento normal, sem falhas: qual é a latência típica de escrita, e o que ela custa em termos de consistência garantida? Bancos como muitos sistemas de documentos ou colunares amplamente usados na indústria tendem a priorizar disponibilidade e latência baixa por padrão — o que é uma escolha excelente para um catálogo de produtos, e uma escolha arriscada para um saldo financeiro sem ajustes adicionais de configuração.

Escolher a chave de partição, também, não é um detalhe técnico menor — é uma decisão de arquitetura que precisa refletir os padrões de consulta reais do seu domínio. Perguntar "como esse dado é mais consultado?" antes de "como esse dado é mais escrito?" costuma evitar boa parte dos problemas de ponto quente.

E essa decisão, uma vez tomada, tende a ser cara de reverter depois. Migrar de uma chave de partição para outra, em um sistema já em produção com dados reais, normalmente significa reprocessar e mover uma fração significativa dos dados — o tipo de projeto que consome semanas de trabalho de engenharia, não apenas uma alteração de configuração. Por isso, investir tempo analisando o padrão de consulta antes de definir a chave de partição costuma valer muito mais a pena do que corrigir essa escolha depois que o sistema já está em produção com milhões de registros.

*[indicação de edição: inserir tela com a frase em destaque: "A chave de partição deve seguir o padrão de consulta, não o alfabeto"]*

Outro ponto importante para a vida profissional: particionamento e replicação quase sempre aparecem juntos, não como alternativas. Um cluster de dados real costuma ter, digamos, várias dezenas de partições, e cada partição, por sua vez, replicada em três ou cinco nós, como vimos na aula passada. Isso significa que, quando um único nó físico falha, normalmente ele não derruba o sistema inteiro — ele afeta apenas as partições cujas réplicas ele hospedava, e, mesmo assim, só se as outras réplicas dessas partições específicas também estiverem indisponíveis ao mesmo tempo. Entender essa combinação entre as duas técnicas é o que separa quem sabe a teoria isoladamente de quem consegue desenhar a arquitetura de dados de um sistema real.

### Fechamento

Recapitulando: particionamento distribui volume entre nós; *hashing* consistente reduz drasticamente o custo de rebalanceamento; pontos quentes exigem tratamento específico, mesmo com boa estratégia de partição; e o CAP, estendido pelo PACELC, descreve os compromissos entre consistência, disponibilidade e latência que todo sistema distribuído de dados precisa assumir explicitamente.

Guarde também a lição por trás do erro inicial da NexaOrder: escolher uma chave de partição pelo formato do dado — como a letra inicial de um nome — é diferente de escolher uma chave de partição pelo padrão real de consulta e escrita do sistema. A primeira parece mais simples de explicar; a segunda é a que efetivamente evita pontos quentes em produção. Na próxima aula, vamos ver como um conjunto de nós concorda automaticamente sobre quem é o líder, evitando o tipo de confusão que vimos brevemente hoje. Até lá!

*[indicação de edição: encerrar com vinheta padrão e chamada para a Aula 7]*

### Indicações de edição e recursos visuais

- Tela de título animada (0:00–0:10).
- Três diagramas comparativos de estratégias de particionamento (aproximadamente 2:30).
- Animação do anel de *hashing* consistente com inserção de nó (aproximadamente 6:30).
- Diagrama de partição de rede com dois caminhos CP/AP (aproximadamente 11:00).
- Tela de destaque com a frase sobre chave de partição (aproximadamente 16:30).
- Vinheta de encerramento com chamada para a próxima aula.

### Fontes e links de mídia

- KLEPPMANN, Martin. *Designing Data-Intensive Applications*. Sebastopol: O'Reilly Media, 2017. Capítulo 6 — referência conceitual para particionamento e *hashing* consistente.
- Nenhuma mídia de terceiros com direitos autorais foi utilizada; diagramas devem ser produzidos originalmente pela equipe de edição.

---

## Videoaula 7 — “Cinco nós, um líder: como o Raft evita o split-brain”

**Vínculo com o plano de aprendizagem:** Aula 7 — Consenso, eleição de líder e Raft.

**Objetivo da videoaula:** demonstrar, com uma simulação de eleição, como o algoritmo Raft garante um único líder por termo e mantém um log replicado consistente mesmo com falha de nós.

### Abertura contextualizada

Olá novamente! Vou começar contando o que aconteceu numa madrugada, na nossa NexaOrder fictícia. O nó líder responsável pelo estoque da região sul ficou inacessível por uma falha de rede. Dois operadores de plantão, sem se falar, promoveram dois nós diferentes a líder quase ao mesmo tempo. Por alguns minutos, o sistema teve dois líderes aceitando escritas de estoque simultaneamente. Isso tem um nome: *split-brain*. E o resultado foi reservas de estoque divergentes, que a equipe teve que reconciliar manualmente depois.

*[indicação de edição: inserir tela cheia com o texto "Cinco nós, um líder: como o Raft evita o split-brain"]*

A pergunta de hoje é: como automatizar essa decisão de "quem é o líder" de um jeito que nunca dois nós cheguem a essa conclusão ao mesmo tempo, mesmo com falhas de rede no meio do caminho? A resposta que vamos estudar é o algoritmo Raft — hoje, provavelmente, o algoritmo de consenso mais usado e mais didático em sistemas de produção.

Vale registrar por que o Raft ficou tão popular. Antes dele, o algoritmo de consenso mais citado na literatura era o Paxos, conhecido por resolver o problema corretamente, mas por ser notoriamente difícil de entender e de implementar corretamente. Os autores do Raft — que você vai encontrar na referência bibliográfica desta aula — tinham um objetivo explícito de projeto: criar um algoritmo com as mesmas garantias formais do Paxos, mas organizado de um jeito que um estudante, ou um engenheiro em produção, conseguisse acompanhar o raciocínio passo a passo. É esse objetivo de compreensibilidade que torna o Raft um ótimo ponto de partida para estudar consenso.

Isso tem uma implicação prática que vale destacar: quando um algoritmo é mais fácil de entender corretamente, ele também é mais fácil de implementar, de depurar e de auditar corretamente. Um bug sutil em uma implementação de consenso pode significar exatamente o tipo de inconsistência silenciosa que discutimos ao longo desta unidade — dados divergentes sem que ninguém perceba de imediato. Por isso, a clareza de um algoritmo não é apenas uma conveniência acadêmica; é, em si, uma característica de engenharia que reduz risco operacional.

### Desenvolvimento conceitual

Vamos começar pelo problema geral: consenso é fazer um conjunto de nós concordar sobre um único valor, mesmo que alguns falhem, de um jeito válido, uniforme entre todos os nós corretos, e irrevogável depois de decidido. Isso aparece toda vez que um sistema precisa de uma única fonte de verdade — "quem é o líder", "qual foi a próxima operação do log", "qual transação foi confirmada".

Repare que resolver consenso manualmente, como os dois operadores de plantão da NexaOrder tentaram fazer naquela madrugada, não é uma falha de atenção isolada — é uma tentativa humana de resolver, sob pressão e sem coordenação entre si, exatamente o problema que um algoritmo formal como o Raft foi desenhado para resolver de forma automática e correta.

Algoritmos de consenso como o Raft resolvem isso com o princípio de maioria: uma decisão só vale se aceita por mais da metade dos nós. Para um cluster de $N$ nós, o número de falhas toleradas, mantendo capacidade de formar maioria, é o piso de $N$ menos um, dividido por dois. Em um cluster de cinco nós, isso dá dois: você tolera a falha de até dois nós e ainda forma maioria com os três restantes. É por isso que clusters de consenso, na prática, quase sempre têm um número ímpar de nós.

*[indicação de edição: inserir tela com a fórmula $f = \lfloor (N-1)/2 \rfloor$ e, ao lado, cinco círculos representando nós, com dois deles sendo "apagados" para ilustrar a tolerância a falhas]*

O Raft organiza tudo em torno de uma máquina de estados replicada: todo nó mantém uma cópia idêntica de uma máquina de estados e aplica exatamente a mesma sequência de operações, na mesma ordem. Se todo mundo parte do mesmo estado e aplica as mesmas operações na mesma ordem, todo mundo termina no mesmo lugar. O problema de manter réplicas consistentes vira, então, o problema de garantir que todos concordem sobre a mesma sequência ordenada de operações — um log replicado.

Para isso funcionar, o Raft elege um único líder por vez. Se o líder some, os seguidores — cada um com um temporizador de eleição com um valor aleatório, e não fixo — viram candidatos e pedem votos. Quem recebe voto da maioria vira o novo líder. O motivo do temporizador ser aleatório, e não igual para todos, é evitar que todos os seguidores comecem uma eleição exatamente no mesmo instante e fiquem empatando indefinidamente.

O tempo, no Raft, é dividido em termos numerados. Cada termo tem, no máximo, um líder. Toda mensagem carrega o número do termo, o que permite qualquer nó identificar e descartar ordens vindas de um líder de um termo já ultrapassado.

Antes de simular, vale comparar rapidamente diferentes tamanhos de cluster, porque essa é uma decisão real de projeto. Um cluster de três nós tolera só uma falha, mas coordena mais rápido, porque só precisa de dois nós para maioria. Um cluster de sete nós tolera até três falhas, mas cada operação precisa ser confirmada por quatro nós, o que tende a aumentar um pouco a latência de escrita. E um cluster de seis nós — um número par — não ganha tolerância a falha nenhuma em relação a um de cinco: você paga o custo de coordenar mais um nó sem ganhar mais resiliência. Por isso, na prática, você quase nunca vê clusters de consenso com número par de nós.

*[indicação de edição: inserir tabela comparativa simples com clusters de três, cinco e sete nós, mostrando a tolerância a falhas de cada um]*

### Demonstração, exemplo e estudo de caso

Vamos simular. Imagine nosso cluster de cinco nós, todos no termo 1, com o nó A como líder. O nó A recebe uma operação — digamos, "reservar uma unidade do produto X" — e a replica para os outros quatro nós por meio de mensagens de *append entries*. Assim que a maioria — três nós, incluindo o próprio líder — confirma ter recebido essa entrada, ela é considerada confirmada, aplicada à máquina de estados, e só então o resultado volta para quem pediu a reserva.

*[indicação de edição: inserir diagrama de sequência animado com o nó A enviando *append entries* para B, C, D e E, e uma marca de "confirmado" aparecendo assim que três respostas chegam]*

Agora, o nó A falha — exatamente como aconteceu com o líder da região sul da NexaOrder. Os nós B, C, D e E percebem que pararam de receber sinais do líder. Cada um tem um temporizador levemente diferente; suponha que o nó C atinja o limite primeiro, se torna candidato, avança para o termo 2, e pede votos aos demais. Se B, D e E votarem em C, temos maioria — quatro em cinco, incluindo o próprio C — e C se torna o novo líder do termo 2. Note que isso acontece de forma automática, sem dois operadores de plantão tomando decisões conflitantes ao mesmo tempo. É exatamente o que teria evitado o incidente de *split-brain* da nossa situação-problema.

*[indicação de edição: inserir animação mostrando o nó A "apagado", o nó C avançando para o termo 2 e recebendo votos de B, D e E, com contagem visual de votos até atingir maioria]*

E se o nó A voltar a funcionar depois disso? Ele ainda está no termo 1, achando que é líder. Assim que ele tenta se comunicar com qualquer outro nó, recebe de volta a informação de que já existe um termo 2 em andamento, reconhece que não é mais líder, e passa a seguir C, reconciliando seu log com o log atual do cluster.

Isso nos leva a duas garantias importantes que o Raft oferece. A primeira é segurança: em qualquer termo, existe no máximo um líder, e uma entrada confirmada nunca desaparece nem é substituída. A segunda é disponibilidade: enquanto a maioria dos nós conseguir se comunicar, o cluster elege um líder e continua funcionando. Só que essas duas garantias não são simétricas — a segurança vale sempre, mesmo sob partição de rede; a disponibilidade só vale para o lado que tiver maioria. Se uma partição dividir nosso cluster de cinco em um grupo de dois e outro de três, só o grupo de três consegue eleger líder e continuar aceitando escritas.

Vamos colocar um número na demora dessa eleição. Se o tempo de ida e volta entre os nós é de, digamos, 5 milissegundos, e o temporizador de eleição está configurado para expirar entre 150 e 300 milissegundos — um intervalo típico usado na prática, justamente para deixar espaço suficiente para múltiplas rodadas de mensagens sem gerar eleições desnecessárias —, então, na pior hipótese, o cluster fica sem líder, e portanto sem aceitar novas escritas, por até 300 milissegundos mais o tempo de uma rodada de votação. Não é uma eternidade, mas também não é zero — e é exatamente por isso que sistemas críticos monitoram esse tempo de recuperação como uma métrica operacional, e não apenas como um detalhe teórico do algoritmo.

### Aplicação profissional

O Raft aparece, hoje, embutido em bancos de dados distribuídos, sistemas de coordenação de cluster e ferramentas de orquestração amplamente usadas na indústria — geralmente escondido atrás de um nome de configuração como "número de nós do cluster de controle" ou "quórum mínimo". Um profissional que entende consenso sabe, por exemplo, por que se recomenda número ímpar de nós nesses componentes, por que uma manutenção que retira dois nós de um cluster de cinco pode ser arriscada, e por que uma escrita pode demorar alguns segundos a mais logo após a queda do líder — é exatamente o tempo da eleição de um novo líder.

*[indicação de edição: inserir tela com a frase em destaque: "Consenso não evita falhas — evita que falhas virem decisões conflitantes"]*

Isso também muda a forma como você planeja uma manutenção programada. Se você sabe que o seu cluster de consenso tem cinco nós e tolera até duas falhas, retirar um único nó para atualização é seguro — o cluster continua com maioria de quatro entre os quatro restantes. Mas retirar dois nós ao mesmo tempo, achando que "ainda sobram três, que é maioria de cinco", é um erro sutil: se um terceiro nó falhar de forma inesperada durante essa janela de manutenção, o cluster perde a maioria e para de aceitar escritas. Planejar manutenções considerando a margem de segurança real do cluster, e não apenas o número mínimo teórico de maioria, é exatamente o tipo de raciocínio que separa uma operação tranquila de um incidente evitável.

### Fechamento

Hoje vimos como o Raft resolve, de forma automática, o problema que causou o incidente de *split-brain* da NexaOrder: eleição de líder por maioria, termos numerados, log replicado e confirmação por quórum. Vimos também que essa segurança tem um custo — de latência, de throughput, e de assumir que os nós falham por parar, não por mentir.

Fica também uma lição que conecta essa aula com a anterior: o Raft, na prática, é uma aplicação direta do teorema CAP que estudamos sobre particionamento de dados. Diante de uma partição de rede, o Raft escolhe consistência, não disponibilidade — o lado minoritário do cluster simplesmente para de aceitar escritas, em vez de arriscar dois líderes divergentes. Entender essa escolha explícita é o que permite a um profissional explicar, com segurança, por que um sistema baseado em consenso às vezes "trava" brevemente durante uma instabilidade de rede — e por que isso é, na verdade, o comportamento correto e desejado. Na próxima aula, vamos fechar a unidade tratando de um problema que atravessa vários serviços ao mesmo tempo: como manter uma compra coerente entre pedidos, estoque, pagamento e expedição, sem uma transação global. Até lá!

*[indicação de edição: encerrar com vinheta padrão e chamada para a Aula 8]*

### Indicações de edição e recursos visuais

- Tela de título animada (0:00–0:10).
- Fórmula de tolerância a falhas com ilustração de cinco nós (aproximadamente 3:00).
- Diagrama de sequência do ciclo normal de replicação do Raft (aproximadamente 7:00).
- Animação de falha do líder e eleição do novo líder com contagem de votos (aproximadamente 11:30).
- Tela de destaque com a frase sobre consenso e decisões conflitantes (aproximadamente 17:00).
- Vinheta de encerramento com chamada para a próxima aula.

### Fontes e links de mídia

- ONGARO, Diego; OUSTERHOUT, John. In search of an understandable consensus algorithm. In: USENIX ANNUAL TECHNICAL CONFERENCE, 2014, Philadelphia. *Proceedings [...]*. Berkeley: USENIX Association, 2014. Disponível em: https://raft.github.io/ — referência conceitual para a simulação apresentada no roteiro.
- Nenhuma mídia de terceiros com direitos autorais foi utilizada; diagramas e animações devem ser produzidos originalmente pela equipe de edição a partir das indicações acima.

---

## Videoaula 8 — “Sem transação global: como uma compra sobrevive a quatro falhas possíveis”

**Vínculo com o plano de aprendizagem:** Aula 8 — Transações distribuídas, sagas e idempotência.

**Objetivo da videoaula:** demonstrar, com o fluxo completo de compra da NexaOrder, como sagas com ações compensatórias e chaves de idempotência substituem uma transação distribuída global, evitando duplicações como a do estudo de caso.

### Abertura contextualizada

Chegamos à última aula da nossa Unidade 2! E ela fecha com o problema que, de certa forma, resume tudo o que vimos até aqui: uma compra na NexaOrder passa por quatro serviços diferentes — pedidos, estoque, pagamento e expedição —, cada um com seu próprio banco de dados. Não existe mais uma única transação capaz de garantir que os quatro passos aconteçam todos, ou nenhum.

*[indicação de edição: inserir tela cheia com o texto "Sem transação global: como uma compra sobrevive a quatro falhas possíveis"]*

Em um teste de carga recente, a equipe da NexaOrder viu isso na prática: o pagamento foi autorizado, mas uma falha de rede impediu a confirmação de chegar a tempo ao serviço de pedidos. O cliente, vendo a tela travada, tentou de novo — e dois pagamentos foram processados para a mesma compra. Hoje vamos entender por que isso aconteceu, e como projetar o fluxo para que isso não aconteça mais.

Esse é, talvez, o incidente mais caro entre todos os que vimos na Unidade 2 — não porque seja tecnicamente mais complexo, mas porque tem impacto financeiro direto e imediato sobre o cliente. E é também um ótimo exemplo de como boa parte da engenharia de sistemas distribuídos não é sobre impedir falhas — é sobre garantir que, quando a falha acontecer, e ela vai acontecer, o sistema se comporte de um jeito previsível e recuperável.

### Desenvolvimento conceitual

Dentro de um único banco de dados, atomicidade é fácil: o próprio banco garante que uma transação aplica tudo ou nada. Você não precisa se preocupar com o que acontece se o processo morrer no meio — o próprio motor do banco de dados cuida disso. O problema começa quando a operação de negócio atravessa vários bancos independentes. Existe uma solução clássica para isso, chamada confirmação em duas fases, ou 2PC: um coordenador pergunta a cada participante se está pronto para confirmar; se todos disserem sim, o coordenador manda confirmar; se qualquer um disser não, ou não responder a tempo, o coordenador manda desfazer tudo.

O problema do 2PC é que, durante essa espera, cada participante mantém recursos bloqueados. E se o coordenador falhar bem no meio, entre perguntar e decidir, os participantes ficam travados, sem saber se devem confirmar ou desfazer sozinhos. Para uma operação rápida, dentro de um único domínio de infraestrutura, isso pode ser aceitável. Para uma compra que envolve quatro serviços de equipes diferentes, com latências variáveis, um coordenador bloqueante desse tipo se torna, ele mesmo, um novo ponto frágil do sistema.

*[indicação de edição: inserir diagrama do 2PC com coordenador e três participantes, mostrando a fase de preparação e a fase de confirmação, com um ícone de "bloqueado" aparecendo sobre os participantes durante a espera]*

E o risco cresce mais rápido do que parece à primeira vista. Se cada um dos quatro serviços da NexaOrder tem, isoladamente, apenas 1% de chance de estar lento ou fora do ar num dado momento, a chance de que pelo menos um deles atrapalhe uma transação 2PC que dependa dos quatro simultaneamente já sobe para quase 4%. Quanto mais participantes um coordenador precisa reunir, maior a chance de a transação inteira ficar refém do elo mais fraco.

A alternativa amplamente adotada na indústria é a saga. Em vez de uma transação distribuída única, você tem uma sequência de transações locais, cada uma dentro de um serviço, encadeadas por eventos ou comandos. Se uma etapa falha, você não tenta desfazer tudo instantaneamente — você executa ações compensatórias, que revertem, de forma lógica, o que já tinha sido feito.

Existem duas formas de organizar isso. Na saga coreografada, cada serviço publica um evento ao terminar sua parte, e os outros reagem de forma independente, sem um centro. É simples para poucos passos, mas o fluxo completo fica implícito, espalhado entre vários serviços. Na saga orquestrada, um componente central conhece a sequência inteira e manda comandos explícitos, esperando confirmação antes de avançar. O fluxo fica visível e fácil de rastrear, mas esse orquestrador concentra o conhecimento do processo — ainda que, diferente do 2PC, ele não bloqueie recursos enquanto espera.

Como escolher entre as duas? Uma boa regra prática é pensar no número de passos e na complexidade de recuperação. Para um fluxo de dois ou três passos, com poucas variações possíveis, a coreografia costuma ser suficientemente simples e evita a criação de um componente central novo. Já para um fluxo como o da NexaOrder, com quatro passos, múltiplas compensações possíveis dependendo de onde a falha ocorre, e a necessidade de acompanhar, a qualquer momento, "em que ponto está esta compra específica", a orquestração tende a valer o custo de manter um componente central — porque esse componente é também o lugar onde você consegue observar e depurar o estado de cada saga em andamento.

### Demonstração, exemplo e estudo de caso

Vamos desenhar a saga da compra da NexaOrder, no modelo orquestrado. Primeiro passo: reservar estoque. Segundo: autorizar pagamento. Terceiro: confirmar o pedido. Quarto: solicitar expedição.

*[indicação de edição: inserir diagrama de fluxo com as quatro etapas em sequência, numeradas, e um orquestrador central acima delas]*

Agora, o que acontece se o pagamento falhar, no passo dois? A compensação é simples: liberar a reserva de estoque feita no passo um. E se a expedição falhar, no passo quatro, depois que o pagamento já foi autorizado? Aí a compensação é dupla: estornar o pagamento e liberar a reserva de estoque. Repare que a compensação nem sempre é o inverso perfeito da operação original — estornar um pagamento já processado pode envolver prazos e taxas diferentes de simplesmente "não ter cobrado". Isso é, tanto quanto uma decisão técnica, uma decisão de negócio.

*[indicação de edição: inserir o mesmo diagrama de fluxo, agora com setas vermelhas de compensação voltando do passo dois para o passo um, e do passo quatro para os passos dois e um]*

Mas isso ainda não resolve o incidente da situação-problema — o pagamento duplicado. Para isso, precisamos de dois mecanismos adicionais. O primeiro é o padrão *outbox*: em vez de gravar a alteração no banco e, separadamente, publicar um evento — o que cria o risco de fazer uma coisa e não a outra, se o serviço cair no meio —, você grava o evento a publicar na mesma transação local que grava a alteração de negócio, numa tabela auxiliar. Um processo separado lê essa tabela e publica os eventos de forma confiável.

O segundo mecanismo é a chave de idempotência. A cada tentativa de compra, geramos um identificador único. Antes de autorizar um pagamento, o serviço verifica: essa chave já foi processada antes? Se já foi, ele simplesmente devolve o resultado anterior, sem cobrar de novo. Se não foi, processa normalmente e registra a chave. No nosso incidente, se essa verificação existisse, a segunda tentativa do cliente teria sido reconhecida como repetição da primeira — e não como uma nova compra.

*[indicação de edição: inserir fluxograma de decisão: requisição de pagamento chega com uma chave; se a chave já existe na tabela de operações concluídas, retorna o resultado anterior; senão, processa e registra]*

Vale a pena reforçar de onde vem essa necessidade de deduplicação: sistemas de mensageria distribuída, quase sem exceção, preferem entregar uma mensagem duas vezes a arriscar não entregar nenhuma — essa garantia se chama entrega "pelo menos uma vez". Isso não é um defeito do sistema de mensageria; é uma escolha de projeto deliberada, porque perder uma mensagem silenciosamente costuma ser pior do que reprocessá-la. O trabalho do engenheiro, então, não é tentar convencer a rede a parar de duplicar mensagens — isso é praticamente impossível de garantir de ponta a ponta —, é desenhar cada operação para que processá-la duas vezes produza exatamente o mesmo resultado que processá-la uma vez. É essa propriedade, a idempotência, que transforma "a rede vai duplicar mensagens de vez em quando" de um problema em um detalhe operacional já previsto.

### Aplicação profissional

Sagas, *outbox* e chaves de idempotência aparecem, na prática, em praticamente qualquer sistema de e-commerce, de pagamentos ou de logística que você for construir ou manter profissionalmente. E o motivo é simples: sistemas de mensageria distribuída, por padrão, preferem entregar uma mensagem duas vezes a arriscar perder ela de vez — chamamos isso de entrega "pelo menos uma vez". Duplicatas não são exceção, são esperadas. Um sistema profissional não tenta impedir a rede de duplicar mensagens — ele torna o processamento dessas mensagens idempotente, de modo que processar duas vezes produza exatamente o mesmo resultado que processar uma vez.

*[indicação de edição: inserir tela com a frase em destaque: "A rede vai duplicar mensagens. A pergunta é: seu sistema aguenta isso?"]*

Antes de fechar, vale contrastar diretamente com o 2PC do início da aula: se a NexaOrder tivesse tentado resolver essa mesma compra com confirmação em duas fases, um coordenador teria mantido reserva de estoque, autorização de pagamento e emissão de etiqueta de expedição todos bloqueados, esperando a decisão final — por segundos ou minutos, dependendo da latência de cada serviço. Com a saga orquestrada, cada etapa confirma e libera seus recursos assim que termina, e apenas a lógica de compensação precisa ser acionada em caso de falha posterior. É uma troca deliberada: um pouco mais de complexidade de projeto, em troca de nenhum bloqueio global.

Um último ponto vale a pena levar para a prática profissional: sagas, compensações, *outbox* e idempotência não são quatro técnicas independentes que você escolhe usar isoladamente. Elas formam um conjunto coerente. Uma saga sem *outbox* corre o risco de perder eventos. Um consumidor sem *inbox* ou sem chave de idempotência corre o risco de processar o mesmo evento duas vezes. E uma compensação mal desenhada pode, ela mesma, criar um novo estado inconsistente. Projetar esse fluxo completo, com as quatro peças encaixadas, é o que efetivamente resolve o problema com o qual abrimos esta aula.

*[indicação de edição: inserir diagrama final consolidando as quatro peças — saga, compensação, outbox e idempotência — como camadas complementares de um mesmo fluxo de compra]*

### Fechamento

Fechamos aqui a Unidade 2. Vimos como replicar dados com o modelo de consistência certo, como particionar dados para crescer além da capacidade de um único nó, como o CAP e o PACELC descrevem os compromissos envolvidos, como o Raft resolve consenso de forma automática e segura, e, hoje, como sagas, ações compensatórias, o padrão *outbox* e chaves de idempotência substituem uma transação global impossível de sustentar em produção.

Se você olhar para trás, vai perceber que as quatro aulas desta unidade formam uma progressão: primeiro aprendemos a manter cópias de um mesmo dado coerentes entre si; depois, a dividir um volume de dados grande demais para um único nó; em seguida, a fazer um conjunto de nós concordarem automaticamente sobre decisões críticas, como quem é o líder; e, por fim, a manter operações de negócio coerentes quando elas atravessam vários serviços independentes. Essas quatro capacidades, juntas, são exatamente o que sustenta a camada de dados de qualquer sistema distribuído maduro. Na Unidade 3, vamos usar exatamente essa base para decompor a NexaOrder em serviços com limites de domínio bem definidos e construir uma arquitetura orientada a eventos de verdade. Até lá!

*[indicação de edição: encerrar com vinheta padrão de fechamento de unidade e chamada para a Unidade 3]*

### Indicações de edição e recursos visuais

- Tela de título animada (0:00–0:10).
- Diagrama do 2PC com fases de preparação e confirmação (aproximadamente 3:00).
- Diagrama de fluxo da saga orquestrada da NexaOrder, com e sem compensações (aproximadamente 8:00 e 10:30).
- Fluxograma de decisão de chave de idempotência (aproximadamente 13:30).
- Tela de destaque com a frase sobre mensagens duplicadas (aproximadamente 17:30).
- Vinheta de encerramento de unidade com chamada para a Unidade 3.

### Fontes e links de mídia

- RICHARDSON, Chris. *Microservices Patterns*. Shelter Island: Manning, 2018. Capítulos sobre sagas e consistência de dados — referência conceitual para o roteiro.
- Nenhuma mídia de terceiros com direitos autorais foi utilizada; diagramas devem ser produzidos originalmente pela equipe de edição a partir das indicações acima.
