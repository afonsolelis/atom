(() => {
  'use strict';

  const root = document.documentElement;
  const deck = document.getElementById('deck');
  const nav = document.querySelector('.nav');
  const lessonMatch = location.pathname.match(/aula(\d+)\.html$/i);
  const lesson = lessonMatch ? Number(lessonMatch[1]) : null;

  const style = document.createElement('style');
  style.dataset.slideEnhancements = '';
  style.textContent = `
    .sr-only {
      position: absolute !important;
      width: 1px !important;
      height: 1px !important;
      padding: 0 !important;
      margin: -1px !important;
      overflow: hidden !important;
      clip: rect(0, 0, 0, 0) !important;
      white-space: nowrap !important;
      border: 0 !important;
    }

    .slide.active {
      overflow-x: hidden;
      overflow-y: auto;
      overscroll-behavior: contain;
      scrollbar-gutter: stable;
    }
    .mosaico-bg ~ .slide-content {
      max-height: none !important;
      overflow: visible !important;
      justify-content: flex-start;
    }
    /* O cartão de conteúdo ganha corpo em vez de flutuar como uma tarja no topo */
    .mosaico-bg ~ .slide-content > .slide-content-box {
      flex: 1 1 auto;
      display: flex;
      flex-direction: column;
      justify-content: center;
      gap: .55rem;
      min-height: 0;
      padding: 1.6em 2em;
    }
    .mosaico-bg ~ .slide-content > .slide-content-box > :last-child { margin-bottom: 0; }

    /* Destaque azul dentro do cartão claro — o cartão claro escurece o texto por herança */
    .slide-content-box .callout-azul,
    .slide-content-box .callout-azul p,
    .slide-content-box .callout-azul li { color: #fff !important; }
    .slide-content-box .callout-azul strong { color: #f2cb0a !important; }
    .slide-content-box .callout-azul em { color: #9fe3ff !important; }
    .callout-azul > :last-child { margin-bottom: 0 !important; }
    .callout-azul p { font-size: clamp(.96rem, 1.16vw, 1.18rem) !important; line-height: 1.45; }

    /* Bloco de código (manifestos, contratos) */
    .bloco-codigo { margin: 0; }
    .bloco-codigo figcaption {
      margin-bottom: .4rem;
      color: #4a5368;
      font-family: var(--fonte-titulo, 'Poppins', 'Montserrat', Arial, sans-serif);
      font-size: .78rem;
      font-weight: 700;
      letter-spacing: .06em;
      text-transform: uppercase;
    }
    .bloco-codigo pre {
      margin: 0;
      padding: 1rem 1.15rem;
      border-radius: 12px;
      border-left: 6px solid #f2cb0a;
      color: #eaf1ff;
      background: #002156;
      overflow-x: auto;
    }
    /* Especificidade maior que a regra genérica de code, definida adiante */
    .bloco-codigo pre code {
      font-family: 'JetBrains Mono', 'Fira Mono', Consolas, monospace;
      font-size: clamp(.78rem, .95vw, .98rem);
      line-height: 1.5;
      white-space: pre;
      overflow-wrap: normal;
      word-break: normal;
    }

    /* Fórmula em destaque */
    .callout-azul.formula { text-align: center; border-left-width: 0; border-top: 6px solid #f2cb0a; }
    .callout-azul.formula p {
      font-size: clamp(1.25rem, 2.1vw, 1.95rem) !important;
      font-weight: 700;
      letter-spacing: .01em;
      line-height: 1.3;
    }
    .slide svg { max-width: 100%; }
    .slide-content,
    .slide-content-box {
      min-width: 0;
      max-width: 100%;
    }
    .slide h1,
    .slide h2,
    .slide h3,
    .slide p,
    .slide li {
      overflow-wrap: anywhere;
    }
    .slide-content-box code {
      white-space: normal;
      overflow-wrap: anywhere;
      word-break: break-word;
    }
    .slide-content-box pre {
      max-width: 100%;
      overflow-x: auto;
    }

    /* Escala tipográfica do conteúdo — o texto precisa ocupar a tela de projeção */
    .slide-content-box p,
    .slide-content-box li { font-size: clamp(1rem, 1.26vw, 1.32rem); line-height: 1.5; }
    .slide-content-box h3 { font-size: clamp(1rem, 1.22vw, 1.22rem); }
    .ponto p { font-size: clamp(.95rem, 1.12vw, 1.12rem) !important; }
    .ponto h3 { font-size: clamp(1rem, 1.18vw, 1.18rem) !important; }
    /* Grade fixa evita a última linha com um cartão órfão */
    .pontos-chave { grid-template-columns: repeat(3, minmax(0, 1fr)); }
    .pontos-chave:has(.ponto:nth-child(4):last-child) { grid-template-columns: repeat(2, minmax(0, 1fr)); }
    @media (max-width: 900px) { .pontos-chave { grid-template-columns: repeat(2, minmax(0, 1fr)) !important; } }
    @media (max-width: 600px) { .pontos-chave { grid-template-columns: 1fr !important; } }

    .visual-diagram {
      --visual-accent: #254ab9;
      --visual-accent-2: #00b1d2;
      position: relative;
      isolation: isolate;
      border: 1px solid rgba(31, 68, 168, .18);
      background:
        radial-gradient(circle at 100% 0, rgba(43,187,224,.13), transparent 34%),
        linear-gradient(145deg, #fff, #f7faff);
    }
    .visual-diagram::before {
      content: attr(data-visual-caption);
      display: inline-flex;
      align-items: center;
      min-height: 1.8rem;
      margin: 0 0 .75rem;
      padding: .25rem .72rem;
      border-radius: 999px;
      color: #fff;
      background: var(--visual-accent);
      font-family: var(--fonte-titulo, 'Poppins', 'Montserrat', Arial, sans-serif);
      font-size: .72rem;
      font-weight: 800;
      letter-spacing: .08em;
      text-transform: uppercase;
    }
    .visual-diagram > p {
      max-width: none;
      margin-bottom: .8rem;
      font-size: clamp(.98rem, 1.2vw, 1.24rem);
    }
    .visual-diagram > ul,
    .visual-diagram > ol {
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: .7rem;
      padding: 0;
      margin: 0;
      list-style: none;
      counter-reset: visual-item;
    }
    .visual-diagram > ul > li,
    .visual-diagram > ol > li {
      counter-increment: visual-item;
      position: relative;
      min-width: 0;
      min-height: 4rem;
      margin: 0;
      padding: .85rem .95rem .85rem 2.85rem;
      border: 1px solid rgba(31,68,168,.14);
      border-left: 4px solid var(--visual-accent-2);
      border-radius: 12px;
      background: rgba(255,255,255,.95);
      box-shadow: 0 4px 13px rgba(0,32,87,.07);
      font-size: clamp(.94rem, 1.1vw, 1.16rem) !important;
      line-height: 1.42 !important;
    }
    .visual-diagram > ul > li::before,
    .visual-diagram > ol > li::before {
      content: counter(visual-item);
      position: absolute;
      top: .8rem;
      left: .8rem;
      display: grid;
      place-items: center;
      width: 1.35rem;
      height: 1.35rem;
      border-radius: 50%;
      color: #fff;
      background: var(--visual-accent);
      font-size: .72rem;
      font-weight: 800;
    }
    /* Cinco ou mais itens em uma linha só ficam estreitos demais: quebra em 3 colunas */
    .visual-diagram > ul:has(> li:nth-child(5)),
    .visual-diagram > ol:has(> li:nth-child(5)) { grid-template-columns: repeat(3, minmax(0, 1fr)); }
    .visual-diagram strong { color: #9f174d !important; }
    .visual-timeline::before, .visual-metric::before { color: #002156; }

    .visual-flow > ul,
    .visual-timeline > ul,
    .visual-cycle > ul {
      display: flex;
      align-items: stretch;
      gap: 1.2rem;
    }
    .visual-flow > ul > li,
    .visual-timeline > ul > li,
    .visual-cycle > ul > li { flex: 1 1 0; }
    .visual-flow > ul > li:not(:last-child)::after,
    .visual-timeline > ul > li:not(:last-child)::after {
      content: '→';
      position: absolute;
      top: 50%;
      right: -1.05rem;
      z-index: 2;
      translate: 0 -50%;
      color: var(--visual-accent);
      font-size: 1.3rem;
      font-weight: 900;
    }
    .visual-timeline { --visual-accent: #11a360; --visual-accent-2: #95de68; }
    .visual-timeline > ul { border-top: 4px solid rgba(31,138,78,.28); padding-top: .75rem; }
    .visual-cycle { --visual-accent: #351b65; --visual-accent-2: #00b1d2; }
    .visual-cycle > ul > li { border-radius: 22px; }
    .visual-cycle > ul > li:not(:last-child)::after {
      content: '↻';
      position: absolute;
      right: -.92rem;
      bottom: -.35rem;
      z-index: 2;
      color: var(--visual-accent);
      font-size: 1.25rem;
      font-weight: 900;
    }
    .visual-compare { --visual-accent: #c2185b; --visual-accent-2: #f2cb0a; }
    .visual-compare > ul > li:nth-child(odd) { border-top: 4px solid #00b1d2; }
    .visual-compare > ul > li:nth-child(even) { border-top: 4px solid #f2cb0a; }
    .visual-map { --visual-accent: #002156; --visual-accent-2: #95de68; }
    .visual-map > ul { grid-template-columns: repeat(auto-fit, minmax(185px, 1fr)); }
    .visual-map > ul > li { border-left-width: 8px; }
    .visual-metric { --visual-accent: #11a360; --visual-accent-2: #f2cb0a; }
    .visual-metric > ul > li,
    .visual-metric .stat-card {
      text-align: center;
      border-top: 5px solid var(--visual-accent-2);
    }
    .visual-triangle { --visual-accent: #254ab9; --visual-accent-2: #ff2b5f; }
    .visual-triangle > ul { grid-template-columns: repeat(3, minmax(0, 1fr)); }
    .visual-triangle > ul > li { border-top: 6px solid var(--visual-accent-2); border-left-width: 1px; }
    .visual-pyramid { --visual-accent: #9f174d; --visual-accent-2: #f2cb0a; }
    .visual-pyramid > ul { display: flex; flex-direction: column-reverse; align-items: center; }
    .visual-pyramid > ul > li:nth-child(1) { width: 100%; }
    .visual-pyramid > ul > li:nth-child(2) { width: 78%; }
    .visual-pyramid > ul > li:nth-child(3) { width: 56%; }
    .visual-pyramid > ul > li:nth-child(n+4) { width: 42%; }

    .unit-overview {
      margin-top: 1.15rem;
      padding: 1rem 1.1rem;
      border-left: 6px solid #11a360;
      border-radius: 10px;
      color: #002156;
      background: #eef8ee;
      box-shadow: 0 5px 16px rgba(0,32,87,.08);
    }
    .unit-overview strong {
      display: block;
      margin-bottom: .35rem;
      color: #002156;
      font-family: var(--fonte-titulo, 'Poppins', 'Montserrat', Arial, sans-serif);
      font-size: .82rem;
      letter-spacing: .06em;
      text-transform: uppercase;
    }
    .unit-overview p { margin: 0; color: #23314f; font-size: clamp(.88rem, 1.05vw, 1.05rem); line-height: 1.38; }

    .reference-list {
      display: grid;
      gap: .65rem;
      margin: .2rem 0 0;
      padding-left: 1.4rem;
    }
    .reference-list li {
      margin: 0;
      font-size: clamp(.78rem, .95vw, .98rem) !important;
      line-height: 1.35 !important;
    }
    .reference-note { margin-top: .9rem !important; color: #4a5368 !important; font-size: .8rem !important; }

    /* Contador de progresso do slide, no canto superior direito do cartão */
    .slide-progresso {
      position: absolute;
      top: 1.35rem;
      right: 2.4rem;
      z-index: 3;
      margin: 0 !important;
      color: rgba(255,255,255,.6);
      font-size: .8rem !important;
      font-weight: 600;
      letter-spacing: .06em;
      white-space: nowrap;
    }

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
    .fullscreen-button:hover { background: #254ab9; box-shadow: 0 7px 22px rgba(0,0,0,.38); transform: translateY(-2px); }
    .fullscreen-button:active { transform: translateY(0) scale(.96); }
    .fullscreen-button:focus-visible { outline: 3px solid #f2cb0a; outline-offset: 3px; }
    .nav button:focus-visible, .btn-home:focus-visible { outline: 3px solid #f2cb0a; outline-offset: 3px; }
    .fullscreen-button svg { width: 22px; height: 22px; pointer-events: none; }
    .fullscreen-button .icon-compress { display: none; }
    .fullscreen-button[aria-pressed="true"] .icon-expand { display: none; }
    .fullscreen-button[aria-pressed="true"] .icon-compress { display: block; }
    .fullscreen-button.with-slide-nav { bottom: max(78px, calc(62px + env(safe-area-inset-bottom))); }

    @media (max-width: 900px), (max-height: 680px) {
      .slide.active { justify-content: flex-start; padding: 4vh 5vw 96px !important; }
      .slide:has(.mosaico-bg) { padding: 3vh 3.5vw 96px !important; }
      .mosaico-bg ~ .slide-content { flex: 0 0 auto !important; width: 100%; padding: 1rem 1.15rem 1.25rem !important; }
      .slide-content-box { padding: 1rem 1.1rem !important; }
      .slide-capa.active { justify-content: center; }
      .slide-capa .logo-marca { margin-bottom: 1.2rem; }
      .slide-sumario.active, .slide-prof.active { padding: 0 !important; }
      .sumario-grid, .prof-grid { grid-template-columns: 1fr; height: auto; min-height: 100%; }
      .sumario-lado-claro, .sumario-lado-escuro, .prof-lado-claro, .prof-lado-escuro { min-height: auto; padding: 2rem 7vw; }
      .sumario-titulo { margin: 1.2rem 0 0; padding: 0; }
      .sumario-lado-escuro { padding-bottom: 96px; }
      .prof-foto { max-width: 280px; }
      .slide-fim .slide-content { margin-top: 18vh; }
      .fim-cluster-base { opacity: .45; }
      .visual-flow > ul, .visual-timeline > ul, .visual-cycle > ul { display: grid; grid-template-columns: repeat(2, minmax(0,1fr)); gap: .7rem; }
      .visual-flow > ul > li::after, .visual-timeline > ul > li::after, .visual-cycle > ul > li::after { display: none; }
      .visual-pyramid > ul > li { width: 100% !important; }
      .mosaico-bg ~ .slide-content > .slide-content-box { flex: 0 0 auto; justify-content: flex-start; }
      .slide-progresso { top: .8rem; right: 1.2rem; }
    }
    @media (min-width: 901px) and (max-height: 800px) {
      .slide-quote .quote-card { padding: 1.25rem 2rem; }
      .slide-quote blockquote { font-size: clamp(1.25rem, 2.15vw, 1.85rem); }
      .slide-quote cite { margin-top: .65rem; }
    }
    @media (max-width: 600px) {
      .slide h1 { font-size: clamp(1.85rem, 9vw, 2.7rem); }
      .slide h2 { font-size: clamp(1.35rem, 7vw, 2rem); }
      .slide p, .slide li { font-size: .96rem; }
      .slide-audio h1 { font-size: clamp(1.6rem, 8vw, 2.2rem); }
      .capa-canto { width: 145px; height: 145px; opacity: .55; }
      .slide-capa .logo-marca svg { width: min(270px, 80vw); height: auto; }
      .visual-diagram > ul, .visual-diagram > ol,
      .visual-flow > ul, .visual-timeline > ul, .visual-cycle > ul,
      .visual-triangle > ul { grid-template-columns: 1fr; }
      .visual-diagram > ul > li, .visual-diagram > ol > li { min-height: 0; }
      .btn-home { width: 42px; height: 42px; justify-content: center; padding: 0; }
      .btn-home span { display: none; }
      .nav { left: 50%; right: auto; bottom: max(10px, env(safe-area-inset-bottom)); transform: translateX(-50%); }
      .fullscreen-button { width: 42px; height: 42px; }
      .slide-progresso { display: none; }
    }
    @media (prefers-reduced-motion: reduce) { .fullscreen-button { transition: none; } }
    @media print {
      .fullscreen-button, .slide-announcer { display: none !important; }
      .slide { overflow: hidden !important; }
    }
  `;
  document.head.appendChild(style);

  const VISUAL_TYPES = {
    0: ['map', 'timeline', 'map', 'map', 'flow'],
    1: ['map', 'compare', 'map', 'metric', 'compare'],
    2: ['compare', 'map', 'flow', 'timeline', 'flow'],
    3: ['timeline', 'metric', 'flow', 'timeline', 'compare'],
    4: ['map', 'map', 'compare', 'cycle', 'compare'],
    5: ['map', 'compare', 'timeline', 'compare', 'flow'],
    6: ['map', 'compare', 'metric', 'map', 'triangle'],
    7: ['map', 'metric', 'cycle', 'timeline', 'compare'],
    8: ['compare', 'flow', 'compare', 'flow', 'flow'],
    9: ['compare', 'compare', 'metric', 'map', 'flow'],
    10: ['flow', 'compare', 'map', 'metric', 'timeline'],
    11: ['flow', 'compare', 'map', 'cycle', 'cycle'],
    12: ['map', 'map', 'compare', 'flow', 'map'],
    13: ['flow', 'compare', 'map', 'flow', 'metric'],
    14: ['flow', 'pyramid', 'compare', 'cycle', 'map'],
    15: ['flow', 'compare', 'flow', 'metric', 'timeline'],
    16: ['map', 'compare', 'flow', 'map', 'compare']
  };
  const VISUAL_LABELS = {
    map: 'Mapa conceitual', compare: 'Quadro comparativo', flow: 'Fluxo de decisão',
    timeline: 'Sequência temporal', metric: 'Painel numérico', cycle: 'Ciclo operacional',
    triangle: 'Triângulo de decisões', pyramid: 'Pirâmide de testes'
  };

  const REFERENCES = {
    1: [
      'COULOURIS, George et al. Distributed systems: concepts and design. 5. ed. Boston: Addison-Wesley, 2012.',
      'TANENBAUM, Andrew S.; VAN STEEN, Maarten. Distributed systems. 3. ed. [S. l.]: Maarten van Steen, 2017.',
      'KLEPPMANN, Martin. Designing data-intensive applications. Sebastopol: O’Reilly, 2017.'
    ],
    2: [
      'FIELDING, Roy T. Architectural styles and the design of network-based software architectures. Irvine: University of California, 2000.',
      'IETF. RFC 9110: HTTP semantics. [S. l.]: Internet Engineering Task Force, 2022.',
      'HOHPE, Gregor; WOOLF, Bobby. Enterprise integration patterns. Boston: Addison-Wesley, 2003.'
    ],
    3: [
      'LAMPORT, Leslie. Time, clocks, and the ordering of events in a distributed system. Communications of the ACM, v. 21, n. 7, p. 558–565, 1978.',
      'FIDGE, Colin J. Timestamps in message-passing systems that preserve the partial ordering. Canberra: Australian National University, 1988.',
      'MATTERN, Friedemann. Virtual time and global states of distributed systems. In: PARALLEL AND DISTRIBUTED ALGORITHMS, 1989. Proceedings […]. Amsterdam: North-Holland, 1989.'
    ],
    4: [
      'AVIZIENIS, Algirdas et al. Basic concepts and taxonomy of dependable and secure computing. IEEE Transactions on Dependable and Secure Computing, v. 1, n. 1, p. 11–33, 2004.',
      'CHANDRA, Tushar D.; TOUEG, Sam. Unreliable failure detectors for reliable distributed systems. Journal of the ACM, v. 43, n. 2, p. 225–267, 1996.',
      'NYGARD, Michael T. Release it! 2. ed. Raleigh: Pragmatic Bookshelf, 2018.'
    ],
    5: [
      'TERRY, Douglas B. et al. Session guarantees for weakly consistent replicated data. In: INTERNATIONAL CONFERENCE ON PARALLEL AND DISTRIBUTED INFORMATION SYSTEMS, 1994. Proceedings […]. Los Alamitos: IEEE, 1994.',
      'VOGELS, Werner. Eventually consistent. Communications of the ACM, v. 52, n. 1, p. 40–44, 2009.',
      'KLEPPMANN, Martin. Designing data-intensive applications. Sebastopol: O’Reilly, 2017.'
    ],
    6: [
      'KARGER, David et al. Consistent hashing and random trees. In: ACM SYMPOSIUM ON THEORY OF COMPUTING, 29., 1997. Proceedings […]. New York: ACM, 1997.',
      'GILBERT, Seth; LYNCH, Nancy. Brewer’s conjecture and the feasibility of consistent, available, partition-tolerant web services. SIGACT News, v. 33, n. 2, p. 51–59, 2002.',
      'ABADI, Daniel. Consistency tradeoffs in modern distributed database system design. Computer, v. 45, n. 2, p. 37–42, 2012.'
    ],
    7: [
      'ONGARO, Diego; OUSTERHOUT, John. In search of an understandable consensus algorithm. In: USENIX ANNUAL TECHNICAL CONFERENCE, 2014. Proceedings […]. Berkeley: USENIX, 2014.',
      'FISCHER, Michael J.; LYNCH, Nancy A.; PATERSON, Michael S. Impossibility of distributed consensus with one faulty process. Journal of the ACM, v. 32, n. 2, p. 374–382, 1985.',
      'LAMPORT, Leslie. The part-time parliament. ACM Transactions on Computer Systems, v. 16, n. 2, p. 133–169, 1998.'
    ],
    8: [
      'GARCIA-MOLINA, Hector; SALEM, Kenneth. Sagas. In: ACM SIGMOD INTERNATIONAL CONFERENCE, 1987. Proceedings […]. New York: ACM, 1987.',
      'GRAY, Jim; LAMPORT, Leslie. Consensus on transaction commit. ACM Transactions on Database Systems, v. 31, n. 1, p. 133–160, 2006.',
      'RICHARDSON, Chris. Microservices patterns. Shelter Island: Manning, 2018.'
    ],
    9: [
      'EVANS, Eric. Domain-driven design. Boston: Addison-Wesley, 2003.',
      'NEWMAN, Sam. Building microservices. 2. ed. Sebastopol: O’Reilly, 2021.',
      'MARTIN, Robert C. Agile software development: principles, patterns, and practices. Upper Saddle River: Prentice Hall, 2002.'
    ],
    10: [
      'HOHPE, Gregor; WOOLF, Bobby. Enterprise integration patterns. Boston: Addison-Wesley, 2003.',
      'KREPS, Jay; NARKHEDE, Neha; RAO, Jun. Kafka: a distributed messaging system for log processing. In: NETDB, 2011. Proceedings […]. [S. l.: s. n.], 2011.',
      'KLEPPMANN, Martin. Designing data-intensive applications. Sebastopol: O’Reilly, 2017.'
    ],
    11: [
      'BURNS, Brendan et al. Borg, Omega, and Kubernetes. Communications of the ACM, v. 59, n. 5, p. 50–57, 2016.',
      'HIGHTOWER, Kelsey; BURNS, Brendan; BEDA, Joe. Kubernetes: up and running. 3. ed. Sebastopol: O’Reilly, 2022.',
      'THE KUBERNETES AUTHORS. Kubernetes documentation. [S. l.]: Cloud Native Computing Foundation, 2026.'
    ],
    12: [
      'NIST. Zero trust architecture: SP 800-207. Gaithersburg: National Institute of Standards and Technology, 2020.',
      'IETF. RFC 8446: the transport layer security (TLS) protocol version 1.3. [S. l.]: Internet Engineering Task Force, 2018.',
      'SPIFFE. Secure Production Identity Framework for Everyone: specification. [S. l.]: Cloud Native Computing Foundation, 2026.'
    ],
    13: [
      'SIGELMAN, Benjamin H. et al. Dapper, a large-scale distributed systems tracing infrastructure. [S. l.]: Google, 2010.',
      'BEYER, Betsy et al. Site reliability engineering. Sebastopol: O’Reilly, 2016.',
      'OPEN TELEMETRY. OpenTelemetry specification. [S. l.]: Cloud Native Computing Foundation, 2026.'
    ],
    14: [
      'ROSENTHAL, Casey; JONES, Nora. Chaos engineering. Sebastopol: O’Reilly, 2020.',
      'BEYER, Betsy et al. Site reliability engineering. Sebastopol: O’Reilly, 2016.',
      'BASIRI, Ali et al. Chaos engineering. IEEE Software, v. 33, n. 3, p. 35–41, 2016.'
    ],
    15: [
      'DEAN, Jeffrey; GHEMAWAT, Sanjay. MapReduce: simplified data processing on large clusters. In: OSDI, 6., 2004. Proceedings […]. Berkeley: USENIX, 2004.',
      'AKIDAU, Tyler et al. The dataflow model. Proceedings of the VLDB Endowment, v. 8, n. 12, p. 1792–1803, 2015.',
      'KLEPPMANN, Martin. Designing data-intensive applications. Sebastopol: O’Reilly, 2017.'
    ],
    16: [
      'BASS, Len; CLEMENTS, Paul; KAZMAN, Rick. Software architecture in practice. 4. ed. Boston: Addison-Wesley, 2021.',
      'ISO; IEC. ISO/IEC 25010: systems and software quality models. Geneva: ISO, 2023.',
      'NYGARD, Michael. Documenting architecture decisions. [S. l.]: Cognitect, 2011.'
    ]
  };

  const UNIT_OVERVIEWS = {
    1: 'Fundamentos do pensamento distribuído; comunicação entre processos; tempo e ordenação; falhas parciais e recuperação.',
    5: 'Replicação e consistência; particionamento e CAP; consenso com Raft; transações distribuídas, sagas e idempotência.',
    9: 'Limites de domínio e serviços; arquitetura orientada a eventos; Kubernetes e reconciliação; identidade e comunicação segura.',
    13: 'Observabilidade; testes de resiliência e caos; processamento em lote e fluxo; avaliação arquitetural integrada.'
  };

  const FOREIGN_TERM_PATTERN = /(?<![\p{L}\p{N}])(at-most-once|at-least-once|exactly-once|read-your-writes|last-writer-wins|sloppy quorums?|peer-to-peer|scatter-gather|split-brain|cloud-native|service mesh|circuit breakers?|cold start|happened-before|replication lag|round-trip|scale-out|scale-up|throughput|timeouts?|retries|retry|backoff|jitter|failover|bulkhead|fallbacks?|safety|liveness|appendentries|outbox|inbox|replay|postmortem|watermark|serverless|frameworks?|pipelines?|gateways?|brokers?|proxies?|threads?|clusters?|hashing|sharding|traces?|spans?|logs?|batch|shuffle|reduce|jobs?|edge|cache)(?![\p{L}\p{N}])/giu;

  function italicizeForeignTerms() {
    if (!deck) return;
    const walker = document.createTreeWalker(deck, NodeFilter.SHOW_TEXT);
    const nodes = [];
    while (walker.nextNode()) nodes.push(walker.currentNode);
    nodes.forEach(node => {
      const parent = node.parentElement;
      if (!parent || parent.closest('em, code, pre, script, style, svg, [aria-hidden="true"]')) return;
      FOREIGN_TERM_PATTERN.lastIndex = 0;
      if (!FOREIGN_TERM_PATTERN.test(node.data)) return;
      FOREIGN_TERM_PATTERN.lastIndex = 0;
      const fragment = document.createDocumentFragment();
      let cursor = 0;
      for (const match of node.data.matchAll(FOREIGN_TERM_PATTERN)) {
        fragment.append(node.data.slice(cursor, match.index));
        const emphasis = document.createElement('em');
        emphasis.textContent = match[0];
        fragment.append(emphasis);
        cursor = match.index + match[0].length;
      }
      fragment.append(node.data.slice(cursor));
      node.replaceWith(fragment);
    });
  }

  function contentFooter() {
    if (!Number.isInteger(lesson) || lesson < 1) return '';
    const unit = Math.floor((lesson - 1) / 4) + 1;
    return `<div class="slide-footer"><span>Distributed Systems Engineering · Unidade ${unit}</span><span>Aula ${lesson} — Videoaula ${lesson}</span></div>`;
  }

  function addUnitOverview() {
    const text = UNIT_OVERVIEWS[lesson];
    if (!text || document.querySelector('.unit-overview')) return;
    const host = document.querySelector('.slide-sumario .sumario-lado-claro');
    if (!host) return;
    const overview = document.createElement('div');
    overview.className = 'unit-overview';
    overview.setAttribute('role', 'note');
    overview.innerHTML = `<strong>O que você verá nesta unidade</strong><p>${text}</p>`;
    host.appendChild(overview);
  }

  function addReferenceSlide() {
    const references = REFERENCES[lesson];
    if (!references || document.querySelector('.slide-referencias')) return;
    const ending = document.querySelector('.slide-fim');
    if (!ending) return;
    const section = document.createElement('section');
    section.className = 'slide slide-referencias';
    const items = references.map(reference => `<li>${reference}</li>`).join('');
    section.innerHTML = `
      <div class="mosaico-bg"><svg preserveAspectRatio="none" aria-hidden="true"><use href="#mosaico-frame"></use></svg></div>
      <div class="slide-content">
        <p class="kicker">Fundamentação</p>
        <h2>Referências essenciais</h2>
        <div class="slide-content-box">
          <ol class="reference-list">${items}</ol>
          <p class="reference-note">Organização bibliográfica orientada pela ABNT NBR 6023:2018.</p>
        </div>
      </div>
      ${contentFooter()}`;
    ending.before(section);
  }

  // Numera os slides dentro do cartão de conteúdo (ex.: "07 / 22").
  function numberSlides() {
    if (!deck) return;
    const slides = [...deck.querySelectorAll(':scope > .slide')];
    const total = String(slides.length).padStart(2, '0');
    slides.forEach((slide, index) => {
      if (slide.matches('.slide-capa, .slide-audio, .slide-prof, .slide-fim')) return;
      if (slide.querySelector('.slide-progresso')) return;
      const badge = document.createElement('p');
      badge.className = 'slide-progresso';
      badge.setAttribute('aria-hidden', 'true');
      badge.textContent = `${String(index + 1).padStart(2, '0')} / ${total}`;
      (slide.querySelector(':scope > .slide-content') || slide).appendChild(badge);
    });
  }

  function enhanceVisuals() {
    const types = VISUAL_TYPES[lesson] || [];
    const figures = [...document.querySelectorAll('.slide-content-box.visual-diagram')];
    figures.forEach((figure, index) => {
      // O deck pode declarar o tipo no HTML (data-visual-type); o mapa por aula é apenas fallback.
      const type = figure.dataset.visualType || types[index] || 'map';
      const slide = figure.closest('.slide');
      const heading = slide?.querySelector('h1, h2, h3')?.textContent.trim() || `recurso ${index + 1}`;
      const label = VISUAL_LABELS[type] || VISUAL_LABELS.map;
      figure.classList.add(`visual-${type}`);
      figure.dataset.visualType = type;
      figure.dataset.visualCaption = label;
      figure.setAttribute('role', 'figure');
      figure.setAttribute('aria-label', `${label} sobre ${heading}`);
    });
  }

  function improveAccessibility() {
    if (!deck) return;
    const slides = [...deck.querySelectorAll('.slide')];
    const counter = nav?.querySelector('.counter');
    const prev = document.getElementById('prev');
    const next = document.getElementById('next');
    counter?.setAttribute('aria-hidden', 'true');
    prev?.setAttribute('aria-keyshortcuts', 'ArrowLeft PageUp');
    next?.setAttribute('aria-keyshortcuts', 'ArrowRight PageDown Space');

    const announcer = document.createElement('div');
    announcer.className = 'sr-only slide-announcer';
    announcer.setAttribute('aria-live', 'polite');
    announcer.setAttribute('aria-atomic', 'true');
    document.body.appendChild(announcer);

    const sync = () => {
      let activeIndex = 0;
      slides.forEach((slide, index) => {
        const active = slide.classList.contains('active');
        if (active) activeIndex = index;
        const heading = slide.querySelector('h1, h2')?.textContent.trim() || 'Sem título';
        slide.setAttribute('role', 'group');
        slide.setAttribute('aria-roledescription', 'slide');
        slide.setAttribute('aria-label', `Slide ${index + 1} de ${slides.length}: ${heading}`);
        slide.setAttribute('aria-hidden', String(!active));
        slide.tabIndex = active ? -1 : -1;
      });
      const heading = slides[activeIndex]?.querySelector('h1, h2')?.textContent.trim() || 'Sem título';
      announcer.textContent = `Slide ${activeIndex + 1} de ${slides.length}: ${heading}`;
    };
    const observer = new MutationObserver(sync);
    slides.forEach(slide => observer.observe(slide, { attributes: true, attributeFilter: ['class'] }));
    sync();

    window.addEventListener('hashchange', () => {
      const target = Number(location.hash.slice(1));
      if (Number.isInteger(target) && target >= 1 && target <= slides.length && typeof window.show === 'function') {
        window.show(target - 1);
      }
    });
  }

  italicizeForeignTerms();
  addUnitOverview();
  addReferenceSlide();
  enhanceVisuals();
  numberSlides();
  improveAccessibility();

  const canEnter = root.requestFullscreen || root.webkitRequestFullscreen;
  const canExit = document.exitFullscreen || document.webkitExitFullscreen;
  if (!canEnter || !canExit || document.querySelector('[data-fullscreen-button]')) return;

  const button = document.createElement('button');
  button.type = 'button';
  button.className = 'fullscreen-button';
  if (nav) button.classList.add('with-slide-nav');
  button.dataset.fullscreenButton = '';
  button.innerHTML = `
    <svg class="icon-expand" viewBox="0 0 24 24" aria-hidden="true"><path d="M8 3H3v5M16 3h5v5M8 21H3v-5M16 21h5v-5" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>
    <svg class="icon-compress" viewBox="0 0 24 24" aria-hidden="true"><path d="M8 3v5H3M16 3v5h5M8 21v-5H3M16 21v-5h5" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>
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
  document.body.appendChild(button);
  syncButton();
})();
