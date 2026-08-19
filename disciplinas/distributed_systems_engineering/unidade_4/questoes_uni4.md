# Questionário — Unidade 4

Quantidade obrigatória: 40 questões.  
Distribuição: questões 1 a 20 de asserção-razão; questões 21 a 40 de interpretação.  
Cinco alternativas por questão (a. a e.), alternativa correta marcada com `*`, feedback específico para cada alternativa.

## Questões

### Asserção-razão (questões 1 a 20)

**1.** I. Monitoramento tradicional, baseado em painéis e alertas para condições previamente conhecidas, é insuficiente para diagnosticar falhas inéditas em um sistema como a NexaOrder.

PORQUE

II. A observabilidade permite formular perguntas não antecipadas sobre o comportamento interno do sistema a partir de métricas, logs e traces coletados, sem exigir a criação prévia de um painel específico para cada tipo de falha.

a. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*b. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
c. As asserções I e II são proposições falsas.
d. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
e. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.

**2.** I. Métricas, logs e traces são pilares complementares da observabilidade, cada um oferecendo uma perspectiva distinta sobre o comportamento do sistema.

PORQUE

II. As métricas são séries numéricas agregadas ao longo do tempo, adequadas para detectar tendências e disparar alertas.

a. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
b. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*c. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
d. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
e. As asserções I e II são proposições falsas.

**3.** I. Em uma arquitetura de microsserviços como a da NexaOrder, um identificador de correlação (trace ID) propagado entre serviços permite reconstruir o caminho completo de uma requisição.

PORQUE

II. A propagação do contexto de rastreamento ocorre automaticamente em qualquer chamada de rede, independentemente de instrumentação, pois faz parte do protocolo TCP/IP.

a. As asserções I e II são proposições falsas.
b. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
c. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
d. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*e. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.

**4.** I. O indicador de nível de serviço (SLI) é definido pela equipe de negócio como uma meta aspiracional para a experiência do cliente, enquanto o objetivo de nível de serviço (SLO) é uma medição bruta e não normalizada do comportamento do sistema.

PORQUE

II. O SLI é uma medida quantitativa do comportamento observado do serviço, como a proporção de requisições bem-sucedidas, e o SLO é a meta definida para esse indicador ao longo de um período.

a. As asserções I e II são proposições falsas.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.

**5.** I. O orçamento de erro de um serviço aumenta automaticamente sempre que uma nova funcionalidade é implantada, independentemente do comportamento observado em produção.

PORQUE

II. A taxa de consumo do orçamento de erro (*burn rate*) é irrelevante para decisões operacionais, pois o único critério válido é o valor absoluto do SLO definido.

*a. As asserções I e II são proposições falsas.
b. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
c. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
d. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
e. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.

**6.** I. Em sistemas distribuídos, a pirâmide de testes recomenda uma base ampla de testes unitários e de contrato, com menor volume de testes de ponta a ponta.

PORQUE

II. Testes de ponta a ponta que atravessam múltiplos serviços reais tendem a ser mais lentos, mais frágeis e mais caros de manter do que testes unitários e de contrato isolados.

a. As asserções I e II são proposições falsas.
b. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*c. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
d. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
e. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.

**7.** I. Um teste de contrato entre o serviço de pedidos e o serviço de estoque verifica se ambos concordam com o formato e o significado das mensagens trocadas, sem exigir que os dois serviços estejam em execução simultânea.

PORQUE

II. Testes de contrato são normalmente definidos e mantidos em conjunto pelas equipes consumidora e provedora do serviço, reduzindo o risco de quebras não percebidas em produção.

*a. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
b. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
c. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
d. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
e. As asserções I e II são proposições falsas.

**8.** I. Um experimento de caos bem projetado começa pela definição de uma hipótese de estado estável, isto é, uma expectativa mensurável do comportamento normal do sistema antes da falha injetada.

PORQUE

II. A hipótese de estado estável dispensa a coleta de métricas antes do experimento, pois seu único objetivo é observar o comportamento do sistema durante a falha.

a. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. As asserções I e II são proposições falsas.
*d. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
e. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.

**9.** I. O raio de impacto (blast radius) de um experimento de caos deve ser maximizado desde a primeira execução, para que a equipe obtenha o máximo de dados possível sobre o comportamento do sistema.

PORQUE

II. Limitar o raio de impacto de um experimento de caos, por exemplo restringindo-o a uma pequena fração do tráfego ou a um ambiente de testes, reduz o risco de causar uma indisponibilidade real para os clientes.

a. As asserções I e II são proposições falsas.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
d. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*e. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.

**10.** I. A cultura de postmortem sem culpa (blameless postmortem) tem como objetivo identificar e punir o indivíduo responsável pela falha, para reduzir a recorrência de erros semelhantes.

PORQUE

II. Registros de incidentes anteriores não devem influenciar o planejamento de novos experimentos de caos, pois cada falha é um evento estatisticamente independente das demais.

*a. As asserções I e II são proposições falsas.
b. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
c. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.

**11.** I. O processamento em fluxo (streaming) permite que a NexaOrder avalie sinais de fraude à medida que os eventos de pedido chegam, em vez de esperar a formação de um lote completo.

PORQUE

II. Diferentemente do processamento em lote, o processamento em fluxo opera sobre um conjunto de dados potencialmente ilimitado, processando cada evento ou pequenos grupos de eventos assim que se tornam disponíveis.

a. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
b. As asserções I e II são proposições falsas.
*c. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.

**12.** I. No modelo MapReduce, a fase de embaralhamento (shuffle) redistribui os pares intermediários entre os nós, agrupando-os pelas chaves antes da fase de redução.

PORQUE

II. O MapReduce foi originalmente descrito por Dean e Ghemawat como um modelo de programação para processamento paralelo de grandes volumes de dados em clusters.

a. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
b. As asserções I e II são proposições falsas.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
e. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.

**13.** I. Em processamento de fluxo, o tempo de evento (event time) corresponde ao instante em que o evento efetivamente ocorreu no domínio de negócio, podendo diferir do tempo de processamento no cluster.

PORQUE

II. Eventos que chegam fora de ordem ou atrasados nunca podem ser corretamente atribuídos a uma janela de tempo de evento, tornando o conceito de janela inútil na prática.

a. As asserções I e II são proposições falsas.
*b. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
c. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.

**14.** I. Uma função como serviço (FaaS) mantém sempre uma instância "quente" disponível, eliminando qualquer latência adicional na primeira execução após um período de ociosidade.

PORQUE

II. Quando uma função como serviço não possui instância ociosa disponível, a plataforma precisa inicializar um novo ambiente de execução antes de processar a requisição, fenômeno conhecido como inicialização a frio (cold start).

a. As asserções I e II são proposições falsas.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
d. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*e. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.

**15.** I. A computação de borda elimina totalmente a necessidade de qualquer comunicação com uma região central de nuvem, pois todo o processamento passa a ocorrer exclusivamente no dispositivo do usuário.

PORQUE

II. O compromisso entre custo e latência na computação de borda favorece sempre o processamento na borda, independentemente do volume de dados ou da complexidade do processamento exigido.

*a. As asserções I e II são proposições falsas.
b. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
e. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.

**16.** I. Atributos de qualidade como desempenho, disponibilidade, segurança e capacidade de manutenção também influenciam decisivamente a arquitetura da NexaOrder, ao lado dos requisitos funcionais explícitos.

PORQUE

II. Um requisito funcional descreve o que o sistema deve fazer, enquanto um atributo de qualidade descreve como o sistema deve se comportar sob determinadas condições, e frequentemente exige decisões arquiteturais específicas para ser satisfeito.

a. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
c. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
d. As asserções I e II são proposições falsas.
e. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.

**17.** I. Um registro de decisão arquitetural (ADR) documenta o contexto, a decisão tomada e as consequências previstas de uma escolha significativa de arquitetura, permitindo que decisões futuras sejam avaliadas à luz do que já foi decidido.

PORQUE

II. Ferramentas de controle de versão permitem armazenar arquivos de ADR junto ao código-fonte, possibilitando o rastreamento do histórico de decisões ao longo do tempo.

a. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
b. As asserções I e II são proposições falsas.
c. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.

**18.** I. A análise de pontos únicos de falha (SPOF) da NexaOrder deve identificar componentes cuja indisponibilidade isolada comprometeria todo o fluxo de pedidos, mesmo que o restante do sistema esteja saudável.

PORQUE

II. Um componente redundante, com múltiplas réplicas ativas, nunca pode se tornar parte de um ponto único de falha, independentemente de como as réplicas estão distribuídas fisicamente ou de quais dependências compartilham.

a. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
b. As asserções I e II são proposições falsas.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
e. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.

**19.** I. O objetivo de tempo de recuperação (RTO) mede a quantidade máxima de dados que o negócio aceita perder em uma falha, enquanto o objetivo de ponto de recuperação (RPO) mede o tempo máximo aceitável para restaurar o serviço.

PORQUE

II. RTO e RPO são parâmetros que orientam decisões de replicação, backup e failover, pois traduzem tolerância de negócio a perda de dados e a indisponibilidade em metas técnicas mensuráveis.

a. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
b. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
c. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**20.** I. Uma arquitetura distribuída bem projetada permanece ótima indefinidamente, sem exigir revisão de custos, capacidade ou decisões técnicas ao longo do tempo.

PORQUE

II. O custo de operação de um sistema distribuído é determinado exclusivamente pelo número de linhas de código do sistema, sendo independente de decisões de replicação, particionamento ou observabilidade.

a. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
b. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
c. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
d. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*e. As asserções I e II são proposições falsas.

### Interpretação (questões 21 a 40)

**21.** A equipe da NexaOrder definiu um SLO mensal de 99,9% de disponibilidade para o serviço de checkout. Faltando 10 dias para o fim de um mês de 30 dias, o painel de observabilidade indica que 80% do orçamento de erro mensal já foi consumido. Diante desse cenário, qual conduta é mais consistente com a prática de engenharia de confiabilidade?

a. Interpretar o consumo do orçamento como evidência de que o SLO foi definido de forma equivocada e deve ser abandonado.
b. Concluir que, como o serviço ainda está no ar, o consumo do orçamento de erro não representa risco algum para o restante do mês.
*c. Reduzir temporariamente a frequência de implantações arriscadas e priorizar correções de estabilidade até que a taxa de consumo do orçamento se estabilize, já que o ritmo atual de consumo é incompatível com o tempo restante do mês.
d. Aumentar imediatamente o valor do SLO definido para 99,99%, tornando o orçamento restante proporcionalmente maior.
e. Ignorar o consumo do orçamento, pois o indicador só deve ser considerado no último dia do mês, quando o resultado final é conhecido.

**22.** Um trace distribuído de uma requisição de compra na NexaOrder registrou os seguintes tempos de execução (spans): gateway, 15 ms; serviço de pedidos, 40 ms; serviço de estoque, 35 ms; serviço de pagamento, 310 ms; serviço de expedição, 20 ms, totalizando 420 ms. O objetivo de latência (SLO) definido para o fluxo completo é de p95 igual ou inferior a 300 ms. Com base exclusivamente nesse trace, qual é a conclusão mais adequada?

a. O trace não permite qualquer conclusão sobre onde investigar, pois latência de rede não pode ser medida por instrumentação.
*b. Esta requisição específica ultrapassou 300 ms e o pagamento concentra a maior parcela observada, sendo o primeiro alvo de investigação; porém, um único trace não permite concluir se o p95 do período cumpre ou viola o SLO.
c. O gargalo está distribuído igualmente entre todos os serviços, portanto qualquer otimização isolada terá o mesmo impacto.
d. Como o gateway apresentou o menor tempo de execução, ele deve ser o primeiro componente investigado.
e. A soma dos tempos indica falha do sistema de observabilidade, já que nenhum serviço deveria ultrapassar 300 ms individualmente.

**23.** O painel de métricas da NexaOrder mostra um aumento pontual na taxa de erros do fluxo de pedidos entre 18h e 19h, sem que nenhum serviço tenha sido reiniciado ou apresentado indisponibilidade total. A equipe deseja identificar a causa exata dentro dessa janela. Qual é a sequência de investigação mais adequada?

a. Aumentar o número de réplicas de todos os serviços, já que qualquer aumento de erro é sempre resolvido por mais capacidade computacional.
b. Aguardar o próximo incidente idêntico antes de investigar, pois dados históricos não têm valor diagnóstico em sistemas distribuídos.
*c. Usar as métricas para delimitar a janela de tempo e os serviços afetados e, em seguida, examinar logs e traces correlacionados a requisições com falha registradas nesse intervalo, buscando um padrão comum entre elas.
d. Descartar os traces coletados no período, pois amostras estatísticas não representam adequadamente o comportamento real do sistema.
e. Ignorar as métricas, pois elas não são suficientes por si só, e reescrever o serviço de pagamento do zero como medida preventiva.

**24.** A equipe de plataforma da NexaOrder propõe definir a utilização média de CPU dos servidores como o principal indicador de nível de serviço (SLI) do fluxo de checkout, argumentando que o valor é fácil de coletar. Do ponto de vista da prática de definição de SLIs orientados à experiência do cliente, qual é a avaliação mais adequada dessa proposta?

a. A proposta é adequada, mas apenas se a utilização de CPU for medida em todos os data centers simultaneamente.
b. A proposta é adequada, pois qualquer métrica de infraestrutura reflete diretamente a experiência do cliente.
c. A proposta é inadequada porque SLIs só podem ser definidos para serviços que não utilizam contêineres.
*d. A proposta é inadequada porque a utilização de CPU é uma métrica interna de recurso, que pode permanecer baixa mesmo quando pedidos falham ou demoram além do aceitável, não capturando diretamente a experiência do usuário; um SLI mais adequado seria, por exemplo, a proporção de requisições de checkout concluídas com sucesso dentro de um limite de latência.
e. A proposta é inadequada porque a utilização de CPU não pode ser coletada por nenhuma ferramenta de observabilidade atual.

**25.** Ao investigar um pedido da NexaOrder que passou por comunicação síncrona (API) e, em seguida, por um evento assíncrono publicado em um tópico consumido pelo serviço de expedição, a equipe percebeu que o trace se interrompe no limite entre a chamada HTTP e a publicação do evento, impedindo a reconstrução do caminho completo. Qual é a causa mais provável e a correção adequada?

*a. O contexto de rastreamento provavelmente não está sendo propagado nos metadados/cabeçalhos da mensagem publicada; a correção adequada é instrumentar o produtor para incluir o contexto de rastreamento no cabeçalho do evento e o consumidor para extraí-lo ao processar a mensagem, preservando a continuidade do trace.
b. A correção adequada é abandonar a mensageria assíncrona e substituí-la integralmente por chamadas síncronas, eliminando o problema de propagação de contexto.
c. O problema ocorre porque o serviço de expedição está implementado em uma linguagem diferente da usada pelo serviço de pedidos, e traces não funcionam entre linguagens distintas.
d. O problema é irrelevante, pois cada serviço deve ser observado de forma totalmente independente, sem qualquer necessidade de correlação entre eles.
e. Traces distribuídos não podem, por definição, atravessar sistemas de mensageria, sendo essa uma limitação permanente da abordagem.

**26.** O serviço de pedidos da NexaOrder alterou, sem aviso prévio, o nome de um campo em um evento publicado, o que quebrou a lógica do serviço de estoque em produção. As equipes trabalham de forma independente e não compartilham o mesmo repositório de código. Qual prática de teste teria maior probabilidade de detectar esse problema antes da implantação em produção?

a. Testes de penetração de segurança focados exclusivamente em autenticação e autorização.
b. Testes unitários exclusivamente no serviço de pedidos, sem qualquer conhecimento do formato esperado pelos consumidores.
c. Testes manuais exploratórios realizados apenas pela equipe de pedidos, sem participação da equipe de estoque.
*d. Testes de contrato orientados pelo consumidor, em que o serviço de estoque define expectativas sobre o formato do evento e o serviço de pedidos verifica, em seu próprio pipeline, se essas expectativas continuam sendo atendidas antes de publicar uma nova versão.
e. Testes de carga executados uma vez por trimestre em ambiente de homologação.

**27.** A equipe de confiabilidade da NexaOrder planeja três experimentos distintos: (1) manter o sistema sob a carga máxima esperada em um dia de promoção por 24 horas contínuas, para observar vazamentos de memória e degradação gradual; (2) aumentar a carga progressivamente além do esperado até que o sistema apresente falha, para identificar seu limite; (3) validar se o sistema sustenta o tráfego típico de um dia normal sem violar o SLO de latência. Quais são, respectivamente, os tipos de teste mais adequados para os três experimentos?

a. Teste de penetração; teste de carga; teste de estresse.
b. Teste de carga; teste unitário; teste de duração.
c. Teste de estresse; teste de duração; teste de contrato.
d. Teste de contrato; teste de penetração; teste unitário.
*e. Teste de duração (soak test); teste de estresse; teste de carga.

**28.** A equipe da NexaOrder está formulando um experimento de engenharia do caos para avaliar o comportamento do sistema diante da indisponibilidade momentânea do provedor de pagamento. Qual das alternativas a seguir representa uma hipótese de estado estável corretamente formulada para esse experimento?

a. "O sistema não deve, em hipótese alguma, apresentar qualquer erro durante o experimento, mesmo diante da indisponibilidade simulada do provedor de pagamento."
b. "Como o serviço de pagamento já foi testado manualmente uma vez, não é necessário formular qualquer hipótese antes do experimento."
c. "O experimento será considerado bem-sucedido se nenhuma métrica for coletada durante sua execução, evitando resultados tendenciosos."
*d. "Em condições normais, a taxa de conclusão de pedidos permanece acima de 98% e a latência p95 do checkout permanece abaixo de 400 ms; durante a indisponibilidade simulada do provedor de pagamento, o circuito de proteção deve ser acionado, o sistema deve degradar graciosamente informando o cliente, e a taxa de conclusão de pedidos não deve cair abaixo de 90%."
e. "A equipe espera que algo aconteça de diferente durante o experimento, mas não é possível prever o quê."

**29.** Ao planejar o experimento de indisponibilidade do serviço de pagamento, a equipe da NexaOrder precisa decidir como limitar o risco para os clientes reais. Qual configuração representa a aplicação mais adequada dos princípios de raio de impacto controlado e mecanismo de interrupção?

*a. Executar o experimento inicialmente afetando uma pequena fração do tráfego real ou um subconjunto controlado de instâncias, com um mecanismo que permita interromper imediatamente a injeção de falha caso os indicadores de negócio ultrapassem um limite predefinido de degradação.
b. Executar o experimento apenas quando o tráfego estiver em seu pico histórico máximo, para maximizar a relevância estatística dos resultados.
c. Executar o experimento apenas em ambiente de desenvolvimento local, isolado de qualquer característica realista de produção, e considerar os resultados diretamente aplicáveis ao ambiente de produção.
d. Executar o experimento em produção, afetando 100% do tráfego real, sem qualquer possibilidade de interromper a injeção de falha antes do horário previamente agendado.
e. Executar o experimento afetando aleatoriamente qualquer serviço do sistema, sem relação com a hipótese formulada sobre o provedor de pagamento.

**30.** Após um incidente real em que a indisponibilidade do provedor de pagamento causou falhas em cascata na NexaOrder, a equipe conduz um postmortem. Qual conduta está mais alinhada com a prática de aprendizagem operacional sem culpabilização (blameless postmortem)?

a. Restringir o acesso ao relatório do postmortem apenas à liderança técnica, para evitar constrangimento das pessoas envolvidas.
*b. Reconstruir a linha do tempo do incidente, identificar fatores contribuintes sistêmicos (como ausência de teste de contrato ou de raio de impacto limitado em experimentos anteriores), documentar ações de melhoria com responsáveis e prazos, e compartilhar o aprendizado com toda a organização.
c. Concluir que o incidente foi resultado de erro humano isolado e que nenhuma mudança sistêmica é necessária.
d. Encerrar o postmortem assim que a causa imediata for identificada, sem documentar ações de acompanhamento.
e. Identificar o funcionário responsável pela configuração do circuito de proteção e aplicar uma medida disciplinar formal.

**31.** A NexaOrder deseja detectar padrões suspeitos de fraude (por exemplo, múltiplas tentativas de compra com cartões diferentes em poucos segundos a partir do mesmo dispositivo) antes que o pedido seja aprovado. A equipe avalia duas alternativas: um pipeline de processamento em lote executado a cada hora, ou um pipeline de processamento em fluxo que avalia cada evento de tentativa de compra assim que ele ocorre. Qual alternativa atende melhor ao requisito de negócio descrito e por quê?

a. O processamento em lote é mais adequado, pois lotes horários garantem maior precisão estatística do que qualquer processamento evento a evento.
b. As duas alternativas são equivalentes, pois a janela de tempo entre eventos não influencia a eficácia da detecção de fraude.
c. O processamento em lote é mais adequado, pois elimina totalmente a necessidade de particionamento e tolerância a falhas.
d. Nenhuma das alternativas é adequada, pois a detecção de fraude não pode ser automatizada em sistemas distribuídos.
*e. O processamento em fluxo é mais adequado, pois a decisão de aprovar ou bloquear o pedido precisa ocorrer em segundos, e um pipeline em lote executado a cada hora não teria informação atualizada a tempo de impedir a fraude antes da aprovação.

**32.** Durante a execução de um job de processamento em lote sobre o histórico de pedidos da NexaOrder, um dos nós responsáveis pela fase de redução falha antes de concluir seu trabalho. Considerando o modelo MapReduce e frameworks de DAG modernos inspirados nele, qual é o comportamento esperado do sistema?

a. A falha de um único nó de redução é sempre ignorada, e o resultado final é produzido sem os dados desse nó, sem qualquer inconsistência.
b. O modelo MapReduce não é capaz de lidar com falhas de nós, sendo essa uma limitação exclusiva de frameworks mais recentes baseados em DAGs.
*c. O framework deve identificar a tarefa de redução malsucedida e reatribuí-la a outro nó disponível, reexecutando-a a partir dos dados intermediários já persistidos ou reprocessados pelas tarefas de mapeamento correspondentes, sem exigir intervenção manual para esse tipo de falha isolada.
d. O job deve ser cancelado definitivamente, e todo o histórico de pedidos deve ser reprocessado manualmente linha a linha.
e. Todo o cluster deve ser reiniciado manualmente, pois o modelo não prevê nenhuma forma de recuperação automática.

**33.** Um evento de confirmação de pagamento da NexaOrder foi gerado às 14h00 (tempo de evento), mas, devido a uma instabilidade de rede, só chegou ao pipeline de processamento em fluxo às 14h07 (tempo de processamento). O pipeline calcula, em janelas de um minuto baseadas em tempo de evento, o volume de pagamentos aprovados por minuto. Qual mecanismo permite que esse pipeline ainda atribua corretamente o evento atrasado à janela das 14h00–14h01, dentro de um limite configurado de tolerância?

*a. Uso de marcas d'água (watermarks) e de uma tolerância configurável a atraso (allowed lateness), que mantêm a janela correspondente ao tempo de evento aberta por um período adicional antes de ser considerada definitivamente fechada.
b. Descarte automático e definitivo de qualquer evento que não chegue na ordem exata de geração.
c. Processamento exclusivamente em lote, pois pipelines de fluxo não conseguem lidar com eventos fora de ordem.
d. Reinicialização completa do pipeline a cada evento atrasado recebido.
e. Substituição do tempo de evento pelo tempo de processamento em todos os cálculos, eliminando a necessidade de qualquer tratamento especial.

**34.** A NexaOrder precisa processar um evento esporádico e de curta duração: enviar uma notificação por e-mail sempre que um pedido é confirmado, com volume variável e picos apenas em datas promocionais. Do ponto de vista de compromissos entre modelo de execução, custo e latência, qual avaliação é mais adequada para a escolha entre uma função como serviço (FaaS) e um serviço de longa duração dedicado?

a. O serviço de longa duração elimina completamente qualquer custo de infraestrutura, tornando-se sempre a opção mais barata.
*b. A FaaS tende a ser adequada para essa carga esporádica e de curta duração, pois o modelo cobra por execução e escala automaticamente com picos, embora seja necessário considerar a latência adicional de inicialização a frio (cold start) em invocações após períodos de ociosidade.
c. Ambos os modelos são idênticos em custo e desempenho, tornando a escolha irrelevante.
d. O serviço de longa duração é sempre superior, pois FaaS não pode ser acionado por eventos.
e. A FaaS é inadequada, pois funções como serviço não podem, em nenhuma hipótese, processar eventos assíncronos.

**35.** A NexaOrder avalia executar parte da análise de fraude diretamente em pontos de borda próximos aos dispositivos dos clientes, em vez de centralizar todo o processamento em uma região de nuvem. Qual consideração melhor descreve o compromisso entre custo e latência nessa decisão?

a. A latência é irrelevante para decisões de detecção de fraude, tornando desnecessária qualquer análise de localização de dados.
b. O custo de operação em pontos de borda é sempre inferior ao custo de uma região central de nuvem, independentemente do volume de dispositivos atendidos.
c. A computação de borda deve ser adotada integralmente, pois elimina por completo a necessidade de qualquer processamento central, independentemente da complexidade do modelo de fraude.
*d. A decisão deve ponderar a redução de latência obtida ao processar sinais simples próximos ao cliente contra o custo e a complexidade operacional de manter lógica distribuída em múltiplos pontos de borda, reservando modelos mais complexos ou que dependam de contexto histórico amplo para o processamento centralizado.
e. A computação de borda não deve ser considerada, pois qualquer processamento fora de uma região central de nuvem é, por definição, inseguro.

**36.** Ao revisar a arquitetura final da NexaOrder, a equipe percebe que dois requisitos de qualidade entram em tensão: o time de produto deseja reduzir ao máximo a latência de exibição do catálogo, enquanto o time de confiabilidade exige garantias mais fortes de consistência no saldo de estoque exibido ao cliente. Qual conduta melhor reflete uma avaliação arquitetural madura desse compromisso?

a. Concluir que, como os dois requisitos entram em tensão, um deles deve ser eliminado do sistema.
b. Exigir consistência forte em toda a aplicação, sem exceção, pois qualquer leitura desatualizada é sempre inaceitável, independentemente do contexto de uso.
*c. Explicitar o compromisso entre latência e consistência para cada parte do sistema separadamente, aceitando, por exemplo, leituras eventualmente consistentes no catálogo, mas exigindo consistência mais forte no momento da confirmação da reserva de estoque durante o checkout.
d. Ignorar completamente o requisito de latência do catálogo, pois atributos de qualidade não têm relevância arquitetural comparável aos requisitos funcionais.
e. Resolver o conflito escolhendo aleatoriamente entre os dois times, sem qualquer análise técnica dos compromissos envolvidos.

**37.** Ao compilar os registros de decisão arquitetural (ADRs) da NexaOrder ao longo das quatro unidades, a equipe encontra um documento que afirma apenas: "Decidimos usar Kubernetes." Do ponto de vista das boas práticas de documentação arquitetural discutidas na disciplina, qual é a avaliação mais adequada desse registro?

a. O registro está completo, pois um ADR deve conter apenas o nome da tecnologia escolhida, sem qualquer justificativa adicional.
*b. O registro está incompleto, pois um ADR deve também explicitar o contexto que motivou a decisão, as alternativas consideradas e as consequências esperadas, elementos ausentes nesse exemplo.
c. O registro está completo, desde que seja armazenado em uma ferramenta de gestão de projetos, independentemente do conteúdo textual.
d. O registro é desnecessário, pois decisões de orquestração de contêineres não precisam ser documentadas.
e. O registro deveria ter sido feito apenas pela equipe de segurança, e não pela equipe de infraestrutura.

**38.** Na revisão final da NexaOrder, a equipe descreve a seguinte configuração: o serviço de pagamento possui três réplicas distribuídas em três zonas de disponibilidade distintas, mas todas as réplicas dependem de uma única instância do sistema de mensageria, hospedada em apenas uma zona, sem réplicas configuradas. Qual é a conclusão mais adequada sobre pontos únicos de falha nessa configuração?

a. Não existe ponto único de falha, pois o serviço de pagamento em si está replicado em três zonas.
b. Pontos únicos de falha só podem existir em bancos de dados, nunca em sistemas de mensageria.
c. O ponto único de falha está nas réplicas do serviço de pagamento, e não no sistema de mensageria.
d. A configuração é adequada, pois três réplicas de qualquer componente eliminam automaticamente qualquer ponto único de falha do sistema como um todo.
*e. O sistema de mensageria não replicado constitui um ponto único de falha, pois sua indisponibilidade pode impedir a comunicação entre os serviços mesmo com o serviço de pagamento saudável em suas três réplicas.

**39.** A NexaOrder replica de forma assíncrona o banco de dados de pedidos para uma região secundária a cada 5 minutos, e o plano de recuperação prevê que a equipe consiga promover a região secundária e restabelecer o serviço em até 15 minutos após um desastre na região primária. Nesse cenário, quais são, respectivamente, o RPO e o RTO aproximados do plano descrito?

*a. RPO de aproximadamente 5 minutos, correspondente à possível perda de dados entre a última replicação bem-sucedida e o desastre, e RTO de aproximadamente 15 minutos, correspondente ao tempo necessário para restabelecer o serviço.
b. RPO de 0 minutos e RTO de 0 minutos, pois a replicação assíncrona garante recuperação instantânea.
c. RPO e RTO são ambos indefinidos, pois não é possível estimá-los sem um desastre real.
d. RPO de 15 minutos e RTO de 5 minutos.
e. RPO de 5 minutos e RTO de 5 minutos, pois ambos os indicadores são sempre iguais ao intervalo de replicação.

**40.** Passados alguns meses da implantação da arquitetura final, a equipe da NexaOrder percebe que o número de instâncias provisionadas para o pico de tráfego permanece constante mesmo em horários de baixíssima demanda, gerando custo elevado sem benefício correspondente de desempenho ou confiabilidade. Qual conduta está mais alinhada com uma visão madura de custo, sustentabilidade e evolução arquitetural?

a. Manter a capacidade fixa indefinidamente, pois qualquer redução de instâncias representa risco inaceitável, independentemente dos dados de utilização observados.
*b. Revisar a estratégia de capacidade com base em dados reais de utilização, adotando mecanismos de escalonamento automático que ajustem o número de instâncias à demanda observada, preservando as metas de disponibilidade e desempenho definidas para os cenários de pico.
c. Revisar apenas o custo da equipe de desenvolvimento, sem considerar o custo de infraestrutura como parte da avaliação arquitetural.
d. Ignorar o custo observado, pois atributos de qualidade como desempenho e disponibilidade nunca devem ser avaliados em conjunto com custo.
e. Eliminar toda a redundância do sistema imediatamente, retornando a uma única instância para reduzir custo ao mínimo possível.

## Gabarito e feedbacks

**Questão 1** (correta: b)
- a. Incorreta: I é verdadeira, não falsa; monitoramento tradicional é, de fato, insuficiente para falhas inéditas.
- b. Correta: I é verdadeira — monitoramento baseado em condições conhecidas não cobre falhas inéditas — e II justifica diretamente essa limitação, ao descrever como a observabilidade permite investigar perguntas não antecipadas.
- c. Incorreta: ambas as asserções são verdadeiras, não falsas.
- d. Incorreta: II não é apenas verdadeira, ela explica exatamente por que I é verdadeira.
- e. Incorreta: II também é verdadeira, não falsa; observabilidade de fato dispensa a criação prévia de um painel específico para cada falha.

**Questão 2** (correta: c)
- a. Incorreta: I é verdadeira, não falsa; os três pilares são de fato complementares.
- b. Incorreta: II é verdadeira, mas descreve apenas a natureza das métricas, sem explicar por que os três pilares são complementares entre si.
- c. Correta: ambas são verdadeiras, mas II apenas define métricas, sem justificar a complementaridade entre métricas, logs e traces afirmada em I.
- d. Incorreta: II também é verdadeira, não falsa; a definição de métricas apresentada está correta.
- e. Incorreta: ambas as asserções são verdadeiras.

**Questão 3** (correta: e)
- a. Incorreta: I é verdadeira, não falsa.
- b. Incorreta: I é verdadeira, não falsa.
- c. Incorreta: II é falsa, não verdadeira; propagação de contexto não é automática nem faz parte do protocolo TCP/IP.
- d. Incorreta: II é falsa, portanto não pode ser uma justificativa verdadeira, ainda que não correta, de I.
- e. Correta: I é verdadeira — o trace ID propagado permite reconstruir o caminho da requisição — e II é falsa, pois a propagação exige instrumentação explícita em cada serviço, não ocorre automaticamente por protocolo de rede.

**Questão 4** (correta: d)
- a. Incorreta: II é verdadeira, não falsa.
- b. Incorreta: I é falsa, portanto essa alternativa não se aplica.
- c. Incorreta: I é falsa, não verdadeira; as definições de SLI e SLO estão trocadas em relação ao conceito correto.
- d. Correta: I é falsa — inverte as definições de SLI e SLO — e II é verdadeira, apresentando corretamente o SLI como medida quantitativa observada e o SLO como meta definida para esse indicador.
- e. Incorreta: II é verdadeira, não falsa; ela apresenta corretamente as definições de SLI e SLO.

**Questão 5** (correta: a)
- a. Correta: I é falsa, pois o orçamento de erro é consumido por falhas reais observadas em produção, não aumentado por implantações; II é falsa, pois a taxa de consumo do orçamento é um dos principais insumos para decisões operacionais, como pausar implantações arriscadas.
- b. Incorreta: II também é falsa, não verdadeira; a taxa de consumo do orçamento (burn rate) é altamente relevante para decisões operacionais.
- c. Incorreta: ambas as asserções são falsas.
- d. Incorreta: ambas as asserções são falsas, não verdadeiras.
- e. Incorreta: I também é falsa, não verdadeira; o orçamento de erro não aumenta automaticamente com implantações, ele é consumido por falhas observadas.

**Questão 6** (correta: c)
- a. Incorreta: ambas as asserções são verdadeiras.
- b. Incorreta: I é verdadeira, não falsa; essa é exatamente a recomendação da pirâmide de testes em sistemas distribuídos.
- c. Correta: ambas as asserções são verdadeiras, e II justifica diretamente I, explicando por que a pirâmide recomenda uma base ampla de testes mais baratos e uma menor proporção de testes de ponta a ponta.
- d. Incorreta: II de fato justifica I, não é uma relação sem nexo lógico.
- e. Incorreta: II também é verdadeira, não falsa; testes de ponta a ponta realmente tendem a ser mais lentos e frágeis.

**Questão 7** (correta: a)
- a. Correta: ambas as asserções são verdadeiras, mas II trata da governança colaborativa dos contratos, enquanto I trata da independência de execução entre os serviços — não há relação de justificativa direta entre elas.
- b. Incorreta: I é verdadeira, não falsa; essa é justamente a vantagem central dos testes de contrato.
- c. Incorreta: II é verdadeira, mas não justifica diretamente a afirmação de I sobre não exigir execução simultânea dos dois serviços.
- d. Incorreta: II também é verdadeira, não falsa.
- e. Incorreta: ambas as asserções são verdadeiras.

**Questão 8** (correta: d)
- a. Incorreta: I é verdadeira, não falsa.
- b. Incorreta: II é falsa, portanto não pode justificar I.
- c. Incorreta: I é verdadeira, não falsa.
- d. Correta: I é verdadeira — a hipótese de estado estável é o ponto de partida de um experimento bem projetado — e II é falsa, pois a coleta prévia de métricas é justamente o que permite comparar o comportamento antes e durante a falha injetada.
- e. Incorreta: II é falsa, não verdadeira; a hipótese de estado estável depende, sim, de métricas coletadas antes do experimento para servir de referência.

**Questão 9** (correta: e)
- a. Incorreta: II é verdadeira, não falsa.
- b. Incorreta: I é falsa, portanto essa alternativa não se aplica.
- c. Incorreta: I é falsa, não verdadeira; a prática recomendada é começar com raio de impacto limitado, não maximizado.
- d. Incorreta: II é verdadeira, não falsa.
- e. Correta: I é falsa, pois maximizar o raio de impacto na primeira execução contraria a prática responsável de engenharia do caos; II é verdadeira, pois limitar o raio de impacto de fato reduz o risco de indisponibilidade real para os clientes.

**Questão 10** (correta: a)
- a. Correta: I é falsa, pois o postmortem sem culpa busca causas sistêmicas, não a punição de indivíduos; II é falsa, pois o histórico de incidentes é justamente um dos principais insumos para planejar novos experimentos de caos com foco nos riscos já conhecidos.
- b. Incorreta: I também é falsa; o objetivo do postmortem sem culpa é justamente evitar a identificação e punição de indivíduos, focando em causas sistêmicas.
- c. Incorreta: ambas as asserções são falsas.
- d. Incorreta: II também é falsa; incidentes anteriores devem, sim, influenciar o planejamento de novos experimentos, pois raramente são estatisticamente independentes em sistemas com dependências compartilhadas.
- e. Incorreta: ambas as asserções são falsas, não verdadeiras.

**Questão 11** (correta: c)
- a. Incorreta: II de fato justifica I nesse caso.
- b. Incorreta: ambas as asserções são verdadeiras.
- c. Correta: ambas as asserções são verdadeiras, e II justifica diretamente I, explicando a característica do processamento em fluxo (dados ilimitados, processados assim que disponíveis) que o torna adequado à avaliação em tempo quase real.
- d. Incorreta: I é verdadeira, não falsa; o processamento em fluxo de fato permite essa avaliação contínua.
- e. Incorreta: II também é verdadeira, não falsa; essa é a definição correta de processamento em fluxo.

**Questão 12** (correta: d)
- a. Incorreta: I é verdadeira, não falsa; essa é a definição correta da fase de embaralhamento.
- b. Incorreta: ambas as asserções são verdadeiras.
- c. Incorreta: II também é verdadeira, não falsa; o MapReduce foi de fato descrito por Dean e Ghemawat.
- d. Correta: ambas as asserções são verdadeiras, mas II é um fato histórico sobre a origem do modelo, enquanto I descreve um mecanismo interno — não há relação de justificativa direta entre elas.
- e. Incorreta: II é verdadeira, mas não justifica diretamente o mecanismo descrito em I; trata de autoria histórica, não do funcionamento do shuffle.

**Questão 13** (correta: b)
- a. Incorreta: I é verdadeira, não falsa.
- b. Correta: I é verdadeira — tempo de evento pode diferir do tempo de processamento — e II é falsa, pois mecanismos como marcas d'água e tolerância configurável a atraso permitem atribuir corretamente eventos atrasados às janelas certas, sem tornar o conceito de janela inútil.
- c. Incorreta: II é falsa, portanto não pode justificar I.
- d. Incorreta: I é verdadeira, não falsa.
- e. Incorreta: II é falsa, não verdadeira; eventos atrasados podem, sim, ser corretamente atribuídos a janelas por meio de marcas d'água e tolerância a atraso.

**Questão 14** (correta: e)
- a. Incorreta: II é verdadeira, não falsa.
- b. Incorreta: I é falsa, portanto essa alternativa não se aplica.
- c. Incorreta: I é falsa, não verdadeira; FaaS não mantém sempre uma instância quente, por isso existe o fenômeno de inicialização a frio.
- d. Incorreta: II é verdadeira, não falsa.
- e. Correta: I é falsa, pois a ausência de instância quente é justamente o que caracteriza a inicialização a frio; II é verdadeira, descrevendo corretamente o fenômeno de cold start quando não há instância ociosa disponível.

**Questão 15** (correta: a)
- a. Correta: I é falsa, pois a computação de borda tipicamente complementa, e não elimina, a comunicação com uma região central; II é falsa, pois a escolha entre borda e processamento central depende do volume de dados e da complexidade exigida, não havendo favorecimento absoluto da borda.
- b. Incorreta: II também é falsa; o compromisso entre custo e latência não favorece sempre a borda, dependendo do volume e da complexidade do processamento.
- c. Incorreta: I também é falsa; a computação de borda não elimina totalmente a comunicação com uma região central, especialmente para lógica que depende de contexto histórico amplo.
- d. Incorreta: ambas as asserções são falsas, não verdadeiras.
- e. Incorreta: ambas as asserções são falsas.

**Questão 16** (correta: b)
- a. Incorreta: II de fato justifica I nesse caso.
- b. Correta: ambas as asserções são verdadeiras, e II justifica diretamente I, explicando por que atributos de qualidade influenciam decisões arquiteturais específicas ao lado dos requisitos funcionais.
- c. Incorreta: I é verdadeira, não falsa; atributos de qualidade também influenciam decisivamente a arquitetura.
- d. Incorreta: ambas as asserções são verdadeiras.
- e. Incorreta: II também é verdadeira, não falsa; essa é a distinção correta entre requisito funcional e atributo de qualidade.

**Questão 17** (correta: e)
- a. Incorreta: II também é verdadeira, não falsa; ferramentas de versionamento realmente permitem esse rastreamento.
- b. Incorreta: ambas as asserções são verdadeiras.
- c. Incorreta: II é verdadeira, mas trata de uma questão de ferramental de armazenamento, não justificando diretamente o conteúdo que um ADR deve documentar, afirmado em I.
- d. Incorreta: I é verdadeira, não falsa; essa é a definição correta de um ADR completo.
- e. Correta: ambas as asserções são verdadeiras, mas II descreve uma prática de armazenamento de ADRs, enquanto I descreve o conteúdo que um ADR deve conter — não há relação de justificativa direta entre elas.

**Questão 18** (correta: c)
- a. Incorreta: I é verdadeira, não falsa.
- b. Incorreta: I é verdadeira, não falsa.
- c. Correta: I é verdadeira — a análise de SPOF deve identificar componentes cuja indisponibilidade isolada compromete todo o fluxo — e II é falsa, pois réplicas distribuídas fisicamente ainda podem compartilhar uma dependência não replicada, tornando-se, em conjunto, parte de um ponto único de falha.
- d. Incorreta: II é falsa, não verdadeira; um componente com múltiplas réplicas pode, sim, fazer parte de um ponto único de falha, se todas as réplicas compartilharem uma dependência não replicada.
- e. Incorreta: II é falsa, portanto não pode ser uma justificativa, correta ou não, de I.

**Questão 19** (correta: d)
- a. Incorreta: II é verdadeira, não falsa; RTO e RPO de fato orientam decisões de replicação, backup e failover.
- b. Incorreta: I é falsa, não verdadeira; as definições de RTO e RPO estão trocadas em relação ao conceito correto.
- c. Incorreta: I é falsa, portanto essa alternativa não se aplica.
- d. Correta: I é falsa, pois inverte as definições — RPO mede perda de dados tolerável e RTO mede tempo de recuperação tolerável; II é verdadeira, descrevendo corretamente o papel de RTO e RPO como metas técnicas mensuráveis derivadas de tolerância de negócio.
- e. Incorreta: II é verdadeira, não falsa.

**Questão 20** (correta: e)
- a. Incorreta: ambas as asserções são falsas.
- b. Incorreta: II também é falsa; o custo de operação depende fortemente de decisões de replicação, particionamento e observabilidade, não apenas do número de linhas de código.
- c. Incorreta: ambas as asserções são falsas, não verdadeiras.
- d. Incorreta: I também é falsa; nenhuma arquitetura permanece ótima indefinidamente sem revisão de custo, capacidade e decisões técnicas.
- e. Correta: I é falsa, pois toda arquitetura distribuída exige revisão contínua de custo, capacidade e decisões técnicas ao longo do tempo; II é falsa, pois o custo de operação é diretamente influenciado por decisões de replicação, particionamento e observabilidade, não apenas pelo tamanho do código.

**Questão 21** (correta: c)
- a. Incorreta: consumo elevado do orçamento não indica, por si só, que o SLO foi definido de forma equivocada, apenas que o comportamento observado está fora do esperado para o período.
- b. Incorreta: o fato de o serviço continuar no ar não elimina o risco de violar o SLO se o ritmo de consumo do orçamento se mantiver.
- c. Correta: reduzir o ritmo de mudanças arriscadas é a resposta operacional adequada quando a taxa de consumo do orçamento de erro está incompatível com o tempo restante do período de medição.
- d. Incorreta: alterar o SLO definido é uma decisão de produto e negócio, que não deve ser tomada unilateralmente como reação operacional imediata a um consumo elevado.
- e. Incorreta: o orçamento de erro deve ser monitorado continuamente, não apenas avaliado ao final do período de medição.

**Questão 22** (correta: b)
- a. Incorreta: exatamente o contrário é verdadeiro — traces distribuídos são projetados para permitir esse tipo de conclusão sobre onde investigar.
- b. Correta: o trace mostra que esta requisição excedeu 300 ms e aponta pagamento como maior parcela observada. A conformidade do p95 exige uma distribuição de muitas requisições no período, não uma única amostra.
- c. Incorreta: o gargalo está concentrado no serviço de pagamento (310 ms de 420 ms, cerca de 74% do total), não distribuído igualmente.
- d. Incorreta: o menor tempo de execução não é critério de prioridade de investigação; o objetivo é reduzir a latência total.
- e. Incorreta: o SLO se aplica ao fluxo completo, não exige que cada serviço individualmente fique abaixo de 300 ms, e a soma dos tempos não indica falha do sistema de observabilidade.

**Questão 23** (correta: c)
- a. Incorreta: aumentar réplicas não resolve necessariamente a causa raiz de um aumento correlacionado de erros em uma janela específica, além de gerar custo desnecessário.
- b. Incorreta: dados históricos têm valor diagnóstico significativo e não é necessário aguardar a recorrência do incidente para investigar.
- c. Correta: usar métricas para delimitar escopo e, em seguida, aprofundar com logs e traces correlacionados é o fluxo de investigação recomendado pela prática de observabilidade.
- d. Incorreta: traces coletados no período são justamente os dados mais úteis para identificar um padrão comum entre as requisições com falha.
- e. Incorreta: descartar métricas e reescrever um serviço inteiro sem investigação prévia é uma medida desproporcional e não baseada em evidência.

**Questão 24** (correta: d)
- a. Incorreta: medir CPU em todos os data centers não resolve a limitação fundamental de a métrica não capturar a experiência do usuário.
- b. Incorreta: métricas de infraestrutura não refletem diretamente a experiência do cliente; um serviço pode falhar sem que a CPU se eleve.
- c. Incorreta: a definição de SLIs não depende do uso ou não de contêineres.
- d. Correta: CPU é uma métrica interna de recurso que não captura diretamente falhas ou lentidão percebidas pelo usuário; um SLI orientado à experiência do cliente, como taxa de sucesso dentro de um limite de latência, é mais adequado.
- e. Incorreta: a utilização de CPU pode, sim, ser coletada por praticamente qualquer ferramenta de observabilidade atual; esse não é o problema da proposta.

**Questão 25** (correta: a)
- a. Correta: o problema mais provável é a ausência de propagação do contexto de rastreamento nos metadados da mensagem; a correção adequada envolve instrumentar produtor e consumidor para incluir e extrair esse contexto.
- b. Incorreta: abandonar a mensageria assíncrona é uma medida desproporcional que sacrifica benefícios arquiteturais para contornar um problema de instrumentação, corrigível de forma mais simples.
- c. Incorreta: a linguagem de implementação do serviço consumidor não é a causa da interrupção do trace; o problema está na propagação do contexto, não na linguagem.
- d. Incorreta: a correlação entre serviços é justamente o que permite investigar o caminho completo de uma requisição; não é irrelevante.
- e. Incorreta: traces distribuídos podem, sim, atravessar sistemas de mensageria, desde que o contexto seja propagado nos metadados da mensagem.

**Questão 26** (correta: d)
- a. Incorreta: testes de penetração de segurança têm outro escopo e não avaliam compatibilidade de esquema de eventos.
- b. Incorreta: testes unitários isolados no serviço de pedidos, sem conhecimento do contrato esperado pelo consumidor, não detectariam essa quebra específica.
- c. Incorreta: testes manuais exploratórios feitos apenas por uma das equipes, sem a participação da equipe consumidora, dificilmente identificariam essa quebra de contrato.
- d. Correta: testes de contrato orientados pelo consumidor detectam justamente esse tipo de incompatibilidade de esquema entre equipes independentes, antes da implantação em produção.
- e. Incorreta: testes de carga trimestrais não são projetados para detectar incompatibilidades de esquema entre serviços.

**Questão 27** (correta: e)
- a. Incorreta: teste de penetração e teste de carga não correspondem, respectivamente, ao primeiro e ao segundo experimento descritos.
- b. Incorreta: nenhum dos tipos mencionados corresponde corretamente aos três experimentos descritos.
- c. Incorreta: a correspondência está trocada entre os experimentos e os tipos de teste.
- d. Incorreta: nenhum dos três tipos de teste mencionados nessa alternativa corresponde aos experimentos descritos.
- e. Correta: teste de duração corresponde à observação de degradação ao longo de 24 horas; teste de estresse corresponde ao aumento progressivo até a falha; teste de carga corresponde à validação do tráfego típico sem violar o SLO.

**Questão 28** (correta: d)
- a. Incorreta: uma hipótese que exige ausência total de erro não é mensurável de forma realista e não reflete o objetivo de observar degradação graciosa sob falha controlada.
- b. Incorreta: um teste manual anterior não substitui a formulação de uma hipótese de estado estável mensurável para o experimento específico.
- c. Incorreta: a ausência de coleta de métricas impede qualquer verificação da hipótese, contrariando o propósito do experimento.
- d. Correta: a hipótese apresentada é mensurável, específica, e define tanto o comportamento normal quanto o comportamento esperado durante a falha injetada, incluindo limites numéricos verificáveis.
- e. Incorreta: uma hipótese vaga, sem previsão mensurável, não cumpre o requisito de ser uma expectativa específica e verificável.

**Questão 29** (correta: a)
- a. Correta: iniciar com raio de impacto limitado e manter um mecanismo de interrupção imediata acionado por limites de degradação predefinidos é a aplicação correta dos princípios de segurança em engenharia do caos.
- b. Incorreta: executar o experimento no pico histórico máximo de tráfego maximiza o risco para os clientes reais, contrariando o princípio de raio de impacto controlado.
- c. Incorreta: resultados obtidos exclusivamente em ambiente de desenvolvimento isolado não podem ser considerados diretamente aplicáveis a produção, dada a diferença de condições reais.
- d. Incorreta: afetar 100% do tráfego real sem mecanismo de interrupção viola tanto o princípio de raio de impacto limitado quanto o de interrupção imediata.
- e. Incorreta: afetar serviços aleatoriamente, sem relação com a hipótese formulada, não constitui um experimento controlado e válido.

**Questão 30** (correta: b)
- a. Incorreta: restringir o acesso ao relatório limita o compartilhamento do aprendizado, contrariando o objetivo de disseminar melhorias na organização.
- b. Correta: reconstruir a linha do tempo, identificar fatores sistêmicos contribuintes, documentar ações com responsáveis e prazos, e compartilhar o aprendizado é a prática recomendada de postmortem sem culpabilização.
- c. Incorreta: atribuir o incidente a erro humano isolado, sem investigar fatores sistêmicos, ignora causas estruturais que podem se repetir.
- d. Incorreta: encerrar o postmortem sem documentar ações de acompanhamento desperdiça a oportunidade de aprendizagem sistêmica do incidente.
- e. Incorreta: identificar e punir um indivíduo específico contraria diretamente o princípio de postmortem sem culpabilização.

**Questão 31** (correta: e)
- a. Incorreta: lotes horários não garantem, por definição, maior precisão estatística, e a alegação ignora o requisito de tempo de resposta do negócio.
- b. Incorreta: a janela de tempo entre eventos influencia diretamente a eficácia da detecção de fraude em tempo quase real, tornando as alternativas não equivalentes.
- c. Incorreta: o processamento em lote não elimina a necessidade de particionamento e tolerância a falhas, e tampouco atende ao requisito de tempo do negócio.
- d. Incorreta: a detecção de fraude pode, sim, ser automatizada em sistemas distribuídos, inclusive com processamento em fluxo.
- e. Correta: a decisão de bloquear ou aprovar precisa ocorrer em segundos, e um pipeline horário não teria informação atualizada a tempo de impedir a fraude antes da aprovação.

**Questão 32** (correta: c)
- a. Incorreta: ignorar os dados do nó falho produziria um resultado incompleto e inconsistente, não uma recuperação correta.
- b. Incorreta: a tolerância a falhas de nós é uma característica central do modelo MapReduce original, não uma limitação exclusiva de frameworks de DAG mais recentes.
- c. Correta: o framework reatribui a tarefa malsucedida a outro nó e a reexecuta a partir dos dados intermediários já disponíveis, sem exigir intervenção manual para uma falha isolada.
- d. Incorreta: cancelar o job inteiro e reprocessar manualmente contraria o propósito de tolerância a falhas automatizada do modelo.
- e. Incorreta: o modelo prevê recuperação automática de tarefas isoladas, sem exigir reinício manual de todo o cluster.

**Questão 33** (correta: a)
- a. Correta: marcas d'água combinadas com tolerância configurável a atraso permitem manter a janela correspondente ao tempo de evento aberta por tempo suficiente para acomodar eventos atrasados dentro de um limite aceitável.
- b. Incorreta: descartar automaticamente qualquer evento fora de ordem eliminaria dados válidos e não é a prática recomendada para tratamento de atraso.
- c. Incorreta: pipelines de fluxo, com os mecanismos adequados, conseguem lidar com eventos fora de ordem sem exigir processamento exclusivamente em lote.
- d. Incorreta: reinicializar todo o pipeline a cada evento atrasado seria impraticável e não é o mecanismo utilizado para tratar atraso de eventos.
- e. Incorreta: substituir tempo de evento por tempo de processamento eliminaria a fidelidade da análise ao momento real de ocorrência do evento no domínio de negócio.

**Questão 34** (correta: b)
- a. Incorreta: um serviço de longa duração não elimina custo de infraestrutura; ele mantém custo mesmo durante períodos de ociosidade.
- b. Correta: FaaS tende a ser adequada para cargas esporádicas e de curta duração, dado o modelo de cobrança por execução e escalonamento automático, com o custo adicional de latência em inicializações a frio.
- c. Incorreta: os dois modelos não são idênticos em custo e desempenho; eles apresentam compromissos distintos relevantes para a escolha.
- d. Incorreta: FaaS pode, sim, ser acionada por eventos assíncronos; essa é uma de suas aplicações mais comuns.
- e. Incorreta: funções como serviço são amplamente utilizadas para processar eventos assíncronos, contrariando a afirmação.

**Questão 35** (correta: d)
- a. Incorreta: a latência é altamente relevante para decisões de detecção de fraude em tempo quase real, tornando a análise de localização de dados necessária.
- b. Incorreta: o custo de operação em pontos de borda não é sempre inferior ao de uma região central, especialmente considerando a complexidade de manter lógica distribuída em muitos pontos.
- c. Incorreta: adotar a borda integralmente, eliminando todo processamento central, ignora a necessidade de contexto histórico amplo em modelos de fraude mais complexos.
- d. Correta: a decisão deve ponderar o ganho de latência para sinais simples e locais contra o custo e a complexidade de manter lógica distribuída na borda, reservando processamento mais complexo e dependente de contexto histórico para a região central.
- e. Incorreta: processamento fora de uma região central não é, por definição, inseguro; segurança depende de como a comunicação e os dados são protegidos, não da localização do processamento.

**Questão 36** (correta: c)
- a. Incorreta: a tensão entre dois requisitos de qualidade não implica que um deles deva ser eliminado; ela pode ser resolvida com decisões diferenciadas por contexto.
- b. Incorreta: exigir consistência forte em toda a aplicação, sem exceção, ignora os compromissos de latência e desempenho envolvidos em cada contexto de uso.
- c. Correta: explicitar o compromisso separadamente para cada parte do sistema, aceitando consistência eventual onde é tolerável e exigindo consistência mais forte onde a divergência tem custo direto, reflete uma avaliação arquitetural madura.
- d. Incorreta: atributos de qualidade como latência têm, sim, relevância arquitetural comparável à dos requisitos funcionais.
- e. Incorreta: resolver o conflito de forma aleatória, sem análise técnica, contraria a prática de avaliação arquitetural baseada em evidências e compromissos explícitos.

**Questão 37** (correta: b)
- a. Incorreta: um ADR deve conter, além da tecnologia escolhida, o contexto, as alternativas consideradas e as consequências esperadas.
- b. Correta: o registro está incompleto por não explicitar o contexto que motivou a decisão, as alternativas avaliadas e as consequências esperadas, elementos centrais de um ADR bem elaborado.
- c. Incorreta: o meio de armazenamento não supre a ausência de conteúdo substantivo sobre contexto, alternativas e consequências.
- d. Incorreta: decisões de orquestração de contêineres têm impacto arquitetural significativo e devem, sim, ser documentadas.
- e. Incorreta: a autoria do registro não deve ser restrita a uma equipe específica; deve envolver quem participou da decisão e é afetado por ela.

**Questão 38** (correta: e)
- a. Incorreta: a ausência de ponto único de falha não pode ser concluída sem considerar dependências compartilhadas, como o sistema de mensageria não replicado.
- b. Incorreta: pontos únicos de falha podem existir em qualquer componente não replicado do sistema, incluindo sistemas de mensageria, não apenas em bancos de dados.
- c. Incorreta: as réplicas do serviço de pagamento, distribuídas em zonas distintas, não constituem, isoladamente, o ponto único de falha descrito no cenário.
- d. Incorreta: réplicas de um componente não eliminam automaticamente pontos únicos de falha em outras partes do sistema das quais esse componente depende.
- e. Correta: o sistema de mensageria não replicado, hospedado em uma única zona, constitui um ponto único de falha, pois sua indisponibilidade pode comprometer a comunicação entre os serviços mesmo com o serviço de pagamento saudável em suas três réplicas.

**Questão 39** (correta: a)
- a. Correta: o RPO aproximado é de 5 minutos, refletindo a possível perda de dados desde a última replicação bem-sucedida, e o RTO aproximado é de 15 minutos, refletindo o tempo necessário para restabelecer o serviço.
- b. Incorreta: replicação assíncrona não garante recuperação instantânea nem perda zero de dados; há uma janela de possível perda entre replicações.
- c. Incorreta: RPO e RTO podem, sim, ser estimados a partir da configuração de replicação e do plano de recuperação descritos, sem exigir um desastre real.
- d. Incorreta: os valores estão trocados; o intervalo de replicação de 5 minutos corresponde ao RPO, e o tempo de restabelecimento de 15 minutos corresponde ao RTO.
- e. Incorreta: RPO e RTO não são necessariamente iguais ao intervalo de replicação; RTO reflete o tempo de restabelecimento do serviço, descrito no cenário como 15 minutos, não 5.

**Questão 40** (correta: b)
- a. Incorreta: manter capacidade fixa independentemente dos dados de utilização ignora a possibilidade de ajustar recursos com segurança, mantendo as metas de disponibilidade.
- b. Correta: revisar a estratégia de capacidade com base em dados reais de utilização, adotando escalonamento automático que ajuste recursos à demanda observada, preserva as metas de disponibilidade e desempenho sem manter custo desnecessário em períodos de baixa demanda.
- c. Incorreta: o custo de infraestrutura é parte central da avaliação arquitetural e não pode ser ignorado em favor exclusivo do custo de equipe.
- d. Incorreta: custo deve, sim, ser avaliado em conjunto com desempenho e disponibilidade, como parte de uma avaliação arquitetural completa.
- e. Incorreta: eliminar toda a redundância comprometeria a disponibilidade e a resiliência necessárias para os cenários de pico.
