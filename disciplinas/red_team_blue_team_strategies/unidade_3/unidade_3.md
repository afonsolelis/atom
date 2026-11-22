# Unidade 3 — Defesa, Monitoramento e Detecção

Disciplina: Red Team & Blue Team Strategies  
Professor-conteudista: Afonso Cesar Lelis Brandão  
Prazo de entrega: 20/12/2026  
Template de origem: `documentos/Unidade 3/TEMPLATE - Unidade 3_nome da disciplina.docx`

> Versão alinhada à **ementa oficial** enviada pela coordenação em 18/11/2026 (`EMENTA.md`).
> Recursos visuais indicados entre colchetes, como pede o template; a equipe de produção substitui pelas imagens finais.

## Aula 9 — Arquitetura de monitoramento: logs, SIEM e telemetria de endpoints

### O que você verá nesta unidade

Na Unidade 2, executamos em laboratório as técnicas do adversário: reconhecimento, exploração, escalada de privilégios, movimentação lateral e evasão. Em cada etapa, perguntamos que rastro ficava para trás. Agora vestimos a camisa azul e respondemos à pergunta inversa: **como a defesa enxerga esses rastros, detecta o ataque e diminui as chances de ele dar certo?** Nesta unidade, você vai montar a arquitetura de monitoramento que leva *logs* e telemetria de *endpoints* e de rede até o SIEM (Aula 9); comparar a detecção por assinatura, por comportamento e por regras de correlação, escrevendo e ajustando regras (Aula 10); conduzir uma caça a ameaças guiada por hipóteses, consultas e análise de anomalias (Aula 11); e aplicar *hardening* e redução da superfície de ataque com base nos CIS Benchmarks e nos CIS Controls (Aula 12). O objetivo é que você consiga projetar a cadeia que vai do dado bruto ao alerta investigado e ao controle reforçado. Essa competência é central para quem pretende atuar em SOC, engenharia de detecção ou administração segura de sistemas, e prepara a Unidade 4, em que a defesa responde a incidentes e valida suas detecções em exercícios *purple team*.

### Texto base

Imagine um condomínio com câmeras em todos os corredores, mas sem ninguém assistindo às gravações e com o equipamento configurado para apagar tudo depois de 24 horas. As câmeras existem, mas não protegem ninguém. Muitas organizações vivem situação parecida com seus registros: os sistemas geram eventos o tempo todo, mas eles não são coletados, não são analisados ou são descartados antes de alguém precisar deles. Nesta aula, vamos desenhar a arquitetura que transforma esse fluxo de dados em capacidade de detecção.

#### Evento, registro e telemetria

Um **evento** é qualquer ocorrência observável em um sistema: um *login*, a criação de um processo, uma consulta DNS. O **registro** (*log*) é a anotação desse evento, com data, hora, origem e detalhes. **Telemetria** é o termo mais amplo para o fluxo contínuo de dados que agentes e sensores enviam para análise. O guia NIST SP 800-92 trata a gestão de registros como um ciclo de gerar, transmitir, armazenar, analisar e descartar, e lembra que cada etapa precisa ser planejada antes do incidente, e não improvisada durante ele.

Na **defesa em profundidade**, a proteção é organizada em camadas sobrepostas (perímetro, rede, *endpoint*, aplicação, identidade e dados), porque qualquer controle pode falhar. Para o monitoramento, cada camada é também uma fonte de telemetria: um *firewall* que deixou passar uma conexão ainda registra que ela aconteceu. Quem consome esses dados é o **SOC** (*Security Operations Center*), em geral organizado em níveis: N1 faz a triagem dos alertas, N2 investiga e inicia a contenção, N3 caça ameaças e cria novas detecções.

#### Telemetria de *endpoints*

O *endpoint* (servidor, notebook, estação) é onde o adversário executa suas ações, por isso concentra as fontes mais ricas:

| Fonte | Exemplo de evento | O que revela |
|---|---|---|
| Windows (canal Security) | 4624 (*logon* bem-sucedido), 4625 (falha de *logon*), 4688 (criação de processo), 1102 (registro de auditoria apagado) | Uso de credenciais, força bruta, execução, tentativa de apagar rastros |
| Sysmon | ID 1 (processo, com linha de comando), ID 3 (conexão de rede), ID 22 (consulta DNS) | Comportamento detalhado do *endpoint* |
| Linux | `auth.log` ou `secure`, regras do `auditd` | Acessos SSH, uso de `sudo`, chamadas de sistema auditadas |

O **Sysmon** (*System Monitor*), ferramenta gratuita da Microsoft, acrescenta o que o registro nativo não traz por padrão, como o *hash* do executável e a linha de comando do processo pai. O próprio evento 4688 só registra a linha de comando se uma política específica estiver habilitada. Ter a fonte não basta: é preciso configurá-la e garantir que ela chegue ao SIEM.

[Imagem 1 — Captura de tela do Visualizador de Eventos do Windows exibindo um evento 4625, com os campos de conta, tipo de *logon* e endereço de origem destacados. Texto alternativo: "Visualizador de Eventos do Windows mostrando uma falha de logon com ID 4625". Captura própria em máquina virtual de laboratório.]

#### Telemetria de rede

Um sensor de rede recebe uma cópia do tráfego, por uma porta espelhada (SPAN) do *switch* ou por um TAP, e enxerga inclusive as máquinas sem agente. O **Zeek** resume cada conexão em uma linha de metadados (`conn.log`, `dns.log`, `rdp.log`), o **Suricata** compara o tráfego com assinaturas e a captura completa guarda os pacotes (PCAP), que o analista abre no **Wireshark**. No Wireshark, o filtro de exibição (`tcp.port == 3389`) escolhe o que mostrar de um arquivo já capturado, enquanto o filtro de captura (`port 3389`, na sintaxe BPF) decide o que gravar. Com TLS, o conteúdo segue cifrado, mas endereços, portas, horários e volumes continuam visíveis. Bejtlich (2013) resume o papel dessa camada: o *endpoint* diz qual conta e qual processo agiram; a rede diz de onde, para onde e quantas vezes.

[Imagem 2 — Captura de tela do Wireshark com o filtro `tcp.port == 3389` aplicado, mostrando a lista de pacotes e o painel de detalhes de uma conexão RDP. Texto alternativo: "Janela do Wireshark com a lista de pacotes de uma conexão de área de trabalho remota". Captura própria em laboratório; o Wireshark é *software* livre (licença GPL).]

#### Arquitetura de referência: Wazuh e Security Onion

Duas plataformas de código aberto servem de referência para esta unidade. No **Wazuh**, o **agente** instalado em cada *endpoint* lê os canais do Windows e os *logs* do Linux e envia os eventos, cifrados, ao **Wazuh server** (o *manager*) pela porta 1514/TCP. No *server*, *decoders* extraem os campos de cada evento e **regras** classificam o que foi visto com um nível de 0 a 15. Os alertas seguem para o **Wazuh indexer**, que os guarda e indexa, e aparecem no **Wazuh dashboard**, a interface do analista. No **Security Onion 2.4**, sensores (*forward nodes*) rodam Zeek, Suricata e a captura de pacotes; o *manager* e os *search nodes* indexam os dados, e o analista trabalha no SOC Console, com as telas Alerts, Hunt, Cases e PCAP.

[Imagem 3 — Diagrama da arquitetura de monitoramento: agentes Wazuh nos servidores e notebooks enviando eventos ao Wazuh server, indexer e dashboard; um sensor Security Onion recebendo a cópia do tráfego e enviando ao *manager*; as duas visões convergindo para o analista do SOC. Texto alternativo: "Diagrama com o fluxo de eventos dos endpoints e da rede até o analista do SOC". Recriado pela equipe a partir da documentação oficial do Wazuh e do Security Onion.]

#### O SIEM: normalizar, correlacionar e reter

O SIEM (*Security Information and Event Management*) centraliza os registros e executa funções-chave. A **normalização** converte formatos diferentes em um esquema comum: o `TargetUserName` do Windows e o endereço de origem do Zeek passam a ocupar campos como `user.name` e `source.ip`, o que permite pesquisar todas as fontes de uma vez. O **enriquecimento** acrescenta contexto, como a criticidade do ativo e o cargo do usuário. A **correlação** combina eventos que, isolados, parecem inofensivos: dez falhas de *logon* (4625) seguidas de um sucesso (4624) da mesma origem, em menos de cinco minutos, sugerem que uma senha foi descoberta.

A **retenção** define por quanto tempo os dados ficam disponíveis. O PCI DSS exige guardar o histórico de auditoria por pelo menos 12 meses, com os 3 meses mais recentes disponíveis para análise imediata. O Marco Civil da Internet (Lei nº 12.965/2014) fixa um ano para registros de conexão e seis meses para registros de acesso a aplicações, para os provedores a que se aplica. O PCAP ocupa muito espaço e costuma ser guardado por poucos dias.

[Imagem 4 — Linha do tempo com dez eventos 4625 em sequência e um 4624 ao final, destacados como uma regra de correlação. Texto alternativo: "Linha do tempo de várias falhas de logon seguidas de um logon bem-sucedido". Recriado pela equipe.]

#### Exemplo numérico: alertas *versus* capacidade

Coletar tudo e alertar sobre tudo produz **fadiga de alertas**: quando quase tudo é falso positivo, o analista fecha alertas no automático. Um SOC recebe 1.800 alertas por dia, e a triagem de cada um leva 10 minutos: 1.800 × 10 = 18.000 minutos, ou **300 horas de análise por dia**. A equipe N1 tem seis analistas, com 6 horas efetivas cada: 36 horas, ou 36 × 60 ÷ 10 = **216 alertas por dia, apenas 12% do volume**. Se 95% dos alertas vêm de cinco regras ruidosas e o ajuste corta 90% do ruído delas, o volume cai para 1.800 − (0,95 × 1.800 × 0,9) ≈ 261 alertas por dia. Ajustar regras costuma render mais do que contratar.

#### Pontos-chave

- Cada camada da defesa em profundidade é também uma fonte de telemetria.
- No Wazuh, o agente coleta, o *server* decodifica e aplica regras, o *indexer* guarda e o *dashboard* mostra.
- O Security Onion acrescenta a visão de rede, com Zeek, Suricata e PCAP.
- Eventos 4624, 4625 e 4688 e o Sysmon só ajudam se estiverem configurados e chegarem ao SIEM.
- Retenção e volume de alertas são decisões de projeto.

### Referências da aula

BEJTLICH, Richard. *The practice of network security monitoring*: understanding incident detection and response. San Francisco: No Starch Press, 2013.

BRASIL. Lei nº 12.965, de 23 de abril de 2014. Estabelece princípios, garantias, direitos e deveres para o uso da Internet no Brasil (Marco Civil da Internet). *Diário Oficial da União*, Brasília, DF, 24 abr. 2014.

KENT, Karen; SOUPPAYA, Murugiah. *SP 800-92*: guide to computer security log management. Gaithersburg: NIST, 2006. DOI: 10.6028/NIST.SP.800-92.

MICROSOFT. *Sysmon*. Sysinternals. Disponível em: <https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon>. Acesso em: 22 nov. 2026.

PCI SECURITY STANDARDS COUNCIL. *Payment card industry data security standard*: requirements and testing procedures. Versão 4.0.1. [*S. l.*]: PCI SSC, 2024.

SANDERS, Chris; SMITH, Jason. *Applied network security monitoring*: collection, detection, and analysis. Waltham: Syngress, 2013.

SECURITY ONION SOLUTIONS. *Security Onion 2.4 documentation*. Disponível em: <https://docs.securityonion.net/>. Acesso em: 22 nov. 2026.

WAZUH. *Wazuh documentation*: architecture. Disponível em: <https://documentation.wazuh.com/current/getting-started/architecture.html>. Acesso em: 22 nov. 2026.

### Roteiro da Videoaula 9 — "Um *login* às 2h da manhã: quem está olhando?"

Duração-alvo: 15 a 20 minutos. Deck: unidade_3/slides/aula9.html (23 slides).

**Slides 1 e 2 — Capa e sumário (0:00–0:30)**
Fala: "Olá! Começamos hoje a Unidade 3, Defesa, Monitoramento e Detecção, em que trocamos de lado e vestimos a camisa azul. Nesta aula, vamos montar a arquitetura de monitoramento da Rede Tatame: *logs*, SIEM e telemetria de *endpoints* e de rede, com o Wazuh e o Security Onion como referência. O sumário mostra o caminho."

**Slide 3 — O problema de hoje na Rede Tatame (0:30–1:40)**
Fala: "Madrugada de sexta-feira, 13 de novembro. A Luiza Ferraz está no plantão do SOC. Às 02:17, alguém entra no SRV-ERP-01, o servidor do sistema financeiro, com a conta da Carla Dias, depois de errar a senha dez vezes. A Carla está dormindo, e a fila já tem centenas de alertas. No mapa à direita, o caminho em destaque sai do notebook NB-FIN-031 e chega ao ERP, em vermelho. A pergunta da aula está no quadro amarelo: que arquitetura de monitoramento a Rede Tatame precisa para que o SOC perceba esse *login* a tempo? O que coletar, por onde os dados passam e onde a Luiza os vê?"
[Take de apoio: sala de monitoramento à noite, analista diante de vários monitores — Envato]

**Slide 4 — O que você verá nesta unidade (1:40–2:10)**
Fala: "Na Unidade 2, executamos as técnicas do adversário em laboratório. Agora a pergunta se inverte. Hoje montamos a arquitetura que enxerga os rastros; na Aula 10, escrevemos regras de detecção; na Aula 11, caçamos o que as regras não viram; e na Aula 12, fortalecemos os sistemas para reduzir a superfície de ataque."

**Slide 5 — Evento, registro e telemetria, camada por camada (2:10–2:50)**
Fala: "Evento é qualquer ocorrência observável; registro é a anotação dela; telemetria é o fluxo contínuo que agentes e sensores enviam. Na defesa em profundidade, cada camada é uma barreira e também uma fonte de dados: um controle que falhou ainda pode deixar rastro. E quem consome esses dados é o SOC, com N1 na triagem, N2 na investigação e N3 na caça e na criação de detecções."

**Slide 6 — Wazuh para o *endpoint*, Security Onion para a rede (2:50–3:40)**
Fala: "Vamos usar duas plataformas de código aberto como referência. No Wazuh, o agente roda em cada servidor e notebook, lê os canais do Windows e os *logs* do Linux e envia tudo ao Wazuh server, na porta 1514. O server decodifica e aplica regras, o indexer guarda e o dashboard mostra ao analista. No Security Onion, um sensor ligado a uma porta espelhada roda o Zeek, que resume cada conexão, o Suricata, que compara o tráfego com assinaturas, e a captura de pacotes. O manager e os search nodes indexam, e o analista usa o SOC Console."

**Slide 7 — Laboratório: o caminho de um evento na arquitetura da Rede Tatame (3:40–5:20)**
Objetivo: seguir o evento das 02:14 até a tela do SOC. Responde a "por onde os dados passam".
Na tela:
1. Ao abrir o slide, o passo "02:14:03 · Gerar" já está na tela (contador 1 / 8), com o nó SRV-ERP-01 aceso.
2. Clicar em "▶ Avançar": "Coletar no endpoint". Pontos azuis saem do ERP e do NB-FIN-031 para o Wazuh server.
3. Avançar por "Decodificar e aplicar regras" e "Indexar e mostrar".
4. Avançar por "A mesma sessão na rede" e "Indexar a rede", em que os pontos ficam amarelos na linha de baixo.
5. Avançar por "Duas visões, um caso" e "O ponto cego".
Fala: "O primeiro passo é o evento 4625 no servidor: falha de *logon* da carla.dias, tipo 10, que é área de trabalho remota, vinda de 10.10.4.31. O agente Wazuh lê o canal Security e manda o evento cifrado ao server pela porta 1514; a 1515 é usada só para registrar o agente. No server, os *decoders* separam campos como targetUserName e ipAddress, e as regras dão ao evento um nível de 0 a 15. Os alertas vão para o indexer e aparecem no dashboard da Luiza. Agora a linha de baixo: o *switch* da sede copia o tráfego para o sensor do Security Onion. O Zeek registra cada conexão do notebook para a porta 3389 do ERP, o Suricata compara com assinaturas e o PCAP guarda os pacotes. No passo 'Duas visões, um caso', reparem que as duas linhas chegam à Luiza: o Wazuh diz qual conta entrou, o Security Onion diz de onde e quantas vezes. O último passo mostra o ponto cego: as catracas das academias não têm agente nem sensor."
Atenção: o botão "⏯ Auto" avança sozinho; para gravar, prefira os cliques manuais. O botão "◀" volta um passo.
Conclusão: "Os dados percorrem dois caminhos, o do *endpoint* e o da rede, e só o que tem agente ou sensor chega ao SOC."
[Tela: gravação do laboratório do slide 7]

**Slide 8 — O que cada fonte revela, e o que precisa ser configurado (5:20–5:55)**
Fala: "No Windows, os eventos 4624, 4625, 4688 e 1102; no Sysmon, os IDs 1, 3 e 22; no Linux, o auth.log e o auditd; e, na rede, o conn.log e o dns.log do Zeek e os alertas do Suricata. O quadro azul traz o recado da aula: o 4688 só grava a linha de comando com uma política habilitada, e o agente Wazuh só lê o Sysmon se o canal dele estiver na configuração."

**Slide 9 — Laboratório: o que um *endpoint* Windows registra, e o que o agente envia (5:55–7:45)**
Objetivo: ver os eventos que um *login* deixa numa máquina Windows e conferir se o agente os coleta. Responde a "o que coletar".
Na tela (PowerShell da VM isolada LAB-WIN11; clicar em "▶ Próximo comando" sete vezes):
1. Get-WinEvent no canal Security, filtrando o Id 4625.
2. Get-WinEvent filtrando o Id 4624 da conta aluno.
3. Instalação do Sysmon com o arquivo sysmonconfig.xml.
4. Start-Process notepad.exe.
5. Leitura do evento ID 1 do Sysmon que menciona o notepad.
6. Get-Service WazuhSvc.
7. Select-String no ossec.conf, procurando as linhas location.
Fala: "O primeiro comando lê as três últimas falhas e monta cinco colunas: hora, Id, conta, tipo de *logon* e origem. No 4625, a conta está na propriedade 5, o tipo na 10 e a origem na 19. Aparecem três falhas da conta aluno, tipo 2, que é teclado. No 4624 as posições mudam, tipo na 8 e origem na 18, e o sucesso vem às 10:02:52: aqui foi só o aluno digitando errado. Instalamos o Sysmon, as linhas verdes confirmam o serviço e o *driver*, abrimos o Bloco de Notas e lemos o evento 1: as linhas destacadas são Image, CommandLine, Hashes, com o SHA-256, e ParentImage, que mostra o PowerShell como processo pai. O Get-Service mostra o agente Wazuh rodando, com o nome WazuhSvc. E o último comando é a surpresa: o ossec.conf lista só Application, Security e System. O Sysmon grava, mas o canal dele não está na lista, então nada do Sysmon chega ao Wazuh. A linha cinza mostra a correção: um bloco localfile com o canal do Sysmon e o formato eventchannel."
Atenção: a saída é simulada e representa uma VM isolada; os horários são da VM, não da madrugada do caso. "⏭ Executar tudo" roda o roteiro inteiro, e "⟲ Reiniciar" limpa o terminal.
Conclusão: "Ter a fonte não basta: ela precisa estar configurada e ligada ao SIEM."
[Tela: gravação do laboratório do slide 9]

**Slide 10 — Laboratório: que telemetria da Rede Tatame chega ao SOC (7:45–9:15)**
Objetivo: descobrir quais fontes da plataforma chegam ao SOC e quanto custa ligar mais uma. Responde a "o que coletar", com a restrição de custo.
Na tela (simulador da disciplina, aberto na aba Telemetria):
1. Rolar até o painel "Volume e custo" e ler os indicadores: "Fontes ligadas 7 de 10", "Ingestão por dia 32,8 GB" e "Custo por mês R$ 2.462".
2. Marcar as chaves "Heartbeat e firmware das catracas" e "Acesso a buckets e saída de rede". Os indicadores passam a 9 de 10, 34,5 GB por dia e R$ 2.586 por mês.
3. Abrir a aba "Filas e eventos" e clicar em "Iniciar", no topo.
4. Clicar em "Parar o encaminhador do SIEM" e observar as barras de atraso.
5. Clicar em "Religar o encaminhador do SIEM" para fechar.
Fala: "Cada linha da lista é uma fonte, com a taxa em eventos por segundo e as regras que dependem dela. Ligar as catracas e a saída de rede soma cerca de 1,6 GB por dia e R$ 124 por mês, valores fictícios do simulador. Na aba Filas e eventos, o Kafka é o barramento: os serviços publicam ali e três consumidores leem, o CEP, o *data lake* e o encaminhador do SIEM. Quando paro o encaminhador, a barra dele fica vermelha e o *lag*, o atraso medido em mensagens, cresce sem parar. Os eventos continuam no Kafka, mas o SOC deixa de vê-los. É o mesmo efeito de um agente parado ou de um canal esquecido no ossec.conf."
Atenção: o simulador roda em tempo acelerado; o *lag* leva uns 10 segundos para ficar visível. Se algo travar, use "Reiniciar", no topo.
Conclusão: "Cada fonte ligada custa dinheiro; cada fonte desligada ou parada é um ponto cego."
[Tela: gravação do laboratório do slide 10, no simulador]

**Slide 11 — O que o pacote mostra que o *log* do servidor não mostra (9:15–9:50)**
Fala: "O sensor recebe uma cópia do tráfego e vê também as máquinas sem agente. O Zeek resume cada conexão; o Wireshark abre os pacotes um a um, a partir do PCAP. Atenção à diferença: o filtro de exibição escolhe o que mostrar de um arquivo já capturado; o filtro de captura, em sintaxe BPF, decide o que gravar. E com TLS o conteúdo vai cifrado, mas endereço, porta, horário e volume continuam visíveis."

**Slide 12 — Laboratório: o *login* das 02:17 visto na rede (9:50–11:50)**
Objetivo: confirmar nos pacotes de onde veio o acesso ao ERP. Responde a "o que coletar na rede".
Na tela (Wireshark simulado, arquivo sede-span_2026-11-13_0213.pcapng, aberto com o filtro ip.addr == 10.10.4.31):
1. Ler a lista de pacotes e a barra de status "Pacotes: 5.812 · Exibidos: 22".
2. Clicar no botão "dns".
3. Clicar no botão "tcp.port == 3389" e depois na linha 4113, de protocolo RDP.
4. Clicar no botão "tcp.flags.syn == 1 && tcp.flags.ack == 0".
5. Clicar no botão "tcp.flags.reset == 1".
Fala: "Cada linha é um pacote, com número, hora, origem, destino, protocolo, tamanho e um resumo. As cores seguem o padrão do Wireshark: azul-claro para DNS, lilás para TCP, verde para TLS. No filtro dns, o notebook pergunta ao AD, 10.10.1.10, o endereço de srv-erp-01.corp.tatame.local e recebe 10.10.1.30. No filtro da porta 3389, vemos o aperto de mão do TCP: SYN, SYN-ACK e ACK. O pacote 4113 é o primeiro do RDP, e o painel de detalhes destaca o *cookie* mstshash=carla.dias: o nome da conta vai em claro antes do TLS. Depois vêm o Client Hello, o certificado do SRV-ERP-01 e Application Data, cifrado. A senha não aparece, e é assim que deve ser. O filtro dos SYN conta os inícios de conexão: 11 para o ERP em pouco mais de três minutos, uma por tentativa de senha, e um para a porta 445 do servidor de arquivos. O último filtro mostra a resposta do SRV-ARQ-01 às 02:19:40: um RST, em vermelho. A conexão foi recusada, mas a rede registrou que alguém tentou ir além do ERP."
Atenção: o arquivo e os pacotes são simulados e os botões substituem a digitação do filtro; digitar um filtro diferente dos cinco deixa a barra vermelha. A barra verde indica filtro válido, como no Wireshark real.
Conclusão: "A rede confirma a origem, o NB-FIN-031, e mostra o passo seguinte, que o *log* do ERP não veria."
[Tela: gravação do laboratório do slide 12]

**Slide 13 — Normalizar, enriquecer, correlacionar e reter (11:50–12:25)**
Fala: "Com dados do *endpoint* e da rede, o SIEM precisa colocá-los no mesmo idioma. No Wazuh, *decoders* e regras fazem esse trabalho; no Security Onion, o Elastic Agent e os *pipelines* de ingestão. A normalização põe o targetUserName do Windows e a origem do Zeek em campos comuns, o enriquecimento acrescenta contexto, a correlação junta dez falhas e um sucesso em cinco minutos, e a retenção decide por quanto tempo tudo fica pesquisável."

**Slide 14 — Antes do código: onde achar e como instalar (12:25–12:45)**
Fala: "O próximo laboratório usa o VS Code com a extensão Python da Microsoft e o Python 3.12, baixados dos *sites* oficiais da tabela. Os módulos json, datetime e collections são da biblioteca padrão, então não há pacote a instalar: basta conferir o nome no índice da documentação do Python. As amostras imitam o que o agente Wazuh lê do Windows e o conn.log do Zeek em JSON."

**Slide 15 — Laboratório: *endpoint* e rede no mesmo esquema (12:45–15:05)**
Objetivo: juntar Windows e Zeek num formato comum e achar o padrão das 02:17. Responde a "correlacionar".
Na tela (VS Code em tela cheia, pasta normalizacao; o roteiro do laboratório abre com a tecla G ou com o botão "☰ Roteiro" da barra de status e fica fechado durante a gravação):
1. Clicar em "⬇ Preparar o ambiente", na barra do terminal, e esperar o botão mudar para "✓ Ambiente pronto".
2. Com normalizar.py aberto, mostrar as linhas destacadas 6 a 13 (MAPA_WINDOWS) e 29 a 31 (campos do Zeek).
3. No explorador, abrir amostras/windows_seguranca.jsonl e amostras/zeek_conn.log.
4. Clicar em "▶ Normalizar".
5. Abrir correlacao.py, mostrar as linhas destacadas 7, 8, 16, 17, 21 e 24 a 26 e clicar em "▶ Correlacionar".
Fala: "Primeiro o ambiente: a versão do Python, 3.12.7; a criação do ambiente virtual, a pasta .venv; a ativação, que muda o *prompt*; e o pip list, que mostra só o próprio pip, porque o código usa apenas a biblioteca padrão. Agora o código. O dicionário MAPA_WINDOWS diz que TimeCreated vira @timestamp, TargetUserName vira user.name e IpAddress vira source.ip. A função de_zeek faz o mesmo com o conn.log: id.orig_h vira source.ip, id.resp_h vira destination.ip e id.resp_p vira destination.port. O horário do Zeek vem em segundos desde 1970 e é convertido para o fuso de Brasília, para que as duas fontes fiquem na mesma linha do tempo. Ao normalizar, a saída diz 28 eventos: 13 do Zeek e 15 do Windows. O primeiro, às 02:14:01, é uma conexão do Zeek para a porta 3389; o segundo, dois segundos depois, é a primeira falha da carla.dias. Agora a correlação. A linha 7 define o limiar de 10 falhas e a linha 8 a janela de 5 minutos. As linhas 16 e 17 descartam falhas antigas; a linha 21 decide: com 10 ou mais falhas guardadas, sai o alerta. As linhas 24 a 26 vão à rede e contam as conexões RDP da mesma origem perto do horário do sucesso. O resultado em vermelho mostra carla.dias no SRV-ERP-01, 10 falhas e sucesso às 02:17:12 a partir de 10.10.4.31, e a linha azul confirma: 11 conexões RDP para 10.10.1.30, entre 02:14:01 e 02:17:10. A ana.lima errou duas vezes e entrou, abaixo do limiar, e o caio.mendes entrou sem errar."
Atenção: o código é ilustrativo e roda apenas na simulação; a preparação do ambiente também é simulada (cerca de 5 segundos). Os nomes de campos imitam o ECS (*Elastic Common Schema*).
Conclusão: "Com campos comuns, uma regra simples encontra o *login* das 02:17, e a rede confirma a origem."
[Tela: gravação do laboratório do slide 15]

**Slide 16 — Laboratório: os mesmos eventos no painel do Wazuh (15:05–16:45)**
Objetivo: confirmar no Wazuh o que houve às 02:17, o que veio depois e até quando dá para olhar para trás. Responde a "onde o analista vê" e a "guardar".
Na tela (console com a aparência do Wazuh; a busca 1 roda sozinha ao abrir o slide):
1. Ler o resultado de "1. Falhas de logon por agente".
2. Clicar em "2. Regra local: sucesso após falhas".
3. Clicar em "3. O que rodou depois no ERP?", no grupo Endpoint.
4. Clicar em "4. Até quando dá para olhar?", no grupo Retenção.
Fala: "A busca 1 filtra a regra 60122, que o Wazuh usa para falha de *logon* do Windows, o evento 4625. São 214 alertas no dia; o histograma tem uma barra por hora e a das 02h está destacada. Quem lidera é a conta de serviço svc-backup, com 96 falhas, 4 por hora o dia inteiro, por causa de uma senha vencida: volume alto, mas ruído conhecido. A busca 2 procura a regra 100100, uma regra local, escrita pela própria Rede Tatame no arquivo local_rules.xml, onde as regras próprias usam IDs a partir de 100000. Ela dispara uma vez, às 02:17:12, para carla.dias, com nível 12 e a técnica T1110 do ATT&CK. A busca 3 mostra os eventos 1 do Sysmon no ERP depois do *login*: o rdpclip, normal numa sessão remota, e em seguida whoami /groups e net user carla.dias /domain, comandos de descoberta às 2h da manhã. Isso só aparece porque o canal do Sysmon foi incluído no ossec.conf. A busca 4 compara a retenção: alertas do Wazuh com 365 dias, eventos brutos e *logs* do Zeek com 90, e o PCAP com apenas 7."
Atenção: o texto da consulta é digitado aos poucos antes do resultado; espere a tabela completar antes de comentar. O botão "Pesquisar" repete a busca selecionada. Em cada busca, a nota abaixo da tabela resume a leitura.
Conclusão: "Volume alto não indica ataque. A regra de correlação e o contexto separam o ruído do svc-backup da ameaça na conta da carla.dias."
[Tela: gravação do laboratório do slide 16]

**Slide 17 — Laboratório: a catraca adulterada, sem e com a fonte certa (16:45–18:05)**
Objetivo: provar, na plataforma, que uma regra só dispara se a fonte estiver ligada e a regra ativa. Responde a "coletar" e "correlacionar" juntos.
Na tela (simulador na aba Cenários, com a fonte das catracas e a regra R10 desligadas):
1. No cartão "Catraca adulterada", clicar em "Iniciar cenário" e esperar os três passos, cerca de 20 segundos.
2. Na aba Telemetria, ligar "Heartbeat e firmware das catracas".
3. Na aba Regras do CEP, ligar "R10 · Catraca fora do padrão (volume ou firmware)".
4. Voltar a Cenários e clicar em "Repetir com as fontes e regras atuais".
5. Na aba SOC, clicar em "Investigar" no alerta da R10.
Fala: "Na primeira rodada, os dois primeiros passos recebem a etiqueta 'não detectado': a fonte das catracas está desligada, é o ponto cego que vimos no fluxo do slide 7. O terceiro passo, os *check-ins* falsos, fica 'visto nos logs, sem alerta': o API *gateway* registrou, mas nenhuma regra olha para isso. Depois de ligar a fonte e a R10, a segunda rodada marca os dois primeiros passos como 'detectado', e no SOC o painel de investigação mostra a lógica da regra e a linha do tempo correlacionada."
Atenção: o alerta chega alguns segundos depois do passo, porque a regra precisa correlacionar. Na aba SOC pode aparecer também um alerta benigno de outra regra; ignore-o nesta gravação.
Conclusão: "Para avisar o SOC, a Rede Tatame precisa das duas coisas: a fonte ligada e a regra ativa."
[Tela: gravação do laboratório do slide 17, no simulador]

**Slide 18 — Guardar o bastante e alertar só o que cabe (18:05–18:35)**
Fala: "Duas decisões de projeto fecham a arquitetura. Retenção: o PCI DSS pede 12 meses, com 3 para análise imediata, e o Marco Civil fixa prazos para alguns provedores. E volume: 1.800 alertas por dia vezes 10 minutos são 300 horas de análise; seis analistas com 6 horas efetivas triam 216 alertas, 12% do total. Ajustando as cinco regras ruidosas, a fila cai para cerca de 261."

**Slide 19 — Laboratório: calculadora de alertas e capacidade do SOC (18:35–19:15)**
Objetivo: verificar se o alerta das 02:17 cabe na fila. Responde a "a tempo, sem se afogar em alertas".
Na tela:
1. Ler os valores iniciais: demanda de 300 h por dia (1.800 alertas), capacidade de 36 h por dia (216 alertas), cobertura de 12%.
2. Subir "Analistas N1" de 6 para 8.
3. Voltar a 6 e subir "Ruído cortado nessas regras" para 90%.
4. Baixar "Minutos de triagem por alerta" de 10 para 6.
Fala: "Com oito analistas, a capacidade vai a 288 alertas e a cobertura só a 16%. Com seis analistas e 90% do ruído cortado, a demanda cai para 261 alertas e a cobertura salta para 82,8%. Com triagem de 6 minutos, a equipe tria 360 alertas e o indicador mostra 'cabe tudo'."
Atenção: a calculadora usa um tempo médio fixo de triagem por alerta; na prática ele varia com o tipo de alerta. Volte cada controle ao valor inicial antes de mexer no próximo, para isolar o efeito de cada mudança.
Conclusão: "Ajustar regras rende mais do que contratar, e é isso que garante que o alerta da carla.dias seja lido."
[Tela: gravação do laboratório do slide 19]

**Slide 20 — De volta ao problema (19:15–19:45)**
Fala: "Voltemos à Luiza. Os cartões resumem a resposta: agentes Wazuh no ERP e nos notebooks, com o Sysmon configurado; um sensor do Security Onion na porta espelhada, com Zeek e PCAP; normalização e correlação para a regra achar a carla.dias às 02:17:12; e retenção e volume de alertas dimensionados. Respondendo à pergunta da aula: agentes e sensor enviam telemetria a um SIEM que normaliza, correlaciona e guarda, e a Luiza vê o alerta no painel, com contexto, numa fila que cabe na equipe."

**Slides 21 a 23 — Pontos-chave, referências e encerramento (19:45–20:00)**
Fala: "Para levar desta aula: cada camada é uma fonte de telemetria, o Wazuh cuida do *endpoint*, o Security Onion da rede, e fonte sem configuração não detecta nada. Na próxima aula, vamos escrever as regras: assinatura, comportamento e correlação."

[Envato: "security operations center night", "network switch cables", "server logs scrolling screen". Slides de apoio: mini-mapa do slide 3, fluxo do slide 7 e cartões do slide 20.]

## Aula 10 — Detecção baseada em assinaturas, comportamento e regras

### Texto base

Na aula anterior, montamos a arquitetura de monitoramento: agentes coletam registros e telemetria dos *endpoints*, sensores observam a rede e o SIEM centraliza tudo. Mas dados só viram alerta quando alguém diz **o que procurar**. Nesta aula, vamos comparar as três grandes famílias de detecção (assinatura, comportamento e regra de correlação), ver como cada uma é escrita em ferramentas abertas como YARA, Suricata, Sigma e Wazuh, e aprender a medir e ajustar uma regra para que ela dispare quando o ataque acontece sem afogar o SOC em falsos positivos.

#### Três famílias de detecção

| Família | Pergunta que faz | Exemplos | Força | Limite |
|---|---|---|---|---|
| Assinatura | "Já vi exatamente isto?" | *Hash*, regra YARA, assinatura do Suricata | Precisa e barata | Só reconhece o que já é conhecido |
| Comportamento | "Isto se parece com a técnica?" | Árvore de processos no EDR, desvio da linha de base | Resiste à troca de ferramenta | Exige conhecer o ambiente |
| Regra e correlação | "Estes eventos, juntos, formam um ataque?" | Regras do Wazuh, Sigma | Junta fontes e aumenta a confiança | Depende de dados normalizados e de ajuste |

As famílias não competem entre si. Uma boa estratégia usa a assinatura para o conhecido, o comportamento para a técnica e a correlação para transformar pistas fracas em um alerta forte.

#### Assinaturas: *hash*, YARA e Suricata

A assinatura mais simples é o ***hash*** criptográfico de um arquivo, como o SHA-256. Ele é exato: se um único *byte* mudar, o *hash* muda por inteiro. Isso torna a comparação precisa, mas também trivial de contornar, porque basta o adversário recompilar a ferramenta ou alterar um texto.

O **YARA**, mantido pelo VirusTotal, descreve famílias de arquivos por **trechos** (textos, sequências de *bytes* ou expressões regulares) e por uma **condição** que combina esses trechos. A regra abaixo, didática e aplicada a uma nota de resgate fictícia, exige o identificador da vítima e mais um dos dois textos típicos do grupo:

```
rule Cobalto_Nota_Resgate_v2
{
    strings:
        $grupo = "COBALTO AUSTRAL"
        $frase = "arquivos foram cifrados" nocase
        $id    = /CA-[0-9]{4}-[A-Z]{3,10}/
    condition:
        filesize < 10KB and $id and ($grupo or $frase)
}
```

Na rede, o mesmo princípio aparece no **Suricata**, o sensor de detecção de intrusão usado no Security Onion. Cada regra tem um cabeçalho (ação, protocolo, origem e destino) e opções entre parênteses, como `content`, a mensagem `msg` e o identificador `sid`.

[Imagem 1 — Duas colunas: à esquerda, um arquivo com três trechos destacados e a condição YARA; à direita, um pacote HTTP com o cabeçalho User-Agent destacado por uma regra do Suricata. Texto alternativo: "Comparação entre uma regra YARA aplicada a um arquivo e uma assinatura do Suricata aplicada ao tráfego de rede". Pode ser recriado pela equipe a partir da descrição.]

#### Comportamento: detectar a técnica

A detecção comportamental olha **o que o processo faz**: quem o iniciou, com que linha de comando, que arquivo alterou, que conexão abriu. O Sysmon (evento 1, criação de processo) e o EDR fornecem essa árvore de processos. Um exemplo clássico é a técnica T1490 do MITRE ATT&CK (*Inhibit System Recovery*): antes de cifrar, muitos grupos de *ransomware* tentam apagar as cópias de sombra do Windows. O nome do arquivo do invasor muda a cada campanha, mas o pedido ao sistema operacional continua o mesmo.

Uma variante é a detecção por **anomalia**, que compara o presente com a linha de base (*baseline*) do próprio ambiente: uma catraca que envia dez *heartbeats* por segundo, em vez de um a cada 30 segundos, é anômala, qualquer que seja a causa.

A **Pirâmide da Dor**, proposta por David Bianco em 2013, organiza essa ideia. Na base ficam *hashes*, endereços IP e domínios, que o adversário troca com facilidade; no topo ficam ferramentas e TTPs (táticas, técnicas e procedimentos), cuja detecção o obriga a mudar o modo de operar.

[Imagem 2 — Pirâmide de seis camadas, da base ao topo: valores de *hash*, endereços IP, nomes de domínio, artefatos de rede e de *host*, ferramentas e TTPs, com uma seta lateral indicando "custo para o adversário" crescente. Texto alternativo: "Pirâmide da Dor de David Bianco, com o custo imposto ao adversário aumentando da base ao topo". Pode ser recriada pela equipe a partir de BIANCO (2013).]

#### Regras e correlação: Wazuh e Sigma

No **Wazuh**, o **decodificador** extrai os campos de cada evento e as **regras**, escritas em XML, decidem o que vira alerta. Regras próprias usam identificadores de 100000 a 120000, e o nível (`level`) vai de 0 a 15; nível 0 não gera alerta. Os elementos `if_sid` e `if_group` encadeiam uma regra a outra, `field` compara um campo com uma expressão regular, `mitre` associa a técnica ATT&CK, e `frequency` com `timeframe` correlaciona repetições, como "20 falhas de *login* em 60 segundos". Uma regra-filha de nível 0 funciona como **exceção** da regra-mãe.

O **Sigma** é um formato aberto, em YAML, para escrever a lógica uma única vez, com fonte de dados, técnica ATT&CK e falsos positivos esperados, e convertê-la para a linguagem de diferentes SIEMs. Em ambos os casos, a regra vale como código: fica em repositório, passa por revisão e é **testada antes de ser publicada**, por exemplo com o utilitário `wazuh-logtest`, que mostra qual regra um evento aciona.

[Imagem 3 — Captura do painel do Wazuh (módulo *Threat Hunting*) com a lista de alertas filtrada por `rule.id`, mostrando colunas de nível, agente e técnica ATT&CK. Texto alternativo: "Painel do Wazuh exibindo alertas de uma regra personalizada com nível e técnica MITRE ATT&CK". Captura própria em máquina de laboratório.]

#### Falso positivo, falso negativo e ajuste

Um **falso positivo** é um alerta sem ataque; um **falso negativo** é um ataque sem alerta. Dois indicadores orientam o ajuste: a **precisão** (dos alertas gerados, quantos eram ataque) e a **sensibilidade** ou *recall* (dos ataques que aconteceram, quantos viraram alerta). Ajustar quase sempre é uma troca entre os dois, e a regra de ouro é fazer exceções **específicas**: por conta, processo pai e parâmetro, nunca por servidor inteiro.

#### Exemplo numérico

Em 30 dias, uma regra que detecta a exclusão de cópias de sombra gerou 252 alertas: 240 vieram da rotina noturna de *backup* de um servidor de arquivos (8 por dia), 2 de uma limpeza manual feita pelo administrador e 10 de emulações autorizadas do Red Team (4 no servidor de arquivos e 6 no ERP). A precisão era de 10 ÷ 252 ≈ **4,0%**, com sensibilidade de 10 ÷ 10 = 100%.

Com uma exceção específica (conta de *backup* e parâmetro que apaga só a cópia mais antiga), sobram 12 alertas, dos quais 10 verdadeiros: precisão de 10 ÷ 12 ≈ **83,3%** e sensibilidade mantida em 100%. Se, em vez disso, a equipe ignorasse o servidor de arquivos inteiro, restariam 8 alertas (6 verdadeiros): precisão de 6 ÷ 8 = 75%, mas sensibilidade de 6 ÷ 10 = **60%**. A fila fica limpa e o SOC fica cego em 4 dos 10 ataques.

[Imagem 4 — Gráfico de barras agrupadas com as três versões da regra (sem exceção, exceção específica, exceção ampla), mostrando precisão e sensibilidade em porcentagem. Texto alternativo: "Gráfico comparando precisão e sensibilidade de uma regra de detecção antes e depois de dois tipos de ajuste". Pode ser recriado pela equipe com os números do exemplo.]

#### Pontos-chave

- Assinaturas (*hash*, YARA, Suricata) reconhecem o conhecido com precisão, mas o adversário troca o artefato com facilidade.
- Detecções de comportamento miram a técnica e resistem à troca de ferramenta, como sugere a Pirâmide da Dor.
- Regras e correlação, no Wazuh ou em Sigma, juntam eventos em um alerta com contexto e técnica ATT&CK.
- Toda regra é testada antes de publicar e ajustada com exceções específicas.
- Precisão e sensibilidade medem o ajuste: cortar ruído não pode cegar o SOC.

### Referências da aula

BIANCO, David J. *The pyramid of pain*. Enterprise Detection & Response, 1 mar. 2013. Disponível em: <https://detect-respond.blogspot.com/2013/03/the-pyramid-of-pain.html>. Acesso em: 22 nov. 2026.

MITRE. *Inhibit system recovery (T1490)*. MITRE ATT&CK. Disponível em: <https://attack.mitre.org/techniques/T1490/>. Acesso em: 22 nov. 2026.

OPEN INFORMATION SECURITY FOUNDATION. *Suricata user guide*: rules. Disponível em: <https://docs.suricata.io/>. Acesso em: 22 nov. 2026.

SANDERS, Chris; SMITH, Jason. *Applied network security monitoring*: collection, detection, and analysis. Waltham: Syngress, 2013.

SIGMAHQ. *Sigma*: generic signature format for SIEM systems. Disponível em: <https://github.com/SigmaHQ/sigma>. Acesso em: 22 nov. 2026.

VIRUSTOTAL. *YARA documentation*: writing YARA rules. Disponível em: <https://yara.readthedocs.io/>. Acesso em: 22 nov. 2026.

WAZUH. *Wazuh documentation*: rules syntax. Disponível em: <https://documentation.wazuh.com/current/user-manual/ruleset/ruleset-xml-syntax/rules.html>. Acesso em: 22 nov. 2026.

### Roteiro da Videoaula 10 — "Uma lista de 5 mil *hashes* pega o *ransomware*?"

Duração-alvo: 15 a 20 minutos. Deck: unidade_3/slides/aula10.html (18 slides).

**Slides 1 e 2 — Capa e sumário (0:00–0:40)**
Fala: "Olá! Na aula passada, montamos a arquitetura de monitoramento da Rede Tatame. Hoje vamos decidir o que essa arquitetura deve procurar. Vamos comparar três famílias de detecção, assinatura, comportamento e regra de correlação, escrever uma regra YARA e uma regra do Wazuh, testar as duas e medir se o ajuste ajudou ou atrapalhou. O sumário mostra os cinco laboratórios do caminho."

**Slide 3 — O problema de hoje na Rede Tatame (0:40–2:00)**
Fala: "Conheçam o Rafael Tavares, engenheiro de detecção da Rede Tatame. Um fornecedor oferece a ele uma lista com 5 mil *hashes* de arquivos do Grupo Cobalto Austral, o adversário fictício que emulamos na disciplina. Parece ótimo. Só que, ao mesmo tempo, a regra que vigia a exclusão de cópias de sombra gerou 252 alertas em 30 dias, e a Luiza Ferraz, no SOC, já fecha esses alertas sem ler. No mapa à direita, o caminho em destaque vai da internet, pela VPN e pelo AD, até o ERP, em vermelho. A pergunta da aula está no quadro amarelo: que combinação de assinaturas, comportamento e regras detecta o Cobalto Austral mesmo quando ele troca de ferramenta, sem afogar o SOC?"
[Take de apoio: analista diante de uma fila longa de alertas em vários monitores — Envato]

**Slide 4 — Três famílias de detecção (2:00–3:00)**
Fala: "A tabela organiza a aula. A assinatura pergunta 'já vi exatamente isto?', e é precisa e barata, mas só reconhece o que já é conhecido. O comportamento pergunta 'isto se parece com a técnica?', e resiste à troca de ferramenta, mas exige conhecer o ambiente. A regra de correlação pergunta 'estes eventos, juntos, formam um ataque?', e junta fontes diferentes, mas depende de dados normalizados e de ajuste. Reparem no quadro azul: as três se completam."

**Slide 5 — Laboratório: o Cobalto Austral diante de três detectores (3:00–5:00)**
Objetivo: ver o que cada família enxerga no mesmo ataque emulado. Responde à parte "mesmo quando ele troca de ferramenta".
Na tela:
1. Ao abrir o slide, o passo "1 · A ferramenta conhecida" está na tela (contador 1 / 7).
2. Clicar em "▶ Avançar" para "2 · Um byte a mais": o nó "Passou" acende em amarelo.
3. Avançar para "3 · A assinatura por padrão" e "4 · O comportamento".
4. Avançar para "5 · A correlação", "6 · Um alerta com contexto" e "Conclusão · A Pirâmide da Dor".
Fala: "À esquerda, o Cobalto Austral, emulado pelo Bruno Sato, líder do Red Team. No passo 1, a nota de resgate conhecida tem o *hash* na lista do fornecedor, e a assinatura exata funciona. No passo 2, o grupo muda só o identificador da vítima: o *hash* muda por inteiro e a lista de 5 mil *hashes* não serve mais. Vejam a linha tracejada indo para 'Passou'. No passo 3, a regra YARA procura trechos que se repetem em toda a família e reconhece a variante. No passo 4, antes de cifrar, o grupo pede ao Windows para apagar as cópias de sombra, a técnica T1490; o Sysmon registra o processo e a regra 100210 do Wazuh gera um alerta de nível 12, qualquer que seja a ferramenta. No passo 5, um *login* na VPN sem MFA e uma consulta grande ao AD, sozinhos, parecem rotina; do mesmo usuário, em dez minutos, viram um alerta mais forte. No passo 6, tudo chega à Luiza como um alerta só, com contexto. A conclusão é a Pirâmide da Dor: o *hash* está na base, fácil de trocar; a técnica está no topo."
Atenção: o botão "⏯ Auto" avança sozinho a cada 3,8 segundos; para gravar, prefira os cliques manuais. As bolinhas animadas são eventos em trânsito, não pacotes reais.
Conclusão: "Cada família pega um pedaço; juntas, elas acompanham o adversário quando ele troca de ferramenta."
[Tela: gravação do laboratório do slide 5]

**Slide 6 — Assinaturas: *hash*, YARA e Suricata (5:00–6:10)**
Fala: "À esquerda, a regra YARA que vamos rodar daqui a pouco. Em strings ficam três trechos: o nome do grupo, a frase 'arquivos foram cifrados', sem diferenciar maiúsculas, graças ao nocase, e uma expressão regular para o identificador da vítima: CA, quatro dígitos e um nome. Em condition, a regra exige arquivo menor que 10 KB, o identificador e mais um dos dois textos. À direita, o mesmo princípio na rede: uma assinatura do Suricata, o sensor de rede do Security Onion. O cabeçalho diz 'alerte tráfego HTTP de qualquer origem para a nossa rede'; as opções procuram, no cabeçalho User-Agent, o texto 'Nmap Scripting Engine', típico de uma varredura. O sid identifica a regra e o rev, a versão."

**Slide 7 — Antes do código: onde achar e como instalar (6:10–6:50)**
Fala: "O laboratório usa o VS Code com a extensão Python, o Python 3.12 e um único pacote de terceiros, o yara-python 4.5.4. Cuidado com o nome: no código escrevemos import yara, mas o pacote oficial no PyPI chama-se yara-python, mantido pelo VirusTotal. Partam do repositório do projeto e sigam o *link* para o PyPI, em vez de adivinhar o nome. O hashlib e o pathlib já vêm com o Python. E as amostras são textos fictícios e inofensivos: regra YARA se testa sem *malware* real."

**Slide 8 — Laboratório: lista de *hashes* contra regra YARA (6:50–9:40)**
Objetivo: comparar a assinatura exata com a assinatura por padrão nas mesmas quatro amostras. Responde a "a lista de *hashes* basta?".
Na tela (VS Code em tela inteira, pasta yara-cobalto; o roteiro do laboratório abre com a tecla G ou com o botão "☰ Roteiro" da barra de status e fica fechado durante a gravação):
1. Clicar em "⬇ Preparar o ambiente" e esperar o botão mudar para "✓ Ambiente pronto".
2. No explorador, abrir varrer.py e mostrar as linhas destacadas 10, 17, 18 e 19.
3. Abrir iocs/hashes_conhecidos.txt e amostras/leia-me_v2.txt.
4. Abrir regras/cobalto_v1.yar (linhas 7 a 10 destacadas) e clicar em "▶ Varrer com a regra v1".
5. Clicar em "▶ Varrer com a regra v2"; o editor abre regras/cobalto_v2.yar (linhas 8 a 12 destacadas).
Fala: "Primeiro a preparação: Python 3.12.7, o ambiente virtual .venv, a ativação, que acrescenta .venv ao *prompt*, a instalação do yara-python 4.5.4 a partir do requirements.txt e a conferência, que imprime 4.5.4. Agora o código. A linha 10 do varrer.py lê a lista de *hashes* publicada no relatório de inteligência; ela tem um único SHA-256, o da leia-me_v1. Para cada amostra, a linha 17 calcula o SHA-256, a 18 compara com a lista e a 19 aplica a regra YARA. Comparem a leia-me_v2 com a v1: só mudou o identificador da vítima e uma palavra da frase. Rodando a regra v1, a coluna 'hash IOC' diz 'sim' só para a leia-me_v1, que começa por 7f11ac785aa0; a v2, com *hash* 86997d269c98, passa batida pela lista. A coluna YARA mostra que a regra v1 pegou as duas notas, mas pegou também o briefing_cti.txt, em amarelo: o próprio resumo de inteligência do SOC, que cita o nome do grupo e a frase. É um falso positivo, causado pela condição 'any of them', qualquer um dos trechos. A regra v2 exige o identificador da vítima. Rodando de novo, o *briefing* fica com traço, e as duas notas aparecem com os três trechos encontrados, $grupo, $frase e $id. O relatório financeiro nunca dispara."
Atenção: o código é real e foi executado com yara-python 4.5.4; os *hashes* aparecem abreviados nos 12 primeiros caracteres. A preparação do ambiente é simulada e leva uns 6 segundos. As cores amarela e verde na saída são só destaque do laboratório.
Conclusão: "A assinatura por padrão pega a variante que a lista de *hashes* perdeu, e uma condição bem escrita evita o falso positivo."
[Tela: gravação do laboratório do slide 8]

**Slide 9 — Comportamento: detectar a técnica, e não a ferramenta (9:40–10:40)**
Fala: "Se o grupo reescrever a nota inteira, até a YARA perde. Por isso subimos na pirâmide. A detecção de comportamento olha o que o processo faz: quem o iniciou, com que linha de comando, que conexão abriu. É o que o Sysmon, no evento 1, e o EDR entregam. Antes de cifrar, o *ransomware* tenta apagar as cópias de sombra, a técnica T1490; o nome do arquivo do invasor muda, mas o pedido ao Windows é o mesmo. A anomalia compara com a linha de base do ambiente, como a catraca que manda dez *heartbeats* por segundo. E a Pirâmide da Dor, de David Bianco, resume: bloquear *hash*, IP ou domínio custa pouco ao adversário; detectar técnicas o obriga a mudar o modo de operar."

**Slide 10 — Uma regra do Wazuh, com exceção (10:40–11:50)**
Fala: "Esta é a regra 100210, no arquivo local_rules.xml do gerenciador Wazuh. Ela depende do grupo sysmon_event1, ou seja, só olha criação de processo. O primeiro field exige que a imagem termine em vssadmin.exe; o segundo, que a linha de comando contenha 'delete shadows'. O nível é 12, e o bloco mitre associa a T1490. Logo abaixo, a regra 100211, filha da 100210 pelo if_sid, tem nível 0: quando a conta é svc-backup e o comando tem /oldest, ela vence e nenhum alerta sai. Essa é a forma de escrever exceções no Wazuh. Do lado direito: o decodificador extrai os campos e a regra decide; regras próprias usam ids de 100000 a 120000 e níveis de 0 a 15; frequency e timeframe fazem correlação por repetição. E o Sigma é o formato aberto para escrever a mesma lógica uma vez e convertê-la para vários SIEMs."

**Slide 11 — Laboratório: teste no wazuh-logtest (11:50–14:10)**
Objetivo: provar, antes de publicar, que a regra dispara no ataque emulado e fica quieta no *backup*. Responde a "a regra dispara de verdade?".
Na tela (terminal do gerenciador Wazuh do laboratório; clicar em "▶ Próximo comando" cinco vezes):
1. O grep conta as regras de local_rules.xml: saída 2.
2. sudo /var/ossec/bin/wazuh-logtest: "Starting wazuh-logtest v4.14.10".
3. Evento 1: vssadmin.exe delete shadows /all /quiet no SRV-ERP-01.
4. Evento 2: vssadmin.exe delete shadows /for=D: /oldest /quiet no SRV-ARQ-01, conta svc-backup.
5. Evento 3: atualiza.exe delete shadows /all /quiet, com originalFileName VSSADMIN.EXE.
Fala: "O wazuh-logtest passa um evento pelos decodificadores e pelas regras e mostra o resultado em três fases, sem gerar alerta de verdade. Cada linha que colamos é um evento do Sysmon em JSON. O evento 1 é a emulação autorizada do Bruno no ERP. Na fase 2, o decodificador windows_eventchannel extrai a imagem; na fase 3, aparecem o id 100210, o nível 12, a técnica T1490, a tática Impact e a frase 'Alert to be generated'. O evento 2 é a rotina de *backup*: a fase 3 mostra a 100211 com nível 0, e nenhum alerta é gerado. O evento 3 é a surpresa: a mesma técnica, com o vssadmin copiado e renomeado para atualiza.exe. A imagem não termina mais em vssadmin.exe, e o evento cai só na regra-base 61603 do Wazuh, 'Process creation', de nível 0. É um falso negativo, encontrado no teste, e não no incidente. O campo originalFileName ainda diz VSSADMIN.EXE, porque vem dos metadados do executável; a linha amarela registra o ajuste: comparar esse campo, e não o caminho."
Atenção: o terminal é simulado. As linhas iniciadas por # são anotações do laboratório, não saída do Wazuh. No Wazuh real, eventos do Windows colados no logtest precisam estar no formato do EventChannel. "⏭ Executar tudo" roda o roteiro inteiro e "⟲ Reiniciar" limpa a tela.
Conclusão: "Uma regra só é confiável depois de testada com o ataque e com o legítimo, e o teste pode revelar o falso negativo antes do invasor."
[Tela: gravação do laboratório do slide 11]

**Slide 12 — Falso positivo, falso negativo e ajuste (14:10–15:10)**
Fala: "Agora os números do problema. Em 30 dias, a regra 100210 gerou 252 alertas: 240 do *backup* do SRV-ARQ-01, oito por dia, 2 de limpeza manual do Caio Mendes no ERP e 10 das emulações do Bruno, 4 no servidor de arquivos e 6 no ERP. Precisão é, dos alertas, quantos eram ataque: 10 em 252, cerca de 4%. Sensibilidade é, dos ataques, quantos viraram alerta: 10 em 10, 100%. Com a exceção específica, sobram 12 alertas, precisão de 83,3% e sensibilidade de 100%. Com a exceção ampla, ignorando o servidor inteiro, sobram 8 alertas e a precisão é de 75%, mas a sensibilidade cai para 60%."

**Slide 13 — Laboratório: ajustar o falso positivo sem cegar o SOC (15:10–16:40)**
Objetivo: escolher a exceção que corta o ruído sem perder ataques. Responde a "sem afogar o SOC".
Na tela (painel com a aparência do Wazuh, módulo Threat Hunting):
1. Ler a versão "Sem exceção", que abre selecionada.
2. Clicar em "Exceção específica (100211)".
3. Clicar em "Exceção ampla (SRV-ARQ-01)".
Fala: "Na barra DQL está o filtro rule.id:100210. Os seis indicadores mostram alertas, verdadeiros, falsos positivos, ataques perdidos, precisão e sensibilidade, e a tabela agrupa os alertas por agente, usuário e linha de comando, com a classificação que o SOC deu. Sem exceção: 252 alertas, 242 falsos positivos, precisão de 4,0%. Na exceção específica, a linha dos 240 alertas do svc-backup fica riscada, suprimida, e os indicadores mostram 12 alertas, 10 verdadeiros, precisão de 83,3% e sensibilidade de 100%. Os 2 que sobram são as limpezas manuais do Caio, que pedem uma conversa com a TI, e não outra exceção. Na exceção ampla, a fila cai para 8, mas a linha dos 4 ataques emulados no SRV-ARQ-01 fica riscada, com a classificação 'ataque perdido', e a sensibilidade cai para 60%."
Atenção: o painel imita o Wazuh, mas é uma simulação com os números do exemplo do texto base. Os comandos da tabela são registros do Sysmon vistos pelo defensor.
Conclusão: "A exceção específica leva a precisão de 4,0% a 83,3% e mantém todos os ataques; a ampla limpa a fila e cega o SOC."
[Tela: gravação do laboratório do slide 13]

**Slide 14 — Laboratório: uma regra desligada é um ataque que passa (16:40–18:40)**
Objetivo: ver, na plataforma, a diferença entre telemetria que chega e regra que dispara. Responde a "a regra precisa estar ativa e testada".
Na tela (simulador da disciplina, aberto na aba Cenários, já reiniciado, com a R3 desligada):
1. No cartão "Abuso da API do app", clicar em "Iniciar cenário" e esperar os quatro passos, cerca de 30 segundos.
2. Abrir a aba "Regras do CEP", marcar "R3 · Token lendo fichas de muitos alunos diferentes (BOLA)" e ler a lógica embaixo dela.
3. Voltar a "Cenários" e clicar em "Repetir com as fontes e regras atuais".
4. Abrir a aba "SOC" e clicar em "Investigar" no alerta da R3.
Fala: "O cenário tem quatro passos: 2.000 tentativas de *login* com senhas vazadas, 14 contas que entram e a leitura de fichas de outros alunos trocando o id na URL, que é o BOLA, em dois momentos. O primeiro passo fica 'detectado' pela R2, uma regra de correlação: muitas falhas seguidas de sucesso da mesma origem. Os outros ficam amarelos, 'visto nos logs, sem alerta': o *log* do API *gateway* está ligado, mas a R3 está desligada. Embaixo de cada passo aparecem a técnica, a fonte e a regra. A lógica da R3 conta, por *token*, quantos alunos diferentes foram lidos em um minuto e alerta acima de 20 quando o aluno lido não é o dono do *token*: é comportamento, e não assinatura. Na segunda rodada, os dois passos de leitura viram 'detectado'. No SOC, a investigação mostra a lógica da regra e a linha do tempo correlacionada."
Atenção: o simulador roda em tempo acelerado (1 s = 15 s), e o alerta chega alguns segundos depois do passo, porque a regra precisa correlacionar. O passo "14 contas entram" continua amarelo, porque nenhuma regra o cobre; é uma lacuna para a reunião *purple*. Se algo travar, usar "Reiniciar", no topo, e repetir os passos.
Conclusão: "A fonte ligada não basta: a regra precisa existir, estar ativa e ter sido testada."
[Tela: gravação do laboratório do slide 14, no simulador]

**Slide 15 — De volta ao problema (18:40–19:30)**
Fala: "Voltemos ao Rafael. A lista de 5 mil *hashes* entra, mas não sozinha. A assinatura pega a cópia conhecida, e a YARA v2 pega a variante sem acusar o *briefing*. O comportamento, na regra 100210, vigia a técnica T1490, e o teste mostrou que ela deve olhar o nome original do arquivo. O ajuste com a exceção 100211 corta 240 falsos positivos e mantém os 10 ataques. E, na plataforma, a R3 só alertou depois de ligada e retestada. Respondendo à pergunta da aula: a Rede Tatame combina assinaturas para o conhecido, comportamento para as técnicas e correlação para juntar pistas fracas, e testa e ajusta cada regra medindo precisão e sensibilidade."

**Slides 16 a 18 — Pontos-chave, referências e encerramento (19:30–20:00)**
Fala: "Para levar: assinaturas reconhecem o conhecido; o comportamento mira a técnica; regras e correlação dão contexto; e toda regra é testada e ajustada sem cegar o SOC. Mas e o ataque que nenhuma regra previu? Na próxima aula, vamos caçar ameaças a partir de hipóteses, consultas e análise de anomalias."

[Envato: "security analyst alerts screen", "code on screen dark", "server room blue light". Slides de apoio: tabela do slide 4, código do slide 10 e indicadores do slide 13.]

## Aula 11 — Caça a ameaças: hipóteses, consultas e análise de anomalias

### Texto base

As regras de detecção encontram o que alguém já previu. Um adversário que usa uma ferramenta legítima, instalada com uma conta válida, pode passar semanas sem disparar nenhum alerta. Segundo o relatório M-Trends 2024, da Mandiant, a mediana global de permanência de invasores antes da descoberta (*dwell time*) foi de 10 dias em 2023, e muitos casos ficam bem acima da mediana. A caça a ameaças existe para encurtar esse período: em vez de esperar o alerta, a equipe vai atrás do adversário.

#### Comprometimento presumido e tipos de caça

Caça a ameaças (*threat hunting*) é a busca proativa e iterativa por atividade maliciosa que escapou dos controles automatizados. Ela parte do **comprometimento presumido** (*assume breach*): o caçador supõe que o adversário já está no ambiente e procura evidências disso. A caça não substitui o SOC; ela cobre o que as regras ainda não veem e devolve regras novas para a engenharia de detecção estudada na Aula 10.

Costuma-se distinguir três abordagens, que se combinam na prática:

- **orientada por hipótese**: parte de uma técnica do MITRE ATT&CK que um adversário usaria no ambiente;
- **orientada por indicadores**: procura endereços IP, domínios ou *hashes* citados em um relatório recente;
- **situacional ou por anomalia**: parte dos ativos mais críticos ou do que foge do comportamento normal.

A inteligência de ameaças, estudada na Unidade 1, entra aqui como matéria-prima. Do relatório sobre um grupo como o fictício Cobalto Austral, o caçador aproveita principalmente o comportamento descrito, por exemplo, o uso de ferramentas de acesso remoto (T1219) e a cópia de dados para armazenamento externo (T1567.002). Pela Pirâmide da Dor, proposta por David Bianco em 2013, *hashes* e IPs são trocados pelo adversário em minutos, enquanto o comportamento é caro de mudar.

[Imagem 1 — Ciclo da caça orientada por hipótese: origens (inteligência, ATT&CK, Red Team, anomalias) → hipótese → consulta → investigação → incidente e detecção nova → próxima hipótese. Texto alternativo: "Diagrama circular do ciclo de caça a ameaças, da hipótese à detecção nova". Pode ser recriado pela equipe.]

#### A hipótese testável

Uma boa hipótese é **específica e testável**: diz o que se procura, onde procurar, o que conta como evidência e o que a descartaria. Na Rede Tatame, a hipótese H-11 ficou assim: "um adversário usa uma ferramenta de acesso remoto não aprovada para manter contato periódico com a internet e tirar dados da sede". Onde olhar: processos registrados pelo EDR e pelo Sysmon, conexões registradas pelo Zeek, volume de saída por máquina e a base de mudanças da TI. Evidência: programa raro, conexões em intervalos regulares e saída acima do normal, sem chamado de mudança. Uma hipótese que não pode ser provada nem descartada com os dados disponíveis ainda não está pronta para a caça, mas já revela uma lacuna de coleta.

#### Consultas: empilhar e pivotar

A caça acontece onde os dados estão. No Security Onion, a tela **Hunt** pesquisa alertas, eventos do Sysmon e os registros do Zeek (`conn`, `dns`, `http`) com uma linguagem que combina filtros e agrupamentos, como `event.dataset:conn | groupby destination.ip`. No Wazuh, o painel aceita consultas DQL ou Lucene sobre os eventos dos agentes.

Duas técnicas de consulta sustentam a maior parte das caças. O **empilhamento** (*stacking*) conta em quantas máquinas cada valor aparece e ordena do mais raro para o mais comum: o programa oficial de suporte aparece em quase todas as máquinas, e o que está na cauda longa merece atenção. O **pivô** transforma um achado no filtro da próxima consulta: do programa raro ao endereço que ele contata, do endereço à linha do tempo do servidor.

[Imagem 2 — Captura de tela da tela Hunt do Security Onion com uma consulta agrupada por `process.name` e a contagem de máquinas por programa. Texto alternativo: "Tela Hunt do Security Onion mostrando o empilhamento de processos por número de máquinas". Captura própria em laboratório; o Security Onion é software livre.]

#### *Baseline* e anomalia com estatística simples

O *baseline* é o comportamento normal de uma máquina, conta ou serviço em um período de referência. Com ele, é possível perguntar se o valor de hoje é estranho. A medida mais simples é o ***z-score***, que indica quantos desvios-padrão o valor observado está acima da média: z = (x − média) ÷ desvio-padrão. Um limiar comum é z maior que 3.

A média e o desvio-padrão, porém, são sensíveis a dias atípicos. Se um dia de *backup* entra no período de referência, o desvio cresce e a anomalia real some. Uma alternativa robusta usa a **mediana** e o **MAD** (desvio absoluto mediano): z robusto = 0,6745 × (x − mediana) ÷ MAD.

Para conexões, a pergunta muda: o programa fala com a internet em intervalos regulares demais? Esse padrão, chamado **batimento** (*beaconing*), é típico de ferramentas automáticas. O **coeficiente de variação** dos intervalos, cv = desvio-padrão ÷ média, fica perto de zero quando um programa conecta a cada cinco minutos e perto de um quando uma pessoa navega. Ferramentas abertas, como o RITA, aplicam essa ideia aos registros do Zeek.

[Imagem 3 — Gráfico de barras com 14 dias de volume de saída de um servidor, a faixa de média ± 3 desvios-padrão e o último dia muito acima da faixa. Texto alternativo: "Gráfico de baseline de tráfego de saída com um dia anômalo acima do limiar". Pode ser recriado pela equipe.]

Anomalia não é prova de ataque. Ela indica onde olhar; o contexto decide. Na caça H-11, um notebook da TI também passou do limiar, mas tinha uma mudança aprovada que explicava o tráfego.

#### Exemplo numérico

Um servidor enviou para a internet, em sete dias, 180, 200, 220, 190, 210, 200 e 200 MB. A média é 1.400 ÷ 7 = 200 MB. A soma dos quadrados dos desvios é 400 + 0 + 400 + 100 + 100 + 0 + 0 = 1.000, e o desvio-padrão amostral é √(1.000 ÷ 6) ≈ 12,91 MB. Se hoje saíram 260 MB, z = 60 ÷ 12,91 ≈ 4,65: anomalia pelo limiar 3. Agora inclua no *baseline* um dia de *backup* de 600 MB. A média sobe para 250 MB, o desvio para cerca de 141,9 MB e o z de 260 MB cai para 0,07: a anomalia desaparece. Com mediana 200 e MAD 10, o z robusto vale 0,6745 × 60 ÷ 10 ≈ 4,05, com ou sem o *backup*.

#### Da descoberta à detecção

Toda caça termina com entregas. Se a hipótese se confirma, abre-se um incidente, tema da Unidade 4. Em qualquer caso, a caça devolve detecções novas, consultas documentadas e lacunas de coleta. Na Rede Tatame, a caça H-11 levou a ligar a fonte de saída de rede, ativar as regras de acesso remoto não aprovado e de saída volumosa e propor uma regra de batimento.

[Imagem 4 — Pirâmide da Dor de David Bianco com seis camadas, de *hashes* (base) a TTPs (topo), em cores do verde ao vermelho. Texto alternativo: "Pirâmide da Dor com os tipos de indicador e o custo crescente para o adversário". Recriar a partir do texto original de Bianco (2013).]

#### Pausa para reflexão

> Uma caçadora testou durante uma semana a hipótese "contas válidas estão entrando na VPN de madrugada, fora do horário dos donos" (T1078). Ela consultou 30 dias de autenticação e não achou nenhum caso suspeito, e o gestor concluiu que a semana foi perdida.
>
> 1. A hipótese era específica e testável? Que dados a provariam ou a descartariam?
> 2. O que a caçadora pode entregar mesmo sem ter achado um invasor?
> 3. Que *baseline* e que limiar você usaria para transformar essa caça em uma regra?
>
> **Desafio prático:** escreva a hipótese no formato da H-11 (hipótese, onde olhar, evidência, o que a descarta) e uma consulta que a teste.

#### Pontos-chave

- A caça parte do comprometimento presumido e de uma hipótese específica e testável.
- Consultas empilham dados para achar o raro e pivotam de um achado ao próximo.
- *Baseline*, *z-score*, mediana/MAD e coeficiente de variação revelam muitas anomalias.
- Anomalia indica onde olhar; o contexto diz se é ataque.
- O melhor resultado de uma caça é uma detecção nova.

### Referências da aula

BEJTLICH, Richard. *The practice of network security monitoring*: understanding incident detection and response. San Francisco: No Starch Press, 2013.

BIANCO, David J. The pyramid of pain. *Enterprise Detection & Response*, mar. 2013. Disponível em: <https://detect-respond.blogspot.com/2013/03/the-pyramid-of-pain.html>. Acesso em: 22 nov. 2026.

MANDIANT. *M-Trends 2024*: special report. [*S. l.*]: Google Cloud, 2024.

MITRE. *T1219*: remote access tools. MITRE ATT&CK. Disponível em: <https://attack.mitre.org/techniques/T1219/>. Acesso em: 22 nov. 2026.

SANDERS, Chris; SMITH, Jason. *Applied network security monitoring*: collection, detection, and analysis. Waltham: Syngress, 2013.

SECURITY ONION SOLUTIONS. *Security Onion documentation*. Disponível em: <https://docs.securityonion.net/>. Acesso em: 22 nov. 2026.

### Roteiro da Videoaula 11 — "O servidor que liga para fora a cada cinco minutos"

Duração-alvo: 15 a 20 minutos. Deck: unidade_3/slides/aula11.html (22 slides).

**Slides 1 e 2 — Capa e sumário (0:00–0:30)**
Fala: "Olá! Até aqui, a defesa esperou o alerta. Hoje vamos inverter a postura: com a caça a ameaças, saímos procurando o invasor antes de qualquer alarme. O sumário mostra o caminho: hipótese, consultas, estatística simples e, no fim, regras novas."

**Slide 3 — O problema de hoje na Rede Tatame (0:30–1:45)**
Fala: "Terça-feira, 17 de novembro. A Luiza Ferraz, analista nível 2 do SOC, recebe um relatório do setor: o Grupo Cobalto Austral instala ferramentas legítimas de acesso remoto e, dias depois, copia dados para armazenamento externo. Na Rede Tatame, as regras que veriam isso, a R8 e a R9, estão desligadas, e a saída de rede nem é coletada. Nenhum alerta tocou. No mapa à direita, o SRV-ERP-01 está em vermelho, e o caminho em destaque vai dele para a internet. A pergunta da aula está no quadro amarelo: como encontrar um invasor que já está dentro e que nenhuma regra apontou?"
[Take de apoio: analista diante de gráficos em tela escura, à noite — Envato]

**Slide 4 — Caça a ameaças: procurar antes do alerta (1:45–2:40)**
Fala: "Caça a ameaças é a busca proativa e iterativa por atividade que escapou dos controles automáticos. Ela parte do comprometimento presumido: o caçador supõe que o adversário já entrou. Há três abordagens. A orientada por hipótese parte de uma técnica do ATT&CK; a orientada por indicadores procura IPs, domínios e *hashes* de um relatório; e a situacional parte do que é crítico ou do que foge do normal. A caça não substitui o SOC: ela cobre o que as regras ainda não veem e devolve regras novas."

**Slide 5 — Uma boa hipótese é específica e testável (2:40–3:35)**
Fala: "Do relatório, a Luiza aproveita o comportamento: as técnicas T1219, ferramentas de acesso remoto, e T1567.002, cópia para armazenamento na nuvem. Vejam o cartão da H-11. A hipótese diz o que se procura; 'Onde olhar' lista os dados, processos do EDR e do Sysmon, conexões do Zeek, volume de saída e base de mudanças; 'Evidência' diz o que confirma; e 'Descarta se' diz o que derruba a hipótese. Se não dá para provar nem descartar com dados, a hipótese ainda não está pronta."

**Slide 6 — Laboratório: o ciclo da caça orientada por hipótese (3:35–4:50)**
Objetivo: mostrar o caminho completo da caça H-11, da origem da hipótese às regras novas.
Na tela:
1. Ao abrir o slide, o passo "1 · Origens" já está na tela (contador 1 / 6), com as quatro fontes da esquerda acesas.
2. Clicar em "▶ Avançar" para "2 · Hipótese H-11" e "3 · Consultar".
3. Avançar para "4 · Investigar" e "5 · Incidente", em que o nó Incidente fica vermelho.
4. Avançar para "6 · Detecção nova", com as linhas verdes voltando para a hipótese.
Fala: "As hipóteses nascem de quatro origens: inteligência de ameaças, técnicas do ATT&CK sem cobertura, achados do Red Team e anomalias. Hoje, o relatório e a T1219 com a R8 desligada. Os pontos que correm nas linhas mostram o caminho de cada etapa. Na consulta, a Luiza empilha 30 dias de processos das 149 máquinas e analisa as conexões em Python. Na investigação, o contexto separa o legítimo: as máquinas da TI têm a mudança MUD-5521. No SRV-ERP-01, o ConectaJá foi instalado como serviço às 02:22 de 13/11 e bate a cada 300 segundos em 198.51.100.77. O passo 5 abre o incidente, porque 2,8 GB saíram em 16/11, e o passo 6 devolve ao SOC a fonte ligada, a R8, a R9 e uma regra de batimento."
Atenção: prefira os cliques manuais; o botão "⏯ Auto" avança sozinho, e o "◀" volta um passo.
Conclusão: "Toda caça devolve alguma coisa à detecção, mesmo quando não acha nada."
[Tela: gravação do laboratório do slide 6]

**Slide 7 — Consultas no Security Onion e no Wazuh (4:50–5:40)**
Fala: "A caça acontece onde os dados estão. No Security Onion, a tela Hunt pesquisa alertas, Sysmon e os registros do Zeek com filtros e agrupamentos, como 'event.dataset:conn', barra vertical, 'groupby destination.ip'. No Wazuh, o painel aceita DQL ou Lucene. Duas técnicas sustentam a maior parte das caças: o empilhamento, que conta em quantas máquinas cada valor aparece e mostra a cauda longa, e o pivô, que transforma um achado no filtro da próxima consulta."

**Slide 8 — Laboratório: empilhar, pivotar e montar a linha do tempo (5:40–7:50)**
Objetivo: testar a H-11 com consultas, das 149 máquinas da sede até um único servidor.
Na tela (console "Security Onion · Hunt"; a busca 1 roda sozinha ao abrir o slide):
1. Ler o resultado de "1. Empilhar acesso remoto".
2. Clicar em "2. Para onde se conectam? (Zeek)".
3. Clicar em "3. Linha do tempo no SRV-ERP-01".
4. Clicar em "4. Saída diária do ERP (baseline)".
5. Clicar em "5. Máquinas da TI: há mudança aprovada?", no grupo Contexto.
Fala: "A busca 1 filtra processos de acesso remoto e agrupa por programa e máquina. O suporte_ti.exe, oficial, está em 145 máquinas, 97,3%; o remotodesk.exe em 3; e o conectaja.exe em uma só, 0,7%. Na busca 2, pivotamos para a rede, com os registros de conexão do Zeek. As máquinas da TI falam com relay.remotodesk.example.com poucas vezes. O SRV-ERP-01 fala direto com 198.51.100.77, sem consulta DNS, 1.152 vezes em quatro dias: 288 por dia, uma a cada cinco minutos. As barras destacadas no fim do histograma são esses dias. A busca 3 monta a linha do tempo do servidor entre 02:10 e 02:30 de 13/11: o *logon* remoto da carla.dias às 02:17:12, o PowerShell, o arquivo ConectaJa.exe, o serviço 'ConectaJa Update' com início automático e a primeira conexão às 02:22:33. A última coluna traz as técnicas do ATT&CK. A busca 4 soma os bytes de saída por dia: em torno de 200 MB até o dia 15 e 3.010 MB no dia 16, cerca de 2,8 GB acima. A busca 5 cruza as máquinas da TI com a base de mudanças: todas têm a MUD-5521 aprovada, pedida pelo Caio Mendes."
Atenção: o texto da consulta é digitado aos poucos antes do resultado; espere a tabela completar e a nota aparecer. A sintaxe imita a do Hunt; os dados são da Rede Tatame, fictícios.
Conclusão: "O raro só vira suspeito quando o contexto não o explica. No SRV-ERP-01, nada o explica."
[Tela: gravação do laboratório do slide 8]

**Slide 9 — *Baseline*, anomalia e batimento com estatística simples (7:50–8:50)**
Fala: "O *baseline* é o comportamento normal num período de referência. O *z-score* diz quantos desvios-padrão o valor de hoje está acima da média, e o limiar usual é 3. Mediana e MAD, o desvio absoluto mediano, fazem o mesmo de forma robusta. Para conexões, medimos o batimento: o coeficiente de variação dos intervalos, desvio dividido pela média, perto de zero sugere um programa; perto de um, uma pessoa. E lembrem: a anomalia diz onde olhar, e o contexto diz o que ela é."

**Slide 10 — Antes do código: onde achar e como instalar (8:50–9:20)**
Fala: "O laboratório usa o VS Code, a extensão Python da Microsoft, o Python 3.12 e o pandas 3.1.1, todos das fontes oficiais da tabela. No PyPI, confiram o nome pandas letra por letra e o *link* para o repositório pandas-dev no GitHub. A versão fica fixa no requirements.txt, para a caça dar o mesmo resultado em qualquer máquina."

**Slide 11 — Laboratório: a caça em Python, batimento e *baseline* (9:20–12:00)**
Objetivo: provar com números o que as consultas sugeriram: conexões regulares demais e saída fora do normal.
Na tela (VS Code em tela cheia, pasta caca-h11; o roteiro do laboratório abre com a tecla G ou com o botão "☰ Roteiro" da barra de status e fica fechado durante a gravação):
1. Clicar em "⬇ Preparar o ambiente" e esperar o botão mudar para "✓ Ambiente pronto".
2. Abrir dados/conexoes_saida.csv no explorador e voltar a beacon.py, mostrando as linhas destacadas 4, 5, 9, 12 e 13.
3. Clicar em "▶ Procurar batimento".
4. Abrir baseline.py (linhas destacadas 4, 7, 10, 11 e 19) e dados/saida_diaria_mb.csv.
5. Clicar em "▶ Comparar com o baseline".
Fala: "Primeiro, o ambiente. O Python é o 3.12.10; criamos e ativamos o .venv, e o *prompt* ganha o .venv entre parênteses. O pip install lê o requirements.txt, baixa o pandas 3.1.1 e as dependências, numpy, python-dateutil e tzdata, e o pip list confirma as versões. O CSV de conexões cobre uma hora da noite de domingo, 15/11, exportada do Security Onion. No beacon.py, as linhas 4 e 5 definem as regras do jogo: pelo menos 10 conexões e coeficiente de variação de até 0,10. A linha 9 calcula, para cada par de máquina e destino, o intervalo em segundos desde a conexão anterior. A linha 11 resume cada par, a 12 calcula o cv e a 13 decide. Na saída, o SRV-ERP-01 tem 14 conexões, intervalo médio de 300,3 segundos, desvio de 2,5 e cv de 0,008, em vermelho. O NB-TI-003 tem cv de 0,761, e o NB-ATD-012, de 0,931: são pessoas usando o computador. Agora o baseline.py. A linha 7 separa os 14 dias de referência do dia 16/11; as linhas 10 e 11 calculam o desvio amostral e o z; a 19 aplica o limiar 3. O SRV-ERP-01 tem média de 200,1 MB, desvio de 9,2 e 3.010 MB no dia 16: z de 306,3, cerca de 2.810 MB acima da média. O NB-TI-003 também passa, com z de 8,6, em amarelo. O SRV-ARQ-01 fica em 1,2."
Atenção: a preparação do ambiente é simulada e leva alguns segundos; a saída mostrada é a que os *scripts* produzem ao rodar de verdade com esses CSV. O pandas imprime números com ponto decimal.
Conclusão: "A estatística aponta duas máquinas. O contexto da busca 5 explica o NB-TI-003; o SRV-ERP-01 continua sem explicação, e é ali que está o invasor."
[Tela: gravação do laboratório do slide 11]

**Slide 12 — O *z-score* feito à mão (12:00–12:50)**
Fala: "Vamos fazer a conta com números redondos. Sete dias de saída: 180, 200, 220, 190, 210, 200 e 200 MB. A média é 200. A soma dos quadrados dos desvios dá 1.000; dividindo por 6 e tirando a raiz, o desvio é 12,91. Se hoje saíram 260 MB, z é 60 dividido por 12,91, cerca de 4,65: anomalia. Mas, se um dia de *backup* de 600 MB entrar no *baseline*, a média vai a 250, o desvio a 141,9 e o z cai para 0,07. Com mediana 200 e MAD 10, o z robusto fica em 4,05, com ou sem o *backup*."

**Slide 13 — Laboratório: quando o *baseline* engana (12:50–14:00)**
Objetivo: ver o limiar de 3 desvios em ação e o efeito de um dia atípico no *baseline*.
Na tela:
1. Ler os valores iniciais: saída de hoje 260 MB, limiar 3,0, média e desvio "200,0 ± 12,91 MB", z de 4,65 e z robusto de 4,05, ambos "anomalia".
2. Marcar "Incluir o dia de backup (600 MB) no baseline".
3. Desmarcar e arrastar "Saída de hoje (MB)" até 230.
Fala: "As barras cinzentas são os sete dias, a linha tracejada é a média e a faixa azul vai de três desvios abaixo a três acima. A barra de hoje fica vermelha quando passa do limiar. Ao incluir o *backup*, aparece uma barra amarela, a média vira 250, o desvio 141,93, e o z de 260 MB cai para 0,07, 'normal': a faixa engoliu a anomalia. O z robusto continua em 4,05. Sem o *backup* e com 230 MB, o z é 2,32 e o robusto 2,02: abaixo do limiar, a barra fica verde."
Atenção: o controle do limiar também muda a faixa; com limiar 2, os 230 MB passam a ser anomalia.
Conclusão: "*Baseline* limpo e medida robusta evitam que o ruído esconda a anomalia."
[Tela: gravação do laboratório do slide 13]

**Slide 14 — Laboratório: 149 máquinas, três medidas (14:00–14:55)**
Objetivo: enxergar a anomalia em várias dimensões ao mesmo tempo.
Na tela:
1. Deixar a cena girar alguns segundos e depois arrastar para girar.
2. Clicar nos botões "Normais", "NB-TI-003" e "SRV-ERP-01", um por vez.
Fala: "Cada esfera é uma máquina da sede. Os três eixos são o z da saída, a quantidade de destinos novos e a regularidade das conexões, que é um menos o cv. A nuvem azul são 147 máquinas normais. Ao clicar em NB-TI-003, o quadro explica: z de 8,6, mas conexões irregulares e destino conhecido, coberto pela MUD-5521. Ao clicar em SRV-ERP-01, a esfera vermelha pulsa: z de 306,3, destino novo sem DNS e batimento com cv de 0,008, longe da nuvem nos três eixos."
Atenção: a cena precisa de internet para carregar o three.js; as posições das esferas são ilustrativas.
Conclusão: "Quanto mais medidas concordam, mais forte é o indício."
[Tela: gravação do laboratório do slide 14]

**Slide 15 — Laboratório: a caça H-11 na plataforma, antes e depois das regras (14:55–16:45)**
Objetivo: ver por que a caça foi necessária: o dado existia, faltavam a fonte e as regras.
Na tela (simulador na aba Cenários, reiniciado com as fontes e regras padrão):
1. No cartão "Acesso remoto não aprovado e saída de dados", clicar em "Iniciar cenário" e esperar os três passos, cerca de 30 segundos.
2. Na aba Telemetria, ligar "Acesso a buckets e saída de rede".
3. Na aba Regras do CEP, ligar "R8 · Ferramenta de acesso remoto não aprovada" e "R9 · Saída volumosa para destino novo".
4. Voltar a Cenários e clicar em "Repetir com as fontes e regras atuais".
5. Opcional: na aba SOC, clicar em "Investigar" no alerta da R8 e depois em "Conter".
Fala: "Na primeira rodada, a instalação do ConectaJá no SRV-ERP-01 e as conexões periódicas para 198.51.100.77 ficam amarelas, 'visto nos logs, sem alerta': o EDR e o DNS registraram, mas nenhuma regra olhava. O envio de 2,8 GB fica vermelho, 'não detectado', porque a fonte de saída de rede está desligada. É exatamente o ponto cego que a caça cobriu. Ligamos a fonte, a R8 e a R9 e repetimos. Agora o primeiro e o terceiro passos viram 'detectado'. O segundo, o batimento, continua amarelo: não há regra para ele, e é essa a regra nova que a caça propõe. Se eu conter o alerta da R8 a tempo, o envio aparece como 'interrompido pela contenção'."
Atenção: na velocidade padrão, "1 s = 15 s", o envio acontece cerca de 27 segundos após o início; para dar tempo de conter, troque a velocidade, no topo, para "1 s = 5 s". Se algo travar, use "Reiniciar", no topo.
Conclusão: "A caça cobre o ponto cego e diz qual regra falta."
[Tela: gravação do laboratório do slide 15, no simulador]

**Slide 16 — O que a caça H-11 devolve ao SOC (16:45–17:30)**
Fala: "A tabela mostra o destino de cada achado. O *hash* do ConectaJa.exe e o IP 198.51.100.77 viram bloqueios, úteis mas frágeis, porque ficam na base da Pirâmide da Dor, de David Bianco: o adversário os troca em minutos. Os comportamentos, acesso remoto fora da lista, batimento regular e saída acima do *baseline*, viram regras: a R8 e a R9 ligadas e uma regra de batimento proposta ao Rafael Tavares. O melhor produto de uma caça é a detecção que nasce dela."

**Slides 17 e 18 — Pausa para reflexão e um caminho para responder (17:30–18:20)**
Fala: "Pause o vídeo. Uma caçadora testou por uma semana a hipótese de contas válidas entrando na VPN de madrugada e não achou nada. O gestor diz que a semana foi perdida. Foi? [pausa] A hipótese era testável, desde que a VPN registre conta, horário e origem. Mesmo sem achar invasor, ela entrega o *baseline* de horário de cada conta, as lacunas de dados encontradas e a consulta documentada. E a caça pode virar regra: alertar quando o horário fugir mais de 3 MAD da mediana da conta ou quando a origem for nova e não houver MFA. A semana não foi perdida."

**Slide 19 — De volta ao problema (18:20–19:10)**
Fala: "Voltemos à Luiza. Os quatro cartões resumem a caça: a hipótese H-11, tirada do comportamento do Cobalto Austral; as consultas, que acharam o conectaja.exe em uma das 149 máquinas e a linha do tempo de 13/11; a estatística, com batimento a cada 300 segundos e 3.010 MB de saída, enquanto o NB-TI-003 tinha mudança aprovada; e a detecção nova. Respondendo à pergunta da aula: com uma hipótese testável, consultas que empilham e pivotam a telemetria e um *baseline* com estatística simples, a caçadora encontra o invasor que as regras não viram, separa o legítimo pelo contexto e transforma o achado em incidente e em detecções novas."

**Slides 20 a 22 — Pontos-chave, referências e encerramento (19:10–19:45)**
Fala: "Para levar desta aula: a caça parte do comprometimento presumido e de uma hipótese testável; consultas empilham e pivotam; a estatística simples revela anomalias, e o contexto decide. Achamos a porta escondida no ERP. Na próxima aula, vamos fechar as portas antes que alguém as use: *hardening* de sistemas e redução da superfície de ataque."

[Envato: "analyst night monitors", "network traffic visualization", "data scatter plot". Slides de apoio: cartão da hipótese (slide 5), tabela do slide 16 e cartões do slide 19.]

## Aula 12 — *Hardening* de sistemas e redução da superfície de ataque

### Texto base

Nas Aulas 9, 10 e 11, construímos a capacidade de enxergar o adversário: coletar registros, escrever regras e caçar o que as regras não viram. No exercício de emulação do Grupo Cobalto Austral na Rede Tatame, as regras dispararam, e o adversário chegou ao ERP mesmo assim, entrando pela VPN com uma senha vazada e sem MFA. Nesta aula, olhamos para o outro lado da defesa: diminuir os caminhos disponíveis antes que alguém os use.

#### Superfície de ataque e *hardening*

A **superfície de ataque** é a soma dos pontos por onde um adversário pode tentar entrar ou agir: portas abertas, serviços em execução, contas e privilégios, *software* instalado e sistemas expostos à internet. ***Hardening*** (endurecimento) é o conjunto de ações que configura cada sistema de forma segura e **remove o que não é necessário**: o serviço que ninguém usa, o protocolo antigo, a conta esquecida, o privilégio a mais.

O primeiro passo é o inventário. Não se endurece o que ninguém sabe que existe: o servidor de homologação `hml-gestao`, encontrado no reconhecimento da Unidade 2 fora do inventário e sem WAF, é o exemplo clássico. Por isso os CIS Controls começam por inventário de ativos (Controle 1) e de *software* (Controle 2), e o NIST CSF 2.0 coloca a gestão de ativos (ID.AM) na função Identificar, antes de Proteger.

[Imagem 1 — Diagrama com dois círculos lado a lado: à esquerda, um servidor com muitas "portas" abertas (FTP, NetBIOS, SMBv1, RDP aberto para toda a rede, seis administradores); à direita, o mesmo servidor depois do *hardening*, com três portas e dois administradores. Texto alternativo: "Comparação de um servidor antes e depois do hardening, com menos portas, serviços e contas". Pode ser recriado pela equipe a partir da descrição.]

#### CIS Benchmarks e CIS Controls v8

Duas referências do *Center for Internet Security* (CIS) orientam o trabalho. Os **CIS Benchmarks** são guias de configuração segura por tecnologia (Windows Server, distribuições Linux, bancos de dados, provedores de nuvem, navegadores). Cada recomendação traz o valor esperado, a justificativa e o modo de auditar. As recomendações são agrupadas em perfis: o **Nível 1** reúne o essencial, com pouco impacto no uso do sistema; o **Nível 2** acrescenta medidas de defesa em profundidade para ambientes mais sensíveis, que podem limitar funcionalidades. A conformidade pode ser medida pela ferramenta CIS-CAT ou por *scripts* que comparam a configuração exportada de cada máquina com o *baseline*.

O ***baseline*** é a configuração mínima aprovada para um tipo de sistema. Todo desvio vira correção ou **exceção documentada**, com justificativa, aprovador e prazo.

Os **CIS Controls v8** (atualizados para a versão 8.1 em 2024) olham para o programa inteiro: 18 controles e 153 salvaguardas, organizados em três grupos de implementação. O **IG1**, com 56 salvaguardas, é a "higiene cibernética essencial" que toda organização deveria cumprir; o IG2 e o IG3 acrescentam salvaguardas para ambientes maiores e mais visados. Várias salvaguardas são *hardening* puro: 4.1 (processo de configuração segura), 4.4 (*firewall* nos servidores), 4.7 (contas padrão), 4.8 (desabilitar serviços desnecessários) e 7.3 (atualização automatizada do sistema operacional).

[Imagem 2 — Infográfico com os 18 CIS Controls em três faixas coloridas, indicando quais salvaguardas pertencem ao IG1, IG2 e IG3. Texto alternativo: "Os 18 controles do CIS Controls v8 organizados nos grupos de implementação IG1, IG2 e IG3". Pode ser recriado pela equipe a partir do documento público do CIS.]

#### Portas, serviços e protocolos

No servidor, reduzir a superfície significa desligar o que não tem função: FTP instalado para uma migração antiga, *spooler* de impressão em servidor que não imprime, NetBIOS sobre TCP/IP, SMBv1 (o protocolo explorado pelo WannaCry em 2017). O que precisa continuar ligado é restringido: o RDP, por exemplo, passa a aceitar conexões apenas da sub-rede da equipe de TI e exige autenticação no nível da rede (NLA).

#### Contas, privilégios e MFA

O **princípio do menor privilégio** determina que cada pessoa, serviço e programa receba apenas o acesso necessário à sua função, pelo tempo necessário. Na prática: contas administrativas separadas das contas de uso diário (salvaguarda 5.4), senha única e aleatória para o administrador local de cada máquina, gerida pelo LAPS (5.2), contas de serviço sem *logon* interativo, desativação de contas inativas há 45 dias (5.3) e **MFA** nas aplicações expostas, no acesso remoto e em todo acesso administrativo (6.3, 6.4 e 6.5). O menor privilégio ataca diretamente a movimentação lateral vista na Unidade 2: uma senha descoberta abre menos portas.

#### *Patching* com prioridade

O NIST SP 800-40 Rev. 4 trata o *patching* como manutenção preventiva: um processo contínuo, com inventário, priorização, janela de mudança e verificação. Como nem tudo pode ser corrigido ao mesmo tempo, a prioridade combina o **CVSS** (gravidade técnica), o **EPSS** (probabilidade estimada de exploração em 30 dias) e o catálogo **KEV** da CISA (falhas já exploradas), como vimos na Unidade 2, além da criticidade e da exposição do ativo. Quando a correção não pode entrar logo, uma mitigação temporária, como uma regra no WAF ou o desligamento do serviço, reduz a exposição até o *patch*.

[Imagem 3 — Gráfico de barras com a quantidade média de falhas críticas abertas para prazos de correção de 45, 14 e 7 dias. Texto alternativo: "Gráfico mostrando que, quanto menor o prazo de correção, menos falhas ficam abertas ao mesmo tempo". Pode ser recriado pela equipe com os números do exemplo numérico.]

#### Exemplo numérico

Na auditoria dos dois servidores-membro da sede contra um *baseline* de 10 itens inspirado no CIS Benchmark, o SRV-ARQ-01 e o SRV-ERP-01 cumpriam 3 itens cada: 6 de 20, ou **30%** de conformidade. Depois do *hardening*, o SRV-ARQ-01 passou a 10 de 10 e o SRV-ERP-01 a 9 de 10, com uma exceção aprovada para o *spooler* de impressão: 19 de 20, ou **95%**. No SRV-ARQ-01, as portas escutando caíram de 5 para 3 (redução de 40%) e os administradores locais, de 6 para 2 (redução de 67%).

O prazo de correção também se mede. Se surgem 12 falhas críticas novas por mês (0,4 por dia) e cada uma leva 45 dias para ser corrigida, ficam abertas, em média, 0,4 × 45 = **18 falhas ao mesmo tempo**. Com prazo de 14 dias, a média cai para 0,4 × 14 = **5,6**, uma redução de 1 − 14/45 ≈ **69%** na exposição.

#### Defesa em profundidade e NIST CSF 2.0

O *hardening* não substitui a detecção; ele a complementa dentro da **defesa em profundidade**, que organiza a proteção em camadas (pessoas, perímetro, rede, *endpoint*, aplicação e dados) porque qualquer controle pode falhar. No NIST *Cybersecurity Framework* 2.0, publicado em 2024 com seis funções (Governar, Identificar, Proteger, Detectar, Responder e Recuperar), o *hardening* está sobretudo em Proteger, nas categorias de identidade e acesso (PR.AA) e de segurança das plataformas (PR.PS). Na emulação do Cobalto Austral, seis dos sete passos tinham um controle preventivo possível; a descoberta no AD só se resolve com detecção. Por isso a Unidade 3 junta as duas coisas.

[Imagem 4 — Ilustração de anéis concêntricos (pessoas, perímetro, rede, *endpoint*, aplicação, dados) em volta de um banco de dados, com setas de ataque sendo barradas em camadas diferentes. Texto alternativo: "Modelo de defesa em profundidade com seis camadas de proteção em volta dos dados". Pode ser recriado pela equipe a partir da descrição.]

#### O que você verá na próxima unidade

Monitoramos, detectamos, caçamos e fechamos caminhos, mas algum ataque ainda vai passar. A **Unidade 4 — Resposta a Incidentes e Purple Team** começa quando o alerta vira incidente: o ciclo de resposta, da preparação à recuperação (Aula 13); a coleta de evidências e a linha do tempo do incidente (Aula 14); os exercícios *purple team* que validam as detecções contra técnicas emuladas (Aula 15); e o relatório final, com achados, riscos, recomendações e métricas de melhoria (Aula 16).

#### Pontos-chave

- *Hardening* é configurar com segurança e remover o desnecessário, e começa pelo inventário.
- CIS Benchmarks dizem como configurar cada tecnologia (Níveis 1 e 2); CIS Controls v8 organizam o programa em 18 controles e nos grupos IG1, IG2 e IG3.
- Menor privilégio, contas administrativas separadas, LAPS e MFA reduzem a movimentação lateral.
- *Patching* prioriza KEV, EPSS e criticidade, e o prazo de correção define a exposição média.
- O *hardening* fica em Proteger, no NIST CSF 2.0, e se soma à detecção em camadas.

### Referências da aula

CENTER FOR INTERNET SECURITY. *CIS Benchmarks*. East Greenbush: CIS, [2026]. Disponível em: <https://www.cisecurity.org/cis-benchmarks>. Acesso em: 22 nov. 2026.

CENTER FOR INTERNET SECURITY. *CIS Critical Security Controls*: version 8.1. East Greenbush: CIS, 2024. Disponível em: <https://www.cisecurity.org/controls/v8-1>. Acesso em: 22 nov. 2026.

NAKAMURA, Emilio Tissato; GEUS, Paulo Lício de. *Segurança de redes em ambientes cooperativos*. São Paulo: Novatec, 2007.

NATIONAL INSTITUTE OF STANDARDS AND TECHNOLOGY. *The NIST Cybersecurity Framework (CSF) 2.0*. Gaithersburg: NIST, 2024. (NIST CSWP 29). DOI: 10.6028/NIST.CSWP.29.

SOUPPAYA, Murugiah; SCARFONE, Karen. *SP 800-40 Rev. 4*: guide to enterprise patch management planning: preventive maintenance for technology. Gaithersburg: NIST, 2022. DOI: 10.6028/NIST.SP.800-40r4.

### Roteiro da Videoaula 12 — "Se o SOC viu tudo, por que o invasor chegou ao ERP?"

Duração-alvo: 15 a 20 minutos. Deck: unidade_3/slides/aula12.html (20 slides).

**Slides 1 e 2 — Capa e sumário (0:00–0:35)**
Fala: "Olá! Esta é a última aula da Unidade 3. Até aqui, aprendemos a enxergar o adversário: registros, regras e caça. Hoje vamos fazer o caminho inverso e diminuir os lugares por onde ele pode passar. O sumário mostra o percurso: superfície de ataque, CIS Benchmarks e CIS Controls, menor privilégio, *patching* e defesa em profundidade, com cinco laboratórios."

**Slide 3 — O problema de hoje na Rede Tatame (0:35–1:45)**
Fala: "Na emulação do Grupo Cobalto Austral, o SOC da Rede Tatame viu o *login* sem MFA na VPN, a consulta em massa ao AD e o RDP para o servidor de arquivos. As regras funcionaram, e mesmo assim o adversário chegou ao ERP. Na reunião *purple*, a CISO, Marina Prado, pergunta quantos desses passos nem deveriam ter sido possíveis. O Caio Mendes, administrador da sede, abre o inventário e encontra SMBv1 ligado, seis administradores locais no SRV-ARQ-01 e *patches* com 74 dias de atraso. No mapa, o caminho vermelho vai da internet à VPN, ao AD, ao SRV-ARQ-01 e ao ERP, e o `hml-gestao` aparece destacado porque está fora do inventário. A pergunta da aula está no quadro amarelo: que portas, serviços e contas precisamos fechar, e em que ordem, para que o próximo ataque encontre menos caminhos?"
[Take de apoio: administrador de sistemas diante de um *rack* de servidores, revisando uma lista — Envato]

**Slide 4 — Superfície de ataque e *hardening* (1:45–2:25)**
Fala: "Superfície de ataque é a soma dos pontos por onde alguém pode tentar entrar: portas, serviços, contas, *software* e sistemas expostos. *Hardening* é configurar cada sistema com segurança e remover o que não é necessário. Detecção avisa quando algo acontece; *hardening* impede que muitos passos aconteçam e ainda tira ruído da fila do SOC. E tudo começa pelo inventário: o `hml-gestao` não podia ser endurecido porque ninguém sabia que ele existia."

**Slide 5 — Laboratório: o caminho do Cobalto Austral e os controles que faltaram (2:25–4:15)**
Objetivo: ligar cada passo do adversário ao controle preventivo que o fecharia, respondendo ao "o que fechar" da pergunta.
Na tela:
1. Ao abrir o slide, o passo 1 já está na tela (contador 1 / 8): "Passo 1 · T1078 Contas válidas", com a VPN em vermelho e o nó verde "MFA na VPN" aceso.
2. Clicar em "▶ Avançar" até "Passo 2 · T1087.002 Descoberta no AD": o nó amarelo "Regra R13" acende.
3. Avançar por "Passo 3" (RDP só da TI), "Passo 4" (LSA protegida), "Passo 5" (Conta de serviço) e "Passo 6" (Saída restrita), um clique por vez.
4. Avançar até "Passo 7 · T1490 e T1486 Impacto" (Backup offline) e, por fim, "Resultado · Hardening e detecção juntos" (8 / 8).
Fala: "A linha de cima é o caminho do adversário, com o ID do ATT&CK de cada passo; embaixo, em verde, o controle que fecharia aquele passo. No passo 1, a senha vazada do caio.mendes basta porque a VPN não exige MFA. A regra R11 detecta, mas o acesso acontece; o controle preventivo é MFA no acesso remoto, a salvaguarda 6.4 do CIS. O passo 2 é diferente: qualquer conta do domínio consegue ler o AD, então aqui o nó é amarelo, e quem resolve é a detecção, a regra R13. No passo 3, o *firewall* do servidor só aceita RDP da sub-rede da TI. No passo 4, a proteção da LSA e a retirada de contas comuns do grupo de administradores dificultam a leitura de credenciais. No passo 5, a conta de serviço deixa de aceitar *logon* interativo. No 6, os servidores só falam com destinos de uma lista permitida. No 7, o *backup* *offline* garante a recuperação. O último quadro resume: seis dos sete passos tinham um controle preventivo."
Atenção: os controles são exemplos de *hardening* ligados aos passos do cenário `ransomware` do simulador; prefira os cliques manuais ao botão "⏯ Auto", para dar tempo de ler cada quadro. O botão "◀" volta um passo.
Conclusão: "*Hardening* e detecção se completam: o que não dá para fechar, a gente vigia."
[Tela: gravação do laboratório do slide 5]

**Slide 6 — CIS Benchmarks e CIS Controls v8 (4:15–5:15)**
Fala: "Duas referências do *Center for Internet Security* guiam esse trabalho. Os CIS Benchmarks são guias de configuração por tecnologia: para o Windows Server, cada recomendação diz o valor esperado e como auditar, e elas vêm em dois perfis. O Nível 1 é o essencial, com pouco impacto no uso; o Nível 2 acrescenta defesa em profundidade para ambientes mais sensíveis. Os CIS Controls v8, atualizados para a 8.1 em 2024, olham para o programa inteiro: 18 controles e 153 salvaguardas, em três grupos de implementação. O IG1, com 56 salvaguardas, é a higiene básica. E o quadro azul traz a palavra-chave da aula: *baseline*, a configuração mínima aprovada. Todo desvio vira correção ou exceção documentada, com dono e prazo."

**Slide 7 — Antes do código: onde achar e como instalar (5:15–5:45)**
Fala: "O próximo laboratório usa o VS Code com a extensão Python da Microsoft, o Python 3.12 e um único pacote de terceiros, o PyYAML, que lê o arquivo do *baseline*. Conferimos o nome no PyPI letra por letra, porque pacote com nome parecido é golpe conhecido, e instalamos num ambiente virtual. Os CIS Benchmarks originais estão no *site* do CIS, em PDF gratuito para uso não comercial, depois de um cadastro."

**Slide 8 — Laboratório: auditoria dos servidores contra o *baseline* (5:45–8:30)**
Objetivo: medir quanto os servidores-membro da sede se afastam do *baseline*, respondendo ao "em que ordem" com números.
Na tela (VS Code em tela cheia, pasta hardening-sede; o roteiro do laboratório abre com a tecla G ou com o botão "☰ Roteiro" e fica fechado durante a gravação):
1. Esperar o `auditoria.py` terminar de ser digitado na abertura do slide.
2. Clicar em "⬇ Preparar o ambiente" e esperar o botão mudar para "✓ Ambiente pronto".
3. No explorador, abrir `baseline_servidor.yaml` e mostrar as linhas destacadas (6, 12 a 15).
4. Abrir `export/antes/SRV-ARQ-01.json`.
5. Clicar em "▶ Auditar antes do hardening".
6. Clicar em "▶ Auditar depois do hardening".
Fala: "Primeiro, a preparação. O `python3 --version` confirma o Python 3.12.7; o `venv` cria a pasta `.venv` com um Python isolado; o `activate` liga esse ambiente, e o *prompt* ganha `.venv` entre parênteses; o `pip install` baixa o PyYAML 6.0.4, e o `pip list` confirma que só ele e o pip estão instalados. Agora o *baseline*. São 10 itens inspirados no perfil Nível 1 do CIS Benchmark para servidor-membro, cada um com a chave que vamos procurar no servidor, o valor esperado ou o limite, e a salvaguarda do CIS Controls que ele atende. Na linha 6, SMBv1 desabilitado; na 12, no máximo dois administradores locais; na 15, último *patch* há até 30 dias. No fim, a seção de exceções: o *spooler* do ERP fica ligado porque o ERP imprime boletos, com aprovação da Marina Prado na mudança MUD-0412 e validade até março de 2027. O JSON do SRV-ARQ-01 é a configuração que a TI exportou: SMBv1 ligado, seis administradores, 74 dias sem *patch*. No código, a função `conforme`, linhas 10 a 15, decide cada item: se o item tem `esperado`, compara igualdade; se tem `minimo`, exige maior ou igual; senão, menor ou igual ao `maximo`. A linha 25 conta o acerto, e a 27 separa o que é exceção aprovada do que é falha. Rodando a auditoria de antes: o SRV-ARQ-01 tem 3 de 10, 30%, com sete falhas em vermelho, cada uma com a salvaguarda do CIS e o valor encontrado. O SRV-ERP-01 também fica em 3 de 10: a linha amarela é a exceção do *spooler*, que não conta como conforme, mas também não aparece como falha. O total é 6 de 20, 30%. Depois do *hardening*, o SRV-ARQ-01 vai a 10 de 10, o ERP a 9 de 10 por causa da exceção, e o total chega a 19 de 20, 95%."
Atenção: o código roda apenas na simulação, e a preparação do ambiente também é simulada (cerca de 5 segundos). O *baseline* é didático e inspirado no CIS Benchmark; os itens reais do *benchmark* têm numeração e texto próprios. Os arquivos de `export/depois` representam a configuração depois do laboratório do slide 10 e da mudança no ERP.
Conclusão: "O *hardening* vira um número, 30% para 95%, que a Rede Tatame pode acompanhar a cada mês."
[Tela: gravação do laboratório do slide 8]

**Slide 9 — Menor privilégio e MFA (8:30–9:20)**
Fala: "O menor privilégio diz que cada pessoa, serviço e programa recebe só o acesso de que precisa, pelo tempo de que precisa. O Caio passa a ter duas contas: caio.mendes para *e-mail* e navegação, e caio.mendes.adm só para administrar, como pede a salvaguarda 5.4. O administrador local de cada máquina ganha senha única e aleatória, trocada pelo LAPS: uma senha descoberta não abre os outros servidores. Contas de serviço perdem o *logon* interativo, contas paradas há 45 dias são desabilitadas, e o MFA vale para o acesso remoto, as aplicações expostas e todo acesso administrativo. Foi a falta dele na VPN que abriu o cenário do Cobalto Austral."

**Slide 10 — Laboratório: fechando portas, serviços e contas no SRV-ARQ-01 (9:20–11:50)**
Objetivo: aplicar no servidor de arquivos as correções que a auditoria apontou, respondendo ao "fechar portas, serviços e contas".
Na tela (PowerShell como administrador no SRV-ARQ-01, sessão de caio.mendes.adm; clicar em "▶ Próximo comando" nove vezes):
1. `Get-NetTCPConnection` com `-State Listen`: lista as portas escutando.
2. `Get-SmbServerConfiguration`: mostra `EnableSMB1Protocol` igual a True.
3. `Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force`.
4. `Get-LocalGroupMember -Group Administradores`: seis membros.
5. `Remove-LocalGroupMember`: remove quatro membros.
6. `Get-Service Spooler, ftpsvc`: os dois em execução, com início automático.
7. `Stop-Service` e `Set-Service -StartupType Disabled`.
8. `Set-NetFirewallRule -DisplayGroup 'Área de Trabalho Remota' -RemoteAddress 10.10.5.0/24`.
9. Desligar o NetBIOS com `SetTcpipNetbios` e repetir a lista de portas.
Fala: "O primeiro comando lista as portas TCP escutando em todas as interfaces, com o processo dono de cada uma. São cinco: 21, do FTP instalado para uma migração antiga; 135, do RPC; 139, do NetBIOS; 445, do SMB; e 3389, do RDP. O segundo mostra que o SMBv1 está ligado; é o protocolo antigo explorado pelo WannaCry em 2017, e o terceiro comando o desliga sem afetar o SMB 3, que atende os compartilhamentos. Depois olhamos o grupo Administradores: seis membros, e os quatro em vermelho não deveriam estar ali, inclusive a conta comum do Caio, a da Ana Lima, do financeiro, e a conta de serviço svc-backup. O `Remove-LocalGroupMember` deixa só o administrador local, com senha do LAPS, e o grupo TI-Admins-Servidores, onde está a conta caio.mendes.adm. A svc-backup vai para o grupo Operadores de Cópia, que tem só o direito de fazer *backup*. Em seguida, o *spooler* de impressão e o FTP: rodando num servidor que não imprime nem precisa de FTP. Paramos os dois e desativamos o início automático. O RDP continua, mas o *firewall* passa a aceitar conexões só da sub-rede da TI, 10.10.5.0/24. Por fim, desligamos o NetBIOS e repetimos a primeira consulta: sobram três portas, 135, 445 e 3389."
Atenção: a saída é simulada; num servidor real, essas mudanças passam por janela de mudança (aqui, MUD-0409) e por teste, porque desligar um serviço usado quebra a operação. O texto embaixo do terminal explica cada comando. "⏭ Executar tudo" roda o roteiro inteiro e "⟲ Reiniciar" limpa o terminal.
Conclusão: "De 5 para 3 portas e de 6 para 2 administradores: o próximo exercício encontra menos caminhos no SRV-ARQ-01."
[Tela: gravação do laboratório do slide 10]

**Slide 11 — Corrigir primeiro o que já está sendo explorado (11:50–12:40)**
Fala: "*Patching* também é *hardening*. O NIST SP 800-40 Rev. 4 trata a correção como manutenção preventiva, um processo com inventário, prioridade, janela de mudança e verificação. Para priorizar, voltamos à Unidade 2: CVSS mede a gravidade, EPSS estima a chance de exploração em 30 dias, e o KEV da CISA lista o que já está sendo explorado. A ordem prática é KEV em ativo exposto, depois EPSS alto em ativo crítico, depois o resto. Se o *patch* não pode entrar já, uma mitigação temporária segura a exposição. E o quadro azul traz o exemplo numérico que vamos explorar agora."

**Slide 12 — Laboratório: quantas falhas ficam abertas ao mesmo tempo? (12:40–13:50)**
Objetivo: mostrar como o prazo de correção muda a exposição, respondendo ao "em que ordem e com que pressa".
Na tela:
1. Ler os valores iniciais: 12 falhas por mês, 45 dias hoje, prazo proposto de 14 dias.
2. Arrastar "Prazo de correção proposto (dias)" para 7.
3. Voltar o prazo a 14 e arrastar "Falhas críticas novas por mês" para 20.
Fala: "A conta é simples: falhas novas por dia vezes os dias até corrigir dá quantas ficam abertas, em média, ao mesmo tempo. Doze por mês são 0,4 por dia; com 45 dias, ficam 18 abertas, o cartão vermelho. Com o prazo de 14 dias, o cartão verde mostra 5,6, e a redução é de 69%. As barras de baixo comparam as duas situações. Com 7 dias, a média cai para 2,8. Se o volume sobe para 20 por mês, com 14 dias ficam 9,3 abertas: mais falhas pedem prazo menor ou mais gente."
Atenção: a conta é a lei de Little (falhas abertas em média = falhas novas por dia × dias até corrigir) e vale para médias em regime estável, não para um mês específico. Volte o prazo a 14 dias antes de mudar o volume.
Conclusão: "Encurtar o prazo de correção reduz a exposição na mesma proporção, e esse é um argumento que a diretoria entende."
[Tela: gravação do laboratório do slide 12]

**Slide 13 — Laboratório: a superfície externa em ordem de risco (13:50–15:30)**
Objetivo: decidir por onde começar o *hardening* da borda, na plataforma da disciplina.
Na tela (simulador na aba Superfície, reiniciado ao abrir o slide):
1. Com "ordenar por risco" marcado, rolar a tabela para a direita até a coluna "Risco" e ler as duas primeiras linhas.
2. Abrir a aba Cenários e, no cartão "Emulação do Grupo Cobalto Austral", clicar em "Iniciar cenário".
3. Na linha do tempo, esperar o primeiro passo, "Login na VPN com a senha vazada de caio.mendes, sem MFA".
Fala: "A aba Superfície lista o que um levantamento externo encontra. A coluna de risco combina CVSS, EPSS, KEV e a criticidade do ativo, com desconto para quem está atrás do WAF. Em primeiro lugar aparece a VPN, com risco 43,8: uma falha crítica de *appliance* de borda, no KEV. Em segundo, o `hml-gestao`, com 32,4, marcado como 'não' na coluna de inventário e sem WAF. Ao iniciar o cenário do Cobalto Austral, o primeiro passo é justamente o *login* na VPN sem MFA. A etiqueta mostra que a regra R11 detectou, mas o passo aconteceu e o cenário segue. Detecção não é bloqueio."
Atenção: a tabela é larga e precisa de rolagem horizontal. O cenário roda em tempo acelerado; se for preciso recomeçar, use "Reiniciar", no topo do simulador. As probabilidades EPSS da tabela são ilustrativas.
Conclusão: "A ordem está dada: corrigir a VPN e exigir MFA fecha o primeiro passo; tirar o `hml-gestao` do ar elimina um ativo inteiro da superfície."
[Tela: gravação do laboratório do slide 13, no simulador]

**Slide 14 — Defesa em profundidade e o NIST CSF 2.0 (15:30–16:10)**
Fala: "Nenhum desses controles é perfeito, e é por isso que eles se organizam em camadas: pessoas, perímetro, rede, *endpoint*, aplicação e dados. No NIST CSF 2.0, de 2024, com suas seis funções, o *hardening* fica sobretudo em Proteger, nas categorias de identidade e acesso e de segurança das plataformas, e depende de Identificar, que cuida do inventário. As Aulas 9 a 11 ficaram em Detectar; a Unidade 4 entra em Responder e Recuperar."

**Slide 15 — Laboratório: as camadas em volta das fichas de alunos (16:10–17:10)**
Objetivo: ver por que uma camada sozinha não basta.
Na tela:
1. Deixar a cena girar alguns segundos com as seis camadas ligadas e ler a legenda.
2. Clicar no botão "Endpoint" para desligar essa camada.
3. Desligar também "Perímetro", "Rede" e "Aplicação".
Fala: "Os pontos vermelhos são tentativas de ataque vindo de fora; quando uma camada barra, o ponto fica azul e some. No centro está o `db-alunos`. Com as seis camadas, quase nada chega, e a legenda conta os barrados e os que chegaram. Desligar o Endpoint é como ter um servidor sem *hardening*: mais pontos passam, mas as outras camadas ainda seguram muitos. Com quase tudo desligado, o contador de 'chegaram ao ativo' dispara."
Atenção: a cena precisa de internet para carregar o three.js; as chances de bloqueio são ilustrativas.
Conclusão: "Nenhuma camada precisa ser perfeita, desde que existam várias."
[Tela: gravação do laboratório do slide 15]

**Slide 16 — O que você verá na próxima unidade (17:10–17:45)**
Fala: "Monitoramos, detectamos, caçamos e fechamos caminhos. Mas algum ataque ainda vai passar, e a Unidade 4, Resposta a Incidentes e Purple Team, começa exatamente aí. Na Aula 13, o ciclo de resposta a incidentes; na 14, a coleta de evidências e a linha do tempo; na 15, os exercícios *purple team* que validam as detecções; e na 16, o relatório final com achados, riscos e métricas."

**Slide 17 — De volta ao problema (17:45–18:35)**
Fala: "Voltemos à pergunta da Marina. Os quatro cartões resumem: ligamos cada passo do Cobalto Austral a um controle; medimos os servidores contra o *baseline* e saímos de 30% para 95%; fechamos portas, serviços e contas no SRV-ARQ-01; e definimos a ordem de correção, com prazo de 14 dias. Respondendo à pergunta da aula: a Rede Tatame fecha primeiro o que está exposto e já é explorado, a VPN, o MFA e o `hml-gestao`; depois aplica o *baseline* nos servidores, reduz contas e privilégios ao mínimo e mantém o *patching* com prazo e prioridade, medindo a conformidade a cada ciclo."

**Slides 18 a 20 — Pontos-chave, referências e encerramento (18:35–19:20)**
Fala: "Para levar desta aula: *hardening* começa pelo inventário; CIS Benchmarks dizem como configurar e CIS Controls organizam o programa; menor privilégio e MFA cortam a movimentação lateral; e o prazo de correção define a exposição. Com isso, fechamos a Unidade 3. Na Unidade 4, vamos responder a um incidente de verdade, da preparação à recuperação. Até a próxima aula!"

[Envato: "server room technician", "padlock network security", "checklist on laptop screen". Slides de apoio: mini-mapa do slide 3, fluxo do slide 5 e cartões do slide 17.]

## Quiz não avaliativo

### Questão 1 (verdadeiro ou falso)

Uma regra YARA que procura o *hash* SHA-256 exato de um arquivo malicioso continua detectando uma variante desse arquivo em que o adversário alterou apenas um *byte*, porque a assinatura descreve o comportamento do programa.

( ) Verdadeiro  
(X) Falso

### Questão 2 (múltipla escolha)

Na caça a ameaças, o *baseline* de saída de dados de um servidor é de 200 MB por dia, com desvio-padrão de 50 MB. Em um dia, o servidor enviou 450 MB para a internet. O escore z dessa observação e a leitura mais adequada são:

a) 0,25; o volume está dentro do esperado.  
b) 2,5; o volume é alto, mas comum para esse servidor.  
*c) 5; o volume está muito acima do *baseline* e merece investigação.  
d) 9; o volume prova que houve exfiltração de dados.

### Feedback

**Questão 1 — Falso.** O *hash* é uma assinatura do arquivo inteiro: mudar um único *byte* produz um *hash* completamente diferente, e a regra deixa de casar. Por isso as assinaturas de *hash* ficam na base da Pirâmide da Dor. Para resistir a variantes, a detecção precisa olhar características mais estáveis (cadeias de texto e estruturas, em uma regra YARA mais elaborada) ou o comportamento do programa durante a execução.

**Questão 2 — Alternativa c.** O escore z mede quantos desvios-padrão a observação está acima da média: (450 − 200) ÷ 50 = 250 ÷ 50 = 5. Um valor tão distante do *baseline* é uma anomalia forte e justifica abrir uma investigação. A alternativa d exagera: a anomalia estatística indica onde olhar, mas não prova exfiltração. Ela pode vir de um *backup* novo ou de uma mudança legítima, e só a investigação confirma ou descarta a hipótese.

## Material complementar

### Direto da fonte (livro da Biblioteca Virtual)

- **Texto provocativo:** Um adversário paciente pode passar meses dentro de uma rede sem disparar nenhum alerta. O capítulo indicado discute por que os modelos tradicionais, que esperam o incidente acontecer para reagir, não bastam contra ameaças persistentes avançadas (APTs). Leia pensando na Aula 11: que hipótese de caça você formularia para encontrar um invasor que já está lá dentro e se esforça para parecer um usuário comum?
- **Nome do livro:** LEVI, Hiago Kin. *Confronto cibernético*: técnicas e táticas de enfrentamento e resposta a ameaças persistentes avançadas (APTs). Rio de Janeiro: Brasport, 2026. *E-book*.
- **Capítulo:** 3 — Por que o padrão de resposta do NIST é insuficiente contra APTs
- **Link de acesso:** <https://plataforma.bvirtual.com.br/Acervo/Publicacao/235882>
- **Aula em que entra:** Aula 11

### Para mergulhar no assunto (saiba mais)

- **Texto provocativo:** Quantas configurações separam um servidor recém-instalado de um servidor endurecido? Os CIS Benchmarks são guias gratuitos, escritos por consenso entre profissionais do mundo inteiro, com centenas de recomendações para sistemas operacionais, nuvem e aplicações. Baixe o *benchmark* do sistema que você mais usa, escolha cinco recomendações de nível 1 e confira quantas o seu computador já atende.
- **Link:** <https://www.cisecurity.org/cis-benchmarks> (download gratuito em PDF mediante cadastro; conteúdo em inglês)
- **Link complementar:** documentação oficial do Security Onion 2.4, a plataforma aberta de monitoramento de rede usada como referência na Aula 9 — <https://docs.securityonion.net/en/2.4/>
- **Aula em que entra:** Aula 12 (e Aula 9, no link complementar)

### Podcast (curadoria, até 45 min)

- **Texto provocativo:** Analistas de SOC começam o dia se atualizando sobre o que os adversários estão fazendo. Neste episódio de cerca de 10 minutos, o SANS Internet Stormcast comenta, entre outros assuntos, truques de ofuscação do *malware* Formbook. Ouça e reflita com o que vimos na Aula 10: que tipo de detecção sobrevive melhor à ofuscação, a assinatura do arquivo ou o comportamento do programa em execução?
- **Nome do podcast:** SANS Internet Stormcast
- **Nome do episódio:** SANS Stormcast Friday, November 14th, 2025: SmartApeSG and ClickFix; Formbook Obfuscation Tricks; Sudo-rs Vulnerabilities; SANS Holiday Hack Challenge (14 nov. 2025, em inglês, cerca de 10 min)
- **Link:** <https://www.youtube.com/watch?v=lkHDgFJUZv0> (página do episódio: <https://isc.sans.edu/podcastdetail/9700>)
- **Aula em que entra:** Aula 10

### Artigo científico

- **Texto provocativo:** E se o próprio sistema de monitoramento pudesse ordenar os alertas pela probabilidade de serem ataques reais, em vez de deixar o analista se afogar na fila? Este artigo, apresentado em um dos principais simpósios de segurança de redes, propõe usar o histórico de causalidade dos eventos (proveniência) para reduzir a fadiga de alertas. Leia e reflita: que limites essa automação ainda tem, e que fontes de telemetria ela exige?
- **Link:** <https://www.ndss-symposium.org/ndss-paper/nodoze-combatting-threat-alert-fatigue-with-automated-provenance-triage/>
- **Aula em que entra:** Aula 9
- **Referência ABNT:** HASSAN, Wajih Ul *et al*. NoDoze: combatting threat alert fatigue with automated provenance triage. *In*: NETWORK AND DISTRIBUTED SYSTEM SECURITY SYMPOSIUM (NDSS), 2019, San Diego. *Proceedings* [...]. Reston: Internet Society, 2019.
