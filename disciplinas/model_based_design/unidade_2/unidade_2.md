# Unidade 2 — Modelagem e simulação de sistemas de controle

Disciplina: Model-Based Design for Cyber-Physical Systems
Professor-conteudista: Afonso Cesar Lelis Brandão

## Relação da unidade com a atuação profissional

A Unidade 1 devolveu um modelo do NexaBot validado contra dados de ensaio. Um modelo, por si só, não move um AGV: é preciso decidir como a tensão do motor reage ao erro entre velocidade desejada e medida. Essa decisão raramente segue a realimentação de estados da Aula 4, que exige sensores de corrente e de velocidade simultâneos. Na indústria, a estrutura dominante é o PID de saída única: robusto, barato de instrumentar e bem compreendido por quem mantém o sistema em campo — não porque seja teoricamente ótimo, mas porque funciona com o sensoriamento que a maioria dos equipamentos realmente tem.

Esta unidade também expõe uma tensão inevitável: todo modelo contínuo será executado por um microcontrolador que amostra, calcula e atua em instantes discretos. A escolha do período de amostragem não é detalhe de implementação — é decisão de projeto capaz de transformar uma malha estável em papel em uma malha instável em silício.

Por fim, sistemas ciberfísicos raramente nascem de uma única ferramenta: a planta pode ser modelada em uma ferramenta e o controlador em outra, e ambos precisam conversar antes de existir hardware físico para integrar. O padrão FMI, estudado ao final da unidade, é o mecanismo aberto mais adotado pela indústria automotiva e aeroespacial para essa integração, desde que o erro do acoplamento seja conhecido e controlado.

Ao final, o estudante terá exercitado o ciclo que separa um modelo de um controlador em produção: fechar a malha, sintonizá-la, discretizá-la sem perder margem e integrá-la a outros subsistemas com erro quantificado.

## O que você verá nesta unidade

A Aula 5 formaliza malha aberta contra malha fechada com as funções de sensibilidade $S$ e complementar $T$. A Aula 6 projeta um PID completo para o NexaBot, com sintonia por Ziegler-Nichols, métricas objetivas e o tratamento de saturação e *windup*. A Aula 7 discretiza esse controlador, fixa o contrato numérico do `DiscretePID` que reaparece em C na Unidade 4, e mostra por que o período de amostragem é uma decisão de projeto. A Aula 8 acopla planta e controlador por co-simulação FMI 3.0, medindo o erro que esse acoplamento introduz.

Ao final, o estudante projeta, sintoniza e discretiza um controlador, justifica numericamente o $T_s$ escolhido, trata saturação e *windup*, e mede o erro de uma co-simulação — preparando a Unidade 3, em que esse comportamento será verificado exaustivamente, não apenas simulado.

## Aula 5 — Malha aberta, malha fechada e álgebra de diagramas de blocos

### Situação-problema: a carga muda, e a malha aberta erra de novo

A Aula 1 mostrou o NexaBot perdendo velocidade sob carga em malha aberta. Uma primeira "correção" somou um deslocamento fixo à tensão, calibrado para a carga média observada — e falhou assim que o robô carregou uma caixa mais pesada, porque o deslocamento fixo não sabe que a carga mudou. O problema não é o valor do deslocamento: é a ausência de realimentação. Esta aula formaliza por que fechar a malha resolve o problema de forma estrutural.

### Realimentação negativa e a malha fechada

Na realimentação negativa, a tensão deixa de ser fixa e passa a ser calculada por um controlador $C(s)$ a partir do erro $e(s)=R(s)-Y(s)$. Com $L(s)=C(s)G(s)$, a saída em função da referência e de um distúrbio de carga $T_l(s)$ é:

$
Y(s) = \frac{L(s)}{1+L(s)} R(s) - \frac{G(s)}{1+L(s)} T_l(s)
$

Os dois termos compartilham o denominador $1+L(s)$: a mesma realimentação que faz o sistema seguir a referência determina também sua rejeição a distúrbios. $L(s)$ é chamado **ganho de malha aberta**: descreve o que aconteceria se o laço fosse cortado logo após o somador do erro, e é a partir dele que $S(s)$ e $T(s)$, definidos a seguir, são construídos. Em `python-control`, essa álgebra deixa de ser manuscrita: `ct.series(C, G)` monta $L(s)$, e `ct.feedback(L, 1)` monta $T(s)=L/(1+L)$ diretamente. O resultado coincide, ponto a ponto, com a redução simbólica feita em SymPy na Aula 3 — comparação que abre o laboratório desta aula.

### Funções de sensibilidade $S$ e complementar $T$

A **sensibilidade** $S(s)=1/(1+L(s))$ multiplica o efeito de um distúrbio e do ruído de medição; a **complementar** $T(s)=L(s)/(1+L(s))$ multiplica o efeito da referência. Por definição, $S(s)+T(s)=1$. Não é possível tornar $S$ e $T$ pequenos na mesma frequência: reduzir $S$ em baixa frequência exige $T\approx1$ nessa faixa, desejável para rastreamento, mas o mesmo $T\approx1$ em alta frequência amplifica ruído de medição. Para o NexaBot, isso é concreto: o encoder de quadratura introduz ruído de quantização em frequências relativamente altas (Aula 7), e é ali que $T(s)\approx1$ transmitiria esse ruído quase sem atenuação para a tensão de comando. Projetar $C(s)$ é decidir até que frequência vale a pena perseguir rastreamento agressivo.

### Erro em regime permanente e tipo de sistema

O número de integradores puros em $L(s)$ define o **tipo** do sistema. $G(s)$ do NexaBot não tem polo na origem: é tipo 0. Com $C(s)$ também sem integrador, $L(s)$ segue tipo 0 e o erro de regime a um distúrbio constante é finito e não nulo. Basta um polo na origem em $C(s)$ — a ação integral, formalizada na Aula 6 — para tornar $L(s)$ tipo 1: $S(0)\to0$ e o erro de regime a qualquer distúrbio constante tende a zero, **independentemente dos valores dos ganhos**, desde que a malha seja estável. O mesmo raciocínio vale para o rastreamento de uma referência em degrau: um sistema tipo 0 converge a um valor final abaixo do pedido, enquanto um sistema tipo 1 rastreia sem erro de regime — a distinção entre "chegar perto" e "chegar exatamente" depende de quantos integradores existem no laço, não de quão bem os ganhos foram escolhidos.

### Exemplo numérico: a queda de velocidade em malha aberta

Com $V=18{,}85\,\mathrm{V}$ fixos, o NexaBot sustenta $400\,\mathrm{rad/s}$ ($1{,}000\,\mathrm{m/s}$) sem carga. Aplicando $T_l=0{,}05\,\mathrm{N\,m}$, as equações de equilíbrio $0=V-Ri-K_e\omega$ e $0=K_ti-b\omega-T_l$ dão:

$
\omega = \frac{V-\dfrac{RT_l}{K_t}}{\dfrac{Rb}{K_t}+K_e}
$

Com $\dfrac{Rb}{K_t}=\dfrac{1{,}2\times8{,}0\times10^{-5}}{0{,}045}=0{,}0021333$, denominador $0{,}0471333$, e $\dfrac{RT_l}{K_t}=\dfrac{1{,}2\times0{,}05}{0{,}045}=1{,}3333$:

$
\omega=\frac{18{,}85-1{,}3333}{0{,}0471333}\approx371{,}56\ \mathrm{rad/s}\ \Rightarrow\ v\approx0{,}929\ \mathrm{m/s}
$

Em malha aberta a velocidade cai de $1{,}000$ para $0{,}929\,\mathrm{m/s}$ ($7{,}07\%$) e permanece ali enquanto a carga persistir.

### E a mesma conta em malha fechada

Em malha fechada com ação integral, o resultado da seção anterior garante erro de regime nulo para esse mesmo distúrbio: a velocidade converge de volta a $1{,}000\,\mathrm{m/s}$, qualquer que seja o ganho escolhido, desde que estável. Essa correção, porém, só é possível enquanto houver margem de tensão abaixo dos $24\,\mathrm{V}$ do driver — margem que a Unidade 1 já calculou em apenas $5{,}15\,\mathrm{V}$ para o transitório de um degrau de $1{,}0\,\mathrm{m/s}$ partindo do repouso, o problema central da Aula 6.

### Da realimentação de estados à realimentação de saída única

O controlador por alocação de polos da Aula 4 exige medir corrente e velocidade; a maioria dos AGVs de baixo custo mede apenas velocidade pelo encoder. A estrutura PID entrega ação integral e derivativa sobre um único sinal medido, sem sensor adicional — resposta industrial a essa restrição de instrumentação. Formalmente, o PID é um caso particular de $C(s)$: basta reconhecer que $K_p + K_i/s + K_ds$ tem exatamente um polo na origem, o suficiente para elevar $L(s)$ a tipo 1 e obter a eliminação de erro de regime provada nesta aula, sem exigir realimentação de nenhuma variável além da própria saída medida. A Aula 6 projeta esse controlador para o NexaBot e mostra que a escolha dos três ganhos é bem menos trivial do que a estrutura sugere.

> **Recurso visual 1 — Malha aberta versus fechada com distúrbio.** Dois diagramas de blocos: tensão fixa somada ao distúrbio $T_l$ na entrada da planta; e o mesmo distúrbio com um controlador $C(s)$ realimentado pelo erro.
> *Texto alternativo:* comparação entre malha aberta, em que o distúrbio altera a saída diretamente, e malha fechada, em que a realimentação negativa corrige o efeito do distúrbio.

> **Recurso visual 2 — Identidade S + T = 1.** Duas curvas de módulo por frequência: $|S(j\omega)|$ crescente e $|T(j\omega)|$ decrescente, com a soma constante igual a 1 destacada.
> *Texto alternativo:* gráfico das funções de sensibilidade e complementar do NexaBot, cuja soma permanece igual a 1 em qualquer frequência.

> **Recurso visual 3 — Velocidade sob carga: aberta contra fechada.** Degrau de torque em $t=1\,\mathrm{s}$: a curva aberta estabiliza em $0{,}929\,\mathrm{m/s}$; a fechada retorna a $1{,}000\,\mathrm{m/s}$.
> *Texto alternativo:* resposta à mesma perturbação de carga em malha aberta, que se estabiliza abaixo da referência, e em malha fechada, que retorna à referência.

### Laboratório da aula

Em `projeto_nexabot/aula_05/`: `02_rejeicao_disturbio.py` simula a mesma malha por integração RK4 — tensão fixa em malha aberta contra um `DiscretePID` ($K_p=2{,}0$, $K_i=50{,}0$, $K_d=0{,}001$) em malha fechada — sob um degrau de $30\%$ do torque nominal, medindo velocidade final, erro final e recuperação nos dois casos; `03_sensibilidade.py` varre $S(j\omega)$ e $T(j\omega)$ do mesmo PID em versão contínua e confirma numericamente a identidade $S+T=1$.

```
.venv/bin/python aula_05/02_rejeicao_disturbio.py
.venv/bin/python aula_05/03_sensibilidade.py
```

O primeiro imprime velocidade final de $0{,}7771\,\mathrm{m/s}$ em malha aberta (erro de $22{,}3\%$, sem recuperar) contra $1{,}0000\,\mathrm{m/s}$ em malha fechada (erro final $\approx0{,}000\%$); o segundo imprime a maior diferença $\vert S(j\omega)+T(j\omega)-1\vert$ observada na varredura, da ordem de $10^{-16}$, confirmando a identidade.

### Atividade prática

Repita o exemplo para $T_l=0{,}08\,\mathrm{N\,m}$: calcule a queda percentual em malha aberta pelas mesmas equações; prove, pelo argumento de tipo de sistema, que a malha fechada converge à mesma referência independentemente do novo valor de carga; usando `03_sensibilidade.py`, identifique a faixa de frequência em que $|S(j\omega)|<0{,}1$ e explique o que ela representa para rejeição de distúrbios de baixa frequência.

### Síntese da aula

- Realimentação negativa liga o erro à ação de controle; malha aberta e fechada compartilham a planta, não a resposta a distúrbios.
- $S(s)+T(s)=1$: nenhum projeto reduz sensibilidade a distúrbio e resposta a referência na mesma frequência.
- O tipo do sistema determina se o erro de regime a um distúrbio constante é nulo; a planta do NexaBot é tipo 0 e depende do controlador para ganhar essa propriedade.
- Sob $0{,}05\,\mathrm{N\,m}$ de carga, a malha aberta perde $7{,}07\%$ de velocidade permanentemente; a malha fechada com ação integral recupera a referência exata.
- PID de saída única é a alternativa industrial à realimentação de estados quando só a velocidade é medida.

### Roteiro da Videoaula 5 — "A carga muda, e a malha aberta erra de novo"

O roteiro falado completo está em `roteiros_20min.md` desta unidade, retomando o distúrbio de $0{,}05\,\mathrm{N\,m}$ como demonstração central.

### Referências da aula

- OGATA, Katsuhiko. *Engenharia de controle moderno*. 5. ed. São Paulo: Pearson, 2011.
- FRANKLIN, Gene F.; POWELL, J. David; EMAMI-NAEINI, Abbas. *Sistemas de controle para engenharia*. 6. ed. Porto Alegre: Bookman, 2013.
- ÅSTRÖM, Karl Johan; MURRAY, Richard M. *Feedback Systems: An Introduction for Scientists and Engineers*. 2. ed. Princeton: Princeton University Press, 2021.

## Aula 6 — PID na prática: sintonia, métricas e anti-windup

### Situação-problema: uma referência que os 24 V não sustentam

Pede-se ao NexaBot $1{,}3\,\mathrm{m/s}$, acima do limite físico de $1{,}273\,\mathrm{m/s}$ em $24\,\mathrm{V}$. O integrador do PID acumula indefinidamente enquanto o erro nunca desaparece. Minutos depois a referência cai para $1{,}0\,\mathrm{m/s}$, alcançável — mas o robô dispara acima do alvo antes de estabilizar. Esta aula projeta o PID do NexaBot e trata esse *windup* como parte do projeto.

### Estrutura do PID e a ação derivativa filtrada

O PID combina proporcional ($K_pe$), integral ($K_i\int e\,dt$, que zera o erro de regime, Aula 5) e derivativa ($K_d\dot e$, antecipação de tendência). A derivada pura amplifica ruído de encoder, por isso é filtrada com polo em $N$: $K_d\frac{Ns}{s+N}$. O NexaBot usa $N=20$. Quanto maior $N$, mais próxima do derivativo ideal e mais sensível ao ruído de alta frequência que a Aula 5 já havia identificado como o preço de um $T(s)$ próximo de 1; quanto menor $N$, mais o filtro atrasa a ação derivativa e menos ela cumpre seu papel de antecipação. A escolha de $N=20$ é um compromisso, não um valor universal: cada planta e cada nível de ruído de sensor pedem sua própria varredura.

### Sintonia de Ziegler-Nichols pelo ganho crítico

O método clássico eleva $K_p$ (sem $I$ nem $D$) até oscilação sustentada — o **ganho crítico** $K_u$ — e mede o **período crítico** $T_u$. A planta contínua, com dois polos reais e nenhum zero, jamais oscilaria sob proporcional puro em tempo contínuo: a oscilação só aparece porque o controlador roda em tempo discreto, com $T_s=5\,\mathrm{ms}$ — o atraso de fase da amostragem, tema da Aula 7, é o que torna o método aplicável aqui.

### Exemplo numérico: obtendo $K_u$, $T_u$ e comparando sintonias

Discretizando $G(s)$ por ZOH em $T_s=5\,\mathrm{ms}$ e variando $K_p$, o par de polos complexos cruza o círculo unitário em $K_u\approx3{,}691$, com ângulo de $98{,}23^\circ$ por amostra, correspondendo a $T_u\approx18{,}32\,\mathrm{ms}$:

| Sintonia | $K_p$ | $K_i$ | $K_d$ |
| --- | --- | --- | --- |
| Proporcional pura | $1{,}846$ | — | — |
| PI | $1{,}661$ | $108{,}78$ | — |
| PID clássico | $2{,}215$ | $241{,}72$ | $0{,}00507$ |
| PID sem sobressinal | $0{,}738$ | $80{,}57$ | $0{,}00446$ |

Simulando um degrau de $400\,\mathrm{rad/s}$ com atuador saturado, as quatro sintonias — mais um ajuste manual $K_p=1{,}2$, $K_i=70$, $K_d=0{,}002$ — dão sobressinal quase idêntico ($24{,}6\%$ a $24{,}8\%$) e subida de $0{,}160\,\mathrm{s}$: o erro inicial já satura $24\,\mathrm{V}$ para qualquer um desses ganhos, e a subida é ditada pela planta saturada, não pelo controlador. A diferença aparece depois: a sintonia clássica deixa oscilação residual de $\pm2{,}3\,\mathrm{rad/s}$ em torno de $400\,\mathrm{rad/s}$, em vez de convergir; um teste sem saturação confirma que $K_d=0{,}00507$ combinado ao filtro $\tau_f=0{,}01\,\mathrm{s}$ e a $T_s=5\,\mathrm{ms}$ mantém oscilação não amortecida mesmo para referências pequenas — a sintonia clássica não pode ser aplicada sem verificação na malha discreta real.

### Métricas de aceitação e o problema da saturação

Quatro métricas quantificam uma sintonia: **sobressinal** percentual, **tempo de subida** (10–90%), **tempo de acomodação** dentro de $2\%$ e **ISE** ($\int e^2\,dt$), que penaliza erro grande e erro prolongado. O termo integral atualiza por $I[k]=I[k-1]+K_iT_se[k]$: enquanto $e[k]\neq0$, $I[k]$ cresce, mesmo que a tensão calculada já exceda o que o driver entrega. Na referência de $1{,}3\,\mathrm{m/s}$ ($24{,}51\,\mathrm{V}$ necessários, acima dos $24\,\mathrm{V}$ disponíveis), o erro nunca se anula e o integrador cresce sem correspondência com a tensão realmente aplicada — o *windup*.

### Anti-windup por *back-calculation*

A correção compara a saída calculada $u_{ns}$ com a saída aplicada $u$ e realimenta a diferença ao integrador: $I[k]\leftarrow I[k]+K_{aw}(u[k]-u_{ns})T_s$. Sem saturação, $u=u_{ns}$ e a correção é nula; durante a saturação, ela reduz o integrador na proporção do comando que não pôde ser aplicado. O nome *back-calculation* vem exatamente disso: em vez de impedir a priori que o integrador cresça, o método deixa o cálculo normal acontecer e, a posteriori, recalcula quanto desse crescimento deveria ter sido descontado porque a planta nunca recebeu o comando correspondente. Com $K_{aw}=1/T_s$ multiplicando efetivamente uma constante de tempo de correção igual a $T_s$, a correção atua na mesma escala de tempo do próprio controlador, sem introduzir uma dinâmica adicional lenta ou instável.

### Demonstração: com e sem anti-windup

Com os ganhos manuais ($K_p=1{,}3$, $K_i=15{,}0$, $K_d=0{,}01$), a referência irreal de $4{,}0\,\mathrm{m/s}$ ($1\,600\,\mathrm{rad/s}$, acima do teto físico de $1{,}273\,\mathrm{m/s}$ em $24\,\mathrm{V}$) é mantida por $0{,}5\,\mathrm{s}$ e cai para $0{,}5\,\mathrm{m/s}$ ($200\,\mathrm{rad/s}$, segura e alcançável). No instante da troca, o integrador acumulou $9\,251{,}6$ sem correção contra $4\,668{,}2$ com $K_{aw}=2$ — redução de aproximadamente $49{,}5\%$, quase metade. O tempo para a velocidade voltar e permanecer dentro da faixa de $2\%$ do novo alvo cai de $2\,256{,}5\,\mathrm{ms}$ para $872{,}5\,\mathrm{ms}$ — cerca de $2{,}6$ vezes mais rápido. O pico de velocidade pós-comutação é quase igual nos dois casos ($\approx509\,\mathrm{rad/s}$, o teto físico do motor herdado da fase irreal), pois o robô já havia ultrapassado a referência antes da troca; a diferença real é quanto tempo leva para descer, arrastado pelo excesso de integral.

> **Recurso visual 4 — Ganho crítico e oscilação sustentada.** Velocidade oscilando constantemente sob $K_p=K_u=3{,}691$, $T_s=5\,\mathrm{ms}$, com $T_u\approx18{,}32\,\mathrm{ms}$ marcado entre dois picos.
> *Texto alternativo:* oscilação sustentada da malha discreta do NexaBot no ganho crítico, com o período marcado entre dois picos.

> **Recurso visual 5 — Quatro sintonias comparadas.** Resposta ao degrau sobreposta para PI, sem sobressinal, manual e clássica, com zoom na oscilação residual da clássica.
> *Texto alternativo:* quatro curvas quase sobrepostas na fase saturada e divergentes depois, com a sintonia clássica mantendo oscilação persistente.

> **Recurso visual 6 — Anti-windup por back-calculation.** Diagrama do PID discreto com bloco de saturação e um ramo que realimenta $(u-u_{ns})\times K_{aw}$ ao integrador.
> *Texto alternativo:* diagrama de blocos do PID discreto com o ramo de anti-windup que corrige o integrador pela diferença entre comando calculado e aplicado.

> **Recurso visual 7 — Integrador com e sem anti-windup.** Curva sem correção subindo a $9\,251{,}6$ até a troca de referência; curva com anti-windup ($K_{aw}=2$) chegando a apenas $4\,668{,}2$ no mesmo instante.
> *Texto alternativo:* crescimento do termo integral com e sem anti-windup, evidenciando redução de aproximadamente metade no valor acumulado no instante da troca de referência.

### Laboratório da aula

`aula_06/01_ganho_critico.py` varre $K_p$ na malha discreta, localiza o cruzamento do círculo unitário e imprime $K_u$, $T_u$ e a tabela de Ziegler-Nichols via `nexabot.controllers.ziegler_nichols`. `04_antiwindup.py` reproduz a referência irreal seguida da alcançável, imprimindo o integrador na comutação e o tempo de recuperação para `Kaw=0.0` e `Kaw=2.0`.

```
.venv/bin/python aula_06/01_ganho_critico.py
.venv/bin/python aula_06/04_antiwindup.py
```

O primeiro imprime `Ku = 3.691`, `Tu = 0.01832 s`; o segundo imprime o integrador na comutação, $9\,251{,}6$ sem anti-windup contra $4\,668{,}2$ com $K_{aw}=2$, e o tempo de recuperação, $2\,256{,}5\,\mathrm{ms}$ contra $872{,}5\,\mathrm{ms}$.

### Atividade prática

Ajuste $K_d$ da sintonia clássica (mantendo $K_p$, $K_i$) até a malha linear, sem saturação, deixar de oscilar para uma referência pequena; reporte o maior $K_d$ que ainda converge, comparando com $0{,}00507$. Repita a demonstração de anti-windup com $K_{aw}=2{,}0$ e $K_{aw}=0{,}5$ e explique por que um ganho maior não é automaticamente melhor.

### Síntese da aula

- O PID combina proporcional, integral e derivativa filtrada; a integral zera o erro de regime a distúrbio constante, como provado na Aula 5.
- Para o NexaBot discreto em $T_s=5\,\mathrm{ms}$, $K_u\approx3{,}691$ e $T_u\approx18{,}32\,\mathrm{ms}$.
- Sob saturação, sintonias diferentes podem ter sobressinal e subida quase idênticos, pois a dinâmica saturada da planta domina a fase inicial.
- A sintonia clássica de Ziegler-Nichols pode deixar oscilação residual não amortecida na malha discreta real e exige verificação antes de uso.
- *Windup* ocorre quando o integrador cresce mesmo com atuador saturado; o anti-windup por *back-calculation* reduziu o acúmulo do integrador em aproximadamente $49{,}5\%$ e o tempo de recuperação em cerca de $2{,}6$ vezes.

### Roteiro da Videoaula 6 — "O integrador que não sabia parar"

O roteiro falado completo está em `roteiros_20min.md` desta unidade, retomando a referência inalcançável de $1{,}3\,\mathrm{m/s}$ como demonstração central.

### Referências da aula

- OGATA, Katsuhiko. *Engenharia de controle moderno*. 5. ed. São Paulo: Pearson, 2011.
- ÅSTRÖM, Karl Johan; RUNDQWIST, Lars. Integrator windup and how to avoid it. In: AMERICAN CONTROL CONFERENCE, 1989, Pittsburgh. *Proceedings [...]*. Pittsburgh: IEEE, 1989. p. 1693-1698. DOI: 10.23919/ACC.1989.4790464.
- FRANKLIN, Gene F.; POWELL, J. David; EMAMI-NAEINI, Abbas. *Sistemas de controle para engenharia*. 6. ed. Porto Alegre: Bookman, 2013.

## Aula 7 — Discretização e escolha do período de amostragem

### Situação-problema: economizar ciclos de CPU quase custa a estabilidade

Para liberar tempo de processamento a outras tarefas do NexaBot, um engenheiro propõe aumentar $T_s$ de $5\,\mathrm{ms}$ para $50\,\mathrm{ms}$, argumentando que a malha "funcionou bem" nas simulações contínuas da Aula 6. O que era estável em simulação contínua se torna instável quando essa suposição é levada ao extremo. Esta aula mostra onde está o limite entre economia aceitável e economia que destrói a malha.

### Da equação diferencial ao mapa discreto: Euler, Tustin e ZOH

Euler para frente aproxima $\dot x\approx(x[k+1]-x[k])/T_s$; Euler para trás usa $\dot x\approx(x[k]-x[k-1])/T_s$ e é adotado no integrador do `DiscretePID`. Tustin, $s\approx\frac{2}{T_s}\frac{z-1}{z+1}$, preserva melhor a resposta em frequência. Para a planta, o laboratório usa ZOH porque representa tensão constante entre amostras, como no PWM; para o controlador, usa a regra conveniente à implementação.

### O contrato numérico do PID discreto

O `DiscretePID` — a classe que a Unidade 4 traduzirá para C, comparada amostra a amostra — segue um contrato exato:

$
e[k]=r[k]-y[k]
$
$
I[k]=I[k-1]+K_iT_s\,e[k]
$
$
D[k]=\frac{K_d(e[k]-e[k-1])+\tau_fD[k-1]}{\tau_f+T_s}
$
$
u_{ns}=K_pe[k]+I[k]+D[k]
$
$
u[k]=\mathrm{sat}(u_{ns},\pm24\,\mathrm{V})
$

Se $u[k]\neq u_{ns}$: $I[k]\leftarrow I[k]+K_{aw}(u[k]-u_{ns})T_s$. O estado cabe em `integral`, `d_state` e erro anterior; o contrato será traduzido para C sem histórico crescente nem alocação dinâmica.

### Escolha do período de amostragem a partir das constantes de tempo

Um critério prático liga $T_s$ à constante de tempo dominante que a malha precisa acompanhar: $138{,}6\,\mathrm{ms}$ pelo polo lento do modelo acoplado, ou $148{,}1\,\mathrm{ms}$ pela aproximação mecânica desacoplada. A literatura de controle digital usa de $10$ a $30$ amostras por constante dominante como faixa inicial, a confirmar pela simulação da malha real, não como fórmula fechada. Com $T_s=5\,\mathrm{ms}$, obtêm-se $27{,}7$ amostras pelo valor modal exato ou $29{,}6$ pela aproximação — ambos dentro da faixa.

### Exemplo numérico: a varredura de $T_s$ e o limiar de instabilidade

Recalculando o maior polo de malha fechada dos ganhos usados no laboratório desta aula ($K_p=0{,}5$, $K_i=5{,}0$, $K_d=0{,}0005$, $\tau_f=0{,}01\,\mathrm{s}$ — mais moderados que os ganhos de Ziegler-Nichols da Aula 6, escolhidos deliberadamente para que o efeito de $T_s$ apareça isolado, sem que a saturação do atuador mascare tudo) para $T_s$ de $0{,}5$ a $100\,\mathrm{ms}$:

| $T_s$ (ms) | Amostras por $\tau_m$ | Maior $\vert$polo$\vert$ |
| --- | --- | --- |
| $0{,}5$ | $296{,}0$ | $0{,}9947$ |
| $5{,}0$ | $29{,}6$ | $0{,}9500$ |
| $10{,}0$ | $14{,}8$ | $0{,}9052$ |
| $20{,}0$ | $7{,}4$ | $0{,}8280$ |
| $27{,}70$ | $5{,}3$ | $1{,}000$ |
| $30{,}0$ | $4{,}9$ | $1{,}2817$ |
| $50{,}0$ | $3{,}0$ | $3{,}5401$ |
| $100{,}0$ | $1{,}5$ | $9{,}7254$ |

Por este critério — o de polos da malha fechada discreta, que ignora a saturação do atuador — a malha é estável até $T_s\approx27{,}70\,\mathrm{ms}$ e diverge além disso. A margem máxima ocorre perto de $T_s=5\,\mathrm{ms}$, resultado de uma varredura, não de convenção.

O critério acima é linear e ignora o limite de $\pm24\,\mathrm{V}$. Na simulação não linear, há bom desempenho até $8{,}26\,\mathrm{ms}$, degradação desde $11{,}29\,\mathrm{ms}$ e instabilidade observável apenas a partir de $44{,}34\,\mathrm{ms}$. A saturação limita a energia e pode manter a amplitude limitada mesmo com polos lineares instáveis. Portanto, os critérios não se contradizem: medem propriedades diferentes. Para projeto, usa-se o limite linear de $27{,}70\,\mathrm{ms}$ como referência conservadora; a simulação saturada vale apenas para os cenários exercitados.

### Atraso computacional de um ciclo e margem de fase

Em um microcontrolador real, medir, calcular e atuar não são instantâneos: entre a amostra do encoder e a atualização do PWM decorre, tipicamente, quase um ciclo completo de $T_s$ de atraso computacional, que se comporta como atraso de transporte $e^{-sT_s}$, subtraindo fase em toda frequência. A tabela acima, sem esse atraso, já é portanto um limite otimista — o que separa um resultado algébrico de um limite seguro de operação em campo.

### Quantização de encoder e de PWM

Menor $T_s$ dá menos pulsos de encoder por amostra e pode aumentar o ruído da velocidade estimada. O PWM também possui níveis discretos. Assim, escolher $T_s$ equilibra margem, atraso e quantização.

### Pausa para reflexão

A varredura linear indica limite de $27{,}70\,\mathrm{ms}$ e a simulação saturada, $44{,}34\,\mathrm{ms}$. Como *jitter* varia o período ciclo a ciclo, qual margem deve ser preservada se uma carga ocasional levar uma execução a $25\,\mathrm{ms}$?

> **Recurso visual 8 — Três métodos de discretização.** Resposta ao degrau sobreposta para Euler para frente, Euler para trás e Tustin no mesmo $T_s$.
> *Texto alternativo:* três curvas de resposta ao degrau muito próximas, uma para cada método de discretização do integrador, no mesmo período de amostragem.

> **Recurso visual 9 — Maior módulo de polo em função de $T_s$.** Curva em U com mínimo perto de $T_s=5\,\mathrm{ms}$, cruzando o limite de instabilidade linear (o critério conservador) em $T_s\approx27{,}70\,\mathrm{ms}$; uma segunda marca, mais à direita, indica a fronteira de instabilidade observada na simulação com atuador saturado, perto de $T_s\approx44{,}34\,\mathrm{ms}$.
> *Texto alternativo:* maior módulo de polo de malha fechada em função do período de amostragem, com margem máxima perto de cinco milissegundos, cruzamento do critério linear de instabilidade perto de vinte e oito milissegundos, e a fronteira mais otimista da simulação saturada perto de quarenta e quatro milissegundos.

> **Recurso visual 10 — Linha do tempo de um ciclo de controle real.** Leitura do encoder, cálculo do PID e atualização do PWM dentro de um período $T_s$, com a atuação ocorrendo após a amostra lida.
> *Texto alternativo:* linha do tempo de um ciclo de amostragem mostrando leitura, cálculo e atuação, com a atuação posterior ao instante da medição.

### Laboratório da aula

`01_euler_tustin_zoh.py` discretiza $G(s)$ por Euler, Tustin e ZOH e compara a resposta ao degrau de cada versão discreta com a resposta contínua de referência. `02_escolha_de_ts.py` varre $T_s$ de $0{,}5$ a $100\,\mathrm{ms}$ com o PID fixo desta aula, simulando a malha completa **com saturação do atuador**, e classifica cada resposta em bom desempenho, degradado ou instável.

```
.venv/bin/python aula_07/01_euler_tustin_zoh.py
.venv/bin/python aula_07/02_escolha_de_ts.py
```

O primeiro imprime, por método, o erro RMS, o erro final e o erro de pico contra a resposta contínua — o ZOH sai exato, por construção; o segundo imprime a tabela de classificação por $T_s$ e fecha com o resumo: bom desempenho até $T_s\approx8{,}26\,\mathrm{ms}$, degradação a partir de $T_s\approx11{,}29\,\mathrm{ms}$ e malha instável a partir de $T_s\approx44{,}34\,\mathrm{ms}$ (fronteira refinada por bisseção) — a fronteira **da simulação saturada**, mais otimista que o limite linear de $27{,}70\,\mathrm{ms}$ calculado acima.

### Atividade prática

Repita a varredura de `02_escolha_de_ts.py` para a sintonia PI de Ziegler-Nichols ($K_p=1{,}661$, $K_i=108{,}78$, sem derivativo) e determine sua fronteira de instabilidade na simulação saturada. Compare com os $44{,}34\,\mathrm{ms}$ do PID fixo desta aula e explique, pela ausência de ação derivativa e pelos ganhos bem mais altos, se a margem encontrada é maior, menor ou semelhante. Em seguida, calcule também o critério linear de polos (sem saturação) para essa sintonia e verifique se a mesma relação entre os dois critérios — o linear sempre mais conservador que o saturado — se mantém.

### Síntese da aula

- Euler para frente, Euler para trás e Tustin discretizam de formas diferentes; o ZOH modela o atuador entre amostras.
- O contrato numérico do `DiscretePID` — integral por Euler para trás, derivada filtrada por diferença para trás — é o mesmo reproduzido em C na Unidade 4.
- $T_s=5\,\mathrm{ms}$ dá cerca de $29{,}6$ amostras por $\tau_m$, dentro da faixa recomendada de $10$ a $30$.
- Para os ganhos deste laboratório, o critério linear de polos dá estabilidade até $T_s\approx27{,}70\,\mathrm{ms}$ (cerca de $5{,}3$ amostras por $\tau_m$) — o limite de projeto seguro; a simulação com atuador saturado só diverge visivelmente a partir de $T_s\approx44{,}34\,\mathrm{ms}$, um critério mais otimista e menos conservador.
- O atraso computacional de um ciclo, presente em qualquer implementação real, reduz ainda mais essa margem otimista.

### Roteiro da Videoaula 7 — "Trinta amostras por constante de tempo: de onde vem esse número"

O roteiro falado completo está em `roteiros_20min.md` desta unidade, retomando a varredura de $T_s$ de $0{,}5$ a $100\,\mathrm{ms}$ como demonstração central.

### Referências da aula

- FRANKLIN, Gene F.; POWELL, J. David; WORKMAN, Michael L. *Digital Control of Dynamic Systems*. 3. ed. Menlo Park: Addison-Wesley, 1997.
- WESCOTT, Tim. PID without a PhD. *Embedded Systems Programming*, [s. l.], out. 2000.
- OGATA, Katsuhiko. *Engenharia de controle moderno*. 5. ed. São Paulo: Pearson, 2011.

## Aula 8 — Co-simulação planta-controlador com FMI 3.0

### Situação-problema: dois modelos, dois relógios, um só resultado esperado

A planta do NexaBot existe como Python e como componente C independente; o controlador segue em Python. Rodar os dois juntos exige decidir com que frequência um entrega dados ao outro, e um integrante sugere trocar dados a cada $50\,\mathrm{ms}$ em vez de $5\,\mathrm{ms}$, para reduzir sobrecarga sem prejuízo perceptível. Esta aula mede esse prejuízo, em vez de supor que é pequeno.

### Por que simular planta e controlador em integradores separados

Quando subsistemas são desenvolvidos por ferramentas diferentes, integrá-los em um executável monolítico nem sempre é viável: cada ferramenta mantém seu integrador, otimizado para seu domínio. A **co-simulação** troca a integração única por simuladores independentes que trocam entradas e saídas em **pontos de comunicação**, mantendo seus próprios passos internos entre eles. No NexaBot, essa separação já existe na prática: a planta é candidata natural a um modelo multifísico mantido pela mecânica, enquanto o PID discreto é código que o firmware evolui independentemente. Forçar as duas equipes a um único executável criaria uma dependência de ferramenta indesejada; a co-simulação existe para evitar essa amarração.

### O padrão FMI e o FMU de co-simulação

A **Functional Mock-up Interface** (FMI) é o padrão aberto mais adotado pela indústria automotiva e aeroespacial para empacotar um modelo simulável independente de ferramenta. Um **FMU** de co-simulação é um `.fmu` — um `.zip` — com `modelDescription.xml` declarando entradas, saídas e parâmetros, mais uma biblioteca binária que implementa instanciação, inicialização e avanço no tempo (`doStep`). O NexaBot exporta sua planta como FMU, com o mesmo modelo de `nexabot.plant` compilado em C. Qualquer ferramenta compatível com FMI carrega esse `.fmu` sem conhecer o código-fonte original, pois toda a interação ocorre pelas funções padronizadas do `modelDescription.xml` — essa independência de ferramenta é o objetivo central da sigla.

### Passo de comunicação e o mestre de co-simulação

O **mestre de co-simulação** avança ambos os modelos: a cada passo de comunicação $H$, envia a cada FMU as entradas mais recentes, chama `doStep` para avançar $H$ segundos e coleta as novas saídas. Entre pontos de comunicação, cada modelo mantém a entrada constante — uma retenção de ordem zero imposta pelo protocolo, distinta da do atuador físico (Aula 7), mas de efeito análogo: quanto maior $H$, mais desatualizada a informação usada por cada modelo. Essa disciplina é conhecida como acoplamento *Jacobi*: os dois modelos avançam em paralelo dentro de cada intervalo $H$, usando só os valores trocados no início dele. Alternativas mais elaboradas — acoplamento *Gauss-Seidel*, ou passo de comunicação adaptativo — reduzem esse erro sem exigir reduzir $H$ uniformemente, mas ficam fora do escopo desta aula.

### Exemplo numérico: o erro de acoplamento cresce com $H$

Acoplando o `DiscretePID` do mestre de co-simulação ($K_p=0{,}30$, $K_i=6{,}0$, sem derivativo) ao FMU da planta sob um degrau de referência de $1{,}0\,\mathrm{m/s}$ ($400\,\mathrm{rad/s}$), a trajetória com passo $H$ foi comparada a uma referência quase contínua ($H=0{,}5\,\mathrm{ms}$):

| $H$ (ms) | Erro RMS relativo | Erro máximo relativo | Convergência |
| --- | --- | --- | --- |
| $1$ | $0{,}03\%$ | $0{,}12\%$ | correta |
| $5$ | $0{,}25\%$ | $1{,}09\%$ | correta |
| $10$ | $0{,}53\%$ | $2{,}31\%$ | correta |
| $20$ | $1{,}08\%$ | $4{,}95\%$ | correta |
| $50$ | $6{,}23\%$ | $14{,}00\%$ | correta |

O erro cresce continuamente com $H$ em toda a faixa testada, mas a co-simulação converge ao valor correto nos cinco pontos — para os ganhos e a referência usados aqui, o custo de aumentar $H$ é só de fidelidade, não de estabilidade, dentro dessa faixa. Isso não contradiz a Aula 7: $H$ desempenha, para o mestre de co-simulação, exatamente o papel que $T_s$ desempenha para o firmware embarcado — entre pontos de comunicação a tensão fica retida e o `DiscretePID` interno passa a amostrar a $T_s=H$ —, mas se essa retenção chega a desestabilizar a malha depende dos ganhos do controlador e de quão perto eles operam do limite de $T_s$, exatamente como a Aula 7 mostrou ao comparar o critério linear de polos com a simulação saturada. Nada nesta varredura garante a mesma folga para outra combinação de ganhos e referência — é por isso que a Aula 7 recomenda o limite linear, mais conservador, como referência de projeto. A proposta de $H=50\,\mathrm{ms}$ da situação-problema, mesmo sem cruzar nenhum limite de estabilidade nesta demonstração, já não é gratuita: o erro RMS de $6{,}23\%$ e o erro de pico de $14{,}00\%$ comprometem sozinhos a fidelidade da co-simulação.

### Verificação do FMU contra o modelo de referência

Antes de atribuir qualquer diferença ao acoplamento, `verify_fmu.py` compara o FMU em C, amostrado no mesmo passo, contra `nexabot.plant.simulate` em Python, sob entrada em degraus alinhados a $H$ — isolando erro numérico de erro de acoplamento, com erro relativo máximo abaixo de $1\%$. Essa separação é metodologicamente importante: sem ela, um erro de acoplamento grande e um erro de implementação do FMU seriam indistinguíveis a partir de um único gráfico de trajetória divergente, e a equipe poderia gastar dias depurando o compilador C quando o problema real estava na escolha de $H$.

### Ligando ao contrato do PID e à Unidade 4

O controlador aqui já é o mesmo `DiscretePID` com o contrato fechado na Aula 7; na Unidade 4, ele deixará de ser Python e passará a ser C gerado automaticamente, acoplável ao FMU sem a ponte Python-C ainda usada aqui — mas herdando os mesmos limites de $H$ medidos nesta aula, porque esses limites vêm da física e da malha de controle, não da linguagem em que o controlador está escrito.

### Transição para a Unidade 3

Esta unidade fechou a malha do NexaBot, sintonizou-a, discretizou-a e mediu o erro de acoplá-la a outro modelo. Toda evidência até aqui veio de simulação: cada gráfico mostrou o que o sistema faz em um cenário escolhido. A Unidade 3 muda a pergunta: em vez de simular alguns cenários, verifica exaustivamente **todos** os cenários alcançáveis do supervisor de segurança do NexaBot, prova que requisitos como REQ-SAFE-001 nunca são violados, e gera testes automaticamente do mesmo modelo.

> **Recurso visual 11 — Arquitetura de co-simulação FMI.** FMU da planta e controlador, cada um com integrador próprio, conectados por um mestre de co-simulação que troca dados só nos múltiplos de $H$.
> *Texto alternativo:* FMU da planta e controlador como caixas independentes coordenadas por um mestre de co-simulação que troca dados apenas nos pontos de comunicação espaçados por H.

> **Recurso visual 12 — Estrutura interna de um .fmu.** Árvore do `.zip` com `modelDescription.xml` na raiz e `binaries/x86_64-linux/NexaBotPlant.so`.
> *Texto alternativo:* árvore de diretórios de um FMU com o arquivo de descrição na raiz e a biblioteca binária na pasta de binários da plataforma.

> **Recurso visual 13 — Erro de acoplamento cresce com H.** Escala logarítmica, $H$ (1, 5, 10, 20, 50 ms) no eixo x, erro RMS relativo no eixo y, crescendo continuamente sem cruzar nenhum limiar de instabilidade nesta faixa.
> *Texto alternativo:* erro relativo da co-simulação crescendo suavemente com o passo de comunicação, do menor ao maior H testado, sem salto de instabilidade nesta demonstração.

> **Recurso visual 14 — Trajetórias para H pequeno e H grande.** $H=5\,\mathrm{ms}$ quase sobreposto à referência de passo fino; $H=50\,\mathrm{ms}$ com atraso e desvio transitório visivelmente maiores.
> *Texto alternativo:* co-simulação com passo pequeno acompanhando a trajetória de referência e com passo grande exibindo maior diferença durante o transitório, embora permaneça limitada na faixa testada.

### Laboratório da aula

Em `nexabot/fmu/`, `build_fmu.py` compila `plant_fmu.c` e empacota `NexaBotPlant.fmu`; `verify_fmu.py` confere o FMU contra `plant.simulate`. Em `projeto_nexabot/aula_08/`, `01_build_fmu.py` constrói e lista o pacote, `02_inspecta_fmu.py` confere sua interface, `03_cosim_basica.py` fecha a malha e `04_erro_de_acoplamento.py` compara os cinco valores de $H$.

```
.venv/bin/python -m nexabot.fmu.build_fmu
.venv/bin/python -m nexabot.fmu.verify_fmu
.venv/bin/python aula_08/01_build_fmu.py
.venv/bin/python aula_08/02_inspecta_fmu.py
.venv/bin/python aula_08/03_cosim_basica.py
.venv/bin/python aula_08/04_erro_de_acoplamento.py
```

O construtor imprime o conteúdo do `.fmu`; a verificação isolada mede erros máximos de aproximadamente $5{,}5\times10^{-10}\%$ em velocidade e $1{,}8\times10^{-8}\%$ em corrente. A varredura de acoplamento mede erro RMS crescente de $0{,}0284\%$ em $H=1\,\mathrm{ms}$ a $6{,}2299\%$ em $H=50\,\mathrm{ms}$, sem declarar instabilidade nos cinco pontos.

### Atividade prática

Usando `04_erro_de_acoplamento.py`, estabeleça um limite de aceitação de $1\%$ para erro RMS e identifique o maior $H$ aprovado entre os cinco valores testados. Depois, acrescente valores entre $10$ e $20\,\mathrm{ms}$ para localizar por bisseção o cruzamento desse **limite de fidelidade**. Explique por que esse resultado é específico dos ganhos, da referência e da métrica adotados e não pode ser anunciado como limite universal de estabilidade.

### Síntese da aula

- Co-simulação mantém integradores independentes que trocam dados em pontos de comunicação espaçados por $H$, em vez de integrar um modelo monolítico.
- FMI empacota um modelo em um FMU — um `.zip` com `modelDescription.xml` e biblioteca binária — independente da ferramenta que o criou.
- Entre pontos de comunicação, cada modelo mantém a última entrada constante, uma retenção de ordem zero do protocolo.
- Para o cenário testado, o erro RMS cresce monotonicamente de $0{,}0284\%$ em $H=1\,\mathrm{ms}$ a $6{,}2299\%$ em $H=50\,\mathrm{ms}$; os cinco casos permanecem limitados, mas os passos grandes comprometem a fidelidade.
- Verificar o FMU isoladamente contra o modelo em Python separa erro de implementação de erro de acoplamento.
- Simulação mostra o comportamento em cenários escolhidos; a Unidade 3 verifica exaustivamente todos os cenários alcançáveis.

### Roteiro da Videoaula 8 — "Dois relógios, um só resultado: o preço de espaçar a comunicação"

O roteiro falado completo está em `roteiros_20min.md` desta unidade, retomando a varredura do passo de comunicação como demonstração central.

### Referências da aula

- MODELICA ASSOCIATION. *Functional Mock-up Interface Specification*, version 3.0, 2022.
- BLOCHWITZ, Torsten et al. Functional mockup interface 2.0: the standard for tool independent exchange of simulation models. In: INTERNATIONAL MODELICA CONFERENCE, 9., 2012, Munique. *Proceedings [...]*. Linköping: Linköping University Electronic Press, 2012. p. 173-184.
- FRANKLIN, Gene F.; POWELL, J. David; EMAMI-NAEINI, Abbas. *Sistemas de controle para engenharia*. 6. ed. Porto Alegre: Bookman, 2013.

## Atividades, síntese e material complementar

### Quiz não avaliativo

**Questão 1.** O NexaBot é submetido a um torque de carga constante de $0{,}05\,\mathrm{N\,m}$ sob duas configurações estáveis: (I) proporcional puro; (II) proporcional-integral. O que se pode afirmar sobre o erro de velocidade em regime causado por esse distúrbio?

a. Em ambas o erro de regime é nulo, pois qualquer realimentação negativa elimina o efeito de um distúrbio constante.
b. Apenas (I) elimina o erro, pois o ganho proporcional pode ser ajustado para qualquer valor necessário.
*c. Apenas (II) elimina o erro, pois a ação integral introduz um polo na origem em $L(s)$, tornando $S(0)=0$ independentemente dos ganhos.
d. Nenhuma elimina o erro, pois isso exigiria também ação derivativa.
e. O erro de regime depende só da magnitude do torque, não da estrutura do controlador.

*Feedback conceitual:* a alternativa correta é c. O erro de regime a um distúrbio constante é o valor final de $S(s)T_l(s)$; com proporcional puro, $S(0)$ é finito e não nulo — erro residual apenas atenuado. Um polo na origem em $C(s)$ torna $L(s)$ tipo 1 e força $S(0)=0$, eliminando o erro a qualquer $K_p$ ou $K_i$, desde que a malha seja estável. Aumentar só o proporcional reduz o erro sem jamais anulá-lo.

**Questão 2.** Na co-simulação FMI do NexaBot, a equipe aumenta o passo de comunicação de $H=5\,\mathrm{ms}$ para $H=20\,\mathrm{ms}$ para reduzir sobrecarga. A varredura mede erro RMS de aproximadamente $0{,}25\%$ no primeiro caso e $1{,}08\%$ no segundo. O que esses dados permitem concluir?

a. O aumento de $H$ não teve efeito mensurável, pois os dois erros são numericamente idênticos.
b. O caso de $20\,\mathrm{ms}$ é necessariamente instável, pois qualquer erro RMS acima de $1\%$ prova divergência.
*c. O passo maior degradou a fidelidade no cenário medido, mas esses dois números, sozinhos, não demonstram instabilidade nem autorizam generalizar o mesmo limite para outros controladores.
d. O aumento de $H$ melhorou a resposta, pois reduziu o número de trocas entre os componentes.
e. O erro medido prova que a implementação C do FMU está incorreta.

*Feedback conceitual:* a alternativa correta é c. Entre pontos de comunicação, a entrada fica retida e o controlador reage mais tarde, aumentando o erro de acoplamento. A varredura observada confirma degradação de fidelidade, não divergência: estabilidade exige um critério próprio e depende dos ganhos, da referência e do ponto de operação.

### Síntese da unidade

- Fechar a malha do NexaBot introduz as funções $S$ e $T$, ligadas por $S+T=1$, formalizando o compromisso entre rejeitar distúrbios e rastrear referência.
- A ação integral garante erro de regime nulo a distúrbios constantes, independentemente dos ganhos, desde que a malha seja estável.
- Ziegler-Nichols fornece um ponto de partida a partir de $K_u$ e $T_u$, mas precisa ser verificado na malha discreta: a sintonia clássica deixou oscilação residual que PI, manual e sem sobressinal não apresentaram.
- Saturação e *windup* não são hipóteses acadêmicas: a margem de tensão do NexaBot para o transitório é estreita, e o anti-windup reduziu o acúmulo do integrador em aproximadamente metade.
- O contrato numérico do `DiscretePID` — Euler para trás na integral, diferença para trás filtrada na derivada, saturação e anti-windup — é o mesmo reproduzido em C na Unidade 4.
- O período de amostragem não é livre: para os ganhos da Aula 7, o critério linear cruza o círculo unitário perto de $27{,}70\,\mathrm{ms}$ e a simulação saturada só é classificada como instável perto de $44{,}34\,\mathrm{ms}$; $T_s=5\,\mathrm{ms}$ permanece na região de bom desempenho.
- Co-simulação por FMI acopla modelos independentes trocando dados em pontos espaçados por $H$, que herda os limites de estabilidade de um período de amostragem.
- Simulação, mesmo em malha fechada e bem discretizada, mostra apenas cenários específicos; a Unidade 3 verifica exaustivamente todos os cenários alcançáveis.

### Material complementar

#### Direto da Fonte

**Texto provocativo:** Esta unidade provou, com números do NexaBot, que a ação integral zera o erro de regime a um distúrbio constante — caso particular de uma teoria mais geral de sensibilidade e tipo de sistema. O capítulo indicado desenvolve essa teoria com as mesmas ferramentas de Laplace da Unidade 1.

**Referência:** FRANKLIN, Gene F.; POWELL, J. David; EMAMI-NAEINI, Abbas. *Sistemas de controle para engenharia*. 6. ed. Porto Alegre: Bookman, 2013. Capítulo sobre propriedades básicas da realimentação e erro de regime permanente.

**Link de acesso:** disponível na Biblioteca Virtual da instituição.

**Aula indicada:** Aula 5, após a demonstração de que a ação integral zera o erro de regime.

#### Para Mergulhar no Assunto

**Texto provocativo:** Um artigo curto, para quem programa firmware sem formação em controle, mostra como implementar um PID digital funcional sem álgebra de Laplace — a mesma estrutura numérica formalizada aqui pelo contrato do `DiscretePID`.

**Referência:** WESCOTT, Tim. PID without a PhD. *Embedded Systems Programming*, [s. l.], out. 2000.

**Link de acesso:** <https://www.wescottdesign.com/articles/pid/pidWithoutAPhd.pdf>. Acesso em: 29 ago. 2026.

**Aula indicada:** Aula 7, após a apresentação do contrato numérico do `DiscretePID`.

#### Podcast

**Texto provocativo:** O autor explica, com simulações visuais, por que um integrador satura antes de o cálculo "perceber" e como a correção por *back-calculation* resolve isso — o mesmo mecanismo reproduzido nesta unidade.

**Referência:** DOUGLAS, Brian. *Anti-windup for PID Control | Understanding PID Control, Part 2*. [S. l.: s. n.], 2018. 1 vídeo (9 min). Publicado no canal MATLAB, no YouTube.

**Link de acesso:** <https://www.youtube.com/watch?v=NVLXCwc8HzM>. Acesso em: 29 ago. 2026.

**Aula indicada:** Aula 6, após a demonstração de anti-windup com e sem correção.

#### Artigo científico

**Texto provocativo:** Antes de o anti-windup por *back-calculation* virar rotina industrial, alguém precisou nomear o problema com precisão e comparar formalmente as estratégias de correção. Este é o artigo de referência, que separa "sei que existe anti-windup" de "sei por que o anti-windup que implementei funciona".

**Referência:** ÅSTRÖM, Karl Johan; RUNDQWIST, Lars. Integrator windup and how to avoid it. In: AMERICAN CONTROL CONFERENCE, 1989, Pittsburgh. *Proceedings [...]*. Pittsburgh: IEEE, 1989. p. 1693-1698. DOI: 10.23919/ACC.1989.4790464.

**Link de acesso:** <https://doi.org/10.23919/ACC.1989.4790464>. Acesso em: 29 ago. 2026.

**Aula indicada:** Aula 6, após a formalização do anti-windup por *back-calculation*.

## Referências da unidade

FRANKLIN, Gene F.; POWELL, J. David; EMAMI-NAEINI, Abbas. *Sistemas de controle para engenharia*. 6. ed. Porto Alegre: Bookman, 2013.

FRANKLIN, Gene F.; POWELL, J. David; WORKMAN, Michael L. *Digital Control of Dynamic Systems*. 3. ed. Menlo Park: Addison-Wesley, 1997.

OGATA, Katsuhiko. *Engenharia de controle moderno*. 5. ed. São Paulo: Pearson, 2011.

ÅSTRÖM, Karl Johan; MURRAY, Richard M. *Feedback Systems: An Introduction for Scientists and Engineers*. 2. ed. Princeton: Princeton University Press, 2021.

ÅSTRÖM, Karl Johan; RUNDQWIST, Lars. Integrator windup and how to avoid it. In: AMERICAN CONTROL CONFERENCE, 1989, Pittsburgh. *Proceedings [...]*. Pittsburgh: IEEE, 1989. p. 1693-1698. DOI: 10.23919/ACC.1989.4790464.

MODELICA ASSOCIATION. *Functional Mock-up Interface Specification*, version 3.0, 2022.

BLOCHWITZ, Torsten et al. Functional mockup interface 2.0: the standard for tool independent exchange of simulation models. In: INTERNATIONAL MODELICA CONFERENCE, 9., 2012, Munique. *Proceedings [...]*. Linköping: Linköping University Electronic Press, 2012. p. 173-184.

WESCOTT, Tim. PID without a PhD. *Embedded Systems Programming*, [s. l.], out. 2000.
