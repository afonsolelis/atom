"""Notebook da Aula 9 — a frase em português que vira três programas."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import ABERTURA_IMPORTS, GLOSSARIO, RODAPE_ERRO, md, code  # noqa: E402

TITULO = "Aula 9 — A frase que vira três programas diferentes"
SLUG = "requisito_formal"

CELULAS = [
    md("""
# Aula 9 — A frase que vira três programas diferentes

## O que você vai fazer aqui

A Unidade 2 terminou com um robô que funciona. Agora a pergunta muda: **como
você prova que ele funciona?**

E antes disso vem uma pergunta pior: **funciona fazendo o quê, exatamente?**

Hoje você vai pegar um requisito escrito em português — daqueles que todo
mundo lê e acha claro — e descobrir que três programadores o transformariam em
três programas diferentes. Depois vai reescrevê-lo de um jeito que não admite
leitura dupla.

**Pré-requisito:** ter passado pela Unidade 2. Não precisa de matemática nova.
"""),

    md("""
## Antes de começar

### 1. A ambiguidade não é do técnico, é da língua

Antes de qualquer requisito de engenharia, um bilhete de geladeira:

> *"Compre pão. Se tiver ovo, traga uma dúzia."*

A pessoa voltou com **doze pães**.

Ela errou? Leia de novo. "Se tiver ovo, traga uma dúzia" — uma dúzia de quê?
A frase não diz. As duas leituras cabem.

Requisito de software é exatamente isso, só que caro. E a saída não é "escrever
melhor" — é escrever de um jeito que **só permita uma leitura**.

### 2. O que é um predicado

Um **predicado** é uma pergunta que só aceita **sim ou não**.

- "A velocidade está acima de 1,2 m/s?" → é predicado.
- "A velocidade está boa?" → não é. "Boa" não tem resposta objetiva.

Todo requisito verificável vira um predicado, ou um conjunto deles. Se você
não consegue transformá-lo numa pergunta de sim ou não, ele ainda não está
pronto.

### 3. Os dois tipos que interessam

Existe uma taxonomia grande de propriedades formais. Você precisa de **duas**:

| Tipo | Formato | Exemplo |
| --- | --- | --- |
| **Segurança** (*safety*) | "**nunca** acontece X" | O torque nunca fica ligado com obstáculo detectado |
| **Vivacidade** (*liveness*) | "**uma hora** acontece Y" | Depois de um rearme, o robô uma hora volta a andar |

A diferença prática é grande:

- Uma propriedade de **segurança** é quebrada por **um único momento ruim**.
  Basta achar um instante em que X aconteceu.
- Uma de **vivacidade** é quebrada por **um caminho infinito** em que Y nunca
  acontece.

Segurança diz o que não pode. Vivacidade diz que algo bom não pode ser adiado
para sempre. Um sistema que nunca liga o motor satisfaz todas as propriedades
de segurança do mundo — e é inútil. Por isso as duas.
"""),

    md(GLOSSARIO),

    md("""
## Passo 1 — O requisito ambíguo

Aqui está o requisito, como ele chegaria do cliente:

> **REQ-SAFE-001** — *"O robô deve parar quando detectar um obstáculo."*

Todo mundo lê e concorda. Agora responda três perguntas:

1. **"Parar" é o quê?** Cortar o torque? Acionar o freio? Chegar a velocidade
   zero? São três coisas diferentes, com tempos diferentes.
2. **"Quando" é quando?** No mesmo ciclo? Em até quanto tempo?
3. **E se o obstáculo sumir no meio da parada?** Volta a andar? Continua
   parando?

Três leituras, três programas. A célula abaixo implementa as três e mostra que
elas discordam.
"""),
    code(ABERTURA_IMPORTS + r"""
from nexabot.supervisor import Estado, Entradas

# Três programadores leem "o robô deve parar quando detectar um obstáculo".

def leitura_A(estado, entradas):
    # "Parar = cortar o torque, imediatamente."
    if entradas.obstaculo:
        return "torque cortado"
    return "torque mantido"

def leitura_B(estado, entradas):
    # "Parar = desacelerar até a velocidade zerar."
    if entradas.obstaculo and not entradas.parado():
        return "desacelerando"
    if entradas.obstaculo:
        return "torque cortado"
    return "torque mantido"

def leitura_C(estado, entradas):
    # "Parar = cortar torque E travar até alguém rearmar."
    if estado == Estado.PARADO_OBSTACULO:
        return "travado, aguarda rearme"
    if entradas.obstaculo:
        return "torque cortado"
    return "torque mantido"


cenario = Entradas(obstaculo=True, velocidade=0.6)
print("Cenário: obstáculo detectado, robô a 0,6 m/s")
print("-" * 52)
for nome, f in (("A", leitura_A), ("B", leitura_B), ("C", leitura_C)):
    print(f"  Leitura {nome}: {f(Estado.MOVENDO, cenario)}")

print()
print("Agora o obstáculo sumiu, e o robô já estava parado:")
print("-" * 52)
depois = Entradas(obstaculo=False, velocidade=0.0)
for nome, f in (("A", leitura_A), ("B", leitura_B), ("C", leitura_C)):
    print(f"  Leitura {nome}: {f(Estado.PARADO_OBSTACULO, depois)}")

print()
print("Repare na segunda tabela: A e B mandam o robô voltar a andar sozinho.")
print("C mantém travado. Num armazém com pessoas circulando, essa diferença")
print("é a diferença entre um susto e um acidente.")
"""),

    md("""
## Passo 2 — A reescrita que não admite dúvida

O conserto não é escrever mais bonito. É escrever de forma que **cada palavra
tenha um teste**.

O requisito reescrito fica assim:

> **REQ-SAFE-001** — Sempre que a entrada `obstaculo` for verdadeira, a saída
> `torque_habilitado` deve ser falsa **no mesmo ciclo de amostragem**. O
> supervisor deve permanecer no estado `PARADO_OBSTACULO` até receber
> `rearme`, mesmo que `obstaculo` volte a ser falsa.

Compare com o original. Nada de "deve parar". Agora tem:

- **qual entrada** (`obstaculo`)
- **qual saída** (`torque_habilitado`)
- **quando** (no mesmo ciclo)
- **até quando** (até `rearme`)
- **o caso difícil resolvido** (obstáculo sumir não libera)

Cada um desses vira um teste. É por isso que a reescrita vale a pena.
"""),
    code(r"""
from nexabot import requisitos

print("Os requisitos formais do NexaBot, como estão no código:")
print()
for req in requisitos.REQUISITOS:
    tipo_legivel = {
        "invariante": "segurança — nunca acontece",
        "seguranca": "segurança — nunca acontece",
        "alcancabilidade": "vivacidade — uma hora acontece",
        "vivacidade": "vivacidade — uma hora acontece",
        "invariante_continuo": "segurança, mas no mundo contínuo",
        "temporizado": "segurança com prazo",
    }.get(req.tipo, req.tipo)
    print(f"  {req.id}  [{tipo_legivel}]")
    print(f"      {req.descricao}")
    print()
"""),

    md("""
## Passo 3 — Do texto ao predicado executável

Aqui está a virada da aula.

O requisito reescrito não é um comentário no documento. Ele é **uma função
Python que devolve `True` ou `False`**.

Olhe o código do `REQ-SAFE-001` abaixo: ele recebe uma transição do supervisor
(o estado de antes, as entradas, as saídas e o estado de depois) e responde uma
única pergunta — *essa transição respeitou o requisito?*

A partir do momento em que o requisito é uma função, um computador consegue
testá-la em **todas** as transições possíveis. É isso que a Aula 10 vai fazer.
"""),
    code(r"""
import inspect

req1 = requisitos.por_id("REQ-SAFE-001")
print(f"{req1.id}: {req1.descricao}")
print()
print("E aqui está ele como código executável:")
print()
print(inspect.getsource(req1.verificar_transicao))
"""),

    md("""
### Testando o predicado à mão

Antes de deixar o computador testar tudo, teste você mesmo dois casos: um que
respeita e um que viola.

O segundo é uma transição **inventada por nós**, que o supervisor real nunca
produziria. Serve para confirmar que o predicado realmente pega a violação —
um teste que nunca falha não prova nada.
"""),
    code(r"""
from nexabot.supervisor import Saidas, transition

# Caso 1: o supervisor de verdade, com obstáculo
entrada = Entradas(obstaculo=True, velocidade=0.5)
destino, saida = transition(Estado.MOVENDO, entrada)
ok = req1.verificar_transicao(Estado.MOVENDO, entrada, saida, destino)

print("Caso 1 — o supervisor real, com obstáculo detectado:")
print(f"  MOVENDO + obstáculo  ->  {destino.name}")
print(f"  torque habilitado?   {saida.torque_habilitado}")
print(f"  REQ-SAFE-001 passou? {ok}")
print()

# Caso 2: uma transição inventada, que mantém o torque com obstáculo
saida_ruim = Saidas(torque_habilitado=True, freio_acionado=False)
ok_ruim = req1.verificar_transicao(Estado.MOVENDO, entrada, saida_ruim, Estado.MOVENDO)

print("Caso 2 — uma transição INVENTADA, que ignora o obstáculo:")
print(f"  MOVENDO + obstáculo  ->  MOVENDO")
print(f"  torque habilitado?   {saida_ruim.torque_habilitado}")
print(f"  REQ-SAFE-001 passou? {ok_ruim}")
print()
if ok and not ok_ruim:
    print("O predicado aprovou o certo e reprovou o errado. Ele funciona.")
    print()
    print("Isso importa mais do que parece: um teste que nunca reprova nada")
    print("não é um teste, é decoração. Sempre confira que o seu verificador")
    print("consegue falhar.")
"""),

    md("""
## Passo 4 — Os dois tipos, lado a lado

Volte à tabela do começo. Agora com os requisitos reais do NexaBot.
"""),
    code(r"""
print("SEGURANÇA — 'nunca acontece'")
print("Verificáveis olhando cada transição isoladamente.")
print("-" * 62)
for req in requisitos.REQUISITOS_TRANSICAO:
    print(f"  {req.id}: {req.descricao[:56]}")

print()
print("VIVACIDADE — 'uma hora acontece'")
print("Exigem procurar um caminho que chegue lá.")
print("-" * 62)
for req in requisitos.REQUISITOS_ALCANCABILIDADE:
    print(f"  {req.id}: {req.descricao[:56]}")

print()
print("Por que a distinção importa na prática:")
print()
print("  Para reprovar uma propriedade de SEGURANÇA, basta achar UM")
print("  momento ruim. O contraexemplo é curto e óbvio.")
print()
print("  Para reprovar uma de VIVACIDADE, é preciso mostrar um caminho")
print("  em que a coisa boa NUNCA acontece. É mais difícil de achar e")
print("  mais difícil de explicar para quem vai consertar.")
"""),

    md("""
## Mexa aqui

**Experimento 1 — o requisito da velocidade.**
Escreva o predicado de `REQ-SAFE-005` você mesmo, sem olhar: *"a velocidade
nunca passa de 1,2 m/s"*. Depois compare com o que está no código. Você
lembrou de tratar velocidade negativa (robô andando de ré)?

**Experimento 2 — quebre o supervisor.**
Na célula abaixo, modifique a função `transition_quebrada` para permitir
torque com obstáculo. Veja qual requisito reprova. Esse é o ciclo de trabalho
real: você mexe no código, o verificador aponta o que quebrou.

**Experimento 3 — o requisito impossível.**
Tente escrever, em português sem ambiguidade, o requisito *"o robô deve ser
seguro"*. Você vai descobrir que não dá — e essa descoberta é o conteúdo da
aula. "Seguro" não é requisito; é um guarda-chuva sobre requisitos.
"""),
    code(r"""
def transition_quebrada(estado, entradas):
    '''Uma cópia do supervisor com um bug introduzido de propósito.'''
    destino, saida = transition(estado, entradas)
    # ⬇️ o bug: se o robô estiver rápido, ignora o obstáculo
    if entradas.obstaculo and entradas.velocidade > 0.5:
        saida = Saidas(torque_habilitado=True, freio_acionado=False)
    return destino, saida


entradas_teste = [
    Entradas(obstaculo=True, velocidade=0.6),
    Entradas(obstaculo=True, velocidade=0.1),
    Entradas(obstaculo=False, velocidade=0.6),
]

print(f"{'entrada':>34}  {'requisito':>16}  resultado")
print("-" * 68)
for e in entradas_teste:
    destino, saida = transition_quebrada(Estado.MOVENDO, e)
    for req in requisitos.REQUISITOS_TRANSICAO:
        passou = req.verificar_transicao(Estado.MOVENDO, e, saida, destino)
        if not passou:
            desc = f"obst={e.obstaculo}, v={e.velocidade}"
            print(f"{desc:>34}  {req.id:>16}  REPROVOU")
print()
print("Um bug que só aparece acima de 0,5 m/s. Em teste manual você")
print("provavelmente não pegaria — quem lembra de testar exatamente essa")
print("faixa? O verificador pega porque testa tudo.")
"""),

    md("""
## Aprofundamento (opcional)

### Por que linguagem natural falha como especificação

Não é falta de capricho de quem escreve. É estrutural:

- **Contexto implícito.** "Parar" significa coisas diferentes num carro, num
  elevador e num robô de armazém. Quem escreve carrega um contexto que quem lê
  não tem.
- **Quantificadores escondidos.** "O robô para quando detecta obstáculo" — em
  toda situação? sempre? na primeira vez? A frase não diz, e o leitor preenche
  sozinho.
- **Silêncio sobre o caso difícil.** O requisito original não dizia nada sobre
  o obstáculo sumir. O silêncio não é neutro: cada programador preenche de um
  jeito.

### A escada da formalização

Não é tudo ou nada. Existe uma escada:

1. **Português corrido** — "o robô deve parar quando detectar obstáculo"
2. **Português estruturado** — "sempre que ENTRADA, então SAÍDA, em até PRAZO"
3. **Predicado executável** — uma função que devolve `True`/`False`
4. **Lógica temporal** — uma fórmula que uma ferramenta verifica exaustivamente

Cada degrau custa mais e entrega mais. Esta disciplina chega ao degrau 3 nesta
aula e ao 4 na Aula 10. Na indústria, subir até o 2 já resolve a maior parte
dos mal-entendidos — e é de graça.
"""),
    code(r"""
print("A escada, aplicada ao REQ-SAFE-001:")
print()
print("1. Português corrido")
print('   "O robô deve parar quando detectar um obstáculo."')
print("   → três leituras possíveis, como você viu no Passo 1")
print()
print("2. Português estruturado")
print('   "SEMPRE QUE obstaculo = verdadeiro,')
print('    ENTÃO torque_habilitado = falso NO MESMO ciclo,')
print('    E o estado permanece PARADO_OBSTACULO ATÉ rearme."')
print("   → uma leitura só, e ainda legível por quem não programa")
print()
print("3. Predicado executável")
print("   → a função que você imprimiu no Passo 3")
print()
print("4. Lógica temporal")
print("   G(obstaculo -> !torque_habilitado)")
print('   lê-se: "globalmente, se obstáculo então não torque"')
print("   → é o que a Aula 10 vai verificar em TODOS os caminhos possíveis")
"""),

    md("""
## O que você leva desta aula

1. **Português ambíguo produz programas diferentes.** Você viu três, e elas
   discordam justamente no caso perigoso.
2. **Predicado é pergunta de sim ou não.** Se não vira predicado, não é
   requisito ainda.
3. **Segurança diz "nunca acontece". Vivacidade diz "uma hora acontece".**
   Um sistema precisa das duas — só segurança se satisfaz não fazendo nada.
4. **Requisito vira função.** E a partir daí um computador testa por você.
5. **Confira que o seu verificador consegue reprovar.** Teste que nunca falha
   não prova nada.

Na Aula 10 você entrega esses predicados a um verificador que percorre **todos
os caminhos possíveis** do supervisor — e não uma amostra deles.

## Se deu erro

**`AttributeError` em `req.verificar_transicao`.**
Alguns requisitos não têm predicado de transição — os de alcançabilidade e o
temporizado. Use `requisitos.REQUISITOS_TRANSICAO`, que já filtra.

**`inspect.getsource` falhou.**
Acontece se o módulo foi carregado de forma incomum. Não é grave: abra
`projeto_nexabot/nexabot/requisitos.py` direto no editor.

**Nenhum requisito reprovou no Experimento 2.**
Confira se você deixou a condição `entradas.velocidade > 0.5` e se está
passando uma entrada com velocidade acima disso.
""" + RODAPE_ERRO),
]
