# Roteiros das videoaulas 1 a 4 — Unidade 1 (20 minutos)

Disciplina: Distributed Systems Engineering
Professor-conteudista: Afonso Cesar Lelis Brandão
Unidade 1: Fundamentos, comunicação, tempo e falhas
Duração-alvo de cada videoaula: 20 minutos.
Narração prevista: aproximadamente 2.200 a 2.700 palavras faladas por videoaula, sem contar títulos, marcações de tempo, indicações de edição e fontes.
Ritmo de referência: 115 a 130 palavras por minuto, já considerando pausas, respiração e construção progressiva dos recursos visuais.

Cada roteiro acompanha, slide a slide, o deck HTML da aula correspondente em `unidade_1/slides/`. As marcações entre colchetes duplos indicam o intervalo de tempo e o slide que deve estar na tela naquele momento. O avanço de slide é o principal marcador de edição: quando a marcação muda, o slide muda.

Plano de tempo de referência, adaptável ao ritmo de cada aula:

- 00:00–01:45 — capa, audiodescrição e sumário;
- 01:45–04:00 — objetivos de aprendizagem e situação-problema;
- 04:00–13:00 — desenvolvimento conceitual;
- 13:00–16:00 — demonstração, exemplos numéricos e estudo de caso;
- 16:00–18:00 — aplicação profissional e pausa para reflexão;
- 18:00–20:00 — pontos-chave, atividade prática e fechamento.

Os quatro roteiros a seguir correspondem às Aulas 1 a 4 da Unidade 1, tendo a NexaOrder como fio condutor prático. Cada roteiro é um texto de narração pronto para gravação, e não notas de aula. O registro é o de exposição didática contínua, próximo ao de um livro-texto lido em voz alta: frases completas, encadeamento explícito entre as ideias e ausência de recursos de oralidade informal.

---

## Roteiro da Videoaula 1 — “Seu sistema cresceu; por que ele ficou menos previsível?”

**Vínculo com o plano de aprendizagem:** Unidade 1, Aula 1 — Pensar distribuído: conceitos, propriedades e compromissos.

**Deck de apoio:** `unidade_1/slides/aula1.html` — 23 slides (capa, audiodescrição, sumário, 19 de conteúdo e encerramento).

**Objetivo da videoaula:** ao final, o estudante deve ser capaz de caracterizar um sistema distribuído, justificar a decisão de distribuir a partir de um requisito concreto, estimar capacidade e disponibilidade com fórmulas simples e reconhecer concorrência, ausência de estado global e falha parcial como propriedades inerentes da distribuição.

**Mapa de tempo e slides:** 00:00 capa · 00:25 audiodescrição · 00:55 sumário · 01:40 objetivos · 02:25 situação-problema · 04:00 definição · 05:30 os quatro serviços · 06:30 por que distribuir · 07:45 escala vertical e horizontal · 09:00 exemplo numérico de instâncias · 10:40 disponibilidade · 12:20 geografia e autonomia · 13:20 citação · 13:40 propriedades · 15:00 silêncio ambíguo · 16:00 transparência · 16:50 métricas · 17:50 estilos arquiteturais · 18:20 decisão arquitetural · 18:50 pausa para reflexão · 19:20 pontos-chave e atividade · 19:40 encerramento.

### Abertura contextualizada

**[00:00–00:25 · Slide 0 — Capa]**

Esta é a primeira aula da disciplina de Engenharia de Sistemas Distribuídos. Eu sou o professor Afonso Brandão. Nesta videoaula construímos o vocabulário que sustenta toda a disciplina: o que caracteriza um sistema distribuído, por que uma equipe decide distribuir um sistema e o que essa decisão cobra em troca.

**[00:25–00:55 · Slide 1 — Audiodescrição]**

Antes de começar, a audiodescrição desta aula. Os slides usam fundo azul-marinho com molduras de triângulos em amarelo, verde e ciano, e o conteúdo aparece em cartões claros. Ao longo da aula surgem cinco recursos visuais: um diagrama de arquitetura, uma fórmula de dimensionamento, uma tabela de disponibilidade, uma linha do tempo de falha e um quadro de decisão arquitetural. Descrevo cada um deles, em voz alta, no momento em que aparecerem.

**[00:55–01:40 · Slide 2 — Sumário]**

Este é o percurso da aula. Começo pelo que caracteriza um sistema distribuído e por que alguém decide distribuir. Em seguida saio da intuição e vou para o dimensionamento, com duas contas simples que transformam achismo em hipótese verificável. Depois apresento as propriedades que mudam o seu raciocínio de projeto, discuto por que transparência é ótima para o usuário e perigosa para o engenheiro, separo quatro métricas que costumam ser confundidas e fecho com um modelo de decisão arquitetural que você vai usar do começo ao fim da disciplina.

**[01:40–02:25 · Slide 3 — Objetivos de aprendizagem]**

Combinando o resultado: ao final desta aula, você deve conseguir caracterizar um sistema distribuído a partir de quatro palavras — pluralidade, autonomia, comunicação e coordenação. Deve justificar uma decisão de distribuição a partir de um requisito concreto, e não de tendência tecnológica. Deve estimar capacidade e disponibilidade com fórmulas simples. Deve distinguir latência, throughput, disponibilidade e confiabilidade. Deve reconhecer concorrência, ausência de estado global e falhas parciais como propriedades inerentes, não como defeitos de programação. E deve registrar uma decisão arquitetural explicitando benefício, custo e evidência.

**[02:25–04:00 · Slide 4 — Situação-problema]**

A disciplina inteira será atravessada por uma mesma história: a da NexaOrder, uma plataforma fictícia de pedidos, pagamentos e expedição.

A NexaOrder nasceu em um único servidor. Interface, regras de negócio e banco de dados dividiam o mesmo ambiente. Funcionava bem. Aí as vendas cresceram, e a equipe fez o que parecia óbvio: separou o sistema em pedaços — catálogo, estoque, pagamento, expedição — e colocou cada pedaço para rodar em várias instâncias, em várias máquinas.

A capacidade de atendimento realmente aumentou. Mas apareceram comportamentos que ninguém tinha visto antes. Dois clientes conseguiram comprar o último item do estoque, ao mesmo tempo. Uma cobrança foi processada mesmo depois de a tela mostrar erro. E o painel de operações exibiu, para o mesmo pedido, dois estados diferentes simultaneamente.

Nenhum desses três incidentes veio de programação descuidada, e nenhum deles se resolve revisando linha de código. São propriedades da distribuição. Enquanto forem tratados como defeito de implementação, a investigação continuará procurando um culpado que não existe.

### Desenvolvimento conceitual

**[04:00–05:30 · Slide 5 — O que é um sistema distribuído?]**

Um sistema distribuído é um conjunto de componentes computacionais autônomos que se comunicam por rede e coordenam suas ações para entregar um objetivo comum. E, por definição, não existe ali nem memória global instantânea, nem relógio perfeito acessível a todos.

Quatro palavras dessa definição acompanham a disciplina inteira. Pluralidade: há mais de um processo, contêiner, máquina ou nó participante. Autonomia: cada participante executa e pode falhar de forma independente dos outros — o estoque pode cair sem que o pagamento caia junto. Comunicação: a cooperação acontece por mensagens transmitidas pela rede, não por memória compartilhada instantânea. E coordenação: o resultado final depende de como essas ações se combinam.

Um cuidado importante, porque é um erro comum: o determinante não é a distância física. É a separação entre participantes com comunicação não instantânea. Um sistema é distribuído mesmo com todos os nós no mesmo datacenter. E várias funções chamando umas às outras dentro do mesmo processo não formam, por si só, um sistema distribuído.

**[05:30–06:30 · Slide 6 — Uma operação para o cliente, quatro serviços para a arquitetura]**

Essa definição se concretiza na NexaOrder.

*[indicação de edição: inserir Recurso visual 1 da Aula 1 — diagrama da NexaOrder com cliente, gateway, pedidos, estoque, pagamento e expedição, construído componente a componente conforme a narração]*

Para quem compra, existe um único botão: comprar. Para a arquitetura, existe uma sequência de mensagens, estados intermediários e pontos de falha independentes.

Pedidos registra a intenção do cliente e coordena o restante do fluxo. Estoque reserva a unidade e responde se a reserva foi possível. Pagamento solicita autorização a um provedor que está fora da NexaOrder — ou seja, fora do seu controle. E expedição prepara o envio depois que os passos anteriores convergem. O verbo convergir é deliberado: o resultado não aparece pronto de uma vez, ele se forma ao longo de uma sequência de etapas.

**[06:30–07:45 · Slide 7 — Por que distribuir?]**

Se distribuir cria problemas, por que fazer isso? Porque distribuir não é um objetivo em si — é uma resposta a requisitos que uma arquitetura centralizada não atende de forma satisfatória.

São seis requisitos típicos. Escalabilidade: sustentar crescimento de carga sem degradação incompatível com os objetivos do serviço. Disponibilidade: manter o serviço acessível quando um componente falha. Proximidade geográfica: reduzir latência e atender exigências de residência de dados. Autonomia organizacional: permitir que equipes evoluam partes do produto em ritmos diferentes. Integração entre organizações: cooperar com sistemas que simplesmente não estão sob o seu controle, como o provedor de pagamento da NexaOrder. E uso eficiente de recursos: dimensionar cada capacidade conforme a demanda que ela de fato recebe, em vez de crescer o sistema inteiro por causa de uma parte.

Se você não consegue apontar qual desses requisitos está resolvendo, ainda não tem motivo para distribuir.

**[07:45–09:00 · Slide 8 — Escala vertical e escala horizontal]**

Falando em escalabilidade: existem dois caminhos, e eles não são equivalentes.

Escala vertical é aumentar CPU, memória ou armazenamento de uma máquina. É operacionalmente simples: basta trocar o tamanho da instância e reiniciar. Escala horizontal é aumentar o número de instâncias que dividem o trabalho, ampliando capacidade por paralelismo.

Cada caminho tem seu limite. O limite da vertical é físico e econômico: sempre existe uma máquina maior, até o momento em que não existe mais — e, bem antes disso, o preço deixa de fazer sentido. O preço da horizontal é outro: você passa a ter que distribuir requisições, lidar com concorrência, replicar dados e coordenar participantes.

E tem um detalhe que derruba muita estimativa otimista: a relação raramente é linear. Dobrar o número de instâncias raramente dobra a capacidade, porque o banco pode virar gargalo e o próprio balanceamento tem custo. E parte da carga simplesmente não paraleliza: os trechos que exigem coordenação limitam o ganho total.

**[09:00–10:40 · Slide 9 — Exemplo numérico: quantas instâncias sustentam o pico?]**

Essa discussão fica mais precisa quando se transforma em conta. Estimar antes de escalar é o que separa uma decisão intuitiva de uma hipótese verificável.

*[indicação de edição: inserir Recurso visual 2 da Aula 1 — fórmula do número mínimo de instâncias, com cada variável destacada conforme a narração]*

O número mínimo de instâncias é o teto da divisão entre a taxa de chegada no pico e o produto da capacidade medida de uma instância pela utilização-alvo. Em símbolos: N é igual ao teto de lambda-pico dividido por capacidade vezes utilização-alvo.

Os números da NexaOrder são os seguintes. A taxa de chegada no pico é de 800 requisições por segundo. Cada instância aguenta, medida em teste, 200 requisições por segundo. E a utilização-alvo é de 70%. A conta fica: 800 dividido por 200 vezes 0,7, ou seja, 800 dividido por 140. Isso dá 5,71. Como não existe meia instância, arredondamos para cima: seis instâncias.

Convém observar o que uma estimativa ingênua produziria. Dividir 800 por 200 dá 4, e quatro instâncias parecem suficientes. O problema é que isso significa operar a 100% da capacidade o tempo todo, sem nenhuma folga. A utilização-alvo de 70% existe justamente para que o serviço não opere continuamente no limite: um pico inesperado, uma instância que reinicia, uma consulta mais pesada que o normal — qualquer um desses eventos satura o serviço e faz as filas e a latência explodirem.

E a ressalva mais importante: essa conta não substitui teste de carga. Ela indica onde começar a medir.

**[10:40–12:20 · Slide 10 — Disponibilidade: o preço de cada nove]**

A segunda conta é sobre disponibilidade. Disponibilidade é a proporção de tempo em que o serviço cumpre a sua função: tempo operacional dividido pelo tempo total observado.

*[indicação de edição: inserir Recurso visual 3 da Aula 1 — tabela de disponibilidade, revelando uma linha por vez conforme a narração]*

Cada nove adicional tem um significado preciso em uma janela de 30 dias. Com 99%, são cerca de 7 horas e 12 minutos de indisponibilidade por mês, e isso exige redundância básica com recuperação manual. Com 99,9%, cai para cerca de 43 minutos, e já exige múltiplas instâncias com desvio automático de tráfego. Com 99,99%, são cerca de 4 minutos e 19 segundos, o que exige zonas independentes, automação e ensaio recorrente de falhas. E com 99,999%, sobram 26 segundos no mês inteiro — um investimento raramente justificável fora de domínios críticos.

O padrão é o seguinte: cada nove adicional não custa um pouco mais. Custa redundância, automação e recuperação em outro patamar.

Há ainda uma armadilha frequente: redundância só protege se as instâncias não compartilharem o mesmo ponto de falha. Duas instâncias no mesmo host não protegem contra a queda desse host; duas zonas alimentadas pelo mesmo banco não protegem contra a falha desse banco. Redundância no diagrama não é redundância na prática.

**[12:20–13:20 · Slide 11 — Geografia e autonomia organizacional]**

Os outros dois requisitos merecem uma passagem rápida, porque voltam nas próximas unidades.

Proximidade reduz latência: posicionar recursos perto do usuário encurta o caminho da rede, e isso é física, não configuração. Residência de dados: algumas informações precisam permanecer em uma jurisdição específica, por exigência legal. A cópia, porém, tem preço — é preciso decidir quando uma atualização feita em uma região se torna visível nas demais, e o que acontece durante uma interrupção de comunicação entre regiões, porque essa interrupção ocorrerá em algum momento.

Do lado organizacional, serviços separados permitem que equipes evoluam partes do produto de forma independente. Há, contudo, um sintoma clássico a observar: se toda mudança exige coordenação simultânea de várias equipes, o que existe é distribuição técnica sem autonomia real. Isso tem nome — monólito distribuído — e a Unidade 3 volta a esse ponto com detalhe.

**[13:20–13:40 · Slide 12 — Citação]**

Esta frase resume o argumento da aula: distribuir não é um objetivo isolado; é uma resposta a requisitos que uma arquitetura centralizada não atende de forma satisfatória.

### Demonstração, exemplo ou estudo de caso

**[13:40–15:00 · Slide 13 — Propriedades que mudam o raciocínio]**

A distribuição faz surgir quatro propriedades que alteram o raciocínio de projeto, e não apenas a implementação.

Concorrência: componentes trabalham ao mesmo tempo e disputam recursos. Não basta a operação estar correta isoladamente; é preciso analisar quais ordens de execução podem acontecer. Foi isso que permitiu dois clientes comprarem o último item.

Ausência de estado global instantâneo: cada componente só vê o que já chegou até ele. A consequência é contraintuitiva — duas visões diferentes podem estar, cada uma, coerentes com as observações locais de quem as tem. Foi isso que colocou dois estados no painel.

Falhas parciais: um componente pode falhar enquanto outro continua funcionando. A dificuldade está no sintoma: mensagem atrasada e serviço parado produzem exatamente a mesma manifestação, que é o silêncio.

Heterogeneidade: linguagens, bancos, protocolos e versões convivem. Contratos e compatibilidade passam a fazer parte do sistema.

E uma consequência de projeto: divergência não é sinônimo de erro. O projeto define quais estados podem divergir, por quanto tempo e com qual mecanismo de convergência.

**[15:00–16:00 · Slide 14 — O silêncio ambíguo]**

O incidente do pagamento ilustra essas propriedades com particular clareza.

*[indicação de edição: inserir Recurso visual 4 da Aula 1 — linha do tempo da falha ambígua, com o cliente vendo “erro” de um lado e o log interno mostrando “pagamento aprovado” do outro, ligados por uma seta “resposta perdida”]*

Depois de um timeout na autorização de pagamento, a NexaOrder não sabe o que aconteceu do outro lado. Cinco hipóteses distintas produzem exatamente o mesmo sintoma. Primeira: a requisição não chegou ao provedor. Segunda: chegou, mas ainda não foi processada. Terceira: foi processada e a resposta se perdeu na volta. Quarta: continua em execução neste exato momento. Quinta: falhou antes de produzir qualquer efeito.

Cinco leituras, um único sintoma. E as consequências são opostas: repetir sem proteção pode gerar cobrança duplicada; desistir de imediato pode abandonar uma compra válida. A saída não está em ajustar o timeout — está em desenho: idempotência, identificação de operações, consulta de estado e reconciliação. Tudo isso são temas das próximas aulas.

**[16:00–16:50 · Slide 15 — Transparência]**

Há um conceito que costuma ser mal compreendido: transparência. Esconder localização, replicação e migração melhora a experiência de quem usa o sistema, e nisso reside seu valor. O problema é esconder a rede do raciocínio interno do engenheiro, pois o projeto passa a tratar a chamada remota como se fosse local. E ela nunca é.

Uma chamada remota tem latência maior e variável. Pode falhar sem que o destino tenha falhado. Pode produzir efeito sem retornar confirmação — que é exatamente o caso da cobrança da NexaOrder. Depende de serialização dos dados que trafegam. Atravessa limites de segurança e de organização. E pode ser repetida, o que exige compatibilidade de contrato.

### Aplicação profissional

**[16:50–17:50 · Slide 16 — Quatro métricas que não devem ser confundidas]**

Na prática profissional, boa parte das discussões improdutivas vem de confundir quatro métricas, que convém separar com cuidado.

Latência é o tempo para concluir uma operação. Médias, aqui, escondem os casos ruins. Afirmar que o p95 é de 300 milissegundos significa que 5% das observações demoraram mais do que isso — e são justamente essas que geram reclamação.

Throughput é trabalho concluído por unidade de tempo, como pedidos por segundo. Disponibilidade é a capacidade de atender, observando-se que um endpoint pode responder normalmente e ainda assim estar funcionalmente indisponível, devolvendo erro para toda requisição. Confiabilidade é produzir resultados corretos de forma sustentada. Responder rápido e duplicar cobranças não é confiabilidade.

E a relação entre elas: aumentar concorrência eleva o throughput até que algum recurso sature. Depois desse joelho da curva, as filas crescem e a latência sobe de forma abrupta. Por isso desempenho e correção precisam ser avaliados juntos.

**[17:50–18:20 · Slide 17 — Estilos arquiteturais iniciais]**

Um panorama dos principais estilos. Cliente-servidor: um servidor concentra capacidade e disponibilidade. Em camadas — apresentação, aplicação, domínio e dados: separar cada camada por rede acrescenta latência e novos modos de falha. Peer-to-peer: participantes atuam como cliente e servidor, e descoberta, confiança e consistência ficam mais difíceis. E serviços: capacidades de negócio expostas por contratos, que sem coesão e sem baixo acoplamento viram monólito distribuído.

A observação que interessa reter é esta: camadas ajudam a separar interesses, mas não exigem distribuição física. Distribuir uma camada precisa ser decisão justificada, não consequência automática do desenho.

**[18:20–18:50 · Slide 18 — Decisão arquitetural]**

É assim que qualquer decisão desta disciplina deve ser registrada. Uma decisão madura não afirma apenas que “microsserviços escalam” ou que “a nuvem garante disponibilidade”. Ela encadeia quatro elementos.

Requisito: processar 800 pedidos por segundo no pico. Decisão: manter múltiplas instâncias sem estado atrás de um balanceador. Compromisso: sessões locais deixam de ser confiáveis e o banco pode virar gargalo. Evidência: teste de carga com p95 abaixo do objetivo e falha controlada de uma instância.

Requisito, decisão, compromisso, evidência. Se faltar qualquer um dos quatro, o que existe é opinião, não decisão.

**[18:50–19:20 · Slide 19 — Pausa para reflexão]**

Pause o vídeo e examine o cenário a seguir. Um sistema interno é usado por 30 funcionários, processa poucas solicitações, opera em horário comercial e tolera alguns minutos de indisponibilidade. A equipe propõe dividi-lo em 20 microsserviços.

Quatro perguntas orientam a análise: quais requisitos justificariam essa distribuição? Quais custos operacionais seriam introduzidos? Que alternativa intermediária preservaria modularidade sem multiplicar falhas de rede? Quais métricas deveriam ser coletadas antes de decidir?

*[indicação de edição: inserir pausa com contagem regressiva de 10 segundos e o texto “Pense e continue”]*

A resposta tecnicamente mais madura, nesse cenário, provavelmente é um monólito modular. Engenharia de sistemas distribuídos também consiste em reconhecer quando não distribuir.

### Fechamento

**[19:20–19:40 · Slides 20 e 21 — Pontos-chave e atividade prática]**

Recapitulando os seis pontos-chave. Um sistema distribuído é feito de componentes autônomos que coordenam ações por mensagens, sem memória global instantânea nem relógio perfeito. Distribuir responde a requisito, não a moda. Concorrência, ausência de estado global e falhas parciais mudam o raciocínio de projeto. Latência, throughput, disponibilidade e confiabilidade medem dimensões diferentes. A rede não some: chamada remota nunca é chamada local. E toda decisão arquitetural registra requisito, mecanismo, compromisso e evidência.

Sua atividade prática é elaborar um registro de decisão arquitetural de uma página para a NexaOrder: selecione um requisito, descreva o estado atual, proponha uma decisão de distribuição, liste três benefícios e três custos, defina duas métricas com um experimento de validação e represente a solução em um diagrama simples.

**[19:40–20:00 · Slide 22 — Encerramento]**

Esta aula se encerra com três resultados: reconhecer o que caracteriza um sistema distribuído, justificar a distribuição a partir de um requisito e identificar os compromissos que ela introduz. A próxima aula trata da comunicação entre processos — como a NexaOrder troca mensagens entre pedidos, estoque, pagamento e expedição, comparando chamadas síncronas, RPC e mensageria. Bons estudos.

### Indicações de edição e recursos visuais

- Slide 0 — capa da Aula 1, com vinheta de abertura (00:00–00:25).
- Slide 1 — audiodescrição narrada integralmente (00:25–00:55).
- Slide 4 — situação-problema; sugere-se destacar os três incidentes um a um (02:25–04:00).
- Recurso visual 1 — diagrama da NexaOrder, construído componente a componente (aproximadamente 05:40).
- Recurso visual 2 — fórmula do número de instâncias, com variáveis surgindo em sincronia com o cálculo (aproximadamente 09:10).
- Recurso visual 3 — tabela de disponibilidade, revelada linha a linha (aproximadamente 10:50).
- Slide 12 — citação em tela cheia, com 3 segundos de silêncio antes da leitura (13:20).
- Recurso visual 4 — linha do tempo da falha ambígua, em tela dividida cliente/log interno (aproximadamente 15:10).
- Slide 19 — pausa de reflexão com contagem regressiva de 10 segundos (aproximadamente 19:00).
- Slide 22 — vinheta de encerramento e chamada para a próxima aula (últimos 15 segundos).

### Fontes e links de mídia

- COULOURIS, George et al. *Distributed Systems: Concepts and Design*. 5. ed. Boston: Addison-Wesley, 2011 — referência conceitual, sem reprodução de trecho externo.
- TANENBAUM, Andrew S.; VAN STEEN, Maarten. *Distributed Systems*. 4. ed. [S. l.]: Maarten van Steen, 2023 — referência conceitual, sem reprodução de trecho externo.
- Nenhuma mídia de terceiros é incorporada; diagramas, fórmulas e animações devem ser produzidos originalmente pela equipe de edição a partir do texto-base da Aula 1 (`unidade_1.md`) e do deck `unidade_1/slides/aula1.html`.

---

## Roteiro da Videoaula 2 — “Esperar ou seguir em frente? O dilema da comunicação distribuída”

**Vínculo com o plano de aprendizagem:** Unidade 1, Aula 2 — Comunicação entre processos: APIs, RPC e mensageria.

**Deck de apoio:** `unidade_1/slides/aula2.html` — 21 slides (capa, audiodescrição, sumário, 17 de conteúdo e encerramento).

**Objetivo da videoaula:** ao final, o estudante deve ser capaz de decidir entre comunicação síncrona e assíncrona a partir do contrato entre serviços, modelar APIs orientadas a recursos, evoluir esquemas sem quebrar consumidores, distinguir fila de publicação-assinatura e evento de comando, dimensionar retentativas com backoff e jitter e tornar operações repetíveis com idempotência e correlação.

**Mapa de tempo e slides:** 00:00 capa · 00:25 audiodescrição · 00:55 sumário · 01:40 objetivos · 02:20 situação-problema · 04:00 síncrono e assíncrono · 05:30 exemplo numérico do encadeamento · 07:10 HTTP e recursos · 08:40 RPC · 10:00 serialização e esquema · 11:20 citação · 11:40 fila e pub-sub · 12:50 evento e comando · 14:00 timeout, retry, backoff · 15:20 exemplo numérico do backoff · 16:50 idempotência · 18:00 correlação · 18:40 comparação dos dois fluxos · 19:15 pontos-chave e atividade · 19:40 encerramento.

### Abertura contextualizada

**[00:00–00:25 · Slide 0 — Capa]**

Esta é a Aula 2 da Unidade 1, dedicada à comunicação entre processos: APIs, RPC e mensageria. A aula anterior mostrou que separar a NexaOrder em serviços trouxe concorrência, ausência de estado global e falha parcial. Esta aula responde a uma pergunta prática que decorre disso.

**[00:25–00:55 · Slide 1 — Audiodescrição]**

A audiodescrição desta aula: os slides mantêm o fundo azul-marinho com molduras de triângulos em amarelo, verde e ciano, e o conteúdo em cartões claros. São cinco recursos visuais nesta aula: o fluxo HTTP síncrono encadeado, a comparação entre fila e publicação-assinatura, a fórmula do backoff exponencial com jitter, o fluxo de idempotência e correlação e o quadro comparativo dos dois desenhos de criação de pedido. Descrevo cada um deles conforme forem aparecendo.

**[00:55–01:40 · Slide 2 — Sumário]**

O percurso é este. Primeiro, comunicação síncrona e assíncrona: quando esperar e quando seguir em frente. Depois, HTTP e APIs orientadas a recursos. Na sequência, RPC e contratos de interface, com o cuidado devido à serialização e à evolução de esquema. Em seguida, filas, publicação-assinatura e eventos. Fecho com as proteções da comunicação distribuída — timeout, retry, backoff e jitter — e com idempotência e correlação de requisições. E, no final, comparo lado a lado dois desenhos possíveis para a criação de pedido na NexaOrder.

**[01:40–02:20 · Slide 3 — Objetivos de aprendizagem]**

Ao final desta aula, você deve conseguir decidir entre comunicação síncrona e assíncrona a partir do contrato entre serviços, e não do hábito herdado do monólito. Deve conseguir modelar APIs orientadas a recursos, com semântica de verbos e códigos de status bem definidos. Deve conseguir evoluir esquemas de mensagem sem quebrar consumidores já implantados. Deve distinguir fila de publicação-assinatura, e evento de comando. Deve dimensionar timeouts e políticas de retentativa com backoff exponencial e jitter. E deve tornar operações repetíveis com segurança, usando chave de idempotência e identificador de correlação.

**[02:20–04:00 · Slide 4 — Situação-problema]**

O incidente que motiva a aula é o seguinte. Depois de decompor a NexaOrder em serviços, a equipe manteve o hábito do monólito: cada etapa chamava a seguinte e esperava a resposta antes de prosseguir. Com pouco tráfego, funcionava perfeitamente. Sob campanha de vendas, o comportamento mudou.

Uma lentidão no provedor de pagamento prendeu conexões no serviço de estoque. Pedidos ficou esperando estoque, e o cliente viu a tela de carregamento por vários segundos. Clientes cancelaram e tentaram de novo, gerando dois pedidos para o mesmo carrinho. E respostas chegaram depois de a interface já ter expirado, deixando o pedido marcado como “pendente” apesar de ter sido processado.

Duas perguntas passaram a organizar o projeto: quando faz sentido esperar uma resposta antes de continuar? E quando basta registrar a intenção e seguir em frente? Não há resposta universal. A escolha depende do contrato entre os serviços, da tolerância a atraso e de como as falhas serão tratadas.

### Desenvolvimento conceitual

**[04:00–05:30 · Slide 5 — Comunicação síncrona e assíncrona]**

Convém separar bem os dois conceitos, porque eles costumam ser confundidos.

Na comunicação síncrona, quem solicita aguarda a resposta antes de continuar. Uma chamada, um resultado, fluxo linear e fácil de raciocinar. Na comunicação assíncrona, quem solicita registra a intenção e segue. O resultado chega por outro canal: uma notificação, um evento posterior ou uma consulta de status.

O custo da síncrona é estrutural: em cadeias longas, a latência percebida se aproxima da soma das latências do caminho crítico. E, se todas as etapas forem obrigatórias, a indisponibilidade de um elo faz a operação inteira falhar. O ganho da assíncrona é reduzir o acoplamento temporal: o pagamento pode estar indisponível sem impedir que o pedido seja aceito.

Nenhum dos dois modelos é superior em abstrato. Síncrono serve quando o cliente precisa da resposta para decidir o próximo passo — conferir se o item ainda existe antes de mostrar a tela de pagamento, por exemplo. Assíncrono serve quando o resultado pode ser processado depois — emitir nota fiscal, avisar a transportadora, atualizar relatórios. A pergunta certa nunca é “qual é melhor”, e sim “esta interação específica precisa da resposta agora?”.

**[05:30–07:10 · Slide 6 — Exemplo numérico: o que o encadeamento síncrono custa]**

Os números mostram por que encadear chamadas síncronas é mais caro do que parece.

Em um modelo simplificado, com etapas obrigatórias e falhas independentes, a latência do fluxo soma as etapas, e a disponibilidade do fluxo é o produto das disponibilidades de cada etapa.

*[indicação de edição: exibir a fórmula da disponibilidade do fluxo com os quatro fatores, destacando o sinal de multiplicação]*

Aplicando à NexaOrder: pedidos, estoque, pagamento e expedição, cada um com 99,9% de disponibilidade. Quatro etapas encadeadas. A conta é 0,999 elevado a 4, que dá aproximadamente 0,996 — ou seja, 99,6%.

Esse resultado merece atenção. Quatro componentes com 99,9% cada não entregam 99,9% ao fluxo; entregam 99,6%. Traduzido em tempo, 99,6% corresponde a cerca de 2 horas e 53 minutos de indisponibilidade por mês, contra os 43 minutos de um serviço com 99,9%. O encadeamento multiplicou as chances de falha.

Cabe uma ressalva: esse cálculo pressupõe falhas independentes. No mundo real, dependências compartilhadas e falhas correlacionadas exigem medição conjunta, e não apenas a multiplicação dos números do contrato de cada serviço. A conta serve para mostrar a direção do efeito, não para fechar um número.

**[07:10–08:40 · Slide 7 — HTTP e APIs orientadas a recursos]**

Passemos aos mecanismos concretos, começando por HTTP.

A ideia central de uma API orientada a recursos é que cada entidade relevante do domínio — um pedido, uma reserva, uma cobrança — vira um recurso identificado por uma URI, e as operações se expressam por verbos. POST cria um recurso e devolve um identificador, como em POST barra pedidos. GET consulta o estado atual, sem efeito colateral, como em GET barra pedidos barra identificador. PUT e PATCH substituem ou atualizam parcialmente.

Os códigos de status também carregam semântica. A faixa 2xx indica sucesso — 201 Created na criação do pedido. A faixa 4xx indica erro do cliente, como um 404 para um pedido que não existe. E a faixa 5xx indica erro do servidor, como um 503 quando o estoque não responde. Essa distinção volta adiante, no tratamento de retentativas.

Um ponto costuma gerar confusão: ser sem estado, ou stateless, é uma decisão arquitetural da API, não uma garantia do protocolo. HTTP também transporta sessões com estado. Adotada a restrição, qualquer instância pode atender qualquer requisição — e é isso que torna o balanceamento simples.

**[08:40–10:00 · Slide 8 — RPC e contratos de interface]**

O segundo mecanismo é RPC, chamada de procedimento remoto. A ideia é invocar algo como estoque ponto reservarItem, passando pedido, item e quantidade, como se fosse uma função local. O mecanismo transforma essa chamada em mensagem de rede.

*[indicação de edição: inserir texto em tela — “RPC parece local. Não é.” — com destaque]*

Nisso reside o risco, que é exatamente a transparência discutida na Aula 1: conveniente para quem usa, perigosa para quem projeta. A chamada remota tem falhas que a função local não tem — rede indisponível, mensagem perdida, resposta ausente mesmo com a operação concluída do outro lado.

O valor real de RPC não é parecer local. É o contrato explícito: métodos, tipos de parâmetro e de retorno, e erros possíveis, descritos em uma linguagem de definição de interface. A partir desse contrato único, cliente e servidor compatíveis podem ser gerados, o que reduz divergência manual.

Um esclarecimento importante: síncrono não é uma propriedade do protocolo. Tanto HTTP quanto RPC sustentam interações assíncronas. Síncrono e assíncrono descrevem o contrato de interação entre os serviços, não a tecnologia de transporte.

**[10:00–11:20 · Slide 9 — Serialização e evolução de esquema]**

Toda mensagem precisa ser serializada, ou seja, transformada de dados em memória para bytes que trafegam pela rede. O formato — JSON, binário — afeta tamanho e desempenho. O problema realmente crítico, porém, é outro: a evolução do esquema.

O motivo é simples: serviços independentes são implantados em momentos diferentes. Não existe o instante em que todos atualizam simultaneamente.

Valem, então, quatro regras. Campos novos são opcionais, com valor padrão bem definido quando ausentes. Não remova nem renomeie campos que consumidores existentes ainda utilizam. Versione explicitamente quando a mudança for de fato incompatível. E teste a compatibilidade entre versões de produtor e de consumidor antes de implantar.

Ignorar esses cuidados transforma uma alteração aparentemente local — a equipe de pedidos adiciona um campo canalVenda — em uma interrupção distribuída, sentida por serviços que essa equipe talvez nem soubesse que existiam.

**[11:20–11:40 · Slide 10 — Citação]**

Esta é a formulação a reter: uma chamada RPC pode falhar de formas que uma chamada local nunca falha — a resposta pode não retornar mesmo que a operação remota tenha sido concluída com sucesso.

### Demonstração, exemplo ou estudo de caso

**[11:40–12:50 · Slide 11 — Fila e publicação-assinatura]**

Passemos à comunicação assíncrona. Ela costuma passar por um intermediário, o broker, que recebe, armazena temporariamente e entrega mensagens. É esse armazenamento que desacopla o tempo de vida do produtor do tempo de vida do consumidor.

*[indicação de edição: inserir Recurso visual 6 da Aula 2 — comparação entre fila e publicação-assinatura, com as mensagens animadas nos dois modelos]*

Existem dois modelos. Na fila, também chamada de ponto a ponto, cada mensagem vai a um único consumidor entre os que competem por ela. O uso típico é distribuir trabalho: processar reservas em paralelo por várias instâncias do mesmo serviço. Na publicação-assinatura, cada mensagem de um tópico é entregue a todos os assinantes interessados. O uso típico é notificar vários serviços sobre o mesmo acontecimento, sem acoplar o produtor à lista de quem escuta.

A diferença entre os dois modelos não é de tecnologia, e sim de intenção: dividir trabalho ou difundir informação.

**[12:50–14:00 · Slide 12 — Evento e comando]**

Há uma distinção que altera profundamente o acoplamento do sistema: a distinção entre evento e comando.

Evento é o registro de algo que já aconteceu: PedidoCriado, PagamentoAprovado. Comando é a solicitação de uma ação futura: ReservarEstoque. A diferença parece sutil, mas suas consequências são extensas.

Quem publica um evento não escolhe quem reage. Estoque, antifraude e um futuro serviço de recomendação podem assinar o mesmo PedidoCriado. O benefício é que novos consumidores entram sem alterar o produtor. O custo é que não há resposta imediata: quem publica não sabe, no mesmo instante, se e como os assinantes reagiram.

Há ainda uma consequência de projeto frequentemente percebida tarde demais: o estado do pedido deixa de ser binário — deu certo ou deu errado — e passa a ser uma progressão a ser rastreada. Isso muda a interface, muda o suporte ao cliente e muda a observabilidade.

**[14:00–15:20 · Slide 13 — Timeout, retry, backoff e jitter]**

Tratemos agora das proteções. Toda chamada de rede precisa de um limite de espera. Sem ele, uma dependência lenta retém recursos indefinidamente e propaga lentidão — foi exatamente o que ocorreu na situação-problema desta aula.

Primeiro princípio: um timeout não prova que a operação falhou. Ele indica que a resposta não chegou dentro do prazo tolerado. São afirmações distintas.

Segundo: retry só para falha transitória, e apenas se ainda houver prazo no orçamento da operação e se a repetição for segura. Erro permanente não se retenta — validações 4xx, prazo já esgotado ou sinais explícitos de sobrecarga pedem falha imediata ou controle de admissão, nunca uma nova tentativa automática.

Terceiro: há o efeito manada, o thundering herd. Retentar sem critério lança uma nova onda de requisições sobre um serviço já sobrecarregado, agravando precisamente o problema que se pretendia resolver.

A resposta a isso combina duas técnicas. Backoff exponencial: cada tentativa espera mais que a anterior, dando tempo de recuperação. E jitter: uma soma aleatória que evita que todos os clientes retentem no mesmo instante.

**[15:20–16:50 · Slide 14 — Exemplo numérico: a progressão do backoff]**

O comportamento fica evidente em números.

*[indicação de edição: inserir Recurso visual 7 da Aula 2 — fórmula do backoff com jitter, construída termo a termo, seguida da progressão animada dos cinco valores]*

A fórmula é: o tempo da tentativa n é o mínimo entre o tempo-base multiplicado por dois elevado a n e um teto máximo, mais um valor aleatório sorteado entre zero e o jitter máximo.

Com tempo-base de 200 milissegundos e teto de 5 segundos, o componente exponencial, sem jitter, evolui assim: na tentativa zero, 200 milissegundos; na tentativa um, 400; na dois, 800; na três, 1,6 segundo; na quatro, 3,2 segundos. Cada tentativa dobra a espera anterior.

O teto cumpre um papel específico. Sem ele, a tentativa cinco esperaria 6,4 segundos, prazo impraticável para quem aguarda diante da tela. O teto interrompe esse crescimento. E o jitter soma alguns milissegundos aleatórios a cada valor, espalhando as tentativas no tempo mesmo quando muitos clientes falharam no mesmo instante — que é justamente o cenário do efeito manada.

**[16:50–18:00 · Slide 15 — Idempotência]**

Backoff e jitter, no entanto, não resolvem tudo. Eles espalham as tentativas no tempo, mas não impedem a duplicação. Se a operação já produziu efeito no destino, repeti-la sem proteção gera cobrança duplicada. É esse o problema que a idempotência resolve.

Uma operação é idempotente quando executá-la mais de uma vez produz o mesmo efeito que executá-la uma vez. Consultar um pedido é idempotente por natureza. Criar um pedido, sem nenhum cuidado adicional, não é.

*[indicação de edição: inserir Recurso visual 8 da Aula 2 — fluxo de idempotência em quatro passos, revelados um a um]*

O mecanismo tem quatro passos. Primeiro, o cliente gera a chave de idempotência antes do primeiro envio — antes, não depois da falha. Segundo, essa chave acompanha o pedido original e toda retentativa da mesma operação. Terceiro, o serviço registra as chaves já processadas junto com o resultado produzido. Quarto, quando uma chave repetida chega, o serviço devolve o resultado da primeira execução, sem criar um novo pedido.

O mecanismo é simples de enunciar e resolve a classe inteira de problemas que abriu a Aula 1.

### Aplicação profissional

**[18:00–18:40 · Slide 16 — Correlação]**

Complementar à idempotência, existe a correlação. O identificador de correlação acompanha uma operação lógica por várias chamadas, mensagens e retentativas.

A diferença entre os dois mecanismos é direta: a chave de idempotência evita duplicar efeito; o identificador de correlação permite reconstruir o caminho. Ele atravessa serviços — o mesmo identificador segue de pedidos a estoque, pagamento e expedição — e é a base da observabilidade. Sem correlação, um incidente vira uma coleção de logs que ninguém consegue costurar.

Um ponto profissional importante: a correlação precisa ser decidida no contrato, no desenho da comunicação. Ela não pode ser improvisada durante o incidente, momento em que já é indispensável. Na Unidade 4, traces e spans se apoiam exatamente nessa ideia.

**[18:40–19:15 · Slide 17 — Dois fluxos de criação de pedido, lado a lado]**

A comparação entre os dois desenhos fecha a aula.

*[indicação de edição: inserir Recurso visual 9 da Aula 2 — quadro comparativo dos dois fluxos, revelando uma linha por vez]*

No fluxo síncrono encadeado, o cliente recebe confirmação completa em uma única resposta; a latência percebida é a soma das etapas do caminho crítico; a falha de uma etapa indisponibiliza o fluxo inteiro; novos consumidores exigem alterar quem chama; e o custo introduzido é acoplamento temporal forte.

No fluxo orientado a eventos, o cliente recebe um status “processando” imediato; a latência percebida é apenas o registro da intenção; a falha de uma etapa gera evento próprio e pode acionar compensação; novos consumidores assinam o evento sem tocar no produtor; e o custo introduzido é ter que rastrear etapa, tratar mensagens fora de ordem e comunicar progressão ao cliente.

Um cuidado se impõe: no fluxo por eventos, a sequência PedidoCriado, EstoqueReservado, PagamentoAprovado, PedidoEnviado preserva as pré-condições de negócio. Desacoplamento não autoriza expedir antes de cobrar. Já consumidores sem pré-condição, como antifraude, reagem direto ao PedidoCriado.

### Fechamento

**[19:15–19:40 · Slides 18 e 19 — Pontos-chave e atividade prática]**

Recapitulando. Síncrono soma: simplifica o raciocínio, mas soma latências e propaga indisponibilidade pela cadeia. Assíncrono desacopla: reduz o acoplamento temporal ao custo de resposta não imediata e mais complexidade de rastreamento. Contratos importam, tanto em APIs de recursos quanto em RPC. Esquema evolui, e compatibilidade é requisito, não detalhe. Retry tem critério: timeout limita a espera, e backoff com jitter só vale para falha transitória, dentro de um orçamento. E, por fim, a chave de idempotência evita duplicar efeito enquanto o identificador de correlação torna a operação rastreável de ponta a ponta.

Na atividade prática, você vai modelar o contrato do evento PedidoCriado: listar campos obrigatórios e opcionais com seus tipos, incluir chave de idempotência e identificador de correlação justificando cada um, descrever uma mudança futura de esquema sem quebrar consumidores, separar reações independentes das que exigem pré-condição, justificar por que a expedição não pode começar antes da aprovação do pagamento e definir uma política limitada de retry.

**[19:40–20:00 · Slide 20 — Encerramento]**

Esta aula deixa três capacidades formadas: escolher entre esperar e seguir em frente, modelar contratos que sobrevivem à evolução e proteger chamadas de rede com timeout, retry e idempotência. A próxima aula trata de uma pergunta que parece trivial e não é: qual evento aconteceu primeiro?

### Indicações de edição e recursos visuais

- Slide 0 — capa da Aula 2 (00:00–00:25).
- Slide 1 — audiodescrição narrada integralmente (00:25–00:55).
- Slide 4 — situação-problema, com os quatro sintomas destacados um a um (02:20–04:00).
- Slide 6 — fórmula da disponibilidade do fluxo, com o produto dos quatro fatores em destaque (aproximadamente 05:50).
- Recurso visual 5 — fluxo HTTP síncrono encadeado, com barra de progresso somando latências (aproximadamente 07:20).
- Card “RPC parece local. Não é.” (aproximadamente 08:50).
- Slide 10 — citação em tela cheia (11:20).
- Recurso visual 6 — comparação entre fila e publicação-assinatura (aproximadamente 11:50).
- Recurso visual 7 — fórmula do backoff com jitter e progressão dos cinco valores (aproximadamente 15:30).
- Recurso visual 8 — fluxo de idempotência em quatro passos (aproximadamente 17:10).
- Recurso visual 9 — quadro comparativo dos dois fluxos de criação de pedido (aproximadamente 18:45).
- Slide 20 — vinheta de encerramento e chamada para a próxima aula (últimos 15 segundos).

### Fontes e links de mídia

- BIRRELL, Andrew D.; NELSON, Bruce Jay. Implementing remote procedure calls. *ACM Transactions on Computer Systems*, v. 2, n. 1, p. 39-59, 1984. DOI: 10.1145/2080.357392 — referência conceitual, sem reprodução de trecho externo.
- FIELDING, Roy Thomas. *Architectural styles and the design of network-based software architectures*. 2000. Tese (Doutorado) — University of California, Irvine, 2000 — referência conceitual, sem reprodução de trecho externo.
- Nenhuma mídia de terceiros é incorporada; diagramas, fórmulas e animações devem ser produzidos originalmente pela equipe de edição a partir do texto-base da Aula 2 (`unidade_1.md`) e do deck `unidade_1/slides/aula2.html`.

---

## Roteiro da Videoaula 3 — “Qual evento aconteceu primeiro? A pergunta que o relógio não responde sozinho”

**Vínculo com o plano de aprendizagem:** Unidade 1, Aula 3 — Concorrência, relógios e ordenação de eventos.

**Deck de apoio:** `unidade_1/slides/aula3.html` — 20 slides (capa, audiodescrição, sumário, 16 de conteúdo e encerramento).

**Objetivo da videoaula:** ao final, o estudante deve ser capaz de explicar por que carimbos de hora físicos não ordenam com segurança eventos de processos diferentes, estimar o desvio máximo entre relógios, aplicar a relação happened-before, calcular relógios lógicos de Lamport, comparar relógios vetoriais para detectar concorrência e definir uma política de resolução de conflito antes que ele ocorra.

**Mapa de tempo e slides:** 00:00 capa · 00:25 audiodescrição · 00:55 sumário · 01:40 objetivos · 02:20 situação-problema · 03:50 ausência de relógio global · 05:10 exemplo numérico do desvio · 06:50 happened-before · 08:30 regras de Lamport · 10:00 exemplo numérico de Lamport · 12:00 citação · 12:20 limite de Lamport · 13:30 relógios vetoriais · 14:50 exemplo numérico dos vetores · 16:20 ordem total e parcial · 17:20 conflitos concorrentes · 18:20 pausa para reflexão · 19:10 pontos-chave e atividade · 19:40 encerramento.

### Abertura contextualizada

**[00:00–00:25 · Slide 0 — Capa]**

Esta é a Aula 3 da Unidade 1, dedicada a concorrência, relógios e ordenação de eventos. A pergunta que organiza a aula parece elementar, mas está entre as mais difíceis da computação distribuída: qual evento aconteceu primeiro?

**[00:25–00:55 · Slide 1 — Audiodescrição]**

A audiodescrição desta aula: os slides mantêm o fundo azul-marinho com molduras de triângulos em amarelo, verde e ciano, e o conteúdo em cartões claros. São cinco recursos visuais: dois relógios divergentes, a fórmula do desvio acumulado, a linha do tempo com raias por processo, a tabela de carimbos de Lamport e a comparação de dois vetores posição a posição. Descrevo cada um conforme aparecem.

**[00:55–01:40 · Slide 2 — Sumário]**

O percurso começa pela ausência de um relógio global, passa pelos relógios físicos, seu desvio e sua sincronização, e chega à relação happened-before, que é a base conceitual de tudo. Em seguida construímos os relógios lógicos de Lamport, vemos o limite deles e avançamos para relógios vetoriais, que permitem detectar concorrência com certeza. Depois separo ordem total, ordem parcial e causalidade, aplico tudo isso a um conflito real entre estoque e pagamento na NexaOrder e fecho com a necessidade de uma política de resolução definida a priori.

**[01:40–02:20 · Slide 3 — Objetivos de aprendizagem]**

Ao final da aula, você deve conseguir explicar por que carimbos de hora físicos não ordenam com segurança eventos de processos diferentes. Deve conseguir estimar o desvio máximo entre relógios a partir da taxa de drift e do intervalo de sincronização. Deve aplicar a relação happened-before para identificar pares causalmente relacionados. Deve calcular relógios lógicos de Lamport ao longo de uma sequência de eventos e mensagens. Deve comparar relógios vetoriais para afirmar, com certeza, que dois eventos são concorrentes. E deve definir uma política de resolução de conflito antes que o conflito ocorra em produção.

**[02:20–03:50 · Slide 4 — Situação-problema]**

O incidente que abre a aula é este. O painel de operações da NexaOrder ordena eventos pelo carimbo de hora físico do servidor que os gerou. Em um incidente, ReservaCancelada apareceu antes de PagamentoAprovado.

*[indicação de edição: inserir Recurso visual 10 da Aula 3 — dois relógios de parede, um adiantado e outro atrasado, sobre os ícones do serviço de estoque e do serviço de pagamento]*

A equipe examinou o painel, concluiu que o cancelamento viera primeiro e estornou o pagamento automaticamente. A conclusão parece razoável: se o cliente cancelou, devolve-se o dinheiro.

A apuração posterior revelou outra coisa: o relógio do servidor de pagamento estava atrasado. A ordem exibida na tela refletia a ordem dos carimbos, não a ordem dos acontecimentos.

O ponto decisivo é este: o problema não é de configuração. Ninguém deixou de instalar o serviço de sincronização. O problema é estrutural. Não existe relógio único capaz de ordenar eventos de processos diferentes com precisão absoluta. Essa é uma propriedade do mundo, não um defeito da NexaOrder.

### Desenvolvimento conceitual

**[03:50–05:10 · Slide 5 — A ausência de um relógio global]**

Convém entender a razão disso.

Dentro de um único processo, as instruções ocorrem em sequência total. Comparar “antes” e “depois” é trivial, porque existe uma linha do tempo única e um único executor.

Entre processos, a situação é outra. Cada processo tem seu relógio local, e não existe sinal instantâneo capaz de sincronizá-los perfeitamente. Qualquer sinal de sincronização também viaja pela rede, e a rede introduz atraso variável entre o envio e a chegada. Essa variação não pode ser eliminada — ela pode ser reduzida, medida, estimada, mas não zerada.

A consequência prática é direta: a pergunta “o pagamento foi recusado antes ou depois da reserva?” não se responde comparando carimbos gerados independentemente por dois servidores. Um carimbo de hora físico reflete apenas o relógio local de quem o gerou. E relógios locais divergem.

**[05:10–06:50 · Slide 6 — Exemplo numérico: quanto dois relógios podem divergir]**

Essa divergência pode ser quantificada, e a ordem de grandeza costuma ser maior do que se supõe.

Relógios de computadores comuns sofrem desvio, o drift, causado por variações no oscilador de quartzo — temperatura, envelhecimento, tensão. A sincronização por rede reduz a divergência periodicamente, mas não a elimina entre duas sincronizações sucessivas.

*[indicação de edição: inserir a fórmula do desvio máximo, com cada termo aparecendo conforme a fala]*

O limite é: o desvio máximo é menor ou igual ao erro residual da sincronização, que chamo de épsilon, mais duas vezes a taxa de drift multiplicada pelo intervalo sem sincronizar. O fator dois aparece porque, no pior caso, um relógio adianta enquanto o outro atrasa.

Os números do exemplo são estes. Taxa de drift de 50 partes por milhão, ou seja, 0,00005. Intervalo de uma hora sem sincronizar, que são 3600 segundos. Isolando o drift, com épsilon igual a zero: duas vezes 0,00005, vezes 3600, resulta em 0,36 segundo. Trezentos e sessenta milissegundos.

A conexão com o incidente é imediata. Trezentos e sessenta milissegundos bastam para inverter, em um painel ordenado por carimbo físico, dois eventos separados por menos que isso. Sincronizar com mais frequência reduz a parcela de drift, mas o erro residual da própria sincronização permanece. Reduz-se o limite; jamais se o anula.

**[06:50–08:30 · Slide 7 — A relação happened-before]**

Diante dessa impossibilidade, Leslie Lamport propôs, em 1978, uma saída elegante: em vez de confiar no relógio físico, confiar na causalidade observável. Ele definiu uma relação lógica, escrita com uma seta, que ordena eventos por causalidade — não por tempo de relógio.

São três regras. Primeira, mesmo processo: se dois eventos ocorrem no mesmo processo e um executa antes do outro, então o primeiro aconteceu antes do segundo. Trata-se do sequenciamento que qualquer programa já possui.

Segunda, mensagem: se um evento é o envio de uma mensagem e outro é o recebimento dessa mesma mensagem, então o envio aconteceu antes do recebimento. A regra parece evidente, mas é ela que costura causalidade entre processos diferentes.

Terceira, transitividade: se A aconteceu antes de B, e B aconteceu antes de C, então A aconteceu antes de C — mesmo que A e C estejam em processos que nunca trocaram mensagem diretamente.

Chega-se, assim, ao conceito central da aula. Dois eventos sem nenhuma dessas relações, nem direta nem transitiva, são chamados concorrentes, o que significa que nenhum deles pode ter causado o outro. Note-se que isso não depende de proximidade no tempo físico. Dois eventos separados por uma semana podem ser concorrentes, se não houver caminho causal entre eles.

**[08:30–10:00 · Slide 8 — Relógios lógicos de Lamport: as três regras]**

Para tornar essa ideia operacional, Lamport propôs um mecanismo simples: cada processo mantém um contador inteiro.

Regra um, evento local ou envio: incremente o contador em 1 e use o novo valor como carimbo do evento. Regra dois, ao enviar: inclua na mensagem o carimbo atribuído ao evento de envio. Regra três, ao receber: ajuste o contador para o máximo entre o valor local e o valor que veio na mensagem, e some 1.

*[indicação de edição: destacar a fórmula do recebimento, com máximo entre contador local e contador da mensagem, mais um]*

A garantia que esse mecanismo oferece é a seguinte: se A aconteceu antes de B, então o carimbo de A é menor que o carimbo de B. Causalidade implica ordem numérica crescente. A direção do enunciado é essencial: adiante veremos por que a implicação contrária não se sustenta.

**[10:00–12:00 · Slide 9 — Exemplo numérico: Lamport aplicado à NexaOrder]**

O mecanismo se torna mais claro quando aplicado, passo a passo, a um trecho do fluxo da NexaOrder. Pedidos e Estoque começam ambos com contador zero.

*[indicação de edição: exibir a tabela de carimbos de Lamport ao vivo, preenchendo linha por linha conforme a narração]*

Evento 1: Pedidos cria o pedido. É um evento local, então o contador de Pedidos vai de zero para um.

Evento 2: Pedidos envia ao Estoque a solicitação “reservar item”. É um evento de envio, então o contador vai de um para dois, e o valor dois é anexado à mensagem.

Evento 3: Estoque recebe a mensagem, que chegou carregando o carimbo dois. O contador de Estoque estava em zero. Aplicando a regra: máximo entre zero e dois, que é dois, mais um, dá três. O contador do Estoque passa a valer três.

Evento 4: Estoque envia a confirmação de reserva. Contador vai de três para quatro, e o quatro é anexado à mensagem.

Evento 5: Pedidos recebe a confirmação com carimbo quatro. O contador de Pedidos estava em dois. Máximo entre dois e quatro, que é quatro, mais um, dá cinco.

Observada a cadeia inteira, o evento 5 recebeu carimbo 5, maior que o carimbo 2 que iniciou a troca e maior que o carimbo 4 do envio que o causou diretamente. A propriedade “A antes de B implica carimbo de A menor que carimbo de B” foi respeitada em todos os passos. Ao contrário do relógio de parede, esse resultado não depende de nenhum servidor estar com a hora certa.

**[12:00–12:20 · Slide 10 — Citação]**

A frase que abre a segunda metade da aula é esta: o relógio de Lamport ordena, mas não distingue causalidade de coincidência — dois eventos concorrentes também recebem carimbos diferentes.

### Demonstração, exemplo ou estudo de caso

**[12:20–13:30 · Slide 11 — O limite de Lamport]**

Essa limitação merece exame cuidadoso, pois é a origem de muitos erros de interpretação em produção.

A garantia de Lamport vale em um sentido só: A antes de B implica carimbo de A menor que carimbo de B. A recíproca não é verdadeira. Carimbo menor não implica relação causal.

Imagine que o serviço de Pagamento, sem trocar nenhuma mensagem com Pedidos ou Estoque, chegasse ao carimbo 5 apenas por eventos internos próprios. O empate numérico com o evento 5 de Pedidos não indicaria relação causal alguma. É coincidência de contagem.

O motivo é estrutural: o contador é um número único, e ele não guarda de quem veio cada avanço. Ele registra que houve progresso, mas não a origem do progresso.

A consequência prática, decisiva no trabalho cotidiano, é que comparar carimbos de Lamport não autoriza afirmar que um evento causou o outro. É exatamente essa limitação que motiva o próximo mecanismo.

**[13:30–14:50 · Slide 12 — Relógios vetoriais]**

Relógio vetorial. Em vez de um contador, cada processo mantém um vetor com uma posição por processo do sistema.

As regras são análogas, mas com uma diferença crucial. Em um evento local, o processo incrementa apenas a própria posição no vetor. Ao enviar, anexa o vetor completo à mensagem. Ao receber, atualiza cada posição para o maior valor entre o próprio e o recebido, e então incrementa a própria posição.

A comparação também muda. Dizemos que A aconteceu antes de B se todas as posições do vetor de A forem menores ou iguais às de B, com pelo menos uma estritamente menor. Ou seja, o vetor de B domina o vetor de A em todas as posições.

O ganho está aqui: se nenhum vetor domina o outro — se um é maior em uma posição e menor em outra — então os eventos são genuinamente concorrentes. O relógio vetorial permite afirmá-lo com certeza, o que o relógio de Lamport não permitia. O preço é o tamanho: o vetor cresce com o número de processos.

**[14:50–16:20 · Slide 13 — Exemplo numérico: dois eventos concorrentes]**

A aplicação ao incidente de abertura é direta. Os vetores estão na ordem Pedidos, Estoque, Pagamento.

*[indicação de edição: inserir Recurso visual 11 da Aula 3 — comparação dos vetores posição a posição, com destaque na cor de quem é maior em cada linha]*

O evento ReservaCancelada ocorre no Estoque, por timeout do cliente, com vetor dois, três, zero. O evento PagamentoAprovado ocorre a partir do provedor de pagamento, com vetor dois, um, dois.

A comparação se faz posição a posição. Na posição de Pedidos: dois contra dois — empate. Na posição de Estoque: três contra um — maior no cancelamento. Na posição de Pagamento: zero contra dois — maior na aprovação.

Conclusão: nenhum vetor domina o outro. Os dois eventos são concorrentes. Nenhum causou o outro.

O significado desse resultado para o negócio é importante. O sistema passa a saber, com certeza matemática, que não há relação causal entre o cancelamento e a aprovação. Essa certeza, porém, não indica qual dos dois deve prevalecer. A ordem causal, sozinha, não resolve o conflito. Isso exige uma regra de negócio explícita — que é uma decisão humana, não uma dedução técnica.

**[16:20–17:20 · Slide 14 — Ordem total, ordem parcial e causalidade]**

Convém separar três ideias que costumam ser confundidas.

Ordem parcial é o que happened-before define: alguns pares de eventos são comparáveis, e outros, por serem concorrentes, são incomparáveis. Isso não constitui limitação do modelo, e sim descrição fiel da realidade.

Ordem total compara todo par de eventos. Ela surge naturalmente dentro de um processo, ou por imposição externa. E se impõe de duas formas: por um sequenciador central, ou por desempate determinístico usando, por exemplo, o identificador do processo.

Há também o que a ordem total não faz: impor ordem total sobre eventos concorrentes não recupera uma causalidade que nunca existiu. Ela é útil quando o sistema precisa de uma decisão única e consistente sobre qual atualização prevalece. O erro conceitual, bastante comum, está em confundir a posição escolhida arbitrariamente com a afirmação de que um evento causou o outro.

**[17:20–18:20 · Slide 15 — Conflitos concorrentes em estoque e pagamento]**

Com esse vocabulário, o incidente da abertura pode ser reformulado com precisão: o cancelamento e a aprovação eram concorrentes. E nenhuma sincronização de relógio físico eliminaria isso, porque a concorrência é estrutural — os eventos ocorreram em processos diferentes, sem troca de mensagem entre eles.

Diante disso, existem três políticas legítimas.

Priorizar o cancelamento é a política conservadora: evita cobrar por item indisponível, mas pode gerar estorno desnecessário. Priorizar a aprovação é a política otimista: pode gerar cobrança para um item que não será enviado. Tratar como exceção significa suspender o pedido para revisão manual ou automatizada, aceitando o custo operacional dessa revisão.

Qualquer uma das três é defensável. O único erro efetivo é não escolher, deixando que a ordem acidental de chegada das mensagens decida pela equipe.

### Aplicação profissional

**[18:20–19:10 · Slide 16 — Pausa para reflexão]**

A aula se encerra com uma reflexão. Pause o vídeo e responda por escrito às perguntas a seguir.

No incidente, ReservaCancelada aparece três segundos antes de PagamentoAprovado, e o relógio do servidor de pagamento estava atrasado.

*[indicação de edição: pausar a narração por 10 segundos com o texto “Pense: essa conclusão está garantida pelos dados?” na tela]*

Primeira pergunta: a conclusão “o cancelamento ocorreu primeiro” está logicamente garantida pelos dados disponíveis? Segunda: que informação, se registrada nos eventos, permitiria decidir se há relação causal ou apenas concorrência? Terceira: com relógios vetoriais, o sistema saberia qual deve prevalecer — ou apenas que ambos são concorrentes? E quarta: que política de negócio a NexaOrder deveria adotar diante desse par concorrente?

Não existe uma única resposta correta para a última pergunta. Existe, porém, uma resposta ausente que caracteriza um sistema mal projetado: não ter pensado no cenário antes de ele acontecer em produção.

Na prática profissional, a pergunta a levar para qualquer revisão de arquitetura é: este sistema está ordenando por carimbo físico, por causalidade ou apenas por um desempate determinístico? As três respostas são diferentes, e as consequências também.

### Fechamento

**[19:10–19:40 · Slides 17 e 18 — Pontos-chave e atividade prática]**

Recapitulando. Não existe relógio global: relógios físicos de máquinas diferentes divergem por desvio acumulado, e carimbos não ordenam com segurança. Happened-before ordena por causalidade observável — execução local e troca de mensagens — e não por tempo de relógio. O relógio de Lamport garante que causalidade implica ordem numérica crescente, mas a recíproca não vale. Relógios vetoriais, comparados posição a posição, permitem afirmar com certeza que dois eventos são concorrentes. Ordem total é uma escolha que pode ser imposta artificialmente, sem recuperar relações causais inexistentes. E eventos concorrentes sobre o mesmo dado exigem uma política de resolução definida antes do incidente.

Na atividade prática, você vai construir os carimbos de Lamport para uma sequência de oito eventos envolvendo Pedidos, Estoque e Expedição, todos iniciando em zero, e depois identificar dois eventos concorrentes da sequência — justificando com base na definição de happened-before, e não na proximidade dos carimbos.

**[19:40–20:00 · Slide 19 — Encerramento]**

Esta aula forma a capacidade de raciocinar sobre tempo e ordem sem depender cegamente de relógios físicos e de reconhecer quando dois eventos são genuinamente concorrentes. A próxima aula, última da Unidade 1, trata de modelos de falha e desenho para recuperação.

### Indicações de edição e recursos visuais

- Slide 0 — capa da Aula 3 (00:00–00:25).
- Slide 1 — audiodescrição narrada integralmente (00:25–00:55).
- Recurso visual 10 — dois relógios de parede divergentes sobre os ícones de estoque e pagamento (aproximadamente 02:30).
- Slide 6 — fórmula do desvio máximo de relógio, construída termo a termo (aproximadamente 05:30).
- Slide 7 — as três regras de happened-before, reveladas uma a uma (aproximadamente 07:00).
- Slide 9 — tabela dos carimbos de Lamport, preenchida linha a linha em sincronia com a narração (10:00–12:00).
- Slide 10 — citação em tela cheia (12:00).
- Recurso visual 11 — comparação dos vetores $(2,3,0)$ e $(2,1,2)$, posição a posição (aproximadamente 15:00).
- Slide 16 — pausa de reflexão de 10 segundos (aproximadamente 18:40).
- Slide 19 — vinheta de encerramento e chamada para a próxima aula (últimos 15 segundos).

### Fontes e links de mídia

- LAMPORT, Leslie. Time, clocks, and the ordering of events in a distributed system. *Communications of the ACM*, v. 21, n. 7, p. 558-565, 1978. DOI: 10.1145/359545.359563 — referência conceitual, sem reprodução de trecho externo.
- FIDGE, Colin J. Timestamps in message-passing systems that preserve the partial ordering. *Australian Computer Science Communications*, v. 10, n. 1, p. 56-66, 1988 — referência conceitual, sem reprodução de trecho externo.
- Nenhuma mídia de terceiros é incorporada; diagramas, tabelas e fórmulas devem ser produzidos originalmente pela equipe de edição a partir do texto-base da Aula 3 (`unidade_1.md`) e do deck `unidade_1/slides/aula3.html`.

---

## Roteiro da Videoaula 4 — “Um serviço lento não é um serviço fora do ar: contendo o colapso em cascata”

**Vínculo com o plano de aprendizagem:** Unidade 1, Aula 4 — Modelos de falha e desenho para recuperação.

**Deck de apoio:** `unidade_1/slides/aula4.html` — 20 slides (capa, audiodescrição, sumário, 16 de conteúdo e encerramento).

**Objetivo da videoaula:** ao final, o estudante deve ser capaz de classificar falhas em parada, omissão, temporização e comportamento arbitrário, reconhecer detectores de falha como estimativas imperfeitas, identificar o risco de split-brain em um particionamento, aplicar circuit breaker, bulkhead e degradação graciosa, calcular a taxa de erro que abre um disjuntor e ligar cada investimento em resiliência a um objetivo de confiabilidade declarado.

**Mapa de tempo e slides:** 00:00 capa · 00:25 audiodescrição · 00:55 sumário · 01:40 objetivos · 02:20 situação-problema · 03:50 quatro modelos de falha · 05:40 detectores de falha · 07:10 partição e split-brain · 08:40 isolamento · 10:00 citação · 10:20 timeout como decisão · 11:40 circuit breaker · 13:10 exemplo numérico do disjuntor · 14:50 bulkhead · 16:00 degradação graciosa · 17:10 objetivos de confiabilidade · 18:30 transição para a Unidade 2 · 19:10 pontos-chave e atividade · 19:40 encerramento.

### Abertura contextualizada

**[00:00–00:25 · Slide 0 — Capa]**

Esta é a última aula da Unidade 1, dedicada a modelos de falha e desenho para recuperação. A unidade se encerra com o incidente mais grave que a NexaOrder enfrentou até aqui — grave precisamente porque nenhum erro de programação esteve envolvido.

**[00:25–00:55 · Slide 1 — Audiodescrição]**

A audiodescrição desta aula: mantemos o fundo azul-marinho com molduras de triângulos em amarelo, verde e ciano, e o conteúdo em cartões claros. São cinco recursos visuais: o funil de conexões se esgotando, o quadro comparativo dos quatro modelos de falha, o diagrama das duas zonas isoladas por particionamento, o diagrama de estados do disjuntor e a tabela de objetivos de disponibilidade. Descrevo cada um deles no momento em que aparecerem.

**[00:55–01:40 · Slide 2 — Sumário]**

Este é o percurso da aula. Começo pelos modelos de falha — parada, omissão, temporização e bizantina. Trato, em seguida, da falha parcial e dos detectores de falha imperfeitos, e depois do particionamento de rede e do split-brain. Apresento então o princípio que organiza a segunda metade: redundância não basta, é preciso isolamento. Discuto o timeout como decisão, e não como prova, e a partir daí os três padrões centrais da aula — circuit breaker, bulkhead e degradação graciosa. Fecho com objetivos de confiabilidade explícitos e com a transição para a Unidade 2.

**[01:40–02:20 · Slide 3 — Objetivos de aprendizagem]**

Ao final da aula, você deve conseguir classificar falhas em parada, omissão, temporização e comportamento arbitrário. Deve reconhecer detectores de falha como estimativas sujeitas a falso positivo e falso negativo. Deve identificar o risco de divergência de estado em um particionamento de rede. Deve aplicar circuit breaker, bulkhead e degradação graciosa como padrões complementares de contenção. Deve calcular a taxa de erro que dispara a abertura de um disjuntor. E deve ligar cada investimento em resiliência a um objetivo de confiabilidade declarado.

**[02:20–03:50 · Slide 4 — Situação-problema]**

O incidente ocorreu da seguinte maneira. Durante uma campanha de vendas, o provedor externo de pagamento não ficou indisponível; apenas passou a responder devagar. Essa distinção é o eixo de toda a aula.

*[indicação de edição: inserir Recurso visual 12 da Aula 4 — animação de um funil se enchendo, com as conexões do serviço de pedidos sendo ocupadas uma a uma]*

O serviço de pedidos chamava o pagamento de forma síncrona, sem nenhum limite de recursos dedicados. As conexões disponíveis para pagamento se esgotaram rapidamente. Ocorre que o mesmo conjunto de conexões também atendia consultas de pedidos antigos. Em minutos, quem apenas desejava consultar o status de uma compra feita na semana anterior também deixou de receber resposta.

Nenhuma linha de código continha erro. Não havia defeito de implementação. Faltou contenção.

A pergunta que organiza esta aula é, portanto: como conter o raio de impacto de uma falha antes que ela vire um colapso mais amplo?

### Desenvolvimento conceitual

**[03:50–05:40 · Slide 5 — Quatro modelos de falha]**

O ponto de partida é o vocabulário, porque nem toda falha é igual e distinguir os tipos orienta a escolha da proteção adequada.

*[indicação de edição: inserir Recurso visual 13 da Aula 4 — quadro comparativo dos quatro modelos de falha, revelando uma linha por vez]*

Falha de parada, também chamada de crash: o componente para de funcionar e permanece parado. Ele não emite respostas incorretas — simplesmente não emite. É o modelo mais benigno e, em infraestrutura bem operada, o mais comum.

Falha de omissão: o componente deixa de enviar ou de receber algumas mensagens, e continua funcionando para as demais. Aparece em perda de pacotes, fila cheia, descarte seletivo sob sobrecarga.

Falha de temporização: o componente responde corretamente, mas fora do prazo esperado. É exatamente o caso do provedor de pagamento da situação-problema, e também o modelo mais difícil de diagnosticar, porque o componente parece saudável em qualquer verificação superficial.

Falha arbitrária, também chamada de bizantina: o componente produz respostas incorretas, inconsistentes ou até maliciosas. É rara dentro de uma organização, mas relevante em sistemas que atravessam fronteiras de confiança.

A orientação prática que decorre disso é a seguinte: presumir que qualquer dependência externa pode falhar por parada, omissão ou temporização — e desenhar para isso — cobre a maioria dos incidentes reais, sem pagar o custo alto de proteção contra comportamento arbitrário.

**[05:40–07:10 · Slide 6 — Falha parcial e detectores de falha]**

Uma pergunta aparentemente simples organiza esta seção: quem decide se um componente está indisponível?

A resposta é um detector de falhas. Ele pode ser explícito, com health checks e métricas, ou implícito, como “estourou o timeout três vezes seguidas”. Mas ele sempre existe, mesmo que ninguém tenha desenhado conscientemente.

O ponto central é que detectores reais nunca são perfeitos. Eles erram de duas maneiras. Falso positivo é declarar indisponível um componente que apenas está lento, o que derruba tráfego que poderia ter sido atendido. Falso negativo é demorar a perceber uma indisponibilidade real, e nesse caso o sistema continua enviando trabalho para o vazio.

Entre os dois erros existe um compromisso inescapável. Detectar rápido aumenta o risco de falso positivo. Esperar mais reduz falsos positivos, mas atrasa a reação a falhas reais. Não existe configuração que elimine os dois erros ao mesmo tempo.

Na NexaOrder, o detector pode ser tão simples quanto contar falhas consecutivas, ou combinar taxa de erro, latência e verificações de saúde. O essencial é aceitar que qualquer detector é uma estimativa, não uma certeza — e que o resto do desenho precisa conviver com essa incerteza.

**[07:10–08:40 · Slide 7 — Particionamento de rede e split-brain]**

Há um cenário que precisa ser incorporado ao vocabulário desde já, porque domina a Unidade 2: o particionamento de rede.

*[indicação de edição: inserir Recurso visual 14 da Aula 4 — duas zonas isoladas por um rompimento de rede, cada uma continuando a operar internamente]*

Particionamento é quando um subconjunto de componentes perde comunicação com outro, embora cada lado continue funcionando internamente. Imagine duas réplicas do serviço de estoque, em duas zonas diferentes, que perdem o link entre si.

Há nesse cenário uma simetria da ilusão. De cada lado, o outro parece indisponível. Tecnicamente, nenhum dos dois está caído. Os dois estão vivos, os dois estão certos sobre si mesmos, e os dois estão errados sobre o outro.

O perigo é ambos continuarem aceitando escrita de forma independente. Se as réplicas do estoque em duas zonas aceitarem reservas para os mesmos itens, cada uma se julgando a única responsável, configura-se o split-brain — cérebro dividido. A consequência é divergência de estado, que precisará ser reconciliada depois, muitas vezes com perda ou conflito de dados.

A Unidade 2 inteira gira em torno disso: replicação, tolerância a partição e consenso.

**[08:40–10:00 · Slide 8 — Redundância não basta: o princípio do isolamento]**

A Aula 1 estabeleceu que redundância só protege se as instâncias não compartilharem o mesmo ponto de falha e se houver desvio de tráfego. Esta aula acrescenta um segundo princípio, que completa a explicação do incidente.

O princípio é: impedir que a degradação de uma dependência se propague para partes do sistema que não dependem dela.

O incidente pode ser relido sob essa lente. O que houve: pedidos usava o mesmo conjunto de conexões para chamar o pagamento e para atender consultas. O efeito: todas as conexões ficaram ocupadas esperando o pagamento responder. O dano: não sobrou capacidade para consultas, que nada tinham a ver com pagamento.

A lição é que a ausência de isolamento transformou uma degradação pontual em indisponibilidade ampla. Note-se que a NexaOrder mantinha várias instâncias de pedidos. Redundância não faltou; o que faltou foi separação interna de recursos.

**[10:00–10:20 · Slide 9 — Citação]**

Esta é a formulação a reter, pois reorganiza a leitura de qualquer log de produção: um timeout não é prova de que a operação falhou; é a decisão de que a espera deixou de valer a pena.

### Demonstração, exemplo ou estudo de caso

**[10:20–11:40 · Slide 10 — Timeout como decisão deliberada]**

Sendo o timeout uma decisão, ele produz consequências nos dois extremos, e a escolha precisa ser consciente.

Timeout curto demais trata operações lentas, mas ainda válidas, como se tivessem falhado. O efeito colateral é desperdiçar trabalho que já estava em andamento e, se houver retentativa sem proteção, duplicar efeito — exatamente o problema que resolvemos com idempotência na Aula 2.

Timeout longo demais mantém recursos presos e amplia o risco de esgotamento de conexões. O efeito colateral é propagar lentidão, exatamente como na situação-problema desta aula.

Não existe valor universalmente correto. O valor apropriado depende de três coisas: a latência típica observada naquela operação específica, a criticidade de ter a resposta imediatamente e o custo de manter o recurso ocupado enquanto se espera.

Há uma boa prática a registrar: o prazo restante da operação deve ser propagado pela cadeia. Se o cliente desistiu em dois segundos, não faz sentido que pedidos, estoque e pagamento continuem trabalhando por mais quinze. Trata-se de trabalho em execução cujo resultado ninguém consumirá.

**[11:40–13:10 · Slide 11 — Circuit breaker: três estados]**

O primeiro dos três padrões é o disjuntor, ou circuit breaker.

*[indicação de edição: inserir Recurso visual 15 da Aula 4 — diagrama de estados do circuit breaker, com as transições animadas]*

O disjuntor formaliza a decisão de parar de tentar uma dependência que falha repetidamente, em vez de desperdiçar recursos em chamadas com alta probabilidade de falhar.

Ele tem três estados. Fechado: as chamadas fluem normalmente, e o disjuntor monitora a taxa de falhas em uma janela. Aberto: ultrapassado o limite, o disjuntor rejeita chamadas de imediato, sem sequer tentar a dependência — a falha vira instantânea e barata, em vez de lenta e cara. Semiaberto: decorrido um intervalo, ele permite um número limitado de chamadas de teste. Se os testes passarem, volta ao estado fechado. Se falharem, retorna ao aberto.

O estado semiaberto cumpre um papel duplo: evita que o disjuntor permaneça aberto indefinidamente e impede que todo o tráfego seja devolvido de uma só vez a um serviço ainda em recuperação.

**[13:10–14:50 · Slide 12 — Exemplo numérico: quando o disjuntor abre]**

Configurar um disjuntor é uma decisão quantitativa, e convém acompanhá-la com números.

A taxa de erro é simplesmente as chamadas com falha divididas pelo total de chamadas na janela observada.

A NexaOrder define um limite de 50% de falhas em uma janela das últimas 20 chamadas ao provedor de pagamento. Durante o incidente, observa 12 falhas nessa janela.

A conta: 12 dividido por 20 dá 0,60, ou seja, 60% de taxa de erro. Como 60% excede o limite configurado de 50%, o disjuntor abre.

O efeito prático é o que mais interessa. As chamadas seguintes ao pagamento são rejeitadas pelo próprio serviço de pedidos, imediatamente, sem esperar o timeout de rede. Cada chamada rejeitada libera uma conexão que ficaria presa por segundos. Isso devolve capacidade para as consultas de pedidos existentes — que é exatamente o isolamento que faltou no incidente original.

Convém marcar a diferença: o timeout limita uma tentativa individual; o disjuntor observa várias tentativas e decide parar de iniciar chamadas. Eles são complementares, não substitutos.

**[14:50–16:00 · Slide 13 — Bulkhead: compartimentar os recursos]**

O segundo padrão é o bulkhead, o anteparo.

A metáfora vem da náutica: os anteparos de um navio dividem o casco em compartimentos estanques, de modo que ele continua flutuando mesmo com um compartimento alagado.

Na arquitetura, o anteparo aplica o isolamento de forma estrutural: conexões, threads e filas são particionadas por dependência ou por criticidade.

Na NexaOrder, o compartimento do pagamento é um conjunto de conexões exclusivo para chamadas ao provedor. O compartimento das consultas é um conjunto separado, imune ao esgotamento do primeiro. O efeito é que a lentidão do pagamento esgota apenas o próprio compartimento. As consultas continuam sendo atendidas normalmente, porque nunca disputaram aquelas conexões.

Há uma diferença de natureza entre os dois padrões: o disjuntor é uma decisão dinâmica, tomada em tempo de execução a partir de métricas; o anteparo é uma decisão estrutural, tomada no desenho.

**[16:00–17:10 · Slide 14 — Degradação graciosa]**

O terceiro padrão é a degradação graciosa: continuar oferecendo uma versão reduzida do serviço quando uma dependência não essencial falha.

O exemplo canônico é o seguinte: se o serviço de recomendação de produtos falha, o checkout omite as recomendações e prossegue com a compra. A alternativa inadequada, ainda assim frequente, é bloquear o cliente porque um componente acessório está indisponível.

Existe um pré-requisito habitualmente esquecido: é preciso classificar de antemão quais dependências são essenciais e quais são acessórias. Essa classificação não é apenas de engenharia; é uma decisão de produto tanto quanto técnica. Alguém precisa dizer, com autoridade, que vender sem recomendação é aceitável e vender sem verificar estoque não é.

Os três padrões se complementam: o disjuntor detecta e corta o desperdício, o anteparo contém o dano no compartimento certo, e a degradação graciosa mantém o serviço de pé com o que sobrou.

### Aplicação profissional

**[17:10–18:30 · Slide 15 — Objetivos de confiabilidade]**

Resta a pergunta profissional que articula toda a aula: até onde investir em resiliência?

Detectores, isolamento, disjuntores, anteparos e degradação graciosa servem a um objetivo mensurável, não a uma aspiração vaga de que “o sistema não pode cair”.

*[indicação de edição: inserir a tabela de objetivos de disponibilidade, com o orçamento mensal correspondente em destaque]*

A tabela organiza essa correspondência. Um objetivo de 99% no fluxo de pedidos corresponde a um orçamento de cerca de 7 horas e 12 minutos de indisponibilidade por mês — aceitável para operações internas de baixo impacto. Um objetivo de 99,9% corresponde a cerca de 43 minutos, que é o alvo típico de um fluxo de receita direta. E 99,99% corresponde a cerca de 4 minutos e 19 segundos, o que exige zonas independentes e ensaio recorrente de falhas.

O papel do objetivo explícito é estabelecer um orçamento de indisponibilidade tolerável. Com ele, torna-se possível decidir quando investir mais e, principalmente, quando o nível alcançado já é suficiente. Resiliência sem objetivo declarado converte-se em investimento sem critério de parada, com equipes de engenharia dedicando meses a problemas que o negócio já considerava resolvidos.

**[18:30–19:10 · Slide 16 — Transição para a Unidade 2]**

Antes do encerramento, cabe articular a unidade inteira.

Esta unidade tratou de comunicação, ordenação e falhas em processos individuais. Um fio comum atravessa as quatro aulas: componentes autônomos, conectados por rede, discordam temporariamente sobre o estado — e o projeto precisa prever isso, em vez de negar.

A Unidade 2 desloca exatamente essa mesma pergunta para os dados. Como manter réplicas de um mesmo dado consistentes entre si? Como o sistema deve se comportar durante uma partição de rede, sem violar as garantias mais importantes? Que mecanismos garantem acordo quando múltiplos nós precisam concordar sobre um único fato? E como sustentar transações que atravessam serviços, com sagas e idempotência?

### Fechamento

**[19:10–19:40 · Slides 17 e 18 — Pontos-chave e atividade prática]**

Recapitulando os pontos-chave. Quatro modelos de falha: parada, omissão, temporização e comportamento arbitrário, sendo que a maioria dos incidentes cotidianos é das três primeiras. Detector estima: falsos positivos e falsos negativos são inevitáveis, e o desenho deve conviver com a incerteza. Partição não é queda: os dois lados continuam vivos e isolados, e aceitar escrita em ambos gera split-brain. Isolar, não apenas duplicar: redundância sem isolamento não impede que a degradação de uma dependência atinja partes não relacionadas. Padrões complementares: disjuntor corta o desperdício, anteparo compartimenta recursos e degradação graciosa preserva o essencial. E objetivo declarado: resiliência se mede contra um alvo explícito de disponibilidade.

A atividade prática pede uma análise de modos de falha do fluxo de criação de pedidos, apresentada em tabela: para cada uma das quatro etapas, ao menos um modo de falha plausível, o efeito observável pelas etapas vizinhas, ao menos uma proteção proposta, a identificação de qual etapa deveria acionar degradação graciosa e qual deveria interromper o fluxo, a justificativa dessa diferença pela criticidade de negócio e, para uma das etapas, um objetivo de disponibilidade com o orçamento correspondente em minutos por mês.

**[19:40–20:00 · Slide 19 — Encerramento]**

A Unidade 1 se encerra com o vocabulário necessário para nomear modos de falha e com padrões para conter a propagação de uma degradação. A Unidade 2 leva essas mesmas ideias para os dados: replicação, consistência, consenso e transações distribuídas. Bons estudos.

### Indicações de edição e recursos visuais

- Slide 0 — capa da Aula 4 (00:00–00:25).
- Slide 1 — audiodescrição narrada integralmente (00:25–00:55).
- Recurso visual 12 — funil de conexões se esgotando (aproximadamente 02:30).
- Recurso visual 13 — quadro comparativo dos quatro modelos de falha, revelado linha a linha (aproximadamente 04:00).
- Recurso visual 14 — duas zonas isoladas por particionamento de rede (aproximadamente 07:20).
- Slide 9 — citação em tela cheia, com 3 segundos de silêncio antes da leitura (10:00).
- Recurso visual 15 — diagrama de estados do *circuit breaker*, com transições animadas (aproximadamente 11:50).
- Slide 12 — cálculo da taxa de erro, com os quatro números aparecendo em sequência (aproximadamente 13:20).
- Slide 15 — tabela de objetivos de disponibilidade e orçamento mensal (aproximadamente 17:20).
- Slide 19 — vinheta de encerramento e transição para a Unidade 2 (últimos 15 segundos).

### Fontes e links de mídia

- CHANDRA, Tushar Deepak; TOUEG, Sam. Unreliable failure detectors for reliable distributed systems. *Journal of the ACM*, v. 43, n. 2, p. 225-267, 1996. DOI: 10.1145/226643.226647 — referência conceitual, sem reprodução de trecho externo.
- NYGARD, Michael T. *Release It!: Design and Deploy Production-Ready Software*. 2. ed. Raleigh: Pragmatic Bookshelf, 2018 — referência conceitual, sem reprodução de trecho externo.
- Nenhuma mídia de terceiros é incorporada; diagramas, quadros comparativos e fórmulas devem ser produzidos originalmente pela equipe de edição a partir do texto-base da Aula 4 (`unidade_1.md`) e do deck `unidade_1/slides/aula4.html`.
