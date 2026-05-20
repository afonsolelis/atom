# Unidade 1 — Fundamentos de Sistemas de Informação

- **Disciplina:** Sistemas de Informação, Automação e IA Aplicada à Produção
- **Conteudista:** Afonso Cesar Lelis Brandão
- **Videoaulas desta unidade:** 1 a 4

## Vídeo introdutório + Relação da disciplina com a atuação profissional

Você já parou para pensar que **toda decisão na indústria moderna é, no fundo, uma decisão sobre dados**? Comprar mais matéria-prima? Decisão de dado. Parar uma máquina para manutenção? Decisão de dado. Contratar mais um turno? Decisão de dado. Promover uma pessoa? Decisão de dado. Investir em um equipamento? Decisão de dado.

E, no entanto, a maioria das empresas brasileiras ainda trata dado como subproduto da operação — coisa que **alguém da TI** cuida. Esta disciplina existe exatamente para mudar essa visão: para que você, futuro(a) engenheiro(a) de produção, entenda que **Sistemas de Informação, Automação e IA são a infraestrutura sobre a qual a indústria moderna roda** — e que dominar esses conceitos é o que separa o profissional **executor** do profissional **decisor**.

Vamos começar pelos fundamentos absolutos: o que é um sistema de informação, como funciona um banco de dados, para que serve um ERP, por que automação industrial é diferente da automação que você usa no celular, o que de fato é IA aplicada à produção. Sem assumir conhecimento prévio. Do zero. Mas chegando até o ponto onde você consegue ler um projeto de TI corporativo e conversar de igual para igual com o analista da empresa.

Ao final da disciplina, você sai sabendo o que muitos engenheiros com 5+ anos de mercado ainda não dominam — porque os sistemas de informação e a IA estão evoluindo mais rápido do que a maioria consegue acompanhar. Use isso.

### Roteiro do vídeo introdutório (até 2 min)

**Abertura (0:00 – 0:20):**
> "Olá! Eu sou o professor Afonso Brandão. Seja muito bem-vindo(a) à disciplina de Sistemas de Informação, Automação e IA Aplicada à Produção. Se você quer entender como **dados, sistemas e algoritmos** mudaram (e continuam mudando) o trabalho do engenheiro de produção, está no lugar certo."

**Conexão com o mercado (0:20 – 0:55):**
> "Hoje, a maior parte das vagas de engenheiro de produção em empresas competitivas exige domínio mínimo de TI industrial — ERP, MES, SCADA, IA preditiva. O profissional que sabe operar essas ferramentas vale duas vezes o que sabe só Excel."

**Conteúdo e diferencial (0:55 – 1:25):**
> "Aqui, a gente vai do absoluto zero — você vai entender o que é dado, o que é sistema de informação, como funciona um banco de dados. Depois, sobe pra ERP e MES, depois automação industrial, e por último IA aplicada. Você vai sair sabendo conversar com profissionais de TI de igual para igual."

**Benefício para o aluno (1:25 – 1:45):**
> "Ao final, você consegue **diagnosticar** o nível de digitalização de uma indústria, **propor** soluções realistas e **defender** tecnicamente cada decisão. Diferencial real para quem está saindo da graduação."

**Encerramento (1:45 – 2:00):**
> "Bora! Sistemas de Informação e IA são o esqueleto invisível da indústria moderna. Vem comigo entender esse esqueleto. Te espero na Aula 1!"

---

## Aula 1 — Dado, informação e conhecimento: o que é tudo isso?

Antes de qualquer outra coisa, precisamos alinhar **vocabulário básico**. Você vai ouvir, ao longo da disciplina, três palavras que parecem sinônimos mas **não são**: **dado**, **informação** e **conhecimento**. Confundi-las é o erro mais comum em projetos de TI industrial — e é o que esta aula vai resolver de uma vez por todas.

### A pirâmide DIKW: dado, informação, conhecimento e sabedoria

Há um modelo clássico chamado **pirâmide DIKW** (Data, Information, Knowledge, Wisdom) que organiza esses conceitos:

| Camada | Pergunta que responde | Exemplo industrial |
| --- | --- | --- |
| **Dado** | O quê? | "85,3" |
| **Informação** | O que isso significa? | "Temperatura do forno A está em 85,3 °C" |
| **Conhecimento** | Como isso se conecta? | "Forno A está 5 °C acima do limite operacional ideal" |
| **Sabedoria** | O que fazer? | "Reduzir a temperatura do Forno A em 5 °C, evitando degradação do produto" |

Note como cada camada **adiciona contexto** à anterior. Um dado isolado (`85,3`) é inútil. Uma informação contextualizada (`85,3 °C no forno A`) é melhor. Conhecimento (`acima do limite`) começa a ser acionável. Sabedoria (`reduzir 5 °C`) é decisão.

### Dado: a matéria-prima invisível

> **Dado** é um **registro factual** sobre algo — número, texto, imagem, áudio — **sem contexto** ou interpretação.

Dados são o "tijolo" da pirâmide. Características importantes:

- **Atômicos** — geralmente são valores isolados.
- **Sem significado próprio** — `85,3` sozinho não diz nada.
- **Existem em formatos variados** — números, textos, imagens, vídeos, sinais elétricos.
- **Podem ser estruturados** (arrumados em tabelas) ou **não estruturados** (textos livres, fotos).

Em uma fábrica média, **milhões de dados são gerados por dia** — leituras de sensores, registros de ponto, ordens de produção, notas fiscais, e-mails, planilhas. Sem organização, é só ruído.

### Informação: dado + contexto

> **Informação** é o dado **dentro de um contexto** — quando você sabe **o que** o número significa, **quando** foi medido, **onde** está, **quem** registrou.

Para um dado virar informação, você precisa de **metadados** (dados sobre dados): unidade de medida, momento, fonte, formato.

**Exemplo:** o dado `85,3` vira informação quando se torna `Temperatura = 85,3 °C, sensor F2_TEMP_03, em 19/05/2026 às 14:32, no forno A da linha 2`.

### Conhecimento: informação + experiência

> **Conhecimento** é a capacidade de **conectar informações** a partir de experiência ou regras aprendidas, produzindo entendimento.

Um operador experiente, ao ver "Temperatura = 85,3 °C no Forno A", **sabe** que isso está acima do ideal (80 °C) — porque conhece o processo. Esse é o conhecimento operacional. Ele só existe porque alguém **aprendeu**, ao longo do tempo, o que aquele número significa para o negócio.

### Sabedoria: conhecimento + ação

> **Sabedoria** é a capacidade de **agir corretamente** a partir do conhecimento, em situações específicas e considerando o contexto mais amplo.

O operador sábio não apenas reconhece o desvio — ele **decide** se deve ajustar agora, esperar 5 minutos, ou parar a operação. Essa decisão depende de muitos fatores que vão além do número: histórico, prazo do lote, custo da parada.

### Por que isso importa para sistemas de informação

A grande missão de um **sistema de informação industrial** é **subir essa pirâmide**:

- Coletar dados em escala e qualidade.
- Estruturá-los em informação contextual.
- Apresentá-los de forma a apoiar conhecimento operacional.
- E, idealmente, ajudar a tomar decisões com mais sabedoria (apoiado por IA, automação, regras).

Sem entender essa hierarquia, projetos de TI industrial falham porque tentam vender "dashboards lindos" sem questionar **qual decisão eles habilitam**.

### Exemplo numérico: o quanto cada camada multiplica valor

Considere um cenário simplificado em uma fábrica:

| Camada | O que custa coletar | O que vale para a empresa |
| --- | --- | --- |
| Dado bruto (sensor) | R\$ 0,01 por leitura | Quase zero isoladamente |
| Informação (dashboard) | R\$ 0,10 por leitura | R\$ 5 por leitura (visibilidade) |
| Conhecimento (análise) | R\$ 0,50 por leitura | R\$ 50 por leitura (causa-raiz) |
| Sabedoria (decisão) | R\$ 2,00 por leitura | R\$ 500 por leitura (ação correta) |

São números ilustrativos, mas mostram o princípio: **subir uma camada na pirâmide tipicamente multiplica o valor por 5 a 10 vezes**. Coletar dado é barato e baixo valor; tomar decisão sábia com base em dado é caro e alto valor.

### Dados estruturados vs não estruturados

Antes de fechar a aula, uma distinção que vamos usar muito:

- **Dados estruturados** — organizados em formato de tabela, com colunas e tipos definidos. Ex.: lista de pedidos no ERP (data, cliente, valor, produto, quantidade).
- **Dados semi-estruturados** — têm alguma estrutura, mas flexível. Ex.: JSON, XML, log de máquina.
- **Dados não estruturados** — texto livre, foto, áudio, vídeo. Ex.: comentário no relatório de inspeção, foto da peça, ligação telefônica gravada.

Estima-se que **80% dos dados gerados no mundo são não estruturados** — e até pouco tempo, eram **invisíveis** para sistemas de informação tradicionais. A IA mudou isso (vamos ver na Unidade 4).

### Atividade prática

Pegue um dia comum no seu trabalho ou estágio (ou imagine uma fábrica). Identifique:

1. **Três dados** que são gerados ao longo do dia.
2. **Três informações** (dados com contexto).
3. **Um conhecimento** que alguém da empresa carrega na cabeça.
4. **Uma decisão** que se beneficiaria de mais dado/informação/conhecimento.

Anote no caderno — vamos voltar nisso na Aula 2.

### Pontos-chave

- A pirâmide **DIKW** organiza: **dado → informação → conhecimento → sabedoria**.
- Cada camada adiciona contexto à anterior — e tipicamente **multiplica valor por 5-10×**.
- **Dado** é registro factual atômico; **informação** é dado contextualizado; **conhecimento** conecta informações; **sabedoria** age.
- Dados podem ser **estruturados, semi-estruturados ou não estruturados** — 80% do total mundial é não estruturado.
- Sistemas de informação existem para **subir a pirâmide** — transformar dado em decisão.

### Para saber mais

- **Davenport, T.; Prusak, L.** *Conhecimento Empresarial*. Editora Campus.
- **Pirâmide DIKW (Wikipedia em inglês — explicação aprofundada):** https://en.wikipedia.org/wiki/DIKW_pyramid
- **Vídeo (Hashtag Programação, YouTube):** "Dado, Informação e Conhecimento — qual a diferença?"
- **Portal Brasil Mais Produtivo:** https://brasilmaisprodutivo.gov.br/

---

## Aula 1 — Roteiro da Videoaula 1: "Dado, informação, conhecimento — a confusão que custa caro"

**Duração:** 8 a 10 minutos.

### 1. Abertura (0:00 – 0:40)

> "Toda decisão na indústria moderna é, no fundo, uma decisão sobre dados. Mas a maioria das pessoas confunde **dado, informação e conhecimento** — e essa confusão custa caro. Hoje a gente vai resolver isso de uma vez por todas."

### 2. A pirâmide DIKW (0:40 – 4:00)

- Apresentar a pirâmide com a tabela "85,3 → ... → ação".
- Reforçar: cada camada multiplica valor.
- Caso concreto: temperatura de forno A.

### 3. Dado, informação, conhecimento, sabedoria (4:00 – 7:00)

- Definir cada um com exemplo industrial.
- Dado é atômico; informação tem contexto; conhecimento conecta; sabedoria age.

### 4. Estruturados vs não estruturados (7:00 – 8:30)

- Listar: ERP, JSON/log, fotos.
- 80% do dado mundial é não estruturado — IA mudou isso.

### 5. Encerramento (8:30 – 10:00)

> "Próxima aula, a gente vai entender o que é um **sistema de informação** — a máquina que sobe essa pirâmide o tempo todo. Te espero!"

---

## Aula 2 — O que é um Sistema de Informação? Componentes e tipos

Agora que você sabe o que é dado, informação e conhecimento, vamos para o segundo conceito-base: **o que é um Sistema de Informação (SI)?** Vou te dar a definição clara, mostrar os 5 componentes que todo SI tem, e listar os principais tipos que você vai encontrar na indústria.

### A definição em uma frase

> **Sistema de Informação (SI)** é um conjunto coordenado de **pessoas, processos, dados, software e hardware** que **coleta, processa, armazena e distribui informações** para apoiar a operação, a gestão e a tomada de decisão em uma organização.

Note os **cinco elementos** (vamos detalhar cada um abaixo). E note também que SI **não é só software** — é o conjunto. Uma planilha do Excel sozinha não é um SI. Mas Excel + processo de preenchimento + pessoa responsável + computador + dados consolidados pode ser.

### Os 5 componentes de um SI

1. **Pessoas** — quem opera, alimenta, usa, decide com base no sistema. **Sem pessoas, nenhum SI funciona.** É comum subestimar esse componente — e é nele que a maioria dos projetos falha.
2. **Processos** — as rotinas, normas e fluxos de trabalho que orientam **como** o sistema é usado. "Toda nota fiscal recebida deve ser lançada no ERP em até 4 horas" é um processo.
3. **Dados** — os registros (estruturados ou não) que o sistema armazena e processa. Vimos na Aula 1.
4. **Software** — os programas e aplicativos que processam os dados (ERP, planilha, banco de dados, app).
5. **Hardware** — os equipamentos físicos que rodam o software (servidores, computadores, tablets, sensores).

Há quem inclua **redes/comunicação** como sexto componente — mas costumam ser tratadas dentro de hardware/software.

### Por que pessoas e processos vêm primeiro

Em uma palestra famosa, um consultor disse: "se você pegar a melhor tecnologia do mundo e jogar dentro de uma empresa caótica, o resultado é caos mais caro". A frase resume bem por que **pessoas e processos vêm antes** de software e hardware em projetos sérios.

Os melhores sistemas falham se:

- Os operadores **não usam** corretamente.
- O processo de alimentação **não é seguido**.
- A liderança **não cobra disciplina**.
- A empresa não treina **continuamente**.

Por isso, **sempre que falamos em "implementar um sistema", o trabalho com pessoas representa 50-70% do esforço**.

### Os tipos de SI mais comuns na indústria

Vamos categorizar pelos **níveis hierárquicos** da empresa — modelo clássico de SI:

| Nível | Tipo de SI | O que faz |
| --- | --- | --- |
| **Operacional** | **TPS** (Transaction Processing System) | Registra transações do dia a dia |
| **Tático** | **MIS** (Management Information System) | Gera relatórios para gerência |
| **Tático** | **DSS** (Decision Support System) | Apoia decisões com análises e simulações |
| **Estratégico** | **EIS** (Executive Information System) | Dashboards executivos consolidados |
| **Estratégico** | **ESS** (Executive Support System) | EIS + comunicação + colaboração para alta direção |
| **Integrador** | **ERP** (Enterprise Resource Planning) | Integra processos de toda a empresa |
| **Específico** | **MES, CRM, SCM, WMS, PLM** | Sistemas verticais (vamos ver na U2) |

Não precisa decorar a sopa de letrinhas agora — você vai conviver com cada um. O importante: **cada sistema atende a uma necessidade diferente** e **deveriam** se integrar (mas raramente integram bem).

### O ciclo básico de um SI

Todo SI executa quatro operações:

1. **Coleta (entrada)** — captura dados do mundo (manual, automática, importada).
2. **Processamento** — limpa, valida, agrega, calcula.
3. **Armazenamento** — guarda em banco de dados, arquivo, nuvem.
4. **Saída** — entrega resultado como tela, relatório, alerta, integração com outro sistema.

Cada um desses passos pode falhar. **A qualidade do SI depende de cada elo** dessa cadeia. Sistemas que coletam dado ruim → produzem informação ruim → geram decisão ruim.

### Exemplo numérico: o ciclo em uma fábrica

Pedido recebido em uma empresa que produz tampas plásticas:

| Etapa | Tempo típico (sem SI) | Tempo típico (com ERP) |
| --- | --- | --- |
| Cliente envia pedido por e-mail | 1 dia | 1 hora |
| Pedido lançado no sistema | 4 horas | 5 minutos (automático) |
| Programação da produção | 1 dia | 30 minutos |
| Nota fiscal emitida | 4 horas | Automática |
| Cliente recebe confirmação | 2 dias | 1 hora |
| **Total** | **~5 dias** | **~3 horas** |

Esse ganho de **5 dias para 3 horas** é o que torna SI essencial em fábricas competitivas. **Velocidade de informação = velocidade do negócio.**

### Atividade prática

Pegue uma operação da sua empresa (ou de uma que você conhece). Identifique:

1. Quais são os **5 componentes** do SI envolvido (pessoas, processos, dados, software, hardware)?
2. Em qual **nível** (operacional, tático, estratégico) esse SI atua?
3. Qual é o **ciclo** (coleta → processamento → armazenamento → saída) desse sistema?
4. Onde está o **elo mais fraco** desse ciclo?

### Pontos-chave

- **Sistema de Informação** = pessoas + processos + dados + software + hardware.
- **Pessoas e processos** vêm **antes** da tecnologia (50-70% do esforço de implantação).
- Tipos clássicos: **TPS, MIS, DSS, EIS, ERP, MES, CRM, SCM, WMS, PLM**.
- Ciclo básico: **coleta → processamento → armazenamento → saída**.
- Qualidade do SI é tão fraca quanto seu **elo mais fraco** no ciclo.

### Para saber mais

- **Laudon, K.; Laudon, J.** *Sistemas de Informação Gerenciais*. Pearson.
- **Vídeo (Curso em Vídeo, YouTube):** "O que é Sistema de Informação?"
- **Portal Sebrae sobre SI:** https://sebrae.com.br/

---

## Aula 2 — Roteiro da Videoaula 2: "Não é só software — o que torna um SI realmente útil"

**Duração:** 8 a 10 minutos.

### 1. Abertura (0:00 – 0:30)

> "Sistema de informação **não é só software**. Quem ainda acha isso vai entender hoje por que tantos projetos de TI falham."

### 2. Os 5 componentes (0:30 – 4:00)

- Pessoas, processos, dados, software, hardware.
- Reforçar: pessoas e processos vêm **primeiro**.
- "Caos mais caro" — frase de consultor.

### 3. Os tipos principais (4:00 – 6:30)

- TPS, MIS, DSS, EIS, ERP — mostrar tabela com nível e função.
- Mencionar verticais (MES, CRM, etc.) — próxima unidade.

### 4. O ciclo + exemplo numérico (6:30 – 8:30)

- Coleta → processamento → armazenamento → saída.
- Caso: pedido de tampa plástica de 5 dias para 3 horas.

### 5. Encerramento (8:30 – 10:00)

> "Próxima aula, vamos abrir os principais tipos por dentro: TPS, MIS, DSS, ERP. Para que serve cada um, na prática. Te espero!"

---

## Aula 3 — TPS, MIS, DSS, ERP: para que serve cada um

> **Pausa para reflexão:** se eu te der um Excel e um ERP, e ambos têm "os mesmos dados", qual a diferença? Pensa nisso enquanto avançamos.

Na aula passada, vimos rapidamente uma sopa de letrinhas: **TPS, MIS, DSS, EIS, ERP**. Esta aula é dedicada a **abrir cada um** desses sistemas — entender o que faz, onde atua, e por que aparece como aparece. Sem esse vocabulário, conversas técnicas com TI viram conversas em chinês.

### TPS — Transaction Processing System

> **TPS** é o sistema que **registra as transações do dia a dia** da empresa — vendas, compras, pagamentos, recebimentos, ordens de produção, registros de ponto.

São os sistemas mais **antigos** e **operacionais** da empresa. Características:

- Alta **frequência** de uso (várias transações por minuto).
- Foco em **velocidade e confiabilidade** — não pode falhar.
- Geram **muito dado bruto** (o "tijolo" da pirâmide DIKW).
- Tipicamente: **caixa, faturamento, folha de pagamento, controle de estoque, ordem de serviço**.

**Exemplos:** sistema de PDV (ponto de venda) do supermercado, sistema de faturamento da Sigma, módulo de ordens de produção do TOTVS.

### MIS — Management Information System

> **MIS** é o sistema que **gera relatórios consolidados** a partir dos dados dos TPS, para apoio à gestão tática (gerência).

Sai do detalhe e vai para o **agregado**:

- Não registra transações — **lê e organiza** o que os TPS já registraram.
- Gera relatórios **periódicos** (diário, semanal, mensal).
- Tipicamente: **relatório de vendas por região, OEE mensal por linha, custo médio por produto**.
- Hoje, **MIS clássico** é frequentemente substituído por **BI (Business Intelligence)** — versão moderna do MIS, com dashboards em tempo real e drill-down.

**Exemplo:** o dashboard de produção mensal que o gerente apresenta na reunião.

### DSS — Decision Support System

> **DSS** é o sistema que **apoia decisões mais complexas** com análise, simulação e modelos matemáticos.

DSS é o MIS turbinado. Não apenas mostra o que aconteceu — **simula o que acontece se**:

- "E se eu aumentar 10% a velocidade da linha?"
- "E se eu trocar o fornecedor de X?"
- "Qual a melhor combinação de turnos para atender o pico de demanda?"

DSS usa **modelos** (matemáticos, estatísticos, IA) para responder. É a fronteira entre BI e IA preditiva.

**Exemplo:** simulador de cenário de produção que mostra o impacto financeiro de cada decisão antes de ela ser tomada.

### EIS / ESS — Executive Information / Support System

> **EIS** é o painel **executivo**, consolidado, com indicadores estratégicos da empresa em tela única.

Características:

- Foco em **alta direção** (presidência, diretoria).
- **Poucos indicadores** — só o que importa estrategicamente.
- Visual **simples e direto** — semáforos verdes/amarelos/vermelhos.
- Conectado a **fontes diversas** (consolida vários sistemas).
- **ESS** é o EIS + ferramentas de comunicação e colaboração (e-mail integrado, videoconferência).

**Exemplo:** dashboard de governança que mostra, em uma única tela, EBITDA, market share, NPS, OEE consolidado da empresa.

### ERP — Enterprise Resource Planning

> **ERP** é o sistema **integrador** da empresa — junta em uma única base de dados os processos de **finanças, RH, produção, vendas, compras, estoque, contabilidade**.

ERP é o **espinha dorsal** da TI empresarial moderna. Características:

- **Único banco de dados** central — sem duplicação.
- **Módulos integrados** — vendas atualiza estoque, que atualiza compras, que atualiza financeiro.
- Implementação **longa e cara** — meses ou anos.
- **Pesado de operar** — exige disciplina das equipes.
- Tipicamente, é o **maior investimento de TI** que uma empresa faz.

**Exemplos:** SAP, Oracle EBS/NetSuite, TOTVS Protheus, Microsoft Dynamics, Sankhya, Odoo.

### Como esses sistemas se conectam

A relação **clássica** entre TPS, MIS, DSS, EIS e ERP pode ser desenhada assim:

```
Sensores / chão de fábrica
        ↓
TPS (registros transacionais)
        ↓
ERP (integrador, banco único)
        ↓                  ↓
   MIS/BI         DSS (análise/simulação)
        ↓                  ↓
        ↓             EIS/ESS (executivo)
```

Numa empresa madura, **todos esses sistemas funcionam juntos**. Numa empresa imatura, cada departamento tem o seu, e os dados não conversam.

### Diferença entre ERP e MES (preview para U2)

Confusão muito comum: "ERP é igual a MES?". Resposta curta: **não**.

- **ERP** olha o **negócio**: pedidos, faturas, custo, RH, financeiro.
- **MES** olha o **chão de fábrica**: ordem de produção em execução, máquina ligada/parada, OEE em tempo real.

Eles deveriam **conversar** — o pedido entra no ERP, é enviado ao MES, é executado, e o resultado volta para o ERP atualizar estoque/custo. Vamos detalhar isso na Unidade 2.

### Exemplo numérico: economia em integração ERP + outros sistemas

Em uma fábrica de médio porte sem ERP integrado:

- Dados duplicados em 6 sistemas → **15-25% das informações têm divergência**.
- Tempo gasto reconciliando: **~120 horas/mês** (3 analistas em meio expediente).
- Custo: 120 × R\$ 50/h = R\$ 6.000/mês = **R\$ 72 mil/ano** só em reconciliação.
- Decisões atrasadas, retrabalho, multas fiscais → estimadas em **R\$ 200-500 mil/ano**.

Implementação de ERP integrado: **R\$ 800 mil a R\$ 3 milhões** (varia muito por porte). Payback típico em **2-4 anos**.

### Atividade prática

Identifique, na empresa que você conhece:

1. **Que TPS existem?** (sistema de faturamento, ponto eletrônico, controle de estoque...)
2. **Existe ERP?** Se sim, qual?
3. **Existe MIS/BI?** Quem usa?
4. **Existe DSS** ou simulações? Em que decisões?
5. **Existe EIS** para a diretoria? Como ele é alimentado?

### Pontos-chave

- **TPS** registra transações; **MIS/BI** gera relatórios; **DSS** apoia decisão; **EIS** consolida para executivos.
- **ERP** é o **integrador** — espinha dorsal da TI empresarial.
- Em uma empresa madura, esses sistemas trabalham **juntos**, em camadas hierárquicas.
- **ERP ≠ MES** — ERP é negócio, MES é chão de fábrica.
- Implementação de ERP é o **maior projeto de TI** de uma empresa típica.

### Para saber mais

- **Norris, G.** *E-Business and ERP*. Wiley.
- **Vídeo (Itaipu Parquetec, YouTube):** "O que é ERP? Para que serve?"
- **SAP for Manufacturing:** https://www.sap.com/products/scm.html
- **TOTVS — Conteúdo educativo:** https://www.totvs.com/blog/

---

## Aula 3 — Roteiro da Videoaula 3: "TPS, MIS, DSS, ERP — destrinchando a sopa de letrinhas"

**Duração:** 9 a 11 minutos.

### 1. Abertura (0:00 – 0:30)

> "TPS, MIS, DSS, ERP... parece sopa de letrinhas. Mas cada uma dessas siglas é uma peça do quebra-cabeça da TI empresarial. Hoje a gente abre cada uma e mostra o porquê existirem."

### 2. TPS — o registro do dia a dia (0:30 – 2:30)

- Definição + exemplos (PDV, faturamento, ordem de produção).
- Alta frequência, foco em velocidade.

### 3. MIS, DSS, EIS — subindo a pirâmide (2:30 – 6:00)

- MIS/BI: relatórios consolidados.
- DSS: simulação e análise para decisão.
- EIS/ESS: dashboards executivos.

### 4. ERP — o integrador (6:00 – 8:30)

- Definição.
- Único banco, módulos integrados.
- Exemplos (SAP, TOTVS, Oracle).
- ERP ≠ MES — preview para U2.

### 5. Encerramento (8:30 – 11:00)

> "Próxima aula, a gente desce no detalhe técnico: **banco de dados**. Onde toda essa informação **realmente** vive. Te espero!"

---

## Aula 4 — Banco de dados na produção: modelagem básica

Você chegou ao último tópico da Unidade 1 — e ao mais "técnico" de todos. Não se assuste: **vou tratar de banco de dados em linguagem de gente**, sem fórmulas mágicas. Você vai sair sabendo o que é, como funciona e por que importa para a engenharia de produção.

### O que é um banco de dados

> **Banco de dados** (database) é uma **coleção organizada de dados**, armazenada eletronicamente, que pode ser facilmente consultada, atualizada e analisada.

Pense em um banco de dados como uma **biblioteca digital**: tem prateleiras (tabelas), livros (linhas/registros), e cada livro tem capítulos (colunas/campos). Tudo organizado de forma que você consegue **encontrar** rapidamente o que precisa.

### Dado vs banco de dados

Não confunda:

- **Dado** = uma única informação registrada (vimos na Aula 1).
- **Banco de dados** = **muitos** dados organizados, com regras para acesso, consulta e atualização.

Uma planilha de Excel **não é** banco de dados de verdade. É um arquivo. Banco de dados real é um sistema que serve vários usuários simultaneamente, com controle de acesso, segurança, integridade e tudo mais.

### Banco de dados relacional (SQL)

A categoria mais comum em empresas é o **banco de dados relacional**, baseado no modelo de **tabelas**. Características:

- **Tabela** = entidade. Ex.: tabela de Clientes, tabela de Pedidos, tabela de Produtos.
- **Coluna** = atributo. Ex.: na tabela Clientes, colunas como Nome, CPF, Endereço.
- **Linha** = registro (também chamado de **tupla** ou **row**). Cada cliente é uma linha.
- **Chave primária** = identificador único de cada linha (CPF do cliente, número do pedido).
- **Chave estrangeira** = referência a outra tabela (o pedido tem o CPF do cliente).

A linguagem usada para consultar bancos relacionais é **SQL** (Structured Query Language) — você verá esse nome muito na vida profissional. SQL é a linguagem mais usada em TI corporativa **do mundo inteiro**.

Exemplo simples de uma tabela de Pedidos:

| ID_Pedido | Data | CPF_Cliente | Produto | Quantidade | Valor |
| --- | --- | --- | --- | --- | --- |
| 1001 | 2026-05-19 | 123.456.789-00 | Tampa 60mm | 5.000 | 12.500 |
| 1002 | 2026-05-19 | 987.654.321-00 | Tampa 80mm | 2.000 | 6.000 |
| 1003 | 2026-05-20 | 123.456.789-00 | Tampa 60mm | 3.000 | 7.500 |

### Bancos de dados NoSQL

Existem também **bancos NoSQL** (Not Only SQL), que **não usam tabelas rígidas**. São mais flexíveis para certos casos:

- **Documentos (MongoDB)** — guarda objetos JSON com estrutura variável.
- **Chave-valor (Redis)** — guarda pares simples; muito rápido.
- **Colunar (Cassandra, BigQuery, ClickHouse)** — otimizado para análise.
- **Grafo (Neo4j)** — guarda relações entre entidades (redes sociais, fraude).
- **Time series (InfluxDB, TimescaleDB)** — otimizado para dados de sensor IIoT.

Em uma fábrica moderna, **convivem** vários tipos: ERP usa relacional, IIoT usa time series, IA usa colunar para análise. Cada um para o que faz melhor.

### Modelagem básica: entidades e relacionamentos

Antes de criar um banco, você modela. Existem duas representações clássicas:

1. **Diagrama Entidade-Relacionamento (ER)** — desenho que mostra entidades (tabelas) e como se relacionam.
2. **Modelo lógico** — definição de tabelas, colunas, chaves e tipos de dado.

Exemplo de modelagem para uma fábrica:

```
[Clientes] 1 ──── n [Pedidos] n ──── m [Produtos]
                       │
                       │ 1
                       ▼
                 [Ordens de Produção]
                       │
                       │ n
                       ▼
                 [Operações]
                       │
                       │ n
                       ▼
                  [Máquinas]
```

A leitura: **um** cliente pode ter **vários** pedidos; cada pedido pode ter **vários** produtos; cada pedido gera **uma ou mais** ordens de produção; ordem tem **várias** operações; operações usam **máquinas**.

Esse desenho é o **mapa** do banco de dados — e antes de programar **nada**, você desenha. Engenheiros que pulam essa etapa criam bancos confusos que ninguém entende.

### Normalização: por que dividir os dados em várias tabelas?

Pergunta comum: "Por que não colocar **tudo** numa tabela só?". Resposta: porque dá problema. Imagina se cada pedido tivesse, na própria linha, **todos os dados do cliente** (nome, CPF, endereço, telefone). Quando o cliente mudasse de telefone, você teria que atualizar **todos** os pedidos dele — e seria fácil esquecer um.

**Normalização** é o processo de **eliminar redundância**, separando dados em tabelas específicas. Tem 5 níveis (1FN, 2FN, 3FN, BCNF, 4FN), mas para você bastam os primeiros 3 — todo banco em uso real está normalizado pelo menos até 3FN.

### Banco de dados na produção: casos típicos

Em uma fábrica, banco de dados aparece em vários lugares:

1. **ERP** — banco enorme, normalizado, com centenas de tabelas (TPS).
2. **MES** — banco de produção em tempo real (estado das máquinas, ordens em execução).
3. **Historian** — banco de séries temporais (leituras de sensor, MES, SCADA).
4. **Data warehouse / data lake** — banco analítico (consolida tudo para BI/IA).

Você como engenheiro(a) **não precisa criar** esses bancos do zero (TI faz). Mas **precisa entender** o que cada um tem, para fazer perguntas certas e cruzar dados.

### Exemplo numérico: o ganho de eficiência de uma consulta SQL

Imagine que você quer saber: "qual o produto que mais foi vendido para clientes do Sudeste no último trimestre?". Sem banco de dados:

- Você abre planilha com 200 mil linhas.
- Filtra manualmente região "Sudeste".
- Soma quantidades por produto.
- Ordena.
- Tempo: **2-4 horas** (e provavelmente comete erros).

Com banco de dados e SQL simples:

```sql
SELECT produto, SUM(quantidade) AS total
FROM pedidos
WHERE regiao = 'Sudeste'
  AND data BETWEEN '2026-01-01' AND '2026-03-31'
GROUP BY produto
ORDER BY total DESC
LIMIT 1;
```

Tempo: **3 segundos**. Sem erros. Esse é o poder do banco + SQL.

### Atividade prática

Em uma folha em branco, desenhe o **modelo entidade-relacionamento (ER)** de uma operação simples:

> Uma fábrica recebe **pedidos** de **clientes**. Cada pedido tem um ou mais **produtos**, em quantidades específicas. A fábrica produz com **máquinas** organizadas em **linhas de produção**. Cada produto é fabricado em uma linha específica.

Identifique:

1. Quais são as **entidades** (futuras tabelas)?
2. Quais são as **chaves primárias** (identificadores únicos) de cada uma?
3. Quais são os **relacionamentos** (1-n, n-m) entre elas?

### O que você verá na próxima unidade

Na **Unidade 2**, vamos abrir os **sistemas de informação específicos da produção** — **ERP, MES, SCM/WMS, CRM, PLM** — e ver como eles trabalham juntos no chão de fábrica e na cadeia de suprimentos. É a unidade que "aterra" tudo o que você aprendeu até aqui em sistemas reais.

### Pontos-chave

- **Banco de dados** é coleção organizada de dados, com regras de acesso, consulta e atualização.
- **Relacional (SQL)** é o tipo mais comum em empresas; **NoSQL** atende casos específicos (sensor, grafo, documento).
- **Modelagem ER** (entidades + relacionamentos) é o **mapa** do banco — feito **antes** de programar.
- **Normalização** elimina redundância — banco normal é mais consistente e mais fácil de manter.
- Em uma fábrica: ERP (negócio), MES (produção), Historian (sensor), Data warehouse (análise) — cada um tem seu papel.

### Para saber mais

- **Date, C. J.** *Introdução a Sistemas de Bancos de Dados*. Editora Campus.
- **Vídeo (Asimov Academy, YouTube):** "SQL para iniciantes — em 1 hora"
- **Curso gratuito (Estácio):** Fundamentos de Banco de Dados — https://www.estacio.br/
- **Khan Academy — SQL Course (em inglês):** https://www.khanacademy.org/computing/computer-programming/sql

---

## Aula 4 — Roteiro da Videoaula 4: "Banco de dados em linguagem de gente"

**Duração:** 9 a 11 minutos.

### 1. Abertura (0:00 – 0:40)

> "Banco de dados parece coisa de TI cabeludo. Hoje eu vou te provar o contrário — em linguagem de gente. Quando essa aula acabar, você vai conseguir ler um diagrama, entender o que é SQL e desenhar um banco simples."

### 2. O que é banco de dados (0:40 – 2:30)

- Definir como biblioteca digital.
- Distinguir de planilha de Excel.
- Relacional (SQL) vs NoSQL.

### 3. Modelagem ER (2:30 – 5:30)

- Entidades, atributos, chaves.
- Desenhar fluxo Clientes → Pedidos → Produtos → Máquinas.
- Por que normalizar.

### 4. Bancos na fábrica (5:30 – 8:30)

- ERP, MES, Historian, Data warehouse — cada um para o quê.
- Exemplo numérico: consulta SQL vs Excel (3s vs 4h).

### 5. Encerramento + gancho U2 (8:30 – 11:00)

> "Próxima unidade: vamos ver os **sistemas verticais** que rodam o chão de fábrica brasileiro — ERP, MES, SCM, WMS, CRM, PLM. É a hora de aterrissar tudo. Te espero!"

---

## Quiz não avaliativo

### Questão 1

Sobre a pirâmide **DIKW** (Dado, Informação, Conhecimento, Sabedoria), assinale a alternativa **correta**:

- [ ] a. A pirâmide DIKW estabelece que dado e informação são sinônimos, sendo conhecimento e sabedoria as únicas camadas distintas.
- [x] b. Cada camada da pirâmide adiciona contexto à anterior: dado é registro factual sem contexto, informação é dado contextualizado, conhecimento conecta informações por experiência, sabedoria é ação correta.
- [ ] c. A pirâmide DIKW começa pela sabedoria no topo e desce para o dado bruto na base, sendo a sabedoria a matéria-prima.
- [ ] d. A pirâmide DIKW se aplica apenas a dados estruturados, sendo irrelevante para dados não estruturados como fotos ou áudios.

**Resposta correta:** `b`

**Feedback:** A alternativa (b) descreve corretamente as quatro camadas e a relação entre elas — base do raciocínio em qualquer projeto de sistema de informação. A (a) confunde dado com informação — são distintos. A (c) inverte completamente a ordem da pirâmide. A (d) é falsa: a pirâmide se aplica a **qualquer** tipo de dado (estruturado, semi-estruturado, não estruturado).

### Questão 2

Em relação aos **cinco componentes** de um sistema de informação (SI), assinale a alternativa **correta**:

- [ ] a. Um SI é composto apenas por hardware e software — pessoas, processos e dados são elementos externos ao sistema.
- [ ] b. Os cinco componentes têm igual importância em qualquer projeto, mas a tecnologia (hardware + software) representa 80% do esforço de implementação.
- [ ] c. Pessoas e processos são apenas decorativos no SI; o que define o sucesso é exclusivamente a qualidade do software escolhido.
- [x] d. Um SI é composto por pessoas, processos, dados, software e hardware — sendo que **pessoas e processos** representam, em média, 50-70% do esforço de implementação e são determinantes para o sucesso do projeto.

**Resposta correta:** `d`

**Feedback:** A (d) descreve corretamente os cinco componentes e a proporção realista do esforço. As (a) e (b) e (c) ignoram ou minimizam o componente humano e processual — exatamente o erro que faz a maioria dos projetos de TI falharem. Implantar tecnologia em organização caótica gera "caos mais caro" (frase clássica de consultoria).

---

## Atividade Verificadora (AAI — Atividade Avaliativa Individual)

**Pergunta:**

> Considere uma empresa de **médio porte** (300 a 800 funcionários) que opera principalmente com **planilhas Excel** para controle de produção, vendas, estoque e financeiro. A diretoria reconhece que esse modelo está "passando do limite" — divergências entre planilhas, retrabalho manual e decisões atrasadas.
>
> Você foi convidado(a) a apresentar **uma proposta inicial** de transformação dos sistemas de informação dessa empresa.
>
> Estruture sua resposta em três partes:
>
> 1. **Diagnóstico** — quais os 3 principais problemas que essa empresa enfrenta hoje pelo uso de planilhas? Justifique tecnicamente cada um (perda de qualidade do dado, retrabalho, divergência, segurança, escalabilidade).
> 2. **Recomendação** — qual sistema (ou conjunto de sistemas) você recomendaria implementar primeiro? Justifique a escolha considerando porte, custo realista (R\$) e prazo.
> 3. **Riscos e mitigações** — quais os 3 principais riscos do seu plano e como mitigar cada um?

**Resposta esperada:**

> Resposta exemplar começa pelo diagnóstico realista — problemas típicos do "Excel-centrismo": (1) **divergência entre planilhas** (a do financeiro não bate com a do comercial); (2) **retrabalho manual** (alguém precisa consolidar tudo todo mês); (3) **risco de erro humano** (uma fórmula errada propaga erro pela empresa); (4) **falta de segurança e auditoria** (qualquer pessoa pode editar, ninguém rastreia quem mudou o quê); (5) **escalabilidade limitada** (Excel trava com mais de 100k linhas; multi-usuário simultâneo é impossível). A recomendação típica para esse porte é **ERP integrado** (TOTVS Protheus, Sankhya, Odoo ou similar) — investimento entre R\$ 200 mil e R\$ 1 milhão, prazo de implementação de 8 a 18 meses, payback de 24 a 36 meses. A resposta deve demonstrar consciência de que ERP **não é solução mágica** — exige patrocínio executivo, equipe interna treinada, mudança de processo. Riscos esperados: (a) **resistência cultural** (pessoas acostumadas com Excel resistem); (b) **superdimensionamento de escopo** (querer tudo no primeiro projeto); (c) **falta de mestre interno** (depender só do consultor da implantação); cada um com mitigação concreta. Resposta de qualidade evita "comprar SAP" e justifica a escolha pelo perfil da empresa.

---

## Material complementar

### Direto da fonte — livro da Biblioteca Virtual

> Este é o clássico de SI usado em escolas de administração e engenharia no mundo inteiro. Os primeiros capítulos consolidam tudo o que vimos na Unidade 1 — dado, informação, sistemas, tipos. Leitura **essencial** para fixar vocabulário e ganhar autoridade no assunto.

- **Nome do livro:** *Sistemas de Informação Gerenciais*
- **Capítulo:** Capítulos 1 (SI nos negócios), 2 (e-business) e 6 (banco de dados)
- **Autores:** Kenneth Laudon e Jane Laudon
- **Editora:** Pearson
- **Link de acesso:** BV UniFECAF — https://fecaf.brightspace.com/d2l/home (BV Professor)
- **Aula em que entra:** Aulas 1 a 4

### Para mergulhar no assunto

> Recomendo o filme **"O Jogo da Imitação"** (2014), sobre Alan Turing, disponível em algumas plataformas gratuitas e em trechos no YouTube. Mostra como o conceito de **processar informação por máquina** nasceu — base intelectual de tudo o que estudamos hoje em SI e IA. Conectar passado e presente ajuda a entender por que esses conceitos são tão poderosos.

- **Link(s):** https://www.youtube.com/results?search_query=jogo+da+imita%C3%A7%C3%A3o+trailer (trailer + análises gratuitas)
- **Aula em que entra:** Aula 1 ou 4

### Podcast (curadoria, até 45 min)

> O podcast **"TecMasters Tech Insider"** discute tecnologia empresarial em linguagem acessível. O episódio recomendado fala sobre ERP, sistemas de informação e o impacto na produtividade — com exemplos de empresas brasileiras.

- **Nome do podcast:** TecMasters Tech Insider
- **Nome do episódio:** "ERP — entendendo o que move a empresa moderna"
- **Link:** https://www.youtube.com/@TecMasters
- **Aula em que entra:** Aula 3

### Artigo científico

> Artigo de revisão sobre o papel dos sistemas de informação na manufatura, com foco em empresas brasileiras. Excelente leitura para defender pontos com base em pesquisa nacional.

- **Link:** https://doi.org/10.1590/0103-6513.20160079
- **Aula em que entra:** Aula 4
- **Referência bibliográfica do artigo no formato ABNT:**
  > MENDES, Glauco Henrique de Sousa; LIMA, Edson Pinheiro de. **Avaliação de modelos para implementação de sistemas integrados de gestão (ERP) em pequenas e médias empresas industriais**. *Produção*, v. 27, p. e20160079, 2017.
