"""Notebook da Aula 4 — controlabilidade, observabilidade e o limite dos 24 V."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import ABERTURA_IMPORTS, GLOSSARIO, RODAPE_ERRO, md, code  # noqa: E402

TITULO = "Aula 4 — O que a física deixa você fazer"
SLUG = "limites_do_projeto"

CELULAS = [
    md("""
# Aula 4 — O que a física deixa você fazer

## O que você vai fazer aqui

Você vai fazer duas perguntas ao modelo e receber duas respostas honestas:

1. *Consigo levar o robô a qualquer velocidade que eu queira, com o motor que
   eu tenho?*
2. *Consigo saber a corrente sem medir a corrente?*

Depois vai projetar um controle cada vez mais rápido — até a física dizer não.
E vai ver exatamente onde ela diz não.

**Pré-requisito:** notebooks das Aulas 1 a 3.
"""),

    md("""
## Antes de começar

### 1. Controlabilidade

Nome feio, pergunta simples:

> **Com o comando que eu tenho, consigo levar o sistema a qualquer estado que
> eu queira?**

Um exemplo de quando a resposta é *não*: um carro com o volante travado.
Você acelera e freia à vontade, mas não chega em qualquer lugar do
estacionamento. O carro é *incontrolável* naquela direção.

Para o motor: você comanda a tensão. Essa tensão consegue levar corrente e
velocidade a qualquer combinação? Vamos perguntar.

### 2. Observabilidade

A pergunta espelhada:

> **Com os sensores que eu tenho, consigo descobrir tudo o que está
> acontecendo lá dentro?**

O NexaBot mede **só a velocidade** — tem um encoder no eixo, e nada mais. A
corrente não é medida (o sensor custa dinheiro e ocupa espaço na placa).

Mesmo assim, dá para *deduzir* a corrente? Se der, o sistema é **observável**,
e você acabou de economizar um sensor.

### 3. Saturação

Esta você vai sentir na pele hoje.

O driver do NexaBot entrega **no máximo 24 V**. Se o seu controlador pedir
40 V, o driver entrega 24 e pronto. Pedir mais não faz aparecer mais.

Isso chama-se **saturação**, e é onde a maioria dos projetos bonitos no papel
morre. O papel não tem limite de tensão. O armazém tem.
"""),

    md(GLOSSARIO),

    md("""
## Passo 1 — Perguntando ao modelo

As duas perguntas têm resposta mecânica: monta-se uma tabela com os dados do
modelo e conta-se o *posto* dela (em inglês, *rank*).

**Você não precisa saber montar essas tabelas.** O que precisa saber ler é a
resposta: se o posto for igual ao número de estados (aqui, 2), a resposta é
sim.

Pense no posto como "quantas direções independentes essa tabela alcança".
Posto 2 num sistema de 2 estados significa "alcança tudo".
"""),
    code(ABERTURA_IMPORTS + r"""
import numpy as np
import control as ct
from nexabot.params import PARAMS
from nexabot.plant import state_space

sys_motor = state_space()
n_estados = sys_motor.nstates

Co = ct.ctrb(sys_motor.A, sys_motor.B)     # tabela da controlabilidade
Ob = ct.obsv(sys_motor.A, sys_motor.C)     # tabela da observabilidade

posto_c = np.linalg.matrix_rank(Co)
posto_o = np.linalg.matrix_rank(Ob)

print(f"O motor tem {n_estados} estados: corrente e velocidade.")
print()
print(f"CONTROLÁVEL?  posto {posto_c} de {n_estados}  →  {'SIM' if posto_c == n_estados else 'NÃO'}")
print("   Com a tensão, você alcança qualquer par (corrente, velocidade).")
print()
print(f"OBSERVÁVEL?   posto {posto_o} de {n_estados}  →  {'SIM' if posto_o == n_estados else 'NÃO'}")
print("   Medindo só a velocidade, você deduz a corrente.")
"""),

    md("""
### Por que "observável" vale dinheiro

O motor é observável medindo só a velocidade. Traduzindo para o mundo real:
**você não precisa comprar sensor de corrente**.

Como isso é possível? Volte à Aula 2. As duas equações estão amarradas: a
corrente produz torque, o torque muda a velocidade. Então, olhando **como** a
velocidade muda, dá para inferir quanta corrente estava passando.

A célula abaixo faz exatamente isso: reconstrói a corrente a partir só da
velocidade medida, usando a segunda equação da Aula 2 isolada.
"""),
    code(r"""
from nexabot.plant import simulate

t, X = simulate(u_of_t=12.0, t_end=0.5)
corrente_real = X[:, 0]
velocidade = X[:, 1]

# Da frase 2 da Aula 2:  J·dω/dt = Kt·i − b·ω
# Isolando a corrente:   i = (J·dω/dt + b·ω) / Kt
dw_dt = np.gradient(velocidade, t)
corrente_deduzida = (PARAMS.J * dw_dt + PARAMS.b * velocidade) / PARAMS.Kt

erro = np.abs(corrente_real - corrente_deduzida)

print("Deduzindo a corrente sem medir a corrente:")
print(f"{'t [ms]':>8}  {'real [A]':>10}  {'deduzida [A]':>13}")
for k in range(0, 2500, 500):
    print(f"{t[k]*1000:>8.1f}  {corrente_real[k]:>10.3f}  {corrente_deduzida[k]:>13.3f}")
print()
print(f"Maior erro em toda a simulação: {erro.max():.4f} A")
print(f"E ele acontece em t = {t[int(erro.argmax())]*1000:.1f} ms.")
print()
print("Esse erro está todo no primeiro instante, e não é falha do método:")
print("é a derivada numérica, que na primeira amostra não tem um ponto")
print("anterior para comparar. Do segundo ponto em diante o erro some.")
print()
print(f"Ignorando a primeira amostra, o maior erro cai para {erro[1:].max():.6f} A.")
print()
print("Um sensor de corrente a menos na placa. É isso que 'observável'")
print("significa em reais.")
"""),

    md("""
## Passo 2 — Escolhendo o quão rápido o robô responde

Aqui está o poder que a Aula 3 te deu.

Você aprendeu que **polo = velocidade de esquecer**. Agora vem a virada: com
realimentação, **você escolhe onde ficam os polos**.

O motor sozinho tem polos em $-7$ e $-336$. O lento manda, e ele é lento: 139 ms
de constante de tempo.

E se você quisesse os dois polos em $-50$? A resposta ficaria com τ = 20 ms —
sete vezes mais rápida.

A técnica chama-se **alocação de polos**. Você diz onde quer, e uma conta
devolve os ganhos `K` que colocam eles lá. O `python-control` faz a conta.
"""),
    code(r"""
from nexabot.controllers import state_feedback_gain

# Repare que os dois polos nunca são idênticos: o algoritmo `place` não
# aceita polo repetido num sistema com uma só entrada. Use valores próximos,
# mas distintos.
for alvo in ([-50, -55], [-100, -120], [-300, -350]):
    K = state_feedback_gain(alvo)
    tau_ms = 1000.0 / abs(alvo[0])
    print(f"polos em {str(alvo):>14}  →  τ = {tau_ms:6.1f} ms   "
          f"K = [{K[0,0]:8.4f}, {K[0,1]:8.4f}]")

print()
print("Repare como os ganhos K crescem quando você pede mais velocidade.")
print("Ganho grande significa comando grande. E comando grande esbarra")
print("nos 24 V do driver. É o assunto do próximo passo.")
"""),

    md("""
## Passo 3 — Até a física dizer não

Agora o experimento que dá nome à aula.

Vamos pedir respostas cada vez mais rápidas e, para cada uma, medir **quanta
tensão o controlador realmente pede**. Em algum ponto ele vai pedir mais que
os 24 V que existem.

Antes de rodar, faça uma aposta: em qual velocidade de resposta você acha que
o projeto estoura?
"""),
    code(r"""
def tensao_de_pico(polo, referencia_rad_s=200.0, t_end=0.6, dt=1e-4):
    '''Simula a malha com realimentação de estados e devolve o pico de tensão pedida.'''
    K = state_feedback_gain([polo, polo * 1.2])
    A, B = sys_motor.A, sys_motor.B

    # ganho de pré-alimentação para o regime bater com a referência
    A_mf = A - B @ K
    ganho_dc = (-sys_motor.C @ np.linalg.inv(A_mf) @ B).item()
    N = 1.0 / ganho_dc

    x = np.zeros(2)
    pico = 0.0
    for _ in range(int(t_end / dt)):
        u = (N * referencia_rad_s - K @ x).item()
        pico = max(pico, abs(u))
        u_aplicado = np.clip(u, -PARAMS.V_max, PARAMS.V_max)
        dx = A @ x + B.flatten() * u_aplicado
        x = x + dt * dx
    return pico


print(f"Referência: 200 rad/s   |   Driver entrega no máximo {PARAMS.V_max} V")
print()
print(f"{'polo alvo':>11}  {'τ [ms]':>8}  {'pico pedido':>13}  situação")
print("-" * 56)
for polo in (-10, -25, -50, -75, -100, -150, -200):
    pico = tensao_de_pico(polo)
    ok = pico <= PARAMS.V_max
    marca = "cabe nos 24 V" if ok else f"ESTOUROU ({pico/PARAMS.V_max:.1f}x o driver)"
    print(f"{polo:>11}  {1000/abs(polo):>8.1f}  {pico:>11.1f} V  {marca}")
"""),

    md("""
### A lição

Existe um projeto matematicamente perfeito para qualquer velocidade que você
pedir. A matemática nunca reclama.

**O driver reclama.**

A partir de certo ponto, o controlador pede uma tensão que não existe. O que
acontece na prática não é o projeto falhar elegantemente: o driver satura, o
sistema passa a se comportar de um jeito que o modelo linear não previu, e o
robô faz coisa estranha.

Esse é o momento em que engenharia deixa de ser matemática e passa a ser
escolha. Você tem três saídas:

1. **Aceitar uma resposta mais lenta** — a mais comum e a mais honesta.
2. **Comprar um driver maior** — custa dinheiro e espaço.
3. **Aceitar a saturação e tratá-la** — é o que a Aula 6 vai fazer, com o
   anti-windup.

O gráfico abaixo mostra os dois mundos: o projeto que cabe e o que não cabe.
"""),
    code(r"""
import matplotlib.pyplot as plt

def simular_malha(polo, referencia=200.0, t_end=0.5, dt=1e-4, saturar=True):
    K = state_feedback_gain([polo, polo * 1.2])
    A, B = sys_motor.A, sys_motor.B
    A_mf = A - B @ K
    N = 1.0 / (-sys_motor.C @ np.linalg.inv(A_mf) @ B).item()

    n = int(t_end / dt)
    ts = np.zeros(n); ws = np.zeros(n); us = np.zeros(n)
    x = np.zeros(2)
    for k in range(n):
        u = (N * referencia - K @ x).item()
        us[k] = np.clip(u, -PARAMS.V_max, PARAMS.V_max) if saturar else u
        ws[k] = x[1]; ts[k] = k * dt
        x = x + dt * (A @ x + B.flatten() * us[k])
    return ts, ws, us


fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9.5, 7), sharex=True)

for polo, cor, rotulo in ((-25, "#4A9D5F", "polo −25 (cabe)"),
                          (-150, "#C0392B", "polo −150 (estoura)")):
    ts, ws, us = simular_malha(polo)
    ax1.plot(ts, ws, color=cor, linewidth=2, label=rotulo)
    ax2.plot(ts, us, color=cor, linewidth=2, label=rotulo)

ax1.axhline(200, color="#888888", linestyle="--", linewidth=1, label="referência")
ax1.set_ylabel("velocidade ω [rad/s]")
ax1.set_title("O que o robô faz")
ax1.legend(loc="lower right"); ax1.grid(alpha=0.25)

ax2.axhline(PARAMS.V_max, color="#333333", linestyle="--", linewidth=1.5)
ax2.text(0.30, PARAMS.V_max + 1.5, "teto do driver: 24 V", fontsize=10, color="#333333")
ax2.set_ylabel("tensão pedida [V]")
ax2.set_xlabel("tempo [s]")
ax2.set_title("O que o controlador pede — e o teto que ele encontra")
ax2.grid(alpha=0.25)

plt.tight_layout()
plt.show()
"""),

    md("""
## Mexa aqui

**Experimento 1 — achar o limite exato.**
Na célula abaixo, vá ajustando `POLO_ALVO` até o pico ficar bem em cima dos
24 V. Esse é o projeto mais rápido que o seu driver aguenta.

**Experimento 2 — referência menor.**
Baixe `REFERENCIA` de 200 para 100 rad/s e refaça. O limite muda? Por quê?
Pense: o comando é proporcional ao erro, e um alvo menor gera erro menor.

**Experimento 3 — driver maior.**
Suba `PARAMS.V_max` para 48 V (na célula, usando `replace`). Quanto mais rápido
você consegue ser? A resposta é uma boa estimativa de quanto vale, em
desempenho, gastar mais no driver.
"""),
    code(r"""
from dataclasses import replace

# ⬇️ mexa aqui
POLO_ALVO = -75
REFERENCIA = 200.0
TENSAO_MAX = 24.0

p_mod = replace(PARAMS, V_max=TENSAO_MAX)
pico = tensao_de_pico(POLO_ALVO, referencia_rad_s=REFERENCIA)

print(f"polo alvo = {POLO_ALVO}   (τ = {1000/abs(POLO_ALVO):.1f} ms)")
print(f"referência = {REFERENCIA} rad/s")
print(f"driver     = {TENSAO_MAX} V")
print("-" * 48)
print(f"pico pedido = {pico:.1f} V")
if pico <= TENSAO_MAX:
    folga = 100 * (1 - pico / TENSAO_MAX)
    print(f"CABE. Sobra {folga:.0f}% de folga — dá para pedir mais rápido.")
else:
    print(f"ESTOUROU em {pico - TENSAO_MAX:.1f} V. Peça mais devagar.")
"""),

    md("""
## Aprofundamento (opcional)

### As tabelas por dentro

A matriz de controlabilidade é montada assim: pega-se $B$, depois $AB$, depois
$A^2B$, e assim por diante, até $n-1$ colunas. Para o motor, com 2 estados:

$$
\\mathcal{C} = \\begin{bmatrix} B & AB \\end{bmatrix}
$$

A de observabilidade é a mesma ideia empilhando $C$, $CA$, $CA^2$...

Se essa tabela tem posto cheio, o sistema é controlável (ou observável). A
intuição: cada coluna nova é uma "direção" que o comando alcança; se as
direções cobrem o espaço inteiro, você chega em qualquer lugar.

### E se não fosse controlável?

A célula abaixo constrói um motor de mentira, com `Kt = 0` — um motor cujo
torque não depende da corrente. Fisicamente absurdo, mas útil: veja o posto
cair, e veja a alocação de polos falhar.
"""),
    code(r"""
motor_quebrado = replace(PARAMS, Kt=0.0)
sys_quebrado = state_space(motor_quebrado)

Co_q = ct.ctrb(sys_quebrado.A, sys_quebrado.B)
posto_q = np.linalg.matrix_rank(Co_q)

print("Motor de mentira, com Kt = 0 (a corrente não gera torque):")
print(f"  posto da controlabilidade: {posto_q} de 2  →  NÃO controlável")
print()
print("  Faz sentido: se a corrente não vira torque, a tensão nunca")
print("  alcança a velocidade. Você comanda o lado elétrico e o mecânico")
print("  fica solto, girando por conta própria.")
print()

try:
    ct.place(sys_quebrado.A, sys_quebrado.B, [-50, -60])
    print("  (a alocação passou — não deveria)")
except Exception as e:
    print(f"  E a alocação de polos falha, como tem que falhar:")
    print(f"    {type(e).__name__}: {str(e)[:70]}")
"""),

    md("""
## O que você leva desta aula

1. **Controlável** = com o comando que eu tenho, alcanço qualquer estado.
2. **Observável** = com os sensores que eu tenho, descubro tudo lá dentro.
   No NexaBot isso significa **um sensor de corrente a menos na conta**.
3. **Você escolhe os polos.** Realimentação de estados transforma "o sistema
   é assim" em "o sistema é como eu decidir".
4. **Mas o driver tem teto.** Todo projeto rápido demais pede tensão que não
   existe.
5. **Onde o teto aparece é uma decisão de engenharia, não de matemática.**

Isso fecha a Unidade 1. Você saiu de "o robô perde velocidade e ninguém sabe
por quê" para "eu tenho um modelo dos parâmetros medidos, sei o quão rápido
ele pode ser e sei onde a física me barra".

Na Unidade 2 você finalmente **fecha a malha**: mede, compara e corrige.

## Se deu erro

**`ValueError` na alocação de polos.**
Você pediu dois polos exatamente iguais. O algoritmo `place` não gosta disso.
Use valores levemente diferentes, como `[-50, -51]`.

**A varredura do Passo 3 demora.**
Ela simula sete malhas completas. Uns 10 segundos é normal. Se estiver
insuportável, aumente `dt` de `1e-4` para `5e-4`.

**Os picos deram diferentes dos meus.**
Confira se você não deixou `REFERENCIA` ou `TENSAO_MAX` alterados do "Mexa
aqui". Rode do começo (*Run → Restart Kernel and Run All Cells*).
""" + RODAPE_ERRO),
]
