"""Trechos compartilhados pelos dezesseis notebooks."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import code, md  # noqa: F401,E402  (reexportado para os fontes)

# Toda primeira célula de código ajusta o caminho sozinha, para o notebook
# funcionar tanto aberto de `notebooks/` quanto de `projeto_nexabot/`.
#
# ATENÇÃO: toda célula de código é declarada como *raw string* (r"""...""").
# Sem o `r`, um `\n` dentro de um print viraria quebra de linha de verdade na
# hora do import e quebraria a string no notebook gerado.
ABERTURA_IMPORTS = r"""
import sys
from pathlib import Path

# Acha o pacote `nexabot` esteja o notebook aberto de onde estiver.
for candidato in [Path.cwd(), *Path.cwd().parents]:
    if (candidato / "projeto_nexabot" / "nexabot").is_dir():
        sys.path.insert(0, str(candidato / "projeto_nexabot"))
        break
    if (candidato / "nexabot" / "params.py").is_file():
        sys.path.insert(0, str(candidato))
        break
"""

RODAPE_ERRO = """
---

*Notebook da disciplina Model-Based Design for Cyber-Physical Systems ·
UniFECAF · Prof. Afonso Cesar Lelis Brandão. Os números vêm de
`projeto_nexabot/nexabot/params.py`, a fonte única de verdade da disciplina.*
"""


# Tabela de símbolos, repetida em todo notebook. O aluno não precisa lembrar
# de qual aula veio cada letra — ela está sempre ali, a um scroll de distância.
GLOSSARIO = """
## Como se lê cada símbolo

Guarde esta tabela. Ela vale para as 16 aulas, e nenhuma letra vai aparecer
aqui sem estar nela.

### Letras gregas

| Símbolo | Nome | Lê-se | O que é |
| --- | --- | --- | --- |
| ω | ômega minúsculo | *ô-me-ga* | Velocidade de giro do eixo, em radianos por segundo |
| τ | tau | *táu* | Duas coisas, e o contexto diz qual: **torque** (força de giro, em N·m) ou **constante de tempo** (quanto o sistema demora, em segundos) |
| Δ | delta maiúsculo | *dél-ta* | "A variação de" — Δt é um pedacinho de tempo |
| π | pi | *pi* | 3,1416. Uma volta inteira são 2π = 6,28 radianos |
| Σ | sigma maiúsculo | *sig-ma* | "A soma de tudo isto" |
| ε | épsilon | *ép-si-lon* | Um número bem pequenininho |
| φ | fi | *fi* | Ângulo de fase — o quanto um sinal atrasa em relação a outro |

### Letras latinas desta disciplina

| Símbolo | Lê-se | O que é |
| --- | --- | --- |
| `R` | erre | Resistência do fio do motor, em ohm |
| `L` | ele | Indutância do fio, em henry — resiste a mudar a corrente rápido |
| `Kt` | ká-tê | Constante de torque: quanto giro por ampère |
| `Ke` | ká-ê | Constante de tensão: quanta tensão o motor gera ao girar |
| `J` | jota | Inércia: o quanto o eixo custa a acelerar |
| `b` | bê | Atrito viscoso: o que rouba giro |
| `Ts` | tê-esse | Período de amostragem: de quanto em quanto tempo o controlador olha |
| `i` | i | Corrente elétrica, em ampère |
| `V` ou `u` | vê / u | Tensão aplicada no motor, em volt |
| `r` | erre | Referência: a velocidade que você **quer** |
| `y` | ípsilon | Saída medida: a velocidade que você **tem** |
| `e` | e | Erro: a diferença entre as duas, `e = r − y` |
| `s` | esse | A variável de Laplace (Aula 3). Multiplicar por `s` é o mesmo que derivar |

### Como ler uma equação

Não tente ler tudo de uma vez. Toda equação desta disciplina se lê em três
passos:

1. **O que está do lado esquerdo do igual?** É a coisa que você quer saber.
2. **Quantas parcelas tem do lado direito?** Cada uma somando ou subtraindo é
   um efeito físico separado.
3. **O que cada parcela faz?** Uma empurra, outra freia, outra atrapalha.

Se você conseguir dizer em português o que cada parcela faz, você entendeu a
equação. O resto é conta.
"""
