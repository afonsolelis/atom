"""Notebook da Aula 10 — testar todos os caminhos, não uma amostra."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import ABERTURA_IMPORTS, GLOSSARIO, RODAPE_ERRO, md, code  # noqa: E402

TITULO = "Aula 10 — Testar tudo, não uma amostra"
SLUG = "model_checking"

CELULAS = [
    md("""
# Aula 10 — Testar tudo, não uma amostra

## O que você vai fazer aqui

Você já testou software. Escreveu uns casos, rodou, passou, ficou feliz.

Só que "passou nos meus testes" e "está correto" são coisas muito diferentes.
Seus testes cobriram os casos que **você pensou**. O bug mora nos que você não
pensou.

Hoje você vai usar uma ferramenta que percorre **todos os caminhos possíveis**
do supervisor do NexaBot. Não uma amostra grande: todos. E quando ela achar um
problema, vai te entregar a sequência exata de passos que leva até ele.

**Tempo:** cerca de 35 minutos.
**Pré-requisito:** notebook da Aula 9.
"""),

    md("""
## Antes de começar

### 1. Espaço de estados — o mapa de todas as situações

Pense num jogo da velha. Ele tem um número finito de tabuleiros possíveis. Dá
para desenhar **todos** eles, ligados por setas de "jogada".

Esse desenho completo chama-se **espaço de estados**. Nele, cada bolinha é uma
situação e cada seta é uma coisa que pode acontecer.

O supervisor do NexaBot também tem um espaço de estados, e ele é pequeno:

- **6 estados possíveis** — OCIOSO, MOVENDO, DESACELERANDO, PARADO_OBSTACULO,
  FALHA, EMERGENCIA
- **entradas** — botão de partir, botão de parar, obstáculo, emergência, falha
  de encoder, rearme, e a velocidade

Pequeno o bastante para o computador desenhar o mapa inteiro em fração de
segundo. É por isso que o supervisor foi projetado assim: **para ser
verificável**.

### 2. Busca em largura

O jeito de percorrer o mapa. Em português comum:

1. Comece no estado inicial.
2. Aplique **todas** as entradas possíveis e anote onde cada uma leva.
3. Para cada estado novo que apareceu, repita.
4. Pare quando não aparecer estado novo nenhum.

É como explorar um labirinto abrindo todas as portas de um corredor antes de
avançar para o próximo. Chama-se **busca em largura** porque avança nivelado,
em vez de mergulhar num caminho só.

Garantia: se um estado é alcançável, essa busca **vai** achá-lo.

### 3. Testar não é provar

Guarde esta frase:

> **Testar mostra a presença de defeitos, nunca a ausência.**

É de Dijkstra, e é a razão de existir esta aula.

- Você rodou 500 testes e passaram todos → você sabe que aqueles 500 casos
  estão bons. Nada além disso.
- O verificador percorreu **todo** o espaço de estados e não achou violação →
  aí sim, não existe violação. Dentro do modelo.

Essa última frase — "dentro do modelo" — é importante e volta no fim da aula.

### 4. LTL, em dois símbolos

**LTL** quer dizer *Linear Temporal Logic*, lógica temporal linear. É uma
notação para dizer coisas sobre o tempo.

Você só precisa de dois símbolos:

| Símbolo | Lê-se | Significa |
| --- | --- | --- |
| **G** | *globally* | "sempre, em todo instante" |
| **F** | *finally* | "uma hora, em algum instante" |

Exemplos com os requisitos que você já conhece:

- `G(obstaculo → ¬torque)` — *"sempre: se tem obstáculo, então não tem torque"*
- `F(estado = MOVENDO)` — *"uma hora o robô se move"*

O `→` é "então" e o `¬` (lê-se "não") nega. Só isso.
"""),

    md(GLOSSARIO),

    md("""
## Passo 1 — Desenhando o mapa inteiro

A célula abaixo percorre todo o espaço de estados do supervisor.

Repare no tempo que leva. Isso é o mapa **completo** — não uma amostra, não um
teste aleatório. Tudo.
"""),
    code(ABERTURA_IMPORTS + r"""
from nexabot import modelcheck
from nexabot.supervisor import Estado

resultado = modelcheck.explorar()

print(f"Exploração completa em {resultado.tempo_s*1000:.1f} ms")
print("-" * 52)
print(f"Estados alcançáveis : {len(resultado.estados_alcancaveis)}")
print(f"Transições testadas : {len(resultado.transicoes)}")
print()
print("Os estados que o supervisor consegue alcançar:")
for estado in sorted(resultado.estados_alcancaveis, key=lambda e: e.name):
    print(f"  {estado.name}")

nao_alcancados = set(Estado) - resultado.estados_alcancaveis
if nao_alcancados:
    print()
    print("Estados que existem no código mas NUNCA são alcançados:")
    for e in sorted(nao_alcancados, key=lambda e: e.name):
        print(f"  {e.name}  ← código morto, ou bug de projeto")
else:
    print()
    print("Todos os estados declarados são alcançáveis. Nenhum código morto.")
"""),

    md("""
### O que "testadas" significa aqui

Aquele número de transições não é "casos de teste que escrevemos". É
**origem × entrada**, para toda origem alcançável e toda entrada possível.

Compare com um teste manual honesto: um bom engenheiro escreve talvez 20 ou 30
casos para um supervisor desses. O verificador cobriu ordens de grandeza mais,
em milissegundos, e sem esquecer nenhum.
"""),
    code(r"""
entradas = modelcheck.gerar_entradas_possiveis()

print(f"Entradas distintas consideradas : {len(entradas)}")
print(f"Estados alcançáveis             : {len(resultado.estados_alcancaveis)}")
print(f"Produto (todas as combinações)  : "
      f"{len(entradas) * len(resultado.estados_alcancaveis)}")
print(f"Transições realmente exploradas : {len(resultado.transicoes)}")
print()
print("Exemplo de uma entrada, com os campos que estão ativos:")
for e in entradas[:3]:
    print(f"  {modelcheck.formatar_entrada(e)}")
print("  ...")
print()
print("Uma suíte manual caprichada teria umas 30 casos. Aqui foram")
print(f"{len(resultado.transicoes)}, e nenhum foi escolhido por alguém — foram")
print("todos, por construção.")
"""),

    md("""
## Passo 2 — Verificando os requisitos em todas as transições

Agora a parte que importa: pegar os predicados da Aula 9 e aplicá-los a **cada
uma** das transições exploradas.

Se nenhum reprovar, você tem uma afirmação forte: *dentro deste modelo, esses
requisitos valem sempre*.
"""),
    code(r"""
from nexabot import requisitos

violacoes = modelcheck.verificar_invariantes(resultado, requisitos.REQUISITOS_TRANSICAO)

print("Verificando cada requisito de segurança em cada transição:")
print()
for req in requisitos.REQUISITOS_TRANSICAO:
    falhas = [v for v in violacoes if v.requisito.id == req.id]
    marca = "PASSOU" if not falhas else f"REPROVOU ({len(falhas)} violações)"
    print(f"  {req.id}  {marca}")

print()
print(f"Total de violações: {len(violacoes)}")
print()
if not violacoes:
    print("Nenhuma violação em nenhuma das", len(resultado.transicoes), "transições.")
    print()
    print("Repare no que isso é e no que não é:")
    print("  É: prova de que, DENTRO DESTE MODELO, os requisitos valem sempre.")
    print("  Não é: garantia de que o robô real é seguro. O modelo pode estar")
    print("         incompleto, e o código embarcado pode divergir dele.")
    print("         As Aulas 13 a 16 tratam justamente dessa distância.")
"""),

    md("""
## Passo 3 — Verificando vivacidade

Segurança é "nunca acontece". A verificação é por transição.

**Vivacidade é diferente**: "uma hora acontece". Não adianta olhar transição
por transição — é preciso procurar um caminho que chegue lá.

E quando encontra, a ferramenta devolve o caminho como **testemunha**: a
sequência exata de entradas que leva ao estado desejado.
"""),
    code(r"""
for req in requisitos.REQUISITOS_ALCANCABILIDADE:
    alcancavel, caminho = modelcheck.verificar_alcancabilidade(resultado, req)
    print(f"{req.id}: {req.descricao}")
    print(f"  alcançável? {'SIM' if alcancavel else 'NÃO'}")
    if alcancavel:
        print(f"  em {len(caminho)} passo(s). A testemunha:")
        print()
        print(modelcheck.formatar_caminho(caminho))
    print()
"""),

    md("""
## Passo 4 — O contraexemplo, que é o produto de verdade

Um verificador que só diz "passou" ou "reprovou" não serve para muita coisa.

O valor está no **contraexemplo**: quando reprova, a ferramenta entrega a
sequência exata de passos que leva ao problema. Você não precisa investigar —
ela te dá o roteiro para reproduzir.

Vamos ver isso funcionando. A célula abaixo introduz um bug de propósito no
supervisor e manda o verificador achá-lo.

O bug: em `EMERGENCIA`, alguém "otimizou" o código e deixou o torque ligado
quando o robô já está parado. Parece inofensivo. Não é.
"""),
    code(r"""
from nexabot.supervisor import transition, Saidas

def transition_com_bug(estado, entradas):
    destino, saida = transition(estado, entradas)
    # ⬇️ o bug: "se já está parado, não precisa cortar o torque, né?"
    if destino == Estado.EMERGENCIA and entradas.parado():
        saida = Saidas(torque_habilitado=True, freio_acionado=saida.freio_acionado)
    return destino, saida


resultado_bug = modelcheck.explorar(transition_fn=transition_com_bug)
violacoes_bug = modelcheck.verificar_invariantes(
    resultado_bug, requisitos.REQUISITOS_TRANSICAO)

print(f"Com o bug introduzido: {len(violacoes_bug)} violações encontradas")
print()
if violacoes_bug:
    v = violacoes_bug[0]
    print(f"Requisito quebrado: {v.requisito.id}")
    print(f"  {v.requisito.descricao}")
    print()
    print("CONTRAEXEMPLO — a sequência exata que quebra o requisito:")
    print()
    print(modelcheck.formatar_caminho(v.caminho))
    print()
    print("Isso é o que você leva para quem vai consertar. Não 'tem um bug em")
    print("algum lugar da emergência': a receita completa para reproduzir.")
"""),

    md("""
### Por que teste manual não pegaria

Olhe a sequência do contraexemplo. Ela exige uma combinação bem específica:
emergência pressionada **e** robô já parado.

Quem escreve teste manual testa emergência com o robô andando — é o caso que
vem à cabeça. Testar emergência com o robô já parado parece redundante.

É exatamente por isso que o bug sobrevive à revisão. Ele mora num caso que
ninguém julga interessante.

A célula abaixo mostra que uma suíte manual razoável passaria batido.
"""),
    code(r"""
from nexabot.supervisor import Entradas

# Uma suíte manual "razoável", do tipo que sai numa revisão de código
suite_manual = [
    ("partida normal",        Estado.OCIOSO,   Entradas(comando_partir=True)),
    ("parada normal",         Estado.MOVENDO,  Entradas(comando_parar=True, velocidade=0.5)),
    ("obstáculo em marcha",   Estado.MOVENDO,  Entradas(obstaculo=True, velocidade=0.5)),
    ("emergência em marcha",  Estado.MOVENDO,  Entradas(emergencia=True, velocidade=0.5)),
    ("falha de encoder",      Estado.MOVENDO,  Entradas(falha_encoder=True, velocidade=0.5)),
    ("rearme após falha",     Estado.FALHA,    Entradas(rearme=True)),
]

print(f"{'caso de teste':>24}  resultado")
print("-" * 50)
pegou = False
for nome, origem, entrada in suite_manual:
    destino, saida = transition_com_bug(origem, entrada)
    falhou = [r.id for r in requisitos.REQUISITOS_TRANSICAO
              if not r.verificar_transicao(origem, entrada, saida, destino)]
    if falhou:
        pegou = True
        print(f"{nome:>24}  REPROVOU em {', '.join(falhou)}")
    else:
        print(f"{nome:>24}  passou")

print()
if not pegou:
    print("A suíte manual passou inteira. Seis casos bem pensados, e o bug")
    print("escapou de todos — porque nenhum deles aciona a emergência com o")
    print("robô já parado.")
    print()
    print(f"O verificador, testando as {len(resultado_bug.transicoes)} transições, pegou.")
"""),

    md("""
## Mexa aqui

**Experimento 1 — outro bug.**
Na `transition_com_bug`, troque a condição para quebrar outro requisito. Por
exemplo, permita sair de `FALHA` sem rearme (isso quebra o `REQ-SAFE-004`).
Veja o contraexemplo mudar.

**Experimento 2 — um estado inalcançável.**
Adicione um estado novo ao supervisor que nenhuma transição alcança. A
exploração vai listá-lo como código morto. Na indústria isso é achado de
auditoria: código que nunca roda ou é desnecessário, ou é um caminho que
alguém esqueceu de ligar.

**Experimento 3 — o custo de crescer.**
O supervisor tem 6 estados e algumas entradas booleanas. Some mentalmente uma
sétima entrada booleana: o número de combinações **dobra**. Some dez, e
multiplica por mil. Esse crescimento tem nome e é o limite da técnica —
está no Aprofundamento.
"""),
    code(r"""
# ⬇️ mexa aqui: mude a condição do bug e veja o contraexemplo mudar
def transition_experimento(estado, entradas):
    destino, saida = transition(estado, entradas)
    # exemplo: sair de FALHA sem rearme (quebra o REQ-SAFE-004)
    if estado == Estado.FALHA and entradas.comando_partir:
        destino = Estado.MOVENDO
    return destino, saida


res_x = modelcheck.explorar(transition_fn=transition_experimento)
viol_x = modelcheck.verificar_invariantes(res_x, requisitos.REQUISITOS_TRANSICAO)

print(f"Transições exploradas: {len(res_x.transicoes)}")
print(f"Violações encontradas: {len(viol_x)}")
print()
por_requisito = {}
for v in viol_x:
    por_requisito.setdefault(v.requisito.id, []).append(v)
for req_id, lista in sorted(por_requisito.items()):
    print(f"  {req_id}: {len(lista)} violações")

if viol_x:
    print()
    print("Primeiro contraexemplo:")
    print(modelcheck.formatar_caminho(viol_x[0].caminho))
"""),

    md("""
## Aprofundamento (opcional)

### Explosão de estados

O supervisor do NexaBot tem 6 estados e 6 entradas booleanas mais uma
velocidade amostrada. Cabe folgado na memória.

Agora imagine um sistema com 30 variáveis booleanas. O número de combinações
é 2 elevado a 30 — mais de um bilhão. Com 50 variáveis, passa de mil trilhões.

Isso chama-se **explosão de estados**, e é o limite prático da técnica. A
resposta da engenharia não é uma ferramenta mais rápida: é **projetar o
supervisor pequeno de propósito**, separando a parte crítica de segurança do
resto do software.

O supervisor desta disciplina é pequeno porque foi desenhado para ser
verificável. Essa é uma decisão de arquitetura, não um acaso.

### O que ficou de fora

Existe uma segunda lógica temporal, **CTL** (*Computation Tree Logic*), que
fala sobre a árvore de caminhos possíveis em vez de um caminho linear. Ela
permite dizer coisas como "existe algum caminho em que...".

Ela foi tirada desta aula. LTL com dois operadores já resolve todos os
requisitos do NexaBot, e aprender duas lógicas parecidas ao mesmo tempo é a
receita para não aprender nenhuma. CTL está no material complementar da
unidade.

### Contraparte industrial

Esta disciplina usa um verificador escrito em Python, em algumas centenas de
linhas, para que você **veja o espaço de estados sendo percorrido**. Um botão
que devolve "property satisfied" ensina menos.

Na indústria usa-se NuSMV, SPIN, TLA+ ou UPPAAL. A mecânica é a mesma: modelo,
propriedade, busca exaustiva, contraexemplo.
"""),
    code(r"""
print("Quanto o espaço de estados cresce:")
print()
print(f"{'variáveis booleanas':>22}  {'combinações':>22}")
print("-" * 48)
for n in (6, 10, 20, 30, 50):
    combinacoes = 2 ** n
    print(f"{n:>22}  {combinacoes:>22,}".replace(",", "."))

print()
print(f"O supervisor do NexaBot explorou {len(resultado.transicoes)} transições")
print(f"em {resultado.tempo_s*1000:.1f} ms. Um sistema com 50 booleanos não caberia")
print("em nenhum computador — nem hoje, nem daqui a cem anos.")
print()
print("A saída não é força bruta. É manter pequeno o pedaço que precisa")
print("ser provado.")
"""),

    md("""
## O que você leva desta aula

1. **Espaço de estados é o mapa de todas as situações possíveis**, com as
   setas do que pode acontecer.
2. **Busca em largura percorre esse mapa inteiro** e garante achar tudo o que
   é alcançável.
3. **Testar mostra presença de defeito, nunca ausência.** Verificar exaustiva-
   mente é outra coisa.
4. **O contraexemplo é o produto.** Ele te entrega a receita para reproduzir o
   bug, não um alarme genérico.
5. **Explosão de estados é o limite.** A resposta é projetar pequeno, não
   comprar máquina maior.
6. **"Provado dentro do modelo" não é "seguro na prática".** O modelo pode
   estar incompleto, e o código pode divergir dele.

Na Aula 11 entra o relógio: como provar que algo acontece **em até 150
milissegundos**, e não apenas "uma hora".

## Se deu erro

**A exploração não termina.**
Se você mexeu na função de transição e criou um estado novo a cada passo, o
espaço fica infinito. Confira que a sua transição sempre devolve um dos
estados do `Estado`.

**Nenhuma violação apareceu no bug.**
Confira se a sua condição realmente é alcançável. Um bug num caminho que nunca
acontece não é violação — e descobrir isso já é informação útil.

**`formatar_caminho` imprimiu vazio.**
Acontece quando a violação está na primeira transição, saindo do estado
inicial. O caminho até a origem é vazio mesmo.
""" + RODAPE_ERRO),
]
