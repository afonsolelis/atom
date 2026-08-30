# Questionário — Unidade 2

Quantidade obrigatória: 40 questões — 20 de asserção-razão (1 a 20) e 20 de interpretação (21 a 40).
Cinco alternativas por questão (a-e); alternativa correta marcada com `*` imediatamente antes da letra.
Distribuição da letra correta: 8 questões para cada uma das letras a, b, c, d, e, no total das 40 questões.

## Questões

### Asserção-razão

**1.** I. Ao introduzir um polo na origem no controlador $C(s)$ da malha de velocidade do NexaBot, o erro de regime permanente a um distúrbio de torque constante torna-se nulo, para qualquer conjunto de ganhos que mantenha a malha estável.

PORQUE

II. Isso ocorre porque o aumento do ganho proporcional $K_p$, isoladamente, já é suficiente para levar a função de sensibilidade $S(0)$ a zero.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**2.** I. A adição de um deslocamento fixo de tensão, calibrado para a carga média, corrige permanentemente o erro de velocidade do NexaBot em malha aberta, qualquer que seja a carga aplicada.

PORQUE

II. Isso ocorre porque, em malha aberta, a função de sensibilidade $S(s)$ é sempre nula, eliminando qualquer efeito de distúrbio sobre a saída.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

**3.** I. Não é possível tornar as funções de sensibilidade $S(j\omega)$ e complementar $T(j\omega)$ simultaneamente pequenas na mesma faixa de frequência.

PORQUE

II. Como $S(j\omega)+T(j\omega)=1$ para toda frequência, reduzir $S$ nessa faixa implica necessariamente que $T$ se aproxime de 1 na mesma faixa.

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**4.** I. O controlador por alocação de polos da Aula 4 é a estrutura preferida para o NexaBot porque dispensa qualquer sensor de corrente ou velocidade adicional.

PORQUE

II. O PID de saída única realimenta apenas o sinal de velocidade medido pelo encoder, sem exigir medição adicional de corrente.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**5.** I. Sob um torque de carga de $0{,}05\,\mathrm{N\,m}$, a velocidade do NexaBot em malha aberta estabiliza em aproximadamente $0{,}929\,\mathrm{m/s}$, uma queda de cerca de $7{,}07\%$ em relação à referência de $1{,}000\,\mathrm{m/s}$.

PORQUE

II. O ganho estático da planta do NexaBot, de $21{,}2164\,\mathrm{rad/(s\cdot V)}$, foi obtido pela redução simbólica da função de transferência em SymPy na Aula 3.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**6.** I. O termo derivativo do PID do NexaBot é implementado com um filtro de primeira ordem, $K_d\frac{Ns}{s+N}$, em vez da derivada pura.

PORQUE

II. A derivada pura amplifica fortemente o ruído de alta frequência presente na medição de velocidade pelo encoder de quadratura.

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**7.** I. A planta contínua do NexaBot, com dois polos reais e nenhum zero, não entraria em oscilação sustentada sob controle puramente proporcional em tempo contínuo.

PORQUE

II. Isso ocorre porque a sintonia de Ziegler-Nichols pelo ganho crítico só pode ser aplicada a plantas de primeira ordem sem atraso.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**8.** I. Saturação do atuador e efeito *windup* do integrador são o mesmo fenômeno, e qualquer sistema saturado necessariamente sofre *windup* na mesma intensidade.

PORQUE

II. O anti-*windup* por *back-calculation* impede que a saturação do atuador ocorra, atuando diretamente sobre o sinal de tensão aplicado ao motor antes de ele ser limitado.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

**9.** I. Para o degrau de $400\,\mathrm{rad/s}$ do NexaBot com atuador saturado, as quatro sintonias avaliadas apresentam sobressinal muito próximo, entre $24{,}6\%$ e $24{,}8\%$.

PORQUE

II. O ganho crítico $K_u$ do NexaBot foi obtido variando $K_p$ na malha discreta até o par de polos complexos cruzar o círculo unitário em $T_s=5\,\mathrm{ms}$.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**10.** I. Um ganho de anti-*windup* $K_{aw}$ maior é sempre melhor, pois reduz o acúmulo do integrador proporcionalmente, sem qualquer limite prático.

PORQUE

II. O anti-*windup* por *back-calculation* compara a saída calculada $u_{ns}$ com a saída efetivamente aplicada $u$ e realimenta essa diferença ao integrador.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**11.** I. Aumentar o período de amostragem do controlador do NexaBot sempre melhora a margem de estabilidade da malha fechada, pois reduz a frequência de cálculo do PID.

PORQUE

II. A transformação de Tustin e o método de Euler para frente produzem exatamente o mesmo mapa discreto, para qualquer período de amostragem $T_s$.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

**12.** I. O integrador do `DiscretePID` do NexaBot é implementado pela regra de Euler para trás, enquanto a planta contínua $G(s)$ é discretizada pelo equivalente de retenção de ordem zero (ZOH) para análise da malha fechada.

PORQUE

II. O ZOH modela a tensão aplicada pelo PWM como constante entre amostras, reproduzindo o comportamento real da eletrônica de potência.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**13.** I. A margem de estabilidade calculada na varredura de $T_s$ da Aula 7, sem considerar atraso computacional, representa o pior caso real de um microcontrolador em campo.

PORQUE

II. Um ciclo adicional de atraso computacional entre leitura e atuação se comporta como um atraso de transporte $e^{-sT_s}$, subtraindo fase em toda frequência.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**14.** I. Reduzir $T_s$ para ganhar margem de estabilidade tem um custo colateral sobre a estimativa de velocidade por diferença de posição do encoder.

PORQUE

II. Um período de amostragem menor reduz o número de pulsos de encoder acumulados entre amostras consecutivas, tornando a estimativa de velocidade proporcionalmente mais ruidosa.

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**15.** I. Com $T_s=5\,\mathrm{ms}$, a aproximação mecânica desacoplada de $148{,}1\,\mathrm{ms}$ fornece aproximadamente $29{,}6$ amostras por essa escala; usando o polo dominante exato, obtêm-se $27{,}7$ amostras. Ambos os resultados ficam na faixa inicial de $10$ a $30$.

PORQUE

II. Isso ocorre porque a aproximação elétrica $L/R\approx2{,}92\,\mathrm{ms}$ é a escala dominante para a malha de velocidade.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**16.** I. O objetivo central declarado pela sigla FMI é permitir a co-simulação com passo de comunicação fixo, sem qualquer preocupação com a ferramenta de origem do modelo.

PORQUE

II. Um FMU de co-simulação é distribuído como um arquivo `.zip` contendo `modelDescription.xml` e uma biblioteca binária que implementa instanciação, inicialização e avanço no tempo.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**17.** I. Entre pontos de comunicação de uma co-simulação, cada FMU mantém a última entrada recebida constante durante todo o intervalo $H$.

PORQUE

II. O protocolo de acoplamento *Jacobi* impõe que os modelos avancem em paralelo dentro de cada intervalo, usando apenas os valores trocados no início desse intervalo.

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**18.** I. Na co-simulação do NexaBot, o erro relativo cresce continuamente entre $H=1\,\mathrm{ms}$ e $H=10\,\mathrm{ms}$, sem que a malha perca a convergência para o valor correto.

PORQUE

II. O script `verify_fmu.py` compara o FMU em C, amostrado no mesmo passo, contra `nexabot.plant.simulate` em Python, sob entrada em degraus alinhados a $H$.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**19.** I. Para os ganhos manuais do NexaBot, o erro RMS de acoplamento cresce monotonicamente de aproximadamente $0{,}028\%$ em $H=1\,\mathrm{ms}$ para $6{,}23\%$ em $H=50\,\mathrm{ms}$.

PORQUE

II. Isso ocorre porque o mestre de co-simulação troca automaticamente o integrador RK4 interno do FMU pelo método de Euler para frente quando $H$ ultrapassa $10\,\mathrm{ms}$.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**20.** I. A co-simulação existe para permitir que planta e controlador compartilhem um único integrador numérico monolítico, otimizado simultaneamente para os dois domínios físicos.

PORQUE

II. Isso ocorre porque o padrão FMI exige que toda ferramenta de simulação utilize exatamente o mesmo algoritmo de integração interno.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

### Interpretação

**21.** Repetindo o exemplo da Aula 5 para $T_l=0{,}08\,\mathrm{N\,m}$ em vez de $0{,}05\,\mathrm{N\,m}$, usando as mesmas equações de equilíbrio ($R=1{,}2\,\Omega$, $K_t=K_e=0{,}045$, $b=8{,}0\times10^{-5}$, $V=18{,}85\,\mathrm{V}$), qual é a velocidade aproximada em malha aberta e a queda percentual em relação à referência de $1{,}000\,\mathrm{m/s}$?

a. Aproximadamente $0{,}929\,\mathrm{m/s}$, queda de $7{,}07\%$.
*b. Aproximadamente $0{,}887\,\mathrm{m/s}$, queda de $11{,}3\%$.
c. Aproximadamente $0{,}950\,\mathrm{m/s}$, queda de $5{,}0\%$.
d. Aproximadamente $1{,}000\,\mathrm{m/s}$, sem queda, pois a malha aberta compensa automaticamente variações de carga.
e. Aproximadamente $0{,}800\,\mathrm{m/s}$, queda de $20{,}0\%$.

**22.** Um colega argumenta que, para eliminar o erro de regime causado por um distúrbio de carga constante na malha de velocidade do NexaBot, basta aumentar indefinidamente o ganho proporcional $K_p$ de um controlador puramente proporcional, sem adicionar ação integral. Essa afirmação está correta?

a. Sim, pois $K_p$ suficientemente grande sempre leva $S(0)$ exatamente a zero.
b. Não, pois o tipo do sistema depende apenas da planta, nunca do controlador.
c. Sim, desde que um compensador de avanço de fase seja adicionado, dispensando ação integral.
*d. Não: aumentar apenas $K_p$ reduz, mas não elimina, o erro de regime, pois a planta é tipo 0 e um controlador proporcional puro não acrescenta polo na origem a $L(s)$; seria necessária ação integral para tornar a malha tipo 1.
e. Não, pois nenhuma malha realimentada consegue eliminar erro de regime a um distúrbio constante.

**23.** A tensão de regime necessária para sustentar $1{,}0\,\mathrm{m/s}$ no NexaBot é $18{,}85\,\mathrm{V}$, com um driver limitado a $24\,\mathrm{V}$. Qual é a margem de tensão disponível para o transitório de um degrau de $1{,}0\,\mathrm{m/s}$ partindo do repouso, e por que essa margem é relevante para o projeto do PID na Aula 6?

a. $24\,\mathrm{V}$, pois o driver nunca satura abaixo da tensão máxima.
b. $18{,}85\,\mathrm{V}$, pois toda a tensão de regime pode ser usada livremente durante o transitório.
*c. $5{,}15\,\mathrm{V}$, e essa margem estreita é o que torna saturação do atuador e *windup* do integrador problemas reais de projeto, não apenas hipóteses acadêmicas.
d. $21{,}2164\,\mathrm{V}$, correspondente ao ganho estático da planta.
e. $0\,\mathrm{V}$, pois a tensão de regime já consome toda a faixa disponível do driver.

**24.** Um engenheiro propõe projetar $C(s)$ de modo que $T(j\omega)\approx1$ em toda a faixa de frequência, argumentando que isso maximizaria simultaneamente o rastreamento de referência e a rejeição de distúrbios em qualquer frequência. Avalie essa proposta para o NexaBot.

a. Válida, pois $T(j\omega)\approx1$ em toda frequência garante rastreamento perfeito sem custo algum.
b. Válida, pois a identidade $S+T=1$ permite que ambas sejam simultaneamente próximas de $1$.
c. Inválida, pois $S$ e $T$ não têm relação matemática definida entre si.
d. Válida, desde que o encoder de quadratura tenha resolução infinita.
*e. Inválida: como $S+T=1$, ter $T\approx1$ em toda frequência implicaria $S\approx0$ em toda frequência, inclusive nas frequências altas em que o ruído de quantização do encoder é relevante, amplificando esse ruído na tensão de comando em vez de atenuá-lo.

**25.** Um colega argumenta que apenas um controlador por realimentação de estados com alocação de polos, como o da Aula 4, é capaz de garantir erro de regime nulo a um distúrbio de torque constante no NexaBot. Avalie essa afirmação.

*a. Incorreto: basta que o controlador $C(s)$ tenha um polo na origem — como o termo integral do PID — para elevar $L(s)$ a tipo 1 e eliminar o erro de regime, sem exigir realimentação de estados adicional, como a de corrente.
b. Correto, pois somente a realimentação de estados por alocação de polos consegue introduzir um polo na origem em $L(s)$.
c. Correto, pois o PID não pode, por definição, eliminar erro de regime a distúrbios constantes.
d. Incorreto, pois nenhum controlador de saída única pode alterar o tipo do sistema.
e. Correto, mas apenas se um observador de estados for acoplado ao PID.

**26.** Aplicando a fórmula de Ziegler-Nichols para sintonia sem sobressinal, $K_p=0{,}20K_u$, aos valores medidos do NexaBot ($K_u\approx3{,}691$), qual é o valor aproximado de $K_p$ resultante?

a. $2{,}215$
b. $1{,}661$
*c. $0{,}738$
d. $1{,}846$
e. $0{,}200$

**27.** Após calcular $K_u$, $T_u$ e os ganhos da sintonia clássica de Ziegler-Nichols para o NexaBot, um colega os implementa diretamente na malha discreta real, argumentando que "Ziegler-Nichols é um método consagrado, logo é seguro". Avalie essa conduta.

a. Correta, pois Ziegler-Nichols garante estabilidade robusta em qualquer implementação discreta.
*b. Incorreta: a sintonia clássica pode deixar oscilação residual não amortecida na malha discreta real do NexaBot, como observado mesmo sem saturação do atuador; o método fornece um ponto de partida que precisa ser verificado na malha real, não um resultado final.
c. Correta, pois a saturação do atuador elimina qualquer risco de oscilação residual.
d. Incorreta, pois Ziegler-Nichols só pode ser aplicado a plantas instáveis em malha aberta.
e. Correta, desde que o filtro derivativo seja desligado.

**28.** Na demonstração de anti-*windup* do NexaBot, o integrador acumulou $5\,888{,}0$ sem correção e $2\,624{,}96$ com $K_{aw}=1{,}0$. Qual é a redução percentual aproximada do valor acumulado pelo anti-*windup*?

*a. Aproximadamente $55{,}4\%$.
b. Aproximadamente $44{,}6\%$.
c. Aproximadamente $62{,}0\%$.
d. Aproximadamente $38{,}0\%$.
e. Aproximadamente $70{,}0\%$.

**29.** Duas sintonias para o NexaBot produzem sobressinal e tempo de subida quase idênticos sob saturação do atuador, mas a sintonia X deixa oscilação residual de $\pm2{,}3\,\mathrm{rad/s}$ em torno da referência, enquanto a sintonia Y se acomoda sem oscilação. Qual das quatro métricas de aceitação melhor distingue X de Y, e por quê?

a. O sobressinal, pois é a métrica mais sensível a oscilação de longo prazo.
b. O tempo de subida, pois mede diretamente a duração da fase saturada.
c. Nenhuma das quatro métricas apresentadas na aula consegue distinguir as duas sintonias.
d. Apenas a inspeção visual do gráfico, pois métricas numéricas não capturam oscilação residual.
*e. O ISE ($\int e^2\,dt$), pois penaliza erro prolongado no tempo, capturando o custo adicional da oscilação residual que sobressinal e tempo de subida, medidos majoritariamente na fase inicial, não distinguem.

**30.** Um engenheiro aumenta o parâmetro $N$ do filtro derivativo do PID do NexaBot de $20$ para $200$, esperando que isso sempre melhore a resposta do sistema, pois aproxima o filtro do derivativo ideal. Avalie essa expectativa.

a. Correta, pois $N$ maior sempre reduz o tempo de acomodação sem qualquer custo.
b. Correta, pois $N$ não afeta a resposta em frequência do filtro derivativo.
c. Incorreta, pois $N=20$ é o único valor numericamente estável para o `DiscretePID`.
*d. Incorreta: um $N$ maior aproxima o filtro do derivativo ideal, mas também o torna mais sensível ao ruído de alta frequência do encoder; a escolha de $N$ é um compromisso específico da planta e do nível de ruído do sensor, não uma constante a ser maximizada.
e. Incorreta, pois $N$ deveria ser reduzido a zero para eliminar completamente a ação derivativa.

**31.** Um engenheiro propõe usar $T_s=7\,\mathrm{ms}$ para o controlador do NexaBot. Usando a aproximação mecânica desacoplada $JR/(K_tK_e)\approx148\,\mathrm{ms}$, quantas amostras por essa escala de tempo a escolha fornece, aproximadamente, e ela está dentro da faixa inicial de $10$ a $30$ amostras?

*a. Aproximadamente $21{,}1$ amostras, dentro da faixa recomendada.
b. Aproximadamente $14{,}8$ amostras, dentro da faixa recomendada.
c. Aproximadamente $29{,}6$ amostras, dentro da faixa recomendada.
d. Aproximadamente $10{,}6$ amostras, no limite inferior da faixa.
e. Aproximadamente $5{,}3$ amostras, abaixo da faixa recomendada.

**32.** O PWM do driver do NexaBot é quantizado em $2^{12}$ níveis entre $0$ e $24\,\mathrm{V}$. Qual é, aproximadamente, a resolução de tensão de um único nível de PWM?

a. Aproximadamente $23{,}4\,\mathrm{mV}$.
b. Aproximadamente $11{,}7\,\mathrm{mV}$.
*c. Aproximadamente $5{,}86\,\mathrm{mV}$.
d. Aproximadamente $2{,}93\,\mathrm{mV}$.
e. Aproximadamente $46{,}9\,\mathrm{mV}$.

**33.** Na simulação temporal da Aula 7 com $T_s=5\,\mathrm{ms}$, o pico de velocidade é $51{,}59\,\mathrm{rad/s}$ sem atraso computacional adicional e $64{,}37\,\mathrm{rad/s}$ com atraso de um ciclo, para referência de $50\,\mathrm{rad/s}$. Qual interpretação é sustentada pelos dados?

a. O atraso reduz o pico em aproximadamente $25\%$ e melhora a margem de fase.
b. O atraso torna a malha instável, pois qualquer pico acima da referência caracteriza divergência.
c. As duas respostas são idênticas; a diferença é apenas arredondamento de impressão.
d. O atraso duplica o pico e elimina o erro de regime permanente.
*e. O atraso aumenta o pico em aproximadamente $25\%$, mas a resposta ainda converge para $50\,\mathrm{rad/s}$; houve degradação transitória sem perda de estabilidade nesse caso.

**34.** Um estudante pergunta por que a planta $G(s)$ do NexaBot é discretizada por ZOH para a análise de malha fechada da Aula 7, enquanto o integrador do controlador usa Euler para trás. Qual justificativa é correta?

a. Porque Tustin é numericamente instável para plantas de segunda ordem.
*b. Porque o ZOH reproduz o comportamento real do PWM, que mantém a tensão constante entre amostras, enquanto o controlador é código livre para adotar a regra de integração mais conveniente à implementação embarcada.
c. Porque Euler para trás não pode ser aplicado a controladores PID.
d. Porque ZOH e Euler para trás produzem exatamente o mesmo mapa discreto para a planta do NexaBot.
e. Porque a planta do NexaBot não pode ser discretizada por nenhum método além do ZOH.

**35.** A Aula 7 encontrou cruzamento do critério linear perto de $T_s\approx27{,}70\,\mathrm{ms}$ e classificação de instabilidade na simulação saturada perto de $44{,}34\,\mathrm{ms}$, enquanto o valor nominal é $5\,\mathrm{ms}$. Um colega conclui que essa margem torna irrelevante qualquer *jitter* de alguns milissegundos em um microcontrolador real. Avalie essa conclusão.

a. Correta, pois a margem calculada já representa o pior caso de qualquer implementação real.
b. Correta, pois *jitter* não afeta a fase da malha discreta.
c. Incorreta, pois a margem deveria ter sido medida em amostras por $\tau_e$, e não por $\tau_m$.
*d. Incorreta: a margem foi calculada em regime, sem atraso computacional adicional; um pico isolado de *jitter* que leve um ciclo a um valor bem acima do nominal, ou um atraso sistemático de um ciclo, reduz essa margem já otimista, e o pior caso de campo pode ser mais severo do que a varredura nominal sugere.
e. Incorreta, pois *jitter* só afeta sistemas com ação derivativa.

**36.** O laboratório da Aula 8 mede dois erros distintos. A verificação isolada do FMU em C contra `nexabot.plant.simulate`, sob a mesma entrada e o mesmo passo, encontra erros máximos da ordem de $10^{-10}\%$ em velocidade e $10^{-8}\%$ em corrente. Já a co-simulação fechada contra uma referência de passo fino mede erro RMS de $0{,}028\%$, $0{,}254\%$, $0{,}533\%$, $1{,}078\%$ e $6{,}230\%$ para $H$ de 1, 5, 10, 20 e 50 ms. Qual afirmação caracteriza corretamente essa diferença?

a. São o mesmo erro medido de duas formas equivalentes, e ambos devem ser sempre numericamente idênticos.
b. O erro de verificação numérica do FMU é sempre maior, pois inclui o erro de acoplamento como subconjunto.
c. Nenhum dos dois erros cresce com $H$; ambos permanecem constantes independentemente do passo de comunicação.
d. Apenas o erro de acoplamento existe; o erro de verificação numérica é uma medida irrelevante, introduzida apenas por rigor formal.
*e. São erros de naturezas diferentes: a verificação isolada mede a fidelidade da implementação C sob entradas idênticas; o erro de acoplamento mede o efeito de trocar dados apenas nos pontos espaçados por $H$, por isso cresce mesmo quando o FMU isolado está numericamente correto.

**37.** A atividade prática da Aula 8 adota erro RMS máximo de $1\%$ como critério de fidelidade e pede uma bisseção entre os pontos medidos. A tabela apresenta $0{,}533\%$ em $H=10\,\mathrm{ms}$ e $1{,}078\%$ em $H=20\,\mathrm{ms}$. Qual conclusão é correta?

a. O maior valor aprovado entre os cinco pontos é $20\,\mathrm{ms}$, pois $1{,}078<1$.
b. O cruzamento deve estar abaixo de $5\,\mathrm{ms}$, pois qualquer erro diferente de zero reprova a co-simulação.
c. A tabela já prova que o cruzamento ocorre exatamente em $15\,\mathrm{ms}$, sem necessidade de novas execuções.
*d. Entre os pontos medidos, $10\,\mathrm{ms}$ é o maior aprovado; o cruzamento do limiar está entre $10$ e $20\,\mathrm{ms}$ e precisa ser refinado por novas simulações.
e. O limiar de $1\%$ é uma propriedade universal do padrão FMI, independente do projeto.

**38.** Diante dos erros elevados observados em $H=20\,\mathrm{ms}$ e $H=50\,\mathrm{ms}$, um engenheiro conclui que a implementação em C da planta no FMU deve estar incorreta. Avalie essa conclusão.

a. Correta, pois qualquer erro observado na co-simulação decorre exclusivamente de erro de implementação do FMU.
b. Correta, desde que o erro exceda $100\%$.
*c. Não necessariamente: `verify_fmu.py` já isolou a implementação do FMU sob a mesma entrada e encontrou erro próximo do ruído de ponto flutuante; a diferença crescente na co-simulação é compatível com erro de acoplamento causado pelo passo de comunicação, não com defeito no C da planta.
d. Incorreta, pois FMUs nunca podem ser verificados isoladamente antes da co-simulação.
e. Correta, pois o `modelDescription.xml` não pode declarar corretamente entradas e saídas de um modelo em C.

**39.** Um colega argumenta que reduzir o passo de comunicação $H$ da co-simulação do NexaBot não tem custo algum, já que o FMU aceita qualquer valor de $H$. Avalie essa afirmação.

a. Correta, pois FMUs de co-simulação não impõem nenhum limite inferior de $H$.
*b. Incorreta: embora $H$ menor reduza o erro de acoplamento, ele aumenta a frequência de troca de dados entre os simuladores, elevando a sobrecarga de comunicação — a mesma tensão entre precisão e custo computacional discutida para o período de amostragem na Aula 7.
c. Correta, pois o padrão FMI garante desempenho constante independentemente de $H$.
d. Incorreta, pois $H$ menor sempre piora a precisão da co-simulação.
e. Correta, desde que o mestre de co-simulação utilize acoplamento *Gauss-Seidel*.

**40.** Ao final da Unidade 2, uma equipe conclui que, como todo cenário simulado nas Aulas 5 a 8 mostrou comportamento satisfatório, o requisito de segurança REQ-SAFE-001 do supervisor do NexaBot está provado válido em qualquer situação. Avalie essa conclusão.

*a. Incorreta: cada simulação, mesmo em malha fechada, discretizada e verificada por co-simulação, cobre apenas os cenários explicitamente escolhidos; a Unidade 3 verifica exaustivamente todos os cenários alcançáveis do supervisor de segurança, prova necessária para afirmar que um requisito como REQ-SAFE-001 nunca é violado.
b. Correta, pois simulação e verificação formal têm exatamente a mesma cobertura de cenários.
c. Correta, desde que todas as simulações tenham sido executadas com o mesmo $T_s$.
d. Incorreta, pois nenhuma simulação desta unidade envolveu malha fechada.
e. Correta, pois o contrato numérico do `DiscretePID` já constitui, por si só, uma prova formal de segurança.

## Gabarito e feedbacks

**Questão 1** (correta: c)
- a. Incorreta: a asserção II é falsa, não verdadeira — o proporcional puro não zera $S(0)$ para qualquer ganho.
- b. Incorreta: a asserção II é falsa pelo mesmo motivo; ela não é verdadeira em nenhum sentido.
- c. Correta: a I é verdadeira — um polo na origem em $C(s)$ eleva $L(s)$ a tipo 1 e zera o erro de regime independentemente dos ganhos, desde que a malha seja estável; a II é falsa, pois apenas aumentar $K_p$ reduz mas nunca anula $S(0)$, já que o proporcional puro não acrescenta polo na origem.
- d. Incorreta: a asserção I é verdadeira, não falsa.
- e. Incorreta: a asserção I é verdadeira, não falsa.

**Questão 2** (correta: e)
- a. Incorreta: as duas asserções são falsas, não verdadeiras.
- b. Incorreta: as duas asserções são falsas, não verdadeiras.
- c. Incorreta: a asserção I é falsa — um deslocamento fixo é calibrado para uma carga específica e falha ao mudar a carga, como mostrou a situação-problema da Aula 5.
- d. Incorreta: a asserção II também é falsa — em malha aberta não existe realimentação que module $S(s)$; o distúrbio afeta a saída diretamente, sem qualquer correção estrutural.
- e. Correta: a I é falsa, pois o deslocamento fixo não se adapta a uma carga diferente da usada na calibração; a II é falsa, pois a noção de sensibilidade $S(s)$ pressupõe realimentação, inexistente em malha aberta, e não é nula nesse caso — o distúrbio passa integralmente para a saída.

**Questão 3** (correta: a)
- a. Correta: ambas as asserções são verdadeiras, e a II explica corretamente a I — a identidade $S+T=1$ impõe que reduzir $S$ em uma faixa de frequência força $T$ a se aproximar de $1$ na mesma faixa, o que é exatamente o compromisso descrito na I.
- b. Incorreta: a II realmente justifica a I nesta questão, pois deriva diretamente da identidade algébrica entre as duas funções.
- c. Incorreta: a asserção II também é verdadeira, não falsa.
- d. Incorreta: a asserção I também é verdadeira, não falsa.
- e. Incorreta: as duas asserções são verdadeiras, não falsas.

**Questão 4** (correta: d)
- a. Incorreta: a asserção I é falsa, não verdadeira.
- b. Incorreta: a asserção I é falsa, não verdadeira.
- c. Incorreta: a asserção I é falsa, e a II é verdadeira, não falsa.
- d. Correta: a I é falsa — o controlador por alocação de polos exige medir corrente e velocidade simultaneamente, ao contrário do que a afirmação sugere; a II é verdadeira e descreve corretamente a vantagem de instrumentação do PID de saída única.
- e. Incorreta: a asserção II é verdadeira, não falsa.

**Questão 5** (correta: b)
- a. Incorreta: a II é um fato verdadeiro sobre a origem do ganho estático, mas não explica por que a velocidade em malha aberta cai para $0{,}929\,\mathrm{m/s}$ sob aquele distúrbio específico.
- b. Correta: ambas as asserções são verdadeiras, mas a II não justifica a I; o resultado numérico da I decorre das equações de equilíbrio elétrico e mecânico sob o distúrbio de $0{,}05\,\mathrm{N\,m}$, não do método usado para obter o ganho estático em outra aula.
- c. Incorreta: a asserção II também é verdadeira, não falsa.
- d. Incorreta: a asserção I também é verdadeira, não falsa.
- e. Incorreta: as duas asserções são verdadeiras, não falsas.

**Questão 6** (correta: a)
- a. Correta: ambas as asserções são verdadeiras, e a II explica corretamente por que o PID do NexaBot usa derivativo filtrado — evitar a amplificação do ruído de encoder que a derivada pura produziria.
- b. Incorreta: a II realmente justifica a I nesta questão.
- c. Incorreta: a asserção II também é verdadeira, não falsa.
- d. Incorreta: a asserção I também é verdadeira, não falsa.
- e. Incorreta: as duas asserções são verdadeiras, não falsas.

**Questão 7** (correta: c)
- a. Incorreta: a asserção II é falsa, não verdadeira.
- b. Incorreta: a asserção II é falsa, não verdadeira.
- c. Correta: a I é verdadeira — a planta contínua do NexaBot jamais oscilaria sob proporcional puro em tempo contínuo; a II é falsa, pois o método de Ziegler-Nichols não está restrito a plantas de primeira ordem, e a verdadeira razão da oscilação observada é o atraso de fase introduzido pela discretização em $T_s=5\,\mathrm{ms}$.
- d. Incorreta: a asserção I é verdadeira, não falsa.
- e. Incorreta: a asserção I é verdadeira, não falsa.

**Questão 8** (correta: e)
- a. Incorreta: as duas asserções são falsas, não verdadeiras.
- b. Incorreta: as duas asserções são falsas, não verdadeiras.
- c. Incorreta: a asserção I é falsa — saturação é a limitação física da tensão aplicável, enquanto *windup* é o crescimento descontrolado específico do termo integral durante essa saturação; a intensidade do *windup* depende dos ganhos e da duração da saturação, não é automática.
- d. Incorreta: a asserção II também é falsa — o anti-*windup* por *back-calculation* não impede a saturação, que continua ocorrendo; ele apenas corrige, a posteriori, o valor acumulado no integrador.
- e. Correta: a I é falsa, pois saturação e *windup* são fenômenos relacionados, mas distintos; a II é falsa, pois o anti-*windup* age sobre o integrador depois da saturação, não sobre a própria saturação.

**Questão 9** (correta: b)
- a. Incorreta: a II descreve corretamente como $K_u$ foi obtido, mas isso não explica por que as quatro sintonias têm sobressinal semelhante sob saturação.
- b. Correta: ambas as asserções são verdadeiras, mas a II não justifica a I; o motivo do sobressinal semelhante é que a fase inicial saturada é dominada pela dinâmica da planta saturada em $24\,\mathrm{V}$, e não pelos ganhos específicos de cada sintonia.
- c. Incorreta: a asserção II também é verdadeira, não falsa.
- d. Incorreta: a asserção I também é verdadeira, não falsa.
- e. Incorreta: as duas asserções são verdadeiras, não falsas.

**Questão 10** (correta: d)
- a. Incorreta: a asserção I é falsa, não verdadeira.
- b. Incorreta: a asserção I é falsa, não verdadeira.
- c. Incorreta: a asserção I é falsa, e a II é verdadeira, não falsa.
- d. Correta: a I é falsa — não existe garantia de que um $K_{aw}$ maior seja sempre melhor; a atividade prática da Aula 6 mostra que a escolha do ganho de anti-*windup* também é um compromisso de projeto. A II é verdadeira e descreve corretamente o mecanismo de *back-calculation*.
- e. Incorreta: a asserção II é verdadeira, não falsa.

**Questão 11** (correta: e)
- a. Incorreta: as duas asserções são falsas, não verdadeiras.
- b. Incorreta: as duas asserções são falsas, não verdadeiras.
- c. Incorreta: a asserção I é falsa — a varredura da Aula 7 mostra bom desempenho só até cerca de $8{,}26\,\mathrm{ms}$ e instabilidade observável na simulação saturada perto de $44{,}34\,\mathrm{ms}$; aumentar $T_s$ indiscriminadamente piora, não melhora, a margem.
- d. Incorreta: a asserção II também é falsa — Tustin e Euler para frente são métodos de discretização distintos, com mapas $s\to z$ diferentes.
- e. Correta: a I é falsa, pois a relação entre $T_s$ e margem de estabilidade não é monotônica; a II é falsa, pois Tustin e Euler para frente produzem aproximações diferentes da mesma equação diferencial.

**Questão 12** (correta: b)
- a. Incorreta: a II justifica apenas a escolha do ZOH para a planta, não explica por que o controlador usa Euler para trás no integrador.
- b. Correta: ambas as asserções são verdadeiras — o contrato do `DiscretePID` de fato usa Euler para trás, e a planta é discretizada por ZOH para a análise de malha fechada —, mas a II não justifica integralmente a I, pois explica apenas a metade referente ao ZOH da planta, e não a escolha de Euler para trás no controlador, que decorre de conveniência de implementação embarcada, não do comportamento do PWM.
- c. Incorreta: a asserção II também é verdadeira, não falsa.
- d. Incorreta: a asserção I também é verdadeira, não falsa.
- e. Incorreta: as duas asserções são verdadeiras, não falsas.

**Questão 13** (correta: d)
- a. Incorreta: a asserção I é falsa, não verdadeira.
- b. Incorreta: a asserção I é falsa, não verdadeira.
- c. Incorreta: a asserção I é falsa, e a II é verdadeira, não falsa.
- d. Correta: a I é falsa — a própria unidade afirma que a tabela sem atraso computacional "já é um limite otimista", não o pior caso real; a II é verdadeira e descreve corretamente o efeito do atraso de um ciclo como atraso de transporte que subtrai fase.
- e. Incorreta: a asserção II é verdadeira, não falsa.

**Questão 14** (correta: a)
- a. Correta: ambas as asserções são verdadeiras, e a II explica corretamente o custo colateral citado na I — menos tempo entre amostras significa menos pulsos de encoder por amostra e, portanto, uma estimativa de velocidade mais ruidosa.
- b. Incorreta: a II realmente justifica a I nesta questão.
- c. Incorreta: a asserção II também é verdadeira, não falsa.
- d. Incorreta: a asserção I também é verdadeira, não falsa.
- e. Incorreta: as duas asserções são verdadeiras, não falsas.

**Questão 15** (correta: c)
- a. Incorreta: a asserção II é falsa, não verdadeira.
- b. Incorreta: a asserção II é falsa, não verdadeira.
- c. Correta: a I é verdadeira quando explicita a aproximação mecânica desacoplada: $148/5=29{,}6$ amostras, dentro da faixa inicial de $10$ a $30$. A II é falsa, pois o modo dominante é o lento; pelo polo exato, $138{,}6/5=27{,}7$ e a conclusão permanece a mesma.
- d. Incorreta: a asserção I é verdadeira, não falsa.
- e. Incorreta: a asserção I é verdadeira, não falsa.

**Questão 16** (correta: d)
- a. Incorreta: a asserção I é falsa, não verdadeira.
- b. Incorreta: a asserção I é falsa, não verdadeira.
- c. Incorreta: a asserção I é falsa, e a II é verdadeira, não falsa.
- d. Correta: a I é falsa — o objetivo central da FMI é a independência de ferramenta na troca de modelos simuláveis, não impor um passo de comunicação fixo; a II é verdadeira e descreve corretamente a estrutura de um FMU de co-simulação.
- e. Incorreta: a asserção II é verdadeira, não falsa.

**Questão 17** (correta: a)
- a. Correta: ambas as asserções são verdadeiras, e a II explica corretamente o mecanismo descrito na I — o acoplamento *Jacobi* mantém as entradas constantes dentro de cada intervalo $H$ porque os modelos avançam em paralelo usando apenas os valores trocados no início do intervalo.
- b. Incorreta: a II realmente justifica a I nesta questão.
- c. Incorreta: a asserção II também é verdadeira, não falsa.
- d. Incorreta: a asserção I também é verdadeira, não falsa.
- e. Incorreta: as duas asserções são verdadeiras, não falsas.

**Questão 18** (correta: b)
- a. Incorreta: a II descreve corretamente o propósito de `verify_fmu.py`, mas isso não explica por que o erro de acoplamento cresce sem perder convergência até $H=10\,\mathrm{ms}$.
- b. Correta: ambas as asserções são verdadeiras, mas a II não justifica a I; o crescimento gradual do erro até $H=10\,\mathrm{ms}$ decorre do efeito de retenção de ordem zero do acoplamento sobre a malha fechada, não da verificação numérica isolada do FMU descrita na II.
- c. Incorreta: a asserção II também é verdadeira, não falsa.
- d. Incorreta: a asserção I também é verdadeira, não falsa.
- e. Incorreta: as duas asserções são verdadeiras, não falsas.

**Questão 19** (correta: c)
- a. Incorreta: a asserção II é falsa, não verdadeira.
- b. Incorreta: a asserção II é falsa, não verdadeira.
- c. Correta: a I é verdadeira — a tabela mede crescimento monotônico do erro RMS de acoplamento. A II é falsa: o FMU mantém seu RK4 interno; o erro cresce porque entradas e saídas só são trocadas nos pontos espaçados por $H$.
- d. Incorreta: a asserção I é verdadeira, não falsa.
- e. Incorreta: a asserção I é verdadeira, não falsa.

**Questão 20** (correta: e)
- a. Incorreta: as duas asserções são falsas, não verdadeiras.
- b. Incorreta: as duas asserções são falsas, não verdadeiras.
- c. Incorreta: a asserção I é falsa — a co-simulação existe precisamente para evitar um executável monolítico, permitindo que cada ferramenta mantenha seu próprio integrador.
- d. Incorreta: a asserção II também é falsa — a FMI padroniza a interface de troca de dados entre modelos, não o algoritmo de integração interno de cada um.
- e. Correta: a I é falsa, pois a co-simulação separa integradores em vez de uni-los; a II é falsa, pois a FMI não impõe um algoritmo de integração comum às ferramentas.

**Questão 21** (correta: b)
- a. Incorreta: $0{,}929\,\mathrm{m/s}$ e $7{,}07\%$ correspondem ao distúrbio de $0{,}05\,\mathrm{N\,m}$ do exemplo original, não ao de $0{,}08\,\mathrm{N\,m}$ pedido.
- b. Correta: recalculando com $T_l=0{,}08$, o numerador da fórmula de $\omega$ fica $18{,}85-2{,}1333\approx16{,}717$, e dividindo pelo mesmo denominador $0{,}0471333$ resulta em $\omega\approx354{,}7\,\mathrm{rad/s}$, ou seja, $v\approx0{,}887\,\mathrm{m/s}$, uma queda de aproximadamente $11{,}3\%$.
- c. Incorreta: esse valor não corresponde ao cálculo com as equações de equilíbrio para $T_l=0{,}08\,\mathrm{N\,m}$.
- d. Incorreta: a malha aberta não compensa variações de carga; é exatamente essa ausência de compensação que motiva o fechamento da malha na Aula 5.
- e. Incorreta: essa queda é maior do que a que resulta do cálculo com os valores fornecidos.

**Questão 22** (correta: d)
- a. Incorreta: $S(0)$ com proporcional puro é finito e não nulo para qualquer $K_p$ finito; apenas tende a diminuir com $K_p$ maior, sem nunca se anular exatamente.
- b. Incorreta: o tipo do sistema é definido pelo número de integradores puros em $L(s)=C(s)G(s)$, que inclui o controlador, não apenas a planta.
- c. Incorreta: um compensador de avanço de fase melhora margem de fase, mas não introduz um polo na origem nem elimina, por si só, o erro de regime a distúrbio constante.
- d. Correta: sem polo na origem em $C(s)$, $L(s)$ permanece tipo 0 e $S(0)$ nunca chega a zero, apenas se reduz com $K_p$ maior; é a ação integral que muda estruturalmente essa propriedade.
- e. Incorreta: a Aula 5 prova exatamente o contrário — uma malha fechada com ação integral elimina o erro de regime a um distúrbio constante.

**Questão 23** (correta: c)
- a. Incorreta: $24\,\mathrm{V}$ é a tensão máxima do driver, não a margem disponível após descontar a tensão de regime.
- b. Incorreta: a tensão de regime já está comprometida em sustentar a velocidade desejada; não pode ser reaproveitada livremente no transitório.
- c. Correta: $24-18{,}85=5{,}15\,\mathrm{V}$; essa margem estreita é o que torna saturação e *windup* riscos reais de projeto, como a Aula 6 desenvolve.
- d. Incorreta: o ganho estático é uma grandeza em $\mathrm{rad/(s\cdot V)}$, não uma tensão, e não corresponde à margem pedida.
- e. Incorreta: ainda resta margem de tensão, exatamente $5{,}15\,\mathrm{V}$, embora estreita.

**Questão 24** (correta: e)
- a. Incorreta: $T\approx1$ não é obtido sem custo; pela identidade $S+T=1$, implica $S\approx0$ na mesma faixa, incluindo faixas onde isso é indesejável.
- b. Incorreta: a identidade $S+T=1$ impede justamente que ambas sejam simultaneamente próximas de $1$ na mesma frequência.
- c. Incorreta: $S$ e $T$ têm relação matemática definida e exata: $S(s)+T(s)=1$ para toda frequência.
- d. Incorreta: mesmo com resolução infinita de encoder, a identidade $S+T=1$ continuaria impedindo $T\approx1$ e $S\approx0$ simultaneamente sem consequência.
- e. Correta: perseguir $T\approx1$ em toda frequência amplificaria o ruído de quantização do encoder nas frequências altas, pois $S\approx0$ nessa faixa não atenuaria esse ruído antes de chegar à tensão de comando.

**Questão 25** (correta: a)
- a. Correta: o PID é um caso particular de $C(s)$ com um polo na origem devido ao termo integral, suficiente para tornar $L(s)$ tipo 1 sem exigir realimentação de nenhuma variável além da saída medida.
- b. Incorreta: o polo na origem pode vir de qualquer controlador com ação integral, não exclusivamente da realimentação de estados.
- c. Incorreta: o PID elimina, sim, o erro de regime a distúrbios constantes, exatamente por conter ação integral.
- d. Incorreta: o PID é um controlador de saída única e, mesmo assim, altera o tipo do sistema ao introduzir um polo na origem.
- e. Incorreta: um observador de estados não é necessário para essa propriedade; ela decorre apenas da presença do polo na origem em $C(s)$.

**Questão 26** (correta: c)
- a. Incorreta: $2{,}215$ corresponde ao $K_p$ da sintonia PID clássica, calculado por $0{,}60K_u$, não por $0{,}20K_u$.
- b. Incorreta: $1{,}661$ corresponde ao $K_p$ da sintonia PI, calculado por $0{,}45K_u$.
- c. Correta: $0{,}20\times3{,}691\approx0{,}738$, valor que coincide com o $K_p$ da sintonia sem sobressinal da tabela da Aula 6.
- d. Incorreta: $1{,}846$ corresponde ao $K_p$ da sintonia proporcional pura, calculado por $0{,}50K_u$.
- e. Incorreta: $0{,}200$ é o coeficiente da fórmula, não o valor final de $K_p$ após multiplicar por $K_u$.

**Questão 27** (correta: b)
- a. Incorreta: a própria Aula 6 mostra que a sintonia clássica mantém oscilação residual não amortecida na malha discreta real do NexaBot.
- b. Correta: o método fornece um ponto de partida a partir de $K_u$ e $T_u$, mas precisa ser verificado na malha discreta real antes de ser adotado, como evidenciado pela oscilação residual observada mesmo sem saturação.
- c. Incorreta: a oscilação residual observada ocorreu mesmo em teste sem saturação, o que contradiz essa alternativa.
- d. Incorreta: Ziegler-Nichols pelo ganho crítico é aplicado a plantas estáveis em malha aberta, elevando o ganho até induzir oscilação sustentada.
- e. Incorreta: o filtro derivativo não é a causa da oscilação residual atribuída à sintonia clássica; a oscilação persiste mesmo considerando o filtro com $\tau_f=0{,}01\,\mathrm{s}$.

**Questão 28** (correta: a)
- a. Correta: $(5\,888{,}0-2\,624{,}96)/5\,888{,}0\approx0{,}554$, ou seja, aproximadamente $55{,}4\%$ de redução.
- b. Incorreta: esse valor corresponderia à fração restante do integrador em relação ao original, não à redução percentual.
- c. Incorreta: esse percentual não corresponde ao cálculo com os valores fornecidos.
- d. Incorreta: esse percentual subestima a redução real observada na demonstração.
- e. Incorreta: esse percentual superestima a redução real observada na demonstração.

**Questão 29** (correta: e)
- a. Incorreta: o sobressinal é definido pelo pico máximo da resposta, insensível a uma oscilação residual de menor amplitude que ocorre após a fase inicial.
- b. Incorreta: o tempo de subida mede apenas o intervalo entre $10\%$ e $90\%$ da referência, período dominado pela saturação, e não captura o comportamento posterior.
- c. Incorreta: o ISE, ao integrar o erro ao quadrado ao longo do tempo, captura exatamente esse tipo de diferença.
- d. Incorreta: a unidade apresenta métricas numéricas objetivas, entre elas o ISE, como forma preferível de comparação frente à inspeção visual isolada.
- e. Correta: por integrar o erro ao quadrado ao longo de todo o intervalo, o ISE penaliza a oscilação residual prolongada da sintonia X, mesmo quando sobressinal e tempo de subida são semelhantes entre as duas sintonias.

**Questão 30** (correta: d)
- a. Incorreta: um $N$ maior aumenta a sensibilidade ao ruído de encoder, o que não representa melhoria sem custo.
- b. Incorreta: o parâmetro $N$ define exatamente o polo do filtro derivativo, afetando diretamente sua resposta em frequência.
- c. Incorreta: $N=20$ é o valor adotado para o NexaBot neste material, mas o texto da aula explicita que é um compromisso, não o único valor numericamente estável.
- d. Correta: a aula descreve explicitamente esse compromisso — $N$ maior aproxima do derivativo ideal, mas amplifica mais ruído de alta frequência; a escolha depende da planta e do nível de ruído do sensor.
- e. Incorreta: reduzir $N$ a zero eliminaria o efeito prático da ação derivativa, contrariando seu papel de antecipação de tendência.

**Questão 31** (correta: a)
- a. Correta: $148/7\approx21{,}1$ amostras pela aproximação mecânica desacoplada, valor dentro da faixa inicial de $10$ a $30$ amostras. Pelo polo dominante exato seriam $138{,}6/7\approx19{,}8$, o que preserva a mesma conclusão.
- b. Incorreta: $14{,}8$ corresponde ao resultado para $T_s=10\,\mathrm{ms}$, não para $T_s=7\,\mathrm{ms}$.
- c. Incorreta: $29{,}6$ corresponde ao resultado para $T_s=5\,\mathrm{ms}$, não para $T_s=7\,\mathrm{ms}$.
- d. Incorreta: esse valor está abaixo do resultado correto do cálculo com $T_s=7\,\mathrm{ms}$.
- e. Incorreta: esse valor está muito abaixo do resultado correto e também abaixo da faixa recomendada, ao contrário do que o cálculo mostra.

**Questão 32** (correta: c)
- a. Incorreta: $23{,}4\,\mathrm{mV}$ corresponde à resolução com $2^{10}$ níveis, não $2^{12}$.
- b. Incorreta: esse valor não corresponde à divisão de $24\,\mathrm{V}$ por $4\,096$ níveis.
- c. Correta: $24/4\,096\approx5{,}86\times10^{-3}\,\mathrm{V}=5{,}86\,\mathrm{mV}$.
- d. Incorreta: esse valor corresponderia a $2^{13}$ níveis, não a $2^{12}$.
- e. Incorreta: esse valor está muito acima da resolução correta para $2^{12}$ níveis.

**Questão 33** (correta: e)
- a. Incorreta: o pico aumenta, não diminui.
- b. Incorreta: sobressinal não é sinônimo de instabilidade; a saída retorna a $50\,\mathrm{rad/s}$ nesse caso.
- c. Incorreta: a diferença de $12{,}78\,\mathrm{rad/s}$ é muito maior que o arredondamento de impressão.
- d. Incorreta: $64{,}37/51{,}59\approx1{,}25$, não $2$, e ambas as respostas já têm erro de regime praticamente nulo.
- e. Correta: o pico cresce cerca de $24{,}8\%$, mas a resposta ainda converge; o atraso degrada o transitório sem desestabilizar a malha em $T_s=5\,\mathrm{ms}$.

**Questão 34** (correta: b)
- a. Incorreta: a instabilidade numérica de Tustin não é a razão dada na aula para a escolha do ZOH; a Aula 7 usa Tustin normalmente em outras comparações.
- b. Correta: o ZOH reproduz fielmente o comportamento do PWM entre amostras, e o controlador, por ser código e não um circuito físico com retenção natural, é livre para adotar a regra de integração mais conveniente à implementação embarcada — daí Euler para trás no `DiscretePID`.
- c. Incorreta: Euler para trás é justamente o método usado no integrador do `DiscretePID`, um controlador PID.
- d. Incorreta: ZOH e Euler para trás são aproximações distintas da relação $s\to z$, com mapas diferentes.
- e. Incorreta: a planta poderia, em princípio, ser discretizada por outros métodos; o ZOH é escolhido por reproduzir o comportamento real do atuador entre amostras, não por ser o único possível.

**Questão 35** (correta: d)
- a. Incorreta: a própria Pausa para Reflexão da Aula 7 questiona justamente essa suposição, apontando que a margem calculada em regime não é necessariamente o pior caso.
- b. Incorreta: o *jitter* afeta o instante efetivo de amostragem e atuação, alterando a fase acumulada na malha, de forma análoga ao atraso computacional discutido na aula.
- c. Incorreta: a margem de amostras por constante de tempo dominante é definida, corretamente, em relação a $\tau_m$, a mais lenta; isso não é o problema levantado pela reflexão.
- d. Correta: a varredura nominal não inclui atraso computacional adicional nem variações ciclo a ciclo; um pico isolado de *jitter* ou um atraso sistemático de um ciclo consome parte dessa margem otimista, podendo aproximar a malha real do limiar de instabilidade mais do que a tabela nominal sugere.
- e. Incorreta: o *jitter* afeta a fase da malha independentemente de haver ação derivativa.

**Questão 36** (correta: e)
- a. Incorreta: os erros têm experimentos de referência diferentes e não devem ser numericamente idênticos.
- b. Incorreta: a verificação isolada fica próxima do ruído de ponto flutuante, enquanto o erro de acoplamento alcança pontos percentuais.
- c. Incorreta: o erro de acoplamento cresce claramente com $H$.
- d. Incorreta: `verify_fmu.py` é justamente o controle experimental que separa defeito de implementação de efeito do acoplamento.
- e. Correta: a verificação isolada compara implementações sob a mesma entrada; a co-simulação mede a defasagem introduzida pelas trocas espaçadas, que cresce com $H$ mesmo com o FMU correto.

**Questão 37** (correta: d)
- a. Incorreta: $1{,}078\%$ é maior, não menor, que $1\%$.
- b. Incorreta: o critério aceita erro não nulo até o limite definido.
- c. Incorreta: dois pontos delimitam um intervalo, mas não determinam o cruzamento exato sem novas execuções.
- d. Correta: $10\,\mathrm{ms}$ é aprovado e $20\,\mathrm{ms}$ é reprovado; logo o cruzamento está no intervalo aberto entre eles e a bisseção deve refiná-lo.
- e. Incorreta: $1\%$ é um critério de engenharia adotado na atividade, não uma regra do padrão FMI.

**Questão 38** (correta: c)
- a. Incorreta: a existência de `verify_fmu.py` mostra que a unidade distingue explicitamente erro de implementação de erro de acoplamento; nem todo erro é atribuível ao FMU.
- b. Incorreta: o valor do erro não determina, por si só, sua origem; é necessário isolar as duas fontes, como faz `verify_fmu.py`.
- c. Correta: `verify_fmu.py` isola o erro de implementação da planta em C e encontra erro próximo do ruído de ponto flutuante; o crescimento observado com $H$ na malha fechada é consistente com erro de acoplamento, não com defeito no FMU.
- d. Incorreta: a unidade descreve exatamente esse procedimento de verificação isolada do FMU antes da co-simulação completa.
- e. Incorreta: o `modelDescription.xml` cumpre a função de declarar entradas, saídas e parâmetros de forma padronizada, independentemente da linguagem de implementação do modelo.

**Questão 39** (correta: b)
- a. Incorreta: embora o FMU aceite tecnicamente qualquer $H$ positivo, isso não significa ausência de custo prático de comunicação.
- b. Correta: reduzir $H$ diminui o erro de acoplamento, mas aumenta a frequência de troca de dados entre os simuladores, elevando a sobrecarga de comunicação — o mesmo tipo de tensão entre precisão e custo computacional discutido para o período de amostragem do controlador na Aula 7.
- c. Incorreta: o padrão FMI define a interface de troca de dados, mas não garante desempenho constante independentemente da frequência de chamadas.
- d. Incorreta: a tabela de erro da Aula 8 mostra o oposto — $H$ menor reduz o erro de acoplamento, não o piora.
- e. Incorreta: a mudança de disciplina de acoplamento para *Gauss-Seidel* não elimina o custo de comunicação associado a um $H$ menor; ela afeta a ordem de avanço dos modelos, não a frequência de troca de dados.

**Questão 40** (correta: a)
- a. Correta: mesmo simulações em malha fechada, discretizadas e verificadas por co-simulação cobrem apenas cenários explicitamente escolhidos; a Unidade 3 verifica exaustivamente todos os cenários alcançáveis, condição necessária para provar que um requisito de segurança nunca é violado.
- b. Incorreta: simulação cobre cenários específicos escolhidos pelo projetista; verificação formal exaustiva cobre todos os cenários alcançáveis do modelo, uma cobertura estritamente maior.
- c. Incorreta: usar o mesmo $T_s$ em todas as simulações não amplia a cobertura de cenários testados, apenas mantém constante um parâmetro de discretização.
- d. Incorreta: as Aulas 5 a 8 tratam justamente de malha fechada, sintonia, discretização e co-simulação da malha fechada do NexaBot.
- e. Incorreta: o contrato numérico do `DiscretePID` define uma aritmética precisa e reprodutível, mas não constitui, por si só, uma prova formal de que um requisito de segurança nunca é violado em todos os cenários alcançáveis.
