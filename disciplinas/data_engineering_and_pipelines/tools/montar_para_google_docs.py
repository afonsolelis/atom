#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gera, para cada .md de conteudo da disciplina, um HTML autocontido
(<stem>_para_colar.html) com TODAS as imagens embutidas em base64,
pronto para o fluxo: abrir no navegador -> Ctrl+A -> Ctrl+C -> colar no Google Docs.

Diferenca em relacao a disciplina de Portos: aqui a matematica esta em LaTeX cru
($...$ inline e $$...$$ em bloco). Se fosse colada como texto, o Google Docs
"desconfiguraria" tudo. Entao cada formula e RENDERIZADA para PNG (via MathJax +
Chrome headless) e embutida como imagem — igual ao resultado final de Portos.

O que o script faz com cada elemento:
  - $...$ / $$...$$  -> renderiza com MathJax -> PNG (autocrop) -> base64 embutido.
  - imagem http(s)   -> baixa (thumbnail Wikimedia) -> base64 embutido.
  - imagem local     -> le e embute (png/jpg direto; svg rasterizado via Chrome).
  - \\$ vira $ ; "R$ 120" (cifrao de moeda) permanece como texto (regra do pandoc).

Uso:
    python tools/montar_para_google_docs.py               # todos os arquivos-alvo
    python tools/montar_para_google_docs.py unidade_1/unidade_1.md   # so um arquivo

Requisitos: Python 3, pacote 'markdown' (pip install --user markdown), Pillow,
Google Chrome ou Microsoft Edge (para renderizar as formulas), e internet na
primeira execucao (baixa o MathJax e as fotos remotas).
"""
import sys
import re
import os
import io
import base64
import hashlib
import mimetypes
import subprocess
import tempfile
import time
import urllib.request
import urllib.error
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

try:
    import markdown as md_lib
except ImportError:
    sys.exit("Falta o pacote 'markdown'. Rode:  python -m pip install --user markdown")

try:
    from PIL import Image, ImageChops
except ImportError:
    sys.exit("Falta o Pillow (necessario para recortar as formulas). Rode:  python -m pip install --user pillow")

DISC = Path(__file__).resolve().parent.parent
CACHE = DISC / "tools" / "_cache_formulas"     # PNGs de formula + mathjax.js (acelera rebuilds)
MATHJAX_URL = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"

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

MAX_W = 1600
SVG_SCALE = 2
_svg_cache = {}
_remote_cache = {}


# ----------------------------------------------------------------------------- navegador
def find_browser():
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
        if os.path.sep in c or ":" in c:
            if Path(c).exists():
                return c
        else:
            from shutil import which
            w = which(c)
            if w:
                return w
    return None


BROWSER = find_browser()


# ----------------------------------------------------------------------------- MathJax
_MATHJAX_JS = None


def ensure_mathjax():
    global _MATHJAX_JS
    if _MATHJAX_JS is not None:
        return _MATHJAX_JS
    CACHE.mkdir(parents=True, exist_ok=True)
    local = CACHE / "mathjax-tex-svg.js"
    if not local.exists():
        print("  baixando MathJax (uma vez)...")
        req = urllib.request.Request(MATHJAX_URL, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=90) as r:
            local.write_bytes(r.read())
    _MATHJAX_JS = local
    return local


PAGE_TMPL = (
    "<!doctype html><html><head><meta charset='utf-8'>"
    "<style>*{{margin:0;padding:0}}html,body{{background:#fff}}"
    "#m{{display:inline-block;padding:6px 10px;font-size:{fs}px;color:#111;"
    "font-family:'Times New Roman',serif}}</style>"
    "<script>window.MathJax={{tex:{{inlineMath:[['\\\\(','\\\\)']],"
    "displayMath:[['$$','$$']]}},svg:{{fontCache:'none'}}}};</script>"
    "<script src='mathjax.js'></script></head>"
    "<body><div id='m'>{body}</div></body></html>"
)


def _crop_png(raw_path: Path) -> bytes:
    im = Image.open(raw_path).convert("RGB")
    bg = Image.new("RGB", im.size, (255, 255, 255))
    bbox = ImageChops.difference(im, bg).getbbox()
    if bbox:
        pad = 6
        bbox = (max(0, bbox[0] - pad), max(0, bbox[1] - pad),
                min(im.width, bbox[2] + pad), min(im.height, bbox[3] + pad))
        im = im.crop(bbox)
    buf = io.BytesIO()
    im.save(buf, format="PNG")
    return buf.getvalue()


def _render_formula_uncached(latex: str, display: bool, workdir: Path, idx: int) -> bytes:
    mj = ensure_mathjax()
    d = workdir / f"job{idx}"
    d.mkdir(parents=True, exist_ok=True)
    # symlink/copiar mathjax.js para o dir do job (referencia relativa same-origin)
    js = d / "mathjax.js"
    if not js.exists():
        js.write_bytes(mj.read_bytes())
    body = f"$${latex}$$" if display else f"\\({latex}\\)"
    fs = 30 if display else 26
    page = d / "f.html"
    page.write_text(PAGE_TMPL.format(fs=fs, body=body), encoding="utf-8")
    raw = d / "raw.png"
    cmd = [
        BROWSER, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--no-first-run", "--no-default-browser-check",
        f"--user-data-dir={d / 'p'}",
        "--force-device-scale-factor=2",
        "--virtual-time-budget=8000",
        "--window-size=2200,1400",
        f"--screenshot={raw}",
        page.as_uri(),
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                   timeout=120, check=False)
    if not raw.exists():
        raise RuntimeError("MathJax/Chrome nao gerou PNG")
    return _crop_png(raw)


def render_all_formulas(formulas):
    """formulas: lista de (latex, display). Retorna dict {(latex,display): png_bytes}.
    Usa cache em disco por hash; renderiza os faltantes em paralelo."""
    if not BROWSER:
        raise RuntimeError("Chrome/Edge nao encontrado — necessario para renderizar formulas. "
                           "Defina a variavel de ambiente CHROME.")
    CACHE.mkdir(parents=True, exist_ok=True)
    result = {}
    todo = []
    for latex, display in formulas:
        h = hashlib.sha1((("D:" if display else "I:") + latex).encode("utf-8")).hexdigest()[:16]
        cp = CACHE / f"{h}.png"
        if cp.exists():
            result[(latex, display)] = cp.read_bytes()
        else:
            todo.append((latex, display, cp))
    if todo:
        print(f"  renderizando {len(todo)} formulas novas (cache: {len(result)})...")
        with tempfile.TemporaryDirectory() as td:
            workdir = Path(td)

            def work(job):
                latex, display, cp, idx = job
                png = _render_formula_uncached(latex, display, workdir, idx)
                cp.write_bytes(png)
                return (latex, display), png

            jobs = [(l, d, cp, i) for i, (l, d, cp) in enumerate(todo)]
            with ThreadPoolExecutor(max_workers=4) as ex:
                for i, (key, png) in enumerate(ex.map(work, jobs), 1):
                    result[key] = png
                    if i % 10 == 0 or i == len(jobs):
                        print(f"    {i}/{len(jobs)}")
    return result


# ----------------------------------------------------------------------------- tokenizer de math
def iter_math(text):
    """Gera segmentos (kind, content). kind in {'text','inline','display'}.
    Regras do pandoc: '$' so abre math se o proximo char nao for espaco; so fecha se
    o anterior nao for espaco e o seguinte nao for digito; inline nao cruza linha.
    Tags HTML <...> sao tratadas como texto opaco (protege alt de <img>)."""
    i, n = 0, len(text)
    buf = []
    def flush():
        if buf:
            yield_buf.append(("text", "".join(buf)))
            buf.clear()
    yield_buf = []
    while i < n:
        ch = text[i]
        if ch == "<":                                   # tag HTML: opaco ate '>'
            j = text.find(">", i)
            if j == -1:
                buf.append(text[i:]); break
            buf.append(text[i:j + 1]); i = j + 1; continue
        if ch == "\\" and i + 1 < n:
            buf.append(text[i:i + 2]); i += 2; continue
        if ch == "$":
            if text[i + 1:i + 2] == "$":                # display $$...$$
                j = text.find("$$", i + 2)
                if j != -1:
                    flush(); yield_buf.append(("display", text[i + 2:j].strip())); i = j + 2; continue
                buf.append("$$"); i += 2; continue
            nxt = text[i + 1] if i + 1 < n else ""
            if nxt == "" or nxt.isspace():              # nao abre (espaco apos $)
                buf.append("$"); i += 1; continue
            j = i + 1; found = -1
            while j < n:
                cj = text[j]
                if cj == "\n":
                    break
                if cj == "\\":
                    j += 2; continue
                if cj == "$":
                    prev = text[j - 1]; after = text[j + 1] if j + 1 < n else ""
                    if not prev.isspace() and not after.isdigit():
                        found = j; break
                j += 1
            if found != -1:
                flush(); yield_buf.append(("inline", text[i + 1:found])); i = found + 1; continue
            buf.append("$"); i += 1; continue
        buf.append(ch); i += 1
    flush()
    return yield_buf


def collect_formulas(text):
    return [(c, kind == "display") for kind, c in iter_math(text) if kind in ("inline", "display")]


def replace_math_with_imgs(text, formula_pngs):
    """Substitui cada math por <img data:...> (inline ou bloco centrado);
    desescapa \\$ -> $ no texto normal."""
    out = []
    for kind, content in iter_math(text):
        if kind == "text":
            out.append(content.replace(r"\$", "$"))
        else:
            display = kind == "display"
            png = formula_pngs.get((content.strip(), display))
            if png is None:
                out.append(("$$%s$$" if display else "$%s$") % content)  # fallback: texto
                continue
            uri = "data:image/png;base64," + base64.b64encode(png).decode("ascii")
            if display:
                out.append(f'\n\n<p style="text-align:center;margin:1em 0">'
                           f'<img src="{uri}" style="max-width:100%;height:auto" alt="formula" /></p>\n\n')
            else:
                out.append(f'<img src="{uri}" style="height:1.15em;vertical-align:-0.28em" alt="formula" />')
    return "".join(out)


# ----------------------------------------------------------------------------- imagens (svg/remoto/local)
def rasterize_svg(svg_path: Path) -> bytes:
    key = (str(svg_path), svg_path.stat().st_mtime)
    if key in _svg_cache:
        return _svg_cache[key]
    if not BROWSER:
        raise RuntimeError(f"Chrome/Edge nao encontrado para rasterizar SVG: {svg_path}")
    svg = svg_path.read_text(encoding="utf-8")
    m = re.search(r'viewBox="[\d.]+\s+[\d.]+\s+([\d.]+)\s+([\d.]+)"', svg)
    if m:
        w, h = int(float(m.group(1))), int(float(m.group(2)))
    else:
        mw = re.search(r'width="([\d.]+)', svg); mh = re.search(r'height="([\d.]+)', svg)
        w = int(float(mw.group(1))) if mw else 800
        h = int(float(mh.group(1))) if mh else 600
    with tempfile.TemporaryDirectory() as td:
        td = Path(td)
        wrapper = td / "wrap.html"
        wrapper.write_text(
            "<!doctype html><html><head><meta charset='utf-8'>"
            "<style>*{margin:0;padding:0}html,body{background:#fff}"
            f"svg{{display:block;width:{w}px;height:{h}px}}</style></head><body>"
            + svg + "</body></html>", encoding="utf-8")
        out = td / "out.png"
        cmd = [BROWSER, "--headless=new", "--disable-gpu", "--hide-scrollbars",
               "--no-first-run", "--no-default-browser-check",
               f"--user-data-dir={td / 'profile'}",
               f"--force-device-scale-factor={SVG_SCALE}",
               f"--window-size={w},{h}", f"--screenshot={out}", wrapper.as_uri()]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=90, check=False)
        if not out.exists():
            raise RuntimeError(f"Falha ao rasterizar {svg_path}")
        data = out.read_bytes()
    _svg_cache[key] = data
    return data


def fetch_remote(url: str):
    if url in _remote_cache:
        return _remote_cache[url]
    fetch_url = url
    if "Special:FilePath" in url and "width=" not in url:
        sep = "&" if "?" in url else "?"
        fetch_url = f"{url}{sep}width={MAX_W}"
    headers = {"User-Agent": "montar-google-docs/1.0 (material didatico; contato afonsolelis@gmail.com)"}
    last = None
    for attempt in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(fetch_url, headers=headers), timeout=45) as r:
                data = r.read()
                ctype = (r.headers.get("Content-Type") or "").split(";")[0].strip()
            _remote_cache[url] = (data, ctype)
            time.sleep(0.4)
            return data, ctype
        except urllib.error.HTTPError as e:
            last = e
            if e.code in (429, 503):
                wait = e.headers.get("Retry-After")
                wait = int(wait) if (wait and str(wait).isdigit()) else (2 ** attempt) * 3
                time.sleep(min(wait, 30)); continue
            raise
        except Exception as e:
            last = e; time.sleep(2 ** attempt)
    raise last


def downscale(data: bytes, mime: str):
    if "svg" in mime:
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


def resolve_src(src, md_dir, stats):
    if src.startswith("data:"):
        return src
    try:
        if src.startswith(("http://", "https://")):
            data, mime = fetch_remote(src)
            # NAO decidir SVG pela extensao da URL: a Wikimedia, ao pedir thumbnail
            # (?width=), devolve PNG mesmo para arquivos .svg. Confiar no Content-Type.
            if "svg" in mime:
                with tempfile.NamedTemporaryFile(suffix=".svg", delete=False) as tf:
                    tf.write(data); tmp = Path(tf.name)
                try:
                    data, mime = rasterize_svg(tmp), "image/png"
                finally:
                    tmp.unlink(missing_ok=True)
            if not mime:
                mime = mimetypes.guess_type(src)[0] or "image/png"
            data, mime = downscale(data, mime)
            stats["remoto"] += 1
            return to_data_uri(data, mime)
        p = (md_dir / src).resolve()
        if not p.exists():
            stats["faltando"].append(src); return src
        if p.suffix.lower() == ".svg":
            stats["svg"] += 1
            return to_data_uri(rasterize_svg(p), "image/png")
        mime = mimetypes.guess_type(str(p))[0] or "image/png"
        data, mime = downscale(p.read_bytes(), mime)
        stats["local"] += 1
        return to_data_uri(data, mime)
    except Exception as e:
        stats["erros"].append(f"{src} -> {e}")
        return src


IMG_SRC_RE = re.compile(r'(<img\b[^>]*?\bsrc=")([^"]+)(")', re.IGNORECASE)


def inline_images(html, md_dir, stats):
    return IMG_SRC_RE.sub(lambda m: m.group(1) + resolve_src(m.group(2), md_dir, stats) + m.group(3), html)


# ----------------------------------------------------------------------------- pagina final
PAGE_CSS = """
:root{--tinta:#1a1a1a;--linha:#c9c9c9;--azul:#0b3d5c}
*{box-sizing:border-box}
body{max-width:820px;margin:32px auto;padding:0 20px;color:var(--tinta);
  font-family:'Georgia','Times New Roman',serif;font-size:17px;line-height:1.6}
h1,h2,h3,h4{font-family:'Segoe UI',Arial,sans-serif;color:var(--azul);line-height:1.25}
h1{font-size:1.9em;border-bottom:2px solid var(--azul);padding-bottom:.2em}
h2{font-size:1.5em;margin-top:1.6em}h3{font-size:1.2em}h4{font-size:1.05em}
img{max-width:100%;height:auto}
table{border-collapse:collapse;margin:1em 0;width:100%}
th,td{border:1px solid var(--linha);padding:6px 10px;text-align:left}
th{background:#eef1f6}
blockquote{border-left:4px solid var(--azul);margin:1em 0;padding:.2em 1em;background:#f6f8fb;color:#333}
code{background:#f0f0f0;padding:1px 4px;border-radius:3px;font-size:.9em}
pre{background:#f6f8fb;padding:12px;overflow:auto;border-radius:4px}
hr{border:0;border-top:1px solid var(--linha);margin:2em 0}
"""

PAGE = ("<!doctype html>\n<html lang='pt-BR'><head><meta charset='utf-8'>"
        "<meta name='viewport' content='width=device-width, initial-scale=1'>"
        "<title>{title}</title><style>{css}</style></head>\n<body>\n{body}\n</body></html>\n")


def build_file(rel, formula_pngs):
    src_md = DISC / rel
    if not src_md.exists():
        print(f"  ! pulando (nao existe): {rel}"); return
    md_dir = src_md.parent
    text = src_md.read_text(encoding="utf-8")
    text = replace_math_with_imgs(text, formula_pngs)     # $..$ -> <img data:>
    html_body = md_lib.markdown(text, extensions=["tables", "sane_lists", "attr_list", "fenced_code"],
                                output_format="html5")
    stats = {"local": 0, "svg": 0, "remoto": 0, "faltando": [], "erros": []}
    html_body = inline_images(html_body, md_dir, stats)
    out = src_md.with_name(src_md.stem + "_para_colar.html")
    out.write_text(PAGE.format(title=src_md.stem, css=PAGE_CSS, body=html_body), encoding="utf-8")
    kb = out.stat().st_size // 1024
    print(f"  OK {rel}\n       -> {out.name}  ({kb} KB)  "
          f"[formulas, png {stats['local']}, svg {stats['svg']}, remotas {stats['remoto']}]")
    if stats["faltando"]:
        print(f"       ! imagens locais nao encontradas: {len(stats['faltando'])}")
        for s in stats["faltando"][:8]:
            print(f"          - {s}")
    if stats["erros"]:
        print(f"       ! erros: {len(stats['erros'])}")
        for s in stats["erros"][:8]:
            print(f"          - {s}")


def main():
    args = [a.replace("\\", "/") for a in sys.argv[1:]]
    targets = args if args else TARGETS
    print(f"Disciplina: {DISC.name}")
    print(f"Navegador: {BROWSER or 'NAO ENCONTRADO'}")
    print("-" * 60)

    # 1) coletar TODAS as formulas unicas de todos os arquivos e renderiza-las
    all_formulas = {}
    for rel in targets:
        p = DISC / rel
        if p.exists():
            for latex, disp in collect_formulas(p.read_text(encoding="utf-8")):
                all_formulas[(latex.strip(), disp)] = None
    print(f"Formulas unicas a garantir: {len(all_formulas)}")
    formula_pngs = render_all_formulas(list(all_formulas.keys())) if all_formulas else {}
    print("-" * 60)

    # 2) montar cada HTML
    for rel in targets:
        build_file(rel, formula_pngs)
    print("-" * 60)
    print("Pronto. Abra cada *_para_colar.html no Chrome, Ctrl+A, Ctrl+C e cole no Google Docs.")


if __name__ == "__main__":
    main()
