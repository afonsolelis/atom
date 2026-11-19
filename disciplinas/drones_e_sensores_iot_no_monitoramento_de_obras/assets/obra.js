/* =====================================================================
   obra.js — cenas 3D, animações e calculadoras dos decks de
   "Drones e Sensores IoT no Monitoramento de Obras".

   Uso no HTML (carregar ANTES de deck.js, no fim do <body>):
     <div class="viz" data-viz="canteiro3d" data-opts='{"drone":true}'></div>

   Cada visualização só é construída quando o slide entra em cena
   (evento "slide:enter" de deck.js) e pausa ao sair ("slide:leave").

   Visualizações prontas (data-viz):
     3D (three.js r128, cdnjs):  canteiro3d · gemeo3d · drone3d
     2D (canvas):                malha · sensor · amostragem · rede · cobertura
     Genérica:                   calc   (calculadora declarativa, ver abaixo)
   Extras: .contador[data-ate]  (número que sobe ao entrar no slide)

   Novas visualizações específicas de uma aula:
     Obra.register('nome', (el, opts, painel) => ({ start(){}, stop(){} }));
   ===================================================================== */
(function () {
  'use strict';
  const THREE_URL = 'https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js';
  const COR = { azul: 0x002156, ciano: 0x2bd9fe, amarelo: 0xf2cb0a, alerta: 0xff2b5f, ok: 0x11a360, laranja: 0xff8a1f, concreto: 0xb9bcc2, terra: 0x8a6f4d, grama: 0x47703f };
  const R = {};
  const fmt = (v, d = 0) => Number(v).toLocaleString('pt-BR', { minimumFractionDigits: d, maximumFractionDigits: d });
  const clamp = (v, a, b) => Math.max(a, Math.min(b, v));
  const lerp = (a, b, t) => a + (b - a) * t;

  let threeP = null;
  function loadThree() {
    if (window.THREE) return Promise.resolve(window.THREE);
    if (!threeP) threeP = new Promise((res, rej) => {
      const s = document.createElement('script');
      s.src = THREE_URL; s.onload = () => res(window.THREE); s.onerror = () => rej(new Error('three.js indisponível'));
      document.head.appendChild(s);
    });
    return threeP;
  }

  /* ---------- utilidades ---------- */
  function el(tag, attrs = {}, html) {
    const e = document.createElement(tag);
    for (const k in attrs) e.setAttribute(k, attrs[k]);
    if (html != null) e.innerHTML = html;
    return e;
  }
  function loop(fn) {
    let raf = 0, last = 0, t = 0, on = false;
    const tick = (now) => {
      if (!on) return;
      const dt = last ? Math.min(0.05, (now - last) / 1000) : 0;
      last = now; t += dt; fn(t, dt);
      raf = requestAnimationFrame(tick);
    };
    return {
      start() { if (on) return; on = true; last = 0; raf = requestAnimationFrame(tick); },
      stop() { on = false; cancelAnimationFrame(raf); },
      get t() { return t; }, reset() { t = 0; }
    };
  }
  function canvas2d(host) {
    const cv = el('canvas'); host.appendChild(cv);
    const ctx = cv.getContext('2d');
    const o = { cv, ctx, w: 1, h: 1 };
    const fit = () => {
      const r = host.getBoundingClientRect(), dpr = Math.min(2, window.devicePixelRatio || 1);
      o.w = Math.max(1, r.width); o.h = Math.max(1, r.height);
      cv.width = o.w * dpr; cv.height = o.h * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    };
    fit(); new ResizeObserver(fit).observe(host);
    return o;
  }
  function hud(host) { const h = el('div', { class: 'hud' }); host.appendChild(h); return h; }
  function chip(h, html, cls) { const c = el('span', { class: 'chip' + (cls ? ' ' + cls : '') }, html); h.appendChild(c); return c; }
  function botoes(host, lista) {
    const box = el('div', { class: 'controles' }); host.appendChild(box);
    // o HUD (chips, à esquerda) não pode passar por baixo dos botões (à direita)
    new ResizeObserver(() => host.style.setProperty('--ctrl-w', (box.offsetWidth + 12) + 'px')).observe(box);
    return lista.map(([txt, fn, on]) => {
      const b = el('button', { class: 'btn-viz' + (on ? ' on' : ''), type: 'button' }, txt);
      b.addEventListener('click', (e) => { e.stopPropagation(); fn(b); }); box.appendChild(b); return b;
    });
  }
  function grupoExclusivo(btns, i) { btns.forEach((b, k) => b.classList.toggle('on', k === i)); }
  function dica(host, txt) { host.appendChild(el('p', { class: 'dica' }, txt)); }
  function slider(painel, { id, label, min, max, step, value, unit = '', dec }) {
    const d = el('div', { class: 'ctrl' });
    const casas = dec != null ? dec : (String(step).split('.')[1] || '').length;
    d.innerHTML = `<label><span>${label}</span><output></output></label><input type="range" min="${min}" max="${max}" step="${step}" value="${value}" data-id="${id}">`;
    const inp = d.querySelector('input'), out = d.querySelector('output');
    const show = () => { out.textContent = fmt(inp.value, casas) + (unit ? ' ' + unit : ''); };
    inp.addEventListener('input', show); show(); inp.classList.add('no-nav');
    painel.appendChild(d); return inp;
  }

  /* ---------- base 3D: cena, câmera orbital por arraste, rótulos ---------- */
  function cena3d(host, opts, build) {
    return loadThree().then((THREE) => {
      const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
      renderer.setPixelRatio(Math.min(2, window.devicePixelRatio || 1));
      renderer.shadowMap.enabled = true; renderer.shadowMap.type = THREE.PCFSoftShadowMap;
      host.appendChild(renderer.domElement);
      const scene = new THREE.Scene();
      scene.fog = new THREE.Fog(0x0b1a33, opts.fogNear || 160, opts.fogFar || 420);
      const cam = new THREE.PerspectiveCamera(45, 1, 0.1, 2000);
      const alvo = new THREE.Vector3(...(opts.alvo || [0, 8, 0]));
      const orb = { th: opts.th != null ? opts.th : 0.8, ph: opts.ph != null ? opts.ph : 1.05, r: opts.r || 140, auto: opts.auto !== false };
      const posCam = () => {
        cam.position.set(alvo.x + orb.r * Math.sin(orb.ph) * Math.sin(orb.th), alvo.y + orb.r * Math.cos(orb.ph), alvo.z + orb.r * Math.sin(orb.ph) * Math.cos(orb.th));
        cam.lookAt(alvo);
      };
      scene.add(new THREE.HemisphereLight(0xdbe8ff, 0x3a3020, 0.75));
      const sol = new THREE.DirectionalLight(0xffffff, 0.9);
      sol.position.set(80, 140, 60); sol.castShadow = true;
      sol.shadow.mapSize.set(1024, 1024);
      Object.assign(sol.shadow.camera, { left: -120, right: 120, top: 120, bottom: -120, far: 400 });
      scene.add(sol);
      // arrastar para girar, roda para aproximar
      let drag = null, parado = 0;
      const dom = renderer.domElement; dom.style.cursor = 'grab'; dom.style.touchAction = 'none';
      dom.addEventListener('pointerdown', (e) => { drag = [e.clientX, e.clientY]; dom.setPointerCapture(e.pointerId); dom.style.cursor = 'grabbing'; });
      dom.addEventListener('pointermove', (e) => {
        if (!drag) return;
        orb.th -= (e.clientX - drag[0]) * 0.006; orb.ph = clamp(orb.ph - (e.clientY - drag[1]) * 0.005, 0.25, 1.5);
        drag = [e.clientX, e.clientY]; parado = 0;
      });
      dom.addEventListener('pointerup', () => { drag = null; dom.style.cursor = 'grab'; });
      dom.addEventListener('wheel', (e) => { e.preventDefault(); orb.r = clamp(orb.r * (1 + Math.sign(e.deltaY) * 0.08), (opts.r || 140) * 0.35, (opts.r || 140) * 2); }, { passive: false });
      // rótulos HTML presos a objetos 3D
      const rotulos = [];
      const rotulo = (obj, txt, dy = 0) => { const d = el('div', { class: 'rotulo3d' }, txt); host.appendChild(d); rotulos.push({ obj, d, dy }); return d; };
      const v = new THREE.Vector3();
      const fit = () => {
        const r = host.getBoundingClientRect();
        renderer.setSize(r.width, r.height, false); renderer.domElement.style.width = '100%'; renderer.domElement.style.height = '100%';
        cam.aspect = r.width / Math.max(1, r.height); cam.updateProjectionMatrix();
      };
      fit(); new ResizeObserver(fit).observe(host);
      const ctx = { THREE, scene, cam, renderer, orb, alvo, rotulo, host };
      const update = build(ctx) || (() => {});
      const lp = loop((t, dt) => {
        parado += dt;
        if (orb.auto && !drag && parado > 2) orb.th += dt * 0.08;
        posCam(); update(t, dt);
        renderer.render(scene, cam);
        const r = host.getBoundingClientRect();
        const pos = [];
        for (const rt of rotulos) {
          const { obj, d, dy } = rt;
          obj.getWorldPosition(v); v.y += dy; v.project(cam);
          const vis = v.z < 1 && obj.visible !== false && !d.dataset.oculto;
          d.style.opacity = vis ? 1 : 0;
          // mantém o rótulo inteiro dentro da cena (não corta na borda)
          const w = d.offsetWidth, hh = d.offsetHeight, meia = w / 2 + 4;
          const x = clamp(((v.x + 1) / 2) * r.width, meia, r.width - meia);
          const y = clamp(((1 - v.y) / 2) * r.height, hh + 40, r.height - 4);
          if (vis) pos.push({ d, x, y, w, hh }); else { d.style.left = x + 'px'; d.style.top = y + 'px'; }
        }
        // rótulos não se sobrepõem: o de baixo desce até ficar livre
        pos.sort((a, b) => a.y - b.y);
        pos.forEach((p, i) => {
          for (let volta = 0; volta < 6; volta++) {
            const choque = pos.slice(0, i).find((q) => Math.abs(q.x - p.x) < (q.w + p.w) / 2 + 4 && Math.abs(q.y - p.y) < (q.hh + p.hh) / 2 + 3);
            if (!choque) break;
            p.y = choque.y + choque.hh + 3;
          }
          p.y = Math.min(p.y, r.height - 4);
          p.d.style.left = p.x + 'px'; p.d.style.top = p.y + 'px';
        });
      });
      dica(host, 'Arraste para girar · role para aproximar');
      return { start: lp.start, stop: lp.stop };
    }).catch(() => {
      host.innerHTML = '<p style="padding:1rem">Não foi possível carregar a cena 3D (sem internet?). O conteúdo do slide continua válido.</p>';
      return { start() {}, stop() {} };
    });
  }

  /* peças reutilizáveis */
  function mat(THREE, cor, extra = {}) { return new THREE.MeshStandardMaterial({ color: cor, roughness: 0.8, metalness: 0.1, ...extra }); }
  function caixa(THREE, w, h, d, cor, extra) {
    const m = new THREE.Mesh(new THREE.BoxGeometry(w, h, d), mat(THREE, cor, extra));
    m.castShadow = true; m.receiveShadow = true; return m;
  }
  function droneModelo(THREE, escala = 1) {
    const g = new THREE.Group(), helices = [], partes = {};
    const corpo = caixa(THREE, 2.2, 0.7, 3, 0xe8ecf2, { metalness: 0.3, roughness: 0.4 });
    g.add(corpo); partes.corpo = corpo;
    const braco = (ang) => {
      const a = new THREE.Group(); a.rotation.y = ang;
      const b = new THREE.Mesh(new THREE.CylinderGeometry(0.12, 0.12, 3.4, 8), mat(THREE, 0x30343c));
      b.rotation.z = Math.PI / 2; b.position.x = 1.7; a.add(b);
      const mot = new THREE.Mesh(new THREE.CylinderGeometry(0.32, 0.32, 0.5, 14), mat(THREE, 0x50545c, { metalness: 0.6 }));
      mot.position.set(3.4, 0.25, 0); a.add(mot);
      const h = new THREE.Mesh(new THREE.BoxGeometry(3.2, 0.04, 0.32), mat(THREE, 0x1b1f27, { transparent: true, opacity: 0.85 }));
      h.position.set(3.4, 0.55, 0); a.add(h); helices.push(h);
      const luz = new THREE.Mesh(new THREE.SphereGeometry(0.12, 8, 8), new THREE.MeshBasicMaterial({ color: ang < Math.PI ? 0xff3344 : 0x33ff88 }));
      luz.position.set(3.4, -0.1, 0); a.add(luz);
      return a;
    };
    [Math.PI / 4, 3 * Math.PI / 4, 5 * Math.PI / 4, 7 * Math.PI / 4].forEach((a) => g.add(braco(a)));
    const gimbal = new THREE.Group(); gimbal.position.set(0, -0.75, 1);
    const cam = caixa(THREE, 0.8, 0.7, 0.8, 0x1d2129); gimbal.add(cam);
    const lente = new THREE.Mesh(new THREE.CylinderGeometry(0.22, 0.22, 0.2, 16), mat(THREE, 0x0a63a8, { metalness: 0.8, roughness: 0.2 }));
    lente.rotation.x = Math.PI / 2; lente.position.z = 0.45; gimbal.add(lente);
    g.add(gimbal); partes.gimbal = gimbal;
    g.scale.setScalar(escala);
    return { g, helices, partes };
  }

  /* =========================================================
     canteiro3d — canteiro de obras vivo: prédio subindo,
     grua, escavação com sensores, gateway IoT, nuvem e drone
     fazendo varredura fotogramétrica.
     opts: drone, sensores, guindaste, predio (bool, padrão true)
     ========================================================= */
  R.canteiro3d = (host, opts) => {
    const o = { drone: true, sensores: true, guindaste: true, predio: true, ...opts };
    const h = hud(host);
    const cAnd = o.predio ? chip(h, 'Pavimentos: <b>0</b>') : null;
    const cCob = o.drone ? chip(h, 'Cobertura do voo: <b>0%</b>') : null;
    const cPac = o.sensores ? chip(h, 'Leituras recebidas: <b>0</b>') : null;
    return cena3d(host, { r: 158, ph: 0.98, alvo: [-5, 14, 0] }, ({ THREE, scene, rotulo }) => {
      // terreno
      const fGrama = new THREE.Shape([new THREE.Vector2(-300, -300), new THREE.Vector2(300, -300), new THREE.Vector2(300, 300), new THREE.Vector2(-300, 300)]);
      fGrama.holes.push(new THREE.Path([new THREE.Vector2(-65, -50), new THREE.Vector2(65, -50), new THREE.Vector2(65, 50), new THREE.Vector2(-65, 50)]));
      const grama = new THREE.Mesh(new THREE.ShapeGeometry(fGrama), mat(THREE, COR.grama, { side: THREE.DoubleSide }));
      grama.rotation.x = -Math.PI / 2; grama.position.y = -0.05; grama.receiveShadow = true; scene.add(grama);
      // lote com um furo onde fica a escavação (senão o terreno tampa o subsolo)
      const forma = new THREE.Shape([new THREE.Vector2(-65, -50), new THREE.Vector2(65, -50), new THREE.Vector2(65, 50), new THREE.Vector2(-65, 50)]);
      forma.holes.push(new THREE.Path([new THREE.Vector2(-48, -5), new THREE.Vector2(-12, -5), new THREE.Vector2(-12, 25), new THREE.Vector2(-48, 25)]));
      const lote = new THREE.Mesh(new THREE.ShapeGeometry(forma), mat(THREE, COR.terra, { side: THREE.DoubleSide }));
      lote.rotation.x = -Math.PI / 2; lote.receiveShadow = true; scene.add(lote);
      const grade = new THREE.GridHelper(130, 26, 0xffffff, 0xffffff); grade.material.opacity = 0.06; grade.material.transparent = true; grade.position.y = 0.02; scene.add(grade);
      // tapume
      for (const [x, z, w, d] of [[0, 50, 130, 0.4], [0, -50, 130, 0.4], [65, 0, 0.4, 100], [-65, 0, 0.4, 100]]) {
        const t = caixa(THREE, w, 2.4, d, 0x1f4f99); t.position.set(x, 1.2, z); scene.add(t);
      }
      // escavação (subsolo) com cortina de contenção
      const cava = new THREE.Group(); cava.position.set(-30, 0, -10); scene.add(cava);
      const fundo = new THREE.Mesh(new THREE.PlaneGeometry(36, 30), mat(THREE, 0x5d4a33)); fundo.rotation.x = -Math.PI / 2; fundo.position.y = -7.9; cava.add(fundo);
      const paredes = [];
      for (const [x, z, w, d] of [[0, 15, 36, 0.8], [0, -15, 36, 0.8], [18, 0, 0.8, 30], [-18, 0, 0.8, 30]]) {
        const p = caixa(THREE, w, 8, d, 0x9a9da3); p.position.set(x, -4, z); cava.add(p); paredes.push(p);
      }
      // escoras
      for (let k = -1; k <= 1; k++) { const e = caixa(THREE, 35, 0.6, 0.6, COR.amarelo); e.position.set(0, -2, k * 9); cava.add(e); }
      // prédio que sobe
      const predio = new THREE.Group(); predio.position.set(25, 0, 5); scene.add(predio);
      const pav = [], NP = 9, HP = 3.4;
      for (let i = 0; i < NP; i++) {
        const laje = caixa(THREE, 30, 0.5, 22, COR.concreto); laje.position.y = i * HP + HP;
        const pil = new THREE.Group();
        for (const px of [-14, -5, 5, 14]) for (const pz of [-10, 0, 10]) { const c = caixa(THREE, 0.8, HP, 0.8, 0xa7aab0); c.position.set(px, i * HP + HP / 2, pz); pil.add(c); }
        const forma = caixa(THREE, 30.4, 0.3, 22.4, 0xc0782f); forma.position.y = i * HP + HP + 0.4;
        const grupo = new THREE.Group(); grupo.add(laje, pil, forma); grupo.visible = !o.predio || false; predio.add(grupo); pav.push({ grupo, forma });
      }
      if (!o.predio) pav.forEach((p) => { p.grupo.visible = true; p.forma.visible = false; });
      // grua
      let lanca = null, carro = null, cabo = null, carga = null;
      if (o.guindaste) {
        const grua = new THREE.Group(); grua.position.set(5, 0, 25); scene.add(grua);
        const torre = new THREE.Mesh(new THREE.BoxGeometry(2, 48, 2), new THREE.MeshStandardMaterial({ color: COR.amarelo, wireframe: true }));
        torre.position.y = 24; grua.add(torre);
        const nucleo = caixa(THREE, 1.2, 48, 1.2, 0xd8b40a); nucleo.position.y = 24; grua.add(nucleo);
        lanca = new THREE.Group(); lanca.position.y = 48; grua.add(lanca);
        const jib = caixa(THREE, 52, 1.2, 1.4, COR.amarelo); jib.position.x = 18; lanca.add(jib);
        const contra = caixa(THREE, 14, 1.2, 1.6, COR.amarelo); contra.position.x = -9; lanca.add(contra);
        const peso = caixa(THREE, 4, 3, 3, 0x777b82); peso.position.set(-14, -1.5, 0); lanca.add(peso);
        const cab = caixa(THREE, 3, 3, 3, 0x2a5cc4); cab.position.set(1.8, -2, 0); lanca.add(cab);
        const topo = caixa(THREE, 1, 8, 1, COR.amarelo); topo.position.y = 4.5; lanca.add(topo);
        carro = caixa(THREE, 2, 0.8, 1.6, 0x444); carro.position.set(30, -1, 0); lanca.add(carro);
        cabo = new THREE.Mesh(new THREE.CylinderGeometry(0.08, 0.08, 1, 4), mat(THREE, 0x222222)); lanca.add(cabo);
        carga = caixa(THREE, 3, 2, 3, 0x8b5a2b); lanca.add(carga);
        rotulo(topo, 'Grua (sensor de vento)', 6);
      }
      // gateway + nuvem
      const gw = new THREE.Group(); gw.position.set(-52, 0, 38); scene.add(gw);
      const poste = new THREE.Mesh(new THREE.CylinderGeometry(0.4, 0.5, 18, 10), mat(THREE, 0xdddddd)); poste.position.y = 9; gw.add(poste);
      const antena = new THREE.Mesh(new THREE.ConeGeometry(0.6, 3, 10), mat(THREE, 0xffffff)); antena.position.y = 19.5; gw.add(antena);
      const anel = new THREE.Mesh(new THREE.TorusGeometry(2, 0.12, 6, 40), new THREE.MeshBasicMaterial({ color: COR.ciano, transparent: true }));
      anel.rotation.x = Math.PI / 2; anel.position.y = 19; gw.add(anel);
      const nuvem = new THREE.Group(); nuvem.position.set(-38, 50, -42); scene.add(nuvem);
      for (const [x, y, z, r] of [[0, 0, 0, 7], [7, -1, 2, 5.5], [-7, -1, 1, 5.5], [3, 3, -2, 5], [-3, 2.5, 3, 4.5]]) {
        const b = new THREE.Mesh(new THREE.SphereGeometry(r, 18, 14), new THREE.MeshStandardMaterial({ color: 0xffffff, emissive: 0x2a6fa8, emissiveIntensity: 0.25, transparent: true, opacity: 0.92 }));
        b.position.set(x, y, z); nuvem.add(b);
      }
      rotulo(antena, 'Gateway LoRaWAN', 3);
      rotulo(nuvem, 'Nuvem · plataforma e gêmeo digital', 9);
      // referências de escala: caminhão basculante (~10 m) e uma pessoa de 1,75 m
      const caminhao = new THREE.Group(); caminhao.position.set(20, 0, 32); caminhao.rotation.y = 0.8; scene.add(caminhao);
      const cabine = caixa(THREE, 2.5, 3.2, 2.5, 0xe8ecf2); cabine.position.set(-3.8, 1.6, 0); caminhao.add(cabine);
      const cacamba = caixa(THREE, 6.6, 2.4, 2.5, COR.laranja); cacamba.position.set(1.2, 2.0, 0); caminhao.add(cacamba);
      for (const rx of [-3.8, 0, 2.8]) for (const rz of [-1.3, 1.3]) {
        const roda = new THREE.Mesh(new THREE.CylinderGeometry(0.55, 0.55, 0.4, 12), mat(THREE, 0x1b1f27)); roda.rotation.x = Math.PI / 2; roda.position.set(rx, 0.55, rz); caminhao.add(roda);
      }
      rotulo(cabine, 'Caminhão (≈ 10 m)', 2.4);
      const pessoa = new THREE.Group(); pessoa.position.set(6, 0, 34); scene.add(pessoa);
      const tronco = new THREE.Mesh(new THREE.CylinderGeometry(0.28, 0.24, 1.25, 10), mat(THREE, COR.laranja)); tronco.position.y = 0.95; pessoa.add(tronco);
      const cabeca = new THREE.Mesh(new THREE.SphereGeometry(0.22, 10, 8), mat(THREE, 0xf2f2f2)); cabeca.position.y = 1.53; pessoa.add(cabeca);
      const pernas = new THREE.Mesh(new THREE.CylinderGeometry(0.2, 0.18, 0.35, 8), mat(THREE, 0x30343c)); pernas.position.y = 0.17; pessoa.add(pernas);
      rotulo(cabeca, 'Pessoa (1,75 m)', 0.6);
      // sensores
      const sensores = [], pacotes = [];
      let recebidas = 0;
      if (o.sensores) {
        const sGeo = new THREE.SphereGeometry(0.9, 12, 10);
        const pos = [
          [cava, -18, -3, 6, 'Inclinômetro'], [cava, 18, -5, -6, 'Piezômetro'], [cava, 0, -1, 15, null],
          [predio, -15, 6, 11, 'Extensômetro'], [predio, 15, 13, -11, null], [scene, 42, 1.5, -40, 'Medidor de vibração'], [scene, -60, 3, -45, null]
        ];
        for (const [pai, x, y, z, nome] of pos) {
          const s = new THREE.Mesh(sGeo, new THREE.MeshBasicMaterial({ color: COR.ok }));
          s.position.set(x, y, z); pai.add(s); sensores.push({ s, fase: Math.random() * 3 });
          if (nome) rotulo(s, nome, 1.5);
        }
      }
      const pGeo = new THREE.SphereGeometry(1.25, 12, 10);
      const destGw = new THREE.Vector3(-52, 19, 38), destN = new THREE.Vector3(-38, 47, -42), tmp = new THREE.Vector3();
      // drone
      let dr = null, rastro = [], cobertos = new Set();
      const NX = 8, NZ = 6, CX = 130 / NX, CZ = 100 / NZ;
      if (o.drone) {
        dr = droneModelo(THREE, 1.4); scene.add(dr.g);
        const cone = new THREE.Mesh(new THREE.ConeGeometry(11, 36, 4, 1, true), new THREE.MeshBasicMaterial({ color: COR.ciano, transparent: true, opacity: 0.13, side: THREE.DoubleSide, depthWrite: false }));
        cone.rotation.y = Math.PI / 4; cone.position.y = -18; dr.g.add(cone);
        rotulo(dr.g, 'Drone · varredura fotogramétrica', 3);
        const tGeo = new THREE.PlaneGeometry(CX * 0.96, CZ * 0.96);
        for (let i = 0; i < NX * NZ; i++) {
          const t = new THREE.Mesh(tGeo, new THREE.MeshBasicMaterial({ color: COR.ciano, transparent: true, opacity: 0, depthWrite: false }));
          t.rotation.x = -Math.PI / 2; t.position.set(-65 + CX * (i % NX + 0.5), 0.12, -50 + CZ * (Math.floor(i / NX) + 0.5)); scene.add(t); rastro.push(t);
        }
      }
      let proxPacote = 0, proxPav = 0, nPav = 0;
      return (t, dt) => {
        // prédio: um pavimento a cada 2,5 s, recomeça ao completar
        if (o.predio && t > proxPav) {
          proxPav = t + 2.5;
          if (nPav >= NP) { nPav = 0; pav.forEach((p) => (p.grupo.visible = false)); }
          pav[nPav].grupo.visible = true; pav.forEach((p, k) => (p.forma.visible = k === nPav)); nPav++;
          if (cAnd) cAnd.innerHTML = `Pavimentos: <b>${nPav}</b> de ${NP}`;
        }
        if (lanca) {
          lanca.rotation.y = Math.sin(t * 0.25) * 1.3;
          const x = 22 + Math.sin(t * 0.6) * 12; carro.position.x = x;
          const L = 14 + Math.sin(t * 0.9) * 8;
          cabo.scale.y = L; cabo.position.set(x, -1 - L / 2, 0); carga.position.set(x, -2 - L, 0);
        }
        anel.scale.setScalar(1 + (t * 1.5 % 1) * 2); anel.material.opacity = 1 - (t * 1.5 % 1);
        sensores.forEach(({ s, fase }) => s.scale.setScalar(1 + 0.35 * Math.sin(t * 4 + fase)));
        // pacotes: sensor -> gateway -> nuvem
        if (sensores.length && t > proxPacote) {
          proxPacote = t + 0.35;
          const { s } = sensores[Math.floor(Math.random() * sensores.length)];
          const p = new THREE.Mesh(pGeo, new THREE.MeshBasicMaterial({ color: COR.amarelo }));
          s.getWorldPosition(p.position); scene.add(p);
          pacotes.push({ p, a: p.position.clone(), k: 0, fase: 0 });
        }
        for (let i = pacotes.length - 1; i >= 0; i--) {
          const q = pacotes[i]; q.k += dt * (q.fase ? 0.45 : 0.6);
          const fim = q.fase ? destN : destGw;
          tmp.copy(q.a).lerp(fim, Math.min(1, q.k)); tmp.y += Math.sin(Math.min(1, q.k) * Math.PI) * 10; q.p.position.copy(tmp);
          if (q.k >= 1) {
            if (!q.fase) { q.fase = 1; q.k = 0; q.a = destGw.clone(); q.p.material.color.setHex(COR.ciano); }
            else { scene.remove(q.p); pacotes.splice(i, 1); recebidas++; if (cPac) cPac.innerHTML = `Leituras recebidas: <b>${fmt(recebidas)}</b>`; }
          }
        }
        // drone em "zigue-zague" (padrão de cortador de grama)
        if (dr) {
          dr.helices.forEach((hh, k) => (hh.rotation.y += (k % 2 ? 1 : -1) * 0.9));
          const ciclo = 26, u = (t % ciclo) / ciclo, faixa = u * NZ, iz = Math.floor(faixa), f = faixa - iz;
          const x = iz % 2 ? 60 - f * 120 : -60 + f * 120, z = -50 + CZ * (iz + 0.5);
          const nx = (iz % 2 ? -1 : 1);
          dr.g.position.set(x, 36 + Math.sin(t * 2) * 0.4, z); dr.g.rotation.y = nx > 0 ? -Math.PI / 2 : Math.PI / 2;
          if (u < 0.01) { cobertos.clear(); rastro.forEach((r) => (r.material.opacity = 0)); }
          const ix = clamp(Math.floor((x + 65) / CX), 0, NX - 1), id = iz * NX + ix;
          if (rastro[id] && !cobertos.has(id)) { cobertos.add(id); rastro[id].material.opacity = 0.28; }
          if (cCob) cCob.innerHTML = `Cobertura do voo: <b>${Math.round(cobertos.size / (NX * NZ) * 100)}%</b>`;
        }
      };
    });
  };

  /* =========================================================
     gemeo3d — prédio real × gêmeo digital, ligados por dados.
     "Simular recalque" inclina o prédio real; o gêmeo acompanha
     e colore por nível de alerta. Em malha fechada, o gêmeo
     devolve um comando (ação) que estabiliza o recalque.
     ========================================================= */
  R.gemeo3d = (host) => {
    const h = hud(host);
    const cInc = chip(h, 'Distorção angular: <b>0</b>');
    const cSt = chip(h, 'Situação: <b>normal</b>');
    let recalcando = false, fechada = true, theta = 0, acao = false;
    const btns = botoes(host, [
      ['▶ Simular recalque', (b) => { recalcando = !recalcando; b.classList.toggle('on', recalcando); }],
      ['Malha fechada', () => { fechada = true; grupoExclusivo(btns.slice(1, 3), 0); }, true],
      ['Malha aberta', () => { fechada = false; acao = false; grupoExclusivo(btns.slice(1, 3), 1); }],
      ['↺ Reiniciar', () => { theta = 0; acao = false; recalcando = false; btns[0].classList.remove('on'); }]
    ]);
    return cena3d(host, { r: 95, ph: 1.12, alvo: [0, 13, 0], th: 0.2 }, ({ THREE, scene, rotulo }) => {
      const chao = new THREE.Mesh(new THREE.PlaneGeometry(400, 400), mat(THREE, 0x2b3a52)); chao.rotation.x = -Math.PI / 2; chao.receiveShadow = true; scene.add(chao);
      const grade = new THREE.GridHelper(400, 80, COR.ciano, COR.ciano); grade.material.transparent = true; grade.material.opacity = 0.08; scene.add(grade);
      const NP = 8, HP = 3.6;
      // prédio real
      const real = new THREE.Group(); real.position.set(-28, 0, 0); scene.add(real);
      const andaresR = [];
      for (let i = 0; i < NP; i++) {
        const a = caixa(THREE, 16, HP - 0.3, 14, i % 2 ? 0xc9ccd2 : 0xbfc3ca); a.position.y = i * HP + HP / 2; real.add(a); andaresR.push(a);
        for (let j = -2; j <= 2; j++) { const jan = caixa(THREE, 2, 1.6, 0.2, 0x335577, { metalness: 0.6, roughness: 0.2 }); jan.position.set(j * 3, i * HP + HP / 2, 7.05); real.add(jan); }
      }
      const sens = [];
      for (const [x, y, z] of [[8.1, 4, 5], [8.1, 15, -5], [-8.1, 26, 3]]) {
        const s = new THREE.Mesh(new THREE.SphereGeometry(0.6, 10, 8), new THREE.MeshBasicMaterial({ color: COR.ok })); s.position.set(x, y, z); real.add(s); sens.push(s);
      }
      rotulo(andaresR[NP - 1], 'Prédio real (físico)', 4);
      // gêmeo digital
      const gem = new THREE.Group(); gem.position.set(28, 0, 0); scene.add(gem);
      const andaresG = [];
      for (let i = 0; i < NP; i++) {
        const geo = new THREE.BoxGeometry(16, HP - 0.3, 14);
        const m = new THREE.Mesh(geo, new THREE.MeshBasicMaterial({ color: COR.ok, transparent: true, opacity: 0.18 }));
        const arestas = new THREE.LineSegments(new THREE.EdgesGeometry(geo), new THREE.LineBasicMaterial({ color: COR.ciano }));
        m.add(arestas); m.position.y = i * HP + HP / 2; gem.add(m); andaresG.push(m);
      }
      rotulo(andaresG[NP - 1], 'Gêmeo digital (modelo vivo)', 4);
      // fluxos de dados
      const ida = [], volta = [];
      const pGeo = new THREE.SphereGeometry(0.45, 8, 6);
      for (let k = 0; k < 18; k++) { const p = new THREE.Mesh(pGeo, new THREE.MeshBasicMaterial({ color: COR.amarelo })); scene.add(p); ida.push({ p, f: k / 18 }); }
      for (let k = 0; k < 10; k++) { const p = new THREE.Mesh(pGeo, new THREE.MeshBasicMaterial({ color: COR.alerta })); p.visible = false; scene.add(p); volta.push({ p, f: k / 10 }); }
      const curva = (f, y0, alt) => new THREE.Vector3(lerp(-20, 20, f), y0 + Math.sin(f * Math.PI) * alt, 0);
      const rotData = rotulo(ida[9].p, 'dados dos sensores →', 1.5);
      const rotAcao = rotulo(volta[5].p, '← comando / ação na obra', -2.5);
      const corPorNivel = (r) => (r < 1 / 500 * 0.5 ? COR.ok : r < 1 / 500 ? COR.amarelo : COR.alerta);
      return (t, dt) => {
        // taxa de rotação (exagerada no desenho); a ação corta a taxa
        if (recalcando) theta += dt * (acao ? 0.00002 : 0.0011);
        const beta = theta; // distorção angular ~ rotação
        if (fechada && beta > 1 / 1000) acao = true; // nível de atenção dispara a ação
        real.rotation.z = -beta * 40; gem.rotation.z = -beta * 40;
        const cor = corPorNivel(beta);
        andaresG.forEach((a, i) => a.material.color.setHex(i < 2 ? cor : corPorNivel(beta * (0.6 + i * 0.06))));
        sens.forEach((s) => s.material.color.setHex(cor));
        ida.forEach((q) => { q.f = (q.f + dt * 0.35) % 1; q.p.position.copy(curva(q.f, 22, 10)); });
        volta.forEach((q) => { q.p.visible = acao; q.f = (q.f + dt * 0.35) % 1; q.p.position.copy(curva(1 - q.f, 8, -4)); });
        rotAcao.dataset.oculto = acao ? '' : '1'; if (!acao) rotAcao.style.opacity = 0;
        const inv = beta > 0 ? Math.round(1 / beta) : 0;
        cInc.innerHTML = 'Distorção angular: <b>' + (beta > 0 ? '1/' + fmt(inv) : '0') + '</b>';
        const est = beta < 1 / 1000 ? 'normal' : beta < 1 / 500 ? 'atenção' : 'ALERTA — limite 1/500';
        cSt.innerHTML = 'Situação: <b>' + est + '</b>' + (acao ? ' · ação aplicada' : '');
        cSt.classList.toggle('alerta', beta >= 1 / 500);
        void rotData;
      };
    });
  };

  /* =========================================================
     drone3d — quadricóptero com vista explodida e rótulos.
     ========================================================= */
  R.drone3d = (host) => {
    let explodir = 0, alvoE = 0;
    botoes(host, [['Vista explodida', (b) => { alvoE = alvoE ? 0 : 1; b.classList.toggle('on', !!alvoE); }]]);
    const aviso = el('p', { class: 'dica', style: 'left:auto;right:.8rem;transition:opacity .3s' }, 'Clique em <b>Vista explodida</b> para ver o nome de cada peça');
    host.appendChild(aviso);
    return cena3d(host, { r: 15.5, ph: 1.1, alvo: [0, 0.2, 0], fogNear: 60, fogFar: 200 }, ({ THREE, scene, rotulo }) => {
      // luz extra: o modelo é escuro (fibra de carbono) e sumia no fundo azul
      scene.add(new THREE.AmbientLight(0xffffff, 0.55));
      const frente = new THREE.DirectionalLight(0xffffff, 0.6); frente.position.set(-10, 8, 14); scene.add(frente);
      const base = new THREE.Mesh(new THREE.CircleGeometry(7.5, 48), mat(THREE, 0x22385e)); base.rotation.x = -Math.PI / 2; base.position.y = -3.2; base.receiveShadow = true; scene.add(base);
      const g = new THREE.Group(); scene.add(g);
      const pecas = [], rots = [];
      const add = (obj, nome, dir, dy = 0.8) => { g.add(obj); pecas.push({ obj, p0: obj.position.clone(), dir: new THREE.Vector3(...dir) }); if (nome) rots.push(rotulo(obj, nome, dy)); return obj; };
      add(caixa(THREE, 2.6, 0.9, 3.6, 0xe8ecf2, { metalness: 0.3, roughness: 0.35 }), 'Estrutura (frame) + controladora de voo', [0, 0, 0], 1.6);
      const bat = caixa(THREE, 1.8, 0.7, 2.6, 0x3a3f4a); bat.position.y = 0.85; add(bat, 'Bateria LiPo', [0, 2.2, -0.6], 0.6);
      const gnss = new THREE.Mesh(new THREE.CylinderGeometry(0.5, 0.55, 0.3, 20), mat(THREE, 0xf2f2f2)); gnss.position.set(0, 1.35, 1); add(gnss, 'Antena GNSS / RTK', [0, 3.6, 0.8], 0.5);
      const imu = caixa(THREE, 0.6, 0.25, 0.6, 0x11a360); imu.position.set(0.6, 0.55, -1.2); add(imu, 'IMU (acelerômetros + giroscópios)', [2.4, 1.8, -1.2], 0.5);
      const radio = new THREE.Mesh(new THREE.CylinderGeometry(0.07, 0.07, 1.6, 6), mat(THREE, 0x222222)); radio.position.set(-1, 0.3, -1.9); radio.rotation.x = 0.5; add(radio, 'Rádio de telemetria / vídeo', [-2.4, 0.6, -2.6], 1);
      const helices = [];
      [[1, 1], [-1, 1], [-1, -1], [1, -1]].forEach(([sx, sz], k) => {
        const braco = new THREE.Mesh(new THREE.CylinderGeometry(0.16, 0.16, 4.2, 8), mat(THREE, 0x6b7280));
        braco.rotation.z = Math.PI / 2; braco.rotation.y = Math.atan2(-sz, sx); braco.position.set(sx * 1.5, 0, sz * 1.5);
        add(braco, null, [sx * 1.2, 0, sz * 1.2]);
        const mot = new THREE.Mesh(new THREE.CylinderGeometry(0.45, 0.45, 0.6, 16), mat(THREE, 0x60656e, { metalness: 0.7, roughness: 0.3 }));
        mot.position.set(sx * 3, 0.3, sz * 3); add(mot, k === 0 ? 'Motor sem escovas + ESC' : null, [sx * 2.4, 0.4, sz * 2.4], 0.6);
        const hel = new THREE.Mesh(new THREE.BoxGeometry(4.4, 0.06, 0.42), mat(THREE, 0x9aa3b2)); hel.position.set(sx * 3, 0.7, sz * 3);
        add(hel, k === 1 ? 'Hélices (pares em sentidos opostos)' : null, [sx * 2.4, 2.2, sz * 2.4], 0.5); helices.push(hel);
        const perna = new THREE.Mesh(new THREE.CylinderGeometry(0.08, 0.08, 1.8, 6), mat(THREE, 0x6b7280)); perna.position.set(sx * 1, -1.3, sz * 1.3); add(perna, null, [sx * 0.8, -1.6, sz * 0.8]);
      });
      const gimbal = new THREE.Group(); gimbal.position.set(0, -1.1, 1.3);
      gimbal.add(caixa(THREE, 1, 0.9, 1, 0x1d2129));
      const lente = new THREE.Mesh(new THREE.CylinderGeometry(0.3, 0.3, 0.3, 18), mat(THREE, 0x0a63a8, { metalness: 0.9, roughness: 0.15 })); lente.rotation.x = Math.PI / 2; lente.position.z = 0.6; gimbal.add(lente);
      add(gimbal, 'Gimbal + câmera (carga útil)', [0, -2.6, 2.2], 1);
      return (t, dt) => {
        explodir += (alvoE - explodir) * Math.min(1, dt * 3);
        // montado, os rótulos se sobrepõem: só aparecem na vista explodida
        rots.forEach((d) => { d.dataset.oculto = explodir > 0.6 ? '' : '1'; });
        aviso.style.opacity = explodir < 0.3 ? 1 : 0;
        pecas.forEach(({ obj, p0, dir }) => obj.position.copy(p0).addScaledVector(dir, explodir));
        helices.forEach((hh, k) => (hh.rotation.y += (k % 2 ? 1 : -1) * (0.6 - explodir * 0.5)));
        g.position.y = Math.sin(t * 1.6) * 0.25 * (1 - explodir);
      };
    });
  };

  /* =========================================================
     malha — malha aberta × malha fechada no monitoramento.
     Padrão: recalque de um vizinho durante uma escavação. Na
     fechada, leituras automáticas disparam ação ao passar o nível
     de atenção (ou de alerta, com acaoNo:"alerta"). Na aberta, a
     leitura é manual e a ação só vem depois.
     opts: nome, unidade, eixo, atencao, alerta, taxa (unid./h),
           residual (unid./h após a ação; negativo = a grandeza volta),
           max, horas, vel (h simuladas por segundo), acaoNo,
           manual (h entre leituras manuais), atrasoAberta, atrasoFechada (h),
           intMin/intMax/intPasso/intIni + intUnid ("h" ou "min"),
           base (grandeza "invertida", ex.: nível d'água em m abaixo do
           fundo da escavação: o valor mostrado é base − subida),
           rotFechada, rotAberta, dec
     ========================================================= */
  R.malha = (host, opts, painel) => {
    const o = {
      nome: 'Recalque', unidade: 'mm', atencao: 15, alerta: 25, taxa: 0.08, residual: 0.004, max: 40, horas: 480, vel: 40,
      acaoNo: 'atencao', manual: 168, atrasoAberta: 120, atrasoFechada: 1,
      intMin: 1, intMax: 48, intPasso: 1, intIni: 6, intUnid: 'h',
      rotFechada: 'ação automática', rotAberta: 'ação após relatório', dec: 1, ...opts
    };
    const inv = o.base != null;                       // grandeza que "piora" ao diminuir
    const mostra = (x) => (inv ? o.base - x : x);      // valor interno (subida) -> valor exibido
    const limA = mostra(o.atencao), limL = mostra(o.alerta), vMax = inv ? o.base : o.max;
    const limAcao = o.acaoNo === 'alerta' ? limL : limA;
    const eixo = o.eixo || o.nome.toLowerCase() + ' (' + o.unidade + ')';
    const { ctx, ...dim } = canvas2d(host);
    const h = hud(host);
    const cModo = chip(h, 'Modo: <b>malha fechada</b>'), cVal = chip(h, o.nome + ': <b>0</b>'), cEst = chip(h, 'Situação: <b>normal</b>');
    let fechada = true;
    const btns = botoes(host, [
      ['Malha fechada (IoT)', () => { fechada = true; grupoExclusivo(btns.slice(0, 2), 0); reinicia(); }, true],
      ['Malha aberta (manual)', () => { fechada = false; grupoExclusivo(btns.slice(0, 2), 1); reinicia(); }],
      ['↺ Reiniciar', () => reinicia()]
    ]);
    const sInt = painel
      ? slider(painel, { id: 'int', label: 'Intervalo entre leituras (malha fechada)', min: o.intMin, max: o.intMax, step: o.intPasso, value: o.intIni, unit: o.intUnid })
      : { value: o.intIni };
    const intH = () => (+sInt.value) / (o.intUnid === 'min' ? 60 : 1);
    const txtInt = () => fmt(+sInt.value) + ' ' + o.intUnid;
    // intervalos de dias em dias (168 h = "semanal"), não em horas
    const txtManual = o.manual >= 24
      ? (o.manual === 168 ? 'semanal (a cada 7 dias)' : 'a cada ' + fmt(o.manual / 24, o.manual % 24 ? 1 : 0) + ' dias')
      : 'a cada ' + fmt(o.manual, o.manual % 1 ? 1 : 0) + ' h';
    let tH, v, leituras, acaoEm, acaoAplicada, prox, tok;
    const ETAPAS = ['Obra', 'Sensor', 'Gateway', 'Plataforma / gêmeo', 'Decisão', 'Ação'];
    function reinicia() { tH = 0; v = 0; leituras = []; acaoEm = null; acaoAplicada = null; prox = 0; tok = -1; }
    reinicia();
    const taxaEm = (hh) => (acaoAplicada != null && hh >= acaoAplicada ? o.residual : o.taxa);
    const lp = loop((t, dt) => {
      const W = dim.w = ctx.canvas.width / Math.min(2, window.devicePixelRatio || 1), H = dim.h = ctx.canvas.height / Math.min(2, window.devicePixelRatio || 1);
      if (tH < o.horas) {
        const passo = dt * o.vel;
        for (let s = 0; s < 8; s++) {
          const dh = passo / 8; tH += dh;
          v = clamp(v + dh * taxaEm(tH), 0, vMax);
          const inter = fechada ? intH() : o.manual;
          if (tH >= prox) {
            prox += inter; leituras.push([tH, v]); tok = 0;
            if (acaoEm == null && v >= limAcao - 1e-9) {
              acaoEm = tH; acaoAplicada = tH + (fechada ? o.atrasoFechada : o.atrasoAberta);
            }
          }
        }
      }
      if (tok >= 0) tok += dt * 3;
      // desenho
      ctx.clearRect(0, 0, W, H);
      const top = 50, gx = W * 0.07, gw = W * 0.58, gh = H - top - 40, gy = top;
      const X = (hh) => gx + (hh / o.horas) * gw, Y = (x) => gy + gh - (x / vMax) * gh;
      ctx.fillStyle = 'rgba(255,255,255,.04)'; ctx.fillRect(gx, gy, gw, gh);
      ctx.fillStyle = 'rgba(255,43,95,.12)'; ctx.fillRect(gx, gy, gw, Y(limL) - gy);
      ctx.fillStyle = 'rgba(242,203,10,.10)'; ctx.fillRect(gx, Y(limL), gw, Y(limA) - Y(limL));
      ctx.font = '13px Montserrat, Arial'; ctx.textAlign = 'left';
      [[limL, '#FF2B5F', 'Nível de alerta: ' + fmt(o.alerta, o.alerta % 1 ? 1 : 0) + ' ' + o.unidade], [limA, '#F2CB0A', 'Nível de atenção: ' + fmt(o.atencao, o.atencao % 1 ? 1 : 0) + ' ' + o.unidade]].forEach(([y, c, txt]) => {
        ctx.strokeStyle = c; ctx.setLineDash([6, 5]); ctx.beginPath(); ctx.moveTo(gx, Y(y)); ctx.lineTo(gx + gw, Y(y)); ctx.stroke(); ctx.setLineDash([]);
        ctx.fillStyle = c; ctx.fillText(txt, gx + 6, Y(y) - 5);
      });
      if (inv) { ctx.fillStyle = 'rgba(255,255,255,.75)'; ctx.fillText('0 m = água no fundo da escavação', gx + 6, gy + 14); }
      ctx.fillStyle = 'rgba(255,255,255,.65)'; ctx.textAlign = 'center';
      if (o.horas <= 72) { const pz = o.horas <= 24 ? 2 : 6; for (let hh = 0; hh <= o.horas; hh += pz) ctx.fillText(hh + ' h', X(hh), gy + gh + 17); }
      else { for (let d = 0; d <= o.horas / 24; d += 5) ctx.fillText(d + ' d', X(d * 24), gy + gh + 17); }
      ctx.save(); ctx.translate(gx - 10, gy + gh / 2); ctx.rotate(-Math.PI / 2); ctx.textAlign = 'center'; ctx.fillText(eixo, 0, 0); ctx.restore();
      // curva "real"
      ctx.strokeStyle = '#2BD9FE'; ctx.lineWidth = 2.5; ctx.beginPath();
      let vv = 0; const ph = o.horas / 240; ctx.moveTo(X(0), Y(0));
      for (let hh = ph; hh <= tH; hh += ph) { vv = clamp(vv + ph * taxaEm(hh), 0, vMax); ctx.lineTo(X(hh), Y(vv)); }
      ctx.stroke(); ctx.lineWidth = 1;
      leituras.forEach(([a, b]) => { ctx.fillStyle = '#fff'; ctx.beginPath(); ctx.arc(X(a), Y(b), 3.5, 0, 7); ctx.fill(); });
      if (acaoEm != null && tH >= acaoAplicada) {
        ctx.strokeStyle = '#11A360'; ctx.beginPath(); ctx.moveTo(X(acaoAplicada), gy); ctx.lineTo(X(acaoAplicada), gy + gh); ctx.stroke();
        ctx.fillStyle = '#11A360'; ctx.font = '600 13px Montserrat, Arial'; ctx.textAlign = 'left';
        const rot = fechada ? o.rotFechada : o.rotAberta, lw = ctx.measureText(rot).width;
        ctx.fillText(rot, Math.min(X(acaoAplicada) + 5, gx + gw - lw - 4), gy + (inv ? 32 : 14));
      }
      // ciclo de etapas
      const cx = W * 0.83, cy = top + gh / 2, rr = Math.min(W * 0.13, gh * 0.4);
      ETAPAS.forEach((nome, k) => {
        const a = -Math.PI / 2 + k * (2 * Math.PI / ETAPAS.length), px = cx + rr * Math.cos(a), py = cy + rr * Math.sin(a);
        const ativo = fechada ? Math.floor(tok) === k : (k <= 1 && Math.floor(tok) === k);
        const morto = !fechada && k >= 2;
        ctx.fillStyle = ativo ? '#F2CB0A' : morto ? 'rgba(255,255,255,.08)' : 'rgba(43,217,254,.25)';
        ctx.beginPath(); ctx.arc(px, py, 9 + (ativo ? 4 : 0), 0, 7); ctx.fill();
        ctx.fillStyle = morto ? 'rgba(255,255,255,.4)' : '#fff'; ctx.textAlign = 'center'; ctx.font = '12px Montserrat, Arial';
        ctx.fillText(nome, px, py + (Math.sin(a) > 0.1 ? 26 : -16));
      });
      ctx.strokeStyle = fechada ? 'rgba(43,217,254,.6)' : 'rgba(255,255,255,.15)'; ctx.setLineDash(fechada ? [] : [4, 6]);
      ctx.beginPath(); ctx.arc(cx, cy, rr, 0, 7); ctx.stroke(); ctx.setLineDash([]);
      ctx.fillStyle = '#fff'; ctx.font = '600 13px Montserrat, Arial'; ctx.textAlign = 'center';
      ctx.fillText(fechada ? 'Malha FECHADA' : 'Malha ABERTA', cx, cy - 4);
      ctx.font = '12px Montserrat, Arial'; ctx.fillStyle = 'rgba(255,255,255,.75)';
      ctx.fillText(fechada ? 'medir → decidir → agir' : 'medir → arquivar', cx, cy + 13);
      cModo.innerHTML = 'Modo: <b>' + (fechada ? 'malha fechada, leitura a cada ' + txtInt() : 'malha aberta, leitura manual ' + txtManual) + '</b>';
      cVal.innerHTML = o.nome + ': <b>' + fmt(mostra(v), o.dec) + ' ' + o.unidade + '</b>';
      const est = v >= limL - 1e-9 ? (inv ? 'ALERTA' : 'ALERTA ultrapassado') : v >= limA - 1e-9 ? 'atenção' : 'normal';
      cEst.innerHTML = 'Situação: <b>' + est + '</b>'; cEst.classList.toggle('alerta', v >= limL - 1e-9);
    });
    return { start: lp.start, stop: lp.stop };
  };

  /* =========================================================
     sensor — exatidão × precisão (alvo) com viés e dispersão.
     ========================================================= */
  R.sensor = (host, opts, painel) => {
    const { ctx } = canvas2d(host);
    const p = painel || el('div');
    const sV = slider(p, { id: 'v', label: 'Erro sistemático (viés)', min: 0, max: 10, step: 0.5, value: 0, unit: 'mm' });
    const sD = slider(p, { id: 'd', label: 'Dispersão (desvio-padrão)', min: 0.2, max: 6, step: 0.2, value: 1, unit: 'mm' });
    const res = el('div', { class: 'resultado' }); p.appendChild(res);
    const pts = []; let prox = 0;
    const gauss = () => { let u = 0, v = 0; while (!u) u = Math.random(); while (!v) v = Math.random(); return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v); };
    const lp = loop((t) => {
      const dpr = Math.min(2, window.devicePixelRatio || 1), W = ctx.canvas.width / dpr, H = ctx.canvas.height / dpr;
      if (t > prox) { prox = t + 0.08; pts.push([+sV.value * 0.7 + gauss() * sD.value, +sV.value * 0.7 + gauss() * sD.value]); if (pts.length > 60) pts.shift(); }
      ctx.clearRect(0, 0, W, H);
      const cx = W / 2, cy = H / 2 + 10, esc = Math.min(W, H) / 34;
      ['#ffffff', '#ff2b5f', '#ffffff', '#ff2b5f', '#F2CB0A'].forEach((c, k) => {
        ctx.fillStyle = c; ctx.globalAlpha = 0.18 + k * 0.08; ctx.beginPath(); ctx.arc(cx, cy, esc * (12 - k * 2.5), 0, 7); ctx.fill();
      });
      ctx.globalAlpha = 1;
      ctx.strokeStyle = 'rgba(255,255,255,.4)'; ctx.beginPath(); ctx.moveTo(cx - esc * 16, cy); ctx.lineTo(cx + esc * 16, cy); ctx.moveTo(cx, cy - esc * 16); ctx.lineTo(cx, cy + esc * 16); ctx.stroke();
      let mx = 0, my = 0;
      pts.forEach(([x, y], k) => { mx += x; my += y; ctx.fillStyle = `rgba(43,217,254,${0.3 + 0.7 * k / pts.length})`; ctx.beginPath(); ctx.arc(cx + x * esc, cy - y * esc, 4, 0, 7); ctx.fill(); });
      mx /= pts.length || 1; my /= pts.length || 1;
      ctx.strokeStyle = '#F2CB0A'; ctx.lineWidth = 2; ctx.beginPath(); ctx.arc(cx + mx * esc, cy - my * esc, 8, 0, 7); ctx.stroke(); ctx.lineWidth = 1;
      ctx.fillStyle = '#fff'; ctx.font = '600 13px Montserrat, Arial'; ctx.textAlign = 'center';
      ctx.fillText('centro = valor verdadeiro · círculo amarelo = média das leituras · mosca = ±2 mm', cx, 22);
      const vies = +sV.value, d = +sD.value;
      const veraz = vies <= 1, preciso = d <= 1;
      res.innerHTML = `<b>${veraz ? 'Sem viés (boa veracidade)' : 'Com viés (veracidade ruim)'} · ${preciso ? 'preciso' : 'impreciso'}</b><br>` +
        `Cada leitura é <b>${veraz && preciso ? 'exata' : 'inexata'}</b>: exatidão exige veracidade <i>e</i> precisão.<br>` +
        (veraz ? '' : 'Viés se corrige com <b>calibração</b>. ') + (preciso ? '' : 'Dispersão se reduz com sensor melhor, mais leituras ou filtragem.');
    });
    return { start: lp.start, stop: lp.stop };
  };

  /* =========================================================
     amostragem — teorema de Nyquist e aliasing.
     opts: f0 (Hz) frequência do sinal
     ========================================================= */
  R.amostragem = (host, opts, painel) => {
    const f0 = (opts && opts.f0) || 5;
    const k0 = f0 / 5; // escala do controle: 5 Hz -> 2 a 60 Hz; 50 Hz -> 20 a 600 Hz
    const { ctx } = canvas2d(host);
    const p = painel || el('div');
    const sF = slider(p, { id: 'fs', label: 'Taxa de amostragem f<sub>s</sub>', min: (opts && opts.fsMin) || 2 * k0, max: (opts && opts.fsMax) || 60 * k0, step: (opts && opts.fsPasso) || k0, value: (opts && opts.fsIni) || 40 * k0, unit: 'Hz', dec: 0 });
    const res = el('div', { class: 'resultado' }); p.appendChild(res);
    const lp = loop((t) => {
      const dpr = Math.min(2, window.devicePixelRatio || 1), W = ctx.canvas.width / dpr, H = ctx.canvas.height / dpr;
      ctx.clearRect(0, 0, W, H);
      const fs = +sF.value, T = 5 / f0, x0 = 40, ww = W - 60, cy = H / 2 + 10, A = H * 0.3, desl = (t * 0.75 / f0) % (100 / f0);
      const X = (s) => x0 + (s / T) * ww, sinal = (s) => Math.sin(2 * Math.PI * f0 * (s + desl));
      ctx.strokeStyle = 'rgba(255,255,255,.2)'; ctx.beginPath(); ctx.moveTo(x0, cy); ctx.lineTo(x0 + ww, cy); ctx.stroke();
      ctx.strokeStyle = 'rgba(43,217,254,.8)'; ctx.lineWidth = 2; ctx.beginPath();
      for (let k = 0; k <= 600; k++) { const s = k / 600 * T; k ? ctx.lineTo(X(s), cy - A * sinal(s)) : ctx.moveTo(X(s), cy - A * sinal(s)); }
      ctx.stroke();
      const n = Math.floor(fs * T); ctx.strokeStyle = '#F2CB0A'; ctx.beginPath();
      for (let k = 0; k <= n; k++) { const s = k / fs; k ? ctx.lineTo(X(s), cy - A * sinal(s)) : ctx.moveTo(X(s), cy - A * sinal(s)); }
      ctx.stroke(); ctx.lineWidth = 1;
      for (let k = 0; k <= n; k++) { const s = k / fs; ctx.fillStyle = '#F2CB0A'; ctx.beginPath(); ctx.arc(X(s), cy - A * sinal(s), 4, 0, 7); ctx.fill(); }
      ctx.fillStyle = '#fff'; ctx.font = '600 13px Montserrat, Arial'; ctx.textAlign = 'left';
      ctx.fillText(`azul: vibração real (${fmt(f0)} Hz; 5 ciclos = ${fmt(T * 1000)} ms) · amarelo: o que o sensor "enxerga" com ${fmt(fs)} amostras/s`, x0, 24);
      const fa = Math.abs(f0 - Math.round(f0 / fs) * fs);
      res.innerHTML = fs > 2 * f0
        ? `<b>f<sub>s</sub> = ${fmt(fs)} Hz &gt; 2 × ${fmt(f0)} Hz.</b> A frequência do sinal é preservada${fs >= 5 * f0 ? '.' : ', mas a forma de onda ainda sai grosseira: na prática, use de 5 a 10 vezes f<sub>max</sub>.'}`
        : fs === 2 * f0
          ? `<b>No limite:</b> f<sub>s</sub> = ${fmt(fs)} Hz = 2 × ${fmt(f0)} Hz. O resultado depende da fase e pode até virar uma linha reta. Nyquist exige f<sub>s</sub> <b>maior</b> que o dobro.`
          : `<b>Aliasing!</b> Com f<sub>s</sub> = ${fmt(fs)} Hz &lt; ${fmt(2 * f0)} Hz, o sinal parece ter <span class="num">${fmt(fa, 1)} Hz</span>: uma vibração que não existe.`;
    });
    return { start: lp.start, stop: lp.stop };
  };

  /* =========================================================
     rede — alcance de Wi-Fi, LoRaWAN, NB-IoT e 4G sobre um
     mapa de 4 km; sensores conectam ou não.
     ========================================================= */
  R.rede = (host) => {
    const { ctx } = canvas2d(host);
    const TEC = {
      'Wi-Fi': { r: 0.2, taxa: 'dezenas a centenas de Mbit/s', cons: 'alto', bat: 'dias (precisa de energia)', x: 0.5, y: 0.55, cor: '#95DE68', nota: 'ao ar livre, antena externa' },
      'LoRaWAN': { r: 3, taxa: '0,3 a 50 kbit/s', cons: 'muito baixo', bat: 'anos', x: 0.5, y: 0.55, cor: '#2BD9FE', nota: 'urbano; em área aberta passa de 10 km' },
      'NB-IoT': { r: 6, taxa: 'dezenas de kbit/s', cons: 'baixo', bat: 'anos', x: 1.08, y: 0.0, cor: '#F2CB0A' },
      '4G/5G': { r: 6, taxa: 'Mbit/s (vídeo, imagens)', cons: 'alto', bat: 'horas a dias', x: 1.08, y: 0.0, cor: '#FF8A1F' }
    };
    let tec = 'LoRaWAN';
    const nomes = Object.keys(TEC);
    const btns = botoes(host, nomes.map((n, k) => [n, () => { tec = n; grupoExclusivo(btns, k); }, n === tec]));
    const h = hud(host); const info = chip(h, ''), info2 = chip(h, '');
    const nos = [[0.53, 0.585, 'piezômetro'], [0.47, 0.515, 'extensômetro'], [0.62, 0.66, 'inclinômetro'], [0.2, 0.3, 'vibração (vizinho)'], [0.85, 0.82, 'estação meteorológica'], [0.33, 0.8, 'nível de rio'], [0.1, 0.9, 'talude remoto']];
    const lp = loop((t) => {
      const dpr = Math.min(2, window.devicePixelRatio || 1), W = ctx.canvas.width / dpr, H = ctx.canvas.height / dpr;
      ctx.clearRect(0, 0, W, H);
      const L = Math.min(W, H) * 0.92, ox = (W - L) / 2, oy = (H - L) / 2, km = L / 4;
      ctx.strokeStyle = 'rgba(255,255,255,.06)';
      for (let k = 0; k <= 8; k++) { ctx.beginPath(); ctx.moveTo(ox + k * L / 8, oy); ctx.lineTo(ox + k * L / 8, oy + L); ctx.moveTo(ox, oy + k * L / 8); ctx.lineTo(ox + L, oy + k * L / 8); ctx.stroke(); }
      ctx.fillStyle = 'rgba(255,255,255,.08)';
      for (let k = 0; k < 40; k++) { const x = (k * 37 % 97) / 97, y = (k * 61 % 89) / 89; ctx.fillRect(ox + x * L, oy + y * L, 14, 10); }
      ctx.fillStyle = 'rgba(194,120,47,.5)'; ctx.fillRect(ox + 0.44 * L, oy + 0.47 * L, 0.12 * L, 0.12 * L);
      ctx.fillStyle = '#fff'; ctx.font = '12px Montserrat, Arial'; ctx.textAlign = 'center'; ctx.fillText('canteiro', ox + 0.5 * L, oy + 0.62 * L + 10);
      const T = TEC[tec], gx = ox + T.x * L, gy = oy + T.y * L, rr = T.r * km;
      const grd = ctx.createRadialGradient(gx, gy, 0, gx, gy, rr);
      grd.addColorStop(0, T.cor + '55'); grd.addColorStop(1, T.cor + '08');
      ctx.fillStyle = grd; ctx.beginPath(); ctx.arc(gx, gy, rr, 0, 7); ctx.fill();
      ctx.strokeStyle = T.cor; ctx.setLineDash([5, 5]); ctx.beginPath(); ctx.arc(gx, gy, rr, 0, 7); ctx.stroke(); ctx.setLineDash([]);
      for (let k = 0; k < 3; k++) { const f = (t * 0.5 + k / 3) % 1; ctx.strokeStyle = T.cor; ctx.globalAlpha = 1 - f; ctx.beginPath(); ctx.arc(gx, gy, Math.min(rr, 6 * km) * f, 0, 7); ctx.stroke(); }
      ctx.globalAlpha = 1;
      let ok = 0;
      nos.forEach(([x, y, nome], k) => {
        const nx = ox + x * L, ny = oy + y * L, d = Math.hypot(nx - gx, ny - gy) / km, liga = d <= T.r;
        if (liga) {
          ok++; ctx.strokeStyle = T.cor; ctx.globalAlpha = 0.5; ctx.beginPath(); ctx.moveTo(nx, ny); ctx.lineTo(gx, gy); ctx.stroke(); ctx.globalAlpha = 1;
          const f = (t * 0.7 + k * 0.17) % 1; ctx.fillStyle = '#fff'; ctx.beginPath(); ctx.arc(lerp(nx, gx, f), lerp(ny, gy, f), 3, 0, 7); ctx.fill();
        }
        ctx.fillStyle = liga ? '#11A360' : '#FF2B5F'; ctx.beginPath(); ctx.arc(nx, ny, 6, 0, 7); ctx.fill();
        ctx.fillStyle = '#fff'; ctx.textAlign = 'left'; ctx.fillText(nome + (liga ? '' : ' ✕'), nx + 9, ny + 4);
      });
      ctx.fillStyle = T.cor; ctx.beginPath(); ctx.moveTo(gx, gy - 14); ctx.lineTo(gx - 8, gy + 6); ctx.lineTo(gx + 8, gy + 6); ctx.fill();
      ctx.fillStyle = '#fff'; ctx.strokeStyle = '#fff'; ctx.beginPath(); ctx.moveTo(ox + 12, oy + L - 14); ctx.lineTo(ox + 12 + km, oy + L - 14); ctx.stroke();
      ctx.textAlign = 'left'; ctx.fillText('1 km', ox + 12, oy + L - 20);
      info.innerHTML = `<b>${tec}</b> · alcance ~${T.r < 1 ? fmt(T.r * 1000) + ' m' : fmt(T.r) + ' km'}${T.nota ? ' (' + T.nota + ')' : ''} · conectados: <b>${ok}/${nos.length}</b>`;
      info2.innerHTML = `taxa: ${T.taxa} · consumo: ${T.cons} · bateria: ${T.bat}`;
    });
    return { start: lp.start, stop: lp.stop };
  };

  /* =========================================================
     cobertura — vista de cima do voo em faixas: autonomia ×
     área coberta. opts.area (ha) da obra; opts.v, opts.t, opts.d
     (valores iniciais de velocidade, tempo útil e espaçamento).
     ========================================================= */
  R.cobertura = (host, opts, painel) => {
    const o = { area: 20, ...opts };
    const { ctx } = canvas2d(host);
    const p = painel || el('div');
    const sV = slider(p, { id: 'v', label: 'Velocidade de cruzeiro', min: 3, max: 15, step: 0.5, value: o.v ?? 8, unit: 'm/s' });
    const sT = slider(p, { id: 't', label: 'Tempo útil por bateria', min: 10, max: 40, step: 1, value: o.t ?? 20, unit: 'min' });
    const sE = slider(p, { id: 'e', label: 'Espaçamento entre faixas d', min: 20, max: 80, step: 1, value: o.d ?? 40, unit: 'm' });
    const res = el('div', { class: 'resultado' }); p.appendChild(res);
    // ao mexer num controle, o voo recomeça do início (a 2ª cor aparece logo)
    let t0 = 0, tAgora = 0;
    [sV, sT, sE].forEach((s) => s.addEventListener('input', () => { t0 = tAgora; }));
    const lp = loop((t) => {
      tAgora = t;
      const dpr = Math.min(2, window.devicePixelRatio || 1), W = ctx.canvas.width / dpr, H = ctx.canvas.height / dpr;
      const v = +sV.value, tm = +sT.value, e = +sE.value;
      const areaHa = (v * tm * 60 * e) / 10000, bat = Math.ceil(o.area / areaHa);
      res.innerHTML = `<span class="formula">A = v · t<sub>útil</sub> · d</span> = ${fmt(v, 1)} × ${fmt(tm * 60)} × ${fmt(e)} m²<br>` +
        `<span class="num">${fmt(areaHa, 1)} ha</span> por bateria → <b>${bat} bateria(s)</b> para ${fmt(o.area)} ha (t<sub>útil</sub> já desconta reserva, decolagem, pouso e curvas).`;
      ctx.clearRect(0, 0, W, H);
      const lado = Math.sqrt(o.area * 10000), esc = Math.min(W, H) * 0.82 / lado, ox = (W - lado * esc) / 2, oy = (H - lado * esc) / 2 + 8;
      ctx.fillStyle = 'rgba(194,120,47,.35)'; ctx.fillRect(ox, oy, lado * esc, lado * esc);
      ctx.strokeStyle = 'rgba(255,255,255,.5)'; ctx.strokeRect(ox, oy, lado * esc, lado * esc);
      const nf = Math.ceil(lado / e), compTotal = nf * lado, porBat = v * tm * 60;
      const cores = ['#2BD9FE', '#F2CB0A', '#95DE68', '#FF8A1F', '#FF2B5F', '#c58bff'];
      const prog = ((t - t0) * 0.2 % 1.15) * compTotal;
      let feito = 0;
      for (let k = 0; k < nf; k++) {
        const y = oy + (k + 0.5) * e * esc; if (y > oy + lado * esc) break;
        ctx.fillStyle = 'rgba(43,217,254,.07)'; ctx.fillRect(ox, y - e * esc / 2, lado * esc, e * esc);
        const ini = feito, fim = feito + lado; feito = fim;
        if (prog <= ini) continue;
        const parte = Math.min(lado, prog - ini);
        const ida = k % 2 === 0;
        for (let s = 0; s < parte; s += 4) {
          const d = ini + s, b = Math.floor(d / porBat);
          ctx.fillStyle = cores[b % cores.length];
          const x = ida ? ox + s * esc : ox + (lado - s) * esc; ctx.fillRect(x - 1, y - 1.5, 4 * esc + 1, 3);
        }
      }
      ctx.fillStyle = '#fff'; ctx.font = '600 13px Montserrat, Arial'; ctx.textAlign = 'center';
      ctx.fillText(`Área da obra: ${fmt(o.area)} ha · cada cor = uma bateria (um voo)`, W / 2, 20);
    });
    return { start: lp.start, stop: lp.stop };
  };

  /* =========================================================
     calc — calculadora declarativa, sem JS por aula.
     data-opts = {
       "inputs":  [{"id":"a","label":"Área","min":1,"max":100,"step":1,"value":20,"unit":"ha"}],
       "outputs": [{"label":"Custo","expr":"a*1500","unit":"R$","dec":0,"destaque":true}],
       "barras":  [{"label":"Convencional","expr":"a*1500"},{"label":"Drone","expr":"a*400"}],
       "nota": "texto opcional"
     }
     Expressões em JavaScript, usando os ids das entradas e as
     saídas anteriores (o1, o2...). Strings também são aceitas.
     ========================================================= */
  R.calc = (host, opts, painel) => {
    const o = { inputs: [], outputs: [], barras: [], ...opts };
    const p = painel || host;
    const inps = o.inputs.map((d) => [d.id, slider(p, d)]);
    const res = el('div', { class: 'resultado' }); p.appendChild(res);
    const temCanvas = o.barras.length && host !== p;
    const c2 = temCanvas ? canvas2d(host) : null;
    const compila = (expr, nomes) => new Function(...nomes, 'return (' + expr + ');');
    const nomesIn = o.inputs.map((d) => d.id);
    const fOut = o.outputs.map((s, k) => compila(s.expr, [...nomesIn, ...o.outputs.slice(0, k).map((_, j) => 'o' + (j + 1))]));
    const nomesTodos = [...nomesIn, ...o.outputs.map((_, j) => 'o' + (j + 1))];
    const fBar = o.barras.map((b) => compila(b.expr, nomesTodos));
    let anim = o.barras.map(() => 0);
    const calcula = () => {
      const vals = inps.map(([, i]) => +i.value), outs = [];
      fOut.forEach((f) => outs.push(f(...vals, ...outs)));
      res.innerHTML = o.outputs.map((s, k) => {
        const v = outs[k], txt = typeof v === 'number' ? (s.unit === 'R$' ? 'R$ ' + fmt(v, s.dec || 0) : fmt(v, s.dec || 0) + (s.unit ? ' ' + s.unit : '')) : v;
        return s.destaque ? `${s.label}: <span class="num">${txt}</span>` : `${s.label}: <b>${txt}</b>`;
      }).join('<br>') + (o.nota ? `<br><small>${o.nota}</small>` : '');
      return [...vals, ...outs];
    };
    const lp = loop((t, dt) => {
      const todos = calcula();
      if (!c2) return;
      const { ctx } = c2, dpr = Math.min(2, window.devicePixelRatio || 1), W = ctx.canvas.width / dpr, H = ctx.canvas.height / dpr;
      ctx.clearRect(0, 0, W, H);
      const vals = fBar.map((f) => Math.max(0, +f(...todos) || 0)), mx = Math.max(...vals, 1e-9);
      anim = anim.map((a, k) => a + (vals[k] - a) * Math.min(1, dt * 6));
      const n = vals.length, bw = Math.min(140, W / (n * 1.8)), base = H - 50, alt = H - 110;
      const cores = ['#FF8A1F', '#2BD9FE', '#F2CB0A', '#95DE68', '#FF2B5F'];
      anim.forEach((a, k) => {
        const x = W / 2 + (k - (n - 1) / 2) * bw * 1.6 - bw / 2, hh = (a / mx) * alt;
        ctx.fillStyle = cores[k % cores.length]; ctx.fillRect(x, base - hh, bw, hh);
        ctx.fillStyle = '#fff'; ctx.textAlign = 'center'; ctx.font = '600 13px Montserrat, Arial';
        ctx.fillText(o.barras[k].label, x + bw / 2, base + 20);
        const u = o.barras[k].unit || '';
        ctx.font = '700 15px Montserrat, Arial';
        ctx.fillText((u === 'R$' ? 'R$ ' : '') + fmt(a, o.barras[k].dec || 0) + (u && u !== 'R$' ? ' ' + u : ''), x + bw / 2, base - hh - 8);
      });
    });
    return { start: lp.start, stop: lp.stop };
  };

  /* ---------- números que sobem ---------- */
  function contadores(slide) {
    slide.querySelectorAll('.contador[data-ate]').forEach((c) => {
      const ate = +c.dataset.ate, dec = +(c.dataset.dec || 0), t0 = performance.now(), dur = 1400;
      const step = (now) => {
        const f = Math.min(1, (now - t0) / dur), e = 1 - Math.pow(1 - f, 3);
        c.textContent = (c.dataset.pre || '') + fmt(ate * e, dec) + (c.dataset.suf || '');
        if (f < 1) requestAnimationFrame(step);
      };
      requestAnimationFrame(step);
    });
  }

  /* ---------- ciclo de vida ligado a deck.js ---------- */
  const inst = new WeakMap();
  function painelDe(v) {
    const sel = v.dataset.painel;
    if (sel) return document.querySelector(sel);
    const g = v.closest('.viz-grid'); return g ? g.querySelector('.viz-lado [data-controles]') : null;
  }
  function entrar(slide) {
    contadores(slide);
    slide.querySelectorAll('.viz[data-viz]').forEach((v) => {
      let i = inst.get(v);
      if (!i) {
        const f = R[v.dataset.viz];
        if (!f) { v.textContent = 'Visualização desconhecida: ' + v.dataset.viz; return; }
        let opts = {}; try { opts = v.dataset.opts ? JSON.parse(v.dataset.opts) : {}; } catch (e) { console.warn('data-opts inválido', v, e); }
        i = Promise.resolve(f(v, opts, painelDe(v))); inst.set(v, i);
      }
      i.then((x) => { if (slide.classList.contains('active')) x.start(); });
    });
  }
  function sair(slide) { slide.querySelectorAll('.viz[data-viz]').forEach((v) => { const i = inst.get(v); if (i) i.then((x) => x.stop()); }); }
  document.querySelectorAll('#deck > .slide').forEach((s) => {
    s.addEventListener('slide:enter', () => entrar(s));
    s.addEventListener('slide:leave', () => sair(s));
    if (s.classList.contains('active')) entrar(s);
  });

  window.Obra = { register: (n, f) => { R[n] = f; }, loadThree, cena3d, canvas2d, loop, slider, botoes, hud, chip, fmt, droneModelo, caixa };
})();
