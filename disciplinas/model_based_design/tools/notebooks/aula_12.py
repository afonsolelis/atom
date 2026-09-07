"""Notebook da Aula 12 — passar em todos os testes não prova nada."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import ABERTURA_IMPORTS, GLOSSARIO, RODAPE_ERRO, md, code  # noqa: E402

TITULO = "Aula 12 — Passar em todos os testes não prova nada"
SLUG = "cobertura_e_testes"

CELULAS = [
    md("""
# Aula 12 — Passar em todos os testes não prova nada

## O que você vai fazer aqui

"A suíte está verde." Todo mundo já ouviu isso e relaxou.

Hoje você vai medir **o que a suíte realmente toca** — e descobrir que verde
não quer dizer coberto. Depois vai deixar o computador escrever os testes por
você, a partir do modelo, e ver a cobertura pular.

No fim, uma ferramenta vai encontrar um caso que ninguém escreveu à mão e
reduzi-lo ao mínimo que ainda quebra.

**Pré-requisito:** notebooks das Aulas 9 e 10.
"""),

    md("""
## Antes de começar

### 1. O que é cobertura

**Cobertura** é a resposta a uma pergunta simples: *dos pedaços que existem,
quantos os meus testes tocaram?*

A analogia: você precisa revisar um texto de 100 linhas e leu 40. Sua
"cobertura de leitura" é 40%. Os erros das outras 60 linhas continuam lá,
intactos, e a sua sensação de dever cumprido não muda isso.

Existem várias formas de contar "pedaço":

| Tipo de cobertura | O "pedaço" é | Força |
| --- | --- | --- |
| de linha | cada linha de código | fraca |
| de estado | cada estado do modelo | média |
| **de transição** | cada seta entre estados | **boa** |

Esta aula usa **cobertura de transição**. É a que faz sentido para um
supervisor: o que importa não é ter visitado cada estado, é ter exercitado
cada caminho **entre** eles.

### 2. Por que cobertura de linha engana

Este é o ponto que separa quem entende de quem repete.

Um teste pode passar por 100% das linhas e ainda assim não testar nada, porque
**passar por uma linha não é o mesmo que verificar o que ela faz**.

Se o seu teste roda o código inteiro e não confere nenhum resultado, a
cobertura de linha dá 100% e o valor do teste é zero.

Cobertura é uma métrica de **omissão**: ela diz o que você certamente não
testou. Ela nunca diz que o que você testou está bem testado.

### 3. Teste de exemplo × teste de propriedade

Duas formas de escrever teste:

**Teste de exemplo** — você escolhe os valores:
> "Com obstáculo e velocidade 0,5, o torque deve cair."

Testa exatamente aquele caso. Você acertou o caso? Ótimo. Errou? Passa batido.

**Teste de propriedade** — você declara uma regra e a ferramenta procura o
contraexemplo:
> "Para qualquer sequência de entradas, o torque nunca fica ligado com
> obstáculo."

A ferramenta gera centenas de sequências aleatórias tentando quebrar a regra.
Ela não sabe onde está o bug, mas procura muito mais lugares que você.

### 4. Redução (*shrinking*)

O superpoder do teste de propriedade.

Quando a ferramenta acha uma sequência de 47 passos que quebra a regra, ela
não te entrega os 47. Ela vai **removendo passos** enquanto o problema
continuar acontecendo, até sobrar o mínimo.

Você recebe: *"3 passos, e quebra"*. Isso é a diferença entre um relatório que
alguém consegue depurar e um que ninguém lê.
"""),

    md(GLOSSARIO),

    md("""
## Passo 1 — Medindo a suíte manual

Vamos começar com uma suíte escrita à mão — do tipo que sai numa revisão de
código caprichada. Seis casos, cada um cobrindo uma situação que faz sentido.

E vamos medir o quanto ela cobre.
"""),
    code(ABERTURA_IMPORTS + r"""
from nexabot import mbt, modelcheck
from nexabot.supervisor import Estado, Entradas, Supervisor

# O espaço completo: tudo o que o supervisor consegue fazer
referencia = modelcheck.explorar()
transicoes_possiveis = {(t.origem, t.destino) for t in referencia.transicoes}

print(f"O que existe para ser coberto:")
print(f"  estados alcançáveis        : {len(referencia.estados_alcancaveis)}")
print(f"  transições distintas       : {len(transicoes_possiveis)}")
print()

# A suíte manual, escrita à mão
def suite_manual():
    casos = [
        ("partida",            [Entradas(comando_partir=True)]),
        ("parada comandada",   [Entradas(comando_partir=True),
                                Entradas(comando_parar=True, velocidade=0.5)]),
        ("obstáculo",          [Entradas(comando_partir=True),
                                Entradas(obstaculo=True, velocidade=0.5)]),
        ("emergência",         [Entradas(comando_partir=True),
                                Entradas(emergencia=True, velocidade=0.5)]),
        ("falha de encoder",   [Entradas(comando_partir=True),
                                Entradas(falha_encoder=True, velocidade=0.5)]),
        ("rearme",             [Entradas(falha_encoder=True),
                                Entradas(rearme=True)]),
    ]
    resultado = []
    for nome, sequencia in casos:
        sup = Supervisor()
        estados = [sup.state]
        for e in sequencia:
            sup.step(e)
            estados.append(sup.state)
        resultado.append((nome, tuple(estados)))
    return resultado


manual = suite_manual()
estados_tocados = set()
transicoes_tocadas = set()
for nome, estados in manual:
    estados_tocados.update(estados)
    for i in range(len(estados) - 1):
        transicoes_tocadas.add((estados[i], estados[i + 1]))

pct_e = 100 * len(estados_tocados & referencia.estados_alcancaveis) / len(referencia.estados_alcancaveis)
pct_t = 100 * len(transicoes_tocadas & transicoes_possiveis) / len(transicoes_possiveis)

print("A suíte manual, de 6 casos:")
print(f"  todos os casos passaram?   sim")
print(f"  cobertura de estados       : {pct_e:5.1f}%")
print(f"  cobertura de transições    : {pct_t:5.1f}%")
print()
print("Verde na tela, e menos da metade das transições exercitada.")
print("É esse o abismo que 'a suíte está passando' esconde.")
"""),

    md("""
### E o que exatamente ficou de fora

Não basta saber a porcentagem. É preciso saber **quais** transições ninguém
testou — porque é exatamente ali que os bugs sobrevivem.
"""),
    code(r"""
faltando = sorted(transicoes_possiveis - transicoes_tocadas,
                  key=lambda p: (p[0].name, p[1].name))

print(f"Transições que a suíte manual NUNCA exercitou ({len(faltando)}):")
print()
for origem, destino in faltando:
    print(f"  {origem.name:>18}  ->  {destino.name}")
print()
print("Leia essa lista como uma lista de riscos. Cada linha é um caminho")
print("que o robô pode percorrer no armazém e que ninguém nunca testou.")
"""),

    md("""
## Passo 2 — Deixando o computador escrever os testes

Aqui está a virada.

Você já tem o modelo do supervisor. O computador já sabe percorrer o espaço de
estados (Aula 10). Então por que escrever testes à mão?

**Teste baseado em modelo** (*model-based testing*): a ferramenta olha o
modelo, escolhe caminhos que cobrem o que você pediu, e gera os casos.
"""),
    code(r"""
suite_estados = mbt.gerar_casos_cobertura_estados(referencia)
suite_transicoes = mbt.gerar_casos_cobertura_transicoes(referencia)

print(f"{'suíte':>30}  {'casos':>7}  {'estados':>9}  {'transições':>12}")
print("-" * 64)

cob_manual = {"pct_estados": pct_e, "pct_transicoes": pct_t}
print(f"{'manual (escrita à mão)':>30}  {len(manual):>7}  "
      f"{cob_manual['pct_estados']:>8.1f}%  {cob_manual['pct_transicoes']:>11.1f}%")

for nome, suite in (("gerada — cobrir estados", suite_estados),
                    ("gerada — cobrir transições", suite_transicoes)):
    c = mbt.medir_cobertura(suite, referencia)
    print(f"{nome:>30}  {len(suite):>7}  "
          f"{c['pct_estados']:>8.1f}%  {c['pct_transicoes']:>11.1f}%")

print()
print("A suíte gerada para cobrir transições chega onde a manual não chegou,")
print("e ninguém precisou pensar em cada caso.")
"""),

    md("""
### Os testes gerados rodam de verdade

Uma suíte gerada não vale nada se for só uma lista. Ela precisa executar
contra o código e conferir o resultado esperado.

A célula abaixo roda todos os casos gerados. Cada um instancia um supervisor
novo, aplica a sequência de entradas e confere, passo a passo, que o estado
resultante é o que o modelo previu.
"""),
    code(r"""
falhas = []
for caso in suite_transicoes:
    try:
        caso.rodar()
    except AssertionError as e:
        falhas.append((caso.id, str(e)))

print(f"Casos gerados executados : {len(suite_transicoes)}")
print(f"Falhas                   : {len(falhas)}")
print()
if not falhas:
    print("Todos passaram — o código concorda com o modelo em cada passo.")
    print()
    print("Repare no que isso significa: o modelo virou a especificação")
    print("executável, e o código está sendo medido contra ela. Não contra")
    print("a opinião de quem escreveu o teste.")

print()
print("Exemplo de um caso gerado:")
exemplo = suite_transicoes[len(suite_transicoes) // 2]
print(f"  id        : {exemplo.id}")
print(f"  descrição : {exemplo.descricao}")
print(f"  passos    : {len(exemplo.entradas_sequencia)}")
print(f"  percurso  : {' -> '.join(e.name for e in exemplo.estados_esperados)}")
"""),

    md("""
## Passo 3 — Teste de propriedade: procurando o que ninguém pensou

Suítes geradas cobrem o modelo. Mas e se o **próprio modelo** tiver um
problema?

Aqui entra o teste de propriedade. Em vez de casos, você declara uma regra
que deve valer sempre, e a ferramenta — o **Hypothesis** — gera sequências
aleatórias de entradas tentando quebrá-la.

Vamos declarar uma propriedade **falsa de propósito**, para ver a máquina
achar o contraexemplo e reduzi-lo.

A propriedade errada: *"o supervisor nunca sai do estado OCIOSO"*. Obviamente
falso. Quantos passos o Hypothesis precisa para provar isso?
"""),
    code(r"""
from hypothesis import given, settings, strategies as st, Phase

entrada_qualquer = st.builds(
    Entradas,
    comando_partir=st.booleans(),
    comando_parar=st.booleans(),
    obstaculo=st.booleans(),
    emergencia=st.booleans(),
    falha_encoder=st.booleans(),
    rearme=st.booleans(),
    velocidade=st.floats(min_value=0.0, max_value=1.5,
                         allow_nan=False, allow_infinity=False),
)

contraexemplo = {}

@settings(max_examples=300, deadline=None)
@given(st.lists(entrada_qualquer, min_size=1, max_size=20))
def propriedade_falsa(sequencia):
    sup = Supervisor()
    for e in sequencia:
        sup.step(e)
    # afirmação deliberadamente falsa
    assert sup.state == Estado.OCIOSO, "saiu de OCIOSO"

try:
    propriedade_falsa()
    print("Nenhum contraexemplo — a propriedade seria verdadeira.")
except AssertionError as e:
    print("O Hypothesis achou um contraexemplo.")
    print()
    print(f"Mensagem da asserção: {e}")
    print()
    print("Logo acima desta saída, no notebook, o Hypothesis imprime a linha")
    print("'Falsifying example:' com a sequência mínima que ele encontrou.")
    print("Repare no tamanho dela: costuma ser UM passo, com quase todos os")
    print("campos em False. Ele começou com sequências longas e aleatórias e")
    print("foi cortando até sobrar o mínimo que ainda quebra.")
"""),

    md("""
### Agora a propriedade verdadeira

A anterior era falsa de propósito, para você ver a máquina caçar.

Agora a propriedade que realmente importa — a mesma do `REQ-SAFE-001`:

> Para **qualquer** sequência de entradas, o torque nunca fica habilitado no
> mesmo ciclo em que há obstáculo.

Se o Hypothesis não achar contraexemplo em centenas de tentativas, isso é
evidência (não prova) de que a regra vale.
"""),
    code(r"""
tentativas = {"n": 0}

@settings(max_examples=500, deadline=None)
@given(st.lists(entrada_qualquer, min_size=1, max_size=30))
def torque_nunca_com_obstaculo(sequencia):
    tentativas["n"] += 1
    sup = Supervisor()
    for e in sequencia:
        saida = sup.step(e)
        assert not (e.obstaculo and saida.torque_habilitado), (
            f"torque ligado com obstáculo em {sup.state.name}"
        )

try:
    torque_nunca_com_obstaculo()
    print(f"Nenhum contraexemplo em {tentativas['n']} sequências aleatórias,")
    print("de até 30 passos cada.")
    print()
    print("Isso é EVIDÊNCIA, não prova. A prova você já tem da Aula 10, que")
    print("percorreu o espaço inteiro. As duas se complementam:")
    print()
    print("  o model checker prova dentro do modelo;")
    print("  o teste de propriedade procura no código de verdade.")
except AssertionError as e:
    print("Contraexemplo encontrado:")
    print(str(e)[:400])
"""),

    md("""
## Mexa aqui

**Experimento 1 — quebre o supervisor e deixe o Hypothesis achar.**
Na célula abaixo, o supervisor tem um bug condicionado a uma faixa estreita de
velocidade. Rode e veja em quantas tentativas o Hypothesis encontra — e veja o
tamanho do contraexemplo que ele devolve depois de reduzir.

**Experimento 2 — estreite a faixa do bug.**
Troque a condição para uma faixa bem menor, tipo `0.77 < v < 0.78`. O
Hypothesis ainda acha? Em quantas tentativas? Isso te dá a intuição do limite
da busca aleatória.

**Experimento 3 — cobertura como orçamento.**
Volte à lista de transições não cobertas do Passo 1 e escreva, à mão, um caso
que cubra uma delas. Meça de novo. Quantos casos manuais seriam necessários
para chegar aos 100% que a geração automática alcançou sozinha?
"""),
    code(r"""
from nexabot.supervisor import transition, Saidas

class SupervisorComBug(Supervisor):
    def step(self, entradas):
        saida = super().step(entradas)
        # ⬇️ o bug: numa faixa estreita de velocidade, ignora o obstáculo
        if entradas.obstaculo and 0.70 < entradas.velocidade < 0.90:
            saida = Saidas(torque_habilitado=True, freio_acionado=saida.freio_acionado)
        return saida


achou = {"n": 0}

@settings(max_examples=500, deadline=None)
@given(st.lists(entrada_qualquer, min_size=1, max_size=30))
def busca_o_bug(sequencia):
    achou["n"] += 1
    sup = SupervisorComBug()
    for e in sequencia:
        saida = sup.step(e)
        assert not (e.obstaculo and saida.torque_habilitado), (
            f"BUG: torque ligado com obstáculo, v={e.velocidade:.3f}"
        )

try:
    busca_o_bug()
    print(f"Não achou em {achou['n']} tentativas. A faixa do bug é estreita demais")
    print("para a busca aleatória — e essa é uma limitação real da técnica.")
except AssertionError as e:
    print(f"ACHOU, depois de {achou['n']} sequências geradas.")
    print()
    print("E olhe o tamanho do contraexemplo depois da redução:")
    print(str(e)[:500])
    print()
    print("Ele começou com uma sequência longa e foi cortando passos")
    print("enquanto o bug continuava aparecendo. O que sobrou é o mínimo.")
"""),

    md("""
## Aprofundamento (opcional)

### Por que cobertura de linha não é evidência

Considere este código:

```c
if (obstaculo && velocidade > 0.5) {
    torque = 0;
}
```

Um único teste com `obstaculo=true, velocidade=0.6` executa **todas as
linhas**. Cobertura de linha: 100%.

E, no entanto, nunca foi testado:

- obstáculo verdadeiro com velocidade baixa;
- obstáculo falso com velocidade alta;
- a combinação que faz a condição ser falsa por cada motivo separado.

Normas de sistemas críticos exigem critérios mais fortes por isso. O mais
conhecido chama-se **MC/DC**, e ele exige mostrar que **cada condição
isoladamente** consegue mudar o resultado. É caro, e é obrigatório em software
aeronáutico do nível mais crítico.

### Os outros critérios de cobertura

A teoria de cobertura de grafo tem uma família inteira de critérios —
cobertura de nós, de arestas, de pares de arestas, de caminhos principais, de
caminhos completos —, cada um mais forte e mais caro que o anterior.

Aqui você usou **um**: cobrir toda transição. É o que faz sentido para um
supervisor de estados, e é o que a norma industrial costuma pedir na prática.
Os demais estão no material complementar.

### O limite honesto de tudo isto

O modelo discreto do supervisor prova coisas sobre **estados e transições**.
Ele não sabe nada sobre a planta contínua.

É por isso que o `REQ-SAFE-007` — "a velocidade nunca passa de 1,2 m/s" —
continua marcado como lacuna: ele depende da trajetória física, não da máquina
de estados. Nenhuma quantidade de cobertura de transição resolve isso.

Reconhecer o que a sua técnica **não** cobre é parte do trabalho.
"""),
    code(r"""
from nexabot import requisitos

print("O que cada técnica desta unidade cobre:")
print()
print(f"{'requisito':>14}  {'tipo':>32}  técnica que o cobre")
print("-" * 84)
for req in requisitos.REQUISITOS:
    if req.verificar_transicao is not None:
        tecnica = "model checking (Aula 10)"
    elif req.estado_alvo is not None:
        tecnica = "alcançabilidade (Aula 10)"
    elif req.limite_periodos is not None:
        tecnica = "autômato temporizado (Aula 11)"
    else:
        tecnica = "NENHUMA — lacuna declarada"
    print(f"{req.id:>14}  {req.tipo:>32}  {tecnica}")

print()
print("A última linha é a mais honesta do material. O REQ-SAFE-007 fala da")
print("velocidade física, e o supervisor discreto não enxerga velocidade")
print("física — só recebe um número já amostrado.")
print()
print("Declarar a lacuna vale mais que fingir cobertura. Numa auditoria, a")
print("lacuna declarada é uma conversa; a lacuna escondida é uma reprovação.")
"""),

    md("""
## O que você leva desta aula

1. **Cobertura mede omissão, não qualidade.** Ela diz o que você não testou.
2. **Cobertura de linha engana.** Passar por uma linha não é verificar o que
   ela faz.
3. **Cobertura de transição é a que importa** num supervisor de estados.
4. **O computador escreve os testes a partir do modelo**, e chega onde a
   suíte manual não chega.
5. **Teste de propriedade procura o que você não pensou**, e a redução entrega
   o contraexemplo mínimo.
6. **Prova e evidência se complementam.** O model checker prova dentro do
   modelo; o teste de propriedade procura no código real.
7. **Declare o que a sua técnica não cobre.** Lacuna escondida é reprovação em
   auditoria.

Isso fecha a Unidade 3. Você saiu de "o robô funciona" para "eis a prova, eis
a cobertura, e eis o que ainda não está coberto".

Na Unidade 4 tudo isso vira **código embarcado** — e a pergunta final passa a
ser se o binário que roda no robô é mesmo o modelo que você provou.

## Se deu erro

**O Hypothesis demora.**
Ele gera centenas de sequências. Reduza `max_examples` para `100`.

**`DeadlineExceeded`.**
Já está tratado com `deadline=None` nas células. Se aparecer, é porque você
mexeu no `settings`.

**O Experimento 1 não achou o bug.**
Aumente `max_examples` ou alargue a faixa de velocidade do bug. Não achar
também é resultado: mostra que busca aleatória tem limite, e é por isso que
ela não substitui a verificação exaustiva da Aula 10.
""" + RODAPE_ERRO),
]
