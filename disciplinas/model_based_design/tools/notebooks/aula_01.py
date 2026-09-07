"""Notebook da Aula 1 — por que um comando fixo não sustenta a velocidade."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import ABERTURA_IMPORTS, RODAPE_ERRO, md, code  # noqa: E402

TITULO = "Aula 1 — O NexaBot que esquece a própria velocidade"
SLUG = "primeiro_contato"

CELULAS = [
    md("""
# Aula 1 — O NexaBot que esquece a própria velocidade

## O que você vai fazer aqui

Você vai mandar o robô andar a uma velocidade, colocar uma carga em cima dele
e ver a velocidade cair sozinha. Depois vai descobrir, com um número, o
tamanho exato dessa queda.

É só isso. Nenhuma fórmula nova, nenhuma teoria. Um robô que desobedece, e a
medida de quanto ele desobedece.

**Tempo:** cerca de 30 minutos, com calma.
**Pré-requisito:** nenhum. Sério, nenhum.
"""),

    md("""
## Antes de começar

Três palavras vão aparecer o tempo todo nesta disciplina. Vamos combinar o
que cada uma quer dizer, em português, antes de qualquer conta.

### 1. `rad/s` — radianos por segundo

É o jeito da engenharia de dizer **velocidade de giro**.

Você conhece "rotações por minuto" (RPM), do velocímetro do carro. Radiano por
segundo é a mesma ideia, com outra régua:

- Uma volta inteira = **6,28 radianos** (isso é $2\\pi$).
- Então **6,28 rad/s = uma volta por segundo**.
- E **100 rad/s ≈ 16 voltas por segundo**.

Por que engenharia usa radiano e não volta? Porque as contas de física ficam
mais simples. É a única razão. Não tem mistério.

O símbolo é **ω**, que se lê **ômega**. Toda vez que você vir ω, leia
"a velocidade de giro do eixo".

### 2. Modelo

Um **modelo** é uma conta que imita o robô.

Se a conta é boa, você descobre no computador que o robô vai bater — em vez de
descobrir no chão de fábrica, com o robô batendo. É essa a proposta da
disciplina inteira: errar barato.

### 3. Malha aberta

**Malha aberta** é mandar e não conferir.

Você grita "anda a 1 metro por segundo!" e vai embora. Ninguém mede se ele
está mesmo a 1 m/s. Se aparecer uma rampa, ele desacelera e você nem fica
sabendo.

O contrário — medir, comparar e corrigir — chama-se *malha fechada*, e é o
assunto da Unidade 2. Hoje a gente só descobre por que a malha aberta não
serve.
"""),

    md("""
## Passo 1 — Ligar o laboratório

A célula abaixo carrega o pacote `nexabot`, que é o código da disciplina, e o
`params`, que guarda os números do robô.

Um detalhe que importa: **todo número desta disciplina mora num arquivo só**,
o `params.py`. Nenhuma aula inventa valor. Se um dia o motor for outro, muda
ali e as dezesseis aulas acompanham.

Rode a célula. Se ela imprimir a lista de parâmetros, está tudo certo.
"""),
    code(ABERTURA_IMPORTS + r"""
from nexabot.params import PARAMS

print("Parâmetros do NexaBot")
print("-" * 46)
print(f"  R  (resistência do fio)      = {PARAMS.R} ohm")
print(f"  L  (indutância)              = {PARAMS.L} H")
print(f"  Kt (constante de torque)     = {PARAMS.Kt} N.m/A")
print(f"  J  (inércia do eixo)         = {PARAMS.J} kg.m²")
print(f"  b  (atrito)                  = {PARAMS.b} N.m.s/rad")
print()
print(f"  Driver: no máximo {PARAMS.V_max} V e {PARAMS.i_max} A")
print(f"  Roda de {PARAMS.r_wheel * 1000:.0f} mm, redutor {PARAMS.N_gear:.0f}:1")
"""),

    md("""
## Passo 2 — Traduzir `rad/s` para uma velocidade que você enxerga

Antes de olhar qualquer gráfico, vamos ancorar a unidade.

O motor gira rápido, mas a roda gira devagar: entre os dois existe um
**redutor** de 20 para 1. O motor dá 20 voltas para a roda dar uma. E a roda
tem 50 mm de raio, então cada volta dela empurra o robô um tanto para a
frente.

A célula abaixo faz essa tradução para alguns valores. Olhe a última coluna:
é ali que a unidade vira algo que você consegue imaginar.
"""),
    code(r"""
import math

print(f"{'ω do motor':>12}  {'voltas/s':>10}  {'velocidade do robô':>20}")
print("-" * 46)
for omega in [10, 50, 100, 200, 480]:
    voltas_por_segundo = omega / (2 * math.pi)
    v_linear = PARAMS.omega_to_v(omega)          # m/s
    print(f"{omega:>9} rad/s  {voltas_por_segundo:>10.1f}  {v_linear:>17.3f} m/s")

print()
print("Leia a linha de 100 rad/s assim: o eixo do motor dá cerca de 16 voltas")
print("por segundo, e o robô anda a 25 centímetros por segundo.")
"""),

    md("""
## Passo 3 — O robô andando sem carga

Agora a primeira simulação.

Vamos aplicar **12 volts** no motor e deixar rodar por 2 segundos. Nada
empurra contra o robô: chão plano, sem caixa em cima. É o caso fácil.

Por que 2 segundos e não meio? Porque a velocidade demora quase 1 segundo para
parar de subir. Se eu cortasse antes, estaria medindo o robô ainda acelerando,
e não a velocidade que ele de fato mantém. Medir cedo demais é um erro clássico
— e a razão de o número desta célula ser confiável.

A função `simulate` resolve, numericamente, como a corrente e a velocidade
evoluem instante a instante. Você não precisa entender como ela faz isso hoje
— isso é a Aula 2. Hoje interessa só o resultado.
"""),
    code(r"""
from nexabot.plant import simulate

TENSAO = 12.0        # volts aplicados no motor
DURACAO = 2.0        # segundos — tempo de sobra para a velocidade estabilizar

t, X = simulate(u_of_t=TENSAO, t_end=DURACAO)

corrente = X[:, 0]   # ampères
omega = X[:, 1]      # rad/s

omega_final = omega[-1]
print(f"Tensão aplicada:        {TENSAO} V")
print(f"Velocidade no fim:      {omega_final:.2f} rad/s")
print(f"Ou seja, o robô anda a: {PARAMS.omega_to_v(omega_final):.3f} m/s")
"""),

    md("""
### O que aconteceu no gráfico

A célula abaixo desenha as duas grandezas — e faz uma coisa incomum de
propósito: **os dois gráficos têm escalas de tempo diferentes**.

O de cima mostra só os primeiros **50 milissegundos**. O de baixo mostra os
**2 segundos** inteiros. Repare nos rótulos do eixo x antes de comparar.

Precisei disso porque duas coisas de ritmos muito diferentes convivem aqui.

**A corrente sobe num piscar de olhos.** Ela chega perto do pico em uns 6 ms.
É a parte elétrica do motor, e ela é rápida.

**Depois a corrente desce devagar** — e essa descida não é elétrica. Conforme
o motor ganha velocidade, ele passa a *gerar* uma tensão contrária (tem nome:
força contraeletromotriz), que sobra menos para empurrar corrente. Ou seja: a
descida lenta da corrente é a velocidade subindo.

**A velocidade leva quase meio segundo para estabilizar.** É a parte mecânica,
lenta, porque tem massa para acelerar.

A diferença entre os dois ritmos é de **48 vezes**. Se eu pusesse as duas na
mesma escala, a subida da corrente viraria um risco vertical ilegível.

Guarde um número: a velocidade chega a **63%** do valor final em exatamente
141 ms. Esse 63% parece arbitrário agora, mas ele tem nome — *constante de
tempo* — e na Aula 3 você vai descobrir por que ele é o número que a
engenharia escolheu para medir "quão rápido é rápido".
"""),
    code(r"""
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 6))

# de cima: só os primeiros 50 ms, para a corrente caber na tela
ax1.plot(t * 1000, corrente, color="#C0392B")
ax1.set_xlim(0, 50)
ax1.set_xlabel("tempo [ms]  ← repare: milissegundos")
ax1.set_ylabel("corrente [A]")
ax1.set_title("O elétrico é rápido: 90% do pico em 6 ms")
ax1.grid(alpha=0.3)

# de baixo: os 2 segundos inteiros
ax2.plot(t, omega, color="#002057")
ax2.set_xlabel("tempo [s]  ← repare: segundos")
ax2.set_ylabel("velocidade ω [rad/s]")
ax2.set_title("O mecânico é lento: 63% em 141 ms, 95% só em 418 ms")
ax2.axhline(0.63 * omega_final, color="#888888", linestyle=":", linewidth=1)
ax2.axvline(0.1414, color="#888888", linestyle=":", linewidth=1)
ax2.text(0.16, 0.63 * omega_final - 32, "63% em 141 ms", fontsize=9, color="#555555")
ax2.grid(alpha=0.3)

plt.tight_layout()
plt.show()
"""),

    md("""
## Passo 4 — Agora com carga: o robô desobedece

Aqui está o ponto da aula inteira.

Vamos repetir **exatamente** a mesma simulação: os mesmos 12 volts, os mesmos
2 segundos. Nada muda no comando. A única diferença é que, no instante 1
segundo, aparece uma **carga** — pense numa rampa, ou numa caixa pesada que o
robô passa a empurrar.

Nessa altura a velocidade já estabilizou, então o que você vai ver a seguir é
efeito da carga, e só dela.

Antes de rodar, responda para você mesmo: *a velocidade vai mudar?*

O comando não mudou. Se você acha que a velocidade fica igual, rode a célula.
""" ),
    code(r"""
TORQUE_CARGA = 0.15      # N.m — a carga que aparece
INSTANTE_CARGA = 1.0     # segundos — quando ela aparece

def carga(tempo):
    '''Sem carga até 1 s; com carga depois disso.'''
    return TORQUE_CARGA if tempo >= INSTANTE_CARGA else 0.0

t2, X2 = simulate(u_of_t=TENSAO, t_end=DURACAO, tau_load_of_t=carga)
omega2 = X2[:, 1]

# velocidade logo antes da carga e no fim
idx_antes = int(INSTANTE_CARGA / (t2[1] - t2[0])) - 1
omega_antes = omega2[idx_antes]
omega_depois = omega2[-1]

queda = omega_antes - omega_depois
queda_pct = 100 * queda / omega_antes

print(f"Antes da carga:  {omega_antes:7.2f} rad/s  ({PARAMS.omega_to_v(omega_antes):.3f} m/s)")
print(f"Depois da carga: {omega_depois:7.2f} rad/s  ({PARAMS.omega_to_v(omega_depois):.3f} m/s)")
print("-" * 52)
print(f"Perdeu:          {queda:7.2f} rad/s  ({queda_pct:.1f}% da velocidade)")
"""),

    md("""
### Esse número é a disciplina inteira

O comando foi o mesmo. A tensão foi a mesma. E o robô ficou mais lento.

Numa esteira de armazém isso significa que o robô chega atrasado ao ponto de
encontro. Se outro robô já estiver lá, os dois se batem.

E note: **ninguém no sistema percebeu**. Não existe alarme, não existe
correção. O comando continuou os mesmos 12 volts até o fim, porque em malha
aberta ninguém está medindo nada.

O gráfico abaixo põe os dois casos lado a lado. O degrau para baixo é o
momento em que a carga entra.
"""),
    code(r"""
fig, ax = plt.subplots(figsize=(9.5, 5))

# faixa cinza marcando o trecho em que a carga está agindo
ax.axvspan(INSTANTE_CARGA, t2[-1], color="#C0392B", alpha=0.05)

# a curva sem carga vai tracejada e mais grossa: até 1 s as duas são
# idênticas, e o tracejado deixa isso visível em vez de esconder uma sob a outra
ax.plot(t, omega, label="sem carga (comando de 12 V)",
        color="#4A9D5F", linewidth=3.5, linestyle="--")
ax.plot(t2, omega2, label="com carga a partir de 1 s (mesmos 12 V)",
        color="#C0392B", linewidth=2)

ax.axvline(INSTANTE_CARGA, color="#555555", linestyle=":", linewidth=1.5)

# seta medindo a queda
ax.annotate("", xy=(1.9, omega_depois), xytext=(1.9, omega_antes),
            arrowprops=dict(arrowstyle="<->", color="#333333", linewidth=1.5))
ax.text(1.86, (omega_antes + omega_depois) / 2,
        f"perdeu\n{queda:.0f} rad/s\n({queda_pct:.0f}%)",
        ha="right", va="center", fontsize=10, color="#333333")

ax.text(INSTANTE_CARGA + 0.02, 30, " a carga entra aqui",
        fontsize=10, color="#555555")
ax.text(0.5, 105, "até aqui as duas curvas são a mesma",
        ha="center", fontsize=9.5, color="#2E7D4A", style="italic")

ax.set_xlabel("tempo [s]")
ax.set_ylabel("velocidade ω [rad/s]")
ax.set_title("Mesmo comando, dois resultados — isso é malha aberta",
             fontsize=13, pad=12)
ax.set_ylim(0, omega_antes * 1.15)
ax.legend(loc="lower left", framealpha=0.95)
ax.grid(alpha=0.25)
plt.tight_layout()
plt.show()
"""),

    md("""
## Mexa aqui

Agora é você. Altere **um** valor por vez e rode de novo.

**Experimento 1 — carga maior.**
Troque `TORQUE_CARGA` de `0.15` para `0.30`. Antes de rodar, escreva num papel:
a queda vai dobrar, vai ser menor que o dobro, ou maior?

Rode e confira. A queda vai de 84,6 para 169,4 rad/s — **exatamente o dobro**.
Isso não é coincidência: dentro dos limites do driver, este motor responde de
forma *linear*. Dobrou a causa, dobrou o efeito. É essa propriedade que permite
tudo o que vem nas próximas quinze aulas.

**Experimento 2 — compensar na mão.**
Deixe a carga em `0.15` e vá aumentando `TENSAO` até a velocidade final voltar
aos ~254 rad/s do caso sem carga. Vá de meio em meio volt. Anote a tensão que
resolveu — deve dar 16 V.

Agora a pergunta que importa: **essa tensão que você achou continua certa se a
carga mudar de novo?** Troque a carga para `0.30` mantendo os 16 V e veja.
Essa é a razão de existir a Unidade 2 inteira.

**Experimento 3 — o limite físico.**
Continue subindo `TENSAO`. Em algum ponto o resultado para de melhorar. Por
quê? Olhe o valor de `PARAMS.V_max` que a primeira célula imprimiu.
"""),
    code(r"""
# ⬇️ mexa nos dois números e rode
TORQUE_CARGA = 0.15
TENSAO = 12.0

def carga(tempo):
    return TORQUE_CARGA if tempo >= 1.0 else 0.0

t3, X3 = simulate(u_of_t=TENSAO, t_end=2.0, tau_load_of_t=carga)
w3 = X3[:, 1]

alvo = omega[-1]
falta = alvo - w3[-1]

print(f"tensão = {TENSAO} V, carga = {TORQUE_CARGA} N.m")
print("-" * 52)
print(f"velocidade final = {w3[-1]:7.2f} rad/s  ({PARAMS.omega_to_v(w3[-1]):.3f} m/s)")
print(f"alvo sem carga   = {alvo:7.2f} rad/s")
print(f"ainda falta      = {falta:7.2f} rad/s")
if abs(falta) < 1.0:
    print()
    print("Chegou! Agora troque a carga para 0.30 sem mexer na tensão e rode de novo.")
"""),

    md("""
## Aprofundamento (opcional)

Esta parte não cai na prova e não aparece na videoaula. Está aqui para quem
quiser ver de onde vem o número.

Existe uma conta fechada para a velocidade final sem carga, sem precisar
simular nada. Ela sai de igualar a zero as duas taxas de variação — ou seja,
perguntar "quando é que nada mais muda?".

$$
\\frac{\\omega}{V} = \\frac{K_t}{R\\,b + K_t K_e}
$$

Esse número chama-se **ganho estático**: quantos rad/s você ganha por volt
aplicado. Ele é uma conferência barata — se a simulação discordar dele, uma
das duas está errada.

De onde vem essa fórmula é o assunto da Aula 2. Por enquanto, use como
conferência.
"""),
    code(r"""
ganho_estatico = PARAMS.Kt / (PARAMS.R * PARAMS.b + PARAMS.Kt * PARAMS.Ke)

previsao = ganho_estatico * 12.0
medido = omega[-1]
erro_pct = 100 * abs(previsao - medido) / previsao

print(f"Ganho estático (fórmula):  {ganho_estatico:.4f} rad/(s·V)")
print(f"Previsão para 12 V:        {previsao:.2f} rad/s")
print(f"Simulação sem carga deu:   {medido:.2f} rad/s")
print(f"Diferença:                 {erro_pct:.3f}%")
print()
print("Menos de um centésimo de por cento. A conta e a simulação concordam —")
print("é assim que se confere um modelo sem depender de fé.")
print()
print("Experimento: mude DURACAO para 0.5 s lá em cima e rode tudo de novo.")
print("A diferença pula para quase 3%. Não porque a fórmula ficou errada, mas")
print("porque a simulação foi interrompida antes de a velocidade estabilizar.")
"""),

    md("""
## O que você leva desta aula

1. **ω em rad/s é velocidade de giro.** Uma volta são 6,28 rad. Você já
   consegue traduzir qualquer valor para metros por segundo.
2. **Malha aberta é mandar sem conferir.** Funciona enquanto nada muda.
3. **Quando a carga muda, a velocidade cai — e ninguém percebe.** Você mediu
   essa queda: de 254 para 170 rad/s, um terço da velocidade.
4. **Aumentar a tensão na mão resolve uma carga, não o problema.** Mudou a
   carga, errou de novo.

Na Aula 2 você vai descobrir *por que* o motor se comporta assim — as duas
equações de física que explicam tudo o que você viu hoje.

## Se deu erro

**`ModuleNotFoundError: No module named 'nexabot'`**
O notebook não achou o pacote. Confira se você abriu o Jupyter a partir da
pasta `projeto_nexabot`, ou rode a primeira célula de novo — ela ajusta o
caminho sozinha.

**`ModuleNotFoundError: No module named 'matplotlib'`** (ou `numpy`, `control`)
O ambiente não está instalado. No terminal, dentro de `projeto_nexabot`:

```bash
uv venv .venv
uv pip install --python .venv/bin/python -e .
```

E depois selecione esse ambiente como *kernel* do notebook.

**Os gráficos não aparecem.**
Rode `%matplotlib inline` numa célula e execute o gráfico de novo.

**Os números deram diferentes dos meus.**
Confira se você não deixou algum valor alterado do "Mexa aqui". Rode o
notebook do começo (menu *Run → Restart Kernel and Run All Cells*).
""" + RODAPE_ERRO),
]
