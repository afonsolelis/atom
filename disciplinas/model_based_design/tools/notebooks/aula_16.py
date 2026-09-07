"""Notebook da Aula 16 — evidência não é certificado."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import ABERTURA_IMPORTS, GLOSSARIO, RODAPE_ERRO, md, code  # noqa: E402

TITULO = "Aula 16 — Evidência não é certificado"
SLUG = "rastreabilidade_e_fechamento"

CELULAS = [
    md("""
# Aula 16 — Evidência não é certificado

## O que você vai fazer aqui

Você chegou ao fim. Tem modelo, controlador, provas formais, código gerado,
comparação numérica e medição de tempo real.

Alguém vai olhar tudo isso e perguntar: **"isso está certificado?"**

Hoje você aprende a responder essa pergunta com honestidade — e a montar o
documento que sustenta a resposta: a **matriz de rastreabilidade**, que liga
cada requisito ao código e ao teste que o cobre.

**Pré-requisito:** ter passado pelas quinze aulas anteriores.
"""),

    md("""
## Antes de começar

### 1. O que é uma norma

Uma **norma** é um acordo escrito sobre como fazer uma coisa, publicado por
uma organização que a indústria reconhece.

Ela não diz "seu software está correto". Ela diz **quais evidências você
precisa produzir** para que alguém possa julgar se está.

As duas que importam aqui:

| Norma | Setor | O que é |
| --- | --- | --- |
| **DO-178C** | aeronáutico | software embarcado em aeronaves |
| **ISO 26262** | automotivo | segurança funcional em veículos |

### 2. Nível de criticidade

Nem todo software precisa do mesmo rigor. Faria sentido exigir de um
brinquedo o mesmo que de um freio?

As normas resolvem isso com **níveis**. Quanto pior a consequência de uma
falha, mais alto o nível, e mais evidência é exigida.

| Se falhar... | DO-178C | ISO 26262 |
| --- | --- | --- |
| catastrófico, com mortes | Nível A | ASIL D |
| perigoso, com feridos graves | Nível B | ASIL C |
| grave, mas controlável | Nível C | ASIL B |
| incômodo | Nível D | ASIL A |
| sem efeito na segurança | Nível E | QM |

A diferença entre os níveis não é filosófica: é **quantidade de trabalho**. O
nível mais alto pode exigir dezenas de objetivos a mais, cada um com sua
evidência documentada.

### 3. Rastreabilidade

**Rastreabilidade** é conseguir responder, para qualquer artefato do projeto:

- de onde ele veio;
- o que ele implementa;
- o que prova que ele está correto.

Na prática, é conseguir seguir uma linha do requisito até o binário, e voltar.

Por que isso importa? Porque quando um requisito muda, você precisa saber
**tudo** o que precisa ser refeito. Sem rastreabilidade, a resposta é "sei lá,
melhor testar tudo de novo" — e ninguém testa tudo de novo.

### 4. A distinção que dá nome à aula

> **Evidência** é um artefato que você produz e alguém pode conferir.
>
> **Certificado** é o julgamento de uma autoridade sobre essa evidência.

Você produz evidência. **Quem certifica é outra pessoa**, com mandato para
isso.

Um pipeline aberto e bem feito produz evidência de primeira. Ele não certifica
nada, e nenhuma ferramenta certifica — nem a mais cara.
"""),

    md(GLOSSARIO),

    md("""
## Passo 1 — A matriz de rastreabilidade

A célula abaixo varre o projeto inteiro procurando marcadores de requisito
(`REQ-XXXX-NNN`) e monta a matriz.

Repare que ela não é escrita à mão. Ela é **derivada do código**, e por isso
não fica desatualizada quando alguém mexe em alguma coisa.
"""),
    code(ABERTURA_IMPORTS + r"""
from nexabot import rastreabilidade

resultado = rastreabilidade.construir_matriz()

print(f"Arquivos varridos : {resultado.n_arquivos_lidos}")
print(f"Arquivos com erro : {resultado.n_arquivos_com_erro}")
print(f"Requisitos achados: {len(resultado.entradas)}")
print()
if resultado.avisos:
    print("Avisos da varredura:")
    for aviso in resultado.avisos[:5]:
        print(f"  - {aviso}")
    print()

CATEGORIAS = ("Modelo", "Código gerado", "Teste")

print(f"{'requisito':>16}  {'modelo':>7}  {'gerado':>7}  {'teste':>6}  descrição")
print("-" * 92)
for entrada in resultado.entradas:
    desc = (entrada.descricao or "")[:44]
    n = [len(entrada.arquivos_por_categoria(c)) for c in CATEGORIAS]
    print(f"{entrada.requisito:>16}  {n[0]:>7}  {n[1]:>7}  {n[2]:>6}  {desc}")
"""),

    md("""
## Passo 2 — Percorrendo uma linha inteira

Uma tabela com números é resumo. O que convence é seguir **uma linha do começo
ao fim**.

Vamos pegar o `REQ-SAFE-001` — "nunca há torque com obstáculo" — e percorrer
todo o caminho: onde ele está escrito, onde está implementado, e o que prova
que está certo.
"""),
    code(r"""
alvo = "REQ-SAFE-001"
entrada = next(e for e in resultado.entradas if e.requisito == alvo)

print(f"{alvo}")
print(f"  {entrada.descricao}")
print()
for rotulo, categoria in (("ESPECIFICAÇÃO / MODELO", "Modelo"),
                          ("IMPLEMENTAÇÃO (código gerado)", "Código gerado"),
                          ("EVIDÊNCIA (testes e verificação)", "Teste")):
    arquivos = entrada.arquivos_por_categoria(categoria)
    print(f"  {rotulo}")
    if arquivos:
        for a in sorted(arquivos):
            print(f"      {a}")
    else:
        print("      (nenhum)")
    print()
"""),

    md("""
### O que essa linha responde

Com ela na mão, você responde sem hesitar:

- **"Onde está escrito esse requisito?"** — em `requisitos.py`, como predicado
  executável (Aula 9).
- **"Quem implementa?"** — o `supervisor.py`, e o `timed.py` para a parte de
  prazo.
- **"O que prova que está certo?"** — quatro arquivos: a verificação
  exaustiva (Aula 10), o contraexemplo, e o teste de propriedade (Aula 12).
- **"Se eu mudar esse requisito, o que preciso refazer?"** — exatamente os
  arquivos dessa linha, e nada além.

Repare que a coluna de **código gerado** está vazia para este requisito, e isso
está certo: o `REQ-SAFE-001` vive no supervisor de segurança, que nesta
disciplina não passa pelo gerador de código — só o PID passa. A matriz não
inventa preenchimento.

Aquela pergunta sobre o que refazer é a que economiza dinheiro de verdade num
projeto longo.
"""),

    md("""
## Passo 3 — O que este pipeline produz, e o que não produz

Aqui está a parte mais importante do curso, e a mais fácil de errar.

A célula abaixo lista, lado a lado, as evidências que você de fato produziu e
as coisas que **não** foram feitas.
"""),
    code(r"""
produz = [
    ("Modelo executável da planta",
     "identificado de ensaio, com erro medido (Aula 2)"),
    ("Requisitos formais",
     "predicados executáveis, sem ambiguidade (Aula 9)"),
    ("Verificação exaustiva",
     "todo o espaço de estados percorrido (Aula 10)"),
    ("Prova de prazo",
     "pior caso enumerado, não estimado (Aula 11)"),
    ("Cobertura medida",
     "de transição, com a lista do que falta (Aula 12)"),
    ("Código gerado com assinatura",
     "hash que muda se um ganho mudar (Aula 13)"),
    ("Equivalência modelo-código",
     "erro medido amostra a amostra (Aula 14)"),
    ("Temporização real medida",
     "jitter e latência do laço fechado (Aula 15)"),
    ("Matriz de rastreabilidade",
     "derivada do código, não escrita à mão (esta aula)"),
]

nao_produz = [
    ("Qualificação de ferramenta",
     "as ferramentas usadas não foram qualificadas segundo o DO-330"),
    ("Cobertura MC/DC do código",
     "só cobertura de transição do modelo, que é outra coisa"),
    ("Análise de código-fonte segundo norma",
     "regras MISRA-C, análise estática certificada"),
    ("Prova sobre a planta contínua",
     "REQ-SAFE-007 segue como lacuna declarada"),
    ("Revisão independente",
     "nenhum revisor externo ao time olhou nada disto"),
    ("Certificado",
     "nenhum. Certificação é ato de autoridade, não de ferramenta"),
]

print("O QUE ESTE PIPELINE PRODUZ")
print("=" * 76)
for item, detalhe in produz:
    print(f"  ✓ {item}")
    print(f"      {detalhe}")

print()
print("O QUE ELE NÃO PRODUZ")
print("=" * 76)
for item, detalhe in nao_produz:
    print(f"  ✗ {item}")
    print(f"      {detalhe}")

print()
print("Saber recitar a segunda lista vale mais, numa entrevista, do que")
print("saber recitar a primeira. Ela mostra que você entende o limite do")
print("que fez — e é isso que separa engenheiro de operador de ferramenta.")
"""),

    md("""
## Passo 4 — A pergunta sobre ferramenta aberta

Uma objeção que você vai ouvir:

> *"Mas você usou ferramentas abertas e gratuitas. Isso não desqualifica tudo?"*

A resposta honesta é **não**, e a razão é técnica.

Nenhuma ferramenta — aberta ou paga — é confiável por decreto. O que as normas
exigem é **qualificação**: demonstrar que a ferramenta faz o que promete, no
uso específico que você dá a ela.

E a exigência de qualificação depende de três perguntas, nenhuma delas sobre
licença ou preço:

1. **A ferramenta pode introduzir um erro** no produto final?
2. **A ferramenta permite que você deixe de fazer** alguma verificação que
   faria de outro jeito?
3. **Um erro dela seria detectado** por outra atividade do processo?

Um gerador de código responde "sim" à primeira: ele pode gerar C errado. Por
isso ele precisaria ser qualificado — **seja ele aberto ou custe cem mil
dólares**.

A célula abaixo aplica essas três perguntas às ferramentas desta disciplina.
"""),
    code(r"""
ferramentas = [
    # (nome, pode introduzir erro?, permite pular verificação?, erro seria detectado?)
    ("gerador de código (codegen)", True,  False, True),
    ("model checker (modelcheck)",  False, True,  False),
    ("gerador de testes (mbt)",     False, True,  False),
    ("compilador gcc",              True,  False, True),
    ("matplotlib (gráficos)",       False, False, True),
]

print(f"{'ferramenta':>28}  {'introduz':>9}  {'deixa pular':>12}  "
      f"{'detectável':>11}  precisa qualificar?")
print("-" * 92)
for nome, introduz, pula, detectavel in ferramentas:
    # Se não pode introduzir erro nem deixa pular verificação, não precisa.
    # Se pode introduzir mas o erro é detectado depois, a exigência é menor.
    if not introduz and not pula:
        veredito = "não"
    elif introduz and detectavel:
        veredito = "sim, com rigor menor"
    else:
        veredito = "SIM, com rigor alto"
    print(f"{nome:>28}  {str(introduz):>9}  {str(pula):>12}  "
          f"{str(detectavel):>11}  {veredito}")

print()
print("Repare no model checker: ele não introduz erro no produto, mas se")
print("ele mentir dizendo 'passou', você deixa de procurar o bug por outro")
print("caminho. É por isso que a coluna do meio importa tanto quanto a")
print("primeira — e por que essa é a linha mais exigente da tabela.")
print()
print("Nenhuma coluna pergunta o preço da licença.")
"""),

    md("""
## Passo 5 — O que você construiu em dezesseis aulas

Vale olhar para trás.
"""),
    code(r"""
import numpy as np
from nexabot.params import PARAMS
from nexabot.plant import simulate, transfer_function
from nexabot.controllers import DiscretePID

# a Aula 1: malha aberta, carga entrando
tensao_fixa = 200.0 / PARAMS.dc_gain
t_ma, X_ma = simulate(u_of_t=tensao_fixa, t_end=2.0,
                      tau_load_of_t=lambda tt: 0.15 if tt >= 1.0 else 0.0)

# a Aula 16: malha fechada, mesmo distúrbio
pid = DiscretePID(Kp=0.30, Ki=8.0, Kd=0.004, Ts=PARAMS.Ts,
                  u_max=PARAMS.V_max, Kaw=100.0)
n = int(2.0 / PARAMS.Ts)
x = np.zeros(2); w_mf = np.zeros(n)
for k in range(n):
    tempo = k * PARAMS.Ts
    w_mf[k] = x[1]
    u = pid.step(200.0, x[1])
    tau = 0.15 if tempo >= 1.0 else 0.0
    _, Xk = simulate(u_of_t=u, t_end=PARAMS.Ts, dt=PARAMS.Ts/40, x0=x, tau_load_of_t=tau)
    x = Xk[-1]

print("O mesmo robô, o mesmo distúrbio, dezesseis aulas depois")
print("=" * 62)
print(f"{'':>28}  {'ω final':>10}  {'erro':>10}")
print("-" * 52)
print(f"{'Aula 1 — malha aberta':>28}  {X_ma[-1,1]:>10.2f}  {200 - X_ma[-1,1]:>10.2f}")
print(f"{'Aula 16 — malha fechada':>28}  {w_mf[-1]:>10.2f}  {200 - w_mf[-1]:>10.2f}")
print()
print("E não é só o número que mudou. Do controlador de hoje você sabe:")
print()
print("  de onde vieram os parâmetros    (identificados, Aula 2)")
print("  por que os polos são esses      (Laplace, Aula 3)")
print("  onde o driver barra o projeto   (saturação, Aula 4)")
print("  por que Ts = 5 ms               (amostragem, Aula 7)")
print("  que os requisitos valem sempre  (prova exaustiva, Aula 10)")
print("  que o prazo cabe no pior caso   (150 ms, Aula 11)")
print("  o que a suíte NÃO cobre         (cobertura, Aula 12)")
print("  que o C é o modelo              (equivalência medida, Aula 14)")
print("  quanto o tempo real varia       (jitter, Aula 15)")
"""),

    md("""
### O gráfico do fechamento

A primeira e a última curva do curso, no mesmo eixo.
"""),
    code(r"""
import matplotlib.pyplot as plt

t_mf = np.arange(n) * PARAMS.Ts

fig, ax = plt.subplots(figsize=(9.5, 5.5))
ax.axhline(200, color="#888888", linestyle="--", linewidth=1.2, label="alvo")
ax.plot(t_ma, X_ma[:, 1], color="#C0392B", linewidth=2,
        label="Aula 1 — malha aberta")
ax.plot(t_mf, w_mf, color="#4A9D5F", linewidth=2.5,
        label="Aula 16 — modelado, controlado, verificado, embarcado")
ax.axvline(1.0, color="#555555", linestyle=":", linewidth=1.2)
ax.text(1.03, 40, "a carga entra", fontsize=10, color="#555555")

ax.set_xlabel("tempo [s]")
ax.set_ylabel("velocidade ω [rad/s]")
ax.set_title("Dezesseis aulas, o mesmo robô, o mesmo distúrbio",
             fontsize=13, pad=12)
ax.set_ylim(0, 260)
ax.legend(loc="lower left"); ax.grid(alpha=0.25)
plt.tight_layout()
plt.show()
"""),

    md("""
## Mexa aqui

**Experimento 1 — quebre a rastreabilidade.**
Apague um marcador `REQ-SAFE-` de algum arquivo do projeto e rode a matriz de
novo. A linha correspondente perde uma coluna. Agora imagine isso acontecendo
sem ninguém notar, num projeto de dois anos.

**Experimento 2 — a lacuna.**
Procure o `REQ-SAFE-007` na matriz. Ele tem evidência? Qual seria o caminho
para cobri-lo? (Dica: exige raciocínio sobre a trajetória contínua, não sobre
a máquina de estados — é uma técnica que esta disciplina não cobriu.)

**Experimento 3 — a resposta pronta.**
Escreva, em três frases, a resposta que você daria à pergunta *"isso está
certificado?"*. Guarde. É provável que você use isso numa entrevista.
"""),
    code(r"""
# ⬇️ mexa aqui: qual requisito você quer inspecionar?
REQUISITO = "REQ-SAFE-007"

achado = next((e for e in resultado.entradas if e.requisito == REQUISITO), None)

if achado is None:
    print(f"{REQUISITO} não aparece na matriz.")
    print("Ou ele não existe, ou ninguém o marcou em lugar nenhum do código —")
    print("e as duas hipóteses são problema.")
else:
    print(f"{REQUISITO}")
    print(f"  {achado.descricao}")
    print()
    testes = achado.arquivos_por_categoria("Teste")
    print(f"  arquivos de modelo : {len(achado.arquivos_por_categoria('Modelo'))}")
    print(f"  arquivos gerados   : {len(achado.arquivos_por_categoria('Código gerado'))}")
    print(f"  arquivos de teste  : {len(testes)}")
    print()
    if not testes:
        print("  ⚠ SEM EVIDÊNCIA. Este requisito está declarado e implementado,")
        print("    mas nada prova que ele é cumprido.")
        print()
        print("    Numa auditoria, essa linha vira uma pergunta. E a resposta")
        print("    certa não é inventar um teste fraco para preencher a coluna:")
        print("    é dizer qual técnica faltaria e por que ela não foi feita.")
"""),

    md("""
## Aprofundamento (opcional)

### O texto normativo

O **DO-330** é o suplemento do DO-178C que trata especificamente de
qualificação de ferramenta. Ele define cinco níveis (TQL-1 a TQL-5) e os
objetivos exigidos em cada um.

O critério das três perguntas que você aplicou no Passo 4 é a essência dele.
O texto completo é leitura de quem vai trabalhar em certificação, e está no
material complementar.

### Onde isso é usado de verdade

| Setor | Como aparece |
| --- | --- |
| **Automotivo** | Toda unidade de controle de freio, direção e propulsão passa por ISO 26262. Modelagem, geração de código e rastreabilidade são práticas correntes, não exceção. |
| **Aeroespacial** | DO-178C nível A para controle de voo. A evidência custa mais que o código. |
| **Robótica industrial** | ISO 10218 e ISO/TS 15066 para robôs colaborativos. Prazo de parada é requisito duro, exatamente como o da Aula 11. |
| **Dispositivos médicos** | IEC 62304, com a mesma lógica de níveis de criticidade. |

Em todos, a pergunta profissional é a mesma: *"mostre a evidência"*.

### A resposta à pergunta do título

Quando alguém perguntar "isso está certificado?", a resposta honesta é:

> Não. Isto **produz evidência** — modelo identificado com erro medido,
> requisitos formais verificados exaustivamente, prazo provado no pior caso,
> código gerado com assinatura, equivalência modelo-código medida, e
> rastreabilidade derivada do próprio código.
>
> Certificação é ato de uma autoridade, sobre um processo completo, com
> revisão independente e qualificação de ferramenta — nada disso foi feito
> aqui.
>
> O que existe é a base sobre a qual esse processo seria construído.

Essa resposta é melhor que um "sim" — porque um "sim" seria falso, e quem
pergunta sabe.
"""),
    code(r"""
_, caminho_md = rastreabilidade.gerar_e_salvar()
print(f"Matriz de rastreabilidade salva em: {caminho_md}")
print()
texto = Path(caminho_md).read_text(encoding="utf-8")
print("As primeiras linhas do documento gerado:")
print()
print("\n".join(texto.splitlines()[:20]))
print("...")
print()
print(f"O documento inteiro tem {len(texto.splitlines())} linhas.")
print()
print("Este arquivo é o entregável final da disciplina. Ele não é escrito")
print("por ninguém: é derivado do código, toda vez que roda. Por isso ele")
print("não fica desatualizado — e por isso ele vale como evidência.")
"""),

    md("""
## O que você leva desta aula, e do curso

1. **Norma não diz que seu software está certo.** Ela diz quais evidências
   você precisa produzir.
2. **Nível de criticidade é quantidade de trabalho**, proporcional à
   consequência da falha.
3. **Rastreabilidade responde "o que refazer se isso mudar"** — e é isso que
   economiza dinheiro num projeto longo.
4. **Qualificação de ferramenta não depende de licença.** Depende de a
   ferramenta poder introduzir erro, de ela deixar você pular verificação, e
   de o erro ser detectável depois.
5. **Evidência é o que você produz. Certificado é o que outra pessoa
   julga.** Confundir os dois é o erro mais caro da área.
6. **Declarar a lacuna é mais forte que escondê-la.**

E a coisa maior: você não entregou um robô que funciona. Entregou um robô cuja
correção você consegue **demonstrar**, artefato por artefato, do requisito ao
binário.

É essa diferença que o mercado paga.

Obrigado por chegar até aqui.

## Se deu erro

**A matriz veio vazia.**
A varredura procura marcadores `REQ-XXXX-NNN` nos arquivos `.py` do projeto.
Confira se você está rodando a partir de dentro de `projeto_nexabot/`, ou se o
`PROJECT_ROOT` do módulo aponta para o lugar certo.

**`gerar_e_salvar` falhou por permissão.**
Ele escreve `rastreabilidade.md` na raiz do projeto. Se a pasta for somente
leitura, passe outro caminho como argumento.

**Algum requisito apareceu sem descrição.**
A descrição vem de `requisitos.py` quando o requisito está declarado lá, e de
heurística quando não está. Requisito sem descrição canônica é sinal de que
ele foi citado no código mas nunca formalizado — vale investigar.
""" + RODAPE_ERRO),
]
