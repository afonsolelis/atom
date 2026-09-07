"""Notebook da Aula 5 — medir, comparar, corrigir."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import ABERTURA_IMPORTS, GLOSSARIO, RODAPE_ERRO, md, code  # noqa: E402

TITULO = "Aula 5 — Medir, comparar, corrigir"
SLUG = "malha_fechada"

CELULAS = [
    md("""
# Aula 5 — Medir, comparar, corrigir

## O que você vai fazer aqui

Na Aula 1 o robô perdeu 33% da velocidade quando a carga apareceu, e ninguém
percebeu. Hoje você conserta isso.

A correção cabe em três palavras: **medir, comparar, corrigir**. Você vai
implementar isso em umas dez linhas e ver a mesma carga que derrubou o robô
não derrubar mais nada.

**Pré-requisito:** notebooks das Aulas 1 a 4.
"""),

    md("""
## Antes de começar

### 1. Realimentação — você já usa isso todo dia

Você toma banho assim:

1. Abre o registro num ponto qualquer.
2. **Mede** a temperatura com a mão.
3. **Compara** com a que você queria.
4. **Corrige** — mexe no registro.
5. Repete, o banho inteiro.

Isso é realimentação. E repare no ponto essencial: **você não precisa saber
nada sobre o aquecedor**. Não precisa saber se ele é a gás ou elétrico, se o
vizinho abriu a torneira, se a pressão caiu. Você mede o resultado e corrige.

Um termostato faz igual: mede a temperatura, compara com a desejada, liga ou
desliga.

Na Aula 1 você fez o contrário: abriu o registro num ponto e foi embora. Se a
água esfriasse, azar.

### 2. Erro

**Erro** é a palavra técnica para "a diferença entre o que eu queria e o que
eu tenho":

$$
e = r - y
$$

- $r$ é a **referência** (o que você quer) — lê-se "erre"
- $y$ é a **saída medida** (o que você tem)
- $e$ é o **erro**

Se você quer 200 rad/s e o encoder mede 170, o erro é 30. O controlador olha
para esse 30 e decide o que fazer.

Erro positivo = está devagar demais, acelera. Erro negativo = está rápido
demais, alivia. É literalmente isso.

### 3. Regime permanente

**Regime permanente** é "depois que parou de balançar".

Todo sistema tem um período de agitação quando você muda alguma coisa
(chamado *transitório*) e depois assenta num valor. O regime permanente é esse
valor final.

A pergunta que importa: **o erro em regime permanente é zero?** Ou seja,
depois que tudo assentou, o robô ficou na velocidade que você pediu, ou ficou
perto e desistiu?
"""),

    md(GLOSSARIO),

    md("""
## Passo 1 — Relembrando o problema

Primeiro, reproduza a falha da Aula 1. Mesma carga, mesmo comando fixo.

Este é o "antes".
"""),
    code(ABERTURA_IMPORTS + r"""
import numpy as np
from nexabot.params import PARAMS
from nexabot.plant import simulate

ALVO = 200.0             # rad/s — a velocidade que queremos
CARGA = 0.15             # N.m — a rampa que aparece em 1 s

# Em malha aberta você calcula a tensão UMA vez, pelo ganho estático,
# e reza para a carga não mudar.
tensao_calculada = ALVO / PARAMS.dc_gain

def carga(tempo):
    return CARGA if tempo >= 1.0 else 0.0

t_ma, X_ma = simulate(u_of_t=tensao_calculada, t_end=2.0, tau_load_of_t=carga)
w_ma = X_ma[:, 1]

print(f"Alvo:                    {ALVO:.1f} rad/s")
print(f"Tensão calculada:        {tensao_calculada:.2f} V")
print("-" * 46)
print(f"Antes da carga (1 s):    {w_ma[int(len(t_ma)*0.49)]:.2f} rad/s")
print(f"Depois da carga (2 s):   {w_ma[-1]:.2f} rad/s")
print(f"Erro final:              {ALVO - w_ma[-1]:.2f} rad/s")
print()
print("A malha aberta acertou o alvo enquanto nada mudou, e errou feio")
print("assim que a carga entrou. Ela não tem como saber que errou.")
"""),

    md("""
## Passo 2 — Fechando a malha em dez linhas

Agora o conserto.

A cada 5 milissegundos o controlador vai:

1. **medir** a velocidade,
2. **comparar** com o alvo (calcular o erro),
3. **corrigir** — somar um pouco de tensão proporcional ao erro.

O "um pouco" é o ganho `Kp`. Se `Kp = 0.1`, cada rad/s de erro vira 0,1 V a
mais de comando.

Leia o laço abaixo. São dez linhas, e elas são a Unidade 2 inteira em
miniatura.
"""),
    code(r"""
def malha_fechada(Kp, alvo=ALVO, carga_nm=CARGA, t_end=2.0, Ts=PARAMS.Ts):
    '''Controlador proporcional simples, rodando a cada Ts segundos.'''
    n_passos = int(t_end / Ts)
    x = np.zeros(2)                     # [corrente, velocidade]
    ts, ws, us, es = [], [], [], []

    for k in range(n_passos):
        tempo = k * Ts
        y = x[1]                        # 1. MEDIR a velocidade
        e = alvo - y                    # 2. COMPARAR com o alvo
        u = Kp * e                      # 3. CORRIGIR
        u = float(np.clip(u, -PARAMS.V_max, PARAMS.V_max))   # o driver tem teto

        tau = carga_nm if tempo >= 1.0 else 0.0
        _, Xk = simulate(u_of_t=u, t_end=Ts, dt=Ts / 50, x0=x, tau_load_of_t=tau)
        x = Xk[-1]

        ts.append(tempo); ws.append(y); us.append(u); es.append(e)

    return np.array(ts), np.array(ws), np.array(us), np.array(es)


t_mf, w_mf, u_mf, e_mf = malha_fechada(Kp=0.5)

print(f"Malha fechada com Kp = 0.5")
print("-" * 46)
print(f"Antes da carga (1 s):    {w_mf[int(len(t_mf)*0.49)]:.2f} rad/s")
print(f"Depois da carga (2 s):   {w_mf[-1]:.2f} rad/s")
print(f"Erro final:              {ALVO - w_mf[-1]:.2f} rad/s")
print()
print(f"Em malha aberta o erro final era de {ALVO - w_ma[-1]:.1f} rad/s.")
print(f"Agora é de {ALVO - w_mf[-1]:.1f}. O controlador percebeu a carga e reagiu.")
"""),

    md("""
### Veja os dois lado a lado

O gráfico de cima mostra as duas velocidades. O de baixo mostra a **tensão
comandada** — e é aí que mora a diferença.

Em malha aberta a tensão é uma linha reta: o comando nunca muda, porque
ninguém está olhando.

Em malha fechada a tensão **sobe sozinha** no instante em que a carga entra. O
controlador não sabe que existe uma carga; ele só viu a velocidade cair e
reagiu. Isso é o essencial da realimentação: ela conserta problemas que você
não previu.
"""),
    code(r"""
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9.5, 7), sharex=True)

ax1.axhline(ALVO, color="#888888", linestyle="--", linewidth=1.2, label="alvo: 200 rad/s")
ax1.plot(t_ma, w_ma, color="#C0392B", linewidth=2, label="malha aberta")
ax1.plot(t_mf, w_mf, color="#4A9D5F", linewidth=2, label="malha fechada (Kp = 0,5)")
ax1.axvline(1.0, color="#555555", linestyle=":", linewidth=1.2)
ax1.set_ylabel("velocidade ω [rad/s]")
ax1.set_title("A carga entra em 1 s. Uma das duas percebe.", fontsize=12)
ax1.legend(loc="lower left"); ax1.grid(alpha=0.25)

ax2.axhline(tensao_calculada, color="#C0392B", linewidth=2, label="malha aberta: fixa")
ax2.plot(t_mf, u_mf, color="#4A9D5F", linewidth=2, label="malha fechada: reage")
ax2.axvline(1.0, color="#555555", linestyle=":", linewidth=1.2)
ax2.set_ylabel("tensão comandada [V]")
ax2.set_xlabel("tempo [s]")
ax2.set_title("O comando: um é reta, o outro responde", fontsize=12)
ax2.legend(loc="lower left"); ax2.grid(alpha=0.25)

plt.tight_layout()
plt.show()
"""),

    md("""
## Passo 3 — O erro que sobra

Olhe de novo o número do erro final da malha fechada. Ele diminuiu muito, mas
**não zerou**.

Por que não? Aqui está a lógica, e ela é bonita:

O comando é $u = K_p \\cdot e$. Para o robô vencer a carga, ele precisa de um
comando maior que zero. Mas se o erro fosse zero, o comando seria zero. Logo,
**o erro não pode zerar** — ele é justamente o que sustenta o comando.

O controlador proporcional vive de erro. Sem erro, ele não faz nada.

Aumentar `Kp` reduz o erro que sobra (menos erro produz o mesmo comando), mas
nunca chega a zero. A célula abaixo mostra isso.
"""),
    code(r"""
print(f"{'Kp':>8}  {'ω final':>12}  {'erro que sobra':>16}")
print("-" * 42)
for Kp in (0.1, 0.25, 0.5, 1.0, 2.0):
    _, w, _, _ = malha_fechada(Kp=Kp)
    erro_final = ALVO - w[-1]
    print(f"{Kp:>8.2f}  {w[-1]:>10.2f}    {erro_final:>12.2f} rad/s")

print()
print("O erro encolhe pela metade cada vez que Kp dobra. Encolhe,")
print("encolhe... e nunca zera. Ele não pode zerar: é ele que sustenta")
print("o comando que vence a carga.")
print()
print("E não adianta continuar subindo Kp. Rode a célula seguinte.")
"""),

    md("""
### Subir Kp não é a saída

A tentação óbvia é aumentar `Kp` até o erro sumir. Não funciona, e a célula
abaixo mostra por quê.

Com `Kp` alto o controlador reage com violência a qualquer diferença. Ele
corrige, passa do ponto, corrige para o outro lado, passa de novo. O sistema
**oscila** e nunca assenta.

Repare na última coluna: ela mede o quanto a velocidade ainda está balançando
no fim da simulação. Enquanto ela for zero, o robô assentou. Quando ela cresce,
ele está balançando para sempre.
"""),
    code(r"""
print(f"{'Kp':>8}  {'ω final':>10}  {'erro':>9}  {'ainda balança?':>16}")
print("-" * 50)
for Kp in (0.5, 1.0, 2.0, 5.0, 10.0):
    _, w, _, _ = malha_fechada(Kp=Kp, t_end=3.0)
    balanco = w[-20:].std()
    marca = "assentou" if balanco < 0.01 else f"±{balanco:.1f} rad/s"
    print(f"{Kp:>8.1f}  {w[-1]:>10.2f}  {ALVO - w[-1]:>9.2f}  {marca:>16}")

print()
print("De Kp = 5 em diante o robô para de assentar: ele oscila em torno do")
print("alvo, sem parar. Num armazém isso é um robô tremendo no corredor.")
print()
print("Ou seja: Kp alto troca um problema por outro. O erro que sobra")
print("continua lá, e agora com oscilação de brinde.")
"""),

    md("""
## Passo 4 — A memória que zera o erro

A solução é dar **memória** ao controlador.

Além de olhar o erro de agora, ele passa a acumular todos os erros passados.
Esse acumulado se chama **integral**, e o termo entra assim:

$$
u = \\underbrace{K_p \\cdot e}_{\\text{o erro de agora}} + \\underbrace{K_i \\int e \\, dt}_{\\text{a soma de todos os erros}}
$$

Por que isso resolve? Porque **enquanto houver erro, a soma continua
crescendo**, e o comando continua subindo. O único jeito de o comando parar de
crescer é o erro chegar a zero. O sistema é obrigado a acertar o alvo.

Em código, "integral" é uma variável que você vai somando. Duas linhas.
"""),
    code(r"""
def malha_fechada_pi(Kp, Ki, alvo=ALVO, carga_nm=CARGA, t_end=2.0, Ts=PARAMS.Ts):
    '''Proporcional + Integral: agora com memória.'''
    n_passos = int(t_end / Ts)
    x = np.zeros(2)
    integral = 0.0                      # ← a memória
    ts, ws, us = [], [], []

    for k in range(n_passos):
        tempo = k * Ts
        y = x[1]
        e = alvo - y
        integral += Ki * Ts * e         # ← acumula o erro
        u = Kp * e + integral
        u = float(np.clip(u, -PARAMS.V_max, PARAMS.V_max))

        tau = carga_nm if tempo >= 1.0 else 0.0
        _, Xk = simulate(u_of_t=u, t_end=Ts, dt=Ts / 50, x0=x, tau_load_of_t=tau)
        x = Xk[-1]
        ts.append(tempo); ws.append(y); us.append(u)

    return np.array(ts), np.array(ws), np.array(us)


t_pi, w_pi, u_pi = malha_fechada_pi(Kp=0.3, Ki=8.0)

print(f"{'controlador':>28}  {'ω final':>10}  {'erro':>10}")
print("-" * 54)
print(f"{'malha aberta':>28}  {w_ma[-1]:>8.2f}  {ALVO - w_ma[-1]:>8.2f}")
print(f"{'proporcional (Kp=0,5)':>28}  {w_mf[-1]:>8.2f}  {ALVO - w_mf[-1]:>8.2f}")
print(f"{'proporcional + integral':>28}  {w_pi[-1]:>8.2f}  {ALVO - w_pi[-1]:>8.2f}")
print()
print("Zero. Não 'quase zero': zero, dentro da precisão da conta.")
print("A carga continua lá. O robô simplesmente passou a compensá-la.")
"""),

    md("""
### O gráfico do conserto

Três curvas, três gerações do mesmo robô.

Repare no que acontece depois de 1 s na curva verde: ela **cai e volta**. Esse
mergulho é o controlador percebendo a carga e reagindo. Ele não some — mas
não sobra.
"""),
    code(r"""
fig, ax = plt.subplots(figsize=(9.5, 5.5))

ax.axhline(ALVO, color="#888888", linestyle="--", linewidth=1.2, label="alvo: 200 rad/s")
ax.plot(t_ma, w_ma, color="#C0392B", linewidth=2, label="malha aberta")
ax.plot(t_mf, w_mf, color="#D68910", linewidth=2, label="proporcional")
ax.plot(t_pi, w_pi, color="#4A9D5F", linewidth=2.5, label="proporcional + integral")
ax.axvline(1.0, color="#555555", linestyle=":", linewidth=1.2)
ax.annotate("a carga entra", xy=(1.0, 60), xytext=(1.08, 45), fontsize=10,
            color="#555555")

ax.set_xlabel("tempo [s]")
ax.set_ylabel("velocidade ω [rad/s]")
ax.set_title("Três gerações do mesmo robô", fontsize=13, pad=12)
ax.set_ylim(0, ALVO * 1.25)
ax.legend(loc="lower left"); ax.grid(alpha=0.25)
plt.tight_layout()
plt.show()
"""),

    md("""
## Mexa aqui

**Experimento 1 — integral fraca demais.**
Baixe `Ki` de `8.0` para `0.5`. O erro ainda zera? Zera, mas demora uma
eternidade. A memória existe, só que ela esquece devagar.

**Experimento 2 — integral forte demais.**
Suba `Ki` para `80`. Agora o robô passa do alvo e volta, passa e volta. Isso
chama-se **sobressinal** (*overshoot*), e é o preço de reagir com pressa
demais. Num robô de armazém, sobressinal significa passar do ponto de parada.

**Experimento 3 — carga muito maior.**
Deixe `Kp=0.3, Ki=8.0` e suba a carga para `0.6` N.m. O erro ainda zera? Se
não, olhe a tensão comandada: você provavelmente esbarrou nos 24 V de novo. Aí
não existe controlador que resolva — falta motor.
"""),
    code(r"""
# ⬇️ mexa aqui
KP = 0.3
KI = 8.0
CARGA_TESTE = 0.15

t_x, w_x, u_x = malha_fechada_pi(Kp=KP, Ki=KI, carga_nm=CARGA_TESTE)

erro_final = ALVO - w_x[-1]
sobressinal = 100 * (w_x.max() - ALVO) / ALVO

# Saturar na PARTIDA é normal e esperado: o robô sai do zero, o erro é o
# alvo inteiro, e o controlador pede tudo o que pode. O que interessa é se
# ele ainda está saturado DEPOIS que a carga entrou, em 1 s.
depois_da_carga = t_x >= 1.0
satura_no_regime = np.any(np.abs(u_x[depois_da_carga]) >= PARAMS.V_max - 1e-9)

print(f"Kp = {KP}   Ki = {KI}   carga = {CARGA_TESTE} N.m")
print("-" * 50)
print(f"velocidade final : {w_x[-1]:8.2f} rad/s")
print(f"erro final       : {erro_final:8.2f} rad/s")
print(f"sobressinal      : {max(sobressinal, 0):8.1f}%")
print(f"pico na partida  : {np.abs(u_x).max():8.2f} V  (teto: {PARAMS.V_max} V)")
print(f"pico após a carga: {np.abs(u_x[depois_da_carga]).max():8.2f} V")
print()
if satura_no_regime:
    print("⚠ O driver está saturado mesmo depois que tudo assentou.")
    print("  O controlador pede mais do que existe. Nenhum ajuste de Kp ou")
    print("  Ki resolve isso — falta motor.")
else:
    print("O driver satura só na partida, o que é normal: saindo do zero, o")
    print("erro é o alvo inteiro e o controlador pede tudo o que pode. Depois")
    print("que assenta, ele opera com folga.")
"""),

    md("""
## Aprofundamento (opcional)

### A fórmula exata do erro que sobra

Dá para prever o erro do controlador proporcional sem simular nada. Iguale as
duas equações da Aula 2 a zero (regime permanente), substitua
$u = K_p(r - \\omega)$ e isole:

$$
e_\\infty \\;=\\; \\frac{c\\,r \\;+\\; \\tau_{\\text{carga}}}{a + c}
\\qquad\\text{com}\\quad
a = \\frac{K_t K_p}{R}, \\quad c = \\frac{K_t K_e}{R} + b
$$

Repare que o erro tem **duas parcelas somadas**: uma que vem da referência
($c\\,r$) e outra que vem da carga ($\\tau$). São dois problemas distintos, e o
proporcional falha nos dois.

Quando $K_p$ cresce, $a$ cresce junto e o erro encolhe — mas o numerador nunca
some. Por isso o erro tende a zero sem nunca chegar.

### Por que a integral zera, formalmente

Com o integrador, o controlador tem $C(s) = K_p + \\frac{K_i}{s}$. Em $s = 0$
isso vai a infinito, e é isso que zera o erro: o "$a$" da fórmula acima vira
infinito, e qualquer numerador finito dividido por infinito dá zero.

O integrador coloca um infinito no lugar certo.

### Se você quiser ir além

Existe um jeito mais formal de analisar malha fechada, com as **funções de
sensibilidade $S$ e complementar $T$** e a classificação por **tipo de
sistema**. São ferramentas boas, e estão no material complementar da unidade.

Elas pedem que você já esteja confortável com resposta em frequência, que só
aparece na Aula 7. A conclusão prática de que você precisa hoje já está aqui:
**com integrador, o erro em regime vai a zero**.
"""),
    code(r"""
import control as ct
from nexabot.plant import transfer_function

c = PARAMS.Kt * PARAMS.Ke / PARAMS.R + PARAMS.b

print("Erro previsto pela fórmula, contra o erro medido simulando:")
print()
print(f"{'Kp':>6}  {'por referência':>16}  {'pela carga':>12}  "
      f"{'total previsto':>15}  {'medido':>9}")
print("-" * 68)
for Kp in (0.5, 1.0, 2.0):
    a = PARAMS.Kt * Kp / PARAMS.R
    parcela_ref = c * ALVO / (a + c)
    parcela_carga = CARGA / (a + c)
    _, w, _, _ = malha_fechada(Kp=Kp)
    print(f"{Kp:>6.1f}  {parcela_ref:>14.2f}  {parcela_carga:>12.2f}  "
          f"{parcela_ref + parcela_carga:>15.2f}  {ALVO - w[-1]:>9.2f}")

print()
print("Bate na segunda casa decimal. E veja a decomposição: com Kp = 0,5,")
print("uns 17 rad/s de erro vêm de não conseguir seguir a referência, e")
print("uns 7 vêm da carga. São dois problemas somados.")
"""),

    md("""
## O que você leva desta aula

1. **Realimentação é medir, comparar, corrigir.** Você já faz isso no chuveiro.
2. **Ela conserta problemas que você não previu.** O controlador não sabe que
   existe uma carga; ele só vê a velocidade cair.
3. **Proporcional sozinho deixa erro.** Ele *precisa* de erro para produzir
   comando.
4. **A integral zera o erro** porque acumula enquanto houver erro.
5. **Integral demais causa sobressinal.** Tudo em controle é troca.
6. **Se o driver satura, nenhum ganho resolve.** Aí falta motor, não ajuste.

Na Aula 6 entra a terceira letra — o **D** — e a sintonia deixa de ser
tentativa e erro.

## Se deu erro

**A simulação demora muito.**
Cada malha simula 400 passos, e cada passo roda um integrador. Uns 5 a 15
segundos por célula. Se ficar insuportável, reduza `t_end` para `1.5`.

**O robô oscilou até explodir.**
Você provavelmente pôs `Ki` alto demais. Volte para `8.0`.

**O erro final deu negativo.**
Significa que o robô passou do alvo e ficou acima. Com integral isso acontece
transitoriamente; se persistir no fim, seu `Ki` está alto.
""" + RODAPE_ERRO),
]
