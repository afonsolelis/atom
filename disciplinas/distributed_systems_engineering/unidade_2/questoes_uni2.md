# Questionário — Unidade 2

Disciplina: Distributed Systems Engineering  
Unidade: 2 — Dados distribuídos, consistência e coordenação  
Quantidade: 40 questões (20 de asserção-razão + 20 de interpretação), padrão ENADE, cinco alternativas cada, alternativa correta marcada com asterisco (`*`).

## Questões

### Asserção-razão (questões 1 a 20)

**1.** I. Em um sistema replicado com $N = 5$, uma configuração com $W = 3$ e $R = 3$ garante que qualquer conjunto de três réplicas consultado na leitura intersecte o conjunto de três que confirmou a escrita anterior.

PORQUE

II. A soma de $W$ e $R$ é maior que $N$ nessa configuração, garantindo que o conjunto de réplicas lidas e o conjunto de réplicas escritas compartilhem ao menos uma réplica em comum.

a. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
c. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
d. As asserções I e II são proposições falsas.
e. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.

**2.** I. A replicação multi-líder permite que centros de distribuição em regiões diferentes aceitem escritas locais com baixa latência.

PORQUE

II. A replicação líder-seguidor concentra todas as escritas em um único nó, o que simplifica a resolução de conflitos entre escritas concorrentes.

a. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
b. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
c. As asserções I e II são proposições falsas.
*d. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
e. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.

**3.** I. A replicação assíncrona pode reduzir a latência de escrita percebida pelo cliente, pois o líder responde sem esperar confirmações das réplicas, ainda que a propagação já possa ter sido iniciada.

PORQUE

II. A replicação assíncrona elimina completamente o risco de perda de dados em caso de falha do líder.

a. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
c. As asserções I e II são proposições falsas.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.

**4.** I. A consistência eventual garante que, a qualquer momento após uma escrita, todas as réplicas retornem imediatamente o mesmo valor.

PORQUE

II. A consistência eventual garante que, se novas escritas cessarem e a replicação continuar ou se recuperar, as réplicas convergirão para o mesmo valor, sem prazo definido.

a. As asserções I e II são proposições falsas.
b. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*c. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
d. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
e. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.

**5.** I. Garantias centradas no cliente, como a leitura das próprias escritas, exigem que o sistema adote necessariamente consistência forte global.

PORQUE

II. A leitura de prefixo consistente permite que um cliente observe uma escrita B sem antes observar a escrita A da qual B depende causalmente.

*a. As asserções I e II são proposições falsas.
b. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
c. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
d. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
e. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.

**6.** I. Com uma função de *hash* de bom espalhamento, quantidade suficiente de chaves distintas e partições equilibradas, o particionamento por *hash* tende a distribuir as chaves de forma aproximadamente uniforme.

PORQUE

II. Uma função de *hash* de bom espalhamento produz resultados sem relação direta com a ordem alfabética ou temporal do valor original, reduzindo a concentração por faixas da chave.

a. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. As asserções I e II são proposições falsas.
*d. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
e. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.

**7.** I. O *hashing* consistente reduz drasticamente a fração de chaves redistribuída quando um nó é adicionado a um cluster.

PORQUE

II. O particionamento por diretório mantém uma tabela explícita de mapeamento entre chaves e partições, exigindo disponibilidade própria.

*a. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
c. As asserções I e II são proposições falsas.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.

**8.** I. Um ponto quente pode surgir mesmo em um sistema com *hashing* consistente bem implementado, quando uma única chave concentra tráfego desproporcional.

PORQUE

II. O *hashing* consistente resolve integralmente o problema de pontos quentes causados pela popularidade desigual de chaves individuais.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições falsas.
c. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.

**9.** I. O teorema CAP afirma que um sistema distribuído deve, permanentemente, escolher entre ser consistente ou disponível, mesmo na ausência de qualquer falha de rede.

PORQUE

II. O teorema CAP descreve o compromisso entre consistência e disponibilidade especificamente durante uma partição de rede.

*a. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
b. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
c. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
d. As asserções I e II são proposições falsas.
e. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.

**10.** I. O PACELC afirma que, na ausência de partição de rede, um sistema distribuído pode ignorar completamente qualquer compromisso entre latência e consistência.

PORQUE

II. O particionamento por faixa é sempre superior ao particionamento por *hash*, independentemente do padrão de consultas do sistema.

a. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
b. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
c. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*d. As asserções I e II são proposições falsas.
e. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.

**11.** I. Um cluster de consenso com cinco nós tolera a falha simultânea de até dois nós sem perder a capacidade de formar maioria.

PORQUE

II. Para um cluster de $N$ nós, o número de falhas toleradas é dado por $f = \lfloor (N-1)/2 \rfloor$, que para $N = 5$ resulta em $f = 2$.

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições falsas.
c. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
d. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
e. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.

**12.** I. O algoritmo Raft utiliza temporizadores de eleição aleatórios para reduzir a chance de disputas simultâneas entre candidatos.

PORQUE

II. O algoritmo Raft organiza o tempo em termos numerados sequencialmente, e cada termo possui no máximo um líder.

a. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
b. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*c. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
d. As asserções I e II são proposições falsas.
e. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.

**13.** I. Uma entrada criada pelo líder no termo corrente do Raft pode ser confirmada (*committed*) quando armazenada por uma maioria dos nós do cluster.

PORQUE

II. Uma entrada de log confirmada no Raft pode ser posteriormente removida ou substituída caso o líder que a confirmou venha a falhar.

a. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*b. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
c. As asserções I e II são proposições falsas.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.

**14.** I. O algoritmo Raft garante disponibilidade contínua para escrita mesmo quando apenas uma minoria dos nós do cluster está ativa e comunicável.

PORQUE

II. A disponibilidade do Raft depende de haver, em algum momento, comunicação suficiente entre a maioria dos nós do cluster.

a. As asserções I e II são proposições falsas.
b. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
c. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.

**15.** I. O algoritmo Raft, em sua formulação padrão, tolera falhas bizantinas, nas quais um nó pode enviar informações deliberadamente incorretas.

PORQUE

II. O *throughput* de um cluster Raft cresce proporcionalmente ao número de líderes que processam escritas em paralelo.

a. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*b. As asserções I e II são proposições falsas.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
e. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.

**16.** I. A confirmação em duas fases (2PC) pode deixar participantes bloqueados caso o coordenador falhe entre a fase de preparação e a fase de confirmação.

PORQUE

II. Durante a fase de preparação do 2PC, cada participante mantém recursos bloqueados até receber a decisão final do coordenador.

a. As asserções I e II são proposições falsas.
b. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*c. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.

**17.** I. Sagas substituem uma transação distribuída única por uma sequência de transações locais encadeadas por eventos ou comandos.

PORQUE

II. O padrão *outbox* grava o evento a ser publicado na mesma transação local que grava a alteração de negócio.

a. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. As asserções I e II são proposições falsas.
e. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.

**18.** I. Uma ação compensatória em uma saga busca reverter, de forma lógica, o efeito de uma etapa já concluída.

PORQUE

II. Uma ação compensatória é sempre o inverso matemático exato da operação original, sem qualquer diferença de custo, prazo ou política de negócio.

a. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
b. As asserções I e II são proposições falsas.
c. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.

**19.** I. Sistemas de mensageria distribuída garantem, por padrão, entrega exatamente uma vez, eliminando a necessidade de operações idempotentes.

PORQUE

II. Sistemas de mensageria distribuída tipicamente oferecem entrega pelo menos uma vez (*at-least-once*), o que implica que duplicatas de mensagens devem ser esperadas.

a. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
b. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*c. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
d. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
e. As asserções I e II são proposições falsas.

**20.** I. O padrão *inbox* continua seguro quando o consumidor confirma o identificador da mensagem em uma transação e só depois, em outra transação, aplica o efeito de negócio, pois uma falha entre essas etapas não causa perda de processamento.

PORQUE

II. A saga orquestrada elimina totalmente a necessidade de qualquer componente central conhecer a sequência do processo de negócio.

*a. As asserções I e II são proposições falsas.
b. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
c. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.

### Interpretação (questões 21 a 40)

**21.** A NexaOrder configura seu banco de dados de catálogo com $N = 5$ réplicas, $W = 1$ e $R = 1$, priorizando latência mínima tanto na escrita quanto na leitura. Qual é a consequência mais provável dessa configuração para a consistência das leituras do catálogo?

a. Leituras sempre refletirão a escrita mais recente, pois $W = 1$ já é suficiente para garantir consistência forte.
b. A configuração elimina completamente o atraso de réplica entre os nós.
c. A configuração é inválida e o sistema não conseguirá operar.
*d. Leituras podem retornar valores desatualizados, pois não há garantia de sobreposição entre os conjuntos de réplicas escritas e lidas.
e. O sistema rejeitará qualquer leitura até que todas as réplicas estejam sincronizadas.

**22.** A NexaOrder decide usar $N = 5$, $W = 3$ e $R = 3$ para o serviço de estoque, buscando equilíbrio entre disponibilidade e consistência. Qual afirmação melhor descreve essa escolha?

a. A configuração é inválida, pois $W$ e $R$ não podem assumir o mesmo valor.
b. A configuração exige a confirmação das cinco réplicas em toda escrita.
c. A configuração é equivalente, em termos de garantias, a $W = 1$ e $R = 1$.
d. A configuração prioriza exclusivamente disponibilidade, sem qualquer garantia de consistência.
*e. A soma de $W$ e $R$ é maior que $N$, garantindo sobreposição entre os conjuntos de réplicas lidas e escritas, ao custo de exigir resposta de três réplicas em cada operação.

**23.** Um cliente da NexaOrder atualiza seu endereço de entrega e, imediatamente após, consulta seus dados de cadastro na mesma sessão, esperando ver o novo endereço refletido. Qual garantia centrada no cliente descreve exatamente essa expectativa?

a. Consistência sequencial.
*b. Leitura das próprias escritas (*read-your-writes*).
c. Leituras monotônicas.
d. Leitura de prefixo consistente.
e. Escritas monotônicas.

**24.** Dois centros de distribuição da NexaOrder, em regiões diferentes, operam sob replicação multi-líder. Quase simultaneamente, um registra a saída de uma unidade de um produto e o outro registra uma correção de inventário para o mesmo produto. O que esse cenário exige do sistema, segundo os conceitos estudados?

a. A eliminação da replicação multi-líder em favor de um único banco de dados centralizado.
b. A promoção imediata de um dos centros a único líder global.
c. A conversão automática do dado para consistência forte, sem necessidade de qualquer regra adicional.
d. Nada, pois a replicação multi-líder impede automaticamente escritas concorrentes sobre o mesmo dado.
*e. Uma regra explícita de resolução de conflitos, pois escritas concorrentes em líderes diferentes podem colidir sobre o mesmo dado.

**25.** Ao decidir o modelo de consistência para o registro de transações de pagamento, a equipe da NexaOrder avalia os riscos financeiros de uma leitura obsoleta durante a confirmação de uma cobrança. Qual escolha é mais coerente com o raciocínio apresentado na aula para esse dado específico?

a. Consistência eventual pura, pois reduz a latência de leitura ao máximo.
b. Replicação assíncrona sem quórum, priorizando a menor latência de escrita possível.
*c. Consistência próxima da forte, priorizando a atualidade do valor confirmado mesmo ao custo de maior latência.
d. Nenhum modelo de consistência é aplicável a dados financeiros distribuídos.
e. Consistência eventual combinada exclusivamente com leituras monotônicas.

**26.** A NexaOrder particiona seu catálogo de produtos por faixa alfabética e observa que uma campanha publicitária concentra tráfego em produtos cujo nome começa com a letra "S", sobrecarregando a partição correspondente. Qual é a explicação mais adequada para esse comportamento?

a. A sobrecarga indica necessariamente uma falha do banco de dados, sem relação com a estratégia de particionamento.
*b. O particionamento por faixa é vulnerável a pontos quentes quando a distribuição real das chaves não é uniforme.
c. O particionamento por diretório eliminaria automaticamente esse problema, sem qualquer configuração adicional.
d. O problema só poderia ocorrer em particionamento por *hash*, nunca em particionamento por faixa.
e. O particionamento por faixa distribui sempre a carga de forma perfeitamente uniforme, independentemente do padrão de acesso.

**27.** Um cluster de armazenamento da NexaOrder com nove nós, organizado por *hashing* consistente, recebe um décimo nó. Qual é o efeito esperado sobre a distribuição das chaves?

a. Metade das chaves é redistribuída, independentemente do número de nós.
b. A redistribuição depende exclusivamente do número de réplicas, não do número de nós.
*c. Apenas uma fração próxima a $1/(N+1)$, ou cerca de 10%, das chaves é redistribuída, movendo-se para o novo nó.
d. Todas as chaves do cluster são redistribuídas, como ocorreria em um *hash* simples por módulo.
e. Nenhuma chave é redistribuída, pois o *hashing* consistente é imutável após a criação do anel.

**28.** Mesmo com *hashing* consistente bem implementado, um produto específico da NexaOrder concentra grande parte das **leituras informativas** de estoque em uma única partição. A aplicação tolera alguns segundos de defasagem nessa exibição, enquanto a reserva autoritativa continua protegida por controle de concorrência separado. Qual medida é mais coerente para mitigar o ponto quente?

*a. Usar cache ou réplicas de leitura para a consulta informativa, com política explícita de expiração ou versionamento, sem fragmentar ingenuamente a decisão autoritativa de reserva.
b. Migrar o sistema inteiro para particionamento por faixa.
c. Ignorar o problema, pois o *hashing* consistente já distribui qualquer chave uniformemente entre todas as partições.
d. Bloquear temporariamente todas as leituras do produto até o fim da campanha.
e. Aumentar o número total de partições do sistema, o que resolve automaticamente qualquer ponto quente de chave única.

**29.** Durante uma falha de rede, um sistema distribuído da NexaOrder decide continuar respondendo a requisições em ambos os lados da partição, aceitando o risco de valores divergentes que serão reconciliados posteriormente. Essa escolha caracteriza o sistema, durante a partição, como:

a. Um sistema que viola o teorema CAP.
b. Um sistema sem tolerância a partição, pois continua operando apesar da falha de rede.
*c. AP, pois prioriza disponibilidade em detrimento da garantia de consistência imediata.
d. CP, pois prioriza consistência acima de tudo.
e. CA, pois oferece consistência e disponibilidade simultaneamente, sem restrições.

**30.** Fora de qualquer cenário de partição de rede, a NexaOrder configura seu banco de estoque para exigir confirmação de todas as réplicas antes de responder a uma escrita, buscando a maior garantia de consistência possível. Segundo o PACELC, qual é a consequência mais direta dessa escolha no funcionamento cotidiano do sistema?

a. Aumento da disponibilidade do sistema em todas as condições.
b. Eliminação completa do atraso de réplica em qualquer configuração futura.
c. Redução do *throughput* de leitura, sem qualquer efeito sobre a latência de escrita.
*d. Aumento da latência de escrita no dia a dia, mesmo sem qualquer falha de rede, como custo permanente da consistência elevada.
e. Nenhuma, pois o PACELC só se aplica durante partições de rede.

**31.** Um cluster Raft de sete nós sofre uma falha de rede que isola três nós de um lado e mantém quatro nós comunicáveis entre si do outro lado. O que se espera, segundo o critério de maioria estudado na aula?

a. Ambos os grupos formam maioria e continuam aceitando escritas de forma independente.
b. Nenhum dos dois grupos consegue eleger um líder, pois o cluster inteiro precisa estar íntegro.
*c. Apenas o grupo de quatro nós forma maioria e pode eleger um líder e continuar aceitando escritas.
d. A maioria é irrelevante para a eleição de líder no algoritmo Raft.
e. O grupo de três nós forma maioria, pois responde mais rápido por ter menos participantes.

**32.** Suponha que, em um cluster Raft, todos os seguidores utilizassem exatamente o mesmo valor fixo de temporizador de eleição, em vez de valores aleatórios. Qual seria a consequência mais provável dessa mudança de projeto?

a. O cluster elegeria instantaneamente um líder, sem qualquer atraso.
b. Nenhuma, pois o valor do temporizador não afeta o processo de eleição.
c. O algoritmo deixaria de exigir maioria para eleger um líder.
d. Os seguidores deixariam de conseguir detectar a falha do líder.
*e. Maior chance de múltiplos nós se tornarem candidatos simultaneamente e empatarem repetidamente na votação, atrasando a eleição de um novo líder.

**33.** O líder de um cluster Raft de cinco nós replica uma nova entrada criada em seu termo corrente e recebe confirmação de apenas um seguidor, além de sua própria cópia local. Essa entrada pode ser considerada confirmada (*committed*)?

a. Não, pois o Raft exige confirmação unânime dos cinco nós antes de considerar qualquer entrada confirmada.
b. Sim, pois o líder e um seguidor já formam maioria suficiente.
c. Sim, pois basta que o líder tenha registrado a entrada em seu próprio log.
*d. Não, pois a confirmação exige maioria do cluster — neste caso, ao menos três dos cinco nós —, e apenas dois nós (líder e um seguidor) confirmaram até o momento.
e. Sim, pois qualquer replicação para pelo menos um nó além do líder já é suficiente no Raft.

**34.** Um nó que havia sido líder no termo 1 de um cluster Raft volta a operar após uma falha, sem saber que já existe um líder eleito no termo 2. O que se espera que aconteça quando esse nó voltar a se comunicar com o restante do cluster?

*a. Ele identificará, pelo número de termo recebido nas mensagens, que já existe um termo mais recente, reconhecerá que não é mais líder e passará a seguir o líder atual, reconciliando seu log.
b. O cluster inteiro entrará em um estado de erro irreversível, exigindo reinício manual.
c. Ele será permanentemente removido do cluster, sem possibilidade de voltar a participar.
d. Ele continuará agindo como líder do termo 1 indefinidamente, ignorando o termo 2.
e. Ele forçará automaticamente uma reversão do cluster para o termo 1.

**35.** A equipe da NexaOrder cogita usar o Raft, em sua formulação padrão, para coordenar nós operados por diferentes empresas parceiras, algumas das quais poderiam, em tese, enviar informações deliberadamente falsas ao cluster. O que os conceitos estudados na aula indicam sobre essa aplicação?

a. Isso não representa risco algum, pois o critério de maioria protege automaticamente contra qualquer tipo de falha, incluindo informações falsas.
b. O Raft padrão exige, nesse cenário, apenas a redução do número de nós para simplificar o consenso.
c. O problema seria resolvido apenas aumentando o número de nós do cluster, sem qualquer mudança de algoritmo.
d. O Raft padrão foi projetado especificamente para tolerar esse tipo de comportamento malicioso.
*e. O Raft padrão pressupõe falhas de parada ou de rede, não falhas bizantinas, de modo que participantes maliciosos exigiriam um algoritmo de consenso bizantino, fora do escopo do Raft convencional.

**36.** Durante uma transação distribuída coordenada por confirmação em duas fases, o coordenador falha exatamente após receber "pronto" de todos os participantes, mas antes de enviar a ordem final de confirmação. Qual é a consequência mais provável para os participantes?

*a. Os participantes permanecem bloqueados, com os recursos da transação retidos, até que o coordenador se recupere ou um processo de recuperação consulte seu registro de decisão.
b. Os participantes decidem automaticamente confirmar a transação de forma independente, sem qualquer risco.
c. O problema não existe no 2PC, pois o protocolo não depende de um coordenador central.
d. Os participantes desfazem automaticamente a transação, sem qualquer possibilidade de confirmação posterior.
e. A transação é concluída normalmente, pois a fase de preparação já é suficiente para garantir o resultado.

**37.** A equipe da NexaOrder projeta a saga da compra com um componente central que conhece toda a sequência de passos e envia comandos explícitos a cada serviço, aguardando confirmação antes de avançar para o próximo passo. Esse desenho caracteriza uma saga:

a. Baseada em confirmação em duas fases, pois existe um coordenador central.
b. Coreografada, pois cada serviço decide sozinho quando agir.
c. Equivalente, em todos os aspectos relevantes, a uma saga coreografada.
*d. Orquestrada, pois um componente central conhece o fluxo completo e comanda explicitamente cada etapa.
e. Sem qualquer mecanismo de coordenação, pois os serviços agem de forma totalmente independente.

**38.** Ao desenhar a compensação para uma etapa de pagamento já autorizado, a equipe da NexaOrder percebe que estornar a cobrança envolve prazos e taxas diferentes de simplesmente não ter processado a cobrança originalmente. Esse cenário ilustra qual princípio estudado na aula sobre ações compensatórias?

a. Compensações nunca devem ser aplicadas a operações financeiras, apenas a operações de estoque.
*b. Uma compensação nem sempre é o inverso perfeito da operação original, sendo tanto uma decisão técnica quanto uma decisão de negócio.
c. Compensações tornam-se desnecessárias quando o sistema utiliza o padrão *outbox*.
d. Ações compensatórias devem ser sempre o inverso matemático exato da operação original.
e. O estorno de pagamentos deve ser sempre instantâneo e sem qualquer custo adicional.

**39.** Um serviço da NexaOrder grava uma alteração de estoque em seu banco de dados e, em uma operação separada, publica um evento correspondente em um sistema de mensageria. O banco e o *broker* não participam de uma transação distribuída XA/2PC. Em um teste, o serviço falha exatamente entre as duas operações, e o evento nunca é publicado. Qual padrão estudado resolve o problema mantendo o registro do evento na mesma transação local do estado de negócio e publicando-o depois?

a. A eliminação completa da publicação de eventos entre serviços.
b. Aumento do número de réplicas do banco de dados de estoque.
c. Confirmação em duas fases entre o banco de dados e o sistema de mensageria.
d. Substituição da saga por uma transação distribuída única.
*e. O padrão *outbox*, que grava o evento a ser publicado na mesma transação local que grava a alteração de negócio, eliminando a janela entre as duas operações.

**40.** Um cliente da NexaOrder, após não receber confirmação por causa de uma falha de rede, reenvia a mesma compra com a **mesma chave de idempotência criada antes da primeira tentativa**. O serviço de pagamento verifica a chave antes de processar a requisição. Qual é o resultado esperado se ela já constar como concluída?

a. O sistema rejeita permanentemente a compra, sem retornar qualquer resposta ao cliente.
*b. O sistema reconhece a chave como já processada e devolve o resultado da operação original, sem processar uma nova cobrança, evitando a duplicação observada no incidente estudado na aula.
c. O sistema soma o valor da nova tentativa ao valor da tentativa anterior, cobrando o dobro.
d. O sistema ignora a chave de idempotência sempre que a requisição vem do mesmo cliente.
e. O sistema processa uma nova cobrança, pois toda nova requisição deve ser tratada como uma compra distinta.

## Gabarito e feedbacks

**Questão 1** (correta: b)
- a. Incorreta. A II é verdadeira, mas descreve corretamente a razão pela qual a I é verdadeira — não é o caso de "verdadeiras sem justificativa", já que aqui há justificativa direta.
- b. Correta. $W + R = 3 + 3 = 6 > 5 = N$, o que garante a interseção afirmada na I; a II apresenta exatamente a condição que explica essa sobreposição.
- c. Incorreta. A I é verdadeira porque descreve apenas a interseção dos conjuntos. Essa interseção, isoladamente, não garantiria linearizabilidade nem a escolha automática da versão mais recente; ainda são necessários metadados de versão e reconciliação.
- d. Incorreta. Ambas as asserções são verdadeiras, não falsas.
- e. Incorreta. A II também é verdadeira: a soma $W + R$ de fato excede $N$ nessa configuração.

**Questão 2** (correta: d)
- a. Incorreta. A I é verdadeira: multi-líder realmente permite escritas locais de baixa latência em regiões diferentes.
- b. Incorreta. A I é verdadeira, mas a II também é verdadeira — replicação líder-seguidor de fato concentra escritas em um único nó.
- c. Incorreta. Ambas as asserções são verdadeiras, apenas não relacionadas por justificativa.
- d. Correta. Ambas as asserções são verdadeiras, mas a II descreve a replicação líder-seguidor, um mecanismo diferente do discutido na I (multi-líder); portanto, não justifica a I.
- e. Incorreta. As duas asserções são verdadeiras, mas a II não justifica a I: líder único e multi-líder são estratégias distintas de replicação.

**Questão 3** (correta: e)
- a. Incorreta. Pelo mesmo motivo, a II não pode ser considerada verdadeira.
- b. Incorreta. A II é falsa: replicação assíncrona não elimina o risco de perda de dados, que existe enquanto nenhuma réplica durável recebeu a escrita confirmada.
- c. Incorreta. A I é verdadeira; apenas a II é falsa.
- d. Incorreta. A I é verdadeira, não falsa: o ponto definidor é não aguardar a confirmação das réplicas antes de responder ao cliente.
- e. Correta. A I é verdadeira — o líder responde sem aguardar confirmações das réplicas, embora possa já ter iniciado a propagação —, e a II é falsa, pois existe risco real de perda se ele falhar antes que outra réplica durável receba a escrita.

**Questão 4** (correta: c)
- a. Incorreta. A II é verdadeira, não falsa.
- b. Incorreta. A I é falsa, não verdadeira: consistência eventual não garante retorno imediato do mesmo valor após uma escrita.
- c. Correta. A I é falsa, pois contradiz a própria definição de consistência eventual, e a II descreve corretamente a convergência sob as hipóteses declaradas.
- d. Incorreta. A II é verdadeira, não falsa: ela declara tanto a ausência de novas escritas quanto a continuidade ou recuperação da replicação.
- e. Incorreta. Pelo mesmo motivo, a I não pode ser considerada verdadeira.

**Questão 5** (correta: a)
- a. Correta. A I é falsa, pois garantias centradas no cliente podem ser oferecidas sem consistência forte global; a II é falsa, pois inverte a definição real de leitura de prefixo consistente.
- b. Incorreta. A II também é falsa, não verdadeira: a leitura de prefixo consistente garante o oposto do afirmado — impede observar B sem A.
- c. Incorreta. Nenhuma das duas asserções é verdadeira nesse par.
- d. Incorreta. A I é falsa, não verdadeira: garantias centradas no cliente não exigem, necessariamente, consistência forte global.
- e. Incorreta. Idem: ambas são falsas, não verdadeiras.

**Questão 6** (correta: d)
- a. Incorreta. A I é verdadeira sob as hipóteses explícitas de bom espalhamento, diversidade de chaves e partições equilibradas.
- b. Incorreta. A II justifica a tendência afirmada na I ao descrever a propriedade de espalhamento, sem prometer uniformidade para qualquer função ou conjunto de dados.
- c. Incorreta. Ambas as asserções são verdadeiras.
- d. Correta. Sob as hipóteses declaradas na I, ambas as asserções são verdadeiras, e a II explica como o bom espalhamento reduz concentrações ligadas à ordem original das chaves.
- e. Incorreta. A II também é verdadeira, não falsa.

**Questão 7** (correta: a)
- a. Correta. Ambas as afirmações são verdadeiras, mas tratam de estratégias diferentes de particionamento; a II não é justificativa da I.
- b. Incorreta. A II descreve o particionamento por diretório, um mecanismo distinto, e não explica por que o *hashing* consistente reduz a redistribuição de chaves.
- c. Incorreta. Ambas as asserções são verdadeiras.
- d. Incorreta. A I é verdadeira: essa é exatamente a vantagem central do *hashing* consistente sobre o *hash* simples por módulo.
- e. Incorreta. A II também é verdadeira: tabelas de diretório realmente exigem disponibilidade própria.

**Questão 8** (correta: e)
- a. Incorreta. A II é falsa: o *hashing* consistente não resolve pontos quentes de chave única.
- b. Incorreta. A I é verdadeira; apenas a II é falsa.
- c. Incorreta. Pelo mesmo motivo, a II não pode ser tida como verdadeira.
- d. Incorreta. A I é verdadeira, não falsa: é exatamente o comportamento observado no caso da NexaOrder.
- e. Correta. A I é verdadeira — pontos quentes de chave única persistem mesmo com boa estratégia de particionamento —, e a II é falsa, pois contradiz diretamente essa limitação.

**Questão 9** (correta: a)
- a. Correta. A I é falsa, pois generaliza incorretamente o teorema CAP para fora do cenário de partição, e a II é verdadeira, descrevendo corretamente seu escopo.
- b. Incorreta. A I é falsa, não verdadeira: o CAP trata do comportamento durante uma partição, não de uma escolha permanente.
- c. Incorreta. Pelo mesmo motivo, a I não pode ser considerada verdadeira.
- d. Incorreta. A II é verdadeira, não falsa.
- e. Incorreta. A II é verdadeira, não falsa: essa é exatamente a formulação correta do teorema CAP.

**Questão 10** (correta: d)
- a. Incorreta. A II também é falsa, não verdadeira: a superioridade de uma estratégia de particionamento depende do padrão de consultas, não é absoluta.
- b. Incorreta. A I é falsa, não verdadeira: o PACELC afirma justamente o oposto — mesmo sem partição, existe compromisso entre latência e consistência.
- c. Incorreta. Nenhuma das duas asserções é verdadeira.
- d. Correta. A I é falsa, pois inverte o argumento central do PACELC, e a II é falsa, pois nenhuma estratégia de particionamento é superior em qualquer cenário.
- e. Incorreta. Idem, ambas são falsas.

**Questão 11** (correta: a)
- a. Correta. Ambas as asserções são verdadeiras, e a fórmula apresentada na II explica diretamente o resultado numérico afirmado na I.
- b. Incorreta. Ambas as asserções são verdadeiras.
- c. Incorreta. A II justifica sim a I, fornecendo a fórmula geral da qual o caso $N=5$ é uma aplicação direta.
- d. Incorreta. A II também é verdadeira: a fórmula $f = \lfloor (N-1)/2 \rfloor$ é exatamente a estudada na aula.
- e. Incorreta. A I é verdadeira, não falsa: um cluster de cinco nós realmente tolera até duas falhas simultâneas.

**Questão 12** (correta: c)
- a. Incorreta. A I é verdadeira: o uso de temporizadores aleatórios é exatamente a estratégia do Raft para reduzir empates em eleições simultâneas.
- b. Incorreta. A II descreve a divisão em termos do Raft, um mecanismo relacionado, mas que não explica por que os temporizadores aleatórios reduzem disputas simultâneas.
- c. Correta. Ambas as afirmações são verdadeiras, mas a II trata de um aspecto diferente do Raft (numeração de termos) e não justifica a I (uso de temporizadores aleatórios).
- d. Incorreta. Ambas as asserções são verdadeiras.
- e. Incorreta. A II também é verdadeira: termos numerados com um único líder por termo são parte central do Raft.

**Questão 13** (correta: b)
- a. Incorreta. Pelo mesmo motivo, a II não pode ser considerada verdadeira.
- b. Correta. A I explicita a regra para uma entrada do termo corrente; a II é falsa porque uma entrada confirmada não pode desaparecer nem ser substituída.
- c. Incorreta. A I é verdadeira; apenas a II é falsa.
- d. Incorreta. A I é verdadeira, não falsa. Entradas de termos anteriores têm uma nuance adicional: não são confirmadas diretamente só pela contagem de réplicas, mas indiretamente quando uma entrada posterior do termo corrente é confirmada.
- e. Incorreta. A II é falsa: uma entrada confirmada não pode ser removida ou substituída, por definição da propriedade de segurança do Raft.

**Questão 14** (correta: d)
- a. Incorreta. A II é verdadeira, não falsa.
- b. Incorreta. A I é falsa, não verdadeira: sem maioria ativa, o Raft não garante disponibilidade de escrita.
- c. Incorreta. Pelo mesmo motivo, a I não pode ser considerada verdadeira.
- d. Correta. A I é falsa, pois inverte a real exigência de maioria para disponibilidade, e a II é verdadeira, descrevendo corretamente essa dependência.
- e. Incorreta. A II é verdadeira, não falsa: a disponibilidade do Raft realmente depende de comunicação suficiente entre a maioria.

**Questão 15** (correta: b)
- a. Incorreta. A II também é falsa, não verdadeira: o Raft opera com um único líder por termo, não com múltiplos líderes em paralelo.
- b. Correta. A I é falsa, pois o Raft padrão pressupõe apenas falhas de parada ou de rede, e a II é falsa, pois o *throughput* do Raft é limitado pela capacidade de um único líder, não cresce com múltiplos líderes.
- c. Incorreta. A I é falsa, não verdadeira: o Raft padrão não tolera falhas bizantinas.
- d. Incorreta. Nenhuma das duas asserções é verdadeira.
- e. Incorreta. Idem, ambas são falsas.

**Questão 16** (correta: c)
- a. Incorreta. Ambas as asserções são verdadeiras.
- b. Incorreta. A II também é verdadeira: participantes de fato mantêm recursos bloqueados durante a fase de preparação do 2PC.
- c. Correta. Ambas as asserções são verdadeiras, e a II explica diretamente por que a falha do coordenador nesse intervalo bloqueia os participantes.
- d. Incorreta. A I é verdadeira, não falsa: esse é exatamente o problema clássico de bloqueio do 2PC discutido na aula.
- e. Incorreta. A II justifica sim a I, descrevendo exatamente o mecanismo de bloqueio de recursos responsável pelo problema afirmado na I.

**Questão 17** (correta: b)
- a. Incorreta. A I é verdadeira: essa é exatamente a definição de saga apresentada na aula.
- b. Correta. Ambas as afirmações são verdadeiras, mas tratam de conceitos diferentes; a II não é justificativa da I.
- c. Incorreta. A II também é verdadeira: essa é exatamente a definição do padrão *outbox* estudado na aula.
- d. Incorreta. Ambas as asserções são verdadeiras.
- e. Incorreta. A II descreve o padrão *outbox*, um mecanismo relacionado, mas distinto do motivo pelo qual sagas substituem uma transação única por transações locais.

**Questão 18** (correta: e)
- a. Incorreta. Pelo mesmo motivo, a II não pode ser considerada verdadeira.
- b. Incorreta. A I é verdadeira; apenas a II é falsa.
- c. Incorreta. A II é falsa: compensações nem sempre são o inverso matemático exato da operação original.
- d. Incorreta. A I é verdadeira, não falsa: essa é exatamente a definição de ação compensatória estudada na aula.
- e. Correta. A I é verdadeira — compensações revertem logicamente uma etapa concluída —, e a II é falsa, pois generaliza incorretamente a compensação como inverso matemático perfeito.

**Questão 19** (correta: c)
- a. Incorreta. Pelo mesmo motivo, a I não pode ser considerada verdadeira.
- b. Incorreta. A II é verdadeira, não falsa: entrega pelo menos uma vez é de fato o padrão típico desses sistemas.
- c. Correta. A I é falsa, pois inverte a garantia real oferecida pela maioria dos sistemas de mensageria, e a II é verdadeira, descrevendo corretamente essa garantia e sua implicação.
- d. Incorreta. A I é falsa, não verdadeira: sistemas de mensageria distribuída não garantem, por padrão, entrega exatamente uma vez.
- e. Incorreta. A II é verdadeira, não falsa.

**Questão 20** (correta: a)
- a. Correta. A I é falsa porque o ID do inbox e o efeito de negócio devem ser confirmados na mesma transação local; a II é falsa porque a orquestração concentra o conhecimento do fluxo no orquestrador.
- b. Incorreta. Nenhuma das duas asserções é verdadeira.
- c. Incorreta. Idem, ambas são falsas.
- d. Incorreta. A II também é falsa: a saga orquestrada mantém um componente central que conhece a sequência completa do processo.
- e. Incorreta. A I é falsa: se o processo cair depois de confirmar o ID e antes do efeito, a reentrega será descartada e a operação será perdida.

**Questão 21** (correta: d)
- a. Incorreta. $W = 1$ garante apenas que uma réplica confirmou a escrita, não que todas as réplicas — nem a lida — já a receberam.
- b. Incorreta. A configuração não elimina o atraso de réplica; pelo contrário, ela o torna mais perceptível, pois não há verificação de sobreposição na leitura.
- c. Incorreta. A configuração é válida; é uma escolha legítima que prioriza latência em detrimento de garantias de atualidade.
- d. Correta. Com $W = 1$ e $R = 1$, não há garantia de sobreposição entre o nó que recebeu a escrita e o nó consultado na leitura, o que pode resultar em leitura obsoleta.
- e. Incorreta. O sistema não rejeita leituras nessa configuração; ele prioriza responder rapidamente, mesmo com risco de desatualização.

**Questão 22** (correta: e)
- a. Incorreta. Não há restrição que impeça $W$ e $R$ de assumirem o mesmo valor.
- b. Incorreta. A configuração exige apenas três das cinco réplicas, não todas.
- c. Incorreta. É o oposto de $W=1$ e $R=1$: essa configuração oferece garantia de sobreposição, que aquela não oferece.
- d. Incorreta. A configuração com $W=3$ e $R=3$ não prioriza exclusivamente disponibilidade; ela busca equilíbrio, oferecendo garantia de sobreposição.
- e. Correta. $3 + 3 = 6 > 5$, garantindo sobreposição entre os conjuntos de réplicas, ao custo de exigir resposta de três réplicas por operação.

**Questão 23** (correta: b)
- a. Incorreta. Consistência sequencial é uma garantia mais ampla, sobre a ordem global de operações, e não descreve especificamente essa expectativa individual do cliente.
- b. Correta. A leitura das próprias escritas garante exatamente que um cliente veja as alterações que ele mesmo realizou, mesmo que outras réplicas ainda estejam desatualizadas.
- c. Incorreta. Leituras monotônicas garantem que um cliente não veja um valor mais antigo após já ter observado um mais novo, mas não tratam especificamente das próprias escritas do cliente.
- d. Incorreta. Leitura de prefixo consistente trata da ordem causal entre escritas relacionadas, não da visibilidade das próprias escritas de um cliente específico.
- e. Incorreta. Escritas monotônicas garantem a ordem de aplicação das escritas de um cliente, não a visibilidade dessas escritas em leituras subsequentes.

**Questão 24** (correta: e)
- a. Incorreta. Abandonar a replicação multi-líder é uma solução possível, mas não é o que "esse cenário exige" segundo os conceitos da aula — a exigência imediata é uma regra de resolução de conflitos.
- b. Incorreta. Promover um centro a líder global eliminaria a vantagem de latência local que motivou a escolha por multi-líder.
- c. Incorreta. A conversão automática para consistência forte não ocorre sem uma decisão explícita de arquitetura.
- d. Incorreta. A replicação multi-líder não impede escritas concorrentes sobre o mesmo dado; pelo contrário, ela as torna possíveis.
- e. Correta. Escritas concorrentes em líderes diferentes sobre o mesmo dado exigem uma regra explícita de resolução de conflitos, como discutido na aula.

**Questão 25** (correta: c)
- a. Incorreta. Consistência eventual pura não é coerente com o risco financeiro descrito, pois permitiria leituras obsoletas durante decisões de cobrança.
- b. Incorreta. Priorizar exclusivamente a latência de escrita, sem quórum, aumentaria o risco de leituras obsoletas em um dado sensível a erro financeiro.
- c. Correta. Dado o risco financeiro de uma leitura obsoleta durante a confirmação de uma cobrança, a aula recomenda consistência próxima da forte para esse tipo de dado, mesmo com maior custo de latência.
- d. Incorreta. Modelos de consistência são, sim, aplicáveis a dados financeiros distribuídos — é exatamente o tema da aula.
- e. Incorreta. Leituras monotônicas sozinhas não impedem que uma leitura reflita um estado anterior à confirmação mais recente da cobrança.

**Questão 26** (correta: b)
- a. Incorreta. O comportamento descrito é uma consequência esperada da estratégia de particionamento escolhida, não uma falha do banco de dados.
- b. Correta. O particionamento por faixa distribui bem quando as chaves são uniformemente distribuídas, mas concentra carga quando um subconjunto de chaves — como nomes começando com "S" — recebe demanda desproporcional.
- c. Incorreta. O particionamento por diretório não elimina automaticamente pontos quentes; ele exige configuração e rebalanceamento explícitos.
- d. Incorreta. Pontos quentes também ocorrem no particionamento por faixa, como demonstra o próprio cenário descrito.
- e. Incorreta. É exatamente o oposto: o particionamento por faixa não garante uniformidade quando o padrão de acesso não é uniforme.

**Questão 27** (correta: c)
- a. Incorreta. A fração redistribuída não é fixa em 50%; ela depende do número de nós existentes no anel.
- b. Incorreta. A redistribuição no *hashing* consistente depende da posição dos nós no anel, relacionada ao número de nós, não apenas ao número de réplicas.
- c. Correta. O *hashing* consistente redistribui apenas a fração aproximada de $1/(N+1)$ das chaves ao adicionar um nó, preservando a posição das demais no anel.
- d. Incorreta. Essa seria a consequência de um *hash* simples por módulo, não do *hashing* consistente, que é justamente projetado para evitar essa redistribuição massiva.
- e. Incorreta. Uma fração das chaves é sim redistribuída — apenas muito menor do que ocorreria com *hash* simples por módulo.

**Questão 28** (correta: a)
- a. Correta. Cache ou réplicas distribuem as leituras informativas sem transformar cada consulta em um *scatter-gather*; expiração ou versionamento tornam explícita a defasagem aceita, enquanto a reserva mantém sua coordenação autoritativa.
- b. Incorreta. Migrar para particionamento por faixa não resolve o problema de ponto quente de chave única; a estratégia por faixa é ainda mais vulnerável a esse tipo de concentração.
- c. Incorreta. O *hashing* consistente distribui bem chaves diferentes entre si, mas não divide a carga de uma única chave extremamente popular.
- d. Incorreta. Bloquear leituras do produto prejudicaria diretamente o negócio durante o período de maior demanda, contrariando o objetivo da mitigação.
- e. Incorreta. Aumentar o número de partições não resolve, sozinho, a concentração de tráfego sobre uma única chave popular.

**Questão 29** (correta: c)
- a. Incorreta. O comportamento descrito não viola o CAP; ele exemplifica exatamente uma das escolhas possíveis previstas pelo teorema.
- b. Incorreta. O sistema demonstra tolerância a partição justamente por continuar operando apesar da falha de rede; não é essa dimensão que está ausente na escolha.
- c. Correta. Continuar respondendo em ambos os lados da partição, aceitando divergência temporária, caracteriza uma escolha AP.
- d. Incorreta. Um sistema CP recusaria ou atrasaria respostas para preservar consistência, o oposto do comportamento descrito.
- e. Incorreta. Não existe sistema CA sob partição de rede real; consistência e disponibilidade simultâneas e irrestritas não são sustentáveis quando a comunicação entre nós é interrompida.

**Questão 30** (correta: d)
- a. Incorreta. Exigir confirmação unânime tende a reduzir a disponibilidade em caso de lentidão ou falha de qualquer réplica, não a aumentá-la.
- b. Incorreta. A escolha descrita não elimina o atraso de réplica em geral; ela apenas aumenta a exigência de confirmação para cada escrita específica.
- c. Incorreta. Exigir confirmação de todas as réplicas afeta principalmente a latência de escrita, não o *throughput* de leitura.
- d. Correta. Segundo o PACELC, exigir consistência elevada implica maior latência de escrita mesmo no funcionamento cotidiano, sem qualquer partição de rede envolvida.
- e. Incorreta. O PACELC trata explicitamente também do compromisso fora de cenários de partição, que é o próprio ponto central da extensão ao CAP.

**Questão 31** (correta: c)
- a. Incorreta. Apenas um dos grupos pode formar maioria em um cluster de sete nós; ambos não podem simultaneamente satisfazer esse critério.
- b. Incorreta. O grupo de quatro nós consegue, sim, eleger um líder, pois constitui maioria.
- c. Correta. Em um cluster de sete nós, a maioria mínima é de quatro; apenas o grupo com quatro nós consegue formar essa maioria e continuar operando.
- d. Incorreta. A maioria é justamente o critério central usado pelo Raft para eleição de líder e confirmação de entradas.
- e. Incorreta. O tamanho do grupo isoladamente não determina a formação de maioria; o critério é numérico em relação ao total de nós do cluster.

**Questão 32** (correta: e)
- a. Incorreta. Pelo contrário, temporizadores fixos tenderiam a atrasar, não acelerar, a eleição de um novo líder, devido a empates repetidos.
- b. Incorreta. O valor do temporizador afeta diretamente a probabilidade de disputas simultâneas entre candidatos.
- c. Incorreta. A exigência de maioria é independente do valor do temporizador; ela permanece um critério do algoritmo.
- d. Incorreta. A detecção de falha do líder depende da ausência de sinais dentro do intervalo do temporizador, não do fato de ele ser aleatório ou fixo.
- e. Correta. Temporizadores fixos e iguais aumentam a chance de múltiplos seguidores se tornarem candidatos ao mesmo tempo, gerando eleições empatadas e atrasando a escolha de um novo líder.

**Questão 33** (correta: d)
- a. Incorreta. O Raft exige maioria, não unanimidade, para confirmar uma entrada de log.
- b. Incorreta. Líder mais um seguidor totalizam dois nós, abaixo da maioria de três exigida em um cluster de cinco.
- c. Incorreta. O registro apenas no log do líder, sem confirmação da maioria, não é suficiente para considerar a entrada confirmada.
- d. Correta. A confirmação exige maioria — três dos cinco nós —, e o cenário descrito apresenta apenas dois nós confirmados (líder e um seguidor), abaixo do necessário.
- e. Incorreta. Um único seguidor além do líder não é suficiente; é necessário atingir a maioria do cluster.

**Questão 34** (correta: a)
- a. Correta. Ao identificar um número de termo mais recente nas mensagens recebidas, o nó reconhece que não é mais líder, passa a seguir o líder atual e reconcilia seu log com o do cluster.
- b. Incorreta. O cluster não entra em erro irreversível; o protocolo foi projetado justamente para lidar com esse tipo de reintegração de nó.
- c. Incorreta. O nó não é removido permanentemente; ele pode voltar a participar normalmente do cluster como seguidor.
- d. Incorreta. O nó não continuaria agindo como líder indefinidamente; o número de termo nas mensagens recebidas o levaria a reconhecer que não é mais líder.
- e. Incorreta. Não há reversão do cluster para um termo anterior; termos avançam, nunca retrocedem, no Raft.

**Questão 35** (correta: e)
- a. Incorreta. O critério de maioria protege contra a indisponibilidade de nós, mas não contra informações deliberadamente falsas enviadas por um nó ainda ativo.
- b. Incorreta. Reduzir o número de nós não trata do problema de participantes maliciosos; pelo contrário, reduziria a tolerância a falhas do cluster.
- c. Incorreta. Aumentar o número de nós, sozinho, não resolve o problema de tolerância a falhas bizantinas, que exige um algoritmo de consenso diferente.
- d. Incorreta. O Raft padrão não foi projetado para tolerar comportamento malicioso deliberado; ele pressupõe falhas de parada ou de rede.
- e. Correta. O Raft padrão pressupõe falhas de parada ou de rede, não falhas bizantinas; coordenar participantes potencialmente maliciosos exigiria um algoritmo de consenso bizantino, fora do escopo do Raft convencional.

**Questão 36** (correta: a)
- a. Correta. Sem a decisão final do coordenador, os participantes não sabem se devem confirmar ou desfazer, permanecendo bloqueados até a recuperação do coordenador ou de um registro de decisão.
- b. Incorreta. Participantes não decidem de forma independente no 2PC; essa é justamente a limitação central do protocolo diante da falha do coordenador.
- c. Incorreta. O 2PC depende, por definição, de um coordenador central que conduz as duas fases do protocolo.
- d. Incorreta. Os participantes não podem desfazer automaticamente, pois já sinalizaram "pronto" e aguardam a decisão final, que pode ainda ser de confirmação.
- e. Incorreta. A fase de preparação, isoladamente, não conclui a transação; a confirmação depende da segunda fase.

**Questão 37** (correta: d)
- a. Incorreta. A saga orquestrada não é uma instância de confirmação em duas fases; diferentemente do 2PC, ela não bloqueia recursos durante a espera.
- b. Incorreta. Em uma saga coreografada não existe um componente central comandando explicitamente cada etapa; os serviços reagem a eventos de forma independente.
- c. Incorreta. Saga orquestrada e saga coreografada diferem justamente na existência ou ausência de um componente central, o que as torna distintas, não equivalentes.
- d. Correta. A existência de um componente central que conhece o fluxo completo e envia comandos explícitos a cada serviço é a definição de saga orquestrada.
- e. Incorreta. O desenho descrito possui, sim, um mecanismo explícito de coordenação central.

**Questão 38** (correta: b)
- a. Incorreta. Compensações são aplicáveis a operações financeiras; o cenário trata exatamente de uma compensação de pagamento.
- b. Correta. O cenário ilustra que uma compensação nem sempre é o inverso perfeito da operação original, envolvendo decisões técnicas e de negócio, como prazos e taxas de estorno.
- c. Incorreta. O padrão *outbox* trata da publicação confiável de eventos, não elimina a necessidade de ações compensatórias em caso de falha em etapas posteriores.
- d. Incorreta. O cenário descrito demonstra exatamente o contrário: a compensação envolve diferenças de prazo e custo em relação à operação original.
- e. Incorreta. O próprio cenário descreve o oposto: o estorno envolve prazos e taxas diferentes de uma reversão instantânea e sem custo.

**Questão 39** (correta: e)
- a. Incorreta. Eliminar a publicação de eventos comprometeria a comunicação entre os serviços da saga, não resolvendo o problema de forma construtiva.
- b. Incorreta. Aumentar réplicas do banco de dados não resolve o problema da escrita dupla entre banco de dados e mensageria.
- c. Incorreta. Se banco e *broker* oferecessem integração XA/2PC, uma transação distribuída poderia coordená-los, com seus custos e hipóteses. O enunciado exclui esse suporte e pede uma solução baseada na mesma transação local do estado de negócio.
- d. Incorreta. Além de o enunciado excluir XA/2PC entre banco e *broker*, substituir toda a saga por uma transação distribuída amplia o escopo e não corresponde ao padrão local solicitado.
- e. Correta. O padrão *outbox* grava o evento na mesma transação local da alteração de negócio, eliminando a janela em que uma das duas operações poderia falhar isoladamente.

**Questão 40** (correta: b)
- a. Incorreta. O sistema não rejeita permanentemente a compra; ele reconhece a repetição e devolve o resultado já processado.
- b. Correta. Como a chave foi criada antes do primeiro envio e reutilizada, o serviço reconhece a mesma operação lógica e devolve seu resultado registrado sem gerar nova cobrança. No serviço, a reserva da chave, a cobrança e o resultado devem ter uma fronteira atômica ou usar idempotência equivalente no provedor externo.
- c. Incorreta. Somar os valores das duas tentativas seria uma forma de duplicação, exatamente o que a chave de idempotência busca evitar.
- d. Incorreta. A chave de idempotência deve ser verificada independentemente da origem da requisição, não apenas quando conveniente.
- e. Incorreta. Uma nova requisição só representa nova compra quando identifica outra operação lógica; uma retentativa com a mesma chave não deve gerar novo efeito.
