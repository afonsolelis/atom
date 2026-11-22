# Unidade 2 — Técnicas Ofensivas em Ambiente Controlado

Disciplina: Red Team & Blue Team Strategies  
Professor-conteudista: Afonso Cesar Lelis Brandão  
Prazo de entrega: 02/12/2026  
Template de origem: `documentos/Unidade 2/TEMPLATE - Unidade 2_nome da disciplina.docx`

> Versão alinhada à **ementa oficial** enviada pela coordenação em 18/11/2026 (`EMENTA.md`).
> Recursos visuais indicados entre colchetes, como pede o template; a equipe de produção substitui pelas imagens finais.
> Todos os laboratórios acontecem contra a plataforma fictícia Rede Tatame, dentro do escopo da carta de autorização do exercício. Nenhum trecho traz código de exploração, *payload* ou comando real de evasão.

## Aula 5 — Reconhecimento e enumeração de serviços e usuários

### O que você verá nesta unidade

Nesta unidade, você acompanha por dentro um exercício autorizado de Red Team contra a Rede Tatame, a plataforma fictícia da disciplina, sempre em laboratório e dentro do escopo assinado. Vamos percorrer as técnicas ofensivas na ordem em que um adversário as usaria: o reconhecimento e a enumeração de serviços e usuários; a exploração de vulnerabilidades e a obtenção de acesso inicial, com a priorização por CVSS, EPSS e KEV, a verificação controlada no Metasploit e o *phishing* como vetor; a escalada de privilégios, a movimentação lateral e a persistência; e, por fim, a evasão básica de defesas e a limpeza de rastros, estudadas pelo rastro que deixam para o defensor, junto com o relatório da operação. O objetivo é que você saiba planejar e executar cada etapa em ambiente controlado e, principalmente, reconhecer que evidência cada passo produz para o Blue Team. A justificativa é direta: só detecta bem quem entende como o adversário avança, e é o exercício ofensivo autorizado que transforma uma ameaça abstrata em evidência concreta para a defesa.

### Texto base

Antes de enviar um único pacote para a rede de uma empresa, um adversário competente já sabe muito sobre ela: quais domínios possui, quais tecnologias usa, quem trabalha na TI, qual é o formato dos endereços de *e-mail* e quais serviços estão expostos na internet. Essa fase é o **reconhecimento**, a tática TA0043 (*Reconnaissance*) da matriz MITRE ATT&CK estudada na Unidade 1. Na Rede Tatame, ela abre o exercício autorizado de novembro de 2026, conduzido pelo Red Team de Bruno Sato com carta assinada pela CISO, Marina Prado.

#### Reconhecimento passivo e ativo

No reconhecimento **passivo**, a equipe consulta apenas fontes de terceiros, sem interagir com os sistemas do alvo. É o território da OSINT (*Open Source Intelligence*), a inteligência de fontes abertas:

| Fonte | O que revela | Técnica ATT&CK |
|---|---|---|
| Transparência de certificados, DNS público, WHOIS | Subdomínios, servidores de *e-mail*, provedores | T1596 — *Search Open Technical Databases* |
| *Sites*, vagas e redes sociais | Organograma, cargos, tecnologias usadas | T1593 — *Search Open Websites/Domains*; T1591 — *Gather Victim Org Information* |
| Endereços de *e-mail* e nomes | Padrão de *e-mail*, pessoas-alvo | T1589 — *Gather Victim Identity Information* |

No reconhecimento **ativo**, há interação: consultas ao DNS da empresa, visitas ao *site* e varreduras de portas (T1595 — *Active Scanning*). A diferença pesa duas vezes. Juridicamente, o ativo toca ativos que precisam constar da autorização. Para a defesa, o passivo praticamente não deixa rastro no ambiente do alvo, enquanto o ativo pode ser registrado.

[Imagem 1 — Ilustração de uma lupa sobre um mapa de rede com ícones de domínios, pessoas e servidores. Texto alternativo: "Lupa sobre um mapa com domínios, pessoas e servidores de uma empresa, representando o reconhecimento". Sugestão de busca no Envato: "magnifying glass network map cyber".]

#### Kali Linux: a bancada do laboratório

O **Kali Linux**, mantido pela OffSec, é uma distribuição baseada no Debian que reúne centenas de ferramentas de teste de segurança. Em um exercício, ele roda em uma máquina dedicada da equipe, cujo endereço de origem consta da autorização; na Tatame, a máquina virtual `lab-tatame`. A ferramenta não legitima nada: o que torna a ação legítima é o documento que define redes, janela de horário e origem.

#### Varredura e descoberta de serviços

O **Nmap** é a ferramenta clássica de varredura. A opção `-sn` apenas descobre quais *hosts* estão ativos. A varredura **SYN** (`-sS`, padrão quando o Nmap roda com privilégio de administrador) envia um pacote SYN a cada porta e não completa o *handshake* TCP: se volta SYN/ACK, a porta está **aberta** (*open*); se volta RST, está **fechada** (*closed*); se nada volta, um *firewall* descartou o pacote e a porta aparece como **filtrada** (*filtered*). A varredura *connect* (`-sT`) completa a conexão e, por isso, aparece mais nos registros das aplicações. A opção `-sV` conversa com cada serviço aberto para identificar o programa e a versão.

Feita de fora, a varredura é T1595. Feita de dentro da rede, pertence à tática Descoberta (TA0007), como T1046 — *Network Service Discovery*.

[Imagem 2 — Diagrama comparando o *handshake* TCP completo (SYN, SYN/ACK, ACK) com a varredura de meia abertura (SYN, SYN/ACK, RST) e com a porta fechada (SYN, RST/ACK). Texto alternativo: "Três sequências de pacotes TCP mostrando porta aberta, porta fechada e a varredura SYN". Pode ser recriado pela equipe de produção.]

#### Enumeração de serviços e de usuários

A **enumeração** aprofunda a varredura e extrai dos serviços informações como versões, nomes de domínio, compartilhamentos e contas. Um servidor LDAP, por exemplo, informa a qualquer cliente o nome do domínio do Active Directory e seu nível funcional.

A enumeração de **usuários** costuma começar na OSINT: *e-mails* públicos revelam o formato dos logins, como nome.sobrenome (T1589.002 e T1589.003). Depois, ela pode explorar falhas de projeto. Se a página de login responde "senha incorreta" para contas que existem e "usuário não encontrado" para as que não existem, ou se o tempo de resposta muda, a página confirma quais contas são válidas. O guia de testes da OWASP (WSTG) trata o caso no teste WSTG-IDNT-04. Já dentro da rede, listar contas e grupos do diretório corresponde a T1087.002 (*Account Discovery: Domain Account*), tema da Aula 7. Nas regras de engajamento da Tatame, a enumeração no login fica limitada a uma tentativa por conta, sempre com senha sabidamente errada e sem nenhum teste de senha.

#### Que rastro isso deixa para o Blue Team?

Uma captura de pacotes no **Wireshark** torna a varredura evidente: centenas de SYN da mesma origem e da mesma porta de origem para portas diferentes, em fração de segundo, seguidos de RST. *Firewall*, WAF e sensores de rede (como o Zeek) registram o padrão. A enumeração de usuários aparece como falhas de login para muitas contas diferentes, várias inexistentes; a enumeração interna, como consultas volumosas ao diretório. A condição é coletar a fonte certa: um servidor fora do WAF e do inventário, como a homologação esquecida da Tatame, recebe a varredura sem que o SOC veja nada.

[Imagem 3 — Captura de tela do Wireshark com uma sequência de pacotes SYN destacados e respostas RST em vermelho. Texto alternativo: "Lista de pacotes no Wireshark mostrando uma varredura de portas". Sugestão: captura de tela do Wireshark disponível no Wikimedia Commons ("Wireshark screenshot"), licença GPL.]

#### Limites éticos, legais e de escopo

Informação pública também está sujeita a regras. Nomes, cargos e *e-mails* são dados pessoais sujeitos à LGPD, e as regras de engajamento devem dizer o que pode ser coletado, como será protegido e quando será descartado. Varreduras só alcançam redes e horários da carta; um subdomínio com o nome da empresa hospedado por uma agência de *marketing* entra no relatório, mas não é tocado, e acessar sistema de terceiro pode configurar o crime do art. 154-A do Código Penal. Se a equipe encontrar fichas de alunos menores em um servidor exposto, registra a evidência mínima e avisa a CISO, sem copiar os dados.

#### Exemplo numérico: quanto a empresa expõe sem saber

O Red Team identifica 180 subdomínios da Tatame na transparência de certificados. Destes, 120 respondem na internet e 15 não constam do inventário da TI: 15 ÷ 120 = **12,5%** da superfície ativa é desconhecida. A Tatame tem 400 pessoas com *e-mail* corporativo, e 260 endereços aparecem em fontes públicas: 260 ÷ 400 = **65%** do quadro exposto. Dos 260, 243 seguem o formato nome.sobrenome, ou 243 ÷ 260 ≈ **93,5%**, o que basta para prever o login da maioria. Na varredura das 100 portas mais comuns da homologação, a captura registrou 203 pacotes: 100 SYN, 3 SYN/ACK das portas abertas, 97 RST/ACK das fechadas e 3 RST enviados pelo próprio Kali.

#### Pontos-chave

- O reconhecimento (TA0043) pode ser passivo, quase sem rastro, ou ativo, que exige escopo e aparece nos registros.
- O Nmap descobre *hosts*, portas e versões: T1595 quando feito de fora, T1046 quando feito de dentro.
- A enumeração de usuários explora o padrão de *e-mail* e respostas de login diferentes para contas existentes e inexistentes.
- Cada passo ativo deixa rastro, mas o Blue Team só o vê se coletar a fonte daquele ativo.

### Referências da aula

LYON, Gordon Fyodor. *Nmap network scanning*: the official Nmap project guide to network discovery and security scanning. Sunnyvale: Insecure.Com, 2009.

MITRE. *Reconnaissance (TA0043)*. In: MITRE ATT&CK. Disponível em: <https://attack.mitre.org/tactics/TA0043/>. Acesso em: 22 nov. 2026.

NATIONAL INSTITUTE OF STANDARDS AND TECHNOLOGY. *SP 800-115*: technical guide to information security testing and assessment. Gaithersburg: NIST, 2008.

OWASP FOUNDATION. *OWASP web security testing guide*. Versão 4.2. 2020. Disponível em: <https://owasp.org/www-project-web-security-testing-guide/>. Acesso em: 22 nov. 2026.

WEIDMAN, Georgia. *Testes de invasão*: uma introdução prática ao hacking. São Paulo: Novatec, 2014.

### Roteiro da Videoaula 5 — "Antes de entrar: o que a Rede Tatame entrega a quem procura?"

Duração-alvo: 15 a 20 minutos. Deck: unidade_2/slides/aula5.html (22 slides).

**Slides 1 e 2 — Capa e sumário (0:00–0:25)**
Fala: "Olá! Esta é a Aula 5, a primeira da Unidade 2, em que acompanhamos por dentro o exercício autorizado do Red Team contra a Rede Tatame. Hoje o tema é reconhecimento e enumeração de serviços e usuários: tudo o que um adversário descobre antes de entrar."
[Câmera: professor em plano médio.]

**Slide 3 — O problema de hoje na Rede Tatame (0:25–1:35)**
Fala: "Começa o exercício de novembro. De 16 a 27, o Red Team de Bruno Sato emula o Grupo Cobalto Austral, com a carta assinada por Marina Prado no chamado APR-2291. O inventário da TI lista 105 endereços na internet, mas ninguém sabe se há outros, que serviços respondem neles nem que contas um atacante conseguiria adivinhar. Repare no mapa à direita: a borda vista da internet e, em vermelho, a homologação `hml-gestao`, fora do inventário e do WAF, com uma cópia do banco de alunos. A pergunta da aula está no quadro amarelo: o que a Tatame expõe e quais serviços e usuários um adversário consegue enumerar antes de entrar?"
[Take de apoio: pessoa digitando em notebook com mapa de rede ao fundo — Envato, "network map laptop".]

**Slide 4 — O que você verá nesta unidade (1:35–2:15)**
Fala: "Esta tabela é o mapa da unidade, na ordem em que um adversário agiria. Hoje, reconhecimento e enumeração. Na Aula 6, a falha ou a pessoa que abre a porta, verificada sem causar dano. Na 7, até onde o adversário chega depois de entrar. Na 8, como o defensor percebe quem tenta se esconder e como o exercício termina. Em todas, a mesma pergunta: que rastro esse passo deixa para o Blue Team?"

**Slide 5 — Reconhecimento passivo e reconhecimento ativo (2:15–3:00)**
Fala: "Reconhecimento é a tática TA0043 do ATT&CK. No passivo, a equipe só consulta fontes de terceiros: certificados, buscadores, registro do domínio, vagas e perfis. As técnicas são T1596, T1593, T1591 e T1589. No ativo, ela interage com o alvo: consulta o DNS da empresa ou varre portas, a técnica T1595. Olhar da calçada é passivo; tocar a campainha é ativo. Por isso o ativo precisa estar na autorização e aparece nos registros."

**Slide 6 — Laboratório: o que a própria empresa publica (3:00–4:40)**
Objetivo: mostrar o que a própria Tatame publica, incluindo o formato de usuário, sem tocar a rede dela.
Na tela:
1. Na aba "Vaga de emprego", clicar em "migração da VPN NetGuard 9.1 para a versão 10", "Active Directory em Windows Server 2012 R2", "ERP financeiro em servidor próprio da sede", "ambiente de homologação do portal das academias, criado em 2024" e "caio.mendes@tatame.com.br".
2. Clicar na aba "Perfil profissional" e nos trechos "Administrador de TI na Rede Tatame", "troca dos 120 notebooks da sede", "vpn.tatame.com.br", "O segundo fator ainda não chegou às contas da TI" e "foto da recepção com a tela da catraca facial".
3. Clicar na aba "Buscador de dispositivos" e nos três resultados: VPN em 203.0.113.30, `hml-gestao` em 203.0.113.45 e `promo-hml` em 198.51.100.23.
4. Conferir o contador no canto superior direito: "13 de 13 pistas".
Fala: "Cada trecho amarelo, quando clicado, mostra na faixa escura de baixo o que revela. A vaga entrega o fabricante e a versão da VPN e o endereço de Caio Mendes, que mostra o padrão nome.sobrenome; esse padrão costuma ser também o formato do login. O perfil confirma o endereço da VPN e admite que as contas da TI entram sem segundo fator, a informação mais grave da página. O buscador confirma a versão da VPN e mostra a `hml-gestao` sem WAF. Nenhuma dessas consultas tocou a rede da Tatame."
Atenção: as páginas são fictícias e usam domínios example.com. O terceiro resultado do buscador pertence à agência de *marketing*: entra no relatório e não pode ser acessado.
Conclusão: "Sem enviar um pacote, o Red Team já tem alvo, versão e formato de usuário."
[Tela: gravação do laboratório do slide 6.]

**Slide 7 — Laboratório: da calçada à campainha (4:40–6:10)**
Objetivo: ver quais consultas deixam rastro e quais chegam ao SOC.
Na tela:
1. Ler o passo "Passivo · Transparência de certificados", que abre o laboratório.
2. Clicar em "▶ Avançar" até "Passivo · Buscadores, vagas e WHOIS" e "Passivo · O que o SIEM viu até aqui".
3. Avançar para "Ativo · Consultas ao DNS da empresa" e "Ativo · Varredura da borda".
4. Avançar para "Ativo · Varredura da hml-gestao" e "Escopo · O servidor da agência".
Fala: "À esquerda está o Kali da equipe, a `lab-tatame`, com o endereço 192.0.2.66. Nos passos passivos, as setas vermelhas vão para serviços de terceiros e o SIEM fica sozinho: não viu nada. Nos ativos, a seta chega ao DNS ou ao WAF da Tatame, e uma seta azul leva os registros ao SIEM. Agora observe o sexto passo: a mesma varredura contra a `hml-gestao` não passa pelo WAF, e o nó fica em âmbar. O rastro existe no servidor, mas não chega ao SOC. No último passo, o servidor da agência fica com contorno vermelho: tocar nele seria agir sobre um terceiro sem autorização."
Atenção: o botão "⏯ Auto" toca a sequência sozinho; para gravar, prefira "▶ Avançar" e espere cerca de dois segundos por passo.
Conclusão: "O passivo se combate publicando menos; o ativo deixa rastro, desde que alguém colete a fonte."
[Tela: gravação do laboratório do slide 7.]

**Slide 8 — Kali Linux e Nmap: quem responde e o quê (6:10–7:10)**
Fala: "As duas primeiras ferramentas da ementa entram aqui. O Kali Linux, mantido pela OffSec, é uma distribuição Debian com centenas de ferramentas de teste; no exercício, ele roda na máquina virtual `lab-tatame`. O Nmap descobre *hosts* com `-sn`, faz a varredura SYN com `-sS`, que não completa a conexão, a varredura *connect* com `-sT`, que completa, e identifica versões com `-sV`. Guarde os três estados de porta: *open* responde SYN/ACK, *closed* responde RST, *filtered* não responde. De fora, isso é T1595; de dentro, T1046, na tática Descoberta. E o quadro azul lembra: quem autoriza é a carta, com redes, horário e a origem 192.0.2.66."
[Take de apoio: tela de terminal com texto verde rolando — Envato, "terminal code green".]

**Slide 9 — Laboratório: do certificado ao serviço (7:10–9:40)**
Objetivo: descobrir que serviços e versões a Tatame expõe, dentro da carta.
Na tela:
1. Clicar em "▶ Próximo comando": consulta à base de certificados, que grava `ct.txt` e conta 180 linhas.
2. "▶ Próximo comando": `dig` de `hml-gestao` e `promo-hml`.
3. "▶ Próximo comando": `nmap -sn` na borda 203.0.113.0/24.
4. "▶ Próximo comando": `nmap -sS -sV --top-ports 100` na VPN e na `hml-gestao`.
5. "▶ Próximo comando": `nmap -sV` com o script `ldap-rootdse` no SRV-AD-01.
Fala: "O primeiro comando ainda é passivo: lê a base pública de certificados e devolve 180 nomes. O segundo já toca o DNS da Tatame, como a RoE permite: `hml-gestao` resolve para 203.0.113.45, um endereço da casa, e `promo-hml` aponta para a agência, e a linha vermelha diz fora do escopo. O terceiro só descobre quem está no ar: 18 *hosts*, 6 do inventário e 12 que a TI não lista. O quarto é a varredura de serviços. Leia a saída por *host*. Na VPN, 99 portas aparecem como *filtered*, porque há um *firewall* na frente, e só a 443 responde, com o NetGuard 9.1. Na homologação, 97 portas aparecem como *closed*, ou seja, o servidor responde RST a cada uma, e três estão abertas: SSH na 22 e Apache 2.4.49 na 80 e na 443. Essa versão vai ser importante na próxima aula. O último comando simula a fase de acesso presumido, com a VM no segmento do laboratório da sede: o LDAP do controlador de domínio informa o domínio `corp.tatame.local`, e o nível funcional 6 corresponde ao Windows Server 2012 R2, o mesmo da vaga."
Atenção: as linhas coloridas que começam com comentário são notas didáticas do laboratório, não saída real dos programas. O terminal é simulado; avise que ninguém deve repetir esses comandos contra domínios reais, porque `tatame.com.br` é usado apenas como exemplo didático. Use "▶ Próximo comando" um a um e leia a nota de rodapé de cada passo.
Conclusão: "Varredura e enumeração dizem onde procurar falhas: a `hml-gestao`, com Apache 2.4.49, sobe para o topo da lista."
[Tela: gravação do laboratório do slide 9.]

**Slide 10 — Laboratório: a varredura vista no fio (9:40–11:30)**
Objetivo: ver, pacote a pacote, o rastro da varredura SYN, como um analista veria.
Na tela:
1. Com "Sem filtro" ativo, mostrar a lista e a barra de baixo: "Pacotes: 203 · Exibidos: 203 (100,0%)".
2. Clicar em "SYN enviados": a caixa de filtro mostra `tcp.flags.syn == 1 && tcp.flags.ack == 0` e 100 pacotes.
3. Clicar em "SYN/ACK": 3 pacotes, das portas 80, 443 e 22.
4. Clicar em "RST": 100 pacotes.
5. Clicar em uma linha vermelha que sai de 192.0.2.66 e ler o painel de detalhes.
Fala: "Este é o Wireshark, a terceira ferramenta da ementa, com a captura da varredura na `hml-gestao`. Cada linha é um pacote: número, tempo em segundos, origem, destino, protocolo, tamanho e o resumo na coluna *Info*. Repare que todos os 203 pacotes acontecem em cerca de um décimo de segundo e que a porta de origem, 41322, nunca muda: assinatura de varredura. O filtro de SYN mostra 100 pedidos, um por porta, fora da ordem numérica. O de SYN/ACK mostra só três respostas: são as portas abertas que o Nmap listou. O de RST mostra 100 pacotes: 97 são a homologação dizendo porta fechada e 3 são o próprio Kali derrubando a conexão logo depois do SYN/ACK. No painel de detalhes, as *flags* aparecem em hexadecimal, 0x004 para RST. Como o *handshake* nunca termina, a aplicação quase não registra nada; quem vê é a rede."
Atenção: a captura é simulada e mostra só a fase de descoberta de portas. A faixa amarela abaixo dos detalhes explica cada filtro; leia-a ao gravar.
Conclusão: "Para quem captura o tráfego, a varredura é barulhenta. O problema da Tatame é que ninguém captura o tráfego da homologação."
[Tela: gravação do laboratório do slide 10.]

**Slide 11 — Enumerar serviços e usuários (11:30–12:10)**
Fala: "Enumerar é extrair dos serviços o que eles contam: versões, domínio, compartilhamentos, contas. Para usuários, o caminho começa na OSINT, com o formato nome.sobrenome. Depois, uma falha de projeto comum: o login responder de um jeito para quem existe e de outro para quem não existe. A OWASP descreve esse teste como WSTG-IDNT-04. Dentro da rede, listar contas do AD é T1087.002, que retomaremos na Aula 7. E o limite da RoE: uma tentativa por conta, com senha sabidamente errada."

**Slide 12 — Laboratório: um login que entrega quem existe (12:10–13:30)**
Objetivo: verificar se o portal confirma quais contas existem, e como a produção evita isso.
Na tela:
1. O laboratório abre na tentativa "1. hml-gestao · caio.mendes".
2. Clicar em "2. hml-gestao · joao.inexistente".
3. Clicar em "3. produção · caio.mendes".
4. Clicar em "4. produção · joao.inexistente" e ler a tabela.
Fala: "À esquerda está o formulário; à direita, as tentativas e a tabela que registra mensagem e tempo. Na homologação, a conta de Caio Mendes recebe 'Senha incorreta para caio.mendes.' em 212 milissegundos, e a conta que não existe recebe 'Usuário não encontrado.' em 31. A mensagem e o tempo entregam quem existe. No portal de produção, as duas tentativas recebem a mesma frase, 'Usuário ou senha inválidos.', em cerca de 200 milissegundos. Não dá para distinguir."
Atenção: o laboratório não testa senhas; cada conta recebe uma única tentativa com senha sabidamente errada, como manda a RoE.
Conclusão: "Resposta genérica e tempo constante impedem a enumeração. É a recomendação que vai para o relatório da `hml-gestao`."
[Tela: gravação do laboratório do slide 12.]

**Slide 13 — Laboratório: o reconhecimento na plataforma Rede Tatame (13:30–15:30)**
Objetivo: ver o que o SOC enxerga do reconhecimento e o que muda com o monitor de certificados.
Na tela:
1. Conferir que a plataforma abriu na aba "Cenários", com a velocidade "1 s = 15 s".
2. No cartão "Reconhecimento externo", clicar em "Iniciar cenário" e esperar os cinco passos terminarem (cerca de 30 segundos).
3. Abrir a aba "Telemetria" e ligar "Monitor de certificados (CT)".
4. Abrir "Regras do CEP" e ligar a "R12 · Certificado novo para subdomínio fora do inventário".
5. Voltar a "Cenários" e clicar em "Repetir com as fontes e regras atuais".
6. Abrir a aba "Superfície" e localizar a linha de `hml-gestao.tatame.com.br`.
Fala: "Na primeira rodada, os indicadores mostram 1 de 5 passos detectado: só a varredura da borda, pela R4, que conta excesso de respostas 403 e 404 por endereço. A consulta a certificados, a resolução de 180 nomes e a varredura da `hml-gestao` passam sem alerta. Depois de ligar a fonte CT e a R12, a segunda rodada mostra 2 detectados: o certificado da homologação vira alerta logo no início. A varredura na `hml-gestao` continua com o ícone de não detectado, porque ninguém coleta os registros dela. Na aba Superfície, a linha mostra a homologação fora do inventário e sem WAF, com o Apache vulnerável que estudaremos na próxima aula."
Atenção: use "Repetir com as fontes e regras atuais"; o botão "Reiniciar" do topo volta tudo ao padrão e apagaria os ajustes. Cada rodada leva cerca de 30 segundos na velocidade padrão; se quiser encurtar, troque para "1 s = 1 min".
Conclusão: "Monitorar certificados mostra ao SOC o mesmo nome que o Red Team achou, mas só a coleta da homologação revelaria a varredura."
[Tela: gravação do laboratório do slide 13.]

**Slide 14 — Informação pública e varredura também têm regras (15:30–16:10)**
Fala: "Nomes, cargos e *e-mails* são dados pessoais e estão sujeitos à LGPD. A varredura só alcança as redes e os horários da carta, a partir da origem registrada. O servidor da agência e a API da PagaFácil não são tocados, porque acessar sistema de terceiro pode configurar o crime do art. 154-A do Código Penal. E, se aparecerem fichas de alunos menores na `hml-gestao`, a equipe registra a evidência mínima e avisa a CISO, sem copiar nada."

**Slide 15 — Antes do código: onde achar e como instalar (16:10–16:35)**
Fala: "Para o próximo laboratório, você precisa do Visual Studio Code com a extensão Python da Microsoft, do Python 3.12, de python.org, e do módulo `venv`, que já vem com ele. No Kali, o Python já está instalado. Os quatro módulos que o script importa são da biblioteca padrão; confira em docs.python.org. Não há pacote de terceiros para baixar."

**Slide 16 — Laboratório: do achado solto ao relatório de exposição (16:35–18:45)**
Objetivo: transformar os achados em números para a diretoria, respeitando o escopo.
Na tela:
1. O VS Code ocupa o slide inteiro. O roteiro do laboratório abre com a tecla G ou com o botão "☰ Roteiro", na barra de status; deixar esse painel fechado durante a gravação.
2. Clicar em "⬇ Preparar o ambiente" e esperar o botão mudar para "✓ Ambiente pronto".
3. No explorador, abrir `escopo.json`.
4. Voltar a `consolidar_recon.py` e mostrar as três linhas destacadas.
5. Clicar em "Executar".
Fala: "O editor ocupa a tela inteira, como no meu computador. Na preparação, `python3 --version` confirma o Python 3.12; o segundo comando cria o ambiente virtual `.venv`, isolado do sistema; o terceiro o ativa, e o *prompt* passa a começar com `(.venv)`; o `pip list` mostra só o `pip`, porque o script usa apenas a biblioteca padrão. O `escopo.json` diz que a Tatame tem 400 pessoas com *e-mail* e lista três hospedagens fora do escopo: a agência, a página de status e a PagaFácil. No script, o primeiro bloco lê os quatro arquivos da pasta `dados`. A primeira linha destacada monta `desconhecidos`: *hosts* que respondem e não estão no inventário. A segunda decide a ação: se a hospedagem estiver na lista de terceiros, não acessar e avisar o cliente. A terceira conta o formato de *e-mail* mais comum. Na saída: 180 nomes, 120 respondem, 15 fora do inventário, 12,5%, e 260 de 400 *e-mails*, 65%. Na lista, três linhas vermelhas são de terceiros e a `hml-gestao` aparece em amarelo. Depois, o formato nome.sobrenome em 243 de 260, 93,5%. No fim, a exposição por área: academias com 132, atendimento com 46 e financeiro com 31."
Atenção: ao abrir o slide, o código de `consolidar_recon.py` é digitado sozinho no editor; o botão "Digitar ao vivo" repete a digitação, se quiser mostrar de novo. Os arquivos de dados mostram só as primeiras linhas, e a saída usa a base completa. Os *e-mails* estão pseudonimizados. A preparação do ambiente leva cerca de 10 segundos; espere "✓ Ambiente pronto" antes de executar.
Conclusão: "O relatório mostra o tamanho do problema e onde agir primeiro: inventário, terceiros e treinamento das academias."
[Tela: gravação do laboratório do slide 16.]

**Slide 17 — Que rastro o reconhecimento e a enumeração deixam (18:45–19:15)**
Fala: "Do lado da defesa: o passivo quase não deixa rastro, e a proteção é publicar menos e monitorar certificados. A varredura aparece no *firewall*, no WAF e na captura de pacotes, como vimos no Wireshark. A enumeração de usuários aparece como falhas de login para muitas contas, várias inexistentes. A enumeração interna, como consultas volumosas ao AD, que na plataforma é a regra R13, desligada no padrão. E a lição da `hml-gestao`: quem não coleta o tráfego de um ativo não vê a varredura contra ele."

**Slide 18 — Exemplo numérico: quanto a Tatame expõe sem saber (19:15–19:35)**
Fala: "Juntando: 15 dividido por 120 dá 12,5% da superfície ativa desconhecida. 260 dividido por 400 dá 65% das pessoas expostas. 243 dividido por 260 dá 93,5% dos *e-mails* no formato dominante. E a varredura da homologação: 203 pacotes, três portas abertas em cem."

**Slide 19 — De volta ao problema (19:35–19:55)**
Fala: "Voltemos à pergunta. A Tatame expõe 15 ativos fora do inventário, serviços com versões identificáveis e um portal de homologação que confirma contas. O Red Team descobriu isso dentro do escopo. A defesa fecha a lacuna com inventário atualizado, monitor de certificados, mensagem de login genérica e coleta do tráfego da homologação."

**Slides 20 a 22 — Pontos-chave, referências e encerramento (19:55–20:00)**
Fala: "Na próxima aula, os serviços que encontramos hoje viram candidatos a vulnerabilidade e porta de entrada. Até lá!"
[Slides: pontos-chave e referências ficam disponíveis no material. Envato: "digital footprint data".]

## Aula 6 — Exploração de vulnerabilidades e obtenção de acesso inicial

### Texto base

Concluídos o reconhecimento e a enumeração, o Red Team tem nas mãos uma lista de serviços, versões e, em geral, centenas de achados de um *scanner* de vulnerabilidades. A pergunta agora é outra: **quais desses achados dariam a um adversário real o primeiro ponto de apoio no ambiente, e como provar isso sem causar dano?** É a tática TA0001 (*Initial Access*) da matriz MITRE ATT&CK, estudada na Unidade 1.

#### Da vulnerabilidade à exploração controlada

**Vulnerabilidade** é uma fraqueza conhecida em um *software*, em uma configuração ou em um processo. **Exploração** é o uso dessa fraqueza para obter algo que não deveria ser possível, como ler arquivos protegidos ou executar comandos. Entre uma e outra há uma distância importante: o *scanner* deduz muitas falhas apenas pelo número de versão anunciado pelo serviço, gera falsos positivos e não comprova que a falha pode ser explorada naquele ambiente.

Em um exercício autorizado, a validação segue o princípio de **demonstrar, e não executar**: confirmar a falha com o teste menos invasivo disponível, registrar a evidência mínima (código de resposta, versão, horário) e parar. Ler dados pessoais, instalar programas no alvo ou derrubar um serviço ficam fora das regras de engajamento, salvo previsão expressa e justificada.

#### CVE e CVSS: nome e gravidade

Cada vulnerabilidade conhecida recebe um identificador **CVE** (*Common Vulnerabilities and Exposures*), no formato CVE-ano-número, coordenado pela MITRE; a NVD, mantida pelo NIST, acrescenta severidade e produtos afetados. Um exemplo é a CVE-2021-41773, falha de travessia de diretório (*path traversal*) no servidor Apache HTTP 2.4.49. O **CVSS** (*Common Vulnerability Scoring System*), mantido pelo FIRST, atribui a cada falha uma nota de 0 a 10 a partir do vetor de ataque, da complexidade, dos privilégios e da interação exigidos e do impacto. A versão 4.0 foi publicada em 2023, mas a 3.1 ainda é a mais usada. As faixas são: 0,1 a 3,9, baixa; 4,0 a 6,9, média; 7,0 a 8,9, alta; 9,0 a 10,0, crítica. A nota-base mede **severidade técnica**, e não **risco**.

#### EPSS e KEV: o que o adversário usaria primeiro

O **EPSS** (*Exploit Prediction Scoring System*), também do FIRST, estima a probabilidade de exploração de uma falha nos 30 dias seguintes. O catálogo **KEV** (*Known Exploited Vulnerabilities*), da agência norte-americana CISA, lista falhas com exploração confirmada. Para o Blue Team, essas referências ordenam a correção; para o Red Team, ordenam o teste, porque um adversário emulado tende a usar primeiro o que já funciona contra outras vítimas. Somadas à exposição e à criticidade do ativo, elas dizem por onde começar.

[Imagem 1 — Matriz de prioridade com o eixo horizontal "severidade (CVSS)" e o eixo vertical "probabilidade de exploração (EPSS)", destacando o quadrante superior direito como "testar e corrigir primeiro". Texto alternativo: "Gráfico de dispersão de vulnerabilidades com CVSS no eixo x e EPSS no eixo y, com a região de prioridade destacada". Pode ser recriado pela equipe de produção.]

#### Metasploit Framework em ambiente controlado

O **Metasploit Framework** é um projeto de código aberto mantido pela Rapid7 e incluído no Kali Linux. Ele organiza os testes em **módulos**: *auxiliary* (varredura, enumeração e verificação, sem abrir acesso), *exploit* (exploração de uma falha específica), *payload* (o código que roda no alvo depois da exploração) e *post* (ações após o acesso), entre outros. No console `msfconsole`, o comando `search` localiza módulos por produto ou CVE, `info` descreve o que o módulo faz e quais opções exige, `use` e `set` escolhem e configuram o módulo, e `run` executa um `auxiliary/scanner`. Muitos módulos de exploração oferecem ainda o comando `check`, que pergunta se o alvo parece vulnerável sem explorá-lo. As respostas distinguem evidência direta (*vulnerable*) de evidência indireta (*appears*), que pode vir só da versão.

Em um engajamento, a regra de engajamento define quais tipos de módulo são permitidos. Neste curso, os laboratórios usam apenas `search`, `info`, módulos *auxiliary* e `check`, sempre contra *hosts* fictícios dentro do escopo.

[Imagem 2 — Tela de terminal escuro com uma sessão de console de testes mostrando uma lista de módulos e a mensagem "The target appears to be vulnerable". Texto alternativo: "Terminal com sessão de verificação de vulnerabilidade, sem exploração". Pode ser recriado pela equipe de produção a partir do laboratório da aula.]

#### Os vetores de acesso inicial

| Técnica ATT&CK | Como o adversário entra | O que a RoE costuma permitir |
|---|---|---|
| T1190 — *Exploit Public-Facing Application* | Falha em aplicação exposta à internet | Verificar a falha; não ler dados reais |
| T1133 — *External Remote Services* | VPN, RDP ou portal remoto exposto | Verificação de versão e comportamento |
| T1078 — *Valid Accounts* | Conta legítima obtida por vazamento ou reuso de senha | Só contas de teste criadas para o exercício |
| T1566 — *Phishing* (.001 anexo, .002 *link*) | Mensagem que leva a pessoa a agir | Campanha educativa, sem guardar senhas |

Nem todo acesso inicial depende de CVE. Contas válidas e falhas de lógica, como a autorização por objeto mal implementada em uma API, não aparecem no relatório do *scanner* e só são reveladas por teste.

[Imagem 3 — Diagrama com quatro portas de entrada de uma empresa: servidor exposto, VPN, aplicativo com login e caixa de *e-mail*, todas convergindo para a rede interna. Texto alternativo: "Diagrama dos quatro vetores de acesso inicial convergindo para a rede da empresa". Sugestão de busca no Envato: "network entry points diagram".]

#### *Phishing* como vetor autorizado

Muitos adversários preferem uma pessoa a uma falha técnica. Uma simulação de *phishing* autorizada exige aval formal da liderança, com RH, jurídico e encarregado de dados cientes; finalidade educativa, com orientação imediata para quem clica, e não punição; proteção de dados, sem armazenar senhas e com acesso restrito aos resultados individuais, conforme a LGPD; e limites de pretexto, vetando temas como demissões ou saúde. A métrica mais útil para a defesa é a **taxa de reporte**: um aviso rápido permite ao SOC bloquear a mensagem para todos.

#### Que rastro isso deixa para o Blue Team?

Verificações de falhas *web* deixam linhas incomuns no log do servidor, como caminhos com sequências codificadas e muitas respostas de erro. Tentativas em serviços remotos aparecem nos registros da VPN e da auditoria de identidade; o uso de contas válidas aparece como sequências de falhas seguidas de sucesso; o *phishing* passa pelo *gateway* de *e-mail*, pelo DNS e pelo *proxy*. Um ativo que não envia logs a ninguém, porém, não deixa rastro útil, por mais ruidoso que seja o teste. Por isso o Red Team registra hora e origem de cada verificação, para que o relatório compare o que foi feito com o que o SOC viu.

[Imagem 4 — Painel de monitoramento com alertas de login suspeito e de requisições anômalas a um servidor *web*. Texto alternativo: "Tela de monitoramento de segurança com alertas gerados por tentativas de acesso inicial". Sugestão de busca no Envato: "security operations center dashboard alerts".]

#### Exemplo numérico: CVSS ou EPSS?

Uma equipe que corrige 150 vulnerabilidades por semana recebe um relatório com 1.200 achados. Se priorizar tudo com CVSS ≥ 7,0 (480 achados), levará 480 ÷ 150 = **3,2 semanas** só nessa fila. Considere três casos com valores ilustrativos:

| Vulnerabilidade | CVSS | EPSS | No KEV? | Ativo |
|---|---|---|---|---|
| A | 9,8 | 0,02 (2%) | Não | Servidor interno isolado |
| B | 7,5 | 0,94 (94%) | Sim | Portal de homologação exposto à internet |
| C | 5,3 | 0,40 (40%) | Não | Serviço de acesso remoto exposto |

Pelo CVSS, A viria primeiro. Pelo risco, **B é a prioridade**, de teste e de correção: tem exploração confirmada, alta probabilidade e está exposta. Se a fila crítica incluir apenas KEV ou EPSS ≥ 10% em ativos expostos e restarem 60 achados, ela será tratada em 60 ÷ 150 = **0,4 semana**, cerca de dois dias úteis.

#### Pontos-chave

- CVE identifica a falha; CVSS mede a severidade técnica; EPSS e KEV indicam a probabilidade e a confirmação de exploração.
- Em exercício autorizado, a exploração é demonstrada com o teste menos invasivo, como `check` e módulos *auxiliary* do Metasploit.
- O acesso inicial (TA0001) inclui aplicações expostas, serviços remotos, contas válidas e *phishing*.
- Cada vetor tem limites próprios na RoE e deixa rastros que o Blue Team pode aprender a detectar.

### Referências da aula

CYBERSECURITY AND INFRASTRUCTURE SECURITY AGENCY. *Known exploited vulnerabilities catalog*. Disponível em: <https://www.cisa.gov/known-exploited-vulnerabilities-catalog>. Acesso em: 22 nov. 2026.

FORUM OF INCIDENT RESPONSE AND SECURITY TEAMS. *Common vulnerability scoring system version 4.0*: specification document. 2023. Disponível em: <https://www.first.org/cvss/>. Acesso em: 22 nov. 2026.

FORUM OF INCIDENT RESPONSE AND SECURITY TEAMS. *Exploit prediction scoring system (EPSS)*. Disponível em: <https://www.first.org/epss/>. Acesso em: 22 nov. 2026.

MITRE. *Initial access (TA0001)*. In: MITRE ATT&CK. Disponível em: <https://attack.mitre.org/tactics/TA0001/>. Acesso em: 22 nov. 2026.

RAPID7. *Metasploit documentation*. Disponível em: <https://docs.metasploit.com/>. Acesso em: 22 nov. 2026.

WEIDMAN, Georgia. *Testes de invasão*: uma introdução prática ao hacking. São Paulo: Novatec, 2014.

### Roteiro da Videoaula 6 — "Como provar que a porta está aberta sem atravessá-la?"

Duração-alvo: 15 a 20 minutos. Deck: unidade_2/slides/aula6.html (22 slides).

**Slides 1 e 2 — Capa e sumário (0:00–0:30)**
Fala: "Olá! Esta é a Aula 6. Na aula passada, o Red Team descobriu o que a Rede Tatame expõe. Hoje vamos escolher, entre centenas de falhas, as que serviriam de porta de entrada para um adversário, e provar cada uma sem atravessá-la. No sumário, você vê o caminho: referências de vulnerabilidade, Metasploit no Kali, os vetores de acesso inicial e o rastro que tudo isso deixa."
[Câmera: professor em plano médio.]

**Slide 3 — O problema de hoje na Rede Tatame (0:30–1:50)**
Fala: "O *scanner* devolveu 1.200 achados sobre a borda e a sede da Tatame. Bruno Sato, do Red Team, tem até 27 de novembro para mostrar à CISO, Marina Prado, por onde o Grupo Cobalto Austral entraria, e Caio Mendes, da TI, só consegue corrigir 150 falhas por semana. Olhe o mapa à direita: em vermelho está a `hml-gestao`, sem WAF e com cópia do banco de alunos. A regra do exercício é provar o risco sem derrubar nada e sem tocar em dado pessoal. A pergunta da aula está no quadro amarelo: entre 1.200 achados, quais dão acesso inicial, e como provar isso sem causar dano?"
[Take de apoio: porta entreaberta em corredor escuro — Envato, "door ajar dark corridor".]

**Slide 4 — Da vulnerabilidade ao acesso inicial (1:50–2:40)**
Fala: "Vulnerabilidade é a fraqueza; exploração é usar essa fraqueza para obter o que não deveria ser possível. O *scanner* fica no meio do caminho: ele deduz a falha pela versão, erra às vezes e não prova nada. O primeiro ponto de apoio do adversário é a tática TA0001 do ATT&CK, o acesso inicial. E, num exercício autorizado, a regra é demonstrar, e não executar: o teste menos invasivo, a evidência mínima e parar."

**Slide 5 — CVE dá o nome; CVSS mede a gravidade técnica (2:40–3:20)**
Fala: "Cada falha conhecida ganha um CVE, um nome comum, coordenado pela MITRE, e a NVD acrescenta a severidade. O CVSS, do FIRST, dá a nota de 0 a 10. Leia a tabela à direita: de 7,0 a 8,9 é alta; de 9,0 em diante, crítica. Guarde o quadro azul: essa nota mede gravidade técnica, e não risco."

**Slide 6 — EPSS e KEV: a falha está sendo explorada? (3:20–4:00)**
Fala: "Duas referências completam o quadro. O EPSS estima a probabilidade de exploração nos próximos 30 dias. O KEV, da CISA, lista o que já está sendo explorado. Para o Blue Team, isso ordena a correção. Para o Red Team, ordena o teste, porque o adversário que estamos emulando usaria primeiro o que já funciona contra outras vítimas."

**Slide 7 — Laboratório: a falha da `hml-gestao` em três fontes (4:00–5:30)**
Objetivo: ler uma falha real, a da `hml-gestao`, pelas três referências e decidir se ela merece teste.
Na tela:
1. Na aba "Registro e CVSS", clicar em cada parte do vetor: AV:N, AC:L, PR:N, UI:N, S:U, C:H, I:N e A:N.
2. Clicar na aba "EPSS".
3. Clicar na aba "KEV".
4. Clicar na aba "Na Rede Tatame".
Fala: "A varredura encontrou Apache 2.4.49 na `hml-gestao`, e essa versão tem a CVE-2021-41773, uma travessia de diretório: pedir arquivos fora da pasta publicada. Cada clique no vetor explica uma sigla na faixa escura. Rede, complexidade baixa, nenhum privilégio, nenhum clique de usuário: qualquer pessoa na internet consegue tentar. O impacto é alto só na confidencialidade, por isso a nota fica em 7,5, alta, e não crítica. Na aba EPSS, a probabilidade é muito alta; a planilha do exercício registrou 0,94 no dia da coleta. Na aba KEV, a resposta é sim, desde a primeira versão do catálogo, em novembro de 2021. A última aba mostra o que a RoE permite: verificar a travessia, sem copiar ou baixar arquivos e sem executar comando."
Atenção: o valor do EPSS muda todos os dias; o 0,94 é o da planilha fictícia do exercício. A página é de estudo e usa domínio `example.com`.
Conclusão: "Uma falha 'só' alta, mas explorada e exposta, vai para o topo da lista de teste."
[Tela: gravação do laboratório do slide 7.]

**Slide 8 — Laboratório: o cubo de risco (5:30–6:40)**
Objetivo: ver gravidade, probabilidade e importância do ativo ao mesmo tempo.
Na tela:
1. Arrastar a cena para girar o cubo de lado.
2. Localizar a esfera 003 (VPN) e a 002 (`hml-gestao`), no alto e dentro da caixa vermelha.
3. Localizar a esfera 001 (SRV-LEGADO-07), embaixo, fora da caixa.
Fala: "O eixo da frente é o CVSS, o vertical é o EPSS e a profundidade é a criticidade do ativo. A caixa vermelha, com o rótulo 'testar primeiro', é a região de CVSS alto, probabilidade alta e ativo importante. Os anéis amarelos marcam o que está no KEV. A VPN, 003, e a `hml-gestao`, 002, estão dentro dela. Já a 001 tem CVSS 9,8, quase o máximo, mas EPSS de 2% e fica num servidor isolado: está longe da caixa."
Atenção: as esferas pequenas são achados ilustrativos de fundo; os números que valem são os rótulos. A cena precisa de internet para carregar o three.js.
Conclusão: "CVSS alto não quer dizer porta de entrada provável."
[Tela: gravação do laboratório do slide 8.]

**Slide 9 — Metasploit Framework: uma biblioteca de módulos (6:40–7:30)**
Fala: "O Metasploit, mantido pela Rapid7, já vem no Kali. Cada teste é um módulo. Os *auxiliary* varrem e verificam sem abrir acesso; os *exploit* exploram uma falha, e muitos têm o comando `check`; os *payloads* são o que rodaria no alvo; e os *post* agem depois da entrada, assunto da próxima aula. Na Tatame, a RoE libera só *auxiliary* e `check`. Os comandos de hoje estão no quadro azul: `search`, `info`, `use`, `set`, `run` e `check`."

**Slide 10 — Laboratório: Metasploit com `check`, dentro do escopo (7:30–10:30)**
Objetivo: confirmar as duas portas de entrada mais prováveis, a `hml-gestao` e a VPN, sem explorar nenhuma.
Na tela (um clique em "▶ Próximo comando" para cada comando):
1. `cat roe/escopo-externo.txt`.
2. `msfconsole -q`.
3. `search cve:2021-41773`.
4. `info auxiliary/scanner/http/apache_normalize_path`.
5. `use auxiliary/scanner/http/apache_normalize_path`, `set RHOSTS 203.0.113.45`, `set ACTION CHECK_TRAVERSAL` e `set CVE CVE-2021-41773`.
6. `run`.
7. `search netguard`, `use auxiliary/scanner/http/netguard_sslvpn_check` e `set RHOSTS 203.0.113.30`.
8. `check`.
9. `vulns`.
Fala: "Estamos na VM `lab-tatame` do Red Team, no Kali, em 18 de novembro. Antes de abrir o Metasploit, leio o escopo do dia: em verde, os dois alvos, o teste permitido em cada um e a autorização explícita da verificação de travessia, sem guardar conteúdo; em vermelho, o que está proibido, como *payload* e cópia de arquivos, e o que está fora do escopo. O `msfconsole -q` abre o console sem o banner, e o *prompt* vira `msf6`. A busca pela CVE devolve dois módulos: o de exploração, em cinza, que não vamos usar, e o *scanner* auxiliar, destacado. O `info` mostra que o *scanner* tem três ações; a seta marca a padrão, `CHECK_TRAVERSAL`, a única que a RoE libera. A linha de opções mostra que o módulo cobre duas CVEs e que o padrão é a CVE-2021-42013, a da versão 2.4.50. Repare que o *prompt* muda com o `use`, e cada `set` responde com o valor gravado; no último, escolho a CVE-2021-41773, porque o servidor é o 2.4.49. O `run` pede um arquivo-padrão do sistema pelo caminho de travessia e só confere se a resposta tem a assinatura esperada, sem exibir nem guardar o conteúdo, uma verificação que a RoE autoriza de forma explícita: a linha com o sinal de mais diz que o alvo é vulnerável à CVE-2021-41773. Depois passamos à VPN. O módulo do NetGuard é fictício, criado para o laboratório, e só tem verificação. O `check` detecta a versão 9.1 e responde *appears to be vulnerable*, parece vulnerável: a evidência é indireta, vem da versão e do comportamento. Por fim, o `vulns` lista o que ficou registrado no banco do Metasploit, com data e hora, e a linha verde confirma: nenhum *payload*, nenhuma sessão."
Atenção: a sessão é simulada e as linhas coloridas são realces didáticos. O NetGuard e a CVE-2026-0000 são fictícios. Avise que esses comandos só podem ser usados em laboratório autorizado. O botão "⏭ Executar tudo" roda a sequência de uma vez; para gravar, vá um a um e leia a nota de rodapé de cada passo.
Conclusão: "Duas portas de entrada confirmadas, duas evidências com hora para o relatório e nenhum dano."
[Tela: gravação do laboratório do slide 10.]

**Slide 11 — As portas de entrada e a regra para cada uma (10:30–11:15)**
Fala: "Falha em *software* não é a única porta. A tabela traz quatro técnicas da TA0001. T1190 é a aplicação exposta, como a `hml-gestao` e o BOLA da API. T1133 é o serviço remoto, como a VPN. T1078 são as contas válidas: a senha certa basta. T1566 é o *phishing*. Na última coluna, a regra de engajamento de cada uma: verificar sem ler dados, só `check`, só contas de teste e campanha educativa sem guardar senha."

**Slide 12 — *Phishing* como vetor autorizado (11:15–11:50)**
Fala: "O Cobalto Austral gosta de entrar por pessoas, e por isso o *phishing* entra no exercício. Mas com quatro cuidados: autorização formal com RH, jurídico e DPO; finalidade educativa, sem punição; nenhuma senha guardada; e pretextos que não machuquem ninguém. A métrica que mais ajuda o Blue Team é a taxa de reporte."

**Slide 13 — Laboratório: quatro portas de entrada, uma semana de exercício (11:50–13:20)**
Objetivo: ver as quatro portas testadas e o que cada teste provou, inclusive o que o SOC não viu.
Na tela:
1. Ler o passo "O ponto de partida".
2. Clicar em "▶ Avançar" para "T1133 · Serviço remoto exposto" e para "T1190 · Aplicação exposta".
3. Avançar para "Rastro · Ninguém viu a hml-gestao".
4. Avançar para "T1078 · Contas válidas" e para "T1566.002 · Phishing simulado".
5. Avançar para "O que vai para o relatório".
Fala: "À esquerda, o Red Team, saindo do endereço 192.0.2.66, registrado na carta de autorização. As duas primeiras setas roxas levam a VPN e a `hml-gestao` ao relatório: são os testes do laboratório anterior. No passo de rastro, a linha tracejada âmbar vai da homologação para 'Sem alerta', porque ela não passa pelo WAF e ninguém coleta os logs dela. No app, as contas de teste mostram que basta a senha, já que não há MFA, e a seta azul indica que a regra R2 avisou o SOC. No *phishing* da Aula 1, Carla Dias clicou, mas o MFA da VPN bloqueou a senha e a R1 alertou. O último passo resume: quatro portas, duas falhas confirmadas, uma entrada por conta válida e um *phishing* contido."
Atenção: o botão "⏯ Auto" toca a sequência sozinho; para gravar, prefira "▶ Avançar" e espere cerca de dois segundos por passo.
Conclusão: "Cada porta tem uma prova diferente, e cada prova tem hora e origem para comparar com o SOC."
[Tela: gravação do laboratório do slide 13.]

**Slide 14 — Antes do código: onde achar e como instalar (13:20–13:45)**
Fala: "Antes do código, o que precisa estar instalado: o VS Code com a extensão Python da Microsoft, o Python 3.12 de python.org e o módulo `venv`, que já vem com ele. O script só usa o módulo `csv` da biblioteca padrão, então não há pacote de terceiros para baixar. Se um dia houver, confira o nome no PyPI letra por letra."

**Slide 15 — Laboratório: priorizar por risco e decidir como validar (13:45–16:00)**
Objetivo: ordenar sete achados por risco e decidir, para cada um, se o Red Team valida, só reporta ou deixa para a correção.
Na tela:
1. O VS Code ocupa o slide inteiro. O roteiro do laboratório abre com a tecla G ou com o botão "☰ Roteiro", na barra de status; deixar o painel fechado durante a gravação.
2. Clicar em "⬇ Preparar o ambiente" e esperar o botão mudar para "✓ Ambiente pronto".
3. No explorador, abrir `achados.csv` e voltar a `priorizar.py`.
4. Clicar em "Priorizar".
5. Clicar em "Calcular filas".
Fala: "O editor está em tela cheia, como no meu computador. A preparação roda quatro comandos: a versão do Python, a criação do ambiente virtual `.venv`, a ativação, que põe `(.venv)` no *prompt*, e o `pip list`, que mostra só o `pip`. No `achados.csv`, cada linha é um achado validado, com CVSS, EPSS, KEV, exposição, criticidade e o efeito da falha; as linhas destacadas são a `hml-gestao`, a VPN e o portal `gestao`. No script, a função `risco` multiplica o CVSS pela probabilidade, que vale 1 se a falha está no KEV ou o próprio EPSS se não está, pelo peso da exposição e por 1,5 se o ativo é crítico. A coluna final sai da função `validacao`: se o efeito está em `PROIBIDO_NA_ROE`, a negação de serviço, o achado só é reportado; se o risco passa de 5, vai para o `check`; senão, para a fila de correção. Na saída, a primeira linha é a ordem pelo CVSS, em que a 001 aparece em segundo lugar. Na tabela por risco, a VPN tem 10 vezes 1 vezes 1 vezes 1,5, ou seja, 15; a `hml-gestao`, 7,5 vezes 1,5, ou 11,25. As duas vão para o `check`. O `gestao` tem o mesmo risco, mas a falha é de negação de serviço e fica só no relatório. A 001 cai para o sexto lugar, com 0,06. O `fila.py` fecha a conta: 480 achados pela fila de CVSS dão 3,2 semanas; os 60 da fila crítica, 0,4 semana, cerca de dois dias úteis."
Atenção: a saída mostrada é a que o código produz de verdade; os decimais aparecem com ponto, como no Python. A preparação é simulada e leva cerca de 10 segundos.
Conclusão: "O código cruza risco e RoE antes de qualquer teste."
[Tela: gravação do laboratório do slide 15.]

**Slide 16 — Exemplo numérico: CVSS ou EPSS? (16:00–16:30)**
Fala: "O texto base traz a mesma conta com três casos. A, com 9,8, num servidor isolado e EPSS de 2%. B, com 7,5, no KEV e exposta. C, com 5,3 e EPSS de 40%. Pelo CVSS, A viria primeiro; pelo risco, B. E a fila crítica de 60 achados cabe em 0,4 semana, contra 3,2 semanas da fila por CVSS."

**Slide 17 — Laboratório: superfície e acesso inicial pelo app (16:30–18:30)**
Objetivo: ver a fila de risco na plataforma e uma entrada por contas válidas que nenhum *scanner* acha.
Na tela:
1. Conferir que a plataforma abriu na aba "Superfície", com "ordenar por risco" marcado, e ler as duas primeiras linhas.
2. Abrir a aba "Cenários" e, no cartão "Abuso da API do app", clicar em "Iniciar cenário". Esperar os quatro passos, cerca de 30 segundos na velocidade "1 s = 15 s".
3. Abrir a aba "Regras do CEP" e ligar a R3, "Token lendo fichas de muitos alunos diferentes (BOLA)".
4. Voltar a "Cenários" e clicar em "Repetir com as fontes e regras atuais".
Fala: "Na Superfície, a coluna de risco põe a VPN em primeiro, com 43,8, e a `hml-gestao` em segundo, com 32,4: a mesma ordem do script, com a fórmula didática que aparece embaixo da tabela. Agora o app. Na primeira rodada do cenário, o primeiro passo, as 2.000 tentativas com senhas vazadas, vira 'detectado' pela R2. Mas os 14 logins que dão certo e a leitura das fichas de outros alunos, trocando o número na URL, aparecem em amarelo, 'visto nos logs, sem alerta'. Nos indicadores, um detectado e três vistos sem alerta. Depois de ligar a R3 e repetir, os dois passos de leitura viram detectados: três de quatro. Só o login com conta válida continua sem regra."
Atenção: não use o botão "Reiniciar" do topo entre as rodadas, porque ele volta as regras ao padrão. Os alertas novos aparecem na aba "SOC". Se aparecer o alerta da R11 sobre a conta `svc-backup`, ele é benigno e não faz parte do cenário.
Conclusão: "Conta válida e falha de lógica entram sem CVE. Só o teste as revela, e só uma regra própria as detecta."
[Tela: gravação do laboratório do slide 17.]

**Slide 18 — Que rastro o acesso inicial deixa? (18:30–19:05)**
Fala: "Do lado da defesa, cada vetor tem a sua fonte: log do servidor *web* para a aplicação exposta, log da VPN e auditoria de identidade para o serviço remoto, falhas seguidas de sucesso para as contas válidas e o *gateway* de *e-mail* para o *phishing*. A exceção é a `hml-gestao`, sem coleta. E cada `check` do Red Team tem hora e origem, para comparar com o que o SOC viu."

**Slide 19 — De volta ao problema (19:05–19:35)**
Fala: "Voltemos à pergunta. CVSS, EPSS, KEV e criticidade puseram a VPN e a `hml-gestao` no topo. O Metasploit confirmou as duas com *scanner* e `check`, sem *payload*. O código separou o que se valida do que só se reporta. E a plataforma mostrou as entradas sem CVE. A resposta: as portas reais são a VPN, a `hml-gestao`, as contas sem MFA e o *phishing*, e o Red Team prova cada uma com o teste menos invasivo que a RoE permite."

**Slides 20 a 22 — Pontos-chave, referências e encerramento (19:35–20:00)**
Fala: "Na próxima aula, vamos ver o que o adversário faz depois de entrar: escalada de privilégios, movimentação lateral e persistência. Até lá!"
[Slides: pontos-chave e referências ficam disponíveis no material. Envato: "open door light network".]

## Aula 7 — Escalada de privilégios, movimentação lateral e persistência

### Texto base

O acesso inicial raramente é o objetivo final. Um *e-mail* clicado dá ao adversário uma única máquina, quase sempre com um usuário sem privilégios. O que transforma esse ponto de apoio em incidente grave é a **pós-exploração**, um ciclo que se repete a cada máquina nova: descobrir o ambiente (TA0007, *Discovery*), obter permissões mais altas (TA0004, *Privilege Escalation*), saltar para outra máquina (TA0008, *Lateral Movement*) e garantir a volta (TA0003, *Persistence*). Muitos exercícios começam direto nessa fase, em um cenário de **acesso presumido** (*assumed breach*): a organização entrega ao Red Team uma conta comum, como se o *phishing* tivesse funcionado, e mede o que acontece depois. Nesta aula, cada técnica é tratada em nível conceitual e sempre acompanhada do rastro que deixa para o Blue Team.

#### Descoberta: o mapa antes do salto

Dentro da rede, o adversário precisa saber onde estão os servidores, quais serviços respondem e quem pertence a quais grupos. A descoberta de serviços (T1046, *Network Service Discovery*) usa varreduras internas, e a descoberta de contas e grupos do domínio (T1087.002 e T1069.002) usa consultas LDAP ao Active Directory (AD). No Kali Linux, o Nmap e os módulos *auxiliary* do Metasploit, como o `smb_version`, cumprem esse papel. O rastro são muitas conexões a partir de uma única estação e consultas volumosas ao diretório feitas por uma conta comum.

#### Escalada de privilégios

| Caminho | Técnica | Rastro típico |
|---|---|---|
| Falha sem correção no sistema ou em um serviço | T1068 | Processo com privilégio de sistema criado por usuário comum (evento 4688, Sysmon 1) |
| Desvio do controle de conta de usuário (UAC) | T1548.002 | Processo elevado sem tela de confirmação |
| Grupo amplo com administração local ou senha de administrador reaproveitada | T1078.002 e T1078.003 | *Logon* (4624) seguido de privilégios especiais (4672) fora do padrão da conta |
| Senha esquecida em *script* | T1552.001 | Leitura do arquivo por quem não o usa (4663, se auditado) |

Repare que dois dos quatro caminhos não exploram nenhuma falha de *software*: bastam uma configuração fraca e uma credencial válida. Por isso, separar contas administrativas das de uso diário e restringir a administração local está entre as recomendações mais frequentes dos relatórios. Em seguida vem o acesso a credenciais (TA0006): um administrador com sessão aberta em uma máquina deixa material de autenticação na memória do processo LSASS, e o acesso a essa memória (T1003.001) é um dos comportamentos mais vigiados pelo EDR (Sysmon 10).

[Imagem 1 — Escada com degraus rotulados "usuário comum", "administrador local", "suporte" e "administrador do domínio". Texto alternativo: "Escada representando a escalada de privilégios do usuário comum ao administrador do domínio". Sugestão de busca no Envato: "stairs levels access hierarchy".]

#### Movimentação lateral

Com uma conta mais forte, o adversário salta. Pelo RDP (T1021.001), o *logon* aparece como evento 4624 do tipo 10, remoto interativo; pelos compartilhamentos administrativos via SMB (T1021.002), como 4624 do tipo 3, de rede, acompanhado dos eventos 5140 e 5145; no reuso de *hash* (T1550.002), surge autenticação NTLM onde o normal seria Kerberos. O sinal raramente é o evento em si, que administradores geram todos os dias, e sim a combinação incomum: uma conta do suporte abrindo RDP a partir do notebook da recepção.

[Imagem 2 — Diagrama de uma rede corporativa com uma estação comprometida e setas indicando saltos sucessivos até um controlador de domínio. Texto alternativo: "Diagrama de movimentação lateral de uma estação de trabalho até o controlador de domínio". Sugestão de busca no Envato: "network diagram lateral movement".]

#### Persistência

| Técnica | Mecanismo | Rastro típico |
|---|---|---|
| T1053.005 | Tarefa agendada | Evento 4698, se a auditoria *Other Object Access Events* estiver ligada |
| T1543.003 | Serviço do Windows | Evento 7045 (log *System*) e 4697 |
| T1136.001 e T1136.002 | Conta local ou de domínio criada | Evento 4720 e inclusão em grupo |
| T1547.001 | Chave de registro *Run* | Sysmon 13 |

#### Caminhos de ataque em grafos

No AD, as permissões formam uma rede: o usuário A administra a máquina B, onde o administrador C faz *logon*, e C pertence a um grupo que controla o domínio. O **BloodHound** representa essas relações como um **grafo** e calcula **caminhos de ataque** até o grupo *Domain Admins*. A defesa usa a mesma visão: eliminar uma relação mal configurada pode cortar dezenas de caminhos. Vale a frase atribuída a John Lambert, da Microsoft: os defensores pensam em listas, os atacantes pensam em grafos.

[Imagem 3 — Grafo com nós de usuários, computadores e grupos, destacando em vermelho o caminho mais curto até o grupo de administradores do domínio. Texto alternativo: "Grafo de caminhos de ataque no Active Directory com o caminho crítico destacado". Pode ser recriado pela equipe de produção.]

#### Limites no engajamento

As regras de engajamento dizem até onde a equipe vai. O impacto é **demonstrado, e não executado**: em vez de copiar fichas de alunos, registra-se a evidência mínima de acesso. Credenciais obtidas são protegidas e trocadas ao final. Persistência só é aceita com **marca** (nome que cita o chamado do exercício), programa inofensivo, registro de hora, máquina e *hash*, e remoção conferida até o último dia da janela. Módulos *post* do Metasploit, criação de contas no domínio e redes fora do escopo ficam vetados quando a autorização não os prevê.

[Imagem 4 — Etiqueta amarela presa a um cabo de servidor com a inscrição "teste autorizado, remover até 27/11". Texto alternativo: "Etiqueta de identificação em equipamento, representando o artefato de teste marcado e com prazo de remoção". Sugestão de busca no Envato: "server cable tag label".]

#### Exemplo numérico: cortando caminhos

Em um domínio com 5.000 contas, a análise de grafo mostra que 1.200 delas (**24%**) têm algum caminho até os administradores do domínio. Quase todos passam por dois servidores em que administradores fazem *logon* rotineiramente e por um grupo de suporte com permissões excessivas. Corrigidos esses três pontos, restam 40 contas com caminho: 40 ÷ 5.000 = **0,8%**, uma redução de 1.160 ÷ 1.200 ≈ **97%** dos caminhos.

#### Pausa para reflexão

> No último dia de um exercício autorizado, o administrador de TI da organização pede ao Red Team que não remova a tarefa agendada marcada que ficou em um servidor de arquivos: "deixe ligada mais 30 dias, para ver se o SOC acha sozinho".
>
> 1. O Red Team pode atender ao pedido? Considere a janela de execução, a carta de autorização e quem a assinou.
> 2. Que risco um artefato de persistência esquecido cria para a organização?
> 3. Que alternativa testa a detecção de persistência sem deixar nada para trás?
>
> **Desafio prático:** redija o item "Persistência" das regras de engajamento: técnicas permitidas, marcação, registro, prazo de remoção e quem confere a limpeza.

#### Pontos-chave

- Descoberta, escalada, movimentação lateral e persistência formam um ciclo que se repete a cada máquina.
- Contas válidas e configurações fracas escalam privilégio sem nenhuma falha de *software*.
- Cada técnica deixa um evento conhecido; sem regra que o observe, ninguém é avisado.
- Em engajamento, o impacto é demonstrado e a persistência é marcada, registrada e removida.

### Referências da aula

LAMBERT, John. *Defenders think in lists. Attackers think in graphs. As long as this is true, attackers win*. 2015. Disponível em: <https://github.com/JohnLaTwC/Shared/blob/master/Defenders%20think%20in%20lists.%20Attackers%20think%20in%20graphs.%20As%20long%20as%20this%20is%20true%2C%20attackers%20win.md>. Acesso em: 22 nov. 2026.

MITRE. *Lateral movement (TA0008)*. In: MITRE ATT&CK. Disponível em: <https://attack.mitre.org/tactics/TA0008/>. Acesso em: 22 nov. 2026.

MITRE. *Persistence (TA0003)*. In: MITRE ATT&CK. Disponível em: <https://attack.mitre.org/tactics/TA0003/>. Acesso em: 22 nov. 2026.

MITRE. *Privilege escalation (TA0004)*. In: MITRE ATT&CK. Disponível em: <https://attack.mitre.org/tactics/TA0004/>. Acesso em: 22 nov. 2026.

SANTOS, Joas Antonio dos. *Introdução ao Red Team Operations 2.0*: um guia básico para suas operações de Red Team. Rio de Janeiro: Brasport, 2024. *E-book*.

WEIDMAN, Georgia. *Testes de invasão*: uma introdução prática ao hacking. São Paulo: Novatec, 2014.

### Roteiro da Videoaula 7 — "Da recepção ao administrador do domínio: quantos passos o SOC enxerga?"

Duração-alvo: 15 a 20 minutos. Deck: unidade_2/slides/aula7.html (22 slides).

**Slides 1 e 2 — Capa e sumário (0:00–0:30)**
Fala: "Olá! Esta é a Aula 7, e hoje vamos acompanhar o adversário depois que ele já entrou. Vamos ver como ele descobre o domínio, aumenta os próprios privilégios, salta entre máquinas e tenta ficar, e que rastro cada passo deixa para o Blue Team. Como sempre, tudo acontece na Rede Tatame, a nossa rede fictícia de academias, dentro de um exercício autorizado."
[Câmera: professor em plano médio.]

**Slide 3 — O problema de hoje na Rede Tatame (0:30–1:40)**
Fala: "Estamos na fase 2 do exercício de novembro. A CISO Marina Prado autorizou um cenário de acesso presumido: o Red Team de Bruno Sato recebeu uma conta de teste com os mesmos direitos de um usuário da recepção e uma máquina virtual Kali no segmento do laboratório, como se um *e-mail* falso tivesse funcionado. A pergunta da aula está no quadro amarelo: a partir de um usuário comum da recepção, até onde o adversário chega no domínio, e que rastro cada passo deixa para o SOC? No mapa à direita, o caminho em vermelho vai de um notebook da sede ao servidor de arquivos e dali ao controlador do Active Directory, o diretório que guarda contas e permissões. O mapa desenha o NB-FIN-031; o notebook da recepção, o NB-REC-001, fica na mesma rede. Quem controla o domínio controla o SRV-ARQ-01, com fichas de alunos menores, e o ERP financeiro."
[Take de apoio: recepção de academia com computador no balcão — Envato, "gym reception computer".]

**Slide 4 — Do ponto de apoio ao domínio: um ciclo (1:40–2:25)**
Fala: "O acesso inicial dá ao adversário uma máquina e um usuário comum. A partir daí, ele entra em um ciclo de quatro táticas do MITRE ATT&CK: descoberta, para mapear usuários, grupos e servidores; escalada de privilégios, para ganhar permissões mais altas; movimentação lateral, para saltar para outra máquina; e persistência, para garantir a volta depois de uma reinicialização ou de uma troca de senha. Em cada máquina nova, o ciclo recomeça. E em cada etapa vamos perguntar: que evento isso gera para o defensor?"

**Slide 5 — Escalada de privilégios: quatro caminhos comuns (2:25–3:20)**
Fala: "A tabela mostra quatro caminhos de escalada e o rastro de cada um. O primeiro explora uma falha sem correção, a T1068, e aparece como um processo com privilégio de sistema criado por um usuário comum. O segundo desvia o controle de conta de usuário do Windows, a tela que pede confirmação, e é a T1548.002. Agora repare nos dois últimos: nenhum explora falha de *software*. Um grupo amplo com administração local, ou uma senha de administrador reaproveitada, já basta; o rastro é um *logon*, o evento 4624, seguido do 4672, que registra privilégios especiais. E uma senha esquecida em um *script* é a T1552.001. Na Tatame, os dois últimos acontecem juntos no notebook da recepção."

**Slide 6 — Laboratório: da recepção ao controlador de domínio (3:20–5:40)**
Objetivo: mostrar o caminho completo na sede e o rastro esperado em cada etapa, a primeira parte da resposta à pergunta da aula.
Na tela:
1. Mostrar o diagrama parado: na linha de cima, NB-REC-001, Diretório, SRV-ARQ-01 e SRV-AD-01; embaixo, Persistência, EDR, SIEM e Revisão purple.
2. Clicar em "▶ Avançar" para o passo 1, "Ponto de apoio (acesso presumido)".
3. "▶ Avançar" para o passo 2, "Descoberta (TA0007) · 10h02": seta vermelha do notebook ao Diretório.
4. "▶ Avançar" para o passo 3, "Escalada local (TA0004) · 11h40": acende só o NB-REC-001.
5. "▶ Avançar" para o passo 4, "Movimentação lateral (TA0008) · 13h20": seta vermelha até o SRV-ARQ-01 e linha âmbar até o SIEM, que fica com contorno vermelho.
6. "▶ Avançar" para o passo 5, "Credenciais (TA0006) · 14h05": linha azul até o EDR.
7. "▶ Avançar" pelos passos 6, "Contas válidas (T1078) · 15h10", e 7, "Persistência (TA0003) · 15h30".
8. Terminar no passo 8, "Revisão purple", com o contador em 8/8.
Fala: "Leia a legenda de cada passo embaixo do diagrama. No passo 2, às 10h02, a equipe lista serviços e grupos do domínio a partir do Kali; o rastro esperado são consultas volumosas ao AD, a regra R13 da plataforma, que vem desligada. No passo 3, a escalada: o grupo TODOS-SEDE, do qual todo mundo faz parte, é administrador do notebook da recepção. Então a conta comum já tem privilégio local, e ali existe um *script* de manutenção com a senha do sup.heitor, do suporte. No passo 4, com a conta do suporte, a equipe abre RDP do notebook para o SRV-ARQ-01. O evento 4624 do tipo 10 estava lá, mas sem regra: por isso a linha é âmbar e o SIEM fica com contorno vermelho. No passo 5, um administrador do domínio, o adm.caio, tem sessão aberta nesse servidor. A equipe emula o acesso à memória do LSASS, o processo do Windows que guarda credenciais, e o EDR alerta: linha azul. No passo 6, com a conta do administrador, o acesso ao controlador de domínio parece trabalho normal, e a equipe só grava o arquivo-marca combinado. No passo 7, duas persistências marcadas com o código do chamado, uma tarefa agendada e uma chave Run. No passo 8, Red e Blue comparam: quase tudo deixou evento, e só uma etapa virou alerta."
Atenção: o diagrama é conceitual e não mostra como executar nenhuma técnica. O botão "⏯ Auto" avança sozinho; na gravação, prefira "▶ Avançar". Nas linhas, azul é alerta e âmbar é evento registrado sem alerta; o contorno vermelho marca onde a defesa não reagiu.
Conclusão: "Da recepção ao administrador do domínio são poucos saltos, e quase todos deixaram evento. O problema é que só um virou alerta."
[Tela: gravação do laboratório do slide 6.]

**Slide 7 — Descoberta e movimentação lateral (5:40–6:30)**
Fala: "Agora o detalhe de duas táticas. Na descoberta, a T1046 lista serviços da rede interna e a T1087.002 lista contas e grupos do domínio. Na movimentação lateral, cada protocolo deixa uma assinatura diferente: o RDP gera *logon* do tipo 10; o acesso aos compartilhamentos administrativos, como C$ e ADMIN$, gera *logon* do tipo 3 e os eventos 5140 e 5145; e o reuso de *hash* aparece como autenticação NTLM onde o normal seria Kerberos. No quadro azul, um ponto importante: o Metasploit, que vem no Kali, tem módulos *auxiliary*, de descoberta, e módulos *post*, de pós-exploração. As regras de engajamento da Tatame autorizaram só os primeiros."

**Slide 8 — Laboratório: descoberta do domínio no Kali Linux (6:30–8:50)**
Objetivo: mapear serviços e grupos do domínio dentro do que a fase 2 autoriza, e perceber que cada consulta deixa rastro.
Na tela:
1. Clicar em "▶ Próximo comando": `cat escopo/fase2_acesso_presumido.txt`.
2. "▶ Próximo comando": `nmap -sV -Pn -p 88,135,389,445,3389` contra os três servidores.
3. "▶ Próximo comando": `msfconsole` com o módulo `auxiliary/scanner/smb/smb_version`.
4. "▶ Próximo comando": `ldapsearch` com a conta de teste.
5. "▶ Próximo comando": `sha256sum` da evidência, gravado no `registro.log`.
6. Ler a nota de rodapé de cada comando antes de avançar.
Fala: "O *prompt* mostra kali@lab-tatame, a máquina virtual do Red Team. O primeiro comando não ataca nada: relê o escopo da fase 2. Origem autorizada 10.10.250.66, conta de teste tst.redteam01, três servidores como alvo, Metasploit só com módulos de descoberta, e a linha amarela lembra que persistência só com a marca RT-APR2291. O segundo comando é o Nmap com `-sV`, que identifica o serviço e a versão em cada porta. Leia a primeira tabela: o SRV-AD-01 responde em 88, que é o Kerberos, em 389, o LDAP do Active Directory, e em 445 e 3389, SMB e área de trabalho remota. Os outros dois servidores não têm Kerberos nem LDAP, o que confirma que o controlador de domínio é só o primeiro. O terceiro comando abre o Metasploit em modo silencioso e roda o módulo `smb_version`. Ele só pergunta a cada servidor que versão de SMB fala e se exige assinatura. As linhas com sinal de mais mostram Windows Server 2012 R2 nos três, e a linha amarela traz o achado: o SRV-ARQ-01 ainda aceita SMB 1, e dois servidores não exigem assinatura. O quarto comando consulta o AD com a conta de teste; a senha é digitada e não aparece. A resposta lista os membros de três grupos: adm.caio em Domain Admins, sup.heitor e sup.iris no SUPORTE-N1, e atd.elisa no LEGADO-ERP. Guarde esses nomes, porque eles voltam no grafo. E repare na nota: essa consulta é exatamente o que a regra R13 detecta. O último comando calcula o *hash* do arquivo de evidência e o grava no registro da operação."
Atenção: o terminal é simulado; os servidores, endereços e contas são fictícios. Comente que, no mundo real, esses comandos só podem ser usados contra ambientes com autorização escrita. A saída do Nmap foi resumida para os dois últimos servidores. O comando do Metasploit é longo e quebra em duas linhas no terminal.
Conclusão: "A descoberta já aponta o caminho: grupos, servidores e uma configuração fraca. E cada consulta ao AD deixa rastro para quem tiver a regra."
[Tela: gravação do laboratório do slide 8.]

**Slide 9 — Defensores pensam em listas, atacantes em grafos (8:50–9:25)**
Fala: "No Active Directory, as permissões formam uma rede de relações: o usuário A administra a máquina B, onde o administrador C costuma fazer *logon*, e C pertence a um grupo que controla o domínio. O BloodHound representa essas relações como um grafo e calcula caminhos de ataque até o grupo Domain Admins. E a defesa pode usar a mesma visão: eliminar uma relação mal configurada corta dezenas de caminhos de uma vez. É o sentido da frase de John Lambert, no quadro azul."
[Take de apoio: quadro de investigação com fios ligando fotos — Envato, "investigation board strings".]

**Slide 10 — Laboratório: o grafo do diretório em 3D (9:25–11:00)**
Objetivo: descobrir quais relações, se cortadas, eliminam mais caminhos até o topo.
Na tela:
1. Mostrar a cena parada: embaixo os usuários, no meio grupos e computadores, no topo o losango amarelo "DOMAIN ADMINS". No painel, "10 de 11 usuários comuns com caminho" e "rec.ana: 7 saltos".
2. Arrastar para girar a cena e seguir as arestas vermelhas de rec.ana.
3. Clicar em "Cortar sessão no SRV-ARQ-01": o painel vai para 3 de 11 e rec.ana fica sem caminho.
4. Clicar em "Cortar sessão no SRV-ERP-01": o painel cai para 1 de 11.
5. Clicar em "Cortar admin do NB-REC-001": o painel continua em 1 de 11.
6. Clicar em "Restaurar" e voltar aos 10 de 11.
Fala: "Esfera vermelha é um usuário comum com algum caminho até o topo; azul é quem não tem. São 11 usuários comuns, porque o adm.caio já é administrador e não entra na conta. O caminho da rec.ana, a recepcionista, tem 7 saltos: TODOS-SEDE, NB-REC-001, a sessão do sup.heitor, SUPORTE-N1, SRV-ARQ-01, a sessão do adm.caio e o topo. É o mesmo caminho do fluxo e dos grupos que o Kali listou. Quando corto a sessão do administrador no SRV-ARQ-01, sete usuários perdem o caminho de uma vez. A sessão no SRV-ERP-01 derruba os dois desenvolvedores. O terceiro corte tira do TODOS-SEDE a administração do notebook da recepção; o número não muda agora, mas fecha a escalada local por outro lado. Sobra a atd.elisa, pelo grupo antigo LEGADO-ERP."
Atenção: nenhuma técnica de ataque é executada; a cena só lê relações de permissão. Os rótulos do fundo ficam menores pela perspectiva; gire a cena antes de ler um nome. A cena precisa de internet para carregar o three.js.
Conclusão: "Poucas correções bem escolhidas cortam quase todos os caminhos da recepção ao domínio."
[Tela: gravação do laboratório do slide 10.]

**Slide 11 — Antes do código: onde achar e como instalar (11:00–11:20)**
Fala: "Antes do código, o que ele exige: o Visual Studio Code com a extensão Python da Microsoft, o Python 3.8 ou mais novo, por causa do operador dois-pontos-igual, e só módulos da biblioteca padrão. O BloodHound, citado no comentário, não é instalado: o laboratório reproduz apenas a ideia do grafo, sobre um diretório fictício."

**Slide 12 — Laboratório: menor caminho por busca em largura (11:20–13:20)**
Objetivo: contar, com código, quantos usuários chegam a Domain Admins antes e depois das correções.
Na tela:
1. O VS Code ocupa o slide inteiro. O roteiro do laboratório abre com a tecla G ou com o botão "☰ Roteiro", na barra de status; deixar esse painel fechado durante a gravação.
2. Clicar em "⬇ Preparar o ambiente" e esperar o botão mudar para "✓ Ambiente pronto".
3. Com `caminhos.py` aberto, destacar a função `menor_caminho`.
4. Abrir `grafo.json` no explorador e mostrar a lista "arestas".
5. Clicar em "Antes das correções" e esperar a saída.
6. Abrir `correcoes.json`.
7. Clicar em "Depois das correções" e ler a saída.
Fala: "O editor ocupa a tela inteira, como no meu computador. Primeiro, o ambiente: o terminal confere o Python 3.12, cria o ambiente virtual `.venv`, uma cópia isolada do Python só para este projeto, e o ativa, o que aparece no `(.venv)` do *prompt*. O `pip list` mostra só o `pip`, porque o script usa apenas a biblioteca padrão. No `grafo.json`, cada aresta tem origem, relação e destino. MemberOf é ser membro de um grupo, AdminTo é administrar uma máquina, HasSession é ter sessão aberta nela e GenericAll é ter controle total sobre um objeto. No código, o primeiro bloco lê o grafo e, se eu passar um arquivo na linha de comando, as arestas removidas. O laço que monta `vizinhos` pula as removidas: é essa linha que faz a correção ter efeito. A função `menor_caminho` é uma busca em largura: com uma fila, visita primeiro os vizinhos a um salto, depois a dois, e assim por diante; por isso o primeiro caminho que encontra é o mais curto. Na saída de antes: 10 de 11, ou 91%. A atd.elisa chega em 3 saltos, os dois do suporte e os dois desenvolvedores em 4, e cinco usuários em 7, entre eles a rec.ana. Depois das 3 correções do `correcoes.json`: 1 de 11, ou 9%. Sobra só a atd.elisa pelo LEGADO-ERP, que é a próxima correção a propor."
Atenção: o terminal é simulado e mostra a saída que o código produz de verdade; o código pode ser rodado em casa com os mesmos arquivos. É o mesmo grafo da cena 3D, por isso os números batem. A preparação do ambiente leva cerca de 10 segundos.
Conclusão: "Com o cálculo, a Tatame mostra o efeito de cada correção antes de aplicá-la."
[Tela: gravação do laboratório do slide 12, com zoom na função `menor_caminho`.]

**Slide 13 — Persistência: ficar depois da reinicialização (13:20–14:10)**
Fala: "A última tática do ciclo é a persistência. Uma tarefa agendada, a T1053.005, gera o evento 4698, desde que a auditoria de objetos esteja ligada. Um serviço novo, a T1543.003, gera o 7045 no log de sistema. Uma conta criada pelo adversário gera o 4720. E uma chave Run, que executa um programa a cada *logon*, aparece no Sysmon como evento 13. No quadro azul está a regra do exercício: persistência só com marca, com o código do chamado no nome, programa inofensivo, registro de hora, máquina e *hash*, e remoção conferida no último dia da janela."

**Slide 14 — Laboratório: que evento existe em cada etapa (14:10–15:50)**
Objetivo: separar o que virou alerta do que ficou só nos registros, a parte da pergunta sobre o que o SOC enxerga.
Na tela:
1. Clicar na busca salva "1. Logon remoto atípico".
2. Clicar em "2. Acesso à memória do LSASS".
3. Clicar em "3. Tarefa agendada criada".
4. Clicar em "4. Inicialização automática alterada".
Fala: "Luiza Ferraz revisa o dia 18 no SIEM, com a linha do tempo do Red Team em mãos. A busca 1 filtra *logons* do tipo 10 que saem de notebooks da recepção para servidores: um evento, às 13:20:44, sup.heitor do NB-REC-001 para o SRV-ARQ-01, e a coluna 'alerta?' diz não. A busca 2 procura processos fora de uma lista aprovada abrindo a memória do LSASS: às 14:05:12, um `atualizador.exe` rodando de uma pasta pública, severidade crítica. É o único alerta do dia. A busca 3 lista os eventos 4698: a tarefa de *backup* do svc-backup, que é aprovada, e a tarefa RT-APR2291-marca, criada às 15:31 no SRV-ARQ-01, sem alerta. A busca 4 lê o Sysmon 13 em chaves Run: a marca do Red Team no notebook da recepção, às 15:44, também sem alerta."
Atenção: as consultas estão em uma sintaxe parecida com KQL só para ilustrar o filtro; explique o que cada linha seleciona, sem entrar na sintaxe. Lembre que as duas persistências são marcadas e constam da planilha do Red Team.
Conclusão: "O SOC tinha o evento de quase tudo, mas só foi avisado do LSASS. Evento sem regra fica guardado e ninguém é avisado."
[Tela: gravação do laboratório do slide 14.]

**Slide 15 — Laboratório: a movimentação lateral na plataforma (15:50–17:40)**
Objetivo: ver a emulação inteira na plataforma e medir o que muda com duas regras novas.
Na tela:
1. Conferir que a plataforma abriu na aba "Cenários". No topo, trocar a "Velocidade" para "1 s = 1 min".
2. No cartão "Emulação do Grupo Cobalto Austral", clicar em "Iniciar cenário" e esperar cerca de 15 segundos, até o passo do impacto.
3. Ler os indicadores abaixo da linha do tempo: 3 detectados, 2 não detectados, 3 vistos sem alerta.
4. Abrir "Regras do CEP" e ligar a R5, "RDP de estação de trabalho para servidor", e a R13, "Consulta em massa ao AD".
5. Voltar a "Cenários" e clicar em "Repetir com as fontes e regras atuais". Esperar o fim e ler: 6 detectados, 0 vistos sem alerta.
6. Abrir "Cobertura ATT&CK" e localizar T1021.001 e T1087.002 como "comprovada".
Fala: "Na plataforma, a emulação entra pela VPN, com a senha vazada de caio.mendes, mas as etapas internas são as mesmas: consulta em massa ao AD, RDP para o SRV-ARQ-01, LSASS, RDP para o SRV-ERP-01, cópia de fichas, exclusão das cópias de sombra e impacto. Na primeira rodada, a consulta ao AD e os dois RDPs aparecem com o ícone amarelo, 'visto nos logs, sem alerta': o evento chegou, mas o CEP, o motor que correlaciona eventos, não tinha regra ligada. Ligo a R5 e a R13 e repito com as mesmas fontes. Agora são 6 detectados e nenhum visto sem alerta, e na cobertura as duas técnicas passam a comprovadas. Os dois passos que continuam sem detecção dependem de outra fonte, a de saída de rede, que fica para a Unidade 3."
Atenção: não use o botão "Reiniciar" do topo entre as rodadas, porque ele volta as regras ao padrão; o "Repetir com as fontes e regras atuais" mantém a R5 e a R13. Na aba "SOC" aparece também um alerta benigno da R11 sobre a conta `svc-backup`, que não faz parte do cenário. Se quiser mostrar a contenção, volte a velocidade para "1 s = 15 s", repita o cenário e, no "SOC", clique em "Conter" no alerta da R11 que cita caio.mendes: o cenário para em 1 de 8 passos.
Conclusão: "O evento já existia. Faltava a regra, e com ela o SOC passa a ver a movimentação lateral."
[Tela: gravação do laboratório do slide 15, com as duas rodadas.]

**Slide 16 — Impacto demonstrado, e não executado (17:40–18:15)**
Fala: "As regras de engajamento definem até onde a equipe vai. Em vez de copiar fichas de alunos do SRV-ARQ-01, o Red Team registra a evidência mínima de que teria acesso. Em vez de alterar o domínio, grava um arquivo-marca combinado. Credenciais são protegidas e trocadas no fim, e persistências marcadas são removidas no último dia, com registro. Módulos *post*, criação de contas no domínio e a rede de pagamentos ficaram fora da autorização, e a palavra de parada 'LARANJA' interrompe qualquer etapa."

**Slide 17 — Pausa para reflexão (18:15–18:45)**
Fala: "Agora pense comigo. No último dia, Caio Mendes pede a Bruno que deixe a tarefa agendada ligada mais 30 dias, para ver se o SOC acha sozinho. O Red Team pode atender? Quem assinou a autorização, e até quando ela vale? Que risco um artefato esquecido cria? E que alternativa testa a detecção de persistência sem deixar nada para trás? Pause o vídeo, responda e faça o desafio: escrever o item 'Persistência' das regras de engajamento."
[Câmera: professor em plano fechado.]

**Slide 18 — Exemplo numérico: cortando caminhos em escala (18:45–19:10)**
Fala: "Em escala maior: em um domínio com 5.000 contas, 1.200 têm caminho até os administradores do domínio, 24%. Corrigidos dois servidores com *logon* rotineiro de administradores e um grupo de suporte com permissões excessivas, restam 40 contas, 0,8%. São 97% dos caminhos cortados com três correções."

**Slide 19 — De volta ao problema (19:10–19:40)**
Fala: "Voltemos à pergunta: a partir de um usuário comum da recepção, até onde o adversário chega, e que rastro deixa? O fluxo e o Kali mostraram a rota até a sessão do administrador do domínio. O grafo e o código calcularam 10 de 11 usuários com caminho, e 1 depois de três correções. O SIEM mostrou que quase tudo deixou evento, mas só o LSASS virou alerta. E a plataforma mostrou que a R5 e a R13 transformam esses eventos em detecção."

**Slides 20 a 22 — Pontos-chave, referências e encerramento (19:40–19:58)**
Fala: "Para levar: o ciclo se repete a cada máquina, contas válidas escalam sem falha de *software*, cada técnica deixa um evento conhecido e, em engajamento, a persistência é marcada e removida. Na próxima aula, o adversário tenta apagar esses rastros, e vamos ver como o defensor percebe isso. Até lá!"
[Envato: "keychain master key", "security operations center screens".]

## Aula 8 — Evasão básica de defesas e limpeza de rastros em laboratório

### Texto base

Um adversário que chegou aos servidores de uma empresa tem um novo problema: continuar lá sem ser notado. Cada minuto a mais dentro do ambiente aumenta as chances de alcançar o objetivo, e cada alerta disparado aumenta as chances de ser expulso. Por isso, grupos reais investem em técnicas para se esconder, cegar os controles e apagar o que deixaram para trás. Nesta aula, estudamos essas técnicas como o defensor as enxerga: pelo rastro que cada uma produz. Encerramos com a outra face do tema, a limpeza legítima que o Red Team faz ao final de um exercício, e com o relatório que fecha a operação.

#### Furtividade e enfraquecimento de defesas

No MITRE ATT&CK atual, a evasão de defesas ocupa duas táticas. A **Furtividade** (*Stealth*, TA0005) reúne o que o adversário faz para se esconder: apagar arquivos usados (T1070.004 — *File Deletion*), alterar as datas de um arquivo para que ele pareça antigo (T1070.006 — *Timestomp*), disfarçar um programa com o nome de outro legítimo (T1036 — *Masquerading*) e ofuscar conteúdo (T1027 — *Obfuscated Files or Information*). O **Enfraquecimento de defesas** (*Defense Impairment*, TA0112) reúne o que ele faz para cegar os controles: parar ou modificar o antivírus e o agente EDR (T1685 — *Disable or Modify Tools*), desativar o log de eventos do Windows (T1685.001) e apagar logs já gravados (T1685.005 — *Clear Windows Event Logs*). Materiais anteriores a 2026 chamam tudo de *Defense Evasion* (TA0005) e usam T1562 (*Impair Defenses*) para os controles desligados.

[Imagem 1 — Ilustração de uma silhueta apagando pegadas na areia enquanto uma câmera de segurança registra a cena. Texto alternativo: "Pessoa tentando apagar pegadas observada por uma câmera, representando a remoção de indicadores que ainda deixa rastro". Sugestão de busca no Envato: "erasing footprints security camera".]

#### Toda técnica de evasão deixa um rastro próprio

Essas técnicas, porém, também geram evidências. Ao apagar o log de Segurança, o próprio Windows grava o evento **1102** (*The audit log was cleared*), com a conta que fez a limpeza; quando outro log é apagado, aparece o evento **104** no log de Sistema. Parar o agente EDR gera, no log de Sistema, o evento **7036** (serviço entrou no estado parado) e, se o tipo de início for alterado, o **7040**; um serviço novo instalado aparece como **7045**. No console do EDR, o agente parado deixa de enviar o sinal periódico de vida, o *heartbeat*, e abre uma **lacuna de telemetria**. O Sysmon, ferramenta gratuita da Microsoft que detalha a atividade do Windows, registra a mudança de data de criação de um arquivo (evento **2**), arquivos apagados (eventos **23** e **26**) e processos criados (evento **1**), o que revela um `svchost.exe` rodando fora da pasta `C:\Windows\System32`.

[Imagem 2 — Tabela visual com quatro colunas ligando técnica, evento gerado, log de origem e o que o analista procura. Texto alternativo: "Quadro que associa técnicas de evasão aos eventos 1102, 7036, 7040 e Sysmon 2 que elas geram". Pode ser recriado pela equipe de produção.]

#### Duas defesas que tornam a evasão cara

O rastro só ajuda se sobreviver. A primeira defesa é **encaminhar os logs para fora da máquina** assim que são gerados, pelo *Windows Event Forwarding* (WEF) ou pelo agente do SIEM, como o Wazuh. Assim, apagar o log local leva só uma cópia; a central continua íntegra e ainda recebe o 1102. A segunda é a **proteção contra adulteração** (*tamper protection*) do EDR, que impede que o agente seja parado ou desinstalado sem autorização central e avisa o SOC da tentativa. Há ainda uma terceira, de processo: tratar o silêncio como sinal. Um servidor que para de enviar *heartbeat* no meio do expediente, sem reinício planejado, merece investigação.

[Imagem 3 — Diagrama com um servidor enviando eventos ao SIEM em tempo real e uma cópia local sendo apagada, enquanto a cópia central permanece. Texto alternativo: "Fluxo de encaminhamento de logs mostrando que apagar a cópia local não apaga a cópia central". Pode ser recriado pela equipe de produção.]

#### Evasão em um exercício autorizado

Em um engajamento, a evasão só entra para **medir a detecção**. As regras de engajamento listam cada técnica, os servidores em que ela pode ser emulada e a janela, sempre combinadas com o White Team, que controla o exercício. Desligar uma defesa de produção exige autorização expressa e prazo para religar; limpar um log só é aceitável depois de confirmar que ele foi encaminhado ao SIEM, porque a cópia central é evidência que o exercício precisa preservar. Na Rede Tatame, a carta assinada por Marina Prado permitiu parar o agente EDR em dois servidores por até 40 minutos e limpar o log de Segurança do `SRV-ARQ-01` depois de conferido o encaminhamento.

#### Limpeza legítima de rastros

No fim do exercício, "limpar rastros" ganha outro sentido. O Red Team **remove tudo o que criou** (contas, tarefas agendadas, serviços, chaves de registro, arquivos de teste, regras de *firewall*) e entrega um **inventário de artefatos**, marcados com o código do exercício (na Tatame, `RT-APR2291`), ao Blue Team, que confere cada item com uma varredura própria. Nenhum registro de auditoria é apagado. Se o Blue Team encontrar um artefato que não consta do inventário, ele deixa de ser assunto do exercício e passa a ser tratado como suspeita de incidente real. As credenciais usadas também são trocadas ao final.

#### O relatório de Red Team

O relatório serve a dois públicos. Uma estrutura comum inclui **sumário executivo**, com resultado e riscos em linguagem de negócio; **narrativa do ataque**, com a linha do tempo de cada etapa; **achados**, com evidências, severidade e técnica ATT&CK; **análise de detecção e resposta**, com o que foi visto, quando e o que passou despercebido; a situação da **limpeza**; e **recomendações priorizadas**. A linha do tempo permite ao Blue Team comparar, minuto a minuto, o que o Red Team fez com o que os registros mostram.

[Imagem 4 — Capa estilizada de relatório técnico com seções numeradas e uma linha do tempo com marcos verdes e vermelhos. Texto alternativo: "Estrutura de um relatório de Red Team com linha do tempo de técnicas detectadas e não detectadas". Sugestão de busca no Envato: "report timeline infographic".]

#### Exemplo numérico: a fase de evasão da Rede Tatame

Na tarde de 25/11/2026, o Red Team emulou seis técnicas de evasão. Duas viraram alerta em tempo real: a tentativa de parar o EDR do `SRV-ARQ-01`, barrada pela proteção contra adulteração, e a limpeza do log de Segurança, vista pelo evento 1102 no SIEM. A taxa de detecção foi de 2 ÷ 6 ≈ **33%**. No `SRV-ERP-01`, sem proteção contra adulteração, o agente ficou parado das 14h48 às 15h26: uma lacuna de **38 minutos**. Uma regra "agente sem *heartbeat* por mais de 10 minutos" teria disparado às 14h58, reduzindo o tempo cego em 28 ÷ 38 ≈ **74%**. Na limpeza, dos 12 artefatos inventariados, o Blue Team conferiu 11 (11 ÷ 12 ≈ **92%**); a conta local `tst.local01` continuava no `SRV-ERP-01` e voltou para o Red Team remover.

#### O que você verá na próxima unidade

Na Unidade 3 — Defesa, Monitoramento e Detecção, trocamos de lado. Os rastros desta unidade, da varredura no WAF ao log apagado e ao agente em silêncio, viram matéria-prima da defesa. Você vai estudar a arquitetura de monitoramento, com logs, SIEM e telemetria de *endpoints* (Aula 9); a detecção baseada em assinaturas, comportamento e regras (Aula 10); a caça a ameaças com hipóteses, consultas e análise de anomalias (Aula 11); e o *hardening* de sistemas e a redução da superfície de ataque (Aula 12).

#### Pontos-chave

- A evasão de defesas ocupa hoje duas táticas do ATT&CK: Furtividade (TA0005) e Enfraquecimento de defesas (TA0112).
- Cada técnica deixa rastro próprio: eventos 1102 e 104, 7036 e 7040, Sysmon 2 e 23 e a ausência de *heartbeat*.
- Logs encaminhados na hora e proteção contra adulteração do EDR tornam a evasão cara e visível.
- Limpeza legítima é remover os próprios artefatos e provar a remoção; o relatório mostra também o que a defesa não viu.

### Referências da aula

MICROSOFT. *Sysmon v15*. In: Microsoft Learn: Sysinternals. Disponível em: <https://learn.microsoft.com/sysinternals/downloads/sysmon>. Acesso em: 22 nov. 2026.

MITRE. *Defense impairment (TA0112)*. In: MITRE ATT&CK. Disponível em: <https://attack.mitre.org/tactics/TA0112/>. Acesso em: 22 nov. 2026.

MITRE. *Stealth (TA0005)*. In: MITRE ATT&CK. Disponível em: <https://attack.mitre.org/tactics/TA0005/>. Acesso em: 22 nov. 2026.

MITRE. *Indicator removal (T1070)*. In: MITRE ATT&CK. Disponível em: <https://attack.mitre.org/techniques/T1070/>. Acesso em: 22 nov. 2026.

SANTOS, Joas Antonio dos. *Introdução ao Red Team Operations 2.0*: um guia básico para suas operações de Red Team. Rio de Janeiro: Brasport, 2024.

WEIDMAN, Georgia. *Testes de invasão*: uma introdução prática ao hacking. São Paulo: Novatec, 2014.

### Roteiro da Videoaula 8 — "38 minutos de silêncio: o que o adversário apaga e o que fica"

Duração-alvo: 15 a 20 minutos. Deck: unidade_2/slides/aula8.html (21 slides).

**Slides 1 e 2 — Capa e sumário (0:00–0:30)**
Fala: "Olá! Esta é a Aula 8, a última da Unidade 2. Hoje vamos ver como um adversário tenta se esconder e apagar os próprios rastros, e como o defensor enxerga cada uma dessas tentativas. No fim, vamos fechar o exercício da Rede Tatame do jeito certo: com a limpeza comprovada e o relatório."
[Câmera: professor em plano médio.]

**Slide 3 — O problema de hoje na Rede Tatame (0:30–1:45)**
Fala: "Estamos no último dia útil do exercício autorizado, 25 de novembro. O Red Team de Bruno Sato emulou a fase de evasão do Grupo Cobalto Austral, como previam as regras de engajamento. Na revisão, Luiza Ferraz, do SOC, encontrou duas coisas estranhas: o agente EDR do `SRV-ERP-01` ficou calado das 14h48 às 15h26, e o log de Segurança do `SRV-ARQ-01` foi apagado às 14h10. No mapa, os dois servidores da sede aparecem destacados, junto com o console do EDR e o SIEM. A pergunta da aula está no quadro amarelo: como o Blue Team enxerga um adversário que tenta se esconder, e como o Red Team encerra o exercício com o ambiente limpo e comprovado?"
[Take de apoio: sala de monitoramento com telas escuras e uma tela sem sinal — Envato, "security operations center screens".]

**Slide 4 — Evasão de defesas: continuar no ambiente sem ser visto (1:45–2:45)**
Fala: "No ATT&CK atual, a evasão de defesas ocupa duas táticas. A Furtividade, TA0005, reúne o que o adversário faz para se esconder: apagar arquivos, alterar datas, disfarçar um programa com o nome de outro. O Enfraquecimento de defesas, TA0112, reúne o que ele faz para cegar os controles: parar o agente EDR, a técnica T1685, desativar o log do Windows, T1685.001, ou apagar logs já gravados, T1685.005. Se você ler um material anterior a 2026, vai encontrar tudo isso sob o nome *Defense Evasion*, TA0005, e a técnica T1562 para os controles desligados."
Atenção: os IDs estão no slide; leia só as duas táticas e a técnica T1685, para não transformar o slide numa lista falada.

**Slide 5 — Laboratório: onde o rastro sobrevive (2:45–5:00)**
Objetivo: mostrar, técnica por técnica, o que a evasão apaga e o que ela deixa para o defensor.
Na tela:
1. Ler o primeiro passo, "Antes · Cada evento sai da máquina em segundos", que já abre na tela.
2. Clicar em "▶ Avançar" para "14h02 · Tentar parar o EDR no SRV-ARQ-01 (T1685)".
3. "▶ Avançar" para "14h10 · Limpar o log de Segurança (T1685.005)".
4. "▶ Avançar" para "E se o log não saísse da máquina?".
5. "▶ Avançar" para "14h48 · Parar o EDR no SRV-ERP-01 (T1685)".
6. "▶ Avançar" para "15h05 e 15h20 · Data alterada e arquivo apagado (T1070.006, T1070.004)".
7. "▶ Avançar" para o último passo, "15h26 · Fim da janela: o Red Team religa o agente".
Fala: "No primeiro passo, repare nas setas azuis: cada servidor manda os eventos para o encaminhador, o agente do Wazuh, que os entrega ao SIEM em segundos. E o agente EDR manda um sinal de vida, o *heartbeat*, ao console. Às 14h02, a tentativa de parar o EDR no `SRV-ARQ-01` esbarra na proteção contra adulteração, e a seta verde mostra o aviso chegando à Luiza. Às 14h10, o log local é apagado, mas veja a seta azul: o encaminhador já tinha enviado tudo, e o próprio ato de apagar gera o evento 1102. No passo seguinte, o cenário contrário: sem encaminhamento, a linha tracejada leva à caixa 'Evidência perdida'. Às 14h48, no `SRV-ERP-01`, a proteção estava desligada por uma exceção antiga, e o console do EDR fica vermelho: acabou o *heartbeat*. As setas âmbar mostram que os eventos 7040 e 7036 continuam chegando ao SIEM, mas sem regra. O mesmo vale para a data alterada e o arquivo apagado. No último passo, o balanço: dois alertas, quatro rastros sem alerta e 38 minutos sem EDR."
Atenção: o botão "⏯ Auto" toca a sequência sozinho; para gravar, use "▶ Avançar" e espere a animação de cerca de dois segundos em cada passo.
Conclusão: "A evasão tira cópias e sinais de vida, mas não alcança o que já saiu da máquina."
[Tela: gravação do laboratório do slide 5.]

**Slide 6 — Toda técnica de evasão deixa um rastro próprio (5:00–5:50)**
Fala: "Esta tabela é a cola do defensor. Log apagado gera o 1102, ou o 104 quando é outro log. EDR parado gera ausência de *heartbeat* e, no log de Sistema, o 7036 e o 7040. Serviço novo gera o 7045. O Sysmon, ferramenta gratuita da Microsoft, mostra a data de criação alterada no evento 2, o arquivo apagado no 23 e no 26 e o `svchost.exe` fora da pasta System32. O quadro azul resume as duas defesas que tornam tudo isso caro: encaminhar os logs na hora e ligar a proteção contra adulteração."

**Slide 7 — Laboratório: a caça aos rastros no Wazuh (5:50–8:20)**
Objetivo: encontrar no SIEM o rastro de cada técnica de evasão do exercício.
Na tela:
1. Ao abrir o slide, a busca "1. Log de auditoria apagado (1102)" já roda sozinha; ler o resultado.
2. Clicar em "2. Agente EDR sem heartbeat".
3. Clicar em "3. Serviço de segurança parado (7036)".
4. Clicar em "4. Data de criação alterada (Sysmon 2)".
5. Clicar em "5. SRV-ERP-01, 14h40 – 15h30".
Fala: "Este console imita o Wazuh, o SIEM de código aberto que vamos estudar na Unidade 3. A consulta, no alto, está em DQL e filtra pelo canal e pelo número do evento. A busca 1 devolve um único evento: 1102, às 14h10, no `SRV-ARQ-01`, com a conta que fez a limpeza e nível alto. Esta tinha regra e virou alerta. A busca 2 lista as lacunas de *heartbeat*: o `NB-FIN-031` ficou 55 minutos fora, mas a coluna 'explicação' mostra um reinício planejado, o evento 1074; o `SRV-ERP-01` ficou 38 minutos fora sem explicação. A busca 3 mostra o 7040, alguém mudando o início do agente para desabilitado, o 7036 do agente parado e, às 15h26, o 7036 dele voltando. A busca 4 é ruidosa: instaladores mudam datas o tempo todo, como o `msiexec.exe` da primeira linha. O que destoa é a segunda: um programa da pasta pública recuando para 2024 a data de um arquivo criado hoje. A busca 5 junta tudo numa linha do tempo, e a coluna 'alerta?' diz 'não' quatro vezes."
Atenção: os dados são fictícios e o Wazuh é simulado; a nota escura abaixo de cada tabela resume a leitura e pode ser lida em voz alta.
Conclusão: "Os rastros estavam no SIEM o tempo todo. Só dois tinham regra."
[Tela: gravação do laboratório do slide 7.]

**Slide 8 — Laboratório: sem o EDR, o SOC fica cego (8:20–10:20)**
Objetivo: medir, na plataforma, o que deixa de ser visto quando o agente EDR para.
Na tela:
1. A plataforma abre na aba *Telemetria*, já reiniciada. Desmarcar "EDR dos notebooks e servidores".
2. No topo, trocar a velocidade para "1 s = 1 min".
3. Abrir *Cenários* e, no cartão "Emulação do Grupo Cobalto Austral", clicar em "Iniciar cenário". Esperar o último passo, cerca de 15 segundos.
4. Ler os indicadores abaixo da linha do tempo: 1 detectado, 4 não detectados, 3 vistos sem alerta.
5. Voltar a *Telemetria* e marcar de novo "EDR dos notebooks e servidores".
6. Em *Cenários*, clicar em "Repetir com as fontes e regras atuais" e esperar o fim.
Fala: "Desmarcar a fonte EDR é a forma de simular, na plataforma, a técnica T1685: o agente parou. Na primeira rodada, olhe os ícones. O login na VPN é detectado pela R11, que usa a auditoria de identidade. Mas a leitura da memória do LSASS e a exclusão das cópias de sombra aparecem com o X vermelho, 'não detectado', porque as regras R6 e R7 dependem do EDR. O último passo é o impacto consumado. Agora religo o EDR e repito com as mesmas regras. As duas linhas viram 'detectado', e o contador passa para 3 detectados e 2 não detectados."
Atenção: não use o botão "Reiniciar" do topo entre as duas rodadas, porque ele volta as fontes ao padrão. Os alertas levam alguns segundos para aparecer depois do passo; espere o ícone mudar da lupa para ✅. Se o SOC mostrar um alerta da R11 sobre a conta `svc-backup`, ele é benigno e não faz parte do cenário.
Conclusão: "Com o agente parado, o que vem depois deixa de ser visto. Por isso a ausência de *heartbeat* precisa virar alerta."
[Tela: gravação do laboratório do slide 8.]

**Slide 9 — O que vale em evasão num exercício autorizado (10:20–11:00)**
Fala: "Tudo isso aconteceu num exercício, então tinha regras. A evasão só entra para medir a detecção, técnica por técnica, combinada com o White Team, que controla o exercício. Na Tatame, a carta assinada por Marina Prado permitia parar o EDR em dois servidores por até 40 minutos, e o Red Team religou às 15h26. O log só podia ser limpo depois de confirmado o encaminhamento ao SIEM. E a palavra 'LARANJA' interrompe tudo se houver risco real. O quadro azul traz o ponto central: no fim do exercício, limpar rastros quer dizer remover o que o Red Team criou; nenhum registro de auditoria é apagado."

**Slide 10 — Antes do código: onde achar e como instalar (11:00–11:25)**
Fala: "Para o próximo laboratório, você precisa do VS Code com a extensão Python da Microsoft e do Python 3.12, baixado de python.org. O script usa só os módulos `csv` e `json`, que já vêm com o Python. Se algum tutorial mandar instalar 'csv' pelo `pip`, desconfie: pacote com nome de módulo padrão é golpe conhecido."

**Slide 11 — Laboratório: lacunas de telemetria e sinais de evasão (11:25–13:45)**
Objetivo: achar, com um script de caça, o silêncio do EDR e os sinais de evasão que nenhuma regra mostrou.
Na tela:
1. O VS Code ocupa o slide inteiro, como no meu computador. O roteiro do laboratório abre com a tecla G ou com o botão "☰ Roteiro", na barra de status; deixar fechado durante a gravação.
2. Clicar em "⬇ Preparar o ambiente" e esperar o botão mudar para "✓ Ambiente pronto".
3. No explorador, abrir `sessoes_edr.csv` e depois `eventos.jsonl`.
4. Voltar a `lacunas.py` e mostrar as linhas destacadas.
5. Clicar em "▶ Procurar lacunas".
Fala: "A preparação roda quatro comandos: a versão do Python, a criação do ambiente virtual `.venv`, a ativação, que põe `(.venv)` no início do *prompt*, e o `pip list`, que mostra só o `pip`, porque não há o que instalar. O `sessoes_edr.csv` é a exportação do console do EDR: cada linha é um período em que o agente esteve conectado. Repare que o `SRV-ERP-01` tem duas linhas, uma até 14h48 e outra a partir de 15h26. O `eventos.jsonl` traz os eventos que o Wazuh recebeu, um por linha. No script, o dicionário `SINAIS` liga cada canal e número de evento a uma técnica. O primeiro laço compara o fim de uma sessão com o início da seguinte; a linha que decide é a do `gap`. Se a lacuna passa de 10 minutos, o script procura um evento 1074, de reinício planejado, até cinco minutos antes. O segundo laço marca os eventos da tabela e um caso especial: `svchost.exe` fora da System32, a técnica T1036.005. Na saída, leia de cima para baixo: o notebook do financeiro tem lacuna explicada; o `SRV-ERP-01` tem 38 minutos sem explicação. Depois vêm oito sinais, em dois servidores; os amarelos são os que nenhuma regra transformou em alerta. A última linha, das 15h26, é o agente voltando, o que fecha a lacuna."
Atenção: a preparação do ambiente é simulada e leva cerca de 10 segundos. O botão "⌨ Digitar ao vivo" redigita o arquivo aberto, se quiser mostrar o código sendo escrito.
Conclusão: "A lacuna sem explicação é o achado que nenhuma regra mostrou, e ela vira regra na Unidade 3."
[Tela: gravação do laboratório do slide 11.]

**Slide 12 — Limpeza legítima: remover o que criou e provar que removeu (13:45–14:25)**
Fala: "Agora, o outro sentido de limpar rastros. Durante toda a operação, o Red Team mantém um inventário de cada conta, tarefa, serviço, chave de registro e arquivo que criou, todos marcados com o código do exercício, `RT-APR2291`. No fim da janela, remove tudo e registra como. O Blue Team confere item a item com uma varredura própria, e o White Team só fecha o exercício quando as pendências zeram e as credenciais usadas foram trocadas. Repare na frase de baixo: se aparecer um artefato fora do inventário, ele deixa de ser assunto do exercício e vira suspeita de incidente real."

**Slide 13 — O relatório de Red Team serve a dois públicos (14:25–14:55)**
Fala: "O relatório tem seis partes: sumário executivo para a diretoria, narrativa do ataque da Aula 5 à Aula 8, achados com a técnica ATT&CK, a análise do que foi e do que não foi detectado, a situação da limpeza e as recomendações com dono. A linha do tempo é o que permite ao Blue Team comparar, minuto a minuto, o ataque com os registros."

**Slide 14 — Antes do código: o que falta instalar para gerar o relatório (14:55–15:15)**
Fala: "O segundo laboratório lê um arquivo YAML, então precisa do pacote PyYAML. Atenção: no código está escrito `import yaml`, mas o pacote se chama PyYAML, e quem confirma isso é a documentação do projeto. A versão fica fixada no `requirements.txt` com dois sinais de igual."

**Slide 15 — Laboratório: relatório da evasão e conferência da limpeza (15:15–17:05)**
Objetivo: gerar a seção de evasão e limpeza do relatório a partir do registro da operação.
Na tela:
1. Clicar em "⬇ Preparar o ambiente" e esperar "✓ Ambiente pronto".
2. Com o `operacao.yaml` aberto, mostrar as linhas destacadas.
3. Abrir `gerar_relatorio.py`.
4. Clicar em "▶ Gerar relatório"; ao terminar, o editor abre o `relatorio.md`.
Fala: "Desta vez a preparação instala de verdade um pacote: o `pip` baixa o PyYAML 6.0.3 e o `pip list` confirma. O `operacao.yaml` tem duas listas. Em `evasao`, as seis técnicas da tarde, cada uma com hora, ID, nome e se foi detectada; a linha destacada é a parada do EDR no `SRV-ERP-01`, com `detectada: false`. Em `artefatos`, os 12 itens do inventário; a linha destacada é a conta `tst.local01`, removida segundo o Red Team, mas com `conferido: false`. No script, três linhas fazem o trabalho: `detectadas` filtra as técnicas vistas, `taxa` divide pelo total e `pendentes` separa os artefatos que não foram removidos e conferidos. Na saída: seis técnicas, duas detectadas, 33%; as quatro lacunas em vermelho; 11 de 12 artefatos conferidos; e a pendência da conta `tst.local01`, que volta ao White Team. O `relatorio.md` traz a mesma informação em tabela, pronta para o documento final."
Atenção: o relatório gerado é o rascunho de uma seção; o documento completo da operação junta as quatro aulas da unidade.
Conclusão: "O exercício só termina quando a pendência zera, e o relatório já mostra o que a defesa não viu."
[Tela: gravação do laboratório do slide 15.]

**Slide 16 — Exemplo numérico (17:05–17:35)**
Fala: "Os números da tarde: 15h26 menos 14h48 dá 38 minutos de lacuna. Com uma regra de 10 minutos sem *heartbeat*, o alerta sairia às 14h58, e o tempo cego cairia 28 de 38 minutos, cerca de 74%. A detecção da evasão foi de 2 em 6, 33%. E a limpeza conferida, 11 de 12, cerca de 92%."

**Slide 17 — O que você verá na próxima unidade (17:35–18:05)**
Fala: "Na Unidade 3, trocamos a camisa vermelha pela azul. Cada rastro desta unidade vira matéria-prima da defesa. Começamos pela arquitetura de monitoramento, com logs, SIEM e telemetria de *endpoints*; depois, a detecção por assinaturas, comportamento e regras; a caça a ameaças; e o *hardening* para reduzir a superfície de ataque."
[Take de apoio: analista diante de painéis de monitoramento — Envato, "cyber security analyst dashboard".]

**Slide 18 — De volta ao problema (18:05–18:45)**
Fala: "Voltemos à pergunta. O fluxo e o Wazuh mostraram que o 1102, o 7036 e o Sysmon 2 chegaram ao SIEM, porque os logs saem da máquina na hora. A plataforma e o script mostraram o que some sem o EDR e acharam os 38 minutos sem explicação. O relatório conferiu 11 dos 12 artefatos. A resposta, então: o Blue Team enxerga a evasão pelo rastro que ela mesma gera, desde que os logs sejam encaminhados e alguém procure o silêncio; e o Red Team encerra o exercício removendo o que criou e entregando o inventário para conferência, sem apagar nenhum registro."

**Slides 19 a 21 — Pontos-chave, referências e encerramento (18:45–19:15)**
Fala: "Fechamos aqui a Unidade 2 e a parte ofensiva da disciplina. Na próxima aula, a Aula 9, começamos a montar a arquitetura de monitoramento da Rede Tatame. Até lá!"
[Slides: pontos-chave e referências ficam disponíveis no material.]

## Quiz não avaliativo

### Questão 1 (verdadeiro ou falso)

Uma vulnerabilidade com nota CVSS 9,8 deve sempre ser testada e corrigida antes de uma vulnerabilidade com nota CVSS 7,5, pois a nota CVSS expressa o risco que cada falha representa para a organização.

( ) Verdadeiro  
(X) Falso

### Questão 2 (múltipla escolha)

Durante um exercício autorizado, o SIEM recebe, às 14h05, um evento 1102 do log de Segurança do servidor SRV-ARQ-01. Até as 14h04, o servidor enviava eventos normalmente. O que esse registro indica e por que o SOC ainda consegue vê-lo?

a) Indica uma falha de disco, e o SOC só o vê porque o servidor foi reiniciado.  
b) Indica um *login* bem-sucedido de administrador, registrado normalmente pelo Windows.  
*c) Indica que o log de auditoria foi apagado (técnica T1685.005, *Clear Windows Event Logs*), e o SOC o vê porque os eventos já tinham sido encaminhados para fora da máquina.  
d) Indica que o antivírus foi atualizado, e o SOC o vê porque o EDR gera o evento 1102 a cada atualização.

### Feedback

**Questão 1 — Falso.** A nota-base do CVSS mede a severidade técnica da falha, e não o risco. A priorização por risco também considera a probabilidade de exploração (EPSS), a exploração confirmada (catálogo KEV da CISA) e a exposição e a criticidade do ativo. Uma falha 7,5 em um portal exposto à internet, presente no KEV e com EPSS alto, pode ser muito mais urgente do que uma falha 9,8 em um servidor interno isolado.

**Questão 2 — Alternativa c.** O evento 1102 ("*The audit log was cleared*") é gerado pelo próprio Windows quando alguém apaga o log de Segurança, técnica que, desde a versão 19 do ATT&CK (abril de 2026), fica na tática Enfraquecimento de defesas (*Defense Impairment*, TA0112) como T1685.005; materiais anteriores a classificam como T1070.001, na antiga *Defense Evasion*. Apagar o log local não apaga o que já foi encaminhado ao SIEM, por isso o encaminhamento dos registros para fora da máquina é uma das defesas mais simples contra essa técnica. As demais alternativas atribuem ao evento significados que ele não tem.

## Material complementar

### Direto da fonte (livro da Biblioteca Virtual)

- **Texto provocativo:** Por que um invasor gastaria semanas procurando uma falha técnica se pode simplesmente pedir a senha a alguém? Escrito por profissionais brasileiros de segurança ofensiva, o capítulo indicado mostra como pretexto, urgência e autoridade são explorados em ataques de engenharia social, e como um *red team* autorizado reproduz essas técnicas de forma ética para medir a resiliência das pessoas e dos processos. É leitura essencial para entender o *phishing* como vetor de acesso inicial e planejar simulações com responsabilidade.
- **Nome do livro:** SOARES, Cleber; FRANCO, Deivison Pinheiro; SANTOS, Joas Antonio dos. *Introdução à segurança ofensiva*: uma abordagem para pentesters e red teams. Rio de Janeiro: Brasport, 2023. *E-book*.
- **Capítulo:** 3 — Técnicas de engenharia social
- **Link de acesso:** <https://plataforma.bvirtual.com.br/Acervo/Publicacao/213767>
- **Aula em que entra:** Aula 6

### Para mergulhar no assunto (saiba mais)

- **Texto provocativo:** Em 2016, três pesquisadores subiram ao palco da DEF CON e mostraram que, em muitas empresas, o caminho de um usuário comum até o controle total do domínio é uma questão de teoria dos grafos. A palestra apresentou o BloodHound e mudou a forma como Red Teams e Blue Teams enxergam o Active Directory. Assista e pense: quantos caminhos desses existem na rede em que você trabalha?
- **Indicação:** ROBBINS, Andy; VAZARKAR, Rohan; SCHROEDER, Will. *Six degrees of domain admin*: using graph theory to accelerate red team operations. Palestra apresentada na DEF CON 24, Las Vegas, 6 ago. 2016. Vídeo gratuito no canal oficial da DEF CON no YouTube: <https://www.youtube.com/watch?v=wP8ZCczC1OU>.
- **Links complementares:** guia de referência do Nmap, do próprio projeto — <https://nmap.org/book/man.html> (Aula 5); catálogo KEV da CISA — <https://www.cisa.gov/known-exploited-vulnerabilities-catalog> (Aula 6); táticas Furtividade (*Stealth*, TA0005) e Enfraquecimento de defesas (*Defense Impairment*, TA0112) no MITRE ATT&CK, que substituíram a antiga *Defense Evasion* na versão 19 — <https://attack.mitre.org/tactics/TA0005/> e <https://attack.mitre.org/tactics/TA0112/> (Aula 8).
- **Aula em que entra:** Aula 7 (links complementares: Aulas 5, 6 e 8)

### Podcast (curadoria, até 45 min)

- **Texto provocativo:** Se uma voz idêntica à do seu diretor ligasse pedindo um Pix urgente, você desconfiaria? Neste episódio de cerca de 20 minutos, o pesquisador Daniel Barbosa, da ESET Brasil, mostra como a inteligência artificial tornou a engenharia social mais convincente, com vozes e vídeos falsos, e por que urgência e autoridade continuam sendo os gatilhos centrais dos golpes. Ouça pensando no *phishing* como vetor de acesso inicial da Aula 6: quais pistas ainda funcionam quando a isca é quase perfeita?
- **Nome do podcast:** Podcast Canaltech
- **Nome do episódio:** Golpes com IA e fraudes no Pix: como funcionam os crimes digitais em 2026 (7 jan. 2026)
- **Link:** <https://canaltech.com.br/podcast/podcast-canaltech/golpes-com-ia-e-fraudes-no-pix-como-funcionam-os-crimes-digitais-em-2026-6287/> (também no Spotify, Apple Podcasts e Deezer)
- **Aula em que entra:** Aula 6

### Artigo científico

- **Texto provocativo:** Se a sua simulação de *phishing* teve 2% de cliques, isso é uma boa notícia ou apenas sinal de que a isca era fácil demais? Pesquisadoras do NIST propõem um método para classificar a dificuldade de uma mensagem de *phishing* a partir das pistas que ela contém e do quanto o pretexto se encaixa na rotina do público. O artigo ajuda a interpretar com mais honestidade o resultado de um teste de acesso inicial por engenharia social.
- **Link:** <https://academic.oup.com/cybersecurity/article/6/1/tyaa009/5905453> (acesso aberto; DOI: <https://doi.org/10.1093/cybsec/tyaa009>)
- **Aula em que entra:** Aula 6
- **Referência ABNT:** STEVES, Michelle; GREENE, Kristen; THEOFANOS, Mary. Categorizing human phishing difficulty: a Phish Scale. *Journal of Cybersecurity*, v. 6, n. 1, tyaa009, 2020. DOI: 10.1093/cybsec/tyaa009.
