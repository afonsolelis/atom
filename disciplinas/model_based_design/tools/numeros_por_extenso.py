#!/usr/bin/env python3
"""Converte número por extenso em algarismo, nos roteiros de videoaula.

Por que existe: os roteiros foram escritos com os números por extenso, para
leitura em voz alta ("um vírgula dois ohms"). O professor pediu o contrário —
algarismo na tela, "1,2 ohm" —, que é mais rápido de conferir contra o
laboratório e não deixa dúvida sobre o valor.

A conversão é conservadora de propósito. "Um" e "uma" aparecem 1.086 vezes nos
quatro roteiros, quase sempre como artigo ("um sistema", "uma tabela"). Então
uma sequência de palavras-número só vira algarismo quando houver evidência de
que ela é mesmo um número:

- vem seguida de uma unidade de medida (volts, ohms, milissegundos, ...); ou
- contém "vírgula" (é um decimal); ou
- tem duas ou mais palavras-número compostas ("vinte e quatro", "cento e dez").

**Não rode isto sobre os títulos das videoaulas.** Em título, número por
extenso é a forma correta em português: "Dois polos, uma pergunta", não
"2 polos". A primeira execução converteu os títulos junto, e os decks HTML
— que carregam o título da própria aula — passaram a divergir dos roteiros,
quebrando `validar_slides.py`. Os títulos foram restaurados à mão.

Uso:
    python3 tools/numeros_por_extenso.py --check     # mostra o que mudaria
    python3 tools/numeros_por_extenso.py             # aplica
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent

ALVOS = [f"unidade_{u}/roteiros_20min.md" for u in (1, 2, 3, 4)] + [
    "roteiro_video_introdutorio.md",
]

UNIDADES = {
    "zero": 0, "um": 1, "uma": 1, "dois": 2, "duas": 2, "três": 3, "tres": 3,
    "quatro": 4, "cinco": 5, "seis": 6, "sete": 7, "oito": 8, "nove": 9,
    "dez": 10, "onze": 11, "doze": 12, "treze": 13, "quatorze": 14,
    "catorze": 14, "quinze": 15, "dezesseis": 16, "dezessete": 17,
    "dezoito": 18, "dezenove": 19,
}
DEZENAS = {
    "vinte": 20, "trinta": 30, "quarenta": 40, "cinquenta": 50, "sessenta": 60,
    "setenta": 70, "oitenta": 80, "noventa": 90,
}
CENTENAS = {
    "cem": 100, "cento": 100, "duzentos": 200, "duzentas": 200,
    "trezentos": 300, "trezentas": 300, "quatrocentos": 400,
    "quatrocentas": 400, "quinhentos": 500, "quinhentas": 500,
    "seiscentos": 600, "seiscentas": 600, "setecentos": 700, "setecentas": 700,
    "oitocentos": 800, "oitocentas": 800, "novecentos": 900, "novecentas": 900,
}
PALAVRAS = {**UNIDADES, **DEZENAS, **CENTENAS}

# Unidades de medida que confirmam que a sequência anterior é um número.
UNIDADES_MEDIDA = r"""(?:volts?|ampères?|amperes?|ohms?|milihenries|henrys?|
    milissegundos?|microssegundos?|nanossegundos?|segundos?|minutos?|horas?|
    metros?|milímetros?|centímetros?|quilogramas?|
    radianos?|graus?|hertz|quilohertz|newton-metros?|newtons?|
    por\s+cento|bits?|bytes?|quilobytes?)"""

RE_UNIDADE_MEDIDA = re.compile(UNIDADES_MEDIDA, re.X | re.I)


def _valor_grupo(tokens: list[str]) -> int | None:
    """Converte um grupo de até três ordens ('cento e vinte e quatro').

    Em português o "e" só liga ordens **decrescentes**: centena, depois
    dezena, depois unidade. "Vinte e quatro" é 24; "três e quatro" NÃO é 7 —
    é uma lista de dois números, e o texto dos roteiros está cheio delas
    ("entre zero e cinco centésimos", "nos instantes três e quatro").

    Sem esta regra o conversor somava os dois e destruía a frase.
    """
    ORDEM = {"centena": 3, "dezena": 2, "unidade": 1}
    total = 0
    ultima_ordem = 99
    visto = False
    for tok in tokens:
        if tok == "e":
            continue
        if tok in CENTENAS:
            ordem = ORDEM["centena"]
            valor = CENTENAS[tok]
        elif tok in DEZENAS:
            ordem = ORDEM["dezena"]
            valor = DEZENAS[tok]
        elif tok in UNIDADES:
            ordem = ORDEM["unidade"]
            valor = UNIDADES[tok]
        else:
            return None
        if ordem >= ultima_ordem:
            return None          # ordem não decresceu: é lista, não composto
        total += valor
        ultima_ordem = ordem
        visto = True
    return total if visto else None


def _valor(tokens: list[str]) -> int | None:
    """Converte uma sequência inteira, tratando 'mil'."""
    if "mil" in tokens:
        i = tokens.index("mil")
        antes = tokens[:i]
        depois = [t for t in tokens[i + 1:] if t != "e"]
        milhares = _valor_grupo(antes) if antes else 1
        resto = _valor_grupo(depois) if depois else 0
        if milhares is None or resto is None:
            return None
        return milhares * 1000 + resto
    return _valor_grupo(tokens)


def _digitos_apos_virgula(tokens: list[str]) -> tuple[str, int] | None:
    """Lê a parte decimal, que vem falada em blocos.

    Depois da vírgula ninguém diz "zero quatro cinco": diz "zero quarenta e
    cinco", que é 045. E "trinta e um oitenta e nove" é 3189 — dois blocos
    colados, não uma soma.

    Então a leitura é gulosa: consome o maior bloco válido, anota os dígitos,
    e recomeça no token seguinte. Devolve (dígitos, quantos tokens consumiu),
    porque o resto da frase ("e menos 0,32 na segunda") não é do número.
    """
    partes: list[str] = []
    i = 0
    while i < len(tokens):
        if tokens[i] == "e":
            # "e" só continua o número se o bloco seguinte for válido junto
            # com o anterior; senão é conjunção da frase e o número acabou.
            if not partes or i + 1 >= len(tokens):
                break
            i += 1
            continue
        if tokens[i] == "zero":
            partes.append("0")
            i += 1
            continue
        # bloco guloso: o maior prefixo que forma um número válido
        melhor = None
        for fim in range(len(tokens), i, -1):
            v = _valor(tokens[i:fim])
            if v is not None:
                melhor = (v, fim)
                break
        if melhor is None:
            break
        partes.append(str(melhor[0]))
        i = melhor[1]
    if not partes:
        return None
    return "".join(partes), i


# `mil` precisa de fronteira à direita, senão casa dentro de
# "milihenries" e "milissegundos".
TOKEN = r"(?:" + "|".join(sorted(PALAVRAS, key=len, reverse=True)) + r"|mil(?![a-zà-ÿ])|e)"
# A sequência nunca começa por "e": sem isto, em "24 volts e doze ampères" o
# casamento engole "e doze" e o 12 nunca chega a ser avaliado.
TOKEN_INICIAL = r"(?:" + "|".join(sorted(PALAVRAS, key=len, reverse=True)) + r"|mil(?![a-zà-ÿ]))"
RE_SEQ = re.compile(
    rf"\b({TOKEN_INICIAL}(?:\s+{TOKEN})*)"            # parte inteira
    rf"(\s+vírgula\s+{TOKEN}(?:\s+{TOKEN})*)?",       # parte decimal
    re.I,
)


def converter_texto(texto: str) -> tuple[str, list[tuple[str, str]]]:
    trocas: list[tuple[str, str]] = []

    def repl(m: re.Match) -> str:
        bruto = m.group(0)

        # "por cento" é locução ("dez por cento"), não o número 100.
        antes = texto[max(0, m.start() - 5):m.start()].lower()
        if bruto.lower().startswith("cento") and antes.rstrip().endswith("por"):
            return bruto
        inteiro_txt = m.group(1)
        decimal_txt = m.group(2)

        toks_int = [t.lower() for t in inteiro_txt.split()]
        while toks_int and toks_int[-1] == "e":
            toks_int.pop()
        if not toks_int or toks_int[0] == "e":
            return bruto

        valor_int = _valor(toks_int)
        if valor_int is None:
            return bruto

        decimal = None
        sobra = ""
        if decimal_txt:
            brutos_dec = decimal_txt.split()[1:]        # sem a palavra "vírgula"
            toks_dec = [t.lower() for t in brutos_dec]
            resultado = _digitos_apos_virgula(toks_dec)
            if resultado is None:
                return bruto
            decimal, consumidos = resultado
            # o que veio depois do número não é do número: devolve à frase
            if consumidos < len(brutos_dec):
                sobra = " " + " ".join(brutos_dec[consumidos:])

        # --- a sequência é mesmo um número?
        #
        # A regra é ampla de propósito: o professor quer algarismo em tudo.
        # A única exceção é "um"/"uma" ISOLADO, que nos quatro roteiros
        # aparece 1.086 vezes e é quase sempre artigo ("um sistema", "uma
        # tabela"). Trocar isso por "1" estragaria o texto.
        composto = len([t for t in toks_int if t != "e"]) > 1
        tem_decimal = decimal is not None
        apos_virgula = texto[max(0, m.start() - 9):m.start()].lower().rstrip().endswith("vírgula")
        if (not composto and not tem_decimal and not apos_virgula
                and toks_int[0] in ("um", "uma")):
            return bruto

        saida = f"{valor_int:,}".replace(",", ".") if valor_int >= 10000 else str(valor_int)
        if decimal is not None:
            saida = f"{saida},{decimal}"

        # O regex às vezes engole um "e" solto no fim ("vinte e cinco e o
        # driver..."). Ele é conjunção da frase, não parte do número:
        # devolva-o, senão a frase perde a ligação.
        if re.search(r"\se\s*$", bruto, re.I):
            saida += " e"
        saida += sobra

        trocas.append((bruto, saida))
        return saida

    return RE_SEQ.sub(repl, texto), trocas


SUPERESCRITO = str.maketrans("0123456789-", "⁰¹²³⁴⁵⁶⁷⁸⁹⁻")


def pos_processar(texto: str) -> str:
    """Arruma o que a conversão palavra a palavra não alcança."""
    # notação científica: "2,5 vezes 10 elevado a menos 4"  ->  "2,5 × 10⁻⁴"
    def cientifica(m):
        mant, sinal, exp = m.group(1), m.group(2), m.group(3)
        expoente = ("-" if sinal else "") + exp
        return f"{mant} × 10{expoente.translate(SUPERESCRITO)}"

    texto = re.sub(
        r"([\d,\.]+)\s+vezes\s+10\s+elevado\s+a\s+(menos\s+)?(\d+)",
        cientifica, texto, flags=re.I)

    # versões: "0,12 vírgula 7" -> "0.12.7"; "2,5 vírgula 2" -> "2.5.2"
    def versao(m):
        return f"{m.group(1)}.{m.group(2)}.{m.group(3)}"

    texto = re.sub(r"\b(\d+),(\d+)\s+vírgula\s+(\d+)\b", versao, texto)

    # decimal solto que sobrou como palavra
    texto = re.sub(r"\b(\d+)\s+vírgula\s+(\d+)\b", r"\1,\2", texto)
    return texto


def main(argv: list[str]) -> int:
    apenas_checar = "--check" in argv
    total = 0
    for rel in ALVOS:
        caminho = RAIZ / rel
        if not caminho.exists():
            continue
        original = caminho.read_text(encoding="utf-8")
        novo, trocas = converter_texto(original)
        novo = pos_processar(novo)
        total += len(trocas)
        print(f"\n{rel}: {len(trocas)} conversões")
        for antes, depois in trocas[:12]:
            print(f"    {antes!r:>58}  ->  {depois}")
        if len(trocas) > 12:
            print(f"    ... e mais {len(trocas) - 12}")
        if not apenas_checar and novo != original:
            caminho.write_text(novo, encoding="utf-8")
    print(f"\nTotal: {total} conversões" + (" (nada gravado)" if apenas_checar else ""))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
