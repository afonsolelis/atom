"""Notebook da Aula 8 — dois simuladores conversando."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import ABERTURA_IMPORTS, GLOSSARIO, RODAPE_ERRO, md, code  # noqa: E402

TITULO = "Aula 8 — Quando dois simuladores conversam"
SLUG = "cosimulacao"

CELULAS = [
    md("""
# Aula 8 — Quando dois simuladores conversam

## O que você vai fazer aqui

Até agora tudo rodou dentro do mesmo programa. Na vida real não é assim.

O time de mecânica simula o motor numa ferramenta. O time de software simula o
controlador em outra. As duas precisam conversar — e **é na conversa que o
erro nasce**.

Hoje você mede esse erro e vê ele crescer quando as duas ferramentas se falam
menos.

**Pré-requisito:** notebook da Aula 7.
"""),

    md("""
## Antes de começar

### 1. Por que dois simuladores separados?

Parece burrice ter dois. Mas pense em quem faz o trabalho:

- A **planta** (o motor, a mecânica, a física) é modelada pelo pessoal de
  engenharia mecânica, numa ferramenta boa para física.
- O **controlador** é escrito pelo pessoal de software, numa ferramenta boa
  para código.

Juntar tudo num programa só significaria um dos dois times abandonar sua
ferramenta. Na indústria isso não acontece: cada um fica com a sua, e elas
trocam informação.

Isso chama-se **co-simulação** — "simular junto".

### 2. A analogia dos dois remadores

Duas pessoas remam uma canoa, sentadas de costas uma para a outra, e **não
conseguem se ver**.

De tempos em tempos elas gritam: "estou remando assim!". Entre um grito e
outro, cada uma rema achando que a outra continua no mesmo ritmo.

- Gritam a cada 2 segundos → a canoa vai razoavelmente reta.
- Gritam a cada 30 segundos → a canoa faz zigue-zague.

O intervalo entre os gritos tem nome: **passo de comunicação**, escrito `H`.

### 3. O erro de acoplamento

O zigue-zague da canoa é o **erro de acoplamento**.

Ele não vem de nenhuma das duas ferramentas estar errada. As duas podem estar
perfeitas. Ele vem do **intervalo em que cada uma trabalha com informação
velha da outra**.

Quanto maior o `H`, maior o erro. É a única regra que você precisa levar
desta aula — e você vai medi-la.

### 4. FMU e FMI

Para dois programas diferentes conversarem, eles precisam falar a mesma
língua. A língua padrão da indústria chama-se **FMI** (*Functional Mock-up
Interface*), e um modelo empacotado nessa língua chama-se **FMU**.

Pense no FMU como um arquivo `.zip` que contém o modelo e sabe responder a
duas perguntas: *"aqui está a entrada, avance `H` segundos"* e *"qual é a sua
saída agora?"*.

Você não precisa saber como o FMU é feito por dentro. Precisa saber que ele
existe, que é padrão aberto, e que a indústria automotiva e aeroespacial o
usa de verdade.
"""),

    md(GLOSSARIO),

    md("""
## Passo 1 — Abrindo o FMU da planta

O laboratório desta disciplina traz a planta do NexaBot empacotada como FMU.

A célula abaixo carrega o arquivo e mostra o que ele expõe. Repare: são as
mesmas grandezas de sempre — tensão de entrada, carga, velocidade, corrente.
O FMU é só uma embalagem.
"""),
    code(ABERTURA_IMPORTS + r"""
from pathlib import Path
import numpy as np
from nexabot.params import PARAMS
from nexabot import cosim

print(f"Arquivo do FMU: {cosim.FMU_PATH.name}")
print(f"Existe: {cosim.FMU_PATH.exists()}")
print(f"Tamanho: {cosim.FMU_PATH.stat().st_size / 1024:.0f} kB")
print()
print("O que este FMU expõe para quem conversa com ele:")
print(f"  entrada  {cosim.VR_U_VOLTS}: tensão aplicada no motor [V]")
print(f"  entrada  {cosim.VR_TAU_LOAD}: torque de carga [N.m]")
print(f"  saída    {cosim.VR_OMEGA}: velocidade angular [rad/s]")
print(f"  saída    {cosim.VR_CURRENT}: corrente de armadura [A]")
print()
print("São as mesmas quatro grandezas das Aulas 1 e 2. Nada de novo na")
print("física — o que muda é que agora ela mora num arquivo separado, que")
print("outra ferramenta consegue abrir.")
"""),

    md("""
## Passo 2 — A primeira conversa

Agora rodamos a co-simulação: o FMU faz a planta, o Python faz o controlador,
e os dois trocam informação a cada `H` segundos.

Vamos começar com `H` igual ao período do controlador, 5 ms. É o caso bem
comportado.
"""),
    code(r"""
V_REF = 0.8      # m/s — velocidade linear desejada do robô

res = cosim.run_cosimulation(H=0.005, t_end=1.5, v_ref=V_REF)

omega_ref = PARAMS.v_to_omega(V_REF)
print(f"Referência: {V_REF} m/s  =  {omega_ref:.1f} rad/s")
print(f"Passo de comunicação H: {res.H*1000:.0f} ms")
print(f"Trocas de informação: {len(res.t)}")
print("-" * 50)
print(f"Velocidade final: {res.omega[-1]:.2f} rad/s "
      f"({PARAMS.omega_to_v(res.omega[-1]):.3f} m/s)")
print(f"Erro final:       {omega_ref - res.omega[-1]:.2f} rad/s")
print()
print("Funcionou. Duas ferramentas separadas produziram o mesmo controle")
print("que você já tinha na Aula 5 — só que agora a planta é um arquivo")
print("que qualquer outra ferramenta compatível com FMI consegue abrir.")
"""),

    md("""
## Passo 3 — O erro cresce com `H`

Aqui está a lição da aula.

Vamos rodar a mesma co-simulação com passos de comunicação cada vez maiores, e
comparar cada resultado com uma **referência**: a co-simulação de passo bem
pequeno, que consideramos "a verdade".

Antes de rodar, preveja: o erro cresce devagar ou rápido?
"""),
    code(r"""
# a "verdade": passo pequeno o bastante para o erro de acoplamento ser desprezível
ref = cosim.run_cosimulation(H=0.001, t_end=1.5, v_ref=V_REF)

def erro_contra_referencia(res_teste):
    # reamostra a referência nos instantes do teste, para comparar maçã com maçã
    omega_ref_interp = np.interp(res_teste.t, ref.t, ref.omega)
    return float(np.max(np.abs(res_teste.omega - omega_ref_interp)))

print(f"Referência: co-simulação com H = 1 ms")
print()
print(f"{'H':>8}  {'trocas':>8}  {'maior desvio':>14}  {'em % do alvo':>14}")
print("-" * 52)
resultados = {}
for H_ms in (1, 2, 5, 10, 20, 40):
    r = cosim.run_cosimulation(H=H_ms / 1000.0, t_end=1.5, v_ref=V_REF)
    resultados[H_ms] = r
    e = erro_contra_referencia(r)
    print(f"{H_ms:>5} ms  {len(r.t):>8}  {e:>12.2f}    {100*e/omega_ref:>12.2f}%")

print()
print("O erro cresce junto com H. Não é ruído, não é acaso: é o intervalo")
print("em que cada lado trabalha com informação velha do outro.")
"""),

    md("""
### O gráfico do zigue-zague

Duas curvas: a conversa frequente e a conversa rara.

A de passo grande não é "mais imprecisa" de um jeito difuso — ela tem uma
forma diferente, com sobressinal maior. O controlador está corrigindo com
base numa velocidade que já mudou.
"""),
    code(r"""
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(9.5, 5.5))
ax.axhline(omega_ref, color="#888888", linestyle="--", linewidth=1.2,
           label=f"alvo: {omega_ref:.0f} rad/s")

for H_ms, cor in ((1, "#4A9D5F"), (10, "#D68910"), (40, "#C0392B")):
    r = resultados[H_ms]
    ax.plot(r.t, r.omega, linewidth=2, color=cor,
            marker="o" if H_ms == 40 else None, markersize=3,
            label=f"H = {H_ms} ms ({len(r.t)} trocas)")

ax.set_xlabel("tempo [s]")
ax.set_ylabel("velocidade ω [rad/s]")
ax.set_title("Quanto mais raro o diálogo, pior o resultado", fontsize=13, pad=12)
ax.legend(loc="lower right"); ax.grid(alpha=0.25)
plt.tight_layout()
plt.show()
"""),

    md("""
## Passo 4 — Conferindo o FMU contra o modelo de referência

Uma pergunta legítima: **como sei que o FMU está certo?**

Ele foi gerado a partir do mesmo modelo, mas gerar código é um processo que
pode introduzir erro. Confiar sem conferir seria exatamente o oposto do que
esta disciplina prega.

A conferência é direta: aplica-se a mesma entrada nos dois — no FMU e no
`simulate` que você usa desde a Aula 1 — e compara-se a saída.
"""),
    code(r"""
from nexabot.plant import simulate

TENSAO = 12.0
T_FIM = 0.5
H = 0.001

# lado A: o FMU, avançado passo a passo.
# O `with` abre e fecha o FMU sozinho, como faria com um arquivo.
t_fmu, w_fmu = [], []
n = int(T_FIM / H)
with cosim.PlantaFMU(cosim.FMU_PATH) as planta:
    for k in range(n):
        planta.set_entradas(u_volts=TENSAO, tau_load=0.0)
        planta.do_step(k * H, H)
        omega, corrente = planta.get_saidas()
        t_fmu.append((k + 1) * H)
        w_fmu.append(omega)
t_fmu = np.array(t_fmu); w_fmu = np.array(w_fmu)

# lado B: o integrador Python das aulas anteriores
t_py, X_py = simulate(u_of_t=TENSAO, t_end=T_FIM, dt=1e-5)
w_py_interp = np.interp(t_fmu, t_py, X_py[:, 1])

erro = np.abs(w_fmu - w_py_interp)
print(f"Comparando FMU e modelo Python, degrau de {TENSAO} V:")
print("-" * 54)
print(f"  velocidade final pelo FMU:    {w_fmu[-1]:9.4f} rad/s")
print(f"  velocidade final pelo Python: {w_py_interp[-1]:9.4f} rad/s")
print(f"  maior diferença:              {erro.max():9.6f} rad/s")
print(f"  em termos relativos:          {100*erro.max()/w_fmu[-1]:9.4f}%")
print()
print("O FMU reproduz o modelo de referência. Agora ele pode ser entregue")
print("a outro time, em outra ferramenta, com evidência de que está certo.")
print("Isso é o que 'evidência' significa nesta disciplina: um número que")
print("alguém pode conferir, não uma afirmação.")
"""),

    md("""
## Mexa aqui

**Experimento 1 — o limite útil.**
Encontre o maior `H` que ainda mantém o desvio abaixo de 1% do alvo. Esse é o
seu orçamento de comunicação: se as duas ferramentas rodam em máquinas
diferentes, cada troca custa tempo de rede.

**Experimento 2 — com carga.**
Passe uma carga para `tau_load_of_t` e refaça. O erro de acoplamento piora?
Faz sentido: agora há mais coisa acontecendo entre uma conversa e outra.

**Experimento 3 — controlador mais agressivo.**
Suba `KP` para `1.0`. Um controlador que reage mais rápido é mais sensível a
informação velha, então o erro para um mesmo `H` deve crescer.
"""),
    code(r"""
# ⬇️ mexa aqui
H_MS = 10
KP = 0.30
KI = 6.0
COM_CARGA = False

def carga(t):
    return 0.15 if t >= 0.75 else 0.0

r_x = cosim.run_cosimulation(
    H=H_MS / 1000.0, t_end=1.5, v_ref=V_REF, Kp=KP, Ki=KI,
    tau_load_of_t=carga if COM_CARGA else None,
)
e_x = erro_contra_referencia(r_x)

print(f"H = {H_MS} ms   Kp = {KP}   Ki = {KI}   carga = {COM_CARGA}")
print("-" * 52)
print(f"trocas de informação : {len(r_x.t):6d}")
print(f"velocidade final     : {r_x.omega[-1]:9.2f} rad/s")
print(f"maior desvio         : {e_x:9.2f} rad/s ({100*e_x/omega_ref:.2f}%)")
print()
if 100 * e_x / omega_ref < 1.0:
    print("Abaixo de 1%. Este passo de comunicação serve.")
else:
    print("Acima de 1%. Converse com mais frequência (H menor).")
"""),

    md("""
## Aprofundamento (opcional)

### Se você for trabalhar com isto

O padrão FMI tem bastante coisa por dentro: a estrutura do arquivo `.fmu`, o
`modelDescription.xml` que descreve as variáveis, os tipos de dado e os modos
de acoplamento (Jacobi contra Gauss-Seidel).

Você não precisa de nada disso para entender **por que o erro nasce na
conversa**, que é a ideia daqui. Mas quem for integrar modelos de verdade vai
precisar — o padrão completo está no material complementar da unidade.

### Por que o erro cresce linearmente com H

O mestre de co-simulação usado aqui congela a entrada durante todo o passo de
comunicação — a planta recebe a mesma tensão do começo ao fim de `H`.

O erro cometido nesse congelamento é proporcional à taxa com que a grandeza
mudaria, vezes o intervalo. Ou seja, proporcional a `H`. Métodos mais
espertos extrapolam a entrada em vez de congelar, e aí o erro passa a cair
com `H²` — mas custam mais e podem instabilizar.

A célula abaixo confirma a linearidade nos números que você já mediu.
"""),
    code(r"""
# H = 1 ms fica de fora: ele É a referência, então o erro dele contra si
# mesmo é zero por construção, não por mérito.
Hs = np.array([2, 5, 10, 20, 40], dtype=float)
erros = np.array([erro_contra_referencia(resultados[int(h)]) for h in Hs])

print(f"{'H [ms]':>8}  {'erro':>9}  {'erro / H':>10}")
print("-" * 32)
for h, e in zip(Hs, erros):
    print(f"{h:>8.0f}  {e:>9.3f}  {e/h:>10.4f}")

razoes = erros / Hs
print()
print(f"A última coluna varia entre {razoes.min():.2f} e {razoes.max():.2f} —")
print("fica na mesma ordem de grandeza enquanto o H cresce 20 vezes.")
print("Não é constante perfeita, mas é claramente linear, não quadrática:")
print("se fosse quadrática, essa coluna cresceria junto com H.")
print()
print("Utilidade prática: se você mediu o erro para um H, sabe estimar")
print("para outro sem rodar de novo. Dobrou H, dobrou o erro.")
"""),

    md("""
## O que você leva desta aula

1. **Co-simulação é rodar planta e controlador em ferramentas separadas**, que
   trocam informação de tempos em tempos.
2. **Existe porque times diferentes usam ferramentas diferentes**, e ninguém
   vai abrir mão da sua.
3. **`H` é o passo de comunicação** — o intervalo entre dois "gritos" dos
   remadores.
4. **O erro de acoplamento cresce com `H`**, de forma aproximadamente linear.
   Nenhuma das ferramentas está errada: o erro está no intervalo.
5. **FMU é o formato padrão** para empacotar um modelo e entregá-lo a outro
   time.
6. **Modelo entregue vem com conferência.** Você comparou o FMU contra o
   modelo de referência e mediu a diferença.

Isso fecha a Unidade 2. Você saiu de "malha aberta não funciona" para um
controlador sintonizado, discretizado e rodando em co-simulação com a planta.

Na Unidade 3 a pergunta muda: em vez de *"funciona?"*, passa a ser
**"como eu provo que funciona?"**.

## Se deu erro

**`FileNotFoundError` no FMU.**
O arquivo fica em `nexabot/fmu/NexaBotPlant.fmu`. Se não existir, rode
`python aula_08/01_gerar_fmu.py` a partir de `projeto_nexabot/`.

**`ModuleNotFoundError: No module named 'fmpy'`.**
Falta a biblioteca que lê FMU:
`uv pip install --python .venv/bin/python fmpy`.

**A varredura demora.**
Cada co-simulação abre e fecha o FMU. Uns 30 a 60 segundos no total. Reduza
`t_end` para `1.0` se precisar.

**O erro deu zero para todos os H.**
Você provavelmente comparou a referência com ela mesma. Confira se `ref` foi
gerado com `H=0.001`.
""" + RODAPE_ERRO),
]
