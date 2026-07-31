# Roteiros das videoaulas 1 a 4 — Unidade 1

Disciplina: Distributed Systems Engineering
Professor-conteudista: Afonso Cesar Lelis Brandão
Duração-base de cada videoaula: 20 minutos (aproximadamente 2.200 a 2.700 palavras faladas).

Os quatro roteiros a seguir correspondem às Aulas 1 a 4 da Unidade 1, seguindo a NexaOrder como fio condutor prático. Cada roteiro é um texto de narração pronto para gravação, não notas de aula: leia-o como se estivesse falando diretamente com o estudante. As marcações de edição aparecem em itálico entre colchetes.

## Roteiro da Videoaula 1 — "Seu sistema cresceu; por que ele ficou menos previsível?"

**Vínculo com o plano de aprendizagem:** Unidade 1, Aula 1 — Pensar distribuído: conceitos, propriedades e compromissos.

**Objetivo da videoaula:** ao final, o estudante deve ser capaz de reconhecer o que caracteriza um sistema distribuído, relacionar a decisão de distribuir a requisitos concretos e identificar, na NexaOrder, os problemas criados pela distribuição de uma aplicação antes centralizada.

### Abertura contextualizada

Oi! Seja bem-vindo à primeira aula da disciplina de Engenharia de Sistemas Distribuídos. Antes de falar de conceito, quero te contar uma história — a história da NexaOrder, uma plataforma fictícia de pedidos, pagamentos e expedição que vai te acompanhar durante toda esta disciplina.

*[indicação de edição: inserir, em tela cheia, o logotipo fictício "NexaOrder" com a assinatura "plataforma de pedidos, pagamentos e expedição"]*

A NexaOrder começou pequena: uma única aplicação, rodando em um único servidor, com a interface, as regras de negócio e o banco de dados vivendo lado a lado. Funcionava bem. Até que as vendas cresceram. A equipe fez o que parecia óbvio: separou o sistema em pedaços — catálogo, estoque, pagamento, expedição — e colocou cada pedaço para rodar em várias instâncias, em várias máquinas.

O resultado? A capacidade de atendimento aumentou. Mas apareceram comportamentos que ninguém tinha visto antes. Dois clientes conseguiram comprar o último item do estoque, ao mesmo tempo. Um cliente foi cobrado mesmo depois de a tela mostrar erro. E o painel de operações mostrou, para o mesmo pedido, dois estados diferentes ao mesmo tempo.

Se você já trabalhou com sistemas em produção, talvez esses sintomas soem familiares. E a primeira coisa que eu quero que você entenda, hoje, é isto: esses incidentes não aconteceram porque alguém programou errado. Eles aconteceram porque a equipe trocou chamadas locais, previsíveis, por comunicação em rede — e essa troca muda as regras do jogo.

### Desenvolvimento conceitual

Vamos com calma. O que é, afinal, um sistema distribuído?

Um sistema distribuído é um conjunto de componentes autônomos — pode ser processos, máquinas virtuais, contêineres — que se comunicam por rede e coordenam suas ações para entregar um serviço. Repare em quatro palavras-chave aqui, porque elas vão te acompanhar a disciplina inteira: pluralidade, autonomia, comunicação e coordenação.

*[indicação de edição: inserir Recurso visual 1 da Aula 1 — diagrama da NexaOrder com cliente, gateway, pedidos, estoque, pagamento e expedição]*

Pluralidade significa que há mais de um participante. Autonomia significa que cada participante pode falhar de forma independente dos outros — o estoque pode cair sem que o pagamento caia junto. Comunicação significa que a cooperação passa por mensagens, não por memória compartilhada instantânea. E coordenação significa que o resultado final depende de como essas mensagens se combinam.

Agora, uma pergunta importante: por que distribuir um sistema, afinal? Distribuir não é um objetivo em si — é uma resposta a um requisito. E os requisitos mais comuns são: escalabilidade, disponibilidade, proximidade geográfica e autonomia organizacional.

Escalabilidade é a capacidade de aguentar mais carga sem quebrar. Você pode escalar verticalmente — colocando mais CPU e memória em uma única máquina — ou horizontalmente — adicionando mais instâncias. A escala vertical é operacionalmente mais simples, mas tem limite físico e limite de custo. A escala horizontal multiplica a capacidade, mas exige que você resolva balanceamento, concorrência e coordenação entre as instâncias.

Deixa eu te mostrar uma conta rápida, porque ela ilustra bem esse raciocínio.

*[indicação de edição: inserir na tela a fórmula do número estimado de instâncias, com destaque para cada variável]*

Se a NexaOrder precisa atender 800 requisições por segundo no pico, e cada instância aguenta 200 requisições por segundo, com uma meta de operar a 70% da capacidade, a conta é: 800 dividido por 200 vezes 0,7 — isso dá 5,71, e a gente arredonda para cima, porque não existe meia instância. O resultado é 6 instâncias, no mínimo. Note que a margem de segurança — os 70% — evita que o sistema opere sempre no limite, o que é perigoso: qualquer pico inesperado já derruba tudo.

Mas escalabilidade sozinha não resolve tudo. Tem disponibilidade: várias instâncias só protegem contra falha se elas não compartilharem o mesmo ponto de falha. Duas instâncias no mesmo servidor físico não te protegem de nada se esse servidor cair. E tem um detalhe interessante: cada "nove" a mais de disponibilidade custa exponencialmente mais caro. 99,9% de disponibilidade permite cerca de 43 minutos de indisponibilidade por mês. 99,99% reduz isso para pouco mais de 4 minutos. É uma diferença enorme de engenharia.

Agora, o ponto mais importante desta aula: quando você distribui um sistema, três propriedades mudam o seu jeito de raciocinar, e eu quero que você grave isso.

Primeiro, concorrência: componentes diferentes trabalham ao mesmo tempo, e isso cria disputa por recursos compartilhados — como dois clientes tentando comprar o último item do estoque simultaneamente.

Segundo, ausência de estado global instantâneo: como a comunicação leva tempo, dois componentes podem ter visões diferentes da realidade, e as duas podem estar "certas" do ponto de vista de cada um.

Terceiro — e esse é talvez o mais sutil — falha parcial. Em um programa local, se algo quebra, você sabe. Em um sistema distribuído, um componente pode estar funcionando perfeitamente enquanto outro está fora do ar, e quem está esperando uma resposta não consegue, só pelo silêncio, saber qual das duas coisas está acontecendo.

Tem mais duas coisas que eu preciso te contar antes de seguir. A primeira é heterogeneidade: sistemas distribuídos normalmente combinam linguagens de programação, bancos de dados, protocolos e até versões diferentes de um mesmo serviço. Isso significa que contratos de interface e formatos de dados deixam de ser detalhe de implementação e passam a ser parte do próprio sistema — uma mudança que parece local, dentro de um serviço, pode quebrar quem consome esse serviço sem nem imaginar que ele existe.

A segunda é a transparência. Um objetivo comum em sistemas distribuídos é esconder do usuário que existe distribuição — ele não precisa saber qual servidor atendeu a requisição dele, nem se os dados vieram de uma réplica ou de outra. Isso é ótimo para quem usa o sistema. Mas é perigoso para quem projeta, porque uma chamada remota não é uma chamada local disfarçada: ela tem latência maior e variável, pode falhar sem que o destino tenha falhado, pode produzir efeito sem confirmar, depende de serialização, atravessa limites de segurança, pode ser repetida e exige compatibilidade de contrato. Esconder isso do usuário é desejável. Esconder isso de você, que projeta o sistema, é um erro que vai custar caro mais adiante.

*[indicação de edição: inserir lista dos sete pontos de diferença entre chamada remota e chamada local, aparecendo item a item]*

Agora, três métricas que eu quero que você nunca confunda, porque elas medem coisas diferentes. Latência é o tempo para concluir uma operação — e aqui, esquece a média, porque ela esconde os casos ruins; olhe para percentis. Um p95 de 300 milissegundos significa que 95% das respostas vieram em até 300 milissegundos, e 5% demoraram mais que isso. Throughput é a quantidade de trabalho concluída por unidade de tempo — pedidos por segundo, por exemplo, e aumentar concorrência eleva throughput só até certo ponto, depois filas crescem e a latência dispara. E disponibilidade não é apenas "o servidor respondeu" — é "o servidor respondeu com o resultado certo, de um jeito que serve para o negócio". Um endpoint pode responder rapidinho e ainda estar funcionalmente indisponível, se ele devolve erro para quase toda compra.

E, por fim, quatro estilos de arquitetura que você vai ouvir a disciplina inteira: cliente-servidor, o mais simples, onde clientes pedem e servidores atendem; arquitetura em camadas, que separa apresentação, aplicação e dados, sem exigir necessariamente distribuição física; peer-to-peer, em que cada participante pode ser cliente e servidor ao mesmo tempo; e arquitetura de serviços, em que capacidades de negócio são expostas por contratos, com o risco de virar um "monólito distribuído" se os serviços não tiverem autonomia real.

*[indicação de edição: inserir Recurso visual 4 da Aula 1 — quadro comparativo dos quatro estilos arquiteturais]*

*[indicação de edição: inserir Recurso visual 2 da Aula 1 — linha do tempo de uma falha ambígua, mostrando cobrança processada e resposta perdida]*

### Demonstração, exemplo ou estudo de caso

Vamos aplicar isso na prática, com o próprio incidente da NexaOrder. Um cliente clica em "finalizar compra". O pedido de autorização de pagamento é enviado ao provedor. A resposta demora. O serviço de pedidos espera, espera, e estoura o tempo limite. A tela mostra "erro ao processar pagamento".

Só que, nos bastidores, o pagamento foi processado com sucesso — a resposta é que se perdeu no caminho de volta. Se o cliente tentar de novo, sem nenhuma proteção, ele pode ser cobrado duas vezes. Se o sistema simplesmente desistir, uma compra válida é perdida.

Note que essa ambiguidade — "a operação não chegou? Chegou e ainda está processando? Foi processada e a resposta se perdeu?" — é impossível de resolver só olhando o timeout. Ela exige desenho: identificação de operações, consulta de estado, idempotência. A gente vai aprofundar exatamente isso na próxima aula, quando falarmos de comunicação entre processos.

*[indicação de edição: exibir, em tela dividida, o cliente vendo "erro" à esquerda e o log interno mostrando "pagamento aprovado" à direita, com uma seta de "resposta perdida" entre os dois lados]*

Agora, um exercício rápido para você fazer comigo. Pense em uma aplicação centralizada qualquer — pode ser um sistema de agendamento, um sistema de estoque de uma loja pequena. Pergunte: se eu separar esse sistema em três serviços independentes, quais dessas três propriedades — concorrência, ausência de estado global, falha parcial — passam a existir, que não existiam antes? Pausa o vídeo um instante e pensa nisso antes de eu continuar.

*[indicação de edição: inserir tela de pausa com contagem regressiva de 10 segundos e o texto "Pense e continue"]*

Voltou? Ótimo. Na maioria dos casos, as três aparecem juntas, porque elas são consequência direta da separação — não de uma escolha isolada de tecnologia.

### Aplicação profissional

Por que isso importa para a sua carreira? Porque toda decisão de arquitetura que você tomar — seja como desenvolvedor, arquiteto, engenheiro de dados, profissional de nuvem, DevOps, SRE ou segurança — vai, em algum momento, esbarrar nessas três propriedades.

Se você trabalha com desenvolvimento de APIs, vai precisar decidir o que fazer quando uma chamada não responde a tempo. Se você trabalha com dados, vai lidar com réplicas que mostram estados diferentes por alguns instantes. Se você trabalha com operações, vai precisar diferenciar um componente que caiu de um componente que só está lento.

E o critério para decidir se vale a pena distribuir não pode ser "porque todo mundo faz assim" ou "porque parece mais moderno". O critério precisa amarrar quatro coisas: qual requisito você está resolvendo, qual mecanismo você vai adotar, qual compromisso — ou seja, qual custo — esse mecanismo introduz, e como você vai medir se funcionou.

*[indicação de edição: inserir card com os quatro termos — requisito, decisão, compromisso, evidência — aparecendo um a um]*

Um sistema interno pequeno, usado por poucas pessoas, com tolerância alta a alguns minutos de indisponibilidade, pode muito bem continuar sendo um monólito modular. Distribuir sem necessidade só multiplica os pontos de falha que você acabou de aprender a reconhecer.

### Fechamento

Recapitulando: um sistema distribuído é definido por componentes autônomos que se comunicam por rede e coordenam ações. Distribuir resolve requisitos de escalabilidade, disponibilidade, proximidade e autonomia — mas introduz concorrência, ausência de estado global instantâneo e falha parcial, que mudam completamente o seu jeito de pensar o sistema.

Na próxima aula, a gente entra na comunicação entre processos: como a NexaOrder troca mensagens entre pedidos, estoque, pagamento e expedição, comparando chamadas síncronas, RPC e mensageria — e por que essa escolha influencia diretamente os incidentes que acabamos de discutir.

Até lá, faça a atividade prática do texto-base: elabore um registro de decisão arquitetural para a NexaOrder, amarrando requisito, decisão, compromisso e evidência. Nos vemos na próxima aula.

*[indicação de edição: encerrar com tela de créditos e o texto "Próxima aula: Comunicação entre processos — APIs, RPC e mensageria"]*

### Indicações de edição e recursos visuais

- Abertura: logotipo fictício da NexaOrder em tela cheia (3 segundos).
- Recurso visual 1 (reaproveitado da Aula 1 do texto-base): diagrama da NexaOrder com cliente, gateway e os quatro serviços.
- Fórmula do número de instâncias em destaque na tela durante o cálculo numérico, com cada variável surgindo em sincronia com a fala.
- Recurso visual 2 (reaproveitado da Aula 1 do texto-base): linha do tempo da falha ambígua de pagamento.
- Tela dividida cliente/log interno durante a demonstração do incidente de pagamento.
- Tela de pausa com contagem regressiva de 10 segundos durante o exercício rápido.
- Card com os quatro termos do registro de decisão arquitetural (requisito, decisão, compromisso, evidência).
- Encerramento com chamada para a próxima videoaula.

### Fontes e links de mídia

- Diagramas e fórmulas originais, produzidos internamente a partir do texto-base da Aula 1 (`unidade_1.md`), sem mídia externa incorporada.
- Referência conceitual de apoio: COULOURIS, George et al. *Distributed Systems: Concepts and Design*. 5. ed. Boston: Addison-Wesley, 2011 (não há trecho de vídeo ou áudio externo a licenciar nesta videoaula).

## Roteiro da Videoaula 2 — "Esperar ou seguir em frente? O dilema da comunicação distribuída"

**Vínculo com o plano de aprendizagem:** Unidade 1, Aula 2 — Comunicação entre processos: APIs, RPC e mensageria.

**Objetivo da videoaula:** ao final, o estudante deve ser capaz de comparar comunicação síncrona e assíncrona, reconhecer os papéis de APIs HTTP, RPC e mensageria, e aplicar *timeout*, *retry* com *backoff*/*jitter* e idempotência ao fluxo de criação de pedidos da NexaOrder.

### Abertura contextualizada

Bem-vindo de volta! Na aula passada, a gente viu que separar a NexaOrder em serviços trouxe concorrência, ausência de estado global e falha parcial. Hoje eu quero focar em uma pergunta bem prática: quando um serviço fala com outro, ele deveria esperar a resposta, ou deveria só avisar e seguir em frente?

*[indicação de edição: inserir tela dividida com dois ícones — um relógio de ampulheta representando "esperar" e uma seta representando "seguir em frente"]*

Lembra do incidente que fechei a aula passada? O cliente clicou em "finalizar compra", o pagamento demorou, o timeout estourou, e a cobrança foi processada mesmo assim. Isso aconteceu porque o fluxo da NexaOrder, hoje, é totalmente síncrono e encadeado: pedidos chama estoque, espera; estoque aprovado, chama pagamento, espera; pagamento aprovado, chama expedição, espera. Um encadeamento inteiro de esperas.

### Desenvolvimento conceitual

Vamos separar dois conceitos que costumam se confundir: comunicação síncrona e comunicação assíncrona.

Na comunicação síncrona, quem pede espera a resposta antes de continuar. É fácil de programar e de entender, mas tem um problema estrutural: se você encadeia várias chamadas síncronas, a latência total tende a somar a latência de cada uma. E pior: a disponibilidade do fluxo inteiro despenca, porque qualquer elo mais fraco da corrente derruba todo mundo.

Na comunicação assíncrona, quem pede não espera o resultado final. Ele registra a intenção — normalmente publicando uma mensagem — e segue em frente. O resultado chega depois, por outro caminho.

*[indicação de edição: inserir Recurso visual 1 da Aula 2 — fluxo HTTP síncrono encadeado do pedido]*

Agora, como essa comunicação acontece na prática? Dois estilos síncronos aparecem com frequência. O primeiro é a API HTTP orientada a recursos: cada entidade do domínio — um pedido, uma reserva de estoque, uma cobrança — vira um recurso identificado por uma URL, e você usa verbos HTTP para operar sobre ele. Um POST para /pedidos cria um pedido e devolve um identificador. Um GET para /pedidos/id consulta o estado dele, sem repetir a criação. Os códigos de status — a faixa 2xx pra sucesso, a 4xx pra erro do cliente, a 5xx pra erro do servidor — comunicam o resultado de forma padronizada, sem que cada equipe da NexaOrder precise inventar seu próprio vocabulário de erro.

Um detalhe que vale a pena grifar: cada requisição HTTP é, por padrão, autocontida. O servidor não depende de memória de requisições anteriores para interpretá-la. Isso parece um detalhe técnico pequeno, mas tem um efeito enorme na prática: qualquer instância do serviço de pedidos pode atender qualquer requisição, o que facilita demais o balanceamento entre múltiplas instâncias — lembra da conta de escalabilidade horizontal que fizemos na Aula 1? Pois é, ela só funciona bem se as requisições forem, de fato, independentes entre si.

O segundo estilo síncrono é o RPC — chamada remota de procedimento. Aqui a ideia é fazer a chamada remota parecer uma chamada de função comum: `estoque.reservarItem(pedido, item, quantidade)`. É conveniente, mas atenção: essa aparência de chamada local é enganosa. Uma chamada remota pode falhar de jeitos que uma chamada local nunca falha — a rede pode cair, a mensagem pode se perder, a resposta pode não voltar mesmo que a operação remota tenha sido concluída. Tratar RPC como se fosse uma função comum é repetir o erro que já vimos na aula passada.

*[indicação de edição: inserir texto na tela — "RPC parece local. Não é." — com destaque em vermelho]*

O que dá valor real ao RPC não é a aparência de chamada local — é o contrato explícito de interface por trás dela. Uma definição formal dos métodos disponíveis, dos tipos de parâmetro e retorno, e dos erros possíveis, normalmente escrita em uma linguagem de definição de interface. Esse contrato permite gerar automaticamente código de cliente e servidor compatível entre si, o que reduz um tipo de erro muito comum: um lado da comunicação implementado de um jeito, o outro lado esperando outro formato, e ninguém percebendo até a mensagem chegar deformada em produção.

Só que HTTP e RPC não resolvem tudo sozinhos. Tem um detalhe importante por trás de qualquer comunicação: a serialização e a evolução de esquema. Toda mensagem precisa virar bytes para viajar pela rede, e virar dado de novo do outro lado. O problema real não é o formato — é o que acontece quando um serviço muda o formato da mensagem e o outro lado ainda não foi atualizado. Se pedidos manda um novo campo, "canal de venda", o estoque — ainda na versão antiga — precisa continuar funcionando sem quebrar. Por isso, campo novo deve ser opcional, com valor padrão, e você não deve remover ou renomear campo que alguém já está usando.

Agora vamos para a comunicação assíncrona: filas e publicação-assinatura, também chamado de *pub-sub*. Numa fila, cada mensagem é entregue a um único consumidor entre os que competem por ela — bom para distribuir trabalho. No pub-sub, cada mensagem publicada em um tópico chega a todos os assinantes, de forma independente — bom para notificar múltiplos serviços sobre um mesmo acontecimento, sem que o produtor precise conhecer cada um deles.

*[indicação de edição: inserir Recurso visual 2 da Aula 2 — comparação fila versus publicação-assinatura]*

E aqui entra um conceito-chave: evento. Um evento é o registro de algo que já aconteceu — "PedidoCriado", "PagamentoAprovado". Isso é diferente de um comando, que pede uma ação futura, como "ReservarEstoque". Quando pedidos publica "PedidoCriado", ele não decide quem vai reagir. Estoque, pagamento, e até um futuro serviço de análise de fraude podem assinar esse mesmo evento, de forma independente — e, repara, se amanhã a NexaOrder quiser adicionar um serviço de recomendação que também reage à criação de um pedido, ela simplesmente assina o mesmo evento. Ninguém precisa mexer no serviço de pedidos pra isso. É esse desacoplamento que torna a arquitetura orientada a eventos tão atraente conforme o sistema cresce.

O preço dessa independência toda, repito, é que quem publica um evento não sabe, no mesmo instante, se e como os assinantes reagiram. Isso não é um detalhe menor — significa que você precisa pensar, desde o desenho, em como vai saber que uma reação aconteceu, ou que falhou, sem depender de uma resposta síncrona.

### Demonstração, exemplo ou estudo de caso

Vamos comparar, lado a lado, os dois fluxos possíveis de criação de pedido na NexaOrder.

No fluxo síncrono — o que existe hoje — pedidos chama estoque e espera; chama pagamento e espera; chama expedição e espera; só então devolve a resposta final ao cliente. O cliente recebe uma confirmação completa, de uma vez. Mas se o pagamento estiver lento, o cliente espera junto — e, como vimos, pode até abandonar ou repetir a compra.

*[indicação de edição: animação do fluxo síncrono, com barra de progresso mostrando a soma das latências de cada etapa]*

No fluxo orientado a eventos, pedidos só registra a intenção, publica "PedidoCriado", e devolve na hora um status de "processando". Estoque, pagamento e expedição assinam esse evento e reagem de forma independente, publicando seus próprios eventos de conclusão. Pedidos agrega essas notificações depois. O cliente recebe uma resposta rápida, mas não definitiva — ele vai acompanhar o progresso.

*[indicação de edição: animação do fluxo assíncrono, com o evento "PedidoCriado" se ramificando em três setas paralelas para estoque, pagamento e expedição]*

Repare que nenhum dos dois é "o certo". O síncrono é mais simples de acompanhar, mas mais frágil a lentidão de qualquer etapa. O assíncrono é mais resiliente, mas exige que você rastreie em que estágio o pedido está — e, atenção, exige que você trate eventos que podem chegar fora de ordem, um problema que a gente ataca de frente na próxima aula.

Agora, e se uma chamada falhar? Você tenta de novo. Mas tentar de novo sem cuidado é perigoso — se todos os clientes tentarem de novo ao mesmo tempo, depois de uma falha, você cria uma avalanche de tentativas exatamente sobre um serviço que já está sobrecarregado. É o efeito manada, ou *thundering herd*.

A solução combina duas técnicas. Backoff exponencial: cada nova tentativa espera mais tempo que a anterior. E jitter: você soma um valor aleatório a essa espera, pra evitar que todo mundo tente de novo no mesmo milissegundo.

*[indicação de edição: inserir na tela a fórmula do backoff com jitter, com cada termo destacado]*

Vamos ao número. Com um intervalo base de 200 milissegundos e um teto de 5 segundos, veja como cresce, sem contar ainda o jitter: primeira tentativa, 200 milissegundos; segunda, 400; terceira, 800; quarta, 1600; quinta, 3200. Cada tentativa dobra a espera da anterior. O teto existe justamente para não deixar essa espera crescer sem limite. E o jitter, por cima disso, espalha essas tentativas no tempo, mesmo quando muitos clientes falharam ao mesmo tempo.

Mas isso ainda não resolve tudo. Se a operação já tiver produzido efeito — o pedido já foi criado — e você tentar de novo sem proteção, você cria um pedido duplicado. É aqui que entra a idempotência: uma chave gerada pelo cliente, enviada em toda tentativa da mesma operação, que o servidor usa para reconhecer "essa operação eu já processei" e devolver o resultado anterior, em vez de repetir o efeito.

*[indicação de edição: inserir Recurso visual 3 da Aula 2 — dois fluxos de criação de pedido lado a lado]*

### Aplicação profissional

No seu dia a dia profissional, essa decisão entre síncrono e assíncrono vai aparecer toda vez que você desenhar uma integração entre serviços. E a pergunta certa não é "qual é mais moderno", é: o chamador precisa de uma resposta imediata para decidir o próximo passo? Se sim, síncrono tende a fazer mais sentido. Se o resultado pode ser processado depois, sem bloquear ninguém, assíncrono reduz o acoplamento e melhora a resiliência.

E, seja qual for a escolha, três proteções são praticamente obrigatórias em qualquer chamada de rede que importa: um timeout bem calibrado, uma política de retry com backoff e jitter, e idempotência sempre que a operação tiver efeito colateral, como criar ou cobrar algo.

Tem um último elemento que eu quero deixar plantado na sua cabeça, mesmo que a gente só vá aprofundar isso na Unidade 4: todo contrato de comunicação que você desenhar deveria prever, desde já, um identificador de correlação — um valor que acompanha uma operação lógica através de todas as chamadas, mensagens e retentativas que ela gerar, mesmo quando atravessa vários serviços. Sem isso, quando um incidente acontecer — e vai acontecer —, reconstruir o que aconteceu com um pedido específico da NexaOrder vira um trabalho de detetive, catando log por log, serviço por serviço, torcendo para os horários baterem. Com um identificador de correlação bem definido desde o desenho da API, esse trabalho vira uma simples busca.

*[indicação de edição: inserir tela com um identificador de correlação hipotético — por exemplo, um código alfanumérico — sendo repassado entre os quatro serviços da NexaOrder em um diagrama de sequência]*

### Fechamento

Recapitulando: comunicação síncrona simplifica o raciocínio, mas soma latência e propaga indisponibilidade. Comunicação assíncrona reduz esse acoplamento, ao custo de mais complexidade de rastreamento. HTTP e RPC são dois estilos síncronos com contratos diferentes; filas e pub-sub são dois estilos assíncronos com propósitos diferentes. E toda chamada de rede precisa de timeout, retry com backoff e jitter, e idempotência.

Na próxima aula, vamos lidar com um problema que apareceu agora, de relance, quando falei de eventos fora de ordem: como saber qual evento aconteceu primeiro, se não existe um relógio único compartilhado entre os serviços da NexaOrder? Nos vemos lá.

*[indicação de edição: encerrar com tela de créditos e o texto "Próxima aula: Concorrência, relógios e ordenação de eventos"]*

### Indicações de edição e recursos visuais

- Abertura: tela dividida "esperar" versus "seguir em frente".
- Recurso visual 1 (Aula 2 do texto-base): fluxo HTTP síncrono encadeado.
- Texto de destaque "RPC parece local. Não é." em tela cheia.
- Recurso visual 2 (Aula 2 do texto-base): comparação fila versus publicação-assinatura.
- Duas animações comparativas: fluxo síncrono com barra de progresso somando latências; fluxo assíncrono com evento se ramificando em três setas paralelas.
- Fórmula do backoff exponencial com jitter, com destaque progressivo dos termos durante a fala.
- Recurso visual 3 (Aula 2 do texto-base): comparação dos dois fluxos de criação de pedido.
- Encerramento com chamada para a próxima videoaula.

### Fontes e links de mídia

- Diagramas, fórmulas e animações originais, produzidos a partir do texto-base da Aula 2 (`unidade_1.md`).
- Referência conceitual de apoio: BIRRELL, Andrew D.; NELSON, Bruce Jay. Implementing remote procedure calls. ACM Transactions on Computer Systems, v. 2, n. 1, p. 39-59, 1984. DOI: 10.1145/2080.357392 (não há trecho de vídeo ou áudio externo a licenciar nesta videoaula).

## Roteiro da Videoaula 3 — "Qual evento aconteceu primeiro? A pergunta que o relógio não responde sozinho"

**Vínculo com o plano de aprendizagem:** Unidade 1, Aula 3 — Concorrência, relógios e ordenação de eventos.

**Objetivo da videoaula:** ao final, o estudante deve ser capaz de explicar por que não existe relógio global em um sistema distribuído, aplicar a relação happened-before, construir relógios lógicos de Lamport e reconhecer quando dois eventos são concorrentes.

### Abertura contextualizada

Oi, de novo! Imagina a seguinte cena: dois eventos acontecem na NexaOrder quase ao mesmo tempo. Um servidor de estoque cancela uma reserva porque o cliente demorou demais. Outro servidor, o de pagamento, aprova a cobrança que já estava em andamento. O painel de operações da equipe ordena esses dois eventos pelo horário registrado em cada servidor, e conclui que o cancelamento veio primeiro.

*[indicação de edição: inserir tela com dois relógios de parede, um adiantado e outro atrasado, sobre os ícones do serviço de estoque e do serviço de pagamento]*

Só que tem um detalhe: o relógio do servidor de pagamento estava 360 milissegundos atrasado. E é sobre isso que a gente vai falar hoje: por que você não pode confiar cegamente no relógio de parede de cada máquina para decidir o que aconteceu primeiro em um sistema distribuído.

### Desenvolvimento conceitual

Primeiro, uma verdade desconfortável: não existe relógio global instantâneo compartilhado entre os componentes da NexaOrder. Cada serviço tem seu próprio relógio físico, e esses relógios divergem, porque o hardware de cada máquina tem um desvio próprio — um erro de contagem que se acumula com o tempo, mesmo com sincronização periódica.

Dá pra estimar esse desvio. A fórmula é: o desvio máximo é igual a duas vezes a taxa de desvio, vezes o tempo desde a última sincronização.

*[indicação de edição: inserir a fórmula do desvio máximo, com cada termo aparecendo conforme a fala]*

Vamos ao número: se cada relógio pode desviar até 50 partes por milhão, e passou uma hora — 3600 segundos — desde a última sincronização, o cálculo é: duas vezes 0,00005, vezes 3600. Isso dá 0,36 segundos. Ou seja, 360 milissegundos de desvio possível entre dois servidores. E foi exatamente isso que confundiu o painel de operações da NexaOrder: dois eventos separados por menos de 360 milissegundos podem aparecer em qualquer ordem, dependendo de qual relógio está adiantado e qual está atrasado.

Diante disso, Leslie Lamport propôs, em 1978, uma solução diferente: em vez de confiar no relógio físico, confiar em causalidade observável. Essa relação se chama happened-before, e ela tem três regras. Primeira: se dois eventos acontecem no mesmo processo, na ordem em que foram executados, o primeiro "aconteceu antes" do segundo — isso é só o processamento sequencial que qualquer programa já tem, dentro de um único processo. Segunda: se um evento é o envio de uma mensagem, e outro é o recebimento dessa mesma mensagem, o envio "aconteceu antes" do recebimento — o que parece óbvio, mas é justamente essa regra que costura a causalidade entre processos diferentes. Terceira: essa relação é transitiva — se A aconteceu antes de B, e B aconteceu antes de C, então A aconteceu antes de C, mesmo que A e C estejam em processos completamente diferentes, sem nenhuma mensagem direta entre eles.

E aqui vem o conceito mais importante da aula: dois eventos que não têm nenhuma cadeia de causalidade entre eles, nem direta, nem por transitividade, são chamados de concorrentes. Não é sobre estarem próximos no tempo. É sobre não existir um caminho causal entre eles.

*[indicação de edição: inserir Recurso visual 1 da Aula 3 — linha do tempo dos relógios lógicos com raias por processo]*

Para tornar essa ideia prática, Lamport criou um mecanismo simples: cada processo mantém um contador. Antes de cada evento local, incrementa o contador em um. Ao enviar uma mensagem, anexa o valor do contador. Ao receber, ajusta o contador para o maior valor entre o seu e o recebido, e soma mais um.

### Demonstração, exemplo ou estudo de caso

Vamos construir isso junto, passo a passo, com pedidos e estoque.

Pedidos cria um pedido — evento local. Contador de pedidos vai de zero para um. Pedidos envia a solicitação de reserva para estoque, anexando o valor um. Contador de pedidos sobe pra dois.

*[indicação de edição: exibir tabela ao vivo, preenchendo linha por linha conforme a narração]*

Estoque recebe a mensagem, que veio com o valor um. O contador de estoque, que estava em zero, vira o máximo entre zero e um, mais um — ou seja, dois. Estoque confirma a reserva e envia de volta pra pedidos, anexando o valor dois. Contador de estoque sobe pra três. Pedidos recebe a confirmação, que veio com o valor dois. O contador de pedidos, que estava em dois, vira o máximo entre dois e dois, mais um — ou seja, três.

Repare: o evento de recebimento da confirmação, em pedidos, ficou com contador três — maior que o contador dois do evento que o originou. Isso é esperado, porque causalidade sempre implica número crescente.

Só que — atenção pra essa pegadinha — se o serviço de pagamento, em paralelo, sem trocar nenhuma mensagem com pedidos ou estoque até esse ponto, registrar um evento local que também chega a contador três, esse empate não significa relação causal nenhuma. É só uma coincidência de contagem. O relógio de Lamport ordena números, mas não te diz, sozinho, quando dois eventos são realmente concorrentes.

*[indicação de edição: inserir Recurso visual 2 da Aula 3 — comparação de vetores concorrentes]*

Isso pode parecer um detalhe teórico, mas tem uma implicação prática direta: qualquer sistema que ordene eventos só pelo relógio de Lamport, sem mais nada, corre o risco de tratar dois eventos concorrentes como se um tivesse causado o outro, só porque um número ficou maior que o outro. E se você usar esse número para decidir, por exemplo, qual atualização de estoque "vale" no fim do dia, você pode estar tomando uma decisão de negócio baseada em uma coincidência de contagem, não em causalidade real.

Pra resolver isso, existe o relógio vetorial. Em vez de um número só, cada processo guarda um vetor com uma posição pra cada processo do sistema. Volta pro nosso incidente inicial: o cancelamento de reserva, no estoque, tem vetor dois, três, zero — nessa ordem, pedidos, estoque, pagamento. A aprovação de pagamento tem vetor dois, um, dois. Compara posição por posição: a primeira empata; a segunda é maior no cancelamento; a terceira é maior na aprovação. Nenhum vetor domina o outro em todas as posições — isso prova, com certeza, que os dois eventos são concorrentes. Nenhum causou o outro. E o sistema, sozinho, não tem como saber qual "deveria" prevalecer — isso é uma decisão de negócio, não uma dedução técnica.

Vale marcar também a diferença entre ordem parcial e ordem total, porque isso aparece direto em entrevista técnica e em discussão de arquitetura. A relação happened-before define uma ordem parcial: alguns pares de eventos são comparáveis, um precede o outro; outros pares, os concorrentes, simplesmente não são comparáveis por critério causal nenhum. Uma ordem total, em contraste, compara qualquer par de eventos — e você pode até impor uma ordem total artificialmente, por exemplo usando o identificador do processo como critério de desempate quando os contadores lógicos empatam. Mas presta atenção: impor uma ordem total sobre eventos concorrentes não devolve a causalidade que nunca existiu. É só uma escolha arbitrária, porém determinística, útil quando o sistema precisa de uma decisão única — mas não confunda essa escolha com "descobrir" o que realmente aconteceu primeiro.

### Aplicação profissional

Isso importa demais no seu trabalho, porque a tentação de ordenar eventos por timestamp de parede é enorme — é o jeito mais simples de programar um painel, um log, uma fila. Mas se dois eventos vierem de máquinas diferentes, o timestamp de parede pode te enganar, como enganou a equipe de operações da NexaOrder.

Lembra do identificador de correlação que eu mencionei na aula passada, quando falamos de comunicação entre processos? Pois é exatamente aqui que ele se encontra com o tema de hoje. Um identificador de correlação bem desenhado não substitui o relógio lógico, mas ajuda demais a reconstruir, depois de um incidente, a cadeia real de mensagens que ligou um evento ao outro — em vez de você tentar adivinhar essa cadeia só olhando carimbos de hora físicos espalhados em logs de serviços diferentes. Quando a disciplina chegar em observabilidade, na Unidade 4, você vai ver como *traces* distribuídos usam exatamente essa ideia, combinando identificadores de correlação com uma noção de ordem parecida com a que estudamos hoje.

A lição prática: para decidir causalidade, use relógio lógico ou vetorial, ou pelo menos um identificador de correlação que capture a cadeia de mensagens. E para os casos em que os eventos são genuinamente concorrentes — o que vai acontecer, mais cedo ou mais tarde, em qualquer sistema com múltiplos serviços — defina, antes do incidente acontecer em produção, qual é a política de negócio para resolver o conflito.

Se você entrar em um time que já opera um sistema distribuído em produção, uma boa pergunta para levar na primeira reunião de arquitetura é: "como esse sistema decide qual evento aconteceu primeiro, quando dois deles chegam de serviços diferentes?" Se a resposta for "a gente ordena pelo timestamp que vem em cada mensagem", vale a pena investigar se esse timestamp é físico ou lógico, e se alguém já mapeou os cenários em que essa ordenação pode enganar a operação — exatamente como enganou a equipe da NexaOrder nesta aula.

E não esquece: nenhuma dessas técnicas é sobre "ter um relógio melhor". É sobre aceitar que causalidade e tempo físico são duas coisas diferentes, e que confundir uma com a outra é o tipo de erro que só aparece quando o sistema já está em produção, sob carga real, com múltiplos servidores em regiões diferentes — exatamente o cenário em que você, profissionalmente, vai estar.

### Pausa para reflexão

Antes de fechar, quero te propor uma reflexão rápida, baseada na situação-problema desta aula. O painel da NexaOrder concluiu que o cancelamento aconteceu primeiro, só porque o timestamp de parede dizia isso — mas o relógio do servidor de pagamento estava atrasado.

*[indicação de edição: pausar a narração por 5 segundos com o texto "Pense: essa conclusão está garantida pelos dados?" na tela]*

Pergunto: essa conclusão estava logicamente garantida? E, mesmo com relógio vetorial, identificando que os dois eventos são concorrentes, o sistema saberia sozinho qual dos dois deveria prevalecer? Guarda essas perguntas — elas estão na atividade prática do texto-base, e eu quero que você as responda por escrito antes de seguir para a próxima aula.

Uma última observação sobre essa pausa: repare que nenhuma das quatro perguntas pede pra você "descobrir a verdade" sobre qual evento aconteceu primeiro. Isso é proposital. Em muitos casos reais, essa verdade simplesmente não existe de forma recuperável — os dois eventos podem ser genuinamente concorrentes, e insistir em encontrar uma ordem "certa" entre eles é procurar uma resposta que a própria estrutura do sistema não garante.

### Fechamento

Recapitulando: não existe relógio global; relógios físicos divergem por desvio acumulado; a relação happened-before ordena por causalidade, não por tempo de parede; o relógio de Lamport garante que causalidade implica número crescente, mas não detecta concorrência sozinho; o relógio vetorial detecta concorrência com certeza, comparando vetores posição a posição.

Na próxima e última aula desta unidade, vamos falar sobre o que fazer quando um componente simplesmente para de responder — os modelos de falha, os detectores de falha e os padrões de resiliência que protegem a NexaOrder de um colapso em cascata. Te vejo lá.

*[indicação de edição: encerrar com tela de créditos e o texto "Próxima aula: Modelos de falha e desenho para recuperação"]*

### Indicações de edição e recursos visuais

- Abertura: dois relógios de parede, um adiantado e um atrasado, sobre os ícones de estoque e pagamento.
- Fórmula do desvio máximo de relógio, com destaque progressivo dos termos.
- Recurso visual 1 (Aula 3 do texto-base): linha do tempo dos relógios lógicos por raia de processo.
- Tabela ao vivo, preenchida linha a linha, com o exemplo de relógio de Lamport entre pedidos e estoque.
- Recurso visual 2 (Aula 3 do texto-base): comparação de vetores concorrentes (2,3,0) e (2,1,2).
- Pausa de 5 segundos com texto de reflexão em tela durante a seção de pausa para reflexão.
- Encerramento com chamada para a próxima videoaula.

### Fontes e links de mídia

- Diagramas, tabela e fórmulas originais, produzidos a partir do texto-base da Aula 3 (`unidade_1.md`).
- Referência conceitual de apoio: LAMPORT, Leslie. Time, clocks, and the ordering of events in a distributed system. Communications of the ACM, v. 21, n. 7, p. 558-565, 1978. DOI: 10.1145/359545.359563 (não há trecho de vídeo ou áudio externo a licenciar nesta videoaula).

## Roteiro da Videoaula 4 — "Um serviço lento não é um serviço fora do ar: contendo o colapso em cascata"

**Vínculo com o plano de aprendizagem:** Unidade 1, Aula 4 — Modelos de falha e desenho para recuperação.

**Objetivo da videoaula:** ao final, o estudante deve ser capaz de classificar modelos de falha, reconhecer os limites dos detectores de falha, e aplicar os padrões circuit breaker, bulkhead e degradação graciosa a um fluxo distribuído.

### Abertura contextualizada

Chegamos à última aula da Unidade 1! E eu quero fechar com o incidente mais assustador que a NexaOrder enfrentou até aqui. Durante uma campanha de vendas, o provedor de pagamento externo começou a responder devagar — não caiu, só ficou lento. E, olha que interessante: o serviço de pedidos não tinha nenhum bug no seu próprio código. Mesmo assim, ele parou de responder — inclusive para consultas de pedidos antigos, que não tinham nada a ver com pagamento.

*[indicação de edição: inserir animação de um funil se enchendo — conexões do serviço de pedidos todas ocupadas esperando o provedor de pagamento]*

Como uma lentidão pontual, em um único componente externo, virou um colapso mais amplo? É essa pergunta que a gente responde hoje.

### Desenvolvimento conceitual

Primeiro, vocabulário. Nem toda falha é igual, e distinguir os tipos ajuda demais a desenhar proteção certa. Falha de parada: o componente simplesmente para e fica parado — não responde mais nada, mas também não responde errado. É o modelo mais comum, e o mais benigno.

Falha de omissão: o componente continua rodando, mas perde algumas mensagens — de envio ou de recebimento —, por exemplo, por fila cheia ou descarte sob sobrecarga.

Falha de temporização: o componente responde certo, mas fora do prazo esperado — geralmente tarde demais. Foi exatamente o que aconteceu com o provedor de pagamento da NexaOrder.

E falha de comportamento arbitrário, às vezes chamada de falha bizantina: o componente responde de forma incorreta ou inconsistente, sem seguir o protocolo esperado. É rara dentro de uma única organização, mas relevante quando você integra com múltiplos parceiros externos.

*[indicação de edição: inserir quadro comparativo com os quatro tipos de falha e um ícone representativo para cada um]*

Vamos fixar isso com exemplos rápidos, todos dentro da própria NexaOrder. Falha de parada: a instância do serviço de estoque trava e some do balanceador, sem responder mais nada — comportamento benigno, fácil de detectar. Falha de omissão: o broker de mensagens descarta silenciosamente uma pequena fração das mensagens sob pico de carga, porque a fila está cheia — o serviço de pagamento simplesmente nunca recebe aquele evento específico. Falha de temporização: exatamente o nosso incidente de hoje, o provedor de pagamento respondendo, só que tarde demais. E falha de comportamento arbitrário: um parceiro de logística externo, mal integrado, retorna um código de sucesso mesmo quando a expedição não foi de fato agendada — isso é raro, mas quando acontece, é o mais difícil de detectar, porque o sistema não está em silêncio, está mentindo.

Repare que o incidente da NexaOrder foi uma falha de temporização, não de parada. E isso é importante, porque, como vimos na Aula 1, um timeout não prova que a operação falhou — ele só indica que a resposta não chegou dentro do prazo tolerado. É uma decisão, não uma certeza.

Quem decide se um componente está indisponível é o detector de falhas — e nenhum detector real é perfeito. Ele pode declarar indisponível um componente que só está lento — falso positivo — ou pode demorar a perceber uma indisponibilidade real — falso negativo. Detectar rápido aumenta o risco de falso positivo; esperar mais aumenta o atraso de reação. Não tem almoço grátis aqui.

Pra NexaOrder, um detector de falhas pode ser tão simples quanto contar falhas consecutivas de uma chamada ao provedor de pagamento — três falhas seguidas, trata como indisponível — ou tão elaborado quanto combinar taxa de erro, latência observada e resultado de verificações de saúde periódicas. O que importa é você nunca esquecer que esse detector é uma estimativa. Ele não é uma câmera apontada para dentro do provedor de pagamento, mostrando o que está acontecendo lá dentro de verdade. Ele é uma inferência, feita de fora, com informação incompleta.

Tem outro cenário que precisa entrar no seu vocabulário: o particionamento de rede. Imagina duas réplicas do serviço de estoque, em duas zonas diferentes, que perdem a comunicação entre si, mas cada uma continua funcionando internamente, normalmente. Do ponto de vista de cada lado, o outro lado "sumiu" — mas nenhum dos dois, tecnicamente, está fora do ar. Se as duas continuarem aceitando reserva para os mesmos itens, sem saber uma da outra, você tem uma divergência de estado, que informalmente é chamada de split-brain.

*[indicação de edição: inserir Recurso visual 1 da Aula 4 — duas zonas isoladas por rompimento de rede]*

Antes de seguir pra demonstração, deixa eu reforçar um princípio que atravessa tudo isso: redundância sozinha não é proteção. Redundância só protege contra falha se as instâncias redundantes não compartilharem o mesmo ponto de falha, e se existir um mecanismo capaz de desviar o tráfego quando uma delas para. Duas instâncias no mesmo servidor físico não te protegem de nada, se esse servidor cair. E, como você vai ver já já, ter várias instâncias também não te protege se todas elas competirem pelos mesmos recursos internos ao atender uma dependência lenta.

### Demonstração, exemplo ou estudo de caso

Voltando ao incidente: por que a lentidão do pagamento derrubou até as consultas de pedidos, que nada tinham a ver com pagamento? Porque o serviço de pedidos usava o mesmo conjunto de conexões pra tudo. Quando o pagamento ficou lento, todas as conexões disponíveis ficaram presas esperando resposta do pagamento — e não sobrou capacidade pra atender nada mais. Redundância sem isolamento não protege ninguém.

É aqui que entram três padrões de resiliência que eu quero que você domine.

O primeiro é o circuit breaker, o disjuntor. Ele tem três estados: fechado, em que as chamadas fluem normalmente enquanto o disjuntor monitora a taxa de falha; aberto, em que, depois de ultrapassar um limite de falhas, o disjuntor passa a rejeitar chamadas imediatamente, sem nem tentar a dependência, por um tempo definido; e semiaberto, em que, passado esse tempo, ele libera algumas chamadas de teste — se derem certo, volta pra fechado; se derem errado, volta pra aberto.

*[indicação de edição: inserir Recurso visual 2 da Aula 4 — diagrama de estados do circuit breaker]*

Vamos ao número. Se a NexaOrder define um limite de 50% de falhas numa janela das últimas 20 chamadas ao provedor de pagamento, e observa 12 falhas nessa janela, a taxa de erro é 12 dividido por 20 — 0,60, ou 60%. Como 60% passa do limite de 50%, o disjuntor abre. As chamadas seguintes são rejeitadas na hora, pelo próprio serviço de pedidos, sem nem esperar o timeout de rede — liberando recursos pra atender, por exemplo, consultas de pedidos antigos. É exatamente o isolamento que faltou no nosso incidente.

O segundo padrão é o bulkhead, o anteparo — pensa nos compartimentos estanques de um navio, que impedem que um alagamento afunde o navio inteiro. Na prática, você separa os recursos — conexões, threads, filas — por dependência. Se o serviço de pedidos reservar um conjunto de conexões só para o provedor de pagamento, separado do conjunto usado pra consultas, a lentidão do pagamento esgota só o próprio compartimento dele.

O terceiro é a degradação graciosa: continuar oferecendo uma versão reduzida do serviço quando uma dependência não essencial falha, em vez de falhar tudo. Se o serviço de recomendação de produtos cair, a tela de checkout simplesmente esconde as recomendações e segue com a compra. Isso exige que você classifique, antes do incidente, o que é essencial e o que é acessório.

E note como esses três padrões respondem exatamente ao princípio que eu falei no começo, sobre timeout ser uma decisão, não uma prova de falha. O circuit breaker decide, com base em taxa de erro observada, quando parar de tentar. O bulkhead decide, com base em criticidade, como dividir os recursos disponíveis. E a degradação graciosa decide, com base em valor de negócio, o que pode ser sacrificado temporariamente para manter o essencial de pé. Nenhum dos três espera por uma certeza absoluta de que algo quebrou — todos operam com estimativa, exatamente como o detector de falhas que discutimos há pouco.

### Aplicação profissional

No seu trabalho, essas três técnicas — circuit breaker, bulkhead, degradação graciosa — praticamente sempre aparecem juntas em sistemas de produção maduros. E elas servem a um objetivo mensurável: um objetivo de confiabilidade explícito, tipo "99,9% de disponibilidade no fluxo de criação de pedidos", que define quanto de indisponibilidade é tolerável e até onde vale a pena investir em resiliência adicional. Sem esse objetivo declarado, resiliência vira um investimento sem critério de parada — você nunca sabe se já fez o suficiente.

*[indicação de edição: inserir card com o objetivo de disponibilidade e o orçamento de indisponibilidade correspondente em minutos por mês]*

E aqui vale uma reflexão de carreira: engenheiros iniciantes costumam tratar resiliência como "quanto mais proteção, melhor". Engenheiros experientes perguntam primeiro qual é o objetivo de confiabilidade que está sendo perseguido, porque cada camada de proteção — disjuntor, anteparo, degradação graciosa, redundância adicional — tem custo de implementação, de operação e, muitas vezes, de complexidade cognitiva para quem vai dar plantão. Se o fluxo de criação de pedidos já atinge 99,9% de disponibilidade e esse número atende ao negócio, investir semanas de trabalho para chegar a 99,99% pode não valer a pena — a menos que o requisito de negócio realmente exija esse salto.

Antes de fechar, um convite direto: pega o fluxo de criação de pedidos da NexaOrder — pedidos, estoque, pagamento, expedição — e, pra cada etapa, pergunta: qual modo de falha é plausível aqui? Qual o efeito nas etapas vizinhas se eu não proteger nada? E qual proteção, entre timeout, circuit breaker, bulkhead ou degradação graciosa, eu aplicaria? Essa é a atividade prática completa do texto-base — vale a pena fazer com calma, porque ela amarra tudo o que vimos nesta unidade.

### Fechamento

Recapitulando: falhas se classificam em parada, omissão, temporização e comportamento arbitrário; detectores de falha são estimativas, não certezas; particionamento de rede isola grupos que continuam funcionando, mas podem divergir entre si; e circuit breaker, bulkhead e degradação graciosa são padrões complementares de contenção, sempre orientados por um objetivo de confiabilidade explícito.

E com isso a gente fecha a Unidade 1. Você já sabe o que caracteriza um sistema distribuído, como os serviços da NexaOrder se comunicam, como ordenar eventos sem relógio global, e como conter falhas parciais. Repara no fio que ligou as quatro aulas: componentes autônomos, conectados por uma rede imperfeita, podem discordar temporariamente sobre o estado do sistema — e um bom projeto distribuído não finge que essa discordância não existe, ele prevê como lidar com ela.

Na Unidade 2, a gente desloca essa mesma pergunta para os dados. Se estoque e pagamento podem observar eventos concorrentes, como réplicas de um mesmo dado devem ser mantidas consistentes entre si? Se uma partição de rede pode isolar dois grupos de nós, como o sistema deve se comportar sem violar suas garantias mais importantes? E quando múltiplos nós precisam concordar sobre um único fato — por exemplo, qual reserva de estoque é válida —, que mecanismos garantem esse acordo mesmo diante de falhas? Vamos falar de replicação, particionamento, o teorema CAP e algoritmos de consenso, sempre com a NexaOrder como fio condutor. Te vejo lá.

*[indicação de edição: encerrar com tela de créditos e o texto "Próxima unidade: Dados distribuídos, consistência e coordenação"]*

### Indicações de edição e recursos visuais

- Abertura: animação de funil se enchendo, representando conexões do serviço de pedidos esgotadas esperando o provedor de pagamento.
- Quadro comparativo dos quatro tipos de falha, com ícone representativo para cada um.
- Recurso visual 1 (Aula 4 do texto-base): duas zonas isoladas por rompimento de rede (particionamento).
- Recurso visual 2 (Aula 4 do texto-base): diagrama de estados do circuit breaker.
- Card com o objetivo de disponibilidade e o orçamento de indisponibilidade em minutos por mês.
- Encerramento com chamada de transição para a Unidade 2.

### Fontes e links de mídia

- Diagramas, quadro comparativo e fórmulas originais, produzidos a partir do texto-base da Aula 4 (`unidade_1.md`).
- Referência conceitual de apoio: CHANDRA, Tushar Deepak; TOUEG, Sam. Unreliable failure detectors for reliable distributed systems. Journal of the ACM, v. 43, n. 2, p. 225-267, 1996. DOI: 10.1145/226643.226647 (não há trecho de vídeo ou áudio externo a licenciar nesta videoaula).
