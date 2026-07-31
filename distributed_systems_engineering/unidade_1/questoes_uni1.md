# Questionário — Unidade 1

Quantidade obrigatória: 40 questões — 20 de asserção-razão (1 a 20) e 20 de interpretação (21 a 40).
Cinco alternativas por questão (a-e); alternativa correta marcada com `*` imediatamente antes da letra.
Distribuição da letra correta: 8 questões para cada uma das letras a, b, c, d, e, no total das 40 questões.

## Questões

### Asserção-razão

1. I. Um sistema distribuído é caracterizado pela pluralidade de componentes autônomos que se comunicam por rede e coordenam ações para um objetivo comum.

PORQUE

II. Em qualquer sistema distribuído, existe uma memória global instantaneamente compartilhada entre todos os componentes, o que garante que todos observem o mesmo estado ao mesmo tempo.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

2. I. A escala horizontal amplia a capacidade de atendimento da NexaOrder por meio do paralelismo entre múltiplas instâncias.

PORQUE

II. Adicionar instâncias permite distribuir a carga de requisições entre vários processos que operam simultaneamente, embora exija tratamento de concorrência, balanceamento e coordenação entre elas.

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

3. I. Duas instâncias de um serviço hospedadas no mesmo servidor físico garantem tolerância a falhas, pois qualquer uma pode assumir o tráfego da outra.

PORQUE

II. A disponibilidade de um sistema distribuído independe do compartilhamento de pontos de falha entre suas réplicas.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

4. I. Uma chamada remota entre o serviço de pedidos e o serviço de estoque da NexaOrder deve ser tratada de forma diferente de uma chamada de função local.

PORQUE

II. Protocolos HTTP utilizam o formato JSON para representar recursos em APIs orientadas a recursos.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

5. I. A falha parcial não representa um desafio relevante para sistemas distribuídos, pois qualquer indisponibilidade é imediatamente percebida por todos os componentes.

PORQUE

II. Em um sistema distribuído, um componente pode estar operacional enquanto outro está indisponível, e essa condição pode ser difícil de distinguir de uma mensagem apenas atrasada.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

6. I. A comunicação assíncrona reduz o acoplamento temporal entre o serviço de pedidos e o serviço de pagamento da NexaOrder.

PORQUE

II. O protocolo HTTP define os verbos GET, POST, PUT, PATCH e DELETE para operações sobre recursos.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

7. I. Retentar uma chamada de rede sem qualquer proteção adicional é sempre seguro, pois o serviço de destino nunca processa uma mesma operação mais de uma vez.

PORQUE

II. O uso de backoff exponencial elimina completamente a necessidade de definir um valor de timeout para qualquer chamada remota.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

8. I. A adição de um novo campo opcional à mensagem de criação de pedido, com valor padrão bem definido, tende a preservar a compatibilidade com consumidores que ainda não foram atualizados.

PORQUE

II. Serviços independentes da NexaOrder são implantados em momentos diferentes, de modo que produtores e consumidores de uma mesma mensagem podem operar, temporariamente, em versões distintas do contrato.

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

9. I. Um identificador de correlação permite reconstruir o caminho de uma operação lógica através de múltiplos serviços e retentativas.

PORQUE

II. O identificador de correlação, por si só, impede que uma operação de criação de pedido seja executada mais de uma vez.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

10. I. Em um padrão de publicação-assinatura, o produtor de um evento precisa conhecer previamente cada um dos serviços que irão consumi-lo.

PORQUE

II. Em uma fila do tipo ponto a ponto, cada mensagem publicada é entregue a apenas um consumidor entre os que competem por ela.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

11. I. O relógio de Lamport garante que, se um evento A aconteceu antes de um evento B pela relação happened-before, então o carimbo lógico de A é menor que o carimbo lógico de B.

PORQUE

II. O relógio de Lamport é incrementado a cada evento local e ajustado para o maior valor entre o contador local e o contador recebido, somado de um, ao processar uma mensagem.

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

12. I. O relógio de Lamport permite distinguir, com certeza, quando dois eventos são concorrentes.

PORQUE

II. O relógio vetorial permite identificar concorrência com certeza, pois compara cada posição do vetor entre dois eventos.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

13. I. Não existe relógio global instantâneo compartilhado entre os serviços da NexaOrder.

PORQUE

II. Protocolos de sincronização de tempo por rede reduzem periodicamente o desvio acumulado entre relógios físicos de máquinas diferentes.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

14. I. Dois eventos concorrentes são sempre aqueles que ocorrem exatamente no mesmo instante de tempo físico em processos diferentes.

PORQUE

II. A relação happened-before define uma ordem total entre todos os eventos de um sistema distribuído, comparando qualquer par de eventos.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

15. I. Um desvio de relógio de algumas centenas de milissegundos entre dois servidores pode inverter, em um painel ordenado por timestamp físico, a ordem real de dois eventos próximos no tempo.

PORQUE

II. A sincronização de relógios por rede elimina totalmente o desvio entre relógios físicos de máquinas diferentes, tornando o timestamp físico uma fonte confiável de ordenação causal.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

16. I. Um timeout comprova, de forma definitiva, que o componente remoto falhou por parada.

PORQUE

II. Um detector de falhas distribuído nunca produz falsos positivos, pois identifica com precisão absoluta qualquer componente indisponível.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

17. I. O padrão circuit breaker evita que um serviço continue investindo recursos em chamadas a uma dependência com alta taxa de falha.

PORQUE

II. O padrão bulkhead isola os recursos destinados a cada dependência, como conexões e threads, em compartimentos separados.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

18. I. A degradação graciosa permite que a NexaOrder continue oferecendo uma versão reduzida do checkout quando o serviço de recomendação de produtos está indisponível.

PORQUE

II. Nem toda dependência de um fluxo distribuído é essencial para a operação principal, e essa classificação prévia permite decidir quais falhas podem ser toleradas sem interromper o fluxo.

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

19. I. Um particionamento de rede entre duas zonas de disponibilidade da NexaOrder significa que ambas as réplicas do serviço de estoque pararam de funcionar.

PORQUE

II. Durante um particionamento de rede, cada grupo isolado de componentes pode continuar operando normalmente do ponto de vista interno, sem perceber o estado do outro grupo.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

20. I. Redundância entre instâncias de um serviço só protege contra falha se as instâncias não compartilharem o mesmo ponto de falha.

PORQUE

II. Qualquer conjunto de instâncias redundantes, independentemente de como os recursos de rede e computação são compartilhados entre elas, garante isolamento total de falhas.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Interpretação

21. Durante uma campanha promocional, a NexaOrder estima um pico de 1.200 requisições por segundo. Cada instância do serviço de pedidos sustenta, de forma medida, 150 requisições por segundo. A equipe deseja operar com uma utilização-alvo de 80% da capacidade de cada instância. Considerando arredondamento para cima, qual é o número mínimo de instâncias necessárias?

a. 8 instâncias.
b. 9 instâncias.
c. 12 instâncias.
*d. 10 instâncias.
e. 15 instâncias.

22. A equipe de operações da NexaOrder define que o serviço de pagamento deve operar com disponibilidade de 99,95% em um período de 30 dias. Qual alternativa apresenta, aproximadamente, o orçamento de indisponibilidade tolerável nesse período?

a. Cerca de 4 minutos.
b. Cerca de 43 minutos.
c. Cerca de 8 horas.
d. Cerca de 1 hora.
*e. Cerca de 22 minutos.

23. Dois clientes da NexaOrder tentam comprar, ao mesmo tempo, a última unidade disponível de um produto. Ambos os processos de compra leem o mesmo valor de estoque disponível — uma unidade — antes que qualquer reserva seja confirmada. Qual conceito discutido na Unidade 1 explica diretamente o risco de os dois clientes conseguirem finalizar a compra do mesmo item?

a. Transparência de localização.
*b. Concorrência sobre um recurso compartilhado sem controle de acesso coordenado.
c. Evolução de esquema incompatível.
d. Desvio de relógio físico entre servidores.
e. Ausência de circuit breaker no serviço de estoque.

24. Uma equipe divide um sistema em doze serviços, mas qualquer alteração de negócio exige que todos os doze sejam implantados simultaneamente, pois os contratos entre eles mudam a cada nova funcionalidade. Essa situação caracteriza melhor qual risco discutido na Aula 1?

*a. Monólito distribuído, no qual a distribuição técnica não trouxe autonomia organizacional real.
b. Escalabilidade vertical insuficiente.
c. Ausência de transparência de acesso.
d. Falha de comportamento arbitrário.
e. Ausência de particionamento de rede.

25. O time de performance da NexaOrder mede que o percentil 95 de latência do endpoint de checkout é de 300 milissegundos. Qual é a interpretação correta dessa métrica?

a. Todas as requisições foram concluídas em exatamente 300 milissegundos.
b. A latência média é necessariamente igual a 300 milissegundos.
*c. 95% das requisições observadas foram concluídas em até 300 milissegundos, e 5% demoraram mais.
d. O sistema está indisponível para 5% dos usuários.
e. O throughput do sistema é de 300 requisições por segundo.

26. Um cliente da NexaOrder falha ao chamar o serviço de pagamento e aplica uma política de backoff exponencial com intervalo base de 300 milissegundos e teto de 4.000 milissegundos, sem considerar o jitter. Qual seria o intervalo de espera, sem jitter, antes da quarta tentativa (n = 3, contando a primeira tentativa como n = 0)?

a. 300 ms.
b. 600 ms.
c. 1.200 ms.
d. 4.000 ms.
*e. 2.400 ms.

27. O serviço de pedidos da NexaOrder recebe duas requisições POST /pedidos idênticas, enviadas pelo mesmo cliente após um timeout, ambas contendo a mesma chave de idempotência. Qual deve ser o comportamento correto do serviço de pedidos?

a. Criar dois pedidos distintos, pois cada requisição HTTP é independente.
b. Rejeitar ambas as requisições, pois chaves repetidas indicam erro do cliente.
c. Processar a segunda requisição normalmente, ignorando a chave de idempotência.
*d. Reconhecer a chave já processada e devolver o resultado da primeira execução, sem criar um novo pedido.
e. Aguardar indefinidamente até que o cliente confirme qual requisição deve prevalecer.

28. A NexaOrder avalia migrar a etapa de expedição do fluxo de criação de pedido de uma chamada síncrona para uma reação assíncrona a um evento PedidoCriado. Qual é a justificativa mais consistente com os conceitos desta unidade para essa mudança?

a. A expedição deixará de poder falhar, pois eventos não falham.
b. O cliente deixará de precisar de qualquer confirmação sobre o pedido.
*c. O resultado da expedição pode ser comunicado posteriormente ao cliente, sem bloquear a resposta imediata do pedido.
d. A mudança elimina a necessidade de contrato entre pedidos e expedição.
e. A mudança garante ordenação total de todos os eventos do sistema.

29. Uma nova versão do serviço de pedidos passa a exigir um campo obrigatório "canalVenda" em toda mensagem de criação de pedido. Consumidores antigos, que não enviam esse campo, começam a ter suas mensagens rejeitadas. Qual foi o erro de evolução de esquema cometido pela equipe?

a. O campo deveria ter sido enviado em formato binário.
*b. Um campo novo foi introduzido como obrigatório, em vez de opcional com valor padrão, quebrando a compatibilidade com consumidores ainda não atualizados.
c. O campo deveria ter sido removido, não adicionado.
d. O erro foi usar um broker de mensagens em vez de uma API HTTP.
e. O erro foi não definir um identificador de correlação para o campo.

30. A NexaOrder precisa notificar três serviços diferentes — estoque, análise de fraude e um futuro serviço de recomendação — sempre que um pedido for criado, sem que o serviço de pedidos precise conhecer cada um deles individualmente. Qual mecanismo de comunicação é mais adequado a esse requisito?

*a. Publicação-assinatura em um tópico de eventos, permitindo que cada serviço assine de forma independente.
b. Uma fila ponto a ponto, garantindo que apenas um dos três serviços processe cada evento.
c. Uma chamada RPC síncrona para cada um dos três serviços, encadeada.
d. Uma única chamada HTTP com todos os três serviços como destinatários no cabeçalho.
e. A replicação do banco de dados do serviço de pedidos para os três serviços.

31. No serviço de estoque da NexaOrder, o contador de Lamport está em 4. Ele recebe uma mensagem do serviço de pedidos com contador anexado igual a 6. Qual será o valor do contador do serviço de estoque após processar o recebimento dessa mensagem, segundo a regra do relógio de Lamport?

a. 4.
b. 5.
c. 6.
d. 10.
*e. 7.

32. Dois eventos da NexaOrder apresentam os seguintes relógios vetoriais, na ordem (Pedidos, Estoque, Pagamento): evento X = (3, 2, 1) e evento Y = (3, 1, 4). Qual é a relação correta entre os dois eventos?

a. X aconteceu antes de Y.
*b. X e Y são eventos concorrentes, pois nenhum vetor domina o outro em todas as posições.
c. Y aconteceu antes de X.
d. X e Y são idênticos.
e. A comparação é impossível sem relógio físico.

33. Dois servidores da NexaOrder não se sincronizam há 2 horas (7.200 segundos). Cada relógio pode desviar até 30 partes por milhão em relação ao tempo real. Qual é, aproximadamente, o desvio máximo possível entre os dois relógios nesse intervalo?

a. 30 ms.
b. 72 ms.
c. 216 ms.
*d. 432 ms.
e. 720 ms.

34. A NexaOrder identifica que, em certos pedidos, o evento de cancelamento de reserva de estoque e o evento de aprovação de pagamento são concorrentes, segundo o relógio vetorial. Qual é a conduta tecnicamente correta diante desse achado?

a. Ignorar o achado, pois relógios vetoriais não têm aplicação prática em produção.
b. Sincronizar os relógios físicos dos dois serviços com maior frequência, o que elimina a concorrência entre os eventos.
*c. Definir uma política de negócio explícita para decidir qual evento prevalece quando ambos ocorrerem de forma concorrente para o mesmo pedido.
d. Tratar sempre o evento com carimbo de hora físico mais antigo como o evento correto.
e. Impedir que os serviços de estoque e pagamento operem de forma independente.

35. O serviço de pedidos envia uma mensagem ao serviço de estoque; o serviço de estoque, ao processá-la, envia uma nova mensagem ao serviço de expedição. Com base na relação happened-before, qual afirmação é correta sobre o evento de envio original em pedidos e o evento de recebimento em expedição?

*a. O evento de envio em pedidos aconteceu antes do evento de recebimento em expedição, por transitividade da relação happened-before.
b. Os dois eventos são necessariamente concorrentes.
c. Não é possível estabelecer nenhuma relação causal entre os dois eventos.
d. A relação só pode ser estabelecida comparando os relógios físicos dos três serviços.
e. O evento de recebimento em expedição aconteceu antes do evento de envio em pedidos.

36. O serviço de pedidos monitora uma janela das últimas 25 chamadas ao provedor de pagamento e observa 9 falhas nessa janela. O limite de abertura do disjuntor é de 30%. Com base na taxa de erro observada, qual deve ser o comportamento do disjuntor?

a. Permanecer fechado, pois 9 falhas é um número baixo em termos absolutos.
*b. Abrir, pois a taxa de erro observada, 36%, ultrapassa o limite de 30% definido.
c. Entrar em estado semiaberto imediatamente, sem qualquer intervalo de espera.
d. Permanecer fechado, pois o disjuntor só considera falhas de comportamento arbitrário.
e. Abrir apenas se todas as 25 chamadas tiverem falhado.

37. O serviço de expedição da NexaOrder para de responder a qualquer requisição e permanece assim até ser reiniciado manualmente pela equipe de operações. Qual modelo de falha essa situação exemplifica?

a. Falha de omissão.
b. Falha de comportamento arbitrário.
*c. Falha de parada.
d. Falha de temporização.
e. Particionamento de rede.

38. Duas réplicas do serviço de estoque, em zonas diferentes, perdem a comunicação entre si durante um particionamento de rede, mas cada uma continua aceitando reservas de forma independente para os mesmos itens. Qual é a consequência mais provável dessa situação, segundo os conceitos desta aula?

a. Nenhuma consequência, pois o particionamento não afeta réplicas que continuam operando internamente.
b. A indisponibilidade total do serviço de estoque em ambas as zonas.
c. A eliminação automática da concorrência entre as duas réplicas.
d. A conversão automática da comunicação síncrona em assíncrona.
*e. Divergência de estado entre as réplicas, exigindo reconciliação posterior das reservas registradas de forma independente.

39. Após a NexaOrder aplicar o padrão bulkhead, reservando um conjunto de conexões exclusivo para chamadas ao provedor de pagamento, separado do conjunto usado para consultas de pedidos, o provedor de pagamento volta a apresentar lentidão. Qual é o efeito esperado sobre as consultas de pedidos não relacionadas ao pagamento?

*a. As consultas continuam sendo atendidas normalmente, pois seus recursos estão isolados do compartimento afetado pela lentidão do pagamento.
b. As consultas também ficarão indisponíveis, pois todo o serviço de pedidos compartilha os mesmos recursos.
c. As consultas passarão a usar automaticamente o provedor de pagamento como intermediário.
d. O padrão bulkhead elimina a necessidade de qualquer timeout nas chamadas de pagamento.
e. O padrão bulkhead transforma a chamada de pagamento em uma chamada idempotente.

40. A NexaOrder define um objetivo de disponibilidade de 99,9% para o fluxo de criação de pedidos, em um período de 30 dias. Qual é, aproximadamente, o orçamento de indisponibilidade tolerável nesse período, e qual a implicação prática desse número para a equipe?

a. Cerca de 4 minutos, e qualquer indisponibilidade acima disso deve ser tratada como falha de comportamento arbitrário.
b. Cerca de 8 horas, o que torna o objetivo de 99,9% pouco exigente.
c. Zero minutos, pois 99,9% exige disponibilidade total.
*d. Cerca de 43 minutos, que funcionam como orçamento a ser gerido entre incidentes, mudanças e manutenção, sem exigir disponibilidade absoluta.
e. Cerca de 43 minutos por semana, não por mês.

## Gabarito e feedbacks

**Questão 1** (correta: c)
- a. Incorreta: a asserção II é falsa, não verdadeira — não existe memória global instantaneamente compartilhada em um sistema distribuído.
- b. Incorreta: a asserção II é falsa, não verdadeira, pelo mesmo motivo.
- c. Correta: a definição de sistema distribuído (I) é verdadeira; a afirmação de que existe memória global instantânea (II) é falsa, pois é justamente a ausência dela que caracteriza a distribuição.
- d. Incorreta: a asserção I é verdadeira, não falsa.
- e. Incorreta: a asserção I é verdadeira, não falsa.

**Questão 2** (correta: a)
- a. Correta: ambas as asserções são verdadeiras, e a II explica corretamente por que a escala horizontal amplia capacidade — o paralelismo entre instâncias, com as ressalvas de concorrência e coordenação.
- b. Incorreta: a II realmente justifica a I nesta questão.
- c. Incorreta: a asserção II também é verdadeira, não falsa.
- d. Incorreta: a asserção I também é verdadeira, não falsa.
- e. Incorreta: as duas asserções são verdadeiras, não falsas.

**Questão 3** (correta: e)
- a. Incorreta: as duas asserções são falsas, não verdadeiras.
- b. Incorreta: as duas asserções são falsas, não verdadeiras.
- c. Incorreta: a asserção I é falsa — instâncias no mesmo servidor físico compartilham o mesmo ponto de falha e não garantem tolerância a falhas.
- d. Incorreta: a asserção II também é falsa — a disponibilidade depende, sim, do compartilhamento (ou não) de pontos de falha entre réplicas.
- e. Correta: a I é falsa, pois redundância no mesmo servidor não protege contra a falha desse servidor; a II é falsa, pois a disponibilidade depende diretamente do isolamento entre pontos de falha.

**Questão 4** (correta: b)
- a. Incorreta: a II é verdadeira como fato isolado, mas não justifica a I nesta questão.
- b. Correta: ambas as asserções são verdadeiras isoladamente, mas o formato de dados usado em APIs HTTP não é a razão pela qual uma chamada remota deve ser tratada de forma diferente de uma chamada local — a razão está nos modos de falha da rede.
- c. Incorreta: a asserção II também é verdadeira, não falsa.
- d. Incorreta: a asserção I também é verdadeira, não falsa.
- e. Incorreta: as duas asserções são verdadeiras, não falsas.

**Questão 5** (correta: d)
- a. Incorreta: a asserção I é falsa, não verdadeira.
- b. Incorreta: a asserção I é falsa, não verdadeira.
- c. Incorreta: a asserção I é falsa, e a II é verdadeira, não falsa.
- d. Correta: a I é falsa — a falha parcial é justamente um desafio relevante, pois nem sempre é percebida de forma clara; a II é verdadeira e descreve corretamente essa ambiguidade.
- e. Incorreta: a asserção II é verdadeira, não falsa.

**Questão 6** (correta: b)
- a. Incorreta: a II é verdadeira como fato isolado sobre HTTP, mas não justifica a I, que trata de acoplamento temporal entre serviços.
- b. Correta: ambas as asserções são verdadeiras, mas a definição dos verbos HTTP não é a razão pela qual a comunicação assíncrona reduz o acoplamento temporal.
- c. Incorreta: a asserção II também é verdadeira, não falsa.
- d. Incorreta: a asserção I também é verdadeira, não falsa.
- e. Incorreta: as duas asserções são verdadeiras, não falsas.

**Questão 7** (correta: e)
- a. Incorreta: as duas asserções são falsas, não verdadeiras.
- b. Incorreta: as duas asserções são falsas, não verdadeiras.
- c. Incorreta: a asserção I é falsa — retentar sem proteção pode duplicar efeitos, como cobranças.
- d. Incorreta: a asserção II também é falsa — backoff não elimina a necessidade de timeout; são mecanismos complementares.
- e. Correta: a I é falsa, pois retentativas sem idempotência podem duplicar efeitos; a II é falsa, pois backoff exponencial não substitui a definição de um timeout.

**Questão 8** (correta: a)
- a. Correta: ambas as asserções são verdadeiras, e a II explica corretamente por que campos novos devem ser opcionais — a implantação independente de produtores e consumidores em momentos diferentes.
- b. Incorreta: a II realmente justifica a I nesta questão.
- c. Incorreta: a asserção II também é verdadeira, não falsa.
- d. Incorreta: a asserção I também é verdadeira, não falsa.
- e. Incorreta: as duas asserções são verdadeiras, não falsas.

**Questão 9** (correta: c)
- a. Incorreta: a asserção II é falsa, não verdadeira.
- b. Incorreta: a asserção II é falsa, não verdadeira.
- c. Correta: a I é verdadeira — o identificador de correlação serve para rastrear uma operação através de múltiplos serviços; a II é falsa, pois quem previne duplicação de efeito é a chave de idempotência, não o identificador de correlação.
- d. Incorreta: a asserção I é verdadeira, não falsa.
- e. Incorreta: a asserção I é verdadeira, não falsa.

**Questão 10** (correta: d)
- a. Incorreta: a asserção I é falsa, não verdadeira.
- b. Incorreta: a asserção I é falsa, não verdadeira.
- c. Incorreta: a asserção I é falsa, e a II é verdadeira, não falsa.
- d. Correta: a I é falsa — em publicação-assinatura, o produtor não precisa conhecer seus assinantes; a II é verdadeira e descreve corretamente o comportamento de uma fila ponto a ponto.
- e. Incorreta: a asserção II é verdadeira, não falsa.

**Questão 11** (correta: a)
- a. Correta: ambas as asserções são verdadeiras, e a II descreve corretamente o mecanismo do relógio de Lamport que garante a propriedade enunciada na I.
- b. Incorreta: a II realmente justifica a I nesta questão.
- c. Incorreta: a asserção II também é verdadeira, não falsa.
- d. Incorreta: a asserção I também é verdadeira, não falsa.
- e. Incorreta: as duas asserções são verdadeiras, não falsas.

**Questão 12** (correta: d)
- a. Incorreta: a asserção I é falsa, não verdadeira.
- b. Incorreta: a asserção I é falsa, não verdadeira.
- c. Incorreta: a asserção I é falsa, e a II é verdadeira, não falsa.
- d. Correta: a I é falsa — o relógio de Lamport não distingue concorrência de coincidência numérica; a II é verdadeira, pois o relógio vetorial identifica concorrência com certeza ao comparar posições.
- e. Incorreta: a asserção II é verdadeira, não falsa.

**Questão 13** (correta: b)
- a. Incorreta: a II é verdadeira, mas não é a razão da I — a ausência de relógio global é uma característica estrutural, independente de existirem ou não protocolos de sincronização.
- b. Correta: ambas as asserções são verdadeiras, mas a II não justifica a I; mesmo com sincronização periódica, o desvio entre sincronizações persiste, o que reforça, e não explica, a I.
- c. Incorreta: a asserção II também é verdadeira, não falsa.
- d. Incorreta: a asserção I também é verdadeira, não falsa.
- e. Incorreta: as duas asserções são verdadeiras, não falsas.

**Questão 14** (correta: e)
- a. Incorreta: as duas asserções são falsas, não verdadeiras.
- b. Incorreta: as duas asserções são falsas, não verdadeiras.
- c. Incorreta: a asserção I é falsa — concorrência depende de ausência de caminho causal, não de simultaneidade física.
- d. Incorreta: a asserção II também é falsa — happened-before define uma ordem parcial, não total.
- e. Correta: a I é falsa, pois concorrência é definida por causalidade, não por tempo físico; a II é falsa, pois happened-before não compara todo par de eventos.

**Questão 15** (correta: c)
- a. Incorreta: a asserção II é falsa, não verdadeira.
- b. Incorreta: a asserção II é falsa, não verdadeira.
- c. Correta: a I é verdadeira — um desvio de centenas de milissegundos pode inverter a ordem observada de eventos próximos; a II é falsa, pois a sincronização de relógios reduz, mas não elimina totalmente, o desvio entre sincronizações.
- d. Incorreta: a asserção I é verdadeira, não falsa.
- e. Incorreta: a asserção I é verdadeira, não falsa.

**Questão 16** (correta: e)
- a. Incorreta: as duas asserções são falsas, não verdadeiras.
- b. Incorreta: as duas asserções são falsas, não verdadeiras.
- c. Incorreta: a asserção I é falsa — timeout indica apenas ausência de resposta no prazo, não prova falha de parada.
- d. Incorreta: a asserção II também é falsa — nenhum detector real de falhas é imune a falsos positivos.
- e. Correta: a I é falsa, pois timeout é uma decisão, não uma prova; a II é falsa, pois detectores de falha são estimativas sujeitas a falsos positivos e falsos negativos.

**Questão 17** (correta: b)
- a. Incorreta: a II é verdadeira, mas descreve o padrão bulkhead, não justificando o comportamento do circuit breaker descrito na I.
- b. Correta: ambas as asserções são verdadeiras, mas descrevem padrões distintos e complementares — a II não é a razão da I.
- c. Incorreta: a asserção II também é verdadeira, não falsa.
- d. Incorreta: a asserção I também é verdadeira, não falsa.
- e. Incorreta: as duas asserções são verdadeiras, não falsas.

**Questão 18** (correta: a)
- a. Correta: ambas as asserções são verdadeiras, e a II explica corretamente por que a degradação graciosa é possível — a distinção prévia entre dependências essenciais e acessórias.
- b. Incorreta: a II realmente justifica a I nesta questão.
- c. Incorreta: a asserção II também é verdadeira, não falsa.
- d. Incorreta: a asserção I também é verdadeira, não falsa.
- e. Incorreta: as duas asserções são verdadeiras, não falsas.

**Questão 19** (correta: d)
- a. Incorreta: a asserção I é falsa, não verdadeira.
- b. Incorreta: a asserção I é falsa, não verdadeira.
- c. Incorreta: a asserção I é falsa, e a II é verdadeira, não falsa.
- d. Correta: a I é falsa — um particionamento não significa que as réplicas pararam de funcionar, apenas que perderam comunicação entre si; a II descreve corretamente esse comportamento.
- e. Incorreta: a asserção II é verdadeira, não falsa.

**Questão 20** (correta: c)
- a. Incorreta: a asserção II é falsa, não verdadeira.
- b. Incorreta: a asserção II é falsa, não verdadeira.
- c. Correta: a I é verdadeira — redundância só protege se não houver ponto de falha compartilhado; a II é falsa, pois compartilhar recursos de rede ou computação entre réplicas pode, sim, comprometer o isolamento de falhas.
- d. Incorreta: a asserção I é verdadeira, não falsa.
- e. Incorreta: a asserção I é verdadeira, não falsa.

**Questão 21** (correta: d)
- a. Incorreta: 8 instâncias sustentariam apenas 8 × 120 = 960 req/s, abaixo do necessário.
- b. Incorreta: 9 instâncias sustentariam 1.080 req/s, abaixo do pico de 1.200 req/s.
- c. Incorreta: 12 instâncias excedem o mínimo necessário; o cálculo exato resulta em 10.
- d. Correta: 1.200 dividido por (150 × 0,8 = 120) resulta exatamente em 10 instâncias.
- e. Incorreta: 15 instâncias representam uma margem muito acima da necessária pelo cálculo.

**Questão 22** (correta: e)
- a. Incorreta: 4 minutos corresponde ao orçamento de uma disponibilidade de 99,99%, não de 99,95%.
- b. Incorreta: 43 minutos corresponde ao orçamento de 99,9%, não de 99,95%.
- c. Incorreta: 8 horas é muito superior ao orçamento real de 99,95% em 30 dias.
- d. Incorreta: 1 hora está acima do valor correto.
- e. Correta: 30 dias equivalem a 43.200 minutos; 0,05% desse total é aproximadamente 21,6 minutos, arredondados para cerca de 22 minutos.

**Questão 23** (correta: b)
- a. Incorreta: transparência de localização trata de esconder onde um componente está hospedado, não do risco de disputa simultânea por um recurso.
- b. Correta: o cenário descreve exatamente concorrência sobre um recurso compartilhado — dois processos lendo o mesmo estado antes de qualquer reserva ser confirmada.
- c. Incorreta: não há, no cenário, mudança de contrato ou mensagem entre versões diferentes de serviço.
- d. Incorreta: o cenário não envolve comparação de timestamps entre servidores.
- e. Incorreta: a ausência de circuit breaker não é a causa do problema descrito, que é de concorrência sobre estoque.

**Questão 24** (correta: a)
- a. Correta: a situação descreve um monólito distribuído — a divisão técnica em serviços não trouxe autonomia real, pois toda mudança ainda exige coordenação simultânea entre todos eles.
- b. Incorreta: o cenário não trata de limites de capacidade de uma única máquina.
- c. Incorreta: o cenário não descreve esconder localização de componentes, e sim acoplamento de implantação.
- d. Incorreta: não há, no cenário, indício de respostas incorretas ou maliciosas de algum componente.
- e. Incorreta: o cenário não menciona isolamento de rede entre grupos de nós.

**Questão 25** (correta: c)
- a. Incorreta: percentil não indica que todas as requisições tiveram a mesma duração.
- b. Incorreta: percentil 95 não é igual, necessariamente, à média das observações.
- c. Correta: por definição, p95 de 300 ms significa que 95% das requisições concluíram em até esse tempo, e 5% demoraram mais.
- d. Incorreta: latência elevada em parte das requisições não equivale, necessariamente, a indisponibilidade.
- e. Incorreta: o percentil de latência não mede diretamente o throughput do sistema.

**Questão 26** (correta: e)
- a. Incorreta: 300 ms corresponde à primeira tentativa (n = 0), não à quarta.
- b. Incorreta: 600 ms não corresponde a nenhuma potência de 2 multiplicada pela base neste cálculo.
- c. Incorreta: 1.200 ms corresponde à terceira tentativa (n = 2), não à quarta.
- d. Incorreta: 4.000 ms é o teto definido, mas o valor calculado (2.400 ms) ainda está abaixo dele.
- e. Correta: 300 × 2³ = 2.400 ms, valor que ainda está abaixo do teto de 4.000 ms.

**Questão 27** (correta: d)
- a. Incorreta: criar dois pedidos distintos é exatamente o efeito indesejado que a chave de idempotência deve evitar.
- b. Incorreta: chave repetida não indica erro do cliente; é o comportamento esperado de uma retentativa legítima após timeout.
- c. Incorreta: ignorar a chave de idempotência anula sua finalidade.
- d. Correta: o propósito da chave de idempotência é permitir que o serviço reconheça a repetição e devolva o resultado já processado, sem duplicar o efeito.
- e. Incorreta: não há necessidade de intervenção do cliente para resolver uma retentativa idempotente.

**Questão 28** (correta: c)
- a. Incorreta: eventos também podem falhar ao ser processados; a mensageria não elimina falhas.
- b. Incorreta: o cliente ainda precisa de alguma forma de acompanhar o resultado, mesmo que não imediata.
- c. Correta: a principal vantagem de tornar a expedição assíncrona é permitir que seu resultado seja comunicado depois, sem bloquear a resposta inicial ao cliente.
- d. Incorreta: contratos entre produtor e consumidor continuam necessários em comunicação assíncrona.
- e. Incorreta: comunicação assíncrona não garante, por si só, ordenação total dos eventos.

**Questão 29** (correta: b)
- a. Incorreta: o formato de serialização (binário ou textual) não é a causa da quebra descrita.
- b. Correta: tornar um campo novo obrigatório, em vez de opcional com valor padrão, quebra a compatibilidade com consumidores que ainda não foram atualizados.
- c. Incorreta: o problema não está na adição do campo, e sim em torná-lo obrigatório.
- d. Incorreta: a escolha entre broker e API HTTP não é a causa da quebra de compatibilidade.
- e. Incorreta: identificador de correlação não está relacionado à evolução de esquema descrita.

**Questão 30** (correta: a)
- a. Correta: publicação-assinatura permite que múltiplos serviços assinem o mesmo evento de forma independente, sem que o produtor precise conhecê-los.
- b. Incorreta: uma fila ponto a ponto entregaria o evento a apenas um dos três serviços, não a todos.
- c. Incorreta: RPC síncrono encadeado acoplaria fortemente o produtor a cada consumidor, contrariando o requisito.
- d. Incorreta: HTTP não oferece nativamente entrega a múltiplos destinatários dessa forma.
- e. Incorreta: replicar o banco de dados não resolve o requisito de notificação de eventos entre serviços.

**Questão 31** (correta: e)
- a. Incorreta: o contador não permanece inalterado ao processar um recebimento.
- b. Incorreta: 5 corresponderia a max(4,4)+1, não ao caso descrito.
- c. Incorreta: 6 corresponderia a copiar o valor recebido sem aplicar a regra de incremento.
- d. Incorreta: 10 corresponderia a somar os dois valores, o que não é a regra do relógio de Lamport.
- e. Correta: pela regra de recebimento, o novo contador é max(4,6) + 1 = 7.

**Questão 32** (correta: b)
- a. Incorreta: X não domina Y em todas as posições (a terceira posição de Y é maior).
- b. Correta: comparando posição a posição, nenhum vetor domina o outro em todas elas — a segunda posição favorece X e a terceira favorece Y —, o que caracteriza concorrência.
- c. Incorreta: Y não domina X em todas as posições (a segunda posição de X é maior).
- d. Incorreta: os vetores são diferentes, portanto os eventos não são idênticos.
- e. Incorreta: a comparação causal é possível e é feita exatamente por meio do relógio vetorial, sem depender de relógio físico.

**Questão 33** (correta: d)
- a. Incorreta: 30 ms não corresponde ao cálculo com os valores fornecidos.
- b. Incorreta: 72 ms corresponderia a usar apenas uma fração do tempo decorrido.
- c. Incorreta: 216 ms corresponderia a omitir o fator 2 da fórmula com esses valores.
- d. Correta: 2 × 0,00003 × 7.200 = 0,432 s = 432 ms.
- e. Incorreta: 720 ms está acima do valor correto para os parâmetros informados.

**Questão 34** (correta: c)
- a. Incorreta: relógios vetoriais têm aplicação prática direta na identificação de conflitos em produção.
- b. Incorreta: sincronizar relógios físicos com mais frequência reduz o desvio de tempo, mas não elimina a concorrência estrutural entre eventos causalmente independentes.
- c. Correta: diante de eventos genuinamente concorrentes, a resolução exige uma política de negócio definida previamente, pois não há critério técnico que determine qual evento deveria prevalecer.
- d. Incorreta: usar o timestamp físico mais antigo reintroduz o mesmo problema de confiabilidade discutido na aula.
- e. Incorreta: impedir a operação independente dos serviços contraria os benefícios de autonomia da arquitetura distribuída.

**Questão 35** (correta: a)
- a. Correta: pela regra de transitividade da relação happened-before, o envio em pedidos precede o recebimento em estoque, que precede o envio em estoque, que precede o recebimento em expedição.
- b. Incorreta: os eventos fazem parte de uma cadeia causal de mensagens, não são concorrentes.
- c. Incorreta: existe, sim, uma relação causal estabelecida pela cadeia de envio e recebimento de mensagens.
- d. Incorreta: a relação happened-before é estabelecida por causalidade observável (mensagens), não por comparação de relógios físicos.
- e. Incorreta: a ordem descrita é exatamente a inversa da real, conforme a cadeia de mensagens.

**Questão 36** (correta: b)
- a. Incorreta: o critério do disjuntor é a taxa de erro relativa, não o número absoluto de falhas.
- b. Correta: 9 dividido por 25 resulta em 36%, taxa que ultrapassa o limite de 30% definido, o que deve abrir o disjuntor.
- c. Incorreta: o estado semiaberto só é alcançado após o intervalo de abertura, não imediatamente.
- d. Incorreta: o disjuntor considera qualquer falha registrada na janela, não apenas falhas de comportamento arbitrário.
- e. Incorreta: o disjuntor abre ao ultrapassar o limite definido, não apenas quando todas as chamadas falham.

**Questão 37** (correta: c)
- a. Incorreta: falha de omissão envolveria perda de algumas mensagens, com o componente continuando a operar para outras.
- b. Incorreta: falha de comportamento arbitrário envolveria respostas incorretas, não ausência total de resposta.
- c. Correta: um componente que para completamente e permanece parado até intervenção manual exemplifica falha de parada.
- d. Incorreta: falha de temporização envolveria resposta correta, porém fora do prazo, não ausência total de resposta.
- e. Incorreta: o cenário não descreve isolamento de comunicação entre grupos de nós, e sim a parada de um único componente.

**Questão 38** (correta: e)
- a. Incorreta: a continuidade de operação interna de cada réplica não elimina o risco de divergência entre elas.
- b. Incorreta: o cenário descreve réplicas que continuam operando, não indisponibilidade total.
- c. Incorreta: a concorrência entre as réplicas se mantém justamente porque elas continuam aceitando reservas de forma independente.
- d. Incorreta: o particionamento não converte automaticamente o tipo de comunicação utilizado.
- e. Correta: réplicas isoladas aceitando reservas independentes para os mesmos itens tendem a divergir de estado, exigindo reconciliação posterior.

**Questão 39** (correta: a)
- a. Correta: o propósito do padrão bulkhead é justamente isolar os recursos, de modo que a lentidão em um compartimento não afete os demais.
- b. Incorreta: o cenário descreve recursos isolados por compartimento, o que contraria essa alternativa.
- c. Incorreta: o padrão bulkhead não redireciona chamadas de consulta para o provedor de pagamento.
- d. Incorreta: o padrão bulkhead isola recursos, mas não substitui a necessidade de definir timeouts.
- e. Incorreta: bulkhead e idempotência são mecanismos distintos e não equivalentes.

**Questão 40** (correta: d)
- a. Incorreta: 4 minutos corresponde ao orçamento de 99,99%, não de 99,9%; além disso, exceder o orçamento não caracteriza, por si só, falha de comportamento arbitrário.
- b. Incorreta: 8 horas está muito acima do orçamento real associado a 99,9% em 30 dias.
- c. Incorreta: 99,9% não exige disponibilidade absoluta; por definição, admite um orçamento de indisponibilidade maior que zero.
- d. Correta: 30 dias equivalem a 43.200 minutos; 0,1% desse total é aproximadamente 43 minutos, que funcionam como orçamento a ser gerido pela equipe.
- e. Incorreta: o orçamento de 43 minutos refere-se ao período de 30 dias definido no enunciado, não a uma semana.
