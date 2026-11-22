# Questionário — Unidade 2

Disciplina: Red Team & Blue Team Strategies
Professor-conteudista: Afonso Cesar Lelis Brandão
Template de origem: `documentos/Unidade 2/40 Questões - UNI2_nomedadisciplina.docx`

Quantidade obrigatória: 40 questões padrão ENADE — 20 de asserção-razão (1 a 20) e 20 de interpretação (21 a 40).
Cinco alternativas por questão (a–e); a correta é marcada com `*` imediatamente antes da letra.
Feedback para **cada alternativa** (por que está correta ou qual o equívoco), todos ao final do documento.

## Questões

### Asserção-razão

**1.** I. Em uma varredura SYN autorizada (`nmap -sS`), as aplicações que escutam nas portas abertas tendem a registrar pouco ou nada da atividade, embora uma captura de pacotes na rede mostre claramente a varredura.

PORQUE

II. Na varredura SYN, o *scanner* envia um SYN, recebe o SYN/ACK das portas abertas e responde com RST, de modo que o *handshake* TCP nunca se completa.

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**2.** I. Quando o Nmap informa que 99 portas de um *host* estão no estado *filtered*, o mais provável é que um *firewall* esteja descartando os pacotes de teste antes que cheguem ao serviço.

PORQUE

II. O Nmap classifica uma porta como *filtered* quando o *host* responde ao SYN com um pacote RST.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**3.** I. Como o reconhecimento passivo não interage com os sistemas da organização-alvo, a coleta de nomes, cargos e *e-mails* de funcionários em redes sociais dispensa qualquer previsão nas regras de engajamento.

PORQUE

II. Nomes, cargos e endereços de *e-mail* de funcionários são dados pessoais e estão sujeitos à LGPD, mesmo quando publicados pelo próprio titular.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**4.** I. Uma página de login que responde "senha incorreta" para contas existentes e "usuário não encontrado" para contas inexistentes permite que um atacante enumere usuários válidos.

PORQUE

II. O Kali Linux é uma distribuição baseada no Debian, mantida pela OffSec, que reúne ferramentas de teste de segurança.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**5.** I. Uma varredura de portas feita a partir de uma máquina já dentro da rede corporativa corresponde, no MITRE ATT&CK, à técnica T1595 (*Active Scanning*), da tática Reconhecimento.

PORQUE

II. A opção `-sn` do Nmap identifica o programa e a versão de cada serviço que responde nas portas abertas.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

**6.** I. Em um exercício autorizado de Red Team, uma vulnerabilidade apontada pelo *scanner* deve ser confirmada com o teste menos invasivo disponível, registrando-se a evidência mínima, como o código de resposta, a versão do serviço e o horário do teste.

PORQUE

II. *Scanners* de vulnerabilidades costumam deduzir falhas pelo número de versão anunciado pelo serviço, o que gera falsos positivos e não comprova que a falha pode ser explorada naquele ambiente.

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**7.** I. Uma vulnerabilidade com nota-base CVSS 9,8 deve sempre ser testada e corrigida antes de outra com nota 7,5, porque representa necessariamente maior risco para a organização.

PORQUE

II. O EPSS estima a probabilidade de que uma vulnerabilidade seja explorada nos 30 dias seguintes, com base em atividade de exploração observada.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**8.** I. No Metasploit Framework, o comando `check`, disponível em muitos módulos, permite verificar se um alvo parece vulnerável sem explorar a falha, o que o torna compatível com regras de engajamento que proíbem a exploração.

PORQUE

II. Módulos do tipo *payload* são usados para varrer redes e enumerar serviços antes da exploração, sem abrir nenhum acesso no alvo.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**9.** I. O uso de contas válidas (T1078) é uma técnica de acesso inicial que costuma aparecer no relatório do *scanner* de vulnerabilidades, já que toda conta com senha fraca recebe um identificador CVE.

PORQUE

II. Na matriz MITRE ATT&CK, a tática de acesso inicial (TA0001) reúne apenas técnicas de exploração de falhas de *software* com CVE publicado.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

**10.** I. Em uma simulação de *phishing* autorizada, a taxa de reporte é uma das métricas mais úteis para o Blue Team.

PORQUE

II. Uma simulação de *phishing* ética exige autorização formal da liderança e cuidados com a proteção de dados, como não armazenar as senhas digitadas pelos colaboradores.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**11.** I. Em um domínio Windows, um grupo amplo de usuários com permissão de administração local em estações de trabalho pode permitir a escalada de privilégios sem que o adversário explore nenhuma falha de *software*.

PORQUE

II. Com uma conta válida que já recebe privilégios por configuração (T1078), o adversário obtém permissões mais altas usando credenciais e permissões legítimas, sem depender de código de exploração.

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**12.** I. Um *logon* do tipo 10 (remoto interativo), registrado pelo evento 4624, de uma estação da recepção para um servidor de arquivos é um rastro útil para detectar movimentação lateral por RDP.

PORQUE

II. O Windows só registra o evento 4624 do tipo 10 quando a conexão remota é maliciosa, o que dispensa qualquer correlação com o padrão de uso da conta.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**13.** I. Em um exercício de Red Team autorizado, a equipe pode manter um artefato de persistência ativo depois do fim da janela de execução sempre que a área de TI do cliente pedir verbalmente.

PORQUE

II. Nas regras de engajamento, artefatos de persistência devem ser marcados, registrados com hora, máquina e *hash* e removidos até o último dia da janela, com conferência da limpeza.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**14.** I. O evento 4698 do Windows pode revelar a criação de uma tarefa agendada usada como persistência (T1053.005), desde que a auditoria correspondente esteja habilitada.

PORQUE

II. A consulta em massa a usuários e grupos do Active Directory (T1087.002) pertence à tática de Descoberta (TA0007) do MITRE ATT&CK.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**15.** I. Na análise de caminhos de ataque em grafo, a busca em largura é usada porque o primeiro caminho que ela encontra até o alvo é sempre o mais longo, o que mostra o pior cenário.

PORQUE

II. No grafo de permissões do Active Directory, eliminar uma relação mal configurada afeta no máximo um caminho de ataque, por isso as correções precisam ser feitas usuário por usuário.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

**16.** I. Em um servidor Windows cujos logs são encaminhados ao SIEM, apagar o log de Segurança não elimina, por si só, a evidência de que a limpeza ocorreu.

PORQUE

II. Ao limpar o log de Segurança, o próprio Windows grava o evento 1102 (*The audit log was cleared*), que identifica a conta responsável e pode ser encaminhado ao SIEM como qualquer outro evento.

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**17.** I. Encaminhar os logs para fora da máquina assim que são gerados reduz o efeito da técnica *Clear Windows Event Logs* (T1685.005), pois a cópia central continua íntegra depois da limpeza local.

PORQUE

II. A proteção contra adulteração (*tamper protection*) do EDR impede que o agente seja parado ou desinstalado sem autorização da console central e avisa o SOC da tentativa.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**18.** I. Em um exercício autorizado de Red Team, a limpeza pós-operação inclui remover as contas, tarefas agendadas, serviços e arquivos criados pela equipe e entregar o inventário desses artefatos para conferência do Blue Team.

PORQUE

II. Em um exercício autorizado, o Red Team deve apagar os logs de auditoria dos servidores ao final da operação, para devolver o ambiente ao estado em que estava antes do teste.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**19.** I. Na versão atual do MITRE ATT&CK, parar o agente EDR (T1685 — *Disable or Modify Tools*) e alterar a data de criação de um arquivo (T1070.006 — *Timestomp*) pertencem à mesma tática, a Furtividade (*Stealth*, TA0005).

PORQUE

II. O MITRE ATT&CK atual reúne no Enfraquecimento de defesas (*Defense Impairment*, TA0112) as técnicas que desligam ou cegam controles, como T1685, e na Furtividade (TA0005) as técnicas com que o adversário se esconde, como a remoção de indicadores (T1070).

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**20.** I. Uma lacuna no *heartbeat* do agente EDR de um servidor, em horário comercial e sem reinício planejado, deve ser descartada pelo SOC como ruído, porque a ausência de dados não constitui evidência de atividade maliciosa.

PORQUE

II. O evento 2 do Sysmon registra apenas a exclusão de arquivos e, por isso, não contribui para identificar a alteração de datas de arquivos (*timestomp*).

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

### Interpretação

**21.** Em um engajamento autorizado na varejista fictícia LojaNorte, o Red Team identificou 240 subdomínios em bases de transparência de certificados. Desses, 160 ainda respondem na internet. Ao comparar os que respondem com o inventário oficial, a equipe constatou que 24 não constavam em nenhum registro da TI. Qual é a taxa de ativos desconhecidos em relação à superfície ativa?

a. 10%.
b. 24%.
*c. 15%.
d. 66,7%.
e. 85%.

**22.** Durante um exercício autorizado, um analista captura no Wireshark uma varredura SYN contra as 200 portas mais comuns de um servidor. Quatro portas estão abertas e todas as demais estão fechadas, respondendo com RST. Considerando que o *scanner* envia um SYN por porta e encerra com RST cada conexão aceita, quantos pacotes TCP a captura deve conter?

*a. 404.
b. 400.
c. 204.
d. 408.
e. 600.

**23.** Leia o trecho de saída do Nmap, obtido em uma varredura autorizada:

```
Nmap scan report for vpn.exemplo.com.br (203.0.113.30)
Host is up (0.012s latency).
Not shown: 99 filtered tcp ports (no-response)
PORT    STATE SERVICE  VERSION
443/tcp open  ssl/http NetGuard SSL VPN httpd 9.1
```

Qual conclusão é compatível com essa saída?

a. O *host* está desligado, e a linha da porta 443 vem de um *cache* do Nmap.
b. As 99 portas não listadas estão fechadas e o servidor respondeu RST para cada uma delas.
c. A VPN está vulnerável, pois o Nmap só lista versões de serviços com falhas conhecidas.
d. A varredura foi passiva, porque a opção de versão consulta bases públicas em vez do servidor.
*e. Um *firewall* descartou os testes das portas não listadas e apenas o serviço HTTPS da VPN respondeu, informando a versão 9.1.

**24.** Em um teste autorizado, o Red Team observa que o portal de homologação de uma empresa responde "Senha incorreta para joana.reis." em 210 ms quando a conta existe e "Usuário não encontrado." em 30 ms quando a conta não existe. Qual recomendação corrige o problema descrito?

a. Exibir a mensagem de erro apenas em inglês, para dificultar a leitura por atacantes.
*b. Responder com a mesma mensagem genérica e em tempo semelhante para contas existentes e inexistentes.
c. Retirar o campo de senha da página e autenticar apenas pelo nome de usuário.
d. Bloquear o Kali Linux na borda, já que a enumeração depende dessa distribuição.
e. Publicar a lista de usuários válidos, para que os testes deixem de ser necessários.

**25.** Na fictícia Clínica Aurora, que tem 500 colaboradores com *e-mail* corporativo, a fase de OSINT encontrou 300 endereços válidos em fontes públicas, dos quais 270 seguem o formato nome.sobrenome. Qual afirmação está correta?

a. 54% do quadro está exposto e 90% dos endereços seguem o formato dominante.
b. 60% do quadro está exposto e 54% dos endereços seguem o formato dominante.
c. 90% do quadro está exposto e 60% dos endereços seguem o formato dominante.
*d. 60% do quadro está exposto e 90% dos endereços seguem o formato dominante.
e. 30% do quadro está exposto e 27% dos endereços seguem o formato dominante.

**26.** A equipe de TI da distribuidora fictícia NorteFarma corrige, no máximo, 200 vulnerabilidades por semana. O relatório do *scanner* trouxe 1.600 achados, dos quais 640 têm CVSS ≥ 7,0. Filtrando apenas os achados no catálogo KEV ou com EPSS ≥ 10% em ativos expostos à internet, restam 80. Quanto tempo a equipe levaria para tratar cada fila?

a. 3,2 semanas para a fila de CVSS e 0,8 semana para a fila crítica.
b. 8 semanas para a fila de CVSS e 0,4 semana para a fila crítica.
*c. 3,2 semanas para a fila de CVSS e 0,4 semana para a fila crítica.
d. 0,4 semana para a fila de CVSS e 3,2 semanas para a fila crítica.
e. 4 semanas para a fila de CVSS e 0,5 semana para a fila crítica.

**27.** Em um exercício autorizado, o Red Team de um hospital fictício avalia três achados:

| Achado | CVSS | EPSS | No KEV? | Ativo |
|---|---|---|---|---|
| X | 9,8 | 0,03 | Não | Servidor interno isolado |
| Y | 7,5 | 0,91 | Sim | Portal de agendamento exposto à internet |
| Z | 6,1 | 0,05 | Não | Estação administrativa interna |

Considerando a priorização por risco estudada na aula, qual achado deve ser verificado primeiro e por quê?

a. X, porque tem a maior nota CVSS e, portanto, o maior risco.
b. Z, porque está em uma estação usada pela administração.
c. X e Z empatados, porque ambos estão na rede interna.
d. Nenhum, porque falhas no KEV não podem ser testadas em exercícios.
*e. Y, porque combina exploração confirmada (KEV), alta probabilidade de exploração e exposição à internet.

**28.** Durante um exercício autorizado, um analista do Red Team executa no `msfconsole` o comando `check` contra a VPN de uma empresa fictícia e recebe a resposta "*The target appears to be vulnerable*". Qual é a interpretação adequada desse resultado?

*a. Há evidência indireta, baseada em versão ou comportamento, de que a falha existe; o achado vai ao relatório com a hora do teste, sem exploração.
b. A falha foi explorada com sucesso e uma sessão foi aberta no alvo.
c. O alvo está fora do escopo e o Metasploit bloqueou o teste.
d. A VPN é certamente segura, pois o módulo não encontrou nenhum indício de falha.
e. O resultado autoriza a equipe a configurar um *payload* para confirmar a falha, mesmo que a RoE proíba a exploração.

**29.** As regras de engajamento de um exercício em uma rede fictícia de escolas preveem: "verificar falhas em aplicações expostas sem ler dados reais; nos serviços remotos, só verificação de versão e comportamento; contas válidas apenas com contas de teste criadas pela TI; *phishing* apenas educativo, sem armazenar senhas". O Red Team encontra um portal de matrículas com uma falha de leitura de arquivos e quer copiar a lista de alunos para "provar o impacto". Qual conduta está de acordo com as regras?

a. Copiar a lista inteira, pois só assim o impacto fica comprovado.
*b. Confirmar a falha com o teste menos invasivo, registrar versão, resposta e horário como evidência e não acessar a lista de alunos.
c. Copiar apenas os dados dos alunos maiores de idade.
d. Abandonar o achado, pois falhas de leitura de arquivos não fazem parte do acesso inicial.
e. Explorar a falha fora da janela autorizada, para não alertar o SOC.

**30.** Ao revisar os registros de um exercício, a analista de SOC de uma empresa fictícia encontra: (1) 1.800 falhas de login no aplicativo, vindas de 25 endereços, seguidas de 11 logins bem-sucedidos; (2) requisições com sequências codificadas de travessia de diretório no log do servidor *web* do portal; (3) acesso de um colaborador a um domínio registrado havia dois dias, logo após um *e-mail* externo. Que técnicas de acesso inicial esses rastros sugerem, respectivamente?

a. T1566.002, T1078 e T1190.
b. T1190, T1133 e T1078.
c. T1133, T1566.002 e T1190.
*d. Uso de contas válidas após tentativas com senhas vazadas (T1078), exploração de aplicação exposta (T1190) e *phishing* com *link* (T1566.002).
e. T1078, T1133 e T1566.001.

**31.** Em um exercício autorizado na distribuidora fictícia Logística Sul, a análise de grafo mostrou que 2.000 de 8.000 contas do domínio tinham algum caminho até o grupo de administradores do domínio. Depois de corrigir as sessões de administradores em dois servidores e as permissões de um grupo de suporte, restaram 160 contas com caminho. Qual é o percentual de contas com caminho após as correções e a redução percentual dos caminhos?

a. 25% e 8%.
*b. 2% e 92%.
c. 8% e 92%.
d. 2% e 80%.
e. 1,6% e 98%.

**32.** Durante a revisão de um exercício na clínica fictícia Vida Plena, o SOC encontra no servidor `SRV-LAB-02` um evento 7045 no log *System*, registrado às 15h12, com o nome `RT-APR3104-marca`, mesmo código do chamado de autorização do exercício. Qual é a interpretação mais adequada?

a. Uma conta de domínio foi criada pelo Red Team, técnica T1136.002.
b. Houve *logon* remoto interativo por RDP, técnica T1021.001.
c. Um valor foi gravado em uma chave *Run* do registro, técnica T1547.001.
*d. Um serviço novo foi instalado como persistência marcada do exercício, técnica T1543.003, que deve constar do registro do Red Team e ser removido até o fim da janela.
e. O controle de conta de usuário foi desviado, técnica T1548.002.

**33.** Em um exercício autorizado, o Red Team roda no Kali Linux o módulo `auxiliary/scanner/smb/smb_version` do Metasploit contra três servidores do escopo e obtém, para um deles, a linha "SMB Detected (versions:1, 2, 3) (signatures:optional)". Qual é a interpretação correta?

*a. O módulo apenas identificou as versões do SMB aceitas e a assinatura não exigida; é um achado de configuração a relatar, obtido dentro de uma autorização que permite módulos de descoberta.
b. O módulo explorou uma falha do SMB 1 e obteve acesso administrativo ao servidor.
c. O módulo extraiu as credenciais armazenadas no servidor, pois a assinatura é opcional.
d. A linha indica que o servidor é um controlador de domínio, já que aceita a versão 1 do SMB.
e. O resultado prova que o servidor já foi comprometido por um adversário real antes do exercício.

**34.** A diretoria da academia fictícia Faixa Preta quer saber, sem esperar um *phishing* bem-sucedido, o que um adversário conseguiria fazer depois de entrar com a conta de um funcionário comum. A CISO propõe entregar ao Red Team uma conta de teste com os mesmos grupos de um funcionário da recepção, dentro da carta de autorização. Esse desenho corresponde a qual abordagem?

a. Reconhecimento passivo, porque a equipe não interage com os sistemas.
b. Teste de caixa-branca do código-fonte do sistema de matrículas.
c. Simulação de *phishing* com finalidade educativa.
d. Exercício de mesa (*tabletop*), sem nenhuma ação técnica.
*e. Cenário de acesso presumido (*assumed breach*), que começa na pós-exploração para medir descoberta, escalada, movimentação lateral e persistência.

**35.** Na plataforma de um exercício, a emulação de uma cadeia de *ransomware* termina com 3 passos detectados, 2 não detectados e 3 "vistos nos logs, sem alerta": uma consulta em massa ao AD e dois acessos por RDP a servidores. Depois de ligar as regras de correlação para essas duas técnicas, sem mudar nenhuma fonte, a repetição mostra 6 detectados e nenhum visto sem alerta. O que esse resultado indica?

a. Que as fontes de telemetria do AD estavam desligadas na primeira rodada.
b. Que o Red Team deixou de executar os três passos na segunda rodada.
*c. Que os eventos já chegavam ao SIEM, e a lacuna estava na ausência de regras que os transformassem em alerta.
d. Que as duas regras novas também passaram a detectar a exfiltração e o impacto.
e. Que a detecção ficou completa, pois nenhum passo deixou de gerar alerta.

**36.** Em um exercício autorizado na distribuidora fictícia Vale Verde, o agente EDR de um servidor de banco de dados ficou parado das 10h12 às 11h02, sem que nenhum alerta fosse gerado. O SOC propõe uma regra que dispare quando um agente ficar mais de 15 minutos sem *heartbeat*. Se a regra já existisse, em quanto o tempo em que o SOC ficou sem saber da parada teria sido reduzido, em termos percentuais?

*a. 70%.
b. 30%.
c. 15%.
d. 50%.
e. 35%.

**37.** No relatório de um exercício autorizado na mesma distribuidora, o Red Team registra que emulou 8 técnicas de evasão de defesas, das quais o SOC detectou em tempo real 2: a limpeza de um log de Segurança (pelo evento 1102) e uma tentativa de parar o EDR (barrada pela proteção contra adulteração). As outras 6 deixaram eventos no SIEM, mas nenhuma regra os transformou em alerta. Qual é a taxa de detecção da fase de evasão?

a. 2%.
*b. 25%.
c. 75%.
d. 33%.
e. 80%.

**38.** Ao revisar um exercício autorizado, uma analista de SOC consulta os eventos 2 do Sysmon (data de criação de arquivo alterada) de dois servidores e obtém duas linhas: na primeira, o processo `msiexec.exe` altera a data de uma biblioteca em `C:\Program Files\Backup`; na segunda, um executável rodando de `C:\Users\Public` altera para 2023 a data de criação de um arquivo que surgiu no mesmo dia em uma pasta de exportações. Qual interpretação é a mais adequada?

a. As duas linhas indicam *timestomp*, pois todo evento 2 do Sysmon é sinal de atividade maliciosa e deve gerar alerta crítico.
b. Nenhuma das linhas merece atenção, pois o evento 2 do Sysmon só registra arquivos apagados.
*c. A segunda linha é um forte indício de *timestomp* (T1070.006) e merece investigação, porque combina processo em pasta pública e data recuada em um arquivo recente; a primeira é compatível com o comportamento normal de um instalador.
d. A primeira linha é a mais suspeita, pois instaladores legítimos nunca alteram datas de arquivos.
e. A análise é inútil, pois, se o adversário alterou a data, o SIEM também perdeu o registro original do arquivo.

**39.** Ao final de um exercício autorizado, o Red Team entrega um inventário com 15 artefatos que afirma ter removido. A varredura do Blue Team confirma a remoção de 13, encontra ainda presente uma conta local listada no inventário e encontra uma tarefa agendada desconhecida, que não consta do inventário nem traz o código do exercício. Qual é a conduta mais adequada?

a. Encerrar o exercício, pois mais de 85% dos artefatos foram conferidos.
b. Pedir ao Red Team que remova também a tarefa desconhecida, já que tudo o que aparece durante o exercício é responsabilidade dele.
c. Apagar os logs dos servidores afetados para que o relatório não mostre as pendências.
*d. Manter a conta local como pendência do Red Team até a remoção ser conferida e tratar a tarefa desconhecida como suspeita de incidente real, acionando o processo de resposta a incidentes.
e. Ignorar as duas divergências, pois a limpeza é uma etapa opcional em exercícios internos.

**40.** A equipe que planeja um exercício autorizado quer incluir técnicas de evasão de defesas para medir a capacidade de detecção do SOC. Qual cláusula das regras de engajamento é a mais adequada?

a. O Red Team poderá desligar o EDR de todos os notebooks e servidores da sede durante a semana do exercício, sem comunicar ninguém, para tornar o teste mais realista.
b. O Red Team poderá apagar os logs do SIEM ao final da operação, para que o Blue Team não tenha acesso antecipado ao resultado.
c. O Red Team poderá emular qualquer técnica de evasão, em qualquer servidor, desde que não use *malware*.
d. O Red Team decidirá durante a operação quais técnicas de evasão usar, informando o White Team só no relatório final.
*e. O Red Team poderá parar o agente EDR em dois servidores definidos, por até 40 minutos e na janela combinada com o White Team, religando-o ao fim; limpar um log só será permitido depois de confirmado o seu encaminhamento ao SIEM.

## Gabarito e feedbacks

**Questão 1** (correta: a)
- a. Correta: como o *handshake* nunca se completa (II), a conexão não chega à aplicação e ela registra pouco, enquanto a rede vê cada SYN e RST (I); a II explica a I.
- b. Incorreta: a II não é apenas verdadeira, ela é a causa do baixo registro na aplicação descrito na I.
- c. Incorreta: a II é verdadeira; é exatamente o funcionamento da varredura de meia abertura visto no laboratório do Wireshark.
- d. Incorreta: a I é verdadeira; a captura mostra a varredura, mas a aplicação quase não a registra.
- e. Incorreta: ambas as asserções são verdadeiras. Revise a seção "Varredura e descoberta de serviços".

**Questão 2** (correta: c)
- a. Incorreta: a II é falsa, logo não pode justificar a I.
- b. Incorreta: a II é falsa; resposta RST indica porta fechada (*closed*), e não filtrada.
- c. Correta: a I é verdadeira, pois *filtered* significa que nada voltou, sinal típico de *firewall*; a II é falsa, pois RST corresponde ao estado *closed*.
- d. Incorreta: a I é verdadeira; no laboratório, a VPN atrás de *firewall* mostrou 99 portas filtradas.
- e. Incorreta: a I é verdadeira. Revise os três estados de porta do Nmap.

**Questão 3** (correta: d)
- a. Incorreta: a I é falsa; mesmo o reconhecimento passivo sobre pessoas precisa estar previsto nas regras de engajamento.
- b. Incorreta: a I é falsa, portanto não há relação de justificativa a avaliar.
- c. Incorreta: a combinação é a inversa: a I é falsa e a II é verdadeira.
- d. Correta: a I é falsa, porque a coleta de dados de funcionários exige previsão nas regras de engajamento; a II é verdadeira, porque esses dados são pessoais e a LGPD se aplica.
- e. Incorreta: a II é verdadeira. Revise "Limites éticos, legais e de escopo".

**Questão 4** (correta: b)
- a. Incorreta: as duas são verdadeiras, mas a descrição do Kali não explica por que mensagens de erro diferentes permitem enumerar contas.
- b. Correta: a I descreve a enumeração por mensagens de erro (WSTG-IDNT-04) e a II descreve corretamente o Kali, mas a falha está no projeto da página, e não na ferramenta usada.
- c. Incorreta: a II é verdadeira; o Kali é baseado no Debian e mantido pela OffSec.
- d. Incorreta: a I é verdadeira; mensagens diferentes confirmam quais contas existem.
- e. Incorreta: ambas as asserções são verdadeiras.

**Questão 5** (correta: e)
- a. Incorreta: as duas asserções são falsas.
- b. Incorreta: as duas asserções são falsas, portanto não podem ser ambas verdadeiras.
- c. Incorreta: a I é falsa; varredura feita de dentro da rede é T1046 (*Network Service Discovery*), da tática Descoberta (TA0007).
- d. Incorreta: a II é falsa; `-sn` apenas descobre *hosts* ativos, e quem identifica versões é `-sV`.
- e. Correta: a I confunde T1595, usada de fora, com T1046, usada de dentro; a II atribui à `-sn` a função da `-sV`.

**Questão 6** (correta: a)
- a. Correta: a I descreve o princípio de demonstrar, e não executar; a II explica por que a confirmação é necessária, já que o *scanner* deduz pela versão, erra e não prova a explorabilidade.
- b. Incorreta: a II não é um fato independente; é justamente o motivo pelo qual o achado precisa ser confirmado antes de entrar no relatório.
- c. Incorreta: a II é verdadeira; *scanners* geram falsos positivos ao inferir falhas pela versão anunciada.
- d. Incorreta: a I é verdadeira; a validação com o teste menos invasivo e a evidência mínima é a regra dos exercícios autorizados.
- e. Incorreta: as duas asserções são verdadeiras. Revise "Da vulnerabilidade à exploração controlada".

**Questão 7** (correta: d)
- a. Incorreta: a I é falsa, pois a nota-base do CVSS mede severidade técnica, e não risco.
- b. Incorreta: a alternativa considera a I verdadeira, mas a prioridade também depende de EPSS, KEV, exposição e criticidade do ativo.
- c. Incorreta: a I é falsa e a II é verdadeira; a combinação é a inversa.
- d. Correta: a I é falsa, porque uma falha 7,5 explorada e exposta pode ser mais urgente que uma 9,8 em servidor isolado; a II descreve corretamente o EPSS.
- e. Incorreta: a II é verdadeira; o EPSS, do FIRST, estima a probabilidade de exploração nos 30 dias seguintes.

**Questão 8** (correta: c)
- a. Incorreta: a II é falsa e não pode justificar a I.
- b. Incorreta: a II é falsa; quem varre e enumera são os módulos *auxiliary*.
- c. Correta: a I é verdadeira, pois o `check` verifica sem explorar; a II é falsa, pois o *payload* é o código que roda no alvo depois da exploração.
- d. Incorreta: a I é verdadeira; o `check` é o recurso usado na aula justamente por não explorar a falha.
- e. Incorreta: a I é verdadeira. Revise os tipos de módulo do Metasploit.

**Questão 9** (correta: e)
- a. Incorreta: as duas asserções são falsas.
- b. Incorreta: contas válidas não recebem CVE, e a TA0001 inclui técnicas sem CVE, como T1078 e T1566.
- c. Incorreta: a I é falsa; contas válidas não aparecem no relatório do *scanner* e só são reveladas por teste.
- d. Incorreta: a II é falsa; a tática de acesso inicial inclui serviços remotos, contas válidas e *phishing*, além da exploração de aplicações.
- e. Correta: a I é falsa, pois credenciais fracas ou reutilizadas não têm CVE; a II é falsa, pois a TA0001 vai além de falhas de *software*.

**Questão 10** (correta: b)
- a. Incorreta: a II é verdadeira, mas trata das condições éticas da simulação, e não do motivo pelo qual a taxa de reporte é útil.
- b. Correta: as duas são verdadeiras; a taxa de reporte importa porque um aviso rápido permite ao SOC bloquear a mensagem para todos, razão que a II não apresenta.
- c. Incorreta: a II é verdadeira; autorização formal e proteção de dados são exigências de uma simulação ética.
- d. Incorreta: a I é verdadeira; a taxa de reporte mede a capacidade humana de detectar e acionar a defesa.
- e. Incorreta: as duas asserções são verdadeiras. Revise "*Phishing* como vetor autorizado".

**Questão 11** (correta: a)
- a. Correta: a I é verdadeira, pois administração local concedida a um grupo amplo dá privilégio por configuração; a II explica o motivo, já que contas válidas (T1078) dispensam código de exploração.
- b. Incorreta: a II não é só verdadeira, ela é a razão da I. Revise a tabela de caminhos de escalada.
- c. Incorreta: a II é verdadeira; contas válidas são justamente o atalho que dispensa exploração de falha.
- d. Incorreta: a I é verdadeira; dois dos quatro caminhos de escalada da aula não exploram falha de *software*.
- e. Incorreta: ambas são verdadeiras. Revise "Escalada de privilégios".

**Questão 12** (correta: c)
- a. Incorreta: a II é falsa, logo não justifica a I.
- b. Incorreta: a II é falsa; o 4624 do tipo 10 é gerado por qualquer *logon* remoto interativo, legítimo ou não.
- c. Correta: a I é verdadeira, pois o *logon* tipo 10 de uma estação da recepção para um servidor é a combinação incomum que sinaliza movimentação lateral; a II é falsa, pois administradores geram esse evento todos os dias e a detecção depende de correlação com o padrão da conta.
- d. Incorreta: a I é verdadeira; o evento é o rastro do RDP (T1021.001).
- e. Incorreta: a I é verdadeira. Revise "Movimentação lateral".

**Questão 13** (correta: d)
- a. Incorreta: a I é falsa; um pedido verbal não altera a janela nem a carta de autorização.
- b. Incorreta: a I é falsa; manter o artefato além da janela contraria as regras de engajamento.
- c. Incorreta: a combinação é a inversa; a I é falsa e a II é verdadeira.
- d. Correta: a I é falsa, porque só quem assinou a autorização pode alterá-la, por escrito, e o artefato esquecido vira uma porta real; a II é verdadeira e descreve a regra de persistência marcada, registrada e removida.
- e. Incorreta: a II é verdadeira. Revise "Limites no engajamento".

**Questão 14** (correta: b)
- a. Incorreta: as duas são verdadeiras, mas tratam de assuntos diferentes; a tática da consulta ao AD não explica o evento de tarefa agendada.
- b. Correta: a I é verdadeira (o 4698 registra tarefas criadas quando a auditoria *Other Object Access Events* está ligada) e a II também (T1087.002 é Descoberta), mas a II não justifica a I.
- c. Incorreta: a II é verdadeira; a descoberta de contas de domínio pertence à TA0007.
- d. Incorreta: a I é verdadeira; o 4698 é o rastro típico da T1053.005.
- e. Incorreta: ambas são verdadeiras. Revise as tabelas de descoberta e persistência.

**Questão 15** (correta: e)
- a. Incorreta: as duas asserções são falsas.
- b. Incorreta: nenhuma das asserções é verdadeira.
- c. Incorreta: a I é falsa; a busca em largura visita primeiro os vizinhos a um salto, por isso encontra o caminho mais curto.
- d. Incorreta: a II é falsa; uma única relação mal configurada pode estar em dezenas de caminhos, como mostrou o corte da sessão do administrador no servidor de arquivos.
- e. Correta: a I é falsa (a BFS devolve o menor caminho) e a II é falsa (cortar uma relação elimina muitos caminhos de uma vez). Revise "Caminhos de ataque em grafos".

**Questão 16** (correta: a)
- a. Correta: a limpeza do log de Segurança não apaga a própria evidência (I) justamente porque o Windows grava o evento 1102 ao limpar e esse evento chega ao SIEM pelo encaminhamento (II); a II explica a I.
- b. Incorreta: a II não é apenas verdadeira, ela é a razão pela qual a limpeza continua visível. Revise "Toda técnica de evasão deixa um rastro próprio".
- c. Incorreta: a II é verdadeira; o evento 1102 (*The audit log was cleared*) é gerado pelo próprio Windows e registra a conta responsável.
- d. Incorreta: a I é verdadeira; com encaminhamento, a limpeza leva só a cópia local e o SIEM recebe o 1102.
- e. Incorreta: as duas asserções são verdadeiras. Revise a relação entre o evento 1102 e o encaminhamento de logs.

**Questão 17** (correta: b)
- a. Incorreta: as duas asserções são verdadeiras, mas a proteção contra adulteração do EDR não explica por que o encaminhamento de logs reduz o efeito da limpeza; são defesas diferentes.
- b. Correta: o encaminhamento preserva a cópia central (I) e a proteção contra adulteração impede que o agente seja parado sem autorização (II); as duas afirmações são verdadeiras, mas tratam de técnicas distintas, T1685.005 e T1685.
- c. Incorreta: a II é verdadeira; a proteção contra adulteração bloqueia a parada do agente e avisa o SOC, como na tentativa contra o `SRV-ARQ-01`.
- d. Incorreta: a I é verdadeira; é a primeira das duas defesas que tornam a evasão cara, segundo o texto da aula.
- e. Incorreta: ambas são verdadeiras. Revise "Duas defesas que tornam a evasão cara".

**Questão 18** (correta: c)
- a. Incorreta: a II é falsa, logo não pode justificar a I.
- b. Incorreta: a II é falsa; nenhum registro de auditoria é apagado na limpeza pós-operação, porque os logs são evidência do exercício.
- c. Correta: a I descreve a limpeza legítima (remover o que foi criado e entregar o inventário para conferência); a II é falsa, pois apagar logs de auditoria destruiria a evidência que o Blue Team e o relatório usam.
- d. Incorreta: a I é verdadeira; é exatamente o que a aula chama de limpeza legítima de rastros.
- e. Incorreta: a I é verdadeira. Revise "Limpeza legítima de rastros".

**Questão 19** (correta: d)
- a. Incorreta: a I é falsa, então a combinação "ambas verdadeiras" não se aplica.
- b. Incorreta: a I é falsa; T1685 pertence ao Enfraquecimento de defesas (TA0112), e não à Furtividade.
- c. Incorreta: a combinação é a inversa; a I é falsa e a II é verdadeira.
- d. Correta: a I é falsa, pois parar o EDR (T1685) está no Enfraquecimento de defesas (TA0112) e o *timestomp* (T1070.006) está na Furtividade (TA0005); a II descreve corretamente essa divisão do ATT&CK atual.
- e. Incorreta: a II é verdadeira. Revise "Furtividade e enfraquecimento de defesas".

**Questão 20** (correta: e)
- a. Incorreta: as duas asserções são falsas.
- b. Incorreta: as duas asserções são falsas; não há o que justificar.
- c. Incorreta: a I é falsa; um servidor que para de enviar *heartbeat* em horário comercial, sem reinício planejado, merece investigação, como os 38 minutos do `SRV-ERP-01`.
- d. Incorreta: a II é falsa; o evento 2 do Sysmon registra justamente a alteração da data de criação de arquivo, sinal típico de *timestomp*. Arquivos apagados aparecem nos eventos 23 e 26.
- e. Correta: a I é falsa, pois a ausência de *heartbeat* é um sinal da técnica T1685; a II também é falsa, pois o evento 2 do Sysmon é o rastro característico do *timestomp* (T1070.006).

**Questão 21** (correta: c)
- a. Incorreta: 10% seria 24 ÷ 240, que usa o total de certificados, e não a superfície ativa.
- b. Incorreta: 24% confunde a quantidade de ativos desconhecidos com uma porcentagem.
- c. Correta: 24 ÷ 160 = 0,15, ou seja, 15% da superfície ativa é desconhecida.
- d. Incorreta: 66,7% é 160 ÷ 240, a proporção de subdomínios que respondem, e não a de desconhecidos.
- e. Incorreta: 85% é a parcela da superfície ativa que consta do inventário.

**Questão 22** (correta: a)
- a. Correta: 200 SYN + 4 SYN/ACK + 4 RST do *scanner* + 196 RST/ACK das portas fechadas = 404 pacotes.
- b. Incorreta: 400 considera um SYN e uma resposta por porta, mas esquece os 4 RST que o *scanner* envia após cada SYN/ACK.
- c. Incorreta: 204 conta só os SYN e as respostas das portas abertas, ignorando os RST/ACK das portas fechadas.
- d. Incorreta: 408 soma pacotes a mais, como se cada porta aberta gerasse dois RST.
- e. Incorreta: 600 corresponde a um *handshake* completo de três pacotes em todas as portas, o que não ocorre na varredura SYN.

**Questão 23** (correta: e)
- a. Incorreta: a linha "Host is up" mostra que o *host* respondeu na varredura.
- b. Incorreta: portas fechadas aparecem como *closed* (resposta RST); *filtered* indica ausência de resposta.
- c. Incorreta: o Nmap lista os serviços que respondem, vulneráveis ou não; a verificação de falhas é outra etapa (Aula 6).
- d. Incorreta: a identificação de versão conversa com o próprio serviço, portanto é reconhecimento ativo.
- e. Correta: *filtered* (*no-response*) indica pacotes descartados, típico de *firewall*, e só a porta 443 respondeu, com a versão informada pelo serviço.

**Questão 24** (correta: b)
- a. Incorreta: trocar o idioma não remove a diferença entre as mensagens nem a diferença de tempo.
- b. Correta: mensagem genérica e tempo de resposta semelhante impedem que o atacante distinga contas existentes, como no portal de produção do laboratório.
- c. Incorreta: remover a senha enfraqueceria a autenticação e não resolve a enumeração.
- d. Incorreta: a enumeração independe da ferramenta ou do sistema operacional do atacante.
- e. Incorreta: publicar a lista entregaria ao adversário exatamente o que a enumeração busca.

**Questão 25** (correta: d)
- a. Incorreta: 54% é 270 ÷ 500, que mistura o numerador do formato com o total do quadro.
- b. Incorreta: os percentuais estão trocados e calculados sobre bases erradas.
- c. Incorreta: os dois percentuais estão invertidos.
- d. Correta: 300 ÷ 500 = 60% do quadro exposto e 270 ÷ 300 = 90% dos endereços no formato nome.sobrenome.
- e. Incorreta: 30% e 27% dividem os valores por 1.000, uma base que não existe no enunciado.

**Questão 26** (correta: c)
- a. Incorreta: a fila crítica é 80 ÷ 200 = 0,4 semana, e não 0,8.
- b. Incorreta: 8 semanas seria 1.600 ÷ 200, o relatório inteiro, e não a fila de CVSS ≥ 7,0.
- c. Correta: 640 ÷ 200 = 3,2 semanas e 80 ÷ 200 = 0,4 semana, cerca de dois dias úteis.
- d. Incorreta: os valores estão invertidos entre as filas.
- e. Incorreta: os cálculos não correspondem a 640 ÷ 200 nem a 80 ÷ 200.

**Questão 27** (correta: e)
- a. Incorreta: o CVSS mede severidade técnica; X tem EPSS baixo e está isolado, o que reduz o risco.
- b. Incorreta: Z tem CVSS e EPSS baixos e não está exposto; a função do usuário não o torna prioritário.
- c. Incorreta: estar na rede interna não gera empate; os dois têm risco baixo frente a Y.
- d. Incorreta: falhas no KEV são justamente as primeiras a verificar, com o teste menos invasivo permitido.
- e. Correta: Y reúne exploração confirmada, EPSS alto e exposição à internet; por isso lidera a fila de teste e de correção.

**Questão 28** (correta: a)
- a. Correta: *appears* indica evidência indireta, de versão ou comportamento; o achado é registrado com hora, sem exploração.
- b. Incorreta: o `check` não explora a falha nem abre sessão.
- c. Incorreta: a mensagem indica possível vulnerabilidade, e não bloqueio por escopo.
- d. Incorreta: a resposta aponta o contrário: o alvo parece vulnerável.
- e. Incorreta: a RoE prevalece; se ela proíbe exploração, configurar um *payload* violaria o escopo autorizado.

**Questão 29** (correta: b)
- a. Incorreta: as regras proíbem ler dados reais; o impacto é demonstrado, e não executado.
- b. Correta: confirmar a falha com o teste menos invasivo e registrar a evidência mínima segue o princípio de demonstrar, e não executar.
- c. Incorreta: dados de alunos maiores também são dados pessoais protegidos pela LGPD e pelas regras do exercício.
- d. Incorreta: a falha em aplicação exposta é acesso inicial (T1190) e deve constar do relatório.
- e. Incorreta: agir fora da janela autorizada viola as regras de engajamento e pode configurar crime.

**Questão 30** (correta: d)
- a. Incorreta: a ordem está trocada; o primeiro rastro indica contas válidas, e não *phishing*.
- b. Incorreta: o primeiro rastro não é exploração de aplicação, e o terceiro não é uso de serviço remoto.
- c. Incorreta: não há indício de serviço remoto exposto (T1133) nos registros descritos.
- d. Correta: falhas seguidas de sucesso indicam contas válidas (T1078); travessia de diretório no log *web* indica T1190; domínio recém-registrado após *e-mail* externo indica *phishing* com *link* (T1566.002).
- e. Incorreta: o segundo rastro é de aplicação exposta (T1190), e o terceiro é *phishing* com *link* (.002), e não com anexo (.001).

**Questão 31** (correta: b)
- a. Incorreta: 25% é a situação antes das correções (2.000 ÷ 8.000), e 8% não corresponde a nenhum cálculo pedido.
- b. Correta: após as correções, 160 ÷ 8.000 = 2%; a redução é (2.000 − 160) ÷ 2.000 = 1.840 ÷ 2.000 = 92%.
- c. Incorreta: 8% é 160 ÷ 2.000, a fração que restou dos caminhos, e não o percentual de contas do domínio.
- d. Incorreta: o primeiro valor está certo, mas a redução é 92%, e não 80%.
- e. Incorreta: os dois valores não resultam dos dados; refaça as divisões por 8.000 e por 2.000.

**Questão 32** (correta: d)
- a. Incorreta: a criação de conta gera o evento 4720, e não o 7045.
- b. Incorreta: o RDP aparece como 4624 do tipo 10.
- c. Incorreta: a alteração de chave *Run* aparece no Sysmon como evento 13.
- d. Correta: o 7045 registra serviço instalado (T1543.003); a marca com o código do chamado indica persistência do exercício, que precisa estar no registro do Red Team e ser removida até o fim da janela.
- e. Incorreta: o desvio do UAC deixa um processo elevado sem confirmação, não um serviço novo.

**Questão 33** (correta: a)
- a. Correta: o `smb_version` é um módulo *auxiliary* de descoberta; ele só identifica versões e a exigência de assinatura, e SMB 1 aceito com assinatura opcional é um achado de configuração.
- b. Incorreta: módulos *auxiliary/scanner* não exploram falhas nem dão acesso.
- c. Incorreta: o módulo não extrai credenciais; a assinatura opcional é um risco a relatar, não uma extração.
- d. Incorreta: aceitar SMB 1 não identifica controlador de domínio; na aula, o controlador se distingue por Kerberos (88) e LDAP (389).
- e. Incorreta: uma configuração fraca não é evidência de comprometimento anterior.

**Questão 34** (correta: e)
- a. Incorreta: a equipe interage com os sistemas usando a conta de teste; não é reconhecimento passivo.
- b. Incorreta: não há análise de código-fonte no desenho proposto.
- c. Incorreta: o objetivo é medir o que acontece depois da entrada, sem enviar iscas.
- d. Incorreta: no *tabletop* não há ação técnica; aqui o Red Team atua no ambiente.
- e. Correta: entregar uma conta comum autorizada para começar na pós-exploração é o cenário de acesso presumido descrito na aula.

**Questão 35** (correta: c)
- a. Incorreta: as fontes não mudaram entre as rodadas; se estivessem desligadas, ligar regras não bastaria.
- b. Incorreta: os mesmos passos foram executados nas duas rodadas.
- c. Correta: "visto nos logs, sem alerta" significa que o evento chegou e faltava a regra; ligar as regras, sem mudar fontes, transformou esses eventos em detecção.
- d. Incorreta: os 2 passos não detectados continuaram assim; dependem de outra fonte.
- e. Incorreta: 2 passos continuaram não detectados, então a detecção não ficou completa.

**Questão 36** (correta: a)
- a. Correta: a parada durou 50 minutos (10h12 a 11h02). Com a regra, o alerta sairia às 10h27, 15 minutos depois; o tempo sem saber cairia de 50 para 15 minutos, uma redução de 35 ÷ 50 = 70%.
- b. Incorreta: 30% é a fração do tempo que continuaria cega (15 ÷ 50), e não a redução.
- c. Incorreta: 15 é o limite da regra em minutos, e não um percentual.
- d. Incorreta: 50 é a duração da parada em minutos; a redução é calculada sobre ela.
- e. Incorreta: 35 é o número de minutos economizados; dividido pelos 50 minutos da parada, dá 70%.

**Questão 37** (correta: b)
- a. Incorreta: 2 é o número de técnicas detectadas, e não a taxa.
- b. Correta: a taxa de detecção é o número de técnicas detectadas dividido pelo total emulado: 2 ÷ 8 = 25%.
- c. Incorreta: 75% é a taxa de técnicas não detectadas (6 ÷ 8).
- d. Incorreta: 33% seria 2 ÷ 6, que divide as detectadas pelas não detectadas, e não pelo total.
- e. Incorreta: 80% não corresponde a nenhuma razão entre os números do enunciado.

**Questão 38** (correta: c)
- a. Incorreta: o evento 2 do Sysmon é ruidoso, porque instaladores e atualizações alteram datas legitimamente; tratar todo evento como crítico gera falsos positivos.
- b. Incorreta: o evento 2 registra a alteração da data de criação de arquivo; arquivos apagados aparecem nos eventos 23 e 26.
- c. Correta: o que destoa é o contexto, como na aula: processo rodando de pasta pública e data recuada em um arquivo criado no mesmo dia indicam possível *timestomp* (T1070.006); a primeira linha é compatível com um instalador.
- d. Incorreta: instaladores alteram datas de arquivos com frequência; por isso a primeira linha é a menos suspeita.
- e. Incorreta: o evento 2 registra a data anterior e a nova e foi encaminhado ao SIEM; a análise continua possível.

**Questão 39** (correta: d)
- a. Incorreta: o exercício só termina quando as pendências zeram, e um artefato desconhecido não pode ser ignorado.
- b. Incorreta: um artefato fora do inventário e sem o código do exercício não pode ser presumido como do Red Team; ele é tratado como suspeita de incidente real.
- c. Incorreta: apagar logs destrói evidência e contraria as regras de engajamento; a limpeza legítima não apaga registros de auditoria.
- d. Correta: a conta listada volta ao Red Team até a remoção ser conferida, e o artefato desconhecido deixa de ser assunto do exercício e segue o processo de resposta a incidentes.
- e. Incorreta: a limpeza comprovada é obrigatória ao final de um exercício autorizado, mesmo interno.

**Questão 40** (correta: e)
- a. Incorreta: desligar defesas de toda a sede, sem prazo e sem comunicação, expõe a empresa a ameaças reais e contraria o princípio de que a evasão só entra para medir a detecção, combinada com o White Team.
- b. Incorreta: os logs do SIEM são evidência do exercício e nunca devem ser apagados.
- c. Incorreta: a regra de engajamento precisa listar cada técnica e os servidores autorizados; "qualquer técnica, em qualquer servidor" não define escopo.
- d. Incorreta: as técnicas de evasão são definidas antes, nas regras de engajamento, e combinadas com o White Team, que controla o exercício.
- e. Correta: a cláusula define técnica, servidores, duração, janela, religamento e a condição de encaminhamento antes da limpeza, como na carta da Rede Tatame.
