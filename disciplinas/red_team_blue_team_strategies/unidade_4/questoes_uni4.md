# Questionário — Unidade 4

Disciplina: Red Team & Blue Team Strategies  
Professor-conteudista: Afonso Cesar Lelis Brandão  
Template de origem: `documentos/Unidade 4/40 Questões - UNI4_nomedadisciplina.docx`

Quantidade obrigatória: 40 questões padrão ENADE — 20 de asserção-razão (1 a 20) e 20 de interpretação (21 a 40).
Cinco alternativas por questão (a–e); a correta é marcada com `*` imediatamente antes da letra.
Feedback para **cada alternativa** (por que está correta ou qual o equívoco), todos ao final do documento.
Distribuição da letra correta: 8 questões para cada uma das letras a, b, c, d, e, no total das 40 questões.

## Questões

### Asserção-razão

**1.** I. Em um exercício de *purple teaming*, o Blue Team sabe previamente quais técnicas serão executadas e quando, e acompanha cada passo da execução.

PORQUE

II. No *purple teaming*, o objetivo deixa de ser avaliar a reação a um ataque surpresa e passa a ser aprender rápido, transformando cada técnica executada em melhoria da detecção e da resposta.

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**2.** I. No ciclo do *purple teaming*, a etapa de retestar é indispensável para que uma técnica possa ser contabilizada como coberta.

PORQUE

II. Uma regra de detecção criada durante a sessão já está comprovada no momento em que é escrita, pois foi elaborada pelo Blue Team a partir da observação da telemetria.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**3.** I. Emulação de adversários e simulação de técnicas genéricas são atividades equivalentes, sem diferença quanto à fidelidade ao comportamento de um ator de ameaça real.

PORQUE

II. A defesa informada por ameaças (*threat-informed defense*) recomenda escolher aleatoriamente as técnicas a testar, para evitar que a inteligência de ameaças introduza viés no exercício.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

**4.** I. Plataformas como o MITRE Caldera e as soluções de *breach and attack simulation* (BAS) permitem aumentar a frequência dos testes de detecção de uma organização.

PORQUE

II. A *Adversary Emulation Library*, mantida pelo MITRE Center for Threat-Informed Defense, reúne planos de emulação baseados em grupos documentados, como APT29, FIN6 e menuPass.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**5.** I. Por ser conduzido por equipes internas e de forma colaborativa, um exercício de *purple teaming* dispensa escopo, autorização e regras de engajamento por escrito.

PORQUE

II. Ferramentas automatizadas de emulação testam técnicas conhecidas, enquanto o adversário real improvisa, razão pela qual a automação deve complementar, e não substituir, operadores e analistas experientes.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**6.** I. Ao acompanhar indicadores de tempo como o MTTD e o MTTR, é recomendável observar também a mediana, e não apenas a média.

PORQUE

II. A média é sensível a valores extremos, de modo que um único incidente que permaneceu sem detecção por 90 dias pode distorcer o indicador de um trimestre inteiro.

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**7.** I. O indicador "bloqueamos 2 milhões de ataques este ano" é uma boa métrica para demonstrar a capacidade de uma organização de enfrentar um adversário competente.

PORQUE

II. Boas métricas de segurança respondem a perguntas de decisão, como se a organização está melhorando, onde investir e qual risco ainda é aceito.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**8.** I. Reduzir a taxa de falsos positivos de um SOC é uma melhoria de segurança, e não apenas de produtividade, porque diminui o risco de fadiga de alertas.

PORQUE

II. O NIST CSF 2.0 descreve quatro níveis (*tiers*) para o rigor da governança e da gestão de riscos cibernéticos: Parcial, Informado por riscos, Repetível e Adaptativo.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**9.** I. A cobertura ATT&CK testada é um indicador mais confiável do que a simples contagem de técnicas para as quais existe uma regra de detecção.

PORQUE

II. Cada técnica ATT&CK só pode ser executada de uma única forma, de modo que uma regra que detecta um procedimento detecta automaticamente qualquer outra execução da mesma técnica.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**10.** I. Cobrar um SOC exclusivamente pela redução do MTTR pode levar a equipe a encerrar incidentes antes de concluir adequadamente a contenção e a investigação.

PORQUE

II. De acordo com a Lei de Goodhart, quando uma métrica se torna meta, ela tende a deixar de ser uma boa medida, pois as pessoas passam a otimizar o número em vez do objetivo que ele deveria representar.

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**11.** I. Segundo o NIST SP 800-84, o exercício simula um cenário para validar planos, políticas e capacidades, distinguindo-se do treinamento e do teste.

PORQUE

II. O NIST SP 800-84 classifica o *tabletop* como um exercício funcional, no qual os participantes executam tecnicamente suas funções em um ambiente simulado.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**12.** I. Em um exercício *tabletop*, os *injects* são dispensáveis, pois o cenário apresentado no início já contém todas as informações necessárias para as decisões da equipe.

PORQUE

II. O *tabletop* é um formato voltado exclusivamente ao público técnico, sem a participação de áreas como jurídico, comunicação e diretoria.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

**13.** I. O formato *Jeopardy* de *capture the flag* (CTF), com desafios independentes organizados por categoria e pontuação, é o mais comum para iniciantes.

PORQUE

II. O Locked Shields é um exercício anual de defesa cibernética ao vivo, organizado pelo Centro de Excelência em Defesa Cibernética Cooperativa da OTAN (CCDCOE).

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**14.** I. O *cyber range* é, entre os formatos de exercício estudados, o de menor custo e preparo, sendo por isso o mais indicado como primeira atividade para envolver a diretoria executiva.

PORQUE

II. Um *cyber range* é um ambiente virtual controlado que reproduz uma rede realista e permite executar ataques simulados sem risco ao ambiente de produção.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**15.** I. Os objetivos de um exercício de simulação devem ser definidos de forma mensurável antes de seu início, como "acionar o plano de comunicação em até 1 hora".

PORQUE

II. Um exercício só gera valor se for avaliado, e a avaliação depende de critérios estabelecidos previamente, que fundamentam o *hot wash*, o relatório pós-ação e o plano de melhoria.

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**16.** I. A função Governar (*Govern*), incluída no NIST CSF 2.0, abrange a definição do apetite a riscos, de papéis e responsabilidades, de políticas e da supervisão pela alta administração.

PORQUE

II. A MITRE mantém o ATLAS, uma base de táticas e técnicas de ataque contra sistemas de inteligência artificial, organizada nos moldes do ATT&CK.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**17.** I. Os resultados de ALE e de ROSI devem ser apresentados à diretoria como valores exatos, sem faixas nem premissas, para transmitir confiança na decisão de investimento.

PORQUE

II. ALE e ROSI dependem de estimativas, como a probabilidade anual de um incidente, e pequenas variações nessas premissas podem alterar significativamente o resultado.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**18.** I. Em uma organização que adota a arquitetura *Zero Trust*, os ciclos de *purple teaming* devem dar atenção especial ao abuso de identidades e de credenciais válidas.

PORQUE

II. No modelo *Zero Trust*, descrito no NIST SP 800-207, todo acesso originado na rede interna é considerado confiável e dispensa verificação adicional.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**19.** I. Certificações profissionais são suficientes para comprovar competência em segurança, o que torna dispensáveis laboratórios, CTFs e relatórios práticos no portfólio de um profissional.

PORQUE

II. O NIST NICE Framework organiza a força de trabalho em cibersegurança exclusivamente por certificações, sem descrever tarefas, conhecimentos ou habilidades associados a cada função.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

**20.** I. A adoção de ferramentas de inteligência artificial na defesa não elimina a necessidade de analistas humanos no SOC.

PORQUE

II. As ferramentas de IA trazem ganhos reais na triagem de alertas e no resumo de investigações, mas também cometem erros, o que exige supervisão humana sobre seus resultados.

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Interpretação

**21.** A equipe de segurança da Varejo Horizonte montou um plano de emulação com 40 técnicas ATT&CK associadas a um grupo de *ransomware* que ataca o varejo. Na primeira execução, 12 técnicas geraram alerta. Durante a própria sessão, a equipe criou regras para outras 10 técnicas que já tinham telemetria. No reteste, 8 dessas novas regras geraram o alerta esperado e 2 não dispararam. Considerando apenas detecções comprovadas por execução, qual é a cobertura testada do plano ao final da sessão?

a. 55%, pois as 10 novas regras somam-se às 12 detecções iniciais.
*b. 50%.
c. 30%, pois as regras criadas na sessão só contam no ciclo seguinte.
d. 20%, considerando apenas as regras que passaram no reteste.
e. 45%.

**22.** Durante uma sessão de *purple teaming* na Transportadora Rota Sul, o facilitador registrou o seguinte quadro:

| Técnica | Telemetria | Alerta | Resposta do analista |
|---|---|---|---|
| A — T1059 (*Command and Scripting Interpreter*) | Sim | Sim | Adequada |
| B — T1003 (*OS Credential Dumping*) | Sim | Não | — |
| C — T1021 (*Remote Services*) | Não | Não | — |

Com base no ciclo do *purple teaming*, qual é a leitura correta do quadro?

a. A técnica A pode ser excluída dos próximos ciclos, e as técnicas B e C podem ser registradas como cobertas assim que as novas regras forem escritas.
b. Para a técnica B, é preciso habilitar uma nova fonte de registros; para a técnica C, basta criar uma regra sobre a telemetria já existente.
c. As três técnicas estão cobertas, pois o Red Team conseguiu executá-las e o Blue Team acompanhou a execução.
d. As técnicas B e C devem ser aceitas imediatamente como risco residual, sem ajustes, porque não geraram alerta na primeira execução.
*e. Para B, cabe criar ou refinar uma regra sobre a telemetria existente; para C, habilitar antes a fonte de registros; ambas exigem reteste.

**23.** O Banco Aurora, instituição financeira de médio porte, vai iniciar seu programa de *purple teaming* e precisa decidir quais técnicas testar primeiro. A equipe tem tempo limitado e quer que os resultados sejam relevantes para o risco real da organização. Qual abordagem é a mais adequada?

*a. Elaborar um plano de emulação a partir de inteligência de ameaças sobre grupos com histórico de ataques ao setor financeiro.
b. Executar todas as técnicas da matriz ATT&CK em ordem aleatória, para evitar qualquer viés na seleção dos testes.
c. Contratar uma plataforma de BAS e dispensar a participação de analistas, já que a automação cobre as técnicas conhecidas.
d. Emular grupos voltados à sabotagem industrial, por serem considerados os mais sofisticados, independentemente do setor atacado.
e. Deixar o Red Team escolher livremente as técnicas, sem informar o Blue Team, para preservar o realismo do exercício *purple*.

**24.** Um engenheiro de detecção da Clínica Vitalis acabou de escrever uma regra para a técnica T1053 (*Scheduled Task/Job*) e quer validá-la rapidamente com um teste pequeno, já mapeado a essa técnica, em um laboratório autorizado. Qual recurso estudado na Aula 13 atende diretamente a essa necessidade?

a. ATT&CK Navigator, que permite visualizar a cobertura e o plano de emulação sobre a matriz.
b. *Adversary Emulation Library*, que reúne planos completos de emulação baseados em grupos reais.
c. MITRE Caldera, plataforma para automatizar campanhas completas de emulação de adversários.
*d. Atomic Red Team.
e. DeTT&CT, que pontua separadamente visibilidade e detecção de cada técnica.

**25.** Relato de uma sessão de *purple teaming* na Logística Veloz: "Em quatro horas, percorremos apenas 3 das 20 técnicas planejadas. As discussões sobre cada alerta se estenderam sem conclusão, e ninguém registrou quem criaria as regras pendentes nem quando." Qual papel, descrito no *Purple Team Exercise Framework* (PTEF), foi mal exercido nessa sessão?

a. O operador do Red Team, que deveria ter executado as técnicas sem avisar os defensores, para acelerar a sessão.
b. O analista de inteligência de ameaças, que deveria ter reduzido o plano a apenas três técnicas.
*c. O facilitador, responsável por conduzir a sessão, controlar o tempo e garantir que as discussões terminem em tarefas concretas.
d. A plataforma de BAS, que deveria ter substituído a discussão entre as equipes.
e. O avaliador externo, encarregado de atribuir notas de maturidade ao SOC durante a sessão.

**26.** O SOC da Editora Prisma registrou os seguintes números antes e depois de três ciclos de *purple teaming*:

| Período | Alertas no mês | Verdadeiros positivos |
|---|---|---|
| Março | 2.000 | 300 |
| Setembro | 800 | 240 |

Qual alternativa apresenta corretamente a precisão dos alertas em março e em setembro, respectivamente?

a. 15% e 24%.
b. 85% e 70%.
c. 15% e 20%.
d. 30% e 15%.
*e. 15% e 30%.

**27.** Após a implantação de novas fontes de telemetria e de regras validadas em ciclos *purple*, o MTTD mediano da Agro Campos caiu de 20 horas para 5 horas. Qual foi a redução percentual do MTTD?

a. 25%.
b. 15%.
*c. 75%.
d. 300%.
e. 80%.

**28.** No último trimestre, o SOC da Construtora Pilar tratou dez incidentes. Em nove deles, o tempo entre a detecção e a contenção foi de 2 horas; em um, foi de 90 dias (2.160 horas). Qual interpretação é a mais adequada?

a. A média do trimestre é de 2 horas, o que indica um desempenho uniformemente bom do SOC.
*b. A média (cerca de 218 horas) é distorcida pelo caso extremo; a mediana (2 horas) representa o caso típico, e o incidente atípico deve ser investigado.
c. A mediana é de cerca de 218 horas, pois considera o peso de todos os incidentes do período.
d. O incidente de 90 dias deve ser excluído do relatório, já que não representa a operação normal do SOC.
e. A média é sempre o indicador preferível, por incluir todos os valores; a mediana não deve ser usada em métricas de tempo.

**29.** A *layer* do ATT&CK Navigator do Grupo Méridien mostra 45 das 50 técnicas priorizadas pela inteligência de ameaças em verde, porque existe uma regra de detecção para cada uma delas. A análise detalhada revela que há telemetria disponível para 35 dessas técnicas e que apenas 20 tiveram a detecção validada em ciclos de *purple teaming*. Qual leitura está correta?

a. A cobertura ATT&CK é de 90%, pois toda técnica com regra cadastrada pode ser considerada coberta.
b. A cobertura testada é de 70%, já que a existência de telemetria garante a detecção da técnica.
c. A meta deve ser ampliar o mapa para 100% da matriz ATT&CK, independentemente das técnicas priorizadas.
*d. A cobertura testada é de 40% e a visibilidade, de 70%; os 90% indicam apenas a existência de regras.
e. A cobertura testada é de cerca de 44%, calculada sobre as 45 técnicas que possuem regra cadastrada.

**30.** A gerente de segurança da Seguradora Atlântica terá cinco minutos na reunião da diretoria para mostrar a evolução do SOC no semestre. Qual indicador comunica melhor o progresso em linguagem de decisão e de risco?

*a. A cobertura testada das técnicas mais usadas contra o setor de seguros subiu de 45% para 72% no semestre.
b. O SOC processou 14.300 alertas no semestre, um aumento de 20% em relação ao período anterior.
c. Uma lista com a precisão individual de cada uma das 180 regras de detecção em produção.
d. Os sistemas de proteção bloquearam 2 milhões de tentativas de ataque ao longo do semestre.
e. A equipe escreveu 60 novas regras de detecção, número recorde desde a criação do SOC.

**31.** Em um *tabletop* de *ransomware* com 10 *injects*, os avaliadores atribuíram de 0 a 3 pontos à resposta da equipe em cada *inject*. No primeiro exercício, a equipe somou 15 pontos; no exercício seguinte, após revisar o plano e treinar o jurídico, somou 24 pontos. Qual foi o desempenho percentual em cada exercício?

a. 50% e 24%.
b. 15% e 24%.
c. 50% e 70%.
*d. 50% e 80%.
e. 60% e 80%.

**32.** A cooperativa de crédito Unicredi, com 40 agências, nunca realizou exercícios de simulação. A diretoria afirma que "o plano de resposta a incidentes está aprovado, então estamos preparados". O SOC é terceirizado e o *backup* nunca foi restaurado em um teste completo. Qual deve ser o primeiro exercício recomendado?

a. Um exercício em *cyber range* com equipes Red e Blue, por reproduzir com mais realismo a infraestrutura das agências.
b. Um CTF no formato *Jeopardy* para a diretoria, para desenvolver as habilidades técnicas dos executivos.
c. Uma operação completa de Red Team sem aviso, para comprovar à diretoria que o plano aprovado é insuficiente.
d. Nenhum exercício por ora, pois o plano já aprovado pela diretoria cumpre o papel de validar a capacidade de resposta.
*e. Um *tabletop*, de baixo custo, que reúna público técnico e executivo para testar decisões, papéis e comunicação.

**33.** Trecho do roteiro de um exercício na Indústria Metalcorte: "14h20 — O facilitador anuncia: 'Um jornalista ligou pedindo posicionamento sobre o vazamento de dados de clientes.' Os participantes têm 10 minutos para decidir quem responde e o que será dito." Como se denomina esse elemento do exercício?

a. *Hot wash*.
b. Relatório pós-ação (*after-action report*).
*c. *Inject*.
d. *Flag*.
e. Célula de controle.

**34.** A equipe técnica da Fintech Lumen quer um treinamento em que cada time receba uma infraestrutura com serviços vulneráveis, precise protegê-los enquanto tenta explorar os serviços dos outros times e dependa de trabalho coordenado. Qual formato de exercício corresponde a essa descrição?

a. CTF no formato *Jeopardy*.
*b. CTF no formato ataque e defesa.
c. Exercício *tabletop* baseado em discussão de cenário.
d. *Hot wash* conduzido logo após um incidente real.
e. Treinamento de papéis e procedimentos, conforme o NIST SP 800-84.

**35.** Leia o resumo do relatório de um exercício *tabletop* da Rede Farmavida:

> "Objetivos definidos previamente. *Hot wash* realizado ao final. O relatório pós-ação lista seis lacunas, entre elas a demora em notificar a ANPD. Não foram atribuídos responsáveis nem prazos às ações. O próximo exercício está previsto para daqui a 12 meses, com um cenário diferente."

Qual é a principal fragilidade desse processo?

a. A realização do *hot wash*, que deveria ser dispensada quando há relatório formal.
b. A inclusão de lacunas no relatório, que deveria registrar apenas os pontos fortes da equipe.
c. A escolha do formato *tabletop*, que deveria ter sido substituído por um CTF de forense.
d. A definição prévia dos objetivos, que deveria ocorrer somente após o término do exercício.
*e. As ações de melhoria sem dono, sem prazo e sem previsão de verificação no exercício seguinte.

**36.** A Distribuidora Norte estima a perda de um incidente grave em R$ 5 milhões, com probabilidade anual de 20%. Um programa contínuo de segurança custa R$ 250.000 por ano e, segundo as premissas da equipe, reduziria essa probabilidade para 10%. Qual alternativa apresenta corretamente a ALE inicial e o ROSI do programa?

*a. ALE inicial de R$ 1.000.000 e ROSI de 100%.
b. ALE inicial de R$ 1.000.000 e ROSI de 200%, obtido ao dividir a redução da perda esperada pelo custo.
c. ALE inicial de R$ 500.000 e ROSI de 100%.
d. ALE inicial de R$ 1.000.000 e ROSI de 50%.
e. ALE inicial de R$ 1.000.000 e ROSI de 300%, obtido a partir da ALE inicial completa.

**37.** Retome o caso da Distribuidora Norte (perda estimada de R$ 5 milhões, probabilidade anual inicial de 20% e programa de R$ 250.000 por ano). Em um cenário conservador, a probabilidade final seria de 15%, e não de 10%. Qual é a interpretação correta desse cenário?

a. O ROSI permanece em 100%, pois o custo do programa não mudou.
b. O ROSI torna-se negativo, de −50%, indicando que o programa destrói valor.
*c. A redução esperada (R$ 250.000) apenas iguala o custo, o ROSI cai a 0%, e isso evidencia a sensibilidade às premissas.
d. O ROSI sobe para 200%, pois uma probabilidade final maior aumenta a perda evitada.
e. O cálculo deixa de ser válido, porque o ROSI só pode ser aplicado quando a probabilidade final é zero.

**38.** O novo CISO da Energética Vale Azul apresentou o seguinte plano anual:

> "Varreduras contínuas; *pentests* em sistemas novos; ciclos *purple* mensais; *tabletop* semestral; uma operação de Red Team por ano. Os achados serão registrados em uma planilha compartilhada, sem responsável definido. O relatório trimestral à diretoria listará todas as vulnerabilidades técnicas encontradas, identificadas por CVE."

Qual ajuste torna o plano mais aderente a um programa contínuo de segurança?

a. Eliminar os ciclos *purple* mensais, já que a operação anual de Red Team cobre as mesmas técnicas.
b. Substituir os *tabletops* semestrais por varreduras adicionais, que geram resultados mais objetivos.
c. Retirar o patrocínio executivo do programa, para que a equipe técnica tenha mais autonomia.
*d. Dar dono, prazo e reteste aos achados, integrando-os à gestão de riscos, e reportar à liderança em linguagem de risco e de negócio.
e. Detalhar ainda mais o relatório à diretoria, incluindo a descrição técnica de cada CVE e seus *exploits* conhecidos.

**39.** Uma estudante concluiu a disciplina e descobriu que gosta de escrever regras de detecção, testá-las contra técnicas emuladas em laboratório e ajustá-las para reduzir falsos positivos. Considerando as funções apresentadas na Aula 16, qual trilha de carreira corresponde melhor a esse perfil?

a. *Pentester*, que realiza testes de invasão em escopo definido.
b. Operador de Red Team, dedicado à emulação de adversários orientada a objetivos.
c. Resposta a incidentes, com foco em contenção, investigação e recuperação.
d. Analista de SOC, concentrado na triagem e na investigação de alertas recebidos.
*e. Engenheiro de detecção.

**40.** A Rede Educa Mais migrou seus sistemas acadêmicos para a nuvem e adotou uma arquitetura *Zero Trust*. A equipe precisa atualizar o plano de emulação usado nos ciclos de *purple teaming*. Qual atualização é a mais coerente com as tendências estudadas?

a. Concentrar os testes em varreduras do perímetro de rede, pois no *Zero Trust* o tráfego interno é confiável por padrão.
*b. Incluir técnicas da seção de nuvem do ATT&CK e priorizar testes de abuso de identidades e credenciais válidas.
c. Remover os testes de identidade, já que a autenticação multifator elimina o risco de uso indevido de credenciais.
d. Substituir a matriz ATT&CK pelo MITRE ATLAS, que passa a ser a referência para todos os ataques em nuvem.
e. Substituir os analistas do SOC por ferramentas de IA generativa, que dispensam supervisão na triagem de alertas.

## Gabarito e feedbacks

**Questão 1** (correta: a)
- a. Correta: ambas são verdadeiras, e a II explica a I — como o objetivo do *purple teaming* é aprender rápido, e não testar a reação a uma surpresa, os defensores precisam saber o que será executado e acompanhar cada passo.
- b. Incorreta: a II é justamente o motivo da transparência descrita na I; reveja a diferença entre exercício de Red Team tradicional e exercício *purple* (Aula 13).
- c. Incorreta: a II é verdadeira; o foco do *purple teaming* é aprender rápido, e não "vencer".
- d. Incorreta: a I é verdadeira; no exercício *purple* os defensores sabem o que será executado e quando. Quem normalmente não sabe do teste é o Blue Team em um exercício de Red Team tradicional.
- e. Incorreta: as duas asserções são verdadeiras; reveja a definição de *purple teaming* como forma de trabalho colaborativa e transparente.

**Questão 2** (correta: c)
- a. Incorreta: a II é falsa; uma regra recém-escrita, sem execução real da técnica, é apenas uma hipótese.
- b. Incorreta: a II não é verdadeira; escrever a regra não comprova que ela funciona — pode haver erro de lógica ou dependência de um registro não coletado.
- c. Correta: a I é verdadeira, pois o reteste é a etapa que comprova a melhoria; a II é falsa, pois uma detecção nunca testada contra o comportamento real é apenas uma hipótese.
- d. Incorreta: a I é verdadeira; reveja o ciclo planejar, executar, observar, ajustar e retestar.
- e. Incorreta: a I é verdadeira; só a II é falsa.

**Questão 3** (correta: e)
- a. Incorreta: as duas asserções são falsas; emulação e simulação não são equivalentes, e a defesa informada por ameaças não escolhe técnicas ao acaso.
- b. Incorreta: nenhuma das duas é verdadeira; reveja a distinção entre emulação e simulação na Aula 13.
- c. Incorreta: a I é falsa — a emulação reproduz o comportamento de um adversário específico, enquanto a simulação executa técnicas genéricas.
- d. Incorreta: a II é falsa — a defesa informada por ameaças usa a inteligência de ameaças para priorizar as técnicas de quem realmente ameaça a organização.
- e. Correta: a I é falsa, pois emulação tem fidelidade a um ator real e simulação não; a II é falsa, pois a defesa informada por ameaças prioriza técnicas a partir da CTI, e não aleatoriamente.

**Questão 4** (correta: b)
- a. Incorreta: as duas são verdadeiras, mas a existência de uma biblioteca de planos (II) não explica por que plataformas automatizadas aumentam a frequência dos testes (I).
- b. Correta: Caldera e BAS automatizam a execução e aumentam a frequência dos testes (I); a *Adversary Emulation Library* reúne planos baseados em grupos reais (II). São fatos verdadeiros, mas independentes.
- c. Incorreta: a II é verdadeira; a biblioteca do MITRE Center for Threat-Informed Defense inclui planos como APT29, FIN6 e menuPass.
- d. Incorreta: a I é verdadeira; ferramentas automatizadas aumentam a frequência dos testes, embora não substituam o raciocínio humano.
- e. Incorreta: ambas são verdadeiras; reveja a tabela de ferramentas de apoio da Aula 13.

**Questão 5** (correta: d)
- a. Incorreta: a I é falsa; mesmo exercícios internos exigem escopo, autorização e regras de engajamento por escrito.
- b. Incorreta: a I não é verdadeira; a regra da Unidade 1 vale para qualquer atividade ofensiva, inclusive o *purple teaming*.
- c. Incorreta: a situação é a inversa — a I é falsa e a II é verdadeira.
- d. Correta: a I é falsa, porque autorização e regras de engajamento por escrito são obrigatórias mesmo em exercícios internos; a II é verdadeira, pois a automação testa técnicas conhecidas e deve complementar o trabalho humano.
- e. Incorreta: a II é verdadeira; reveja o trecho da Aula 13 sobre os limites da automação.

**Questão 6** (correta: a)
- a. Correta: ambas são verdadeiras, e a sensibilidade da média a valores extremos (II) é exatamente a razão para acompanhar também a mediana (I).
- b. Incorreta: a II justifica diretamente a I; reveja os cuidados com métricas de tempo na Aula 14.
- c. Incorreta: a II é verdadeira; um único caso extremo distorce a média de todo o período.
- d. Incorreta: a I é verdadeira; acompanhar a mediana é uma das recomendações da Aula 14.
- e. Incorreta: ambas são verdadeiras e relacionadas como causa e consequência.

**Questão 7** (correta: d)
- a. Incorreta: a I é falsa; esse tipo de número conta tentativas automatizadas que qualquer filtro barra e nada revela sobre a capacidade diante de um adversário competente.
- b. Incorreta: a I não é verdadeira; trata-se de uma métrica de vaidade, e não de decisão.
- c. Incorreta: ocorre o inverso — a I é falsa e a II é verdadeira.
- d. Correta: a I é falsa, pois o número de ataques bloqueados não mede a capacidade de detecção e resposta; a II é verdadeira, pois boas métricas apoiam decisões sobre melhoria, investimento e risco aceito.
- e. Incorreta: a II é verdadeira; ela resume o critério de boa métrica apresentado na Aula 14.

**Questão 8** (correta: b)
- a. Incorreta: as duas são verdadeiras, mas os *tiers* do NIST CSF 2.0 (II) não explicam por que reduzir falsos positivos melhora a segurança (I); a justificativa da I é a fadiga de alertas.
- b. Correta: a I é verdadeira, porque o excesso de falsos positivos leva analistas a ignorar alertas verdadeiros; a II também é verdadeira, mas trata de maturidade de governança, sem relação causal com a I.
- c. Incorreta: a II é verdadeira; os quatro *tiers* são Parcial, Informado por riscos, Repetível e Adaptativo.
- d. Incorreta: a I é verdadeira; a Aula 14 afirma que reduzir ruído é melhoria de segurança, e não apenas de produtividade.
- e. Incorreta: ambas as asserções são verdadeiras.

**Questão 9** (correta: c)
- a. Incorreta: a II é falsa; uma técnica pode ser executada por muitos procedimentos diferentes.
- b. Incorreta: a II não é verdadeira; uma regra pode detectar apenas um dos procedimentos de uma técnica.
- c. Correta: a I é verdadeira, pois só a cobertura testada comprova que a detecção funciona; a II é falsa, pois uma técnica pode ser executada de várias formas e a regra pode cobrir apenas parte delas.
- d. Incorreta: a I é verdadeira; contar a técnica como coberta só porque existe uma regra é uma das armadilhas descritas na Aula 14.
- e. Incorreta: a I é verdadeira; só a II é falsa.

**Questão 10** (correta: a)
- a. Correta: ambas são verdadeiras, e a Lei de Goodhart (II) explica o risco descrito na I — se o MTTR vira meta isolada, a equipe pode fechar incidentes cedo demais para melhorar o número.
- b. Incorreta: a II justifica diretamente a I; o exemplo do MTTR é usado na Aula 14 para ilustrar a Lei de Goodhart.
- c. Incorreta: a II é verdadeira; reveja o trecho "Do número à decisão".
- d. Incorreta: a I é verdadeira; cobrar apenas MTTR pode gerar encerramentos prematuros.
- e. Incorreta: as duas asserções são verdadeiras e relacionadas.

**Questão 11** (correta: c)
- a. Incorreta: a II é falsa; o *tabletop* é baseado em discussão, e não um exercício funcional.
- b. Incorreta: a II não é verdadeira; o NIST SP 800-84 distingue o *tabletop* (discussão) do exercício funcional (execução das funções em ambiente simulado).
- c. Correta: a I é verdadeira, pois o SP 800-84 distingue treinamento, teste e exercício; a II é falsa, pois o *tabletop* é um formato de discussão, diferente do exercício funcional.
- d. Incorreta: a I é verdadeira; reveja a seção "Por que exercitar" da Aula 15.
- e. Incorreta: a I é verdadeira; apenas a II é falsa.

**Questão 12** (correta: e)
- a. Incorreta: as duas são falsas; os *injects* são essenciais, e o *tabletop* envolve público técnico e executivo.
- b. Incorreta: nenhuma das asserções é verdadeira; reveja os elementos do *tabletop*.
- c. Incorreta: a I é falsa — os *injects* inserem informações novas ao longo do exercício para forçar decisões.
- d. Incorreta: a II é falsa — participam do *tabletop* áreas como TI, jurídico, comunicação e diretoria.
- e. Correta: a I é falsa, pois os *injects* são o que faz o cenário evoluir e exige novas decisões; a II é falsa, pois o *tabletop* reúne público técnico e executivo.

**Questão 13** (correta: b)
- a. Incorreta: as duas são verdadeiras, mas o fato de o Locked Shields ser organizado pelo CCDCOE (II) não explica por que o *Jeopardy* é indicado para iniciantes (I).
- b. Correta: o *Jeopardy*, com desafios independentes por categoria, é o mais comum para iniciantes (I), e o Locked Shields é um exercício de *cyber range* da OTAN (II); são fatos verdadeiros e sem relação de causa.
- c. Incorreta: a II é verdadeira; o Locked Shields é organizado anualmente pelo CCDCOE.
- d. Incorreta: a I é verdadeira; o picoCTF, por exemplo, usa esse formato para iniciantes.
- e. Incorreta: ambas as asserções são verdadeiras.

**Questão 14** (correta: d)
- a. Incorreta: a I é falsa; o *cyber range* tem custo e preparo de médio a alto.
- b. Incorreta: a I não é verdadeira; o formato de menor custo e indicado para envolver a diretoria é o *tabletop*.
- c. Incorreta: ocorre o inverso — a I é falsa e a II é verdadeira.
- d. Correta: a I é falsa, pois o *cyber range* é o formato mais caro e de público técnico; a II é verdadeira, pois descreve corretamente o *cyber range* como ambiente virtual controlado e realista.
- e. Incorreta: a II é verdadeira; reveja a tabela comparativa da Aula 15.

**Questão 15** (correta: a)
- a. Correta: ambas são verdadeiras, e a II explica a I — sem critérios definidos antes, não há como avaliar o exercício nem produzir um plano de melhoria consistente.
- b. Incorreta: a II é a razão pela qual os objetivos precisam ser mensuráveis e prévios.
- c. Incorreta: a II é verdadeira; reveja a seção "Avaliar para melhorar".
- d. Incorreta: a I é verdadeira; a Aula 15 recomenda objetivos mensuráveis definidos antes do exercício.
- e. Incorreta: as duas asserções são verdadeiras e relacionadas.

**Questão 16** (correta: b)
- a. Incorreta: as duas são verdadeiras, mas a existência do ATLAS (II) não justifica o conteúdo da função Governar (I).
- b. Correta: a função Governar trata de apetite a riscos, papéis, políticas e supervisão (I), e o ATLAS cataloga técnicas contra sistemas de IA (II); ambas são verdadeiras, mas independentes.
- c. Incorreta: a II é verdadeira; o ATLAS é mantido pela MITRE nos moldes do ATT&CK.
- d. Incorreta: a I é verdadeira; reveja a seção de governança da Aula 16.
- e. Incorreta: ambas as asserções são verdadeiras.

**Questão 17** (correta: d)
- a. Incorreta: a I é falsa; esses cálculos devem ser apresentados com premissas explícitas e em faixas.
- b. Incorreta: a I não é verdadeira; apresentar estimativas como certezas induz a diretoria ao erro.
- c. Incorreta: ocorre o inverso — a I é falsa e a II é verdadeira.
- d. Correta: a I é falsa, pois ALE e ROSI devem ser apresentados com premissas e em faixas; a II é verdadeira, como mostra o exemplo da Aula 16, em que o ROSI cai de 87% para cerca de 7% ao mudar a probabilidade final.
- e. Incorreta: a II é verdadeira; reveja o exemplo numérico dos cenários otimista e conservador.

**Questão 18** (correta: c)
- a. Incorreta: a II é falsa; o *Zero Trust* elimina justamente a confiança implícita baseada na localização de rede.
- b. Incorreta: a II não é verdadeira; no *Zero Trust*, cada acesso é verificado com base em identidade, dispositivo e contexto.
- c. Correta: a I é verdadeira, pois, se a identidade passa a ser o centro da verificação, o abuso de credenciais válidas é um vetor prioritário de teste; a II é falsa, pois o modelo não confia em nenhum acesso pela origem na rede interna.
- d. Incorreta: a I é verdadeira; a Aula 16 recomenda testar sobretudo o abuso de identidades e credenciais válidas.
- e. Incorreta: a I é verdadeira; apenas a II é falsa.

**Questão 19** (correta: e)
- a. Incorreta: as duas são falsas; a prática pesa tanto quanto as certificações, e o NICE Framework descreve tarefas, conhecimentos e habilidades.
- b. Incorreta: nenhuma das asserções é verdadeira; reveja a seção de carreira da Aula 16.
- c. Incorreta: a I é falsa — laboratórios, CTFs, relatórios e contribuições a projetos abertos demonstram competência real.
- d. Incorreta: a II é falsa — o NICE Framework organiza funções de trabalho (*work roles*) com tarefas, conhecimentos e habilidades.
- e. Correta: a I é falsa, pois certificações não substituem a prática; a II é falsa, pois o NICE Framework é estruturado por funções, tarefas, conhecimentos e habilidades, e não por certificações.

**Questão 20** (correta: a)
- a. Correta: ambas são verdadeiras, e a II explica a I — como as ferramentas de IA erram, seus resultados precisam ser supervisionados por analistas, que continuam necessários.
- b. Incorreta: a II é exatamente o motivo pelo qual a IA não elimina os analistas.
- c. Incorreta: a II é verdadeira; a Aula 16 reconhece ganhos reais e limites das ferramentas de IA.
- d. Incorreta: a I é verdadeira; a IA apoia, mas não substitui, o trabalho humano no SOC.
- e. Incorreta: as duas asserções são verdadeiras e relacionadas.

**Questão 21** (correta: b)
- a. Incorreta: somar as 10 regras pressupõe que todas funcionaram, mas 2 não dispararam no reteste; regra não retestada (ou reprovada) é apenas hipótese.
- b. Correta: cobertura testada = (12 detecções iniciais + 8 regras aprovadas no reteste) ÷ 40 = 20 ÷ 40 = 50%.
- c. Incorreta: regras criadas e retestadas na própria sessão já contam, como no exemplo da Aula 13 (de 30% para 50% no reteste).
- d. Incorreta: o cálculo ignora as 12 técnicas que já geravam alerta desde a primeira execução.
- e. Incorreta: 45% corresponderia a 18 técnicas; o total comprovado é 12 + 8 = 20.

**Questão 22** (correta: e)
- a. Incorreta: técnicas cobertas continuam sendo testadas em ciclos futuros, e uma regra só conta como cobertura depois de retestada.
- b. Incorreta: a leitura está invertida — B já tem telemetria e precisa de regra; C não tem telemetria e precisa primeiro de uma fonte de registros.
- c. Incorreta: executar a técnica não significa detectá-la; B e C não geraram alerta.
- d. Incorreta: aceitar risco residual é decisão da liderança para o que resta após os ajustes, e não a primeira reação a uma lacuna.
- e. Correta: sem alerta mas com telemetria (B), ajusta-se a regra; sem telemetria (C), habilita-se a fonte de registros; em ambos os casos, o reteste comprova a melhoria.

**Questão 23** (correta: a)
- a. Correta: a defesa informada por ameaças prioriza o comportamento de grupos que realmente atacam o setor da organização, usando CTI para montar o plano de emulação.
- b. Incorreta: testar técnicas aleatórias desperdiça o tempo limitado e ignora as ameaças relevantes; o objetivo não é cobrir toda a matriz.
- c. Incorreta: a automação aumenta a frequência dos testes, mas não substitui operadores e analistas experientes.
- d. Incorreta: a escolha do adversário deve considerar o setor da organização; para um banco, faz sentido emular grupos com histórico no setor financeiro.
- e. Incorreta: no *purple teaming*, o Blue Team sabe o que será executado; ocultar a execução descreve um exercício de Red Team tradicional.

**Questão 24** (correta: d)
- a. Incorreta: o ATT&CK Navigator serve para visualizar cobertura e planos sobre a matriz, não para executar testes.
- b. Incorreta: a *Adversary Emulation Library* fornece planos completos baseados em grupos, e não testes pequenos e isolados por técnica.
- c. Incorreta: o Caldera automatiza a emulação de adversários em campanhas; para validar rapidamente uma regra, a biblioteca de testes atômicos é mais direta.
- d. Correta: o Atomic Red Team, da Red Canary, é uma biblioteca de testes pequenos, cada um mapeado a uma técnica ATT&CK, ideal para validar uma regra específica em laboratório autorizado.
- e. Incorreta: o DeTT&CT é um *framework* para pontuar visibilidade e detecção, e não uma ferramenta para executar técnicas.

**Questão 25** (correta: c)
- a. Incorreta: executar sem avisar contraria a lógica transparente do *purple teaming* e não resolveria a falta de condução.
- b. Incorreta: o problema não foi o tamanho do plano, mas a ausência de condução e de encaminhamentos concretos.
- c. Correta: segundo o PTEF, o facilitador conduz a sessão, controla o tempo e garante que as discussões terminem em tarefas concretas — exatamente o que faltou.
- d. Incorreta: plataformas de BAS automatizam testes, mas não substituem a discussão colaborativa entre as equipes.
- e. Incorreta: atribuir notas de maturidade não é o papel central de uma sessão *purple*; o relato aponta falha de condução e de registro de ações.

**Questão 26** (correta: e)
- a. Incorreta: o valor de setembro está errado; 240 ÷ 800 = 30%, e não 24%.
- b. Incorreta: 85% e 70% são as taxas de falsos positivos (supondo que os demais alertas sejam falsos), e não a precisão.
- c. Incorreta: o valor de setembro está errado; 240 ÷ 800 = 30%.
- d. Incorreta: os valores estão trocados ou mal calculados; março = 300 ÷ 2.000 = 15%.
- e. Correta: precisão = verdadeiros positivos ÷ total de alertas; março = 300 ÷ 2.000 = 15%, setembro = 240 ÷ 800 = 30%.

**Questão 27** (correta: c)
- a. Incorreta: 25% é a razão entre o valor final e o inicial (5 ÷ 20), e não a redução.
- b. Incorreta: 15 é a diferença em horas, não um percentual.
- c. Correta: redução = (20 − 5) ÷ 20 = 15 ÷ 20 = 75%.
- d. Incorreta: 300% resulta de dividir a diferença pelo valor final (15 ÷ 5); a base correta é o valor inicial.
- e. Incorreta: não há base de cálculo que leve a 80%; reveja o exemplo da Aula 14 (de 18 para 4 horas ≈ 78%).

**Questão 28** (correta: b)
- a. Incorreta: 2 horas é a mediana; a média é (9 × 2 + 2.160) ÷ 10 = 217,8 horas.
- b. Correta: a média de cerca de 218 horas é distorcida por um único caso extremo; a mediana de 2 horas mostra o caso típico, e o incidente atípico merece investigação própria.
- c. Incorreta: os conceitos estão trocados; a mediana é o valor central (2 horas) e não é afetada pelo peso do caso extremo.
- d. Incorreta: excluir o caso esconderia uma falha relevante; a recomendação é acompanhar média e mediana e analisar o atípico.
- e. Incorreta: a Aula 14 recomenda acompanhar também a mediana justamente porque a média é sensível a extremos.

**Questão 29** (correta: d)
- a. Incorreta: contar a técnica como coberta só porque existe uma regra é a primeira armadilha da cobertura ATT&CK.
- b. Incorreta: telemetria indica visibilidade (há dados para detectar), não detecção comprovada.
- c. Incorreta: o objetivo é cobrir as técnicas priorizadas pela inteligência de ameaças, e não 100% da matriz.
- d. Correta: cobertura testada = 20 ÷ 50 = 40%; visibilidade = 35 ÷ 50 = 70%; os 90% (45 ÷ 50) refletem apenas regras cadastradas, sem validação.
- e. Incorreta: o denominador da cobertura testada é o total de técnicas priorizadas (50), e não as técnicas com regra.

**Questão 30** (correta: a)
- a. Correta: para a diretoria, interessam tendências e risco; a evolução da cobertura testada frente às técnicas usadas contra o setor comunica progresso real.
- b. Incorreta: volume de alertas não indica se a organização está mais protegida; pode inclusive refletir mais ruído.
- c. Incorreta: a precisão por regra é um indicador detalhado útil à equipe técnica, não à diretoria.
- d. Incorreta: é a métrica de vaidade discutida na Aula 14, que nada diz sobre a capacidade diante de um adversário competente.
- e. Incorreta: o número de regras escritas mede esforço, não resultado; regras não testadas são apenas hipóteses.

**Questão 31** (correta: d)
- a. Incorreta: o segundo valor foi expresso em pontos (24), e não em percentual.
- b. Incorreta: os valores são as pontuações brutas, não os percentuais sobre a pontuação máxima.
- c. Incorreta: 24 ÷ 30 = 80%, e não 70%.
- d. Correta: pontuação máxima = 10 × 3 = 30; primeiro exercício = 15 ÷ 30 = 50%; segundo = 24 ÷ 30 = 80%.
- e. Incorreta: 15 ÷ 30 = 50%, e não 60%.

**Questão 32** (correta: e)
- a. Incorreta: o *cyber range* tem custo médio a alto e público técnico; não é o melhor primeiro passo para envolver a diretoria.
- b. Incorreta: CTFs desenvolvem habilidades técnicas e não testam decisões executivas nem papéis em crise.
- c. Incorreta: uma operação de Red Team não testa diretamente decisões, papéis e comunicação da liderança, e é cara para um primeiro passo.
- d. Incorreta: um plano que nunca foi exercitado é só um documento; a aprovação não comprova a capacidade de resposta.
- e. Correta: o *tabletop* tem baixo custo, envolve técnicos e executivos e testa decisões, papéis e comunicação — exatamente as fragilidades de uma organização que nunca exercitou o plano.

**Questão 33** (correta: c)
- a. Incorreta: o *hot wash* é a conversa imediata ao final do exercício, e não uma informação inserida durante ele.
- b. Incorreta: o relatório pós-ação é o documento final com pontos fortes, lacunas e plano de melhoria.
- c. Correta: o *inject* é uma informação nova inserida ao longo do exercício para forçar decisões, como a ligação de um jornalista.
- d. Incorreta: a *flag* é a sequência de texto que comprova a solução de um desafio em um CTF.
- e. Incorreta: a célula de controle observa e coordena exercícios em *cyber range*; não é o nome do evento inserido no cenário.

**Questão 34** (correta: b)
- a. Incorreta: o *Jeopardy* tem desafios independentes por categoria, sem infraestrutura a defender.
- b. Correta: no CTF de ataque e defesa, cada equipe protege seus serviços vulneráveis enquanto tenta explorar os das outras, o que exige trabalho coordenado.
- c. Incorreta: o *tabletop* é baseado em discussão de cenário, sem execução técnica.
- d. Incorreta: o *hot wash* é a conversa de avaliação imediata após um exercício, não um formato de treinamento.
- e. Incorreta: segundo o SP 800-84, treinamento ensina papéis e procedimentos; não envolve defender e atacar serviços.

**Questão 35** (correta: e)
- a. Incorreta: o *hot wash* é recomendado e complementa o relatório formal.
- b. Incorreta: o relatório pós-ação deve registrar pontos fortes e lacunas, com plano de melhoria.
- c. Incorreta: o *tabletop* é adequado para testar decisões como a notificação à ANPD; o problema não é o formato.
- d. Incorreta: definir objetivos antes do exercício é correto e necessário para a avaliação.
- e. Correta: as ações de melhoria precisam de dono e prazo, devem entrar no mesmo controle do *purple teaming* e ser verificadas no exercício seguinte; sem isso, as lacunas tendem a se repetir.

**Questão 36** (correta: a)
- a. Correta: ALE inicial = 0,20 × 5.000.000 = R$ 1.000.000; nova ALE = 0,10 × 5.000.000 = R$ 500.000; redução = R$ 500.000; ROSI = (500.000 − 250.000) ÷ 250.000 = 100%.
- b. Incorreta: o ROSI subtrai o custo da redução antes de dividir pelo custo; dividir só a redução pelo custo dá 200%.
- c. Incorreta: R$ 500.000 é a nova ALE (após o programa), e não a ALE inicial.
- d. Incorreta: 50% não corresponde à fórmula; reveja ROSI = (redução − custo) ÷ custo.
- e. Incorreta: usar a ALE inicial inteira como redução supõe eliminar todo o risco, o que não corresponde às premissas.

**Questão 37** (correta: c)
- a. Incorreta: o ROSI depende da redução da perda esperada, que muda com a probabilidade final.
- b. Incorreta: a redução (R$ 250.000) iguala o custo, o que leva a ROSI de 0%, e não negativo.
- c. Correta: nova ALE = 0,15 × 5.000.000 = R$ 750.000; redução = R$ 250.000; ROSI = (250.000 − 250.000) ÷ 250.000 = 0%. O cenário mostra como as premissas mudam a conclusão.
- d. Incorreta: uma probabilidade final maior significa menor redução de perda e, portanto, ROSI menor.
- e. Incorreta: o ROSI se aplica a qualquer redução estimada; não exige eliminar o risco.

**Questão 38** (correta: d)
- a. Incorreta: o programa contínuo combina atividades complementares; ciclos *purple* frequentes e Red Team anual têm objetivos diferentes.
- b. Incorreta: *tabletops* testam decisões e comunicação, algo que varreduras não avaliam.
- c. Incorreta: o patrocínio executivo é um dos requisitos de um programa contínuo, segundo a função Governar do NIST CSF 2.0.
- d. Correta: a gestão de achados precisa de dono, prazo e reteste integrados à gestão de riscos, e os relatórios à liderança devem usar linguagem de risco e de negócio.
- e. Incorreta: detalhamento técnico de CVEs interessa à equipe técnica; à diretoria interessam tendências e risco.

**Questão 39** (correta: e)
- a. Incorreta: o *pentester* realiza testes de invasão em escopo definido, e não a criação e manutenção de regras.
- b. Incorreta: o operador de Red Team emula adversários; quem cria as detecções é o lado defensivo.
- c. Incorreta: a resposta a incidentes foca contenção, investigação e recuperação.
- d. Incorreta: o analista de SOC faz triagem e investigação de alertas; criar, testar e manter regras é tarefa do engenheiro de detecção.
- e. Correta: o engenheiro de detecção cria, testa e mantém regras de detecção, inclusive reduzindo falsos positivos — exatamente o perfil descrito.

**Questão 40** (correta: b)
- a. Incorreta: o *Zero Trust* elimina a confiança implícita na rede interna; focar apenas no perímetro contraria o modelo.
- b. Correta: com a nuvem, configurações, identidades e APIs passam a compor a superfície de ataque, e a matriz ATT&CK tem seção específica para isso; no *Zero Trust*, o abuso de credenciais válidas é prioritário.
- c. Incorreta: nenhum controle elimina o risco de abuso de credenciais; o *Zero Trust* torna esses testes ainda mais importantes.
- d. Incorreta: o ATLAS trata de ataques contra sistemas de IA e não substitui a seção de nuvem do ATT&CK.
- e. Incorreta: as ferramentas de IA erram e exigem supervisão humana; elas apoiam, mas não substituem, os analistas.
