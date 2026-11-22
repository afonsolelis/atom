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

**1.** I. Na contenção do incidente no servidor do ERP, o *playbook* determina isolar o servidor pelo EDR, mantendo-o ligado, em vez de desligá-lo.

PORQUE

II. Desligar o servidor apaga a memória volátil, onde ficam processos e conexões ativas que servem de evidência para a investigação.

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**2.** I. O NIST SP 800-61 Rev. 3, publicado em 2025, organiza as recomendações de resposta a incidentes como um perfil do CSF 2.0, distribuindo-as pelas funções Governar, Identificar, Proteger, Detectar, Responder e Recuperar.

PORQUE

II. A Rev. 3 eliminou a preparação do ciclo de resposta, que passou a começar na função Detectar, no momento em que surge o primeiro alerta.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**3.** I. Pela Resolução CD/ANPD nº 15/2024, o prazo de três dias úteis para comunicar um incidente à ANPD começa a contar quando a investigação técnica é concluída e o relatório final é aprovado.

PORQUE

II. A mesma resolução dispensa o controlador de manter o registro do incidente sempre que a comunicação à ANPD é feita dentro do prazo.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

**4.** I. Na resposta a incidentes, um alerta é a sinalização, gerada por uma regra, de que um evento pode ser malicioso, e não equivale automaticamente à declaração de um incidente.

PORQUE

II. No Wazuh, as regras atribuem a cada alerta um nível de 0 a 15, e o módulo de *active response* pode executar ações configuradas, como bloquear um endereço no *firewall* do *host*.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**5.** I. Na fase de recuperação, a equipe deve restaurar sempre o *backup* mais recente disponível, mesmo que ele tenha sido feito depois do primeiro evento malicioso, para minimizar a perda de dados.

PORQUE

II. Um *backup* feito depois do comprometimento pode conter a ferramenta ou a persistência deixada pelo invasor.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**6.** I. Na coleta de evidências de um servidor comprometido, a imagem do disco deve ser produzida antes da cópia da memória RAM, porque o disco concentra o maior volume de dados.

PORQUE

II. Segundo a RFC 3227, a coleta de evidências deve seguir da evidência mais volátil para a menos volátil.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**7.** I. O *hash* SHA-256 calculado no momento da coleta e conferido na entrega da evidência permite demonstrar que o arquivo não foi alterado no caminho.

PORQUE

II. A cadeia de custódia registra, para cada evidência, quem a coletou, quando, como e onde ela ficou guardada, além de cada transferência de mãos.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**8.** I. Ao montar a linha do tempo de um incidente, os carimbos de tempo de todas as fontes devem ser convertidos para um mesmo referencial, como o UTC.

PORQUE

II. Fontes diferentes podem registrar horários em fusos distintos, como uma VPN que grava em UTC e um controlador de domínio que grava em horário de Brasília, e a mistura sem conversão produz uma ordem de eventos falsa.

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**9.** I. Quando o tráfego entre um servidor e um endereço externo é cifrado com TLS, a captura de pacotes (*pcap*) desse tráfego não tem valor como evidência na investigação.

PORQUE

II. O Wireshark só exibe informações de pacotes cujo conteúdo esteja em texto claro.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

**10.** I. Durante a contenção, isolar pela rede um servidor comprometido, mantendo-o ligado, é preferível a desligá-lo da tomada.

PORQUE

II. Desligar o servidor preserva o conteúdo da memória RAM, desde que a imagem do disco seja feita logo em seguida.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**11.** I. Em um exercício *purple team*, o Blue Team não deve saber quais técnicas serão executadas nem quando, para que a reação dos defensores seja avaliada em condições realistas.

PORQUE

II. O objetivo principal do exercício *purple team* é medir se o Red Team consegue alcançar os objetivos da operação sem ser percebido pelo SOC.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

**12.** I. No ciclo emular, observar, ajustar e retestar, uma técnica só pode ser contabilizada como detectada depois que o mesmo caso de teste é repetido e gera o alerta esperado.

PORQUE

II. Uma regra ligada e nunca retestada é apenas uma hipótese: ela pode ter erro de lógica, depender de um registro que não é coletado ou disparar tarde demais.

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**13.** I. Na sessão *purple* da Rede Tatame de 10/12/2026, a técnica T1567.002 passou a contar na cobertura testada depois do reteste, porque a fonte de saída de rede foi ligada e a regra R9 gerou alerta.

PORQUE

II. A cobertura testada considera apenas as técnicas cujo alerta chegou dentro do critério de tempo combinado antes do exercício.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**14.** I. Os casos de teste de um exercício *purple team* devem usar contas de teste, dados sintéticos e máquinas descartáveis, dentro de uma autorização escrita que defina escopo e janela.

PORQUE

II. Como o exercício *purple* é interno e o Blue Team sabe do teste, a autorização formal e a definição de escopo deixam de ser necessárias.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**15.** I. Ao fim de uma sessão *purple*, a visibilidade (técnicas com telemetria ÷ técnicas do plano) pode ser maior que a cobertura testada (técnicas com alerta dentro do critério ÷ técnicas do plano).

PORQUE

II. O Apache Caldera, criado pela MITRE, é uma plataforma que automatiza a execução de planos de emulação de adversários.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**16.** I. O sumário executivo do relatório final deve caber em uma página e usar linguagem de negócio, com risco, decisões pedidas, donos e prazos.

PORQUE

II. No relatório técnico, cada achado deve trazer o identificador da técnica do MITRE ATT&CK correspondente, o que liga o achado à cobertura e ao próximo exercício.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**17.** I. Em uma matriz de risco com escalas de 1 a 5, um achado com probabilidade 2 e impacto 4 tem o mesmo risco que um achado com probabilidade 4 e impacto 5.

PORQUE

II. Na matriz de probabilidade e impacto, o risco é calculado pela soma das duas notas, o que torna equivalentes achados com notas trocadas.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

**18.** I. Uma recomendação cuja regra de detecção já foi ligada, mas ainda não foi testada contra a técnica, não deve ser registrada no relatório final como achado corrigido.

PORQUE

II. Ligar a fonte de telemetria e a regra correspondente é suficiente para comprovar que a técnica será detectada, dispensando o reteste.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**19.** I. Na ordem de execução das recomendações, um achado de risco alto que exige meses de trabalho, como segmentar a rede da sede, pode ficar atrás de achados de risco semelhante e correção rápida.

PORQUE

II. Ao usar a prioridade igual ao risco dividido pelo esforço, a priorização favorece as correções que reduzem muito risco com pouco trabalho, os chamados ganhos rápidos.

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**20.** I. Para que as métricas do relatório final sejam objetivas, o desempenho do SOC deve ser cobrado exclusivamente pela redução do MTTR, dispensando outros indicadores.

PORQUE

II. Segundo a Lei de Goodhart, quando uma medida se torna meta, ela tende a deixar de ser uma boa medida, pois as pessoas passam a otimizar o número em vez do resultado.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Interpretação

**21.** Em um incidente na Rede Tatame, o primeiro evento malicioso (um *login* indevido) ocorreu às 08:12:30. Uma regra gerou alerta às 08:20:00, mas a triagem só aconteceu às 09:40:00, quando o caso foi aberto. A contenção, com isolamento do servidor e bloqueio da conta, foi concluída às 10:05:00. Considerando que o MTTD é medido do primeiro evento até a abertura do caso e o MTTR, da abertura do caso até a contenção, quais são esses tempos?

a. MTTD de 7 min 30 s e MTTR de 1 h 45 min.
b. MTTD de 1 h 20 min e MTTR de 25 min.
*c. MTTD de 1 h 27 min 30 s e MTTR de 25 min.
d. MTTD de 1 h 27 min 30 s e MTTR de 1 h 52 min 30 s.
e. MTTD de 1 h 52 min 30 s e MTTR de 25 min.

**22.** Uma rede de academias, que não é agente de tratamento de pequeno porte, confirmou na sexta-feira, 4 de dezembro de 2026, que um incidente de segurança afetou dados pessoais de alunos e pode acarretar risco relevante a eles. Não há feriados no período. De acordo com a Resolução CD/ANPD nº 15/2024, até que data a comunicação à ANPD deve ser feita?

a. 7 de dezembro de 2026 (segunda-feira).
b. 6 de dezembro de 2026 (domingo).
c. 8 de dezembro de 2026 (terça-feira).
d. 14 de dezembro de 2026 (segunda-feira).
*e. 9 de dezembro de 2026 (quarta-feira).

**23.** O coordenador de incidentes de uma empresa usa a pontuação prioridade = criticidade do ativo (1 a 5) × confiança na detecção (1 a 3) × abrangência (1 a 3). Três incidentes estão abertos:

| Incidente | Criticidade | Confiança | Abrangência |
|---|---|---|---|
| X — servidor de arquivos com exclusão de cópias de sombra em vários *hosts* | 4 | 3 | 3 |
| Y — banco de dados de alunos com processo desconhecido | 5 | 2 | 1 |
| Z — notebook da diretoria conectado a destino suspeito | 3 | 3 | 2 |

Qual é a ordem de atendimento indicada pela pontuação?

*a. X (36), Z (18) e Y (10).
b. Y (10), X (36) e Z (18).
c. X (36), Y (10) e Z (18).
d. Z (18), X (36) e Y (10).
e. Y (10), Z (18) e X (36).

**24.** Durante um incidente com ferramenta de acesso remoto não aprovada, a equipe realizou as atividades abaixo:

1. Confirmar o alerta e definir quais máquinas e contas estão envolvidas.
2. Isolar o servidor pelo EDR e bloquear o endereço de destino.
3. Remover a ferramenta, redefinir as credenciais usadas e corrigir a porta de entrada.
4. Restaurar o servidor a partir de *backup* íntegro e monitorá-lo com atenção redobrada.

Segundo o NIST SP 800-61 Rev. 2, as atividades 1, 2, 3 e 4 correspondem, respectivamente, a:

a. preparação, detecção, contenção e recuperação.
b. detecção e análise, erradicação, contenção e atividade pós-incidente.
c. contenção, detecção e análise, recuperação e erradicação.
*d. detecção e análise, contenção, erradicação e recuperação.
e. detecção e análise, contenção, recuperação e atividade pós-incidente.

**25.** Ao revisar um *playbook* antigo de resposta a incidentes, uma analista encontrou as etapas na seguinte ordem: triagem; isolar o servidor; remover a ferramenta e redefinir credenciais; preservar evidências; acionar coordenador e jurídico; restaurar *backup*. Qual é o problema mais grave dessa sequência, segundo o que foi estudado na Aula 13?

a. O isolamento do servidor deveria ser feito apenas depois da restauração do *backup*.
*b. A preservação de evidências vem depois da erradicação, o que pode destruir os rastros necessários à investigação.
c. A triagem deveria ser eliminada, porque todo alerta de severidade alta já é um incidente declarado.
d. O jurídico não deveria ser acionado, porque a comunicação à ANPD é tarefa exclusiva da equipe técnica.
e. A restauração de *backup* não faz parte do ciclo de resposta a incidentes do NIST.

**26.** Na investigação de um incidente na Rede Tatame, a VPN registrou o *login* da conta usada pelo invasor como `2026-12-02T01:58:10Z` (UTC). O Active Directory, que grava em horário de Brasília (UTC−3), registrou o evento 4624 tipo 10 (RDP) dessa mesma conta no servidor do ERP em `01/12/2026 23:06:42`. Considerando os dois registros corretamente normalizados, qual é a relação entre os eventos?

a. O RDP ocorreu 3 h 08 min 32 s depois do *login* na VPN.
*b. O RDP ocorreu 8 min 32 s depois do *login* na VPN.
c. O RDP ocorreu 2 h 51 min 28 s antes do *login* na VPN, o que indica dois invasores diferentes.
d. Os dois eventos ocorreram no mesmo segundo, pois a diferença corresponde exatamente ao fuso horário.
e. Não é possível relacionar os eventos sem conhecer o fuso do sensor de rede.

**27.** Uma analista de SOC precisa coletar evidências de um servidor comprometido, já isolado pela rede e mantido ligado. Ela tem quatro itens a coletar: (1) imagem do disco de 512 GB; (2) lista de processos e de conexões de rede ativas; (3) cópia da memória RAM; (4) exportação dos registros do SIEM, armazenados em outro servidor. Qual sequência segue a ordem de volatilidade da RFC 3227?

a. 1, 3, 2, 4.
b. 4, 2, 3, 1.
c. 3, 1, 2, 4.
*d. 2, 3, 1, 4.
e. 1, 2, 3, 4.

**28.** Ao receber as evidências de um incidente, uma perita externa recalcula o *hash* SHA-256 da cópia da memória RAM e obtém um valor diferente do registrado no formulário de cadeia de custódia no momento da coleta. Os outros quatro arquivos conferem. Qual é a conduta adequada?

a. Considerar a diferença irrelevante, já que quatro das cinco evidências conferem.
b. Recalcular o *hash* com outro algoritmo, como o MD5, e usar o novo valor no formulário.
c. Substituir o valor antigo no formulário pelo novo, para que a conferência passe a dar "OK".
d. Analisar normalmente a memória, pois o *hash* serve apenas para identificar o arquivo, e não para provar integridade.
*e. Registrar a divergência, investigar sua causa e não tratar essa cópia como idêntica à coletada, pois a integridade dela não pode ser comprovada.

**29.** No *pcap* do sensor de rede, um analista filtrou os pacotes *Client Hello* trocados entre o servidor do ERP e o endereço 198.51.100.77 e acrescentou uma coluna com o tempo desde o pacote exibido anterior:

| Horário (UTC) | Tempo desde o anterior (s) |
|---|---|
| 05:30:00 | 300,0 |
| 05:35:00 | 300,0 |
| 05:37:00 | 119,8 |
| 05:40:00 | 180,2 |
| 05:45:00 | 300,0 |

O fluxo aberto às 05:37:00 durou 1.680 s e enviou cerca de 2,9 GB do servidor para o endereço externo. Qual interpretação é mais adequada?

*a. As conexões a cada 300 s indicam o *beacon* de uma ferramenta de acesso remoto; a conexão fora do ritmo, às 05:37, abre um fluxo de saída de dados compatível com a exfiltração, mesmo com o conteúdo cifrado.
b. Como o tráfego é TLS, a tabela não permite nenhuma conclusão sobre o incidente.
c. O intervalo de 300 s comprova que o tráfego é legítimo, pois programas maliciosos se conectam em intervalos aleatórios.
d. A conexão das 05:37 é um falso positivo, porque ocorreu fora do intervalo de 300 s.
e. O volume de 2,9 GB indica um ataque de negação de serviço contra o endereço externo.

**30.** A linha do tempo de um incidente, normalizada em horário de Brasília, registra: primeiro evento do invasor (*login* na VPN) às 22:58:10; alerta da regra de detecção às 23:14:40; triagem do alerta e abertura do caso às 03:20:00 do dia seguinte; contenção às 03:41:00. Considerando MTTD como o tempo do primeiro evento até a abertura do caso e MTTR como o tempo da abertura do caso até a contenção, qual afirmação está correta?

a. O MTTD foi de 16 min 30 s, e o MTTR, de 4 h 26 min 20 s.
b. O MTTD foi de 4 h 05 min 20 s, e o MTTR, de 42 min 50 s.
*c. O MTTD foi de 4 h 21 min 50 s, dos quais 4 h 05 min 20 s foram de alerta à espera de triagem, e o MTTR foi de 21 min.
d. O MTTD foi de 4 h 42 min 50 s, e o MTTR, de 21 min.
e. O MTTD foi de 21 min, e o MTTR, de 4 h 21 min 50 s.

**31.** Uma rede de clínicas validou, em uma sessão *purple*, um plano com 8 técnicas ATT&CK, com o critério "alerta na fila do SOC em até 5 minutos". O facilitador registrou: 3 técnicas geraram alerta em menos de 2 minutos; 2 técnicas geraram telemetria, mas nenhum alerta; 1 técnica gerou telemetria e alerta, mas o alerta chegou em 7 minutos; 2 técnicas não geraram nenhum evento. Quais são, respectivamente, a cobertura testada e a visibilidade dessa primeira execução?

a. 50% e 75%.
b. 37,5% e 62,5%.
c. 75% e 75%.
*d. 37,5% e 75%.
e. 62,5% e 100%.

**32.** Após um exercício *purple*, a equipe gerou uma *layer* do ATT&CK Navigator. Para uma das técnicas, o arquivo traz: `"techniqueID": "T1567.002"`, `"score": 50`, `"color": "#F2CB0A"` e `"comment": "parcial | regra R9 | alerta em 540 s; critério: 300 s"`. Na legenda da *layer*, 100 significa detectado dentro do critério, 50 significa parcial e 0 significa sem visibilidade. Qual interpretação está correta?

*a. A técnica já gera telemetria e alerta, mas o alerta chegou depois do limite combinado; por isso conta na visibilidade e não na cobertura testada.
b. A técnica não gera nenhuma telemetria, e a cor amarela indica que a fonte de dados está desligada.
c. A técnica ficou fora do plano de emulação e aparece na *layer* apenas como referência.
d. A técnica foi detectada dentro do critério, mas só em metade dos procedimentos possíveis, o que justifica a pontuação 50.
e. O arquivo está mal formado, porque o Navigator só aceita pontuações 0 ou 100.

**33.** Na Rede Tatame, o engenheiro de detecção ligou a regra R5 (RDP de estação para servidor) durante a sessão *purple*. No simulador, a técnica T1021.001 passou de "parcial" para "detectável", e a "cobertura com regra" subiu imediatamente. Um diretor pede que a técnica já seja registrada como coberta no relatório. Qual deve ser o próximo passo?

a. Registrar a técnica como coberta, pois a regra está ativa e a fonte de dados está ligada.
b. Desligar a R5 até o próximo exercício, para evitar alertas de manutenção.
*c. Repetir o mesmo caso de teste da T1021.001 e conferir se o alerta chega dentro do critério combinado, antes de registrá-la como comprovada.
d. Aguardar um ataque real para confirmar que a regra funciona.
e. Ampliar o plano para todas as técnicas da matriz antes de registrar qualquer resultado.

**34.** Depois de um incidente, a diretoria de uma rede de academias quer verificar, com baixo custo, se está claro quem decide isolar o servidor do ERP em horário comercial, quem aciona o jurídico e quem comunica a autoridade de proteção de dados. Participarão diretores, jurídico, comunicação e TI, e nenhum sistema deve ser tocado. Qual formato de exercício atende melhor a esse objetivo?

a. *Cyber range*, com uma rede virtual que reproduz o ERP.
*b. *Tabletop*, com um cenário apresentado em etapas e *injects* que forçam decisões.
c. CTF no formato *jeopardy*, com desafios de forense.
d. Exercício *purple* técnica a técnica, com casos de teste no ERP.
e. Operação de Red Team sem aviso prévio aos defensores.

**35.** Em uma sessão *purple*, as equipes começaram a discutir longamente se uma exceção da regra R5 deveria incluir um segundo servidor de salto. A sessão já estava atrasada, três técnicas ainda não tinham sido executadas e ninguém havia anotado quem faria o ajuste. Segundo o PTEF, qual papel deve intervir para manter o tempo e transformar a discussão em tarefa com dono e prazo?

a. O líder do Red Team, que decide quais técnicas podem ser puladas.
b. A CISO, que assinou a autorização do exercício.
c. O analista de SOC de plantão, que acompanha os alertas.
d. A perita forense externa, que guarda as evidências.
*e. O facilitador, que conduz a sessão, controla o tempo e registra as ações de melhoria.

**36.** Uma rede de academias classifica o risco de seus achados de segurança pelo produto entre probabilidade e impacto, ambos em escala de 1 a 5, com as faixas: 15 ou mais, crítico; 10 a 14, alto; 5 a 9, médio; 1 a 4, baixo. A ordem de execução usa a prioridade igual ao risco dividido pelo esforço (1 = dias, 2 = semanas, 3 = meses). Um achado indica que o servidor do ERP pode ser alcançado diretamente pela VPN, com probabilidade 3, impacto 4 e esforço 3, porque a correção exige segmentar a rede. Qual é o risco, a classe e a prioridade desse achado?

a. Risco 7, classe médio e prioridade 2,3.
b. Risco 12, classe crítico e prioridade 4.
c. Risco 12, classe alto e prioridade 36.
d. Risco 7, classe baixo e prioridade 21.
*e. Risco 12, classe alto e prioridade 4.

**37.** O relatório final de um incidente define o MTTD como o tempo entre o primeiro evento malicioso e a abertura do caso pelo SOC, e o MTTR como o tempo entre a abertura do caso e a contenção. Os marcos registrados foram: primeiro evento às 22h58min10s do dia 1º; alerta da regra às 23h14min40s do dia 1º; abertura do caso às 03h20min00s do dia 2; contenção às 03h41min00s do dia 2. Quais são o MTTD e o MTTR desse incidente?

a. MTTD de 16 min 30 s e MTTR de 4 h 26 min 20 s.
b. MTTD de 4 h 05 min 20 s e MTTR de 21 min.
*c. MTTD de 4 h 21 min 50 s e MTTR de 21 min.
d. MTTD de 4 h 21 min 50 s e MTTR de 4 h 42 min 50 s.
e. MTTD de 16 min 30 s e MTTR de 21 min.

**38.** A CISO de uma rede de academias vai apresentar à diretoria o relatório final de um incidente e de um exercício *purple team*. A diretoria pediu um sumário executivo de uma página. Qual dos trechos a seguir é o mais adequado para esse sumário?

a. "Às 23h06min42s houve um evento 4624 com tipo de *logon* 10 no SRV-ERP-01, originado do endereço da VPN, sem disparo da regra R5."
*b. "Pedimos aprovar nesta semana o segundo fator mais forte na VPN, com dono e prazo definidos, e aceitar formalmente, até março, o risco da rede da sede ainda não segmentada."
c. "A regra proposta usa a condição event_id == 4624 and logon_type == 10 com exceção para o servidor de salto."
d. "Os *hashes* SHA-256 das imagens de memória e de disco estão listados no anexo de cadeia de custódia."
e. "A tabela a seguir mostra todas as técnicas do ATT&CK com seus identificadores e o estado de cada regra no motor de correlação."

**39.** Uma equipe de segurança precisa ordenar quatro recomendações abertas usando a prioridade igual ao risco dividido pelo esforço:

| Achado | Risco (probabilidade × impacto) | Esforço |
|---|---|---|
| X — MFA por *push* sem correspondência de número | 20 | 1 |
| Y — dados pessoais completos em planilhas exportadas | 16 | 2 |
| Z — ambiente de homologação exposto sem WAF | 15 | 1 |
| W — servidor crítico sem segmentação de rede | 12 | 3 |

Qual é a ordem de execução, da maior para a menor prioridade?

a. X, Y, Z, W.
b. W, Y, Z, X.
c. Z, X, Y, W.
*d. X, Z, Y, W.
e. X, Z, W, Y.

**40.** Após um incidente, uma equipe priorizou quatro técnicas do MITRE ATT&CK e registrou o estado de cada uma: T1078 tem telemetria, mas nenhuma regra; T1021.001 e T1219 têm regra ativa e foram testadas com sucesso em um exercício *purple*; T1567.002 teve a fonte de telemetria e a regra ligadas, mas ainda não foi testada. Considerando que a cobertura testada conta só as técnicas com detecção comprovada e que a visibilidade conta as técnicas com telemetria disponível, quais são esses dois indicadores?

*a. Cobertura testada de 50% e visibilidade de 100%.
b. Cobertura testada de 75% e visibilidade de 100%.
c. Cobertura testada de 50% e visibilidade de 75%.
d. Cobertura testada de 75% e visibilidade de 75%.
e. Cobertura testada de 25% e visibilidade de 100%.

## Gabarito e feedbacks

**Questão 1** (correta: a)
- a. Correta: as duas são verdadeiras, e a II explica a I. Isolar corta a rede e interrompe o dano, mas mantém a máquina ligada, preservando a memória volátil que desligar apagaria.
- b. Incorreta: a II é exatamente o motivo da instrução da I; há relação de justificativa entre elas.
- c. Incorreta: a II é verdadeira; a memória volátil guarda processos e conexões que se perdem quando o servidor é desligado.
- d. Incorreta: a I é verdadeira; o *playbook* estudado manda isolar, e não desligar.
- e. Incorreta: as duas asserções são verdadeiras; reveja a tensão entre contenção e evidência na Aula 13.

**Questão 2** (correta: c)
- a. Incorreta: a II é falsa; a preparação continua existindo e se distribui pelas funções Governar, Identificar e Proteger.
- b. Incorreta: a II não é verdadeira, pois a Rev. 3 não eliminou a preparação.
- c. Correta: a I é verdadeira, pois a Rev. 3 é um perfil do CSF 2.0; a II é falsa, pois a preparação passa a corresponder a Governar, Identificar e Proteger.
- d. Incorreta: a I é verdadeira; a Rev. 3, de abril de 2025, organiza a resposta nas seis funções do CSF 2.0.
- e. Incorreta: só a II é falsa; reveja a tabela que relaciona as fases da Rev. 2 às funções do CSF 2.0.

**Questão 3** (correta: e)
- a. Incorreta: as duas asserções são falsas; o prazo não depende do fim da investigação, e o registro não é dispensado.
- b. Incorreta: nenhuma das duas é verdadeira; reveja os arts. 6º e 10 da Resolução CD/ANPD nº 15/2024.
- c. Incorreta: a I é falsa, pois o prazo conta do conhecimento de que o incidente afetou dados pessoais.
- d. Incorreta: a II é falsa, pois o controlador deve manter o registro do incidente por no mínimo cinco anos.
- e. Correta: a I é falsa, porque os três dias úteis contam do conhecimento, e não do fim da investigação; a II é falsa, porque o registro do incidente é obrigatório por pelo menos cinco anos.

**Questão 4** (correta: b)
- a. Incorreta: as duas são verdadeiras, mas os níveis e a *active response* do Wazuh não explicam a diferença conceitual entre alerta e incidente.
- b. Correta: a I é verdadeira (alerta é sinalização; incidente é decisão formal após a análise) e a II também (níveis de 0 a 15 e *active response*), mas a II descreve uma ferramenta, sem justificar a I.
- c. Incorreta: a II é verdadeira; essas são características documentadas do Wazuh.
- d. Incorreta: a I é verdadeira; declarar um incidente é uma decisão formal tomada depois da triagem do alerta.
- e. Incorreta: as duas asserções são verdadeiras; o erro está apenas em buscar relação de causa entre elas.

**Questão 5** (correta: d)
- a. Incorreta: a I é falsa; a recuperação usa *backup* íntegro, anterior ao comprometimento.
- b. Incorreta: a I não é verdadeira, e a II, que é verdadeira, contradiz a I em vez de justificá-la.
- c. Incorreta: a I é falsa e a II é verdadeira, e não o contrário.
- d. Correta: a I é falsa, porque restaurar um *backup* posterior ao primeiro evento pode trazer o invasor de volta; a II é verdadeira e é justamente o motivo para escolher um *backup* anterior, como o de 01/12 às 20:00 no caso da Rede Tatame.
- e. Incorreta: a II é verdadeira; um *backup* feito depois do comprometimento pode conter a ferramenta ou a persistência.

**Questão 6** (correta: d)
- a. Incorreta: a I é falsa; o disco é menos volátil e deve ser coletado depois da memória, independentemente do volume de dados.
- b. Incorreta: a I é falsa; o tamanho do disco não define a ordem de coleta, e sim a volatilidade de cada evidência.
- c. Incorreta: a I é que é falsa, e a II é verdadeira; reveja a ordem de volatilidade da RFC 3227 (Aula 14).
- d. Correta: a I é falsa, porque a memória RAM, mais volátil, se perde primeiro e deve ser coletada antes do disco; a II é verdadeira e descreve exatamente a recomendação da RFC 3227.
- e. Incorreta: a II é verdadeira; a RFC 3227 recomenda ir da evidência mais volátil para a menos volátil.

**Questão 7** (correta: b)
- a. Incorreta: as duas são verdadeiras, mas o que prova que o arquivo não mudou é a propriedade do *hash* (qualquer alteração gera outro valor), e não o registro de quem, quando e onde descrito na II.
- b. Correta: a I é verdadeira, pois o *hash* conferido na entrega demonstra a integridade; a II também é verdadeira, pois descreve o conteúdo do formulário de custódia; mas a II não explica a I, já que são mecanismos complementares, e não causa e efeito.
- c. Incorreta: a II é verdadeira; o formulário de custódia registra o quê, quem, quando, como, onde e cada transferência.
- d. Incorreta: a I é verdadeira; o SHA-256 recalculado e comparado com o valor da coleta comprova que o arquivo não foi alterado.
- e. Incorreta: as duas asserções são verdadeiras; reveja cadeia de custódia e *hash* na Aula 14.

**Questão 8** (correta: a)
- a. Correta: a I é verdadeira, pois a linha do tempo exige um referencial único de horário; a II é verdadeira e explica a I, já que fontes em fusos diferentes, sem conversão, produzem ordens impossíveis, como um acesso pela VPN anterior ao próprio *login* na VPN.
- b. Incorreta: a II é justamente o motivo da normalização descrita na I.
- c. Incorreta: a II é verdadeira; no incidente da Aula 14, a VPN gravava em UTC e o AD em horário de Brasília.
- d. Incorreta: a I é verdadeira; normalizar para UTC é o cuidado central da linha do tempo.
- e. Incorreta: as duas asserções são verdadeiras; reveja a linha do tempo e a *super timeline* na Aula 14.

**Questão 9** (correta: e)
- a. Incorreta: as duas asserções são falsas; o *pcap* de tráfego cifrado continua sendo evidência pelos metadados.
- b. Incorreta: nenhuma das asserções é verdadeira; o Wireshark exibe endereços, portas, tamanhos e horários mesmo de tráfego TLS.
- c. Incorreta: a I é falsa; quem falou com quem, quando, com que regularidade e quanto foi enviado são informações valiosas mesmo sem ler o conteúdo.
- d. Incorreta: a II é falsa; o Wireshark exibe os cabeçalhos e os metadados de pacotes cifrados, apenas não mostra o conteúdo em texto claro.
- e. Correta: a I é falsa, porque os metadados do tráfego cifrado confirmam destino, ritmo e volume, como o *beacon* e os 2,8 GB do incidente; a II é falsa, porque o Wireshark mostra as informações de cabeçalho de qualquer pacote capturado.

**Questão 10** (correta: c)
- a. Incorreta: a II é falsa; desligar o servidor apaga a memória RAM, e nenhuma cópia posterior do disco a recupera.
- b. Incorreta: a II não é verdadeira; a memória é volátil e se perde quando a máquina é desligada.
- c. Correta: a I é verdadeira, pois o isolamento pela rede interrompe o ataque e mantém a memória disponível para coleta; a II é falsa, pois desligar o servidor apaga a memória RAM, onde estão processos, conexões e chaves de sessão.
- d. Incorreta: a I é verdadeira; isolar e manter ligado é o que o *playbook* recomenda para preservar evidências.
- e. Incorreta: a I é verdadeira; só a II é falsa.

**Questão 11** (correta: e)
- a. Incorreta: as duas asserções são falsas; no exercício *purple* o Blue Team sabe o que será executado, e o objetivo não é passar despercebido.
- b. Incorreta: nenhuma das asserções é verdadeira; reveja a diferença entre operação de Red Team tradicional e exercício *purple* (Aula 15).
- c. Incorreta: a I é falsa; quem normalmente não sabe do teste é o Blue Team em uma operação de Red Team tradicional, e não no exercício *purple*.
- d. Incorreta: a II é falsa; medir se o Red Team alcança os objetivos sem ser percebido é próprio da operação tradicional. No *purple*, o objetivo é aprender rápido e comprovar a melhoria.
- e. Correta: a I é falsa, pois no exercício *purple* os defensores sabem o que será executado e quando; a II é falsa, pois o objetivo é validar telemetria, alerta, tempo e resposta, técnica a técnica, e ajustar a defesa na própria sessão.

**Questão 12** (correta: a)
- a. Correta: as duas são verdadeiras, e a II explica a I; como uma regra nunca retestada pode falhar por vários motivos, só o reteste do mesmo caso de teste comprova a detecção.
- b. Incorreta: a II é justamente o motivo pelo qual o reteste é exigido na I.
- c. Incorreta: a II é verdadeira; regra ligada sem reteste continua sendo hipótese.
- d. Incorreta: a I é verdadeira; o ciclo só se completa com o reteste.
- e. Incorreta: as duas asserções são verdadeiras; reveja o ciclo emular, observar, ajustar e retestar.

**Questão 13** (correta: d)
- a. Incorreta: a I é falsa; a T1567.002 ganhou telemetria e alerta, mas o alerta chegou em 540 s, acima do limite de 300 s, e ela não entrou na cobertura testada.
- b. Incorreta: a I é falsa; a técnica ficou como parcial após o reteste.
- c. Incorreta: a I é falsa e a II é verdadeira, e não o contrário.
- d. Correta: a I é falsa, porque o alerta da R9 veio fora do critério e a técnica ficou parcial (cobertura testada de 5/6); a II é verdadeira, pois a cobertura testada só conta alertas dentro do critério de tempo.
- e. Incorreta: a II é verdadeira; o critério de sucesso inclui o tempo até o alerta.

**Questão 14** (correta: c)
- a. Incorreta: a II é falsa; mesmo em exercício interno, autorização e escopo por escrito são obrigatórios.
- b. Incorreta: a II não é verdadeira; o fato de o Blue Team saber do teste não dispensa a autorização.
- c. Correta: a I é verdadeira, pois casos de teste inofensivos geram o rastro da técnica sem causar dano, dentro de uma autorização como a APR-3107; a II é falsa, pois a regra da Unidade 1 vale para qualquer atividade ofensiva, inclusive interna.
- d. Incorreta: a I é verdadeira; casos de teste devem ser inofensivos e autorizados.
- e. Incorreta: a I é verdadeira; só a II é falsa.

**Questão 15** (correta: b)
- a. Incorreta: as duas são verdadeiras, mas a existência do Caldera não explica por que a visibilidade pode superar a cobertura testada.
- b. Correta: a I é verdadeira, pois uma técnica pode gerar telemetria sem gerar alerta, ou gerar alerta fora do critério; a II é verdadeira, mas trata de uma ferramenta de automação e não justifica a I.
- c. Incorreta: a II é verdadeira; o Apache Caldera, criado pela MITRE, automatiza a emulação de adversários.
- d. Incorreta: a I é verdadeira; na sessão da Rede Tatame, a visibilidade foi de 100% e a cobertura testada de 83% após o reteste.
- e. Incorreta: as duas asserções são verdadeiras.

**Questão 16** (correta: b)
- a. Incorreta: as duas asserções são verdadeiras, mas a presença do identificador ATT&CK no relatório técnico não explica por que o sumário executivo tem uma página e linguagem de negócio; são camadas diferentes do mesmo relatório.
- b. Correta: o sumário executivo é escrito para a diretoria, em uma página, com risco, decisão, dono e prazo; o relatório técnico traz a técnica ATT&CK de cada achado. As duas afirmações são verdadeiras, mas tratam de públicos distintos, e a II não justifica a I.
- c. Incorreta: a II é verdadeira; o identificador ATT&CK é um dos campos mínimos do achado no relatório técnico (Aula 16).
- d. Incorreta: a I é verdadeira; a diretoria pede uma página em linguagem de negócio, sem identificadores técnicos.
- e. Incorreta: as duas asserções são verdadeiras; reveja a diferença entre relatório técnico e sumário executivo.

**Questão 17** (correta: e)
- a. Incorreta: as duas asserções são falsas; o risco é o produto das notas, e os dois achados têm riscos 8 e 20.
- b. Incorreta: nenhuma das asserções é verdadeira; 2 × 4 = 8 e 4 × 5 = 20 caem em classes diferentes (médio e crítico).
- c. Incorreta: a I é falsa, pois os riscos são diferentes (8 e 20).
- d. Incorreta: a II é falsa; na matriz estudada, o risco é a multiplicação, e não a soma, da probabilidade pelo impacto.
- e. Correta: a I é falsa, porque 2 × 4 = 8 (médio) e 4 × 5 = 20 (crítico); a II é falsa, porque o risco é o produto das notas, e mesmo pela soma os valores seriam diferentes (6 e 9).

**Questão 18** (correta: c)
- a. Incorreta: a II é falsa; regra ligada sem teste é uma hipótese, e por isso a I é verdadeira.
- b. Incorreta: a II não é verdadeira; a plataforma da disciplina mostra a técnica como "detectável", e não "comprovada", até o cenário ser rodado de novo.
- c. Correta: a I é verdadeira, pois só conta como corrigido o que foi retestado; a II é falsa, pois ligar fonte e regra torna a técnica detectável, mas não comprova a detecção. A regra pode ter erro de lógica ou depender de um campo que não chega.
- d. Incorreta: a I é verdadeira; o critério de reteste faz parte do achado e precisa ser cumprido antes do estado "corrigido".
- e. Incorreta: a I é verdadeira; só a II é falsa.

**Questão 19** (correta: a)
- a. Correta: a I é verdadeira, e a II explica por quê: dividir o risco pelo esforço reduz a prioridade de correções longas (12 ÷ 3 = 4) diante de correções rápidas de risco semelhante (15 ÷ 1 = 15). O risco longo vai para o *roadmap*, com aceitação formal até lá.
- b. Incorreta: a II não é apenas verdadeira; ela é justamente o critério que produz a ordem descrita na I.
- c. Incorreta: a II é verdadeira; os ganhos rápidos são os achados de risco 10 ou mais com esforço 1.
- d. Incorreta: a I é verdadeira; correções que exigem projeto podem esperar no *roadmap*, desde que a diretoria aceite o risco residual ou aprove medida provisória.
- e. Incorreta: as duas asserções são verdadeiras; reveja a priorização por risco e esforço.

**Questão 20** (correta: d)
- a. Incorreta: a I é falsa; cobrar só o MTTR é exatamente o que a Lei de Goodhart desaconselha.
- b. Incorreta: a I não é verdadeira; um SOC cobrado só por MTTR tende a fechar casos cedo demais.
- c. Incorreta: a I é falsa e a II é verdadeira, ao contrário do que esta alternativa afirma.
- d. Correta: a I é falsa, porque o relatório usa poucos indicadores complementares (MTTD, MTTR, cobertura testada, visibilidade, ações retestadas), cada um com meta e dono; a II é verdadeira e explica o risco de transformar uma única medida em meta.
- e. Incorreta: a II é verdadeira; reveja a seção de métricas de melhoria da Aula 16.

**Questão 21** (correta: c)
- a. Incorreta: 7 min 30 s é o tempo até o alerta, e não até a abertura do caso; e 1 h 45 min mistura o alerta com a contenção.
- b. Incorreta: 1 h 20 min é o tempo do alerta (08:20) até a abertura do caso; o MTTD começa no primeiro evento (08:12:30).
- c. Correta: de 08:12:30 a 09:40:00 são 1 h 27 min 30 s (MTTD); de 09:40:00 a 10:05:00 são 25 min (MTTR).
- d. Incorreta: o MTTD está certo, mas o MTTR começa na abertura do caso (09:40), e não no primeiro evento.
- e. Incorreta: 1 h 52 min 30 s vai do primeiro evento à contenção; esse intervalo soma MTTD e MTTR.

**Questão 22** (correta: e)
- a. Incorreta: 7/12 é apenas o primeiro dia útil contado; o prazo tem três dias úteis.
- b. Incorreta: domingo não é dia útil e não pode ser o fim de um prazo em dias úteis.
- c. Incorreta: 8/12 é o segundo dia útil; ainda falta um.
- d. Incorreta: 14/12 seria o prazo em dobro (seis dias úteis), que vale só para agentes de tratamento de pequeno porte, o que não é o caso.
- e. Correta: o conhecimento foi na sexta, 4/12; sábado e domingo não contam; os dias úteis são 7/12 (segunda), 8/12 (terça) e 9/12 (quarta).

**Questão 23** (correta: a)
- a. Correta: X = 4 × 3 × 3 = 36; Z = 3 × 3 × 2 = 18; Y = 5 × 2 × 1 = 10. A ordem é decrescente de pontuação: X, Z e Y.
- b. Incorreta: a maior criticidade do ativo, isolada, não define a ordem; a pontuação combina os três fatores.
- c. Incorreta: as notas estão certas, mas Y (10) é menor que Z (18) e deve vir depois.
- d. Incorreta: Z tem 18, menos que X, com 36; a ordem deve ser decrescente.
- e. Incorreta: a ordem está invertida; atende-se primeiro a maior pontuação.

**Questão 24** (correta: d)
- a. Incorreta: confirmar o alerta e definir o escopo é detecção e análise, e não preparação; remover a ferramenta é erradicação.
- b. Incorreta: isolar e bloquear é contenção, e remover a ferramenta é erradicação; a ordem está trocada.
- c. Incorreta: a triagem não é contenção, e restaurar o *backup* é recuperação, e não erradicação.
- d. Correta: triagem e escopo são detecção e análise; isolar e bloquear, contenção; remover e redefinir, erradicação; restaurar e monitorar, recuperação.
- e. Incorreta: remover a ferramenta e redefinir credenciais é erradicação, e restaurar o *backup* é recuperação; a atividade pós-incidente é a das lições aprendidas.

**Questão 25** (correta: b)
- a. Incorreta: o isolamento é contenção e vem cedo, antes da recuperação, para impedir que o dano aumente.
- b. Correta: preservar evidências depois de erradicar pode apagar os rastros da investigação; o *playbook* revisado preserva antes de erradicar.
- c. Incorreta: a triagem é indispensável; um alerta só vira incidente depois de confirmado, por decisão formal.
- d. Incorreta: jurídico, comunicação e encarregado de dados participam desde as primeiras horas; a comunicação à ANPD não é decisão só da equipe técnica.
- e. Incorreta: a restauração a partir de *backup* íntegro faz parte da fase de recuperação.

**Questão 26** (correta: b)
- a. Incorreta: esse resultado soma 3 horas ao horário local em vez de converter o horário UTC para Brasília; 01:58:10Z corresponde a 22:58:10 de 01/12.
- b. Correta: 01:58:10 em UTC equivale a 22:58:10 de 01/12 em Brasília (UTC−3); até o RDP das 23:06:42 passam 8 min 32 s, uma ordem coerente com o acesso pela VPN.
- c. Incorreta: esse é o erro de ler o horário da VPN como se fosse local; a ordem impossível que surge é sinal de fusos misturados, e não de dois invasores.
- d. Incorreta: depois da conversão, a diferença entre os eventos é de 8 min 32 s, e não zero.
- e. Incorreta: os dois registros já trazem a informação de fuso suficiente (Z para UTC e o horário de Brasília do AD); o sensor de rede não é necessário para esse cálculo.

**Questão 27** (correta: d)
- a. Incorreta: começa pelo disco, que é das evidências menos voláteis, e deixa processos e conexões para depois da memória.
- b. Incorreta: os registros do SIEM ficam em outro servidor e não se perdem com o servidor comprometido; são os menos urgentes dessa lista.
- c. Incorreta: o disco não deve vir antes de processos e conexões, que mudam a cada segundo.
- d. Correta: processos e conexões (2) e memória (3) estão no nível mais volátil coletável; depois vem o disco (1) e, por fim, os registros remotos (4), como recomenda a RFC 3227.
- e. Incorreta: começar pelo disco arrisca perder o estado da memória, dos processos e das conexões.

**Questão 28** (correta: e)
- a. Incorreta: cada evidência tem a própria integridade; a conferência das outras quatro não comprova a quinta.
- b. Incorreta: trocar de algoritmo não resolve a divergência e ainda substitui o SHA-256 por um algoritmo mais fraco.
- c. Incorreta: sobrescrever o registro da coleta destrói a própria prova de integridade e compromete a cadeia de custódia; o formulário só recebe linhas novas.
- d. Incorreta: o *hash* serve justamente para provar que o arquivo não mudou; uma divergência indica alteração ou cópia diferente.
- e. Correta: a divergência mostra que a cópia não é idêntica à coletada; ela deve ser registrada, investigada e não pode ser apresentada como a evidência original.

**Questão 29** (correta: a)
- a. Correta: o ritmo fixo de 300 s é a assinatura de um *beacon*, e a conexão fora do ritmo abre um fluxo de 1.680 s com cerca de 2,9 GB saindo do servidor, o que confirma a saída de dados pelos metadados, sem decifrar o conteúdo.
- b. Incorreta: o conteúdo é cifrado, mas horários, ritmo, destino e volume são metadados suficientes para confirmar a linha do tempo.
- c. Incorreta: intervalo fixo é justamente a característica de *beacons*; regularidade não comprova legitimidade.
- d. Incorreta: a conexão fora do ritmo é o início do fluxo de 2,9 GB, o evento mais relevante da tabela, e não um falso positivo.
- e. Incorreta: o volume sai do servidor da organização para o endereço externo; o padrão é de exfiltração, e não de negação de serviço.

**Questão 30** (correta: c)
- a. Incorreta: 16 min 30 s é o tempo do primeiro evento até o alerta, e não até a abertura do caso; e o MTTR foi calculado com marcos errados.
- b. Incorreta: 4 h 05 min 20 s é o tempo do alerta até a triagem, só uma parte do MTTD; o MTTR também está errado.
- c. Correta: de 22:58:10 a 03:20:00 são 4 h 21 min 50 s (MTTD), dos quais 4 h 05 min 20 s entre o alerta (23:14:40) e a triagem; de 03:20:00 a 03:41:00 são 21 min (MTTR).
- d. Incorreta: 4 h 42 min 50 s vai do primeiro evento até a contenção, e não até a abertura do caso.
- e. Incorreta: os valores estão invertidos; o MTTD é o intervalo longo e o MTTR, o curto.

**Questão 31** (correta: d)
- a. Incorreta: 50% seria contar a técnica com alerta em 7 minutos na cobertura, mas ela ficou fora do critério de 5 minutos.
- b. Incorreta: 62,5% de visibilidade deixa de fora a técnica que gerou telemetria e alerta tardio.
- c. Incorreta: a cobertura testada só considera os 3 alertas dentro do critério.
- d. Correta: cobertura testada = 3 ÷ 8 = 37,5% (só os alertas dentro de 5 minutos); visibilidade = (3 + 2 + 1) ÷ 8 = 6 ÷ 8 = 75% (todas as técnicas com telemetria).
- e. Incorreta: 62,5% seria somar técnicas sem alerta à cobertura, e 100% ignoraria as 2 técnicas sem nenhum evento.

**Questão 32** (correta: a)
- a. Correta: pontuação 50 e comentário "parcial" indicam que há telemetria e alerta, mas o alerta chegou em 540 s, acima dos 300 s combinados; a técnica conta na visibilidade e fica fora da cobertura testada.
- b. Incorreta: sem telemetria a pontuação seria 0 e a cor, vermelha.
- c. Incorreta: técnicas fora do plano não recebem pontuação na *layer*.
- d. Incorreta: o comentário explica o motivo (alerta tardio), e não uma detecção parcial de procedimentos.
- e. Incorreta: o Navigator aceita pontuações numéricas livres; a legenda é que dá o significado de cada valor.

**Questão 33** (correta: c)
- a. Incorreta: "detectável" significa regra e fonte ativas, ainda sem teste; registrar como coberta transforma uma hipótese em número de relatório.
- b. Incorreta: desligar a regra reabre a lacuna do incidente; o ruído de manutenção se trata com exceção documentada.
- c. Correta: o ciclo só se completa com o reteste; a técnica passa a comprovada quando o mesmo caso de teste gera o alerta dentro do critério.
- d. Incorreta: o exercício *purple* existe justamente para comprovar a detecção antes de um ataque real.
- e. Incorreta: a cobertura é medida sobre as técnicas priorizadas, e não sobre a matriz inteira.

**Questão 34** (correta: b)
- a. Incorreta: o *cyber range* treina a operação técnica, tem custo maior e não é o melhor formato para testar decisões da diretoria.
- b. Correta: o *tabletop* é baseado em discussão, tem baixo custo, envolve técnicos e executivos e usa *injects* para testar decisões, papéis e comunicação sem tocar sistemas.
- c. Incorreta: o CTF desenvolve habilidades técnicas e não testa quem decide ou comunica.
- d. Incorreta: o exercício *purple* valida detecções técnica a técnica e executa casos de teste nos sistemas.
- e. Incorreta: uma operação de Red Team avalia a reação técnica a um ataque realista, não o processo de decisão da diretoria.

**Questão 35** (correta: e)
- a. Incorreta: o líder do Red Team executa os casos de teste; quem conduz o tempo e as tarefas é o facilitador.
- b. Incorreta: a CISO autoriza o exercício, mas não conduz a sessão.
- c. Incorreta: o analista de SOC observa telemetria, alertas e resposta.
- d. Incorreta: a perita forense não participa da condução do exercício *purple*.
- e. Correta: no PTEF, o facilitador conduz a sessão, controla o tempo e garante que cada discussão termine em ação com dono e prazo.

**Questão 36** (correta: e)
- a. Incorreta: 7 é a soma das notas; o risco é o produto, 3 × 4 = 12.
- b. Incorreta: 12 fica na faixa de 10 a 14, que é alto; crítico começa em 15.
- c. Incorreta: a prioridade é o risco dividido pelo esforço, 12 ÷ 3 = 4, e não multiplicado (36).
- d. Incorreta: o risco é 12 (produto), e não 7; e a prioridade divide pelo esforço.
- e. Correta: risco = 3 × 4 = 12, classe alto (10 a 14) e prioridade = 12 ÷ 3 = 4. Por isso o achado vai para o *roadmap*, atrás dos ganhos rápidos.

**Questão 37** (correta: c)
- a. Incorreta: 16 min 30 s é o tempo até o alerta da regra, e não até a abertura do caso, que é o marco definido para o MTTD; e o MTTR vai da abertura do caso à contenção.
- b. Incorreta: 4 h 05 min 20 s é o tempo entre o alerta e a abertura do caso, e não entre o primeiro evento e a abertura.
- c. Correta: de 22h58min10s a 03h20min00s passam 4 h 21 min 50 s (MTTD); de 03h20 a 03h41 passam 21 min (MTTR).
- d. Incorreta: o MTTR conta a partir da abertura do caso, e não do primeiro evento.
- e. Incorreta: o MTTD foi definido até a abertura do caso; usar o horário do alerta subestima o tempo em que o ataque ficou sem resposta.

**Questão 38** (correta: b)
- a. Incorreta: evento 4624, tipo de *logon* e nome de regra são detalhes do relatório técnico e da linha do tempo.
- b. Correta: o trecho fala em linguagem de negócio, pede uma decisão com dono e prazo e explicita a aceitação formal do risco residual, que é o que o sumário executivo deve fazer.
- c. Incorreta: a lógica de uma regra é conteúdo técnico, útil à engenharia de detecção, e não à diretoria.
- d. Incorreta: os *hashes* das evidências pertencem ao anexo técnico e à cadeia de custódia.
- e. Incorreta: uma tabela com todos os identificadores ATT&CK é conteúdo técnico e não cabe em uma página voltada à decisão.

**Questão 39** (correta: d)
- a. Incorreta: esta ordem segue apenas o risco, sem considerar o esforço.
- b. Incorreta: esta ordem inverte a prioridade, começando pelo achado de menor relação risco por esforço.
- c. Incorreta: X tem prioridade 20 ÷ 1 = 20, maior que a de Z (15 ÷ 1 = 15).
- d. Correta: as prioridades são X = 20, Z = 15, Y = 16 ÷ 2 = 8 e W = 12 ÷ 3 = 4; logo, X, Z, Y e W.
- e. Incorreta: Y (8) tem prioridade maior que W (4).

**Questão 40** (correta: a)
- a. Correta: só T1021.001 e T1219 têm detecção comprovada, 2 ÷ 4 = 50%; as quatro técnicas têm telemetria, 4 ÷ 4 = 100%. A T1567.002 está detectável, mas não comprovada, porque não foi retestada.
- b. Incorreta: 75% contaria a T1567.002 como comprovada, mas regra ligada sem reteste não comprova a detecção.
- c. Incorreta: a visibilidade é de 100%, pois a T1078 tem telemetria, mesmo sem regra.
- d. Incorreta: a T1567.002 não está comprovada e a T1078 tem telemetria; os dois valores estão errados.
- e. Incorreta: há duas técnicas comprovadas, e não uma; 25% subestima a cobertura testada.
