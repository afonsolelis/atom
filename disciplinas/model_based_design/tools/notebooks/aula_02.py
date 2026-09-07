"""Notebook da Aula 2 — as duas contas de física que descrevem o motor."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import ABERTURA_IMPORTS, GLOSSARIO, RODAPE_ERRO, md, code  # noqa: E402

TITULO = "Aula 2 — Duas contas de física descrevem o motor inteiro"
SLUG = "modelo_do_motor"

CELULAS = [
    md("""
# Aula 2 — Duas contas de física descrevem o motor inteiro

## O que você vai fazer aqui

Na Aula 1 o robô perdeu velocidade e você mediu a queda. Hoje você descobre
**por quê**.

Vai ver que o motor inteiro cabe em **duas frases de física**. E vai descobrir
os cinco números do motor sem abrir o motor — só olhando como ele responde a
um empurrão.

**Pré-requisito:** ter rodado o notebook da Aula 1.
"""),

    md("""
## Antes de começar

Três ideias. Nenhuma delas exige matemática que você não tenha visto.

### 1. O que é uma equação diferencial

Assusta pelo nome. É só isto: **uma frase que diz o quanto uma coisa muda por
segundo**.

Pense na sua conta bancária. Se o salário entra e o aluguel sai, você pode
escrever:

> *a variação do saldo por mês = salário − aluguel*

Pronto, isso é uma equação diferencial. Ela não te diz quanto você tem hoje.
Ela te diz **a que ritmo** o valor está mudando. Se você souber quanto tem
agora e essa regra, consegue prever o resto.

Em notação de engenharia, "a variação de $x$ por segundo" se escreve
$\\frac{dx}{dt}$. Leia como "de-xis-de-tê", e pense "o quanto x muda por
segundo". Só isso.

### 2. O que é *estado*

**Estado é a memória do sistema.** É o conjunto mínimo de coisas que você
precisa saber *agora* para prever o futuro.

Para um carro, saber só a posição não basta — precisa saber a velocidade
também. Posição e velocidade são o estado.

Para o motor do NexaBot, o estado tem **duas coisas**:

- a **corrente** que está passando pelo fio (em ampères);
- a **velocidade de giro** ω do eixo (em rad/s).

Sabendo essas duas agora, mais a tensão que você vai aplicar, dá para prever
tudo. Não precisa saber o histórico. Essa é a mágica do conceito de estado:
ele resume o passado inteiro em dois números.

### 3. As cinco letras, em português

Estas aparecem o tempo todo. Cada uma é uma propriedade física do motor:

| Letra | Lê-se | O que é, sem jargão |
| --- | --- | --- |
| `R` | erre | O quanto o fio **resiste** à passagem de corrente |
| `L` | ele | O quanto o fio **resiste a mudar** a corrente rápido |
| `Kt` | ká-tê | Quanto **torque** o motor faz por ampère que passa |
| `Ke` | ká-ê | Quanta **tensão o motor gera** ao girar (ele vira gerador) |
| `J` | jota | O quanto o eixo **custa a acelerar** — é a inércia |
| `b` | bê | O **atrito** que rouba giro |

Guarde `Ke` em especial: quando o motor gira, ele *gera* tensão contrária.
Foi isso que fez a corrente descer devagar no gráfico da Aula 1.
"""),

    md(GLOSSARIO),

    md("""
## Passo 1 — As duas frases

Aqui estão as duas equações. Leia cada uma como uma frase em português antes
de olhar os símbolos.

**Frase 1 — o lado elétrico:**

> A corrente muda conforme sobra tensão para empurrá-la. Sobra a tensão que
> você aplicou, menos a que o fio consome resistindo, menos a que o próprio
> motor gera ao girar.

$$
L\\,\\frac{di}{dt} \\;=\\; \\underbrace{V}_{\\text{o que você aplica}} \\;-\\; \\underbrace{R\\,i}_{\\text{o fio consome}} \\;-\\; \\underbrace{K_e\\,\\omega}_{\\text{o motor gera girando}}
$$

**Frase 2 — o lado mecânico:**

> A velocidade muda conforme sobra torque para acelerar o eixo. Sobra o torque
> que a corrente produz, menos o que o atrito rouba, menos a carga externa.

$$
J\\,\\frac{d\\omega}{dt} \\;=\\; \\underbrace{K_t\\,i}_{\\text{a corrente empurra}} \\;-\\; \\underbrace{b\\,\\omega}_{\\text{o atrito freia}} \\;-\\; \\underbrace{\\tau_{\\text{carga}}}_{\\text{a rampa freia}}
$$

É isso. **O motor inteiro são essas duas frases.** Todo o resto da disciplina
— controle, verificação, código embarcado — é construído em cima delas.

Repare no último termo da frase 2: $\\tau_{\\text{carga}}$ (lê-se "tau de
carga") é exatamente a carga que você ligou na Aula 1. Ela entra freando.
"""),
    code(ABERTURA_IMPORTS + r"""
from nexabot.params import PARAMS
from nexabot.plant import derivative

# A função `derivative` é literalmente as duas frases, escritas em Python.
# Vamos perguntar a ela: "o robô está parado e eu acabei de aplicar 12 V.
# O que muda no próximo instante?"

estado_parado = [0.0, 0.0]     # corrente = 0 A, velocidade = 0 rad/s
d = derivative(estado_parado, u=12.0, tau_load=0.0)

print("Robô parado, 12 V acabaram de ser aplicados:")
print(f"  a corrente está subindo a  {d[0]:>10.1f} A por segundo")
print(f"  a velocidade está subindo a {d[1]:>9.1f} rad/s por segundo")
print()
print("A corrente dispara e a velocidade nem se mexeu ainda.")
print("Faz sentido: sem corrente não há torque, e sem torque nada gira.")
"""),

    md("""
### Confira você mesmo, na mão

A célula acima devolveu dois números. Vamos ver de onde eles vêm.

Com o robô **parado**, temos $i = 0$ e $\\omega = 0$. Substituindo nas duas
frases:

- Frase 1: $\\frac{di}{dt} = \\frac{V - R \\cdot 0 - K_e \\cdot 0}{L} = \\frac{12}{0{,}0035}$
- Frase 2: $\\frac{d\\omega}{dt} = \\frac{K_t \\cdot 0 - b \\cdot 0 - 0}{J} = 0$

A célula abaixo faz essa conta na mão e compara. Se os dois baterem, você
acabou de conferir a física do motor com uma divisão.
"""),
    code(r"""
na_mao_corrente = 12.0 / PARAMS.L
na_mao_velocidade = 0.0 / PARAMS.J

print(f"Na mão:     di/dt = 12 / {PARAMS.L} = {na_mao_corrente:.1f} A/s")
print(f"A função deu:                     {d[0]:.1f} A/s")
print()
print(f"Na mão:     dw/dt = 0 / {PARAMS.J} = {na_mao_velocidade:.1f} rad/s²")
print(f"A função deu:                     {d[1]:.1f} rad/s²")
print()
print("Bateu. Não tem caixa-preta aqui: a função é a fórmula.")
"""),

    md("""
## Passo 2 — Agora com o motor girando

Repita a pergunta, mas com o motor já em movimento. Vamos pegar o robô no
meio da aceleração: corrente de 5 A e velocidade de 150 rad/s.

Antes de rodar, pense: **a corrente ainda vai estar subindo?**

Dica: a 150 rad/s o motor já está gerando bastante tensão contrária.
"""),
    code(r"""
estado_girando = [5.0, 150.0]   # 5 A, 150 rad/s
d2 = derivative(estado_girando, u=12.0, tau_load=0.0)

tensao_gerada = PARAMS.Ke * 150.0
tensao_no_fio = PARAMS.R * 5.0

print("Contabilidade dos 12 V aplicados:")
print(f"  o fio consome resistindo:      {tensao_no_fio:6.2f} V")
print(f"  o motor gera girando (Ke·ω):   {tensao_gerada:6.2f} V")
print(f"  sobra para empurrar corrente:  {12.0 - tensao_no_fio - tensao_gerada:6.2f} V")
print("-" * 48)
print(f"  logo, di/dt = {d2[0]:>8.1f} A/s   (negativo: a corrente está CAINDO)")
print(f"  e    dw/dt = {d2[1]:>8.1f} rad/s² (ainda acelerando)")
"""),

    md("""
### Foi isso que você viu na Aula 1

Lembra do gráfico em que a corrente subia rápido e depois descia devagar?

Agora você sabe o motivo, e ele tem nome: **força contraeletromotriz**. O
termo $K_e\\,\\omega$.

Quanto mais rápido o motor gira, mais tensão ele gera *contra* a que você
aplicou. Sobra menos para empurrar corrente, então a corrente cai. E quando
sobra zero, o motor para de acelerar — chegou na velocidade final.

É por isso que existe uma velocidade máxima para cada tensão. Não é limite
de projeto, é o motor brigando consigo mesmo.
"""),

    md("""
## Passo 3 — Empacotando: as matrizes A, B, C, D

As duas frases são tudo. Mas escrever "as duas frases" toda vez é chato, então
a engenharia empacota isso numa notação padrão:

$$
\\dot{x} = A\\,x + B\\,u
$$

Traduzindo: *"a variação do estado é uma combinação do estado de agora, mais o
efeito do que eu comando"*.

- $x$ é o estado — no nosso caso, `[corrente, velocidade]`
- $u$ é o comando — a tensão
- $A$ é uma tabelinha 2×2 que diz como o estado influencia a si mesmo
- $B$ diz como o comando entra

**Não decore.** O que importa é: `A` e `B` são só as duas frases, reorganizadas
numa tabela. A célula abaixo mostra a tabela e, ao lado, de qual divisão cada
número veio.
"""),
    code(r"""
from nexabot.plant import state_space_matrices

A, B, C, D = state_space_matrices()

print("Matriz A (como o estado influencia a si mesmo):")
print(f"   [ {A[0,0]:>10.3f}  {A[0,1]:>10.3f} ]   ← linha da corrente")
print(f"   [ {A[1,0]:>10.3f}  {A[1,1]:>10.3f} ]   ← linha da velocidade")
print()
print("De onde veio cada número:")
print(f"   -R/L  = -{PARAMS.R}/{PARAMS.L}      = {-PARAMS.R/PARAMS.L:>10.3f}")
print(f"   -Ke/L = -{PARAMS.Ke}/{PARAMS.L}   = {-PARAMS.Ke/PARAMS.L:>10.3f}")
print(f"    Kt/J =  {PARAMS.Kt}/{PARAMS.J}  = {PARAMS.Kt/PARAMS.J:>10.3f}")
print(f"   -b/J  = -{PARAMS.b}/{PARAMS.J}  = {-PARAMS.b/PARAMS.J:>10.3f}")
print()
print("Repare na ordem de grandeza: a primeira linha está na casa das")
print("centenas, a segunda na casa das unidades. O elétrico é MUITO mais")
print("rápido que o mecânico — os mesmos 48x da Aula 1, agora visíveis")
print("na tabela. Isso vira assunto da Aula 3.")
"""),

    md("""
## Passo 4 — Descobrir os cinco números sem abrir o motor

Situação real: o fornecedor entregou o motor montado no chassi e não mandou a
ficha técnica completa. Você não sabe `R`, `L`, `Ke`, `J` nem `b`.

E agora?

**Você empurra o motor e observa a resposta.** Aplica um degrau de tensão,
mede corrente e velocidade, e procura os cinco números que fazem a conta bater
com o que você mediu. Isso chama-se **identificação de sistemas**.

Primeiro, o ensaio. A célula abaixo gera dados de bancada realistas — com
ruído de sensor e tudo, como num laboratório de verdade, não perfeitos.
"""),
    code(r"""
from nexabot.identificacao import gerar_ensaio_degrau

ensaio = gerar_ensaio_degrau(amplitude_v=12.0, t_end=0.8, seed=42)

print(f"Ensaio: degrau de 12 V, {ensaio.t[-1]:.1f} s, {len(ensaio.t)} amostras")
print()
print("Bem no começo, quando o motor mal saiu do lugar:")
print(f"{'t [ms]':>8}  {'corrente medida':>16}  {'velocidade medida':>18}")
for k in range(0, 30, 6):
    print(f"{ensaio.t[k]*1000:>8.1f}  {ensaio.i_medido[k]:>14.3f} A  {ensaio.w_medido[k]:>14.2f} rad/s")
print()
print("Os zeros na velocidade NÃO são erro. O encoder mede contando pulsos,")
print("e nesses primeiros milissegundos o eixo ainda não girou o bastante")
print("para completar um pulso. Para o sensor, isso é indistinguível de")
print("estar parado. É uma limitação real de bancada, e o método precisa")
print("funcionar apesar dela.")
print()
print("Mais adiante, já com o motor girando:")
print(f"{'t [ms]':>8}  {'corrente medida':>16}  {'velocidade medida':>18}")
for k in range(1000, 1250, 50):
    print(f"{ensaio.t[k]*1000:>8.1f}  {ensaio.i_medido[k]:>14.3f} A  {ensaio.w_medido[k]:>14.2f} rad/s")
"""),

    md("""
### O ruído é o ponto, não um defeito

Rode a célula abaixo e compare o sinal **verdadeiro** (que só existe na
simulação) com o **medido** (o que o sensor devolve na vida real).

- A corrente medida vem com **ruído** — chuvisco em volta do valor certo.
- A velocidade medida vem em **degraus** — porque o encoder conta pulsos, e
  entre um pulso e outro ele não tem o que informar.

Nenhum sensor real é perfeito. O método de identificação precisa funcionar
apesar disso, e é por isso que ele usa a trajetória inteira em vez de olhar
ponto a ponto: o ruído se cancela na média, os pontos isolados mentiriam.
"""),
    code(r"""
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9.5, 6.5), sharex=True)

ax1.plot(ensaio.t * 1000, ensaio.i_medido, ".", markersize=2,
         color="#C0392B", alpha=0.5, label="medido pelo sensor")
ax1.plot(ensaio.t * 1000, ensaio.i_verdadeiro, "-", linewidth=2,
         color="#002057", label="verdadeiro (só a simulação sabe)")
ax1.set_ylabel("corrente [A]")
ax1.set_title("O sensor de corrente tem ruído")
ax1.legend()
ax1.grid(alpha=0.3)

ax2.plot(ensaio.t * 1000, ensaio.w_medido, "-", linewidth=1,
         color="#C0392B", alpha=0.8, label="medido pelo encoder")
ax2.plot(ensaio.t * 1000, ensaio.w_verdadeiro, "-", linewidth=2,
         color="#002057", label="verdadeiro")
ax2.set_xlim(0, 60)
ax2.set_xlabel("tempo [ms]  (só os primeiros 60 ms, para dar zoom nos degraus)")
ax2.set_ylabel("velocidade [rad/s]")
ax2.set_title("O encoder mede em degraus: ele conta pulsos")
ax2.legend()
ax2.grid(alpha=0.3)

plt.tight_layout()
plt.show()
"""),

    md("""
## Passo 5 — O ajuste

Agora o computador procura os cinco números.

A ideia, em uma frase: **ele chuta cinco valores, simula, compara com o
ensaio, vê o quanto errou, e ajusta o chute. Repete até parar de melhorar.**

O chute inicial é de propósito **ruim** — 40% a 60% longe da verdade, como
seria numa bancada onde você só conhece a ordem de grandeza pelo datasheet.

Rode. Pode levar alguns segundos: ele está simulando o motor inteiro dezenas
de vezes.
"""),
    code(r"""
from nexabot.identificacao import ajustar_minimos_quadrados, comparar_com_verdade

estimado = ajustar_minimos_quadrados(ensaio)

print(f"Convergiu: {estimado.sucesso}   (em {estimado.iteracoes} iterações)")
print()
print(f"{'parâmetro':>10}  {'verdadeiro':>14}  {'identificado':>14}  {'erro':>8}")
print("-" * 54)
for linha in comparar_com_verdade(estimado):
    print(f"{linha['parametro']:>10}  {linha['verdadeiro']:>14.6g}  "
          f"{linha['identificado']:>14.6g}  {linha['erro_pct']:>7.2f}%")
"""),

    md("""
### O que você acabou de fazer

Você recuperou as cinco propriedades físicas de um motor **sem abrir o motor,
sem datasheet e com sensores imperfeitos**. Só empurrando e observando.

Isso é o pão de cada dia de quem trabalha com sistemas reais. O fornecedor
raramente entrega tudo, e o que ele entrega raramente vale depois de o
equipamento envelhecer.

E tem uma conferência barata, que não depende do ajuste: o **ganho estático**,
que você já viu na Aula 1. Ele é uma conta de uma linha, e tem que bater com
a razão velocidade/tensão que você mediu no ensaio.
"""),
    code(r"""
# ganho estático previsto pelos parâmetros IDENTIFICADOS
ganho_identificado = estimado.Kt / (estimado.R * estimado.b + estimado.Kt * estimado.Ke)

# ganho estático MEDIDO no ensaio: velocidade final dividida pela tensão
w_final_medido = ensaio.w_medido[-200:].mean()
ganho_medido = w_final_medido / 12.0

print(f"Ganho pela fórmula, com os parâmetros identificados: {ganho_identificado:.3f} rad/(s·V)")
print(f"Ganho medido direto no ensaio:                       {ganho_medido:.3f} rad/(s·V)")
print(f"Diferença:                                           {100*abs(ganho_identificado-ganho_medido)/ganho_medido:.2f}%")
print()
print("Duas rotas independentes chegando ao mesmo número. É assim que se")
print("confia num modelo: não por fé, por conferência cruzada.")
"""),

    md("""
## Mexa aqui

**Experimento 1 — um ensaio mais curto.**
Troque `t_end=0.8` para `t_end=0.15` e refaça o ajuste. O erro dos parâmetros
piora muito. Por quê? Dica: em 150 ms a velocidade nem chegou perto de
estabilizar (lembra dos 418 ms da Aula 1?), então o ensaio não contém a
informação sobre o atrito `b`.

**Experimento 2 — sensor pior.**
Aumente `ruido_i_std` de `0.03` para `0.3` — dez vezes mais ruído. Veja quanto
o erro cresce. O método aguenta, mas não faz milagre.

**Experimento 3 — outra bancada.**
Troque `seed=42` para outro número. Isso gera um ruído diferente, como se
fosse outro dia no laboratório. Os parâmetros identificados mudam um pouco.
Essa variação é real, e é por isso que na indústria se faz o ensaio várias
vezes.
"""),
    code(r"""
# ⬇️ mexa nos três e rode
T_FIM = 0.8
RUIDO = 0.03
SEMENTE = 42

ensaio_v2 = gerar_ensaio_degrau(amplitude_v=12.0, t_end=T_FIM,
                                ruido_i_std=RUIDO, seed=SEMENTE)
est_v2 = ajustar_minimos_quadrados(ensaio_v2)

print(f"ensaio de {T_FIM} s, ruído {RUIDO}, semente {SEMENTE}")
print("-" * 54)
erros = [abs(l["erro_pct"]) for l in comparar_com_verdade(est_v2)]
for linha in comparar_com_verdade(est_v2):
    print(f"  {linha['parametro']:>4}: erro de {linha['erro_pct']:>7.2f}%")
print("-" * 54)
print(f"  pior erro: {max(erros):.2f}%")
"""),

    md("""
## Aprofundamento (opcional)

Opcional. É para quem quer saber *como* o computador acha os cinco números.

O método chama-se **mínimos quadrados não lineares**. "Mínimos quadrados"
porque ele minimiza a soma dos erros ao quadrado (eleva ao quadrado para que
errar para cima e para baixo contem igual). "Não linear" porque os cinco
parâmetros entram na conta de um jeito emaranhado, então não dá para resolver
de uma vez — tem que ir chegando perto aos poucos.

O algoritmo específico é o **Levenberg-Marquardt**, que é uma mistura
inteligente de duas estratégias: quando está longe da resposta, ele dá passos
cautelosos; quando está perto, dá passos ousados.

Duas escolhas de projeto que importam:

1. **Ajustar a trajetória inteira**, e não estimar derivadas ponto a ponto.
   Derivada numérica amplifica ruído de forma brutal — dois pontos ruidosos
   viram uma derivada absurda.
2. **Normalizar cada grandeza pelo próprio desvio-padrão.** Corrente está na
   casa dos ampères, velocidade na casa das centenas de rad/s. Sem normalizar,
   a velocidade dominaria o custo e a corrente seria ignorada.

A célula abaixo mostra o quanto o chute inicial estava errado, para você ver
de onde o algoritmo partiu.
"""),
    code(r"""
from nexabot.identificacao import PALPITE_INICIAL_FATOR

print("De onde o algoritmo partiu (o chute inicial):")
print(f"{'parâmetro':>10}  {'verdadeiro':>12}  {'chute inicial':>14}  {'erro do chute':>14}")
print("-" * 58)
for nome, fator in PALPITE_INICIAL_FATOR.items():
    verdadeiro = getattr(PARAMS, nome)
    chute = verdadeiro * fator
    print(f"{nome:>10}  {verdadeiro:>12.6g}  {chute:>14.6g}  {100*(fator-1):>13.0f}%")

print()
print(f"E chegou ao alvo em {estimado.iteracoes} iterações.")
"""),

    md("""
## O que você leva desta aula

1. **Equação diferencial é uma frase sobre o quanto algo muda por segundo.**
   Nada mais assustador que isso.
2. **Estado é a memória do sistema.** Para o motor, são duas coisas: corrente
   e velocidade.
3. **O motor inteiro são duas frases de física** — uma elétrica, uma mecânica,
   ligadas pelas constantes `Kt` e `Ke`.
4. **A força contraeletromotriz (`Ke·ω`) explica o gráfico da Aula 1.** O motor
   girando gera tensão contra si mesmo.
5. **Dá para descobrir os parâmetros sem abrir o motor**, empurrando e
   observando.

Na Aula 3 você vai aprender um truque que transforma essas equações
diferenciais em contas de álgebra comum — e vai descobrir por que aquele 63%
da Aula 1 é o número que a engenharia escolheu.

## Se deu erro

**O ajuste demora demais ou não converge.**
Normal se você mexeu muito nos parâmetros. Volte `t_end` para `0.8` e
`ruido_i_std` para `0.03`.

**`sucesso: False`.**
O algoritmo não conseguiu. Quase sempre é ensaio curto demais ou ruído alto
demais — o ensaio não tem informação suficiente para separar cinco números.

**Os erros deram diferentes dos meus.**
Confira a `seed`. Cada semente é um ruído diferente, como um dia diferente no
laboratório.

**`ModuleNotFoundError`.**
Veja a seção "Se deu erro" do notebook da Aula 1.
""" + RODAPE_ERRO),
]
