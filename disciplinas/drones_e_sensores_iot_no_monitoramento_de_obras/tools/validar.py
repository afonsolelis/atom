"""Validação estrutural de uma unidade (markdown + decks).

Uso: python tools/validar.py 1        (número da unidade)

Confere: marcadores pendentes, palavras do texto base por aula, subseções,
imagens, pontos-chave, quiz, AAI, material complementar, questões (20, 10 AR +
10 interpretação, 5 alternativas, 1 correta, rotação a–e), roteiros estendidos e
decks (scripts, créditos de foto, sintaxe JS dos <script> inline via node --check).
"""
import pathlib
import re
import subprocess
import sys
import tempfile

sys.stdout.reconfigure(encoding="utf-8")

RAIZ = pathlib.Path(__file__).resolve().parent.parent
u = int(sys.argv[1]) if len(sys.argv) > 1 else 1
d = RAIZ / f"unidade_{u}"
erros, avisos = [], []


def palavras(txt):
    txt = re.sub(r"\$[^$]*\$", " X ", txt)
    txt = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", txt)
    txt = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", txt)
    return len(re.findall(r"\w+", txt))


# ---------- unidade_N.md ----------
md = (d / f"unidade_{u}.md").read_text(encoding="utf-8")
for m in re.finditer(r"_\[A PREENCHER[^\]]*\]_", md):
    erros.append(f"unidade_{u}.md: marcador pendente na linha {md[:m.start()].count(chr(10)) + 1}")
if "```" in md:
    avisos.append(f"unidade_{u}.md: bloco de código encontrado (matemática deve ser LaTeX com $)")
blocos = re.split(r"(?m)^## ", md)
for b in blocos:
    cab = b.split("\n", 1)[0]
    m = re.match(r"Aula (\d+) — (?!Roteiro)", cab)
    if not m:
        continue
    n = m.group(1)
    corpo = b.split("\n", 1)[1]
    texto = re.split(r"(?m)^### (Exemplo numérico|Atividade prática|Pontos-chave|Para saber mais)", corpo)[0]
    w = palavras(texto)
    subs = len(re.findall(r"(?m)^### ", corpo))
    imgs = len(re.findall(r"!\[[^\]]+\]\(https?://", corpo))
    pk = re.search(r"(?ms)^### Pontos-chave\n(.*?)(?=^### |\Z)", corpo)
    npk = len(re.findall(r"(?m)^- ", pk.group(1))) if pk else 0
    psm = re.search(r"(?ms)^### Para saber mais\n(.*?)(?=^### |\Z)", corpo)
    nl = len(re.findall(r"https?://", psm.group(1))) if psm else 0
    total = palavras(corpo)
    print(f"Aula {n}: texto base ~{w} palavras (aula inteira ~{total}), {subs} subseções, {imgs} imagens, {npk} pontos-chave, {nl} links")
    if not 700 <= total <= 1600:
        avisos.append(f"Aula {n}: {total} palavras na aula (alvo 700–1200 de texto base)")
    if not 6 <= subs <= 14:
        avisos.append(f"Aula {n}: {subs} subseções")
    if not 1 <= imgs <= 3:
        erros.append(f"Aula {n}: {imgs} imagens (esperado 1–3)")
    if not 3 <= npk <= 5:
        erros.append(f"Aula {n}: {npk} pontos-chave (esperado 3–5)")
    if not 2 <= nl <= 4:
        erros.append(f"Aula {n}: {nl} links em Para saber mais (esperado 2–4)")
    if "### Exemplo numérico" not in corpo:
        erros.append(f"Aula {n}: sem Exemplo numérico")
    if int(n) % 4 == 3 and "Pausa para reflexão" not in corpo:
        erros.append(f"Aula {n}: Aula 3 da unidade sem Pausa para reflexão")
for sec in ["## Quiz não avaliativo", "## Atividade Verificadora", "## Material complementar", "### Para mergulhar", "### Podcast", "### Artigo científico"]:
    if sec not in md:
        erros.append(f"unidade_{u}.md: falta seção '{sec}'")
rot = len(re.findall(r"(?m)^## Aula \d+ — Roteiro da Videoaula", md))
if rot != 4:
    erros.append(f"unidade_{u}.md: {rot} roteiros de videoaula (esperado 4)")
pod = re.search(r"(?ms)^### Podcast.*?(?=^### |\Z)", md)
if pod and "youtube.com" not in pod.group(0) and "youtu.be" not in pod.group(0):
    erros.append("Podcast não aponta para o YouTube")

# ---------- questões ----------
q = (d / f"questoes_uni{u}.md").read_text(encoding="utf-8")
if "A PREENCHER" in q:
    erros.append(f"questoes_uni{u}.md: marcadores pendentes")
parte_q = q.split("## Feedbacks")[0]
qs = re.split(r"(?m)^### Questão \d+", parte_q)[1:]
tipos = re.findall(r"(?m)^### Questão \d+ \(([^)]+)\)", parte_q)
if len(qs) != 20:
    erros.append(f"questões: {len(qs)} (esperado 20)")
if tipos.count("Asserção-Razão") != 10 or tipos.count("Interpretação") != 10:
    erros.append(f"questões: tipos {tipos.count('Asserção-Razão')} AR / {tipos.count('Interpretação')} interpretação")
letras = []
for i, bq in enumerate(qs, 1):
    alts = re.findall(r"(?m)^(\*?)([a-e])\. ", bq)
    if [a[1] for a in alts] != list("abcde"):
        erros.append(f"Questão {i}: alternativas {[a[1] for a in alts]}")
    corr = [a[1] for a in alts if a[0]]
    if len(corr) != 1:
        erros.append(f"Questão {i}: {len(corr)} alternativas marcadas com *")
    letras.append(corr[0] if corr else "?")
print("Gabarito:", "".join(letras))
for l in "abcde":
    if letras.count(l) != 4:
        avisos.append(f"letra {l} correta {letras.count(l)}x (esperado 4)")
fb = q.split("## Feedbacks")[1] if "## Feedbacks" in q else ""
if len(re.findall(r"(?m)^### Questão \d+", fb)) != 20:
    erros.append("questões: feedbacks ≠ 20")

# ---------- roteiros estendidos ----------
r = (d / "roteiros_15min.md").read_text(encoding="utf-8")
if "A PREENCHER" in r:
    erros.append("roteiros_15min.md: marcadores pendentes")
for b in re.split(r"(?m)^## Roteiro da Videoaula ", r)[1:]:
    n = b.split(" ", 1)[0]
    falas = " ".join(re.findall(r"(?m)^> (.*)$", b))
    w = palavras(falas)
    print(f"Roteiro {n}: ~{w} palavras faladas (~{w / 140:.1f} min a 140 ppm)")
    if not 1900 <= w <= 3000:
        avisos.append(f"Roteiro {n}: {w} palavras faladas (alvo 15–20 min ≈ 2.100–2.800)")

# ---------- decks ----------
for h in sorted((d / "slides").glob("aula*.html")):
    s = h.read_text(encoding="utf-8")
    nome = h.name
    for need in ["../../assets/deck.css", "../../assets/obra.css", "../../assets/obra.js", "../../assets/deck.js", "../../assets/sprite.js"]:
        if need not in s:
            erros.append(f"{nome}: não carrega {need}")
    if s.find("obra.js") > s.find("deck.js\"></script>"):
        erros.append(f"{nome}: obra.js precisa vir antes de deck.js")
    nimg = len(re.findall(r"<img |foto-bg", s))
    ncred = len(re.findall(r'class="credito"', s))
    n3d = len(re.findall(r'data-viz="[a-z]*3d"', s))
    nviz = len(re.findall(r"data-viz=", s))
    nsl = len(re.findall(r'<section class="slide', s))
    print(f"{nome}: {nsl} slides, {nimg} fotos, {ncred} créditos, {nviz} visualizações ({n3d} em 3D)")
    if ncred < nimg - 1:  # foto do professor não leva crédito
        erros.append(f"{nome}: {nimg} fotos e só {ncred} créditos")
    if "mathjax" in s.lower() or "katex" in s.lower():
        erros.append(f"{nome}: usa MathJax/KaTeX (proibido)")
    for k, js in enumerate(re.findall(r"<script>(.*?)</script>", s, re.S)):
        with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as f:
            f.write(js)
        p = subprocess.run(["node", "--check", f.name], capture_output=True, text=True)
        if p.returncode:
            erros.append(f"{nome}: script inline {k + 1} com erro de sintaxe: {p.stderr.strip().splitlines()[-1]}")

print()
print("\n".join("ERRO  " + e for e in erros) or "sem erros")
print("\n".join("AVISO " + a for a in avisos))
sys.exit(1 if erros else 0)
