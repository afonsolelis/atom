# Roteiros das videoaulas — Unidade 4 — Resposta a Incidentes e Purple Team

Disciplina: Red Team & Blue Team Strategies  
Professor: Afonso Cesar Lelis Brandão

> Cópia dos roteiros de `unidade_4.md`, só para a gravação. O texto de origem continua no `unidade_4.md` (é dele que sai o DOCX).

## Roteiro da Videoaula 13 — "Quatro horas na fila: o que fazer quando o alerta finalmente é aberto?"

Duração-alvo: 15 a 20 minutos. Deck: unidade_4/slides/aula13.html (23 slides).

**Slides 1 e 2 — Capa e sumário (0:00–0:30)**
Fala: "Olá! Bem-vindo à Aula 13, que abre a Unidade 4, a última da disciplina. Hoje o tema é o ciclo de resposta a incidentes: preparação, detecção, contenção, erradicação e recuperação. No sumário você vê o caminho: um incidente na Rede Tatame, o ciclo do NIST, seis laboratórios e, no fim, o prazo da ANPD e as lições aprendidas."
[Tela: capa; parar 5 segundos no sumário]

**Slide 3 — O problema de hoje na Rede Tatame (0:30–1:45)**
Fala: "Terça-feira, 1º de dezembro, 23h14. A regra R8 do motor de correlação avisa que uma ferramenta de acesso remoto não aprovada, o ConectaJá, foi instalada no SRV-ERP-01, o servidor do ERP financeiro da sede. O alerta é de severidade alta, mas Luiza Ferraz, de plantão no SOC, só o abre às 3h20 da madrugada. A conta usada é a de Caio Mendes, da TI, e o servidor está conversando com um endereço externo, 198.51.100.77. O que está em jogo é sério: o ERP guarda nome, CPF e situação de pagamento de alunos e responsáveis, inclusive de menores. Repare no mapa à direita: o caminho em destaque vai da internet à VPN, passa pelo AD e chega ao SRV-ERP-01, em vermelho. A pergunta da aula é esta: como a Rede Tatame conduz este incidente, contendo sem destruir evidências, recuperando o ERP e comunicando a ANPD no prazo? Guarde os papéis: Marina Prado coordena, Luiza Ferraz está no SOC, Caio Mendes é da TI e Rafael Tavares cuida das regras de detecção."
[Take de apoio: sala de monitoramento à noite, analista diante de alertas na tela — Envato]

**Slide 4 — O que você verá nesta unidade (1:45–2:20)**
Fala: "Nesta unidade, o mesmo caso atravessa as quatro aulas: o incidente INC-2026-1202-01. Hoje, conduzimos a resposta. Na Aula 14, coletamos as evidências e montamos a linha do tempo. Na Aula 15, validamos as detecções num exercício *purple team*, com técnicas emuladas. E na Aula 16 escrevemos o relatório final, com achados, riscos, recomendações e métricas. A ideia é sair da disciplina sabendo responder com método e provar que a defesa melhorou."

**Slide 5 — Evento, alerta e incidente (2:20–3:00)**
Fala: "Três palavras que parecem sinônimas, mas têm sentidos diferentes. Evento é qualquer ocorrência observável: um *login*, uma conexão, um programa instalado. Alerta é a sinalização, gerada por uma regra, de que um evento pode ser malicioso; a R8 gerou um alerta. Incidente é o que compromete, ou ameaça de forma iminente, a confidencialidade, a integridade ou a disponibilidade. Quando Luiza declara o incidente às 3h20, ela toma uma decisão formal: abre um registro, chama pessoas e pode disparar obrigações legais."

**Slide 6 — NIST SP 800-61: da Rev. 2 à Rev. 3 (3:00–3:50)**
Fala: "O guia mais usado para organizar a resposta é o NIST SP 800-61. A Revisão 2, de 2012, que está na bibliografia da disciplina, tem quatro fases: preparação; detecção e análise; contenção, erradicação e recuperação; e atividade pós-incidente. Em abril de 2025, o NIST publicou a Revisão 3, que substitui a anterior e encaixa a resposta nas seis funções do CSF 2.0. Olhe a tabela: a preparação corresponde a Governar, Identificar e Proteger; a detecção, a Detectar; a contenção, a erradicação e a recuperação, a Responder e Recuperar; e o pós-incidente volta para Identificar, como melhoria."

**Slide 7 — Laboratório: as quatro fases dentro das seis funções (3:50–5:00)**
Objetivo: situar o ciclo clássico dentro do CSF 2.0 e ver o nosso incidente nesse mapa.
Na tela:
1. O diagrama abre no passo "Rev. 2 (2012) · o ciclo clássico" (contador "1 / 7"). Apontar as quatro caixas da esquerda.
2. Clicar em "▶ Avançar": "Rev. 3 (2025) · seis funções do CSF 2.0"; apontar as seis caixas da direita.
3. Clicar em "▶ Avançar" três vezes, parando em cada ligação: Preparação; Detecção e análise; Contenção, erradicação e recuperação.
4. Clicar em "▶ Avançar": "Pós-incidente: Identificar (melhoria)", com a seta tracejada.
5. Clicar em "▶ Avançar" uma última vez: "O INC-2026-1202-01 no mapa" (contador "7 / 7").
Fala: "À esquerda estão as quatro fases da Rev. 2, em sequência. À direita, as seis funções do CSF 2.0. Repare que a preparação acende três funções de uma vez: políticas, inventário, *playbooks* e treinamento deixam de ser assunto só da equipe de resposta e passam a ser da gestão. Detecção e análise vão para Detectar, onde entram o SIEM, o EDR e a caça a ameaças da Unidade 3. Contenção, erradicação e recuperação se dividem entre Responder e Recuperar. E o pós-incidente volta, pela seta tracejada, para Identificar: as lições mudam o que a organização sabe dos próprios riscos. No último passo aparece o nosso caso: o *playbook* aprovado pela CISO em Governar, o alerta das 23h14 em Detectar, o isolamento das 3h41 em Responder, o *backup* em Recuperar e a reunião de 9 de dezembro em Identificar."
Atenção: use "▶ Avançar"; o botão "⏯ Auto" troca de passo sozinho e atrapalha a narração. Espere os pacotes animados percorrerem as ligações antes de clicar de novo.
Conclusão: "A Rev. 3 mantém as atividades das quatro fases, mas as coloca dentro da gestão de riscos da organização inteira."
[Tela: gravação do laboratório do slide 7]

**Slide 8 — *Playbooks* e papéis (5:00–5:40)**
Fala: "A preparação tem dois produtos concretos. O primeiro é o *playbook*: um roteiro, passo a passo, para um tipo de incidente, com responsáveis, critérios de decisão, contatos e prazos. Parte dele pode ser automatizada por uma plataforma SOAR, de orquestração, automação e resposta. O segundo são os papéis: o coordenador do incidente decide e prioriza, os analistas investigam e executam, e o jurídico, a comunicação e o encarregado de dados entram desde as primeiras horas. Às 3h20, ninguém deveria estar perguntando quem decide."

**Slide 9 — Antes do código: onde achar e como instalar o que o laboratório usa (5:40–6:10)**
Fala: "Antes do código, veja o que o laboratório usa e de onde vem. O Visual Studio Code sai do site oficial, com as extensões de Python e de YAML. O Python 3.12 vem do python.org. O único pacote de terceiros é o PyYAML, que lê os *playbooks*. Atenção a uma armadilha: o código escreve `import yaml`, mas o pacote se chama PyYAML, e existe outro projeto de nome parecido, o `pyaml`. Confira o nome no PyPI e fixe a versão: a ferramenta usada no incidente tem de ser a mesma que foi testada antes dele."

**Slide 10 — Laboratório: o *playbook* de acesso remoto não aprovado (6:10–9:10)**
Objetivo: mostrar que um *playbook* revisado e conferido por código diz quem faz o quê, em que ordem e com que prazo.
Na tela (o VS Code ocupa o slide inteiro; o roteiro do laboratório abre e fecha com a tecla G ou com o botão "☰ Roteiro" da barra de status e deve ficar fechado durante a gravação):
1. No painel do terminal, clicar em "⬇ Preparar o ambiente" e esperar o botão mudar para "✓ Ambiente pronto". Durante a instalação, o editor mostra o `requirements.txt`.
2. No explorador, abrir `acesso-remoto-v1.yaml`, na pasta `playbooks`, e rolar devagar.
3. Abrir `acesso-remoto-v2.yaml` e parar nas linhas destacadas.
4. Abrir `validar_playbook.py`, na pasta `ferramentas`.
5. Clicar em "▶ Validar v1".
6. Clicar em "▶ Validar v2".
7. Clicar em "▶ Prazo ANPD (02/12)", que abre o `prazo_anpd.py`.
Fala (preparação): "O VS Code agora ocupa a tela inteira, como no meu computador. Antes de rodar, preparo o ambiente. O `python3 --version` confirma o interpretador, Python 3.12.7. O `python3 -m venv .venv` cria um ambiente virtual, uma instalação separada só para este projeto, e o `source .venv/bin/activate` liga esse ambiente: repare no `(.venv)` no início da linha. O `pip install -r requirements.txt` instala o que o arquivo aberto no editor lista, o PyYAML 6.0.3. Na saída, 'Downloading' mostra o arquivo que veio do PyPI e 'Successfully installed' confirma a instalação. O `pip list` fecha a conferência: só o pip e o PyYAML."
Fala (arquivos e execuções): "A v1 é um rascunho de 2025 que ninguém revisou. Note a ordem das etapas: triagem, isolar, erradicar e só depois preservar. E a etapa 'acionar' chama só o coordenador e o jurídico, sem dizer quem é o responsável. A v2 foi revisada em 25 de novembro por Marina e Luiza. Ela tem uma linha nova no gatilho, `triagem_maxima_min: 30`: alerta alto sem triagem em 30 minutos é escalonado. Ela isola com um comentário claro, 'isolar, não desligar: a memória é evidência', bloqueia a conta e o destino, preserva antes de erradicar, aciona o encarregado e a comunicação e termina com as lições aprendidas. Agora o validador. Ele lê o YAML e faz quatro perguntas. Toda etapa que não é automática tem responsável? Os quatro papéis obrigatórios, coordenador, jurídico, encarregado e comunicação, aparecem em algum `notificar`? A linha que compara `ids.index("preservar")` com `ids.index("erradicar")` verifica a ordem. E existe a etapa de lições aprendidas? Rodando na v1, saem quatro problemas em vermelho: a etapa 'acionar' sem responsável, comunicação e encarregado nunca acionados, evidências preservadas depois da erradicação e a falta das lições aprendidas. Na v2: nove etapas e nenhum problema. Por fim, o prazo. A função `dias_contados` anda um dia de cada vez a partir do conhecimento e só guarda os dias aprovados por `dia_util`, que exclui sábado, domingo e feriados. Com ciência em 2 de dezembro, quarta-feira, os dias úteis são quinta, 3; sexta, 4; e segunda, 7. O sábado e o domingo aparecem como 'não conta'. Prazo final: 7 de dezembro."
Atenção: a preparação é simulada e leva cerca de 10 segundos; espere "✓ Ambiente pronto" antes das execuções. As saídas mostradas são as que o código produz de verdade. O script de prazo também aceita `--pequeno-porte`, que conta seis dias úteis (prazo em dobro, até 10/12); comente sem rodar. A regra de contagem e os feriados locais devem ser confirmados com o jurídico.
Conclusão: "Com o *playbook* v2, a madrugada de 2 de dezembro tem roteiro, ordem e prazo. Essa é a parte da preparação na resposta à pergunta da aula."
[Tela: gravação do laboratório do slide 10]

**Slide 11 — O Wazuh como console de resposta (9:10–9:45)**
Fala: "Agora a detecção e análise, a fase em que se confirma o alerta e se definem o escopo e a severidade. O console que vamos usar é o Wazuh, uma plataforma aberta de SIEM e XDR. Agentes enviam os eventos de cada sistema, e as regras dão a cada alerta um nível de 0 a 15. O módulo de *active response* executa ações configuradas, como bloquear um endereço no *firewall* da máquina. O Security Onion, citado na ementa, pode usar o Wazuh e acrescenta a análise do tráfego de rede."

**Slide 12 — Laboratório: a triagem do alerta no Wazuh (9:45–12:00)**
Objetivo: confirmar o alerta da R8, definir o escopo e medir os tempos do caso.
Na tela (o console abre com a busca "1. O alerta da R8" já executada):
1. Ler a linha da busca 1 e a nota amarela abaixo da tabela.
2. Clicar em "2. Quem abriu a sessão?".
3. Clicar em "3. De onde veio a conta?".
4. Clicar em "4. Para onde o ERP fala?" e apontar o histograma.
5. Clicar em "5. Active response: conter".
6. Clicar em "6. Tempos do caso".
Fala: "Esta tela imita o Wazuh. No alto ficam a consulta, o período e o índice de alertas; à esquerda, as buscas salvas do caso. A primeira mostra o alerta: agente SRV-ERP-01, regra 100208, nível 12, a descrição da R8 e o estado, sem triagem até as 3h20. Regras locais do Wazuh usam IDs a partir de 100000, e o nível 12 é de alta importância. A segunda busca filtra o evento 4624 com tipo de logon 10, que é um acesso remoto por RDP: às 23h06, a conta caio.mendes entrou no servidor a partir de um endereço da VPN. A R5, que alertaria isso, estava desligada. A terceira vai à VPN: seis pedidos de MFA seguidos, recusados ou sem resposta, até um 'aprovado' às 22h58. Isso tem nome: fadiga de MFA. Como houve MFA, a R11 não disparou. O primeiro evento malicioso do caso é esse login, às 22h58min10s. A quarta mostra 19 conexões do ConectaJá para 198.51.100.77, uma a cada cinco minutos, das 2h10 às 3h40; o histograma fica regular, como um relógio. O proxy registra a conexão, mas não o volume, e por isso o envio de 2,8 GB só aparece na análise. A quinta mostra a contenção às 3h41: o EDR isola o servidor sem desligá-lo, a conta é desabilitada, com o evento 4725 no AD, e o script `firewall-drop` do Wazuh bloqueia o destino. A sexta resume o caso: MTTD de 4 horas, 21 minutos e 50 segundos, do primeiro evento à abertura do caso, e MTTR de 21 minutos, da abertura à contenção."
Atenção: os dados e o ID 100208 são fictícios; os campos `rule.id`, `rule.level`, `agent.name` e `data.win.system.eventID` e o script `firewall-drop` existem no Wazuh. Espere a tabela terminar de aparecer antes de clicar na busca seguinte.
Conclusão: "A regra funcionou em 35 segundos. O atraso de 4 horas e 5 minutos está entre o alerta e a triagem, e isso vai para as lições aprendidas."
[Tela: gravação do laboratório do slide 12]

**Slide 13 — Contenção, erradicação e recuperação (12:00–12:40)**
Fala: "Depois de confirmar, é hora de responder. Contenção impede que o dano aumente: isolar o servidor, desabilitar a conta, bloquear o destino. Erradicação remove a ferramenta e as contas do invasor, redefine credenciais e corrige a porta de entrada, que aqui foi a fadiga de MFA. Recuperação restaura de um *backup* íntegro, anterior ao comprometimento, e monitora com atenção redobrada. E repare no destaque: isolar, e não desligar. Desligar o servidor interrompe o ataque, mas apaga a memória, onde estão processos e conexões. Como coletar essa memória é o assunto da próxima aula."

**Slide 14 — Laboratório: plataforma Rede Tatame, conter a tempo (12:40–14:50)**
Objetivo: ver na plataforma o efeito de conter cedo e de não conter.
Na tela:
1. No seletor de velocidade, ao lado do relógio, escolher "1 s = 5 s".
2. Na aba "Cenários", clicar em "Iniciar cenário" no cartão "Acesso remoto não aprovado e saída de dados".
3. Quando o contador da aba "SOC" acender, abrir o "SOC", clicar em "Investigar" no alerta da R8 (host SRV-ERP-01) e, em seguida, em "Conter".
4. Voltar a "Cenários" e ler a linha do tempo: o passo "Envio de 2,8 GB para armazenamento externo" aparece como "interrompido pela contenção".
5. Trocar a velocidade para "1 s = 1 min" e clicar em "Repetir com as fontes e regras atuais". Não conter nada e esperar os três passos.
Fala: "Agora o mesmo caso na plataforma da disciplina. A R8 já está ligada neste slide, como na Rede Tatame depois da caça da Aula 11. Inicio o cenário. O primeiro passo é a instalação do ConectaJá no SRV-ERP-01. Em alguns segundos, o alerta da R8 chega ao SOC. Clico em Investigar: à direita aparecem a regra, a lógica dela e o tempo do primeiro sinal até o alerta. Clico em Conter: o servidor fica isolado e o cenário é interrompido. De volta aos Cenários, o envio dos 2,8 GB não aconteceu: 'interrompido pela contenção'. Agora repito o cenário com as mesmas regras, mas faço o que o plantão fez naquela madrugada: nada. As conexões periódicas aparecem como 'visto nos logs, sem alerta', e o envio dos 2,8 GB passa como 'não detectado', porque a fonte de saída de rede está desligada. Nos indicadores abaixo da linha do tempo: um detectado, um visto sem alerta e um não detectado."
Atenção: conter antes do terceiro passo, que acontece cerca de 80 segundos depois do início na velocidade "1 s = 5 s". Se as conexões periódicas já tiverem ocorrido, elas aparecem como "visto nos logs, sem alerta"; os passos ainda pendentes ficam como "interrompido pela contenção". "Repetir com as fontes e regras atuais" mantém a R8 ligada; "Reiniciar" volta ao padrão, com a R8 desligada. A plataforma é simulada.
Conclusão: "Conter cedo salva os dados. Com 4 horas de fila, a contenção chega depois da saída."
[Tela: gravação do laboratório do slide 14]

**Slide 15 — Laboratório: o ERP pode voltar à produção? (14:50–16:20)**
Objetivo: conferir a erradicação e a recuperação antes de liberar o SRV-ERP-01.
Na tela:
1. Clicar em "▶ Próximo comando": `Get-WBBackupSet`.
2. "▶ Próximo comando": a busca do serviço ConectaJá.
3. "▶ Próximo comando": `Get-ADUser caio.mendes`.
4. "▶ Próximo comando": `Get-NetFirewallRule`.
5. "▶ Próximo comando": `Test-NetConnection` e a linha final do *checklist*.
Fala: "Estamos no PowerShell do SRV-ERP-01, ainda numa rede de quarentena. O primeiro comando lista os *backups*: o escolhido é o de 1º de dezembro às 20h, anterior ao primeiro evento malicioso, às 22h58. Restaurar um *backup* posterior poderia trazer o invasor junto. O segundo procura qualquer serviço cujo nome comece com ConectaJa: nenhum resultado, a ferramenta foi erradicada. O terceiro mostra a conta de Caio: senha redefinida em 3 de dezembro às 9h12 e a conta ainda desabilitada, porque ela só volta depois do novo cadastro de MFA com correspondência de número. O quarto confirma a regra de *firewall* que bloqueia a saída para 198.51.100.77. O último tenta a conexão na porta 443: `TcpTestSucceeded` falso. O *checklist* fecha em cinco de cinco, e o ERP volta à produção às 14h de 3 de dezembro, com monitoração reforçada por 30 dias."
Atenção: o terminal é simulado; os *cmdlets* existem no Windows Server, mas as saídas são ilustrativas. Nenhum comando altera o servidor: são só conferências.
Conclusão: "Recuperar exige provar que o invasor saiu e que o caminho dele está fechado, antes de religar o serviço."
[Tela: gravação do laboratório do slide 15]

**Slide 16 — LGPD e a Resolução CD/ANPD nº 15/2024 (16:20–17:05)**
Fala: "Agora a comunicação. O art. 48 da LGPD exige comunicar à ANPD e aos titulares o incidente que possa acarretar risco ou dano relevante. A Resolução CD/ANPD nº 15, de 2024, fixou três dias úteis, contados do conhecimento de que dados pessoais foram afetados, para a ANPD, no art. 6º, e para os titulares, no art. 9º. O registro do incidente fica guardado por no mínimo cinco anos, pelo art. 10, e para agentes de pequeno porte os prazos contam em dobro. No nosso caso, a análise confirmou às 10h30 de 2 de dezembro que os 2,8 GB eram planilhas de cobrança de 9.400 alunos e responsáveis. O prazo corre daí, e não do fim da investigação: vai até 7 de dezembro."

**Slide 17 — Exemplo numérico: tempos do incidente e prioridade (17:05–17:40)**
Fala: "Vamos juntar os números. MTTD: do login das 22h58min10s à abertura do caso, às 3h20, 4 horas, 21 minutos e 50 segundos. MTTR: da abertura, às 3h20, à contenção, às 3h41, 21 minutos. O alerta ficou na fila 4 horas, 5 minutos e 20 segundos. E o prazo da ANPD termina em 7 de dezembro. Embaixo, uma fórmula para quando há vários incidentes ao mesmo tempo: criticidade do ativo, de 1 a 5, vezes confiança, de 1 a 3, vezes abrangência, de 1 a 3. O ERP dá 5 vezes 3 vezes 2, ou 30; o notebook que acessou um domínio recém-registrado, 6; a varredura barrada pelo WAF, 4."

**Slide 18 — Laboratório: qual incidente atender primeiro? (17:40–18:30)**
Objetivo: usar a pontuação para ordenar a fila do plantão.
Na tela:
1. Conferir os valores iniciais e a frase "Ordem de atendimento: A (30), B (6), C (4)."
2. Na linha (B), mudar "Abrangência" para 3.
3. Na linha (B), mudar "Confiança" para 3.
Fala: "Cada linha é um incidente, e as três listas são os fatores da fórmula. Suponha que o notebook NB-FIN-031, o incidente B, também abriu conexão para 198.51.100.77. Subo a abrangência para 3: a nota vai de 6 para 18 e fica amarela. Agora a confiança também sobe para 3: 27, em vermelho. Mesmo assim, B continua atrás de A, que tem 30. A frase embaixo mostra a ordem de atendimento atualizada."
Atenção: a fila se reordena sozinha a cada mudança. Os casos B e C são ilustrativos.
Conclusão: "A pontuação deixa a decisão explícita e auditável, mas quem decide é o coordenador do incidente."
[Tela: gravação do laboratório do slide 18]

**Slide 19 — Lições aprendidas sem caça a culpados (18:30–19:05)**
Fala: "Em 9 de dezembro, a reunião de lições aprendidas, sem caça a culpados. O que funcionou? A R8 disparou 35 segundos depois da instalação, e a contenção levou 21 minutos. Onde demorou? O alerta alto esperou 4 horas e 5 minutos na fila. O que muda? Escalonar alerta alto sem triagem em 30 minutos, adotar MFA com correspondência de número contra a fadiga de MFA e ligar a R5 e a fonte de saída de rede com a R9. Cada item vira ação com dono e prazo, e as regras novas serão testadas no exercício *purple team* da Aula 15."

**Slide 20 — De volta ao problema (19:05–19:35)**
Fala: "Voltemos à madrugada de 2 de dezembro. Preparar: o *playbook* v2 define papéis e ordem. Detectar e analisar: no Wazuh, o alerta virou caso com escopo. Conter e recuperar: isolar sem desligar, bloquear conta e destino e restaurar o *backup* de 1º de dezembro às 20h. Comunicar e aprender: ciência em 2 de dezembro, comunicação até 7 e ações a partir de 9. Então, como a Rede Tatame conduz o incidente? Seguindo o ciclo do NIST: com o *playbook* pronto, isola o SRV-ERP-01 sem apagar a memória, erradica o ConectaJá e a credencial usada, recupera de um *backup* íntegro, comunica a ANPD em três dias úteis e transforma a demora da triagem em melhoria."

**Slides 21 a 23 — Pontos-chave, referências e encerramento (19:35–20:00)**
Fala: "Para levar desta aula: evento, alerta e incidente são diferentes; a Rev. 3 distribui as fases da Rev. 2 pelas funções do CSF 2.0; *playbooks* e papéis economizam tempo; a contenção isola sem destruir evidências; e a comunicação à ANPD tem três dias úteis. As referências estão no slide. Na próxima aula, voltamos ao SRV-ERP-01 com a perita M. Teixeira para coletar as evidências e montar a linha do tempo do incidente. Até lá!"
[Tela: slide de encerramento por 5 segundos]

## Roteiro da Videoaula 14 — "Desligar ou não desligar? O que as evidências contam sobre a madrugada do incidente"

Duração-alvo: 15 a 20 minutos. Deck: unidade_4/slides/aula14.html (19 slides).

**Slides 1 e 2 — Capa e sumário (0:00–0:40)**
Fala: "Olá! Esta é a Aula 14. Na aula passada, a Rede Tatame respondeu a um incidente real e conteve o servidor do ERP. Hoje vamos fazer a pergunta seguinte: como provar o que aconteceu? No sumário você vê o caminho: o que é evidência digital, a ordem em que ela é coletada, a cadeia de custódia com *hash*, a linha do tempo e quatro laboratórios, um deles no Wireshark."
[Tela: capa; parar 5 segundos no sumário]

**Slide 3 — O problema de hoje na Rede Tatame (0:40–2:00)**
Fala: "São três e quarenta e um da manhã de 2 de dezembro. Luiza Ferraz, analista de SOC, acaba de isolar o SRV-ERP-01 pelo EDR. O incidente se chama INC-2026-1202-01: alguém instalou o ConectaJá, uma ferramenta de acesso remoto não aprovada, e mandou dados para o endereço 198.51.100.77. O dano parou. Mas Marina Prado, a CISO, precisa explicar à diretoria, ao jurídico e talvez à ANPD por onde o invasor entrou, o que levou e quando. E a perita externa, M. Teixeira, avisa: evidência sem registro de custódia pode ser contestada. Repare no mapa: o caminho vai da internet à VPN, passa pelo AD e chega ao SRV-ERP-01, em vermelho. A pergunta da aula é esta: como reconstruir o que aconteceu no SRV-ERP-01, em ordem e com provas que resistam a uma contestação?"
[Take de apoio: sala de SOC de madrugada, analista diante de vários monitores — Envato]

**Slide 4 — O que conta como evidência digital (2:00–3:00)**
Fala: "Evidência digital é qualquer informação em forma digital que ajude a provar ou refutar um fato: a memória de um servidor, uma imagem de disco, um *login* na VPN, uma captura de tráfego. A norma ABNT NBR ISO/IEC 27037 divide o trabalho em quatro etapas: identificar o que é relevante, coletar, adquirir uma cópia fiel e preservar até o fim do caso. Em todas elas valem três exigências: método repetível, evidência íntegra e cada ação documentada. E no Brasil o Código de Processo Penal define a cadeia de custódia nos artigos 158-A a 158-F, desde a Lei 13.964, de 2019. Guarde a frase do quadro azul: a coleta começa na contenção."

**Slide 5 — Do mais volátil para o menos volátil (3:00–4:10)**
Fala: "A RFC 3227, de 2002, dá a ordem da coleta: primeiro o que desaparece mais rápido. Os registradores e o cache somem em nanossegundos, então na prática ficam de fora. Em seguida vêm a tabela de rotas, o cache ARP, os processos, as estatísticas do núcleo e a memória. No SRV-ERP-01, é ali que estão o processo do ConectaJá e as conexões com 198.51.100.77. Depois, os arquivos temporários, o disco, os registros remotos, a topologia e, por último, as mídias de arquivamento, como o *backup* da noite de 1º de dezembro. Leia a tabela de cima para baixo: é a ordem em que Luiza trabalhou."

**Slide 6 — Laboratório: do alerta ao lacre (4:10–6:10)**
Objetivo: seguir, no SRV-ERP-01, a ordem certa da coleta e ver o que se perde com o atalho errado.
Na tela (passo a passo do que clicar, na ordem):
1. O diagrama abre no passo "03:20 · O caso é aberto" (contador "1 / 10"). Apontar o nó "Caso aberto".
2. Clicar em "▶ Avançar": "O atalho errado · Desligar da tomada". O nó "Desligar" fica em destaque de alerta e o resto escurece.
3. Clicar em "▶ Avançar": "03:41 · Isolar pela rede".
4. Clicar em "▶ Avançar" três vezes: "03:46 · Primeiro o mais volátil", "03:58 · Memória RAM" e "05:30 · Imagem do disco".
5. Clicar em "▶ Avançar": "06:12 · Registros remotos".
6. Clicar em "▶ Avançar" três vezes: "Hash de cada arquivo", "Cadeia de custódia" e "09:10 · Entrega à perita" (contador "10 / 10").
Fala: "O caso abre às 03h20, quando Luiza confirma o alerta da regra R8. A primeira tentação é desligar o servidor da tomada. Isso para a saída de dados, mas apaga a memória: o processo do ConectaJá, as conexões abertas e as chaves de sessão somem. Por isso o *playbook* manda isolar. Às 03h41 o EDR corta a rede do servidor, menos o canal com o próprio console, e a máquina continua ligada. Às 03h46 saem os voláteis: processos, conexões, rotas, ARP. Às 03h58 termina a cópia dos 32 GB de memória. Só às 05h30 fica pronta a imagem do disco, no formato E01, que guarda o conteúdo e os dados da aquisição. Os registros remotos, do SIEM, da VPN, do AD, do EDR e o *pcap* do sensor, vêm por último, porque estão fora do servidor e não se perdem com ele. Cada arquivo recebe o seu *hash*, o formulário registra tudo, o disco externo vai com o lacre 0457 e, às 09h10, a perita M. Teixeira recebe o material."
Atenção: o botão "⏯ Auto" avança sozinho; para gravar, use "▶ Avançar" e leia o texto de cada passo na barra abaixo do diagrama. Os horários seguem a linha do tempo do incidente.
Conclusão: "Isolar, não desligar, e ir do mais volátil para o menos volátil. Essa é a primeira parte da resposta."
[Tela: gravação do laboratório do slide 6]

**Slide 7 — Cadeia de custódia e *hash* SHA-256 (6:10–7:00)**
Fala: "A cadeia de custódia é a biografia da evidência. Para cada item, o formulário diz o que é, quem coletou, quando, como e onde ficou guardado, e registra cada vez que ele muda de mãos. Mídia física vai em embalagem com lacre numerado. A integridade vem do *hash* SHA-256, uma impressão digital de 256 bits: se um único bit do arquivo mudar, o valor muda inteiro. Calcula-se na coleta, confere-se em cada entrega, e a análise trabalha sempre em cópias."

**Slide 8 — Laboratório: cinco evidências, cinco *hashes* e uma entrega (7:00–8:50)**
Objetivo: comprovar que as evidências entregues à perita são as mesmas que foram coletadas.
Na tela (passo a passo do que clicar, na ordem):
1. Clicar em "▶ Próximo comando": `ls -l evidencias/`.
2. "▶ Próximo comando": `sha256sum evidencias/* | tee evidencias.sha256`.
3. "▶ Próximo comando": `column -s, -t cadeia_custodia.csv`.
4. "▶ Próximo comando" duas vezes: os dois `printf ... | sha256sum`.
5. "▶ Próximo comando": o `echo ... >> cadeia_custodia.csv`.
6. "▶ Próximo comando": `sha256sum -c evidencias.sha256`.
Fala: "Estamos na estação de Luiza, a NB-SOC-004. O `ls -l` lista as cinco evidências. Olhe a coluna de horário: 03h46 os voláteis, 03h58 a memória, 05h30 o disco, depois o *pcap* e os registros. É a ordem de volatilidade registrada pelo próprio sistema de arquivos. Repare também nas permissões, `-r--r-----`: os arquivos são só de leitura. O `sha256sum` calcula o *hash* de cada um, e o `tee` grava o resultado no arquivo `evidencias.sha256`, que acompanha o formulário. O `column` mostra o formulário de custódia como tabela: item, descrição, quem, quando, método e o *hash* abreviado. Agora um teste para você ver o *hash* trabalhando. Calculo o *hash* do texto INC-2026-1202-01 e depois o do mesmo texto terminando em 02. Só o último caractere mudou, e o valor é completamente outro. A transferência para a perita vira uma linha nova no formulário, com o `>>`, que acrescenta sem apagar nada. Por fim, a perita roda `sha256sum -c`, que recalcula cada *hash* e compara com o arquivo da coleta. Cinco vezes OK."
Atenção: os *hashes* das evidências são fictícios; os dois do teste com `printf` são os valores reais desses textos. Nenhum comando altera as evidências.
Conclusão: "Formulário conta a história; *hash* prova que nada mudou."
[Tela: gravação do laboratório do slide 8]

**Slide 9 — Linha do tempo e *super timeline* (8:50–9:40)**
Fala: "Com as evidências guardadas, a pergunta passa a ser 'em que ordem as coisas aconteceram?'. A linha do tempo junta os registros de várias fontes. A *super timeline* vai além e ordena todos os carimbos de tempo do disco e dos registros; a ferramenta livre mais usada é o plaso, com o comando `log2timeline`. Quatro cuidados: normalizar tudo para UTC, conferir os relógios, desconfiar de ordem impossível e marcar cada linha com a fonte. Na Rede Tatame, a VPN grava em UTC, o AD e o SOC em horário de Brasília e o *proxy* sem fuso nenhum."

**Slide 10 — Antes do código: onde achar e como instalar o que o laboratório usa (9:40–10:10)**
Fala: "Antes do código, veja o que o laboratório usa. VS Code e Python 3.12 vêm dos sites oficiais. Os módulos `csv`, `json`, `datetime` e `zoneinfo` já fazem parte do Python. O único pacote de terceiros é o `tzdata`, a base de fusos horários da IANA, mantida pela equipe do Python no PyPI. Ela é necessária no Windows; no Linux e no macOS o sistema já traz essa base, mas com o pacote o resultado é o mesmo em qualquer máquina. Confira o nome letra por letra antes de instalar."

**Slide 11 — Laboratório: seis fontes, uma linha do tempo (10:10–13:30)**
Objetivo: juntar seis fontes em uma linha do tempo em UTC e medir os intervalos do incidente.
Na tela (o VS Code ocupa o slide inteiro; o roteiro do laboratório abre e fecha com a tecla G ou com o botão "☰ Roteiro" da barra de status e deve ficar fechado durante a gravação):
1. No terminal, clicar em "⬇ Preparar o ambiente" e esperar o botão mudar para "✓ Ambiente pronto". Durante a instalação, o editor mostra o `requirements.txt`.
2. No explorador, abrir, na pasta `fontes`, `vpn_netguard.csv`, `ad_4624.json`, `edr_srv-erp-01.jsonl`, `proxy_dns.csv`, `sensor_conn.log` e `soc_casos.csv`, nessa ordem.
3. Abrir `linha_do_tempo.py` e parar na função `utc` (linhas destacadas 11 a 16).
4. Clicar em "▶ Montar a linha do tempo" (`python linha_do_tempo.py`).
5. Clicar em "▶ Sem o fuso (erro comum)" (`python linha_do_tempo.py --sem-fuso`).
6. Clicar em "▶ Calcular intervalos" (`python linha_do_tempo.py --intervalos`).
Fala (preparação): "O VS Code ocupa a tela inteira, como no meu computador. O `python3 --version` confirma o Python 3.12. O `python3 -m venv .venv` cria um ambiente virtual só para este caso, e o `activate` liga esse ambiente: repare no `(.venv)` no começo da linha. O `pip install -r requirements.txt` instala o que o arquivo aberto lista, o `tzdata` 2026.6; 'Successfully installed' confirma. O `pip list` mostra só o pip e o `tzdata`."
Fala (fontes): "Cada fonte tem o seu formato e o seu fuso. A VPN NetGuard é um CSV em UTC: o Z no fim do horário, 01:58:10Z, quer dizer UTC. Ela registra o *login* de `caio.mendes` a partir de 198.51.100.77, com o MFA aprovado na sexta solicitação, sinal de fadiga de MFA. O AD vem em JSON com o fuso escrito, -03:00: evento 4624, tipo 10, que é *logon* remoto por RDP, no SRV-ERP-01. O EDR também grava em UTC: a instalação do ConectaJá, o alerta da R8 e o isolamento. O *proxy* grava a hora local sem fuso: são 19 conexões, de cinco em cinco minutos. O sensor de rede segue o formato do Zeek, com o horário em segundos desde 1970, em UTC, a duração de 1.680 segundos e 2,8 bilhões de bytes enviados. E o sistema de casos do SOC registra a abertura do caso às 03h20."
Fala (código e execuções): "A função `utc` decide tudo. Ela lê o texto do horário, troca o Z por +00:00 e, se o horário não tiver fuso, aplica o fuso padrão da fonte, que aqui é America/Sao_Paulo. No fim, converte para UTC. Cada bloco seguinte lê uma fonte e põe na lista uma tupla com o instante em UTC, o nome da fonte e a descrição. As conexões do *proxy* são agrupadas em uma linha só, com o intervalo calculado. Depois, `eventos.sort()` ordena tudo pelo instante. Na primeira execução, veja as duas colunas de horário, Brasília e UTC: *login* às 22h58min10s, RDP às 23h06min42s, ConectaJá às 23h14min05s, alerta às 23h14min40s, conexões a partir das 02h10, a saída de 2,80 GB às 02h37, o caso às 03h20 e o isolamento às 03h41. Agora o erro comum. Com `--sem-fuso`, o programa lê o horário da VPN como se fosse local. O *login* pula para 01h58 do dia 2, depois do RDP e da instalação. É impossível acessar o servidor pela VPN antes de entrar na VPN, e o teste no fim do código, que compara o primeiro evento da VPN com o primeiro do AD, acusa: confira o fuso das fontes. Por fim, `--intervalos`: 8 minutos e 32 segundos do *login* ao RDP, 15 minutos e 55 segundos até a instalação, 4 horas, 5 minutos e 20 segundos de alerta parado até a triagem, MTTD de 4 horas, 21 minutos e 50 segundos, MTTR de 21 minutos, e a saída de 2,8 GB em 28 minutos, 1,67 MB por segundo."
Atenção: a preparação do ambiente é simulada e leva cerca de 10 segundos; espere o "✓ Ambiente pronto" antes das execuções. A saída mostrada é a que o código produz de verdade com esses arquivos. Na terceira execução, a primeira linha cinza resume as nove linhas da linha do tempo, que se repetem.
Conclusão: "A linha do tempo só vira prova quando todas as fontes falam o mesmo fuso."
[Tela: gravação do laboratório do slide 11]

**Slide 12 — Exemplo numérico: o que a linha do tempo mede (13:30–14:20)**
Fala: "Vamos ler os números com calma. Do *login* ao RDP, 8 minutos e 32 segundos: o invasor sabia aonde ir. O alerta da R8 tocou às 23h14min40s, mas a triagem só aconteceu às 03h20: 4 horas e 5 minutos de fila. O MTTD, do primeiro evento até o caso aberto, foi de 4 horas, 21 minutos e 50 segundos. O MTTR, do caso até a contenção, 21 minutos. E a saída de dados, 2,8 GB em 28 minutos, ou 1.680 segundos, dá cerca de 1,67 MB por segundo. A leitura que importa está no quadro azul: a saída inteira aconteceu enquanto o alerta esperava na fila. A resposta foi rápida; a triagem, não."

**Slide 13 — O tráfego também é evidência (14:20–15:00)**
Fala: "Falta uma fonte: a rede. O sensor da sede grava a captura completa, o *pcap*, por alguns dias, e registros de conexão no estilo do Zeek, por mais tempo. O Wireshark abre o *pcap* e filtra com filtros de exibição. Com TLS o conteúdo vem cifrado, mas os metadados contam quem falou com quem, quando, com que ritmo e quanto. Um *beacon* é a chamada periódica de um programa ao seu servidor de controle, e o intervalo fixo é a assinatura dele. E atenção: a fonte de saída de rede estava desligada no SIEM; só o sensor viu os 2,8 GB."

**Slide 14 — Laboratório: o *beacon* e os 2,8 GB no *pcap* do sensor (15:00–16:50)**
Objetivo: confirmar no tráfego o *beacon* e a saída de dados que o SIEM não viu.
Na tela (passo a passo do que clicar, na ordem):
1. Clicar em "1. Conversa com 198.51.100.77" e depois na linha 18230 para abrir os detalhes do pacote.
2. Clicar em "2. Só os Client Hello" e apontar a coluna "Delta" e a linha em vermelho, às 05:37:00.207.
3. Clicar em "3. tcp.stream eq 6" e clicar em uma linha "Application Data".
4. Clicar em "4. Statistics › Conversations" e apontar a linha em vermelho das duas tabelas.
Fala: "Este é o *pcap* do sensor aberto no Wireshark, com a hora em UTC. O primeiro filtro, `ip.addr == 198.51.100.77`, mostra toda a conversa com o endereço suspeito: 2.900.829 pacotes dos 4.812.337 da captura, como diz a barra de baixo. As primeiras linhas são um ciclo do *beacon*: SYN, SYN-ACK e ACK abrem a conexão, o Client Hello inicia o TLS, poucos pacotes de dados e o FIN fecha. Clicando em um pacote, o painel de detalhes mostra endereços e portas, que são legíveis. O segundo filtro fica só com os Client Hello, o primeiro pacote de cada sessão TLS. Acrescentei uma coluna Delta, o tempo desde o pacote anterior exibido: 300 segundos, 300, 300. Esse ritmo é o *beacon* do ConectaJá. A linha vermelha quebra o ritmo: às 05h37 em UTC, 02h37 em Brasília, abre-se o fluxo 6. O terceiro filtro, `tcp.stream eq 6`, isola esse fluxo: quase só pacotes cheios, de 1.514 bytes, saindo do 10.10.1.30, que é o SRV-ERP-01, até as 06h05 UTC, 1.680 segundos depois. Clique em um Application Data: o conteúdo é cifrado, não dá para ler, mas dá para saber quem mandou, para onde, quando e quanto. Por fim, Statistics, Conversations. Na aba IPv4, 2,93 GB de 10.10.1.30 para 198.51.100.77. Na aba TCP, o fluxo 6 sozinho tem 2,93 GB, e os outros fluxos do *beacon* têm 2,3 kB cada. Por que 2,93 e não 2,80? O Wireshark conta os quadros inteiros, com cabeçalhos; o registro do Zeek conta só os dados da aplicação."
Atenção: a lista de pacotes é ilustrativa e foi resumida com linhas de reticências. Os números de pacote seguem a ordem da captura, por isso saltam durante o fluxo 6. Nenhum conteúdo foi decifrado.
Conclusão: "O conteúdo é secreto, mas volume, destino e horário confirmam a linha do tempo."
[Tela: gravação do laboratório do slide 14]

**Slide 15 — Laboratório: plataforma Rede Tatame, o que o SIEM viu e o que só o sensor viu (16:50–18:30)**
Objetivo: ver, no simulador, quais passos do incidente deixaram registro no SIEM.
Na tela (passo a passo do que clicar, na ordem):
1. No seletor de velocidade, ao lado do relógio, escolher "1 s = 1 min".
2. Na aba "Cenários", clicar em "Iniciar cenário" no cartão "Acesso remoto não aprovado e saída de dados" e esperar os três passos da "Linha do tempo" (cerca de 10 segundos).
3. Ir à aba "SOC". Na linha da regra R8, host SRV-ERP-01, clicar em "Investigar" e ler o painel "Investigação"; depois clicar em "Conter".
4. Ir à aba "Arquitetura" e clicar na caixa "SRV-ERP-01".
Fala: "Agora o mesmo incidente na plataforma da disciplina. Ao abrir o slide, o simulador já vem com a R8 ligada, como no dia do incidente. Acelero o relógio e inicio o cenário. Na linha do tempo do cenário aparecem três passos com três desfechos. A instalação do ConectaJá: detectado, pela R8, com fonte EDR. As conexões periódicas: visto nos logs, sem alerta, porque a fonte de DNS e *proxy* está ligada, mas nenhuma regra olha para esse padrão. E o envio de 2,8 GB: não detectado, porque a fonte de *buckets* e saída de rede está desligada. Esse é o passo que só o sensor de rede viu. No SOC, o alerta da R8 está na fila. Pode aparecer também um alerta da R11 para o svc-backup: é a exceção documentada que já conhecemos, não faz parte do incidente. Em Investigar, o painel mostra a regra, o tempo até o alerta e a linha do tempo correlacionada, só com o passo que gerou sinal. Clico em Conter. Na Arquitetura, o SRV-ERP-01 aparece como isolado pelo SOC, e a telemetria dele, o EDR, continua chegando ao SIEM, exatamente como no isolamento sem desligar."
Atenção: os tempos de alerta, de MTTD e de MTTR do simulador variam a cada execução e correm no relógio simulado, que não é o do incidente. Não clique em "Conter" antes de os três passos aparecerem, porque a contenção interrompe o cenário. Para repetir do zero, use "Reiniciar".
Conclusão: "O SIEM viu um passo, viu outro sem alerta e não viu o terceiro. A lacuna foi preenchida pelo *pcap*."
[Tela: gravação do laboratório do slide 15]

**Slide 16 — De volta ao problema (18:30–19:20)**
Fala: "Voltemos à pergunta: como reconstruir o que aconteceu no SRV-ERP-01, em ordem e com provas que resistam a uma contestação? Primeiro, coletando na ordem certa: servidor isolado e ligado, voláteis e memória antes do disco. Segundo, provando a integridade: cinco *hashes* no formulário, lacre 0457 e cinco OK na entrega à perita. Terceiro, montando a linha do tempo com seis fontes em UTC, que mostra o *login* às 22h58 e o MTTD de 4 horas e 21 minutos. E quarto, fechando a lacuna do SIEM com o tráfego: 2,93 GB em 28 minutos para 198.51.100.77. Essa linha do tempo é a matéria-prima da Aula 15, em que as técnicas do incidente serão emuladas para testar a detecção."

**Slide 17 — Pontos-chave (19:20–19:40)**
Fala: "Para levar desta aula: memória antes do disco, como manda a RFC 3227; isolar em vez de desligar; cadeia de custódia e *hash* SHA-256; tudo em UTC na linha do tempo; e o tráfego de rede preenchendo as lacunas do SIEM."

**Slides 18 e 19 — Referências e encerramento (19:40–20:00)**
Fala: "As referências estão no slide, com destaque para a RFC 3227 e para o livro de Richard Bejtlich, da bibliografia da disciplina. Na Aula 15, Red e Blue vão sentar juntos para emular as técnicas deste incidente e provar que a detecção agora funciona. Até lá!"
[Tela: slide de encerramento por 5 segundos]

## Roteiro da Videoaula 15 — "Temos a regra. Mas ela dispara?"

Duração-alvo: 15 a 20 minutos. Deck: unidade_4/slides/aula15.html (19 slides).

**Slides 1 e 2 — Capa e sumário (0:00–0:40)**
Fala: "Olá! Bem-vindo à Aula 15. Hoje o tema é o exercício *purple team*: como validar, técnica por técnica, se as detecções funcionam contra técnicas emuladas. Vamos continuar na Rede Tatame, logo depois do incidente que estudamos nas Aulas 13 e 14. No sumário você vê o caminho: o ciclo emular, observar, ajustar e retestar, o plano de emulação, cinco laboratórios, com terminal, código, a matriz do ATT&CK Navigator e o simulador da disciplina, e no fim os formatos complementares: *tabletop*, *cyber range* e CTF."
[Tela: capa; parar 5 segundos no sumário]

**Slide 3 — O problema de hoje na Rede Tatame (0:40–2:00)**
Fala: "Lembra do incidente INC-2026-1202-01? Dois passos do invasor passaram sem alerta. O RDP para o SRV-ERP-01, porque a regra R5 estava desligada, e a saída de 2,8 GB, porque a fonte de saída de rede nem chegava ao SIEM. Na reunião de lições aprendidas, em 9 de dezembro, a CISO Marina Prado fez uma pergunta incômoda: das regras que dizemos ter, quantas disparariam de verdade contra o mesmo adversário? Ninguém soube responder com números. No mapa à direita, o caminho em destaque é o do incidente: internet, VPN, AD e o SRV-ERP-01, em vermelho. Em destaque também o CEP e o SIEM, que precisam provar que veem cada passo. A pergunta da aula é esta: como provar, técnica por técnica, que as detecções da Rede Tatame funcionam contra o que o incidente e o Grupo Cobalto Austral fazem? Guarde os papéis: Bruno Sato no Red Team, Luiza Ferraz no Blue Team, Rafael Tavares como facilitador, Caio Mendes pela TI e Marina Prado, que autoriza."
[Take de apoio: reunião diante de um painel de alertas — Envato]

**Slide 4 — Exercício *purple* e operação de Red Team (2:00–3:00)**
Fala: "Olhe a tabela. Na operação de Red Team tradicional, o Blue Team normalmente não sabe do teste, porque o que se avalia é a reação a um ataque realista, e o resultado chega semanas depois em um relatório. No exercício *purple*, o Blue Team sabe o que será executado e quando, e cada técnica é avaliada na hora: telemetria, alerta e resposta. O ritmo é de horas, e o ajuste acontece na própria sessão. O *Purple Team Exercise Framework*, o PTEF, publicado pela SCYTHE, descreve essa sessão colaborativa e dá destaque a um papel: o facilitador, que controla o tempo e garante que cada discussão termine em tarefa com dono e prazo."

**Slide 5 — Emular, observar, ajustar e retestar (3:00–4:00)**
Fala: "Cada técnica percorre quatro passos. Emular: o Red Team executa um caso de teste inofensivo, dentro da autorização, e avisa no canal da sessão. Observar: o Blue Team confere o critério de sucesso que foi combinado antes. O evento chegou? A regra disparou? Chegou a tempo, por exemplo em até 5 minutos? E o analista abriu o caso e seguiu o *playbook*? Ajustar: ligar a fonte, criar ou corrigir a regra, documentar uma exceção. Retestar: repetir exatamente o mesmo caso de teste. Repare no destaque em azul: regra ligada e nunca retestada é uma hipótese."

**Slide 6 — Laboratório: uma técnica do incidente percorre o ciclo (4:00–5:40)**
Objetivo: mostrar, com o RDP que passou sem alerta no incidente, como uma técnica sai de hipótese e vira detecção comprovada.
Na tela:
1. O diagrama abre no passo "Antes · O que o incidente mostrou" (contador "1 / 6"). Apontar o nó central "T1021.001", com o subtítulo "hipótese", e ler o texto na barra abaixo.
2. Clicar em "▶ Avançar" (passo "1 · Emular").
3. Clicar em "▶ Avançar" (passo "2 · Observar") e apontar o nó central, que muda para "parcial: sem alerta".
4. Clicar em "▶ Avançar" (passo "3 · Ajustar").
5. Clicar em "▶ Avançar" (passo "4 · Retestar") e apontar o nó central, que passa a "detecção comprovada".
6. Clicar em "▶ Avançar" uma última vez ("O ciclo recomeça"); o botão fica desativado.
Fala: "Vamos seguir a T1021.001, uso de RDP de uma estação para um servidor. No incidente, às 23:06:42 de 1º de dezembro, o logon remoto ficou registrado no AD, mas nada alertou. Por isso ela entra no plano com um critério claro: o evento 4624 tipo 10 no tópico tatame.auditoria e o alerta da R5 em até 5 minutos. Na emulação, às 14:32:40 do dia 10, Bruno Sato avisa no canal e abre uma sessão RDP do NB-TI-012 para o SRV-ERP-01 com a conta de teste svc-purple. Nada é lido nem alterado. Na observação, a telemetria chega às 14:32:52, mas o alerta não, porque a R5 continua desligada. Resultado: parcial. No ajuste, Rafael liga a R5 com uma exceção documentada para o servidor de salto que a equipe de Caio Mendes usa na manutenção, para não gerar ruído. No reteste, às 15:02:13, o mesmo caso é repetido e o alerta chega à fila de Luiza às 15:02:51: 38 segundos, dentro do critério. Ela abre o caso e segue o *playbook*. Só agora a detecção está comprovada."
Atenção: o modo "⏯ Auto" avança sozinho; para gravar, prefira "▶ Avançar" e espere a animação dos pacotes antes do próximo clique. O texto de cada passo aparece na barra abaixo do diagrama.
Conclusão: "A técnica só conta como coberta depois do reteste. Esse é o primeiro pedaço da resposta à pergunta da aula."
[Tela: gravação do laboratório do slide 6]

**Slide 7 — Plano de emulação e casos de teste inofensivos (5:40–6:40)**
Fala: "Quais técnicas entram na sessão? Aqui vale a diferença entre emulação e simulação. Emulação reproduz o comportamento de um adversário específico, conhecido por inteligência de ameaças; simulação executa técnicas genéricas. O nosso plano junta as técnicas do incidente e as do Grupo Cobalto Austral. Três recursos públicos ajudam: a *Adversary Emulation Library*, do MITRE Center for Threat-Informed Defense, com planos de grupos documentados; o Atomic Red Team, da Red Canary, com testes pequenos mapeados a técnicas ATT&CK; e o Apache Caldera, criado pela MITRE e hoje em incubação na Apache Software Foundation, que automatiza a execução. E cada caso de teste é inofensivo: conta de teste, dados sintéticos, máquina descartável, sempre dentro da autorização APR-3107. Ele deixa o mesmo rastro da técnica, sem causar o dano."
[Take de apoio: páginas públicas do Atomic Red Team e da Adversary Emulation Library]

**Slide 8 — Laboratório: o executor da sessão de 10/12 (6:40–8:50)**
Objetivo: ver a sessão rodar com segurança e registrar, caso a caso, o que o SOC observou.
Na tela:
1. Clicar em "▶ Próximo comando": `purple-runner verificar-roe --autorizacao APR-3107`.
2. "▶ Próximo comando": `purple-runner listar --plano plano/validacao-2026-12-10.yaml`.
3. "▶ Próximo comando": `purple-runner executar T1021.001-01`.
4. "▶ Próximo comando": `purple-runner retestar T1021.001-01`.
5. "▶ Próximo comando": `purple-runner executar T1567.002-01`.
6. "▶ Próximo comando": `purple-runner retestar T1567.002-01`.
7. "▶ Próximo comando": `purple-runner relatorio --sessao 2026-12-10`.
Fala: "Este terminal mostra o executor da sessão, um programa fictício chamado `purple-runner`. O primeiro comando confere as regras de engajamento: a APR-3107 está válida e assinada por Marina Prado, o escopo é a sede, 10.10.0.0/16, com a conta svc-purple, e a linha amarela lembra o que fica fora: a rede de pagamentos e a API do parceiro. A janela vai das 14h às 18h e os observadores do SOC estão conectados. Nada roda sem isso. O segundo comando lista os seis casos: cada linha tem a tática, a regra esperada e o teste inofensivo, e o rodapé lembra o critério, alerta em até 300 segundos. Agora a T1021.001: telemetria às 14:32:52, nenhum alerta, status parcial. No reteste, com a R5 ligada, o alerta chega às 15:02:51, em 38 segundos: detectado. A T1567.002 é mais instrutiva. Na primeira execução, nenhum evento de saída de rede: sem visibilidade. Rafael liga a fonte e a R9, e o caso é repetido. A telemetria chega às 16:10:31, e o alerta também vem, mas às 16:19:00: 540 segundos, acima do limite. Por quê? Porque a R9 soma bytes em uma janela de uma hora e só passa de 1 GB perto do fim do envio. Status: parcial, com a ação de reduzir a janela, dono Rafael Tavares e prazo 17 de dezembro. O relatório final resume: seis técnicas, três detectadas na primeira execução, cinco depois do reteste e telemetria em todas as seis."
Atenção: o executor e as saídas são ilustrativos; nenhum comando executa ataque. Os casos de teste são catalogados e usam só dados sintéticos. Os comandos aparecem fora da ordem cronológica de propósito: primeiro o ciclo completo da T1021.001, depois o da T1567.002.
Conclusão: "Alerta fora do tempo combinado ainda não é detecção comprovada."
[Tela: gravação do laboratório do slide 8]

**Slide 9 — Antes do código: onde achar e como instalar o que o laboratório usa (8:50–9:20)**
Fala: "Antes do código, veja o que o laboratório usa e de onde vem. O Visual Studio Code e o Python 3.12 saem dos sites oficiais. O único pacote de terceiros é o PyYAML, que lê o plano em YAML; no PyPI, confira o nome letra por letra e se o *link* 'Source Code' leva ao repositório oficial. Os módulos `csv`, `json`, `statistics` e `sys` já vêm com o Python. E o ATT&CK Navigator roda no navegador, no endereço da própria MITRE: use esse, porque as *layers* mostram exatamente o que a Rede Tatame ainda não detecta."

**Slide 10 — Laboratório: do resultado da sessão às *layers* do Navigator (9:20–12:20)**
Objetivo: transformar o resultado da sessão em cobertura testada e visibilidade, antes e depois do reteste, e gravar as *layers* do Navigator.
Na tela (o VS Code ocupa o slide inteiro; o roteiro do laboratório abre e fecha com a tecla G ou com o botão "☰ Roteiro" da barra de status e deve ficar fechado durante a gravação):
1. Esperar o editor terminar de digitar o `validacao-2026-12-10.yaml`, que abre sozinho ao entrar no slide.
2. No terminal, clicar em "⬇ Preparar o ambiente" e esperar o botão mudar para "✓ Ambiente pronto". Durante a instalação, o editor mostra o `requirements.txt`.
3. No explorador, clicar em `sessao-2026-12-10.csv`, na pasta `resultados`.
4. Clicar em `gerar_layer.py` e parar na função `status` (linhas destacadas).
5. No terminal, clicar em "▶ Layer antes do reteste" (`python gerar_layer.py`).
6. Clicar em "▶ Layer depois do reteste" (`python gerar_layer.py --reteste`); o editor abre `layers/validacao-depois.json`.
Fala (preparação): "O VS Code agora ocupa a tela inteira, como no meu computador. Antes de rodar, preparo o ambiente. O `python3 --version` confirma o interpretador, Python 3.12.7. O `python3 -m venv .venv` cria um ambiente virtual, uma instalação separada só para este projeto, e o `activate` liga esse ambiente: repare no `(.venv)` no início da linha. O `pip install -r requirements.txt` instala o que o arquivo aberto lista, o PyYAML 6.0.3; 'Downloading' mostra o arquivo que veio do PyPI e 'Successfully installed' confirma. O `pip list` mostra o resultado: só o pip e o PyYAML."
Fala (arquivos e execuções): "Primeiro o plano. No topo, a origem, as lições aprendidas do incidente e o Cobalto Austral, e a autorização APR-3107. A linha destacada é o critério: `alerta_em_ate_s: 300`, cinco minutos. Depois vêm as seis técnicas, cada uma com tática, regra esperada e teste inofensivo. O CSV guarda o que a sessão observou. A coluna `alerta_s` é o tempo até o alerta na primeira execução; vazia quer dizer sem alerta. A `reteste_s` é o tempo no reteste. Veja a T1567.002: telemetria 'nao', sem alerta, e 540 no reteste. Agora o código. A função `status` decide tudo. A primeira linha escolhe o tempo: no modo `--reteste`, usa o do reteste quando existe. Se há tempo e ele é menor ou igual ao limite, a técnica é 'detectado'. Se há alerta fora do limite, ou só telemetria, é 'parcial'. Sem nada, 'sem_visibilidade'. Cada estado vira uma cor e uma pontuação: 100, 50 ou 0. No fim, a cobertura testada conta as técnicas com 100, e a visibilidade, as com 50 ou mais. Rodo a primeira: T1078, T1219 e T1490 detectadas; T1087.002 e T1021.001 parciais; T1567.002 sem visibilidade. Cobertura testada de 3 em 6, 50%, e visibilidade de 5 em 6, 83%. O tempo médio até o alerta é 46 segundos, a média de 41, 35 e 63. Agora com `--reteste`: a T1087.002 e a T1021.001 viram detectadas, e a T1567.002 sobe para parcial, porque 540 passa do limite. Cobertura testada de 5 em 6, 83%, e visibilidade de 6 em 6, 100%. O tempo médio continua em 46 segundos: agora são cinco alertas, 41, 52, 38, 35 e 63, que somam 229. O JSON aberto é a *layer* no formato do Navigator: nome, versões, domínio `enterprise-attack` e, para cada técnica, `techniqueID`, `score`, `color` e `comment`."
Atenção: a preparação do ambiente é simulada e leva cerca de 10 segundos; espere o "✓ Ambiente pronto" antes de clicar nas execuções. A digitação automática do plano leva alguns segundos; espere terminar. A saída mostrada é a mesma que o script produz quando executado com esses arquivos.
Conclusão: "O plano diz o que testar; a *layer* mostra o que foi comprovado, com o critério de tempo aplicado."
[Tela: gravação do laboratório do slide 10]

**Slide 11 — Laboratório: a matriz antes e depois do reteste (12:20–13:40)**
Objetivo: ler as duas *layers* como a diretoria vai vê-las, na forma da matriz.
Na tela:
1. Com o botão "Antes" selecionado, apontar as cores e os três indicadores da base: 3/6 = 50%, 5/6 = 83% e 3 pendentes.
2. Clicar em "Depois do reteste" e apontar as três células que mudam de cor.
3. Clicar na célula T1567.002 e ler o comentário que aparece abaixo da matriz.
4. Clicar em uma célula cinza, por exemplo T1486, e ler o comentário.
Fala: "Esta é a matriz no formato do Navigator, com as táticas nas colunas. Verde é score 100, detectado dentro do critério; amarelo é 50, parcial; vermelho é 0, sem visibilidade. Antes do reteste, três verdes, dois amarelos e o vermelho da exfiltração. Depois, a descoberta de contas e o RDP ficam verdes, e a T1567.002 sai do vermelho para o amarelo. O comentário explica: alerta em 540 segundos, acima dos 300, com ação pendente para Rafael até 17 de dezembro. As células cinzas são técnicas que ficaram fora deste plano. Elas não têm pontuação e não entram no denominador. Por isso os indicadores são sempre sobre seis técnicas: cobertura de 83% e visibilidade de 100%, com uma pendência."
Atenção: os indicadores da base mudam junto com o botão; dê um segundo para a transição de cor.
Conclusão: "Cobertura vale para as técnicas priorizadas, e não para a matriz inteira."
[Tela: gravação do laboratório do slide 11]

**Slide 12 — Laboratório: plataforma Rede Tatame, o reteste do Cobalto Austral (13:40–15:50)**
Objetivo: repetir o ciclo no simulador da disciplina e ver a diferença entre técnica detectável e técnica comprovada.
Na tela:
1. Na aba "Cobertura ATT&CK", apontar os indicadores: "Comprovadas" 0, "Detectáveis sem teste" 7 e "Cobertura com regra" 44%.
2. No seletor de velocidade, ao lado do relógio, escolher "1 s = 1 min".
3. Ir à aba "Cenários" e clicar em "Iniciar cenário" no cartão "Emulação do Grupo Cobalto Austral". Esperar os 8 passos (cerca de 20 segundos): "Detectados" 3, "Não detectados" 2, "Vistos sem alerta" 3.
4. Voltar a "Cobertura ATT&CK": "Comprovadas" 3; a cobertura com regra continua em 44%.
5. Na aba "Regras do CEP", marcar R5, R13 e R9. Na aba "Telemetria", marcar "Acesso a buckets e saída de rede".
6. Voltar a "Cobertura ATT&CK": "Cobertura com regra" 63%, mas "Comprovadas" continua 3.
7. Em "Cenários", clicar em "Repetir com as fontes e regras atuais" e esperar os 8 passos: "Detectados" 7, "Não detectados" 1.
8. Abrir "Cobertura ATT&CK" mais uma vez: "Comprovadas" 6.
Fala: "Agora o mesmo raciocínio na plataforma da disciplina. A aba Cobertura lista as 16 técnicas de todos os cenários, com quatro estados: comprovada, com regra ativa e já testada; detectável, com regra e fonte, mas sem teste; parcial, com telemetria e sem regra; e cega. O simulador abre com a R8 ligada, como ficou depois do incidente. Repare: nenhuma técnica está comprovada. Rodo a emulação do Cobalto Austral com o relógio acelerado. Na linha do tempo, três passos alertam: o login sem MFA, o acesso ao LSASS e a exclusão de cópias de sombra. Três são vistos sem alerta e dois passam despercebidos. Na Cobertura, as comprovadas sobem para 3. Agora ligo a R5, a R13 e a R9, e a fonte de saída de rede. Olhe o que acontece: a cobertura com regra salta para 63% na hora, sem nenhum teste. É o número que impressiona, mas ainda é hipótese. Só quando repito o cenário com as fontes e regras atuais, e os novos passos alertam de verdade, as comprovadas vão a 6. O único passo não detectado no reteste é o impacto, a criptografia, que não tem regra no simulador."
Atenção: não clique em "Conter" no SOC durante a gravação, porque conter interrompe o cenário. Se algo sair da ordem, use "Reiniciar" no topo e recomece do passo 1 (a R8 volta ao padrão; para religá-la, saia e volte a este slide). Os números do simulador (16 técnicas de todos os cenários) são diferentes dos da sessão de 10/12 (6 técnicas do plano); explique isso ao aluno. A plataforma é simulada e não toca sistema real.
Conclusão: "Ligar a regra muda a cobertura com regra; só o reteste muda o número de comprovadas."
[Tela: gravação do laboratório do slide 12]

**Slide 13 — Exemplo numérico: a sessão de 10/12 em números (15:50–16:40)**
Fala: "Vamos consolidar. Cobertura testada: 3 de 6 antes do reteste, 50%; 5 de 6 depois, cerca de 83%. Visibilidade: 5 de 6, cerca de 83%, e depois 6 de 6, 100%. O tempo médio até o alerta ficou em 46 segundos nos dois casos. Foram três ações de melhoria: duas retestadas e concluídas e uma pendente, a T1567.002, com dono e prazo. Repare no destaque: ela já tem telemetria e alerta, mas o alerta chegou depois do limite. Por isso conta na visibilidade e não na cobertura testada. Guarde esses números: eles vão para o relatório final da Aula 16."

**Slide 14 — *Tabletop*, *cyber range* e CTF (16:40–17:30)**
Fala: "O exercício *purple* valida a detecção, mas não testa tudo. O *tabletop* reúne técnicos, jurídico, comunicação e diretoria para discutir um cenário em etapas, com *injects* que forçam decisões: quem isola o servidor, quem fala com a ANPD. A CISA oferece pacotes gratuitos, e o NIST SP 800-84 orienta o planejamento. O *cyber range* é uma rede virtual realista e isolada, para treinar a operação técnica sem tocar a produção, como no Locked Shields, da OTAN, ou no Exercício Guardião Cibernético, no Brasil. E o CTF desenvolve habilidades técnicas em desafios com bandeiras, como o picoCTF. Um programa maduro alterna os três."
[Take de apoio: sala de reunião em exercício de crise — Envato]

**Slide 15 — Pausa para reflexão (17:30–18:10)**
Fala: "Agora é com você. Uma rede de clínicas mostra à diretoria 92% da matriz 'coberta', porque há uma regra para cada técnica, mas nenhuma foi retestada no último ano. Na semana passada, um *ransomware* usou RDP entre servidores sem alerta, embora a regra existisse. Que número a diretoria está vendo de verdade? Monte um plano de validação com cinco técnicas e o critério de cada uma, e pense em um *inject* de *tabletop* sobre isolar um servidor em produção. O desafio é escrever a *layer* 'antes' em JSON, no formato que usamos hoje. Pause o vídeo e tente."

**Slide 16 — De volta ao problema (18:10–18:55)**
Fala: "Voltemos à pergunta de Marina Prado. Seis casos de teste inofensivos, com a conta svc-purple e dentro da APR-3107. Para cada um, telemetria, alerta em até 300 segundos e a resposta do SOC. A R13 e a R5 foram ligadas e retestadas, e a fonte de saída ganhou telemetria: a cobertura testada foi de 50% para 83%. A T1567.002 ficou registrada, em amarelo, com dono e prazo. Então, como provar que as detecções funcionam? Com um exercício *purple* que emula cada técnica, observa telemetria, alerta, tempo e resposta, ajusta o que falhou e retesta. Só o que passou no reteste, dentro do critério, conta como detecção comprovada."

**Slide 17 — Pontos-chave (18:55–19:20)**
Fala: "Para levar desta aula: o exercício *purple* é transparente e mede técnica a técnica. O ciclo só se completa com o reteste. Casos de teste são inofensivos, autorizados e mapeados ao ATT&CK. Cobertura testada e visibilidade são números diferentes, e as *layers* mostram os dois. E *tabletop*, *cyber range* e CTF complementam a validação técnica."

**Slides 18 e 19 — Referências e encerramento (19:20–19:50)**
Fala: "As referências estão no slide, com destaque para o PTEF, o Atomic Red Team e o ATT&CK Navigator. Na próxima aula, a última da disciplina, vamos transformar o incidente e este exercício em um relatório final: achados, riscos, recomendações e métricas de melhoria. Até lá!"
[Tela: slide de encerramento por 5 segundos]

## Roteiro da Videoaula 16 — "Uma página para a diretoria: o que entra e o que fica de fora?"

Duração-alvo: 15 a 20 minutos. Deck: unidade_4/slides/aula16.html (19 slides).

**Slides 1 e 2 — Capa e sumário (0:00–0:35)**
Fala: "Olá! Esta é a Videoaula 16, a última da disciplina. Hoje vamos escrever o relatório final: achados, riscos, recomendações e métricas de melhoria. No sumário você vê o caminho: o problema da Rede Tatame, o relatório técnico e o executivo, a matriz de risco, a priorização, as métricas e cinco laboratórios. No fim, olhamos juntos para o percurso das quatro unidades."
[Tela: capa; parar 5 segundos no sumário]

**Slide 3 — O problema de hoje na Rede Tatame (0:35–1:45)**
Fala: "Foram quinze dias intensos na Rede Tatame, a nossa rede fictícia de academias. Em 1º de dezembro aconteceu o incidente INC-2026-1202-01, que acompanhamos nas Aulas 13 e 14: um acesso remoto não aprovado no SRV-ERP-01 e 2,8 GB de planilhas de cobrança enviados para fora. Em 10 de dezembro, o exercício *purple* da Aula 15 retestou as detecções. Agora, em 16 de dezembro, a CISO Marina Prado precisa levar tudo isso à diretoria. São oito achados, dois já corrigidos e retestados, e a diretoria pediu uma página. A pergunta da aula está no quadro amarelo: como transformar o incidente e o exercício em um relatório que leve a diretoria a decidir e que permita medir a melhoria? No mini-mapa à direita, o caminho em destaque é o do incidente, da internet à VPN e daí ao SRV-ERP-01, em vermelho. Guarde os papéis: Marina apresenta, Rafael Tavares consolida os achados, Luiza Ferraz traz os números do SOC e a diretoria decide."
[Take de apoio: executiva entrando em sala de reunião com um documento de uma página — Envato, "boardroom presentation"]

**Slide 4 — Um relatório, dois públicos (1:45–2:40)**
Fala: "O primeiro cuidado é lembrar que o relatório tem dois leitores. Olhe a tabela. O relatório técnico é para o SOC, a engenharia de detecção, a TI e a auditoria, e responde 'o que aconteceu, com que evidência, e o que corrigir?'. Ele tem a linha do tempo, os achados e as recomendações, com o tamanho que for preciso. O sumário executivo é para a diretoria e responde 'quanto risco corremos e o que decidimos agora?', em uma página. Repare na frase do quadro azul: o sumário vem primeiro no documento, mas é escrito por último, depois que os achados estão fechados."

**Slide 5 — Anatomia de um achado: o A-03 (2:40–3:40)**
Fala: "O achado é a unidade do relatório técnico. Vamos ler um, o A-03, campo por campo. O título resume o problema: saída de dados sem telemetria nem regra. A evidência diz o que, quando e onde: 2,8 GB do SRV-ERP-01 para o endereço 198.51.100.77, entre 2h37 e 3h05, vistos só no *pcap* do sensor, que analisamos na Aula 14. A técnica ATT&CK é a T1567.002, e é ela que liga o achado à cobertura e ao próximo exercício. O impacto são as planilhas de 9.400 alunos e responsáveis, com comunicação à ANPD. O risco é 3 vezes 5, 15, crítico. A recomendação tem dono e prazo, e o último campo, que muita gente esquece, é o critério de reteste: como saberemos que está resolvido. Aqui, alerta da R9 em até 300 segundos. No exercício de 10 de dezembro a fonte e a regra já estavam ligadas e a R9 alertou, mas em 540 segundos. Por isso o achado continua aberto, agora com a recomendação de reduzir a janela da regra até 17 de dezembro."

**Slide 6 — Matriz de risco: probabilidade × impacto (3:40–4:35)**
Fala: "Para comparar achados tão diferentes quanto um MFA fraco e um CPF numa planilha, usamos a matriz de probabilidade e impacto, a mesma ideia do guia NIST SP 800-30 e da ISO 31000. A probabilidade vai de 1 a 5 e considera exposição, facilidade e o que a inteligência de ameaças mostra. O impacto vai de 1 a 5 e pesa mais quando há dados de menores, saúde, biometria ou pagamento. O risco é o produto, de 1 a 25. Na Rede Tatame, 15 ou mais é crítico; de 10 a 14, alto; de 5 a 9, médio; abaixo disso, baixo. Como a escala depende de julgamento, o relatório registra quem pontuou e por quê. E note o quadro azul: o CVSS mede a falha; o risco mede a falha naquele ambiente."

**Slide 7 — Laboratório: os oito achados do RPT-2026-12 na matriz (4:35–6:15)**
Objetivo: ver onde cada achado cai na matriz e quantos são críticos.
Na tela:
1. Apontar a grade: linhas de probabilidade (5 no alto) e colunas de impacto (1 a 5), com as zonas verde, amarela, laranja e vermelha.
2. Clicar em "A-01" e ler a caixa de detalhes.
3. Clicar em "A-03" e depois em "A-07".
4. Clicar em "Todos os achados" e apontar os quatro indicadores abaixo da caixa.
5. Clicar em "Só os abertos".
Fala: "Cada célula da grade é uma combinação de probabilidade e impacto, e a cor já mostra a classe. Clico no A-01: a VPN aceita MFA por *push* sem correspondência de número. Foi assim que o invasor entrou, insistindo até alguém aprovar. Probabilidade 4, impacto 5, risco 20, crítico. O número 01 aparece na linha 4, coluna 5. O A-03, que acabamos de ler, cai em 3 por 5, 15, ainda na zona vermelha. O A-07, CPF completo nas planilhas de cobrança, fica em 2 por 4, 8, médio. Agora 'Todos os achados': quatro críticos, dois altos, dois médios. Os números riscados são o A-05 e o A-08, o RDP sem alerta e a consulta em massa ao AD, que o exercício de 10 de dezembro corrigiu e retestou; o indicador Retestados mostra 2. Em 'Só os abertos' ficam seis: quatro críticos, um alto e um médio. Esta é a lista que vai à decisão."
Atenção: a matriz é um registro estático do relatório; os valores de probabilidade e impacto foram atribuídos pela equipe e são fictícios. Clique em um achado de cada vez e espere a caixa de detalhes atualizar.
Conclusão: "A matriz mostra para onde olhar primeiro, mas ainda não diz o que fazer primeiro. Esse é o próximo passo."
[Tela: gravação do laboratório do slide 7]

**Slide 8 — Priorizar por risco e por esforço (6:15–7:05)**
Fala: "Risco alto diz onde está o perigo; o esforço diz quanto custa resolver. Damos a cada recomendação um esforço de 1 a 3: dias, semanas ou meses. Uma ordem simples é prioridade igual a risco dividido por esforço. Os ganhos rápidos, os *quick wins*, são os de risco 10 ou mais com esforço 1, e entram já na semana seguinte. O que exige projeto, como segmentar a rede da sede, vai para o *roadmap*. E aqui está um ponto que separa relatório de lista de desejos: até a correção sair, a diretoria aceita formalmente o risco residual, por escrito, ou aprova uma medida provisória. Toda recomendação tem dono, prazo e critério de reteste; sem dono, vira opinião."

**Slide 9 — Antes do código: onde achar e como instalar o que o laboratório usa (7:05–7:35)**
Fala: "Antes do código, a lista do que o laboratório usa e de onde vem. O Visual Studio Code e a extensão Python da Microsoft, o Python 3.12 do site oficial e um único pacote de terceiros, o PyYAML, no PyPI, que lê o arquivo de metas. Os módulos `csv` e `datetime` vêm com o Python. Ao procurar o pacote no PyPI, confira o nome letra por letra e o *link* para o repositório oficial. E fixe a versão no `requirements.txt`: os números que vão à diretoria precisam sair iguais se alguém rodar o script daqui a um ano."

**Slide 10 — Laboratório: priorizar os achados e medir a melhoria (7:35–10:40)**
Objetivo: gerar a ordem das recomendações e os indicadores que vão ao sumário executivo.
Na tela (o VS Code ocupa o slide inteiro; o roteiro do laboratório abre e fecha com a tecla G ou com o botão "☰ Roteiro" da barra de status e deve ficar fechado durante a gravação):
1. No terminal, clicar em "Preparar o ambiente" e esperar o botão mudar para "Ambiente pronto". Durante a instalação, o editor mostra o `requirements.txt`.
2. No explorador, clicar em `achados.csv` e apontar as linhas destacadas do A-01 e do A-04.
3. Clicar em `metas.yaml` e apontar o bloco `marcos`, destacado.
4. Clicar em `priorizar.py` e parar nas linhas destacadas do cálculo de risco e de prioridade.
5. No terminal, clicar em "Priorizar achados" (o comando executado é `python priorizar.py`).
6. Clicar em "Indicadores de melhoria" (`python priorizar.py --metricas`).
Fala (preparação): "O VS Code agora ocupa a tela inteira, como no meu computador. Antes de rodar, preparo o ambiente. O `python3 --version` confirma o interpretador, Python 3.12.7. O `python3 -m venv .venv` cria um ambiente virtual, uma instalação separada só para este projeto, e o `activate` liga esse ambiente: repare no `(.venv)` no início da linha. O `pip install -r requirements.txt` instala o que o arquivo aberto lista, o PyYAML 6.0.3: a linha 'Downloading' mostra o arquivo que veio do PyPI e 'Successfully installed' confirma. O `pip list` mostra o resultado: só o pip e o PyYAML."
Fala (arquivos e execuções): "O `achados.csv` é o relatório técnico em forma de tabela: uma linha por achado, com técnica, probabilidade, impacto, esforço, dono, prazo e estado. Os dois com estado 'retestado' foram corrigidos e passaram no reteste do exercício *purple*. O `metas.yaml` guarda as regras do relatório. Primeiro os limites das classes: crítico a partir de 15, alto a partir de 10. Depois os marcos do incidente, que definem as métricas: o primeiro evento às 22h58min10s, o alerta da R8 às 23h14min40s, o caso aberto por Luiza às 3h20 e a contenção às 3h41. Em seguida as metas em minutos e o estado das seis técnicas do exercício *purple* antes e depois do reteste. Agora o código. A função `achados` lê o CSV, e duas linhas decidem tudo: `risco` é probabilidade vezes impacto, e `prioridade` é risco dividido por esforço. A função `priorizar` separa só os abertos e ordena pela prioridade, do maior para o menor; em caso de empate, vence o risco maior. Rodo 'Priorizar achados'. A saída mostra A-01 com prioridade 20, A-02 com 16, e A-03 e A-04 com 15, os quatro com esforço 1: são os ganhos rápidos que a linha verde lista. Entre A-03 e A-04 há empate completo, e a ordem do arquivo se mantém. O A-06 tem risco 12, alto, mas esforço 3, e cai para prioridade 4; o A-07 também fica com 4, e o desempate pelo risco o põe por último. A última linha resume: oito achados, quatro críticos, dois altos, dois médios, dois já retestados. Agora 'Indicadores de melhoria'. A função `minutos` subtrai dois marcos do YAML. O MTTD, do primeiro evento até o caso aberto, dá 4 h 21 min 50 s, fora da meta de 60 minutos. O tempo entre o alerta e a abertura do caso dá 4 h 05 min 20 s: o alerta existia, mas esperou na fila do plantão. Isso é o achado A-02. O MTTR, da abertura até a contenção, dá 21 minutos, dentro da meta. Depois vêm os números do exercício *purple*: a cobertura testada das seis técnicas vai de 3 em 6, 50%, para 5 em 6, 83%, e a visibilidade de 83% para 100%. A T1567.002 agora tem telemetria e alerta, mas fora do critério, por isso conta como parcial. Por fim, das seis ações da reunião de lições aprendidas, três foram concluídas no prazo, 50%, e duas dessas três passaram no reteste, 67%."
Atenção: a preparação do ambiente é simulada e leva cerca de 10 segundos; espere o botão mostrar "Ambiente pronto" antes de executar. Os dados são fictícios, mas o código é real e produz exatamente essa saída com o Python 3.12. As classes aparecem sem acento ("critico", "medio") porque são chaves do YAML.
Conclusão: "A conta fica no código e as premissas no YAML. Qualquer pessoa refaz os números, e é isso que dá credibilidade ao relatório."
[Tela: gravação do laboratório do slide 10]

**Slide 11 — Poucos números, cada um com meta e dono (10:40–11:35)**
Fala: "Vamos organizar as métricas que acabaram de sair. O MTTD vai do primeiro evento malicioso até a abertura do caso; o MTTR, da abertura até a contenção. Repare que definimos os marcos por escrito: sem isso, cada analista mediria de um jeito. A cobertura testada divide as técnicas com detecção comprovada pelas técnicas priorizadas; a visibilidade conta as que têm telemetria. E as ações no prazo e retestadas mostram se as correções saíram do papel. O quadro azul traz dois cuidados. Com vários incidentes, acompanhe a mediana, porque um caso extremo distorce a média. E a Lei de Goodhart: quando uma medida vira meta, deixa de ser boa medida. Um SOC cobrado só por MTTR fecha casos cedo demais."

**Slide 12 — Laboratório: das lacunas do incidente às recomendações, na plataforma Rede Tatame (11:35–13:45)**
Objetivo: ver na plataforma as lacunas que viraram recomendações e o que custa fechá-las.
Na tela:
1. Na aba "Cobertura ATT&CK", apontar os indicadores: 16 técnicas, 0 comprovadas, 6 detectáveis, 6 parciais, 4 cegas e "Cobertura com regra" de 38%. Localizar na matriz T1219 (parcial, regra R8 off) e T1567.002 (cega, regra R9 off).
2. Ir à aba "Telemetria" e marcar "Acesso a buckets e saída de rede". Apontar "Custo por mês" mudando de R$ 2.462 para R$ 2.560.
3. Ir à aba "Regras do CEP" e ligar R8 e R9.
4. Voltar à "Cobertura ATT&CK": 8 detectáveis, 3 cegas, cobertura com regra de 50%, comprovadas ainda 0.
5. No seletor de velocidade, ao lado do relógio, escolher "1 s = 1 min". Ir à aba "Cenários" e clicar em "Iniciar cenário" no cartão "Acesso remoto não aprovado e saída de dados". Esperar os três passos (cerca de 10 segundos).
6. Voltar à "Cobertura ATT&CK": comprovadas passa para 2.
Fala: "Agora as mesmas lacunas na plataforma que acompanha a disciplina. Na Cobertura, as duas técnicas do incidente que nos interessam estão aqui: a T1219, software de acesso remoto, parcial, porque há telemetria do EDR mas a R8 está desligada no estado padrão; e a T1567.002, exfiltração para nuvem, cega, porque nem a fonte existe. Na Telemetria, ligo a fonte de saída de rede. Olhe o custo por mês: de R$ 2.462 para R$ 2.560, cerca de R$ 100 a mais na amostra simulada. Esse é o tipo de número que entra na coluna de esforço e na decisão da diretoria. Nas Regras do CEP, ligo a R8 e a R9. De volta à Cobertura: as duas técnicas viram detectáveis e a cobertura com regra sobe de 38% para 50%. Mas comprovadas continua zero. Regra ligada sem teste é hipótese. Então rodo o cenário com o relógio acelerado. Na linha do tempo, a instalação do ConectaJá é detectada pela R8, as conexões periódicas aparecem nos logs sem alerta e o envio de 2,8 GB é detectado pela R9. Volto à Cobertura: duas técnicas comprovadas."
Atenção: o simulador começa no estado padrão a cada gravação; se algo já estiver ligado, use "Reiniciar". Espere o cenário terminar antes de trocar de aba. A cobertura com regra soma detectáveis e comprovadas, por isso continua em 50% depois do cenário; o que muda é quantas estão comprovadas. Custos e volumes são da amostra fictícia.
Conclusão: "No relatório, só conta como corrigido o que passou no reteste. No simulador, o cenário comprovou a detecção; no exercício real de 10 de dezembro, a R9 alertou fora do critério de 300 segundos, e por isso o A-03 continua aberto."
[Tela: gravação do laboratório do slide 12]

**Slide 13 — Laboratório: o sumário executivo de uma página (13:45–15:20)**
Objetivo: ler o RPT-2026-12 como a diretoria vai ler.
Na tela:
1. Com a aba "Sumário executivo" aberta, ler os títulos dos quatro blocos: "1. O que aconteceu", "2. Onde estamos", "3. O que pedimos" e "4. Como vamos medir".
2. Clicar em "Anexo técnico" e percorrer a tabela dos oito achados.
3. Clicar em "Sumário executivo" de novo e depois em "Registrar decisões".
Fala: "Esta é a página que a diretoria recebe. Repare no que não está nela: nenhum identificador de técnica, nenhum nome de regra. No bloco 1, o incidente em três frases, terminando com a comunicação à ANPD no prazo. No bloco 2, onde estamos: oito falhas, quatro críticas, duas já corrigidas e testadas de novo; no teste de 10 de dezembro detectamos a tempo 5 das 6 técnicas, contra 3 antes da correção. No bloco 3, o que pedimos, e é aqui que o relatório vira decisão: aprovar já os ganhos rápidos que dependem da diretoria, com o alerta de saída de dados acelerado até 17 de dezembro, incluir a separação da rede no primeiro trimestre de 2027 e aceitar o risco alto até lá. No bloco 4, como vamos medir: tempo até perceber de 4 h 21 min para até 1 hora e tempo até conter abaixo de 30 minutos. No Anexo técnico, cada linha é um achado com técnica, evidência, risco e estado, e remete à ficha completa. Volto e clico em 'Registrar decisões': a ata de 16 de dezembro registra cada decisão com dono e prazo, e a aceitação do risco do A-06 até 31 de março de 2027, assinada pela diretoria."
Atenção: o documento e a ata são fictícios. Dê alguns segundos para a leitura de cada bloco antes de comentar.
Conclusão: "Três decisões, cada uma com dono, prazo e indicador. Essa é a segunda metade da resposta à pergunta da aula."
[Tela: gravação do laboratório do slide 13]

**Slide 14 — Laboratório: o relatório alimenta o próximo exercício (15:20–16:45)**
Objetivo: ver que o relatório fecha um ciclo e abre o próximo.
Na tela:
1. O diagrama abre no passo "1 · O incidente" (contador "1 / 7"); ler o texto da barra inferior.
2. Clicar em "Avançar" (passo 2 · Lições aprendidas).
3. "Avançar" (passo 3 · Exercício purple) e apontar o rótulo "2 retestadas".
4. "Avançar" (passo 4 · O relatório).
5. "Avançar" (passo 5 · A decisão) e apontar o nó amarelo "Risco aceito".
6. "Avançar" (passo 6 · Roadmap e próximo exercício).
7. "Avançar" (passo 7 · O ciclo recomeça) e apontar a ligação tracejada "próximo relatório", de volta ao início.
Fala: "Vamos juntar a unidade inteira num diagrama. O incidente de 1º de dezembro mostrou o que faltava. Na reunião de lições aprendidas, em 9 de dezembro, sem caça a culpados, cada falha virou ação: seis ações. No exercício *purple* de 10 de dezembro, R5 e R13 passaram no reteste; a R9 alertou em 540 segundos, acima do critério de 300, e voltou para ajuste. O relatório junta tudo e a diretoria decide: aprova os ganhos rápidos, põe a segmentação no orçamento e assina a aceitação do risco do A-06. As decisões entram no *roadmap* com dono e prazo, e o exercício de março retesta o que foi corrigido, incluindo uma regra nova para a fadiga de MFA. As métricas de março serão comparadas com as de dezembro, e o próximo relatório responde se o MTTD caiu para até uma hora. O ciclo recomeça."
Atenção: prefira "Avançar" a "Auto" na gravação e espere a animação dos pacotes antes do próximo clique.
Conclusão: "Um programa de segurança é esse ciclo repetido, com números que se comparam de um relatório para o outro."
[Tela: gravação do laboratório do slide 14]

**Slide 15 — O caminho percorrido nas quatro unidades (16:45–17:40)**
Fala: "Antes de responder à pergunta da aula, quero olhar com você para o caminho todo. Na Unidade 1, você aprendeu a planejar: as quatro cores, as regras de engajamento, o ATT&CK e a inteligência de ameaças. Na Unidade 2, viu técnicas ofensivas em laboratório, sempre perguntando que rastro cada uma deixa. Na Unidade 3, a defesa: telemetria, SIEM, regras, caça a ameaças e *hardening*. E nesta unidade, você respondeu a um incidente, preservou evidências, validou detecções e escreveu o relatório. Cada etapa tem uma função profissional: analista de SOC, resposta a incidentes, engenharia de detecção, *threat hunting*, *pentest*, Red Team. O NICE Framework do NIST descreve essas funções, e laboratórios, CTFs e relatórios bem escritos mostram a sua prática."
[Take de apoio: profissionais em um SOC trocando informações diante de painéis — Envato]

**Slide 16 — De volta ao problema (17:40–18:35)**
Fala: "Voltemos a Marina Prado e à página que a diretoria pediu. Os oito achados ficaram comparáveis, com evidência, técnica, risco, dono e prazo. A divisão do risco pelo esforço pôs o A-01, o A-02, o A-03 e o A-04 na semana seguinte e a segmentação no *roadmap*. Os números têm meta: o MTTD de 4 h 21 min contra uma meta de 1 hora, o MTTR de 21 minutos dentro da meta e a cobertura testada do exercício de 50% para 83%. E o ciclo continua: o próximo exercício retesta o que está aberto. Então, como transformar o incidente e o exercício em um relatório que leve a decidir e permita medir? Separando o técnico do executivo, pontuando cada achado na matriz de risco, ordenando as recomendações por risco e esforço e escolhendo poucas métricas com meta."

**Slide 17 — Pontos-chave (18:35–19:00)**
Fala: "Para levar desta aula: o relatório final tem uma camada técnica, com evidências, e uma executiva, em uma página. Cada achado traz evidência, técnica, impacto, risco, recomendação, dono, prazo e critério de reteste. A matriz de probabilidade e impacto classifica; risco dividido por esforço ordena. As métricas têm definição, meta e dono. E só o que foi retestado conta como corrigido."

**Slides 18 e 19 — Referências e encerramento da disciplina (19:00–19:45)**
Fala: "As referências estão no slide, com destaque para o NIST SP 800-30 e a ISO 31000, sobre avaliação de risco. E assim encerramos a disciplina. Você planejou uma operação, atacou e defendeu a Rede Tatame em laboratório, respondeu a um incidente, validou detecções e escreveu o relatório que leva à decisão. Continue praticando, sempre em ambientes autorizados, porque nesta área autorização e ética vêm antes de qualquer técnica. Foi um prazer fazer este percurso com você. Até a próxima!"
[Tela: slide de encerramento por 5 segundos]
