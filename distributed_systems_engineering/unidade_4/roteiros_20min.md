# Roteiros das videoaulas 13 a 16

Duração-base de 20 minutos por videoaula (aproximadamente 2.200 a 2.700 palavras faladas por roteiro, ajustado pela presença de demonstrações). Os roteiros abaixo são textos de narração para gravação, não notas de aula. Marcações de edição, indicações de recurso visual e sugestões de tela aparecem *em itálico, entre colchetes*.

## Videoaula 13 — “Doze segundos de silêncio: seguindo um pedido pelo sistema”

**Vínculo com o plano de aprendizagem:** Unidade 4, Aula 13 — Observabilidade e diagnóstico distribuído.

**Objetivo da videoaula:** capacitar o estudante a diferenciar monitoramento de observabilidade, a reconhecer o papel complementar de métricas, logs e traces, e a interpretar um trace distribuído para localizar a origem de uma latência inesperada.

### Abertura contextualizada

Imagine que você recebe uma mensagem de um cliente da NexaOrder: “meu pedido demorou doze segundos para confirmar, e eu quase desisti da compra”. Você abre o painel de infraestrutura. CPU normal. Memória normal. Nenhum alerta disparado. Nenhum serviço caiu. E, mesmo assim, doze segundos aconteceram, para uma pessoa real, em um momento real. *[indicação de edição: abrir com tela de painel de métricas “tudo verde”, seguida de uma notificação de reclamação de cliente sobreposta]*

Essa é uma cena comum na vida de quem opera sistemas distribuídos, e é o ponto de partida da nossa videoaula de hoje. Vamos entender por que “estar tudo verde” nos painéis não significa que sabemos o que está acontecendo dentro do sistema — e o que muda quando um sistema passa a ser, de fato, observável.

### Desenvolvimento conceitual

Vamos começar separando dois termos que, no dia a dia das equipes, costumam ser usados como sinônimos, mas não são: monitoramento e observabilidade.

Monitoramento é observar indicadores que você já decidiu, de antemão, que são importantes. CPU, memória, taxa de erro agregada, tempo de resposta médio. Você define um limite, configura um alerta, e é avisado quando esse limite é ultrapassado. Isso é extremamente útil — mas só funciona para perguntas que você já sabia fazer antes do problema acontecer.

Observabilidade é diferente. É a capacidade de investigar uma pergunta que ninguém formulou antes, usando os dados que o sistema já está expondo. “O que aconteceu com o pedido número 48213, especificamente, entre 14h32 e 14h32min12s?” — essa não é uma pergunta que cabe em um painel de CPU. Ela exige dados granulares, contextualizados, e conectados entre si. *[indicação de edição: inserir quadro comparativo simples: “Monitoramento: perguntas conhecidas” à esquerda, “Observabilidade: perguntas não antecipadas” à direita]*

E é aqui que entram os três pilares que sustentam a observabilidade moderna: métricas, logs e traces.

Métricas são números agregados ao longo do tempo. Requisições por segundo, taxa de erro, percentual de utilização. Elas são baratas de guardar por muito tempo e ótimas para detectar tendências — mas, sozinhas, não contam uma história completa. Uma taxa de erro de meio por cento não te diz quais requisições falharam, nem por quê.

Logs são registros de eventos específicos: “pedido recebido”, “estoque reservado”, “timeout ao chamar o provedor de pagamento”. Eles têm riqueza de detalhe, mas, se cada serviço guarda seus próprios logs isoladamente, sem nenhuma forma de juntar os pedaços, você tem fragmentos de uma história, não a história inteira.

Vale um parêntese sobre custo, porque isso influencia decisões reais de engenharia. Métricas são baratas justamente porque são agregadas — guardar “número de erros por minuto” pelos próximos dois anos ocupa muito pouco espaço. Traces e logs detalhados, por outro lado, geram um volume de dados imenso quando você multiplica milhares de requisições por segundo pelo número de spans de cada uma. Por isso, é comum aplicar amostragem: guardar o trace completo de, digamos, 5% das requisições bem-sucedidas, mas guardar 100% das requisições que resultaram em erro ou que ultrapassaram um limite de latência. Você não perde justamente os casos que mais importa investigar, e ainda economiza espaço de armazenamento.

E traces. Um trace representa a jornada completa de uma única requisição através de vários serviços. Ele quebra essa jornada em pedaços menores, chamados spans — cada span representa uma operação específica, com início, fim, e duração. Se você reconstrói o trace de um pedido específico, você vê, em uma única visualização, exatamente por onde ele passou e quanto tempo levou em cada etapa. *[indicação de edição: animação simples mostrando quatro blocos — gateway, pedidos, estoque, pagamento, expedição — conectados por setas, com uma barra de tempo crescendo sob cada bloco]*

Nenhum dos três substitui o outro. Métrica te diz que algo mudou. Trace te mostra onde, dentro de uma requisição específica, esse algo aconteceu. Log te conta, em detalhe, o que exatamente ocorreu naquele ponto.

Mas para que um trace funcione, é preciso um ingrediente adicional: correlação. Cada requisição que entra na NexaOrder recebe um identificador único — geralmente chamado de trace ID — logo na entrada, no gateway. Esse identificador precisa viajar junto com a requisição em cada chamada seguinte. Quando o serviço de pedidos chama o serviço de estoque, o identificador vai junto, dentro de um cabeçalho da requisição. Quando um evento é publicado para o serviço de expedição, o identificador precisa ir junto nos metadados desse evento também.

E atenção: essa propagação não acontece sozinha, por mágica da rede. Ela é responsabilidade explícita de instrumentação. Se um único serviço, no meio do caminho, esquecer de propagar esse identificador, o trace se rompe ali. E é exatamente por isso que existe um padrão aberto chamado OpenTelemetry: ele define, de forma neutra em relação a qualquer fornecedor de ferramenta, como instrumentar aplicações para capturar métricas, logs e traces de forma consistente, incluindo essa propagação de contexto entre serviços. *[indicação de edição: logotipo ou tela de documentação do OpenTelemetry, de forma ilustrativa]*

Na prática, o fluxo funciona assim: cada serviço da NexaOrder roda um pequeno agente de instrumentação, capaz de capturar automaticamente operações comuns — uma chamada HTTP recebida, uma consulta ao banco de dados, a publicação de um evento. Esses dados são enviados para um coletor, que os processa e os encaminha para o backend de armazenamento e visualização escolhido pela equipe. E aqui está o ponto importante: se, daqui a dois anos, a NexaOrder decidir trocar de ferramenta de análise de traces, o código de instrumentação de cada serviço não precisa mudar — só o destino dos dados muda, lá no coletor. Isso evita que a equipe fique presa a um único fornecedor, e evita também que cada squad instrumente do seu próprio jeito, criando um quebra-cabeça impossível de juntar depois.

### Demonstração, exemplo ou estudo de caso

Vamos voltar ao nosso caso: os doze segundos.

Com o trace reconstruído — porque, neste cenário, a NexaOrder já tinha instrumentação OpenTelemetry implantada — a equipe consegue ver a árvore completa de spans daquela requisição específica. E os números aparecem assim: gateway, 15 milissegundos; serviço de pedidos, 40 milissegundos; serviço de estoque, 35 milissegundos; serviço de pagamento, 310 milissegundos; serviço de expedição, 20 milissegundos.

Somando o tempo de serviço, chegamos a cerca de 420 milissegundos — e ainda existe um atraso adicional de rede e de fila que, nesse caso específico, ampliou o tempo total percebido para os doze segundos relatados pelo cliente. Mas repare: mesmo sem chegar ao valor exato de doze segundos só com essa soma, a distribuição já aponta exatamente para onde olhar. O serviço de pagamento sozinho responde por mais de 70% do tempo de serviço somado. *[indicação de edição: exibir diagrama de cascata, com a barra do serviço de pagamento visivelmente mais longa que as demais, destacada em cor diferente]*

Esse é o primeiro suspeito. E, ao investigar esse span específico, a equipe encontra o problema: uma chamada ao provedor externo de pagamento sem um timeout configurado adequadamente, que em determinadas condições de rede simplesmente aguardava, silenciosamente, muito além do razoável.

Sem o trace, essa investigação levaria horas — cruzando logs manualmente, em quatro sistemas diferentes, tentando adivinhar qual entrada, em qual arquivo, correspondia ao pedido reclamado pelo cliente. Com o trace, levou minutos.

Vale narrar o passo a passo real dessa investigação, porque é exatamente isso que você vai fazer no seu dia a dia. A pessoa de plantão recebe o número do pedido, cola esse número em um campo de busca na ferramenta de observabilidade, e o trace correspondente aparece na tela em segundos. Ela expande o span do serviço de pagamento — o mais longo de todos — e vê, ali dentro, um span filho representando a chamada ao provedor externo, com uma tag indicando “timeout após 300 segundos”. Ela então busca, pelo mesmo identificador de correlação, os logs daquele span específico, e encontra a mensagem exata de erro registrada pelo serviço no momento da falha. Três telas, um identificador comum, menos de cinco minutos. *[indicação de edição: gravação de tela simulada, mostrando a navegação da busca pelo identificador até o log específico]*

E aqui entra outro conceito importante: como saber, de forma contínua, se esse tipo de problema está piorando ou melhorando? É aqui que entram os indicadores de nível de serviço, os SLIs. Para o checkout da NexaOrder, um bom SLI não é “CPU está normal”. Um bom SLI é, por exemplo, “proporção de requisições de checkout concluídas dentro de 300 milissegundos”. Esse número reflete diretamente a experiência de quem está comprando — não apenas a saúde interna dos servidores.

E quando você define uma meta para esse indicador — digamos, 99,9% das requisições dentro desse limite, ao longo de um mês —, você tem um objetivo de nível de serviço, um SLO. A diferença entre 100% e essa meta é o que chamamos de orçamento de erro. *[indicação de edição: inserir cálculo na tela]* Se a NexaOrder processa 12 milhões de requisições de checkout por mês, e o SLO é 99,9%, o orçamento de erro mensal é de 12 mil requisições malsucedidas toleradas. Se, em dez dias, a equipe já consumiu 9 mil dessas 12 mil — 75% do orçamento, em um terço do mês —, isso é um sinal claro: reduzir o ritmo de mudanças arriscadas, e investigar com prioridade, antes que o orçamento se esgote de vez.

Vale diferenciar rapidamente SLO de um termo parecido, que você provavelmente já ouviu: SLA, o acordo de nível de serviço. O SLO é uma meta interna, usada pela equipe para orientar decisões técnicas do dia a dia. O SLA costuma ser um compromisso contratual, assumido perante clientes ou parceiros, com consequências formais — financeiras, inclusive — caso não seja cumprido. É comum, e recomendado, que o SLO interno seja mais rigoroso do que o SLA externo: isso dá à equipe uma margem de segurança, permitindo agir antes que a meta contratual, mais visível e mais cara de violar, seja de fato ameaçada.

### Aplicação profissional

No dia a dia de um engenheiro de confiabilidade, de um engenheiro de plataforma, ou mesmo de qualquer desenvolvedor responsável por um serviço em produção, essa é uma das competências mais valorizadas: a capacidade de instrumentar corretamente um serviço desde o início, e de usar essa instrumentação para investigar incidentes com rapidez, em vez de depender de tentativa e erro. Empresas de médio e grande porte frequentemente perguntam, em entrevistas técnicas, sobre exatamente esse tipo de cenário: “como você investigaria uma requisição lenta em um sistema distribuído?”. A resposta que você acabou de ver — trace, correlação, SLI, SLO, orçamento de erro — é, literalmente, a resposta que se espera de um profissional maduro nessa área.

Pense também em quem está de plantão, no meio da madrugada, recebendo um alerta sozinho. Sem observabilidade, essa pessoa depende de sorte e de memória: “será que já vi esse erro antes? Em qual serviço?”. Com observabilidade, essa mesma pessoa abre um painel, busca pelo identificador de correlação do pedido reclamado, e em poucos cliques está olhando exatamente para o span que concentra o problema. A diferença entre essas duas realidades não é sutil — é a diferença entre um incidente resolvido em quinze minutos e um incidente que vira notícia, ou que vira uma madrugada inteira perdida.

### Fechamento

Voltando à nossa cena inicial: painel verde, cliente reclamando, doze segundos sem explicação. A diferença entre resolver esse problema em minutos ou em horas não está na sorte da equipe — está em ter, ou não, instrumentado o sistema para responder perguntas que ainda não foram feitas.

Recapitulando os pontos centrais de hoje: monitoramento observa o que já se sabe importante, observabilidade permite investigar o que ainda não se sabia perguntar. Métricas, logs e traces são complementares, e a correlação entre eles depende de um identificador propagado explicitamente, com o apoio de uma instrumentação consistente, como a que o OpenTelemetry padroniza. SLIs bem escolhidos refletem a experiência de quem usa o sistema, e o orçamento de erro transforma um SLO em uma decisão operacional concreta sobre quando desacelerar.

Na próxima aula, vamos além do diagnóstico: vamos aprender a testar, deliberadamente, se os mecanismos de resiliência do sistema realmente funcionam sob falha — porque, como veremos, às vezes a resposta é “não, e ninguém sabia”. *[indicação de edição: encerrar com a frase-chave em tela: “Observabilidade não é sobre ter painéis. É sobre poder responder perguntas que você ainda não fez.”]*

### Indicações de edição e recursos visuais

- Abertura: painel de métricas “tudo verde” sobreposto por notificação de reclamação de cliente.
- Quadro comparativo monitoramento versus observabilidade.
- Animação da jornada de uma requisição pelos quatro serviços da NexaOrder.
- Diagrama de cascata (waterfall) do trace, com o span do serviço de pagamento destacado.
- Cálculo do orçamento de erro exibido em tela, com os números do exemplo.
- Encerramento com frase-chave em tela.

### Fontes e links de mídia

- Documentação oficial do OpenTelemetry, seção de conceitos de traces e spans: <https://opentelemetry.io/docs/concepts/signals/traces/> — usar como referência visual da estrutura de spans, sem reprodução de trecho específico além de capturas de tela ilustrativas da própria documentação pública.
- O’REILLY, Tim et al. *Site Reliability Engineering*. Sebastopol: O’Reilly Media, 2016 — capítulo sobre monitoramento de sistemas distribuídos, como referência conceitual para SLI, SLO e orçamento de erro.

## Videoaula 14 — “O circuito que não segurou: planejando um experimento de caos”

**Vínculo com o plano de aprendizagem:** Unidade 4, Aula 14 — Resiliência, testes distribuídos e engenharia do caos.

**Objetivo da videoaula:** capacitar o estudante a distinguir tipos de teste em sistemas distribuídos, a compreender os princípios da engenharia do caos e a planejar um experimento controlado de indisponibilidade com hipótese de estado estável, raio de impacto limitado e mecanismo de interrupção.

### Abertura contextualizada

Black Friday. O provedor de pagamento usado pela NexaOrder trava por alguns minutos — uma instabilidade pequena, do tipo que acontece com qualquer provedor externo, de vez em quando. O problema é o que acontece depois. O serviço de pedidos, esperando a resposta do pagamento, começa a acumular conexões penduradas. Em poucos minutos, o serviço de pedidos também fica lento. E, como o serviço de estoque depende do serviço de pedidos para confirmar reservas, ele também começa a travar. *[indicação de edição: animação de efeito cascata — um bloco pisca em vermelho, e o vermelho se espalha para os blocos vizinhos, um a um]*

A equipe tinha implementado um circuito de proteção exatamente para esse cenário. Só que ninguém nunca tinha testado, de verdade, se ele funcionava. E funcionou? Vamos descobrir juntos por que a resposta, nesse caso, foi não — e o que fazer para nunca mais precisar descobrir isso durante um incidente real.

### Desenvolvimento conceitual

Vamos começar pela pirâmide de testes. Você provavelmente já ouviu falar dela: testes unitários na base, rápidos e baratos; testes de integração no meio, verificando a interação com uma dependência específica; e testes de ponta a ponta no topo, verificando um fluxo de negócio completo, atravessando vários serviços reais. *[indicação de edição: desenhar a pirâmide na tela, camada por camada, conforme cada tipo é mencionado]*

Em um sistema distribuído, o topo dessa pirâmide é caro. Um teste de ponta a ponta do fluxo de compra da NexaOrder exige que pedidos, estoque, pagamento e expedição estejam todos rodando, configurados de forma coerente. É lento. É frágil — qualquer mudança não relacionada pode quebrar o teste. E, quando falha, é difícil saber exatamente onde está o problema.

Por isso, existe um tipo de teste intermediário, muito subestimado: o teste de contrato. A ideia é simples e poderosa. Em vez de rodar dois serviços juntos para verificar se eles se entendem, você verifica separadamente se cada um cumpre um contrato acordado. O serviço de estoque, que consome eventos publicados pelo serviço de pedidos, declara: “eu espero receber um evento com estes campos, deste jeito”. Essa expectativa vai para um repositório compartilhado. E, no pipeline do serviço de pedidos, antes de qualquer implantação, o contrato é verificado automaticamente. Se alguém mudar o nome de um campo sem querer, o pipeline quebra ali — não em produção, semanas depois, quando ninguém mais lembra da mudança.

Esse padrão costuma ser chamado de teste de contrato orientado pelo consumidor, porque é o serviço consumidor — no nosso caso, o estoque — quem define o que espera receber, não o serviço produtor. Isso é importante: em uma organização com dezenas de equipes trabalhando de forma independente, ninguém no time de pedidos precisa saber, de cor, todos os detalhes internos do time de estoque. O contrato formaliza esse conhecimento, tornando-o verificável automaticamente, todas as vezes, sem depender de reunião, de mensagem no chat, ou de alguém lembrar de avisar.

Agora, além de testes de contrato, existem três tipos de teste que avaliam comportamento sob demanda, e é fácil confundi-los. Teste de carga verifica se o sistema aguenta o tráfego esperado — o volume normal de um dia, ou o pico projetado de uma campanha — sem violar suas metas de latência e erro. Teste de estresse aumenta a carga além do esperado, de propósito, até o sistema quebrar, para você saber exatamente onde está o limite. E teste de duração — também chamado de soak test — mantém uma carga por um período longo, horas, às vezes dias, para revelar problemas que só aparecem com o tempo: vazamento de memória, esgotamento gradual de conexões. *[indicação de edição: três gráficos pequenos lado a lado, mostrando o perfil de carga de cada tipo de teste ao longo do tempo]*

Mas nenhum desses testes — nem mesmo o de estresse — responde à pergunta que realmente importa depois de um incidente como o nosso: “o que acontece, de fato, quando uma dependência externa fica indisponível?”. Um teste de estresse, por exemplo, aumenta a carga sobre o próprio sistema, mas normalmente presume que as dependências externas continuam saudáveis. O nosso incidente não foi causado por excesso de carga — foi causado por uma dependência externa, fora do controle da NexaOrder, ficando temporariamente indisponível. É um tipo de falha diferente, que exige um tipo diferente de teste. Para responder isso, entra a engenharia do caos.

A engenharia do caos é a prática de injetar falhas deliberadas — latência extra, erros simulados, indisponibilidade total de um componente — em um sistema, e observar o que realmente acontece, em vez de presumir. E o ponto de partida de todo experimento sério é a hipótese de estado estável: uma expectativa mensurável, específica, sobre o comportamento normal do sistema, formulada antes de qualquer falha ser injetada.

Não é “o sistema deve continuar funcionando” — isso é vago demais para significar alguma coisa. É algo como: “em condições normais, a taxa de conclusão de pedidos fica acima de 98%, e a latência do checkout fica abaixo de 400 milissegundos no percentil 95. Durante a indisponibilidade simulada do provedor de pagamento, o circuito de proteção deve ser acionado, o sistema deve degradar de forma graciosa, informando o cliente, e a taxa de conclusão de pedidos não deve cair abaixo de 90%”. *[indicação de edição: exibir a hipótese completa, escrita, em tela]*

E note: para formular e verificar essa hipótese, você precisa das métricas que vimos na aula anterior. Observabilidade e engenharia do caos andam juntas — sem uma, a outra fica cega.

Dois princípios protegem esse experimento de virar um novo incidente: raio de impacto limitado e mecanismo de interrupção imediata. Raio de impacto significa começar pequeno — 1% do tráfego real, um pequeno subconjunto de instâncias — e só ampliar gradualmente, conforme a confiança aumenta. Mecanismo de interrupção significa ter um botão, literalmente, capaz de parar a injeção de falha instantaneamente, caso os indicadores de negócio piorem além de um limite predefinido. *[indicação de edição: animação de escopo crescendo em círculos concêntricos — do menor para o maior, com pausa entre cada expansão]*

Na prática, essa progressão costuma seguir etapas parecidas com estas: primeiro, o experimento roda em um ambiente de testes que reproduz as características de produção o mais fielmente possível. Depois, com resultados satisfatórios, ele passa a afetar 1% do tráfego real, monitorado de perto. Se os indicadores de negócio se mantêm dentro do esperado, o raio de impacto sobe para 10%, depois talvez 50%, sempre com o mecanismo de interrupção pronto para agir a qualquer sinal de degradação real. Cada etapa só avança depois que a anterior confirma a hipótese — nunca antes.

### Demonstração, exemplo ou estudo de caso

Vamos entender numericamente por que esse cuidado é tão necessário, olhando de novo para a nossa cadeia de serviços.

Suponha que pedidos, estoque, pagamento e expedição tenham, cada um, individualmente, 99,9% de disponibilidade. Parece um número ótimo, certo? Mas se esses quatro serviços dependem uns dos outros de forma estritamente sequencial e síncrona — sem nenhum mecanismo de tolerância a falha parcial —, a disponibilidade combinada do fluxo completo é o produto das disponibilidades individuais. *[indicação de edição: exibir o cálculo na tela, passo a passo]*

Zero vírgula nove nove nove, elevado à quarta potência, é aproximadamente zero vírgula nove nove seis. Ou seja: 99,9% de disponibilidade em cada serviço isolado se transforma em apenas 99,6% de disponibilidade no fluxo completo. Um valor pior que qualquer componente individual. E é exatamente esse efeito que explica por que o incidente da Black Friday aconteceu: o circuito de proteção existia no papel, mas nunca tinha sido testado sob a condição real que deveria proteger.

Depois de um incidente — ou de um experimento de caos que revela algo inesperado — vem a etapa final: o postmortem sem culpabilização. A ideia central é simples: incidentes complexos raramente têm uma única causa atribuível a uma pessoa. Eles emergem de combinações de decisões, lacunas de teste, condições operacionais que, isoladamente, pareciam razoáveis. Um bom postmortem não termina em “o serviço de pedidos esgotou conexões”. Ele pergunta: por que o circuito de proteção não impediu isso? Por que nenhum teste, nenhum experimento, revelou essa lacuna antes? E quais mudanças sistêmicas, não apenas correções pontuais, reduzem a chance de isso se repetir?

Um bom postmortem, na prática, costuma seguir uma estrutura parecida com esta: uma linha do tempo minuto a minuto do que foi observado e do que a equipe fez; uma seção de impacto, quantificando quantos pedidos foram afetados e por quanto tempo; uma seção de causas contribuintes, no plural, porque raramente existe uma causa única; e uma lista de ações de melhoria, cada uma com um responsável nomeado e um prazo — não “melhorar o monitoramento”, de forma vaga, mas “instrumentar timeout explícito na chamada ao provedor de pagamento, responsável fulano, prazo de duas semanas”. *[indicação de edição: exibir um modelo simplificado de postmortem em tela, com as quatro seções nomeadas]*

### Aplicação profissional

Se você trabalha, ou pretende trabalhar, com confiabilidade de sistemas — seja como SRE, como engenheiro de plataforma, ou mesmo como desenvolvedor responsável por um serviço crítico —, a capacidade de planejar um experimento de caos responsável, com hipótese clara, raio de impacto limitado e mecanismo de interrupção, é uma habilidade concreta e demandada. Empresas que operam plataformas de médio e grande porte tratam engenharia do caos não como luxo, mas como parte do ciclo normal de validação de resiliência — no mesmo nível de importância que testes automatizados de código.

Isso vale para setores muito diferentes entre si. Uma instituição financeira testa deliberadamente a indisponibilidade de um serviço de autorização de crédito, para garantir que transações fiquem em fila com segurança, em vez de simplesmente falharem. Uma plataforma de streaming testa a perda de uma região inteira de data center, para confirmar que o tráfego é redirecionado sem que o usuário perceba. E uma plataforma de comércio eletrônico, como a nossa NexaOrder, testa exatamente o cenário que vimos hoje: a indisponibilidade de um provedor de pagamento externo, fora do seu próprio controle direto. Em todos os casos, o raciocínio é o mesmo: não presumir resiliência, comprová-la.

E não é preciso esperar por uma equipe grande e madura para começar. Mesmo um time pequeno pode conduzir seu primeiro experimento de caos com escopo mínimo: uma única instância, em um ambiente que já reproduz boa parte das condições de produção, com uma hipótese simples e uma métrica clara para observar. O importante não é a sofisticação da ferramenta usada para injetar a falha — é a disciplina de formular a hipótese antes, limitar o escopo, e aprender com o resultado, seja ele o esperado, seja ele uma surpresa desconfortável como a que vimos na abertura desta aula.

### Fechamento

O circuito de proteção da NexaOrder não falhou porque foi mal projetado no papel. Falhou porque nunca tinha sido testado sob a condição exata que deveria proteger.

Recapitulando: a pirâmide de testes recomenda base ampla de testes rápidos e uso seletivo de testes de ponta a ponta; testes de contrato evitam quebras silenciosas entre serviços; testes de carga, estresse e duração respondem a perguntas diferentes sobre comportamento sob demanda; e engenharia do caos, com hipótese de estado estável, raio de impacto limitado e mecanismo de interrupção, transforma suposições de resiliência em evidência real, seguida de aprendizagem sistemática por meio de postmortems sem culpabilização.

Na próxima aula, vamos mudar de escala: em vez de olhar para uma falha isolada, vamos olhar para como processar volumes enormes de dados, em lote e em tempo quase real — inclusive para detectar, entre outras coisas, fraude, antes que ela aconteça. *[indicação de edição: encerrar com a frase-chave em tela: “Resiliência que nunca foi testada é apenas uma suposição.”]*

### Indicações de edição e recursos visuais

- Abertura: animação de efeito cascata entre os quatro serviços.
- Pirâmide de testes desenhada camada por camada.
- Três gráficos de perfil de carga: teste de carga, estresse e duração.
- Hipótese de estado estável exibida por completo em tela.
- Animação de raio de impacto em círculos concêntricos crescentes.
- Cálculo de disponibilidade combinada exibido passo a passo.
- Encerramento com frase-chave em tela.

### Fontes e links de mídia

- BASIRI, Ali et al. Chaos engineering. *IEEE Software*, v. 33, n. 3, p. 35-41, 2016. DOI: 10.1109/MS.2016.60 — referência conceitual para a definição de hipótese de estado estável e raio de impacto.
- Palestra “Chaos Engineering: The History, Principles, and Practice”, canal oficial do YouTube da USENIX (série SREcon): <https://www.youtube.com/@usenix> — usar como referência de linguagem visual para a animação de raio de impacto, sem reprodução de trecho específico.

## Videoaula 15 — “Segundos, não horas: detectando fraude em tempo quase real”

**Vínculo com o plano de aprendizagem:** Unidade 4, Aula 15 — Processamento distribuído, edge e serverless.

**Objetivo da videoaula:** capacitar o estudante a diferenciar processamento em lote e em fluxo, a compreender o modelo MapReduce e sua generalização em DAGs, e a avaliar compromissos entre funções como serviço, computação de borda e processamento centralizado para um requisito de decisão em tempo quase real.

### Abertura contextualizada

O time de risco da NexaOrder identifica um padrão preocupante: alguém testando vários cartões de crédito diferentes, em sequência rápida, a partir do mesmo dispositivo. A primeira proposta técnica é simples: um job que roda a cada hora, lê o histórico de tentativas, e sinaliza padrões suspeitos para revisão manual no dia seguinte. *[indicação de edição: relógio acelerado passando de 1 hora, com um selo “tarde demais” aparecendo por cima]*

O time de risco rejeita a proposta na hora: uma hora é tempo suficiente para dezenas de fraudes serem aprovadas. A decisão precisa acontecer em segundos, não em horas. Essa exigência muda completamente o tipo de arquitetura necessária — e é exatamente isso que vamos explorar hoje.

### Desenvolvimento conceitual

Existem, essencialmente, duas formas de processar grandes volumes de dados distribuídos: em lote e em fluxo.

Processamento em lote opera sobre um conjunto de dados finito, coletado ao longo de um período, processado de uma vez só. É perfeito para coisas que podem esperar: relatório diário de vendas, cálculo mensal de comissão, reprocessamento de dados históricos depois de uma correção. A vantagem é a simplicidade: você sabe exatamente qual é o conjunto de dados no momento de processar.

Processamento em fluxo — streaming — opera sobre uma sequência de eventos que, em princípio, nunca acaba. Cada evento é processado assim que chega, sem esperar formar um lote completo. Para a nossa detecção de fraude, essa é claramente a escolha certa: cada tentativa de pagamento precisa ser avaliada no instante em que acontece. *[indicação de edição: comparação visual lado a lado — de um lado, uma caixa fechada representando “lote”; do outro, uma esteira contínua representando “fluxo”]*

Agora, como esse processamento em larga escala realmente funciona por baixo dos panos? O modelo clássico que originou boa parte dessas ideias é o MapReduce, descrito por Dean e Ghemawat, do Google, em um artigo de 2008. A ideia central: você divide o trabalho em duas fases. A fase de mapeamento, que transforma cada registro de entrada de forma independente, gerando pares de chave e valor. E a fase de redução, que agrupa e combina esses pares por chave, produzindo o resultado final. Entre as duas fases, existe uma etapa crucial chamada embaralhamento — o shuffle —, que redistribui os pares intermediários entre os nós responsáveis pela redução, agrupando tudo pela chave certa. *[indicação de edição: diagrama animado — dados de entrada se dividindo em tarefas de mapeamento, convergindo em um funil de embaralhamento, e saindo como resultado agregado]*

Frameworks modernos generalizaram essa ideia usando grafos acíclicos dirigidos — DAGs —, permitindo encadear várias etapas de transformação, não só um par map-reduce. Mas o princípio de tolerância a falhas permanece o mesmo: se um nó falha no meio de uma tarefa, o framework simplesmente reatribui essa tarefa a outro nó disponível e reexecuta a partir dos dados intermediários já salvos. Não é preciso reiniciar o job inteiro, nem alguém precisa intervir manualmente para uma falha pontual.

Pense em um grafo acíclico dirigido como uma receita de várias etapas, em que cada etapa depende do resultado da etapa anterior, mas etapas independentes entre si podem rodar em paralelo. Para o histórico de pedidos da NexaOrder, um DAG poderia, por exemplo, primeiro filtrar pedidos de um determinado período, depois agrupar por região, depois calcular o ticket médio por região, e finalmente gerar um relatório consolidado — cada etapa alimentando a próxima, com o framework decidindo automaticamente quais partes podem ser paralelizadas e quais precisam esperar dados de uma etapa anterior.

Pipelines de fluxo também particionam o trabalho — geralmente por uma chave, como o identificador do dispositivo, garantindo que todos os eventos daquele dispositivo específico sejam processados, em ordem, pela mesma partição. E aqui vale um cálculo rápido, no mesmo espírito da fórmula de capacidade que usamos lá na Aula 1 desta disciplina. *[indicação de edição: exibir o cálculo em tela]* Se o pipeline de fraude precisa processar um pico de 5 mil eventos por segundo, e cada consumidor de partição sustenta, comprovadamente, 750 eventos por segundo, o número mínimo de partições é 5 mil dividido por 750, arredondado para cima: aproximadamente 6,67, ou seja, 7 partições.

Tem mais um detalhe sutil, mas importante: a diferença entre tempo de evento e tempo de processamento. Tempo de evento é quando a tentativa de pagamento realmente aconteceu. Tempo de processamento é quando o pipeline efetivamente processa esse evento — que pode ser alguns segundos depois, ou, em caso de instabilidade de rede, minutos depois. Se você calcula, por exemplo, “quantas tentativas com o mesmo dispositivo em um minuto”, e um evento chega atrasado, ele pode acabar caindo na janela errada. A solução usada na prática se chama marca d’água — watermark —, combinada com uma tolerância configurável a atraso, que mantém a janela aberta um pouco mais antes de fechá-la de vez.

E já que estamos falando de janelas, vale diferenciar os tipos mais comuns. Uma janela “tumbling”, ou fixa, divide o tempo em blocos que não se sobrepõem — por exemplo, um bloco novo a cada minuto exato. Uma janela “sliding”, ou deslizante, se sobrepõe: você pode calcular “tentativas nos últimos cinco minutos”, recalculado a cada segundo, não só a cada cinco minutos. E uma janela de sessão agrupa eventos por proximidade temporal entre eles, encerrando a janela quando há um intervalo sem atividade — útil, por exemplo, para agrupar todas as tentativas de um mesmo dispositivo em uma única “sessão suspeita”, mesmo que ela dure trinta segundos ou cinco minutos, dependendo do comportamento observado. *[indicação de edição: três pequenos diagramas ilustrando janela fixa, deslizante e de sessão]*

Além do lote e do fluxo centralizados, temos duas outras opções relevantes. Funções como serviço — FaaS — permitem rodar um trecho de código em resposta a um evento, sem manter um servidor ligado o tempo todo. A plataforma aloca o ambiente na hora da chamada e cobra pelo tempo de execução, não pela capacidade ociosa. É ótimo para cargas esporádicas, como enviar um e-mail de confirmação de pedido. O custo está na inicialização a frio — o cold start —, quando não existe uma instância já “aquecida” e a plataforma precisa preparar um ambiente novo antes de processar, o que adiciona latência.

E computação de borda: processar dados próximo de onde eles são gerados, em vez de mandar tudo para uma região central de nuvem. Para a nossa detecção de fraude, isso poderia significar avaliar sinais simples — velocidade de digitação, padrões básicos do dispositivo — direto num ponto próximo ao cliente, ganhando latência ali. Mas isso tem custo: manter lógica em vários pontos de borda é operacionalmente mais complexo, e nem sempre mais barato — especialmente quando a decisão precisa de contexto histórico amplo, que só está disponível de forma centralizada. *[indicação de edição: mapa estilizado com pontos de borda distribuídos, cada um conectado de volta a uma região central]*

Repare que FaaS e computação de borda respondem a perguntas diferentes, mesmo que às vezes apareçam juntas na mesma conversa. FaaS é sobre como você executa código — sob demanda, sem servidor dedicado —, e pode rodar tanto em uma região central quanto em um ponto de borda. Computação de borda é sobre onde você executa esse código — fisicamente mais perto do usuário. Uma plataforma pode, inclusive, combinar as duas ideias: funções pequenas, sob demanda, rodando em pontos de borda geograficamente distribuídos, cada uma reagindo a eventos locais sem exigir um servidor dedicado naquele local.

### Demonstração, exemplo ou estudo de caso

Vamos comparar três alternativas reais para o nosso problema de fraude.

Alternativa um: pipeline em lote, rodando a cada hora. Latência de decisão: até uma hora. Já rejeitamos essa opção — tempo demais.

Alternativa dois: pipeline em fluxo, centralizado, particionado por dispositivo, como descrevemos. Latência de decisão: segundos. E, como o processamento é centralizado, o pipeline tem acesso fácil ao histórico completo do dispositivo, essencial para detectar padrões de múltiplas tentativas. Lembrando o cálculo de partições que fizemos: para um pico de 5 mil eventos por segundo, com consumidores de 750 eventos por segundo cada, são necessárias 7 partições — um número que a equipe pode validar com um teste de carga real do pipeline, no mesmo espírito dos testes que discutimos na aula anterior.

Alternativa três: uma combinação — triagem inicial rápida na borda, capturando sinais simples e óbvios, com avaliação mais profunda enviada para o pipeline de fluxo centralizado, que tem o contexto histórico completo.

A alternativa três tende a ser a mais equilibrada: ganha velocidade nos casos óbvios, sem abrir mão de contexto nos casos que exigem análise mais completa. Mas ela também é a mais complexa operacionalmente — duas lógicas de decisão, sincronizadas, precisam ser mantidas.

E vale trazer o custo para essa comparação, porque decisão de arquitetura raramente é só sobre desempenho técnico. O pipeline em lote é o mais barato de operar, mas já eliminamos por não atender ao requisito de negócio. O pipeline em fluxo centralizado tem um custo de operação contínuo — ele processa eventos o tempo todo, mesmo em horários de baixo movimento, ao contrário de um job em lote que só consome recursos quando roda. E a combinação com borda adiciona ainda mais custo de manutenção, porque a lógica simples da borda precisa ser atualizada e sincronizada em vários pontos distribuídos, sempre que o modelo de fraude evolui. Não existe alternativa gratuita aqui — existe a alternativa cujo custo, técnico e financeiro, melhor se justifica pelo valor que a decisão em segundos representa para o negócio.

### Aplicação profissional

Engenheiros de dados, engenheiros de machine learning e arquitetos de plataforma lidam, rotineiramente, com exatamente esse tipo de decisão: lote ou fluxo? Centralizado, borda, ou os dois? A resposta certa nunca é genérica — depende de até quando, especificamente, uma informação pode esperar antes de perder valor para o negócio. Saber fazer essa pergunta, e traduzir a resposta em arquitetura, é uma competência central para quem trabalha com dados em escala.

Esse mesmo raciocínio aparece em contextos muito diferentes da NexaOrder. Uma rede de sensores industriais processa leituras de temperatura na borda, para reagir a uma condição perigosa em milissegundos, mas envia os dados agregados para uma região central, onde um modelo mais sofisticado analisa tendências ao longo de meses. Um aplicativo de recomendação processa cliques em fluxo, para atualizar sugestões quase imediatamente, mas recalcula, em lote, o modelo completo de recomendação uma vez por dia, usando todo o histórico disponível. Em todos os casos, é a mesma pergunta orientando decisões de arquitetura completamente diferentes.

### Fechamento

Da proposta de rodar a cada hora até a arquitetura combinada de borda e fluxo centralizado, o que mudou não foi a tecnologia disponível — foi a pergunta certa sobre o que o negócio realmente precisa.

Recapitulando: lote atende análises que toleram espera, fluxo atende decisões em tempo quase real; MapReduce e seus sucessores em DAG organizam processamento distribuído com tolerância a falhas por reexecução de tarefas isoladas; tempo de evento e tempo de processamento podem divergir, e marcas d’água tratam eventos atrasados sem descartar o conceito de janela; e funções como serviço, junto com computação de borda, ampliam onde e como processar dados, cada uma com seus próprios compromissos de custo, latência e complexidade.

Na nossa última videoaula, vamos reunir tudo o que vimos nas quatro unidades desta disciplina para defender, de ponta a ponta, uma arquitetura completa da NexaOrder. *[indicação de edição: encerrar com a frase-chave em tela: “A pergunta não é qual tecnologia usar. É até quando a informação pode esperar.”]*

### Indicações de edição e recursos visuais

- Abertura: relógio acelerado com selo “tarde demais”.
- Comparação visual lote versus fluxo.
- Diagrama animado das fases do MapReduce.
- Cálculo de dimensionamento de partições exibido em tela.
- Mapa estilizado de pontos de borda conectados a uma região central.
- Encerramento com frase-chave em tela.

### Fontes e links de mídia

- DEAN, Jeffrey; GHEMAWAT, Sanjay. MapReduce: simplified data processing on large clusters. *Communications of the ACM*, v. 51, n. 1, p. 107-113, 2008. DOI: 10.1145/1327452.1327492 — referência primária do modelo MapReduce.
- Documentação pública de conceitos de processamento em fluxo (tempo de evento, janelas e marcas d’água) de um framework de streaming amplamente adotado, a ser referenciada de forma genérica em tela, sem reprodução de trecho específico.

## Videoaula 16 — “Da aplicação em um servidor à plataforma distribuída: encerrando a jornada da NexaOrder”

**Vínculo com o plano de aprendizagem:** Unidade 4, Aula 16 — Projeto integrado e avaliação arquitetural. Encerramento da disciplina.

**Objetivo da videoaula:** capacitar o estudante a integrar requisitos, decisões, riscos e evidências em uma avaliação arquitetural completa, e a reconhecer a trajetória de aprendizagem construída ao longo das quatro unidades da disciplina.

### Abertura contextualizada

A diretoria da NexaOrder convoca a equipe de engenharia para uma reunião. Não é uma reunião de status. É uma revisão formal, antes da aprovação do orçamento do próximo ciclo. A pergunta na mesa não é “o sistema funciona?” — isso todo mundo já sabe que sim. A pergunta é: “por que devemos confiar que essa arquitetura aguenta o crescimento que vocês estão prevendo, resiste às falhas mais prováveis, e vale o que custa?”. *[indicação de edição: sala de reunião estilizada, com a equipe técnica de um lado e a diretoria do outro, um projetor ao centro]*

Essa é a cena com que fechamos a disciplina inteira. E, hoje, vamos construir, juntos, a resposta.

### Desenvolvimento conceitual

Toda avaliação arquitetural séria começa separando dois tipos de requisito. Requisitos funcionais dizem o que o sistema precisa fazer: “o cliente consegue finalizar uma compra”, “o estoque é reservado antes da confirmação do pagamento”. Atributos de qualidade dizem como o sistema precisa se comportar: desempenho, disponibilidade, segurança, capacidade de manutenção, custo.

Esses dois tipos entram em tensão o tempo todo, e uma avaliação madura não escolhe um lado de forma absoluta — ela resolve a tensão de forma explícita, por contexto. No catálogo da NexaOrder, uma leitura levemente desatualizada é aceitável, então vale priorizar latência mínima. Na hora da reserva de estoque, durante o checkout, uma divergência tem custo direto — cobrar duas pessoas pelo último item —, então vale priorizar consistência mais forte, mesmo que isso custe alguns milissegundos a mais.

E os atributos de qualidade não param em desempenho e disponibilidade. Segurança e observabilidade, os temas centrais desta unidade e da unidade anterior, também são atributos de qualidade — e o momento certo de tratá-los não é depois que o sistema já está em produção. Um novo serviço que nasce sem identidade própria, sem comunicação autenticada, ou sem instrumentação de telemetria, carrega uma dívida técnica que só fica mais cara de pagar com o tempo. A pergunta que uma banca de revisão arquitetural deveria sempre fazer não é apenas “o sistema funciona?”, mas “quando um novo componente for adicionado daqui a seis meses, ele já nasce seguro e observável, ou isso vai depender de alguém lembrar de adicionar depois?”.

Vamos revisitar uma fórmula que você viu lá na primeira aula desta disciplina — a estimativa de número de instâncias necessárias para um pico de tráfego. *[indicação de edição: reexibir a fórmula da Aula 1, em tela, ao lado da versão “atualizada” com dados reais]* Na época, ela dependia de estimativas. Agora, depois de tudo o que vimos nesta unidade — testes de carga reais, métricas históricas reais coletadas por instrumentação —, os insumos dessa mesma fórmula deixaram de ser suposições. Isso é o que significa amadurecer uma arquitetura: não trocar a fórmula, mas alimentá-la com evidência real, em vez de palpite.

Toda decisão significativa, ao longo do caminho, merece um registro — um ADR, um registro de decisão arquitetural. Não basta anotar “decidimos usar Kubernetes”. Um ADR completo explica o contexto que motivou a decisão, as alternativas que foram consideradas, e as consequências que a equipe aceitou conscientemente. Reunidos, os ADRs da NexaOrder contam a história de cada escolha: instâncias sem estado atrás de um balanceador, na Unidade 1; o modelo de consistência escolhido para estoque e catálogo, na Unidade 2; a decomposição em serviços e a arquitetura orientada a eventos, na Unidade 3; a estratégia de observabilidade e a política de testes de resiliência, nesta Unidade 4.

Um bom ADR não precisa ser longo. Ele pode caber em uma página: um título curto, uma seção de contexto explicando qual problema motivou a decisão, uma seção listando as alternativas avaliadas — mesmo as que foram descartadas —, a decisão em si, e as consequências esperadas, positivas e negativas. O valor de um ADR não está no tamanho, está em existir e em ser lido meses depois, quando alguém questiona “por que fizemos assim?” e a resposta não depende da memória de ninguém.

Junto aos ADRs, vem a análise de pontos únicos de falha. E aqui mora uma armadilha comum: réplicas distribuídas em várias zonas não eliminam, sozinhas, todos os pontos únicos de falha, se todas dependerem de um componente não replicado — por exemplo, uma única instância do sistema de mensageria, sem réplica, usada por todas as réplicas do serviço de pagamento. *[indicação de edição: diagrama mostrando três réplicas “saudáveis” do serviço de pagamento, todas conectadas a um único ícone de mensageria sem redundância, destacado em vermelho]*

Para recuperação, dois números orientam tudo: RPO, o objetivo de ponto de recuperação — quanto dado o negócio aceita perder — e RTO, o objetivo de tempo de recuperação — quanto tempo o negócio aceita ficar fora do ar. Se a NexaOrder replica o banco de pedidos a cada cinco minutos para uma região secundária, e consegue promover essa região e restabelecer o serviço em até quinze minutos, o RPO é de cerca de cinco minutos, e o RTO, de cerca de quinze minutos. Esses números não são escolhidos por conveniência técnica — eles vêm de uma conversa com o negócio sobre o que é tolerável.

E, por fim, custo e evolução. Uma arquitetura não fica ótima para sempre. Um exemplo prático: capacidade dimensionada para o pico de tráfego, mas mantida constante mesmo de madrugada, quando quase ninguém está comprando, custa dinheiro sem entregar benefício nenhum naquele horário. A resposta não é eliminar a redundância necessária para o pico — é fazer essa capacidade se ajustar automaticamente à demanda observada.

Isso conecta diretamente com o que vimos na Aula 15: capacidade e custo não são decisões estáticas, tomadas uma vez e esquecidas. Elas evoluem junto com o negócio, e a mesma disciplina de observar dados reais, formular hipóteses e validar com evidência — que usamos para diagnosticar latência, para testar resiliência, e para dimensionar pipelines de processamento — se aplica também à revisão contínua de custo. Uma arquitetura madura não é a que acerta tudo de primeira; é a que tem os mecanismos certos para perceber quando algo deixou de fazer sentido, e para corrigir o rumo sem drama.

E, para fechar o raciocínio sobre redundância, vale um último número. *[indicação de edição: exibir o cálculo em tela]* Se uma única instância de um serviço crítico tem 99,5% de disponibilidade, e você coloca três réplicas independentes atrás de um balanceador — réplicas que só falham juntas se todas falharem ao mesmo tempo —, a disponibilidade combinada é 1 menos 0,005 elevado ao cubo. Isso dá, aproximadamente, 99,9999875% — muito próximo de sete “noves”. Compare isso com o que vimos na aula passada, sobre uma cadeia sequencial de quatro serviços de 99,9% cada, que resultava em apenas 99,6% combinados. A diferença não está no número de componentes — está em como eles dependem uns dos outros: em série, o risco se acumula; em paralelo e independente, ele se dilui.

Essa conta também explica por que o dimensionamento de capacidade não pode ser separado da análise de resiliência. Não adianta ter réplicas suficientes para o pico de tráfego se elas compartilham uma única dependência de rede, um único banco de dados sem réplica, ou um único provedor externo sem plano de contingência. A avaliação arquitetural madura olha para capacidade e para resiliência como duas faces da mesma pergunta: quantas réplicas independentes, de fato independentes, sustentam o nível de disponibilidade que o negócio exige?

### Demonstração, estudo de caso e aplicação profissional

Voltando à sala de reunião com a diretoria: a equipe da NexaOrder não chega com uma afirmação vaga de que “o sistema é robusto”. Chega com requisitos explícitos, com um ADR pronto para qualquer decisão questionada, com uma análise de pontos únicos de falha que já identificou e corrigiu a dependência não replicada da mensageria, com RPO e RTO definidos a partir de conversa real com o negócio, e com um plano de custo que ajusta capacidade à demanda observada, sem desperdício.

Essa é, literalmente, a competência que separa um profissional júnior de um profissional sênior em arquitetura de sistemas distribuídos: não é saber mais tecnologias — é saber justificar cada decisão com requisito, compromisso e evidência, diante de qualquer audiência, técnica ou não.

E essa habilidade se transfere para além da NexaOrder. Se você participar, no futuro, de uma auditoria de segurança, de uma diligência técnica antes de um investimento, ou simplesmente de uma reunião de arquitetura com colegas mais experientes, o roteiro é o mesmo: requisito, decisão registrada, risco identificado, e evidência de que a decisão funciona na prática, não apenas na teoria. Quem consegue apresentar essa sequência, de forma clara e honesta sobre as limitações do sistema, ganha credibilidade técnica muito mais rápido do que quem apenas lista tecnologias no currículo.

### Fechamento — encerrando a disciplina

E aqui chegamos ao final. Não só desta aula, mas da disciplina inteira. Vale parar um segundo para olhar para trás. *[indicação de edição: montagem rápida recapitulando, em poucos segundos cada, os principais diagramas usados nas Unidades 1, 2, 3 e 4]*

A NexaOrder começou, na Aula 1, como uma aplicação simples, instalada em um único servidor, onde duas pessoas conseguiam comprar o último item disponível ao mesmo tempo, sem que ninguém soubesse explicar exatamente por quê. Dezesseis aulas depois, ela virou uma plataforma distribuída de verdade: serviços com limites claros, comunicação assíncrona e orientada a eventos, replicação e consenso sustentando os dados, orquestração automatizada mantendo tudo no ar, segurança de ponta a ponta entre cada chamada, observabilidade contínua permitindo enxergar o que está acontecendo, e testes de resiliência deliberados garantindo que os mecanismos de proteção realmente funcionam quando precisam funcionar.

Pense em cada unidade como uma camada adicionada sobre a anterior, nunca substituindo o que veio antes. Os fundamentos da Unidade 1 — comunicação, tempo, falhas parciais — continuam presentes em todo o resto: são eles que explicam por que a replicação da Unidade 2 precisa de modelos de consistência explícitos, por que a decomposição em serviços da Unidade 3 precisa de contratos e comunicação segura, e por que a observabilidade e os testes desta Unidade 4 são indispensáveis, não opcionais. Nenhuma camada torna a anterior desnecessária — cada uma depende do que foi construído antes dela.

Isso não é uma trajetória especial, exclusiva de um caso fictício de sala de aula. É, com variações, a trajetória real de praticamente qualquer sistema que cresce de verdade. E o que sustenta essa trajetória não é nenhuma tecnologia específica — é uma forma de pensar: tratar cada decisão arquitetural como uma hipótese que pode, e deve, ser verificada, medida, e ajustada, em vez de um dogma definido uma vez e nunca mais questionado.

Se você chegou até aqui, você não aprendeu apenas conceitos isolados de sistemas distribuídos. Você aprendeu a fazer, sistematicamente, a pergunta que sustenta toda essa disciplina: “o que acontece se isso falhar?” — e a construir, a partir dessa pergunta, sistemas mais honestos sobre suas próprias limitações, e por isso mesmo, mais confiáveis. Essa competência não expira com a próxima tecnologia da moda. Ela é o que forma, de fato, um engenheiro ou engenheira de sistemas distribuídos.

Foi uma jornada longa, ao lado da NexaOrder. Obrigado por tê-la percorrido até aqui. E boa sorte — com seus próprios sistemas, e com as falhas que, mais cedo ou mais tarde, eles também vão enfrentar. *[indicação de edição: encerrar com a frase-chave em tela, permanecendo por mais tempo que nas aulas anteriores: “Todo sistema falha. A engenharia está em decidir, com evidência, como.” Seguido dos créditos finais da disciplina.]*

### Indicações de edição e recursos visuais

- Abertura: sala de reunião estilizada, equipe técnica e diretoria.
- Reexibição da fórmula de capacidade da Aula 1 ao lado da versão alimentada por dados reais.
- Diagrama de ponto único de falha oculto na mensageria não replicada.
- Cálculo de disponibilidade combinada com três réplicas independentes.
- Montagem de recapitulação das quatro unidades.
- Encerramento estendido com frase-chave e créditos finais da disciplina.

### Fontes e links de mídia

- LAMPSON, Butler W. Hints for computer system design. In: ACM SYMPOSIUM ON OPERATING SYSTEMS PRINCIPLES, 9., 1983, Bretton Woods. *Proceedings [...]*. New York: ACM, 1983. DOI: 10.1145/800217.806614 — referência conceitual para a discussão de decisões e registros arquiteturais.
- O’REILLY, Tim et al. *Site Reliability Engineering*. Sebastopol: O’Reilly Media, 2016 — referência conceitual para RPO, RTO e custo de operação.
