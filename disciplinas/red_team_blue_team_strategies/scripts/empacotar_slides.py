"""Gera uma versão autocontida (um único .html) de cada deck, para entregar no Drive.

Uso:  python scripts/empacotar_slides.py      (saída em entregas_docx/slides_html/aulaN.html)

O deck do repositório depende de assets/ e de simulador/. Aqui tudo é embutido:
CSS, JS, foto do professor, favicon e o simulador da Rede Tatame (carregado no iframe
por um blob URL). Só o three.js das cenas 3D continua vindo do cdnjs (precisa de internet).
"""
from __future__ import annotations

import base64
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SAIDA = RAIZ / "entregas_docx" / "slides_html"


def ler(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def js_seguro(s: str) -> str:
    return s.replace("</script", "<\\/script")


def data_uri(p: Path, mime: str) -> str:
    return f"data:{mime};base64," + base64.b64encode(p.read_bytes()).decode()


def simulador_embutido() -> str:
    html = ler(RAIZ / "simulador" / "index.html")
    html = html.replace('<link rel="stylesheet" href="simulador.css">', f"<style>\n{ler(RAIZ / 'simulador' / 'simulador.css')}\n</style>")
    html = html.replace('<script src="simulador.js"></script>', f"<script>\n{js_seguro(ler(RAIZ / 'simulador' / 'simulador.js'))}\n</script>")
    # dentro do deck ele sempre roda no modo embutido
    html = html.replace("if (new URLSearchParams(location.search).get('embed') === '1') {", "if (true) {")
    html = re.sub(r'<link rel="(alternate icon|apple-touch-icon|icon)"[^>]*>', "", html)
    html = html.replace('href="../index.html"', 'href="#"')
    assert "simulador.js" not in html and "simulador.css" not in html
    return html


def empacotar(deck: Path, sim_b64: str, fav: str) -> str:
    h = ler(deck)
    a = RAIZ / "assets"
    for css in ("deck.css", "labs.css"):
        h = h.replace(f'<link rel="stylesheet" href="../../assets/{css}">', f"<style>\n{ler(a / css)}\n</style>")
    labs = ler(a / "labs.js")
    alvo = "simFrame.src = (cfg.src || '../../simulador/index.html') + '?embed=1#' + (cfg.aba || 'arquitetura');"
    assert alvo in labs
    labs = labs.replace(alvo, "simFrame.src = (window.__SIM_URL || (window.__SIM_URL = URL.createObjectURL(new Blob("
                              "[new TextDecoder().decode(Uint8Array.from(atob(window.__SIM_B64), (c) => c.charCodeAt(0)))],"
                              " { type: 'text/html' })))) + '#' + (cfg.aba || 'arquitetura');")
    for js, conteudo in (("sprite.js", ler(a / "sprite.js")), ("deck.js", ler(a / "deck.js")), ("labs.js", labs)):
        h = h.replace(f'<script src="../../assets/{js}"></script>', f"<script>\n{js_seguro(conteudo)}\n</script>")
    h = h.replace("../../assets/foto-professor.jpg", data_uri(a / "foto-professor.jpg", "image/jpeg"))
    h = h.replace("</head>", f'<link rel="icon" type="image/svg+xml" href="{fav}">\n'
                             f"<script>window.__SIM_B64 = '{sim_b64}';</script>\n</head>", 1)
    resto = re.findall(r'(?:href|src)="\.\./\.\./[^"]+"', h)
    assert not resto, (deck.name, resto)
    return h


def main():
    SAIDA.mkdir(parents=True, exist_ok=True)
    sim_b64 = base64.b64encode(simulador_embutido().encode("utf-8")).decode()
    fav = data_uri(RAIZ / "assets" / "favicon.svg", "image/svg+xml")
    for deck in sorted(RAIZ.glob("unidade_*/slides/aula*.html"), key=lambda p: int(re.search(r"\d+", p.stem).group())):
        destino = SAIDA / deck.name
        destino.write_text(empacotar(deck, sim_b64, fav), encoding="utf-8")
        print(f"{deck.parent.parent.name}/{deck.name} -> {destino.relative_to(RAIZ)} ({destino.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
