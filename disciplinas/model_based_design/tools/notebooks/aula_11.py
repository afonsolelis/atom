"""Notebook da Aula 11 — provar que cabe no prazo."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import ABERTURA_IMPORTS, GLOSSARIO, RODAPE_ERRO, md, code  # noqa: E402

TITULO = "Aula 11 — 'Rápido' não é requisito; 150 ms é"
SLUG = "prazo_e_watchdog"

CELULAS = [
    md("""
# Aula 11 — "Rápido" não é requisito; 150 ms é

## O que você vai fazer aqui

A Aula 10 provou que o robô **uma hora** corta o torque quando vê um
obstáculo. Ótimo.

Só que "uma hora" não serve. Um robô a 1,2 m/s percorre 1,2 metro por segundo.
Se ele leva 2 segundos para reagir, já andou mais de dois metros com um
obstáculo na frente.

Hoje você troca "uma hora" por **"em até 150 milissegundos"**, e prova isso —
incluindo o pior caso possível, aquele que nenhum teste normal produz.

**Tempo:** cerca de 30 minutos.
**Pré-requisito:** notebook da Aula 10.
"""),

    md("""
## Antes de começar

### 1. O que é um relógio no modelo

Até agora o modelo do supervisor não tinha noção de tempo. Ele só sabia
"estado de antes → estado de depois".

Um **autômato temporizado** acrescenta uma coisa: **relógios**. Pense num
cronômetro que:

- anda sozinho enquanto o tempo passa,
- pode ser **zerado** quando alguma coisa acontece,
- pode ser **consultado** para decidir o que fazer.

Exemplo do dia a dia: o sensor de presença do corredor. Ele acende a luz e
zera um cronômetro. Enquanto o cronômetro não chega a 60 segundos, a luz fica
acesa. Alguém passa de novo, o cronômetro volta a zero.

É esse o mecanismo inteiro. Nada mais complicado que isso.

### 2. Por que o pior caso não aparece em teste normal

Aqui está o motivo desta aula existir.

Quando você testa o robô na bancada, tudo funciona no tempo esperado. O sensor
detecta na hora, o controlador reage no ciclo seguinte, o torque cai.

Mas na vida real acontecem coisas raras:

- o filtro do sensor segura a detecção por 1 ou 2 ciclos;
- o ciclo do controlador atrasa porque outra tarefa demorou;
- um comando se perde e só chega no ciclo seguinte.

Cada uma dessas é rara. **Juntas, são raríssimas** — talvez uma vez a cada
milhão de ciclos. Você nunca vai ver isso na bancada.

E é justamente essa combinação que estoura o prazo. Teste não pega o que é
raro; verificação exaustiva pega, porque não depende de sorte.

### 3. Watchdog

**Watchdog** ("cão de guarda") é um cronômetro que precisa ser "alimentado"
periodicamente pelo software. Se o software travar e parar de alimentá-lo, o
watchdog dispara e coloca o sistema num estado seguro.

É a última linha de defesa: ele protege contra o software ter parado de
funcionar, algo que nenhum teste do software consegue detectar de dentro.

### 4. O requisito de hoje

> **REQ-SAFE-006** — Depois de detectar obstáculo ou emergência, o torque
> chega a zero em no máximo **150 ms**, mesmo no pior caso de atraso de
> detecção e de um ciclo de atuação perdido.

Com `Ts = 5 ms`, 150 ms são **30 períodos de amostragem**. Esse é o
orçamento inteiro.
"""),

    md(GLOSSARIO),

    md("""
## Passo 1 — O orçamento de tempo

Antes de verificar, vamos entender o que está sendo contado.

O prazo de 150 ms não é arbitrário. Ele vem de uma conta de segurança: a que
distância o robô consegue parar antes de encostar no obstáculo.
"""),
    code(ABERTURA_IMPORTS + r"""
from nexabot.params import PARAMS
from nexabot import timed

print("O orçamento de tempo do NexaBot")
print("-" * 52)
print(f"  período de amostragem Ts    : {PARAMS.Ts*1000:6.1f} ms")
print(f"  prazo máximo para zerar torque: {PARAMS.d_stop_max*1000:6.1f} ms")
print(f"  ou seja, em períodos          : {timed.LIMITE_PERIODOS:6d} ciclos")
print()
print(f"  velocidade máxima admitida    : {PARAMS.v_max_safe:6.2f} m/s")

distancia = PARAMS.v_max_safe * PARAMS.d_stop_max
print(f"  distância percorrida no prazo : {distancia*100:6.1f} cm")
print()
print("Ou seja: entre o obstáculo aparecer e o torque zerar, o robô ainda")
print(f"anda {distancia*100:.0f} centímetros. É por isso que o prazo é 150 ms e não")
print("500 ms — e é por isso que ele precisa ser PROVADO, não estimado.")
"""),

    md("""
## Passo 2 — O caso feliz

Primeiro, o caminho que todo mundo imagina: o sensor detecta na hora, o
controlador reage no ciclo seguinte, o torque cai.

Quantos ciclos isso leva?
"""),
    code(r"""
caminhos_ideais = timed.explorar_caminhos(atraso_deteccao_max=0,
                                          permite_ciclo_perdido=False)
melhor = min(caminhos_ideais, key=lambda c: c.periodos_ate_zerar)
pior_ideal = max(caminhos_ideais, key=lambda c: c.periodos_ate_zerar)

print("Cenário ideal: sensor sem atraso, nenhum ciclo perdido")
print("-" * 56)
print(f"  caminhos possíveis     : {len(caminhos_ideais)}")
print(f"  melhor caso            : {melhor.periodos_ate_zerar:3d} ciclos "
      f"({melhor.ms_ate_zerar:5.1f} ms)")
print(f"  pior caso deste cenário: {pior_ideal.periodos_ate_zerar:3d} ciclos "
      f"({pior_ideal.ms_ate_zerar:5.1f} ms)")
print(f"  limite do requisito    : {timed.LIMITE_PERIODOS:3d} ciclos "
      f"({PARAMS.d_stop_max*1000:5.1f} ms)")
print()
print("Folga enorme. Se você testasse só isso, dormiria tranquilo.")
"""),

    md("""
## Passo 3 — O pior caso, que ninguém testa

Agora ligamos as imperfeições reais:

- o sensor pode atrasar até 2 ciclos (filtro anti-ruído);
- um ciclo de atuação pode se perder.

A ferramenta vai enumerar **todas as combinações possíveis** desses atrasos e
achar a pior.
"""),
    code(r"""
resultado = timed.verificar_req_safe_006(atraso_deteccao_max=2,
                                         permite_ciclo_perdido=True)

print("Cenário realista: sensor atrasa até 2 ciclos, 1 ciclo pode se perder")
print("-" * 62)
print(f"  caminhos explorados : {resultado.n_caminhos_explorados}")
print(f"  PIOR CASO           : {resultado.pior_caso_periodos} ciclos "
      f"({resultado.pior_caso_ms:.1f} ms)")
print(f"  limite do requisito : {resultado.limite_periodos} ciclos "
      f"({resultado.limite_ms:.1f} ms)")
print()
print(f"  REQ-SAFE-006: {'PASSOU' if resultado.ok else 'REPROVOU'}")

folga = resultado.limite_periodos - resultado.pior_caso_periodos
print(f"  folga restante      : {folga} ciclos ({folga*PARAMS.Ts*1000:.0f} ms)")
print()
print("E aqui está o caminho do pior caso — a sequência exata de")
print("infortúnios que produz o atraso máximo:")
print()
print(timed.formatar_caminho_temporizado(resultado.pior_caminho))
"""),

    md("""
### O que acabou de acontecer

Você provou uma afirmação forte:

> Não existe combinação de atrasos, dentro do envelope declarado, que faça o
> torque demorar mais que o pior caso medido.

Não é "testamos muito e não vimos". É "enumeramos todas as combinações".

E repare que o pior caso é bem mais lento que o caso feliz do Passo 2. Essa
diferença é exatamente o que um teste de bancada esconderia.
"""),

    md("""
## Passo 4 — Onde o requisito quebra

Um requisito que passa com folga não te ensina onde está a fronteira.

Vamos empurrar: e se o sensor atrasar mais? Em algum ponto o prazo estoura, e
é útil saber **onde**, porque isso vira uma especificação para quem compra o
sensor.

Repare que os atrasos aqui vão bem além do realista. Não é para simular um
sensor plausível — é para **achar a fronteira**. Saber onde o projeto quebra
vale tanto quanto saber que ele passa.
"""),
    code(r"""
print(f"{'atraso do sensor':>18}  {'ciclo perdido':>14}  {'pior caso':>18}  requisito")
print("-" * 72)
fronteira = None
for atraso in (0, 2, 5, 10, 20, 25, 26, 27, 28, 30):
    for perdido in (False, True):
        r = timed.verificar_req_safe_006(atraso_deteccao_max=atraso,
                                         permite_ciclo_perdido=perdido)
        marca = "PASSOU" if r.ok else "REPROVOU"
        if not r.ok and fronteira is None:
            fronteira = (atraso, perdido)
        print(f"{atraso:>13} ciclos  {str(perdido):>14}  "
              f"{r.pior_caso_periodos:>3d} ciclos ({r.pior_caso_ms:5.1f} ms)  {marca}")

print()
if fronteira:
    print(f"O requisito quebra a partir de {fronteira[0]} ciclos de atraso do")
    print(f"sensor, ou seja {fronteira[0]*PARAMS.Ts*1000:.0f} ms.")
    print()
    print("Isso é uma ESPECIFICAÇÃO DE COMPRA. Ao escolher o sensor de")
    print(f"obstáculo, o atraso de detecção dele precisa ficar abaixo de")
    print(f"{fronteira[0]*PARAMS.Ts*1000:.0f} ms. Antes desta análise esse número não existia —")
    print("alguém teria escrito 'sensor rápido' na especificação, e o")
    print("fornecedor teria entregue o que ele acha que é rápido.")
else:
    print("O requisito passou em todos os cenários testados.")
"""),

    md("""
### O gráfico da margem

Quanto do orçamento de 150 ms cada cenário consome.

A linha vermelha é o limite. Enquanto as barras ficarem abaixo dela, o projeto
está dentro do prazo — e a distância até a linha é a sua margem de segurança.
"""),
    code(r"""
import matplotlib.pyplot as plt
import numpy as np

atrasos = [0, 2, 5, 10, 15, 20, 25, 27, 28, 30]
piores = []
for a in atrasos:
    r = timed.verificar_req_safe_006(atraso_deteccao_max=a, permite_ciclo_perdido=True)
    piores.append(r.pior_caso_ms)

cores = ["#4A9D5F" if p <= resultado.limite_ms else "#C0392B" for p in piores]

fig, ax = plt.subplots(figsize=(9.5, 5))
ax.bar([a * PARAMS.Ts * 1000 for a in atrasos], piores,
       width=5.0, color=cores, edgecolor="white")
ax.axhline(resultado.limite_ms, color="#C0392B", linestyle="--", linewidth=2)
ax.text(2, resultado.limite_ms + 5, f"limite do requisito: {resultado.limite_ms:.0f} ms",
        color="#C0392B", fontsize=10.5)
ax.annotate("aqui o projeto reprova", xy=(140, piores[-1]), xytext=(85, piores[-1] + 25),
            fontsize=10, color="#C0392B",
            arrowprops=dict(arrowstyle="->", color="#C0392B"))

ax.set_xlabel("atraso de detecção do sensor [ms]")
ax.set_ylabel("pior caso até o torque zerar [ms]")
ax.set_title("Quanto do orçamento de 150 ms cada cenário consome",
             fontsize=13, pad=12)
ax.grid(alpha=0.25, axis="y")
plt.tight_layout()
plt.show()
"""),

    md("""
## Mexa aqui

**Experimento 1 — um sensor melhor.**
Rode com `ATRASO = 0`. Quanta margem você ganha? Vale a diferença de preço de
um sensor mais rápido? Essa é a conversa que a análise permite ter com o
setor de compras.

**Experimento 2 — amostrar mais rápido.**
E se `Ts` fosse 2 ms em vez de 5? O prazo em milissegundos é o mesmo, mas cabe
mais ciclos dentro dele. Diminuir `Ts` compra margem — e custa CPU, como você
viu na Aula 7.

**Experimento 3 — dois ciclos perdidos.**
O modelo hoje admite **um** ciclo perdido. Se a rede do robô for pior e
puder perder dois, o requisito ainda passa? Se não passar, você acabou de
descobrir um requisito de rede.
"""),
    code(r"""
# ⬇️ mexa aqui
ATRASO = 2
CICLO_PERDIDO = True

r_x = timed.verificar_req_safe_006(atraso_deteccao_max=ATRASO,
                                   permite_ciclo_perdido=CICLO_PERDIDO)

print(f"atraso do sensor = {ATRASO} ciclos ({ATRASO*PARAMS.Ts*1000:.0f} ms)")
print(f"ciclo perdido    = {CICLO_PERDIDO}")
print("-" * 52)
print(f"caminhos explorados : {r_x.n_caminhos_explorados}")
print(f"pior caso           : {r_x.pior_caso_ms:6.1f} ms")
print(f"limite              : {r_x.limite_ms:6.1f} ms")
print(f"margem              : {r_x.limite_ms - r_x.pior_caso_ms:6.1f} ms "
      f"({100*(1 - r_x.pior_caso_ms/r_x.limite_ms):.0f}% do orçamento)")
print()
print("REQ-SAFE-006:", "PASSOU" if r_x.ok else "REPROVOU")
"""),

    md("""
## Aprofundamento (opcional)

### O que ficou de fora

Autômatos temporizados têm uma teoria bonita por trás: **invariantes de
localização** (condições que precisam valer enquanto o sistema fica num
estado), **guardas** (condições de relógio que liberam uma transição) e
**regiões de relógio** (a técnica que torna o problema decidível apesar de o
tempo ser contínuo).

Nada disso é necessário para entender que *o pior caso precisa ser enumerado,
não estimado* — que é a ideia da aula. A teoria completa está no material
complementar.

### Contraparte industrial: UPPAAL

A ferramenta padrão para autômatos temporizados chama-se **UPPAAL**. Ela tem
editor gráfico, simulador e verificador, e é usada em projeto de sistemas
embarcados críticos há décadas.

O verificador desta disciplina é um enumerador simples em Python, para você
**ver os caminhos sendo percorridos**. O UPPAAL faz o mesmo com muito mais
sofisticação — e com uma curva de aprendizado que não cabe nesta unidade.

### Por que o watchdog é diferente de tudo o mais

Todos os outros requisitos protegem contra o software fazer a coisa errada.

O watchdog protege contra o software **parar de fazer qualquer coisa**. Se a
tarefa travar num laço infinito, nenhum teste interno percebe — o código que
detectaria também travou.

Por isso o watchdog é hardware, ou pelo menos independente. Ele conta sozinho,
e se ninguém o alimentar no prazo, ele age. A célula abaixo mostra o
orçamento dele.
"""),
    code(r"""
print("Orçamento do watchdog do NexaBot")
print("-" * 52)
periodo_alimentacao = PARAMS.Ts
print(f"  o software alimenta o watchdog a cada : {periodo_alimentacao*1000:6.1f} ms")
print(f"  o watchdog dispara se ficar sem comer : {PARAMS.d_stop_max*1000:6.1f} ms")
print(f"  ou seja, tolera perder até            : "
      f"{PARAMS.d_stop_max/periodo_alimentacao:6.0f} refeições seguidas")
print()
print("Escolher esse número é um compromisso:")
print("  muito curto  -> dispara à toa, num atraso normal de escalonamento")
print("  muito longo  -> o robô anda tempo demais com o software travado")
print()
print(f"O NexaBot adotou {PARAMS.d_stop_max*1000:.0f} ms, o mesmo prazo do REQ-SAFE-006.")
print("Não é coincidência: um software travado e um software lento demais")
print("produzem o mesmo perigo, então merecem o mesmo prazo.")
"""),

    md("""
## O que você leva desta aula

1. **"Rápido" não é requisito.** "Em até 150 ms" é, porque dá para provar ou
   reprovar.
2. **Relógio no modelo é um cronômetro** que anda, zera e pode ser consultado.
3. **O pior caso é uma combinação rara de infortúnios**, e é por isso que teste
   de bancada não o encontra.
4. **Enumerar todos os cenários dá um número defensável** — e a folga que
   sobra é a sua margem.
5. **A fronteira vira especificação de compra.** Você descobriu qual atraso
   máximo o sensor pode ter.
6. **Watchdog protege contra o software ter parado**, coisa que o próprio
   software não consegue detectar.

Na Aula 12 a pergunta vira: os seus testes estão **cobrindo** o que deveriam?
E você vai descobrir que "todos passaram" pode significar muito pouco.

## Se deu erro

**A varredura do Passo 4 demora.**
O número de caminhos cresce com o atraso permitido. Reduza o `range` para
`range(0, 6)`.

**`MemoryError` com atraso alto.**
É a explosão de estados da Aula 10 aparecendo aqui. Com atraso muito grande, o
número de combinações estoura. Isso é a técnica mostrando o próprio limite.

**O pior caso deu igual ao melhor.**
Confira se você passou `permite_ciclo_perdido=True`. Com ele em `False` e
atraso zero, só existe um caminho.
""" + RODAPE_ERRO),
]
