# Roteiros das videoaulas 9 a 12

Duração-base de 20 minutos por videoaula, aproximadamente 2.200 a 2.700 palavras faladas cada, ajustadas pela presença de demonstrações. Os roteiros abaixo são texto de narração para gravação — fala corrida, não notas de aula —, com indicações de edição em itálico entre colchetes.

---

## Roteiro da Videoaula 9 — “Serviços separados, mas ainda amarrados: como desenhar fronteiras de verdade”

**Vínculo com o plano de aprendizagem:** Unidade 3, Aula 9 — Decomposição em serviços e limites de domínio.

**Objetivo da videoaula:** capacitar o estudante a distinguir monólito, monólito modular e microsserviços, e a usar coesão, acoplamento, contexto delimitado e capacidade de negócio para desenhar fronteiras de serviço que reduzam acoplamento sem multiplicar coordenação entre times.

### Abertura contextualizada

Oi! Seja bem-vindo à Unidade 3 da nossa disciplina de Distributed Systems Engineering. Nas duas primeiras unidades, a gente conversou sobre comunicação, tempo, falhas, replicação e consenso. Agora a NexaOrder já tem quatro serviços — pedidos, estoque, pagamento e expedição — e, à primeira vista, parece que o trabalho de "distribuir o sistema" já está feito. Só que tem um problema: dividir em processos separados não é a mesma coisa que desacoplar de verdade.

*[indicação de edição: inserir tela com o logotipo da NexaOrder e um esquema simples dos quatro serviços já mencionados nas unidades anteriores]*

Imagina a seguinte cena. É segunda-feira de manhã, a equipe de pedidos quer lançar uma pequena mudança no formato do pedido, algo que parece trivial. Só que essa mudança quebra o serviço de estoque, porque os dois compartilham a mesma tabela no banco de dados. E pior: para lançar essa correção, as duas equipes precisam coordenar um horário de implantação conjunta, porque não dá para atualizar um sem o outro. Isso é sintoma de um problema que tem nome: monólito distribuído. A gente paga o preço da rede, da serialização, das falhas parciais — tudo que já vimos nas unidades anteriores — sem ganhar o principal benefício, que é a autonomia de cada serviço evoluir e ser implantado sozinho.

Nesta aula, a gente vai entender por que isso acontece e, principalmente, como desenhar fronteiras de serviço que realmente funcionem.

### Desenvolvimento conceitual

Primeiro, vamos separar três formas de organizar um sistema, porque elas costumam ser tratadas, erradamente, como uma escada onde "microsserviços" é sempre o degrau mais alto.

Um monólito é aquele sistema implantado como uma unidade só. Pode até ter módulos internos bem organizados no código, mas o deploy, o processo, geralmente o banco de dados, tudo é compartilhado.

Um monólito modular é diferente: continua sendo uma unidade de implantação só, mas com fronteiras internas rígidas entre os módulos — interfaces explícitas, e, se possível, até esquemas de dados separados dentro do mesmo banco. Repara que eu não estou descrevendo isso como "estágio intermediário para chegar a microsserviços". Um monólito modular bem feito é uma arquitetura legítima, ponto final. Times pequenos, com pouca maturidade operacional, costumam sofrer menos com um monólito modular bem desenhado do que com quinze microsserviços mal delimitados.

E aí chegamos nos microsserviços de verdade: cada serviço implantável, escalável e substituível de forma independente, com seu próprio armazenamento de dados, se comunicando com os outros por contratos explícitos.

*[indicação de edição: gráfico comparando os três modelos lado a lado, sem indicar hierarquia de "melhor para pior"]*

Agora, como a gente decide onde cortar? Dois conceitos guiam essa decisão. Coesão: o quanto os elementos internos de um componente estão relacionados e mudam juntos. E acoplamento: o quanto um componente depende de detalhes internos de outro. A regra de ouro é: alta coesão dentro, baixo acoplamento fora.

Tem um jeito de colocar número nisso, emprestado da engenharia de componentes de software, proposto pelo Robert Martin. A instabilidade de um componente é I igual a Ce dividido pela soma de Ca mais Ce, onde Ca é o acoplamento aferente — quantos outros dependem dele — e Ce é o acoplamento eferente — de quantos outros ele depende. Se o estoque da NexaOrder é consultado por pedidos, pagamento e um painel administrativo, então Ca é 3. E se o estoque só depende do catálogo para validar categoria de item, Ce é 1. Fazendo a conta: I igual a 1 dividido por 3 mais 1, que dá 0,25. Um valor baixo assim sugere um serviço relativamente estável — bom para concentrar regra central de domínio, porque mudanças nele afetam bastante gente. Isso não substitui julgamento de negócio, mas transforma um "acho que esse serviço está muito enredado" em algo que o time pode discutir com dados.

*[indicação de edição: quadro mostrando o cálculo passo a passo de I = Ce / (Ca + Ce) com os números do estoque]*

Além de coesão e acoplamento, o Domain-Driven Design nos dá dois conceitos valiosos. Contexto delimitado: a fronteira dentro da qual um modelo de domínio tem um significado consistente. E capacidade de negócio: algo que a organização faz para gerar valor, tipo "gerenciar estoque" ou "processar pagamento", independentemente de como isso é implementado.

Aqui vai um exemplo bem concreto da NexaOrder. A palavra "item" significa coisas diferentes dependendo de quem fala. Para o catálogo, item é uma descrição comercial, com preço, fotos, categoria. Para o estoque, item é uma quantidade física, com número de série, localização física em um depósito. Se a gente trata isso como se fosse o mesmo modelo de dados compartilhado, qualquer mudança no significado de "item" para o catálogo pode quebrar silenciosamente o controle de estoque. Reconhecer que são contextos delimitados diferentes autoriza — e recomenda — que cada serviço mantenha seu próprio modelo.

E capacidade de negócio ajuda a calibrar o tamanho certo de um serviço — nem grande demais, nem pequeno demais. Pensa em "processar pagamento" como uma capacidade de negócio única e coesa: autorizar, capturar, estornar, tudo faz parte da mesma responsabilidade, e provavelmente deveria viver no mesmo serviço. Já "gerenciar estoque" e "calcular frete de expedição" são capacidades diferentes, mesmo que estejam próximas no fluxo do pedido — uma trata de quantidade disponível, a outra de logística de entrega. Se a NexaOrder colocasse as duas dentro do mesmo serviço só porque "andam juntas no fluxo", a coesão interna cairia: mudanças em regra de frete passariam a exigir revisão de código que também mexe com controle de estoque, sem necessidade real. O teste prático que eu sugiro: pergunte "se essa capacidade mudasse de fornecedor, de regra de negócio ou de equipe responsável amanhã, o resto do serviço precisaria mudar junto?" Se a resposta for não, provavelmente você já tem uma capacidade de negócio separável, candidata a virar sua própria fronteira de serviço.

### Demonstração, exemplo e estudo de caso

Vamos aplicar isso na prática, olhando para dentro da NexaOrder.

*[indicação de edição: tela dividida mostrando, de um lado, a arquitetura atual com banco compartilhado, e do outro, a proposta de dados por serviço]*

O princípio de dados por serviço diz: cada serviço tem seu próprio armazenamento, ponto. Nenhum outro serviço acessa esse armazenamento diretamente, nem para leitura. Toda interação passa por um contrato explícito — API, mensagem ou evento, que a gente vai ver com detalhe na próxima aula. Sim, isso elimina a conveniência de um JOIN direto entre tabelas de serviços diferentes. Mas esse custo é deliberado: sem essa separação, uma mudança de esquema em um serviço quebra silenciosamente outros serviços, e a "fronteira do serviço" deixa de existir na prática, mesmo que exista repositório de código separado — que foi exatamente o erro que a NexaOrder cometeu.

Agora, quando um cliente externo — o app do cliente, por exemplo — precisa de dados que vêm de vários serviços ao mesmo tempo, a gente não quer que ele converse diretamente com cada um. Isso cria acoplamento entre a topologia interna e o mundo externo. Para isso existe o API Gateway: um ponto de entrada que roteia, agrega respostas de múltiplos serviços numa resposta só — o que a gente chama de composição —, aplica autenticação e limite de taxa. Uma tela de detalhes de pedido, por exemplo, pode precisar de dados de pedidos, estoque e expedição; o gateway consulta os três e devolve uma resposta única, sem que o app precise saber que existem três serviços por trás daquela tela.

Só um cuidado importante: o gateway não pode virar depósito de regra de negócio. Quando isso acontece, ele vira um novo monólito escondido atrás de uma fachada de microsserviços.

Um sinal claro de que a fronteira está no lugar errado é o que chamamos de comunicação excessivamente conversacional: um único caso de uso do cliente dispara dezenas de chamadas remotas entre serviços para ser concluído. Se isso está acontecendo, provavelmente duas responsabilidades fortemente relacionadas foram separadas sem necessidade.

*[indicação de edição: animação mostrando uma requisição do cliente disparando uma cascata excessiva de chamadas entre serviços internos]*

Um jeito adicional de perceber se a fronteira de serviço está alinhada com a organização é olhar para a estrutura dos próprios times. Há uma observação antiga, conhecida como Lei de Conway, que diz que a arquitetura de um sistema tende a espelhar a estrutura de comunicação da organização que o constrói. Se a NexaOrder tem um time só cuidando de pedidos e estoque juntos, mas a arquitetura já separa os dois em serviços distintos, é bem provável que, na prática, as duas partes continuem evoluindo em conjunto — porque é a mesma equipe decidindo as duas coisas ao mesmo tempo, revisando o mesmo código nas mesmas reuniões. Isso não invalida a separação técnica, mas é um sinal de que, se a intenção é ganhar autonomia real, a estrutura de times também pode precisar acompanhar a fronteira de serviços — e não só o inverso.

### Aplicação profissional

No dia a dia, esse raciocínio aparece toda vez que você participa de uma discussão sobre "vamos quebrar esse serviço em dois" ou "vamos juntar esses dois serviços". Alguns sinais para você levar para uma retrospectiva de arquitetura: implantações que precisam ser coordenadas no mesmo horário; qualquer mudança de esquema em um serviço quebrando outro; um incidente exigindo presença de praticamente todo o time; serviços compartilhando tabelas, filas ou segredos sem contrato explícito; topologia de chamadas profunda e conversacional para um único caso de uso; e times que não conseguem testar ou implantar sem depender de outro time no mesmo instante.

Nenhum desses sinais isolado é prova definitiva. Mas se você encontrar vários ao mesmo tempo na sua arquitetura, provavelmente a divisão física em repositórios ou processos não produziu autonomia real — só produziu mais rede para atravessar.

Deixa eu te dar um exemplo de como esse raciocínio aparece numa reunião de verdade. Imagina que alguém no time propõe: "vamos juntar catálogo e estoque num serviço só, porque eles sempre mudam próximos um do outro". Antes de concordar ou discordar de cabeça, vale aplicar o que vimos: qual é o Ca e o Ce de cada um hoje? Se o catálogo é consultado por cinco outros serviços — pedidos, busca, recomendação, painel administrativo e o próprio estoque — e depende só de um serviço de precificação, o Ca dele é alto e o Ce é baixo, o que dá uma instabilidade baixa: um serviço central, que muitos dependem, e que deveria mudar com cautela. Já o estoque, consultado por pedidos e pagamento, mas dependente do catálogo e de um serviço externo de logística, tem instabilidade mais alta. Juntar os dois significa colocar, no mesmo processo e no mesmo ciclo de implantação, um componente que quer ser estável e outro que muda com mais frequência — na prática, isso tende a forçar o catálogo a acompanhar o ritmo de mudança do estoque, prejudicando justamente os cinco consumidores que dependem da sua estabilidade. Esse tipo de conta simples, feita em cinco minutos numa reunião, evita decisões tomadas só por impressão.

E, como em toda decisão arquitetural desta disciplina, uma boa decisão de fronteira explicita requisito, decisão, compromisso e evidência. Requisito: eliminar coordenação de implantação entre pedidos e estoque. Decisão: separar o modelo de item de catálogo do modelo de unidade em estoque, cada um com seu armazenamento. Compromisso: consultas que hoje usam JOIN local vão precisar de composição ou réplicas assíncronas, com atraso de propagação. Evidência: medir quantas implantações precisaram de coordenação simultânea antes e depois da mudança.

### Fechamento

Recapitulando: monólito, monólito modular e microsserviços são opções válidas, e a escolha depende de requisito, não de moda. Coesão alta dentro, acoplamento baixo fora. Contexto delimitado e capacidade de negócio revelam onde um mesmo termo muda de significado. Dados por serviço evita acoplamento escondido atrás de um banco compartilhado. E toda fronteira boa nasce de um raciocínio explícito sobre requisito, decisão, compromisso e evidência — não de uma regra genérica sobre microsserviços.

Na próxima videoaula, a gente vai resolver um problema que aparece justamente quando os serviços ficam bem delimitados: como eles conversam entre si sem ficar em fila, esperando resposta uns dos outros. Vamos entrar em arquitetura orientada a eventos. Até lá!

*[indicação de edição: encerrar com card de transição "Próxima aula: arquitetura orientada a eventos"]*

**Fontes e links de mídia:**

- DRAGONI, N. et al. Microservices: yesterday, today, and tomorrow. In: *Present and Ulterior Software Engineering*. Cham: Springer, 2017. DOI: 10.1007/978-3-319-67425-4_12. Trecho sugerido: seção introdutória sobre a evolução histórica de monólitos a microsserviços.
- LEWIS, James; FOWLER, Martin. Microservices. *martinfowler.com*, 2014. Disponível em: <https://martinfowler.com/articles/microservices.html>. Trecho sugerido: seção "Componentization via Services".
- NEWMAN, Sam. *Building Microservices*. 2. ed. Sebastopol: O'Reilly Media, 2021.

---

## Roteiro da Videoaula 10 — “Parar de esperar: como eventos desacoplam o ciclo do pedido”

**Vínculo com o plano de aprendizagem:** Unidade 3, Aula 10 — Arquitetura orientada a eventos.

**Objetivo da videoaula:** capacitar o estudante a projetar fluxos de comunicação assíncrona usando eventos de domínio, tópicos, partições, grupos de consumidores e semânticas de entrega apropriadas a cada consumidor.

### Abertura contextualizada

Bem-vindo de volta! Na aula passada, a gente organizou a NexaOrder em serviços com fronteiras mais claras: pedidos, estoque, pagamento e expedição, cada um com seu próprio banco de dados. Só que ainda tem um problema escondido na forma como eles se falam.

*[indicação de edição: diagrama do fluxo atual, com setas síncronas em cadeia entre os quatro serviços]*

Hoje, o fluxo de checkout funciona assim: pedidos chama estoque de forma síncrona e espera resposta; estoque chama pagamento de forma síncrona e espera resposta; pagamento chama expedição de forma síncrona e espera resposta. Parece razoável, até você perceber a consequência: se qualquer um desses serviços estiver lento, a cadeia inteira fica lenta. E se qualquer um estiver indisponível — mesmo que seja só o serviço de expedição, que nem precisa responder imediatamente — o pedido inteiro falha.

Repara na ironia: o serviço de expedição normalmente só precisa agir minutos ou horas depois da aprovação do pagamento, já que preparar uma embalagem física não é instantâneo. Mesmo assim, na cadeia síncrona atual, uma instabilidade passageira nesse serviço consegue derrubar a confirmação de um pedido cujo pagamento já foi aprovado com sucesso. Isso é acoplamento temporal desnecessário: etapas que não precisam de resposta imediata estão, mesmo assim, bloqueando etapas anteriores que já deveriam poder seguir em frente.

Essa aula é sobre uma alternativa: tratar essas etapas como reações a fatos que já aconteceram, e não como uma corrente de chamadas bloqueantes.

### Desenvolvimento conceitual

Primeiro, vamos separar três tipos de mensagem que costumam ser confundidos. Comando: uma solicitação para que algo aconteça, endereçada a um destinatário específico, que pode aceitar ou recusar — por exemplo, "reserve uma unidade do item X". Evento de domínio: o registro de um fato que já ocorreu, publicado sem destinatário específico — "pedido 4021 criado", "pagamento 4021 aprovado". E notificação: um aviso leve, sem os dados completos, convidando quem estiver interessado a buscar mais informação.

Por que essa distinção importa? Comando cria acoplamento direto — quem envia sabe quem deve receber e espera confirmação. Evento de domínio favorece baixo acoplamento — quem publica não sabe, e não precisa saber, quem vai consumir. A NexaOrder vai tratar "pedido criado", "estoque reservado", "pagamento aprovado" e "pedido expedido" como eventos de domínio.

Um erro comum de quem está começando com eventos é confundir os dois conceitos e nomear um comando disfarçado de evento, tipo "reservar-estoque", como se fosse um fato consumado. Isso quebra a expectativa de quem consome o "evento": um serviço que lê "reservar-estoque" pode se sentir no direito de recusar a reserva, mas o nome sugere que a reserva já deveria ter acontecido. Um jeito simples de testar se você nomeou corretamente: eventos de domínio quase sempre são descritos no particípio passado — "criado", "reservado", "aprovado", "expedido" — porque descrevem algo que já ocorreu; comandos são descritos no imperativo — "criar", "reservar", "aprovar" — porque pedem que algo aconteça.

*[indicação de edição: tabela comparativa comando / evento de domínio / notificação, com um exemplo da NexaOrder para cada]*

Agora, como esses eventos circulam? Uma plataforma de transmissão de eventos organiza tudo em tópicos — canais nomeados por tipo de evento. Produtores publicam eventos num tópico. Consumidores leem esses eventos, e, olha que interessante: sem remover a mensagem para os outros, o que permite que múltiplos serviços processem o mesmo evento de forma independente.

Para escalar, um tópico é dividido em partições. Cada partição mantém uma sequência ordenada e imutável de eventos, com um deslocamento crescente. Um evento é direcionado a uma partição com base numa chave — por exemplo, o identificador do pedido — garantindo que todos os eventos daquele pedido caiam na mesma partição.

E aqui vai um ponto que costuma confundir: a plataforma garante ordem dentro de uma partição, não entre partições diferentes. Se todos os eventos do pedido 4021 usam a chave "4021", eles chegam na mesma partição, na ordem certa: criado, estoque reservado, pagamento aprovado, expedido. Eventos de pedidos diferentes podem ficar fora de ordem relativa entre si, e geralmente tudo bem, porque são agregados de negócio distintos. Mas se a NexaOrder tivesse escolhido particionar por região geográfica em vez de por identificador de pedido, dois eventos do mesmo pedido processados em regiões diferentes poderiam cair em partições distintas — e aí, sim, chegariam fora de ordem.

*[indicação de edição: animação mostrando eventos do pedido 4021 caindo sempre na mesma partição por causa da chave, e eventos de outros pedidos se espalhando por partições diferentes]*

Um grupo de consumidores é um conjunto de instâncias que dividem entre si as partições de um tópico, de modo que cada partição fique atribuída a exatamente uma instância por vez. Isso permite escalar horizontalmente: com um tópico de seis partições e um grupo de três consumidores, cada instância processa, em média, duas partições. E grupos diferentes são independentes: o grupo que atualiza o painel operacional e o grupo que dispara e-mail de confirmação podem consumir o mesmo tópico, cada um no seu ritmo, sem interferir um no outro.

E o que acontece quando uma instância de um grupo de consumidores falha? A plataforma redistribui as partições que estavam com ela entre as instâncias remanescentes do mesmo grupo — um processo chamado de rebalanceamento. Se o grupo de três instâncias que processa o tópico de seis partições perde uma instância, as duas restantes passam a dividir as seis partições entre si, cada uma assumindo três. Isso significa que o serviço continua funcionando, mas com throughput reduzido por instância até que uma nova réplica seja adicionada — o mesmo raciocínio de redundância sem ponto único de falha que vimos lá na Aula 1, agora aplicado à camada de consumo de eventos.

### Demonstração, exemplo e estudo de caso

Vamos fazer uma conta de dimensionamento juntos. Suponha que o tópico de eventos de pedido da NexaOrder precisa sustentar uma taxa de pico de 1200 eventos por segundo, e cada consumidor processa, de forma sustentável, 150 eventos por segundo. O número mínimo de partições necessário é P igual ao teto de lambda de pico dividido por C de consumidor: 1200 dividido por 150, que dá exatamente 8.

*[indicação de edição: cálculo aparecendo na tela, com destaque para o resultado P = 8]*

Repara numa coisa importante: se a equipe resolver adicionar um nono consumidor ao grupo achando que vai acelerar ainda mais o processamento, isso não vai adiantar nada, porque não existe uma nona partição para atribuir a ele. A instância fica ociosa. O número de partições é um limite estrutural de paralelismo, e por isso deve ser definido com folga em relação à carga de pico esperada — não só para o dia de hoje, mas pensando no crescimento.

Agora, uma propriedade que diferencia essa arquitetura de uma fila tradicional: retenção. Numa fila comum, a mensagem some depois de consumida. Numa plataforma de eventos, as mensagens ficam retidas por um período configurável, independentemente de já terem sido lidas. Isso permite reprocessamento: um consumidor novo pode começar do início da retenção e reconstruir um estado inteiro a partir do histórico. Se a NexaOrder encontrar um bug no serviço que alimenta o painel de vendas, ela pode simplesmente reconstruir esse painel do zero, reprocessando os eventos já publicados — sem precisar de um mecanismo de exportação separado.

Vale pensar em retenção como uma decisão de custo e utilidade, não como "quanto mais, melhor" de forma automática. Reter eventos por sete dias, por exemplo, permite que a equipe da NexaOrder corrija um bug percebido numa segunda-feira e reprocesse tudo desde a semana anterior. Reter por apenas algumas horas praticamente elimina essa possibilidade, mas custa menos armazenamento. Reter indefinidamente transforma o próprio tópico em uma espécie de registro histórico completo do negócio — o que tem valor para auditoria, mas também tem custo de armazenamento crescente ao longo do tempo. A escolha do período de retenção, então, é uma decisão arquitetural como qualquer outra: qual o requisito de auditoria e recuperação, qual o custo de manter os dados retidos, e qual o compromisso aceitável entre os dois.

E, claro, entrega de mensagem está sujeita às mesmas falhas parciais que vimos na Aula 4. Três semânticas descrevem o resultado. At-most-once: cada evento é entregue zero ou uma vez, nunca duplicado, mas pode se perder — acontece quando o consumidor confirma antes de terminar de processar. At-least-once: cada evento é entregue uma ou mais vezes, nunca se perde, mas pode duplicar — acontece quando o consumidor só confirma depois de processar, e uma falha entre processar e confirmar gera reentrega. E exactly-once: cada evento produz exatamente um efeito observável, mesmo com reentregas — normalmente combinando at-least-once com deduplicação, o mesmo princípio de idempotência que vimos na Aula 8.

*[indicação de edição: três linhas do tempo lado a lado ilustrando perda, duplicação e efeito único]*

Na prática, a maioria das plataformas amplamente usadas entrega garantia forte de at-least-once por padrão, e cabe ao consumidor alcançar um comportamento efetivamente único. Por isso, o consumidor de "pagamento aprovado" da NexaOrder verifica se aquele identificador de evento já foi processado antes de disparar a expedição — absorvendo duplicação sem duplicar efeito.

Por fim, um cuidado de longo prazo: evolução de esquema. Eventos publicados hoje podem ser lidos por serviços implantados semanas depois. Mudanças aditivas — campo novo opcional — costumam ser seguras, preservando compatibilidade retroativa e prospectiva. Remover ou renomear um campo existente costuma quebrar consumidores antigos, exigindo uma estratégia explícita de transição. Um exemplo simples: se a NexaOrder decide adicionar um campo `canal_venda` ao evento "pedido criado" — para diferenciar vendas feitas pelo aplicativo, pelo site e por um parceiro comercial —, consumidores antigos que ainda não conhecem esse campo simplesmente o ignoram e continuam funcionando normalmente. Mas se a decisão fosse renomear `valor_total` para `valor_liquido`, sem qualquer transição, qualquer consumidor que ainda espera o nome antigo passaria a interpretar o pedido como se não tivesse valor algum — um erro silencioso, que só aparece quando alguém percebe que o painel financeiro está zerado.

### Aplicação profissional

No trabalho, você vai usar exatamente esse raciocínio ao desenhar um novo fluxo assíncrono: qual é o evento de domínio certo para publicar? Qual chave garante a ordenação que eu preciso? Quantas partições eu preciso para o pico esperado? Quantos grupos de consumidores diferentes vão ler esse tópico, e cada um precisa de qual semântica de entrega?

Essa última pergunta merece atenção especial, porque nem todo consumidor precisa do mesmo nível de garantia. O consumidor que dispara e-mail de confirmação pode tolerar, ocasionalmente, um e-mail que não chega a ser enviado — o cliente vê a confirmação na tela mesmo assim, então uma semântica mais simples, próxima de at-most-once, é aceitável. Já o consumidor que debita o estoque não pode tolerar duplicação, porque duas reservas do mesmo pedido consumiriam duas unidades em vez de uma; esse consumidor precisa de deduplicação explícita para alcançar, na prática, um efeito exactly-once. Perceba que a decisão não é "qual semântica a plataforma oferece", e sim "qual comportamento cada consumidor específico precisa garantir, dado o que ele faz com o evento".

Reunindo tudo na NexaOrder: pedidos recebe um comando síncrono do cliente, "criar pedido", e publica o evento "pedido criado". Estoque consome esse evento e publica "estoque reservado" ou "estoque indisponível". Pagamento consome "estoque reservado" e publica "pagamento aprovado" ou "pagamento recusado". Expedição consome "pagamento aprovado" e publica "pedido expedido". Nenhum desses serviços chama o seguinte de forma síncrona e bloqueante — cada um reage a fatos publicados, no seu próprio ritmo.

Isso conecta diretamente com algo que vimos lá na Unidade 2, quando falamos de sagas coreografadas: uma sequência de passos de negócio coordenada sem um orquestrador central, cada serviço reagindo ao evento publicado pelo anterior e publicando seu próprio evento de conclusão. O fluxo de pedidos que acabamos de desenhar é, na prática, uma saga coreografada: se o pagamento for recusado, o serviço de pagamento publica "pagamento recusado", e cabe ao serviço de estoque — ou a um consumidor dedicado a compensações — reagir a esse evento liberando a reserva feita anteriormente. A arquitetura orientada a eventos não é só uma técnica de comunicação; ela é o mecanismo que viabiliza, na prática, o padrão de sagas que discutimos antes de conhecer tópicos, partições e grupos de consumidores.

### Fechamento

Recapitulando: comandos, eventos de domínio e notificações têm propósitos e acoplamentos diferentes. Tópicos e partições organizam eventos, com ordem garantida só dentro da partição. A chave de particionamento decide o que fica ordenado junto. Grupos de consumidores escalam o processamento, limitados pelo número de partições. Retenção permite reprocessamento. E at-most-once, at-least-once e exactly-once descrevem compromissos diferentes entre perda e duplicação.

Na próxima aula, a gente sai do desenho lógico e entra na camada de execução: como esses serviços rodam de verdade, em contêineres, orquestrados pelo Kubernetes. Até lá!

*[indicação de edição: card de transição "Próxima aula: contêineres, Kubernetes e reconciliação"]*

**Fontes e links de mídia:**

- KLEPPMANN, Martin. *Designing Data-Intensive Applications*. Sebastopol: O'Reilly Media, 2017. Trecho sugerido: capítulo sobre processamento de fluxos (*stream processing*) e semânticas de entrega.
- Apache Kafka Documentation. Disponível em: <https://kafka.apache.org/documentation/>. Trecho sugerido: seção sobre design de tópicos e partições.

---

## Roteiro da Videoaula 11 — “Quem recriou essa instância? Dentro do laço de reconciliação do Kubernetes”

**Vínculo com o plano de aprendizagem:** Unidade 3, Aula 11 — Contêineres, Kubernetes e reconciliação.

**Objetivo da videoaula:** capacitar o estudante a interpretar os objetos centrais do Kubernetes, compreender o laço de reconciliação e reconhecer seus limites diante de defeitos recorrentes.

### Abertura contextualizada

Oi, de novo! Vamos contar uma história rápida. É madrugada, tráfego alto na NexaOrder, e uma instância do serviço de pagamento trava e para de responder. Minutos depois, sem qualquer intervenção humana, uma nova instância aparece no lugar, assume o tráfego, e o incidente quase passa despercebido pelos usuários.

*[indicação de edição: simulação em tela de um painel de monitoramento mostrando uma instância ficando vermelha e, logo depois, uma nova instância verde aparecendo no lugar]*

A equipe de plantão fica intrigada: quem decidiu recriar essa instância? Como o sistema sabia que ela deveria existir? E, pergunta mais importante ainda: e se a causa do travamento for um defeito que volta a acontecer a cada reinício? Essa aula é sobre entender esse mecanismo de recuperação automática — o que ele resolve e o que ele não resolve.

### Desenvolvimento conceitual

Vamos começar pelos blocos básicos. Uma imagem de contêiner é um pacote autocontido com o código da aplicação, suas dependências, e instruções de execução, construído em camadas imutáveis. Um contêiner é uma instância em execução dessa imagem, isolada em termos de processo, sistema de arquivos e, em geral, rede — mas compartilhando o núcleo do sistema operacional do hospedeiro, diferente de uma máquina virtual completa.

E aqui entra um princípio central: imutabilidade. Em vez de corrigir uma instância em execução, a prática recomendada é publicar uma nova imagem e substituir os contêineres antigos por novos criados a partir dela. Isso elimina aquele clássico "funciona na minha máquina", porque a imagem publicada é exatamente o que roda em produção, sem gambiarra manual depois.

Pensa no contraste com a forma antiga de operar servidores: alguém entra numa máquina em produção, aplica uma correção manual, reinicia um processo, e torce para lembrar de aplicar a mesma correção no próximo servidor. Depois de algumas semanas, ninguém mais sabe ao certo o que cada máquina tem instalado, porque cada uma acumulou pequenos ajustes manuais diferentes — um fenômeno às vezes chamado de "servidor de estimação", tratado como único e insubstituível. Contêineres imutáveis tratam cada instância como descartável: se algo está errado, você não conserta o Pod que já existe, você publica uma imagem corrigida e deixa o laço de reconciliação substituir todas as instâncias antigas por novas, geradas exatamente da mesma receita.

*[indicação de edição: diagrama simples mostrando camadas de uma imagem de contêiner sendo empacotadas]*

O Kubernetes organiza a execução em torno de alguns objetos. Cluster é o conjunto de máquinas gerenciadas como uma unidade. Nó é uma máquina, física ou virtual, que executa contêineres. Pod é a menor unidade implantável — agrupa um ou mais contêineres que compartilham rede e armazenamento local. Deployment declara quantas réplicas de um Pod devem existir e como atualizações são aplicadas ao longo do tempo. E Service expõe um conjunto de Pods sob um endereço estável, mesmo quando Pods individuais são substituídos.

Na NexaOrder, o serviço de pagamento é um Deployment com, digamos, quatro réplicas de um Pod, e um Service estável que os outros serviços usam para chamá-lo, sem precisar conhecer o endereço volátil de cada Pod individual.

Agora, o conceito mais importante da aula: a separação entre estado desejado e estado observado. O usuário não instrui o Kubernetes passo a passo sobre como criar uma instância. Ele declara "eu quero quatro réplicas saudáveis desse Pod" — isso é o estado desejado — e delega ao sistema a responsabilidade de alcançar e manter esse estado, comparando continuamente com o estado observado, que é a condição real do cluster naquele momento.

*[indicação de edição: mostrar na tela um manifesto YAML simplificado com "replicas: 4" e o nome da imagem "nexaorder/pagamento:1.7.0"]*

Um controlador é o processo que observa continuamente esse estado atual, compara com o estado desejado, e age para reduzir a diferença entre os dois. Isso é o laço de reconciliação. Não é uma execução única — é um ciclo que roda indefinidamente, reagindo tanto a mudanças declaradas por humanos quanto a mudanças observadas no ambiente, como a falha de um Pod.

E como o Kubernetes sabe que um Pod não está mais saudável? Não é por mágica: ele depende de sondas configuradas pelo próprio time responsável pelo serviço. Uma sonda de vivacidade, a *liveness probe*, verifica periodicamente se o processo dentro do contêiner ainda responde; se parar de responder, o Kubernetes entende que o Pod não está mais no estado desejado e o substitui. Uma sonda de prontidão, a *readiness probe*, verifica se o Pod já está pronto para receber tráfego — útil logo após a inicialização, quando o processo já está de pé, mas talvez ainda esteja carregando configuração ou aquecendo uma conexão com o banco. Um Pod que falha na sonda de prontidão continua existindo, mas é temporariamente removido da lista de destinos válidos de um Service, sem ser recriado. Essas sondas são o elo entre "o que está acontecendo de fato dentro do contêiner" e "o que o laço de reconciliação consegue observar" — sem elas configuradas corretamente, o Kubernetes só percebe uma falha grave o suficiente para derrubar o processo inteiro, e não seria capaz de perceber um serviço que está de pé, mas incapaz de processar qualquer requisição.

### Demonstração, exemplo e estudo de caso

Voltando à nossa história do início: quando a instância de pagamento trava, o controlador de Deployment observa que só três dos quatro Pods desejados estão saudáveis, e cria um novo Pod para restaurar o número declarado. É exatamente esse comportamento que produz a recuperação automática que a equipe de plantão percebeu, sem ninguém digitar um comando manual.

*[indicação de edição: diagrama circular do laço de reconciliação — observar, comparar, agir — voltando ao início]*

Só que aqui vem o ponto crítico da aula: esse laço restaura a quantidade e o estado de execução declarados. Ele não restaura a causa raiz de uma falha recorrente. Se aquele Pod trava repetidamente por um defeito de código sob determinada condição de carga, o Kubernetes vai continuar recriando ele indefinidamente — um padrão conhecido como reinício em loop —, e isso pode acabar mascarando um problema que precisa de diagnóstico humano. Recuperação automática é sinal de disponibilidade. Não é prova de correção. Isso é o mesmo raciocínio que a gente já viu lá na Aula 4, quando falamos de timeout como decisão, e não como prova de falha.

Vamos ver como o resto da infraestrutura sustenta essa recuperação. Como Pods são substituídos com frequência e ganham endereços internos voláteis, os serviços não podem apontar diretamente para um Pod específico. O Service resolve isso associando um nome estável a um conjunto de Pods selecionados por rótulo, distribuindo o tráfego entre os Pods saudáveis disponíveis — descoberta de serviço e balanceamento de carga, juntos. Quando o estoque da NexaOrder precisa falar com pagamento, ele conversa com o nome estável do Service, e o Kubernetes decide para qual réplica saudável rotear, mesmo que os Pods por trás tenham sido recriados dezenas de vezes naquele dia.

E contêineres imutáveis não devem embutir configuração ou credenciais na própria imagem. O Kubernetes separa isso em ConfigMaps, para configuração não sensível, e Secrets, para dados sensíveis, injetados no Pod em tempo de execução. Para dados que precisam sobreviver à substituição de um Pod — já que o armazenamento local de um Pod é efêmero por padrão —, existe armazenamento persistente, vinculado ao ciclo de vida da aplicação, não a um Pod específico.

Outro detalhe que costuma passar despercebido em quem está começando: cada contêiner pode declarar solicitações e limites de recursos — quanto de CPU e memória ele espera usar normalmente, e qual o teto que não pode ultrapassar. Isso não é burocracia; é o que permite ao Kubernetes decidir, com informação, em qual nó colocar cada novo Pod durante a reconciliação, evitando que um nó fique sobrecarregado com contêineres famintos por recursos enquanto outro fica ocioso. Se o serviço de pagamento da NexaOrder declara uma solicitação de meio núcleo de CPU e um limite de um núcleo inteiro, o Kubernetes reserva, no mínimo, aquele meio núcleo para ele em algum nó com capacidade disponível — e, se o Pod tentar ultrapassar o limite superior de forma persistente, pode ser contido ou até reiniciado, dependendo do tipo de recurso.

*[indicação de edição: diagrama de um Service distribuindo tráfego entre Pods saudáveis, com um Pod recém-recriado ao fundo]*

Agora, uma conta de escalonamento. O Horizontal Pod Autoscaler ajusta o número de réplicas com base em métrica observada, geralmente utilização de CPU. A fórmula, de forma simplificada, é: N desejado igual ao teto de N atual vezes U atual dividido por U alvo. Se o Deployment de pagamento tem 4 réplicas atuais, utilização observada de 85%, e o alvo configurado é 60%, fazemos: 4 vezes 85 dividido por 60, que dá 5,67, arredondado para cima, 6. O autoescalonador ajustaria para seis réplicas, e o laço de reconciliação criaria os dois Pods que faltam.

*[indicação de edição: cálculo aparecendo na tela passo a passo, com destaque para o resultado final, 6 réplicas]*

E, quando uma nova versão é publicada, uma atualização gradual substitui réplicas antigas por novas de forma incremental, respeitando limites configuráveis de quantas réplicas podem ficar indisponíveis ou excedentes durante a transição — para que a atualização não derrube a capacidade total do serviço.

Vamos fixar isso com um exemplo numérico rápido. Se o Deployment de pagamento tem 6 réplicas e a atualização é configurada para permitir, no máximo, 1 réplica indisponível e 1 réplica excedente durante a transição, o Kubernetes primeiro cria 1 Pod novo com a versão nova — chegando a 7 Pods no total, 6 antigos e 1 novo —, espera esse Pod passar na sonda de prontidão, depois remove 1 Pod antigo — voltando a 6 no total, agora 5 antigos e 1 novo — e repete esse ciclo até que todos os 6 Pods estejam na versão nova. Em nenhum momento a capacidade saudável cai abaixo de 5 réplicas nem sobe além de 7, dentro dos limites configurados. Se algo der errado no meio do processo — por exemplo, o Pod novo falhar repetidamente na sonda de prontidão —, a atualização gradual pode ser interrompida automaticamente antes de substituir todas as réplicas, evitando que um defeito na versão nova derrube o serviço inteiro de uma vez.

### Aplicação profissional

No dia a dia de quem opera esse tipo de plataforma, essa distinção entre "o Kubernetes recuperou sozinho" e "o problema foi resolvido de verdade" é essencial. Se você é responsável por um serviço e percebe reinícios repetidos, isso não é motivo para relaxar — é motivo para investigar. Pergunte: o que, além de "o serviço está no ar", eu deveria monitorar para perceber esse padrão? Um Pod que trava sob carga alta e volta sozinho está, de fato, resolvido do ponto de vista do negócio? E: como eu configuro um limite de tentativas de reinício que force intervenção humana, em vez de tentativas indefinidas?

Vale também comentar um erro comum de quem está começando a operar Kubernetes: confundir "o painel mostra tudo verde" com "o sistema está saudável". O painel geralmente reflete o que as sondas reportam, e sondas mal configuradas — por exemplo, uma sonda de vivacidade que só verifica se a porta de rede está aberta, sem checar se o processo realmente consegue atender a uma requisição de negócio — podem mostrar verde para um Pod que já não processa pagamento nenhum. Configurar sondas que reflitam a saúde real do serviço, e não apenas a existência do processo, é parte do trabalho de quem projeta o Deployment, tanto quanto escolher o número de réplicas.

### Fechamento

Recapitulando: imagens imutáveis eliminam divergência entre ambientes. Cluster, nó, Pod, Deployment e Service organizam a execução. O laço de reconciliação compara estado desejado e observado continuamente. Recuperação automática restaura quantidade e execução, não causa raiz. Services garantem descoberta e balanceamento estáveis. ConfigMaps, Secrets e armazenamento persistente separam configuração e dados do ciclo de vida da imagem. E escalonamento automático mais atualização gradual ajustam capacidade e versão sem interromper o serviço.

E fica um convite para reflexão antes da próxima aula: se a recuperação automática do Kubernetes resolve tão bem a disponibilidade, o que ainda falta para que a NexaOrder confie de verdade em quem está do outro lado de cada chamada entre serviços? Disponibilidade não é a mesma coisa que confiabilidade de comunicação — e é exatamente esse assunto que fecha a nossa unidade.

Na próxima e última aula desta unidade, a gente vai proteger essa comunicação toda: identidade de serviço, autenticação, TLS mútuo e confiança zero. Até lá!

*[indicação de edição: card de transição "Próxima aula: segurança e comunicação confiável entre serviços"]*

**Fontes e links de mídia:**

- BURNS, B. et al. Borg, Omega, and Kubernetes. *Communications of the ACM*, 2016. DOI: 10.1145/2890784. Trecho sugerido: seção sobre lições operacionais do Borg e do Omega que moldaram o Kubernetes.
- Kubernetes Documentation. Disponível em: <https://kubernetes.io/docs/>. Trecho sugerido: conceitos de Pods, Deployments e o laço de controle (*controllers*).

---

## Roteiro da Videoaula 12 — “Confiar em quê? Autenticação, TLS mútuo e menor privilégio entre serviços”

**Vínculo com o plano de aprendizagem:** Unidade 3, Aula 12 — Segurança e comunicação confiável entre serviços.

**Objetivo da videoaula:** capacitar o estudante a projetar comunicação autenticada, autorizada e protegida entre serviços, aplicando confiança zero, menor privilégio, TLS mútuo, gestão de segredos e limitação de taxa.

### Abertura contextualizada

Chegamos à última aula da Unidade 3! E ela começa com uma pergunta desconfortável, feita numa revisão de segurança da NexaOrder: nada, hoje, impede que o serviço de expedição chame diretamente o serviço de pagamento e peça um reembolso — mesmo essa não sendo uma operação prevista para ele. A comunicação interna acontece em texto claro dentro do cluster, sem verificação de identidade além do endereço de rede. E, para piorar, a credencial do provedor de pagamento está num arquivo de configuração acessível a qualquer pessoa com acesso ao repositório de código.

*[indicação de edição: ilustração de um "alarme" visual destacando a chamada indevida de expedição para pagamento]*

Nesta aula, a gente vai tratar de confiabilidade num sentido mais amplo do que só "o serviço está no ar". Confiar que uma mensagem vem de quem diz que vem, que ela não foi alterada no caminho, que cada serviço só pode fazer o que é explicitamente permitido, e que segredo não vaza por conveniência operacional.

Essa é, propositalmente, a última aula da unidade, e não por acaso. Depois de desenhar fronteiras de serviço, comunicação por eventos e execução orquestrada, faltava fechar o círculo com a pergunta que atravessa tudo isso: será que essa arquitetura, tecnicamente elegante, resistiria a alguém tentando explorá-la de forma maliciosa? Serviços, eventos e Kubernetes resolvem problemas de organização, desempenho e disponibilidade — mas nenhum deles, sozinho, resolve o problema de confiança entre as partes.

### Desenvolvimento conceitual

Vamos começar pelo modelo mental. Em arquiteturas tradicionais, a segurança de rede costuma se apoiar em perímetro: tudo dentro da rede interna é considerado relativamente confiável, e o esforço se concentra na borda. Esse modelo fica frágil quando você tem dezenas de serviços, vários times, múltiplos ambientes de nuvem — porque um único componente comprometido dentro do perímetro ganha acesso amplo demais.

O modelo de confiança zero parte do oposto: nenhuma requisição é confiável só por vir de dentro da rede interna. Cada serviço tem uma identidade verificável — normalmente um certificado ou token criptográfico associado a ele, não só ao endereço de rede — e toda comunicação, mesmo entre serviços do mesmo cluster, é autenticada e autorizada explicitamente, como se estivesse cruzando uma fronteira não confiável. Esse é o modelo formalizado pela publicação especial do NIST sobre arquitetura de confiança zero, que é uma das nossas referências desta aula.

*[indicação de edição: diagrama comparando o modelo de perímetro — "castelo com muralha" — e o modelo de confiança zero — verificação em cada porta interna]*

Duas perguntas diferentes, que costumam ser confundidas: autenticação responde "quem está fazendo essa requisição?"; autorização responde "o que essa identidade pode fazer?". Uma não substitui a outra — um serviço pode estar corretamente autenticado e, mesmo assim, não ter autorização para uma operação específica.

E o princípio do menor privilégio: cada identidade recebe só as permissões estritamente necessárias para sua função, nada além. Aplicando à NexaOrder: o serviço de expedição deveria ser autenticado como "expedição" e autorizado só a consultar status de pedido e confirmar envio — sem qualquer permissão sobre reembolso do serviço de pagamento, mesmo que a rede, tecnicamente, deixasse a chamada passar.

Vale reforçar por que isso importa tanto especificamente em sistemas distribuídos, e não só em segurança de aplicação de um jeito genérico. Num sistema centralizado, um "excesso de permissão" costuma ficar contido dentro de um processo só. Num sistema distribuído com dezenas de serviços, uma identidade com privilégio além do necessário se torna um caminho de propagação: se o serviço de expedição for comprometido — por uma dependência desatualizada, por exemplo — e ele tiver permissão de reembolso que nunca deveria ter, o dano do incidente deixa de estar contido em "expedição parou de funcionar" e passa a ser "dinheiro saindo indevidamente da conta de pagamento". Cada permissão concedida além do necessário multiplica o raio de impacto possível de qualquer comprometimento futuro, mesmo que hoje pareça inofensiva.

### Demonstração, exemplo e estudo de caso

Vamos ver como isso vira mecanismo concreto. TLS protege dados em trânsito contra leitura e alteração por terceiros, usando criptografia entre as duas pontas. Em comunicação interna entre serviços, é cada vez mais comum usar TLS mútuo — mTLS — onde as duas partes, não só o servidor como numa conexão web comum, apresentam certificado e verificam a identidade uma da outra antes de trocar dados. Numa arquitetura com mTLS bem configurado, o serviço de pagamento só aceita conexão de um chamador cujo certificado comprove identidade autorizada. Isso torna inviável que um serviço não autenticado — ou um invasor que conseguiu acesso à rede interna — simplesmente inicie uma conexão válida por estar na mesma rede.

*[indicação de edição: diagrama comparando chamada em texto claro sem verificação e chamada com TLS mútuo, certificado em ambas as pontas]*

E credencial, chave de API, certificado — chamamos isso de segredo — não deveria estar embutido em imagem de contêiner, em arquivo de configuração versionado, ou em variável de ambiente definida à mão. A prática recomendada é usar um sistema dedicado de gestão de segredos, que controla acesso, registra auditoria e permite rotação — a substituição programada de uma credencial antiga por uma nova, reduzindo a janela de exposição se um segredo tiver sido comprometido sem que ninguém tenha percebido. Na NexaOrder, a credencial do provedor de pagamento deveria ser injetada no Pod em tempo de execução, nunca lida de um arquivo versionado no repositório — retomando o objeto Secret do Kubernetes que vimos na aula passada.

Pensa na diferença prática entre os dois cenários. Se a credencial estiver embutida na imagem e for comprometida, a única forma de trocá-la é publicar uma nova versão da imagem, testá-la e implantá-la em todos os Pods — um processo que pode levar horas, durante as quais a credencial exposta continua válida. Se a credencial estiver num sistema de gestão de segredos com rotação automatizada, trocá-la pode ser uma operação de segundos, sem precisar publicar nada, porque o Pod já busca o valor atual do segredo no momento em que precisa dele. A diferença entre essas duas velocidades de resposta é, muitas vezes, a diferença entre um incidente de segurança controlado e um incidente que se arrasta por dias.

Implementar tudo isso — autenticação, criptografia, limite de taxa, política de autorização — dentro do código de cada serviço, repetidamente, é caro e sujeito a inconsistência. Por isso existe o padrão de proxy lateral, ou sidecar: um processo auxiliar implantado junto a cada instância de serviço, no mesmo Pod no caso do Kubernetes, que intercepta todo o tráfego de entrada e saída e aplica essas políticas de forma uniforme, sem que o código da aplicação precise implementar nada disso diretamente. Quando esses proxies laterais são coordenados por um plano de controle central que distribui configuração, certificado e política para todos eles, chamamos isso de service mesh.

*[indicação de edição: diagrama de service mesh com os quatro serviços da NexaOrder, cada um com seu proxy lateral, e um plano de controle central]*

Um service mesh permite aplicar mTLS entre todos os serviços da NexaOrder de forma centralizada, sem tocar no código de pedidos, estoque, pagamento e expedição individualmente — e ainda coleta métricas uniformes de comunicação, tema que a gente retoma na próxima unidade, quando falar de observabilidade.

Agora, vamos falar de sobrecarga. Além de autenticar e autorizar, um serviço precisa se proteger de volume excessivo de requisição, seja tráfego legítimo em pico, seja uso indevido. Um mecanismo comum é o balde de fichas: um balde de capacidade C fichas é reabastecido a uma taxa constante r fichas por segundo; cada requisição consome uma ficha; requisição sem ficha disponível é recusada ou colocada em espera.

Vamos fazer a conta. O serviço de pagamento define um balde com capacidade de 50 fichas e taxa de reposição de 20 fichas por segundo. Isso tolera picos curtos de até 50 requisições simultâneas — o estouro, ou burst — e, em regime permanente, sustenta no máximo 20 requisições por segundo, que é a própria taxa de reposição. Se chegar uma rajada de 90 requisições num único segundo, o balde absorve as primeiras 50 na hora, e recusa ou atrasa as 40 restantes até repor novas fichas — protegendo o serviço de uma sobrecarga que comprometeria a disponibilidade para todo mundo, não só para quem gerou a rajada.

*[indicação de edição: animação do balde de fichas enchendo a taxa constante e sendo consumido por requisições, com destaque para a recusa do excedente durante a rajada]*

### Aplicação profissional

Algumas ameaças específicas de sistemas distribuídos merecem atenção especial no seu trabalho: ataque de repetição, quando uma mensagem legítima capturada é reenviada depois para produzir efeito indevido — mitigado por identificador único de operação e janela de validade, retomando idempotência da Aula 8. Movimento lateral, quando um invasor que compromete um serviço de baixo privilégio tenta usar essa posição para alcançar serviços mais sensíveis — mitigado por autenticação mútua e menor privilégio entre todos os serviços, não só na borda. Amplificação por retry, quando política agressiva de repetição transforma indisponibilidade parcial em sobrecarga generalizada, se todo mundo retentar ao mesmo tempo sem backoff. E exposição de segredo por configuração, quando credencial embutida em imagem, log ou repositório fica acessível muito além do escopo pretendido.

Note como essas quatro ameaças conversam com temas que já vimos em unidades anteriores, só que agora sob a ótica de segurança. O ataque de repetição explora exatamente a mesma ausência de identificação de operação que discutimos ao falar de idempotência, só que agora com intenção maliciosa em vez de falha de rede acidental. A amplificação por retry é o mesmo padrão de política de repetição sem *backoff* que vimos na Aula 2, só que agora o gatilho é uma indisponibilidade real de um serviço, e o resultado é uma sobrecarga que se autoalimenta — cada tentativa fracassada gera novas tentativas, que geram mais carga, que geram mais falhas. Isso reforça algo importante: segurança de sistemas distribuídos não é uma disciplina isolada das outras que vimos na disciplina; ela reaproveita e reinterpreta, sob a lente de um adversário ativo, praticamente todos os conceitos de comunicação, falha e resiliência já estudados.

Juntando tudo, uma chamada de pedidos para pagamento na NexaOrder deveria ter, no mínimo: conexão por TLS mútuo com certificado válido dos dois lados; autorização verificando que "pedidos" pode solicitar autorização de pagamento, mas não reembolso; limite de taxa aplicado pelo proxy lateral de pagamento; e um identificador único de operação, permitindo rejeitar repetição indevida.

Repara que nenhum desses quatro elementos, sozinho, resolve o problema todo. TLS mútuo garante identidade e confidencialidade, mas não impede que uma identidade autenticada peça algo fora do seu escopo — para isso existe autorização. Autorização por si só não impede que um chamador legítimo seja usado de forma abusiva por volume — para isso existe limite de taxa. E limite de taxa não impede que uma mensagem legítima capturada seja reaproveitada mais tarde — para isso existe o identificador único de operação. Segurança de comunicação entre serviços distribuídos não é um interruptor único que se liga; é a composição deliberada de várias camadas independentes, cada uma cobrindo um tipo de risco que as outras não cobrem. Essa mentalidade de camadas complementares, e não de uma solução única que resolve tudo, é talvez o aprendizado mais transferível desta aula para o seu dia a dia profissional.

### Fechamento

Recapitulando: confiança zero trata toda comunicação, mesmo interna, como potencialmente não confiável até prova de identidade. Autenticação e autorização respondem perguntas diferentes. TLS mútuo protege dados em trânsito e verifica identidade dos dois lados. Segredos vivem em sistemas dedicados de gestão, com rotação. Proxy lateral e service mesh centralizam política de segurança. E limitação de taxa protege contra sobrecarga legítima ou indevida.

Com isso, fechamos a Unidade 3. A NexaOrder agora tem serviços bem delimitados, comunicação orientada a eventos, execução orquestrada e comunicação segura — estruturalmente, a arquitetura está completa. Na Unidade 4, a gente muda o foco de "como construir" para "como saber que está funcionando": observabilidade, resiliência, engenharia do caos, processamento distribuído, borda, serverless, e o projeto integrado final da NexaOrder. Até lá!

*[indicação de edição: card de encerramento de unidade "Unidade 3 concluída — próxima: Unidade 4, Operação, validação e evolução"]*

**Fontes e links de mídia:**

- ROSE, S. et al. *Zero trust architecture*. Gaithersburg: NIST, 2020. (NIST Special Publication 800-207). DOI: 10.6028/NIST.SP.800-207. Trecho sugerido: seção 2, sobre os princípios básicos da arquitetura de confiança zero.
- GOTO Conferences. *When To Use Microservices (And When Not!) • Sam Newman & Martin Fowler*. YouTube, 2020. Disponível em: <https://www.youtube.com/watch?v=GBTdnfD6s5Q>.
