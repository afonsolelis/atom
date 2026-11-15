"""Valida os arquivos de trabalho de Red Team & Blue Team Strategies contra as regras dos templates do Drive.

Uso (a partir da raiz da disciplina):  python scripts/validar.py
Sai com código 1 se alguma verificação falhar.
"""
from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
problems: list[str] = []
notes: list[str] = []


def fail(msg: str) -> None:
    problems.append(msg)


def words(text: str) -> int:
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    text = re.sub(r"^\[Imagem[^\n]*$", " ", text, flags=re.M)
    return len(re.findall(r"\w+", text))


def sections(text: str, level: int) -> list[tuple[str, str]]:
    marker = "#" * level + " "
    out, title, buf = [], None, []
    for line in text.splitlines():
        if line.startswith(marker) and not line.startswith(marker + "#"):
            if title is not None:
                out.append((title, "\n".join(buf)))
            title, buf = line[len(marker):].strip(), []
        elif title is not None:
            if re.match(r"^#{1,%d} " % (level - 1), line):
                out.append((title, "\n".join(buf)))
                title, buf = None, []
            else:
                buf.append(line)
    if title is not None:
        out.append((title, "\n".join(buf)))
    return out


def check_unit(n: int) -> None:
    path = ROOT / f"unidade_{n}" / f"unidade_{n}.md"
    text = path.read_text(encoding="utf-8")
    rel = path.relative_to(ROOT)
    if "[título" in text or "[título a definir" in text:
        fail(f"{rel}: ainda há títulos provisórios '[título]'")
    h2 = [t for t, _ in sections(text, 2)]
    aulas = [t for t in h2 if t.startswith("Aula ")]
    expected = list(range((n - 1) * 4 + 1, n * 4 + 1))
    got = [int(re.match(r"Aula (\d+)", t).group(1)) for t in aulas]
    if got != expected:
        fail(f"{rel}: aulas {got}, esperado {expected}")
    has_intro = any("atuação profissional" in t for t in h2)
    has_aai = any(t.startswith("AAI") for t in h2)
    if (n == 1) != has_intro:
        fail(f"{rel}: 'Relação com a atuação profissional' deve existir só na Unidade 1")
    if (n == 1) != has_aai:
        fail(f"{rel}: AAI deve existir só na Unidade 1")
    for req in ("Quiz não avaliativo", "Material complementar"):
        if req not in h2:
            fail(f"{rel}: falta a seção '{req}'")
    for sub in ("Direto da fonte", "Para mergulhar no assunto", "Podcast", "Artigo científico"):
        if f"### {sub}" not in text:
            fail(f"{rel}: material complementar sem '{sub}'")
    for title, body in sections(text, 2):
        if not title.startswith("Aula "):
            continue
        num = int(re.match(r"Aula (\d+)", title).group(1))
        pos = num - (n - 1) * 4
        h3 = dict(sections("## x\n" + body, 3))
        base = h3.get("Texto base", "")
        w = words(base)
        imgs = len(re.findall(r"^\[Imagem \d+", base, flags=re.M))
        notes.append(f"{rel} Aula {num}: {w} palavras, {imgs} imagens")
        if not 700 <= w <= 1200:
            fail(f"{rel} Aula {num}: texto base com {w} palavras (faixa 700–1200)")
        if not 3 <= imgs <= 5:
            fail(f"{rel} Aula {num}: {imgs} imagens (template pede 3 a 5)")
        if not any(k.startswith("Roteiro da Videoaula") for k in h3):
            fail(f"{rel} Aula {num}: sem roteiro da videoaula")
        if "Referências da aula" not in h3:
            fail(f"{rel} Aula {num}: sem referências")
        if pos == 1 and "O que você verá nesta unidade" not in h3:
            fail(f"{rel} Aula {num}: falta 'O que você verá nesta unidade'")
        if pos == 3 and "Pausa para reflexão" not in base:
            fail(f"{rel} Aula {num}: falta 'Pausa para reflexão'")
        if pos == 4 and "O que você verá na próxima unidade" not in body:
            fail(f"{rel} Aula {num}: falta 'O que você verá na próxima unidade'")
    left = len(re.findall(r"\[conferir", text))
    if left:
        notes.append(f"{rel}: {left} marcador(es) [conferir] para revisão humana")


AR_ALTS = [
    "As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.",
    "As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.",
    "A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.",
    "A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.",
    "As asserções I e II são proposições falsas.",
]


def check_questions(n: int) -> None:
    path = ROOT / f"unidade_{n}" / f"questoes_uni{n}.md"
    text = path.read_text(encoding="utf-8")
    rel = path.relative_to(ROOT)
    if "## Gabarito e feedbacks" not in text:
        fail(f"{rel}: falta '## Gabarito e feedbacks'")
        return
    qpart, fpart = text.split("## Gabarito e feedbacks", 1)
    blocks = re.split(r"^\*\*(\d+)\.\*\*", qpart, flags=re.M)[1:]
    qs = {int(blocks[i]): blocks[i + 1] for i in range(0, len(blocks), 2)}
    if sorted(qs) != list(range(1, 41)):
        fail(f"{rel}: questões numeradas {sorted(qs)[:3]}…, esperado 1–40 ({len(qs)} encontradas)")
    letters = Counter()
    answer = {}
    for k, body in qs.items():
        alts = re.findall(r"^(\*?)([a-e])\. (.+)$", body, flags=re.M)
        if [a[1] for a in alts] != list("abcde"):
            fail(f"{rel} Q{k}: alternativas {[a[1] for a in alts]}")
            continue
        stars = [a[1] for a in alts if a[0]]
        if len(stars) != 1:
            fail(f"{rel} Q{k}: {len(stars)} alternativas marcadas com *")
            continue
        answer[k] = stars[0]
        letters[stars[0]] += 1
        if k <= 20:
            if "PORQUE" not in body:
                fail(f"{rel} Q{k}: asserção-razão sem 'PORQUE'")
            if [a[2].strip() for a in alts] != AR_ALTS:
                fail(f"{rel} Q{k}: alternativas de asserção-razão fora do padrão")
    if any(letters[c] != 8 for c in "abcde"):
        fail(f"{rel}: distribuição de corretas {dict(sorted(letters.items()))} (esperado 8 por letra)")
    fb = re.split(r"^\*\*Questão (\d+)\*\* \(correta: ([a-e])\)", fpart, flags=re.M)[1:]
    fbs = {int(fb[i]): (fb[i + 1], fb[i + 2]) for i in range(0, len(fb), 3)}
    if sorted(fbs) != list(range(1, 41)):
        fail(f"{rel}: feedbacks para {len(fbs)} questões (esperado 40)")
    for k, (letter, body) in fbs.items():
        if answer.get(k) and answer[k] != letter:
            fail(f"{rel} Q{k}: gabarito '{letter}' difere da alternativa marcada '{answer[k]}'")
        bullets = re.findall(r"^- ([a-e])\. (Correta|Incorreta)", body, flags=re.M)
        if [b[0] for b in bullets] != list("abcde"):
            fail(f"{rel} Q{k}: feedback sem as 5 alternativas")
        elif [b[0] for b in bullets if b[1] == "Correta"] != [letter]:
            fail(f"{rel} Q{k}: feedback marca como correta {[b[0] for b in bullets if b[1] == 'Correta']}, gabarito {letter}")
    notes.append(f"{rel}: {len(qs)} questões, corretas {dict(sorted(letters.items()))}")


def check_final() -> None:
    path = ROOT / "instrumentos_avaliativos" / "avaliacao_final.md"
    text = path.read_text(encoding="utf-8")
    rel = path.relative_to(ROOT)
    q = len(re.findall(r"^### Questão \d+", text, flags=re.M))
    if q != 20:  # 10 enunciados + 10 respostas esperadas
        fail(f"{rel}: {q} cabeçalhos '### Questão N' (esperado 10 enunciados + 10 feedbacks)")


def check_pbl() -> None:
    path = ROOT / "instrumentos_avaliativos" / "entrega_trabalho.md"
    text = path.read_text(encoding="utf-8")
    rel = path.relative_to(ROOT)
    for sec in ("Título", "Desafio", "Fonte de pesquisa", "Entregável e distribuição da pontuação", "Solução"):
        if not re.search(rf"^## {sec}", text, flags=re.M):
            fail(f"{rel}: falta a seção '{sec}'")
    sec = text.split("## Entregável e distribuição da pontuação", 1)[-1].split("\n## ", 1)[0]
    pct = [int(p) for p in re.findall(r"\|\s*\**(\d{1,3})%\**\s*\|\s*$", sec, flags=re.M)]
    total = sum(pct) - (100 if pct and pct[-1] == 100 else 0)
    notes.append(f"{rel}: pesos {pct[:-1] if pct and pct[-1] == 100 else pct} (soma {total}%)")
    if total != 100:
        fail(f"{rel}: pesos da pontuação somam {total}%")


def main() -> int:
    for n in range(1, 5):
        check_unit(n)
        check_questions(n)
    check_pbl()
    check_final()
    for md in ROOT.rglob("*.md"):
        if "documentos" in md.parts:
            continue
        t = md.read_text(encoding="utf-8")
        if "\r\n" in t:
            fail(f"{md.relative_to(ROOT)}: quebras de linha CRLF")
    print("\n".join(notes))
    print()
    if problems:
        print(f"{len(problems)} problema(s):")
        print("\n".join(f"  - {p}" for p in problems))
        return 1
    print("OK: todas as verificações passaram.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
