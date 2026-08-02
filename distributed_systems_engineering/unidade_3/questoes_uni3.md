# Questionário — Unidade 3

Quantidade obrigatória: 40 questões.  
Distribuição: 20 questões de asserção-razão (1 a 20) + 20 questões de interpretação (21 a 40).  
Cada questão possui cinco alternativas; a alternativa correta é marcada com `*`.

## Questões

### Bloco 1 — Asserção-razão (1 a 20)

Todas as questões deste bloco seguem o padrão ENADE de asserção-razão, com as cinco alternativas fixas repetidas em cada questão a seguir (apenas a letra marcada como correta varia, conforme o valor-verdade real das asserções I e II).

**1.** I. A separação física de um sistema em múltiplos serviços não garante, por si só, autonomia de implantação.

PORQUE

II. Quando serviços compartilham o mesmo esquema de banco de dados, uma alteração em um deles pode exigir mudança coordenada nos demais, reduzindo a autonomia de implantação.

a. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*b. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
c. As asserções I e II são proposições falsas.
d. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
e. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.

**2.** I. O contexto delimitado ajuda a decidir onde separar serviços em uma arquitetura como a da NexaOrder.

PORQUE

II. O protocolo HTTP permite comunicação síncrona entre serviços utilizando métodos como GET e POST.

*a. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
b. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
c. As asserções I e II são proposições falsas.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.

**3.** I. Um monólito modular mantém uma única unidade de implantação, mas impõe fronteiras internas rígidas entre módulos.

PORQUE

II. Um monólito modular, por definição, permite que cada módulo seja implantado de forma totalmente independente dos demais.

a. As asserções I e II são proposições falsas.
b. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
c. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*d. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
e. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.

**4.** I. Um API Gateway deve concentrar as principais regras de negócio da aplicação para simplificar os serviços internos.

PORQUE

II. Quando um gateway acumula regras de negócio, ele se transforma em um novo monólito escondido atrás de uma fachada de microsserviços.

a. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
b. As asserções I e II são proposições falsas.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*e. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.

**5.** I. A métrica de instabilidade I = Ce / (Ca + Ce) determina, de forma definitiva e objetiva, se um serviço deve ser dividido em dois.

PORQUE

II. Serviços com alta instabilidade devem sempre ser fundidos em um único serviço para reduzir o acoplamento aferente.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*d. As asserções I e II são proposições falsas.
e. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.

**6.** I. Em uma arquitetura orientada a eventos, um produtor pode publicar um evento sem saber quais consumidores irão processá-lo.

PORQUE

II. Eventos de domínio são publicados sem destinatário específico, permitindo que múltiplos consumidores reajam de forma independente ao mesmo fato.

a. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
c. As asserções I e II são proposições falsas.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.

**7.** I. Em uma partição, o consumidor observa os registros pela ordem crescente de seus offsets, sem que isso estabeleça uma ordem global entre partições.

PORQUE

II. O protocolo TLS mútuo verifica a identidade de ambas as partes envolvidas em uma comunicação.

a. As asserções I e II são proposições falsas.
b. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
c. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*d. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
e. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.

**8.** I. Sob publicação confirmada em armazenamento durável, retenção vigente e tentativas disponíveis, a semântica at-least-once busca entregar o evento uma ou mais vezes, admitindo duplicação.

PORQUE

II. A semântica at-least-once impede completamente que um consumidor processe o mesmo evento mais de uma vez.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
c. As asserções I e II são proposições falsas.
d. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*e. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.

**9.** I. O número de partições de um tópico pode ser ignorado no dimensionamento do paralelismo de um grupo de consumidores, pois consumidores extras sempre aumentam o throughput.

PORQUE

II. Cada partição de um tópico só pode ser atribuída a uma instância de um grupo de consumidores por vez, o que limita o paralelismo útil ao número de partições disponíveis.

a. As asserções I e II são proposições falsas.
*b. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
c. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
d. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
e. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.

**10.** I. A retenção de eventos em uma plataforma de transmissão é sempre de poucos segundos, o que torna o reprocessamento inviável na prática.

PORQUE

II. Alterar o tipo de um campo já existente em um evento é sempre uma mudança segura que preserva compatibilidade retroativa.

a. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
b. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. As asserções I e II são proposições falsas.
e. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.

**11.** I. Quando uma instância de um serviço falha, o Kubernetes pode recriar uma nova instância automaticamente, sem intervenção manual.

PORQUE

II. O laço de reconciliação compara continuamente o estado observado do cluster com o estado desejado declarado e age para reduzir a diferença entre eles.

a. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
d. As asserções I e II são proposições falsas.
e. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.

**12.** I. Um Service do Kubernetes expõe um conjunto de Pods sob um endereço de rede estável, mesmo quando Pods individuais são substituídos.

PORQUE

II. Imagens de contêiner são construídas a partir de camadas imutáveis.

*a. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
c. As asserções I e II são proposições falsas.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.

**13.** I. O reinício em loop de um Pod pode mascarar um defeito determinístico de código sem resolver sua causa raiz.

PORQUE

II. O laço de reconciliação do Kubernetes é capaz de identificar e corrigir automaticamente a causa raiz de um defeito de código.

a. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*b. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
c. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
d. As asserções I e II são proposições falsas.
e. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.

**14.** I. Segredos, como credenciais de acesso a um provedor de pagamento, devem ser embutidos diretamente na imagem do contêiner para garantir disponibilidade imediata.

PORQUE

II. Objetos do tipo Secret no Kubernetes permitem injetar dados sensíveis em um Pod em tempo de execução, sem alterar a imagem publicada.

a. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. As asserções I e II são proposições falsas.
d. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*e. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.

**15.** I. O Horizontal Pod Autoscaler ajusta o número de réplicas de um Deployment exclusivamente com base no número de eventos publicados em um tópico.

PORQUE

II. Uma atualização gradual (rolling update) substitui todas as réplicas de um serviço simultaneamente, para garantir consistência de versão.

*a. As asserções I e II são proposições falsas.
b. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
c. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
d. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
e. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.

**16.** I. Em um modelo de confiança zero, uma requisição originada dentro da rede interna do cluster não deve ser considerada automaticamente confiável.

PORQUE

II. O modelo de confiança zero exige que cada serviço possua uma identidade verificável e que toda comunicação seja autenticada e autorizada explicitamente, independentemente de sua origem.

a. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
b. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*c. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
d. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
e. As asserções I e II são proposições falsas.

**17.** I. O princípio do menor privilégio recomenda conceder a cada identidade apenas as permissões estritamente necessárias para sua função.

PORQUE

II. Um tópico de eventos pode ser dividido em partições para permitir paralelismo entre consumidores.

*a. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
c. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
d. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
e. As asserções I e II são proposições falsas.

**18.** I. O TLS mútuo exige que tanto o cliente quanto o servidor apresentem certificados válidos antes de estabelecer a comunicação.

PORQUE

II. O TLS mútuo é utilizado exclusivamente para proteger comunicações entre um navegador e um servidor web público, não sendo aplicável à comunicação interna entre serviços.

a. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
b. As asserções I e II são proposições falsas.
c. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*d. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
e. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.

**19.** I. A limitação de taxa por balde de fichas tem como único objetivo impedir o acesso de usuários não autenticados a um serviço.

PORQUE

II. A limitação de taxa por balde de fichas protege um serviço contra sobrecarga, seja ela originada de tráfego legítimo em pico ou de uso indevido.

a. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
b. As asserções I e II são proposições falsas.
*c. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
d. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
e. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.

**20.** I. Um ataque de repetição (*replay*) é impossível de ocorrer em sistemas que utilizam comunicação assíncrona por eventos.

PORQUE

II. Um proxy lateral (*sidecar*) deve ser implementado separadamente dentro do código de cada serviço para que políticas de segurança sejam aplicadas.

a. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
b. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
c. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
d. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*e. As asserções I e II são proposições falsas.

### Bloco 2 — Interpretação (21 a 40)

**21.** A equipe da NexaOrder percebe que todo *deploy* do serviço de pedidos exige, no mesmo horário, um *deploy* coordenado do serviço de estoque, porque os dois serviços leem e escrevem diretamente na mesma tabela de itens. Nenhum dos dois times consegue testar ou implantar de forma isolada.

Qual conceito discutido na Aula 9 explica com mais precisão esse cenário?

a. Balde de fichas — o tráfego entre os dois serviços excede a capacidade configurada.
*b. Monólito distribuído — a separação física não produziu autonomia real porque os serviços compartilham dados e ciclo de implantação.
c. Confiança zero — a comunicação entre pedidos e estoque não está sendo autenticada.
d. Laço de reconciliação — o Kubernetes está tentando restaurar o estado desejado dos dois serviços.
e. Semântica exactly-once — os eventos entre os dois serviços estão sendo processados de forma duplicada.

**22.** Ao calcular a instabilidade I = Ce / (Ca + Ce) de dois serviços da NexaOrder, a equipe obtém: serviço de estoque, com Ca = 3 e Ce = 1, resultando em I = 0,25; serviço de catálogo, com Ca = 1 e Ce = 4, resultando em I = 0,8.

Com base nesses valores, qual afirmação é mais adequada?

a. Ambos os serviços apresentam exatamente o mesmo grau de instabilidade.
b. Quanto maior o valor de I, mais estável é o serviço.
c. O serviço de catálogo é mais estável que o de estoque, pois seu Ce é maior.
*d. O serviço de catálogo é mais instável que o de estoque, pois depende proporcionalmente de mais serviços do que é dependido por eles.
e. A instabilidade calculada determina, sozinha, que o serviço de catálogo deve ser removido da arquitetura.

**23.** A tela de detalhes do pedido no aplicativo da NexaOrder precisa exibir dados de pedidos, estoque e expedição em uma única tela. A equipe decide que o próprio aplicativo fará três chamadas diretas, uma para cada serviço, em vez de utilizar um ponto de entrada único.

Qual é o principal risco dessa decisão, à luz do conceito de API Gateway apresentado na aula?

*a. O aplicativo cliente passa a conhecer a topologia interna dos serviços, aumentando o acoplamento externo e multiplicando autenticação e limite de taxa em cada chamada.
b. Nenhum risco relevante, pois cada serviço já possui seu próprio armazenamento de dados.
c. O aplicativo passará a processar eventos de domínio de forma incorreta.
d. A instabilidade dos três serviços será reduzida automaticamente.
e. O laço de reconciliação do Kubernetes deixará de funcionar corretamente.

**24.** Ao analisar o fluxo de um único caso de uso na NexaOrder, a equipe percebe que a conclusão de uma simples consulta de status de pedido dispara 14 chamadas remotas sequenciais entre cinco serviços diferentes.

O que esse padrão mais provavelmente indica, segundo os critérios apresentados na aula?

a. Que o problema está exclusivamente relacionado à ausência de TLS mútuo.
b. Que os serviços envolvidos possuem baixa instabilidade.
*c. Que a fronteira entre alguns desses serviços provavelmente foi traçada no lugar errado, gerando comunicação excessivamente conversacional.
d. Que a arquitetura atingiu o nível ideal de granularidade de serviços.
e. Que o número de partições do tópico de eventos está subdimensionado.

**25.** Ao adotar o princípio de dados por serviço, a NexaOrder deixa de poder executar um `JOIN` direto entre a tabela de pedidos e a tabela de itens de estoque, que antes pertenciam ao mesmo banco de dados.

Qual é a consequência mais provável e esperada dessa decisão?

a. A obrigatoriedade de fundir os dois serviços em um único banco de dados compartilhado.
*b. A necessidade de obter dados combinados por composição explícita, como chamadas de API ou réplicas assíncronas, ao custo de possível atraso de propagação.
c. A eliminação do conceito de contexto delimitado entre os dois serviços.
d. A garantia de que nenhuma inconsistência temporária poderá ocorrer entre os dois serviços.
e. A eliminação total da necessidade de comunicação entre pedidos e estoque.

**26.** A NexaOrder decide particionar o tópico "eventos-pedido" usando o tipo do evento (`pedido-criado`, `estoque-reservado` ou `pagamento-aprovado`) como chave, em vez do identificador estável do pedido.

Qual é a consequência técnica mais provável dessa escolha, segundo o que foi discutido na Aula 10?

a. O gateway de API passará a compor as respostas dos serviços de forma incorreta.
b. O throughput do tópico aumentará automaticamente, independentemente do número de partições.
*c. Eventos de um mesmo pedido podem cair em partições distintas e ser observados fora de ordem pelo consumidor, pois a chave varia ao longo do fluxo.
d. A semântica de entrega passará automaticamente a ser exactly-once.
e. A retenção de eventos deixará de ser configurável.

**27.** O tópico "eventos-pedido" da NexaOrder possui 8 partições. Um grupo de consumidores responsável por atualizar o painel operacional passa a ter 10 instâncias.

O que ocorre com as duas instâncias excedentes desse grupo?

a. Elas assumem partições do grupo de consumidores responsável pelo envio de e-mails.
b. Elas processam eventos fora de ordem, violando a garantia de ordenação por partição.
c. Elas forçam o tópico a criar automaticamente duas novas partições.
d. Elas processam, cada uma, metade da carga de uma partição já atribuída a outra instância.
*e. Elas permanecem ociosas, pois não há partições disponíveis para atribuir a elas.

**28.** O consumidor responsável por enviar o e-mail de confirmação de pedido na NexaOrder confirma o recebimento do evento antes de efetivamente enviar o e-mail. Uma falha ocorre exatamente entre a confirmação e o envio.

Qual é o resultado mais provável desse desenho, considerando as semânticas de entrega discutidas na aula?

a. O evento será reprocessado automaticamente, garantindo o envio do e-mail sem duplicação.
b. O evento será duplicado indefinidamente até ser reprocessado manualmente.
c. A ordenação de eventos dentro da partição será violada.
*d. O e-mail de confirmação pode não ser enviado, caracterizando um comportamento próximo de at-most-once, já que a confirmação ocorreu antes da conclusão do processamento.
e. O consumidor alcançará automaticamente uma semântica exactly-once.

**29.** Um serviço da NexaOrder renomeia o campo `valor_total` para `valor_liquido` no evento "pedido criado", sem qualquer período de transição, e publica a nova versão diretamente em produção.

Qual é a consequência mais provável para consumidores que ainda não foram atualizados?

a. Nenhuma, pois toda mudança de esquema é automaticamente compatível.
b. A ordenação por partição será automaticamente corrigida.
c. O tópico será automaticamente dividido em mais partições para compensar a mudança.
d. Os consumidores antigos passarão a processar os eventos mais rapidamente.
*e. Consumidores antigos podem rejeitar ou falhar ao desserializar o evento, ou tratar o campo esperado como ausente, conforme o contrato e a implementação, quebrando a compatibilidade.

**30.** A NexaOrder projeta um novo tópico para eventos de rastreamento de expedição, com taxa de pico estimada de 900 eventos por segundo. Cada consumidor sustenta, de forma confiável, 100 eventos por segundo.

Qual é o número mínimo de partições necessário para sustentar esse pico, considerando a fórmula P = ⌈λ_pico / C_consumidor⌉ apresentada na aula?

a. 90 partições.
*b. 9 partições.
c. 6 partições.
d. 7 partições.
e. 8 partições.

**31.** Um Pod do serviço de expedição da NexaOrder é removido manualmente por um engenheiro durante um teste, sem qualquer alteração no manifesto do Deployment correspondente.

O que o Kubernetes deve fazer, considerando o laço de reconciliação discutido na Aula 11?

*a. Criar um novo Pod automaticamente, pois o estado desejado declarado no Deployment ainda especifica o número original de réplicas.
b. Migrar automaticamente o serviço de expedição para um novo cluster.
c. Reduzir permanentemente o número de réplicas declarado no Deployment.
d. Interromper o Service associado até nova configuração manual.
e. Aguardar uma nova solicitação humana antes de qualquer ação.

**32.** O Deployment do serviço de estoque da NexaOrder possui 5 réplicas atuais, utilização média observada de CPU de 90% e utilização alvo configurada de 50%.

Qual o número de réplicas resultante, segundo a fórmula N = ⌈N_atual × U_atual / U_alvo⌉ apresentada na aula?

a. 45 réplicas.
b. 10 réplicas.
c. 4 réplicas.
d. 5 réplicas.
*e. 9 réplicas.

**33.** Um Pod do serviço de pagamento da NexaOrder é recriado pelo Kubernetes repetidamente, a cada poucos minutos, sempre travando sob o mesmo padrão de carga.

Qual é a interpretação mais adequada desse cenário, à luz do que foi discutido na aula?

a. O Service associado deixará de rotear tráfego para esse Deployment.
b. A imagem do contêiner deixou de ser imutável.
*c. A recriação automática mantém a disponibilidade aparente do serviço, mas provavelmente mascara um defeito recorrente que exige diagnóstico humano.
d. O problema está definitivamente resolvido, pois o serviço volta a responder após cada recriação.
e. O laço de reconciliação identificou e corrigiu a causa raiz do defeito.

**34.** Um novo integrante da equipe sugere embutir a credencial do provedor de pagamento diretamente na imagem do contêiner do serviço de pagamento, para simplificar a implantação.

Por que essa prática é desaconselhada, segundo os conceitos discutidos na aula?

*a. Porque credenciais embutidas na imagem ficam expostas a qualquer pessoa com acesso a ela e exigem nova publicação da imagem a cada rotação de credencial, ao contrário de um Secret injetado em tempo de execução.
b. Porque isso tornaria o serviço automaticamente instável, segundo a métrica I = Ce/(Ca+Ce).
c. Porque isso impediria o laço de reconciliação de funcionar corretamente.
d. Porque o Kubernetes rejeita automaticamente imagens que contenham qualquer variável de ambiente.
e. Porque imagens de contêiner não podem conter nenhum tipo de arquivo de configuração.

**35.** A NexaOrder publica a versão 1.8.0 do serviço de pagamento e configura uma atualização gradual (*rolling update*) com limites que impedem a redução da capacidade total abaixo do necessário.

Qual é o comportamento esperado durante essa atualização?

a. O Service associado interrompe o roteamento de tráfego até a conclusão completa da atualização.
b. Todas as réplicas da versão 1.7.0 são removidas simultaneamente antes de qualquer réplica da versão 1.8.0 ser criada.
c. Todas as réplicas da versão 1.8.0 são criadas de uma só vez, sem qualquer controle de disponibilidade.
*d. Réplicas antigas são substituídas por novas de forma incremental, mantendo o total de réplicas saudáveis dentro dos limites configurados.
e. A atualização exige que o número de partições do tópico de eventos seja recalculado.

**36.** Um invasor obtém acesso a um Pod de baixo privilégio dentro do cluster da NexaOrder e tenta, a partir dele, estabelecer conexão direta com o serviço de pagamento.

Em uma arquitetura corretamente configurada com confiança zero, TLS mútuo e autorização de menor privilégio, o que deveria ocorrer?

a. O laço de reconciliação impediria automaticamente a existência do Pod comprometido.
b. A instabilidade do serviço de pagamento aumentaria, impedindo qualquer conexão.
c. O balde de fichas do serviço de pagamento aumentaria automaticamente sua capacidade para atender à nova conexão.
d. A conexão deveria ser aceita automaticamente, pois ambos estão na mesma rede interna do cluster.
*e. O certificado autentica a identidade do Pod, mas a política de autorização deve recusar a operação porque essa identidade não tem permissão para acessar o pagamento.

**37.** Por engano, a identidade de serviço "expedição" da NexaOrder recebe permissão para solicitar reembolsos ao serviço de pagamento, além de suas permissões originais de consulta e confirmação de envio.

Qual princípio discutido na aula está sendo violado?

a. Limitação de taxa, pois o balde de fichas do serviço de pagamento foi mal configurado.
b. Confiança zero, pois toda comunicação interna deveria ser proibida.
*c. Menor privilégio, pois a identidade "expedição" recebeu permissão além do estritamente necessário para sua função.
d. Reconciliação, pois o estado desejado do Deployment não corresponde ao estado observado.
e. Evolução de esquema, pois o formato do evento de pagamento foi alterado sem compatibilidade.

**38.** O serviço de pagamento da NexaOrder configura um balde de fichas com capacidade de 40 fichas e taxa de reposição de 15 fichas por segundo. O balde está cheio no início do intervalo, quando uma rajada de 60 requisições chega de uma só vez.

Quantas dessas requisições são atendidas imediatamente, considerando apenas a capacidade do balde?

*a. 40 requisições, correspondentes à capacidade do balde; as demais serão recusadas ou atrasadas até a reposição de novas fichas.
b. 15 requisições, correspondentes à taxa de reposição sustentável em regime permanente.
c. 60 requisições, pois o balde absorve toda a rajada instantaneamente.
d. 25 requisições, referentes à diferença entre a rajada e a capacidade do balde.
e. 0 requisições, pois qualquer rajada acima da taxa de reposição é integralmente recusada.

**39.** Um invasor captura uma mensagem legítima de autorização de pagamento da NexaOrder e a reenvia horas depois, tentando produzir uma nova cobrança sobre o mesmo pedido.

Qual mecanismo, discutido na aula, mitiga diretamente esse tipo de ataque?

a. Escalonamento automático horizontal baseado em utilização de CPU.
b. Retenção estendida de eventos em um tópico.
*c. Identificador único de operação associado a uma janela de validade, permitindo que o serviço de pagamento rejeite repetições indevidas.
d. Composição de respostas por um API Gateway.
e. Aumento do número de partições do tópico de eventos.

**40.** Em vez de implementar autenticação mútua e limite de taxa dentro do código de cada um dos quatro serviços da NexaOrder, a equipe de plataforma decide implantar um proxy lateral junto a cada serviço, coordenado por um plano de controle central.

Qual conceito discutido na aula essa decisão representa?

a. Confiança zero aplicada exclusivamente à borda externa do sistema.
*b. Adoção de um *service mesh*, que centraliza políticas de segurança e comunicação sem replicá-las no código de cada serviço individualmente.
c. Substituição do laço de reconciliação por um mecanismo de autenticação.
d. Eliminação da necessidade de gestão de segredos.
e. Redução da instabilidade dos serviços, segundo a métrica I = Ce/(Ca+Ce).

## Gabarito e feedbacks

**Questão 1** (correta: b)
- a. Incorreta. A I é verdadeira, não falsa: a experiência da NexaOrder confirma que dividir fisicamente não basta.
- b. Correta. As duas asserções são verdadeiras: a separação física realmente não garante autonomia, e o compartilhamento de esquema de dados é exatamente o mecanismo que explica por que essa autonomia não se concretiza.
- c. Incorreta. Ambas as asserções são verdadeiras, não falsas.
- d. Incorreta. A II não é apenas verdadeira e desconexa: ela justifica diretamente a I, ao explicar o mecanismo pelo qual a separação física não produz autonomia.
- e. Incorreta. A II também é verdadeira, não falsa: esquema compartilhado de fato exige coordenação de mudanças.

**Questão 2** (correta: a)
- a. Correta. Ambas as afirmações são verdadeiras isoladamente, mas tratam de assuntos distintos: uma fala de modelagem de domínio, a outra de um protocolo de comunicação. A II não justifica a I.
- b. Incorreta. A II também é verdadeira: o HTTP de fato permite comunicação síncrona com GET e POST.
- c. Incorreta. Ambas as asserções são verdadeiras.
- d. Incorreta. A I é verdadeira: contexto delimitado é exatamente o critério discutido na aula para desenhar fronteiras.
- e. Incorreta. A II é verdadeira, mas não justifica a I: o fato de o HTTP permitir chamadas síncronas não explica por que contexto delimitado orienta fronteiras de serviço.

**Questão 3** (correta: d)
- a. Incorreta. A I é verdadeira; apenas a II é falsa.
- b. Incorreta. A I é verdadeira, não falsa.
- c. Incorreta. A II é falsa, não verdadeira: monólito modular, por definição, mantém uma única unidade de implantação.
- d. Correta. A I descreve corretamente o monólito modular; a II o contradiz, pois afirma implantação totalmente independente dos módulos, o que descaracterizaria a própria definição de monólito.
- e. Incorreta. A II é falsa, não apenas desconexa da I.

**Questão 4** (correta: e)
- a. Incorreta. A I é falsa, e a questão não trata de asserções ambas verdadeiras.
- b. Incorreta. A II é verdadeira, não falsa.
- c. Incorreta. A I é falsa, não verdadeira.
- d. Incorreta. A I é falsa: um gateway não deve concentrar regras de negócio.
- e. Correta. A I contraria o que foi ensinado na aula — o gateway não deve acumular regras de negócio — enquanto a II descreve corretamente o risco de isso acontecer.

**Questão 5** (correta: d)
- a. Incorreta. Nenhuma das duas asserções é verdadeira da forma como está enunciada.
- b. Incorreta. Ambas as asserções são falsas, não verdadeiras.
- c. Incorreta. A II também é falsa: alta instabilidade não implica necessariamente fusão de serviços.
- d. Correta. A métrica de instabilidade é um heurístico de apoio à discussão, não uma regra definitiva de decisão; e alta instabilidade não determina automaticamente a fusão de serviços.
- e. Incorreta. A I também é falsa: a métrica é um heurístico de apoio, não um critério definitivo e objetivo isolado.

**Questão 6** (correta: b)
- a. Incorreta. A II justifica sim a I, não é uma relação apenas coincidente.
- b. Correta. Ambas as afirmações são verdadeiras, e a II explica diretamente por que a I é verdadeira: eventos sem destinatário específico permitem que o produtor não precise conhecer os consumidores.
- c. Incorreta. Ambas são verdadeiras.
- d. Incorreta. A I é verdadeira, não falsa.
- e. Incorreta. A II também é verdadeira.

**Questão 7** (correta: d)
- a. Incorreta. Ambas são verdadeiras.
- b. Incorreta. A II também é verdadeira.
- c. Incorreta. A II não justifica a I: TLS mútuo trata de identidade em comunicação, não de ordenação de eventos.
- d. Correta. Ambas as afirmações são verdadeiras isoladamente, mas tratam de temas distintos — leitura por ordem de offset na partição e verificação de identidade — sem relação de justificativa entre si.
- e. Incorreta. A I é verdadeira, não falsa.

**Questão 8** (correta: e)
- a. Incorreta. A II é falsa: at-least-once não impede duplicação, pelo contrário, ela é a característica central dessa semântica.
- b. Incorreta. A I é verdadeira, não falsa.
- c. Incorreta. A I é verdadeira; apenas a II é falsa.
- d. Incorreta. A II é falsa, não apenas desconexa.
- e. Correta. A I explicita o escopo operacional de *at-least-once* e a possibilidade de duplicação; a II é falsa porque essa semântica não impede reprocessamento.

**Questão 9** (correta: b)
- a. Incorreta. A II é verdadeira, não falsa.
- b. Correta. A I contraria o que foi ensinado: adicionar consumidores além do número de partições não aumenta throughput. A II descreve corretamente a razão para esse limite.
- c. Incorreta. A I é falsa: consumidores extras além do número de partições não aumentam throughput.
- d. Incorreta. A I é falsa, então a relação de asserções ambas verdadeiras não se aplica.
- e. Incorreta. A I é falsa, não verdadeira.

**Questão 10** (correta: d)
- a. Incorreta. A II também é falsa: alterar o tipo de um campo costuma quebrar compatibilidade.
- b. Incorreta. Nenhuma das duas é verdadeira.
- c. Incorreta. A I também é falsa: a retenção é configurável e frequentemente estendida por horas ou dias, viabilizando reprocessamento.
- d. Correta. A retenção de eventos é configurável e tipicamente mais longa do que poucos segundos, viabilizando reprocessamento; e alterar o tipo de um campo existente costuma ser uma mudança insegura, não uma mudança automaticamente compatível.
- e. Incorreta. Ambas são falsas, não verdadeiras.

**Questão 11** (correta: c)
- a. Incorreta. A II também é verdadeira.
- b. Incorreta. A II justifica diretamente a I; não é uma coincidência de duas verdades desconexas.
- c. Correta. Ambas as afirmações são verdadeiras, e a II explica exatamente o mecanismo — o laço de reconciliação — que produz o comportamento descrito na I.
- d. Incorreta. Ambas são verdadeiras.
- e. Incorreta. A I é verdadeira, não falsa.

**Questão 12** (correta: a)
- a. Correta. Ambas as afirmações são verdadeiras isoladamente, mas tratam de conceitos distintos do Kubernetes, sem relação de causa entre si.
- b. Incorreta. A II não justifica a I: imutabilidade de imagens não explica por que um Service mantém endereço estável.
- c. Incorreta. Ambas são verdadeiras.
- d. Incorreta. A I é verdadeira, não falsa.
- e. Incorreta. A II também é verdadeira.

**Questão 13** (correta: b)
- a. Incorreta. A II é falsa, não apenas desconexa.
- b. Correta. A I descreve corretamente o risco do reinício em loop; a II o contradiz, atribuindo ao laço de reconciliação uma capacidade de diagnóstico que ele não possui.
- c. Incorreta. A II é falsa: o laço de reconciliação não identifica nem corrige causas de código, apenas restaura quantidade e execução declaradas.
- d. Incorreta. A I é verdadeira; apenas a II é falsa.
- e. Incorreta. A I é verdadeira, não falsa.

**Questão 14** (correta: e)
- a. Incorreta. A I é falsa, não verdadeira.
- b. Incorreta. A I é falsa, não verdadeira.
- c. Incorreta. A II é verdadeira, não falsa.
- d. Incorreta. A I é falsa: embutir segredos na imagem é uma prática desaconselhada, não recomendada.
- e. Correta. A I contraria a prática recomendada apresentada na aula; a II descreve corretamente o mecanismo do Kubernetes para gestão segura de segredos.

**Questão 15** (correta: a)
- a. Correta. O Horizontal Pod Autoscaler pode usar métricas de recursos, customizadas ou externas, conforme a configuração; portanto, não depende exclusivamente do número de eventos publicados. A atualização gradual substitui réplicas de forma incremental, não simultânea.
- b. Incorreta. Nenhuma das duas é verdadeira.
- c. Incorreta. A II também é falsa: rolling update substitui réplicas de forma incremental, não simultânea.
- d. Incorreta. A I também é falsa: o HPA pode usar métricas de recursos e, quando configurado, métricas customizadas ou externas; não ajusta réplicas exclusivamente pelo número de eventos publicados em um tópico.
- e. Incorreta. Ambas são falsas, não verdadeiras.

**Questão 16** (correta: c)
- a. Incorreta. A I é verdadeira, não falsa.
- b. Incorreta. A II também é verdadeira.
- c. Correta. Ambas as afirmações são verdadeiras, e a II descreve exatamente a exigência do modelo de confiança zero que justifica por que a origem interna não deve ser considerada automaticamente confiável.
- d. Incorreta. A II justifica diretamente a I.
- e. Incorreta. Ambas são verdadeiras.

**Questão 17** (correta: a)
- a. Correta. Ambas as afirmações são verdadeiras isoladamente, mas tratam de temas distintos — segurança e mensageria — sem relação de justificativa entre si.
- b. Incorreta. A II não justifica a I: partições de tópico não têm relação com o princípio do menor privilégio.
- c. Incorreta. A I é verdadeira, não falsa.
- d. Incorreta. A II também é verdadeira.
- e. Incorreta. Ambas são verdadeiras.

**Questão 18** (correta: d)
- a. Incorreta. A II é falsa, não apenas desconexa.
- b. Incorreta. A I é verdadeira; apenas a II é falsa.
- c. Incorreta. A II é falsa: TLS mútuo é amplamente aplicado à comunicação interna entre serviços, não apenas a navegadores.
- d. Correta. A I descreve corretamente o funcionamento do TLS mútuo; a II o contradiz ao restringir indevidamente seu uso.
- e. Incorreta. A I é verdadeira, não falsa.

**Questão 19** (correta: c)
- a. Incorreta. A I é falsa, não verdadeira.
- b. Incorreta. A II é verdadeira, não falsa.
- c. Correta. A I restringe indevidamente o propósito da limitação de taxa; a II descreve corretamente seu objetivo, que inclui tráfego legítimo em pico e uso indevido.
- d. Incorreta. A I é falsa: a limitação de taxa protege contra sobrecarga, não é um mecanismo de autenticação.
- e. Incorreta. A I é falsa, não verdadeira.

**Questão 20** (correta: e)
- a. Incorreta. A II também é falsa: o proxy lateral existe justamente para evitar reimplementar políticas de segurança no código de cada serviço.
- b. Incorreta. A I também é falsa: ataques de repetição podem ocorrer mesmo em comunicação assíncrona por eventos, se não houver deduplicação.
- c. Incorreta. Ambas são falsas, não verdadeiras.
- d. Incorreta. Nenhuma das duas é verdadeira.
- e. Correta. Ataques de repetição não são exclusivos de comunicação síncrona e podem afetar eventos sem deduplicação adequada; e o proxy lateral tem como propósito justamente centralizar políticas de segurança fora do código de cada serviço.

**Questão 21** (correta: b)
- a. Incorreta. Não há menção a limitação de taxa ou sobrecarga de tráfego no cenário.
- b. Correta. O cenário descreve exatamente os sintomas de um monólito distribuído: separação física sem autonomia real de dados ou implantação.
- c. Incorreta. O cenário não menciona ausência de autenticação entre os serviços.
- d. Incorreta. O laço de reconciliação é um mecanismo do Kubernetes, não relacionado ao acoplamento de dados descrito.
- e. Incorreta. Não há menção a processamento de eventos duplicados no cenário.

**Questão 22** (correta: d)
- a. Incorreta. Os valores calculados (0,25 e 0,8) são diferentes.
- b. Incorreta. É o oposto: quanto maior o valor de I, mais instável — não mais estável — é o serviço.
- c. Incorreta. A afirmação inverte o significado da métrica: Ce alto contribui para maior instabilidade, não maior estabilidade.
- d. Correta. Um valor de I mais próximo de 1 indica maior instabilidade; o catálogo, com I = 0,8, depende proporcionalmente mais de outros serviços do que é dependido por eles.
- e. Incorreta. A métrica é um heurístico de apoio, não uma regra definitiva de remoção de serviços.

**Questão 23** (correta: a)
- a. Correta. Sem um gateway, o cliente precisa conhecer e chamar diretamente cada serviço, aumentando o acoplamento externo e replicando preocupações transversais como autenticação e limite de taxa.
- b. Incorreta. Há risco relevante: o acoplamento entre cliente e topologia interna, independentemente de cada serviço ter seu próprio armazenamento.
- c. Incorreta. O cenário não envolve processamento de eventos de domínio.
- d. Incorreta. A decisão descrita não afeta a instabilidade estrutural dos serviços.
- e. Incorreta. O cenário não tem relação com o laço de reconciliação do Kubernetes.

**Questão 24** (correta: c)
- a. Incorreta. TLS mútuo trata de segurança da comunicação, não do número de chamadas exigidas para um caso de uso.
- b. Incorreta. O cenário não fornece dados sobre acoplamento aferente e eferente para essa conclusão.
- c. Correta. Comunicação excessivamente conversacional para um único caso de uso é um sintoma clássico de fronteiras de serviço mal desenhadas.
- d. Incorreta. Uma cadeia de 14 chamadas para uma simples consulta é sinal de problema, não de granularidade ideal.
- e. Incorreta. O cenário descreve chamadas síncronas entre serviços, não consumo de um tópico de eventos.

**Questão 25** (correta: b)
- a. Incorreta. A decisão de dados por serviço é o oposto de fundir bancos de dados.
- b. Correta. Sem `JOIN` direto, dados de serviços diferentes precisam ser combinados por composição explícita — chamada de API ou réplica assíncrona —, o que pode introduzir atraso de propagação.
- c. Incorreta. O contexto delimitado continua existindo e é, inclusive, o que justifica a separação de dados.
- d. Incorreta. Dados por serviço não elimina a possibilidade de inconsistência temporária; ao contrário, costuma introduzi-la.
- e. Incorreta. A comunicação entre pedidos e estoque continua necessária; apenas muda de forma.

**Questão 26** (correta: c)
- a. Incorreta. O cenário não envolve um API Gateway.
- b. Incorreta. O throughput depende do número de partições e consumidores, não da escolha específica da chave.
- c. Correta. Usar uma chave que muda conforme o tipo de evento quebra a afinidade do pedido com uma única partição e permite observação fora de ordem.
- d. Incorreta. A semântica de entrega depende do desenho do produtor e consumidor, não da chave escolhida.
- e. Incorreta. A retenção é uma configuração independente da chave de particionamento.

**Questão 27** (correta: e)
- a. Incorreta. Grupos de consumidores diferentes são independentes; um grupo não assume partições de outro grupo.
- b. Incorreta. A ordenação dentro de cada partição continua garantida, independentemente do número de instâncias ociosas.
- c. Incorreta. O número de partições de um tópico não é ajustado automaticamente pelo número de instâncias de um grupo.
- d. Incorreta. Uma instância não compartilha o processamento de uma partição já atribuída a outra instância do mesmo grupo.
- e. Correta. Como cada partição só pode ser atribuída a uma instância por vez, e há apenas 8 partições para 10 instâncias, duas instâncias ficam sem partição atribuída e permanecem ociosas.

**Questão 28** (correta: d)
- a. Incorreta. Não há reprocessamento automático garantido nesse desenho, já que a confirmação já ocorreu antes da falha.
- b. Incorreta. Não há indício de reentrega nesse desenho, já que o evento já foi confirmado.
- c. Incorreta. O cenário não descreve um problema de ordenação dentro da partição.
- d. Correta. Como a confirmação ocorre antes da conclusão do processamento, uma falha nesse intervalo pode levar à perda do efeito (o e-mail não enviado), sem nova tentativa — comportamento típico de at-most-once.
- e. Incorreta. Esse desenho não garante exactly-once; ao contrário, arrisca perda de efeito.

**Questão 29** (correta: e)
- a. Incorreta. Renomear um campo sem transição costuma ser uma mudança insegura, não automaticamente compatível.
- b. Incorreta. O cenário não envolve ordenação por partição.
- c. Incorreta. O número de partições não é ajustado automaticamente por mudanças de esquema.
- d. Incorreta. A velocidade de processamento não é afetada por essa mudança de esquema.
- e. Correta. Consumidores antigos esperam `valor_total`; sem uma transição compatível, podem rejeitar/falhar ao desserializar o evento ou aplicar seu comportamento para campo ausente. O efeito exato depende do contrato e da implementação, mas a compatibilidade foi quebrada.

**Questão 30** (correta: b)
- a. Incorreta. 90 partições excede em muito o resultado da fórmula aplicada aos valores do enunciado.
- b. Correta. P = ⌈900 / 100⌉ = ⌈9⌉ = 9 partições.
- c. Incorreta. 900 dividido por 100 resulta em 9, não em 6.
- d. Incorreta. O cálculo correto não resulta em 7.
- e. Incorreta. O cálculo correto não resulta em 8.

**Questão 31** (correta: a)
- a. Correta. O manifesto do Deployment ainda declara o número original de réplicas; o laço de reconciliação detecta a divergência e cria um novo Pod para restaurar o estado desejado.
- b. Incorreta. O cenário não envolve migração de cluster.
- c. Incorreta. A remoção manual de um Pod não altera o manifesto do Deployment nem reduz permanentemente o número declarado de réplicas.
- d. Incorreta. O Service continua roteando tráfego para os Pods saudáveis remanescentes e para o novo Pod criado.
- e. Incorreta. O laço de reconciliação age de forma autônoma e contínua, sem esperar nova solicitação humana para restaurar o estado desejado.

**Questão 32** (correta: e)
- a. Incorreta. 45 corresponde ao produto 5 × 90 sem a divisão pelo alvo, o que não representa a fórmula correta.
- b. Incorreta. O resultado do cálculo é 9, não 10.
- c. Incorreta. O resultado indica aumento de réplicas, não redução.
- d. Incorreta. O cálculo não mantém o número de réplicas inalterado, já que a utilização está muito acima do alvo.
- e. Correta. N = ⌈5 × 90 / 50⌉ = ⌈9,0⌉ = 9 réplicas.

**Questão 33** (correta: c)
- a. Incorreta. O Service continua roteando tráfego normalmente enquanto houver Pods, mesmo que estejam sendo recriados repetidamente.
- b. Incorreta. A imutabilidade da imagem não é afetada pelo padrão de reinício.
- c. Correta. A disponibilidade aparente é mantida pela recriação automática, mas o padrão recorrente sob a mesma carga sugere um defeito determinístico que precisa de investigação humana.
- d. Incorreta. A recriação repetida sob o mesmo padrão de carga indica que o problema não está resolvido, apenas mascarado temporariamente.
- e. Incorreta. O laço de reconciliação não diagnostica nem corrige causas de código; ele apenas restaura quantidade e execução declaradas.

**Questão 34** (correta: a)
- a. Correta. Credenciais embutidas na imagem ficam expostas a qualquer pessoa com acesso a ela e exigem republicação a cada rotação, ao contrário de um Secret injetado dinamicamente em tempo de execução.
- b. Incorreta. A prática descrita não tem relação direta com a métrica de instabilidade discutida na Aula 9.
- c. Incorreta. Embutir credenciais na imagem não impede o funcionamento do laço de reconciliação.
- d. Incorreta. O Kubernetes não rejeita automaticamente imagens com variáveis de ambiente.
- e. Incorreta. Imagens de contêiner podem conter arquivos de configuração; o problema é especificamente embutir segredos sensíveis nelas.

**Questão 35** (correta: d)
- a. Incorreta. O Service continua roteando tráfego durante toda a atualização gradual, exceto para réplicas momentaneamente indisponíveis.
- b. Incorreta. A remoção simultânea de todas as réplicas antigas antes de criar novas contraria o propósito de uma atualização gradual.
- c. Incorreta. Criar todas as réplicas novas de uma vez, sem controle, contraria o propósito de limitar indisponibilidade e excedente durante a transição.
- d. Correta. A atualização gradual substitui réplicas antigas por novas de forma incremental, respeitando limites que preservam a capacidade saudável do serviço.
- e. Incorreta. A atualização de versão de um serviço não exige recálculo do número de partições de um tópico de eventos.

**Questão 36** (correta: e)
- a. Incorreta. O laço de reconciliação não tem relação com a prevenção de comprometimento de segurança de um Pod.
- b. Incorreta. A instabilidade estrutural do serviço não é afetada por uma tentativa de conexão não autorizada.
- c. Incorreta. O balde de fichas não se ajusta automaticamente para atender a uma nova conexão não autorizada.
- d. Incorreta. Aceitar a conexão apenas por estar na mesma rede interna é exatamente o modelo de perímetro que a confiança zero rejeita.
- e. Correta. O mTLS autentica a identidade; uma política de autorização separada verifica o menor privilégio e recusa à identidade comprometida a operação sobre pagamento.

**Questão 37** (correta: c)
- a. Incorreta. O cenário não envolve volume de requisições nem configuração de balde de fichas.
- b. Incorreta. Confiança zero não proíbe toda comunicação interna; ela exige autenticação e autorização explícitas para cada comunicação permitida.
- c. Correta. Conceder à identidade "expedição" uma permissão além de suas necessidades funcionais viola diretamente o princípio do menor privilégio.
- d. Incorreta. O cenário não descreve divergência entre estado desejado e observado de um Deployment.
- e. Incorreta. O cenário não envolve alteração de formato de evento.

**Questão 38** (correta: a)
- a. Correta. Como o enunciado informa que o balde começa cheio, suas 40 fichas atendem imediatamente 40 requisições; as 20 restantes são recusadas ou atrasadas.
- b. Incorreta. 15 é a taxa de reposição sustentável em regime permanente, não o número de requisições atendidas imediatamente pela capacidade do balde.
- c. Incorreta. O balde não absorve toda a rajada, pois sua capacidade é de apenas 40 fichas.
- d. Incorreta. O número de requisições atendidas corresponde à capacidade do balde (40), não à diferença entre rajada e capacidade.
- e. Incorreta. O balde atende requisições até o limite de sua capacidade, não recusa integralmente a rajada.

**Questão 39** (correta: c)
- a. Incorreta. O escalonamento automático trata de capacidade computacional, não de mitigação de repetição de mensagens.
- b. Incorreta. A retenção de eventos permite reprocessamento legítimo, mas não mitiga diretamente o reenvio malicioso de uma mensagem específica.
- c. Correta. Um identificador único de operação, combinado a uma janela de validade, permite que o serviço de pagamento reconheça e rejeite uma mensagem já processada ou fora do prazo.
- d. Incorreta. A composição de respostas por um gateway não impede o reenvio de uma mensagem capturada.
- e. Incorreta. O número de partições de um tópico não tem relação com a mitigação de ataques de repetição.

**Questão 40** (correta: b)
- a. Incorreta. O cenário descreve proteção da comunicação interna entre serviços, não exclusivamente da borda externa.
- b. Correta. Coordenar proxies laterais por um plano de controle central, aplicando políticas de segurança e comunicação sem replicá-las no código de cada serviço, é a definição de service mesh apresentada na aula.
- c. Incorreta. O proxy lateral não substitui o laço de reconciliação, que é um mecanismo distinto do Kubernetes.
- d. Incorreta. A gestão de segredos continua necessária mesmo com um service mesh; os proxies laterais frequentemente dependem dela para obter certificados.
- e. Incorreta. A decisão descrita não altera a métrica estrutural de instabilidade dos serviços.
