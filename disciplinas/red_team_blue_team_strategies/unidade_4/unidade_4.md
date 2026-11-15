# Unidade 4 — Purple Team e estratégia de segurança

Disciplina: Red Team & Blue Team Strategies  
Professor-conteudista: Afonso Cesar Lelis Brandão  
Prazo de entrega: 20/12/2026  
Template de origem: `documentos/Unidade 4/TEMPLATE - Unidade 4_nome da disciplina.docx`

> Versão de trabalho baseada na **ementa proposta** (`EMENTA.md`); ajustar quando o plano de aprendizagem oficial chegar.
> Recursos visuais indicados entre colchetes, como pede o template; a equipe de produção substitui pelas imagens finais.

## Aula 13 — *Purple teaming* e emulação de adversários

### O que você verá nesta unidade

Nesta última unidade, as duas camisas se encontram. Depois de estudar as operações ofensivas na Unidade 2 e a detecção e a resposta na Unidade 3, você vai aprender a unir as equipes no *purple teaming*: planejar a emulação de adversários com base em inteligência de ameaças, medir a capacidade de detecção e resposta com indicadores e com a cobertura da matriz MITRE ATT&CK, conduzir exercícios de simulação (*tabletop*, CTF e *cyber range*) e estruturar um programa contínuo de segurança, que fale a língua da diretoria e abra caminhos de carreira. O objetivo é que você saia da disciplina capaz de transformar testes isolados em melhoria contínua e mensurável — que é o que as organizações realmente esperam de um profissional de segurança.

### Texto base

Uma empresa contrata uma operação de Red Team. Seis semanas depois, recebe um relatório de 80 páginas com dezenas de achados. O SOC lê, concorda com quase tudo e... volta à rotina, porque ninguém tem tempo de transformar cada achado em uma detecção. Meses depois, um teste semelhante encontra as mesmas lacunas. Esse desperdício é o problema que o *purple teaming* resolve.

#### Do relatório à colaboração

Como vimos na Unidade 1, *purple teaming* é menos uma equipe fixa e mais uma **forma de trabalho**: Red Team e Blue Team atuam juntos, de forma transparente, para testar e melhorar a defesa. Em um exercício de Red Team tradicional, o Blue Team normalmente não sabe do teste, pois o que se avalia é a reação a um ataque realista. No exercício *purple*, ao contrário, os defensores sabem o que será executado e quando, e acompanham cada passo. O objetivo deixa de ser "vencer" e passa a ser **aprender rápido**.

O SCYTHE *Purple Team Exercise Framework* (PTEF), material gratuito e de uso aberto, descreve esse exercício como uma sessão colaborativa — presencial ou remota — em que as equipes percorrem uma lista de técnicas, verificam a telemetria e os alertas gerados e registram as ações de melhoria. Um papel importante é o do **facilitador**, que conduz a sessão, controla o tempo e garante que as discussões terminem em tarefas concretas.

[Imagem 1 — Duas pessoas, uma com crachá vermelho e outra com crachá azul, analisando juntas um painel de alertas em uma sala de reunião. Texto alternativo: "Profissionais de ataque e de defesa trabalhando lado a lado diante de um monitor". Sugestão de busca no Envato: "cybersecurity team collaboration meeting".]

#### O ciclo do *purple teaming*

Cada técnica testada percorre um ciclo curto, que pode ser repetido várias vezes na mesma sessão:

1. **Planejar:** escolher a técnica ATT&CK, definir o comportamento esperado e o critério de sucesso.
2. **Executar:** o Red Team executa a técnica em um ambiente autorizado.
3. **Observar:** o Blue Team verifica se houve **telemetria** (o registro existe?), **alerta** (alguma regra disparou?) e **resposta** (o analista agiria corretamente?).
4. **Ajustar:** criar ou refinar a regra, habilitar uma fonte de registros ou corrigir um *playbook*.
5. **Retestar:** executar novamente para comprovar que a melhoria funciona.

[Imagem 2 — Diagrama circular com cinco etapas: planejar, executar, observar, ajustar e retestar, com uma seta de retorno ao início. Texto alternativo: "Ciclo do purple teaming em cinco etapas, do planejamento ao reteste".]

O passo 5 é o que mais se esquece e o que mais importa: uma detecção que nunca foi testada contra o comportamento real é apenas uma **hipótese**.

#### Emulação de adversários: testar o que realmente ameaça

Em vez de executar técnicas aleatórias, a abordagem madura é a **emulação de adversários**: reproduzir o comportamento de um grupo real, conhecido por meio de inteligência de ameaças (CTI), como vimos na Unidade 3. Se a organização é um banco, faz sentido emular grupos com histórico de ataques ao setor financeiro; se é uma indústria, grupos ligados a *ransomware* e sabotagem. Essa ideia é chamada de **defesa informada por ameaças** (*threat-informed defense*).

Um **plano de emulação** descreve o adversário, seus objetivos, a sequência de técnicas ATT&CK que ele costuma usar e os procedimentos para reproduzi-las com segurança. O MITRE Center for Threat-Informed Defense mantém publicamente a *Adversary Emulation Library*, com planos baseados em grupos documentados, como APT29, FIN6 e menuPass. Vale distinguir: **emulação** reproduz o comportamento de um adversário específico; **simulação** executa técnicas genéricas, sem a fidelidade a um ator.

#### Ferramentas de apoio

| Ferramenta | Mantenedor | Uso principal |
|---|---|---|
| MITRE Caldera | MITRE (código aberto) | Plataforma para automatizar a emulação de adversários |
| Atomic Red Team | Red Canary (código aberto) | Biblioteca de testes pequenos, cada um mapeado a uma técnica ATT&CK |
| *Adversary Emulation Library* | MITRE Center for Threat-Informed Defense | Planos completos de emulação baseados em grupos reais |
| ATT&CK Navigator | MITRE | Visualização da cobertura e do plano sobre a matriz |
| Plataformas de BAS | Diversos fornecedores | Simulação contínua e automatizada de ataques (*breach and attack simulation*) |

Ferramentas automatizadas aumentam a frequência dos testes, mas não substituem o raciocínio humano: elas testam técnicas conhecidas, enquanto o adversário real improvisa. Por isso, a automação deve complementar — e não substituir — operadores e analistas experientes. E, como em qualquer atividade ofensiva, vale a regra da Unidade 1: escopo, autorização e regras de engajamento por escrito, mesmo que o exercício seja interno.

[Imagem 3 — Captura de tela de uma *layer* do ATT&CK Navigator com as técnicas de um plano de emulação destacadas. Texto alternativo: "Matriz ATT&CK com as técnicas de um plano de emulação marcadas em cor". Conteúdo da MITRE com licença de uso livre mediante atribuição.]

#### Exemplo numérico: a cobertura evoluindo a cada ciclo

Uma equipe montou um plano de emulação com **30 técnicas** associadas a um grupo de *ransomware*. Na primeira execução, 9 técnicas geraram alerta: cobertura de 9 ÷ 30 = **30%**. Durante a própria sessão, a equipe ajustou regras para 6 técnicas que já tinham telemetria; no reteste, a cobertura subiu para 15 ÷ 30 = **50%**. No segundo ciclo, um mês depois, novas fontes de registro elevaram o número para 21 (**70%**); no terceiro, para 25 (**83%**). As 5 técnicas restantes foram tratadas com controles preventivos e aceitas como risco residual pela liderança. Note que cada ponto percentual só conta porque **foi retestado**.

#### Pontos-chave

- *Purple teaming* é colaboração transparente entre ataque e defesa, focada em aprender rápido.
- O ciclo planejar → executar → observar → ajustar → retestar transforma achados em detecções comprovadas.
- A emulação de adversários prioriza o comportamento de quem realmente ameaça a organização.
- Caldera, Atomic Red Team e a *Adversary Emulation Library* apoiam, mas não substituem, o trabalho humano.

### Referências da aula

APPLEBAUM, Andy *et al*. Intelligent, automated red team emulation. *In*: ANNUAL CONFERENCE ON COMPUTER SECURITY APPLICATIONS, 32., 2016, Los Angeles. *Proceedings* [...]. New York: ACM, 2016.

MITRE CENTER FOR THREAT-INFORMED DEFENSE. *Adversary emulation library*. Disponível em: <https://github.com/center-for-threat-informed-defense/adversary_emulation_library>. Acesso em: 13 nov. 2026.

MITRE. *Caldera*. Disponível em: <https://caldera.mitre.org/>. Acesso em: 13 nov. 2026.

RED CANARY. *Atomic Red Team*. Disponível em: <https://github.com/redcanaryco/atomic-red-team>. Acesso em: 13 nov. 2026.

SCYTHE. *Purple team exercise framework (PTEF)*. Disponível em: <https://github.com/scythe-io/purple-team-exercise-framework>. Acesso em: 13 nov. 2026.

### Roteiro da Videoaula 13 — "O relatório de 80 páginas que ninguém aplicou"

Duração-alvo: 15 a 20 minutos. Deck: unidade_4/slides/aula13.html (20 slides).

**Slides 1 a 3 — Capa, audiodescrição e sumário (0:00–0:40)**
Fala: "Olá! Bem-vindo à Aula 13, que abre a Unidade 4 da disciplina. Hoje o tema é *purple teaming* e emulação de adversários. Como sempre, vamos trabalhar na plataforma fictícia da Rede Tatame, e esta aula tem seis laboratórios. No sumário você vê o caminho: um problema real da Rede Tatame, o ciclo do *purple teaming*, o plano de emulação e a medição da cobertura antes e depois do reteste."
[Tela: capa; avançar devagar pela audiodescrição; parar 5 segundos no sumário]

**Slide 4 — O problema de hoje na Rede Tatame (0:40–2:00)**
Fala: "Quero começar com uma situação que acontece em muitas empresas. Rafael Tavares é o engenheiro de detecção da Rede Tatame, a pessoa que escreve as regras que geram alertas no SOC, o centro de operações de segurança. A última operação de Red Team rendeu um relatório de 80 páginas. O SOC concordou com quase tudo e voltou à rotina. Agora chega um boletim de CTI, inteligência de ameaças, avisando que o Grupo Cobalto Austral, um grupo de *ransomware*, ataca redes de academias com senhas vazadas de VPN. O que está em jogo são os servidores da sede e as fichas de 36 mil alunos, cerca de 30% menores de idade. Repare no mapa à direita: o caminho em destaque vai da internet à VPN, passa pelo AD e chega ao SRV-ARQ-01, em vermelho. A pergunta da aula é esta: como transformar os achados do Red Team em detecções comprovadas contra o Grupo Cobalto Austral? Guarde os papéis: Bruno Sato no Red Team, Luiza Ferraz no Blue Team, Rafael Tavares como facilitador e Marina Prado, a CISO, que autoriza."
[Take de apoio: equipe olhando um relatório extenso sobre a mesa — Envato]

**Slide 5 — O que você verá nesta unidade (2:00–2:40)**
Fala: "Esta é a última unidade, e nela as duas camisas se encontram. Na Unidade 2 você viu as operações ofensivas; na Unidade 3, a detecção e a resposta. Agora vamos unir as equipes. Na Aula 13, planejamos a emulação com base em inteligência de ameaças. Na 14, medimos detecção e resposta. Na 15, conduzimos exercícios de simulação. Na 16, montamos um programa contínuo que a diretoria entenda. A meta é que você saia capaz de transformar testes isolados em melhoria contínua e mensurável."

**Slide 6 — Do relatório à colaboração (2:40–3:40)**
Fala: "Como vimos na Unidade 1, *purple teaming* é menos uma equipe fixa e mais uma forma de trabalho. Olhe a tabela. No exercício de Red Team tradicional, o Blue Team normalmente não sabe de nada e se avalia a reação a um ataque realista. No exercício *purple*, o Blue Team sabe o que será executado e quando, e cada técnica é avaliada em telemetria, alerta e resposta. O objetivo passa a ser aprender rápido. O SCYTHE *Purple Team Exercise Framework*, o PTEF, descreve essa sessão colaborativa e o papel do facilitador, que controla o tempo e garante que cada discussão termine em uma tarefa concreta."

**Slide 7 — O ciclo do *purple teaming* (3:40–4:40)**
Fala: "Cada técnica percorre cinco passos. Planejar: escolher a técnica ATT&CK, o comportamento esperado e o critério de sucesso. Executar: o Red Team roda a técnica em ambiente autorizado. Observar: o Blue Team verifica se houve telemetria, se alguma regra gerou alerta e se o analista responderia bem. Ajustar: criar ou refinar a regra, ligar uma fonte de registros ou corrigir um *playbook*. Retestar: executar de novo para comprovar a melhoria. O passo 5 é o mais esquecido. Pense no treino de futebol, em que o goleiro pede 'de novo, do mesmo jeito' até conseguir defender. Uma detecção nunca testada contra o comportamento real continua sendo uma hipótese."
[Take de apoio: goleiro treinando defesas repetidas — Envato]

**Slide 8 — Laboratório: uma técnica percorre o ciclo inteiro (4:40–6:30)**
Objetivo: mostrar, com uma técnica do Cobalto Austral, como um achado vira detecção comprovada.
Na tela:
1. Apontar o nó central "T1021.001", com o subtítulo "hipótese".
2. Clicar em "Avançar" (passo 1 · Planejar).
3. Clicar em "Avançar" (passo 2 · Executar).
4. Clicar em "Avançar" (passo 3 · Observar) e apontar o nó central, que muda para "parcial: telemetria sem alerta".
5. Clicar em "Avançar" (passo 4 · Ajustar).
6. Clicar em "Avançar" (passo 5 · Retestar) e apontar o nó central, que passa a "detecção comprovada".
7. Clicar em "Avançar" uma última vez ("O ciclo recomeça").
Fala: "Vamos seguir uma técnica só: a T1021.001, uso de RDP de uma estação para um servidor. No planejamento, o comportamento esperado é um logon remoto do NB-TI-012 no SRV-ARQ-01, registrado no tópico tatame.auditoria, e o alerta da regra R5. O critério de sucesso é alerta em até 5 minutos. Na execução, às 14h32, Bruno Sato avisa no canal da sessão e abre o RDP com a conta de teste svc-purple; nada é lido nem alterado no servidor. Agora a observação: a telemetria existe, o logon chegou ao tópico. Mas não houve alerta, porque a R5 estava desligada no CEP. Por isso a técnica fica parcial. No ajuste, Rafael Tavares liga a R5 com uma exceção para o servidor de salto que a TI de Caio Mendes usa na manutenção, para não gerar ruído. No reteste, a mesma sessão é repetida e o alerta chega à fila de Luiza Ferraz em 38 segundos, dentro do critério. Só agora a detecção está comprovada."
Atenção: o modo "Auto" avança sozinho; para gravar, prefira "Avançar" e espere a animação dos pacotes terminar antes do próximo clique. O texto de cada passo aparece na barra abaixo do diagrama.
Conclusão: "A técnica só conta como coberta depois do reteste. Essa é a primeira parte da resposta à pergunta da aula."
[Tela: gravação do laboratório do slide 8]

**Slide 9 — Emulação de adversários (6:30–7:20)**
Fala: "Quais técnicas testar? A abordagem madura é a emulação de adversários: reproduzir o comportamento de um grupo real, conhecido por CTI. Um banco emula grupos com histórico no setor financeiro; uma rede de academias, como a Rede Tatame, emula quem ataca academias. Um plano de emulação descreve o adversário, os objetivos, a sequência de técnicas ATT&CK e como reproduzi-las com segurança. O MITRE Center for Threat-Informed Defense mantém a *Adversary Emulation Library*, com planos de grupos como APT29, FIN6 e menuPass. Repare na diferença: emulação imita um ator específico; simulação executa técnicas genéricas."

**Slide 10 — Laboratório: do boletim de CTI à *layer* do Navigator (7:20–9:40)**
Objetivo: transformar o boletim de CTI em um plano de teste e medir a cobertura testada.
Na tela:
1. Com `plano/cobalto-austral.yaml` aberto, rolar devagar pelo arquivo.
2. No explorador, abrir `resultados/sessao-2026-11-18.csv`.
3. Abrir `gerar_layer.py` e parar na função `status`.
4. No terminal, clicar em "Layer da 1ª execução" (`python gerar_layer.py`).
5. Clicar em "Layer após o reteste" (`python gerar_layer.py --reteste`).
6. Abrir `layers/cobalto-austral-reteste.json`.
Fala: "O plano é um arquivo YAML. No topo, a fonte, o boletim BI-2026-041, e a autorização APR-3107, assinada por Marina Prado. Depois vêm o adversário, com a motivação e a forma de entrada, a senha vazada em VPN sem MFA. O escopo é a sede, 10.10.0.0/16, e o fora do escopo deixa de fora a rede de pagamentos e a API do parceiro. Em seguida, cinco técnicas. Cada uma tem a tática, o teste inofensivo que será feito e a telemetria esperada, com a regra que deveria disparar. Por exemplo, a T1021.001 espera o evento 4624 tipo 10 no AD e a regra R5. O CSV guarda o resultado da sessão: para cada técnica, se houve telemetria, alerta, reteste e qual ação ficou. Agora o código. A função `status` decide tudo. Se houve alerta, ou se estamos no modo `--reteste` e o reteste deu certo, a técnica é 'detectado'. Se não houve alerta mas há telemetria, é 'parcial'. Sem telemetria, 'sem_visibilidade'. Cada estado vira uma cor e uma pontuação: 100, 50 ou 0. No fim, a cobertura testada conta as técnicas com 100 pontos e a visibilidade conta as que têm 50 ou mais. Na primeira execução saem dois detectados, T1078 e T1490; duas parciais, T1087.002 e T1021.001; e a T1567.002 sem visibilidade. Cobertura testada de 2 em 5, 40%, e visibilidade de 4 em 5, 80%. Com `--reteste`, as duas parciais viram detectadas e a cobertura vai a 4 em 5, 80%. A visibilidade continua em 80%, porque a T1567.002 segue sem telemetria."
Atenção: o código é ilustrativo e roda no editor simulado; o JSON gerado pode ser importado no ATT&CK Navigator pelo menu *Open Existing Layer*, como a saída sugere. Nenhum teste aqui executa ataque: o plano só descreve casos inofensivos.
Conclusão: "O plano diz o que testar; a *layer* mostra o que já foi comprovado."
[Tela: gravação do laboratório do slide 10]

**Slide 11 — Laboratório: a planilha da sessão *purple* (9:40–11:30)**
Objetivo: registrar, técnica por técnica, o que o SOC viu na sessão de 18/11.
Na tela:
1. Clicar em "Executar" na linha T1078 e ler o *feed* abaixo da tabela.
2. Clicar em "Executar" em T1087.002, T1021.001, T1567.002 e T1490, um de cada vez.
3. Na linha T1087.002, clicar em "Ajustar e retestar".
4. Na linha T1021.001, clicar em "Ajustar e retestar".
5. Apontar os três indicadores na base: Cobertura testada, Visibilidade e Ações retestadas.
Fala: "Esta é a planilha que o facilitador preenche durante a sessão. Cada linha é uma técnica, e as colunas são as do ciclo: telemetria, alerta, resposta, ação de melhoria e se foi retestado. Quando clico em Executar, o *feed* mostra Bruno Sato rodando o caso de teste com a conta svc-purple e, logo depois, o que o CEP fez. Na T1078, o CEP gera o alerta da R11, login sem MFA, e Luiza Ferraz bloqueou a conta de teste em 5 minutos. Na T1087.002 e na T1021.001, o evento chega ao tópico tatame.auditoria, mas nenhuma regra ativa dispara: alerta 'não'. Na T1567.002, nem o evento chega, porque a fonte de buckets e saída de rede está desligada. A T1490 gera o alerta da R7. Com tudo executado, a cobertura testada fica em 2 de 5, 40%, e a visibilidade em 4 de 5. Agora ajusto as duas linhas parciais. Rafael liga a regra, Bruno retesta e o alerta aparece. A coluna Retestado muda para 'sim' e a cobertura sobe para 4 de 5, 80%. Ações retestadas: 2 de 3."
Atenção: a T1567.002 fica marcada como "próximo ciclo" e não tem botão de ajuste. Isso é proposital: sem telemetria, nenhuma regra resolve na hora.
Conclusão: "Cada lacuna vira uma ação com dono e prazo, e só sai da lista depois do reteste."
[Tela: gravação do laboratório do slide 11]

**Slide 12 — Laboratório: plataforma Rede Tatame, cobertura antes e depois do reteste (11:30–13:40)**
Objetivo: fazer o ciclo inteiro no simulador da disciplina e medir a cobertura antes e depois.
Na tela:
1. Na aba "Cobertura ATT&CK", apontar o indicador "Cobertura com regra": 38%.
2. Trocar a velocidade, no seletor ao lado do relógio, para "1 s = 1 min".
3. Ir à aba "Cenários" e clicar em "Iniciar cenário" no cartão "Emulação do Grupo Cobalto Austral".
4. Aguardar os passos do cenário aparecerem e voltar a "Cobertura ATT&CK" para ver o resultado da primeira execução.
5. Ir à aba "Regras do CEP" e ligar a R5 e a R13.
6. Voltar a "Cobertura ATT&CK": T1087.002 e T1021.001 aparecem como "detectáveis".
7. Voltar a "Cenários" e iniciar de novo a "Emulação do Grupo Cobalto Austral" (o reteste).
8. Abrir "Cobertura ATT&CK" mais uma vez.
Fala: "Agora o mesmo ciclo na plataforma que acompanha toda a disciplina. A aba Cobertura ATT&CK lista as técnicas dos cenários com quatro estados. Comprovada: regra ativa e já testada com sucesso. Detectável: regra e fonte ativas, ainda sem teste. Parcial: há telemetria, mas falta regra. Cega: nem telemetria. No início, a cobertura com regra é 38%. Rodo a emulação do Cobalto Austral com o relógio acelerado e acompanho no cenário quais passos geraram alerta. Em seguida ligo a R5 e a R13 em Regras do CEP. Repare: na Cobertura, a T1087.002 e a T1021.001 viram só 'detectáveis'. A regra existe, mas ninguém provou que ela funciona. Só depois de rodar a emulação de novo elas passam a 'comprovadas', e a taxa vai a 50%."
Atenção: se o cenário ainda estiver rodando, espere terminar antes de mudar de aba; para repetir do zero, use "Reiniciar". A plataforma é simulada e não toca nenhum sistema real.
Conclusão: "Regra ligada sem reteste ainda é hipótese. A cobertura só subiu de 38% para 50% depois do reteste."
[Tela: gravação do laboratório do slide 12]

**Slide 13 — Ferramentas de apoio (13:40–14:30)**
Fala: "Algumas ferramentas ajudam a fazer isso em escala. O MITRE Caldera automatiza a emulação de adversários. O Atomic Red Team, da Red Canary, é uma biblioteca de testes pequenos, cada um mapeado a uma técnica ATT&CK. A *Adversary Emulation Library* traz planos completos. O ATT&CK Navigator mostra a cobertura na matriz, como a *layer* que geramos. E as plataformas de BAS, *breach and attack simulation*, rodam simulações contínuas. A automação aumenta a frequência dos testes, mas testa técnicas conhecidas, enquanto o adversário real improvisa. E vale a regra da Unidade 1: escopo, autorização e regras de engajamento por escrito, mesmo em exercício interno."
[Take de apoio: páginas públicas do Caldera, do Atomic Red Team e da Adversary Emulation Library]

**Slide 14 — Laboratório: o executor de casos de teste da sessão (14:30–16:10)**
Objetivo: ver como a sessão roda com segurança, com autorização, escopo e casos de teste inofensivos.
Na tela:
1. Avançar o comando `purple-runner verificar-roe --autorizacao APR-3107`.
2. Avançar `purple-runner listar --plano plano/cobalto-austral.yaml`.
3. Avançar `purple-runner executar T1567.002-01`.
4. Avançar `purple-runner executar T1021.001-01`.
5. Avançar `purple-runner retestar T1021.001-01`.
6. Avançar `purple-runner relatorio --sessao 2026-11-18`.
Fala: "Este terminal mostra o executor que a equipe usa na sessão, um programa fictício chamado `purple-runner`. O primeiro comando confere as regras de engajamento: a autorização APR-3107 está válida, o escopo é a sede com a conta de teste svc-purple, a rede de pagamentos fica fora, a janela vai das 14h às 18h e os observadores do SOC estão conectados. Nada roda sem isso. O segundo lista os cinco casos do plano, cada um com tática, regra esperada e descrição do teste inofensivo, sem nenhum dado real de aluno. Agora a T1567.002: o caso é executado, o executor espera até 5 minutos e não chega nenhum evento. Status: sem visibilidade, e a ação sugerida é ligar a fonte e a regra R9. Na T1021.001, a telemetria chega às 14:32:52, mas não há alerta, porque a R5 está desligada. Status: parcial. Rafael liga a R5 e o reteste mostra o alerta às 14:51:51, 38 segundos depois do evento. Status: detectado. O relatório final resume: 5 técnicas, 4 com telemetria, 4 detectadas após o reteste e a T1567.002 pendente, com dono Rafael Tavares e prazo 02/12/2026."
Atenção: o executor e as saídas são ilustrativos; nenhum comando executa ataque. Explique que os casos de teste são catalogados e inofensivos.
Conclusão: "Só os casos retestados entram na cobertura."
[Tela: gravação do laboratório do slide 14]

**Slide 15 — Exemplo numérico: a cobertura evoluindo a cada ciclo (16:10–17:00)**
Fala: "Vamos ampliar a escala. Uma equipe montou um plano com 30 técnicas de um grupo de *ransomware*. Na primeira execução, 9 técnicas geraram alerta: 9 dividido por 30, 30%. No reteste do mesmo ciclo, com 6 regras ajustadas, foram 15, ou 50%. Um mês depois, com novas fontes de registro, 21, ou 70%. No ciclo 3, 25 técnicas, 83%. As 5 restantes foram tratadas com controles preventivos e aceitas como risco residual pela liderança. Cada ponto percentual só conta porque foi retestado."

**Slide 16 — Laboratório 3D: trinta técnicas, quatro momentos (17:00–17:50)**
Objetivo: ver a cobertura crescer ciclo a ciclo, como no exemplo numérico.
Na tela:
1. Com "Ciclo 1 · 1ª execução" selecionado, apontar a legenda: 9 com alerta, 21 sem alerta, 30%.
2. Clicar em "Ciclo 1 · reteste" (50%).
3. Clicar em "Ciclo 2" (70%).
4. Clicar em "Ciclo 3" (83%) e apontar os blocos cinzas.
5. Arrastar para girar a cena.
Fala: "Cada bloco é uma técnica, organizada pelas táticas da matriz na base. Verde e alto significa alerta comprovado; vermelho e baixo, sem alerta. A cada botão, mais blocos sobem e ficam verdes, e o título mostra a cobertura. No ciclo 3, os blocos cinzas são as 5 técnicas aceitas como risco residual."
Atenção: as alturas sobem com animação; espere cerca de um segundo após cada clique.
Conclusão: "Ciclos curtos e retestados levam a cobertura de 30% a 83%."
[Tela: gravação do laboratório do slide 16]

**Slide 17 — De volta ao problema (17:50–18:50)**
Fala: "Voltemos a Rafael Tavares e ao relatório de 80 páginas. O boletim de CTI virou um plano com cinco técnicas do Cobalto Austral, escopo e regra esperada. Na sessão *purple*, Red e Blue olharam juntos cada técnica: telemetria, alerta e resposta. A R5 e a R13 foram ligadas e retestadas, e a cobertura da plataforma foi de 38% para 50%. A T1567.002 ficou sem telemetria e virou ação com dono e prazo. Então, como transformar os achados do Red Team em detecções comprovadas? Com o ciclo do *purple teaming*: cada achado vira teste planejado, regra ajustada e reteste, e só o que foi retestado conta como detecção."

**Slide 18 — Pontos-chave (18:50–19:20)**
Fala: "Para levar desta aula: *purple teaming* é colaboração transparente entre ataque e defesa. O ciclo planejar, executar, observar, ajustar e retestar transforma achados em detecções comprovadas. A emulação prioriza quem realmente ameaça a organização. E as ferramentas apoiam o trabalho humano, sem substituí-lo."

**Slides 19 e 20 — Referências e encerramento (19:20–20:00)**
Fala: "As referências estão no slide, com destaque para o PTEF e a *Adversary Emulation Library*. Fica uma pergunta para a próxima aula: se cada ciclo aumenta a cobertura, como provar isso para a diretoria? Na Aula 14, vamos falar de métricas de detecção e resposta e de cobertura ATT&CK. Até lá!"
[Tela: slide de encerramento por 5 segundos]

## Aula 14 — Métricas de detecção e resposta e cobertura ATT&CK

### Texto base

"Bloqueamos 2 milhões de ataques este ano." Esse tipo de número aparece em muitos relatórios de segurança, mas diz pouco: conta tentativas automatizadas que qualquer filtro barra e nada revela sobre a capacidade de enfrentar um adversário competente. Boas métricas respondem a perguntas de decisão: **estamos melhorando? onde investir? qual risco ainda aceitamos?**

#### Métricas de tempo

Na Unidade 1, você conheceu o **MTTD** (*mean time to detect*), o tempo médio entre o início de uma atividade maliciosa e sua detecção, e o **MTTR** (*mean time to respond*), o tempo médio entre a detecção e a contenção. Há ainda o *dwell time* (tempo de permanência), período em que o atacante permanece no ambiente sem ser descoberto. Os relatórios M-Trends, da Mandiant, mostram que a mediana global de *dwell time* caiu de centenas de dias, no início da década de 2010, para cerca de dez dias em 2023 — evidência de que investir em detecção funciona.

Dois cuidados são essenciais. Primeiro, médias são sensíveis a valores extremos: um único incidente esquecido por 90 dias distorce a média do trimestre, por isso vale acompanhar também a **mediana**. Segundo, é preciso definir com precisão os marcos de início e fim; se cada analista marca o "momento da detecção" de um jeito, a métrica não é comparável ao longo do tempo.

#### Métricas de qualidade da detecção

| Métrica | Fórmula ou definição | O que revela |
|---|---|---|
| Precisão dos alertas | verdadeiros positivos ÷ total de alertas | Quanto do trabalho do SOC é útil |
| Taxa de falsos positivos | falsos positivos ÷ total de alertas | Ruído e risco de fadiga de alertas |
| Cobertura ATT&CK testada | técnicas com detecção validada ÷ técnicas priorizadas | Lacunas frente às ameaças relevantes |
| Visibilidade | técnicas com telemetria disponível ÷ técnicas priorizadas | Se há dados para detectar |
| Taxa de reteste | ações de melhoria retestadas ÷ ações concluídas | Se as correções foram comprovadas |

A **fadiga de alertas** é um risco real: quando a maior parte dos alertas é falsa, os analistas passam a fechá-los rapidamente e acabam ignorando o verdadeiro. Por isso, reduzir ruído é uma melhoria de segurança, e não apenas de produtividade.

[Imagem 1 — Painel de indicadores (*dashboard*) com gráficos de MTTD, MTTR e precisão de alertas ao longo de seis meses. Texto alternativo: "Painel com gráficos de linha mostrando a evolução de indicadores de detecção e resposta". Sugestão de busca no Envato: "security dashboard analytics".]

#### Cobertura ATT&CK: útil, desde que bem interpretada

Mapear as detecções na matriz ATT&CK, com o ATT&CK Navigator, gera um mapa de calor muito comunicativo. Mas ele tem armadilhas. A primeira é **contar a técnica como coberta porque existe uma regra**, sem nunca tê-la testado — por isso o indicador relevante é a cobertura **testada**, alimentada pelos ciclos de *purple teaming*. A segunda é **tratar todas as técnicas como iguais**: uma técnica pode ser executada de muitas formas (procedimentos), e uma regra pode detectar apenas uma delas. A terceira é **buscar 100% da matriz**: o objetivo é cobrir as técnicas priorizadas pela inteligência de ameaças, e não todas as existentes.

Frameworks abertos ajudam a tornar essa avaliação mais rigorosa. O DeTT&CT, por exemplo, propõe pontuar separadamente a visibilidade (qualidade das fontes de dados) e a detecção de cada técnica, em níveis, em vez de usar apenas "coberto/não coberto".

[Imagem 2 — Duas *layers* do ATT&CK Navigator lado a lado: "antes" com poucas células verdes e "depois" com mais células verdes e amarelas. Texto alternativo: "Comparação de mapas de calor de cobertura ATT&CK antes e depois de ciclos de purple teaming".]

#### Modelos de maturidade

Métricas operacionais mostram o desempenho; **modelos de maturidade** mostram a capacidade da organização de sustentá-lo. O NIST CSF 2.0 descreve quatro níveis (*tiers*) para o rigor da governança e da gestão de riscos cibernéticos: Parcial, Informado por riscos, Repetível e Adaptativo. Na operação de SOC, modelos como o SOC-CMM avaliam pessoas, processos, tecnologia e serviços. O valor de um modelo de maturidade não está na nota, mas no diálogo que ele provoca sobre **onde a organização quer chegar** e o que falta para isso.

[Imagem 3 — Escada com quatro degraus rotulados Parcial, Informado por riscos, Repetível e Adaptativo. Texto alternativo: "Escada representando os quatro níveis de implementação do NIST CSF 2.0".]

#### Do número à decisão

Um bom painel de métricas tem poucos indicadores, cada um com **dono, meta, fonte de dados e periodicidade**. Para a equipe técnica, interessam indicadores detalhados, como a precisão de cada regra. Para a diretoria, interessam tendências e risco: "a cobertura das técnicas mais usadas contra o nosso setor subiu de 45% para 72% no semestre" comunica mais do que qualquer número de alertas. Lembre-se também da Lei de Goodhart: quando uma métrica vira meta, ela tende a deixar de ser uma boa métrica. Se o SOC for cobrado apenas por MTTR, pode fechar incidentes cedo demais.

#### Exemplo numérico: antes e depois do *purple teaming*

Em janeiro, um SOC recebia **1.200 alertas por mês**, dos quais 180 eram verdadeiros positivos: precisão de 180 ÷ 1.200 = **15%**. O MTTD mediano era de **18 horas** e o MTTR, de **9 horas**. Após três ciclos de *purple teaming*, com ajuste de regras e automação da triagem, o volume caiu para **600 alertas**, com 150 verdadeiros positivos: precisão de 150 ÷ 600 = **25%**. O MTTD caiu para **4 horas** (redução de (18 − 4) ÷ 18 ≈ **78%**) e o MTTR, para **3 horas** (redução de 67%). Observe que o número de verdadeiros positivos caiu de 180 para 150: parte dos "positivos" anteriores eram duplicados de um mesmo incidente, consolidados pela nova correlação. Por isso, toda métrica precisa de contexto.

#### Pontos-chave

- Métricas devem apoiar decisões, e não apenas contar eventos.
- MTTD, MTTR e *dwell time* medem velocidade; precisão e taxa de falsos positivos medem qualidade.
- Cobertura ATT&CK só tem valor quando é **testada** e focada nas técnicas priorizadas.
- Modelos de maturidade, como os *tiers* do NIST CSF 2.0, orientam a evolução da capacidade.

### Referências da aula

HUBBARD, Douglas W.; SEIERSEN, Richard. *How to measure anything in cybersecurity risk*. Hoboken: Wiley, 2016.

MANDIANT. *M-Trends 2024: special report*. Reston: Mandiant, 2024.

MITRE. *ATT&CK Navigator*. Disponível em: <https://mitre-attack.github.io/attack-navigator/>. Acesso em: 13 nov. 2026.

NATIONAL INSTITUTE OF STANDARDS AND TECHNOLOGY. *The NIST cybersecurity framework (CSF) 2.0*. Gaithersburg: NIST, 2024. DOI: 10.6028/NIST.CSWP.29.

RABOBANK CYBER DEFENCE CENTRE. *DeTT&CT: detect tactics, techniques & combat threats*. Disponível em: <https://github.com/rabobank-cdc/DeTTECT>. Acesso em: 13 nov. 2026.

### Roteiro da Videoaula 14 — "2 milhões de ataques bloqueados: e daí?"

Duração-alvo: 15 a 20 minutos. Deck: unidade_4/slides/aula14.html (20 slides).

**Slides 1 a 3 — Capa, audiodescrição e sumário (0:00–0:40)**
Fala: "Olá! Esta é a Aula 14, sobre métricas de detecção e resposta e cobertura ATT&CK. Hoje vamos sair de números que impressionam e chegar a números que ajudam a decidir. O sumário mostra o caminho: o problema da Rede Tatame, as métricas de tempo e de qualidade, a cobertura ATT&CK, os modelos de maturidade e seis laboratórios."
[Take de apoio: painel de indicadores em monitor de sala de operações — Envato]

**Slide 4 — O problema de hoje na Rede Tatame (0:40–2:00)**
Fala: "Conheça Marina Prado, a CISO, ou seja, a diretora de segurança da informação da Rede Tatame. Todo trimestre ela leva um relatório à diretoria, e o último abria com 'bloqueamos 2 milhões de ataques'. Um diretor fez três perguntas: estamos melhorando, onde investir e qual risco ainda aceitamos? O número não respondia a nenhuma delas. Por isso a nossa pergunta de hoje é esta: quais números mostram à diretoria se a detecção e a resposta da Rede Tatame estão melhorando? No mapa à direita, o ponto vermelho é o SIEM do SOC, o centro de operações de segurança de Luiza Ferraz. Ele recebe os alertas do motor CEP e do EDR, e é dali que saem os números do relatório."
[Tela: destacar com o cursor o caminho Kafka, CEP e SIEM no mini-mapa]

**Slide 5 — Laboratório: vaidade ou decisão? (2:00–3:40)**
Objetivo: separar, no relatório de Marina, os números que impressionam dos que ajudam a decidir.
Na tela (passo a passo do que clicar, na ordem):
1. Ler em voz alta o primeiro indicador, "2 milhões de ataques bloqueados no ano", e pausar dois segundos antes de clicar.
2. Clicar em "Vaidade" e ler a explicação que aparece no cartão.
3. Repetir com os outros cinco indicadores: "MTTD mediano dos incidentes confirmados: 4 h (meta: até 6 h)" em "Decisão"; "1.450 regras de detecção ativas no SIEM" em "Vaidade"; "Precisão dos alertas por regra, com as 5 piores destacadas" em "Decisão"; "38 mil e-mails filtrados por dia no mx1.tatame.com.br" em "Vaidade"; "Cobertura testada das técnicas priorizadas pela CTI: 72%" em "Decisão".
4. Mostrar os dois indicadores do rodapé: "Acertos" chega a "6 de 6" e "Indicadores de decisão no relatório" mostra "3 de 6".
Fala: "Para cada linha eu faço uma pergunta simples: se este número piorar, alguém muda alguma coisa? Dois milhões de ataques bloqueados contam tentativas automáticas que qualquer filtro barra. Já o MTTD mediano tem meta, usa a mediana e, se piorar, leva a revisar regras, turnos ou a automação da triagem. Repare que 1.450 regras ativas podem significar apenas mais ruído; o que importa é quantas foram testadas. Os indicadores de decisão têm meta, dono e consequência."
Atenção: cada cartão aceita um único clique; para refazer, recarregue a página. Dê tempo ao aluno para pensar antes de cada clique. Os números são fictícios.
Conclusão: "Só três dos seis indicadores ajudam a diretoria a decidir. Esse é o primeiro corte no relatório."
[Tela: gravação do laboratório do slide 5]

**Slide 6 — Métricas de tempo: MTTD, MTTR e *dwell time* (3:40–4:40)**
Fala: "Vamos às métricas de velocidade. O MTTD, do inglês *mean time to detect*, é o tempo médio entre o início de uma atividade maliciosa e sua detecção. O MTTR, *mean time to respond*, vai da detecção até a contenção. O *dwell time* é o tempo de permanência do atacante sem ser descoberto; segundo os relatórios M-Trends da Mandiant, a mediana global caiu de centenas de dias, no início da década de 2010, para cerca de dez dias em 2023. Guarde dois cuidados: a média é sensível a valores extremos, e os marcos de início e fim precisam ser definidos do mesmo jeito por todos os analistas."

**Slide 7 — Laboratório: média e mediana de dez incidentes (4:40–7:00)**
Objetivo: medir o tempo de detecção e de resposta sem ser enganado por um caso extremo.
Na tela (passo a passo do que clicar, na ordem):
1. Esperar o editor digitar o `metricas.py`, que abre sozinho ao entrar no slide.
2. No explorador, clicar em `marcos.yaml` e ler as três definições: `inicio_atividade`, `deteccao` e `contencao`.
3. Clicar em `dados/incidentes_2026T2.csv` e apontar a linha destacada do INC-07.
4. Voltar ao `metricas.py` e, no terminal, clicar no botão "Calcular o trimestre" (o comando executado é `python metricas.py`).
5. Ler a saída de baixo para cima: as linhas de MTTD e MTTR e o "Maior tempo de contenção".
Fala: "Primeiro o `marcos.yaml`. Ele fixa as regras do jogo: a detecção conta na abertura do caso no sistema de casos, e não no horário do alerta bruto; a contenção conta quando o host é isolado ou a conta é bloqueada. Sem isso, cada analista mediria de um jeito. No CSV, cada linha é um incidente do segundo trimestre com três horários. Agora o código. A função `horas` subtrai dois horários e divide os segundos por 3.600 para obter horas. No laço, a linha `ttd.append(horas(inc["inicio_atividade"], inc["deteccao"]))` mede o tempo até detectar, e a linha `ttr.append(horas(inc["deteccao"], inc["contencao"]))` mede o tempo até conter. As duas linhas que decidem o resultado são as que imprimem `mean` e `median`, lado a lado. Veja a saída: o MTTD tem média 4,0 h e mediana 4,0 h, porque não há caso extremo. No MTTR, nove incidentes foram contidos em 2 h, mas o INC-07 levou 2.160 h, ou 90 dias. A média vai a 217,8 h, que é (9 × 2 + 2160) ÷ 10, enquanto a mediana continua em 2 h."
Atenção: a linha do INC-07 aparece em vermelho no terminal porque é o caso extremo. Explique que a mediana é o valor do meio da lista ordenada e por isso ignora um único caso fora da curva. A digitação automática leva alguns segundos; espere terminar antes de clicar.
Conclusão: "Reporte média e mediana, e trate o INC-07 à parte, perguntando por que ele ficou esquecido. Esse é o primeiro número confiável para a diretoria."
[Tela: gravação do laboratório do slide 7]

**Slide 8 — Métricas de qualidade da detecção (7:00–7:50)**
Fala: "Velocidade não basta. A precisão dos alertas é verdadeiros positivos divididos pelo total de alertas e mostra quanto do trabalho do SOC é útil. A taxa de falsos positivos mede o ruído. A cobertura ATT&CK testada divide as técnicas com detecção validada pelas técnicas priorizadas, e a visibilidade mostra se há dados para detectar. Por fim, a taxa de reteste diz se as correções foram comprovadas. Quando a maior parte dos alertas é falsa, surge a fadiga de alertas: o analista fecha tudo rápido e acaba ignorando o alerta verdadeiro."

**Slide 9 — Cobertura ATT&CK e suas três armadilhas (7:50–8:40)**
Fala: "O ATT&CK Navigator gera mapas de calor muito comunicativos, desde que bem lidos. Há três armadilhas. A primeira é contar a técnica como coberta só porque existe uma regra. A segunda é tratar todas as técnicas como iguais, quando uma regra pode detectar apenas um dos procedimentos. A terceira é buscar 100% da matriz, quando o alvo são as técnicas priorizadas pela inteligência de ameaças, a CTI. O DeTT&CT ajuda ao pontuar separadamente a visibilidade e a detecção de cada técnica."

**Slide 10 — Laboratório: a *layer* toda verde (8:40–10:20)**
Objetivo: ver se a cobertura ATT&CK mede detecção de verdade ou só a existência de regras.
Na tela (passo a passo do que clicar, na ordem):
1. Mostrar a *layer* na visão inicial "Existe regra": as 20 técnicas priorizadas estão verdes e o indicador "Cobertura exibida" marca "20/20 = 100%"; "Hipóteses (nunca testadas)" mostra "?".
2. Clicar no botão "Cobertura testada", no alto à direita.
3. Ler os indicadores: "Cobertura exibida" passa a "10/20 = 50%" e "Hipóteses (nunca testadas)" passa a "10".
4. Clicar em T1021.001 (RDP), na coluna Mov. lateral, e ler o detalhe: visibilidade 4/4, detecção validada 4/5, 1 de 1 procedimento.
5. Clicar em T1078 (Contas válidas), na coluna Acesso inicial, e ler o detalhe "Nunca testada: a detecção é uma hipótese".
Fala: "Esta é a *layer* que o SOC gostaria de mostrar à diretoria: tudo verde. Só que verde aqui significa apenas que existe uma regra no SIEM. Quando troco para 'Cobertura testada', fica verde só o que passou por um ciclo *purple* e alertou de verdade. Metade some. No detalhe de cada técnica, a visibilidade vai de 0 a 4 e mede a qualidade das fontes de dados; a detecção vai de 0 a 5 e mede o quanto a regra pegou nos testes. Veja também a coluna de procedimentos: em T1087.002, a regra detectou 1 de 3 procedimentos, então mesmo uma técnica testada pode ter lacunas."
Atenção: a T1078 é justamente a técnica de entrada do Grupo Cobalto Austral, que vimos na Aula 13. Os níveis de visibilidade e detecção seguem a ideia do DeTT&CT, com valores fictícios.
Conclusão: "As 20 técnicas têm regra, mas só 10 foram testadas, e a cobertura real é 50%. Uma regra nunca testada continua sendo hipótese."
[Tela: gravação do laboratório do slide 10]

**Slide 11 — Modelos de maturidade (10:20–11:00)**
Fala: "Métricas operacionais mostram o desempenho; modelos de maturidade mostram se a organização consegue sustentá-lo. O NIST CSF 2.0 descreve quatro *tiers*: Parcial, Informado por riscos, Repetível e Adaptativo. Para o SOC, o SOC-CMM avalia pessoas, processos, tecnologia e serviços. O mais valioso nesses modelos é a conversa sobre onde a organização quer chegar."

**Slide 12 — Visualização 3D: a escada dos *tiers* do CSF 2.0 (11:00–12:10)**
Objetivo: mostrar à diretoria onde a Rede Tatame está e aonde quer chegar.
Na tela (passo a passo do que clicar, na ordem):
1. Com o botão "Hoje" ativo, apontar a esfera amarela sobre o degrau "2 · Informado por riscos" e a legenda: Pessoas 2,5; Processos 1,8; Tecnologia 3,4; Serviços 2,6.
2. Clicar em "Meta em 18 meses": a esfera sobe ao degrau "3 · Repetível" e as colunas crescem para 3,5; 3,2; 3,8 e 3,4.
3. Arrastar a cena para girar e mostrar as colunas de lado.
4. Clicar de novo em "Hoje" para comparar.
Fala: "A escada tem os quatro *tiers* do CSF 2.0, e a esfera amarela marca onde a Rede Tatame está hoje: no *tier* 2. A meta para 18 meses é o *tier* 3, o roxo. À direita, as quatro colunas são uma autoavaliação no estilo do SOC-CMM, o modelo de maturidade de SOC, numa escala de 1 a 5. A legenda destaca que Processos é a dimensão mais baixa, com 1,8. É ela que mais precisa crescer para chegar à meta."
Atenção: a autoavaliação é fictícia. As colunas e a esfera se movem com animação de cerca de um segundo; espere parar antes de comentar.
Conclusão: "A coluna mais baixa indica por onde começar o plano de 18 meses."
[Tela: gravação do laboratório do slide 12]

**Slide 13 — Do número à decisão (12:10–13:00)**
Fala: "Um bom painel tem poucos indicadores, e cada um tem dono, meta, fonte e periodicidade. No exemplo, o MTTD mediano é da coordenação do SOC, com meta de até 6 h; a precisão é da engenharia de detecção, com meta de pelo menos 25%; a cobertura testada é do líder *purple*, com meta de pelo menos 70%. Para a diretoria, uma frase como 'a cobertura das técnicas mais usadas contra o nosso setor subiu de 45% para 72% no semestre' comunica mais do que qualquer contagem de alertas. Cuidado com a Lei de Goodhart: se o SOC for cobrado só por MTTR, pode fechar incidentes cedo demais."

**Slide 14 — Exemplo numérico: antes e depois do *purple teaming* (13:00–13:40)**
Fala: "Em janeiro, o SOC recebia 1.200 alertas por mês, com 180 verdadeiros positivos, o que dá precisão de 15%. Depois de três ciclos *purple*, são 600 alertas e 150 verdadeiros positivos: precisão de 25%. O MTTD mediano caiu de 18 h para 4 h, cerca de 78% de redução, e o MTTR caiu de 9 h para 3 h, cerca de 67%. Fica uma pergunta: por que os verdadeiros positivos caíram? Vamos conferir no SIEM."

**Slide 15 — Laboratório: a conta na tela, regra por regra (13:40–15:40)**
Objetivo: provar com dados que três ciclos *purple* melhoraram a detecção.
Na tela (passo a passo do que clicar, na ordem):
1. No grupo "Janeiro", clicar em "1. Alertas por regra" e mostrar o total de 1.200 alertas e a linha "Login falho em massa" com 420 alertas e 5% de precisão.
2. No grupo "Após três ciclos", clicar em "2. Alertas por regra": total de 600, e "Login falho em massa" caiu para 90.
3. No grupo "Comparação", clicar em "3. Resumo antes e depois" e ler a linha "variação".
4. Clicar em "4. Duplicados de janeiro" e mostrar os quatro alertas do caso INC-2026-0117.
Fala: "A primeira busca, em SPL, filtra o índice `tatame_seguranca` no mês 2026-01, conta os alertas e soma os verdadeiros positivos por regra; o `eval` calcula a precisão de cada uma. A regra de login falho gera 35% dos alertas com 5% de precisão: ela é a primeira candidata a ajuste. A segunda busca é igual, mas no mês 2026-09. A mesma regra caiu de 420 para 90 alertas depois do ajuste de limiar e da lista de contas de serviço com exceção documentada, como a `svc-backup`. Somando a coluna, temos 1.200 em janeiro e 600 depois. O resumo mostra precisão de 15% para 25%, MTTD mediano de 18 h para 4 h e MTTR de 9 h para 3 h. Os verdadeiros positivos caíram 17%, e a quarta busca explica o motivo: em 14 de janeiro, um único incidente no notebook NB-FIN-044 gerou quatro alertas verdadeiros em três minutos. A nova correlação agrupa alertas do mesmo host e da mesma janela em um só."
Atenção: a queda dos verdadeiros positivos parece piora, mas vem da consolidação de duplicados. Faça a pausa antes da quarta busca para o aluno tentar explicar sozinho. O histograma acima da tabela mostra a distribuição dos alertas no período.
Conclusão: "Toda métrica precisa de contexto antes de ir à diretoria. Com as quatro buscas, Marina consegue mostrar a melhora e explicar a queda."
[Tela: gravação do laboratório do slide 15]

**Slide 16 — Laboratório: as métricas no painel do SOC da Plataforma Rede Tatame (15:40–17:50)**
Objetivo: ler MTTD, MTTR e falsos positivos no painel do SOC e ver quantas técnicas estão de fato comprovadas.
Na tela (passo a passo do que clicar, na ordem):
1. No seletor de velocidade, no alto, escolher "1 s = 1 min".
2. Abrir a aba Cenários e clicar em "Iniciar cenário" no cartão "Emulação do Grupo Cobalto Austral". O relógio começa a correr sozinho; não é preciso clicar em "Iniciar".
3. Abrir a aba SOC e esperar os alertas na tabela "Alertas".
4. No alerta R11 do `svc-backup` (descrição "conta de serviço com exceção documentada"), clicar em "Investigar", ler a nota de contexto e clicar em "Falso positivo". O indicador "Falsos positivos marcados" passa a 1.
5. No alerta R11 do login de `caio.mendes` na VPN, clicar em "Investigar" e depois em "Conter".
6. Ler os indicadores "MTTD médio" e "MTTR médio".
7. Abrir a aba Cobertura ATT&CK e ler os quadros "Comprovadas" e "Detectáveis sem teste".
Fala: "Agora a mesma lógica dentro da plataforma. O Grupo Cobalto Austral entra pela VPN com a senha vazada de `caio.mendes`, sem MFA, e a regra R11 dispara. Repare que chega também um R11 da conta `svc-backup`. Ao investigar, o painel mostra que é um comportamento conhecido e documentado; por isso marco como falso positivo, e isso entra na métrica de qualidade. No alerta de `caio.mendes`, a investigação mostra o tempo do primeiro sinal até o alerta, que é o MTTD daquele caso. Quando clico em 'Conter', a conta é bloqueada, os passos seguintes do cenário são interrompidos e o MTTR médio aparece. Por fim, a aba Cobertura ATT&CK: só 1 técnica está comprovada, contra 5 detectáveis sem teste."
Atenção: se o seletor ficar em "1 s = 15 s", os alertas demoram bem mais. Os tempos exatos variam conforme o momento do clique, por isso leia os valores da sua gravação. Se precisar repetir, use "Reiniciar" e comece de novo pela aba Cenários. O alerta do `svc-backup` só aparece com a regra R11 e a fonte de identidade ligadas, que é o estado inicial.
Conclusão: "A plataforma confirma o que vimos na *layer*: o painel mede velocidade e ruído, mas a 'cobertura com regra' ainda soma hipóteses. Uma regra só conta como cobertura depois de testada."
[Tela: gravação do laboratório do slide 16]

**Slide 17 — De volta ao problema (17:50–18:40)**
Fala: "Voltemos à pergunta de Marina. O relatório trocou os '2 milhões de ataques' por indicadores com meta, dono e consequência. O MTTD e o MTTR passaram a vir com média e mediana, e um caso esquecido não esconde mais o trimestre. A cobertura passou a ser a testada: das 20 técnicas com regra, só 10 foram testadas, então a cobertura real é 50%. E o antes e depois mostra precisão de 15% para 25% e MTTD mediano de 18 h para 4 h. Resposta à pergunta da aula: MTTD e MTTR com mediana, precisão dos alertas e cobertura ATT&CK testada, comparados ao longo do tempo e explicados com contexto."

**Slides 18 a 20 — Pontos-chave, referências e encerramento (18:40–19:30)**
Fala: "Para levar desta aula: métricas devem apoiar decisões; MTTD, MTTR e *dwell time* medem velocidade, e precisão e falsos positivos medem qualidade; a cobertura ATT&CK só tem valor quando é testada; e os *tiers* do NIST CSF 2.0 orientam a evolução. As referências estão no slide. Métricas mostram se o SOC melhora, mas e as pessoas e as decisões em uma crise? Na próxima aula, vamos treinar com simulações: *tabletop*, CTF e *cyber range*. Até lá!"
[Take de apoio: equipe reunida em sala de crise — Envato]

## Aula 15 — Exercícios de simulação: *tabletop*, CTF e *cyber range*

### Texto base

Pilotos de avião passam horas em simuladores treinando panes que, com sorte, nunca enfrentarão. Equipes de segurança precisam do mesmo: uma crise cibernética real não é o momento de descobrir quem tem autoridade para desligar um servidor ou quem fala com a imprensa. Exercícios de simulação permitem errar em um ambiente seguro — e aprender com isso.

#### Por que exercitar

O NIST SP 800-84 distingue três atividades complementares: **treinamento**, que ensina papéis e procedimentos; **teste**, que avalia se um componente funciona; e **exercício**, que simula um cenário para validar planos, políticas e capacidades. A publicação descreve dois formatos principais de exercício: o *tabletop*, baseado em discussão, e o exercício funcional, em que as pessoas executam suas funções em um ambiente simulado. Os exercícios completam o ciclo da resposta a incidentes estudado na Unidade 3: um plano que nunca foi exercitado é só um documento.

#### Exercício *tabletop*

No *tabletop*, os participantes se reúnem — em uma sala ou por videoconferência — e discutem como reagiriam a um cenário apresentado em etapas. Seus elementos são:

- **Cenário:** uma situação plausível, como um *ransomware* em uma sexta-feira à noite.
- ***Injects*:** informações novas inseridas ao longo do exercício ("a imprensa ligou", "o *backup* também foi criptografado") para forçar decisões.
- **Papéis:** facilitador, que conduz; participantes, de TI, jurídico, comunicação e diretoria; e avaliadores, que registram as decisões.
- **Relatório pós-ação** (*after-action report*): documento com pontos fortes, lacunas e um plano de melhoria com responsáveis e prazos.

A CISA, agência de cibersegurança dos Estados Unidos, disponibiliza gratuitamente os *CISA Tabletop Exercise Packages* (CTEP), com cenários prontos, perguntas de discussão e modelos de relatório, alinhados à metodologia HSEEP de exercícios.

[Imagem 1 — Mesa de reunião com executivos e técnicos discutindo diante de uma tela com a mensagem "Inject 3: dados de clientes publicados". Texto alternativo: "Equipe multidisciplinar reunida em um exercício tabletop de crise cibernética". Sugestão de busca no Envato: "crisis meeting boardroom".]

#### *Capture the flag* (CTF)

Os CTFs são competições em que participantes resolvem desafios técnicos para obter "bandeiras" (*flags*), sequências de texto que comprovam a solução. Há dois formatos principais:

- **Jeopardy:** desafios independentes, organizados por categoria (forense, criptografia, *web*, análise de registros) e pontuação. É o formato mais comum para iniciantes, como no picoCTF, da Carnegie Mellon University.
- **Ataque e defesa:** cada equipe recebe uma infraestrutura com serviços vulneráveis e precisa protegê-los enquanto tenta explorar os das outras equipes. Exige trabalho coordenado e é mais próximo da realidade operacional.

Para o Blue Team, há CTFs defensivos, focados em investigar registros, analisar tráfego e reconstruir a linha do tempo de um incidente.

[Imagem 2 — Placar de competição CTF com equipes, pontuações e categorias de desafios. Texto alternativo: "Placar de uma competição capture the flag com equipes e pontos". Sugestão de busca no Envato: "hackathon competition scoreboard".]

#### *Cyber range*

Um *cyber range* é um ambiente virtual controlado que reproduz uma rede realista — servidores, estações, tráfego de usuários e ferramentas de defesa — para treinamento e exercícios técnicos em escala. Ele permite executar ataques simulados sem risco ao ambiente de produção. O exemplo mais conhecido é o **Locked Shields**, exercício anual de defesa cibernética ao vivo organizado pelo Centro de Excelência em Defesa Cibernética Cooperativa da OTAN (CCDCOE), em que equipes azuis defendem sistemas de um país fictício. No Brasil, o Comando de Defesa Cibernética promove o **Exercício Guardião Cibernético**, que reúne órgãos públicos e setores de infraestrutura crítica.

| Critério | *Tabletop* | CTF | *Cyber range* |
|---|---|---|---|
| Foco | Decisões, papéis e comunicação | Habilidades técnicas individuais ou de equipe | Operação técnica integrada em ambiente realista |
| Público | Técnico e executivo | Técnico | Técnico (equipes Blue, Red e coordenação) |
| Custo e preparo | Baixo | Baixo a médio | Médio a alto |
| Entregável | Relatório pós-ação e plano de melhoria | Pontuação e aprendizado | Métricas de desempenho e lições aprendidas |

[Imagem 3 — Diagrama de um *cyber range*: rede simulada com servidores e estações, uma equipe azul defendendo e uma célula de controle observando. Texto alternativo: "Esquema de um cyber range com rede simulada, equipe de defesa e célula de controle".]

#### Avaliar para melhorar

Um exercício só gera valor se for **avaliado**. Antes de começar, definem-se objetivos mensuráveis ("acionar o plano de comunicação em até 1 hora") e critérios de avaliação. Ao final, faz-se um *hot wash* — uma conversa imediata, enquanto as impressões estão frescas — e, depois, o relatório formal. As ações de melhoria devem entrar no mesmo controle usado no *purple teaming*, com dono e prazo, e ser verificadas no exercício seguinte.

#### Exemplo numérico: pontuando um *tabletop*

Em um *tabletop* de *ransomware* com **8 *injects***, os avaliadores atribuíram de 0 a 3 pontos à resposta da equipe em cada um (0 = sem ação; 3 = ação correta, no tempo e pelo responsável certo). Pontuação máxima: 8 × 3 = 24. No primeiro exercício, a equipe obteve **14 pontos**: 14 ÷ 24 ≈ **58%**. Os piores resultados foram nos *injects* de comunicação com clientes e de notificação à ANPD. Após revisar o plano e treinar o jurídico, o exercício seguinte atingiu **20 pontos** (≈ **83%**).

#### Pausa para reflexão

> Uma cooperativa de crédito com 40 agências nunca realizou exercícios de simulação. A diretoria acredita que "o plano de resposta a incidentes está aprovado, então estamos preparados". O SOC é terceirizado e o *backup* nunca foi restaurado em um teste completo.
>
> 1. Qual tipo de exercício você recomendaria primeiro? Justifique considerando custo e público.
> 2. Proponha três *injects* que testem as fragilidades descritas.
> 3. Que métricas você incluiria no relatório pós-ação?
>
> **Desafio prático:** usando um dos cenários dos *CISA Tabletop Exercise Packages* como inspiração, monte um roteiro de *tabletop* de 60 minutos para essa cooperativa, com objetivos, papéis, cinco *injects* e critérios de pontuação.

#### Pontos-chave

- Exercícios validam planos, papéis e capacidades antes de uma crise real.
- O *tabletop* testa decisões e comunicação; o CTF desenvolve habilidades técnicas; o *cyber range* integra a operação em ambiente realista.
- Todo exercício precisa de objetivos mensuráveis e de um relatório pós-ação com plano de melhoria.

### Referências da aula

CYBERSECURITY AND INFRASTRUCTURE SECURITY AGENCY. *CISA tabletop exercise packages*. Disponível em: <https://www.cisa.gov/resources-tools/services/cisa-tabletop-exercise-packages>. Acesso em: 13 nov. 2026.

GRANCE, Tim *et al*. *SP 800-84: guide to test, training, and exercise programs for IT plans and capabilities*. Gaithersburg: NIST, 2006.

NATO COOPERATIVE CYBER DEFENCE CENTRE OF EXCELLENCE. *Locked Shields*. Disponível em: <https://ccdcoe.org/exercises/locked-shields/>. Acesso em: 13 nov. 2026.

PICOCTF. *picoCTF*. Pittsburgh: Carnegie Mellon University. Disponível em: <https://picoctf.org/>. Acesso em: 13 nov. 2026.

### Roteiro da Videoaula 15 — "Sexta-feira, 22h: o *ransomware* chegou. Quem decide?"

Duração-alvo: 15 a 20 minutos. Deck: unidade_4/slides/aula15.html (22 slides).

**Slides 1 a 3 — Capa, audiodescrição e sumário (0:00–0:40)**
Fala: "Olá! Esta é a videoaula 15, a penúltima da disciplina. Hoje vamos falar de exercícios de simulação: *tabletop*, CTF e *cyber range*. No sumário você vê o caminho: primeiro um problema da Rede Tatame, depois os três formatos, cada um com um laboratório, e no fim como avaliar um exercício para que ele gere melhoria de verdade."
[Câmera: professor em plano médio. Slide 2 fica na tela por 3 segundos, sem leitura em voz alta.]

**Slide 4 — O problema de hoje na Rede Tatame (0:40–2:10)**
Fala: "Imagine a cena. Sexta-feira, 22h. A Luiza Ferraz, analista do SOC, o centro de operações de segurança da Rede Tatame, está de plantão e lê na tela: 'SRV-ARQ-01 e SRV-ERP-01 criptografados. Pedido de resgate recebido.' A Rede Tatame tem um plano de resposta a incidentes, aquele que escrevemos na Unidade 3. Só que ninguém nunca o ensaiou. Quem a Luiza liga primeiro? Quem pode desligar a VPN? Quem fala com a imprensa? No mapa à direita você vê onde a aula acontece: o ataque entrou pela VPN, passou pelo AD e chegou aos servidores da sede; o SRV-ERP-01 está em vermelho. O que está em jogo são as fichas de 36 mil alunos, cerca de 30% menores de idade, e as academias paradas sem *check-in*. Pilotos treinam panes em simulador antes de voar. A pergunta da aula é: como a Rede Tatame pode treinar a resposta a um *ransomware* antes de enfrentar um de verdade? Guarde também os papéis: Luiza no plantão, Marina Prado como facilitadora, Bruno Sato na equipe vermelha e Caio Mendes na TI da sede."
[Take de apoio: cabine de simulador de voo; sala de servidores à noite — Envato.]

**Slide 5 — Por que exercitar (2:10–3:00)**
Fala: "O NIST, na publicação SP 800-84, separa três atividades. O treinamento ensina papéis e procedimentos. O teste avalia se um componente funciona, por exemplo, se o *backup* restaura. O exercício simula um cenário para validar planos, políticas e capacidades. A mesma publicação descreve dois formatos de exercício: o *tabletop*, baseado em discussão, e o exercício funcional, em que as pessoas executam suas funções em um ambiente simulado. Um plano que nunca foi exercitado continua sendo só um documento."

**Slide 6 — Exercício *tabletop* (3:00–3:50)**
Fala: "No *tabletop*, os participantes se reúnem, numa sala ou por videoconferência, e discutem como reagiriam a um cenário apresentado em etapas. Há quatro elementos. O cenário, como o *ransomware* de sexta à noite. Os *injects*, que são informações novas inseridas pela facilitação, como 'a imprensa ligou', para forçar decisões. Os papéis: facilitador, participantes de TI, jurídico, comunicação e diretoria, e avaliadores. E o relatório pós-ação, o *after-action report*, com pontos fortes, lacunas e um plano de melhoria com responsáveis e prazos. A CISA, agência de cibersegurança dos Estados Unidos, oferece de graça os *CISA Tabletop Exercise Packages*, com cenários prontos e modelos de relatório."

**Slide 7 — Laboratório: mini-*tabletop*, três *injects*, três decisões (3:50–6:00)**
Objetivo: responder à parte "quem decide e quem fala" da pergunta da aula, ensaiando as decisões das primeiras horas sem tocar em nenhum sistema.
Na tela (passo a passo):
1. Mostrar o console: relógio em 22:00, título "Tabletop · Rede Tatame · facilitadora Marina Prado" e o placar "0 / 9 pts" no canto.
2. Ler o *inject* 1 de 3 (22:00): "SRV-ARQ-01 e SRV-ERP-01 criptografados. Pedido de resgate recebido." Quem você liga primeiro? Pausar 3 segundos antes de clicar.
3. Clicar na alternativa A ("Aciono o plantão do SOC e o responsável pelo plano de resposta, que convoca o comitê de crise."). Ler a resposta comentada: 3 pontos.
4. Clicar em "Próximo inject". *Inject* 2 (22:20): "O backup em disco também foi criptografado." Clicar em A ("Verifico se existe cópia offline ou imutável e testo a restauração em ambiente isolado, preservando evidências."): 3 pontos.
5. Clicar em "Próximo inject". *Inject* 3 (22:40): "A imprensa ligou: há rumores de vazamento de fichas de alunos, inclusive menores." Para mostrar o contraste, clicar em C ("Respondo 'sem comentários' e desligo."): 1 ponto.
6. Ler a mensagem final: "Fim do mini-tabletop: 7 de 9 pontos (78%). No hot wash, discuta as escolhas com nota 0 ou 1."
Fala: "Cada *inject* tem três alternativas, e cada uma vale 3, 1 ou 0 pontos. Depois do clique, as cores mostram qual era a melhor e o texto explica o porquê. Repare no padrão: as respostas de 3 pontos começam por autoridade e comunicação. No primeiro *inject*, a primeira ligação vai para quem pode convocar o comitê de crise, e não para o fornecedor do antivírus. No segundo, restaurar com pressa sobre máquinas comprometidas pode reinfectar o ambiente e apagar evidências. No terceiro, escolhi de propósito o 'sem comentários': evita o pior, mas o silêncio alimenta especulação, e o plano deveria prever uma mensagem de espera aprovada. É essa escolha de 1 ponto que vai para a conversa de *hot wash*."
Atenção: pause o vídeo antes de cada clique e convide o aluno a decidir sozinho. Depois de escolher, as alternativas ficam travadas; para refazer, use "Reiniciar". Pagar o resgate aparece como alternativa de 0 pontos porque é decisão da diretoria com apoio jurídico, e não uma resposta técnica ao *inject*.
Conclusão: "O *tabletop* mostra as lacunas do plano, como quem fala com a imprensa, sem tocar em nenhum sistema."
[Tela: gravação do laboratório do slide 7.]

**Slide 8 — *Capture the flag* (6:00–6:40)**
Fala: "O segundo formato é o CTF, *capture the flag*. Os participantes resolvem desafios técnicos para obter *flags*, sequências de texto que comprovam a solução. No formato *jeopardy*, os desafios são independentes e organizados por categoria e pontuação; é o mais comum para iniciantes, como no picoCTF, da Carnegie Mellon. No formato ataque e defesa, cada equipe protege a própria infraestrutura. Para o Blue Team existem CTFs defensivos, focados em investigar registros e reconstruir a linha do tempo de um incidente."

**Slide 9 — Laboratório: CTF defensivo de análise de registros (6:40–8:40)**
Objetivo: responder à parte técnica da pergunta. Antes da crise, o analista precisa ter treinado o olho para achar um padrão em registros de autenticação.
Na tela (passo a passo):
1. Mostrar o quadro "CTF da turma · formato jeopardy · ambiente de treino": quatro categorias (Forense, Criptografia, Web, Registros), valores 100, 200 e 300, e o placar à direita, com a "Turma UniFECAF (você)" em 3º lugar, com 500 pontos.
2. Clicar em "Forense 200" para mostrar que os outros desafios aparecem só com a descrição ("Desafio fechado nesta demonstração"). Voltar para "Registros 100", que já abre selecionado.
3. Ler a pergunta: "Qual endereço fez cinco falhas seguidas na mesma conta e depois conseguiu entrar?" Percorrer o `auth.log` do `svc-gestao-01` linha a linha.
4. Clicar em "Dica" e ler: ignorar a conta "carla" e o endereço que tenta "root" sem sucesso; contar as falhas por endereço e por conta.
5. Digitar um valor errado, por exemplo `flag{10.10.9.7}`, clicar em "Enviar" e mostrar a mensagem vermelha "Hash não confere".
6. Corrigir para `flag{10.10.8.23}`, clicar em "Enviar" e mostrar a mensagem verde "Flag correta. SHA-256 confere". O placar da turma sobe de 500 para 600 pontos, ainda em 3º lugar, atrás da Equipe Farol, com 700.
Fala: "Cada linha do registro tem data, servidor, o serviço `sshd`, o resultado (*Failed* ou *Accepted*), a conta e o endereço de origem. A Carla errou a senha uma vez e entrou; é um usuário comum. O 10.10.9.7 tenta 'root' três vezes e nunca entra; é ruído que merece atenção, mas não responde à pergunta. O 10.10.8.23 erra cinco vezes na conta 'suporte', às 09:01:12, 15, 20, 24 e 28, e às 09:01:31 entra. Esse é o padrão de senha adivinhada que terminou em sucesso. Agora repare como o placar confere a resposta: o código calcula o *hash* SHA-256 do que você digitou e compara com um *hash* guardado. A resposta certa nunca aparece em texto no arquivo, então não adianta abrir o código-fonte para colar a *flag*."
Atenção: o registro é fictício e uma cópia de treino; ninguém ataca nada. O campo aceita maiúsculas e espaços, porque o código converte para minúsculas e remove espaços antes de calcular o *hash*. A mensagem verde lembra o passo seguinte na vida real: abrir um caso, porque a conta "suporte" foi acessada depois de tentativas seguidas de senha.
Conclusão: "O CTF treina, em pequenas doses, a habilidade que a Luiza vai precisar na sexta-feira às 22h."
[Tela: gravação do laboratório do slide 9.]

**Slide 10 — *Cyber range*: a operação em escala (8:40–9:20)**
Fala: "O terceiro formato é o *cyber range*, um ambiente virtual controlado que reproduz uma rede realista, com servidores, estações, tráfego de usuários e ferramentas de defesa. Ele permite simular ataques sem risco à produção. Dois exemplos: o Locked Shields, exercício anual da OTAN organizado pelo CCDCOE, e o Exercício Guardião Cibernético, promovido no Brasil pelo Comando de Defesa Cibernética. A lógica é sempre a mesma: equipes azuis defendem, uma equipe vermelha gera a pressão prevista no roteiro e uma célula de controle conduz, observa e pontua."
[Take de apoio: centro de operações com várias telas; equipe em exercício — Envato.]

**Slide 11 — Visualização 3D: por dentro de um *cyber range* (9:20–10:30)**
Objetivo: entender quem faz o quê em um *cyber range*, antes de usar a plataforma como um deles no próximo slide.
Na tela (passo a passo):
1. Mostrar a cena inteira: a rede simulada no centro, a equipe azul à esquerda, a equipe vermelha à direita e a célula de controle, o bloco amarelo, no alto. Apontar a legenda: verde é tráfego de usuários, vermelho são eventos do roteiro e azul são ações de defesa.
2. Clicar em "Rede" e ler a nota: réplica da sede e da nuvem da Rede Tatame, com tráfego gerado por robôs; nada toca a produção nem dados reais de alunos.
3. Clicar em "Equipe azul" (quem está sendo treinada e avaliada), depois em "Equipe vermelha" (gera os eventos do roteiro, dentro do ambiente isolado) e em "Controle" (conduz, injeta eventos, observa e pontua).
4. Clicar de novo no botão ativo para voltar à visão completa. Arrastar para girar a cena e mostrar as linhas tracejadas que ligam a célula de controle às duas equipes e à rede.
Fala: "Cada botão destaca um papel e deixa os outros transparentes. Repare nas partículas: as verdes circulam o tempo todo, porque um *cyber range* precisa de tráfego normal para que o ataque não fique óbvio. As vermelhas saem da equipe vermelha e as azuis saem da equipe azul. As linhas tracejadas mostram que a célula de controle enxerga todos."
Atenção: a cena é ilustrativa e as partículas não representam volumes reais. Se a cena girar demais, use a rolagem do mouse para aproximar ou afastar.
Conclusão: "A célula de controle conduz e pontua; nada do que acontece ali toca a produção."
[Tela: gravação do laboratório do slide 11.]

**Slide 12 — Laboratório: plataforma Rede Tatame, o exercício completo em duas rodadas (10:30–13:00)**
Objetivo: responder à parte "agir" da pergunta, usando a plataforma da disciplina como *cyber range* e medindo o efeito de conter cedo ou tarde.
Na tela (passo a passo):
1. A plataforma abre na aba **Cenários**. Manter a velocidade em "1 s = 15 s". Clicar em "Iniciar cenário" no cartão *Emulação do Grupo Cobalto Austral* e mostrar os oito passos da cadeia, do login na VPN ao impacto.
2. Rodada 1: abrir a aba **SOC**. Quando chegar o alerta R11 "Login sem MFA" de `caio.mendes`, clicar em "Investigar" e depois em "Conter". Ignorar o outro R11, do `svc-backup`.
3. Voltar a **Cenários** e mostrar que os passos seguintes ficam "interrompido pela contenção": o adversário parou em um ou dois passos.
4. Rodada 2: clicar em **Reiniciar**, iniciar o mesmo cenário de novo e, desta vez, não conter o R11. Esperar o alerta R6, "Acesso à memória do LSASS", em SRV-ARQ-01 (cerca de 30 segundos nessa velocidade).
5. No R6, clicar em "Investigar" e depois em "Conter". Voltar a **Cenários**: o adversário já passou por quatro passos ou mais, e alguns aparecem como "visto nos logs, sem alerta" ou "não detectado".
Fala: "Na tabela do SOC, cada linha é um alerta: identificador, hora simulada, severidade, regra, *host*, descrição e estado. A regra R11 dispara quando há login sem MFA em conta privilegiada ou de VPN. Ela dispara duas vezes. Uma é a conta `svc-backup`, que tem exceção documentada, e a outra é `caio.mendes`, cuja senha vazou. Contendo cedo, o Cobalto Austral fica preso na VPN. Na segunda rodada deixamos o ataque andar: consulta ao AD, RDP para o SRV-ARQ-01 e leitura da memória do LSASS para roubar outras credenciais. Só o quarto passo gerou um alerta forte, o R6. Os passos que passaram sem alerta são exatamente o que entra no relatório pós-ação como lacunas."
Atenção: os passos sem alerta dependem das regras ligadas; com a configuração inicial, as regras R13 e R5 estão desligadas, como vimos na Aula 13. Se a simulação correr rápido demais para explicar, troque para "1 s = 5 s". Se o relógio ficar parado em 09:00:00, clique em "Iniciar" na barra superior. Sempre clique em Reiniciar entre as rodadas, para o relógio e os alertas voltarem a zero.
Conclusão: "Conter cedo parou o adversário em um ou dois passos; conter tarde deixou avançar quatro. Os passos sem alerta viram lacunas no relatório pós-ação."
[Tela: gravação do laboratório do slide 12, com as duas rodadas.]

**Slide 13 — Comparação dos três formatos (13:00–13:40)**
Fala: "Vamos comparar. O *tabletop* foca em decisões, papéis e comunicação, serve a público técnico e executivo, tem custo baixo e entrega um relatório pós-ação com plano de melhoria. O CTF foca em habilidades técnicas, para público técnico, tem custo baixo a médio e entrega pontuação e aprendizado. O *cyber range* integra a operação técnica em ambiente realista, envolve equipes Blue, Red e coordenação, tem custo médio a alto e entrega métricas de desempenho e lições aprendidas. Os três se completam."

**Slide 14 — Avaliar para melhorar (13:40–14:20)**
Fala: "Um exercício só gera valor se for avaliado. Antes, definimos objetivos mensuráveis, como acionar o plano de comunicação em até 1 hora. Logo ao final, fazemos o *hot wash*, uma conversa imediata com as impressões frescas. Depois vem o relatório formal. E no exercício seguinte as ações de melhoria entram no mesmo controle usado no *purple teaming*, com dono e prazo, e são verificadas."

**Slide 15 — Laboratório: do objetivo ao exercício seguinte (14:20–15:30)**
Objetivo: ver como a avaliação vira melhoria (o objetivo aparece no alto do slide, porque o fluxo ocupa a tela inteira).
Na tela (passo a passo):
1. Clicar em "Avançar" a cada etapa, sem o modo automático, para comentar com calma.
2. Etapas 1 a 3: Objetivos (comitê em 15 minutos, comunicação em 1 hora, decisão sobre a ANPD), Condução (8 *injects*, ninguém executa nada nos sistemas) e Avaliadores (notas de 0 a 3; primeiro exercício com 14 de 24 pontos).
3. Etapas 4 e 5: *Hot wash* (ninguém sabia quem falava com alunos e academias, nem quem decidia sobre a ANPD) e Relatório pós-ação, que fica destacado em vermelho: 58%, com comunicação com nota 0 e ANPD com nota 1.
4. Etapas 6 e 7: Plano de melhoria no controle de ações (comunicação com prazo de 30 dias; DPO com prazo de 45 dias) e Próximo exercício: 20 de 24 pontos, 83%, com as duas ações verificadas.
Fala: "Cada nó acende quando chega a vez dele, e a legenda abaixo explica a etapa. Repare na seta tracejada que volta do próximo exercício para os objetivos: o ciclo recomeça. É o mesmo raciocínio do reteste do *purple teaming*, só que aplicado a pessoas e decisões."
Atenção: o botão de voltar retorna uma etapa; o modo "Auto" avança sozinho e pode ser rápido demais para a narração.
Conclusão: "A avaliação só fecha o ciclo quando o exercício seguinte verifica as ações."
[Tela: gravação do laboratório do slide 15.]

**Slide 16 — Exemplo numérico: pontuando um *tabletop* (15:30–16:10)**
Fala: "Agora as contas. São 8 *injects* com nota de 0 a 3, então a pontuação máxima é 8 vezes 3, igual a 24. No primeiro exercício a equipe fez 14 pontos: 14 dividido por 24 dá 58%. Os piores resultados foram em comunicação com clientes e notificação à ANPD, a Autoridade Nacional de Proteção de Dados. Depois de revisar o plano e treinar o jurídico, a equipe chegou a 20 pontos: 20 dividido por 24 dá 83%."

**Slide 17 — Laboratório: cronograma de *injects* e pontuação (16:10–18:00)**
Objetivo: mostrar como a facilitação pontua o *tabletop* e transforma as notas baixas em plano de melhoria.
Na tela (passo a passo):
1. Com `injects.yaml` aberto, ler as linhas 3 a 6 (os três objetivos) e as linhas 7 a 15 (os 8 *injects*, cada um com tempo `t`, identificador, responsável e texto).
2. Abrir `avaliacao.csv` e mostrar as colunas `exercicio_1` e `exercicio_2`, destacando I6 (0 e 2) e I7 (1 e 2).
3. Abrir `pontuar.py` e explicar o código.
4. No terminal, clicar em "Pontuar o 1º exercício" (`python pontuar.py exercicio_1`).
5. Clicar em "Pontuar o exercício seguinte" (`python pontuar.py exercicio_2`).
Fala: "O YAML é o cronograma da facilitadora: no minuto 0, o I1 para o SOC; no minuto 50, o I6 para a Comunicação, com alunos reclamando nas redes; no minuto 60, o I7 para o DPO e o Jurídico, com indícios de cópia de fichas de menores. O CSV guarda as notas dos avaliadores. No `pontuar.py`, a linha com `sys.argv` escolhe qual coluna pontuar, e `MAX_POR_INJECT` vale 3. O laço imprime uma barra para cada *inject*: um cerquilha por ponto e um ponto final para cada ponto que faltou. O máximo é 3 vezes o número de *injects*, ou seja, 24. A linha que decide as lacunas é a lista `fracos`: ela pega todo *inject* com nota menor ou igual a 1. Na primeira execução, a saída mostra 'Pontuação: 14/24 = 58%' e duas lacunas: I6, da Comunicação, e I7, do DPO e Jurídico. Na segunda, 'Pontuação: 20/24 = 83%' e a mensagem 'Nenhum inject com nota 0 ou 1'."
Atenção: o código lê arquivos de exemplo e só faz contas; não há nenhum sistema real envolvido. Se quiser digitar os comandos, use "Digitar ao vivo" no terminal.
Conclusão: "Nota baixa vira ação com dono, prazo e verificação no exercício seguinte."
[Tela: gravação do laboratório do slide 17.]

**Slide 18 — Pausa para reflexão: a cooperativa que nunca exercitou (18:00–18:40)**
Fala: "Agora é com você. Uma cooperativa de crédito com 40 agências nunca fez exercícios de simulação. A diretoria acha que, como o plano está aprovado, todos estão preparados. O SOC é terceirizado e o *backup* nunca foi restaurado em um teste completo. Qual exercício você recomendaria primeiro, considerando custo e público? Que três *injects* testariam essas fragilidades? Que métricas entrariam no relatório pós-ação? O desafio prático é montar um *tabletop* de 60 minutos para essa cooperativa, inspirado nos pacotes da CISA, com objetivos, papéis, cinco *injects* e critérios de pontuação."
[Câmera: professor em plano fechado; slide em tela cheia por 10 segundos para leitura.]

**Slide 19 — De volta ao problema: agora o plano já foi ensaiado (18:40–19:25)**
Fala: "Voltemos à Luiza, sexta-feira, 22h. Como a Rede Tatame treina a resposta antes do ataque real? No *tabletop*, os *injects* mostraram quem aciona o comitê, quem fala com a imprensa e o que se preserva. No CTF, o analista praticou achar nos registros o endereço que forçou a senha e entrou. No *cyber range* da plataforma, conter cedo parou o adversário em um ou dois passos, e conter tarde deixou avançar quatro. E a avaliação levou a pontuação de 58% para 83%. Então a resposta é: com exercícios em ambiente seguro, com objetivos medidos e um relatório pós-ação cujas ações são verificadas no exercício seguinte."

**Slides 20 a 22 — Pontos-chave, referências e encerramento (19:25–20:00)**
Fala: "Para levar desta aula: exercícios validam planos, papéis e capacidades antes de uma crise real; o *tabletop* testa decisões, o CTF desenvolve habilidades técnicas e o *cyber range* integra a operação; e todo exercício precisa de objetivos mensuráveis e de um plano de melhoria. As referências estão no slide. Resolva a pausa para reflexão. Na próxima e última aula, vamos juntar tudo em um programa contínuo de segurança e falar da sua carreira. Até lá!"
[Slide 21 na tela por 3 segundos, sem leitura. Encerrar no slide 22 com a vinheta.]

## Aula 16 — Programa contínuo de segurança, carreira e tendências

### Texto base

Ao longo da disciplina, você viu operações de Red Team, detecções, investigações, ciclos *purple* e exercícios. Cada uma dessas atividades, isolada, gera um ganho pontual. O desafio de uma organização madura é transformá-las em um **programa contínuo**, com governança, orçamento e evolução mensurável.

#### Governança: segurança como decisão de negócio

A função Governar (*Govern*), incluída no NIST CSF 2.0, lembra que a segurança começa na estratégia: definir o apetite a riscos, os papéis e responsabilidades, as políticas e a supervisão pela alta administração. Na prática, um programa contínuo de testes e melhoria precisa de:

- **Patrocínio executivo**, com um responsável (como o CISO) que presta contas à diretoria ou ao conselho;
- **Calendário anual** de atividades: varreduras periódicas, *pentests* em sistemas novos, ciclos *purple* frequentes, uma operação de Red Team e exercícios *tabletop*;
- **Gestão de achados** com dono, prazo e reteste, integrada à gestão de riscos;
- **Relatórios periódicos** à liderança, em linguagem de risco e de negócio.

[Imagem 1 — Linha do tempo de 12 meses com marcos trimestrais: ciclos *purple* mensais, *tabletop* semestral, Red Team anual e varreduras contínuas. Texto alternativo: "Calendário anual de um programa contínuo de testes de segurança".]

#### O roteiro (*roadmap*) e o orçamento

Um *roadmap* de segurança conecta o estado atual (medido com as métricas e os modelos de maturidade da Aula 14) ao estado desejado, em etapas priorizadas por risco. Para justificar investimentos, é comum usar a **expectativa de perda anual** (*annualized loss expectancy*, ALE), que você conheceu na Unidade 1, e o retorno sobre o investimento em segurança (*return on security investment*, ROSI):

ROSI = (redução da perda esperada − custo da medida) ÷ custo da medida

Esses cálculos dependem de estimativas e devem ser apresentados com suas premissas, em faixas, e não como certezas.

#### Tendências que moldam o programa

**Zero Trust.** O modelo descrito no NIST SP 800-207 elimina a confiança implícita na localização de rede: cada acesso é verificado com base em identidade, dispositivo e contexto. Para o *purple teaming*, isso significa testar sobretudo o abuso de identidades e credenciais válidas.

**Nuvem.** Com serviços em nuvem, parte da superfície de ataque passa a ser formada por configurações, identidades e APIs. A matriz ATT&CK tem uma seção específica para nuvem, e os planos de emulação precisam incluí-la.

**Inteligência artificial nos dois lados.** Relatórios como o *ENISA Threat Landscape* registram o uso de IA generativa para tornar a engenharia social mais convincente e em maior escala. Na defesa, a IA apoia a triagem de alertas, o resumo de investigações e a análise de grandes volumes de dados. Os ganhos são reais, mas as ferramentas erram e exigem supervisão humana. Os próprios sistemas de IA também se tornaram alvos — a MITRE mantém o ATLAS, uma base de táticas e técnicas contra sistemas de IA, nos moldes do ATT&CK.

[Imagem 2 — Ilustração de uma rede neural estilizada dividida ao meio, com um lado vermelho (ataque) e outro azul (defesa). Texto alternativo: "Representação da inteligência artificial sendo usada tanto no ataque quanto na defesa". Sugestão de busca no Envato: "artificial intelligence cyber security concept".]

#### Carreira: os caminhos de Red, Blue e Purple

O NIST NICE Framework (SP 800-181 Rev. 1) organiza a força de trabalho em cibersegurança em funções de trabalho (*work roles*), com tarefas, conhecimentos e habilidades associados — uma referência útil para planejar a carreira.

| Função | O que faz | Certificações conhecidas |
|---|---|---|
| Analista de SOC | Triagem e investigação de alertas | CompTIA Security+, CompTIA CySA+ |
| *Pentester* | Testes de invasão em escopo definido | CompTIA PenTest+, OSCP (OffSec) |
| Operador de Red Team | Emulação de adversários orientada a objetivos | OSCP e certificações avançadas de Red Team |
| Engenheiro de detecção | Cria, testa e mantém regras de detecção | GIAC (por exemplo, GCIA), CySA+ |
| Resposta a incidentes | Contenção, investigação e recuperação | GIAC GCIH |
| *Threat hunter* / CTI | Caça proativa e inteligência de ameaças | GIAC (por exemplo, GCTI) |

Certificações ajudam a comprovar conhecimento, mas a prática pesa tanto quanto elas: laboratórios, CTFs, relatórios bem escritos e contribuições a projetos abertos demonstram competência real.

[Imagem 3 — Mapa de trilhas de carreira em formato de metrô, com linhas vermelha, azul e roxa e estações para cada função. Texto alternativo: "Mapa de carreira em cibersegurança com trilhas ofensiva, defensiva e purple".]

#### Exemplo numérico: justificando o programa

Uma empresa estima a perda de um incidente grave em **R$ 8 milhões**, com probabilidade anual de **12%**: ALE = 0,12 × 8.000.000 = **R$ 960.000**. O programa contínuo proposto custa **R$ 300.000 por ano** e, segundo as premissas da equipe, reduziria a probabilidade para **5%**: nova ALE = 0,05 × 8.000.000 = R$ 400.000. A redução é de R$ 560.000, e o ROSI = (560.000 − 300.000) ÷ 300.000 ≈ **87%**. Em um cenário conservador, com probabilidade final de 8%, a redução seria de R$ 320.000 e o ROSI cairia para cerca de 7% — ainda positivo, mas mostra como as premissas importam.

#### O que você verá na próxima unidade

Esta é a última unidade, então é hora de olhar para o caminho percorrido. Na Unidade 1, você construiu a base: os papéis de Red, Blue e Purple, a ética e a legalidade, a Kill Chain, o ATT&CK e os fundamentos da defesa. Na Unidade 2, acompanhou uma operação ofensiva controlada, sempre perguntando que rastro cada ação deixa. Na Unidade 3, viu como a defesa coleta telemetria, detecta, caça ameaças e responde a incidentes. E nesta unidade, uniu tudo em ciclos de melhoria mensuráveis. O próximo passo é seu: pratique em laboratórios e CTFs, explore a matriz ATT&CK, escolha uma trilha de carreira e uma certificação inicial — e nunca esqueça que, nesta área, autorização e ética vêm antes de qualquer técnica.

#### Pontos-chave

- Um programa contínuo integra testes, exercícios e melhorias sob governança e orçamento.
- ALE e ROSI ajudam a justificar investimentos, desde que as premissas sejam explicitadas.
- Zero Trust, nuvem e IA mudam o que precisa ser testado e defendido.
- O NICE Framework e as certificações orientam a carreira; a prática a consolida.

### Referências da aula

EUROPEAN UNION AGENCY FOR CYBERSECURITY. *ENISA threat landscape 2024*. Atenas: ENISA, 2024.

MITRE. *ATLAS: adversarial threat landscape for artificial-intelligence systems*. Disponível em: <https://atlas.mitre.org/>. Acesso em: 13 nov. 2026.

NATIONAL INSTITUTE OF STANDARDS AND TECHNOLOGY. *The NIST cybersecurity framework (CSF) 2.0*. Gaithersburg: NIST, 2024. DOI: 10.6028/NIST.CSWP.29.

PETERSEN, Rodney *et al*. *SP 800-181 Rev. 1: workforce framework for cybersecurity (NICE framework)*. Gaithersburg: NIST, 2020. DOI: 10.6028/NIST.SP.800-181r1.

ROSE, Scott *et al*. *SP 800-207: zero trust architecture*. Gaithersburg: NIST, 2020. DOI: 10.6028/NIST.SP.800-207.

### Roteiro da Videoaula 16 — "Dez minutos com o conselho: do primeiro alerta ao programa contínuo"

Duração-alvo: 15 a 20 minutos. Deck: unidade_4/slides/aula16.html (21 slides).

**Slides 1 a 3 — Capa, audiodescrição e sumário (0:00–0:40)**
Fala: "Olá! Esta é a Videoaula 16, a última da disciplina. Hoje vamos juntar tudo o que construímos em um programa contínuo de segurança, falar das tendências que mudam o que testamos e olhar para a sua carreira. No sumário você vê o caminho: um problema, três ideias de gestão, seis laboratórios e o fechamento das quatro unidades."
[Slide 2: a audiodescrição fica na tela por alguns segundos, sem leitura em voz alta.]

**Slide 4 — O problema de hoje na Rede Tatame (0:40–2:00)**
Fala: "Marina Prado, a CISO, ou seja, a diretora de segurança da informação da Rede Tatame, tem dez minutos na reunião do conselho para pedir o orçamento de 2027. Lembra da Aula 1? Lá ela não sabia responder à pergunta 'estamos seguros?'. Desde então a Rede Tatame passou por uma operação de Red Team, ganhou regras novas, rodou ciclos *purple* e fez exercícios. Cada atividade gerou um ganho, mas isolado. Agora estão em jogo R$ 300 mil por ano e a proteção de 36 mil alunos, cerca de 30% menores de idade. A pergunta da aula é esta, no quadro amarelo: como transformar testes e exercícios em um programa contínuo que o conselho entenda e aprove? À direita, o mini-mapa mostra que hoje a aula acontece na plataforma inteira: nuvem, sede e catracas, tudo convergindo para o SOC, em vermelho."
[Take de apoio: executiva apresentando números em sala de reunião — Envato, "boardroom presentation"]

**Slide 5 — Governança: segurança como decisão de negócio (2:00–3:00)**
Fala: "O primeiro passo vem do NIST CSF 2.0, que incluiu a função Governar. Segurança começa na estratégia: quanto risco a empresa aceita, quem responde por quê e quem supervisiona. Para um programa contínuo, quatro peças são indispensáveis. Patrocínio executivo, com alguém como a CISO prestando contas ao conselho. Um calendário anual de testes e exercícios. Uma gestão de achados com dono, prazo e reteste. E relatórios periódicos em linguagem de risco e de negócio. Os próximos laboratórios montam cada uma dessas peças."

**Slide 6 — Laboratório: o calendário anual de 2027 (3:00–4:40)**
Objetivo: mostrar a primeira peça da resposta, um calendário em que cada atividade de teste tem ritmo fixo.
Na tela:
1. Abrir o slide; o calendário já vem com **set** destacado e, embaixo, o quadro "SET/2027 · 4 atividades".
2. Ler as seis linhas da esquerda: Varreduras (contínuo), Pentests (sob demanda), Ciclos purple (mensal), Tabletop (semestral), Red Team (anual) e Relatório (trimestral).
3. Clicar no mês **mar**: aparecem varreduras, o *pentest* da nova versão do portal gestao.tatame.com.br, o ciclo *purple* e o relatório à liderança.
4. Clicar na célula amarela de **mai**: o *tabletop* de *ransomware* com a diretoria.
5. Voltar a **set** e ler as quatro atividades.
Fala: "Cada linha é um tipo de atividade, e a cor mostra em que meses ela acontece. As varreduras e os ciclos *purple* aparecem em todos os meses porque são contínuos e mensais. Os *pentests* acontecem quando entra um sistema novo: em março o portal de gestão, em julho a API de check-in das catracas, em outubro a nova versão do app do aluno. Os *tabletops* são semestrais, em maio e novembro. Repare em setembro: ali estão a operação anual de Red Team e o relatório trimestral. Isso foi planejado, para que os achados do Red Team cheguem ao conselho no mesmo mês. A última linha do quadro vale para todos os meses: todos os achados entram na mesma gestão, com dono, prazo e reteste, e alimentam o *roadmap*."
Atenção: as datas são fictícias e servem de modelo; cada organização ajusta o ritmo ao seu risco e ao seu orçamento.
Conclusão: "Com o calendário, o conselho vê que testar faz parte da rotina da Rede Tatame, todos os meses."
[Tela: gravação do laboratório do slide 6]

**Slide 7 — O roadmap e o orçamento (4:40–5:30)**
Fala: "O *roadmap* liga o estado atual, medido com as métricas e a maturidade da Aula 14, ao estado desejado, em etapas ordenadas por risco. Para pedir dinheiro, usamos duas contas. A ALE, expectativa de perda anual, que você viu na Unidade 1. E o ROSI, o retorno sobre o investimento em segurança: a redução da perda esperada, menos o custo da medida, dividido pelo custo da medida. As duas dependem de estimativas, então sempre as apresentamos com premissas e em faixas."

**Slide 8 — Laboratório: como os achados alimentam o roadmap (5:30–7:10)**
Objetivo: ver o ciclo que transforma atividades soltas em um programa contínuo.
Na tela:
1. Clicar em **Avançar** uma vez por etapa, esperando a animação do pacote entre os nós (cerca de 2 segundos).
2. Etapa 1, "Medir o estado atual": ler o texto embaixo do diagrama.
3. Seguir até a etapa 7, "O ciclo recomeça", quando todos os nós acendem.
4. Opcional: clicar em **Auto** para mostrar o ciclo inteiro sem pausa.
Fala: "O diagrama tem sete nós. No centro está a Governança, a CISO e o conselho. Na etapa 1 medimos: cobertura testada de 45%, MTTD mediano de 18 horas e *tier* 2 do CSF. Na etapa 2 priorizamos as lacunas pela ALE de cada cenário. Na 3 montamos o *roadmap* em etapas trimestrais, cada uma com orçamento e meta. Na 4 o calendário que acabamos de ver é executado. Na 5 cada achado vira uma ação com dono e prazo, e só fecha depois do reteste. Na 6 relatamos à liderança em linguagem de negócio, por exemplo: a cobertura das técnicas mais usadas contra o nosso setor subiu de 45% para 72% no semestre. Na 7 a liderança decide apetite a risco e orçamento, e a nova medição alimenta o *roadmap* de novo. As linhas tracejadas mostram onde a Governança atua: ela recebe o relato e aprova o *roadmap*."
Atenção: os números deste diagrama são ilustrativos e diferem da cobertura de 38% da plataforma, que veremos no slide 11; explique que são medições de exemplos distintos.
Conclusão: "O programa é contínuo porque a saída de uma volta vira a entrada da próxima."
[Tela: gravação do laboratório do slide 8]

**Slide 9 — Exemplo numérico: justificando o programa (7:10–8:10)**
Fala: "Vamos à conta. Um incidente grave custaria R$ 8 milhões, com probabilidade anual de 12%. A ALE é 0,12 vezes 8 milhões, ou seja, R$ 960 mil. O programa custa R$ 300 mil por ano. Se a equipe estima que a probabilidade cai para 5%, a nova ALE é R$ 400 mil, a redução é R$ 560 mil e o ROSI fica em torno de 87%. No cenário conservador, com 8%, a nova ALE é R$ 640 mil, a redução é R$ 320 mil e o ROSI cai para cerca de 7%. Os dois são positivos, mas a distância entre 87% e 7% mostra o peso das premissas. Por isso elas vão para a mesa junto com o resultado."

**Slide 10 — Laboratório: o caso de negócio em Python (8:10–10:40)**
Objetivo: traduzir o programa em reais, com as premissas visíveis para o conselho.
Na tela:
1. Com `premissas.yaml` aberto, mostrar as linhas destacadas: `impacto_incidente_grave: 8000000`, `probabilidade_atual: 0.12`, `custo_programa_anual: 300000` e os dois cenários, `otimista` com 0.05 e `conservador` com 0.08.
2. Abrir `rosi.py` no explorador e mostrar as linhas destacadas do laço `for`.
3. Clicar em **Calcular ALE e ROSI** e esperar a saída no terminal.
4. Abrir `roadmap.csv` e depois `priorizar.py`.
5. Clicar em **Priorizar o roadmap** e ler a saída até a linha final.
Fala: "O primeiro arquivo guarda só as premissas, e o comentário diz de onde vieram: um *workshop* de risco com Finanças e Operações. Isso deixa claro que são estimativas. O `rosi.py` lê esse arquivo e calcula a ALE atual: 12% de R$ 8 milhões, R$ 960 mil. Depois, para cada cenário, três linhas decidem o resultado: a nova ALE é a probabilidade final vezes o impacto; a redução é a ALE atual menos a nova; e o ROSI é a redução menos o custo, dividido pelo custo. É a fórmula do slide 7 escrita em Python. A saída confirma 87% no otimista, em verde, e 7% no conservador, em amarelo. A última linha calcula o ponto de equilíbrio: 0,12 menos 300 mil dividido por 8 milhões dá 8,25%. Abaixo dessa probabilidade o programa se paga. Agora o `roadmap.csv`: cinco iniciativas, cada uma com a redução de risco anual, o custo e o trimestre mínimo. O `priorizar.py` divide a redução pelo custo para saber quanto risco cada real reduz e ordena da maior razão para a menor. Depois percorre a lista e só aceita a iniciativa se o gasto acumulado continuar dentro dos R$ 300 mil; essa comparação é a linha que decide quem entra. Na saída, entram o MFA resistente a *phishing* e os *tabletops*, os dois com razão 3,00, os ciclos *purple*, com 2,44, e a telemetria de nuvem, com 1,71. O orçamento usado é R$ 240 mil. A operação de Red Team, com razão 1,27, fica como ESPERA: os R$ 60 mil que sobram não cobrem os R$ 110 mil dela."
Atenção: o terminal imprime "8.25%" com ponto, porque o Python formata números em inglês; diga em voz alta "oito vírgula vinte e cinco por cento". Se o aluno estranhar o Red Team fora do orçamento, lembre que ele continua no calendário; o que o script mostra é que falta verba para ele neste ano.
Conclusão: "Com as premissas à vista, o conselho decide sabendo o risco: aprovar R$ 110 mil a mais ou adiar o Red Team para o ano seguinte."
[Tela: gravação do laboratório do slide 10]

**Slide 11 — Laboratório na plataforma Rede Tatame: do ponto cego ao roadmap (10:40–12:50)**
Objetivo: ver que as primeiras linhas do *roadmap* saem dos pontos cegos medidos na plataforma.
Na tela:
1. A plataforma abre na aba **Cobertura ATT&CK**. Ler os quadros: 16 técnicas nos cenários, 0 comprovadas, 6 detectáveis sem teste, 6 parciais, 4 cegas e cobertura com regra de 38%.
2. Ir à aba **Arquitetura** e clicar em **Catracas IoT** e em **Data lake**: o painel informa que a telemetria está desligada.
3. Ir à aba **Telemetria** e ligar as três fontes desligadas: "Acesso a buckets e saída de rede", "Heartbeat e firmware das catracas" e "Monitor de certificados (CT)". Mostrar o custo mensal passando de R$ 2.462 para R$ 2.586.
4. Voltar a **Cobertura ATT&CK**: as cegas somem, mas a cobertura com regra continua em 38%.
5. Ir à aba **Regras do CEP** e ligar R9 (saída volumosa para destino novo), R10 (catraca fora do padrão) e R12 (certificado novo para subdomínio fora do inventário).
6. Voltar a **Cobertura ATT&CK**: a cobertura com regra sobe para 63%.
Fala: "Os cartões coloridos embaixo mostram cada técnica dos cenários com o seu estado. Cega quer dizer que não há telemetria; parcial, que há telemetria mas falta regra; detectável, que há fonte e regra, mas ninguém testou; comprovada, que a regra foi testada com sucesso. Começamos com 4 cegas. Na Arquitetura vemos o porquê: as catracas e o *data lake* não enviam eventos ao SIEM. Na Telemetria ligamos as três fontes, e a plataforma mostra o preço: o custo de ingestão sobe para R$ 2.586 por mês. As cegas desaparecem, mas a cobertura não muda, porque ver o evento ainda não gera alerta. Só quando ligamos R9, R10 e R12 a cobertura vai de 38% para 63%. Mesmo assim, o quadro de comprovadas continua em zero."
Atenção: não é preciso iniciar nenhum cenário nem mudar a velocidade neste laboratório. Se a plataforma já tiver sido usada em outro slide, recarregue o deck para voltar ao estado inicial de 38%.
Conclusão: "Fonte e regra novas viram linhas do *roadmap* com custo conhecido, e a próxima linha é um ciclo *purple* para comprovar essas regras."
[Tela: gravação do laboratório do slide 11]

**Slide 12 — Tendências: Zero Trust e nuvem (12:50–13:40)**
Fala: "Duas tendências mudam o que entra no plano de testes. O Zero Trust, descrito no NIST SP 800-207, tira a confiança implícita da localização na rede: cada acesso é verificado por identidade, dispositivo e contexto. Para o *purple teaming*, isso significa testar sobretudo o abuso de identidades e credenciais válidas, como vimos com a VPN sem MFA. E a nuvem desloca parte da superfície de ataque para configurações, identidades e APIs. A matriz ATT&CK tem uma seção própria para nuvem, e os planos de emulação precisam incluí-la."

**Slide 13 — Tendências: inteligência artificial nos dois lados (13:40–14:20)**
Fala: "A IA aparece em três papéis. No ataque, relatórios como o *ENISA Threat Landscape* registram o uso de IA generativa para deixar a engenharia social mais convincente e em maior escala. Na defesa, ela ajuda na triagem de alertas, no resumo de investigações e na análise de grandes volumes de dados, mas erra e precisa de supervisão. E como alvo: a MITRE mantém o ATLAS, uma base de táticas e técnicas contra sistemas de IA, nos moldes do ATT&CK. Vamos ver os dois primeiros papéis na prática."

**Slide 14 — Laboratório: IA no ataque e na defesa (14:20–15:50)**
Objetivo: mostrar onde a IA ajuda e onde engana, e por que o programa precisa de revisão humana.
Na tela:
1. A aba **Conscientização** do Portal do SOC já vem aberta. Ler os quadros "Como era" e "Como pode ser com IA generativa".
2. Mostrar o exemplo de treinamento: remetente repasses@tatame-repasses.com, assunto "Repasse das academias de outubro".
3. Clicar na aba **Assistente do SOC** e ler o resumo do caso INC-2026-1104, marcado como "aguardando revisão humana".
4. Clicar em **Conferir com a linha do tempo**: os trechos errados ficam destacados em vermelho e aparece a revisão de Luiza Ferraz.
Fala: "Antes, o *phishing* tinha erros de português e um pedido vago. Com IA generativa, o texto fica fluente, usa o tom da empresa e cita um assunto do dia a dia, como esta mensagem fictícia para a Carla sobre os repasses. Por isso o treinamento muda o foco para sinais que continuam valendo: domínio parecido mas diferente do oficial, urgência com prazo curto, pedido de clique ou de senha e um canal para confirmar por fora. Na defesa, o assistente resumiu o incidente em quatro linhas. Ao conferir com a linha do tempo, Luiza descobre que o notebook isolado às 09h22 foi o NB-FIN-013, e não o NB-FIN-031, e que a mesma conta fez login nesse segundo notebook às 09h19. O resumo trocou os nomes, omitiu um host e afirmou que nenhum outro host teve atividade. O ganho existe, porque ele poupou a leitura de 140 eventos, mas o erro veio escrito com total confiança."
Atenção: a mensagem é um exemplo de treinamento, sem link funcional; deixe claro que nada nesta página é um ataque real.
Conclusão: "A IA acelera a leitura, mas quem assina o caso e o relatório ao conselho é a analista."
[Tela: gravação do laboratório do slide 14]

**Slide 15 — Carreira: os caminhos de Red, Blue e Purple (15:50–16:30)**
Fala: "Agora, você. O NIST NICE Framework organiza a força de trabalho em cibersegurança em funções, com tarefas, conhecimentos e habilidades. Na tabela estão seis funções que apareceram ao longo da disciplina, do analista de SOC ao *threat hunter*, com certificações conhecidas para cada uma. Certificação ajuda a comprovar conhecimento, mas laboratórios, CTFs, relatórios bem escritos e contribuições a projetos abertos pesam tanto quanto ela."
[Take de apoio: estrada com bifurcações — Envato, "career path road"]

**Slide 16 — Laboratório: o mapa de trilhas em formato de metrô (16:30–17:40)**
Objetivo: ligar o programa contínuo às funções que o fazem funcionar e escolher um primeiro passo.
Na tela:
1. O mapa abre com a estação **Fundamentos** selecionada; ler o quadro embaixo: o que faz, certificações conhecidas e primeiro passo.
2. Seguir a linha vermelha: clicar em **Pentester** e em **Operador de Red Team**.
3. Seguir a linha azul: clicar em **Analista de SOC** e em **Resposta a incidentes**.
4. Clicar em **Engenheiro de detecção** e em **Threat hunter / CTI**, na linha roxa.
Fala: "Toda trilha sai de Fundamentos: redes, Windows e Linux, programação e a lógica de ataque e defesa desta disciplina, com um primeiro passo simples, como o picoCTF e a leitura da matriz ATT&CK. A linha vermelha é ofensiva: *pentester*, com PenTest+ e OSCP, e depois operador de Red Team. A azul é defensiva: analista de SOC, com Security+ e CySA+, e resposta a incidentes, com GCIH. A roxa liga as duas pela engenharia de detecção e pela caça a ameaças, as funções que mais vivem o *purple teaming*. Repare que o analista de SOC também tem ligação direta com a engenharia de detecção. Escolha uma estação de chegada e anote o primeiro passo dela."
Atenção: as certificações são exemplos conhecidos do mercado, sem recomendação de uma em particular.
Conclusão: "As trilhas se cruzam: muita gente começa no SOC e migra para o Red Team, e o programa contínuo precisa das duas pontas."
[Tela: gravação do laboratório do slide 16]

**Slide 17 — O caminho percorrido nas quatro unidades (17:40–18:30)**
Fala: "Olhe o caminho que fizemos. Na Unidade 1, a base: os papéis de Red, Blue e Purple, a ética e a legalidade, a Kill Chain, o ATT&CK e os fundamentos da defesa. Na Unidade 2, uma operação ofensiva controlada, sempre perguntando que rastro cada ação deixa. Na Unidade 3, a defesa coletando telemetria, detectando, caçando e respondendo. Na Unidade 4, tudo unido em ciclos de melhoria mensuráveis, exercícios e um programa contínuo. Na Videoaula 1 perguntei por que alguém pagaria para ser atacado. A resposta é que só um ataque autorizado, medido e seguido de correção e reteste transforma 'achamos que estamos seguros' em evidência para decidir. No estudo de caso, você vai percorrer esse caminho de ponta a ponta."

**Slide 18 — De volta ao problema: "Estamos seguros?" (18:30–19:20)**
Fala: "Voltemos aos dez minutos de Marina com o conselho. Ela leva quatro evidências. Um calendário com ritmo fixo para varreduras, *pentests*, ciclos *purple*, *tabletops* e Red Team, com relatório trimestral. Um caso de negócio com ALE de R$ 960 mil, ROSI entre 7% e 87% e um *roadmap* que cabe em R$ 300 mil. Um *roadmap* que nasce das lacunas medidas, levando a cobertura da plataforma de 38% para 63% a R$ 2.586 por mês. E quatro unidades de evidência: ataque autorizado, detecção medida, melhoria retestada e exercitada. A resposta à pergunta da aula é um programa contínuo, governado pela CISO, com calendário, orçamento em linguagem de risco e achados que viram ações retestadas. E a resposta à pergunta da Aula 1 é honesta: a Rede Tatame ainda não está 100% segura, mas agora sabe o que detecta, em quanto tempo responde e o que falta, e mede isso todo trimestre."

**Slides 19 e 20 — Pontos-chave e referências (19:20–19:40)**
Fala: "Leve quatro ideias desta aula: o programa integra testes, exercícios e melhorias sob governança e orçamento; ALE e ROSI justificam investimentos quando as premissas estão explícitas; Zero Trust, nuvem e IA mudam o que testamos; e o NICE Framework orienta a carreira, enquanto a prática a consolida. As referências estão no slide seguinte."

**Slide 21 — Encerramento da disciplina (19:40–20:00)**
Fala: "Aqui termina a disciplina Red Team & Blue Team Strategies. O próximo passo é seu: pratique em laboratórios e CTFs, explore a matriz ATT&CK, escolha uma trilha e uma certificação inicial. E lembre que, nesta área, autorização e ética vêm antes de qualquer técnica. Obrigado por percorrer este caminho comigo até aqui, e sucesso na sua jornada!"
[Take de apoio: formandos comemorando — Envato, "graduation celebration"]

## Quiz não avaliativo

### Questão 1 (verdadeiro ou falso)

Se o mapa do ATT&CK Navigator de uma organização mostra 80% das técnicas priorizadas marcadas como "cobertas" porque existe uma regra de detecção para cada uma delas, pode-se concluir que a organização detectaria 80% das ações de um adversário real.

( ) Verdadeiro  
(X) Falso

### Questão 2 (múltipla escolha)

Em um exercício de *purple teaming*, a equipe executou uma técnica, constatou que não houve alerta e criou uma nova regra de detecção. Qual deve ser o passo seguinte para concluir o ciclo?

a) Registrar a técnica como coberta no relatório final.  
b) Desativar as regras antigas relacionadas à técnica.  
*c) Executar a técnica novamente para comprovar que a nova regra gera o alerta esperado.  
d) Agendar uma operação de Red Team sem aviso para o ano seguinte.

### Feedback

**Questão 1 — Falso.** A existência de uma regra não garante que ela funcione. A cobertura que tem valor é a **testada**, validada por execução real da técnica, como nos ciclos de *purple teaming*. Além disso, uma técnica pode ser executada de vários modos (procedimentos), e a regra pode detectar apenas alguns deles; e o adversário pode usar técnicas fora da lista priorizada. Por isso, a cobertura ATT&CK é um indicador útil, mas não uma probabilidade de detecção.

**Questão 2 — Alternativa c.** O ciclo do *purple teaming* é planejar, executar, observar, ajustar e **retestar**. Sem o reteste, a nova regra é apenas uma hipótese: ela pode conter erros de lógica, depender de um registro que não está sendo coletado ou gerar alertas apenas em condições diferentes das reais. Só depois de comprovada a técnica pode ser contabilizada como coberta.

## Material complementar

### Direto da fonte (livro da Biblioteca Virtual)

- **Texto provocativo:** Emular um adversário não é “atacar do jeito que der”: é escolher um grupo real, estudar suas táticas, técnicas e procedimentos e transformá-los em um plano que a defesa possa testar e medir. O capítulo indicado, escrito por um contribuidor do MITRE ATT&CK, mostra como montar esse plano passo a passo — exatamente a base dos ciclos de *purple teaming* desta unidade.
- **Nome do livro:** SANTOS, Joas Antonio dos. *Introdução ao Red Team Operations 2.0*: um guia básico para suas operações de Red Team. Rio de Janeiro: Brasport, 2024. *E-book*.
- **Capítulo:** 7 — Construindo seu plano de emulação de adversário
- **Link de acesso:** <https://plataforma.bvirtual.com.br/Acervo/Publicacao/220894>
- **Aula em que entra:** Aula 13

### Para mergulhar no assunto (saiba mais)

- **Texto provocativo:** Imagine receber um cenário de crise pronto, com perguntas de discussão, roteiro para o facilitador e modelo de relatório — de graça. A CISA disponibiliza pacotes de exercícios *tabletop* sobre temas como *ransomware*, ameaça interna e ataques à cadeia de suprimentos. Escolha um deles e tente conduzi-lo com colegas de turma ou de trabalho: você vai descobrir que as perguntas mais difíceis não são técnicas.
- **Link:** <https://www.cisa.gov/resources-tools/services/cisa-tabletop-exercise-packages>
- **Link complementar (prática técnica gratuita):** picoCTF — <https://picoctf.org/>
- **Aula em que entra:** Aula 15

### Podcast (curadoria, até 45 min)

- **Texto provocativo:** Como é, na prática, o dia a dia de quem trabalha com segurança no Brasil? Que certificações valem a pena e o que os recrutadores realmente observam? Ouvir profissionais da área falando de carreira, mercado e tendências ajuda você a planejar os próximos passos depois desta disciplina.
- **Nome do podcast:** Segurança Legal **[conferir]**
- **Nome do episódio:** [selecionar episódio sobre carreira em cibersegurança ou exercícios de simulação, com até 45 min] **[conferir episódio, duração e link]**
- **Link:** <https://www.segurancalegal.com/> **[conferir]**
- **Aula em que entra:** Aula 16

### Artigo científico

- **Texto provocativo:** Antes de ser uma plataforma conhecida de emulação de adversários, o Caldera foi um projeto de pesquisa da MITRE que buscava responder a uma pergunta ousada: é possível automatizar um Red Team que planeja seus próximos passos como um adversário real? Ler o artigo original ajuda a entender o potencial — e os limites — da automação no *purple teaming*.
- **Link:** <https://dl.acm.org/doi/10.1145/2991079.2991111> **[conferir link e DOI]**
- **Aula em que entra:** Aula 13
- **Referência ABNT:** APPLEBAUM, Andy; MILLER, Doug; STROM, Blake; KORBAN, Chris; WOLF, Ross. Intelligent, automated red team emulation. *In*: ANNUAL CONFERENCE ON COMPUTER SECURITY APPLICATIONS, 32., 2016, Los Angeles. *Proceedings* [...]. New York: ACM, 2016. p. 363-373. **[conferir páginas]**
