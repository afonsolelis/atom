# Unidade 2 — Dados distribuídos, consistência e coordenação

Disciplina: Distributed Systems Engineering  
Professor-conteudista: Afonso Cesar Lelis Brandão  
Prazo de produção: 16 de agosto de 2026

## Relação da unidade com a atuação profissional

Toda plataforma que armazena dados em mais de um lugar precisa responder a uma pergunta que parece simples e não é: quando duas cópias divergem, qual delas está certa? Bancos que replicam saldos entre agências, marketplaces que sincronizam estoque entre centros de distribuição, aplicativos de mobilidade que replicam localização entre regiões e sistemas de saúde que espelham prontuários entre unidades convivem, todos os dias, com esse problema. A resposta não é única: depende do que o negócio pode tolerar, por quanto tempo e com qual custo.

Esta unidade prepara o profissional para tomar essas decisões de forma explícita. Você estudará por que dados são replicados, como réplicas podem divergir, o que significa consistência forte ou eventual, como um conjunto de dados pode ser particionado entre muitos nós e por que, durante uma falha de rede, um sistema é obrigado a escolher entre continuar disponível ou permanecer perfeitamente consistente. Você também estudará como máquinas concordam entre si mesmo quando algumas falham — o problema do consenso — e como algoritmos como o Raft resolvem esse problema de forma compreensível e auditável. Por fim, você verá como transações que atravessam vários serviços podem ser mantidas coerentes sem um bloqueio global, usando sagas, ações compensatórias e idempotência.

Esses temas aparecem no cotidiano de quem projeta bancos de dados distribuídos, arquiteturas de microsserviços, plataformas de pagamento, sistemas de estoque em tempo real e serviços de infraestrutura em nuvem. Um engenheiro de dados precisa saber por que uma consulta analítica pode ler um valor desatualizado. Um arquiteto de soluções precisa justificar, perante o negócio, por que optou por consistência eventual no catálogo e consistência forte no pagamento. Um SRE precisa entender por que a perda de um nó líder pode interromper escritas por alguns segundos até uma nova eleição. Um desenvolvedor de backend precisa saber projetar operações idempotentes para que uma repetição de mensagem não gere um pedido duplicado ou uma cobrança duplicada.

Dominar esse vocabulário evita dois erros comuns e caros: tratar qualquer inconsistência temporária como um bug a ser eliminado a qualquer custo, e ignorar completamente os riscos de duplicação e divergência até que eles cheguem à produção como incidentes. Entre esses extremos está o trabalho real da engenharia de sistemas distribuídos: escolher, para cada dado, a garantia adequada ao risco que ele representa.

## O que você verá nesta unidade

A Unidade 2 acompanha a NexaOrder em um novo estágio: os serviços de pedidos, estoque, pagamento e expedição, já decompostos na Unidade 1, agora precisam armazenar e sincronizar dados em múltiplas cópias. Na Aula 5, você estudará estratégias de replicação e os principais modelos de consistência, incluindo quóruns de leitura e escrita. Na Aula 6, examinará como particionar grandes volumes de dados, como o hashing consistente reduz o custo de rebalanceamento e como o teorema CAP — estendido pelo PACELC — descreve os compromissos entre consistência, disponibilidade e latência. Na Aula 7, você investigará o problema do consenso e o algoritmo Raft, entendendo como um conjunto de nós elege um líder e mantém um log replicado mesmo diante de falhas. Na Aula 8, fechará a unidade estudando transações distribuídas, a confirmação em duas fases, sagas coreografadas e orquestradas, e os padrões que garantem processamento idempotente.

Ao final desta unidade, você será capaz de escolher e justificar estratégias de replicação, particionamento, consenso e transação distribuída para um sistema real, relacionando cada decisão a evidências e a compromissos explícitos — exatamente como fez na Unidade 1 ao justificar decisões de arquitetura, comunicação e tolerância a falhas.

## Aula 5 — Replicação e modelos de consistência

### Situação-problema: três cópias, três respostas diferentes

Depois de decompor a NexaOrder em serviços independentes, a equipe percebeu que um único banco de dados por serviço ainda representava um ponto único de falha e um gargalo de leitura. A solução óbvia — manter cópias do mesmo dado em vários nós — resolveu a disponibilidade, mas criou um problema novo. Durante uma promoção relâmpago, um cliente consultou o catálogo em três momentos consecutivos e recebeu três preços diferentes, todos supostamente “atuais”. Em paralelo, o time de operações registrou um caso mais grave: uma reserva de estoque confirmada em uma réplica não havia chegado a outra, e um segundo cliente conseguiu reservar a mesma unidade do mesmo produto.

Nenhuma dessas réplicas “mentiu”. Cada uma respondeu com exatidão ao que já havia recebido. O problema está em não termos definido, para cada tipo de dado, qual garantia de consistência era necessária e qual mecanismo de replicação a sustentaria. Esta aula constrói esse raciocínio.

### Por que replicar dados

Replicação é a manutenção de cópias do mesmo dado em nós diferentes. As motivações mais comuns são:

1. **Disponibilidade:** se um nó falhar, outra cópia continua respondendo.
2. **Redução de latência:** servir leituras a partir do nó geograficamente mais próximo do cliente.
3. **Escalabilidade de leitura:** distribuir um volume grande de consultas entre várias réplicas.
4. **Durabilidade:** reduzir a chance de perda definitiva de dados após a falha de um único nó.

Nenhum desses benefícios é gratuito. Toda cópia adicional introduz a pergunta central desta aula: como manter réplicas coerentes o suficiente para o uso que se pretende dar a elas, sem sacrificar o benefício que motivou a replicação.

### Replicação primário-réplica (líder-seguidor)

No modelo primário-réplica, também chamado *líder-seguidor*, um nó — o líder — recebe todas as escritas e as propaga para um ou mais seguidores. Leituras podem ser atendidas pelo líder ou pelos seguidores, dependendo da garantia desejada.

Esse modelo tem uma vantagem estrutural: como existe um único ponto de escrita, não há disputa entre líderes sobre qual valor é o correto. A desvantagem é que o líder se torna, ao mesmo tempo, um possível gargalo de escrita e um ponto que exige mecanismo de recuperação quando falha — tema retomado na Aula 7, ao tratarmos de eleição de líder.

### Replicação multi-líder

Na replicação multi-líder, mais de um nó aceita escritas, e cada um propaga suas mudanças para os demais. O modelo é útil quando existem múltiplas regiões geográficas, cada uma escrevendo localmente para reduzir latência — por exemplo, centros de distribuição da NexaOrder em diferentes países atualizando seu próprio estoque local.

O custo aparece quando dois líderes aceitam escritas concorrentes sobre o mesmo dado. Se um centro de distribuição registra a saída de uma unidade e, quase simultaneamente, outro registra uma correção de inventário para o mesmo item, o sistema precisa de uma regra de resolução de conflito — por exemplo, prevalência do último timestamp, mesclagem de campos ou intervenção manual. Sem essa regra explícita, o comportamento do sistema em conflito é imprevisível.

> **Recurso visual 1 — Líder único versus múltiplos líderes:** dois diagramas lado a lado; à esquerda, um líder recebendo escritas e replicando para dois seguidores; à direita, dois líderes em regiões diferentes replicando um para o outro, com um ícone de conflito na interseção.  
> **Texto alternativo:** comparação entre replicação de líder único, sem conflitos de escrita, e replicação multi-líder, na qual escritas concorrentes em regiões diferentes podem colidir.

### Replicação síncrona e assíncrona

Um segundo eixo de decisão é quando a escrita é considerada concluída.

- **Replicação síncrona:** o líder só confirma a escrita ao cliente depois que uma ou mais réplicas confirmaram tê-la recebido. Aumenta a durabilidade e reduz o risco de perda, mas eleva a latência da escrita e torna o líder dependente da disponibilidade das réplicas envolvidas.
- **Replicação assíncrona:** o líder confirma a escrita imediatamente e propaga a mudança em segundo plano. A latência de escrita é menor, mas existe uma janela em que uma falha do líder pode perder dados ainda não replicados.

Um esquema intermediário, a **replicação semissíncrona**, exige confirmação de apenas parte das réplicas, equilibrando durabilidade e latência — ideia que retomaremos como quórum de escrita.

### Atraso de réplica e leituras obsoletas

O intervalo entre a confirmação da escrita no líder e sua aplicação em uma réplica é o *atraso de réplica*, ou *replication lag*. Enquanto esse atraso existe, uma leitura na réplica pode retornar um valor mais antigo que o valor já confirmado no líder — uma leitura obsoleta.

Suponha que o líder confirme uma escrita no instante $t_0$ e que a réplica aplique essa escrita apenas em $t_0 + \Delta$, com $\Delta = 150\,\text{ms}$ nesse cenário. Qualquer leitura dirigida a essa réplica entre $t_0$ e $t_0 + \Delta$ observará o estado anterior. Isso explica o caso do catálogo na situação-problema: cada consulta pode ter sido atendida por uma réplica diferente, cada uma em um ponto distinto de sua própria janela de atraso.

O atraso de réplica não é, isoladamente, um defeito. Ele se torna um problema quando o processo de negócio pressupõe, implicitamente, uma consistência que o sistema não oferece.

### Modelos de consistência

Os modelos de consistência descrevem quais garantias um sistema replicado oferece sobre a ordem e a visibilidade das atualizações.

- **Consistência forte (linearizabilidade):** o sistema se comporta como se existisse uma única cópia dos dados; toda leitura reflete a escrita mais recente já confirmada, na ordem real do tempo. É a garantia mais cara em latência e disponibilidade.
- **Consistência sequencial:** todas as réplicas concordam com a mesma ordem de operações, mas essa ordem não precisa coincidir exatamente com a ordem real de tempo entre operações de clientes diferentes.
- **Consistência causal:** operações que têm relação de causa e efeito são vistas na mesma ordem por todos os nós; operações verdadeiramente concorrentes podem ser vistas em ordens diferentes. É uma retomada direta da relação *happened-before*, estudada na Aula 3.
- **Consistência eventual:** garante apenas que, se não houver novas escritas, todas as réplicas convergirão para o mesmo valor eventualmente — sem prazo definido nem garantia sobre a ordem observada nesse meio-tempo.

Consistência forte não é “melhor” em termos absolutos; é mais cara. Consistência eventual não é “pior”; é mais barata e mais disponível. A escolha depende do que o dado representa.

### Garantias centradas no cliente

Entre a consistência forte e a eventual pura existem garantias mais baratas que resolvem boa parte dos problemas percebidos pelo usuário:

- **Leitura das próprias escritas (*read-your-writes*):** um cliente sempre vê as alterações que ele mesmo realizou, mesmo que outras réplicas ainda estejam atrasadas.
- **Leituras monotônicas:** uma vez que um cliente observou um valor, ele nunca observará, em leituras seguintes, um valor mais antigo.
- **Escritas monotônicas:** as escritas de um mesmo cliente são aplicadas na ordem em que foram emitidas.
- **Leitura de prefixo consistente:** se uma escrita B depende causalmente de uma escrita A, nenhum cliente observa B sem antes observar A.

Essas garantias evitam boa parte dos comportamentos estranhos que um usuário perceberia como “bug”, sem exigir o custo de uma consistência forte global.

> **Recurso visual 2 — Espectro de consistência:** régua horizontal com “consistência eventual” à esquerda e “consistência forte” à direita, marcando pontos intermediários para causal, sequencial e garantias centradas no cliente, com indicação de custo de latência crescente da esquerda para a direita.  
> **Texto alternativo:** régua ilustra o espectro de modelos de consistência, do mais barato e disponível ao mais caro e rigoroso, com o custo de latência crescendo da esquerda para a direita.

### Quóruns de leitura e escrita

Quando um dado é replicado em $N$ nós, um mecanismo comum para equilibrar consistência e disponibilidade é o uso de quóruns: uma escrita é considerada concluída quando confirmada por $W$ réplicas, e uma leitura consulta $R$ réplicas, combinando as respostas.

A garantia de que toda leitura enxergará a escrita mais recente depende da sobreposição entre os conjuntos de réplicas lidas e escritas, expressa por:

$$
W + R > N
$$

Para $N = 5$, uma configuração de $W = 3$ e $R = 3$ satisfaz $3 + 3 = 6 > 5$: qualquer conjunto de três réplicas escolhido para leitura compartilha ao menos uma réplica com qualquer conjunto de três réplicas usado na escrita anterior, garantindo que a leitura enxergue o valor mais recente confirmado.

Outras combinações mudam o compromisso:

- $W = 1$, $R = N$: escrita rápida, leitura cara e mais lenta, pois depende de todas as réplicas.
- $W = N$, $R = 1$: leitura rápida, escrita cara, pois depende da confirmação de todos os nós.
- $W + R \leq N$: nenhuma garantia de sobreposição; o sistema prioriza disponibilidade e aceita leituras potencialmente obsoletas.

O número mínimo de réplicas necessário para tolerar $f$ falhas simultâneas, mantendo quórum de maioria, é dado por $N \geq 2f + 1$. Esse mesmo princípio de maioria será retomado na Aula 7, ao tratarmos de consenso.

### Aplicando o modelo à NexaOrder

Três dados da NexaOrder ilustram como escolhas diferentes convivem no mesmo sistema:

- **Catálogo de produtos:** tolera consistência eventual. Um preço ou descrição levemente desatualizado por alguns segundos não compromete o negócio, e a prioridade é disponibilidade e baixa latência de leitura.
- **Estoque:** exige, no mínimo, garantias centradas no cliente e, em pontos críticos de reserva, quórum com sobreposição — a alternativa de vender a mesma unidade duas vezes é mais cara do que a latência adicional de uma escrita com $W \geq 2$.
- **Pagamento:** exige a maior rigidez, aproximando-se de consistência forte no registro da transação, ainda que o restante do fluxo — como notificações — possa permanecer eventual.

Esse raciocínio de decompor o sistema por dado, e não por serviço inteiro, é uma das habilidades centrais desta unidade.

> **Recurso visual 3 — Quórum de leitura e escrita:** diagrama com cinco nós circulares; três deles destacados como conjunto de escrita ($W=3$) e três destacados, com sobreposição parcial, como conjunto de leitura ($R=3$), evidenciando o nó em comum.  
> **Texto alternativo:** diagrama de cinco réplicas mostra um conjunto de três nós usado na escrita e outro conjunto de três nós usado na leitura, com um nó em comum garantindo a visibilidade do valor mais recente.

### Atividade prática

Para cada um dos três dados a seguir da NexaOrder — catálogo, estoque e pagamento —, defina:

1. o modelo de consistência mais adequado (forte, causal, centrada no cliente ou eventual), com justificativa de negócio;
2. o modelo de replicação (líder único ou multi-líder);
3. se a replicação será síncrona, assíncrona ou por quórum, indicando valores plausíveis de $N$, $W$ e $R$;
4. um cenário de leitura obsoleta que seria aceitável e um que não seria, para esse dado.

Entregue o resultado em uma tabela de três linhas, uma por dado, permitindo comparação direta entre as escolhas.

### Síntese da aula

- Replicação melhora disponibilidade, latência de leitura e durabilidade, mas introduz o problema de manter cópias coerentes.
- Replicação líder-seguidor evita conflitos de escrita; replicação multi-líder reduz latência regional, mas exige resolução de conflitos.
- Replicação síncrona aumenta durabilidade às custas de latência; a assíncrona faz o inverso.
- O atraso de réplica explica leituras obsoletas sem que nenhuma réplica esteja “errada”.
- Consistência forte, sequencial, causal e eventual formam um espectro de custo e garantia, não uma escala de qualidade absoluta.
- Garantias centradas no cliente resolvem boa parte da percepção de inconsistência a um custo menor que a consistência forte global.
- Quóruns de leitura e escrita, com $W + R > N$, equilibram consistência e disponibilidade de forma configurável.

### Roteiro da Videoaula 5 — “Três cópias, três respostas: qual está certa?”

O roteiro falado e as indicações de edição estão desenvolvidos no arquivo `roteiros_20min.md`, retomando o caso do catálogo e do estoque da NexaOrder como demonstração central.

### Referências da aula

- COULOURIS, George et al. *Distributed Systems: Concepts and Design*. 5. ed. Boston: Addison-Wesley, 2011.
- KLEPPMANN, Martin. *Designing Data-Intensive Applications*. Sebastopol: O'Reilly Media, 2017.
- TANENBAUM, Andrew S.; VAN STEEN, Maarten. *Distributed Systems*. 4. ed. [S. l.]: distributed-systems.net, 2023.

## Aula 6 — Particionamento, CAP e escalabilidade de dados

### Situação-problema: quando uma cópia inteira já não cabe em um nó

Resolvido o problema de manter réplicas coerentes, a NexaOrder enfrentou um segundo limite: o catálogo cresceu para milhões de produtos, e o histórico de pedidos passou a acumular bilhões de registros. Replicar essa base inteira em cada nó tornou-se inviável em custo de armazenamento e em tempo de sincronização. A equipe precisava dividir os dados, não apenas copiá-los.

Ao testar uma primeira divisão simples — produtos de "A" a "M" em um nó e de "N" a "Z" em outro —, a equipe descobriu que uma campanha publicitária concentrada em produtos cujo nome começava com "S" sobrecarregou um único nó, enquanto o outro permanecia ocioso. Dividir os dados exige uma estratégia, não apenas um corte arbitrário.

### Particionamento horizontal

Particionamento horizontal, ou *sharding*, consiste em dividir um conjunto de dados em partições menores, cada uma armazenada e servida por um subconjunto de nós. Diferentemente da replicação, que mantém cópias completas do mesmo dado, o particionamento distribui fatias diferentes de um mesmo conjunto de dados. Na prática, sistemas de produção combinam as duas técnicas: cada partição, por sua vez, é replicada para garantir disponibilidade.

O objetivo do particionamento é permitir que o volume de dados e o volume de operações cresçam distribuindo trabalho entre nós, em vez de exigir que um único nó armazene e processe tudo.

### Estratégia por faixa

O particionamento por faixa (*range partitioning*) atribui intervalos contíguos de uma chave a cada partição — por exemplo, pedidos de janeiro em uma partição e de fevereiro em outra, ou produtos "A–M" e "N–Z", como na tentativa inicial da NexaOrder.

A vantagem é que consultas por intervalo — “todos os pedidos de fevereiro” — são eficientes, pois atingem partições contíguas. A desvantagem, evidenciada no incidente da campanha, é a formação de *pontos quentes* (*hot spots*): se a distribuição real das chaves não é uniforme, algumas partições recebem carga desproporcional.

### Estratégia por hash

O particionamento por hash aplica uma função de espalhamento à chave e usa o resultado para determinar a partição, distribuindo as chaves de forma aproximadamente uniforme, independentemente de seu valor original. Isso resolve o problema de pontos quentes causados por concentração alfabética ou temporal, mas sacrifica a eficiência de consultas por intervalo, já que chaves originalmente próximas passam a ficar espalhadas entre partições distintas.

### Estratégia por diretório

Uma terceira alternativa mantém um serviço de diretório — uma tabela de mapeamento explícita entre cada chave, ou faixa de chaves, e a partição responsável. Essa abordagem oferece flexibilidade máxima para rebalancear dados manualmente ou por regras de negócio, mas introduz um componente adicional que precisa ser consultado, replicado e mantido disponível, sob pena de se tornar, ele mesmo, um ponto único de falha.

> **Recurso visual 4 — Três estratégias de particionamento:** três diagramas lado a lado mostrando o mesmo conjunto de chaves distribuído por faixa, por hash e por diretório, com cores indicando a partição de destino de cada chave.  
> **Texto alternativo:** comparação visual entre particionamento por faixa, por hash e por diretório, evidenciando como o mesmo conjunto de chaves é distribuído de formas diferentes em cada estratégia.

### Hashing consistente

Uma limitação do particionamento por hash simples — calcular `hash(chave) mod N` — é que alterar o número de nós $N$ redistribui quase todas as chaves, exigindo movimentação massiva de dados a cada adição ou remoção de nó.

O *hashing consistente* resolve esse problema organizando o espaço de hash como um anel. Cada nó ocupa uma ou mais posições nesse anel — na prática, cada nó físico costuma receber múltiplos *nós virtuais*, para distribuir a carga de forma mais equilibrada. Uma chave é atribuída ao primeiro nó encontrado ao percorrer o anel em sentido horário a partir da posição do seu hash.

Quando um nó é adicionado ou removido, apenas as chaves posicionadas entre ele e o nó vizinho anterior no anel são redistribuídas — as demais permanecem no lugar. Para um anel com $N$ nós, a fração aproximada de chaves redistribuída ao adicionar um novo nó é:

$$
\text{fração redistribuída} \approx \frac{1}{N + 1}
$$

Para $N = 9$ nós existentes, adicionar um décimo nó redistribui aproximadamente $\frac{1}{10} = 10\%$ das chaves — uma fração muito menor do que a redistribuição quase total provocada pelo hash simples com módulo.

O uso de nós virtuais reforça esse benefício. Se cada nó físico ocupasse uma única posição no anel, a distribuição de carga dependeria do acaso de onde cada nó caiu no espaço de hash, podendo gerar segmentos bem maiores que outros. Atribuindo, por exemplo, 100 ou 200 posições virtuais a cada nó físico, espalhadas pelo anel, a soma dos segmentos de cada nó tende a se aproximar da média esperada, reduzindo a variância de carga entre nós sem exigir nenhuma mudança na lógica de atribuição de chaves.

### Rebalanceamento e pontos quentes

Mesmo com hashing consistente, um ponto quente pode surgir quando uma única chave concentra volume desproporcional de tráfego — por exemplo, um produto em promoção relâmpago concentrando a maior parte das leituras de estoque da NexaOrder em uma única partição. Hashing distribui bem chaves diferentes, mas não divide a carga de uma única chave muito popular.

Estratégias de mitigação incluem particionar artificialmente a chave quente (por exemplo, sufixando-a com um número aleatório e agregando os resultados na leitura), aplicar cache na frente da partição afetada, ou isolar deliberadamente esse produto em uma partição dedicada durante o pico de demanda.

Rebalancear não é apenas mover dados: é também mover carga de processamento. Enquanto uma migração de partição está em andamento, a partição de origem e a partição de destino processam, simultaneamente, requisições normais e a transferência dos dados migrados — o que pode degradar temporariamente a latência de ambas. Por isso, sistemas maduros de particionamento costumam limitar a taxa de migração (*throttling*) e programar rebalanceamentos para janelas de menor tráfego, sempre que o negócio permitir esse tipo de planejamento.

### Particionamento e replicação combinados

Particionamento e replicação resolvem problemas diferentes, mas raramente aparecem isolados em produção. Uma arquitetura típica particiona os dados em $P$ partições e replica cada partição em $R$ nós, de modo que o cluster total possua $P \times R$ réplicas distribuídas. Cada partição, isoladamente, aplica os conceitos de replicação estudados na Aula 5 — líder-seguidor ou multi-líder, quóruns de leitura e escrita — enquanto o conjunto de partições aplica os conceitos de particionamento desta aula.

Isso significa que a falha de um único nó físico normalmente afeta apenas uma fração pequena dos dados — as partições cujas réplicas ele hospedava —, e não o sistema inteiro. Para a NexaOrder, isso implica que a perda de um nó do cluster de estoque compromete a disponibilidade de escrita apenas dos produtos cujas chaves de partição foram mapeadas para aquele nó, desde que as demais réplicas dessas partições continuem operando normalmente.

### Consultas entre partições

Uma consulta que precisa combinar dados de várias partições — por exemplo, “todos os pedidos com valor acima de determinado limite, em todas as regiões” — exige um padrão de dispersão e coleta (*scatter-gather*): a consulta é enviada a todas as partições relevantes, e os resultados parciais são agregados. Esse padrão tem custo maior que uma consulta dentro de uma única partição e é sensível à cauda de latência: o tempo total de resposta é determinado pela partição mais lenta a responder.

Por isso, a escolha da chave de partição deve favorecer os padrões de consulta mais frequentes do sistema, mesmo sabendo que nenhuma escolha atenderá igualmente bem a todos os tipos de consulta.

Um exemplo numérico simples ilustra o custo do *scatter-gather*. Suponha que uma consulta entre partições atinja oito partições, cada uma respondendo, em média, em 20 milissegundos, mas com uma cauda de latência em que 5% das respostas individuais levam 200 milissegundos. Se o tempo total da consulta é determinado pela partição mais lenta a responder, a probabilidade de que pelo menos uma das oito partições caia nessa cauda cresce rapidamente:

$$
P(\text{pelo menos uma partição lenta}) = 1 - (1 - 0{,}05)^{8} \approx 1 - 0{,}66 = 0{,}34
$$

Ou seja, mais de um terço das consultas que tocam oito partições simultaneamente tende a sofrer o efeito da cauda de latência de pelo menos uma delas — mesmo que cada partição individual seja lenta apenas 5% das vezes. Esse é um argumento numérico direto a favor de projetar chaves de partição que minimizem consultas dispersas em muitas partições ao mesmo tempo.

### O teorema CAP

O teorema CAP descreve um compromisso central em sistemas distribuídos que replicam dados: durante uma partição de rede — quando nós deixam de conseguir se comunicar entre si —, um sistema não pode oferecer simultaneamente:

- **Consistência (C):** toda leitura reflete a escrita mais recente confirmada;
- **Disponibilidade (A):** toda requisição a um nó ativo recebe uma resposta, mesmo sem garantia de que seja a mais recente;
- **Tolerância a partição (P):** o sistema continua operando apesar da perda de comunicação entre alguns de seus nós.

Como partições de rede são inevitáveis em sistemas distribuídos reais, a tolerância a partição não é opcional na prática — a escolha relevante ocorre entre consistência e disponibilidade durante o período em que a partição persiste. Um sistema **CP** rejeita ou atrasa respostas no lado da partição que não pode garantir a versão mais recente, preservando consistência. Um sistema **AP** continua respondendo em ambos os lados, aceitando o risco de retornar valores divergentes, que precisarão ser reconciliados quando a comunicação for restabelecida.

É importante notar que o CAP descreve o comportamento **durante** uma partição; fora desse cenário, um sistema pode oferecer alta consistência e alta disponibilidade simultaneamente, o que motiva a extensão discutida a seguir.

> **Recurso visual 5 — CAP durante uma partição de rede:** diagrama com dois grupos de nós separados por uma marca de rede rompida; um ramo do diagrama mostra o grupo continuando a responder (AP) e o outro mostra o grupo recusando respostas até a reconciliação (CP).  
> **Texto alternativo:** diagrama ilustra dois nós separados por uma falha de rede; em um cenário o sistema prioriza disponibilidade e responde com possível divergência, no outro prioriza consistência e recusa respostas até restabelecer a comunicação.

### PACELC como extensão de análise

O teorema CAP descreve apenas o comportamento sob partição. O **PACELC** estende essa análise: **se há partição (P), o sistema escolhe entre disponibilidade (A) e consistência (C); caso contrário (E, *else*), o sistema escolhe entre latência (L) e consistência (C)**.

Essa extensão é relevante porque partições de rede são eventos relativamente raros, enquanto o compromisso entre latência e consistência ocorre a cada operação, mesmo em condições normais. Um sistema que exige confirmação de todas as réplicas antes de responder a uma escrita paga um custo de latência constante, não apenas durante falhas. O PACELC ajuda a comunicar que a escolha de consistência tem impacto no dia a dia do sistema, não apenas em cenários excepcionais.

### Aplicando à NexaOrder

Para o catálogo de produtos, a NexaOrder tende a favorecer AP/EL: disponibilidade e baixa latência quase sempre, com convergência eventual. Para a confirmação de pagamento, tende a favorecer CP/EC: preferir recusar ou atrasar uma resposta a confirmar uma cobrança com base em informação potencialmente desatualizada. Para o estoque, a resposta é mista: a leitura do saldo pode tolerar AP em situações de baixo risco, mas a reserva efetiva de uma unidade, no momento da compra, deve se aproximar de CP, evitar vender o mesmo item duas vezes.

Essa análise combina diretamente com a escolha de chave de partição discutida ao longo da aula: não basta decidir *como* particionar um dado; é preciso decidir também *o que* o sistema deve fazer com aquela partição específica quando uma parte do cluster ficar inacessível. Uma decisão registrada apenas como "usamos hash consistente" está incompleta sem a decisão complementar de "e, sob partição de rede, esse dado prioriza consistência ou disponibilidade".

> **Recurso visual 6 — Matriz de decisão CAP por dado da NexaOrder:** tabela com uma linha para catálogo, uma para estoque e uma para pagamento, e colunas indicando a escolha CP ou AP, a justificativa de negócio e o comportamento esperado durante uma partição de rede.  
> **Texto alternativo:** tabela relaciona cada dado da NexaOrder — catálogo, estoque e pagamento — à escolha entre CP e AP, com a justificativa de negócio correspondente a cada linha.

### Atividade prática

Escolha as chaves de partição para dois dados da NexaOrder: pedidos e estoque.

1. Defina a chave de partição de cada dado e a estratégia (faixa, hash ou diretório), justificando a escolha pelos padrões de consulta mais comuns.
2. Simule um cenário de crescimento desigual: um produto específico se torna um ponto quente durante uma campanha. Descreva o efeito esperado sobre a partição correspondente.
3. Proponha uma mitigação concreta para esse ponto quente.
4. Classifique cada dado, sob partição de rede, como CP ou AP, e diga se a escolha se sustenta também fora de uma partição, na lógica do PACELC.

### Síntese da aula

- Particionamento horizontal distribui fatias de um conjunto de dados entre nós, complementando — e não substituindo — a replicação.
- Particionamento por faixa favorece consultas por intervalo, mas é vulnerável a pontos quentes.
- Particionamento por hash distribui chaves de forma uniforme, ao custo de consultas por intervalo eficientes.
- Hashing consistente reduz drasticamente o volume de dados redistribuído quando nós são adicionados ou removidos.
- Pontos quentes podem surgir mesmo com boa estratégia de particionamento, quando uma única chave concentra tráfego desproporcional.
- O teorema CAP descreve a escolha entre consistência e disponibilidade durante uma partição de rede.
- O PACELC amplia essa análise para o compromisso cotidiano entre latência e consistência, mesmo sem partição.

### Roteiro da Videoaula 6 — “Dividir para crescer: como fatiar dados sem quebrar o sistema”

O roteiro falado e as indicações de edição estão desenvolvidos no arquivo `roteiros_20min.md`, retomando o incidente do ponto quente no catálogo da NexaOrder como demonstração central.

### Referências da aula

- KLEPPMANN, Martin. *Designing Data-Intensive Applications*. Sebastopol: O'Reilly Media, 2017.
- COULOURIS, George et al. *Distributed Systems: Concepts and Design*. 5. ed. Boston: Addison-Wesley, 2011.
- TANENBAUM, Andrew S.; VAN STEEN, Maarten. *Distributed Systems*. 4. ed. [S. l.]: distributed-systems.net, 2023.

## Aula 7 — Consenso, eleição de líder e Raft

### Situação-problema: quem manda quando o líder some

Na Aula 5, a NexaOrder adotou replicação líder-seguidor para o estoque. Certa noite, o nó líder da região sul ficou inacessível por falha de rede. A equipe de plantão precisou promover manualmente um seguidor a líder, mas dois operadores, sem se comunicar, promoveram dois nós diferentes quase ao mesmo tempo. Por alguns minutos, o sistema teve dois líderes aceitando escritas — uma condição conhecida como *split-brain* — e parte das reservas de estoque feitas nesse intervalo divergiu entre os dois.

O incidente expôs um problema mais profundo do que a simples indisponibilidade do líder: como um conjunto de nós concorda, de forma automática e seguramente, sobre qual deles é o líder legítimo, mesmo quando alguns nós falham ou a comunicação entre eles é interrompida? Este é o problema do consenso, e esta aula estuda uma de suas soluções mais adotadas na prática: o algoritmo Raft.

### O problema do consenso

Consenso é o problema de fazer com que um conjunto de nós concorde sobre um único valor, mesmo na presença de falhas, de modo que essa decisão seja: **válida** (o valor decidido foi de fato proposto por algum nó), **uniforme** (todos os nós corretos decidem o mesmo valor) e **irrevogável** (uma vez decidido, o valor não muda).

Esse problema aparece sempre que um sistema distribuído precisa de uma única fonte de verdade sobre algo — qual nó é o líder, qual foi a próxima operação aplicada a um log, ou qual transação foi confirmada. Resolver consenso manualmente, como fez a equipe de plantão da NexaOrder, é sujeito a exatamente o tipo de erro que causou o *split-brain*: decisões concorrentes tomadas sem coordenação.

### Maioria e quórum

Algoritmos de consenso amplamente utilizados, como o Raft, se apoiam no princípio de maioria: uma decisão só é considerada válida quando aceita por mais da metade dos nós do cluster. Esse mesmo princípio de quórum foi apresentado na Aula 5 para replicação de dados; aqui, ele é aplicado à decisão sobre qual nó é o líder e sobre quais entradas de log foram confirmadas.

Para um cluster de $N$ nós, o número de falhas simultâneas que ele tolera, mantendo capacidade de formar maioria, é:

$$
f = \left\lfloor \frac{N - 1}{2} \right\rfloor
$$

Para $N = 5$, $f = \lfloor 4/2 \rfloor = 2$: o cluster tolera a falha de até dois nós e ainda forma maioria com os três restantes. Esse é o motivo pelo qual clusters de consenso costumam ter número ímpar de nós — cinco é um tamanho comum, equilibrando tolerância a falhas e custo de coordenação.

Vale comparar tamanhos alternativos de cluster para entender esse equilíbrio. Um cluster de três nós tolera apenas uma falha ($f = \lfloor 2/2 \rfloor = 1$) com um custo de coordenação menor. Um cluster de sete nós tolera três falhas ($f = \lfloor 6/2 \rfloor = 3$), mas exige que cada operação seja confirmada por quatro nós antes de ser considerada segura, aumentando a latência típica de escrita. Note também que adicionar um nó par — passar de cinco para seis, por exemplo — não aumenta a tolerância a falhas: $f = \lfloor 5/2 \rfloor$ continua igual a 2, apenas com um nó a mais para coordenar. É por isso que números pares raramente fazem sentido em clusters de consenso.

> **Recurso visual 7 — Tamanho do cluster versus tolerância a falhas:** tabela com três linhas (clusters de 3, 5 e 7 nós), mostrando o valor de $f$, o número de nós exigido para maioria e um comentário sobre o custo de coordenação de cada configuração.  
> **Texto alternativo:** tabela compara clusters de três, cinco e sete nós, relacionando cada tamanho ao número de falhas toleradas e ao número de nós necessário para formar maioria.

### Máquina de estados replicada

A abstração central usada pelo Raft é a *máquina de estados replicada*: cada nó mantém uma cópia idêntica de uma máquina de estados, e todos os nós aplicam exatamente a mesma sequência de operações, na mesma ordem. Se todos os nós partem do mesmo estado inicial e aplicam a mesma sequência de operações determinísticas, todos chegam ao mesmo estado final.

O problema de manter réplicas consistentes se transforma, então, em um problema mais restrito: garantir que todos os nós concordem sobre a mesma sequência ordenada de operações — um log replicado.

### Eleição de líder

O Raft opera com um único líder por vez, responsável por receber novas operações e replicá-las para os demais nós (seguidores). Se o líder para de responder, os seguidores — cada um com um temporizador de eleição aleatório, para reduzir a chance de disputas simultâneas — tornam-se candidatos e solicitam votos aos demais nós. Um candidato que recebe votos da maioria do cluster se torna o novo líder.

O uso de temporizadores aleatórios, e não fixos, é deliberado: se todos os seguidores disparassem uma eleição exatamente no mesmo instante, poderiam empatar repetidamente, atrasando a formação de um novo líder.

> **Recurso visual 8 — Linha do tempo de uma eleição:** diagrama mostrando o líder deixando de enviar sinais de vida, os temporizadores de três seguidores expirando em instantes ligeiramente diferentes, o primeiro seguidor a expirar se tornando candidato e recebendo votos até atingir maioria.  
> **Texto alternativo:** linha do tempo mostra o silêncio do líder anterior, os temporizadores aleatórios de cada seguidor expirando em momentos distintos e o candidato vencedor recebendo votos suficientes para se tornar o novo líder.

### Termos, log replicado e confirmação

O tempo, no Raft, é dividido em *termos* (*terms*), numerados sequencialmente. Cada termo tem, no máximo, um líder. Toda mensagem trocada entre os nós carrega o número do termo, permitindo que um nó identifique e rejeite informações de um termo já superado — por exemplo, ordens vindas de um líder antigo que ainda não percebeu ter sido substituído.

Quando o líder recebe uma nova operação, ele a adiciona ao seu log e a replica aos seguidores por meio de mensagens de *append entries*. Uma entrada é considerada **confirmada** (*committed*) quando replicada pela maioria dos nós — o mesmo princípio de quórum de escrita. Somente depois de confirmada, a entrada é aplicada à máquina de estados e o resultado é retornado ao cliente. Esse mecanismo garante que uma entrada confirmada sobreviva à eventual falha do líder, pois estará presente em pelo menos um nó de qualquer maioria futura.

> **Recurso visual 9 — Ciclo de replicação do Raft:** diagrama sequencial mostrando o líder recebendo uma operação, enviando *append entries* a dois seguidores, recebendo confirmação da maioria e aplicando a entrada à máquina de estados.  
> **Texto alternativo:** diagrama de sequência mostra o líder recebendo uma operação do cliente, replicando-a a dois seguidores, aguardando confirmação da maioria e só então aplicando a operação e respondendo ao cliente.

### Segurança e disponibilidade no Raft

O Raft é projetado para satisfazer duas propriedades:

- **Segurança (*safety*):** em qualquer termo, existe no máximo um líder; uma entrada confirmada nunca é perdida ou substituída por outra em uma posição já confirmada do log. Essas garantias são o que teria evitado o *split-brain* do incidente da NexaOrder, caso o cluster de estoque estivesse sob consenso automatizado em vez de promoção manual.
- **Disponibilidade (*liveness*):** enquanto uma maioria dos nós estiver ativa e capaz de se comunicar, o cluster eventualmente elege um líder e continua processando operações.

Note a assimetria: a segurança do Raft vale mesmo durante uma partição de rede ou atraso arbitrário de mensagens; a disponibilidade depende de haver, em algum momento, comunicação suficiente entre a maioria dos nós. Se um cluster de cinco nós se divide em um grupo de dois e outro de três por uma partição de rede, apenas o grupo com três nós — a maioria — pode eleger um líder e continuar aceitando escritas; o grupo de dois permanece sem líder até a partição ser resolvida. Esse comportamento é uma aplicação direta do teorema CAP estudado na Aula 6: o Raft escolhe consistência (CP) em detrimento da disponibilidade do lado minoritário.

### Limites e custos do consenso

Consenso não é gratuito. Cada operação confirmada exige, no mínimo, uma rodada de comunicação entre o líder e a maioria dos seguidores, o que adiciona latência proporcional ao tempo de ida e volta (*round-trip time*) até os nós mais distantes envolvidos no quórum. O throughput do sistema é limitado pela capacidade de um único líder processar e replicar operações — algoritmos de consenso não paralelizam escritas entre múltiplos líderes, ao contrário da replicação multi-líder discutida na Aula 5.

Um exemplo numérico ajuda a dimensionar esse custo. Se o cluster de consenso da NexaOrder está distribuído em três zonas de disponibilidade com tempo de ida e volta médio de 4 milissegundos entre o líder e cada seguidor, e a confirmação de uma escrita exige resposta de pelo menos dois seguidores (para formar maioria de três em um cluster de cinco), a latência mínima esperada para confirmar uma operação é de aproximadamente 4 milissegundos — o tempo de uma única rodada de ida e volta até os seguidores mais lentos necessários para completar o quórum. Se o cluster estivesse espalhado entre continentes diferentes, com tempo de ida e volta de 120 milissegundos, essa mesma operação levaria, no mínimo, 120 milissegundos só pela rodada de confirmação — antes de qualquer processamento. Esse é o motivo pelo qual clusters de consenso costumam ser posicionados com nós relativamente próximos entre si, ainda que o sistema como um todo sirva usuários espalhados globalmente por outras camadas de replicação e cache.

Além disso, o Raft, como a maioria dos algoritmos de consenso amplamente utilizados, pressupõe falhas de parada ou de rede — nós que param ou ficam inacessíveis —, mas não falhas bizantinas, em que um nó pode enviar informações deliberadamente incorretas. Sistemas que precisam tolerar participantes maliciosos exigem algoritmos de consenso bizantino, fora do escopo desta disciplina, mas relevantes, por exemplo, em redes de blockchain público.

### Pausa para reflexão

Um cluster de cinco nós de consenso está distribuído em três zonas de disponibilidade: duas máquinas na zona A, duas na zona B e uma na zona C. Uma falha de rede isola completamente a zona C do restante e, simultaneamente, degrada parcialmente a comunicação entre as zonas A e B, mas sem isolá-las totalmente.

Reflita:

1. Considerando apenas o critério de maioria, quais combinações de nós ainda conseguiriam eleger um líder nesse cenário?
2. Que diferença faz, para a disponibilidade do cluster, distribuir os cinco nós em três zonas em vez de concentrá-los em apenas duas?
3. Se a empresa decidisse reduzir custo e operar esse cluster com apenas três nós, qual seria o novo limite de tolerância a falhas, e o que isso significaria em uma manutenção programada que retira um nó de operação?
4. Que evidência operacional (métrica, log ou alerta) permitiria à equipe perceber, em produção, que o cluster está operando sem maioria disponível?

Não existe uma única resposta correta; o objetivo é praticar o raciocínio sobre maioria, topologia física e disponibilidade, retomando o conceito de zonas independentes de falha apresentado na Unidade 1.

### Atividade prática

Simule, em papel ou em uma ferramenta de sua escolha, um cluster Raft de cinco nós:

1. Desenhe o cluster e identifique o líder inicial no termo 1.
2. Simule a falha do líder: descreva a sequência de eventos até a eleição de um novo líder, indicando o novo número de termo.
3. Simule o envio de três novas operações pelo novo líder e a réplica dessas operações para os seguidores, indicando em que ponto cada uma é considerada confirmada.
4. Simule a recuperação do nó que havia falhado: descreva como seu log deve ser reconciliado com o log do cluster atual.

Entregue um diagrama e uma descrição textual curta de cada etapa.

### Síntese da aula

- Consenso é o problema de um conjunto de nós concordarem sobre um único valor, de forma válida, uniforme e irrevogável, mesmo com falhas.
- Algoritmos de consenso se apoiam no princípio de maioria; um cluster de $N$ nós tolera $\lfloor (N-1)/2 \rfloor$ falhas.
- A máquina de estados replicada transforma o problema de consistência em um problema de ordenação de um log replicado.
- O Raft elege um único líder por termo, usando temporizadores aleatórios para reduzir disputas simultâneas.
- Uma entrada de log é confirmada quando replicada pela maioria dos nós, garantindo que sobreviva a falhas futuras do líder.
- A segurança do Raft impede múltiplos líderes no mesmo termo e perda de entradas confirmadas; a disponibilidade depende de uma maioria ativa e comunicável.
- Consenso tem custo de latência e limite de throughput, e não protege, por padrão, contra falhas bizantinas.

### Roteiro da Videoaula 7 — “Cinco nós, um líder: como o Raft evita o split-brain”

O roteiro falado e as indicações de edição estão desenvolvidos no arquivo `roteiros_20min.md`, retomando o incidente de promoção manual conflitante do estoque da NexaOrder como demonstração central.

### Referências da aula

- ONGARO, Diego; OUSTERHOUT, John. In search of an understandable consensus algorithm. In: USENIX ANNUAL TECHNICAL CONFERENCE, 2014, Philadelphia. *Proceedings [...]*. Berkeley: USENIX Association, 2014.
- COULOURIS, George et al. *Distributed Systems: Concepts and Design*. 5. ed. Boston: Addison-Wesley, 2011.
- TANENBAUM, Andrew S.; VAN STEEN, Maarten. *Distributed Systems*. 4. ed. [S. l.]: distributed-systems.net, 2023.

## Aula 8 — Transações distribuídas, sagas e idempotência

### Situação-problema: uma compra, quatro serviços, nenhuma transação única

Com replicação, particionamento e consenso resolvidos para cada serviço individualmente, restou o problema que atravessa todos eles: uma compra na NexaOrder envolve os serviços de pedidos, estoque, pagamento e expedição, cada um com seu próprio banco de dados. Não existe mais uma única transação de banco de dados capaz de garantir que os quatro passos aconteçam todos ou nenhum. Em um teste de carga, a equipe observou um caso preocupante: o pagamento foi autorizado, mas uma falha de rede impediu a confirmação de chegar ao serviço de pedidos a tempo; o cliente, ao ver a interface travada, tentou novamente, e dois pagamentos foram processados para a mesma compra.

Esta aula final da unidade trata exatamente desse problema: como manter operações coerentes quando elas atravessam múltiplos serviços e múltiplos bancos de dados independentes, sem um coordenador global bloqueante, e como evitar que falhas de rede se transformem em duplicações.

### Atomicidade local e distribuída

Dentro de um único banco de dados, a atomicidade é responsabilidade do próprio sistema: uma transação local aplica todas as suas operações ou nenhuma, mesmo em caso de falha. Quando uma operação de negócio abrange vários bancos de dados independentes — como a compra da NexaOrder, que toca pedidos, estoque, pagamento e expedição —, não existe mais uma transação única capaz de garantir essa propriedade automaticamente. É preciso um mecanismo explícito de coordenação entre os serviços.

### Confirmação em duas fases (2PC)

A confirmação em duas fases (*two-phase commit*, ou 2PC) é um protocolo clássico para coordenar transações distribuídas. Um coordenador conduz o processo em duas etapas:

1. **Fase de preparação:** o coordenador pergunta a cada participante se está pronto para confirmar sua parte da transação. Cada participante executa sua operação de forma provisória, bloqueia os recursos envolvidos e responde “pronto” ou “abortar”.
2. **Fase de confirmação:** se todos os participantes responderam “pronto”, o coordenador envia a ordem de confirmação definitiva a todos; se qualquer participante respondeu “abortar”, ou não respondeu a tempo, o coordenador envia a ordem de desfazer a operação a todos.

O 2PC garante atomicidade distribuída, mas ao custo de manter recursos bloqueados durante toda a espera pela decisão do coordenador. Se o coordenador falhar depois da fase de preparação e antes de comunicar a decisão final, os participantes ficam bloqueados, incapazes de decidir sozinhos se devem confirmar ou desfazer — um problema conhecido como bloqueio do 2PC. Recuperar esse estado exige registrar a decisão de forma durável antes da falha e, em geral, intervenção de um processo de recuperação que consulte o registro do coordenador assim que ele voltar a operar.

### Bloqueios, coordenador e recuperação

O custo do 2PC cresce com o número de participantes e com a duração da transação: quanto mais serviços envolvidos, maior a chance de que ao menos um esteja lento ou indisponível, e quanto mais tempo os recursos permanecem bloqueados, maior o impacto sobre outras operações concorrentes que dependam dos mesmos dados. Por essa razão, o 2PC é pouco utilizado para coordenar operações de negócio de longa duração — como uma compra que pode levar minutos entre reserva de estoque e confirmação de pagamento — sendo mais comum em transações curtas dentro de um mesmo domínio de infraestrutura.

Um exemplo simples ilustra o efeito multiplicativo desse risco. Se cada um dos quatro serviços da NexaOrder tem, isoladamente, uma probabilidade de 1% de estar lento ou indisponível em um dado instante, a probabilidade de que **pelo menos um** dos quatro participantes cause atraso ou bloqueio em uma transação 2PC que os envolva simultaneamente é:

$$
P(\text{pelo menos um lento}) = 1 - (1 - 0{,}01)^{4} \approx 1 - 0{,}961 = 3{,}9\%
$$

Quatro vezes maior do que o risco de um único serviço isolado. Quanto mais participantes um coordenador de 2PC precisa reunir, maior a chance de que a transação inteira fique refém do elo mais lento — um argumento adicional, além do risco de bloqueio na falha do coordenador, para evitar esse padrão em fluxos com muitos serviços independentes.

Para o cenário da NexaOrder, com quatro serviços independentes, mantidos por equipes diferentes e sujeitos a variações de latência e disponibilidade, um coordenador bloqueante representaria um novo ponto único de fragilidade. A alternativa amplamente adotada são as sagas.

### Sagas coreografadas e orquestradas

Uma *saga* substitui uma única transação distribuída por uma sequência de transações locais, cada uma confinada a um serviço, encadeadas por eventos ou comandos. Se uma etapa falha, a saga não tenta desfazer tudo instantaneamente como o 2PC; em vez disso, executa ações compensatórias que revertem, de forma lógica, o efeito das etapas já concluídas.

Existem duas formas de coordenar uma saga:

- **Coreografada:** cada serviço publica eventos de domínio ao concluir sua etapa, e os demais serviços reagem a esses eventos de forma independente, sem um coordenador central. É simples para poucos passos, mas o fluxo completo fica implícito, disperso entre os serviços, dificultando o rastreamento do estado de uma saga específica.
- **Orquestrada:** um orquestrador central conhece a sequência completa de passos e envia comandos explícitos a cada serviço, aguardando confirmação antes de avançar. O fluxo fica explícito e fácil de rastrear, mas o orquestrador concentra o conhecimento do processo de negócio, aproximando-se de um coordenador — ainda que, diferentemente do 2PC, ele não bloqueie recursos durante a espera.

> **Recurso visual 10 — Saga coreografada versus orquestrada:** dois diagramas; o primeiro mostra quatro serviços publicando e reagindo a eventos entre si, sem centro; o segundo mostra um orquestrador central enviando comandos numerados aos mesmos quatro serviços.  
> **Texto alternativo:** comparação entre uma saga coreografada, na qual pedidos, estoque, pagamento e expedição reagem a eventos uns dos outros, e uma saga orquestrada, na qual um orquestrador central envia comandos sequenciais a cada serviço.

### Ações compensatórias

Como não há uma transação global para desfazer, cada etapa de uma saga que altera estado precisa de uma ação compensatória correspondente, capaz de reverter seu efeito de forma consistente com o negócio. Para a compra da NexaOrder:

- reservar estoque → compensação: liberar a reserva;
- autorizar pagamento → compensação: estornar o valor autorizado;
- gerar etiqueta de expedição → compensação: cancelar a etiqueta antes do despacho.

Uma compensação nem sempre é o inverso perfeito da operação original — estornar um pagamento já processado pode envolver taxas, prazos ou políticas comerciais diferentes de simplesmente “não ter cobrado”. Por isso, projetar a compensação é uma decisão de negócio tanto quanto uma decisão técnica.

### Padrões outbox e inbox

Um risco recorrente ao publicar eventos de uma saga é o **problema da escrita dupla** (*dual write problem*): um serviço grava uma alteração em seu banco de dados e, em seguida, publica um evento correspondente; se o serviço falhar entre essas duas operações, o evento pode nunca ser publicado, mesmo que a alteração tenha sido persistida — ou o inverso, o evento pode ser publicado sem que a alteração tenha, de fato, sido confirmada.

O padrão ***outbox*** resolve esse problema gravando o evento a ser publicado na mesma transação local que grava a alteração de negócio, em uma tabela auxiliar dentro do mesmo banco de dados. Um processo separado lê essa tabela e publica os eventos de forma confiável, garantindo que evento e alteração de estado sejam consistentes entre si, sem depender de uma transação distribuída entre o banco de dados e o sistema de mensageria.

O padrão ***inbox*** complementa essa abordagem do lado do consumidor: antes de processar uma mensagem recebida, o serviço registra seu identificador em uma tabela de mensagens já tratadas; se a mesma mensagem chegar novamente — por *retry*, duplicação de rede ou reentrega do sistema de mensageria —, o serviço reconhece que ela já foi processada e a descarta sem repetir seus efeitos.

> **Recurso visual 11 — Padrão outbox de ponta a ponta:** diagrama mostrando um serviço gravando, em uma única transação local, a alteração de negócio e o evento correspondente em uma tabela outbox; ao lado, um processo separado lendo essa tabela e publicando os eventos no sistema de mensageria.  
> **Texto alternativo:** diagrama mostra a gravação simultânea da alteração de negócio e do evento na mesma transação local, seguida da publicação assíncrona e confiável do evento por um processo separado que lê a tabela outbox.

### Deduplicação e processamento efetivamente único

Sistemas de mensageria distribuída, em geral, oferecem entrega **pelo menos uma vez** (*at-least-once*): preferem reentregar uma mensagem em caso de dúvida a arriscar perdê-la, o que implica que duplicatas são esperadas, não excepcionais. Alcançar efeito **exatamente uma vez** (*exactly-once*) do ponto de vista do negócio não depende de a rede nunca duplicar mensagens — o que nenhum sistema garante de forma absoluta —, mas de tornar o processamento **idempotente**: aplicar a mesma operação duas ou mais vezes produz exatamente o mesmo resultado que aplicá-la uma única vez.

O padrão *inbox* é uma forma de idempotência; outra forma comum é associar a cada operação uma **chave de idempotência** — um identificador único gerado pelo cliente ou pela primeira tentativa da operação — e verificar, antes de processá-la, se aquela chave já foi registrada como concluída. No incidente de pagamento duplicado da situação-problema, uma chave de idempotência por tentativa de compra, verificada pelo serviço de pagamento antes de autorizar uma nova cobrança, teria permitido reconhecer a segunda tentativa como repetição da primeira, e não como uma nova compra.

> **Recurso visual 12 — Fluxo de idempotência no pagamento:** diagrama de decisão mostrando uma requisição de pagamento chegando com uma chave de idempotência; se a chave já existe na tabela de operações concluídas, o serviço retorna o resultado anterior; caso contrário, processa a cobrança e registra a chave.  
> **Texto alternativo:** fluxograma mostra o serviço de pagamento verificando se a chave de idempotência da requisição já foi processada antes de decidir entre retornar o resultado anterior ou processar uma nova cobrança.

### Modelando a saga da NexaOrder

Aplicando os conceitos da aula ao caso central da disciplina, uma saga orquestrada para a compra da NexaOrder poderia seguir a sequência: reservar estoque → autorizar pagamento → confirmar pedido → solicitar expedição. Se a autorização de pagamento falhar, a compensação libera a reserva de estoque. Se a solicitação de expedição falhar após o pagamento já autorizado, a compensação estorna o pagamento e libera a reserva. Cada etapa publica seu evento via padrão *outbox*, e cada serviço consumidor aplica o padrão *inbox* e chaves de idempotência para tratar reentregas sem duplicar efeitos.

### O que vem na próxima unidade

Esta unidade tratou de como os dados da NexaOrder são replicados, particionados, coordenados por consenso e mantidos coerentes através de sagas. A Unidade 3 parte desse alicerce para tratar da organização dos próprios serviços: como decompor a NexaOrder em limites de domínio bem definidos, como arquiteturas orientadas a eventos organizam produtores, consumidores e tópicos, como contêineres e Kubernetes automatizam a implantação e a recuperação desses serviços, e como garantir comunicação segura entre eles. Os padrões *outbox* e as sagas estudados aqui reaparecerão como parte central da arquitetura orientada a eventos da próxima unidade.

### Atividade prática

Modele a saga completa pedido–estoque–pagamento–expedição da NexaOrder.

1. Liste as etapas na ordem em que devem ocorrer e indique, para cada uma, a ação compensatória correspondente.
2. Escolha entre coreografia e orquestração, justificando a escolha para esse fluxo específico.
3. Indique em quais etapas o padrão *outbox* deveria ser aplicado, e por quê.
4. Defina onde uma chave de idempotência deveria ser verificada para evitar o cenário de pagamento duplicado descrito na situação-problema desta aula.

Represente o resultado em um diagrama de fluxo com as etapas normais e as etapas de compensação claramente distinguidas.

### Síntese da aula

- Atomicidade dentro de um único banco de dados não se estende automaticamente a operações que atravessam múltiplos serviços.
- A confirmação em duas fases garante atomicidade distribuída, mas bloqueia recursos e é vulnerável à falha do coordenador.
- Sagas substituem uma transação única por uma sequência de transações locais com ações compensatórias.
- Sagas coreografadas dispensam um coordenador central; sagas orquestradas concentram o fluxo em um componente explícito e rastreável.
- O padrão *outbox* evita o problema da escrita dupla entre banco de dados e mensageria; o padrão *inbox* evita o reprocessamento de mensagens duplicadas.
- Como sistemas de mensageria tipicamente entregam mensagens pelo menos uma vez, o efeito de exatamente uma vez depende de tornar as operações idempotentes.

### Roteiro da Videoaula 8 — “Sem transação global: como uma compra sobrevive a quatro falhas possíveis”

O roteiro falado e as indicações de edição estão desenvolvidos no arquivo `roteiros_20min.md`, retomando o incidente do pagamento duplicado da NexaOrder como demonstração central.

### Referências da aula

- RICHARDSON, Chris. *Microservices Patterns*. Shelter Island: Manning, 2018.
- KLEPPMANN, Martin. *Designing Data-Intensive Applications*. Sebastopol: O'Reilly Media, 2017.
- COULOURIS, George et al. *Distributed Systems: Concepts and Design*. 5. ed. Boston: Addison-Wesley, 2011.

## Atividades, síntese e material complementar

### Quiz não avaliativo

**Questão 1.** Um sistema replica um catálogo de produtos entre cinco nós e utiliza escrita com $W = 1$ e leitura com $R = 1$. Um cliente atualiza o preço de um produto e, na sequência imediata, outro cliente consulta esse mesmo produto em um nó diferente. Qual é a consequência mais provável dessa configuração?

a. A leitura sempre refletirá o novo preço, pois $W$ e $R$ são independentes de $N$.
b. A leitura nunca refletirá o novo preço, pois $W = 1$ impede a propagação da escrita.
c. A configuração garante consistência forte, pois ambos os valores são mínimos.
*d. A leitura pode retornar o preço antigo, pois não há garantia de sobreposição entre os nós de escrita e de leitura quando $W + R \leq N$.
e. A leitura falhará com erro, pois $W = 1$ e $R = 1$ são valores inválidos para um sistema com cinco nós.

*Feedback:* a alternativa correta é d. A regra de sobreposição de quórum exige $W + R > N$ para garantir que toda leitura consulte pelo menos um nó que participou da escrita mais recente. Com $W = 1$, $R = 1$ e $N = 5$, temos $1 + 1 = 2$, muito abaixo de $N$; a leitura pode perfeitamente atingir um nó que ainda não recebeu a atualização, retornando um valor obsoleto. Essa configuração prioriza latência mínima em ambas as operações, à custa de qualquer garantia de atualidade — coerente com a decisão de tratar o catálogo como um dado tolerante a consistência eventual.

**Questão 2.** Em um cluster Raft de sete nós, três nós ficam temporariamente isolados por uma falha de rede, enquanto os outros quatro permanecem capazes de se comunicar entre si. O que se espera que aconteça com a capacidade de aceitar novas escritas nesse cluster?

a. Nenhum dos dois grupos consegue aceitar escritas, pois o cluster inteiro precisa estar íntegro.
b. Ambos os grupos continuam aceitando escritas de forma independente, pois cada um tem nós suficientes para operar.
c. Apenas o grupo de três nós aceita escritas, pois grupos menores respondem mais rápido.
*d. Apenas o grupo de quatro nós aceita escritas, pois somente ele forma maioria em um cluster de sete.
e. Os dois grupos alternam a capacidade de escrita a cada poucos segundos, até a rede ser restabelecida.

*Feedback:* a alternativa correta é d. Em um cluster de sete nós, a maioria mínima necessária para eleger um líder e confirmar entradas de log é de quatro nós. O grupo de quatro consegue formar essa maioria e continuar operando; o grupo de três, isolado, não alcança maioria e permanece sem líder até a partição ser resolvida. Esse comportamento é uma aplicação prática do critério $f = \lfloor (N-1)/2 \rfloor$ estudado na Aula 7 e ilustra por que o Raft prioriza consistência (CP) em detrimento da disponibilidade do lado minoritário durante uma partição de rede.

### Síntese da unidade

- Replicar dados melhora disponibilidade e latência de leitura, mas obriga a escolher, para cada dado, entre consistência forte, causal, centrada no cliente ou eventual.
- Quóruns de leitura e escrita, com $W + R > N$, oferecem uma forma configurável de equilibrar consistência e disponibilidade sem depender de um único extremo.
- Particionar dados horizontalmente permite escalar volume e carga além da capacidade de um único nó, mas exige escolher uma chave de partição alinhada aos padrões de consulta mais frequentes.
- O hashing consistente reduz drasticamente o custo de rebalanceamento quando nós são adicionados ou removidos, mas não elimina pontos quentes causados por chaves com popularidade desproporcional.
- O teorema CAP descreve a escolha entre consistência e disponibilidade durante uma partição de rede; o PACELC estende essa análise ao compromisso cotidiano entre latência e consistência.
- Algoritmos de consenso como o Raft resolvem, de forma automática e auditável, o problema de eleger um líder único e manter um log replicado, evitando situações de múltiplos líderes concorrentes.
- Transações que atravessam múltiplos serviços podem ser mantidas coerentes por sagas com ações compensatórias, em vez de um coordenador bloqueante como o 2PC.
- Os padrões *outbox*, *inbox* e chaves de idempotência protegem operações distribuídas contra os efeitos de mensagens duplicadas, tornando o processamento efetivamente único do ponto de vista do negócio.

### Material complementar

**Direto da Fonte:** KLEPPMANN, Martin. *Designing Data-Intensive Applications*. Sebastopol: O'Reilly Media, 2017. Capítulo 5 ("Replication") e Capítulo 9 ("Consistency and Consensus") aprofundam, com exemplos de sistemas reais, os modelos de replicação, os níveis de consistência e os algoritmos de consenso discutidos nesta unidade — leitura recomendada para quem deseja relacionar os conceitos apresentados a implementações concretas de bancos de dados distribuídos amplamente usados na indústria.

**Para Mergulhar:** o blog técnico *Jepsen* (disponível em jepsen.io), mantido por Kyle Kingsbury, publica análises independentes e detalhadas de como bancos de dados distribuídos reais se comportam sob partições de rede, falhas de nó e condições de concorrência extremas — um contraponto empírico valioso às garantias teóricas de consistência e consenso estudadas nesta unidade, mostrando como implementações reais às vezes falham em cumprir as promessas de seus próprios manuais.

**Podcast:** ONGARO, Diego. *Raft: In Search of an Understandable Consensus Algorithm*. Tech talk em vídeo, YouTube, 2014. Disponível em: <https://www.youtube.com/watch?v=LAqyTyNUYSY>. Acesso em: 30 jul. 2026. Diego Ongaro, coautor do algoritmo, apresenta a motivação de projeto do Raft e compara suas escolhas com as do Paxos, aprofundando o conteúdo da Aula 7.

**Artigo científico:** GILBERT, Seth; LYNCH, Nancy. Brewer's conjecture and the feasibility of consistent, available, partition-tolerant web services. *ACM SIGACT News*, v. 33, n. 2, p. 51-59, jun. 2002. DOI: 10.1145/564585.564601. O artigo apresenta a prova formal do que ficou conhecido como teorema CAP, discutido na Aula 6, e é leitura de referência obrigatória para quem deseja compreender os limites formais — e não apenas a versão popularizada — do compromisso entre consistência, disponibilidade e tolerância a partição.
