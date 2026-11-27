# Roteiros das videoaulas — Unidade 1 — Planejamento de Operações e Emulação de Adversário

Disciplina: Red Team & Blue Team Strategies  
Professor: Afonso Cesar Lelis Brandão

> Cópia dos roteiros de `unidade_1.md`, só para a gravação. O texto de origem continua no `unidade_1.md` (é dele que sai o DOCX).

## Roteiro do vídeo introdutório (até 2 minutos)

**Abertura (0:00–0:15)**  
"Olá! Eu sou o professor Afonso Brandão e seja muito bem-vindo, seja muito bem-vinda à disciplina Red Team & Blue Team Strategies! Se você quer entender como os ataques acontecem de verdade para conseguir defender uma empresa, você está no lugar certo!"

**Conexão com o mercado (0:15–0:45)**  
"Quase toda semana aparece uma notícia de vazamento de dados ou de *ransomware* parando uma empresa. O que as organizações buscam hoje vai além de instalar antivírus e *firewall*. Elas querem profissionais que saibam simular um adversário real, com autorização, e que saibam detectar e responder rápido quando algo acontece."  
[Take de apoio: manchetes de incidentes de segurança e uma sala de SOC com telas de monitoramento — Envato]

**Conteúdo e diferencial (0:45–1:20)**  
"Você vai planejar uma operação de Red Team com regras de engajamento, montar um plano de emulação na matriz MITRE ATT&CK, conhecer o Kali Linux, o Metasploit, o Wazuh e o Wireshark, detectar, caçar e responder a incidentes e, no fim, juntar as equipes em exercícios *purple team*. O diferencial? Tudo acontece na Rede Tatame, uma rede fictícia de academias de jiu-jitsu, com app, catracas e um SOC, que você vai atacar e defender em simulação no semestre inteiro."  
[Tela: gravação de 5 segundos do simulador da Rede Tatame, aba Arquitetura, com o cenário rodando]

**Benefícios (1:20–1:45)**  
"Ao final, você será capaz de conduzir um exercício completo, do planejamento ao relatório, e de conversar com a área técnica e com a diretoria sobre risco cibernético, com evidências e métricas."

**Chamada para ação (1:45–2:00)**  
"Então, se você quer estar preparado para os desafios da cibersegurança, essa disciplina é para você! Nos vemos nas aulas. Boa aula!"

## Roteiro da Videoaula 1 — "Quem apita o jogo quando a empresa contrata o próprio invasor?"

Duração-alvo: 15 a 20 minutos. Deck: unidade_1/slides/aula1.html (18 slides).

**Slides 1 e 2 — Capa e sumário (0:00–0:35)**  
Fala: "Olá! Nesta primeira aula da Unidade 1, vamos conhecer os quatro papéis de um exercício de segurança ofensiva e defensiva: Red Team, Blue Team, White Team e Purple Team. Você vai ver o que cada um faz, o que cada um entrega e como é o ciclo de uma operação de Red Team, do planejamento ao reteste. A aula tem sete laboratórios, e todos usam a Rede Tatame, a empresa fictícia que vamos atacar e defender durante o semestre."  
[Tela: deck aberto no slide 1; avançar até o sumário]

**Slide 3 — O problema de hoje na Rede Tatame (0:35–2:00)**  
Fala: "Imagine a cena. A Rede Tatame tem 240 academias de jiu-jitsu e já comprou *firewall*, antivírus e autenticação em dois fatores. Na reunião de diretoria, alguém pergunta à CISO, a diretora de segurança da informação, Marina Prado: 'estamos seguros?'. E ela percebe que não tem como provar. As ferramentas estão instaladas, mas ninguém sabe se detectariam um ataque, nem em quanto tempo a equipe reagiria. E o que está em jogo pesa: 36 mil alunos, cerca de 30% menores de idade, biometria facial nas catracas e atestados de saúde. A pergunta desta aula está em amarelo no slide: como a Rede Tatame pode testar a própria defesa sem esperar um ataque real, e quem faz o quê nesse teste? Guarde os quatro nomes aqui embaixo: Bruno Sato, do Red Team; Luiza Ferraz, do Blue Team; Marina Prado, que hoje fará o papel de White Team; e Carla Dias, do financeiro, que será o alvo do teste."  
Fala (apontando o mapa): "À direita está o mapa da plataforma. Em destaque, o *e-mail*, o notebook de Carla, em vermelho, e o SOC, o centro de operações de segurança, que deveria perceber o exercício."  
[Take de apoio: reunião de diretoria com uma pessoa apresentando gráficos — Envato]

**Slide 4 — Da simulação militar ao adversário autorizado (2:00–2:50)**  
Fala: "Os nomes vêm dos *wargames*, os jogos de guerra militares. A força vermelha fazia o papel do inimigo para testar os planos da força azul, e uma equipe neutra, de branco, controlava as regras. Na cibersegurança, a lógica continua: só sabemos se uma defesa funciona quando alguém que pensa como o adversário a põe à prova, sob regras que alguém faz cumprir. O Red Team emula um adversário real, com autorização, e persegue objetivos combinados, como acessar a base de fichas de alunos. O Blue Team protege, monitora, detecta e responde todos os dias, contra ameaças reais. E guarde duas siglas: MTTD, o tempo médio do primeiro evento até a detecção, e MTTR, o tempo da detecção até a contenção."

**Slide 5 — O árbitro e a ponte: White Team e Purple Team (2:50–3:55)**  
Fala: "Agora as duas cores que costumam ser esquecidas. O White Team, também chamado de célula branca, planeja, controla e arbitra o exercício, sem participar da disputa. São poucas pessoas, os *trusted agents*, ou agentes de confiança, que sabem que a operação está acontecendo. É o White Team que aprova o plano e as regras de engajamento, decide se uma ação está dentro do combinado, pausa ou encerra o exercício pelos critérios de parada e julga o que foi detectado. Uma tarefa dele merece destaque: a *deconfliction*. Quando o SOC escala um alerta, o White Team confere no registro do Red Team se aquela atividade é do exercício. Se não for, pode ser um incidente real, e o teste para. Já o Purple Team é uma forma de colaboração: o Red executa uma técnica, o Blue confere se a detectou e os dois ajustam a regra e retestam."

**Slide 6 — Visualização 3D: quatro cores, um exercício (3:55–4:55)**  
Objetivo: ver o papel de cada equipe antes de montar o teste da Rede Tatame.  
Na tela:  
1. Deixar a cena girar alguns segundos sozinha.  
2. Arrastar com o *mouse* até ver o ponto em que os anéis vermelho e azul se cruzam, com a esfera roxa no centro.  
3. Girar para o lado até ver o anel branco, maior, que envolve tudo, e os quatro marcadores brancos que correm sobre ele.  
4. Rolar a roda do *mouse* para aproximar das partículas.  
Fala: "O anel vermelho, à esquerda, é o Red Team, com o rótulo 'emular'. O azul, à direita, é o Blue Team, com o rótulo 'detectar'. No cruzamento fica a esfera roxa, o Purple, que significa colaborar. As partículas saem vermelhas do lado do ataque, ficam roxas no meio e chegam azuis do lado da defesa: cada uma representa uma técnica testada que virou detecção. E repare no anel branco, por fora de tudo, com o rótulo 'White Team · arbitrar'. Ele não cruza com nenhum dos outros, porque o árbitro não joga. Os quatro marcadores sobre ele lembram as tarefas do White Team: aprovar as regras, fazer a *deconfliction*, decidir a parada e julgar o resultado. A legenda, no canto, resume as quatro cores."  
Atenção: a cena é uma metáfora visual; as partículas não representam dados reais. Se não carregar, avise que ela depende de conexão com a internet.  
Conclusão: "Testar a defesa pede quem ataca, quem defende, quem junta os resultados e quem garante as regras."  
[Tela: gravação do laboratório do slide 6]

**Slide 7 — Missão, pergunta, entregável e quem sabe do exercício (4:55–5:50)**  
Fala: "Esta tabela compara as quatro cores. Olhe a linha da pergunta central. O Red Team pergunta 'até onde um atacante chegaria?'. O Blue Team, 'percebemos e contivemos a tempo?'. O White Team, 'o exercício está seguro e dentro do combinado?'. E o Purple Team, 'o que aprendemos e o que mudou?'. Os entregáveis também mudam: relatório e caminho de ataque; alertas e relatórios de incidente; plano aprovado, arbitragem e linha do tempo oficial; detecções novas e métricas de cobertura. A última linha é a mais importante para o exercício: o Blue Team, em geral, não sabe que está sendo testado. Só o Red e o White sabem, e é isso que torna a medição honesta."

**Slide 8 — Laboratório: o ciclo de uma operação de Red Team (5:50–7:35)**  
Objetivo: ver que a operação começa muito antes do primeiro comando e que o White Team acompanha todas as etapas.  
Na tela:  
1. Ler o passo inicial, "Seis etapas e um árbitro", que já está na tela.  
2. Clicar em "Avançar" para "1 · Planejamento".  
3. Avançar por "2 · Inteligência e emulação", "3 · Preparação" e "4 · Execução".  
4. Avançar por "5 · Relatório" e "6 · Lições e reteste". O contador, à direita, mostra 7 / 7.  
Fala: "O diagrama mostra as seis etapas de uma operação, em sentido horário, e o White Team no centro. Na primeira, o planejamento, Marina Prado e Bruno Sato combinam o objetivo de negócio, por exemplo 'o SOC percebe um *phishing* no financeiro?', o escopo, as regras de engajamento e a carta de autorização. Repare na linha amarela saindo do White Team: é ele que aprova. Esse é o tema da Aula 2. Na segunda etapa, a inteligência de ameaças escolhe qual adversário emular, e as técnicas dele, catalogadas no MITRE ATT&CK, viram o plano de emulação; isso é assunto das Aulas 3 e 4. Na preparação, o Red Team monta o domínio do exercício, as contas de teste e o registro de ações, que anota o quê, de onde e quando. Na execução, as técnicas rodam dentro da janela e do escopo, e o White Team faz a *deconfliction* sempre que o SOC escala um alerta. No relatório, a linha do tempo do Red Team é comparada com o que o Blue viu, e o White valida o julgamento. Por fim, lições e reteste: cada lacuna vira uma regra nova, testada em ciclos *purple*, e a seta tracejada leva de volta ao próximo planejamento."  
Atenção: o botão "Auto" avança sozinho; para gravar com calma, prefira "Avançar". A seta para a esquerda volta um passo.  
Conclusão: "A execução é só uma das seis etapas. Sem planejamento, inteligência e reteste, o exercício vira um teste solto, que não mede nada."  
[Tela: gravação do laboratório do slide 8]

**Slide 9 — Laboratório: um *phishing* simulado e dois desfechos (7:35–9:45)**  
Objetivo: ver os quatro papéis agindo no mesmo exercício e o que muda quando o SOC percebe ou não percebe.  
Na tela:  
1. Ler o passo inicial, "09h00 · A campanha começa".  
2. Clicar em "Avançar" para "09h04 · O filtro deixa passar" e "09h12 · Um clique".  
3. Avançar pelos quatro passos do Desfecho A: "09h13 · A telemetria chega", "09h17 · Alerta e triagem", "09h19 · Deconfliction" e "09h22 · Contenção em 10 minutos".  
4. Avançar para "Desfecho B · Ninguém percebe".  
5. Avançar para "Nos dois casos · Reunião purple". O contador mostra 9 / 9.  
Fala: "Às 9h, Bruno Sato dispara 40 *e-mails* de um domínio registrado há dois dias, como faria um criminoso. O exercício está no plano aprovado pelo White Team. O domínio é novo e ainda não aparece em listas de bloqueio, então o filtro deixa passar. Às 9h12, Carla Dias clica no *link* 'Atualize seus benefícios' no notebook NB-FIN-031, e abre uma página falsa de *login*, controlada pelo Red Team. No desfecho A, em azul, o EDR, o agente de segurança do notebook, manda o evento para o SIEM, que correlaciona com o *e-mail* recebido. Às 9h17 sai um alerta de severidade alta, e Luiza abre o caso. Agora o passo novo desta aula: às 9h19, Luiza escala o caso como faria com qualquer incidente. Marina, do White Team, confere o registro do Red Team: mesmo domínio, mesmo horário. É o exercício. E ela não avisa o SOC, porque é a resposta do SOC que está sendo medida. Às 9h22, o notebook está isolado, a senha foi trocada e as mensagens foram removidas; a tentativa na VPN já tinha parado no MFA. No desfecho B, em amarelo, falta a regra que liga domínio novo e *e-mail* recebido, e ninguém percebe. Nos dois casos, termina na reunião *purple*, com a linha do tempo validada pelo White Team."  
Atenção: os horários e os nomes são fictícios. Se faltar tempo, o botão "Auto" percorre os passos sozinho.  
Conclusão: "O Red cria a situação, o Blue responde, o White separa o exercício da realidade e o Purple transforma o resultado em melhoria."  
[Tela: gravação do laboratório do slide 9]

**Slide 10 — Laboratório: o analista de SOC investiga o exercício (9:45–11:55)**  
Objetivo: medir se o SOC de Luiza Ferraz percebeu o *phishing* simulado.  
Na tela:  
1. Clicar na busca salva "1. Quem recebeu?".  
2. Clicar em "2. Quem clicou?".  
3. Clicar em "3. Processo estranho depois?".  
4. Clicar em "4. A senha foi usada?".  
5. Clicar em "5. Em quanto tempo o SOC viu?", no grupo Métricas.  
Fala (busca 1): "Este é o console do SIEM. No alto, a consulta em KQL, a linguagem de busca da ferramenta, filtra os *e-mails* do domínio portal-rh-beneficios.example. Resultado: 40 mensagens, todas entregues, com pico às 9h no histograma."  
Fala (busca 2): "Agora os acessos ao mesmo domínio. Três pessoas abriram a página de *login*: 3 cliques em 40 envios, uma taxa de 7,5%. Esse número entra no relatório, sem expor quem clicou para fora da equipe."  
Fala (busca 3): "Esta consulta procura processos no NB-FIN-031 abertos pelo navegador ou pelo Outlook. Só aparecem dois eventos do próprio navegador, com severidade 'info'. Nenhum programa foi executado, como o escopo previa."  
Fala (busca 4): "Aqui está a auditoria de *login* de carla.dias. Às 9h13, a senha capturada foi testada na VPN: 'senha ok, MFA recusado'. O MFA segurou, mas a senha precisa ser trocada mesmo assim."  
Fala (busca 5): "Por fim, as métricas do caso INC-2026-1116-01. Primeiro evento às 9h12min07, alerta às 9h17min02, contenção às 9h22min10. O MTTD foi de 4 minutos e 55 segundos, e o MTTR, de 5 minutos e 8 segundos."  
Atenção: as consultas são exibidas para leitura; o console não executa KQL de verdade. Os IPs 198.51.100.x são de uma faixa reservada para documentação.  
Conclusão: "O exercício virou números que a CISO pode mostrar à diretoria."  
[Tela: gravação do laboratório do slide 10]

**Slide 11 — Laboratório: o mesmo exercício na plataforma da disciplina (11:55–14:05)**  
Objetivo: ver o mesmo exercício na plataforma Rede Tatame, responder como Blue Team e notar o alerta que não pertence ao exercício.  
Na tela:  
1. O simulador abre na aba Cenários. Conferir que a velocidade está em "1 s = 15 s".  
2. No cartão "Phishing simulado no financeiro", clicar em "Iniciar cenário" e rolar até a linha do tempo dos passos.  
3. Esperar os três passos aparecerem (cerca de 25 segundos reais).  
4. Abrir a aba SOC. Na linha do alerta da regra R1, clicar em "Investigar" e ler o painel; depois clicar em "Conter".  
5. Na mesma tabela, clicar em "Investigar" na linha da regra R11 (conta svc-backup).  
6. Voltar à aba Arquitetura e localizar o notebook NB-FIN-031.  
Fala: "Agora o mesmo *phishing* roda no simulador da disciplina. Ao clicar em 'Iniciar cenário', o relógio anda e os passos entram na linha do tempo, cada um com a técnica do ATT&CK, a fonte de dados e a regra que o detectaria. Os 40 *e-mails* aparecem como 'visto nos logs, sem alerta': o *gateway* registrou, mas nenhuma regra disparou. O clique de Carla aparece como 'detectado', pela regra R1. A senha usada na VPN aparece como 'bloqueado pelo controle': é o MFA. Na aba SOC, abro o alerta da R1, leio a lógica da regra e o tempo até o alerta, e clico em 'Conter'. Agora vejam o segundo alerta, da R11: *login* sem MFA na VPN com a conta svc-backup. Pensem como White Team: essa conta não aparece no registro do Red Team. Não é do exercício. O painel mostra que é um comportamento conhecido e documentado, então aqui seria falso positivo; mas, se não fosse, o White Team trataria como possível incidente real. Na Arquitetura, o NB-FIN-031 aparece isolado."  
Atenção: se você conter o alerta antes do terceiro passo, ele aparece como "interrompido pela contenção"; para mostrar o MFA, espere os três passos. O alerta da R11 surge cerca de 30 segundos depois do início. Para repetir, use "Repetir com as fontes e regras atuais"; "Reiniciar" devolve fontes e regras ao padrão.  
Conclusão: "O Red Team criou o cenário, o Blue Team respondeu e o White Team separou o que era do exercício. A aba Cobertura ATT&CK mostra o resultado do ponto de vista *purple*."  
[Tela: gravação do laboratório do slide 11, com zoom na linha do tempo e na tabela do SOC]

**Slide 12 — Antes do código: onde achar e como instalar (14:05–14:35)**  
Fala: "Antes de rodar o código, veja o que ele usa e de onde vem. O Visual Studio Code e o Python 3.12, baixados dos *sites* oficiais; a extensão Python, da Microsoft; e o pacote tabulate, que imprime o veredito em forma de tabela. Os módulos csv, sys e datetime já vêm com o Python. Antes de instalar um pacote, busque o nome no PyPI, o índice oficial de pacotes Python, e confira letra por letra. Nome quase igual ao verdadeiro é um golpe conhecido, o *typosquatting*."

**Slide 13 — Laboratório: o caderno do árbitro (14:35–17:05)**  
Objetivo: julgar o exercício como o White Team, cruzando o registro do Red Team com os alertas do SOC.  
Tela cheia: o VS Code ocupa o slide inteiro, sem cabeçalho nem painel lateral. O roteiro do laboratório (Objetivo, Faça, Observe e Conclusão) abre e fecha com a tecla G ou com o botão "☰ Roteiro", na barra de status do VS Code. Deixe-o fechado durante a gravação.  
Na tela:  
1. Com o arquivo arbitro.py aberto, esperar a digitação automática terminar.  
2. Clicar em "Preparar o ambiente", o botão azul acima do terminal, e esperar ele mudar para "Ambiente pronto". O editor passa a mostrar o requirements.txt.  
3. No explorador, clicar em acoes_red.csv e depois em alertas_soc.csv.  
4. Voltar a arbitro.py e mostrar as linhas destacadas (24 a 26).  
5. Clicar em "Julgar o exercício" e ler a saída no terminal.  
6. Clicar em "Julgar o reteste" (o editor abre o alertas_reteste.csv) e ler a saída.  
Fala (ambiente): "O VS Code ocupa a tela inteira, como no meu computador. Clico em 'Preparar o ambiente'. O primeiro comando confere a versão do Python. O segundo cria o ambiente virtual, a pasta .venv, que separa os pacotes deste projeto dos do sistema, e o terceiro o ativa: repare no .venv no início da linha. O pip install -r requirements.txt baixa do PyPI o tabulate na versão fixada, 0.9.0, e o pip list mostra o que ficou instalado."  
Fala (dados): "São dois registros independentes. O acoes_red.csv é o diário do Red Team: três ações, o envio às 9h00min41, o clique de Carla às 9h12min07 e a tentativa na VPN às 9h13min40, que o MFA bloqueou. O alertas_soc.csv é o que o SOC viu: um alerta da R1 às 9h17min02 e um da R11, às 9h31min10, com a conta svc-backup."  
Fala (código): "As linhas destacadas são as que decidem. Para cada ação do Red Team, o código procura um alerta com a mesma técnica, o mesmo alvo e a mesma conta, registrado na mesma hora ou depois. Se encontra, calcula o atraso em segundos; se não encontra, verifica se o controle bloqueou; senão, a ação passou despercebida. No fim, todo alerta que não casou com nenhuma ação é marcado como *deconfliction*."  
Fala (saídas): "Resultado: a ação A1, o envio, não foi detectada; a A2, o clique, foi detectada pela R1 em 4 minutos e 55 segundos, o mesmo MTTD do SIEM; a A3 foi bloqueada pelo MFA, sem alerta. Detectadas: 1 de 3, 33%. E a última linha, em roxo: o alerta da R11 não é do exercício, então o SOC trata como alerta real. No reteste, depois da reunião *purple*, entrou uma regra nova, a EM-01, que alerta no próprio *gateway* de *e-mail*. Agora o envio é detectado em 1 minuto e 29 segundos: 2 de 3, 67%, com tempo médio de 3 minutos e 12 segundos."  
Atenção: o terminal é simulado e mostra a saída gravada, que é exatamente a que o código produz com esses arquivos. A preparação do ambiente leva cerca de 10 segundos e não baixa nada de verdade; os botões de execução ficam travados até aparecer "Ambiente pronto". A regra EM-01 é um exemplo da aula e não existe no simulador.  
Conclusão: "Sem o registro do Red Team, ninguém separa o exercício de um incidente real, nem mede o que melhorou."  
[Tela: gravação do laboratório do slide 13]

**Slide 14 — Laboratório: por que testar compensa (17:05–18:10)**  
Objetivo: mostrar à diretoria, em reais, por que testar compensa.  
Na tela:  
1. Conferir os valores iniciais: impacto de R$ 6.000.000, 15% sem o programa, 6% com o programa e custo anual de R$ 250.000.  
2. Arrastar "Probabilidade anual com o programa" até 12%.  
3. Voltar para 6%.  
Fala: "A expectativa de perda anual, ou ALE, multiplica o impacto de um incidente pela chance de ele acontecer no ano. Sem o programa: 6 milhões vezes 15% dá R$ 900.000. Com o programa, a chance cai para 6%, e a ALE vai a R$ 360.000. A redução é de R$ 540.000 por ano, 2,16 vezes o custo. Agora, se o programa só baixar a chance para 12%, a ALE com o programa vai a R$ 720.000, a redução cai para R$ 180.000 e o painel avisa que o programa não se paga."  
Atenção: os valores são ilustrativos, para mostrar o raciocínio da expectativa de perda anual; não são estatísticas da Rede Tatame nem do mercado. Mexa em um controle por vez e volte ao valor inicial antes do próximo.  
Conclusão: "O programa só se paga se reduzir o risco de verdade, e é por isso que cada exercício precisa ser medido."  
[Tela: gravação do laboratório do slide 14]

**Slide 15 — De volta ao problema (18:10–19:05)**  
Fala: "Voltemos à pergunta de Marina: como testar a defesa sem esperar um ataque real, e quem faz o quê? Quem ataca é o Red Team de Bruno, num ciclo que começa no planejamento e termina no reteste. Quem defende é o SOC de Luiza, medido em MTTD e MTTR. Quem arbitra é o White Team, que controla as regras, faz a *deconfliction* e julga: 1 de 3 ações detectada, 2 de 3 no reteste. E quem junta é o Purple Team, que transforma o passo que ninguém viu em regra nova. A resposta está no cartão amarelo: exercícios autorizados em que cada cor tem seu papel, e cada falha vira melhoria comprovada."

**Slides 16 a 18 — Pontos-chave, referências e encerramento (19:05–19:45)**  
Fala: "Para levar desta aula: o Red Team emula adversários; o Blue Team defende de forma contínua; o White Team planeja, controla, arbitra e pode parar o exercício; e o Purple Team transforma ataques simulados em detecções validadas. As referências estão no slide seguinte. Na próxima aula, vamos ver o que precisa estar escrito e assinado antes de o Red Team tocar no primeiro sistema: regras de engajamento, escopo, autorização e os aspectos legais. Até lá!"  
[Take de apoio: equipe em frente a telas de monitoramento — Envato]

## Roteiro da Videoaula 2 — "Quem assina antes de o Red Team atacar?"

Duração-alvo: 15 a 20 minutos. Deck: unidade_1/slides/aula2.html (20 slides).

**Slides 1 e 2 — Capa e sumário (0:00–0:40)**  
Fala: "Olá! Na aula passada, vimos os quatro papéis de um exercício: Red, Blue, White e Purple Team. Hoje vamos tratar do que vem antes de qualquer ação técnica: a autorização, as regras de engajamento, o escopo e os cuidados legais. A aula tem cinco laboratórios, e em todos eles a pergunta é a mesma: o que precisa estar escrito antes de o Red Team começar?"  
[Tela: deck aberto no slide 1; avançar até o sumário]

**Slide 3 — O problema de hoje na Rede Tatame (0:40–2:00)**  
Fala: "Bruno Sato, líder do Red Team interno da Rede Tatame, tem uma operação marcada para 16 de novembro. O objetivo é chegar às exportações de fichas de alunos no servidor de arquivos, o SRV-ARQ-01. Mas, da diretoria, chegou só um *e-mail*: 'pentest completo, sem mexer nos dados'. A lista de alvos sugeridos inclui a rede de pagamentos e o parceiro PagaFácil. Ninguém definiu janela, quem pode parar o teste nem como o SOC vai separar o exercício de um ataque de verdade. Por isso a pergunta desta aula, em amarelo no slide: o que precisa estar escrito e assinado antes de o Red Team tocar no primeiro sistema da Rede Tatame? Guarde os quatro nomes de baixo: Bruno, do Red Team; Marina Prado, a CISO, que lidera o White Team; Caio Mendes, administrador de TI, que será o *trusted agent*; e Luiza Ferraz, do SOC, que não vai saber do exercício."  
Fala (apontando o mapa): "No mapa da plataforma, o alvo da operação está em vermelho. Em destaque também aparecem o que não pode ser tocado sem estar escrito: pagamentos, a homologação e os serviços de terceiros."  
[Take de apoio: reunião com uma pessoa revisando documentos sobre a mesa — Envato]

**Slide 4 — O que separa um teste de um crime (2:00–3:00)**  
Fala: "Do ponto de vista técnico, muitas ações de um Red Team são iguais às de um criminoso. A diferença está na autorização. A Lei nº 12.737, de 2012, incluiu no Código Penal o artigo 154-A, que tipifica a invasão de dispositivo informático alheio, e a Lei nº 14.155, de 2021, agravou as penas. O que afasta o crime é a autorização expressa de quem tem poder sobre o dispositivo e os dados. Daí saem três consequências. Primeira: quem assina precisa ter autoridade real; um gerente de TI não autoriza o teste do sistema de um parceiro. Segunda: serviços de terceiros, como o PagaFácil ou a página de status, ficam fora, a menos que o próprio terceiro autorize. Terceira: o que não foi previsto não foi autorizado."  
[Take de apoio: pessoa assinando um documento ao lado de um *notebook* — Envato]

**Slide 5 — A LGPD continua valendo durante o exercício (3:00–3:50)**  
Fala: "A autorização para testar não suspende a LGPD. Fichas, atestados e biometria facial são dados pessoais, alguns sensíveis e de crianças, porque cerca de 30% dos alunos são menores. Então as regras do exercício precisam prever três coisas: minimização, ou seja, coletar só a evidência necessária, como a contagem de registros acessíveis, nunca uma cópia da base; segurança das evidências, como pede o artigo 46; e o descarte ao final, com prazo. E, se o teste revelar um vazamento real, a empresa avalia a comunicação à ANPD e aos titulares, pelo artigo 48."

**Slide 6 — Varredura, pentest e Red Team (3:50–4:50)**  
Fala: "As regras dependem do tipo de avaliação. A varredura de vulnerabilidades pergunta quais falhas conhecidas existem; tem escopo amplo, nenhuma furtividade, e o Blue Team sabe. O *pentest* pergunta o que pode ser explorado num alvo delimitado, e o Blue Team normalmente também sabe. A operação de Red Team pergunta se a organização detecta e responde, persegue um objetivo e é furtiva: normalmente só o White Team sabe. Repare também no nível de informação: caixa-preta, só o nome da empresa; caixa-cinza, informações parciais, como uma conta de colaborador; caixa-branca, diagramas, código e configurações. A operação de novembro será em caixa-cinza."

**Slide 7 — Visualização 3D: a pirâmide das avaliações (4:50–5:50)**  
Objetivo: ver por que o tipo de avaliação muda o que a autorização precisa dizer.  
Na tela:  
1. Arrastar a cena para girar a pirâmide.  
2. Clicar em "Varredura", no canto da cena, e ler a legenda.  
3. Clicar em "Pentest" e depois em "Red Team".  
4. Clicar em "Pirâmide inteira".  
Fala: "Cada andar é um tipo de avaliação. Quando clico em Varredura, o andar se destaca e a legenda mostra a pergunta, o escopo e quem é avisado. Subindo para *Pentest*, a autorização passa a listar técnicas permitidas e proibidas. No topo, Red Team: furtividade alta, e só o White Team sabe. Veja o rótulo à esquerda, 'menos gente sabe do teste'. Quanto menos o Blue Team sabe, mais o documento precisa prever: critérios de parada, contatos 24 horas e *deconfliction*."  
Atenção: a cena gira sozinha devagar; clique nos botões antes de arrastar para a legenda acompanhar a fala.  
Conclusão: "A operação de novembro está no topo da pirâmide, e é por isso que ela pede as regras mais completas."  
[Tela: gravação do laboratório do slide 7]

**Slide 8 — Os dez itens que traduzem a autorização em limites (5:50–7:00)**  
Fala: "As regras de engajamento, ou RoE, de *Rules of Engagement*, transformam a autorização em limites operacionais. Metodologias como o NIST SP 800-115 e o PTES colocam essa etapa, o pré-engajamento, antes de qualquer ação técnica. São dez itens: o objetivo; o escopo, com os excluídos por escrito; o modelo de caixa e as contas de teste; as janelas de execução; as técnicas permitidas e proibidas; o tratamento de dados sensíveis; os critérios de parada e a palavra de parada; o White Team, os *trusted agents* e os contatos 24 horas; a *deconfliction* e o registro de ações do operador; e, por fim, a forma e o prazo do relatório e da destruição das evidências. Vamos conferir esses dez itens em código daqui a pouco."  
[Take de apoio: prancheta com uma lista de verificação sendo preenchida — Envato]

**Slide 9 — A carta que o operador leva consigo (7:00–7:40)**  
Fala: "A carta de autorização é o documento curto que o operador apresenta se alguém perguntar o que ele está fazendo. Ela identifica quem autoriza e com que autoridade, que na Rede Tatame é a CISO Marina Prado, a equipe, o escopo resumido, o período, os contatos de verificação e o número do chamado de aprovação, o APR-2291. Como ela protege o Red Team e a empresa, a integridade importa. Guarda-se a versão assinada, com o *hash* SHA-256 registrado no chamado. Uma cópia alterada depois da assinatura não autoriza nada. Vamos verificar isso no terminal."

**Slide 10 — Laboratório: a carta de autorização é a versão assinada? (7:40–9:20)**  
Objetivo: confirmar que a carta que Bruno Sato leva é a versão assinada por Marina Prado.  
Na tela:  
1. Clicar em "Próximo comando": `ls -l autorizacao/`.  
2. Clicar em "Próximo comando": `cat autorizacao/APR-2291.sha256`.  
3. Clicar em "Próximo comando": `sha256sum -c APR-2291.sha256`, executado dentro da pasta.  
4. Clicar em "Próximo comando": `gpg --verify` com a assinatura `.asc`.  
5. Clicar em "Próximo comando": `sha256sum` da cópia que chegou por *e-mail*.  
Fala (ls): "Estamos no notebook do Red Team, o NB-RED-002. A pasta tem quatro arquivos: o APR-2291.sha256, que é o *hash* registrado no chamado; a carta em PDF; a assinatura destacada, terminada em .asc; e uma cópia que chegou por *e-mail* às 9h40. Repare no tamanho: a cópia tem 201.377 *bytes*, 33 a mais que a original."  
Fala (cat e sha256sum -c): "O *hash* é uma impressão digital do arquivo: qualquer mudança de um único *byte* gera outro valor. O cat mostra o valor registrado por Marina, seguido do nome do arquivo. O sha256sum com a opção -c recalcula o *hash* da carta e compara com esse registro. A palavra OK, em verde, quer dizer que nenhum *byte* mudou desde a aprovação."  
Fala (gpg): "O *hash* prova que o arquivo é o mesmo; a assinatura digital prova quem aprovou. O gpg --verify mostra a data da assinatura, 12 de novembro às 18h02, a chave usada e, na linha verde, 'Good signature' de Marina Prado."  
Fala (cópia): "Agora a cópia do *e-mail*. O *hash* começa com 595a7e, totalmente diferente do registrado, que começa com 0a4a81. Alguém mudou o documento. Essa versão não vale como autorização, e Bruno avisa Marina sobre a divergência."  
Atenção: os *hashes* e a chave são ilustrativos, gerados para o laboratório; o comportamento dos comandos é o real.  
Conclusão: "Só a versão assinada, com o *hash* conferido no chamado, autoriza o exercício."  
[Tela: gravação do laboratório do slide 10]

**Slide 11 — Laboratório: *deconfliction* passo a passo (9:20–11:30)**  
Objetivo: ver como a equipe separa o exercício de um incidente real durante a operação.  
Na tela:  
1. Ler o primeiro passo, "Quem participa".  
2. Clicar em "▶ Avançar" para "10h20 · A ação e o registro".  
3. Avançar para "10h24 · O alerta chega" e "10h26 · O trusted agent confere".  
4. Avançar para "Desfecho A · Bate" e "Desfecho B · Não bate".  
5. Avançar para "Palavra de parada" e "Retomada".  
Fala: "Em uma operação de Red Team, o Blue Team normalmente não sabe do teste. Então, como evitar que um alerta do exercício seja tratado como ataque, ou pior, que um ataque real seja ignorado porque 'deve ser o Red Team'? Às 10h20, Bruno enumera compartilhamentos no SRV-ARQ-01 a partir do NB-RED-002 e anota no registro de ações o quê, de onde e quando. Às 10h24, o EDR gera um alerta, e Luiza Ferraz escala o caso como faria com qualquer incidente. Ela não pode ser avisada, porque é a resposta dela que está sendo medida. Às 10h26, Caio Mendes, o *trusted agent*, compara com o registro: mesma origem, mesmo horário, mesma técnica."  
Fala (desfechos): "No desfecho A, tudo bate. O exercício segue e o alerta conta como detecção, com MTTD de 4 minutos. No desfecho B, às 10h41, aparece um login no SRV-ERP-01 com uma conta que não está no registro, vinda de outra origem. Pode ser um ataque real acontecendo em paralelo. Esse é um critério de parada da RoE: Marina Prado diz a palavra de parada, QUIMONO, Bruno interrompe todas as ações na hora, anota o horário e preserva o registro, e o SOC trata o caso como incidente real. O exercício só volta quando o White Team decide."  
Atenção: o botão "⏯ Auto" avança sozinho; na gravação, prefira "▶ Avançar" para controlar o ritmo da fala.  
Conclusão: "Sem o registro de ações do operador, ninguém consegue separar o exercício de um ataque verdadeiro."  
[Tela: gravação do laboratório do slide 11]

**Slide 12 — Antes do código: onde achar e como instalar (11:30–12:00)**  
Fala: "Antes de rodar o código, veja o que os laboratórios usam e de onde vem cada coisa: o Kali Linux, numa máquina virtual, que vamos instalar no próximo slide; o Visual Studio Code e o Python 3.12, baixados dos *sites* oficiais; a extensão Python, da Microsoft; e o pacote PyYAML, que lê o arquivo de regras. Antes de instalar, busque o nome no PyPI, o índice oficial de pacotes Python, e confira letra por letra. Nome quase igual ao verdadeiro é um golpe conhecido, o *typosquatting*. Os outros módulos, ipaddress, sys e datetime, já vêm com o Python."

**Slide 13 — Laboratório: instalar e preparar o Kali Linux (12:00–13:30)**  
Objetivo: mostrar como se instala, confere e prepara a máquina virtual com Kali Linux que os laboratórios de Red Team usam a partir desta aula.  
Na tela:  
1. Clicar em "▶ Próximo comando": o `wget` baixa a imagem do Kali para VirtualBox.  
2. "▶ Próximo comando": `sha256sum` da imagem. Apontar a linha verde.  
3. "▶ Próximo comando": `7z x`, `VBoxManage registervm` e `VBoxManage startvm`. Esperar o *login* `kali` e a mensagem dos desenvolvedores; apontar que o título da janela e o *prompt* mudaram para `kali㉿kali`.  
4. "▶ Próximo comando": `passwd`.  
5. "▶ Próximo comando": `sudo apt update && sudo apt full-upgrade -y`.  
6. "▶ Próximo comando": as versões do Nmap, do Metasploit e do Wireshark.  
7. "▶ Próximo comando": `hostnamectl` e `mkdir`. Apontar o *prompt* final, `kali㉿lab-tatame`.  
Fala (comandos 1 a 3): "A partir de hoje, os laboratórios de Red Team rodam no Kali Linux, a distribuição que já traz as ferramentas da disciplina. Você vai precisar dele instalado, numa máquina virtual, nunca direto no computador do trabalho. Eu baixo a imagem pronta para VirtualBox do *site* oficial, kali.org. Antes de abrir, confiro o *hash*, exatamente como fizemos com a carta de autorização: se não bater com o publicado no *site*, o arquivo não é o original. Depois descompacto, registro a máquina no VirtualBox e ligo. Repare que o terminal mudou: agora estou dentro do Kali."  
Fala (comandos 4 a 7): "O usuário e a senha de fábrica são kali e kali, e isso está na documentação. Então a primeira coisa é trocar a senha. A segunda é atualizar: o Kali recebe versões novas o tempo todo. Confiro as três ferramentas da ementa, o Nmap, o Metasploit e o Wireshark, que já vêm instaladas. Por fim, dou à máquina o nome lab-tatame e crio a pasta do exercício. É esse terminal que você vai ver nas próximas aulas."  
Atenção: a sessão é simulada e o número da versão é ilustrativo; no *site* aparece sempre a versão atual. A máquina virtual só deve ser usada contra alvos autorizados, como manda a RoE desta aula.  
Conclusão: "Até ferramenta de ataque se baixa da fonte oficial, se confere e se mantém atualizada."  
[Tela: gravação do laboratório do slide 13]

**Slide 14 — Laboratório: a RoE conferida antes do primeiro pacote (13:30–16:15)**  
Objetivo: conferir, antes de qualquer ação, se a RoE tem os dez itens, se o horário está na janela e quais alvos estão no escopo.  
Tela cheia: o VS Code ocupa o slide inteiro, sem cabeçalho nem painel lateral. O roteiro do laboratório (Objetivo, Faça, Observe e Conclusão) abre e fecha com a tecla G ou com o botão "☰ Roteiro", na barra de status do VS Code. Deixe-o fechado durante a gravação.  
Na tela:  
1. Com o validar_roe.py aberto, esperar a digitação automática terminar.  
2. Clicar em "Preparar o ambiente", o botão azul acima do terminal, e esperar ele mudar para "Ambiente pronto". O editor passa a mostrar o requirements.txt.  
3. Clicar em roe_rascunho.yaml, no explorador, e depois em roe_tatame.yaml e em alvos.txt.  
4. Voltar ao validar_roe.py.  
5. Clicar em "Rascunho da diretoria" e ler a saída.  
6. Clicar em "Versão final às 10h15".  
7. Clicar em "Versão final às 21h40".  
Fala (ambiente): "O VS Code agora ocupa a tela inteira, como no meu computador. Clico em 'Preparar o ambiente'. O primeiro comando confere a versão do Python; o segundo cria o ambiente virtual, a pasta .venv, e o terceiro o ativa, repare no .venv no início da linha. O pip install -r requirements.txt lê o arquivo aberto no editor e baixa o PyYAML na versão fixada, a 6.0.3. A linha verde confirma a instalação, e o pip list mostra o que ficou no ambiente."  
Fala (arquivos YAML): "O rascunho é o que chegou da diretoria: objetivo 'pentest completo', escopo só com a sede e nada sobre parada, White Team ou *deconfliction*. A versão final, roe_tatame.yaml, tem os dez itens. As linhas destacadas são as que faltavam: a parada, com os critérios e a palavra QUIMONO; o White Team, com Marina Prado, o *trusted agent* Caio Mendes e os contatos 24 horas; e a *deconfliction*, com o registro de ações e a estação NB-RED-002 como única origem. No alvos.txt estão os sete endereços sugeridos."  
Fala (validar_roe.py): "O script tem três partes. A lista ITENS, no topo, são os dez itens da RoE. A linha destacada com if faltam é a que decide se o teste pode começar: se faltar qualquer item, o programa para ali. Depois, a função dias_uteis percorre a janela, pula fins de semana e o feriado, e o script calcula as horas. A linha na_janela confere se o momento informado é um dia útil dentro do horário. Por último, a função no_escopo recusa primeiro os excluídos, IPs da rede PCI ou domínios de terceiros, e só depois aceita o que está nas redes e no domínio autorizados."  
Fala (saídas): "No rascunho, aparecem três X vermelhos: parada, white_team e *deconfliction*. 'Faltam 3 de 10 itens. Nada começa.' Na versão final às 10h15, todos os itens passam. A linha amarela mostra a janela: 9 dias úteis vezes 11 horas, 99 horas; com 80 horas planejadas, sobra uma folga de 19 horas, 19%. Depois vêm os alvos: os dois servidores da sede e o portal gestao estão dentro; a rede PCI, a API da PagaFácil, a página de status e o promo-hml, que é da agência, ficam bloqueados. São 4 de 7, 57%. Às 21h40, o script para logo depois da janela: 'fora da janela, pare e registre'."  
Atenção: os números da saída são os mesmos do exemplo numérico do texto base; a data 2026-11-18 é uma quarta-feira dentro da janela.  
Conclusão: "A RoE deixa de ser só um documento e vira uma verificação que roda antes de cada sessão do Red Team."  
[Tela: gravação do laboratório do slide 14]

**Slide 15 — Laboratório: o escopo e os alertas na plataforma (16:15–18:00)**  
Objetivo: ver o escopo na superfície exposta da Rede Tatame e praticar a *deconfliction* com alertas da plataforma.  
Na tela:  
1. Na aba "8 Superfície", deixar marcada a opção "ordenar por risco".  
2. Localizar as linhas `hml-gestao.tatame.com.br` e `promo-hml.tatame.com.br`, com "não" na coluna inventário.  
3. Ir à aba "6 Cenários" e clicar em "Iniciar cenário" no card "Reconhecimento externo". Manter a velocidade padrão, "1 s = 15 s".  
4. Acompanhar a linha do tempo até o passo da varredura contra 203.0.113.0/24 ficar detectado.  
5. Ir à aba "7 SOC" e clicar em "Investigar" em cada alerta: o R4 da varredura, o R11 do svc-backup e, perto de 1 minuto e 40 segundos depois do início, o R4 do monitor de disponibilidade.  
Fala (superfície): "A aba Superfície lista os ativos expostos da Rede Tatame, com o risco calculado. Duas linhas estão sem inventário. O hml-gestao é uma homologação esquecida da própria Rede Tatame, e por isso pode entrar no escopo se a RoE disser. O promo-hml está hospedado pela agência: aparece no levantamento, mas fica fora do escopo, como diz a nota abaixo da tabela."  
Fala (cenário e SOC): "No cenário de reconhecimento, a primeira consulta a certificados públicos passa sem alerta, porque a fonte está desligada. A varredura da borda dispara a regra R4. Esse alerta bate com o registro do operador: é o exercício. Mas o SOC também recebe outros dois. O R11 mostra um login sem MFA da conta svc-backup, e o R4 seguinte vem do monitor de disponibilidade contratado, o status.tatame.com.br. Nenhum dos dois está no registro do Red Team. Ao clicar em Investigar, a plataforma mostra que são comportamentos conhecidos e documentados, então o SOC marca como falso positivo e o exercício segue. Se não houvesse essa explicação, seria o caso de acionar a parada."  
Atenção: os alertas da R11 e do monitor aparecem em momentos diferentes da simulação; se quiser gravar de novo, use "Reiniciar" no topo e inicie o cenário outra vez.  
Conclusão: "O alerta que não bate com o registro do operador é tratado pelo SOC como qualquer outro, até que se prove o contrário."  
[Tela: gravação do laboratório do slide 15]

**Slide 16 — A janela e o escopo em números (18:00–18:40)**  
Fala: "Vamos fechar as contas que o script fez. De 16 a 27 de novembro de 2026 são 10 dias úteis, mas 20 de novembro, Dia Nacional de Zumbi e da Consciência Negra, é feriado nacional. Restam 9 dias, vezes 11 horas, das 9h às 20h: 99 horas de janela. Com 80 horas planejadas, sobram 19 horas, cerca de 19%, para as pausas de *deconfliction*. E, dos 7 alvos sugeridos, 3 estavam no escopo e 4 foram bloqueados, 57%, entre eles a rede PCI e o parceiro de pagamentos."

**Slide 17 — De volta ao problema (18:40–19:20)**  
Fala: "Voltemos a Bruno Sato. Agora ele pode começar. Tem a carta assinada por Marina Prado, com o *hash* conferido no chamado APR-2291. Tem escopo e janela por escrito, com as exclusões. Tem quem controla o exercício: o White Team, o *trusted agent* e a palavra de parada. E tem as regras para os dados, pela LGPD, e o registro de ações para a *deconfliction*. Então, respondendo à pergunta da aula: antes do primeiro sistema, precisam estar escritas e assinadas a autorização de quem tem autoridade e as regras de engajamento completas."

**Slides 18 e 19 — Pontos-chave e referências (19:20–19:45)**  
Fala: "Para levar desta aula: sem autorização expressa de quem tem autoridade, o teste pode configurar o crime do artigo 154-A; a RoE define objetivo, escopo e exclusões, janelas, técnicas proibidas, dados sensíveis, parada, White Team e contatos; a carta precisa ser a versão assinada, com integridade verificável; e a *deconfliction* separa o exercício de um incidente real, com a LGPD valendo o tempo todo. As referências estão no slide e no material da unidade."

**Slide 20 — Encerramento (19:45–20:00)**  
Fala: "Agora você sabe o que precisa estar no papel antes de uma operação de Red Team. Na próxima aula, vamos descrever o próprio ataque com precisão, usando o MITRE ATT&CK, suas táticas e técnicas, e montar um plano de emulação de adversário. Até lá!"  
[Tela: deck no slide de encerramento]

## Roteiro da Videoaula 3 — "Como 'o atacante entrou e se moveu' vira sete linhas de um plano?"

Duração-alvo: 15 a 20 minutos. Deck: unidade_1/slides/aula3.html (22 slides).

**Slides 1 e 2 — Capa e sumário (0:00–0:35)**  
Fala: "Olá! Nas duas primeiras aulas, montamos os papéis de um exercício e as regras que precisam estar assinadas antes de começar. Hoje vamos aprender a descrever o adversário com precisão: a Cyber Kill Chain, o MITRE ATT&CK e o plano de emulação, que transforma o comportamento de um grupo em passos que o Red Team executa e o Blue Team mede. São seis laboratórios, todos na Rede Tatame."  
[Tela: deck aberto no slide 1; avançar até o sumário]

**Slide 3 — O problema de hoje na Rede Tatame (0:35–1:45)**  
Fala: "O relatório do último teste da Rede Tatame tem uma frase só: 'o atacante entrou, se moveu e chegou aos dados'. Parece suficiente, mas não serve para nada. Bruno Sato, do Red Team, não sabe o que repetir no próximo exercício. Rafael Tavares, engenheiro de detecção, não sabe que regra escrever. E agora chegou o boletim de inteligência BI-2026-041: o Grupo Cobalto Austral, um grupo fictício de *ransomware*, entra com senha vazada na VPN, anda pelos servidores da sede e cifra tudo. Em jogo estão as exportações de fichas de alunos no SRV-ARQ-01. A pergunta da aula está em amarelo: como descrever o ataque com precisão suficiente para o Red Team emular e o Blue Team medir? Guarde os nomes de baixo: Bruno, Rafael e Marina Prado, que vai aprovar o plano pelo White Team."  
Fala (apontando o mapa): "No mapa, o caminho vermelho é o trajeto do grupo: da internet para a VPN, da VPN para o Active Directory e dali para o servidor de arquivos, em vermelho."  
[Take de apoio: equipe lendo um relatório curto em uma sala de reunião, com expressão de dúvida — Envato]

**Slide 4 — A Cyber Kill Chain e onde ela não alcança (1:45–2:40)**  
Fala: "O primeiro modelo para organizar um ataque veio em 2011, de pesquisadores da Lockheed Martin: a Cyber Kill Chain, com sete fases. Reconhecimento, armamento, entrega, exploração, instalação, comando e controle e, por fim, ações sobre os objetivos. A grande ideia está no quadro azul: o defensor não precisa vencer em todas as fases; basta interromper uma. Mas o modelo é linear e foi pensado para *malware* entregue de fora para dentro. O Cobalto Austral entra com uma senha vazada na VPN: não há armamento nem instalação. A Kill Chain diz em que fase estamos, mas não diz que comportamento procurar."

**Slide 5 — Visualização 3D: a cadeia e o ponto de corte (2:40–3:35)**  
Objetivo: ver que basta cortar uma fase para o ataque falhar, e o que o modelo não diz.  
Na tela:  
1. Deixar a cena rodar alguns segundos em "Sem defesa": a esfera branca percorre as sete fases.  
2. Clicar em "3", no canto da cena, e ler a legenda.  
3. Clicar em "6" e ler a legenda.  
4. Clicar em "Sem defesa".  
Fala: "Cada cubo vermelho é uma fase, e a esfera branca é o ataque andando pela cadeia. Quando ponho a defesa na fase 3, a entrega, aparece o escudo azul, as fases seguintes se apagam e a legenda mostra o controle: filtro de *e-mail* com *sandbox* de anexos. Na fase 6, comando e controle, o corte também funciona, com DNS e *proxy* revelando contato com um domínio recém-registrado. Mas repare: aí o atacante já está dentro da rede."  
Atenção: a cena depende de conexão com a internet para carregar a biblioteca 3D. Arrastar gira a cena; a roda do *mouse* aproxima.  
Conclusão: "A fase diz onde cortar, mas não diz qual comportamento procurar. Para isso, precisamos de um vocabulário mais fino."  
[Tela: gravação do laboratório do slide 5]

**Slide 6 — MITRE ATT&CK: o vocabulário do comportamento adversário (3:35–4:35)**  
Fala: "Esse vocabulário é o MITRE ATT&CK, uma base pública mantida pela MITRE, organização sem fins lucrativos, construída a partir de ataques reais. Ele tem três níveis. As táticas, com IDs que começam com TA, são o porquê: o objetivo do atacante naquele momento. A matriz Enterprise tem 15 táticas. A décima quinta é recente: na versão 19, de abril de 2026, a antiga Evasão de defesas foi dividida em Furtividade, que manteve o ID TA0005, e Enfraquecimento de defesas, a TA0112. As técnicas e subtécnicas, com IDs que começam com T, são o como: T1566 é *Phishing*; T1566.002, o *phishing* com *link*. E os procedimentos são a implementação concreta de um grupo. Cada técnica traz ainda as mitigações, com IDs M, os grupos que a usaram e como detectá-la."

**Slide 7 — O ataque do Cobalto Austral em técnicas (4:35–5:25)**  
Fala: "Veja como a frase vaga do relatório ganha precisão. 'Entrou' vira Acesso inicial, T1078, contas válidas, e o rastro que a defesa procura é um *login* sem MFA na VPN. 'Se moveu' se desdobra em três técnicas: Descoberta, T1087.002, uma consulta em massa ao Active Directory; Movimentação lateral, T1021.001, um *logon* RDP de uma estação para um servidor; e Acesso a credenciais, T1003, a leitura da memória do processo LSASS. E 'chegou aos dados' termina em Impacto, T1486, muitos arquivos renomeados em minutos. Cada linha diz ao Red Team o que fazer e ao Blue Team onde olhar."

**Slide 8 — Laboratório: a técnica T1078 na base ATT&CK (5:25–7:05)**  
Objetivo: ler a técnica de entrada do Cobalto Austral pelos olhos do Red e do Blue Team.  
Na tela:  
1. Ler a aba "Descrição", que já está aberta.  
2. Clicar em "Subtécnicas".  
3. Clicar em "Mitigações".  
4. Clicar em "Detecção".  
5. Clicar em "Red x Blue".  
Fala (descrição): "Esta é uma reprodução simplificada da página T1078, *Valid Accounts*, contas válidas. Repare no cabeçalho: a mesma técnica serve a quatro táticas, de Acesso inicial a Furtividade. Faz sentido: uma conta legítima ajuda a entrar, a ficar, a ganhar privilégio e a passar despercebido."  
Fala (subtécnicas e mitigações): "São quatro subtécnicas: contas padrão, de domínio, locais e de nuvem. Nas mitigações, a principal para o nosso caso é a M1032, autenticação multifator: com MFA em todas as contas da VPN, a senha vazada sozinha não basta. Ao lado, políticas de senha, gestão de contas privilegiadas e treinamento."  
Fala (detecção): "Na aba Detecção está a fonte que mostra o rastro: a auditoria de identidade da Rede Tatame, onde a regra R11 alerta *login* sem MFA. Os *logs* da VPN e do AD completam a visão."  
Fala (Red x Blue): "E a aba que resume a aula. Do lado vermelho, o procedimento seguro do Red Team: *login* com a conta de teste svc-purple, criada para o exercício e aprovada pelo White Team, com IP e hora registrados para a *deconfliction*. Do lado azul, a pergunta do Blue Team: a R11 está ligada e chega ao SOC? E a medida: o tempo do *login* até o alerta."  
Atenção: a página é uma reprodução didática; no *site* oficial, a seção *Procedure Examples* lista os grupos reais que usaram a técnica.  
Conclusão: "A mesma página diz ao Red Team o que emular e ao Blue Team o que procurar."  
[Tela: gravação do laboratório do slide 8]

**Slide 9 — Emular é diferente de simular (7:05–8:00)**  
Fala: "Agora a diferença entre dois verbos. Emular é reproduzir o comportamento de um grupo específico, conhecido por inteligência de ameaças, na ordem e do jeito que ele age. A pergunta é: e se aquele grupo nos atacasse? Simular é executar técnicas genéricas, sem fidelidade a um ator. Há apoio para isso: a *Adversary Emulation Library*, do MITRE Center for Threat-Informed Defense, publica planos de grupos documentados, e ferramentas como Caldera e Atomic Red Team automatizam testes mapeados no ATT&CK. O documento que organiza tudo é o plano de emulação: o White Team aprova, e Red e Blue usam como roteiro comum."

**Slide 10 — Laboratório: o plano de emulação, passo a passo (8:00–9:55)**  
Objetivo: montar o plano de emulação do Cobalto Austral nos sete passos.  
Na tela:  
1. O passo "Sete passos até o plano" já está na tela ao abrir o slide.  
2. Clicar em "▶ Avançar" para cada passo, de "1 · Perfil do adversário" a "7 · Aprovação pelo White Team".  
3. Avançar para "O plano vira uma camada" (contador 9 / 9).  
Fala: "Cada caixa é um passo, e o White Team só assina quando os sete estão completos. Primeiro, o perfil do adversário: Cobalto Austral, extorsão com *ransomware* e dados de alunos, segundo o boletim BI-2026-041. Segundo, o objetivo da emulação, uma pergunta que dá para responder: o SOC percebe a cadeia antes da cópia das fichas? Terceiro, a sequência de técnicas: as cinco da tabela, mais duas que o boletim cita, T1567.002, a cópia de dados para um serviço de nuvem, e T1490, a destruição das cópias de sombra, que impede a recuperação. Quarto, e muito importante, o procedimento seguro: conta de teste, arquivos fictícios, *bucket* de teste e máquina virtual descartável. O impacto é só simulado; nenhum dado real é cifrado ou copiado. Quinto, a telemetria e a regra esperadas para cada técnica; por exemplo, para a T1087.002, os *logs* do AD e a regra R13. Sexto, os critérios: sucesso é cada técnica executada e registrada, com ou sem alerta; a parada segue a RoE da aula passada. Sétimo, Marina Prado confere o plano contra a RoE e assina o chamado APR-3107. Por fim, o plano vira uma camada do ATT&CK Navigator."  
Atenção: o botão "⏯ Auto" avança sozinho; para gravar, prefira "▶ Avançar". A seta "◀" volta um passo.  
Conclusão: "Um plano de emulação liga cada técnica a um procedimento seguro, à telemetria e à regra esperadas."  
[Tela: gravação do laboratório do slide 10]

**Slide 11 — O plano em camadas (9:55–10:35)**  
Fala: "O ATT&CK Navigator é a ferramenta *web* gratuita da MITRE para anotar a matriz. Cada anotação é uma camada, um arquivo JSON que lista técnicas com pontuação, o *score*, uma cor e um comentário. No planejamento, usamos três: a camada do plano, com as técnicas do adversário; a camada de cobertura, com o que a defesa detecta hoje; e a sobreposição das duas, que mostra onde o exercício vai encontrar lacunas. Depois da execução, uma quarta registra o resultado. Vamos abrir as três."

**Slide 12 — Laboratório: três camadas no ATT&CK Navigator (10:35–12:25)**  
Objetivo: ver onde o plano encontra lacunas.  
Na tela:  
1. A aba "Plano Cobalto Austral" abre selecionada.  
2. Clicar em "Ocultar não anotadas"; clicar de novo para mostrar tudo.  
3. Clicar na aba "Cobertura atual".  
4. Clicar na aba "Plano × cobertura" e, depois, na célula T1567.002.  
5. Clicar em "{ } Ver JSON da camada"; clicar de novo para fechar.  
Fala (plano): "Esta é uma matriz reduzida, com as 15 táticas da versão 19 na ordem certa, de Reconhecimento a Impacto, e três ou quatro técnicas em cada uma. Em lilás, as sete técnicas do plano, espalhadas por seis táticas. Com 'Ocultar não anotadas', o resto da matriz se apaga e a cadeia salta aos olhos."  
Fala (cobertura): "A camada de cobertura é outra coisa: o que a Rede Tatame detecta hoje, com ou sem o Cobalto Austral. Verde é regra ativa, *score* 100. Amarelo é telemetria sem regra, *score* 50. Vermelho é nem telemetria, *score* 0. Repare que há verdes fora do plano, como o *phishing* e o *credential stuffing*: a defesa também cobre outros adversários."  
Fala (sobreposição): "Agora a camada que interessa: só as técnicas do plano, pintadas com a cobertura. Três verdes, T1078, T1003 e T1490. Três amarelas, a descoberta no AD, o RDP e a criptografia. E uma vermelha, a T1567.002. Clicando nela, o rodapé mostra o comentário: a fonte de saída de rede está desligada. Os indicadores no topo resumem: 3 detectadas de 7, e visibilidade de 6 de 7."  
Fala (JSON): "E este é o arquivo por trás da camada: nome, domínio enterprise-attack, versão do formato e a lista de técnicas, cada uma com tática, *score*, cor e comentário. É esse JSON que se troca entre as equipes."  
Atenção: é uma reprodução didática do Navigator, com a matriz reduzida. Clique fora das células para não deixar uma técnica selecionada ao trocar de camada.  
Conclusão: "A sobreposição diz, antes da execução, onde o exercício vai encontrar lacunas."  
[Tela: gravação do laboratório do slide 12]

**Slide 13 — Antes do código: onde achar e como instalar (12:25–13:05)**  
Fala: "Antes de abrir o editor, o que o laboratório usa. O Visual Studio Code vem de code.visualstudio.com, e a extensão Python da Microsoft se instala pela aba Extensões. O Python 3.12 vem de python.org; os módulos json e sys já vêm com ele. O único pacote de terceiros é o PyYAML, que lê os arquivos do plano. E o ATT&CK Navigator não precisa de instalação: roda no navegador. No quadro azul, dois cuidados. No PyPI, confira o nome letra por letra: o pacote é PyYAML, e o módulo importado se chama yaml. Pacotes de nome parecido são uma forma conhecida de trazer código malicioso, o *typosquatting*. E camadas com dados da empresa só vão para o Navigator oficial, no GitHub da MITRE."

**Slide 14 — Laboratório: o plano cruzado com a defesa, em Python (13:05–15:00)**  
Objetivo: gerar a camada "plano × cobertura" a partir de arquivos, sem pintar à mão.  
Tela cheia: o VS Code ocupa o slide inteiro, sem cabeçalho nem painel lateral. O roteiro do laboratório (Objetivo, Faça, Observe e Conclusão) abre e fecha com a tecla G ou com o botão "☰ Roteiro", na barra de status do VS Code. Deixe-o fechado durante a gravação.  
Na tela:  
1. Ao abrir o slide, o arquivo plano/cobalto-austral.yaml é digitado sozinho; esperar terminar.  
2. Clicar em "⬇ Preparar o ambiente" e esperar "✓ Ambiente pronto".  
3. Mostrar no plano as linhas destacadas (6 a 10), da técnica T1078.  
4. Abrir defesa_atual.yaml no explorador de arquivos.  
5. Abrir gerar_layer.py e mostrar as linhas destacadas (16 a 19).  
6. Clicar em "Executar gerar_layer.py".  
7. Clicar em "Com R13 e R5 ligadas".  
Fala (preparação): "O terminal confere o Python 3.12, cria o ambiente virtual, ativa e instala o que está no requirements.txt: só o PyYAML, na versão 6.0.3. O pip list confirma: pip e PyYAML, nada mais."  
Fala (arquivos): "O plano é o mesmo do laboratório anterior, agora em YAML: o adversário, o objetivo e as sete técnicas. Em cada uma, nas linhas destacadas, o ID, a tática, o procedimento seguro, a fonte de dados e a regra esperada. O defesa_atual.yaml descreve a Rede Tatame hoje: quais fontes estão ligadas, e a fonte de nuvem não está, e quais regras estão ativas. R13 e R5 estão desligadas."  
Fala (código): "O coração do código está nas linhas destacadas, a função estado. Se a fonte da técnica está desligada, a técnica é cega. Se a fonte está ligada e a regra está ativa, é detectada. Se só a fonte está ligada, é parcial. Depois o código monta a camada com *score*, cor e comentário e grava o JSON na pasta layers."  
Fala (execução): "Resultado: três detectadas em verde, três parciais em amarelo e a T1567.002 cega, em vermelho. Cobertura esperada: 3 de 7, 42,9%. Visibilidade: 6 de 7, 85,7%. A camada foi gravada em layers/plano-x-cobertura.json."  
Fala (com R13 e R5): "Agora a mesma conta com as regras R13 e R5 ligadas, que usam *logs* do AD que já existem. A descoberta e o RDP passam a detectadas: 5 de 7, 71,4%, sem nenhuma fonte nova. A T1567.002 continua cega: essa exige ligar a fonte de saída de rede. A última linha, em roxo, mostra como abrir o arquivo no Navigator: *Open Existing Layer*, *Upload from local*."  
Atenção: a saída do Python usa ponto decimal (42.9%); na fala, diga "42,9%". A preparação do ambiente é simulada e leva cerca de 10 segundos; os outros botões ficam travados até aparecer "Ambiente pronto". Para mostrar o código sendo escrito, use "⌨ Digitar ao vivo".  
Conclusão: "Ligar regras onde a telemetria já existe é o caminho mais barato."  
[Tela: gravação do laboratório do slide 14]

**Slide 15 — Laboratório: o plano do Cobalto Austral na plataforma (15:00–16:35)**  
Objetivo: conferir, passo a passo, o que a camada previu.  
Na tela:  
1. A plataforma abre na aba "Cenários". Trocar a velocidade para "1 s = 1 min".  
2. No cartão "Emulação do Grupo Cobalto Austral", clicar em "Iniciar cenário" e não conter nada.  
3. Se aparecer um alerta de comportamento conhecido, marcar "Falso positivo".  
4. Ao final, abrir a aba "Cobertura ATT&CK".  
5. Abrir "Regras do CEP", ligar R13 e R5, voltar a "Cenários" e clicar em "Repetir com as fontes e regras atuais".  
6. Abrir de novo "Cobertura ATT&CK".  
Fala (execução): "Esta é a plataforma da disciplina. O cenário reproduz a cadeia do grupo. A R11 dispara logo no início, no *login* sem MFA. Depois vêm a consulta ao AD e o RDP para o SRV-ARQ-01: repare que esses passos aparecem em amarelo, vistos nos *logs*, sem alerta. A leitura do LSASS dispara a R6. A cópia de 4,2 GB para a nuvem aparece em vermelho, não detectada. A destruição das cópias de sombra dispara a R7, e a criptografia fecha a cadeia sem regra."  
Fala (cobertura): "Na aba Cobertura, cada técnica tem um estado: comprovada, quando a regra existe e já foi testada com sucesso; detectável; parcial; ou cega. É o mesmo retrato da camada que o *script* gerou."  
Fala (reteste): "Agora o reteste. Ligo R13 e R5 nas regras do CEP e repito o cenário com as fontes e regras atuais. A descoberta e o RDP passam a gerar alerta, e na Cobertura saem de parcial. A cópia de dados continua cega."  
Atenção: em "1 s = 1 min", o cenário completo leva menos de 20 segundos reais. Se quiser mostrar a contenção, clique em "Investigar" e depois em "Conter" no primeiro alerta, no SOC; os passos seguintes aparecem como "interrompido pela contenção". "Reiniciar" restaura as fontes e regras padrão.  
Conclusão: "A plataforma confirma a camada: a cópia de dados é a lacuna que exige uma fonte nova."  
[Tela: gravação do laboratório do slide 15]

**Slide 16 — Pausa para reflexão: a cooperativa que quer "testar tudo do ATT&CK" (16:35–17:15)**  
Fala: "Hora de parar e pensar. Uma cooperativa de crédito quer 'testar tudo do ATT&CK'. O SOC tem 3 analistas, e a operação dura 3 semanas. A inteligência indica que o grupo que ataca o setor entra por credenciais válidas de VPN, consulta o Active Directory e exfiltra dados antes de cifrar os servidores. Três perguntas: por que 'testar tudo' é um mau objetivo? Que cinco técnicas você colocaria no plano, e em que ordem? E que procedimento seguro você proporia para a técnica de impacto? O desafio prático é montar esse plano em uma página. Pause o vídeo e tente antes de seguir."  
[Tela: manter o slide 16 por 5 segundos]

**Slide 17 — Uma resolução possível (17:15–17:55)**  
Fala: "Uma resposta possível. Primeiro: são centenas de técnicas e três analistas; o exercício viraria uma simulação genérica e não responderia à pergunta 'e se aquele grupo nos atacasse?'. Segundo, na ordem da cadeia: T1078, contas válidas na VPN; T1087.002, contas de domínio; T1021.001, RDP; T1567.002, exfiltração para a nuvem; e T1486, criptografia. Terceiro, para o impacto: renomear arquivos fictícios em uma pasta de teste ou em máquina virtual descartável, nunca cifrar dados reais. Outras escolhas valem quando justificadas pela inteligência, como incluir a T1490 antes do impacto."

**Slide 18 — Exemplo numérico: a cobertura do plano (17:55–18:30)**  
Fala: "Vamos fixar a conta. O plano tem 7 técnicas. Três têm regra ativa: T1078, T1003 e T1490. Três têm só telemetria: T1087.002, T1021.001 e T1486. Uma não tem telemetria: T1567.002. A cobertura esperada é 3 dividido por 7, cerca de 42,9%. A visibilidade, quem tem pelo menos telemetria, é 6 dividido por 7, cerca de 85,7%. Criando as regras da descoberta e do RDP, que já têm telemetria, a cobertura sobe para 5 de 7, cerca de 71,4%, sem o custo de uma fonte nova."

**Slide 19 — De volta ao problema (18:30–19:05)**  
Fala: "Voltemos à frase 'o atacante entrou, se moveu e chegou aos dados'. Com o ATT&CK, ela virou sete técnicas, de T1078 a T1486, com tática e ID. No plano aprovado por Marina, cada técnica tem procedimento seguro, telemetria e regra esperadas. A camada mostra 3 de 7 detectadas, 3 parciais e a cópia de dados cega. E a ordem do trabalho está clara: ligar R13 e R5 leva a 71,4%, e a cópia de dados exige a fonte de saída de rede. A resposta à pergunta da aula está em amarelo: descrever o ataque como um plano de emulação em técnicas ATT&CK e registrar plano, cobertura e resultado em camadas do Navigator."

**Slides 20 e 21 — Pontos-chave e referências (19:05–19:30)**  
Fala: "Para levar desta aula: a Kill Chain mostra que interromper uma fase basta, e o ATT&CK dá o detalhe para planejar e medir. Táticas são o porquê; técnicas, o como; procedimentos, a implementação de um grupo. O plano de emulação liga cada técnica a um procedimento seguro, à telemetria e à regra esperadas. E o Navigator registra tudo em camadas comparáveis. As referências estão no slide e no texto da aula."  
[Tela: avançar do slide 20 para o 21 e manter 3 segundos]

**Slide 22 — Encerramento (19:30–19:45)**  
Fala: "Você já descreve um adversário em táticas e técnicas, monta um plano de emulação e lê a cobertura em camadas. Mas por que o Cobalto Austral, e não outro grupo? Na próxima aula, a Aula 4, vamos usar a inteligência de ameaças para escolher o adversário e decidir por onde começar. Até lá!"  
[Tela: slide de encerramento por 3 segundos]

## Roteiro da Videoaula 4 — "300 IPs, 150 hashes e uma pergunta: por onde começar?"

Duração-alvo: 15 a 20 minutos. Deck: unidade_1/slides/aula4.html (21 slides).

**Slides 1 e 2 — Capa e sumário (0:00–0:35)**  
Fala: "Olá! Esta é a última aula da Unidade 1. Até aqui, você montou uma operação com papéis, regras e autorização e aprendeu a descrever o adversário no ATT&CK. Falta uma decisão: qual adversário emular e por quais técnicas começar. Hoje vamos usar a inteligência de ameaças para responder a isso, com seis laboratórios na Rede Tatame."  
[Tela: deck aberto no slide 1; avançar até o sumário]

**Slide 3 — O problema de hoje na Rede Tatame (0:35–1:50)**  
Fala: "A Rede Tatame participa de uma rede setorial de segurança, um grupo de empresas que trocam informações sobre ameaças. Essa rede publicou o boletim BI-2026-041: o Grupo Cobalto Austral, um grupo fictício de *ransomware*, atacou outras redes de academias. O boletim traz 300 endereços IP, 150 *hashes* de arquivos e só três parágrafos sobre o comportamento do grupo. Bruno Sato, que lidera o Red Team, tem vagas para poucas técnicas na primeira rodada da operação e precisa decidir por onde começar. O que está em jogo são as exportações de fichas de alunos no SRV-ARQ-01 e a chance de o exercício testar o que de fato ameaça a empresa. A pergunta da aula está em amarelo: como transformar um relatório de ameaça em prioridades para a operação de Red Team da Rede Tatame?"  
Fala (apontando o mapa): "No mapa, os destaques são a borda exposta: a VPN, o *e-mail* e a homologação hml-gestao. O caminho vermelho é o trajeto que o Cobalto Austral costuma fazer nas vítimas: da internet para a VPN, da VPN para o Active Directory e dali para o servidor de arquivos."  
[Take de apoio: analista lendo um relatório extenso em duas telas, com planilhas e listas de endereços — Envato]

**Slide 4 — Do dado à inteligência (1:50–2:40)**  
Fala: "A inteligência de ameaças, ou CTI, de *Cyber Threat Intelligence*, é a informação sobre adversários coletada, analisada e contextualizada para apoiar decisões. Uma lista de IPs, sozinha, é um dado. Ela vira inteligência quando responde a perguntas como: quem ameaça o nosso setor, com quais objetivos e de que forma? Essas perguntas, definidas com a liderança, se chamam requisitos de inteligência. E o trabalho segue um ciclo: direção, coleta, processamento, análise, disseminação e *feedback*. No planejamento de uma operação, o produto desse ciclo é a resposta a uma pergunta bem prática: qual adversário emular e por onde começar."

**Slide 5 — Laboratório: o ciclo de inteligência aplicado ao boletim (2:40–4:20)**  
Objetivo: seguir o boletim BI-2026-041 pelas seis etapas do ciclo de inteligência.  
Na tela:  
1. O passo "O boletim BI-2026-041 chega" já está na tela ao abrir o slide.  
2. Clicar em "▶ Avançar" para cada passo seguinte, até "6 · Feedback" (contador 7/7).  
Fala: "Antes de abrir o arquivo, vem a pergunta: o que precisamos saber para planejar a operação? Primeiro passo, direção. Marina Prado, a CISO, e Bruno Sato definem os requisitos: o Cobalto Austral ameaça a Rede Tatame? Como ele entra? Que técnicas a nossa defesa ainda não vê? Segundo, coleta: o boletim da rede setorial, um alerta de um CERT parceiro, o relatório de resposta de outra rede de academias e fontes abertas sobre a própria Tatame. Terceiro, processamento: converter tudo para um formato comum, o STIX, eliminar repetições e separar os 450 indicadores das descrições de comportamento. Quarto, análise: montar o perfil do adversário, com motivação, vítimas e técnicas do ATT&CK. Quinto, disseminação: cada público recebe o seu nível. A diretoria recebe o risco estratégico; o White Team, o adversário e o cenário; o Red Team e Rafael Tavares, da detecção, recebem as técnicas. Repare na linha tracejada roxa: o nível tático vira o plano de emulação. E sexto, *feedback*: o resultado do exercício volta como resposta aos requisitos e gera as perguntas do próximo ciclo."  
Atenção: o botão "⏯ Auto" avança sozinho; para gravar, prefira "▶ Avançar", que deixa o ritmo com o professor.  
Conclusão: "O boletim só vira plano depois de passar pelas seis etapas, começando pelas perguntas certas."  
[Tela: gravação do laboratório do slide 5]

**Slide 6 — Três níveis, três usos no planejamento (4:20–5:15)**  
Fala: "A inteligência costuma ser dividida em três níveis, e cada um tem um uso no planejamento. A estratégica traz tendências e riscos, como a extorsão contra empresas que guardam dados de crianças. Ela vai para a diretoria e justifica o exercício e o orçamento. A operacional fala de campanhas e atores específicos, com intenções e capacidades. Ela vai para os líderes do SOC, do Red Team e do White Team e define qual adversário emular. A tática traz as TTPs, isto é, táticas, técnicas e procedimentos, e os indicadores. Ela vai para analistas e engenheiros de detecção e alimenta o plano técnica por técnica. O quadro azul lembra duas coisas: a nomenclatura varia entre autores, e no TIBER-EU, o arcabouço europeu de testes guiados por ameaças, um fornecedor de inteligência produz o relatório de ameaças antes de o Red Team montar os cenários."

**Slide 7 — A Pirâmide da Dor (5:15–6:05)**  
Fala: "Em 2013, David Bianco propôs a Pirâmide da Dor. A ideia é simples: quanto mais alto o indicador, mais difícil para o adversário trocá-lo. Na base estão os *hashes*: os 150 do boletim mudam se o grupo recompilar o arquivo, então trocá-los é trivial. Os 300 IPs, fácil: trocar de servidor leva minutos. Domínios, simples. Depois vêm os artefatos de rede e de *host*, como uma consulta LDAP em massa saindo de uma sessão de VPN: trocá-los já incomoda. Ferramentas, desafiador. E no topo, as TTPs, o comportamento em si: conta válida na VPN, descoberta no AD, RDP e cópia para a nuvem. Mudar isso obriga o grupo a mudar o jeito de trabalhar."

**Slide 8 — Visualização 3D: o que vale emular (6:05–7:05)**  
Objetivo: decidir que parte do boletim entra no plano de emulação.  
Na tela:  
1. Arrastar a cena para girar a pirâmide uma vez.  
2. Clicar nos botões dos seis níveis, de "Hashes" até "TTPs", parando dois ou três segundos em cada um.  
Fala: "Cada camada é um nível, do verde, barato para o adversário, ao vermelho, caro. Quando clico em *Hashes*, a camada sobe e a legenda mostra o exemplo do Cobalto Austral e o uso no plano: vai para o bloqueio, não para o plano. Endereços IP, a mesma coisa. Nos domínios, servem de pista, mas o exercício usa um domínio próprio. Em artefatos, a legenda diz: bom alvo de teste, porque mostra se a regra R13 funcionaria. Nas ferramentas, o plano usa um equivalente seguro, com arquivos fictícios. E no topo, as TTPs: é o que o plano de emulação reproduz."  
Atenção: se a cena 3D não carregar, aparece um texto alternativo com os seis níveis; a fala continua a mesma.  
Conclusão: "Repetir IPs e *hashes* não testa nada. O plano emula o topo da pirâmide."  
[Tela: gravação do laboratório do slide 8]

**Slide 9 — Modelo Diamante, STIX, TAXII, MISP e TLP (7:05–8:00)**  
Fala: "Para analisar e compartilhar inteligência, quatro siglas e um modelo aparecem sempre. O Modelo Diamante, de Caltagirone, Pendergast e Betz, descreve cada evento de intrusão por quatro vértices: adversário, capacidade, infraestrutura e vítima. Conhecendo um vértice, o analista 'pivota' para os outros. O STIX descreve objetos como atores, campanhas, padrões de ataque e relatórios. O TAXII define como trocar esses objetos entre organizações. O MISP é uma plataforma aberta que guarda e distribui eventos de inteligência. E o TLP 2.0, o *Traffic Light Protocol* mantido pelo FIRST, diz com que liberdade cada informação pode circular: CLEAR, GREEN, AMBER, AMBER+STRICT e RED."

**Slide 10 — Laboratório: o boletim na plataforma de CTI (8:00–9:45)**  
Objetivo: separar, no boletim, o que serve ao bloqueio e o que serve ao plano.  
Na tela:  
1. Mostrar o cabeçalho do evento 1187 e as etiquetas, com destaque para "tlp:amber".  
2. Na aba "Atributos", ler a frase dos 450 atributos e as primeiras linhas.  
3. Clicar na aba "ATT&CK".  
4. Clicar na aba "Diamante" e depois na caixa vermelha "Infraestrutura".  
5. Clicar na aba "Níveis" e em cada botão "Revelar".  
Fala: "Este é o evento 1187 no MISP da rede setorial. A etiqueta amarela, TLP:AMBER, diz que podemos usar a informação dentro da Rede Tatame, sem publicá-la. Na aba Atributos, 450 linhas: 300 IPs e 150 *hashes*. Agora a aba ATT&CK: oito técnicas, do acesso pela VPN à criptografia dos servidores. Oito linhas contra 450. Na aba Diamante, clico na infraestrutura para pivotar: o IP 198.51.100.12 aparece em *logins* na VPN de outras duas redes de academias, mas no SIEM da Rede Tatame não há nenhum *login* dele nos últimos 90 dias. Ou o grupo ainda não esteve aqui, ou já trocou de endereço. Por isso o plano emula o comportamento, e o IP vai só para o bloqueio. Por fim, a aba Níveis. 'O grupo ataca empresas que guardam dados de crianças': estratégica. 'Campanha ativa contra redes de academias desde outubro': operacional. 'Credencial válida na VPN, consulta ao AD, RDP, cópia para a nuvem': tática, e alimenta o plano. '300 IPs e 150 *hashes*': também tática, ou técnica, mas vai para o bloqueio."  
Atenção: os endereços 198.51.100.x e 192.0.2.x pertencem a faixas reservadas para documentação; os *hashes* aparecem abreviados de propósito.  
Conclusão: "As técnicas viram o plano; os indicadores vão para o bloqueio."  
[Tela: gravação do laboratório do slide 10]

**Slide 11 — Perfil do Grupo Cobalto Austral (9:45–10:35)**  
Fala: "Juntando as fontes, este é o perfil do adversário. Motivação: extorsão com *ransomware* e ameaça de publicar dados de alunos. Vítimas: redes de academias com VPN e dados pessoais. No acesso inicial, *phishing* ou credencial vazada em VPN sem MFA, que são T1566, T1078 e T1133. Na descoberta, consulta em massa ao Active Directory, T1087.002. Na movimentação lateral, RDP até os servidores da sede, T1021.001. Depois, leitura de credenciais da memória, T1003, cópia de dados para a nuvem, T1567.002, e, no impacto, exclusão das cópias de sombra e criptografia dos servidores, T1490 e T1486. Falta uma pergunta: esse perfil encaixa na Rede Tatame?"

**Slide 12 — Laboratório: a Rede Tatame vista pelo adversário (10:35–12:15)**  
Objetivo: conferir, só com fontes abertas, quais técnicas do perfil teriam chance contra a Rede Tatame.  
Na tela:  
1. Clicar em "▶ Próximo comando" cinco vezes, lendo a nota de cada passo antes da saída.  
Fala (comando 1): "Estou no notebook do Red Team, o NB-RED-002. O primeiro comando consulta o registro público do domínio, no registro .br. O contato técnico é Caio Mendes, e o *e-mail* revela o padrão nome.sobrenome@tatame.com.br. Isso serve para *phishing*, T1566."  
Fala (comando 2): "O segundo pergunta o servidor de *e-mail* a um resolvedor público. A resposta vem do provedor de DNS, não da Tatame: mx1.tatame.com.br."  
Fala (comando 3): "O terceiro consulta os logs públicos de transparência de certificados: todo certificado emitido para o domínio fica registrado. Aparecem a VPN, com nome público, que é um serviço remoto externo, T1133, e o hml-gestao, que tem certificado mas não está no inventário da TI."  
Fala (comando 4): "O quarto abre anotações feitas a partir de vagas e perfis profissionais públicos: uma vaga de infraestrutura cita VPN NetGuard, Active Directory e RDP. Atenção: isso é dado pessoal. Fica no cofre do exercício e é descartado ao final, como manda a LGPD."  
Fala (comando 5): "E a conclusão: a VPN exposta é a entrada provável, o padrão de *e-mail* é a alternativa, e o RDP citado na vaga confirma a movimentação lateral. O hml-gestao fica registrado, e o White Team decide se ele entra no escopo. Repare na última linha: nenhum serviço da Rede Tatame foi contatado nesta etapa."  
Atenção: todas as consultas são passivas e públicas; nenhuma varredura ou conexão ativa é feita contra a empresa. A varredura autorizada fica para a Unidade 2.  
Conclusão: "O perfil do grupo encaixa na superfície da Rede Tatame: T1133, T1078 e T1566 entram no plano."  
[Tela: gravação do laboratório do slide 12]

**Slide 13 — Exemplo numérico: relevância × lacuna (12:15–13:15)**  
Fala: "Agora a conta que organiza a decisão. Relevância vai de 1 a 3: a técnica aparece em 1, 2 ou 3 ou mais relatórios confiáveis. Lacuna também vai de 1 a 3: 1 quando há regra ativa, 2 quando só há telemetria e 3 quando não há telemetria nenhuma. A prioridade é o produto. A exfiltração para a nuvem, T1567.002, aparece nos três relatórios e não tem telemetria, porque a fonte de saída de rede está desligada: 3 vezes 3, prioridade 9. O RDP e a consulta a contas de domínio também aparecem nos três relatórios, mas têm telemetria sem regra: 3 vezes 2, prioridade 6 cada. As contas válidas, T1078, também são muito citadas, mas a regra R11 já está ligada: 3 vezes 1, prioridade 3. Com 4 vagas na primeira rodada, o plano começa por T1567.002, T1021.001 e T1087.002. A quarta vaga vai para a próxima da lista, e T1078 fica como teste de confirmação da regra R11 na rodada seguinte."

**Slide 14 — Antes do código: onde achar e como instalar (13:15–13:55)**  
Fala: "Antes de abrir o editor, vamos ver o que o laboratório usa. O Visual Studio Code vem de code.visualstudio.com. O Python 3.12, de python.org. A extensão Python da Microsoft se instala pela aba Extensões. E os módulos json, csv e collections fazem parte da biblioteca padrão: já vêm com o Python, nada a instalar. No quadro azul, um cuidado de segurança: confira na documentação oficial se o módulo já vem com o Python. Instalar 'por garantia' um pacote de nome parecido é um jeito conhecido de trazer código malicioso para a máquina; o nome do golpe é *typosquatting*."

**Slide 15 — Laboratório: do boletim STIX às prioridades do plano (13:55–15:40)**  
Objetivo: calcular, a partir do boletim e da cobertura atual, as técnicas da primeira rodada.  
Tela cheia: o VS Code ocupa o slide inteiro, sem cabeçalho nem painel lateral. O roteiro do laboratório (Objetivo, Faça, Observe e Conclusão) abre e fecha com a tecla G ou com o botão "☰ Roteiro", na barra de status do VS Code. Deixe-o fechado durante a gravação.  
Na tela:  
1. Clicar em "⬇ Preparar o ambiente" e esperar "✓ Ambiente pronto".  
2. Abrir boletim_BI-2026-041.json no explorador de arquivos.  
3. Abrir cobertura_tatame.csv.  
4. Voltar a priorizar.py e mostrar as linhas destacadas (21 a 23).  
5. Clicar em "Executar priorizar.py".  
Fala (preparação): "O terminal confere a versão do Python, cria o ambiente virtual, ativa e testa os três módulos. O pip list mostra só o próprio pip: este laboratório usa apenas a biblioteca padrão."  
Fala (arquivos): "O boletim está em STIX: um conjunto de objetos com o grupo, nove padrões de ataque e três relatórios. Cada relatório lista as técnicas que cita. A planilha de cobertura traz, para cada técnica, a regra, a fonte e a lacuna, de 1 a 3."  
Fala (código): "O código lê os dois arquivos e conta em quantos relatórios cada técnica aparece. Nas linhas destacadas está o coração da conta: relevância limitada a 3, vezes a lacuna, e a ordenação da maior prioridade para a menor. No fim, o código soma os indicadores que ficam fora do plano e imprime a tabela."  
Fala (execução): "Resultado: 3 relatórios, 9 técnicas e 450 indicadores fora do plano. No topo, T1567.002 com 9. Depois T1021.001 e T1087.002 com 6. A quarta vaga vai para T1486, a criptografia, com 4: aparece em dois relatórios e não tem regra. T1078 fica com 3, fora da primeira rodada."  
Atenção: a preparação do ambiente é simulada e leva cerca de 10 segundos; os outros botões ficam travados até aparecer "Ambiente pronto". Se quiser mostrar o código sendo escrito, use "⌨ Digitar ao vivo".  
Conclusão: "A prioridade sai de uma conta que o White Team pode conferir."  
[Tela: gravação do laboratório do slide 15]

**Slide 16 — Laboratório: o perfil do adversário contra a plataforma (15:40–16:50)**  
Objetivo: confirmar na plataforma a exposição e as lacunas que o plano vai testar.  
Na tela:  
1. A plataforma abre na aba "8 Superfície". Marcar "ordenar por risco", se não estiver marcado.  
2. Apontar as linhas de vpn.tatame.com.br e de hml-gestao.tatame.com.br.  
3. Clicar na aba "9 Cobertura ATT&CK" e localizar T1078, T1087.002, T1021.001, T1567.002 e T1486.  
Fala (superfície): "Esta é a plataforma da disciplina, com a Rede Tatame inteira. Na aba Superfície, ordenada por risco, a VPN NetGuard está no topo: falha crítica, presente no catálogo KEV de vulnerabilidades exploradas, risco 43,8. Logo abaixo, o hml-gestao, que não está no inventário e não passa pelo WAF. É exatamente a borda que o Cobalto Austral procura."  
Fala (cobertura): "Na aba Cobertura, cada técnica tem um estado. T1567.002 está cega: a fonte de saída de rede está desligada. T1087.002 e T1021.001 estão parciais: há logs do AD, mas as regras R13 e R5 estão desligadas. T1486 também é parcial: o EDR vê, mas não há regra. E T1078 aparece como detectável, porque a R11 está ligada. É o mesmo retrato da planilha que o script usou."  
Atenção: a plataforma é reiniciada ao abrir o slide; não é preciso clicar em "Iniciar" para ler as abas Superfície e Cobertura.  
Conclusão: "A plataforma confirma a lacuna que a conta apontou."  
[Tela: gravação do laboratório do slide 16]

**Slide 17 — De volta ao problema (16:50–17:35)**  
Fala: "Voltemos a Bruno e ao boletim de 450 indicadores. O ciclo de inteligência, guiado pelos requisitos de Marina e Bruno, organizou a coleta, a análise e a entrega. A Pirâmide da Dor separou o que vai para o bloqueio, os indicadores, do que vai para o plano, as oito técnicas. O olhar do adversário, só com fontes abertas, mostrou a VPN exposta, o padrão de *e-mail* e um subdomínio fora do inventário. E a conta de relevância vezes lacuna pôs T1567.002, T1021.001, T1087.002 e T1486 na primeira rodada. A resposta à pergunta da aula está em amarelo: a Rede Tatame transforma o relatório em prioridades analisando o comportamento do adversário, conferindo a própria exposição com fontes abertas e cruzando a relevância de cada técnica com a lacuna da defesa."

**Slide 18 — O que você verá na próxima unidade (17:35–18:10)**  
Fala: "Na Unidade 2, Técnicas Ofensivas em Ambiente Controlado, o plano sai do papel, sempre em laboratório e dentro da carta de autorização. Na Aula 5, reconhecimento e enumeração de serviços e usuários, com Kali Linux e Wireshark. Na Aula 6, exploração de vulnerabilidades e acesso inicial, com os módulos de verificação do Metasploit. Na Aula 7, escalada de privilégios, movimentação lateral e persistência. E na Aula 8, evasão básica de defesas e limpeza de rastros, vistas pelo rastro que deixam na telemetria do defensor. Em todas, a mesma pergunta: que rastro a técnica deixa para o Blue Team?"

**Slides 19 e 20 — Pontos-chave e referências (18:10–18:40)**  
Fala: "Para levar desta aula: CTI é informação contextualizada para decisão, guiada por requisitos e produzida em ciclo. O nível estratégico justifica o exercício, o operacional escolhe o adversário e o tático alimenta o plano. Pela Pirâmide da Dor, emular TTPs testa a defesa; repetir IPs e *hashes*, não. E relevância vezes lacuna transforma um relatório de ameaça em prioridades. As referências estão no slide e no texto da aula."  
[Tela: avançar do slide 19 para o 20 e manter 3 segundos]

**Slide 21 — Encerramento (18:40–19:00)**  
Fala: "Você fechou a Unidade 1: já sabe montar uma operação com papéis, regras e autorização, descrever o adversário no ATT&CK e usar a inteligência de ameaças para decidir por onde começar. Na próxima aula, a Aula 5, começamos o reconhecimento e a enumeração de serviços e usuários. Até lá!"  
[Tela: slide de encerramento por 3 segundos]
