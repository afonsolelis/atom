"""Notebook da Aula 15 — o tempo não é exato."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import ABERTURA_IMPORTS, GLOSSARIO, RODAPE_ERRO, md, code  # noqa: E402

TITULO = "Aula 15 — O tempo não é exato"
SLUG = "hardware_in_the_loop"

CELULAS = [
    md("""
# Aula 15 — O tempo não é exato

## O que você vai fazer aqui

Na Aula 14 o código C bateu com o modelo, dígito por dígito. Perfeito.

Só que essa comparação assumiu uma coisa que a realidade não entrega: que cada
ciclo acontece **exatamente** a cada 5 milissegundos.

No hardware de verdade, um ciclo demora 4,9 ms, o próximo 5,3, o próximo 5,0.
Hoje você vai medir essa variação — ela tem nome, **jitter** — e vai ver o
watchdog disparar quando o alvo para de responder.

**Tempo:** cerca de 30 minutos.
**Pré-requisito:** notebook da Aula 14.
"""),

    md("""
## Antes de começar

### 1. *Hardware-in-the-loop*

Na Aula 14 (SIL) o código C rodava dentro do Python, como biblioteca.

Em **HIL**, o código roda **no hardware de verdade** — um microcontrolador
ligado por cabo — enquanto a planta continua simulada no computador.

O laço fica assim, e ele roda 200 vezes por segundo:

1. O computador simula o motor e calcula a velocidade.
2. Manda essa velocidade pelo cabo para o microcontrolador.
3. O microcontrolador roda o PID e devolve a tensão de comando.
4. O computador aplica essa tensão na planta simulada.
5. Repete.

Por que fazer isso? Porque testar com o robô de verdade é caro e perigoso.
Aqui o controlador é real, a física é simulada, e você pode provocar uma
emergência mil vezes sem quebrar nada.

Este notebook usa um alvo simulado (*loopback*), que se comporta como um
microcontrolador ligado por cabo sem precisar de hardware.

### 2. Tempo real não é "rápido"

Este é o mal-entendido mais comum da área.

> **Tempo real** não significa "rápido". Significa **no prazo, sempre**.

Um sistema que responde em 1 ms na média mas às vezes leva 100 ms **não é**
tempo real. Um sistema que responde sempre em 50 ms, sem nunca falhar, **é**.

O que importa é o pior caso ser conhecido e respeitado — exatamente a lógica
da Aula 11.

### 3. Jitter — a analogia do ônibus

O ônibus da sua linha passa a cada 10 minutos. Na teoria.

Na prática ele passa aos 9, depois aos 13, depois aos 10, depois aos 8. O
intervalo **médio** continua 10 minutos, mas você nunca sabe qual vai ser o
próximo.

Essa variação chama-se **jitter** (pronuncia-se "djíter"). Duas medidas
importam:

- **Jitter médio** — o quanto varia normalmente.
- **Jitter de pior caso** — a maior variação já observada. Esta é a que
  importa para segurança.

### 4. Latência

Diferente de jitter, e as duas vivem confundidas.

- **Latência** é o tempo de ida e volta: mandei a pergunta, quanto demorou a
  resposta chegar?
- **Jitter** é a variação do intervalo entre um ciclo e o próximo.

Um sistema pode ter latência alta e jitter baixo — resposta demorada, mas
sempre igualmente demorada. Isso é ruim, mas **previsível**, e dá para
projetar em cima.

O contrário — latência baixa com jitter alto — costuma ser pior, porque você
não consegue garantir nada.
"""),

    md(GLOSSARIO),

    md("""
## Passo 1 — Fechando a malha com o alvo

A célula abaixo roda o laço HIL: planta simulada no computador, controlador no
alvo, conversando ciclo a ciclo.

Repare no `real_time=True`. Com ele, o laço **dorme** o tempo necessário para
respeitar os 5 ms de parede a parede — e é justamente esse dormir que produz
jitter medível, como num sistema embarcado de verdade.
"""),
    code(ABERTURA_IMPORTS + r"""
import numpy as np
from nexabot.params import PARAMS
from nexabot import hil

alvo = hil.LoopbackTarget(Kp=0.30, Ki=8.0, Kd=0.004,
                          Ts=PARAMS.Ts, u_max=PARAMS.V_max, Kaw=100.0)

V_REF = 0.6      # m/s
omega_ref = PARAMS.v_to_omega(V_REF)

resultado = hil.run_closed_loop_hil(
    target=alvo,
    r_of_t=lambda t: omega_ref,
    t_end=2.0,
    Ts=PARAMS.Ts,
    real_time=True,
)

print(f"Referência       : {V_REF} m/s = {omega_ref:.0f} rad/s")
print(f"Ciclos executados: {len(resultado.u)}")
print("-" * 52)
print(f"Velocidade final : {resultado.y[-1]:.2f} rad/s")
print(f"Erro final       : {omega_ref - resultado.y[-1]:.2f} rad/s")
print()
print("O controle funcionou. Agora vem a parte que a simulação escondia:")
print("quanto tempo cada ciclo realmente levou.")
"""),

    md("""
## Passo 2 — Medindo o jitter

Agora os números de tempo.

O laço deveria rodar exatamente a cada 5 ms. Vamos ver o que ele fez de fato.
"""),
    code(r"""
stats = resultado.jitter_stats

print("Temporização do laço HIL")
print("-" * 56)
for chave, valor in stats.items():
    if isinstance(valor, float):
        print(f"  {chave:>22} : {valor:10.4f}")
    else:
        print(f"  {chave:>22} : {valor:10d}")
"""),

    md("""
### Lendo os números

O **período nominal** é 5 ms — o que você pediu.

O **período médio** é o que aconteceu na média. Ele deve ficar perto de 5 ms;
se estiver muito acima, o seu laço não consegue acompanhar o ritmo, e isso é
um problema de projeto, não de jitter.

O **desvio máximo** é o que importa para segurança. É o pior atraso que já
aconteceu, e é ele que entra na conta do REQ-SAFE-006 da Aula 11.

O gráfico abaixo mostra a distribuição. Repare que ela não é uma linha reta em
5 ms — é uma nuvem em torno de 5 ms.
"""),
    code(r"""
import matplotlib.pyplot as plt

periodos_ms = resultado.periodos_loop_s * 1e3
nominal_ms = PARAMS.Ts * 1e3

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 4.5))

ax1.plot(periodos_ms, linewidth=0.8, color="#002057")
ax1.axhline(nominal_ms, color="#4A9D5F", linestyle="--", linewidth=1.8,
            label=f"nominal: {nominal_ms:.1f} ms")
ax1.set_xlabel("ciclo")
ax1.set_ylabel("duração do ciclo [ms]")
ax1.set_title("Cada ciclo, um tempo diferente", fontsize=12)
ax1.legend(); ax1.grid(alpha=0.25)

ax2.hist(periodos_ms, bins=40, color="#5B8DBE", edgecolor="white")
ax2.axvline(nominal_ms, color="#4A9D5F", linestyle="--", linewidth=1.8)
ax2.set_xlabel("duração do ciclo [ms]")
ax2.set_ylabel("quantas vezes")
ax2.set_title("A distribuição — uma nuvem, não um ponto", fontsize=12)
ax2.grid(alpha=0.25, axis="y")

plt.tight_layout()
plt.show()
"""),

    md("""
## Passo 3 — O jitter cabe no orçamento?

Aqui a aula se conecta com a Aula 11.

Lá você provou que o torque zera em até 150 ms **contando ciclos**. Mas se
cada ciclo pode durar mais que 5 ms, a conta em milissegundos muda.

A pergunta prática: **com o jitter medido, o prazo ainda é respeitado?**
"""),
    code(r"""
from nexabot import timed

r_prazo = timed.verificar_req_safe_006(atraso_deteccao_max=2,
                                       permite_ciclo_perdido=True)

periodo_pior_ms = float(np.max(periodos_ms))
ciclos_pior_caso = r_prazo.pior_caso_periodos

prazo_nominal = ciclos_pior_caso * nominal_ms
prazo_com_jitter = ciclos_pior_caso * periodo_pior_ms

print("Juntando a Aula 11 com o jitter medido agora")
print("-" * 62)
print(f"  pior caso em ciclos (Aula 11)     : {ciclos_pior_caso:6d} ciclos")
print(f"  período nominal                   : {nominal_ms:9.3f} ms")
print(f"  período de PIOR CASO medido       : {periodo_pior_ms:9.3f} ms")
print()
print(f"  prazo se todo ciclo durar 5 ms    : {prazo_nominal:9.2f} ms")
print(f"  prazo se TODO ciclo durar o pior  : {prazo_com_jitter:9.2f} ms")
print(f"  limite do requisito               : {r_prazo.limite_ms:9.2f} ms")
print()
if prazo_com_jitter <= r_prazo.limite_ms:
    margem = r_prazo.limite_ms - prazo_com_jitter
    print(f"  PASSA mesmo no cenário pessimista, com {margem:.1f} ms de margem.")
    print()
    print("  E note que esse cenário é conservador de propósito: ele supõe")
    print("  que TODOS os ciclos durem o pior tempo já observado, o que na")
    print("  prática não acontece. Em segurança, a conta se faz pelo pior.")
else:
    print("  NÃO PASSA. O jitter come a margem do requisito.")
    print("  Caminhos: reduzir o jitter, reduzir Ts, ou renegociar o prazo.")
"""),

    md("""
## Passo 4 — Quando o alvo para de responder

Agora o cenário que nenhum teste de software pega de dentro: **o alvo travou**.

Não é um erro que o código detecta, porque o código que detectaria também
travou. É por isso que o watchdog existe fora dele.

A célula abaixo pede ao alvo que demore cada vez mais para responder, e
observa o watchdog agir.
"""),
    code(r"""
# O watchdog real do projeto roda o passo do alvo numa thread auxiliar e
# impõe um prazo. Se o alvo não responder a tempo, ele devolve comando
# seguro (torque zero) em vez de travar o laço esperando para sempre.
prazo_s = timed.LIMITE_PERIODOS * PARAMS.Ts
watchdog = hil.Watchdog(deadline_s=prazo_s)

print(f"Prazo do watchdog: {prazo_s*1000:.0f} ms "
      f"({timed.LIMITE_PERIODOS} ciclos de {nominal_ms:.0f} ms)")
print()
print(f"{'atraso do alvo':>18}  {'comando devolvido':>19}  situação")
print("-" * 62)

for atraso_ms in (0.0, 20.0, 100.0, 200.0, 400.0):
    try:
        u, estourou = watchdog.guarded_step(alvo, omega_ref, 100.0,
                                            delay_ms=atraso_ms)
    except hil.TargetError as e:
        print(f"{atraso_ms:>15.0f} ms  {'—':>17}    alvo já encerrado: {e}")
        print()
        print("O watchdog não só devolveu comando seguro: ele DERRUBOU o alvo.")
        print("É o `kill_target_on_timeout=True`, e é intencional.")
        print()
        print("A lógica: um alvo que estourou o prazo pode nunca responder.")
        print("Se o watchdog só esperasse mais um pouco, a thread auxiliar")
        print("continuaria presa na chamada antiga, e o laço travaria de vez.")
        print("Melhor encerrar e recomeçar limpo.")
        break
    situacao = "PRAZO ESTOURADO -> comando seguro" if estourou else "respondeu a tempo"
    print(f"{atraso_ms:>15.0f} ms  {u:>17.3f} V  {situacao}")

print()
print("Repare no que o watchdog NÃO faz: ele não tenta descobrir o motivo.")
print("Não sabe se o firmware travou, se o cabo caiu ou se a fonte desligou.")
print("Ele sabe uma coisa só — faz tempo demais que ninguém respondeu.")
print()
print("Essa ignorância deliberada é o que o torna confiável: ele funciona")
print("para modos de falha que ninguém listou no projeto.")
"""),

    md("""
## Mexa aqui

**Experimento 1 — o jitter sem tempo real.**
Rode com `TEMPO_REAL = False`. O laço passa a correr o mais rápido possível.
Os números de jitter viram outra coisa completamente — e isso mostra que
medição de tempo só vale no modo em que o sistema vai operar.

**Experimento 2 — o watchdog apertado.**
Baixe `PRAZO_MS` para `10`. O watchdog passa a disparar em atrasos que são
normais de escalonamento, e o robô para à toa. Watchdog apertado demais é tão
ruim quanto folgado demais — e o custo aqui é disponibilidade, não segurança.

**Experimento 3 — o orçamento com Ts menor.**
Volte ao Passo 3 e refaça a conta com `Ts = 2 ms`. O prazo em milissegundos
melhora? Cuidado: com `Ts` menor cabem mais ciclos no mesmo prazo, mas o
jitter relativo tende a piorar, porque o tempo de comunicação não encolhe
junto.
"""),
    code(r"""
# ⬇️ mexa aqui
TEMPO_REAL = True
PRAZO_MS = timed.LIMITE_PERIODOS * PARAMS.Ts * 1000
DURACAO_S = 1.5

alvo_x = hil.LoopbackTarget(Kp=0.30, Ki=8.0, Kd=0.004,
                            Ts=PARAMS.Ts, u_max=PARAMS.V_max, Kaw=100.0)
res_x = hil.run_closed_loop_hil(target=alvo_x, r_of_t=lambda t: omega_ref,
                                t_end=DURACAO_S, Ts=PARAMS.Ts,
                                real_time=TEMPO_REAL)
st_x = res_x.jitter_stats
p_ms = res_x.periodos_loop_s * 1e3

print(f"real_time = {TEMPO_REAL}   |   prazo do watchdog = {PRAZO_MS:.0f} ms")
print("-" * 58)
print(f"  período nominal   : {nominal_ms:8.3f} ms")
print(f"  período médio     : {float(np.mean(p_ms)):8.3f} ms")
print(f"  período mínimo    : {float(np.min(p_ms)):8.3f} ms")
print(f"  período máximo    : {float(np.max(p_ms)):8.3f} ms")
print(f"  jitter (desvio)   : {float(np.std(p_ms)):8.3f} ms")
print()
print(f"  watchdog dispara após : {PRAZO_MS:6.0f} ms sem resposta")
if PRAZO_MS < float(np.max(p_ms)) * 3:
    print("  ⚠ apertado: um atraso normal do laço já chega perto de disparar.")
    print("    Num sistema real isso pararia o robô sem que nada tivesse")
    print("    quebrado de verdade.")
"""),

    md("""
## Aprofundamento (opcional)

### O que ficou de fora

Esta aula, antes, detalhava o **protocolo de linha**: como os bytes são
empacotados num quadro, o `checksum` que detecta corrupção, o byte de
sincronismo que marca o início da mensagem, o tratamento de mensagem
truncada.

É conteúdo importante para quem vai implementar a ponte, e está no `README` do
laboratório da aula. Mas ele não acrescenta nada ao entendimento de que **o
tempo não é exato**, que é a ideia desta aula.

### De onde vem o jitter

Numa lista, do mais comum ao menos:

1. **Escalonamento do sistema operacional.** No PC, o Linux ou o Windows
   decide quando a sua tarefa roda. Você pede 5 ms; o sistema entrega quando
   der. É a principal fonte no laço HIL rodando em PC.
2. **Tempo de comunicação.** A porta serial tem taxa de transmissão finita, e
   os buffers introduzem atraso variável.
3. **Interrupções no alvo.** No microcontrolador, uma interrupção de maior
   prioridade adia o laço de controle.
4. **Coleta de lixo, cache, memória virtual.** Em linguagens gerenciadas,
   pausas imprevisíveis.

Num microcontrolador dedicado, com o laço de controle numa interrupção de
temporizador de alta prioridade, o jitter cai para microssegundos. Num PC com
sistema operacional comum, fica em milissegundos — como você acabou de medir.

### O caminho para o ESP32 real

O `LoopbackTarget` desta aula simula o alvo. Para usar hardware de verdade, o
projeto traz o `SerialTarget`: mesma interface, mesma chamada, só que
conversando por porta serial com um ESP32 rodando o firmware gerado.

O código do notebook não muda — só a linha que cria o alvo. Essa é a vantagem
de a interface ser a mesma: você desenvolve com o simulado e troca por
hardware sem reescrever o teste.
"""),
    code(r"""
print("Como trocar o alvo simulado pelo hardware de verdade:")
print()
print("  # o que você usou nesta aula")
print("  alvo = hil.LoopbackTarget(Kp=0.30, Ki=8.0, Kd=0.004, ...)")
print()
print("  # o que você usaria com um ESP32 na porta USB")
print("  alvo = hil.SerialTarget(port='/dev/ttyUSB0', baudrate=115200)")
print()
print("O resto do notebook é idêntico. run_closed_loop_hil não sabe nem")
print("se importa com qual dos dois recebeu.")
print()
print("Alvos disponíveis no laboratório:")
for nome in ("LoopbackTarget", "SerialTarget"):
    classe = getattr(hil, nome, None)
    if classe is not None:
        doc = (classe.__doc__ or "").strip().splitlines()[0]
        print(f"  {nome:>16}: {doc}")
"""),

    md("""
## O que você leva desta aula

1. **HIL é o controlador real com a planta simulada.** Barato, seguro e
   repetível.
2. **Tempo real é "no prazo, sempre", não "rápido".**
3. **Jitter é a variação do intervalo entre ciclos.** O ônibus que passa a
   cada 10 minutos, menos quando não passa.
4. **Latência e jitter são coisas diferentes.** Latência alta e previsível é
   melhor que latência baixa e imprevisível.
5. **O jitter come a margem do prazo** que você provou na Aula 11. A conta de
   segurança se refaz com o pior caso medido.
6. **O watchdog não precisa entender a causa.** Ele só sabe que faz tempo
   demais que ninguém respondeu — e essa ignorância é o que o torna confiável.

Na Aula 16, a última, tudo o que você produziu nas quinze aulas vira uma coisa
só: uma linha de matriz que liga o requisito ao binário. E a pergunta final:
isso é um certificado?

## Se deu erro

**O laço demorou o tempo da simulação inteiro.**
Com `real_time=True` ele dorme para respeitar os 5 ms, então 2 segundos de
simulação levam 2 segundos de relógio. É proposital.

**O jitter deu zero ou quase.**
Sua máquina está pouco carregada, ou o Python conseguiu dormir com precisão
boa. Rode alguma coisa pesada em paralelo e repita: o jitter aparece.

**`TargetError` na criação do alvo.**
O `LoopbackTarget` compila o firmware de loopback com o `gcc` na hora de ser
criado. Sem compilador, ele falha aí. Instale o `build-essential`.

**`AttributeError: SerialTarget`.**
Só aparece se você tentar usar hardware sem o `pyserial` instalado:
`uv pip install --python .venv/bin/python pyserial`.
""" + RODAPE_ERRO),
]
