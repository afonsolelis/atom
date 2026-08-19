# Avaliação final dissertativa — arquivo-mestre

Disciplina: *Distributed Systems Engineering*

Professor-conteudista: Afonso Cesar Lelis Brandão

Prazo de produção informado: 25 de agosto de 2026

> **Controle de versão:** a Parte A é destinada ao estudante. A Parte B é exclusiva do professor tutor e contém respostas esperadas e critérios de correção. A versão mestra já foi gerada no modelo institucional; antes da distribuição, devem ser exportadas e aprovadas cópias separadas, com o arquivo do estudante terminando antes da Parte B.

---

# Parte A — Versão do estudante

## Orientações

- Quantidade: 10 questões dissertativas.
- Abrangência: as quatro unidades, com a seguinte distribuição: Unidade 1, questões 1 a 3; Unidade 2, questões 4 a 6; Unidade 3, questões 7 e 8; Unidade 4, questões 9 e 10.
- Conteúdo: situações-problema envolvendo a NexaOrder ou cenários equivalentes, com aplicação dos conceitos estudados.
- Valor sugerido: 10 pontos por questão, totalizando 100 pontos.
- Cada resposta deve relacionar conceito, mecanismo, hipóteses e consequência prática. Respostas puramente definicionais, sem análise do cenário, não atendem integralmente ao que foi solicitado.

## Questões

### Questão 1 — Unidade 1: comunicação e falhas parciais

Durante um pico de vendas, o serviço de pedidos da NexaOrder chama o provedor de pagamento e, após 8 segundos sem resposta, a chamada atinge seu limite de tempo (*timeout*). A equipe de operação precisa decidir automaticamente se reenvia a cobrança. Explique por que o *timeout*, isoladamente, não permite saber se o pagamento foi efetivado, liste pelo menos três estados possíveis da operação naquele momento e proponha um mecanismo concreto que torne seguro decidir se a cobrança deve ser reenviada.

### Questão 2 — Unidade 1: concorrência e ordenação de eventos

Dois clientes tentam comprar simultaneamente a última unidade de um produto na NexaOrder a partir de instâncias diferentes do serviço de estoque, sem relógio global sincronizado. Explique por que não existe uma noção única de “quem chegou primeiro”, descreva a garantia causal fornecida pelos relógios lógicos de Lamport, explique como se pode construir uma ordem total determinística a partir deles e apresente pelo menos uma limitação dessa abordagem.

### Questão 3 — Unidade 1: modelos de falha e resiliência

O provedor de pagamento da NexaOrder começou a responder com lentidão crescente. Sem proteção, os recursos do serviço de pedidos ficaram ocupados aguardando respostas, e o site inteiro parou de responder, mesmo sem falha no estoque ou na expedição. Explique por que uma dependência lenta pode ser mais perigosa que uma dependência totalmente fora do ar e descreva como *circuit breaker* e *bulkhead*, aplicados em conjunto, reduziriam a cascata.

### Questão 4 — Unidade 2: replicação e consistência

A NexaOrder replica o catálogo em três regiões e permite que múltiplos líderes aceitem escritas locais para melhorar a disponibilidade e reduzir a latência de escrita regional. A descrição de um mesmo produto é editada quase simultaneamente em duas regiões. Explique o que caracteriza um conflito de escrita, apresente uma estratégia de resolução e explique por que a mesma replicação otimista seria arriscada para a reserva da última unidade em estoque.

### Questão 5 — Unidade 2: CAP, pagamento e idempotência

Durante uma partição de rede entre duas regiões, o catálogo e o registro interno de pagamentos da NexaOrder precisam decidir se continuam aceitando operações localmente ou se recusam operações até a comunicação ser restabelecida. Aplicando o teorema CAP, recomende uma política para cada domínio e justifique o compromisso entre disponibilidade e consistência. Em seguida, explique por que escolher consistência para o registro interno não basta, por si só, para impedir cobrança duplicada em um provedor externo.

### Questão 6 — Unidade 2: sagas e idempotência

O fluxo pedido → reserva de estoque → cobrança → expedição passou a ser implementado como uma saga coreografada baseada em eventos. A cobrança falhou depois da reserva do estoque. Descreva como a saga deve reagir, incluindo as ações compensatórias, e explique por que o padrão *outbox* evita que o evento “estoque reservado” se perca se o serviço falhar logo após gravar a reserva.

### Questão 7 — Unidade 3: decomposição em serviços

Um analista propõe dividir a NexaOrder em 15 microsserviços, incluindo um serviço apenas para validar CEP e outro apenas para formatar o número do pedido. Ambos são consumidos exclusivamente pelo serviço de pedidos e sempre são alterados e implantados com ele. Avalie a proposta usando contexto delimitado, coesão, acoplamento e “monólito distribuído” e proponha uma alternativa para esses dois casos.

### Questão 8 — Unidade 3: Kubernetes e reconciliação

O serviço de pagamento está implantado em Kubernetes por meio de um *Deployment* configurado para quatro réplicas. Durante um pico, um Pod trava e deixa de responder, enquanto a carga supera a capacidade dos três Pods saudáveis. Diferencie o papel das sondas de prontidão (*readiness*) e vivacidade (*liveness*), explique quando o contêiner ou o Pod é reiniciado ou substituído e indique o que precisa ser configurado para que o número desejado de réplicas também cresça com a carga.

### Questão 9 — Unidade 4: observabilidade e SLOs

Um cliente informa que sua compra demorou mais de 12 segundos. A equipe possui painéis agregados de CPU e latência média, mas não consegue identificar qual serviço causou a demora daquele pedido. Explique a diferença entre monitoramento e observabilidade, descreva como o rastreamento distribuído resolveria esse problema e proponha um SLI e um SLO coerentes. Se escolher percentil de latência, formule a meta em percentil; se escolher proporção de requisições abaixo de um limiar, formule a meta como proporção. Não misture as duas medidas.

### Questão 10 — Unidade 4: engenharia do caos

Antes da próxima Black Friday, a equipe quer validar de forma controlada se o site continua respondendo quando o provedor de pagamento fica indisponível. Proponha um experimento de engenharia do caos, definindo a hipótese de estado estável, o raio de impacto, as métricas observadas e o mecanismo de interrupção caso o dano supere o esperado.

---

# Parte B — Versão exclusiva do professor tutor

> **NÃO DISTRIBUIR AOS ESTUDANTES.** Esta parte deve ser removida do DOCX do estudante. Ela deve permanecer apenas na versão do tutor, posicionada ao final do documento conforme o requisito registrado para as devolutivas.

## Respostas esperadas e critérios de correção

### Questão 1

- **0 a 2 pontos:** reconhece que a ausência de resposta não informa se a mensagem chegou ou se o efeito ocorreu; o *timeout* é uma decisão operacional, não prova de falha.
- **0 a 3 pontos:** lista pelo menos três estados plausíveis: requisição não recebida, recebida e pendente, processada com resposta perdida, ainda em execução ou falha antes do efeito.
- **0 a 3 pontos:** propõe chave de idempotência reutilizada na nova tentativa e/ou consulta e reconciliação do estado no provedor.
- **0 a 2 pontos:** relaciona o mecanismo à prevenção de cobrança duplicada.

### Questão 2

- **0 a 2 pontos:** explica que processos observam eventos locais e mensagens e que relógios físicos não sincronizados não determinam uma ordem causal global.
- **0 a 3 pontos:** descreve o contador de Lamport e a atualização $L \leftarrow \max(L_{\text{local}}, L_{\text{recebido}})+1$; reconhece a garantia $a \rightarrow b \Rightarrow L(a)<L(b)$.
- **0 a 3 pontos:** explica que timestamps escalares podem empatar e que uma ordem total determinística pode usar o par `(timestamp, identificador_do_processo)` como desempate. Reconhece que $L(a)<L(b)$ não implica $a \rightarrow b$ e que essa ordem artificial não detecta concorrência; relógios vetoriais podem representar melhor essa relação.
- **0 a 2 pontos:** conclui que ordenar eventos não concede exclusão mútua nem resolve sozinho a venda da última unidade; ainda é necessário coordenar a decisão.

### Questão 3

- **0 a 3 pontos:** explica que uma dependência lenta retém conexões, filas ou unidades de execução e propaga espera, enquanto uma falha rápida libera recursos mais cedo.
- **0 a 3 pontos:** descreve o *circuit breaker*: mede falhas ou *timeouts*, abre após um limiar, falha rapidamente durante um período e testa recuperação de forma controlada.
- **0 a 2 pontos:** descreve o *bulkhead*: separa limites e conjuntos de recursos por dependência.
- **0 a 2 pontos:** explica que os mecanismos são complementares: um limita o raio de impacto e o outro reduz tentativas contra a dependência degradada.

### Questão 4

- **0 a 2 pontos:** identifica escritas concorrentes aceitas por líderes diferentes antes da replicação mútua.
- **0 a 3 pontos:** apresenta estratégia coerente, como mesclagem determinística por campo, resolução pela aplicação ou *last-writer-wins*, indicando os riscos de perda silenciosa desta última.
- **0 a 3 pontos:** explica que reservas concorrentes da última unidade podem ser aceitas nas duas regiões e causar venda acima do estoque.
- **0 a 2 pontos:** defende políticas de consistência diferentes por domínio, com coordenação mais forte para estoque.

### Questão 5

- **0 a 2 pontos:** enuncia CAP no contexto correto: diante de uma partição, um sistema replicado não consegue oferecer simultaneamente disponibilidade irrestrita e uma visão linearizável única.
- **0 a 2 pontos:** para dados descritivos do catálogo, aceita priorizar disponibilidade e reconciliar divergências, desde que discuta quais campos de negócio realmente toleram desatualização.
- **0 a 3 pontos:** para o registro interno de pagamentos, justifica recusar ou limitar operações no lado que não consegue garantir o estado autorizado, priorizando consistência.
- **0 a 3 pontos:** reconhece que CAP trata o estado replicado interno, não a atomicidade de um efeito em um provedor externo; cobrança duplicada ainda exige chave de idempotência, consulta/reconciliação e tratamento de estados incertos.

### Questão 6

- **0 a 3 pontos:** explica que cada passo da saga é uma transação local e que a falha da cobrança deve desencadear a compensação da reserva.
- **0 a 2 pontos:** reconhece que, na coreografia, cada serviço reage a eventos sem um orquestrador central e deve implementar suas compensações.
- **0 a 3 pontos:** explica que a reserva e o registro do evento na tabela *outbox* ocorrem na mesma transação local; um publicador separado envia o evento posteriormente.
- **0 a 2 pontos:** menciona consumo idempotente, pois a publicação pode ocorrer mais de uma vez.

### Questão 7

- **0 a 3 pontos:** explica que contexto delimitado corresponde a uma capacidade de negócio com fronteiras e evolução próprias; validar CEP e formatar número são detalhes internos no cenário dado.
- **0 a 3 pontos:** identifica o risco de “monólito distribuído”: chamadas de rede e pontos de falha sem autonomia real.
- **0 a 2 pontos:** relaciona a proposta a baixa coesão e alto acoplamento operacional.
- **0 a 2 pontos:** recomenda manter as funções como módulos internos, salvo evidência futura de escala, propriedade de dados ou evolução independente.

### Questão 8

- **0 a 3 pontos:** explica que falha de prontidão remove o Pod dos pontos de acesso do serviço, mas não reduz necessariamente a contagem desejada nem cria um quinto Pod.
- **0 a 3 pontos:** explica que falha de vivacidade faz o `kubelet` reiniciar o contêiner no mesmo Pod; o controlador cria substituto quando um Pod termina, é removido ou deixa de contar para o conjunto de réplicas, inclusive após os mecanismos aplicáveis a falha de nó.
- **0 a 2 pontos:** reconhece que o *Deployment* continua declarando quatro réplicas e que reconciliação de falha não equivale a escalonamento por carga.
- **0 a 2 pontos:** indica HPA com métrica adequada, limites mínimo/máximo e capacidade disponível no *cluster*.

### Questão 9

- **0 a 2 pontos:** diferencia monitoramento de indicadores previstos e observabilidade como capacidade de investigar estados internos por sinais produzidos pelo sistema.
- **0 a 3 pontos:** descreve a propagação de um identificador de rastreamento e os segmentos temporais de cada serviço, permitindo localizar a etapa lenta daquele pedido.
- **0 a 3 pontos:** formula um par coerente. Exemplo de proporção: SLI = fração de finalizações bem-sucedidas em até 3 segundos; SLO = pelo menos 99% em 30 dias. Exemplo de percentil: SLI = p95 da latência; SLO = p95 inferior a 3 segundos em cada janela de 30 dias.
- **0 a 2 pontos:** explica o orçamento de erro e não mistura p95 com “99% abaixo do limiar” como se fossem a mesma medida.

### Questão 10

- **0 a 3 pontos:** formula hipótese mensurável de estado estável para as funções que devem continuar disponíveis e para a degradação controlada do pagamento.
- **0 a 2 pontos:** limita e amplia gradualmente o raio de impacto, começando em ambiente de teste e evitando 100% do tráfego de produção.
- **0 a 3 pontos:** injeta indisponibilidade ou latência de forma controlada e mede latência, erro, saturação e disponibilidade dos demais serviços.
- **0 a 2 pontos:** define critérios objetivos e mecanismo automático ou manual de interrupção e restauração.

## Conferência antes da exportação

- [ ] Gerar um DOCX do estudante contendo somente a Parte A.
- [ ] Gerar um DOCX do tutor contendo as Partes A e B.
- [ ] Posicionar respostas e devolutivas ao final no formato exigido pelo modelo.
- [ ] Confirmar que cada rubrica soma 10 pontos e que o total é 100.
- [ ] Remover exemplos e instruções internas do modelo institucional.
- [ ] Validar plano de aprendizagem, linguagem, formatação e similaridade.
