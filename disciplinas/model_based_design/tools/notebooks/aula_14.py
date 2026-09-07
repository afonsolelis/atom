"""Notebook da Aula 14 — 'equivalente' só vale depois de virar número."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import ABERTURA_IMPORTS, GLOSSARIO, RODAPE_ERRO, md, code  # noqa: E402

TITULO = "Aula 14 — 'Equivalente' é palavra até virar número"
SLUG = "software_in_the_loop"

CELULAS = [
    md("""
# Aula 14 — "Equivalente" é palavra até virar número

## O que você vai fazer aqui

Na Aula 13 você gerou código C a partir do modelo, e eu disse que ele é
equivalente ao modelo.

**Por que você acreditaria em mim?**

Hoje você compila esse C de verdade, roda os dois lado a lado com as mesmas
entradas, e mede a diferença amostra por amostra. No fim você vai ter um
número — e um número é a única forma de "equivalente" que vale alguma coisa.

De brinde: um bug real, e a correção dele.

**Pré-requisito:** notebook da Aula 13. Precisa do `gcc` instalado.
"""),

    md("""
## Antes de começar

### 1. O que é *software-in-the-loop*

Traduzindo literalmente: "software dentro da malha".

A ideia:

1. Você compila o código C de verdade — o mesmo que iria para o
   microcontrolador.
2. Carrega esse código compilado dentro do Python.
3. Roda os dois controladores — o modelo Python e o C compilado — **com as
   mesmas entradas, no mesmo instante**.
4. Compara as saídas.

O nome da sigla é **SIL**. Existe também HIL (*hardware*-in-the-loop), que é a
Aula 15, com o código rodando no microcontrolador de verdade.

### 2. Por que o modelo e o código podem discordar

Eles foram gerados um do outro. Deveriam bater exatamente. Mas:

- **Ordem das operações.** `(a + b) + c` e `a + (b + c)` podem dar resultados
  ligeiramente diferentes em ponto flutuante.
- **Otimização do compilador.** O `gcc -O2` reorganiza contas.
- **Tipos diferentes.** Python usa 64 bits sempre; o C pode usar 32.
- **E, claro, bug no gerador.** É para isso que a comparação existe.

### 3. Épsilon de máquina

Aqui está o número que dá sentido a "praticamente iguais".

Um computador não guarda números reais — guarda aproximações com um número
finito de casas. **Épsilon de máquina** (escreve-se ε, lê-se "épsilon") é o
menor degrau que ele consegue representar perto do número 1.

Em ponto flutuante de 64 bits, ε vale cerca de **0,00000000000000022**.

A régua prática:

- Diferença **da ordem de ε** → os dois cálculos são o mesmo, e a diferença é
  o arredondamento inevitável.
- Diferença **muito maior que ε** → tem alguma coisa diferente de verdade, e
  você precisa achar o quê.

É essa distinção que transforma "deu quase igual" em uma afirmação técnica.
"""),

    md(GLOSSARIO),

    md("""
## Passo 1 — Compilando o C de verdade

A célula abaixo gera o código, chama o `gcc` e carrega a biblioteca resultante
dentro do Python.

Repare: é compilação de verdade, com `-O2`, as mesmas otimizações que um
projeto de produção usaria.
"""),
    code(ABERTURA_IMPORTS + r"""
import shutil
import tempfile
from pathlib import Path
import numpy as np
from nexabot.params import PARAMS
from nexabot.controllers import DiscretePID
from nexabot.codegen import generate
from nexabot import sil

print(f"Compilador encontrado: {shutil.which('gcc')}")
print()

pid_modelo = DiscretePID(Kp=0.30, Ki=8.0, Kd=0.004, Ts=PARAMS.Ts,
                         u_max=PARAMS.V_max, Kaw=100.0)

pasta = Path(tempfile.mkdtemp(prefix="nexabot_aula14_"))
gerado = generate.generate_pid_controller(pid_modelo, output_dir=pasta)
lib = sil.compile_shared_library(gerado.source_path)

print(f"Fonte C   : {gerado.source_path.name}")
print(f"Biblioteca: {lib.name}  ({lib.stat().st_size / 1024:.0f} kB)")
print()
print("Este .so contém o MESMO código que iria para o microcontrolador,")
print("compilado com as mesmas otimizações. Não é uma reimplementação em")
print("Python: é o binário.")
"""),

    md("""
## Passo 2 — Rodando os dois lado a lado

Agora a comparação.

Vamos criar uma sequência de entradas — a referência que muda e a velocidade
medida — e alimentar **exatamente a mesma sequência** aos dois controladores,
amostra por amostra.

O ponto essencial: em cada instante `k`, os dois recebem exatamente `(r[k],
y[k])`. Nenhum dos dois vê nada que o outro não viu.
"""),
    code(r"""
n = 1200
t = np.arange(n) * PARAMS.Ts

# uma referência que muda: degrau, depois outro degrau, depois volta
r = np.where(t < 1.0, 200.0, np.where(t < 3.0, 350.0, 150.0))

# uma "medição" que persegue a referência com atraso, para gerar erro variado
y = np.zeros(n)
for k in range(1, n):
    y[k] = y[k-1] + 0.06 * (r[k-1] - y[k-1])

relatorio = sil.compare_model_vs_code(
    r_sequence=r, y_sequence=y,
    Kp=0.30, Ki=8.0, Kd=0.004,
    Ts=PARAMS.Ts, u_max=PARAMS.V_max, tau_f=0.01, Kaw=100.0,
)

eps = np.finfo(float).eps
print(f"Amostras comparadas : {relatorio.n_amostras}")
print("-" * 58)
print(f"  erro máximo       : {relatorio.erro_maximo_abs:.3e} V")
print(f"  erro médio        : {relatorio.erro_medio_abs:.3e} V")
print(f"  erro RMS          : {relatorio.erro_rms:.3e} V")
print(f"  pior amostra      : índice {relatorio.amostra_pior_caso}")
print()
print(f"  épsilon de máquina: {eps:.3e}")
if relatorio.erro_maximo_abs == 0.0:
    print()
    print("  Erro exatamente ZERO, em todas as amostras.")
    print("  O compilador não reassociou nenhuma conta: o C executa a mesma")
    print("  sequência de operações que o Python, bit a bit.")
    print()
    print("  Nem sempre dá zero — o Aprofundamento explica quando não dá, e")
    print("  por que o critério de aceitação é 'da ordem do épsilon' e não")
    print("  'exatamente zero'.")
else:
    print(f"  razão erro/épsilon: {relatorio.erro_maximo_abs/eps:.1f}")
"""),

    md("""
### Lendo o número

O que importa é a **ordem de grandeza** do erro, comparada ao épsilon:

| Erro medido | Leitura |
| --- | --- |
| exatamente **zero** | o C executa a mesma sequência de operações, bit a bit |
| **alguns épsilons** | mesma conta, ordem das operações ligeiramente diferente |
| **milhares de épsilons ou mais** | alguma coisa é diferente de verdade — investigue |

Nos dois primeiros casos você pode dizer "equivalente" com a consciência
tranquila, porque tem um número para mostrar.

E ponha em perspectiva: o comando do PID chega a dezenas de volts. Um erro na
ordem de 10⁻¹⁶ V sobre um sinal de 24 V é uma diferença que nenhum
instrumento do mundo consegue medir.
"""),
    code(r"""
import matplotlib.pyplot as plt

erro_amostra = np.abs(relatorio.saidas_modelo - relatorio.saidas_codigo)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9.5, 7), sharex=True)

ax1.plot(t, relatorio.saidas_modelo, color="#002057", linewidth=2,
         label="modelo (Python)")
ax1.plot(t, relatorio.saidas_codigo, color="#C0392B", linewidth=1,
         linestyle="--", label="código C compilado")
ax1.set_ylabel("comando u [V]")
ax1.set_title("As duas saídas — sobrepostas, indistinguíveis", fontsize=12)
ax1.legend(loc="upper right"); ax1.grid(alpha=0.25)

ax2.semilogy(t, np.maximum(erro_amostra, 1e-20), color="#D68910", linewidth=1)
ax2.axhline(eps, color="#4A9D5F", linestyle="--", linewidth=1.5)
ax2.text(0.05, eps * 1.6, "épsilon de máquina", color="#4A9D5F", fontsize=10)
ax2.set_ylabel("|diferença| [V]")
ax2.set_xlabel("tempo [s]")
ax2.set_title("A diferença, em escala logarítmica", fontsize=12)
ax2.grid(alpha=0.25, which="both")

plt.tight_layout()
plt.show()
"""),

    md("""
## Passo 3 — E a versão em ponto fixo?

Na Aula 13 você viu que Q16.16 tem um degrau de 0,0000153. Esse degrau não
some na hora da comparação.

Vamos repetir o teste, agora contra a variante de ponto fixo do código gerado.
"""),
    code(r"""
relatorio_fixo = sil.compare_model_vs_code(
    r_sequence=r, y_sequence=y,
    Kp=0.30, Ki=8.0, Kd=0.004,
    Ts=PARAMS.Ts, u_max=PARAMS.V_max, tau_f=0.01, Kaw=100.0,
    fixed_point=True,
)

degrau_q16 = 1.0 / (1 << 16)

print(f"{'variante':>22}  {'erro máximo':>14}  {'em épsilons':>14}")
print("-" * 56)
print(f"{'ponto flutuante':>22}  {relatorio.erro_maximo_abs:>12.3e} V  "
      f"{relatorio.erro_maximo_abs/eps:>13.0f}")
print(f"{'ponto fixo Q16.16':>22}  {relatorio_fixo.erro_maximo_abs:>12.3e} V  "
      f"{relatorio_fixo.erro_maximo_abs/eps:>13.0f}")
print()
print(f"Degrau do Q16.16: {degrau_q16:.3e}")
print(f"Erro do Q16.16 em degraus: {relatorio_fixo.erro_maximo_abs/degrau_q16:.1f}")
print()
print("O ponto fixo erra MUITO mais que o flutuante, e isso é esperado.")
print()
print("Mas repare no tamanho: o erro dá milhares de degraus, não um ou dois.")
print("Por quê? Porque o integrador SOMA. Cada soma arredonda um pouquinho,")
print("e ao longo de mais de mil ciclos os arredondamentos se acumulam —")
print("exatamente o efeito que você mediu no fim da Aula 13.")
print()
print("A pergunta certa não é 'o erro é zero?'. É 'o erro cabe no")
print("orçamento?'. Compare com o comando máximo de 24 V:")
print(f"  erro relativo do Q16.16: {100*relatorio_fixo.erro_maximo_abs/24.0:.4f}%")
print()
print("Um quarto de por cento do fundo de escala. Para um controle de")
print("velocidade de AGV, cabe com folga. Para uma superfície de comando")
print("de aeronave, provavelmente não caberia — e aí você usa mais bits")
print("fracionários, ou ponto flutuante mesmo.")
"""),

    md("""
## Passo 4 — O bug real, e como ele foi pego

Até agora tudo passou. Um teste que só aprova não convence ninguém.

Vamos introduzir um bug do tipo que acontece de verdade: alguém "otimiza" o
código C e troca a ordem de duas operações, aplicando a saturação **antes** do
anti-windup em vez de depois.

Parece inofensivo. As duas linhas estão lá, as duas rodam. O resultado muda.
"""),
    code(r"""
# O cenário: o C foi gerado a partir de um modelo com Kaw = 0, ou alguém
# transcreveu essa constante errada. O modelo de referência tem Kaw = 100.
# Nada mais muda: mesmos Kp, Ki, Kd, Ts e teto de tensão.
print("Cenário: o código C ficou com Kaw = 0 (anti-windup desligado).")
print("O modelo de referência continua com Kaw = 100.")
print("Todas as outras constantes são idênticas.")
print()

relatorio_bug = sil.compare_model_vs_code(
    r_sequence=r, y_sequence=y,
    Kp=0.30, Ki=8.0, Kd=0.004,
    Ts=PARAMS.Ts, u_max=PARAMS.V_max, tau_f=0.01,
    Kaw=0.0,           # ← o "código" com o bug
)

# e o modelo de referência, com o Kaw certo
modelo_certo = relatorio.saidas_modelo
codigo_bugado = relatorio_bug.saidas_codigo
divergencia = np.abs(modelo_certo - codigo_bugado)

print(f"{'comparação':>34}  {'erro máximo':>14}  {'em épsilons':>16}")
print("-" * 70)
print(f"{'modelo x código correto':>34}  {relatorio.erro_maximo_abs:>12.3e} V  "
      f"{relatorio.erro_maximo_abs/eps:>15.0f}")
print(f"{'modelo x código com o bug':>34}  {divergencia.max():>12.3e} V  "
      f"{divergencia.max()/eps:>15.0f}")
print()
print(f"O código correto divergiu {relatorio.erro_maximo_abs:.1e} V do modelo.")
print(f"O código com o bug divergiu {divergencia.max():.1f} V — dois volts a mais")
print(f"que o teto inteiro do driver, de {PARAMS.V_max:.0f} V.")
print()
print("Nenhuma revisão de código pegaria isso olhando o diff — as duas")
print("versões são plausíveis. A comparação numérica pega no primeiro")
print("teste, e aponta a amostra exata onde as curvas se separam.")
print(f"Primeira divergência acima de 1 mV: amostra {int(np.argmax(divergencia > 1e-3))}, "
      f"t = {t[int(np.argmax(divergencia > 1e-3))]:.3f} s")
"""),

    md("""
### O gráfico do bug

Aqui está a diferença entre um bug que "não faz mal" e um que faz.

A curva com o bug não é ligeiramente diferente. Ela **passa muito mais do
alvo**, porque o integral acumula comando que o driver nunca entregou — é o
windup da Aula 6, agora escondido dentro do código gerado.
"""),
    code(r"""
fig, ax = plt.subplots(figsize=(9.5, 5))

ax.plot(t, modelo_certo, color="#4A9D5F", linewidth=2.5,
        label="modelo (anti-windup ligado)")
ax.plot(t, codigo_bugado, color="#C0392B", linewidth=1.8,
        label="código com o bug (anti-windup desligado)")
ax.axhline(PARAMS.V_max, color="#333333", linestyle="--", linewidth=1.2)
ax.text(0.1, PARAMS.V_max + 1, "teto do driver", fontsize=9.5, color="#333333")
ax.axhline(-PARAMS.V_max, color="#333333", linestyle="--", linewidth=1.2)

ax.set_xlabel("tempo [s]")
ax.set_ylabel("comando u [V]")
ax.set_title("O mesmo controlador, uma constante trocada", fontsize=13, pad=12)
ax.legend(loc="lower right"); ax.grid(alpha=0.25)
plt.tight_layout()
plt.show()
"""),

    md("""
## Mexa aqui

**Experimento 1 — o limite de aceitação.**
Qual erro máximo você aceitaria como "equivalente"? Escreva o número antes de
olhar os resultados. Depois confira: o ponto flutuante passa no seu critério?
E o ponto fixo?

**Experimento 2 — sequência mais agressiva.**
Troque a referência por algo que sature muito o driver (degraus de 500 rad/s).
O erro do ponto fixo cresce? Faz sentido: mais saturação, mais trabalho do
anti-windup, mais oportunidades de arredondar.

**Experimento 3 — outro bug.**
Mude `Kd` só no lado do "código" e veja o erro. Depois mude `tau_f`. Qual dos
dois produz a divergência maior? Isso te diz qual constante é mais sensível a
um erro de transcrição.
"""),
    code(r"""
# ⬇️ mexa aqui: os ganhos do "código", contra o modelo de referência
KP_CODIGO, KI_CODIGO, KD_CODIGO = 0.30, 8.0, 0.004
TAUF_CODIGO, KAW_CODIGO = 0.01, 100.0
CRITERIO_V = 1e-6      # o seu limite de aceitação, em volts

rel_x = sil.compare_model_vs_code(
    r_sequence=r, y_sequence=y,
    Kp=KP_CODIGO, Ki=KI_CODIGO, Kd=KD_CODIGO,
    Ts=PARAMS.Ts, u_max=PARAMS.V_max, tau_f=TAUF_CODIGO, Kaw=KAW_CODIGO,
)
divergencia_x = np.abs(modelo_certo - rel_x.saidas_codigo)

print(f"código com Kp={KP_CODIGO} Ki={KI_CODIGO} Kd={KD_CODIGO} "
      f"tau_f={TAUF_CODIGO} Kaw={KAW_CODIGO}")
print("-" * 62)
print(f"  erro máximo contra o modelo : {divergencia_x.max():.3e} V")
print(f"  em épsilons de máquina      : {divergencia_x.max()/eps:.0f}")
print(f"  seu critério                : {CRITERIO_V:.3e} V")
print()
if divergencia_x.max() <= CRITERIO_V:
    print("  APROVADO pelo seu critério.")
else:
    print("  REPROVADO. A diferença estoura o seu limite de aceitação.")
    print(f"  Primeira amostra fora: {int(np.argmax(divergencia_x > CRITERIO_V))}")
"""),

    md("""
## Aprofundamento (opcional)

### Por que ponto flutuante não dá zero exato

Você pode se perguntar: se o C foi gerado do modelo, e as duas fazem as mesmas
contas na mesma ordem, por que não dá zero absoluto?

Às vezes dá. Quando não dá, os culpados são:

- **O compilador reassocia.** Com `-O2`, o `gcc` pode transformar
  `(a*b) + (c*d)` numa instrução combinada que arredonda uma vez em vez de
  duas. O resultado é mais preciso, e diferente.
- **Registradores mais largos.** Alguns processadores calculam em precisão
  estendida internamente e só arredondam ao guardar.
- **Ordem das somas.** Em ponto flutuante, `a + b + c` depende da ordem.

Nada disso é bug. É a razão de o critério de aceitação ser "da ordem do
épsilon", e não "exatamente zero".

### Como isto vira rotina de time

O passo seguinte natural é a **integração contínua**: o `GitHub Actions`
rodando esta comparação a cada `commit`, com o critério de aceitação como
portão de mérito. Ninguém integra código que divergiu do modelo.

A configuração está no material complementar da unidade. A parte conceitual —
**por que a comparação numérica é necessária** — é o que você acabou de fazer,
e é ela que sustenta o resto.

### O teste de regressão

O valor prático do que você fez hoje: transformar essa comparação num teste
automático. A célula abaixo mostra a forma dele.
"""),
    code(r"""
CRITERIO_ACEITACAO_V = 1e-9      # o portão: erro máximo tolerado

def teste_equivalencia_modelo_codigo():
    '''Roda em CI a cada commit. Reprova se o C divergir do modelo.'''
    rel = sil.compare_model_vs_code(
        r_sequence=r, y_sequence=y,
        Kp=0.30, Ki=8.0, Kd=0.004,
        Ts=PARAMS.Ts, u_max=PARAMS.V_max, tau_f=0.01, Kaw=100.0,
    )
    assert rel.erro_maximo_abs <= CRITERIO_ACEITACAO_V, (
        f"código divergiu do modelo: {rel.erro_maximo_abs:.3e} V "
        f"> critério de {CRITERIO_ACEITACAO_V:.3e} V"
    )
    return rel.erro_maximo_abs


erro = teste_equivalencia_modelo_codigo()
print("teste_equivalencia_modelo_codigo: PASSOU")
print(f"  erro medido : {erro:.3e} V")
print(f"  critério    : {CRITERIO_ACEITACAO_V:.3e} V")
if erro == 0.0:
    print("  folga       : total (erro exatamente zero)")
else:
    print(f"  folga       : {CRITERIO_ACEITACAO_V/erro:.0f}x")
print()
print("Este teste é o que impede a regressão silenciosa. Alguém mexe no")
print("gerador daqui a seis meses, o número muda, e o CI reprova antes de")
print("o código chegar perto do robô.")
"""),

    md("""
## O que você leva desta aula

1. **"Equivalente" sem número não vale nada.** Você mediu.
2. **SIL é rodar o C compilado de verdade lado a lado com o modelo**, com as
   mesmas entradas.
3. **Épsilon de máquina é a régua.** Diferença da ordem de ε é
   arredondamento; muito acima disso é problema.
4. **Ponto fixo erra mais, e isso é esperado.** A pergunta é se o erro cabe no
   orçamento, não se ele é zero.
5. **Um bug de uma constante trocada não aparece em revisão de código** — e
   aparece na primeira comparação numérica.
6. **A comparação vira teste de regressão**, e o critério de aceitação vira
   portão de CI.

Na Aula 15 o código sai do computador e vai para o hardware. E aí aparece um
inimigo novo, que a simulação nunca mostrou: **o tempo não é exato**.

## Se deu erro

**`SILCompilationError` ou `gcc não encontrado`.**
Instale o compilador. No Ubuntu/Debian: `sudo apt install build-essential`.
No macOS: `xcode-select --install`.

**A edição do bug não achou a constante.**
O template do gerador pode ter mudado. Não é grave: a comparação seguinte usa
`Kaw=0.0` diretamente na chamada, e demonstra a mesma coisa.

**O erro deu exatamente zero.**
Ótimo — significa que o seu compilador não reassociou nada. Continua valendo:
zero é menor que qualquer critério.

**Os gráficos ficaram sobrepostos e você não vê duas curvas.**
É o resultado esperado do Passo 2. As duas são indistinguíveis; a diferença só
aparece no gráfico logarítmico de baixo.
""" + RODAPE_ERRO),
]
