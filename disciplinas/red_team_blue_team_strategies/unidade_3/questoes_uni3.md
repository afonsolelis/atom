# Questionário — Unidade 3

Disciplina: Red Team & Blue Team Strategies  
Professor-conteudista: Afonso Cesar Lelis Brandão  
Template de origem: `documentos/Unidade 3/40 Questões - UNI3_nomedadisciplina.docx`

Quantidade obrigatória: 40 questões padrão ENADE — 20 de asserção-razão (1 a 20) e 20 de interpretação (21 a 40).
Cinco alternativas por questão (a–e); a correta é marcada com `*` imediatamente antes da letra.
Distribuição da letra correta: 8 questões para cada uma das letras a, b, c, d, e, no total das 40 questões.
Feedback para **cada alternativa** (por que está correta ou qual o equívoco), todos ao final do documento.

## Questões

### Asserção-razão

**1.** I. No Windows, o evento 4688 (criação de processo) pode registrar a linha de comando executada, desde que a política específica para isso esteja habilitada.

PORQUE

II. O registro nativo de segurança do Windows já inclui, por padrão, o *hash* do executável e o processo pai em todos os eventos de criação de processo, o que torna o Sysmon redundante.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**2.** I. Uma sequência de várias falhas de *logon* (evento 4625) seguida de um *logon* bem-sucedido (evento 4624), da mesma origem e em poucos minutos, é mais indicativa de senha descoberta do que as falhas observadas isoladamente.

PORQUE

II. A correlação realizada pelo SIEM combina eventos que, isolados, parecem inofensivos, mas que, em conjunto e em sequência, revelam um padrão de ataque.

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**3.** I. Manter os registros no SIEM por apenas sete dias é suficiente para investigar qualquer intrusão, desde que as regras de correlação sejam de boa qualidade.

PORQUE

II. A retenção de registros deve atender a requisitos legais e contratuais e ao tempo real das investigações, já que um invasor pode permanecer semanas no ambiente antes de ser descoberto.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**4.** I. A normalização realizada pelo SIEM permite pesquisar, de uma só vez, registros de fontes diferentes, como o *firewall* e o registro de segurança do Windows.

PORQUE

II. O SIEM enriquece os eventos com contexto, como a geolocalização do endereço IP, a criticidade do ativo e o cargo do usuário, o que acelera a triagem.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**5.** I. Gerar o maior número possível de alertas é a estratégia operacional mais segura para um SOC, pois maximiza a chance de que nenhum ataque passe despercebido.

PORQUE

II. Quando a maioria dos alertas é composta de falsos positivos, os analistas tendem a investigar cada um com mais cuidado, o que eleva a qualidade da triagem.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

**6.** I. A abordagem de detecção como código (*detection-as-code*) permite identificar e desfazer rapidamente uma alteração de regra que passou a gerar ruído no SIEM.

PORQUE

II. Nessa abordagem, as regras ficam em um repositório com controle de versão, que registra quem alterou cada regra, quando e por quê, e passam por revisão de pares e validação automática antes da produção.

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**7.** I. Uma regra escrita no formato Sigma pode ser convertida, por ferramentas do próprio projeto, para a linguagem de consulta de diferentes SIEMs.

PORQUE

II. O Sigma é um formato proprietário, vinculado a um único fornecedor de SIEM, que executa as regras diretamente, sem necessidade de conversão.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**8.** I. Detecções baseadas em indicadores de comprometimento (IOC), como *hashes* e endereços IP, são as mais resistentes a mudanças do adversário.

PORQUE

II. Detecções comportamentais procuram a técnica em si e, por isso, resistem a variações de ferramenta, embora exijam conhecimento do ambiente para reduzir o ruído.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**9.** I. Ao criar uma exceção para reduzir falsos positivos, a equipe de detecção pode aumentar a precisão de uma regra e, ao mesmo tempo, reduzir sua sensibilidade.

PORQUE

II. A precisão mede quantos dos alertas gerados eram verdadeiros, enquanto a sensibilidade (*recall*) mede quantos dos ataques ocorridos foram detectados; uma exceção que elimina ruído também pode excluir um ataque real.

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**10.** I. Além de detectar, o EDR (*Endpoint Detection and Response*) permite responder a um ataque, por exemplo isolando a máquina da rede, encerrando processos e coletando evidências remotamente.

PORQUE

II. A MITRE mantém o D3FEND, uma base de conhecimento de contramedidas defensivas complementar ao ATT&CK.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**11.** I. O *threat hunting* parte da premissa de comprometimento presumido (*assume breach*): em vez de esperar o alerta, o caçador supõe que o adversário já está no ambiente e procura evidências disso.

PORQUE

II. A caça a ameaças substitui o monitoramento contínuo do SOC, tornando desnecessárias as regras automatizadas de detecção.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**12.** I. Na Pirâmide da Dor, proposta por David Bianco, os endereços IP ocupam o topo, por serem os indicadores mais difíceis de o adversário substituir.

PORQUE

II. Alterar um único byte de um arquivo executável mantém inalterado o seu *hash* SHA-256, o que torna o bloqueio por *hash* uma defesa robusta.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

**13.** I. Uma lista com 300 endereços IP maliciosos, recebida de um parceiro sem qualquer contexto, já constitui, por si só, inteligência de ameaças.

PORQUE

II. A inteligência de ameaças (CTI) é a informação sobre adversários coletada, analisada e contextualizada para apoiar decisões, respondendo a perguntas como quem ameaça o setor, com quais objetivos e de que forma.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**14.** I. Com o Modelo Diamante, a partir de um domínio malicioso já identificado, o analista pode descobrir outras vítimas que se comunicaram com esse domínio.

PORQUE

II. O Modelo Diamante descreve cada evento de intrusão por quatro vértices relacionados — adversário, capacidade, infraestrutura e vítima —, permitindo "pivotar" de um vértice conhecido para os demais.

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**15.** I. O produto mais valioso de uma caça a ameaças bem-sucedida não é apenas o incidente encontrado, mas a detecção automatizada que nasce dela.

PORQUE

II. Caças feitas a cada 30 dias e caças semanais resultam no mesmo tempo médio de permanência do invasor, pois a cadência da caça não influencia o *dwell time*.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**16.** I. A declaração de um incidente é uma decisão formal, que mobiliza pessoas, recursos e, muitas vezes, obrigações legais.

PORQUE

II. O NIST SP 800-61 Rev. 3, publicado em 2025, reorganiza as recomendações de resposta a incidentes como um perfil do CSF 2.0.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**17.** I. Diante de um alerta de *ransomware*, desligar imediatamente o servidor da tomada é sempre a melhor forma de contenção, pois preserva integralmente as evidências do ataque.

PORQUE

II. A RFC 3227 recomenda coletar as evidências da mais volátil para a menos volátil, como a memória antes do disco.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**18.** I. Pela Resolução CD/ANPD nº 15/2024, o controlador dispõe de trinta dias corridos, contados da detecção do primeiro alerta, para comunicar à ANPD qualquer incidente de segurança.

PORQUE

II. A regulamentação da ANPD exige apenas a comunicação dos incidentes, dispensando o controlador de manter qualquer registro interno dos incidentes de segurança.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

**19.** I. A cadeia de custódia é indispensável para que uma evidência digital coletada durante a resposta a um incidente seja considerada confiável.

PORQUE

II. A cadeia de custódia registra quem coletou a evidência, quando, como, onde ela ficou guardada e por quais mãos passou, com *hashes* que comprovam a sua integridade.

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**20.** I. A reunião de lições aprendidas deve ser conduzida sem caça a culpados, e cada achado deve se converter em uma ação com responsável e prazo.

PORQUE

II. No NIST SP 800-61 Rev. 3, as lições aprendidas ficam restritas à função Recuperar do CSF 2.0 e não influenciam as demais funções.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Interpretação

**21.** O SIEM da distribuidora fictícia Vale Norte exibiu, para a mesma conta, os seguintes eventos do registro de segurança de um servidor exposto à internet:

```
02:14:01  4625  conta=financeiro01  origem=203.0.113.45
02:14:09  4625  conta=financeiro01  origem=203.0.113.45
   ... (mais 7 eventos 4625 idênticos até 02:16:22)
02:16:40  4624  conta=financeiro01  origem=203.0.113.45
```

Com base nos conceitos da Aula 9, qual é a interpretação mais adequada desse trecho?

a. Trata-se de erros de digitação do próprio usuário, pois o *logon* final foi bem-sucedido, e não há motivo para análise adicional.
*b. A sequência de falhas seguida de sucesso, da mesma origem e em menos de três minutos, sugere senha descoberta e justifica investigar a conta.
c. O evento 4624 indica que o registro de auditoria do servidor foi apagado logo após as tentativas de acesso, o que caracteriza tentativa de apagar rastros.
d. Os eventos 4625 registram a criação de processos com linha de comando, revelando a execução de comandos maliciosos no servidor.
e. Como cada evento 4625 é inofensivo quando observado isoladamente, a sequência inteira pode ser descartada pela triagem sem prejuízo.

**22.** O SOC da empresa fictícia Atlas Saúde recebe, em média, 1.200 alertas por dia. A triagem de cada alerta leva 12 minutos. A equipe N1 tem quatro analistas, cada um com cerca de 6 horas efetivas de triagem por dia. Qual é a capacidade diária de triagem da equipe e que fração do volume ela representa?

a. 480 alertas por dia, o que corresponde a 40% do volume recebido.
b. 240 alertas por dia, o que corresponde a 20% do volume recebido.
c. 100 alertas por dia, o que corresponde a cerca de 8,3% do volume recebido.
d. 1.200 alertas por dia, o que corresponde a 100% do volume recebido.
*e. 120 alertas por dia, o que corresponde a 10% do volume recebido.

**23.** Um SOC recebe 2.000 alertas por dia. A análise mostrou que 90% desse volume vem de apenas quatro regras ruidosas. A equipe de detecção ajusta essas quatro regras e consegue eliminar 80% do ruído que elas produziam, sem alterar as demais. Qual é, aproximadamente, o novo volume diário de alertas?

*a. 560 alertas por dia.
b. 1.440 alertas por dia.
c. 400 alertas por dia.
d. 1.600 alertas por dia.
e. 200 alertas por dia.

**24.** Ao investigar um servidor de arquivos, uma analista encontra, no registro de segurança do Windows, vários eventos 4688 às 03:02 e, às 03:10, um evento 1102. Nenhuma tarefa de manutenção estava programada para esse horário. Qual é a interpretação correta do evento 1102 nesse contexto?

a. Indica um *logon* bem-sucedido de conta administrativa, comum em manutenções noturnas e sem relevância para a investigação.
b. Indica uma falha de *logon*, sugerindo uma tentativa de força bruta contra o servidor.
c. Corresponde a uma consulta DNS registrada pelo Sysmon, útil para identificar domínios recém-registrados.
*d. Indica que o registro de auditoria foi apagado, o que, após a execução de processos, sugere tentativa de apagar rastros.
e. Corresponde a uma conexão de rede registrada pelo Sysmon, indicando comunicação com servidor de comando e controle.

**25.** A loja virtual fictícia Pague Fácil processa pagamentos com cartão e mantém apenas os últimos 30 dias de registros no SIEM, por economia de armazenamento. Em uma investigação, a equipe estima que o invasor obteve o acesso inicial há cerca de 45 dias. Qual avaliação é correta?

a. A retenção atende ao PCI DSS, que exige apenas sete dias de histórico, e a investigação não é prejudicada.
b. A retenção é irrelevante, pois uma boa correlação no SIEM compensa a ausência dos registros antigos.
*c. A retenção não atende ao PCI DSS (12 meses, com 3 de acesso imediato) e impede reconstruir o início da intrusão.
d. O único problema da política é o custo, que poderia ser reduzido ainda mais com retenção de sete dias, sem efeito sobre investigações futuras.
e. O PCI DSS exige três meses de retenção no total; a empresa está apenas dois meses abaixo do exigido, mas a investigação do acesso inicial não é afetada pela retenção.

**26.** A equipe de engenharia de detecção recebeu, para revisão de pares, a seguinte regra Sigma:

```yaml
title: Exclusão de cópias de sombra com wmic
logsource:
  category: process_creation
  product: windows
detection:
  selection:
    Image|endswith: '\wmic.exe'
    CommandLine|contains|all:
      - 'shadowcopy'
      - 'delete'
  condition: selection
falsepositives:
  - Rotinas legítimas de administração de backup
tags:
  - attack.impact
  - attack.t1490
level: high
```

Qual interpretação da regra está correta?

a. A regra depende de registros de consultas DNS, pois procura domínios associados a *ransomware*.
b. A regra dispara sempre que a linha de comando do `wmic.exe` contiver qualquer um dos dois termos listados.
c. A regra só funciona no SIEM do fornecedor que a criou, pois o formato Sigma não admite conversão.
d. O campo `falsepositives` faz a regra ignorar automaticamente as execuções originadas de rotinas de *backup*.
*e. A regra exige telemetria de criação de processos (4688 com linha de comando ou Sysmon ID 1) e os dois termos na mesma linha de comando.

**27.** Em 30 dias, uma regra de detecção de PowerShell suspeito disparou 500 vezes, e a investigação confirmou 25 alertas verdadeiros, que correspondiam a todos os ataques ocorridos no período. A equipe criou uma exceção para um *script* de inventário. No mês seguinte, em cenário equivalente, com os mesmos 25 ataques, a regra disparou 50 vezes, com 24 alertas verdadeiros. Quais são a precisão e a sensibilidade antes e depois do ajuste?

a. Precisão de 5% para 50%; sensibilidade inalterada em 100%.
*b. Precisão de 5% para 48%; sensibilidade de 100% para 96%.
c. Precisão de 25% para 48%; sensibilidade de 100% para 96%.
d. Precisão de 5% para 96%; sensibilidade de 100% para 48%.
e. Precisão de 95% para 52%; sensibilidade de 100% para 96%.

**28.** Um relatório indica que um grupo criminoso recompila seu artefato malicioso a cada campanha (gerando um *hash* novo) e troca seus servidores com frequência, mas sempre segue o mesmo comportamento: um documento do Word abre o PowerShell, que baixa e executa um arquivo. Qual detecção é mais adequada para resistir a essas mudanças?

a. Bloquear, no EDR, os *hashes* listados no relatório, atualizando a lista sempre que uma nova campanha for divulgada.
b. Bloquear, no *firewall*, os endereços IP dos servidores de comando e controle informados no relatório mais recente.
c. Criar uma detecção por anomalia, comparando o tráfego com uma linha de base que ainda está instável por causa de uma migração recente.
*d. Criar uma regra comportamental que alerte quando o processo do Word iniciar o PowerShell, usando a árvore de processos do EDR.
e. Dispensar novas regras e contratar mais analistas para revisar manualmente todas as execuções de PowerShell.

**29.** A equipe de uma empresa escreveu uma regra para detectar a exclusão de cópias de sombra e a implantou diretamente no SIEM, sem validação. Meses depois, o Red Team executou em laboratório o teste do Atomic Red Team para a técnica T1490, e a regra não disparou: o nome de um campo estava errado. Qual conclusão é mais adequada?

*a. Pulou-se a etapa de teste do ciclo de vida; testes mapeados ao ATT&CK, em esteira de detecção como código, deveriam validar a regra antes da implantação.
b. A falha ocorreu na etapa de aposentadoria, pois a regra deveria ter sido desativada logo após a implantação.
c. O problema foi a ausência de requisito, e bastaria aumentar o nível da regra para `critical` para que ela passasse a disparar.
d. A regra deveria ser substituída por um antivírus baseado em assinaturas de arquivos, que dispensa testes.
e. O Atomic Red Team não serve para validar regras, pois reproduz técnicas fora do mapeamento ATT&CK.

**30.** O console do EDR da empresa fictícia Rota Sul mostra, em uma estação do setor financeiro, a árvore `WINWORD.EXE → powershell.exe → update.exe`. Dez minutos antes, os sensores de três outras estações do mesmo setor pararam de enviar telemetria. Qual interpretação é mais adequada?

a. Por ser baseado em assinaturas de arquivos, o EDR só alertaria se `update.exe` constasse de uma lista de *hashes* conhecidos; sem isso, não há motivo de preocupação.
b. A interrupção dos sensores indica manutenção rotineira e deve ser ignorada, pois a saúde do agente não é um sinal de segurança relevante.
c. O EDR apenas registra eventos; para conter a ameaça, um técnico precisa ir fisicamente até a estação e desconectar o cabo de rede.
d. A árvore de processos é típica de atualização legítima do Office e não exige investigação adicional.
*e. A árvore sugere execução maliciosa a partir de documento, e o silêncio dos sensores pode indicar tentativa de desativar agentes; cabe investigar e considerar isolar as máquinas.

**31.** Um caçador de ameaças de uma cooperativa de crédito precisa formular uma hipótese para iniciar uma caça. Qual das opções a seguir é a hipótese mais adequada, segundo a abordagem orientada por hipóteses?

a. "Pode haver *hackers* na nossa rede."
*b. "Um adversário usa contas de VPN válidas fora do horário habitual, de países onde a cooperativa não opera, para acessar servidores de arquivos."
c. "Vamos exportar todos os registros de todas as fontes do último ano e analisá-los linha a linha, sem foco definido, até que algum evento chame a atenção da equipe."
d. "O antivírus detecta qualquer ameaça conhecida e desconhecida, portanto não há o que caçar."
e. "Vamos importar 500 *hashes* de um relatório de inteligência no EDR e considerar a caça concluída."

**32.** Um relatório de inteligência sobre um grupo que ataca o setor financeiro traz: o *hash* SHA-256 do executável usado, o IP do servidor de comando e controle, um domínio de *phishing*, uma chave de registro criada para persistência e a descrição do comportamento de apagar cópias de sombra com `vssadmin` antes da criptografia. Se a equipe puder implementar apenas uma detecção, qual impõe maior custo ao adversário segundo a Pirâmide da Dor?

a. Bloqueio do *hash* SHA-256 do executável no EDR.
b. Bloqueio do IP do servidor de comando e controle no *firewall*.
*c. Detecção do comportamento de apagar cópias de sombra antes da criptografia.
d. Bloqueio do domínio de *phishing* no servidor DNS.
e. Detecção da chave de registro criada para persistência.

**33.** Uma técnica de persistência não tem regra de detecção e só pode ser encontrada por caça. A equipe realiza essa caça a cada 14 dias e estuda passar a realizá-la a cada 4 dias. Considerando que o invasor se instala em um dia aleatório, qual é o tempo médio até a descoberta em cada cenário?

a. 14 dias no cenário atual e 4 dias no novo cenário.
b. 7 dias no cenário atual e 4 dias no novo cenário.
c. 3,5 dias no cenário atual e 1 dia no novo cenário.
d. 14 dias no cenário atual e 2 dias no novo cenário.
*e. 7 dias no cenário atual e 2 dias no novo cenário.

**34.** Um relatório de inteligência recebido por um hospital contém três partes: (1) uma análise do aumento de ataques de extorsão contra o setor de saúde, dirigida à diretoria; (2) a descrição de uma campanha em curso de um grupo específico contra hospitais da região, com suas intenções e capacidades, para a liderança do SOC e de resposta a incidentes; (3) uma lista de TTPs e indicadores para analistas e engenheiros de detecção. Como se classificam, respectivamente, essas partes?

a. Tática, operacional e estratégica.
b. Operacional, estratégica e tática.
c. Estratégica, tática e operacional.
*d. Estratégica, operacional e tática.
e. Tática, estratégica e operacional.

**35.** Durante uma investigação, um analista identifica um domínio malicioso e consulta os registros do *proxy* para descobrir que outras máquinas da empresa o acessaram. Em seguida, compartilha o achado com outras organizações do setor por meio do MISP, em formato STIX, com marcação TLP. Qual alternativa descreve corretamente essas ações?

a. O analista pivotou a partir do vértice adversário; o TAXII descreve os objetos compartilhados; e o TLP define o formato do arquivo.
*b. O analista pivotou do vértice infraestrutura para o vértice vítima; o STIX descreve os objetos; e o TLP indica com que liberdade a informação pode ser repassada.
c. O analista pivotou do vértice capacidade para o vértice adversário; o STIX define o transporte; e o TLP criptografa a informação.
d. O domínio é o vértice vítima do Modelo Diamante; o STIX é um protocolo de transporte; e o TLP é mantido pela MITRE.
e. O domínio é o vértice capacidade; o MISP é um formato de descrição de objetos; e o TLP define o prazo de comunicação à ANPD.

**36.** A equipe de resposta de uma empresa tem três incidentes abertos e usa a pontuação severidade = criticidade do ativo (1 a 5) × confiança na detecção (1 a 3) × abrangência (1 a 3). (X) Estação do RH com macro suspeita: 2, 3 e 1. (Y) Controlador de domínio com conta administrativa criada fora do processo: 5, 2 e 2. (Z) Servidores de arquivos com criptografia em andamento: 4, 3 e 2. Qual é a ordem de atendimento?

*a. Z (24), Y (20) e X (6).
b. Y (20), Z (24) e X (6).
c. X (6), Y (20) e Z (24).
d. Z (24), X (6) e Y (20).
e. Y (10), Z (9) e X (6).

**37.** Linha do tempo de um incidente na empresa fictícia Lumen Varejo: na segunda-feira, o EDR detecta atividade suspeita em um servidor; na quarta-feira, a equipe confirma que o servidor continha dados pessoais de clientes e que o incidente pode acarretar risco relevante aos titulares. Qual afirmação está de acordo com a LGPD e a Resolução CD/ANPD nº 15/2024?

a. A comunicação à ANPD deve ocorrer em até 72 horas corridas, contadas da detecção na segunda-feira.
b. A comunicação só é obrigatória se uma perícia judicial confirmar a exfiltração dos dados.
c. Basta comunicar os titulares, pois a ANPD só é notificada quando há mais de mil pessoas afetadas.
d. O controlador tem 30 dias para comunicar, contados da conclusão das lições aprendidas.
*e. O prazo de três dias úteis conta da quarta-feira, quando se soube que dados pessoais foram afetados; ANPD e titulares devem ser comunicados.

**38.** Um coordenador de incidentes listou as seguintes atividades: (1) elaborar *playbooks* e treinar a equipe; (2) triar alertas e definir escopo e severidade; (3) isolar máquinas, remover a persistência e restaurar *backups*; (4) realizar a reunião de lições aprendidas. Segundo o ciclo clássico do NIST SP 800-61 Rev. 2, a que fases correspondem, respectivamente?

a. Detecção e análise; preparação; pós-incidente; contenção, erradicação e recuperação.
b. Preparação; contenção, erradicação e recuperação; detecção e análise; pós-incidente.
*c. Preparação; detecção e análise; contenção, erradicação e recuperação; pós-incidente.
d. Pós-incidente; detecção e análise; preparação; contenção, erradicação e recuperação.
e. Preparação; detecção e análise; pós-incidente; contenção, erradicação e recuperação.

**39.** Linha do tempo de um incidente: às 03:00, o EDR alerta sobre exclusão de cópias de sombra; às 03:10, um analista desliga o servidor da tomada; às 03:40, faz uma cópia do disco sem calcular *hash*; até as 05:00, o *pendrive* com a cópia passa por três pessoas, sem registro. Qual avaliação é correta?

a. O procedimento foi adequado, pois a prioridade absoluta é interromper o ataque, e a documentação das evidências é opcional.
b. O único erro foi não formatar o servidor logo às 03:10, já que a erradicação deve preceder a contenção.
c. Não houve perda relevante, porque o disco é mais volátil do que a memória e foi preservado.
*d. Desligar o servidor apagou a memória volátil; sem *hash* nem registro de manuseio, a cadeia de custódia ficou comprometida. Isolar pelo EDR seria preferível.
e. A cadeia de custódia só se aplica a evidências físicas, e não a cópias de disco digitais armazenadas em *pendrive*.

**40.** Em um mesmo dia, o SOC de uma empresa registra: (1) uma única falha de *logon* (4625) de um colaborador que errou a senha; (2) o disparo de uma regra que sinaliza PowerShell possivelmente malicioso, ainda não analisado; (3) a confirmação de que dados de clientes foram copiados para um servidor externo por um invasor. Como se classificam, respectivamente, essas ocorrências?

a. Incidente, alerta e evento.
*b. Evento, alerta e incidente.
c. Alerta, evento e incidente.
d. Evento, incidente e alerta.
e. Alerta, incidente e evento.

## Gabarito e feedbacks

**Questão 1** (correta: c)
- a. Incorreta: a asserção II é falsa; o registro nativo não traz por padrão o *hash* do executável nem o processo pai, e é justamente isso que o Sysmon acrescenta.
- b. Incorreta: a asserção II não é verdadeira; reveja a comparação entre o evento 4688 e o Sysmon na Aula 9.
- c. Correta: o evento 4688 só registra a linha de comando se a política específica estiver habilitada ("ter a fonte não basta; é preciso configurá-la"), e o Sysmon não é redundante, pois enriquece a telemetria com *hash* e processo pai.
- d. Incorreta: a asserção I é verdadeira; o registro da linha de comando no 4688 depende de uma política específica.
- e. Incorreta: apenas a II é falsa; a I descreve corretamente a configuração do evento 4688.

**Questão 2** (correta: a)
- a. Correta: a I é verdadeira e a II explica por quê — a correlação junta falhas (4625) e sucesso (4624) da mesma origem em curto intervalo, revelando um padrão que os eventos isolados não mostram.
- b. Incorreta: a II é exatamente o mecanismo que torna a sequência mais significativa do que os eventos isolados, portanto justifica a I.
- c. Incorreta: a II é verdadeira; a correlação é uma das funções-chave do SIEM.
- d. Incorreta: a I é verdadeira; reveja o exemplo de dez falhas seguidas de um *logon* bem-sucedido na Aula 9.
- e. Incorreta: ambas as asserções são verdadeiras e descrevem o conceito de correlação.

**Questão 3** (correta: d)
- a. Incorreta: a I é falsa; correlação de qualidade não recupera registros que já foram descartados.
- b. Incorreta: a I é falsa; além disso, a II contradiz a I, em vez de apenas não a justificar.
- c. Incorreta: a avaliação está invertida; a I é falsa e a II é verdadeira.
- d. Correta: sete dias não contam a história do início de uma intrusão que durou semanas (I falsa), e a retenção deve considerar lei, contratos e o tempo real das investigações (II verdadeira).
- e. Incorreta: a II é verdadeira; reveja o tópico de retenção do SIEM, incluindo o exemplo do PCI DSS.

**Questão 4** (correta: b)
- a. Incorreta: o enriquecimento acrescenta contexto aos eventos, mas não é o que permite pesquisar fontes diferentes de uma vez; isso decorre da conversão para um esquema comum (normalização).
- b. Correta: ambas são verdadeiras — a normalização coloca campos equivalentes (como "usuário" e "*TargetUserName*") no mesmo campo, e o enriquecimento acelera a triagem —, mas são funções distintas, e a II não justifica a I.
- c. Incorreta: a II é verdadeira; o enriquecimento é uma função do SIEM descrita na Aula 9.
- d. Incorreta: a I é verdadeira; é exatamente o propósito da normalização.
- e. Incorreta: as duas asserções são verdadeiras; reveja as funções do SIEM (normalizar, enriquecer, correlacionar e reter).

**Questão 5** (correta: e)
- a. Incorreta: as duas asserções são falsas; o excesso de alertas produz o efeito contrário ao desejado.
- b. Incorreta: nenhuma das asserções é verdadeira; reveja o conceito de fadiga de alertas.
- c. Incorreta: a I é falsa; alertar sobre tudo gera fadiga de alertas e faz o alerta verdadeiro se perder na fila.
- d. Incorreta: a II é falsa; com muitos falsos positivos, os analistas passam a fechar alertas no automático.
- e. Correta: ambas são falsas — a pergunta certa é quantos alertas a equipe consegue investigar com qualidade, e o excesso de falsos positivos reduz, e não aumenta, o cuidado na triagem.

**Questão 6** (correta: a)
- a. Correta: o controle de versão registra quem alterou a regra, quando e por quê, o que explica a capacidade de identificar e desfazer uma mudança que gerou ruído.
- b. Incorreta: a II é justamente a causa da I; sem o versionamento, não haveria como desfazer a alteração com rapidez.
- c. Incorreta: a II é verdadeira; descreve a abordagem de detecção como código.
- d. Incorreta: a I é verdadeira; reveja o tópico "Detecção como código e o padrão Sigma".
- e. Incorreta: as duas asserções são verdadeiras e relacionadas causalmente.

**Questão 7** (correta: c)
- a. Incorreta: a II é falsa; o Sigma é aberto e independente de fornecedor.
- b. Incorreta: a II não é verdadeira; um formato proprietário e sem conversão contradiria a própria I.
- c. Correta: a I é verdadeira — regras Sigma são convertidas para a linguagem de diferentes SIEMs —, e a II é falsa, pois o Sigma é um formato aberto, em YAML, independente de fornecedor.
- d. Incorreta: a I é verdadeira; a portabilidade entre SIEMs é a principal vantagem do Sigma.
- e. Incorreta: somente a II é falsa.

**Questão 8** (correta: d)
- a. Incorreta: a I é falsa; indicadores são simples e precisos, mas o adversário os troca com facilidade.
- b. Incorreta: a I é falsa; reveja a tabela de tipos de detecção da Aula 10.
- c. Incorreta: a avaliação está invertida; a I é falsa e a II é verdadeira.
- d. Correta: detecções por IOC são frágeis diante de mudanças do adversário (I falsa), enquanto as comportamentais resistem a variações de ferramenta, com a ressalva do ruído (II verdadeira).
- e. Incorreta: a II é verdadeira; descreve a vantagem e a limitação das detecções comportamentais.

**Questão 9** (correta: a)
- a. Correta: a definição dos dois indicadores (II) explica a troca descrita na I — a exceção reduz falsos positivos (precisão sobe), mas pode excluir um ataque real (sensibilidade cai), como no exemplo de 5% para 47,5% de precisão e de 100% para 95% de sensibilidade.
- b. Incorreta: a II explica diretamente a troca entre precisão e sensibilidade mencionada na I.
- c. Incorreta: a II é verdadeira; as definições de precisão e sensibilidade estão corretas.
- d. Incorreta: a I é verdadeira; ajustar uma regra quase sempre é uma troca entre os dois indicadores.
- e. Incorreta: as duas asserções são verdadeiras; reveja o exemplo numérico de precisão da Aula 10.

**Questão 10** (correta: b)
- a. Incorreta: o D3FEND é uma base de conhecimento de contramedidas; não é ele que dá ao EDR a capacidade de responder, mas o próprio agente instalado no *endpoint*.
- b. Correta: ambas são verdadeiras — o EDR detecta e responde (isolar, encerrar processos, coletar evidências), e o D3FEND é mantido pela MITRE —, mas a existência do D3FEND não explica a capacidade de resposta do EDR.
- c. Incorreta: a II é verdadeira; o D3FEND complementa o ATT&CK com técnicas defensivas.
- d. Incorreta: a I é verdadeira; a capacidade de resposta diferencia o EDR do antivírus tradicional.
- e. Incorreta: as duas asserções são verdadeiras.

**Questão 11** (correta: c)
- a. Incorreta: a II é falsa; a caça complementa o SOC, não o substitui.
- b. Incorreta: a II não é verdadeira; a caça bem-sucedida gera novas regras automatizadas, em vez de dispensá-las.
- c. Correta: a I descreve corretamente a premissa de comprometimento presumido, e a II é falsa, pois a caça complementa o SOC e alimenta a engenharia de detecção.
- d. Incorreta: a I é verdadeira; reveja a definição de *threat hunting* na Aula 11.
- e. Incorreta: apenas a II é falsa.

**Questão 12** (correta: e)
- a. Incorreta: as duas asserções são falsas.
- b. Incorreta: nenhuma das asserções é verdadeira; reveja a Pirâmide da Dor.
- c. Incorreta: a I é falsa; o topo da pirâmide é ocupado pelas TTPs, e os IPs ficam perto da base, como indicadores fáceis de trocar.
- d. Incorreta: a II é falsa; alterar um único byte gera um *hash* completamente diferente.
- e. Correta: ambas são falsas — os IPs estão perto da base da pirâmide, e a troca de um único byte muda o *hash*, o que torna o bloqueio por *hash* trivial de contornar.

**Questão 13** (correta: d)
- a. Incorreta: a I é falsa; dados soltos, como uma lista de IPs, ainda não são inteligência.
- b. Incorreta: a I é falsa; além disso, a definição da II mostra por que a lista sem contexto não é CTI.
- c. Incorreta: a avaliação está invertida; a I é falsa e a II é verdadeira.
- d. Correta: a lista sem contexto não é inteligência (I falsa); ela só se torna inteligência quando analisada e contextualizada para apoiar decisões (II verdadeira).
- e. Incorreta: a II é verdadeira; reveja a definição de CTI na Aula 11.

**Questão 14** (correta: a)
- a. Correta: a estrutura de quatro vértices relacionados (II) é o que permite pivotar da infraestrutura (o domínio) para a vítima (outras máquinas que o contataram), como afirma a I.
- b. Incorreta: o pivô entre vértices, descrito na II, é exatamente o que justifica a I.
- c. Incorreta: a II é verdadeira; os quatro vértices são adversário, capacidade, infraestrutura e vítima.
- d. Incorreta: a I é verdadeira; é o exemplo de pivô apresentado na Aula 11.
- e. Incorreta: as duas asserções são verdadeiras.

**Questão 15** (correta: c)
- a. Incorreta: a II é falsa; a cadência influencia diretamente o tempo médio até a descoberta.
- b. Incorreta: a II não é verdadeira; caças mensais levam, em média, 15 dias, e caças semanais, 3,5 dias.
- c. Correta: a I é verdadeira, pois uma regra automatizada reduz o tempo de descoberta para minutos; a II é falsa, porque cadências diferentes resultam em tempos médios diferentes (metade do intervalo).
- d. Incorreta: a I é verdadeira; reveja o exemplo numérico de cadência da caça.
- e. Incorreta: apenas a II é falsa.

**Questão 16** (correta: b)
- a. Incorreta: o caráter formal da declaração de incidente não decorre da publicação da Rev. 3 do NIST; são informações verdadeiras, mas sem relação causal.
- b. Correta: ambas são verdadeiras — declarar incidente é uma decisão formal, e a Rev. 3 integra a resposta ao CSF 2.0 —, mas a II não explica a I.
- c. Incorreta: a II é verdadeira; a Rev. 3 foi publicada em abril de 2025 como perfil do CSF 2.0.
- d. Incorreta: a I é verdadeira; reveja a distinção entre evento, alerta e incidente.
- e. Incorreta: as duas asserções são verdadeiras.

**Questão 17** (correta: d)
- a. Incorreta: a I é falsa; desligar o servidor apaga a memória volátil, contrariando a própria recomendação da II.
- b. Incorreta: a I é falsa; reveja o tópico "Contenção sem destruir evidências".
- c. Incorreta: a avaliação está invertida; a I é falsa e a II é verdadeira.
- d. Correta: desligar a máquina interrompe o ataque, mas apaga chaves, processos e conexões em memória (I falsa); a RFC 3227 recomenda coletar primeiro o que é mais volátil (II verdadeira).
- e. Incorreta: a II é verdadeira; a ordem de volatilidade é uma recomendação da RFC 3227.

**Questão 18** (correta: e)
- a. Incorreta: as duas asserções são falsas.
- b. Incorreta: nenhuma das asserções é verdadeira; reveja o tópico "Comunicação e obrigações legais".
- c. Incorreta: a I é falsa; o prazo é de três dias úteis, contados do conhecimento de que o incidente afetou dados pessoais, e vale para incidentes que possam acarretar risco ou dano relevante.
- d. Incorreta: a II é falsa; a resolução exige que o controlador mantenha registro dos incidentes.
- e. Correta: ambas são falsas — o prazo não é de trinta dias corridos nem conta do primeiro alerta, e a regulamentação exige registro dos incidentes.

**Questão 19** (correta: a)
- a. Correta: o registro de cada etapa de manuseio e os *hashes* de integridade (II) são o que torna a evidência confiável (I).
- b. Incorreta: a II descreve justamente os elementos que garantem a confiabilidade afirmada na I, portanto a justifica.
- c. Incorreta: a II é verdadeira; é a definição de cadeia de custódia apresentada na Aula 12.
- d. Incorreta: a I é verdadeira; sem cadeia de custódia, a integridade da evidência pode ser contestada.
- e. Incorreta: as duas asserções são verdadeiras.

**Questão 20** (correta: c)
- a. Incorreta: a II é falsa; as lições aprendidas alimentam a melhoria contínua em todas as funções.
- b. Incorreta: a II não é verdadeira; reveja como a Rev. 3 distribui as atividades entre as funções do CSF 2.0.
- c. Correta: a I descreve corretamente a reunião de lições aprendidas, e a II é falsa, pois na Rev. 3 as lições aprendidas alimentam a melhoria em todas as funções, fechando o ciclo com a engenharia de detecção.
- d. Incorreta: a I é verdadeira; o foco é aprender, não punir, e cada resposta vira ação com responsável e prazo.
- e. Incorreta: somente a II é falsa.

**Questão 21** (correta: b)
- a. Incorreta: o sucesso ao final de várias falhas, a partir de um IP externo, é justamente o padrão que sugere senha descoberta; não pode ser tratado como simples erro de digitação.
- b. Correta: é o padrão de correlação estudado na Aula 9 — falhas (4625) seguidas de sucesso (4624) da mesma origem em curto intervalo sugerem força bruta bem-sucedida e exigem investigação.
- c. Incorreta: o evento 4624 é um *logon* bem-sucedido; o apagamento do registro de auditoria corresponde ao evento 1102.
- d. Incorreta: o 4625 é falha de *logon*; a criação de processos é registrada pelo 4688 (ou Sysmon ID 1).
- e. Incorreta: é exatamente a combinação de eventos isoladamente inofensivos que a correlação deve examinar.

**Questão 22** (correta: e)
- a. Incorreta: 480 resultaria de 6 minutos por alerta, ou do dobro de horas de análise; o enunciado indica 12 minutos.
- b. Incorreta: 240 alertas exigiriam 48 horas de análise; a equipe dispõe de 24 horas (4 × 6).
- c. Incorreta: o valor não corresponde à conta; 24 horas × 60 ÷ 12 = 120, e não 100.
- d. Incorreta: a equipe não consegue triar todo o volume; essa é justamente a situação de fadiga de alertas.
- e. Correta: 4 × 6 = 24 horas = 1.440 minutos; 1.440 ÷ 12 = 120 alertas por dia, ou 10% de 1.200.

**Questão 23** (correta: a)
- a. Correta: o ruído eliminado é 0,90 × 2.000 × 0,80 = 1.440 alertas; o novo volume é 2.000 − 1.440 = 560 alertas por dia.
- b. Incorreta: 1.440 é a quantidade de alertas eliminados, e não o volume restante.
- c. Incorreta: 400 resulta de aplicar a redução de 80% a todo o volume (2.000 × 0,20); o ajuste atingiu apenas as quatro regras ruidosas, e os 200 alertas das demais regras permanecem.
- d. Incorreta: 1.600 corresponderia a eliminar apenas 20% do volume total, o que não reflete o ajuste descrito.
- e. Incorreta: 200 é o volume das demais regras (10%), sem considerar o ruído remanescente das quatro regras ajustadas.

**Questão 24** (correta: d)
- a. Incorreta: o *logon* bem-sucedido corresponde ao evento 4624, não ao 1102.
- b. Incorreta: a falha de *logon* corresponde ao evento 4625.
- c. Incorreta: a consulta DNS é o evento ID 22 do Sysmon, não um evento do registro de segurança.
- d. Correta: o evento 1102 indica que o registro de auditoria foi apagado; logo após criação de processos e fora de manutenção, é um forte indício de tentativa de apagar rastros.
- e. Incorreta: a conexão de rede é o evento ID 3 do Sysmon.

**Questão 25** (correta: c)
- a. Incorreta: o PCI DSS exige pelo menos 12 meses de histórico, e não sete dias.
- b. Incorreta: a correlação depende dos dados disponíveis; ela não reconstrói registros já descartados.
- c. Correta: o PCI DSS exige 12 meses de histórico, com os 3 mais recentes disponíveis de imediato, e 30 dias não alcançam o acesso inicial, ocorrido há 45 dias.
- d. Incorreta: reduzir ainda mais a retenção agravaria o descumprimento do PCI DSS e a perda de capacidade de investigação.
- e. Incorreta: o PCI DSS exige 12 meses no total (3 de acesso imediato), e a falta de registros antigos afeta, sim, a investigação do acesso inicial.

**Questão 26** (correta: e)
- a. Incorreta: o campo `logsource` declara a categoria `process_creation`, ou seja, telemetria de criação de processos, e não de DNS.
- b. Incorreta: o modificador `contains|all` exige que todos os termos estejam presentes na linha de comando.
- c. Incorreta: o Sigma é aberto e independente de fornecedor, e suas regras podem ser convertidas para diferentes SIEMs.
- d. Incorreta: o campo `falsepositives` apenas documenta os falsos positivos esperados; ele não cria exceções automáticas.
- e. Correta: a regra declara a fonte de criação de processos (que pode vir do 4688 com linha de comando habilitada ou do Sysmon ID 1) e exige o executável `wmic.exe` com os dois termos na linha de comando.

**Questão 27** (correta: b)
- a. Incorreta: a precisão após o ajuste é 24 ÷ 50 = 48%, e a sensibilidade caiu, pois um dos 25 ataques deixou de ser detectado.
- b. Correta: antes, 25 ÷ 500 = 5% e 25 ÷ 25 = 100%; depois, 24 ÷ 50 = 48% e 24 ÷ 25 = 96%.
- c. Incorreta: a precisão inicial é 25 ÷ 500 = 5%, e não 25%.
- d. Incorreta: os valores foram trocados; 96% é a sensibilidade final, e 48%, a precisão final.
- e. Incorreta: 95% é a proporção de falsos positivos antes do ajuste, e não a precisão.

**Questão 28** (correta: d)
- a. Incorreta: o grupo gera um *hash* novo a cada campanha; *hashes* estão na base da Pirâmide da Dor e são trivialmente trocados.
- b. Incorreta: o grupo troca seus servidores com frequência; IPs são fáceis de substituir.
- c. Incorreta: detecções por anomalia geram muitos falsos positivos quando a linha de base é instável, como no cenário descrito.
- d. Correta: o comportamento é constante; uma detecção comportamental baseada na árvore de processos do EDR resiste à troca de ferramentas e infraestrutura.
- e. Incorreta: aumentar a revisão manual agrava a fadiga de alertas; ajustar e criar boas regras costuma ser mais eficiente do que contratar mais analistas.

**Questão 29** (correta: a)
- a. Correta: uma regra nunca testada é apenas uma hipótese; o ciclo de vida prevê teste antes da implantação, e a detecção como código inclui validação automática, com apoio de testes como os do Atomic Red Team.
- b. Incorreta: a aposentadoria ocorre quando a regra deixa de fazer sentido, e não logo após a implantação; o problema foi a ausência de teste.
- c. Incorreta: o nível de severidade não corrige um nome de campo errado; a regra continuaria sem disparar.
- d. Incorreta: o antivírus baseado em assinaturas não substitui detecções comportamentais, e nenhuma detecção dispensa validação.
- e. Incorreta: o Atomic Red Team oferece testes pequenos e mapeados ao ATT&CK justamente para verificar se as regras disparam.

**Questão 30** (correta: e)
- a. Incorreta: o EDR não se limita a assinaturas de arquivos; ele reconstrói a árvore de processos e detecta comportamentos.
- b. Incorreta: como adversários tentam desativar os agentes, a saúde do próprio sensor precisa ser monitorada como sinal de segurança.
- c. Incorreta: o EDR permite responder remotamente, inclusive isolando a máquina da rede.
- d. Incorreta: um documento do Word que inicia o PowerShell, que executa um arquivo desconhecido, é o exemplo clássico de cadeia suspeita estudado na Aula 10.
- e. Correta: a árvore de processos é suspeita e o silêncio simultâneo de sensores pode indicar tentativa de desativá-los; investigar e isolar as máquinas pelo EDR são respostas adequadas.

**Questão 31** (correta: b)
- a. Incorreta: a hipótese é vaga e não indica o que procurar nem como verificar.
- b. Correta: a hipótese é específica e verificável — define o comportamento, as condições e o alvo, e pode ser testada com registros de VPN e de acesso a arquivos.
- c. Incorreta: a busca sem foco não é orientada por hipóteses e tende a ser improdutiva.
- d. Incorreta: a caça existe justamente para encontrar o que escapou dos controles automatizados, partindo do comprometimento presumido.
- e. Incorreta: importar indicadores é uma ação de bloqueio na base da Pirâmide da Dor, e não uma caça orientada por hipóteses.

**Questão 32** (correta: c)
- a. Incorreta: o *hash* está na base da pirâmide; sua troca é trivial para o adversário.
- b. Incorreta: o endereço IP é fácil de substituir, segundo a Pirâmide da Dor.
- c. Correta: o comportamento corresponde a uma TTP, no topo da pirâmide; detectá-lo obriga o adversário a mudar a forma como opera.
- d. Incorreta: nomes de domínio são simples de trocar, ainda que um pouco mais custosos que IPs.
- e. Incorreta: artefatos de *host*, como chaves de registro, são incômodos de trocar, mas impõem menos custo do que as TTPs.

**Questão 33** (correta: e)
- a. Incorreta: o intervalo entre caças é o tempo máximo, e não o tempo médio, até a descoberta.
- b. Incorreta: o cenário atual está correto (7 dias), mas a média do novo cenário é metade de 4 dias, ou seja, 2 dias.
- c. Incorreta: 3,5 dias corresponderia a caças semanais (7 dias), não quinzenais.
- d. Incorreta: o valor do cenário atual corresponde ao intervalo completo, e não à sua metade.
- e. Correta: em média, o invasor é encontrado na metade do intervalo: 14 ÷ 2 = 7 dias e 4 ÷ 2 = 2 dias.

**Questão 34** (correta: d)
- a. Incorreta: a análise de tendências para a diretoria é estratégica, e a lista de TTPs e indicadores é tática.
- b. Incorreta: a primeira parte é estratégica, e a segunda, operacional.
- c. Incorreta: a campanha específica de um grupo, com intenções e capacidades, é operacional, e a lista de TTPs é tática.
- d. Correta: tendências e riscos para a alta gestão são estratégicos; campanhas e atores específicos são operacionais; TTPs e indicadores para analistas são táticos.
- e. Incorreta: a ordem dos níveis está invertida; reveja os níveis de CTI na Aula 11.

**Questão 35** (correta: b)
- a. Incorreta: o domínio é infraestrutura, não adversário; o TAXII define como trocar os objetos, e o TLP indica a liberdade de repasse.
- b. Correta: do domínio (infraestrutura) o analista chegou a outras máquinas afetadas (vítima); o STIX descreve os objetos, e o TLP, mantido pelo FIRST, indica com que liberdade a informação pode ser repassada.
- c. Incorreta: o pivô partiu da infraestrutura; o transporte é papel do TAXII, e o TLP não criptografa informações.
- d. Incorreta: o domínio é infraestrutura; o STIX descreve objetos (o transporte é o TAXII); e o TLP é mantido pelo FIRST.
- e. Incorreta: o domínio é infraestrutura; o MISP é uma plataforma de armazenamento e compartilhamento; e o TLP não trata de prazos da ANPD.

**Questão 36** (correta: a)
- a. Correta: X = 2 × 3 × 1 = 6; Y = 5 × 2 × 2 = 20; Z = 4 × 3 × 2 = 24; a ordem é Z, Y e X.
- b. Incorreta: as pontuações estão corretas, mas a ordem não segue a maior severidade; Z (24) supera Y (20).
- c. Incorreta: a ordem está invertida, começando pelo incidente de menor severidade.
- d. Incorreta: X (6) tem severidade menor que Y (20) e deve ser atendido por último.
- e. Incorreta: as pontuações de Y e Z foram calculadas com soma, e não com multiplicação dos fatores.

**Questão 37** (correta: e)
- a. Incorreta: o prazo da Resolução CD/ANPD nº 15/2024 é de três dias úteis, e conta do conhecimento de que dados pessoais foram afetados, não da detecção.
- b. Incorreta: a comunicação é exigida quando o incidente possa acarretar risco ou dano relevante, sem depender de perícia judicial.
- c. Incorreta: o art. 48 da LGPD determina a comunicação à ANPD e aos titulares; não há o limite de pessoas mencionado.
- d. Incorreta: o prazo não é de 30 dias nem conta das lições aprendidas.
- e. Correta: o marco é o conhecimento de que o incidente afetou dados pessoais (quarta-feira), e o controlador deve comunicar à ANPD e aos titulares em três dias úteis.

**Questão 38** (correta: c)
- a. Incorreta: elaborar *playbooks* e treinar é preparação, e a triagem é detecção e análise.
- b. Incorreta: as fases das atividades 2 e 3 foram trocadas.
- c. Correta: *playbooks* e treinamento são preparação; triagem e escopo, detecção e análise; isolar, remover persistência e restaurar, contenção, erradicação e recuperação; lições aprendidas, pós-incidente.
- d. Incorreta: a ordem não corresponde às fases; elaborar *playbooks* não é atividade pós-incidente.
- e. Incorreta: as fases das atividades 3 e 4 foram trocadas.

**Questão 39** (correta: d)
- a. Incorreta: a contenção deve impedir que o dano aumente sem destruir evidências, e a cadeia de custódia não é opcional.
- b. Incorreta: a erradicação vem depois da contenção, e formatar o servidor destruiria as evidências.
- c. Incorreta: a memória é mais volátil do que o disco; por isso, a RFC 3227 manda coletá-la primeiro.
- d. Correta: o desligamento apagou chaves, processos e conexões em memória, e a falta de *hash* e de registro de manuseio quebrou a cadeia de custódia; isolar pelo EDR conteria o ataque preservando a memória.
- e. Incorreta: a cadeia de custódia aplica-se às evidências digitais, como orientam a RFC 3227 e a ABNT NBR ISO/IEC 27037.

**Questão 40** (correta: b)
- a. Incorreta: a ordem está invertida; a falha de *logon* isolada é apenas um evento.
- b. Correta: uma falha de *logon* isolada é um evento; a sinalização de possível atividade maliciosa é um alerta; e o comprometimento efetivo da confidencialidade de dados é um incidente.
- c. Incorreta: a falha de *logon* não foi sinalizada como maliciosa e, portanto, é um evento, não um alerta.
- d. Incorreta: o disparo da regra, ainda não analisado, é um alerta; a cópia confirmada de dados é que configura incidente.
- e. Incorreta: um alerta é a sinalização de possível atividade maliciosa, o que não se aplica a um erro de senha isolado; reveja a distinção entre evento, alerta e incidente.
