"""Valida os decks HTML de Red Team & Blue Team Strategies.

Uso (a partir da raiz da disciplina):  python scripts/validar_slides.py [aulaN ...]
Verifica, em cada unidade_N/slides/aulaK.html:
- estrutura (deck, capa, audiodescrição só na aula0, encerramento, assets compartilhados);
- laboratórios: pelo menos 4 chamadas Labs.*, com pelo menos um VS Code, uma
  simulação de programa (terminal, SIEM, navegador ou laboratório próprio) e uma
  visualização (fluxo animado ou cena 3D); todo alvo '#id' existe no HTML;
- sintaxe dos <script> embutidos (node --check);
- ausência de comandos ofensivos operacionais e de marcadores provisórios.
Sai com código 1 se algo falhar.
"""
from __future__ import annotations

import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DECKS = {0: 1, **{k: (k - 1) // 4 + 1 for k in range(1, 17)}}
ASSETS = ["../../assets/deck.css", "../../assets/labs.css", "../../assets/sprite.js", "../../assets/deck.js", "../../assets/labs.js"]
# padrões quebrados em duas partes para não disparar antivírus ao abrir este arquivo
PARTS = [("seku", "rlsa"), ("invoke-mimi", "katz"), ("msfv", "enom"), ("meter", "preter"), ("nc ", "-e "),
         ("reverse ", "shell"), ("hashcat ", "-m"), ("powershell ", "-enc"), ("lsadump", "::"), ("sqlm", "ap "),
         ("hydra ", "-l"), ("cobalt", "strike beacon"), ("procdump ", "-ma lsass"), ("john ", "--wordlist"),
         ("crackmap", "exec"), ("impacket", "-"), ("rubeus", " "), ("kerbe", "roast")]
OFFENSIVE = re.compile("|".join(re.escape(a + b) for a, b in PARTS), re.I)


def check(k: int) -> list[str]:
    n = DECKS[k]
    path = ROOT / f"unidade_{n}" / "slides" / f"aula{k}.html"
    rel = path.relative_to(ROOT)
    if not path.exists():
        return [f"{rel}: não existe"]
    t = path.read_text(encoding="utf-8")
    p: list[str] = []
    for a in ASSETS:
        if a not in t:
            p.append(f"{rel}: falta referência a {a}")
    if 'id="deck"' not in t:
        p.append(f"{rel}: falta <div class=\"deck\" id=\"deck\">")
    for cls in ("slide-capa", "slide-fim"):
        if cls not in t:
            p.append(f"{rel}: falta slide '{cls}'")
    # Audiodescrição do professor: só na apresentação da disciplina (aula0).
    if k == 0 and "slide-audio" not in t:
        p.append(f"{rel}: aula0 deve ter o slide de audiodescrição (slide-audio)")
    if k != 0 and "slide-audio" in t:
        p.append(f"{rel}: audiodescrição fica só na aula0; remova o slide-audio")
    if k == 0 and "slide-prof" not in t:
        p.append(f"{rel}: aula0 deve ter o slide 'Sobre o professor' (slide-prof)")
    n_slides = len(re.findall(r'<section class="slide[ "]', t))
    if n_slides < 12:
        p.append(f"{rel}: só {n_slides} slides (mínimo 12)")
    calls = re.findall(r"Labs\.(vscode|terminal|siem|browser|flow|scene3d|register|plataforma)\(\s*'#([\w-]+)'", t)
    kinds = {c for c, _ in calls}
    if len(calls) < 4:
        p.append(f"{rel}: {len(calls)} laboratórios (mínimo 4)")
    if "vscode" not in kinds:
        p.append(f"{rel}: nenhum laboratório VS Code")
    # Cada VS Code mostra a preparação do ambiente (setup) antes de rodar, e o deck traz o slide "Antes do código".
    for bloco in re.split(r"(?=Labs\.vscode\(\s*')", t)[1:]:
        alvo = re.match(r"Labs\.vscode\(\s*'#([\w-]+)'", bloco).group(1)
        fim = re.search(r"\n\}\);", bloco)
        if not re.search(r"\bsetup:\s*\[", bloco[: fim.start() if fim else len(bloco)]):
            p.append(f"{rel}: VS Code #{alvo} sem a preparação do ambiente (setup)")
    if "vscode" in kinds and "Antes do código" not in t:
        p.append(f"{rel}: falta o slide 'Antes do código' (onde achar e como instalar) antes do VS Code")
    # Os comentários <!-- N. título --> acompanham o número real do slide.
    for n, m in enumerate(re.finditer(r'(?:<!--\s*(.*?)\s*-->\s*)?<section class="slide[ "]', t, re.S), 1):
        c = m.group(1) or ""
        if not re.match(rf"{n}\.\s", c):
            p.append(f"{rel}: slide {n} sem comentário numerado '<!-- {n}. ... -->' (achei: '{c[:30]}')")
            break
    if not kinds & {"terminal", "siem", "browser", "register"}:
        p.append(f"{rel}: nenhuma simulação de programa (terminal, SIEM, navegador ou laboratório próprio)")
    if "plataforma" not in kinds:
        p.append(f"{rel}: nenhum laboratório na plataforma Rede Tatame (Labs.plataforma)")
    if not kinds & {"flow", "scene3d"}:
        p.append(f"{rel}: nenhuma visualização (fluxo animado ou cena 3D)")
    for _, i in calls:
        if f'id="{i}"' not in t:
            p.append(f"{rel}: alvo #{i} não existe no HTML")
    if re.search(r"\b(TODO|FIXME)\b|lorem ipsum|\[PLACEHOLDER\]", t):
        p.append(f"{rel}: marcador provisório (TODO/lorem/PLACEHOLDER)")
    for m in OFFENSIVE.finditer(t):
        line = t[: m.start()].count("\n") + 1
        p.append(f"{rel}:{line}: comando ofensivo operacional '{m.group(0)}'")
    scripts = re.findall(r"<script>(.*?)</script>", t, flags=re.S)
    for j, s in enumerate(scripts):
        with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as fh:
            fh.write(s)
        r = subprocess.run(["node", "--check", fh.name], capture_output=True, text=True)
        Path(fh.name).unlink(missing_ok=True)
        if r.returncode:
            err = (r.stderr.strip().splitlines() or ["?"])
            msg = next((e for e in err if "Error" in e), err[-1])
            loc = next((e for e in err if e.endswith(".js:" + e.split(":")[-1])), "")
            p.append(f"{rel}: erro de sintaxe no <script> {j + 1}: {msg} {loc}")
    print(f"{rel}: {n_slides} slides, laboratórios {len(calls)} ({', '.join(sorted(kinds))}), {len(t) // 1024} KB")
    return p


def main() -> int:
    want = [int(a.replace("aula", "")) for a in sys.argv[1:]] or sorted(DECKS)
    problems = [x for k in want for x in check(k)]
    print()
    if problems:
        print(f"{len(problems)} problema(s):")
        print("\n".join("  - " + x for x in problems))
        return 1
    print("OK: decks válidos.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
