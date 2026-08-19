#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gera, para cada .md de conteudo da disciplina, um HTML autocontido
(<stem>_para_colar.html) com TODAS as imagens embutidas em base64,
pronto para o fluxo: abrir no navegador -> Ctrl+A -> Ctrl+C -> colar no Google Docs.

Por que isso resolve o problema de "colar direto no Google Docs":
  - Caminhos locais de imagem (assets/eq/*.png, assets/*.svg) NAO sao carregados
    pelo Google Docs quando voce cola. Embutindo tudo como data URI (base64), o
    Chrome coloca os bitmaps no clipboard e o Google Docs os incorpora de verdade.
  - As formulas ja sao imagens PNG (assets/eq/*.png), entao entram pixel-perfect,
    sem o Google Docs "desconfigurar" LaTeX ou autocorrigir simbolos.

O que o script faz com cada imagem:
  - PNG/JPG local  -> le e embute em base64 direto.
  - SVG local      -> rasteriza para PNG (via Chrome/Edge headless) e embute.
  - http(s) remoto -> baixa; se for SVG rasteriza; senao embute como esta.

Uso:
    python tools/montar_para_google_docs.py               # todos os arquivos-alvo
    python tools/montar_para_google_docs.py unidade_1/unidade_1.md   # so um arquivo

Requisitos: Python 3, pacote 'markdown' (pip install --user markdown),
Google Chrome ou Microsoft Edge (para os diagramas SVG). Pillow e opcional
(usado so para reduzir imagens muito grandes).
"""
import sys
import re
import os
import base64
import mimetypes
import subprocess
import tempfile
import time
import urllib.request
import urllib.error
from pathlib import Path

try:
    import markdown as md_lib
except ImportError:
    sys.exit("Falta o pacote 'markdown'. Rode:  python -m pip install --user markdown")

try:
    from PIL import Image
    import io
    HAVE_PIL = True
except ImportError:
    HAVE_PIL = False

DISC = Path(__file__).resolve().parent.parent  # raiz da disciplina

# Arquivos de conteudo que viram HTML para colar. Ajuste a vontade.
TARGETS = [
    "unidade_1/unidade_1.md",
    "unidade_2/unidade_2.md",
    "unidade_3/unidade_3.md",
    "unidade_4/unidade_4.md",
    "unidade_1/questoes_uni1.md",
    "unidade_2/questoes_uni2.md",
    "unidade_3/questoes_uni3.md",
    "unidade_4/questoes_uni4.md",
    "instrumentos_avaliativos/avaliacao_final.md",
    "instrumentos_avaliativos/entrega_trabalho.md",
]

MAX_W = 1600          # imagens raster mais largas que isso sao reduzidas (doc mais leve)
SVG_SCALE = 2         # rasteriza SVG em 2x para ficar nitido
_svg_cache = {}       # (path, mtime) -> png bytes
_remote_cache = {}    # url -> (bytes, mime)  (evita rebaixar a mesma imagem)


def find_browser():
    """Localiza Chrome ou Edge (necessario so para rasterizar os SVG)."""
    cands = [
        os.environ.get("CHROME"),
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        "google-chrome", "chromium", "chromium-browser", "msedge",
    ]
    for c in cands:
        if not c:
            continue
        if os.path.sep in c or (":" in c):
            if Path(c).exists():
                return c
        else:
            from shutil import which
            w = which(c)
            if w:
                return w
    return None


def rasterize_svg(svg_path: Path, browser: str) -> bytes:
    """Renderiza um SVG local para PNG (bytes) usando navegador headless."""
    key = (str(svg_path), svg_path.stat().st_mtime)
    if key in _svg_cache:
        return _svg_cache[key]
    if not browser:
        raise RuntimeError(
            "Chrome/Edge nao encontrado; nao da para rasterizar SVG.\n"
            f"  Defina a variavel de ambiente CHROME apontando para o chrome.exe.\n"
            f"  SVG: {svg_path}")

    svg = svg_path.read_text(encoding="utf-8")
    m = re.search(r'viewBox="[\d.]+\s+[\d.]+\s+([\d.]+)\s+([\d.]+)"', svg)
    if m:
        w, h = int(float(m.group(1))), int(float(m.group(2)))
    else:
        mw = re.search(r'width="([\d.]+)', svg)
        mh = re.search(r'height="([\d.]+)', svg)
        w = int(float(mw.group(1))) if mw else 800
        h = int(float(mh.group(1))) if mh else 600

    with tempfile.TemporaryDirectory() as td:
        td = Path(td)
        wrapper = td / "wrap.html"
        wrapper.write_text(
            "<!doctype html><html><head><meta charset='utf-8'>"
            "<style>*{margin:0;padding:0}html,body{background:#fff}"
            f"svg{{display:block;width:{w}px;height:{h}px}}</style></head><body>"
            + svg + "</body></html>",
            encoding="utf-8",
        )
        out = td / "out.png"
        cmd = [
            browser, "--headless=new", "--disable-gpu", "--hide-scrollbars",
            "--no-first-run", "--no-default-browser-check",
            f"--user-data-dir={td / 'profile'}",
            f"--force-device-scale-factor={SVG_SCALE}",
            f"--window-size={w},{h}",
            f"--screenshot={out}",
            wrapper.as_uri(),
        ]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                       timeout=90, check=False)
        if not out.exists():
            raise RuntimeError(f"Falha ao rasterizar {svg_path} (navegador nao gerou PNG).")
        data = out.read_bytes()
    _svg_cache[key] = data
    return data


def fetch_remote(url: str):
    """Baixa uma imagem remota (com cache, thumbnail e retry). Retorna (bytes, mime)."""
    if url in _remote_cache:
        return _remote_cache[url]

    # Wikimedia recomenda usar thumbnails em vez do original; alem de mais leve,
    # reduz o risco de rate-limit (HTTP 429). Special:FilePath aceita ?width=N.
    fetch_url = url
    if "Special:FilePath" in url and "width=" not in url:
        sep = "&" if "?" in url else "?"
        fetch_url = f"{url}{sep}width={MAX_W}"

    headers = {"User-Agent": "montar-google-docs/1.0 (material didatico; contato afonsolelis@gmail.com)"}
    last = None
    for attempt in range(4):
        try:
            req = urllib.request.Request(fetch_url, headers=headers)
            with urllib.request.urlopen(req, timeout=45) as r:
                data = r.read()
                ctype = (r.headers.get("Content-Type") or "").split(";")[0].strip()
            _remote_cache[url] = (data, ctype)
            time.sleep(0.4)  # cortesia: nao martelar o servidor
            return data, ctype
        except urllib.error.HTTPError as e:
            last = e
            if e.code in (429, 503):
                wait = e.headers.get("Retry-After")
                wait = int(wait) if (wait and str(wait).isdigit()) else (2 ** attempt) * 3
                time.sleep(min(wait, 30))
                continue
            raise
        except Exception as e:
            last = e
            time.sleep(2 ** attempt)
    raise last


def downscale(data: bytes, mime: str) -> tuple:
    """Reduz imagens raster muito largas (mantendo proporcao). Retorna (bytes, mime)."""
    if not HAVE_PIL or "svg" in mime:
        return data, mime
    try:
        im = Image.open(io.BytesIO(data))
        if im.width <= MAX_W:
            return data, mime
        ratio = MAX_W / im.width
        im = im.resize((MAX_W, max(1, int(im.height * ratio))))
        buf = io.BytesIO()
        if im.mode in ("RGBA", "P") and "jpeg" not in mime:
            im.save(buf, format="PNG"); mime = "image/png"
        else:
            im.convert("RGB").save(buf, format="JPEG", quality=85); mime = "image/jpeg"
        return buf.getvalue(), mime
    except Exception:
        return data, mime


def to_data_uri(data: bytes, mime: str) -> str:
    return f"data:{mime};base64," + base64.b64encode(data).decode("ascii")


def resolve_src(src: str, md_dir: Path, browser: str, stats: dict) -> str:
    """Converte um src de imagem em data URI base64."""
    if src.startswith("data:"):
        return src
    try:
        if src.startswith(("http://", "https://")):
            data, mime = fetch_remote(src)
            if "svg" in mime or src.lower().split("?")[0].endswith(".svg"):
                # remoto e SVG: grava temporario e rasteriza
                with tempfile.NamedTemporaryFile(suffix=".svg", delete=False) as tf:
                    tf.write(data); tmp = Path(tf.name)
                try:
                    data, mime = rasterize_svg(tmp, browser), "image/png"
                finally:
                    tmp.unlink(missing_ok=True)
            if not mime:
                mime = mimetypes.guess_type(src)[0] or "image/png"
            data, mime = downscale(data, mime)
            stats["remoto"] += 1
            return to_data_uri(data, mime)

        # local
        p = (md_dir / src).resolve()
        if not p.exists():
            stats["faltando"].append(src)
            return src  # deixa como esta; aparecera quebrado (sinaliza problema)
        if p.suffix.lower() == ".svg":
            data = rasterize_svg(p, browser)
            stats["svg"] += 1
            return to_data_uri(data, "image/png")
        mime = mimetypes.guess_type(str(p))[0] or "image/png"
        data, mime = downscale(p.read_bytes(), mime)
        stats["local"] += 1
        return to_data_uri(data, mime)
    except Exception as e:
        stats["erros"].append(f"{src} -> {e}")
        return src


IMG_SRC_RE = re.compile(r'(<img\b[^>]*?\bsrc=")([^"]+)(")', re.IGNORECASE)


def inline_images(html: str, md_dir: Path, browser: str, stats: dict) -> str:
    def repl(m):
        return m.group(1) + resolve_src(m.group(2), md_dir, browser, stats) + m.group(3)
    return IMG_SRC_RE.sub(repl, html)


PAGE_CSS = """
:root{--tinta:#1a1a1a;--linha:#c9c9c9;--azul:#002057}
*{box-sizing:border-box}
body{max-width:820px;margin:32px auto;padding:0 20px;color:var(--tinta);
  font-family:'Georgia','Times New Roman',serif;font-size:17px;line-height:1.6}
h1,h2,h3,h4{font-family:'Segoe UI',Arial,sans-serif;color:var(--azul);line-height:1.25}
h1{font-size:1.9em;border-bottom:2px solid var(--azul);padding-bottom:.2em}
h2{font-size:1.5em;margin-top:1.6em}
h3{font-size:1.2em}h4{font-size:1.05em}
img{max-width:100%;height:auto}
table{border-collapse:collapse;margin:1em 0;width:100%}
th,td{border:1px solid var(--linha);padding:6px 10px;text-align:left}
th{background:#eef1f6}
blockquote{border-left:4px solid var(--azul);margin:1em 0;padding:.2em 1em;
  background:#f6f8fb;color:#333}
code{background:#f0f0f0;padding:1px 4px;border-radius:3px;font-size:.9em}
hr{border:0;border-top:1px solid var(--linha);margin:2em 0}
"""

PAGE = """<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title><style>{css}</style></head>
<body>
{body}
</body></html>
"""


def build_file(rel: str, browser: str):
    src_md = DISC / rel
    if not src_md.exists():
        print(f"  ! pulando (nao existe): {rel}")
        return
    md_dir = src_md.parent
    text = src_md.read_text(encoding="utf-8")
    # O conteudo foi escrito para pandoc, que trata "$" como delimitador de
    # matematica; por isso cifroes visiveis vem escapados como "\$". O
    # python-markdown nao desfaz esse escape (nao e um caractere especial dele),
    # entao "R\$ 20" apareceria com a barra. Desescapamos aqui.
    text = text.replace(r"\$", "$")
    html_body = md_lib.markdown(
        text,
        extensions=["tables", "sane_lists", "attr_list"],
        output_format="html5",
    )
    stats = {"local": 0, "svg": 0, "remoto": 0, "faltando": [], "erros": []}
    html_body = inline_images(html_body, md_dir, browser, stats)

    title = src_md.stem
    page = PAGE.format(title=title, css=PAGE_CSS, body=html_body)
    out = src_md.with_name(src_md.stem + "_para_colar.html")
    out.write_text(page, encoding="utf-8")

    kb = out.stat().st_size // 1024
    msg = (f"  OK {rel}\n"
           f"       -> {out.name}  ({kb} KB)  "
           f"[png locais {stats['local']}, svg {stats['svg']}, remotas {stats['remoto']}]")
    print(msg)
    if stats["faltando"]:
        print(f"       ! imagens locais nao encontradas: {len(stats['faltando'])}")
        for s in stats["faltando"][:8]:
            print(f"          - {s}")
    if stats["erros"]:
        print(f"       ! erros: {len(stats['erros'])}")
        for s in stats["erros"][:8]:
            print(f"          - {s}")


def main():
    args = sys.argv[1:]
    targets = args if args else TARGETS
    browser = find_browser()
    print(f"Disciplina: {DISC.name}")
    print(f"Navegador para SVG: {browser or 'NAO ENCONTRADO (SVGs falharao)'}")
    print(f"Pillow (reduzir imagens grandes): {'sim' if HAVE_PIL else 'nao'}")
    print("-" * 60)
    for rel in targets:
        rel = rel.replace("\\", "/")
        build_file(rel, browser)
    print("-" * 60)
    print("Pronto. Para cada arquivo, abra o *_para_colar.html no Chrome,")
    print("selecione tudo (Ctrl+A), copie (Ctrl+C) e cole no Google Docs.")


if __name__ == "__main__":
    main()
