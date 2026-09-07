"""Notebook da Aula 6 — PID: três ajustes e o erro que quebra tudo."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import ABERTURA_IMPORTS, GLOSSARIO, RODAPE_ERRO, md, code  # noqa: E402

TITULO = "Aula 6 — P, I e D: três ajustes, três personalidades"
SLUG = "pid_na_pratica"

CELULAS = [
    md("""
# Aula 6 — P, I e D: três ajustes, três personalidades

## O que você vai fazer aqui

Na Aula 5 você usou dois ajustes: o P e o I. Hoje entra o terceiro, o D, e
você vai ver **cada um sozinho** antes de juntar os três.

Depois vai cometer, de propósito, o erro mais comum de quem programa PID em
sistema real — e consertá-lo.

**Tempo:** cerca de 40 minutos.
**Pré-requisito:** notebook da Aula 5.
"""),

    md("""
## Antes de começar

### PID em português

PID são três contas somadas. Cada uma olha o erro de um jeito diferente.

| Letra | Nome | O que ela faz | Analogia |
| --- | --- | --- | --- |
| **P** | Proporcional | Reage ao erro **de agora** | Você está longe do destino? Acelera proporcionalmente. |
| **I** | Integral | Lembra do erro **acumulado** | "Faz meia hora que estou atrasado" — a pressa cresce. |
| **D** | Derivativo | Antecipa **para onde o erro vai** | Você vê o carro da frente freando e já tira o pé. |

Somando as três:

$$
u = \\underbrace{K_p\\, e}_{\\text{agora}} \\;+\\; \\underbrace{K_i \\!\\int\\! e\\,dt}_{\\text{o passado}} \\;+\\; \\underbrace{K_d\\, \\frac{de}{dt}}_{\\text{o futuro}}
$$

Presente, passado e futuro. É literalmente essa a divisão de trabalho.

### O que cada um estraga

Nenhum é de graça:

- **P demais** → oscila (você viu na Aula 5).
- **I demais** → passa do alvo e demora a voltar.
- **D demais** → fica nervoso, amplifica o ruído do sensor.

Sintonizar um PID é escolher o ponto de equilíbrio entre esses três defeitos.

### Windup — o erro que você vai cometer hoje

Este é o assunto principal da aula, e ele só existe porque o mundo real tem
limites.

Imagine: o robô está saindo do zero para 200 rad/s. O erro é enorme. O termo
integral vai **somando** esse erro enorme, e o comando vai crescendo: 30 V,
50 V, 80 V...

Mas o driver só entrega 24 V. Os 56 V a mais são fictícios — só existem dentro
da variável.

Quando o robô finalmente chega ao alvo, o integral está carregadíssimo. Ele
continua mandando comando alto mesmo com erro zero, e o robô **passa do
ponto** — e leva um tempão para voltar, porque o integral precisa descarregar.

Isso se chama **windup** (algo como "dar corda"). E a correção tem nome
também: **anti-windup**.
"""),

    md(GLOSSARIO),

    md("""
## Passo 1 — Cada letra, sozinha

Antes de misturar, veja cada termo trabalhando isolado.

Vamos usar a classe `DiscretePID` do projeto, que é a mesma que na Unidade 4
vira código C embarcado. Zerando dois dos três ganhos, sobra um.
"""),
    code(ABERTURA_IMPORTS + r"""
import numpy as np
from nexabot.params import PARAMS
from nexabot.plant import simulate
from nexabot.controllers import DiscretePID

ALVO = 200.0

def rodar(pid, t_end=1.5, carga_nm=0.0, instante_carga=1.0):
    '''Roda a malha fechada com o PID dado. Devolve tempo, velocidade e comando.'''
    n = int(t_end / PARAMS.Ts)
    x = np.zeros(2)
    ts = np.zeros(n); ws = np.zeros(n); us = np.zeros(n)
    for k in range(n):
        tempo = k * PARAMS.Ts
        y = x[1]
        u = pid.step(ALVO, y)
        tau = carga_nm if tempo >= instante_carga else 0.0
        _, Xk = simulate(u_of_t=u, t_end=PARAMS.Ts, dt=PARAMS.Ts / 40,
                         x0=x, tau_load_of_t=tau)
        x = Xk[-1]
        ts[k] = tempo; ws[k] = y; us[k] = u
    return ts, ws, us


casos = {
    "só P  (Kp=0,3)":        DiscretePID(Kp=0.3, Ki=0.0, Kd=0.0),
    "só I  (Ki=8)":          DiscretePID(Kp=0.0, Ki=8.0, Kd=0.0),
    "P + I (Kp=0,3, Ki=8)":  DiscretePID(Kp=0.3, Ki=8.0, Kd=0.0),
}

resultados = {}
print(f"{'controlador':>24}  {'ω final':>9}  {'erro':>8}  {'sobressinal':>12}")
print("-" * 60)
for nome, pid in casos.items():
    t, w, u = rodar(pid)
    resultados[nome] = (t, w, u)
    sobre = max(0.0, 100 * (w.max() - ALVO) / ALVO)
    print(f"{nome:>24}  {w[-1]:>9.2f}  {ALVO - w[-1]:>8.2f}  {sobre:>11.1f}%")
"""),

    md("""
### Lendo a tabela

- **Só P**: chega perto, mas para antes do alvo. Já era esperado da Aula 5 —
  o proporcional vive de erro.
- **Só I**: chega no alvo (a memória não desiste), mas passa do ponto no
  caminho. O integral é teimoso e lento.
- **P + I**: o P dá a resposta rápida, o I fecha o erro. Juntos são melhores
  que qualquer um sozinho.

O gráfico deixa as três personalidades óbvias.
"""),
    code(r"""
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(9.5, 5.5))
cores = {"só P  (Kp=0,3)": "#D68910",
         "só I  (Ki=8)": "#5B8DBE",
         "P + I (Kp=0,3, Ki=8)": "#4A9D5F"}

ax.axhline(ALVO, color="#888888", linestyle="--", linewidth=1.2, label="alvo")
for nome, (t, w, u) in resultados.items():
    ax.plot(t, w, linewidth=2, color=cores[nome], label=nome)

ax.set_xlabel("tempo [s]")
ax.set_ylabel("velocidade ω [rad/s]")
ax.set_title("Três personalidades", fontsize=13, pad=12)
ax.legend(loc="lower right"); ax.grid(alpha=0.25)
plt.tight_layout()
plt.show()
"""),

    md("""
## Passo 2 — E o D?

O termo derivativo olha **a que velocidade o erro está mudando**.

Se o erro está caindo rápido, o D diz: "calma, você vai passar do ponto,
alivia". Ele funciona como um amortecedor.

O problema é que derivada amplifica ruído. Um sensor que treme um pouquinho
vira um comando que treme muito. Por isso, na prática, **nunca se usa o D
puro**: usa-se um D filtrado, que é o que a classe `DiscretePID` implementa.

A célula abaixo acrescenta o D e mede o efeito no sobressinal.
"""),
    code(r"""
comparacao = {
    "P + I":      DiscretePID(Kp=0.3, Ki=8.0, Kd=0.0),
    "P + I + D":  DiscretePID(Kp=0.3, Ki=8.0, Kd=0.004),
}

res_d = {}
print(f"{'controlador':>12}  {'sobressinal':>12}  {'ω final':>9}")
print("-" * 40)
for nome, pid in comparacao.items():
    t, w, u = rodar(pid)
    res_d[nome] = (t, w, u)
    sobre = max(0.0, 100 * (w.max() - ALVO) / ALVO)
    print(f"{nome:>12}  {sobre:>11.1f}%  {w[-1]:>9.2f}")

print()
print("O D corta parte do sobressinal sem estragar o resto. Ele é o")
print("amortecedor da equipe: não acelera nada, só evita o exagero.")
"""),

    md("""
## Passo 3 — O windup, ao vivo

Agora o erro que a aula existe para mostrar.

A `DiscretePID` do projeto tem anti-windup embutido, controlado pelo ganho
`Kaw`. Colocando `Kaw = 0`, você desliga a proteção e vê o problema
acontecer.

Vamos pedir uma partida agressiva — `Ki` alto, saindo do zero — que é
exatamente a situação em que o driver satura.

Antes de rodar, preveja: qual das duas curvas vai passar mais do alvo?
"""),
    code(r"""
ALVO = 300.0     # bem alto: força o driver a ficar no teto por bastante tempo

sem_protecao = DiscretePID(Kp=0.15, Ki=40.0, Kd=0.0, Kaw=0.0)
com_protecao = DiscretePID(Kp=0.15, Ki=40.0, Kd=0.0, Kaw=100.0)

t_sem, w_sem, u_sem = rodar(sem_protecao, t_end=3.0)
t_com, w_com, u_com = rodar(com_protecao, t_end=3.0)

def resumo(nome, t, w, u):
    sobre = max(0.0, 100 * (w.max() - ALVO) / ALVO)
    # tempo até entrar e ficar dentro de 2% do alvo
    fora = np.where(np.abs(w - ALVO) > 0.02 * ALVO)[0]
    t_acomoda = t[fora[-1] + 1] if len(fora) and fora[-1] + 1 < len(t) else 0.0
    ciclos_teto = int(np.sum(np.abs(u) >= PARAMS.V_max - 1e-9))
    print(f"{nome:>16}  sobressinal {sobre:>6.1f}%   "
          f"acomodou em {t_acomoda:>5.2f} s   "
          f"{ciclos_teto:>4d} ciclos no teto")

print(f"Alvo: {ALVO} rad/s   |   Driver: {PARAMS.V_max} V")
print("-" * 78)
resumo("SEM anti-windup", t_sem, w_sem, u_sem)
resumo("COM anti-windup", t_com, w_com, u_com)
print()
print("Sem proteção o robô passa 8 vezes mais do alvo e leva 3 vezes mais")
print("tempo para assentar. É o mesmo controlador, os mesmos ganhos Kp e Ki.")
print("A única diferença são as duas linhas do anti-windup.")
"""),

    md("""
### O gráfico que explica

Olhe os dois painéis juntos — é a leitura dos dois que conta a história.

**Painel de baixo (o comando).** A linha vermelha fica grudada no teto de 24 V
por muito mais tempo. Não é que ela queira 24 V: ela quer muito mais, e o
driver corta. Todo esse excesso está sendo acumulado no integral.

**Painel de cima (a velocidade).** A vermelha passa do alvo e demora a voltar.
Ela não consegue voltar antes: o integral precisa *descarregar* todo o excesso
que guardou, e isso leva tempo.

A curva verde tem anti-windup: sempre que o comando é cortado, ela desconta a
diferença do integral. O integral nunca guarda o que não foi entregue.
"""),
    code(r"""
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9.5, 7.5), sharex=True)

ax1.axhline(ALVO, color="#888888", linestyle="--", linewidth=1.2, label="alvo")
ax1.plot(t_sem, w_sem, color="#C0392B", linewidth=2, label="sem anti-windup")
ax1.plot(t_com, w_com, color="#4A9D5F", linewidth=2, label="com anti-windup")
ax1.set_ylabel("velocidade ω [rad/s]")
ax1.set_title("O robô passa do ponto — e demora a voltar", fontsize=12)
ax1.legend(loc="lower right"); ax1.grid(alpha=0.25)

ax2.axhline(PARAMS.V_max, color="#333333", linestyle="--", linewidth=1.5)
ax2.text(1.25, PARAMS.V_max - 3.2, "teto do driver", fontsize=9.5, color="#333333")
ax2.plot(t_sem, u_sem, color="#C0392B", linewidth=2, label="sem anti-windup")
ax2.plot(t_com, u_com, color="#4A9D5F", linewidth=2, label="com anti-windup")
ax2.set_ylabel("tensão comandada [V]")
ax2.set_xlabel("tempo [s]")
ax2.set_title("Quanto tempo cada um passa grudado no teto", fontsize=12)
ax2.legend(loc="lower right"); ax2.grid(alpha=0.25)

plt.tight_layout()
plt.show()
"""),

    md("""
### A correção, em uma linha

Olhe o código do `DiscretePID`. O anti-windup é isto:

```python
u_sem_corte = Kp*e + integral + d
u = satura(u_sem_corte)

if u != u_sem_corte:                       # o driver cortou
    integral += Kaw * (u - u_sem_corte) * Ts   # desconta a diferença
```

Uma linha. Quando o driver corta, o integral devolve o que não foi entregue.

Essa técnica chama-se **back-calculation**, e é a que se usa em código
embarcado porque não precisa de nada além do que já está na memória.
"""),

    md("""
## Passo 4 — Sintonizando sem chutar

Até aqui os ganhos vieram prontos. De onde eles saem?

Existe uma receita clássica, do **Ziegler-Nichols**, que funciona assim:

1. Desligue o I e o D. Só P.
2. Aumente `Kp` até o robô oscilar sem parar, nem crescendo nem sumindo.
3. Anote esse ganho — chama-se **ganho crítico**, $K_u$ — e o **período da
   oscilação**, $T_u$.
4. Aplique a tabela de Ziegler-Nichols e saia com `Kp`, `Ki`, `Kd`.

A célula abaixo faz os passos 1 a 3 automaticamente, procurando o ponto onde a
oscilação para de sumir.
"""),
    code(r"""
def oscila_sem_sumir(Kp, t_end=2.0):
    '''Mede o quanto a velocidade ainda balança no fim.'''
    pid = DiscretePID(Kp=Kp, Ki=0.0, Kd=0.0, u_max=1e6)   # sem teto, para achar Ku
    t, w, _ = rodar(pid, t_end=t_end)
    return w[-int(0.3 / PARAMS.Ts):].std()

print(f"{'Kp':>8}  {'balanço no fim':>16}")
print("-" * 28)
Ku = None
for Kp in (1, 2, 5, 10, 20, 40, 80):
    balanco = oscila_sem_sumir(Kp)
    marca = "some" if balanco < 0.5 else "PERSISTE"
    print(f"{Kp:>8}  {balanco:>12.2f}    {marca}")
    if Ku is None and balanco >= 0.5:
        Ku = Kp

print()
print(f"O ganho crítico Ku está por volta de {Ku}.")
print("A partir dali a oscilação para de sumir sozinha.")
"""),

    md("""
### Aplicando a receita

Com $K_u$ e o período da oscilação $T_u$, a tabela do Ziegler-Nichols devolve
os três ganhos.

Um aviso honesto: **Ziegler-Nichols é um ponto de partida, não uma resposta**.
A receita é de 1942 e foi feita para processos industriais lentos. Ela costuma
dar um sobressinal alto demais para robótica. Serve para você não começar do
zero — depois você ajusta.
"""),
    code(r"""
from nexabot.controllers import ziegler_nichols

# período da oscilação no ganho crítico, medido do sinal
pid_critico = DiscretePID(Kp=Ku, Ki=0.0, Kd=0.0, u_max=1e6)
t_c, w_c, _ = rodar(pid_critico, t_end=2.0)
trecho = w_c[-int(0.5 / PARAMS.Ts):]
cruzamentos = np.where(np.diff(np.sign(trecho - trecho.mean())))[0]
Tu = 2 * np.mean(np.diff(cruzamentos)) * PARAMS.Ts if len(cruzamentos) > 2 else 4 * PARAMS.Ts

Kp_zn, Ki_zn, Kd_zn = ziegler_nichols(Ku, Tu)

print(f"Ku = {Ku}      Tu = {Tu*1000:.1f} ms")
print("-" * 46)
print(f"Ziegler-Nichols sugere:  Kp = {Kp_zn:.4f}")
print(f"                         Ki = {Ki_zn:.4f}")
print(f"                         Kd = {Kd_zn:.6f}")
print()

pid_zn = DiscretePID(Kp=Kp_zn, Ki=Ki_zn, Kd=Kd_zn)
t_zn, w_zn, u_zn = rodar(pid_zn, t_end=2.0)
sobre_zn = max(0.0, 100 * (w_zn.max() - ALVO) / ALVO)

pid_mao = DiscretePID(Kp=0.3, Ki=8.0, Kd=0.004)
t_mao, w_mao, u_mao = rodar(pid_mao, t_end=2.0)
sobre_mao = max(0.0, 100 * (w_mao.max() - ALVO) / ALVO)

print(f"{'sintonia':>18}  {'sobressinal':>12}  {'ω final':>9}")
print("-" * 44)
print(f"{'Ziegler-Nichols':>18}  {sobre_zn:>11.1f}%  {w_zn[-1]:>9.2f}")
print(f"{'ajustada na mão':>18}  {sobre_mao:>11.1f}%  {w_mao[-1]:>9.2f}")
"""),

    md("""
## Mexa aqui

**Experimento 1 — o D contra o ruído.**
Suba `Kd` de `0.004` para `0.05`. A resposta melhora ou piora? Olhe a curva do
comando: ela fica serrilhada. Num robô real, isso vira motor chiando.

**Experimento 2 — a dosagem da proteção.**
O anti-windup não é liga-desliga, é dosagem. Rode com `KAW` valendo 0, depois
1, depois 10, depois 100. Você vai ver o sobressinal descer degrau a degrau.

Repare que `Kaw = 1` quase não muda nada. A correção que ele aplica por ciclo é
`Kaw × (u_cortado − u_pedido) × Ts`, e com `Ts` valendo 5 milissegundos isso é
pequeno demais para dar conta. Sintonizar `Kaw` faz parte do trabalho.

**Experimento 3 — alvo modesto.**
Baixe `ALVO_TESTE` para `80` rad/s, mantendo `KAW = 0`. O windup some quase
todo. Por quê? Porque com alvo baixo o driver nem chega a saturar, e sem
saturação não existe windup. **O windup é um problema de saturação, não de
PID.**
"""),
    code(r"""
# ⬇️ mexa aqui
KP, KI, KD, KAW = 0.15, 40.0, 0.0, 100.0
ALVO_TESTE = 300.0

alvo_antigo = ALVO
ALVO = ALVO_TESTE

pid_x = DiscretePID(Kp=KP, Ki=KI, Kd=KD, Kaw=KAW)
t_x, w_x, u_x = rodar(pid_x, t_end=3.0)

sobre = max(0.0, 100 * (w_x.max() - ALVO) / ALVO)
ciclos_saturados = int(np.sum(np.abs(u_x) >= PARAMS.V_max - 1e-9))

print(f"Kp={KP}  Ki={KI}  Kd={KD}  Kaw={KAW}   alvo={ALVO_TESTE} rad/s")
print("-" * 56)
print(f"sobressinal            : {sobre:6.1f}%")
print(f"velocidade final       : {w_x[-1]:6.2f} rad/s")
print(f"ciclos com driver no teto: {ciclos_saturados:4d} de {len(u_x)}")
if ciclos_saturados == 0:
    print()
    print("Nenhuma saturação → nenhum windup possível. O anti-windup fica")
    print("sem trabalho, e o valor de Kaw não muda nada.")

ALVO = alvo_antigo
"""),

    md("""
## Aprofundamento (opcional)

### A tabela do Ziegler-Nichols

Para o PID clássico, a receita é:

| Ganho | Fórmula |
| --- | --- |
| $K_p$ | $0{,}6\\,K_u$ |
| $K_i$ | $1{,}2\\,K_u / T_u$ |
| $K_d$ | $0{,}075\\,K_u\\,T_u$ |

Os números vieram de ajuste empírico sobre uma família de processos
industriais, publicados em 1942. Não há derivação teórica elegante por trás —
é engenharia experimental, e por isso mesmo funciona razoavelmente em muita
coisa e mal em algumas.

### Por que o derivativo é filtrado

O D puro seria $K_d \\frac{de}{dt}$. Em tempo discreto isso vira
$K_d \\frac{e[k]-e[k-1]}{T_s}$ — uma subtração dividida por 5 milissegundos.
Um tremor de 0,1 rad/s no sensor vira 20 rad/s de derivada.

A `DiscretePID` usa um filtro de primeira ordem com constante `tau_f`:

$$
D[k] = \\frac{K_d\\,(e[k]-e[k-1]) + \\tau_f\\,D[k-1]}{\\tau_f + T_s}
$$

A célula abaixo mostra o estrago que o D sem filtro faria com um sensor
ruidoso.
"""),
    code(r"""
# Cenário: o robô JÁ chegou no alvo. O erro deveria ser zero e o comando
# deveria ficar parado. Só que o encoder treme um pouquinho, e é só isso
# que o termo derivativo tem para olhar.
rng = np.random.default_rng(7)
tau_f = 0.01
n_amostras = 400

def termo_derivativo(sigma_ruido, Kd):
    # Compara o D puro com o D filtrado, vendo SÓ ruído de sensor.
    erro = rng.normal(0.0, sigma_ruido, n_amostras)     # erro médio zero
    d_puro = Kd * np.diff(erro, prepend=erro[0]) / PARAMS.Ts

    d_filt = np.zeros(n_amostras)
    for k in range(1, n_amostras):
        d_filt[k] = (Kd * (erro[k] - erro[k-1]) + tau_f * d_filt[k-1]) / (tau_f + PARAMS.Ts)
    return d_puro, d_filt

print("O robô parado no alvo. O erro é só o tremor do encoder.")
print("Quanto de comando o termo D inventa a partir de nada?")
print()
print(f"{'tremor':>9}  {'Kd':>8}  {'D puro (pico)':>15}  {'D filtrado (pico)':>19}")
print("-" * 60)
for sigma, Kd in ((0.5, 0.004), (0.5, 0.02), (2.0, 0.02)):
    dp, df = termo_derivativo(sigma, Kd)
    print(f"{sigma:>6.1f} rad/s  {Kd:>8.3f}  {np.abs(dp).max():>13.2f} V  {np.abs(df).max():>17.2f} V")

dp, df = termo_derivativo(2.0, 0.02)
print()
print(f"O filtro corta a agitação em {dp.std()/df.std():.1f} vezes, em todos os casos.")
print()
print("Olhe a última linha. Com o encoder tremendo 2 rad/s e um Kd um")
print("pouco mais alto, o D puro inventa picos de dezenas de volts de")
print("comando — a partir de um robô que está PARADO no alvo. O filtro")
print("derruba isso para menos de um quarto.")
print()
print("É por isso que D puro não se usa em sistema com sensor de verdade.")
"""),

    md("""
## O que você leva desta aula

1. **P olha o presente, I o passado, D o futuro.** Cada um resolve uma coisa
   e estraga outra.
2. **O D precisa ser filtrado.** Derivada de sinal ruidoso é ruído amplificado.
3. **Windup é o integral guardando comando que nunca foi entregue.** Ele só
   existe quando o atuador satura.
4. **Anti-windup por back-calculation é uma linha de código**: quando o driver
   corta, desconte a diferença do integral.
5. **Ziegler-Nichols é ponto de partida, não resposta.** Sintonia boa termina
   ajustando na mão, com um critério de aceitação.

Na Aula 7 você vai descobrir que o controlador não vê o robô o tempo todo —
ele olha de 5 em 5 milissegundos — e o que acontece se ele olhar pouco demais.

## Se deu erro

**A varredura do ganho crítico demora.**
Ela simula sete malhas. Uns 20 a 40 segundos. Reduza `t_end` para `1.2` se
precisar.

**`Tu` deu um valor estranho.**
A detecção do período depende de o sinal estar oscilando de forma limpa. Se o
seu `Ku` caiu num ponto de transição, o valor sai torto. Não invalida a aula —
o ponto é o método, não o número.

**O sobressinal do Ziegler-Nichols ficou enorme.**
Isso é esperado e está no texto: a receita de 1942 é agressiva demais para
robótica. É por isso que a última tabela compara com a sintonia feita na mão.
""" + RODAPE_ERRO),
]
