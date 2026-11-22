# Questionário — Unidade 3

Disciplina: Red Team & Blue Team Strategies  
Professor-conteudista: Afonso Cesar Lelis Brandão  
Template de origem: `documentos/Unidade 3/40 Questões - UNI3_nomedadisciplina.docx`

Quantidade obrigatória: 40 questões padrão ENADE — 20 de asserção-razão (1 a 20) e 20 de interpretação (21 a 40).
Cinco alternativas por questão (a–e); a correta é marcada com `*` imediatamente antes da letra.
Distribuição da letra correta: 8 questões para cada uma das letras a, b, c, d, e, no total das 40 questões.
Feedback para **cada alternativa** (por que está correta ou qual o equívoco), todos ao final do documento.
Questões alinhadas à ementa oficial: Aula 9 (1–5 e 21–25), Aula 10 (6–10 e 26–30), Aula 11 (11–15 e 31–35) e Aula 12 (16–20 e 36–40).

## Questões

### Asserção-razão

**1.** I. No Windows, o evento 4688 (criação de processo) pode registrar a linha de comando executada, desde que a política específica para isso esteja habilitada.

PORQUE

II. O registro nativo de segurança do Windows já inclui, por padrão, o *hash* do executável e a linha de comando do processo pai em todos os eventos de criação de processo, o que torna o Sysmon redundante.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**2.** I. Em uma arquitetura com Wazuh, um evento 4625 gerado em um servidor Windows só aparece no *dashboard* do analista depois de passar pelo agente, pelo Wazuh server e pelo Wazuh indexer.

PORQUE

II. No Wazuh, o agente coleta e envia os eventos ao *server*, que aplica *decoders* e regras e gera alertas; o *indexer* guarda e indexa esses alertas; e o *dashboard* é a interface em que o analista os pesquisa.

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**3.** I. Manter os registros no SIEM por apenas sete dias é suficiente para investigar qualquer intrusão, desde que as regras de correlação sejam de boa qualidade.

PORQUE

II. A retenção de registros deve atender a requisitos legais e contratuais e ao tempo real das investigações; o PCI DSS, por exemplo, exige 12 meses de histórico de auditoria, com os 3 mais recentes disponíveis para análise imediata.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**4.** I. Um sensor de rede do Security Onion, ligado a uma porta espelhada (SPAN) do *switch*, consegue registrar conexões de máquinas que não têm agente instalado.

PORQUE

II. O Zeek, executado no sensor, resume cada conexão em metadados como origem, destino, porta, duração e protocolo, gravados em arquivos como o `conn.log`.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**5.** I. Quando uma sessão de área de trabalho remota é protegida por TLS, o Wireshark deixa de mostrar os endereços IP, as portas e os horários das conexões, o que torna inútil a captura de pacotes nesse caso.

PORQUE

II. No Wireshark, o filtro de exibição, como `tcp.port == 3389`, define quais pacotes serão gravados pela placa de rede durante a captura.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

**6.** I. Uma regra YARA que combina trechos de texto e uma expressão regular pode reconhecer variantes de uma mesma família de arquivos que uma lista de *hashes* SHA-256 não reconhece.

PORQUE

II. O *hash* criptográfico muda por inteiro quando um único *byte* do arquivo é alterado, enquanto a regra YARA descreve trechos e uma condição que continuam presentes nas variantes.

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**7.** I. Segundo a Pirâmide da Dor, bloquear os endereços IP e os *hashes* usados por um grupo é a forma de detecção que impõe o maior custo ao adversário.

PORQUE

II. Endereços IP e *hashes* estão ligados ao modo de operar do grupo, isto é, às suas táticas, técnicas e procedimentos, e por isso são os indicadores mais difíceis de trocar.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

**8.** I. No Wazuh, uma regra-filha com nível 0, encadeada à regra-mãe por `if_sid`, pode funcionar como exceção para uma rotina legítima conhecida.

PORQUE

II. O Sigma é um formato aberto, escrito em YAML, que permite descrever a lógica de detecção uma única vez e convertê-la para a linguagem de diferentes SIEMs.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**9.** I. Uma detecção comportamental voltada à exclusão de cópias de sombra (T1490) tende a resistir melhor à troca de ferramenta pelo adversário do que uma lista de *hashes* de arquivos conhecidos.

PORQUE

II. Detecções comportamentais dispensam o conhecimento do ambiente e, por isso, não geram falsos positivos com rotinas legítimas de administração, como *backups*.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**10.** I. Para eliminar os falsos positivos de uma regra, a melhor prática é criar uma exceção que ignore todos os eventos do servidor que mais gera alertas.

PORQUE

II. A sensibilidade (*recall*) de uma regra mede, dos ataques que realmente aconteceram, quantos geraram alerta, e pode cair quando uma exceção suprime eventos maliciosos junto com os legítimos.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**11.** I. Na caça a ameaças, o analista aguarda que uma regra do SIEM dispare para só então iniciar a busca por evidências do adversário.

PORQUE

II. A caça a ameaças parte do comprometimento presumido (*assume breach*): o caçador supõe que o adversário já está no ambiente e procura evidências antes de qualquer alerta.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**12.** I. O empilhamento (*stacking*) ajuda a encontrar programas raros, ao contar em quantas máquinas cada valor aparece e ordenar do menos frequente para o mais frequente.

PORQUE

II. O pivô transforma um achado no filtro da próxima consulta, como passar de um programa raro para o endereço IP que ele contata.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**13.** I. Muitas conexões de um servidor para o mesmo destino externo, com coeficiente de variação dos intervalos próximo de zero, são um indício de batimento (*beaconing*) de uma ferramenta automatizada.

PORQUE

II. Programas que mantêm contato periódico com um servidor remoto tendem a se conectar em intervalos quase constantes, enquanto o uso humano produz intervalos irregulares.

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**14.** I. Um *z-score* acima do limiar 3 no volume de saída de uma máquina comprova que ela foi comprometida, o que dispensa a análise de contexto.

PORQUE

II. A média e o desvio-padrão são medidas robustas, que não se alteram de forma relevante quando um dia atípico, como um *backup*, entra no período de referência.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

**15.** I. Uma hipótese de caça bem formulada indica onde procurar e o que contaria como evidência, de modo que possa ser confirmada ou descartada com os dados disponíveis.

PORQUE

II. Uma caça que termina sem encontrar nenhum adversário não produz nenhum resultado útil para a equipe de defesa.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**16.** I. Os CIS Benchmarks agrupam suas recomendações de configuração em perfis, como o Nível 1, com medidas essenciais e de pouco impacto no uso do sistema, e o Nível 2, com medidas adicionais para ambientes mais sensíveis.

PORQUE

II. Os CIS Controls v8 organizam suas salvaguardas em três grupos de implementação, IG1, IG2 e IG3, sendo o IG1 o conjunto de higiene cibernética essencial.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**17.** I. Desabilitar o SMBv1 em um servidor de arquivos Windows reduz a superfície de ataque sem impedir que os compartilhamentos continuem atendendo pelo SMB 3.

PORQUE

II. *Hardening* consiste, essencialmente, em instalar novas ferramentas de detecção nos servidores, como agentes de EDR e sensores de rede, sem alterar a configuração existente.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**18.** I. Na Rede Tatame, como a regra R11 detecta *login* sem MFA em conta privilegiada ou na VPN, exigir MFA na VPN tornou-se uma medida desnecessária.

PORQUE

II. Detectar um passo do adversário equivale a impedi-lo, já que todo alerta gerado pelo SIEM encerra automaticamente a sessão que o originou.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

**19.** I. Manter, para o administrador de TI, uma conta de uso diário (*e-mail* e navegação) separada da conta usada para administrar servidores reduz o impacto de um *phishing* bem-sucedido contra esse administrador.

PORQUE

II. Pelo princípio do menor privilégio, a conta de uso diário não tem privilégios administrativos, de modo que a senha capturada por uma página falsa não dá controle sobre os servidores.

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**20.** I. Um servidor de homologação que ficou fora do inventário estará protegido, desde que o *baseline* de configuração seja aplicado a todos os servidores inventariados.

PORQUE

II. Não é possível endurecer o que não se sabe que existe; por isso, o inventário de ativos é o primeiro dos CIS Controls e, no NIST CSF 2.0, faz parte da função Identificar.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Interpretação

**21.** O painel do SIEM da Rede Tatame exibiu, para a mesma conta, os seguintes eventos do canal Security do servidor SRV-ERP-01:

```
02:14:03  4625  conta=carla.dias  tipo=10  origem=10.10.4.31
02:14:21  4625  conta=carla.dias  tipo=10  origem=10.10.4.31
   ... (mais 8 eventos 4625 idênticos até 02:16:40)
02:17:12  4624  conta=carla.dias  tipo=10  origem=10.10.4.31
```

Com base nos conceitos da Aula 9, qual é a interpretação mais adequada desse trecho?

a. Trata-se de erros de digitação da própria usuária, pois o *logon* final foi bem-sucedido, e não há motivo para análise adicional.
*b. A sequência de falhas seguida de sucesso, da mesma origem, por área de trabalho remota e em pouco mais de três minutos, sugere senha descoberta e justifica investigar a conta.
c. O evento 4624 indica que o registro de auditoria do servidor foi apagado logo após as tentativas de acesso, o que caracteriza tentativa de apagar rastros.
d. O tipo de *logon* 10 indica acesso pelo teclado do próprio servidor, o que descarta um acesso a partir de outra máquina.
e. Como cada evento 4625 é inofensivo quando observado isoladamente, a sequência inteira pode ser descartada pela triagem sem prejuízo.

**22.** O SOC de uma rede de clínicas recebe, em média, 1.200 alertas por dia. A triagem de cada alerta leva 12 minutos. A equipe N1 tem quatro analistas, cada um com cerca de 6 horas efetivas de triagem por dia. Qual é a capacidade diária de triagem da equipe e que fração do volume ela representa?

a. 240 alertas por dia, o que corresponde a 20% do volume.
b. 480 alertas por dia, o que corresponde a 40% do volume.
c. 24 alertas por dia, o que corresponde a 2% do volume.
*d. 120 alertas por dia, o que corresponde a 10% do volume.
e. 1.200 alertas por dia, o que corresponde a 100% do volume.

**23.** Ao revisar o agente Wazuh de um servidor Windows da Rede Tatame, o analista encontrou, no arquivo `ossec.conf`, apenas os canais de eventos Application, Security e System. O Sysmon está instalado e gravando eventos normalmente no próprio servidor. Qual é a conclusão correta?

*a. Os eventos do Sysmon não chegam ao Wazuh, porque o canal Microsoft-Windows-Sysmon/Operational precisa ser incluído na configuração do agente.
b. Os eventos do Sysmon chegam ao Wazuh normalmente, porque o canal Security já contém todos os eventos gerados pelo Sysmon.
c. O Sysmon precisa ser desinstalado, porque ele impede o agente Wazuh de ler o canal Security.
d. O problema está no Wazuh indexer, que descarta por padrão qualquer evento vindo de servidores Windows.
e. Basta habilitar a política de linha de comando do evento 4688 para que os eventos do Sysmon passem a ser enviados.

**24.** Em um arquivo de captura aberto no Wireshark, o analista aplicou o filtro `tcp.flags.syn == 1 && tcp.flags.ack == 0` e viu 11 pacotes de 10.10.4.31 para 10.10.1.30, porta 3389, em pouco mais de três minutos, e um pacote de 10.10.4.31 para 10.10.1.20, porta 445, respondido por um pacote com a flag RST. Qual é a interpretação mais adequada?

a. O filtro mostra apenas pacotes de dados cifrados, e por isso não permite contar conexões.
b. As 11 linhas indicam uma única conexão RDP longa, e o pacote RST confirma que ela foi encerrada normalmente.
c. A porta 445 corresponde ao RDP, e a porta 3389 ao compartilhamento de arquivos do Windows.
d. O RST indica que o servidor 10.10.1.20 aceitou a conexão e transferiu arquivos para a origem.
*e. Houve 11 inícios de conexão RDP com o servidor 10.10.1.30 e uma tentativa de conexão na porta 445 do servidor 10.10.1.20, que foi recusada.

**25.** Na Rede Tatame, os índices do SIEM guardam os alertas do Wazuh por 365 dias, os *logs* do Zeek por 90 dias e a captura completa de pacotes (PCAP) por 7 dias. Uma investigação conclui que o invasor entrou há 30 dias. O que o SOC ainda consegue analisar sobre o primeiro dia da invasão?

a. Apenas os pacotes completos, porque o PCAP é sempre guardado por mais tempo do que os alertas.
b. Nada, porque nenhuma das três fontes alcança 30 dias.
*c. Os alertas do Wazuh e os metadados de conexão do Zeek, mas não os pacotes completos, que já foram descartados.
d. Somente os alertas do Wazuh, porque os *logs* do Zeek guardam apenas o dia corrente.
e. Todos os dados, porque a retenção de 365 dias dos alertas se aplica automaticamente às demais fontes.

**26.** O engenheiro de detecção da Rede Tatame aplicou duas versões de uma regra YARA a quatro arquivos e obteve o resultado abaixo.

```
arquivo                   hash IOC  YARA v1                      YARA v2
briefing_cti.txt          não       Cobalto_Nota_Resgate_v1      -
leia-me_v1.txt            sim       Cobalto_Nota_Resgate_v1      Cobalto_Nota_Resgate_v2
leia-me_v2.txt            não       Cobalto_Nota_Resgate_v1      Cobalto_Nota_Resgate_v2
relatorio_financeiro.txt  não       -                            -
```

Sabendo que as duas notas de resgate são maliciosas e que o *briefing* é um resumo de inteligência escrito pelo próprio SOC, qual é a interpretação correta?

a. A lista de *hashes* é suficiente, porque reconheceu todas as notas de resgate maliciosas presentes na pasta.
b. A regra v1 é a melhor das três abordagens, porque é a única que não deixa passar nenhum arquivo malicioso e não gera falso positivo.
c. A regra v2 gerou um falso negativo no *briefing*, que deveria ter sido marcado por citar o nome do grupo.
d. O resultado mostra que regras YARA não servem para variantes, pois a leia-me_v2 só foi reconhecida por coincidência.
*e. A lista de *hashes* perdeu a variante leia-me_v2, a regra v1 gerou um falso positivo no *briefing* e a regra v2 reconheceu as duas notas sem o falso positivo.

**27.** Em 30 dias, uma regra de detecção gerou 252 alertas, dos quais 10 correspondiam a ataques emulados pelo Red Team. Todos os 10 ataques emulados no período geraram alerta. Quais são, respectivamente, a precisão e a sensibilidade (*recall*) aproximadas dessa regra?

a. 100% e 4,0%.
b. 96,0% e 100%.
*c. 4,0% e 100%.
d. 4,0% e 96,0%.
e. 10% e 25,2%.

**28.** Ao testar uma regra no `wazuh-logtest`, um analista colou três eventos de criação de processo e obteve:

```
Evento 1: vssadmin.exe delete shadows /all       -> regra 100210, nível 12, Alert to be generated
Evento 2: vssadmin.exe ... /oldest (svc-backup)  -> regra 100211, nível 0
Evento 3: atualiza.exe delete shadows /all
          (originalFileName: VSSADMIN.EXE)        -> regra 61603, nível 0
```

Qual é a interpretação correta do teste?

a. Os três eventos geraram alerta, porque todos foram processados por alguma regra do Wazuh.
b. O evento 2 é um falso negativo, pois a exclusão de cópias de sombra é sempre maliciosa.
c. O evento 3 foi detectado corretamente, já que a regra 61603 trata da criação de processos.
*d. O evento 1 gerou o alerta esperado, o evento 2 caiu na exceção, como planejado, e o evento 3 revelou um falso negativo, corrigível ao comparar o nome original do arquivo.
e. O teste não tem valor, porque o `wazuh-logtest` só verifica a sintaxe do XML e não aplica as regras aos eventos.

**29.** Um fornecedor oferece à Rede Tatame uma lista com milhares de *hashes* de arquivos de um grupo de *ransomware*. A CISO pergunta se a lista resolve a detecção desse grupo. Com base na comparação entre assinatura, comportamento e correlação, qual resposta é a mais adequada?

*a. A lista é útil para reconhecer cópias conhecidas com baixo custo, mas deve ser combinada com regras de comportamento e de correlação, porque o grupo pode trocar os arquivos e escapar das assinaturas exatas.
b. A lista resolve a detecção, porque *hashes* são o indicador mais difícil de o adversário alterar.
c. A lista deve ser descartada, porque assinaturas não têm nenhuma utilidade diante de grupos organizados.
d. A lista substitui a necessidade de testar regras, já que cada *hash* foi confirmado pelo fornecedor.
e. A lista só funciona se for convertida em regra Sigma, porque o Wazuh não aceita indicadores de *hash*.

**30.** Considere a regra do Suricata abaixo, usada em um sensor de rede de laboratório.

```
alert http any any -> $HOME_NET any (msg:"TATAME LAB varredura com Nmap NSE";
  flow:established,to_server; http.user_agent; content:"Nmap Scripting Engine";
  classtype:attempted-recon; sid:1000101; rev:1;)
```

Qual é a interpretação correta dessa regra?

a. Ela bloqueia automaticamente qualquer tráfego HTTP que saia da rede interna para a internet.
*b. Ela gera um alerta quando uma requisição HTTP destinada à rede protegida traz, no cabeçalho User-Agent, o texto típico do mecanismo de *scripts* do Nmap.
c. Ela detecta comportamento anômalo, comparando o volume de requisições com a linha de base do servidor.
d. Ela é uma regra de correlação que junta falhas de *login* e sucesso da mesma origem em 60 segundos.
e. Ela identifica arquivos maliciosos pelo *hash* SHA-256 registrado no campo `sid`.

**31.** Ao testar a hipótese de que há ferramentas de acesso remoto instaladas fora do processo oficial de TI, uma caçadora empilhou 30 dias de processos das 149 máquinas da sede da Rede Tatame e obteve:

```
process.name      máquinas   aprovada?
conectaja.exe            1   não
remotodesk.exe           3   não
suporte_ti.exe         145   sim
```

Qual é a interpretação mais adequada desse resultado?

*a. As duas ferramentas da cauda longa merecem investigação, mas a raridade sozinha não prova ataque: é preciso verificar contexto, como processo pai, conta, destino das conexões e existência de mudança aprovada.
b. Como o suporte_ti.exe aparece em quase todas as máquinas, ele é o programa mais suspeito, pois um adversário procuraria o maior alcance possível.
c. O conectaja.exe e o remotodesk.exe devem ser tratados imediatamente como incidentes confirmados, sem necessidade de outras consultas.
d. O resultado não tem valor para a caça, porque o empilhamento só funciona com endereços IP e não com nomes de processos.
e. O remotodesk.exe é certamente legítimo e o conectaja.exe é certamente malicioso, porque a quantidade de máquinas define a natureza do programa.

**32.** Uma caçadora calculou o *baseline* de 14 dias do volume diário de saída para a internet de um servidor: média de 500 MB e desvio-padrão amostral de 40 MB. No dia analisado, o servidor enviou 640 MB. A equipe usa limiar de 3 desvios-padrão. Qual é a leitura correta?

a. O *z-score* é 1,4, abaixo do limiar, e o dia pode ser considerado normal.
b. O *z-score* é 14, o que comprova a exfiltração de dados e dispensa qualquer outra análise.
c. O *z-score* é 3,5, abaixo do limiar, porque o limiar só é ultrapassado quando o valor dobra em relação à média.
d. O *z-score* não pode ser calculado, porque é preciso conhecer a mediana e o MAD do período.
*e. O *z-score* é (640 − 500) ÷ 40 = 3,5, acima do limiar; o servidor merece investigação, embora o número sozinho não prove um ataque.

**33.** Um *script* de caça considera batimento (*beaconing*) o par máquina-destino com pelo menos 10 conexões e coeficiente de variação (cv) dos intervalos de no máximo 0,10. O resultado foi:

```
par                                  conexões   intervalo médio   cv
SRV-ERP-01 -> 198.51.100.77                14           300,3 s   0,008
NB-ATD-012 -> www.tatame.com.br             6           737,8 s   0,931
SRV-ARQ-01 -> www.tatame.com.br             6           600,0 s   0,050
NB-TI-003 -> relay.remotodesk.example.com  20           689,6 s   0,761
```

Qual interpretação está de acordo com o critério do *script*?

a. Os quatro pares são batimento, pois todos se conectaram a destinos externos mais de uma vez.
*b. Apenas o par do SRV-ERP-01 atende aos dois critérios; o par do SRV-ARQ-01 tem intervalos regulares, mas poucas conexões para formar padrão.
c. Apenas o par do NB-TI-003 é batimento, porque tem o maior número de conexões.
d. Os pares do SRV-ERP-01 e do SRV-ARQ-01 são batimento, porque o número de conexões não faz parte do critério.
e. Nenhum par é batimento, porque o cv precisaria ser maior que 0,10 para indicar regularidade.

**34.** Um servidor enviou 180, 200, 220, 190, 210, 200 e 200 MB em sete dias (média de 200 MB e desvio de cerca de 12,91 MB). Hoje enviou 260 MB, com *z-score* de cerca de 4,65. Um analista incluiu no *baseline* um dia de *backup* de 600 MB; a média subiu para 250 MB, o desvio para cerca de 141,9 MB e o *z-score* de hoje caiu para 0,07. Com mediana 200 e MAD 10, o *z* robusto é de cerca de 4,05. Qual é a interpretação mais adequada?

a. O *backup* comprova que o volume de hoje é normal, e a primeira análise estava errada.
b. O *z* robusto está errado, porque deveria variar tanto quanto o *z-score* clássico.
*c. O dia atípico inflou a média e o desvio e escondeu a anomalia; um *baseline* limpo ou uma medida robusta, como mediana e MAD, preserva a sinalização.
d. O limiar de 3 deve ser elevado para 5, porque assim nenhum dia de *backup* afeta o resultado.
e. A mediana e o MAD só podem ser usados quando não há nenhum dia atípico no período.

**35.** No simulador da Rede Tatame, o cenário "Acesso remoto não aprovado e saída de dados" foi executado com as regras R8 (ferramenta de acesso remoto não aprovada) e R9 (saída volumosa) desligadas e sem a fonte de saída de rede. A linha do tempo mostrou: instalação da ferramenta no SRV-ERP-01, "visto nos logs, sem alerta"; conexões periódicas para 198.51.100.77, "visto nos logs, sem alerta"; envio de 2,8 GB, "não detectado". Qual interpretação é a mais adequada?

a. Os três passos foram ignorados porque o SOC não estava monitorando, e nenhuma mudança de configuração alteraria o resultado.
b. O envio de 2,8 GB não foi detectado porque a regra R8 estava desligada; ligá-la resolveria os três passos.
c. Os dois primeiros passos não ficaram registrados em lugar nenhum, por isso a caça não teria como encontrá-los.
*d. Os dois primeiros passos foram registrados, mas nenhuma regra olhava para eles; o envio não foi visto porque a fonte estava desligada. Ligar a fonte, a R8 e a R9 cobre o primeiro e o terceiro passos, e o batimento ainda pede uma regra nova.
e. O resultado mostra que a caça é desnecessária, porque bastaria aumentar a velocidade do simulador para que os alertas aparecessem.

**36.** Um *script* de auditoria comparou a configuração de um servidor-membro com um *baseline* de 10 itens inspirado no CIS Benchmark e produziu a saída abaixo.

```
SRV-ARQ-02: 7/10 conformes (70%)
  [EXCEÇÃO] H02 Spooler de impressão desligado: aprovado pela CISO (MUD-0520) até 30/06/2027
  [FALHA]   H07 No máximo 2 administradores locais (CIS 5.4): encontrado 5
  [FALHA]   H10 Último patch há até 30 dias (CIS 7.3): encontrado 52
```

Qual é a interpretação mais adequada desse resultado?

a. O servidor está em conformidade total, pois a exceção aprovada compensa as duas falhas encontradas.
b. A exceção do H02 deve ser tratada como falha grave e corrigida imediatamente, porque exceções não são admitidas em um *baseline*.
c. O resultado indica que o *baseline* está errado, já que nenhum servidor real consegue cumprir os itens H07 e H10.
*d. O servidor cumpre 7 dos 10 itens; a exceção documentada, com aprovador e prazo, não conta como conformidade nem como falha, e os itens H07 e H10 precisam ser corrigidos ou virar exceção formal.
e. Como a conformidade passou de 50%, o servidor pode ser considerado endurecido e as falhas podem ficar para a próxima auditoria anual.

**37.** Uma equipe de TI recebe, em média, 18 falhas críticas novas por mês em seus servidores e hoje leva 30 dias para corrigir cada uma. A gestão propõe um prazo de correção de 10 dias. Considerando que o número médio de falhas abertas ao mesmo tempo é igual às falhas novas por dia multiplicadas pelos dias até a correção, assinale a alternativa correta.

*a. Hoje ficam, em média, 18 falhas abertas; com o novo prazo, 6, uma redução de cerca de 67% na exposição.
b. Hoje ficam, em média, 540 falhas abertas; com o novo prazo, 180, uma redução de cerca de 67%.
c. Hoje ficam, em média, 18 falhas abertas; com o novo prazo, 12, uma redução de cerca de 33%.
d. O prazo não altera a quantidade de falhas abertas, que depende apenas do número de falhas novas por mês.
e. Hoje ficam, em média, 0,6 falha aberta; com o novo prazo, 0,2, o que torna a mudança irrelevante.

**38.** Um levantamento da superfície externa de uma empresa encontrou dois ativos com falhas pendentes:

| Ativo | Exposição | Inventário | CVSS | EPSS | No catálogo KEV |
|---|---|---|---|---|---|
| A — servidor de relatórios | rede interna | sim | 9,8 | 2% | não |
| B — painel de homologação | internet, sem WAF | não | 7,5 | 94% | sim |

Com base nos critérios de priorização de *patching* estudados, qual deve ser a decisão?

a. Corrigir primeiro o ativo A, porque o CVSS é o único critério relevante para priorizar correções.
b. Ignorar o ativo B, porque ele não está no inventário e, portanto, não pertence ao escopo de proteção.
*c. Tratar primeiro o ativo B, porque está exposto à internet, tem falha já explorada (KEV) e alta probabilidade de exploração (EPSS), e incluí-lo no inventário ou tirá-lo do ar.
d. Corrigir os dois ao mesmo tempo, já que CVSS acima de 7 coloca ambos na mesma prioridade.
e. Aguardar a próxima janela anual de manutenção, porque nenhum dos dois ativos tem CVSS igual a 10.

**39.** Em um servidor de arquivos, o administrador executou um comando do PowerShell e obteve a lista de membros do grupo de administradores locais:

```
Name                        ObjectClass
----                        -----------
SRV-ARQ-01\Administrador    Usuário
CORP\TI-Admins-Servidores   Grupo
CORP\joao.pessoal           Usuário
CORP\svc-backup             Usuário
CORP\Usuários do domínio    Grupo
```

Considerando o princípio do menor privilégio e as salvaguardas do CIS Controls estudadas, qual é a ação mais adequada?

a. Manter todos os membros, porque o servidor já está protegido pelo *firewall* da rede.
b. Remover apenas o administrador local, pois é a única conta que existe em todos os servidores.
c. Adicionar também o grupo de administradores do domínio, para que qualquer administrador possa agir em caso de incidente.
d. Desabilitar o grupo TI-Admins-Servidores e deixar a administração com a conta de serviço svc-backup.
*e. Remover o grupo Usuários do domínio, a conta pessoal e a conta de serviço, mantendo o administrador local com senha única gerida pelo LAPS e o grupo de administração de servidores, com contas administrativas separadas.

**40.** Uma organização usa o NIST CSF 2.0 para classificar suas ações de segurança. No último trimestre, ela exigiu MFA para o acesso remoto e administrativo, aplicou um *baseline* do CIS Benchmark aos servidores e desligou serviços desnecessários, como o FTP e o *spooler* de impressão. Em qual função do CSF 2.0 essas ações se enquadram principalmente?

a. Detectar, porque reduzem o número de alertas gerados pelo SIEM.
*b. Proteger, nas categorias de identidade, autenticação e controle de acesso e de segurança das plataformas, apoiada pelo inventário da função Identificar.
c. Responder, porque são executadas depois de um incidente confirmado.
d. Recuperar, porque restauram os servidores a um estado anterior ao ataque.
e. Governar, porque toda configuração técnica é uma decisão estratégica da diretoria.

## Gabarito e feedbacks

**Questão 1** (correta: c)
- a. Incorreta: a asserção II é falsa; o registro nativo não traz por padrão o *hash* do executável nem a linha de comando do processo pai, e é justamente esse contexto que o Sysmon acrescenta.
- b. Incorreta: a asserção II não é verdadeira; reveja a comparação entre o evento 4688 e o Sysmon na Aula 9.
- c. Correta: o evento 4688 só registra a linha de comando se a política específica estiver habilitada ("ter a fonte não basta; é preciso configurá-la"), e o Sysmon não é redundante, pois enriquece a telemetria com o *hash* do executável e os detalhes do processo pai.
- d. Incorreta: a asserção I é verdadeira; o registro da linha de comando no 4688 depende de uma política específica.
- e. Incorreta: apenas a II é falsa; a I descreve corretamente a configuração do evento 4688.

**Questão 2** (correta: a)
- a. Correta: a I é verdadeira e a II explica por quê; o evento percorre agente, *server* (*decoders* e regras), *indexer* (armazenamento e indexação) e só então é pesquisado no *dashboard*.
- b. Incorreta: a II descreve exatamente o caminho que torna a I verdadeira, portanto a justifica.
- c. Incorreta: a II é verdadeira; ela resume os quatro componentes do Wazuh apresentados na Aula 9.
- d. Incorreta: a I é verdadeira; o *dashboard* não lê o evento diretamente do servidor monitorado.
- e. Incorreta: as duas asserções são verdadeiras e descrevem a arquitetura de referência do Wazuh.

**Questão 3** (correta: d)
- a. Incorreta: a I é falsa; correlação de qualidade não recupera registros que já foram descartados.
- b. Incorreta: a I é falsa; além disso, a II contradiz a I, em vez de apenas não a justificar.
- c. Incorreta: a avaliação está invertida; a I é falsa e a II é verdadeira.
- d. Correta: sete dias não contam a história do início de uma intrusão que durou semanas (I falsa), e a retenção deve considerar lei, contratos e o tempo real das investigações, como no requisito de 12 meses do PCI DSS (II verdadeira).
- e. Incorreta: a II é verdadeira; reveja o tópico de retenção do SIEM, com o exemplo do PCI DSS.

**Questão 4** (correta: b)
- a. Incorreta: o que permite ver máquinas sem agente é o sensor receber uma cópia do tráfego pela porta espelhada; o formato dos metadados do Zeek não explica essa capacidade.
- b. Correta: ambas são verdadeiras; o sensor enxerga o tráfego de máquinas sem agente porque recebe uma cópia dele (SPAN ou TAP), e o Zeek de fato gera metadados como o `conn.log`, mas a II descreve o formato do registro, e não a razão da I.
- c. Incorreta: a II é verdadeira; o `conn.log` do Zeek registra origem, destino, porta, duração e protocolo de cada conexão.
- d. Incorreta: a I é verdadeira; a visibilidade de rede independe de agente instalado nas máquinas.
- e. Incorreta: as duas asserções são verdadeiras; reveja o tópico de telemetria de rede na Aula 9.

**Questão 5** (correta: e)
- a. Incorreta: as duas asserções são falsas; com TLS, endereços, portas e horários continuam visíveis, e o filtro de exibição não define o que é gravado.
- b. Incorreta: nenhuma das duas asserções é verdadeira.
- c. Incorreta: a I é falsa; o TLS cifra o conteúdo, mas não esconde os cabeçalhos IP e TCP.
- d. Incorreta: a II é falsa; quem decide o que gravar é o filtro de captura, em sintaxe BPF, como `port 3389`.
- e. Correta: a I é falsa, pois a captura continua mostrando quem falou com quem, quando e quanto, mesmo com TLS; a II é falsa, pois o filtro de exibição apenas escolhe o que mostrar de pacotes já capturados.

**Questão 6** (correta: a)
- a. Correta: a I é verdadeira e a II explica por quê: um *byte* alterado muda todo o *hash*, mas os trechos e a condição da regra YARA continuam presentes na variante.
- b. Incorreta: a II é justamente o mecanismo que explica a vantagem da YARA sobre o *hash*, portanto justifica a I.
- c. Incorreta: a II é verdadeira; o *hash* criptográfico é exato e muda por inteiro com qualquer alteração.
- d. Incorreta: a I é verdadeira; no laboratório da Aula 10, a regra YARA reconheceu a variante leia-me_v2, que a lista de *hashes* perdeu.
- e. Incorreta: as duas asserções são verdadeiras; reveja o tópico "Assinaturas: *hash*, YARA e Suricata".

**Questão 7** (correta: e)
- a. Incorreta: as duas asserções são falsas; IP e *hash* ficam na base da Pirâmide da Dor.
- b. Incorreta: nenhuma das asserções é verdadeira; o maior custo vem da detecção de TTPs, no topo da pirâmide.
- c. Incorreta: a I é falsa; bloquear IP e *hash* custa pouco ao adversário, que os troca com facilidade.
- d. Incorreta: a II é falsa; IP e *hash* são artefatos fáceis de trocar e não se confundem com as TTPs.
- e. Correta: segundo Bianco (2013), *hashes* e endereços IP estão na base da pirâmide (I falsa) e são justamente os indicadores mais fáceis de trocar, distintos das TTPs (II falsa).

**Questão 8** (correta: b)
- a. Incorreta: as duas são verdadeiras, mas a II fala da portabilidade do Sigma e não explica o funcionamento da exceção de nível 0 no Wazuh.
- b. Correta: a regra-filha de nível 0 não gera alerta e funciona como exceção (I verdadeira), e o Sigma é um formato portátil em YAML (II verdadeira), mas são fatos independentes.
- c. Incorreta: a II é verdadeira; o Sigma é convertido para a linguagem de vários SIEMs.
- d. Incorreta: a I é verdadeira; no Wazuh, nível 0 não gera alerta, e a regra 100211 da aula funciona exatamente assim.
- e. Incorreta: ambas as asserções são verdadeiras; reveja o tópico "Regras e correlação: Wazuh e Sigma".

**Questão 9** (correta: c)
- a. Incorreta: a II é falsa, portanto não pode justificar a I.
- b. Incorreta: a II não é verdadeira; detecções comportamentais exigem conhecer o ambiente justamente para separar o legítimo do malicioso.
- c. Correta: a regra que vigia a técnica independe do nome da ferramenta (I verdadeira), mas o comportamento gera falsos positivos com rotinas legítimas, como o *backup* do exemplo, e exige ajuste (II falsa).
- d. Incorreta: a I é verdadeira; detectar a técnica, e não a ferramenta, é o que dá resistência à troca de artefatos.
- e. Incorreta: a I é verdadeira; apenas a II é falsa.

**Questão 10** (correta: d)
- a. Incorreta: a I é falsa; uma exceção por servidor inteiro suprime também os ataques que acontecem nele.
- b. Incorreta: a I é falsa; a boa prática é a exceção específica, por conta, processo e parâmetro.
- c. Incorreta: a avaliação está invertida; a I é falsa e a II é verdadeira.
- d. Correta: a exceção ampla é má prática (I falsa), e a sensibilidade mede os ataques que viraram alerta, caindo de 100% para 60% no exemplo da aula quando o servidor inteiro foi ignorado (II verdadeira).
- e. Incorreta: a II é verdadeira; reveja o exemplo numérico com as três versões da regra.

**Questão 11** (correta: d)
- a. Incorreta: a I é falsa; a caça é proativa e não espera o alerta para começar.
- b. Incorreta: a I é falsa, pois descreve o oposto da caça a ameaças.
- c. Incorreta: a avaliação está invertida; a I é falsa e a II é verdadeira.
- d. Correta: a caça não aguarda o disparo de regras (I falsa); ela parte do comprometimento presumido e busca evidências antes de qualquer alerta (II verdadeira).
- e. Incorreta: a II é verdadeira; o comprometimento presumido é a premissa da caça vista na Aula 11.

**Questão 12** (correta: b)
- a. Incorreta: o pivô não explica por que o empilhamento encontra o raro; são técnicas distintas, ainda que usadas juntas.
- b. Correta: as duas são verdadeiras. O empilhamento conta e ordena valores para revelar a cauda longa, e o pivô encadeia consultas, mas a II não justifica a I.
- c. Incorreta: a II é verdadeira; o pivô transforma um achado no filtro da próxima consulta.
- d. Incorreta: a I é verdadeira; o empilhamento é a técnica usada para achar o raro.
- e. Incorreta: ambas as asserções descrevem corretamente técnicas de consulta da caça.

**Questão 13** (correta: a)
- a. Correta: o cv próximo de zero indica intervalos quase constantes (I), e é justamente porque programas automáticos conectam em intervalos regulares, ao contrário de pessoas, que esse indicador funciona (II justifica I).
- b. Incorreta: a II é a razão pela qual o cv baixo indica batimento, portanto justifica a I.
- c. Incorreta: a II é verdadeira; o uso humano gera intervalos irregulares, com cv próximo de um.
- d. Incorreta: a I é verdadeira; reveja o laboratório em que o SRV-ERP-01 teve cv de 0,008.
- e. Incorreta: ambas são verdadeiras e descrevem o conceito de batimento.

**Questão 14** (correta: e)
- a. Incorreta: as duas asserções são falsas.
- b. Incorreta: nenhuma das duas é verdadeira; anomalia não é prova, e média e desvio não são robustos.
- c. Incorreta: a I é falsa; o *z-score* alto indica onde olhar, mas o contexto decide se há ataque.
- d. Incorreta: a II é falsa; um dia atípico infla a média e o desvio e pode esconder a anomalia.
- e. Correta: a anomalia não comprova comprometimento, como mostrou o NB-TI-003, explicado por uma mudança aprovada (I falsa), e média e desvio são sensíveis a dias atípicos; robustas são a mediana e o MAD (II falsa).

**Questão 15** (correta: c)
- a. Incorreta: a II é falsa e, portanto, não pode justificar a I.
- b. Incorreta: a II é falsa; uma caça sem achados também gera entregas.
- c. Correta: a hipótese precisa ser específica e testável (I verdadeira), e uma caça sem achados ainda entrega *baseline*, lacunas de coleta, consulta documentada e, muitas vezes, uma regra nova (II falsa).
- d. Incorreta: a I é verdadeira; reveja o cartão da hipótese H-11.
- e. Incorreta: a I é verdadeira; apenas a II é falsa.

**Questão 16** (correta: b)
- a. Incorreta: as duas asserções são verdadeiras, mas tratam de documentos diferentes; os grupos de implementação dos CIS Controls não explicam os perfis dos CIS Benchmarks.
- b. Correta: os CIS Benchmarks têm perfis Nível 1 e Nível 2, e os CIS Controls v8 têm os grupos IG1, IG2 e IG3; são afirmações verdadeiras sobre referências distintas, sem relação de causa.
- c. Incorreta: a II é verdadeira; o IG1, com 56 salvaguardas, é a higiene cibernética essencial dos CIS Controls v8.
- d. Incorreta: a I é verdadeira; reveja os perfis Nível 1 e Nível 2 dos CIS Benchmarks na Aula 12.
- e. Incorreta: ambas as asserções descrevem corretamente as duas referências do CIS.

**Questão 17** (correta: c)
- a. Incorreta: a II é falsa; *hardening* é configurar com segurança e remover o desnecessário, e não instalar ferramentas de detecção.
- b. Incorreta: a II não é verdadeira; reveja a definição de *hardening* na Aula 12.
- c. Correta: desligar o SMBv1, protocolo antigo explorado pelo WannaCry, reduz a superfície sem afetar o SMB 3 (I verdadeira); a II confunde *hardening* com detecção, que são complementares, mas diferentes.
- d. Incorreta: a I é verdadeira; o laboratório do SRV-ARQ-01 desliga o SMBv1 mantendo os compartilhamentos.
- e. Incorreta: apenas a II é falsa.

**Questão 18** (correta: e)
- a. Incorreta: as duas asserções são falsas; detecção e prevenção são complementares.
- b. Incorreta: nenhuma das asserções é verdadeira.
- c. Incorreta: a I é falsa; no cenário do Cobalto Austral, a R11 detectou o *login* sem MFA, mas o acesso aconteceu, e só o MFA o teria impedido.
- d. Incorreta: a II é falsa; um alerta não encerra a sessão automaticamente, ele depende de análise e de resposta.
- e. Correta: a detecção avisa que o passo aconteceu, mas não o impede (I falsa), e o alerta não interrompe a sessão por si só (II falsa); por isso o MFA na VPN continua necessário.

**Questão 19** (correta: a)
- a. Correta: a separação de contas reduz o impacto do *phishing* (I verdadeira) justamente porque a conta de uso diário, pelo menor privilégio, não tem acesso administrativo (II verdadeira e justificativa da I), como pede a salvaguarda 5.4 do CIS Controls.
- b. Incorreta: a II explica diretamente por que a separação reduz o impacto, portanto justifica a I.
- c. Incorreta: a II é verdadeira; é a aplicação do princípio do menor privilégio.
- d. Incorreta: a I é verdadeira; reveja o exemplo das contas caio.mendes e caio.mendes.adm.
- e. Incorreta: ambas as asserções são verdadeiras.

**Questão 20** (correta: d)
- a. Incorreta: a I é falsa; o ativo fora do inventário não recebe o *baseline*.
- b. Incorreta: a I é falsa; além disso, a II contradiz a I, em vez de apenas não a justificar.
- c. Incorreta: a avaliação está invertida; a I é falsa e a II é verdadeira.
- d. Correta: o *baseline* só alcança o que está inventariado, então o servidor esquecido continua exposto, como o `hml-gestao` (I falsa); o inventário vem primeiro nos CIS Controls e fica em Identificar no CSF 2.0 (II verdadeira).
- e. Incorreta: a II é verdadeira; reveja a relação entre inventário e *hardening* na Aula 12.

**Questão 21** (correta: b)
- a. Incorreta: o sucesso final, após dez falhas seguidas da mesma origem, é exatamente o que torna o padrão suspeito; ignorá-lo seria um erro de triagem.
- b. Correta: dez falhas (4625) seguidas de um sucesso (4624), da mesma origem e em poucos minutos, é o padrão clássico de correlação que sugere senha descoberta; o tipo 10 indica acesso remoto, e a hora incomum reforça a necessidade de investigar.
- c. Incorreta: o 4624 registra um *logon* bem-sucedido; o evento que indica registro de auditoria apagado é o 1102.
- d. Incorreta: o tipo 10 indica *logon* interativo remoto (área de trabalho remota); o *logon* pelo teclado local é o tipo 2.
- e. Incorreta: a correlação existe justamente porque eventos inofensivos isoladamente revelam um ataque quando combinados em sequência.

**Questão 22** (correta: d)
- a. Incorreta: 240 alertas exigiriam 2.880 minutos de triagem, mais do que as 24 horas (1.440 minutos) disponíveis; reveja o cálculo da capacidade.
- b. Incorreta: o valor dobra a capacidade real; com 12 minutos por alerta, cada hora permite triar 5 alertas, e não 20.
- c. Incorreta: o cálculo esqueceu de converter horas em minutos antes de dividir pelo tempo de triagem.
- d. Correta: 4 analistas × 6 horas = 24 horas = 1.440 minutos; 1.440 ÷ 12 = 120 alertas por dia, ou seja, 120 ÷ 1.200 = 10% do volume, situação típica de fadiga de alertas.
- e. Incorreta: a demanda é de 1.200 × 12 = 14.400 minutos (240 horas), muito acima das 24 horas disponíveis.

**Questão 23** (correta: a)
- a. Correta: o agente Wazuh só lê os canais listados no `ossec.conf`; sem um bloco `localfile` com o canal Microsoft-Windows-Sysmon/Operational, o Sysmon grava localmente, mas nada chega ao SIEM.
- b. Incorreta: o Sysmon grava em um canal próprio (Microsoft-Windows-Sysmon/Operational), e não no canal Security.
- c. Incorreta: o Sysmon e o agente convivem normalmente; o problema é apenas a ausência do canal na configuração.
- d. Incorreta: o *indexer* guarda o que o *server* envia; os eventos nem chegaram a ser coletados pelo agente.
- e. Incorreta: a política do 4688 afeta a linha de comando no canal Security, e não a coleta do canal do Sysmon.

**Questão 24** (correta: e)
- a. Incorreta: o filtro seleciona pacotes SYN sem ACK, isto é, inícios de conexão TCP, e não dados cifrados.
- b. Incorreta: cada SYN sem ACK marca o início de uma nova conexão; 11 pacotes indicam 11 conexões, e o RST se refere à porta 445, não ao RDP.
- c. Incorreta: as portas estão invertidas; 3389 é o RDP e 445 é o SMB, o compartilhamento de arquivos do Windows.
- d. Incorreta: um RST em resposta a um SYN indica conexão recusada, e não transferência de dados.
- e. Correta: os 11 SYN mostram tentativas sucessivas de conexão RDP, compatíveis com várias tentativas de senha, e o RST mostra que o servidor de arquivos recusou a conexão na porta 445, um passo seguinte que o *log* do ERP não registraria.

**Questão 25** (correta: c)
- a. Incorreta: o PCAP ocupa muito espaço e, neste cenário, é guardado por apenas 7 dias, o menor prazo das três fontes.
- b. Incorreta: os alertas (365 dias) e os *logs* do Zeek (90 dias) alcançam os 30 dias da invasão.
- c. Correta: 30 dias estão dentro da retenção dos alertas do Wazuh e dos *logs* do Zeek, mas fora dos 7 dias do PCAP; o SOC sabe quem se conectou com quem, mas não tem mais os pacotes daquele dia.
- d. Incorreta: os *logs* do Zeek ficam disponíveis por 90 dias, e não apenas no dia corrente.
- e. Incorreta: cada conjunto de dados tem sua própria política de retenção; o prazo dos alertas não se estende às outras fontes.

**Questão 26** (correta: e)
- a. Incorreta: a lista de *hashes* reconheceu só a leia-me_v1; a variante leia-me_v2 passou sem ser reconhecida.
- b. Incorreta: a regra v1 marcou o *briefing* do SOC, que não é malicioso, gerando um falso positivo.
- c. Incorreta: o *briefing* não é malicioso; não marcá-lo é o comportamento correto, e não um falso negativo.
- d. Incorreta: a leia-me_v2 foi reconhecida porque contém os trechos e o identificador descritos na regra, e não por coincidência.
- e. Correta: o *hash* exato perdeu a variante, a condição "qualquer trecho" da v1 gerou o falso positivo e a v2, que exige o identificador da vítima, reconheceu só as duas notas.

**Questão 27** (correta: c)
- a. Incorreta: os valores estão invertidos; a precisão é baixa e a sensibilidade é total.
- b. Incorreta: 96% é a proporção de falsos positivos entre os alertas (242 ÷ 252), e não a precisão.
- c. Correta: precisão = 10 ÷ 252 ≈ 4,0%, pois só 10 dos alertas eram ataque; sensibilidade = 10 ÷ 10 = 100%, pois nenhum ataque deixou de gerar alerta.
- d. Incorreta: a sensibilidade é 100%, já que todos os 10 ataques geraram alerta.
- e. Incorreta: 10% e 25,2% não correspondem a nenhuma das razões; precisão divide verdadeiros por alertas e sensibilidade divide verdadeiros por ataques.

**Questão 28** (correta: d)
- a. Incorreta: só o evento 1 gerou alerta; regras de nível 0 não geram alerta.
- b. Incorreta: o evento 2 é a rotina de *backup* coberta pela exceção 100211; trata-se de comportamento legítimo, e não de falso negativo.
- c. Incorreta: a regra 61603 é a regra-base de criação de processo, de nível 0; ela não alerta, e a técnica passou sem detecção.
- d. Correta: o teste confirmou o alerta no ataque, a exceção no *backup* e revelou que o executável renomeado escapa da regra que olha o caminho da imagem, o que se corrige comparando o originalFileName.
- e. Incorreta: o `wazuh-logtest` passa o evento pelos decodificadores e pelas regras e mostra qual regra é acionada.

**Questão 29** (correta: a)
- a. Correta: assinaturas exatas são baratas e precisas para o conhecido, mas o adversário troca o artefato; por isso a lista se combina com comportamento e correlação.
- b. Incorreta: *hashes* ficam na base da Pirâmide da Dor e são os indicadores mais fáceis de trocar.
- c. Incorreta: assinaturas continuam úteis para reconhecer cópias conhecidas com baixo custo e poucos falsos positivos.
- d. Incorreta: nenhuma detecção dispensa testes; o fornecedor não conhece o ambiente nem as variantes futuras.
- e. Incorreta: a conversão para Sigma não é requisito; a lista de *hashes* pode ser usada diretamente por diferentes ferramentas.

**Questão 30** (correta: b)
- a. Incorreta: a ação é `alert`, que gera alerta e não bloqueia; além disso, o destino é a rede protegida (`$HOME_NET`).
- b. Correta: a regra olha o tráfego HTTP com destino à rede protegida e procura, no User-Agent, o texto "Nmap Scripting Engine"; o `sid` identifica a regra e o `rev`, a versão.
- c. Incorreta: a regra é uma assinatura de conteúdo, e não uma comparação com linha de base.
- d. Incorreta: a regra analisa uma única requisição; não há correlação de falhas e sucessos de *login*.
- e. Incorreta: o `sid` é o identificador da regra, e não um *hash* de arquivo.

**Questão 31** (correta: a)
- a. Correta: o empilhamento mostra onde olhar (a cauda longa), mas a decisão depende do contexto; na Aula 11, o remotodesk.exe tinha mudança aprovada, e o conectaja.exe não.
- b. Incorreta: o valor comum, presente em 145 máquinas, é o programa oficial da TI; o empilhamento destaca justamente o raro.
- c. Incorreta: raridade é indício, não confirmação; sem verificar contexto, a equipe trataria uma mudança aprovada como incidente.
- d. Incorreta: o empilhamento funciona com qualquer campo, como nome de processo, destino ou conta.
- e. Incorreta: a quantidade de máquinas não define a natureza do programa; é preciso investigar o contexto de cada um.

**Questão 32** (correta: e)
- a. Incorreta: 1,4 não corresponde à conta; o *z-score* é (640 − 500) ÷ 40 = 3,5.
- b. Incorreta: 14 seria o resultado de dividir por 10, e nenhum *z-score* comprova ataque sozinho.
- c. Incorreta: 3,5 está acima do limiar 3; o limiar é medido em desvios-padrão, não em múltiplos da média.
- d. Incorreta: o *z-score* clássico usa média e desvio-padrão; mediana e MAD são uma alternativa robusta, não um requisito.
- e. Correta: z = 140 ÷ 40 = 3,5, acima do limiar; a anomalia indica onde olhar, e o contexto decidirá se há ataque.

**Questão 33** (correta: b)
- a. Incorreta: conectar mais de uma vez não basta; o critério exige pelo menos 10 conexões e cv de no máximo 0,10.
- b. Correta: só o SRV-ERP-01 tem 14 conexões e cv de 0,008; o SRV-ARQ-01 tem cv baixo, mas só 6 conexões, e o NB-TI-003 tem muitas conexões, mas intervalos irregulares.
- c. Incorreta: o NB-TI-003 tem cv de 0,761, típico de uso humano; muitas conexões não bastam.
- d. Incorreta: o número mínimo de conexões faz parte do critério e exclui o SRV-ARQ-01.
- e. Incorreta: o critério é o inverso; cv pequeno indica intervalos regulares.

**Questão 34** (correta: c)
- a. Incorreta: o *backup* não diz nada sobre o volume de hoje; ele apenas distorceu o período de referência.
- b. Incorreta: a mediana e o MAD foram escolhidos justamente por não variarem com um único dia atípico.
- c. Correta: o dia de 600 MB elevou a média e, principalmente, o desvio, fazendo o *z-score* cair para 0,07; limpar o *baseline* ou usar mediana e MAD mantém o *z* em cerca de 4,05.
- d. Incorreta: elevar o limiar reduz a sensibilidade para todos os casos e não corrige a contaminação do *baseline*.
- e. Incorreta: a mediana e o MAD são úteis exatamente quando há valores atípicos no período.

**Questão 35** (correta: d)
- a. Incorreta: o resultado depende das fontes e regras; ao ligá-las e repetir o cenário, dois passos passam a ser detectados.
- b. Incorreta: o envio depende da fonte de saída de rede e da R9, não da R8.
- c. Incorreta: "visto nos logs, sem alerta" significa que o dado foi registrado; é por isso que a caça consegue encontrá-lo.
- d. Correta: os passos amarelos estavam nos registros sem regra, e o vermelho ficou invisível sem a fonte; a caça cobre esse ponto cego e indica as regras que faltam, inclusive a de batimento.
- e. Incorreta: a velocidade do simulador só muda o ritmo da simulação, não a cobertura de fontes e regras.

**Questão 36** (correta: d)
- a. Incorreta: 7 de 10 itens não é conformidade total, e uma exceção não compensa falhas.
- b. Incorreta: exceções são admitidas quando documentadas, com justificativa, aprovador e prazo, como a do H02.
- c. Incorreta: falhas na auditoria indicam desvio do servidor, não erro do *baseline*; limite de administradores e prazo de *patch* são itens comuns de *hardening*.
- d. Correta: a conformidade é 7 de 10 (70%); a exceção formal não conta como conforme nem como falha, e os itens H07 e H10 precisam ser corrigidos ou virar exceção aprovada, com dono e prazo.
- e. Incorreta: não existe limite de 50% para considerar um servidor endurecido; desvios devem ser tratados, e a conformidade é acompanhada continuamente.

**Questão 37** (correta: a)
- a. Correta: 18 por mês são 0,6 falha por dia; 0,6 × 30 = 18 abertas hoje e 0,6 × 10 = 6 com o novo prazo, redução de 1 − 10/30 ≈ 67%.
- b. Incorreta: 540 e 180 resultam de multiplicar as falhas por mês pelos dias, sem converter para falhas por dia.
- c. Incorreta: com prazo de 10 dias ficam 6 falhas abertas em média, não 12.
- d. Incorreta: a quantidade média de falhas abertas depende do volume e do prazo de correção; reduzir o prazo reduz a exposição na mesma proporção.
- e. Incorreta: 0,6 é a taxa de falhas novas por dia, e não a quantidade média de falhas abertas.

**Questão 38** (correta: c)
- a. Incorreta: o CVSS mede a gravidade técnica, mas a priorização também considera exploração conhecida (KEV), probabilidade de exploração (EPSS), exposição e criticidade.
- b. Incorreta: ativo fora do inventário continua exposto; o correto é trazê-lo para o inventário ou desativá-lo, como no caso do `hml-gestao`.
- c. Correta: o ativo B está exposto à internet sem WAF, tem falha no KEV e EPSS de 94%; deve ser tratado primeiro, além de ser incluído no inventário ou retirado do ar.
- d. Incorreta: CVSS acima de 7 não iguala prioridades; KEV, EPSS e exposição diferenciam os dois ativos.
- e. Incorreta: falhas já exploradas em ativos expostos não podem esperar uma janela anual; o *patching* é um processo contínuo.

**Questão 39** (correta: e)
- a. Incorreta: o *firewall* não substitui o menor privilégio; qualquer membro do grupo tem controle total do servidor.
- b. Incorreta: o administrador local deve continuar, com senha única e aleatória gerida pelo LAPS; o problema está nos membros não aprovados.
- c. Incorreta: ampliar o grupo aumenta a superfície e contraria o menor privilégio.
- d. Incorreta: contas de serviço não devem administrar servidores nem ter *logon* interativo.
- e. Correta: remover o grupo Usuários do domínio, a conta pessoal e a conta de serviço aplica o menor privilégio (CIS 5.4); ficam o administrador local com LAPS (CIS 5.2) e o grupo de administração, usado com contas administrativas separadas.

**Questão 40** (correta: b)
- a. Incorreta: Detectar trata de encontrar e analisar possíveis ataques; MFA, *baseline* e desligamento de serviços são medidas preventivas.
- b. Correta: as ações estão em Proteger, nas categorias PR.AA (identidade, autenticação e controle de acesso) e PR.PS (segurança das plataformas), e dependem do inventário de Identificar.
- c. Incorreta: Responder trata das ações sobre um incidente detectado; as medidas descritas são preventivas.
- d. Incorreta: Recuperar trata da restauração de ativos e operações após um incidente.
- e. Incorreta: Governar trata de estratégia, papéis e supervisão de riscos; as configurações técnicas descritas pertencem a Proteger.
