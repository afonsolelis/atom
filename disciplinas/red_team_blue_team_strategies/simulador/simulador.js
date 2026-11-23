/* =====================================================================
   Simulador da plataforma da Rede Tatame (fictícia)
   Red Team & Blue Team Strategies — aplicação padrão da disciplina.
   Tudo roda no navegador; nenhum sistema real é tocado.
   Embutido nos slides com ?embed=1; o deck manda postMessage:
     { simAba: 'soc' }                       troca a aba
     { cenario: 'ransomware', autostart }    seleciona (e inicia) um cenário
     { regras: { R5: true }, fontes: { cloud: true } }   ajusta a defesa
     { reiniciar: true }
   ===================================================================== */
(function () {
  'use strict';
  const $ = (id) => document.getElementById(id);
  const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const fmt = new Intl.NumberFormat('pt-BR');
  const pick = (a) => a[Math.floor(Math.random() * a.length)];

  /* ------------------------------ Componentes ------------------------------ */
  const NODES = [
    { id: 'app', x: 110, y: 80, l: 'App do aluno', s: 'app.tatame.com.br', papel: 'Aplicativo dos 36 mil alunos: reserva de aula, check-in, pagamento, vídeos.', dados: 'Token de sessão do aluno; nenhum dado guardado no aparelho além do cache.', exp: 'Internet', fonte: 'gateway' },
    { id: 'portal', x: 110, y: 165, l: 'Portal gestão', s: 'gestao.tatame.com.br', papel: 'Portal web das 240 academias: matrícula, cobrança, graduação.', dados: 'Acessa fichas completas de alunos, inclusive menores e atestados.', exp: 'Internet, com MFA', fonte: 'ident' },
    { id: 'catraca', x: 110, y: 250, l: 'Catracas IoT', s: '10.80.x.0/24', papel: 'Leitor facial na entrada de cada academia; heartbeat a cada 30 s.', dados: 'Modelo biométrico do rosto (dado sensível na LGPD).', exp: 'Rede da academia, saída para a API', fonte: 'catracas' },
    { id: 'net', x: 110, y: 360, l: 'Internet', s: 'inclui o Red Team', ext: true, papel: 'Qualquer origem externa. Nos exercícios, é de onde parte o Red Team autorizado.', dados: '—', exp: '—', fonte: null },
    { id: 'waf', x: 320, y: 165, l: 'CDN / WAF', s: '203.0.113.0/24', papel: 'Borda: cache, TLS, bloqueio de padrões maliciosos e limite de taxa.', dados: 'Logs de todas as requisições externas.', exp: 'Internet', fonte: 'waf' },
    { id: 'hml', x: 320, y: 330, l: 'hml-gestao', s: 'sem WAF · fora do inventário', papel: 'Ambiente de homologação esquecido de um projeto de 2024.', dados: 'Cópia antiga do banco de produção, com alunos reais.', exp: 'Internet, sem WAF', fonte: null },
    { id: 'gw', x: 505, y: 165, l: 'API gateway', s: 'api.tatame.com.br', papel: 'Valida o JWT, aplica limite de taxa e roteia para os microsserviços.', dados: 'Log de cada requisição (rota, status, latência, aluno anonimizado).', exp: 'Atrás do WAF', fonte: 'gateway' },
    { id: 'pay', x: 505, y: 300, l: 'PagaFácil', s: 'parceiro · fora do escopo', ext: true, papel: 'Parceiro de pagamentos (terceiro). Nunca entra no escopo dos exercícios.', dados: 'Cartões tokenizados (PCI DSS).', exp: 'Internet do parceiro', fonte: null },
    { id: 'ident', x: 700, y: 55, l: 'svc-identidade', s: 'OAuth 2.0 · MFA', papel: 'Login, emissão de tokens, MFA do portal e da VPN.', dados: 'Hashes de senha, fatores de MFA, sessões.', exp: 'Interno', fonte: 'ident' },
    { id: 'alunos', x: 700, y: 120, l: 'svc-alunos', s: 'fichas e matrículas', papel: 'Fichas de alunos, responsáveis legais, atestados.', dados: 'Dados pessoais e de saúde.', exp: 'Interno', fonte: 'gateway' },
    { id: 'checkin', x: 700, y: 185, l: 'svc-checkin', s: 'frequência', papel: 'Registra check-ins da catraca e do app.', dados: 'Frequência por aluno e academia.', exp: 'Interno', fonte: 'gateway' },
    { id: 'cobranca', x: 700, y: 250, l: 'svc-cobranca', s: 'mensalidades', papel: 'Mensalidades e repasses; fala com a PagaFácil.', dados: 'Status de pagamento (sem cartão).', exp: 'Interno', fonte: 'gateway' },
    { id: 'notif', x: 700, y: 315, l: 'svc-notificacoes', s: 'e-mail e push', papel: 'Avisos de aula, cobrança e graduação.', dados: 'E-mails e tokens de push.', exp: 'Interno', fonte: 'gateway' },
    { id: 'db', x: 890, y: 95, l: 'db-alunos', s: 'PostgreSQL 10.40.9.0/24', papel: 'Banco principal de alunos.', dados: '36 mil fichas, ~30% de menores.', exp: 'Interno', fonte: 'cloud' },
    { id: 'kafka', x: 890, y: 215, l: 'Kafka', s: '3 tópicos · 4 regiões', papel: 'Barramento de eventos: tatame.eventos, tatame.auditoria, tatame.seguranca.', dados: 'Eventos com o aluno anonimizado (HMAC).', exp: 'Interno', fonte: null },
    { id: 'cep', x: 1075, y: 150, l: 'Motor CEP', s: 'regras em tempo real', papel: 'Correlaciona eventos em janelas de tempo e gera alertas.', dados: 'Estado das janelas das regras.', exp: 'Interno', fonte: null },
    { id: 'lake', x: 1075, y: 240, l: 'Data lake', s: 'bucket tatame-lake', papel: 'Guarda os eventos brutos para análise e reprocessamento.', dados: 'Histórico de eventos (13 meses).', exp: 'Interno', fonte: 'cloud' },
    { id: 'siem', x: 1075, y: 345, l: 'SIEM · SOC', s: 'Blue Team 24x7', papel: 'Recebe telemetria e alertas; o SOC investiga e responde.', dados: 'Logs de segurança (retenção de 12 meses).', exp: 'Interno', fonte: null },
    { id: 'mail', x: 320, y: 470, l: 'E-mail', s: 'mx1.tatame.com.br', papel: 'Gateway de e-mail corporativo com SPF/DMARC.', dados: 'Caixas dos 120 colaboradores.', exp: 'Internet', fonte: 'email' },
    { id: 'vpn', x: 320, y: 570, l: 'VPN NetGuard', s: 'vpn.tatame.com.br', papel: 'Acesso remoto da equipe da sede.', dados: 'Sessões e logins remotos.', exp: 'Internet', fonte: 'ident' },
    { id: 'nb', x: 525, y: 470, l: 'NB-FIN-031', s: 'notebook · EDR', papel: 'Notebook da analista do financeiro.', dados: 'Planilhas de repasse.', exp: 'Rede da sede', fonte: 'edr' },
    { id: 'ad', x: 525, y: 570, l: 'SRV-AD-01', s: 'corp.tatame.local', papel: 'Active Directory da sede.', dados: 'Contas e grupos de 120 colaboradores.', exp: 'Rede da sede', fonte: 'ad' },
    { id: 'arq', x: 730, y: 470, l: 'SRV-ARQ-01', s: 'servidor de arquivos', papel: 'Arquivos do financeiro e do atendimento.', dados: 'Exportações de fichas de alunos.', exp: 'Rede da sede', fonte: 'edr' },
    { id: 'erp', x: 730, y: 570, l: 'SRV-ERP-01', s: 'ERP da sede', papel: 'ERP financeiro e contábil.', dados: 'Contas a pagar e receber.', exp: 'Rede da sede', fonte: 'edr' },
    { id: 'edr', x: 930, y: 520, l: 'Console EDR', s: 'agentes da sede', papel: 'Recebe a telemetria dos agentes e permite isolar máquinas.', dados: 'Processos, conexões, arquivos.', exp: 'Interno', fonte: null }
  ];
  const N = Object.fromEntries(NODES.map((n) => [n.id, n]));
  const EDGES = [['app', 'waf'], ['portal', 'waf'], ['catraca', 'waf'], ['net', 'waf'], ['net', 'hml'], ['net', 'mail'], ['net', 'vpn'], ['waf', 'gw'], ['hml', 'db'],
    ['gw', 'ident'], ['gw', 'alunos'], ['gw', 'checkin'], ['gw', 'cobranca'], ['gw', 'notif'], ['cobranca', 'pay'], ['alunos', 'db'],
    ['ident', 'kafka'], ['alunos', 'kafka'], ['checkin', 'kafka'], ['cobranca', 'kafka'], ['kafka', 'cep'], ['kafka', 'lake'], ['kafka', 'siem'], ['cep', 'siem'],
    ['mail', 'nb'], ['vpn', 'ad'], ['nb', 'ad'], ['ad', 'arq'], ['ad', 'erp'], ['arq', 'erp'], ['nb', 'edr'], ['arq', 'edr'], ['erp', 'edr'], ['edr', 'siem'], ['ad', 'siem'], ['arq', 'net']];
  const LEGIT = [['app', 'waf', 'gw', 'checkin', 'kafka', 'cep'], ['app', 'waf', 'gw', 'alunos', 'db'], ['portal', 'waf', 'gw', 'alunos', 'kafka', 'lake'], ['catraca', 'waf', 'gw', 'checkin', 'kafka', 'lake'],
    ['portal', 'waf', 'gw', 'cobranca', 'pay'], ['app', 'waf', 'gw', 'ident', 'kafka', 'siem'], ['portal', 'waf', 'gw', 'notif']];

  /* ------------------------------ Telemetria ------------------------------ */
  const FONTES = [
    { id: 'waf', l: 'Logs do WAF/CDN', d: 'Toda requisição externa, com IP, rota e status.', eps: 120, on: true },
    { id: 'gateway', l: 'Log do API gateway', d: 'Rota, status, latência, token e aluno anonimizado.', eps: 300, on: true },
    { id: 'ident', l: 'Auditoria de identidade', d: 'Logins, falhas, uso de MFA no portal, no app e na VPN.', eps: 40, on: true },
    { id: 'edr', l: 'EDR dos notebooks e servidores', d: 'Processos, linhas de comando, acesso a memória, conexões.', eps: 60, on: true },
    { id: 'ad', l: 'Logs do Active Directory', d: 'Eventos 4624, 4625, 4769 e consultas LDAP.', eps: 80, on: true },
    { id: 'dns', l: 'DNS e proxy da sede', d: 'Domínios consultados e acessados pelos colaboradores.', eps: 150, on: true },
    { id: 'email', l: 'Gateway de e-mail', d: 'Remetente, SPF/DMARC, links e anexos.', eps: 10, on: true },
    { id: 'cloud', l: 'Acesso a buckets e saída de rede', d: 'Leituras no banco e no data lake, bytes enviados para fora.', eps: 30, on: false },
    { id: 'catracas', l: 'Heartbeat e firmware das catracas', d: '240 catracas a cada 30 s (8 eventos/s) e assinatura do firmware.', eps: 8, on: false },
    { id: 'ct', l: 'Monitor de certificados (CT)', d: 'Novos certificados emitidos para *.tatame.com.br.', eps: 0.01, on: false }
  ];
  const F = Object.fromEntries(FONTES.map((f) => [f.id, f]));
  const GB_POR_EPS_DIA = 0.0432; // 0,5 KB por evento
  const CUSTO_GB = 2.5;          // R$ por GB ingerido (valor fictício)

  /* ------------------------------ Regras do CEP ------------------------------ */
  const REGRAS = [
    { id: 'R1', l: 'Acesso a domínio recém-registrado logo após e-mail externo', f: 'dns', tec: 'T1566.002', sev: 'alta', on: true, dsl: 'sequence by user within 30m\n  [email where sender.domain_age_days < 7]\n  [dns   where query == email.sender.domain]' },
    { id: 'R2', l: 'Muitas falhas de login seguidas de sucesso', f: 'ident', tec: 'T1110.004', sev: 'alta', on: true, dsl: 'count(login.failure) by src_ip > 50 within 5m\n  followed by login.success from same src_ip' },
    { id: 'R3', l: 'Token lendo fichas de muitos alunos diferentes (BOLA)', f: 'gateway', tec: 'T1190', sev: 'critica', on: false, dsl: 'count_distinct(path.aluno_id) by token > 20 within 1m\n  where path.aluno_id != token.sub' },
    { id: 'R4', l: 'Varredura: excesso de 403/404 por IP', f: 'waf', tec: 'T1595', sev: 'media', on: true, dsl: 'count(status in (403, 404)) by src_ip > 200 within 2m' },
    { id: 'R5', l: 'RDP de estação de trabalho para servidor', f: 'ad', tec: 'T1021.001', sev: 'alta', on: false, dsl: 'event_id == 4624 and logon_type == 10\n  and src_host like "NB-%" and dst_host like "SRV-%"' },
    { id: 'R6', l: 'Acesso à memória do LSASS', f: 'edr', tec: 'T1003', sev: 'critica', on: true, dsl: 'target.process == "lsass.exe" and access == "read_memory"\n  and not source.process in allowlist_assinados' },
    { id: 'R7', l: 'Exclusão de cópias de sombra', f: 'edr', tec: 'T1490', sev: 'critica', on: true, dsl: 'process.cmdline contains "shadow" and process.cmdline contains "delete"' },
    { id: 'R8', l: 'Ferramenta de acesso remoto não aprovada', f: 'edr', tec: 'T1219', sev: 'alta', on: false, dsl: 'process.name in lista_acesso_remoto\n  and not process.name in lista_aprovada_ti' },
    { id: 'R9', l: 'Saída volumosa para destino novo', f: 'cloud', tec: 'T1567.002', sev: 'alta', on: false, dsl: 'sum(bytes_out) by host, dest_domain > 1 GB within 1h\n  and dest_domain.first_seen < 7d' },
    { id: 'R10', l: 'Catraca fora do padrão (volume ou firmware)', f: 'catracas', tec: 'T1495', sev: 'media', on: false, dsl: 'firmware.signature != "valida"\n  or heartbeat_rate > 3 * baseline(catraca)' },
    { id: 'R11', l: 'Login sem MFA em conta privilegiada ou VPN', f: 'ident', tec: 'T1078', sev: 'alta', on: true, dsl: 'login.success and mfa.used == false\n  and account.type in ("admin", "vpn")' },
    { id: 'R12', l: 'Certificado novo para subdomínio fora do inventário', f: 'ct', tec: 'T1596', sev: 'baixa', on: false, dsl: 'ct.new_cert and domain like "*.tatame.com.br"\n  and domain not in inventario' },
    { id: 'R13', l: 'Consulta em massa ao AD', f: 'ad', tec: 'T1087.002', sev: 'media', on: false, dsl: 'count(ldap.query where objectClass == "user") by host > 500 within 5m' }
  ];
  const R = Object.fromEntries(REGRAS.map((r) => [r.id, r]));

  /* ------------------------------ Cenários ------------------------------ */
  // t = segundos simulados após o início; caminho = nós percorridos pelo pacote vermelho
  const CENARIOS = [
    { id: 'phishing', l: 'Phishing simulado no financeiro', aulas: 'Aulas 1 e 7', d: 'Campanha autorizada: 40 e-mails de um domínio registrado há 2 dias; uma analista clica e digita a senha.', passos: [
      { t: 0, no: 'mail', c: ['net', 'mail'], txt: '40 e-mails de rh@portal-rh-beneficios.example chegam ao financeiro', tec: 'T1566.002', f: 'email', r: null },
      { t: 240, no: 'nb', c: ['mail', 'nb'], txt: 'Carla Dias clica no link e abre a página falsa (domínio com 2 dias)', tec: 'T1566.002', f: 'dns', r: 'R1' },
      { t: 330, no: 'ident', c: ['net', 'vpn', 'ident'], txt: 'A senha digitada na página falsa é usada na VPN; o MFA bloqueia o acesso', tec: 'T1078', f: 'ident', r: null, bloqueado: true }
    ] },
    { id: 'recon', l: 'Reconhecimento externo', aulas: 'Aulas 5 e 6', d: 'Levantamento autorizado da superfície: certificados públicos, DNS, varredura da borda e o subdomínio esquecido.', passos: [
      { t: 0, no: 'net', c: ['net'], txt: 'Consulta a certificados públicos revela hml-gestao.tatame.com.br', tec: 'T1596', f: 'ct', r: 'R12' },
      { t: 90, no: 'net', c: ['net'], txt: 'Resolução de 180 nomes candidatos em DNS público', tec: 'T1596', f: null, r: null },
      { t: 180, no: 'waf', c: ['net', 'waf'], txt: 'Varredura de portas e rotas contra 203.0.113.0/24', tec: 'T1595', f: 'waf', r: 'R4', http: ['GET', '/admin', 404, 60] },
      { t: 300, no: 'hml', c: ['net', 'hml'], txt: 'Varredura em hml-gestao, que não passa pelo WAF: painel administrativo e versão antiga', tec: 'T1595', f: null, r: null },
      { t: 420, no: 'hml', c: ['net', 'hml', 'db'], txt: 'Achado do relatório: a homologação usa cópia antiga do banco com alunos reais', tec: 'T1190', f: null, r: null }
    ] },
    { id: 'api-abuso', l: 'Abuso da API do app', aulas: 'Aulas 6 e 10', d: 'Senhas vazadas de outros sites testadas no app e leitura de fichas de outros alunos trocando o id na URL (BOLA).', passos: [
      { t: 0, no: 'ident', c: ['net', 'waf', 'gw', 'ident'], txt: '2.000 tentativas de login com senhas vazadas, a partir de 30 IPs', tec: 'T1110.004', f: 'ident', r: 'R2', http: ['POST', '/v1/auth/login', 401, 80] },
      { t: 150, no: 'ident', c: ['net', 'waf', 'gw', 'ident'], txt: '14 contas entram: reuso de senha e app sem MFA', tec: 'T1078', f: 'ident', r: null, http: ['POST', '/v1/auth/login', 200, 14] },
      { t: 270, no: 'alunos', c: ['net', 'waf', 'gw', 'alunos', 'db'], txt: 'Com um token válido, trocando o id na URL, o atacante lê fichas de outros alunos', tec: 'T1190', f: 'gateway', r: 'R3', http: ['GET', '/v1/alunos/{id}', 200, 60] },
      { t: 420, no: 'alunos', c: ['gw', 'alunos', 'db'], txt: '1.300 fichas lidas em 6 minutos, incluindo responsáveis de alunos menores', tec: 'T1190', f: 'gateway', r: 'R3', http: ['GET', '/v1/alunos/{id}', 200, 60] }
    ] },
    { id: 'ransomware', l: 'Emulação do Grupo Cobalto Austral', aulas: 'Aulas 2, 8, 12 e 13', d: 'Cadeia de ransomware emulada: conta válida na VPN, descoberta, RDP, credenciais, cópia de dados e impacto na sede.', passos: [
      { t: 0, no: 'vpn', c: ['net', 'vpn'], txt: 'Login na VPN com a senha vazada de caio.mendes, sem MFA', tec: 'T1078', f: 'ident', r: 'R11' },
      { t: 150, no: 'ad', c: ['vpn', 'ad'], txt: 'Consulta em massa ao AD: usuários, grupos e servidores', tec: 'T1087.002', f: 'ad', r: 'R13' },
      { t: 300, no: 'arq', c: ['vpn', 'ad', 'arq'], txt: 'Acesso remoto (RDP) para SRV-ARQ-01', tec: 'T1021.001', f: 'ad', r: 'R5' },
      { t: 420, no: 'arq', c: ['arq'], txt: 'Leitura da memória do LSASS para obter outras credenciais', tec: 'T1003', f: 'edr', r: 'R6' },
      { t: 540, no: 'erp', c: ['arq', 'erp'], txt: 'RDP para SRV-ERP-01 com a conta de serviço obtida', tec: 'T1021.001', f: 'ad', r: 'R5' },
      { t: 660, no: 'arq', c: ['arq', 'net'], txt: 'Cópia de 4,2 GB de exportações de fichas para armazenamento externo', tec: 'T1567.002', f: 'cloud', r: 'R9' },
      { t: 780, no: 'erp', c: ['erp'], txt: 'Exclusão das cópias de sombra dos servidores', tec: 'T1490', f: 'edr', r: 'R7' },
      { t: 840, no: 'erp', c: ['erp', 'arq'], txt: 'Impacto: arquivos dos servidores da sede cifrados', tec: 'T1486', f: 'edr', r: null, impacto: true }
    ] },
    { id: 'catraca', l: 'Catraca adulterada', aulas: 'Aulas 4 e 9', d: 'Uma catraca da academia 117 recebe firmware não assinado e passa a gerar check-ins falsos.', passos: [
      { t: 0, no: 'catraca', c: ['catraca', 'waf', 'gw'], txt: 'A catraca da academia 117 passa a enviar heartbeats 10 vezes por segundo', tec: 'T1499', f: 'catracas', r: 'R10' },
      { t: 150, no: 'catraca', c: ['catraca'], txt: 'Firmware não assinado é carregado na catraca', tec: 'T1495', f: 'catracas', r: 'R10' },
      { t: 300, no: 'checkin', c: ['catraca', 'waf', 'gw', 'checkin', 'kafka'], txt: 'Check-ins falsos inflam a frequência da academia 117', tec: 'T1565', f: 'gateway', r: null, http: ['POST', '/v1/checkin', 201, 40] }
    ] },
    { id: 'exfiltracao', l: 'Acesso remoto não aprovado e saída de dados', aulas: 'Aulas 11 e 14', d: 'Uma ferramenta de acesso remoto não aprovada aparece no ERP e, dias depois, dados saem para a internet.', passos: [
      { t: 0, no: 'erp', c: ['erp'], txt: 'Ferramenta de acesso remoto não aprovada (ConectaJá) instalada no SRV-ERP-01', tec: 'T1219', f: 'edr', r: 'R8' },
      { t: 200, no: 'erp', c: ['erp', 'ad', 'net'], txt: 'Conexões periódicas do ConectaJá para 198.51.100.77', tec: 'T1219', f: 'dns', r: null },
      { t: 400, no: 'erp', c: ['erp', 'arq', 'net'], txt: 'Envio de 2,8 GB para armazenamento externo', tec: 'T1567.002', f: 'cloud', r: 'R9' }
    ] }
  ];
  const C = Object.fromEntries(CENARIOS.map((c) => [c.id, c]));
  const TEC_NOMES = { 'T1566.002': 'Phishing: link', 'T1078': 'Contas válidas', 'T1596': 'Busca em bases técnicas abertas', 'T1595': 'Varredura ativa', 'T1190': 'Exploração de aplicação exposta', 'T1110.004': 'Credential stuffing', 'T1087.002': 'Descoberta de contas de domínio', 'T1021.001': 'Serviços remotos: RDP', 'T1003': 'Extração de credenciais do SO', 'T1567.002': 'Exfiltração para nuvem', 'T1490': 'Inibir recuperação do sistema', 'T1486': 'Dados cifrados para impacto', 'T1499': 'Negação de serviço no endpoint', 'T1495': 'Corrupção de firmware', 'T1565': 'Manipulação de dados', 'T1219': 'Software de acesso remoto' };

  const KC = { 'T1593': 'Reconhecimento', 'T1596': 'Reconhecimento', 'T1595': 'Reconhecimento', 'T1566.002': 'Entrega', 'T1078': 'Exploração', 'T1110.004': 'Exploração', 'T1190': 'Exploração',
    'T1087.002': 'Ações no objetivo (descoberta)', 'T1021.001': 'Ações no objetivo (movimento lateral)', 'T1003': 'Ações no objetivo (credenciais)', 'T1567.002': 'Ações no objetivo (exfiltração)',
    'T1490': 'Ações no objetivo (impacto)', 'T1486': 'Ações no objetivo (impacto)', 'T1499': 'Ações no objetivo (impacto)', 'T1495': 'Instalação', 'T1565': 'Ações no objetivo (impacto)', 'T1219': 'Instalação / comando e controle' };

  /* ------------------------------ Superfície ------------------------------ */
  const ATIVOS = [
    { host: 'hml-gestao.tatame.com.br', ip: '203.0.113.45', svc: 'HTTPS (painel antigo)', inv: false, waf: false, cve: 'CVE-2021-41773', cvss: 7.5, epss: 0.94, kev: true, crit: 3, obs: 'Homologação esquecida com cópia de dados reais' },
    { host: 'vpn.tatame.com.br', ip: '203.0.113.30', svc: 'VPN NetGuard', inv: true, waf: false, cve: 'CVE-2026-0000 (fictícia)', cvss: 10.0, epss: 0.96, kev: true, crit: 3, obs: 'Exemplo de falha crítica em appliance de borda' },
    { host: 'mx1.tatame.com.br', ip: '203.0.113.40', svc: 'SMTP', inv: true, waf: false, cve: '—', cvss: 0, epss: 0, kev: false, crit: 2, obs: 'SPF e DMARC em quarentena' },
    { host: 'gestao.tatame.com.br', ip: '203.0.113.21', svc: 'HTTPS (portal)', inv: true, waf: true, cve: 'CVE-2023-44487', cvss: 7.5, epss: 0.82, kev: true, crit: 3, obs: 'Mitigado na CDN; corrigir na origem' },
    { host: 'api.tatame.com.br', ip: '203.0.113.22', svc: 'HTTPS (API)', inv: true, waf: true, cve: 'BOLA (achado de teste)', cvss: 8.1, epss: 0, kev: false, crit: 3, obs: 'Falha de lógica, sem CVE: autorização por objeto' },
    { host: 'www.tatame.com.br', ip: '203.0.113.10', svc: 'HTTPS (site)', inv: true, waf: true, cve: 'CVE-2021-44228', cvss: 10.0, epss: 0.97, kev: true, crit: 1, obs: 'Componente já corrigido; manter no inventário' },
    { host: 'app.tatame.com.br', ip: '203.0.113.20', svc: 'HTTPS (app)', inv: true, waf: true, cve: '—', cvss: 0, epss: 0, kev: false, crit: 3, obs: 'Sem MFA no app do aluno' },
    { host: 'promo-hml.tatame.com.br', ip: '198.51.100.23', svc: 'HTTPS (agência)', inv: false, waf: false, cve: '—', cvss: 0, epss: 0, kev: false, crit: 1, obs: 'Hospedado por terceiro: fora do escopo' }
  ];
  const risco = (a) => (a.cvss / 10) * (0.5 + a.epss) * (a.kev ? 1.5 : 1) * a.crit * (a.waf ? 0.8 : 1) * 10 / 1.5;

  /* ------------------------------ Estado ------------------------------ */
  const T0 = new Date(2026, 10, 16, 9, 0, 0).getTime();
  let S;
  function novoEstado() {
    S = {
      t: 0, rodando: false, vel: +$('velocidade').value, fontes: {}, regras: {}, reqs: [], reqTot: 0, reqMin: [], status: {}, svc: {},
      topicos: { 'tatame.eventos': Array(6).fill(0), 'tatame.auditoria': Array(3).fill(0), 'tatame.seguranca': Array(2).fill(0) },
      msgs: { 'tatame.eventos': [], 'tatame.auditoria': [], 'tatame.seguranca': [] },
      cons: { cep: 0, lake: 0, siem: 0 }, siemParado: false,
      cen: null, alertas: [], seqAlerta: 0, disparos: {}, testadas: {}, nos: {}, pk: [], benignos: [{ t: 420, feito: false }, { t: 1500, feito: false }]
    };
    FONTES.forEach((f) => (S.fontes[f.id] = f.on));
    REGRAS.forEach((r) => (S.regras[r.id] = r.on));
  }

  /* ------------------------------ Utilidades ------------------------------ */
  const relogio = (t) => new Date(T0 + t * 1000).toLocaleTimeString('pt-BR');
  const dur = (s) => (s < 60 ? Math.round(s) + ' s' : s < 3600 ? Math.floor(s / 60) + ' min ' + String(Math.round(s % 60)).padStart(2, '0') + ' s' : (s / 3600).toFixed(1).replace('.', ',') + ' h');
  const hmac = () => 'hm_' + Math.random().toString(16).slice(2, 8);
  const ipExt = () => pick(['203.0.113.', '198.51.100.', '192.0.2.']) + (10 + Math.floor(Math.random() * 230));
  const REGIOES = ['sa-saopaulo', 'sa-saopaulo', 'us-virginia', 'eu-estocolmo', 'ap-sydney'];

  function pubMsg(topico, obj) {
    const parts = S.topicos[topico];
    const p = Math.floor(Math.random() * parts.length);
    parts[p]++;
    S.msgs[topico].unshift(JSON.stringify({ offset: parts[p], particao: p, ...obj }));
    if (S.msgs[topico].length > 25) S.msgs[topico].pop();
  }
  function addReq(r) {
    S.reqs.unshift(r); if (S.reqs.length > 160) S.reqs.pop();
    S.reqTot++; S.reqMin.push({ t: S.t, svc: r.svc, st: r.st });
    S.status[r.st] = (S.status[r.st] || 0) + 1;
  }
  function pacote(caminho, cls) { if (caminho.length > 1 && S.pk.length < 60) S.pk.push({ c: caminho, h: 0, u: 0, cls }); }

  /* ------------------------------ Tráfego legítimo ------------------------------ */
  const ROTAS = [['GET', '/v1/aulas/hoje', 'checkin', 200], ['POST', '/v1/checkin', 'checkin', 201], ['GET', '/v1/alunos/me', 'alunos', 200], ['POST', '/v1/auth/login', 'ident', 200],
    ['POST', '/v1/auth/login', 'ident', 401], ['GET', '/v1/cobrancas/me', 'cobranca', 200], ['PUT', '/v1/alunos/{id}/graduacao', 'alunos', 200], ['POST', '/v1/notificacoes', 'notif', 202], ['GET', '/v1/academias/117/agenda', 'checkin', 200], ['GET', '/v1/alunos/me/fatura', 'cobranca', 404]];
  function trafego(dt) {
    const n = Math.max(1, Math.round(dt * 0.9));
    for (let i = 0; i < n; i++) {
      const r = pick(ROTAS);
      const orig = r[2] === 'checkin' && Math.random() < 0.4 ? 'catraca' : pick(['app', 'app', 'portal']);
      addReq({ t: S.t, m: r[0], rota: r[1].replace('{id}', 1000 + Math.floor(Math.random() * 35000)), st: r[3], ms: 18 + Math.floor(Math.random() * 90), orig, ip: orig === 'catraca' ? '10.80.' + (1 + Math.floor(Math.random() * 240)) + '.' + (10 + Math.floor(Math.random() * 20)) : ipExt(), aluno: hmac(), svc: r[2], reg: pick(REGIOES), atk: false });
      S.svc[r[2]] = (S.svc[r[2]] || 0) + 1;
      pubMsg(r[2] === 'ident' ? 'tatame.auditoria' : 'tatame.eventos', { regiao: pick(REGIOES), academia: 1 + Math.floor(Math.random() * 240), tipo: { checkin: 'checkin', alunos: 'ficha_atualizada', ident: r[3] === 200 ? 'login_ok' : 'login_falhou', cobranca: 'cobranca_consultada', notif: 'aviso_enviado' }[r[2]], aluno: hmac(), ts: relogio(S.t) });
    }
    if (Math.random() < 0.6) pacote(pick(LEGIT), '');
    // consumidores
    const tot = Object.values(S.topicos).flat().reduce((a, b) => a + b, 0);
    S.cons.cep = tot; S.cons.lake = Math.max(S.cons.lake, tot - 3);
    if (!S.siemParado) S.cons.siem = Math.min(tot, S.cons.siem + Math.max(5, (tot - S.cons.siem) * 0.6 + 3));
    S.reqMin = S.reqMin.filter((x) => x.t > S.t - 60);
  }

  /* ------------------------------ Cenários ------------------------------ */
  function iniciarCenario(id) {
    const c = C[id]; if (!c) return;
    S.alertas.forEach((a) => { if (a.st === 'novo' && a.passo) a.st = 'antigo'; });
    S.cen = { id, ini: S.t, passos: c.passos.map((p) => ({ ...p, st: 'pend' })) };
    if (!S.rodando) rodar(true);
    render();
  }
  function repetirCenario() {
    if (!S.cen) return;
    const id = S.cen.id, fontes = { ...S.fontes }, regras = { ...S.regras }, testadas = { ...S.testadas }, vel = S.vel, rod = S.rodando;
    rodar(false); novoEstado(); S.fontes = fontes; S.regras = regras; S.testadas = testadas; S.vel = vel;
    S.benignos.forEach((b) => (b.feito = true));
    iniciarCenario(id); if (!rod) rodar(true);
  }
  function executarPasso(p) {
    const viu = p.f && S.fontes[p.f];
    const regraOk = p.r && S.regras[p.r] && viu;
    p.tExec = S.t;
    if (p.bloqueado) p.st = 'blk';
    else if (regraOk) { p.st = 'esperando'; p.tAlerta = S.t + 45 + Math.random() * 120; }
    else if (viu) p.st = 'parc';
    else p.st = 'miss';
    if (!p.bloqueado && !regraOk && p.impacto) p.st = 'imp';
    S.nos[p.no] = S.nos[p.no] === 'isol' ? 'isol' : (p.bloqueado ? S.nos[p.no] : 'comp');
    // nós de passagem não ficam "comprometidos", mas um isolamento feito pelo SOC persiste
    if (['net', 'mail', 'waf', 'ident', 'gw'].includes(p.no) && !p.impacto && S.nos[p.no] !== 'isol') S.nos[p.no] = undefined;
    S.alvo = { no: p.no, ate: S.t + 60 };
    for (let k = 0; k < 3; k++) pacote(p.c, 'red');
    if (p.http) {
      const [m, rota, st, qtd] = p.http;
      for (let i = 0; i < Math.min(qtd, 18); i++) addReq({ t: S.t, m, rota: rota.replace('{id}', 1000 + Math.floor(Math.random() * 35000)), st, ms: 25 + Math.floor(Math.random() * 60), orig: 'externo', ip: pick(['203.0.113.77', '198.51.100.14', '192.0.2.201', '198.51.100.90']), aluno: hmac(), svc: N[p.no] ? p.no : 'gw', reg: 'sa-saopaulo', atk: true });
    }
    if (viu) pubMsg(p.f === 'ident' || p.f === 'ad' ? 'tatame.auditoria' : 'tatame.eventos', { fonte: p.f, host: N[p.no].l, evento: p.txt, tecnica: p.tec, ts: relogio(S.t) });
  }
  function novoAlerta(a) {
    a.id = 'AL-' + String(++S.seqAlerta).padStart(4, '0'); a.st = 'novo'; a.t = S.t;
    S.alertas.unshift(a); S.disparos[a.r] = (S.disparos[a.r] || 0) + 1;
    pubMsg('tatame.seguranca', { alerta: a.id, regra: a.r, severidade: a.sev, host: N[a.no] ? N[a.no].l : a.no, tecnica: a.tec, ts: relogio(S.t) });
    if (!a.benigno && S.nos[a.no] !== 'isol') S.nos[a.no] = S.nos[a.no] === 'comp' ? 'comp' : 'alerta';
    S.alertaNo = { no: a.no, ate: S.t + 90 };
    pacote(['cep', 'siem'], 'amber');
  }
  function avancarCenario() {
    if (!S.cen) return;
    S.cen.passos.forEach((p) => {
      if (p.st === 'pend' && S.t >= S.cen.ini + p.t) executarPasso(p);
      if (p.st === 'esperando' && S.t >= p.tAlerta) {
        p.st = 'det';
        S.testadas[p.tec] = true;
        novoAlerta({ r: p.r, sev: R[p.r].sev, no: p.no, tec: p.tec, txt: R[p.r].l + ' · ' + p.txt, passo: p, mttd: S.t - p.tExec });
      }
    });
  }
  function benignos() {
    S.benignos.forEach((b, k) => {
      if (!b.feito && S.t >= b.t) {
        b.feito = true;
        if (k === 0 && S.regras.R11 && S.fontes.ident) novoAlerta({ r: 'R11', sev: 'alta', no: 'vpn', tec: 'T1078', txt: 'Login sem MFA na VPN: svc-backup (conta de serviço com exceção documentada)', benigno: true });
        if (k === 1 && S.regras.R4 && S.fontes.waf) novoAlerta({ r: 'R4', sev: 'media', no: 'waf', tec: 'T1595', txt: 'Excesso de 404 vindo do monitor de disponibilidade contratado (status.tatame.com.br)', benigno: true });
      }
    });
  }
  function conter(id) {
    const a = S.alertas.find((x) => x.id === id); if (!a || a.st === 'contido') return;
    a.st = 'contido'; a.tCont = S.t; a.mttr = S.t - a.t;
    if (!a.benigno) S.nos[a.no] = 'isol';
    if (S.cen && !a.benigno && a.passo && S.cen.passos.includes(a.passo)) S.cen.passos.forEach((p) => { if (p.st === 'pend' || p.st === 'esperando') p.st = 'canc'; });
    render();
  }
  function fp(id) { const a = S.alertas.find((x) => x.id === id); if (a) { a.st = 'fp'; if (S.nos[a.no] === 'alerta') S.nos[a.no] = undefined; render(); } }

  /* ------------------------------ Laço ------------------------------ */
  let timer = null;
  function rodar(on) {
    S.rodando = on; $('btn-rodar').textContent = on ? 'Pausar' : 'Iniciar'; $('btn-rodar').classList.toggle('go', !on);
    clearInterval(timer);
    if (on) timer = setInterval(tick, 250);
  }
  function tick() {
    const dt = S.vel * 0.25;
    S.t += dt;
    trafego(dt); avancarCenario(); benignos();
    if (S.alvo && S.t > S.alvo.ate) S.alvo = null;
    if (S.alertaNo && S.t > S.alertaNo.ate) S.alertaNo = null;
    render();
    parent !== window && parent.postMessage({ simStatus: { rodando: S.rodando, relogio: relogio(S.t), alertas: S.alertas.filter((a) => a.st === 'novo').length } }, '*');
  }

  /* ------------------------------ Arquitetura (SVG) ------------------------------ */
  const svg = $('arch'); const NS = 'http://www.w3.org/2000/svg';
  function montarArq() {
    const zonas = [[20, 20, 200, 390, 'CLIENTES'], [235, 20, 170, 390, 'BORDA'], [420, 20, 375, 390, 'MICROSSERVIÇOS'], [810, 20, 360, 390, 'DADOS E SEGURANÇA'], [235, 425, 935, 195, 'SEDE · corp.tatame.local (10.10.0.0/16)']];
    let h = '';
    zonas.forEach(([x, y, w, hh, l]) => (h += `<rect class="zone" x="${x}" y="${y}" width="${w}" height="${hh}" rx="12"/><text class="zone-l" x="${x + 12}" y="${y + 16}">${l}</text>`));
    EDGES.forEach(([a, b]) => (h += `<line class="edge" x1="${N[a].x}" y1="${N[a].y}" x2="${N[b].x}" y2="${N[b].y}"/>`));
    h += '<g id="pk"></g>'; // pacotes passam por baixo das caixas
    NODES.forEach((n) => (h += `<g class="node${n.ext ? ' ext' : ''}" data-id="${n.id}"><rect x="${n.x - 78}" y="${n.y - 24}" width="156" height="48" rx="9"/><text x="${n.x}" y="${n.y - 3}" text-anchor="middle">${esc(n.l)}</text><text class="sub" x="${n.x}" y="${n.y + 13}" text-anchor="middle">${esc(n.s)}</text></g>`));
    svg.innerHTML = h;
    svg.querySelectorAll('.node').forEach((g) => g.addEventListener('click', () => infoNo(g.dataset.id)));
  }
  function infoNo(id) {
    const n = N[id];
    svg.querySelectorAll('.node').forEach((g) => g.classList.toggle('sel', g.dataset.id === id));
    $('no-nome').textContent = n.l;
    const f = n.fonte ? F[n.fonte] : null;
    $('no-info').innerHTML = `<p><b>Papel.</b> ${esc(n.papel)}</p><p><b>Dados.</b> ${esc(n.dados)}</p><p><b>Exposição.</b> ${esc(n.exp)}</p><p><b>Telemetria.</b> ${f ? esc(f.l) + ' ' + (S.fontes[f.id] ? '<span class="tag ok">chega ao SIEM</span>' : '<span class="tag bad">desligada</span>') : '<span class="tag warn">nenhuma fonte</span>'}</p>` + (S.nos[id] ? `<p><b>Estado.</b> ${{ comp: '<span class="tag bad">comprometido no cenário</span>', isol: '<span class="tag ok">isolado pelo SOC</span>', alerta: '<span class="tag warn">com alerta aberto</span>' }[S.nos[id]] || ''}</p>` : '');
  }
  let last = performance.now();
  function anim(now) {
    const dt = Math.max(0, Math.min(0.05, (now - last) / 1000)); last = now;
    const g = $('pk');
    if (g && $('v-arquitetura').classList.contains('on')) {
      let h = '';
      S.pk.forEach((p) => {
        p.u += dt * (p.cls === 'red' ? 1.6 : 2.4);
        if (p.u >= 1) { p.u = 0; p.h++; }
        if (p.h >= p.c.length - 1) { p.done = true; return; }
        const a = N[p.c[p.h]], b = N[p.c[p.h + 1]];
        h += `<circle class="pk ${p.cls}" r="${p.cls ? 6 : 4.5}" cx="${a.x + (b.x - a.x) * p.u}" cy="${a.y + (b.y - a.y) * p.u}"/>`;
      });
      S.pk = S.pk.filter((p) => !p.done);
      g.innerHTML = h;
      svg.querySelectorAll('.node').forEach((el) => {
        const id = el.dataset.id, st = S.nos[id];
        el.classList.toggle('comp', st === 'comp'); el.classList.toggle('isol', st === 'isol');
        el.classList.toggle('alerta', st === 'alerta' || !!(S.alertaNo && S.alertaNo.no === id && st !== 'isol'));
        el.classList.toggle('alvo', !!(S.alvo && S.alvo.no === id && st !== 'isol'));
      });
    } else if (!S.rodando) S.pk = [];
    requestAnimationFrame(anim);
  }

  /* ------------------------------ Render por aba ------------------------------ */
  let aba = 'arquitetura';
  const kpi = (l, v, c) => `<div class="kpi ${c || ''}"><small>${l}</small><b>${v}</b></div>`;
  const barras = (el, itens, max, cls) => { el.innerHTML = itens.map(([l, v, txt, c]) => `<div class="bar"><span>${esc(l)}</span><div class="t"><i class="${c || cls || ''}" style="width:${max ? Math.min(100, (v / max) * 100) : 0}%"></i></div><span class="mono">${txt != null ? txt : fmt.format(Math.round(v))}</span></div>`).join(''); };
  const sevTag = (s) => `<span class="sev ${s}">${{ critica: 'crítica', alta: 'alta', media: 'média', baixa: 'baixa' }[s] || s}</span>`;
  const abertos = () => S.alertas.filter((a) => a.st === 'novo').length;

  function rArquitetura() {
    const det = S.alertas.filter((a) => !a.benigno).length;
    $('kpis-geral').innerHTML = kpi('Requisições', fmt.format(S.reqTot * 40), 'blue') + kpi('Eventos no Kafka', fmt.format(Object.values(S.topicos).flat().reduce((a, b) => a + b, 0) * 40)) +
      kpi('Alertas abertos', abertos(), abertos() ? 'red' : 'green') + kpi('Detecções reais', det, 'amber');
    const sel = svg.querySelector('.node.sel'); if (sel) infoNo(sel.dataset.id);
  }
  function rTrafego() {
    const so = $('so-atk').checked;
    const lin = S.reqs.filter((r) => !so || r.atk).slice(0, 70);
    $('tb-req').innerHTML = '<tr><th>hora</th><th>origem</th><th>IP</th><th>método</th><th>rota</th><th>status</th><th>ms</th><th>aluno</th></tr>' +
      lin.map((r) => `<tr class="${r.atk ? 'atk' : ''}"><td class="mono">${relogio(r.t)}</td><td>${r.orig}</td><td class="mono">${r.ip}</td><td class="mono">${r.m}</td><td class="mono">${esc(r.rota)}</td><td class="mono">${r.st}</td><td class="mono">${r.ms}</td><td class="mono">${r.aluno}</td></tr>`).join('');
    const por = {}; const st = {};
    S.reqMin.forEach((x) => { por[x.svc] = (por[x.svc] || 0) + 1; st[x.st] = (st[x.st] || 0) + 1; });
    const mx = Math.max(1, ...Object.values(por));
    barras($('bars-svc'), Object.entries(por).sort((a, b) => b[1] - a[1]).map(([k, v]) => [N[k] ? N[k].l : k, v, fmt.format(v * 40)]), mx);
    const mx2 = Math.max(1, ...Object.values(st));
    barras($('bars-status'), Object.entries(st).sort().map(([k, v]) => [k, v, fmt.format(v * 40), +k >= 400 ? 'red' : '']), mx2);
  }
  function rEventos() {
    const tp = $('sel-topico').value; const parts = S.topicos[tp];
    $('parts').innerHTML = parts.map((v, i) => `<div class="part">partição ${i}<b>${fmt.format(v)}</b><small class="hint">offset</small></div>`).join('');
    const tot = Object.values(S.topicos).flat().reduce((a, b) => a + b, 0);
    barras($('bars-lag'), [['cep', tot - S.cons.cep, fmt.format(tot - S.cons.cep) + ' msg'], ['data-lake', tot - S.cons.lake, fmt.format(tot - S.cons.lake) + ' msg'], ['siem-forwarder', tot - S.cons.siem, fmt.format(Math.round(tot - S.cons.siem)) + ' msg', S.siemParado ? 'red' : '']], Math.max(50, tot - S.cons.siem));
    $('msgs').textContent = S.msgs[tp].slice(0, 12).join('\n') || '(sem mensagens; clique em Iniciar)';
    $('msg-info').textContent = tp;
    $('btn-parar-siem').textContent = S.siemParado ? 'Religar o encaminhador do SIEM' : 'Parar o encaminhador do SIEM';
  }
  function rTelemetria() {
    $('lst-fontes').innerHTML = FONTES.map((f) => `<label class="sw"><input type="checkbox" data-fonte="${f.id}" ${S.fontes[f.id] ? 'checked' : ''}><span class="d"><b>${esc(f.l)}</b><small>${esc(f.d)} · ${String(f.eps).replace('.', ',')} eventos/s</small></span>${REGRAS.filter((r) => r.f === f.id).map((r) => `<span class="tag ${S.regras[r.id] ? 'info' : ''}">${r.id}</span>`).join(' ')}</label>`).join('');
    const ligadas = FONTES.filter((f) => S.fontes[f.id]);
    const gb = ligadas.reduce((a, f) => a + f.eps * GB_POR_EPS_DIA, 0);
    $('kpis-fontes').innerHTML = kpi('Fontes ligadas', ligadas.length + ' de ' + FONTES.length, 'blue') + kpi('Ingestão por dia', gb.toFixed(1).replace('.', ',') + ' GB') + kpi('Custo por mês', 'R$ ' + fmt.format(Math.round(gb * 30 * CUSTO_GB)), 'amber');
    barras($('bars-fontes'), FONTES.map((f) => [f.l.split(' ').slice(0, 3).join(' '), S.fontes[f.id] ? f.eps : 0, S.fontes[f.id] ? (f.eps * GB_POR_EPS_DIA).toFixed(2).replace('.', ',') + ' GB' : 'desligada']), 300);
    $('lst-fontes').querySelectorAll('input').forEach((i) => i.addEventListener('change', () => { S.fontes[i.dataset.fonte] = i.checked; render(); }));
  }
  function rCep() {
    $('lst-regras').innerHTML = REGRAS.map((r) => `<label class="sw"><input type="checkbox" data-regra="${r.id}" ${S.regras[r.id] ? 'checked' : ''}><span class="d"><b>${r.id} · ${esc(r.l)}</b><small>${sevTag(r.sev)} <span class="tag purple">${r.tec}</span> fonte: ${esc(F[r.f].l)} ${S.fontes[r.f] ? '' : '<span class="tag bad">fonte desligada</span>'}</small><div class="dsl">${esc(r.dsl)}</div></span></label>`).join('');
    $('cep-resumo').textContent = REGRAS.filter((r) => S.regras[r.id]).length + ' de ' + REGRAS.length + ' ativas';
    const mx = Math.max(1, ...Object.values(S.disparos));
    barras($('bars-regras'), REGRAS.map((r) => [r.id + ' ' + r.l.split(' ').slice(0, 2).join(' '), S.disparos[r.id] || 0]), mx);
    $('lst-regras').querySelectorAll('input').forEach((i) => i.addEventListener('change', () => { S.regras[i.dataset.regra] = i.checked; render(); }));
  }
  const ICO = { pend: '⏳', esperando: '🔎', det: '✅', parc: '🟡', miss: '❌', blk: '🛡️', canc: '⛔', imp: '💥' };
  const ROT = { pend: 'aguardando', esperando: 'regra correlacionando', det: 'detectado', parc: 'visto nos logs, sem alerta', miss: 'não detectado', blk: 'bloqueado pelo controle', canc: 'interrompido pela contenção', imp: 'impacto consumado' };
  function rCenarios() {
    $('cards-cen').innerHTML = CENARIOS.map((c) => `<div class="card ${S.cen && S.cen.id === c.id ? 'on' : ''}"><h3>${esc(c.l)}</h3><span class="tag">${c.aulas}</span><p>${esc(c.d)}</p><p>${[...new Set(c.passos.map((p) => p.tec))].map((t) => `<span class="tag purple">${t}</span>`).join(' ')}</p><button class="btn red sm" data-cen="${c.id}">Iniciar cenário</button></div>`).join('');
    $('cards-cen').querySelectorAll('[data-cen]').forEach((b) => b.addEventListener('click', () => iniciarCenario(b.dataset.cen)));
    $('v-cenarios').classList.toggle('rodando', !!S.cen);
    $('btn-repetir').style.display = S.cen ? '' : 'none';
    if (!S.cen) { $('cen-passos').innerHTML = '<li class="pend"><span></span><span></span><span>Escolha um cenário acima.</span><span></span></li>'; $('kpis-cen').innerHTML = ''; return; }
    const c = C[S.cen.id];
    $('cen-nome').textContent = c.l + ' · ' + c.aulas;
    $('cen-passos').innerHTML = S.cen.passos.map((p) => {
      const cls = { det: 'det', miss: 'miss', imp: 'miss', blk: 'blk', canc: 'canc', pend: 'pend' }[p.st] || '';
      return `<li class="${cls}"><span class="mono">${relogio(S.cen.ini + p.t).slice(0, 5)}</span><span class="ic">${ICO[p.st]}</span><span>${esc(p.txt)}<br><small class="hint">${p.tec} ${TEC_NOMES[p.tec] || ''} · Kill Chain: ${KC[p.tec] || '—'} · fonte: ${p.f ? esc(F[p.f].l) : 'nenhuma'} · regra: ${p.r ? p.r : 'nenhuma'}</small></span><span class="tag ${p.st === 'det' || p.st === 'blk' ? 'ok' : p.st === 'parc' ? 'warn' : p.st === 'miss' || p.st === 'imp' ? 'bad' : ''}">${ROT[p.st]}</span></li>`;
    }).join('');
    const ex = S.cen.passos.filter((p) => !['pend', 'canc'].includes(p.st));
    const det = ex.filter((p) => p.st === 'det').length;
    const mttd = S.alertas.filter((a) => a.passo && S.cen.passos.includes(a.passo));
    $('kpis-cen').innerHTML = kpi('Passos executados', ex.length + ' de ' + S.cen.passos.length) + kpi('Detectados', det, 'green') + kpi('Não detectados', ex.filter((p) => p.st === 'miss' || p.st === 'imp').length, 'red') + kpi('Vistos sem alerta', ex.filter((p) => p.st === 'parc').length, 'amber') +
      kpi('Primeiro alerta', mttd.length ? dur(mttd[mttd.length - 1].t - S.cen.ini) + ' após o início' : '—', 'amber');
  }
  let invId = null;
  function rSoc() {
    const reais = S.alertas.filter((a) => !a.benigno && a.mttd != null);
    const med = (arr) => (arr.length ? arr.reduce((a, b) => a + b, 0) / arr.length : null);
    const mttd = med(reais.map((a) => a.mttd)), mttr = med(S.alertas.filter((a) => a.mttr != null).map((a) => a.mttr));
    $('kpis-soc').innerHTML = kpi('Abertos', abertos(), abertos() ? 'red' : 'green') + kpi('Total de alertas', S.alertas.length) + kpi('Falsos positivos marcados', S.alertas.filter((a) => a.st === 'fp').length) +
      kpi('MTTD médio', mttd == null ? '—' : dur(mttd), 'amber') + kpi('MTTR médio', mttr == null ? '—' : dur(mttr), 'blue');
    $('tb-alertas').innerHTML = '<tr><th>id</th><th>hora</th><th>sev.</th><th>regra</th><th>host</th><th>descrição</th><th>estado</th><th></th></tr>' + (S.alertas.length ? S.alertas.map((a) => `<tr><td class="mono">${a.id}</td><td class="mono">${relogio(a.t)}</td><td>${sevTag(a.sev)}</td><td class="mono">${a.r}</td><td>${N[a.no] ? esc(N[a.no].l) : a.no}</td><td>${esc(a.txt)}</td><td>${{ antigo: '<span class="tag">execução anterior</span>', novo: '<span class="tag bad">novo</span>', contido: '<span class="tag ok">contido</span>', fp: '<span class="tag">falso positivo</span>' }[a.st]}</td><td style="white-space:nowrap"><button class="btn sm" data-inv="${a.id}">Investigar</button>${a.st === 'novo' ? ` <button class="btn sm blue" data-cont="${a.id}">Conter</button> <button class="btn sm" data-fp="${a.id}">Falso positivo</button>` : ''}</td></tr>`).join('') : '<tr><td colspan="8" class="hint">Nenhum alerta ainda. Inicie a simulação e um cenário.</td></tr>');
    $('tb-alertas').querySelectorAll('[data-inv]').forEach((b) => b.addEventListener('click', () => { invId = b.dataset.inv; rSoc(); }));
    $('tb-alertas').querySelectorAll('[data-cont]').forEach((b) => b.addEventListener('click', () => conter(b.dataset.cont)));
    $('tb-alertas').querySelectorAll('[data-fp]').forEach((b) => b.addEventListener('click', () => fp(b.dataset.fp)));
    const a = S.alertas.find((x) => x.id === invId);
    $('inv-id').textContent = a ? a.id : '';
    if (a) {
      const rel = S.cen && a.passo ? S.cen.passos.filter((p) => p.tExec != null && p.tExec <= a.t) : [];
      $('inv').innerHTML = `<p><b>${esc(R[a.r].l)}</b> ${sevTag(a.sev)} <span class="tag purple">${a.tec}</span></p><div class="dsl">${esc(R[a.r].dsl)}</div>` +
        (a.benigno ? '<div class="note">Contexto encontrado: comportamento conhecido e documentado. Marque como falso positivo e registre a exceção para a regra não disparar de novo.</div>' :
          `<p class="hint">Tempo do primeiro sinal até o alerta: <b>${dur(a.mttd)}</b>${a.mttr != null ? ' · até a contenção: <b>' + dur(a.mttr) + '</b>' : ''}.</p><p><b>Linha do tempo correlacionada</b></p><ul style="margin:0;padding-left:18px">${rel.map((p) => `<li class="hint">${relogio(p.tExec).slice(0, 5)} · ${esc(p.txt)} <span class="tag ${p.st === 'det' ? 'ok' : p.st === 'parc' ? 'warn' : 'bad'}">${ROT[p.st]}</span></li>`).join('')}</ul><div class="note">Passos marcados como "não detectado" aconteceram antes ou ao lado deste alerta sem gerar sinal: são candidatos a regra nova na reunião <em>purple</em>.</div>`);
    }
  }
  function rSuperficie() {
    const l = ATIVOS.slice();
    if ($('ord-risco').checked) l.sort((a, b) => risco(b) - risco(a));
    $('tb-ativos').innerHTML = '<tr><th>host</th><th>IP</th><th>serviço</th><th>inventário</th><th>WAF</th><th>achado</th><th>CVSS</th><th>EPSS</th><th>KEV</th><th>criticidade</th><th>risco</th><th>observação</th></tr>' +
      l.map((a) => `<tr class="${a.inv ? '' : 'atk'}"><td class="mono">${a.host}</td><td class="mono">${a.ip}</td><td>${a.svc}</td><td>${a.inv ? '<span class="tag ok">sim</span>' : '<span class="tag bad">não</span>'}</td><td>${a.waf ? 'sim' : 'não'}</td><td class="mono">${a.cve}</td><td class="mono">${a.cvss ? a.cvss.toFixed(1).replace('.', ',') : '—'}</td><td class="mono">${a.epss ? Math.round(a.epss * 100) + '%' : '—'}</td><td>${a.kev ? '<span class="tag bad">sim</span>' : '—'}</td><td>${'●'.repeat(a.crit)}</td><td class="mono"><b>${risco(a).toFixed(1).replace('.', ',')}</b></td><td>${esc(a.obs)}</td></tr>`).join('');
    $('sup-nota').innerHTML = 'Risco = CVSS/10 × (0,5 + EPSS) × 1,5 se estiver no KEV × criticidade × 0,8 se houver WAF (fórmula didática da disciplina). As probabilidades EPSS são ilustrativas: consulte o valor do dia no site do FIRST. O <code>promo-hml</code> está hospedado por terceiro e fica fora do escopo, mesmo aparecendo no levantamento.';
  }
  function estadoTec(tec) {
    const ps = CENARIOS.flatMap((c) => c.passos).filter((p) => p.tec === tec);
    const det = ps.some((p) => p.r && S.regras[p.r] && p.f && S.fontes[p.f]);
    if (det && S.testadas[tec]) return 'prov';
    if (det) return 'det';
    if (ps.some((p) => p.f && S.fontes[p.f])) return 'parc';
    return 'cego';
  }
  function rCobertura() {
    const tecs = [...new Set(CENARIOS.flatMap((c) => c.passos.map((p) => p.tec)))];
    const est = tecs.map((t) => [t, estadoTec(t)]);
    const n = (s) => est.filter((e) => e[1] === s).length;
    $('kpis-cob').innerHTML = kpi('Técnicas nos cenários', tecs.length) + kpi('Comprovadas', n('prov'), 'green') + kpi('Detectáveis sem teste', n('det'), 'blue') + kpi('Parciais', n('parc'), 'amber') + kpi('Cegas', n('cego'), 'red') +
      kpi('Cobertura com regra', Math.round(((n('prov') + n('det')) / tecs.length) * 100) + '%', 'amber');
    const ROTC = { prov: 'comprovada', det: 'detectável', parc: 'parcial', cego: 'cega' };
    $('matrix').innerHTML = est.map(([t, s]) => `<div class="cell ${s}"><b>${t}</b>${esc(TEC_NOMES[t] || '')}<br><small>${ROTC[s]} · regra: ${REGRAS.filter((r) => r.tec === t).map((r) => r.id + (S.regras[r.id] ? '' : ' (off)')).join(', ') || 'nenhuma'}</small></div>`).join('');
  }
  const RENDER = { arquitetura: rArquitetura, trafego: rTrafego, eventos: rEventos, telemetria: rTelemetria, cep: rCep, cenarios: rCenarios, soc: rSoc, superficie: rSuperficie, cobertura: rCobertura };
  let lastStatic = 0;
  function render() {
    $('relogio').textContent = relogio(S.t);
    $('badge-soc').textContent = abertos() || '';
    // abas com formulários só redesenham quando algo mudou, para não roubar o clique
    if ((aba === 'telemetria' || aba === 'cep') && S.rodando && performance.now() - lastStatic < 2000) return;
    lastStatic = performance.now();
    RENDER[aba] && RENDER[aba]();
  }
  function mostrar(nome) {
    if (!RENDER[nome]) nome = 'arquitetura';
    aba = nome;
    document.querySelectorAll('.view').forEach((v) => v.classList.toggle('on', v.id === 'v-' + nome));
    document.querySelectorAll('#abas a').forEach((a) => a.classList.toggle('on', a.getAttribute('href') === '#' + nome));
    lastStatic = 0; render();
  }

  /* ------------------------------ Eventos ------------------------------ */
  document.querySelectorAll('#abas a').forEach((a) => a.addEventListener('click', (e) => { e.preventDefault(); mostrar(a.getAttribute('href').slice(1)); history.replaceState(null, '', location.search + a.getAttribute('href')); }));
  $('btn-rodar').addEventListener('click', () => rodar(!S.rodando));
  $('btn-reiniciar').addEventListener('click', () => { rodar(false); novoEstado(); mostrar(aba); });
  $('velocidade').addEventListener('change', () => (S.vel = +$('velocidade').value));
  $('so-atk').addEventListener('change', render);
  $('sel-topico').addEventListener('change', render);
  $('ord-risco').addEventListener('change', render);
  $('btn-repetir').addEventListener('click', repetirCenario);
  $('btn-parar-siem').addEventListener('click', () => { S.siemParado = !S.siemParado; render(); });
  window.addEventListener('message', (e) => {
    const d = e.data || {};
    if (d.reiniciar) { rodar(false); novoEstado(); }
    if (d.repetir) repetirCenario();
    if (d.regras) Object.assign(S.regras, d.regras);
    if (d.fontes) Object.assign(S.fontes, d.fontes);
    if (d.simAba) mostrar(d.simAba);
    if (d.cenario && C[d.cenario] && (!S.cen || S.cen.id !== d.cenario) && d.autostart) iniciarCenario(d.cenario);
    else if (d.cenario && C[d.cenario] && !S.cen) { /* só destaca */ }
    if (d.rodar && !S.rodando) rodar(true);
    render();
  });

  novoEstado(); montarArq();
  const q = new URLSearchParams(location.search);
  mostrar(location.hash.slice(1) || 'arquitetura');
  if (q.get('cenario')) iniciarCenario(q.get('cenario'));
  requestAnimationFrame(anim);
  window.Simulador = { estado: () => S, iniciarCenario, repetirCenario, mostrar, rodar };
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
