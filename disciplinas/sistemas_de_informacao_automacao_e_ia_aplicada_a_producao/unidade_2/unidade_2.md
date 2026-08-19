# Unidade 2 — Sistemas para a Produção

- **Disciplina:** Sistemas de Informação, Automação e IA Aplicada à Produção
- **Conteudista:** Afonso Cesar Lelis Brandão
- **Videoaulas desta unidade:** 5 a 8

> **Recap da Unidade 1:** vimos a pirâmide DIKW (dado → informação → conhecimento → sabedoria), entendemos o que é um sistema de informação (5 componentes), conhecemos os tipos clássicos (TPS, MIS/BI, DSS, EIS, ERP) e abrimos a caixa-preta dos bancos de dados. Agora vamos descer ao **chão de fábrica** e ver os sistemas **específicos da produção** — ERP, MES, SCM/WMS, CRM/PLM — em ação.

---

## Aula 5 — ERP na manufatura: SAP, TOTVS e o fluxo integrado

O **ERP** já apareceu várias vezes na disciplina. Agora vamos abri-lo de verdade — entender como ele funciona na manufatura, quais módulos importam para o engenheiro de produção, quem domina o mercado brasileiro e como ele realmente impacta a operação no dia a dia.

### A história rápida do ERP

ERP é a evolução de sistemas mais antigos. A linhagem:

- **Anos 1960** — **MRP** (Material Requirements Planning) — apenas planejamento de necessidade de materiais.
- **Anos 1980** — **MRP II** (Manufacturing Resource Planning) — MRP + chão de fábrica + capacidade.
- **Anos 1990** — **ERP** (Enterprise Resource Planning) — MRP II + finanças + RH + vendas + tudo integrado.
- **2000+** — **ERP em nuvem, ERP modular, ERP especialista por setor**.

A SAP (Alemanha) e a Oracle (EUA) são as gigantes globais. No Brasil, **TOTVS** domina o mercado de PME e médio porte.

![Sede mundial da SAP em Walldorf, Alemanha — uma das duas maiores empresas globais de software ERP](https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/SAP_AG_headquarter_Walldorf_building_1.jpg/960px-SAP_AG_headquarter_Walldorf_building_1.jpg)

### Os módulos clássicos de um ERP de manufatura

Um ERP industrial típico tem **6 a 12 módulos** principais. Os mais relevantes para você como engenheiro(a) de produção:

| Módulo | Para que serve |
| --- | --- |
| **Vendas / Pedidos (SD)** | Registra pedido do cliente |
| **Planejamento (PP)** | Calcula ordens de produção, capacidade, MRP |
| **Materiais (MM)** | Estoque, compras, lista de materiais (BOM) |
| **Produção (PM)** | Ordens em execução, custo do produto |
| **Qualidade (QM)** | Planos de inspeção, certificados de qualidade |
| **Manutenção (PM)** | Ordens preventivas e corretivas |
| **Finanças (FI/CO)** | Contabilidade, custos, faturamento |
| **RH (HR)** | Folha de pagamento, ponto, treinamento |

Os módulos **conversam entre si** pela base única — quando o **PP** programa uma ordem, ele consulta **MM** (tem matéria-prima?), **HR** (tem mão de obra?), **PM** (a máquina está disponível?) e atualiza tudo automaticamente.

### O fluxo integrado: pedido → produção → entrega → financeiro

Vamos ver na prática como um pedido atravessa o ERP:

1. **Cliente faz pedido** (módulo SD) → 1.000 peças do produto X em 15 dias.
2. **MRP calcula** (módulo PP): para fazer 1.000 X, precisa de 5.000 unidades de Y e 3.000 de Z; quanto tempo de máquina A; quem trabalha quando.
3. **MM verifica estoque** — tem Y, mas falta Z; gera ordem de compra automática.
4. **PP gera ordem de produção** — programa máquina A, equipe X, prazo Y.
5. **Produção (PM)** registra início, paradas, fim, refugo.
6. **QM** registra inspeções de qualidade nas amostras.
7. **MM** dá baixa nas matérias-primas e entrada do produto acabado no estoque.
8. **SD emite nota fiscal**, expedição programada.
9. **FI/CO** apropria custos da ordem (matéria, mão de obra, energia, depreciação) e fatura para o cliente.
10. **HR** registra horas trabalhadas, integra com folha.

Esse é o **ciclo completo** que um ERP coordena — em uma empresa madura, **tudo isso roda sem ninguém duplicar dado em planilha**.

### Os grandes players do mercado

**Internacionais:**

- **SAP** — líder global, padrão em multinacionais. Caro, complexo, robusto.
- **Oracle** (NetSuite, Fusion) — segundo lugar global.
- **Microsoft Dynamics** — forte em empresas de pequeno e médio porte global.
- **Infor** — especializado em setores específicos.

**Brasileiros:**

- **TOTVS** — Protheus (médio/grande porte), Datasul (industrial), RM (administrativo). Líder do mercado brasileiro.
- **Sankhya** — cresceu muito nos últimos anos, médio porte.
- **Senior Sistemas** — forte em RH, espalhando-se para outros módulos.

**Open source / nuvem leve:**

- **Odoo** — modular, código aberto, custo acessível para PME.
- **ERPNext** — também open source, ganhou tração.

A escolha depende de **porte, setor, integração com legados e orçamento**. Não existe "o melhor ERP" — existe o **mais adequado para o seu contexto**.

### O que é "implantação" e por que demora tanto

"Implantar ERP" não é instalar software. É um projeto com várias frentes:

1. **Mapear processos** (vimos na Unidade 1 — DIKW, e veremos BPM mais à frente).
2. **Configurar o ERP** — parametrizar para refletir os processos da empresa.
3. **Migrar dados** — trazer dados de sistemas legados para o ERP novo.
4. **Treinar equipe** — operadores, supervisores, gerentes.
5. **Validar (UAT — User Acceptance Test)** — usuários testam, encontram bugs.
6. **Go-live** — entrar em produção. Sempre dramático.
7. **Estabilizar** — primeiros 3-6 meses, resolver problemas que só aparecem em produção.

Implantar um ERP em uma fábrica média leva tipicamente **6 a 24 meses**. Investimento: **R\$ 200 mil a vários milhões**. Falha em projetos de ERP é estatisticamente comum — taxas de **30 a 50% de insucesso** em diferentes estudos.

### Customização vs configuração: a armadilha clássica

**Configurar** = ajustar parâmetros do ERP padrão (telas, regras, fluxos pré-existentes).
**Customizar** = mudar o código-fonte para atender necessidade exclusiva.

Customização **traz três problemas**:

1. **Atualizações futuras quebram** — você fica preso à versão antiga.
2. **Custo de manutenção explode** — cada upgrade exige re-customização.
3. **Conhecimento concentrado em poucas pessoas** — quando elas saem, ninguém entende.

A regra de ouro: **80% do que parece "específico da empresa" é, na verdade, processo mal mapeado**. Conserte o processo, e o ERP padrão atende.

### Exemplo numérico: ROI realista de ERP em PME

Fábrica de 400 funcionários, faturamento R\$ 90 milhões/ano, sem ERP integrado.

**Investimento:**

- Licenças TOTVS Protheus: R\$ 350 mil (one-time + recorrente).
- Implantação (consultoria + parametrização): R\$ 500 mil.
- Infraestrutura (nuvem ou servidores): R\$ 80 mil/ano.
- Treinamento: R\$ 70 mil.
- **Total ano 1:** ~R\$ 1 milhão.

**Ganhos no primeiro ano:**

- Redução de retrabalho/reconciliação: R\$ 80 mil/ano.
- Redução de perdas de estoque: R\$ 150 mil/ano (3% de melhoria em R\$ 5 mi/ano de estoque).
- Redução de erros fiscais e multas: R\$ 50 mil/ano.
- Aumento de velocidade de cotação: ganho de 5% em receita = R\$ 4,5 mi/ano (ganho conservador).
- **Total ano 1:** ~R\$ 700 mil + ganho de receita gradual.

**Payback estimado:** 18-30 meses, dependendo do quanto se aproveita do ERP.

Esses números são **conservadores** — muitos casos reais entregam payback em 12 meses quando há uso intenso.

### Atividade prática

Para a empresa que você analisou na U1:

1. Quais **módulos de ERP** essa empresa tem (formal ou informalmente, em planilhas)?
2. Há **integração** real entre eles? Quais "ilhas" você identifica?
3. Que **fluxo** (pedido → produção → entrega → financeiro) está mais quebrado?
4. Se você fosse implantar ERP, em **qual ordem** ativaria os módulos?

### Pontos-chave

- **ERP** evoluiu de MRP → MRP II → ERP → ERP em nuvem.
- Módulos clássicos: **Vendas, Planejamento, Materiais, Produção, Qualidade, Manutenção, Finanças, RH**.
- Em ERP maduro, **todos os módulos conversam** — sem duplicação.
- Mercado dominado por **SAP, Oracle, Microsoft, TOTVS, Sankhya**.
- **Implantar ERP** = projeto de 6-24 meses, R\$ 200 mil a milhões; falha em 30-50% dos casos.
- **Configuração > customização** — customizar gera dor de longo prazo.

### Para saber mais

- **Norris, G.** *E-Business and ERP*. Wiley.
- **TOTVS — Blog educativo:** https://www.totvs.com/blog/
- **SAP for Manufacturing:** https://www.sap.com/products/scm.html
- **Vídeo (Curso TI Total, YouTube):** "ERP — o que é, para que serve, como implantar"

---

## Aula 5 — Roteiro da Videoaula 5: "ERP na manufatura: a espinha dorsal da fábrica moderna"

**Duração:** 9 a 11 minutos.

### 1. Abertura (0:00 – 0:40)

> "Toda empresa de médio porte para cima vive em torno do ERP — o sistema que junta tudo: pedido, produção, estoque, financeiro, RH. Hoje você vai entender por dentro como ele funciona e por que é tão decisivo."

### 2. História (MRP → MRP II → ERP) (0:40 – 2:00)

- Evolução de 60 anos.
- SAP e Oracle como gigantes globais; TOTVS como líder brasileiro.

### 3. Módulos e fluxo integrado (2:00 – 6:00)

- Listar os módulos principais.
- Caminhar pelo fluxo "pedido → produção → entrega → financeiro" em 10 passos.

### 4. Mercado e implantação (6:00 – 8:30)

- Players principais (SAP, Oracle, TOTVS).
- Por que implantar leva 6-24 meses.
- A armadilha customização vs configuração.

### 5. Encerramento + gancho U6 (8:30 – 11:00)

> "Próxima aula: o **MES** — o sistema que faz o **chão de fábrica** falar com o ERP. Você vai entender por que MES + ERP é hoje o dueto mais importante da TI industrial. Te espero!"

---

## Aula 6 — MES (Manufacturing Execution System)

Você ouviu o nome MES várias vezes — agora vamos abrir. Esta aula explica o que é, por que existe, como se conecta ao ERP e por que é tão importante para a engenharia de produção moderna.

### O que é MES, em uma frase

> **MES** (Manufacturing Execution System) é o sistema que **gerencia, monitora e otimiza a execução da produção em tempo real**, conectando o ERP (mundo de negócio) ao chão de fábrica (mundo físico).

Imagine o ERP dizendo: "produza 1.000 peças do produto X, começando amanhã, 8h, na linha 2". É o **MES** que **executa** isso: orienta os operadores, monitora as máquinas, registra o que aconteceu de fato, alerta sobre desvios e devolve ao ERP os números reais.

### O lugar do MES na pirâmide ISA-95

Existe uma norma internacional — **ISA-95** — que define uma **pirâmide** de níveis de TI/automação:

| Nível | Sistema | Foco |
| --- | --- | --- |
| **4** | **ERP / Business Planning** | Planejamento de negócio (semanas/meses) |
| **3** | **MES / MOM** | Execução de manufatura (turnos/horas) |
| **2** | **SCADA / HMI** | Supervisão de processo (segundos/minutos) |
| **1** | **CLP / DCS** | Controle de equipamento (milissegundos) |
| **0** | **Equipamento físico** | Sensores e atuadores |

MES está no **nível 3** — meio do caminho. Vai falar de nível 1 e 2 na próxima Unidade.

![Operadores em sala de controle industrial — onde MES, SCADA e operadores se encontram para coordenar a execução da produção](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Power_plant_operators_st_work.jpg/960px-Power_plant_operators_st_work.jpg)

### As 11 funções clássicas de um MES (ISA-95)

A norma define 11 funções:

1. **Alocação de recursos** — quem (máquina, pessoa, ferramenta) faz o quê.
2. **Sequenciamento de ordens** — ordem em que as ordens entram.
3. **Despacho de ordens** — liberação para execução.
4. **Gestão de documentos** — instruções de trabalho, desenhos.
5. **Coleta de dados** — registro do que aconteceu.
6. **Gestão da mão de obra** — habilidades, certificações, presença.
7. **Gestão da qualidade** — inspeções e desvios.
8. **Gestão do processo** — receitas, parâmetros operacionais.
9. **Gestão da manutenção** — preventivas e corretivas.
10. **Rastreabilidade** — quem fez, quando, com o quê.
11. **Análise de performance** — OEE, MTBF, taxas de defeito.

Você não precisa decorar — mas saber que essas 11 funções existem ajuda quando ler um RFP de MES.

### MES vs ERP: a divisão clara

Vamos repetir a comparação (porque é base):

| Aspecto | ERP | MES |
| --- | --- | --- |
| **Foco** | Negócio (pedido, fatura, RH) | Chão de fábrica (execução) |
| **Granularidade** | Tarefa | Operação individual |
| **Frequência** | Diária / semanal | Tempo real (segundos) |
| **Usuários típicos** | Compras, finanças, vendas, gerência | Operadores, supervisores, manutenção |
| **Indicadores** | Faturamento, margem, OTIF | OEE, MTBF, refugo |
| **Vida útil típica** | 8-15 anos | 5-10 anos |

E o ponto crítico: **devem se integrar**. ERP planeja, MES executa, MES devolve dados ao ERP. Sem essa integração, há **ilhas** — ERP não sabe o que está acontecendo na fábrica em tempo real, fábrica não sabe o que o ERP programou.

### Indicadores que o MES gera

**OEE (Overall Equipment Effectiveness)** — o indicador clássico:

```
OEE = Disponibilidade × Performance × Qualidade
```

Onde:

- **Disponibilidade** = tempo real produzindo / tempo planejado.
- **Performance** = velocidade real / velocidade nominal.
- **Qualidade** = peças boas / peças produzidas.

OEE de classe mundial = **85%+**. Maioria das fábricas brasileiras = **60-75%**. Cada **1 p.p.** de OEE costuma valer milhões em fábricas médias.

Outros indicadores:

- **MTBF** (Mean Time Between Failures) — tempo médio entre falhas.
- **MTTR** (Mean Time To Repair) — tempo médio para reparar.
- **PPM** (Partes Por Milhão de defeito).
- **Takt time** — ritmo de produção alinhado à demanda.

### Players de mercado

- **Siemens Opcenter (ex-Camstar)** — top de linha.
- **GE Proficy Plant Applications** — forte em manufatura discreta.
- **Honeywell MES** — química e processo.
- **Rockwell FactoryTalk** — forte em automação.
- **PPI Multitask, Plant Star Brasil** — players nacionais com bom custo-benefício.
- **TOTVS Linha de Produção** — integrado ao TOTVS ERP.

### Exemplo numérico: ROI de implantar MES em 3 linhas

Fábrica metalúrgica com **3 linhas críticas**, OEE médio de **65%**.

**Antes do MES:**

- Apontamento manual de produção (operador anota em ficha de papel).
- Identificação de paradas: por entrevista, com 2-3 dias de atraso.
- OEE calculado mensalmente, com viés (operadores subestimam paradas).

**Com MES:**

- Apontamento automático (sensores ligados às máquinas + interfaces para causa).
- Identificação de causa de parada em tempo real.
- OEE calculado em tempo real, sem viés.
- Após 6 meses: identificadas as 5 maiores causas de parada; eliminada a maior (troca de ferramenta sem padronização).
- **OEE sobe de 65% para 72%** em 8 meses (+7 p.p.).
- Cada 1 p.p. de OEE = ~R\$ 150 mil/ano em receita extra (linha custa R\$ 300 mil/mês operando 1 turno).
- Ganho anual: **+7 × R\$ 150 mil = R\$ 1,05 milhão/ano**.

**Investimento típico:**

- Sensores e gateways em 3 linhas: R\$ 200 mil.
- Licença MES (anual): R\$ 100 mil.
- Implantação: R\$ 300 mil.
- **Total:** ~R\$ 600 mil + R\$ 100 mil/ano.

**Payback:** ~7-9 meses. **Excelente.**

### Caso brasileiro: MES na Klabin

A **Klabin** (celulose, Telêmaco Borba-PR) implementou MES integrado com sensores em 1.500+ pontos. O MES é o **cérebro operacional** que recebe os dados, alimenta digital twin, manda comando de volta às máquinas. Resultado documentado: +8% de produtividade, -22% de paradas (já vimos esse caso na disciplina de I4.0; aqui repetimos pelo recorte de SI).

### Atividade prática

Para uma linha de produção que você conhece:

1. Qual é o **OEE atual**? (Disponibilidade × Performance × Qualidade)
2. Qual o **gargalo principal** — disponibilidade, performance ou qualidade?
3. Quais **5 dados** seriam mais úteis em tempo real?
4. Como um **MES** mudaria a operação dessa linha?

### Pontos-chave

- **MES** executa o que o ERP planejou — está no **nível 3** da pirâmide ISA-95.
- A norma ISA-95 define **11 funções** clássicas do MES.
- **OEE** é o indicador clássico — **Disponibilidade × Performance × Qualidade**; classe mundial ≥ 85%.
- ERP **planeja**; MES **executa**; ambos devem se **integrar**.
- ROI típico de MES é rápido (6-12 meses) quando bem implantado.

### Para saber mais

- **Site ISA (norma ISA-95):** https://www.isa.org/standards-and-publications/isa-standards/isa-standards-committees/isa95
- **Vídeo (Senai SC, YouTube):** "O que é MES? Para que serve?"
- **Portal Siemens MOM:** https://www.plm.automation.siemens.com/global/en/products/manufacturing-operations-center/
- **Webinar (Rockwell):** "MES Best Practices" — disponível em rockwellautomation.com

---

## Aula 6 — Roteiro da Videoaula 6: "MES — a cola entre o ERP e o chão de fábrica"

**Duração:** 9 a 11 minutos.

### 1. Abertura (0:00 – 0:30)

> "Você conheceu o ERP na aula passada — o sistema do escritório. Agora vamos conhecer o irmão dele que mora no chão de fábrica: o **MES**. Sem MES, ERP é cego em relação à produção."

### 2. O lugar do MES (pirâmide ISA-95) (0:30 – 3:00)

- Mostrar a pirâmide (5 níveis).
- MES no nível 3.
- Por que cada nível tem granularidade temporal diferente.

### 3. As 11 funções do MES (3:00 – 5:30)

- Listar, com exemplo curto de cada uma.
- Reforçar: rastreabilidade e OEE são as mais valiosas.

### 4. OEE e indicadores (5:30 – 8:30)

- Fórmula do OEE.
- Caso: linha de 65% para 72% = +R\$ 1 milhão/ano.

### 5. Encerramento + gancho U7 (8:30 – 11:00)

> "Próxima aula: como o **SCM e WMS** governam a logística — a outra metade do quebra-cabeça. Te espero!"

---

## Aula 7 — SCM e WMS: logística e gestão de estoque

> **Pausa para reflexão:** se sua fábrica produz com perfeição mas o cliente recebe atrasado, o cliente vai elogiar o quê? Pensa nisso enquanto avançamos.

Na fábrica, **produzir bem não basta**. É preciso garantir que a matéria-prima chega no momento certo e que o produto acabado sai para o cliente no prazo. Esse é o domínio do **SCM** (gestão da cadeia de suprimentos) e do **WMS** (gestão de armazém). Esta aula abre os dois.

### SCM — Supply Chain Management

> **SCM** (Supply Chain Management) é a gestão integrada de todos os elos da **cadeia de suprimentos**: fornecedores, fabricantes, distribuidores, varejistas e consumidor final.

SCM **não é apenas software** — é uma disciplina ampla de gestão. Mas existe um tipo de sistema chamado **Sistema SCM** (ou módulo SCM dentro do ERP) que apoia decisões nessa cadeia:

- Quando comprar matéria-prima? De quem? Em que quantidade?
- Onde produzir? Quando?
- Como distribuir o produto acabado?
- Como prever a demanda?
- Como reagir a interrupções (greves, pandemias, conflitos)?

### Os elos da cadeia

Numa fábrica média, a cadeia pode ter:

```
Fornecedor de minério → Fornecedor de aço → Fornecedor de chapa → 
Sua fábrica → Distribuidor → Varejista → Consumidor final
```

Quanto **mais elos**, mais riscos. Cada elo tem **lead time** (tempo de resposta), **custo**, **qualidade** e **risco**. SCM moderna tenta **visibilidade ponta a ponta** — saber em tempo real onde está cada material.

### Conceitos centrais

**Lead time** — tempo entre fazer pedido e receber. Quanto **menor**, melhor.

**Estoque de segurança** — quantidade extra mantida para absorver imprevistos. Quanto **maior**, mais seguro mas mais caro.

**Bullwhip effect (efeito chicote)** — pequenas variações de demanda no consumidor final se amplificam à medida que sobem na cadeia, fazendo o fornecedor de matéria-prima sofrer oscilações enormes. **Sistemas SCM modernos** reduzem o efeito chicote por compartilhamento de informação.

**JIT (Just In Time)** — modelo japonês — receber matéria-prima **no exato momento** em que vai usar, sem estoque grande. Reduz custo, mas exige fornecedores ultraconfiáveis.

### Visibilidade da cadeia: o sonho da Indústria 4.0

Hoje, o estado da arte é a **visibilidade ponta a ponta** — sistemas SCM modernos integrados com **IoT** rastreiam materiais em tempo real:

- Container vindo da China — onde está agora?
- Caminhão chegando — quanto tempo até o portão?
- Estoque no varejista — quanto está vendendo?

Empresas como **Amazon e Maersk** dominam isso. No Brasil, **Ambev e Magazine Luiza** estão entre as mais avançadas.

![Centro de distribuição moderno: o palco onde WMS, AGVs e SCM se materializam em corredores, paletes e operações de picking](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Modern_warehouse_with_pallet_rack_storage_system.jpg/960px-Modern_warehouse_with_pallet_rack_storage_system.jpg)

### WMS — Warehouse Management System

> **WMS** (Warehouse Management System) é o sistema que gerencia **armazéns** — entrada, armazenagem, separação (picking), embalagem e expedição.

O WMS é o **MES do armazém** — em vez de máquinas, gerencia caminhões, empilhadeiras, AGVs, esteiras e estantes.

### As 5 operações de um armazém moderno

1. **Recebimento** — conferência de cargas que chegam.
2. **Armazenagem (put-away)** — onde guardar cada item (otimizado por rotatividade, peso, fragilidade).
3. **Picking (separação)** — separar pedidos para expedição. Aqui mora 50-60% do custo do armazém.
4. **Packing (embalagem)** — embalar pedido para envio.
5. **Expedição** — saída para o cliente, com nota fiscal e rastreamento.

WMS otimiza **cada uma** dessas etapas. Em armazéns avançados, picking é assistido por:

- **Pick-by-light** — luzes na prateleira indicam a peça.
- **Pick-by-voice** — comando por áudio.
- **AGVs/AMRs** — robôs móveis trazem as peças até o picker (estilo Amazon Kiva).
- **Realidade Aumentada** — óculos guiam o picker (vimos na disciplina de I4.0).

### Diferença ERP vs SCM vs WMS

| Aspecto | ERP | SCM | WMS |
| --- | --- | --- | --- |
| **Foco** | Negócio interno | Toda a cadeia | Armazém específico |
| **Escopo geográfico** | Empresa | Fornecedores + clientes | Um galpão |
| **Granularidade** | Pedido | Cadeia inteira | Caixa, palete, item |
| **Integra com** | Tudo | ERP, fornecedores, transporte | ERP, MES, transporte |

Em uma fábrica média, **ERP é o coração; SCM e WMS são extensões** especializadas.

### Exemplo numérico: economia em otimização de picking

Armazém com **10 funcionários de picking**, cada um separando 200 pedidos/dia. Custo por funcionário: R\$ 3.500/mês.

**Sem WMS otimizado:**

- Distância média percorrida por pedido: 180 metros.
- Tempo médio: 4 min/pedido.
- 200 pedidos × 4 min = 800 min = **13,3 horas/dia** (saturado).
- Erros de picking: 1,5%.

**Com WMS otimizado (sequência de picking, rotas inteligentes):**

- Distância média: 100 metros (-45%).
- Tempo médio: 2,5 min/pedido.
- 200 pedidos × 2,5 min = 500 min = **8,3 horas/dia**.
- Erros: 0,3% (-80%).

**Ganhos:**

- Cada funcionário libera 5 horas/dia → reorganização permite produzir mais pedidos OU reduzir time.
- Redução de erros: R\$ 50 mil/ano economizados em retrabalho/devolução.
- Capacidade do armazém aumenta em ~40% sem investimento físico.

**Investimento típico em WMS PME:** R\$ 80-300 mil de implantação + R\$ 30-80 mil/ano de licença.

### Atividade prática

Para uma operação que você conhece (ou imagine uma):

1. Quantos **elos** tem a cadeia da matéria-prima ao cliente final?
2. Onde está o maior **risco** (lead time, fornecedor único, falta de visibilidade)?
3. Como funciona o **armazém** — manual ou com WMS?
4. Que **otimização** de picking traria maior impacto?

### Pontos-chave

- **SCM** gerencia toda a cadeia (fornecedores → cliente final); **WMS** gerencia um armazém específico.
- Conceitos centrais: **lead time, estoque de segurança, bullwhip effect, JIT**.
- Visibilidade ponta a ponta com **IoT integrado** é o estado da arte.
- Em armazéns, **picking** representa 50-60% do custo; tecnologia (pick-by-light, AGVs) otimiza.
- ROI típico de WMS: ganho de **40-60% de capacidade** sem investimento físico adicional.

### Para saber mais

- **Bowersox, D.; Closs, D.; Cooper, M.** *Gestão Logística da Cadeia de Suprimentos*. AMGH.
- **Site ABRALOG (Associação Brasileira de Logística):** https://www.abralog.com.br/
- **Vídeo (Tecnologística, YouTube):** "WMS na prática"
- **Caso Amazon Kiva:** https://www.youtube.com/results?search_query=amazon+kiva+robots

---

## Aula 7 — Roteiro da Videoaula 7: "Logística inteligente: SCM e WMS na prática"

**Duração:** 9 a 11 minutos.

### 1. Abertura (0:00 – 0:30)

> "Produzir bem não basta. Se o cliente recebe atrasado, ele te lembra como atrasado, não como bem produzido. Hoje a gente fala dos sistemas que governam a **logística** da fábrica para a frente."

### 2. SCM — visibilidade ponta a ponta (0:30 – 3:30)

- Definir SCM.
- Elos da cadeia.
- Bullwhip effect, lead time, JIT.
- Caso Amazon e Maersk.

### 3. WMS — o "MES do armazém" (3:30 – 6:30)

- 5 operações: recebimento, put-away, picking, packing, expedição.
- Picking é 50-60% do custo.
- Tecnologias: pick-by-light, voice, AGVs (caso Amazon Kiva).

### 4. Exemplo numérico (6:30 – 8:30)

- Armazém com WMS: 40% mais capacidade, -80% erros de picking.

### 5. Encerramento + gancho U8 (8:30 – 11:00)

> "Última aula da unidade: como **CRM, PLM** e demais sistemas verticais fecham o quebra-cabeça da informação na empresa moderna. Te espero!"

---

## Aula 8 — CRM, PLM e a integração da cadeia de informação

Esta aula fecha a Unidade 2 com os **sistemas verticais** que faltam: **CRM** (relacionamento com cliente) e **PLM** (ciclo de vida do produto). Depois, vamos juntar tudo — como ERP, MES, SCM, WMS, CRM e PLM **se integram** em uma empresa madura.

### CRM — Customer Relationship Management

> **CRM** é o sistema que gerencia o **relacionamento com clientes** — cadastros, contatos, oportunidades comerciais, atendimentos, reclamações, fidelização.

CRM é o **olho da empresa para o mercado externo**. Sem ele, conhecimento sobre clientes fica na cabeça de vendedores — e quando o vendedor sai, leva o cliente junto.

### Os 4 pilares do CRM moderno

1. **Operacional** — automação de marketing, vendas e atendimento (chatbots, e-mails, gestão de oportunidades).
2. **Analítico** — análise de comportamento, segmentação, previsão de churn (perda de cliente).
3. **Colaborativo** — atendimento omnichannel (telefone, WhatsApp, e-mail, presencial) com histórico único.
4. **Estratégico** — visão 360° do cliente para tomada de decisão.

### Players principais

- **Salesforce** — líder global, padrão em multinacionais.
- **Microsoft Dynamics 365** — concorrente direto.
- **HubSpot** — popular em PMEs, com versão gratuita.
- **RD Station** (brasileiro) — forte no Brasil para marketing/vendas.
- **TOTVS CRM** — integrado ao ecossistema TOTVS.
- **Pipedrive, Zoho** — opções intermediárias.

### Como CRM impacta a fábrica

Você pode pensar: "CRM é coisa de comercial, não de engenharia de produção". Errado. CRM bem usado **alimenta** a fábrica com:

- **Previsão de demanda** mais precisa → planejamento de produção melhor.
- **Histórico de reclamações** → identifica problemas recorrentes de qualidade.
- **Lead time esperado pelo cliente** → ajusta MES para priorizar.
- **Volumetria de pedidos por região** → otimiza distribuição.

Em uma empresa orientada a dados, **CRM e ERP/MES conversam o tempo todo**.

### PLM — Product Lifecycle Management

> **PLM** (Product Lifecycle Management) é o sistema que gerencia todo o **ciclo de vida de um produto** — desde a ideia inicial, passando pelo projeto, produção, manutenção pós-venda, até o descarte.

PLM nasce na engenharia de produto, mas atravessa toda a empresa:

- **Concepção** — ideia, requisitos, mercado-alvo.
- **Projeto** — desenhos CAD, simulação, prototipagem.
- **Engenharia** — Bill of Materials (BOM), processos, ferramentaria.
- **Produção** — instruções, validações.
- **Pós-venda** — manuais, manutenção, peças de reposição.
- **Descarte** — recuperação, reciclagem (cada vez mais relevante na I5.0).

### Players principais de PLM

- **Siemens Teamcenter** — líder global, integrado com NX (CAD) e Mentor (eletrônica).
- **Dassault Systèmes 3DEXPERIENCE** — forte em automotivo e aeroespacial (cliente: Embraer, Boeing).
- **PTC Windchill** — concorrente direto.
- **Autodesk Fusion 360 / Vault** — popular em PMEs.
- **Oracle Agile** — integrado ao ecossistema Oracle.

### Como PLM impacta a fábrica

PLM é a **fonte de verdade** sobre o produto. Quando bem implantado:

- **BOM única e atualizada** — eliminando divergências entre engenharia e produção.
- **Mudanças rastreadas** — sabe-se quem aprovou cada alteração.
- **Documentação alinhada** — manuais sempre refletem a versão atual.
- **Reuso de componentes** — engenharia evita reinventar o que já existe.

Em multinacionais, **PLM é tão crítico quanto ERP**.

![Engenheiros trabalhando com modelos CAD — o tipo de informação de produto que o PLM organiza, versiona e propaga para toda a empresa](https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/CAD_computer-aided_design.jpg/960px-CAD_computer-aided_design.jpg)

### A arquitetura integrada: o desenho completo

Vamos juntar tudo o que vimos na Unidade 2. Em uma empresa madura, os sistemas se conectam assim:

```
                  ┌──────────┐
                  │   CRM    │  (clientes, demanda, pós-venda)
                  └─────┬────┘
                        ▼
   ┌────────┐     ┌──────────┐     ┌────────┐
   │  PLM   │ →   │   ERP    │  ←  │  SCM   │
   │(produto)│     │(negócio)│     │(cadeia)│
   └────────┘     └─────┬────┘     └────────┘
                        ▼
                  ┌──────────┐
                  │   MES    │  (chão de fábrica)
                  └─────┬────┘
                        ▼
                  ┌──────────┐
                  │   WMS    │  (armazém)
                  └──────────┘
```

Não é só uma figura bonita — é um **mapa** que você deve guardar. Cada empresa começa com um ou dois desses sistemas; à medida que amadurece, integra os outros.

### Integração: o desafio real

A maioria dessas integrações **não vem pronta** — é projeto de TI específico. As três abordagens comuns:

1. **Integração ponto a ponto** — cada sistema fala diretamente com cada outro. Funciona para 2-3 sistemas; cresce em complexidade.
2. **Barramento corporativo (ESB)** — sistema central de mensagens; cada sistema fala só com o ESB. Padrão antigo, mas robusto.
3. **APIs modernas (REST/GraphQL)** — cada sistema expõe APIs; outros consumem. Padrão atual.

Em fábricas modernas, **APIs REST** dominam. Tecnologias como **MuleSoft, Boomi, Microsoft Power Platform** ajudam a integrar.

### Exemplo numérico: economia em integração

Empresa com 5 sistemas (ERP, MES, CRM, WMS, PLM) **sem integração**:

- 4 analistas dedicados a "copiar dado entre sistemas": R\$ 4.000 × 4 = R\$ 16.000/mês = **R\$ 192 mil/ano**.
- Erros de digitação: estimativa de R\$ 100 mil/ano em retrabalho.
- Decisões atrasadas: difícil mensurar — estimativa conservadora de R\$ 300 mil/ano em oportunidades perdidas.
- **Total de "custo da não-integração":** R\$ 590 mil/ano.

Implementar integração via APIs: R\$ 250-500 mil de projeto.

**Payback:** 6-12 meses.

### O que você verá na próxima unidade

Na **Unidade 3**, vamos descer ainda mais — da camada de sistemas de informação para a **automação industrial física**. Vamos entender sensores e atuadores (Aula 9), CLP e lógica ladder (Aula 10), SCADA e supervisão (Aula 11) e fechar com a integração TI-OT pela pirâmide ISA-95 (Aula 12). É a hora de **descer ao físico** que os sistemas de informação coordenam.

### Atividade prática

Para uma empresa que você conhece:

1. Quais sistemas (entre ERP, MES, SCM, WMS, CRM, PLM) existem?
2. Quais **se integram** de verdade? E quais são "ilhas"?
3. Onde está a **maior perda** com a falta de integração?
4. Por **onde começaria** uma integração de baixo custo?

### Pontos-chave

- **CRM** gerencia o relacionamento com cliente; **PLM** gerencia o ciclo de vida do produto.
- CRM impacta a fábrica via **previsão de demanda, qualidade e priorização**.
- PLM é a **fonte de verdade** sobre o produto — BOM, mudanças, documentação.
- Em uma empresa madura, **ERP + MES + SCM + WMS + CRM + PLM** trabalham integrados.
- A maioria das **integrações** entre sistemas é via **APIs REST modernas**; ROI tipicamente em 6-12 meses.

### Para saber mais

- **Salesforce — recursos educativos:** https://www.salesforce.com/br/resources/
- **Siemens PLM:** https://www.plm.automation.siemens.com/global/en/
- **Vídeo (Endeavor, YouTube):** "Como o CRM transforma a empresa"
- **Curso gratuito Coursera:** Customer Relationship Management — https://www.coursera.org/

---

## Aula 8 — Roteiro da Videoaula 8: "CRM, PLM e a sinfonia dos sistemas integrados"

**Duração:** 9 a 11 minutos.

### 1. Abertura (0:00 – 0:30)

> "ERP, MES, SCM, WMS... e ainda tem CRM e PLM. Hoje a gente fecha a sopa de letrinhas — e mostra como tudo isso, integrado, vira o **sistema nervoso** da empresa moderna."

### 2. CRM (0:30 – 3:00)

- Definir e dar exemplos (Salesforce, HubSpot, RD Station).
- Como CRM impacta a fábrica (previsão de demanda, qualidade, lead time).

### 3. PLM (3:00 – 5:30)

- Definir e dar exemplos (Siemens, Dassault, PTC).
- Ciclo do produto: ideia → projeto → produção → pós-venda → descarte.

### 4. Arquitetura integrada (5:30 – 8:30)

- Mostrar o diagrama completo.
- Reforçar: cada elemento é uma peça; integração é projeto.
- Exemplo numérico: custo da não-integração ~R\$ 590 mil/ano.

### 5. Encerramento + gancho U3 (8:30 – 11:00)

> "Próxima unidade: descemos da camada de sistemas para a **automação industrial física**. Sensor, atuador, CLP, SCADA. Te espero!"

---

## Quiz não avaliativo

### Questão 1

Sobre a **norma ISA-95** e o lugar do MES, assinale a alternativa **correta**:

- [ ] a. A ISA-95 define que o ERP está no nível 0 (equipamento físico) e que o CLP está no nível 4 (negócio).
- [x] b. A ISA-95 organiza a fábrica em 5 níveis hierárquicos: ERP (nível 4) → MES (nível 3) → SCADA (nível 2) → CLP (nível 1) → equipamento (nível 0); cada nível tem uma granularidade temporal e função distintas.
- [ ] c. A ISA-95 elimina a necessidade de MES e SCADA, fundindo tudo no ERP.
- [ ] d. A ISA-95 tem apenas 2 níveis: TI e OT.

**Resposta correta:** `b`

**Feedback:** A (b) descreve corretamente a pirâmide. Cada nível tem **granularidade temporal** específica (segundos no nível 0, milissegundos no CLP, minutos no SCADA, horas no MES, dias no ERP). A (a) inverte a pirâmide. A (c) é o oposto: a ISA-95 reforça a importância de **cada nível**. A (d) é simplista demais — ainda que TI e OT existam, a pirâmide tem 5 níveis distintos.

### Questão 2

A respeito do **OEE** (Overall Equipment Effectiveness), assinale a alternativa **correta**:

- [ ] a. OEE é calculado como Velocidade × Custo, sem considerar disponibilidade ou qualidade.
- [ ] b. OEE de classe mundial está em torno de 40%, e qualquer valor acima disso é exceção.
- [x] c. OEE = Disponibilidade × Performance × Qualidade. Valores de classe mundial estão em torno de 85%+; a maioria das fábricas brasileiras opera entre 60-75%.
- [ ] d. OEE não é um indicador relevante em fábricas modernas, sendo substituído integralmente pelo OEE3 (indicador hipotético).

**Resposta correta:** `c`

**Feedback:** A (c) é a definição clássica do OEE — fórmula correta e referências realistas. A (a) é falsa: OEE não considera custo diretamente. A (b) inverte a referência: 40% é OEE crítico, não classe mundial. A (d) é falsa: OEE permanece como **indicador clássico** em qualquer MES moderno.

---

## Atividade Verificadora (AAI — Atividade Avaliativa Individual)

**Pergunta:**

> Considere uma empresa de manufatura de **médio porte** (400 funcionários) que tem **ERP TOTVS Protheus implantado** há 5 anos, mas que opera **sem MES, sem CRM, sem PLM** — apenas com planilhas auxiliares. A diretoria pergunta a você qual seria o **próximo passo** de TI a investir, com orçamento de até R\$ 1 milhão no próximo ano.
>
> Estruture sua resposta em três partes:
>
> 1. **Recomendação** — qual sistema priorizar (MES / CRM / PLM ou combinação)? Justifique técnica e estrategicamente.
> 2. **Plano de implementação** — quais etapas, com prazos e investimentos realistas?
> 3. **Indicadores de sucesso** — quais KPIs acompanhar nos primeiros 12 meses?

**Resposta esperada:**

> Resposta de qualidade tipicamente recomenda **MES** primeiro — porque é o sistema que **fecha o ciclo** com o ERP existente, traz dados em tempo real do chão de fábrica e tem ROI rápido em fábricas que apontam manualmente. Investimento realista: R\$ 400-700 mil + licença anual de R\$ 80-150 mil. Etapas: piloto em 1-2 linhas críticas (3-4 meses) → expansão progressiva (6-9 meses). KPIs principais: subir OEE (alvo: +5 a 10 p.p.), reduzir paradas não programadas (alvo: -25%), reduzir refugo (alvo: -15%), reduzir tempo de coleta de dados (de horas para minutos). A resposta deve demonstrar **pensamento sistêmico**: o ganho não é só do MES isolado — é da combinação ERP + MES. CRM e PLM podem ser próximos passos (anos seguintes), priorizados conforme dores de comercial ou engenharia. Texto deve evitar "vamos implantar tudo" e justificar **uma escolha** com argumentos sólidos.

---

## Material complementar

### Direto da fonte — livro da Biblioteca Virtual

> Este é o capítulo que mais se aproxima do coração da Unidade 2: os **aplicativos integrados** que vimos em ação — ERP, SCM e CRM. Laudon e Laudon mostram como essas suítes coordenam pedido, produção, cadeia de suprimentos e relacionamento com o cliente para alcançar excelência operacional. Leitura direta sobre o que destrinchamos nas Aulas 5 a 8.

- **Nome do livro:** *Sistemas de Informação Gerenciais* (7ª edição)
- **Capítulo:** Capítulo 8 — *Conquistando excelência operacional e intimidade com o cliente: aplicativos integrados* (p. 262)
- **Autores:** Kenneth C. Laudon e Jane P. Laudon (trad. Thelma Guimarães; rev. Belmiro do Nascimento João)
- **Editora:** Pearson Prentice Hall
- **Link de acesso (BV):** https://plataforma.bvirtual.com.br/Acervo/Publicacao/375
- **Aula em que entra:** Aulas 5 a 8

### Para mergulhar no assunto

> Recomendo o documentário **"Inside Amazon's Smart Warehouse"**, da CNBC, disponível em trechos no YouTube. Mostra o WMS da Amazon em operação, com AGVs Kiva, picking otimizado e integração com SCM global. Visualizar a escala real ajuda a entender o estado da arte.

- **Link(s):** https://www.youtube.com/results?search_query=amazon+warehouse+documentary
- **Aula em que entra:** Aula 7

### Podcast (curadoria, até 45 min)

> O podcast **"Logística Descomplicada"** discute SCM e WMS em linguagem prática, com entrevistas de gestores de empresas brasileiras. Excelente para fixar conceitos com casos reais.

- **Nome do podcast:** Logística Descomplicada
- **Nome do episódio:** "WMS na prática — como escolher e implantar"
- **Link:** https://www.youtube.com/@logisticadescomplicada
- **Aula em que entra:** Aula 7

### Artigo científico

> Artigo sobre os efeitos da filosofia **lean** nas cadeias de suprimentos, explorando como a orientação à aprendizagem e os recursos relacionais influenciam o desempenho. Leitura essencial para defender argumentos sobre integração e coordenação na cadeia.

- **Link:** https://doi.org/10.1016/j.ijpe.2019.04.012
- **Aula em que entra:** Aula 6
- **Referência bibliográfica do artigo no formato ABNT:**
  > IYER, Karthik N. S.; SRIVASTAVA, Prashant; SRINIVASAN, Mahesh. **Performance implications of lean in supply chains: exploring the role of learning orientation and relational resources**. *International Journal of Production Economics*, v. 216, p. 94-104, out. 2019.
