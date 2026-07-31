# Questionário — Unidade 3

Quantidade obrigatória: 40 questões.  
Distribuição: 20 questões de asserção-razão (1 a 20) + 20 questões de interpretação (21 a 40).  
Cada questão possui cinco alternativas; a alternativa correta é marcada com `*`.

## Questões

### Bloco 1 — Asserção-razão (1 a 20)

Todas as questões deste bloco seguem o padrão ENADE de asserção-razão, com as cinco alternativas fixas repetidas em cada questão a seguir (apenas a letra marcada como correta varia, conforme o valor-verdade real das asserções I e II).

**Questão 1**

I. A separação física de um sistema em múltiplos serviços não garante, por si só, autonomia de implantação.

PORQUE

II. Quando serviços compartilham o mesmo esquema de banco de dados, uma alteração em um deles pode exigir mudança coordenada nos demais, reduzindo a autonomia de implantação.

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**Questão 2**

I. O contexto delimitado ajuda a decidir onde separar serviços em uma arquitetura como a da NexaOrder.

PORQUE

II. O protocolo HTTP permite comunicação síncrona entre serviços utilizando métodos como GET e POST.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**Questão 3**

I. Um monólito modular mantém uma única unidade de implantação, mas impõe fronteiras internas rígidas entre módulos.

PORQUE

II. Um monólito modular, por definição, permite que cada módulo seja implantado de forma totalmente independente dos demais.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**Questão 4**

I. Um API Gateway deve concentrar as principais regras de negócio da aplicação para simplificar os serviços internos.

PORQUE

II. Quando um gateway acumula regras de negócio, ele se transforma em um novo monólito escondido atrás de uma fachada de microsserviços.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**Questão 5**

I. A métrica de instabilidade I = Ce / (Ca + Ce) determina, de forma definitiva e objetiva, se um serviço deve ser dividido em dois.

PORQUE

II. Serviços com alta instabilidade devem sempre ser fundidos em um único serviço para reduzir o acoplamento aferente.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

**Questão 6**

I. Em uma arquitetura orientada a eventos, um produtor pode publicar um evento sem saber quais consumidores irão processá-lo.

PORQUE

II. Eventos de domínio são publicados sem destinatário específico, permitindo que múltiplos consumidores reajam de forma independente ao mesmo fato.

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**Questão 7**

I. A ordenação de eventos é garantida dentro de uma mesma partição de um tópico.

PORQUE

II. O protocolo TLS mútuo verifica a identidade de ambas as partes envolvidas em uma comunicação.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**Questão 8**

I. A semântica at-least-once garante que um evento nunca será perdido, mas pode ser entregue mais de uma vez.

PORQUE

II. A semântica at-least-once impede completamente que um consumidor processe o mesmo evento mais de uma vez.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**Questão 9**

I. O número de partições de um tópico pode ser ignorado no dimensionamento do paralelismo de um grupo de consumidores, pois consumidores extras sempre aumentam o throughput.

PORQUE

II. Cada partição de um tópico só pode ser atribuída a uma instância de um grupo de consumidores por vez, o que limita o paralelismo útil ao número de partições disponíveis.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**Questão 10**

I. A retenção de eventos em uma plataforma de transmissão é sempre de poucos segundos, o que torna o reprocessamento inviável na prática.

PORQUE

II. Alterar o tipo de um campo já existente em um evento é sempre uma mudança segura que preserva compatibilidade retroativa.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

**Questão 11**

I. Quando uma instância de um serviço falha, o Kubernetes pode recriar uma nova instância automaticamente, sem intervenção manual.

PORQUE

II. O laço de reconciliação compara continuamente o estado observado do cluster com o estado desejado declarado e age para reduzir a diferença entre eles.

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**Questão 12**

I. Um Service do Kubernetes expõe um conjunto de Pods sob um endereço de rede estável, mesmo quando Pods individuais são substituídos.

PORQUE

II. Imagens de contêiner são construídas a partir de camadas imutáveis.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**Questão 13**

I. O reinício em loop de um Pod pode mascarar um defeito determinístico de código sem resolver sua causa raiz.

PORQUE

II. O laço de reconciliação do Kubernetes é capaz de identificar e corrigir automaticamente a causa raiz de um defeito de código.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**Questão 14**

I. Segredos, como credenciais de acesso a um provedor de pagamento, devem ser embutidos diretamente na imagem do contêiner para garantir disponibilidade imediata.

PORQUE

II. Objetos do tipo Secret no Kubernetes permitem injetar dados sensíveis em um Pod em tempo de execução, sem alterar a imagem publicada.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**Questão 15**

I. O Horizontal Pod Autoscaler ajusta o número de réplicas de um Deployment exclusivamente com base no número de eventos publicados em um tópico.

PORQUE

II. Uma atualização gradual (rolling update) substitui todas as réplicas de um serviço simultaneamente, para garantir consistência de versão.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

**Questão 16**

I. Em um modelo de confiança zero, uma requisição originada dentro da rede interna do cluster não deve ser considerada automaticamente confiável.

PORQUE

II. O modelo de confiança zero exige que cada serviço possua uma identidade verificável e que toda comunicação seja autenticada e autorizada explicitamente, independentemente de sua origem.

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**Questão 17**

I. O princípio do menor privilégio recomenda conceder a cada identidade apenas as permissões estritamente necessárias para sua função.

PORQUE

II. Um tópico de eventos pode ser dividido em partições para permitir paralelismo entre consumidores.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**Questão 18**

I. O TLS mútuo exige que tanto o cliente quanto o servidor apresentem certificados válidos antes de estabelecer a comunicação.

PORQUE

II. O TLS mútuo é utilizado exclusivamente para proteger comunicações entre um navegador e um servidor web público, não sendo aplicável à comunicação interna entre serviços.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**Questão 19**

I. A limitação de taxa por balde de fichas tem como único objetivo impedir o acesso de usuários não autenticados a um serviço.

PORQUE

II. A limitação de taxa por balde de fichas protege um serviço contra sobrecarga, seja ela originada de tráfego legítimo em pico ou de uso indevido.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**Questão 20**

I. Um ataque de repetição (*replay*) é impossível de ocorrer em sistemas que utilizam comunicação assíncrona por eventos.

PORQUE

II. Um proxy lateral (*sidecar*) deve ser implementado separadamente dentro do código de cada serviço para que políticas de segurança sejam aplicadas.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

### Bloco 2 — Interpretação (21 a 40)

**Questão 21**

A equipe da NexaOrder percebe que todo *deploy* do serviço de pedidos exige, no mesmo horário, um *deploy* coordenado do serviço de estoque, porque os dois serviços leem e escrevem diretamente na mesma tabela de itens. Nenhum dos dois times consegue testar ou implantar de forma isolada.

Qual conceito discutido na Aula 9 explica com mais precisão esse cenário?

*a. Monólito distribuído — a separação física não produziu autonomia real porque os serviços compartilham dados e ciclo de implantação.
b. Confiança zero — a comunicação entre pedidos e estoque não está sendo autenticada.
c. Laço de reconciliação — o Kubernetes está tentando restaurar o estado desejado dos dois serviços.
d. Semântica exactly-once — os eventos entre os dois serviços estão sendo processados de forma duplicada.
e. Balde de fichas — o tráfego entre os dois serviços excede a capacidade configurada.

**Questão 22**

Ao calcular a instabilidade I = Ce / (Ca + Ce) de dois serviços da NexaOrder, a equipe obtém: serviço de estoque, com Ca = 3 e Ce = 1, resultando em I = 0,25; serviço de catálogo, com Ca = 1 e Ce = 4, resultando em I = 0,8.

Com base nesses valores, qual afirmação é mais adequada?

a. O serviço de catálogo é mais estável que o de estoque, pois seu Ce é maior.
*b. O serviço de catálogo é mais instável que o de estoque, pois depende proporcionalmente de mais serviços do que é dependido por eles.
c. Ambos os serviços apresentam exatamente o mesmo grau de instabilidade.
d. A instabilidade calculada determina, sozinha, que o serviço de catálogo deve ser removido da arquitetura.
e. Quanto maior o valor de I, mais estável é o serviço.

**Questão 23**

A tela de detalhes do pedido no aplicativo da NexaOrder precisa exibir dados de pedidos, estoque e expedição em uma única tela. A equipe decide que o próprio aplicativo fará três chamadas diretas, uma para cada serviço, em vez de utilizar um ponto de entrada único.

Qual é o principal risco dessa decisão, à luz do conceito de API Gateway apresentado na aula?

a. Nenhum risco relevante, pois cada serviço já possui seu próprio armazenamento de dados.
b. O aplicativo passará a processar eventos de domínio de forma incorreta.
*c. O aplicativo cliente passa a conhecer a topologia interna dos serviços, aumentando o acoplamento externo e multiplicando autenticação e limite de taxa em cada chamada.
d. O laço de reconciliação do Kubernetes deixará de funcionar corretamente.
e. A instabilidade dos três serviços será reduzida automaticamente.

**Questão 24**

Ao analisar o fluxo de um único caso de uso na NexaOrder, a equipe percebe que a conclusão de uma simples consulta de status de pedido dispara 14 chamadas remotas sequenciais entre cinco serviços diferentes.

O que esse padrão mais provavelmente indica, segundo os critérios apresentados na aula?

a. Que a arquitetura atingiu o nível ideal de granularidade de serviços.
b. Que os serviços envolvidos possuem baixa instabilidade.
c. Que o problema está exclusivamente relacionado à ausência de TLS mútuo.
*d. Que a fronteira entre alguns desses serviços provavelmente foi traçada no lugar errado, gerando comunicação excessivamente conversacional.
e. Que o número de partições do tópico de eventos está subdimensionado.

**Questão 25**

Ao adotar o princípio de dados por serviço, a NexaOrder deixa de poder executar um `JOIN` direto entre a tabela de pedidos e a tabela de itens de estoque, que antes pertenciam ao mesmo banco de dados.

Qual é a consequência mais provável e esperada dessa decisão?

a. A eliminação total da necessidade de comunicação entre pedidos e estoque.
b. A garantia de que nenhuma inconsistência temporária poderá ocorrer entre os dois serviços.
c. A obrigatoriedade de fundir os dois serviços em um único banco de dados compartilhado.
d. A eliminação do conceito de contexto delimitado entre os dois serviços.
*e. A necessidade de obter dados combinados por composição explícita, como chamadas de API ou réplicas assíncronas, ao custo de possível atraso de propagação.

**Questão 26**

A NexaOrder decide particionar o tópico "eventos-pedido" utilizando como chave o identificador da região geográfica do cliente, em vez do identificador do pedido.

Qual é a consequência técnica mais provável dessa escolha, segundo o que foi discutido na Aula 10?

*a. Eventos de um mesmo pedido processados por serviços em regiões diferentes podem cair em partições distintas e chegar fora de ordem ao consumidor.
b. O throughput do tópico aumentará automaticamente, independentemente do número de partições.
c. A retenção de eventos deixará de ser configurável.
d. A semântica de entrega passará automaticamente a ser exactly-once.
e. O gateway de API passará a compor as respostas dos serviços de forma incorreta.

**Questão 27**

O tópico "eventos-pedido" da NexaOrder possui 8 partições. Um grupo de consumidores responsável por atualizar o painel operacional passa a ter 10 instâncias.

O que ocorre com as duas instâncias excedentes desse grupo?

a. Elas processam, cada uma, metade da carga de uma partição já atribuída a outra instância.
*b. Elas permanecem ociosas, pois não há partições disponíveis para atribuir a elas.
c. Elas assumem partições do grupo de consumidores responsável pelo envio de e-mails.
d. Elas forçam o tópico a criar automaticamente duas novas partições.
e. Elas processam eventos fora de ordem, violando a garantia de ordenação por partição.

**Questão 28**

O consumidor responsável por enviar o e-mail de confirmação de pedido na NexaOrder confirma o recebimento do evento antes de efetivamente enviar o e-mail. Uma falha ocorre exatamente entre a confirmação e o envio.

Qual é o resultado mais provável desse desenho, considerando as semânticas de entrega discutidas na aula?

a. O evento será reprocessado automaticamente, garantindo o envio do e-mail sem duplicação.
b. O consumidor alcançará automaticamente uma semântica exactly-once.
*c. O e-mail de confirmação pode não ser enviado, caracterizando um comportamento próximo de at-most-once, já que a confirmação ocorreu antes da conclusão do processamento.
d. O evento será duplicado indefinidamente até ser reprocessado manualmente.
e. A ordenação de eventos dentro da partição será violada.

**Questão 29**

Um serviço da NexaOrder renomeia o campo `valor_total` para `valor_liquido` no evento "pedido criado", sem qualquer período de transição, e publica a nova versão diretamente em produção.

Qual é a consequência mais provável para consumidores que ainda não foram atualizados?

a. Nenhuma, pois toda mudança de esquema é automaticamente compatível.
b. Os consumidores antigos passarão a processar os eventos mais rapidamente.
c. A ordenação por partição será automaticamente corrigida.
*d. Os consumidores antigos provavelmente interpretarão o pedido como se não tivesse valor, pois o campo esperado não existe mais no evento.
e. O tópico será automaticamente dividido em mais partições para compensar a mudança.

**Questão 30**

A NexaOrder projeta um novo tópico para eventos de rastreamento de expedição, com taxa de pico estimada de 900 eventos por segundo. Cada consumidor sustenta, de forma confiável, 100 eventos por segundo.

Qual é o número mínimo de partições necessário para sustentar esse pico, considerando a fórmula P = ⌈λ_pico / C_consumidor⌉ apresentada na aula?

a. 6 partições.
b. 7 partições.
c. 8 partições.
d. 90 partições.
*e. 9 partições.

**Questão 31**

Um Pod do serviço de expedição da NexaOrder é removido manualmente por um engenheiro durante um teste, sem qualquer alteração no manifesto do Deployment correspondente.

O que o Kubernetes deve fazer, considerando o laço de reconciliação discutido na Aula 11?

*a. Criar um novo Pod automaticamente, pois o estado desejado declarado no Deployment ainda especifica o número original de réplicas.
b. Reduzir permanentemente o número de réplicas declarado no Deployment.
c. Aguardar uma nova solicitação humana antes de qualquer ação.
d. Migrar automaticamente o serviço de expedição para um novo cluster.
e. Interromper o Service associado até nova configuração manual.

**Questão 32**

O Deployment do serviço de estoque da NexaOrder possui 5 réplicas atuais, utilização média observada de CPU de 90% e utilização alvo configurada de 50%.

Qual o número de réplicas resultante, segundo a fórmula N = ⌈N_atual × U_atual / U_alvo⌉ apresentada na aula?

a. 5 réplicas.
*b. 9 réplicas.
c. 10 réplicas.
d. 4 réplicas.
e. 45 réplicas.

**Questão 33**

Um Pod do serviço de pagamento da NexaOrder é recriado pelo Kubernetes repetidamente, a cada poucos minutos, sempre travando sob o mesmo padrão de carga.

Qual é a interpretação mais adequada desse cenário, à luz do que foi discutido na aula?

a. O problema está definitivamente resolvido, pois o serviço volta a responder após cada recriação.
b. O laço de reconciliação identificou e corrigiu a causa raiz do defeito.
*c. A recriação automática mantém a disponibilidade aparente do serviço, mas provavelmente mascara um defeito recorrente que exige diagnóstico humano.
d. O Service associado deixará de rotear tráfego para esse Deployment.
e. A imagem do contêiner deixou de ser imutável.

**Questão 34**

Um novo integrante da equipe sugere embutir a credencial do provedor de pagamento diretamente na imagem do contêiner do serviço de pagamento, para simplificar a implantação.

Por que essa prática é desaconselhada, segundo os conceitos discutidos na aula?

a. Porque imagens de contêiner não podem conter nenhum tipo de arquivo de configuração.
b. Porque o Kubernetes rejeita automaticamente imagens que contenham qualquer variável de ambiente.
c. Porque isso impediria o laço de reconciliação de funcionar corretamente.
*d. Porque credenciais embutidas na imagem ficam expostas a qualquer pessoa com acesso a ela e exigem nova publicação da imagem a cada rotação de credencial, ao contrário de um Secret injetado em tempo de execução.
e. Porque isso tornaria o serviço automaticamente instável, segundo a métrica I = Ce/(Ca+Ce).

**Questão 35**

A NexaOrder publica a versão 1.8.0 do serviço de pagamento e configura uma atualização gradual (*rolling update*) com limites que impedem a redução da capacidade total abaixo do necessário.

Qual é o comportamento esperado durante essa atualização?

a. Todas as réplicas da versão 1.7.0 são removidas simultaneamente antes de qualquer réplica da versão 1.8.0 ser criada.
b. O Service associado interrompe o roteamento de tráfego até a conclusão completa da atualização.
c. A atualização exige que o número de partições do tópico de eventos seja recalculado.
d. Todas as réplicas da versão 1.8.0 são criadas de uma só vez, sem qualquer controle de disponibilidade.
*e. Réplicas antigas são substituídas por novas de forma incremental, mantendo o total de réplicas saudáveis dentro dos limites configurados.

**Questão 36**

Um invasor obtém acesso a um Pod de baixo privilégio dentro do cluster da NexaOrder e tenta, a partir dele, estabelecer conexão direta com o serviço de pagamento.

Em uma arquitetura corretamente configurada com confiança zero e TLS mútuo, o que deveria ocorrer?

*a. A conexão deveria ser recusada, pois o Pod comprometido não possui um certificado de identidade autorizado para se comunicar com o serviço de pagamento.
b. A conexão deveria ser aceita automaticamente, pois ambos estão na mesma rede interna do cluster.
c. O laço de reconciliação impediria automaticamente a existência do Pod comprometido.
d. O balde de fichas do serviço de pagamento aumentaria automaticamente sua capacidade para atender à nova conexão.
e. A instabilidade do serviço de pagamento aumentaria, impedindo qualquer conexão.

**Questão 37**

Por engano, a identidade de serviço "expedição" da NexaOrder recebe permissão para solicitar reembolsos ao serviço de pagamento, além de suas permissões originais de consulta e confirmação de envio.

Qual princípio discutido na aula está sendo violado?

a. Confiança zero, pois toda comunicação interna deveria ser proibida.
*b. Menor privilégio, pois a identidade "expedição" recebeu permissão além do estritamente necessário para sua função.
c. Limitação de taxa, pois o balde de fichas do serviço de pagamento foi mal configurado.
d. Evolução de esquema, pois o formato do evento de pagamento foi alterado sem compatibilidade.
e. Reconciliação, pois o estado desejado do Deployment não corresponde ao estado observado.

**Questão 38**

O serviço de pagamento da NexaOrder configura um balde de fichas com capacidade de 40 fichas e taxa de reposição de 15 fichas por segundo. Uma rajada de 60 requisições chega em um único segundo.

Quantas dessas requisições são atendidas imediatamente, considerando apenas a capacidade do balde?

a. 15 requisições, correspondentes à taxa de reposição sustentável em regime permanente.
b. 60 requisições, pois o balde absorve toda a rajada instantaneamente.
*c. 40 requisições, correspondentes à capacidade do balde; as demais serão recusadas ou atrasadas até a reposição de novas fichas.
d. 0 requisições, pois qualquer rajada acima da taxa de reposição é integralmente recusada.
e. 25 requisições, referentes à diferença entre a rajada e a capacidade do balde.

**Questão 39**

Um invasor captura uma mensagem legítima de autorização de pagamento da NexaOrder e a reenvia horas depois, tentando produzir uma nova cobrança sobre o mesmo pedido.

Qual mecanismo, discutido na aula, mitiga diretamente esse tipo de ataque?

a. Escalonamento automático horizontal baseado em utilização de CPU.
b. Composição de respostas por um API Gateway.
c. Retenção estendida de eventos em um tópico.
*d. Identificador único de operação associado a uma janela de validade, permitindo que o serviço de pagamento rejeite repetições indevidas.
e. Aumento do número de partições do tópico de eventos.

**Questão 40**

Em vez de implementar autenticação mútua e limite de taxa dentro do código de cada um dos quatro serviços da NexaOrder, a equipe de plataforma decide implantar um proxy lateral junto a cada serviço, coordenado por um plano de controle central.

Qual conceito discutido na aula essa decisão representa?

a. Confiança zero aplicada exclusivamente à borda externa do sistema.
b. Substituição do laço de reconciliação por um mecanismo de autenticação.
c. Eliminação da necessidade de gestão de segredos.
d. Redução da instabilidade dos serviços, segundo a métrica I = Ce/(Ca+Ce).
*e. Adoção de um *service mesh*, que centraliza políticas de segurança e comunicação sem replicá-las no código de cada serviço individualmente.

## Gabarito e feedbacks

**Questão 1** (correta: a)
- a. Correta. As duas asserções são verdadeiras: a separação física realmente não garante autonomia, e o compartilhamento de esquema de dados é exatamente o mecanismo que explica por que essa autonomia não se concretiza.
- b. Incorreta. A II não é apenas verdadeira e desconexa: ela justifica diretamente a I, ao explicar o mecanismo pelo qual a separação física não produz autonomia.
- c. Incorreta. A II também é verdadeira, não falsa: esquema compartilhado de fato exige coordenação de mudanças.
- d. Incorreta. A I é verdadeira, não falsa: a experiência da NexaOrder confirma que dividir fisicamente não basta.
- e. Incorreta. Ambas as asserções são verdadeiras, não falsas.

**Questão 2** (correta: b)
- a. Incorreta. A II é verdadeira, mas não justifica a I: o fato de o HTTP permitir chamadas síncronas não explica por que contexto delimitado orienta fronteiras de serviço.
- b. Correta. Ambas as afirmações são verdadeiras isoladamente, mas tratam de assuntos distintos: uma fala de modelagem de domínio, a outra de um protocolo de comunicação. A II não justifica a I.
- c. Incorreta. A II também é verdadeira: o HTTP de fato permite comunicação síncrona com GET e POST.
- d. Incorreta. A I é verdadeira: contexto delimitado é exatamente o critério discutido na aula para desenhar fronteiras.
- e. Incorreta. Ambas as asserções são verdadeiras.

**Questão 3** (correta: c)
- a. Incorreta. A II é falsa, não verdadeira: monólito modular, por definição, mantém uma única unidade de implantação.
- b. Incorreta. A II é falsa, não apenas desconexa da I.
- c. Correta. A I descreve corretamente o monólito modular; a II o contradiz, pois afirma implantação totalmente independente dos módulos, o que descaracterizaria a própria definição de monólito.
- d. Incorreta. A I é verdadeira, não falsa.
- e. Incorreta. A I é verdadeira; apenas a II é falsa.

**Questão 4** (correta: d)
- a. Incorreta. A I é falsa: um gateway não deve concentrar regras de negócio.
- b. Incorreta. A I é falsa, e a questão não trata de asserções ambas verdadeiras.
- c. Incorreta. A I é falsa, não verdadeira.
- d. Correta. A I contraria o que foi ensinado na aula — o gateway não deve acumular regras de negócio — enquanto a II descreve corretamente o risco de isso acontecer.
- e. Incorreta. A II é verdadeira, não falsa.

**Questão 5** (correta: e)
- a. Incorreta. Nenhuma das duas asserções é verdadeira da forma como está enunciada.
- b. Incorreta. Ambas as asserções são falsas, não verdadeiras.
- c. Incorreta. A I também é falsa: a métrica é um heurístico de apoio, não um critério definitivo e objetivo isolado.
- d. Incorreta. A II também é falsa: alta instabilidade não implica necessariamente fusão de serviços.
- e. Correta. A métrica de instabilidade é um heurístico de apoio à discussão, não uma regra definitiva de decisão; e alta instabilidade não determina automaticamente a fusão de serviços.

**Questão 6** (correta: a)
- a. Correta. Ambas as afirmações são verdadeiras, e a II explica diretamente por que a I é verdadeira: eventos sem destinatário específico permitem que o produtor não precise conhecer os consumidores.
- b. Incorreta. A II justifica sim a I, não é uma relação apenas coincidente.
- c. Incorreta. A II também é verdadeira.
- d. Incorreta. A I é verdadeira, não falsa.
- e. Incorreta. Ambas são verdadeiras.

**Questão 7** (correta: b)
- a. Incorreta. A II não justifica a I: TLS mútuo trata de identidade em comunicação, não de ordenação de eventos.
- b. Correta. Ambas as afirmações são verdadeiras isoladamente, mas tratam de temas distintos — ordenação por partição e verificação de identidade — sem relação de justificativa entre si.
- c. Incorreta. A II também é verdadeira.
- d. Incorreta. A I é verdadeira, não falsa.
- e. Incorreta. Ambas são verdadeiras.

**Questão 8** (correta: c)
- a. Incorreta. A II é falsa: at-least-once não impede duplicação, pelo contrário, ela é a característica central dessa semântica.
- b. Incorreta. A II é falsa, não apenas desconexa.
- c. Correta. A I descreve corretamente a semântica at-least-once; a II a contradiz diretamente, pois afirma o oposto do que essa semântica garante.
- d. Incorreta. A I é verdadeira, não falsa.
- e. Incorreta. A I é verdadeira; apenas a II é falsa.

**Questão 9** (correta: d)
- a. Incorreta. A I é falsa: consumidores extras além do número de partições não aumentam throughput.
- b. Incorreta. A I é falsa, então a relação de asserções ambas verdadeiras não se aplica.
- c. Incorreta. A I é falsa, não verdadeira.
- d. Correta. A I contraria o que foi ensinado: adicionar consumidores além do número de partições não aumenta throughput. A II descreve corretamente a razão para esse limite.
- e. Incorreta. A II é verdadeira, não falsa.

**Questão 10** (correta: e)
- a. Incorreta. Nenhuma das duas é verdadeira.
- b. Incorreta. Ambas são falsas, não verdadeiras.
- c. Incorreta. A I também é falsa: a retenção é configurável e frequentemente estendida por horas ou dias, viabilizando reprocessamento.
- d. Incorreta. A II também é falsa: alterar o tipo de um campo costuma quebrar compatibilidade.
- e. Correta. A retenção de eventos é configurável e tipicamente mais longa do que poucos segundos, viabilizando reprocessamento; e alterar o tipo de um campo existente costuma ser uma mudança insegura, não uma mudança automaticamente compatível.

**Questão 11** (correta: a)
- a. Correta. Ambas as afirmações são verdadeiras, e a II explica exatamente o mecanismo — o laço de reconciliação — que produz o comportamento descrito na I.
- b. Incorreta. A II justifica diretamente a I; não é uma coincidência de duas verdades desconexas.
- c. Incorreta. A II também é verdadeira.
- d. Incorreta. A I é verdadeira, não falsa.
- e. Incorreta. Ambas são verdadeiras.

**Questão 12** (correta: b)
- a. Incorreta. A II não justifica a I: imutabilidade de imagens não explica por que um Service mantém endereço estável.
- b. Correta. Ambas as afirmações são verdadeiras isoladamente, mas tratam de conceitos distintos do Kubernetes, sem relação de causa entre si.
- c. Incorreta. A II também é verdadeira.
- d. Incorreta. A I é verdadeira, não falsa.
- e. Incorreta. Ambas são verdadeiras.

**Questão 13** (correta: c)
- a. Incorreta. A II é falsa: o laço de reconciliação não identifica nem corrige causas de código, apenas restaura quantidade e execução declaradas.
- b. Incorreta. A II é falsa, não apenas desconexa.
- c. Correta. A I descreve corretamente o risco do reinício em loop; a II o contradiz, atribuindo ao laço de reconciliação uma capacidade de diagnóstico que ele não possui.
- d. Incorreta. A I é verdadeira, não falsa.
- e. Incorreta. A I é verdadeira; apenas a II é falsa.

**Questão 14** (correta: d)
- a. Incorreta. A I é falsa: embutir segredos na imagem é uma prática desaconselhada, não recomendada.
- b. Incorreta. A I é falsa, não verdadeira.
- c. Incorreta. A I é falsa, não verdadeira.
- d. Correta. A I contraria a prática recomendada apresentada na aula; a II descreve corretamente o mecanismo do Kubernetes para gestão segura de segredos.
- e. Incorreta. A II é verdadeira, não falsa.

**Questão 15** (correta: e)
- a. Incorreta. Nenhuma das duas é verdadeira.
- b. Incorreta. Ambas são falsas, não verdadeiras.
- c. Incorreta. A I também é falsa: o HPA se baseia em métricas como utilização de CPU, não no número de eventos publicados.
- d. Incorreta. A II também é falsa: rolling update substitui réplicas de forma incremental, não simultânea.
- e. Correta. O Horizontal Pod Autoscaler baseia-se em métricas como utilização de recursos, não no número de eventos publicados; e a atualização gradual substitui réplicas de forma incremental, não simultânea.

**Questão 16** (correta: a)
- a. Correta. Ambas as afirmações são verdadeiras, e a II descreve exatamente a exigência do modelo de confiança zero que justifica por que a origem interna não deve ser considerada automaticamente confiável.
- b. Incorreta. A II justifica diretamente a I.
- c. Incorreta. A II também é verdadeira.
- d. Incorreta. A I é verdadeira, não falsa.
- e. Incorreta. Ambas são verdadeiras.

**Questão 17** (correta: b)
- a. Incorreta. A II não justifica a I: partições de tópico não têm relação com o princípio do menor privilégio.
- b. Correta. Ambas as afirmações são verdadeiras isoladamente, mas tratam de temas distintos — segurança e mensageria — sem relação de justificativa entre si.
- c. Incorreta. A II também é verdadeira.
- d. Incorreta. A I é verdadeira, não falsa.
- e. Incorreta. Ambas são verdadeiras.

**Questão 18** (correta: c)
- a. Incorreta. A II é falsa: TLS mútuo é amplamente aplicado à comunicação interna entre serviços, não apenas a navegadores.
- b. Incorreta. A II é falsa, não apenas desconexa.
- c. Correta. A I descreve corretamente o funcionamento do TLS mútuo; a II o contradiz ao restringir indevidamente seu uso.
- d. Incorreta. A I é verdadeira, não falsa.
- e. Incorreta. A I é verdadeira; apenas a II é falsa.

**Questão 19** (correta: d)
- a. Incorreta. A I é falsa: a limitação de taxa protege contra sobrecarga, não é um mecanismo de autenticação.
- b. Incorreta. A I é falsa, não verdadeira.
- c. Incorreta. A I é falsa, não verdadeira.
- d. Correta. A I restringe indevidamente o propósito da limitação de taxa; a II descreve corretamente seu objetivo, que inclui tráfego legítimo em pico e uso indevido.
- e. Incorreta. A II é verdadeira, não falsa.

**Questão 20** (correta: e)
- a. Incorreta. Nenhuma das duas é verdadeira.
- b. Incorreta. Ambas são falsas, não verdadeiras.
- c. Incorreta. A I também é falsa: ataques de repetição podem ocorrer mesmo em comunicação assíncrona por eventos, se não houver deduplicação.
- d. Incorreta. A II também é falsa: o proxy lateral existe justamente para evitar reimplementar políticas de segurança no código de cada serviço.
- e. Correta. Ataques de repetição não são exclusivos de comunicação síncrona e podem afetar eventos sem deduplicação adequada; e o proxy lateral tem como propósito justamente centralizar políticas de segurança fora do código de cada serviço.

**Questão 21** (correta: a)
- a. Correta. O cenário descreve exatamente os sintomas de um monólito distribuído: separação física sem autonomia real de dados ou implantação.
- b. Incorreta. O cenário não menciona ausência de autenticação entre os serviços.
- c. Incorreta. O laço de reconciliação é um mecanismo do Kubernetes, não relacionado ao acoplamento de dados descrito.
- d. Incorreta. Não há menção a processamento de eventos duplicados no cenário.
- e. Incorreta. Não há menção a limitação de taxa ou sobrecarga de tráfego no cenário.

**Questão 22** (correta: b)
- a. Incorreta. A afirmação inverte o significado da métrica: Ce alto contribui para maior instabilidade, não maior estabilidade.
- b. Correta. Um valor de I mais próximo de 1 indica maior instabilidade; o catálogo, com I = 0,8, depende proporcionalmente mais de outros serviços do que é dependido por eles.
- c. Incorreta. Os valores calculados (0,25 e 0,8) são diferentes.
- d. Incorreta. A métrica é um heurístico de apoio, não uma regra definitiva de remoção de serviços.
- e. Incorreta. É o oposto: quanto maior o valor de I, mais instável — não mais estável — é o serviço.

**Questão 23** (correta: c)
- a. Incorreta. Há risco relevante: o acoplamento entre cliente e topologia interna, independentemente de cada serviço ter seu próprio armazenamento.
- b. Incorreta. O cenário não envolve processamento de eventos de domínio.
- c. Correta. Sem um gateway, o cliente precisa conhecer e chamar diretamente cada serviço, aumentando o acoplamento externo e replicando preocupações transversais como autenticação e limite de taxa.
- d. Incorreta. O cenário não tem relação com o laço de reconciliação do Kubernetes.
- e. Incorreta. A decisão descrita não afeta a instabilidade estrutural dos serviços.

**Questão 24** (correta: d)
- a. Incorreta. Uma cadeia de 14 chamadas para uma simples consulta é sinal de problema, não de granularidade ideal.
- b. Incorreta. O cenário não fornece dados sobre acoplamento aferente e eferente para essa conclusão.
- c. Incorreta. TLS mútuo trata de segurança da comunicação, não do número de chamadas exigidas para um caso de uso.
- d. Correta. Comunicação excessivamente conversacional para um único caso de uso é um sintoma clássico de fronteiras de serviço mal desenhadas.
- e. Incorreta. O cenário descreve chamadas síncronas entre serviços, não consumo de um tópico de eventos.

**Questão 25** (correta: e)
- a. Incorreta. A comunicação entre pedidos e estoque continua necessária; apenas muda de forma.
- b. Incorreta. Dados por serviço não elimina a possibilidade de inconsistência temporária; ao contrário, costuma introduzi-la.
- c. Incorreta. A decisão de dados por serviço é o oposto de fundir bancos de dados.
- d. Incorreta. O contexto delimitado continua existindo e é, inclusive, o que justifica a separação de dados.
- e. Correta. Sem `JOIN` direto, dados de serviços diferentes precisam ser combinados por composição explícita — chamada de API ou réplica assíncrona —, o que pode introduzir atraso de propagação.

**Questão 26** (correta: a)
- a. Correta. Particionar por região em vez de por identificador de pedido quebra a garantia de que todos os eventos de um mesmo pedido caiam na mesma partição, permitindo que cheguem fora de ordem.
- b. Incorreta. O throughput depende do número de partições e consumidores, não da escolha específica da chave.
- c. Incorreta. A retenção é uma configuração independente da chave de particionamento.
- d. Incorreta. A semântica de entrega depende do desenho do produtor e consumidor, não da chave escolhida.
- e. Incorreta. O cenário não envolve um API Gateway.

**Questão 27** (correta: b)
- a. Incorreta. Uma instância não compartilha o processamento de uma partição já atribuída a outra instância do mesmo grupo.
- b. Correta. Como cada partição só pode ser atribuída a uma instância por vez, e há apenas 8 partições para 10 instâncias, duas instâncias ficam sem partição atribuída e permanecem ociosas.
- c. Incorreta. Grupos de consumidores diferentes são independentes; um grupo não assume partições de outro grupo.
- d. Incorreta. O número de partições de um tópico não é ajustado automaticamente pelo número de instâncias de um grupo.
- e. Incorreta. A ordenação dentro de cada partição continua garantida, independentemente do número de instâncias ociosas.

**Questão 28** (correta: c)
- a. Incorreta. Não há reprocessamento automático garantido nesse desenho, já que a confirmação já ocorreu antes da falha.
- b. Incorreta. Esse desenho não garante exactly-once; ao contrário, arrisca perda de efeito.
- c. Correta. Como a confirmação ocorre antes da conclusão do processamento, uma falha nesse intervalo pode levar à perda do efeito (o e-mail não enviado), sem nova tentativa — comportamento típico de at-most-once.
- d. Incorreta. Não há indício de reentrega nesse desenho, já que o evento já foi confirmado.
- e. Incorreta. O cenário não descreve um problema de ordenação dentro da partição.

**Questão 29** (correta: d)
- a. Incorreta. Renomear um campo sem transição costuma ser uma mudança insegura, não automaticamente compatível.
- b. Incorreta. A velocidade de processamento não é afetada por essa mudança de esquema.
- c. Incorreta. O cenário não envolve ordenação por partição.
- d. Correta. Consumidores antigos esperam o campo `valor_total`; como ele não existe mais no novo formato, eles provavelmente interpretarão o pedido como se não tivesse valor definido.
- e. Incorreta. O número de partições não é ajustado automaticamente por mudanças de esquema.

**Questão 30** (correta: e)
- a. Incorreta. 900 dividido por 100 resulta em 9, não em 6.
- b. Incorreta. O cálculo correto não resulta em 7.
- c. Incorreta. O cálculo correto não resulta em 8.
- d. Incorreta. 90 partições excede em muito o resultado da fórmula aplicada aos valores do enunciado.
- e. Correta. P = ⌈900 / 100⌉ = ⌈9⌉ = 9 partições.

**Questão 31** (correta: a)
- a. Correta. O manifesto do Deployment ainda declara o número original de réplicas; o laço de reconciliação detecta a divergência e cria um novo Pod para restaurar o estado desejado.
- b. Incorreta. A remoção manual de um Pod não altera o manifesto do Deployment nem reduz permanentemente o número declarado de réplicas.
- c. Incorreta. O laço de reconciliação age de forma autônoma e contínua, sem esperar nova solicitação humana para restaurar o estado desejado.
- d. Incorreta. O cenário não envolve migração de cluster.
- e. Incorreta. O Service continua roteando tráfego para os Pods saudáveis remanescentes e para o novo Pod criado.

**Questão 32** (correta: b)
- a. Incorreta. O cálculo não mantém o número de réplicas inalterado, já que a utilização está muito acima do alvo.
- b. Correta. N = ⌈5 × 90 / 50⌉ = ⌈9,0⌉ = 9 réplicas.
- c. Incorreta. O resultado do cálculo é 9, não 10.
- d. Incorreta. O resultado indica aumento de réplicas, não redução.
- e. Incorreta. 45 corresponde ao produto 5 × 90 sem a divisão pelo alvo, o que não representa a fórmula correta.

**Questão 33** (correta: c)
- a. Incorreta. A recriação repetida sob o mesmo padrão de carga indica que o problema não está resolvido, apenas mascarado temporariamente.
- b. Incorreta. O laço de reconciliação não diagnostica nem corrige causas de código; ele apenas restaura quantidade e execução declaradas.
- c. Correta. A disponibilidade aparente é mantida pela recriação automática, mas o padrão recorrente sob a mesma carga sugere um defeito determinístico que precisa de investigação humana.
- d. Incorreta. O Service continua roteando tráfego normalmente enquanto houver Pods, mesmo que estejam sendo recriados repetidamente.
- e. Incorreta. A imutabilidade da imagem não é afetada pelo padrão de reinício.

**Questão 34** (correta: d)
- a. Incorreta. Imagens de contêiner podem conter arquivos de configuração; o problema é especificamente embutir segredos sensíveis nelas.
- b. Incorreta. O Kubernetes não rejeita automaticamente imagens com variáveis de ambiente.
- c. Incorreta. Embutir credenciais na imagem não impede o funcionamento do laço de reconciliação.
- d. Correta. Credenciais embutidas na imagem ficam expostas a qualquer pessoa com acesso a ela e exigem republicação a cada rotação, ao contrário de um Secret injetado dinamicamente em tempo de execução.
- e. Incorreta. A prática descrita não tem relação direta com a métrica de instabilidade discutida na Aula 9.

**Questão 35** (correta: e)
- a. Incorreta. A remoção simultânea de todas as réplicas antigas antes de criar novas contraria o propósito de uma atualização gradual.
- b. Incorreta. O Service continua roteando tráfego durante toda a atualização gradual, exceto para réplicas momentaneamente indisponíveis.
- c. Incorreta. A atualização de versão de um serviço não exige recálculo do número de partições de um tópico de eventos.
- d. Incorreta. Criar todas as réplicas novas de uma vez, sem controle, contraria o propósito de limitar indisponibilidade e excedente durante a transição.
- e. Correta. A atualização gradual substitui réplicas antigas por novas de forma incremental, respeitando limites que preservam a capacidade saudável do serviço.

**Questão 36** (correta: a)
- a. Correta. Em confiança zero com TLS mútuo, a identidade, não a localização na rede, determina se uma conexão é aceita; um Pod comprometido sem certificado autorizado deveria ter sua conexão recusada.
- b. Incorreta. Aceitar a conexão apenas por estar na mesma rede interna é exatamente o modelo de perímetro que a confiança zero rejeita.
- c. Incorreta. O laço de reconciliação não tem relação com a prevenção de comprometimento de segurança de um Pod.
- d. Incorreta. O balde de fichas não se ajusta automaticamente para atender a uma nova conexão não autorizada.
- e. Incorreta. A instabilidade estrutural do serviço não é afetada por uma tentativa de conexão não autorizada.

**Questão 37** (correta: b)
- a. Incorreta. Confiança zero não proíbe toda comunicação interna; ela exige autenticação e autorização explícitas para cada comunicação permitida.
- b. Correta. Conceder à identidade "expedição" uma permissão além de suas necessidades funcionais viola diretamente o princípio do menor privilégio.
- c. Incorreta. O cenário não envolve volume de requisições nem configuração de balde de fichas.
- d. Incorreta. O cenário não envolve alteração de formato de evento.
- e. Incorreta. O cenário não descreve divergência entre estado desejado e observado de um Deployment.

**Questão 38** (correta: c)
- a. Incorreta. 15 é a taxa de reposição sustentável em regime permanente, não o número de requisições atendidas imediatamente pela capacidade do balde.
- b. Incorreta. O balde não absorve toda a rajada, pois sua capacidade é de apenas 40 fichas.
- c. Correta. A capacidade do balde é de 40 fichas, então até 40 requisições da rajada são atendidas imediatamente; as 20 restantes são recusadas ou atrasadas.
- d. Incorreta. O balde atende requisições até o limite de sua capacidade, não recusa integralmente a rajada.
- e. Incorreta. O número de requisições atendidas corresponde à capacidade do balde (40), não à diferença entre rajada e capacidade.

**Questão 39** (correta: d)
- a. Incorreta. O escalonamento automático trata de capacidade computacional, não de mitigação de repetição de mensagens.
- b. Incorreta. A composição de respostas por um gateway não impede o reenvio de uma mensagem capturada.
- c. Incorreta. A retenção de eventos permite reprocessamento legítimo, mas não mitiga diretamente o reenvio malicioso de uma mensagem específica.
- d. Correta. Um identificador único de operação, combinado a uma janela de validade, permite que o serviço de pagamento reconheça e rejeite uma mensagem já processada ou fora do prazo.
- e. Incorreta. O número de partições de um tópico não tem relação com a mitigação de ataques de repetição.

**Questão 40** (correta: e)
- a. Incorreta. O cenário descreve proteção da comunicação interna entre serviços, não exclusivamente da borda externa.
- b. Incorreta. O proxy lateral não substitui o laço de reconciliação, que é um mecanismo distinto do Kubernetes.
- c. Incorreta. A gestão de segredos continua necessária mesmo com um service mesh; os proxies laterais frequentemente dependem dela para obter certificados.
- d. Incorreta. A decisão descrita não altera a métrica estrutural de instabilidade dos serviços.
- e. Correta. Coordenar proxies laterais por um plano de controle central, aplicando políticas de segurança e comunicação sem replicá-las no código de cada serviço, é a definição de service mesh apresentada na aula.
