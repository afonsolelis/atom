"""Notebook da Aula 7 — o controlador só olha de tempos em tempos."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import ABERTURA_IMPORTS, GLOSSARIO, RODAPE_ERRO, md, code  # noqa: E402

TITULO = "Aula 7 — O controlador pisca"
SLUG = "amostragem"

CELULAS = [
    md("""
# Aula 7 — O controlador pisca

## O que você vai fazer aqui

Até agora a gente fingiu que o controlador enxerga o robô o tempo todo. Ele
não enxerga.

Ele é um programa rodando num microcontrolador. Ele **acorda, mede, calcula,
manda o comando e dorme**. Depois acorda de novo. No NexaBot isso acontece a
cada 5 milissegundos.

Hoje você vai descobrir o que acontece quando ele dorme demais — e vai achar,
com um número, o ponto exato em que o robô fica instável.

**Pré-requisito:** notebooks das Aulas 5 e 6.
"""),

    md("""
## Antes de começar

### 1. Amostragem — a analogia da câmera

Pense num filme. Ele parece movimento contínuo, mas é uma sequência de fotos.
Cinema clássico tira 24 fotos por segundo.

Se você filmar uma roda de carroça girando rápido com poucas fotos por
segundo, acontece aquele efeito estranho: **a roda parece girar para trás**.
Não é defeito da câmera. É que entre uma foto e a seguinte a roda deu quase
uma volta inteira, e a câmera não tem como saber disso.

O controlador é a câmera. Ele tira uma "foto" da velocidade a cada `Ts`
segundos, e entre uma foto e outra ele não faz ideia do que aconteceu.

### 2. `Ts` — o período de amostragem

Lê-se "tê-esse". É o intervalo entre duas fotos.

No NexaBot, `Ts = 5 ms = 0,005 s`. Ou seja, o controlador acorda **200 vezes
por segundo**.

A relação entre período e frequência é a mais simples possível:

$$
f = \\frac{1}{T_s}
$$

$$
\\frac{1}{0{,}005} = 200 \\text{ vezes por segundo} = 200\\ \\text{Hz}
$$

**Hz** (lê-se "hertz") significa "vezes por segundo". Nada além disso.

### 3. Por que não olhar sempre?

Porque custa. Cada vez que o controlador acorda ele gasta ciclos de CPU e
energia. Num robô a bateria, isso é autonomia.

Então existe uma tentação constante de aumentar `Ts` — acordar menos vezes,
gastar menos. Hoje você vê o preço disso.

### 4. Margem de fase

Esta palavra vem da Aula 3, onde ela foi adiada de propósito. Agora ela tem
um problema para resolver.

**Margem de fase** é o quanto de atraso o seu sistema aguenta antes de ficar
instável. É medida em graus, e a regra de bolso é:

- acima de 45° → confortável
- entre 30° e 45° → apertado
- abaixo de 30° → vai oscilar feio
- zero → instável

Cada vez que você aumenta `Ts`, você adiciona atraso, e a margem cai. Quando
ela chega a zero, o robô entra em oscilação crescente.
"""),

    md(GLOSSARIO),

    md("""
## Passo 1 — O mesmo controlador, dois períodos

Vamos rodar o mesmo PID duas vezes: uma acordando a cada 5 ms, outra a cada
40 ms. Nada mais muda — mesmos ganhos, mesmo alvo, mesmo motor.

Antes de rodar, faça a aposta: o que muda?
"""),
    code(ABERTURA_IMPORTS + r"""
import numpy as np
from nexabot.params import PARAMS
from nexabot.plant import simulate
from nexabot.controllers import DiscretePID

ALVO = 200.0

def rodar_com_ts(Ts, Kp=0.3, Ki=8.0, t_end=2.0):
    # O controlador acorda a cada Ts segundos. Entre uma vez e outra, a
    # planta continua evoluindo sozinha, com o último comando congelado.
    pid = DiscretePID(Kp=Kp, Ki=Ki, Kd=0.0, Ts=Ts, Kaw=100.0)
    n = int(t_end / Ts)
    x = np.zeros(2)
    ts = np.zeros(n); ws = np.zeros(n); us = np.zeros(n)
    for k in range(n):
        y = x[1]
        u = pid.step(ALVO, y)
        _, Xk = simulate(u_of_t=u, t_end=Ts, dt=min(Ts / 40, 1e-4), x0=x)
        x = Xk[-1]
        ts[k] = k * Ts; ws[k] = y; us[k] = u
    return ts, ws, us


print(f"{'Ts':>10}  {'acorda':>14}  {'ω final':>10}  {'ainda balança?':>16}")
print("-" * 60)
for Ts in (0.005, 0.040):
    t, w, u = rodar_com_ts(Ts)
    balanco = w[-int(0.4 / Ts):].std()
    marca = "assentou" if balanco < 1.0 else f"±{balanco:.0f} rad/s"
    print(f"{Ts*1000:>7.0f} ms  {1/Ts:>9.0f} Hz  {w[-1]:>10.2f}  {marca:>16}")
"""),

    md("""
## Passo 2 — Onde exatamente ele quebra

Agora a varredura que dá o número.

Vamos aumentar `Ts` aos poucos e medir o quanto o robô ainda está balançando
no fim. Em algum ponto ele para de assentar.

Esse ponto é uma **fronteira física do projeto**: acima dele, nenhum ajuste de
`Kp` ou `Ki` salva. O controlador simplesmente não está olhando o suficiente.
"""),
    code(r"""
print(f"{'Ts':>9}  {'frequência':>12}  {'ω final':>10}  {'balanço':>10}   situação")
print("-" * 68)
limite = None
for Ts_ms in (5, 10, 20, 30, 40, 50, 60, 80):
    Ts = Ts_ms / 1000.0
    t, w, u = rodar_com_ts(Ts, t_end=2.0)
    balanco = w[-int(0.4 / Ts):].std()
    estavel = balanco < 1.0 and np.all(np.isfinite(w)) and w.max() < 3 * ALVO
    if limite is None and not estavel:
        limite = Ts_ms
    situacao = "estável" if estavel else "INSTÁVEL"
    print(f"{Ts_ms:>6} ms  {1/Ts:>9.0f} Hz  {w[-1]:>10.1f}  {balanco:>9.1f}   {situacao}")

print()
if limite:
    print(f"A instabilidade aparece a partir de Ts = {limite} ms.")
    print(f"O NexaBot roda a 5 ms, ou seja, com folga de {limite/5:.0f} vezes.")
    print("Essa folga não é luxo: ela é o que absorve atraso de cálculo,")
    print("variação de temporização e envelhecimento do sistema.")
"""),

    md("""
### O gráfico da quebra

Três períodos, três destinos. Repare que a curva instável não "erra um
pouco": ela **cresce sem parar**.

É esse o comportamento de um polo positivo, que a Aula 3 descreveu como "o
sistema que não esquece". Num robô de armazém, isso é o motor indo de um
extremo ao outro até alguém desligar na tomada.
"""),
    code(r"""
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(9.5, 5.5))
ax.axhline(ALVO, color="#888888", linestyle="--", linewidth=1.2, label="alvo")

for Ts_ms, cor in ((5, "#4A9D5F"), (30, "#D68910"), (60, "#C0392B")):
    t, w, u = rodar_com_ts(Ts_ms / 1000.0, t_end=1.5)
    ax.plot(t, w, linewidth=2, color=cor, label=f"Ts = {Ts_ms} ms")

ax.set_xlabel("tempo [s]")
ax.set_ylabel("velocidade ω [rad/s]")
ax.set_title("O mesmo controlador, olhando com frequências diferentes",
             fontsize=13, pad=12)
ax.set_ylim(-100, 500)
ax.legend(loc="upper right"); ax.grid(alpha=0.25)
plt.tight_layout()
plt.show()
"""),

    md("""
## Passo 3 — Como escolher `Ts` sem descobrir na marra

Existe uma regra de bolso, e ela usa a constante de tempo que você aprendeu na
Aula 3.

> **Amostre entre 10 e 20 vezes dentro da constante de tempo mais rápida que
> você quer controlar.**

A constante de tempo mecânica do NexaBot é de cerca de 140 ms. Dividindo por
20, dá 7 ms. O projeto adotou 5 ms — um pouco mais folgado que o mínimo, e é
assim que se faz.

A célula abaixo aplica a regra.
"""),
    code(r"""
from nexabot.plant import transfer_function

G = transfer_function()
polos = sorted(G.poles(), key=abs)
tau_lento = 1.0 / abs(polos[0].real)
tau_rapido = 1.0 / abs(polos[1].real)

print(f"Constante de tempo mecânica (a que interessa): {tau_lento*1000:6.1f} ms")
print(f"Constante de tempo elétrica (rápida demais):   {tau_rapido*1000:6.1f} ms")
print()
print("Aplicando a regra de bolso sobre a mecânica:")
for n in (10, 20, 30):
    print(f"  {n:>2} amostras dentro de τ  →  Ts = {tau_lento/n*1000:5.1f} ms "
          f"({n/tau_lento:>5.0f} Hz)")
print()
print(f"O projeto adotou Ts = {PARAMS.Ts*1000:.0f} ms, "
      f"o que dá {tau_lento/PARAMS.Ts:.0f} amostras dentro de τ.")
print("Dentro da faixa, com folga para o lado seguro.")
"""),

    md("""
## Passo 4 — Margem de fase: o número que prevê a quebra

A varredura do Passo 2 achou o limite testando. Dá para prever antes de
testar, e o instrumento é a **margem de fase**.

A ideia: amostrar de `Ts` em `Ts` equivale a introduzir um atraso de meio
período (`Ts/2`) no sistema. Atraso come margem de fase. Quando a margem
chega a zero, acabou.

A célula abaixo calcula a margem para cada `Ts` e compara com o que a
simulação mostrou.
"""),
    code(r"""
import control as ct

Kp, Ki = 0.3, 8.0
C = ct.tf([Kp, Ki], [1, 0])          # o PI em forma contínua
malha_aberta = C * G

print(f"{'Ts':>8}  {'atraso (Ts/2)':>15}  {'margem de fase':>16}  leitura")
print("-" * 66)
for Ts_ms in (5, 10, 20, 30, 40, 50, 60, 80):
    Ts = Ts_ms / 1000.0
    # aproximação de Padé de 1a ordem para o atraso de meio período
    atraso = ct.tf(*ct.pade(Ts / 2, 1))
    _, pm, _, _ = ct.margin(malha_aberta * atraso)
    if pm > 45:
        leitura = "confortável"
    elif pm > 30:
        leitura = "apertado"
    elif pm > 0:
        leitura = "vai oscilar"
    else:
        leitura = "INSTÁVEL"
    print(f"{Ts_ms:>5} ms  {Ts/2*1000:>12.1f} ms  {pm:>14.1f}°  {leitura}")

print()
print("Cruze com a varredura do Passo 2: lá o sistema começou a divergir")
print("em Ts = 30 ms, e é exatamente onde esta tabela já marca 'vai")
print("oscilar', com a margem caindo abaixo de 30°.")
print()
print("A margem avisa antes, e sem precisar simular. É por isso que")
print("engenheiro de controle olha para ela.")
"""),

    md("""
## Passo 5 — De contínuo para discreto: a tradução

Uma última peça. O PID que você escreveu na Aula 5 tem uma integral:

$$
u = K_p\\,e + K_i \\int e \\, dt
$$

Mas o microcontrolador não sabe integrar. Ele sabe somar.

A tradução do mundo contínuo para o discreto chama-se **discretização**, e a
mais simples é: *a integral vira uma soma acumulada*.

$$
\\int e\\,dt \\;\\longrightarrow\\; I[k] = I[k-1] + e[k] \\cdot T_s
$$

Leia assim: "o acumulado de agora é o acumulado de antes, mais o erro de agora
vezes o tempo que passou". Uma linha de código.

Existem várias receitas de tradução, com nomes próprios — Euler para frente,
Euler para trás, Tustin, ZOH. Elas diferem em detalhes de precisão. **Esta
disciplina adota Tustin**, que é o melhor compromisso entre exatidão e
simplicidade.

A célula abaixo compara as três mais usadas, para você ver que a diferença
existe mas é pequena na faixa em que trabalhamos.
"""),
    code(r"""
import warnings
warnings.filterwarnings("ignore")   # o scipy reclama do condicionamento; é esperado

Gd_zoh = ct.sample_system(G, PARAMS.Ts, method="zoh")
Gd_tustin = ct.sample_system(G, PARAMS.Ts, method="bilinear")
Gd_euler = ct.sample_system(G, PARAMS.Ts, method="euler")

T = np.arange(0, 1.0, PARAMS.Ts)
resp = {}
for nome, sistema in (("ZOH", Gd_zoh), ("Tustin", Gd_tustin), ("Euler", Gd_euler)):
    _, y = ct.step_response(sistema * 12.0, T=T)
    resp[nome] = y

ref = resp["ZOH"]
print(f"Discretizando a planta com Ts = {PARAMS.Ts*1000:.0f} ms:")
print()
print(f"{'método':>10}  {'valor final':>13}  {'maior desvio do ZOH':>22}")
print("-" * 50)
for nome, y in resp.items():
    desvio = float(np.max(np.abs(y - ref)))
    print(f"{nome:>10}  {y[-1]:>11.2f}  {desvio:>20.3f}")

pior = max(float(np.max(np.abs(y - ref))) for y in resp.values())
print()
print(f"O maior desvio entre os métodos é de {pior:.1f} rad/s sobre {ref[-1]:.0f},")
print(f"ou seja {100*pior/ref[-1]:.1f}%. E ele mora todo no transitório: no fim,")
print("os três param no mesmo lugar.")
print()
print("Compare com o Passo 2, onde trocar o Ts levou o sistema de estável")
print("a divergente. A escolha do método importa muito menos que a")
print("escolha do Ts.")
"""),

    md("""
## Mexa aqui

**Experimento 1 — o limite com outro controlador.**
Baixe `KP` para `0.1` e refaça a varredura. O limite de `Ts` muda? Deve subir:
um controlador mais manso tolera mais atraso. Agressividade e tolerância a
atraso são grandezas opostas.

**Experimento 2 — a folga do projeto.**
Rode com `TS_MS = 5` e olhe a margem de fase. Depois com `TS_MS = 20`. Quanto
de margem você perdeu quadruplicando o período?

**Experimento 3 — a fronteira fina.**
Encontre, com precisão de 1 ms, o maior `Ts` em que o sistema ainda assenta.
Esse número é o orçamento de tempo do seu microcontrolador: tudo — leitura de
sensor, cálculo, escrita no driver — precisa caber nele.
"""),
    code(r"""
# ⬇️ mexa aqui
KP = 0.3
KI = 8.0
TS_MS = 20

Ts = TS_MS / 1000.0
t_x, w_x, u_x = rodar_com_ts(Ts, Kp=KP, Ki=KI, t_end=2.0)
balanco = w_x[-int(0.4 / Ts):].std()

C_x = ct.tf([KP, KI], [1, 0])
atraso_x = ct.tf(*ct.pade(Ts / 2, 1))
_, pm_x, _, _ = ct.margin(C_x * G * atraso_x)

print(f"Kp = {KP}   Ki = {KI}   Ts = {TS_MS} ms ({1/Ts:.0f} Hz)")
print("-" * 52)
print(f"velocidade final : {w_x[-1]:8.2f} rad/s")
print(f"balanço no fim   : {balanco:8.2f} rad/s")
print(f"margem de fase   : {pm_x:8.1f}°")
print()
if balanco < 1.0:
    print("Assentou. Este Ts serve.")
else:
    print("Não assentou. Reduza o Ts ou amanse o controlador.")
"""),

    md("""
## Aprofundamento (opcional)

### Por que Ts/2 de atraso

O controlador calcula o comando no instante `k·Ts` e o mantém congelado até
`(k+1)·Ts`. Do ponto de vista da planta, o comando "certo" chegou cedo demais
no começo do intervalo e tarde demais no fim.

Na média, é como se tudo chegasse com **meio período** de atraso. Daí o
`Ts/2`. Essa aproximação é padrão de projeto e erra pouco.

### As quatro receitas de discretização

| Método | Como traduz a integral | Comentário |
| --- | --- | --- |
| Euler para frente | usa o erro **anterior** | mais simples, e o que mais facilmente instabiliza |
| Euler para trás | usa o erro **atual** | estável sempre, mas distorce um pouco |
| Tustin (bilinear) | usa a **média** dos dois | o melhor compromisso — adotado aqui |
| ZOH | reproduz exato o degrau congelado | o mais fiel à realidade do conversor |

A `DiscretePID` desta disciplina usa Euler para trás na integral e diferença
para trás filtrada na derivada. A escolha não é por exatidão: é porque essa
forma **cabe em duas variáveis de memória**, e vai virar código C na Aula 13.
Em microcontrolador, memória é decisão de projeto.

### Aliasing — a roda girando para trás

O nome do efeito da roda de carroça é **aliasing**. Ele acontece quando o
sinal tem conteúdo mais rápido que metade da taxa de amostragem.

Metade da taxa tem nome: **frequência de Nyquist**. Amostrando a 200 Hz, você
enxerga com honestidade até 100 Hz. Acima disso, o sinal aparece disfarçado de
outra coisa — e não existe filtro digital que desfaça, porque a informação já
foi perdida na foto.
"""),
    code(r"""
f_amostragem = 1.0 / PARAMS.Ts
f_nyquist = f_amostragem / 2

print(f"Taxa de amostragem do NexaBot:  {f_amostragem:6.0f} Hz")
print(f"Frequência de Nyquist:          {f_nyquist:6.0f} Hz")
print()
print("Ou seja: o controlador enxerga honestamente qualquer coisa que")
print(f"aconteça até {f_nyquist:.0f} vezes por segundo. Acima disso, mentira.")
print()

# a dinâmica mais rápida da planta, em Hz
f_eletrica = 1.0 / (2 * np.pi * tau_rapido)
f_mecanica = 1.0 / (2 * np.pi * tau_lento)
print(f"Dinâmica mecânica do motor: {f_mecanica:6.2f} Hz  "
      f"→ {'dentro' if f_mecanica < f_nyquist else 'FORA'} da faixa honesta")
print(f"Dinâmica elétrica do motor: {f_eletrica:6.2f} Hz  "
      f"→ {'dentro' if f_eletrica < f_nyquist else 'FORA'} da faixa honesta")
print()
print("As duas cabem. E note que a elétrica cabe raspando — mais um")
print("motivo para não aumentar o Ts sem pensar.")
"""),

    md("""
## O que você leva desta aula

1. **O controlador não enxerga sempre.** Ele tira fotos a cada `Ts`.
2. **`Ts` grande demais instabiliza**, e nenhum ajuste de ganho salva.
3. **Regra de bolso: de 10 a 20 amostras dentro da constante de tempo.**
4. **Margem de fase prevê a quebra** antes de ela aparecer na simulação.
5. **Discretizar a integral é acumular uma soma.** Uma linha de código.
6. **Frequência de Nyquist é metade da taxa.** Acima dela, o sinal mente.

Na Aula 8 você vai ligar dois simuladores um no outro — a planta de um lado,
o controlador do outro — e descobrir que o erro nasce na conversa entre eles.

## Se deu erro

**`ct.pade` não existe.**
Versão antiga do `python-control`. Atualize, ou pule a célula da margem de
fase: a varredura do Passo 2 já mostra o fenômeno.

**A varredura demora.**
São oito simulações completas. Uns 30 segundos. Reduza `t_end` para `1.2`.

**Algum caso deu `nan` ou `inf`.**
É o sistema instável divergindo até estourar o número de ponto flutuante.
Está certo: é exatamente o que acontece com um robô de verdade batendo no
batente.
""" + RODAPE_ERRO),
]
