// Slide audit harness — renders each deck in Chrome (1280x720), toggles each
// slide active, and measures content overflow + stray LaTeX leakage.
// Usage: node check.js
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright-core');

const REPO = path.resolve(__dirname, '..');
const DISC_NAME = process.argv[2] || 'data_engineering_and_pipelines';
const DISC = path.join(REPO, DISC_NAME);
const UNIT_DIRS = ['unidade_1', 'unidade_2', 'unidade_3', 'unidade_4'].map(
  (u) => path.join(DISC, u, 'slides')
);
const SHOTS = path.join(__dirname, 'shots', DISC_NAME);
fs.mkdirSync(SHOTS, { recursive: true });

function deckList() {
  const out = [];
  for (const d of UNIT_DIRS) {
    if (!fs.existsSync(d)) continue;
    for (const f of fs.readdirSync(d)) {
      if (f.endsWith('.html')) out.push(path.join(d, f));
    }
  }
  // sort by aula number
  return out.sort((a, b) => {
    const na = parseInt((a.match(/aula(\d+)\.html$/) || [])[1] ?? '0', 10);
    const nb = parseInt((b.match(/aula(\d+)\.html$/) || [])[1] ?? '0', 10);
    return na - nb;
  });
}

const AUDIT_FN = `(() => {
  const LATEX = /\\\\(mathrm|frac|times|approx|geq|leq|cdot|circ|left|right|begin|end|text|lceil|rceil|sqrt|sum|alpha|beta|mu|le|ge|,)\\b|\\\\,|\\^\\{|_\\{|\\{,\\}|\\\\\\(|\\\\\\[/;
  const slides = Array.from(document.querySelectorAll('.slide'));
  const res = [];
  for (let k = 0; k < slides.length; k++) {
    slides.forEach((s, i) => s.classList.toggle('active', i === k));
    const s = slides[k];
    // overflow at slide level (slide has overflow:hidden, so clipped content)
    let slideOver = s.scrollHeight - s.clientHeight;
    // overflow inside scrolling content containers
    let innerOver = 0, innerSel = '';
    s.querySelectorAll('.slide-content, .slide-content-box, .quote-card, .prof-lado-escuro, .sumario-lado-escuro, .audio-texto').forEach((el) => {
      const o = el.scrollHeight - el.clientHeight;
      if (o > innerOver) { innerOver = o; innerSel = el.className; }
    });
    const txt = s.innerText || '';
    const latex = LATEX.test(txt);
    const latexSample = latex ? (txt.match(LATEX) || [''])[0] : '';
    const cls = s.className.replace('active', '').trim();
    res.push({
      k,
      cls,
      slideOver: Math.round(slideOver),
      innerOver: Math.round(innerOver),
      innerSel,
      latex,
      latexSample,
      hasAudio: s.classList.contains('slide-audio'),
      hasProf: s.classList.contains('slide-prof'),
    });
  }
  // restore first slide
  slides.forEach((s, i) => s.classList.toggle('active', i === 0));
  return { count: slides.length, slides: res };
})()`;

(async () => {
  const browser = await chromium.launch({ channel: 'chrome', headless: true });
  const page = await browser.newPage({ viewport: { width: 1280, height: 720 }, deviceScaleFactor: 1 });
  const report = [];
  for (const deck of deckList()) {
    const rel = path.relative(DISC, deck).replace(/\\/g, '/');
    const aula = (deck.match(/aula\d+/) || ['?'])[0];
    try {
      await page.goto('file:///' + deck.replace(/\\/g, '/'), { waitUntil: 'networkidle' });
      const data = await page.evaluate(AUDIT_FN);
      const flagged = data.slides.filter((s) => s.slideOver > 2 || s.innerOver > 2 || s.latex);
      const hasAudio = data.slides.some((s) => s.hasAudio);
      const hasProf = data.slides.some((s) => s.hasProf);
      report.push({ deck: rel, aula, count: data.count, hasAudio, hasProf, flagged, slides: data.slides });
      // screenshot: cover + audio + prof + every flagged slide
      const special = data.slides.filter((s) => s.hasAudio || s.hasProf).map((s) => s.k);
      const toShoot = new Set([0, ...special, ...flagged.map((f) => f.k)]);
      for (const k of toShoot) {
        await page.evaluate((kk) => {
          const sl = Array.from(document.querySelectorAll('.slide'));
          sl.forEach((s, i) => s.classList.toggle('active', i === kk));
        }, k);
        await page.screenshot({ path: path.join(SHOTS, `${aula}_s${k}.png`) });
      }
      const fl = flagged.length;
      console.log(`${aula.padEnd(7)} slides=${String(data.count).padStart(2)}  audio=${hasAudio ? 'Y' : 'N'} prof=${hasProf ? 'Y' : 'N'}  flagged=${fl}` +
        (fl ? '  -> ' + flagged.map((f) => `s${f.k}[${f.cls || 'slide'}${f.slideOver > 2 ? ' over' + f.slideOver : ''}${f.innerOver > 2 ? ' inner' + f.innerOver : ''}${f.latex ? ' LATEX:' + f.latexSample : ''}]`).join(' ') : ''));
    } catch (e) {
      report.push({ deck: rel, aula, error: String(e) });
      console.log(`${aula.padEnd(7)} ERROR ${e}`);
    }
  }
  fs.writeFileSync(path.join(__dirname, 'report.json'), JSON.stringify(report, null, 2));
  await browser.close();
  // summary
  const noAudio = report.filter((r) => r.hasAudio === false).map((r) => r.aula);
  const noProf = report.filter((r) => r.hasProf === false).map((r) => r.aula);
  const withFlags = report.filter((r) => (r.flagged || []).length).map((r) => `${r.aula}(${r.flagged.length})`);
  console.log('\\n=== SUMMARY ===');
  console.log('decks sem Audiodescricao:', noAudio.join(', ') || 'nenhum');
  console.log('decks sem Sobre-o-professor:', noProf.join(', ') || 'nenhum');
  console.log('decks com overflow/LaTeX flagged:', withFlags.join(', ') || 'nenhum');
})();
