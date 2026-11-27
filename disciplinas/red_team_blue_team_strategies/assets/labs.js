/* =====================================================================
   Red Team & Blue Team Strategies — biblioteca de laboratórios dos slides
   ---------------------------------------------------------------------
   Labs.register(alvo, init)  laboratório próprio: init(el) roda na 1ª
                              entrada do slide e pode devolver {enter, leave}
   Labs.vscode(alvo, cfg)     editor VS Code com explorador, abas, realce de
                              sintaxe, digitação ao vivo e terminal integrado.
                              Ocupa o slide inteiro (cfg.full: false desliga);
                              o roteiro do laboratório abre com a tecla G.
                              cfg.setup: [{cmd, out, file, venv}] vira o botão
                              "Preparar o ambiente" (instalação antes de rodar)
   Labs.terminal(alvo, cfg)   terminal (linux | windows | green) roteirizado
   Labs.siem(alvo, cfg)       console de SIEM com buscas salvas, histograma
                              e tabela de resultados
   Labs.browser(alvo, cfg)    janela de navegador com página arbitrária
   Labs.flow(alvo, cfg)       diagrama de arquitetura animado, por etapas
   Labs.scene3d(alvo, build)  cena 3D (three.js r128 via cdnjs), arrastável
   Labs.highlight(code, lang) realce de sintaxe (python, yaml, json, bash,
                              ps, sql, kql, spl, js, text)
   Todo o conteúdo é simulado: nenhum comando é executado de verdade.
   ===================================================================== */
(function () {
  'use strict';

  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
  const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const $ = (sel, root) => (typeof sel === 'string' ? (root || document).querySelector(sel) : sel);
  const h = (tag, cls, html) => { const e = document.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; };

  /* ------------------------------------------------------------------
     Ciclo de vida: inicia na primeira entrada do slide; pausa ao sair
     ------------------------------------------------------------------ */
  function register(sel, init) {
    const el = $(sel);
    if (!el) { console.warn('[Labs] alvo não encontrado:', sel); return null; }
    const slide = el.closest('.slide');
    const box = { ctl: null, active: false };
    const enter = () => {
      box.active = true;
      if (!box.ctl) { try { box.ctl = init(el) || {}; } catch (e) { console.error('[Labs]', e); box.ctl = {}; } }
      box.ctl.enter && box.ctl.enter();
    };
    const leave = () => { box.active = false; box.ctl && box.ctl.leave && box.ctl.leave(); };
    if (slide) {
      slide.addEventListener('slide:enter', enter);
      slide.addEventListener('slide:leave', leave);
      if (slide.classList.contains('active')) enter();
    } else enter();
    return box;
  }

  /* ------------------------------------------------------------------
     Realce de sintaxe (por linha)
     ------------------------------------------------------------------ */
  const words = (s) => new Set(s.split(/\s+/).filter(Boolean));
  const STR = String.raw`"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'`;
  const NUM = String.raw`\b\d+(?:\.\d+)?%?`;
  const LANGS = {
    python: { c: '#.*$', kw: words('def class return if elif else for while in not and or import from as with try except finally raise lambda yield pass break continue is async await global assert'), bi: words('print len range dict list set tuple int float str sorted sum min max open enumerate zip any all round abs isinstance map filter json re datetime timedelta Counter defaultdict math hashlib csv Path'), k2: words('None True False self'), extra: String.raw`@[\w.]+` },
    yaml: { c: '#.*$', yk: true, kw: words(''), bi: words(''), k2: words('true false null yes no') },
    json: { jk: true, kw: words(''), bi: words(''), k2: words('true false null') },
    bash: { c: '#.*$', vars: true, kw: words('if then fi for do done while case esac function return in else elif'), bi: words('sudo cd ls cat grep awk sed echo export curl jq python3 python git docker systemctl journalctl tail head wc sort uniq find chmod whois dig host nslookup openssl ssh ping traceroute nmap tcpdump zeek suricata yara sigma auditctl ausearch'), k2: words('') },
    ps: { c: '#.*$', vars: true, ps: true, kw: words('if else foreach function return param in'), bi: words(''), k2: words('$true $false $null') },
    sql: { c: '--.*$', ci: true, kw: words('SELECT FROM WHERE GROUP BY ORDER HAVING JOIN LEFT RIGHT INNER OUTER ON AS AND OR NOT IN DISTINCT LIMIT CASE WHEN THEN ELSE END WITH DESC ASC BETWEEN LIKE IS NULL UNION ALL OVER PARTITION INSERT INTO VALUES CREATE TABLE'), bi: words('COUNT SUM AVG MIN MAX ROUND COALESCE DATE_TRUNC NOW INTERVAL LAG'), k2: words('') },
    kql: { c: '//.*$', kw: words('where project summarize by extend join on let sort order take top render union parse kind asc desc and or not in between'), bi: words('count dcount countif sum avg min max bin ago now datetime timespan make_set make_list has contains startswith endswith strcat tostring toint arg_max distinct iff isnotempty'), k2: words('true false') },
    spl: { c: '`.*?`', kw: words('index sourcetype source host search where by as AND OR NOT OVER'), bi: words('stats count dc values earliest latest eval table sort head tail tstats rename dedup timechart bin span transaction lookup iplocation if case round'), k2: words('') },
    js: { c: '//.*$', kw: words('const let var function return if else for of in new class import from export await async while switch case break default try catch throw typeof'), bi: words('console Math JSON Date Object Array Promise setTimeout document window'), k2: words('true false null undefined this') },
    text: { kw: words(''), bi: words(''), k2: words('') }
  };
  LANGS.py = LANGS.python; LANGS.yml = LANGS.yaml; LANGS.sh = LANGS.bash; LANGS.powershell = LANGS.ps; LANGS.sigma = LANGS.yaml;
  for (const k in LANGS) {
    const L = LANGS[k]; if (L.re) continue;
    const parts = [];
    if (L.c) parts.push('(?<c>' + L.c + ')');
    if (L.yk) parts.push(String.raw`(?<yk>^\s*-?\s*[\w.\-/|]+(?=\s*:(?:\s|$)))`);
    if (L.jk) parts.push(String.raw`(?<jk>"(?:[^"\\]|\\.)*"(?=\s*:))`);
    parts.push('(?<s>' + STR + ')');
    if (L.vars) parts.push(String.raw`(?<v>\$\{[^}]+\}|\$[\w:]+)`);
    if (L.ps) parts.push(String.raw`(?<f2>\b[A-Z][a-zA-Z]+-[A-Z][A-Za-z]+\b)|(?<v2>(?<=\s)-[A-Za-z]\w*)`);
    if (L.extra) parts.push('(?<d>' + L.extra + ')');
    parts.push('(?<n>' + NUM + ')');
    parts.push(String.raw`(?<w>[A-Za-z_][\w]*)`);
    L.re = new RegExp(parts.join('|'), 'g');
  }
  function hlLine(line, L) {
    let out = '', last = 0, m;
    L.re.lastIndex = 0;
    while ((m = L.re.exec(line))) {
      if (!m[0].length) { L.re.lastIndex++; continue; }
      out += esc(line.slice(last, m.index));
      const g = m.groups, t = m[0];
      let cls = '';
      if (g.c) cls = 'c'; else if (g.yk || g.jk) cls = 'v'; else if (g.s) cls = 's'; else if (g.v || g.v2) cls = 'v';
      else if (g.f2) cls = 'f'; else if (g.d) cls = 'd'; else if (g.n) cls = 'n';
      else if (g.w) {
        const w = L.ci ? t.toUpperCase() : t;
        if (L.kw.has(w)) cls = 'k'; else if (L.k2.has(t)) cls = 'p'; else if (L.bi.has(w)) cls = 'b';
        else if (/^\s*\(/.test(line.slice(L.re.lastIndex))) cls = 'f';
      }
      out += cls ? '<span class="tk-' + cls + '">' + esc(t) + '</span>' : esc(t);
      last = L.re.lastIndex;
    }
    return out + esc(line.slice(last));
  }
  function highlight(code, lang) {
    const L = LANGS[lang] || LANGS.text;
    return String(code).split('\n').map((l) => hlLine(l, L));
  }
  const EXT = { py: 'python', yml: 'yaml', yaml: 'yaml', json: 'json', sh: 'bash', ps1: 'ps', sql: 'sql', kql: 'kql', spl: 'spl', js: 'js', md: 'text', txt: 'text', csv: 'text', log: 'text', conf: 'bash', toml: 'bash', rules: 'bash', env: 'bash' };
  const ICO = { python: ['py', '#4B8BBE'], yaml: ['!', '#CB171E'], json: ['{}', '#F2CB0A'], bash: ['$', '#89E051'], ps: ['>_', '#5391FE'], sql: ['db', '#E38C00'], kql: ['K', '#00B1D2'], spl: ['S', '#65A637'], js: ['JS', '#F7DF1E'], text: ['≡', '#9DA5B4'] };
  const langOf = (f) => f.lang || EXT[(f.path.split('.').pop() || '').toLowerCase()] || 'text';

  /* Saída: "[ok] texto", "[warn]", "[err]", "[info]", "[mute]", "[hi]", "[red]", "[blue]", "[purple]" ou {t, c, d} */
  function outLine(line) {
    let t = line, c = '', d = null;
    if (line && typeof line === 'object') { t = line.t || ''; c = line.c || ''; d = line.d; }
    if (!c) { const m = /^\[(ok|warn|err|info|mute|hi|red|blue|purple)\]\s?/.exec(t || ''); if (m) { c = m[1]; t = t.slice(m[0].length); } }
    return { html: c ? '<span class="o-' + c + '">' + esc(t) + '</span>' : esc(t), d };
  }
  async function stream(target, lines, scroller, token, speed) {
    for (const l of lines) {
      if (token && token.cancel) return;
      const o = outLine(l);
      target.insertAdjacentHTML('beforeend', o.html + '\n');
      scroller.scrollTop = scroller.scrollHeight;
      await sleep(o.d != null ? o.d : (speed || 45));
    }
  }

  /* ------------------------------------------------------------------
     VS Code
     ------------------------------------------------------------------ */
  function vscode(sel, cfg) {
    return register(sel, (el) => {
      const theme = cfg.team ? ' ' + cfg.team + '-team' : '';
      const root = h('div', 'vsc' + theme);
      root.innerHTML =
        '<div class="vsc-title"><i></i><i></i><i></i><span>' + esc(cfg.title || (cfg.folder || 'lab') + ' — Visual Studio Code') + '</span></div>' +
        '<div class="vsc-body"><div class="vsc-activity"><b></b><b></b><b></b><b></b></div>' +
        '<div class="vsc-explorer"><h4>EXPLORADOR</h4><div class="vsc-folder">▾ ' + esc(cfg.folder || 'lab') + '</div><div class="vsc-tree"></div></div>' +
        '<div class="vsc-main"><div class="vsc-tabs"></div><div class="vsc-crumbs"></div><div class="vsc-editor"><pre class="vsc-code"></pre></div>' +
        '<div class="vsc-panel"><div class="vsc-panel-tabs"><span>PROBLEMAS</span><span>SAÍDA</span><span class="on">TERMINAL</span><span class="sp"></span></div><div class="vsc-term"></div></div></div></div>' +
        '<div class="vsc-status"><span>⎇ ' + esc(cfg.branch || 'main') + '</span><span>' + esc(cfg.status || '') + '</span><span class="sp"></span><button type="button" class="vsc-guia" title="Mostrar ou esconder o roteiro do laboratório (tecla G)">☰ Roteiro</button><span class="vsc-lang"></span><span>UTF-8</span><span>LF</span></div>';
      el.appendChild(root);
      // Tela cheia: o VS Code ocupa o slide inteiro; o roteiro (Objetivo, Faça, Observe, Conclusão)
      // vira um painel sobreposto, aberto pelo botão "Roteiro" da barra de status ou pela tecla G.
      const slideEl = el.closest('.slide');
      const guia = root.querySelector('.vsc-guia');
      if (slideEl && cfg.full !== false) {
        slideEl.classList.add('vsc-full');
        const alterna = () => slideEl.classList.toggle('show-side');
        guia.addEventListener('click', alterna);
        document.addEventListener('keydown', (e) => {
          if ((e.key === 'g' || e.key === 'G') && slideEl.classList.contains('active') && !e.ctrlKey && !e.metaKey && !e.altKey && !/^(INPUT|TEXTAREA|SELECT)$/.test((e.target.tagName || ''))) alterna();
        });
        if (!slideEl.querySelector('.lab-side')) guia.remove();
      } else guia.remove();
      const tree = root.querySelector('.vsc-tree'), tabs = root.querySelector('.vsc-tabs'), crumbs = root.querySelector('.vsc-crumbs');
      const codeEl = root.querySelector('.vsc-code'), editor = root.querySelector('.vsc-editor'), term = root.querySelector('.vsc-term');
      const ptabs = root.querySelector('.vsc-panel-tabs'), langEl = root.querySelector('.vsc-lang');
      if (cfg.panelHeight) root.querySelector('.vsc-panel').style.flexBasis = cfg.panelHeight;
      const files = cfg.files || [];
      const opened = [];
      let current = null, typing = null;

      // árvore de arquivos
      let lastDirs = [];
      files.slice().sort((a, b) => a.path.localeCompare(b.path)).forEach((f) => {
        const parts = f.path.split('/'); const dirs = parts.slice(0, -1);
        dirs.forEach((d, k) => {
          if (lastDirs[k] !== d) { const b = h('div', 'vsc-file', '▾ ' + esc(d)); b.style.setProperty('--depth', k); b.style.fontWeight = 600; tree.appendChild(b); lastDirs = dirs.slice(0, k + 1); }
        });
        lastDirs = dirs;
        const lang = langOf(f), ic = ICO[lang] || ICO.text;
        const b = h('button', 'vsc-file', esc(parts[parts.length - 1]));
        b.dataset.ico = ic[0]; b.style.setProperty('--ico', ic[1]); b.style.setProperty('--depth', dirs.length);
        b.addEventListener('click', () => open(f.path));
        f._btn = b; tree.appendChild(b);
      });

      function render(f, upto) {
        const lines = highlight(upto == null ? f.code : f.code.slice(0, upto), langOf(f));
        const hl = new Set(f.hl || []);
        codeEl.innerHTML = lines.map((l, k) => '<span class="ln' + (hl.has(k + 1) && upto == null ? ' hl' : '') + '">' + (l || ' ') + (upto != null && k === lines.length - 1 ? '<span class="caret"></span>' : '') + '</span>').join('');
      }
      function drawTabs() {
        tabs.innerHTML = '';
        opened.forEach((p) => {
          const f = files.find((x) => x.path === p); const ic = ICO[langOf(f)] || ICO.text;
          const t = h('button', 'vsc-tab' + (p === current.path ? ' is-active' : ''), '<span style="color:' + ic[1] + ';font-weight:700;font-size:10px">' + esc(ic[0]) + '</span> ' + esc(p.split('/').pop()));
          t.addEventListener('click', () => open(p)); tabs.appendChild(t);
        });
      }
      function open(path) {
        const f = files.find((x) => x.path === path); if (!f) return;
        if (typing) typing.cancel = true;
        current = f;
        if (!opened.includes(path)) opened.push(path);
        files.forEach((x) => x._btn && x._btn.classList.toggle('is-open', x === f));
        drawTabs();
        crumbs.textContent = (cfg.folder || 'lab') + ' › ' + path.split('/').join(' › ');
        langEl.textContent = { python: 'Python', yaml: 'YAML', json: 'JSON', bash: 'Shell Script', ps: 'PowerShell', sql: 'SQL', kql: 'KQL', spl: 'SPL', js: 'JavaScript', text: 'Texto sem formatação' }[langOf(f)] || '';
        render(f); editor.scrollTop = 0;
        if (f.scrollTo) editor.scrollTop = Math.max(0, (f.scrollTo - 3) * 21.7);
      }
      async function typeOut(f) {
        if (typing) typing.cancel = true;
        const tok = typing = { cancel: false };
        const total = f.code.length; const steps = Math.min(140, total);
        for (let s = 1; s <= steps; s++) {
          if (tok.cancel) return;
          render(f, Math.round(total * s / steps)); editor.scrollTop = editor.scrollHeight;
          await sleep(cfg.typeDelay || 28);
        }
        render(f); typing = null;
      }
      // cfg.kali: true ou "usuario@maquina" → terminal integrado com o prompt do Kali (zsh)
      const kali = !!cfg.kali && cfg.shell !== 'pwsh';
      let prompt = cfg.prompt || (cfg.shell === 'pwsh' ? 'PS C:\\lab\\' + (cfg.folder || 'lab') + '> ' : (kali ? (cfg.kali === true ? 'kali@kali' : cfg.kali) : 'aluno@lab') + ':~/' + (cfg.folder || 'lab') + '$ ');
      const pV = (p) => (kali ? '<span class="pr-k">' + promptHTML(p, true) + '</span>' : '<span class="o-ok">' + esc(p) + '</span>');
      let running = null;
      async function exec(cmd, out, speed) {
        term.insertAdjacentHTML('beforeend', pV(prompt));
        for (const ch of cmd) { term.insertAdjacentText('beforeend', ch); await sleep(14); }
        term.insertAdjacentText('beforeend', '\n'); term.scrollTop = term.scrollHeight; await sleep(250);
        const lines = typeof out === 'function' ? out() : (out || []);
        await stream(term, lines, term, running, speed);
      }
      const travar = (v) => ptabs.querySelectorAll('.lab-btn').forEach((b) => (b.disabled = v));
      async function run(k) {
        const r = cfg.run[k]; if (!r || running) return;
        running = { cancel: false };
        travar(true);
        if (r.file) open(r.file);
        if (r.clear !== false) term.innerHTML = '';
        await exec(r.cmd, r.out, r.speed);
        term.insertAdjacentHTML('beforeend', pV(prompt));
        travar(false);
        running = null;
        cfg.onRun && cfg.onRun(k, api);
      }
      // Preparação do ambiente: cfg.setup = [{ cmd, out, speed, file }], executados em sequência no
      // mesmo terminal (versão do interpretador, ambiente virtual, instalação de pacotes e programas).
      let pronto = false, bSetup = null;
      async function setup() {
        if (!cfg.setup || running) return;
        running = { cancel: false };
        travar(true);
        term.innerHTML = '';
        for (const st of cfg.setup) {
          if (st.file) open(st.file);
          await exec(st.cmd, st.out, st.speed);
          if (st.venv) prompt = '(' + (st.venv === true ? '.venv' : st.venv) + ') ' + prompt;   // ambiente virtual ativado
          if (st.prompt) prompt = st.prompt;
          await sleep(350);
        }
        term.insertAdjacentHTML('beforeend', pV(prompt));
        term.scrollTop = term.scrollHeight;
        travar(false);
        running = null; pronto = true;
        if (bSetup) { bSetup.classList.add('feito'); bSetup.textContent = '✓ ' + (cfg.setupLabel || 'Ambiente pronto'); }
      }
      if (cfg.setup && cfg.setup.length) {
        bSetup = h('button', 'lab-btn setup', '⬇ ' + esc(cfg.setupLabel || 'Preparar o ambiente'));
        bSetup.addEventListener('click', setup); ptabs.appendChild(bSetup);
      }
      (cfg.run || []).forEach((r, k) => {
        const b = h('button', 'lab-btn' + (r.kind ? ' ' + r.kind : ''), '▶ ' + esc(r.label || r.cmd));
        b.addEventListener('click', () => run(k)); ptabs.appendChild(b);
      });
      const bt = h('button', 'lab-btn ghost', '⌨ Digitar ao vivo');
      bt.addEventListener('click', () => current && typeOut(current)); ptabs.appendChild(bt);
      term.innerHTML = cfg.intro ? cfg.intro.map((l) => outLine(l).html).join('\n') + '\n' : '';
      term.insertAdjacentHTML('beforeend', pV(prompt));
      open(cfg.open || (files[0] && files[0].path));
      let first = true;
      const api = {
        open, run, setup, term, get pronto() { return pronto; }, setCode(path, code) { const f = files.find((x) => x.path === path); if (f) { f.code = code; if (current === f) render(f); } },
        enter() { if (first && cfg.typeOnEnter && current) typeOut(current); first = false; },
        leave() { if (typing) typing.cancel = true; }
      };
      return api;
    });
  }

  /* ------------------------------------------------------------------
     Terminal roteirizado
     ------------------------------------------------------------------ */
  /* Prompt no estilo do Kali Linux (zsh): duas linhas, moldura verde (azul para root), usuário㉿máquina em azul.
     Aceita "usuario@maquina:~/pasta$ " (com "(.venv) " na frente, se houver) e os prompts do Metasploit ("msf6 > "). */
  function promptHTML(p, kali) {
    if (!kali) return null;
    const m = /^(?:\(([^)]+)\) )?([\w.-]+)@([\w.-]+):(.*?)([$#]) ?$/.exec(p);
    if (m) {
      const root = m[5] === '#', f = root ? 'kz-rf' : 'kz-f';
      return '<span class="' + f + '">┌──' + (m[1] ? '(' + esc(m[1]) + ')─' : '') + '(</span><span class="' + (root ? 'kz-ru' : 'kz-u') + '">' + esc(m[2]) + '㉿' + esc(m[3]) + '</span><span class="' + f + '">)-[</span><span class="kz-d">' + esc(m[4]) + '</span><span class="' + f + '">]</span>\n' +
        '<span class="' + f + '">└─</span><span class="' + (root ? 'kz-ru' : 'kz-u') + '">' + m[5] + '</span> ';
    }
    const x = /^(msf\d?)( (\w+)\(([^)]+)\))? > $/.exec(p);
    if (x) return '<span class="kz-msf">' + x[1] + '</span>' + (x[2] ? ' ' + esc(x[3]) + '(<span class="kz-mod">' + esc(x[4]) + '</span>)' : '') + ' &gt; ';
    return esc(p);
  }
  const KALI_BAR = '<div class="term-bar kali-bar"><span class="kb-ico">▣</span><span class="kb-t"></span><b class="kb-w">─</b><b class="kb-w">☐</b><b class="kb-w kb-x">✕</b></div>' +
    '<div class="kali-menu"><span>File</span><span>Actions</span><span>Edit</span><span>View</span><span>Help</span></div>';

  function terminal(sel, cfg) {
    return register(sel, (el) => {
      const root = h('div', 'term ' + (cfg.theme || ''));
      const kali = cfg.theme === 'kali';
      // prompt iniciado por "!" fica no formato simples (ex.: o computador hospedeiro, antes de a VM do Kali existir)
      const pH = (p) => (p[0] === '!' ? '<span class="kz-host">' + esc(p.slice(1)) + '</span>' : kali ? promptHTML(p, true) : esc(p));
      root.innerHTML = (kali ? KALI_BAR : '<div class="term-bar"><i></i><i></i><i></i><span>' + esc(cfg.title || 'terminal') + '</span></div>') + '<div class="term-body"></div>' +
        '<div class="term-ctrl"><button class="lab-btn">▶ Próximo comando</button><button class="lab-btn ghost">⏭ Executar tudo</button><button class="lab-btn ghost">⟲ Reiniciar</button><span class="note"></span></div>';
      el.appendChild(root);
      const body = root.querySelector('.term-body'), note = root.querySelector('.note');
      if (kali) root.querySelector('.kb-t').textContent = cfg.title || 'kali@kali: ~';
      const [bNext, bAll, bReset] = root.querySelectorAll('.term-ctrl button');
      const prompt0 = cfg.prompt || (cfg.theme === 'windows' ? 'PS C:\\Users\\analista> ' : 'analista@lab:~$ ');
      const prompt = prompt0;
      let k = 0, busy = false, tok = { cancel: false };
      function reset() {
        tok.cancel = true; tok = { cancel: false }; k = 0; busy = false;
        if (kali) root.querySelector('.kb-t').textContent = cfg.title || 'kali@kali: ~';
        body.innerHTML = (cfg.intro || []).map((l) => outLine(l).html).join('\n') + (cfg.intro ? '\n' : '');
        body.insertAdjacentHTML('beforeend', '<span class="pr">' + pH(prompt) + '</span>');
        note.textContent = cfg.hint || 'Clique em "Próximo comando" para executar o roteiro passo a passo.';
        bNext.disabled = false;
      }
      async function step() {
        if (busy || k >= cfg.steps.length) return;
        busy = true; const s = cfg.steps[k++]; const my = tok;
        note.innerHTML = s.note ? esc(s.note) : '';
        const span = h('span', 'cm'); body.appendChild(span);
        const delay = Math.max(6, Math.min(30, 900 / (s.cmd.length || 1)));
        for (const ch of s.cmd) { if (my.cancel) return; span.textContent += ch; body.scrollTop = body.scrollHeight; await sleep(delay); }
        body.insertAdjacentText('beforeend', '\n'); await sleep(s.wait || 300);
        await stream(body, s.out || [], body, my, s.speed || cfg.speed);
        if (my.cancel) return;
        if (s.title && kali) root.querySelector('.kb-t').textContent = s.title;
        body.insertAdjacentHTML('beforeend', '<span class="pr">' + pH(s.prompt || prompt) + '</span>');
        body.scrollTop = body.scrollHeight;
        busy = false;
        if (k >= cfg.steps.length) { bNext.disabled = true; if (cfg.done) note.textContent = cfg.done; }
        cfg.onStep && cfg.onStep(k - 1);
      }
      async function all() { while (k < cfg.steps.length) { if (busy) { await sleep(120); continue; } await step(); } }
      bNext.addEventListener('click', step); bAll.addEventListener('click', all); bReset.addEventListener('click', reset);
      reset();
      return { step, reset, leave() {} };
    });
  }

  /* ------------------------------------------------------------------
     Console SIEM
     ------------------------------------------------------------------ */
  function siem(sel, cfg) {
    return register(sel, (el) => {
      const root = h('div', 'siem');
      root.innerHTML = '<div class="siem-top"><span class="siem-logo">' + esc(cfg.product || 'SIEM') + '</span><div class="siem-q"><span class="lang"></span><span class="qt"></span></div><span class="siem-time">🕒 ' + esc(cfg.time || 'Últimas 24 horas') + '</span><button class="lab-btn blue">Pesquisar</button></div>' +
        '<div class="siem-nav"></div><div class="siem-main"><div class="siem-meta"></div><div class="siem-hist"></div><div class="siem-tablewrap"><table><thead></thead><tbody></tbody></table></div><div class="siem-note" hidden></div></div>';
      el.appendChild(root);
      const nav = root.querySelector('.siem-nav'), qt = root.querySelector('.qt'), lang = root.querySelector('.lang');
      const meta = root.querySelector('.siem-meta'), hist = root.querySelector('.siem-hist'), thead = root.querySelector('thead'), tbody = root.querySelector('tbody'), noteEl = root.querySelector('.siem-note');
      let cur = 0, tok = { cancel: false };
      let group = null;
      (cfg.searches || []).forEach((s, k) => {
        if (s.group && s.group !== group) { group = s.group; nav.appendChild(h('h5', '', esc(group))); }
        const b = h('button', '', esc(s.name)); b.addEventListener('click', () => pick(k)); nav.appendChild(b); s._b = b;
      });
      if (!cfg.searches.some((s) => s.group)) nav.insertBefore(h('h5', '', 'Buscas salvas'), nav.firstChild);
      function cell(v, c, s) {
        if (s.sevCol === c) return '<span class="sev sev-' + String(v).toLowerCase() + '">' + esc(v) + '</span>';
        return esc(v);
      }
      async function pick(k) {
        tok.cancel = true; const my = tok = { cancel: false };
        cur = k; const s = cfg.searches[k];
        cfg.searches.forEach((x, j) => x._b.classList.toggle('is-on', j === k));
        lang.textContent = s.lang || cfg.lang || 'KQL';
        qt.textContent = '';
        for (const ch of s.q) { if (my.cancel) return; qt.textContent += ch; await sleep(Math.max(4, 700 / s.q.length)); }
        meta.innerHTML = '<span>Pesquisando…</span>'; tbody.innerHTML = ''; noteEl.hidden = true;
        const H = s.hist || []; const mx = Math.max(1, ...H);
        hist.innerHTML = H.map((v, j) => '<i style="height:0%" class="' + ((s.hot || []).includes(j) ? 'hot' : '') + '" title="' + v + '"></i>').join('');
        await sleep(450); if (my.cancel) return;
        hist.querySelectorAll('i').forEach((b, j) => (b.style.height = Math.max(2, (H[j] / mx) * 100) + '%'));
        const total = s.total != null ? s.total : (s.rows || []).length;
        meta.innerHTML = '<span><b>' + Number(total).toLocaleString('pt-BR') + '</b> ' + (s.unit || 'resultados') + '</span><span>' + esc(s.index || cfg.index || '') + '</span>' + (s.took ? '<span>' + esc(s.took) + '</span>' : '');
        thead.innerHTML = '<tr>' + (s.cols || []).map((c) => '<th>' + esc(c) + '</th>').join('') + '</tr>';
        for (const r of s.rows || []) {
          if (my.cancel) return;
          const tr = h('tr', 'new', r.map((v, c) => '<td>' + cell(v, c, s) + '</td>').join(''));
          tbody.appendChild(tr); await sleep(70);
        }
        if (s.note) { noteEl.innerHTML = s.note; noteEl.hidden = false; }
        cfg.onSearch && cfg.onSearch(k);
      }
      root.querySelector('.siem-top .lab-btn').addEventListener('click', () => pick(cur));
      return { pick, enter() { if (!tbody.children.length) pick(cfg.start || 0); } };
    });
  }

  /* ------------------------------------------------------------------
     Navegador
     ------------------------------------------------------------------ */
  function browser(sel, cfg) {
    return register(sel, (el) => {
      const root = h('div', 'brw');
      root.innerHTML = '<div class="brw-bar"><i></i><i></i><i></i><div class="brw-url"><span class="lock"></span><span class="u"></span></div></div><div class="brw-page"></div>';
      el.appendChild(root);
      const page = root.querySelector('.brw-page'), url = root.querySelector('.brw-url');
      function go(u, html, secure) {
        url.querySelector('.u').textContent = u;
        url.querySelector('.lock').textContent = secure === false ? '⚠' : '🔒';
        url.classList.toggle('danger', secure === false);
        page.innerHTML = html; page.scrollTop = 0;
        cfg.onReady && cfg.onReady(page, api);
      }
      const api = { go, page };
      go(cfg.url || 'about:blank', cfg.html || '', cfg.secure);
      return api;
    });
  }

  /* ------------------------------------------------------------------
     Diagrama animado por etapas
     nodes: [{id, x, y, label, sub, icon, k, w, h}]  (x, y = centro)
     links: [{from, to, label, dashed, curve}]
     steps: [{title, text, on:[ids], bad:[ids], links:[[de, para, cor]], dim}]
     ------------------------------------------------------------------ */
  function flow(sel, cfg) {
    return register(sel, (el) => {
      const W = cfg.w || 1000, H = cfg.h || 480;
      const root = h('div', 'flow');
      root.innerHTML = '<div class="flow-stage"></div><div class="flow-cap"><button class="lab-btn ghost">◀</button><button class="lab-btn">▶ Avançar</button><button class="lab-btn ghost">⏯ Auto</button><div class="txt"></div><span class="cnt"></span></div>';
      el.appendChild(root);
      const stage = root.querySelector('.flow-stage'), txt = root.querySelector('.txt'), cnt = root.querySelector('.cnt');
      const [bPrev, bNext, bAuto] = root.querySelectorAll('.flow-cap button');
      const NS = 'http://www.w3.org/2000/svg';
      const svg = document.createElementNS(NS, 'svg');
      svg.setAttribute('viewBox', '0 0 ' + W + ' ' + H); svg.setAttribute('preserveAspectRatio', 'xMidYMid meet');
      stage.appendChild(svg);
      const byId = {}; (cfg.nodes || []).forEach((n) => (byId[n.id] = n));
      const path = (a, b, curve) => {
        if (!curve) return 'M' + a.x + ',' + a.y + ' L' + b.x + ',' + b.y;
        const mx = (a.x + b.x) / 2 + curve, my = (a.y + b.y) / 2 - curve;
        return 'M' + a.x + ',' + a.y + ' Q' + mx + ',' + my + ' ' + b.x + ',' + b.y;
      };
      const linkEls = {};
      (cfg.links || []).forEach((l) => {
        const a = byId[l.from], b = byId[l.to]; if (!a || !b) return;
        const p = document.createElementNS(NS, 'path');
        p.setAttribute('d', path(a, b, l.curve)); p.setAttribute('class', 'flow-link' + (l.dashed ? ' dashed' : ''));
        svg.appendChild(p); linkEls[l.from + '>' + l.to] = p; linkEls[l.to + '>' + l.from] = linkEls[l.to + '>' + l.from] || p;
        if (l.label) {
          const t = document.createElementNS(NS, 'text'); t.setAttribute('class', 'flow-link-lbl');
          t.setAttribute('x', (a.x + b.x) / 2 + (l.dx || 0)); t.setAttribute('y', (a.y + b.y) / 2 - 6 + (l.dy || 0)); t.setAttribute('text-anchor', 'middle');
          t.textContent = l.label; svg.appendChild(t);
        }
      });
      const nodeEls = {};
      (cfg.nodes || []).forEach((n) => {
        const w = n.w || 170, hh = n.h || 66;
        const g = document.createElementNS(NS, 'g'); g.setAttribute('class', 'flow-node' + (n.k ? ' k-' + n.k : ''));
        g.innerHTML = '<rect x="' + (n.x - w / 2) + '" y="' + (n.y - hh / 2) + '" width="' + w + '" height="' + hh + '" rx="12"/>' +
          (n.icon ? '<text class="ico" x="' + (n.x - w / 2 + 14) + '" y="' + (n.y + 9) + '">' + esc(n.icon) + '</text>' : '') +
          '<text class="lbl" x="' + (n.x + (n.icon ? 16 : 0)) + '" y="' + (n.y + (n.sub ? -3 : 5)) + '" text-anchor="middle">' + esc(n.label) + '</text>' +
          (n.sub ? '<text class="sub" x="' + (n.x + (n.icon ? 16 : 0)) + '" y="' + (n.y + 15) + '" text-anchor="middle">' + esc(n.sub) + '</text>' : '');
        svg.appendChild(g); nodeEls[n.id] = g;
      });
      // pacotes passam por baixo dos nós: a camada fica entre as ligações e os nós
      const pktLayer = document.createElementNS(NS, 'g');
      const firstNode = svg.querySelector('.flow-node'); svg.insertBefore(pktLayer, firstNode);
      // Ajuste de texto: só dá para medir com o slide visível
      let fitted = false;
      function fit() {
        if (fitted) return;
        const probe = svg.querySelector('.flow-node .lbl');
        if (!probe || !probe.getBBox().width) return;
        fitted = true;
        const rects = [];
        (cfg.nodes || []).forEach((n) => {
          const w = n.w || 170, hh = n.h || 66, g = nodeEls[n.id];
          rects.push({ x0: n.x - w / 2, x1: n.x + w / 2, y0: n.y - hh / 2, y1: n.y + hh / 2 });
          const ico = g.querySelector('.ico');
          let left = n.x - w / 2 + 10;
          if (ico) { const ib = ico.getBBox(); left = ib.x + ib.width + 8; }
          const right = n.x + w / 2 - 10, avail = right - left, cx = (left + right) / 2;
          g.querySelectorAll('.lbl, .sub').forEach((tx) => {
            tx.setAttribute('x', cx);
            const bw = tx.getBBox().width;
            if (bw > avail) {
              const fs = parseFloat(getComputedStyle(tx).fontSize) || 14;
              tx.style.fontSize = Math.max(9, fs * avail / bw).toFixed(1) + 'px';
            }
          });
        });
        // rótulos das ligações: afasta dos nós
        svg.querySelectorAll('.flow-link-lbl').forEach((tx) => {
          for (let tries = 0; tries < 6; tries++) {
            const b = tx.getBBox();
            const hit = rects.some((r) => !(b.x + b.width < r.x0 - 2 || b.x > r.x1 + 2 || b.y + b.height < r.y0 - 2 || b.y > r.y1 + 2));
            if (!hit) break;
            tx.setAttribute('y', +tx.getAttribute('y') - 12);
          }
        });
      }
      let k = 0, pkts = [], raf = null, auto = null, active = false;
      function apply() {
        const s = (cfg.steps || [])[k] || {};
        const on = new Set(s.on || []), bad = new Set(s.bad || []);
        Object.entries(nodeEls).forEach(([id, g]) => {
          g.classList.toggle('is-on', on.has(id)); g.classList.toggle('is-bad', bad.has(id));
          g.classList.toggle('is-dim', !!s.dim && !on.has(id) && !bad.has(id));
        });
        Object.values(linkEls).forEach((p) => p.setAttribute('class', p.getAttribute('class').replace(/ is-on.*$/, '')));
        pktLayer.innerHTML = ''; pkts = [];
        (s.links || []).forEach(([a, b, c], j) => {
          const p = linkEls[a + '>' + b]; const A = byId[a], B = byId[b];
          if (p) p.setAttribute('class', p.getAttribute('class') + ' is-on ' + (c || ''));
          if (!A || !B) return;
          for (let q = 0; q < 2; q++) {
            const dot = document.createElementNS(NS, 'circle'); dot.setAttribute('r', 7); dot.setAttribute('class', 'flow-pkt ' + (c || ''));
            pktLayer.appendChild(dot);
            const l = (cfg.links || []).find((x) => (x.from === a && x.to === b) || (x.from === b && x.to === a));
            const L0 = l ? byId[l.from] : A, L1 = l ? byId[l.to] : B;
            pkts.push({ dot, L0, L1, curve: (l && l.curve) || 0, dir: !l || l.from === a ? 1 : -1, off: q * 0.5 + j * 0.13 });
          }
        });
        txt.innerHTML = (s.title ? '<b>' + esc(s.title) + '</b>' : '') + '<span>' + (s.text || '') + '</span>';
        cnt.textContent = (k + 1) + ' / ' + (cfg.steps || []).length;
        bPrev.disabled = k === 0; bNext.disabled = k >= (cfg.steps || []).length - 1;
        cfg.onStep && cfg.onStep(k, s);
      }
      function frame(t) {
        pkts.forEach((p) => {
          const u = ((t / 1600) + p.off) % 1;
          const uu = p.dir > 0 ? u : 1 - u, a0 = p.L0, b0 = p.L1;
          const mx = (a0.x + b0.x) / 2 + p.curve, my = (a0.y + b0.y) / 2 - p.curve;
          const x = (1 - uu) * (1 - uu) * a0.x + 2 * (1 - uu) * uu * mx + uu * uu * b0.x;
          const y = (1 - uu) * (1 - uu) * a0.y + 2 * (1 - uu) * uu * my + uu * uu * b0.y;
          p.dot.setAttribute('cx', x); p.dot.setAttribute('cy', y);
        });
        if (active) raf = requestAnimationFrame(frame);
      }
      const go = (n) => { k = Math.max(0, Math.min((cfg.steps || []).length - 1, n)); apply(); };
      bPrev.addEventListener('click', () => { stopAuto(); go(k - 1); });
      bNext.addEventListener('click', () => { stopAuto(); go(k + 1); });
      function stopAuto() { clearInterval(auto); auto = null; bAuto.classList.add('ghost'); }
      bAuto.addEventListener('click', () => {
        if (auto) return stopAuto();
        bAuto.classList.remove('ghost');
        auto = setInterval(() => { if (k >= (cfg.steps || []).length - 1) { if (cfg.loop === false) return stopAuto(); go(0); } else go(k + 1); }, cfg.interval || 3800);
      });
      apply();
      return {
        go, get step() { return k; },
        enter() { active = true; requestAnimationFrame(fit); cancelAnimationFrame(raf); raf = requestAnimationFrame(frame); },
        leave() { active = false; cancelAnimationFrame(raf); stopAuto(); }
      };
    });
  }

  /* ------------------------------------------------------------------
     Cena 3D (three.js r128). build(ctx) recebe:
     { THREE, scene, camera, renderer, root, el, label(texto, opts), onFrame(fn), legend(html), controls(html) }
     ------------------------------------------------------------------ */
  let threeP = null;
  function loadThree() {
    if (window.THREE) return Promise.resolve(window.THREE);
    if (!threeP) threeP = new Promise((res, rej) => {
      const s = document.createElement('script');
      s.src = 'https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js';
      s.onload = () => res(window.THREE); s.onerror = rej; document.head.appendChild(s);
    });
    return threeP;
  }
  function scene3d(sel, build, opts) {
    opts = opts || {};
    return register(sel, (el) => {
      const box = h('div', 'scene3d'); el.appendChild(box);
      box.insertAdjacentHTML('beforeend', '<div class="hint">' + esc(opts.hint || 'Arraste para girar · role para aproximar') + '</div>');
      let ctx = null, running = false, raf = null, frames = [];
      const api = {
        enter() { running = true; if (ctx) loop(); },
        leave() { running = false; cancelAnimationFrame(raf); }
      };
      loadThree().then((THREE) => {
        const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
        renderer.setPixelRatio(Math.min(2, window.devicePixelRatio || 1));
        box.insertBefore(renderer.domElement, box.firstChild);
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(opts.fov || 45, 1, 0.1, 2000);
        camera.position.set(...(opts.camera || [0, 4, 16]));
        camera.lookAt(0, 0, 0);
        scene.add(new THREE.AmbientLight(0xffffff, 0.65));
        const dl = new THREE.DirectionalLight(0xffffff, 0.8); dl.position.set(6, 12, 8); scene.add(dl);
        const root = new THREE.Group(); scene.add(root);
        function size() { const r = box.getBoundingClientRect(); if (!r.width) return; renderer.setSize(r.width, r.height, false); camera.aspect = r.width / r.height; camera.updateProjectionMatrix(); }
        new ResizeObserver(size).observe(box); size();
        // arrastar para girar, roda para zoom
        let drag = null, autoRot = opts.autoRotate !== false, idle = 0;
        box.addEventListener('pointerdown', (e) => { if (e.target.closest('button, input, select, label, .ctrl, .controls')) return; drag = { x: e.clientX, y: e.clientY }; box.setPointerCapture(e.pointerId); idle = 0; });
        box.addEventListener('pointermove', (e) => { if (!drag) return; root.rotation.y += (e.clientX - drag.x) * 0.008; root.rotation.x = Math.max(-1.2, Math.min(1.2, root.rotation.x + (e.clientY - drag.y) * 0.006)); drag = { x: e.clientX, y: e.clientY }; });
        box.addEventListener('pointerup', () => { drag = null; });
        box.addEventListener('wheel', (e) => { e.preventDefault(); const d = camera.position.length(); const nd = Math.max(4, Math.min(60, d * (1 + Math.sign(e.deltaY) * 0.08))); camera.position.multiplyScalar(nd / d); }, { passive: false });
        function label(text, o) {
          o = o || {};
          const c = document.createElement('canvas'); const fs = o.size || 44; const g = c.getContext('2d');
          g.font = '700 ' + fs + 'px Montserrat, Arial'; const w = Math.ceil(g.measureText(text).width) + 30;
          c.width = w; c.height = fs + 26; g.font = '700 ' + fs + 'px Montserrat, Arial';
          if (o.bg !== false) { g.fillStyle = o.bg || 'rgba(5,11,24,.75)'; g.beginPath(); if (g.roundRect) g.roundRect(0, 0, c.width, c.height, 12); else g.rect(0, 0, c.width, c.height); g.fill(); }
          g.fillStyle = o.color || '#ffffff'; g.textBaseline = 'middle'; g.fillText(text, 15, c.height / 2 + 2);
          const tex = new THREE.CanvasTexture(c); tex.minFilter = THREE.LinearFilter;
          const sp = new THREE.Sprite(new THREE.SpriteMaterial({ map: tex, transparent: true, depthTest: o.depthTest !== false }));
          const sc = (o.scale || 1) * 0.0075; sp.scale.set(c.width * sc, c.height * sc, 1);
          return sp;
        }
        ctx = {
          THREE, scene, camera, renderer, root, el: box, label,
          onFrame(fn) { frames.push(fn); },
          legend(html) { const d = h('div', 'legend', html); box.appendChild(d); return d; },
          controls(html) { const d = h('div', 'ctrl', html); box.appendChild(d); return d; },
          stopAutoRotate() { autoRot = false; }
        };
        try { build(ctx); } catch (err) {
          console.error('[Labs] erro na cena 3D:', err);
          box.insertAdjacentHTML('beforeend', '<div class="fallback">Erro ao montar a cena 3D: ' + esc(err.message) + '</div>');
        }
        let last = performance.now();
        window.__labsLoop = window.__labsLoop || 0;
        function loopInner(t) {
          const dt = Math.max(0, Math.min(0.05, (t - last) / 1000)); last = t;
          if (autoRot && !drag) { idle += dt; if (idle > 1.5) root.rotation.y += dt * (opts.spin || 0.18); }
          frames.forEach((fn) => fn(t / 1000, dt));
          renderer.render(scene, camera);
          if (running) raf = requestAnimationFrame(loopInner);
        }
        loop = () => { cancelAnimationFrame(raf); last = performance.now(); raf = requestAnimationFrame(loopInner); };
        if (running) loop();
      }).catch(() => {
        box.insertAdjacentHTML('beforeend', '<div class="fallback">A cena 3D precisa de conexão com a internet para carregar a biblioteca three.js (cdnjs).<br>' + esc(opts.fallback || '') + '</div>');
      });
      let loop = () => {};
      return api;
    });
  }


  /* ------------------------------------------------------------------
     Plataforma Rede Tatame: o simulador único da disciplina
     (simulador/index.html) embutido por iframe. Um só iframe por deck
     é movido para o slide ativo, então o estado (cenário, alertas,
     regras) continua de um slide para o outro.
     cfg: { aba, cenario, autostart, rodar, regras: {R5:true}, fontes: {cloud:true},
            reiniciar, src }
     ------------------------------------------------------------------ */
  let simFrame = null, simCfg = {};
  function simSend() {
    const cfg = simCfg, msg = { simAba: cfg.aba || 'arquitetura' };
    ['cenario', 'autostart', 'rodar', 'regras', 'fontes', 'reiniciar'].forEach((k) => { if (cfg[k] != null) msg[k] = cfg[k]; });
    simFrame && simFrame.contentWindow && simFrame.contentWindow.postMessage(msg, '*');
  }
  function plataforma(sel, cfg) {
    cfg = cfg || {};
    return register(sel, (el) => {
      el.classList.add('plataforma');
      return {
        enter() {
          simCfg = cfg;
          if (!simFrame) {
            simFrame = document.createElement('iframe');
            simFrame.className = 'plataforma-frame';
            simFrame.title = 'Simulador da plataforma Rede Tatame';
            simFrame.src = (cfg.src || '../../simulador/index.html') + '?embed=1#' + (cfg.aba || 'arquitetura');
            simFrame.addEventListener('load', simSend); // mover o iframe no DOM recarrega a página: reaplica a config do slide atual
          }
          if (simFrame.parentNode !== el) el.appendChild(simFrame);
          else simSend();
        }
      };
    });
  }

  /* ------------------------------------------------------------------
     Mini-mapa da Rede Tatame: mostra ONDE acontece o problema da aula.
     Labs.miniMapa('#id', { destaque: ['vpn','ad'], alvo: 'arq', caminho: ['net','vpn','ad','arq'],
                            legenda: 'texto curto' })
     Ids: app portal catraca net waf hml gw pay ident alunos checkin cobranca notif db kafka cep lake
          siem mail vpn nb ad arq erp edr (os mesmos do simulador)
     ------------------------------------------------------------------ */
  const MAPA = {
    app: [70, 40, 'App do aluno'], portal: [70, 95, 'Portal gestão'], catraca: [70, 150, 'Catracas IoT'], net: [70, 235, 'Internet'],
    waf: [215, 95, 'CDN / WAF'], hml: [215, 195, 'hml-gestao'], gw: [350, 95, 'API gateway'], pay: [350, 180, 'PagaFácil'],
    ident: [490, 25, 'svc-identidade'], alunos: [490, 70, 'svc-alunos'], checkin: [490, 115, 'svc-checkin'], cobranca: [490, 160, 'svc-cobranca'], notif: [490, 205, 'svc-notificacoes'],
    db: [630, 45, 'db-alunos'], kafka: [630, 125, 'Kafka'], cep: [760, 85, 'Motor CEP'], lake: [760, 145, 'Data lake'], siem: [760, 215, 'SIEM · SOC'],
    mail: [215, 300, 'E-mail'], vpn: [215, 355, 'VPN'], nb: [350, 300, 'NB-FIN-031'], ad: [350, 355, 'SRV-AD-01'], arq: [490, 300, 'SRV-ARQ-01'], erp: [490, 355, 'SRV-ERP-01'], edr: [630, 330, 'Console EDR']
  };
  const MAPA_ARESTAS = [['app', 'waf'], ['portal', 'waf'], ['catraca', 'waf'], ['net', 'waf'], ['net', 'hml'], ['net', 'mail'], ['net', 'vpn'], ['waf', 'gw'], ['hml', 'db'], ['gw', 'ident'], ['gw', 'alunos'], ['gw', 'checkin'], ['gw', 'cobranca'], ['gw', 'notif'], ['cobranca', 'pay'], ['alunos', 'db'],
    ['ident', 'kafka'], ['alunos', 'kafka'], ['checkin', 'kafka'], ['cobranca', 'kafka'], ['kafka', 'cep'], ['kafka', 'lake'], ['cep', 'siem'], ['mail', 'nb'], ['vpn', 'ad'], ['nb', 'ad'], ['ad', 'arq'], ['ad', 'erp'], ['arq', 'edr'], ['erp', 'edr'], ['nb', 'edr'], ['edr', 'siem']];
  function miniMapa(sel, cfg) {
    cfg = cfg || {};
    return register(sel, (el) => {
      const dest = new Set(cfg.destaque || []), cam = cfg.caminho || [];
      let s = '<svg viewBox="0 0 830 390" class="minimapa" role="img" aria-label="Mapa da plataforma Rede Tatame com a área desta aula em destaque">';
      s += '<rect class="zona" x="150" y="8" width="660" height="238" rx="10"/><text class="zona-l" x="160" y="241">NUVEM · VPC 10.40.0.0/16</text>';
      s += '<rect class="zona" x="150" y="272" width="560" height="112" rx="10"/><text class="zona-l" x="560" y="381">SEDE · corp.tatame.local</text>';
      MAPA_ARESTAS.forEach(([a, b]) => { const A = MAPA[a], B = MAPA[b]; s += '<line class="ar" x1="' + A[0] + '" y1="' + A[1] + '" x2="' + B[0] + '" y2="' + B[1] + '"/>'; });
      for (let i = 0; i < cam.length - 1; i++) { const A = MAPA[cam[i]], B = MAPA[cam[i + 1]]; if (A && B) s += '<line class="ar cam" x1="' + A[0] + '" y1="' + A[1] + '" x2="' + B[0] + '" y2="' + B[1] + '"/>'; }
      Object.entries(MAPA).forEach(([id, v]) => {
        const x = v[0], y = v[1], l = v[2];
        const cls = id === cfg.alvo ? 'no alvo' : (dest.has(id) || cam.includes(id)) ? 'no dest' : 'no';
        const fit = cls !== 'no' && l.length > 11 ? ' textLength="112" lengthAdjust="spacingAndGlyphs"' : '';
        s += '<g class="' + cls + '"><rect x="' + (x - 64) + '" y="' + (y - 17) + '" width="128" height="34" rx="7"/><text x="' + x + '" y="' + (y + 5.5) + '" text-anchor="middle"' + fit + '>' + esc(l) + '</text></g>';
      });
      s += '</svg>';
      el.classList.add('minimapa-box');
      el.innerHTML = s + (cfg.legenda ? '<p class="minimapa-leg">' + cfg.legenda + '</p>' : '');
      return {};
    });
  }

  window.Labs = { register, plataforma, miniMapa, vscode, terminal, siem, browser, flow, scene3d, highlight, sleep, esc, h };
})();
