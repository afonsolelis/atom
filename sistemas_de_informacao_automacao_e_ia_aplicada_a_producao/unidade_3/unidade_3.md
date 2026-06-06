# Unidade 3 — Automação Industrial

- **Disciplina:** Sistemas de Informação, Automação e IA Aplicada à Produção
- **Conteudista:** Afonso Cesar Lelis Brandão
- **Videoaulas desta unidade:** 9 a 12

> **Recap:** vimos a base de SI (U1) e os sistemas verticais que rodam a empresa (U2). Agora **descemos do nível corporativo para o chão de fábrica físico** — sensores, atuadores, CLPs, SCADA. É a parte de **automação industrial**, sem a qual nenhuma fábrica moderna funciona.

---

## Aula 9 — Fundamentos de automação: sensores, atuadores e controladores

Antes de tudo, vamos alinhar vocabulário. Esta aula trata dos **três blocos elementares** da automação industrial: **sensor** (capta o mundo), **atuador** (age sobre o mundo) e **controlador** (decide o que fazer). Sem entender isso, nenhuma das próximas aulas faz sentido.

### A definição em uma frase

> **Automação industrial** é o uso de **sistemas de controle** para operar equipamentos e processos com **mínima ou nenhuma intervenção humana** direta — substituindo trabalho repetitivo, perigoso ou de alta precisão.

A automação **não é nova** — existe desde a Segunda Revolução Industrial. O que muda na Indústria 4.0 é a **integração** dela com dados, internet e IA. Mas a base **continua a mesma**: sensor → controlador → atuador.

### O ciclo básico de controle

Toda automação industrial segue o **ciclo fechado de controle**:

```
       ┌─────────────────────────────────────────────────────┐
       │                                                     │
       │            ┌──────────────┐                         │
       │            │  Controlador  │                         │
       │  Sinal     │ (CLP/PC/PID) │   Comando               │
       │ medido     └──────┬───────┘   ↓                     │
       │            ▲                                         │
       ▼            │                                         ▼
┌────────────┐      │                              ┌──────────────┐
│   Sensor   │ ─────┘                              │   Atuador     │
│  (mede)    │                                     │   (age)       │
└────────────┘                                     └──────┬───────┘
       ▲                                                   │
       │                                                   ▼
       └─────── Processo ou equipamento ←──────────────────┘
```

O ciclo: **o sensor lê** uma grandeza do processo (temperatura, pressão, velocidade); **o controlador compara** com o valor desejado (setpoint); **o controlador decide**; **o atuador age** (abre válvula, acelera motor, desliga); o **processo muda**; **o sensor lê novamente**.

Isso é **controle em malha fechada (closed loop)**. Existe também **malha aberta**, mais simples, em que não há retorno — mas em automação industrial séria, **malha fechada** é o padrão.

### Sensores: tipos mais usados na indústria

![Sensores industriais (termopar, transdutor de pressão, encoder) — exemplos típicos de chão de fábrica](https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Thermocouple0002.jpg/640px-Thermocouple0002.jpg)

Sensores são **traduzem** grandezas físicas em **sinais elétricos**. Tipos comuns:

| Tipo | O que mede | Tecnologia típica | Aplicação industrial |
| --- | --- | --- | --- |
| **Temperatura** | Calor | Termopar, PT100, infravermelho | Fornos, motores, refrigeração |
| **Pressão** | Força/área | Transdutor piezoelétrico | Compressores, tubulações, hidráulica |
| **Vazão** | Volume/tempo | Eletromagnético, ultrassônico, Coriolis | Líquidos, gases, fluidos industriais |
| **Nível** | Altura de líquido/sólido | Capacitivo, ultrassônico, radar | Silos, tanques, caldeiras |
| **Posição** | Distância / ângulo | Encoder, LVDT | Robôs, esteiras, máquinas-ferramenta |
| **Velocidade** | Movimento | Encoder, tacômetro | Motores, eixos rotativos |
| **Vibração** | Oscilação mecânica | Acelerômetro piezoelétrico | Manutenção preditiva |
| **Proximidade** | Presença de objeto | Indutivo, capacitivo, óptico | Detecção em esteiras |
| **Visão** | Imagem | Câmera + software | Inspeção, contagem, segurança |

Cada sensor tem **especificações técnicas**: faixa de medição, precisão, repetibilidade, tempo de resposta, faixa de temperatura de operação, grau de proteção (IP67, IP68 — resistência a poeira/água).

### Sinais analógicos vs digitais

Sensores enviam sinais de duas formas:

- **Analógico** — valor contínuo, normalmente representado por **corrente (4-20 mA)** ou **tensão (0-10 V)**. Ex.: temperatura varia entre 4 mA (mínimo da faixa) e 20 mA (máximo).
- **Digital** — valor discreto, ligado/desligado (on/off). Ex.: sensor de proximidade — peça presente ou ausente.

O padrão industrial **4-20 mA** é mais robusto que 0-10 V porque tolera melhor interferência elétrica e indica claramente quando o sensor está com defeito (0 mA = problema).

### Atuadores: tipos mais usados na indústria

Atuadores **convertem sinal elétrico em ação física**. Tipos comuns:

| Tipo | Função | Exemplos industriais |
| --- | --- | --- |
| **Motor elétrico** | Movimento rotativo | Esteiras, ventiladores, bombas |
| **Servo-motor** | Movimento rotativo de precisão | Robôs, máquinas CNC |
| **Cilindro pneumático** | Movimento linear (ar comprimido) | Prensas, fixação, abertura/fechamento |
| **Cilindro hidráulico** | Movimento linear de alta força | Prensas pesadas, elevadores |
| **Válvula solenoide** | Abre/fecha fluxo de fluido | Tubulações, dosadores |
| **Inversor de frequência** | Controla velocidade de motor | Praticamente qualquer motor moderno |
| **Aquecedor / resistência** | Aquece processo | Fornos, caldeiras |
| **Relé** | Liga/desliga circuito elétrico | Controle de cargas elétricas |

Cada atuador também tem suas especificações: potência, torque, velocidade, precisão, vida útil.

### Controladores: o "cérebro" da automação

Entre o sensor e o atuador entra o **controlador** — que **decide** o que fazer. Quatro tipos comuns:

1. **CLP (Controlador Lógico Programável)** — o mais comum em fábricas. Veremos em detalhe na Aula 10.
2. **PID (Proportional-Integral-Derivative)** — controlador clássico para variáveis contínuas (temperatura, pressão). Pode ser hardware dedicado ou função dentro de um CLP.
3. **DCS (Distributed Control System)** — usado em indústrias de **processo contínuo** (química, petróleo, energia). Distribui inteligência por toda a planta.
4. **PAC (Programmable Automation Controller)** — híbrido entre CLP e PC industrial. Mais flexível.

Cada um tem nicho. Em manufatura discreta (autopeças, eletrônicos), **CLP domina**. Em processos contínuos (química, petróleo), **DCS**. Em controle fino de temperatura/pressão, **PID** (frequentemente embutido em CLP).

### Exemplo numérico: dimensionando um controle de temperatura

Cenário: forno industrial precisa manter temperatura entre **150 °C e 155 °C**.

- **Sensor:** termopar tipo K (faixa 0-1200 °C, precisão ±2 °C).
- **Sinal:** 4-20 mA (4 mA = 0 °C, 20 mA = 1200 °C).
- **Setpoint:** 152 °C.
- **Controlador:** PID embutido em CLP, lê 1× por segundo.
- **Atuador:** resistência elétrica controlada por SSR (Solid State Relay) com **modulação PWM**.

**Lógica:** se temperatura < 152 → liga resistência mais tempo no ciclo PWM. Se > 152 → liga menos. Histerese de ±1 °C para evitar oscilação.

Ajustar **PID** (constantes proporcional, integral, derivativa) é arte — exige conhecimento do processo. Mal ajustado: forno oscila ou demora muito para estabilizar.

### Grau de proteção IP

Sensores e atuadores industriais têm **grau de proteção IP** (Ingress Protection):

- **IP66** — protegido contra poeira e jatos de água.
- **IP67** — totalmente protegido contra poeira; imersão até 1 m por 30 min.
- **IP68** — imersão contínua em água.
- **IP69K** — resistente a jato de água quente sob alta pressão (lavagem industrial).

Para ambientes industriais agressivos (química, alimentos, mineração), IP67 ou superior é exigência.

### Atividade prática

Pense em **um equipamento** que você conhece (industrial ou doméstico — ar-condicionado, geladeira, máquina de lavar):

1. Que **sensores** ele tem? O que medem?
2. Que **atuadores**? O que fazem?
3. Onde está o **controlador**? Como decide?
4. É **malha fechada** ou aberta?

### Pontos-chave

- Automação industrial = **sensor → controlador → atuador** em ciclo fechado.
- **Sensores** traduzem grandezas físicas em sinais elétricos (analógico 4-20 mA ou digital on/off).
- **Atuadores** convertem sinal em ação física (motor, válvula, resistência).
- **Controladores** podem ser **CLP, PID, DCS ou PAC** — cada um para seu nicho.
- **Grau IP** é essencial para ambientes industriais agressivos.

### Para saber mais

- **Groover, M. P.** *Automação Industrial e Sistemas de Manufatura*. Pearson.
- **Vídeo (Senai, YouTube):** "Sensores e atuadores na indústria"
- **Site Festo (educativo):** https://www.festo.com/br/pt/
- **Portal Mecatrônica Atual:** https://www.mecatronicaatual.com.br/

---

## Aula 9 — Roteiro da Videoaula 9: "Sensor, atuador, controlador — o ABC da automação"

**Duração:** 9 a 11 minutos.

### 1. Abertura (0:00 – 0:40)

> "Toda automação industrial — desde a esteira do supermercado até a refinaria gigante — é feita do mesmo trio: sensor, controlador, atuador. Hoje a gente fixa esse ABC."

### 2. O ciclo de controle (0:40 – 3:00)

- Diagrama: sensor → controlador → atuador → processo → sensor.
- Malha fechada vs aberta.

### 3. Sensores e sinais (3:00 – 5:30)

- Tabela: temperatura, pressão, vazão, nível, posição, velocidade, vibração, visão.
- Analógico (4-20 mA, 0-10 V) vs digital (on/off).

### 4. Atuadores e controladores (5:30 – 8:30)

- Atuadores: motor, servo, cilindro, válvula, inversor.
- Controladores: CLP, PID, DCS, PAC.
- Exemplo: controle de forno a 152 °C.

### 5. Encerramento + gancho U10 (8:30 – 11:00)

> "Próxima aula: vamos abrir o **CLP** — o cérebro mais usado na fábrica brasileira — e entender a famosa **lógica ladder**. Te espero!"

---

## Aula 10 — CLP e lógica ladder

> **Pausa para reflexão:** se você fosse projetar um sistema que liga uma lâmpada quando alguém aperta um botão, mas só se outra chave está fechada, e desliga depois de 30 segundos — como descreveria essa regra? Pensa nisso enquanto avançamos.

O **CLP (Controlador Lógico Programável)** é o **cérebro mais comum** na automação industrial brasileira. Surgiu em 1969 (vimos na história da I4.0) e desde então domina o chão de fábrica. Esta aula abre o que ele é, como funciona, e introduz a famosa **lógica ladder** — a linguagem mais usada para programá-lo.

### O que é um CLP

> **CLP** (Controlador Lógico Programável) é um **computador industrial** dedicado a executar lógica de controle, tipicamente operando em ciclos contínuos de leitura de entradas, execução de programa e escrita de saídas.

Características distintivas:

- **Robusto** — projetado para ambiente industrial (vibração, temperatura, poeira).
- **Confiável** — operação 24/7, taxa de falha extremamente baixa.
- **Tempo real** — ciclo típico de execução em **milissegundos**.
- **Modular** — adicione módulos conforme necessidade (entradas, saídas, comunicação).
- **Programável em campo** — engenheiro reescreve lógica sem trocar hardware.

### O ciclo de varredura (scan cycle)

Todo CLP roda em um **ciclo contínuo**:

1. **Leitura de entradas** — captura estado de todos os sensores conectados.
2. **Execução do programa** — aplica a lógica programada (ladder ou outra linguagem).
3. **Escrita de saídas** — comanda os atuadores conforme decisão.
4. **Diagnóstico interno** — verifica saúde do CLP.
5. **Repete** — volta ao passo 1.

Tempo típico de ciclo: **5 a 50 milissegundos**, dependendo do tamanho do programa. Esse ciclo é a base da operação em tempo real.

### Anatomia de um CLP

![CLP modular com módulos de entrada/saída acoplados em trilho DIN — arquitetura típica de chão de fábrica](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/Siemens_Simatic_S7-400.jpg/640px-Siemens_Simatic_S7-400.jpg)

| Componente | Função |
| --- | --- |
| **CPU** | Processa a lógica (cérebro) |
| **Módulos de entrada** | Recebem sinais de sensores (digitais e analógicos) |
| **Módulos de saída** | Comandam atuadores |
| **Fonte de alimentação** | Energia (24 V típico) |
| **Módulos de comunicação** | Ethernet industrial, serial, Wi-Fi, fibra |
| **Interface de programação** | Geralmente Ethernet ou USB |

Em fábricas modernas, CLPs são programados por **software em PC** (Studio 5000 da Rockwell, TIA Portal da Siemens, GX Works da Mitsubishi, RSLogix). O programa é transferido para o CLP, que passa a executá-lo.

### As 5 linguagens da norma IEC 61131-3

A norma internacional **IEC 61131-3** define **5 linguagens** padronizadas para programar CLPs:

1. **Ladder Logic (LD)** — a clássica; diagramas estilo "escada" elétrica.
2. **Function Block Diagram (FBD)** — blocos conectados; visual.
3. **Structured Text (ST)** — textual, parecido com Pascal; para lógica mais complexa.
4. **Instruction List (IL)** — assembly-like; quase em desuso.
5. **Sequential Function Chart (SFC)** — diagramas de máquinas de estado; para processos sequenciais.

Você não precisa dominar todas. Mas precisa saber que existem. **Ladder ainda é a mais popular no Brasil** — porque imita esquemas elétricos que técnicos já conhecem.

### Lógica ladder: o que é

> **Ladder Logic** é uma linguagem gráfica que representa a lógica de controle como **diagramas elétricos** — com **trilhos verticais** (energia) e **degraus horizontais** (rungs) onde a lógica é montada.

Origem histórica: nos anos 1970-80, técnicos eletricistas precisavam migrar relés físicos para CLPs. A ladder foi criada para que eles **lessem o programa como leriam um esquema elétrico**.

### Elementos básicos da ladder

- **Contato normalmente aberto (NA)** — `─┤ ├─` — fecha (passa corrente) quando a variável está em 1.
- **Contato normalmente fechado (NF)** — `─┤/├─` — fecha (passa corrente) quando a variável está em 0.
- **Bobina (output)** — `─( )─` — ativa uma saída.
- **Bobina com retenção (latch/unlatch)** — mantém estado.
- **Temporizador (TON, TOF)** — conta tempo.
- **Contador (CTU, CTD)** — conta eventos.

### Exemplo de ladder

Vamos voltar à pergunta da reflexão: "ligar lâmpada quando botão for apertado, mas só se chave está fechada; desligar após 30 segundos".

```
   |                                                |
   |   B1        S1                  L_TEMPO      L|
   |─┤ ├──────┤ ├─────────────────┤/├─────────( )─|
   |                                                |
   |                                                |
   |   L                            T1              |
   |─┤ ├────────────────────────────[TON, 30s]─────|
   |                                                |
```

Leitura:

- Se **B1** (botão) e **S1** (chave) estão fechados, e o **L_TEMPO** (timer) ainda não estourou → **liga L** (lâmpada).
- Quando **L** acende, dispara o **T1** (timer de 30 s); quando estouram 30 s, **L_TEMPO** vai para 1 → contato `┤/├` abre → lâmpada apaga.

É a tradução em ladder daquela regra. Cada degrau ("rung") é uma condição lógica.

### Marcas dominantes de CLP

- **Rockwell Automation (Allen-Bradley)** — líder nos EUA, presença forte no Brasil.
- **Siemens (S7-1200, S7-1500)** — líder europeu e global.
- **Mitsubishi** — forte na Ásia.
- **Schneider Electric (Modicon)** — concorrente histórico.
- **Omron, Beckhoff, B&R** — competidores fortes em nichos.
- **Weg, Altus, HI Tecnologia** — marcas brasileiras.

A escolha depende de **integração com legados, suporte local e preço**.

### Exemplo numérico: economia em uma linha automatizada com CLP

Cenário: linha de enchimento manual de garrafas.

- **Antes (manual):** 2 operadores enchem 800 garrafas/hora. Custo: R\$ 3.500/mês × 2 = R\$ 7.000/mês.
- **Depois (automatizado com CLP):** linha enche 2.400 garrafas/hora; 1 supervisor para 3 linhas.
- **Investimento:** CLP + sensores + atuadores + integração = R\$ 220.000.
- **Economia mensal:** 1 operador eliminado = R\$ 3.500. Mas o ganho real está no **volume**: 3× a produção sem aumento de mão de obra.
- **Capacidade extra:** 1.600 garrafas/h × 8h = 12.800 garrafas/dia adicionais. A R\$ 0,80 de margem cada = **R\$ 10.240/dia**.
- **Payback:** se for vendido tudo, menos de 1 mês. Em cenários realistas (com gradual), 3-6 meses.

### Atividade prática

Desenhe (em ladder ou descreva em linguagem clara) a lógica para:

> Uma esteira deve ligar quando:
> - O botão "Iniciar" foi pressionado **E**
> - A porta de segurança está fechada **E**
> - Não há produto na próxima estação (sensor de presença = 0).
>
> A esteira deve desligar imediatamente se:
> - Botão "Parar" for pressionado **OU**
> - Porta abrir **OU**
> - Sensor de presença detectar produto.

### Pontos-chave

- **CLP** é o cérebro de automação industrial — robusto, confiável, em tempo real.
- Roda em **ciclo de varredura**: leitura de entradas → execução → escrita de saídas → repete.
- **Norma IEC 61131-3** define 5 linguagens; **Ladder** é a mais popular no Brasil.
- Ladder usa **contatos, bobinas, temporizadores e contadores** como elementos básicos.
- Marcas dominantes: **Rockwell, Siemens, Mitsubishi, Schneider** — e nacionais (WEG, Altus).

### Para saber mais

- **Petruzella, F. D.** *Controladores Lógicos Programáveis*. AMGH.
- **Vídeo (Mundo da Elétrica, YouTube):** "Ladder do zero — primeiros passos"
- **Norma IEC 61131-3:** disponível em https://webstore.iec.ch/
- **Studio 5000 da Rockwell (versão de avaliação):** https://www.rockwellautomation.com/

---

## Aula 10 — Roteiro da Videoaula 10: "CLP e lógica ladder — o cérebro do chão de fábrica"

**Duração:** 9 a 11 minutos.

### 1. Abertura (0:00 – 0:40)

> "Se você entrar em qualquer fábrica brasileira de médio porte para cima, vai esbarrar com CLPs. Eles são o cérebro mais comum do chão de fábrica. Hoje a gente abre o que é, como funciona e introduz a famosa lógica ladder."

### 2. O CLP e o ciclo de varredura (0:40 – 3:30)

- Definição e características.
- Ciclo: leitura → execução → escrita → diagnóstico → repete.
- Anatomia: CPU + módulos de I/O + comunicação.

### 3. Linguagens IEC 61131-3 (3:30 – 5:00)

- Listar as 5.
- Ladder é a mais popular no Brasil — origem histórica.

### 4. Ladder na prática (5:00 – 8:00)

- Elementos: contatos NA/NF, bobina, timer, contador.
- Exemplo: botão + chave + timer (lâmpada por 30 s).
- Marcas dominantes: Rockwell, Siemens, Mitsubishi.

### 5. Encerramento + gancho U11 (8:00 – 11:00)

> "Próxima aula: como o **SCADA** supervisiona tudo isso em escala — telas, alarmes, históricos. Te espero!"

---

## Aula 11 — SCADA e supervisão de processos

CLPs controlam o equipamento individual. Mas como **supervisionar** uma fábrica inteira em tempo real? Como ver, em uma tela, o estado de **dezenas de máquinas e centenas de sensores**? É para isso que existe o **SCADA** — o sistema de **Supervisão, Controle e Aquisição de Dados**.

### A definição em uma frase

> **SCADA** (Supervisory Control And Data Acquisition) é o sistema que **supervisiona e controla** equipamentos industriais distribuídos, **adquire e armazena** dados em tempo real e **gera alarmes** quando algo sai do esperado.

SCADA está no **nível 2 da pirâmide ISA-95** (vimos na U2) — acima dos CLPs (nível 1), abaixo do MES (nível 3).

### O que um SCADA típico tem

1. **Telas de operação** (HMI — Human-Machine Interface) — desenhos animados da planta com valores atualizados em tempo real.
2. **Coleta de dados** dos CLPs e sensores, via protocolos industriais (Modbus, OPC, EtherNet/IP).
3. **Histórico** (data historian) — armazena leituras com timestamp, para análise posterior.
4. **Alarmes** — alerta operador quando variável sai da faixa aceitável.
5. **Gráficos de tendência** — visualiza variável ao longo do tempo.
6. **Receitas** — armazena parâmetros para diferentes produtos/operações.
7. **Relatórios** — exporta dados para análise.
8. **Controle limitado** — operador pode comandar partidas, paradas, ajustes via SCADA.

### HMI: a tela que o operador vê

![Sala de controle industrial com múltiplas telas SCADA exibindo telemetria em tempo real](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/Telemetry_room_control_centre.jpg/640px-Telemetry_room_control_centre.jpg)

A **HMI (Human-Machine Interface)** é a parte visual do SCADA. Telas típicas:

- **Visão geral** — mapa da planta com indicadores resumidos.
- **Detalhe por equipamento** — tela específica de uma máquina com todos os parâmetros.
- **Alarmes ativos** — lista de problemas em andamento.
- **Tendências** — gráficos de variáveis ao longo do tempo.
- **Histórico de eventos** — log de tudo que aconteceu.
- **Relatórios** — turnos, lotes, produção.

Boa HMI tem **3 princípios**:

1. **Foco no operador** — não no engenheiro que projetou. Operador precisa identificar problemas em **segundos**.
2. **Hierarquia visual** — informação crítica em destaque; ruído visual minimizado.
3. **Padronização** — todos os equipamentos similares têm tela similar.

A norma **ISA-101** define boas práticas de design de HMI.

### Protocolos industriais

SCADA precisa "falar" com vários equipamentos de marcas diferentes. Os protocolos clássicos:

- **Modbus** — clássico, simples, ainda dominante em equipamentos legados.
- **Profibus / Profinet** — Siemens. Profinet é Ethernet industrial.
- **EtherNet/IP** — Rockwell.
- **CC-Link** — Mitsubishi.
- **OPC UA** — padrão aberto, semanticamente rico, futuro do setor.
- **MQTT** — leve, usado em IIoT (vimos em I4.0).

Em fábricas modernas, **OPC UA** está virando o **lingua franca** — todo equipamento novo suporta. Em fábricas antigas, **Modbus** ainda é o padrão real.

### Alarmes: o coração operacional do SCADA

Alarme é o "grito de socorro" do sistema — algo saiu da faixa aceitável. A norma **ISA-18.2** define boas práticas:

1. **Cada alarme deve exigir ação** — alarme que ninguém faz nada vira ruído.
2. **Prioridade clara** — vermelho (crítico), amarelo (alerta), azul (informativo).
3. **Não exagerar** — fábrica com **mais de 6-10 alarmes ativos por turno** sofre **alarm flood** (operador ignora todos).
4. **Reconhecimento e resolução** — operador acusa o alarme e registra o que fez.

Excesso de alarmes mal projetados foi causa de **acidentes industriais graves** (Texas City 2005, Bhopal 1984, entre outros). Por isso a engenharia de alarmes é levada muito a sério hoje.

### Players de mercado

- **Rockwell FactoryTalk** — top de linha, integrado com PLC Allen-Bradley.
- **Siemens WinCC** — top de linha, integrado com Siemens S7.
- **Wonderware (AVEVA)** — independente, multiplataforma.
- **Ignition (Inductive Automation)** — moderno, baseado em web, em ascensão.
- **Elipse Software (brasileira)** — Elipse E3, Elipse Power, líder nacional.
- **Indusoft (brasileiro)** — adquirido pela AVEVA.

### Exemplo numérico: redução de tempo de resposta com SCADA

Cenário: fábrica de cerâmica, 8 fornos em operação contínua.

**Sem SCADA centralizado:**

- Operador faz **ronda física** a cada 30 minutos.
- Detecta desvio em até **30 minutos** após acontecer.
- Em caso de queda de chama (problema crítico): perda de qualidade do lote queimado, custo médio de R\$ 8.000 por evento.
- Frequência: 4-6 eventos/mês.

**Com SCADA + HMI bem configurado:**

- Alarme instantâneo na tela quando temperatura sai da faixa.
- Detecção em **menos de 1 minuto**.
- Custo médio por evento: R\$ 2.000 (intervenção rápida, lote salvo).
- Frequência: 1-2 eventos/mês (causas mapeadas, prevenidas).

**Ganho:**

- Antes: 5 eventos × R\$ 8.000 = R\$ 40.000/mês.
- Depois: 1,5 eventos × R\$ 2.000 = R\$ 3.000/mês.
- Economia: **R\$ 37.000/mês = R\$ 444.000/ano**.

Investimento típico: SCADA + integração + treinamento = R\$ 300-500 mil. **Payback de ~12 meses.**

### Atividade prática

Imagine um SCADA para uma operação que você conhece:

1. Que **5 variáveis** seriam exibidas na tela principal?
2. Que **3 alarmes** críticos faria sentido configurar?
3. Que **histórico** mais ajudaria em análises posteriores?
4. Que **integrações** com outros sistemas (ERP, MES) seriam úteis?

### Pontos-chave

- **SCADA** supervisiona e controla equipamentos distribuídos em tempo real (nível 2 ISA-95).
- **HMI** é a parte visual — boas práticas definidas pela norma **ISA-101**.
- Protocolos comuns: **Modbus** (legado), **OPC UA** (padrão moderno), **Profinet, EtherNet/IP**.
- **Alarmes** devem exigir ação, ter prioridade clara e não causar **alarm flood** (norma ISA-18.2).
- Players: **Rockwell, Siemens, Wonderware, Ignition, Elipse** (brasileira).

### Para saber mais

- **Site Elipse Software:** https://www.elipse.com.br/
- **Norma ISA-101 (HMI Design):** https://www.isa.org/standards-and-publications/isa-standards/isa-isa-101
- **Vídeo (Senai, YouTube):** "SCADA — o que é e como funciona"
- **Webinar Inductive Automation (Ignition):** https://inductiveautomation.com/

---

## Aula 11 — Roteiro da Videoaula 11: "SCADA — os olhos da fábrica"

**Duração:** 9 a 11 minutos.

### 1. Abertura (0:00 – 0:30)

> "Se o CLP é o **cérebro** da máquina individual, o **SCADA** é o **olho** que vê a fábrica inteira em tempo real. Hoje a gente entende como ele funciona."

### 2. O que é SCADA (0:30 – 3:00)

- Definição e o lugar no ISA-95 (nível 2).
- O que compõe um SCADA: telas, dados, históricos, alarmes.

### 3. HMI e boas práticas (3:00 – 5:30)

- O que o operador vê.
- ISA-101 — design centrado no operador.
- Padronização.

### 4. Protocolos e alarmes (5:30 – 8:30)

- Modbus, OPC UA, Profinet, EtherNet/IP.
- Alarmes: ISA-18.2, não causar alarm flood.
- Caso da cerâmica: -R\$ 37 mil/mês com SCADA.

### 5. Encerramento + gancho U12 (8:30 – 11:00)

> "Última aula da unidade: vamos fechar a pirâmide ISA-95 e entender a integração TI ↔ OT — o desafio do século 21. Te espero!"

---

## Aula 12 — Pirâmide da automação (ISA-95): integração TI ↔ OT

Última aula da Unidade 3. Vamos juntar tudo o que vimos — sensores, atuadores, CLPs, SCADA, MES, ERP — em uma única visão: a **pirâmide ISA-95**. E depois, falar do desafio que **define** a competitividade industrial moderna: a **integração entre TI e OT**.

### A pirâmide ISA-95 completa

![Pirâmide hierárquica ISA-95 / modelo Purdue com 5 níveis — do equipamento físico ao ERP corporativo](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Functional_levels_of_a_Distributed_Control_System.svg/640px-Functional_levels_of_a_Distributed_Control_System.svg.png)

A **norma internacional ISA-95** (também chamada **IEC 62264**) define uma **pirâmide hierárquica** de 5 níveis (também usada como modelo Purdue, com sobreposição):

| Nível | Sistema | Função | Tempo típico de decisão |
| --- | --- | --- | --- |
| **4** | ERP / Negócio | Planejamento estratégico e financeiro | Dias a meses |
| **3** | MES / MOM | Execução da manufatura | Horas a turnos |
| **2** | SCADA / HMI | Supervisão de processo | Segundos a minutos |
| **1** | CLP / DCS / PID | Controle de equipamento | Milissegundos a segundos |
| **0** | Equipamento físico | Sensores, atuadores, máquinas | Tempo real (milissegundos) |

A leitura: quanto mais **baixo**, mais **rápida** a decisão e mais **físico** o sistema; quanto mais **alto**, mais **lenta** a decisão e mais **estratégico** o sistema. Cada nível **fornece dados** para o nível acima e **recebe comandos** do nível acima.

### O que é TI e o que é OT?

- **TI (Tecnologia da Informação)** — tudo do **nível 3 para cima**: MES, ERP, BI, CRM, e-mail, intranet. Foco em **dados e processos de negócio**.
- **OT (Tecnologia da Automação ou Operacional)** — do **nível 2 para baixo**: SCADA, CLPs, sensores, atuadores. Foco em **processos físicos** e **operação em tempo real**.

Tradicionalmente, **TI e OT são mundos separados** — equipes diferentes, fornecedores diferentes, prioridades diferentes:

| Aspecto | TI | OT |
| --- | --- | --- |
| Prioridade | Confidencialidade do dado | Disponibilidade do processo |
| Aceita atualizar agora? | Sim | Não — parada custa $$$ |
| Vida útil | 3-5 anos | 15-30 anos |
| Sistema operacional | Atualizado | Frequentemente antigo |
| Quem opera | TI corporativa | Operadores e engenheiros de manutenção |

Esse é o **mesmo dilema** que vimos em I4.0 ao falar de cibersegurança industrial. Repete aqui porque é a **dor central** da automação moderna.

### Por que TI ↔ OT precisam conversar agora

Até 2010, TI e OT podiam viver **separados** sem grande prejuízo. Hoje, **não dá mais**:

- **Decisões de negócio** dependem de dados do chão de fábrica em tempo real.
- **Otimização de operação** depende de algoritmos rodando em servidores TI.
- **Manutenção preditiva** combina dados de sensores (OT) com IA (TI).
- **Visão única do cliente** integra CRM (TI) com qualidade (MES, OT).

A **convergência TI ↔ OT** é o tema de TI industrial dos próximos 10 anos.

### Como fazer a integração na prática

Existem **três abordagens** mais comuns:

1. **Gateway de dados** — um servidor intermediário lê dos CLPs/SCADA e envia para sistemas TI via APIs.
2. **OPC UA puro** — equipamentos novos já falam OPC UA; sistemas TI consomem direto.
3. **Plataforma IIoT (Mindsphere, AWS IoT, ThingWorx)** — camada intermediária especializada que coleta de OT e expõe para TI.

A abordagem moderna é a **plataforma IIoT** — ela cuida da segurança, normalização, históricos e integração. Mas é caro e exige maturidade.

### Cibersegurança na integração TI ↔ OT

Quando OT se conecta ao TI, sofre os **mesmos riscos** do TI:

- Ransomware.
- Acesso indevido.
- Vazamento de dados.

A norma **IEC 62443** (vimos em I4.0) define como proteger. O modelo **Purdue** (alinhado ao ISA-95) organiza a defesa em **zonas** — cada nível protegido por firewall do nível adjacente.

**Cibersegurança industrial é hoje pré-requisito** — não diferencial.

### Exemplo numérico: ROI de integrar dados do chão de fábrica ao ERP

Fábrica com CLPs nos equipamentos, mas **sem integração** ao ERP.

**Antes:**

- Apontamento manual: operador anota produção em papel; supervisor digita no ERP no fim do turno.
- Tempo: 2 h/turno de digitação (3 turnos × 5 dias × 4 sem) = 120 h/mês.
- Erros de digitação: ~5%.
- Custo de erro: R\$ 30 mil/mês (decisões erradas, problemas fiscais, etc.).

**Depois (com gateway de integração):**

- Dado dos CLPs sobe automaticamente para o ERP.
- Tempo de digitação: ~5 h/mês (só exceções).
- Erros: <0,5%.
- Custo de erro: R\$ 3 mil/mês.

**Ganhos:**

- Mão de obra liberada: 115 h/mês × R\$ 50/h = R\$ 5.750/mês.
- Redução de erro: R\$ 27 mil/mês.
- **Total:** R\$ 32.750/mês = ~R\$ 393 mil/ano.

**Investimento:** gateway + integração + projeto = R\$ 250.000.

**Payback:** ~8 meses.

### Caso brasileiro: TI-OT na Ambev

A **Ambev** tem operações brasileiras totalmente integradas TI-OT. Cada cervejaria:

- Tem CLPs em todos os equipamentos.
- SCADA supervisiona em tempo real.
- MES coordena ordens de produção.
- Tudo conecta ao ERP corporativo.
- Dados sobem para um **data lake** central onde IA roda modelos de previsão e otimização.

Resultado: **decisões corporativas baseadas em dados reais** do chão de fábrica, em **tempo quase real**. É referência no setor de bebidas mundial.

### O que você verá na próxima unidade

Na **Unidade 4**, vamos coroar a disciplina com **IA aplicada à produção**. Você verá o que é IA, como funciona ML, IA aplicada à previsão de demanda e manutenção preditiva, visão computacional para qualidade, e por fim IA generativa na engenharia de produção — fechando seu repertório como engenheiro(a) preparado(a) para a indústria moderna.

### Atividade prática

Para a empresa que você analisou nas U1 e U2:

1. Em **qual nível** da pirâmide ISA-95 ela tem mais maturidade?
2. **Onde está a maior lacuna** (Ex.: tem ERP mas chão de fábrica desconectado)?
3. Que **uma integração** TI ↔ OT traria maior impacto rapidamente?
4. **Quais riscos** de cibersegurança você antecipa nessa integração?

### Pontos-chave

- **ISA-95** define 5 níveis: equipamento (0) → CLP (1) → SCADA (2) → MES (3) → ERP (4).
- **TI** (3 para cima) e **OT** (2 para baixo) têm filosofias diferentes mas precisam **convergir**.
- A convergência TI-OT é o **desafio central** da automação moderna.
- Cibersegurança industrial (IEC 62443) é **pré-requisito**, não diferencial.
- ROI de integração TI-OT é tipicamente rápido (6-12 meses) quando bem executado.

### Para saber mais

- **Norma ISA-95 / IEC 62264:** https://www.isa.org/standards-and-publications/isa-standards/isa-standards-committees/isa95
- **Site Ambev (sobre operações):** https://www.ambev.com.br/
- **Vídeo (Siemens, YouTube):** "IT-OT Convergence in Manufacturing"
- **Norma IEC 62443 (cibersegurança industrial):** https://webstore.iec.ch/

---

## Aula 12 — Roteiro da Videoaula 12: "Pirâmide ISA-95 — fechando o ciclo TI ↔ OT"

**Duração:** 9 a 11 minutos.

### 1. Abertura (0:00 – 0:30)

> "Você já viu sensor, CLP, SCADA, MES, ERP em aulas separadas. Hoje a gente junta tudo em uma única pirâmide — a ISA-95 — e fala do desafio que define a competitividade industrial moderna: a convergência TI ↔ OT."

### 2. A pirâmide ISA-95 completa (0:30 – 3:30)

- Tabela dos 5 níveis.
- Tempo de decisão por nível.

### 3. TI vs OT (3:30 – 6:00)

- Tabela comparativa.
- Por que se separaram historicamente.
- Por que precisam convergir agora.

### 4. Integração e cibersegurança (6:00 – 8:30)

- Gateway, OPC UA, plataforma IIoT.
- IEC 62443 e modelo Purdue.
- Caso Ambev como referência brasileira.

### 5. Encerramento + gancho U4 (8:30 – 11:00)

> "Última unidade: vamos coroar a disciplina com **IA aplicada à produção**. Previsão, manutenção preditiva, visão computacional, IA generativa. Te espero!"

---

## Quiz não avaliativo

### Questão 1

A respeito do **CLP (Controlador Lógico Programável)**, assinale a alternativa **correta**:

- [ ] a. CLP é um robô físico industrial com braço mecânico, projetado para soldar carrocerias.
- [ ] b. CLP só pode ser programado em linguagens textuais como Python ou Java; ladder não é uma linguagem real de CLP.
- [x] c. CLP é um computador industrial dedicado a executar lógica de controle em ciclos contínuos (leitura de entradas → execução → escrita de saídas), tipicamente programado em linguagens definidas pela norma IEC 61131-3 (entre elas, Ladder, Function Block, Structured Text).
- [ ] d. CLP nunca opera em tempo real e tem ciclos de execução que duram horas.

**Resposta correta:** `c`

**Feedback:** A (c) descreve corretamente o CLP. A (a) confunde CLP com robô industrial — são coisas distintas (CLP é cérebro de controle; robô é atuador físico). A (b) é falsa: a norma IEC 61131-3 padroniza 5 linguagens, sendo **Ladder** a mais usada. A (d) é o oposto: CLP opera em **tempo real**, com ciclos de milissegundos.

### Questão 2

Sobre a **convergência TI ↔ OT**, assinale a alternativa **correta**:

- [ ] a. TI e OT são exatamente o mesmo conceito e podem ser tratados como sinônimos.
- [ ] b. TI e OT devem permanecer completamente isoladas, sem qualquer integração, sob risco de comprometer a operação.
- [x] c. TI (sistemas de negócio, ERP, BI) e OT (automação, SCADA, CLPs) têm filosofias historicamente distintas — TI prioriza confidencialidade e atualizações frequentes; OT prioriza disponibilidade e tem equipamentos com vida útil longa — mas **precisam convergir** para habilitar decisões de negócio em tempo real, com cibersegurança industrial (IEC 62443) como pré-requisito.
- [ ] d. OT é uma versão atualizada do TI, com escopo idêntico, sendo TI considerada obsoleta.

**Resposta correta:** `c`

**Feedback:** A (c) descreve corretamente a relação TI ↔ OT. A (a) confunde os conceitos. A (b) é o erro histórico — funcionava antes de 2010, hoje compromete competitividade. A (d) é falsa: TI e OT são domínios complementares, não evolução um do outro.

---

## Atividade Verificadora (AAI — Atividade Avaliativa Individual)

**Pergunta:**

> Uma fábrica brasileira de médio porte (500 funcionários) tem **CLPs em todos os equipamentos críticos** e **ERP TOTVS Protheus implantado**, mas **não tem SCADA e o ERP é alimentado manualmente** com dados do chão de fábrica (apontamento em planilhas).
>
> A diretoria pede sua opinião sobre **como integrar TI e OT** com orçamento de R\$ 800 mil no próximo ano.
>
> Estruture sua resposta em três partes:
>
> 1. **Diagnóstico** — onde estão os principais gaps (em qual nível da pirâmide ISA-95)?
> 2. **Recomendação técnica** — o que implementar (SCADA, gateway, MES, plataforma IIoT)? Justifique tecnicamente.
> 3. **Plano em 12 meses** — etapas, prazo e KPIs.

**Resposta esperada:**

> Resposta de qualidade reconhece que o **gap principal** está no **nível 2 (SCADA)** e na **integração nível 2 ↔ nível 4 (ERP)**. Como o ERP é alimentado manualmente, a empresa **perde tempo, gera erros e atrasa decisões**. Recomendação típica: implantar **SCADA + gateway de integração** para automatizar o fluxo CLP → SCADA → ERP. Investimento aproximado: SCADA em 1-2 áreas-piloto (R\$ 250 mil), gateway de integração (R\$ 150 mil), implantação e treinamento (R\$ 300 mil), reserva para imprevistos (R\$ 100 mil) — dentro do orçamento de R\$ 800 mil. Plano em 12 meses: M1-3 SCADA piloto em 1 linha crítica; M3-6 ajuste e treinamento; M6-9 expansão para 2-3 linhas; M9-12 gateway ERP integrando dados automaticamente. KPIs: redução de tempo de digitação (alvo: -80%), redução de erros (alvo: -90%), velocidade de decisão (alvo: -50% no tempo entre evento e ação), cobertura de chão de fábrica (alvo: 80% dos equipamentos críticos sensoreados). Resposta deve mencionar **cibersegurança industrial** (IEC 62443) e **segmentação de rede** OT/TI. Resposta de qualidade também antecipa **resistência cultural** dos operadores e propõe gestão da mudança.

---

## Material complementar

### Direto da fonte — livro da Biblioteca Virtual

> A automação industrial vive sobre uma camada de **infraestrutura de TI** — hardware, redes e software que sustentam sensores, CLPs e SCADA. Esta unidade do livro detalha exatamente essa infraestrutura, dando o alicerce de TI que conecta o chão de fábrica (OT) ao mundo dos sistemas de informação (TI) — a ponte TI-OT que fechamos na Aula 12.

- **Nome do livro:** *Sistemas de Informação* (2ª edição)
- **Capítulo:** Unidade 2 — *Infraestrutura de Tecnologia da Informação (TI)* (p. 35)
- **Organizador:** Belmiro do Nascimento João
- **Editora:** Pearson
- **Link de acesso (BV):** https://plataforma.bvirtual.com.br/Acervo/Publicacao/183216
- **Aula em que entra:** Aulas 9 a 12

### Para mergulhar no assunto

> A série **"Marvels of Modern Manufacturing"** (Discovery / National Geographic) tem episódios curtos sobre fábricas modernas em operação, com CLPs e SCADA em ação. Disponível em trechos no YouTube.

- **Link(s):** https://www.youtube.com/results?search_query=marvels+modern+manufacturing
- **Aula em que entra:** Aula 11

### Podcast (curadoria, até 45 min)

> O podcast **"Automation World"** (em inglês, mas com tradução automática no YouTube) discute automação industrial em casos reais. O episódio recomendado discute SCADA e a transição para sistemas modernos.

- **Nome do podcast:** Automation World
- **Nome do episódio:** "SCADA Modernization"
- **Link:** https://www.youtube.com/@AutomationWorldVideo
- **Aula em que entra:** Aula 11

### Artigo científico

> Este artigo apresenta uma revisão sistemática sobre **convergência TI ↔ OT** em ambientes industriais, com foco em arquiteturas de referência e desafios de cibersegurança.

- **Link:** https://doi.org/10.1016/j.compind.2018.09.005
- **Aula em que entra:** Aula 12
- **Referência bibliográfica do artigo no formato ABNT:**
  > GIVEHCHI, Omid *et al*. **Interoperability for industrial cyber-physical systems: an approach for legacy systems**. *IEEE Transactions on Industrial Informatics*, v. 13, n. 6, p. 3370-3378, dez. 2017.
