# Unidade 3 — Blue Team: detecção e resposta

Disciplina: Red Team & Blue Team Strategies  
Professor-conteudista: Afonso Cesar Lelis Brandão  
Prazo de entrega: 20/12/2026  
Template de origem: `documentos/Unidade 3/TEMPLATE - Unidade 3_nome da disciplina.docx`

> Versão de trabalho baseada na **ementa proposta** (`EMENTA.md`); ajustar quando o plano de aprendizagem oficial chegar.
> Recursos visuais indicados entre colchetes, como pede o template; a equipe de produção substitui pelas imagens finais.

## Aula 9 — Telemetria, registros e SIEM

### O que você verá nesta unidade

Na Unidade 2, acompanhamos o adversário: reconhecimento, exploração de vulnerabilidades, engenharia social e movimentação lateral. Em cada etapa, perguntamos que rastro ficava para trás. Agora é hora de vestir a camisa azul e responder à pergunta inversa: **como a defesa encontra esses rastros e reage a tempo?** Nesta unidade, você vai entender de onde vêm os dados que alimentam o SOC (registros, telemetria e SIEM); como transformar conhecimento sobre técnicas de ataque em regras de detecção testáveis, com apoio do EDR; como caçar ameaças que escaparam das regras, usando inteligência de ameaças; e como conduzir a resposta a um incidente, da contenção às lições aprendidas, incluindo as obrigações de comunicação previstas na LGPD. O objetivo é que você consiga projetar, em linhas gerais, a cadeia completa de detecção e resposta de uma organização — competência central para quem pretende atuar em um SOC, em engenharia de detecção ou em resposta a incidentes.

### Texto base

Imagine um condomínio com câmeras em todos os corredores, mas sem ninguém assistindo às gravações, e com o equipamento configurado para apagar tudo depois de 24 horas. As câmeras existem, mas não protegem ninguém. Muitas organizações vivem situação parecida com seus registros: os sistemas geram eventos o tempo todo, mas eles não são coletados, não são analisados ou são descartados antes de alguém precisar deles. Nesta aula, vamos entender como transformar esse fluxo de dados em capacidade de detecção.

#### Evento, registro e telemetria

Um **evento** é qualquer ocorrência observável em um sistema: um *login*, a criação de um processo, uma consulta DNS. O **registro** (*log*) é a anotação desse evento, com data, hora, origem e detalhes. **Telemetria** é o termo mais amplo para o conjunto de dados que sensores e sistemas enviam continuamente para análise. O guia NIST SP 800-92 define a gestão de registros como o processo de gerar, transmitir, armazenar, analisar e descartar esses dados — e lembra que cada etapa precisa ser planejada, não improvisada durante um incidente.

[Imagem 1 — Fluxo horizontal: fontes de dados (servidores, estações, *firewall*, nuvem) → coleta → normalização → SIEM → alerta → analista. Texto alternativo: "Fluxograma do caminho de um registro, da fonte ao analista do SOC". Pode ser recriado pela equipe a partir da descrição.]

#### Fontes de registro essenciais

Não existe monitoração sem saber **o que** monitorar. As fontes abaixo cobrem boa parte das técnicas que vimos na Unidade 2:

| Fonte | Exemplo de evento | O que revela |
|---|---|---|
| Windows (Segurança) | 4624 (*logon* bem-sucedido), 4625 (falha de *logon*), 4688 (criação de processo), 1102 (registro de auditoria apagado) | Uso de credenciais, força bruta, execução de comandos, tentativa de apagar rastros |
| Sysmon | ID 1 (processo, com linha de comando), ID 3 (conexão de rede), ID 22 (consulta DNS) | Comportamento detalhado do *endpoint* |
| *Firewall* e *proxy* | Conexões permitidas e bloqueadas, URLs acessadas | Comando e controle, exfiltração |
| DNS | Domínios consultados por cada máquina | Domínios recém-registrados, tunelamento |
| Nuvem e identidade | Trilhas de auditoria do provedor e do serviço de identidade | Criação de chaves, mudança de permissões, *logins* impossíveis |

O **Sysmon** (*System Monitor*), ferramenta gratuita da Microsoft, merece destaque: ele enriquece a telemetria do Windows com informações que o registro nativo não traz por padrão, como o *hash* do executável e o processo pai. Já o evento 4688 só registra a linha de comando se uma política específica estiver habilitada — um bom exemplo de que **ter a fonte não basta; é preciso configurá-la**.

[Imagem 2 — Captura de tela do Visualizador de Eventos do Windows exibindo um evento 4625, com os campos de conta, tipo de *logon* e endereço de origem destacados. Texto alternativo: "Visualizador de Eventos do Windows mostrando uma falha de logon com ID 4625". Captura própria em máquina de laboratório.]

#### O SIEM: normalizar, correlacionar e reter

O SIEM (*Security Information and Event Management*) centraliza os registros e executa três funções-chave. A **normalização** converte formatos diferentes em um esquema comum: o "usuário" do *firewall* e o "*TargetUserName*" do Windows passam a ocupar o mesmo campo, o que permite pesquisar todas as fontes de uma vez. Esquemas abertos, como o OCSF (*Open Cybersecurity Schema Framework*), buscam padronizar esse trabalho entre fornecedores.

A **correlação** combina eventos que, isolados, parecem inofensivos. Dez falhas de *logon* (4625) contra uma conta não significam muito; dez falhas seguidas de um *logon* bem-sucedido (4624) da mesma origem, em menos de cinco minutos, sugerem que uma senha foi descoberta. O SIEM também **enriquece** os eventos com contexto — geolocalização do IP, criticidade do ativo, cargo do usuário —, o que acelera a triagem.

A **retenção** define por quanto tempo os dados ficam disponíveis. Ela deve atender a requisitos legais e contratuais — o PCI DSS, por exemplo, exige guardar o histórico de auditoria por pelo menos 12 meses, com os 3 meses mais recentes disponíveis para análise imediata — e à realidade das investigações: se um invasor permaneceu semanas no ambiente, registros de apenas sete dias não contam a história do início.

[Imagem 3 — Gráfico de linha do tempo com eventos 4625 em sequência e um 4624 ao final, destacados como uma regra de correlação. Texto alternativo: "Linha do tempo de várias falhas de logon seguidas de um logon bem-sucedido". Pode ser recriado pela equipe.]

#### Fadiga de alertas: quando mais é menos

Coletar tudo e alertar sobre tudo parece seguro, mas produz o efeito contrário. Quando a maioria dos alertas é de falsos positivos, os analistas passam a fechá-los no automático — e o alerta verdadeiro se perde no meio da fila. Esse fenômeno, chamado **fadiga de alertas**, é um dos principais problemas operacionais dos SOCs. Por isso, a pergunta certa não é "quantos alertas geramos?", mas "quantos alertas conseguimos investigar com qualidade?".

#### Exemplo numérico: alertas *versus* capacidade

Um SOC recebe 1.800 alertas por dia. A triagem de cada um leva, em média, 10 minutos, o que exige 1.800 × 10 = 18.000 minutos, ou **300 horas de análise por dia**. A equipe N1 tem seis analistas (dois por turno), com cerca de 6 horas efetivas de triagem cada: 6 × 6 = 36 horas por dia. A capacidade real é de 36 × 60 ÷ 10 = **216 alertas por dia — apenas 12% do volume**. Suponha agora que 95% dos alertas venham de cinco regras ruidosas. Ajustando essas regras para cortar 90% do seu ruído, o volume cai para 1.800 − (0,95 × 1.800 × 0,9) ≈ 261 alertas por dia, muito mais próximo da capacidade. Ajustar regras costuma ser mais eficiente do que contratar mais analistas.

#### Pontos-chave

- Sem fontes de registro bem escolhidas e configuradas, não há detecção possível.
- Eventos como 4624, 4625 e 4688 e a telemetria do Sysmon são a base da monitoração de *endpoints* Windows.
- O SIEM normaliza, enriquece, correlaciona e retém dados de múltiplas fontes.
- A retenção deve atender à lei, aos contratos e ao tempo real das investigações.
- Volume de alertas acima da capacidade da equipe gera fadiga e alertas perdidos.

### Referências da aula

BRASIL. Lei nº 12.965, de 23 de abril de 2014. Estabelece princípios, garantias, direitos e deveres para o uso da Internet no Brasil (Marco Civil da Internet). *Diário Oficial da União*, Brasília, DF, 24 abr. 2014.

KENT, Karen; SOUPPAYA, Murugiah. *SP 800-92: guide to computer security log management*. Gaithersburg: NIST, 2006. DOI: 10.6028/NIST.SP.800-92.

MICROSOFT. *Sysmon*. Sysinternals. Disponível em: <https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon>. Acesso em: 13 nov. 2026.

PCI SECURITY STANDARDS COUNCIL. *Payment card industry data security standard: requirements and testing procedures*. Versão 4.0.1. [*S. l.*]: PCI SSC, 2024.

SANDERS, Chris; SMITH, Jason. *Applied network security monitoring: collection, detection, and analysis*. Waltham: Syngress, 2014.

### Roteiro da Videoaula 9 — "Um *login* às 2h da manhã: o SOC vai perceber?"

Duração-alvo: 15 a 20 minutos. Deck: unidade_3/slides/aula9.html (24 slides).

**Slides 1 a 3 — Capa, audiodescrição e sumário (0:00–0:40)**
Fala: "Olá! Começamos hoje a Unidade 3, em que trocamos de lado e vestimos a camisa azul. Nesta aula, vamos ver de onde vêm os dados que alimentam a defesa: registros, telemetria e SIEM. O sumário mostra o caminho, e quase todo tópico tem um laboratório para fazermos juntos."

**Slide 4 — O problema de hoje na Rede Tatame (0:40–2:00)**
Fala: "Imagine a Luiza Ferraz, analista nível 2 do SOC, o centro de operações de segurança da Rede Tatame, no plantão da madrugada de sexta-feira, 13 de novembro. Às 02:17, alguém entra no SRV-ERP-01, o servidor do sistema financeiro, com a conta da Carla Dias, depois de errar a senha dez vezes. A Carla está dormindo, e a fila do SOC já tem centenas de alertas, quase todos ruído. No mapa à direita, o caminho em destaque sai do notebook NB-FIN-031 e chega ao ERP, em vermelho. A pergunta da aula está no quadro amarelo: que registros a Rede Tatame precisa coletar, guardar e correlacionar para que o SOC perceba esse *login* a tempo, sem se afogar em alertas? Guarde essa pergunta, porque cada laboratório vai responder um pedaço dela."
[Take de apoio: sala de monitoramento à noite, analista diante de vários monitores — Envato]

**Slide 5 — O que você verá nesta unidade (2:00–2:30)**
Fala: "Na Unidade 2, acompanhamos o adversário. Agora a pergunta se inverte: como a defesa encontra os rastros e reage a tempo? A história do SRV-ERP-01 vai atravessar as quatro aulas. Hoje o SOC precisa enxergar o *login*; na Aula 10, escrevemos e testamos regras; na Aula 11, caçamos o que as regras não viram; e na Aula 12, conduzimos a resposta ao incidente."

**Slide 6 — Evento, registro e telemetria (2:30–3:10)**
Fala: "Um evento é qualquer ocorrência observável, como um *login* ou a criação de um processo. O registro, o *log*, é a anotação desse evento, e telemetria é o conjunto de dados que sensores enviam continuamente. O guia NIST SP 800-92 organiza a gestão de registros em cinco fases: gerar, transmitir, armazenar, analisar e descartar. Vamos ver essas fases em movimento agora."

**Slide 7 — Laboratório: o caminho de um registro, da fonte ao analista (3:10–4:30)**
Objetivo: mostrar por onde o evento das 02:14 precisa passar para virar trabalho do SOC. Responde à parte "coletar" da pergunta.
Na tela:
1. Clicar em "▶ Avançar". Passo "02:14:03 · Gerar": o nó Servidores acende.
2. "Avançar" de novo: passo "Transmitir". As quatro fontes da esquerda enviam pontos ao nó Coleta.
3. Avançar por "Normalizar", "Enriquecer e correlacionar" e "Analisar", um clique por vez.
4. Avançar por "Armazenar e descartar" e, por fim, "A câmera sem gravação", em que o nó DNS interno fica vermelho.
Fala: "O primeiro passo é o evento 4625, uma falha de *logon* da carla.dias, tipo 10, que é área de trabalho remota, vinda do endereço 10.10.20.31. Cada ponto que corre nas linhas é um evento em trânsito. Na normalização, reparem no texto embaixo: TargetUserName, do Windows, e usuario, do *firewall*, viram o mesmo campo user.name. Depois o SIEM acrescenta contexto, percebe as dez falhas seguidas de sucesso em 3 minutos e gera um alerta de severidade alta para o analista N1. O último passo mostra o problema mais comum: o DNS interno nunca foi configurado para enviar registros, então nada dele chega ao SIEM."
Atenção: o botão "⏯ Auto" avança sozinho; para gravar, prefira os cliques manuais, que dão tempo de ler o texto de cada passo. O botão "◀" volta um passo.
Conclusão: "Coletar significa configurar cada fonte. Uma fonte esquecida é uma câmera sem gravação."
[Tela: gravação do laboratório do slide 7]

**Slide 8 — Fontes de registro essenciais (4:30–5:10)**
Fala: "Esta tabela é o nosso cardápio de fontes. No Windows, os eventos 4624, 4625, 4688 e 1102; no Sysmon, os IDs 1, 3 e 22; depois *firewall* e *proxy*, DNS, nuvem e identidade. No nosso caso, o 4625 e o 4624 contam a história do *login*, e o Sysmon conta o que aconteceu depois dele."

**Slide 9 — Laboratório: que telemetria da Rede Tatame chega ao SOC (5:10–6:50)**
Objetivo: descobrir quais fontes da plataforma chegam ao SOC e quanto custa ligar mais uma. Responde a "coletar", com a restrição de custo.
Na tela (simulador da disciplina, já aberto na aba Telemetria):
1. Ler os indicadores do topo: "Fontes ligadas 7 de 10", "Ingestão por dia 32,8 GB" e "Custo por mês R$ 2.462".
2. Marcar as chaves "Heartbeat e firmware das catracas" e "Acesso a buckets e saída de rede". Os indicadores passam a 9 de 10, 34,5 GB por dia e R$ 2.586 por mês.
3. Abrir a aba "Filas e eventos" e clicar em "Iniciar", no topo. As partições do tópico tatame.eventos começam a contar mensagens.
4. Clicar em "Parar o encaminhador do SIEM" e observar as barras de atraso.
5. Clicar em "Religar o encaminhador do SIEM" para fechar.
Fala: "Cada linha da lista é uma fonte, com a taxa em eventos por segundo e as etiquetas das regras que dependem dela, como a R10 nas catracas. Ligar as catracas e a saída de rede soma 38 eventos por segundo, cerca de 1,6 GB a mais por dia e R$ 124 a mais por mês, valores fictícios do simulador. Na aba Filas e eventos, o Kafka é o barramento de mensagens: os sistemas publicam ali, e três consumidores leem, o CEP, o *data lake* e o siem-forwarder. Quando eu paro o encaminhador, a barra do siem-forwarder fica vermelha e o *lag*, o atraso medido em mensagens, cresce sem parar. Os eventos continuam guardados no Kafka, mas o SOC deixa de vê-los."
Atenção: o simulador roda em tempo acelerado (1 s = 15 s); o *lag* leva uns 10 segundos para ficar visível. Se algo travar, use "Reiniciar", no topo.
Conclusão: "Cada fonte ligada custa dinheiro; cada fonte desligada ou parada é um ponto cego para a Luiza."
[Tela: gravação do laboratório do slide 9, no simulador]

**Slide 10 — Ter a fonte não basta: é preciso configurá-la (6:50–7:20)**
Fala: "O Sysmon, ferramenta gratuita da Microsoft, acrescenta o que o registro nativo não traz por padrão. No evento ID 1, ele grava a linha de comando, o *hash* do executável e o processo pai. O 4688 nativo só traz a linha de comando se uma política estiver habilitada. Vamos conferir isso numa máquina de laboratório."

**Slide 11 — Laboratório: falhas, sucesso e processo no Windows (7:20–9:00)**
Objetivo: ver os eventos que um *login* como o das 02:17 deixa numa máquina Windows. Responde a "o que coletar".
Na tela (PowerShell da VM isolada LAB-WIN11; clicar em "▶ Próximo comando" seis vezes):
1. Get-WinEvent no registro Security, filtrando o Id 4625.
2. Get-WinEvent filtrando o Id 4624 da conta aluno.
3. Instalação do Sysmon com o arquivo sysmonconfig.xml.
4. Start-Process notepad.exe.
5. Leitura do evento ID 1 do Sysmon que menciona o notepad.
6. Get-ItemProperty na chave de auditoria, procurando ProcessCreationIncludeCmdLine_Enabled.
Fala: "O primeiro comando lê as três últimas falhas e monta cinco colunas: hora, Id, conta, tipo de *logon* e origem. A conta está na propriedade 5, o tipo na 10 e a origem na 19 do evento. Aparecem três 4625 da conta aluno, tipo 2, que é teclado, vindas de 127.0.0.1, a própria máquina. No 4624, as posições mudam: o tipo fica na 8 e a origem na 18. O resultado é um sucesso às 10:02:52. Três falhas em 15 segundos e um sucesso 11 segundos depois: aqui foi só o aluno digitando errado. No caso da Rede Tatame, o tipo seria 10, área de trabalho remota, e a origem seria o notebook do financeiro. Em seguida instalamos o Sysmon; as linhas verdes confirmam o serviço e o *driver* iniciados. Abrimos o Bloco de Notas e lemos o evento 1. As linhas destacadas são Image, CommandLine, Hashes, com o SHA-256, e ParentImage, que mostra o PowerShell como processo pai. O último comando termina em erro de propósito: a política que coloca a linha de comando no 4688 não existe nesta máquina."
Atenção: a saída é simulada e representa uma VM isolada; os horários são da VM, não da madrugada do caso. "⏭ Executar tudo" roda o roteiro inteiro, e "⟲ Reiniciar" limpa o terminal.
Conclusão: "O 4625 e o 4624 contam o *login*; o Sysmon conta o que veio depois. E uma fonte sem configuração não responde à pergunta da investigação."
[Tela: gravação do laboratório do slide 11]

**Slide 12 — O SIEM: normalizar, enriquecer, correlacionar e reter (9:00–9:40)**
Fala: "O SIEM, *Security Information and Event Management*, faz quatro trabalhos com esses registros. Ele normaliza formatos diferentes num esquema comum, enriquece com contexto, correlaciona eventos que isolados parecem inofensivos e retém os dados pelo tempo definido. Dez falhas seguidas de um sucesso, da mesma origem, em menos de cinco minutos: esse é exatamente o padrão da carla.dias."

**Slide 13 — Laboratório: normalizar dois formatos e correlacionar (9:40–11:30)**
Objetivo: juntar Windows e *firewall* num formato comum e achar o padrão das 02:17. Responde a "correlacionar".
Na tela (VS Code, pasta normalizacao):
1. Com normalizar.py aberto, mostrar as linhas destacadas de 5 a 12 (MAPA_WINDOWS) e a linha 30 (user.name no *firewall*).
2. No explorador, abrir amostras/windows_seguranca.jsonl e amostras/firewall.log.
3. Clicar no botão "Normalizar", na barra do terminal.
4. Abrir correlacao.py, mostrar as linhas destacadas 6, 7, 13, 14, 18 e 19 e clicar em "Correlacionar".
Fala: "O dicionário MAPA_WINDOWS diz que TimeCreated vira @timestamp, TargetUserName vira user.name e IpAddress vira source.ip. A linha 13 traduz o código: 4624 é success e 4625 é failure. A função de_firewall quebra cada linha do *log* em pares chave=valor e preenche os mesmos campos; a linha 30 põe o usuario do *firewall* em user.name. A função carregar junta os dois arquivos e ordena tudo pela hora. Ao rodar, a saída diz 18 eventos normalizados: 15 do Windows e 3 do *firewall*. O primeiro é do *firewall*, às 02:13:58: a conexão permitida do notebook 10.10.20.31 para a porta 3389, de área de trabalho remota, já com user.name igual a carla.dias. Agora a correlação. A linha 6 define o limiar de 10 falhas, e a linha 7, a janela de 5 minutos. Para cada par de origem e conta, o programa guarda os horários das falhas numa fila; as linhas 13 e 14 descartam as falhas mais antigas que a janela. Quando chega um sucesso, as linhas 18 e 19 decidem: com 10 ou mais falhas guardadas, sai o alerta. O resultado, em vermelho, mostra carla.dias no SRV-ERP-01, 10 falhas e sucesso às 02:17:12 a partir de 10.10.20.31. A ana.lima errou duas vezes e entrou, ficando abaixo do limiar, e o caio.mendes entrou sem errar."
Atenção: o código é ilustrativo e roda apenas na simulação. Os nomes de campos imitam o ECS (*Elastic Common Schema*). Em telas estreitas, os botões da barra do terminal passam para uma segunda linha.
Conclusão: "Com campos comuns, uma regra simples, dez falhas e um sucesso em cinco minutos, encontra o *login* das 02:17."
[Tela: gravação do laboratório do slide 13]

**Slide 14 — Laboratório: os mesmos eventos dentro do SIEM (11:30–13:00)**
Objetivo: confirmar no SIEM o que houve às 02:17 e até quando dá para olhar para trás. Responde a "correlacionar" e a "guardar".
Na tela (console do SIEM; a busca 1 roda sozinha ao abrir o slide):
1. Ler o resultado de "1. Falhas de logon por origem".
2. Clicar em "2. Falhas seguidas de sucesso".
3. Clicar em "3. Enriquecer o evento".
4. Clicar em "4. Até quando dá para olhar?", no grupo Retenção.
Fala: "A busca 1 filtra o evento 4625 e conta as falhas por origem, conta e servidor. São 214 eventos no dia. O histograma tem uma barra por hora, e a das 02h está destacada. Quem lidera é a conta de serviço svc-backup, com 96 falhas, 4 por hora o dia inteiro, por causa de uma senha vencida: volume alto, mas ruído conhecido. A busca 2, em EQL, procura a sequência de 10 falhas seguidas de um sucesso em até 5 minutos, para a mesma origem e conta. Ela encontra uma única sequência, das 02:14:03 às 02:17:12, com severidade alta. A busca 3 cruza o *login* com três tabelas, de ativos, de RH e de rede. O resultado diz que o SRV-ERP-01 tem criticidade alta, que a carla.dias é analista do financeiro com horário usual das 8h às 18h e que a origem é o notebook NB-FIN-031, na sede. A busca 4 mostra o registro mais antigo e o mais recente de cada índice. Windows e *firewall* têm 365 dias; o *proxy* tem só 7, porque o equipamento foi trocado há uma semana."
Atenção: o texto da consulta é digitado aos poucos antes do resultado; espere a tabela completar antes de comentar. O botão "Pesquisar" repete a busca selecionada.
Conclusão: "Volume alto não indica ataque. O enriquecimento separa o ruído do svc-backup da ameaça na conta da carla.dias."
[Tela: gravação do laboratório do slide 14]

**Slide 15 — Laboratório: a catraca adulterada, sem e com a fonte certa (13:00–14:40)**
Objetivo: provar, na plataforma, que uma regra só dispara se a fonte estiver ligada e a regra ativa. Responde a "coletar" e "correlacionar" juntos.
Na tela (simulador na aba Cenários, com a fonte das catracas e a regra R10 desligadas):
1. No cartão "Catraca adulterada", clicar em "Iniciar cenário" e esperar os três passos, cerca de 20 segundos.
2. Na aba Telemetria, ligar "Heartbeat e firmware das catracas".
3. Na aba Regras do CEP, ligar "R10 · Catraca fora do padrão (volume ou firmware)".
4. Voltar a Cenários e clicar em "Repetir com as fontes e regras atuais".
5. Na aba SOC, clicar em "Investigar" no alerta da R10.
Fala: "Na primeira rodada, os dois primeiros passos, os *heartbeats* dez vezes por segundo e o *firmware* não assinado, recebem a etiqueta vermelha 'não detectado': a fonte das catracas está desligada, então ninguém viu nada. O terceiro passo, os *check-ins* falsos, fica amarelo, 'visto nos logs, sem alerta'. O *log* do API *gateway* registrou, mas nenhuma regra olha para isso. Embaixo de cada passo aparecem a técnica do ATT&CK, a fonte e a regra. Depois de ligar a fonte e a R10, a segunda rodada marca os dois primeiros passos como 'detectado'. No SOC, o painel de investigação mostra a lógica da regra e a linha do tempo correlacionada."
Atenção: o alerta chega alguns segundos depois do passo, porque a regra precisa correlacionar. Na aba SOC também pode aparecer um alerta da R11 sobre a conta svc-backup; ele é benigno e será tratado na Aula 12.
Conclusão: "Para avisar o SOC, a Rede Tatame precisa das duas coisas: a fonte ligada e a regra ativa."
[Tela: gravação do laboratório do slide 15, no simulador]

**Slide 16 — Por quanto tempo guardar os registros (14:40–15:10)**
Fala: "A retenção atende à lei, aos contratos e ao tempo real das investigações. O PCI DSS exige 12 meses de histórico, com os 3 mais recentes disponíveis para análise imediata. Se o invasor ficou semanas no ambiente, sete dias de registro não contam o começo da história."

**Slide 17 — Laboratório: o início da invasão ainda está nos registros? (15:10–16:10)**
Objetivo: decidir quanto guardar. Responde a "guardar".
Na tela:
1. Partir dos valores iniciais: pesquisa imediata de 7 dias, retenção total de 7 dias e invasão de 30 dias atrás.
2. Arrastar "Retenção total (dias)" até 365 e "Pesquisa imediata (dias)" até 90.
3. Arrastar "Invasão começou há (dias)" até 200.
Fala: "A faixa clara é o que dá para pesquisar na hora, a faixa mais fraca é o arquivo de longo prazo, e a linha vermelha marca o dia da entrada do invasor. Com sete dias, os dois primeiros indicadores ficam vermelhos, e a frase embaixo avisa que os primeiros 23 dias da invasão já foram descartados. Com 365 dias de retenção e 90 de pesquisa imediata, o PCI DSS passa a ser atendido, e o volume guardado chega a 7,3 TB, a 20 GB por dia. Se a invasão começou há 200 dias, o início existe, mas está no arquivo: será preciso restaurá-lo antes de pesquisar."
Atenção: a retenção total nunca fica menor que a pesquisa imediata; o controle se ajusta sozinho.
Conclusão: "A Rede Tatame guarda 12 meses no SIEM, e é isso que permite reconstruir o começo do caso do ERP."
[Tela: gravação do laboratório do slide 17]

**Slides 18 e 19 — Fadiga de alertas e o exemplo numérico (16:10–16:50)**
Fala: "Coletar tudo e alertar sobre tudo produz o efeito contrário: quando quase tudo é falso positivo, o analista fecha alertas no automático. Vejam a conta. São 1.800 alertas por dia vezes 10 minutos, ou 300 horas de análise; seis analistas com 6 horas efetivas somam 36 horas, ou 216 alertas, 12% do volume. Se 95% dos alertas vêm de cinco regras ruidosas e o ajuste corta 90% do ruído delas, a fila cai para cerca de 261."

**Slide 20 — Laboratório: calculadora de alertas e capacidade do SOC (16:50–17:50)**
Objetivo: verificar se o alerta das 02:17 cabe na fila. Responde a "sem se afogar em alertas".
Na tela:
1. Ler os valores iniciais: demanda de 300 h por dia (1.800 alertas), capacidade de 36 h por dia (216 alertas) e cobertura de 12%.
2. Subir "Analistas N1" de 6 para 8.
3. Voltar a 6 e subir "Ruído cortado nessas regras" para 90%.
4. Baixar "Minutos de triagem por alerta" de 10 para 6.
Fala: "Com oito analistas, a capacidade sobe para 48 horas, ou 288 alertas, e a cobertura vai só a 16%. Com seis analistas e 90% do ruído cortado, a demanda cai para 43,5 horas e 261 alertas, e a cobertura salta para 82,8%. Com triagem de 6 minutos, a equipe tria 360 alertas, a cobertura chega a 100% e o indicador mostra 'cabe tudo'. As barras de baixo comparam os alertas recebidos com os que cabem."
Conclusão: "Ajustar regras rende mais do que contratar, e é isso que garante que o alerta da carla.dias seja lido."
[Tela: gravação do laboratório do slide 20]

**Slide 21 — De volta ao problema (17:50–18:50)**
Fala: "Voltemos à Luiza. Os quatro cartões resumem o que vimos: coletar as fontes certas, com 4624, 4625 e Sysmon chegando ao SIEM; normalizar e correlacionar, para a regra achar a carla.dias às 02:17:12; guardar 12 meses; e caber na equipe, com a fila reduzida para cerca de 261 alertas. Respondendo à pergunta da aula: a Rede Tatame precisa coletar os eventos de autenticação e de processos de servidores e notebooks, levá-los ao SIEM em formato comum, correlacionar falhas seguidas de sucesso, guardar 12 meses e manter o volume de alertas dentro da capacidade do SOC."

**Slides 22 a 24 — Pontos-chave, referências e encerramento (18:50–19:30)**
Fala: "Para levar desta aula: sem fontes bem escolhidas e configuradas, não há detecção; o SIEM normaliza, enriquece, correlaciona e retém; e alerta demais vira alerta perdido. O SOC enxergou o *login*, mas ainda falta saber se uma regra dispararia antes do estrago. Na próxima aula, vamos escrever, testar e medir regras de detecção."

[Envato: "security operations center night", "server logs scrolling screen", "data center cables". Slides de apoio: mini-mapa do slide 4 e cartões do slide 21.]

## Aula 10 — Engenharia de detecção e EDR

### Texto base

Na aula anterior, vimos que o SIEM recebe dados de muitas fontes. Mas dados só viram alerta quando alguém escreve uma **regra** que diz o que procurar. Durante muito tempo, essas regras foram criadas de forma artesanal, diretamente na interface da ferramenta, sem documentação nem testes. A **engenharia de detecção** surgiu para tratar a criação de detecções com o mesmo rigor com que a engenharia de *software* trata o código.

#### O ciclo de vida de uma detecção

Uma detecção bem construída percorre etapas previsíveis: (1) **requisito** — qual comportamento adversário queremos detectar e por quê (por exemplo, uma técnica ATT&CK usada por grupos que ameaçam o setor); (2) **pesquisa** — que rastros essa técnica deixa e em quais fontes; (3) **desenvolvimento** da regra; (4) **teste** com dados reais ou simulados; (5) **implantação**; (6) **ajuste** contínuo com base nos resultados; e (7) **aposentadoria**, quando a regra deixa de fazer sentido. Esse ciclo transforma cada técnica emulada pelo Red Team, como as que estudamos na Unidade 2, em uma melhoria verificável.

[Imagem 1 — Ciclo com sete etapas em círculo: requisito, pesquisa, desenvolvimento, teste, implantação, ajuste e aposentadoria. Texto alternativo: "Diagrama circular do ciclo de vida de uma regra de detecção". Pode ser recriado pela equipe.]

#### Detecção como código e o padrão Sigma

Na abordagem de **detecção como código** (*detection-as-code*), as regras ficam em um repositório com controle de versão, passam por revisão de pares e são validadas automaticamente antes de chegar à produção. Isso permite saber quem alterou uma regra, quando e por quê — e desfazer uma mudança que gerou ruído.

O **Sigma** é um formato aberto, em YAML, para escrever regras de detecção independentes de fornecedor. Uma regra Sigma pode ser convertida, por ferramentas do próprio projeto, para a linguagem de consulta de diferentes SIEMs. O exemplo didático a seguir detecta o uso do utilitário `vssadmin` para apagar cópias de sombra do Windows — comportamento frequente pouco antes da criptografia por *ransomware* (técnica T1490 — *Inhibit System Recovery*):

```yaml
title: Exclusão de cópias de sombra com vssadmin
status: experimental
description: Detecta o vssadmin apagando cópias de sombra, ação comum antes de ransomware
references:
  - https://attack.mitre.org/techniques/T1490/
tags:
  - attack.impact
  - attack.t1490
logsource:
  category: process_creation
  product: windows
detection:
  selection:
    Image|endswith: '\vssadmin.exe'
    CommandLine|contains|all:
      - 'delete'
      - 'shadows'
  condition: selection
falsepositives:
  - Rotinas legítimas de administração de backup
level: high
```

Observe que a regra declara a **fonte de dados** necessária (criação de processos, que pode vir do evento 4688 ou do Sysmon ID 1), o **mapeamento ATT&CK**, a lógica de detecção e os **falsos positivos esperados**. Essa documentação embutida é o que permite medir a cobertura, como fizemos na Aula 2.

[Imagem 2 — *Pipeline* de detecção como código: repositório Git → revisão de pares → testes automatizados → conversão Sigma → SIEM em produção. Texto alternativo: "Esteira de integração contínua aplicada a regras de detecção". Pode ser recriado pela equipe.]

#### Tipos de detecção

| Tipo | Como funciona | Vantagem | Limitação |
|---|---|---|---|
| Indicador (IOC) | Compara com *hashes*, IPs ou domínios conhecidos | Simples e precisa | O adversário troca o indicador com facilidade |
| Comportamental | Procura a técnica, como no exemplo acima | Resiste a variações de ferramenta | Exige conhecimento do ambiente para reduzir ruído |
| Anomalia | Compara com uma linha de base estatística | Encontra o desconhecido | Muitos falsos positivos se a base for instável |
| Correlação | Combina eventos de fontes diferentes | Aumenta a confiança | Depende de normalização de qualidade |

#### Testar antes de confiar

Uma regra nunca testada é apenas uma hipótese. Projetos abertos como o **Atomic Red Team** oferecem testes pequenos, mapeados ao ATT&CK, que reproduzem técnicas em laboratório para verificar se a regra dispara. Dois indicadores orientam o ajuste: a **precisão** (dos alertas gerados, quantos eram verdadeiros) e a **sensibilidade** ou *recall* (dos ataques que ocorreram, quantos foram detectados). Ajustar uma regra quase sempre é uma troca entre os dois.

#### EDR: os olhos dentro do *endpoint*

O **EDR** (*Endpoint Detection and Response*) é um agente instalado em computadores e servidores que registra, de forma contínua, criação de processos, alterações em arquivos e no registro do sistema, conexões de rede e carregamento de módulos. Diferentemente do antivírus tradicional, centrado em assinaturas de arquivos, o EDR reconstrói a **árvore de processos** — por exemplo, um documento do Word que abriu o PowerShell, que baixou um executável. Além de detectar, ele permite **responder**: isolar a máquina da rede, encerrar processos e coletar evidências remotamente. Como adversários tentam desativar esses agentes, a saúde do próprio sensor também precisa ser monitorada. Para relacionar técnicas defensivas às ofensivas, a MITRE mantém o **D3FEND**, uma base de conhecimento de contramedidas complementar ao ATT&CK.

[Imagem 3 — Árvore de processos de um EDR: WINWORD.EXE → powershell.exe → executável desconhecido, com o último nó destacado em vermelho. Texto alternativo: "Árvore de processos mostrando o Word iniciando o PowerShell, que executa um arquivo suspeito". Pode ser recriado pela equipe.]

#### Exemplo numérico: precisão de uma regra

Em 30 dias, uma regra de detecção de PowerShell suspeito disparou 400 vezes; a investigação mostrou que 20 alertas eram verdadeiros. A precisão é 20 ÷ 400 = **5%**: de cada 20 alertas, 19 são desperdício. Ao analisar os falsos positivos, a equipe percebeu que 350 vinham do mesmo *script* de inventário e criou uma exceção restrita a ele. No mês seguinte, com o mesmo cenário, a regra disparou 40 vezes, com 19 verdadeiros: precisão de 19 ÷ 40 = **47,5%**. Porém, um ataque real deixou de ser detectado, e a sensibilidade caiu de 100% para 19 ÷ 20 = 95%. Vale a troca? Provavelmente sim, desde que a lacuna seja coberta por outra regra — e que a exceção seja a mais específica possível.

#### Pontos-chave

- Engenharia de detecção aplica requisitos, testes e versionamento à criação de regras.
- O Sigma permite escrever regras portáveis entre SIEMs, documentando fonte, técnica e falsos positivos.
- Detecções comportamentais resistem melhor a mudanças do adversário do que indicadores.
- Precisão e sensibilidade orientam o ajuste das regras.
- O EDR une telemetria detalhada do *endpoint* e capacidade de resposta.

### Referências da aula

MITRE. *Inhibit system recovery (T1490)*. MITRE ATT&CK. Disponível em: <https://attack.mitre.org/techniques/T1490/>. Acesso em: 13 nov. 2026.

MITRE. *MITRE D3FEND*. Disponível em: <https://d3fend.mitre.org/>. Acesso em: 13 nov. 2026.

RED CANARY. *Atomic Red Team*. Disponível em: <https://github.com/redcanaryco/atomic-red-team>. Acesso em: 13 nov. 2026.

SIGMAHQ. *Sigma: generic signature format for SIEM systems*. Disponível em: <https://github.com/SigmaHQ/sigma>. Acesso em: 13 nov. 2026.

### Roteiro da Videoaula 10 — "A regra dispararia antes da criptografia?"

Duração-alvo: 15 a 20 minutos. Deck: unidade_3/slides/aula10.html (22 slides).

**Slides 1 a 3 — Capa, audiodescrição e sumário (0:00–0:30)**
Fala: "Olá! Na aula passada, o SOC passou a enxergar o *login* das 02:17. Hoje vamos para a engenharia de detecção e o EDR: como escrever, testar e medir as regras que geram esses alertas."

**Slide 4 — O problema de hoje na Rede Tatame (0:30–1:50)**
Fala: "Conheça o Rafael Tavares, engenheiro de detecção da Rede Tatame. Ele escreve e mantém as regras que geram alertas para o SOC. O EDR, o agente que registra os processos de cada máquina, mostrou a origem do *login* da Aula 9: dias antes, um documento do Word aberto no notebook NB-FIN-031 iniciou o PowerShell. A CISO, Marina Prado, quer uma prova. Se o invasor apagar as cópias de sombra do servidor, passo que antecede a criptografia num *ransomware*, alguma regra dispara? Ninguém testou, e a regra de PowerShell já gera 400 alertas por mês. No mapa, o EDR, o motor de regras e o SOC estão em destaque. A pergunta da aula: como o Rafael transforma uma técnica de ataque numa regra testada, que dispara quando o ataque acontece e não afoga o SOC?"
[Take de apoio: engenheiro revisando código em dois monitores — Envato]

**Slide 5 — O ciclo de vida de uma detecção (1:50–2:30)**
Fala: "Uma detecção tem ciclo de vida: requisito, pesquisa, desenvolvimento, teste, implantação, ajuste e aposentadoria. É esse ciclo que transforma cada técnica emulada pelo Red Team, como as da Unidade 2, numa melhoria verificável. Vamos percorrê-lo com a regra das cópias de sombra."

**Slide 6 — Laboratório: uma detecção da ideia à aposentadoria (2:30–3:50)**
Objetivo: ver as etapas por que a regra do Rafael precisa passar. Responde a "como transformar a técnica em regra".
Na tela:
1. Clicar em "▶ Avançar": passo "Origem". O nó roxo do centro, "CTI e Red Team", acende.
2. Avançar por "1. Requisito", "2. Pesquisa", "3. Desenvolvimento" e "4. Teste", um clique por vez.
3. Avançar por "5. Implantação" e "6. Ajuste", em que a linha tracejada "volta ao código" fica amarela.
4. Avançar até "7. Aposentadoria".
Fala: "O requisito nasce de um relatório de inteligência e do último exercício do Red Team: grupos de *ransomware* apagam cópias de sombra antes de criptografar. Isso vira a técnica T1490, *Inhibit System Recovery*, com severidade alta. Na pesquisa, o Rafael descobre que a técnica deixa rastro na criação de processos, no 4688 com linha de comando ou no Sysmon ID 1. A regra é escrita em Sigma, testada com o Atomic Red Team numa máquina isolada e publicada pela esteira. No ajuste, uma rotina de *backup* legítima gera alertas, e a exceção volta ao desenvolvimento para passar de novo pelos testes. Na aposentadoria, a regra é desativada com o motivo registrado."
Atenção: os passos ficam em círculo; prefira os cliques manuais ao botão "⏯ Auto".
Conclusão: "Toda regra passa por teste antes de entrar e volta ao código quando precisa de ajuste."
[Tela: gravação do laboratório do slide 6]

**Slides 7 e 8 — Detecção como código e anatomia de uma regra Sigma (3:50–5:00)**
Fala: "Na detecção como código, as regras ficam num repositório Git, passam por revisão de pares e por testes automáticos antes da produção. Dá para saber quem mudou o quê e desfazer uma mudança ruidosa. O Sigma é um formato aberto, em YAML, independente de fornecedor. Nesta regra, logsource diz que a fonte é criação de processos no Windows. Em detection, a seleção exige que Image termine em vssadmin.exe e que a linha de comando contenha as duas palavras, delete e shadows. O campo falsepositives já avisa sobre rotinas legítimas de *backup*, e level marca severidade alta."

**Slide 9 — Laboratório: regra, teste e conversão no mesmo repositório (5:00–7:00)**
Objetivo: escrever a regra das cópias de sombra como código, com testes. Responde a "regra testada".
Na tela (VS Code, pasta deteccoes):
1. Com a regra .yml aberta, apontar as linhas destacadas 14 a 19, o bloco detection.
2. Abrir tests/sigma_lite.py e mostrar as linhas 5 a 12, a função _casa.
3. Abrir tests/test_vssadmin.py e depois tests/eventos/positivos.json e negativos.json.
4. Clicar em "Rodar testes".
5. Clicar em "Para SPL" e depois em "Para KQL".
6. Abrir .github/workflows/deteccoes.yml.
Fala: "O sigma_lite.py é um avaliador mínimo de Sigma, feito só para os testes. A função _casa põe tudo em minúsculas, porque o Sigma compara sem diferenciar maiúsculas. Depois aplica o modificador: endswith compara o fim, contains procura o trecho, e all exige que todos os trechos apareçam; sem all, basta um. O arquivo de teste carrega a regra e roda duas famílias de casos. Os positivos precisam disparar: o atomic-T1490-1 e uma variação toda em maiúsculas. Os negativos precisam ficar quietos: listar cópias, criar uma cópia e um outro programa, o backup.exe, com 'shadows' na linha de comando. Por que o backup.exe não dispara? Porque a Image dele não termina em vssadmin.exe. A saída mostra 'collected 5 items' e os cinco testes como PASSED, terminando em '5 passed'. Agora a conversão. Para SPL, o *pipeline* sysmon traduz a categoria process_creation para EventID=1. Para KQL, a mesma lógica vira uma consulta na tabela DeviceProcessEvents, com outros nomes de campo. O arquivo de *workflow* mostra a esteira: a cada *pull request*, ela roda sigma check, pytest e a conversão."
Atenção: os testes e as conversões são simulados na tela; os comandos são os reais do sigma-cli e do pytest. Em telas estreitas, os botões da barra do terminal passam para uma segunda linha.
Conclusão: "A regra tem testes que rodam a cada mudança, e a mesma lógica roda em SIEMs diferentes sem ser reescrita."
[Tela: gravação do laboratório do slide 9]

**Slides 10 e 11 — Tipos de detecção e testar antes de confiar (7:00–8:00)**
Fala: "A tabela compara quatro tipos de detecção. Indicadores são simples, mas o adversário troca de *hash* ou de IP com facilidade. A detecção comportamental, como a do vssadmin, resiste a mudanças de ferramenta. Anomalia acha o desconhecido, com risco de ruído, e correlação aumenta a confiança. E uma regra nunca testada é só uma hipótese. Duas medidas guiam o ajuste: precisão, quantos alertas eram verdadeiros, e sensibilidade, quantos ataques foram detectados. Os testes atômicos rodam somente em máquina virtual isolada, com *snapshot*."

**Slide 12 — Laboratório: a regra dispara quando a técnica acontece? (8:00–9:40)**
Objetivo: provar que a regra dispara quando a técnica acontece. Responde a "dispara quando o ataque acontece".
Na tela (PowerShell da VM isolada LAB-WIN11; clicar em "▶ Próximo comando" cinco vezes):
1. Invoke-AtomicTest T1490 -ShowDetailsBrief.
2. Invoke-AtomicTest T1490 -TestNumbers 1 -CheckPrereqs.
3. Invoke-AtomicTest T1490 -TestNumbers 1.
4. Get-WinEvent no registro do Sysmon, procurando o evento 1 do vssadmin.
5. Restore-VMSnapshot, no hospedeiro, com o *snapshot* limpo-2026-11-13.
Fala: "A linha cinza do começo lembra que a VM só tem rede *host-only* e que o *snapshot* foi criado antes do teste. O primeiro comando só lista os testes da técnica, sem executar nada; usamos o T1490-1. O segundo confere os pré-requisitos. O terceiro roda o teste, e as linhas amarelas marcam início e fim. Para a defesa, o que importa é o rastro. O quarto comando lê o evento 1 do Sysmon, e as linhas destacadas são Image, terminando em vssadmin.exe, e CommandLine, com delete shadows: os dois campos que a regra Sigma verifica. Na linha azul, o SIEM gera o alerta 'Exclusão de cópias de sombra com vssadmin', nível *high*, às 14:22:09, dois segundos depois do evento das 14:22:07. O último comando devolve a VM ao estado limpo."
Atenção: deixe claro que o teste roda apenas em laboratório isolado, com autorização; a saída do utilitário foi omitida de propósito.
Conclusão: "A técnica aconteceu, a telemetria chegou e a regra disparou em 2 segundos. Agora existe prova."
[Tela: gravação do laboratório do slide 12]

**Slide 13 — Laboratório: ligar uma regra e provar que ela dispara (9:40–11:20)**
Objetivo: ver, na plataforma, que uma regra desligada deixa o ataque passar. Responde a "regra testada" no ambiente da Rede Tatame.
Na tela (simulador aberto na aba Regras do CEP, com a R3 desligada):
1. Ler o cartão "R3 · Token lendo fichas de muitos alunos diferentes (BOLA)" e a lógica embaixo dele.
2. Abrir a aba Cenários e clicar em "Iniciar cenário" no cartão "Abuso da API do app". Esperar os quatro passos, cerca de 30 segundos.
3. Voltar a Regras do CEP e ligar a R3.
4. Em Cenários, clicar em "Repetir com as fontes e regras atuais".
5. Na aba SOC, clicar em "Investigar" no alerta da R3. Depois, em Regras do CEP, ver as barras de disparos por regra.
Fala: "BOLA é quando um usuário lê objetos de outros trocando o identificador na URL. A lógica da R3 conta quantas fichas diferentes um mesmo *token* lê em um minuto e alerta acima de 20, quando a ficha não é do dono do *token*. Na primeira rodada, o passo das 2.000 tentativas de *login* é detectado pela R2, que já estava ligada. O passo '14 contas entram' fica amarelo, 'visto nos logs, sem alerta', e os dois passos de leitura de fichas também, porque a R3 está desligada. São 1.300 fichas lidas em 6 minutos, incluindo responsáveis de alunos menores. Na segunda rodada, os dois passos de leitura viram 'detectado', com severidade crítica, e o SOC mostra a linha do tempo correlacionada."
Atenção: o alerta chega alguns segundos depois do passo. Se faltar tempo, troque a velocidade para "1 s = 1 min". O passo "14 contas entram" continua sem regra, e isso é proposital.
Conclusão: "Uma regra só protege depois de ligada e testada com o cenário, e o passo sem regra mostra qual é a próxima regra a escrever."
[Tela: gravação do laboratório do slide 13, no simulador]

**Slide 14 — EDR: os olhos dentro do *endpoint* (11:20–11:50)**
Fala: "O EDR, *Endpoint Detection and Response*, é um agente que registra continuamente processos, arquivos, registro do sistema e conexões. Ele reconstrói a árvore de processos e permite responder: isolar a máquina, encerrar processos e coletar evidências. Como o adversário tenta desligar esses agentes, a saúde do sensor também precisa ser monitorada."

**Slide 15 — Laboratório: do alerta à resposta no console do EDR (11:50–13:30)**
Objetivo: usar o EDR para entender o alerta e responder. Responde a "o que fazer quando a regra dispara".
Na tela (console "EDR · Console Rede Tatame", com o alerta A-2291 aberto):
1. Ler a árvore do A-2291, no LAB-WIN11.
2. Clicar em "Office iniciou interpretador de comandos" (A-2292, NB-FIN-031).
3. Clicar em "Isolar máquina", depois em "Encerrar processo" e em "Coletar evidências".
4. Clicar em "Sensor sem comunicação" (A-2293, SRV-ARQ-01) e em "Abrir chamado para a TI".
Fala: "O topo mostra 3 alertas abertos e 148 de 149 sensores ativos. O A-2291 é o nosso teste atômico: explorer, PowerShell com Invoke-AtomicTest, cmd e, em vermelho, o vssadmin. O A-2292 é o caso real. A árvore mostra OUTLOOK.EXE, depois o WINWORD.EXE abrindo o arquivo repasse_academias_outubro.docm, depois o powershell.exe em vermelho. Do PowerShell saem uma conexão para 198.51.100.23 na porta 443 e o arquivo fatura_0311.exe, sem assinatura. As técnicas são T1204.002, execução pelo usuário, e T1059.001, PowerShell. Ao isolar, a etiqueta muda para 'isolada da rede', e o registro diz que só o canal com o console do EDR continua aberto. Encerrar processo derruba o powershell.exe e o fatura_0311.exe, e a coleta pede processos, conexões, tarefas agendadas e arquivos recentes, com o SHA-256 do pacote no caso. O terceiro alerta é diferente: o agente do SRV-ARQ-01 parou às 07:10, e a resposta é um chamado para a TI."
Atenção: clicar de novo em "Isolar máquina" libera a máquina; cada alerta guarda o seu registro de ações.
Conclusão: "O EDR mostra a cadeia do Word ao PowerShell e responde sem desligar a máquina, mantendo a investigação viva."
[Tela: gravação do laboratório do slide 15]

**Slide 16 — Laboratório: a árvore de processos em três dimensões (13:30–14:40)**
Objetivo: enxergar a cadeia suspeita no meio da rotina do NB-FIN-031. Responde a "o que a regra comportamental procura".
Na tela:
1. Arrastar a cena para girar a árvore e rolar para aproximar.
2. Clicar em "Destacar cadeia suspeita".
3. Clicar em "Isolar NB-FIN-031".
Fala: "Na cena, cada esfera é um processo. Os azuis são rotina: explorer, chrome, Teams, OneDrive e OUTLOOK. Os vermelhos formam a cadeia suspeita: WINWORD.EXE, powershell.exe e fatura_0311.exe. O losango amarelo é a conexão para 198.51.100.23 na porta 443. Os pontos brancos que correm nas linhas vermelhas mostram o fluxo de execução. Ao destacar a cadeia, a rotina fica transparente. Ao isolar, o losango fica cinza, os pontos param de chegar a ele e o botão passa a dizer 'Máquina isolada (clique para liberar)'. A legenda, no canto, explica as quatro cores."
Atenção: a cena começa parada; gire com calma para os rótulos não se sobreporem na gravação.
Conclusão: "Um editor de texto abrindo um interpretador de comandos é uma relação que o antivírus por assinatura não vê, e é isso que a regra comportamental procura."
[Tela: gravação do laboratório do slide 16]

**Slide 17 — Precisão de uma regra de PowerShell suspeito (14:40–15:20)**
Fala: "Em 30 dias, a regra disparou 400 vezes, e só 20 alertas eram verdadeiros: precisão de 5%. A equipe percebeu que 350 falsos positivos vinham do mesmo *script* de inventário e criou uma exceção restrita a ele. No mês seguinte, foram 40 alertas, 19 verdadeiros: precisão de 47,5% e sensibilidade de 95%. Um ataque deixou de ser detectado. Vale a troca? Provavelmente sim, se a lacuna for coberta por outra regra."

**Slide 18 — Laboratório: precisão e sensibilidade antes e depois do ajuste (15:20–16:30)**
Objetivo: decidir se a exceção vale a pena. Responde a "não afoga o SOC".
Na tela:
1. Ler os valores iniciais: 20 ataques reais; antes, 400 alertas e 20 verdadeiros; depois, 40 alertas e 19 verdadeiros.
2. Em "Depois da exceção", arrastar "Alertas gerados" para 15 e "Alertas verdadeiros" para 12.
Fala: "Com os valores do exemplo, a precisão sobe de 5% para 47,5%, a sensibilidade cai de 100% para 95% e os falsos positivos caem de 380 para 21. A frase embaixo diz: 21 alertas falsos e 1 ataque não detectado, e avisa que a lacuna nova precisa ser coberta por outra regra. Agora simulo uma exceção ampla, com 15 alertas e 12 verdadeiros. A precisão sobe para 80%, mas a sensibilidade despenca para 60%: 8 ataques passam sem alerta. Precisão olha para os alertas recebidos; sensibilidade olha para os ataques que aconteceram."
Atenção: o número de verdadeiros nunca passa do número de alertas nem do de ataques; o controle se ajusta sozinho.
Conclusão: "A exceção mais específica corta o ruído e perde menos ataques."
[Tela: gravação do laboratório do slide 18]

**Slide 19 — De volta ao problema (16:30–17:30)**
Fala: "Voltemos ao pedido da Marina. Os quatro cartões mostram a prova: a regra Sigma está no repositório com 5 testes; o teste atômico T1490 gerou o evento e o alerta saiu em 2 segundos; na plataforma, o abuso da API só gerou alerta depois que a R3 foi ligada e testada; e o EDR mostra a cadeia no NB-FIN-031, enquanto a exceção restrita leva a precisão de 5% para 47,5%. Respondendo à pergunta da aula: o Rafael segue o ciclo de vida da detecção. Ele descreve a técnica pelo ATT&CK, escreve a regra em Sigma, testa com eventos de exemplo e com um teste atômico em laboratório, publica, mede precisão e sensibilidade e ajusta com exceções específicas."

**Slides 20 a 22 — Pontos-chave, referências e encerramento (17:30–18:10)**
Fala: "Para levar desta aula: engenharia de detecção aplica requisitos, testes e versionamento às regras; o Sigma torna a regra portátil; detecção comportamental resiste melhor que indicadores; e precisão e sensibilidade orientam o ajuste. Mas e o que nenhuma regra viu? Na próxima aula, vamos caçar o que ficou para trás no SRV-ERP-01."

[Envato: "code review screen", "laboratory virtual machine", "network security analyst". Slides de apoio: anatomia da regra Sigma (slide 8) e cartões do slide 19.]

## Aula 11 — *Threat hunting* e inteligência de ameaças

### Texto base

Regras de detecção encontram aquilo que alguém já previu. Mas o que acontece com o adversário que usa uma variação nova, ou que se comporta como um administrador legítimo? Segundo o relatório M-Trends 2024, da Mandiant, a mediana global de permanência de invasores antes da descoberta (*dwell time*) foi de 10 dias em 2023 — e esse número é uma mediana, o que significa que muitos invasores ficam bem mais tempo. A caça a ameaças existe para encurtar esse período.

#### O que é *threat hunting*

***Threat hunting*** é a busca proativa e iterativa por atividade maliciosa que escapou dos controles automatizados. Ela parte da premissa de **comprometimento presumido** (*assume breach*): em vez de esperar o alerta, o caçador supõe que o adversário já está no ambiente e procura evidências disso. A caça não substitui o SOC; ela o complementa e, quando bem-sucedida, gera novas regras para a engenharia de detecção.

A abordagem mais madura é a **orientada por hipóteses**. Uma boa hipótese é específica e verificável, por exemplo: "um adversário está usando ferramentas legítimas de acesso remoto, instaladas fora do processo oficial de TI, para manter persistência". As hipóteses nascem de inteligência de ameaças, de técnicas ATT&CK sem cobertura, de achados do Red Team ou de anomalias observadas.

[Imagem 1 — Ciclo da caça: criar hipótese → investigar com ferramentas → descobrir padrões e TTPs → informar e enriquecer as detecções → nova hipótese. Texto alternativo: "Ciclo iterativo de threat hunting orientado por hipóteses". Pode ser recriado pela equipe.]

#### Indicadores *versus* comportamentos: a Pirâmide da Dor

Em 2013, David Bianco propôs a **Pirâmide da Dor** (*Pyramid of Pain*), que relaciona o tipo de indicador usado na defesa ao "custo" que sua detecção impõe ao adversário:

| Nível (da base ao topo) | Exemplo | Dificuldade para o adversário trocar |
|---|---|---|
| *Hashes* | *Hash* SHA-256 de um executável | Trivial |
| Endereços IP | IP de um servidor de comando e controle | Fácil |
| Nomes de domínio | Domínio usado para *phishing* | Simples |
| Artefatos de rede e de *host* | Padrão de URL, chave de registro criada | Incômodo |
| Ferramentas | Uma ferramenta específica de ataque | Desafiador |
| TTPs | O comportamento em si (táticas, técnicas e procedimentos) | Difícil |

A lição é direta: bloquear *hashes* e IPs é útil, mas o adversário contorna isso em minutos. Detectar **TTPs** obriga-o a mudar a forma como trabalha — e é aí que a caça e a engenharia de detecção devem concentrar esforço.

[Imagem 2 — Pirâmide em seis camadas, da base (*hashes*) ao topo (TTPs), com cores do verde ao vermelho indicando o aumento do custo para o adversário. Texto alternativo: "Pirâmide da Dor de David Bianco com os seis tipos de indicadores". Recriar a partir do texto original de Bianco (2013).]

#### Inteligência de ameaças: do dado à decisão

A **inteligência de ameaças** (*Cyber Threat Intelligence*, CTI) é a informação sobre adversários coletada, analisada e contextualizada para apoiar decisões. Dados soltos — uma lista de IPs — ainda não são inteligência; tornam-se inteligência quando respondem a perguntas como "quem ameaça meu setor, com quais objetivos e de que forma?". Costuma-se organizá-la em níveis, embora a nomenclatura varie entre autores:

- **Estratégica:** tendências, motivações e riscos para a alta gestão (por exemplo, o aumento de extorsão contra empresas de saúde).
- **Operacional:** campanhas e atores específicos, com suas intenções e capacidades, para líderes de SOC e resposta a incidentes.
- **Tática:** TTPs e indicadores, consumidos por analistas, caçadores e engenheiros de detecção. Algumas fontes separam ainda um nível **técnico**, restrito aos indicadores.

Para analisar intrusões, o **Modelo Diamante** (Caltagirone, Pendergast e Betz, 2013) descreve cada evento por quatro vértices: **adversário**, **capacidade**, **infraestrutura** e **vítima**. Conhecendo um vértice, o analista "pivota" para descobrir os outros — por exemplo, de um domínio malicioso (infraestrutura) para outras vítimas que o contataram.

[Imagem 3 — Diamante com os vértices adversário, capacidade, infraestrutura e vítima, ligados por arestas. Texto alternativo: "Modelo Diamante de análise de intrusões com quatro vértices". Pode ser recriado pela equipe.]

O compartilhamento de inteligência é apoiado por padrões abertos: o **STIX** descreve objetos como indicadores, campanhas e padrões de ataque; o **TAXII** define como trocá-los; e plataformas abertas como o **MISP** permitem armazenar e compartilhar eventos entre organizações. O **TLP** (*Traffic Light Protocol*), mantido pelo FIRST, indica com que liberdade cada informação pode ser repassada.

#### Exemplo numérico: a cadência da caça e o *dwell time*

Suponha que uma técnica de persistência não tenha regra de detecção e só possa ser encontrada por caça. Se a equipe faz essa caça a cada 30 dias, um invasor que se instale em um dia aleatório será encontrado, em média, depois de metade do intervalo: **15 dias**. Com caças semanais, a média cai para 3,5 dias. Melhor ainda: se a caça resultar em uma regra automatizada, o tempo cai para minutos. Por isso, o melhor produto de uma caça não é apenas o incidente encontrado, mas **a detecção que nasce dela**.

#### Pausa para reflexão

> Uma cooperativa de crédito recebe de um parceiro um relatório de inteligência sobre um grupo que ataca o setor financeiro. O relatório traz 300 IPs e 150 *hashes*, além da descrição do comportamento do grupo: acesso inicial com credenciais válidas de VPN, instalação de ferramentas legítimas de acesso remoto e exclusão de cópias de sombra antes da criptografia. O gestor do SOC propõe apenas importar os IPs e *hashes* no *firewall* e no EDR.
>
> 1. Com base na Pirâmide da Dor, qual é a limitação da proposta do gestor?
> 2. Formule duas hipóteses de caça a partir do comportamento descrito no relatório.
> 3. Em que nível de CTI (estratégico, operacional ou tático) cada parte do relatório se encaixa?
>
> **Desafio prático:** escolha uma das hipóteses e descreva, em até uma página, quais fontes de dados você consultaria, o que seria considerado evidência e qual regra de detecção poderia nascer da caça.

#### Pontos-chave

- *Threat hunting* parte do comprometimento presumido e é guiado por hipóteses.
- Na Pirâmide da Dor, detectar TTPs impõe muito mais custo ao adversário do que bloquear *hashes* e IPs.
- CTI é informação contextualizada para decisão, em níveis estratégico, operacional e tático.
- O Modelo Diamante e padrões como STIX, TAXII, MISP e TLP organizam a análise e o compartilhamento.
- O melhor resultado de uma caça é uma nova detecção automatizada.

### Referências da aula

BIANCO, David J. The pyramid of pain. *Enterprise Detection & Response*, mar. 2013. Disponível em: <https://detect-respond.blogspot.com/2013/03/the-pyramid-of-pain.html>. Acesso em: 13 nov. 2026.

CALTAGIRONE, Sergio; PENDERGAST, Andrew; BETZ, Christopher. *The diamond model of intrusion analysis*. [*S. l.*]: Center for Cyber Intelligence Analysis and Threat Research, 2013.

FIRST. *Traffic light protocol (TLP): FIRST standards definitions and usage guidance*. Versão 2.0. 2022. Disponível em: <https://www.first.org/tlp/>. Acesso em: 13 nov. 2026.

MANDIANT. *M-Trends 2024: special report*. [*S. l.*]: Google Cloud, 2024.

OASIS. *STIX version 2.1*. OASIS Standard. 2021. Disponível em: <https://oasis-open.github.io/cti-documentation/>. Acesso em: 13 nov. 2026.

ROBERTS, Scott J.; BROWN, Rebekah. *Intelligence-driven incident response: outwitting the adversary*. Sebastopol: O'Reilly, 2017.

### Roteiro da Videoaula 11 — "O que o invasor deixou para trás?"

Duração-alvo: 15 a 20 minutos. Deck: unidade_3/slides/aula11.html (24 slides).

**Slides 1 a 3 — Capa, audiodescrição e sumário (0:00–0:30)**
Fala: "Olá! Até aqui, a defesa esperou o alerta. Hoje vamos inverter a postura: com *threat hunting*, a caça a ameaças, saímos procurando o invasor, apoiados pela inteligência de ameaças."

**Slide 4 — O problema de hoje na Rede Tatame (0:30–1:50)**
Fala: "A Luiza Ferraz voltou, agora como caçadora. Caçar ameaças é buscar ativamente invasores que nenhuma regra apontou. Na Aula 9, o SOC viu o *login* das 02:17 no SRV-ERP-01 com a conta da Carla Dias, e a senha foi trocada. Mas o invasor ficou alguns minutos lá dentro, e nenhuma regra disparou depois disso. Ao mesmo tempo, chega um relatório do setor: o Grupo Cobalto Austral instala ferramentas legítimas de acesso remoto para voltar quando quiser. Uma porta escondida no ERP deixaria o grupo voltar, copiar dados de alunos e extorquir a rede. A pergunta da aula: como encontrar um invasor que já está dentro e que nenhuma regra viu?"
[Take de apoio: pessoa analisando gráficos e mapas em tela escura — Envato]

**Slides 5 e 6 — O que é *threat hunting* e a hipótese (1:50–2:40)**
Fala: "*Threat hunting* é a busca proativa e iterativa por atividade que escapou dos controles automáticos. Ela parte do comprometimento presumido, o *assume breach*: em vez de esperar o alerta, o caçador supõe que o adversário já está no ambiente. A abordagem mais madura começa por uma hipótese específica e verificável, como esta: um adversário usa ferramentas legítimas de acesso remoto, instaladas fora do processo oficial de TI, para manter persistência. Essa é a nossa hipótese H-11."

**Slide 7 — Laboratório: o ciclo da caça orientada por hipóteses (2:40–3:50)**
Objetivo: ver o caminho da caça H-11, da hipótese à regra nova. Responde a "como encontrar", em linhas gerais.
Na tela:
1. Clicar em "▶ Avançar": passo "Origens", com as quatro fontes da esquerda acesas.
2. Avançar por "Hipótese H-11", "Investigar" e "Padrões e TTPs".
3. Avançar por "Incidente", em que o nó Resposta fica vermelho.
4. Avançar até "Informar", com as linhas verdes voltando para "Criar hipótese".
Fala: "As hipóteses nascem de quatro origens: inteligência de ameaças, a CTI; técnicas do ATT&CK sem cobertura; achados do Red Team; e anomalias. Aqui, o relatório do setor e a técnica T1219, sem nenhuma regra no SIEM, geram a H-11. Na investigação, a caçadora empilha 30 dias de processos das 149 máquinas da sede: a ferramenta oficial aparece em 145, e duas não aprovadas aparecem em 3 máquinas e em 1. Nas máquinas da TI há mudança aprovada. No SRV-ERP-01, a ferramenta foi instalada como serviço pela conta carla.dias às 02:22, minutos depois do *logon* suspeito. A caça termina em dois produtos: um incidente, que vai para a Aula 12, e uma regra nova."
Conclusão: "Uma caça bem-sucedida sempre devolve alguma coisa à detecção."
[Tela: gravação do laboratório do slide 7]

**Slide 8 — Laboratório: empilhar para achar o raro (3:50–5:40)**
Objetivo: achar, entre 149 máquinas, as poucas que rodam algo fora do padrão. Responde a "onde procurar".
Na tela (VS Code, pasta caca-h11):
1. Abrir hipoteses/H-11.md e ler a hipótese, a origem e o que conta como evidência.
2. Voltar a caca_acesso_remoto.py e mostrar as linhas destacadas 7, 9 e 23 a 25.
3. Abrir dados/amostra_processos.csv.
4. Clicar em "Executar a caça".
Fala: "O arquivo H-11.md registra a hipótese antes da busca. Evidência é ferramenta não aprovada, sem chamado de mudança e com conexão externa. No *script*, a linha 5 define as 149 máquinas com EDR, a linha 6 a única ferramenta aprovada, suporte_ti.exe, e a linha 7 a lista de ferramentas de acesso remoto conhecidas. As linhas 9 e 10 criam dois contadores: em quantas máquinas cada ferramenta rodou e, para as não aprovadas, quem as iniciou. O laço das linhas 11 a 20 lê o CSV de 30 dias e ignora tudo que não é acesso remoto. Para as não aprovadas, a chave da linha 18 junta nome, processo pai e conta. As linhas 23 a 25 imprimem o empilhamento, *stack counting*, ordenado da ferramenta mais rara para a mais comum. Na saída, conectaja.exe aparece em 1 máquina, 0,7%; remotodesk.exe em 3, 2,0%; e suporte_ti.exe em 145, 97,3%. A segunda parte mostra o contexto: o remotodesk rodou 41 vezes, iniciado por services.exe, com a conta SYSTEM, nas três máquinas NB-TI. O conectaja rodou uma vez, iniciado pelo powershell.exe, com a conta carla.dias, no SRV-ERP-01. Reparem na amostra: às 02:22:33 de 13/11, o ConectaJa.exe tem o powershell como pai."
Atenção: o *script* compara nomes em minúsculas; por isso ConectaJa.exe vira conectaja.exe na saída. A última linha avisa que telaviva_agent.exe não apareceu em nenhuma máquina.
Conclusão: "O raro chama a atenção, e o contexto de pai e conta diz qual raro merece investigação."
[Tela: gravação do laboratório do slide 8]

**Slide 9 — Laboratório: separar o legítimo do suspeito (5:40–7:20)**
Objetivo: separar o legítimo do suspeito com rede, linha do tempo e mudanças. Responde a "como confirmar".
Na tela (console "SIEM · Caça H-11"; a busca 1 roda sozinha):
1. Ler "1. Empilhamento no SIEM".
2. Clicar em "2. Para onde se conectam?".
3. Clicar em "3. Linha do tempo no SRV-ERP-01".
4. Clicar em "4. Máquinas da TI: há mudança aprovada?".
Fala: "A busca 1 faz no SIEM o mesmo empilhamento do *script*: conta máquinas distintas por processo e ordena da menor para a maior. O resultado é igual. A busca 2 filtra as conexões de rede das duas ferramentas não aprovadas. As máquinas da TI falam com relay.remotodesk.example.com, o serviço do fabricante. O SRV-ERP-01 fez 22 conexões direto para 198.51.100.77, sem consulta DNS, todas na madrugada de hoje, a barra destacada no fim do histograma. A busca 3 pega tudo que aconteceu no SRV-ERP-01 entre 02:10 e 02:30. Às 02:17:12, o *logon* tipo 10 da carla.dias depois de 10 falhas, o mesmo da Aula 9; às 02:21:40, um PowerShell; às 02:22:05, o arquivo ConectaJa.exe criado em ProgramData; às 02:22:31, o evento 7045, serviço 'ConectaJa Update' com início automático; e às 02:22:33, a conexão para 198.51.100.77. A última coluna traz as técnicas: T1078, T1059.001, T1543.003 e T1219. A busca 4 cruza as máquinas da TI com a base de mudanças: as três têm a MUD-5521 aprovada, uma avaliação pedida pelo Caio Mendes até 30/11."
Atenção: espere cada tabela completar; a nota embaixo de cada resultado resume a leitura.
Conclusão: "Credencial válida, serviço novo e acesso remoto em 6 minutos: a H-11 está confirmada no SRV-ERP-01. Nas máquinas da TI, há um desvio de processo, que vira registro e não incidente."
[Tela: gravação do laboratório do slide 9]

**Slide 10 — Laboratório: a caça H-11 na plataforma, antes e depois da regra (7:20–9:10)**
Objetivo: ver por que a caça foi necessária, já que o dado existia e faltava a regra. Responde a "nenhuma regra viu".
Na tela (simulador na aba Cenários, com a R8 desligada):
1. No cartão "Acesso remoto não aprovado e saída de dados", clicar em "Iniciar cenário" e esperar os três passos, cerca de 30 segundos.
2. Na aba Arquitetura, clicar no nó SRV-ERP-01 e ler o painel.
3. Na aba Regras do CEP, ligar "R8 · Ferramenta de acesso remoto não aprovada".
4. Trocar a velocidade, no topo, para "1 s = 5 s".
5. Em Cenários, clicar em "Repetir com as fontes e regras atuais". Quando o alerta da R8 aparecer na aba SOC, clicar em "Conter".
6. Voltar a Cenários e ver o terceiro passo.
Fala: "Na primeira rodada, a instalação do ConectaJá no SRV-ERP-01 e as conexões periódicas para 198.51.100.77 ficam amarelas, 'visto nos logs, sem alerta': o EDR e o DNS registraram, mas nenhuma regra olhava para isso. O envio de 2,8 GB para fora fica vermelho, 'não detectado', porque a fonte de saída de rede está desligada. Esse é o ponto cego que a caça cobriu. Na Arquitetura, o painel do nó mostra o papel do servidor, os dados que ele guarda e a exposição. Com a R8 ligada, a instalação vira 'detectado'. Ao conter o alerta, o servidor fica isolado no mapa, e o envio dos 2,8 GB aparece como 'interrompido pela contenção'."
Atenção: o alerta chega entre 3 e 11 segundos depois do passo, conforme a velocidade. Na velocidade padrão, o envio acontece cerca de 27 segundos após o início; com "1 s = 5 s", sobra tempo para conter.
Conclusão: "O achado da caça vira regra, e a próxima instalação é contida antes da saída de dados."
[Tela: gravação do laboratório do slide 10, no simulador]

**Slide 11 — A Pirâmide da Dor (9:10–9:50)**
Fala: "Em 2013, David Bianco propôs a Pirâmide da Dor. Ela relaciona o tipo de indicador ao custo que a detecção impõe ao adversário. Na base, *hashes*, triviais de trocar; depois IPs, domínios, artefatos de rede e de host e ferramentas. No topo, as TTPs, táticas, técnicas e procedimentos, o comportamento em si, difícil de mudar."

**Slide 12 — Laboratório: subindo a Pirâmide da Dor (9:50–10:50)**
Objetivo: escolher que tipo de indicador da caça vale mais. Responde a "o que transformar em regra".
Na tela:
1. Clicar nos botões da esquerda, de "Hashes" até "TTPs", um por vez.
2. Arrastar a cena para girar a pirâmide, se quiser mostrar as camadas.
Fala: "A cor vai do verde, barato para o adversário trocar, ao vermelho, caro. Ao clicar num nível, a camada sobe e brilha, e o quadro no canto traz o custo e um exemplo da H-11. Em Hashes: o SHA-256 do ConectaJa.exe, que muda ao recompilar. Em Endereços IP: 198.51.100.77, trocado em minutos. Em Artefatos: o serviço 'ConectaJa Update' criado depois do *logon* remoto. E em TTPs: credencial válida, serviço novo e acesso remoto, as técnicas T1078, T1543.003 e T1219."
Atenção: a cena começa parada; os rótulos à direita acompanham cada camada.
Conclusão: "Detectar TTPs obriga o adversário a mudar o jeito de trabalhar, e é esse nível que a regra R8 alcança."
[Tela: gravação do laboratório do slide 12]

**Slide 13 — Laboratório: um byte a menos, um *hash* novo (10:50–11:50)**
Objetivo: ver por que bloquear o *hash* do ConectaJá não basta. Responde a "por que a regra comportamental".
Na tela:
1. Ler o arquivo ferramenta_demo.txt e os dois SHA-256, idênticos.
2. Clicar em "Alterar um byte".
3. Clicar em "Restaurar original" e, depois, editar qualquer letra no texto.
Fala: "O primeiro *hash* está na lista de bloqueio, a base da pirâmide. O segundo é calculado agora, no navegador. Enquanto são iguais, o quadro verde diz 'Bloqueio por *hash*: arquivo bloqueado'. O botão troca só o último caractere, a versão 1.0 vira 1.1. O *hash* novo muda quase por inteiro: os caracteres diferentes aparecem em negrito, e a contagem diz quantos dos 64 mudaram. O quadro fica vermelho, 'o arquivo passa'. O quadro da direita continua verde: a regra comportamental olha o que o programa faz, criar serviço e abrir acesso remoto, e não o arquivo."
Atenção: o arquivo é inofensivo e o cálculo é um SHA-256 real, feito no navegador.
Conclusão: "Um byte basta para fugir do *hash*. O comportamento continua o mesmo."
[Tela: gravação do laboratório do slide 13]

**Slides 14 e 15 — Níveis de CTI, Modelo Diamante, STIX, TAXII, MISP e TLP (11:50–13:00)**
Fala: "A inteligência de ameaças, a CTI, *Cyber Threat Intelligence*, é informação sobre adversários analisada para apoiar decisões. Uma lista de IPs só vira inteligência quando responde quem ameaça o setor, com que objetivo e de que forma. Ela tem níveis: estratégico, para a alta gestão; operacional, para quem lidera o SOC; e tático, para caçadores e engenheiros de detecção. O Modelo Diamante descreve cada intrusão por quatro vértices, adversário, capacidade, infraestrutura e vítima, e permite pivotar de um vértice para outro. STIX descreve os objetos, TAXII define como trocá-los, o MISP é uma plataforma aberta de compartilhamento, e o TLP, o *Traffic Light Protocol*, diz com que liberdade cada informação pode ser repassada."

**Slide 16 — Laboratório: um evento compartilhado na plataforma de CTI (13:00–14:30)**
Objetivo: usar o relatório do setor sobre o Cobalto Austral sem se afogar em indicadores. Responde a "de onde veio a hipótese".
Na tela (navegador no evento 1187 do MISP da rede setorial):
1. Na aba Atributos, ler a contagem e as primeiras linhas.
2. Clicar na aba ATT&CK.
3. Clicar na aba Diamante e, depois, no vértice Infraestrutura.
4. Clicar na aba Níveis e em cada botão "Revelar".
Fala: "As etiquetas do topo dizem tudo antes de abrir: tlp:amber, setor academias, motivação extorsão e quatro técnicas. TLP:AMBER permite usar a informação dentro da organização, sem publicar. Na aba Atributos, são 450 itens: 300 IPs e 150 *hashes*. A primeira linha já é o 198.51.100.77, descrito como retransmissão de acesso remoto. Na aba ATT&CK, as quatro técnicas: T1078, contas válidas; T1133, serviços remotos externos, a VPN; T1219, ferramentas de acesso remoto; e T1490, a exclusão de cópias de sombra, a mesma regra da Aula 10. No Diamante, ao clicar na infraestrutura, o pivô aparece: 22 conexões do SRV-ERP-01 desde a madrugada, e outras 2 redes de academias reportaram o mesmo IP. Na aba Níveis, cada frase revela o seu nível: extorsão contra quem guarda dados pessoais é estratégica; a campanha contra academias é operacional; o comportamento é tático; e os 300 IPs e 150 *hashes* são táticos, ou técnicos para quem separa esse nível."
Conclusão: "As quatro técnicas valem mais que os 450 atributos juntos, porque são elas que viram hipótese e regra."
[Tela: gravação do laboratório do slide 16]

**Slides 17 e 18 — A cadência da caça e a calculadora (14:30–15:40)**
Objetivo do laboratório: decidir com que frequência caçar. Responde a "a tempo".
Na tela:
1. Ler o exemplo do slide 17: 15 dias com caças a cada 30 dias, 3,5 dias com caças semanais e minutos com uma regra automatizada.
2. No slide 18, arrastar "Intervalo entre caças (dias)" de 30 para 7 e depois para 1.
Fala: "Um invasor que se instala num dia aleatório espera, em média, metade do intervalo até a próxima caça. Com caças a cada 30 dias, a média é de 15 dias. A calculadora sorteia 2.000 chegadas: o primeiro quadro mostra a fórmula, o segundo a média simulada, próxima dela, e o terceiro o pior caso, perto do intervalo inteiro. Com caças semanais, a espera cai para 3,5 dias; com caça diária, para meio dia. A barra verde, de minutos, é a regra automatizada."
Atenção: a média e o pior caso simulados variam um pouco a cada movimento, porque o sorteio muda.
Conclusão: "A caça acha o desconhecido; o que ela acha deve virar regra automática."
[Tela: gravação do laboratório do slide 18]

**Slides 19 e 20 — Pausa para reflexão e um caminho para responder (15:40–16:40)**
Fala: "Pause o vídeo e pense no caso da cooperativa de crédito: um relatório com 300 IPs e 150 *hashes*, além do comportamento do grupo, e um gestor que propõe só importar os indicadores. Qual é a limitação? [pausa] IPs e *hashes* ficam na base da pirâmide; o valor está no comportamento. Dele saem duas hipóteses: contas válidas na VPN em origens ou horários incomuns, T1078, e ferramentas de acesso remoto fora do processo de TI, T1219, a nossa H-11. E cada parte do relatório serve a um nível de CTI diferente."

**Slide 21 — De volta ao problema (16:40–17:40)**
Fala: "Voltemos à Luiza. Os cartões mostram o caminho: a hipótese H-11, vinda do relatório e de uma técnica sem regra; o empilhamento, que achou o ConectaJá em uma única máquina, o SRV-ERP-01, instalado como serviço às 02:22 pela conta carla.dias; a separação do legítimo, com as máquinas da TI cobertas por mudança aprovada; e a subida na pirâmide, com a R8 pegando a próxima instalação. Respondendo à pergunta da aula: com uma hipótese específica, baseada em inteligência de ameaças e no ATT&CK, a caçadora empilha a telemetria do EDR para achar o raro, confirma no SIEM e transforma o achado em incidente e em regra nova de comportamento."

**Slides 22 a 24 — Pontos-chave, referências e encerramento (17:40–18:20)**
Fala: "Para levar desta aula: a caça parte do comprometimento presumido e é guiada por hipóteses; detectar TTPs custa mais ao adversário que bloquear *hashes* e IPs; e o melhor resultado de uma caça é uma detecção nova. Encontramos o invasor no SRV-ERP-01. Na próxima aula, vamos conduzir a resposta a esse incidente."

[Envato: "hunter tracking footprints", "cyber threat map", "analyst whiteboard hypothesis". Slides de apoio: tabela da Pirâmide da Dor (slide 11) e cartões do slide 21.]

## Aula 12 — Resposta a incidentes

### Texto base

São três horas da manhã e o EDR alerta que vários servidores estão apagando cópias de sombra. Quem deve ser acionado? A máquina deve ser desligada ou isolada? É preciso avisar a diretoria, os clientes, a autoridade de proteção de dados? Organizações que só discutem essas perguntas durante o incidente perdem o recurso mais escasso da resposta: o tempo. A resposta a incidentes é, antes de tudo, **preparação**.

#### Evento, alerta e incidente

Nem todo evento é um incidente. Um **evento** é qualquer ocorrência observável; um **alerta** é a sinalização de que um evento pode ser malicioso; um **incidente** é uma ocorrência que efetivamente compromete, ou ameaça de forma iminente, a confidencialidade, a integridade ou a disponibilidade de sistemas e dados. A declaração de incidente é uma decisão formal, que mobiliza pessoas, recursos e, muitas vezes, obrigações legais.

#### O ciclo de resposta: do modelo clássico ao NIST SP 800-61 Rev. 3

Por mais de uma década, o NIST SP 800-61 Rev. 2 (2012) consagrou um ciclo em quatro fases: **preparação**; **detecção e análise**; **contenção, erradicação e recuperação**; e **atividades pós-incidente**. Em abril de 2025, o NIST publicou a **Revisão 3**, que reorganiza as recomendações como um perfil do **CSF 2.0**: a resposta a incidentes deixa de ser um processo isolado e passa a fazer parte da gestão de riscos cibernéticos. As atividades de preparação se distribuem por Governar, Identificar e Proteger; a resposta propriamente dita ocorre em Detectar, Responder e Recuperar; e as lições aprendidas alimentam a melhoria contínua em todas as funções.

| Fase clássica (Rev. 2) | Funções do CSF 2.0 relacionadas (Rev. 3) | Exemplos de atividades |
|---|---|---|
| Preparação | Governar, Identificar, Proteger | Políticas, papéis, inventário, *playbooks*, treinamentos |
| Detecção e análise | Detectar | Triagem de alertas, definição de escopo e severidade |
| Contenção, erradicação e recuperação | Responder, Recuperar | Isolar máquinas, remover persistência, restaurar *backups* |
| Pós-incidente | Identificar (melhoria) | Reunião de lições aprendidas, ajuste de detecções e controles |

[Imagem 1 — Modelo de ciclo de vida de resposta a incidentes do NIST SP 800-61 Rev. 3, que associa as atividades de preparação e de resposta às funções do CSF 2.0. Texto alternativo: "Diagrama do NIST relacionando as funções do CSF 2.0 às atividades de resposta a incidentes". Figura de domínio público do NIST.]

#### *Playbooks* e papéis

Um ***playbook*** descreve, passo a passo, como responder a um tipo específico de incidente — *ransomware*, conta comprometida, vazamento de dados —, com responsáveis, critérios de decisão e contatos. Parte desses passos pode ser automatizada por plataformas SOAR, como bloquear um domínio ou desabilitar uma conta. Também é essencial definir papéis: o **coordenador do incidente** decide e prioriza; os **analistas técnicos** investigam e executam; e as áreas **jurídica**, de **comunicação** e de **privacidade** (o encarregado de dados) participam desde as primeiras horas.

[Imagem 2 — Fluxograma de um *playbook* de *ransomware*: alerta → triagem → isolar *hosts* → preservar evidências → acionar jurídico e encarregado → erradicar → restaurar → lições aprendidas. Texto alternativo: "Fluxograma de playbook de resposta a ransomware com pontos de decisão". Pode ser recriado pela equipe.]

#### Contenção sem destruir evidências

A contenção busca **impedir que o dano aumente**: isolar máquinas pelo EDR, desabilitar contas, bloquear domínios e endereços. Existe, porém, uma tensão: desligar um computador interrompe o ataque, mas apaga a memória volátil, onde podem estar chaves, processos e conexões. A RFC 3227 recomenda coletar evidências da mais volátil para a menos volátil — memória antes do disco, por exemplo. Toda evidência deve ter **cadeia de custódia**: registro de quem a coletou, quando, como, onde ficou guardada e por quais mãos passou, com *hashes* que comprovem sua integridade. A ABNT NBR ISO/IEC 27037 traz diretrizes para identificar, coletar, adquirir e preservar evidências digitais. Só depois da contenção vêm a **erradicação** (remover persistência e contas criadas pelo invasor, corrigir a falha de entrada) e a **recuperação** (restaurar a partir de *backups* íntegros e monitorar com atenção redobrada).

#### Comunicação e obrigações legais

No Brasil, o art. 48 da LGPD determina que o controlador comunique à Autoridade Nacional de Proteção de Dados (ANPD) e aos titulares a ocorrência de incidente de segurança que possa acarretar risco ou dano relevante. A **Resolução CD/ANPD nº 15/2024** regulamentou essa obrigação e fixou o prazo de **três dias úteis**, contados do conhecimento de que o incidente afetou dados pessoais, além de exigir que o controlador mantenha registro dos incidentes. Na prática, isso significa que o encarregado e o jurídico precisam ser acionados cedo, e que o *playbook* deve prever quem decide pela comunicação e com quais informações.

[Imagem 3 — Linha do tempo de um incidente com marcos: detecção, declaração do incidente, conhecimento de que dados pessoais foram afetados e prazo de três dias úteis para comunicar à ANPD. Texto alternativo: "Linha do tempo de resposta a incidente com o prazo de comunicação à ANPD destacado". Pode ser recriado pela equipe.]

#### Exemplo numérico: priorizando incidentes

Com três incidentes abertos ao mesmo tempo e uma equipe pequena, a equipe usa uma pontuação simples: **severidade = criticidade do ativo (1 a 5) × confiança na detecção (1 a 3) × abrangência (1 a 3)**. (A) Conta de estagiário com *login* suspeito: 2 × 2 × 1 = **4**. (B) Servidor de banco de dados de clientes com processo desconhecido: 5 × 2 × 1 = **10**. (C) Cinco servidores apagando cópias de sombra: 4 × 3 × 3 = **36**. A ordem de atendimento é C, B e A. A fórmula não substitui o julgamento do coordenador, mas torna a decisão explícita, rápida e auditável.

#### Lições aprendidas

Após o incidente, a reunião de **lições aprendidas** deve ser feita sem caça a culpados, com foco em perguntas como: o que funcionou? Em que ponto a detecção ou a decisão demorou? Quais regras, *playbooks* e controles precisam mudar? Cada resposta deve virar uma ação com responsável e prazo — fechando o ciclo com a engenharia de detecção.

#### O que você verá na próxima unidade

Na Unidade 4, vermelho e azul trabalham juntos. Você vai aprender a planejar ciclos de *purple teaming* e de emulação de adversários, medir a evolução da defesa com métricas de detecção e resposta e com a cobertura do MITRE ATT&CK, conhecer exercícios de simulação — *tabletop*, CTF e *cyber range* — e estruturar um programa contínuo de segurança, encerrando com as trilhas de carreira da área.

#### Pontos-chave

- Evento, alerta e incidente são conceitos diferentes; declarar incidente é uma decisão formal.
- O NIST SP 800-61 Rev. 3 integra a resposta a incidentes às funções do CSF 2.0.
- *Playbooks* e papéis definidos antes do incidente economizam o tempo mais valioso.
- Contenção deve preservar evidências, com ordem de volatilidade e cadeia de custódia.
- A LGPD e a Resolução CD/ANPD nº 15/2024 exigem comunicação em três dias úteis quando houver risco ou dano relevante.

### Referências da aula

AGÊNCIA NACIONAL DE PROTEÇÃO DE DADOS (Brasil). Resolução CD/ANPD nº 15, de 24 de abril de 2024. Aprova o Regulamento de Comunicação de Incidente de Segurança. *Diário Oficial da União*, Brasília, DF, 2024.

ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. *ABNT NBR ISO/IEC 27037*: tecnologia da informação — técnicas de segurança — diretrizes para identificação, coleta, aquisição e preservação de evidência digital. Rio de Janeiro: ABNT, 2013.

BRASIL. Lei nº 13.709, de 14 de agosto de 2018. Lei Geral de Proteção de Dados Pessoais (LGPD). *Diário Oficial da União*, Brasília, DF, 15 ago. 2018.

BREZINSKI, Dominique; KILLALEA, Tom. *RFC 3227: guidelines for evidence collection and archiving*. [*S. l.*]: IETF, 2002.

CICHONSKI, Paul *et al*. *SP 800-61 Rev. 2: computer security incident handling guide*. Gaithersburg: NIST, 2012. DOI: 10.6028/NIST.SP.800-61r2.

NELSON, Alex *et al*. *SP 800-61 Rev. 3: incident response recommendations and considerations for cybersecurity risk management: a CSF 2.0 community profile*. Gaithersburg: NIST, 2025. DOI: 10.6028/NIST.SP.800-61r3.

### Roteiro da Videoaula 12 — "Três da manhã, invasor confirmado no ERP: e agora?"

Duração-alvo: 15 a 20 minutos. Deck: unidade_3/slides/aula12.html (25 slides).

**Slides 1 a 3 — Capa, audiodescrição e sumário (0:00–0:30)**
Fala: "Olá! Esta é a última aula da Unidade 3. O SOC viu o *login*, o Rafael escreveu regras e a Luiza encontrou o invasor. Agora alguém precisa conduzir a resposta ao incidente, da contenção às lições aprendidas, incluindo a comunicação prevista na LGPD."

**Slide 4 — O problema de hoje na Rede Tatame (0:30–1:50)**
Fala: "A Marina Prado é a CISO, a diretora de segurança da informação da Rede Tatame. Às 03:00 de sexta-feira, 13 de novembro, o telefone toca. A caça da Aula 11 confirmou que, às 02:22, o invasor instalou no SRV-ERP-01 o ConectaJá, uma ferramenta de acesso remoto não aprovada. O ERP guarda os responsáveis financeiros de alunos, inclusive de menores. O próximo passo de um *ransomware* é apagar as cópias de sombra e cifrar os servidores, e a ANPD, a Autoridade Nacional de Proteção de Dados, precisa ser comunicada em três dias úteis. Os papéis estão embaixo: Marina coordena, Luiza no SOC, Caio Mendes na TI, e a conta afetada é a da Carla Dias. A pergunta da aula: como a Rede Tatame conduz este incidente, contendo sem destruir evidências, recuperando o ERP e comunicando a ANPD no prazo?"
[Take de apoio: telefone tocando na mesa à noite, tela de alerta ao fundo — Envato]

**Slide 5 — Evento, alerta e incidente (1:50–2:20)**
Fala: "Nem todo evento é um incidente. Evento é qualquer ocorrência observável; alerta é a sinalização de que um evento pode ser malicioso; incidente é o que compromete, ou ameaça de forma iminente, a confidencialidade, a integridade ou a disponibilidade. Declarar incidente é uma decisão formal, porque mobiliza pessoas, recursos e obrigações legais. Às 03:00, a Marina tomou essa decisão."

**Slides 6 e 7 — Do modelo clássico ao NIST SP 800-61 Rev. 3 (2:20–3:10)**
Fala: "A Revisão 2 do NIST SP 800-61, de 2012, consagrou quatro fases: preparação; detecção e análise; contenção, erradicação e recuperação; e pós-incidente. Em abril de 2025, a Revisão 3 reorganizou tudo como um perfil do CSF 2.0, o *Cybersecurity Framework*. A resposta passa a fazer parte da gestão de riscos. A tabela mostra a correspondência entre as fases e as funções."

**Slide 8 — Laboratório: as quatro fases dentro das seis funções (3:10–4:20)**
Objetivo: situar a resposta nos dois guias do NIST. Responde a "como conduzir", em visão geral.
Na tela:
1. Clicar em "▶ Avançar": "Rev. 2 (2012) · o ciclo clássico", com as quatro fases da esquerda.
2. Avançar: "Rev. 3 (2025) · seis funções do CSF 2.0", com as funções da direita.
3. Avançar pelas quatro correspondências, uma fase por vez.
4. Avançar até "O caso SRV-ERP-01 no mapa".
Fala: "À esquerda, as quatro fases da Rev. 2; à direita, as seis funções do CSF 2.0: Governar, Identificar, Proteger, Detectar, Responder e Recuperar. A preparação se espalha por três funções e vira responsabilidade da gestão. Detecção e análise caem em Detectar, onde entram SIEM, EDR e caça. Contenção, erradicação e recuperação se dividem entre Responder e Recuperar. O pós-incidente volta para Identificar. No último passo, o nosso caso percorre o mapa: em Detectar, as 10 falhas e um sucesso e a caça H-11; em Responder, isolar e preservar; em Recuperar, o *backup* anterior a 13/11; em Identificar e Governar, a regra nova, o MFA no acesso remoto e o *playbook* revisado."
Conclusão: "A resposta ao incidente do ERP toca as seis funções, não só a equipe técnica."
[Tela: gravação do laboratório do slide 8]

**Slide 9 — *Playbooks* e papéis definidos antes do incidente (4:20–4:50)**
Fala: "Um *playbook* descreve, passo a passo, como responder a um tipo de incidente, com responsáveis, critérios e contatos. Parte dele pode ser automatizada por plataformas SOAR, de orquestração e resposta automatizada. O coordenador decide e prioriza, os analistas investigam e executam, e jurídico, comunicação e o encarregado de dados entram desde as primeiras horas."

**Slide 10 — Laboratório: o *playbook* de *ransomware* como código (4:50–6:40)**
Objetivo: ter, antes da crise, quem faz o quê e em que ordem. Responde a "conduzir com ordem".
Na tela (VS Code, pasta resposta-incidentes):
1. Ler playbooks/ransomware.yaml e apontar as linhas destacadas 17, 18, 19, 23, 24 e 29.
2. Abrir ferramentas/validar_playbook.py e clicar em "Validar".
3. Abrir ferramentas/prazo_anpd.py e clicar em "Prazo 13/11".
4. Clicar em "Prazo 17/11".
Fala: "O gatilho do *playbook*, na linha 3, é a regra da Aula 10, a exclusão de cópias de sombra. São oito etapas. A etapa isolar é a única automática, executada pelo SOAR no EDR, e a linha 17 explica: isolar, não desligar, porque a memória volátil é evidência. Logo depois vem preservar, com responsável próprio, o analista forense, e ordem de volatilidade da RFC 3227. A linha 24 lista quem a etapa acionar notifica: coordenador, jurídico, encarregado de dados e comunicação. A erradicação só aparece na linha 29, depois da preservação. O validador confere três coisas: na linha 11, se toda etapa manual tem responsável; na linha 15, se os quatro papéis obrigatórios são acionados; e na linha 16, se preservar vem antes de erradicar. A saída diz 'ransomware-v3: 8 etapas' e 'nenhum problema encontrado'. O prazo_anpd.py conta três dias úteis a partir do conhecimento. A linha 5 lista os feriados, e a função dia_util, nas linhas 8 e 9, aceita só segunda a sexta fora deles. Para 13/11, sexta, o 15/11 cai num domingo e é feriado; os dias úteis são 16, 17 e 18, e o prazo final é 18/11, quarta. Para 17/11, o feriado de 20/11 é pulado, e o prazo final vai para 23/11, segunda."
Atenção: os resultados são simulados na tela. O cálculo segue o modelo da aula, que começa a contagem no dia útil seguinte ao conhecimento; a regra exata deve ser confirmada com o jurídico.
Conclusão: "Com o *playbook* como código, a ordem das etapas e os papéis são verificados antes da madrugada da crise."
[Tela: gravação do laboratório do slide 10]

**Slide 11 — Laboratório: simulação de mesa, o caso de *ransomware* (6:40–8:30)**
Objetivo: tomar, em ordem, as decisões da madrugada de 13/11. Responde a "conter sem destruir evidências" e "comunicar no prazo".
Na tela:
1. Na situação "sex 13/11 · 03:05", ler o texto e clicar em "Isolar os cinco servidores pelo EDR". Ler o retorno e clicar em "Próxima decisão ▶".
2. Em "03:25", escolher o coordenador que aciona jurídico, comunicação e encarregado.
3. Em "04:10", escolher de propósito "Imagem do disco, depois a memória" para mostrar um retorno de erro.
4. Seguir por "16:00", "seg 16/11 · 10:00" e "qua 25/11 · 14:00".
5. Na tela final, ler a pontuação e clicar em "⟲ Recomeçar", se quiser repetir.
Fala: "Cada situação tem um relógio, um texto e três opções. Desligar os servidores para o ataque, mas apaga a memória volátil; esperar até as 8h dá tempo de a criptografia terminar; isolar pelo EDR mantém a máquina ligada com o canal de coleta aberto. Ao escolher, o botão fica verde ou vermelho, o retorno explica o porquê, e o diário à direita registra a decisão, como num incidente real. Às 04:10, se o forense começar pelo disco, o retorno lembra que a RFC 3227 manda começar pela memória. Às 16:00, o cadastro de responsáveis foi acessado: o prazo corre do conhecimento, e vai até 18/11. Na segunda, a erradicação remove o serviço ConectaJa, troca a senha, exige MFA e restaura um *backup* íntegro. No fim, a tela mostra quantas das seis decisões seguiram o *playbook*."
Atenção: o erro escolhido de propósito ajuda a discussão; avise o aluno que a justificativa vale mais que a pontuação.
Conclusão: "Decidir rápido e certo de madrugada depende de papéis e etapas combinados antes."
[Tela: gravação do laboratório do slide 11]

**Slide 12 — Conter sem destruir evidências (8:30–9:10)**
Fala: "A contenção busca impedir que o dano aumente: isolar máquinas, desabilitar contas, bloquear domínios e endereços. Desligar interrompe o ataque, mas apaga a memória. A RFC 3227 manda coletar da evidência mais volátil para a menos volátil, e toda evidência precisa de cadeia de custódia: quem coletou, quando, como, onde ficou e por quais mãos passou, com *hashes*. A ABNT NBR ISO/IEC 27037 traz as diretrizes para isso."

**Slide 13 — Laboratório: conter a tempo, o SOC contra o Cobalto Austral (9:10–11:10)**
Objetivo: medir quanto tempo o SOC leva para perceber e conter. Responde a "conter".
Na tela (simulador na aba SOC; o cenário "Emulação do Grupo Cobalto Austral" começa sozinho):
1. Esperar o primeiro alerta da R11, "Login sem MFA em conta privilegiada ou VPN", sobre caio.mendes. Clicar em "Investigar" e ler o painel.
2. Clicar em "Conter" nesse alerta.
3. Quando aparecer o alerta da R11 sobre svc-backup, clicar em "Investigar" e depois em "Falso positivo".
4. Abrir a aba Cenários e ler os passos.
5. Clicar em "Reiniciar", no topo. Em Cenários, clicar em "Iniciar cenário" no cartão "Emulação do Grupo Cobalto Austral", trocar a velocidade para "1 s = 1 min" e deixar rodar sem conter.
Fala: "A emulação começa com um *login* na VPN com a senha vazada do caio.mendes, sem MFA, e a R11 detecta. No painel de investigação aparecem a lógica da regra, o tempo do primeiro sinal até o alerta e a linha do tempo correlacionada. Ao conter, o nó da VPN fica isolado no mapa e o alerta passa a 'contido'. No topo, o MTTD, tempo médio até detectar, e o MTTR, tempo médio até responder, ganham valores. O alerta do svc-backup é benigno: a conta de serviço tem exceção documentada, e o painel recomenda marcar como falso positivo. Na aba Cenários, os passos seguintes aparecem como 'interrompido pela contenção'. Na segunda rodada, sem conter, a cadeia segue: consulta ao AD, RDP, leitura da memória do LSASS, cópia de 4,2 GB, exclusão das cópias de sombra e, no fim, 'impacto consumado', com os arquivos da sede cifrados, a técnica T1486."
Atenção: o primeiro alerta leva de 3 a 11 segundos na velocidade padrão. Sem contenção, a cadeia completa dura cerca de 1 minuto em "1 s = 15 s" e uns 15 segundos em "1 s = 1 min". Os passos sem regra ativa ficam amarelos, como candidatos a regra nova.
Conclusão: "Conter o primeiro alerta interrompe a cadeia antes da exclusão das cópias de sombra e da criptografia."
[Tela: gravação do laboratório do slide 13, no simulador]

**Slide 14 — Erradicação e recuperação (11:10–11:40)**
Fala: "Erradicar é remover a persistência e as contas do invasor e corrigir a falha de entrada. Recuperar é restaurar de *backups* íntegros e monitorar com atenção redobrada. No nosso caso: remover o serviço 'ConectaJa Update', trocar a senha da carla.dias, exigir segundo fator no acesso remoto ao SRV-ERP-01 e restaurar um *backup* anterior a 13/11."

**Slide 15 — Laboratório: *hash* das evidências e cadeia de custódia (11:40–13:10)**
Objetivo: preservar as evidências do SRV-ERP-01 de modo que valham depois. Responde a "sem destruir evidências".
Na tela (terminal da estação forense, caso IR-2026-031; clicar em "▶ Próximo comando" cinco vezes):
1. ls -l evidencias/
2. sha256sum evidencias/* | tee evidencias.sha256
3. column -s, -t cadeia_custodia.csv
4. echo com a linha de transferência, acrescentada ao fim de cadeia_custodia.csv
5. sha256sum -c evidencias.sha256
Fala: "O primeiro comando lista as duas evidências. As permissões começam com r, de leitura, sem w: ninguém escreve nelas. A memória foi coletada às 04:18, com 16 GB, e o disco às 05:52: primeiro o mais volátil. O segundo comando calcula o SHA-256 de cada arquivo, e o tee grava os *hashes* num arquivo próprio. O terceiro mostra o formulário de custódia em colunas: item, descrição, quem coletou, quando, método, local e *hash*. As duas linhas são da Luiza Ferraz, com destino ao cofre-digital-01. O quarto comando acrescenta uma linha: a entrega à perita M. Teixeira às 09:10, em mãos, com lacre 0457. Os dois sinais de maior acrescentam sem apagar o que já existia. O último confere os *hashes* de novo, e as duas linhas terminam em OK."
Atenção: os arquivos e *hashes* são fictícios. "⏭ Executar tudo" roda o roteiro inteiro.
Conclusão: "Os arquivos ficam somente leitura, e a análise trabalha sempre sobre cópias. Com *hash* e custódia, a evidência continua valendo."
[Tela: gravação do laboratório do slide 15]

**Slide 16 — LGPD e a Resolução CD/ANPD nº 15/2024 (13:10–13:40)**
Fala: "O art. 48 da LGPD manda o controlador comunicar à ANPD e aos titulares o incidente que possa acarretar risco ou dano relevante. A Resolução CD/ANPD nº 15/2024 fixou o prazo de três dias úteis, contados do conhecimento de que o incidente afetou dados pessoais, e exige registro dos incidentes. Por isso o encarregado e o jurídico entram cedo."

**Slide 17 — Laboratório: contando os três dias úteis (13:40–14:40)**
Objetivo: contar o prazo de comunicação à ANPD. Responde a "comunicar a ANPD no prazo".
Na tela:
1. Ler o calendário já marcado em 13/11.
2. Clicar no dia 17.
3. Clicar de volta no dia 13.
Fala: "Em amarelo, o dia do conhecimento; em azul, os dias úteis contados; em vermelho, o prazo final; e os dias marcados como feriado são os nacionais. Com conhecimento em 13/11, sexta, os dias úteis são 16, 17 e 18, e o prazo final é 18/11, quarta. A frase embaixo lembra o feriado no caminho, a Proclamação, que neste ano cai num domingo. Se o conhecimento fosse em 17/11, o feriado de 20/11 seria pulado, e o prazo iria para 23/11, segunda."
Atenção: neste modelo, a contagem começa no dia útil seguinte ao conhecimento. Confirme a regra com o jurídico.
Conclusão: "A data do conhecimento decide o prazo. Por isso o *playbook* manda registrá-la."
[Tela: gravação do laboratório do slide 17]

**Slides 18 e 19 — Priorizando três incidentes e a fila ordenada (14:40–15:50)**
Objetivo do laboratório: escolher que incidente atender primeiro. Responde a "conduzir com ordem".
Na tela:
1. No slide 18, ler a tabela: A = 2 × 2 × 1 = 4, B = 5 × 2 × 1 = 10 e C = 4 × 3 × 3 = 36.
2. No slide 19, mudar a confiança de B para 3.
3. Mudar a criticidade de A para 5.
Fala: "Com uma equipe pequena, a severidade é criticidade do ativo, de 1 a 5, vezes confiança na detecção, de 1 a 3, vezes abrangência, de 1 a 3. Os cinco servidores apagando cópias de sombra dão 36 e vão para o topo. Agora, imagine que B está enviando dados para fora: a confiança sobe para 3, a nota vai a 15, e a fila se reordena sozinha. Se descobrirmos que a conta de A alcança o servidor de pagamentos, a criticidade vai a 5, e A passa a 10. A frase embaixo mostra a ordem: C, B e A."
Conclusão: "A pontuação explica a decisão e a torna auditável, mas quem decide é o coordenador."
[Tela: gravação do laboratório do slide 19]

**Slide 20 — Lições aprendidas sem caça a culpados (15:50–16:20)**
Fala: "Depois do incidente, a reunião de lições aprendidas pergunta o que funcionou, onde a detecção ou a decisão demorou e quais regras, *playbooks* e controles precisam mudar. Ela é feita sem caça a culpados, e cada resposta vira uma ação com responsável e prazo, fechando o ciclo com a engenharia de detecção da Aula 10."

**Slide 21 — Unidade 4: vermelho e azul na mesma sala (16:20–16:50)**
Fala: "Na Unidade 4, vermelho e azul trabalham juntos. Vamos planejar ciclos de *purple teaming* e de emulação de adversários, medir a defesa com métricas e com a cobertura do MITRE ATT&CK, conhecer *tabletop*, CTF e *cyber range* e estruturar um programa contínuo de segurança."

**Slide 22 — De volta ao problema (16:50–17:50)**
Fala: "Voltemos à Marina. Os cartões resumem a resposta: o *playbook* pronto, em que só o isolamento é automático e preservar vem antes de erradicar; a contenção cedo, que interrompeu a cadeia na plataforma; a evidência que vale, com memória antes do disco, *hash* e cadeia de custódia; e o prazo, com conhecimento em 13/11 e comunicação até 18/11, além da fila ordenada pela severidade. Respondendo à pergunta da aula: a Rede Tatame segue o *playbook*. Ela isola o SRV-ERP-01 sem desligá-lo, preserva memória e disco com *hash* e cadeia de custódia, remove o ConectaJá e a credencial da Carla, restaura de *backup* íntegro, comunica a ANPD em até três dias úteis e transforma as lições aprendidas em melhorias."

**Slides 23 a 25 — Pontos-chave, referências e encerramento (17:50–18:40)**
Fala: "Para levar desta aula: declarar incidente é uma decisão formal; o NIST SP 800-61 Rev. 3 integra a resposta ao CSF 2.0; *playbooks* e papéis definidos antes economizam o tempo mais valioso; a contenção preserva evidências; e a LGPD exige comunicação em três dias úteis quando houver risco ou dano relevante. Acompanhamos o caso do SRV-ERP-01 do primeiro *login* à lição aprendida. Na Unidade 4, vermelho e azul vão se sentar à mesma mesa para medir e melhorar essa defesa juntos. Até lá!"

[Envato: "phone ringing at night office", "incident response team meeting", "forensic hard drive evidence bag". Slides de apoio: tabela Rev. 2 e CSF 2.0 (slide 7) e cartões do slide 22.]

## Quiz não avaliativo

### Questão 1 (verdadeiro ou falso)

De acordo com a Pirâmide da Dor, bloquear os *hashes* dos arquivos maliciosos usados por um grupo é a forma de detecção que impõe maior custo ao adversário, pois ele precisaria reescrever todas as suas ferramentas.

( ) Verdadeiro  
(X) Falso

### Questão 2 (múltipla escolha)

Em 30 dias, uma regra de detecção gerou 250 alertas, dos quais 50 foram confirmados como atividade maliciosa. A precisão dessa regra é de:

a) 5%.  
*b) 20%.  
c) 50%.  
d) 80%.

### Feedback

**Questão 1 — Falso.** Os *hashes* ficam na base da Pirâmide da Dor: alterar um único byte de um arquivo gera um *hash* completamente diferente, o que torna trivial para o adversário contornar esse bloqueio. O maior custo é imposto pela detecção de TTPs, no topo da pirâmide, porque obriga o adversário a mudar a forma como opera, e não apenas os artefatos que usa.

**Questão 2 — Alternativa b.** A precisão mede, entre os alertas gerados, a proporção de alertas verdadeiros: 50 ÷ 250 = 0,20, ou 20%. Isso significa que 80% dos alertas (alternativa d) foram falsos positivos — um sinal de que a regra precisa de ajuste para não contribuir para a fadiga de alertas. Note que a precisão não informa quantos ataques deixaram de ser detectados; para isso, usa-se a sensibilidade (*recall*).

## Material complementar

### Direto da fonte (livro da Biblioteca Virtual)

- **Texto provocativo:** O ciclo de resposta a incidentes do NIST é a referência mais usada no mundo — mas ele funciona contra um adversário paciente, que permanece meses no ambiente e reage quando percebe que foi descoberto? O capítulo indicado apresenta as fases da resposta a incidentes segundo o NIST e prepara a discussão do autor sobre seus limites diante de ameaças persistentes avançadas (APTs). Leia com olhar crítico e compare com o que vimos na Aula 12.
- **Nome do livro:** LEVI, Hiago Kin. *Confronto cibernético*: técnicas e táticas de enfrentamento e resposta a ameaças persistentes avançadas (APTs). Rio de Janeiro: Brasport, 2026. *E-book*.
- **Capítulo:** 2 — Fases de resposta a incidentes conforme o NIST (como leitura complementar, o capítulo 3 discute por que esse padrão é insuficiente contra APTs)
- **Link de acesso:** <https://plataforma.bvirtual.com.br/Acervo/Publicacao/235882>
- **Aula em que entra:** Aula 12

### Para mergulhar no assunto (saiba mais)

- **Texto provocativo:** Como é, de verdade, uma intrusão do primeiro clique até a criptografia? O *site* The DFIR Report publica gratuitamente relatos detalhados de intrusões reais, com linha do tempo, técnicas mapeadas no MITRE ATT&CK e sugestões de detecção. Escolha um relatório e tente responder: em que momento você teria detectado o adversário, e com qual fonte de dados?
- **Link:** <https://thedfirreport.com/> **[conferir acesso; conteúdo em inglês]**
- **Link complementar:** repositório de regras Sigma — <https://github.com/SigmaHQ/sigma>
- **Aula em que entra:** Aula 11

### Podcast (curadoria, até 45 min)

- **Texto provocativo:** Analistas de SOC e caçadores de ameaças começam o dia se atualizando sobre o que os adversários estão fazendo. O SANS Internet Stormcast resume, em poucos minutos, as ameaças e vulnerabilidades observadas pelo Internet Storm Center. Ouça alguns episódios e tente classificar cada notícia como inteligência estratégica, operacional ou tática.
- **Nome do podcast:** SANS Internet Stormcast
- **Nome do episódio:** episódio diário mais recente **[conferir; episódios em inglês, com poucos minutos de duração; se possível, indicar também um episódio em português sobre resposta a incidentes]**
- **Link:** <https://isc.sans.edu/podcast.html> **[conferir link]**
- **Aula em que entra:** Aula 11

### Artigo científico

- **Texto provocativo:** E se o próprio sistema pudesse ordenar os alertas pela probabilidade de serem ataques reais, em vez de deixar o analista se afogar na fila? Este artigo, apresentado em um dos principais simpósios de segurança de redes, propõe usar o histórico de causalidade dos eventos (proveniência) para reduzir a fadiga de alertas. Leia e reflita: que limites essa automação ainda tem?
- **Link:** <https://www.ndss-symposium.org/ndss-paper/nodoze-combatting-threat-alert-fatigue-with-automated-provenance-triage/> **[conferir link]**
- **Aula em que entra:** Aula 9
- **Referência ABNT:** HASSAN, Wajih Ul *et al*. NoDoze: combatting threat alert fatigue with automated provenance triage. *In*: NETWORK AND DISTRIBUTED SYSTEM SECURITY SYMPOSIUM (NDSS), 2019, San Diego. *Proceedings* [...]. Reston: Internet Society, 2019.
