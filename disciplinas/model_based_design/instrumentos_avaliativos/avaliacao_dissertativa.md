# Avaliação final dissertativa — arquivo-mestre

Disciplina: *Model-Based Design for Cyber-Physical Systems*

Professor-conteudista: Afonso Cesar Lelis Brandão

> **Controle de versão:** a Parte A é destinada ao estudante. A Parte B é exclusiva do professor tutor e contém respostas esperadas e critérios de correção. A versão mestra reúne as duas partes para controle interno; a exportação para distribuição ao estudante deve cortar o arquivo exatamente no cabeçalho `# Parte B`, de modo que nenhuma resposta, solução ou rubrica chegue à cópia do estudante.

---

# Parte A — Versão do estudante

## Orientações

- Quantidade: 10 questões dissertativas.
- Abrangência: as quatro unidades, com a seguinte distribuição — Unidade 1, questões 1 a 3; Unidade 2, questões 4 a 6; Unidade 3, questões 7 e 8; Unidade 4, questões 9 e 10.
- Conteúdo: situações-problema envolvendo o NexaBot ou sistemas ciberfísicos equivalentes do setor automotivo, aeroespacial ou de robótica industrial, exigindo aplicação analítica dos conceitos estudados — não a reprodução de definições.
- Valor: 10 pontos por questão, totalizando 100 pontos.
- Cada resposta deve relacionar **conceito**, **mecanismo**, **hipóteses assumidas** e **consequência prática** para o sistema descrito. Respostas puramente definicionais, sem análise do cenário apresentado, não atendem integralmente ao que foi solicitado.
- Sempre que a questão pedir um cálculo, apresente a fórmula, a substituição numérica e o resultado com unidade.

## Questões

### Questão 1 — Unidade 1: espaço de estados e o significado físico dos polos

A equipe de engenharia do NexaBot linearizou o motor de tração em espaço de estados e obteve dois polos reais e negativos, em $-335{,}96\ \mathrm{rad/s}$ e $-7{,}215\ \mathrm{rad/s}$. Um estagiário argumenta que, como os dois polos estão no semiplano esquerdo, "o sistema é igualmente rápido em qualquer direção" e que basta um único controlador proporcional simples, sintonizado por tentativa, para atender a qualquer especificação de desempenho. Explique fisicamente o que cada um dos dois polos representa no motor de corrente contínua (associe cada polo a um subsistema — elétrico ou mecânico), calcule as duas constantes de tempo correspondentes, mostre que a separação de escalas de tempo entre elas é de cerca de duas ordens de grandeza e explique por que essa separação — e não apenas o sinal dos polos — é a informação relevante para decidir se o polo elétrico pode ser desprezado em um projeto de controle de velocidade.

### Questão 2 — Unidade 1: identificação de parâmetros e validação com dados retidos

Um colega identificou os parâmetros do motor do NexaBot ajustando-os por mínimos quadrados a um único ensaio de degrau e obteve um erro de ajuste inferior a 1% sobre esse mesmo conjunto de dados. Ele conclui que o modelo está pronto para uso no projeto de controle. Explique por que um erro de ajuste baixo sobre os dados usados na identificação não é evidência suficiente de que o modelo é válido, descreva o procedimento correto de validação com dados retidos (dados não usados na identificação) e explique, com um exemplo numérico plausível para o NexaBot, uma situação em que o ajuste sobre os dados de identificação é excelente mas o modelo falha ao ser testado contra o conjunto retido. Conclua indicando pelo menos duas causas prováveis desse tipo de falha (por exemplo, sobreajuste a ruído de medição ou excitação insuficiente do ensaio).

### Questão 3 — Unidade 1: controlabilidade, observabilidade e o limite físico do atuador

Um projetista, de posse do modelo em espaço de estados do NexaBot, decide alocar os polos de malha fechada por realimentação de estados em posições muito mais rápidas que os polos de malha aberta, buscando um tempo de acomodação muito curto. A simulação mostra que a tensão de comando exigida durante o transitório ultrapassa amplamente os 24 V disponíveis na bateria. Explique o que significa, tecnicamente, o par (planta, matriz de entrada) ser controlável, e por que a controlabilidade garante que a alocação de polos é matematicamente possível, mas não garante que ela seja fisicamente implementável. Descreva o mecanismo pelo qual a exigência de dinâmica mais rápida aumenta o esforço de controle e explique como um projetista deveria reformular o problema (por exemplo, via ponderação em um regulador linear quadrático) para obter um compromisso entre velocidade de resposta e respeito ao limite de 24 V.

### Questão 4 — Unidade 2: sintonia de PID, métricas de aceitação e o sobressinal de Ziegler-Nichols

A equipe do NexaBot sintonizou o controlador de velocidade pelo método clássico de Ziegler-Nichols a partir do ganho crítico e do período crítico de oscilação, obtendo uma resposta ao degrau com sobressinal superior a 20%. O requisito do projeto exige sobressinal inferior a 10% para não saturar o atuador durante manobras. Explique o que representam o ganho crítico e o período crítico no procedimento de Ziegler-Nichols, apresente pelo menos três métricas objetivas de aceitação de uma malha de controle (por exemplo, sobressinal, tempo de acomodação e integral do erro quadrático) e explique o mecanismo pelo qual a regra clássica de Ziegler-Nichols tende a produzir sobressinal elevado. Proponha e justifique uma alternativa de sintonia (variante sem sobressinal ou ajuste manual orientado pelas métricas) compatível com o requisito do NexaBot.

### Questão 5 — Unidade 2: saturação, windup e back-calculation

Para sustentar uma velocidade de $1{,}0\ \mathrm{m/s}$, o NexaBot exige $18{,}85\ \mathrm{V}$ em regime permanente, restando apenas $5{,}15\ \mathrm{V}$ de folga frente ao limite de $24\ \mathrm{V}$ para a ação transitória do controlador. Durante uma referência mais agressiva, o comando calculado pelo PID ultrapassa os 24 V, o atuador satura e a resposta observada apresenta sobressinal grosseiro e assentamento lento, mesmo após a referência ser reduzida. Explique o mecanismo do efeito windup: por que o termo integral continua acumulando erro enquanto o atuador está saturado, e por que essa acumulação atrasa a resposta mesmo depois de o erro real começar a diminuir. Descreva o funcionamento do anti-windup por back-calculation (qual sinal ele realimenta e onde) e explique, em termos do orçamento de tensão do NexaBot (18,85 V de regime contra 24 V disponíveis), por que esse mecanismo é especialmente necessário nesse sistema e não apenas uma boa prática genérica.

### Questão 6 — Unidade 2: período de amostragem e erro de acoplamento em co-simulação FMI

Um engenheiro decide reduzir o período de amostragem do controlador do NexaBot de $T_s = 5\ \mathrm{ms}$ para $T_s = 1\ \mathrm{ms}$, argumentando que "amostrar mais rápido só pode melhorar o resultado", e em seguida acopla o controlador discretizado à planta por co-simulação FMI 3.0 usando um passo de comunicação de 50 ms entre os dois FMUs. Considerando a constante de tempo modal dominante de aproximadamente $138{,}6\ \mathrm{ms}$ (ou a aproximação mecânica desacoplada de $148{,}1\ \mathrm{ms}$), explique o critério que relaciona o período de amostragem às constantes de tempo da planta e avalie se a escolha de 1 ms é adequada, insuficiente ou desnecessariamente conservadora, justificando com o número de amostras por constante de tempo que cada escolha produz. Em seguida, explique o que é o erro de acoplamento em uma co-simulação FMI, por que ele depende do passo de comunicação entre os FMUs — que é uma grandeza distinta do período de amostragem interno do controlador — e por que, nesse cenário, um passo de comunicação de 50 ms pode comprometer a co-simulação mesmo com um controlador amostrado a 1 ms.

### Questão 7 — Unidade 3: de requisito ambíguo a propriedade formal

O requisito original de segurança do NexaBot foi escrito como "o robô deve parar rapidamente se houver obstáculo". Ao tentar formalizar esse texto para verificação, a equipe percebe que ele admite pelo menos três interpretações incompatíveis quanto ao que conta como "parar" (torque zerado, freio acionado, velocidade nula) e quanto ao que significa "rapidamente" (sem prazo numérico). Explique, com um exemplo para cada caso, por que um requisito em linguagem natural como esse é inadequado como entrada de um verificador formal. Reescreva o requisito como uma propriedade formalizável, equivalente em espírito a REQ-SAFE-006 (torque zerado em no máximo 150 ms após a detecção do obstáculo), explicitando o evento de disparo, a ação exigida e o prazo. Por fim, explique a diferença entre uma propriedade de **segurança** ("algo ruim nunca acontece") e uma propriedade de **vivacidade** ("algo bom eventualmente acontece"), classificando o requisito reescrito e um segundo requisito do NexaBot de natureza diferente (por exemplo, REQ-SAFE-005) em uma dessas duas categorias, com justificativa.

### Questão 8 — Unidade 3: o que o contraexemplo prova, e o que a verificação não prova

Um bug foi introduzido no supervisor de segurança do NexaBot: por um erro de transição, o torque pode permanecer habilitado por um ciclo mesmo com obstáculo detectado. O verificador de modelos, ao explorar exaustivamente o espaço de estados alcançável, relata a violação de REQ-SAFE-001 e devolve a sequência exata de entradas (o contraexemplo) que leva o supervisor da condição inicial até o estado de falha. Explique o que exatamente um contraexemplo demonstra sobre o modelo verificado e por que ele é considerado a saída mais valiosa de um model checker, em contraste com uma simulação que passa em todos os cenários testados. Em seguida, explique por que a mesma verificação — mesmo depois de corrigido o bug e de o verificador reportar que a propriedade é satisfeita — não constitui prova de que o NexaBot físico se comportará corretamente, distinguindo explicitamente o modelo (o autômato verificado) do sistema físico real. Encerre relacionando cobertura de transições e cobertura de linhas de código: por que uma suíte de testes pode ter 100% de cobertura de linha e ainda assim não ter exercitado uma transição crítica do supervisor.

### Questão 9 — Unidade 4: equivalência modelo-código e o épsilon de máquina

Durante o teste de software-in-the-loop (SIL) do controlador do NexaBot, a equipe compara, amostra a amostra, a saída do modelo de referência (calculada em Python com aritmética de ponto flutuante em precisão dupla) com a saída do código C gerado automaticamente, também compilado para usar `double`. O erro máximo absoluto observado entre as duas implementações, ao longo de toda a sequência de entradas de teste, é de $4{,}7\times10^{-3}$. Sabendo que o épsilon de máquina para `double` é da ordem de $2{,}2\times10^{-16}$, e considerando que ambas as implementações usam o mesmo tipo de dado e deveriam calcular exatamente a mesma equação de diferenças, explique por que um erro dessa magnitude — muitas ordens de grandeza acima do épsilon de máquina — deve ser interpretado como evidência de um defeito real na geração de código ou na tradução da equação, e não como ruído numérico esperado de arredondamento de ponto flutuante. Descreva pelo menos duas causas plausíveis de defeito que produziriam um erro dessa ordem (por exemplo, ordem de operações divergente, template com erro de sinal, ou truncamento indevido) e explique por que a mesma discrepância, se o código gerado usasse ponto fixo Q16.16, exigiria uma tolerância de aceitação diferente da usada para `double`.

### Questão 10 — Unidade 4: o que o pipeline aberto sustenta perante DO-178C e ISO 26262

O NexaBot chega ao final da disciplina com modelo, propriedades verificadas no escopo declarado, código gerado, testes com cobertura medida e uma matriz que expõe uma lacuna: REQ-SAFE-007 não possui teste da trajetória contínua. Um colega conclui que o restante das evidências "certifica" o sistema segundo a DO-178C ou a ISO 26262. Explique a diferença entre **produzir evidências** e **certificar um sistema**, situando o que a matriz e a suíte sustentam. Explique também como uso, impacto de erro e detecção posterior determinam a análise de confiança ou eventual **qualificação de ferramenta**, além do papel da **independência de verificação**. Conclua indicando o que falta no pipeline e por que a lacuna explícita não pode ser compensada apenas por mais arquivos ou por uma CI verde.

---

# Parte B — Versão exclusiva do professor tutor

> **NÃO DISTRIBUIR AOS ESTUDANTES.** Esta parte deve ser removida do arquivo entregue à turma e permanecer apenas na versão do tutor, posicionada ao final do documento.

## Respostas esperadas e critérios de correção

### Questão 1

- **0 a 3 pontos:** associa corretamente o polo em $-335{,}96\ \mathrm{rad/s}$ à dinâmica elétrica (indutância/resistência de armadura) e o polo em $-7{,}215\ \mathrm{rad/s}$ à dinâmica mecânica (inércia/atrito refletidos).
- **0 a 3 pontos:** calcula $\tau_e = 1/335{,}96 \approx 2{,}98\ \mathrm{ms}$ (valor de referência da disciplina: $\tau_e \approx 2{,}92\ \mathrm{ms}$, calculado a partir de $L/R$) e $\tau_m \approx 1/7{,}215 \approx 139\ \mathrm{ms}$ (valor de referência: $\tau_m \approx 148\ \mathrm{ms}$), aceitando pequenas variações decorrentes do método de cálculo, desde que a ordem de grandeza e o raciocínio estejam corretos.
- **0 a 2 pontos:** identifica a separação de aproximadamente duas ordens de grandeza (fator próximo de 50) entre as duas constantes de tempo.
- **0 a 2 pontos:** explica que a separação de escalas — e não apenas o sinal negativo dos polos — é o que permite considerar a dinâmica elétrica "instantânea" frente à mecânica para fins de projeto de um controlador de velocidade, rejeitando a afirmação do estagiário de que o sinal dos polos, isoladamente, garante desempenho adequado com controlador proporcional simples.

### Questão 2

- **0 a 3 pontos:** explica que ajuste baixo sobre os dados de identificação mede apenas a capacidade do modelo de reproduzir aquele conjunto específico, podendo refletir sobreajuste a ruído de medição ou a características particulares daquele ensaio, e não a capacidade de generalização do modelo.
- **0 a 3 pontos:** descreve corretamente o procedimento de validação com dados retidos: separar um segundo conjunto de dados de ensaio, não utilizado na etapa de identificação por mínimos quadrados, e comparar a saída do modelo identificado contra esse conjunto, quantificando o erro percentual.
- **0 a 2 pontos:** apresenta um exemplo numérico plausível em que o erro de ajuste é baixo (por exemplo, inferior a 1%) sobre os dados de identificação, mas o erro sobre o conjunto retido é significativamente maior (por exemplo, superior a 10%), evidenciando a falha de generalização.
- **0 a 2 pontos:** indica pelo menos duas causas plausíveis, como sobreajuste a ruído de medição, excitação insuficiente do ensaio (por exemplo, um único degrau que não excita toda a faixa de operação) ou quantização do encoder não modelada.

### Questão 3

- **0 a 3 pontos:** explica corretamente controlabilidade como a propriedade que garante existir uma entrada capaz de levar o estado de qualquer condição inicial a qualquer condição final em tempo finito, verificável pelo posto pleno da matriz de controlabilidade.
- **0 a 2 pontos:** explica que controlabilidade é uma condição matemática sobre a existência de uma entrada, sem qualquer restrição sobre a amplitude dessa entrada — por isso não garante que a entrada necessária respeite limites físicos do atuador.
- **0 a 3 pontos:** descreve o mecanismo pelo qual exigir dinâmica mais rápida (polos de malha fechada mais afastados da origem) aumenta a magnitude do comando de controle necessário durante o transitório, relacionando isso ao ganho de realimentação de estados.
- **0 a 2 pontos:** propõe reformulação coerente, como ajustar as matrizes de ponderação $Q$ e $R$ de um regulador linear quadrático para penalizar mais o esforço de controle, ou relaxar a especificação de tempo de acomodação, buscando uma solução que respeite os 24 V disponíveis.

### Questão 4

- **0 a 2 pontos:** explica que o ganho crítico é o ganho proporcional que leva a malha ao limite de estabilidade (oscilação sustentada) e que o período crítico é o período dessa oscilação.
- **0 a 2 pontos:** apresenta pelo menos três métricas de aceitação corretas, entre sobressinal, tempo de subida, tempo de acomodação e integral do erro quadrático (ou métrica equivalente).
- **0 a 3 pontos:** explica que a regra clássica de Ziegler-Nichols foi derivada para produzir uma razão de decaimento específica (cerca de um quarto por ciclo), o que resulta estruturalmente em sobressinal elevado, sem otimizar diretamente para baixo sobressinal.
- **0 a 3 pontos:** propõe alternativa coerente — variante de Ziegler-Nichols sem sobressinal, ajuste manual orientado pelas métricas ou outro método de sintonia — e justifica como ela reduziria o sobressinal para atender ao requisito de menos de 10%.

### Questão 5

- **0 a 3 pontos:** explica o mecanismo do windup: quando o atuador satura, a saída real de controle se mantém no limite (24 V) independentemente do que o PID calcula internamente; se o termo integral continuar sendo atualizado pelo erro medido, ele acumula um valor muito maior do que o necessário, e essa acumulação só é "descontada" depois que o erro muda de sinal, atrasando a resposta.
- **0 a 3 pontos:** descreve corretamente o back-calculation: a diferença entre o comando saturado (efetivamente aplicado) e o comando calculado pelo PID antes da saturação é realimentada, com um ganho, para reduzir o valor acumulado no integrador, impedindo que ele continue crescendo enquanto a saturação persiste.
- **0 a 2 pontos:** relaciona corretamente o orçamento de tensão do NexaBot (18,85 V de regime contra 24 V disponíveis, folga de apenas 5,15 V) à alta probabilidade de saturação durante transitórios, tornando o anti-windup uma necessidade concreta e não apenas uma boa prática abstrata.
- **0 a 2 pontos:** menciona explicitamente que, sem anti-windup, o sintoma observado (sobressinal grosseiro e assentamento lento mesmo após a referência cair) é a assinatura típica do windup, e não de um problema de sintonia do PID em si.

### Questão 6

- **0 a 3 pontos:** explica o critério de escolha do período de amostragem com base na constante de tempo dominante, reconhecendo que amostrar muito mais rápido do que necessário não traz benefício adicional relevante e pode aumentar custo computacional e sensibilidade a ruído de quantização; calcula, pelo valor modal exato, aproximadamente $27{,}7$ amostras para $T_s=5\ \mathrm{ms}$ e $138{,}6$ para $T_s=1\ \mathrm{ms}$ (ou cerca de $29{,}6$ e $148{,}1$ pela aproximação desacoplada), avaliando a segunda escolha como desnecessariamente conservadora frente à primeira, já validada.
- **0 a 2 pontos:** reconhece que "amostrar mais rápido só pode melhorar" é uma simplificação questionável, pois o ganho marginal de desempenho decai enquanto custos (processamento, ruído) podem crescer.
- **0 a 3 pontos:** define corretamente o erro de acoplamento em co-simulação FMI como a diferença entre a trajetória obtida com dois FMUs (planta e controlador) trocando dados apenas nos instantes de comunicação e uma referência monolítica (ou de comunicação muito mais fina), e explica que esse erro cresce com o passo de comunicação porque cada FMU evolui isoladamente, com entradas desatualizadas, entre um instante de troca e o seguinte.
- **0 a 2 pontos:** distingue corretamente o período de amostragem interno do controlador (1 ms, nesse cenário) do passo de comunicação entre os FMUs na co-simulação (50 ms) e explica por que um passo de comunicação grande pode comprometer a co-simulação independentemente de o controlador amostrar rapidamente por dentro.

### Questão 7

- **0 a 3 pontos:** explica com exemplos concretos por que o requisito original é ambíguo — pelo menos duas interpretações distintas quanto ao que conta como "parar" (torque zerado, freio acionado, velocidade nula) e a ausência de prazo numérico para "rapidamente".
- **0 a 3 pontos:** reescreve o requisito de forma formalizável, com evento de disparo (obstáculo detectado), ação exigida (torque zerado) e prazo numérico explícito (equivalente a REQ-SAFE-006, 150 ms), em linguagem compatível com verificação formal.
- **0 a 2 pontos:** define corretamente propriedade de segurança ("algo ruim nunca acontece", tipicamente um invariante) e propriedade de vivacidade ("algo bom eventualmente acontece", tipicamente alcançabilidade de um estado desejável).
- **0 a 2 pontos:** classifica corretamente o requisito reescrito como propriedade de segurança (limitada por prazo) e um segundo requisito do NexaBot (por exemplo, REQ-SAFE-005 — retomada do movimento após remoção do obstáculo) como propriedade de vivacidade, com justificativa coerente.

### Questão 8

- **0 a 3 pontos:** explica que o contraexemplo é uma sequência concreta de estados e/ou entradas, produzida pela exploração exaustiva do espaço de estados alcançável, que demonstra de forma construtiva a existência de ao menos uma execução do modelo que viola a propriedade — e por isso é mais valioso do que uma simulação que passa, pois a simulação só cobre os cenários efetivamente executados, enquanto o contraexemplo resulta de uma busca sobre todo o espaço.
- **0 a 3 pontos:** distingue claramente modelo (o autômato/sistema de transições verificado) de sistema físico real, explicando que a verificação formal prova propriedades sobre o modelo, e que a correção dessa prova depende inteiramente da fidelidade do modelo ao comportamento físico do NexaBot — um modelo com premissas erradas (por exemplo, sem representar um atraso de sensor real) pode ser verificado como correto e ainda assim o sistema físico falhar.
- **0 a 2 pontos:** reconhece explicitamente que a verificação, mesmo após a correção do bug, não constitui prova de correção do NexaBot físico, apenas do modelo formalizado dele.
- **0 a 2 pontos:** explica a diferença entre cobertura de transições (cada transição do autômato foi exercitada ao menos uma vez) e cobertura de linhas de código (cada linha foi executada ao menos uma vez), com um exemplo de como 100% de cobertura de linha pode coexistir com uma transição crítica nunca exercitada (por exemplo, uma condição de guarda composta em que apenas um dos caminhos de decisão foi percorrido, embora todas as linhas tenham sido tocadas).

### Questão 9

- **0 a 3 pontos:** explica que, como as duas implementações usam o mesmo tipo de dado (`double`) para calcular a mesma equação de diferenças, o erro esperado entre elas, na ausência de defeito, deveria ser da ordem do épsilon de máquina (acumulado ao longo de poucas operações), e não de $4{,}7\times10^{-3}$ — muitas ordens de grandeza maior.
- **0 a 3 pontos:** conclui corretamente que essa discrepância é evidência de defeito real, e não de ruído numérico de arredondamento, sustentando a conclusão na comparação de ordens de grandeza entre o erro observado e o épsilon de máquina.
- **0 a 2 pontos:** apresenta pelo menos duas causas plausíveis de defeito, como ordem de operações divergente entre modelo e código gerado, erro de sinal ou de coeficiente no template de geração, truncamento ou arredondamento indevido introduzido na tradução, ou uso inadvertido de precisão simples em algum ponto do código gerado.
- **0 a 2 pontos:** explica que, para uma variante em ponto fixo Q16.16, a tolerância de aceitação deve ser maior do que para `double`, pois a representação em ponto fixo introduz erro de quantização estrutural (relacionado à resolução de $2^{-16}$ da parte fracionária), distinto do erro de arredondamento de ponto flutuante — portanto o mesmo limiar não deve ser aplicado às duas variantes.

### Questão 10

- **0 a 3 pontos:** distingue claramente produzir evidências de correção (o conjunto de artefatos reproduzíveis — modelo, propriedades verificadas, código gerado, testes, matriz de rastreabilidade) de certificar um sistema (um processo formal, conduzido por autoridade ou processo reconhecido, que avalia o cumprimento de objetivos de uma norma e emite um veredito sobre a aptidão do sistema para uso).
- **0 a 2 pontos:** situa corretamente o que o pipeline da disciplina sustenta: evidências objetivas e rastreáveis de que requisitos específicos foram formalizados, verificados e testados, úteis como insumo para um processo de certificação, mas não equivalentes a ele.
- **0 a 2 pontos:** explica confiança e qualificação de ferramenta: a necessidade depende do uso, do impacto de um erro e de esse erro poder ser detectado por verificação posterior; licença aberta ou comercial não decide a classificação.
- **0 a 3 pontos:** explica independência de verificação e conclui que faltam ao pipeline, entre outros elementos, análise formal de confiança nas ferramentas e eventual qualificação aplicável, independência adequada, dados completos de ciclo de vida e avaliação externa — reforçando que o pipeline produz evidências, não certifica.

## Conferência antes da exportação

- [ ] Gerar uma cópia do estudante contendo somente a Parte A, cortada exatamente antes do cabeçalho `# Parte B`.
- [ ] Gerar uma cópia do tutor contendo as Partes A e B.
- [ ] Confirmar que cada rubrica soma exatamente 10 pontos e que o total das 10 questões soma 100 pontos.
- [ ] Confirmar a distribuição por unidade: questões 1–3 (Unidade 1), 4–6 (Unidade 2), 7–8 (Unidade 3), 9–10 (Unidade 4).
- [ ] Confirmar que todo número citado nos enunciados é reproduzível pelos scripts de `projeto_nexabot/`.
- [ ] Validar linguagem, formatação e ausência de conteúdo da Parte B na versão do estudante.
