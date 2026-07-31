# Avaliação final dissertativa

Disciplina: Distributed Systems Engineering  
Professor-conteudista: Afonso Cesar Lelis Brandão  
Prazo de produção: 25 de agosto de 2026

## Orientações

- Quantidade: 10 questões dissertativas.
- Abrangência: as quatro unidades, com distribuição equilibrada (Unidade 1: questões 1-3; Unidade 2: questões 4-6; Unidade 3: questões 7-8; Unidade 4: questões 9-10).
- Conteúdo: situações-problema inéditas envolvendo a NexaOrder ou cenários equivalentes, exigindo aplicação — não apenas definição — dos conceitos estudados.
- Cada questão inclui resposta esperada e critérios de correção, com pontuação sugerida de 0 a 10 por questão.
- Espera-se que a resposta relacione conceito, mecanismo e consequência prática — respostas puramente definicionais, sem análise do cenário, devem pontuar abaixo da média.

## Questões

### Questão 1 (Unidade 1 — Comunicação e falhas parciais)

**Enunciado:** Durante um pico de vendas, o serviço de pedidos da NexaOrder chama o provedor de pagamento e, após 8 segundos sem resposta, a chamada expira (timeout). A equipe de operação precisa decidir automaticamente se reenvia a cobrança ou não. Explique por que o timeout, isoladamente, não permite saber se o pagamento foi efetivado, liste pelo menos três estados possíveis da operação naquele momento e proponha um mecanismo concreto que torne seguro decidir se a cobrança deve ser reenviada.

**Resposta esperada / critérios de correção:**
- (0-2 pontos) Reconhece que falha parcial e rede assíncrona significam que a ausência de resposta não indica se a mensagem chegou nem se foi processada — o timeout é uma decisão operacional (quanto esperar), não uma prova de falha.
- (0-3 pontos) Lista corretamente ao menos três estados possíveis: a requisição não chegou ao provedor; chegou mas ainda não foi processada; foi processada e a resposta se perdeu; continua em execução; falhou antes de produzir efeito.
- (0-3 pontos) Propõe idempotência via identificador único de operação (chave de idempotência), permitindo reenviar a requisição com segurança — o provedor reconhece o identificador repetido e não cobra duas vezes — e/ou consulta de estado ao provedor antes de reenviar.
- (0-2 pontos) Conecta a proposta a uma consequência de negócio concreta (evitar cobrança duplicada) e não apenas a um jargão técnico.

---

### Questão 2 (Unidade 1 — Concorrência e ordenação de eventos)

**Enunciado:** Dois clientes tentam comprar simultaneamente a última unidade de um produto na NexaOrder, a partir de instâncias diferentes do serviço de estoque, sem relógio global sincronizado entre elas. Explique por que não existe uma noção única de "quem chegou primeiro" nesse cenário, descreva como relógios lógicos de Lamport permitem estabelecer uma ordem consistente dos eventos e explique uma limitação dessa abordagem (o que ela não resolve sozinha).

**Resposta esperada / critérios de correção:**
- (0-2 pontos) Explica a ausência de relógio global: cada instância só observa seus próprios eventos e mensagens recebidas; comparar timestamps de relógios físicos não sincronizados não garante uma ordem causal correta.
- (0-3 pontos) Descreve corretamente o mecanismo de Lamport: cada processo mantém um contador que avança a cada evento local e é atualizado para `max(local, recebido) + 1` ao receber uma mensagem, produzindo uma ordem que respeita a relação happened-before.
- (0-3 pontos) Reconhece que relógios de Lamport dão uma ordem total consistente com causalidade, mas não distinguem eventos verdadeiramente concorrentes (não relacionados por happened-before) — dois eventos concorrentes podem receber timestamps diferentes sem que isso signifique que um realmente precedeu o outro; para captar concorrência real, seriam necessários relógios vetoriais.
- (0-2 pontos) Conecta a discussão ao problema de negócio: a ordenação lógica ajuda a decidir determinística e reproduzivelmente qual reserva "vale", mas a decisão de conceder o item ainda exige um mecanismo de exclusão mútua ou coordenação (não decorre apenas de ordenar eventos).

---

### Questão 3 (Unidade 1 — Modelos de falha e resiliência)

**Enunciado:** O provedor de pagamento da NexaOrder começou a responder com lentidão crescente (não caiu, apenas ficou lento). Sem qualquer proteção, as threads dos serviços de pedidos ficaram presas aguardando resposta, e o site inteiro parou de responder, mesmo estoque e expedição não tendo nenhum problema. Explique por que uma dependência lenta pode ser mais perigosa que uma dependência totalmente fora do ar, e descreva como um circuit breaker e um bulkhead, aplicados juntos, evitariam essa cascata.

**Resposta esperada / critérios de correção:**
- (0-3 pontos) Explica que uma falha "óbvia" (conexão recusada) falha rápido e libera recursos, enquanto uma dependência lenta consome recursos (threads, conexões) por mais tempo antes de eventualmente falhar, propagando a lentidão para os chamadores e daí para os chamadores dos chamadores — falha ambígua e sem sinalização clara.
- (0-3 pontos) Descreve o circuit breaker: monitora a taxa de falhas/timeouts e, ao ultrapassar um limiar, "abre" e passa a falhar rapidamente (ou degradar) sem tentar novas chamadas por um período, permitindo que o provedor se recupere e liberando os chamadores para responder rápido.
- (0-2 pontos) Descreve o bulkhead: isola pools de recursos (threads, conexões) por dependência, de modo que a saturação de recursos ao chamar o pagamento não consuma os recursos usados para chamar estoque ou expedição.
- (0-2 pontos) Conclui corretamente que os dois mecanismos são complementares: o bulkhead limita o raio de impacto da lentidão enquanto ela ocorre; o circuit breaker reduz a duração e a frequência das tentativas contra uma dependência já degradada.

---

### Questão 4 (Unidade 2 — Replicação e consistência)

**Enunciado:** A NexaOrder decide replicar o catálogo de produtos em três regiões, com múltiplos líderes aceitando escritas simultaneamente (multi-líder), para reduzir a latência de leitura global. Um mesmo produto tem sua descrição editada quase ao mesmo tempo em duas regiões diferentes. Explique o que caracteriza um conflito de escrita nesse cenário, cite uma estratégia possível de resolução, e explique por que essa mesma escolha de replicação multi-líder seria arriscada se aplicada ao saldo de estoque do último item de um produto.

**Resposta esperada / critérios de correção:**
- (0-2 pontos) Explica que, em replicação multi-líder, duas escritas concorrentes em réplicas diferentes podem ser aceitas localmente antes que a réplica saiba da escrita da outra, gerando divergência que precisa ser reconciliada quando as réplicas sincronizam.
- (0-3 pontos) Cita e descreve corretamente ao menos uma estratégia de resolução: last-writer-wins (com risco de perda silenciosa de uma escrita), merge determinístico dos campos, ou resolução manual/pela aplicação.
- (0-3 pontos) Explica por que estoque do último item é diferente: descrição de produto tolera consistência eventual (leitura levemente desatualizada não causa dano grave), mas decrementar/reservar a última unidade de estoque em múltiplos líderes simultâneos pode levar ambas as réplicas a "aceitarem" a venda do mesmo item, causando overselling — um domínio que exige consistência mais forte ou coordenação (ex.: consenso/quórum) em vez de multi-líder otimista.
- (0-2 pontos) Argumenta de forma coerente que a escolha do modelo de consistência deve ser por domínio de dado, não uma decisão única para todo o sistema.

---

### Questão 5 (Unidade 2 — Teorema CAP)

**Enunciado:** Durante uma partição de rede entre duas regiões da NexaOrder, os serviços de catálogo e de pagamento precisam decidir, cada um, se continuam aceitando operações localmente ou se recusam operações até a partição ser resolvida. Aplicando o teorema CAP, explique a decisão que você recomendaria para cada um dos dois serviços durante a partição, justificando com o compromisso entre disponibilidade e consistência em cada caso.

**Resposta esperada / critérios de correção:**
- (0-2 pontos) Enuncia corretamente o teorema CAP: durante uma partição de rede (P), um sistema replicado precisa escolher entre permanecer disponível (A), aceitando operações possivelmente inconsistentes entre os lados da partição, ou permanecer consistente (C), recusando operações no lado que não pode garantir o estado mais recente.
- (0-3 pontos) Para o catálogo: recomenda priorizar disponibilidade (AP) — mostrar um produto com descrição ou preço levemente desatualizado durante uma partição curta é um dano tolerável frente a impedir toda navegação e compra no site.
- (0-3 pontos) Para o pagamento (ou reserva de estoque do último item): recomenda priorizar consistência (CP) — aceitar uma cobrança ou reserva sem garantia de que a outra região não fez o mesmo aumenta o risco de cobrança duplicada ou overselling, um dano mais caro de reverter do que recusar temporariamente a operação.
- (0-2 pontos) Reconhece explicitamente que a escolha CAP não é única para o sistema inteiro, mas pode (e deve) variar por serviço/domínio, e opcionalmente menciona PACELC (o compromisso entre latência e consistência também existe na ausência de partição).

---

### Questão 6 (Unidade 2 — Sagas e idempotência)

**Enunciado:** O fluxo de compra da NexaOrder (pedido → reserva de estoque → cobrança → expedição) deixou de usar uma transação distribuída única e passou a ser implementado como uma saga coreografada baseada em eventos. Em um caso real, a cobrança falhou depois que o estoque já havia sido reservado. Descreva como a saga deve reagir a essa falha (incluindo o papel das ações compensatórias), e explique por que o padrão outbox é importante para garantir que o evento de "estoque reservado" não se perca mesmo se o serviço de estoque falhar logo após gravar a reserva no seu banco de dados.

**Resposta esperada / critérios de correção:**
- (0-3 pontos) Explica que, sem transação distribuída global, cada passo da saga é uma transação local que publica um evento de sucesso ou falha; quando a cobrança falha após a reserva de estoque, o serviço de estoque deve reagir ao evento de falha de pagamento executando uma **ação compensatória** — liberar a unidade reservada de volta ao estoque disponível — e não simplesmente ignorar a falha.
- (0-2 pontos) Reconhece que, em uma saga coreografada, cada serviço reage a eventos publicados pelos demais, sem um orquestrador central; a compensação é, portanto, responsabilidade de cada serviço que participou de um passo anterior bem-sucedido.
- (0-3 pontos) Explica o padrão outbox: a escrita da reserva de estoque e o registro do evento a ser publicado ocorrem na mesma transação local (mesmo banco de dados), e um processo separado (relay) lê essa tabela de outbox e publica o evento de forma confiável — evitando o cenário em que o estado é gravado, mas o serviço cai antes de publicar o evento, deixando o restante do sistema sem saber que a reserva ocorreu.
- (0-2 pontos) Menciona idempotência no consumo dos eventos (o consumidor pode receber o mesmo evento mais de uma vez e deve tratar reprocessamento sem duplicar efeitos).

---

### Questão 7 (Unidade 3 — Decomposição em serviços)

**Enunciado:** Um analista propõe dividir a NexaOrder em 15 microsserviços, entre eles um serviço isolado apenas para "validar CEP" e outro apenas para "formatar número de pedido", ambos consumidos exclusivamente pelo serviço de pedidos e sempre implantados e alterados junto com ele. Avalie criticamente essa proposta usando os conceitos de contexto delimitado, coesão/acoplamento e "monólito distribuído", e proponha uma alternativa mais adequada para esses dois casos específicos.

**Resposta esperada / critérios de correção:**
- (0-3 pontos) Explica que um contexto delimitado (bounded context) deve corresponder a uma capacidade de negócio com fronteiras de dados e evolução próprias; "validar CEP" e "formatar número de pedido" não são capacidades de negócio autônomas, mas detalhes de implementação internos ao domínio de pedidos.
- (0-3 pontos) Identifica que separar essas funções em serviços de rede, quando sempre são alteradas e implantadas junto com o serviço de pedidos e não têm autonomia real, cria um "monólito distribuído": mais chamadas de rede, mais latência e mais pontos de falha, sem ganho real de autonomia organizacional ou de escala independente.
- (0-2 pontos) Relaciona corretamente com baixa coesão distribuída/alto acoplamento: dividir por essas linhas aumenta o acoplamento operacional (implantação conjunta) sem reduzir o acoplamento de código de forma que compense o custo de rede.
- (0-2 pontos) Propõe alternativa coerente: manter essas duas funções como módulos internos (bibliotecas/funções) dentro do serviço de pedidos, reservando a separação em serviço próprio para quando houver uma razão real de autonomia, escala ou propriedade de dados distinta.

---

### Questão 8 (Unidade 3 — Kubernetes e reconciliação)

**Enunciado:** O serviço de pagamento da NexaOrder está implantado em Kubernetes com um Deployment configurado para 4 réplicas. Durante um pico de tráfego, uma réplica trava e para de responder, e simultaneamente o volume de requisições cresce muito além da capacidade das 3 réplicas restantes. Explique o que o Kubernetes faz automaticamente diante da réplica travada (relacionando com o conceito de estado desejado versus estado observado) e o que precisaria estar configurado adicionalmente para que o sistema também reagisse ao aumento de carga, e não apenas à réplica perdida.

**Resposta esperada / critérios de correção:**
- (0-3 pontos) Explica que o Deployment declara o estado desejado (4 réplicas saudáveis); o laço de reconciliação do Kubernetes observa continuamente o estado real do cluster e, ao perceber que apenas 3 réplicas estão saudáveis (via probes de saúde), cria automaticamente uma nova réplica para restaurar o estado desejado — sem intervenção manual.
- (0-3 pontos) Reconhece que essa reconciliação por si só **não** responde ao aumento de carga: o Kubernetes só sabe manter o número de réplicas **declarado**, e 4 réplicas continuam sendo o teto mesmo que a demanda exija mais.
- (0-2 pontos) Indica corretamente a necessidade de um Horizontal Pod Autoscaler (HPA) configurado com métricas de utilização (CPU, latência ou fila) e limites mínimo/máximo de réplicas, para que o próprio número de réplicas desejadas seja ajustado dinamicamente conforme a carga observada.
- (0-2 pontos) Menciona a importância de configurar corretamente os probes de saúde (liveness/readiness) para que a réplica travada seja de fato detectada como não saudável e retirada de circulação, e não continue recebendo tráfego.

---

### Questão 9 (Unidade 4 — Observabilidade e SLOs)

**Enunciado:** Um cliente reclama que sua compra na NexaOrder demorou mais de 12 segundos para confirmar. A equipe tem métricas agregadas (dashboards de CPU e latência média) mas não consegue identificar, sem investigação manual longa, qual dos quatro serviços (pedidos, estoque, pagamento, expedição) causou a lentidão nesse pedido específico. Explique a diferença entre monitoramento e observabilidade nesse contexto, descreva como o tracing distribuído resolveria esse problema específico, e defina o que seria um SLI e um SLO razoáveis para o fluxo de checkout da NexaOrder.

**Resposta esperada / critérios de correção:**
- (0-2 pontos) Explica que monitoramento tradicional (dashboards agregados) responde a perguntas previstas de antemão ("qual é a latência média?"), enquanto observabilidade permite investigar perguntas não previstas a partir dos dados já coletados ("por que este pedido específico demorou?") sem precisar adicionar instrumentação nova para cada nova pergunta.
- (0-3 pontos) Descreve o tracing distribuído: um identificador de correlação (trace ID) acompanha a requisição por todos os serviços envolvidos, e cada span registra o tempo gasto em cada etapa; isso permite reconstruir, para aquele pedido específico, exatamente quanto tempo cada serviço consumiu e identificar o gargalo sem investigação manual de logs.
- (0-3 pontos) Define corretamente SLI (indicador mensurável, ex.: percentual de checkouts concluídos em menos de 3 segundos, medido no p95) e SLO (meta sobre esse indicador, ex.: 99% dos checkouts em menos de 3 segundos em uma janela de 30 dias), coerentes com o cenário.
- (0-2 pontos) Menciona o conceito de orçamento de erro (quanto o SLO permite "gastar" antes de violar a meta) como ferramenta de decisão operacional.

---

### Questão 10 (Unidade 4 — Engenharia do caos)

**Enunciado:** Antes da próxima Black Friday, a equipe da NexaOrder quer validar, de forma controlada, se o site continua respondendo quando o provedor de pagamento fica indisponível — sem esperar que isso aconteça de surpresa durante o evento real. Proponha um experimento de engenharia do caos para essa validação, definindo a hipótese de estado estável, o raio de impacto do experimento e o mecanismo de interrupção (como parar o experimento se ele causar dano maior que o esperado).

**Resposta esperada / critérios de correção:**
- (0-3 pontos) Formula uma hipótese de estado estável coerente com o cenário, por exemplo: "quando o provedor de pagamento fica indisponível, o restante do site (navegação, carrinho, consulta de pedidos) continua respondendo dentro do SLO, e os pedidos em andamento falham de forma controlada (com mensagem clara ao cliente), sem indisponibilidade em cascata".
- (0-3 pontos) Define um raio de impacto limitado e crescente: primeiro em ambiente de teste/staging, depois, se aprovado, em produção restrita a uma pequena fração de tráfego ou a uma região, nunca 100% do tráfego de produção de imediato.
- (0-2 pontos) Injeta a falha de forma realista e mensurável — por exemplo, simulando indisponibilidade ou lentidão nas chamadas ao provedor de pagamento por um intervalo definido — e coleta as mesmas métricas de observabilidade da Aula 13 (latência, taxa de erro, disponibilidade dos demais serviços) durante o experimento.
- (0-2 pontos) Define um mecanismo de interrupção claro: critérios objetivos (ex.: taxa de erro acima de X% no restante do site, ou violação do orçamento de erro) que acionam o cancelamento automático ou manual imediato do experimento, restaurando o estado normal.

