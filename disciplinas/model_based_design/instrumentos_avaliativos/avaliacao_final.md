# Avaliação Final — Model-Based Design for Cyber-Physical Systems

- **Disciplina:** Model-Based Design for Cyber-Physical Systems
- **Professor-conteudista:** Afonso Cesar Lelis Brandão

## Orientações

- **40 questões** padrão ENADE no total:
  - **15** do tipo **asserção-razão** (Q1–Q15)
  - **15** do tipo **interpretação** (Q16–Q30)
  - **10** do tipo **discursiva** (Q31–Q40, posicionadas ao final)
- Cada questão objetiva tem **5 alternativas (a–e)**, com a correta prefixada por `*`.
- Rotação das alternativas corretas: **a, b, c, d, e, a, b, c, d, e...** (6 questões para cada letra nas objetivas).
- Para cada alternativa de questão objetiva, há **feedback explicativo**.
- Feedbacks das objetivas ao final, na ordem das questões.
- Todo número citado nesta avaliação é reproduzível pelos scripts de `projeto_nexabot/`.

---

## Questões objetivas (1–30) e discursivas (31–40)

### Questão 1 (Asserção-Razão)

> **Asserção I:** A verificação de um sistema ciberfísico precisa tratar conjuntamente a dinâmica contínua da planta e a lógica discreta do controlador, e não cada uma isoladamente.
>
> **porque**
>
> **Razão II:** Em um sistema ciberfísico, trechos de evolução contínua da planta são intercalados por eventos discretos de amostragem e de atualização do comando, de modo que o comportamento observado emerge do acoplamento entre os dois domínios.

A respeito dessas asserções, assinale a opção correta:

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 2 (Asserção-Razão)

> **Asserção I:** Com ganho estático de $21{,}2164\ \mathrm{rad/(s\,V)}$, os $24\ \mathrm{V}$ do driver do NexaBot produzem, sem carga, velocidade linear máxima de aproximadamente $1{,}273\ \mathrm{m/s}$.
>
> **porque**
>
> **Razão II:** O V-Model organiza o desenvolvimento em um ramo descendente de decomposição de requisitos e um ramo ascendente de verificação no mesmo nível de abstração.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 3 (Asserção-Razão)

> **Asserção I:** Com a tensão fixa em $18{,}85\ \mathrm{V}$, a velocidade do NexaBot cai e o erro cresce continuamente quando surge um torque de carga.
>
> **porque**
>
> **Razão II:** A malha aberta mede a velocidade de saída e recalcula o comando, mas com ganho proporcional insuficiente para anular o efeito da carga.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 4 (Asserção-Razão)

> **Asserção I:** A controlabilidade do par (matriz de estados, matriz de entrada) garante que qualquer especificação de tempo de acomodação pode ser atendida dentro dos $24\ \mathrm{V}$ disponíveis no driver do NexaBot.
>
> **porque**
>
> **Razão II:** A matriz de controlabilidade com posto pleno assegura a existência de uma entrada capaz de levar o estado de qualquer condição inicial a qualquer condição final em tempo finito.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 5 (Asserção-Razão)

> **Asserção I:** O polo elétrico do motor do NexaBot pode ser desprezado no projeto do controlador de velocidade porque é o mais lento dos dois polos da planta.
>
> **porque**
>
> **Razão II:** A separação entre as duas constantes de tempo do NexaBot é de aproximadamente uma ordem de grandeza, o que torna dispensável distinguir a dinâmica elétrica da mecânica.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

### Questão 6 (Asserção-Razão)

> **Asserção I:** Em malha fechada, o NexaBot sustenta a referência de $1{,}0\ \mathrm{m/s}$ mesmo quando surge o torque de carga que a malha aberta não compensa.
>
> **porque**
>
> **Razão II:** O erro entre referência e medição realimenta o controlador, de modo que o comando é recalculado continuamente em resposta ao distúrbio, sem depender de conhecimento prévio da carga.

A respeito dessas asserções, assinale a opção correta:

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 7 (Asserção-Razão)

> **Asserção I:** Em uma malha de realimentação unitária, as funções de sensibilidade e de sensibilidade complementar satisfazem $S(s)+T(s)=1$ em toda frequência.
>
> **porque**
>
> **Razão II:** O método de Ziegler-Nichols obtém os ganhos do PID a partir do ganho crítico e do período crítico medidos no limite de oscilação sustentada.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 8 (Asserção-Razão)

> **Asserção I:** Com $T_s = 5\ \mathrm{ms}$ e constante de tempo dominante de $138{,}6\ \mathrm{ms}$, o NexaBot é amostrado a cerca de 28 amostras por constante de tempo, dentro da faixa recomendada de projeto.
>
> **porque**
>
> **Razão II:** A faixa recomendada para a escolha do período de amostragem é de 100 a 300 amostras por constante de tempo dominante.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 9 (Asserção-Razão)

> **Asserção I:** O efeito windup desaparece por si só assim que o atuador sai da saturação, sem necessidade de qualquer mecanismo dedicado no controlador.
>
> **porque**
>
> **Razão II:** O anti-windup por *back-calculation* realimenta ao termo integral a diferença entre o comando calculado e o comando efetivamente aplicado, impedindo que o integrador acumule erro enquanto o atuador está saturado.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 10 (Asserção-Razão)

> **Asserção I:** Em uma co-simulação FMI, o passo de comunicação entre os FMUs é necessariamente igual ao período de amostragem interno do controlador.
>
> **porque**
>
> **Razão II:** Por essa razão, espaçar o passo de comunicação de $5\ \mathrm{ms}$ para $50\ \mathrm{ms}$ não altera o resultado da co-simulação, desde que o controlador continue amostrando a $5\ \mathrm{ms}$.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

### Questão 11 (Asserção-Razão)

> **Asserção I:** O requisito "o robô deve parar rapidamente se houver obstáculo" não serve como entrada de um verificador formal.
>
> **porque**
>
> **Razão II:** O texto não define o evento de disparo, a ação exigida nem um prazo numérico, admitindo leituras incompatíveis sobre o que conta como "parar" e sobre o que significa "rapidamente".

A respeito dessas asserções, assinale a opção correta:

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 12 (Asserção-Razão)

> **Asserção I:** O contraexemplo devolvido por um verificador de modelos é a sequência exata de entradas que leva o sistema do estado inicial até a violação da propriedade.
>
> **porque**
>
> **Razão II:** A explosão do espaço de estados é o principal limite prático da verificação por exploração explícita, já que o número de estados alcançáveis cresce combinatoriamente com as variáveis do modelo.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 13 (Asserção-Razão)

> **Asserção I:** Uma suíte de testes pode atingir 100% de cobertura de linhas do supervisor do NexaBot e ainda assim não exercitar uma transição crítica da máquina de estados.
>
> **porque**
>
> **Razão II:** Cobertura de linha e cobertura de transição são métricas equivalentes, pois ambas são medidas sobre o mesmo grafo de estados do supervisor.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 14 (Asserção-Razão)

> **Asserção I:** Como o código C do controlador é gerado automaticamente a partir do modelo, ajustes finos de ganho podem ser feitos diretamente no arquivo `.c` gerado, desde que documentados em comentário.
>
> **porque**
>
> **Razão II:** O bloco de rastreabilidade no cabeçalho do arquivo gerado registra os requisitos de origem, o modelo, o hash SHA-256 dos parâmetros e a data de geração.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Questão 15 (Asserção-Razão)

> **Asserção I:** Um erro máximo de $4{,}7\times10^{-3}\ \mathrm{V}$ entre o modelo de referência e o código C gerado, ambos executando em `double`, está dentro do ruído numérico esperado de arredondamento de ponto flutuante.
>
> **porque**
>
> **Razão II:** O épsilon de máquina do tipo `double` é da ordem de $10^{-3}$, o que explica diferenças dessa magnitude entre duas implementações da mesma equação.

A respeito dessas asserções, assinale a opção correta:

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

### Questão 16 (Interpretação)

**Estímulo:**

> O motor de tração do NexaBot tem ganho estático de $21{,}2164\ \mathrm{rad/(s\,V)}$. O redutor é de $20{:}1$ e a roda tem raio de $50\ \mathrm{mm}$, de modo que a referência de cruzeiro de $1{,}0\ \mathrm{m/s}$ corresponde a $400\ \mathrm{rad/s}$ no eixo do motor. Considere operação sem carga e em regime permanente.

A tensão de armadura necessária para sustentar essa referência é de aproximadamente:

*a. $18{,}85\ \mathrm{V}$ — pois $400 \div 21{,}2164 \approx 18{,}85$.
b. $8{,}49\ \mathrm{V}$, obtidos multiplicando-se a velocidade pelo raio da roda.
c. $24{,}00\ \mathrm{V}$, pois o driver sempre entrega a tensão máxima em regime.
d. $21{,}22\ \mathrm{V}$, que é o próprio ganho estático expresso em volts.
e. $400\ \mathrm{V}$, numericamente iguais à velocidade angular de regime.

### Questão 17 (Interpretação)

**Estímulo:**

> A linearização do motor do NexaBot em espaço de estados produz dois polos reais e negativos, em $-335{,}96\ \mathrm{rad/s}$ e $-7{,}215\ \mathrm{rad/s}$. A constante de tempo associada a um polo real é o inverso do seu módulo.

As duas constantes de tempo e a razão entre elas são, aproximadamente:

a. $3{,}0\ \mathrm{ms}$ e $14{,}0\ \mathrm{ms}$, razão próxima de 5.
*b. $3{,}0\ \mathrm{ms}$ e $139\ \mathrm{ms}$, razão próxima de 47 — pois $1 \div 335{,}96 \approx 2{,}98\ \mathrm{ms}$ e $1 \div 7{,}215 \approx 139\ \mathrm{ms}$.
c. $336\ \mathrm{ms}$ e $7{,}2\ \mathrm{ms}$, razão próxima de 47, tomando-se o próprio valor do polo como constante de tempo.
d. $335{,}96\ \mathrm{ms}$ e $139\ \mathrm{ms}$, razão próxima de 2,4.
e. As duas constantes são iguais, pois ambos os polos são reais e negativos.

### Questão 18 (Interpretação)

**Estímulo:**

> Mantendo fixa a tensão de $18{,}85\ \mathrm{V}$ que sustenta $1{,}00\ \mathrm{m/s}$ sem carga, aplica-se ao NexaBot um torque de carga de $0{,}05\ \mathrm{N\,m}$. Em regime permanente, a velocidade linear cai para aproximadamente $0{,}929\ \mathrm{m/s}$.

O erro relativo de velocidade que se estabelece, e o que ele revela sobre a estratégia de comando, são:

a. Cerca de $2{,}9\%$, e o erro é eliminado sozinho após alguns segundos.
b. Cerca de $5{,}0\%$, e corresponde ao limite normativo de tolerância de um AGV.
*c. Cerca de $7{,}1\%$ — pois $(1{,}00-0{,}929) \div 1{,}00 \approx 0{,}071$ — e ele **persiste**, porque em malha aberta nada mede a saída para corrigir o comando.
d. Cerca de $9{,}3\%$, e resulta de erro de identificação dos parâmetros do motor.
e. Erro nulo, pois a tensão aplicada permanece constante.

### Questão 19 (Interpretação)

**Estímulo:**

> O driver do NexaBot entrega no máximo $24\ \mathrm{V}$. O ganho estático é de $21{,}2164\ \mathrm{rad/(s\,V)}$, o redutor é de $20{:}1$ e a roda tem raio de $50\ \mathrm{mm}$, de modo que $v = \omega r / N$.

A velocidade linear máxima do NexaBot, sem carga, e a consequência de projeto são:

a. $1{,}00\ \mathrm{m/s}$, exatamente a velocidade de cruzeiro especificada.
b. $0{,}93\ \mathrm{m/s}$, valor já reduzido pelo torque de carga nominal.
c. $2{,}55\ \mathrm{m/s}$, o que garante ampla folga de atuação ao controlador.
*d. $1{,}273\ \mathrm{m/s}$ — pois $24 \times 21{,}2164 \approx 509{,}2\ \mathrm{rad/s}$ e $509{,}2 \times 0{,}05 \div 20 \approx 1{,}273$ — restando **pouca folga** acima do cruzeiro de $1{,}0\ \mathrm{m/s}$ para a ação transitória do controlador.
e. $5{,}09\ \mathrm{m/s}$, tomando-se a velocidade angular diretamente como velocidade linear.

### Questão 20 (Interpretação)

**Estímulo:**

> No ensaio de ganho crítico do NexaBot, obtêm-se $K_u \approx 3{,}6911$ e $T_u \approx 18{,}32\ \mathrm{ms}$. A regra clássica de Ziegler-Nichols para PID prescreve $K_p = 0{,}6\,K_u$, $K_i = 1{,}2\,K_u/T_u$ e $K_d = 0{,}075\,K_u T_u$.

Os ganhos resultantes e o comportamento esperado da resposta são:

a. $K_p \approx 1{,}30$, $K_i \approx 15{,}0$, $K_d \approx 0{,}010$, com resposta sem sobressinal.
b. $K_p \approx 3{,}69$, $K_i \approx 18{,}3$, $K_d \approx 0{,}068$, com resposta criticamente amortecida.
c. $K_p \approx 0{,}60$, $K_i \approx 1{,}20$, $K_d \approx 0{,}075$, com resposta lenta e sem saturação.
d. $K_p \approx 2{,}21$, $K_i \approx 242$, $K_d \approx 0{,}0051$, com resposta sem sobressinal e sem saturação do atuador.
*e. $K_p \approx 2{,}21$, $K_i \approx 242$, $K_d \approx 0{,}0051$, com **sobressinal elevado** e risco de saturar o atuador em $\pm 24\ \mathrm{V}$ durante o transitório.

### Questão 21 (Interpretação)

**Estímulo:**

> O NexaBot é amostrado com $T_s = 5\ \mathrm{ms}$. A constante de tempo modal dominante da planta é de $138{,}6\ \mathrm{ms}$ e a aproximação mecânica desacoplada é de $148{,}1\ \mathrm{ms}$. A faixa recomendada de projeto é de 10 a 30 amostras por constante de tempo.

O número de amostras por constante de tempo dominante e o veredito sobre a escolha de $T_s$ são:

*a. Cerca de $27{,}7$ amostras — pois $138{,}6 \div 5 \approx 27{,}7$ — valor **dentro** da faixa recomendada, próximo ao seu limite superior.
b. Cerca de $27{,}7$ amostras, valor abaixo da faixa recomendada, exigindo reduzir $T_s$.
c. Cerca de $693$ amostras, obtidas multiplicando-se a constante de tempo pelo período.
d. Cerca de $2{,}8$ amostras, o que reprova a escolha de $T_s$.
e. O número de amostras não depende da constante de tempo, apenas da frequência do processador.

### Questão 22 (Interpretação)

**Estímulo:**

> Na co-simulação FMI do NexaBot, a planta compilada em C e o controlador em Python trocam dados a cada passo de comunicação $H$. O controlador amostra internamente a $T_s = 5\ \mathrm{ms}$. A equipe de firmware sugere espaçar a troca para $H = 50\ \mathrm{ms}$ a fim de reduzir a sobrecarga de comunicação.

Quantos ciclos de controle ocorrem entre duas trocas de dados, e qual a consequência:

a. Um ciclo, pois a troca de dados e a amostragem são o mesmo evento.
*b. Dez ciclos — pois $50 \div 5 = 10$ — de modo que em nove deles o controlador atua sobre um estado de planta **desatualizado**, e o erro de acoplamento cresce.
c. Cinquenta ciclos, um para cada milissegundo do passo de comunicação.
d. Dez ciclos, sem consequência para o resultado, já que o controlador mantém sua própria taxa.
e. Nenhum ciclo, pois o controlador fica ocioso entre trocas.

### Questão 23 (Interpretação)

**Estímulo:**

> Após uma referência irreal que satura o atuador, mede-se o tempo para a velocidade do NexaBot voltar à faixa de 2% em torno da referência: $2\,256{,}5\ \mathrm{ms}$ sem anti-windup ($K_{aw}=0$) e $872{,}5\ \mathrm{ms}$ com anti-windup por *back-calculation* ($K_{aw}=2{,}0$). O valor do integrador no instante da comutação cai de $9\,251{,}6$ para $4\,668{,}2$.

A leitura correta desses números é:

a. O anti-windup reduz o pico de velocidade após a comutação, que é o seu efeito principal.
b. Os dois casos são equivalentes, pois o valor final do integrador é praticamente o mesmo.
*c. O anti-windup acelera a **recuperação** em cerca de $2{,}6$ vezes — pois $2\,256{,}5 \div 872{,}5 \approx 2{,}6$ — ao impedir que o integrador acumule erro durante a saturação.
d. O anti-windup elimina a saturação do atuador, mantendo o comando sempre abaixo de $24\ \mathrm{V}$.
e. O ganho $K_{aw}=2{,}0$ dobra a velocidade de resposta em qualquer cenário, saturado ou não.

### Questão 24 (Interpretação)

**Estímulo:**

> O supervisor do NexaBot roda com período $T_s = 5\ \mathrm{ms}$. O REQ-SAFE-006 exige que o torque seja zerado em no máximo $150\ \mathrm{ms}$ após a detecção do obstáculo. A verificação exaustiva do autômato temporizado, no cenário nominal, reporta pior caso de 5 períodos de amostragem.

O pior caso em milissegundos e o veredito de conformidade são:

a. $5\ \mathrm{ms}$, conforme, pois o pior caso é de um único período.
b. $150\ \mathrm{ms}$, exatamente no limite, sem folga alguma.
c. $750\ \mathrm{ms}$, não conforme, multiplicando-se os períodos pelo prazo.
*d. $25\ \mathrm{ms}$, **conforme** — pois $5 \times 5 = 25\ \mathrm{ms}$, contra um limite de 30 períodos ($150\ \mathrm{ms}$).
e. Não é possível determinar sem medir o tempo real de execução no microcontrolador.

### Questão 25 (Interpretação)

**Estímulo:**

> Variando o atraso admitido de detecção, a verificação exaustiva do watchdog do NexaBot mostra que o requisito de $150\ \mathrm{ms}$ é respeitado até um atraso de 27 períodos (pior caso de 30 períodos, $150{,}0\ \mathrm{ms}$) e é violado a partir de 28 períodos (pior caso de 31 períodos, $155{,}0\ \mathrm{ms}$). O período de amostragem é de $5\ \mathrm{ms}$.

A exigência de projeto que se impõe ao filtro de *debounce* do sensor de obstáculo é:

a. Atraso de detecção de no máximo 30 períodos, isto é, $150\ \mathrm{ms}$.
b. Atraso de detecção de no máximo 31 períodos, isto é, $155\ \mathrm{ms}$.
c. Qualquer atraso, desde que o watchdog reinicie o alvo após o estouro.
d. Atraso de detecção de no máximo 5 períodos, isto é, $25\ \mathrm{ms}$.
*e. Atraso de detecção **estritamente menor que 28 períodos**, isto é, no máximo $140\ \mathrm{ms}$ — pois $27 \times 5 = 135$ e $28 \times 5 = 140$ já viola.

### Questão 26 (Interpretação)

**Estímulo:**

> O verificador de modelos explora exaustivamente o espaço de estados alcançável do supervisor do NexaBot e reporta, para o cenário de obstáculo, seis caminhos distintos até a condição analisada, devolvendo a sequência de entradas de cada um.

O que se pode afirmar corretamente a partir desse resultado:

*a. Os seis caminhos foram explorados **exaustivamente** dentro do modelo e do escopo declarado — o que uma bateria de simulações manuais não garante, pois testa apenas os cenários escolhidos.
b. Seis caminhos indicam que o modelo é simples demais e deve ser descartado.
c. A exploração prova que o NexaBot físico se comportará corretamente em campo.
d. O número de caminhos equivale à cobertura de linhas do código do supervisor.
e. Seis caminhos são estatisticamente insuficientes, sendo necessário amostrar aleatoriamente mais execuções.

### Questão 27 (Interpretação)

**Estímulo:**

> Uma suíte de testes do supervisor do NexaBot reporta 100% de cobertura de linhas. A geração de testes a partir do modelo, porém, aponta que uma transição do autômato — a que sai do estado de emergência com obstáculo ainda presente — nunca foi exercitada.

A conclusão tecnicamente correta é:

a. A suíte está completa; a transição apontada é redundante, pois suas linhas já foram executadas.
*b. Cobertura de linha e cobertura de transição medem coisas diferentes: executar todas as linhas **não** implica percorrer todas as combinações de estado e evento que levam a elas.
c. A cobertura de 100% de linhas prova a ausência de defeitos no supervisor.
d. A transição não exercitada indica erro do gerador de testes, não lacuna da suíte.
e. Basta aumentar o número de casos aleatórios para que a cobertura de transição acompanhe a de linha.

### Questão 28 (Interpretação)

**Estímulo:**

> O código C gerado para o NexaBot tem uma variante em ponto fixo no formato Q16.16, com 16 bits para a parte inteira e 16 bits para a parte fracionária.

A resolução dessa representação — o menor incremento representável — é de aproximadamente:

a. $1{,}0 \times 10^{-2}$, correspondente a duas casas decimais.
b. $6{,}1 \times 10^{-5}$, correspondente a $1/16384$.
*c. $1{,}526 \times 10^{-5}$ — pois a resolução é $2^{-16} = 1/65\,536$.
d. $2{,}2 \times 10^{-16}$, igual ao épsilon de máquina do tipo `double`.
e. A resolução é variável, pois o ponto fixo ajusta a escala conforme a magnitude do número.

### Questão 29 (Interpretação)

**Estímulo:**

> Na verificação de equivalência SIL do NexaBot, a tolerância adotada é de $10^{-9}\ \mathrm{V}$ para a comparação em `double` e de $0{,}5\ \mathrm{V}$ para a variante Q16.16. A suíte de regressão gera 25 combinações aleatórias de ganhos e mede, em cada uma, o erro máximo entre modelo e código: em `double`, o erro é exatamente $0$; em Q16.16, varia entre $1{,}2\times10^{-4}$ e cerca de $4{,}1\times10^{-1}\ \mathrm{V}$.

O veredito correto da regressão e sua justificativa são:

a. Reprovado, pois o erro em Q16.16 é muitas ordens de grandeza maior que o erro em `double`.
b. Reprovado, pois o erro em Q16.16 ultrapassa a tolerância de $10^{-9}\ \mathrm{V}$.
c. Aprovado, mas apenas porque o erro em `double` é nulo, sendo o Q16.16 irrelevante.
*d. **Aprovado nos 25 casos**: cada implementação é julgada contra a tolerância adequada à sua aritmética — o `double` deve reproduzir o modelo exatamente, e o Q16.16 tem erro de quantização previsto, sempre abaixo dos $0{,}5\ \mathrm{V}$.
e. Inconclusivo, pois combinações aleatórias de ganhos não constituem teste de regressão válido.

### Questão 30 (Interpretação)

**Estímulo:**

> No ensaio de *hardware-in-the-loop* do NexaBot, com período nominal $T_s = 5\ \mathrm{ms}$, mede-se o desvio-padrão do jitter do laço em três durações crescentes: $0{,}0391$, $0{,}0428$ e $0{,}0442\ \mathrm{ms}$. O critério de aceitação adotado é de que o desvio-padrão do jitter não ultrapasse 10% do período nominal.

O veredito e a interpretação correta desses números são:

a. Reprovado, pois o jitter cresce com a duração do ensaio.
b. Aprovado, e os números comprovam determinismo de tempo real equivalente ao de um RTOS.
c. Reprovado, pois o limite de 10% corresponde a $0{,}05\ \mathrm{ms}$ e o terceiro valor o ultrapassa.
d. Aprovado, e o jitter medido pode ser transposto diretamente para o firmware embarcado no ESP32.
*e. **Aprovado com folga** — o limite é $0{,}5\ \mathrm{ms}$ (10% de $5\ \mathrm{ms}$) e os três valores ficam uma ordem de grandeza abaixo —, lembrando que se trata de um laço em Python de usuário, **não** de um firmware em tempo real.

---

## Questões discursivas (31–40)

### Questão 31 (Discursiva)

**Contexto:** A equipe de engenharia do NexaBot linearizou o motor de tração em espaço de estados e obteve dois polos reais e negativos, em $-335{,}96\ \mathrm{rad/s}$ e $-7{,}215\ \mathrm{rad/s}$. Um estagiário argumenta que, como os dois polos estão no semiplano esquerdo, "o sistema é igualmente rápido em qualquer direção", e que basta um controlador proporcional simples, sintonizado por tentativa, para atender a qualquer especificação de desempenho.

**Enunciado:** Apresente uma análise estruturada contendo: (a) o significado físico de cada polo, associando-o ao subsistema elétrico ou mecânico do motor; (b) o cálculo das duas constantes de tempo e da razão entre elas; (c) por que a separação de escalas — e não o sinal dos polos — é a informação relevante para decidir se o polo elétrico pode ser desprezado; (d) por que a conclusão do estagiário está errada.

**Resposta esperada:**

> Resposta de qualidade associa o polo rápido, $-335{,}96\ \mathrm{rad/s}$, à **dinâmica elétrica de armadura** (indutância e resistência, $\tau_e \approx L/R = 3{,}5/1{,}2 \approx 2{,}92\ \mathrm{ms}$) e o polo lento, $-7{,}215\ \mathrm{rad/s}$, à **dinâmica mecânica** (inércia e atrito refletidos pelo redutor, $\tau_m \approx 139\ \mathrm{ms}$, próximo dos $148\ \mathrm{ms}$ da aproximação mecânica desacoplada). Calcula $\tau = 1/|p|$: $1 \div 335{,}96 \approx 2{,}98\ \mathrm{ms}$ e $1 \div 7{,}215 \approx 139\ \mathrm{ms}$, com **razão próxima de 47** — cerca de duas ordens de grandeza. Explica que é essa separação que autoriza tratar a dinâmica elétrica como praticamente instantânea frente à mecânica em um projeto de controle de velocidade, reduzindo a planta a um modelo de primeira ordem sem perda significativa de fidelidade; sem separação, a redução seria inválida. Rejeita a afirmação do estagiário em dois pontos: o sinal dos polos informa apenas **estabilidade**, não velocidade nem desempenho relativo; e um proporcional simples não anula erro de regime sob carga — como mostram os $7{,}1\%$ de erro persistente da malha aberta — nem respeita, por tentativa, o limite físico de $24\ \mathrm{V}$ do driver. A melhor resposta observa que a separação de escalas é uma **hipótese de projeto que precisa ser verificada**, e não uma propriedade garantida de todo motor.

### Questão 32 (Discursiva)

**Contexto:** Um colega identificou os parâmetros do motor do NexaBot ajustando-os por mínimos quadrados a um único ensaio de degrau, e obteve erro de ajuste inferior a $1\%$ sobre esse mesmo conjunto de dados. Ele conclui que o modelo está pronto para o projeto do controlador.

**Enunciado:** Elabore uma resposta técnica contendo: (a) por que um erro de ajuste baixo sobre os dados de identificação não é evidência suficiente de validade do modelo; (b) o procedimento correto de validação com dados retidos; (c) um exemplo numérico plausível de ajuste excelente com falha na validação; (d) pelo menos duas causas prováveis desse tipo de falha e uma verificação cruzada barata de bancada.

**Resposta esperada:**

> Resposta de qualidade explica que o erro de ajuste mede apenas a capacidade do modelo de **reproduzir o conjunto que ele próprio usou para se ajustar** — pode refletir sobreajuste ao ruído de medição ou a particularidades daquele ensaio, e nada diz sobre generalização. Descreve o procedimento de **validação com dados retidos**: separar um segundo ensaio, não utilizado na identificação, simular o modelo identificado sob a mesma entrada e quantificar o erro percentual contra a saída medida, aceitando o modelo apenas se esse erro permanecer dentro do critério declarado (na disciplina, erro inferior a $5\%$ na reprodução do degrau). Apresenta exemplo numérico coerente: ajuste de $0{,}8\%$ sobre os dados de identificação e erro superior a $10\%$ sobre o conjunto retido, evidenciando falha de generalização. Aponta causas plausíveis: **sobreajuste a ruído**; **excitação insuficiente** do ensaio (um único degrau não excita toda a faixa de operação nem separa bem as duas constantes de tempo); quantização do encoder não modelada; atrito não linear ausente do modelo. A melhor resposta cita a **verificação cruzada de ganho estático** como checagem barata: comparar a razão $\omega/V$ medida em regime com o valor calculado a partir dos parâmetros identificados, $21{,}2164\ \mathrm{rad/(s\,V)}$ — se as duas divergirem, o ajuste é suspeito mesmo com erro de regressão baixo.

### Questão 33 (Discursiva)

**Contexto:** Um projetista, de posse do modelo em espaço de estados do NexaBot, aloca os polos de malha fechada por realimentação de estados em posições muito mais rápidas que as de malha aberta, buscando um tempo de acomodação muito curto. A simulação mostra que a tensão de comando exigida no transitório ultrapassa amplamente os $24\ \mathrm{V}$ da bateria — em um dos casos, pico de comando da ordem de $81\,667\ \mathrm{V}$.

**Enunciado:** Apresente uma análise contendo: (a) o significado técnico de o par (matriz de estados, matriz de entrada) ser controlável e como isso se verifica; (b) por que a controlabilidade não garante implementabilidade física; (c) o mecanismo pelo qual exigir dinâmica mais rápida aumenta o esforço de controle; (d) como reformular o problema para obter um compromisso que respeite os $24\ \mathrm{V}$.

**Resposta esperada:**

> Resposta de qualidade define **controlabilidade** como a existência de uma entrada capaz de levar o estado de qualquer condição inicial a qualquer condição final em tempo finito, verificável pelo **posto pleno da matriz de controlabilidade**; e observa que, sendo o par controlável, a alocação arbitrária de polos é matematicamente possível. Explica em seguida que a formulação da controlabilidade **não impõe qualquer restrição de amplitude** à entrada: ela garante que existe um sinal, não que esse sinal caiba no atuador. Descreve o mecanismo: afastar os polos de malha fechada da origem exige que o erro seja anulado em menos tempo, o que só se obtém com ganhos de realimentação maiores e, portanto, com picos de comando maiores no transitório — daí um pico da ordem de dezenas de milhares de volts para uma especificação agressiva, contra $24\ \mathrm{V}$ disponíveis. Aponta que o efeito prático de ignorar isso é a **saturação**: o sistema real não executa a dinâmica projetada, e a resposta observada difere da simulada. Na reformulação, propõe o **regulador linear quadrático**, ajustando as matrizes de ponderação $Q$ e $R$ para penalizar mais o esforço de controle — trocando a especificação rígida de polos por um compromisso explícito entre desempenho e energia —, ou relaxando a especificação de tempo de acomodação. A melhor resposta conclui que o limite de $24\ \mathrm{V}$ é um **requisito de projeto**, não uma inconveniência a contornar em simulação.

### Questão 34 (Discursiva)

**Contexto:** A equipe do NexaBot sintonizou o controlador de velocidade pelo método clássico de Ziegler-Nichols, a partir de $K_u \approx 3{,}6911$ e $T_u \approx 18{,}32\ \mathrm{ms}$, obtendo $K_p \approx 2{,}21$, $K_i \approx 242$ e $K_d \approx 0{,}0051$. A resposta ao degrau apresenta sobressinal superior a $20\%$. O requisito de projeto exige sobressinal inferior a $10\%$ para não saturar o atuador durante manobras.

**Enunciado:** Apresente uma análise contendo: (a) o que representam o ganho crítico e o período crítico; (b) pelo menos três métricas objetivas de aceitação de uma malha de controle; (c) o mecanismo pelo qual a regra clássica de Ziegler-Nichols tende a produzir sobressinal elevado; (d) uma alternativa de sintonia justificada, compatível com o requisito.

**Resposta esperada:**

> Resposta de qualidade define o **ganho crítico** $K_u$ como o ganho proporcional que leva a malha ao limite de estabilidade, com oscilação sustentada de amplitude constante, e o **período crítico** $T_u$ como o período dessa oscilação — os dois parâmetros que a regra de Ziegler-Nichols usa como única informação sobre a planta. Apresenta ao menos três métricas de aceitação corretas entre **sobressinal percentual**, **tempo de subida**, **tempo de acomodação** (faixa de 2%), **erro em regime permanente** e **integral do erro quadrático**, observando que a aceitação deve ser declarada como critério numérico antes da sintonia, não avaliada "a olho" no gráfico. Explica que a regra clássica foi derivada para produzir uma **razão de decaimento de cerca de um quarto por ciclo**, critério que privilegia rejeição rápida de distúrbio e resulta, estruturalmente, em sobressinal na casa de 20% a 25% — não é defeito de aplicação, é o que a regra otimiza. Relaciona isso ao NexaBot: com apenas $5{,}15\ \mathrm{V}$ de folga entre os $18{,}85\ \mathrm{V}$ de regime e os $24\ \mathrm{V}$ do driver, sobressinal elevado leva à saturação. Propõe alternativa justificada — variante de Ziegler-Nichols sem sobressinal, sintonia manual orientada pelas métricas (na disciplina, $K_p = 1{,}3$, $K_i = 15$, $K_d = 0{,}01$, com sobressinal da ordem de $0{,}5\%$) ou outro método —, explicando que reduzir $K_i$ e $K_p$ troca velocidade por margem. A melhor resposta observa que a sintonia só está encerrada quando as métricas declaradas são verificadas por medição, e acrescenta o anti-windup como proteção complementar contra a saturação residual.

### Questão 35 (Discursiva)

**Contexto:** Para sustentar $1{,}0\ \mathrm{m/s}$, o NexaBot exige $18{,}85\ \mathrm{V}$ em regime permanente, restando apenas $5{,}15\ \mathrm{V}$ de folga frente aos $24\ \mathrm{V}$ do driver. Durante uma referência mais agressiva, o comando calculado pelo PID ultrapassa os $24\ \mathrm{V}$, o atuador satura, e a resposta apresenta sobressinal grosseiro e assentamento lento mesmo depois de a referência ser reduzida. Com anti-windup por *back-calculation* ($K_{aw} = 2{,}0$), o tempo de retorno à faixa de 2% cai de $2\,256{,}5\ \mathrm{ms}$ para $872{,}5\ \mathrm{ms}$.

**Enunciado:** Apresente uma análise contendo: (a) o mecanismo do efeito windup; (b) o funcionamento do anti-windup por *back-calculation*, indicando que sinal é realimentado e onde; (c) a leitura dos números medidos; (d) por que esse mecanismo é especialmente necessário no NexaBot, e não apenas boa prática genérica.

**Resposta esperada:**

> Resposta de qualidade explica o **windup**: enquanto o atuador está saturado, a saída aplicada é menor que a calculada, o erro não diminui na velocidade que o controlador "espera", e o termo integral continua acumulando — na medição da disciplina, o integrador chega a $9\,251{,}6$ no instante da comutação. Quando a referência cai e o erro muda de sinal, esse acúmulo precisa primeiro ser "descarregado" antes que o comando volte à faixa linear, e é isso que produz sobressinal grosseiro e assentamento lento **depois** de o distúrbio ter cessado. Descreve o **back-calculation**: calcula-se a diferença entre o comando computado e o comando efetivamente aplicado após a saturação, multiplica-se por um ganho $K_{aw}$ e **realimenta-se essa diferença no próprio termo integral**, descontando a parcela que o atuador não conseguiu entregar — o integrador para de crescer enquanto houver saturação. Lê os números corretamente: a recuperação passa de $2\,256{,}5$ para $872{,}5\ \mathrm{ms}$, cerca de **$2{,}6$ vezes mais rápida**, e o integrador na comutação cai de $9\,251{,}6$ para $4\,668{,}2$; observa que o **pico** de velocidade pós-comutação praticamente não muda (de $154{,}6\%$ para $154{,}4\%$), porque ele é herança da fase saturada — o que o anti-windup muda é a **velocidade de recuperação**, não o pico. Conclui com o orçamento de tensão: com apenas $5{,}15\ \mathrm{V}$ de folga sobre os $18{,}85\ \mathrm{V}$ de regime, o NexaBot satura com facilidade em qualquer manobra mais exigente, de modo que a saturação é regime normal de operação e não exceção — por isso o anti-windup é requisito, não refinamento.

### Questão 36 (Discursiva)

**Contexto:** Um engenheiro decide reduzir o período de amostragem do controlador do NexaBot de $T_s = 5\ \mathrm{ms}$ para $T_s = 1\ \mathrm{ms}$, argumentando que "amostrar mais rápido só pode melhorar o resultado". Em seguida, acopla o controlador discretizado à planta por co-simulação FMI 3.0 usando passo de comunicação de $50\ \mathrm{ms}$ entre os dois FMUs. A constante de tempo modal dominante é de $138{,}6\ \mathrm{ms}$ (aproximação mecânica desacoplada: $148{,}1\ \mathrm{ms}$).

**Enunciado:** Apresente uma análise contendo: (a) o critério que relaciona o período de amostragem às constantes de tempo da planta e a avaliação da escolha de $1\ \mathrm{ms}$; (b) o que é o erro de acoplamento em co-simulação FMI; (c) por que ele depende do passo de comunicação, grandeza distinta do período de amostragem interno; (d) por que $50\ \mathrm{ms}$ compromete a co-simulação mesmo com o controlador a $1\ \mathrm{ms}$.

**Resposta esperada:**

> Resposta de qualidade aplica o critério de **10 a 30 amostras por constante de tempo dominante**: com $T_s = 5\ \mathrm{ms}$ obtêm-se $138{,}6 \div 5 \approx 27{,}7$ amostras, dentro da faixa; com $T_s = 1\ \mathrm{ms}$, $138{,}6 \div 1 \approx 139$ amostras — **desnecessariamente conservador**, não "melhor". Explica o custo real de amostrar rápido demais: mais ciclos de CPU e de comunicação por segundo, maior sensibilidade a ruído de quantização do encoder na ação derivativa e menor tolerância a jitter, sem ganho de desempenho, já que a planta não tem dinâmica relevante nessa faixa. Define **erro de acoplamento** como a discrepância introduzida pelo fato de que, entre dois instantes de troca, cada FMU **extrapola** a entrada do outro — tipicamente mantendo-a constante —, de modo que ambos avançam sobre informação desatualizada; ele não é erro do integrador interno de nenhum dos dois, e sim do esquema de acoplamento. Distingue claramente as duas grandezas: o período de amostragem $T_s$ governa o **controlador**, enquanto o passo de comunicação $H$ governa a **troca de dados entre FMUs**, e reduzir um não compensa aumentar o outro. Conclui quantitativamente: com $H = 50\ \mathrm{ms}$ e $T_s = 1\ \mathrm{ms}$, ocorrem 50 ciclos de controle entre duas trocas, 49 deles sobre um estado de planta congelado; o passo de comunicação passa a ser da ordem de um terço da constante de tempo dominante, e a co-simulação deixa de representar a planta — o gargalo migrou para o acoplamento. A melhor resposta observa que o passo de comunicação também deve ser escolhido contra as constantes de tempo, e não contra a conveniência de reduzir sobrecarga.

### Questão 37 (Discursiva)

**Contexto:** O requisito original de segurança do NexaBot foi escrito como "o robô deve parar rapidamente se houver obstáculo". Ao tentar formalizá-lo, a equipe percebe que ele admite pelo menos três interpretações incompatíveis para "parar" (torque zerado, freio acionado, velocidade nula) e nenhum prazo numérico para "rapidamente".

**Enunciado:** Apresente uma resposta contendo: (a) por que um requisito assim é inadequado como entrada de um verificador formal, com um exemplo para cada ambiguidade; (b) a reescrita do requisito como propriedade formalizável, explicitando evento de disparo, ação exigida e prazo; (c) a diferença entre propriedade de segurança e de vivacidade, classificando o requisito reescrito e um segundo requisito de natureza distinta.

**Resposta esperada:**

> Resposta de qualidade explica que um verificador formal só decide sobre propriedades **precisamente definidas** sobre o modelo: se "parar" não estiver definido, não há predicado a avaliar, e duas equipes podem "verificar" o mesmo requisito com resultados opostos. Dá exemplo para cada ambiguidade: torque zerado ainda permite o robô deslizar por inércia e atravessar o obstáculo; freio acionado é ação distinta, com hardware e tempo de atuação próprios; velocidade nula é a única condição que garante parada efetiva, mas depende da massa e da rampa. Sobre "rapidamente", mostra que sem prazo qualquer implementação é conforme — $150\ \mathrm{ms}$ ou $15\ \mathrm{s}$ passam igualmente. Reescreve o requisito no espírito do REQ-SAFE-006, explicitando os três elementos: **evento de disparo** — a detecção de obstáculo pelo sensor; **ação exigida** — o comando de torque levado a zero; **prazo** — no máximo $150\ \mathrm{ms}$, equivalentes a 30 períodos de $5\ \mathrm{ms}$, contados a partir da detecção. Distingue **segurança** ("algo ruim nunca acontece", violável por um traço finito, e é por isso que o verificador consegue exibir um contraexemplo finito) de **vivacidade** ("algo bom eventualmente acontece", cuja violação exige um traço infinito). Classifica com justificativa: o requisito reescrito é de **segurança** — existe um instante identificável em que o prazo é estourado; e classifica um segundo requisito de natureza diferente, como a retomada de operação após a remoção do obstáculo, como de **vivacidade**. A melhor resposta observa que formalizar não é burocracia: é o ato que transforma uma discussão de opinião sobre "rápido o bastante" em uma fronteira numérica verificável.

### Questão 38 (Discursiva)

**Contexto:** Um bug foi introduzido no supervisor de segurança do NexaBot: por erro de transição, o torque pode permanecer habilitado por um ciclo mesmo com obstáculo detectado. O verificador de modelos, explorando exaustivamente o espaço de estados alcançável, relata a violação de REQ-SAFE-001 e devolve a sequência exata de entradas que leva o supervisor da condição inicial ao estado de falha.

**Enunciado:** Apresente uma resposta contendo: (a) o que exatamente um contraexemplo demonstra e por que é a saída mais valiosa de um verificador, em contraste com uma simulação que passa; (b) por que, mesmo corrigido o bug e satisfeita a propriedade, isso não prova que o NexaBot físico se comportará corretamente; (c) a relação entre cobertura de transições e cobertura de linhas de código.

**Resposta esperada:**

> Resposta de qualidade explica que o contraexemplo é uma **testemunha construtiva**: não afirma apenas que a propriedade falha, mas exibe a sequência concreta de entradas que a faz falhar, reproduzível passo a passo na bancada e conversível em caso de teste de regressão. Contrasta com a simulação: uma bateria que passa mostra que os cenários **escolhidos** não revelaram falha, o que é evidência fraca, ao passo que a exploração exaustiva percorre todos os estados alcançáveis do modelo no escopo declarado — quando não encontra violação, a garantia vale para todo esse espaço, não para uma amostra. Sobre o limite, distingue com clareza **modelo** e **sistema físico**: o verificador prova propriedades do autômato, sob as hipóteses que ele codifica (tempo discreto em períodos de $5\ \mathrm{ms}$, sensor que não falha, ausência de jitter, escopo de estados declarado); o robô real está sujeito a falha de sensor, atraso de comunicação, jitter de escalonamento e erro de implementação do código que executa o autômato — nenhum deles dentro do modelo. Conclui que verificação formal transfere confiança **do modelo para o código gerado a partir dele**, e que o elo com o físico depende de SIL, HIL e ensaio. Sobre cobertura, explica que **100% de cobertura de linha** significa que cada instrução foi executada ao menos uma vez, o que pode ser obtido por poucos casos; **cobertura de transição** exige percorrer cada par (estado, evento) do autômato, e uma transição crítica — sair da emergência com obstáculo ainda presente — pode compartilhar linhas com outra já executada e jamais ser exercitada. A melhor resposta conclui que a métrica precisa ser escolhida contra o **modelo do comportamento**, não contra o texto do código.

### Questão 39 (Discursiva)

**Contexto:** No teste de *software-in-the-loop* do NexaBot, compara-se, amostra a amostra, a saída do modelo de referência em Python (`double`) com a do código C gerado, também em `double`. O erro máximo absoluto observado ao longo de toda a sequência de teste é de $4{,}7\times10^{-3}$. O épsilon de máquina do `double` é da ordem de $2{,}2\times10^{-16}$, e ambas as implementações deveriam calcular exatamente a mesma equação de diferenças.

**Enunciado:** Apresente uma resposta contendo: (a) por que um erro dessa magnitude deve ser lido como defeito, e não como ruído de arredondamento; (b) pelo menos duas causas plausíveis de defeito que produziriam erro dessa ordem; (c) por que a mesma discrepância exigiria tolerância diferente se o código gerado usasse ponto fixo Q16.16; (d) como a suíte de regressão sustenta essa conclusão.

**Resposta esperada:**

> Resposta de qualidade estabelece a comparação de ordens de grandeza: $4{,}7\times10^{-3}$ é cerca de **treze ordens de grandeza** acima do épsilon de máquina do `double`; como as duas implementações usam o mesmo tipo e a mesma equação, o resultado esperado é erro **exatamente zero** ou, no limite, acúmulo de poucas unidades de último bit. Conclui que uma diferença dessa magnitude não é explicável por arredondamento e indica **defeito determinístico** na tradução do modelo para código — a tolerância adotada na disciplina, $10^{-9}\ \mathrm{V}$, já é folgada frente ao épsilon e ainda assim é violada por várias ordens de grandeza. Apresenta ao menos duas causas plausíveis: **ordem de operações divergente** entre as duas implementações (agrupamento distinto que muda o resultado além do arredondamento apenas se combinado com outro erro, ou uso de uma variável de estado defasada de um ciclo); **erro de sinal ou de coeficiente no template** de geração; **truncamento indevido** ao converter um parâmetro; uso de estado não inicializado; discretização diferente do termo derivativo filtrado. Sobre o ponto fixo, explica que o **Q16.16 tem erro de quantização previsto por construção**, com resolução $2^{-16} \approx 1{,}5\times10^{-5}$ que se propaga pelo acúmulo do integrador e pelo filtro derivativo — comparar essa variante contra a tolerância do `double` reprovaria uma implementação correta, e por isso a disciplina adota tolerância física de $0{,}5\ \mathrm{V}$, definida pelo que é irrelevante para o atuador, não pela aritmética. Fecha com a regressão: 25 combinações aleatórias de ganhos geradas por teste baseado em propriedades, cada uma comparada contra a tolerância adequada à sua aritmética — é essa suíte, e não uma comparação pontual de um par de ganhos, que sustenta a alegação de equivalência a cada mudança no repositório.

### Questão 40 (Discursiva)

**Contexto:** O NexaBot chega ao final da disciplina com modelo, propriedades verificadas no escopo declarado, código C gerado, equivalência SIL medida, testes com cobertura medida, ensaio HIL e uma matriz de rastreabilidade que expõe uma lacuna: o REQ-SAFE-007 não possui teste da trajetória contínua. A integração contínua está verde. Um colega conclui que esse conjunto "certifica" o sistema segundo a DO-178C ou a ISO 26262.

**Enunciado:** Apresente uma resposta contendo: (a) a diferença entre produzir evidências e certificar um sistema, situando o que a matriz e a suíte sustentam; (b) como uso, impacto de erro e capacidade de detecção posterior determinam a análise de confiança e a eventual qualificação de ferramenta; (c) o papel da independência de verificação; (d) o que falta no pipeline e por que a lacuna explícita não é compensada por mais arquivos nem por uma CI verde.

**Resposta esperada:**

> Resposta de qualidade separa com clareza os dois planos: o pipeline **produz evidências objetivas e rastreáveis** — requisitos formalizados, propriedades verificadas no escopo declarado, equivalência modelo-código medida com número, cobertura medida, matriz ligando requisito a modelo, código e teste — enquanto **certificar é um processo organizacional**, conduzido perante uma autoridade ou avaliador independente, com dados de ciclo de vida completos, plano de certificação, evidência de conformidade de processo e revisão externa. As evidências são **insumo** desse processo, nunca substituto. Sobre ferramentas, explica que a necessidade de **qualificação** não decorre da licença ser aberta ou comercial, e sim de três fatores: o **uso** que se faz da ferramenta (se ela pode inserir um erro no produto ou se apenas pode deixar de detectar um erro existente), o **impacto** de um erro por ela introduzido, e se esse erro **seria detectado** por verificação posterior — um gerador de código cujo resultado é verificado por SIL independente exige análise diferente de um gerador cuja saída vai direto ao alvo. Explica a **independência de verificação**: quem verifica não deve ser quem projetou, para que hipóteses erradas não sejam reproduzidas nos dois lados; um pipeline em que a mesma pessoa escreve o modelo, o gerador e o teste tem correlação de erros que nenhuma métrica de cobertura revela. Sobre a lacuna, é assertiva: o REQ-SAFE-007 sem teste de trajetória contínua é uma **lacuna real de cobertura de requisito**, e a matriz cumpre seu papel justamente ao **exibi-la** em vez de escondê-la; uma CI verde só informa que os testes que existem passaram, e nunca que os testes necessários existem. Conclui que faltam ao pipeline, entre outros elementos, o teste ausente, análise formal de confiança nas ferramentas e eventual qualificação aplicável, independência adequada, dados completos de ciclo de vida e avaliação externa — e que acrescentar arquivos não converte evidência em certificação.

---

## Feedbacks (questões objetivas 1–30)

### Questão 1

- **a.** *Correta!* Ambas verdadeiras e a Razão justifica a Asserção. É justamente porque a evolução contínua da planta é intercalada por eventos discretos de amostragem e atualização de comando que o comportamento emerge do acoplamento — e verificar cada domínio isoladamente deixa passar exatamente os defeitos que nascem na fronteira entre eles.
- **b.** Incorreta. A Razão **justifica** a Asserção: o acoplamento descrito na Razão é a causa direta da exigência enunciada na Asserção.
- **c.** Incorreta. A Razão é verdadeira: o sistema híbrido, com trechos contínuos intercalados por eventos discretos, é a definição operacional de um CPS.
- **d.** Incorreta. A Asserção é verdadeira: verificar planta e controlador isoladamente não cobre o comportamento acoplado.
- **e.** Incorreta. Ambas as proposições são verdadeiras.

### Questão 2

- **a.** Incorreta. A Razão não justifica a Asserção: o V-Model é um arranjo de processo de desenvolvimento e nada diz sobre o ganho estático do motor.
- **b.** *Correta!* As duas proposições são verdadeiras — $24 \times 21{,}2164 \approx 509{,}2\ \mathrm{rad/s}$, que com redutor $20{:}1$ e roda de $50\ \mathrm{mm}$ dá $\approx 1{,}273\ \mathrm{m/s}$; e o V-Model de fato organiza decomposição e verificação em ramos espelhados. Mas são afirmações **independentes**: a segunda não explica a primeira.
- **c.** Incorreta. A Razão é verdadeira: essa é a descrição correta do V-Model.
- **d.** Incorreta. A Asserção é verdadeira: o cálculo confere com o ganho estático medido na disciplina.
- **e.** Incorreta. Ambas são verdadeiras.

### Questão 3

- **a.** Incorreta. A Razão é falsa, portanto não pode justificar coisa alguma.
- **b.** Incorreta. A Razão é falsa.
- **c.** *Correta!* A Asserção é verdadeira: com $18{,}85\ \mathrm{V}$ fixos e carga de $0{,}05\ \mathrm{N\,m}$, a velocidade cai para cerca de $0{,}929\ \mathrm{m/s}$, erro de $\approx 7{,}1\%$ que **persiste**. A Razão é falsa por definição de malha aberta: ela **não mede a saída** — não existe realimentação, e o problema não é ganho insuficiente, é ausência de medição.
- **d.** Incorreta. A Asserção é verdadeira: é exatamente o comportamento medido no laboratório da Aula 1.
- **e.** Incorreta. A Asserção é verdadeira.

### Questão 4

- **a.** Incorreta. A Asserção é falsa: controlabilidade não fala de amplitude de comando.
- **b.** Incorreta. A Asserção é falsa.
- **c.** Incorreta. A Razão é verdadeira: posto pleno da matriz de controlabilidade é exatamente essa garantia de existência.
- **d.** *Correta!* A Asserção é falsa: a controlabilidade garante que **existe** uma entrada, sem qualquer restrição sobre a sua amplitude — a alocação pode exigir picos de dezenas de milhares de volts contra os $24\ \mathrm{V}$ disponíveis. A Razão é verdadeira e é justamente a formulação que expõe esse limite.
- **e.** Incorreta. A Razão é verdadeira.

### Questão 5

- **a.** Incorreta. Ambas as proposições são falsas.
- **b.** Incorreta. Ambas as proposições são falsas.
- **c.** Incorreta. A Asserção é falsa: o polo elétrico ($-335{,}96\ \mathrm{rad/s}$, $\tau_e \approx 2{,}9\ \mathrm{ms}$) é o **mais rápido**, não o mais lento.
- **d.** Incorreta. A Razão é falsa: a separação é de cerca de duas ordens de grandeza (razão próxima de 47), e é ela que **autoriza** desprezar o polo elétrico — não o contrário.
- **e.** *Correta!* As duas são falsas. O polo elétrico é o rápido, e pode ser desprezado **por isso**; e a separação, longe de tornar dispensável distinguir as dinâmicas, é exatamente a informação que permite a redução de ordem com segurança.

### Questão 6

- **a.** *Correta!* Ambas verdadeiras e a Razão justifica a Asserção: é o recálculo contínuo do comando a partir do erro medido que permite à malha fechada rejeitar um distúrbio de carga desconhecido, sem que ele precise ser modelado de antemão.
- **b.** Incorreta. A Razão **justifica** a Asserção — descreve o mecanismo pelo qual a malha fechada sustenta a referência.
- **c.** Incorreta. A Razão é verdadeira: é a definição de realimentação negativa.
- **d.** Incorreta. A Asserção é verdadeira: é o resultado medido no laboratório da Aula 5.
- **e.** Incorreta. Ambas são verdadeiras.

### Questão 7

- **a.** Incorreta. A Razão não justifica a Asserção: Ziegler-Nichols é um método de sintonia e nada diz sobre a identidade $S+T=1$, que é uma propriedade algébrica da malha.
- **b.** *Correta!* As duas são verdadeiras — $S+T=1$ vale identicamente em toda frequência para realimentação unitária, e Ziegler-Nichols de fato usa $K_u$ e $T_u$ do limite de oscilação sustentada. São conteúdos **independentes**.
- **c.** Incorreta. A Razão é verdadeira: é a descrição correta do método do ganho crítico.
- **d.** Incorreta. A Asserção é verdadeira: a identidade decorre diretamente das definições $S = 1/(1+L)$ e $T = L/(1+L)$.
- **e.** Incorreta. Ambas são verdadeiras.

### Questão 8

- **a.** Incorreta. A Razão é falsa: a faixa recomendada não é de 100 a 300 amostras.
- **b.** Incorreta. A Razão é falsa.
- **c.** *Correta!* A Asserção é verdadeira: $138{,}6 \div 5 \approx 27{,}7$ amostras por constante de tempo. A Razão é falsa: a faixa recomendada é de **10 a 30** amostras — com 100 a 300, o $T_s$ do NexaBot estaria fora, e a conclusão da Asserção se inverteria.
- **d.** Incorreta. A Asserção é verdadeira: o cálculo confere.
- **e.** Incorreta. A Asserção é verdadeira.

### Questão 9

- **a.** Incorreta. A Asserção é falsa: o windup não se resolve sozinho.
- **b.** Incorreta. A Asserção é falsa.
- **c.** Incorreta. A Razão é verdadeira: é a descrição correta do *back-calculation*.
- **d.** *Correta!* A Asserção é falsa: ao sair da saturação, o integrador carrega o acúmulo da fase saturada e precisa "descarregá-lo" antes que o comando volte à faixa linear — na medição da disciplina, a recuperação leva $2\,256{,}5\ \mathrm{ms}$ sem mecanismo dedicado, contra $872{,}5\ \mathrm{ms}$ com anti-windup. A Razão é verdadeira e descreve exatamente o mecanismo que resolve o problema.
- **e.** Incorreta. A Razão é verdadeira.

### Questão 10

- **a.** Incorreta. Ambas as proposições são falsas.
- **b.** Incorreta. Ambas as proposições são falsas.
- **c.** Incorreta. A Asserção é falsa: passo de comunicação e período de amostragem são grandezas **independentes** em uma co-simulação FMI.
- **d.** Incorreta. A Razão é falsa: espaçar a comunicação altera, sim, o resultado — na medição da disciplina, o erro cresce mais de 200 vezes ao passar de $1\ \mathrm{ms}$ para $50\ \mathrm{ms}$.
- **e.** *Correta!* As duas são falsas. O passo de comunicação $H$ governa a troca entre FMUs e pode ser escolhido independentemente do $T_s$ interno do controlador; e ampliá-lo degrada a co-simulação, porque entre duas trocas cada FMU avança sobre uma entrada congelada — com $H = 50\ \mathrm{ms}$ e $T_s = 5\ \mathrm{ms}$, nove de cada dez ciclos usam estado desatualizado.

### Questão 11

- **a.** *Correta!* Ambas verdadeiras e a Razão justifica a Asserção: é precisamente a ausência de evento de disparo, ação e prazo que impede a construção de um predicado avaliável — sem isso, duas equipes podem "verificar" o mesmo texto com resultados opostos.
- **b.** Incorreta. A Razão **justifica** a Asserção: ela enuncia a causa exata da inadequação.
- **c.** Incorreta. A Razão é verdadeira: "parar" admite torque zerado, freio acionado ou velocidade nula, e "rapidamente" não fixa prazo.
- **d.** Incorreta. A Asserção é verdadeira: um verificador formal exige propriedade precisamente definida sobre o modelo.
- **e.** Incorreta. Ambas são verdadeiras.

### Questão 12

- **a.** Incorreta. A Razão não justifica a Asserção: a explosão de estados é uma limitação de escala do método, e não a razão pela qual o contraexemplo é uma sequência de entradas.
- **b.** *Correta!* As duas são verdadeiras — o contraexemplo é de fato a sequência que leva do estado inicial à violação, e a explosão de estados é de fato o principal limite prático da exploração explícita. Mas são fatos **independentes** sobre o método.
- **c.** Incorreta. A Razão é verdadeira: o número de estados alcançáveis cresce combinatoriamente com as variáveis do modelo.
- **d.** Incorreta. A Asserção é verdadeira: é o que torna o contraexemplo reproduzível na bancada e conversível em caso de teste.
- **e.** Incorreta. Ambas são verdadeiras.

### Questão 13

- **a.** Incorreta. A Razão é falsa: as duas coberturas não são equivalentes.
- **b.** Incorreta. A Razão é falsa.
- **c.** *Correta!* A Asserção é verdadeira: uma transição crítica pode compartilhar linhas com outra já executada e nunca ser percorrida. A Razão é falsa: cobertura de linha é medida sobre o **texto do código**, cobertura de transição sobre o **grafo de estados e eventos** do modelo — são métricas distintas, sobre artefatos distintos.
- **d.** Incorreta. A Asserção é verdadeira: é exatamente a lacuna que a geração de testes a partir do modelo revela.
- **e.** Incorreta. A Asserção é verdadeira.

### Questão 14

- **a.** Incorreta. A Asserção é falsa: código gerado não se edita à mão, ainda que com comentário.
- **b.** Incorreta. A Asserção é falsa.
- **c.** Incorreta. A Razão é verdadeira: o cabeçalho gerado registra requisitos, modelo, hash SHA-256 dos parâmetros e data de geração.
- **d.** *Correta!* A Asserção é falsa: código gerado é **artefato derivado**, e editá-lo quebra a rastreabilidade — na próxima geração a edição é sobrescrita, e o hash do cabeçalho deixa de corresponder ao binário em campo. O ajuste correto se faz no modelo, regerando o código. A Razão é verdadeira e é justamente o que torna a edição manual detectável.
- **e.** Incorreta. A Razão é verdadeira.

### Questão 15

- **a.** Incorreta. Ambas as proposições são falsas.
- **b.** Incorreta. Ambas as proposições são falsas.
- **c.** Incorreta. A Asserção é falsa: $4{,}7\times10^{-3}$ está cerca de treze ordens de grandeza acima do épsilon de máquina do `double` e não é explicável por arredondamento.
- **d.** Incorreta. A Razão é falsa: o épsilon de máquina do `double` é da ordem de $2{,}2\times10^{-16}$, não de $10^{-3}$.
- **e.** *Correta!* As duas são falsas. Como ambas as implementações usam `double` e a mesma equação de diferenças, o esperado é erro exatamente nulo — a tolerância adotada na disciplina, $10^{-9}\ \mathrm{V}$, já é folgada e ainda assim seria violada. Um erro dessa magnitude é **defeito determinístico** de tradução, não ruído numérico.

### Questão 16

- **a.** *Correta!* $400 \div 21{,}2164 \approx 18{,}85\ \mathrm{V}$. É a tensão de regime que sustenta o cruzeiro de $1{,}0\ \mathrm{m/s}$ sem carga, e o número que define o orçamento de tensão da disciplina: sobram apenas $5{,}15\ \mathrm{V}$ até o limite do driver.
- **b.** Incorreta. Multiplicar a velocidade pelo raio da roda não produz tensão — a operação não fecha dimensionalmente.
- **c.** Incorreta. O driver entrega até $24\ \mathrm{V}$, mas em regime aplica apenas o necessário para sustentar a velocidade pedida.
- **d.** Incorreta. Confunde o ganho estático, em $\mathrm{rad/(s\,V)}$, com uma tensão.
- **e.** Incorreta. Iguala numericamente velocidade angular e tensão, ignorando o ganho estático.

### Questão 17

- **a.** Incorreta. Subestima a constante de tempo mecânica em uma ordem de grandeza; a razão entre as duas é próxima de 47, não de 5.
- **b.** *Correta!* $\tau = 1/|p|$, portanto $1 \div 335{,}96 \approx 2{,}98\ \mathrm{ms}$ (dinâmica elétrica, coerente com $L/R \approx 2{,}92\ \mathrm{ms}$) e $1 \div 7{,}215 \approx 139\ \mathrm{ms}$ (dinâmica mecânica, próxima dos $148\ \mathrm{ms}$ da aproximação desacoplada). A razão de cerca de 47 é a separação de escalas que autoriza a redução de ordem.
- **c.** Incorreta. Troca os valores: toma o módulo do polo como se fosse a constante de tempo, invertendo qual dinâmica é a rápida.
- **d.** Incorreta. Usa o valor do polo elétrico diretamente como milissegundos, sem inverter.
- **e.** Incorreta. Polos reais e negativos distintos produzem constantes de tempo distintas; a igualdade só valeria para polos coincidentes.

### Questão 18

- **a.** Incorreta. Subestima o erro; o valor medido em regime é mais que o dobro disso.
- **b.** Incorreta. O valor não confere com o cálculo, e não existe "limite normativo de 5%" aplicável aqui.
- **c.** *Correta!* $(1{,}00 - 0{,}929) \div 1{,}00 \approx 0{,}071$, ou seja, $\approx 7{,}1\%$. O ponto central é que esse erro **persiste indefinidamente**: em malha aberta nada mede a saída, então nada corrige o comando quando a carga muda.
- **d.** Incorreta. O valor não confere, e a causa não é erro de identificação — os parâmetros estão corretos; o que falta é realimentação.
- **e.** Incorreta. Manter a tensão constante é exatamente o que produz o erro, não o que o elimina.

### Questão 19

- **a.** Incorreta. Confunde a velocidade máxima possível com a velocidade de referência especificada.
- **b.** Incorreta. Esse é o valor **sob carga** com tensão de regime, não o máximo do driver sem carga.
- **c.** Incorreta. Superestima o resultado; o cálculo com o ganho estático não chega a esse valor.
- **d.** *Correta!* $24 \times 21{,}2164 \approx 509{,}2\ \mathrm{rad/s}$ e $v = \omega r / N = 509{,}2 \times 0{,}05 \div 20 \approx 1{,}273\ \mathrm{m/s}$. A consequência de projeto é a folga estreita: sobre o cruzeiro de $1{,}0\ \mathrm{m/s}$ resta pouca margem de tensão para a ação transitória, e é por isso que saturação e anti-windup são temas centrais da Unidade 2.
- **e.** Incorreta. Usa a velocidade angular como se fosse linear, ignorando redutor e raio da roda.

### Questão 20

- **a.** Incorreta. Esses são os ganhos do **ajuste manual** apresentado na disciplina, não os produzidos pela regra de Ziegler-Nichols.
- **b.** Incorreta. Usa $K_u$ e $T_u$ diretamente como ganhos, sem aplicar os fatores da regra.
- **c.** Incorreta. Toma os coeficientes da regra ($0{,}6$, $1{,}2$, $0{,}075$) como se fossem os próprios ganhos.
- **d.** Incorreta. Os ganhos estão certos, mas o comportamento não: a regra clássica produz sobressinal elevado, e não uma resposta sem sobressinal.
- **e.** *Correta!* $K_p = 0{,}6 \times 3{,}6911 \approx 2{,}21$; $K_i = 1{,}2 \times 3{,}6911 \div 0{,}01832 \approx 242$; $K_d = 0{,}075 \times 3{,}6911 \times 0{,}01832 \approx 0{,}0051$. A regra foi derivada para uma razão de decaimento de cerca de um quarto por ciclo, o que produz sobressinal na casa de 20% a 25% — com apenas $5{,}15\ \mathrm{V}$ de folga, isso satura o driver no transitório.

### Questão 21

- **a.** *Correta!* $138{,}6 \div 5 \approx 27{,}7$ amostras por constante de tempo dominante, dentro da faixa de 10 a 30 e próximo do seu limite superior — escolha adequada, que ainda deixa margem de CPU e tolerância a jitter.
- **b.** Incorreta. O cálculo está certo, mas $27{,}7$ está **dentro** da faixa recomendada, não abaixo dela.
- **c.** Incorreta. Multiplica em vez de dividir; o número de amostras é a constante de tempo dividida pelo período.
- **d.** Incorreta. Inverte a divisão, obtendo períodos por constante de tempo em vez de amostras.
- **e.** Incorreta. É justamente a constante de tempo da planta que fixa o critério; a frequência do processador é restrição de implementação, não critério de projeto.

### Questão 22

- **a.** Incorreta. Passo de comunicação e período de amostragem são grandezas independentes em uma co-simulação FMI.
- **b.** *Correta!* $50 \div 5 = 10$ ciclos de controle por troca de dados. Em nove deles o controlador atua sobre um estado de planta congelado desde a última troca, e é dessa extrapolação que nasce o erro de acoplamento — que na medição da disciplina cresce mais de 200 vezes em relação ao caso de $1\ \mathrm{ms}$.
- **c.** Incorreta. Conta um ciclo por milissegundo do passo, ignorando que cada ciclo dura $5\ \mathrm{ms}$.
- **d.** Incorreta. O número está certo, mas há consequência sim: o controlador mantém sua taxa, porém alimentado por informação desatualizada.
- **e.** Incorreta. O controlador continua executando normalmente entre trocas — o problema é a entrada que ele usa, não a ociosidade.

### Questão 23

- **a.** Incorreta. O pico praticamente não muda ($154{,}6\%$ contra $154{,}4\%$): ele é herança da fase saturada, não do windup.
- **b.** Incorreta. O valor final do integrador é de fato semelhante, mas o que distingue os casos é o **caminho** até lá — e é ele que define o tempo de recuperação.
- **c.** *Correta!* $2\,256{,}5 \div 872{,}5 \approx 2{,}6$. O anti-windup age sobre a **velocidade de recuperação**, impedindo que o integrador acumule durante a saturação — o valor na comutação cai de $9\,251{,}6$ para $4\,668{,}2$, e é esse acúmulo menor que precisa ser descarregado depois.
- **d.** Incorreta. O anti-windup não impede a saturação, que decorre da referência exigir mais do que os $24\ \mathrm{V}$ permitem; ele trata a **consequência** da saturação sobre o integrador.
- **e.** Incorreta. Sem saturação o termo de *back-calculation* é nulo e o anti-windup não altera coisa alguma.

### Questão 24

- **a.** Incorreta. O pior caso reportado é de 5 períodos, não de um.
- **b.** Incorreta. Confunde o **limite** do requisito com o pior caso medido, que fica bem abaixo dele.
- **c.** Incorreta. Multiplica os períodos pelo prazo em vez de pelo período de amostragem.
- **d.** *Correta!* $5 \times 5 = 25\ \mathrm{ms}$, contra um limite de $150\ \mathrm{ms}$ — equivalente a 30 períodos. O cenário nominal é conforme com folga ampla, o que é diferente de dizer que **todo** cenário é conforme: a varredura de atraso de detecção mostra que a fronteira está em 27 períodos.
- **e.** Incorreta. O autômato temporizado modela o tempo em períodos de amostragem; o pior caso do modelo é determinado sem medição no alvo — a medição em bancada é uma verificação complementar, de outra natureza.

### Questão 25

- **a.** Incorreta. Confunde o **pior caso resultante** (30 períodos) com o **atraso admitido** na entrada, que é a grandeza sob projeto.
- **b.** Incorreta. 31 períodos é o pior caso já em violação, correspondente a $155{,}0\ \mathrm{ms}$.
- **c.** Incorreta. O watchdog trata a ausência de resposta do alvo; ele não substitui o requisito de prazo de parada.
- **d.** Incorreta. 5 períodos é o pior caso do cenário nominal, não o limite do atraso de detecção.
- **e.** *Correta!* A varredura mostra conformidade até 27 períodos de atraso e violação a partir de 28. Como o critério é estrito, o *debounce* precisa garantir atraso **menor que 28 períodos**, isto é, no máximo $140\ \mathrm{ms}$ — um número de projeto para o filtro do sensor, extraído de uma verificação exaustiva, e não de uma estimativa.

### Questão 26

- **a.** *Correta!* A exploração é exaustiva **dentro do modelo e do escopo declarado**: todos os caminhos alcançáveis foram percorridos, o que uma bateria de simulações nunca garante, pois ela cobre apenas os cenários que alguém pensou em escrever.
- **b.** Incorreta. O número de caminhos reflete a estrutura do cenário verificado, e não a qualidade do modelo.
- **c.** Incorreta. A verificação prova propriedades do **modelo**, sob as hipóteses que ele codifica — o comportamento do robô físico depende ainda de SIL, HIL e ensaio.
- **d.** Incorreta. Caminhos do autômato e linhas de código são artefatos distintos, com métricas de cobertura distintas.
- **e.** Incorreta. Exploração exaustiva não é amostragem: acrescentar execuções aleatórias não aumenta uma garantia que já cobre todo o espaço alcançável.

### Questão 27

- **a.** Incorreta. Executar as linhas de uma transição não é o mesmo que percorrer a transição: o par (estado, evento) que a dispara pode nunca ter ocorrido.
- **b.** *Correta!* São métricas sobre artefatos diferentes — o texto do código e o grafo de estados e eventos. Uma transição crítica pode compartilhar linhas com outra já exercitada e permanecer não testada mesmo com 100% de cobertura de linha.
- **c.** Incorreta. Nenhuma métrica de cobertura prova ausência de defeitos; cobertura mede o que foi exercitado, não o que está correto.
- **d.** Incorreta. A transição não exercitada é uma lacuna real da suíte — o gerador de testes a partir do modelo está justamente cumprindo seu papel ao expô-la.
- **e.** Incorreta. Casos aleatórios podem jamais atingir a combinação específica de estado e evento; o caminho é gerar os casos **a partir do modelo**, cobrindo transições por construção.

### Questão 28

- **a.** Incorreta. Duas casas decimais não correspondem à resolução binária de um formato de ponto fixo.
- **b.** Incorreta. $1/16384$ é $2^{-14}$, o que corresponderia a 14 bits fracionários, não 16.
- **c.** *Correta!* Com 16 bits fracionários, a resolução é $2^{-16} = 1/65\,536 \approx 1{,}526\times10^{-5}$. É esse degrau que se propaga pelo acúmulo do integrador e pelo filtro derivativo, e é por isso que a variante Q16.16 é julgada contra tolerância física ($0{,}5\ \mathrm{V}$), e não contra a tolerância do `double`.
- **d.** Incorreta. Esse é o épsilon de máquina do ponto flutuante `double`, aritmética distinta do ponto fixo.
- **e.** Incorreta. A escala do ponto fixo é **fixa** por definição — a resolução constante é justamente a diferença essencial em relação ao ponto flutuante.

### Questão 29

- **a.** Incorreta. A comparação relevante é de cada implementação contra a **sua** tolerância, não de uma contra a outra.
- **b.** Incorreta. A tolerância de $10^{-9}\ \mathrm{V}$ aplica-se à comparação em `double`; aplicá-la ao ponto fixo reprovaria uma implementação correta.
- **c.** Incorreta. A variante Q16.16 é justamente a que vai ao alvo embarcado; verificá-la é essencial, não acessório.
- **d.** *Correta!* Cada aritmética tem a sua tolerância: o `double` deve reproduzir o modelo **exatamente** (erro zero, contra tolerância de $10^{-9}\ \mathrm{V}$), e o Q16.16 tem erro de quantização previsto por construção, mantido abaixo dos $0{,}5\ \mathrm{V}$ que o atuador não distingue. Os 25 casos passam nos dois critérios.
- **e.** Incorreta. Gerar combinações de ganhos por teste baseado em propriedades é precisamente o que torna a regressão mais forte que uma comparação pontual.

### Questão 30

- **a.** Incorreta. A variação entre $0{,}0391$ e $0{,}0442\ \mathrm{ms}$ é pequena e todos os valores permanecem muito abaixo do limite.
- **b.** Incorreta. O veredito está certo, mas a interpretação não: um laço em Python de usuário, sem prioridade de tempo real, não demonstra determinismo equivalente ao de um RTOS.
- **c.** Incorreta. O limite é 10% de $5\ \mathrm{ms}$, ou seja, $0{,}5\ \mathrm{ms}$ — e não $0{,}05\ \mathrm{ms}$.
- **d.** Incorreta. O jitter medido é do laço em Python conversando com um subprocesso por *pipe*; um firmware bare-metal no ESP32 tem jitter ordens de grandeza menor, e os números não são transponíveis.
- **e.** *Correta!* O limite é $0{,}5\ \mathrm{ms}$ e os três valores ficam cerca de uma ordem de grandeza abaixo — aprovado com folga. A ressalva é parte da resposta: o ensaio ensina o **método de medição** e o conceito, não constitui alegação de determinismo de tempo real.
