# Unidade 2 — Red Team: operações ofensivas controladas

Disciplina: Red Team & Blue Team Strategies  
Professor-conteudista: Afonso Cesar Lelis Brandão  
Prazo de entrega: 02/12/2026  
Template de origem: `documentos/Unidade 2/TEMPLATE - Unidade 2_nome da disciplina.docx`

> Versão de trabalho baseada na **ementa proposta** (`EMENTA.md`); ajustar quando o plano de aprendizagem oficial chegar.
> Recursos visuais indicados entre colchetes, como pede o template; a equipe de produção substitui pelas imagens finais.

## Aula 5 — Reconhecimento e OSINT

### O que você verá nesta unidade

Nesta unidade, você vai vestir a camisa vermelha — sempre dentro de um engajamento autorizado. Vamos percorrer, em nível conceitual, as etapas de uma operação ofensiva controlada: o reconhecimento e a inteligência de fontes abertas (OSINT), que revelam o que a organização expõe sem perceber; a varredura, a enumeração e a gestão de vulnerabilidades, com a priorização por risco usando CVSS, EPSS e o catálogo KEV; a engenharia social e as simulações de *phishing* voltadas à conscientização; e a pós-exploração, a movimentação lateral e o relatório de Red Team. O objetivo é que você compreenda como um adversário avança e, principalmente, que rastro cada passo deixa para o Blue Team. A justificativa é simples: ninguém detecta bem aquilo que não entende, e é o Red Team que transforma a ameaça abstrata em evidência concreta para a defesa.

### Texto base

Antes de enviar um único pacote para a rede de uma empresa, um adversário competente já sabe muito sobre ela: quais domínios possui, quais tecnologias usa, quem trabalha no financeiro, qual é o formato dos endereços de *e-mail* e quais serviços estão expostos na internet. Essa fase é o **reconhecimento**, a primeira etapa da Cyber Kill Chain e a tática TA0043 (*Reconnaissance*) da matriz MITRE ATT&CK, estudadas na Unidade 1. Em uma operação de Red Team, ela define o caminho de todo o restante do trabalho.

#### Reconhecimento passivo e ativo

O reconhecimento pode ser **passivo** ou **ativo**. No passivo, a equipe consulta apenas fontes de terceiros — buscadores, registros públicos, redes sociais, bases de certificados — sem interagir diretamente com os sistemas do alvo. No ativo, há interação: consultas aos servidores DNS da empresa, visitas ao *site*, varreduras de portas (técnica T1595 — *Active Scanning*). A diferença é importante por dois motivos. O primeiro é jurídico: o reconhecimento ativo toca ativos que precisam estar no escopo autorizado. O segundo é defensivo: o passivo praticamente não deixa rastro no ambiente do alvo, enquanto o ativo pode ser registrado.

[Imagem 1 — Ilustração de uma lupa sobre um mapa de rede com ícones de domínios, pessoas e servidores. Texto alternativo: "Lupa sobre um mapa com domínios, pessoas e servidores de uma empresa, representando o reconhecimento". Sugestão de busca no Envato: "magnifying glass network map cyber".]

#### OSINT: a inteligência que está à vista de todos

**OSINT** (*Open Source Intelligence*) é a coleta e a análise de informações disponíveis publicamente para produzir conhecimento útil. Para um Red Team, as principais fontes são:

| Fonte | O que revela | Exemplo de ferramenta ou serviço | Técnica ATT&CK relacionada |
|---|---|---|---|
| DNS e registros de domínio | Subdomínios, servidores de *e-mail*, provedores | Consultas WHOIS e DNS | T1596 — *Search Open Technical Databases* |
| Transparência de certificados | Subdomínios que receberam certificados TLS | crt.sh | T1596 |
| Buscadores de dispositivos | Serviços e versões expostos na internet | Shodan, Censys | T1596 |
| *Sites* e redes sociais | Organograma, cargos, tecnologias citadas em vagas | LinkedIn, *site* institucional | T1593 — *Search Open Websites/Domains*; T1591 — *Gather Victim Org Information* |
| Endereços de *e-mail* e nomes | Padrão de *e-mail*, alvos para engenharia social | theHarvester | T1589 — *Gather Victim Identity Information* |
| Repositórios de código | Configurações, nomes de servidores, segredos esquecidos | Buscas em repositórios públicos | T1593 |

Ferramentas como o **Maltego** ajudam a relacionar essas informações em grafos, mostrando, por exemplo, que um subdomínio esquecido aponta para um servidor de homologação mantido por um fornecedor.

[Imagem 2 — Grafo de relacionamento com o domínio da empresa no centro, ligado a subdomínios, endereços IP, pessoas e tecnologias. Texto alternativo: "Grafo de OSINT ligando domínio, subdomínios, IPs, funcionários e tecnologias". Sugestão de busca no Envato: "link analysis graph network nodes".]

#### Superfície de ataque e *shadow IT*

O produto do reconhecimento é um retrato da **superfície de ataque externa**: tudo o que um adversário poderia tentar atingir. É comum que esse retrato revele ativos que a própria área de TI desconhece — um painel de administração publicado por uma agência de *marketing*, um ambiente de testes antigo em nuvem, um serviço de acesso remoto sem segundo fator. Esse fenômeno é chamado de *shadow IT*, e encontrá-lo é, muitas vezes, o resultado mais valioso da fase de reconhecimento. Lembre-se da função Identificar do NIST CSF 2.0: não se protege nem se monitora um ativo que ninguém sabe que existe.

#### Limites éticos e legais do OSINT

"Informação pública" não significa "informação sem regras". Mesmo em um engajamento autorizado, as regras de engajamento devem dizer se a equipe pode coletar dados de perfis pessoais de funcionários, até que ponto e como esses dados serão protegidos e descartados. Nomes, cargos e *e-mails* são dados pessoais e estão sujeitos à LGPD. Também é preciso cuidado com bases de vazamentos: consultar se credenciais corporativas aparecem em vazamentos conhecidos pode ser útil para medir risco, mas usar senhas vazadas para acessar sistemas só é aceitável se estiver explicitamente previsto no escopo. E acessar sistemas fora do escopo — por exemplo, o servidor de um fornecedor encontrado no reconhecimento — pode configurar o crime do art. 154-A do Código Penal.

#### Que rastro isso deixa para o Blue Team?

O reconhecimento passivo quase não deixa rastros no ambiente do alvo, e por isso a defesa aqui é sobretudo **preventiva**: reduzir o que se expõe. O ativo, por sua vez, aparece em registros de *firewall*, de servidores *web* e de DNS — muitas requisições sequenciais, varreduras de portas, consultas a subdomínios inexistentes. Um Blue Team maduro também faz o próprio "reconhecimento defensivo", monitorando continuamente sua superfície de ataque externa e verificando se surgem novos certificados com o nome da empresa.

[Imagem 3 — Painel de monitoramento com um alerta de varredura de portas vinda de um endereço externo. Texto alternativo: "Tela de monitoramento de segurança exibindo alerta de varredura de portas". Sugestão de busca no Envato: "security dashboard alert port scan".]

#### Exemplo numérico: quanto a empresa expõe sem saber

Em um engajamento autorizado, o Red Team identifica 180 subdomínios na transparência de certificados de uma empresa. Destes, 120 ainda respondem na internet. Ao comparar com o inventário oficial, a equipe constata que 15 não constavam em nenhum registro da TI. A taxa de ativos desconhecidos é de 15 ÷ 120 = **12,5%** da superfície ativa. Além disso, a empresa tem 400 funcionários, e a equipe encontrou 260 endereços de *e-mail* válidos em fontes públicas, ou seja, 260 ÷ 400 = **65%** do quadro já está exposto como possível alvo de *phishing*. Esses dois números orientam recomendações concretas: atualizar o inventário de ativos e priorizar o treinamento de quem está mais exposto.

#### Pontos-chave

- O reconhecimento (TA0043) define o caminho de toda a operação ofensiva.
- O reconhecimento passivo quase não deixa rastro; o ativo pode ser registrado e precisa estar no escopo.
- OSINT revela a superfície de ataque externa, incluindo ativos de *shadow IT*.
- Dados de funcionários são dados pessoais: LGPD e regras de engajamento se aplicam também ao OSINT.

### Referências da aula

BRASIL. Lei nº 13.709, de 14 de agosto de 2018. Lei Geral de Proteção de Dados Pessoais (LGPD). *Diário Oficial da União*, Brasília, DF, 15 ago. 2018.

MITRE. *Reconnaissance (TA0043)*. In: MITRE ATT&CK. Disponível em: <https://attack.mitre.org/tactics/TA0043/>. Acesso em: 13 nov. 2026.

NATIONAL INSTITUTE OF STANDARDS AND TECHNOLOGY. *SP 800-115: technical guide to information security testing and assessment*. Gaithersburg: NIST, 2008.

OWASP FOUNDATION. *OWASP web security testing guide*. Versão 4.2. 2020. Disponível em: <https://owasp.org/www-project-web-security-testing-guide/>. Acesso em: 13 nov. 2026.

### Roteiro da Videoaula 5 — "O que a Rede Tatame mostra para quem procura?"

Duração-alvo: 15 a 20 minutos. Deck: unidade_2/slides/aula5.html (24 slides).

**Slides 1 a 3 — Capa, audiodescrição e sumário (0:00–0:30)**
Fala: "Olá! Esta é a Aula 5, a primeira da Unidade 2, em que vestimos a camisa vermelha. Hoje vamos estudar o reconhecimento e a coleta de informações em fontes abertas, sempre sobre a Rede Tatame, a nossa rede fictícia de academias."
[Câmera: professor em plano médio. Slide da audiodescrição fica disponível no material e não precisa ser lido.]

**Slide 4 — O problema de hoje na Rede Tatame (0:30–2:00)**
Fala: "Comece pela história. Bruno Sato lidera o Red Team interno da Tatame, e a CISO Marina Prado autorizou um levantamento externo antes do exercício de *ransomware* do semestre. A reunião travou numa pergunta simples: quantos endereços da Tatame existem na internet? O inventário da TI lista 105, mas ninguém sabe se um adversário acharia outros. Repare no mapa à direita: a borda vista da internet, e em vermelho a homologação `hml-gestao`, que ninguém inventariou e que guarda uma cópia do banco de alunos, 30% deles menores. A pergunta que vamos responder até o fim da aula está no quadro amarelo: o que a Rede Tatame expõe na internet sem saber, e como descobrir isso antes do adversário?"
[Take de apoio: pessoa digitando em notebook com mapa de rede ao fundo — Envato, "network map laptop".]

**Slide 5 — O que você verá nesta unidade (2:00–2:40)**
Fala: "Esta tabela é o mapa da unidade. Cada aula responde a uma pergunta: o que a organização expõe, o que está vulnerável e o que corrigir primeiro, se as pessoas reconhecem a isca e até onde o adversário chegaria. Em todas elas, vamos perguntar também que rastro cada passo deixa para o Blue Team."

**Slide 6 — Antes do primeiro pacote, o adversário pesquisa (2:40–3:30)**
Fala: "Um adversário competente já sabe muito sobre a empresa antes de tocar a rede dela. Essa fase é o reconhecimento, a tática TA0043 do MITRE ATT&CK. A coleta em fontes abertas tem nome: OSINT, inteligência de fontes abertas. Pense no ladrão que observa a casa por dias. Olhar da calçada é reconhecimento passivo; tocar a campainha já é reconhecimento ativo."
[Take de apoio: rua residencial vista de longe, câmera de segurança no portão — Envato, "burglar watching house".]

**Slide 7 — Laboratório: o que a própria empresa publica (3:30–5:30)**
Objetivo: responder à primeira parte da pergunta, mostrando o que a própria Tatame publica, sem tocar a rede dela.
Na tela:
1. Na aba *Vaga de emprego*, clicar em "migração da VPN NetGuard 9.1 para a versão 10".
2. Clicar em "Active Directory em Windows Server 2012 R2", "ERP financeiro em servidor próprio da sede", "ambiente de homologação do portal das academias, criado em 2024" e "caio.mendes@tatame.com.br".
3. Clicar na aba *Perfil profissional* e nos trechos "Administrador de TI na Rede Tatame", "troca dos 120 notebooks da sede", "vpn.tatame.com.br", "O segundo fator ainda não chegou às contas da TI" e "foto da recepção com a tela da catraca facial".
4. Clicar na aba *Buscador de dispositivos* e nos três resultados: a VPN em 203.0.113.30, a `hml-gestao` em 203.0.113.45 e o `promo-hml` em 198.51.100.23.
5. Conferir o contador no canto superior direito: "13 de 13 pistas".
Fala: "Cada trecho amarelo, quando clicado, mostra na faixa escura de baixo o que ele revela. A vaga entrega o fabricante e a versão da VPN e o padrão de *e-mail* nome.sobrenome. O perfil de Caio Mendes confirma o endereço da VPN e admite que as contas da TI ainda entram sem segundo fator, a informação mais grave da página. O buscador de dispositivos confirma a mesma versão da VPN por um serviço público e mostra a `hml-gestao` sem WAF, o filtro de ataques da borda. Repare que nenhuma dessas consultas tocou a rede da Tatame."
Atenção: as páginas são fictícias e usam domínios example.com. O terceiro resultado do buscador é da agência de *marketing*: ele entra no relatório, mas não pode ser acessado.
Conclusão: "Sem enviar um pacote, o Red Team já tem alvo, versão e pessoa. Essa é a primeira parte do que a Tatame expõe sem saber."
[Tela: gravação do laboratório do slide 7.]

**Slide 8 — Reconhecimento passivo e reconhecimento ativo (5:30–6:10)**
Fala: "A tabela compara as duas formas. O passivo consulta só fontes de terceiros e quase não deixa rastro. O ativo interage com o alvo, por exemplo consultando o DNS da empresa, o serviço que traduz nomes em endereços IP, ou varrendo portas. Por isso ele precisa estar no escopo autorizado e pode aparecer nos registros de *firewall*, de servidores *web* e de DNS."

**Slide 9 — Laboratório: da calçada à campainha (6:10–7:40)**
Objetivo: ver quais consultas deixam rastro na Tatame e, portanto, o que o SOC tem chance de enxergar.
Na tela:
1. Clicar em *Avançar* no passo "Passivo · Transparência de certificados".
2. Avançar para "Passivo · Buscadores, redes sociais e WHOIS" e "Passivo · O que o SIEM viu até aqui".
3. Avançar para "Ativo · Consultas ao DNS da empresa" e "Ativo · Varredura de portas".
4. Avançar para o último passo, "Escopo · O servidor da agência".
Fala: "Nos dois primeiros passos, as setas vermelhas saem do Red Team e vão para serviços de terceiros: logs de certificados, buscadores e o registro do domínio. No terceiro passo, o nó SIEM fica sozinho, porque não viu nada. Nos passos ativos, a seta atravessa o DNS da Tatame ou a CDN e o WAF, e uma seta azul leva os registros até o SIEM. O DNS registra perguntas por nomes inexistentes, as respostas NXDOMAIN; a borda registra conexões sequenciais para muitas portas, a técnica T1595. No último passo, o servidor da agência fica em âmbar: interagir com ele seria reconhecimento ativo sobre um terceiro sem autorização."
Atenção: o botão *Auto* toca a sequência sozinho; para gravar, prefira *Avançar* e espere a animação dos pacotes, cerca de dois segundos por passo.
Conclusão: "O passivo não deixa rastro, então a defesa contra ele é reduzir o que se publica. O ativo deixa rastro, e é aí que o SOC pode agir."
[Tela: gravação do laboratório do slide 9.]

**Slide 10 — Fontes de OSINT e técnicas ATT&CK (7:40–8:20)**
Fala: "Aqui estão as fontes que usamos e as técnicas do ATT&CK correspondentes. O WHOIS é o registro público do dono do domínio. A transparência de certificados, ou CT, lista os certificados TLS, aqueles que habilitam o cadeado do HTTPS. Buscadores de dispositivos, redes sociais e repositórios de código completam o quadro. As técnicas T1596, T1593, T1591 e T1589 estão traduzidas no rodapé."

**Slide 11 — Laboratório: registro, DNS e transparência de certificados (8:20–10:20)**
Objetivo: listar todos os nomes da Tatame que existem na internet, inclusive os que a TI esqueceu.
Na tela:
1. Clicar em *Próximo comando*: consulta WHOIS de `tatame.com.br`.
2. *Próximo comando*: consulta DNS dos registros MX e TXT.
3. *Próximo comando*: consulta à base pública de certificados, que grava os nomes em `ct.txt` e conta as linhas.
4. *Próximo comando*: filtro dos nomes que contêm hml, teste, dev, old ou tmp.
5. *Próximo comando*: resolução de `hml-gestao` e `promo-hml`.
Fala: "O primeiro comando mostra o titular do domínio e o contato técnico, CAMEN7, que é Caio Mendes: a mesma pessoa da vaga e do perfil. O segundo mostra o servidor de *e-mail*, mx1, e os registros TXT: a política SPF autoriza a agência de *marketing* a enviar em nome da Tatame, e há verificações da PagaFácil e de uma página de status, que são terceiros fora do escopo. O terceiro comando consulta a base de certificados e devolve 180 subdomínios distintos, sem tocar a empresa. O quarto filtra os nomes com cara de teste ou de ambiente antigo e devolve sete, entre eles `hml-gestao` e `promo-hml`. O quinto já é uma consulta ativa, permitida pelas regras do exercício: `hml-gestao` resolve para 203.0.113.45, um endereço da Tatame; `promo-hml` aponta para a agência, em 198.51.100.23, e a linha vermelha diz fora do escopo."
Atenção: as linhas em amarelo e vermelho na saída são comentários didáticos do laboratório, não saída real dos programas. O botão *Executar tudo* roda os cinco comandos de uma vez, mas para a aula é melhor ir um a um e ler a nota de rodapé de cada comando.
Conclusão: "Bases públicas revelam nomes que a TI esqueceu. Agora sabemos quais nomes existem; falta medir o tamanho do problema."
[Tela: gravação do laboratório do slide 11.]

**Slide 12 — Relacionar informações em grafos (10:20–10:50)**
Fala: "Isolados, os achados dizem pouco. Ferramentas como o Maltego ligam domínios, endereços, pessoas e tecnologias em um grafo. No nosso caso, o grafo liga Caio Mendes à vaga, a vaga à versão da VPN e a VPN ao padrão de *e-mail*. Na próxima tela, a superfície inteira aparece em 3D."

**Slide 13 — Laboratório: a superfície de ataque externa em 3D (10:50–12:10)**
Objetivo: medir o tamanho real da exposição em comparação com o inventário.
Na tela:
1. Arrastar a cena para girar e usar a roda do *mouse* para aproximar.
2. Clicar em *Só shadow IT*.
3. Clicar em *Só pessoas*.
4. Clicar em *Tudo* para voltar.
Fala: "No centro está o domínio `tatame.com.br`. Ao redor, os 180 subdomínios: em azul, os 105 que estão no inventário; em cinza, os 60 que não respondem; em vermelho, pulsando, os 15 que respondem e a TI desconhece. Um deles tem o rótulo `hml-gestao`. Ao clicar em *Só shadow IT*, ficam só os vermelhos e o cubo amarelo da agência, ligado por linhas tracejadas a três subdomínios: é o terceiro que fica fora do escopo. Em *Só pessoas*, aparece o anel de 40 pontos acima do domínio. Cada ponto vale 10 pessoas; os amarelos são os 260 *e-mails* expostos entre 400 pessoas."
Atenção: a distribuição das esferas é ilustrativa; os números da legenda são os que valem.
Conclusão: "A superfície real é maior do que o inventário: 15 ativos a mais e mais da metade das pessoas com *e-mail* exposto."
[Tela: gravação do laboratório do slide 13.]

**Slide 14 — Superfície de ataque externa e *shadow IT* (12:10–12:50)**
Fala: "O retrato que acabamos de ver é a superfície de ataque externa. Os ativos que a TI desconhece têm nome: *shadow IT*. Encontrar esses ativos é a função Identificar do NIST CSF 2.0, o guia de cibersegurança do instituto de padrões dos Estados Unidos. Repare nos dois tratamentos do quadro azul: a `hml-gestao` é da Tatame, entra no escopo e vira prioridade; o `promo-hml` é da agência, entra no relatório, mas ninguém da equipe o acessa."

**Slide 15 — Laboratório: o reconhecimento na plataforma Rede Tatame (12:50–15:00)**
Objetivo: ver o que o SOC, o centro de operações de segurança, enxerga do levantamento e o que muda com o monitor de certificados.
Na tela:
1. Conferir que a plataforma abriu na aba *Cenários*. Deixar a velocidade em "1 s = 15 s".
2. No cartão *Reconhecimento externo*, clicar em *Iniciar cenário* e acompanhar a lista de cinco passos até o último terminar.
3. Abrir a aba *Telemetria* e ligar a fonte *Monitor de certificados (CT)*.
4. Abrir a aba *Regras do CEP* e ligar a R12, "Certificado novo para subdomínio fora do inventário".
5. Voltar a *Cenários* e clicar de novo em *Iniciar cenário* no mesmo cartão.
6. Abrir a aba *Superfície* e localizar a linha de `hml-gestao.tatame.com.br`.
Fala: "Na primeira rodada, olhe o ícone de cada passo. A consulta a certificados e a resolução de 180 nomes aparecem como não detectadas, porque acontecem em serviços de terceiros. A varredura contra 203.0.113.0/24 é detectada pela regra R4, que conta excesso de respostas 403 e 404 por endereço. Os passos quatro e cinco, contra a `hml-gestao`, também passam sem alerta, porque a homologação não fica atrás do WAF e ninguém coleta os registros dela. Depois de ligar a fonte CT e a R12, rode o cenário de novo: agora o primeiro passo vira detectado. Na aba *Superfície*, a linha da `hml-gestao` mostra que ela está fora do inventário e sem WAF, com um risco alto que vamos estudar na próxima aula."
Atenção: clicar de novo em *Iniciar cenário* reinicia o cenário e mantém as fontes e regras ligadas; o botão *Reiniciar* do topo volta tudo ao padrão, então não use esse botão entre as duas rodadas. Um alerta extra da R4 pode aparecer, vindo do monitor de disponibilidade contratado; ele é benigno e não faz parte do cenário. O cenário leva cerca de 30 segundos na velocidade padrão.
Conclusão: "Monitorar certificados mostra ao SOC o mesmo nome que o Red Team achou. A defesa pode ver o reconhecimento passivo, desde que olhe para as mesmas fontes."
[Tela: gravação do laboratório do slide 15.]

**Slide 16 — Informação pública também tem regras (15:00–15:40)**
Fala: "Mesmo pública, a informação tem regras. Nomes, cargos e *e-mails* são dados pessoais e estão sujeitos à LGPD, a Lei Geral de Proteção de Dados. Consultar vazamentos ajuda a medir risco, mas usar senhas vazadas só é aceitável se estiver previsto no escopo. Acessar o servidor da agência ou a API da PagaFácil pode configurar o crime do art. 154-A do Código Penal. E, se a equipe achar fichas de alunos menores na `hml-gestao`, registra a evidência mínima e avisa a CISO, sem copiar os dados."

**Slide 17 — Laboratório: do achado solto ao relatório de exposição (15:40–17:00)**
Objetivo: transformar os achados soltos em números para a diretoria, respeitando o escopo.
Na tela:
1. No explorador, abrir `escopo.json`.
2. Voltar a `consolidar_osint.py` e mostrar as linhas destacadas.
3. Clicar em *Executar*.
Fala: "O `escopo.json` diz que a Tatame tem 400 pessoas com *e-mail* e lista as hospedagens fora do escopo: a agência de *marketing*, a página de status terceirizada e a PagaFácil. No script, o primeiro bloco lê os quatro arquivos da pasta `dados`: os subdomínios dos certificados, os que respondem, o inventário da TI e os *e-mails* públicos. A linha que decide o principal resultado é a que monta `desconhecidos`: são os *hosts* que respondem e não estão no inventário. Depois, o laço marca cada desconhecido; se a hospedagem estiver na lista do escopo, a ação é não acessar e avisar o cliente. Na saída, leia de cima para baixo: 180 nomes nos certificados, 120 respondem, 15 fora do inventário, ou seja, 12,5%, e 260 de 400 *e-mails*, ou 65%. Na lista, três linhas vermelhas são de terceiros, e a `hml-gestao` aparece em amarelo. No fim, a exposição por área: academias com 132 *e-mails*, atendimento com 46 e financeiro com 31."
Atenção: os arquivos de dados mostram só as primeiras linhas, como amostra; a saída usa a base completa. Os *e-mails* estão pseudonimizados.
Conclusão: "O relatório mostra o tamanho do problema e onde agir primeiro: inventário, terceiros e treinamento das academias."
[Tela: gravação do laboratório do slide 17.]

**Slide 18 — Que rastro o reconhecimento deixa (17:00–17:30)**
Fala: "Do lado da defesa, o passivo quase não deixa rastro, e a proteção é preventiva. O ativo aparece nos registros. E o Blue Team maduro faz reconhecimento defensivo: monitora a própria superfície e os certificados novos com o nome da empresa."

**Slide 19 — Laboratório: o SOC da Tatame olha para fora (17:30–18:50)**
Objetivo: ver o reconhecimento pelo lado do Blue Team e mostrar que a defesa pode chegar primeiro.
Na tela:
1. Clicar na busca salva "1. Varredura de portas".
2. Clicar em "2. Nomes inexistentes no DNS".
3. Clicar em "3. Certificado novo com o nosso nome".
4. Clicar em "4. Exposto e fora do inventário".
Fala: "Luiza Ferraz, do SOC, revisa a semana no SIEM, a central que reúne os registros. A busca 1 filtra os bloqueios do WAF e conta portas distintas por origem: 198.51.100.200 testou 1.000 portas em quatro minutos, uma varredura barulhenta; 192.0.2.250 testou 62 portas da VPN em nove horas, lenta e seletiva. A busca 2 conta respostas NXDOMAIN por origem: 2.840 perguntas por nomes inexistentes em dez minutos, tentativa de adivinhar subdomínios. Nada aparece sobre a `hml-gestao`. A busca 3 lê o monitor de certificados: um ambiente novo da agência e um domínio que imita o app do aluno, possível preparação de *phishing*. A busca 4 cruza a superfície externa com o inventário e devolve os mesmos 15 ativos do Red Team, com a `hml-gestao` como crítica."
Atenção: o reconhecimento passivo do Red Team não aparece em nenhuma busca, e isso é o esperado.
Conclusão: "A defesa pode usar as mesmas fontes do adversário e achar o problema primeiro."
[Tela: gravação do laboratório do slide 19.]

**Slide 20 — Exemplo numérico: quanto a empresa expõe sem saber (18:50–19:20)**
Fala: "Juntando tudo: 180 subdomínios, 120 ativos, 15 desconhecidos. 15 dividido por 120 dá 12,5% da superfície ativa desconhecida. E 260 dividido por 400 dá 65% das pessoas expostas como alvo de *phishing*."

**Slide 21 — De volta ao problema (19:20–19:50)**
Fala: "Voltemos à pergunta da aula. A vaga, o perfil e o buscador mostraram o que a Tatame publica. Os certificados revelaram 15 nomes fora do inventário, com a `hml-gestao` no topo. O script mediu 12,5% e 65%. E a plataforma mostrou que, com o monitor de certificados e a R12, o SOC vê o subdomínio novo pela mesma fonte do Red Team. A resposta, então: a Tatame expõe 15 ativos que a TI não conhecia e 260 *e-mails*, descobre isso com OSINT autorizado e se mantém à frente com inventário atualizado e monitor de certificados."

**Slides 22 a 24 — Pontos-chave, referências e encerramento (19:50–20:00)**
Fala: "Na próxima aula, vamos descobrir quais desses serviços expostos estão vulneráveis e qual corrigir primeiro. Até lá!"
[Slides: pontos-chave e referências ficam disponíveis no material. Envato: "digital footprint data".]

## Aula 6 — Varredura, enumeração e gestão de vulnerabilidades

### Texto base

Concluído o reconhecimento, o Red Team sabe **onde** procurar. A etapa seguinte responde a outra pergunta: **o que está aberto e o que está vulnerável?** É aqui que entram a varredura, a enumeração e — do lado de quem defende — a gestão de vulnerabilidades, que transforma uma lista enorme de falhas em um plano de correção viável.

#### Varredura e enumeração

A **varredura** identifica quais *hosts* estão ativos, quais portas estão abertas e quais serviços e versões respondem nelas. O **Nmap** é a ferramenta clássica para isso. A **enumeração** aprofunda o resultado: extrai dos serviços encontrados informações como nomes de usuários, compartilhamentos de rede, versões de aplicações e configurações. No ATT&CK, essas atividades aparecem tanto no reconhecimento (T1595 — *Active Scanning*), quando feitas de fora, quanto na tática de Descoberta (TA0007), quando feitas de dentro da rede, por exemplo T1046 — *Network Service Discovery*.

Em seguida, *scanners* de vulnerabilidades como OpenVAS, Nessus ou Qualys comparam os serviços e versões identificados com bases de falhas conhecidas. Como visto na Unidade 1, esse resultado precisa ser validado: *scanners* geram falsos positivos e não comprovam a explorabilidade.

[Imagem 1 — Fluxo em quatro blocos: descoberta de *hosts* → portas e serviços → enumeração → identificação de vulnerabilidades. Texto alternativo: "Fluxograma das etapas de varredura, enumeração e identificação de vulnerabilidades". Pode ser recriado pela equipe de produção.]

#### CVE: dando nome às falhas

Cada vulnerabilidade conhecida recebe um identificador **CVE** (*Common Vulnerabilities and Exposures*), no formato CVE-ano-número — por exemplo, CVE-2021-44228, a falha na biblioteca Log4j conhecida como Log4Shell. O programa CVE é coordenado pela MITRE, e a NVD (*National Vulnerability Database*), mantida pelo NIST, enriquece os registros com informações de severidade e produtos afetados. O identificador comum permite que *scanner*, fornecedor, Red Team e Blue Team falem da mesma falha sem ambiguidade.

#### CVSS: quão grave é a falha?

O **CVSS** (*Common Vulnerability Scoring System*), mantido pelo FIRST, atribui uma nota de 0 a 10 a uma vulnerabilidade, considerando fatores como o vetor de ataque (rede, local, físico), a complexidade, a necessidade de privilégios ou de interação do usuário e o impacto sobre confidencialidade, integridade e disponibilidade. A versão 4.0 foi publicada em 2023, mas a 3.1 ainda é amplamente usada. As faixas qualitativas são:

| Nota CVSS | Severidade |
|---|---|
| 0,0 | Nenhuma |
| 0,1–3,9 | Baixa |
| 4,0–6,9 | Média |
| 7,0–8,9 | Alta |
| 9,0–10,0 | Crítica |

O ponto de atenção é que a nota-base do CVSS mede **severidade técnica**, e não **risco**. Ela não diz se a falha está sendo explorada no mundo real nem se o ativo afetado é crítico para o negócio.

#### EPSS e KEV: a falha está sendo explorada?

Para complementar o CVSS, surgiram duas referências públicas. O **EPSS** (*Exploit Prediction Scoring System*), também do FIRST, estima a **probabilidade** de que uma vulnerabilidade seja explorada nos 30 dias seguintes, com base em dados observados de atividade de exploração. O catálogo **KEV** (*Known Exploited Vulnerabilities*), da agência norte-americana CISA, lista vulnerabilidades com **exploração confirmada**; para órgãos federais dos Estados Unidos, a correção dessas falhas tem prazos obrigatórios, e muitas empresas privadas adotam o catálogo como critério de prioridade.

[Imagem 2 — Matriz de prioridade com o eixo horizontal "severidade (CVSS)" e o eixo vertical "probabilidade de exploração (EPSS)", destacando o quadrante superior direito como "corrigir já". Texto alternativo: "Gráfico de dispersão de vulnerabilidades com CVSS no eixo x e EPSS no eixo y". Pode ser recriado pela equipe de produção.]

#### Gestão de vulnerabilidades como processo

A gestão de vulnerabilidades é um **ciclo contínuo**: inventariar ativos, identificar falhas, priorizar, corrigir ou mitigar, verificar a correção e reportar. Uma boa priorização combina quatro perguntas: a falha é grave (CVSS)? É provável que seja explorada (EPSS)? Já está sendo explorada (KEV)? O ativo é exposto à internet ou crítico para o negócio? A partir disso, a organização define **SLAs de correção** — por exemplo, 7 dias para falhas no KEV em ativos expostos, 30 dias para altas e 90 para médias. O NIST SP 800-40 Rev. 4 trata a aplicação de correções (*patch management*) como manutenção preventiva, que precisa ser planejada, e não como reação a cada alerta.

[Imagem 3 — Ciclo circular com seis etapas: inventariar, identificar, priorizar, corrigir, verificar e reportar. Texto alternativo: "Ciclo contínuo da gestão de vulnerabilidades". Sugestão de busca no Envato: "continuous cycle infographic six steps".]

#### Que rastro isso deixa para o Blue Team?

Varreduras são ruidosas: muitas conexões em sequência para portas diferentes, a partir da mesma origem, geram registros em *firewalls*, sistemas de detecção de intrusão e servidores. A enumeração interna gera consultas incomuns ao diretório e tentativas de autenticação. Por isso, em operações de Red Team que testam a detecção, a varredura é feita de forma mais lenta e seletiva — e a pergunta para o Blue Team passa a ser "nossa detecção percebe varreduras discretas, ou só as barulhentas?".

#### Exemplo numérico: CVSS ou EPSS?

Uma equipe com capacidade de corrigir 150 vulnerabilidades por semana recebe um relatório com 1.200 achados. Se priorizar tudo com CVSS ≥ 7,0 (480 achados), levará 480 ÷ 150 = **3,2 semanas** só para essa fila. Considere três casos com valores ilustrativos:

| Vulnerabilidade | CVSS | EPSS | No KEV? | Ativo |
|---|---|---|---|---|
| A | 9,8 | 0,02 (2%) | Não | Servidor interno isolado |
| B | 7,5 | 0,89 (89%) | Sim | Portal exposto à internet |
| C | 5,3 | 0,40 (40%) | Não | VPN corporativa |

Pelo CVSS, A viria primeiro. Pelo risco, **B é a prioridade**: está sendo explorada, tem alta probabilidade de exploração e está exposta. Se a empresa filtrar apenas KEV ou EPSS ≥ 10% em ativos expostos e restarem 60 achados, essa fila crítica será tratada em 60 ÷ 150 = **0,4 semana**, cerca de dois dias úteis.

#### Pontos-chave

- Varredura descobre serviços; enumeração extrai detalhes deles; ambas são ruidosas.
- CVE identifica a falha; CVSS mede a severidade técnica, não o risco.
- EPSS estima a probabilidade de exploração; o KEV confirma exploração real.
- Priorizar por risco reduz drasticamente o tempo de exposição às falhas que importam.

### Referências da aula

CYBERSECURITY AND INFRASTRUCTURE SECURITY AGENCY. *Known exploited vulnerabilities catalog*. Disponível em: <https://www.cisa.gov/known-exploited-vulnerabilities-catalog>. Acesso em: 13 nov. 2026.

FORUM OF INCIDENT RESPONSE AND SECURITY TEAMS. *Common vulnerability scoring system version 4.0: specification document*. 2023. Disponível em: <https://www.first.org/cvss/>. Acesso em: 13 nov. 2026.

FORUM OF INCIDENT RESPONSE AND SECURITY TEAMS. *Exploit prediction scoring system (EPSS)*. Disponível em: <https://www.first.org/epss/>. Acesso em: 13 nov. 2026.

JACOBS, Jay *et al*. Exploit prediction scoring system (EPSS). *Digital Threats: Research and Practice*, v. 2, n. 3, 2021.

SOUPPAYA, Murugiah; SCARFONE, Karen. *SP 800-40 Rev. 4: guide to enterprise patch management planning: preventive maintenance for technology*. Gaithersburg: NIST, 2022.

### Roteiro da Videoaula 6 — "1.200 achados e uma semana: o que a Tatame corrige primeiro?"

Duração-alvo: 15 a 20 minutos. Deck: unidade_2/slides/aula6.html (24 slides).

**Slides 1 a 3 — Capa, audiodescrição e sumário (0:00–0:40)**
Fala: "Olá! Esta é a Aula 6 da Unidade 2. Na aula passada, descobrimos o que a Rede Tatame expõe na internet. Hoje vamos varrer esses ativos, encontrar as falhas e decidir qual delas corrigir primeiro. Antes de começar, a audiodescrição dos slides está na tela para quem precisar."
[Câmera: professor em plano médio. Slide 3 na tela ao fim da fala.]

**Slide 4 — O problema de hoje na Rede Tatame (0:40–2:00)**
Fala: "Conheça o Caio Mendes, que administra a TI da sede da Tatame. O Red Team de Bruno Sato terminou a varredura autorizada e o *scanner* devolveu 1.200 achados. Só que a equipe do Caio corrige no máximo 150 por semana, e só os achados de gravidade alta já levariam 3,2 semanas. No mapa, em vermelho, está a `hml-gestao`, aquela homologação esquecida da Aula 5, que guarda fichas de alunos. A pergunta de hoje é esta: com 1.200 achados e capacidade para 150 correções por semana, o que a Tatame deve corrigir primeiro? Guarde essa pergunta, porque cada laboratório vai responder uma parte dela."
[Take de apoio: equipe de TI diante de uma lista longa de alertas — Envato: "IT team overwhelmed alerts".]

**Slide 5 — Varredura, enumeração e *scanners* (2:00–2:50)**
Fala: "Primeiro, os conceitos. A varredura descobre quais máquinas respondem, quais portas estão abertas e que serviço roda em cada uma. A enumeração vai mais fundo e extrai nomes de usuários, compartilhamentos e configurações. Os *scanners* de vulnerabilidades comparam essas versões com bases de falhas conhecidas. Repare no destaque: o *scanner* gera falsos positivos, então todo resultado precisa ser validado."

**Slide 6 — Laboratório: da descoberta de *hosts* à lista de vulnerabilidades (2:50–4:00)**
Objetivo: mostrar de onde vêm os 1.200 achados e que rastro cada etapa deixa.
Na tela:
1. Clicar em *Avançar* no passo "1 · Descoberta de hosts": 7 de 512 endereços respondem.
2. *Avançar* para "2 · Portas e serviços".
3. *Avançar* para "Rastro · O firewall registra": acendem *Firewall e IDS* e *SIEM*, em azul.
4. *Avançar* para "3 · Enumeração" e depois "Rastro · O diretório registra".
5. *Avançar* para "4 · Identificação de vulnerabilidades" (1.200 achados), "5 · Validação" e "6 · Priorização".
Fala: "Cada caixa da linha de cima é uma etapa do Red Team, e cada caixa azul é um lugar onde a defesa pode ver essa etapa. Quando a varredura bate em muitas portas, o *firewall* e o IDS, que é o sistema de detecção de intrusão, registram e mandam para o SIEM. Notem um detalhe no texto do rastro: a `hml-gestao` está fora do WAF, então não registra nada. No fim, o *scanner* gera os 1.200 achados, mas eles ainda passam pela validação e pela priorização."
Atenção: o botão *Auto* avança sozinho; para narrar com calma, prefira *Avançar*. São 8 passos.
Conclusão: "Os 1.200 achados são o começo do trabalho. Ainda falta separar o que é real do que é ruído."
[Tela: gravação do laboratório do slide 6.]

**Slide 7 — Laboratório: varredura autorizada na borda e na sede (4:00–5:40)**
Objetivo: gerar a lista de achados da Tatame e ver um falso positivo sendo descartado.
Na tela:
1. Clicar em *Próximo comando*: roda `inventario-rede descobrir 203.0.113.0/24 10.10.1.0/24`.
2. Clicar em *Próximo comando*: roda `inventario-rede enumerar 10.10.1.20`.
3. Clicar em *Próximo comando*: roda `scanner-vuln resumo varredura-2026-11.json`.
4. Clicar em *Próximo comando*: roda `scanner-vuln validar TAT-2026-014`.
Fala: "Este utilitário é fictício, feito para a aula. O primeiro comando confere a autorização TAT-2611, assinada pela Marina Prado, e mostra o que ficou fora: a PagaFácil e a rede de pagamentos. Depois lista 7 *hosts* ativos, com porta, serviço e versão. Olhem a linha da `hml-gestao`: Apache 2.4.49, sem WAF. O segundo comando enumera o servidor de arquivos com uma conta de teste sem privilégios e acha duas pastas legíveis por todos: FINANCEIRO e EXPORT-ALUNOS, com fichas inclusive de menores. A equipe registra o achado e não abre nenhum arquivo. O terceiro mostra o relatório por severidade: 95 críticos, 385 altos, 520 médios e 200 baixos, total de 1.200. Os de CVSS maior ou igual a 7 somam 480, e 480 dividido por 150 dá 3,2 semanas. O quarto valida o achado TAT-2026-014 no SRV-ERP-01: o *scanner* deduziu a falha só pelo número de versão, mas a correção já estava aplicada. É um falso positivo."
Atenção: os comandos e as saídas são simulados. O botão *Executar tudo* roda os quatro de uma vez; use-o só se o tempo apertar.
Conclusão: "O *scanner* aponta suspeitas, e quem confirma é a validação. Agora temos a lista, mas ainda não sabemos por onde começar."
[Tela: gravação do laboratório do slide 7.]

**Slides 8 a 10 — CVE, CVSS, EPSS e KEV (5:40–7:10)**
Fala: "Para ordenar a lista, precisamos de três referências. A CVE é o nome da falha, como a CVE-2021-44228, o Log4Shell. O CVSS, mantido pelo FIRST, dá uma nota de 0 a 10 para a gravidade técnica, com as faixas da tabela. Mas o CVSS não diz se a falha está sendo explorada nem se o ativo importa. Para isso existe o EPSS, que estima a probabilidade de exploração nos 30 dias seguintes, e o KEV, o catálogo da CISA com as falhas de exploração confirmada. Em resumo: o CVSS diz quão grave é, o EPSS diz quão provável é a exploração e o KEV diz que ela já acontece."
[Take de apoio: tela com tabela de vulnerabilidades — Envato: "vulnerability scan report screen".]

**Slide 11 — Laboratório: uma CVE consultada em três fontes (7:10–8:30)**
Objetivo: ler a mesma falha pelas três referências.
Na tela:
1. Na aba *Registro e CVSS*, clicar em cada parte do vetor: AV:N, AC:L, PR:N, UI:N, S:C, C:H, I:H, A:H.
2. Clicar na aba *EPSS*.
3. Clicar na aba *KEV*.
[Tela de apoio: abrir o site do FIRST e mostrar o EPSS do dia da CVE-2021-44228.]
Fala: "O vetor CVSS é uma frase em código. AV:N quer dizer que o ataque vem pela rede; AC:L, complexidade baixa; PR:N, nenhum privilégio; UI:N, ninguém precisa clicar. Por isso a nota chega a 10. Na aba EPSS, o valor é muito alto, entre os maiores da base, e muda todo dia. Vou abrir o site do FIRST para lermos o número de hoje. Comparem com o EPSS de 0,02 da vulnerabilidade A que veremos no exemplo. Na aba KEV, a falha consta do catálogo desde dezembro de 2021. O resumo da triagem está no fim da página: CVSS crítico, EPSS muito alto e KEV. Se o ativo estiver exposto, é a primeira da fila."
Atenção: a página é ilustrativa; o valor exato do EPSS deve ser lido no site no dia da gravação.
Conclusão: "O CVSS mede a gravidade; o EPSS e o KEV dizem se alguém está explorando."
[Tela: gravação do laboratório do slide 11.]

**Slide 12 — Laboratório: o cubo de risco (8:30–9:40)**
Objetivo: ver gravidade, probabilidade e importância do ativo ao mesmo tempo.
Na tela:
1. Arrastar com o mouse para girar o cubo de lado.
2. Apontar a esfera B, dentro da caixa vermelha "corrigir já".
3. Apontar a esfera C e a esfera A, com o rótulo "A · CVSS 9,8 · EPSS 2%".
Fala: "Cada esfera é um achado. O eixo CVSS mede a gravidade, o eixo EPSS a probabilidade, e a profundidade é a criticidade do ativo. A caixa vermelha é a região de prioridade: CVSS a partir de 7, EPSS a partir de 10% e ativo importante. Os anéis amarelos marcam falhas do KEV. A tem CVSS 9,8, o maior do exemplo, mas EPSS de 2% em um servidor isolado, então fica fora da caixa. B tem CVSS 7,5, EPSS de 89%, está no KEV e mora na `hml-gestao`, exposta à internet. B está dentro da caixa."
Atenção: as esferas pequenas sem rótulo são achados ilustrativos de fundo; só A a G vêm do exemplo da aula.
Conclusão: "CVSS alto não quer dizer risco alto."
[Tela: gravação do laboratório do slide 12.]

**Slide 13 — Gestão de vulnerabilidades como ciclo contínuo (9:40–10:20)**
Fala: "Priorizar é uma etapa de um ciclo: inventariar, identificar, priorizar, corrigir, verificar e reportar. A tabela junta as quatro perguntas da priorização. Os SLAs, prazos máximos combinados, ficam assim no exemplo: 7 dias para falhas no KEV em ativos expostos, 30 para altas e 90 para médias."

**Slide 14 — Laboratório: priorização por risco em Python (10:20–11:50)**
Objetivo: ordenar os sete achados da Tatame por risco e medir o tamanho das filas.
Na tela:
1. Mostrar `priorizar.py` sendo digitado e destacar as funções `probabilidade`, `risco` e `sla`.
2. Abrir `achados.csv` no explorador e mostrar as linhas A, B e C.
3. Clicar em *Priorizar*.
4. Clicar em *Calcular filas*.
Fala: "O código tem três funções. A `probabilidade` devolve 1,0 se a falha está no KEV e, se não estiver, usa o EPSS. A `risco` multiplica o CVSS pela probabilidade, pelo peso da exposição, que é 1,0 na internet, 0,6 na rede interna e 0,3 em segmento isolado, e por 1,5 se o ativo for crítico. Essa é a linha que decide a ordem. A `sla` dá 7 dias para KEV na internet. O arquivo `achados.csv` traz os sete achados. Ao rodar, a primeira linha mostra a ordem por CVSS: A, D, F, B, G, E, C. Logo abaixo vem a ordem por risco, e tudo muda. B, a `hml-gestao`, fica em primeiro com risco 11,25: 7,5 vezes 1,0 do KEV, vezes 1,0 da internet, vezes 1,5 de ativo crítico. A cai para sexto, com 0,06. Agora o `fila.py`: 480 achados levam 3,2 semanas; a fila crítica, KEV ou EPSS de pelo menos 10% em ativo exposto, tem 60 achados e leva 0,4 semana, dois dias úteis."
Atenção: o *Digitar ao vivo* repete a digitação do código; não é necessário para a gravação.
Conclusão: "A fórmula de risco encurta a fila sem esquecer o que importa."
[Tela: gravação do laboratório do slide 14.]

**Slide 15 — Varreduras fazem barulho (11:50–12:20)**
Fala: "Agora o outro lado. Muitas conexões em sequência, para portas diferentes, geram registros no *firewall* e no IDS. A enumeração interna gera consultas incomuns ao diretório. Em exercícios que testam a detecção, o Red Team varre devagar. A pergunta para o Blue Team é se a detecção percebe a varredura discreta."

**Slide 16 — Laboratório: varredura barulhenta e varredura discreta (12:20–13:40)**
Objetivo: ver a varredura pelo lado do SOC e achar uma lacuna de detecção.
Na tela:
1. Clicar em "1. Regra padrão (5 min)".
2. Clicar em "2. A varredura lenta passou?".
3. Clicar em "3. Janela de 24 horas".
4. Clicar em "4. Consultas volumosas ao diretório".
Fala: "A primeira busca conta quantas portas distintas cada origem tocou em janelas de 5 minutos e alerta acima de 50. A origem 10.10.99.5 tocou mil portas em quatro servidores às 10h05: alerta alto. Na plataforma, a regra equivalente para a borda é a R4. A segunda busca aplica a mesma regra à origem 10.10.99.6 e volta vazia: ela testou uma porta a cada 5 minutos o dia todo e nunca passou do limite. A terceira muda a janela para 24 horas e acha as duas origens; a lenta aparece com 288 portas. A quarta olha o AD: a conta de teste `teste.red01` fez 4.310 consultas LDAP a partir do NB-TI-009, algo que um usuário comum não faz. É a regra R13 da plataforma, que veremos na Aula 8."
Atenção: o vazio da busca 2 é o resultado esperado. Explique que ele vai para o relatório como lacuna.
Conclusão: "Uma regra só para varredura rápida deixa passar a discreta, por isso a proposta é manter as duas."
[Tela: gravação do laboratório do slide 16.]

**Slide 17 — Exemplo numérico: CVSS ou EPSS? (13:40–14:20)**
Fala: "Vamos fechar as contas com o exemplo do texto. Tudo com CVSS a partir de 7 soma 480 achados: 3,2 semanas. Na tabela, A tem CVSS 9,8 e EPSS de 2% num servidor isolado. B tem CVSS 7,5, EPSS de 89%, está no KEV e fica exposta. C tem CVSS 5,3 e EPSS de 40% na VPN. Pelo risco, B é a prioridade. Filtrando KEV ou EPSS de pelo menos 10% em ativos expostos, restam 60 achados: 0,4 semana, cerca de dois dias úteis."

**Slide 18 — Laboratório: console de gestão de vulnerabilidades (14:20–15:20)**
Objetivo: montar a fila de correção desta semana.
Na tela:
1. Com *Ordenar por CVSS* ativo, mostrar A no topo.
2. Clicar em *Ordenar por risco*.
3. Clicar em *Só a fila crítica*.
4. Arrastar o controle *Capacidade da equipe* de 150 para 100 e depois de volta para 150.
Fala: "Este console é o que a equipe do Caio usaria no dia a dia. Ordenando por CVSS, A está em primeiro. Ao ordenar por risco, B sobe para o topo e A desce. Quando ligo *Só a fila crítica*, ficam destacados os achados expostos à internet que estão no KEV ou têm EPSS de pelo menos 10%: B, C e E. C tem CVSS de só 5,3, mas está na VPN exposta e tem EPSS de 40%. Embaixo, os dois cartões mostram o tempo de cada fila. Se a capacidade cai para 100, as duas filas crescem; a crítica continua cabendo em poucos dias."
Conclusão: "Os 60 achados críticos cabem em dois dias úteis."
[Tela: gravação do laboratório do slide 18.]

**Slide 19 — Laboratório: priorização e abuso de API na plataforma Rede Tatame (15:20–17:00)**
Objetivo: ver a priorização na plataforma e uma falha que o *scanner* não encontra.
Na tela:
1. O simulador abre na aba *Superfície*. Mostrar a tabela *Ativos expostos* com "ordenar por risco" marcado e comparar as colunas CVSS e RISCO.
2. Abrir a aba *Cenários* e clicar em *Iniciar cenário* no cartão *Abuso da API do app*.
3. Acompanhar a lista de passos do cenário e anotar qual passo fica sem alerta.
4. Abrir *Regras do CEP*, ligar a R3 e voltar a *Cenários* para clicar de novo em *Iniciar cenário*.
Fala: "Esta é a plataforma da disciplina. Na aba *Superfície*, cada linha é um ativo exposto, com CVE, CVSS, EPSS, KEV, criticidade e uma coluna de risco. Olhem o `www`: CVSS 10 e KEV, mas fica só em quarto lugar, porque tem WAF e criticidade baixa. A VPN e a `hml-gestao` vêm antes. Agora o cenário *Abuso da API do app*: senhas vazadas de outros *sites* são testadas no app, e depois alguém lê a ficha de outro aluno trocando o número na URL. Esse tipo de falha se chama BOLA, autorização quebrada no nível do objeto. Ela não tem CVE, então nenhum *scanner* a encontra. Na primeira rodada, a leitura indevida fica sem alerta. Depois de ligar a R3, rodo de novo, e a mesma leitura vira alerta."
Atenção: Iniciar o cenário de novo mantém as regras ligadas; *Reiniciar* volta tudo ao padrão e desliga a R3. Se o tempo apertar, aumente a velocidade no seletor ao lado de *Iniciar*. Na aba *Requisições*, as linhas do ataque só aparecem com o cenário rodando.
Conclusão: "Falha de lógica só aparece em teste e precisa de regra própria."
[Tela: gravação do laboratório do slide 19, com o simulador em tela cheia.]

**Slide 20 — Caso real: Log4Shell, dezembro de 2021 (17:00–17:40)**
Fala: "Um caso real. Quando a CVE-2021-44228 veio a público, a correção já existia. O difícil foi responder onde a biblioteca Log4j estava, porque vinha embutida em aplicações e produtos de fornecedores. Quem tinha inventário foi direto aos ativos expostos. Na Tatame, o `www` foi corrigido assim; a `hml-gestao`, fora do inventário, ficou para trás. É o mesmo recado da Aula 5 sobre *shadow IT*."
[Take de apoio: manchetes de dezembro de 2021 sobre o Log4Shell, sem logotipos de veículos — Envato: "breaking news cyber attack".]

**Slide 21 — De volta ao problema (17:40–18:30)**
Fala: "Voltemos ao Caio. No fluxo e no terminal, vimos de onde vêm os 1.200 achados e descartamos um falso positivo. No cubo, A tinha CVSS 9,8 e mesmo assim ficou fora da região de prioridade. O script e o console colocaram B, a `hml-gestao`, no topo. E a plataforma mostrou uma falha da API que nenhum *scanner* vê. A resposta à pergunta da aula: a Tatame corrige primeiro o que está no KEV ou tem EPSS de pelo menos 10% em ativo exposto, a começar pela `hml-gestao`. São 60 achados, cerca de dois dias úteis, em vez de 3,2 semanas pela fila de CVSS."

**Slides 22 a 24 — Pontos-chave, referências e encerramento (18:30–19:15)**
Fala: "Para levar: varredura e enumeração descobrem serviços e são ruidosas; a CVE dá nome à falha; o CVSS mede a severidade técnica, e o risco depende também do ativo e da exploração; o EPSS e o KEV mostram exploração; priorizar por risco reduz o tempo de exposição. As referências estão no slide. Corrigir falhas técnicas é essencial, mas o adversário também pode simplesmente pedir a senha a alguém do financeiro. Na próxima aula, vamos estudar engenharia social e simulação de *phishing*. Até lá!"
[Câmera: professor em plano médio para o fechamento.]

## Aula 7 — Engenharia social e simulação de *phishing*

### Texto base

Nem todo ataque começa por uma falha técnica. Muitas vezes, o caminho mais curto até os dados de uma empresa passa por uma pessoa: alguém que abre um anexo, informa uma senha por telefone ou segura a porta para um "técnico" sem crachá. Relatórios anuais como o *Data Breach Investigations Report* (DBIR), da Verizon, apontam de forma recorrente que o elemento humano está presente na maioria das violações analisadas. Por isso, a engenharia social é parte essencial de muitas operações de Red Team — sempre com autorização e com finalidade educativa.

#### O que é engenharia social

**Engenharia social** é a manipulação psicológica de pessoas para que realizem ações ou revelem informações que favoreçam o atacante. Ela explora características humanas, e não falhas de *software*. Os princípios de persuasão descritos pelo psicólogo Robert Cialdini ajudam a entender por que ela funciona:

| Princípio | Como aparece em um golpe | Exemplo |
|---|---|---|
| Autoridade | O atacante se passa por alguém com poder | "Aqui é o diretor financeiro, preciso disso agora" |
| Urgência e escassez | Prazo curto para agir | "Sua conta será bloqueada em 1 hora" |
| Aprovação social | "Todos já fizeram" | "Falta só você atualizar o cadastro" |
| Reciprocidade | Oferece algo antes de pedir | Brinde ou ajuda técnica não solicitada |
| Afeição | Simpatia e semelhança | Conversa amigável antes do pedido |
| Compromisso e coerência | Pequenos "sins" levam a um grande "sim" | Pedidos que crescem aos poucos |

[Imagem 1 — Ilustração de uma pessoa ao telefone diante de um computador, com balões de fala indicando urgência e autoridade. Texto alternativo: "Funcionário atendendo telefonema que usa urgência e autoridade para pressioná-lo". Sugestão de busca no Envato: "social engineering phone call office".]

#### Vetores mais comuns

No ATT&CK, o *phishing* aparece como técnica de acesso inicial (T1566), com subtécnicas como anexo malicioso (T1566.001) e *link* malicioso (T1566.002), e também como coleta de informações (T1598 — *Phishing for Information*). Outros vetores incluem o *vishing* (por voz), o *smishing* (por SMS), o *pretexting* (uma história inventada para justificar o pedido) e a engenharia social física, como entrar em um prédio seguindo um funcionário (*tailgating*). Uma variante de alto impacto é a fraude do *e-mail* corporativo comprometido (*Business Email Compromise*), em que o golpista se passa por um executivo ou fornecedor para desviar pagamentos.

#### Simulações de *phishing* autorizadas

As simulações de *phishing* são campanhas controladas, enviadas aos próprios colaboradores, para medir e melhorar a capacidade de reconhecer e **reportar** mensagens suspeitas. Plataformas como o **GoPhish**, de código aberto, permitem criar campanhas, enviar mensagens e coletar métricas. Uma simulação ética precisa de:

- **autorização formal** da liderança e alinhamento com RH, jurídico e encarregado de dados (DPO);
- **finalidade educativa**: quem clica recebe orientação imediata, e não punição;
- **proteção de dados**: nenhuma senha real é armazenada, e os resultados individuais têm acesso restrito, conforme a LGPD;
- **limites de pretexto**: temas como demissões, saúde, salários ou tragédias podem causar dano real e costumam ser vetados nas regras de engajamento.

A dificuldade da mensagem também importa: uma isca muito fácil gera números enganosamente bons. O NIST propôs a *Phish Scale*, um método para classificar a dificuldade de uma mensagem de *phishing* conforme as pistas que ela contém e o quanto o contexto se aproxima da rotina do público.

[Imagem 2 — Painel de uma campanha de simulação com indicadores de enviados, abertos, clicados, dados submetidos e reportados. Texto alternativo: "Painel com as métricas de uma campanha de simulação de *phishing*". Sugestão de busca no Envato: "email campaign dashboard metrics".]

#### Métricas que importam

As métricas mais usadas são a **taxa de clique**, a **taxa de submissão de dados** e a **taxa de reporte**. A taxa de reporte, frequentemente esquecida, é a que mais interessa ao Blue Team: um único reporte rápido permite que o SOC bloqueie a mensagem para toda a empresa. Por isso, além do "quem clicou", vale medir o **tempo até o primeiro reporte** e a razão entre reportes e cliques.

#### Que rastro isso deixa para o Blue Team?

A engenharia social deixa rastros técnicos: cabeçalhos de *e-mail*, domínios recém-registrados e parecidos com o da empresa, falhas nas verificações de autenticação de *e-mail* (SPF, DKIM e DMARC), cliques registrados no *proxy* e acessos a páginas falsas. E deixa um rastro humano: o reporte do colaborador. Em uma organização madura, cada pessoa funciona como um sensor.

#### Exemplo numérico: lendo uma campanha

Uma campanha autorizada envia 1.000 mensagens. Resultado: 180 cliques (**18%**), 60 submissões de dados no formulário simulado (**6%**) e 120 reportes (**12%**), com o primeiro reporte em 9 minutos. A razão reporte/clique é 120 ÷ 180 ≈ **0,67**. Após três meses de treinamentos curtos e de um botão de reporte no cliente de *e-mail*, uma nova campanha de dificuldade equivalente mostra 90 cliques (9%), 25 submissões (2,5%) e 300 reportes (30%). A razão sobe para 300 ÷ 90 ≈ **3,3**: agora há mais de três reportes para cada clique — sinal de uma cultura que detecta.

[Imagem 3 — Gráfico de barras comparando as campanhas 1 e 2 em cliques, submissões e reportes. Texto alternativo: "Gráfico de barras mostrando queda de cliques e aumento de reportes entre duas campanhas de simulação". Pode ser recriado pela equipe com os dados do exemplo.]

#### Pausa para reflexão

> Um hospital com 2.500 colaboradores pede ao Red Team uma simulação de *phishing* com o tema "resultado de exames de colaboradores com covid". A diretoria também quer receber a lista nominal de quem clicou para aplicar advertências.
>
> 1. Que riscos éticos e legais esse pedido apresenta, considerando a LGPD e o bem-estar dos colaboradores?
> 2. Que tema alternativo, plausível para o ambiente hospitalar, você proporia?
> 3. Quais métricas você apresentaria à diretoria no lugar da lista nominal, e por quê?
>
> **Desafio prático:** elabore um plano de campanha de uma página com objetivo, público, pretexto, métricas (clique, submissão, reporte e tempo até o primeiro reporte), tratamento dos dados e ação educativa para quem clicar.

#### Pontos-chave

- A engenharia social explora princípios de persuasão, como autoridade e urgência.
- *Phishing* (T1566) é um dos vetores de acesso inicial mais usados por adversários reais.
- Simulações autorizadas têm finalidade educativa, protegem os dados e evitam pretextos danosos.
- A taxa de reporte e o tempo até o primeiro reporte medem a capacidade de detecção humana.

### Referências da aula

CIALDINI, Robert B. *As armas da persuasão*. Rio de Janeiro: Sextante, 2012.

MITNICK, Kevin D.; SIMON, William L. *A arte de enganar*. São Paulo: Pearson Education, 2003.

MITRE. *Phishing (T1566)*. In: MITRE ATT&CK. Disponível em: <https://attack.mitre.org/techniques/T1566/>. Acesso em: 13 nov. 2026.

STEVES, Michelle; GREENE, Kristen; THEOFANOS, Mary. Categorizing human phishing difficulty: a Phish Scale. *Journal of Cybersecurity*, v. 6, n. 1, 2020.

VERIZON. *Data breach investigations report*. [S. l.]: Verizon, 2025.

### Roteiro da Videoaula 7 — "Quem clicou? Essa é a pergunta errada"

Duração-alvo: 15 a 20 minutos. Deck: unidade_2/slides/aula7.html (23 slides).

**Slides 1 a 3 — Capa, audiodescrição e sumário (0:00–0:40)**
Fala: "Olá! Nesta aula vamos falar de engenharia social e de simulação de *phishing*. Vamos acompanhar uma campanha autorizada na Rede Tatame, da caixa de entrada até o SOC, e terminar planejando uma campanha para um hospital. No caminho, você vai ver sete laboratórios."
[Take de apoio: pessoa lendo *e-mails* no notebook em um escritório — Envato]

**Slide 4 — O problema de hoje na Rede Tatame (0:40–2:00)**
Fala: "Comece pela Carla Dias, analista do financeiro da Rede Tatame. Em março, ela e outras 999 pessoas receberam um *e-mail* de 'benefícios do RH'. Era uma campanha simulada, autorizada pela CISO Marina Prado. A Carla clicou no link e preencheu o formulário simulado. Outras pessoas apagaram a mensagem, e algumas usaram o botão de reporte, que avisa o SOC, o centro de operações de segurança. Por que isso importa? O financeiro paga fornecedores e acessa a VPN. Num ataque real, esse formulário entregaria a senha dela ao adversário. Só o aviso rápido de alguém e o segundo fator de *login* impediriam o uso dessa senha. A pergunta da aula está em amarelo: quando um *e-mail* falso chega, as pessoas da Tatame percebem e avisam o SOC a tempo? Repare nos papéis embaixo e no mapa à direita: o caminho em vermelho vai da internet ao servidor de correio e dali ao notebook do financeiro."
[Tela: slide 4 com o cursor seguindo o caminho em vermelho do mini-mapa]

**Slide 5 — O elemento humano nas violações (2:00–2:50)**
Fala: "Nem todo ataque começa por uma falha técnica. Muitas vezes o caminho mais curto passa por uma pessoa que abre um anexo, informa uma senha por telefone ou segura a porta para um 'técnico' sem crachá. Relatórios anuais como o *Data Breach Investigations Report*, da Verizon, mostram de forma recorrente que o elemento humano está presente na maioria das violações. Por isso a engenharia social entra em muitas operações de Red Team, sempre com autorização e finalidade educativa."

**Slides 6 e 7 — Princípios de persuasão e vetores (2:50–4:10)**
Fala: "Engenharia social é manipular pessoas para que façam algo ou revelem informações. Os princípios de Robert Cialdini ajudam a entender por que funciona: autoridade, urgência e escassez, aprovação social, reciprocidade, afeição, compromisso e coerência. Leia os exemplos da terceira coluna: 'Aqui é o diretor financeiro', 'Sua conta será bloqueada em 1 hora'. No slide seguinte estão os vetores. O *phishing* é a técnica T1566 do ATT&CK; o *vishing* e o *smishing* repetem o golpe por voz e por SMS; o *pretexting* inventa uma história; o *tailgating* é a versão física; e o *Business Email Compromise* desvia pagamentos fingindo ser um executivo ou fornecedor. Guarde esse último, porque o financeiro da Carla é o alvo típico."
[Take de apoio: telefone tocando com "número desconhecido" na tela — Envato]

**Slide 8 — Laboratório: encontre as pistas e reporte a mensagem (4:10–6:00)**
Objetivo: mostrar que a isca tem pistas reconhecíveis e que o reporte é o primeiro passo da defesa. Responde à parte "as pessoas percebem?" da pergunta.
Na tela:
1. Mostrar a caixa de entrada à esquerda, com a mensagem "RH Tatame · URGENTE: seu benefício será bloqueado" selecionada. Ler o contador "0 de 7 pistas" no alto.
2. Clicar no remetente "RH Tatame <rh@portal-rh-beneficios.com>". Ler a explicação na barra inferior.
3. Clicar no assunto "URGENTE: seu acesso ao portal de benefícios será bloqueado em 1 hora".
4. Clicar na saudação "Prezado(a) colaborador(a)".
5. Clicar em "92% do seu setor já atualizou os dados, falta só você."
6. Clicar no botão azul "Acessar o portal Tatame". Aparece o endereço real, http://portal-rh-beneficios.com/login.
7. Clicar na assinatura "Diretoria de Pessoas e Benefícios".
8. Clicar em "Detalhes técnicos" e depois na linha "spf=pass ... dkim=none; dmarc=none". O contador chega a "7 de 7 pistas".
9. Clicar em "⚑ Reportar phishing".
Fala: "Cada trecho clicado acende e a barra embaixo explica a pista. O remetente diz RH Tatame, mas o domínio é portal-rh-beneficios.com, registrado há 2 dias; o da empresa é tatame.com.br. O assunto usa urgência: uma hora para agir antes de pensar. A saudação é genérica, e o RH de verdade sabe o seu nome. '92% do seu setor já atualizou' é aprovação social. A assinatura da diretoria, com ameaça de suspender o benefício, é autoridade. O botão diz portal Tatame, mas leva ao mesmo domínio novo. Nos detalhes técnicos, veja que o SPF passa. Isso surpreende muita gente: o SPF só confirma que o servidor pode enviar por aquele domínio, e o domínio é do próprio golpista. Os sinais estão no domínio externo de 2 dias, sem DKIM e sem DMARC. Agora clico em Reportar. A mensagem de retorno diz que o reporte foi recebido às 09:09 e que, no SOC, ele abre um caso."
Atenção: a mensagem é fictícia e inofensiva. Clique em ordem para o contador subir de forma visível; se pular a pista técnica, o contador para em 6.
Conclusão: "Quase todas as pistas usam um princípio de Cialdini, e quem as reconhece reporta. Esse reporte é o que aciona o SOC."
[Tela: gravação do laboratório do slide 8]

**Slide 9 — O que uma simulação ética de *phishing* exige (6:00–6:50)**
Fala: "Simular *phishing* dentro da empresa exige quatro cuidados. Autorização formal da liderança, com RH, jurídico e o encarregado de dados, o DPO. Finalidade educativa: quem clica recebe orientação, e não punição. Proteção de dados: nenhuma senha real é armazenada, e os resultados individuais têm acesso restrito, conforme a LGPD, a Lei Geral de Proteção de Dados. E limites de pretexto: demissões, saúde, salários e tragédias ficam de fora. Repare no quadro azul: uma isca muito fácil gera números enganosamente bons. Por isso o NIST propôs a *Phish Scale*, que classifica a dificuldade da mensagem."

**Slide 10 — Laboratório: uma campanha autorizada, do envio ao bloqueio (6:50–8:20)**
Objetivo: acompanhar a campanha de março do envio ao bloqueio e ver onde entra o reporte.
Na tela:
1. Clicar em "▶ Avançar" para cada uma das sete etapas, lendo o título e o texto na barra inferior.
2. Etapa "09h00 · Envio": Plataforma e Gateway acendem.
3. Etapa "09h00 · O gateway avalia": o pacote segue até "1.000 caixas".
4. Etapa "Os cliques" e etapa "A orientação imediata": "180 cliques" e "Página educativa".
5. Etapa "09h09 · O primeiro reporte": "120 reportes, 1º em 9 min".
6. Etapa "O SOC age": SOC Tatame, Bloqueio geral e a seta tracejada de volta às caixas.
7. Etapa "A leitura da campanha": nó Métricas, "reporte/clique 0,67".
Fala: "A plataforma dispara 1.000 mensagens com o pretexto aprovado, coberto pela autorização da Marina Prado. O *gateway* de *e-mail* vê que o domínio passa no SPF, mas tem 2 dias e não publica DMARC; marca a mensagem como externa e entrega. Então vêm os cliques: 180 pessoas, 18%, e 60 chegam a enviar o formulário simulado, 6%. Quem clica cai na página educativa. Às 09h09, nove minutos depois do envio, alguém reporta; ao todo serão 120 reportes, 12%. O reporte abre um caso, a Luiza Ferraz confirma a campanha e aplica o bloqueio, e a mensagem some das caixas de quem ainda não abriu. Na última etapa, a conta: 120 dividido por 180 dá cerca de 0,67 reporte por clique."
Atenção: cada etapa leva alguns segundos de animação; espere os pacotes chegarem antes de avançar. O botão "Auto" percorre tudo sozinho, mas para gravar é melhor avançar manualmente.
Conclusão: "O reporte rápido é o que permite ao SOC limpar as caixas antes que mais gente clique."
[Tela: gravação do laboratório do slide 10]

**Slide 11 — Laboratório: bastidores de uma campanha autorizada (8:20–9:40)**
Objetivo: mostrar como se planeja e se mede uma campanha sem guardar senhas nem expor pessoas.
Na tela:
1. Na aba "Planejamento", percorrer as linhas: Objetivo, Público, Pretexto aprovado, Pretextos vetados, Dificuldade, Aprovações, Dados e Quem clicar.
2. Clicar em "Resultados" e ler os cinco indicadores.
3. Clicar em "Página educativa".
Fala: "Esta é uma plataforma fictícia, com o mesmo fluxo de ferramentas como o GoPhish. Nenhuma mensagem real sai daqui. No planejamento, o público são 1.000 contas: o *e-mail* da sede e o portal de gestão das 240 academias. O pretexto aprovado é a atualização de cadastro. Os vetados aparecem riscados: demissões, saúde, salários, tragédias e alunos menores. A dificuldade é moderada pela *Phish Scale*. As aprovações têm CISO, RH, jurídico e DPO. Nos dados, senhas não são armazenadas e o resultado individual só é visível à equipe do programa, com descarte em 90 dias. Em Resultados: 1.000 enviados, 180 cliques, 60 submissões, 120 reportes e primeiro reporte em 9 minutos. A diretoria recebe só números agregados. Na página educativa, quem clicou lê que participou de uma simulação, que nada foi guardado, quais eram as pistas e como reportar da próxima vez."
Atenção: a "submissão" é apenas um evento registrado; a página educativa não tem campo de senha. Não mostre nem descreva como montar páginas que coletam credenciais.
Conclusão: "Dá para medir o risco humano com rigor e, ao mesmo tempo, proteger as pessoas que participaram."
[Tela: gravação do laboratório do slide 11]

**Slide 12 — Métricas que importam (9:40–10:20)**
Fala: "Cinco métricas aparecem na tabela: taxa de clique, taxa de submissão de dados, taxa de reporte, tempo até o primeiro reporte e razão reporte/clique. A taxa de reporte costuma ser esquecida, mas é a que mais interessa ao Blue Team. Um único reporte rápido permite bloquear a mensagem para a empresa inteira. Por isso, além de perguntar quem clicou, medimos quanto tempo levou o primeiro aviso."

**Slide 13 — Laboratório: métricas de campanha em Python e SQL (10:20–12:00)**
Objetivo: comparar a campanha de março com a de junho e calcular o tempo até o primeiro reporte sem identificar ninguém.
Na tela:
1. Mostrar o arquivo `campanhas.json` no explorador: duas campanhas de 1.000 envios.
2. Voltar a `metricas.py` e destacar as linhas marcadas.
3. Clicar em "▶ python metricas.py" e esperar a saída no terminal.
4. Abrir `primeiro_reporte.sql`.
5. Clicar em "▶ Consulta SQL".
Fala: "O JSON tem só totais agregados: março com 180 cliques, 60 submissões e 120 reportes; junho, depois de três meses de treinamentos curtos e de um botão de reporte, com 90, 25 e 300. No `metricas.py`, as duas funções no topo formatam porcentagem e decimal com vírgula. O laço percorre as campanhas e divide cada total pelos enviados; a linha que decide a métrica principal é `razao = c["reportes"] / c["cliques"]`. Depois, o segundo laço calcula a variação entre março e junho, e o `if` final testa se há mais reportes que cliques. Na saída, março aparece em vermelho: 18% de clique, 6% de submissão, 12% de reporte e razão 0,67. Junho aparece em verde: 9%, 2,5%, 30% e 3,33. As variações são de menos 50% nos cliques, menos 58% nas submissões e mais 150% nos reportes, e a última linha diz que as pessoas funcionam como sensores. Agora a consulta SQL. O `MIN` com `CASE` pega o primeiro evento do tipo reporte e subtrai a hora do envio; os dois `COUNT(DISTINCT ...)` contam pessoas, sem trazê-las para o resultado. A saída é uma linha: 00:09:00 até o primeiro reporte, 180 cliques e 120 reportes."
Atenção: o código é ilustrativo e a saída é pré-gravada; o editor digita o código ao abrir o slide, então espere a digitação terminar antes de clicar.
Conclusão: "A razão reporte/clique foi de 0,67 para 3,3: a segunda campanha mostra uma equipe que percebe e avisa."
[Tela: gravação do laboratório do slide 13]

**Slide 14 — O rastro técnico e o rastro humano (12:00–12:40)**
Fala: "Do lado técnico, o Blue Team olha cabeçalhos de *e-mail*, domínios recém-registrados e parecidos com o da empresa, falhas no SPF, que diz quais servidores podem enviar pelo domínio, no DKIM, que assina a mensagem, e no DMARC, que diz o que fazer quando os dois falham. Olha também cliques no *proxy*, o intermediário que registra o acesso à web. Do lado humano, o rastro é o reporte do colaborador. O SIEM junta as duas coisas: o reporte confirma o que os registros sugerem."

**Slide 15 — Laboratório: o SOC acompanha a campanha de março (12:40–14:10)**
Objetivo: medir quanto tempo a isca ficou circulando, do envio ao bloqueio.
Na tela:
1. Clicar na busca salva "1. Autenticação de e-mail".
2. Clicar em "2. Cliques no proxy".
3. Clicar em "3. Reportes recebidos".
4. Clicar em "4. Do reporte ao bloqueio".
Fala: "O SOC trata a campanha autorizada como um ataque real, e assim o exercício também mede a defesa. A primeira consulta filtra os *logs* de *e-mail* pelo domínio portal-rh-beneficios.com e conta as mensagens por resultado de SPF, DKIM e DMARC: 1.000 mensagens, SPF *pass*, DKIM e DMARC *none*, domínio de 2 dias. Na plataforma da disciplina, é a regra R1 que liga esse domínio novo ao clique. A segunda consulta conta usuários distintos no *proxy* em janelas de 10 minutos: 62 só entre 09:00 e 09:10, e 180 no acumulado. A maior parte dos cliques acontece nos primeiros minutos. A terceira conta os reportes: o primeiro às 09:09 e 120 no total. A quarta mostra o caso SIM-2026-03: primeiro reporte às 09:09, triagem às 09:14 e bloqueio geral às 09:21, removendo a mensagem de todas as caixas não abertas."
Atenção: a linguagem das consultas é KQL ilustrativa. Leia sempre a nota amarela no rodapé de cada busca.
Conclusão: "Entre o primeiro reporte e o bloqueio passaram 12 minutos. Cada minuto a menos protege quem ainda não abriu a mensagem."
[Tela: gravação do laboratório do slide 15]

**Slide 16 — Laboratório: a campanha vista pelo SOC da plataforma (14:10–16:00)**
Objetivo: ver o que aconteceria num ataque real depois que a Carla digita a senha e medir o tempo de reação do SOC.
Na tela:
1. A plataforma abre na aba "Cenários". No cartão "Phishing simulado no financeiro", clicar em "Iniciar cenário".
2. Acompanhar os passos do cenário: as 40 mensagens, o clique da Carla e a tentativa de *login* na VPN. Se quiser acelerar, trocar a velocidade no seletor do alto (por exemplo, de "1 s = 15 s" para uma mais rápida).
3. Quando o alerta da R1 aparecer, abrir a aba "SOC", abrir o alerta da R1 para investigar e clicar em "Conter". Ler os indicadores MTTD e MTTR no topo.
4. Esperar o alerta da R11 sobre `svc-backup`, investigar e marcar "Falso positivo".
Fala: "Agora estamos no simulador da disciplina. O cenário reproduz a campanha contra o financeiro: 40 mensagens e o clique da Carla. O clique vira alerta pela regra R1, que liga o domínio recém-criado ao acesso. Em seguida, a senha digitada é testada na VPN, e o MFA, o segundo fator de *login*, bloqueia a entrada. Na aba SOC, investigo o alerta da R1 e contenho. Repare nos dois indicadores: MTTD é o tempo médio até detectar, e MTTR é o tempo médio até responder. Logo depois aparece um alerta da R11 sobre a conta `svc-backup`. Ao investigar, vemos que é rotina de *backup*, então marcamos como falso positivo. Esse também é um trabalho do SOC: separar o que é ataque do que é ruído."
Atenção: o simulador mede o SOC; cliques e reportes da campanha vêm da plataforma de simulação do slide 11. Conter um alerta cancela os passos pendentes do cenário; se quiser repetir, clique de novo em "Iniciar cenário". O botão "Reiniciar" volta regras e fontes ao padrão.
Conclusão: "A senha vazou, mas o MFA e o SOC seguraram o ataque."
[Tela: gravação do laboratório do slide 16]

**Slide 17 — Exemplo numérico: lendo duas campanhas de 1.000 mensagens (16:00–16:40)**
Fala: "Juntando tudo na tabela: cliques de 180 para 90, submissões de 60 para 25 e reportes de 120 para 300. A razão reporte/clique vai de 120 dividido por 180, cerca de 0,67, para 300 dividido por 90, cerca de 3,3. No gráfico, as barras vermelhas mostram a queda e a verde mostra a alta dos reportes. Depois de três meses de treinamentos curtos e de um botão de reporte, há mais de três reportes para cada clique."

**Slide 18 — Pausa para reflexão: o pedido do hospital (16:40–17:10)**
Fala: "Agora um caso fora da Tatame. Um hospital com 2.500 colaboradores pede uma simulação com o tema 'resultado de exames de colaboradores com covid' e quer a lista nominal de quem clicou para aplicar advertências. Pause o vídeo e pense: que riscos éticos e legais esse pedido traz, considerando a LGPD e o bem-estar das pessoas? Que tema você proporia? E que métricas apresentaria no lugar da lista?"
[Take de apoio: corredor de hospital com profissionais de saúde — Envato]

**Slide 19 — Laboratório: planejador de campanha para o hospital (17:10–18:10)**
Objetivo: montar um plano de uma página que respeite as regras de engajamento.
Na tela:
1. Em "Pretexto", clicar primeiro em "Resultado de exames de colaboradores com covid" e ler a avaliação no plano à direita. Depois trocar para "Nova escala de plantões publicada no sistema de RH".
2. Em "O que a diretoria recebe", clicar em "Lista nominal de quem clicou", ler o ✗, e trocar para "Métricas agregadas por área: clique, submissão, reporte e tempo até o 1º reporte".
3. Em "Quem clicar", escolher "Vê a página educativa na hora e faz um microtreinamento".
4. Em "Dados digitados no formulário", escolher "Registrar só o evento de submissão; nada do que foi digitado é guardado". O indicador chega a "4 de 4".
Fala: "Cada escolha aparece no plano com um ✓ ou um ✗ e a justificativa. O tema de saúde causa angústia real e envolve dado sensível; a escala de plantões é plausível e faz parte da rotina. A lista nominal expõe resultado individual sem necessidade e desestimula o reporte; as métricas agregadas mostram a capacidade de detecção sem expor ninguém. Advertência formal gera medo de reportar; a página educativa ensina no momento do erro. E guardar o que foi digitado é risco grave, desnecessário para a métrica."
Atenção: mostre primeiro uma escolha errada em pelo menos duas decisões, para o aluno ver a avaliação negativa.
Conclusão: "Punir quem clica faz as pessoas pararem de reportar, e o SOC perde o sensor mais rápido que tem."
[Tela: gravação do laboratório do slide 19]

**Slide 20 — De volta ao problema (18:10–19:00)**
Fala: "Voltemos à pergunta da aula: quando um *e-mail* falso chega, as pessoas da Tatame percebem e avisam o SOC a tempo? Os laboratórios responderam por partes. A caixa de entrada mostrou 7 pistas, quase todas de autoridade ou urgência. A plataforma de simulação mediu cliques e submissões sem guardar senhas. No SIEM, o primeiro reporte chegou 9 minutos após o envio, e o bloqueio veio 12 minutos depois. E o script mostrou que os reportes foram de 12% para 30%, com 3,3 reportes por clique; no simulador, que reproduz o ataque real, o MFA barrou a senha na VPN. A resposta, então, é sim, e cada vez mais: na campanha de março, 120 pessoas avisaram e o SOC removeu a isca 12 minutos após o primeiro reporte. Três meses depois, há mais de três reportes para cada clique."

**Slides 21 a 23 — Pontos-chave, referências e encerramento (19:00–19:40)**
Fala: "Para levar: a engenharia social explora princípios de persuasão como autoridade e urgência; o *phishing*, T1566, é um dos vetores de acesso inicial mais usados; simulações autorizadas são educativas, protegem os dados e evitam pretextos danosos; e a taxa de reporte e o tempo até o primeiro reporte medem a detecção humana. O clique é só o começo. Na próxima aula, veremos o que o Grupo Cobalto Austral faria depois de entrar na sede da Tatame e como o Red Team conta essa história no relatório."
[Slides: referências exibidas por 5 segundos, sem leitura em voz alta.]

## Aula 8 — Pós-exploração, movimentação lateral e relatório de Red Team

### Texto base

O acesso inicial raramente é o objetivo final. Um *e-mail* clicado ou um servidor vulnerável dá ao adversário um ponto de apoio em uma única máquina, muitas vezes com privilégios limitados. O que transforma esse ponto de apoio em um incidente grave é a **pós-exploração**: tudo o que acontece depois da entrada, até que o objetivo — dados, controle do domínio, interrupção do negócio — seja alcançado. Nesta aula, tratamos essa fase de forma conceitual, como o Red Team a documenta e como o Blue Team a enxerga.

#### As etapas da pós-exploração

Na matriz ATT&CK, a pós-exploração abrange várias táticas que costumam se repetir em ciclos:

| Tática ATT&CK | Objetivo do adversário | Exemplo de técnica | Rastro típico para o Blue Team |
|---|---|---|---|
| Persistência (TA0003) | Manter o acesso após reinicializações | T1053 — *Scheduled Task/Job* | Criação de tarefas agendadas incomuns |
| Escalada de privilégios (TA0004) | Obter permissões mais altas | T1068 — *Exploitation for Privilege Escalation* | Processos com privilégio elevado a partir de usuário comum |
| Acesso a credenciais (TA0006) | Obter senhas, *hashes* e tíquetes | T1003.001 — *LSASS Memory*; T1558.003 — *Kerberoasting* | Acessos ao processo LSASS; pedidos anômalos de tíquetes Kerberos |
| Descoberta (TA0007) | Mapear usuários, grupos e servidores | T1087 — *Account Discovery* | Consultas volumosas ao diretório |
| Movimentação lateral (TA0008) | Saltar para outras máquinas | T1021 — *Remote Services*; T1550.002 — *Pass the Hash* | *Logons* remotos fora do padrão |
| Comando e controle (TA0011) | Manter comunicação com o operador | T1071 — *Application Layer Protocol* | Conexões periódicas (*beaconing*) a domínios raros |

Ferramentas conhecidas, catalogadas no próprio ATT&CK, ilustram essas táticas. O **Mimikatz** (S0002) tornou-se símbolo do acesso a credenciais em ambientes Windows, e sua presença é um dos comportamentos mais monitorados por soluções de EDR. *Frameworks* de comando e controle, comerciais ou de código aberto, oferecem aos operadores um canal para coordenar a operação. Conhecer esses nomes ajuda o defensor a reconhecê-los em relatórios de inteligência.

[Imagem 1 — Diagrama de uma rede corporativa com uma estação comprometida e setas indicando saltos sucessivos até um controlador de domínio. Texto alternativo: "Diagrama de movimentação lateral de uma estação de trabalho até o controlador de domínio". Sugestão de busca no Envato: "network diagram lateral movement".]

#### Credenciais válidas: o atalho preferido

Muitos adversários modernos evitam *malware* sofisticado e preferem usar **contas válidas** (T1078 — *Valid Accounts*): com uma credencial legítima, suas ações se misturam às dos administradores. Por isso, a proteção de contas privilegiadas — segundo fator, separação entre contas administrativas e de uso diário, acesso privilegiado sob demanda — é uma das recomendações mais frequentes em relatórios de Red Team.

#### Caminhos de ataque e o pensamento em grafos

Em ambientes Active Directory, as permissões formam uma rede de relações: o usuário A administra a máquina B, onde o administrador C costuma fazer *logon*, e C pertence a um grupo com controle sobre o domínio. O **BloodHound** representa essas relações como um **grafo** e calcula **caminhos de ataque** até ativos críticos, como o grupo *Domain Admins*. A mesma visão serve à defesa: eliminar uma única relação mal configurada pode cortar dezenas de caminhos de uma só vez. Vale aqui a frase atribuída a John Lambert, da Microsoft: os defensores pensam em listas, os atacantes pensam em grafos.

[Imagem 2 — Grafo com nós de usuários, computadores e grupos, destacando em vermelho o caminho mais curto até o grupo de administradores do domínio. Texto alternativo: "Grafo de caminhos de ataque no Active Directory com o caminho crítico destacado". Pode ser recriado pela equipe de produção.]

#### Limites da pós-exploração em um engajamento

As regras de engajamento definem até onde a equipe pode ir: em geral, o **impacto é demonstrado, e não executado**. Em vez de exfiltrar a base de clientes, o Red Team registra uma evidência de que teria acesso a ela, como uma captura de tela da estrutura da tabela; em vez de criptografar servidores, documenta que tinha os privilégios para isso. Credenciais obtidas são protegidas e invalidadas ao final, e dados pessoais encontrados são tratados conforme a LGPD. Persistências e contas criadas devem ser **removidas** na limpeza pós-operação, com registro do que foi feito.

#### O relatório de Red Team

O relatório é o principal entregável e precisa servir a dois públicos. Uma estrutura comum inclui: **sumário executivo**, com objetivos, resultado e riscos em linguagem de negócio; **narrativa do ataque**, com a linha do tempo de cada etapa; **achados**, com evidências, severidade e técnica ATT&CK correspondente; **análise de detecção e resposta**, indicando o que foi detectado, quando e o que passou despercebido; e **recomendações priorizadas**. A linha do tempo detalhada permite ao Blue Team comparar, minuto a minuto, o que o Red Team fez com o que os registros mostram — base para o *purple teaming* da Unidade 4.

[Imagem 3 — Linha do tempo de uma operação com marcos de acesso inicial, escalada, movimentação lateral e objetivo, e ícones indicando quais etapas foram detectadas. Texto alternativo: "Linha do tempo de uma operação de Red Team com etapas detectadas e não detectadas". Sugestão de busca no Envato: "timeline infographic red green".]

#### Exemplo numérico: cortando caminhos

Em um domínio com 5.000 contas de usuário, a análise de grafo mostra que 1.200 delas (**24%**) têm algum caminho até o grupo de administradores do domínio. Quase todos esses caminhos passam por dois servidores em que administradores fazem *logon* rotineiramente e por um grupo de suporte com permissões excessivas. Após corrigir esses três pontos, restam 40 contas com caminho, isto é, 40 ÷ 5.000 = **0,8%** — uma redução de 1.160 ÷ 1.200 ≈ **97%** dos caminhos. Na mesma operação, das 12 técnicas executadas, o SOC detectou 4, uma taxa de detecção de 4 ÷ 12 ≈ **33%**: um número que o relatório deve destacar como ponto de partida para a melhoria.

#### O que você verá na próxima unidade

Na Unidade 3, vamos trocar a camisa vermelha pela azul. Cada rastro que mencionamos nesta unidade — varreduras nos registros de *firewall*, cliques no *proxy*, acessos ao LSASS, *logons* remotos fora do padrão — vira matéria-prima da defesa. Você vai estudar telemetria, registros e SIEM; a engenharia de detecção e o EDR; o *threat hunting* apoiado por inteligência de ameaças; e a resposta a incidentes, do primeiro alerta às lições aprendidas.

#### Pontos-chave

- A pós-exploração transforma um ponto de apoio em impacto real, em ciclos de descoberta, credenciais e movimentação.
- Contas válidas (T1078) permitem que o adversário se misture aos usuários legítimos.
- Pensar em grafos revela caminhos de ataque e mostra onde uma correção corta muitos deles.
- O relatório de Red Team narra o ataque, mapeia técnicas ATT&CK e mede o que a defesa detectou.

### Referências da aula

LAMBERT, John. *Defenders think in lists. Attackers think in graphs. As long as this is true, attackers win*. 2015. Disponível em: <https://github.com/JohnLaTwC/Shared/blob/master/Defenders%20think%20in%20lists.%20Attackers%20think%20in%20graphs.%20As%20long%20as%20this%20is%20true%2C%20attackers%20win.md>. Acesso em: 13 nov. 2026.

MITRE. *Lateral movement (TA0008)*. In: MITRE ATT&CK. Disponível em: <https://attack.mitre.org/tactics/TA0008/>. Acesso em: 13 nov. 2026.

MITRE. *Valid accounts (T1078)*. In: MITRE ATT&CK. Disponível em: <https://attack.mitre.org/techniques/T1078/>. Acesso em: 13 nov. 2026.

NATIONAL INSTITUTE OF STANDARDS AND TECHNOLOGY. *SP 800-115: technical guide to information security testing and assessment*. Gaithersburg: NIST, 2008.

WEIDMAN, Georgia. *Testes de invasão: uma introdução prática ao hacking*. São Paulo: Novatec, 2014.

### Roteiro da Videoaula 8 — "Da recepção ao controlador de domínio: até onde o adversário chega"

Duração-alvo: 15 a 20 minutos. Deck: unidade_2/slides/aula8.html (23 slides).

**Slides 1 a 3 — Capa, audiodescrição e sumário (0:00–0:40)**
Fala: "Olá! Esta é a última aula da Unidade 2, e hoje vamos acompanhar o adversário depois que ele já entrou. Vamos ver o caminho que ele percorre dentro da rede, o rastro que deixa e como o Red Team transforma tudo isso em um relatório. Como sempre, tudo acontece na Rede Tatame, a nossa rede fictícia de academias."
[Câmera: professor em plano médio. Na audiodescrição, apenas mostrar o slide por alguns segundos.]

**Slide 4 — O problema de hoje na Rede Tatame (0:40–2:00)**
Fala: "A CISO Marina Prado pediu ao Red Team de Bruno Sato uma emulação do Grupo Cobalto Austral, o adversário fictício dos nossos exercícios. O ponto de partida combinado foi o notebook da recepção da sede, o NB-REC-001, como se um *e-mail* falso tivesse funcionado. A pergunta que vamos responder até o fim da aula está aqui em amarelo: até onde um adversário chega a partir da recepção, e quanto disso o SOC, o centro de operações de segurança da Tatame, enxerga? No mapa à direita, o caminho em vermelho vai do notebook ao servidor de arquivos e dali ao controlador do Active Directory, o AD, que é o diretório onde ficam as contas e as permissões. O que está em jogo é grande: quem controla o domínio controla o SRV-ARQ-01, com fichas de alunos menores, e o ERP financeiro."
[Take de apoio: recepção de academia com computador no balcão — Envato.]

**Slide 5 — Do ponto de apoio ao impacto (2:00–2:50)**
Fala: "O acesso inicial raramente é o objetivo final. Um clique dá ao adversário uma única máquina, muitas vezes com um usuário sem privilégios. O que transforma esse ponto de apoio em incidente grave é a pós-exploração: tudo o que acontece depois da entrada até o objetivo, seja ele dados, controle do domínio ou interrupção do negócio. Pense em um molho de chaves: quem tem a chave da sala onde está guardada a chave-mestra não precisa arrombar nada. Nesta aula tratamos essa fase de forma conceitual, olhando como o Red Team a documenta e como o Blue Team a enxerga."

**Slide 6 — As táticas da pós-exploração no ATT&CK (2:50–3:50)**
Fala: "Esta tabela organiza a pós-exploração pelas táticas do MITRE ATT&CK. Leia sempre a última coluna: é o rastro típico que cada tática deixa para o Blue Team. Persistência deixa tarefas agendadas incomuns. Acesso a credenciais deixa acessos ao processo LSASS, que é o processo do Windows que guarda credenciais na memória, e pedidos anômalos de tíquetes de serviço Kerberos. Descoberta deixa consultas volumosas ao diretório. Movimentação lateral deixa *logons* remotos fora do padrão. E comando e controle deixa conexões periódicas, o chamado *beaconing*. Repare que essas táticas se repetem em ciclos: descobrir, obter credenciais, mover-se e descobrir de novo."

**Slide 7 — Ferramentas conhecidas e contas válidas (3:50–4:30)**
Fala: "Alguns nomes de ferramentas aparecem tanto em relatórios de inteligência que o defensor precisa reconhecê-los, e as soluções de EDR, que vigiam processos e memória nas máquinas, monitoram justamente esses comportamentos. Mas muitos adversários preferem algo mais simples: contas válidas, a técnica T1078. Com uma credencial legítima, as ações se misturam às dos administradores. Por isso os relatórios recomendam segundo fator, contas administrativas separadas das de uso diário e acesso privilegiado sob demanda."

**Slide 8 — Laboratório: da recepção ao controlador de domínio (4:30–6:30)**
Objetivo: mostrar o caminho completo do adversário na sede e o rastro esperado em cada etapa, o primeiro pedaço da resposta sobre até onde ele chega.
Na tela:
1. Mostrar o diagrama parado: na linha de cima, NB-REC-001, Diretório, SRV-ARQ-01 e SRV-AD-01; embaixo, Operador, EDR, SIEM e Revisão purple.
2. Clicar em "Avançar" para o passo 1, "Ponto de apoio": acende só o NB-REC-001.
3. "Avançar" para o passo 2, "Descoberta (TA0007)": a seta vermelha vai do notebook ao Diretório.
4. "Avançar" para o passo 3, "Credenciais (TA0006)": a ligação azul com o EDR indica que houve alerta.
5. "Avançar" para o passo 4, "Movimentação lateral (TA0008)": seta vermelha até o SRV-ARQ-01 e o SIEM marcado em âmbar, sem alerta.
6. "Avançar" pelos passos 5, "Credenciais de novo", 6, "Contas válidas (T1078)", e 7, "Comando e controle (TA0011)".
7. Terminar no passo 8, "Revisão purple", com o contador em 8/8.
Fala: "Leia a legenda de cada passo embaixo do diagrama. No passo 1, um *e-mail* clicado dá ao adversário uma sessão no NB-REC-001 com um usuário comum. No passo 2 ele mapeia usuários, grupos e servidores de corp.tatame.local; o rastro esperado são consultas volumosas ao AD a partir de uma estação comum, a regra R13 na plataforma. No passo 3, um técnico de suporte tinha feito *logon* nessa máquina, e o material de autenticação dele ficou na memória; aqui o EDR alertou, por isso a linha é azul. No passo 4, com a conta do suporte, o adversário faz *logon* remoto no SRV-ARQ-01. O suporte nunca faz isso a partir da recepção, e mesmo assim ninguém viu: o SIEM fica âmbar. No passo 5, um administrador do domínio faz *logon* rotineiramente nesse servidor, e a credencial dele é a chave-mestra; os pedidos anômalos de tíquetes geraram alerta no SIEM. No passo 6, o acesso ao SRV-AD-01 parece trabalho normal. No passo 7, a estação conversou com o operador em intervalos regulares o dia todo, e isso estava nos registros sem regra. No passo 8, Red e Blue comparam tudo: 4 de 12 técnicas detectadas."
Atenção: o diagrama é conceitual e não mostra como executar nenhuma técnica. O botão "Auto" avança sozinho; na gravação, prefira "Avançar" para controlar o tempo da fala. Azul significa alerta; âmbar significa evento registrado sem alerta.
Conclusão: "Da recepção ao controlador de domínio são poucas etapas, e em duas delas a defesa tinha o evento, mas não tinha a regra."
[Tela: gravação do laboratório do slide 8.]

**Slide 9 — Defensores pensam em listas, atacantes em grafos (6:30–7:10)**
Fala: "No Active Directory, as permissões formam uma rede de relações: o usuário A administra a máquina B, onde o administrador C costuma fazer *logon*, e C pertence a um grupo que controla o domínio. O BloodHound representa essas relações como um grafo e calcula caminhos de ataque até ativos críticos, como o grupo *Domain Admins*. A defesa pode usar a mesma visão: eliminar uma única relação mal configurada pode cortar dezenas de caminhos de uma vez."
[Take de apoio: quadro de investigação com fios ligando fotos — Envato.]

**Slide 10 — Laboratório: o grafo do diretório e o caminho até *Domain Admins* (7:10–8:50)**
Objetivo: descobrir quais relações, se cortadas, eliminam mais caminhos até o topo.
Na tela:
1. Mostrar a cena parada: embaixo os usuários, no meio grupos e computadores, no topo o losango amarelo de *Domain Admins*. No painel do canto, "10 de 11 usuários comuns com caminho" e "rec.ana: 7 saltos".
2. Arrastar para girar a cena e seguir as arestas vermelhas de rec.ana: TODOS-SEDE, NB-REC-001, SUPORTE-N1, SRV-ARQ-01, adm.caio e *Domain Admins*.
3. Clicar em "Cortar sessão no SRV-ARQ-01". O painel passa para 3 de 11, e rec.ana fica sem caminho.
4. Clicar em "Cortar sessão no SRV-ERP-01". O painel cai para 1 de 11.
5. Clicar em "Cortar admin do NB-REC-001". O painel continua em 1 de 11.
6. Clicar em "Restaurar" e voltar aos 10 de 11.
Fala: "Cada esfera vermelha é um usuário comum que tem algum caminho até o topo; azul é quem não tem. São 11 usuários comuns, porque o adm.caio já está no grupo de administradores e não entra na conta. O caminho de rec.ana, a recepcionista, tem 7 saltos e passa por uma sessão do adm.caio no SRV-ARQ-01. Quando eu corto essa sessão, sete usuários perdem o caminho de uma vez. Quando corto a sessão no SRV-ERP-01, caem os dois desenvolvedores. O terceiro corte tira do grupo TODOS-SEDE o acesso administrativo ao notebook da recepção. Ele não muda o número agora, porque os outros cortes já isolaram esses usuários, mas fecha a porta de entrada por outro lado. Sobra um usuário, a atd.elisa, que chega ao topo por um grupo antigo chamado LEGADO-ERP."
Atenção: nenhuma técnica de ataque é executada; a cena apenas lê relações de permissão e calcula caminhos. Os rótulos de trás ficam menores por causa da perspectiva; gire a cena antes de ler um nome.
Conclusão: "Poucas correções bem escolhidas cortam quase todos os caminhos da recepção ao domínio."
[Tela: gravação do laboratório do slide 10.]

**Slide 11 — Laboratório: menor caminho por busca em largura (8:50–10:30)**
Objetivo: contar, com código, quantos usuários chegam a *Domain Admins* antes e depois das correções.
Na tela:
1. Com caminhos.py aberto, destacar a função menor_caminho.
2. Abrir grafo.json no explorador e mostrar a lista "arestas".
3. Clicar em "Antes das correções" e esperar a saída no terminal.
4. Abrir correcoes.json, com as três relações removidas.
5. Clicar em "Depois das correções" e ler a saída.
Fala: "O grafo da cena 3D está agora em JSON. Cada aresta tem três partes: origem, relação e destino, como 'rec.ana, MemberOf, TODOS-SEDE'. As relações são quatro: MemberOf é ser membro de um grupo, AdminTo é ser administrador de uma máquina, HasSession é ter uma sessão aberta nela e GenericAll é ter controle total sobre um objeto. No código, o primeiro bloco lê o grafo e, se eu passar um arquivo na linha de comando, lê também as arestas removidas. O laço seguinte monta a lista de vizinhos e pula as removidas: é essa linha que faz a correção ter efeito. A função menor_caminho é uma busca em largura, a BFS. Ela usa uma fila: visita primeiro os vizinhos a um salto, depois a dois, e assim por diante. Por isso o primeiro caminho que encontra até o alvo é sempre o mais curto. Na saída de antes, o terminal mostra 10 de 11, ou 91%: a atd.elisa com 3 saltos, os dois do suporte e os dois desenvolvedores com 4, e cinco usuários com 7 saltos, entre eles a rec.ana. Depois das correções, com 3 arestas removidas, sobra 1 de 11, ou 9%, e o próprio script avisa que a próxima correção é o grupo LEGADO-ERP."
Atenção: o terminal é simulado e mostra uma saída já gravada; o código é real e pode ser rodado em casa com os mesmos arquivos. É o mesmo grafo da cena 3D, por isso os números batem.
Conclusão: "Com o cálculo, a Tatame mostra o efeito de cada correção antes de aplicá-la."
[Tela: gravação do laboratório do slide 11, com zoom na função menor_caminho.]

**Slide 12 — Laboratório: que evento deveria existir em cada etapa (10:30–12:00)**
Objetivo: separar as etapas que viraram alerta das que ficaram só nos registros, a parte da pergunta sobre o que o SOC enxerga.
Na tela:
1. Clicar na busca salva "1. Logon remoto atípico".
2. Clicar em "2. Acesso à memória do LSASS".
3. Clicar em "3. Pedido anômalo de tíquetes".
4. Clicar em "4. Conexões periódicas".
Fala: "O SOC revisa o dia da operação no SIEM, a central que reúne os registros, com a linha do tempo do Red Team em mãos. A busca 1 filtra *logons* do tipo 10, que é o remoto interativo, com origem em máquinas da recepção e destino em servidores. Aparece um evento às 13:20:44: sup.heitor, do NB-REC-001 para o SRV-ARQ-01, e a coluna 'alerta?' diz 'não'. O evento estava lá, mas não havia regra; na plataforma, essa regra é a R5 e vem desligada. A busca 2 procura processos fora de uma lista aprovada abrindo a memória do LSASS: às 14:05:12, um atualizador.exe rodando de uma pasta pública, com severidade crítica. Esse o EDR pegou. A busca 3 conta quantos serviços diferentes uma conta pediu em dez minutos, com criptografia antiga: sup.heitor pediu 27, com RC4, e o SIEM alertou. A busca 4 procura um padrão regular de conexões: 540 conexões para cdn-atualiza.example.org, uma a cada 60 segundos, com desvio de 2 segundos. Repare no histograma, todo igual. Estava nos registros, sem regra."
Atenção: as consultas estão escritas em uma linguagem parecida com KQL só para ilustrar o filtro; o professor não precisa explicar a sintaxe, apenas o que cada linha seleciona.
Conclusão: "Duas etapas viraram alerta e duas ficaram guardadas nos registros sem que ninguém fosse avisado."
[Tela: gravação do laboratório do slide 12.]

**Slide 13 — Laboratório: a movimentação lateral na plataforma (12:00–14:00)**
Objetivo: ver a emulação inteira na plataforma e medir o que muda com duas regras novas.
Na tela:
1. Na aba "Cenários", clicar em "Iniciar cenário" no cartão "Emulação do Grupo Cobalto Austral". Deixar a velocidade em "1 s = 15 s"; a cadeia leva cerca de um minuto até o impacto.
2. Acompanhar os passos: login na VPN com a senha vazada de caio.mendes, sem MFA; consulta em massa ao AD; RDP para o SRV-ARQ-01; leitura da memória do LSASS; RDP para o SRV-ERP-01; cópia de 4,2 GB de exportações de fichas; exclusão das cópias de sombra; impacto nos servidores da sede.
3. Abrir "Regras do CEP" e ligar a R5 e a R13. Voltar a "Cenários" e clicar de novo em "Iniciar cenário".
4. Abrir a última aba, "Cobertura ATT&CK", e conferir T1021.001 e T1087.002.
5. Iniciar o cenário mais uma vez. Na aba "SOC", assim que surgir o alerta novo de caio.mendes, investigar e clicar em "Conter".
Fala: "Na primeira rodada, a consulta ao AD e os dois RDPs aparecem como 'visto nos logs, sem alerta', porque a R13 e a R5 estão desligadas. O CEP, o motor que correlaciona eventos, simplesmente não tinha regra para eles. Quando ligo as duas regras e repito, esses passos passam a gerar alerta, e na aba de cobertura as técnicas T1021.001, de serviços remotos, e T1087.002, de descoberta de contas do domínio, passam a comprovadas. Na terceira rodada, eu contenho o alerta de caio.mendes logo que ele aparece. Quando o SOC contém um alerta, os passos seguintes do cenário são cancelados, e o impacto não acontece."
Atenção: "Iniciar cenário" mantém as regras que você ligou; o botão "Reiniciar" volta tudo ao padrão e desliga a R5 e a R13. Se quiser encurtar a gravação, troque a velocidade para "1 s = 1 min", mas na terceira rodada volte para "1 s = 15 s" para dar tempo de conter. Em telas pequenas, a aba "Cobertura ATT&CK" fica no fim da barra de abas.
Conclusão: "Com duas regras a mais e uma contenção rápida, a emulação para antes de chegar ao impacto."
[Tela: gravação do laboratório do slide 13, com as três rodadas.]

**Slide 14 — Limites da pós-exploração em um engajamento (14:00–14:40)**
Fala: "As regras de engajamento definem até onde a equipe vai, e em geral o impacto é demonstrado, e não executado. Em vez de exfiltrar as fichas de alunos, o Red Team registra evidência de que teria acesso a elas. Em vez de criptografar servidores, documenta que tinha os privilégios para isso. Credenciais obtidas são protegidas e invalidadas no fim, e tudo o que foi criado é removido na limpeza. As fichas de alunos menores do SRV-ARQ-01 são tratadas conforme a LGPD, e a PagaFácil fica fora do escopo."

**Slide 15 — O relatório de Red Team serve a dois públicos (14:40–15:10)**
Fala: "O relatório tem cinco seções: sumário executivo em uma página para a diretoria, narrativa do ataque, achados com técnica ATT&CK, detecção e resposta e recomendações priorizadas. A linha do tempo detalhada é o que permite ao Blue Team comparar, minuto a minuto, o que o Red Team fez com o que os registros mostram."

**Slide 16 — Laboratório: do registro da operação ao relatório (15:10–16:20)**
Objetivo: gerar o rascunho do relatório e calcular a taxa de detecção a partir do próprio registro.
Na tela:
1. Com operacao.yaml aberto, mostrar o código OP-2026-11-TATAME e a lista linha_do_tempo.
2. Abrir gerar_relatorio.py e destacar as linhas de detectadas e taxa.
3. Clicar em "Gerar relatório".
4. Ler a saída no terminal e mostrar o relatorio.md que abre em seguida.
Fala: "Durante a operação, cada técnica foi registrada com hora, tática, identificador ATT&CK e um campo 'detectada', verdadeiro ou falso. O script lê esse arquivo, separa as técnicas detectadas e divide pelo total. Essa linha decide o número que vai para o sumário executivo. A saída mostra 12 técnicas executadas, 4 detectadas e taxa de 33%, e lista as oito lacunas, como o RDP para o SRV-ARQ-01 às 13:20 e as conexões periódicas às 16:45. O relatorio.md traz o sumário, a tabela com 'sim' ou 'NÃO' em cada linha e as quatro recomendações priorizadas, começando por remover as sessões de administradores do domínio dos servidores comuns."
Atenção: o registro e o relatório são fictícios. A linha da coleta às 17:30 diz "evidência", porque o impacto foi demonstrado e não executado.
Conclusão: "O relatório conta o ataque e mostra, com números, o que a defesa perdeu."
[Tela: gravação do laboratório do slide 16.]

**Slide 17 — Laboratório: 12 técnicas, 4 detecções (16:20–17:10)**
Objetivo: localizar as lacunas de detecção na linha do tempo da operação.
Na tela:
1. Clicar no marco 6, das 13:20, e ler o rastro que poderia ter sido usado.
2. Clicar no marco 7, das 14:05, que está verde.
3. Clicar no filtro "Só não detectadas".
4. Clicar em "Todas" para voltar.
Fala: "Verde é técnica detectada e vermelho é técnica que passou despercebida. No marco 6, o rastro que poderia ter sido usado é o *logon* remoto do tipo 10 do suporte a partir da recepção, o mesmo evento da busca 1 do SIEM. O marco 7 é o LSASS que o EDR detectou. Com o filtro, sobram os oito pontos vermelhos. Os indicadores embaixo resumem a operação: 12 técnicas executadas, 4 detectadas, 33%."
Conclusão: "Cada ponto vermelho é uma regra a criar na Unidade 3."
[Tela: gravação do laboratório do slide 17.]

**Slide 18 — Exemplo numérico: cortando caminhos e medindo a detecção (17:10–17:50)**
Fala: "Agora em escala maior. Em um domínio com 5.000 contas, 1.200 têm algum caminho até os administradores do domínio: 24%. Quase todos passam por dois servidores com *logon* rotineiro de administradores e por um grupo de suporte com permissões excessivas. Corrigidos esses três pontos, restam 40 contas com caminho, 0,8%, e 97% dos caminhos foram cortados. E a taxa de detecção de 33% entra no relatório como ponto de partida para a melhoria."

**Slide 19 — Unidade 3: da camisa vermelha para a azul (17:50–18:20)**
Fala: "Cada rastro desta unidade vira matéria-prima da defesa: varreduras nos registros de *firewall*, cliques no *proxy*, acessos ao LSASS e *logons* remotos fora do padrão. Na Unidade 3 vamos ver telemetria e SIEM, engenharia de detecção e EDR, *threat hunting* e resposta a incidentes."

**Slide 20 — De volta ao problema (18:20–19:10)**
Fala: "Voltemos à pergunta da aula: até onde um adversário chega a partir da recepção, e quanto disso o SOC enxerga? O diagrama e o grafo mostraram a rota até o controlador de domínio, com 7 saltos no caminho de rec.ana. O script mostrou que três correções levam de 10 para 1 usuário com caminho. O relatório e a linha do tempo mostraram que o SOC viu 4 de 12 técnicas, 33%. E na plataforma, com a R5 e a R13 ligadas e o alerta contido a tempo, o impacto não aconteceu. A resposta, então: a partir da recepção, o adversário chega ao controlador de domínio, e o SOC viu só um terço do caminho. Cortar três relações no AD e criar regras para as lacunas fecham a maior parte dele."

**Slides 21 a 23 — Pontos-chave, referências e encerramento (19:10–19:50)**
Fala: "Para levar desta aula: a pós-exploração transforma um ponto de apoio em impacto; contas válidas misturam o adversário aos usuários legítimos; pensar em grafos mostra onde uma correção corta muitos caminhos; e o relatório mede o que a defesa detectou. Com isso fechamos a Unidade 2. Na Unidade 3, vamos vestir a camisa azul e montar, na plataforma da Tatame, a defesa que detecta cada um desses passos, começando pela Aula 9, sobre telemetria, registros e SIEM. Até lá!"
[Câmera: professor em plano médio para o fechamento. Envato: "keychain master key", "security operations center blue screens".]

## Quiz não avaliativo

### Questão 1 (verdadeiro ou falso)

Uma vulnerabilidade com nota CVSS 9,8 deve sempre ser corrigida antes de uma vulnerabilidade com nota CVSS 7,5, pois a nota CVSS expressa o risco que cada falha representa para a organização.

( ) Verdadeiro  
(X) Falso

### Questão 2 (múltipla escolha)

Uma empresa realizou duas simulações autorizadas de *phishing* com dificuldade equivalente. Qual indicador mostra melhor a evolução da capacidade da organização de **detectar** a ameaça?

a) O número total de mensagens enviadas em cada campanha.  
b) A taxa de abertura das mensagens.  
*c) A taxa de reporte e o tempo até o primeiro reporte.  
d) A lista nominal dos colaboradores que clicaram.

### Feedback

**Questão 1 — Falso.** A nota-base do CVSS mede a severidade técnica da falha, e não o risco. A priorização por risco também considera a probabilidade de exploração (EPSS), a existência de exploração confirmada (catálogo KEV da CISA) e a exposição e a criticidade do ativo. Uma falha 7,5 em um portal exposto à internet, presente no KEV e com EPSS alto, pode ser muito mais urgente do que uma falha 9,8 em um servidor interno isolado.

**Questão 2 — Alternativa c.** A taxa de reporte e o tempo até o primeiro reporte medem a capacidade de as pessoas perceberem a mensagem suspeita e acionarem a defesa — um único reporte rápido permite ao SOC bloquear a mensagem para toda a empresa. O volume enviado não mede desempenho, a taxa de abertura é imprecisa e pouco informativa, e a lista nominal para punição, além de levantar questões de proteção de dados, tende a desestimular o reporte.

## Material complementar

### Direto da fonte (livro da Biblioteca Virtual)

- **Texto provocativo:** Por que um invasor gastaria semanas procurando uma falha técnica se pode simplesmente pedir a senha a alguém? Escrito por profissionais brasileiros de segurança ofensiva, o capítulo indicado mostra como pretexto, urgência e autoridade são explorados em ataques de engenharia social — e como um *red team* autorizado reproduz essas técnicas de forma ética para medir a resiliência das pessoas e dos processos. É leitura essencial para quem vai planejar simulações de *phishing* com responsabilidade.
- **Nome do livro:** SOARES, Cleber; FRANCO, Deivison Pinheiro; SANTOS, Joas Antonio dos. *Introdução à segurança ofensiva*: uma abordagem para pentesters e red teams. Rio de Janeiro: Brasport, 2023. *E-book*.
- **Capítulo:** 3 — Técnicas de engenharia social
- **Link de acesso:** <https://plataforma.bvirtual.com.br/Acervo/Publicacao/213767>
- **Aula em que entra:** Aula 7

### Para mergulhar no assunto (saiba mais)

- **Texto provocativo:** Em 2016, três pesquisadores subiram ao palco da DEF CON e mostraram que, em muitas empresas, o caminho de um usuário comum até o controle total do domínio é uma questão de teoria dos grafos. A palestra apresentou o BloodHound e mudou a forma como Red Teams e Blue Teams enxergam o Active Directory. Assista e pense: quantos caminhos desses existem na rede em que você trabalha?
- **Indicação:** ROBBINS, Andy; VAZARKAR, Rohan; SCHROEDER, Will. *Six degrees of domain admin*. Palestra apresentada na DEF CON 24, Las Vegas, 2016. (Vídeo gratuito no canal oficial da DEF CON no YouTube.) **[conferir link do vídeo]**
- **Link complementar:** catálogo KEV da CISA — <https://www.cisa.gov/known-exploited-vulnerabilities-catalog>
- **Aula em que entra:** Aula 8 (link complementar: Aula 6)

### Podcast (curadoria, até 45 min)

- **Texto provocativo:** Golpes por *e-mail*, falsas centrais telefônicas e fraudes com dados vazados fazem parte do noticiário brasileiro quase todos os dias. Neste podcast nacional, especialistas em segurança da informação e direito digital discutem esses casos à luz da LGPD e da legislação penal — um ótimo complemento para entender os limites éticos e legais das simulações de engenharia social.
- **Nome do podcast:** Segurança Legal
- **Nome do episódio:** **[conferir episódio sobre engenharia social ou *phishing*, com duração de até 45 min]**
- **Link:** **[conferir link do episódio no Spotify]**
- **Aula em que entra:** Aula 7

### Artigo científico

- **Texto provocativo:** Se a sua simulação de *phishing* teve 2% de cliques, isso é uma boa notícia — ou apenas sinal de que a isca era fácil demais? Pesquisadoras do NIST propõem um método para classificar a dificuldade de uma mensagem de *phishing* a partir das pistas que ela contém e do quanto o pretexto se encaixa na rotina do público. O artigo ajuda a interpretar as métricas de campanha com mais honestidade.
- **Link:** **[conferir link de acesso aberto no portal do *Journal of Cybersecurity* (Oxford Academic)]**
- **Aula em que entra:** Aula 7
- **Referência ABNT:** STEVES, Michelle; GREENE, Kristen; THEOFANOS, Mary. Categorizing human phishing difficulty: a Phish Scale. *Journal of Cybersecurity*, v. 6, n. 1, 2020.
