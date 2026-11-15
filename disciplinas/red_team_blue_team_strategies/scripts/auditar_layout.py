"""Auditoria visual dos decks: sobreposição, corte e conteúdo sob a navegação.

Uso (com o servidor local rodando na raiz do repositório atom):
    python -m http.server 8765 --bind 127.0.0.1
    python scripts/auditar_layout.py [aulaN ...] [--shots PASTA] [--size 1280x720]

Para cada slide: ativa, avança fluxos e terminais até o fim, espera as
animações e mede, no DOM:
- conteúdo que passa da borda do slide;
- texto cortado (scrollHeight > clientHeight em caixa sem rolagem);
- irmãos que se sobrepõem (cartões, colunas, painéis);
- rótulos de SVG (fluxos e diagramas) que se sobrepõem ou saem da área;
- conteúdo embaixo dos botões fixos de navegação (fora dos laboratórios, onde a barra some sozinha).
Sai com código 1 se houver problema. Com --shots, salva um PNG por slide.
"""
from __future__ import annotations

import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

BASE = "http://127.0.0.1:8765/disciplinas/red_team_blue_team_strategies/"
DECKS = {0: 1, **{k: (k - 1) // 4 + 1 for k in range(1, 17)}}

JS = r"""
() => {
  const out = [];
  const s = document.querySelector('#deck > section.slide.active');
  if (!s) return out;
  const R = (e) => e.getBoundingClientRect();
  const vis = (e) => { const r = R(e); const cs = getComputedStyle(e); return r.width > 2 && r.height > 2 && cs.visibility !== 'hidden' && cs.display !== 'none' && +cs.opacity > 0.05; };
  const name = (e) => (e.id ? '#' + e.id : '') + (typeof e.className === 'string' && e.className.trim() ? '.' + e.className.trim().split(/\s+/).slice(0, 2).join('.') : '<' + e.tagName.toLowerCase() + '>') + ' "' + (e.textContent || '').trim().replace(/\s+/g, ' ').slice(0, 50) + '"';
  const inter = (a, b, pad) => !(a.right - pad <= b.left || b.right - pad <= a.left || a.bottom - pad <= b.top || b.bottom - pad <= a.top);
  const sr = R(s);
  const content = s.querySelector('.slide-content') || s;
  const insideScroll = (e) => { let p = e.parentElement; while (p && p !== s) { const cs = getComputedStyle(p); if (cs.overflowY === 'auto' || cs.overflowY === 'scroll' || cs.overflow === 'hidden') return true; p = p.parentElement; } return false; };
  content.querySelectorAll('*').forEach((e) => {
    if (!vis(e) || (e.closest('svg') && e.tagName.toLowerCase() !== 'svg')) return;
    const r = R(e);
    if ((r.right > sr.right + 3 || r.bottom > sr.bottom + 3 || r.left < sr.left - 3 || r.top < sr.top - 3) && !insideScroll(e)) out.push(['fora do slide', name(e)]);
  });
  content.querySelectorAll('*').forEach((e) => {
    if (!vis(e) || e.closest('.vsc, .term, .siem, .brw, svg, iframe, .scene3d, .vsc-code, pre')) return;
    const cs = getComputedStyle(e);
    if (cs.overflowY === 'auto' || cs.overflowY === 'scroll') return;
    const clipY = (cs.overflowY === 'hidden') && e.scrollHeight > e.clientHeight + 4;
    const clipX = (cs.overflowX === 'hidden') && e.scrollWidth > e.clientWidth + 4 && cs.textOverflow !== 'ellipsis';
    if (clipY || clipX) out.push(['texto cortado', name(e)]);
  });
  content.querySelectorAll('*').forEach((par) => {
    if (par.closest('svg, .vsc, .term, .siem, .brw, .scene3d, iframe')) return;
    const kids = [...par.children].filter((k) => vis(k) && !['absolute', 'fixed'].includes(getComputedStyle(k).position) && !getComputedStyle(k).display.startsWith('inline'));
    for (let i = 0; i < kids.length; i++) for (let j = i + 1; j < kids.length; j++) {
      if (inter(R(kids[i]), R(kids[j]), 4)) out.push(['sobreposição', name(kids[i]) + '  x  ' + name(kids[j])]);
    }
  });
  s.querySelectorAll('svg').forEach((svg) => {
    if (svg.closest('.mosaico-bg') || !vis(svg)) return;
    const ts = [...svg.querySelectorAll('text')].filter((t) => vis(t) && t.textContent.trim());
    for (let i = 0; i < ts.length; i++) for (let j = i + 1; j < ts.length; j++) {
      if (inter(R(ts[i]), R(ts[j]), 1.5)) out.push(['rótulos SVG sobrepostos', '"' + ts[i].textContent.trim().slice(0, 30) + '" x "' + ts[j].textContent.trim().slice(0, 30) + '"']);
    }
    const vr = R(svg);
    ts.forEach((t) => { const r = R(t); if (r.right > vr.right + 2 || r.left < vr.left - 2 || r.bottom > vr.bottom + 2 || r.top < vr.top - 2) out.push(['rótulo SVG fora da área', '"' + t.textContent.trim().slice(0, 40) + '"']); });
  });
  const fixed = [...document.querySelectorAll('body *')].filter((e) => getComputedStyle(e).position === 'fixed' && vis(e) && !e.closest('#deck') && R(e).width < 600);
  const leafs = [...content.querySelectorAll('p, li, h2, h3, button, td, a, label, input, select, code, .lab-kpi')].filter(vis);
  if (!s.classList.contains('slide-lab')) fixed.forEach((f) => { const fr = R(f); leafs.forEach((e) => { if (inter(R(e), fr, 2)) out.push(['sob a navegação', name(e)]); }); });
  const seen = new Set();
  return out.filter((x) => { const k = x.join('|'); if (seen.has(k)) return false; seen.add(k); return true; }).slice(0, 25);
}
"""

ADVANCE = r"""
async () => {
  const s = document.querySelector('#deck > section.slide.active');
  if (!s) return;
  for (const b of s.querySelectorAll('button')) {
    const t = (b.textContent || '').toLowerCase().trim();
    if (/executar tudo|^próximo|próximo passo|avançar/.test(t)) {
      for (let i = 0; i < 12; i++) { b.click(); await new Promise((r) => setTimeout(r, 60)); }
    }
  }
}
"""


def main() -> int:
    args = sys.argv[1:]
    shots = None
    size = (1280, 720)
    if "--shots" in args:
        i = args.index("--shots"); shots = Path(args[i + 1]); del args[i:i + 2]; shots.mkdir(parents=True, exist_ok=True)
    if "--size" in args:
        i = args.index("--size"); w, h = args[i + 1].split("x"); size = (int(w), int(h)); del args[i:i + 2]
    want = [int(a.replace("aula", "")) for a in args] or sorted(DECKS)
    total = 0
    with sync_playwright() as p:
        b = p.chromium.launch(args=["--use-gl=swiftshader", "--enable-unsafe-swiftshader"])
        for k in want:
            u = DECKS[k]
            pg = b.new_page(viewport={"width": size[0], "height": size[1]})
            errs: list[str] = []
            pg.on("pageerror", lambda e: errs.append(str(e)[:140]))
            pg.goto(f"{BASE}unidade_{u}/slides/aula{k}.html"); pg.wait_for_timeout(500)
            n = pg.evaluate("document.querySelectorAll('#deck > section.slide').length")
            for i in range(n):
                if i:
                    pg.keyboard.press("ArrowRight")
                pg.wait_for_timeout(600)
                pg.evaluate(ADVANCE)
                pg.wait_for_timeout(900)
                probs = pg.evaluate(JS)
                if shots:
                    pg.screenshot(path=str(shots / f"aula{k:02d}_s{i + 1:02d}.png"))
                for kind, what in probs:
                    print(f"aula{k} slide {i + 1}: {kind}: {what}")
                total += len(probs)
            for e in errs:
                print(f"aula{k}: erro JS: {e}"); total += 1
            pg.close()
        b.close()
    print(f"\n{total} ocorrência(s).")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
