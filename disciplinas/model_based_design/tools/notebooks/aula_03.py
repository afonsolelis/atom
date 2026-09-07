"""Notebook da Aula 3 — Laplace, polos e constante de tempo."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import ABERTURA_IMPORTS, GLOSSARIO, RODAPE_ERRO, md, code  # noqa: E402

TITULO = "Aula 3 — Trocando cálculo por álgebra"
SLUG = "laplace_e_polos"

CELULAS = [
    md("""
# Aula 3 — Trocando cálculo por álgebra

## O que você vai fazer aqui

Você tem duas equações diferenciais. Elas descrevem o motor, mas são
desconfortáveis de manipular.

Hoje você aprende um truque que transforma essas equações diferenciais em
**divisão de polinômios** — coisa que dá para fazer no papel. E vai descobrir
que dois números resumem o comportamento inteiro do motor.

De quebra, o mistério dos 63% da Aula 1 acaba.

**Pré-requisito:** notebooks das Aulas 1 e 2.
"""),

    md("""
## Antes de começar

### 1. O que a transformada de Laplace *faz*

Livros gastam capítulos definindo Laplace. Para o que você vai usar aqui,
cabe em uma frase:

> **Laplace troca "derivada" por "multiplicar por $s$".**

Só isso. É um dicionário.

No mundo do tempo, você escreve $\\frac{di}{dt}$ e precisa de cálculo. No
mundo de Laplace, isso vira $s \\cdot I(s)$, e você precisa de... multiplicação.

| No tempo | Em Laplace |
| --- | --- |
| $x(t)$ | $X(s)$ |
| $\\frac{dx}{dt}$ | $s\\,X(s)$ |
| $\\frac{d^2x}{dt^2}$ | $s^2 X(s)$ |
| integral de $x$ | $\\frac{X(s)}{s}$ |

Por que isso importa? Porque uma equação diferencial cheia de derivadas vira
uma **equação algébrica comum**, do tipo que você resolve isolando a variável.

Analogia: é como logaritmo. Multiplicação é chata, soma é fácil; o logaritmo
troca uma pela outra. Laplace faz o mesmo com derivada e multiplicação.

**Você não precisa saber calcular uma transformada de Laplace.** Precisa saber
o que ela faz. O computador calcula.

### 2. O que é uma *função de transferência*

Depois do truque, o motor inteiro vira **uma fração**:

$$
G(s) = \\frac{\\text{o que sai}}{\\text{o que entra}} = \\frac{\\Omega(s)}{V(s)}
$$

Uma fração que diz: *"para cada volt que entra, sai tanto de velocidade"*. Só
que essa "taxa" depende de quão rápido você mexe na entrada — e o $s$ é
justamente quem carrega essa informação.

### 3. O que é um *polo*

Esta é a palavra que assusta mais e explica mais.

Um **polo** é um número que diz **a que velocidade o sistema esquece**.

Sério, é isso. Se você empurra o sistema e solta, ele volta ao repouso. O polo
diz o quão rápido esse esquecimento acontece.

- Polo bem negativo (ex.: $-343$) → esquece rapidíssimo.
- Polo perto de zero (ex.: $-7$) → esquece devagar, o efeito perdura.
- Polo **positivo** → não esquece: cresce sem parar. Isso é instabilidade, e é
  o pesadelo de quem projeta controle.

O motor do NexaBot tem **dois** polos. Um rápido (o elétrico) e um lento (o
mecânico). É a mesma diferença de ritmo que você viu nas Aulas 1 e 2 — agora
com nome e número.
"""),

    md(GLOSSARIO),

    md("""
## Passo 1 — O motor virou uma fração

A célula abaixo pede a função de transferência do motor. Repare que a saída é
literalmente uma fração de polinômios em $s$.
"""),
    code(ABERTURA_IMPORTS + r"""
from nexabot.params import PARAMS
from nexabot.plant import transfer_function

G = transfer_function()

print("Função de transferência do NexaBot — velocidade por tensão:")
print()
print(G)
print()
print("Leia assim: no numerador, o quanto o motor empurra (Kt/(L·J)).")
print("No denominador, o quanto o motor resiste — e é o denominador que")
print("decide o comportamento.")
"""),

    md("""
## Passo 2 — Os dois polos

**Polo é raiz do denominador.** É onde a fração explodiria.

A célula abaixo pede os polos e traduz cada um para linguagem de tempo.

A conversão é simples: se o polo é $p$, a constante de tempo é
$\\tau = \\frac{1}{|p|}$ (lê-se "tau"). Ou seja, polo grande em módulo =
tempo pequeno = rápido.
"""),
    code(r"""
polos = G.poles()

print("Os dois polos do motor:")
print()
for k, p in enumerate(sorted(polos, key=abs), start=1):
    tau = 1.0 / abs(p.real)
    print(f"  polo {k}: {p.real:>10.2f}    →  constante de tempo τ = {tau*1000:7.2f} ms")

lento, rapido = sorted(polos, key=abs)
print()
print(f"Razão entre eles: {abs(rapido.real/lento.real):.0f} vezes.")
print()
print("O polo rápido é o lado ELÉTRICO (a corrente).")
print("O polo lento é o lado MECÂNICO (a velocidade).")
print()
print("Na Aula 1 você estimou 48x medindo os gráficos, e na Aula 2 viu a")
print("mesma proporção na matriz A. Aqui deu 47x. A pequena diferença é")
print("esperada: lá você usou fórmulas aproximadas para cada lado isolado,")
print("aqui são os polos exatos do sistema acoplado. Três caminhos")
print("independentes chegando à mesma ordem de grandeza.")
"""),

    md("""
## Passo 3 — Finalmente, o mistério dos 63%

Na Aula 1 eu pedi que você guardasse um número: a velocidade chegava a **63%**
do valor final em 141 ms. Prometi explicar. Aqui está.

Quando um sistema de um polo responde a um degrau, ele segue exatamente esta
curva:

$$
y(t) = y_{\\text{final}} \\cdot \\left(1 - e^{-t/\\tau}\\right)
$$

Substitua $t = \\tau$ (ou seja, esperou exatamente uma constante de tempo):

$$
y(\\tau) = y_{\\text{final}} \\cdot (1 - e^{-1}) = y_{\\text{final}} \\cdot (1 - 0{,}368) = 0{,}632 \\cdot y_{\\text{final}}
$$

**63,2% não foi escolha de ninguém.** É o que $1 - 1/e$ vale. A engenharia
adotou esse ponto como régua justamente porque ele cai sempre no mesmo lugar,
independente do sistema.

Rode a célula e veja isso acontecer no motor de verdade.
"""),
    code(r"""
import numpy as np
from nexabot.plant import simulate

t, X = simulate(u_of_t=12.0, t_end=2.0)
omega = X[:, 1]
omega_final = omega[-1]

tau_mecanico = 1.0 / abs(lento.real)
idx_tau = int(np.argmin(np.abs(t - tau_mecanico)))
fracao = omega[idx_tau] / omega_final

print(f"Constante de tempo do polo lento:  τ = {tau_mecanico*1000:.1f} ms")
print(f"Velocidade final:                      {omega_final:.2f} rad/s")
print(f"Velocidade em t = τ:                   {omega[idx_tau]:.2f} rad/s")
print("-" * 52)
print(f"Fração alcançada em t = τ:             {fracao*100:.1f}%")
print(f"Previsão teórica (1 - 1/e):            {(1 - np.exp(-1))*100:.1f}%")
print()
print()
print("Deu 62,4% onde a teoria prevê 63,2%. Por que não bateu exato?")
print("Porque a fórmula dos 63,2% vale para um sistema de UM polo, e o")
print("motor tem dois. O polo rápido atrasa um tiquinho a largada, e essa")
print("sobra de 0,8 ponto é exatamente ele. Menos de um por cento: é o")
print("preço de tratar um sistema de dois polos como se tivesse um.")
print()
print("Régua prática que você vai usar o resto da vida:")
for n in (1, 2, 3, 5):
    print(f"  {n}τ = {n*tau_mecanico*1000:6.0f} ms  →  {(1-np.exp(-n))*100:5.1f}% do valor final")
"""),

    md("""
### O gráfico dessa régua

A célula abaixo desenha a resposta com as marcas de 1τ, 2τ, 3τ e 5τ.

Guarde a linha de **5τ**: é a regra de bolso da engenharia para "acabou". Em
cinco constantes de tempo o sistema chegou a 99,3% — perto o suficiente de
qualquer coisa prática.

É por isso que na Aula 1 eu simulei 2 segundos: 5τ dá cerca de 693 ms, e eu
queria folga de sobra.
"""),
    code(r"""
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(9.5, 5))

ax.plot(t, omega, color="#002057", linewidth=2.5, label="velocidade do motor")
ax.axhline(omega_final, color="#888888", linestyle="--", linewidth=1,
           label="valor final")

cores = ["#C0392B", "#D68910", "#4A9D5F", "#5B8DBE"]
for n, cor in zip((1, 2, 3, 5), cores):
    t_n = n * tau_mecanico
    y_n = omega_final * (1 - np.exp(-n))
    ax.plot([t_n], [y_n], "o", color=cor, markersize=8, zorder=5)
    ax.annotate(f"{n}τ = {t_n*1000:.0f} ms\n{(1-np.exp(-n))*100:.1f}%",
                xy=(t_n, y_n), xytext=(t_n + 0.06, y_n - 45),
                fontsize=9, color=cor,
                arrowprops=dict(arrowstyle="-", color=cor, alpha=0.6))

ax.set_xlabel("tempo [s]")
ax.set_ylabel("velocidade ω [rad/s]")
ax.set_title("A régua das constantes de tempo", fontsize=13, pad=12)
ax.set_xlim(0, 1.2)
ax.set_ylim(0, omega_final * 1.15)
ax.legend(loc="lower right")
ax.grid(alpha=0.25)
plt.tight_layout()
plt.show()
"""),

    md("""
## Passo 4 — Por que dá para ignorar o polo rápido

Aqui está a ideia mais útil desta aula.

O motor tem dois polos: um em $-343$ e outro perto de $-7$. O rápido some em
uns 15 ms; o lento leva 700 ms.

Se você está projetando um controlador que age na escala de centenas de
milissegundos, **o polo rápido já acabou antes de você notar**. Dá para
fingir que ele não existe.

Isso chama-se **separação de escalas de tempo**, e é o que permite simplificar
o motor de segunda ordem para primeira ordem — de duas variáveis para uma.

A célula abaixo compara o modelo completo com o modelo simplificado. Veja o
quanto eles diferem.
"""),
    code(r"""
import control as ct

# modelo simplificado: joga L fora (finge que a corrente responde na hora)
K_dc = PARAMS.Kt / (PARAMS.R * PARAMS.b + PARAMS.Kt * PARAMS.Ke)
tau_simples = (PARAMS.R * PARAMS.J) / (PARAMS.R * PARAMS.b + PARAMS.Kt * PARAMS.Ke)
G_simples = ct.tf([K_dc], [tau_simples, 1.0])

t_c, y_c = ct.step_response(G * 12.0, T=np.linspace(0, 1.5, 3000))
t_s, y_s = ct.step_response(G_simples * 12.0, T=np.linspace(0, 1.5, 3000))

erro_max = float(np.max(np.abs(y_c - y_s)))

print(f"Modelo completo:     2 polos, {len(G.poles())} variáveis de estado")
print(f"Modelo simplificado: 1 polo,  τ = {tau_simples*1000:.1f} ms")
print()
print(f"Maior diferença entre os dois: {erro_max:.2f} rad/s")
print(f"Ou seja, {100*erro_max/y_c.max():.2f}% do valor final.")
print()
print("Menos de dois por cento de erro, com metade da complexidade.")
print("E esse erro todo mora nos primeiros milissegundos — depois disso as")
print("duas curvas são a mesma. Essa troca é uma das decisões mais comuns")
print("em engenharia de controle.")
"""),

    md("""
### Onde a simplificação falha

Não saia simplificando tudo. A célula abaixo mostra o zoom nos primeiros
30 ms — exatamente onde o polo rápido ainda está vivo.

O modelo simplificado sobe **instantaneamente** porque ele acredita que a
corrente aparece do nada. O completo sabe que a corrente leva tempo. Toda a
diferença de 1,83% que a célula anterior mediu está concentrada aqui.

Se o seu problema mora nessa faixa de tempo — proteção de sobrecorrente, por
exemplo — a simplificação te dá a resposta errada.
"""),
    code(r"""
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5))

for ax, limite, titulo in ((ax1, 1.5, "Escala de 1,5 s: idênticos"),
                           (ax2, 0.03, "Zoom nos primeiros 30 ms: diferentes")):
    ax.plot(t_c, y_c, color="#002057", linewidth=2.5, label="completo (2 polos)")
    ax.plot(t_s, y_s, color="#C0392B", linewidth=2, linestyle="--",
            label="simplificado (1 polo)")
    ax.set_xlim(0, limite)
    ax.set_xlabel("tempo [s]")
    ax.set_title(titulo, fontsize=11)
    ax.grid(alpha=0.25)

ax1.set_ylabel("velocidade ω [rad/s]")
ax2.set_ylim(0, 40)
ax1.legend(loc="lower right")
plt.tight_layout()
plt.show()
"""),

    md("""
## Mexa aqui

**Experimento 1 — um motor mais pesado.**
Um eixo mais pesado demora mais para acelerar. Aumente `J` e veja o polo lento
chegar mais perto de zero — e a resposta ficar mais lenta.

**Experimento 2 — mais atrito.**
Aumente `b`. Antes de rodar, preveja: o motor vai ficar mais rápido ou mais
lento? E a velocidade final, sobe ou desce?

**Experimento 3 — o limite da simplificação.**
Aumente `L` (a indutância) bastante. Em algum ponto o polo "rápido" deixa de
ser rápido, os dois se aproximam, e simplificar passa a mentir. Encontre esse
ponto.
"""),
    code(r"""
from dataclasses import replace

# ⬇️ mexa aqui e rode
J_NOVO = PARAMS.J          # tente 5e-4 (o dobro)
B_NOVO = PARAMS.b          # tente 3e-4
L_NOVO = PARAMS.L          # tente 0.05 para quebrar a simplificação

p2 = replace(PARAMS, J=J_NOVO, b=B_NOVO, L=L_NOVO)
G2 = transfer_function(p2)
polos2 = sorted(G2.poles(), key=abs)

print(f"J = {J_NOVO:.2e}   b = {B_NOVO:.2e}   L = {L_NOVO:.2e}")
print("-" * 56)
for k, p in enumerate(polos2, start=1):
    print(f"  polo {k}: {p.real:>10.2f}  →  τ = {1000/abs(p.real):7.2f} ms")
print(f"  separação entre eles: {abs(polos2[1].real/polos2[0].real):.1f}x")
if abs(polos2[1].real / polos2[0].real) < 10:
    print()
    print("  ⚠ menos de 10x de separação: NÃO simplifique este motor.")
    print("    Os dois polos importam na mesma faixa de tempo.")
print()
print(f"  velocidade final com 12 V: {12*p2.dc_gain:.1f} rad/s")
"""),

    md("""
## Aprofundamento (opcional)

### Como Laplace resolve as duas equações de uma vez

Pegue as duas frases da Aula 2 e aplique o dicionário — troque cada
$\\frac{d}{dt}$ por $s$:

$$
L\\,s\\,I = V - R\\,I - K_e\\,\\Omega
\\qquad\\qquad
J\\,s\\,\\Omega = K_t\\,I - b\\,\\Omega
$$

Agora são duas equações **algébricas** com duas incógnitas. Isole $I$ na
primeira, substitua na segunda, isole $\\Omega/V$, e cai a fração que a célula
do Passo 1 imprimiu.

É álgebra de ensino médio. Foi isso que Laplace comprou para você: a chance de
resolver um problema de cálculo isolando variável.

### Para onde isto vai

Polos são metade da história da análise em frequência. A outra metade —
**diagrama de Bode, margem de fase e largura de banda** — chega na **Aula 7**,
junto com o problema de estabilidade que torna essas ferramentas necessárias.

A ordem é de propósito: ferramenta antes do problema é ferramenta esquecida.

Você também vai ouvir falar de **zeros**, o parente dos polos. O NexaBot não
tem nenhum que importe, então eles ficam para o material complementar — um
conceito sem exemplo próprio não gruda.
"""),
    code(r"""
import sympy as sp

s, R, L, Ke, Kt, J, b = sp.symbols("s R L K_e K_t J b", positive=True)
V, I, W = sp.symbols("V I Omega")

eq_eletrica = sp.Eq(L * s * I, V - R * I - Ke * W)
eq_mecanica = sp.Eq(J * s * W, Kt * I - b * W)

solucao = sp.solve([eq_eletrica, eq_mecanica], [I, W], dict=True)[0]
G_simbolico = sp.simplify(solucao[W] / V)

print("A função de transferência, derivada simbolicamente:")
print()
sp.pprint(G_simbolico)
print()
print("Compare com o que a célula do Passo 1 imprimiu numericamente.")
print("Mesma fração — uma com letras, outra com números.")
"""),

    md("""
## O que você leva desta aula

1. **Laplace troca derivada por multiplicação.** É um dicionário, não um
   monstro.
2. **O motor virou uma fração** — a função de transferência.
3. **Polo é a velocidade com que o sistema esquece.** Muito negativo = rápido.
   Positivo = instável.
4. **Constante de tempo τ = 1/|polo|.** Em 1τ o sistema fez 63%; em 5τ,
   99,3% — e aí a engenharia considera que acabou.
5. **Polos muito separados permitem simplificar.** Menos de 10x de separação:
   não simplifique.

Na Aula 4 você vai perguntar duas coisas novas ao modelo: *consigo levar o
robô a qualquer velocidade que eu queira?* e *consigo saber a corrente sem
medir a corrente?*

## Se deu erro

**`AttributeError: 'TransferFunction' object has no attribute 'poles'`**
Versão antiga do `python-control`. Use `G.pole()` (sem o "s") ou atualize:
`uv pip install --python .venv/bin/python -U control`.

**A célula do SymPy demora.**
Normal, ela está fazendo álgebra simbólica. Uns 5 segundos.

**Os polos deram complexos (com `j`).**
Se você mexeu muito em `J`, `b` ou `L`, o motor pode passar a oscilar, e aí os
polos ganham parte imaginária. Isso é física legítima — significa que a
resposta vai balançar antes de assentar. Volte aos valores originais para
seguir a aula.
""" + RODAPE_ERRO),
]
