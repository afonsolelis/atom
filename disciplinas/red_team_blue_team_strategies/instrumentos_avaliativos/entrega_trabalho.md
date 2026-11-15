# Entrega de trabalho — estudo de caso (PBL)

Disciplina: Red Team & Blue Team Strategies  
Professor-conteudista: Afonso Cesar Lelis Brandão  
Prazo de entrega: 02/12/2026  
Template de origem: `documentos/Instrumentos Avaliativos/TEMPLATE ENTREGA DE TRABALHO - nomedadisciplina.docx`

> Todos os itens são obrigatórios. O case existe para que o estudante entenda a aplicabilidade do conteúdo no mercado de trabalho.

> **Arquivo-mestre de produção.** As seções de Título a Roteiro do estudante formam a versão do estudante. A seção **Solução**, ao final, é exclusiva do professor tutor e deve ser **removida** antes de o case ser disponibilizado aos estudantes. Versão de trabalho baseada na **ementa proposta** (`EMENTA.md`); ajustar números de aulas se o plano de aprendizagem oficial alterar a ordem.

> **Nota ética.** Este trabalho é **consultivo e defensivo**. Você vai planejar um exercício **autorizado** e propor melhorias de detecção e resposta. Não se pede, nem será aceito, código de exploração, *malware* ou instruções passo a passo de ataque. Empresa, pessoas, grupo adversário e boletim de inteligência são **fictícios**; as técnicas citadas são as catalogadas publicamente na matriz MITRE ATT&CK.

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
| Identidade | Active Directory sincronizado com o Microsoft Entra ID; MFA por notificação *push* simples (sem correspondência de número) |
| Acesso remoto | VPN SSL no *firewall* de borda, com autenticação pelo AD e MFA |
| Faturamento anual | R$ 940 milhões |
| Orçamento aprovado para o programa | **até R$ 1,2 milhão nos próximos 12 meses** |

### Linha do tempo do incidente (horário de Brasília)

| Data e hora | Evento | Registro existente |
|---|---|---|
| 06/10 09h12 | 37 colaboradores do faturamento e do atendimento recebem *e-mail* "Atualização do repasse de convênios — outubro" com *link* para uma página falsa de *login* corporativo. | Filtro de *e-mail* registrou a entrega; nenhum alerta. |
| 06/10 09h31 | Uma analista de faturamento digita usuário e senha na página falsa. | — |
| 06/10 09h33–09h41 | A analista recebe 14 notificações *push* de MFA, nega todas e **aprova a 15ª** por engano. | Registros de entrada do Entra ID (não enviados ao SIEM). |
| 06/10 09h58 | Um novo dispositivo é registrado como método de MFA da conta. | Registro de auditoria do Entra ID (não enviado ao SIEM). |
| 06/10 11h20 | Conexão VPN SSL com a conta da analista, a partir de um endereço residencial brasileiro nunca visto. | *Log* local do *firewall* (7 dias); o SIEM só recebe bloqueios. |
| 06/10 11h47–13h05 | Consultas em massa ao AD (usuários, grupos, computadores) e varredura de portas na rede interna. | Nenhum registro centralizado. |
| 06/10 14h10 | Sessão RDP da conta da analista para o servidor de arquivos FS-FAT01. | Evento 4624 (tipo 10) no SIEM, sem regra associada. |
| 06/10 14h32 | Acesso à memória do processo LSASS em FS-FAT01. **EDR gera alerta de severidade média.** | Console do EDR; alertas médios são vistos só pelo SOC interno, em horário comercial. Não houve triagem. |
| 06/10 15h05 | Uso da conta de serviço `svc_backup` (senha não trocada desde 2021) para acessar compartilhamentos do faturamento. | Evento 4624 no SIEM, sem regra associada. |
| 06/10 16h40 | Compactação de planilhas de faturamento (nome, CPF, convênio e procedimentos de cerca de 212 mil pacientes). | Telemetria de processo no EDR, sem regra. |
| 06/10 17h02–17h51 | Envio de 1,8 GB para um serviço público de armazenamento em nuvem. | *Proxy* permite a categoria "armazenamento em nuvem"; *logs* do *proxy* não vão ao SIEM. |
| 07/10 01h20 | Tentativa de desativar o EDR em 3 servidores, bloqueada pela proteção contra adulteração (*tamper protection*). **Alerta crítico.** | Console do EDR; MSSP recebe alerta crítico. |
| 07/10 02h05 | O MSSP confirma atividade maliciosa e liga para o plantonista da TI. | Registro do chamado. |
| 07/10 02h40 | Conta da analista e `svc_backup` desativadas. | — |
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

### Telemetria e ferramentas atuais

| Fonte / ferramenta | Situação atual | Retenção | Vai ao SIEM? | Volume estimado se enviado ao SIEM |
|---|---|---|---|---|
| SIEM em nuvem | 45 regras ativas (38 padrão do fornecedor, nunca revisadas); ~1.900 alertas/dia, ~92% falsos positivos | 90 dias | — | licença de 60 GB/dia; uso atual de 40 GB/dia |
| Controladores de domínio (AD) | Auditoria padrão: 4624, 4625, 4740 coletados; sem 4768/4769 (Kerberos) e sem auditoria de acesso a objetos | 90 dias | Sim, parcial | +4 GB/dia para incluir Kerberos e alterações de grupos |
| Entra ID (entradas e auditoria) | Habilitado; sem licença de detecção de risco de identidade | 30 dias | Não | 2 GB/dia |
| *Firewall* / VPN SSL | Tráfego e sessões VPN registrados localmente | 7 dias | Só bloqueios | 6 GB/dia (sessões VPN: 0,5 GB/dia) |
| EDR | 85% das estações e 60% dos servidores; *tamper protection* ativa; alertas críticos ao MSSP 24×7, médios ao SOC interno em horário comercial | 30 dias | Só alertas | — |
| Sysmon | Inexistente | — | — | 5 GB/dia (servidores Windows) |
| DNS interno | Sem coleta | — | Não | 8 GB/dia |
| *Proxy web* | Só na sede; categoria "armazenamento em nuvem" liberada | 15 dias | Não | 7 GB/dia |
| Filtro de *e-mail* em nuvem | Reescrita de URL e *sandbox* de anexos | 30 dias | Não | 1 GB/dia |
| Servidores de arquivos | Auditoria de acesso desabilitada | — | — | 3 GB/dia (só pastas sensíveis) |
| Nuvem pública (portal do paciente) | Trilha de auditoria da conta habilitada | 90 dias | Não | 1 GB/dia |
| Resposta a incidentes | Um *playbook* genérico em PDF (2023); sem SOAR; plantão de TI, não de segurança | — | — | — |

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
| Ampliação da licença do SIEM, por bloco de 10 GB/dia | R$ 90 mil |
| MSSP também para alertas de severidade média, 24×7 | R$ 240 mil |
| Exercício de Red Team / Purple Team externo (por exercício, ~3 semanas) | R$ 180 mil |
| EDR em 100% dos servidores | R$ 70 mil |
| Chaves de segurança FIDO2 para 220 usuários privilegiados e financeiros | R$ 66 mil |
| Contratação de um(a) engenheiro(a) de detecção (custo total) | R$ 260 mil |
| Licença de detecção de risco de identidade na nuvem | R$ 110 mil |

O comitê de riscos estima que um ataque de *ransomware* com parada das 41 unidades por 5 dias custaria **R$ 18 milhões**, e atribui hoje probabilidade anual de **20%** a esse cenário.

### Problema central

Como transformar o aprendizado do incidente em um **programa de Purple Team** que (1) emule o adversário que de fato ameaça a Vitalis, (2) teste a defesa de forma ética, legal e segura para os pacientes, (3) feche as lacunas de telemetria, detecção e resposta dentro do orçamento e da licença do SIEM e (4) mostre ao conselho, com números, que a capacidade defensiva está melhorando?

Não existe resposta única. Escolhas diferentes de técnicas, de modelo de exercício (aberto ou às cegas), de prioridades de investimento e de metas são aceitas, **desde que justificadas com os dados do caso e com as fontes**.

---

## Fonte de pesquisa

Fontes primárias mínimas (todas de acesso gratuito):

1. MITRE CORPORATION. *MITRE ATT&CK®*. McLean: MITRE, [s. d.]. Disponível em: <https://attack.mitre.org/>. Acesso em: 13 nov. 2026. — Técnicas, fontes de dados e mitigações. Use também o *ATT&CK Navigator*: <https://mitre-attack.github.io/attack-navigator/>.
2. NATIONAL INSTITUTE OF STANDARDS AND TECHNOLOGY. *The NIST Cybersecurity Framework (CSF) 2.0*. Gaithersburg: NIST, 2024. (NIST CSWP 29). DOI: <https://doi.org/10.6028/NIST.CSWP.29>. Acesso em: 13 nov. 2026.
3. NATIONAL INSTITUTE OF STANDARDS AND TECHNOLOGY. *Incident response recommendations and considerations for cybersecurity risk management: a CSF 2.0 community profile*. Gaithersburg: NIST, 2025. (NIST SP 800-61 Rev. 3). DOI: <https://doi.org/10.6028/NIST.SP.800-61r3>. Acesso em: 13 nov. 2026.
4. NATIONAL INSTITUTE OF STANDARDS AND TECHNOLOGY. *Technical guide to information security testing and assessment*. Gaithersburg: NIST, 2008. (NIST SP 800-115). DOI: <https://doi.org/10.6028/NIST.SP.800-115>. Acesso em: 13 nov. 2026.
5. SCYTHE. *Purple Team Exercise Framework (PTEF)*. [S. l.]: SCYTHE, [s. d.]. Disponível em: <https://github.com/scythe-io/purple-team-exercise-framework>. Acesso em: 13 nov. 2026.
6. SIGMAHQ. *Sigma: generic signature format for SIEM systems*. [S. l.]: SigmaHQ, [s. d.]. Disponível em: <https://github.com/SigmaHQ/sigma>. Acesso em: 13 nov. 2026.

Fontes complementares recomendadas:

7. CYBERSECURITY AND INFRASTRUCTURE SECURITY AGENCY. *#StopRansomware*. Washington, DC: CISA, [s. d.]. Disponível em: <https://www.cisa.gov/stopransomware>. Acesso em: 13 nov. 2026.
8. MITRE ENGENUITY CENTER FOR THREAT-INFORMED DEFENSE. *Adversary emulation library*. [S. l.], [s. d.]. Disponível em: <https://github.com/center-for-threat-informed-defense/adversary_emulation_library>. Acesso em: 13 nov. 2026.
9. BRASIL. Lei nº 13.709, de 14 de agosto de 2018. Lei Geral de Proteção de Dados Pessoais (LGPD). Disponível em: <https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm>. Acesso em: 13 nov. 2026.
10. AUTORIDADE NACIONAL DE PROTEÇÃO DE DADOS. Resolução CD/ANPD nº 15, de 24 de abril de 2024. Aprova o Regulamento de Comunicação de Incidente de Segurança. Brasília, DF: ANPD, 2024.

As fontes 1 a 4 formam o conjunto mínimo obrigatório; 5 e 6 são fortemente recomendadas. O estudante pode acrescentar fontes primárias equivalentes (documentação de fornecedores de EDR/SIEM, relatórios públicos de incidentes no setor de saúde), com referência completa conforme a ABNT.

**Aulas da disciplina a consultar:**

| Item do trabalho | Aulas |
|---|---|
| Papéis, ética e base legal | 1 (Red, Blue e Purple Team; Lei nº 12.737/2012; LGPD) |
| Modelagem do adversário | 2 (Cyber Kill Chain e ATT&CK), 5 (OSINT), 7 (engenharia social e *phishing*), 8 (pós-exploração e movimentação lateral), 11 (inteligência de ameaças) |
| Regras de engajamento | 3 (avaliações, NIST SP 800-115, célula branca), 7 (simulação ética de *phishing*), 13 (emulação de adversários) |
| Telemetria e lacunas | 4 (NIST CSF, defesa em profundidade, SOC), 9 (telemetria, registros e SIEM), 10 (engenharia de detecção e EDR) |
| Detecções e resposta | 10, 11 (*threat hunting*), 12 (resposta a incidentes) |
| Métricas e programa | 14 (MTTD, MTTR, cobertura ATT&CK), 15 (*tabletop*), 16 (programa contínuo) |
| Priorização de riscos | 6 (gestão de vulnerabilidades e priorização por risco) |

---

## Entregável e distribuição da pontuação

**Formato:** um **relatório técnico em PDF**, de **15 a 20 páginas** (sem contar capa, referências e anexos), fonte 11 ou 12, com referências ABNT. **Opcional:** um arquivo JSON de *layer* do *ATT&CK Navigator* com a cobertura atual e a cobertura-alvo, anexado junto com o PDF (não vale nota extra, mas pode substituir a figura de cobertura e conta como evidência no item 3).

**Estrutura e pontuação:**

| Parte | Conteúdo mínimo | Peso |
|---|---|---|
| 1. Modelagem do adversário | Perfil do adversário a emular; **8 a 10 técnicas ATT&CK** (ID, nome, tática), cada uma justificada por evidência do incidente e/ou do boletim ISB-2026-041; sequência na Cyber Kill Chain ou no fluxo de táticas | 20% |
| 2. Regras de engajamento | Objetivo e modelo do exercício; escopo e exclusões; janelas; técnicas proibidas; célula branca e contatos; tratamento de dados sob a LGPD; critérios de parada; autorização formal | 15% |
| 3. Telemetria e lacunas | Matriz técnica × fonte de dados × detecção atual (detectada, parcial, nenhuma); cálculo da cobertura atual; priorização das lacunas, respeitando a licença do SIEM | 15% |
| 4. Detecções e resposta | Pelo menos **4 propostas de detecção** (lógica, fonte, falsos positivos esperados, técnica coberta; pelo menos uma no formato Sigma ou pseudocódigo equivalente); melhorias no *playbook* de resposta segundo o NIST SP 800-61 Rev. 3 | 20% |
| 5. Métricas e programa | Linha de base calculada (MTTD, MTTR, cobertura); metas para 6 e 12 meses; ciclo do programa (cadência, *tabletop*, reteste); alocação do orçamento de R$ 1,2 milhão | 15% |
| 6. Sumário executivo | Até 1 página para o conselho: risco em linguagem de negócio, decisões pedidas, investimento, metas | 10% |
| 7. Qualidade formal | Clareza, coerência entre as partes, uso correto de fontes e ABNT | 5% |
| **Total** | | **100%** |

---

## Roteiro do estudante

### 1. Leia o caso como um investigador

- Releia a linha do tempo e marque, para cada linha, **qual técnica ATT&CK** ela representa e **se havia registro** que permitiria detectá-la.
- Separe o que é **fato do caso** (horários, volumes, ferramentas) do que será **premissa sua** (por exemplo, o momento que você considera "início do ataque" para calcular o MTTD). Premissas devem ser declaradas no relatório.
- Anote os números que vão sustentar seus argumentos: 14 *pushes* negados, 11h33 entre o alerta do LSASS e o alerta crítico, 1,8 GB exfiltrados, 1.900 alertas/dia com 92% de falsos positivos, 40 de 60 GB/dia de licença do SIEM, R$ 1,2 milhão de orçamento.

### 2. Modele o adversário (Parte 1)

- Estude as técnicas no site do ATT&CK e confira táticas, fontes de dados e mitigações.
- Escolha **8 a 10 técnicas**. Bons critérios: apareceram no incidente, aparecem no boletim, têm alto impacto nos ativos da Vitalis, ou são lacunas prováveis da defesa. Explique por que deixou outras de fora.
- Organize as técnicas em uma sequência (do acesso inicial ao impacto). Isso vira o **plano de emulação** do exercício.

### 3. Escreva as regras de engajamento (Parte 2)

- Use a Aula 3 e o NIST SP 800-115 como roteiro. Decida e justifique o modelo: Purple Team **aberto** (as equipes trabalham juntas, técnica a técnica), **às cegas** (o SOC não sabe) ou **híbrido**.
- Pense na segurança do paciente: o que **não pode** ser tocado (analisadores, LIS em produção?) e em que horários.
- Pense na LGPD: o exercício não pode criar um novo vazamento. Como provar a exfiltração sem tirar dados reais da empresa?
- Defina quem compõe a célula branca, quem assina a autorização e quando o exercício para.

### 4. Mapeie telemetria e lacunas (Parte 3)

- Monte uma matriz com as suas técnicas nas linhas e, nas colunas: fonte de dados necessária, fonte existente na Vitalis, regra existente, classificação (detectada, parcial, nenhuma).
- Declare o critério de classificação e calcule a **cobertura atual** em porcentagem.
- Verifique o **orçamento de ingestão**: o que cabe nos 20 GB/dia livres da licença? O que exige comprar mais?

### 5. Proponha detecções e resposta (Parte 4)

- Para cada detecção, descreva: técnica coberta, fonte, lógica em linguagem natural, limiar, falsos positivos esperados e ação do analista. Escreva pelo menos uma no formato Sigma (consulte o repositório SigmaHQ) ou em pseudocódigo.
- Revise o *playbook*: quem é acionado, em quanto tempo, que ações de contenção podem ser feitas sem esperar aprovação, quando acionar o DPO e o jurídico (prazo de comunicação à ANPD).
- Lembre-se do que falhou: o alerta existia, mas ninguém olhou. Melhoria de processo também é resposta.

### 6. Defina métricas e o programa (Parte 5)

- Calcule a **linha de base**: MTTD e MTTR médios dos 6 incidentes (e a mediana, comparando-a com a média), além da cobertura atual.
- Defina metas realistas para 6 e 12 meses e diga **como** serão medidas nos exercícios.
- Monte um ciclo: preparação, execução, ajuste de detecções, reteste, *tabletop* com a diretoria. Mostre como o orçamento de R$ 1,2 milhão é distribuído.

### 7. Escreva para o conselho (Parte 6)

- Uma página, sem siglas não explicadas. Comece pela recomendação, mostre o risco em reais (você pode usar a expectativa de perda anual da Aula 1), o investimento, as metas e as decisões que o conselho precisa tomar.

### 8. Revise antes de enviar

- Cada técnica escolhida aparece na matriz de cobertura? Cada lacuna crítica tem uma detecção ou uma justificativa para não ter? As metas medem o que as detecções prometem melhorar? O orçamento fecha?
- Confira as referências ABNT e os termos estrangeiros em itálico.

Boa entrega!

---

## Solução

> Removida antes de o case ser disponibilizado ao aluno; vai para o professor tutor corrigir.

> **Orientação geral ao tutor.** O caso admite várias soluções. Os valores abaixo são uma **resposta de referência**; aceite escolhas diferentes quando forem coerentes com os dados do caso, justificadas e consistentes entre as partes. Desconte quando o estudante incluir código de exploração ou instruções operacionais de ataque (fora do escopo e contrário à nota ética).

### Parte 1 — Modelagem do adversário (resposta de referência)

Adversário: afiliado de *ransomware* com dupla extorsão (perfil "Cascavel"), motivação financeira, foco em saúde, que prefere contas válidas e ferramentas nativas a *malware* sofisticado.

| Tática | Técnica | Justificativa no caso |
|---|---|---|
| *Initial Access* | T1566.002 *Phishing: Spearphishing Link* | *E-mail* de 06/10 09h12; boletim |
| *Credential Access* | T1621 *Multi-Factor Authentication Request Generation* | 14 *pushes* negados e 15º aprovado |
| *Persistence* | T1098.005 *Account Manipulation: Device Registration* | Novo dispositivo de MFA às 09h58; boletim |
| *Initial Access* / *Persistence* | T1133 *External Remote Services* (com T1078 *Valid Accounts*) | VPN SSL com conta legítima às 11h20 |
| *Discovery* | T1087.002 *Account Discovery: Domain Account* (ou T1046 *Network Service Discovery*) | Consultas em massa ao AD; varredura interna |
| *Credential Access* | T1003.001 *OS Credential Dumping: LSASS Memory* | Alerta do EDR às 14h32 |
| *Lateral Movement* | T1021.001 *Remote Services: Remote Desktop Protocol* | RDP para FS-FAT01 |
| *Defense Evasion* / *Persistence* | T1078.002 *Valid Accounts: Domain Accounts* | Uso de `svc_backup` |
| *Collection* | T1560.001 *Archive Collected Data: Archive via Utility* (ou T1039 *Data from Network Shared Drive*) | Compactação às 16h40 |
| *Exfiltration* | T1567.002 *Exfiltration Over Web Service: Exfiltration to Cloud Storage* | 1,8 GB às 17h02–17h51 |
| *Defense Evasion* | T1562.001 *Impair Defenses: Disable or Modify Tools* | Tentativa às 01h20 |

Alternativas aceitáveis e bem justificáveis pelo boletim: T1110.003 *Password Spraying*, T1558.003 *Kerberoasting*, T1490 *Inhibit System Recovery*, T1484.001 *Group Policy Modification*, T1486 *Data Encrypted for Impact* (esta última deve aparecer como **impacto simulado**, nunca executado). Um bom trabalho explica que incluir técnicas do boletim que **não** ocorreram no incidente testa o que o adversário faria nos próximos passos (3 a 6 dias até a criptografia).

Sinais de baixa qualidade: lista de técnicas sem ID ou com ID errado; técnicas genéricas sem relação com o caso; ignorar o boletim; apresentar comandos de ataque.

### Parte 2 — Regras de engajamento (elementos esperados)

- **Objetivo:** validar detecção e resposta à cadeia "Cascavel" até a exfiltração simulada e a tentativa de desativar defesas; medir MTTD/MTTR por técnica.
- **Modelo:** qualquer modelo justificado. Referência: híbrido — fase 1 **aberta** (técnica a técnica, conforme o PTEF, para construir detecções) e, após 3 a 6 meses, fase 2 **às cegas** para medir MTTD/MTTR reais do SOC e do MSSP.
- **Escopo:** AD, estações e servidores Windows corporativos, VPN, Entra ID, servidores de arquivos, *proxy*; *phishing* simulado para grupos definidos.
- **Exclusões esperadas:** analisadores laboratoriais e sua rede; LIS e banco de laudos em produção (no máximo, testes passivos ou em homologação); portal do paciente em nuvem (salvo autorização específica e respeito às regras do provedor); sistemas de terceiros e operadoras; negação de serviço; criptografia ou exclusão de dados reais; desativação real de EDR em produção sem acordo da célula branca.
- **Janelas:** evitar o pico de coletas (cerca de 6h–10h) e fechamentos de faturamento; execução em horário acordado, com plantão técnico disponível.
- **LGPD:** princípio da necessidade; uso de **arquivos-isca sintéticos** (dados fictícios com marcadores) para simular a exfiltração; proibição de copiar dados reais de pacientes; destino de exfiltração controlado pelo próprio Red Team; registro e descarte seguro de evidências; cláusula de confidencialidade e acordo de tratamento de dados com o fornecedor; DPO na célula branca. O *phishing* simulado não deve usar temas que causem angústia (por exemplo, "resultado de exame alterado") e precisa de alinhamento com RH e jurídico; os resultados individuais não devem ser usados para punição.
- **Célula branca:** CISO (coordenação), CIO ou diretor de TI, DPO, jurídico, representante da diretoria clínica/operações e líder do fornecedor de Red Team. No modelo às cegas, o MSSP e o SOC não participam; no modelo aberto, participam.
- **Critérios de parada:** qualquer impacto em atendimento a pacientes ou nos analisadores; degradação de sistema crítico; detecção de um **adversário real** durante o exercício; acesso inesperado a dados sensíveis reais; violação de escopo; pedido de qualquer membro da célula branca. Deve haver palavra-código e procedimento para diferenciar exercício de incidente real (desconflito).
- **Autorização formal:** assinada por quem tem autoridade sobre os ativos (por exemplo, diretor-presidente ou CIO e CISO), com período, escopo, contatos de emergência e carta que o operador pode apresentar se abordado. Menção ao art. 154-A do Código Penal (Lei nº 12.737/2012) é esperada.

### Parte 3 — Telemetria e lacunas (resposta de referência)

Critério de referência: **detectada** = telemetria centralizada + regra + triagem em tempo útil; **parcial** = telemetria existe mas sem regra, ou regra existe sem triagem oportuna, ou só prevenção; **nenhuma** = sem telemetria utilizável.

| Técnica | Classificação atual | Motivo |
|---|---|---|
| T1566.002 | Parcial | Filtro de *e-mail* previne em parte; *logs* fora do SIEM |
| T1621 | Nenhuma | Entra ID fora do SIEM; sem regra |
| T1098.005 | Nenhuma | Auditoria do Entra ID fora do SIEM |
| T1133 / T1078 | Nenhuma | SIEM só recebe bloqueios da VPN |
| T1087.002 | Nenhuma | Sem eventos de LDAP/Kerberos nem regra |
| T1003.001 | Parcial | EDR alerta, mas severidade média sem triagem fora do horário |
| T1021.001 | Parcial | 4624 tipo 10 no SIEM, sem regra |
| T1560.001 | Parcial | Telemetria de processo no EDR, sem regra |
| T1567.002 | Nenhuma | *Proxy* fora do SIEM e categoria liberada |
| T1562.001 | Detectada | *Tamper protection* + alerta crítico ao MSSP |

Com 10 técnicas: cobertura estrita = 1/10 = **10%**; cobertura ponderada (parcial = 0,5) = (1 + 4 × 0,5)/10 = **30%**. Outras classificações são aceitáveis se o critério estiver declarado e for aplicado de forma consistente.

**Restrição de licença:** há 20 GB/dia livres. Uma priorização coerente cabe nela, por exemplo: Entra ID (2) + sessões VPN (0,5) + Kerberos/grupos do AD (4) + Sysmon em servidores (5) + *proxy* (7) = 18,5 GB/dia. DNS (8 GB/dia) e o tráfego completo do *firewall* (6 GB/dia) exigiriam comprar blocos adicionais (R$ 90 mil por 10 GB/dia) ou filtrar na origem. Deve ser penalizado o trabalho que propõe "enviar tudo ao SIEM" sem considerar a licença.

### Parte 4 — Detecções e resposta (exemplos aceitáveis)

1. **Fadiga de MFA (T1621):** no Entra ID, mais de 5 negações de *push* para o mesmo usuário em 10 minutos, seguidas de aprovação, gera alerta alto. Mitigação complementar: correspondência de número e FIDO2 para usuários críticos.
2. **Registro de novo método de MFA (T1098.005)** em até 24 h após entrada de risco ou de local incomum.
3. **VPN de origem inédita (T1133/T1078):** primeira conexão de um usuário a partir de ASN ou país nunca visto em 30 dias, ou "viagem impossível" entre entradas do Entra ID e da VPN.
4. **Acesso ao LSASS (T1003.001):** reclassificar o alerta do EDR para **alto** em servidores e enviá-lo ao MSSP 24×7; complementar com Sysmon (evento 10). Exemplo Sigma esperado (simplificado):

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
6. **Conta de serviço interativa (T1078.002):** `svc_*` com logon interativo ou RDP; ação de processo: rotação de senhas, contas gerenciadas e remoção de privilégios.
7. **Exfiltração para nuvem (T1567.002):** volume de envio por usuário/host acima de limiar (por exemplo, > 500 MB em 1 h) para a categoria "armazenamento em nuvem"; controle preventivo: bloquear a categoria, liberando apenas serviços corporativos.
8. **Compactação em servidor de arquivos (T1560.001)** por conta não administrativa, correlacionada com acesso a pastas sensíveis.

**Melhorias de resposta esperadas (NIST SP 800-61 Rev. 3, alinhado às funções do CSF 2.0 — *Detect*, *Respond*, *Recover*):** *playbooks* específicos (credencial comprometida/fadiga de MFA; suspeita de pré-*ransomware*; exfiltração de dados pessoais); matriz de severidade que trate roubo de credencial em servidor como crítico; SLA de triagem (por exemplo, alto em até 30 min, 24×7) com cobertura do MSSP para alertas médios/altos ou plantão de segurança; ações de contenção pré-autorizadas (desativar conta, revogar sessões e tokens, isolar host pelo EDR, derrubar VPN); acionamento do DPO e do jurídico para avaliar a comunicação à ANPD em até 3 dias úteis (Resolução CD/ANPD nº 15/2024); preservação de evidências; lições aprendidas com prazo e responsável. Deve aparecer a conclusão central do caso: **o alerta de 14h32 existia; a falha foi de processo (severidade e triagem)**, além de técnica.

### Parte 5 — Métricas e programa

**Linha de base do incidente 6:** contenção às 04h10 de 07/10, detecção confirmada às 02h05 de 07/10.

- Início = acesso à rede (11h20): MTTD = **14h45min (14,75 h)**.
- Início = credencial comprometida (09h31): MTTD = **16h34min (≈16,57 h)**.
- Detecção → contenção: **2h05min (≈2,08 h)**. Aceitar também 02h40 (desativação da conta, 0,58 h) se o estudante definir contenção assim.
- Observação de qualidade: se a detecção fosse contada a partir do alerta de 14h32, o MTTD seria ~3,2 h; a diferença (11h33) mostra o custo da falta de triagem.

**Médias de 12 meses (início = 11h20):**

- MTTD = (20 + 2 + 52 + 30 + 6 + 14,75)/6 = 124,75/6 ≈ **20,8 h**; mediana = (14,75 + 20)/2 ≈ **17,4 h** (o incidente 3, com 52 h, puxa a média para cima).
- MTTR = (6 + 3 + 14 + 8 + 4 + 2,08)/6 = 37,08/6 ≈ **6,2 h**; mediana = (4 + 6)/2 = **5 h**.
- Com início = 09h31: MTTD ≈ 126,57/6 ≈ 21,1 h.

**Cobertura:** 10% (estrita) ou 30% (ponderada) na referência.

**Metas de referência (aceitar outras coerentes):** 6 meses — cobertura ponderada ≥ 60% das técnicas priorizadas; MTTD ≤ 4 h nos exercícios; MTTR ≤ 2 h; 100% dos alertas altos triados em até 30 min. 12 meses — cobertura ≥ 80%; MTTD ≤ 1 h para técnicas de credencial e exfiltração; MTTR ≤ 1 h; taxa de falsos positivos < 70%. Bom trabalho explica que metas medidas em exercício às cegas valem mais que em exercício aberto e que MTTD/MTTR de incidentes reais têm amostra pequena.

**Ciclo do programa:** trimestral, por exemplo: planejamento com inteligência de ameaças → exercício aberto (PTEF) → engenharia de detecção → reteste em 30 dias → *tabletop* semestral com diretoria (Aula 15) → exercício às cegas anual → atualização da *layer* do Navigator.

**Orçamento (exemplo que fecha em R$ 1,2 milhão):** engenheiro(a) de detecção R$ 260 mil + MSSP para alertas médios R$ 240 mil + 2 exercícios externos R$ 360 mil + EDR em 100% dos servidores R$ 70 mil + FIDO2 R$ 66 mil + 1 bloco de SIEM R$ 90 mil = **R$ 1,086 milhão**, com reserva de R$ 114 mil. Alternativas válidas: trocar um exercício externo por exercícios internos com a equipe treinada, ou trocar o MSSP por plantão interno. Penalizar propostas que ultrapassam o orçamento sem pedir suplemento justificado.

**Valor para o negócio (Aula 1):** expectativa de perda anual atual = 0,20 × R$ 18 milhões = **R$ 3,6 milhões**. Se o estudante premissar redução da probabilidade para, por exemplo, 8%, a nova expectativa é R$ 1,44 milhão, redução de R$ 2,16 milhões por ano contra R$ 1,2 milhão investido. A premissa de redução deve estar declarada como estimativa.

### Parte 6 — Sumário executivo

Esperado: recomendação na primeira linha; o incidente em uma frase com o custo (R$ 2,4 milhões) e o dado de que o alerta existia; risco em reais (R$ 3,6 milhões/ano); 3 a 5 decisões solicitadas (aprovar orçamento, aprovar autorização do exercício, aprovar política de MFA resistente a *phishing*, aprovar bloqueio de armazenamento em nuvem não corporativo); metas em linguagem simples (por exemplo, "detectar em menos de 1 hora em vez de 15"); próximos marcos (exercício em fevereiro de 2027, reporte trimestral). Penalizar jargão técnico sem explicação.

### Rubrica de correção

| Critério (peso) | Excelente (100%) | Bom (75%) | Suficiente (50%) | Insuficiente (0–25%) |
|---|---|---|---|---|
| 1. Modelagem do adversário (20%) | 8–10 técnicas com ID e tática corretos, todas justificadas pelo incidente e/ou boletim; sequência coerente; explica exclusões | Técnicas corretas e justificadas, com 1–2 justificativas fracas ou sequência incompleta | Técnicas corretas, mas genéricas ou pouco ligadas ao caso; IDs com erros pontuais | Menos de 6 técnicas, IDs errados, sem relação com o caso, ou conteúdo ofensivo operacional |
| 2. Regras de engajamento (15%) | Todos os elementos (objetivo, modelo, escopo, exclusões clínicas, janelas, LGPD com dados sintéticos, célula branca, parada, desconflito, autorização) | Faltam 1–2 elementos secundários | Faltam elementos importantes (exclusões clínicas ou LGPD ou parada) | RoE genérica, sem autorização formal ou que permite dano a pacientes ou a dados reais |
| 3. Telemetria e lacunas (15%) | Matriz completa com critério explícito; cobertura calculada corretamente; priorização respeitando a licença do SIEM | Matriz e cálculo corretos, priorização sem considerar a licença | Matriz incompleta ou cálculo com erro | Sem matriz ou classificação sem relação com a tabela do caso |
| 4. Detecções e resposta (20%) | ≥ 4 detecções viáveis com fonte, lógica, falsos positivos e ação; uma em Sigma/pseudocódigo correta; *playbook* com SLA, contenção pré-autorizada, ANPD e lições aprendidas; reconhece a falha de processo | ≥ 4 detecções viáveis com pequenas lacunas; *playbook* adequado | Detecções vagas ("monitorar o AD") ou *playbook* genérico | Menos de 2 detecções ou nenhuma melhoria de resposta |
| 5. Métricas e programa (15%) | Linha de base calculada com premissas declaradas (média e mediana); metas realistas e mensuráveis; ciclo contínuo; orçamento fecha | Cálculos corretos, metas ou ciclo pouco detalhados | Erros de cálculo ou metas sem forma de medição | Sem linha de base ou metas arbitrárias; orçamento ignorado |
| 6. Sumário executivo (10%) | 1 página, linguagem de negócio, risco em reais, decisões claras, metas compreensíveis | Bom, com excesso técnico pontual | Resumo técnico, sem decisões claras | Ausente ou cópia do relatório |
| 7. Qualidade formal (5%) | Texto claro, coerente entre as partes, ABNT correta, termos estrangeiros em itálico | Pequenas falhas de formatação | Falhas frequentes | Desorganizado, sem referências |

**Coerência transversal:** ao atribuir os níveis, verifique se as técnicas da Parte 1 aparecem na matriz da Parte 3, se as lacunas críticas recebem detecção na Parte 4 e se as metas da Parte 5 medem essas melhorias. Trabalhos com partes desconectadas não devem receber "Excelente" nos critérios 3, 4 e 5.
