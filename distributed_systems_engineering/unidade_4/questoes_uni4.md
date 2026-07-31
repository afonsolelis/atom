# Questionário — Unidade 4

Quantidade obrigatória: 40 questões.  
Distribuição: questões 1 a 20 de asserção-razão; questões 21 a 40 de interpretação.  
Cinco alternativas por questão (a. a e.), alternativa correta marcada com `*`, feedback específico para cada alternativa.

## Questões

### Asserção-razão (questões 1 a 20)

**1.** I. Monitoramento tradicional, baseado em painéis e alertas para condições previamente conhecidas, é insuficiente para diagnosticar falhas inéditas em um sistema como a NexaOrder.

II. A observabilidade permite formular perguntas não antecipadas sobre o comportamento interno do sistema a partir de métricas, logs e traces coletados, sem exigir a criação prévia de um painel específico para cada tipo de falha.

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**2.** I. Métricas, logs e traces são pilares complementares da observabilidade, cada um oferecendo uma perspectiva distinta sobre o comportamento do sistema.

II. As métricas são séries numéricas agregadas ao longo do tempo, adequadas para detectar tendências e disparar alertas.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**3.** I. Em uma arquitetura de microsserviços como a da NexaOrder, um identificador de correlação (trace ID) propagado entre serviços permite reconstruir o caminho completo de uma requisição.

II. A propagação do contexto de rastreamento ocorre automaticamente em qualquer chamada de rede, independentemente de instrumentação, pois faz parte do protocolo TCP/IP.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**4.** I. O indicador de nível de serviço (SLI) é definido pela equipe de negócio como uma meta aspiracional para a experiência do cliente, enquanto o objetivo de nível de serviço (SLO) é uma medição bruta e não normalizada do comportamento do sistema.

II. O SLI é uma medida quantitativa do comportamento observado do serviço, como a proporção de requisições bem-sucedidas, e o SLO é a meta definida para esse indicador ao longo de um período.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**5.** I. O orçamento de erro de um serviço aumenta automaticamente sempre que uma nova funcionalidade é implantada, independentemente do comportamento observado em produção.

II. A taxa de consumo do orçamento de erro (burn rate) é irrelevante para decisões operacionais, pois o único critério válido é o valor absoluto do SLO contratado.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

**6.** I. Em sistemas distribuídos, a pirâmide de testes recomenda uma base ampla de testes unitários e de contrato, com menor volume de testes de ponta a ponta.

II. Testes de ponta a ponta que atravessam múltiplos serviços reais tendem a ser mais lentos, mais frágeis e mais caros de manter do que testes unitários e de contrato isolados.

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**7.** I. Um teste de contrato entre o serviço de pedidos e o serviço de estoque verifica se ambos concordam com o formato e o significado das mensagens trocadas, sem exigir que os dois serviços estejam em execução simultânea.

II. Testes de contrato são normalmente definidos e mantidos em conjunto pelas equipes consumidora e provedora do serviço, reduzindo o risco de quebras não percebidas em produção.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**8.** I. Um experimento de caos bem projetado começa pela definição de uma hipótese de estado estável, isto é, uma expectativa mensurável do comportamento normal do sistema antes da falha injetada.

II. A hipótese de estado estável dispensa a coleta de métricas antes do experimento, pois seu único objetivo é observar o comportamento do sistema durante a falha.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**9.** I. O raio de impacto (blast radius) de um experimento de caos deve ser maximizado desde a primeira execução, para que a equipe obtenha o máximo de dados possível sobre o comportamento do sistema.

II. Limitar o raio de impacto de um experimento de caos, por exemplo restringindo-o a uma pequena fração do tráfego ou a um ambiente de testes, reduz o risco de causar uma indisponibilidade real para os clientes.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**10.** I. A cultura de postmortem sem culpa (blameless postmortem) tem como objetivo identificar e punir o indivíduo responsável pela falha, para reduzir a recorrência de erros semelhantes.

II. Registros de incidentes anteriores não devem influenciar o planejamento de novos experimentos de caos, pois cada falha é um evento estatisticamente independente das demais.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

**11.** I. O processamento em fluxo (streaming) permite que a NexaOrder avalie sinais de fraude à medida que os eventos de pedido chegam, em vez de esperar a formação de um lote completo.

II. Diferentemente do processamento em lote, o processamento em fluxo opera sobre um conjunto de dados potencialmente ilimitado, processando cada evento ou pequenos grupos de eventos assim que se tornam disponíveis.

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**12.** I. No modelo MapReduce, a fase de embaralhamento (shuffle) redistribui os pares intermediários entre os nós, agrupando-os pelas chaves antes da fase de redução.

II. O MapReduce foi originalmente descrito por Dean e Ghemawat como um modelo de programação para processamento paralelo de grandes volumes de dados em clusters.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**13.** I. Em processamento de fluxo, o tempo de evento (event time) corresponde ao instante em que o evento efetivamente ocorreu no domínio de negócio, podendo diferir do tempo de processamento no cluster.

II. Eventos que chegam fora de ordem ou atrasados nunca podem ser corretamente atribuídos a uma janela de tempo de evento, tornando o conceito de janela inútil na prática.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**14.** I. Uma função como serviço (FaaS) mantém sempre uma instância "quente" disponível, eliminando qualquer latência adicional na primeira execução após um período de ociosidade.

II. Quando uma função como serviço não possui instância ociosa disponível, a plataforma precisa inicializar um novo ambiente de execução antes de processar a requisição, fenômeno conhecido como inicialização a frio (cold start).

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**15.** I. A computação de borda elimina totalmente a necessidade de qualquer comunicação com uma região central de nuvem, pois todo o processamento passa a ocorrer exclusivamente no dispositivo do usuário.

II. O compromisso entre custo e latência na computação de borda favorece sempre o processamento na borda, independentemente do volume de dados ou da complexidade do processamento exigido.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

**16.** I. Atributos de qualidade como desempenho, disponibilidade, segurança e capacidade de manutenção influenciam a arquitetura da NexaOrder tanto quanto os requisitos funcionais explícitos do sistema.

II. Um requisito funcional descreve o que o sistema deve fazer, enquanto um atributo de qualidade descreve como o sistema deve se comportar sob determinadas condições, e frequentemente exige decisões arquiteturais específicas para ser satisfeito.

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**17.** I. Um registro de decisão arquitetural (ADR) documenta o contexto, a decisão tomada e as consequências previstas de uma escolha significativa de arquitetura, permitindo que decisões futuras sejam avaliadas à luz do que já foi decidido.

II. Ferramentas de controle de versão permitem armazenar arquivos de ADR junto ao código-fonte, possibilitando o rastreamento do histórico de decisões ao longo do tempo.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**18.** I. A análise de pontos únicos de falha (SPOF) da NexaOrder deve identificar componentes cuja indisponibilidade isolada comprometeria todo o fluxo de pedidos, mesmo que o restante do sistema esteja saudável.

II. Um componente redundante, com múltiplas réplicas ativas, nunca pode se tornar parte de um ponto único de falha, independentemente de como as réplicas estão distribuídas fisicamente ou de quais dependências compartilham.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**19.** I. O objetivo de tempo de recuperação (RTO) mede a quantidade máxima de dados que o negócio aceita perder em uma falha, enquanto o objetivo de ponto de recuperação (RPO) mede o tempo máximo aceitável para restaurar o serviço.

II. RTO e RPO são parâmetros que orientam decisões de replicação, backup e failover, pois traduzem tolerância de negócio a perda de dados e a indisponibilidade em metas técnicas mensuráveis.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**20.** I. Uma arquitetura distribuída bem projetada permanece ótima indefinidamente, sem exigir revisão de custos, capacidade ou decisões técnicas ao longo do tempo.

II. O custo de operação de um sistema distribuído é determinado exclusivamente pelo número de linhas de código do sistema, sendo independente de decisões de replicação, particionamento ou observabilidade.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

### Interpretação (questões 21 a 40)

**21.** A equipe da NexaOrder definiu um SLO mensal de 99,9% de disponibilidade para o serviço de checkout. Faltando 10 dias para o fim de um mês de 30 dias, o painel de observabilidade indica que 80% do orçamento de erro mensal já foi consumido. Diante desse cenário, qual conduta é mais consistente com a prática de engenharia de confiabilidade?

*a. Reduzir temporariamente a frequência de implantações arriscadas e priorizar correções de estabilidade até que a taxa de consumo do orçamento se estabilize, já que o ritmo atual de consumo é incompatível com o tempo restante do mês.
b. Ignorar o consumo do orçamento, pois o indicador só deve ser considerado no último dia do mês, quando o resultado final é conhecido.
c. Aumentar imediatamente o valor do SLO contratado para 99,99%, tornando o orçamento restante proporcionalmente maior.
d. Interpretar o consumo do orçamento como evidência de que o SLO foi definido de forma equivocada e deve ser abandonado.
e. Concluir que, como o serviço ainda está no ar, o consumo do orçamento de erro não representa risco algum para o restante do mês.

**22.** Um trace distribuído de uma requisição de compra na NexaOrder registrou os seguintes tempos de execução (spans): gateway, 15 ms; serviço de pedidos, 40 ms; serviço de estoque, 35 ms; serviço de pagamento, 310 ms; serviço de expedição, 20 ms, totalizando 420 ms. O objetivo de latência (SLO) definido para o fluxo completo é de p95 igual ou inferior a 300 ms. Com base exclusivamente nesse trace, qual é a conclusão mais adequada?

a. O gargalo está distribuído igualmente entre todos os serviços, portanto qualquer otimização isolada terá o mesmo impacto.
*b. O serviço de pagamento concentra a maior parcela da latência observada e deve ser o primeiro alvo de investigação, pois sua otimização tem o maior potencial de aproximar o fluxo do objetivo de 300 ms.
c. Como o gateway apresentou o menor tempo de execução, ele deve ser o primeiro componente investigado.
d. O trace não permite qualquer conclusão sobre onde investigar, pois latência de rede não pode ser medida por instrumentação.
e. A soma dos tempos indica falha do sistema de observabilidade, já que nenhum serviço deveria ultrapassar 300 ms individualmente.

**23.** O painel de métricas da NexaOrder mostra um aumento pontual na taxa de erros do fluxo de pedidos entre 18h e 19h, sem que nenhum serviço tenha sido reiniciado ou apresentado indisponibilidade total. A equipe deseja identificar a causa exata dentro dessa janela. Qual é a sequência de investigação mais adequada?

a. Ignorar as métricas, pois elas não são suficientes por si só, e reescrever o serviço de pagamento do zero como medida preventiva.
b. Aumentar o número de réplicas de todos os serviços, já que qualquer aumento de erro é sempre resolvido por mais capacidade computacional.
*c. Usar as métricas para delimitar a janela de tempo e os serviços afetados e, em seguida, examinar logs e traces correlacionados a requisições com falha registradas nesse intervalo, buscando um padrão comum entre elas.
d. Descartar os traces coletados no período, pois amostras estatísticas não representam adequadamente o comportamento real do sistema.
e. Aguardar o próximo incidente idêntico antes de investigar, pois dados históricos não têm valor diagnóstico em sistemas distribuídos.

**24.** A equipe de plataforma da NexaOrder propõe definir a utilização média de CPU dos servidores como o principal indicador de nível de serviço (SLI) do fluxo de checkout, argumentando que o valor é fácil de coletar. Do ponto de vista da prática de definição de SLIs orientados à experiência do cliente, qual é a avaliação mais adequada dessa proposta?

a. A proposta é adequada, pois qualquer métrica de infraestrutura reflete diretamente a experiência do cliente.
b. A proposta é adequada, mas apenas se a utilização de CPU for medida em todos os data centers simultaneamente.
c. A proposta é inadequada porque a utilização de CPU não pode ser coletada por nenhuma ferramenta de observabilidade atual.
*d. A proposta é inadequada porque a utilização de CPU é uma métrica interna de recurso, que pode permanecer baixa mesmo quando pedidos falham ou demoram além do aceitável, não capturando diretamente a experiência do usuário; um SLI mais adequado seria, por exemplo, a proporção de requisições de checkout concluídas com sucesso dentro de um limite de latência.
e. A proposta é inadequada porque SLIs só podem ser definidos para serviços que não utilizam contêineres.

**25.** Ao investigar um pedido da NexaOrder que passou por comunicação síncrona (API) e, em seguida, por um evento assíncrono publicado em um tópico consumido pelo serviço de expedição, a equipe percebeu que o trace se interrompe no limite entre a chamada HTTP e a publicação do evento, impedindo a reconstrução do caminho completo. Qual é a causa mais provável e a correção adequada?

a. Traces distribuídos não podem, por definição, atravessar sistemas de mensageria, sendo essa uma limitação permanente da abordagem.
b. O problema ocorre porque o serviço de expedição está implementado em uma linguagem diferente da usada pelo serviço de pedidos, e traces não funcionam entre linguagens distintas.
c. O problema é irrelevante, pois cada serviço deve ser observado de forma totalmente independente, sem qualquer necessidade de correlação entre eles.
d. A correção adequada é abandonar a mensageria assíncrona e substituí-la integralmente por chamadas síncronas, eliminando o problema de propagação de contexto.
*e. O contexto de rastreamento provavelmente não está sendo propagado nos metadados/cabeçalhos da mensagem publicada; a correção adequada é instrumentar o produtor para incluir o contexto de rastreamento no cabeçalho do evento e o consumidor para extraí-lo ao processar a mensagem, preservando a continuidade do trace.

**26.** O serviço de pedidos da NexaOrder alterou, sem aviso prévio, o nome de um campo em um evento publicado, o que quebrou a lógica do serviço de estoque em produção. As equipes trabalham de forma independente e não compartilham o mesmo repositório de código. Qual prática de teste teria maior probabilidade de detectar esse problema antes da implantação em produção?

*a. Testes de contrato orientados pelo consumidor, em que o serviço de estoque define expectativas sobre o formato do evento e o serviço de pedidos verifica, em seu próprio pipeline, se essas expectativas continuam sendo atendidas antes de publicar uma nova versão.
b. Testes unitários exclusivamente no serviço de pedidos, sem qualquer conhecimento do formato esperado pelos consumidores.
c. Testes de carga executados uma vez por trimestre em ambiente de homologação.
d. Testes manuais exploratórios realizados apenas pela equipe de pedidos, sem participação da equipe de estoque.
e. Testes de penetração de segurança focados exclusivamente em autenticação e autorização.

**27.** A equipe de confiabilidade da NexaOrder planeja três experimentos distintos: (1) manter o sistema sob a carga máxima esperada em um dia de promoção por 24 horas contínuas, para observar vazamentos de memória e degradação gradual; (2) aumentar a carga progressivamente além do esperado até que o sistema apresente falha, para identificar seu limite; (3) validar se o sistema sustenta o tráfego típico de um dia normal sem violar o SLO de latência. Quais são, respectivamente, os tipos de teste mais adequados para os três experimentos?

a. Teste de contrato; teste de penetração; teste unitário.
*b. Teste de duração (soak test); teste de estresse; teste de carga.
c. Teste de estresse; teste de duração; teste de contrato.
d. Teste de carga; teste unitário; teste de duração.
e. Teste de penetração; teste de carga; teste de estresse.

**28.** A equipe da NexaOrder está formulando um experimento de engenharia do caos para avaliar o comportamento do sistema diante da indisponibilidade momentânea do provedor de pagamento. Qual das alternativas a seguir representa uma hipótese de estado estável corretamente formulada para esse experimento?

a. "O sistema não deve, em hipótese alguma, apresentar qualquer erro durante o experimento, mesmo diante da indisponibilidade simulada do provedor de pagamento."
b. "A equipe espera que algo aconteça de diferente durante o experimento, mas não é possível prever o quê."
*c. "Em condições normais, a taxa de conclusão de pedidos permanece acima de 98% e a latência p95 do checkout permanece abaixo de 400 ms; durante a indisponibilidade simulada do provedor de pagamento, o circuito de proteção deve ser acionado, o sistema deve degradar graciosamente informando o cliente, e a taxa de conclusão de pedidos não deve cair abaixo de 90%."
d. "O experimento será considerado bem-sucedido se nenhuma métrica for coletada durante sua execução, evitando resultados tendenciosos."
e. "Como o serviço de pagamento já foi testado manualmente uma vez, não é necessário formular qualquer hipótese antes do experimento."

**29.** Ao planejar o experimento de indisponibilidade do serviço de pagamento, a equipe da NexaOrder precisa decidir como limitar o risco para os clientes reais. Qual configuração representa a aplicação mais adequada dos princípios de raio de impacto controlado e mecanismo de interrupção?

a. Executar o experimento em produção, afetando 100% do tráfego real, sem qualquer possibilidade de interromper a injeção de falha antes do horário previamente agendado.
b. Executar o experimento apenas em ambiente de desenvolvimento local, isolado de qualquer característica realista de produção, e considerar os resultados diretamente aplicáveis ao ambiente de produção.
c. Executar o experimento afetando aleatoriamente qualquer serviço do sistema, sem relação com a hipótese formulada sobre o provedor de pagamento.
*d. Executar o experimento inicialmente afetando uma pequena fração do tráfego real ou um subconjunto controlado de instâncias, com um mecanismo que permita interromper imediatamente a injeção de falha caso os indicadores de negócio ultrapassem um limite predefinido de degradação.
e. Executar o experimento apenas quando o tráfego estiver em seu pico histórico máximo, para maximizar a relevância estatística dos resultados.

**30.** Após um incidente real em que a indisponibilidade do provedor de pagamento causou falhas em cascata na NexaOrder, a equipe conduz um postmortem. Qual conduta está mais alinhada com a prática de aprendizagem operacional sem culpabilização (blameless postmortem)?

a. Identificar o funcionário responsável pela configuração do circuito de proteção e aplicar uma medida disciplinar formal.
b. Encerrar o postmortem assim que a causa imediata for identificada, sem documentar ações de acompanhamento.
c. Restringir o acesso ao relatório do postmortem apenas à liderança técnica, para evitar constrangimento das pessoas envolvidas.
d. Concluir que o incidente foi resultado de erro humano isolado e que nenhuma mudança sistêmica é necessária.
*e. Reconstruir a linha do tempo do incidente, identificar fatores contribuintes sistêmicos (como ausência de teste de contrato ou de raio de impacto limitado em experimentos anteriores), documentar ações de melhoria com responsáveis e prazos, e compartilhar o aprendizado com toda a organização.

**31.** A NexaOrder deseja detectar padrões suspeitos de fraude (por exemplo, múltiplas tentativas de compra com cartões diferentes em poucos segundos a partir do mesmo dispositivo) antes que o pedido seja aprovado. A equipe avalia duas alternativas: um pipeline de processamento em lote executado a cada hora, ou um pipeline de processamento em fluxo que avalia cada evento de tentativa de compra assim que ele ocorre. Qual alternativa atende melhor ao requisito de negócio descrito e por quê?

*a. O processamento em fluxo é mais adequado, pois a decisão de aprovar ou bloquear o pedido precisa ocorrer em segundos, e um pipeline em lote executado a cada hora não teria informação atualizada a tempo de impedir a fraude antes da aprovação.
b. O processamento em lote é mais adequado, pois lotes horários garantem maior precisão estatística do que qualquer processamento evento a evento.
c. As duas alternativas são equivalentes, pois a janela de tempo entre eventos não influencia a eficácia da detecção de fraude.
d. Nenhuma das alternativas é adequada, pois a detecção de fraude não pode ser automatizada em sistemas distribuídos.
e. O processamento em lote é mais adequado, pois elimina totalmente a necessidade de particionamento e tolerância a falhas.

**32.** Durante a execução de um job de processamento em lote sobre o histórico de pedidos da NexaOrder, um dos nós responsáveis pela fase de redução falha antes de concluir seu trabalho. Considerando o modelo MapReduce e frameworks de DAG modernos inspirados nele, qual é o comportamento esperado do sistema?

a. Todo o cluster deve ser reiniciado manualmente, pois o modelo não prevê nenhuma forma de recuperação automática.
*b. O framework deve identificar a tarefa de redução malsucedida e reatribuí-la a outro nó disponível, reexecutando-a a partir dos dados intermediários já persistidos ou reprocessados pelas tarefas de mapeamento correspondentes, sem exigir intervenção manual para esse tipo de falha isolada.
c. O job deve ser cancelado definitivamente, e todo o histórico de pedidos deve ser reprocessado manualmente linha a linha.
d. A falha de um único nó de redução é sempre ignorada, e o resultado final é produzido sem os dados desse nó, sem qualquer inconsistência.
e. O modelo MapReduce não é capaz de lidar com falhas de nós, sendo essa uma limitação exclusiva de frameworks mais recentes baseados em DAGs.

**33.** Um evento de confirmação de pagamento da NexaOrder foi gerado às 14h00 (tempo de evento), mas, devido a uma instabilidade de rede, só chegou ao pipeline de processamento em fluxo às 14h07 (tempo de processamento). O pipeline calcula, em janelas de um minuto baseadas em tempo de evento, o volume de pagamentos aprovados por minuto. Qual mecanismo permite que esse pipeline ainda atribua corretamente o evento atrasado à janela das 14h00–14h01, dentro de um limite configurado de tolerância?

a. Reinicialização completa do pipeline a cada evento atrasado recebido.
b. Descarte automático e definitivo de qualquer evento que não chegue na ordem exata de geração.
*c. Uso de marcas d'água (watermarks) e de uma tolerância configurável a atraso (allowed lateness), que mantêm a janela correspondente ao tempo de evento aberta por um período adicional antes de ser considerada definitivamente fechada.
d. Substituição do tempo de evento pelo tempo de processamento em todos os cálculos, eliminando a necessidade de qualquer tratamento especial.
e. Processamento exclusivamente em lote, pois pipelines de fluxo não conseguem lidar com eventos fora de ordem.

**34.** A NexaOrder precisa processar um evento esporádico e de curta duração: enviar uma notificação por e-mail sempre que um pedido é confirmado, com volume variável e picos apenas em datas promocionais. Do ponto de vista de compromissos entre modelo de execução, custo e latência, qual avaliação é mais adequada para a escolha entre uma função como serviço (FaaS) e um serviço de longa duração dedicado?

a. O serviço de longa duração é sempre superior, pois FaaS não pode ser acionado por eventos.
b. A FaaS é inadequada, pois funções como serviço não podem, em nenhuma hipótese, processar eventos assíncronos.
c. Ambos os modelos são idênticos em custo e desempenho, tornando a escolha irrelevante.
*d. A FaaS tende a ser adequada para essa carga esporádica e de curta duração, pois o modelo cobra por execução e escala automaticamente com picos, embora seja necessário considerar a latência adicional de inicialização a frio (cold start) em invocações após períodos de ociosidade.
e. O serviço de longa duração elimina completamente qualquer custo de infraestrutura, tornando-se sempre a opção mais barata.

**35.** A NexaOrder avalia executar parte da análise de fraude diretamente em pontos de borda próximos aos dispositivos dos clientes, em vez de centralizar todo o processamento em uma região de nuvem. Qual consideração melhor descreve o compromisso entre custo e latência nessa decisão?

a. A computação de borda deve ser adotada integralmente, pois elimina por completo a necessidade de qualquer processamento central, independentemente da complexidade do modelo de fraude.
b. A computação de borda não deve ser considerada, pois qualquer processamento fora de uma região central de nuvem é, por definição, inseguro.
c. A latência é irrelevante para decisões de detecção de fraude, tornando desnecessária qualquer análise de localização de dados.
d. O custo de operação em pontos de borda é sempre inferior ao custo de uma região central de nuvem, independentemente do volume de dispositivos atendidos.
*e. A decisão deve ponderar a redução de latência obtida ao processar sinais simples próximos ao cliente contra o custo e a complexidade operacional de manter lógica distribuída em múltiplos pontos de borda, reservando modelos mais complexos ou que dependam de contexto histórico amplo para o processamento centralizado.

**36.** Ao revisar a arquitetura final da NexaOrder, a equipe percebe que dois requisitos de qualidade entram em tensão: o time de produto deseja reduzir ao máximo a latência de exibição do catálogo, enquanto o time de confiabilidade exige garantias mais fortes de consistência no saldo de estoque exibido ao cliente. Qual conduta melhor reflete uma avaliação arquitetural madura desse compromisso?

*a. Explicitar o compromisso entre latência e consistência para cada parte do sistema separadamente, aceitando, por exemplo, leituras eventualmente consistentes no catálogo, mas exigindo consistência mais forte no momento da confirmação da reserva de estoque durante o checkout.
b. Exigir consistência forte em toda a aplicação, sem exceção, pois qualquer leitura desatualizada é sempre inaceitável, independentemente do contexto de uso.
c. Ignorar completamente o requisito de latência do catálogo, pois atributos de qualidade não têm relevância arquitetural comparável aos requisitos funcionais.
d. Resolver o conflito escolhendo aleatoriamente entre os dois times, sem qualquer análise técnica dos compromissos envolvidos.
e. Concluir que, como os dois requisitos entram em tensão, um deles deve ser eliminado do sistema.

**37.** Ao compilar os registros de decisão arquitetural (ADRs) da NexaOrder ao longo das quatro unidades, a equipe encontra um documento que afirma apenas: "Decidimos usar Kubernetes." Do ponto de vista das boas práticas de documentação arquitetural discutidas na disciplina, qual é a avaliação mais adequada desse registro?

a. O registro está completo, pois um ADR deve conter apenas o nome da tecnologia escolhida, sem qualquer justificativa adicional.
*b. O registro está incompleto, pois um ADR deve também explicitar o contexto que motivou a decisão, as alternativas consideradas e as consequências esperadas, elementos ausentes nesse exemplo.
c. O registro é desnecessário, pois decisões de orquestração de contêineres não precisam ser documentadas.
d. O registro deveria ter sido feito apenas pela equipe de segurança, e não pela equipe de infraestrutura.
e. O registro está completo, desde que seja armazenado em uma ferramenta de gestão de projetos, independentemente do conteúdo textual.

**38.** Na revisão final da NexaOrder, a equipe descreve a seguinte configuração: o serviço de pagamento possui três réplicas distribuídas em três zonas de disponibilidade distintas, mas todas as réplicas dependem de uma única instância do sistema de mensageria, hospedada em apenas uma zona, sem réplicas configuradas. Qual é a conclusão mais adequada sobre pontos únicos de falha nessa configuração?

a. Não existe ponto único de falha, pois o serviço de pagamento em si está replicado em três zonas.
b. O ponto único de falha está nas réplicas do serviço de pagamento, e não no sistema de mensageria.
*c. O sistema de mensageria não replicado constitui um ponto único de falha, pois sua indisponibilidade pode impedir a comunicação entre os serviços mesmo com o serviço de pagamento saudável em suas três réplicas.
d. A configuração é adequada, pois três réplicas de qualquer componente eliminam automaticamente qualquer ponto único de falha do sistema como um todo.
e. Pontos únicos de falha só podem existir em bancos de dados, nunca em sistemas de mensageria.

**39.** A NexaOrder replica de forma assíncrona o banco de dados de pedidos para uma região secundária a cada 5 minutos, e o plano de recuperação prevê que a equipe consiga promover a região secundária e restabelecer o serviço em até 15 minutos após um desastre na região primária. Nesse cenário, quais são, respectivamente, o RPO e o RTO aproximados do plano descrito?

a. RPO de 15 minutos e RTO de 5 minutos.
b. RPO e RTO são ambos indefinidos, pois não é possível estimá-los sem um desastre real.
c. RPO de 0 minutos e RTO de 0 minutos, pois a replicação assíncrona garante recuperação instantânea.
*d. RPO de aproximadamente 5 minutos, correspondente à possível perda de dados entre a última replicação bem-sucedida e o desastre, e RTO de aproximadamente 15 minutos, correspondente ao tempo necessário para restabelecer o serviço.
e. RPO de 5 minutos e RTO de 5 minutos, pois ambos os indicadores são sempre iguais ao intervalo de replicação.

**40.** Passados alguns meses da implantação da arquitetura final, a equipe da NexaOrder percebe que o número de instâncias provisionadas para o pico de tráfego permanece constante mesmo em horários de baixíssima demanda, gerando custo elevado sem benefício correspondente de desempenho ou confiabilidade. Qual conduta está mais alinhada com uma visão madura de custo, sustentabilidade e evolução arquitetural?

a. Manter a capacidade fixa indefinidamente, pois qualquer redução de instâncias representa risco inaceitável, independentemente dos dados de utilização observados.
b. Eliminar toda a redundância do sistema imediatamente, retornando a uma única instância para reduzir custo ao mínimo possível.
c. Ignorar o custo observado, pois atributos de qualidade como desempenho e disponibilidade nunca devem ser avaliados em conjunto com custo.
d. Revisar apenas o custo da equipe de desenvolvimento, sem considerar o custo de infraestrutura como parte da avaliação arquitetural.
*e. Revisar a estratégia de capacidade com base em dados reais de utilização, adotando mecanismos de escalonamento automático que ajustem o número de instâncias à demanda observada, preservando as metas de disponibilidade e desempenho definidas para os cenários de pico.

## Gabarito e feedbacks

**Questão 1** (correta: a)
- a. Correta: I é verdadeira — monitoramento baseado em condições conhecidas não cobre falhas inéditas — e II justifica diretamente essa limitação, ao descrever como a observabilidade permite investigar perguntas não antecipadas.
- b. Incorreta: II não é apenas verdadeira, ela explica exatamente por que I é verdadeira.
- c. Incorreta: II também é verdadeira, não falsa; observabilidade de fato dispensa a criação prévia de um painel específico para cada falha.
- d. Incorreta: I é verdadeira, não falsa; monitoramento tradicional é, de fato, insuficiente para falhas inéditas.
- e. Incorreta: ambas as asserções são verdadeiras, não falsas.

**Questão 2** (correta: b)
- a. Incorreta: II é verdadeira, mas descreve apenas a natureza das métricas, sem explicar por que os três pilares são complementares entre si.
- b. Correta: ambas são verdadeiras, mas II apenas define métricas, sem justificar a complementaridade entre métricas, logs e traces afirmada em I.
- c. Incorreta: II também é verdadeira, não falsa; a definição de métricas apresentada está correta.
- d. Incorreta: I é verdadeira, não falsa; os três pilares são de fato complementares.
- e. Incorreta: ambas as asserções são verdadeiras.

**Questão 3** (correta: c)
- a. Incorreta: II é falsa, não verdadeira; propagação de contexto não é automática nem faz parte do protocolo TCP/IP.
- b. Incorreta: II é falsa, portanto não pode ser uma justificativa verdadeira, ainda que não correta, de I.
- c. Correta: I é verdadeira — o trace ID propagado permite reconstruir o caminho da requisição — e II é falsa, pois a propagação exige instrumentação explícita em cada serviço, não ocorre automaticamente por protocolo de rede.
- d. Incorreta: I é verdadeira, não falsa.
- e. Incorreta: I é verdadeira, não falsa.

**Questão 4** (correta: d)
- a. Incorreta: I é falsa, não verdadeira; as definições de SLI e SLO estão trocadas em relação ao conceito correto.
- b. Incorreta: I é falsa, portanto essa alternativa não se aplica.
- c. Incorreta: II é verdadeira, não falsa; ela apresenta corretamente as definições de SLI e SLO.
- d. Correta: I é falsa — inverte as definições de SLI e SLO — e II é verdadeira, apresentando corretamente o SLI como medida quantitativa observada e o SLO como meta definida para esse indicador.
- e. Incorreta: II é verdadeira, não falsa.

**Questão 5** (correta: e)
- a. Incorreta: ambas as asserções são falsas, não verdadeiras.
- b. Incorreta: ambas as asserções são falsas.
- c. Incorreta: I também é falsa, não verdadeira; o orçamento de erro não aumenta automaticamente com implantações, ele é consumido por falhas observadas.
- d. Incorreta: II também é falsa, não verdadeira; a taxa de consumo do orçamento (burn rate) é altamente relevante para decisões operacionais.
- e. Correta: I é falsa, pois o orçamento de erro é consumido por falhas reais observadas em produção, não aumentado por implantações; II é falsa, pois a taxa de consumo do orçamento é um dos principais insumos para decisões operacionais, como pausar implantações arriscadas.

**Questão 6** (correta: a)
- a. Correta: ambas as asserções são verdadeiras, e II justifica diretamente I, explicando por que a pirâmide recomenda uma base ampla de testes mais baratos e uma menor proporção de testes de ponta a ponta.
- b. Incorreta: II de fato justifica I, não é uma relação sem nexo lógico.
- c. Incorreta: II também é verdadeira, não falsa; testes de ponta a ponta realmente tendem a ser mais lentos e frágeis.
- d. Incorreta: I é verdadeira, não falsa; essa é exatamente a recomendação da pirâmide de testes em sistemas distribuídos.
- e. Incorreta: ambas as asserções são verdadeiras.

**Questão 7** (correta: b)
- a. Incorreta: II é verdadeira, mas não justifica diretamente a afirmação de I sobre não exigir execução simultânea dos dois serviços.
- b. Correta: ambas as asserções são verdadeiras, mas II trata da governança colaborativa dos contratos, enquanto I trata da independência de execução entre os serviços — não há relação de justificativa direta entre elas.
- c. Incorreta: II também é verdadeira, não falsa.
- d. Incorreta: I é verdadeira, não falsa; essa é justamente a vantagem central dos testes de contrato.
- e. Incorreta: ambas as asserções são verdadeiras.

**Questão 8** (correta: c)
- a. Incorreta: II é falsa, não verdadeira; a hipótese de estado estável depende, sim, de métricas coletadas antes do experimento para servir de referência.
- b. Incorreta: II é falsa, portanto não pode justificar I.
- c. Correta: I é verdadeira — a hipótese de estado estável é o ponto de partida de um experimento bem projetado — e II é falsa, pois a coleta prévia de métricas é justamente o que permite comparar o comportamento antes e durante a falha injetada.
- d. Incorreta: I é verdadeira, não falsa.
- e. Incorreta: I é verdadeira, não falsa.

**Questão 9** (correta: d)
- a. Incorreta: I é falsa, não verdadeira; a prática recomendada é começar com raio de impacto limitado, não maximizado.
- b. Incorreta: I é falsa, portanto essa alternativa não se aplica.
- c. Incorreta: II é verdadeira, não falsa.
- d. Correta: I é falsa, pois maximizar o raio de impacto na primeira execução contraria a prática responsável de engenharia do caos; II é verdadeira, pois limitar o raio de impacto de fato reduz o risco de indisponibilidade real para os clientes.
- e. Incorreta: II é verdadeira, não falsa.

**Questão 10** (correta: e)
- a. Incorreta: ambas as asserções são falsas, não verdadeiras.
- b. Incorreta: ambas as asserções são falsas.
- c. Incorreta: I também é falsa; o objetivo do postmortem sem culpa é justamente evitar a identificação e punição de indivíduos, focando em causas sistêmicas.
- d. Incorreta: II também é falsa; incidentes anteriores devem, sim, influenciar o planejamento de novos experimentos, pois raramente são estatisticamente independentes em sistemas com dependências compartilhadas.
- e. Correta: I é falsa, pois o postmortem sem culpa busca causas sistêmicas, não a punição de indivíduos; II é falsa, pois o histórico de incidentes é justamente um dos principais insumos para planejar novos experimentos de caos com foco nos riscos já conhecidos.

**Questão 11** (correta: a)
- a. Correta: ambas as asserções são verdadeiras, e II justifica diretamente I, explicando a característica do processamento em fluxo (dados ilimitados, processados assim que disponíveis) que o torna adequado à avaliação em tempo quase real.
- b. Incorreta: II de fato justifica I nesse caso.
- c. Incorreta: II também é verdadeira, não falsa; essa é a definição correta de processamento em fluxo.
- d. Incorreta: I é verdadeira, não falsa; o processamento em fluxo de fato permite essa avaliação contínua.
- e. Incorreta: ambas as asserções são verdadeiras.

**Questão 12** (correta: b)
- a. Incorreta: II é verdadeira, mas não justifica diretamente o mecanismo descrito em I; trata de autoria histórica, não do funcionamento do shuffle.
- b. Correta: ambas as asserções são verdadeiras, mas II é um fato histórico sobre a origem do modelo, enquanto I descreve um mecanismo interno — não há relação de justificativa direta entre elas.
- c. Incorreta: II também é verdadeira, não falsa; o MapReduce foi de fato descrito por Dean e Ghemawat.
- d. Incorreta: I é verdadeira, não falsa; essa é a definição correta da fase de embaralhamento.
- e. Incorreta: ambas as asserções são verdadeiras.

**Questão 13** (correta: c)
- a. Incorreta: II é falsa, não verdadeira; eventos atrasados podem, sim, ser corretamente atribuídos a janelas por meio de marcas d'água e tolerância a atraso.
- b. Incorreta: II é falsa, portanto não pode justificar I.
- c. Correta: I é verdadeira — tempo de evento pode diferir do tempo de processamento — e II é falsa, pois mecanismos como marcas d'água e tolerância configurável a atraso permitem atribuir corretamente eventos atrasados às janelas certas, sem tornar o conceito de janela inútil.
- d. Incorreta: I é verdadeira, não falsa.
- e. Incorreta: I é verdadeira, não falsa.

**Questão 14** (correta: d)
- a. Incorreta: I é falsa, não verdadeira; FaaS não mantém sempre uma instância quente, por isso existe o fenômeno de inicialização a frio.
- b. Incorreta: I é falsa, portanto essa alternativa não se aplica.
- c. Incorreta: II é verdadeira, não falsa.
- d. Correta: I é falsa, pois a ausência de instância quente é justamente o que caracteriza a inicialização a frio; II é verdadeira, descrevendo corretamente o fenômeno de cold start quando não há instância ociosa disponível.
- e. Incorreta: II é verdadeira, não falsa.

**Questão 15** (correta: e)
- a. Incorreta: ambas as asserções são falsas, não verdadeiras.
- b. Incorreta: ambas as asserções são falsas.
- c. Incorreta: I também é falsa; a computação de borda não elimina totalmente a comunicação com uma região central, especialmente para lógica que depende de contexto histórico amplo.
- d. Incorreta: II também é falsa; o compromisso entre custo e latência não favorece sempre a borda, dependendo do volume e da complexidade do processamento.
- e. Correta: I é falsa, pois a computação de borda tipicamente complementa, e não elimina, a comunicação com uma região central; II é falsa, pois a escolha entre borda e processamento central depende do volume de dados e da complexidade exigida, não havendo favorecimento absoluto da borda.

**Questão 16** (correta: a)
- a. Correta: ambas as asserções são verdadeiras, e II justifica diretamente I, explicando por que atributos de qualidade têm peso arquitetural comparável ao dos requisitos funcionais — eles frequentemente exigem decisões de projeto específicas.
- b. Incorreta: II de fato justifica I nesse caso.
- c. Incorreta: II também é verdadeira, não falsa; essa é a distinção correta entre requisito funcional e atributo de qualidade.
- d. Incorreta: I é verdadeira, não falsa; atributos de qualidade realmente influenciam a arquitetura tanto quanto requisitos funcionais.
- e. Incorreta: ambas as asserções são verdadeiras.

**Questão 17** (correta: b)
- a. Incorreta: II é verdadeira, mas trata de uma questão de ferramental de armazenamento, não justificando diretamente o conteúdo que um ADR deve documentar, afirmado em I.
- b. Correta: ambas as asserções são verdadeiras, mas II descreve uma prática de armazenamento de ADRs, enquanto I descreve o conteúdo que um ADR deve conter — não há relação de justificativa direta entre elas.
- c. Incorreta: II também é verdadeira, não falsa; ferramentas de versionamento realmente permitem esse rastreamento.
- d. Incorreta: I é verdadeira, não falsa; essa é a definição correta de um ADR completo.
- e. Incorreta: ambas as asserções são verdadeiras.

**Questão 18** (correta: c)
- a. Incorreta: II é falsa, não verdadeira; um componente com múltiplas réplicas pode, sim, fazer parte de um ponto único de falha, se todas as réplicas compartilharem uma dependência não replicada.
- b. Incorreta: II é falsa, portanto não pode ser uma justificativa, correta ou não, de I.
- c. Correta: I é verdadeira — a análise de SPOF deve identificar componentes cuja indisponibilidade isolada compromete todo o fluxo — e II é falsa, pois réplicas distribuídas fisicamente ainda podem compartilhar uma dependência não replicada, tornando-se, em conjunto, parte de um ponto único de falha.
- d. Incorreta: I é verdadeira, não falsa.
- e. Incorreta: I é verdadeira, não falsa.

**Questão 19** (correta: d)
- a. Incorreta: I é falsa, não verdadeira; as definições de RTO e RPO estão trocadas em relação ao conceito correto.
- b. Incorreta: I é falsa, portanto essa alternativa não se aplica.
- c. Incorreta: II é verdadeira, não falsa; RTO e RPO de fato orientam decisões de replicação, backup e failover.
- d. Correta: I é falsa, pois inverte as definições — RPO mede perda de dados tolerável e RTO mede tempo de recuperação tolerável; II é verdadeira, descrevendo corretamente o papel de RTO e RPO como metas técnicas mensuráveis derivadas de tolerância de negócio.
- e. Incorreta: II é verdadeira, não falsa.

**Questão 20** (correta: e)
- a. Incorreta: ambas as asserções são falsas, não verdadeiras.
- b. Incorreta: ambas as asserções são falsas.
- c. Incorreta: I também é falsa; nenhuma arquitetura permanece ótima indefinidamente sem revisão de custo, capacidade e decisões técnicas.
- d. Incorreta: II também é falsa; o custo de operação depende fortemente de decisões de replicação, particionamento e observabilidade, não apenas do número de linhas de código.
- e. Correta: I é falsa, pois toda arquitetura distribuída exige revisão contínua de custo, capacidade e decisões técnicas ao longo do tempo; II é falsa, pois o custo de operação é diretamente influenciado por decisões de replicação, particionamento e observabilidade, não apenas pelo tamanho do código.

**Questão 21** (correta: a)
- a. Correta: reduzir o ritmo de mudanças arriscadas é a resposta operacional adequada quando a taxa de consumo do orçamento de erro está incompatível com o tempo restante do período de medição.
- b. Incorreta: o orçamento de erro deve ser monitorado continuamente, não apenas avaliado ao final do período de medição.
- c. Incorreta: alterar o valor do SLO contratado é uma decisão de produto e negócio, que não deve ser tomada unilateralmente como reação operacional imediata a um consumo elevado.
- d. Incorreta: consumo elevado do orçamento não indica, por si só, que o SLO foi definido de forma equivocada, apenas que o comportamento observado está fora do esperado para o período.
- e. Incorreta: o fato de o serviço continuar no ar não elimina o risco de violar o SLO se o ritmo de consumo do orçamento se mantiver.

**Questão 22** (correta: b)
- a. Incorreta: o gargalo está concentrado no serviço de pagamento (310 ms de 420 ms, cerca de 74% do total), não distribuído igualmente.
- b. Correta: o serviço de pagamento concentra a maior parte da latência observada, tornando-se o alvo prioritário de investigação para aproximar o fluxo do objetivo de 300 ms.
- c. Incorreta: o menor tempo de execução não é critério de prioridade de investigação; o objetivo é reduzir a latência total.
- d. Incorreta: exatamente o contrário é verdadeiro — traces distribuídos são projetados para permitir esse tipo de conclusão sobre onde investigar.
- e. Incorreta: o SLO se aplica ao fluxo completo, não exige que cada serviço individualmente fique abaixo de 300 ms, e a soma dos tempos não indica falha do sistema de observabilidade.

**Questão 23** (correta: c)
- a. Incorreta: descartar métricas e reescrever um serviço inteiro sem investigação prévia é uma medida desproporcional e não baseada em evidência.
- b. Incorreta: aumentar réplicas não resolve necessariamente a causa raiz de um aumento correlacionado de erros em uma janela específica, além de gerar custo desnecessário.
- c. Correta: usar métricas para delimitar escopo e, em seguida, aprofundar com logs e traces correlacionados é o fluxo de investigação recomendado pela prática de observabilidade.
- d. Incorreta: traces coletados no período são justamente os dados mais úteis para identificar um padrão comum entre as requisições com falha.
- e. Incorreta: dados históricos têm valor diagnóstico significativo e não é necessário aguardar a recorrência do incidente para investigar.

**Questão 24** (correta: d)
- a. Incorreta: métricas de infraestrutura não refletem diretamente a experiência do cliente; um serviço pode falhar sem que a CPU se eleve.
- b. Incorreta: medir CPU em todos os data centers não resolve a limitação fundamental de a métrica não capturar a experiência do usuário.
- c. Incorreta: a utilização de CPU pode, sim, ser coletada por praticamente qualquer ferramenta de observabilidade atual; esse não é o problema da proposta.
- d. Correta: CPU é uma métrica interna de recurso que não captura diretamente falhas ou lentidão percebidas pelo usuário; um SLI orientado à experiência do cliente, como taxa de sucesso dentro de um limite de latência, é mais adequado.
- e. Incorreta: a definição de SLIs não depende do uso ou não de contêineres.

**Questão 25** (correta: e)
- a. Incorreta: traces distribuídos podem, sim, atravessar sistemas de mensageria, desde que o contexto seja propagado nos metadados da mensagem.
- b. Incorreta: a linguagem de implementação do serviço consumidor não é a causa da interrupção do trace; o problema está na propagação do contexto, não na linguagem.
- c. Incorreta: a correlação entre serviços é justamente o que permite investigar o caminho completo de uma requisição; não é irrelevante.
- d. Incorreta: abandonar a mensageria assíncrona é uma medida desproporcional que sacrifica benefícios arquiteturais para contornar um problema de instrumentação, corrigível de forma mais simples.
- e. Correta: o problema mais provável é a ausência de propagação do contexto de rastreamento nos metadados da mensagem; a correção adequada envolve instrumentar produtor e consumidor para incluir e extrair esse contexto.

**Questão 26** (correta: a)
- a. Correta: testes de contrato orientados pelo consumidor detectam justamente esse tipo de incompatibilidade de esquema entre equipes independentes, antes da implantação em produção.
- b. Incorreta: testes unitários isolados no serviço de pedidos, sem conhecimento do contrato esperado pelo consumidor, não detectariam essa quebra específica.
- c. Incorreta: testes de carga trimestrais não são projetados para detectar incompatibilidades de esquema entre serviços.
- d. Incorreta: testes manuais exploratórios feitos apenas por uma das equipes, sem a participação da equipe consumidora, dificilmente identificariam essa quebra de contrato.
- e. Incorreta: testes de penetração de segurança têm outro escopo e não avaliam compatibilidade de esquema de eventos.

**Questão 27** (correta: b)
- a. Incorreta: nenhum dos três tipos de teste mencionados nessa alternativa corresponde aos experimentos descritos.
- b. Correta: teste de duração corresponde à observação de degradação ao longo de 24 horas; teste de estresse corresponde ao aumento progressivo até a falha; teste de carga corresponde à validação do tráfego típico sem violar o SLO.
- c. Incorreta: a correspondência está trocada entre os experimentos e os tipos de teste.
- d. Incorreta: nenhum dos tipos mencionados corresponde corretamente aos três experimentos descritos.
- e. Incorreta: teste de penetração e teste de carga não correspondem, respectivamente, ao primeiro e ao segundo experimento descritos.

**Questão 28** (correta: c)
- a. Incorreta: uma hipótese que exige ausência total de erro não é mensurável de forma realista e não reflete o objetivo de observar degradação graciosa sob falha controlada.
- b. Incorreta: uma hipótese vaga, sem previsão mensurável, não cumpre o requisito de ser uma expectativa específica e verificável.
- c. Correta: a hipótese apresentada é mensurável, específica, e define tanto o comportamento normal quanto o comportamento esperado durante a falha injetada, incluindo limites numéricos verificáveis.
- d. Incorreta: a ausência de coleta de métricas impede qualquer verificação da hipótese, contrariando o propósito do experimento.
- e. Incorreta: um teste manual anterior não substitui a formulação de uma hipótese de estado estável mensurável para o experimento específico.

**Questão 29** (correta: d)
- a. Incorreta: afetar 100% do tráfego real sem mecanismo de interrupção viola tanto o princípio de raio de impacto limitado quanto o de interrupção imediata.
- b. Incorreta: resultados obtidos exclusivamente em ambiente de desenvolvimento isolado não podem ser considerados diretamente aplicáveis a produção, dada a diferença de condições reais.
- c. Incorreta: afetar serviços aleatoriamente, sem relação com a hipótese formulada, não constitui um experimento controlado e válido.
- d. Correta: iniciar com raio de impacto limitado e manter um mecanismo de interrupção imediata acionado por limites de degradação predefinidos é a aplicação correta dos princípios de segurança em engenharia do caos.
- e. Incorreta: executar o experimento no pico histórico máximo de tráfego maximiza o risco para os clientes reais, contrariando o princípio de raio de impacto controlado.

**Questão 30** (correta: e)
- a. Incorreta: identificar e punir um indivíduo específico contraria diretamente o princípio de postmortem sem culpabilização.
- b. Incorreta: encerrar o postmortem sem documentar ações de acompanhamento desperdiça a oportunidade de aprendizagem sistêmica do incidente.
- c. Incorreta: restringir o acesso ao relatório limita o compartilhamento do aprendizado, contrariando o objetivo de disseminar melhorias na organização.
- d. Incorreta: atribuir o incidente a erro humano isolado, sem investigar fatores sistêmicos, ignora causas estruturais que podem se repetir.
- e. Correta: reconstruir a linha do tempo, identificar fatores sistêmicos contribuintes, documentar ações com responsáveis e prazos, e compartilhar o aprendizado é a prática recomendada de postmortem sem culpabilização.

**Questão 31** (correta: a)
- a. Correta: a decisão de bloquear ou aprovar precisa ocorrer em segundos, e um pipeline horário não teria informação atualizada a tempo de impedir a fraude antes da aprovação.
- b. Incorreta: lotes horários não garantem, por definição, maior precisão estatística, e a alegação ignora o requisito de tempo de resposta do negócio.
- c. Incorreta: a janela de tempo entre eventos influencia diretamente a eficácia da detecção de fraude em tempo quase real, tornando as alternativas não equivalentes.
- d. Incorreta: a detecção de fraude pode, sim, ser automatizada em sistemas distribuídos, inclusive com processamento em fluxo.
- e. Incorreta: o processamento em lote não elimina a necessidade de particionamento e tolerância a falhas, e tampouco atende ao requisito de tempo do negócio.

**Questão 32** (correta: b)
- a. Incorreta: o modelo prevê recuperação automática de tarefas isoladas, sem exigir reinício manual de todo o cluster.
- b. Correta: o framework reatribui a tarefa malsucedida a outro nó e a reexecuta a partir dos dados intermediários já disponíveis, sem exigir intervenção manual para uma falha isolada.
- c. Incorreta: cancelar o job inteiro e reprocessar manualmente contraria o propósito de tolerância a falhas automatizada do modelo.
- d. Incorreta: ignorar os dados do nó falho produziria um resultado incompleto e inconsistente, não uma recuperação correta.
- e. Incorreta: a tolerância a falhas de nós é uma característica central do modelo MapReduce original, não uma limitação exclusiva de frameworks de DAG mais recentes.

**Questão 33** (correta: c)
- a. Incorreta: reinicializar todo o pipeline a cada evento atrasado seria impraticável e não é o mecanismo utilizado para tratar atraso de eventos.
- b. Incorreta: descartar automaticamente qualquer evento fora de ordem eliminaria dados válidos e não é a prática recomendada para tratamento de atraso.
- c. Correta: marcas d'água combinadas com tolerância configurável a atraso permitem manter a janela correspondente ao tempo de evento aberta por tempo suficiente para acomodar eventos atrasados dentro de um limite aceitável.
- d. Incorreta: substituir tempo de evento por tempo de processamento eliminaria a fidelidade da análise ao momento real de ocorrência do evento no domínio de negócio.
- e. Incorreta: pipelines de fluxo, com os mecanismos adequados, conseguem lidar com eventos fora de ordem sem exigir processamento exclusivamente em lote.

**Questão 34** (correta: d)
- a. Incorreta: FaaS pode, sim, ser acionada por eventos assíncronos; essa é uma de suas aplicações mais comuns.
- b. Incorreta: funções como serviço são amplamente utilizadas para processar eventos assíncronos, contrariando a afirmação.
- c. Incorreta: os dois modelos não são idênticos em custo e desempenho; eles apresentam compromissos distintos relevantes para a escolha.
- d. Correta: FaaS tende a ser adequada para cargas esporádicas e de curta duração, dado o modelo de cobrança por execução e escalonamento automático, com o custo adicional de latência em inicializações a frio.
- e. Incorreta: um serviço de longa duração não elimina custo de infraestrutura; ele mantém custo mesmo durante períodos de ociosidade.

**Questão 35** (correta: e)
- a. Incorreta: adotar a borda integralmente, eliminando todo processamento central, ignora a necessidade de contexto histórico amplo em modelos de fraude mais complexos.
- b. Incorreta: processamento fora de uma região central não é, por definição, inseguro; segurança depende de como a comunicação e os dados são protegidos, não da localização do processamento.
- c. Incorreta: a latência é altamente relevante para decisões de detecção de fraude em tempo quase real, tornando a análise de localização de dados necessária.
- d. Incorreta: o custo de operação em pontos de borda não é sempre inferior ao de uma região central, especialmente considerando a complexidade de manter lógica distribuída em muitos pontos.
- e. Correta: a decisão deve ponderar o ganho de latência para sinais simples e locais contra o custo e a complexidade de manter lógica distribuída na borda, reservando processamento mais complexo e dependente de contexto histórico para a região central.

**Questão 36** (correta: a)
- a. Correta: explicitar o compromisso separadamente para cada parte do sistema, aceitando consistência eventual onde é tolerável e exigindo consistência mais forte onde a divergência tem custo direto, reflete uma avaliação arquitetural madura.
- b. Incorreta: exigir consistência forte em toda a aplicação, sem exceção, ignora os compromissos de latência e desempenho envolvidos em cada contexto de uso.
- c. Incorreta: atributos de qualidade como latência têm, sim, relevância arquitetural comparável à dos requisitos funcionais.
- d. Incorreta: resolver o conflito de forma aleatória, sem análise técnica, contraria a prática de avaliação arquitetural baseada em evidências e compromissos explícitos.
- e. Incorreta: a tensão entre dois requisitos de qualidade não implica que um deles deva ser eliminado; ela pode ser resolvida com decisões diferenciadas por contexto.

**Questão 37** (correta: b)
- a. Incorreta: um ADR deve conter, além da tecnologia escolhida, o contexto, as alternativas consideradas e as consequências esperadas.
- b. Correta: o registro está incompleto por não explicitar o contexto que motivou a decisão, as alternativas avaliadas e as consequências esperadas, elementos centrais de um ADR bem elaborado.
- c. Incorreta: decisões de orquestração de contêineres têm impacto arquitetural significativo e devem, sim, ser documentadas.
- d. Incorreta: a autoria do registro não deve ser restrita a uma equipe específica; deve envolver quem participou da decisão e é afetado por ela.
- e. Incorreta: o meio de armazenamento não supre a ausência de conteúdo substantivo sobre contexto, alternativas e consequências.

**Questão 38** (correta: c)
- a. Incorreta: a ausência de ponto único de falha não pode ser concluída sem considerar dependências compartilhadas, como o sistema de mensageria não replicado.
- b. Incorreta: as réplicas do serviço de pagamento, distribuídas em zonas distintas, não constituem, isoladamente, o ponto único de falha descrito no cenário.
- c. Correta: o sistema de mensageria não replicado, hospedado em uma única zona, constitui um ponto único de falha, pois sua indisponibilidade pode comprometer a comunicação entre os serviços mesmo com o serviço de pagamento saudável em suas três réplicas.
- d. Incorreta: réplicas de um componente não eliminam automaticamente pontos únicos de falha em outras partes do sistema das quais esse componente depende.
- e. Incorreta: pontos únicos de falha podem existir em qualquer componente não replicado do sistema, incluindo sistemas de mensageria, não apenas em bancos de dados.

**Questão 39** (correta: d)
- a. Incorreta: os valores estão trocados; o intervalo de replicação de 5 minutos corresponde ao RPO, e o tempo de restabelecimento de 15 minutos corresponde ao RTO.
- b. Incorreta: RPO e RTO podem, sim, ser estimados a partir da configuração de replicação e do plano de recuperação descritos, sem exigir um desastre real.
- c. Incorreta: replicação assíncrona não garante recuperação instantânea nem perda zero de dados; há uma janela de possível perda entre replicações.
- d. Correta: o RPO aproximado é de 5 minutos, refletindo a possível perda de dados desde a última replicação bem-sucedida, e o RTO aproximado é de 15 minutos, refletindo o tempo necessário para restabelecer o serviço.
- e. Incorreta: RPO e RTO não são necessariamente iguais ao intervalo de replicação; RTO reflete o tempo de restabelecimento do serviço, descrito no cenário como 15 minutos, não 5.

**Questão 40** (correta: e)
- a. Incorreta: manter capacidade fixa independentemente dos dados de utilização ignora a possibilidade de ajustar recursos com segurança, mantendo as metas de disponibilidade.
- b. Incorreta: eliminar toda a redundância comprometeria a disponibilidade e a resiliência necessárias para os cenários de pico.
- c. Incorreta: custo deve, sim, ser avaliado em conjunto com desempenho e disponibilidade, como parte de uma avaliação arquitetural completa.
- d. Incorreta: o custo de infraestrutura é parte central da avaliação arquitetural e não pode ser ignorado em favor exclusivo do custo de equipe.
- e. Correta: revisar a estratégia de capacidade com base em dados reais de utilização, adotando escalonamento automático que ajuste recursos à demanda observada, preserva as metas de disponibilidade e desempenho sem manter custo desnecessário em períodos de baixa demanda.
