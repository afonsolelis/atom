# Segunda rodada dos decks: plataforma única Rede Tatame

Decisão do professor: o módulo inteiro usa UMA aplicação fictícia, a plataforma distribuída da Rede Tatame
(rede de academias de jiu-jitsu), como alvo do Red Team e ambiente defendido pelo Blue Team.

Leia antes de editar:
- `simulador/APLICACAO.md`: fonte única de nomes, hosts, IPs, pessoas, adversário (Grupo Cobalto Austral) e cenários.
- `simulador/simulador.js`: abas (arquitetura, trafego, eventos, telemetria, cep, cenarios, soc, superficie,
  cobertura), regras R1–R13, fontes, cenários (phishing, recon, api-abuso, ransomware, catraca, exfiltracao).
- `assets/labs.js`, função `Labs.plataforma(sel, { aba, cenario, autostart, rodar, regras:{R5:true}, fontes:{cloud:true}, reiniciar })`.
- Modelo pronto: slide `<!-- 9b. PLATAFORMA REDE TATAME -->` em `unidade_1/slides/aula1.html`
  (`.lab-split plat`, área à esquerda `#lab-tatame`, roteiro "Faça" à direita, badge `lab-badge tatame`).

O que fazer em cada deck da sua unidade:
1. Trocar as empresas fictícias dos laboratórios e exemplos pela Rede Tatame, com os nomes de APLICACAO.md
   (hosts *.tatame.com.br, 203.0.113.x, 10.10.x sede, 10.40.x nuvem, SRV-AD-01, SRV-ARQ-01, SRV-ERP-01,
   NB-FIN-031, pessoas da tabela). Ajuste a narrativa (ex.: dados de alunos menores, biometria das catracas,
   pagamentos com a PagaFácil sempre fora do escopo) em vez de só renomear. Números que vêm do md da unidade
   continuam iguais; só o contexto muda. Se um caso do md (Pausa para reflexão, estudo de caso) cita outra
   organização, mantenha o caso do md nesse slide específico.
2. Incluir 1 ou 2 slides `Labs.plataforma` com roteiro "Faça" de 3–5 passos verificáveis no simulador,
   conforme o mapa abaixo. Cada passo tem de funcionar de verdade no simulador (teste).
3. Os outros labs (VS Code, terminal, SIEM, 3D etc.) continuam, agora com dados da Rede Tatame
   (ex.: logs com hosts da plataforma, scripts lendo tópicos `tatame.*`).
4. `deck.css` já corrige o callout dentro do cartão; `labs.css` já tem `min-width:0`; `labs.js` já corrige o dt
   negativo e mostra erros do build 3D. Pode remover os contornos locais que você criou para isso.
5. Regras de sempre: pt-BR sem estilo de rede social; sem comandos ofensivos; tudo fictício; não editar
   `assets/`, `simulador/` nem decks de outras unidades; não commitar. Se o simulador precisar de algo
   (cenário, regra, campo), descreva no relatório em vez de editar.
6. Rodar `python scripts/validar_slides.py aulaN...` (agora exige `Labs.plataforma`) e testar no Chrome headless
   (servidor em http://127.0.0.1:8765/disciplinas/red_team_blue_team_strategies/...), clicando nos passos do roteiro.

Mapa sugerido (aula → aba/cenário):
- 0 arquitetura (apresentar a plataforma e as abas) · 1 phishing (cenarios → soc; já feito no aula1, só adaptar o resto do deck)
- 2 ransomware visto pela Kill Chain/ATT&CK (cenarios, cobertura) · 3 superficie + recon (pentest x Red Team)
- 4 telemetria e soc, cenário catraca (defesa em profundidade, níveis do SOC)
- 5 recon + superficie · 6 superficie (priorização) + api-abuso · 7 phishing (campanha e métricas)
- 8 ransomware (movimentação lateral; ligar R5 e R13 e comparar)
- 9 telemetria + eventos (fontes, lag do encaminhador do SIEM), cenário catraca com fonte desligada e depois ligada
- 10 cep (regras, ligar R3 e testar api-abuso) · 11 exfiltracao com R8 desligada (hunt) e depois ligada
- 12 soc no ransomware (investigar, conter, MTTD/MTTR) · 13 cobertura antes/depois (purple, ciclo de reteste)
- 14 cobertura + soc (métricas, falso positivo do svc-backup) · 15 exercício completo ransomware como cyber range
- 16 cobertura geral + arquitetura (programa contínuo, roadmap a partir das técnicas cegas)
