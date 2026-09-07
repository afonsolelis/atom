"""Notebook da Aula 13 — o código que ninguém digita."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import ABERTURA_IMPORTS, GLOSSARIO, RODAPE_ERRO, md, code  # noqa: E402

TITULO = "Aula 13 — O código que ninguém digita"
SLUG = "geracao_de_codigo"

CELULAS = [
    md("""
# Aula 13 — O código que ninguém digita

## O que você vai fazer aqui

Você tem um controlador que funciona e foi verificado. Agora ele precisa rodar
num microcontrolador, escrito em C.

A pergunta desta aula: **quem escreve esse C?**

Se for uma pessoa, ela vai transcrever ganhos à mão. E um dia vai digitar
`4,0` onde era `0,4`. Ninguém vai perceber, porque um número plausível não
chama atenção.

Hoje você gera o C a partir do modelo. Ninguém digita, ninguém erra de digitar.

**Pré-requisito:** notebook da Aula 6 (o PID).
"""),

    md("""
## Antes de começar

### 1. Código gerado é artefato derivado

Uma regra que vale para o resto da sua carreira:

> **Arquivo gerado nunca se edita à mão.**

É como a saída de um compilador. Se você não gosta do que saiu, muda a
entrada — o modelo — e gera de novo.

No momento em que alguém "só ajeita uma linha" no C gerado, a próxima geração
apaga o ajeite, e a rastreabilidade entre modelo e código morre. Por isso o
arquivo gerado costuma trazer um aviso no topo dizendo exatamente isso.

### 2. Ponto flutuante × ponto fixo

Duas formas de o computador guardar um número com casas decimais.

**Ponto flutuante** (`float`, `double`): a vírgula "flutua". O computador
guarda o número em notação científica, então representa tanto 0,0000001 quanto
1.000.000. É flexível e é o que o seu PC usa.

**Ponto fixo**: a vírgula fica travada num lugar. É como **contar tudo em
centavos**: em vez de guardar R$ 12,34 como número quebrado, você guarda 1234
centavos, que é inteiro.

Por que alguém escolheria ponto fixo?

- Microcontrolador barato **não tem hardware de ponto flutuante**. Ele
  simularia em software, dezenas de vezes mais devagar.
- Ponto fixo é **determinístico e previsível**: você sabe exatamente qual é o
  menor degrau representável.

O preço: precisão limitada, e o risco de estourar a faixa.

### 3. O que significa `Q16.16`

É a notação de ponto fixo que esta aula usa. Lê-se "cu dezesseis ponto
dezesseis", e quer dizer:

- **32 bits** no total,
- **16 bits** para a parte inteira,
- **16 bits** para a parte fracionária.

Traduzindo em números concretos:

- o menor degrau que dá para representar é 1/65536, ou seja **0,0000153**;
- a faixa vai de aproximadamente −32.768 a +32.767.

Guardar um número em Q16.16 é multiplicar por 65536 e arredondar para inteiro.

### 4. O que é um *hash*

Um **hash** é uma assinatura curta calculada a partir de um conteúdo.

Propriedade essencial: **mude qualquer coisa no conteúdo, e a assinatura muda
completamente**. Não um pouquinho — completamente.

Serve para responder, em um segundo, à pergunta que aparece em toda auditoria:
*"este código foi gerado a partir daqueles parâmetros exatos?"*
"""),

    md(GLOSSARIO),

    md("""
## Passo 1 — Gerando o C

A célula abaixo pega o `DiscretePID` — o mesmo objeto Python das Aulas 6 e 7 —
e gera dois arquivos C a partir dele.

Repare no que **não** acontece: ninguém digita um número.
"""),
    code(ABERTURA_IMPORTS + r"""
import tempfile
from pathlib import Path
from nexabot.params import PARAMS
from nexabot.controllers import DiscretePID
from nexabot.codegen import generate

pid = DiscretePID(Kp=0.30, Ki=8.0, Kd=0.004, Ts=PARAMS.Ts,
                  u_max=PARAMS.V_max, Kaw=100.0)

saida = Path(tempfile.mkdtemp(prefix="nexabot_aula13_"))
gerado = generate.generate_pid_controller(pid, output_dir=saida)

print("Gerado a partir do modelo:")
print(f"  {gerado.header_path.name}  ({gerado.header_path.stat().st_size} bytes)")
print(f"  {gerado.source_path.name}  ({gerado.source_path.stat().st_size} bytes)")
print()
print(f"Assinatura dos parâmetros (hash): {gerado.params_hash}")
print(f"Gerado em: {gerado.generated_at_iso}")
print()
print("Os ganhos que entraram no código:")
for nome, valor in gerado.gains.items():
    print(f"  {nome:>12} = {valor}")
"""),

    md("""
## Passo 2 — O cabeçalho de rastreabilidade

Abra o começo do arquivo gerado.

Ele não começa com código. Começa com um bloco de comentário que responde a
todas as perguntas que uma auditoria faria: de onde veio, quando, com quais
parâmetros, e com qual assinatura.

Isso não é burocracia. É o que transforma "confie em mim" em "confira você
mesmo".
"""),
    code(r"""
fonte = gerado.source_path.read_text(encoding="utf-8")
linhas = fonte.splitlines()

# o bloco de rastreabilidade vai até o fim do primeiro comentário
fim = next(i for i, l in enumerate(linhas) if l.strip().endswith("*/"))
print("\n".join(linhas[:fim + 1]))
"""),

    md("""
## Passo 3 — O hash muda quando o ganho muda

Aqui está a demonstração que faz a assinatura valer alguma coisa.

Vamos gerar o mesmo controlador duas vezes. Na segunda, mudamos **um** ganho,
e por um valor pequeno — de `0,300` para `0,301`.

Um humano revisando o diff pode não notar. O hash nota.
"""),
    code(r"""
saida2 = Path(tempfile.mkdtemp(prefix="nexabot_aula13b_"))
pid_igual = DiscretePID(Kp=0.30, Ki=8.0, Kd=0.004, Ts=PARAMS.Ts,
                        u_max=PARAMS.V_max, Kaw=100.0)
pid_diferente = DiscretePID(Kp=0.301, Ki=8.0, Kd=0.004, Ts=PARAMS.Ts,
                            u_max=PARAMS.V_max, Kaw=100.0)

g_igual = generate.generate_pid_controller(pid_igual, output_dir=saida2)
g_dif = generate.generate_pid_controller(pid_diferente, output_dir=Path(tempfile.mkdtemp()))

print(f"{'controlador':>24}  {'Kp':>8}  assinatura")
print("-" * 62)
print(f"{'original':>24}  {0.300:>8.3f}  {gerado.params_hash}")
print(f"{'gerado de novo, igual':>24}  {0.300:>8.3f}  {g_igual.params_hash}")
print(f"{'com Kp = 0,301':>24}  {0.301:>8.3f}  {g_dif.params_hash}")
print()
if gerado.params_hash == g_igual.params_hash:
    print("Mesmos parâmetros -> mesma assinatura. A geração é DETERMINÍSTICA:")
    print("rodar de novo produz exatamente o mesmo resultado.")
print()
if gerado.params_hash != g_dif.params_hash:
    print("Um ganho mudou na terceira casa decimal, e a assinatura ficou")
    print("completamente diferente. Não parecida: diferente.")
    print()
    print("É isso que responde 'este binário veio destes parâmetros?' sem")
    print("ninguém precisar comparar arquivo linha a linha.")
"""),

    md("""
## Passo 4 — O código gerado, por dentro

Agora olhe o miolo: a função que roda a cada 5 milissegundos no
microcontrolador.

Compare com a `DiscretePID.step` que você leu na Aula 6. É a mesma sequência
de operações — erro, integral, derivada filtrada, saturação, anti-windup — só
que em C, com os ganhos já embutidos como constantes.
"""),
    code(r"""
# imprime a função de passo do controlador em ponto flutuante
inicio = next(i for i, l in enumerate(linhas) if "pid_step" in l and "(" in l)
trecho = linhas[inicio:inicio + 34]
print("\n".join(trecho))
"""),

    md("""
## Passo 5 — Ponto fixo: contando em centavos

O mesmo controlador, agora em `Q16.16`.

Primeiro, a intuição, com números que você consegue conferir de cabeça. A
célula abaixo converte alguns valores para Q16.16 e de volta, mostrando o erro
que a conversão introduz.
"""),
    code(r"""
ESCALA = 1 << 16       # 2^16 = 65536

def para_q16(x):
    '''Guarda um número real como inteiro de 32 bits, no formato Q16.16.'''
    return int(round(x * ESCALA))

def de_q16(q):
    '''Volta de Q16.16 para número real.'''
    return q / ESCALA

print(f"Menor degrau representável em Q16.16: {1/ESCALA:.8f}")
print(f"Faixa: de {-(1<<31)/ESCALA:.0f} a {((1<<31)-1)/ESCALA:.4f}")
print()
print(f"{'valor real':>14}  {'guardado como':>16}  {'volta como':>16}  {'erro':>14}")
print("-" * 68)
for x in (0.30, 8.0, 0.004, 1.0/3.0, 24.0, 0.0000153):
    q = para_q16(x)
    volta = de_q16(q)
    print(f"{x:>14.7f}  {q:>16d}  {volta:>16.7f}  {abs(x-volta):>14.9f}")

print()
print("Repare na linha do 1/3: ele não cabe exato em Q16.16, como também não")
print("cabe exato em decimal. O erro é de menos de 0,00002 — o tamanho de um")
print("degrau. E ele é PREVISÍVEL, que é a graça do ponto fixo.")
"""),

    md("""
### Onde o ponto fixo dói

Aquele erro de um degrau parece desprezível. E é — para um número isolado.

O problema aparece quando o erro se **acumula**. O termo integral do PID soma
o erro a cada ciclo, 200 vezes por segundo. Se cada soma erra um pouquinho, o
erro cresce.

A célula abaixo mede isso: dois integradores, um em ponto flutuante e outro em
Q16.16, somando o mesmo erro por 10 segundos.
"""),
    code(r"""
import numpy as np

n_ciclos = int(10.0 / PARAMS.Ts)      # 10 segundos
erro_por_ciclo = 0.7                  # rad/s, um erro pequeno e constante
Ki = 8.0

acumulado_float = 0.0
acumulado_q16 = 0
incremento_q16 = para_q16(Ki * PARAMS.Ts * erro_por_ciclo)

for _ in range(n_ciclos):
    acumulado_float += Ki * PARAMS.Ts * erro_por_ciclo
    acumulado_q16 += incremento_q16

resultado_q16 = de_q16(acumulado_q16)
desvio = abs(acumulado_float - resultado_q16)

print(f"Somando o mesmo incremento {n_ciclos} vezes (10 segundos a 200 Hz):")
print("-" * 58)
print(f"  em ponto flutuante : {acumulado_float:14.8f}")
print(f"  em Q16.16          : {resultado_q16:14.8f}")
print(f"  desvio acumulado   : {desvio:14.8f}")
print(f"  em termos relativos: {100*desvio/acumulado_float:14.8f}%")
print()
print("Menos de um centésimo de por cento depois de 2000 somas. Q16.16")
print("aguenta este controlador com folga.")
print()
print("Mas o número não é 'sempre pequeno': ele depende do incremento e do")
print("número de ciclos. Numa aplicação que integra por horas, você precisa")
print("refazer esta conta. É por isso que ela está aqui, e não numa tabela.")
"""),

    md("""
## Mexa aqui

**Experimento 1 — o incremento pequeno demais.**
Baixe `erro_por_ciclo` para `0.0001`. O incremento em Q16.16 vira zero, e o
integrador **para de integrar completamente**. Esse é o modo de falha
clássico do ponto fixo: erros pequenos somem, e o controlador nunca corrige
um desvio pequeno.

**Experimento 2 — mais casas fracionárias.**
Troque `ESCALA` para `1 << 24` (formato Q8.24). O erro cai, mas a faixa
inteira encolhe para ±128. Todo formato de ponto fixo é essa troca: precisão
contra faixa.

**Experimento 3 — o estouro.**
Com Q16.16, tente guardar `40000`. O valor não cabe nos 16 bits inteiros e o
resultado vira lixo. Num microcontrolador, isso não dá erro — dá um número
errado que segue adiante.
"""),
    code(r"""
# ⬇️ mexa aqui
ESCALA_TESTE = 1 << 16        # tente 1 << 24
ERRO_POR_CICLO = 0.7          # tente 0.0001
VALOR_TESTE = 100.0           # tente 40000

bits_frac = ESCALA_TESTE.bit_length() - 1
bits_int = 32 - bits_frac
print(f"Formato Q{bits_int}.{bits_frac}")
print("-" * 56)
print(f"  menor degrau : {1/ESCALA_TESTE:.10f}")
print(f"  faixa        : de {-(1<<31)/ESCALA_TESTE:.1f} a {((1<<31)-1)/ESCALA_TESTE:.4f}")
print()

incremento = int(round(8.0 * PARAMS.Ts * ERRO_POR_CICLO * ESCALA_TESTE))
print(f"  incremento do integrador (erro = {ERRO_POR_CICLO}): {incremento}")
if incremento == 0:
    print("  ⚠ ZERO. O integrador não vai integrar nada — o erro é pequeno")
    print("    demais para ser representado. O robô nunca corrige esse desvio.")

print()
q = int(round(VALOR_TESTE * ESCALA_TESTE))
cabe = -(1 << 31) <= q < (1 << 31)
print(f"  guardar {VALOR_TESTE} -> {q}")
print(f"  cabe em 32 bits? {'sim' if cabe else 'NÃO — vai estourar e virar lixo'}")
"""),

    md("""
## Aprofundamento (opcional)

### De onde vem a equação de diferenças

Uma pergunta legítima: como o gerador sabe transformar a integral contínua
numa soma?

Ele não sabe — ele **deriva**, simbolicamente, com o SymPy. A célula abaixo
mostra as recorrências que o gerador produziu, e que foram para dentro do C.

Nenhuma dessas linhas foi digitada por alguém. Elas saem da forma contínua do
PID mais a regra de discretização escolhida (Euler para trás), pela mesma
álgebra que você viu no Aprofundamento da Aula 3.

### A derivação completa

O caminho simbólico inteiro — do PID contínuo até a equação de diferenças, com
a manipulação em `z⁻¹` — está no material complementar.

Ele é conteúdo de quem vai escrever geradores de código. Para entender **por
que o código gerado é confiável**, basta ver a entrada, a saída e a evidência
de que uma corresponde à outra, que é o que a célula abaixo mostra.
"""),
    code(r"""
from nexabot.codegen import derive

recorrencias = derive.derive_all()

print("As equações de diferenças derivadas simbolicamente:")
print()
for nome, rec in recorrencias.items():
    print(f"  {nome}:")
    print(f"    {rec.equacao_str}")
    print()

print("Compare com o contrato numérico documentado na DiscretePID:")
print()
print("    I[k] = I[k-1] + Ki.Ts.e[k]")
print("    D[k] = (Kd.(e[k]-e[k-1]) + tau_f.D[k-1]) / (tau_f + Ts)")
print()
print("São as mesmas. E as do C foram derivadas, não copiadas — é por isso")
print("que a cadeia modelo -> código não tem um humano no meio.")
"""),

    md("""
## O que você leva desta aula

1. **Arquivo gerado nunca se edita à mão.** Mudou? Muda o modelo e gera de
   novo.
2. **O cabeçalho de rastreabilidade responde à auditoria** antes de ela
   perguntar.
3. **Hash é assinatura.** Mudou um ganho na terceira casa, a assinatura muda
   inteira.
4. **A geração é determinística.** Mesma entrada, mesma saída, sempre.
5. **Ponto fixo é contar em centavos.** Previsível e rápido, com precisão e
   faixa limitadas.
6. **Em Q16.16 o degrau é 0,0000153.** Erro pequeno que se acumula precisa ser
   medido, não presumido.
7. **O modo de falha do ponto fixo é silencioso**: incremento vira zero, ou o
   valor estoura, e nada avisa.

Na Aula 14 você vai compilar esse C, rodar lado a lado com o modelo Python, e
**medir** se os dois concordam — porque até agora "equivalente" é só uma
palavra.

## Se deu erro

**`ModuleNotFoundError: No module named 'jinja2'`.**
O gerador usa templates Jinja2:
`uv pip install --python .venv/bin/python jinja2`.

**`StopIteration` ao imprimir o cabeçalho.**
O formato do arquivo gerado mudou e o `next(...)` não achou a marca. Abra o
arquivo direto: o caminho está impresso na primeira célula.

**O hash deu diferente do meu.**
Ele depende dos ganhos, então se você mexeu no `DiscretePID`, muda mesmo. Isso
é o comportamento correto — é justamente o que a aula demonstra.
""" + RODAPE_ERRO),
]
