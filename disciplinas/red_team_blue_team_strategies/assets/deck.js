/* =====================================================================
   Navegação dos decks de Red Team & Blue Team Strategies.
   - setas, Page Up/Down, espaço, Home/End, F (tela cheia);
   - #N na URL abre o slide N;
   - dispara os eventos "slide:enter" e "slide:leave" em cada <section>,
     usados por labs.js para iniciar e pausar os laboratórios.
   ===================================================================== */
(function () {
  'use strict';
  // Favicon da disciplina (escudo vermelho, roxo e azul), servido ao lado deste arquivo
  if (!document.querySelector('link[rel~="icon"]')) {
    const me = document.currentScript && document.currentScript.src;
    const base = me ? me.replace(/deck\.js(\?.*)?$/, '') : '../../assets/';
    [['icon', 'favicon.svg', 'image/svg+xml'], ['alternate icon', 'favicon.png', 'image/png'], ['apple-touch-icon', 'favicon.png', 'image/png']].forEach(([rel, f, type]) => {
      const l = document.createElement('link'); l.rel = rel; l.href = base + f; l.type = type; document.head.appendChild(l);
    });
  }
  const deck = document.getElementById('deck');
  if (!deck) return;
  // Escala: o layout foi desenhado para 1280x720. Em telas maiores (1920x1080,
  // projetor 4K) a fonte-base cresce na mesma proporção, para o conteúdo
  // ocupar o slide em vez de ficar pequeno no meio. Nunca encolhe abaixo de 16px.
  const escala = () => {
    const s = Math.max(1, Math.min(2.2, Math.min(innerWidth / 1280, innerHeight / 720)));
    document.documentElement.style.fontSize = (16 * s).toFixed(2) + 'px';
    document.documentElement.style.setProperty('--escala', s.toFixed(3));
  };
  escala(); addEventListener('resize', escala);
  const slides = Array.from(deck.querySelectorAll(':scope > .slide'));

  // Botão "Início" (portal da disciplina)
  const home = document.createElement('a');
  home.className = 'btn-home';
  home.href = deck.dataset.home || '../../index.html';
  home.title = 'Voltar para o portal da disciplina';
  home.innerHTML = '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 11.5 12 4l9 7.5"/><path d="M5 10.5V20h5v-5.5h4V20h5v-9.5"/></svg><span>Início</span>';
  document.body.appendChild(home);

  // Barra de navegação
  const nav = document.createElement('nav');
  nav.className = 'nav';
  nav.setAttribute('aria-label', 'Navegação dos slides');
  nav.innerHTML = '<button id="prev" aria-label="Slide anterior">‹</button><span class="counter"><span id="cur">1</span> / <span id="total">1</span></span><button id="next" aria-label="Próximo slide">›</button><button id="fs" aria-label="Tela cheia" title="Tela cheia (F)">⛶</button>';
  document.body.appendChild(nav);
  // Navegação discreta: em slides de laboratório, a barra e o botão Início somem
  // depois de 2,5 s sem mexer o mouse, para não cobrir o canto do laboratório.
  // Voltam ao mover o mouse; o teclado continua funcionando o tempo todo.
  let idleT = null;
  const wake = () => {
    document.body.classList.remove('nav-idle');
    clearTimeout(idleT);
    idleT = setTimeout(() => {
      const ativo = document.querySelector('#deck > .slide.active');
      if (ativo && ativo.classList.contains('slide-lab') && !nav.matches(':hover') && !home.matches(':hover')) document.body.classList.add('nav-idle');
    }, 2500);
  };
  ['mousemove', 'pointerdown', 'touchstart'].forEach((ev) => document.addEventListener(ev, wake, { passive: true }));
  document.addEventListener('slide:enter', wake, true);
  wake();
  const cur = nav.querySelector('#cur'), prev = nav.querySelector('#prev'), next = nav.querySelector('#next');
  nav.querySelector('#total').textContent = slides.length;

  let i = -1;
  function show(n) {
    n = Math.max(0, Math.min(slides.length - 1, n));
    if (n === i) return;
    const old = slides[i];
    if (old) { old.classList.remove('active'); old.dispatchEvent(new CustomEvent('slide:leave')); }
    slides[n].classList.add('active');
    slides[n].scrollTop = 0;
    i = n;
    cur.textContent = n + 1;
    prev.disabled = n === 0;
    next.disabled = n === slides.length - 1;
    if (history.replaceState) history.replaceState(null, '', '#' + (n + 1));
    slides[n].dispatchEvent(new CustomEvent('slide:enter'));
  }
  window.Deck = { show, get index() { return i; }, slides };

  function fullscreen() {
    if (!document.fullscreenElement) document.documentElement.requestFullscreen?.();
    else document.exitFullscreen?.();
  }
  prev.addEventListener('click', () => show(i - 1));
  next.addEventListener('click', () => show(i + 1));
  nav.querySelector('#fs').addEventListener('click', fullscreen);

  document.addEventListener('keydown', (e) => {
    const t = e.target instanceof Element ? e.target : null;
    if (e.defaultPrevented || e.ctrlKey || e.metaKey || e.altKey) return;
    if (t && t.closest('input, textarea, select, [contenteditable="true"], .no-nav')) return;
    if (e.key === 'ArrowRight' || e.key === 'PageDown' || (e.key === ' ' && !(t && t.closest('button')))) { e.preventDefault(); show(i + 1); }
    else if (e.key === 'ArrowLeft' || e.key === 'PageUp') { e.preventDefault(); show(i - 1); }
    else if (e.key === 'Home') show(0);
    else if (e.key === 'End') show(slides.length - 1);
    else if (e.key === 'f' || e.key === 'F') fullscreen();
  });

  // Rodapé dos slides de conteúdo: disciplina · unidade | aula
  const rodape = deck.dataset.footer;
  if (rodape) {
    const [esq, dir] = rodape.split('|');
    slides.forEach((s) => {
      if (s.querySelector('.slide-footer') || !s.querySelector('.mosaico-bg')) return;
      const f = document.createElement('div');
      f.className = 'slide-footer';
      f.innerHTML = '<span>' + (esq || '') + '</span><span>' + (dir || '') + '</span>';
      s.appendChild(f);
    });
  }

  window.addEventListener('hashchange', () => {
    const n = parseInt(location.hash.replace('#', ''), 10);
    if (!isNaN(n) && n - 1 !== i) show(n - 1);
  });
  const h = parseInt(location.hash.replace('#', ''), 10);
  // Espera labs.js registrar os laboratórios antes do primeiro slide:enter
  window.addEventListener('DOMContentLoaded', () => show(!isNaN(h) && h >= 1 && h <= slides.length ? h - 1 : 0));
  if (document.readyState !== 'loading') setTimeout(() => { if (i < 0) show(!isNaN(h) && h >= 1 ? h - 1 : 0); }, 0);
})();
