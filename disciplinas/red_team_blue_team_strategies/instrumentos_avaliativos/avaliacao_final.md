# Avaliação final — 10 questões discursivas

Disciplina: Red Team & Blue Team Strategies  
Professor-conteudista: Afonso Cesar Lelis Brandão  
Prazo de entrega: 20/12/2026  
Template de origem: `documentos/Instrumentos Avaliativos/Avaliação final_(10 discursivas)_nomedadisciplina.docx`

> 10 questões discursivas no estilo ENADE (avaliação crítica e analítica), cobrindo as 4 unidades da ementa oficial de 18/11/2026.
> O feedback (resposta esperada) de cada questão fica ao final do documento.

> **Controle de versão:** a seção "Questões" destina-se ao estudante. A seção "Feedbacks" é exclusiva do professor tutor e contém as respostas esperadas e os critérios de correção; ela deve ser removida da cópia distribuída aos estudantes.

**Orientações ao estudante**

- Quantidade: 10 questões discursivas, com valor sugerido de 10 pontos cada (total de 100 pontos).
- Distribuição: Unidade 1 (Planejamento de Operações e Emulação de Adversário), questões 1 e 2; Unidade 2 (Técnicas Ofensivas em Ambiente Controlado), questões 3 a 5; Unidade 3 (Defesa, Monitoramento e Detecção), questões 6 a 8; Unidade 4 (Resposta a Incidentes e Purple Team), questões 9 e 10 (a questão 10 é integradora e mobiliza conteúdos de toda a disciplina).
- Extensão esperada: de 10 a 20 linhas por questão.
- Todas as organizações e situações são fictícias. As atividades ofensivas citadas ocorrem sempre em engajamentos formalmente autorizados, e nenhuma questão pede comandos ou código de ataque.
- Respostas apenas definicionais, sem análise do cenário apresentado, não atendem integralmente ao comando da questão. Quando houver cálculo, mostre o raciocínio.

## Questões

### Questão 1 — Unidade 1: papéis, autorização e regras de engajamento

A Mercantil Aurora, rede varejista com 60 lojas e um *e-commerce* hospedado em um provedor de nuvem, decidiu "testar a segurança" após um concorrente sofrer um vazamento. O gerente de TI convidou, por mensagem de aplicativo, um consultor conhecido para "tentar invadir o site e o que mais conseguir, quando tiver tempo", sem contrato. O consultor pretende incluir no teste o sistema de pagamentos (operado por uma empresa parceira) e copiar uma amostra da base de clientes "para provar que conseguiu". A equipe de monitoramento da empresa não foi informada e ninguém foi designado para acompanhar o teste.

Analise a situação e responda:

a) Explique o que, do ponto de vista legal e ético, diferencia a atividade de um Red Team da conduta de um criminoso, citando a legislação brasileira estudada, e por que a mensagem do gerente de TI não é suficiente.

b) Descreva os papéis de Red, Blue, White e Purple Team que esse exercício deveria ter e proponha os elementos mínimos do documento de autorização e das regras de engajamento, tratando especificamente do sistema do parceiro, da amostra de dados pessoais e do que fazer se a equipe de monitoramento confundir o teste com um ataque real.

### Questão 2 — Unidade 1: inteligência de ameaças e plano de emulação no ATT&CK

A Transportadora Pantanal Cargas recebeu do centro de compartilhamento de informações do setor de logística um relatório sobre o grupo fictício "Lince Dourado". O relatório traz:

| Trecho do relatório | Conteúdo |
|---|---|
| 1 | O grupo tem motivação financeira e ampliou em 60% os ataques a transportadoras brasileiras no último semestre, explorando a dependência do setor de sistemas de rastreamento de frota. |
| 2 | Campanha em curso desde agosto: *e-mails* com faturas falsas, enviados a partir de domínios parecidos com os de clientes reais, a funcionários do financeiro. |
| 3 | Comportamento após o acesso: execução do anexo pelo usuário, comunicação periódica por HTTPS com servidor externo, uso de credenciais válidas de administradores para *logons* remotos em servidores por RDP e envio de dados a serviço de armazenamento em nuvem. |
| 4 | Lista de 300 endereços IP e 120 *hashes* de arquivos associados à campanha. |

A diretoria pediu ao Red Team um exercício que emule esse grupo.

a) Classifique os trechos do relatório nos níveis estratégico, operacional e tático da inteligência de ameaças, indicando quem, na transportadora, usaria cada nível. Explique por que o trecho 4 tem pouco valor para planejar a emulação.

b) Transforme o trecho 3 em um plano de emulação: associe os comportamentos a táticas e técnicas do MITRE ATT&CK (com ID), ordene-os e defina, para cada técnica, um critério de sucesso para o Blue Team. Explique como o *ATT&CK Navigator* seria usado antes e depois do exercício.

### Questão 3 — Unidade 2: reconhecimento, enumeração e o rastro que eles deixam

Em um exercício autorizado na Editora Ponte Alta, a carta de autorização limita o escopo à rede 10.20.0.0/24. Da estação Kali do Red Team (10.20.0.200), uma descoberta de serviços com identificação de versão retornou:

| Host | Portas abertas | Serviço identificado |
|---|---|---|
| 10.20.0.10 | 53, 88, 389, 445 | Controlador de domínio (DNS, Kerberos, LDAP, SMB); LDAP aceita consultas sem autenticação |
| 10.20.0.25 | 21 | FTP com *login* anônimo habilitado |
| 10.20.0.40 | 3389 | RDP |
| 10.20.0.52 | 8080 | Apache Tomcat com a página de administração acessível pela rede |
| 10.20.0.60 | 3306 | MySQL aceitando conexões de qualquer endereço |

A enumeração de DNS também revelou o nome `vpn.parceiro-logistica.com.br` (198.51.100.23), servidor de uma empresa parceira. Do lado do Blue Team, a captura de tráfego no Wireshark mostrou 5.000 pacotes SYN partindo de 10.20.0.200 para as 1.000 portas mais comuns de 5 hosts em 100 segundos, a maioria respondida com RST.

a) Interprete os resultados: quais achados representam a maior superfície de ataque e por quê? Explique o que significa enumerar usuários nesse ambiente e indique, com base nas regras de engajamento, o que o Red Team deve fazer com o servidor do parceiro.

b) Calcule a taxa de pacotes SYN por segundo e explique o padrão que o Blue Team observou no Wireshark. Proponha uma regra de detecção de varredura com limiar e janela de tempo e explique por que uma varredura lenta escaparia dela e como o Blue Team poderia compensar essa limitação.

### Questão 4 — Unidade 2: exploração de vulnerabilidades e acesso inicial

A equipe de infraestrutura da Rede Hospitalar Serra Verde consegue corrigir 100 vulnerabilidades por semana. A varredura do mês retornou 900 achados, dos quais 420 têm CVSS ≥ 7,0. Três exemplos ilustram a fila:

| Vulnerabilidade | CVSS | EPSS | No catálogo KEV? | Ativo |
|---|---|---|---|---|
| X | 9,6 | 0,01 (1%) | Não | Servidor de testes sem acesso externo |
| Y | 7,2 | 0,82 (82%) | Sim | Portal de agendamento exposto à internet |
| Z | 6,1 | 0,35 (35%) | Não | Concentrador de VPN dos médicos |

a) Calcule quanto tempo a equipe levaria para tratar apenas a fila de CVSS ≥ 7,0 e explique por que priorizar somente pelo CVSS é uma estratégia limitada.

b) Proponha um critério de priorização que combine as três fontes de informação e o contexto do ativo, ordenando X, Y e Z e justificando a ordem. Relacione Y e Z aos vetores de acesso inicial do ATT&CK e explique como um Red Team, em exercício autorizado, comprovaria o risco de Y sem causar dano ao portal.

### Questão 5 — Unidade 2: escalada, movimentação lateral, persistência e evasão vistas pelo defensor

Durante um exercício autorizado na Cooperativa de Crédito Ribeira, o Blue Team revisou no Wazuh os eventos de um servidor e encontrou, em sequência:

| Horário | Evento |
|---|---|
| 14h02 | Logon de rede (4624, tipo 3) de uma conta administrativa vindo de uma estação do atendimento |
| 14h03 | Novo serviço instalado no servidor (7045) e processo iniciado como SYSTEM a partir dele |
| 14h09 | Conta local `suporte2` criada (4720) e incluída no grupo Administradores (4732) |
| 14h11 | Tarefa agendada criada para rodar a cada inicialização (4698) |
| 14h20 | Datas de criação de arquivos alteradas em uma pasta temporária (Sysmon, evento 2) |
| 14h24 | Log de segurança apagado (1102) |
| 14h25 | Agente do Wazuh deixa de enviar eventos |

a) Classifique os eventos nas táticas do MITRE ATT&CK (escalada de privilégios, movimentação lateral, persistência e evasão de defesas), indicando uma técnica para cada um. Explique por que a escalada e a persistência, mesmo sem *malware* sofisticado, deixam rastros.

b) Explique por que o apagamento do log e o silêncio do agente são, eles mesmos, sinais de detecção, e proponha duas detecções e duas medidas preventivas para essa sequência. Discuta, ainda, o que "limpeza de rastros" significa para um Red Team em exercício autorizado.

### Questão 6 — Unidade 3: arquitetura de monitoramento, SIEM e fadiga de alertas

O SOC da Distribuidora Elétrica Planalto usa o Wazuh como SIEM e recebe 1.500 alertas por dia. A triagem de cada alerta leva, em média, 12 minutos. A equipe de nível 1 tem oito analistas, cada um com cerca de 6 horas efetivas de triagem por dia. Uma análise de 30 dias mostrou que 70% dos alertas vêm de apenas cinco regras, quase todas com falsos positivos recorrentes de rotinas administrativas conhecidas. O Wazuh recebe hoje apenas eventos de autenticação dos controladores de domínio e alertas do antivírus; não há Sysmon nos servidores nem qualquer sensor de rede.

a) Calcule a capacidade diária de triagem da equipe e o percentual do volume que ela consegue analisar. Explique o conceito de fadiga de alertas e por que ela é um risco de segurança, e não apenas de produtividade.

b) Proponha ações para reequilibrar volume e capacidade sem simplesmente desligar regras e indique duas fontes de telemetria que deveriam entrar na arquitetura de monitoramento (uma de *endpoint*, uma de rede), justificando o que cada uma permitiria detectar.

### Questão 7 — Unidade 3: detecção por assinatura, comportamento e regra; caça a ameaças

A Cooperativa Agrícola Vale do Ipê recebeu um relatório de inteligência sobre um grupo que ataca o agronegócio. O relatório traz 500 endereços IP, 200 *hashes* de arquivos e a descrição do comportamento do grupo: uso de credenciais válidas de acesso remoto obtidas por *phishing*, criação de tarefas agendadas para persistência e uso de ferramentas administrativas legítimas para se mover entre servidores. O gestor do SOC propôs apenas importar os IPs e *hashes* para o *firewall* e o EDR e considerar a ameaça "coberta". Ao mesmo tempo, uma regra existente de tarefas agendadas suspeitas disparou 250 vezes no último mês, com 10 verdadeiros positivos.

a) Diferencie detecção por assinatura, por comportamento e por regra de correlação e, com base na Pirâmide da Dor, analise a limitação da proposta do gestor, indicando em que níveis da pirâmide estão as diferentes partes do relatório.

b) Calcule a precisão da regra de tarefas agendadas e proponha, segundo o ciclo de vida de uma detecção, como melhorá-la e como comprovar que ela funciona antes de considerá-la confiável. Formule uma hipótese de caça a ameaças derivada do relatório, indicando a consulta e a linha de base que permitiriam testá-la.

### Questão 8 — Unidade 3: *hardening* e redução da superfície de ataque

Uma varredura interna na Editora Ponte Alta, após o exercício da Questão 3, encontrou:

- 240 servidores Windows, 61 sem atualizações de segurança há mais de 90 dias, 4 deles com vulnerabilidade presente no catálogo KEV;
- RDP habilitado e acessível a partir de qualquer estação em todos os servidores;
- a mesma senha de administrador local em todas as 1.800 estações;
- SMBv1 habilitado em 35 servidores;
- 92 contas no grupo Domain Admins, 30 delas usadas também para *e-mail* e navegação;
- 9 serviços expostos à internet, 3 sem responsável conhecido (um painel de administração, o FTP anônimo e um servidor de testes).

Há equipe para executar apenas parte das correções no próximo trimestre, e um servidor legado do sistema editorial não pode ser atualizado porque o fornecedor encerrou o suporte.

a) Explique o que é *hardening* e redução da superfície de ataque e como os CIS Benchmarks e os CIS Controls apoiam esse trabalho. Escolha quatro medidas prioritárias para o trimestre, justificando cada uma pela técnica de ataque que ela dificulta.

b) Proponha indicadores para mostrar a redução da superfície antes e depois das medidas e explique como validar que elas funcionam. Indique como tratar o servidor legado que não pode ser atualizado.

### Questão 9 — Unidade 4: resposta a incidentes, evidências e linha do tempo

Na rede de escolas Instituto Horizonte, o EDR alertou às 23h de uma quinta-feira (horário de Brasília) que quatro servidores estavam excluindo cópias de sombra e renomeando arquivos em massa. Um dos servidores, SRV-SEC01, hospeda a secretaria acadêmica, com dados pessoais de alunos menores de idade. O técnico de plantão sugeriu desligar todos os servidores da tomada imediatamente e, na segunda-feira, "ver o que aconteceu". Na sexta-feira, às 10h, a equipe reuniu os registros abaixo e confirmou que arquivos da secretaria haviam sido copiados para fora da rede antes da criptografia:

| Fonte | Fuso do registro | Evento | Horário registrado |
|---|---|---|---|
| EDR | UTC | Exclusão de cópias de sombra em SRV-SEC01 | sexta, 01h58 |
| *Firewall* | Brasília | 2,3 GB enviados de SRV-SEC01 para endereço externo | quinta, 21h10 a 22h35 |
| Servidor SRV-SEC01 | Brasília | Logon RDP da conta `suporte.ti` | quinta, 19h47 |
| Provedor de *e-mail* | UTC | Entrega de *e-mail* com *link* malicioso à conta `suporte.ti` | quinta, 14h52 |

a) Avalie criticamente a sugestão do técnico, considerando a tensão entre conter o dano e preservar evidências, e descreva uma contenção mais adequada, com a ordem de volatilidade e os cuidados de cadeia de custódia. Em seguida, normalize os horários da tabela para um único fuso e monte a linha do tempo do incidente.

b) Relacione as atividades desse incidente às fases do ciclo de resposta do NIST SP 800-61 Rev. 2 (e às funções do CSF 2.0 adotadas na Rev. 3) e explique quais obrigações de comunicação decorrem da confirmação feita na sexta-feira, segundo a LGPD e a regulamentação da ANPD, e quais papéis precisam ser acionados.

### Questão 10 — Unidade 4: exercício *purple team* e relatório final (questão integradora)

O CISO da Seguradora Atlântica Sul apresentou ao conselho o seguinte painel trimestral:

| Indicador | Valor apresentado |
|---|---|
| Ataques bloqueados | 3,2 milhões |
| Cobertura ATT&CK | 85% ("existem regras para 85% das técnicas da matriz") |
| MTTD médio | 40 horas |
| MTTD mediano | 6 horas |
| Alertas no trimestre | 2.400, dos quais 240 verdadeiros positivos |

Nenhuma das regras havia sido executada contra o comportamento real das técnicas. Um conselheiro perguntou se a seguradora estava "85% protegida". Pressionado, o CISO conduziu um exercício *purple team*: com base em inteligência sobre dois grupos que atacam seguradoras, priorizou 25 técnicas e as emulou em ambiente autorizado. Resultado: 7 técnicas geraram alerta correto, 8 deixaram telemetria sem alerta e 10 não deixaram registro algum. Após ajustes, o reteste, 30 dias depois, mostrou 15 com alerta, 6 só com telemetria e 4 sem registro.

a) Analise criticamente o painel: explique por que "ataques bloqueados" e a cobertura de 85% não respondem à pergunta do conselheiro, interprete a diferença entre MTTD médio e mediano e calcule a precisão dos alertas. Calcule a cobertura validada e a visibilidade antes e depois do reteste.

b) Descreva o ciclo do exercício *purple team* que produziu esses números e proponha a estrutura do relatório final ao conselho (achados, riscos, recomendações e métricas), redigindo um achado completo como exemplo e indicando como a *layer* do *ATT&CK Navigator* antes/depois e os indicadores de melhoria seriam apresentados.

## Feedbacks

> **Uso exclusivo do professor tutor.** As respostas esperadas são referências, não gabaritos literais: devem ser aceitas formulações diferentes que demonstrem domínio dos conceitos e análise do cenário. Em cada questão, a nota integral exige os elementos listados nos critérios; a ausência de análise do cenário (resposta apenas conceitual) limita a nota a crédito parcial. Quanto aos IDs do MITRE ATT&CK, aceite os de versões recentes da matriz (por exemplo, a evasão de defesas, *Defense Evasion*, TA0005, foi dividida em *Stealth* e *Defense Impairment* na versão 19, de abril de 2026), desde que coerentes.

**Mapa das questões (uso do tutor):**

| Questão | Unidade | Aulas avaliadas |
|---|---|---|
| 1 | 1 | 1 (papéis) e 2 (regras de engajamento, autorização e aspectos legais) |
| 2 | 1 | 3 (ATT&CK e planos de emulação) e 4 (inteligência de ameaças) |
| 3 | 2 | 5 (reconhecimento e enumeração), com Kali e Wireshark |
| 4 | 2 | 6 (exploração de vulnerabilidades e acesso inicial) |
| 5 | 2 | 7 (escalada, movimentação lateral e persistência) e 8 (evasão e limpeza de rastros) |
| 6 | 3 | 9 (arquitetura de monitoramento) e 10 (regras) |
| 7 | 3 | 10 (assinatura, comportamento e regras) e 11 (caça a ameaças) |
| 8 | 3 | 12 (*hardening* e superfície de ataque) |
| 9 | 4 | 13 (ciclo de resposta) e 14 (evidências e linha do tempo) |
| 10 | 4 | 15 (*purple team*) e 16 (relatório final), integrando 3, 9 e 10 |

### Questão 1

**Resposta esperada**

a) Tecnicamente, muitas ações de um Red Team são idênticas às de um criminoso; o que as distingue é a **autorização formal**, dada por quem tem autoridade sobre os ativos, com escopo e limites definidos. No Brasil, a Lei nº 12.737/2012 incluiu no Código Penal o art. 154-A, que tipifica a invasão de dispositivo informático, com penas agravadas pela Lei nº 14.155/2021. A mensagem do gerente não basta: é informal, não define escopo nem período ("o que mais conseguir, quando tiver tempo"), não há garantia de que o gerente tenha autoridade para autorizar e, sobretudo, ele não pode autorizar testes em ativos que não pertencem à Mercantil Aurora (o sistema de pagamentos do parceiro e, conforme o contrato, a infraestrutura do provedor de nuvem). Eticamente, copiar dados de clientes "para provar" expõe dados pessoais sem necessidade.

b) Papéis: **Red Team** (o consultor, que emula o adversário dentro do escopo); **Blue Team** (a equipe de monitoramento, que detecta e responde); **White Team** (célula de controle com representante da diretoria, TI, jurídico e encarregado de dados, que aprova o plano, arbitra dúvidas, faz o desconflito e pode parar o exercício); **Purple Team** (função de colaboração que, ao final ou durante um exercício aberto, compara o que foi feito com o que foi visto e transforma as diferenças em melhorias). Elementos mínimos: documento assinado por quem tem autoridade (diretoria) contendo **escopo** (ativos incluídos e excluídos, por exemplo URLs e endereços do *e-commerce*), **período e janelas** de execução, **técnicas permitidas e proibidas** (por exemplo, sem negação de serviço), **contatos de emergência** e critérios de interrupção, e regras de **tratamento e descarte** dos dados e credenciais. O sistema de pagamentos do parceiro deve ficar **fora do escopo**, a menos que o próprio parceiro autorize formalmente; o uso do provedor de nuvem deve respeitar a política do provedor. Quanto aos dados pessoais, o **impacto deve ser demonstrado, e não executado**: registrar evidência de acesso (por exemplo, a estrutura da tabela ou a contagem de registros) em vez de copiar a base, com exposição mínima e descarte ao final, conforme a LGPD (Lei nº 13.709/2018). Para o caso de o Blue Team confundir o teste com ataque real, as RoE preveem o **desconflito**: o Blue Team consulta o White Team, que confirma (por palavra-código ou registro de atividades do Red Team) se a atividade é do exercício; se não for, trata-se como incidente real e o exercício é suspenso.

**Critérios de correção**

- Integral: cita autorização formal como diferença central e o art. 154-A (Lei nº 12.737/2012, com ou sem a Lei nº 14.155/2021); aponta ao menos duas falhas da mensagem (informalidade/escopo indefinido/autoridade/ativos de terceiros); descreve corretamente os quatro papéis, com destaque para o White Team; lista escopo, regras de engajamento e contatos de emergência; trata o parceiro como fora do escopo sem autorização dele; propõe demonstrar o impacto sem copiar dados, mencionando a LGPD; descreve o desconflito.
- Parcial: reconhece a necessidade de autorização, mas não cita a legislação, omite o White Team ou não trata do sistema do parceiro, dos dados pessoais ou do desconflito.
- Insuficiente: considera a mensagem válida ou descreve formas de executar o ataque.

### Questão 2

**Resposta esperada**

a) Trecho 1: **estratégico** (tendência, motivação e impacto no setor), usado pela diretoria e pelo CISO para decidir investimento e prioridade. Trecho 2: **operacional** (uma campanha específica em curso, com alvo, período e modo de ação), usado pelo SOC e pela equipe de resposta para se preparar e alertar o financeiro. Trecho 3: **tático** (TTPs: o que o grupo faz depois de entrar), usado pelo Red Team para planejar a emulação e pelo Blue Team para escrever detecções. Trecho 4: **indicadores técnicos** (IoCs, que muitos autores tratam como parte do nível tático ou como um quarto nível, técnico), úteis para bloqueio e busca retroativa. Aceitar outras fronteiras se o critério estiver declarado. O trecho 4 pouco ajuda na emulação porque IPs e *hashes* estão na base da Pirâmide da Dor: mudam a cada campanha e não descrevem comportamento; emular um IP não testa se o Blue Team detecta o modo de agir do grupo.

b) Plano de referência, em ordem: (1) *Initial Access* — T1566.001 *Spearphishing Attachment*; (2) *Execution* — T1204.002 *User Execution: Malicious File*; (3) *Command and Control* — T1071.001 *Application Layer Protocol: Web Protocols*; (4) *Initial Access*/*Persistence* (e *Defense Evasion*/*Stealth*, conforme a versão) — T1078 *Valid Accounts* (T1078.002 para contas de domínio); (5) *Lateral Movement* — T1021.001 *Remote Desktop Protocol*; (6) *Exfiltration* — T1567.002 *Exfiltration to Cloud Storage*. Critérios de sucesso para o Blue Team, por exemplo: anexo bloqueado ou alerta de execução em até 15 min; *beaconing* HTTPS identificado pela regularidade das conexões; logon RDP de conta administrativa a partir de estação incomum gerando alerta; volume anômalo para armazenamento em nuvem detectado antes de 500 MB. A emulação usa procedimentos benignos (arquivo inofensivo que simula o comportamento, dados sintéticos) dentro das RoE. No **Navigator**, antes do exercício cria-se uma *layer* com as técnicas do plano, coloridas pela cobertura esperada; depois, uma *layer* com o resultado (detectado, só telemetria, nada), e a comparação entre as duas orienta as melhorias e o reteste.

**Critérios de correção**

- Integral: classifica corretamente os trechos 1 a 3 nos três níveis, com o público de cada um; explica a limitação dos IoCs (Pirâmide da Dor ou volatilidade); associa ao menos cinco comportamentos a técnicas com IDs corretos e em sequência coerente; define critérios de sucesso observáveis; descreve o uso do Navigator antes e depois.
- Parcial: classificação correta sem a explicação dos IoCs, ou técnicas sem ID/sem critério de sucesso, ou ausência do Navigator.
- Insuficiente: confunde os níveis, propõe emular apenas a lista de IPs e *hashes* ou descreve procedimentos ofensivos operacionais.

### Questão 3

**Resposta esperada**

a) Maior superfície: o **controlador de domínio com LDAP aceitando consultas sem autenticação** (permite listar usuários, grupos e computadores, mapa para todo o ataque seguinte); o **Tomcat com página de administração acessível** (interface administrativa exposta é um caminho clássico para execução de código, se houver credencial fraca); o **MySQL aceitando conexões de qualquer endereço** e o **FTP anônimo** (exposição direta de dados); o RDP é alvo de força bruta e de movimentação lateral. Enumerar usuários significa descobrir nomes de contas válidas (por exemplo, pelo LDAP anônimo, pelo SMB ou pelas respostas do Kerberos), o que alimenta ataques de senha e *phishing*; em exercício, a enumeração é registrada como achado, sem tentativas de senha fora das RoE. O servidor `vpn.parceiro-logistica.com.br` está **fora do escopo** (198.51.100.23 não pertence a 10.20.0.0/24 e é de outra empresa): o Red Team não o testa, registra a descoberta e consulta o White Team; testá-lo seria acesso não autorizado.

b) 5.000 ÷ 100 = **50 SYN por segundo**. O padrão é de varredura SYN (meia conexão): uma única origem envia SYN a muitas portas de vários hosts em pouco tempo; portas fechadas respondem RST, portas abertas SYN-ACK, e a conexão não se completa. Regra possível: alertar quando uma origem interna tocar mais de 100 portas distintas, ou mais de 20 hosts distintos, em 60 segundos (no Wazuh, por correlação de *logs* do *firewall*, ou no Security Onion, por regra Suricata ou pelo `conn.log` do Zeek). Uma varredura lenta (por exemplo, uma porta a cada 30 segundos, levando mais de 8 horas para 1.000 portas) fica abaixo do limiar em qualquer janela de 60 s. Compensações: agregar em janelas longas (portas e hosts distintos por origem em 24 h), comparar com a linha de base de cada estação (estações de usuário não costumam falar com centenas de portas), usar alvos-isca (*honeypots*) que nenhum sistema legítimo acessa e correlacionar com outros sinais.

**Critérios de correção**

- Integral: prioriza corretamente LDAP anônimo, Tomcat administrativo, banco e FTP expostos, com justificativa; explica enumeração de usuários e sua utilidade para o atacante; trata o servidor do parceiro como fora do escopo, com consulta ao White Team; calcula 50 SYN/s; explica o padrão SYN/RST; propõe regra com limiar e janela; explica a evasão por varredura lenta e ao menos uma compensação.
- Parcial: interpreta os serviços sem tratar do escopo, ou propõe a regra sem discutir a varredura lenta, ou erra o cálculo.
- Insuficiente: recomenda testar o servidor do parceiro ou descreve como explorar os serviços.

### Questão 4

**Resposta esperada**

a) 420 ÷ 100 = **4,2 semanas** apenas para a fila de CVSS ≥ 7,0, sem contar os achados novos que surgirão no período. O CVSS mede a **gravidade técnica** da falha, mas não indica se ela está sendo explorada nem considera o contexto do ativo. Priorizar só por ele leva a gastar esforço em falhas graves mas improváveis (como X, em servidor isolado) enquanto falhas exploradas ativamente esperam na fila.

b) Critério: priorizar primeiro o que está no **KEV** (exploração confirmada) em ativos expostos ou críticos; depois, alta **EPSS** (probabilidade de exploração nos próximos 30 dias) combinada à exposição e à criticidade do ativo; usar o CVSS como desempate e critério de severidade. Ordem: **Y** (no KEV, EPSS de 82%, exposta à internet, portal de pacientes); **Z** (EPSS de 35%, VPN é porta de entrada remota e alvo frequente, mesmo com CVSS médio); **X** (CVSS alto, mas EPSS de 1% e ativo sem acesso externo; pode seguir o ciclo normal, com mitigação compensatória). Aplicando esse filtro, a fila crítica tende a ser muito menor que 420 itens e pode ser tratada em dias. No ATT&CK, Y corresponde a T1190 *Exploit Public-Facing Application* e Z a T1133 *External Remote Services*, ambos na tática *Initial Access* (TA0001). Em exercício autorizado, o Red Team comprova o risco de Y sem dano: identifica a versão vulnerável e usa verificações não destrutivas (por exemplo, o `check` de um módulo do Metasploit ou um módulo *auxiliary* de varredura), em janela acordada e com o White Team ciente, registrando a evidência em vez de executar a exploração no ambiente de produção; se for preciso demonstrar a exploração, faz-se em cópia de homologação.

**Critérios de correção**

- Integral: calcula 4,2 semanas; explica que o CVSS mede gravidade e não probabilidade/exploração; define EPSS e KEV corretamente; ordena Y, Z, X (ou Y, X, Z com justificativa contextual consistente) considerando exposição e criticidade; associa Y e Z a técnicas de acesso inicial; descreve comprovação não destrutiva dentro das RoE.
- Parcial: ordenação correta sem explicar os indicadores, ou cálculo ausente/errado, ou sem a ligação com o acesso inicial e a comprovação segura.
- Insuficiente: prioriza X por ter o maior CVSS sem considerar exploração nem contexto, ou propõe explorar o portal em produção.

### Questão 5

**Resposta esperada**

a) 14h02: **movimentação lateral** — T1021.002 *SMB/Windows Admin Shares* ou T1078.002 *Valid Accounts: Domain Accounts* (logon de rede com conta administrativa a partir de estação). 14h03: **execução e escalada de privilégios** — T1569.002 *Service Execution* e T1543.003 *Create or Modify System Process: Windows Service* (o serviço roda como SYSTEM). 14h09: **persistência** — T1136.001 *Create Account: Local Account* e T1098 *Account Manipulation* (inclusão no grupo Administradores). 14h11: **persistência** — T1053.005 *Scheduled Task*. 14h20: **evasão de defesas (furtividade, TA0005)** — T1070.006 *Timestomp*. 14h24: **evasão de defesas (enfraquecimento, TA0112)** — T1685.005 *Clear Windows Event Logs* (T1070.001 em versões anteriores à 19). 14h25: **evasão de defesas (enfraquecimento, TA0112)** — T1685 *Disable or Modify Tools* (T1562.001 em versões anteriores à 19). Escalada e persistência exigem **mudar o estado do sistema** (criar serviço, conta, tarefa, alterar grupo), e cada mudança gera evento nativo do Windows ou do Sysmon; o atacante que usa ferramentas legítimas evita o *hash* malicioso, mas não evita o registro da ação.

b) O evento 1102 é gerado justamente quando o log de segurança é apagado, e, se o agente encaminha os eventos em tempo real, tudo o que aconteceu antes já está no Wazuh; o apagamento revela intenção de esconder. O silêncio repentino de um agente (sem *heartbeat*) num servidor que sempre envia eventos é anomalia: ausência de dado também é dado. Detecções: alerta crítico para 1102 fora de manutenção registrada; alerta de agente desconectado em servidor crítico correlacionado com eventos anteriores do mesmo host; correlação "conta criada + incluída em Administradores + tarefa agendada no mesmo host em 15 minutos"; serviço novo instalado a partir de logon remoto. Medidas preventivas: encaminhamento em tempo real e retenção central; proteção contra adulteração do agente e do EDR; contas administrativas por camadas e LAPS para impedir reuso de credenciais; restringir quem pode criar serviços e tarefas remotamente. Em exercício autorizado, "limpeza de rastros" significa **remover os artefatos que o próprio Red Team criou** (contas, tarefas, arquivos de teste) e **documentar** cada um no relatório, de modo que o cliente possa conferir; apagar logs do cliente ou ocultar ações só ocorre se as RoE o autorizarem expressamente, em laboratório, para testar a detecção, nunca em produção sem acordo do White Team.

**Critérios de correção**

- Integral: classifica corretamente ao menos cinco eventos nas táticas, com técnicas coerentes; explica por que mudanças de estado deixam rastros; explica o 1102 e o silêncio do agente como sinais; propõe duas detecções e duas medidas preventivas viáveis; diferencia limpeza ética de artefatos próprios de antiforense.
- Parcial: classificação correta sem a análise do rastro, ou detecções genéricas, ou omissão da discussão ética.
- Insuficiente: confunde as táticas, considera que o apagamento elimina a possibilidade de detecção ou descreve como executar a evasão.

### Questão 6

**Resposta esperada**

a) Volume: 1.500 × 12 = 18.000 minutos = **300 horas** de análise por dia. Capacidade: 8 × 6 = 48 horas = 2.880 minutos ÷ 12 = **240 alertas por dia**, ou **16%** do volume. A **fadiga de alertas** ocorre quando o excesso de alertas, em especial falsos positivos, leva os analistas a fechá-los rapidamente ou ignorá-los; com isso, o alerta verdadeiro se perde no ruído. É um risco de segurança porque 84% dos alertas nem sequer são analisados, e a atenção dedicada aos analisados cai: o ataque real pode estar entre os ignorados, aumentando o tempo de permanência do invasor.

b) Ações: (1) **ajustar as cinco regras ruidosas** com exceções restritas às rotinas administrativas conhecidas (por exemplo, por conta de serviço e servidor de origem específicos), sem desligá-las; se elas respondem por 70% do volume (1.050 alertas) e o ajuste elimina a maior parte do ruído, o volume se aproxima da capacidade; (2) **priorizar por criticidade** do ativo e confiança da regra (no Wazuh, pelo nível da regra), para que os alertas mais relevantes sejam triados primeiro; (3) **enriquecer e correlacionar** (contexto de ativo, usuário, inteligência), agrupando alertas relacionados em um único caso; (4) **automatizar** etapas repetitivas da triagem; (5) **revisar continuamente** a precisão de cada regra como métrica. Exceções devem ser estreitas, documentadas e revisadas. Telemetria a acrescentar: no *endpoint*, **Sysmon** nos servidores (criação de processos com linha de comando, acesso ao LSASS, conexões de rede por processo), lido pelo agente do Wazuh, que permite detectar execução suspeita, roubo de credenciais e movimentação lateral que hoje passam despercebidos; na rede, um **sensor como o Security Onion** (Zeek e Suricata) ou ao menos os *logs* de DNS e *proxy*, que permite ver varreduras, comunicação de comando e controle e exfiltração, inclusive de equipamentos sem agente. Ao acrescentar fontes, o ajuste das regras precisa vir antes, senão a fadiga aumenta.

**Critérios de correção**

- Integral: calcula 240 alertas/dia e cerca de 16%; define fadiga de alertas e explica por que é risco de segurança; propõe ao menos três ações, incluindo o ajuste das regras ruidosas com exceções restritas; indica uma fonte de *endpoint* e uma de rede, com o que cada uma detecta.
- Parcial: cálculo correto e propostas genéricas (por exemplo, "contratar mais analistas" como única ação), ou sem as fontes de telemetria.
- Insuficiente: propõe desligar as regras ou ignora a fadiga de alertas.

### Questão 7

**Resposta esperada**

a) **Assinatura**: compara com um padrão conhecido (*hash*, cadeia de bytes, regra YARA ou Suricata para um artefato específico); é precisa, mas só pega o que já se conhece. **Comportamento**: observa o que o processo ou o usuário faz (por exemplo, tarefa agendada criada por conta incomum, ferramenta administrativa usada fora do padrão), detectando variantes desconhecidas com mais falsos positivos. **Regra de correlação**: combina eventos de fontes ou momentos diferentes (por exemplo, VPN de origem nova seguida de RDP em servidor). A Pirâmide da Dor, proposta por David Bianco, relaciona o tipo de indicador ao custo que sua detecção impõe ao adversário. *Hashes* (base) e endereços IP estão nos níveis mais baixos: são triviais ou fáceis de trocar, de modo que o bloqueio é útil, mas contornado em minutos. A descrição do comportamento — credenciais válidas de acesso remoto, tarefas agendadas para persistência, ferramentas administrativas legítimas para movimentação lateral — está no topo, nas **TTPs**, que obrigam o adversário a mudar sua forma de trabalhar. Considerar a ameaça "coberta" só com IPs e *hashes* é um erro: justamente o comportamento mais estável do grupo fica sem detecção, e o uso de ferramentas legítimas nem sequer geraria *hash* malicioso.

b) Precisão: 10 ÷ 250 = **4%**. Pelo ciclo de vida da detecção: analisar os falsos positivos para identificar padrões (por exemplo, tarefas criadas por ferramentas corporativas conhecidas), refinar a lógica com exceções restritas e contexto (criação remota, contas incomuns, binários em pastas temporárias), versionar a regra como código (por exemplo, em Sigma ou como regra local do Wazuh), e **testar** antes de confiar: executar o comportamento em ambiente autorizado (emulação, por exemplo com testes atômicos) e verificar se a regra dispara, além de medir a nova precisão no mês seguinte. Hipótese de caça: "se o grupo usa credenciais válidas de acesso remoto, haverá *logons* de VPN de contas em horários, locais ou dispositivos incomuns, seguidos de *logons* remotos em servidores que essas contas não costumam acessar". Consulta: para cada conta, comparar origem, horário e servidores acessados nos últimos 30 dias com a **linha de base** dos 90 dias anteriores (por exemplo, pares conta × servidor nunca vistos, ou horários fora de média ± 2 desvios-padrão). A caça que confirmar o padrão deve gerar uma nova regra automatizada; a que não confirmar documenta o resultado e as lacunas de dados.

**Critérios de correção**

- Integral: diferencia os três tipos de detecção; explica a Pirâmide da Dor, posiciona IPs/*hashes* na base e o comportamento em TTPs; critica a proposta; calcula 4%; descreve refinamento e teste da regra (com reteste/validação); formula hipótese testável ligada ao relatório, com consulta e linha de base.
- Parcial: explica a pirâmide sem diferenciar os tipos de detecção, não propõe teste da regra, ou a hipótese de caça é genérica ("procurar ataques") ou sem linha de base.
- Insuficiente: considera os IoCs suficientes ou não calcula/interpreta a precisão.

### Questão 8

**Resposta esperada**

a) ***Hardening*** é o fortalecimento da configuração de sistemas: remover o que não é necessário (serviços, protocolos, contas, softwares), aplicar configurações seguras e atualizações e restringir privilégios. **Redução da superfície de ataque** é diminuir os pontos pelos quais um adversário pode interagir com o ambiente (serviços expostos, portas, contas, caminhos de acesso). Os **CIS Benchmarks** trazem configurações seguras detalhadas por produto (por exemplo, Windows Server), verificáveis item a item; os **CIS Controls** (v8.1) organizam o programa em 18 controles priorizados, como inventário de ativos (1), configuração segura (4), gestão de contas (5), controle de acesso (6) e gestão contínua de vulnerabilidades (7). Quatro medidas prioritárias coerentes: (1) **LAPS** para senha única de administrador local, que impede a movimentação lateral com a mesma credencial em 1.800 estações (T1078.003, T1021); (2) **restringir RDP** a servidores de salto, com MFA, que fecha o caminho de movimentação lateral (T1021.001); (3) **separar e reduzir as contas Domain Admins**, retirando o uso para *e-mail* e navegação, que reduz o roubo de credenciais privilegiadas (T1078.002, T1566); (4) **atualizar primeiro os 4 servidores com KEV** e **retirar da internet os 3 serviços sem responsável**, que reduz o acesso inicial (T1190, T1133). Desabilitar SMBv1 também é aceitável. A justificativa deve ligar cada medida a uma técnica.

b) Indicadores antes/depois: serviços expostos (9 → 6, −33%); servidores com RDP aberto a qualquer estação (240 → 0); estações com senha local repetida (1.800 → 0); contas Domain Admins (92 → número mínimo justificado); servidores sem atualização há mais de 90 dias (61 → meta) e com KEV pendente (4 → 0); servidores com SMBv1 (35 → 0); conformidade com o CIS Benchmark em porcentagem de itens atendidos. Validação: nova varredura e nova descoberta de serviços, auditoria de configuração automatizada e um **reteste** do Red Team (ou exercício *purple*) das técnicas que as medidas deveriam bloquear. Servidor legado: **exceção formal** com aceite de risco pelo dono do negócio e prazo de revisão, e **controles compensatórios** — isolamento em segmento próprio, acesso só a partir de origens autorizadas, desligar serviços desnecessários, monitoramento reforçado (agente do Wazuh e sensor de rede) e plano de substituição.

**Critérios de correção**

- Integral: define *hardening* e superfície de ataque; explica o papel dos CIS Benchmarks e dos CIS Controls; escolhe quatro medidas coerentes com o cenário, cada uma ligada a uma técnica; propõe indicadores antes/depois mensuráveis e uma forma de validação; trata o legado com aceite de risco e controles compensatórios.
- Parcial: medidas corretas sem ligação com técnicas, indicadores vagos ou legado tratado apenas como "atualizar".
- Insuficiente: lista genérica de boas práticas sem relação com o cenário.

### Questão 9

**Resposta esperada**

a) Desligar os servidores da tomada interrompe a criptografia, mas destrói a **memória volátil** (processos, conexões, possíveis chaves), essencial para entender o ataque, e esperar até segunda-feira deixa o incidente sem tratamento por dias. A contenção busca impedir que o dano aumente preservando evidências: isolar os servidores pela rede (por exemplo, pelo isolamento do EDR), desabilitar a conta `suporte.ti` e revogar suas sessões, bloquear o destino externo da exfiltração e coletar evidências da **mais volátil para a menos volátil** (memória e conexões antes do disco), conforme a RFC 3227. Toda evidência deve ter **cadeia de custódia**: quem coletou, quando, como, onde foi guardada e por quais mãos passou, com *hashes* (por exemplo, SHA-256) que comprovem integridade (ABNT NBR ISO/IEC 27037). Se não houver como isolar e a criptografia avançar, desligar pode ser uma decisão justificável, mas deve ser tomada pelo coordenador do incidente, e não por improviso. **Linha do tempo** (horário de Brasília, UTC−3, sem horário de verão desde 2019): quinta, 11h52 — entrega do *e-mail* com *link* à conta `suporte.ti` (14h52 UTC); 19h47 — logon RDP em SRV-SEC01; 21h10–22h35 — envio de 2,3 GB para fora; 22h58 — exclusão de cópias de sombra em SRV-SEC01 (01h58 UTC de sexta); 23h00 — alerta do EDR sobre a exclusão de cópias e a renomeação em massa nos quatro servidores; sexta, 10h — confirmação da exfiltração. A linha do tempo mostra o padrão de dupla extorsão (dados roubados antes da criptografia) e que houve cerca de 11 horas entre o *e-mail* e o início da criptografia sem detecção. Sem a normalização, a exclusão das cópias de sombra pareceria ter ocorrido no dia seguinte, desordenando a sequência.

b) **Preparação**: plantão sem *playbook* nem autoridade definida para decidir (CSF: Governar, Identificar, Proteger). **Detecção e análise**: alerta do EDR às 23h, análise e confirmação da exfiltração às 10h (Detectar). **Contenção, erradicação e recuperação**: isolamento, desativação de contas, remoção da persistência, correção do vetor de entrada, restauração de *backups* íntegros com monitoramento reforçado (Responder e Recuperar). **Atividade pós-incidente**: lições aprendidas, revisão do *playbook* e das detecções (melhoria contínua, que na Rev. 3 retroalimenta Governar e Identificar). A confirmação de que dados pessoais (de menores, dado de alto risco) foram copiados é o marco a partir do qual corre o prazo: o art. 48 da LGPD e a Resolução CD/ANPD nº 15/2024 exigem comunicar à ANPD e aos titulares (aqui, alunos e responsáveis) incidente que possa causar risco ou dano relevante, em **três dias úteis** contados desse conhecimento (sexta-feira às 10h), além de manter registro do incidente. Devem ser acionados o coordenador do incidente, os analistas técnicos, o **encarregado de dados**, o **jurídico**, a **comunicação** e a direção da instituição.

**Critérios de correção**

- Integral: critica o desligamento pela perda de evidência volátil e pela demora; propõe isolamento e coleta por ordem de volatilidade com cadeia de custódia e *hashes*; normaliza corretamente os horários (11h52 e 22h58 em Brasília) e ordena a linha do tempo, identificando a exfiltração antes da criptografia; relaciona as atividades às fases do 800-61 Rev. 2 e às funções do CSF 2.0; identifica o prazo de três dias úteis a partir da confirmação, a comunicação à ANPD e aos titulares e os papéis (encarregado, jurídico, comunicação).
- Parcial: trata bem a contenção, mas erra a normalização ou omite as obrigações legais, ou vice-versa.
- Insuficiente: endossa a sugestão do técnico sem ressalvas ou desconhece a obrigação de comunicação.

### Questão 10

**Resposta esperada**

a) "Ataques bloqueados" é uma métrica de vaidade: conta eventos que os controles já resolvem (varreduras automatizadas, *spam*) e nada diz sobre a capacidade de detectar um adversário que passou pelas barreiras. A cobertura de 85% tem três armadilhas: conta a técnica como coberta só porque **existe** uma regra, sem nunca tê-la testado; trata todas as técnicas como iguais, embora uma regra possa detectar apenas um dos procedimentos possíveis; e mede contra a matriz inteira, e não contra as técnicas **priorizadas** pela inteligência de ameaças relevante para seguradoras. Logo, não significa "85% protegida". A diferença entre MTTD médio (40 h) e mediano (6 h) indica que poucos casos extremos, provavelmente incidentes detectados muito tarde, puxam a média para cima; a mediana mostra o caso típico, e os casos extremos merecem investigação própria. Precisão: 240 ÷ 2.400 = **10%**, ou seja, 90% de falsos positivos, um risco de fadiga de alertas. Exercício: cobertura validada (alerta correto ÷ técnicas priorizadas) = 7 ÷ 25 = **28%** antes e 15 ÷ 25 = **60%** depois; visibilidade (alerta + telemetria) = 15 ÷ 25 = **60%** antes e 21 ÷ 25 = **84%** depois. A cobertura real e testada era cerca de um terço da apresentada, e a melhoria é mensurável.

b) Ciclo do exercício: **planejar** com CTI (selecionar as técnicas dos grupos que atacam o setor, definir procedimentos, critérios de sucesso e RoE com o White Team); **emular** cada técnica em ambiente autorizado; **observar** se houve telemetria, alerta e resposta; **ajustar** (nova fonte de dados, regra, *playbook*); **retestar** após o ajuste, aqui em 30 dias. Estrutura do relatório final: sumário executivo (risco em linguagem de negócio, decisões pedidas, investimento); escopo, metodologia e limitações; **achados** priorizados por **risco** (probabilidade × impacto); **recomendações** com responsável, prazo e custo; **métricas** (cobertura validada, visibilidade, precisão, MTTD/MTTR medianos, taxa de reteste) com linha de base e metas; anexos técnicos. Exemplo de achado: "A-03 — Movimentação lateral por RDP com conta válida não gera alerta. Evidência: no exercício de 12/03, a técnica T1021.001 foi emulada às 10h14; o logon tipo 10 chegou ao SIEM, mas nenhuma regra disparou (telemetria sem alerta). Risco: alto (técnica usada pelos dois grupos priorizados; impacto em servidores de apólices). Recomendação: regra de primeiro par conta × servidor e de RDP de conta não administrativa, com reteste em 30 dias; responsável: engenharia de detecção; prazo: 30 dias; custo: esforço interno. Métrica: técnica passa a 'alerta' no reteste." A *layer* do Navigator antes/depois mostra as 25 técnicas coloridas por resultado (alerta, só telemetria, nada), e a comparação evidencia as 8 técnicas que mudaram de nível; os indicadores mostram a evolução (28% → 60%; 60% → 84%) e as 4 técnicas ainda sem registro tornam-se prioridade do próximo ciclo. O conselho recebe a resposta honesta à pergunta: a seguradora detecta hoje 60% das técnicas que mais a ameaçam, e não "está 85% protegida".

**Critérios de correção**

- Integral: critica "ataques bloqueados"; aponta ao menos duas armadilhas da cobertura; interpreta média × mediana; calcula 10%, 28% → 60% e 60% → 84% (com as definições de cobertura validada e visibilidade); descreve o ciclo emular → observar → ajustar → retestar com planejamento baseado em CTI; estrutura o relatório com achados, riscos, recomendações e métricas; redige um achado completo (evidência, técnica, risco, recomendação, responsável, prazo, métrica); usa o Navigator antes/depois.
- Parcial: crítica correta sem relatório estruturado, ou relatório sem análise do painel; erros nos cálculos de cobertura ou achado incompleto.
- Insuficiente: aceita os 85% como nível de proteção ou apresenta apenas lista de ferramentas.
