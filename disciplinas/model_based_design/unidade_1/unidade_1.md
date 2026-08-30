# Unidade 1 — Fundamentos de sistemas ciberfísicos e modelagem da planta

Disciplina: Model-Based Design for Cyber-Physical Systems
Professor-conteudista: Afonso Cesar Lelis Brandão

## Relação da unidade com a atuação profissional

Sistemas ciberfísicos governam boa parte da produção industrial, da logística e da mobilidade: braços robóticos, veículos autônomos, redes elétricas inteligentes, equipamentos médicos e frotas de veículos guiados automaticamente (AGV) em armazéns. Em todos esses casos, um algoritmo executado em um processador de baixo custo decide, em milissegundos, como atuar sobre um sistema físico com massa, atrito e limites elétricos que não obedecem a nenhuma linha de código. Projetar esse tipo de sistema sem antes possuir um modelo matemático validado da planta significa ajustar parâmetros por tentativa e erro sobre um equipamento real — abordagem cara, lenta e, em sistemas de segurança crítica, inaceitável.

Esta unidade estabelece a competência que sustenta toda a disciplina: transformar um sistema físico real em um modelo matemático rigoroso, simulável, analisável e, mais adiante, controlável e verificável antes de qualquer código tocar o equipamento. Você derivará equações a partir de leis físicas de conservação, representará o resultado em espaço de estados e em função de transferência, identificará parâmetros a partir de dados de ensaio — como faria um engenheiro diante de um motor real, sem datasheet completo — e avaliará controlabilidade e observabilidade, propriedades que decidem, antes de qualquer projeto de controlador, se um objetivo de desempenho é sequer alcançável.

Essas competências aparecem no cotidiano de quem projeta sistemas automotivos, aeroespaciais, robóticos e industriais. A pergunta inicial é sempre a mesma: qual é o modelo da planta, e como sei que ele está correto? Responder com rigor evita retrabalho caro em bancada, antecipa limitações físicas do atuador e comunica, a outros engenheiros e a auditores de qualidade, exatamente que hipóteses sustentam cada decisão de projeto.

Ao final desta unidade, você terá modelado, identificado e analisado a planta de tração de um veículo autoguiado real de armazém — o NexaBot —, com os métodos e ferramentas usados pela indústria em 2026: Python, `python-control`, SymPy e mínimos quadrados não lineares. Esse modelo é a base sobre a qual as três unidades seguintes constroem controle, verificação formal e geração automática de código.

## O que você verá nesta unidade

Na Aula 1, você compreenderá o que distingue um sistema ciberfísico e por que o design baseado em modelos (MBD) reduz o custo de encontrar defeitos, situando essa abordagem no V-Model. Na Aula 2, derivará as equações do motor de tração do NexaBot a partir de leis de circuitos e de rotação, reescrevendo-as em espaço de estados, e identificará parâmetros a partir de dados de ensaio com ruído realista. Na Aula 3, aplicará a transformada de Laplace para obter a função de transferência da planta, interpretará seus polos fisicamente e explorará a resposta em frequência. Na Aula 4, avaliará controlabilidade e observabilidade e projetará uma primeira realimentação de estados, descobrindo que nem todo projeto matematicamente correto respeita os limites físicos do atuador.

O fio condutor é o NexaBot, um AGV industrial com tração por motor de corrente contínua de ímã permanente. Cada aula avança sobre o mesmo sistema físico, sem trocar de exemplo.

## Aula 1 — Sistemas ciberfísicos e o ciclo do design baseado em modelos

### Situação-problema: o NexaBot que não sustenta a velocidade

Um protótipo do NexaBot mantém 1,00 m/s constante no transporte de peças, com tensão calculada uma vez, em malha aberta. Vazio, sustenta a velocidade; ao receber uma caixa — torque de carga adicional —, a velocidade cai e não se recupera.

Nada quebrou: um comando fixo, calculado para uma condição, não sabe que ela mudou. Esta aula constrói o vocabulário do MBD que torna esse tipo de falha previsível antes de chegar a campo; a Unidade 2 traz a solução por realimentação.

### O que torna um sistema ciberfísico distinto

Um **sistema ciberfísico** (*cyber-physical system*, CPS) integra computação discreta — software com estados, laços e decisões — e dinâmica física contínua, como corrente e velocidade angular, regidas por equações diferenciais. O NexaBot é típico: o firmware lê sensores e decide a tensão; motor, roda e carga obedecem a leis de circuito e rotação.

Frente a software comum, o acoplamento muda a gravidade do erro: uma falha num sistema de informação gera dado incorreto, confinado ao digital; no CPS, pode gerar colisão ou peça derrubada, sem *undo*. Frente a um sistema puramente físico, a diferença é a lógica discreta decidindo como atuar: um motor sem controlador só obedece equações diferenciais; amostrado a cada 5 ms por um algoritmo que decide a tensão, vira CPS.

### Acoplamento entre dinâmica contínua e lógica discreta

Esse acoplamento produz um **sistema híbrido**: evolução contínua (a planta obedecendo suas equações entre amostras) intercalada por eventos discretos (sensor, controlador, atualização do comando). Só a parte contínua ignora que o comando muda a cada $T_s$; só a discreta ignora que a planta evolui entre decisões. O MBD trata as duas num framework único.

> **Recurso visual 1 — Linha do tempo de um sistema híbrido.** Eixo horizontal de tempo mostrando a velocidade angular evoluindo continuamente (curva suave) enquanto marcadores verticais, espaçados por $T_s = 5\,\mathrm{ms}$, indicam os instantes discretos em que o controlador amostra a saída e atualiza o comando de tensão, que permanece constante entre dois marcadores (efeito de segurador de ordem zero).
> *Texto alternativo:* Linha do tempo mostra a velocidade angular do NexaBot evoluindo continuamente entre instantes discretos de amostragem espaçados por 5 ms, nos quais o comando de tensão é atualizado e mantido constante até a amostra seguinte.

### Por que o erro em CPS tem consequência física

Em software convencional, corrigir um defeito é barato: identificar, corrigir, reimplantar. Num CPS, o defeito pode já ter produzido efeito físico irreversível antes de identificado — por isso a engenharia de CPS desloca verificação para antes da implantação.

### O V-Model e a posição do MBD

O **V-Model** organiza o desenvolvimento em dois ramos: no descendente, requisitos se decompõem em arquitetura e projeto até a implementação; no ascendente, cada nível é verificado contra o correspondente. O MBD representa cada nível descendente como **modelo executável**: REQ-PLANT-001 ("erro do modelo da planta no ensaio de degrau inferior a 5%") já nasce verificável, testado muito antes do código embarcado — o ganho central do MBD é adiantar a verificação.

> **Recurso visual 2 — O V-Model com o MBD sobreposto.** Diagrama em V: ramo esquerdo (Requisitos → Arquitetura → Projeto detalhado → Implementação) e ramo direito (Teste unitário → Integração → Sistema → Validação), com setas horizontais de verificação ligando níveis correspondentes; sobreposto, uma camada indica que cada nível do ramo esquerdo já produz um modelo executável verificável antes de descer ao próximo nível.
> *Texto alternativo:* Diagrama em V mostra o desenvolvimento descendo por requisitos, arquitetura, projeto e implementação, e subindo por testes correspondentes, com o design baseado em modelos sobreposto a cada nível do ramo descendente.

O custo de corrigir um defeito cresce exponencialmente com a fase de descoberta: um erro corrigido em campo pode exigir reprojeto de hardware ou nova certificação — o argumento econômico do MBD: capturar o erro por simulação evita esse custo.

### Demonstração: por que a malha aberta falha sob carga

Um controle em **malha aberta** calcula o comando uma vez, sem realimentar medição alguma. Dimensionado para a condição nominal (sem carga), ao mudar a condição física a relação tensão-velocidade muda e o comando antigo não corresponde ao objetivo, operando incorretamente até intervenção humana.

### Exemplo numérico: o NexaBot em malha aberta, com e sem carga

Parâmetros: $R = 1{,}2\,\Omega$, $L = 3{,}5\,\mathrm{mH}$, $K_t = 0{,}045\,\mathrm{N\,m/A}$, $K_e = 0{,}045\,\mathrm{V\,s/rad}$, $J = 2{,}5 \times 10^{-4}\,\mathrm{kg\,m^2}$, $b = 8{,}0 \times 10^{-5}\,\mathrm{N\,m\,s/rad}$, $N = 20$, $r = 0{,}05\,\mathrm{m}$.

Em regime permanente, $0 = V - Ri - K_e\omega$ e $0 = K_t i - b\omega - \tau_{\text{carga}}$; isolando $i$ e substituindo:

$
V = \omega\left(\frac{Rb}{K_t} + K_e\right) + \frac{R\,\tau_{\text{carga}}}{K_t}
$

**Sem carga:** $1{,}00\,\mathrm{m/s}$ corresponde a $\omega = v N/r = 1{,}00 \times 20/0{,}05 = 400\,\mathrm{rad/s}$. Com $\tau_{\text{carga}}=0$: $Rb/K_t = (1{,}2 \times 8{,}0\times10^{-5})/0{,}045 = 0{,}002133$; somando $K_e$: $0{,}047133$. Logo $V = 400 \times 0{,}047133 = 18{,}85\,\mathrm{V}$.

**Com carga de $0{,}05\,\mathrm{N\,m}$**, mantendo $V=18{,}85\,\mathrm{V}$: $R\tau_{\text{carga}}/K_t = (1{,}2 \times 0{,}05)/0{,}045 = 1{,}3333\,\mathrm{V}$; $\omega = (18{,}85-1{,}3333)/0{,}047133 \approx 371{,}65\,\mathrm{rad/s}$; $v = \omega r/N = 371{,}65 \times 0{,}05/20 \approx 0{,}929\,\mathrm{m/s}$. Erro relativo: $(1{,}00-0{,}929)/1{,}00 \approx 7{,}1\%$, que persiste sem correção. Os $18{,}85\,\mathrm{V}$ já consomem boa parte da folga do driver: com ganho estático de $21{,}2164\,\mathrm{rad/(s\,V)}$, os $24\,\mathrm{V}$ máximos produziriam, sem carga, velocidade máxima de $1{,}273\,\mathrm{m/s}$ — margem estreita, consumida por um controlador mal dimensionado (Aula 4).

> **Recurso visual 3 — Velocidade do NexaBot em malha aberta, com e sem carga.** Gráfico de velocidade linear (m/s) versus tempo (s): a curva sobe suavemente até 1,00 m/s e se mantém estável; a partir de um instante marcado, cai e se estabiliza em cerca de 0,93 m/s após a aplicação do torque de carga de 0,05 N·m, com linha tracejada em 1,00 m/s indicando o objetivo.
> *Texto alternativo:* Gráfico de velocidade linear ao longo do tempo mostra o NexaBot estabilizando em 1,00 m/s sem carga e caindo para cerca de 0,93 m/s após a aplicação de um torque de carga, sem retornar à referência.

### Laboratório da aula

Laboratório em `projeto_nexabot/aula_01/`:

```bash
.venv/bin/python aula_01/01_ambiente.py
.venv/bin/python aula_01/02_primeira_simulacao.py
.venv/bin/python aula_01/03_malha_aberta_falha.py
.venv/bin/python aula_01/04_v_model.py
```

O primeiro imprime um relatório de prontidão do ambiente, item a item; nenhuma aula deve ser gravada com pendências. O segundo integra a planta (`simulate` de `nexabot/plant.py`, Runge-Kutta de quarta ordem) sob um degrau de $12\,\mathrm{V}$ e produz a primeira resposta do NexaBot. O terceiro parte do regime em $1{,}0\,\mathrm{m/s}$ e aumenta o torque de carga em rampa durante dois segundos, exibindo o erro crescente da malha aberta. O quarto desenha o V-Model em ASCII e mapeia nele as 16 aulas.

### Atividade prática

Mapeie as 16 videoaulas sobre o V-Model: por unidade, identifique se o conteúdo pertence ao ramo descendente (modelo: planta, controlador, propriedades formais, código) ou ao ascendente (verificação: simulação, *model checking*, testes, SIL/HIL), e justifique por que a Unidade 3 concentra verificação formal sem implementação gerada.

### Síntese da aula

- Um CPS acopla dinâmica física contínua e lógica discreta; o erro tem consequência física, não apenas digital.
- O V-Model organiza requisitos e projeto no ramo descendente, verificação no ramo ascendente correspondente.
- O MBD representa cada nível do ramo descendente como modelo executável, adiantando a detecção de defeitos.
- O custo de corrigir um defeito cresce fortemente quanto mais tarde ele é descoberto.
- Um comando fixo (malha aberta) não corrige perturbação de carga: o NexaBot perde cerca de 7,1% de velocidade sob 0,05 N·m e não se recupera sozinho.

### Roteiro da Videoaula 1 — "Sistemas ciberfísicos e o ciclo do design baseado em modelos"

O roteiro falado completo, com narração pronta para gravação, mapa de tempo e comandos literais de terminal, está em `roteiros_20min.md` desta unidade, usando a instalação do ambiente e a queda de velocidade do NexaBot como demonstração de abertura.

### Referências da aula

- LEE, Edward Ashford; SESHIA, Sanjit A. *Introduction to Embedded Systems: A Cyber-Physical Systems Approach*. 2. ed. Cambridge: MIT Press, 2017.
- OGATA, Katsuhiko. *Engenharia de controle moderno*. 5. ed. São Paulo: Pearson, 2011.
- SOMMERVILLE, Ian. *Engenharia de software*. 10. ed. São Paulo: Pearson, 2019.

## Aula 2 — Da equação diferencial ao espaço de estados, com identificação por dados

### Situação-problema: um motor sem datasheet completo

A equipe recebe o motor de tração do NexaBot já montado no chassi, sem datasheet completo — situação comum quando o fornecedor protege parâmetros internos ou o motor já sofreu desgaste. Como obter um modelo confiável sem abrir o motor?

A resposta é a **identificação de sistemas**: aplicar um sinal conhecido (degrau de tensão), medir a resposta (corrente e velocidade angular) e ajustar os parâmetros de um modelo físico até reproduzi-la. Esta aula constrói o modelo em espaço de estados a partir de leis físicas e mostra, com um ensaio sintético mas realista — com ruído de medição e quantização de encoder —, como recuperar os parâmetros verdadeiros sem jamais tê-los diretamente.

### Modelagem por leis de conservação

O eixo de tração combina um circuito elétrico de armadura e um sistema mecânico rotacional, acoplados pela conversão eletromecânica do motor CC de ímã permanente. Pela lei das tensões de Kirchhoff:

$
L\,\frac{di}{dt} = V - Ri - K_e\omega
$

Pela segunda lei de Newton para rotação:

$
J\,\frac{d\omega}{dt} = K_t i - b\omega - \tau_{\text{carga}}
$

Essas duas equações descrevem integralmente a dinâmica do eixo. A corrente $i$ e a velocidade angular $\omega$ carregam toda a informação necessária para prever o comportamento futuro, dado o comando futuro — a definição de **estado** de um sistema dinâmico.

### Espaço de estados

O **estado** é o menor conjunto de variáveis cujo valor presente, somado à entrada futura, determina a evolução futura. Para o NexaBot, $x = [i, \omega]^T$. Na forma padrão $\dot{x} = Ax + Bu$, $y = Cx + Du$, com $u=V$ e $y=\omega$:

$
A = \begin{bmatrix} -R/L & -K_e/L \\ K_t/J & -b/J \end{bmatrix}, \quad
B = \begin{bmatrix} 1/L \\ 0 \end{bmatrix}, \quad
C = \begin{bmatrix} 0 & 1 \end{bmatrix}, \quad
D = \begin{bmatrix} 0 \end{bmatrix}
$

Essa forma é a entrada padrão para análise de polos, discretização, controle por realimentação e verificação de controlabilidade/observabilidade — temas das próximas duas aulas. Obtê-la a partir das equações físicas é tarefa mecânica, feita simbolicamente no laboratório desta aula com SymPy, sem erro de álgebra manual.

Substituindo os valores identificados:

$
A = \begin{bmatrix} -342{,}857 & -12{,}857 \\ 180{,}0 & -0{,}32 \end{bmatrix}, \quad
B = \begin{bmatrix} 285{,}714 \\ 0 \end{bmatrix}
$

Cada entrada é reproduzível por divisão direta: $-R/L=-342{,}857$; $-K_e/L=-12{,}857$; $K_t/J=180{,}0$; $-b/J=-0{,}32$; $1/L=285{,}714$. A ordem de grandeza da primeira linha (centenas) frente à segunda (unidades) já antecipa que a dinâmica elétrica é muito mais rápida que a mecânica — tema da Aula 3.

> **Recurso visual 1 — Derivação simbólica das matrizes A, B, C, D no terminal.** Captura do terminal mostrando a sessão SymPy: as duas equações diferenciais definidas simbolicamente, o comando de linearização e a impressão das matrizes resultantes em formato de matriz.
> *Texto alternativo:* Terminal mostra sessão SymPy derivando simbolicamente as matrizes de espaço de estados do motor do NexaBot a partir das duas equações diferenciais.

### Identificação por mínimos quadrados

Quando os parâmetros não são conhecidos, eles são **identificados** a partir de dados de ensaio: aplica-se um degrau de tensão, mede-se corrente e velocidade com sensores realistas — sensor de corrente com ruído gaussiano e ADC de resolução finita; encoder incremental que mede velocidade por contagem de pulsos, portanto quantizada — e ajustam-se os cinco parâmetros físicos $(R, L, K_e{=}K_t, J, b)$ por **mínimos quadrados não lineares**, minimizando a diferença entre a trajetória simulada e a medida.

Ajustar a trajetória inteira, simulando o modelo completo para cada candidato, em vez de estimar derivadas ponto a ponto, evita amplificar ruído de medição e o mal-condicionamento de um único degrau para separar cinco parâmetros. Um algoritmo de região de confiança (Levenberg-Marquardt) resolve o ajuste.

### Validação com dados retidos

Reproduzir bem o próprio conjunto usado no ajuste não basta: o modelo pode se ajustar ao ruído específico daquele ensaio (sobreajuste). A prática correta reserva um segundo ensaio — independente, nunca usado no ajuste — para validação, comparando saída prevista e medida sem ajuste adicional. A métrica `fit%` expressa essa concordância: $100\%$ é ajuste perfeito, $0\%$ equivale a prever apenas a média do sinal.

### Demonstração e exemplo numérico: ganho estático como verificação cruzada

O ensaio sintético do laboratório reproduz duas imperfeições de bancada: ruído gaussiano e quantização de ADC na corrente; quantização de encoder na velocidade. Mesmo assim, o ajuste recupera os cinco parâmetros com erro pequeno, pois usa a trajetória inteira, não amostras isoladas.

Uma verificação independente, sem repetir o ajuste, é o **ganho estático** $\omega/V$ em regime, sem carga. Fazendo as derivadas nulas e eliminando $i$:

$
\frac{\omega}{V} = \frac{K_t}{Rb + K_tK_e}
$

Substituindo: $Rb = 9{,}6\times10^{-5}$; $K_tK_e = 2{,}025\times10^{-3}$; soma $= 2{,}1210\times10^{-3}$. Logo $\omega/V = 0{,}045/2{,}1210\times10^{-3} = 21{,}2164\,\mathrm{rad/(s\,V)}$. Esse número deve coincidir, dentro da margem de ruído, com a razão medida diretamente no ensaio — verificação barata de bancada, sem refazer o ajuste completo.

> **Recurso visual 2 — Ensaio de degrau: sinais verdadeiros contra sinais medidos.** Dois gráficos empilhados: o superior compara corrente verdadeira (linha suave) e medida (pontos com ruído de ADC); o inferior compara velocidade angular verdadeira (linha suave) e medida (traço em degraus por quantização de encoder).
> *Texto alternativo:* Dois gráficos comparam corrente e velocidade angular verdadeiras com as respectivas medições realistas, exibindo ruído de ADC na corrente e quantização de encoder na velocidade.

> **Recurso visual 3 — Tabela de parâmetros identificados versus verdadeiros.** Tabela ASCII de terminal com colunas parâmetro, unidade, valor verdadeiro, valor identificado e erro percentual, para os cinco parâmetros $R$, $L$, $K_e$, $K_t$, $J$, $b$, com erros pequenos destacados em verde.
> *Texto alternativo:* Tabela em terminal compara os cinco parâmetros identificados do motor do NexaBot com os valores verdadeiros e o erro percentual de cada um.

### Laboratório da aula

Laboratório em `projeto_nexabot/aula_02/`:

```bash
.venv/bin/python aula_02/01_sympy_derivacao.py
.venv/bin/python aula_02/02_estado_vs_transferencia.py
.venv/bin/python aula_02/03_identificacao.py
.venv/bin/python aula_02/04_validacao.py
```

O primeiro deriva simbolicamente $A$, $B$, $C$, $D$ com SymPy. O segundo confere a equivalência entre espaço de estados e função de transferência, inclusive pela resposta ao mesmo degrau. O terceiro gera o ensaio sintético (`gerar_ensaio_degrau` de `nexabot/identificacao.py`), salva `data/ensaio_degrau.csv`, executa o ajuste e imprime a tabela de parâmetros. O quarto repete a identificação, valida o modelo em um ensaio retido com outra amplitude e compara a amostragem de bancada em $0{,}2\,\mathrm{ms}$ com a do controlador em $5\,\mathrm{ms}$, evidenciando a degradação na estimação de $L$ e $b$.

### Atividade prática

Usando o segundo conjunto de dados de `04_validacao.py` (amplitude de degrau distinta), execute a identificação como se fosse o único conjunto disponível. Reporte parâmetro, valor identificado, valor verdadeiro e erro percentual para os cinco parâmetros. Discuta se o erro de $R$ e $L$ é maior ou menor que o de $J$ e $b$, propondo uma explicação ligada à separação de escalas de tempo.

### Síntese da aula

- As leis de Kirchhoff e de Newton para rotação modelam o motor do NexaBot em duas equações diferenciais de primeira ordem.
- O estado $x=[i,\omega]^T$ é a memória mínima do sistema; a forma $\dot{x}=Ax+Bu$ é entrada padrão para as próximas análises.
- Sem parâmetros conhecidos, mínimos quadrados não lineares os recupera de dados de ensaio, ajustando a trajetória inteira.
- Validação exige dados retidos, nunca usados no ajuste; o ganho estático medido é verificação cruzada independente.

### Roteiro da Videoaula 2 — "Da equação diferencial ao espaço de estados, com identificação por dados"

O roteiro falado completo, com narração pronta para gravação, mapa de tempo e comandos literais de terminal, está em `roteiros_20min.md` desta unidade, construindo ao vivo a derivação simbólica e a identificação do motor do NexaBot.

### Referências da aula

- OGATA, Katsuhiko. *Engenharia de controle moderno*. 5. ed. São Paulo: Pearson, 2011.
- NISE, Norman S. *Engenharia de sistemas de controle*. 6. ed. Rio de Janeiro: LTC, 2013.
- NILSSON, James W.; RIEDEL, Susan A. *Circuitos elétricos*. 10. ed. São Paulo: Pearson, 2016.

## Aula 3 — Laplace, função de transferência e resposta em frequência

### Situação-problema: dois polos, dois comportamentos, uma única resposta

Ao observar a resposta do NexaBot a um degrau de tensão, a curva de velocidade angular parece obedecer a uma dinâmica simples, de primeira ordem. A corrente de armadura, porém, sobe muito mais rápido, quase instantânea na escala em que a velocidade evolui. O sistema é de segunda ordem — duas variáveis de estado, dois polos —, mas se comporta, na escala de observação da velocidade, quase como se tivesse apenas um. Por quê?

Esta aula transforma o modelo em espaço de estados em função de transferência via Laplace, calcula os dois polos do NexaBot e mostra que a resposta observada tem explicação exata: a enorme separação entre as duas constantes de tempo.

### A transformada de Laplace como ferramenta de projeto

A **transformada de Laplace** converte uma equação diferencial linear em uma equação algébrica em $s$, substituindo $d/dt$ por multiplicação por $s$ (condições iniciais nulas). Isso transforma o sistema de equações acopladas do motor em equações algébricas, resolúveis por eliminação, produzindo a **função de transferência** $G(s)=Y(s)/U(s)$.

Aplicando às duas equações da Aula 2 (sem torque de carga) e eliminando $I(s)$:

$
G(s) = \frac{\Omega(s)}{V(s)} = \frac{K_t}{LJs^2 + (RJ + Lb)s + (Rb + K_tK_e)}
$

Substituindo os valores: $LJ = 8{,}75\times10^{-7}$; $RJ+Lb \approx 3{,}0028\times10^{-4}$; $Rb+K_tK_e = 2{,}121\times10^{-3}$:

$
G(s) = \frac{0{,}045}{8{,}75\times10^{-7}s^2 + 3{,}0028\times10^{-4}s + 2{,}121\times10^{-3}}
$

### Polos, zeros e constantes de tempo

Os **polos** são as raízes do denominador e determinam a resposta natural: cada polo real negativo $p$ gera um modo $e^{pt}$ com **constante de tempo** $\tau=-1/p$. $G(s)$ não tem zeros finitos, então os dois polos ditam toda a forma da resposta.

Pela fórmula de Bhaskara, com $a=8{,}75\times10^{-7}$, $b=3{,}0028\times10^{-4}$, $c=2{,}121\times10^{-3}$: $\Delta = b^2-4ac = 9{,}017\times10^{-8}-7{,}424\times10^{-9}=8{,}274\times10^{-8}$, $\sqrt{\Delta}\approx2{,}8765\times10^{-4}$. As raízes:

$
s_1 = \frac{-3{,}0028\times10^{-4} + 2{,}8765\times10^{-4}}{1{,}75\times10^{-6}} \approx -7{,}215\,\mathrm{rad/s}, \quad
s_2 \approx -335{,}96\,\mathrm{rad/s}
$

As constantes de tempo modais exatas são $\tau_1 = 1/335{,}96 \approx 2{,}9765\,\mathrm{ms}$ e $\tau_2 = 1/7{,}215 \approx 138{,}598\,\mathrm{ms}$. As contas rápidas desacopladas $L/R\approx2{,}9167\,\mathrm{ms}$ e $JR/(K_tK_e)\approx148{,}148\,\mathrm{ms}$ aproximam, respectivamente, os modos elétrico e mecânico; a diferença decorre do acoplamento eletromecânico mantido no modelo de segunda ordem.

> **Recurso visual 1 — Mapa de polos no plano complexo s.** Plano cartesiano com eixo real horizontal e imaginário vertical; dois pontos marcados sobre o eixo real negativo, em $-7{,}215$ e $-335{,}96$, com setas indicando a distância à origem e a região de estabilidade (semiplano esquerdo) sombreada.
> *Texto alternativo:* Mapa de polos no plano complexo mostra os dois polos reais negativos do NexaBot, em -7,215 e -335,96 rad/s, ambos no semiplano esquerdo de estabilidade.

### Separação de escalas de tempo

A razão exata entre os polos — e, inversamente, entre as constantes de tempo modais — é $335{,}96/7{,}215\approx46{,}6$, revelando separação de quase duas ordens de grandeza. Isso explica a situação-problema: a corrente (modo rápido) atinge o novo regime em poucos milissegundos, enquanto a velocidade (modo lento) ainda está subindo — por isso a curva de velocidade parece, na escala observada, uma resposta de primeira ordem. Essa separação é o argumento numérico que justificará, na Aula 7, o período de amostragem $T_s=5\,\mathrm{ms}$.

> **Recurso visual 2 — Corrente e velocidade em escalas de tempo distintas.** Dois gráficos sobrepostos com o mesmo eixo horizontal de tempo (0 a 0,5 s): a corrente sobe e satura em menos de 15 ms, enquanto a velocidade angular ainda está subindo suavemente até cerca de 0,5 s, evidenciando a separação de escalas.
> *Texto alternativo:* Gráfico compara a corrente do motor, que se estabiliza em poucos milissegundos, com a velocidade angular, que continua subindo por centenas de milissegundos, evidenciando a separação entre as constantes de tempo elétrica e mecânica.

### Diagrama de Bode, margens e largura de banda

O **diagrama de Bode** representa a resposta em frequência de $G(j\omega)$ — magnitude e fase em regime senoidal — e permite ler a **margem de ganho** (quanto o ganho de malha pode crescer antes da instabilidade) e a **margem de fase** (quanto atraso de fase adicional a malha tolera). A **largura de banda** indica a velocidade máxima de variação de referência que o sistema acompanha sem atenuação excessiva.

Para os dois polos reais bem separados do NexaBot, a magnitude exibe dois pontos de quebra: em $\omega\approx7{,}215\,\mathrm{rad/s}$ (inclinação passa a $-20\,\mathrm{dB/década}$) e em $\omega\approx335{,}96\,\mathrm{rad/s}$ (inclinação passa a $-40\,\mathrm{dB/década}$). Entre os dois, o sistema se comporta como se fosse de primeira ordem — a mesma observação da situação-problema, agora no domínio da frequência.

> **Recurso visual 3 — Diagrama de Bode do NexaBot em malha aberta.** Dois gráficos empilhados em escala logarítmica de frequência: magnitude em dB com dois pontos de quebra em 7,215 e 335,96 rad/s; fase em graus decaindo de 0° a -180°.
> *Texto alternativo:* Diagrama de Bode de magnitude e fase do NexaBot em malha aberta, com dois pontos de quebra correspondentes aos polos elétrico e mecânico.

### Pausa para reflexão

O polo elétrico é cerca de 46 vezes mais rápido que o mecânico. Muitos projetos simplificados desprezam a dinâmica elétrica, tratando o motor como sistema de primeira ordem — **redução de ordem de modelo** praticada na indústria.

Reflita: é legítimo desprezar o polo elétrico aqui? Considere: (i) o efeito sobre a precisão do modelo em frequências próximas a $335{,}96\,\mathrm{rad/s}$; (ii) o efeito sobre a análise da corrente, ligada ao limite $i_{max}=12\,\mathrm{A}$ (REQ-PLANT-002); (iii) se a resposta mudaria para um controlador que amostra a $T_s=5\,\mathrm{ms}$, já próximo da constante de tempo elétrica de $2{,}92\,\mathrm{ms}$. Não há resposta universal — a legitimidade depende do que o modelo reduzido precisa responder.

### Atividade prática

Usando `python-control`, obtenha o diagrama de Bode em malha aberta e determine as margens de ganho e de fase. Em seguida, reproduza a varredura de $K_p$ de $0{,}5$ a $50$ de `04_estabilidade.py` e explique por que nenhum ganho proporcional positivo finito leva esta planta contínua de segunda ordem à instabilidade. Registre a perda de margem de fase e o crescimento do sobressinal; compare esse resultado com o ganho crítico que surgirá apenas na malha discreta da Aula 6.

### Laboratório da aula

Laboratório em `projeto_nexabot/aula_03/`:

```bash
.venv/bin/python aula_03/01_laplace_sympy.py
.venv/bin/python aula_03/02_polos_zeros.py
.venv/bin/python aula_03/03_bode.py
.venv/bin/python aula_03/04_estabilidade.py
```

O primeiro aplica Laplace com o módulo de transformadas do SymPy, chegando simbolicamente a $G(s)$. O segundo calcula os polos com `python-control` (`transfer_function` de `nexabot/plant.py`), imprime a tabela de polos e constantes de tempo e traça o Recurso visual 2. O terceiro traça o Bode do Recurso visual 3 e imprime as margens. O quarto varre $K_p$ e confirma por Routh–Hurwitz que a malha contínua permanece estável, embora o desempenho se degrade.

### Síntese da aula

- Laplace converte as duas equações acopladas do motor em uma função de transferência algébrica $G(s)$.
- $G(s)$ tem dois polos reais, $-335{,}96$ e $-7{,}215\,\mathrm{rad/s}$, com constantes de tempo modais de $2{,}9765\,\mathrm{ms}$ e $138{,}598\,\mathrm{ms}$; $L/R$ e $JR/(K_tK_e)$ são aproximações desacopladas.
- A separação de quase duas ordens de grandeza explica por que a velocidade parece de primeira ordem, mesmo o sistema sendo de segunda.
- O Bode expõe essa separação como dois pontos de quebra e fornece margens de ganho e de fase, retomadas no projeto de controlador.
- Desprezar o polo rápido custa precisão exatamente onde a corrente — ligada a um requisito de segurança — é relevante.

### Roteiro da Videoaula 3 — "Laplace, função de transferência e resposta em frequência"

O roteiro falado completo, com narração pronta para gravação, mapa de tempo e comandos literais de terminal, está em `roteiros_20min.md` desta unidade, derivando ao vivo $G(s)$ e calculando os dois polos do NexaBot.

### Referências da aula

- OGATA, Katsuhiko. *Engenharia de controle moderno*. 5. ed. São Paulo: Pearson, 2011.
- FRANKLIN, Gene F.; POWELL, J. David; EMAMI-NAEINI, Abbas. *Sistemas de controle para engenharia*. 6. ed. Porto Alegre: Bookman, 2013.
- ÅSTRÖM, Karl Johan; MURRAY, Richard M. *Feedback Systems: An Introduction for Scientists and Engineers*. 2. ed. Princeton: Princeton University Press, 2021.

## Aula 4 — Controlabilidade, observabilidade e realimentação de estados

### Situação-problema: um projeto matematicamente correto e fisicamente impossível

Um engenheiro júnior aplica alocação de polos por realimentação de estados ao NexaBot, escolhendo polos de malha fechada bem mais rápidos que os naturais — operação válida sempre que o sistema for controlável, como esta aula mostrará. A simulação confirma: a velocidade atinge a referência muito mais rápido. Ao inspecionar o comando de tensão exigido, porém, o valor ultrapassa os $24\,\mathrm{V}$ do driver, em ordens de grandeza.

O projeto está matematicamente correto e fisicamente impossível. Esta aula constrói controlabilidade, observabilidade e realimentação de estados, mostrando onde esse tipo de projeto encontra o limite do atuador.

### Controlabilidade

Um sistema é **controlável** quando alguma entrada conduz o estado de qualquer condição inicial a qualquer condição final em tempo finito. Verifica-se pelo posto da **matriz de controlabilidade** $\mathcal{C}=[B\ AB]$: controlável se e somente se $\mathcal{C}$ tem posto completo.

Com $B=[285{,}714;0]^T$, calculando $AB$: primeira componente $-342{,}857\times285{,}714=-97\,959{,}2$; segunda $180{,}0\times285{,}714=51\,428{,}6$. A matriz $\mathcal{C}=\begin{bmatrix}285{,}714 & -97\,959{,}2\\0 & 51\,428{,}6\end{bmatrix}$ tem determinante $\approx1{,}469\times10^{7}$, não nulo — posto 2, completo. O NexaBot é controlável: existe, em princípio, tensão capaz de levar corrente e velocidade a qualquer par de valores — condição necessária, mas não suficiente, para viabilidade de um projeto.

### Observabilidade

Um sistema é **observável** quando o estado pode ser reconstruído a partir da saída medida. Verifica-se pelo posto de $\mathcal{O}=[C;\ CA]$. Com $C=[0\ \ 1]$, $CA=[180{,}0,\ -0{,}32]$. A matriz $\mathcal{O}=\begin{bmatrix}0&1\\180{,}0&-0{,}32\end{bmatrix}$ tem determinante $-180{,}0$, não nulo — posto 2, completo. A única medição (velocidade $\omega$) basta para reconstruir também a corrente $i$, sustentando um **observador de estados**, aprofundado na Unidade 2.

> **Recurso visual 1 — Matrizes de controlabilidade e observabilidade no terminal.** Captura de terminal exibindo, em tabela ASCII, as matrizes, seus determinantes e o posto calculado, com "sistema controlável" e "sistema observável" destacados em verde.
> *Texto alternativo:* Terminal exibe as matrizes de controlabilidade e observabilidade do NexaBot com seus determinantes e confirmação de posto completo para ambas.

### Alocação de polos por realimentação de estados

Confirmada a controlabilidade, $u=-Kx+\bar{N}r$ posiciona os polos de malha fechada em qualquer localização, escolhendo $K=[k_1\ k_2]$ tal que $A-BK$ tenha os autovalores desejados. O termo $\bar{N}r$ é um ganho de referência calculado para erro nulo em regime. O compromisso desempenho-esforço aparece direto: polos mais rápidos exigem, em geral, $K$ maior, e $K$ maior multiplica o erro inicial em comando de tensão proporcionalmente maior — sobretudo no instante de um degrau de referência, quando o erro é máximo.

### Demonstração e exemplo numérico: alocando polos até estourar os 24 V

Com $r=400\,\mathrm{rad/s}$ ($1{,}00\,\mathrm{m/s}$) partindo do repouso, o comando inicial é dominado pelo termo $\bar{N}r$, já que $-Kx$ é nulo em $x=0$. A tabela aloca polos duplos progressivamente mais rápidos e reporta $u(0)=\bar{N}\times400$:

| Polo duplo (rad/s) | $k_1$ | $k_2$ | $\bar{N}$ | $u(0)$ (V) |
| --- | --- | --- | --- | --- |
| $-10$ | $-1{,}131$ | $-0{,}043$ | $0{,}0019$ | $0{,}78$ |
| $-30$ | $-0{,}991$ | $-0{,}028$ | $0{,}0175$ | $7{,}00$ |
| $-50$ | $-0{,}851$ | $0{,}003$ | $0{,}0486$ | $19{,}44$ |
| $-60$ | $-0{,}781$ | $0{,}024$ | $0{,}0700$ | $28{,}00$ |
| $-100$ | $-0{,}501$ | $0{,}148$ | $0{,}1944$ | $77{,}78$ |

O limite de $24\,\mathrm{V}$ é ultrapassado já entre $-50$ e $-60\,\mathrm{rad/s}$ — apenas 7 a 8 vezes mais rápido que o polo mecânico natural ($-7{,}215\,\mathrm{rad/s}$), longe da rapidez do polo elétrico. Um projeto que ignore esse limite é matematicamente correto e operacionalmente inútil: o driver satura, o comando real difere do calculado, e a resposta observada não corresponde à prevista. **O limite físico do atuador invalida projetos que se apoiam apenas em critérios matemáticos de desempenho.**

O regulador linear quadrático (LQR) enfrenta o mesmo compromisso por outro caminho: em vez de escolher polos diretamente, o projetista escolhe as matrizes de peso $Q$ (penalidade sobre desvio de estado) e $R$ (penalidade sobre esforço de controle), e o algoritmo calcula o $K$ ótimo. Aumentar $Q$ frente a $R$ desloca os polos resultantes para mais rápido — a mesma família de soluções, obtida por otimização, com a vantagem de ponderar cada estado individualmente (por exemplo, penalizar mais a corrente que a velocidade, se o limite térmico for a preocupação).

> **Recurso visual 2 — Tensão de pico exigida versus velocidade do polo de malha fechada.** Gráfico com o eixo horizontal representando o módulo do polo duplo desejado (10 a 100 rad/s) e o vertical o comando de tensão inicial (V), com linha tracejada em 24 V; a curva cruza essa linha entre 50 e 60 rad/s.
> *Texto alternativo:* Gráfico mostra o crescimento do comando de tensão inicial conforme o polo de malha fechada desejado se torna mais rápido, cruzando o limite de 24 V do driver entre 50 e 60 rad/s.

> **Recurso visual 3 — Varredura de Q e R no LQR: tensão de pico versus tempo de acomodação.** Gráfico de dispersão com o eixo horizontal representando o tempo de acomodação (s) e o vertical o pico de tensão exigido (V) para diferentes pares $(Q,R)$, com uma região sombreada acima de 24 V marcando combinações inviáveis.
> *Texto alternativo:* Gráfico de dispersão relaciona tempo de acomodação e pico de tensão exigido para diferentes pares de matrizes de peso do LQR, com a região acima de 24 V marcada como inviável.

### Laboratório da aula

Laboratório em `projeto_nexabot/aula_04/`:

```bash
.venv/bin/python aula_04/01_ctrb_obsv.py
.venv/bin/python aula_04/02_alocacao_polos.py
.venv/bin/python aula_04/03_lqr.py
.venv/bin/python aula_04/04_observador.py
```

O primeiro monta as matrizes de controlabilidade e observabilidade, calculando determinantes e postos. O segundo compara alocações moderada e agressiva com o limite real de $24\,\mathrm{V}$. O terceiro varre 16 pares $(Q,R)$ do LQR, tabulando pico de tensão contra tempo de acomodação; todas as combinações testadas ultrapassam o limite, resultado que precisa ser interpretado, não escondido. O quarto constrói um observador de Luenberger para estimar a corrente a partir da velocidade medida e confere a convergência do erro.

### Atividade prática

Usando `03_lqr.py`, mantenha $R=0{,}1$ e compare ao menos três valores da penalidade sobre a velocidade em $Q$. Para cada par, registre $K$, pico de tensão ideal e tempo de acomodação. Como nenhuma combinação da grade original respeita $24\,\mathrm{V}$ para o degrau de $400\,\mathrm{rad/s}$, identifique a de menor pico e proponha uma reformulação verificável: limitar a rampa da referência, ampliar $R$, incluir a saturação no projeto ou reduzir a exigência de desempenho.

### Transição para a Unidade 2

Você dispõe do modelo completo do NexaBot — identificado e validado — e de um primeiro controlador em espaço de estados, com limite de implementabilidade já quantificado. Falta a estrutura mais usada na indústria, o **PID**, com sintonia consagrada e tratamento de saturação e *anti-windup*, e levar o controlador ao domínio discreto em que o microcontrolador do NexaBot efetivamente vive.

A Unidade 2 fecha essas lacunas: projeta e sintoniza um PID discreto, escolhe o período de amostragem a partir das constantes de tempo obtidas aqui, e acopla planta e controlador por co-simulação FMI, medindo pela primeira vez o erro de acoplamento entre dois simuladores independentes.

### Síntese da aula

- Controlabilidade ($[B\ AB]$ de posto completo) garante existência de entrada capaz de levar o estado a qualquer valor; observabilidade ($[C;\ CA]$ de posto completo) garante reconstrução do estado pela saída.
- O NexaBot é controlável e observável — ambas as matrizes têm posto 2.
- $u=-Kx+\bar{N}r$ aloca polos de malha fechada em qualquer posição, mas ganhos maiores exigem comandos proporcionalmente maiores.
- Polos apenas 7 a 8 vezes mais rápidos que o natural já exigem tensão acima de 24 V — projeto correto, mas fisicamente inviável.
- O LQR enfrenta o mesmo compromisso via $Q$ e $R$, produzindo a mesma família de soluções por otimização.

### Roteiro da Videoaula 4 — "Controlabilidade, observabilidade e realimentação de estados"

O roteiro falado completo, com narração pronta para gravação, mapa de tempo e comandos literais de terminal, está em `roteiros_20min.md` desta unidade, encerrando a Unidade 1 com a demonstração do comando estourando o limite do driver e conectando-a à Unidade 2.

### Referências da aula

- OGATA, Katsuhiko. *Engenharia de controle moderno*. 5. ed. São Paulo: Pearson, 2011.
- FRANKLIN, Gene F.; POWELL, J. David; EMAMI-NAEINI, Abbas. *Sistemas de controle para engenharia*. 6. ed. Porto Alegre: Bookman, 2013.
- ÅSTRÖM, Karl Johan; MURRAY, Richard M. *Feedback Systems: An Introduction for Scientists and Engineers*. 2. ed. Princeton: Princeton University Press, 2021.

## Atividades, síntese e material complementar

### Quiz não avaliativo

**Questão 1.** Um comando de tensão fixo é aplicado ao motor do NexaBot, calculado para sustentar $1{,}00\,\mathrm{m/s}$ sem carga. Ao aplicar torque de carga de $0{,}05\,\mathrm{N\,m}$, a velocidade cai para cerca de $0{,}93\,\mathrm{m/s}$ e permanece nesse valor. Assinale a alternativa que explica corretamente por que isso ocorre.

a. O motor sofreu falha elétrica permanente ao receber a carga adicional.
b. O modelo em espaço de estados deixou de ser válido no instante em que a carga foi aplicada.
*c. O comando em malha aberta foi calculado para uma condição específica (sem carga) e não possui mecanismo de realimentação capaz de detectar e corrigir a mudança de condição física.
d. O torque de 0,05 N·m excede a capacidade máxima do motor, causando saturação permanente.
e. A queda de velocidade é um artefato do modelo de simulação e não ocorreria em um motor real.

*Feedback conceitual:* a alternativa correta é a "c". Um comando fixo é calculado uma única vez, sem comparação entre saída real e objetivo. Ao mudar a condição física, a relação tensão-velocidade em regime muda, e sem realimentação o erro (cerca de 7,1% no exemplo da aula) permanece indefinidamente. As demais alternativas descrevem falhas ou artefatos que não correspondem ao fenômeno: motor e modelo continuam corretos; a estratégia de controle é que é incapaz de reagir.

**Questão 2.** O NexaBot tem dois polos, $-335{,}96\,\mathrm{rad/s}$ (modo rápido) e $-7{,}215\,\mathrm{rad/s}$ (modo lento), com constantes de tempo modais de aproximadamente $2{,}98\,\mathrm{ms}$ e $138{,}6\,\mathrm{ms}$. Assinale a alternativa que interpreta corretamente essa separação.

a. Os dois polos indicam que o modelo está incorreto, pois um sistema real deveria ter apenas um polo dominante.
b. A constante de tempo do modo rápido, de aproximadamente 2,98 ms, significa que a corrente nunca varia durante a operação.
*c. A dinâmica elétrica evolui quase 47 vezes mais rápido que a mecânica, de modo que, na escala de tempo em que a velocidade é observada, o sistema se aproxima de um comportamento de primeira ordem.
d. A separação indica que o modelo pode ser reduzido a um único polo em qualquer análise, sem qualquer perda de informação.
e. Quanto maior a separação, menor é a corrente máxima que o motor suporta.

*Feedback conceitual:* a alternativa correta é a "c". A razão entre os polos ($\approx46{,}6$) mostra que o modo elétrico decai muito antes de o mecânico se estabilizar, aproximando a resposta de velocidade de uma resposta de primeira ordem. Isso é uma observação sobre a forma da resposta, não prova de modelo incorreto (a), nem justificativa universal para descartar o polo elétrico sem perda (d) — como discutido na Pausa para reflexão da Aula 3, a redução tem custo quando a corrente é relevante.

### Atividade Avaliativa Individual (AAI)

**Enunciado:** um engenheiro júnior projeta uma realimentação de estados para o NexaBot, alocando polos de malha fechada em $-100\,\mathrm{rad/s}$ (duplo). Ao simular o comando exigido para um degrau de $400\,\mathrm{rad/s}$ partindo do repouso, o pico é de aproximadamente $77{,}8\,\mathrm{V}$, acima dos $24\,\mathrm{V}$ do driver. Considerando os conceitos da Unidade 1, elabore uma resposta dissertativa (300 a 500 palavras) que:

a. explique, em termos do modelo em espaço de estados e da relação entre $K$ e $\bar{N}$, por que um polo de malha fechada mais rápido produz comando inicial maior;
b. avalie se controlabilidade garante, por si só, que qualquer objetivo de desempenho seja implementável, distinguindo existência matemática de viabilidade física;
c. proponha uma estratégia alternativa que respeite o limite de $24\,\mathrm{V}$, considerando outra escolha de polos e o uso do LQR com $Q$ e $R$ ajustados;
d. explique por que as escalas de tempo do modo rápido ($2{,}98\,\mathrm{ms}$) e do modo lento ($138{,}6\,\mathrm{ms}$) são relevantes para julgar se um tempo de acomodação é fisicamente razoável antes de simular o comando.

**Resposta esperada (modelo de resposta):**

(a) O comando é $u=-Kx+\bar{N}r$. Partindo de $x(0)=0$, $-Kx$ é nulo, e o comando inicial é $\bar{N}r$. Um polo mais rápido exige $K$ maior em módulo; como $\bar{N}$ é calculado para compensar $K$ e garantir erro nulo em regime, $\bar{N}$ também cresce. O comando inicial cresce proporcionalmente à velocidade de resposta desejada — a tabela da aula ilustra isso, de $0{,}78\,\mathrm{V}$ (polo em $-10$) a $77{,}78\,\mathrm{V}$ (polo em $-100$).

(b) Controlabilidade garante apenas que existe, matematicamente, alguma entrada capaz de levar o estado à condição desejada, sem impor limite sobre sua magnitude. O driver satura em $24\,\mathrm{V}$: uma solução que exija $77{,}8\,\mathrm{V}$ não pode ser aplicada, e o comando saturado produz resposta diferente da prevista. Controlabilidade é condição necessária, não suficiente, para implementabilidade.

(c) Estratégias aceitáveis: polos mais lentos (entre $-30$ e $-50\,\mathrm{rad/s}$, onde a tensão de pico ainda cabe em $24\,\mathrm{V}$); ou LQR com $R$ maior e/ou $Q$ menos agressivo sobre a velocidade, obtendo por otimização um $K$ compatível com o atuador, possivelmente com tempo de acomodação maior como contrapartida — reconhecendo o compromisso entre velocidade e esforço de controle.

(d) A constante modal dominante ($138{,}6\,\mathrm{ms}$) estabelece a escala natural da resposta lenta; exigir acomodação ordens de grandeza menor demanda esforço desproporcional. A constante do modo rápido ($2{,}98\,\mathrm{ms}$) estabelece a outra escala relevante: exigir resposta comparável ou mais rápida tenta comandar uma dinâmica que a parte elétrica ainda não concluiu. Comparar o objetivo a essas duas constantes antes de simular é uma verificação de sanidade barata.

Respostas que apenas repitam valores numéricos sem explicar a relação causal entre polo, $K$, $\bar{N}$ e tensão, ou que concluam que o LQR "resolve" o problema sem reconhecer o compromisso desempenho-esforço, devem ser consideradas incompletas.

### Síntese da unidade

- Um CPS acopla dinâmica física contínua e lógica discreta; o MBD adianta a verificação para antes da implementação, no espírito do V-Model.
- Um comando fixo (malha aberta) não corrige perturbação de carga: o NexaBot perde cerca de 7,1% de velocidade sob 0,05 N·m e permanece nesse erro.
- Kirchhoff e Newton para rotação modelam o eixo em espaço de estados, com $x=[i,\omega]^T$ e matrizes $A$, $B$, $C$, $D$ obtidas diretamente dos parâmetros físicos.
- Sem parâmetros conhecidos, mínimos quadrados não lineares os recupera de dados com ruído e quantização, validando contra um conjunto retido.
- Laplace converte o modelo em $G(s)$, cujos dois polos ($-335{,}96$ e $-7{,}215\,\mathrm{rad/s}$) revelam separação de quase duas ordens de grandeza entre as dinâmicas elétrica e mecânica.
- O Bode expõe essa separação como dois pontos de quebra e fornece margens de ganho e fase, retomadas no projeto de controlador.
- O NexaBot é controlável e observável (posto 2 em ambas as matrizes), condição necessária, mas não suficiente, para viabilidade de controle.
- Alocação de polos e LQR enfrentam o mesmo compromisso desempenho-esforço; ignorar o limite de $24\,\mathrm{V}$ produz projetos corretos e inviáveis.

### Material complementar

#### Direto da Fonte

**Texto provocativo:** Você já modelou o motor do NexaBot a partir de duas leis físicas conhecidas. Mas por que a forma em espaço de estados se tornou o padrão da engenharia de controle moderna, em vez de trabalhar diretamente com as equações originais? Este capítulo mostra a origem histórica dessa escolha, conectando-a às ferramentas de análise que você acabou de usar.

**Referência:** OGATA, Katsuhiko. *Engenharia de controle moderno*. 5. ed. São Paulo: Pearson, 2011. Capítulo 3 — "Modelagem matemática de sistemas dinâmicos".

**Link de acesso:** disponível na Biblioteca Virtual da instituição.

**Aula indicada:** Aula 2, após "Espaço de estados".

#### Para Mergulhar no Assunto

**Texto provocativo:** Um sistema ciberfísico mal modelado não é um problema apenas acadêmico. O relatório oficial sobre o acidente fatal do Boeing 737 MAX detalha como um modelo incompleto do comportamento aerodinâmico, combinado a uma lógica que confiava em um único sensor, produziu decisões automáticas incorretas com consequências irreversíveis — a versão mais grave possível do argumento desta unidade.

**Referência:** ESTADOS UNIDOS. Federal Aviation Administration. *Boeing 737 MAX Flight Control System*: Joint Authorities Technical Review. Washington, D.C., 2019. Relatório técnico.

**Link de acesso:** <https://www.faa.gov/sites/faa.gov/files/2022-08/Final_JATR_Submittal_to_FAA_Oct_2019.pdf>. Acesso em: 29 ago. 2026.

**Aula indicada:** Aula 1, após "Por que o erro em CPS tem consequência física".

#### Podcast

**Texto provocativo:** Antes de projetar qualquer controlador, é preciso confiar no modelo da planta. Esta palestra, sobre identificação de sistemas aplicada a robótica industrial, mostra como equipes reais recuperam parâmetros físicos de motores a partir de dados ruidosos — exatamente o problema resolvido nesta unidade com o motor do NexaBot, visto pela perspectiva de quem faz isso em escala industrial.

**Referência:** MURRAY, Richard M. *System Identification for Control: From Data to Models*. [S. l.: s. n.], 2021. 1 vídeo (38 min). Publicado pelo canal Caltech CDS Seminars.

**Link de acesso:** <https://www.youtube.com/watch?v=k6xhZQ2xJfE>. Acesso em: 30 jul. 2026.

**Trecho obrigatório:** vídeo completo (38 min), dentro do limite institucional de curadoria.

**Aula indicada:** Aula 2, após "Identificação por mínimos quadrados".

#### Artigo científico

**Texto provocativo:** O conceito de espaço de estados, hoje ferramenta padrão de engenharia, nasceu de um artigo que uniu controle ótimo e filtragem sob uma única estrutura matemática. Ler o texto que formalizou a noção de estado ajuda a entender por que essa representação — e não a função de transferência isolada — é o alicerce de tudo o que a disciplina constrói a partir daqui.

**Referência:** KALMAN, Rudolf E. On the general theory of control systems. *IRE Transactions on Automatic Control*, v. 4, n. 3, p. 110, dez. 1959. DOI: 10.1109/TAC.1959.1104873.

**Link de acesso:** <https://doi.org/10.1109/TAC.1959.1104873>. Acesso em: 30 jul. 2026.

**Aula indicada:** Aula 4, após "Controlabilidade".

## Referências da unidade

ÅSTRÖM, Karl Johan; MURRAY, Richard M. *Feedback Systems: An Introduction for Scientists and Engineers*. 2. ed. Princeton: Princeton University Press, 2021.

ESTADOS UNIDOS. Federal Aviation Administration. *Boeing 737 MAX Flight Control System*: Joint Authorities Technical Review. Washington, D.C., 2019.

FRANKLIN, Gene F.; POWELL, J. David; EMAMI-NAEINI, Abbas. *Sistemas de controle para engenharia*. 6. ed. Porto Alegre: Bookman, 2013.

KALMAN, Rudolf E. On the general theory of control systems. *IRE Transactions on Automatic Control*, v. 4, n. 3, p. 110, dez. 1959. DOI: 10.1109/TAC.1959.1104873.

LEE, Edward Ashford; SESHIA, Sanjit A. *Introduction to Embedded Systems: A Cyber-Physical Systems Approach*. 2. ed. Cambridge: MIT Press, 2017.

MURRAY, Richard M. *System Identification for Control: From Data to Models*. [S. l.: s. n.], 2021. 1 vídeo (38 min). Publicado pelo canal Caltech CDS Seminars. Disponível em: <https://www.youtube.com/watch?v=k6xhZQ2xJfE>. Acesso em: 30 jul. 2026.

NILSSON, James W.; RIEDEL, Susan A. *Circuitos elétricos*. 10. ed. São Paulo: Pearson, 2016.

NISE, Norman S. *Engenharia de sistemas de controle*. 6. ed. Rio de Janeiro: LTC, 2013.

OGATA, Katsuhiko. *Engenharia de controle moderno*. 5. ed. São Paulo: Pearson, 2011.

SOMMERVILLE, Ian. *Engenharia de software*. 10. ed. São Paulo: Pearson, 2019.
