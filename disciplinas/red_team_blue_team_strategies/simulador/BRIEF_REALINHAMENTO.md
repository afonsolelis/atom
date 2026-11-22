# Quinta etapa: realinhamento à ementa oficial (22/11/2026)

A coordenação enviou a ementa oficial em 18/11/2026. O material foi produzido sobre uma proposta provisória
e precisa ser reorganizado. **`EMENTA.md` (já atualizado) é a fonte de verdade** dos títulos das unidades e
das aulas, das tecnologias e da bibliografia.

## Novo mapa e reaproveitamento do material antigo

O material antigo continua acessível pelo git: `git show HEAD:disciplinas/red_team_blue_team_strategies/unidade_3/unidade_3.md`,
`git show HEAD:disciplinas/red_team_blue_team_strategies/unidade_3/slides/aula12.html` etc. **Leia sempre a versão
do HEAD** como fonte, porque outras equipes estão reescrevendo os arquivos de trabalho ao mesmo tempo.

| Nova aula | Título | Reaproveitar (HEAD) | Novo a escrever |
|---|---|---|---|
| 1 | Red, Blue, White e Purple Team: papéis e objetivos | antiga 1 (papéis), 3D das três cores | **White team** (árbitro, controle do exercício, *trusted agents*), ciclo de uma operação de Red Team |
| 2 | Regras de engajamento, escopo, autorização e aspectos legais | antiga 1 (ética, Lei 12.737), antiga 3 (RoE, caixa-preta/cinza/branca, tipos de avaliação) | documento de RoE completo, carta de autorização, *deconfliction*, LGPD |
| 3 | MITRE ATT&CK: táticas, técnicas e planos de emulação | antiga 2 (Kill Chain, ATT&CK), antiga 13 (emulação) | **plano de emulação** passo a passo, **ATT&CK Navigator** (*layers*) |
| 4 | Inteligência de ameaças aplicada ao planejamento da operação | antiga 11 (inteligência), antiga 5 (OSINT do adversário) | CTI estratégica/tática/operacional, perfil do Grupo Cobalto Austral, de relatório de ameaça a plano |
| 5 | Reconhecimento e enumeração de serviços e usuários | antigas 5 e 6 (OSINT, varredura, enumeração) | **Kali Linux** (terminal simulado), **Wireshark** vendo a varredura, enumeração de usuários |
| 6 | Exploração de vulnerabilidades e obtenção de acesso inicial | antiga 6 (CVE, CVSS, EPSS, KEV), antiga 7 (*phishing* como acesso inicial) | **Metasploit** (`search`, `info`, `check`, módulos *auxiliary*), vetores de acesso inicial (TA0001) |
| 7 | Escalada de privilégios, movimentação lateral e persistência | antiga 8 (pós-exploração, movimentação lateral, grafo 3D do AD) | escalada (TA0004) e persistência (TA0003) em nível conceitual, o que cada uma deixa de rastro |
| 8 | Evasão básica de defesas e limpeza de rastros em laboratório | antiga 10 (EDR, visão do defensor) | TA0005 Defense Evasion e T1070 Indicator Removal **como o defensor os enxerga**: log apagado (evento 1102), agente parado, *timestomp*; relatório de Red Team (da antiga 8) |
| 9 | Arquitetura de monitoramento: logs, SIEM e telemetria de endpoints | antiga 9 (telemetria, SIEM), antiga 4 (SOC, defesa em profundidade) | **Wazuh / Security Onion** como arquitetura de referência, Sysmon, **Wireshark/Zeek** (tráfego) |
| 10 | Detecção baseada em assinaturas, comportamento e regras | antiga 10 (engenharia de detecção, Sigma) | assinatura x comportamento x regra/correlação (YARA, Sigma, regras do Wazuh), falso positivo |
| 11 | Caça a ameaças: hipóteses, consultas e análise de anomalias | antiga 11 (*threat hunting*) | ciclo de caça com hipótese, consulta, *baseline* e anomalia (estatística simples) |
| 12 | *Hardening* de sistemas e redução da superfície de ataque | antiga 4 (NIST CSF, defesa em profundidade), antiga 6 (superfície externa) | **novo**: CIS Benchmarks, CIS Controls, menor privilégio, *patching*, redução de superfície (portas, serviços, contas) |
| 13 | Ciclo de resposta a incidentes: preparação, detecção, contenção, erradicação e recuperação | antiga 12 (resposta a incidentes) | ciclo NIST SP 800-61 (Rev. 2, da bibliografia, e Rev. 3), *playbooks*, comunicação à ANPD |
| 14 | Coleta de evidências e linha do tempo do incidente | antiga 12 (partes forenses) | **novo**: ordem de volatilidade (RFC 3227), cadeia de custódia, *hash*, *super timeline*, pcap no Wireshark |
| 15 | Exercícios *purple team*: validação de detecções contra técnicas emuladas | antigas 13, 14 e 15 (purple, cobertura, exercícios) | ciclo emular → observar → ajustar → retestar, *Navigator* antes/depois |
| 16 | Relatório final: achados, riscos, recomendações e métricas de melhoria | antiga 8 (relatório), antiga 14 (métricas), antiga 16 (programa contínuo) | estrutura de relatório técnico e executivo, matriz de risco, MTTD/MTTR, fechamento da disciplina |

Temas da proposta antiga que **saem como aula própria** mas podem aparecer como exemplo: engenharia social e
*phishing* (vira vetor de acesso inicial na 6), carreira e tendências (parágrafo curto na 16), CTF e *tabletop*
(citados na 15), NIST CSF (citado na 12).

## O que cada unidade entrega

1. `unidade_N/unidade_N.md` com a estrutura atual do template (ver `scripts/validar.py` e `README.md`, seção
   "Regras de produção"): título da unidade = título oficial; por aula: texto base de **700 a 1200 palavras**,
   **3 a 5 imagens** no formato `[Imagem N: ...]` já usado, pelo menos um exemplo numérico, Pontos-chave,
   "Referências da aula" (ABNT) e o roteiro. Aula 1 da unidade com "O que você verá nesta unidade"; Aula 3 com
   "Pausa para reflexão"; Aula 4 com "O que você verá na próxima unidade" (na 16, fechamento da disciplina).
   Quiz não avaliativo (2 questões) e Material complementar (4 seções, *Direto da fonte* com os livros da BV do
   `EMENTA.md`). **Só a Unidade 1** tem "Relação da disciplina com a atuação profissional", o roteiro do vídeo
   introdutório e a AAI.
2. `unidade_N/questoes_uniN.md`: **40 questões** (1–20 asserção-razão com `PORQUE` e as alternativas padrão;
   21–40 interpretação), **8 corretas por letra**, feedback para cada alternativa no formato atual. Reaproveite
   questões antigas quando o tema continuar na unidade, mas todas precisam bater com o texto base novo.
3. Os 4 decks `unidade_N/slides/aulaK.html` (a Unidade 1 também ajusta a `aula0.html`, que apresenta a
   disciplina, o mapa das 16 aulas e as ferramentas). Mantêm o arco "O problema de hoje na Rede Tatame" →
   laboratórios → "De volta ao problema". Regras de `README.md` (seção "Slides HTML e laboratórios") e de
   `scripts/validar_slides.py`:
   - **VS Code em tela cheia**, como se fosse programação local no computador do professor: todo `Labs.vscode`
     ocupa o slide inteiro, com `setup` (versão do interpretador, `.venv`, `pip install -r requirements.txt`
     com pacotes e versões reais do PyPI, conferência) e o roteiro escondido no botão "☰ Roteiro" / tecla G.
     Antes de cada VS Code, o slide "Antes do código: onde achar e como instalar o que o laboratório usa".
     Modelo: `unidade_1/slides/aula1.html`. O código precisa ser coerente e a saída mostrada precisa ser a
     que o código produziria de verdade (rode o Python localmente para conferir os números).
   - Pelo menos 4 laboratórios, com VS Code, uma simulação de programa (terminal, SIEM, navegador ou
     `Labs.register`), uma visualização (fluxo ou 3D) e um `Labs.plataforma` com passos que funcionam no
     simulador.
   - As ferramentas da ementa entram nas aulas indicadas em `EMENTA.md`: Kali como `Labs.terminal` com
     *prompt* `kali@lab-tatame`; Metasploit como sessão `msfconsole` simulada; Wireshark e Wazuh/Security Onion
     como `Labs.register` próprios ou `Labs.siem` com a aparência da ferramenta. Tudo contra os hosts fictícios
     de `simulador/APLICACAO.md`, dentro do escopo da carta de autorização do exercício.
   - **Limite de segurança**: descoberta de serviços (`nmap -sV`), enumeração, `search`/`info`/`check` e
     módulos `auxiliary/scanner` do Metasploit são permitidos; **nada** de *payload*, *shell* reverso, extração
     ou quebra de credenciais, código de exploração ou comandos de evasão/antiforense reais (o validador barra
     os mais comuns). Na Aula 8, a evasão e a limpeza de rastros aparecem pela técnica ATT&CK e pelo rastro que
     deixam na telemetria, com o laboratório no lado do defensor.
4. Roteiros "bonitinhos e organizados", no formato de `simulador/BRIEF_ROTEIRO.md`: abertura
   `Duração-alvo: 15 a 20 minutos. Deck: ... (X slides).`, um bloco por slide **na ordem exata do deck**, com
   tempos crescentes; laboratórios com Objetivo, Na tela (passos numerados com os rótulos reais), Fala,
   Atenção e Conclusão; indicações de produção entre colchetes.

## Regras gerais

- pt-BR acadêmico, claro e dialógico; termos estrangeiros em itálico; sem estilo de rede social (sem aforismo,
  sem travessão como conector, sem "não é X, é Y"). Fatos, números de normas, IDs ATT&CK e versões de pacotes
  precisam estar corretos; confira o que não souber.
- Nomes, hosts, IPs, pessoas e cenários só de `simulador/APLICACAO.md`.
- **Não edite** `assets/`, `simulador/`, `scripts/`, `index.html`, `EMENTA.md`, `README.md`, os instrumentos
  avaliativos nem arquivos de outras unidades. Se o simulador ou o `labs.js` precisar de algo, descreva no
  relatório. Não faça commit.
- O servidor local já está rodando: `http://127.0.0.1:8765/disciplinas/red_team_blue_team_strategies/`.
- Antes de terminar, rode e deixe passando, a partir da raiz da disciplina:
  `python scripts/validar.py` (a sua unidade precisa estar sem problemas; ignore os das outras),
  `python scripts/validar_slides.py aulaK ...` e `python scripts/auditar_layout.py aulaK ...`.
