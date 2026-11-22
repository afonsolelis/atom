# Entrega de trabalho — estudo de caso (PBL)

Disciplina: Red Team & Blue Team Strategies  
Professor-conteudista: Afonso Cesar Lelis Brandão  
Prazo de entrega: 02/12/2026  
Template de origem: `documentos/Instrumentos Avaliativos/TEMPLATE ENTREGA DE TRABALHO - nomedadisciplina.docx`

> Todos os itens são obrigatórios. O case existe para que o estudante entenda a aplicabilidade do conteúdo no mercado de trabalho.

> **Arquivo-mestre de produção.** As seções de Título a Roteiro do estudante formam a versão do estudante. A seção **Solução**, ao final, é exclusiva do professor tutor e deve ser **removida** antes de o case ser disponibilizado aos estudantes. Versão alinhada à **ementa oficial** de 18/11/2026 (`EMENTA.md`): as seis partes do entregável percorrem o ciclo completo de um exercício de simulação de adversário, do planejamento ao relatório final.

> **Nota ética.** Este trabalho é **consultivo e defensivo**. Você vai planejar um exercício **autorizado** e propor melhorias de detecção, de configuração e de resposta. Não se pede, nem será aceito, código de exploração, *malware* ou instruções passo a passo de ataque. Empresa, pessoas, grupo adversário e boletim de inteligência são **fictícios**; as técnicas citadas são as catalogadas publicamente na matriz MITRE ATT&CK.

---

## Título

**Do quase desastre ao programa contínuo: o Purple Team da Vitalis Diagnósticos**

---

## Desafio

> **O quê?** A **Vitalis Diagnósticos S.A.**, rede fictícia de medicina diagnóstica, sofreu em outubro de 2026 uma intrusão que começou com um *e-mail* de *phishing* e terminou com a **exfiltração de 1,8 GB de planilhas de faturamento com dados pessoais de pacientes**. O *ransomware* não chegou a ser executado: o invasor foi contido quando tentou desativar o EDR dos servidores. A diretoria entendeu que escapou por pouco e decidiu criar um **programa de Purple Team** para medir e melhorar, com evidências, a capacidade de detectar e responder a esse tipo de adversário.
>
> **Quem?** Você foi contratado(a) como **consultor(a) de segurança** pela nova CISO da Vitalis, Renata Albuquerque, que chegou à empresa depois do incidente. Ela precisa de um plano que una o Red Team (um fornecedor externo ainda a ser contratado), o SOC interno (4 pessoas, horário comercial) e o MSSP (provedor de serviços gerenciados de segurança que monitora alertas críticos 24×7).
>
> **Quando?** O incidente ocorreu entre **06 e 07/10/2026**. A CISO apresentará o programa ao **conselho de administração em 15/12/2026**, e o primeiro exercício de Purple Team está previsto para **fevereiro de 2027**.
>
> **Onde?** Sede administrativa e *datacenter* em Belo Horizonte (MG), **41 unidades de coleta** em MG, SP e GO, um laboratório central de processamento e o portal/aplicativo do paciente hospedado em nuvem pública.
>
> **Por quê?** A Vitalis trata **dados pessoais sensíveis** (dados de saúde, art. 5º, II, e art. 11 da LGPD) de cerca de **2,3 milhões de pacientes**. O incidente exigiu comunicação à ANPD e aos titulares, custou cerca de **R$ 2,4 milhões** e mostrou que as ferramentas estavam instaladas, mas não viam o ataque. O SOC tinha um alerta do EDR às 14h32 do primeiro dia e ninguém o analisou por quase 12 horas.

### Perfil da organização

| Item | Dado |
|---|---|
| Colaboradores | 2.300 (1.450 contas ativas no Active Directory, das quais 64 com privilégios administrativos) |
| Estações e servidores | 1.100 estações Windows; 180 servidores (130 Windows, 50 Linux) |
| Sistemas críticos | LIS (sistema de informação laboratorial) e banco de laudos *on-premises*; ERP de faturamento; portal e aplicativo do paciente em nuvem pública; API de integração com 27 operadoras de saúde |
| Ambiente sensível | 96 analisadores laboratoriais conectados ao LIS por uma rede segregada (equipamentos de fornecedor, sem agente de segurança) |
| Identidade | Active Directory sincronizado com o Microsoft Entra ID; MFA de um provedor terceiro (fictício, "AutentiQ"), integrado ao Entra ID e à VPN, com aprovação por notificação *push* simples (sem correspondência de número) |
| Acesso remoto | VPN SSL no *firewall* de borda, com autenticação pelo AD e MFA |
| Monitoramento | **Wazuh** em instalação própria (gerenciador, indexador e painel) como SIEM; EDR comercial separado; nenhum sensor de rede |
| Faturamento anual | R$ 940 milhões |
| Orçamento aprovado para o programa | **até R$ 1,2 milhão nos próximos 12 meses** |

### Linha do tempo do incidente (horário de Brasília)

| Data e hora | Evento | Registro existente |
|---|---|---|
| 06/10 09h12 | 37 colaboradores do faturamento e do atendimento recebem *e-mail* "Atualização do repasse de convênios — outubro" com *link* para uma página falsa de *login* corporativo. | Filtro de *e-mail* registrou a entrega; nenhum alerta. |
| 06/10 09h31 | Uma analista de faturamento digita usuário e senha na página falsa. | — |
| 06/10 09h33–09h41 | A analista recebe 14 notificações *push* de MFA, nega todas e **aprova a 15ª** por engano. | Registro de autenticação do console do AutentiQ (não enviado ao Wazuh); a entrada aparece no Entra ID como bem-sucedida. |
| 06/10 09h58 | Um novo dispositivo é registrado como método de MFA da conta. | Registro de auditoria do console do AutentiQ (não enviado ao Wazuh). |
| 06/10 11h20 | Conexão VPN SSL com a conta da analista, a partir de um endereço residencial brasileiro nunca visto. | *Log* local do *firewall* (7 dias); o Wazuh só recebe bloqueios. |
| 06/10 11h47–13h05 | Consultas em massa ao AD (usuários, grupos, computadores) e varredura de portas na rede interna. | Nenhum registro centralizado. |
| 06/10 14h10 | Sessão RDP da conta da analista para o servidor de arquivos FS-FAT01. | Evento 4624 (tipo 10) no Wazuh, em nível abaixo do limiar de alerta do SOC; nenhuma regra local. |
| 06/10 14h32 | Acesso à memória do processo LSASS em FS-FAT01. **EDR gera alerta de severidade média.** | Console do EDR; alertas médios são vistos só pelo SOC interno, em horário comercial. Não houve triagem. |
| 06/10 15h05 | Uso da conta de serviço `svc_backup` (senha não trocada desde 2021) para acessar compartilhamentos do faturamento. | Evento 4624 no Wazuh, abaixo do limiar de alerta; nenhuma regra local. |
| 06/10 16h40 | Compactação de planilhas de faturamento (nome, CPF, convênio e procedimentos de cerca de 212 mil pacientes). | Telemetria de processo no EDR, sem regra. |
| 06/10 17h02–17h51 | Envio de 1,8 GB para um serviço público de armazenamento em nuvem. | *Proxy* permite a categoria "armazenamento em nuvem"; *logs* do *proxy* não vão ao Wazuh. |
| 07/10 01h20 | Tentativa de desativar o EDR em 3 servidores, bloqueada pela proteção contra adulteração (*tamper protection*). **Alerta crítico.** | Console do EDR; MSSP recebe alerta crítico. |
| 07/10 02h05 | O MSSP confirma atividade maliciosa e liga para o plantonista da TI. | Registro do chamado. |
| 07/10 02h40 | Conta da analista e `svc_backup` desativadas no AD. | — |
| 07/10 04h10 | Sessões VPN derrubadas e FS-FAT01 isolado pelo EDR. **Contenção.** | — |
| 07/10 08h30 | Comitê de crise instalado; perícia contratada. | — |
| 09/10 | Comunicação preliminar à ANPD e início da comunicação aos titulares. | — |

### Inteligência de ameaças disponível

Em 20/10/2026, o centro setorial de compartilhamento de informações de saúde (fictício) **ISAC-Saúde BR** publicou o boletim **ISB-2026-041**, atribuindo pelo menos 7 intrusões em laboratórios e hospitais brasileiros em 2026 a afiliados do grupo de extorsão **"Cascavel"** (fictício). Comportamentos observados:

- acesso inicial por *phishing* com página falsa de *login* e fadiga de MFA, ou por *password spraying* contra VPN;
- registro de dispositivo próprio como método de MFA para persistência;
- reconhecimento do AD, *Kerberoasting* e roubo de credenciais da memória do LSASS;
- movimentação lateral por RDP com contas válidas;
- roubo de dados para serviços públicos de nuvem **antes** da criptografia (dupla extorsão);
- desativação de ferramentas de segurança, exclusão de cópias de sombra (*shadow copies*) e distribuição do *ransomware* por política de grupo (GPO);
- tempo médio de 3 a 6 dias entre o acesso inicial e a criptografia.

O boletim também traz 140 endereços IP e 60 *hashes* de arquivos associados às intrusões, com a ressalva de que a infraestrutura dos afiliados muda a cada campanha.

### Telemetria e ferramentas atuais

| Fonte / ferramenta | Situação atual | Retenção | Vai ao Wazuh? | Volume estimado se enviado ao Wazuh |
|---|---|---|---|---|
| Wazuh (SIEM) | Agentes nos 180 servidores; conjunto de regras padrão, sem regras locais (`local_rules.xml` vazio); ~1.900 alertas/dia de nível ≥ 7, ~92% falsos positivos | 90 dias | — | capacidade do indexador dimensionada para 60 GB/dia; uso atual de 40 GB/dia |
| Controladores de domínio (AD) | Auditoria padrão: 4624, 4625, 4740 coletados; sem 4768/4769 (Kerberos) e sem auditoria de acesso a objetos | 90 dias | Sim, parcial | +4 GB/dia para incluir Kerberos e alterações de grupos |
| Entra ID (entradas e auditoria) | Habilitado; sem licença de detecção de risco de identidade | 30 dias | Não | 2 GB/dia |
| Provedor de MFA (AutentiQ) | Registros de autenticação (*pushes* enviados, negados e aprovados) e de cadastro de dispositivos, só no console do fornecedor; exportação por API em JSON disponível | 30 dias | Não | 0,5 GB/dia |
| *Firewall* / VPN SSL | Tráfego e sessões VPN registrados localmente | 7 dias | Só bloqueios | 6 GB/dia (sessões VPN: 0,5 GB/dia) |
| EDR | 85% das estações e 60% dos servidores; *tamper protection* ativa; alertas críticos ao MSSP 24×7, médios ao SOC interno em horário comercial | 30 dias | Só alertas | — |
| Sysmon | Inexistente | — | — | 5 GB/dia (servidores Windows) |
| DNS interno | Sem coleta | — | Não | 8 GB/dia |
| *Proxy web* | Só na sede; categoria "armazenamento em nuvem" liberada | 15 dias | Não | 7 GB/dia |
| Filtro de *e-mail* em nuvem | Reescrita de URL e *sandbox* de anexos | 30 dias | Não | 1 GB/dia |
| Servidores de arquivos | Auditoria de acesso desabilitada | — | — | 3 GB/dia (só pastas sensíveis) |
| Nuvem pública (portal do paciente) | Trilha de auditoria da conta habilitada | 90 dias | Não | 1 GB/dia |
| Sensor de rede (Security Onion, com Zeek e Suricata) | Inexistente; avaliado em prova de conceito pela TI | — | — | armazenamento próprio, não consome a capacidade do Wazuh |
| Resposta a incidentes | Um *playbook* genérico em PDF (2023); sem SOAR; plantão de TI, não de segurança | — | — | — |

### Situação de configuração (varredura interna de 30/10/2026)

| Item | Situação encontrada |
|---|---|
| Atualizações | 34 dos 130 servidores Windows com atualizações críticas pendentes há mais de 60 dias, 3 deles com vulnerabilidade listada no catálogo KEV da CISA |
| RDP | Habilitado e acessível a partir de qualquer estação em todos os 130 servidores Windows e em 410 estações |
| Administrador local | Mesma senha em todas as 1.100 estações (sem Windows LAPS) |
| Contas de serviço | 18 contas; 11 com senha sem troca há mais de um ano; 4 delas (incluindo `svc_backup`) no grupo Domain Admins, todas com permissão de logon interativo |
| Contas administrativas | 64 contas com privilégio; 41 usadas também para *e-mail* e navegação |
| Protocolos legados | SMBv1 habilitado em 22 servidores; NTLMv1 aceito pelos controladores de domínio |
| Proteção de credenciais | Proteção LSA (*RunAsPPL*) e Credential Guard desabilitados em todos os servidores |
| Exposição à internet | 7 serviços publicados: VPN SSL, portal do paciente, API das operadoras, *webmail* e três sem responsável conhecido (interface de administração do *firewall* na porta 4443, FTP legado de envio de laudos às operadoras e um servidor de homologação do portal) |
| Rede dos analisadores | Segregada por VLAN, mas com regra "qualquer origem / qualquer porta" a partir do servidor do LIS e acesso remoto do fornecedor por VPN própria, sem MFA |

### Indicadores dos últimos 12 meses (incidentes confirmados)

| Nº | Tipo | Início → detecção (h) | Detecção → contenção (h) |
|---|---|---|---|
| 1 | Credencial capturada por *phishing* | 20 | 6 |
| 2 | *Malware* em estação de atendimento | 2 | 3 |
| 3 | Conta de fornecedor usada fora do horário | 52 | 14 |
| 4 | Credencial capturada por *phishing* | 30 | 8 |
| 5 | *Password spraying* na VPN | 6 | 4 |
| 6 | Incidente de 06–07/10/2026 | a calcular | a calcular |

### Custos de referência (estimativas do mercado fornecidas pela Vitalis)

| Item | Custo estimado (12 meses) |
|---|---|
| Ampliação da capacidade do indexador do Wazuh (nós e armazenamento), por bloco de 10 GB/dia | R$ 90 mil |
| Sensor de rede Security Onion no núcleo do *datacenter* e na rede dos analisadores (*hardware*, implantação e operação) | R$ 85 mil |
| MSSP também para alertas de severidade média, 24×7 | R$ 240 mil |
| Exercício de Red Team / Purple Team externo (por exercício, ~3 semanas) | R$ 180 mil |
| EDR em 100% dos servidores | R$ 70 mil |
| Chaves de segurança FIDO2 para 220 usuários privilegiados e financeiros | R$ 66 mil |
| Projeto de *hardening* (3 meses de consultoria: CIS Benchmarks, Windows LAPS, contas de serviço gerenciadas, servidores de salto para RDP) | R$ 150 mil |
| Contratação de um(a) engenheiro(a) de detecção (custo total) | R$ 260 mil |
| Licença de detecção de risco de identidade na nuvem | R$ 110 mil |

O comitê de riscos estima que um ataque de *ransomware* com parada das 41 unidades por 5 dias custaria **R$ 18 milhões**, e atribui hoje probabilidade anual de **20%** a esse cenário.

### Problema central

Como transformar o aprendizado do incidente em um **programa de Purple Team** que (1) planeje exercícios autorizados, com papéis e regras de engajamento claros e seguros para os pacientes; (2) emule o adversário que de fato ameaça a Vitalis, com base na inteligência de ameaças e na matriz ATT&CK; (3) feche as lacunas de telemetria e detecção no Wazuh, ou com um sensor Security Onion, dentro da capacidade e do orçamento; (4) reduza a superfície de ataque que o adversário explorou; (5) melhore a resposta a incidentes, preservando evidências; e (6) mostre ao conselho, com achados, riscos e métricas, que a capacidade defensiva está melhorando?

Não existe resposta única. Escolhas diferentes de técnicas, de modelo de exercício (aberto ou às cegas), de ferramentas, de prioridades de investimento e de metas são aceitas, **desde que justificadas com os dados do caso e com as fontes**.

---

## Fonte de pesquisa

Fontes primárias mínimas (todas de acesso gratuito):

1. MITRE CORPORATION. *MITRE ATT&CK®*. McLean: MITRE, [s. d.]. Disponível em: <https://attack.mitre.org/>. Acesso em: 22 nov. 2026. — Táticas, técnicas, fontes de dados e mitigações. Use também o *ATT&CK Navigator*: <https://mitre-attack.github.io/attack-navigator/>.
2. NATIONAL INSTITUTE OF STANDARDS AND TECHNOLOGY. *Computer security incident handling guide*. Gaithersburg: NIST, 2012. (NIST SP 800-61 Rev. 2). DOI: <https://doi.org/10.6028/NIST.SP.800-61r2>. Acesso em: 22 nov. 2026. — Obra da bibliografia complementar da disciplina; substituída em 2025 pela Rev. 3 (fonte 3), mas ainda a referência mais didática das fases do ciclo de resposta.
3. NATIONAL INSTITUTE OF STANDARDS AND TECHNOLOGY. *Incident response recommendations and considerations for cybersecurity risk management*: a CSF 2.0 community profile. Gaithersburg: NIST, 2025. (NIST SP 800-61 Rev. 3). DOI: <https://doi.org/10.6028/NIST.SP.800-61r3>. Acesso em: 22 nov. 2026.
4. NATIONAL INSTITUTE OF STANDARDS AND TECHNOLOGY. *Technical guide to information security testing and assessment*. Gaithersburg: NIST, 2008. (NIST SP 800-115). DOI: <https://doi.org/10.6028/NIST.SP.800-115>. Acesso em: 22 nov. 2026.
5. WAZUH. *Wazuh documentation*. [S. l.]: Wazuh, [s. d.]. Disponível em: <https://documentation.wazuh.com/>. Acesso em: 22 nov. 2026. — Ou, para quem optar pelo sensor de rede: SECURITY ONION SOLUTIONS. *Security Onion documentation*. [S. l.], [s. d.]. Disponível em: <https://docs.securityonion.net/>. Acesso em: 22 nov. 2026.
6. CENTER FOR INTERNET SECURITY. *CIS Critical Security Controls*: version 8.1. East Greenbush: CIS, 2024. Disponível em: <https://www.cisecurity.org/controls>. Acesso em: 22 nov. 2026. — Para configurações específicas, os *CIS Benchmarks*: <https://www.cisecurity.org/cis-benchmarks>.
7. BREZINSKI, D.; KILLALEA, T. *Guidelines for evidence collection and archiving*. [S. l.]: IETF, 2002. (RFC 3227). DOI: <https://doi.org/10.17487/RFC3227>. Acesso em: 22 nov. 2026.

Fontes complementares recomendadas:

8. SCYTHE. *Purple Team Exercise Framework (PTEF)*. [S. l.]: SCYTHE, [s. d.]. Disponível em: <https://github.com/scythe-io/purple-team-exercise-framework>. Acesso em: 22 nov. 2026.
9. SIGMAHQ. *Sigma: generic signature format for SIEM systems*. [S. l.]: SigmaHQ, [s. d.]. Disponível em: <https://github.com/SigmaHQ/sigma>. Acesso em: 22 nov. 2026.
10. MITRE CENTER FOR THREAT-INFORMED DEFENSE. *Adversary emulation library*. [S. l.], [s. d.]. Disponível em: <https://github.com/center-for-threat-informed-defense/adversary_emulation_library>. Acesso em: 22 nov. 2026.
11. CYBERSECURITY AND INFRASTRUCTURE SECURITY AGENCY. *#StopRansomware*. Washington, DC: CISA, [s. d.]. Disponível em: <https://www.cisa.gov/stopransomware>. Acesso em: 22 nov. 2026.
12. BRASIL. Lei nº 13.709, de 14 de agosto de 2018. Lei Geral de Proteção de Dados Pessoais (LGPD). Disponível em: <https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm>. Acesso em: 22 nov. 2026.
13. AUTORIDADE NACIONAL DE PROTEÇÃO DE DADOS. Resolução CD/ANPD nº 15, de 24 de abril de 2024. Aprova o Regulamento de Comunicação de Incidente de Segurança. *Diário Oficial da União*: seção 1, Brasília, DF, ed. 81, p. 114, 26 abr. 2024.
14. BEJTLICH, Richard. *The practice of network security monitoring*. San Francisco: No Starch Press, 2013. — Bibliografia complementar da disciplina; base para a arquitetura de monitoramento de rede.
15. SANDERS, Chris; SMITH, Jason. *Applied network security monitoring*. Waltham: Syngress, 2013. — Bibliografia complementar da disciplina.

As fontes 1 a 7 formam o conjunto mínimo obrigatório (na fonte 5, basta a documentação da ferramenta escolhida); 8 e 9 são fortemente recomendadas. O estudante pode acrescentar fontes primárias equivalentes (documentação de fornecedores de EDR, relatórios públicos de incidentes no setor de saúde), com referência completa conforme a ABNT.

**Aulas da disciplina a consultar:**

| Parte do trabalho | Aulas |
|---|---|
| 1. Planejamento, papéis e regras de engajamento | 1 (Red, Blue, White e Purple Team: papéis e objetivos), 2 (Regras de engajamento, escopo, autorização e aspectos legais) |
| 2. Plano de emulação no ATT&CK | 3 (MITRE ATT&CK: táticas, técnicas e planos de emulação), 4 (Inteligência de ameaças aplicada ao planejamento da operação), 5 a 8 (reconhecimento, acesso inicial, escalada, movimentação lateral, persistência e evasão: o que cada técnica faz e o rastro que deixa) |
| 3. Telemetria e detecção | 9 (Arquitetura de monitoramento: logs, SIEM e telemetria de endpoints), 10 (Detecção baseada em assinaturas, comportamento e regras), 11 (Caça a ameaças: hipóteses, consultas e análise de anomalias) |
| 4. *Hardening* e superfície de ataque | 12 (*Hardening* de sistemas e redução da superfície de ataque), 6 (priorização de vulnerabilidades com CVSS, EPSS e KEV) |
| 5. Resposta, evidências e linha do tempo | 13 (Ciclo de resposta a incidentes), 14 (Coleta de evidências e linha do tempo do incidente) |
| 6. Relatório final e programa | 15 (Exercícios *purple team*: validação de detecções contra técnicas emuladas), 16 (Relatório final: achados, riscos, recomendações e métricas de melhoria) |

---

## Entregável e distribuição da pontuação

**Formato:** um **relatório técnico em PDF**, de **15 a 20 páginas** (sem contar capa, referências e anexos), fonte 11 ou 12, com referências ABNT, acompanhado de **um arquivo JSON de *layer* do *ATT&CK Navigator*** (obrigatório, parte 2). O relatório segue a ordem do ciclo de um exercício de simulação de adversário.

**Estrutura e pontuação:**

| Parte | Conteúdo mínimo | Peso |
|---|---|---|
| 1. Planejamento e regras de engajamento | Objetivo do programa e do primeiro exercício; **papéis e responsabilidades de Red, Blue, White e Purple Team** com nomes de áreas da Vitalis e do fornecedor; modelo do exercício (aberto, às cegas ou híbrido); escopo e exclusões; janelas; técnicas proibidas; tratamento de dados sob a LGPD; critérios de parada e desconflito; autorização formal e base legal | 15% |
| 2. Plano de emulação no ATT&CK | Perfil do adversário extraído do boletim ISB-2026-041 (níveis estratégico, operacional e tático da inteligência); **8 a 10 técnicas ATT&CK** (ID, nome, tática), cada uma justificada pelo incidente e/ou pelo boletim; sequência do acesso inicial ao impacto simulado; critério de sucesso e telemetria esperada por técnica; **layer do Navigator** com o plano e a cobertura atual (figura no PDF + JSON anexo) | 20% |
| 3. Telemetria e detecção com Wazuh ou Security Onion | Matriz técnica × fonte de dados × situação atual (detectada, parcial, nenhuma) e cálculo da cobertura; arquitetura de coleta proposta dentro da capacidade do indexador; pelo menos **4 detecções** (lógica, fonte, falsos positivos esperados, técnica coberta), sendo **ao menos uma escrita como regra do Wazuh (XML) ou como regra Sigma/Suricata para o Security Onion**; pelo menos **1 hipótese de caça a ameaças** com a consulta correspondente | 20% |
| 4. *Hardening* e redução da superfície de ataque | Pelo menos **6 medidas** priorizadas a partir da varredura de 30/10, cada uma ligada à técnica ATT&CK que dificulta e a um controle do CIS Controls v8.1 ou a um CIS Benchmark; tratamento dos serviços expostos sem responsável e da rede dos analisadores; indicadores de superfície antes e depois | 10% |
| 5. Resposta a incidentes, evidências e linha do tempo | Linha do tempo reconstruída com fonte e evidência de cada evento, classificada nas fases do NIST SP 800-61 Rev. 2 e relacionada às funções do CSF 2.0 (Rev. 3); análise crítica da contenção; plano de preservação de evidências (ordem de volatilidade, cadeia de custódia, *hash*, retenção); linha de base de MTTD e MTTR; melhorias do *playbook*, incluindo a comunicação à ANPD | 15% |
| 6. Relatório final: achados, riscos, recomendações e métricas | Achados priorizados em matriz de risco; recomendações com responsável, prazo e custo; metas de 6 e 12 meses (cobertura validada, MTTD, MTTR, superfície); ciclo do programa com reteste e *layer* do Navigator antes/depois; alocação do orçamento de R$ 1,2 milhão; **sumário executivo de até 1 página** para o conselho | 15% |
| 7. Qualidade formal | Clareza, coerência entre as partes, uso correto de fontes e ABNT | 5% |
| **Total** | | **100%** |

---

## Roteiro do estudante

### 1. Leia o caso como um investigador

- Releia a linha do tempo e marque, para cada linha, **qual técnica ATT&CK** ela representa e **se havia registro** que permitiria detectá-la.
- Separe o que é **fato do caso** (horários, volumes, ferramentas) do que será **premissa sua** (por exemplo, o momento que você considera "início do ataque" para calcular o MTTD). Premissas devem ser declaradas no relatório.
- Anote os números que vão sustentar seus argumentos: 14 *pushes* negados, 11h33 entre o alerta do LSASS e a confirmação pelo MSSP, 1,8 GB exfiltrados, 1.900 alertas/dia com 92% de falsos positivos, 40 de 60 GB/dia de capacidade do Wazuh, 7 serviços expostos, R$ 1,2 milhão de orçamento.

### 2. Planeje o exercício e escreva as regras de engajamento (Parte 1)

- Use as Aulas 1 e 2 e o NIST SP 800-115. Diga quem é o Red Team, quem é o Blue Team, quem compõe o White Team (a célula de controle que arbitra o exercício) e como a função Purple Team vai conectar os dois lados.
- Decida e justifique o modelo: **aberto** (as equipes trabalham juntas, técnica a técnica), **às cegas** (o SOC não sabe) ou **híbrido**.
- Pense na segurança do paciente: o que **não pode** ser tocado (analisadores, LIS em produção?) e em que horários.
- Pense na LGPD: o exercício não pode criar um novo vazamento. Como provar a exfiltração sem tirar dados reais da empresa?
- Defina quem assina a autorização, quando o exercício para e como distinguir o exercício de um ataque real.

### 3. Monte o plano de emulação (Parte 2)

- Leia o boletim ISB-2026-041 separando o que é informação **estratégica** (quem ataca o setor e por quê), **operacional** (como as campanhas acontecem) e **tática** (TTPs e indicadores). Explique por que os 140 IPs e 60 *hashes* do boletim pouco ajudam a planejar a emulação.
- Escolha **8 a 10 técnicas** no site do ATT&CK. Bons critérios: apareceram no incidente, aparecem no boletim, têm alto impacto nos ativos da Vitalis ou são lacunas prováveis da defesa. Explique por que deixou outras de fora.
- Organize as técnicas em sequência, do acesso inicial ao impacto **simulado**. Para cada uma, escreva o critério de sucesso e a telemetria que o Blue Team deveria ver.
- No *ATT&CK Navigator*, crie uma *layer* com as técnicas do plano, use a pontuação ou as cores para indicar a cobertura atual e registre nos comentários a justificativa de cada técnica. Exporte o JSON e inclua a figura no PDF.

### 4. Mapeie telemetria e proponha detecções (Parte 3)

- Monte uma matriz com as suas técnicas nas linhas e, nas colunas: fonte de dados necessária, fonte existente na Vitalis, regra existente, classificação (detectada, parcial, nenhuma). Declare o critério e calcule a **cobertura atual** em porcentagem.
- Desenhe a arquitetura de coleta: o que entra no Wazuh, o que vai para um sensor Security Onion (se você optar por ele) e o que cabe nos **20 GB/dia livres** do indexador. O que exige ampliar a capacidade?
- Para cada detecção, descreva técnica coberta, fonte, lógica em linguagem natural, limiar, falsos positivos esperados e ação do analista. Escreva pelo menos uma como regra do Wazuh ou como regra Sigma/Suricata.
- Formule uma hipótese de caça (Aula 11) a partir do boletim e escreva a consulta que a testaria.

### 5. Reduza a superfície de ataque (Parte 4)

- Leia a tabela da varredura de 30/10 e pergunte, item a item: que técnica do incidente ou do boletim essa configuração facilitou?
- Escolha pelo menos 6 medidas, ordene por risco e esforço e associe cada uma a um controle do CIS Controls ou a um CIS Benchmark.
- Decida o que fazer com os três serviços expostos sem responsável e com a rede dos analisadores, que não aceita agente.
- Defina indicadores que mostrem a superfície diminuindo (por exemplo, serviços expostos, servidores com RDP aberto, contas privilegiadas).

### 6. Reconstrua a resposta (Parte 5)

- Reescreva a linha do tempo com a fonte e a evidência de cada evento e classifique os eventos nas fases do NIST SP 800-61 Rev. 2. Relacione-as às funções do CSF 2.0 usadas na Rev. 3.
- Avalie a contenção: o que foi feito às 02h40 bastava? O que ficou de fora da erradicação?
- Verifique a retenção de cada fonte: que evidências do incidente se perderiam se ninguém as preservasse a tempo? Descreva a ordem de volatilidade, a cadeia de custódia e o uso de *hash*.
- Calcule a **linha de base**: MTTD e MTTR médios dos 6 incidentes, e a mediana, comparando-a com a média.
- Revise o *playbook*: quem é acionado, em quanto tempo, que ações de contenção podem ser feitas sem esperar aprovação, quando acionar o DPO e o jurídico (prazo de comunicação à ANPD). Lembre-se do que falhou: o alerta existia, mas ninguém olhou.

### 7. Escreva o relatório final e o sumário executivo (Parte 6)

- Transforme o que você encontrou em **achados** (fato, evidência, técnica, impacto), classifique-os numa matriz de risco e escreva recomendações com responsável, prazo e custo.
- Defina metas para 6 e 12 meses e diga **como** serão medidas nos exercícios (reteste, *layer* do Navigator antes/depois).
- Mostre como o orçamento de R$ 1,2 milhão é distribuído e qual risco ele reduz.
- Escreva uma página para o conselho, sem siglas não explicadas: comece pela recomendação e mostre o risco em reais, o investimento, as metas e as decisões que o conselho precisa tomar.

### 8. Revise antes de enviar

- Cada técnica do plano aparece na matriz de cobertura e na *layer*? Cada lacuna crítica tem uma detecção, uma medida de *hardening* ou uma justificativa para não ter? As metas medem o que as detecções prometem melhorar? O orçamento fecha?
- Confira as referências ABNT e os termos estrangeiros em itálico.

Boa entrega!

---

## Solução

> Removida antes de o case ser disponibilizado ao aluno; vai para o professor tutor corrigir.

> **Orientação geral ao tutor.** O caso admite várias soluções. Os valores abaixo são uma **resposta de referência**; aceite escolhas diferentes quando forem coerentes com os dados do caso, justificadas e consistentes entre as partes. Desconte quando o estudante incluir código de exploração ou instruções operacionais de ataque (fora do escopo e contrário à nota ética).

### Parte 1 — Planejamento e regras de engajamento (elementos esperados)

**Papéis (referência):**

| Papel | Quem, na Vitalis | Responsabilidade no exercício |
|---|---|---|
| Red Team | Fornecedor externo contratado | Emular as técnicas do plano dentro do escopo, registrar cada ação com horário e evidência, interromper ao primeiro critério de parada |
| Blue Team | SOC interno, MSSP e, no programa, o(a) engenheiro(a) de detecção | Detectar, triar e responder como faria num incidente real; registrar o que viu e quando |
| White Team (célula de controle) | CISO (coordenação), CIO ou diretor de TI, DPO, jurídico, representante da diretoria clínica e de operações, líder do fornecedor | Aprovar o plano, arbitrar dúvidas de escopo, fazer o desconflito, acionar a parada, validar os resultados |
| Purple Team | Função de facilitação, não uma terceira equipe: em geral o(a) engenheiro(a) de detecção com o líder do Red Team | Conduzir as sessões técnica a técnica, comparar o que foi emulado com o que foi visto e transformar as diferenças em detecções e reteste |

- **Objetivo:** validar detecção e resposta à cadeia "Cascavel" até a exfiltração simulada e a tentativa de desativar defesas; medir MTTD/MTTR por técnica.
- **Modelo:** qualquer modelo justificado. Referência: híbrido — fase 1 **aberta** (técnica a técnica, conforme o PTEF, para construir detecções) e, após 3 a 6 meses, fase 2 **às cegas** para medir MTTD/MTTR reais do SOC e do MSSP. No modelo às cegas, SOC e MSSP não participam da célula branca; no aberto, participam das sessões.
- **Escopo:** AD, estações e servidores Windows corporativos, VPN, Entra ID, configuração do AutentiQ do lado da Vitalis (a plataforma do fornecedor só com autorização dele), servidores de arquivos, *proxy*; *phishing* simulado para grupos definidos.
- **Exclusões esperadas:** analisadores laboratoriais e sua rede; LIS e banco de laudos em produção (no máximo, testes passivos ou em homologação); portal do paciente em nuvem (salvo autorização específica e respeito às regras do provedor); sistemas de terceiros e operadoras; negação de serviço; criptografia ou exclusão de dados reais; desativação real de EDR em produção sem acordo da célula branca.
- **Janelas:** evitar o pico de coletas (cerca de 6h–10h) e fechamentos de faturamento; execução em horário acordado, com plantão técnico disponível.
- **LGPD:** princípio da necessidade; uso de **arquivos-isca sintéticos** (dados fictícios com marcadores) para simular a exfiltração; proibição de copiar dados reais de pacientes; destino de exfiltração controlado pelo próprio Red Team; registro e descarte seguro de evidências; cláusula de confidencialidade e acordo de tratamento de dados com o fornecedor; DPO na célula branca. O *phishing* simulado não deve usar temas que causem angústia (por exemplo, "resultado de exame alterado") e precisa de alinhamento com RH e jurídico; os resultados individuais não devem ser usados para punição.
- **Critérios de parada:** qualquer impacto em atendimento a pacientes ou nos analisadores; degradação de sistema crítico; detecção de um **adversário real** durante o exercício; acesso inesperado a dados sensíveis reais; violação de escopo; pedido de qualquer membro da célula branca. Deve haver palavra-código e procedimento para diferenciar exercício de incidente real (desconflito): o SOC que vê um alerta consulta a célula branca, que confirma se a origem é o Red Team.
- **Autorização formal:** assinada por quem tem autoridade sobre os ativos (por exemplo, diretor-presidente ou CIO e CISO), com período, escopo, contatos de emergência e carta que o operador pode apresentar se abordado. Menção ao art. 154-A do Código Penal (incluído pela Lei nº 12.737/2012) é esperada: a autorização expressa do titular é o que separa o exercício do crime.

### Parte 2 — Plano de emulação no ATT&CK (resposta de referência)

**Leitura do boletim:** estratégica — grupo de extorsão com motivação financeira que mira saúde no Brasil, com dupla extorsão; operacional — campanhas com *phishing* de credenciais e fadiga de MFA, de 3 a 6 dias até a criptografia; tática — as TTPs listadas e os indicadores. Os 140 IPs e 60 *hashes* servem para bloqueio e busca retroativa, mas estão na base da Pirâmide da Dor e mudam a cada campanha; um plano de emulação se apoia nas **TTPs**, que são o que o adversário repete. Aceitar outras fronteiras entre os níveis quando o critério estiver declarado.

Adversário: afiliado de *ransomware* com dupla extorsão (perfil "Cascavel"), motivação financeira, foco em saúde, que prefere contas válidas e ferramentas nativas a *malware* sofisticado.

| Ordem | Tática | Técnica | Justificativa no caso |
|---|---|---|---|
| 1 | *Initial Access* | T1566.002 *Phishing: Spearphishing Link* | *E-mail* de 06/10 09h12; boletim |
| 2 | *Credential Access* | T1621 *Multi-Factor Authentication Request Generation* | 14 *pushes* negados e 15º aprovado |
| 3 | *Persistence* | T1098.005 *Account Manipulation: Device Registration* | Novo dispositivo de MFA às 09h58; boletim |
| 4 | *Initial Access* / *Persistence* / *Stealth* | T1133 *External Remote Services* + T1078 *Valid Accounts* (inclui T1078.002 *Domain Accounts*) | VPN SSL com conta legítima às 11h20; uso de `svc_backup` às 15h05 |
| 5 | *Discovery* | T1087.002 *Account Discovery: Domain Account* (ou T1046 *Network Service Discovery*) | Consultas em massa ao AD; varredura interna |
| 6 | *Credential Access* | T1003.001 *OS Credential Dumping: LSASS Memory* | Alerta do EDR às 14h32 |
| 7 | *Lateral Movement* | T1021.001 *Remote Services: Remote Desktop Protocol* | RDP para FS-FAT01 |
| 8 | *Collection* | T1560.001 *Archive Collected Data: Archive via Utility* (ou T1039 *Data from Network Shared Drive*) | Compactação às 16h40 |
| 9 | *Exfiltration* | T1567.002 *Exfiltration Over Web Service: Exfiltration to Cloud Storage* | 1,8 GB às 17h02–17h51 |
| 10 | *Defense Impairment* | T1685 *Disable or Modify Tools* (antiga T1562.001, renumerada no ATT&CK v19) | Tentativa às 01h20 |

Aceitar IDs e nomes de táticas da versão anterior da matriz (por exemplo, T1562.001 em *Defense Evasion*) quando o estudante indicar a versão usada. Alternativas aceitáveis e bem justificáveis pelo boletim: T1110.003 *Password Spraying*, T1558.003 *Kerberoasting*, T1490 *Inhibit System Recovery*, T1484.001 *Group Policy Modification*, T1486 *Data Encrypted for Impact* (esta última deve aparecer como **impacto simulado**, nunca executado). Um bom trabalho explica que incluir técnicas do boletim que **não** ocorreram no incidente testa o que o adversário faria nos próximos passos (3 a 6 dias até a criptografia).

**Critério de sucesso e telemetria esperada (exemplo para a técnica 2):** o Red Team gera uma sequência de *pushes* contra uma conta de teste criada para o exercício; sucesso do Blue Team = alerta no Wazuh em até 15 minutos e contato com o "usuário" antes da aprovação. Telemetria esperada: registros de *push* negado no AutentiQ, ingeridos no Wazuh.

**Layer do Navigator esperada:** domínio Enterprise, versão da matriz declarada; as 8 a 10 técnicas do plano destacadas; pontuação ou cor por cobertura atual (por exemplo, 0 = nenhuma, 50 = parcial, 100 = detectada, coerente com a Parte 3); comentário em cada técnica com a evidência do caso. Um trabalho excelente cria uma segunda *layer* "meta" ou descreve como comparar as *layers* antes e depois do reteste (o Navigator permite criar uma *layer* a partir de outras com uma expressão de pontuação).

Sinais de baixa qualidade: lista de técnicas sem ID ou com ID errado; técnicas genéricas sem relação com o caso; ignorar o boletim; plano baseado só em IPs e *hashes*; ausência da *layer*; apresentar comandos de ataque.

### Parte 3 — Telemetria e detecção (resposta de referência)

Critério de referência: **detectada** = telemetria centralizada + regra + triagem em tempo útil; **parcial** = telemetria existe mas sem regra, ou regra existe sem triagem oportuna, ou só prevenção; **nenhuma** = sem telemetria utilizável.

| Técnica | Classificação atual | Motivo |
|---|---|---|
| T1566.002 | Parcial | Filtro de *e-mail* previne em parte; *logs* fora do Wazuh |
| T1621 | Nenhuma | Registros do AutentiQ fora do Wazuh; sem regra |
| T1098.005 | Nenhuma | Auditoria do AutentiQ fora do Wazuh |
| T1133 / T1078 | Nenhuma | Wazuh só recebe bloqueios da VPN; o 4624 da `svc_backup` chega ao Wazuh, mas abaixo do limiar e sem regra local (quem tratar T1078.002 em linha própria pode classificá-la como parcial) |
| T1087.002 | Nenhuma | Sem eventos de LDAP/Kerberos nem regra |
| T1003.001 | Parcial | EDR alerta, mas com severidade média: não vai ao MSSP e ficou sem triagem na fila do SOC interno, mesmo em horário comercial |
| T1021.001 | Parcial | 4624 tipo 10 no Wazuh, sem regra que gere alerta |
| T1560.001 | Parcial | Telemetria de processo no EDR, sem regra |
| T1567.002 | Nenhuma | *Proxy* fora do Wazuh e categoria liberada |
| T1685 | Detectada | *Tamper protection* + alerta crítico ao MSSP |

Com 10 técnicas: cobertura estrita = 1/10 = **10%**; cobertura ponderada (parcial = 0,5) = (1 + 4 × 0,5)/10 = **30%**. Outras classificações são aceitáveis se o critério estiver declarado e for aplicado de forma consistente.

**Arquitetura e capacidade:** há 20 GB/dia livres no indexador. Uma priorização coerente cabe neles, por exemplo: Entra ID (2) + AutentiQ (0,5) + sessões VPN (0,5) + Kerberos/grupos do AD (4) + Sysmon em servidores (5) + *proxy* (7) = **19 GB/dia**. DNS (8 GB/dia) e o tráfego completo do *firewall* (6 GB/dia) exigiriam ampliar o indexador (R$ 90 mil por 10 GB/dia) ou filtrar na origem. Solução elegante: um sensor **Security Onion** (Zeek e Suricata) no núcleo do *datacenter* e na rede dos analisadores registra DNS, conexões e transferências com armazenamento próprio, sem consumir a capacidade do Wazuh, e dá visibilidade **passiva** à rede que não aceita agente. Penalizar o trabalho que propõe "enviar tudo ao SIEM" sem considerar a capacidade.

**Detecções (exemplos aceitáveis):**

1. **Fadiga de MFA (T1621):** registros do AutentiQ exportados pela API em JSON e lidos pelo Wazuh; 6 ou mais negações de *push* para o mesmo usuário em 10 minutos geram alerta alto, e uma aprovação logo após a sequência deve gerar alerta crítico. Mitigação complementar: correspondência de número e FIDO2 para usuários críticos. Exemplo de regra local do Wazuh (simplificado):

```xml
<group name="local,autentiq,mfa,">
  <rule id="100200" level="3">
    <decoded_as>json</decoded_as>
    <field name="autentiq.evento">^push_negado$</field>
    <description>AutentiQ: push de MFA negado para $(autentiq.usuario)</description>
  </rule>

  <rule id="100201" level="12" frequency="6" timeframe="600">
    <if_matched_sid>100200</if_matched_sid>
    <same_field>autentiq.usuario</same_field>
    <description>Possível fadiga de MFA: 6 ou mais push negados para $(autentiq.usuario) em 10 minutos</description>
    <mitre>
      <id>T1621</id>
    </mitre>
  </rule>
</group>
```

2. **Registro de novo método de MFA (T1098.005)** no AutentiQ em até 24 h após entrada de risco ou de local incomum (correlacionando com o Entra ID e a VPN).
3. **VPN de origem inédita (T1133/T1078):** primeira conexão de um usuário a partir de ASN ou país nunca visto em 30 dias, ou "viagem impossível" entre entradas do Entra ID e da VPN.
4. **Acesso ao LSASS (T1003.001):** reclassificar o alerta do EDR para **alto** em servidores e enviá-lo ao MSSP 24×7; complementar com Sysmon (evento 10) no Wazuh ou, no Security Onion, com uma regra Sigma. Exemplo Sigma esperado (simplificado):

```yaml
title: Acesso suspeito à memória do LSASS em servidor
status: experimental
logsource:
  product: windows
  category: process_access
detection:
  selection:
    TargetImage|endswith: '\lsass.exe'
    GrantedAccess|contains:
      - '0x1010'
      - '0x1410'
  filter_legit:
    SourceImage|endswith:
      - '\MsMpEng.exe'
      - '\agente-edr.exe'
  condition: selection and not filter_legit
falsepositives:
  - Ferramentas de segurança e backup legítimas (ajustar lista de exceções)
level: high
tags:
  - attack.credential-access
  - attack.t1003.001
```

5. **RDP incomum (T1021.001):** logon tipo 10 de conta não administrativa em servidor, ou primeira ocorrência do par conta × servidor.
6. **Conta de serviço interativa (T1078.002):** `svc_*` com logon interativo ou RDP (4624 tipos 2 ou 10).
7. **Exfiltração para nuvem (T1567.002):** volume de envio por usuário/host acima de limiar (por exemplo, > 500 MB em 1 h) para a categoria "armazenamento em nuvem", nos *logs* do *proxy* ou no `conn.log` do Zeek.
8. **Compactação em servidor de arquivos (T1560.001)** por conta não administrativa, correlacionada com acesso a pastas sensíveis.

**Hipótese de caça (exemplo):** "Se afiliados do Cascavel usam *Kerberoasting*, haverá, nos 30 dias anteriores, contas de usuário comuns solicitando tíquetes de serviço (evento 4769) para muitos SPNs distintos, com criptografia RC4 (0x17), num intervalo curto." Consulta: agrupar 4769 por conta solicitante, contar SPNs distintos por hora e comparar com a linha de base de cada conta. Pré-requisito: habilitar a auditoria de Kerberos (+4 GB/dia, já previstos). Outras hipóteses aceitáveis: dispositivos de MFA registrados fora do horário; contas `svc_*` em VPN. A caça que confirmar um padrão deve virar regra.

### Parte 4 — *Hardening* e redução da superfície (resposta de referência)

| Prioridade | Medida | Técnica que dificulta | Referência |
|---|---|---|---|
| 1 | Correspondência de número no AutentiQ para todos e FIDO2 para os 220 usuários críticos | T1621, T1566.002 | CIS Control 6 (gestão de controle de acesso) |
| 2 | Contas de serviço: trocar a senha da `svc_backup` e das outras 10 sem troca, migrar para contas gerenciadas (gMSA), retirar as 4 do Domain Admins e negar logon interativo e por RDP via GPO | T1078.002 | CIS Control 5 (gestão de contas) |
| 3 | Restringir RDP aos servidores de salto, com MFA e NLA, bloqueando RDP entre estações e de estações para servidores | T1021.001 | CIS Control 4 e 12; CIS Benchmark do Windows Server |
| 4 | Ativar proteção LSA (*RunAsPPL*) e Credential Guard nos servidores | T1003.001 | CIS Benchmark do Windows Server |
| 5 | Windows LAPS nas 1.100 estações (senha única de administrador local) | T1078.003, T1021 | CIS Control 5 |
| 6 | Separar contas administrativas das de uso diário (41 contas) e reduzir as 64 contas privilegiadas | T1078 | CIS Control 5 e 6 |
| 7 | Aplicar as atualizações pendentes, começando pelos 3 servidores com vulnerabilidade no KEV | T1190, T1210 | CIS Control 7 |
| 8 | Desabilitar SMBv1 e NTLMv1 | T1557, T1550.002 | CIS Benchmark do Windows Server |
| 9 | Retirar da internet a interface de administração do *firewall* e o servidor de homologação; substituir o FTP legado por SFTP ou pela API das operadoras | T1190, T1133 | CIS Control 1, 4 e 12 |
| 10 | Bloquear a categoria "armazenamento em nuvem" no *proxy*, liberando só serviços corporativos | T1567.002 | CIS Control 9 e 13 |
| 11 | Rede dos analisadores: substituir a regra "qualquer porta" por lista de portas do LIS, exigir MFA no acesso do fornecedor e monitorar passivamente com o sensor de rede | T1133, T1021 | CIS Control 12, 13 e 15 |
| 12 | EDR em 100% dos servidores | T1003.001, T1685 | CIS Control 10 |

Os serviços expostos sem responsável devem ser tratados primeiro como problema de inventário (CIS Control 1): sem dono, ninguém corrige. Indicadores de superfície esperados: serviços expostos de 7 para 4 (−43%); servidores com RDP aberto a qualquer estação de 130 para 0; contas de serviço no Domain Admins de 4 para 0; estações com a mesma senha de administrador local de 1.100 para 0; servidores com atualização crítica pendente há mais de 60 dias de 34 para menos de 5. Aceitar outras escolhas e ordens bem justificadas; penalizar listas genéricas ("aplicar boas práticas") sem ligação com a varredura.

### Parte 5 — Resposta, evidências e linha do tempo (resposta de referência)

**Fases do NIST SP 800-61 Rev. 2 e funções do CSF 2.0 (Rev. 3):**

| Fase (Rev. 2) | Eventos do caso | Função do CSF 2.0 | Leitura crítica |
|---|---|---|---|
| Preparação | *Playbook* genérico de 2023; plantão de TI, não de segurança; alertas médios só em horário comercial | Governar, Identificar, Proteger | A falha começou antes do ataque |
| Detecção e análise | Alerta médio às 14h32 sem triagem; alerta crítico às 01h20; confirmação pelo MSSP às 02h05 | Detectar | O sinal existia 11h33 antes da confirmação |
| Contenção, erradicação e recuperação | Contas desativadas às 02h40; VPN derrubada e FS-FAT01 isolado às 04h10 | Responder, Recuperar | Desativar a conta no AD não encerra sessões VPN nem *tokens* já emitidos: as sessões seguiram ativas por 1h30 |
| Atividade pós-incidente | Comitê de crise; perícia; comunicação à ANPD | Melhoria contínua (Governar, Identificar) | Este trabalho é a lição aprendida |

**Erradicação incompleta esperada:** remover o dispositivo de MFA registrado às 09h58 (senão o invasor mantém a persistência); revogar sessões e *tokens* no Entra ID; trocar as senhas de todas as contas que fizeram logon em FS-FAT01 (credenciais podem ter saído do LSASS) e da `svc_backup`; verificar as outras contas de serviço no Domain Admins e, conforme a perícia, avaliar a troca dupla da senha da `krbtgt`.

**Evidências e retenção:** o *log* do *firewall*/VPN (7 dias) expiraria por volta de 13/10; o do *proxy* (15 dias), por volta de 21/10; AutentiQ, Entra ID e EDR (30 dias), por volta de 05/11. Por isso, a perícia contratada às 08h30 de 07/10 precisava exportar essas fontes nos primeiros dias, calcular o *hash* (por exemplo, SHA-256) de cada exportação e registrar a cadeia de custódia (quem coletou, quando, como, onde guardou, por quais mãos passou). Em FS-FAT01, isolado pela rede e ainda ligado, a ordem de volatilidade da RFC 3227 indica coletar memória antes do disco. Melhoria estrutural: ampliar a retenção das fontes críticas (mínimo de 90 dias) e centralizá-las no Wazuh ou no Security Onion.

**Linha de base do incidente 6:** contenção às 04h10 de 07/10, detecção confirmada às 02h05 de 07/10.

- Início = acesso à rede (11h20): MTTD = **14h45min (14,75 h)**.
- Início = credencial comprometida (09h31): MTTD = **16h34min (≈16,57 h)**.
- Detecção → contenção: **2h05min (≈2,08 h)**. Aceitar também 02h40 (desativação da conta, 0,58 h) se o estudante definir contenção assim, desde que discuta que ela não encerrou as sessões.
- Observação de qualidade: se a detecção fosse contada a partir do alerta de 14h32, o MTTD seria ~3,2 h; a diferença (11h33) mostra o custo da falta de triagem.

**Médias de 12 meses (início = 11h20):**

- MTTD = (20 + 2 + 52 + 30 + 6 + 14,75)/6 = 124,75/6 ≈ **20,8 h**; mediana = (14,75 + 20)/2 ≈ **17,4 h** (o incidente 3, com 52 h, puxa a média para cima).
- MTTR = (6 + 3 + 14 + 8 + 4 + 2,08)/6 = 37,08/6 ≈ **6,2 h**; mediana = (4 + 6)/2 = **5 h**.
- Com início = 09h31: MTTD ≈ 126,57/6 ≈ 21,1 h.

**Melhorias do *playbook*:** *playbooks* específicos (credencial comprometida/fadiga de MFA; suspeita de pré-*ransomware*; exfiltração de dados pessoais); matriz de severidade que trate roubo de credencial em servidor como crítico; SLA de triagem (por exemplo, alto em até 30 min, 24×7) com cobertura do MSSP para alertas médios/altos ou plantão de segurança; ações de contenção pré-autorizadas (desativar conta, revogar sessões e *tokens*, remover métodos de MFA, isolar host pelo EDR, derrubar VPN); coleta de evidências como etapa do *playbook*; acionamento do DPO e do jurídico para avaliar a comunicação à ANPD e aos titulares em até 3 dias úteis do conhecimento do incidente (art. 48 da LGPD e Resolução CD/ANPD nº 15/2024); lições aprendidas com prazo e responsável. Deve aparecer a conclusão central do caso: **o alerta de 14h32 existia; a falha foi de processo (severidade e triagem)**, além de técnica.

### Parte 6 — Relatório final: achados, riscos, recomendações e métricas

**Achados e matriz de risco (exemplo de referência, escala 1–5):**

| Achado | Evidência | Probabilidade | Impacto | Risco |
|---|---|---|---|---|
| MFA vulnerável a fadiga e a registro de dispositivo, sem telemetria | 14 *pushes* negados; dispositivo às 09h58; AutentiQ fora do Wazuh | 5 | 5 | Crítico |
| Alerta de roubo de credencial sem triagem fora do horário comercial | Alerta de 14h32 confirmado só às 02h05 | 4 | 5 | Crítico |
| Contas de serviço privilegiadas com senha antiga e logon interativo | `svc_backup` (2021) no Domain Admins | 4 | 5 | Crítico |
| Exfiltração para nuvem sem visibilidade nem bloqueio | 1,8 GB pelo *proxy*, *logs* fora do Wazuh | 4 | 4 | Alto |
| Serviços expostos sem responsável | 3 de 7 serviços publicados | 3 | 4 | Alto |
| Retenção curta de fontes críticas | VPN 7 dias, *proxy* 15 dias | 4 | 3 | Alto |

Cada achado deve trazer recomendação, responsável, prazo e custo, e a métrica que mostrará a correção.

**Metas de referência (aceitar outras coerentes):** 6 meses — cobertura ponderada ≥ 60% das técnicas priorizadas, **validada em exercício**; MTTD ≤ 4 h nos exercícios; MTTR ≤ 2 h; 100% dos alertas altos triados em até 30 min; serviços expostos sem responsável = 0. 12 meses — cobertura ≥ 80%; MTTD ≤ 1 h para técnicas de credencial e exfiltração; MTTR ≤ 1 h; taxa de falsos positivos < 70%. Bom trabalho explica que metas medidas em exercício às cegas valem mais que em exercício aberto e que MTTD/MTTR de incidentes reais têm amostra pequena.

**Ciclo do programa:** trimestral, por exemplo: planejamento com inteligência de ameaças → exercício aberto (PTEF) → engenharia de detecção e *hardening* → reteste em 30 dias → atualização da *layer* do Navigator (antes/depois) → *tabletop* semestral com a diretoria → exercício às cegas anual.

**Orçamento (exemplo que fecha em R$ 1,2 milhão):** engenheiro(a) de detecção R$ 260 mil + MSSP para alertas médios R$ 240 mil + 1 exercício externo R$ 180 mil (o reteste é feito pela equipe interna com o engenheiro de detecção) + projeto de *hardening* R$ 150 mil + sensor Security Onion R$ 85 mil + 1 bloco do indexador do Wazuh R$ 90 mil + EDR em 100% dos servidores R$ 70 mil + FIDO2 R$ 66 mil = **R$ 1,141 milhão**, com reserva de R$ 59 mil. Alternativas válidas: dois exercícios externos sem o sensor de rede ou sem o MSSP, trocando-o por plantão interno. Penalizar propostas que ultrapassam o orçamento sem pedir suplemento justificado.

**Valor para o negócio (Aula 16):** expectativa de perda anual atual = 0,20 × R$ 18 milhões = **R$ 3,6 milhões**. Se o estudante adotar como premissa a redução da probabilidade para, por exemplo, 8%, a nova expectativa é R$ 1,44 milhão, redução de R$ 2,16 milhões por ano contra R$ 1,2 milhão investido. A premissa de redução deve estar declarada como estimativa.

**Sumário executivo esperado:** recomendação na primeira linha; o incidente em uma frase com o custo (R$ 2,4 milhões) e o dado de que o alerta existia; risco em reais (R$ 3,6 milhões/ano); 3 a 5 decisões solicitadas (aprovar orçamento, aprovar a autorização do exercício, aprovar política de MFA resistente a *phishing*, aprovar o bloqueio de armazenamento em nuvem não corporativo, nomear responsáveis pelos serviços expostos); metas em linguagem simples (por exemplo, "detectar em menos de 1 hora em vez de 15"); próximos marcos (exercício em fevereiro de 2027, reporte trimestral). Penalizar jargão técnico sem explicação.

### Rubrica de correção

| Critério (peso) | Excelente (100%) | Bom (75%) | Suficiente (50%) | Insuficiente (0–25%) |
|---|---|---|---|---|
| 1. Planejamento e regras de engajamento (15%) | Quatro papéis bem definidos com áreas da Vitalis; todos os elementos da RoE (objetivo, modelo, escopo, exclusões clínicas, janelas, LGPD com dados sintéticos, parada, desconflito, autorização e base legal) | Faltam 1–2 elementos secundários ou o papel do Purple Team fica vago | Faltam elementos importantes (White Team, exclusões clínicas, LGPD ou parada) | RoE genérica, sem autorização formal ou que permite dano a pacientes ou a dados reais |
| 2. Plano de emulação no ATT&CK (20%) | Boletim lido nos três níveis; 8–10 técnicas com ID e tática corretos, justificadas e em sequência coerente; critério de sucesso e telemetria por técnica; *layer* do Navigator correta e coerente com a Parte 3 | Técnicas corretas e justificadas, com 1–2 justificativas fracas, sem critério de sucesso ou *layer* incompleta | Técnicas genéricas ou pouco ligadas ao caso; IDs com erros pontuais; *layer* ausente | Menos de 6 técnicas, IDs errados, plano baseado só em IoCs ou conteúdo ofensivo operacional |
| 3. Telemetria e detecção (20%) | Matriz completa com critério explícito e cobertura calculada; arquitetura dentro da capacidade do indexador; ≥ 4 detecções viáveis, uma como regra Wazuh ou Sigma/Suricata correta; hipótese de caça testável com consulta | Matriz e detecções corretas, arquitetura sem considerar a capacidade ou caça genérica | Matriz incompleta, detecções vagas ("monitorar o AD") ou sem regra escrita | Sem matriz ou menos de 2 detecções |
| 4. *Hardening* e superfície (10%) | ≥ 6 medidas priorizadas, cada uma ligada a técnica e a controle CIS; trata serviços expostos e rede dos analisadores; indicadores antes/depois | Medidas corretas, com ligação parcial a técnicas ou controles | Medidas genéricas, pouco ligadas à varredura | Ausente ou propõe medidas que afetam a segurança do paciente |
| 5. Resposta, evidências e linha do tempo (15%) | Linha do tempo com fontes nas fases do 800-61 e funções do CSF; critica a contenção e a erradicação; preservação de evidências com retenção, *hash* e custódia; MTTD/MTTR com premissas (média e mediana); *playbook* com SLA, contenção pré-autorizada e ANPD | Cálculos e *playbook* corretos, análise de evidências superficial | Erros de cálculo, fases mal classificadas ou *playbook* genérico | Sem linha de base nem melhoria de resposta |
| 6. Relatório final (15%) | Achados com evidência em matriz de risco; recomendações com responsável, prazo e custo; metas mensuráveis; ciclo com reteste e Navigator antes/depois; orçamento fecha; sumário executivo de 1 página em linguagem de negócio | Bom, com metas ou ciclo pouco detalhados, ou sumário com excesso técnico | Achados sem priorização, metas sem forma de medição ou sumário sem decisões claras | Sem achados, orçamento ignorado ou sumário ausente |
| 7. Qualidade formal (5%) | Texto claro, coerente entre as partes, ABNT correta, termos estrangeiros em itálico | Pequenas falhas de formatação | Falhas frequentes | Desorganizado, sem referências |

**Coerência transversal:** ao atribuir os níveis, verifique se as técnicas da Parte 2 aparecem na matriz da Parte 3 e na *layer*, se as lacunas críticas recebem detecção (Parte 3) ou medida de *hardening* (Parte 4), se a linha de base da Parte 5 é a mesma usada nas metas e se as metas da Parte 6 medem essas melhorias. Trabalhos com partes desconectadas não devem receber "Excelente" nos critérios 3, 5 e 6.
