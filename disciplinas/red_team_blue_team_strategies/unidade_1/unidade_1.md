# Unidade 1 — Fundamentos: ataque e defesa como estratégia

Disciplina: Red Team & Blue Team Strategies  
Professor-conteudista: Afonso Cesar Lelis Brandão  
Prazo de entrega: 02/12/2026  
Template de origem: `documentos/Unidade 1/TEMPLATE - Unidade 1_nome da disciplina.docx`

> Versão de trabalho baseada na **ementa proposta** (`EMENTA.md`); ajustar quando o plano de aprendizagem oficial chegar.
> Recursos visuais indicados entre colchetes, como pede o template; a equipe de produção substitui pelas imagens finais.

## Relação da disciplina com a atuação profissional

Toda organização que depende de sistemas digitais — de um hospital a uma fintech, de uma indústria a um órgão público — está, neste momento, sendo observada por alguém que procura uma brecha. Ataques de *ransomware*, vazamentos de dados pessoais e fraudes por engenharia social deixaram de ser notícia rara e passaram a fazer parte do risco operacional cotidiano. Diante disso, as empresas perceberam que não basta comprar ferramentas de proteção: é preciso **testar** se elas funcionam e **treinar** as pessoas que as operam.

É exatamente aí que entram as estratégias de Red Team e Blue Team. O Red Team simula, de forma autorizada e controlada, o comportamento de um adversário real para descobrir como ele chegaria aos ativos críticos. O Blue Team protege, monitora, detecta e responde. Quando as duas equipes trabalham juntas, no chamado *purple teaming*, cada ataque simulado vira uma lição concreta para fortalecer a defesa.

Essa lógica está presente em vagas de analista de SOC, analista de segurança, *pentester*, engenheiro de detecção, especialista em resposta a incidentes e consultor de GRC (governança, risco e conformidade). Ela também é exigida por reguladores: o setor financeiro, por exemplo, adota programas de testes de intrusão baseados em inteligência de ameaças, como o europeu TIBER-EU, e a LGPD exige medidas técnicas aptas a proteger dados pessoais. Ao estudar esta disciplina, você desenvolverá o pensamento adversarial aplicado à defesa, a capacidade de planejar testes éticos e legais, de transformar evidências técnicas em decisões de negócio e de medir se a segurança da organização realmente está melhorando. Essas competências são um diferencial em um mercado que, ano após ano, aponta escassez de profissionais de cibersegurança.

## Roteiro do vídeo introdutório (até 2 minutos)

**Abertura (0:00–0:15)**  
"Olá! Eu sou o professor Afonso Brandão e seja muito bem-vindo, seja muito bem-vinda à disciplina Red Team & Blue Team Strategies! Se você quer entender como os ataques acontecem de verdade para conseguir defender uma empresa, você está no lugar certo!"

**Conexão com o mercado (0:15–0:45)**  
"Você já percebeu como quase toda semana aparece uma notícia de vazamento de dados ou de *ransomware* parando uma empresa? O que as organizações buscam hoje vai muito além de instalar antivírus e *firewall*. Elas querem profissionais que saibam pensar como o atacante e, ao mesmo tempo, detectar e responder rápido quando algo acontece."  
[Take de apoio: manchetes de incidentes de segurança e uma sala de SOC com telas de monitoramento — Envato]

**Conteúdo e diferencial (0:45–1:20)**  
"Durante a disciplina, você vai aprender a planejar simulações de ataque éticas e autorizadas, a usar o MITRE ATT&CK para mapear o comportamento de adversários, a montar a detecção e a resposta a incidentes e a unir as duas equipes no *purple teaming*. O grande diferencial? Cada conteúdo ofensivo vira uma melhoria defensiva. Tudo acontece na Rede Tatame, uma rede fictícia de academias de jiu-jitsu, com app, catracas e um SOC, que você vai atacar e defender em simulação no semestre inteiro."  
[Tela: gravação de 5 segundos do simulador da Rede Tatame, aba Arquitetura, com o cenário rodando]

**Benefícios (1:20–1:45)**  
"Ao final, você será capaz de conversar com a área técnica e com a diretoria sobre risco cibernético, com evidências. Além de usar as ferramentas, você vai entender como gerar impacto real na segurança das organizações."

**Chamada para ação (1:45–2:00)**  
"Então, se você quer estar preparado para os desafios da cibersegurança, essa disciplina é para você! Nos vemos nas aulas. Boa aula!"

## Aula 1 — Red, Blue e Purple Team: papéis, objetivos e ética

### O que você verá nesta unidade

Nesta primeira unidade, você vai construir a base conceitual de toda a disciplina. Vamos entender quem são as equipes Red, Blue e Purple, o que cada uma entrega e quais limites éticos e legais orientam o trabalho; aprender a pensar como um adversário por meio da Cyber Kill Chain e da matriz MITRE ATT&CK; diferenciar varredura de vulnerabilidades, teste de invasão e operação de Red Team; e conhecer os fundamentos da defesa organizada, com o NIST Cybersecurity Framework, a defesa em profundidade e o Centro de Operações de Segurança (SOC). O objetivo é que você saia desta unidade com um vocabulário comum e um modelo mental claro de como ataque e defesa se relacionam — algo indispensável para as unidades práticas que virão.

### Texto base

Imagine uma empresa de comércio eletrônico que investiu em *firewall*, antivírus e autenticação em dois fatores. A diretoria pergunta: "estamos seguros?". Ninguém consegue responder com evidências. As ferramentas estão instaladas, mas ninguém sabe se elas detectariam um ataque real, nem se a equipe saberia reagir. Essa pergunta sem resposta é o ponto de partida das estratégias de Red Team e Blue Team.

#### A origem militar dos termos

Os nomes vêm de exercícios militares de simulação, nos quais uma força "vermelha" fazia o papel do inimigo para testar os planos da força "azul". A ideia central permanece a mesma na cibersegurança: **só sabemos se uma defesa funciona quando ela é posta à prova por alguém que pensa como o adversário**.

[Imagem 1 — Ilustração de um tabuleiro de estratégia com peças vermelhas e azuis frente a frente. Texto alternativo: "Peças vermelhas e azuis em lados opostos de um tabuleiro, representando ataque e defesa". Sugestão de busca no Envato: "red vs blue strategy board".]

#### Red Team: o adversário autorizado

O Red Team é a equipe que **emula um adversário real**, de forma autorizada, com o objetivo de testar a capacidade da organização de prevenir, detectar e responder a ataques. Diferentemente de um teste que apenas lista falhas, a operação de Red Team persegue **objetivos** — por exemplo, "acessar a base de clientes" ou "obter privilégios de administrador do domínio" — e avalia até onde um atacante chegaria sem ser percebido. Seu principal entregável é um relatório que narra o caminho do ataque, as evidências coletadas e as recomendações de melhoria.

#### Blue Team: a defesa em operação

O Blue Team é responsável por **proteger, monitorar, detectar e responder**. Em geral, ele está no Centro de Operações de Segurança (SOC), analisando alertas, investigando comportamentos suspeitos, ajustando regras de detecção e conduzindo a resposta a incidentes. O Blue Team não trabalha apenas quando há um exercício: ele defende o ambiente todos os dias, contra ameaças reais.

#### Purple Team: a ponte entre ataque e defesa

O termo Purple Team (roxo, a mistura de vermelho e azul) designa menos uma equipe fixa e mais uma **forma de colaboração**. Em vez de o Red Team atacar e, semanas depois, entregar um relatório, as duas equipes trabalham lado a lado: o Red Team executa uma técnica, o Blue Team verifica se ela foi detectada e, se não foi, ambos ajustam a detecção imediatamente. Essa dinâmica acelera o aprendizado e será aprofundada na Unidade 4.

[Imagem 2 — Diagrama com três círculos (vermelho, azul e roxo na interseção) indicando: Red = emular adversário; Blue = proteger, detectar e responder; Purple = colaborar e melhorar continuamente. Texto alternativo: "Diagrama de Venn mostrando Red Team e Blue Team, com o Purple Team na interseção".]

| Aspecto | Red Team | Blue Team | Purple Team |
|---|---|---|---|
| Missão | Emular adversários | Proteger, detectar e responder | Integrar ataque e defesa |
| Pergunta central | "Até onde um atacante chegaria?" | "Percebemos e contivemos a tempo?" | "O que aprendemos e o que mudou?" |
| Entregável típico | Relatório de operação e caminho de ataque | Alertas, investigações, relatórios de incidente | Detecções novas ou ajustadas, métricas de cobertura |
| Ritmo | Por campanha ou exercício | Contínuo | Ciclos curtos e iterativos |

#### Ética e legalidade: o que separa um teste de um crime

Tecnicamente, muitas ações de um Red Team são idênticas às de um criminoso. O que as diferencia é a **autorização formal**. No Brasil, a Lei nº 12.737/2012 incluiu no Código Penal o art. 154-A, que tipifica a invasão de dispositivo informático; as penas foram agravadas pela Lei nº 14.155/2021. Por isso, nenhuma atividade ofensiva deve começar sem um documento assinado por quem tem autoridade sobre os ativos, definindo o **escopo** (o que pode ser testado), as **regras de engajamento** (como, quando e com quais limites) e os **contatos de emergência**.

Também é preciso respeitar a LGPD (Lei nº 13.709/2018): se o teste acessar dados pessoais, eles devem ser tratados com o mínimo de exposição, protegidos e descartados ao final. Um bom profissional ofensivo é, antes de tudo, alguém de confiança.

[Imagem 3 — Documento de autorização sendo assinado sobre uma mesa, com um *notebook* ao lado. Texto alternativo: "Pessoa assinando um documento de autorização de teste de segurança". Sugestão de busca no Envato: "signing contract laptop security".]

#### Um exemplo numérico: por que testar compensa

Suponha que um incidente grave custe, em média, R$ 6 milhões a uma empresa, e que a probabilidade anual estimada desse incidente seja de 15%. A **expectativa de perda anual** é de 0,15 × R$ 6.000.000 = **R$ 900.000**. Se um programa de Red Team e melhoria de detecção custar R$ 250.000 por ano e reduzir essa probabilidade para 6%, a nova expectativa de perda será 0,06 × R$ 6.000.000 = R$ 360.000. A redução de risco é de R$ 540.000 por ano — mais do que o dobro do investimento. Esse tipo de cálculo ajuda a traduzir segurança para a linguagem da diretoria.

#### Pontos-chave

- O Red Team emula adversários para testar prevenção, detecção e resposta.
- O Blue Team defende o ambiente de forma contínua.
- O Purple Team é a colaboração que transforma ataques simulados em melhorias.
- Sem autorização formal, escopo e regras de engajamento, um teste é crime.

### Referências da aula

BRASIL. Lei nº 12.737, de 30 de novembro de 2012. Dispõe sobre a tipificação criminal de delitos informáticos. *Diário Oficial da União*, Brasília, DF, 3 dez. 2012.

BRASIL. Lei nº 13.709, de 14 de agosto de 2018. Lei Geral de Proteção de Dados Pessoais (LGPD). *Diário Oficial da União*, Brasília, DF, 15 ago. 2018.

BRASIL. Lei nº 14.155, de 27 de maio de 2021. Altera o Código Penal para tornar mais graves os crimes de violação de dispositivo informático, furto e estelionato cometidos de forma eletrônica. *Diário Oficial da União*, Brasília, DF, 28 maio 2021.

EUROPEAN CENTRAL BANK. *TIBER-EU framework: how to implement the European framework for threat intelligence-based ethical red teaming*. Frankfurt: ECB, 2018.

### Roteiro da Videoaula 1 — "Contratamos alguém para nos invadir: e agora?"

Duração-alvo: 15 a 20 minutos. Deck: unidade_1/slides/aula1.html (18 slides).

**Slides 1 a 3 — Capa, audiodescrição e sumário (0:00–0:40)**  
Fala: "Olá! Nesta primeira aula, vamos conhecer os três papéis que dão nome à disciplina: Red Team, Blue Team e Purple Team. Você vai ver para que serve cada um, o que cada equipe entrega e o que separa um teste autorizado de um crime. A aula tem seis laboratórios, e todos usam a Rede Tatame, a empresa fictícia que vamos atacar e defender durante o semestre."  
[Tela: deck aberto no slide 1; avançar até o sumário sem ler a audiodescrição em voz alta]

**Slide 4 — O problema de hoje na Rede Tatame (0:40–2:10)**  
Fala: "Imagine a seguinte cena. A Rede Tatame tem 240 academias de jiu-jitsu e já comprou *firewall*, antivírus e autenticação em dois fatores. Na reunião de diretoria, alguém pergunta à CISO, a diretora de segurança da informação, Marina Prado: 'estamos seguros?'. E ela percebe que não tem como provar. As ferramentas estão instaladas, mas ninguém sabe se elas detectariam um ataque, nem em quanto tempo a equipe reagiria. E o que está em jogo pesa: 36 mil alunos, cerca de 30% menores de idade, biometria facial nas catracas e atestados de saúde. Então fica a pergunta desta aula, que está em amarelo no slide: como a Rede Tatame pode testar a própria defesa sem cometer um crime e sem esperar um ataque real? Guarde também os quatro nomes aqui embaixo: Bruno Sato, do Red Team; Luiza Ferraz, do Blue Team; Carla Dias, do financeiro, que será o alvo do teste; e Marina Prado, que autoriza tudo."  
Fala (apontando o mapa): "À direita está o mapa da plataforma. Em destaque, o *e-mail*, o notebook de Carla, em vermelho, e o SOC, o centro de operações de segurança, que deveria perceber o exercício."  
[Take de apoio: reunião de diretoria com uma pessoa apresentando gráficos — Envato]

**Slide 5 — Da simulação militar ao adversário autorizado (2:10–3:10)**  
Fala: "Os nomes vêm de exercícios militares. A força vermelha fazia o papel do inimigo para testar os planos da força azul. Na cibersegurança, a ideia continua a mesma: só sabemos se uma defesa funciona quando alguém que pensa como o adversário a põe à prova. O Red Team emula um adversário real, com autorização, e persegue objetivos como acessar a base de clientes. O Blue Team protege, monitora, detecta e responde todos os dias, em geral a partir do SOC. E o Purple Team é menos uma equipe fixa e mais uma forma de colaboração: o Red executa uma técnica, o Blue confere se ela foi detectada e os dois ajustam a detecção na hora."

**Slide 6 — Visualização 3D: três cores, uma estratégia (3:10–4:20)**  
Objetivo: entender o papel de cada equipe antes de montar o teste da Rede Tatame.  
Na tela:  
1. Deixar a cena girar alguns segundos sozinha.  
2. Arrastar com o *mouse* para girar até ver o ponto em que o anel vermelho e o anel azul se cruzam, com a esfera roxa no centro.  
3. Rolar a roda do *mouse* para aproximar das partículas.  
Fala: "O anel vermelho, à esquerda, é o Red Team, com o rótulo 'emular'. O azul, à direita, é o Blue Team, com o rótulo 'detectar'. Repare que eles se cruzam, e no cruzamento fica a esfera roxa, o Purple, que significa colaborar. Agora observe as partículas: elas saem vermelhas do lado do ataque, ficam roxas no meio e chegam azuis do lado da defesa. Cada partícula representa uma técnica testada pelo Red Team que virou detecção no Blue Team. A legenda, no canto superior direito, resume as três cores."  
Atenção: a cena é uma metáfora visual; as partículas não representam dados reais. Se a cena não carregar, avise que ela depende de conexão com a internet.  
Conclusão: "Testar a defesa pede as três cores: quem ataca, quem defende e quem junta os resultados."  
[Tela: gravação do laboratório do slide 6]

**Slide 7 — Missão, pergunta, entregável e ritmo (4:20–5:10)**  
Fala: "Esta tabela compara as três equipes em quatro aspectos. Olhe a linha da pergunta central. O Red Team pergunta 'até onde um atacante chegaria?'. O Blue Team pergunta 'percebemos e contivemos a tempo?'. E o Purple Team pergunta 'o que aprendemos e o que mudou?'. Os entregáveis também mudam: relatório da operação, alertas e investigações, detecções novas com métricas de cobertura. E o ritmo: o Red trabalha por campanha, o Blue é contínuo e o Purple funciona em ciclos curtos."

**Slide 8 — Laboratório: um *phishing* simulado e dois desfechos (5:10–7:40)**  
Objetivo: ver o que muda quando o SOC percebe o exercício. Este laboratório responde à parte da pergunta sobre "testar sem esperar um ataque real".  
Na tela:  
1. Clicar em "Avançar" e ler o passo "09h00 · A campanha começa".  
2. Avançar para "09h04 · O filtro deixa passar" e "09h12 · Um clique".  
3. Avançar pelos três passos do Desfecho A: "09h13 · A telemetria chega", "09h17 · Alerta e triagem" e "09h22 · Contenção em 10 minutos".  
4. Avançar para "Desfecho B · Ninguém percebe".  
5. Avançar para o último passo, "Nos dois casos · Reunião purple". O contador, à direita, mostra 8/8.  
Fala: "O diagrama mostra o mesmo exercício com dois finais possíveis. Às 9h, Bruno Sato dispara 40 *e-mails* de um domínio registrado há dois dias, como faria um criminoso. Isso está previsto na carta assinada por Marina Prado. O domínio é novo e ainda não aparece em listas de bloqueio, então o filtro deixa passar. Às 9h12, Carla Dias clica no *link* 'Atualize seus benefícios' no notebook NB-FIN-031, e o navegador abre uma página falsa de *login*, controlada pelo Red Team. Agora vem o desfecho A, em azul: o EDR, que é o agente de segurança instalado no notebook, registra o acesso ao domínio recém-registrado e manda para o SIEM, a ferramenta que centraliza e correlaciona os registros. Às 9h17 sai um alerta de severidade alta, Luiza abre o caso e identifica as outras 39 caixas de entrada. Às 9h22 o notebook está isolado, a senha foi trocada e as mensagens foram removidas. Repare: a tentativa de usar a senha na VPN já tinha parado no MFA. Do clique à contenção, 10 minutos. No desfecho B, em amarelo, falta a regra que liga domínio novo e *e-mail* recebido. O acesso parece navegação comum e, se fosse um ataque real, o invasor teria semanas. Nos dois casos, termina na reunião *purple*: Red e Blue revisam juntos a linha do tempo, e a regra que faltou é escrita e testada na mesma semana."  
Atenção: o botão "Auto" avança sozinho; para gravar com calma, prefira "Avançar". A seta para a esquerda volta um passo. Os horários e os nomes são fictícios.  
Conclusão: "O exercício mostra, com hora marcada, se a defesa funciona. E, quando ela falha, a falha vira melhoria em vez de prejuízo."  
[Tela: gravação do laboratório do slide 8]

**Slide 9 — Laboratório: o analista de SOC investiga o exercício (7:40–10:10)**  
Objetivo: medir se o SOC de Luiza Ferraz percebeu o *phishing* simulado.  
Na tela:  
1. Clicar na busca salva "1. Quem recebeu?".  
2. Clicar em "2. Quem clicou?".  
3. Clicar em "3. Processo estranho depois?".  
4. Clicar em "4. A senha foi usada?".  
5. Clicar em "5. Em quanto tempo o SOC viu?", no grupo Métricas.  
Fala (busca 1): "Este é o console do SIEM. No alto, a consulta em KQL, a linguagem de busca da ferramenta. Ela filtra os *e-mails* cujo domínio de origem é portal-rh-beneficios.com e conta por destinatário. Resultado: 40 mensagens, todas entregues, com assunto 'Atualize seus benefícios'. O histograma mostra o pico às 9h. A nota lembra que domínio novo enviando para dezenas de pessoas é um indicador clássico."  
Fala (busca 2): "Agora filtramos os acessos ao mesmo domínio. Três pessoas abriram a página de *login*: Carla às 9h12, depois mais duas. São 3 cliques em 40 envios, uma taxa de 7,5%. Esse número entra no relatório, sem expor quem clicou para fora da equipe."  
Fala (busca 3): "Esta consulta procura processos no NB-FIN-031 cujo processo pai é o navegador ou o Outlook. Aparecem só dois eventos do próprio navegador, com severidade 'info'. Nenhum programa foi executado, exatamente como o escopo previa."  
Fala (busca 4): "Aqui está o registro de auditoria dos *logins* de carla.dias. Às 9h13, a senha capturada foi testada na VPN: 'senha ok, MFA recusado', resultado negado. A segunda tentativa também foi negada. O MFA segurou, mas a senha precisa ser trocada mesmo assim."  
Fala (busca 5): "Por fim, as métricas do caso INC-2026-1116-01. Primeiro evento às 9h12min07, alerta às 9h17min02, contenção às 9h22min10. O MTTD, tempo até detectar, foi de 4 minutos e 55 segundos. O MTTR, tempo até conter, foi de 10 minutos e 3 segundos."  
Atenção: as consultas são exibidas para leitura; o console não executa KQL de verdade. Os IPs 198.51.100.x são de uma faixa reservada para documentação.  
Conclusão: "O exercício virou números que a CISO pode mostrar à diretoria."  
[Tela: gravação do laboratório do slide 9]

**Slide 10 — Laboratório: o mesmo exercício na plataforma da disciplina (10:10–12:40)**  
Objetivo: ver o mesmo exercício acontecer na plataforma Rede Tatame, passo a passo, e responder ao alerta como Blue Team.  
Na tela:  
1. O simulador abre na aba Cenários. Conferir que a velocidade está em "1 s = 15 s".  
2. No cartão "Phishing simulado no financeiro", clicar em "Iniciar cenário". Rolar a aba para baixo até a linha do tempo dos passos.  
3. Esperar os três passos aparecerem (cerca de 25 segundos reais).  
4. Abrir a aba SOC. Na linha do alerta da regra R1, clicar em "Investigar" e ler o painel; depois clicar em "Conter".  
5. Voltar à aba Arquitetura e localizar o notebook NB-FIN-031.  
Fala: "Agora o mesmo *phishing* roda dentro do simulador da disciplina. Ao clicar em 'Iniciar cenário', o relógio começa a andar e os passos entram na linha do tempo, cada um com a técnica do ATT&CK, a fonte de dados e a regra que o detectaria. O primeiro passo, os 40 *e-mails*, aparece como 'visto nos logs, sem alerta': o gateway registrou, mas nenhuma regra disparou. O segundo, o clique de Carla, aparece como 'detectado', porque a regra R1 correlaciona domínio recém-registrado e *e-mail* externo. O terceiro, a senha usada na VPN, aparece como 'bloqueado pelo controle': é o MFA. Na aba SOC, o alerta da R1 está como novo. Em 'Investigar' vemos a lógica da regra e o tempo do primeiro sinal até o alerta. Ao clicar em 'Conter', o estado muda e os indicadores de MTTD e MTTR são preenchidos. Na Arquitetura, o NB-FIN-031 aparece isolado pelo SOC."  
Atenção: se você conter o alerta antes do terceiro passo, ele aparece como "interrompido pela contenção"; para mostrar o MFA, espere os três passos. Para repetir, use "Repetir com as fontes e regras atuais". O botão "Reiniciar" devolve fontes e regras ao padrão.  
Conclusão: "O Red Team criou o cenário e o Blue Team respondeu. A aba Cobertura ATT&CK mostra o resultado do ponto de vista *purple*: que técnicas a Rede Tatame já consegue ver."  
[Tela: gravação do laboratório do slide 10, com zoom na linha do tempo e na tabela do SOC]

**Slide 11 — O que separa um teste de um crime (12:40–13:30)**  
Fala: "Tecnicamente, muitas ações de um Red Team são idênticas às de um criminoso. O que as diferencia é a autorização formal. A Lei nº 12.737/2012 incluiu no Código Penal o art. 154-A, que tipifica a invasão de dispositivo informático, e a Lei nº 14.155/2021 agravou as penas. Por isso, nenhuma atividade ofensiva começa sem documento assinado por quem tem autoridade sobre os ativos, com escopo, regras de engajamento e contatos de emergência. E a LGPD continua valendo durante o teste: dado pessoal acessado é exposto o mínimo possível, protegido e descartado ao final."

**Slide 12 — Laboratório: regras de engajamento como código (13:30–15:10)**  
Objetivo: garantir que o teste fique dentro da autorização, conferindo escopo e horário por código.  
Na tela:  
1. Com o arquivo roe.yaml aberto, esperar a digitação automática terminar.  
2. Clicar em guardiao.py, no explorador, e depois em alvos.txt.  
3. Clicar em "Executar às 10h15" e ler a saída no terminal.  
4. Clicar em "Executar às 21h40".  
Fala (roe.yaml): "As regras de engajamento, ou RoE, estão escritas em YAML. As linhas destacadas mostram a janela: de 16 a 27 de novembro, das 9h às 20h. Depois, o escopo, com as redes da sede e da nuvem e os domínios autorizados. Em fora_do_escopo ficam o parceiro de pagamentos, a página de status terceirizada e a rede de pagamentos 10.40.99.0/24. Há ainda a lista do que é proibido, como negação de serviço e exfiltração de dados pessoais reais, os contatos de emergência e a palavra de parada, 'LARANJA'."  
Fala (guardiao.py): "O guardião lê esse arquivo. A função dentro_da_janela compara a hora com o horário diário. A função no_escopo é a que decide o resultado: primeiro recusa o que está na lista de fora do escopo, depois recusa IPs dentro de redes bloqueadas e só então aceita IPs das redes autorizadas. Para nomes, aceita o domínio ou seus subdomínios."  
Fala (saídas): "Às 10h15, três alvos aparecem como OK e quatro como BLOQUEADO: o 10.40.99.14, porque está na rede de pagamentos; a API da PagaFácil; a página de status; e o 192.168.0.10, que não pertence a nenhuma rede autorizada. Às 21h40, nada roda: o guardião avisa que a janela diária vai das 9h às 20h."  
Atenção: o terminal é simulado e mostra uma saída gravada; nenhum alvo é contatado.  
Conclusão: "Escopo e horário conferidos por código antes de qualquer ação. É assim que a autorização sai do papel e entra no dia a dia do teste."  
[Tela: gravação do laboratório do slide 12]

**Slide 13 — Laboratório: a carta de autorização é a versão assinada? (15:10–16:30)**  
Objetivo: confirmar que a carta usada pelo Red Team é a versão assinada por Marina Prado.  
Na tela:  
1. Clicar em "Próximo comando" quatro vezes, lendo a nota de cada passo.  
2. Se faltar tempo, usar "Executar tudo"; "Reiniciar" volta ao início.  
Fala: "O primeiro comando, ls -l, lista a pasta de autorização: a carta, a assinatura destacada, com extensão .asc, e uma cópia que chegou por *e-mail*. O segundo, sha256sum, calcula o *hash* da carta. O *hash* funciona como uma impressão digital do arquivo: se mudar um único byte, ele muda inteiro. Esse valor confere com o registrado no chamado de aprovação APR-2291. O terceiro, gpg --verify, confere a assinatura digital e responde 'Good signature from Marina Prado'. Ou seja, foi ela quem aprovou, e o arquivo não mudou desde então. O quarto calcula o *hash* da cópia do *e-mail*. Ela tem 33 bytes a mais e o *hash* não confere. Essa versão não vale como autorização."  
Atenção: os *hashes* e a chave são fictícios. Não é preciso saber usar o GPG agora; a ideia é entender por que a versão importa.  
Conclusão: "Um PDF alterado depois da assinatura não autoriza nada. Só a versão assinada protege o Red Team e a empresa."  
[Tela: gravação do laboratório do slide 13]

**Slide 14 — Laboratório: por que testar compensa (16:30–17:40)**  
Objetivo: mostrar à diretoria, em reais, por que testar compensa.  
Na tela:  
1. Conferir os valores iniciais: impacto de R$ 6.000.000, 15% sem o programa, 6% com o programa e custo anual de R$ 250.000.  
2. Arrastar "Probabilidade anual com o programa" até 12%.  
3. Voltar para 6%.  
Fala: "A expectativa de perda anual, ou ALE, multiplica o impacto de um incidente pela chance de ele acontecer no ano. Sem o programa: 6 milhões vezes 15% dá R$ 900.000. Com o programa, a chance cai para 6%, e a ALE vai a R$ 360.000. A redução de risco é de R$ 540.000 por ano, e o retorno, redução dividida pelo custo, é de 2,16 vezes. Nas barras, o verde é a perda esperada e o amarelo é o custo do programa. Agora veja o que acontece se o programa só baixar a chance para 12%: a ALE com o programa vai a R$ 720.000, a redução cai para R$ 180.000 e o painel avisa que o programa não se paga."  
Conclusão: "O programa só se paga se reduzir o risco de verdade. É por isso que os testes precisam ser medidos."  
[Tela: gravação do laboratório do slide 14]

**Slide 15 — De volta ao problema (17:40–18:40)**  
Fala: "Voltemos à pergunta de Marina: como testar a defesa sem cometer um crime e sem esperar um ataque real? Os quatro cartões resumem o que vimos. Testar com autorização: o Red Team simula o *phishing* dentro de um escopo assinado, com regras conferidas por código. Medir a defesa: o SOC mostra quem recebeu, quem clicou e em quantos minutos o alerta apareceu. Melhorar junto: na reunião *purple*, o passo que ninguém viu vira regra nova. Falar com a diretoria: o cálculo da ALE mostra que o teste custa menos do que o risco que reduz. Então a resposta é esta: a Rede Tatame testa a defesa com exercícios autorizados de Red Team, mede a resposta do Blue Team e usa o Purple Team para transformar cada falha encontrada em melhoria comprovada."

**Slides 16 a 18 — Pontos-chave, referências e encerramento (18:40–19:30)**  
Fala: "Para levar desta aula: o Red Team emula adversários, o Blue Team defende de forma contínua, o Purple Team é a colaboração que transforma ataques simulados em melhorias e, sem autorização formal, escopo e regras de engajamento, um teste é crime. As referências estão no slide seguinte. Na próxima aula, vamos aprender a pensar como o adversário, fase a fase, com a Cyber Kill Chain e o MITRE ATT&CK. Até lá!"  
[Take de apoio: equipe em frente a telas de monitoramento — Envato]

## Aula 2 — Pensar como o adversário: Cyber Kill Chain e MITRE ATT&CK

### Texto base

Para defender bem, é preciso entender **como** os ataques acontecem. Atacantes reais não agem de forma aleatória: eles seguem etapas, reutilizam técnicas e deixam rastros. Modelos de ataque organizam esse conhecimento e criam uma linguagem comum entre Red Team e Blue Team.

#### A Cyber Kill Chain

Em 2011, pesquisadores da Lockheed Martin publicaram um modelo inspirado no conceito militar de "cadeia de abate", aplicando-o às intrusões em redes. A **Cyber Kill Chain** descreve sete fases:

1. **Reconhecimento:** coleta de informações sobre o alvo (pessoas, domínios, tecnologias).
2. **Armamento (*weaponization*):** preparação da carga maliciosa, como um documento com macro.
3. **Entrega:** envio da carga ao alvo — por *e-mail*, *site* comprometido ou mídia removível.
4. **Exploração:** execução do código ao explorar uma vulnerabilidade ou a ação do usuário.
5. **Instalação:** estabelecimento de persistência no sistema comprometido.
6. **Comando e controle (C2):** canal de comunicação entre o atacante e a máquina comprometida.
7. **Ações sobre os objetivos:** roubo de dados, criptografia para extorsão, sabotagem.

A grande contribuição do modelo é mostrar que **o defensor não precisa vencer em todas as fases: basta interromper a cadeia em uma delas**. Se a entrega for bloqueada ou o canal de C2 for detectado, o ataque falha.

[Imagem 1 — Infográfico horizontal com as sete fases da Cyber Kill Chain, cada uma com um ícone. Texto alternativo: "Sete etapas da Cyber Kill Chain, do reconhecimento às ações sobre os objetivos". Pode ser recriado pela equipe a partir da lista acima.]

#### Limitações da Kill Chain

O modelo é linear e foi pensado para intrusões que começam com *malware* entregue de fora para dentro. Ataques modernos frequentemente usam credenciais válidas roubadas, abusam de serviços em nuvem ou partem de um usuário interno — e nem sempre passam por todas as fases. Por isso, a Kill Chain é ótima para comunicar a lógica geral de um ataque, mas pouco detalhada para orientar a detecção.

#### MITRE ATT&CK: o vocabulário do comportamento adversário

A matriz **MITRE ATT&CK** (*Adversarial Tactics, Techniques, and Common Knowledge*) é uma base de conhecimento pública, mantida pela organização sem fins lucrativos MITRE, construída a partir de observações de ataques reais. Ela se organiza em três níveis:

- **Táticas:** o "porquê" — o objetivo do atacante em determinado momento. A matriz Enterprise tem 14 táticas, de Reconhecimento (*Reconnaissance*) a Impacto (*Impact*).
- **Técnicas e subtécnicas:** o "como" — a forma de alcançar o objetivo. Exemplo: T1566 — *Phishing*; T1566.001 — *Spearphishing Attachment*.
- **Procedimentos:** a implementação concreta usada por um grupo ou *malware* específico.

| Tática (objetivo) | Exemplo de técnica | Exemplo de detecção |
|---|---|---|
| Acesso inicial | T1566 — *Phishing* | Análise de anexos e cliques em *links* suspeitos |
| Execução | T1059 — Interpretador de comandos e *scripts* | Monitorar PowerShell com parâmetros ofuscados |
| Acesso a credenciais | T1003 — Extração de credenciais do sistema | Alertar acessos ao processo LSASS |
| Movimentação lateral | T1021 — Serviços remotos | Logons remotos fora do padrão |
| Impacto | T1486 — Dados criptografados para impacto | Muitos arquivos renomeados em pouco tempo |

[Imagem 2 — Captura de tela da matriz MITRE ATT&CK Enterprise (attack.mitre.org), com colunas de táticas e células de técnicas. Texto alternativo: "Matriz MITRE ATT&CK com táticas em colunas e técnicas em células". Conteúdo da MITRE com licença de uso livre mediante atribuição.]

#### Como Red e Blue usam o ATT&CK

Para o Red Team, o ATT&CK é um **cardápio de comportamentos** a emular: em vez de testar "qualquer coisa", a equipe escolhe as técnicas usadas pelos grupos que de fato ameaçam aquele setor. Para o Blue Team, é um **mapa de cobertura**: para cada técnica relevante, a pergunta é "temos telemetria e uma regra capaz de detectá-la?". Ferramentas como o ATT&CK Navigator permitem colorir as técnicas cobertas e evidenciar as lacunas.

[Imagem 3 — Exemplo de *layer* do ATT&CK Navigator com técnicas coloridas em verde (detectadas), amarelo (parcial) e vermelho (sem cobertura). Texto alternativo: "Mapa de calor de cobertura de detecção sobre a matriz ATT&CK".]

#### Kill Chain e ATT&CK: complementares, não concorrentes

Os dois modelos funcionam melhor juntos. A Kill Chain oferece a visão de alto nível, útil para explicar à diretoria em que ponto um ataque foi interrompido. O ATT&CK oferece o detalhe operacional de que o analista precisa para escrever uma regra de detecção ou o operador de Red Team precisa para planejar uma simulação. Na prática, muitas equipes descrevem um incidente pelas fases da Kill Chain e, dentro de cada fase, registram as técnicas ATT&CK observadas. Assim, o relatório conversa ao mesmo tempo com o público executivo e com o técnico — e as lições aprendidas podem ser comparadas entre incidentes diferentes, porque usam o mesmo vocabulário.

#### Exemplo numérico: medindo a cobertura

Uma equipe de defesa levantou 40 técnicas ATT&CK associadas aos grupos que atacam empresas de varejo. Dessas, 18 têm regra de detecção testada, 10 têm telemetria, mas nenhuma regra, e 12 não têm sequer os registros necessários. A cobertura de detecção é 18 ÷ 40 = **45%**. O plano de melhoria é óbvio: começar pelas 10 técnicas que já têm telemetria, pois criar regras é mais barato do que implantar novas fontes de dados. Se todas forem cobertas, a cobertura sobe para 28 ÷ 40 = 70%.

#### Pontos-chave

- A Cyber Kill Chain mostra que interromper uma fase basta para frustrar o ataque.
- O MITRE ATT&CK detalha táticas, técnicas e procedimentos observados em ataques reais.
- Red Team usa o ATT&CK para escolher o que emular; Blue Team, para medir o que detecta.

### Referências da aula

HUTCHINS, Eric M.; CLOPPERT, Michael J.; AMIN, Rohan M. Intelligence-driven computer network defense informed by analysis of adversary campaigns and intrusion kill chains. *Leading Issues in Information Warfare & Security Research*, v. 1, p. 80-106, 2011.

MITRE. *MITRE ATT&CK*. Disponível em: <https://attack.mitre.org/>. Acesso em: 13 nov. 2026.

STROM, Blake E. *et al*. *MITRE ATT&CK: design and philosophy*. McLean: The MITRE Corporation, 2018.

### Roteiro da Videoaula 2 — "O ataque tem roteiro: aprenda a lê-lo"

Duração-alvo: 15 a 20 minutos. Deck: unidade_1/slides/aula2.html (22 slides).

**Slides 1 a 3 — Capa, audiodescrição e sumário (0:00–0:35)**  
Fala: "Olá! Hoje vamos aprender a pensar como o adversário. Vamos usar dois modelos que organizam um ataque em etapas, a Cyber Kill Chain e o MITRE ATT&CK, e aplicar os dois a um ataque contra a Rede Tatame. A aula tem sete laboratórios, e o último calcula quanto da plataforma a defesa consegue enxergar."  
[Tela: deck aberto no slide 1; avançar até o sumário]

**Slide 4 — O problema de hoje na Rede Tatame (0:35–2:00)**  
Fala: "Rafael Tavares é engenheiro de detecção da Rede Tatame. O trabalho dele é escrever as regras que transformam registros em alertas para o SOC, o centro de operações de segurança. Hoje chegou um boletim de inteligência: o Grupo Cobalto Austral, um grupo fictício de *ransomware*, atacou outras redes de academias. Ele entra com senha vazada ou por *phishing*, anda pelos servidores da sede e cifra tudo. O que está em jogo são os servidores da sede e as exportações de fichas de alunos guardadas no SRV-ARQ-01. A pergunta da aula está em amarelo: em que pontos a Rede Tatame consegue interromper esse ataque, e que passos dele ainda passariam sem alerta? Para responder, Rafael precisa de um jeito de dividir o ataque em partes."  
Fala (apontando o mapa): "No mapa, em destaque, estão a VPN, o Active Directory, que é o diretório de usuários da sede, o ERP, o EDR e o SIEM. O caminho vermelho mostra por onde o grupo costuma passar: da internet para a VPN, da VPN para o AD e do AD para o servidor de arquivos."  
[Take de apoio: tela de computador com arquivos sendo cifrados, em ambiente de escritório — Envato]

**Slide 5 — As sete fases da Cyber Kill Chain (2:00–3:00)**  
Fala: "Em 2011, pesquisadores da Lockheed Martin aplicaram às intrusões o conceito militar de cadeia de abate. São sete fases: reconhecimento, em que o atacante estuda pessoas e tecnologias do alvo; armamento, em que prepara a carga maliciosa, como um documento com macro; entrega, por *e-mail*, *site* ou mídia removível; exploração, quando o código roda por uma falha ou pela ação do usuário; instalação, para persistir no sistema; comando e controle, ou C2, o canal entre o atacante e a máquina; e ações sobre os objetivos, como roubo de dados, criptografia ou sabotagem. A grande contribuição do modelo é esta: o defensor não precisa vencer em todas as fases. Basta interromper a cadeia em uma delas."

**Slide 6 — Visualização 3D: a cadeia e o ponto de corte (3:00–4:20)**  
Objetivo: ver que basta cortar uma fase para o ataque falhar.  
Na tela:  
1. Mostrar o estado inicial, "Sem defesa": a esfera branca percorre as sete caixas.  
2. Clicar no botão "3", no canto superior esquerdo da cena.  
3. Clicar no botão "6".  
4. Clicar em "Sem defesa" para voltar.  
Fala: "Cada caixa vermelha é uma fase, ligada às outras por um tubo. A esfera branca é o ataque. Sem defesa, ela percorre as sete fases e chega ao objetivo, como diz a legenda à direita. Quando clico no 3, um escudo azul aparece na fase de entrega, as fases seguintes se apagam e a legenda mostra o controle que corta a cadeia ali: filtro de *e-mail* com *sandbox* de anexos. Agora clico no 6: o escudo vai para comando e controle e o controle passa a ser DNS e *proxy* revelando contato periódico com um domínio recém-registrado. Nos dois casos o objetivo falha. A diferença é que, cortando na fase 6, o atacante já está dentro da rede."  
Atenção: os controles de cada fase são exemplos; outras defesas também cortam a cadeia. A cena pode ser girada e aproximada, mas não é preciso.  
Conclusão: "Quanto mais cedo o corte, menos o atacante avança."  
[Tela: gravação do laboratório do slide 6]

**Slide 7 — Laboratório: um *ransomware* na Rede Tatame, fase a fase (4:20–6:40)**  
Objetivo: achar, fase a fase, onde a defesa poderia agir. É a primeira parte da resposta a Rafael.  
Na tela:  
1. Ler o passo inicial, "Rede Tatame e Grupo Cobalto Austral (fictícios)".  
2. Clicar em "Avançar" sete vezes, da fase "1 · Reconhecimento" até "7 · Ações sobre os objetivos".  
3. Avançar para "Basta interromper uma fase" (contador 9/9).  
Fala: "Nesta versão, o grupo entra por *phishing* no financeiro. No reconhecimento, lista nomes e cargos do financeiro em redes profissionais e no *site* da Tatame; a defesa possível é reduzir a exposição pública e vigiar domínios parecidos com tatame.com.br. No armamento, prepara uma planilha com macro, longe da nossa vista; aqui só a inteligência de ameaças ajuda. Na entrega, o *e-mail* 'Repasse das academias' chega a 12 pessoas, e o nó azul do Blue Team se acende: filtro com *sandbox* e atenção a remetentes recém-criados. Na exploração, uma analista habilita a macro no NB-FIN-027; bloquear macros vindas da internet e o alerta do EDR quando o Excel cria outros processos seriam as defesas. Na instalação, surge uma tarefa agendada para sobreviver ao reinício. No comando e controle, a máquina contata um servidor externo em intervalos regulares, e o Blue Team aparece de novo. Na fase 7, a cópia das fichas do SRV-ARQ-01 e a criptografia dos servidores, que ficam em vermelho. O último passo resume: se o filtro barrasse a entrega, ou se o SOC percebesse o C2, nada disso aconteceria."  
Atenção: as linhas tracejadas azuis indicam onde o Blue Team pode agir; elas aparecem nas fases 3, 6 e 7. O botão "Auto" avança sozinho, mas para gravar prefira "Avançar".  
Conclusão: "Rafael já sabe que há pelo menos três pontos de corte: a entrega, o C2 e o impacto."  
[Tela: gravação do laboratório do slide 7]

**Slide 8 — Onde a Kill Chain não alcança (6:40–7:20)**  
Fala: "O modelo é linear e foi pensado para intrusões que começam com *malware* entregue de fora para dentro. Ataques modernos nem sempre seguem esse caminho: usam credenciais válidas roubadas, sem arquivo malicioso; abusam de serviços em nuvem legítimos; partem de um usuário interno; pulam fases ou voltam a fases anteriores. A Kill Chain é ótima para comunicar a lógica geral, mas é pouco detalhada para orientar a detecção. Precisamos de um vocabulário mais fino."

**Slides 9 e 10 — MITRE ATT&CK em três níveis e do objetivo ao rastro (7:20–8:40)**  
Fala: "Esse vocabulário é o ATT&CK, uma base pública mantida pela MITRE, construída a partir de ataques reais. Ele tem três níveis. Táticas são o 'porquê', o objetivo do atacante naquele momento; a matriz Enterprise tem 14. Técnicas e subtécnicas são o 'como'; por exemplo, T1566 é *Phishing* e T1566.001 é o anexo de *spearphishing*. Procedimentos são a implementação concreta usada por um grupo." (avançar) "Esta tabela liga cada tática a uma técnica e a um exemplo de detecção. Em execução, a técnica T1059, interpretador de comandos, é detectada monitorando o PowerShell com parâmetros ofuscados. Em movimentação lateral, T1021, serviços remotos, aparece como *logons* remotos fora do padrão. Cada técnica deixa um rastro, e a detecção procura esse rastro."

**Slide 11 — Laboratório: a técnica T1566 na base ATT&CK (8:40–10:00)**  
Objetivo: ler uma técnica do ATT&CK pelos olhos do Red e do Blue Team.  
Na tela:  
1. Ler a aba "Descrição".  
2. Clicar em "Subtécnicas", "Mitigações" e "Detecção".  
3. Terminar em "Red x Blue".  
Fala: "Esta é uma reprodução simplificada da página da técnica T1566. No topo, o ID, a tática, que é acesso inicial, e as plataformas. A descrição explica que o adversário envia mensagens fraudulentas com anexo ou *link*. Em Subtécnicas, as quatro formas: anexo, *link*, serviço de terceiros e voz. Em Mitigações, cada linha tem um código M; por exemplo, M1017 é o treinamento de usuários. Em Detecção, as fontes de dados que mostram o rastro: o gateway de *e-mail*, o *proxy* e o EDR. E a aba Red x Blue junta tudo: o Red Team planeja público, tema e taxa de cliques; o Blue Team pergunta se tem esses registros no SIEM e se alguma regra liga a mensagem ao clique."  
Atenção: a página é uma reprodução didática; na página real, a seção *Procedure Examples* lista dezenas de grupos que usaram a técnica.  
Conclusão: "A mesma página diz ao Red Team o que emular e ao Blue Team o que procurar."  
[Tela: gravação do laboratório do slide 11]

**Slide 12 — Cardápio para o Red, mapa para o Blue (10:00–10:30)**  
Fala: "Para o Red Team, o ATT&CK é um cardápio de comportamentos: em vez de testar 'qualquer coisa', a equipe escolhe as técnicas dos grupos que de fato ameaçam o setor. Para o Blue Team, é um mapa de cobertura: para cada técnica relevante, temos telemetria e uma regra capaz de detectá-la? O ATT&CK Navigator pinta essa resposta: verde para detectada, amarelo para parcial, vermelho para sem cobertura."

**Slide 13 — Laboratório: uma camada de cobertura no estilo Navigator (10:30–11:50)**  
Objetivo: pintar o que a Rede Tatame detecta e o que não detecta.  
Na tela:  
1. Clicar em "Camada da aula (5 técnicas)".  
2. Clicar uma vez em uma célula cinza, por exemplo T1078, e mostrar que a cor muda a cada clique.  
3. Clicar em "Exportar layer JSON"; clicar de novo para fechar.  
4. Clicar em "Limpar".  
Fala: "As 14 colunas são as táticas, e cada botão é uma técnica. A camada da aula pinta cinco técnicas do ataque que acabamos de ver: T1566, *phishing*, e T1003, extração de credenciais, ficam em verde; T1059, interpretador de comandos, e T1486, criptografia, ficam em amarelo; T1021, serviços remotos, fica em vermelho. Os contadores no alto mostram 5 avaliadas, 2 detectadas, 2 parciais e 1 sem cobertura, com cobertura de 40%. Cada clique em uma célula avança a cor: vermelho, amarelo, verde e de volta ao cinza. O botão de exportar gera o arquivo JSON no formato que o Navigator real importa."  
Atenção: a cobertura deste painel conta só as técnicas verdes sobre as avaliadas. Se o aluno pintar outras células, o número muda.  
Conclusão: "Pintar a matriz transforma 'achamos que estamos protegidos' em uma lista do que falta."  
[Tela: gravação do laboratório do slide 13]

**Slide 14 — Kill Chain e ATT&CK são complementares (11:50–12:20)**  
Fala: "Os dois modelos trabalham juntos. A Kill Chain dá a visão de alto nível, em sete fases, e serve à diretoria: em que ponto o ataque foi interrompido. O ATT&CK dá o detalhe operacional, com 14 táticas, técnicas e procedimentos, e serve ao analista que escreve a regra. No relatório, as fases organizam a narrativa e, dentro de cada fase, ficam as técnicas observadas."

**Slide 15 — Laboratório: um incidente descrito por fases e técnicas (12:20–13:50)**  
Objetivo: registrar o incidente INC-0412 para três leitores diferentes.  
Na tela:  
1. Clicar na busca "1. Linha do tempo por fase".  
2. Clicar em "2. Técnicas por tática".  
3. Clicar em "3. Visão executiva", no grupo Relatório.  
Fala (busca 1): "O SOC interrompeu o ataque do diagrama, e Luiza Ferraz precisa registrá-lo. A primeira consulta ordena os eventos do incidente pelo tempo. Cada linha tem a fase da Kill Chain e a técnica do ATT&CK. Doze dias antes, 37 acessos à página 'Quem somos'; três dias antes, um domínio parecido registrado; no dia, a entrega às 8h41, o Excel criando processo às 9h02, a tarefa agendada às 9h03 e o contato com o domínio novo a partir das 9h05. As duas últimas linhas são do Blue Team: alerta às 9h26 e isolamento do NB-FIN-027 às 9h41."  
Fala (busca 2): "Esta agrupa por tática e técnica e mostra a situação da detecção. Repare em execução e persistência: 'telemetria, sem regra'. O EDR registrou, mas nada disparou."  
Fala (busca 3): "E esta resume para a diretoria em uma linha: interrompido na fase 6 de 7, entrega às 8h41, alerta às 9h26, contenção às 9h41, nenhum dado afetado."  
Atenção: o console mostra a consulta para leitura; os dados são fictícios.  
Conclusão: "O ataque parou na fase 6 de 7, e duas técnicas entram no plano de melhoria."  
[Tela: gravação do laboratório do slide 15]

**Slide 16 — Laboratório: o Grupo Cobalto Austral na plataforma (13:50–16:20)**  
Objetivo: descobrir onde a defesa atual da Rede Tatame para o grupo e onde ela fica cega.  
Na tela:  
1. Na aba Cenários, no cartão "Emulação do Grupo Cobalto Austral", clicar em "Iniciar cenário". Velocidade em "1 s = 15 s".  
2. Quando aparecer o primeiro alerta, da regra R11, abrir a aba SOC, clicar em "Investigar" e depois em "Conter".  
3. Voltar a Cenários e rolar até a linha do tempo.  
4. Clicar em "Reiniciar" e iniciar o cenário de novo, agora sem conter. Para não esperar, trocar a velocidade para "1 s = 1 min".  
5. Ao fim, abrir a aba "Cobertura ATT&CK".  
Fala (primeira rodada): "O cenário começa com um *login* na VPN usando a senha vazada de caio.mendes, sem MFA. A regra R11, *login* sem MFA em conta de VPN, dispara logo. No SOC, investigo e contenho. Volto à linha do tempo: o primeiro passo está como 'detectado' e todos os outros como 'interrompido pela contenção'. Aqui a cadeia parou logo na entrada."  
Fala (segunda rodada): "Agora deixo o ataque correr para ver tudo o que a Rede Tatame enxerga. A consulta em massa ao AD e o RDP para o SRV-ARQ-01 aparecem em amarelo, 'visto nos logs, sem alerta': a fonte existe, mas as regras R13 e R5 estão desligadas. A leitura da memória do LSASS, que serve para roubar credenciais, é detectada pela R6. A cópia de 4,2 GB para fora aparece em vermelho, 'não detectado', porque a fonte de saída de rede está desligada. A exclusão das cópias de sombra é detectada pela R7, mas o último passo termina como 'impacto consumado'. Nos indicadores, compare detectados, não detectados e vistos sem alerta."  
Fala (Cobertura): "A aba Cobertura ATT&CK pinta cada técnica dos cenários: detectável, parcial ou cega, com a regra que falta. É o Navigator da própria plataforma."  
Atenção: o cenário completo leva cerca de 14 minutos simulados; em "1 s = 1 min", menos de 20 segundos reais. Pode surgir um alerta de comportamento conhecido; em "Investigar" ele aparece como contexto documentado e deve ser marcado como "Falso positivo". O "Reiniciar" devolve fontes e regras ao padrão.  
Conclusão: "A entrada por senha vazada não tem armamento nem instalação. É a limitação do modelo linear, e é por isso que usamos o ATT&CK para descrever o ataque."  
[Tela: gravação do laboratório do slide 16, com zoom na linha do tempo e nos indicadores]

**Slide 17 — Medindo a cobertura de detecção (16:20–16:50)**  
Fala: "Uma equipe levantou 40 técnicas ATT&CK associadas aos grupos que ameaçam a Rede Tatame, como o Cobalto Austral. 18 têm regra de detecção testada, 10 têm telemetria mas nenhuma regra e 12 não têm os registros necessários. A cobertura atual é 18 dividido por 40, 45%. O plano começa pelas 10 técnicas que já têm telemetria, porque criar regra é mais barato do que implantar fonte nova. Com elas, a cobertura sobe para 28 de 40, 70%."

**Slide 18 — Laboratório: a cobertura calculada em Python (16:50–18:10)**  
Objetivo: decidir por onde começar as regras novas.  
Na tela:  
1. Com cobertura.py aberto, esperar a digitação terminar.  
2. Clicar em tecnicas_tatame.csv, no explorador, e rolar a lista.  
3. Clicar em "Executar cobertura.py".  
4. Se houver tempo, abrir deteccoes/T1486_renomeacao.kql.  
Fala (código): "O *script* lê o CSV com csv.DictReader, e cada linha vira um dicionário com id, nome, tática e status. O Counter conta quantas técnicas têm cada status: regra, telemetria ou nenhuma. As linhas destacadas fazem a conta que decide o resultado: a cobertura atual é o número de técnicas com regra dividido pelo total; a cobertura-alvo soma as que têm regra e as que têm telemetria."  
Fala (saída): "Resultado: 40 técnicas, 18 com regra, 10 com telemetria e 12 sem nada. Cobertura atual, 45%; com as regras novas, 70%. Embaixo, a lista das próximas regras: descoberta de contas de domínio, compartilhamentos administrativos, protocolos web de C2, exfiltração para nuvem e outras. Repare que T1087.002 e T1567.002 são exatamente os passos que passaram sem alerta na plataforma."  
Fala (KQL): "O arquivo .kql mostra como seria uma dessas regras: conta arquivos renomeados por máquina em janelas de 5 minutos e alerta acima de 200, um sinal de criptografia em andamento."  
Atenção: o terminal mostra uma execução gravada; o código é real e funcionaria com o mesmo CSV.  
Conclusão: "Criar regra onde o registro já existe é o caminho mais barato para aumentar a cobertura."  
[Tela: gravação do laboratório do slide 18]

**Slide 19 — De volta ao problema (18:10–19:00)**  
Fala: "Voltemos à pergunta de Rafael. A cadeia tem pontos de corte, e quanto mais cedo, menos o atacante avança. No incidente por *phishing*, o SOC isolou o notebook na fase 6 de 7, antes da cópia e da criptografia. A plataforma mostrou as lacunas: a R11 pega o *login* sem MFA na VPN, mas a descoberta no AD, o RDP entre servidores e a cópia para fora passam sem alerta. E a ordem do trabalho está calculada: de 45% para 70% de cobertura. Então a resposta é: a Rede Tatame consegue parar o Cobalto Austral na entrada, pelo *login* sem MFA, e na fase de credenciais e cópias de sombra. Ainda passariam sem alerta a descoberta no AD, o acesso remoto entre servidores e a saída de dados, que são as próximas regras a escrever."

**Slides 20 a 22 — Pontos-chave, referências e encerramento (19:00–19:40)**  
Fala: "Para levar desta aula: interromper uma fase da Kill Chain basta para frustrar o ataque; o ATT&CK detalha táticas, técnicas e procedimentos observados em ataques reais; o Red Team usa o ATT&CK para escolher o que emular, e o Blue Team, para medir o que detecta. Na próxima aula, vamos ver as formas de avaliar a segurança: varredura, *pentest* e Red Team, e por que elas respondem a perguntas diferentes. Até lá!"

## Aula 3 — Avaliações de segurança: varredura, pentest e Red Team

### Texto base

"Fizemos um pentest e está tudo certo." Essa frase aparece com frequência em reuniões de diretoria, mas pode esconder um equívoco: diferentes tipos de avaliação respondem a perguntas diferentes. Escolher o tipo errado gera uma falsa sensação de segurança.

#### Três tipos de avaliação

**Varredura de vulnerabilidades** é uma verificação, em geral automatizada, que compara os sistemas com bases de vulnerabilidades conhecidas. Ela responde: "quais falhas conhecidas existem nos meus ativos?". É ampla, rápida e deve ser periódica, mas gera falsos positivos e não comprova se a falha é realmente explorável.

**Teste de invasão (*pentest*)** é uma avaliação conduzida por especialistas que tentam explorar as vulnerabilidades encontradas, dentro de um escopo definido, para demonstrar o impacto real. Ele responde: "o que um atacante consegue fazer nesse sistema?". O foco é **encontrar o maior número possível de falhas relevantes** em um alvo delimitado — uma aplicação, uma rede, uma API.

**Operação de Red Team** emula um adversário específico perseguindo um objetivo de negócio, normalmente com furtividade e por um período mais longo. Ela responde: "a organização detecta e responde a um ataque realista?". Aqui, o alvo de avaliação é tanto a tecnologia quanto **as pessoas e os processos de defesa**.

| Critério | Varredura | Pentest | Red Team |
|---|---|---|---|
| Pergunta | Quais falhas conhecidas existem? | O que pode ser explorado? | Detectamos e respondemos? |
| Escopo | Amplo | Delimitado | Orientado a objetivos |
| Furtividade | Nenhuma | Baixa | Alta |
| Duração típica | Horas | Dias a semanas | Semanas a meses |
| Blue Team avisado? | Sim | Normalmente sim | Normalmente não (só a liderança) |

[Imagem 1 — Pirâmide com três níveis: varredura na base (mais ampla e frequente), pentest no meio e Red Team no topo (mais profundo e realista). Texto alternativo: "Pirâmide de maturidade das avaliações de segurança".]

#### Metodologias de referência

Testes profissionais seguem metodologias que garantem cobertura e repetibilidade. O **NIST SP 800-115** organiza a avaliação em quatro fases: planejamento, descoberta, ataque e relatório. O **PTES** (*Penetration Testing Execution Standard*) detalha sete fases: pré-engajamento, coleta de informações, modelagem de ameaças, análise de vulnerabilidades, exploração, pós-exploração e relatório. Para aplicações *web*, o **OWASP Web Security Testing Guide** é a referência mais usada.

[Imagem 2 — Fluxograma circular com as fases do PTES, destacando o pré-engajamento como ponto de partida. Texto alternativo: "Ciclo das sete fases do Penetration Testing Execution Standard".]

#### Caixa-preta, caixa-cinza e caixa-branca

O nível de informação fornecido aos testadores muda o resultado. No teste **caixa-preta**, a equipe recebe apenas o nome da empresa, como um atacante externo. No **caixa-cinza**, recebe informações parciais, como uma conta de usuário comum. No **caixa-branca**, tem acesso a diagramas, código-fonte e configurações. Testes caixa-preta são mais realistas, mas consomem mais tempo descobrindo o que já se sabe; testes caixa-branca encontram mais falhas por hora investida.

#### Regras de engajamento na prática

Antes de qualquer teste, o documento de regras de engajamento deve definir: ativos dentro e fora do escopo; janelas de horário; técnicas proibidas (por exemplo, negação de serviço em produção); tratamento de dados sensíveis encontrados; critérios de parada; e uma **carta de autorização** que o testador pode apresentar se for abordado. Em operações de Red Team, define-se também a **célula branca** (*white cell*): um pequeno grupo da liderança que sabe do exercício e pode interrompê-lo se ele for confundido com um incidente real.

[Imagem 3 — *Checklist* de regras de engajamento em uma prancheta: escopo, janelas de horário, técnicas proibidas, dados sensíveis, critérios de parada, contatos de emergência. Texto alternativo: "Prancheta com lista de verificação das regras de engajamento de um teste de segurança". Sugestão de busca no Envato: "checklist clipboard security audit".]

#### O relatório: onde o teste gera valor

Um teste só se transforma em melhoria quando seus resultados são bem comunicados. Um bom relatório tem duas camadas: um **sumário executivo**, que explica em linguagem de negócio o risco encontrado e as prioridades, e uma **seção técnica**, com cada achado descrito, as evidências, a severidade e a recomendação de correção. Em operações de Red Team, o relatório também inclui a linha do tempo do ataque, comparada com o que o Blue Team detectou — é essa comparação que revela as lacunas de detecção e resposta.

#### Pausa para reflexão

> Uma rede de farmácias com 300 lojas pede uma proposta de "pentest completo", com o objetivo declarado de "saber se o SOC terceirizado está detectando ataques". Ela já realiza varreduras mensais de vulnerabilidades.
>
> 1. O serviço solicitado responde à pergunta da empresa? Justifique.
> 2. Que tipo de avaliação você recomendaria e com qual objetivo de negócio?
> 3. Quais três itens não podem faltar nas regras de engajamento desse trabalho?
>
> **Desafio prático:** redija, em até uma página, um esboço de regras de engajamento para esse cenário.

#### Exemplo numérico: priorizando o orçamento

Com R$ 120.000 de orçamento anual, uma empresa avalia duas opções: (a) quatro *pentests* de aplicações a R$ 30.000 cada; ou (b) varreduras mensais (R$ 2.000/mês, R$ 24.000/ano) mais uma operação de Red Team de R$ 96.000. Se a principal dúvida da diretoria é a capacidade de detecção, a opção (b) é mais adequada; se a empresa vai lançar quatro novos sistemas expostos à internet, a opção (a) faz mais sentido. O número sozinho não decide: **a pergunta de negócio decide**.

#### Pontos-chave

- Varredura, *pentest* e Red Team respondem a perguntas diferentes.
- Metodologias como NIST SP 800-115, PTES e OWASP WSTG dão método e repetibilidade.
- Regras de engajamento e carta de autorização são obrigatórias.

### Referências da aula

NATIONAL INSTITUTE OF STANDARDS AND TECHNOLOGY. *SP 800-115: technical guide to information security testing and assessment*. Gaithersburg: NIST, 2008.

OWASP FOUNDATION. *OWASP web security testing guide*. Versão 4.2. 2020. Disponível em: <https://owasp.org/www-project-web-security-testing-guide/>. Acesso em: 13 nov. 2026.

PTES. *The penetration testing execution standard*. Disponível em: <http://www.pentest-standard.org/>. Acesso em: 13 nov. 2026.

### Roteiro da Videoaula 3 — "Pentest não é Red Team (e isso custa caro)"

Duração-alvo: 15 a 20 minutos. Deck: unidade_1/slides/aula3.html (24 slides).

**Slides 1 a 3 — Capa, audiodescrição e sumário (0:00–0:30)**  
Fala: "Olá! Hoje vamos comparar três formas de avaliar a segurança: a varredura de vulnerabilidades, o teste de invasão, ou *pentest*, e a operação de Red Team. Elas parecem parecidas, mas respondem a perguntas diferentes, e escolher a errada custa caro. São seis laboratórios, todos na Rede Tatame."  
[Tela: deck aberto no slide 1; avançar até o sumário]

**Slide 4 — O problema de hoje na Rede Tatame (0:30–1:50)**  
Fala: "Caio Mendes é o administrador de TI da sede da Rede Tatame. Na reunião de planejamento, ele lembra que o portal das academias passou por um *pentest* no ano passado e conclui: 'está tudo certo'. Só que a CISO, Marina Prado, tem R$ 120.000 para o próximo ano e duas dúvidas. Primeira: o que a Rede Tatame expõe na internet hoje? Segunda: o SOC, o centro de operações de segurança, perceberia um ataque realista? E o que está em jogo é concreto: um ambiente de homologação esquecido, com cópia de dados de alunos, e a VPN da sede. A pergunta da aula, em amarelo: que tipo de avaliação responde a cada dúvida da Rede Tatame, varredura, *pentest* ou Red Team?"  
Fala (apontando o mapa): "No mapa, em destaque, a borda da plataforma: WAF, portal, VPN e *e-mail*. Em vermelho, a homologação esquecida, o hml-gestao, que chega ao banco de dados sem passar pelo WAF, o filtro que protege as aplicações *web*."  
[Take de apoio: reunião de equipe de TI com notebook e planilha de orçamento — Envato]

**Slide 5 — Três tipos de avaliação, três perguntas (1:50–2:50)**  
Fala: "A varredura de vulnerabilidades é uma verificação, em geral automatizada, que compara os sistemas com bases de falhas conhecidas. Ela responde 'quais falhas conhecidas existem nos meus ativos?'. É ampla, rápida e deve ser periódica, mas gera falsos positivos e não comprova se a falha é explorável. O *pentest* é feito por especialistas que tentam explorar as falhas dentro de um escopo definido. Ele responde 'o que um atacante consegue fazer nesse sistema?'. Já a operação de Red Team emula um adversário específico, perseguindo um objetivo de negócio, com furtividade e por mais tempo. Ela responde 'a organização detecta e responde a um ataque realista?' e avalia tecnologia, pessoas e processos."

**Slide 6 — Laboratório: uma varredura autorizada e seus limites (2:50–5:00)**  
Objetivo: responder à primeira dúvida de Marina, o que a Rede Tatame expõe na internet.  
Na tela:  
1. Clicar em "Próximo comando" para cada um dos cinco comandos, lendo a nota que aparece ao lado dos botões.  
Fala (cat escopo.txt): "Antes de qualquer pacote, o escopo. O arquivo mostra o chamado SEC-4471, a faixa autorizada 203.0.113.0/26, que é a borda da plataforma, a janela de 16 de novembro, das 9h às 18h, e a aprovação de Marina. Em amarelo, o que está fora: a API da PagaFácil, a página de status e o promo-hml, que tem nome parecido mas é hospedado pela agência."  
Fala (nmap): "O nmap descobre serviços e versões. A opção -sV pede a versão, e -p escolhe as portas 25, 443 e 8080. Leia por bloco: cada 'scan report' é um servidor. O *site*, o app, o portal e a API respondem como 'CDN edge', porque estão atrás da rede de entrega. A VPN mostra a versão NetGuard 9.1. E o hml-gestao aparece sem proteção, com Apache 2.4.49 e Tomcat. No fim, 7 servidores ativos em 64 endereços."  
Fala (vulnscan relatorio): "O *scanner*, que é fictício, cruza as versões com bases de vulnerabilidades. Cada linha traz o componente, o CVE, que é o identificador público da falha, e a nota CVSS, a gravidade de 0 a 10. São 4 achados com CVSS de 7 ou mais, e a última linha avisa: um ativo fora do inventário, o hml-gestao. Repare na coluna método: a maioria das versões foi lida do *banner*, o texto que o serviço anuncia."  
Fala (vulnscan detalhe): "O achado do log4j no *site*, nota 10, veio de uma página de erro antiga. O inventário autenticado mostra que a versão corrigida está instalada desde 2022. Veredito: provável falso positivo, marcado para revisão manual."  
Fala (exportar): "Por fim, o resultado é exportado para priorização: 4 achados, 2 críticos e 2 altos, um deles provável falso positivo."  
Atenção: os comandos são exibidos, não executados; a faixa 203.0.113.0/24 é reservada para documentação. Os CVEs são reais, mas os servidores são fictícios. O "Executar tudo" roda tudo de uma vez se faltar tempo.  
Conclusão: "A varredura é ampla e rápida, aponta candidatos e achou o hml-gestao. Comprovar a falha é trabalho do *pentest*, com outro escopo e outra autorização."  
[Tela: gravação do laboratório do slide 6]

**Slide 7 — Laboratório: da lista de achados ao que a defesa enxerga (5:00–7:20)**  
Objetivo: priorizar os achados e ver o que o SOC percebe de um reconhecimento.  
Na tela:  
1. O simulador abre na aba Superfície. Deixar marcado "ordenar por risco".  
2. Passar o cursor pelas colunas inventário, WAF, CVSS, EPSS, KEV e risco; rolar até o rodapé com a fórmula.  
3. Abrir a aba Cenários e, no cartão "Reconhecimento externo", clicar em "Iniciar cenário". Trocar a velocidade para "1 s = 1 min" e rolar até a linha do tempo.  
4. Clicar em "Reiniciar". Na aba Telemetria, ligar a fonte "Monitor de certificados (CT)". Na aba Regras do CEP, ligar a regra R12. Voltar a Cenários e iniciar o mesmo cenário.  
Fala (Superfície): "A tabela lista os ativos expostos. A linha em destaque é o hml-gestao: inventário 'não' e WAF 'não'. O risco combina quatro coisas. O CVSS, a gravidade da falha. O EPSS, a chance estimada de ela ser explorada nos próximos dias. O KEV, o catálogo de falhas que já estão sendo exploradas. E a criticidade do ativo. Por isso a VPN, com nota 10 e no KEV, fica no topo, com risco 43,8, e o hml-gestao vem logo depois, com 32,4, à frente do portal. Já o *site*, também com nota 10, cai para 11,8: a criticidade é baixa e ele está atrás do WAF."  
Fala (primeira rodada): "Agora o Red Team faz o reconhecimento autorizado. Na linha do tempo, o primeiro passo, a consulta a certificados públicos que revela o hml-gestao, aparece como 'não detectado'. A resolução de nomes também. Só a varredura contra a borda é 'detectado', pela regra R4, excesso de erros 403 e 404 por IP. A varredura no hml-gestao, que não passa pelo WAF, ninguém vê."  
Fala (segunda rodada): "Com a fonte de certificados e a regra R12 ligadas, o primeiro passo passa a ser detectado: um certificado novo para um subdomínio fora do inventário gera um alerta de severidade baixa. Na aba Telemetria, repare que essa fonte custa quase nada por mês."  
Atenção: o "Reiniciar" desliga de novo fontes e regras; ligue-as depois de reiniciar. Se o professor preferir manter o que ligou, use "Repetir com as fontes e regras atuais". O EPSS da tabela é ilustrativo; o valor do dia está no *site* do FIRST.  
Conclusão: "O promo-hml é da agência: aparece no levantamento, mas fica fora do escopo. E o que o reconhecimento mostra ao atacante pode, com uma fonte barata, também aparecer para o SOC."  
[Tela: gravação do laboratório do slide 7, com zoom na tabela de ativos e na linha do tempo]

**Slide 8 — Varredura, *pentest* e Red Team lado a lado (7:20–7:50)**  
Fala: "A tabela resume a comparação. Leia a última linha: na varredura, o Blue Team é avisado; no *pentest*, normalmente também; no Red Team, normalmente não, só a liderança sabe. É isso que permite medir se o SOC percebe. Repare também na duração: horas, dias a semanas, semanas a meses."

**Slide 9 — Visualização 3D: a pirâmide das avaliações (7:50–8:50)**  
Objetivo: comparar os três tipos de avaliação lado a lado.  
Na tela:  
1. Clicar em "Varredura", no canto superior esquerdo da cena.  
2. Clicar em "Pentest" e depois em "Red Team".  
3. Clicar em "Pirâmide inteira" e girar a cena com o *mouse*.  
Fala: "A base da pirâmide, em azul, é a varredura: mais ampla e mais frequente. Ao clicar, o andar se destaca e a legenda mostra a pergunta, o escopo, a furtividade, a duração e se o Blue Team é avisado. O meio, em amarelo, é o *pentest*. O topo, em vermelho, é o Red Team: mais profundo e mais realista. Uma analogia ajuda: num hospital, a varredura é o *check-up* de rotina, o *pentest* é o exame detalhado de um órgão e o Red Team é a simulação de emergência."  
Conclusão: "Cada andar se apoia no de baixo. Um Red Team sem varredura esbarra em falhas que uma varredura já mostraria."  
[Tela: gravação do laboratório do slide 9]

**Slide 10 — Método garante cobertura e repetibilidade (8:50–9:30)**  
Fala: "Três referências organizam o trabalho. O NIST SP 800-115 divide a avaliação em quatro fases: planejamento, descoberta, ataque e relatório. O PTES detalha sete fases, do pré-engajamento ao relatório. E o OWASP Web Security Testing Guide é a referência mais usada para aplicações *web*. Elas concordam no essencial: o teste começa no pré-engajamento, com escopo e autorização, e só termina quando o relatório é entregue."

**Slide 11 — Laboratório: o ciclo do PTES e as fases do NIST (9:30–10:50)**  
Objetivo: ver que as metodologias seguem a mesma ordem.  
Na tela:  
1. Ler o passo "Duas metodologias, a mesma lógica".  
2. Clicar em "Avançar" sete vezes, de "1 · Pré-engajamento" a "7 · Relatório".  
3. Avançar para "O ciclo recomeça" (contador 9/9).  
Fala: "À esquerda, as sete fases do PTES em círculo; à direita, as quatro do NIST, em amarelo. A cada passo, a linha amarela mostra onde uma fase do PTES se encaixa no NIST. O pré-engajamento é o planejamento: objetivo, escopo, regras e carta de autorização. Coleta de informações, modelagem de ameaças e análise de vulnerabilidades caem todas na descoberta; a análise inclui separar falsos positivos, como fizemos no terminal. Exploração e pós-exploração são a fase de ataque: comprovar o acesso e medir até onde ele chega, sempre dentro das regras. O relatório é o mesmo nas duas. No último passo, a seta verde liga o relatório ao próximo pré-engajamento."  
Conclusão: "As metodologias diferem no detalhe, mas a ordem é a mesma: autorizar, descobrir, comprovar e relatar."  
[Tela: gravação do laboratório do slide 11]

**Slides 12 e 13 — Caixa-preta, caixa-cinza, caixa-branca e as regras de engajamento (10:50–11:50)**  
Fala: "O nível de informação dado aos testadores muda o resultado. Na caixa-preta, a equipe recebe só o nome da empresa: é mais realista, mas gasta tempo descobrindo o que a empresa já sabe. Na caixa-cinza, recebe informação parcial, como uma conta de usuário comum. Na caixa-branca, tem diagramas, código e configurações, e encontra mais falhas por hora." (avançar) "E as regras de engajamento precisam definir ativos dentro e fora do escopo, janelas de horário, técnicas proibidas, tratamento de dados sensíveis, critérios de parada e a carta de autorização. Em Red Team, há ainda a célula branca: um pequeno grupo da liderança que sabe do exercício e pode interrompê-lo se ele for confundido com um incidente real."

**Slide 14 — Laboratório: um modelo de RoE, conferido item por item (11:50–13:30)**  
Objetivo: preparar a operação de Red Team que responde à segunda dúvida de Marina.  
Na tela:  
1. Com roe_tatame.yaml aberto, esperar a digitação e mostrar as linhas destacadas.  
2. Clicar em validar_roe.py, no explorador.  
3. Clicar no botão "Rascunho" e ler a saída.  
4. Clicar em "Versão final".  
Fala (YAML): "Este é o modelo de RoE da Rede Tatame. O objetivo é verificar se o SOC detecta um ataque que parte de uma conta do financeiro e busca as exportações de fichas no SRV-ARQ-01. O modelo é caixa-cinza. Fora do escopo ficam a rede de pagamentos e o promo-hml. As linhas destacadas mostram os critérios de parada, como qualquer impacto no *check-in* ou nas catracas, e a palavra de parada 'AMBAR'; a célula branca, com Marina, Caio e a diretoria; e blue_team_avisado: false."  
Fala (Python): "O validador tem uma lista chamada OBRIGATORIOS, com os nove campos que não podem faltar. A função faltando devolve os campos ausentes ou vazios. É ela que decide se o teste pode começar. A função no_escopo recusa primeiro os IPs das redes de fora e só depois aceita os das redes autorizadas."  
Fala (saídas): "No rascunho que a diretoria mandou, sete campos aparecem com o sinal de certo e dois com xis: critérios de parada e célula branca. A mensagem final diz que faltam 2 itens e o teste não pode começar. Na versão final, os nove campos passam, e o validador confere três alvos: o 10.10.1.20 está dentro do escopo; o 10.40.99.14 é da rede de pagamentos; o 198.51.100.23 é o *site* da agência. Os dois últimos aparecem como 'FORA DO ESCOPO: não testar'."  
Atenção: o rascunho tem "carta_de_autorizacao: e-mail do gerente de TI" e passa no validador, porque o *script* só confere se o campo existe.  
Conclusão: "Um *e-mail* do gerente de TI não é carta de autorização, e isso exige leitura humana. O código ajuda, mas não substitui a revisão."  
[Tela: gravação do laboratório do slide 14]

**Slides 15 e 16 — O relatório e o laboratório "um relatório de Red Team em três camadas" (13:30–15:20)**  
Fala (slide 15): "Um teste só vira melhoria quando o resultado é bem comunicado. O relatório tem duas camadas: o sumário executivo, em linguagem de negócio, e a seção técnica, com evidência, severidade e recomendação de cada achado. Em Red Team, entra também a linha do tempo do ataque comparada com o que o Blue Team detectou."  
Objetivo (slide 16): ver o que uma operação de Red Team entrega para a Rede Tatame.  
Na tela:  
1. Ler a aba "Sumário executivo".  
2. Clicar em "Achados técnicos".  
3. Clicar em "Linha do tempo Red x Blue".  
Fala (sumário): "O relatório RT-2026-07 tem três números no topo: objetivo atingido no dia 9, 2 de 7 ações detectadas pelo SOC e 2 achados altos e 2 médios. Embaixo, os riscos principais e as prioridades para 30 dias: MFA na VPN, contas de serviço restritas e triagem 24 horas dos alertas médios."  
Fala (achados): "Cada achado tem ID, severidade, evidência e recomendação. O F-01 é a VPN que aceita só usuário e senha. O F-02 é a conta svc-backup, com senha de 2019 e privilégio de administrador do domínio."  
Fala (linha do tempo): "Esta é a aba que mais ensina. Cada ação do Red Team ao lado do que o Blue Team viu. Cinco linhas dizem 'Nada', marcadas como lacuna. O alerta do dia 5, às 19h40, só foi triado no dia seguinte, 13 horas e meia depois. E o alerta do dia 8 foi encerrado como falso positivo. A última ação é a leitura de uma amostra de 5 fichas, como evidência mínima e sem cópia."  
Conclusão: "O SOC percebeu 2 de 7 ações. As lacunas viram o plano de trabalho do Blue Team."  
[Tela: gravação do laboratório do slide 16]

**Slides 17 e 18 — Pausa para reflexão e resolução do caso (15:20–16:20)**  
Fala: "Agora uma pausa. Uma rede de farmácias com 300 lojas pede um '*pentest* completo' para saber se o SOC terceirizado detecta ataques, e já faz varreduras mensais. Pause o vídeo e responda às três perguntas do slide." [Pausa de 3 segundos com o slide 17 na tela] (avançar) "Uma resposta possível: o *pentest* não responde, porque busca falhas em um alvo delimitado, em geral com o Blue Team avisado. O indicado é uma operação de Red Team com objetivo de negócio, por exemplo partir de uma loja e chegar à base de clientes sem ser detectado, medindo o tempo até detectar e até responder. E as regras não podem esquecer a célula branca, com um contato no fornecedor do SOC, o escopo com exclusões explícitas, os critérios de parada e as regras para dados de clientes e receitas."

**Slide 19 — Priorizando o orçamento de R$ 120.000 (16:20–16:50)**  
Fala: "Voltando à Rede Tatame e aos R$ 120.000. A opção (a) são 4 *pentests* de aplicações a R$ 30.000. A opção (b) são varreduras mensais, 12 vezes R$ 2.000, que dá R$ 24.000, mais uma operação de Red Team de R$ 96.000. As duas custam R$ 120.000. O número sozinho não decide: a pergunta de negócio decide."

**Slide 20 — Laboratório: mesmo orçamento, perguntas diferentes (16:50–18:00)**  
Objetivo: decidir como gastar os R$ 120.000 da Rede Tatame.  
Na tela:  
1. Com a pergunta "Detectamos e respondemos a um ataque?" selecionada, ler o cartão destacado e a recomendação.  
2. Clicar em "Vamos lançar 4 sistemas expostos à internet".  
3. Voltar à primeira pergunta e arrastar "Operação de Red Team" de R$ 96.000 para R$ 110.000.  
Fala: "À esquerda, os quatro controles: orçamento, preço de um *pentest*, varredura por mês e Red Team. À direita, os dois cartões com o total de cada opção. Para a pergunta sobre detecção, o cartão (b) fica em destaque e a recomendação explica: só o Red Team mede se o SOC percebe e reage. Se a pergunta for o lançamento de 4 sistemas, o destaque passa para o (a): um *pentest* por sistema antes de ir ao ar. Agora, se o Red Team subir para R$ 110.000, o cartão (b) passa a mostrar 'passa do orçamento em R$ 14.000'. É aí que entra a negociação: reduzir a duração da operação, espaçar as varreduras ou pedir mais verba."  
Conclusão: "O número sozinho não decide: a pergunta de negócio decide."  
[Tela: gravação do laboratório do slide 20]

**Slide 21 — De volta ao problema (18:00–18:50)**  
Fala: "Voltemos às dúvidas de Marina. O que está exposto? A varredura da borda achou o hml-gestao, fora do inventário, e um falso positivo; ela deve ser periódica. A falha é explorável? Só um *pentest* no hml-gestao, com escopo próprio, comprova o risco da versão antiga. O SOC percebe? Só uma operação de Red Team responde, com RoE, célula branca e critérios de parada. E com a dúvida sobre detecção, a opção de varreduras mensais mais Red Team cabe nos R$ 120.000. A resposta: para saber o que está exposto, varredura periódica; para comprovar uma falha, *pentest*; para saber se o SOC percebe e reage, Red Team. O '*pentest* do ano passado' não responde a nenhuma das duas dúvidas de Marina."

**Slides 22 a 24 — Pontos-chave, referências e encerramento (18:50–19:30)**  
Fala: "Para levar desta aula: varredura, *pentest* e Red Team respondem a perguntas diferentes; NIST SP 800-115, PTES e OWASP dão método e repetibilidade; regras de engajamento e carta de autorização são obrigatórias, e em Red Team também a célula branca; e o relatório, com a linha do tempo Red x Blue, é onde o teste vira melhoria. Na próxima aula, vamos olhar para o lado da defesa: o NIST CSF, a defesa em profundidade e o SOC. Até lá!"

## Aula 4 — Fundamentos da defesa: NIST CSF, defesa em profundidade e SOC

### Texto base

Se as aulas anteriores mostraram como o adversário pensa, agora é a vez de entender como a defesa se organiza. Um Blue Team eficaz não depende de uma única ferramenta "milagrosa", mas de camadas de proteção, de processos claros e de pessoas treinadas.

#### O NIST Cybersecurity Framework 2.0

Publicado em 2024, o **NIST CSF 2.0** organiza a gestão de riscos cibernéticos em seis funções:

- **Governar (*Govern*):** estabelecer estratégia, papéis, políticas e supervisão de riscos — a função incluída na versão 2.0.
- **Identificar (*Identify*):** conhecer ativos, riscos e dependências.
- **Proteger (*Protect*):** aplicar controles como gestão de identidades, treinamento e proteção de dados.
- **Detectar (*Detect*):** encontrar e analisar possíveis ataques e comprometimentos.
- **Responder (*Respond*):** agir sobre um incidente detectado.
- **Recuperar (*Recover*):** restaurar ativos e operações afetados.

O Blue Team atua sobretudo em Detectar e Responder, mas depende das demais funções: não é possível monitorar um ativo que ninguém sabe que existe.

[Imagem 1 — Roda das seis funções do NIST CSF 2.0, com Governar no centro. Texto alternativo: "Diagrama circular do NIST Cybersecurity Framework 2.0 com as funções Governar, Identificar, Proteger, Detectar, Responder e Recuperar". Figura de domínio público do NIST.]

#### Defesa em profundidade

A **defesa em profundidade** parte do princípio de que qualquer controle pode falhar. Por isso, a proteção é organizada em camadas sobrepostas — perímetro, rede, *endpoint*, aplicação, dados e pessoas — de modo que o atacante precise vencer várias barreiras, e cada uma gere uma nova chance de detecção. Um modelo complementar é o **Zero Trust**, que elimina a confiança implícita baseada na localização da rede: todo acesso é verificado, com o menor privilégio necessário.

[Imagem 2 — Camadas concêntricas (pessoas, perímetro, rede, *endpoint*, aplicação, dados) com o ativo crítico no centro. Texto alternativo: "Círculos concêntricos representando as camadas da defesa em profundidade".]

#### O Centro de Operações de Segurança (SOC)

O **SOC** é a estrutura — interna, terceirizada ou híbrida — que monitora o ambiente continuamente. Seu trabalho costuma ser dividido em níveis:

| Nível | Função principal |
|---|---|
| N1 — Triagem | Analisa alertas, descarta falsos positivos e escala casos suspeitos |
| N2 — Investigação | Aprofunda a análise, define escopo e inicia a contenção |
| N3 — Especialistas | Caça ameaças, faz análise forense e cria novas detecções |

As principais ferramentas são o **SIEM**, que centraliza e correlaciona registros; o **EDR**, que monitora o comportamento dos computadores e servidores; e a plataforma de **SOAR**, que automatiza respostas repetitivas. Tudo isso será aprofundado na Unidade 3.

Para saber se o SOC está funcionando, não basta contar alertas. Dois indicadores são centrais: o **MTTD** (*mean time to detect*), tempo médio entre o início de um ataque e sua detecção, e o **MTTR** (*mean time to respond*), tempo médio entre a detecção e a contenção. É justamente nesses números que os exercícios de Red Team e de *purple teaming* geram valor: cada simulação mede, de forma controlada, quanto tempo a defesa leva para perceber e reagir.

[Imagem 3 — Sala de SOC com analistas diante de múltiplos monitores com painéis de alertas. Texto alternativo: "Analistas de segurança monitorando painéis em um centro de operações". Sugestão de busca no Envato: "security operations center analysts".]

#### Pessoas e processos: o elo que as ferramentas não substituem

Ferramentas geram alertas, mas são pessoas que decidem o que fazer com eles. Um SOC maduro documenta seus **procedimentos de resposta** (*playbooks*), define quem pode isolar um servidor ou bloquear uma conta, treina a equipe com simulações e revisa cada incidente para aprender com ele. Também mantém um bom relacionamento com as demais áreas: a infraestrutura, que aplica correções; o jurídico, que avalia obrigações de notificação; e a comunicação, que fala com clientes e imprensa. Sem esses processos, mesmo a melhor tecnologia produz apenas um volume crescente de alertas que ninguém consegue tratar.

#### Exemplo numérico: o custo do tempo

Segundo o relatório *Cost of a Data Breach* 2024, da IBM, as organizações levaram, em média, **258 dias** para identificar e conter uma violação de dados. Suponha que um atacante, depois de entrar, exfiltre 2.000 registros de clientes por dia. Com 258 dias de exposição, seriam 516.000 registros. Se o SOC reduzir o tempo até a contenção para 10 dias, o volume cai para 20.000 registros — uma redução de cerca de **96%**. É por isso que as métricas de tempo de detecção e de resposta estão no centro do trabalho do Blue Team.

#### O que você verá na próxima unidade

Na Unidade 2, vamos vestir a camisa vermelha. Você vai acompanhar, de forma conceitual e sempre dentro de um cenário autorizado, as etapas de uma operação ofensiva: reconhecimento e OSINT, varredura e gestão de vulnerabilidades, engenharia social e pós-exploração — terminando com o entregável mais importante do Red Team, o relatório. Em cada etapa, vamos perguntar: "que rastro isso deixa para o Blue Team?".

#### Pontos-chave

- O NIST CSF 2.0 organiza a segurança em seis funções, com a Governança no centro.
- A defesa em profundidade pressupõe que controles falham e por isso os sobrepõe.
- O SOC, com SIEM, EDR e SOAR, é o coração operacional do Blue Team.
- Reduzir o tempo de detecção e resposta reduz diretamente o impacto de um incidente.

### Referências da aula

IBM. *Cost of a data breach report 2024*. Armonk: IBM, 2024.

NATIONAL INSTITUTE OF STANDARDS AND TECHNOLOGY. *The NIST cybersecurity framework (CSF) 2.0*. Gaithersburg: NIST, 2024. DOI: 10.6028/NIST.CSWP.29.

ROSE, Scott *et al*. *SP 800-207: zero trust architecture*. Gaithersburg: NIST, 2020. DOI: 10.6028/NIST.SP.800-207.

### Roteiro da Videoaula 4 — "258 dias: o tempo que o invasor ficou na sua casa"

Duração-alvo: 15 a 20 minutos. Deck: unidade_1/slides/aula4.html (22 slides).

**Slides 1 a 3 — Capa, audiodescrição e sumário (0:00–0:30)**  
Fala: "Olá! Nesta última aula da Unidade 1, vamos olhar para o lado da defesa: como ela se organiza com o NIST CSF, por que se monta em camadas e como funciona o SOC por dentro. No fim, vamos medir a defesa pelo tempo. São seis laboratórios na Rede Tatame."  
[Tela: deck aberto no slide 1; avançar até o sumário]

**Slide 4 — O problema de hoje na Rede Tatame (0:30–1:50)**  
Fala: "Luiza Ferraz é analista de nível 2 do SOC da Rede Tatame, o centro de operações de segurança que funciona 24 horas por dia. Segundo o relatório *Cost of a Data Breach* 2024, da IBM, as organizações levam, em média, 258 dias para identificar e conter uma violação de dados. A diretoria então pergunta a Marina Prado, a CISO: 'e nós, quanto tempo levaríamos?'. O que está em jogo é simples de entender: cada dia de intruso dentro de casa é mais um dia de fichas de alunos copiadas para fora. A pergunta da aula está em amarelo: como a Rede Tatame organiza a defesa, em camadas e no SOC, para perceber e conter um intruso em horas, e não em meses?"  
Fala (apontando o mapa): "No mapa, o caminho vermelho mostra por onde passam os registros até o SOC: das catracas para o WAF, o API gateway, o serviço de *check-in*, o Kafka, o motor de correlação e, por fim, o SIEM. Cada caixa em destaque é uma camada que pode gerar um sinal."  
[Take de apoio: sala de SOC com analistas olhando painéis de monitoramento — Envato]

**Slide 5 — As seis funções do NIST CSF 2.0 (1:50–2:50)**  
Fala: "Publicado em 2024, o NIST *Cybersecurity Framework* 2.0 organiza a gestão de riscos cibernéticos em seis funções. Governar define estratégia, papéis, políticas e supervisão de riscos, e é a função nova da versão 2.0. Identificar é conhecer ativos, riscos e dependências. Proteger inclui identidades, treinamento e proteção de dados. Detectar é encontrar e analisar possíveis ataques. Responder é agir sobre um incidente detectado. E Recuperar é restaurar ativos e operações. O Blue Team atua sobretudo em Detectar e Responder, mas depende das outras: não é possível monitorar um ativo que ninguém sabe que existe."

**Slide 6 — Laboratório: seis controles, seis funções (2:50–4:20)**  
Objetivo: ver como a defesa da Rede Tatame se organiza nas funções do CSF.  
Na tela:  
1. Ler a legenda de siglas no alto do painel.  
2. Em cada um dos seis controles, clicar em uma sigla: GV, ID, PR, DE, RS ou RC. Para mostrar a correção, errar de propósito o controle 1, marcando DE.  
3. Clicar em "Conferir" e ler as linhas.  
4. Clicar em "Recomeçar" se quiser refazer.  
Fala: "A Rede Tatame listou seis controles que já tem. Vamos encaixar cada um. O primeiro, MFA no portal e na VPN e treinamento contra *phishing*: vou marcar DE para ver o que acontece. O segundo, o *playbook* que isola o notebook e troca a senha, eu marco RS. O terceiro, a diretoria aprovando a política e definindo que a CISO responde pelos riscos, é GV. O quarto, *backups offline* testados e plano para reabrir o *check-in*, é RC. O quinto, o inventário com o dono de cada ativo, é ID. O sexto, o CEP e o SIEM correlacionando *logins* com SOC 24x7, é DE. Agora clico em Conferir: o placar mostra 5 de 6 corretos, e a primeira linha explica que a resposta é Proteger, porque o controle reduz a chance de o ataque dar certo. Cada linha traz o porquê."  
Atenção: uma pergunta ajuda o aluno a decidir: o controle evita, percebe, reage ou restaura? Se ele decide quem faz o quê, é Governar.  
Conclusão: "Detectar e Responder dependem das outras funções: não se monitora o que ninguém sabe que existe."  
[Tela: gravação do laboratório do slide 6]

**Slide 7 — Defesa em profundidade e Zero Trust (4:20–5:00)**  
Fala: "A defesa em profundidade parte do princípio de que qualquer controle pode falhar. Por isso a proteção é organizada em camadas sobrepostas: pessoas, perímetro, rede, *endpoint*, aplicação e dados. O atacante precisa vencer várias barreiras, e cada barreira é uma nova chance de detecção. Pense num banco: portaria, catracas, câmeras, vigilante e, no fim, o cofre. O modelo Zero Trust complementa as camadas: elimina a confiança baseada na localização da rede, e cada acesso é verificado, com o menor privilégio necessário."

**Slide 8 — Visualização 3D: as camadas em volta das fichas de alunos (5:00–6:10)**  
Objetivo: entender por que uma camada sozinha não basta.  
Na tela:  
1. Deixar a cena rodar 10 segundos com as seis camadas ligadas e mostrar o contador no canto superior direito.  
2. Clicar em "Perímetro" para desligar essa camada; esperar mais 10 segundos.  
3. Desligar "Pessoas", "Rede", "Endpoint" e "Aplicação", deixando só "Dados".  
4. Religar todas.  
Fala: "No centro está o db-alunos, o banco de fichas. Em volta, seis anéis, um por camada. Os pontos vermelhos que vêm de fora são tentativas de ataque; quando uma camada barra a tentativa, o ponto fica azul. O contador mostra quantas camadas estão ativas, quantos ataques foram barrados e quantos chegaram ao ativo. Com as seis ligadas, quase nada chega. Ao desligar o perímetro, como um controle que falhou, as outras camadas ainda seguram a maior parte. Mas, quando deixo só a camada de dados, o contador de ataques que chegam ao ativo sobe depressa."  
Atenção: os contadores zeram a cada clique. As chances de bloqueio de cada camada são ilustrativas, como avisa o próprio painel.  
Conclusão: "Nenhuma camada precisa ser perfeita, porque as outras cobrem a falha dela."  
[Tela: gravação do laboratório do slide 8]

**Slide 9 — O SOC em três níveis (6:10–6:50)**  
Fala: "O SOC é a estrutura, interna, terceirizada ou híbrida, que monitora o ambiente continuamente. Ele costuma ter três níveis. O N1 faz a triagem: analisa alertas, descarta falsos positivos e escala o que é suspeito. O N2 investiga: aprofunda a análise, define o escopo e inicia a contenção. O N3 reúne especialistas que caçam ameaças, fazem análise forense e criam detecções. As ferramentas principais são o SIEM, que centraliza e correlaciona registros, o EDR, que monitora computadores e servidores, e o SOAR, que automatiza respostas repetitivas."

**Slide 10 — Laboratório: a jornada de um alerta, do N1 ao N3 (6:50–8:50)**  
Objetivo: ver como os três níveis do SOC encurtam o tempo entre o primeiro sinal e a contenção.  
Na tela:  
1. Clicar em "Avançar" a cada passo, do "08:55 · Um login de outro país" até "A lição vira detecção" (contador 7/7).  
Fala: "Às 8h55, a conta de Carla Dias, do financeiro, entra no *e-mail* a partir de um endereço nos Países Baixos. Às 8h40 ela tinha entrado de São Paulo. Às 9h31, a regra de viagem impossível, que roda a cada 30 minutos, compara os dois *logins*: cerca de 9.800 km em 15 minutos. Um alerta alto cai na fila do N1. Às 9h34, o N1 confere que o endereço não é da VPN nem de fornecedor conhecido e liga para Carla, que confirma estar em São Paulo. O caso sobe para o N2. Às 9h40, Luiza segue o *playbook* PB-07, ligado ao N2 pela linha tracejada amarela, e descobre que a sessão estrangeira criou uma regra que encaminha mensagens com a palavra 'repasse' para fora. Às 10h16, o SOAR revoga as sessões, força a troca de senha e remove a regra. Detectar levou 36 minutos; conter, mais 45. Depois, Rafael Tavares, no N3, procura o mesmo endereço em outras contas e acha duas tentativas sem sucesso. E escreve uma regra nova, que volta ao SIEM pela linha roxa."  
Atenção: o IP 192.0.2.201 é de uma faixa reservada para documentação. O botão "Auto" avança sozinho; para gravar, prefira "Avançar".  
Conclusão: "Cada nível tem um papel e um prazo. Somados, eles levaram o caso do primeiro alerta à contenção em 81 minutos."  
[Tela: gravação do laboratório do slide 10]

**Slide 11 — Laboratório: o turno do analista no console (8:50–11:00)**  
Objetivo: acompanhar o trabalho do SOC no mesmo caso, agora com os registros.  
Na tela:  
1. Clicar na busca "1. Fila do N1".  
2. Clicar em "2. Logins da conta (24 h)".  
3. Clicar em "3. Regra de viagem impossível".  
4. Clicar em "4. Mesmo IP em outras contas".  
5. Clicar em "5. MTTD e MTTR do trimestre".  
Fala (busca 1): "A consulta pega os alertas com status 'New' e ordena por severidade e depois por hora. São 5 alertas. A viagem impossível de carla.dias, alta, fica no topo, à frente de alertas mais antigos de severidade média, baixa e informativa."  
Fala (busca 2): "Agora os *logins* da conta em 24 horas. Às 7h12 e às 8h40, São Paulo. Às 8h55, Amsterdã, no *e-mail*. E às 9h03, a mesma sessão de Amsterdã mexeu nas regras da caixa de entrada. É o primeiro sinal de que alguém quer ficar."  
Fala (busca 3): "Esta é a lógica da regra. Para cada usuário, ela compara cada *login* com o anterior e alerta se o local mudou em menos de 2 horas. Resultado: São Paulo às 8h40, Amsterdã às 8h55, 15 minutos, cerca de 9.800 km. Nenhum avião faz isso."  
Fala (busca 4): "O N3 amplia o escopo: o mesmo IP tentou duas outras contas, caio.mendes e financeiro.repasses, sem sucesso. As senhas são trocadas por precaução."  
Fala (busca 5): "E as métricas do trimestre: 6 incidentes, MTTD médio de 24 horas e mediana de 5,8 horas; MTTR médio de 4,1 horas e mediana de 2,2 horas. O caso de hoje, o INC-34, foi detectado em 0,6 hora e contido em 0,75 hora."  
Atenção: a média e a mediana contam histórias diferentes; o laboratório do slide 15 mostra por quê.  
Conclusão: "Do primeiro sinal à contenção foram 81 minutos. É assim que o SOC troca meses por horas."  
[Tela: gravação do laboratório do slide 11]

**Slide 12 — Laboratório: uma catraca adulterada e a camada que faltava (11:00–13:40)**  
Objetivo: ver uma camada sem telemetria e o efeito de ligá-la.  
Na tela:  
1. Na aba Cenários, no cartão "Catraca adulterada", clicar em "Iniciar cenário". Velocidade em "1 s = 15 s". Rolar até a linha do tempo e esperar os três passos (cerca de 20 segundos).  
2. Abrir a aba Telemetria. Ler o indicador "Custo por mês", ligar a fonte "Heartbeat e firmware das catracas" e ler o novo valor.  
3. Clicar em "Reiniciar". Na aba Telemetria, ligar de novo a fonte das catracas; na aba Regras do CEP, ligar a regra R10. Voltar a Cenários e iniciar o mesmo cenário.  
4. Quando aparecer o alerta da R10, abrir a aba SOC, clicar em "Investigar" e depois em "Conter".  
Fala (primeira rodada): "A catraca da academia 117 passa a enviar sinais de vida dez vezes por segundo, recebe um *firmware* não assinado e começa a gerar *check-ins* falsos. Na linha do tempo, os dois primeiros passos aparecem como 'não detectado': a fonte das catracas está desligada, então o SOC não recebe nada delas. O terceiro, os *check-ins* falsos, aparece como 'visto nos logs, sem alerta', porque o API gateway registra, mas nenhuma regra olha para isso."  
Fala (Telemetria): "Por que a fonte estava desligada? Custo e esquecimento. Repare no custo por mês: com as fontes padrão, cerca de R$ 2.462; com as 240 catracas, que mandam 8 eventos por segundo, vai para cerca de R$ 2.488. É uma camada inteira por pouco dinheiro."  
Fala (segunda rodada): "Com a fonte e a R10 ligadas, a mesma regra pega a taxa anormal de sinais e o *firmware* sem assinatura. O alerta de severidade média aparece no SOC. Investigo, vejo a lógica da regra, e contenho. Na linha do tempo, o passo dos *check-ins* falsos fica como 'interrompido pela contenção', e os indicadores de MTTD e MTTR são preenchidos."  
Atenção: o "Reiniciar" desliga de novo fontes e regras; ligue-as depois de reiniciar, ou use "Repetir com as fontes e regras atuais". Se conter muito cedo, o segundo passo também aparece como interrompido. Os valores de custo são fictícios.  
Conclusão: "Você fez o papel do N1 e do N2. O N3 procuraria o mesmo *firmware* nas outras catracas."  
[Tela: gravação do laboratório do slide 12, com zoom na linha do tempo e no indicador de custo]

**Slides 13 e 14 — MTTD, MTTR, pessoas e processos (13:40–14:30)**  
Fala: "Para saber se o SOC funciona, não basta contar alertas. Dois indicadores são centrais. O MTTD, *mean time to detect*, é o tempo médio entre o início do ataque e a detecção. O MTTR, *mean time to respond*, é o tempo médio entre a detecção e a contenção. É nesses números que os exercícios de Red Team e de *purple teaming* geram valor." (avançar) "Mas ferramentas geram alertas e são pessoas que decidem o que fazer. Um SOC maduro documenta seus *playbooks*, define quem pode isolar um servidor ou bloquear uma conta, treina com simulações e revisa cada incidente, e mantém relação com a infraestrutura, o jurídico e a comunicação."

**Slide 15 — Laboratório: *playbook* e métricas do SOC (14:30–16:10)**  
Objetivo: medir se o SOC está ficando mais rápido.  
Na tela:  
1. Com playbooks/conta_comprometida.yaml aberto, esperar a digitação e mostrar as linhas destacadas.  
2. Clicar em incidentes_2026.csv e depois em metricas_soc.py.  
3. Clicar em "Executar metricas_soc.py".  
Fala (YAML): "O *playbook* PB-07 diz quem faz o quê e em quanto tempo. O N1 tem 15 minutos para conferir os *logins*, checar o IP e confirmar com o usuário por telefone, nunca pelo *e-mail* da conta. O N2 tem 30 minutos. As linhas destacadas mostram a contenção sem aprovação, que o analista executa na hora: revogar sessões, forçar a troca de senha e remover encaminhamentos externos. E também quem comunicar: o gestor e, se houver dado de aluno exposto, o DPO e o jurídico."  
Fala (CSV e Python): "O CSV tem seis incidentes do trimestre, com hora de início, de detecção e de contenção. O *script* tem uma função, horas, que calcula a diferença entre duas datas em horas. As linhas destacadas montam duas listas: ttd, do início à detecção, e ttr, da detecção à contenção. No fim, ele usa mean e median para a média e a mediana."  
Fala (saída): "Na tabela, cada caso com o tempo para detectar e para conter. O INC-36, exfiltração para nuvem, levou 96 horas para ser detectado. Resultado: MTTD médio de 24,0 horas, mas mediana de 5,8; MTTR médio de 4,1 e mediana de 2,2. Por que tanta diferença? A média soma tudo e divide; um único caso de 96 horas puxa o valor para cima. A mediana pega o caso do meio e não se deixa levar por um extremo."  
Atenção: o terminal mostra a saída gravada; o código é real e daria o mesmo resultado com esse CSV.  
Conclusão: "Um único caso de 96 horas, o INC-36, puxa a média para cima. Por isso o SOC acompanha média e mediana."  
[Tela: gravação do laboratório do slide 15]

**Slide 16 — O custo do tempo (16:10–16:40)**  
Fala: "Agora o número que abriu a aula. Se um atacante, depois de entrar, exfiltra 2.000 fichas de alunos por dia, em 258 dias são 516.000 registros. Se a contenção levar 10 dias, são 20.000. É uma redução de cerca de 96% no volume exposto."

**Slide 17 — Laboratório: quantos registros cada dia custa (16:40–17:40)**  
Objetivo: traduzir o tempo de detecção em fichas expostas.  
Na tela:  
1. Conferir os valores do exemplo: 2.000 registros por dia, 258 dias no cenário atual e 10 dias de meta.  
2. Arrastar "Dias até conter, meta do SOC" para 30.  
3. Voltar a meta para 10.  
Fala: "Os três controles são os registros exfiltrados por dia, os dias até conter no cenário atual e a meta do SOC. Os cartões mostram 516.000 no cenário atual, 20.000 com a meta e redução de cerca de 96%. As barras e as contas embaixo repetem a multiplicação. Se a meta for 30 dias, a meta vai a 60.000 registros, e a redução cai para cerca de 88%. Indo de 30 para 10 dias, deixamos de expor mais 40.000 fichas."  
Conclusão: "A conta é linear: cada dia a menos evita o mesmo número de fichas vazadas."  
[Tela: gravação do laboratório do slide 17]

**Slide 18 — Unidade 2: vestindo a camisa vermelha (17:40–18:10)**  
Fala: "Na próxima unidade, trocamos de lado. Agora que você conhece a defesa, vamos ver como o Red Team tenta vencê-la, de forma conceitual e sempre dentro de um cenário autorizado: reconhecimento e OSINT na Aula 5, varredura e gestão de vulnerabilidades na Aula 6, engenharia social e simulação de *phishing* na Aula 7 e pós-exploração e relatório na Aula 8. Em cada etapa, a pergunta será a mesma: que rastro isso deixa para o Blue Team?"

**Slide 19 — De volta ao problema (18:10–19:00)**  
Fala: "Voltemos à pergunta da diretoria. As seis funções do NIST CSF organizam a defesa: Governar define responsáveis, e Detectar e Responder dependem de Identificar e Proteger. As camadas se cobrem, e a catraca era uma camada cega até a fonte e a regra R10 serem ligadas. O SOC em níveis levou o caso de Carla do alerta à contenção em 81 minutos. E medir o tempo mostra o resto: MTTD mediano de 5,8 horas, e passar de 258 para 10 dias evita cerca de 96% das fichas expostas. Então a resposta é: com camadas que se cobrem, telemetria em cada uma delas e um SOC em níveis que segue *playbooks* e mede MTTD e MTTR. É assim que a Rede Tatame troca meses por horas."

**Slides 20 a 22 — Pontos-chave, referências e encerramento (19:00–19:40)**  
Fala: "Para levar desta aula: o NIST CSF 2.0 organiza a segurança em seis funções, com a Governança no centro; a defesa em profundidade pressupõe que controles falham e por isso os sobrepõe; o SOC, com SIEM, EDR e SOAR, é o coração operacional do Blue Team; e reduzir o tempo de detecção e resposta reduz diretamente o impacto de um incidente. Com isso, fechamos a Unidade 1. Na Unidade 2, começamos com a Aula 5, reconhecimento e OSINT, vestindo a camisa vermelha. Nos vemos lá!"  
[Take de apoio: transição de luz azul para vermelha sobre teclado — Envato]

## Quiz não avaliativo

### Questão 1 (verdadeiro ou falso)

Uma operação de Red Team e um teste de invasão (*pentest*) têm o mesmo objetivo: encontrar o maior número possível de vulnerabilidades em um escopo delimitado.

( ) Verdadeiro  
(X) Falso

### Questão 2 (múltipla escolha)

Na matriz MITRE ATT&CK, "Acesso a credenciais" é um exemplo de:

a) procedimento.  
*b) tática.  
c) subtécnica.  
d) indicador de comprometimento.

### Feedback

**Questão 1 — Falso.** O *pentest* busca identificar e explorar o maior número possível de falhas relevantes em um alvo delimitado. A operação de Red Team persegue um objetivo de negócio, emulando um adversário específico, e avalia principalmente a capacidade da organização de detectar e responder ao ataque — incluindo pessoas e processos, e não apenas tecnologia.

**Questão 2 — Alternativa b.** As táticas representam o "porquê" do adversário, isto é, o objetivo que ele busca em determinado momento, como obter credenciais. As técnicas e subtécnicas descrevem "como" esse objetivo é alcançado (por exemplo, T1003 — extração de credenciais do sistema operacional), e os procedimentos são a implementação concreta usada por um grupo específico.

## AAI — Atividade avaliativa individual

**Pergunta:**

Uma empresa de logística sofreu um ataque de *ransomware* no qual o invasor entrou por um *e-mail* de *phishing*, roubou credenciais, moveu-se pela rede durante três semanas e, por fim, criptografou os servidores. A diretoria decidiu contratar uma operação de Red Team para evitar que isso se repita. Explique (a) por que a operação deve emular especificamente esse tipo de adversário, usando a Cyber Kill Chain ou o MITRE ATT&CK para justificar sua resposta; (b) quais elementos devem constar nas regras de engajamento para que a operação seja ética e legal; e (c) como os resultados devem ser aproveitados pelo Blue Team.

**Resposta esperada:**

(a) A operação deve emular o comportamento que efetivamente ameaça a organização, pois o objetivo é testar a capacidade de detectar e responder a ataques realistas. Mapeado no ATT&CK, o incidente envolveu acesso inicial por *phishing* (T1566), acesso a credenciais (por exemplo, T1003), movimentação lateral (por exemplo, T1021) e impacto por criptografia de dados (T1486). Pela Kill Chain, o ataque percorreu entrega, exploração, instalação, comando e controle e ações sobre os objetivos. Emular essa sequência permite verificar em quais fases a defesa poderia ter interrompido a cadeia e por que não o fez — as três semanas sem detecção indicam falhas nas fases intermediárias.

(b) Autorização formal e assinada por quem tem autoridade sobre os ativos; escopo com ativos incluídos e excluídos; objetivo da operação; período e janelas de execução; técnicas proibidas (por exemplo, criptografar dados reais ou causar indisponibilidade — o impacto deve ser apenas simulado); tratamento e descarte de dados sensíveis, em conformidade com a LGPD; critérios de parada; contatos de emergência e definição da célula branca. Sem esses elementos, as ações podem configurar o crime do art. 154-A do Código Penal.

(c) Os resultados devem ser convertidos em melhorias mensuráveis: para cada técnica executada, registrar se houve telemetria, alerta e resposta; criar ou ajustar regras de detecção para as lacunas; atualizar *playbooks* de resposta; e repetir os testes, preferencialmente em ciclos de *purple teaming*, para confirmar que as correções funcionam. Indicadores como cobertura de técnicas ATT&CK e tempo médio de detecção mostram a evolução.

## Material complementar

### Direto da fonte (livro da Biblioteca Virtual)

- **Texto provocativo:** Antes de escolher um lado — atacar para testar ou defender para proteger —, é preciso dominar o vocabulário comum aos dois: ativos, ameaças, vulnerabilidades, riscos e controles. O capítulo indicado apresenta esses conceitos de forma direta, em português, com exemplos do cotidiano das organizações. Ler a fonte ajuda você a usar os termos com precisão, algo que faz diferença em uma entrevista de emprego ou em um relatório técnico.
- **Nome do livro:** SILVA, Michel Bernardo Fernandes da. *Cibersegurança*: uma visão panorâmica sobre a segurança da informação na internet. Rio de Janeiro: Freitas Bastos, 2023. *E-book*.
- **Capítulo:** 1 — Introdução à cibersegurança
- **Link de acesso:** <https://plataforma.bvirtual.com.br/Acervo/Publicacao/208076>
- **Aula em que entra:** Aula 1

### Para mergulhar no assunto (saiba mais)

- **Texto provocativo:** Em 1986, um astrônomo que cuidava dos computadores de um laboratório na Califórnia encontrou uma diferença de 75 centavos na conta de uso do sistema. Ao puxar esse fio, descobriu um invasor que espionava redes militares — e, sem nenhuma das ferramentas que temos hoje, fez o que hoje chamamos de *threat hunting*. O livro *O ovo do cuco* mostra que a essência do Blue Team é curiosidade, método e registro cuidadoso de evidências.
- **Indicação:** STOLL, Clifford. *O ovo do cuco*. (Livro; há diversas edições em português.) **[conferir edição disponível]**
- **Link complementar:** ATT&CK Navigator — <https://mitre-attack.github.io/attack-navigator/>
- **Aula em que entra:** Aula 2

### Podcast (curadoria, até 45 min)

- **Texto provocativo:** E se o seu trabalho fosse entrar em um banco sem autorização dos funcionários — mas com autorização da diretoria? Neste episódio, um profissional de Red Team conta como testou a segurança física de um banco e o que a experiência revelou sobre pessoas, processos e confiança.
- **Nome do podcast:** Darknet Diaries
- **Nome do episódio:** EP 6 — The Beirut Bank Job **[episódio em inglês; conferir duração e, se possível, substituir por equivalente em português]**
- **Link:** <https://darknetdiaries.com/episode/6/>
- **Aula em que entra:** Aula 3

### Artigo científico

- **Texto provocativo:** O artigo que deu origem à Cyber Kill Chain mudou a forma como as empresas pensam a defesa: em vez de reagir a cada alerta isolado, passaram a analisar campanhas inteiras de adversários. Ler o texto original permite entender por que "basta quebrar um elo" — e também enxergar as limitações que o modelo tem diante dos ataques atuais.
- **Link:** <https://www.lockheedmartin.com/content/dam/lockheed-martin/rms/documents/cyber/LM-White-Paper-Intel-Driven-Defense.pdf>
- **Aula em que entra:** Aula 2
- **Referência ABNT:** HUTCHINS, Eric M.; CLOPPERT, Michael J.; AMIN, Rohan M. Intelligence-driven computer network defense informed by analysis of adversary campaigns and intrusion kill chains. *Leading Issues in Information Warfare & Security Research*, v. 1, p. 80-106, 2011.
