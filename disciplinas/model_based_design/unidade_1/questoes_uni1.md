# Questionário — Unidade 1

Quantidade obrigatória: 40 questões — 20 de asserção-razão (1 a 20) e 20 de interpretação (21 a 40).
Cinco alternativas por questão (a-e); alternativa correta marcada com `*` imediatamente antes da letra.
Distribuição da letra correta: 8 questões para cada uma das letras a, b, c, d, e, no total das 40 questões.

## Questões

### Asserção-razão

**1.** I. Um sistema ciberfísico integra, em um único projeto, computação discreta e dinâmica física contínua que evolui segundo equações diferenciais.

PORQUE

II. Esse acoplamento produz um sistema híbrido, no qual trechos de evolução contínua da planta são intercalados por eventos discretos de amostragem e de atualização do comando.

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**2.** I. Um erro em um sistema de informação típico tende a ficar confinado ao domínio digital, gerando um dado incorreto ou uma transação perdida.

PORQUE

II. O V-Model organiza o desenvolvimento em um ramo descendente de decomposição de requisitos e um ramo ascendente de verificação correspondente.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**3.** I. Um sistema ciberfísico não sofre impacto de erros de software, pois a dinâmica física sempre corrige eventuais falhas de comando.

PORQUE

II. O design baseado em modelos concentra toda a verificação apenas na fase de implementação, após o código estar embarcado no equipamento.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

**4.** I. Um comando de tensão fixo, calculado para a condição sem carga, não corrige automaticamente a queda de velocidade do NexaBot quando uma carga é aplicada ao eixo.

PORQUE

II. O controle em malha aberta realimenta continuamente a velocidade medida para recalcular o comando de tensão a cada instante.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**5.** I. O V-Model resolve o problema de adiar a verificação até o produto final estar pronto, pois exige que cada nível do ramo descendente seja verificado contra o nível correspondente do ramo ascendente.

PORQUE

II. O design baseado em modelos representa cada nível do ramo descendente como um modelo executável, permitindo verificação contra dados ou requisitos antes da existência de código embarcado.

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**6.** I. O estado do motor do NexaBot é definido apenas pela corrente de armadura, pois a velocidade angular pode ser calculada a qualquer instante a partir da corrente presente.

PORQUE

II. Para o NexaBot, o vetor de estado mínimo necessário para prever a evolução futura, dado o comando futuro, é $x=[i,\omega]^T$, combinando corrente e velocidade angular.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**7.** I. A matriz $A$ do modelo em espaço de estados do NexaBot tem entradas de ordem de grandeza muito maior na primeira linha do que na segunda.

PORQUE

II. A identificação de parâmetros por mínimos quadrados não lineares ajusta a trajetória inteira simulada ao dado medido, em vez de estimar derivadas ponto a ponto.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**8.** I. Reservar um segundo ensaio, nunca utilizado no ajuste dos parâmetros, é a prática correta para validar se o modelo identificado generaliza além do ruído específico do primeiro ensaio.

PORQUE

II. A métrica `fit%` é calculada apenas sobre o comando de tensão aplicado no ensaio, e não sobre a resposta medida do sistema.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**9.** I. Os cinco parâmetros físicos do motor do NexaBot podem ser identificados com precisão a partir de um único degrau de tensão amostrado no período de controle de $5\,\mathrm{ms}$, sem qualquer perda de informação sobre $R$ e $L$.

PORQUE

II. A quantização do encoder de velocidade elimina completamente o ruído de medição presente no sinal de corrente.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

**10.** I. As matrizes $B$, $C$ e $D$ do modelo em espaço de estados do NexaBot dependem da resistência de armadura $R$ e da indutância $L$, exatamente como a matriz $A$.

PORQUE

II. A matriz $B=[1/L\ \ 0]^T$ depende apenas da indutância, a matriz $C=[0\ \ 1]$ depende apenas de qual variável de estado é medida como saída, e $D=0$.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**11.** I. A função de transferência $G(s)$ do NexaBot, obtida por Laplace a partir das equações do motor, não possui zeros finitos, de modo que os dois polos determinam integralmente a forma da resposta.

PORQUE

II. Os dois polos do NexaBot, aproximadamente $-7{,}215\,\mathrm{rad/s}$ e $-335{,}96\,\mathrm{rad/s}$, encontram-se no semiplano direito do plano complexo, indicando instabilidade da planta em malha aberta.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**12.** I. Na escala de tempo em que a velocidade do NexaBot é observada após um degrau de tensão, a resposta se assemelha à de um sistema de primeira ordem, mesmo o modelo sendo de segunda ordem.

PORQUE

II. Tanto pelos valores modais exatos ($2{,}9765\,\mathrm{ms}$ e $138{,}598\,\mathrm{ms}$) quanto pelas aproximações desacopladas ($2{,}9167\,\mathrm{ms}$ e $148{,}148\,\mathrm{ms}$), o modo rápido já se extinguiu quando o modo lento ainda domina a resposta observada.

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**13.** I. O diagrama de Bode do NexaBot exibe um único ponto de quebra, pois os dois polos do sistema coincidem no mesmo valor de frequência.

PORQUE

II. A margem de fase mede quanto o ganho de malha pode crescer antes de o sistema se tornar instável.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

**14.** I. A separação de escalas de tempo entre os polos elétrico e mecânico do NexaBot é de quase duas ordens de grandeza.

PORQUE

II. O diagrama de Bode representa a magnitude e a fase da resposta em frequência $G(j\omega)$ do sistema.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**15.** I. A largura de banda de um sistema indica o valor máximo absoluto de tensão que pode ser aplicado ao driver do motor sem saturação.

PORQUE

II. A largura de banda indica a velocidade máxima de variação de referência que o sistema consegue acompanhar sem atenuação excessiva.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**16.** I. O NexaBot é controlável, o que garante, em princípio, a existência de uma tensão capaz de levar a corrente e a velocidade a qualquer par de valores desejado.

PORQUE

II. A matriz de controlabilidade $\mathcal{C}=[B\ \ AB]$ do NexaBot tem determinante não nulo, portanto posto completo igual a 2.

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**17.** I. Um projeto de alocação de polos matematicamente correto pode, ainda assim, ser fisicamente inviável para o NexaBot, caso exija um comando de tensão acima do limite do driver.

PORQUE

II. A controlabilidade do sistema garante que qualquer objetivo de desempenho seja alcançável dentro dos limites físicos reais do atuador.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**18.** I. O regulador linear quadrático (LQR) elimina totalmente a necessidade de respeitar o limite de tensão do driver, pois otimiza diretamente o consumo de energia do atuador.

PORQUE

II. As matrizes de peso $Q$ e $R$ do LQR não influenciam a posição dos polos de malha fechada resultantes, apenas o tempo de execução do algoritmo.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

**19.** I. A observabilidade do NexaBot permite que a corrente de armadura seja reconstruída a partir da medição única da velocidade angular.

PORQUE

II. O ganho de referência $\bar{N}$ na lei de controle $u=-Kx+\bar{N}r$ é calculado para garantir erro nulo em regime permanente.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**20.** I. Ganhos de realimentação $K$ maiores em módulo produzem, em geral, comandos de tensão iniciais menores para o mesmo degrau de referência.

PORQUE

II. Polos de malha fechada mais rápidos exigem, em geral, ganhos $K$ maiores em módulo, o que eleva o comando de tensão inicial exigido para a mesma referência.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Interpretação

**21.** O NexaBot opera em malha aberta com comando fixo de $18{,}85\,\mathrm{V}$, valor que sustenta $1{,}00\,\mathrm{m/s}$ sem carga. Um técnico aplica ao eixo um torque de carga de $0{,}10\,\mathrm{N\,m}$ (o dobro do exemplo apresentado na aula), mantendo o mesmo comando de tensão. Usando $R=1{,}2\,\Omega$, $K_t=0{,}045$, $Rb/K_t+K_e=0{,}047133$, qual é, aproximadamente, a nova velocidade linear em regime permanente?

a. $0{,}93\,\mathrm{m/s}$
b. $0{,}80\,\mathrm{m/s}$
*c. $0{,}86\,\mathrm{m/s}$
d. $0{,}70\,\mathrm{m/s}$
e. $1{,}00\,\mathrm{m/s}$

**22.** A equipe de qualidade do NexaBot descobre, três meses após a implantação em campo, que o modelo da planta usado no projeto do controlador subestimava o atrito viscoso $b$ em 40%. Se esse mesmo erro tivesse sido detectado durante a fase de simulação do modelo, antes da implementação em hardware, qual conceito da Unidade 1 explica por que o custo de correção seria menor?

a. A malha aberta corrige automaticamente esse tipo de erro de parâmetro.
b. A controlabilidade do sistema garante que erros de parâmetro nunca cheguem ao campo.
c. O ganho estático do sistema se torna independente do valor de $b$.
*d. O custo de corrigir um defeito cresce fortemente conforme a fase de descoberta avança, de modo que capturar o erro por simulação, antes da implementação, evita o custo de reprojetar hardware já em campo.
e. A separação entre as constantes de tempo elétrica e mecânica elimina a necessidade de verificar o valor de $b$.

**23.** O controlador do NexaBot amostra a velocidade a cada $T_s=5\,\mathrm{ms}$ e atualiza o comando de tensão apenas nesses instantes, mantendo-o constante entre duas amostras consecutivas. Esse comportamento caracteriza corretamente qual conceito?

*a. Um sistema híbrido, em que a dinâmica contínua da planta evolui entre eventos discretos de amostragem e atualização do comando (segurador de ordem zero).
b. Um sistema puramente contínuo, pois o comando de tensão nunca é atualizado.
c. Um sistema puramente discreto, pois a planta não evolui entre as amostras.
d. Uma falha de temporização do controlador, pois o comando deveria ser atualizado continuamente.
e. Uma malha aberta, pois a amostragem elimina qualquer realimentação.

**24.** Um defeito de software em um sistema de gestão de estoque gera um registro duplicado, corrigido horas depois sem maiores consequências. Um defeito de mesma gravidade lógica no firmware do NexaBot faz o robô colidir com uma prateleira antes de ser identificado. Qual conceito da Aula 1 explica essa diferença de consequência?

a. O NexaBot não é, tecnicamente, um sistema ciberfísico, pois usa apenas lógica discreta.
*b. Em um CPS, o acoplamento entre lógica discreta e dinâmica física faz um erro atravessar a fronteira entre código e mundo físico, gerando efeito irreversível sem possibilidade de desfazer a ação.
c. Sistemas de gestão de estoque são, por definição, mais confiáveis que qualquer sistema ciberfísico.
d. A diferença decorre exclusivamente da velocidade de processamento do firmware do robô.
e. Um erro de mesma gravidade lógica produz sempre a mesma consequência física, independentemente do sistema.

**25.** Ao mapear as 16 videoaulas da disciplina sobre o V-Model, conforme pedido na atividade prática da Aula 1, um estudante classifica todo o conteúdo de verificação formal (simulação, *model checking*, testes) como pertencente ao ramo descendente do V-Model. Essa classificação está:

a. Correta, pois o ramo descendente concentra toda a atividade de verificação.
b. Correta, pois modelo executável e verificação são sinônimos no MBD.
c. Incorreta, pois não existe ramo ascendente em um V-Model aplicado a sistemas ciberfísicos.
d. Correta, parcialmente, pois metade da verificação pertence a cada ramo.
*e. Incorreta, pois verificação (simulação, *model checking*, testes) pertence ao ramo ascendente, que confere cada nível contra o correspondente nível do ramo descendente de definição do modelo.

**26.** A tabela abaixo mostra parâmetros identificados por mínimos quadrados não lineares a partir de um ensaio de degrau do motor do NexaBot:

| Parâmetro | Valor verdadeiro | Valor identificado | Erro (%) |
| --- | --- | --- | --- |
| $R\,(\Omega)$ | $1{,}20$ | $1{,}21$ | $0{,}83\%$ |
| $L\,(\mathrm{mH})$ | $3{,}50$ | $3{,}55$ | $1{,}43\%$ |
| $J\,(\mathrm{kg\,m^2})$ | $2{,}5\times10^{-4}$ | $2{,}50\times10^{-4}$ | $0{,}02\%$ |
| $b\,(\mathrm{N\,m\,s/rad})$ | $8{,}0\times10^{-5}$ | $8{,}05\times10^{-5}$ | $0{,}63\%$ |

Considerando a separação de escalas de tempo discutida nas Aulas 2 e 3, qual conclusão é mais consistente com os dados?

a. O erro de $J$ e $b$ deveria ser maior que o de $R$ e $L$, pois a dinâmica mecânica é sempre mais difícil de identificar.
b. Os erros indicam que o ensaio foi amostrado no período de controle de $5\,\mathrm{ms}$, o que compromete a identificação de $R$ e $L$.
c. Todos os parâmetros foram identificados com a mesma precisão, o que indica ausência de qualquer efeito de escala de tempo.
*d. Os erros pequenos e semelhantes entre os quatro parâmetros indicam que o ensaio capturou adequadamente tanto a dinâmica elétrica rápida quanto a mecânica lenta, sem perda de informação por subamostragem.
e. O erro de $R$ e $L$ é aceitável apenas porque esses parâmetros não influenciam o ganho estático do sistema.

**27.** Um estudante deriva simbolicamente a matriz $A$ do NexaBot com SymPy e obtém $A_{11}=-R/L$ na posição correspondente à corrente. Substituindo $R=1{,}2\,\Omega$ e $L=3{,}5\,\mathrm{mH}$, qual valor deve aparecer nessa posição da matriz numérica?

a. $-0{,}343$
b. $-34{,}29$
*c. $-342{,}857$
d. $-3{,}429$
e. $-3428{,}57$

**28.** Um pesquisador ajusta os cinco parâmetros do motor do NexaBot usando o primeiro ensaio de degrau e obtém `fit% = 98%` nesse mesmo conjunto. Ao aplicar o modelo ajustado ao segundo ensaio, nunca usado no ajuste, o `fit%` cai para 40%. Qual é a interpretação mais adequada?

a. O modelo está correto, pois 98% no primeiro ensaio já comprova sua validade geral.
b. O segundo ensaio deve ser descartado, pois ensaios de validação nunca são confiáveis.
c. A queda indica que o motor sofreu uma falha física entre os dois ensaios.
d. O resultado é esperado e não indica problema algum, pois `fit%` deveria naturalmente cair em qualquer segundo ensaio.
*e. A grande queda de `fit%` do primeiro ensaio (ajuste) para o segundo (validação) sugere sobreajuste ao ruído específico do primeiro ensaio, e o modelo deve ser revisado antes de ser considerado validado.

**29.** Considerando a matriz $B=[1/L\ \ 0]^T$ do NexaBot e a matriz $C=[0\ \ 1]$, qual variável de estado é efetivamente utilizada como saída do modelo em espaço de estados, $y=Cx$?

*a. A velocidade angular $\omega$, pois $C$ seleciona a segunda componente do vetor de estado $x=[i,\omega]^T$.
b. A corrente de armadura $i$, pois $C$ seleciona a primeira componente do vetor de estado.
c. Ambas as variáveis de estado, $i$ e $\omega$, simultaneamente.
d. Nenhuma variável de estado, pois $D=0$ anula qualquer saída.
e. A tensão de comando $V$, pois $B$ determina diretamente a saída do sistema.

**30.** Um engenheiro decide estimar os parâmetros do motor calculando derivadas numéricas ponto a ponto da corrente e da velocidade medidas, em vez de ajustar a trajetória inteira simulada por mínimos quadrados não lineares. Qual é a consequência mais provável dessa escolha, segundo os conceitos da Aula 2?

a. Nenhuma consequência, pois os dois métodos produzem exatamente o mesmo resultado.
*b. O ruído de medição presente nos sinais tende a ser amplificado pela derivação numérica, prejudicando a qualidade da estimativa dos parâmetros.
c. O método se torna mais preciso, pois evita qualquer necessidade de simulação da planta.
d. O método elimina a necessidade de um segundo ensaio de validação.
e. O método passa a exigir menos dados do que o ajuste da trajetória inteira.

**31.** Um estudante calcula a razão entre os módulos dos dois polos do NexaBot, $335{,}96/7{,}215$. Qual é o valor aproximado dessa razão, e o que ela representa?

a. Aproximadamente $4{,}7$; representa a razão entre a tensão máxima e o ganho estático do sistema.
b. Aproximadamente $335{,}96$; representa o valor do polo elétrico em rad/s.
c. Aproximadamente $7{,}215$; representa o valor do polo mecânico em rad/s.
d. Aproximadamente $21{,}2$; representa o ganho estático do sistema em rad/(s·V).
*e. Aproximadamente $46{,}6$; representa a separação de escalas de tempo entre as dinâmicas elétrica e mecânica, quase duas ordens de grandeza.

**32.** O diagrama de Bode de magnitude do NexaBot exibe dois pontos de quebra, um em aproximadamente $7{,}215\,\mathrm{rad/s}$ e outro em aproximadamente $335{,}96\,\mathrm{rad/s}$. Entre esses dois pontos, qual é o comportamento aproximado do sistema?

*a. O sistema se comporta como se fosse de primeira ordem, pois o efeito do polo mais rápido já deixou de dominar a magnitude nessa faixa.
b. O sistema se comporta como se tivesse ganho infinito, pois está entre os dois polos.
c. O sistema está instável nessa faixa de frequência, pois ultrapassou o primeiro ponto de quebra.
d. A fase do sistema permanece constante em $0°$ em toda essa faixa.
e. A inclinação da magnitude é de $-40\,\mathrm{dB/década}$ em toda essa faixa.

**33.** Um estudante calcula os coeficientes do denominador de $G(s)$ do NexaBot e obtém $LJ=8{,}75\times10^{-7}$, $RJ+Lb\approx3{,}0028\times10^{-4}$ e $Rb+K_tK_e=2{,}121\times10^{-3}$. Aplicando a fórmula de Bhaskara a esse polinômio de segundo grau, quais são, aproximadamente, os dois polos resultantes?

a. $-21{,}2$ e $-400\,\mathrm{rad/s}$.
b. $-46{,}6$ e $-148\,\mathrm{rad/s}$.
c. $-2{,}92$ e $-335{,}96\,\mathrm{rad/s}$.
*d. $-7{,}215$ e $-335{,}96\,\mathrm{rad/s}$.
e. $-0{,}32$ e $-342{,}857\,\mathrm{rad/s}$.

**34.** A varredura proporcional contínua da Aula 3 mostra que, ao aumentar $K_p$ de $0{,}5$ para $50$, a margem de fase diminui e o sobressinal chega a aproximadamente $71{,}3\%$, mas a malha continua estável. Qual interpretação é correta?

a. Estabilidade garante automaticamente desempenho aceitável, portanto $K_p=50$ é adequado.
b. O sobressinal elevado prova que a planta em malha aberta é instável.
*c. A malha contínua de segunda ordem permanece estável para todo $K_p>0$, mas ganhos altos podem produzir desempenho inaceitável; o ganho crítico finito da Aula 6 surge apenas após a discretização.
d. A margem de fase aumenta com $K_p$, o que explica o aumento do sobressinal.
e. Um sobressinal de $71{,}3\%$ equivale a margem de fase exatamente nula.

**35.** Um projetista decide desprezar o polo elétrico do NexaBot ($-335{,}96\,\mathrm{rad/s}$) para simplificar o modelo a um sistema de primeira ordem, argumentando apenas que os polos estão muito separados. Considerando a Pausa para Reflexão da Aula 3, qual ressalva é a mais pertinente a essa decisão?

a. A redução é sempre ilegítima, pois todo modelo deve preservar exatamente todos os seus polos originais.
*b. A legitimidade da redução depende do uso pretendido do modelo: ela pode prejudicar a precisão em frequências próximas ao polo rápido e a análise da corrente, relevante para o limite de $12\,\mathrm{A}$ do requisito REQ-PLANT-002.
c. A redução é sempre legítima quando a razão entre os polos é maior que 10, sem qualquer outra consideração.
d. A redução elimina automaticamente a necessidade de considerar o período de amostragem do controlador.
e. A redução só é relevante para a análise de controlabilidade, não para a de resposta em frequência.

**36.** A matriz de controlabilidade do NexaBot é $\mathcal{C}=[B\ \ AB]$, com $B=[285{,}714\ \ 0]^T$. Calculando $AB$, um estudante obtém aproximadamente $[-97\,959{,}2\ \ 51\,428{,}6]^T$. O determinante resultante de $\mathcal{C}$ é diferente de zero. O que essa conclusão implica diretamente?

*a. O sistema é controlável, isto é, existe, em princípio, alguma tensão capaz de levar o par (corrente, velocidade) a qualquer condição desejada em tempo finito.
b. O sistema é observável, pois o determinante não nulo garante reconstrução do estado pela saída medida.
c. O sistema é instável, pois o determinante da matriz de controlabilidade é sempre negativo em sistemas estáveis.
d. O sistema não pode ser controlado por realimentação de estados, pois o determinante deveria ser nulo.
e. O resultado não tem relação com a viabilidade física do comando de tensão exigido.

**37.** A tabela abaixo relaciona pares $(Q,R)$ do LQR do NexaBot ao pico de tensão exigido e ao tempo de acomodação para um degrau de $400\,\mathrm{rad/s}$:

| $Q$ (elemento sobre $\omega$) | $R$ | Pico de tensão (V) | Tempo de acomodação (s) |
| --- | --- | --- | --- |
| 1 | 0,1 | 12 | 0,80 |
| 10 | 0,1 | 22 | 0,35 |
| 100 | 0,1 | 40 | 0,12 |

Qual par é o mais agressivo (menor tempo de acomodação) ainda compatível com o limite de $24\,\mathrm{V}$ do driver?

a. $Q=100$, $R=0{,}1$, pois apresenta o menor tempo de acomodação entre os três.
b. $Q=1$, $R=0{,}1$, pois é o único que respeita o limite com folga considerável.
c. Nenhum dos três pares respeita o limite de $24\,\mathrm{V}$.
d. Todos os três pares respeitam igualmente o limite de $24\,\mathrm{V}$, sendo equivalentes.
*e. $Q=10$, $R=0{,}1$, pois é o par com menor tempo de acomodação ($0{,}35\,\mathrm{s}$) que ainda respeita os $24\,\mathrm{V}$, já que $Q=100$ exige $40\,\mathrm{V}$, acima do limite.

**38.** O NexaBot possui um único sensor de velocidade angular $\omega$, sem sensor direto de corrente de armadura. Considerando que a matriz de observabilidade $\mathcal{O}=[C;\ CA]$ tem posto completo igual a 2, qual conclusão é correta?

a. É impossível estimar a corrente de armadura sem instalar um sensor físico adicional.
*b. É possível construir um observador de estados que reconstrua a corrente de armadura a partir apenas da medição de velocidade, pois o sistema é observável.
c. A observabilidade completa exige necessariamente um sensor para cada variável de estado do sistema.
d. O posto completo da matriz de observabilidade indica que o sistema é controlável, não observável.
e. A ausência de sensor de corrente torna o modelo em espaço de estados inválido.

**39.** Consultando a tabela de alocação de polos do NexaBot, reproduzida abaixo, entre qual par de polos duplos consecutivos o comando inicial $u(0)$ ultrapassa o limite de $24\,\mathrm{V}$ do driver?

| Polo duplo (rad/s) | $u(0)$ (V) |
| --- | --- |
| $-30$ | $7{,}00$ |
| $-50$ | $19{,}44$ |
| $-60$ | $28{,}00$ |
| $-100$ | $77{,}78$ |

a. Entre $-30$ e $-50\,\mathrm{rad/s}$.
b. Entre $-100\,\mathrm{rad/s}$ e um valor ainda mais rápido.
c. O limite nunca é ultrapassado para os polos apresentados.
*d. Entre $-50$ e $-60\,\mathrm{rad/s}$, pois $u(0)$ passa de $19{,}44\,\mathrm{V}$ (dentro do limite) para $28{,}00\,\mathrm{V}$ (acima do limite de $24\,\mathrm{V}$).
e. Exatamente em $-50\,\mathrm{rad/s}$, pois esse já é o valor limite.

**40.** Um estudante conclui que, como a matriz de controlabilidade do NexaBot tem posto completo, qualquer polo de malha fechada desejado — por mais rápido que seja — pode ser implementado sem restrição prática. Essa conclusão está:

a. Correta, pois controlabilidade garante viabilidade física irrestrita.
b. Correta, desde que o sistema também seja observável.
*c. Incorreta, pois controlabilidade garante apenas a existência matemática de uma entrada capaz de atingir o estado desejado, sem impor limite sobre sua magnitude — o driver satura em $24\,\mathrm{V}$, e comandos que excedem esse valor produzem respostas diferentes das previstas.
d. Incorreta, pois nenhum sistema controlável admite alocação de polos.
e. Correta, pois o LQR sempre resolve automaticamente qualquer limite físico do atuador.

## Gabarito e feedbacks

**Questão 1** (correta: a)
- a. Correta: I é verdadeira (definição de CPS da Aula 1) e II é verdadeira e explica corretamente o mecanismo — o acoplamento entre lógica discreta e dinâmica contínua produz exatamente o sistema híbrido descrito.
- b. Incorreta: a II realmente justifica a I nesta questão, pois descreve o mecanismo do acoplamento.
- c. Incorreta: a asserção II também é verdadeira, não falsa — o sistema híbrido é consequência direta do acoplamento descrito na I.
- d. Incorreta: a asserção I também é verdadeira, não falsa; é a definição de CPS apresentada na aula.
- e. Incorreta: as duas asserções são verdadeiras, não falsas.

**Questão 2** (correta: b)
- a. Incorreta: a II não justifica a I nesta questão; são fatos independentes sobre tópicos distintos da aula.
- b. Correta: ambas as asserções são verdadeiras (confinamento do erro de software ao domínio digital; estrutura do V-Model em dois ramos), mas a estrutura do V-Model não é a razão pela qual o erro de software fica confinado ao domínio digital.
- c. Incorreta: a asserção II também é verdadeira, não falsa.
- d. Incorreta: a asserção I também é verdadeira, não falsa.
- e. Incorreta: as duas asserções são verdadeiras, não falsas.

**Questão 3** (correta: e)
- a. Incorreta: as duas asserções são falsas, não verdadeiras.
- b. Incorreta: as duas asserções são falsas, não verdadeiras.
- c. Incorreta: a asserção I é falsa — erros de software em um CPS têm, sim, consequência física, e a dinâmica física não os corrige automaticamente.
- d. Incorreta: a asserção II também é falsa — o MBD antecipa a verificação para antes da implementação, não a concentra nela.
- e. Correta: a I é falsa, pois o exemplo da queda de velocidade do NexaBot mostra que erros de comando têm efeito físico não corrigido automaticamente; a II é falsa, pois o MBD desloca verificação para antes da implementação, exatamente o oposto do afirmado.

**Questão 4** (correta: c)
- a. Incorreta: a asserção II é falsa, não verdadeira.
- b. Incorreta: a asserção II é falsa, não verdadeira.
- c. Correta: a I é verdadeira — é exatamente o fenômeno da situação-problema da Aula 1, em que a velocidade cai e não se recupera; a II é falsa, pois a definição de malha aberta é justamente a ausência de realimentação contínua da medição.
- d. Incorreta: a asserção I é verdadeira, não falsa.
- e. Incorreta: a asserção I é verdadeira, não falsa.

**Questão 5** (correta: a)
- a. Correta: ambas as asserções são verdadeiras, e a II explica o mecanismo pelo qual o MBD permite a verificação antecipada mencionada na I — representar cada nível como modelo executável e verificável.
- b. Incorreta: a II realmente justifica a I nesta questão.
- c. Incorreta: a asserção II também é verdadeira, não falsa.
- d. Incorreta: a asserção I também é verdadeira, não falsa.
- e. Incorreta: as duas asserções são verdadeiras, não falsas.

**Questão 6** (correta: d)
- a. Incorreta: a asserção I é falsa, não verdadeira.
- b. Incorreta: a asserção I é falsa, não verdadeira.
- c. Incorreta: a asserção I é falsa, e a II é verdadeira, não falsa.
- d. Correta: a I é falsa — a velocidade angular não pode ser calculada apenas a partir da corrente presente, pois obedece à sua própria equação diferencial; a II é verdadeira e descreve corretamente o vetor de estado mínimo do NexaBot, $x=[i,\omega]^T$.
- e. Incorreta: a asserção II é verdadeira, não falsa.

**Questão 7** (correta: b)
- a. Incorreta: a II não explica a diferença de ordem de grandeza entre as linhas de $A$, que decorre da razão entre os parâmetros elétricos e mecânicos ($R/L$ versus $b/J$), não do método de identificação.
- b. Correta: ambas as asserções são verdadeiras — a assimetria de $A$ é observada na aula, e o método de ajuste da trajetória inteira também é descrito —, mas a II não é a razão da I; são fatos independentes.
- c. Incorreta: a asserção II também é verdadeira, não falsa.
- d. Incorreta: a asserção I também é verdadeira, não falsa.
- e. Incorreta: as duas asserções são verdadeiras, não falsas.

**Questão 8** (correta: c)
- a. Incorreta: a asserção II é falsa, não verdadeira.
- b. Incorreta: a asserção II é falsa, não verdadeira.
- c. Correta: a I é verdadeira — reservar dados nunca usados no ajuste é exatamente a prática de validação descrita na aula, para evitar sobreajuste; a II é falsa, pois `fit%` mede a concordância entre a saída prevista e a saída medida do sistema, não o comando de tensão aplicado.
- d. Incorreta: a asserção I é verdadeira, não falsa.
- e. Incorreta: a asserção I é verdadeira, não falsa.

**Questão 9** (correta: e)
- a. Incorreta: as duas asserções são falsas, não verdadeiras.
- b. Incorreta: as duas asserções são falsas, não verdadeiras.
- c. Incorreta: a asserção I é falsa — o laboratório da Aula 2 mostra explicitamente que amostrar no período de controle de $5\,\mathrm{ms}$ faz a constante de tempo elétrica ($2{,}92\,\mathrm{ms}$) desaparecer, comprometendo a identificação de $R$ e $L$.
- d. Incorreta: a asserção II também é falsa — a quantização do encoder afeta a medição de velocidade, sem qualquer relação com o ruído do sinal de corrente.
- e. Correta: a I é falsa, pois amostragem no período de controle perde informação sobre a dinâmica elétrica rápida; a II é falsa, pois quantização de encoder e ruído de corrente são efeitos independentes em sensores distintos.

**Questão 10** (correta: d)
- a. Incorreta: a asserção I é falsa, não verdadeira.
- b. Incorreta: a asserção I é falsa, não verdadeira.
- c. Incorreta: a asserção I é falsa, e a II é verdadeira, não falsa.
- d. Correta: a I é falsa — $B$ depende apenas de $L$, e $C$, $D$ não dependem de $R$ nem de $L$, ao contrário de $A$, cujas quatro entradas envolvem $R$, $L$, $K_t$, $K_e$, $J$ e $b$; a II é verdadeira e descreve corretamente essas três matrizes.
- e. Incorreta: a asserção II é verdadeira, não falsa.

**Questão 11** (correta: c)
- a. Incorreta: a asserção II é falsa, não verdadeira.
- b. Incorreta: a asserção II é falsa, não verdadeira.
- c. Correta: a I é verdadeira — $G(s)$ do NexaBot não tem zeros finitos, então a forma da resposta depende inteiramente dos dois polos; a II é falsa, pois os polos $-7{,}215$ e $-335{,}96\,\mathrm{rad/s}$ são reais negativos, no semiplano esquerdo, indicando estabilidade, não instabilidade.
- d. Incorreta: a asserção I é verdadeira, não falsa.
- e. Incorreta: a asserção I é verdadeira, não falsa.

**Questão 12** (correta: a)
- a. Correta: ambas as asserções são verdadeiras, e a II explica exatamente por que a resposta observada da velocidade se assemelha à de primeira ordem — a enorme diferença entre as constantes de tempo elétrica e mecânica.
- b. Incorreta: a II realmente justifica a I nesta questão.
- c. Incorreta: a asserção II também é verdadeira, não falsa.
- d. Incorreta: a asserção I também é verdadeira, não falsa.
- e. Incorreta: as duas asserções são verdadeiras, não falsas.

**Questão 13** (correta: e)
- a. Incorreta: as duas asserções são falsas, não verdadeiras.
- b. Incorreta: as duas asserções são falsas, não verdadeiras.
- c. Incorreta: a asserção I é falsa — o Bode do NexaBot exibe dois pontos de quebra distintos, em $7{,}215$ e $335{,}96\,\mathrm{rad/s}$, pois os polos estão bem separados, não coincidem.
- d. Incorreta: a asserção II também é falsa — a definição descrita é a de margem de ganho, não de margem de fase.
- e. Correta: a I é falsa, pois os dois polos do NexaBot produzem dois pontos de quebra distintos no Bode; a II é falsa, pois troca a definição de margem de fase (tolerância a atraso de fase adicional) pela de margem de ganho.

**Questão 14** (correta: b)
- a. Incorreta: a II é verdadeira como definição geral de Bode, mas não explica por que existe separação de escalas de tempo entre os polos do NexaBot.
- b. Correta: ambas as asserções são verdadeiras — a separação de quase duas ordens de grandeza é discutida na Aula 3, e a definição de Bode também está correta —, mas a II não é a razão da I; são fatos independentes sobre tópicos diferentes.
- c. Incorreta: a asserção II também é verdadeira, não falsa.
- d. Incorreta: a asserção I também é verdadeira, não falsa.
- e. Incorreta: as duas asserções são verdadeiras, não falsas.

**Questão 15** (correta: d)
- a. Incorreta: a asserção I é falsa, não verdadeira.
- b. Incorreta: a asserção I é falsa, não verdadeira.
- c. Incorreta: a asserção I é falsa, e a II é verdadeira, não falsa.
- d. Correta: a I é falsa — largura de banda não tem relação com tensão máxima do driver, esse é um limite de saturação do atuador, tema da Aula 4; a II é verdadeira e reproduz a definição correta de largura de banda dada na Aula 3.
- e. Incorreta: a asserção II é verdadeira, não falsa.

**Questão 16** (correta: a)
- a. Correta: ambas as asserções são verdadeiras, e a II fornece a justificativa matemática exata da I — o determinante não nulo de $\mathcal{C}=[B\ AB]$ confirma posto completo, condição necessária e suficiente de controlabilidade.
- b. Incorreta: a II realmente justifica a I nesta questão.
- c. Incorreta: a asserção II também é verdadeira, não falsa.
- d. Incorreta: a asserção I também é verdadeira, não falsa.
- e. Incorreta: as duas asserções são verdadeiras, não falsas.

**Questão 17** (correta: c)
- a. Incorreta: a asserção II é falsa, não verdadeira.
- b. Incorreta: a asserção II é falsa, não verdadeira.
- c. Correta: a I é verdadeira — é exatamente a situação-problema da Aula 4, em que a alocação de polos exige tensão acima de $24\,\mathrm{V}$; a II é falsa, pois controlabilidade garante apenas existência matemática de uma entrada, sem impor limite sobre sua magnitude.
- d. Incorreta: a asserção I é verdadeira, não falsa.
- e. Incorreta: a asserção I é verdadeira, não falsa.

**Questão 18** (correta: e)
- a. Incorreta: as duas asserções são falsas, não verdadeiras.
- b. Incorreta: as duas asserções são falsas, não verdadeiras.
- c. Incorreta: a asserção I é falsa — o LQR enfrenta o mesmo compromisso desempenho-esforço da alocação de polos e pode, sim, exigir tensão acima do limite do driver.
- d. Incorreta: a asserção II também é falsa — aumentar $Q$ em relação a $R$ desloca os polos resultantes para valores mais rápidos, alterando diretamente sua posição.
- e. Correta: a I é falsa, pois o LQR não elimina a necessidade de respeitar o limite de tensão; a II é falsa, pois $Q$ e $R$ determinam diretamente a posição dos polos de malha fechada, não apenas o tempo de execução do algoritmo.

**Questão 19** (correta: b)
- a. Incorreta: a II é verdadeira, mas não é a razão pela qual a observabilidade permite reconstruir a corrente a partir da velocidade; são conceitos de projetos distintos (observador de estados versus ganho de referência da realimentação).
- b. Correta: ambas as asserções são verdadeiras — a observabilidade do NexaBot sustenta a reconstrução da corrente, e $\bar{N}$ garante erro nulo em regime —, mas a II não explica a I.
- c. Incorreta: a asserção II também é verdadeira, não falsa.
- d. Incorreta: a asserção I também é verdadeira, não falsa.
- e. Incorreta: as duas asserções são verdadeiras, não falsas.

**Questão 20** (correta: d)
- a. Incorreta: a asserção I é falsa, não verdadeira.
- b. Incorreta: a asserção I é falsa, não verdadeira.
- c. Incorreta: a asserção I é falsa, e a II é verdadeira, não falsa.
- d. Correta: a I é falsa — a tabela da Aula 4 mostra o oposto: ganhos $K$ maiores produzem comandos iniciais maiores, não menores; a II é verdadeira e descreve corretamente essa relação entre velocidade do polo, magnitude de $K$ e comando inicial.
- e. Incorreta: a asserção II é verdadeira, não falsa.

**Questão 21** (correta: c)
- a. Incorreta: $0{,}93\,\mathrm{m/s}$ é o resultado do exemplo da aula para uma carga de $0{,}05\,\mathrm{N\,m}$, não de $0{,}10\,\mathrm{N\,m}$.
- b. Incorreta: $0{,}80\,\mathrm{m/s}$ subestima a velocidade resultante; o cálculo correto usando a mesma equação de regime da aula fornece um valor mais próximo de $0{,}86\,\mathrm{m/s}$.
- c. Correta: $R\tau_{\text{carga}}/K_t = (1{,}2\times0{,}10)/0{,}045 = 2{,}667\,\mathrm{V}$; $\omega=(18{,}85-2{,}667)/0{,}047133\approx343{,}3\,\mathrm{rad/s}$; $v=\omega r/N=343{,}3\times0{,}05/20\approx0{,}858\,\mathrm{m/s}$, ou seja, aproximadamente $0{,}86\,\mathrm{m/s}$.
- d. Incorreta: $0{,}70\,\mathrm{m/s}$ corresponderia a um torque de carga bem maior que $0{,}10\,\mathrm{N\,m}$.
- e. Incorreta: $1{,}00\,\mathrm{m/s}$ ignora completamente o efeito do torque de carga sobre o comando fixo.

**Questão 22** (correta: d)
- a. Incorreta: a malha aberta não possui mecanismo de detecção ou correção de erros de parâmetro, muito menos automático.
- b. Incorreta: controlabilidade é uma propriedade da planta relacionada à existência de entrada adequada, sem relação com detecção prévia de erros de parâmetro em campo.
- c. Incorreta: o ganho estático $\omega/V=K_t/(Rb+K_tK_e)$ depende diretamente de $b$; um erro em $b$ altera esse ganho.
- d. Correta: o argumento econômico do MBD, apresentado na Aula 1, é justamente que o custo de corrigir um defeito cresce fortemente com o atraso na descoberta; capturar o erro de parâmetro por simulação evita o custo de reprojeto de hardware já em campo.
- e. Incorreta: a separação de escalas de tempo entre os polos elétrico e mecânico não elimina a necessidade de verificar parâmetros mecânicos como $b$.

**Questão 23** (correta: a)
- a. Correta: o comportamento descrito — dinâmica contínua da planta entre instantes discretos de amostragem, com comando mantido por segurador de ordem zero — é exatamente a definição de sistema híbrido apresentada na Aula 1.
- b. Incorreta: o comando de tensão é, sim, atualizado, ainda que apenas nos instantes discretos de amostragem.
- c. Incorreta: a planta continua evoluindo continuamente entre as amostras, segundo suas equações diferenciais; não é um sistema puramente discreto.
- d. Incorreta: manter o comando constante entre amostras é o comportamento esperado de um controlador digital, não uma falha de temporização.
- e. Incorreta: a existência de amostragem da velocidade para atualizar o comando é, por definição, um mecanismo de realimentação, não uma malha aberta.

**Questão 24** (correta: b)
- a. Incorreta: o NexaBot é um CPS típico, pois seu firmware (lógica discreta) decide comandos que atuam sobre motor, roda e carga (dinâmica física contínua).
- b. Correta: a Aula 1 explica exatamente essa diferença — em um CPS, o acoplamento entre código e mundo físico faz o efeito de um erro atravessar essa fronteira, produzindo consequência física irreversível, sem possibilidade de desfazer a ação (sem *undo*).
- c. Incorreta: a confiabilidade não é definida pelo tipo de sistema, e sim pelas consequências do acoplamento entre lógica e física, tema central da aula.
- d. Incorreta: a diferença de consequência decorre do acoplamento físico-computacional descrito na aula, não apenas da velocidade de processamento.
- e. Incorreta: é justamente o oposto do argumento da aula — a mesma gravidade lógica pode ter consequências muito diferentes conforme o sistema seja ou não um CPS.

**Questão 25** (correta: e)
- a. Incorreta: o ramo descendente concentra a definição de modelos (planta, controlador, propriedades formais), não a verificação.
- b. Incorreta: modelo executável (ramo descendente) e verificação (ramo ascendente) são conceitos complementares, não sinônimos.
- c. Incorreta: o V-Model aplicado a CPS mantém os dois ramos, descendente e ascendente, exatamente como em qualquer aplicação do V-Model.
- d. Incorreta: a atividade prática da aula pede a classificação predominante de cada unidade, não uma divisão igualitária arbitrária entre os ramos.
- e. Correta: simulação, *model checking* e testes são atividades de verificação, que pertencem ao ramo ascendente, conferindo cada nível contra o nível correspondente do ramo descendente de definição do modelo.

**Questão 26** (correta: d)
- a. Incorreta: a tabela não mostra esse padrão; os erros de $J$ e $b$ (0,02% e 0,63%) são, na verdade, tão pequenos quanto os de $R$ e $L$.
- b. Incorreta: se o ensaio tivesse sido amostrado no período de controle de $5\,\mathrm{ms}$, os erros de $R$ e $L$ seriam muito maiores, pois a constante de tempo elétrica de $2{,}92\,\mathrm{ms}$ desapareceria sob essa amostragem — o que não ocorre nos dados apresentados.
- c. Incorreta: a igualdade aparente entre os erros é justamente o efeito buscado por um ensaio bem amostrado, e não evidência de ausência de qualquer efeito de escala de tempo.
- d. Correta: erros pequenos e semelhantes para os quatro parâmetros indicam que a amostragem do ensaio capturou tanto a dinâmica elétrica rápida quanto a mecânica lenta, sem a perda de informação que ocorreria com subamostragem.
- e. Incorreta: o ganho estático depende de $R$ e $b$, entre outros parâmetros; não há independência entre eles.

**Questão 27** (correta: c)
- a. Incorreta: $-0{,}343$ corresponde a um erro de posicionamento de vírgula decimal no cálculo.
- b. Incorreta: $-34{,}29$ subestima o resultado por um fator de 10.
- c. Correta: $-R/L = -1{,}2/0{,}0035 = -342{,}857$, exatamente o valor reportado na Aula 2 para essa entrada da matriz $A$.
- d. Incorreta: $-3{,}429$ subestima o resultado por um fator de 100.
- e. Incorreta: $-3428{,}57$ superestima o resultado por um fator de 10.

**Questão 28** (correta: e)
- a. Incorreta: um bom ajuste no próprio conjunto usado no ajuste não comprova validade geral do modelo; é exatamente o risco de sobreajuste discutido na aula.
- b. Incorreta: o ensaio de validação é a ferramenta correta para detectar sobreajuste; descartá-lo eliminaria a única evidência do problema.
- c. Incorreta: nada no cenário indica falha física do motor; a queda de `fit%` é explicada por sobreajuste ao ruído do primeiro ensaio.
- d. Incorreta: uma queda tão grande (de 98% para 40%) não é esperada em um modelo bem ajustado; indica problema de generalização, não um comportamento normal.
- e. Correta: a queda acentuada entre ajuste e validação é o sintoma clássico de sobreajuste ao ruído específico do primeiro ensaio, exatamente o risco que a validação com dados retidos, descrita na Aula 2, busca detectar.

**Questão 29** (correta: a)
- a. Correta: $C=[0\ \ 1]$ seleciona a segunda componente de $x=[i,\omega]^T$, portanto $y=Cx=\omega$, a velocidade angular.
- b. Incorreta: a corrente $i$ é a primeira componente de $x$, mas $C$ tem zero na primeira posição, não a selecionando como saída.
- c. Incorreta: $C$ é um vetor linha que produz uma única saída escalar, não as duas variáveis de estado simultaneamente.
- d. Incorreta: $D=0$ apenas indica ausência de transmissão direta da entrada à saída; a saída $y=Cx$ continua definida e igual a $\omega$.
- e. Incorreta: $B$ define como a entrada afeta a dinâmica dos estados, não a saída do sistema; a tensão $V$ é a entrada $u$, não a saída $y$.

**Questão 30** (correta: b)
- a. Incorreta: os dois métodos não são equivalentes; a aula destaca explicitamente a vantagem do ajuste da trajetória inteira sobre a estimação de derivadas ponto a ponto.
- b. Correta: a Aula 2 explica que ajustar a trajetória inteira evita amplificar ruído de medição, ao contrário de estimar derivadas ponto a ponto, que é sensível a esse ruído.
- c. Incorreta: a estimativa por derivadas ponto a ponto não é mais precisa; é justamente mais sensível a ruído e a mal-condicionamento.
- d. Incorreta: a necessidade de um segundo ensaio de validação é independente do método usado para estimar as derivadas; a validação continua sendo necessária.
- e. Incorreta: nada no método de derivadas ponto a ponto reduz a quantidade de dados necessária; ambos os métodos partem do mesmo ensaio de degrau.

**Questão 31** (correta: e)
- a. Incorreta: $4{,}7$ não corresponde à divisão indicada nem representa a razão entre tensão máxima e ganho estático.
- b. Incorreta: $335{,}96$ é o valor do polo elétrico isoladamente, não o resultado da divisão pedida.
- c. Incorreta: $7{,}215$ é o valor do polo mecânico isoladamente, não o resultado da divisão pedida.
- d. Incorreta: $21{,}2$ corresponde ao ganho estático $\omega/V$ em rad/(s·V), calculado na Aula 2, não à razão entre os polos.
- e. Correta: $335{,}96/7{,}215\approx46{,}6$, o valor que a Aula 3 identifica como a separação de escalas de tempo entre as dinâmicas elétrica e mecânica.

**Questão 32** (correta: a)
- a. Correta: entre os dois pontos de quebra, o polo rápido já deixou de influenciar significativamente a magnitude, e o sistema se comporta, nessa faixa, como se tivesse apenas o polo lento — a mesma observação da situação-problema, agora no domínio da frequência.
- b. Incorreta: estar entre dois polos não produz ganho infinito; ganho infinito ocorreria apenas em um zero no denominador nulo, o que não é o caso aqui.
- c. Incorreta: os polos do NexaBot são reais negativos (semiplano esquerdo); a planta é estável em toda a faixa de frequência, não apenas até o primeiro ponto de quebra.
- d. Incorreta: a fase varia continuamente entre $0°$ e $-180°$ ao longo da faixa de frequência; não permanece constante.
- e. Incorreta: a inclinação de $-40\,\mathrm{dB/década}$ só ocorre acima do segundo ponto de quebra ($335{,}96\,\mathrm{rad/s}$); entre os dois pontos, a inclinação é de $-20\,\mathrm{dB/década}$.

**Questão 33** (correta: d)
- a. Incorreta: $-21{,}2$ e $-400$ não são raízes do polinômio; $21{,}2$ é o ganho estático, e $400$ é a velocidade angular nominal do exemplo da Aula 1, grandezas distintas dos polos.
- b. Incorreta: $-46{,}6$ é a razão entre os polos, não um polo; $-148$ tem unidade de milissegundos (constante de tempo), não de rad/s.
- c. Incorreta: $-2{,}92$ tem unidade de milissegundos (constante de tempo elétrica), não de rad/s; os valores estão trocados de grandeza.
- d. Correta: aplicando Bhaskara aos coeficientes fornecidos, obtêm-se exatamente $-7{,}215\,\mathrm{rad/s}$ e $-335{,}96\,\mathrm{rad/s}$, os dois polos do NexaBot calculados na Aula 3.
- e. Incorreta: $-0{,}32$ e $-342{,}857$ são entradas da matriz $A$ em espaço de estados, não os polos de $G(s)$, que resultam da combinação de todas as entradas de $A$.

**Questão 34** (correta: c)
- a. Incorreta: estabilidade é necessária, mas um sobressinal de $71{,}3\%$ pode violar requisitos de desempenho e segurança.
- b. Incorreta: a planta em malha aberta tem polos negativos; o sobressinal citado pertence à resposta em malha fechada.
- c. Correta: por Routh–Hurwitz, os coeficientes do polinômio de segunda ordem permanecem positivos para $K_p>0$; a discretização acrescenta o efeito que permite um ganho crítico finito na Aula 6.
- d. Incorreta: a margem de fase diminui conforme $K_p$ cresce nessa varredura.
- e. Incorreta: sobressinal e margem de fase se relacionam, mas $71{,}3\%$ não significa margem exatamente nula; a saída ainda converge.

**Questão 35** (correta: b)
- a. Incorreta: a aula não afirma que toda redução de ordem é ilegítima; a legitimidade depende do uso pretendido do modelo, conforme a Pausa para Reflexão.
- b. Correta: a Pausa para Reflexão da Aula 3 lista exatamente essas ressalvas — o efeito sobre a precisão em frequências próximas ao polo rápido e sobre a análise da corrente, ligada ao requisito REQ-PLANT-002 de $12\,\mathrm{A}$.
- c. Incorreta: a aula explicitamente rejeita esse critério único e automático, indicando que não há resposta universal para a legitimidade da redução.
- d. Incorreta: pelo contrário, a aula relaciona a legitimidade da redução também ao período de amostragem do controlador ($T_s=5\,\mathrm{ms}$), próximo da constante de tempo elétrica.
- e. Incorreta: a ressalva discutida envolve tanto a análise de resposta em frequência quanto a de corrente, não apenas controlabilidade — tema que sequer é tratado na Aula 3.

**Questão 36** (correta: a)
- a. Correta: determinante não nulo da matriz de controlabilidade $\mathcal{C}=[B\ AB]$ significa posto completo, condição necessária e suficiente para o sistema ser controlável — existe, em princípio, uma entrada capaz de levar o estado a qualquer condição desejada.
- b. Incorreta: observabilidade é verificada pela matriz $\mathcal{O}=[C;\ CA]$, não pela matriz de controlabilidade $\mathcal{C}$.
- c. Incorreta: o sinal do determinante da matriz de controlabilidade não indica estabilidade do sistema; estabilidade é determinada pelos polos (autovalores de $A$).
- d. Incorreta: é o oposto — determinante não nulo (posto completo) é o que permite a realimentação de estados para alocação arbitrária de polos.
- e. Incorreta: controlabilidade é condição necessária, mas não suficiente, para viabilidade física — o resultado tem relação direta com o tema, mas não garante, por si só, que o comando exigido respeite o limite do driver.

**Questão 37** (correta: e)
- a. Incorreta: $Q=100$ exige pico de tensão de $40\,\mathrm{V}$, acima do limite de $24\,\mathrm{V}$, tornando-o inviável apesar do menor tempo de acomodação.
- b. Incorreta: $Q=1$ respeita o limite, mas não é o mais agressivo entre os pares viáveis; $Q=10$ obtém tempo de acomodação menor ainda dentro do limite.
- c. Incorreta: os pares $Q=1$ e $Q=10$ respeitam o limite de $24\,\mathrm{V}$ ($12\,\mathrm{V}$ e $22\,\mathrm{V}$, respectivamente).
- d. Incorreta: os três pares não são equivalentes; apenas $Q=100$ excede o limite, com pico de $40\,\mathrm{V}$.
- e. Correta: entre os pares viáveis ($Q=1$ com $12\,\mathrm{V}$ e $Q=10$ com $22\,\mathrm{V}$, ambos abaixo de $24\,\mathrm{V}$), $Q=10$ tem o menor tempo de acomodação ($0{,}35\,\mathrm{s}$), sendo o mais agressivo ainda compatível com o limite do driver.

**Questão 38** (correta: b)
- a. Incorreta: é exatamente o oposto do que a observabilidade garante — reconstruir a corrente sem sensor físico adicional, a partir apenas da velocidade medida.
- b. Correta: posto completo de $\mathcal{O}=[C;\ CA]$ significa que o sistema é observável, permitindo construir um observador de estados que reconstrua a corrente de armadura a partir apenas da medição de velocidade, como discutido na Aula 4.
- c. Incorreta: é justamente a vantagem da observabilidade dispensar essa exigência — reconstruir estados não medidos diretamente a partir das saídas disponíveis.
- d. Incorreta: posto completo de $\mathcal{O}=[C;\ CA]$ é o critério de observabilidade, não de controlabilidade, que é verificada por $\mathcal{C}=[B\ AB]$.
- e. Incorreta: a ausência de sensor de corrente não invalida o modelo; é justamente a situação que a observabilidade resolve, permitindo estimar a corrente por um observador.

**Questão 39** (correta: d)
- a. Incorreta: entre $-30$ e $-50\,\mathrm{rad/s}$, a tensão sobe de $7{,}00\,\mathrm{V}$ para $19{,}44\,\mathrm{V}$, permanecendo dentro do limite de $24\,\mathrm{V}$.
- b. Incorreta: o limite já é ultrapassado antes de $-100\,\mathrm{rad/s}$, onde a tensão chega a $77{,}78\,\mathrm{V}$, muito além de $24\,\mathrm{V}$.
- c. Incorreta: a tabela mostra claramente valores acima de $24\,\mathrm{V}$ a partir de $-60\,\mathrm{rad/s}$.
- d. Correta: entre os polos $-50\,\mathrm{rad/s}$ ($19{,}44\,\mathrm{V}$, dentro do limite) e $-60\,\mathrm{rad/s}$ ($28{,}00\,\mathrm{V}$, acima do limite), o comando ultrapassa os $24\,\mathrm{V}$ do driver.
- e. Incorreta: em $-50\,\mathrm{rad/s}$ a tensão é $19{,}44\,\mathrm{V}$, ainda abaixo do limite de $24\,\mathrm{V}$, não exatamente no limite.

**Questão 40** (correta: c)
- a. Incorreta: controlabilidade não garante viabilidade física irrestrita; ela apenas assegura existência matemática de uma entrada, sem limite sobre sua magnitude.
- b. Incorreta: mesmo com observabilidade garantida, o limite de tensão do driver permanece um limite físico independente, que a controlabilidade não elimina.
- c. Correta: controlabilidade garante apenas existência matemática de uma entrada capaz de atingir o estado desejado; o driver satura em $24\,\mathrm{V}$, e um comando que exceda esse valor produz, na prática, uma resposta diferente da prevista pelo projeto — distinção central da Aula 4 entre existência matemática e viabilidade física.
- d. Incorreta: sistemas controláveis admitem, sim, alocação arbitrária de polos; o problema não está na alocação em si, mas na magnitude do comando resultante.
- e. Incorreta: o LQR enfrenta o mesmo compromisso desempenho-esforço da alocação direta de polos, via $Q$ e $R$; ele não resolve automaticamente o limite físico do atuador.
