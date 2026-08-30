#!/usr/bin/env python3
"""Valida o material da disciplina contra as regras de `DIRETRIZES_PRODUCAO.md`.

Executa uma bateria de verificações estruturais e quantitativas sobre os
arquivos Markdown da disciplina e devolve um relatório com falhas (bloqueiam a
entrega) e avisos (exigem revisão humana).

Uso:
    tools/.venv/bin/python tools/validar.py
    tools/.venv/bin/python tools/validar.py --detalhe
"""

from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent

FALHAS: list[str] = []
AVISOS: list[str] = []
OKS: list[str] = []


def falha(msg: str) -> None:
    FALHAS.append(msg)


def aviso(msg: str) -> None:
    AVISOS.append(msg)


def ok(msg: str) -> None:
    OKS.append(msg)


# ---------------------------------------------------------------- utilidades

def ler(rel: str) -> str | None:
    p = RAIZ / rel
    if not p.exists():
        falha(f"{rel}: arquivo ausente")
        return None
    return p.read_text(encoding="utf-8")


def sem_codigo(texto: str) -> str:
    """Remove blocos e trechos de código."""
    texto = re.sub(r"```.*?```", " ", texto, flags=re.S)
    return re.sub(r"`[^`\n]*`", " ", texto)


def contar_palavras(texto: str) -> int:
    return len(re.findall(r"\b[\wÀ-ÿ]+\b", texto))


CABECALHO_PARTE_B = re.compile(r"^# Parte B\b", re.M)


def dividir_partes(texto: str) -> tuple[str, str] | None:
    """Divide o arquivo-mestre no cabeçalho real da Parte B.

    A divisão precisa casar o cabeçalho em início de linha: a expressão
    "# Parte B" também aparece dentro de crases no bloco de controle de versão,
    no topo do arquivo, e uma busca literal cortaria o documento ali.
    """
    m = CABECALHO_PARTE_B.search(texto)
    if not m:
        return None
    return texto[: m.start()], texto[m.end():]


def secoes(texto: str, nivel: int) -> list[tuple[str, str]]:
    """Divide o texto pelas seções de um dado nível de cabeçalho."""
    marca = "#" * nivel
    padrao = re.compile(rf"^{marca} (?!#)(.+)$", re.M)
    ms = list(padrao.finditer(texto))
    saida = []
    for i, m in enumerate(ms):
        fim = ms[i + 1].start() if i + 1 < len(ms) else len(texto)
        saida.append((m.group(1).strip(), texto[m.end():fim]))
    return saida


# ------------------------------------------------------- unidades escritas

def validar_unidade(n: int) -> None:
    rel = f"unidade_{n}/unidade_{n}.md"
    txt = ler(rel)
    if txt is None:
        return

    aulas = secoes(txt, 2)
    aulas_conteudo = [(t, c) for t, c in aulas if re.match(r"^Aula \d+", t)]

    if len(aulas_conteudo) != 4:
        falha(f"{rel}: esperadas 4 aulas, encontradas {len(aulas_conteudo)}")
    else:
        ok(f"{rel}: 4 aulas presentes")

    esperadas = [(n - 1) * 4 + i for i in range(1, 5)]
    numeros = [int(re.match(r"^Aula (\d+)", t).group(1)) for t, _ in aulas_conteudo]
    if numeros != esperadas:
        falha(f"{rel}: numeração das aulas {numeros}, esperada {esperadas}")

    for idx, (titulo, corpo) in enumerate(aulas_conteudo, start=1):
        rotulo = f"{rel} / {titulo[:40]}"
        limpo = sem_codigo(corpo)

        # o texto base exclui laboratório, síntese, referências e remissões
        base = limpo
        for cortar in ("### Laboratório da aula", "### Síntese da aula",
                       "### Referências da aula", "### Roteiro da Videoaula"):
            pos = base.find(cortar)
            if pos != -1:
                base = base[:pos] + re.sub(r"^.*?(?=\n### )", "", base[pos:], flags=re.S)
        palavras = contar_palavras(base)
        if not 650 <= palavras <= 1400:
            aviso(f"{rotulo}: texto base com {palavras} palavras (alvo 700 a 1.200)")
        else:
            ok(f"{rotulo}: {palavras} palavras")

        n_rv = len(re.findall(r"^> \*\*Recurso visual \d+", corpo, re.M))
        if not 3 <= n_rv <= 5:
            falha(f"{rotulo}: {n_rv} recursos visuais (exigidos 3 a 5)")
        n_alt = len(re.findall(r"\*Texto alternativo:\*", corpo))
        if n_alt != n_rv:
            falha(f"{rotulo}: {n_rv} recursos visuais mas {n_alt} textos alternativos")

        for obrig in ("### Situação-problema", "### Atividade prática",
                      "### Síntese da aula", "### Referências da aula"):
            if obrig not in corpo:
                falha(f"{rotulo}: falta a seção '{obrig}'")

        if idx == 3 and "### Pausa para reflexão" not in corpo:
            falha(f"{rotulo}: a terceira aula da unidade exige 'Pausa para reflexão'")
        if idx == 4:
            if n < 4 and f"### Transição para a Unidade {n + 1}" not in corpo:
                falha(f"{rotulo}: falta 'Transição para a Unidade {n + 1}'")
            if n == 4 and "### Fechamento da disciplina" not in corpo:
                falha(f"{rotulo}: a Aula 16 exige 'Fechamento da disciplina'")

    # blocos de fim de unidade
    for obrig in ("### Quiz não avaliativo", "### Síntese da unidade",
                  "### Material complementar"):
        if obrig not in txt:
            falha(f"{rel}: falta '{obrig}'")

    tem_aai = "### Atividade Avaliativa Individual" in txt
    if n == 1 and not tem_aai:
        falha(f"{rel}: a Unidade 1 exige a Atividade Avaliativa Individual")
    if n != 1 and tem_aai:
        falha(f"{rel}: AAI só pode existir na Unidade 1")

    for sec in ("#### Direto da Fonte", "#### Para Mergulhar",
                "#### Podcast", "#### Artigo científico"):
        if sec not in txt:
            falha(f"{rel}: falta a seção de material complementar '{sec}'")
    if "#### Podcast" in txt:
        bloco = txt.split("#### Podcast", 1)[1].split("####", 1)[0]
        if "youtube.com" not in bloco and "youtu.be" not in bloco:
            falha(f"{rel}: a seção Podcast precisa apontar para o YouTube")

    quiz = txt.split("### Quiz não avaliativo", 1)[-1].split("###", 1)[0] if \
        "### Quiz não avaliativo" in txt else ""
    n_quiz = len(re.findall(r"^\*\*Questão \d+", quiz, re.M))
    if n_quiz != 2:
        falha(f"{rel}: quiz com {n_quiz} questões (exigidas 2)")
    if quiz.count("*Feedback conceitual:*") != 2:
        falha(f"{rel}: quiz sem devolutiva conceitual nas duas questões")

    verificar_latex(rel, txt)


# ------------------------------------------------------------- questionários

def validar_questoes(n: int) -> None:
    rel = f"unidade_{n}/questoes_uni{n}.md"
    txt = ler(rel)
    if txt is None:
        return

    corpo = txt.split("## Gabarito", 1)[0]
    questoes = re.split(r"^\*\*(\d+)\.\*\*", corpo, flags=re.M)[1:]
    pares = list(zip(questoes[0::2], questoes[1::2]))

    if len(pares) != 40:
        falha(f"{rel}: {len(pares)} questões (exigidas 40)")
    else:
        ok(f"{rel}: 40 questões")

    numeros = [int(a) for a, _ in pares]
    if numeros != list(range(1, len(pares) + 1)):
        falha(f"{rel}: numeração das questões fora de sequência")

    letras: dict[str, int] = {}
    for num, texto in pares:
        alts = re.findall(r"^\*?([a-e])\. ", texto, re.M)
        if len(alts) != 5:
            falha(f"{rel} Q{num}: {len(alts)} alternativas (exigidas 5)")
        if alts and alts != ["a", "b", "c", "d", "e"]:
            falha(f"{rel} Q{num}: alternativas fora da ordem a-e ({alts})")
        corretas = re.findall(r"^\*([a-e])\. ", texto, re.M)
        if len(corretas) != 1:
            falha(f"{rel} Q{num}: {len(corretas)} alternativas marcadas com '*' (exigida 1)")
        else:
            letras[corretas[0]] = letras.get(corretas[0], 0) + 1

    if len(pares) == 40:
        desbalanceadas = {k: v for k, v in letras.items() if v != 8}
        if desbalanceadas or len(letras) != 5:
            aviso(f"{rel}: distribuição da letra correta {dict(sorted(letras.items()))} "
                  "(alvo: 8 por letra)")
        else:
            ok(f"{rel}: distribuição equilibrada, 8 por letra")

    # tipologia: 20 asserção-razão + 20 interpretação
    n_ar = len(re.findall(r"^PORQUE$", corpo, re.M))
    if n_ar != 20:
        falha(f"{rel}: {n_ar} questões de asserção-razão (exigidas 20)")

    # devolutivas: uma por alternativa das 40 questões
    gab = txt.split("## Gabarito", 1)[1] if "## Gabarito" in txt else ""
    if not gab:
        falha(f"{rel}: falta a seção de gabarito e devolutivas")
    else:
        blocos = re.findall(r"^\*\*Questão (\d+)\*\*", gab, re.M)
        if len(blocos) != len(pares):
            falha(f"{rel}: {len(blocos)} blocos de devolutiva para {len(pares)} questões")
        n_dev = len(re.findall(r"^- [a-e]\. ", gab, re.M))
        if n_dev != 5 * len(pares):
            falha(f"{rel}: {n_dev} devolutivas de alternativa "
                  f"(exigidas {5 * len(pares)}, uma por alternativa)")
        else:
            ok(f"{rel}: devolutiva para todas as {n_dev} alternativas")

        # A letra declarada no gabarito precisa ser a mesma marcada com '*' no
        # enunciado, e a devolutiva dessa letra precisa começar por "Correta".
        # Um gabarito que diverge do enunciado leva o estudante a estudar pela
        # resposta errada, então isto é falha, não aviso.
        declaradas = dict(re.findall(r"^\*\*Questão (\d+)\*\* \(correta: ([a-e])\)", gab, re.M))
        marcadas = {}
        for num, texto in pares:
            corretas = re.findall(r"^\*([a-e])\. ", texto, re.M)
            if len(corretas) == 1:
                marcadas[num] = corretas[0]
        for num, letra in sorted(marcadas.items(), key=lambda kv: int(kv[0])):
            decl = declaradas.get(num)
            if decl is None:
                falha(f"{rel} Q{num}: sem cabeçalho '(correta: X)' no gabarito")
            elif decl != letra:
                falha(f"{rel} Q{num}: enunciado marca '{letra}' mas o gabarito "
                      f"declara '{decl}'")

        blocos_gab = re.split(r"^\*\*Questão (\d+)\*\*[^\n]*$", gab, flags=re.M)[1:]
        for num, corpo in zip(blocos_gab[0::2], blocos_gab[1::2]):
            letra = marcadas.get(num)
            if not letra:
                continue
            linha = re.search(rf"^- {letra}\. (\w+)", corpo, re.M)
            if linha and not linha.group(1).lower().startswith("correta"):
                falha(f"{rel} Q{num}: a devolutiva da alternativa '{letra}' "
                      f"não começa por 'Correta'")

    verificar_latex(rel, txt)


# ------------------------------------------------------------------ roteiros

MARCA_TEMPO = re.compile(r"\*\*\[(\d{2}):(\d{2})[–-](\d{2}):(\d{2})[^\]]*\]\*\*")


def validar_roteiros(n: int) -> None:
    rel = f"unidade_{n}/roteiros_20min.md"
    txt = ler(rel)
    if txt is None:
        return

    roteiros = [(t, c) for t, c in secoes(txt, 2)
                if t.lower().startswith("roteiro da videoaula")]
    if len(roteiros) != 4:
        falha(f"{rel}: {len(roteiros)} roteiros (exigidos 4)")
    else:
        ok(f"{rel}: 4 roteiros")

    for titulo, corpo in roteiros:
        rotulo = f"{rel} / {titulo[:45]}"

        # narração: exclui código, marcações, indicações de edição e as seções finais
        narr = corpo
        for sec in ("### Indicações de edição", "### Fontes e links de mídia",
                    "### Fontes e licenças"):
            narr = narr.split(sec, 1)[0]
        narr = sem_codigo(narr)
        narr = MARCA_TEMPO.sub(" ", narr)
        narr = re.sub(r"^\*\*.*?\*\*\s*$", " ", narr, flags=re.M)   # linhas de marcação
        narr = re.sub(r"\*\[[^\]]*\]\*", " ", narr)                  # indicações de edição
        narr = re.sub(r"^#{1,6} .*$", " ", narr, flags=re.M)         # cabeçalhos
        narr = re.sub(r"^\s*[-*] .*$", " ", narr, flags=re.M)        # listas de apoio
        palavras = contar_palavras(narr)
        if not 2000 <= palavras <= 3000:
            aviso(f"{rotulo}: {palavras} palavras de narração (alvo 2.200 a 2.700)")
        else:
            ok(f"{rotulo}: {palavras} palavras de narração")

        marcas = MARCA_TEMPO.findall(corpo)
        if len(marcas) < 10:
            aviso(f"{rotulo}: apenas {len(marcas)} marcações de tempo")
        if marcas:
            segs = [(int(a) * 60 + int(b), int(c) * 60 + int(d)) for a, b, c, d in marcas]
            if segs[0][0] != 0:
                falha(f"{rotulo}: a primeira marcação não começa em 00:00")
            fim = segs[-1][1]
            if not 1140 <= fim <= 1260:  # 19:00 a 21:00
                falha(f"{rotulo}: termina em {fim // 60:02d}:{fim % 60:02d} (alvo 20:00)")
            for i in range(1, len(segs)):
                if segs[i][0] < segs[i - 1][0]:
                    falha(f"{rotulo}: marcações de tempo fora de ordem "
                          f"em {segs[i][0] // 60:02d}:{segs[i][0] % 60:02d}")
                    break

        for obrig in ("**Objetivo da videoaula", "### Indicações de edição"):
            if obrig not in corpo:
                falha(f"{rotulo}: falta '{obrig}'")

    verificar_latex(rel, txt)


# ------------------------------------------------------ instrumentos e LaTeX

def validar_avaliacao() -> None:
    rel = "instrumentos_avaliativos/avaliacao_dissertativa.md"
    txt = ler(rel)
    if txt is None:
        return

    partes = dividir_partes(txt)
    if partes is None:
        falha(f"{rel}: exige separação explícita entre Parte A e Parte B")
        return

    parte_a, parte_b = partes
    n_q = len(re.findall(r"^### Questão \d+", parte_a, re.M))
    if n_q != 10:
        falha(f"{rel}: {n_q} questões dissertativas na Parte A (exigidas 10)")
    else:
        ok(f"{rel}: 10 questões dissertativas")

    vazados = [m for m in ("Resposta esperada", "Critérios de correção", "Rubrica",
                           "Gabarito") if m in parte_a]
    if vazados:
        falha(f"{rel}: conteúdo de tutor na Parte A: {vazados}")
    else:
        ok(f"{rel}: Parte A sem respostas ou rubricas")

    n_resp = len(re.findall(r"^### Questão \d+", parte_b, re.M))
    if n_resp != n_q:
        falha(f"{rel}: {n_resp} blocos de resposta para {n_q} questões")

    for titulo, corpo in secoes(parte_b, 3):
        if not titulo.startswith("Questão"):
            continue
        pontos = [int(x) for x in re.findall(r"\*\*0 a (\d+) pontos?", corpo)]
        if sum(pontos) != 10:
            falha(f"{rel} / {titulo}: rubrica soma {sum(pontos)} pontos, esperado 10")

    verificar_latex(rel, txt)


def validar_pbl() -> None:
    """Entrega de trabalho no layout Átomo 3.0, o mesmo de
    `disciplinas/portos_aeroportos_e_ferrovias/`: documento único, com a
    caixa `## 5. Solução` posicionada antes do `## Roteiro do Estudante` e
    marcada para remoção na cópia do estudante."""
    rel = "instrumentos_avaliativos/entrega_trabalho.md"
    txt = ler(rel)
    if txt is None:
        return

    obrigatorias = ("## 1. Título", "## 2. Desafio", "## 3. Fontes de pesquisa",
                    "## 4. Entregável e distribuição da pontuação",
                    "## 5. Solução", "## Roteiro do Estudante")
    faltando = [s for s in obrigatorias if s not in txt]
    if faltando:
        falha(f"{rel}: faltam as seções {faltando}")
    else:
        ok(f"{rel}: as 6 seções do modelo Átomo 3.0 presentes")

    if "## 5. Solução" in txt and "## Roteiro do Estudante" in txt:
        if txt.index("## 5. Solução") > txt.index("## Roteiro do Estudante"):
            falha(f"{rel}: '5. Solução' precisa vir antes do 'Roteiro do Estudante'")
        else:
            ok(f"{rel}: ordem das seções conforme o modelo")

    fontes = txt.split("## 3. Fontes de pesquisa", 1)[-1].split("## 4.", 1)[0]
    n_fontes = len(re.findall(r"^\d+\. ", fontes, re.M))
    if n_fontes < 4:
        falha(f"{rel}: {n_fontes} fontes de pesquisa (exigidas ao menos 4)")
    else:
        ok(f"{rel}: {n_fontes} fontes de pesquisa")

    solucao = txt.split("## 5. Solução", 1)[-1].split("## Roteiro do Estudante", 1)[0]
    if "será removido antes" not in solucao:
        falha(f"{rel}: a seção '5. Solução' precisa do aviso de remoção antes da entrega ao aluno")
    else:
        ok(f"{rel}: seção '5. Solução' marcada para remoção na cópia do estudante")

    verificar_latex(rel, txt)


def validar_avaliacao_final() -> None:
    """Avaliação final no padrão Átomo 3.0 (o mesmo de portos_aeroportos_e_ferrovias):
    40 questões — 15 asserção-razão, 15 de interpretação e 10 discursivas —
    com feedback para todas as 5 alternativas das 30 objetivas."""
    rel = "instrumentos_avaliativos/avaliacao_final.md"
    txt = ler(rel)
    if txt is None:
        return

    if "## Feedbacks" not in txt:
        falha(f"{rel}: seção '## Feedbacks' ausente")
        return
    corpo, fb = txt.split("## Feedbacks", 1)

    tipos = re.findall(r"^### Questão (\d+) \((Asserção-Razão|Interpretação|Discursiva)\)",
                       corpo, re.M)
    contagem = {k: sum(1 for _, x in tipos if x == k)
                for k in ("Asserção-Razão", "Interpretação", "Discursiva")}
    esperado = {"Asserção-Razão": 15, "Interpretação": 15, "Discursiva": 10}
    if contagem != esperado:
        falha(f"{rel}: tipologia {contagem} (exigido {esperado})")
    else:
        ok(f"{rel}: 40 questões — 15 asserção-razão + 15 interpretação + 10 discursivas")

    gabarito = {}
    for m in re.finditer(r"^### Questão (\d+) \((?:Asserção-Razão|Interpretação)\)(.*?)"
                         r"(?=^### |\Z)", corpo, re.M | re.S):
        marcadas = re.findall(r"^\*([a-e])\.", m.group(2), re.M)
        if len(marcadas) != 1:
            falha(f"{rel}: questão {m.group(1)} com {len(marcadas)} alternativas marcadas com '*'")
        else:
            gabarito[int(m.group(1))] = marcadas[0]

    seq = "".join(gabarito[k] for k in sorted(gabarito))
    if seq != "abcde" * 6:
        falha(f"{rel}: rotação do gabarito fora do padrão a,b,c,d,e — obtida '{seq}'")
    else:
        ok(f"{rel}: gabarito com rotação a–e e 6 questões por letra")

    blocos = dict(re.findall(r"^### Questão (\d+)\s*\n(.*?)(?=^### |\Z)", fb, re.M | re.S))
    if len(blocos) != 30:
        falha(f"{rel}: {len(blocos)} blocos de feedback (exigidos 30)")
    n_alt = len(re.findall(r"^- \*\*[a-e]\.\*\*", fb, re.M))
    if n_alt != 150:
        falha(f"{rel}: {n_alt} alternativas com feedback (exigidas 150)")
    else:
        ok(f"{rel}: feedback para as 150 alternativas das 30 objetivas")

    divergentes = []
    for num, corpo_fb in blocos.items():
        marcada = re.findall(r"^- \*\*([a-e])\.\*\* \*Correta!\*", corpo_fb, re.M)
        if len(marcada) != 1 or marcada[0] != gabarito.get(int(num)):
            divergentes.append(num)
    if divergentes:
        falha(f"{rel}: feedback divergente do gabarito nas questões {divergentes}")
    else:
        ok(f"{rel}: feedback e gabarito coerentes nas 30 objetivas")

    for m in re.finditer(r"^### Questão (\d+) \(Discursiva\)(.*?)(?=^### |\Z)",
                         corpo, re.M | re.S):
        for campo in ("**Contexto:**", "**Enunciado:**", "**Resposta esperada:**"):
            if campo not in m.group(2):
                falha(f"{rel}: discursiva {m.group(1)} sem o campo '{campo}'")
    n_resp = len(re.findall(r"\*\*Resposta esperada:\*\*", corpo))
    if n_resp == 10:
        ok(f"{rel}: as 10 discursivas com contexto, enunciado e resposta esperada")

    verificar_latex(rel, txt)


def verificar_latex(rel: str, txt: str) -> None:
    """Matemática nunca pode estar dentro de cerca de código."""
    for bloco in re.findall(r"```(?!\w*\n?\$)([^\n]*)\n(.*?)```", txt, re.S):
        linguagem, conteudo = bloco
        if linguagem.strip() in ("", "text", "txt") and re.search(r"\\frac|\\begin\{[bp]matrix\}", conteudo):
            aviso(f"{rel}: possível LaTeX dentro de cerca de código")
            break
    abertos = txt.count("$") - len(re.findall(r"\\\$", txt))
    if abertos % 2 != 0:
        aviso(f"{rel}: número ímpar de delimitadores '$' ({abertos}) — verifique fórmulas")
    if re.search(r"^\$\$", txt, re.M):
        falha(f"{rel}: usa '$$' em bloco; o padrão do repositório exige '$' isolado")


def validar_laboratorio() -> None:
    """Confere se os laboratórios referenciados existem e têm README."""
    base = RAIZ / "projeto_nexabot"
    if not base.exists():
        falha("projeto_nexabot/: diretório ausente")
        return
    for i in range(1, 17):
        d = base / f"aula_{i:02d}"
        if not d.exists():
            falha(f"projeto_nexabot/aula_{i:02d}/: ausente")
            continue
        scripts = sorted(d.glob("*.py"))
        if not scripts:
            falha(f"projeto_nexabot/aula_{i:02d}/: sem scripts Python")
        if not (d / "README.md").exists():
            falha(f"projeto_nexabot/aula_{i:02d}/: sem README.md")
        if scripts and not any("desafio" in s.name for s in scripts):
            aviso(f"projeto_nexabot/aula_{i:02d}/: sem script de desafio")
    ok("projeto_nexabot/: laboratórios das 16 aulas conferidos")
    validar_referencias_de_script(base)


REF_SCRIPT = re.compile(r"aula_(\d{2})/(\w+\.py)")
REF_BASENAME = re.compile(r"`((?:\d{2}|[a-z][a-z0-9_]*)_[a-zA-Z0-9_]+\.py)`")


def validar_referencias_de_script(base: Path) -> None:
    """Todo script citado no material escrito precisa existir no laboratório.

    Um roteiro que manda o professor executar um arquivo inexistente quebra a
    gravação, então esta é uma falha, não um aviso.
    """
    fontes = sorted(RAIZ.glob("unidade_*/*.md")) + \
        sorted(RAIZ.glob("instrumentos_avaliativos/*.md"))
    total, quebradas = 0, 0
    for fonte in fontes:
        texto = fonte.read_text(encoding="utf-8")
        for aula, script in set(REF_SCRIPT.findall(texto)):
            total += 1
            if not (base / f"aula_{aula}" / script).exists():
                quebradas += 1
                falha(f"{fonte.relative_to(RAIZ)}: referencia "
                      f"aula_{aula}/{script}, que não existe no laboratório")
        disponiveis = {p.name for p in base.rglob("*.py") if ".venv" not in p.parts}
        for script in set(REF_BASENAME.findall(texto)):
            total += 1
            if script not in disponiveis:
                quebradas += 1
                falha(f"{fonte.relative_to(RAIZ)}: cita `{script}`, que não existe no laboratório")
    if total and not quebradas:
        ok(f"referências de script: {total} citações, todas existentes")


class _ContadorSlides(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.secoes = 0
        self.classes: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "section":
            return
        classes = dict(attrs).get("class") or ""
        if "slide" in classes.split():
            self.secoes += 1
            self.classes.update(classes.split())


def validar_slides() -> None:
    for aula in range(1, 17):
        unidade = (aula - 1) // 4 + 1
        rel = f"unidade_{unidade}/slides/aula{aula}.html"
        txt = ler(rel)
        if txt is None:
            continue
        parser = _ContadorSlides()
        parser.feed(txt)
        if parser.secoes < 8:
            falha(f"{rel}: apenas {parser.secoes} slides (mínimo 8)")
        for classe in ("slide-capa", "slide-fim"):
            if classe not in parser.classes:
                falha(f"{rel}: falta slide obrigatório da classe '{classe}'")
        # "Sobre o professor" não é obrigatório em todo deck. A convenção do
        # repositório, conferida nas três disciplinas já migradas
        # (data_engineering, industria_4_0, portos), é 1 de 17 decks: apenas o
        # aula0. A auditoria específica dos decks está em tools/validar_slides.py.
        if "slide-prof" in parser.classes and not rel.endswith("aula0.html"):
            falha(f"{rel}: traz 'Sobre o professor', que pela convenção do "
                  "repositório aparece apenas no aula0")
        if "Audiodescrição" not in txt:
            falha(f"{rel}: falta slide de Audiodescrição")
        if not re.search(rf"<title>Aula {aula}\b", txt):
            falha(f"{rel}: título HTML não corresponde à Aula {aula}")
        if re.search(r"MathJax|\\\(|\\\[|\$\$", txt):
            falha(f"{rel}: contém MathJax ou LaTeX cru")
        ok(f"{rel}: {parser.secoes} slides, estrutura acessível conferida")


def validar_introducao() -> None:
    rel = "roteiro_video_introdutorio.md"
    txt = ler(rel)
    if txt is None:
        return
    narr = txt.split("## Narração", 1)[-1].split("## Indicações de edição", 1)[0]
    narr = MARCA_TEMPO.sub(" ", sem_codigo(narr))
    narr = re.sub(r"^#{1,6} .*$", " ", narr, flags=re.M)
    palavras = contar_palavras(narr)
    if not 150 <= palavras <= 300:
        aviso(f"{rel}: {palavras} palavras (alvo de até 2 minutos)")
    if re.search(r"\[(?:preencher|inserir|completar)|\bTODO\b|\bXX+\b", txt, re.I):
        falha(f"{rel}: contém marcador pessoal não preenchido")
    else:
        ok(f"{rel}: sem marcadores pendentes")


# ---------------------------------------------------------------------- main

def main(argv: list[str]) -> int:
    detalhe = "--detalhe" in argv

    for doc in ("PLANO_APRENDIZAGEM_PROPOSTO.md", "DIRETRIZES_PRODUCAO.md",
                "ANALISE_MATERIAIS_RECEBIDOS.md", "AMBIENTE_E_STACK.md",
                "CRONOGRAMA.md", "roteiro_video_introdutorio.md"):
        if (RAIZ / doc).exists():
            ok(f"{doc}: presente")
        else:
            falha(f"{doc}: ausente")

    for n in (1, 2, 3, 4):
        validar_unidade(n)
        validar_questoes(n)
        validar_roteiros(n)
    validar_avaliacao()
    validar_avaliacao_final()
    validar_pbl()
    validar_laboratorio()
    validar_introducao()
    validar_slides()

    print("=" * 78)
    print("VALIDAÇÃO — Model-Based Design for Cyber-Physical Systems")
    print("=" * 78)
    if detalhe:
        print(f"\nAPROVADOS ({len(OKS)}):")
        for m in OKS:
            print(f"  [ok]     {m}")
    if AVISOS:
        print(f"\nAVISOS ({len(AVISOS)}) — exigem revisão humana:")
        for m in AVISOS:
            print(f"  [aviso]  {m}")
    if FALHAS:
        print(f"\nFALHAS ({len(FALHAS)}) — bloqueiam a entrega:")
        for m in FALHAS:
            print(f"  [FALHA]  {m}")

    print("\n" + "-" * 78)
    print(f"Aprovados: {len(OKS)}  |  Avisos: {len(AVISOS)}  |  Falhas: {len(FALHAS)}")
    print("-" * 78)
    return 1 if FALHAS else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
