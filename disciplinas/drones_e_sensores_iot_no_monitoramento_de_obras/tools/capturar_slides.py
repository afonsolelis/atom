"""Captura screenshots de um deck (um PNG por slide) e lista erros de console.

Uso: python tools/capturar_slides.py unidade_1/slides/aula0.html [saida_dir] [espera_ms]

Usa o Chrome instalado (channel="chrome") para ter WebGL de verdade nas cenas 3D.
"""
import pathlib
import sys

from playwright.sync_api import sync_playwright

deck = pathlib.Path(sys.argv[1]).resolve()
saida = pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else "capturas") / deck.stem
espera = int(sys.argv[3]) if len(sys.argv) > 3 else 2500
saida.mkdir(parents=True, exist_ok=True)

with sync_playwright() as p:
    nav = p.chromium.launch(channel="chrome", args=["--use-angle=swiftshader", "--enable-unsafe-swiftshader"])
    pg = nav.new_page(viewport={"width": 1280, "height": 720})
    erros = []
    pg.on("console", lambda m: erros.append(f"[{m.type}] {m.text}") if m.type in ("error", "warning") else None)
    pg.on("pageerror", lambda e: erros.append(f"[pageerror] {e}"))
    pg.goto(deck.as_uri())
    pg.wait_for_timeout(1000)
    n = pg.evaluate("Deck.slides.length")
    for i in range(n):
        pg.evaluate(f"Deck.show({i})")
        pg.wait_for_timeout(espera)
        pg.screenshot(path=str(saida / f"slide_{i + 1:02d}.png"))
        # conteúdo transbordando o cartão do slide
        over = pg.evaluate("""() => { const s = Deck.slides[Deck.index]; const c = s.querySelector('.slide-content');
            return c ? Math.max(0, c.scrollHeight - c.clientHeight) : 0 }""")
        if over > 4:
            erros.append(f"[overflow] slide {i + 1}: conteúdo passa {over}px do cartão")
        # cortes internos: caixas de texto com overflow escondido cujo conteúdo não cabe
        cortes = pg.evaluate(r"""() => { const s = Deck.slides[Deck.index]; const out = [];
            for (const el of s.querySelectorAll('*')) {
              if (el.querySelector('img,canvas,svg,video') || el.closest('.viz canvas')) continue;
              const cs = getComputedStyle(el);
              if (cs.display === 'none' || !/hidden|auto|scroll|clip/.test(cs.overflow + cs.overflowY + cs.overflowX)) continue;
              if (!el.innerText || !el.innerText.trim()) continue;
              const dy = el.scrollHeight - el.clientHeight, dx = el.scrollWidth - el.clientWidth;
              if (dy > 4 || dx > 4) out.push((el.className || el.tagName) + ' (' + Math.max(dy, dx) + 'px): ' + el.innerText.trim().slice(0, 40).replace(/\s+/g, ' '));
            } return out.slice(0, 5) }""")
        for c in cortes:
            erros.append(f"[corte] slide {i + 1}: {c}")
    nav.close()
print(f"{n} slides -> {saida}")
print("\n".join(erros) or "sem erros de console")
