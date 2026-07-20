(() => {
  'use strict';

  const root = document.documentElement;
  const canEnter = root.requestFullscreen || root.webkitRequestFullscreen;
  const canExit = document.exitFullscreen || document.webkitExitFullscreen;

  if (!canEnter || !canExit || document.querySelector('[data-fullscreen-button]')) return;

  const style = document.createElement('style');
  style.textContent = `
    .fullscreen-button {
      position: fixed;
      right: max(18px, env(safe-area-inset-right));
      bottom: max(18px, env(safe-area-inset-bottom));
      z-index: 2147483647;
      display: grid;
      place-items: center;
      width: 46px;
      height: 46px;
      padding: 0;
      border: 1px solid rgba(255, 255, 255, .4);
      border-radius: 50%;
      color: #fff;
      background: rgba(0, 32, 87, .9);
      box-shadow: 0 5px 18px rgba(0, 0, 0, .3);
      cursor: pointer;
      -webkit-backdrop-filter: blur(8px);
      backdrop-filter: blur(8px);
      transition: transform .18s ease, background .18s ease, box-shadow .18s ease;
    }
    .fullscreen-button:hover {
      background: #1f44a8;
      box-shadow: 0 7px 22px rgba(0, 0, 0, .38);
      transform: translateY(-2px);
    }
    .fullscreen-button:active { transform: translateY(0) scale(.96); }
    .fullscreen-button:focus-visible {
      outline: 3px solid #f0ce29;
      outline-offset: 3px;
    }
    .fullscreen-button svg { width: 22px; height: 22px; pointer-events: none; }
    .fullscreen-button .icon-compress { display: none; }
    .fullscreen-button[aria-pressed="true"] .icon-expand { display: none; }
    .fullscreen-button[aria-pressed="true"] .icon-compress { display: block; }
    .fullscreen-button.with-slide-nav {
      bottom: max(78px, calc(62px + env(safe-area-inset-bottom)));
    }
    @media (max-width: 600px) {
      .fullscreen-button { width: 42px; height: 42px; }
    }
    @media (prefers-reduced-motion: reduce) {
      .fullscreen-button { transition: none; }
    }
    @media print {
      .fullscreen-button { display: none; }
    }
  `;

  const button = document.createElement('button');
  button.type = 'button';
  button.className = 'fullscreen-button';
  if (document.querySelector('.nav')) button.classList.add('with-slide-nav');
  button.dataset.fullscreenButton = '';
  button.setAttribute('aria-label', 'Entrar em tela cheia');
  button.setAttribute('aria-pressed', 'false');
  button.title = 'Entrar em tela cheia';
  button.innerHTML = `
    <svg class="icon-expand" viewBox="0 0 24 24" aria-hidden="true">
      <path d="M8 3H3v5M16 3h5v5M8 21H3v-5M16 21h5v-5" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
    <svg class="icon-compress" viewBox="0 0 24 24" aria-hidden="true">
      <path d="M8 3v5H3M16 3v5h5M8 21v-5H3M16 21v-5h5" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
  `;

  const isFullscreen = () => Boolean(document.fullscreenElement || document.webkitFullscreenElement);

  const syncButton = () => {
    const active = isFullscreen();
    const label = active ? 'Sair da tela cheia' : 'Entrar em tela cheia';
    button.setAttribute('aria-pressed', String(active));
    button.setAttribute('aria-label', label);
    button.title = label;
  };

  button.addEventListener('click', async () => {
    try {
      if (isFullscreen()) {
        await (document.exitFullscreen ? document.exitFullscreen() : document.webkitExitFullscreen());
      } else {
        await (root.requestFullscreen ? root.requestFullscreen() : root.webkitRequestFullscreen());
      }
    } catch (error) {
      console.warn('Não foi possível alternar o modo de tela cheia.', error);
    }
  });

  document.addEventListener('fullscreenchange', syncButton);
  document.addEventListener('webkitfullscreenchange', syncButton);
  document.head.appendChild(style);
  document.body.appendChild(button);
  syncButton();
})();
