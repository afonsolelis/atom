# Avaliação final — 10 questões discursivas

Disciplina: Red Team & Blue Team Strategies  
Professor-conteudista: Afonso Cesar Lelis Brandão  
Prazo de entrega: 20/12/2026  
Template de origem: `documentos/Instrumentos Avaliativos/Avaliação final_(10 discursivas)_nomedadisciplina.docx`

> 10 questões discursivas no estilo ENADE (avaliação crítica e analítica), cobrindo as 4 unidades.
> O feedback (resposta esperada) de cada questão fica ao final do documento.

> **Controle de versão:** a seção "Questões" destina-se ao estudante. A seção "Feedbacks" é exclusiva do professor tutor e contém as respostas esperadas e os critérios de correção; ela deve ser removida da cópia distribuída aos estudantes.

**Orientações ao estudante**

- Quantidade: 10 questões discursivas, com valor sugerido de 10 pontos cada (total de 100 pontos).
- Distribuição: Unidade 1, questões 1 a 3; Unidade 2, questões 4 e 5; Unidade 3, questões 6 a 8; Unidade 4, questões 9 e 10 (a questão 10 é integradora e mobiliza conteúdos de toda a disciplina).
- Extensão esperada: de 10 a 20 linhas por questão.
- Todas as organizações e situações são fictícias. As atividades ofensivas citadas ocorrem sempre em engajamentos formalmente autorizados.
- Respostas apenas definicionais, sem análise do cenário apresentado, não atendem integralmente ao comando da questão. Quando houver cálculo, mostre o raciocínio.

## Questões

### Questão 1 — Unidade 1: autorização, escopo e regras de engajamento

A Mercantil Aurora, rede varejista com 60 lojas e um *e-commerce* hospedado em um provedor de nuvem, decidiu "testar a segurança" após um concorrente sofrer um vazamento. O gerente de TI convidou, por mensagem de aplicativo, um consultor conhecido para "tentar invadir o site e o que mais conseguir, quando tiver tempo", sem contrato. O consultor pretende incluir no teste o sistema de pagamentos (operado por uma empresa parceira) e copiar uma amostra da base de clientes "para provar que conseguiu".

Analise a situação e responda:

a) Explique o que, do ponto de vista legal e ético, diferencia a atividade de um Red Team da conduta de um criminoso, citando a legislação brasileira estudada, e por que a mensagem do gerente de TI não é suficiente.

b) Proponha os elementos mínimos do documento de autorização e das regras de engajamento para esse teste, tratando especificamente do sistema do parceiro e da amostra de dados pessoais.

### Questão 2 — Unidade 1: Cyber Kill Chain e MITRE ATT&CK na leitura de um incidente

A Transportadora Pantanal Cargas reconstruiu a linha do tempo de um incidente real:

| Dia | Evento observado |
|---|---|
| D−20 | Perfis de funcionários do setor financeiro são consultados em redes sociais profissionais |
| D−3 | Registro de um domínio parecido com o de um cliente da transportadora |
| D0 | *E-mail* com fatura falsa chega a 12 colaboradores; um deles abre o anexo |
| D0 | Estação do colaborador passa a se comunicar periodicamente com um servidor externo |
| D+4 | Credenciais de um administrador são usadas em *logons* remotos em três servidores |
| D+9 | Grande volume de dados sai para um serviço de armazenamento em nuvem não homologado |

a) Associe os eventos às fases da Cyber Kill Chain e explique por que a maior parte deles, a partir de D+4, fica mal representada nesse modelo.

b) Justifique por que o MITRE ATT&CK complementa a Kill Chain nesse caso, explicando como o Blue Team pode usá-lo para transformar essa linha do tempo em melhorias de detecção.

### Questão 3 — Unidade 1: escolha do tipo de avaliação e fundamentos da defesa

A Fintech Paguá tem R$ 150.000 de orçamento anual para avaliações de segurança. Duas propostas estão em discussão:

| Proposta | Composição | Custo anual |
|---|---|---|
| A | Cinco *pentests* de aplicações (R$ 30.000 cada) | R$ 150.000 |
| B | Varreduras mensais (R$ 2.500/mês) + uma operação de Red Team | R$ 30.000 + R$ 120.000 |

A diretoria declarou duas preocupações: (1) "se fôssemos atacados hoje, nosso SOC terceirizado perceberia?"; e (2) a empresa vai lançar, no próximo semestre, dois aplicativos novos expostos à internet. O inventário de ativos foi atualizado pela última vez há dois anos.

Compare varredura de vulnerabilidades, *pentest* e operação de Red Team quanto à pergunta que cada uma responde e, considerando as duas preocupações da diretoria e o estado do inventário (à luz das funções do NIST CSF 2.0), justifique qual alocação de orçamento você recomendaria. Você pode propor uma combinação diferente das duas apresentadas.

### Questão 4 — Unidade 2: priorização de vulnerabilidades com CVSS, EPSS e KEV

A equipe de infraestrutura da Rede Hospitalar Serra Verde consegue corrigir 100 vulnerabilidades por semana. A varredura do mês retornou 900 achados, dos quais 420 têm CVSS ≥ 7,0. Três exemplos ilustram a fila:

| Vulnerabilidade | CVSS | EPSS | No catálogo KEV? | Ativo |
|---|---|---|---|---|
| X | 9,6 | 0,01 (1%) | Não | Servidor de testes sem acesso externo |
| Y | 7,2 | 0,82 (82%) | Sim | Portal de agendamento exposto à internet |
| Z | 6,1 | 0,35 (35%) | Não | Concentrador de VPN dos médicos |

a) Calcule quanto tempo a equipe levaria para tratar apenas a fila de CVSS ≥ 7,0 e explique por que priorizar somente pelo CVSS é uma estratégia limitada.

b) Proponha um critério de priorização que combine as três fontes de informação e o contexto do ativo, ordenando X, Y e Z e justificando a ordem.

### Questão 5 — Unidade 2: simulação de *phishing* e leitura de métricas

A Prefeitura de Rio Claro do Sul contratou uma simulação de *phishing* autorizada para 2.000 servidores. Os resultados de duas campanhas, de dificuldade equivalente, foram:

| Campanha | Cliques | Submissões de dados | Reportes | Tempo até o primeiro reporte |
|---|---|---|---|---|
| Março | 300 | 110 | 160 | 42 min |
| Setembro | 240 | 60 | 480 | 6 min |

O secretário de administração afirmou: "a taxa de cliques quase não mudou; o programa de conscientização fracassou. Quero a lista nominal de quem clicou nas duas campanhas para abrir processos administrativos".

a) Calcule as taxas de clique, submissão e reporte e a razão reporte/clique de cada campanha e avalie criticamente a conclusão do secretário.

b) Explique os riscos éticos e legais do uso pretendido para a lista nominal e proponha como os resultados deveriam ser apresentados e utilizados.

### Questão 6 — Unidade 3: SIEM, fadiga de alertas e capacidade do SOC

O SOC da Distribuidora Elétrica Planalto recebe 1.500 alertas por dia no SIEM. A triagem de cada alerta leva, em média, 12 minutos. A equipe de nível 1 tem oito analistas, cada um com cerca de 6 horas efetivas de triagem por dia. Uma análise de 30 dias mostrou que 70% dos alertas vêm de apenas cinco regras, quase todas com falsos positivos recorrentes de rotinas administrativas conhecidas.

a) Calcule a capacidade diária de triagem da equipe e o percentual do volume que ela consegue analisar. Explique o conceito de fadiga de alertas e por que ela é um risco de segurança, e não apenas de produtividade.

b) Proponha ações para reequilibrar volume e capacidade sem simplesmente desligar regras, justificando como cada ação preserva a capacidade de detecção.

### Questão 7 — Unidade 3: engenharia de detecção e Pirâmide da Dor

A Cooperativa Agrícola Vale do Ipê recebeu um relatório de inteligência sobre um grupo que ataca o agronegócio. O relatório traz 500 endereços IP, 200 *hashes* de arquivos e a descrição do comportamento do grupo: uso de credenciais válidas de acesso remoto obtidas por *phishing*, criação de tarefas agendadas para persistência e uso de ferramentas administrativas legítimas para se mover entre servidores. O gestor do SOC propôs apenas importar os IPs e *hashes* para o *firewall* e o EDR e considerar a ameaça "coberta". Ao mesmo tempo, uma regra existente de tarefas agendadas suspeitas disparou 250 vezes no último mês, com 10 verdadeiros positivos.

a) Com base na Pirâmide da Dor, analise a limitação da proposta do gestor e indique em que níveis da pirâmide estão as diferentes partes do relatório.

b) Calcule a precisão da regra de tarefas agendadas e proponha, segundo o ciclo de vida de uma detecção, como melhorá-la e como comprovar que ela funciona antes de considerá-la confiável. Indique também uma hipótese de *threat hunting* derivada do relatório.

### Questão 8 — Unidade 3: resposta a incidentes, evidências e obrigações legais

Na rede de escolas Instituto Horizonte, o EDR alertou às 23h de uma quinta-feira que quatro servidores estavam excluindo cópias de sombra e renomeando arquivos em massa. Um dos servidores hospeda a secretaria acadêmica, com dados pessoais de alunos menores de idade. O técnico de plantão sugeriu desligar todos os servidores da tomada imediatamente e, na segunda-feira, "ver o que aconteceu". Na sexta-feira, às 10h, a equipe confirmou que arquivos da secretaria haviam sido copiados para fora da rede antes da criptografia.

a) Avalie criticamente a sugestão do técnico, considerando a tensão entre conter o dano e preservar evidências, e descreva uma contenção mais adequada, com os cuidados de cadeia de custódia.

b) Explique quais obrigações de comunicação decorrem da confirmação feita na sexta-feira, segundo a LGPD e a regulamentação da ANPD, quais papéis precisam ser acionados e como as atividades desse incidente se relacionam às funções do CSF 2.0 no NIST SP 800-61 Rev. 3.

### Questão 9 — Unidade 4: *purple teaming* e métricas de detecção

O CISO da Seguradora Atlântica Sul apresentou ao conselho o seguinte painel trimestral:

| Indicador | Valor apresentado |
|---|---|
| Ataques bloqueados | 3,2 milhões |
| Cobertura ATT&CK | 85% ("existem regras para 85% das técnicas da matriz") |
| MTTD médio | 40 horas |
| MTTD mediano | 6 horas |
| Alertas no trimestre | 2.400, dos quais 240 verdadeiros positivos |

Nenhuma das regras foi executada contra o comportamento real das técnicas. Um conselheiro perguntou se a seguradora estava "85% protegida".

a) Analise criticamente o painel: explique por que "ataques bloqueados" e a cobertura de 85% não respondem à pergunta do conselheiro, interprete a diferença entre MTTD médio e mediano e calcule a precisão dos alertas.

b) Proponha como um programa de *purple teaming* com emulação de adversários produziria indicadores mais confiáveis, descrevendo o ciclo de trabalho e a métrica de cobertura que deveria substituir a apresentada.

### Questão 10 — Unidade 4: programa contínuo de segurança (questão integradora)

A Indústria Metalúrgica Ferraço, com 3.000 colaboradores e produção 24 horas, nunca fez exercícios de simulação. Seus dados atuais:

- perda estimada de um incidente grave de *ransomware*: R$ 12 milhões, com probabilidade anual estimada de 10%;
- programa contínuo proposto (Red Team anual, ciclos trimestrais de *purple teaming*, engenharia de detecção e exercícios *tabletop*): R$ 400.000 por ano, com redução estimada da probabilidade para 4%;
- *backups* nunca foram restaurados em teste completo, e o plano de resposta a incidentes foi aprovado há três anos sem nunca ter sido exercitado.

a) Calcule a ALE atual, a ALE com o programa e o ROSI, e discuta as limitações dessa estimativa para a decisão do conselho.

b) Proponha a estrutura do programa para o primeiro ano, integrando o papel de Red, Blue e Purple Team, um exercício *tabletop* (com pelo menos três *injects* ligados às fragilidades descritas) e os indicadores que serão usados para demonstrar evolução.

## Feedbacks

> **Uso exclusivo do professor tutor.** As respostas esperadas são referências, não gabaritos literais: devem ser aceitas formulações diferentes que demonstrem domínio dos conceitos e análise do cenário. Em cada questão, a nota integral exige os elementos listados nos critérios; a ausência de análise do cenário (resposta apenas conceitual) limita a nota a crédito parcial.

### Questão 1

**Resposta esperada**

a) Tecnicamente, muitas ações de um Red Team são idênticas às de um criminoso; o que as distingue é a **autorização formal**, dada por quem tem autoridade sobre os ativos, com escopo e limites definidos. No Brasil, a Lei nº 12.737/2012 incluiu no Código Penal o art. 154-A, que tipifica a invasão de dispositivo informático, com penas agravadas pela Lei nº 14.155/2021. A mensagem do gerente não basta: é informal, não define escopo nem período ("o que mais conseguir, quando tiver tempo"), não há garantia de que o gerente tenha autoridade para autorizar e, sobretudo, ele não pode autorizar testes em ativos que não pertencem à Mercantil Aurora (o sistema de pagamentos do parceiro e, conforme o contrato, a infraestrutura do provedor de nuvem). Eticamente, copiar dados de clientes "para provar" expõe dados pessoais sem necessidade.

b) Elementos mínimos: documento assinado por quem tem autoridade (diretoria) contendo **escopo** (ativos incluídos e excluídos, por exemplo URLs e endereços do *e-commerce*), **período e janelas** de execução, **técnicas permitidas e proibidas** (por exemplo, sem negação de serviço), **contatos de emergência** e critérios de interrupção, e regras de **tratamento e descarte** dos dados e credenciais. O sistema de pagamentos do parceiro deve ficar **fora do escopo**, a menos que o próprio parceiro autorize formalmente; o uso do provedor de nuvem deve respeitar a política do provedor. Quanto aos dados pessoais, o **impacto deve ser demonstrado, e não executado**: registrar evidência de acesso (por exemplo, a estrutura da tabela ou a contagem de registros) em vez de copiar a base, com exposição mínima e descarte ao final, conforme a LGPD (Lei nº 13.709/2018). O relatório final documenta o que foi feito.

**Critérios de correção**

- Integral: cita autorização formal como diferença central e o art. 154-A (Lei nº 12.737/2012, com ou sem a Lei nº 14.155/2021); aponta ao menos duas falhas da mensagem (informalidade/escopo indefinido/autoridade/ativos de terceiros); lista escopo, regras de engajamento e contatos de emergência; trata o parceiro como fora do escopo sem autorização dele; propõe demonstrar o impacto sem copiar dados, mencionando a LGPD.
- Parcial: reconhece a necessidade de autorização, mas não cita a legislação ou não trata do sistema do parceiro ou dos dados pessoais.
- Insuficiente: considera a mensagem válida ou descreve formas de executar o ataque.

### Questão 2

**Resposta esperada**

a) D−20: **reconhecimento** (coleta de informações sobre alvos em redes sociais). D−3: **armamento/preparação** (infraestrutura do ataque, domínio semelhante ao de um cliente). D0, *e-mail*: **entrega**; abertura do anexo: **exploração** e **instalação**. Comunicação periódica com servidor externo: **comando e controle**. D+4 e D+9: **ações sobre objetivos**. A Kill Chain foi concebida com foco na intrusão inicial e é linear; tudo o que acontece depois do acesso — uso de credenciais válidas, movimentação lateral entre servidores, coleta e exfiltração — fica comprimido em uma única fase ("ações sobre objetivos"), justamente onde o atacante passou a maior parte do tempo. O modelo também não descreve bem ataques que não seguem a sequência, como abuso de credenciais legítimas.

b) O ATT&CK descreve o comportamento adversário em **táticas** (o objetivo: acesso inicial, execução, persistência, movimentação lateral, exfiltração etc.) e **técnicas** (como o objetivo é alcançado), com base em observações reais. Ele detalha exatamente o trecho que a Kill Chain resume: o *phishing* com anexo (acesso inicial), o uso de contas válidas, os serviços remotos para movimentação lateral e a exfiltração para serviço de nuvem. O Blue Team pode mapear cada evento para uma técnica, verificar se havia **telemetria** e **regra testada** para cada uma, medir a cobertura e priorizar as lacunas — começando pelas técnicas que já têm registros, pois criar a regra é mais barato que obter a fonte de dados. As duas abordagens são complementares: a Kill Chain comunica a sequência à gestão; o ATT&CK dá o vocabulário operacional para detecção e testes.

**Critérios de correção**

- Integral: associa corretamente ao menos cinco eventos às fases; explica a limitação da Kill Chain no pós-acesso (linearidade, foco no perímetro); explica táticas e técnicas do ATT&CK e descreve o uso para mapear lacunas de telemetria e detecção; reconhece a complementaridade.
- Parcial: mapeamento correto, mas sem análise da limitação, ou explicação do ATT&CK genérica, sem ligação com a linha do tempo.
- Insuficiente: confunde fases ou trata os modelos como concorrentes sem justificativa.

### Questão 3

**Resposta esperada**

A **varredura** responde "quais falhas conhecidas existem nos meus ativos?": é ampla, rápida, periódica e barata, mas gera falsos positivos e não prova a explorabilidade. O ***pentest*** responde "o que um atacante consegue explorar neste alvo?": é delimitado e busca o maior número de falhas relevantes. A **operação de Red Team** responde "a organização detecta e responde a um ataque realista?": é orientada a objetivo, furtiva, mais longa, e avalia pessoas e processos de defesa, normalmente sem avisar o Blue Team.

A preocupação (1) — se o SOC perceberia um ataque — só é respondida por uma operação de Red Team, o que favorece a proposta B. A preocupação (2) — dois aplicativos novos — é típica de *pentest*, que a proposta B não contempla. Além disso, o inventário desatualizado é uma falha da função **Identificar** do NIST CSF 2.0: não é possível testar nem monitorar (Detectar) um ativo que ninguém sabe que existe; varreduras e o reconhecimento do Red Team ajudam a revelar ativos desconhecidos, mas a atualização do inventário é pré-requisito. Uma recomendação coerente seria uma combinação, por exemplo: varreduras mensais (R$ 30.000), dois *pentests* nos aplicativos antes do lançamento (R$ 60.000) e uma operação de Red Team de escopo menor (R$ 60.000) focada no objetivo de negócio mais crítico, ou adiar o Red Team caso o inventário e a visibilidade básica ainda sejam precários. Aceitam-se outras alocações desde que justificadas pelas preocupações e pela maturidade.

**Critérios de correção**

- Integral: diferencia corretamente as três avaliações pela pergunta que respondem; relaciona a preocupação (1) ao Red Team e a (2) ao *pentest*; aponta o inventário desatualizado como lacuna da função Identificar (ou Governar) do CSF 2.0; apresenta alocação coerente com o orçamento e justificada.
- Parcial: diferencia as avaliações, mas escolhe uma proposta sem analisar as duas preocupações, ou ignora o inventário.
- Insuficiente: trata *pentest* e Red Team como sinônimos ou faz recomendação sem justificativa.

### Questão 4

**Resposta esperada**

a) 420 ÷ 100 = **4,2 semanas** apenas para a fila de CVSS ≥ 7,0, sem contar os achados novos que surgirão no período. O CVSS mede a **gravidade técnica** da falha, mas não indica se ela está sendo explorada nem considera o contexto do ativo. Priorizar só por ele leva a gastar esforço em falhas graves mas improváveis (como X, em servidor isolado) enquanto falhas exploradas ativamente esperam na fila.

b) Critério: priorizar primeiro o que está no **KEV** (exploração confirmada) em ativos expostos ou críticos; depois, alta **EPSS** (probabilidade de exploração nos próximos 30 dias) combinada à exposição e à criticidade do ativo; usar o CVSS como desempate e critério de severidade. Ordem: **Y** (no KEV, EPSS de 82%, exposta à internet, portal de pacientes); **Z** (EPSS de 35%, VPN é porta de entrada remota e alvo frequente, mesmo com CVSS médio); **X** (CVSS alto, mas EPSS de 1% e ativo sem acesso externo; pode seguir o ciclo normal, com mitigação compensatória). Aplicando esse filtro, a fila crítica tende a ser muito menor que 420 itens e pode ser tratada em dias. Deve-se ainda tratar a gestão de vulnerabilidades como processo contínuo (identificar, priorizar, corrigir, verificar) e verificar a correção com nova varredura.

**Critérios de correção**

- Integral: calcula 4,2 semanas; explica que o CVSS mede gravidade e não probabilidade/exploração; define EPSS e KEV corretamente; ordena Y, Z, X (ou Y, X, Z com justificativa contextual consistente) considerando exposição e criticidade.
- Parcial: ordenação correta sem explicar os indicadores, ou cálculo ausente/errado.
- Insuficiente: prioriza X por ter o maior CVSS sem considerar exploração nem contexto.

### Questão 5

**Resposta esperada**

a) Março: cliques 300 ÷ 2.000 = **15%**; submissões 110 ÷ 2.000 = **5,5%**; reportes 160 ÷ 2.000 = **8%**; razão reporte/clique 160 ÷ 300 ≈ **0,53**. Setembro: cliques **12%**; submissões **3%**; reportes 480 ÷ 2.000 = **24%**; razão 480 ÷ 240 = **2,0**. A conclusão do secretário se apoia na métrica menos informativa. Embora os cliques tenham caído pouco, as submissões (o dano efetivo) caíram quase pela metade, os reportes triplicaram e o tempo até o primeiro reporte caiu de 42 para 6 minutos. Para a defesa, o que importa é que alguém avise rápido: um reporte em 6 minutos permite ao Blue Team bloquear o domínio e remover a mensagem das demais caixas. O programa teve resultado positivo; "quem clicou?" é a pergunta errada.

b) Usar a lista nominal para punição contraria a finalidade educativa da simulação, gera medo e desestimula justamente o comportamento desejado (reportar, inclusive quando se clicou). Do ponto de vista legal, os resultados individuais são dados pessoais: a LGPD exige finalidade definida, necessidade e transparência, e o uso disciplinar não previsto no plano da campanha desvirtua a finalidade. Recomenda-se apresentar dados **agregados** (por setor, por tipo de pretexto, evolução entre campanhas), com dados individuais restritos à equipe responsável e usados apenas para ação educativa imediata (página de orientação, treinamento curto); manter e divulgar o botão de reporte; e definir, no plano da campanha aprovado, finalidade, tratamento e descarte dos dados.

**Critérios de correção**

- Integral: calcula corretamente as taxas e as razões; contesta a conclusão com base em submissões, reportes e tempo até o primeiro reporte; explica os riscos éticos (punição, cultura do medo) e legais (LGPD, finalidade); propõe apresentação agregada e uso educativo.
- Parcial: cálculos corretos sem análise crítica, ou análise crítica sem cálculos; ou menciona ética sem relacioná-la à LGPD.
- Insuficiente: concorda com a punição ou analisa apenas a taxa de cliques.

### Questão 6

**Resposta esperada**

a) Volume: 1.500 × 12 = 18.000 minutos = **300 horas** de análise por dia. Capacidade: 8 × 6 = 48 horas = 2.880 minutos ÷ 12 = **240 alertas por dia**, ou **16%** do volume. A **fadiga de alertas** ocorre quando o excesso de alertas, em especial falsos positivos, leva os analistas a fechá-los rapidamente ou ignorá-los; com isso, o alerta verdadeiro se perde no ruído. É um risco de segurança porque 84% dos alertas sequer são analisados, e a atenção dedicada aos analisados cai — o ataque real pode estar entre os ignorados, aumentando o *dwell time*.

b) Ações: (1) **ajustar as cinco regras ruidosas** com exceções restritas às rotinas administrativas conhecidas (por exemplo, por conta de serviço e servidor de origem específicos), sem desligá-las — se elas responderem por 70% do volume (1.050 alertas) e o ajuste eliminar a maior parte do ruído, o volume se aproxima da capacidade; (2) **priorizar por criticidade** do ativo e confiança da regra, para que os alertas mais relevantes sejam triados primeiro; (3) **enriquecer e correlacionar** no SIEM (contexto de ativo, usuário, inteligência), agrupando alertas relacionados em um único caso; (4) **automatizar** etapas repetitivas da triagem (SOAR); (5) **revisar continuamente** a precisão de cada regra como métrica. Cada ação reduz ruído sem retirar visibilidade da técnica monitorada; exceções devem ser estreitas, documentadas e revisadas, para não abrir brechas que o atacante possa usar.

**Critérios de correção**

- Integral: calcula 240 alertas/dia e cerca de 16%; define fadiga de alertas e explica por que é risco de segurança; propõe ao menos três ações, incluindo o ajuste das regras ruidosas com exceções restritas, justificando a preservação da detecção.
- Parcial: cálculo correto e propostas genéricas (por exemplo, "contratar mais analistas" como única ação), ou propostas boas sem cálculo.
- Insuficiente: propõe desligar as regras ou ignora a fadiga de alertas.

### Questão 7

**Resposta esperada**

a) A Pirâmide da Dor, proposta por David Bianco, relaciona o tipo de indicador ao custo que sua detecção impõe ao adversário. *Hashes* (base) e endereços IP estão nos níveis mais baixos: são triviais ou fáceis de trocar, de modo que o bloqueio é útil, mas contornado em minutos. A descrição do comportamento — credenciais válidas de acesso remoto, tarefas agendadas para persistência, uso de ferramentas administrativas legítimas para movimentação lateral — está no topo, nas **TTPs**, que obrigam o adversário a mudar sua forma de trabalhar. Considerar a ameaça "coberta" só com IPs e *hashes* é um erro: justamente o comportamento mais estável do grupo fica sem detecção, e o uso de ferramentas legítimas sequer geraria *hash* malicioso.

b) Precisão: 10 ÷ 250 = **4%**. Pelo ciclo de vida da detecção: analisar os falsos positivos para identificar padrões (por exemplo, tarefas criadas por ferramentas corporativas conhecidas), refinar a lógica com exceções restritas e contexto (criação remota, contas incomuns, binários em pastas temporárias), versionar a regra como código (por exemplo, em padrão Sigma), e **testar** antes de confiar: executar o comportamento em ambiente autorizado (emulação, por exemplo com testes atômicos) e verificar se a regra dispara, além de medir a nova precisão no mês seguinte. Hipótese de caça: "se o grupo usa credenciais válidas de acesso remoto, haverá *logons* de VPN de contas em horários, locais ou dispositivos incomuns, seguidos de *logons* remotos em servidores que essas contas não costumam acessar". A caça que confirmar o padrão deve gerar uma nova regra automatizada.

**Critérios de correção**

- Integral: explica a Pirâmide da Dor, posiciona IPs/*hashes* na base e o comportamento em TTPs; critica a proposta; calcula 4%; descreve refinamento e teste da regra (com reteste/validação); formula uma hipótese de caça testável e ligada ao relatório.
- Parcial: explica a pirâmide, mas não propõe teste da regra, ou a hipótese de caça é genérica ("procurar ataques").
- Insuficiente: considera os IoCs suficientes ou não calcula/interpreta a precisão.

### Questão 8

**Resposta esperada**

a) Desligar os servidores da tomada interrompe a criptografia, mas destrói a **memória volátil** (processos, conexões, possíveis chaves), essencial para entender o ataque, e esperar até segunda-feira deixa o incidente sem tratamento por dias. A contenção busca impedir que o dano aumente preservando evidências: isolar os servidores pela rede (por exemplo, pelo isolamento do EDR), desabilitar contas comprometidas, bloquear destinos de comunicação suspeitos e coletar evidências da **mais volátil para a menos volátil** (memória antes do disco), conforme a RFC 3227. Toda evidência deve ter **cadeia de custódia**: quem coletou, quando, como, onde foi guardada e por quais mãos passou, com *hashes* que comprovem integridade (ABNT NBR ISO/IEC 27037). Em seguida vêm a erradicação (remover persistência e contas criadas, corrigir a falha de entrada) e a recuperação (restaurar de *backups* íntegros, com monitoramento reforçado). Se não houver como isolar e a criptografia avançar, desligar pode ser uma decisão justificável, mas deve ser tomada pelo coordenador do incidente, e não por improviso.

b) A confirmação de que dados pessoais (de menores, dado de alto risco) foram copiados é o marco a partir do qual corre o prazo: o art. 48 da LGPD e a Resolução CD/ANPD nº 15/2024 exigem comunicar à ANPD e aos titulares (aqui, alunos e responsáveis) incidente que possa causar risco ou dano relevante, em **três dias úteis** contados desse conhecimento (sexta-feira às 10h), além de manter registro do incidente. Devem ser acionados o coordenador do incidente, os analistas técnicos, o **encarregado de dados**, o **jurídico** e a **comunicação**. No NIST SP 800-61 Rev. 3, a resposta é tratada como perfil do CSF 2.0: a preparação ausente (plantão sem *playbook*) remete a Governar, Identificar e Proteger; o alerta e a análise, a Detectar; a contenção, a erradicação e a comunicação, a Responder; a restauração, a Recuperar; e as lições aprendidas alimentam a melhoria contínua.

**Critérios de correção**

- Integral: critica o desligamento pela perda de evidência volátil e pela demora; propõe isolamento e coleta por ordem de volatilidade com cadeia de custódia e *hashes*; identifica o prazo de três dias úteis a partir da confirmação, a comunicação à ANPD e aos titulares e os papéis (encarregado, jurídico, comunicação); relaciona as atividades às funções do CSF 2.0.
- Parcial: trata bem a contenção, mas erra ou omite as obrigações legais, ou vice-versa.
- Insuficiente: endossa a sugestão do técnico sem ressalvas ou desconhece a obrigação de comunicação.

### Questão 9

**Resposta esperada**

a) "Ataques bloqueados" é uma métrica de vaidade: conta eventos que os controles já resolvem (varreduras automatizadas, *spam*) e nada diz sobre a capacidade de detectar um adversário que passou pelas barreiras. A cobertura de 85% tem três armadilhas: conta a técnica como coberta só porque **existe** uma regra, sem nunca tê-la testado; trata todas as técnicas como iguais, embora uma regra possa detectar apenas um dos procedimentos possíveis; e mede contra a matriz inteira, e não contra as técnicas **priorizadas** pela inteligência de ameaças relevante para seguradoras. Logo, não significa "85% protegida". A diferença entre MTTD médio (40 h) e mediano (6 h) indica que poucos casos extremos — provavelmente incidentes detectados muito tarde — puxam a média para cima; a mediana mostra o caso típico, e os casos extremos merecem investigação própria. Precisão: 240 ÷ 2.400 = **10%**, ou seja, 90% de falsos positivos, um risco de fadiga de alertas.

b) O *purple teaming* reúne Red e Blue Team em ciclos curtos por técnica: **planejar** (técnica ATT&CK, comportamento e critério de sucesso), **executar** em ambiente autorizado, **observar** se houve telemetria, alerta e resposta, **ajustar** (regra, fonte de registro, *playbook*) e **retestar**. Com **emulação de adversários**, o plano usa as técnicas de grupos que efetivamente atacam o setor, com base em CTI. A métrica que deve substituir a apresentada é a **cobertura ATT&CK testada**: técnicas com detecção validada ÷ técnicas priorizadas, acompanhada de visibilidade (técnicas com telemetria ÷ priorizadas), precisão dos alertas, MTTD/MTTR medianos com marcos bem definidos e taxa de reteste. Frameworks como o DeTT&CT permitem pontuar visibilidade e detecção em níveis, em vez de "coberto/não coberto".

**Critérios de correção**

- Integral: critica "ataques bloqueados"; aponta ao menos duas armadilhas da cobertura (não testada, procedimentos, matriz inteira x técnicas priorizadas); interpreta média x mediana; calcula 10%; descreve o ciclo de *purple teaming* com reteste, a emulação baseada em ameaças relevantes e a cobertura testada sobre técnicas priorizadas.
- Parcial: crítica correta sem proposta estruturada, ou proposta sem análise do painel; ausência do cálculo ou da interpretação da mediana.
- Insuficiente: aceita os 85% como nível de proteção.

### Questão 10

**Resposta esperada**

a) ALE atual = 0,10 × 12.000.000 = **R$ 1.200.000**. ALE com o programa = 0,04 × 12.000.000 = **R$ 480.000**. Redução = R$ 720.000. ROSI = (720.000 − 400.000) ÷ 400.000 = **80%**. Limitações: a perda e as probabilidades são **premissas** estimadas, e pequenas variações mudam o resultado (se a probabilidade final fosse 7%, a redução seria R$ 360.000 e o ROSI ficaria negativo, −10%); o cálculo ignora impactos difíceis de quantificar (reputação, sanções regulatórias, segurança operacional da produção 24 h) e benefícios indiretos (maturidade, conformidade). Por isso, deve ser apresentado com cenários (otimista, conservador) e acompanhado de indicadores que permitam revisar as premissas.

b) Estrutura sugerida para o ano 1, vinculada à governança (CSF 2.0, função Governar) e a um roteiro (*roadmap*) priorizado:

- **Primeiro trimestre**: exercício ***tabletop*** com diretoria, TI, jurídico, comunicação e produção (baixo custo, testa decisões e papéis) e teste completo de restauração de *backup*. *Injects*: (1) servidores de produção criptografados numa sexta-feira à noite, com a linha parada — quem decide parar ou isolar?; (2) constatação de que os *backups* também foram afetados ou não restauram no tempo necessário; (3) confirmação de exfiltração de dados pessoais de colaboradores — acionamento do encarregado e prazo de três dias úteis à ANPD; (4) pedido de resgate e contato da imprensa.
- **Blue Team / engenharia de detecção**: corrigir as lacunas apontadas, revisar e testar o plano de resposta e os *playbooks*, reduzir o ruído do SIEM.
- **Purple Team**: ciclos trimestrais de emulação das técnicas de grupos de *ransomware* que atacam a indústria (planejar, executar, observar, ajustar, retestar).
- **Red Team**: operação anual orientada a objetivo (por exemplo, alcançar o ambiente de produção), executada após a maturidade básica, para verificar se a organização detecta e responde, com relatório que alimenta o ciclo seguinte.
- **Indicadores**: cobertura ATT&CK testada sobre técnicas priorizadas, MTTD e MTTR medianos, precisão dos alertas, pontuação do *tabletop* (e sua evolução no exercício seguinte), tempo real de restauração comparado ao objetivo e percentual de ações de melhoria concluídas e retestadas.

A resposta deve mostrar o encadeamento: o *tabletop* e o teste de *backup* atacam as fragilidades mais urgentes; o *purple teaming* transforma conhecimento ofensivo em detecção; o Red Team valida o conjunto; e os indicadores alimentam a revisão das premissas do ROSI.

**Critérios de correção**

- Integral: calcula corretamente ALE atual, ALE com o programa e ROSI de 80%; discute ao menos duas limitações (premissas, sensibilidade, impactos não quantificados); propõe programa que integra Red, Blue e Purple Team em sequência coerente; apresenta ao menos três *injects* ligados às fragilidades (*backup*, plano não exercitado, comunicação/LGPD, decisão operacional); define indicadores mensuráveis de evolução.
- Parcial: cálculos corretos com programa genérico, ou programa bem estruturado com erro de cálculo ou sem discussão das limitações; *injects* desconectados do cenário.
- Insuficiente: apenas cálculos, ou apenas lista de ferramentas, sem integração entre as frentes.
