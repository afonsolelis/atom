# Questionário — Unidade 2

Disciplina: Red Team & Blue Team Strategies  
Professor-conteudista: Afonso Cesar Lelis Brandão  
Template de origem: `documentos/Unidade 2/40 Questões - UNI2_nomedadisciplina.docx`

Quantidade obrigatória: 40 questões padrão ENADE — 20 de asserção-razão (1 a 20) e 20 de interpretação (21 a 40).
Cinco alternativas por questão (a–e); a correta é marcada com `*` imediatamente antes da letra.
Feedback para **cada alternativa** (por que está correta ou qual o equívoco), todos ao final do documento.

## Questões

### Asserção-razão

**1.** I. O reconhecimento passivo, baseado em fontes de terceiros como bases de transparência de certificados e buscadores de dispositivos expostos, praticamente não deixa rastro no ambiente da organização-alvo.

PORQUE

II. No reconhecimento passivo, a equipe não interage diretamente com os sistemas da organização-alvo, limitando-se a consultar informações já publicadas ou coletadas por terceiros.

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**2.** I. Em um engajamento de Red Team, varreduras de portas contra os servidores de uma empresa só podem ser realizadas sobre ativos incluídos no escopo autorizado.

PORQUE

II. A varredura de portas é uma técnica de reconhecimento passivo, pois apenas consulta informações que os servidores já disponibilizam publicamente, sem interação direta com eles.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**3.** I. Como as informações publicadas em redes sociais profissionais são públicas, a coleta de nomes, cargos e endereços de *e-mail* de funcionários durante o OSINT dispensa qualquer previsão nas regras de engajamento e não está sujeita à LGPD.

PORQUE

II. Nomes, cargos e endereços de *e-mail* associados a pessoas identificáveis são dados pessoais.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**4.** I. A descoberta de ativos de *shadow IT*, como um ambiente de testes antigo em nuvem que a área de TI desconhecia, costuma ser um dos resultados mais valiosos da fase de reconhecimento.

PORQUE

II. Na matriz MITRE ATT&CK, o reconhecimento corresponde à tática identificada como TA0043.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**5.** I. Se, durante o OSINT, o Red Team encontrar o servidor de um fornecedor que não consta no escopo, poderá acessá-lo livremente sempre que a falha identificada for grave, já que o achado beneficia o cliente.

PORQUE

II. No Brasil, o acesso a sistemas fora do escopo autorizado não tem repercussão penal quando a intenção do profissional é ajudar a organização.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

**6.** I. Uma vulnerabilidade com nota-base CVSS 9,8 é classificada, na escala qualitativa do CVSS, como de severidade crítica.

PORQUE

II. A nota-base do CVSS expressa o risco que a falha representa para a organização, pois já incorpora a existência de exploração no mundo real e a criticidade do ativo afetado.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**7.** I. Uma vulnerabilidade presente no catálogo KEV, em um portal exposto à internet, pode ser priorizada à frente de outra com nota CVSS mais alta localizada em um servidor interno isolado.

PORQUE

II. O catálogo KEV reúne vulnerabilidades com exploração confirmada, o que, somado à exposição do ativo, eleva o risco real além do que a severidade técnica isolada indica.

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**8.** I. O EPSS, mantido pela CISA, informa se uma vulnerabilidade já teve exploração confirmada no mundo real, funcionando como uma lista oficial de falhas exploradas.

PORQUE

II. O EPSS estima a probabilidade de que uma vulnerabilidade seja explorada nos 30 dias seguintes, com base em dados observados de atividade de exploração.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**9.** I. Os resultados de um *scanner* de vulnerabilidades precisam ser validados antes de serem tratados como achados comprovados em um relatório.

PORQUE

II. O programa CVE é coordenado pela MITRE, e a NVD, mantida pelo NIST, enriquece os registros com informações de severidade e produtos afetados.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**10.** I. A gestão de vulnerabilidades é um projeto pontual, que se encerra quando o *scanner* deixa de apontar falhas críticas no ambiente.

PORQUE

II. O NIST SP 800-40 Rev. 4 recomenda tratar a aplicação de correções como reação imediata a cada alerta, sem necessidade de planejamento prévio.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

**11.** I. Uma mensagem de *phishing* com o texto "Sua conta será bloqueada em 1 hora" busca reduzir a análise crítica do destinatário antes de ele agir.

PORQUE

II. O princípio de urgência e escassez pressiona a vítima a agir rapidamente, antes de verificar a legitimidade do pedido.

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**12.** I. Em uma simulação de *phishing* ética, o colaborador que clica na mensagem deve receber orientação imediata, e não punição.

PORQUE

II. Para medir com precisão o risco, a simulação deve armazenar as senhas reais digitadas pelos colaboradores no formulário simulado.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**13.** I. Em uma simulação de *phishing*, a taxa de clique é a única métrica relevante, e a taxa de reporte tem importância secundária para o Blue Team.

PORQUE

II. Um reporte isolado tem pouco valor para o SOC, pois uma mensagem maliciosa só pode ser bloqueada depois que todos os destinatários a reportam.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

**14.** I. As regras de engajamento de simulações de *phishing* costumam vetar pretextos envolvendo demissões, saúde, salários ou tragédias.

PORQUE

II. Na matriz MITRE ATT&CK, o *phishing* aparece como técnica de acesso inicial (T1566), com subtécnicas como anexo malicioso e *link* malicioso.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**15.** I. Uma campanha de simulação com taxa de clique de apenas 2% comprova, por si só, que os colaboradores estão preparados, independentemente da dificuldade da mensagem utilizada.

PORQUE

II. A *Phish Scale*, proposta pelo NIST, classifica a dificuldade de uma mensagem de *phishing* conforme as pistas que ela contém e o quanto o contexto se aproxima da rotina do público.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**16.** I. O uso de contas válidas (T1078 — *Valid Accounts*) por um adversário tende a dificultar a detecção pelo Blue Team.

PORQUE

II. Com uma credencial legítima, as ações do adversário se misturam às dos usuários e administradores legítimos do ambiente.

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**17.** I. Em um engajamento de Red Team, o impacto costuma ser demonstrado, e não executado: em vez de exfiltrar uma base de clientes, a equipe registra evidência de que teria acesso a ela.

PORQUE

II. Persistências e contas criadas pelo Red Team devem permanecer no ambiente após o fim da operação, para que o Blue Team possa estudá-las quando quiser.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**18.** I. O acesso inicial costuma ser o objetivo final de uma operação adversária, razão pela qual a pós-exploração tem pouca relevância em um exercício de Red Team.

PORQUE

II. Na matriz MITRE ATT&CK, a pós-exploração abrange táticas como persistência, escalada de privilégios, acesso a credenciais, descoberta, movimentação lateral e comando e controle.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**19.** I. Na análise de caminhos de ataque em um Active Directory, corrigir uma única relação mal configurada elimina no máximo um caminho, por isso a defesa deve tratar as permissões sempre como uma lista, item a item.

PORQUE

II. O BloodHound representa as permissões do domínio como uma tabela plana, sem considerar relações entre usuários, computadores e grupos.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

**20.** I. O relatório de Red Team deve conter uma linha do tempo detalhada das ações executadas, para que o Blue Team possa compará-la com o que os registros do ambiente mostram.

PORQUE

II. O Mimikatz (S0002) tornou-se símbolo do acesso a credenciais em ambientes Windows, e sua presença é um dos comportamentos mais monitorados por soluções de EDR.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Interpretação

**21.** Em um engajamento autorizado na varejista fictícia LojaNorte, o Red Team identificou 240 subdomínios em bases de transparência de certificados. Desses, 160 ainda respondem na internet. Ao comparar os que respondem com o inventário oficial, a equipe constatou que 24 não constavam em nenhum registro da TI. Qual é a taxa de ativos desconhecidos em relação à superfície ativa?

a. 10%.
*b. 15%.
c. 66,7%.
d. 24%.
e. 85%.

**22.** Na mesma operação da LojaNorte, que tem 500 funcionários, a equipe encontrou 340 endereços de *e-mail* corporativos válidos em fontes públicas. Que percentual do quadro está exposto como possível alvo de *phishing*?

a. 32%.
b. 34%.
c. 47%.
*d. 68%.
e. 74%.

**23.** Durante o reconhecimento de uma empresa fictícia, autorizado em contrato, o Red Team realizou as seguintes atividades:

1. consulta a uma base de transparência de certificados;
2. pesquisa em um buscador de dispositivos expostos, como o Shodan;
3. varredura de portas no endereço IP do *site* institucional;
4. leitura de vagas de emprego publicadas em uma rede social profissional;
5. grande volume de consultas aos servidores DNS da empresa por subdomínios inexistentes.

Quais atividades tendem a deixar rastro nos registros do ambiente da própria empresa, podendo ser percebidas pelo Blue Team?

*a. 3 e 5, apenas.
b. 1, 2 e 4, apenas.
c. 1 e 3, apenas.
d. 2, 3 e 5, apenas.
e. 4 e 5, apenas.

**24.** Em um engajamento autorizado para a Alfa Seguros (empresa fictícia), o OSINT revela um painel de administração publicado por uma agência de *marketing* terceirizada, hospedado em servidor da própria agência. O ativo não consta no inventário da Alfa e não está listado no escopo. Qual é a conduta adequada do Red Team?

a. Testar rapidamente se o painel aceita credenciais padrão, já que o ativo está ligado ao nome do cliente e o teste seria breve.
b. Executar apenas uma varredura de vulnerabilidades no servidor da agência, pois a varredura não altera dados e, portanto, não exige autorização.
c. Ignorar o achado e não mencioná-lo no relatório, pois tudo o que está fora do escopo deve ser descartado sem registro.
d. Publicar o achado em um canal aberto, para pressionar a agência a corrigir o problema o quanto antes.
*e. Registrar o achado sem acessar o painel e comunicá-lo ao ponto de contato do cliente, para revisão do inventário e, se for o caso, do escopo.

**25.** Ao analisar perfis em uma rede social profissional, o Red Team de um engajamento autorizado montou uma lista de nomes de funcionários do setor financeiro, confirmou endereços de *e-mail* válidos e deduziu o padrão de formação desses endereços. Com base na tabela de fontes de OSINT estudada, qual técnica ATT&CK descreve mais diretamente essa coleta?

a. T1595 — *Active Scanning*.
b. T1566 — *Phishing*.
*c. T1589 — *Gather Victim Identity Information*.
d. T1046 — *Network Service Discovery*.
e. T1078 — *Valid Accounts*.

**26.** A equipe de segurança da Beta Logística (empresa fictícia) recebeu a seguinte tabela, com valores ilustrativos:

| Vulnerabilidade | CVSS | EPSS | No KEV? | Ativo |
|---|---|---|---|---|
| D | 9,1 | 0,01 (1%) | Não | Servidor de testes interno isolado |
| E | 8,1 | 0,93 (93%) | Sim | *Gateway* de VPN exposto à internet |
| F | 6,5 | 0,35 (35%) | Não | Intranet corporativa |
| G | 9,8 | 0,05 (5%) | Não | Estação de laboratório desconectada da rede |

Considerando a priorização por risco, qual vulnerabilidade deve ser tratada primeiro e por quê?

*a. E, porque combina exploração confirmada, alta probabilidade de exploração e ativo exposto à internet.
b. G, porque tem a maior nota CVSS e, portanto, representa o maior risco para a empresa.
c. D, porque é crítica pelo CVSS e está em um servidor, que é mais importante que uma estação.
d. F, porque está na intranet, que concentra a maior parte dos usuários da empresa.
e. D e G empatadas, porque ambas estão na faixa crítica do CVSS e o EPSS não altera a ordem.

**27.** Uma equipe consegue corrigir 120 vulnerabilidades por semana e recebeu um relatório com 1.500 achados, dos quais 600 têm CVSS ≥ 7,0. Depois de filtrar apenas as falhas no KEV ou com EPSS ≥ 10% em ativos expostos, restaram 48 achados. Quanto tempo a equipe levaria para tratar, respectivamente, a fila de CVSS ≥ 7,0 e a fila filtrada por risco?

a. 12,5 semanas e 0,4 semana.
b. 5 semanas e 4 semanas.
c. 4 semanas e 0,5 semana.
d. 5 semanas e 2,5 semanas.
*e. 5 semanas e 0,4 semana.

**28.** Um relatório de *scanner* lista quatro CVEs com as seguintes notas-base CVSS: 3,9; 4,0; 7,0; e 9,0. Qual alternativa apresenta corretamente a severidade qualitativa de cada uma, na ordem dada?

a. Baixa, baixa, alta e alta.
*b. Baixa, média, alta e crítica.
c. Média, média, alta e crítica.
d. Baixa, média, média e alta.
e. Nenhuma, baixa, média e alta.

**29.** Em um exercício autorizado na Gama Energia (empresa fictícia), o Red Team executou duas varreduras: uma rápida e ampla, que gerou alertas imediatos no sistema de detecção de intrusão, e outra lenta e seletiva, distribuída ao longo de dois dias, que não gerou nenhum alerta. Qual interpretação é a mais adequada para o Blue Team?

a. O Red Team violou as regras de engajamento, pois varreduras lentas não são permitidas em exercícios que testam a detecção.
b. A segunda varredura não deixou nenhum rastro nos registros, já que varreduras lentas não produzem conexões registráveis.
c. O sistema de detecção é suficiente, pois detectou pelo menos uma das varreduras e, portanto, cumpre seu papel.
*d. A detecção percebe varreduras barulhentas, mas não as discretas, o que indica uma lacuna a ser tratada pela defesa.
e. O resultado mostra que a enumeração interna é mais ruidosa que a varredura externa, por isso deve ser priorizada.

**30.** A política de correção da Delta Saúde (empresa fictícia) define: falhas no KEV em ativos expostos à internet — 7 dias, independentemente do CVSS; demais falhas altas (7,0–8,9) — 30 dias; demais falhas médias (4,0–6,9) — 90 dias. Foram identificadas duas falhas: H, com CVSS 7,8, fora do KEV, em um servidor interno; e I, com CVSS 6,1, presente no KEV, em um portal exposto à internet. Quais são os prazos de correção de H e de I, respectivamente?

a. 7 dias e 90 dias.
b. 30 dias e 90 dias.
*c. 30 dias e 7 dias.
d. 7 dias e 7 dias.
e. 90 dias e 30 dias.

**31.** Uma campanha autorizada de simulação de *phishing* enviou 2.000 mensagens e obteve 260 cliques, 80 submissões de dados no formulário simulado e 390 reportes. Quais são, respectivamente, a taxa de clique, a taxa de reporte e a razão entre reportes e cliques?

a. 13%, 4% e 0,67.
b. 26%, 19,5% e 1,5.
c. 13%, 19,5% e 0,67.
d. 4%, 13% e 3,0.
*e. 13%, 19,5% e 1,5.

**32.** Em uma simulação autorizada, a mensagem enviada aos colaboradores dizia: "Todos os colegas do seu setor já confirmaram a adesão ao novo benefício. Falta apenas você." Qual princípio de persuasão de Cialdini é explorado de forma predominante?

*a. Aprovação social.
b. Autoridade.
c. Reciprocidade.
d. Compromisso e coerência.
e. Afeição.

**33.** A diretoria de uma rede varejista fictícia pede ao Red Team uma simulação de *phishing* com o tema "lista de demissões do próximo mês" e quer receber a lista nominal de quem clicar, para aplicar advertências. Qual resposta do Red Team está alinhada às práticas de simulação ética estudadas?

a. Aceitar o tema, pois pretextos mais impactantes geram números mais realistas, e entregar a lista nominal, já que a diretoria é a contratante.
b. Aceitar o tema, mas entregar a lista nominal apenas ao RH, que fica responsável por decidir as advertências aplicáveis a cada pessoa.
*c. Propor um pretexto plausível e não danoso, alinhar com RH, jurídico e DPO e apresentar métricas agregadas, com orientação a quem clicar.
d. Recusar a simulação, pois campanhas de *phishing* contra os próprios colaboradores são vedadas pela LGPD em qualquer circunstância.
e. Substituir a simulação por uma varredura de portas, que mede o mesmo risco sem envolver as pessoas da organização.

**34.** Em uma semana, a central de segurança de uma empresa fictícia registrou três episódios: (1) uma ligação de alguém que se apresentou como suporte técnico e pediu o código de segundo fator de um analista; (2) uma mensagem SMS com *link* para "regularizar o vale-refeição"; (3) uma pessoa sem crachá que entrou no prédio logo atrás de um funcionário. Quais vetores de engenharia social correspondem, respectivamente, aos episódios?

a. *Smishing*, *vishing* e *pretexting*.
b. *Vishing*, *phishing* por anexo e *Business Email Compromise*.
c. *Pretexting*, *smishing* e *vishing*.
*d. *Vishing*, *smishing* e *tailgating*.
e. *Tailgating*, *smishing* e *vishing*.

**35.** Após uma campanha autorizada de simulação, o SOC da Épsilon Tech (empresa fictícia) reuniu as seguintes observações: o domínio remetente fora registrado dois dias antes e era parecido com o da empresa; as verificações SPF, DKIM e DMARC falharam; o *proxy* registrou os cliques na página simulada; e o primeiro reporte de um colaborador chegou em 6 minutos. Qual interpretação está correta?

a. Apenas os rastros técnicos têm valor para a defesa, pois reportes de colaboradores são subjetivos e não permitem nenhuma ação do SOC.
*b. Os rastros técnicos e o reporte rápido, um rastro humano, permitem ao SOC bloquear a mensagem e identificar quem acessou a página.
c. A falha nas verificações SPF, DKIM e DMARC comprova que a mensagem foi enviada de dentro da rede corporativa da empresa.
d. O registro dos cliques no *proxy* torna desnecessário medir a taxa de reporte e o tempo até o primeiro reporte nas próximas campanhas.
e. Um domínio recém-registrado e parecido com o da empresa não é indício relevante, pois domínios novos são comuns e legítimos.

**36.** Em um domínio Active Directory com 8.000 contas de usuário, a análise de grafo mostrou que 2.000 delas tinham algum caminho até o grupo *Domain Admins*. Após a correção de três pontos de passagem, restaram 64 contas com caminho. Quais são, respectivamente, o percentual inicial de contas com caminho, o percentual final e a redução aproximada dos caminhos?

a. 20%, 0,8% e 96,8%.
b. 25%, 3,2% e 87%.
c. 25%, 0,8% e 3,2%.
d. 2,5%, 0,08% e 96,8%.
*e. 25%, 0,8% e 96,8%.

**37.** O relatório de uma operação autorizada de Red Team informa que, das 15 técnicas executadas, o SOC detectou 6. Qual é a taxa de detecção e como esse dado deve ser tratado no relatório?

a. 60%, e o número deve ser omitido do sumário executivo para não expor a equipe de defesa à diretoria.
*b. 40%, e as técnicas não detectadas devem ser destacadas como ponto de partida para a melhoria da detecção.
c. 6%, e o dado indica que o SOC precisa ser substituído por um serviço terceirizado de monitoramento.
d. 40%, e o dado dispensa recomendações, pois o objetivo do relatório é apenas registrar o desempenho do Red Team.
e. 60%, e as técnicas detectadas devem ser removidas dos próximos exercícios, já que a defesa as cobre.

**38.** Um trecho da linha do tempo de um relatório de Red Team registra os seguintes rastros observados pelo Blue Team: (1) acessos incomuns ao processo LSASS em uma estação; (2) *logons* remotos fora do padrão, da estação para dois servidores; (3) conexões periódicas (*beaconing*) a um domínio raro. A quais táticas ATT&CK esses rastros correspondem, respectivamente?

*a. Acesso a credenciais, movimentação lateral e comando e controle.
b. Persistência, descoberta e acesso a credenciais.
c. Escalada de privilégios, persistência e movimentação lateral.
d. Acesso a credenciais, descoberta e persistência.
e. Descoberta, comando e controle e movimentação lateral.

**39.** O seguinte trecho foi extraído de um relatório de Red Team: "Das 12 técnicas executadas, 4 foram detectadas. O acesso à memória do LSASS gerou alerta no EDR 40 minutos após a execução; a movimentação lateral para os servidores de arquivos não foi percebida." Em qual seção da estrutura de relatório estudada esse trecho se encaixa melhor?

a. Sumário executivo.
b. Narrativa do ataque.
*c. Análise de detecção e resposta.
d. Recomendações priorizadas.
e. Escopo e regras de engajamento.

**40.** Em uma operação autorizada, o Red Team chegou da estação de um analista ao controlador de domínio usando a credencial de um administrador que utilizava a mesma conta para ler *e-mails* e administrar servidores, sem segundo fator de autenticação. Qual recomendação ataca mais diretamente a causa desse caminho?

a. Elevar o limite de CVSS usado na priorização de correções, para que mais falhas sejam tratadas a cada semana.
b. Ampliar as simulações de *phishing*, pois o problema foi exclusivamente o comportamento do analista comprometido.
c. Bloquear o uso de ferramentas de varredura na rede, já que a movimentação lateral depende de varreduras de portas.
*d. Separar contas administrativas das de uso diário, exigir segundo fator e adotar acesso privilegiado sob demanda.
e. Reescrever o relatório sem a narrativa do ataque, para evitar que o caminho fique documentado internamente.

## Gabarito e feedbacks

**Questão 1** (correta: a)
- a. Correta: o reconhecimento passivo quase não deixa rastro (I) justamente porque não há interação direta com os sistemas do alvo, apenas consulta a fontes de terceiros (II); a II explica a I.
- b. Incorreta: a II não é apenas verdadeira, ela é a causa do baixo rastro descrito na I. Revise a diferença entre reconhecimento passivo e ativo.
- c. Incorreta: a II é verdadeira; é exatamente a definição de reconhecimento passivo apresentada na Aula 5.
- d. Incorreta: a I é verdadeira; a defesa nessa fase é sobretudo preventiva porque o passivo praticamente não aparece nos registros do alvo.
- e. Incorreta: ambas as asserções são verdadeiras. Revise a seção "Reconhecimento passivo e ativo".

**Questão 2** (correta: c)
- a. Incorreta: a II é falsa, logo não pode justificar a I.
- b. Incorreta: a II é falsa — a varredura de portas é reconhecimento ativo (T1595 — *Active Scanning*).
- c. Correta: a I é verdadeira, pois o reconhecimento ativo toca ativos que precisam estar no escopo; a II é falsa, pois a varredura interage diretamente com os servidores e pode ser registrada.
- d. Incorreta: a I é verdadeira; o primeiro motivo apontado na aula para distinguir passivo e ativo é justamente jurídico — o ativo exige escopo autorizado.
- e. Incorreta: a I é verdadeira. Revise os limites jurídicos do reconhecimento ativo.

**Questão 3** (correta: d)
- a. Incorreta: a I é falsa; "informação pública" não significa "informação sem regras".
- b. Incorreta: a alternativa considera a I verdadeira, mas ela é falsa; a coleta de dados de funcionários exige previsão nas regras de engajamento e está sujeita à LGPD.
- c. Incorreta: a I é falsa e a II é verdadeira — a combinação é a inversa.
- d. Correta: a I é falsa, pois as regras de engajamento devem prever a coleta de dados de funcionários e a LGPD se aplica; a II é verdadeira, pois nomes, cargos e *e-mails* são dados pessoais.
- e. Incorreta: a II é verdadeira. Revise "Limites éticos e legais do OSINT".

**Questão 4** (correta: b)
- a. Incorreta: o código TA0043 apenas identifica a tática; ele não explica por que o *shadow IT* é um achado valioso.
- b. Correta: ambas são verdadeiras — o *shadow IT* revela ativos que ninguém protege nem monitora, e o reconhecimento é a tática TA0043 —, mas a II não justifica a I.
- c. Incorreta: a II é verdadeira; o reconhecimento é a tática TA0043 do ATT&CK.
- d. Incorreta: a I é verdadeira; encontrar *shadow IT* é, muitas vezes, o resultado mais valioso do reconhecimento.
- e. Incorreta: ambas são verdadeiras. Revise "Superfície de ataque e *shadow IT*".

**Questão 5** (correta: e)
- a. Incorreta: as duas asserções são falsas; a gravidade da falha não autoriza o acesso fora do escopo.
- b. Incorreta: nenhuma das asserções é verdadeira.
- c. Incorreta: a I é falsa — o escopo define o que pode ser tocado, independentemente da gravidade do achado.
- d. Incorreta: a II é falsa — acessar sistemas fora do escopo pode configurar o crime do art. 154-A do Código Penal.
- e. Correta: a I é falsa, pois ativos fora do escopo não podem ser acessados; a II é falsa, pois a intenção não afasta a possível tipificação penal da invasão de dispositivo.

**Questão 6** (correta: c)
- a. Incorreta: a II é falsa, logo não justifica a I.
- b. Incorreta: a II é falsa — a nota-base mede severidade técnica, não risco.
- c. Correta: a I é verdadeira (9,0–10,0 é crítica); a II é falsa, pois o CVSS-base não indica se a falha está sendo explorada nem se o ativo é crítico para o negócio.
- d. Incorreta: a I é verdadeira; 9,8 está na faixa crítica.
- e. Incorreta: a I é verdadeira. Revise a tabela de faixas do CVSS e o "ponto de atenção" da Aula 6.

**Questão 7** (correta: a)
- a. Correta: ambas são verdadeiras, e a exploração confirmada (KEV) somada à exposição do ativo é exatamente o que torna a falha mais urgente que outra de CVSS maior em ativo isolado.
- b. Incorreta: a II é a razão da priorização descrita na I, logo a justifica.
- c. Incorreta: a II é verdadeira; o KEV lista vulnerabilidades com exploração confirmada.
- d. Incorreta: a I é verdadeira; é o caso da vulnerabilidade B do exemplo numérico da aula.
- e. Incorreta: ambas são verdadeiras. Revise o exemplo "CVSS ou EPSS?".

**Questão 8** (correta: d)
- a. Incorreta: a I é falsa; o EPSS é do FIRST e é probabilístico.
- b. Incorreta: a I é falsa.
- c. Incorreta: a combinação é a inversa — a I é falsa e a II é verdadeira.
- d. Correta: a I confunde EPSS com o catálogo KEV da CISA; a II descreve corretamente o EPSS como estimativa de probabilidade de exploração em 30 dias.
- e. Incorreta: a II é verdadeira. Revise "EPSS e KEV: a falha está sendo explorada?".

**Questão 9** (correta: b)
- a. Incorreta: a governança do CVE e da NVD não explica a necessidade de validação; o motivo é que *scanners* geram falsos positivos e não comprovam a explorabilidade.
- b. Correta: ambas são verdadeiras, mas a II trata de quem mantém o CVE e a NVD, e não da razão para validar resultados de *scanner*.
- c. Incorreta: a II é verdadeira; MITRE coordena o CVE e o NIST mantém a NVD.
- d. Incorreta: a I é verdadeira; resultados de *scanner* precisam de validação.
- e. Incorreta: ambas são verdadeiras. Revise "Varredura e enumeração" e "CVE: dando nome às falhas".

**Questão 10** (correta: e)
- a. Incorreta: as duas asserções são falsas.
- b. Incorreta: nenhuma das asserções é verdadeira.
- c. Incorreta: a I é falsa — a gestão de vulnerabilidades é um ciclo contínuo.
- d. Incorreta: a II é falsa — o SP 800-40 Rev. 4 trata a correção como manutenção preventiva planejada.
- e. Correta: a I é falsa, pois o processo é cíclico (inventariar, identificar, priorizar, corrigir, verificar, reportar); a II é falsa, pois o NIST recomenda planejamento, e não reação a cada alerta.

**Questão 11** (correta: a)
- a. Correta: a mensagem da I aplica o princípio de urgência e escassez, e a II explica o mecanismo — pressionar a ação antes da verificação.
- b. Incorreta: a II é justamente o mecanismo que explica a I.
- c. Incorreta: a II é verdadeira; descreve o princípio de urgência e escassez.
- d. Incorreta: a I é verdadeira; o exemplo consta da tabela de princípios da Aula 7.
- e. Incorreta: ambas são verdadeiras. Revise os princípios de Cialdini.

**Questão 12** (correta: c)
- a. Incorreta: a II é falsa, logo não justifica a I.
- b. Incorreta: a II é falsa — nenhuma senha real deve ser armazenada.
- c. Correta: a I é verdadeira (finalidade educativa); a II é falsa, pois a proteção de dados exige que nenhuma senha real seja armazenada, conforme a LGPD.
- d. Incorreta: a I é verdadeira; quem clica recebe orientação, e não punição.
- e. Incorreta: a I é verdadeira. Revise os requisitos de uma simulação ética.

**Questão 13** (correta: e)
- a. Incorreta: as duas asserções são falsas.
- b. Incorreta: nenhuma das asserções é verdadeira.
- c. Incorreta: a I é falsa — a taxa de reporte é a métrica que mais interessa ao Blue Team.
- d. Incorreta: a II é falsa — um único reporte rápido permite ao SOC bloquear a mensagem para toda a empresa.
- e. Correta: a I é falsa, pois reporte e tempo até o primeiro reporte medem a detecção humana; a II é falsa, pois basta um reporte rápido para o SOC agir.

**Questão 14** (correta: b)
- a. Incorreta: o código T1566 não explica por que certos pretextos são vetados; o motivo é o dano real que temas sensíveis podem causar.
- b. Correta: ambas são verdadeiras, mas a classificação ATT&CK do *phishing* não justifica o veto a pretextos danosos.
- c. Incorreta: a II é verdadeira; T1566 é técnica de acesso inicial, com subtécnicas T1566.001 e T1566.002.
- d. Incorreta: a I é verdadeira; os limites de pretexto constam das regras de engajamento.
- e. Incorreta: ambas são verdadeiras. Revise "Simulações de *phishing* autorizadas".

**Questão 15** (correta: d)
- a. Incorreta: a I é falsa.
- b. Incorreta: a I é falsa; uma taxa baixa pode refletir uma isca fácil demais.
- c. Incorreta: a combinação é a inversa.
- d. Correta: a I é falsa, pois uma isca fácil gera números enganosamente bons; a II é verdadeira e descreve a *Phish Scale* do NIST.
- e. Incorreta: a II é verdadeira. Revise o papel da dificuldade da mensagem na interpretação das métricas.

**Questão 16** (correta: a)
- a. Correta: o uso de contas válidas dificulta a detecção (I) porque as ações se confundem com as de usuários legítimos (II).
- b. Incorreta: a II é a explicação direta da I.
- c. Incorreta: a II é verdadeira; é o motivo apresentado na aula.
- d. Incorreta: a I é verdadeira; por isso a proteção de contas privilegiadas é recomendação frequente.
- e. Incorreta: ambas são verdadeiras. Revise "Credenciais válidas: o atalho preferido".

**Questão 17** (correta: c)
- a. Incorreta: a II é falsa.
- b. Incorreta: a II é falsa — persistências e contas devem ser removidas na limpeza pós-operação.
- c. Correta: a I é verdadeira (impacto demonstrado, não executado); a II é falsa, pois tudo o que o Red Team criou deve ser removido, com registro do que foi feito.
- d. Incorreta: a I é verdadeira.
- e. Incorreta: a I é verdadeira. Revise "Limites da pós-exploração em um engajamento".

**Questão 18** (correta: d)
- a. Incorreta: a I é falsa.
- b. Incorreta: a I é falsa; o acesso inicial raramente é o objetivo final.
- c. Incorreta: a combinação é a inversa.
- d. Correta: a I é falsa, pois é a pós-exploração que transforma o ponto de apoio em impacto; a II é verdadeira e lista as táticas ATT&CK dessa fase.
- e. Incorreta: a II é verdadeira. Revise a tabela "As etapas da pós-exploração".

**Questão 19** (correta: e)
- a. Incorreta: as duas asserções são falsas.
- b. Incorreta: nenhuma das asserções é verdadeira.
- c. Incorreta: a I é falsa — eliminar uma relação mal configurada pode cortar dezenas de caminhos.
- d. Incorreta: a II é falsa — o BloodHound representa as relações como grafo.
- e. Correta: a I é falsa, pois o pensamento em grafos mostra pontos de passagem comuns a muitos caminhos; a II é falsa, pois o BloodHound modela relações entre usuários, computadores e grupos.

**Questão 20** (correta: b)
- a. Incorreta: o Mimikatz não explica por que o relatório precisa de linha do tempo; o motivo é permitir a comparação com os registros.
- b. Correta: ambas são verdadeiras, mas a II trata de uma ferramenta de acesso a credenciais, sem relação de causa com a estrutura do relatório.
- c. Incorreta: a II é verdadeira; o Mimikatz é catalogado como S0002 e é muito monitorado por EDR.
- d. Incorreta: a I é verdadeira; a linha do tempo é base para o *purple teaming*.
- e. Incorreta: ambas são verdadeiras. Revise "O relatório de Red Team".

**Questão 21** (correta: b)
- a. Incorreta: 24 ÷ 240 = 10% usa todos os subdomínios encontrados, e não a superfície ativa (os 160 que respondem).
- b. Correta: 24 ÷ 160 = 15% da superfície ativa é desconhecida pela TI.
- c. Incorreta: 160 ÷ 240 ≈ 66,7% é a fração de subdomínios que ainda respondem, não a de ativos desconhecidos.
- d. Incorreta: 24% confunde a quantidade absoluta (24 ativos) com o percentual.
- e. Incorreta: 85% é a fração de ativos conhecidos (136 ÷ 160), o complemento do que se pede.

**Questão 22** (correta: d)
- a. Incorreta: 32% é a parcela do quadro não exposta (160 ÷ 500).
- b. Incorreta: 34% resulta de dividir 340 por 1.000, base incorreta.
- c. Incorreta: 47% não corresponde a nenhuma relação entre os dados; revise o cálculo.
- d. Correta: 340 ÷ 500 = 68% do quadro está exposto como possível alvo de *phishing*.
- e. Incorreta: 74% não decorre dos dados informados; a conta correta é 340 ÷ 500.

**Questão 23** (correta: a)
- a. Correta: a varredura de portas (3) e as consultas massivas ao DNS da empresa (5) interagem com os sistemas do alvo e aparecem em registros de *firewall* e DNS.
- b. Incorreta: 1, 2 e 4 são atividades passivas, feitas em fontes de terceiros, e praticamente não deixam rastro no ambiente.
- c. Incorreta: a consulta à transparência de certificados (1) é passiva.
- d. Incorreta: a pesquisa no Shodan (2) consulta a base do serviço, e não os servidores da empresa.
- e. Incorreta: a leitura de vagas (4) é passiva e não toca o ambiente do alvo.

**Questão 24** (correta: e)
- a. Incorreta: testar credenciais em ativo fora do escopo é acesso não autorizado e pode configurar crime, por mais breve que seja.
- b. Incorreta: varredura é reconhecimento ativo e exige que o ativo esteja no escopo.
- c. Incorreta: o achado é valioso (*shadow IT*) e deve ser registrado e comunicado, ainda que não possa ser testado.
- d. Incorreta: divulgar publicamente a falha viola a confidencialidade do engajamento e expõe cliente e fornecedor.
- e. Correta: registrar sem acessar e comunicar ao cliente respeita o escopo e permite atualizar o inventário e, se for o caso, ampliar formalmente a autorização.

**Questão 25** (correta: c)
- a. Incorreta: T1595 é varredura ativa contra a infraestrutura, não coleta de dados de pessoas em fontes abertas.
- b. Incorreta: T1566 é o envio de *phishing* (acesso inicial), etapa posterior à coleta de alvos.
- c. Correta: a coleta de nomes, *e-mails* e padrão de endereços corresponde a T1589 — *Gather Victim Identity Information*.
- d. Incorreta: T1046 é descoberta de serviços de rede, feita de dentro do ambiente.
- e. Incorreta: T1078 é o uso de contas válidas, não a coleta de informações sobre elas.

**Questão 26** (correta: a)
- a. Correta: E está no KEV, tem EPSS de 93% e está exposta à internet — é a que representa maior risco real.
- b. Incorreta: o CVSS mede severidade técnica; G tem baixa probabilidade de exploração e está em ativo desconectado.
- c. Incorreta: D tem EPSS de 1%, não está no KEV e está em servidor isolado; a nota crítica não basta.
- d. Incorreta: F tem severidade média, não está no KEV e tem probabilidade moderada; não supera E.
- e. Incorreta: o EPSS, o KEV e a exposição alteram, sim, a ordem de prioridade. Revise a priorização por risco.

**Questão 27** (correta: e)
- a. Incorreta: 12,5 semanas corresponde a todos os 1.500 achados (1.500 ÷ 120), não à fila de CVSS ≥ 7,0.
- b. Incorreta: a fila filtrada é 48 ÷ 120 = 0,4 semana, não 4 semanas.
- c. Incorreta: 600 ÷ 120 = 5 semanas, e 48 ÷ 120 = 0,4 semana.
- d. Incorreta: 2,5 semanas não resulta de 48 ÷ 120; revise a divisão.
- e. Correta: 600 ÷ 120 = 5 semanas e 48 ÷ 120 = 0,4 semana, cerca de dois dias úteis.

**Questão 28** (correta: b)
- a. Incorreta: 4,0 já é média e 9,0 já é crítica.
- b. Correta: 3,9 é baixa (0,1–3,9), 4,0 é média (4,0–6,9), 7,0 é alta (7,0–8,9) e 9,0 é crítica (9,0–10,0).
- c. Incorreta: 3,9 ainda está na faixa baixa.
- d. Incorreta: 7,0 é alta e 9,0 é crítica; os limites inferiores pertencem à faixa superior.
- e. Incorreta: "nenhuma" corresponde apenas à nota 0,0.

**Questão 29** (correta: d)
- a. Incorreta: varreduras lentas e seletivas são justamente o recurso usado em operações que testam a detecção.
- b. Incorreta: toda varredura gera conexões registráveis; o problema é a detecção não correlacioná-las.
- c. Incorreta: detectar apenas o barulhento deixa uma lacuna diante de adversários discretos.
- d. Correta: a pergunta da aula é "nossa detecção percebe varreduras discretas, ou só as barulhentas?" — o resultado aponta uma lacuna.
- e. Incorreta: o exercício descrito trata de varreduras, não compara enumeração interna com varredura externa.

**Questão 30** (correta: c)
- a. Incorreta: H não está no KEV, então segue a regra de falhas altas (30 dias); I segue a regra do KEV (7 dias).
- b. Incorreta: I está no KEV em ativo exposto; o prazo é 7 dias, independentemente do CVSS 6,1.
- c. Correta: H é alta (7,8) fora do KEV — 30 dias; I está no KEV em ativo exposto — 7 dias.
- d. Incorreta: o prazo de 7 dias vale só para KEV em ativo exposto, o que não é o caso de H.
- e. Incorreta: os prazos estão trocados e não seguem a política descrita.

**Questão 31** (correta: e)
- a. Incorreta: 4% é a taxa de submissão (80 ÷ 2.000), e 0,67 não é a razão reporte/clique desta campanha.
- b. Incorreta: a taxa de clique é 260 ÷ 2.000 = 13%, não 26%.
- c. Incorreta: a razão reporte/clique é 390 ÷ 260 = 1,5; 0,67 é a razão inversa.
- d. Incorreta: os valores estão trocados e a razão não corresponde aos dados.
- e. Correta: 260 ÷ 2.000 = 13%; 390 ÷ 2.000 = 19,5%; 390 ÷ 260 = 1,5 reporte por clique.

**Questão 32** (correta: a)
- a. Correta: "todos já fizeram, falta só você" é o exemplo típico de aprovação social.
- b. Incorreta: autoridade envolve alguém que se apresenta com poder, como um diretor.
- c. Incorreta: reciprocidade envolve oferecer algo antes de pedir.
- d. Incorreta: compromisso e coerência envolve pedidos que crescem aos poucos.
- e. Incorreta: afeição envolve simpatia e semelhança antes do pedido.

**Questão 33** (correta: c)
- a. Incorreta: o tema pode causar dano real e a lista nominal para punição contraria a finalidade educativa e a proteção de dados.
- b. Incorreta: mudar o destinatário da lista não resolve o problema do pretexto danoso nem da finalidade punitiva.
- c. Correta: pretexto não danoso, alinhamento com RH, jurídico e DPO, métricas agregadas e orientação a quem clica são os requisitos de uma simulação ética.
- d. Incorreta: simulações autorizadas são legítimas quando seguem a LGPD e as regras de engajamento.
- e. Incorreta: varredura de portas mede exposição técnica, não a capacidade das pessoas de reconhecer e reportar *phishing*.

**Questão 34** (correta: d)
- a. Incorreta: o episódio 1 é por voz (*vishing*) e o 3 é *tailgating*, não *pretexting*.
- b. Incorreta: o episódio 2 é por SMS, e não há *e-mail* corporativo comprometido no episódio 3.
- c. Incorreta: o episódio 3 é físico (*tailgating*), não por voz.
- d. Correta: ligação = *vishing*; SMS = *smishing*; entrar atrás de um funcionário = *tailgating*.
- e. Incorreta: a ordem está invertida em relação aos episódios.

**Questão 35** (correta: b)
- a. Incorreta: o reporte é o rastro humano mais valioso; um único reporte rápido permite bloquear a mensagem para toda a empresa.
- b. Correta: a aula descreve rastros técnicos (domínio recente e parecido, falha de SPF/DKIM/DMARC, cliques no *proxy*) e o rastro humano (o reporte), que juntos permitem resposta rápida.
- c. Incorreta: falhas de autenticação de *e-mail* indicam remetente não autorizado pelo domínio, geralmente externo.
- d. Incorreta: o *proxy* mostra quem clicou, mas não mede a capacidade de detecção humana, que exige taxa e tempo de reporte.
- e. Incorreta: domínios recém-registrados e parecidos com o da empresa são indício clássico de *phishing*.

**Questão 36** (correta: e)
- a. Incorreta: 2.000 ÷ 8.000 = 25%, não 20%.
- b. Incorreta: o percentual final é 64 ÷ 8.000 = 0,8%, e a redução é cerca de 96,8%.
- c. Incorreta: 3,2% é a fração de caminhos que restou (64 ÷ 2.000), não a redução.
- d. Incorreta: os percentuais foram calculados com a vírgula deslocada.
- e. Correta: 2.000 ÷ 8.000 = 25%; 64 ÷ 8.000 = 0,8%; (2.000 − 64) ÷ 2.000 = 1.936 ÷ 2.000 ≈ 96,8%.

**Questão 37** (correta: b)
- a. Incorreta: 60% é a taxa de técnicas não detectadas (9 ÷ 15), e omitir o dado contraria o propósito do relatório.
- b. Correta: 6 ÷ 15 = 40%, e o relatório deve destacar o que passou despercebido como base para melhorar a detecção.
- c. Incorreta: 6 é a quantidade absoluta, não o percentual; e o relatório recomenda melhorias, não substituições de equipe.
- d. Incorreta: o percentual está certo, mas recomendações priorizadas são parte essencial do relatório.
- e. Incorreta: 60% está errado, e técnicas detectadas continuam úteis para medir regressões.

**Questão 38** (correta: a)
- a. Correta: acesso ao LSASS indica acesso a credenciais (TA0006); *logons* remotos atípicos indicam movimentação lateral (TA0008); *beaconing* indica comando e controle (TA0011).
- b. Incorreta: *logons* remotos não são descoberta, e *beaconing* não é acesso a credenciais.
- c. Incorreta: acesso ao LSASS não é escalada de privilégios, e *logons* remotos não são persistência.
- d. Incorreta: *beaconing* é comando e controle, não persistência.
- e. Incorreta: o acesso ao LSASS é acesso a credenciais, não descoberta.

**Questão 39** (correta: c)
- a. Incorreta: o sumário executivo traz objetivos, resultado e riscos em linguagem de negócio, sem esse detalhe técnico.
- b. Incorreta: a narrativa descreve as ações do Red Team; o trecho avalia o que a defesa percebeu.
- c. Correta: a análise de detecção e resposta indica o que foi detectado, quando e o que passou despercebido.
- d. Incorreta: o trecho não propõe ações; constata o desempenho da detecção.
- e. Incorreta: escopo e regras de engajamento tratam do que é permitido, não dos resultados de detecção.

**Questão 40** (correta: d)
- a. Incorreta: o caminho não decorreu de uma vulnerabilidade de *software*, mas do uso indevido de uma credencial privilegiada.
- b. Incorreta: a simulação ajuda, mas o problema central foi a conta administrativa de uso diário sem segundo fator.
- c. Incorreta: a movimentação lateral com contas válidas não depende de varreduras de portas.
- d. Correta: proteger contas privilegiadas — separação de contas, segundo fator e acesso sob demanda — corta o atalho das credenciais válidas.
- e. Incorreta: a narrativa do ataque é essencial para que o Blue Team compare ações e registros.
