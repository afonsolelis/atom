"""Copia simulador/APLICACAO.md para dentro de simulador/aplicacao.html.

A página tenta ler o .md por fetch (funciona em servidor local); aberta direto
pelo arquivo (file://), o navegador bloqueia o fetch e ela usa esta cópia
embutida. Rode sempre que editar o APLICACAO.md:

    python scripts/embutir_aplicacao.py
"""
from pathlib import Path
import re
import sys

RAIZ = Path(__file__).resolve().parent.parent / "simulador"
MD = RAIZ / "APLICACAO.md"
HTML = RAIZ / "aplicacao.html"
PADRAO = re.compile(
    r'(<script type="text/markdown" id="md-embutido">\n).*?(</script>)', re.S
)

md = MD.read_text(encoding="utf-8")
if "</script" in md.lower():
    sys.exit("APLICACAO.md contém '</script', o que quebraria a cópia embutida.")
html = HTML.read_text(encoding="utf-8")
if not PADRAO.search(html):
    sys.exit("Bloco md-embutido não encontrado em aplicacao.html.")
novo = PADRAO.sub(lambda m: m.group(1) + md.rstrip("\n") + "\n" + m.group(2), html)
HTML.write_text(novo, encoding="utf-8", newline="\n")
print("aplicacao.html", "atualizado" if novo != html else "já estava em dia")
