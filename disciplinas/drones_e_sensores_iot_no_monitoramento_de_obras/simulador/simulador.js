/* =====================================================================
   Simulador da Obra Torre A — Drones e Sensores IoT no Monitoramento de Obras
   Fonte única dos nomes, tópicos e números: APLICACAO.md (nesta pasta).

   Embutido nos slides (obra.js → data-viz="plataforma"), recebe por postMessage:
     { simAba, cenario, autostart, reiniciar, rodar, vel, regras:{...}, seg:{...}, rede:{gw, adr, g4, perda} }
   Na URL: ?embed=1  ?cenario=<id>  #<aba>
   ===================================================================== */
(() => {
  'use strict';
  const $ = (id) => document.getElementById(id);
  const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const fmt = (v, d = 1) => Number(v).toLocaleString('pt-BR', { minimumFractionDigits: d, maximumFractionDigits: d });
  const T0 = Date.UTC(2026, 10, 16, 10, 0, 0); // seg 16/11/2026 07:00 em Brasília (UTC−3)
  const DIA = 86400;
  const DIAS = ['dom', 'seg', 'ter', 'qua', 'qui', 'sex', 'sáb'];
  const local = (t) => new Date(T0 + t * 1000 - 3 * 3600 * 1000);
  const p2 = (n) => String(n).padStart(2, '0');
  const hora = (t) => { const d = local(t); return p2(d.getUTCHours()) + ':' + p2(d.getUTCMinutes()); };
  const dataHora = (t) => { const d = local(t); return DIAS[d.getUTCDay()] + ' ' + p2(d.getUTCDate()) + '/' + p2(d.getUTCMonth() + 1) + ' ' + hora(t); };
  const utc = (t) => new Date(T0 + t * 1000).toISOString().replace('.000', '');
  const horaLocalNum = (t) => { const d = local(t); return d.getUTCHours() + d.getUTCMinutes() / 60; };
  const diaSemana = (t) => local(t).getUTCDay();

  /* ------------------------- sensores da obra ------------------------- */
  // lim: [atenção, alerta, alarme]; taxa: [atenção, alerta] por dia; hist: histerese; salto: maior variação plausível entre leituras
  const SENSORES = [
    { id: 'I-1', nome: 'Inclinômetro I-1', tipo: 'inclinometro', setor: 'cortina', gr: 'desloc', un: 'mm', x: 268, y: 150, int: 900, dist: 60, perdas: 20, lim: [10, 14, 18], taxa: [0.5, 1.0], hist: 0.5, salto: 2, dec: 1, bruto: 'Σ sen θ', elem: 'Cortina de estacas — painel P02', guid: '1x7Kq$Rb93ZeN0vTq2LmA4' },
    { id: 'I-2', nome: 'Inclinômetro I-2', tipo: 'inclinometro', setor: 'cortina', gr: 'desloc', un: 'mm', x: 268, y: 330, int: 900, dist: 70, perdas: 25, lim: [10, 14, 18], taxa: [0.5, 1.0], hist: 0.5, salto: 2, dec: 1, bruto: 'Σ sen θ', elem: 'Cortina de estacas — painel P05 (junto ao prédio antigo)', guid: '0Fh3Wd8Lp1QsY6uRz9KcB2' },
    { id: 'PZ-01', nome: 'Piezômetro PZ-01', tipo: 'piezometro', setor: 'escavacao', gr: 'nivel', un: 'm', x: 340, y: 420, int: 900, dist: 80, perdas: 25, lim: [7, 8, 9], hist: 0.2, salto: 1.5, dec: 2, bruto: 'mA', elem: 'Poço de alívio PA-1 (1º subsolo)', guid: '3Tg8Hn2Vx5MeC7oPq0WsD1' },
    { id: 'PZ-02', nome: 'Piezômetro PZ-02', tipo: 'piezometro', setor: 'escavacao', gr: 'nivel', un: 'm', x: 480, y: 430, int: 900, dist: 70, perdas: 30, lim: [7, 8, 9], hist: 0.2, salto: 1.5, dec: 2, bruto: 'mA', elem: 'Poço de alívio PA-2 (2º subsolo)', guid: '2Rk5Js9Bv4NaF1yTe7GhE3' },
    { id: 'PZ-03', nome: 'Piezômetro PZ-03', tipo: 'piezometro', setor: 'escavacao', gr: 'nivel', un: 'm', x: 610, y: 320, int: 900, dist: 55, perdas: 35, lim: [7, 8, 9], hist: 0.2, salto: 1.5, dec: 2, bruto: 'mA', elem: 'Laje de fundo do 3º subsolo', guid: '1Mv2Pc6Dz8LuH4wXa5KrF0' },
    { id: 'E-01', nome: 'Extensômetro E-01 (escora)', tipo: 'extensometro', setor: 'escavacao', gr: 'carga', un: 'kN', x: 410, y: 210, int: 900, dist: 50, perdas: 15, lim: [780, 840, 960], hist: 20, salto: 150, dec: 0, bruto: 'µε aparente', elem: 'Escora metálica EM-03 (1º nível)', guid: '0Qs7Lf3Ky1RbJ8nVd2TwG6' },
    { id: 'T-01', nome: 'Temperatura T-01 (laje)', tipo: 'temperatura', setor: 'laje', gr: 'temp', un: '°C', x: 560, y: 160, int: 900, dist: 30, perdas: 5, lim: null, dec: 1, bruto: 'Ω (PT100)', elem: 'Laje L1 do térreo', guid: '2Yb4Gm1Xh7SdK3qWc9NpH5' },
    { id: 'UR-01', nome: 'Umidade UR-01', tipo: 'umidade', setor: 'laje', gr: 'ur', un: '%', x: 645, y: 225, int: 900, dist: 25, perdas: 5, lim: null, dec: 0, bruto: '% UR', elem: 'Laje L1 do térreo', guid: '2Yb4Gm1Xh7SdK3qWc9NpH5' },
    { id: 'PO-01', nome: 'Poeira PO-01 (divisa)', tipo: 'poeira', setor: 'divisa', gr: 'pm10', un: 'µg/m³', x: 600, y: 478, int: 300, dist: 60, perdas: 8, lim: [100, 150, 250], hist: 10, salto: 200, dec: 0, bruto: 'µg/m³ óptico', elem: 'Tapume da divisa com a rua', guid: '3Nc6Vt0Ar2PwL9eYb4MjJ7' },
    { id: 'AN-01', nome: 'Anemômetro AN-01 (grua)', tipo: 'anemometro', setor: 'grua', gr: 'vento', un: 'km/h', x: 772, y: 98, int: 120, dist: 2, perdas: 0, cabo: true, lim: [35, 42, 72], hist: 3, salto: 40, dec: 1, bruto: 'm/s', elem: 'Grua G1 — topo da torre', guid: '1Ld9Qa5Wn3TfB6sXk8HvK2' },
    { id: 'ACC-01', nome: 'Acelerômetro ACC-01 (vizinho)', tipo: 'acelerometro', setor: 'vizinho', gr: 'ppv', un: 'mm/s', x: 130, y: 240, int: 300, dist: 110, perdas: 18, lim: [3, 5, 10], hist: 0.3, salto: 8, dec: 2, bruto: 'g (pico)', elem: 'Prédio vizinho — pilar P12 (externo ao modelo)', guid: '—' }
  ];
  SENSORES.forEach((s) => { s.topic = `obra/torre-a/${s.setor}/${s.tipo}/${s.id}/${s.gr}`; });
  const SX = Object.fromEntries(SENSORES.map((s) => [s.id, s]));
  const GW = { x: 772, y: 56 };

  /* ------------------------- LoRaWAN (Aula 11) ------------------------- */
  const SENS = { 7: -123, 8: -126, 9: -129, 10: -132, 11: -134.5, 12: -137 };
  const TOA = { 7: 0.062, 8: 0.113, 9: 0.206, 10: 0.371, 11: 0.741, 12: 1.483 }; // 25 bytes, 125 kHz
  function enlace(s) {
    if (s.cabo) return { rede: 'cabo', rssi: null, sf: null, margem: Infinity, toa: 0, ok: true };
    const perdas = s.id === 'PZ-03' ? S.perdaPZ3 : s.perdas;
    const fspl = 20 * Math.log10(s.dist / 1000) + 20 * Math.log10(915) + 32.44;
    const rssi = 14 + 2 + 3 - fspl - perdas;
    let sf = 12;
    if (S.adr) { for (let k = 7; k <= 12; k++) if (rssi - SENS[k] >= 10) { sf = k; break; } }
    const margem = rssi - SENS[sf];
    return { rede: 'LoRaWAN', rssi, sf, margem, toa: TOA[sf], ok: margem >= 0, perdas };
  }
  function bateriaAnos(s, e) {
    if (s.cabo) return null;
    const porDia = (DIA / s.int) * (120 * e.toa + 5) + 0.01 * DIA; // transmissão + leitura do sensor + sono de 10 µA
    return (2600 * 3600) / porDia / 365;
  }

  /* ------------------------- aleatório reprodutível ------------------------- */
  let seed = 1;
  const rnd = () => { seed |= 0; seed = (seed + 0x6D2B79F5) | 0; let t = Math.imul(seed ^ (seed >>> 15), 1 | seed); t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296; };
  const gauss = (sd) => { let u = 0, v = 0; while (u === 0) u = rnd(); while (v === 0) v = rnd(); return sd * Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v); };

  /* ------------------------- regras e proteções ------------------------- */
  const REGRAS = [
    { id: 'velocidade', nome: 'Limite por velocidade', d: 'Inclinômetros: atenção a 0,5 mm/dia, alerta a 1,0 mm/dia (calculado sobre as últimas 24 h).' },
    { id: 'histerese', nome: 'Histerese', d: 'Entra no nível no limite, mas só sai abaixo do limite menos a histerese (0,5 mm nos inclinômetros). O ruído em torno do limite deixa de gerar notificações.' },
    { id: 'persistencia', nome: 'Persistência (2 leituras)', d: 'Só sobe de nível se duas leituras seguidas confirmarem.' },
    { id: 'termica', nome: 'Compensação térmica da escora', d: 'Desconta do extensômetro E-01 a deformação causada pelo sol (medida pela temperatura da peça).' },
    { id: 'umidade', nome: 'Correção da poeira pela umidade', d: 'O sensor óptico superestima com ar úmido. Acima de 80% de UR, divide a leitura pelo fator de umidade e marca a qualidade como suspeita.' },
    { id: 'mudo', nome: 'Alerta de sensor mudo', d: 'Sensor que não fala há três intervalos fica cinza e gera notificação. Sem esta regra, ele continua verde com a última leitura.' },
    { id: 'plausibilidade', nome: 'Plausibilidade (salto)', d: 'Leitura que salta mais do que o fisicamente possível entre duas medições é marcada como implausível e notificada: pode ser falha ou adulteração.' }
  ];
  const PROTECOES = [
    { id: 'senha', nome: 'Credencial única por dispositivo', d: 'A senha de fábrica do gateway (admin/admin) foi trocada no comissionamento por uma senha longa e única.' },
    { id: 'segmentada', nome: 'Rede segmentada e painel sem acesso pela internet', d: 'O painel web do gateway só abre pela VPN da obra; a rede IoT é separada da rede do escritório.' },
    { id: 'tls', nome: 'MQTT com TLS (porta 8883)', d: 'As mensagens entre o Node-RED, o gateway e o broker vão cifradas; quem escuta a rede não lê as senhas.' },
    { id: 'acl', nome: 'ACL por tópico no broker', d: 'Cada cliente só pode publicar nos próprios tópicos. O gateway não publica em nome de um sensor que não é dele.' },
    { id: 'firmware', nome: 'Firmware atualizado', d: 'Gateway e nós com a versão corrigida do fabricante.' },
    { id: 'mascara', nome: 'Máscara de privacidade nas câmeras (LGPD)', d: 'A câmera da grua desfoca rostos e cobre a janela e o quintal do vizinho; as imagens ficam 30 dias.' }
  ];

  /* ------------------------- cenários ------------------------- */
  const CENARIOS = [
    { id: 'recalque', titulo: 'O I-2 acelera ao lado do prédio antigo', vel: 3600, dur: 4 * DIA, aula: 'Aulas 9 e 13',
      desc: 'O inclinômetro I-2 está em 11,5 mm e sobe 1,2 mm por dia. Pela velocidade já é alerta; pelo valor, chega a 14 mm em cerca de dois dias.',
      passos: [[0, '📈', 'O I-2 começa o cenário em 11,5 mm (acima do nível de atenção, 10 mm).'], [12 * 3600, '⏱️', 'Com 12 h de série, a velocidade fica calculável: cerca de 1,2 mm/dia, acima do alerta por velocidade (1,0 mm/dia). Só notifica se a regra de velocidade estiver ligada.'], [2.1 * DIA, '🟧', 'O I-2 passa de 14 mm: agora é alerta também pelo valor. Pelo TARP, o reforço previsto já deveria estar em execução.'], [3.5 * DIA, '🔎', 'Compare: o alerta por velocidade chegou cerca de dois dias antes do alerta por valor. A série longa, com limites, mostra a tendência a tempo.']] },
    { id: 'escora', titulo: 'Escora no sol', vel: 900, dur: 2 * DIA, aula: 'Aula 9',
      desc: 'Num dia de sol forte, a escora metálica dilata: cerca de 180 µε a mais à tarde. Sem separar a parcela térmica, a variação do dia parece efeito da escavação.',
      passos: [[0, '☀️', 'Dia de sol forte. O extensômetro E-01 mede a deformação aparente da escora.'], [4 * 3600, '🟥', 'Entre 10 h e 16 h, com o sol mais forte, a carga aparente passa de 960 kN: alarme, se a compensação térmica estiver desligada.'], [12 * 3600, '🌙', 'À noite a peça esfria e a carga volta: o "alarme" era o sol.'], [DIA, '🔁', 'Ligue a compensação térmica na aba Alarmes e repita o cenário: a carga corrigida fica perto dos 600 kN.']] },
    { id: 'rajada', titulo: 'Rajada de quase 47 km/h na grua', vel: 60, dur: 2 * 3600, aula: 'Aula 15',
      desc: 'O vento sobe na grua até uma rajada de cerca de 13 m/s (46,8 km/h). A NR-18 pede alarme acima de 42 km/h; acima de 72 km/h, a operação é proibida.',
      passos: [[0, '🌬️', 'Vento moderado na grua, cerca de 20 km/h.'], [28 * 60, '🟨', 'O vento passa de 35 km/h: atenção.'], [36 * 60, '🟧', 'Passa de 42 km/h: alerta. Operação só com análise de risco e permissão de trabalho; o operador precisa ver o número na cabine.'], [40 * 60, '💨', 'Pico de cerca de 13 m/s (46,8 km/h). Ainda abaixo de 72 km/h, limite de proibição.'], [70 * 60, '✅', 'O vento cai. Com histerese, o alerta só normaliza abaixo de 39 km/h.']] },
    { id: 'internet', titulo: 'Três horas sem internet no canteiro', vel: 300, dur: 6 * 3600, aula: 'Aulas 10, 11 e 13',
      desc: 'A fibra do escritório de obra cai por 3 horas. O gateway fica sem saída para a internet. Com o 4G de reserva, nada acontece; sem ele, os nós guardam as leituras e reenviam depois.',
      passos: [[0, '🌐', 'Tudo normal: os pacotes saem do gateway pela fibra.'], [3600, '✂️', 'A fibra cai. Sem 4G de reserva, o broker publica o último desejo do gateway: obra/torre-a/status/GW-01 = offline.'], [3600 + 45 * 60, '🔇', 'Os sensores ficam mudos no painel. Com a regra de sensor mudo, ficam cinza e geram notificação; sem ela, continuam verdes com a última leitura.'], [4 * 3600, '🔁', 'A fibra volta. Os nós reenviam as leituras guardadas, com a hora da medição original: nada se perdeu.'], [5 * 3600, '🔎', 'Na aba Leituras, marque "só com problema": as linhas roxas são as reenviadas.']] },
    { id: 'poeira', titulo: 'Poeira na divisa num dia úmido', vel: 900, dur: DIA, aula: 'Aula 9',
      desc: 'A umidade do ar passa de 90%. O sensor óptico de poeira passa a contar gotículas como partículas e quase dobra a leitura.',
      passos: [[0, '🌫️', 'Madrugada úmida: UR acima de 90%.'], [1 * 3600, '🟧', 'A poeira bruta passa de 150 µg/m³: alerta falso, se a correção pela umidade estiver desligada.'], [8 * 3600, '☀️', 'Com o sol, a umidade cai e a leitura volta ao normal.'], [12 * 3600, '🔁', 'Ligue a correção pela umidade e repita: a leitura corrigida fica dentro do limite, marcada como "suspeita (UR alta)".']] },
    { id: 'fds', titulo: '37 alarmes num fim de semana', vel: 3600, dur: 2 * DIA + 12 * 3600, inicio: 4 * DIA + 17 * 3600, aula: 'Aula 13',
      desc: 'Sábado e domingo, sem ninguém na obra. O I-2 oscila logo abaixo de 10 mm e o PZ-01 logo abaixo de 7 m, com o ruído normal dos instrumentos. Cada cruzamento do limite, para cima ou para baixo, vira uma notificação.',
      passos: [[0, '📅', 'Sábado, 00:00. Ninguém na obra; as leituras seguem a cada 15 minutos.'], [DIA, '📱', 'Conte as notificações na aba Alarmes: sem histerese nem persistência, o celular do engenheiro não para — e nenhuma delas é um problema real.'], [2 * DIA, '😴', 'Na segunda, a equipe já não confia no painel. É assim que um alarme real se perde.'], [2 * DIA + 6 * 3600, '🔁', 'Ligue histerese e persistência na aba Alarmes e repita: as notificações caem para quase nenhuma, e o limite do projeto não mudou.']] },
    { id: 'admin', titulo: 'A senha do gateway era admin', vel: 300, dur: 4 * 3600, aula: 'Aula 16',
      desc: 'Um robô na internet varre endereços em busca de painéis com senha de fábrica. Se entrar, publica leituras falsas do I-2 para esconder o recalque que está acontecendo.',
      passos: [[0, '🤖', 'Um robô varre a internet procurando painéis web de gateways.'], [20 * 60, '🔑', 'Encontra o painel do GW-01 e tenta admin/admin.'], [35 * 60, '📡', 'Com a senha, lê a configuração do broker e conecta como o gateway.'], [50 * 60, '🎭', 'Publica leituras falsas no tópico do I-2 (cerca de 3 mm) logo depois de cada leitura real. O I-2 real sobe cerca de 0,65 mm por hora e passa do nível de atenção, mas o painel mostra o I-2 verde.'], [3 * 3600, '🔁', 'Na aba Segurança, ligue as proteções (ou só a regra de plausibilidade, na aba Alarmes) e repita o cenário.']] }
  ];
  const C = Object.fromEntries(CENARIOS.map((c) => [c.id, c]));

  /* ------------------------- drone e BIM (Aulas 8 e 14) ------------------------- */
  const VOOS = [
    { data: '26/10', gsd: 2.1, gcp: 6, rmse: 2.6, vol: 38100, av: 33.9 },
    { data: '02/11', gsd: 2.1, gcp: 6, rmse: 2.4, vol: 41800, av: 36.2 },
    { data: '09/11', gsd: 2.2, gcp: 6, rmse: 2.9, vol: 44600, av: 38.7 }
  ];
  const VOO_NOVO = { data: '16/11', gsd: 2.1, gcp: 6, rmse: 2.3, vol: 46900, av: 40.8 };
  const SERVICOS = [ // peso, previsto, executado (Aula 14)
    ['Fundações', 15, 100, 100, 'as-built'], ['Estrutura', 45, 55, 50, 'nuvem de pontos: 2.250 de 4.500 m³'], ['Alvenaria', 25, 15, 10, 'ortomosaico'], ['Instalações', 15, 10, 5, 'vistoria']
  ];

  /* ------------------------- estado ------------------------- */
  let S;
  const regrasPadrao = () => ({ velocidade: true, histerese: false, persistencia: false, termica: false, umidade: false, mudo: false, plausibilidade: false });
  const segPadrao = () => ({ senha: false, segmentada: false, tls: false, acl: false, firmware: false, mascara: false });
  function novoEstado(manter) {
    seed = 20261116;
    const velho = S;
    S = {
      t: 0, rodando: false, vel: velho ? velho.vel : 300,
      regras: manter && velho ? velho.regras : regrasPadrao(),
      seg: manter && velho ? velho.seg : segPadrao(),
      adr: manter && velho ? velho.adr : true, gw: true, g4: manter && velho ? velho.g4 : false, fibra: true,
      perdaPZ3: manter && velho ? velho.perdaPZ3 : 35,
      sen: {}, eventos: [], mqtt: [], retidos: {}, notifs: [], broker: [], pk: [],
      voou: false, cen: null, sel: velho ? velho.sel : 'I-2', nLeit: 0, nRe: 0, invasor: false
    };
    SENSORES.forEach((s) => {
      S.sen[s.id] = { prox: Math.round(rnd() * s.int), fila: [], hist: [], ult: null, niv: 'normal', nivTela: 'normal', cand: null, candN: 0, chegada: 0, mudo: false, taxa: null, bat: 3.55 + rnd() * 0.12 };
    });
    S.retidos['obra/torre-a/status/GW-01'] = 'online';
    log('Broker no ar (porta ' + (S.seg.tls ? '8883, TLS' : '1883, sem TLS') + '). GW-01 conectado.');
  }
  const log = (txt) => { S.broker.unshift({ t: S ? S.t : 0, txt }); S.broker.length = Math.min(S.broker.length, 80); };
  const saida = () => S.gw && (S.fibra || S.g4);
  const off = () => (S.cen ? S.t - S.cen.t0 : -1);
  const cenAtivo = (id) => S.cen && S.cen.id === id && off() >= 0;

  /* ------------------------- modelo físico ------------------------- */
  function sol(t) { const h = horaLocalNum(t); return Math.max(0, Math.sin(Math.PI * (h - 7) / 12)); }
  function trabalho(t) { const h = horaLocalNum(t), d = diaSemana(t); return d >= 1 && d <= 5 && h >= 7 && h < 17 ? 1 : d === 6 && h >= 7 && h < 12 ? 0.6 : 0; }
  function ur(t) { const o = off(); if (cenAtivo('poeira') && o < 10 * 3600) return 93 - 4 * sol(t); return 62 - 15 * sol(t); }
  function medir(s, t) {
    const o = off(), dias = o / DIA;
    let v, bruto, q = 'ok', extra = {};
    switch (s.id) {
      case 'I-1': v = 4.2 + gauss(0.12); break;
      case 'I-2':
        if (cenAtivo('recalque')) v = 11.5 + 1.2 * dias + gauss(0.12);
        else if (cenAtivo('fds')) v = 9.7 + gauss(0.19);
        else if (cenAtivo('admin')) v = 9.4 + 0.65 * (off() / 3600) + gauss(0.1);
        else v = 8.6 + gauss(0.15);
        break;
      case 'PZ-01': v = cenAtivo('fds') ? 6.85 + gauss(0.075) : 4.3 + gauss(0.05); break;
      case 'PZ-02': v = (cenAtivo('recalque') ? 5.2 + 0.25 * dias : 5.2) + gauss(0.05); break;
      case 'PZ-03': v = 5.9 + gauss(0.05); break;
      case 'E-01': {
        const amp = cenAtivo('escora') ? 180 : 25;
        const term = amp * sol(t);
        const ue = 250 + term + gauss(3);
        bruto = ue;
        v = 2.4 * (S.regras.termica ? ue - term : ue);
        if (S.regras.termica) extra.nota = 'compensada (−' + fmt(term, 0) + ' µε)';
        break;
      }
      case 'T-01': v = 22 + 8 * sol(t) + gauss(0.2); break;
      case 'UR-01': v = ur(t) + gauss(1); break;
      case 'PO-01': {
        const real = 45 + 30 * trabalho(t) + gauss(6);
        const u = ur(t), fator = u > 80 ? 1 + (u - 80) / 10 : 1;
        bruto = Math.max(5, real * fator);
        v = S.regras.umidade ? bruto / fator : bruto;
        if (u > 85) q = 'suspeita (UR alta)';
        break;
      }
      case 'AN-01': {
        let ms = 4 + 1.5 * sol(t) + gauss(0.5);
        if (cenAtivo('rajada')) ms = 5.5 + 7.5 * Math.exp(-Math.pow((o - 2400) / 600, 2)) + gauss(0.25);
        ms = Math.max(0, ms); bruto = ms; v = ms * 3.6; break;
      }
      case 'ACC-01': v = Math.max(0.05, 0.6 + 0.8 * trabalho(t) + gauss(0.15)); break;
    }
    if (bruto == null) {
      if (s.tipo === 'inclinometro') bruto = v / 500;
      else if (s.tipo === 'piezometro') bruto = 4 + 16 * v / 20;
      else if (s.tipo === 'temperatura') bruto = 100 * (1 + 0.00385 * v);
      else if (s.tipo === 'acelerometro') bruto = v / 1000 * 2 * Math.PI * 12 / 9.81 * 10;
      else bruto = v;
    }
    return { v, bruto, q, extra };
  }
  const brutoTxt = (s, b) => s.tipo === 'inclinometro' ? fmt(b, 4) : s.tipo === 'piezometro' ? fmt(b, 2) + ' mA' : s.tipo === 'temperatura' ? fmt(b, 2) + ' Ω' : s.tipo === 'extensometro' ? fmt(b, 0) + ' µε' : s.tipo === 'anemometro' ? fmt(b, 1) + ' m/s' : s.tipo === 'acelerometro' ? fmt(b, 4) + ' g' : s.tipo === 'poeira' ? fmt(b, 0) : fmt(b, 0) + ' %';

  /* ------------------------- alarmes ------------------------- */
  const NIVEIS = ['normal', 'atencao', 'alerta', 'alarme'];
  const ROT = { normal: 'normal', atencao: 'atenção', alerta: 'alerta', alarme: 'alarme', mudo: 'sem dados' };
  const TARP = {
    normal: ['Leitura dentro do previsto', 'Rotina: leitura a cada 15 min, relatório semanal.', 'Técnico de instrumentação', '—'],
    atencao: ['10 mm ou 0,5 mm/dia', 'Aumentar a frequência, inspecionar, avisar o projetista.', 'Engenheiro da obra', '24 h'],
    alerta: ['14 mm ou 1,0 mm/dia', 'Preparar e iniciar o reforço previsto, restringir a frente.', 'Engenheiro + projetista', '12 h'],
    alarme: ['18 mm', 'Paralisar a escavação na frente, executar a contingência, isolar a área.', 'Responsável técnico + Defesa Civil se preciso', 'imediato']
  };
  const acaoDe = (s, n) => {
    if (n === 'mudo') return 'Verificar nó, bateria e rede; leitura manual se for sensor crítico.';
    if (s.tipo === 'inclinometro') return TARP[n][1];
    if (s.tipo === 'anemometro') return n === 'alarme' ? 'Operação da grua proibida (NR-18).' : n === 'alerta' ? 'Só com análise de risco e permissão de trabalho; avisar o operador.' : n === 'atencao' ? 'Avisar o operador e o encarregado.' : '—';
    if (s.tipo === 'piezometro') return n === 'normal' ? '—' : 'Verificar o rebaixamento e os poços de alívio; avisar o projetista.';
    if (s.tipo === 'poeira') return n === 'normal' ? '—' : 'Umedecer vias, lavar rodas, rever a atividade na divisa.';
    if (s.tipo === 'extensometro') return n === 'normal' ? '—' : 'Inspecionar a escora e o encunhamento; avisar o projetista.';
    if (s.tipo === 'acelerometro') return n === 'normal' ? '—' : 'Reduzir a energia da atividade (cravação, compactação) e vistoriar o vizinho.';
    return '—';
  };
  function nivelValor(s, v) { if (!s.lim) return 0; let k = 0; s.lim.forEach((l, i) => { if (v >= l) k = i + 1; }); return k; }
  function taxaDia(st, t) {
    const h = st.hist; if (h.length < 3) return null;
    const alvo = t - DIA; let a = null;
    for (let i = h.length - 1; i >= 0; i--) { if (h[i].t <= alvo) { a = h[i]; break; } }
    if (!a) { a = h[0]; if (t - a.t < 12 * 3600) return null; }
    // média de 4 leituras em cada ponta, para o ruído não virar velocidade
    const ult = h.slice(-4), ia = h.indexOf(a), ini = h.slice(ia, ia + 4);
    const m = (arr) => arr.reduce((x, p) => x + p.v, 0) / arr.length;
    const mt = (arr) => arr.reduce((x, p) => x + p.t, 0) / arr.length;
    return (m(ult) - m(ini)) / ((mt(ult) - mt(ini)) / DIA);
  }
  function notificar(s, n, motivo) {
    S.notifs.unshift({ t: S.t, id: s.id, niv: n, motivo, acao: acaoDe(s, n) });
    if (S.notifs.length > 300) S.notifs.length = 300;
  }
  function avaliar(s, st, v, tm, falsa) {
    let alvo = nivelValor(s, v), motivo = alvo ? 'valor ' + fmt(v, s.dec) + ' ' + s.un : '';
    if (s.taxa && S.regras.velocidade) {
      const tx = taxaDia(st, tm); st.taxa = tx;
      if (tx != null) { let k = 0; s.taxa.forEach((l, i) => { if (tx >= l) k = i + 1; }); if (k > alvo) { alvo = k; motivo = 'velocidade ' + fmt(tx, 2) + ' mm/dia'; } }
    }
    const atual = NIVEIS.indexOf(st.niv);
    if (S.regras.plausibilidade && st.ult && !falsa && Math.abs(v - st.ult.v) > s.salto && S.t - (st.plaus || -1e9) > 3600) { st.plaus = S.t; notificar(s, 'alerta', 'leitura implausível: salto de ' + fmt(Math.abs(v - st.ult.v), s.dec) + ' ' + s.un + ' — verificar sensor e integridade'); }
    let novo = alvo;
    if (alvo < atual && S.regras.histerese && s.lim) {
      // só desce se ficar abaixo do limite do nível atual menos a histerese
      const limAtual = s.lim[atual - 1];
      if (v >= limAtual - s.hist) novo = atual;
      else novo = Math.max(alvo, 0);
      if (motivo.startsWith('velocidade')) novo = Math.max(novo, alvo);
    }
    if (novo > atual && S.regras.persistencia) {
      if (st.cand === novo) st.candN++; else { st.cand = novo; st.candN = 1; }
      if (st.candN < 2) novo = atual;
    } else { st.cand = null; st.candN = 0; }
    if (novo !== atual) {
      st.niv = NIVEIS[novo];
      notificar(s, st.niv, novo > atual ? (motivo || 'limite') : 'normalizou (' + fmt(v, s.dec) + ' ' + s.un + ')');
    }
    return st.niv;
  }

  /* ------------------------- entrega das leituras ------------------------- */
  function entregar(s, r, re) {
    const st = S.sen[s.id];
    st.hist.push({ t: r.tm, v: r.v, re, fake: r.fake });
    if (re || r.fake) st.hist.sort((a, b) => a.t - b.t);
    if (st.hist.length > 3000) st.hist.shift();
    r.niv = avaliar(s, st, r.v, r.tm, r.fake);
    st.ult = r; st.chegada = S.t;
    if (st.mudo) { st.mudo = false; if (S.regras.mudo) notificar(s, st.niv, 'voltou a falar'); }
    const ev = { ...r, ta: S.t, id: s.id, re };
    S.eventos.unshift(ev); if (S.eventos.length > 400) S.eventos.length = 400;
    S.nLeit++; if (re) S.nRe++;
    const payload = JSON.stringify({ ts: utc(r.tm), bruto: +r.bruto.toFixed(4), valor: +r.v.toFixed(s.dec + 1), un: s.un, q: r.q, bat: +r.bat.toFixed(2) });
    S.mqtt.unshift({ t: S.t, topic: s.topic, qos: 1, payload, fake: r.fake, re });
    if (S.mqtt.length > 500) S.mqtt.length = 500;
    S.retidos[s.topic] = payload;
    if (S.pk.length < 60) S.pk.push({ id: s.id, p: 0, cls: r.fake ? 'bad' : re ? 're' : '' });
  }
  function gerar(s, tm) {
    const st = S.sen[s.id];
    const m = medir(s, tm);
    st.bat = Math.max(3.2, st.bat - 0.0000004 * s.int);
    const e = enlace(s);
    const r = { tm, v: m.v, bruto: m.bruto, q: m.q, nota: m.extra.nota, bat: st.bat, rssi: e.rssi, sf: e.sf, fake: false };
    if (!e.ok || !saida()) { st.fila.push(r); return; }
    if (st.fila.length) { st.fila.forEach((x) => entregar(s, x, true)); st.fila = []; }
    entregar(s, r, false);
  }
  function descarregarFilas() {
    SENSORES.forEach((s) => { const st = S.sen[s.id]; if (st.fila.length && enlace(s).ok && saida()) { st.fila.forEach((x) => entregar(s, x, true)); st.fila = []; } });
  }

  /* ------------------------- relógio ------------------------- */
  let estavaSaida = true;
  function passo(dt) {
    const fim = S.t + dt;
    // cenário: eventos de rede e de ataque
    while (S.t < fim) {
      const prox = Math.min(fim, ...SENSORES.map((s) => S.t + Math.max(1, S.sen[s.id].prox - S.t)));
      S.t = prox;
      cenarioTick();
      SENSORES.forEach((s) => { const st = S.sen[s.id]; while (st.prox <= S.t) { gerar(s, st.prox); st.prox += s.int; } });
      if (saida() !== estavaSaida) {
        estavaSaida = saida();
        if (!estavaSaida) { S.retidos['obra/torre-a/status/GW-01'] = 'offline'; S.mqtt.unshift({ t: S.t, topic: 'obra/torre-a/status/GW-01', qos: 1, payload: 'offline (último desejo, retido)' }); log('GW-01 sem keepalive: broker publica o último desejo (offline).'); }
        else { S.retidos['obra/torre-a/status/GW-01'] = 'online'; S.mqtt.unshift({ t: S.t, topic: 'obra/torre-a/status/GW-01', qos: 1, payload: 'online (retido)' }); log('GW-01 reconectado.'); descarregarFilas(); }
      }
      // sensor mudo: sem leitura há 3 intervalos
      SENSORES.forEach((s) => {
        const st = S.sen[s.id];
        if (!st.mudo && st.ult && S.t - st.chegada > 3 * s.int) { st.mudo = true; if (S.regras.mudo) notificar(s, 'mudo', 'sem leitura há ' + Math.round((S.t - st.chegada) / 60) + ' min'); }
      });
    }
  }
  function cenarioTick() {
    if (!S.cen) return;
    const o = off(), c = S.cen.c;
    S.cen.passos.forEach((p, i) => { if (!p.feito && o >= c.passos[i][0]) p.feito = true; });
    if (c.id === 'internet') { const f = !(o >= 3600 && o < 4 * 3600); if (f !== S.fibra) { S.fibra = f; log(f ? 'Fibra do escritório restabelecida.' : 'Fibra do escritório caiu.' + (S.g4 ? ' Gateway saiu pelo 4G de reserva.' : '')); } }
    if (c.id === 'admin') ataque(o);
    if (o > c.dur && !S.cen.fim) { S.cen.fim = true; S.rodando = false; btnRodar(); }
  }
  function ataque(o) {
    const A = S.cen.atk || (S.cen.atk = {});
    if (o >= 20 * 60 && !A.varre) { A.varre = true; if (S.seg.segmentada) { log('Varredura externa: painel do GW-01 não responde na internet (só pela VPN).'); A.fim = 'bloq-rede'; } else log('Varredura externa encontrou o painel web do GW-01 (porta 80).'); }
    if (A.fim) return;
    if (o >= 25 * 60 && !A.login) { A.login = true; if (S.seg.senha) { log('5 tentativas com senhas de fábrica no GW-01: todas recusadas.'); A.fim = 'bloq-senha'; } else { log('Login admin/admin no painel do GW-01: SUCESSO.'); S.invasor = true; } }
    if (A.fim) return;
    if (o >= 35 * 60 && !A.broker) { A.broker = true; log(S.seg.tls ? 'Invasor copia a credencial do broker da configuração do gateway e conecta pela porta 8883.' : 'Invasor copia a credencial do broker e conecta pela porta 1883, sem TLS.'); }
    if (o >= 50 * 60) {
      const st = S.sen['I-2'];
      if (st.ult && !st.ult.fake && st.ult.tm > (A.ultFalsa || 0)) {
        A.ultFalsa = st.ult.tm;
        if (S.seg.acl) { if (!A.aclLog) { A.aclLog = true; log('Publicação em obra/torre-a/cortina/inclinometro/I-2/desloc NEGADA pela ACL: o cliente GW-01 não pode publicar como sensor.'); } A.negadas = (A.negadas || 0) + 1; return; }
        const s = SX['I-2'], v = 3 + gauss(0.1);
        entregar(s, { tm: st.ult.tm + 30, v, bruto: v / 500, q: 'ok', bat: st.bat, rssi: st.ult.rssi, sf: st.ult.sf, fake: true }, false);
        if (S.regras.plausibilidade && S.t - (st.plaus || -1e9) > 3600) { st.plaus = S.t; notificar(s, 'alerta', 'leitura implausível: salto de ' + fmt(Math.abs(st.hist[st.hist.length - 2].v - v), 1) + ' mm — verificar sensor e integridade'); }
      }
    }
  }

  /* ------------------------- cenários: controle ------------------------- */
  function iniciarCenario(id) {
    const c = C[id]; if (!c) return;
    novoEstado(true);
    if (c.inicio) { S.t = c.inicio; SENSORES.forEach((s) => { S.sen[s.id].prox = S.t + Math.round(rnd() * s.int); }); }
    S.cen = { id, c, t0: S.t, passos: c.passos.map(() => ({ feito: false })) };
    S.vel = c.vel; $('velocidade').value = String(c.vel);
    estavaSaida = true;
    log('Cenário iniciado: ' + c.titulo + '.');
    rodar(true); mostrar(aba);
  }
  const repetirCenario = () => { if (S.cen) iniciarCenario(S.cen.id); };
  function rodar(on) { S.rodando = on; btnRodar(); }
  function btnRodar() { const b = $('btn-rodar'); b.textContent = S.rodando ? 'Pausar' : 'Iniciar'; b.classList.toggle('go', !S.rodando); }

  /* ------------------------- desenho: canteiro ------------------------- */
  const corNiv = (n) => ({ normal: 'var(--green)', atencao: 'var(--amber)', alerta: 'var(--orange)', alarme: 'var(--red)', mudo: '#6B7A94' }[n]);
  const nivTela = (st) => (st.mudo && S.regras.mudo ? 'mudo' : st.ult ? st.niv : 'mudo');
  function montarPlanta() {
    let s = '';
    s += '<rect class="rua" x="0" y="500" width="1000" height="60"/><text class="rot" x="20" y="535">RUA DAS PAINEIRAS</text>';
    s += '<rect class="viz" x="30" y="70" width="175" height="380" rx="4"/><text class="rot2" x="48" y="98">Prédio vizinho</text><text class="rot" x="48" y="116">1968 · fundação rasa</text>';
    s += '<rect class="lote" x="225" y="40" width="750" height="455" rx="6"/><text class="rot" x="830" y="485">LOTE DA TORRE A</text>';
    s += '<rect class="esc" x="255" y="80" width="430" height="390" rx="4"/><text class="rot" x="285" y="458">ESCAVAÇÃO · 3 SUBSOLOS (−10,5 m)</text>';
    s += '<line class="cortina" x1="255" y1="80" x2="255" y2="470"/><text class="rot" x="262" y="74">CORTINA</text>';
    s += '<rect x="470" y="120" width="200" height="130" fill="rgba(185,188,194,.18)" stroke="#8C93A1" stroke-dasharray="5 4"/><text class="rot" x="480" y="140">LAJE L1 · TÉRREO</text>';
    s += '<line x1="300" y1="210" x2="680" y2="210" stroke="#8C93A1" stroke-width="5"/><text class="rot" x="300" y="200">ESCORA EM-03</text>';
    s += '<rect x="800" y="380" width="140" height="60" rx="4" fill="#1B2741" stroke="#5B6E92"/><text class="rot2" x="812" y="405">Escritório de obra</text><text class="rot" x="812" y="424">fibra + roteador 4G</text>';
    s += '<line class="grua" x1="772" y1="80" x2="772" y2="300"/><line class="grua" x1="560" y1="80" x2="960" y2="80"/><text class="rot" x="790" y="300">GRUA G1</text>';
    s += '<g id="lnks"></g>';
    s += `<g class="gw" id="gw"><rect x="${GW.x - 36}" y="${GW.y - 14}" width="72" height="24" rx="5"/><text x="${GW.x}" y="${GW.y + 3}" text-anchor="middle">GW-01</text></g>`;
    SENSORES.forEach((x) => { s += `<g class="sen" data-id="${x.id}" tabindex="0" role="button" aria-label="${esc(x.nome)}"><circle cx="${x.x}" cy="${x.y}" r="11"/><text x="${x.x + 15}" y="${x.y + 4}">${x.id}</text></g>`; });
    s += '<g id="pks"></g><g id="dronegrp"></g>';
    $('planta').innerHTML = s;
    $('lnks').innerHTML = SENSORES.map((x) => `<line class="lnk" x1="${x.x}" y1="${x.y}" x2="${GW.x}" y2="${GW.y}"/>`).join('');
    $('planta').querySelectorAll('.sen').forEach((g) => { const f = () => { S.sel = g.dataset.id; rCanteiro(); }; g.addEventListener('click', f); g.addEventListener('keydown', (e) => { if (e.key === 'Enter') f(); }); });
  }
  function rCanteiro() {
    SENSORES.forEach((x) => {
      const g = $('planta').querySelector(`.sen[data-id="${x.id}"]`), st = S.sen[x.id];
      g.querySelector('circle').setAttribute('fill', corNiv(nivTela(st)));
      g.classList.toggle('sel', S.sel === x.id);
    });
    $('gw').classList.toggle('off', !saida());
    const s = SX[S.sel], st = S.sen[s.id], e = enlace(s), u = st.ult;
    $('det-sub').textContent = s.nome;
    $('det').innerHTML = `<div class="det"><dl>
      <dt>Nível</dt><dd><span class="niv ${nivTela(st)}">${ROT[nivTela(st)]}</span>${st.mudo && !S.regras.mudo ? ' <small class="n-mudo">(mudo, mas a regra está desligada)</small>' : ''}</dd>
      <dt>Última leitura</dt><dd>${u ? '<b>' + fmt(u.v, s.dec) + ' ' + s.un + '</b> · ' + dataHora(u.tm) + (u.fake ? ' <span class="tag bad">falsa</span>' : '') : '—'}</dd>
      <dt>Bruto</dt><dd>${u ? brutoTxt(s, u.bruto) : '—'} <small>(${esc(s.bruto)})</small></dd>
      ${s.taxa ? `<dt>Velocidade</dt><dd>${st.taxa == null ? 'série curta' : fmt(st.taxa, 2) + ' mm/dia'}</dd>` : ''}
      <dt>Limites</dt><dd>${s.lim ? s.lim.map((l) => fmt(l, s.dec >= 1 ? 1 : 0)).join(' · ') + ' ' + s.un : 'sem limite (sensor de apoio)'}</dd>
      <dt>Tópico MQTT</dt><dd><code>${s.topic}</code></dd>
      <dt>Rede</dt><dd>${e.rede}${e.sf ? ' · SF' + e.sf + ' · margem ' + fmt(e.margem, 1) + ' dB' : ' (cabo até o gateway)'}</dd>
      <dt>Intervalo</dt><dd>${s.int >= 900 ? s.int / 60 + ' min' : s.int / 60 + ' min'}</dd>
      <dt>Fila no nó</dt><dd>${st.fila.length} leitura(s)</dd>
      <dt>Elemento BIM</dt><dd>${esc(s.elem)}</dd>
      <dt>Ação (TARP)</dt><dd>${esc(acaoDe(s, nivTela(st)))}</dd></dl></div>`;
    const elos = [['Sensor', s.id, true], ['Nó', s.cabo ? 'datalogger da grua' : 'ESP32 + rádio LoRa', true], ['Rádio', s.cabo ? 'cabo' : 'LoRaWAN 915 MHz', e.ok], ['Gateway', 'GW-01 (grua)', S.gw], ['Internet', S.fibra ? 'fibra' : S.g4 ? '4G de reserva' : 'sem saída', saida()], ['Servidor de rede', 'deduplica, ADR', true], ['Broker MQTT', S.seg.tls ? 'porta 8883 · TLS' : 'porta 1883', true], ['Node-RED', 'valida e converte', true], ['InfluxDB', 'série temporal', true], ['Grafana', 'painel e alertas', true]];
    $('cadeia').innerHTML = elos.map((x, i) => `${i ? '<span class="seta">→</span>' : ''}<div class="elo${x[2] ? '' : ' off'}"><b>${x[0]}</b><small>${x[1]}</small></div>`).join('');
  }
  function animar(dt) {
    const g = $('pks'); if (!g || aba !== 'canteiro') { S.pk.length = 0; return; }
    S.pk.forEach((p) => (p.p += dt * 1.6));
    S.pk = S.pk.filter((p) => p.p < 1);
    g.innerHTML = S.pk.map((p) => { const s = SX[p.id]; const x = s.x + (GW.x - s.x) * p.p, y = s.y + (GW.y - s.y) * p.p; return `<circle class="pk ${p.cls}" cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="4.5"/>`; }).join('');
    const d = $('dronegrp');
    if (S.vooAnim != null) {
      S.vooAnim += dt * 0.25; const k = S.vooAnim; const faixa = Math.floor(k * 8), fr = (k * 8) % 1;
      const x = 270 + (faixa % 2 ? 1 - fr : fr) * 680, y = 60 + faixa * 55;
      d.innerHTML = k < 1 ? `<circle class="drone" cx="${x}" cy="${y}" r="9"/><text class="rot2" x="${x + 12}" y="${y - 8}">drone</text>` : '';
      if (k >= 1) { S.vooAnim = null; S.voou = true; render(); }
    }
  }

  /* ------------------------- desenho: abas ------------------------- */
  const kpi = (l, v, c = '') => `<div class="kpi ${c}"><small>${l}</small><b>${v}</b></div>`;
  function rLeituras() {
    const fila = SENSORES.reduce((a, s) => a + S.sen[s.id].fila.length, 0);
    const mudos = SENSORES.filter((s) => S.sen[s.id].mudo).length;
    $('kpis-leit').innerHTML = kpi('Leituras recebidas', S.nLeit.toLocaleString('pt-BR'), 'blue') + kpi('Reenviadas (guardadas no nó)', S.nRe, S.nRe ? 'amber' : '') + kpi('Na fila dos nós', fila, fila ? 'red' : '') + kpi('Sensores mudos', mudos, mudos ? 'red' : 'green') + kpi('Pontos por dia (11 sensores)', pontosDia().toLocaleString('pt-BR'));
    const fs = $('f-sensor').value, fp = $('f-problema').checked;
    const lin = S.eventos.filter((e) => (!fs || e.id === fs) && (!fp || e.re || e.fake || e.niv !== 'normal' || e.q !== 'ok')).slice(0, 150);
    $('leit-sub').textContent = lin.length ? 'mais recente no topo' : 'aguardando — clique em Iniciar';
    $('tb-leit').innerHTML = lin.map((e) => { const s = SX[e.id]; const cls = e.fake ? 'bad' : e.re ? 're' : e.niv !== 'normal' ? 'warn' : '';
      return `<tr class="${cls}"><td class="mono">${utc(e.tm).slice(5, 16).replace('T', ' ')}Z</td><td>${e.id}</td><td class="mono">${brutoTxt(s, e.bruto)}</td><td class="mono"><b>${fmt(e.v, s.dec)}</b> ${s.un}${e.nota ? ' <small>' + e.nota + '</small>' : ''}</td><td><span class="niv ${e.niv}">${ROT[e.niv]}</span></td><td>${e.fake ? '<span class="tag bad">não veio do sensor</span>' : e.q === 'ok' ? '<span class="tag ok">ok</span>' : '<span class="tag warn">' + e.q + '</span>'}</td><td class="mono">${fmt(e.bat, 2)} V</td><td class="mono">${e.sf ? 'SF' + e.sf + ' · ' + fmt(e.rssi, 0) + ' dBm' : 'cabo'}${e.re ? ' <span class="tag purple">reenviada</span>' : ''}</td></tr>`; }).join('');
  }
  const pontosDia = () => SENSORES.reduce((a, s) => a + DIA / s.int, 0);
  function rRede() {
    const L = SENSORES.map((s) => [s, enlace(s)]);
    const pior = L.filter(([s]) => !s.cabo).sort((a, b) => a[1].margem - b[1].margem)[0];
    const fila = SENSORES.reduce((a, s) => a + S.sen[s.id].fila.length, 0);
    $('kpis-rede').innerHTML = kpi('Gateway GW-01', S.gw ? 'ligado' : 'desligado', S.gw ? 'green' : 'red') + kpi('Saída para a internet', S.fibra ? 'fibra' : S.g4 ? '4G de reserva' : 'nenhuma', saida() ? 'green' : 'red') + kpi('Pior margem', pior[0].id + ' · ' + fmt(pior[1].margem, 1) + ' dB', pior[1].margem >= 10 ? 'green' : pior[1].margem >= 0 ? 'amber' : 'red') + kpi('Leituras na fila', fila, fila ? 'red' : '');
    $('tb-rede').innerHTML = L.map(([s, e]) => { const anos = bateriaAnos(s, e); const st = S.sen[s.id]; const cls = !e.ok ? 'bad' : e.margem < 10 ? 'warn' : '';
      return `<tr class="${cls}"><td>${s.id}</td><td>${e.rede}</td><td class="mono">${s.cabo ? '—' : s.dist + ' m'}</td><td class="mono">${s.cabo ? '—' : (e.perdas) + ' dB'}</td><td class="mono">${e.rssi == null ? '—' : fmt(e.rssi, 1) + ' dBm'}</td><td class="mono">${e.sf ? 'SF' + e.sf : '—'}</td><td class="mono">${e.sf ? fmt(e.margem, 1) + ' dB' : '—'}</td><td class="mono">${e.sf ? fmt(e.toa * 1000, 0) + ' ms' : '—'}</td><td class="mono">${anos == null ? 'rede elétrica' : fmt(anos, 1) + ' anos'}</td><td class="mono">${st.fila.length}</td></tr>`; }).join('');
    const e3 = enlace(SX['PZ-03']);
    $('o-perda').textContent = S.perdaPZ3;
    $('rede-nota').innerHTML = !e3.ok ? `<b>PZ-03 fora do ar:</b> recebe ${fmt(e3.rssi, 1)} dBm, abaixo da sensibilidade até do SF12 (−137 dBm). O nó guarda as leituras; solução: gateway mais perto, antena fora da caixa ou NB-IoT.` : e3.margem < 10 ? `<b>PZ-03 no limite:</b> margem de ${fmt(e3.margem, 1)} dB em SF${e3.sf}. Fecha, mas sem folga para chuva ou máquina na frente.` : `PZ-03 em SF${e3.sf} com margem de ${fmt(e3.margem, 1)} dB. ${S.adr ? 'O ADR escolheu o menor SF com 10 dB de folga.' : 'Sem ADR, todos transmitem em SF12: cerca de 24 vezes mais energia por mensagem que o SF7.'}`;
  }
  function casa(filtro, topico) {
    const f = filtro.split('/'), t = topico.split('/');
    for (let i = 0; i < f.length; i++) { if (f[i] === '#') return true; if (i >= t.length) return false; if (f[i] !== '+' && f[i] !== t[i]) return false; }
    return f.length === t.length;
  }
  const filtroValido = (f) => { const p = f.split('/'); return f.length > 0 && p.every((x, i) => (x === '#' ? i === p.length - 1 : x === '+' || !/[#+]/.test(x))); };
  function rMqtt() {
    const f = $('m-filtro').value.trim(), ok = filtroValido(f);
    $('m-valida').innerHTML = ok ? 'Assinatura válida. O broker entrega as mensagens dos tópicos que casam com ela.' : '<span class="n-alarme">Assinatura inválida: o # só pode ser o último nível (e o + ocupa um nível inteiro). O broker recusa.</span>';
    const lin = ok ? S.mqtt.filter((m) => casa(f, m.topic)) : [];
    $('m-cont').textContent = lin.length + ' mensagem(ns)';
    $('tb-mqtt').innerHTML = lin.slice(0, 120).map((m) => `<tr class="${m.fake ? 'bad' : m.re ? 're' : ''}"><td class="mono">${hora(m.t)}</td><td class="mono">${m.topic}</td><td>${m.qos}</td><td class="mono">${esc(m.payload)}</td></tr>`).join('');
    $('tb-topicos').innerHTML = Object.keys(S.retidos).sort().map((t) => { const p = S.retidos[t]; let v = p; try { const j = JSON.parse(p); v = fmt(j.valor, 2) + ' ' + j.un; } catch (e) { /* texto */ }
      return `<tr class="${ok && casa(f, t) ? '' : 'mute'}"><td class="mono">${t}</td><td class="mono">${esc(v)}</td></tr>`; }).join('');
  }
  function rSeries() {
    const sel = $('s-sensor'); if (!sel.value) sel.value = S.sel;
    const s = SX[sel.value], st = S.sen[s.id];
    const pts = st.hist.slice(-400);
    const W = 1000, H = 300, ml = 56, mr = 14, mt = 14, mb = 30;
    let g = '';
    if (!pts.length) { $('grafico').innerHTML = '<text x="500" y="150" text-anchor="middle">Sem dados ainda: clique em Iniciar.</text>'; }
    else {
      const t0 = pts[0].t, t1 = Math.max(pts[pts.length - 1].t, t0 + 3600);
      let lo = Math.min(...pts.map((p) => p.v)), hi = Math.max(...pts.map((p) => p.v));
      if (s.lim) { hi = Math.max(hi, s.lim[1] * 1.02); lo = Math.min(lo, s.lim[0] * 0.75); }
      const pad = (hi - lo) * 0.08 || 1; lo -= pad; hi += pad;
      const X = (t) => ml + (t - t0) / (t1 - t0) * (W - ml - mr), Y = (v) => mt + (hi - v) / (hi - lo) * (H - mt - mb);
      if (s.lim) {
        const lims = [...s.lim, hi + 1e9];
        ['atencao', 'alerta', 'alarme'].forEach((n, i) => { const a = Math.min(Math.max(lims[i], lo), hi), b = Math.min(Math.max(lims[i + 1], lo), hi); if (b > a) g += `<rect class="faixa ${n}" x="${ml}" y="${Y(b)}" width="${W - ml - mr}" height="${Y(a) - Y(b)}"/>`; });
        s.lim.forEach((l, i) => { if (l > lo && l < hi) g += `<line class="lim" x1="${ml}" x2="${W - mr}" y1="${Y(l)}" y2="${Y(l)}" stroke="${['#F2CB0A', '#F2700A', '#FF2B5F'][i]}"/><text x="${W - mr - 4}" y="${Y(l) - 4}" text-anchor="end">${['atenção', 'alerta', 'alarme'][i]} ${fmt(l, s.dec >= 1 ? 1 : 0)}</text>`; });
      }
      for (let k = 0; k <= 4; k++) { const v = lo + (hi - lo) * k / 4; g += `<line class="eixo" x1="${ml}" x2="${W - mr}" y1="${Y(v)}" y2="${Y(v)}"/><text x="${ml - 6}" y="${Y(v) + 4}" text-anchor="end">${fmt(v, s.dec >= 2 ? 1 : s.dec)}</text>`; }
      for (let k = 0; k <= 4; k++) { const t = t0 + (t1 - t0) * k / 4; g += `<text x="${X(t)}" y="${H - 8}" text-anchor="middle">${dataHora(t).slice(4)}</text>`; }
      g += `<polyline class="linha" points="${pts.map((p) => X(p.t).toFixed(1) + ',' + Y(p.v).toFixed(1)).join(' ')}"/>`;
      g += pts.filter((p) => p.re || p.fake).map((p) => `<circle class="ponto ${p.fake ? 'bad' : 're'}" cx="${X(p.t)}" cy="${Y(p.v)}" r="3.5"/>`).join('');
      g += `<text x="${ml}" y="${mt - 2}">${s.un}</text>`;
      $('grafico').innerHTML = g;
    }
    $('s-info').innerHTML = `${pts.length} pontos · intervalo de ${s.int / 60} min · <span class="ponto-leg" style="color:#C2A5FF">●</span> reenviada <span style="color:#FF7A95">●</span> falsa`;
    const u = st.ult;
    $('lp').textContent = u ? `leitura,obra=torre-a,setor=${s.setor},tipo=${s.tipo},sensor=${s.id} valor=${u.v.toFixed(s.dec + 1)},bruto=${u.bruto.toFixed(4)},bat=${u.bat.toFixed(2)},q="${u.q}" ${(T0 + u.tm * 1000)}000000\n\n# tags (identificam a série): obra, setor, tipo, sensor\n# fields (o que se mede): valor, bruto, bat, q\n# timestamp: hora da MEDIÇÃO, em nanossegundos UTC` : 'Sem leituras ainda.';
    const series = SENSORES.length;
    $('kpis-series').innerHTML = kpi('Séries (sensores)', series) + kpi('Pontos por dia', pontosDia().toLocaleString('pt-BR'), 'blue') + kpi('Pontos por ano', Math.round(pontosDia() * 365).toLocaleString('pt-BR'));
  }
  function rAlarmes() {
    const ativos = SENSORES.filter((s) => ['alerta', 'alarme'].includes(S.sen[s.id].niv)).length;
    const n = S.notifs.length, cen = S.cen ? S.notifs.filter((x) => x.t >= S.cen.t0).length : n;
    $('kpis-alm').innerHTML = kpi('Notificações' + (S.cen ? ' no cenário' : ''), cen, cen > 15 ? 'red' : cen ? 'amber' : 'green') + kpi('Sensores em alerta ou alarme', ativos, ativos ? 'red' : 'green') + kpi('Em atenção', SENSORES.filter((s) => S.sen[s.id].niv === 'atencao').length, 'amber') + kpi('Regras ligadas', Object.values(S.regras).filter(Boolean).length + ' de ' + REGRAS.length, 'blue');
    $('tb-alm').innerHTML = S.notifs.slice(0, 120).map((x) => `<tr><td class="mono">${dataHora(x.t)}</td><td>${x.id}</td><td><span class="niv ${x.niv}">${ROT[x.niv]}</span></td><td>${esc(x.motivo)}</td><td>${esc(x.acao)}</td></tr>`).join('') || '<tr><td colspan="5" class="hint">Nenhuma notificação.</td></tr>';
    REGRAS.forEach((r) => { const i = $('rg-' + r.id); if (i) i.checked = !!S.regras[r.id]; });
  }
  function montarRegras() {
    $('regras').innerHTML = REGRAS.map((r) => `<label class="sw"><input type="checkbox" id="rg-${r.id}"><span class="d"><b>${r.nome}</b><small>${r.d}</small></span></label>`).join('');
    REGRAS.forEach((r) => $('rg-' + r.id).addEventListener('change', (e) => { S.regras[r.id] = e.target.checked; render(); }));
    $('tarp').innerHTML = '<div class="tarp">' + NIVEIS.map((n) => `<div class="${n}"><b><span class="niv ${n}">${ROT[n]}</span> ${TARP[n][0]}</b>${TARP[n][1]}<br><small>${TARP[n][2]} · prazo: ${TARP[n][3]}</small></div>`).join('') + '</div>';
    $('protecoes').innerHTML = PROTECOES.map((r) => `<label class="sw"><input type="checkbox" id="pt-${r.id}"><span class="d"><b>${r.nome}</b><small>${r.d}</small></span></label>`).join('');
    PROTECOES.forEach((r) => $('pt-' + r.id).addEventListener('change', (e) => { S.seg[r.id] = e.target.checked; render(); }));
  }
  function montarCenarios() {
    $('cen-cards').innerHTML = CENARIOS.map((c) => `<div class="card" data-id="${c.id}"><h3>${esc(c.titulo)}</h3><p>${esc(c.desc)}</p><p class="hint">${c.aula} · velocidade ${$('velocidade').querySelector(`option[value="${c.vel}"]`).textContent} · duração ${c.dur >= DIA ? fmt(c.dur / DIA, 1) + ' dia(s)' : c.dur / 3600 + ' h'}</p><button class="btn go" data-cen="${c.id}">Iniciar cenário</button></div>`).join('');
    $('cen-cards').querySelectorAll('[data-cen]').forEach((b) => b.addEventListener('click', () => iniciarCenario(b.dataset.cen)));
  }
  function rCenarios() {
    $('v-cenarios').classList.toggle('rodando', !!S.cen);
    $('cen-cards').querySelectorAll('.card').forEach((el) => el.classList.toggle('on', !!S.cen && S.cen.id === el.dataset.id));
    const tl = $('cen-timeline'); tl.hidden = !S.cen;
    if (!S.cen) return;
    const c = S.cen.c, o = off();
    $('cen-titulo').textContent = c.titulo + ' · ' + (S.cen.fim ? 'concluído' : 'em andamento, ' + (o >= DIA ? fmt(o / DIA, 1) + ' dia(s)' : Math.round(o / 60) + ' min'));
    $('cen-passos').innerHTML = c.passos.map((p, i) => `<li class="${S.cen.passos[i].feito ? 'det' : 'pend'}"><span class="mono">+${p[0] >= DIA ? fmt(p[0] / DIA, 1) + ' d' : p[0] >= 3600 ? fmt(p[0] / 3600, 1) + ' h' : Math.round(p[0] / 60) + ' min'}</span><span class="ic">${p[1]}</span><span>${esc(p[2])}</span><span></span></li>`).join('');
    const A = S.cen.atk;
    $('cen-dica').textContent = c.id === 'admin' && A ? (A.fim === 'bloq-rede' ? 'Bloqueado: o painel do gateway não está exposto à internet.' : A.fim === 'bloq-senha' ? 'Bloqueado: a senha de fábrica foi trocada.' : A.negadas ? 'Invasor entrou no gateway, mas a ACL negou ' + A.negadas + ' publicação(ões) falsa(s).' : S.invasor ? 'O invasor está publicando leituras falsas do I-2.' : '') : '';
  }
  function rDrone() {
    const voos = S.voou ? [...VOOS, VOO_NOVO] : VOOS, u = voos[voos.length - 1];
    const av = S.voou ? SERVICOS.reduce((a, x) => a + x[1] * x[3] / 100, 0) : u.av;
    const prev = 45, orc = 20, VP = orc * prev / 100, VA = orc * av / 100, CR = S.voou ? 8.6 : 8.25;
    $('kpis-drone').innerHTML = kpi('Avanço medido', fmt(av, 1) + '%', 'blue') + kpi('Previsto (curva S)', fmt(prev, 1) + '%') + kpi('Dito na reunião', '62%', 'red') + kpi('VP · VA · CR (R$ mi)', fmt(VP, 2) + ' · ' + fmt(VA, 2) + ' · ' + fmt(CR, 2)) + kpi('IDP = VA/VP', fmt(VA / VP, 2), VA / VP < 1 ? 'red' : 'green') + kpi('IDC = VA/CR', fmt(VA / CR, 2), VA / CR < 1 ? 'red' : 'green');
    $('tb-voos').innerHTML = voos.slice().reverse().map((v) => `<tr><td>${v.data}</td><td class="mono">${fmt(v.gsd, 1)} cm/px</td><td class="mono">${v.gcp}</td><td class="mono">${fmt(v.rmse, 1)} cm</td><td class="mono">${v.vol.toLocaleString('pt-BR')} m³</td><td class="mono">${fmt(v.av, 1)}%</td></tr>`).join('');
    $('voo-status').textContent = S.vooAnim != null ? 'Drone em voo (veja a aba Canteiro)…' : S.voou ? 'Voo de 16/11 processado: 46.900 m³ escavados (a planilha dizia 48.200).' : 'Último voo: 09/11.';
    $('btn-voar').disabled = S.voou || S.vooAnim != null;
    $('tb-bim').innerHTML = SENSORES.map((s) => { const n = nivTela(S.sen[s.id]); return `<tr><td>${s.id}</td><td>${esc(s.elem)}</td><td class="mono">${s.guid}</td><td><span class="niv ${n}">${ROT[n]}</span></td></tr>`; }).join('');
    $('bars-avanco').innerHTML = SERVICOS.map((x) => { const ex = S.voou ? x[3] : x[3] * u.av / 40.75; return `<div class="bar"><span>${x[0]} <small>(peso ${x[1]}%)</small></span><span class="t"><i style="width:${ex}%" class="${ex < x[2] ? 'red' : ''}"></i></span><span class="mono">${fmt(ex, 0)}% / ${x[2]}%</span></div>`; }).join('') + '<p class="hint">Barra: executado; número: executado / previsto. Fontes: ' + SERVICOS.map((x) => x[0] + ' — ' + x[4]).join('; ') + '.</p>';
  }
  function rSeguranca() {
    const on = Object.values(S.seg).filter(Boolean).length;
    const A = S.cen && S.cen.id === 'admin' ? S.cen.atk : null;
    $('kpis-seg').innerHTML = kpi('Proteções ligadas', on + ' de ' + PROTECOES.length, on === PROTECOES.length ? 'green' : on ? 'amber' : 'red') + kpi('Painel do gateway na internet', S.seg.segmentada ? 'não' : 'sim', S.seg.segmentada ? 'green' : 'red') + kpi('Senha do GW-01', S.seg.senha ? 'única' : 'admin (fábrica)', S.seg.senha ? 'green' : 'red') + kpi('Leituras falsas aceitas', S.mqtt.filter((m) => m.fake).length, S.mqtt.some((m) => m.fake) ? 'red' : 'green') + kpi('Publicações negadas (ACL)', A && A.negadas ? A.negadas : 0, 'blue');
    PROTECOES.forEach((r) => { const i = $('pt-' + r.id); if (i) i.checked = !!S.seg[r.id]; });
    const fw = S.seg.firmware ? 'v2.4.1 (atual)' : 'v1.9.0 (2023)';
    const disp = [['GW-01 · gateway LoRaWAN (grua)', S.seg.senha ? 'única' : 'admin/admin', fw, S.seg.segmentada ? 'só VPN' : 'internet, porta 80'], ['Broker MQTT', S.seg.acl ? 'por cliente + ACL' : 'uma senha para todos', 'atual', S.seg.tls ? '8883 (TLS)' : '1883 (sem TLS)'], ['Câmera da grua', S.seg.senha ? 'única' : 'admin/12345', fw, S.seg.segmentada ? 'rede IoT' : 'rede do escritório'], ['Nós LoRa (10)', 'chaves AES-128 por nó', S.seg.firmware ? 'atual' : 'atual', 'só rádio']];
    $('tb-disp').innerHTML = disp.map((d) => `<tr><td>${d[0]}</td><td class="mono">${d[1]}</td><td class="mono">${d[2]}</td><td>${d[3]}</td></tr>`).join('') + `<tr><td>Câmera: privacidade</td><td colspan="3">${S.seg.mascara ? '<span class="tag ok">máscara no vizinho e desfoque de rostos · guarda de 30 dias</span>' : '<span class="tag bad">grava rostos, a janela e o quintal do vizinho, sem prazo de guarda</span>'}</td></tr>`;
    $('tb-broker').innerHTML = S.broker.slice(0, 40).map((b) => `<tr><td class="mono">${dataHora(b.t).slice(4)}</td><td>${esc(b.txt)}</td></tr>`).join('');
  }

  /* ------------------------- abas e laço ------------------------- */
  const RENDER = { canteiro: rCanteiro, leituras: rLeituras, rede: rRede, mqtt: rMqtt, series: rSeries, alarmes: rAlarmes, cenarios: rCenarios, drone: rDrone, seguranca: rSeguranca };
  let aba = 'canteiro', ultCen = 0;
  function render() {
    $('relogio').textContent = hora(S.t);
    $('relogio-sub').textContent = dataHora(S.t).slice(0, 9) + '/2026 · relógio simulado';
    const fila = SENSORES.reduce((a, s) => a + S.sen[s.id].fila.length, 0);
    $('badge-leit').textContent = fila ? fila : '';
    const al = SENSORES.filter((s) => ['alerta', 'alarme'].includes(S.sen[s.id].niv)).length;
    $('badge-alm').textContent = al || '';
    if (aba === 'cenarios') { if (performance.now() - ultCen < 1500 && S.rodando) return; ultCen = performance.now(); }
    RENDER[aba] && RENDER[aba]();
  }
  function mostrar(nome) {
    if (!RENDER[nome]) nome = 'canteiro';
    aba = nome; ultCen = 0;
    document.querySelectorAll('.view').forEach((v) => v.classList.toggle('on', v.id === 'v-' + nome));
    document.querySelectorAll('#abas a').forEach((a) => a.classList.toggle('on', a.getAttribute('href') === '#' + nome));
    render();
  }
  let ult = 0, acc = 0;
  function laco(now) {
    const dt = ult ? Math.min(0.1, (now - ult) / 1000) : 0; ult = now;
    if (S.rodando) passo(dt * S.vel);
    animar(dt);
    acc += dt; if (acc > 0.25) { acc = 0; render(); }
    requestAnimationFrame(laco);
  }

  /* ------------------------- eventos da página ------------------------- */
  document.querySelectorAll('#abas a').forEach((a) => a.addEventListener('click', (e) => { e.preventDefault(); mostrar(a.getAttribute('href').slice(1)); history.replaceState(null, '', location.search + a.getAttribute('href')); }));
  $('btn-rodar').addEventListener('click', () => rodar(!S.rodando));
  $('btn-reiniciar').addEventListener('click', () => { rodar(false); novoEstado(true); estavaSaida = true; mostrar(aba); });
  $('velocidade').addEventListener('change', () => (S.vel = +$('velocidade').value));
  $('f-sensor').innerHTML += SENSORES.map((s) => `<option value="${s.id}">${s.id}</option>`).join('');
  $('s-sensor').innerHTML = SENSORES.map((s) => `<option value="${s.id}">${s.nome}</option>`).join('');
  ['f-sensor', 'f-problema', 's-sensor'].forEach((id) => $(id).addEventListener('change', render));
  $('m-filtro').addEventListener('input', render);
  document.querySelectorAll('[data-f]').forEach((b) => b.addEventListener('click', () => { $('m-filtro').value = b.dataset.f; render(); }));
  $('r-adr').addEventListener('change', (e) => { S.adr = e.target.checked; descarregarFilas(); render(); });
  $('r-gw').addEventListener('change', (e) => { S.gw = e.target.checked; render(); });
  $('r-4g').addEventListener('change', (e) => { S.g4 = e.target.checked; render(); });
  $('r-perda').addEventListener('input', (e) => { S.perdaPZ3 = +e.target.value; descarregarFilas(); render(); });
  $('btn-repetir').addEventListener('click', repetirCenario);
  $('btn-voar').addEventListener('click', () => { S.vooAnim = 0; mostrar('canteiro'); history.replaceState(null, '', location.search + '#canteiro'); });
  const sincControles = () => { $('r-adr').checked = S.adr; $('r-gw').checked = S.gw; $('r-4g').checked = S.g4; $('r-perda').value = S.perdaPZ3; $('velocidade').value = String(S.vel); };
  window.addEventListener('message', (e) => {
    const d = e.data || {};
    if (d.reiniciar) { rodar(false); novoEstado(false); estavaSaida = true; }
    if (d.regras) Object.assign(S.regras, d.regras);
    if (d.seg) Object.assign(S.seg, d.seg);
    if (d.rede) { if (d.rede.gw != null) S.gw = d.rede.gw; if (d.rede.adr != null) S.adr = d.rede.adr; if (d.rede.g4 != null) S.g4 = d.rede.g4; if (d.rede.perda != null) S.perdaPZ3 = d.rede.perda; }
    if (d.vel) S.vel = d.vel;
    if (d.sensor && SX[d.sensor]) { S.sel = d.sensor; $('s-sensor').value = d.sensor; }
    sincControles();
    if (d.simAba) mostrar(d.simAba);
    if (d.cenario && C[d.cenario] && d.autostart && (!S.cen || S.cen.id !== d.cenario)) iniciarCenario(d.cenario);
    if (d.rodar && !S.rodando) rodar(true);
    render();
  });

  novoEstado(false); montarPlanta(); montarRegras(); montarCenarios(); sincControles();
  const q = new URLSearchParams(location.search);
  mostrar(location.hash.slice(1) || 'canteiro');
  if (q.get('cenario')) iniciarCenario(q.get('cenario'));
  requestAnimationFrame(laco);
  window.Simulador = { estado: () => S, iniciarCenario, repetirCenario, mostrar, rodar, passo };
})();

// balões de explicação das abas: um único balão posicionado dentro do cabeçalho
(() => {
  const topo = document.querySelector('header.top'), nav = document.getElementById('abas');
  if (!topo || !nav) return;
  const b = document.createElement('div'); b.className = 'dica-aba'; b.setAttribute('role', 'tooltip'); topo.appendChild(b);
  const mostrar = (a) => {
    b.textContent = a.dataset.dica; b.classList.add('on');
    const x = nav.offsetLeft + a.offsetLeft - nav.scrollLeft;
    const esq = Math.max(8, Math.min(x, topo.clientWidth - b.offsetWidth - 8));
    b.style.left = esq + 'px'; b.style.top = (nav.offsetTop + nav.offsetHeight + 6) + 'px';
    b.style.setProperty('--seta', Math.max(10, Math.min(x - esq + 20, b.offsetWidth - 20)) + 'px');
  };
  const esconder = () => b.classList.remove('on');
  nav.querySelectorAll('a[data-dica]').forEach((a) => {
    a.addEventListener('mouseenter', () => mostrar(a)); a.addEventListener('focus', () => mostrar(a));
    a.addEventListener('mouseleave', esconder); a.addEventListener('blur', esconder);
  });
  nav.addEventListener('scroll', esconder);
})();
