# Entrega de Trabalho (PBL) — Model-Based Design for Cyber-Physical Systems

> **Arquivo-mestre de produção.** A Parte A é a versão do estudante. A Parte B, ao final, é exclusiva do professor tutor e não pode ser incluída no arquivo distribuído aos estudantes. A exportação para distribuição deve encerrar o documento do estudante exatamente antes do cabeçalho `# Parte B`.

- **Disciplina:** Model-Based Design for Cyber-Physical Systems
- **Professor-conteudista:** Afonso Cesar Lelis Brandão

> O **caso** existe para que o estudante transfira o método de design baseado em modelos estudado no NexaBot — modelar, simular, verificar e gerar código com rastreabilidade — para um sistema ciberfísico diferente, demonstrando que aprendeu o método e não apenas reproduziu um exemplo memorizado.

---

# Parte A — Versão do estudante

## 1. Título

**Operação Linha Viva: o desafio do braço colaborativo AuroraArm**

---

## 2. Desafio

> **O quê?** A **Aurora Robótica**, fabricante fictícia de robôs industriais, está integrando o **AuroraArm**, um braço robótico colaborativo de seis graus de liberdade, à linha de montagem de uma fábrica de componentes eletrônicos, dividindo o espaço de trabalho com operadores humanos sem cerca de proteção física. A junta do cotovelo do AuroraArm precisa ser modelada, controlada, verificada formalmente e ter seu firmware gerado a partir do modelo, com rastreabilidade completa, antes de a célula de montagem ser liberada para operação colaborativa.
>
> **Quem?** A equipe de engenharia da Aurora Robótica hoje projeta controladores manualmente, sem modelo formal e sem verificação exaustiva de segurança. Você foi contratado(a) como **engenheiro(a) de design baseado em modelos** para entregar, para a junta do cotovelo, o pacote completo de modelagem, controle, verificação formal e geração de código que sustentará a auditoria de segurança da linha.
>
> **Quando?** Restam **60 dias** até a auditoria de segurança que libera a operação colaborativa sem cerca física. O pacote de evidências deve estar pronto e rastreável dentro desse prazo.
>
> **Onde?** A junta do cotovelo do AuroraArm é acionada por um **motor de corrente contínua de ímã permanente de 48 V**, acoplado a uma **transmissão harmônica de redução 100:1**. Os parâmetros identificados em bancada de ensaio são:
>
> | Parâmetro | Símbolo | Valor | Unidade |
> | --- | --- | --- | --- |
> | Resistência de armadura | $R$ | 0,8 | $\Omega$ |
> | Indutância de armadura | $L$ | 1,2 | mH |
> | Constante de torque | $K_t$ | 0,085 | $\mathrm{N\,m/A}$ |
> | Constante de f.c.e.m. | $K_e$ | 0,085 | $\mathrm{V\,s/rad}$ |
> | Inércia refletida no eixo do motor | $J$ | $4{,}2 \times 10^{-4}$ | $\mathrm{kg\,m^2}$ |
> | Atrito viscoso refletido | $b$ | $1{,}5 \times 10^{-4}$ | $\mathrm{N\,m\,s/rad}$ |
> | Relação de redução | $N$ | 100 | — |
> | Tensão máxima do barramento | $V_{max}$ | 48 | V |
> | Corrente máxima do driver | $i_{max}$ | 8 | A |
> | Período de amostragem alvo do laço de posição | $T_s$ | 2 | ms |
>
> O **ponto de operação crítico** do ciclo de pega-e-solta exige que o eixo do motor sustente uma velocidade angular de $450\ \mathrm{rad/s}$ enquanto a junta carrega um payload de 2 kg fixado a 0,35 m do eixo, produzindo um torque de carga refletido de $0{,}25\ \mathrm{N\,m}$.
>
> **Requisitos de desempenho exigidos pela engenharia de processo:**
>
> | ID | Requisito |
> | --- | --- |
> | REQ-CTRL-AA-001 | O erro de posição da junta em regime permanente deve ser nulo para referência em degrau. |
> | REQ-CTRL-AA-002 | O sobressinal da resposta de posição não pode exceder 8%. |
> | REQ-CTRL-AA-003 | O tempo de acomodação da resposta de posição não pode exceder 300 ms. |
> | REQ-CTRL-AA-004 | O comando de tensão não pode exceder 48 V nem a corrente exceder 8 A em nenhum instante. |
>
> **Requisitos de segurança colaborativa, formalizados a partir da norma ISO/TS 15066 para robôs colaborativos:**
>
> | ID | Requisito |
> | --- | --- |
> | REQ-SAFE-AA-001 | Detectada a mão do operador a menos de 500 mm do efetuador pelo escâner de segurança, o torque da junta deve ser zerado em no máximo 100 ms. |
> | REQ-SAFE-AA-002 | Uma vez zerado o torque por detecção de proximidade, o movimento não pode ser retomado automaticamente: exige rearme explícito do operador. |
> | REQ-SAFE-AA-003 | Removida a mão do campo de detecção e confirmado o rearme, o braço deve retomar a trajetória original. |
> | REQ-SAFE-AA-004 | A velocidade linear do efetuador dentro da zona colaborativa não pode exceder 250 mm/s. |
>
> **Restrição de hardware:** o firmware da junta deve rodar em um microcontrolador de 32 bits com unidade de ponto flutuante (por exemplo, um núcleo ARM Cortex-M4), com o laço de controle de posição executando a $T_s = 2\ \mathrm{ms}$ (500 Hz), orçamento de tempo de execução por ciclo inferior a $200\ \mathrm{\mu s}$ (para não competir com as demais tarefas de tempo real da célula robótica) e memória de programa limitada a 256 KB para o firmware da junta. O sensor de proximidade tem atraso de detecção de até 20 ms, e o sistema operacional de tempo real do controlador pode, em condições de carga, perder até um ciclo de 2 ms por *jitter*.
>
> **Por quê?** Um protótipo anterior de célula colaborativa da Aurora Robótica, sem modelo formal e sem verificação exaustiva do supervisor de segurança, sofreu um quase-acidente durante testes internos: o torque não foi zerado a tempo quando um operador aproximou a mão do efetuador, porque o firmware manual não tratava corretamente uma condição de borda entre os estados de movimento e de parada de segurança. O incidente não causou lesão, mas interrompeu a homologação da linha e expôs a ausência de qualquer evidência reprodutível de que os requisitos de segurança eram de fato satisfeitos pelo firmware embarcado.
>
> **Sua missão como engenheiro(a) de design baseado em modelos:** entregar, para a junta do cotovelo do AuroraArm, um pacote técnico completo e defensável que (1) modele a planta em espaço de estados a partir dos parâmetros físicos e do ponto de operação informados, com identificação e validação apropriadas; (2) projete e sintonize um controlador que atenda aos requisitos de desempenho, tratando explicitamente saturação de atuador e possível efeito *windup*; (3) formalize e verifique exaustivamente os requisitos de segurança e de vivacidade, produzindo evidência de que o prazo de 100 ms é cumprido mesmo sob os atrasos informados; e (4) gere automaticamente o código C do controlador a partir do modelo validado, demonstre equivalência numérica entre modelo e código, e monte a matriz de rastreabilidade completa de requisito a teste.

---

## 3. Fontes de pesquisa

O estudante deverá pesquisar como a indústria projeta, controla e certifica juntas de robôs colaborativos:

1. **Material da disciplina** — as 16 aulas, com ênfase na Unidade 1 (modelagem em espaço de estados, identificação, controlabilidade e observabilidade), Unidade 2 (PID, discretização, saturação e *anti-windup*, co-simulação), Unidade 3 (formalização de requisitos, *model checking*, autômatos temporizados, testes baseados em modelo) e Unidade 4 (geração de código, SIL/HIL, rastreabilidade e certificação).
2. INTERNATIONAL ORGANIZATION FOR STANDARDIZATION. *ISO/TS 15066: Robots and robotic devices — Collaborative robots*. Geneva: ISO, 2016 — norma técnica primária sobre limites de força, velocidade e separação em operação colaborativa.
3. SICILIANO, Bruno; SCIAVICCO, Lorenzo; VILLANI, Luigi; ORIOLO, Giuseppe. *Robotics: Modelling, Planning and Control*. London: Springer-Verlag, 2010 — referência primária de modelagem e controle de manipuladores.
4. INTERNATIONAL ELECTROTECHNICAL COMMISSION. *IEC 61508: Functional safety of electrical/electronic/programmable electronic safety-related systems*. Parts 1-7. Geneva: IEC, 2010 — norma técnica primária de segurança funcional aplicável ao supervisor da junta.
5. BAIER, Christel; KATOEN, Joost-Pieter. *Principles of Model Checking*. Cambridge: MIT Press, 2008 — fundamentação de verificação formal já usada na disciplina, aplicada aqui a um novo conjunto de propriedades.
6. MODELICA ASSOCIATION. *Functional Mock-up Interface Specification*, version 3.0, 2022 — caso o estudante opte por co-simular a junta e o controlador por FMI.
7. **Caso real selecionado pelo estudante** — relato técnico público, identificável e referenciado conforme a ABNT, de uma equipe de engenharia sobre a integração de um robô colaborativo real (por exemplo, de um fabricante como Universal Robots, ABB ou KUKA) a uma linha de produção. Não basta citar genericamente "documentação de fabricante".

As fontes 2, 3 e 4 constituem o conjunto mínimo de três fontes técnicas primárias exigidas além do material da disciplina. O estudante pode substituí-las por fontes primárias equivalentes, desde que justifique a escolha e apresente a referência completa.

**Aulas relacionadas:** todas as 16 servem de insumo. Em ordem de relevância: Aulas 1–4 (modelagem em espaço de estados, identificação e validação, função de transferência, controlabilidade e observabilidade), Aulas 5–8 (malha fechada, PID, saturação e *anti-windup*, discretização, co-simulação FMI), Aulas 9–12 (formalização de requisitos, *model checking*, autômatos temporizados, testes baseados em modelo), Aulas 13–16 (geração de código, SIL, HIL, rastreabilidade e certificação).

---

## 4. Componentes avaliativos, submissão e pontuação

A avaliação possui **três componentes obrigatórios**: parte teórica (25%), parte prática com repositório e memorial de cálculo (50%) e vídeo de apresentação (25%). Para a submissão, o estudante enviará **um PDF único** com as partes teórica e prática e o memorial como anexo, o **link do repositório** (Git) contendo o código do projeto, e **um link para o vídeo** ao final do PDF.

O objetivo é produzir, para a junta do cotovelo do AuroraArm, o mesmo tipo de pacote de evidências construído para o NexaBot ao longo da disciplina — modelo, controle, verificação formal e código rastreável — demonstrando que o método, e não apenas o exemplo do NexaBot, foi de fato aprendido.

### 1. Parte Teórica — (25% da nota)

Desenvolva um **relatório técnico em PDF** contendo:

- Modelagem física da junta a partir das leis de conservação (equação elétrica da armadura e equação mecânica do eixo), com justificativa da escolha das variáveis de estado.
- Análise da diferença entre os requisitos de desempenho (REQ-CTRL-AA-001 a 004) e os requisitos de segurança colaborativa (REQ-SAFE-AA-001 a 004), classificando cada requisito de segurança como propriedade de **segurança** ("algo ruim nunca acontece") ou de **vivacidade** ("algo bom eventualmente acontece"), com justificativa.
- Fundamentação teórica das escolhas de controle, verificação e geração de código, apoiada nos conceitos das 4 unidades e nas referências pesquisadas.

### 2. Parte Prática — (50% da nota)

Entregue um **repositório versionado em Git** contendo, no mínimo:

- **Modelo da planta**: derivação e implementação em código das matrizes de espaço de estados $A$, $B$, $C$, $D$ da junta, a partir dos parâmetros físicos fornecidos.
- **Controlador**: projeto e sintonia de um controlador (PID discreto ou realimentação de estados) que atenda aos requisitos de desempenho, com tratamento explícito de saturação e, se aplicável, mecanismo de *anti-windup*.
- **Propriedades formais verificadas**: formalização e verificação exaustiva de pelo menos um requisito de segurança com prazo (análogo a REQ-SAFE-AA-001) e de pelo menos um requisito de vivacidade (análogo a REQ-SAFE-AA-003), com documentação de pelo menos um contraexemplo obtido durante o desenvolvimento (de uma versão preliminar do modelo, corrigida em seguida) ou uma justificativa fundamentada de por que nenhum contraexemplo surgiu.
- **Suíte de testes**: testes gerados a partir do modelo (por percurso do grafo de estados do supervisor de segurança e/ou por propriedades), com relatório de cobertura de estados e de transições.
- **Código gerado**: código C do controlador gerado automaticamente a partir do modelo (não digitado à mão), com bloco de rastreabilidade no cabeçalho, e teste de equivalência numérica entre o modelo de referência e o código gerado (configuração *software-in-the-loop*).
- **Matriz de rastreabilidade**: tabela requisito → modelo → código → teste, cobrindo pelo menos os oito requisitos apresentados no desafio.

**Memorial de cálculo** — **anexo obrigatório do PDF**, com cada item apresentando fórmula, substituição dos dados do caso, premissas e resultado, demonstrado passo a passo. No mínimo:

- **(a) Modelo em espaço de estados e constantes de tempo.** Montar
  $
  \dot{x} = Ax + Bu, \qquad x = \begin{bmatrix} i \\ \omega \end{bmatrix},
  $
  com $A = \begin{bmatrix} -R/L & -K_e/L \\ K_t/J & -b/J \end{bmatrix}$ e $B = \begin{bmatrix} 1/L \\ 0 \end{bmatrix}$, substituindo os parâmetros da junta. Calcular os autovalores de $A$ e as constantes de tempo elétrica e mecânica associadas, discutindo a separação de escalas de tempo resultante. Verificar o posto das matrizes de controlabilidade e de observabilidade (adotando $C = \begin{bmatrix} 0 & 1 \end{bmatrix}$ para a saída de velocidade angular) e concluir sobre controlabilidade e observabilidade da junta.
- **(b) Ponto de operação crítico.** A partir do balanço em regime permanente
  $
  K_t\, i_{ss} = b\, \omega_{ss} + T_{\text{carga}}, \qquad V_{ss} = R\, i_{ss} + K_e\, \omega_{ss},
  $
  calcular a corrente e a tensão exigidas em regime para sustentar $\omega_{ss} = 450\ \mathrm{rad/s}$ sob $T_{\text{carga}} = 0{,}25\ \mathrm{N\,m}$, e a folga resultante entre $V_{ss}$ e os $48\ \mathrm{V}$ disponíveis. Discutir a implicação dessa folga para a escolha do controlador e a necessidade (ou não) de *anti-windup*.
- **(c) Escolha do período de amostragem.** A partir da constante de tempo mecânica calculada no item (a), justificar numericamente (número de amostras por constante de tempo mecânica) se $T_s = 2\ \mathrm{ms}$ é adequado, insuficiente ou desnecessariamente conservador para o laço de posição.
- **(d) Verificação do prazo de segurança.** Considerando o atraso de detecção do sensor (até 20 ms) e a possibilidade de perda de um ciclo de controle de 2 ms, verificar exaustivamente (por varredura de combinações de atraso ou por autômato temporizado) se o prazo de 100 ms de REQ-SAFE-AA-001 é cumprido em todas as combinações consideradas, ou identificar a combinação que o viola.
- **(e) Equivalência modelo-código.** Calcular o erro máximo absoluto entre a saída do modelo de referência e a saída do código C gerado, ao longo de uma sequência de teste, e compará-lo ao épsilon de máquina do tipo de dado utilizado, concluindo se o resultado indica equivalência aceitável ou evidência de defeito na geração.

A proposta poderá conter diagramas de blocos, gráficos de resposta temporal, diagramas do autômato de segurança e demais representações gráficas que auxiliem na comunicação da solução. **Rastreabilidade:** os resultados do memorial devem ser **citados e discutidos** no relatório técnico — não basta anexar a conta solta, e o código do repositório deve ser referenciado por caminho de arquivo no relatório.

### 3. Vídeo de apresentação — (25% da nota)

Grave um **vídeo de até 5 minutos**, simulando uma apresentação técnica para a auditoria de segurança que libera a operação colaborativa do AuroraArm. O vídeo deverá apresentar:

- Contextualização do problema (quase-acidente do protótipo anterior, ausência de evidência reprodutível de segurança).
- Explicação do modelo, do controlador e dos principais números do memorial (constantes de tempo, tensão exigida em regime, período de amostragem escolhido).
- Demonstração de como o requisito de prazo de 100 ms foi formalizado e verificado, incluindo o tratamento dos atrasos informados.
- Demonstração da equivalência entre modelo e código gerado, e apresentação da matriz de rastreabilidade.
- Encerramento com **honestidade técnica**: o que o pacote de evidências apresentado sustenta perante a auditoria de segurança da Aurora Robótica, e o que ainda exigiria processo formal de certificação (qualificação de ferramenta, independência de verificação) caso o AuroraArm fosse submetido à ISO 26262 ou a uma norma equivalente do setor.

O vídeo deverá ser publicado no **YouTube (modo não listado)** ou em outra plataforma de hospedagem, e o **link deverá ser inserido ao final do PDF**. Antes da submissão, verifique se o link está correto e acessível para a correção.

**Critérios qualitativos transversais:** **clareza** e organização do texto, das tabelas e dos diagramas; **profundidade técnica** (não generalidades sobre "usar controle PID" ou "verificar formalmente"); **realismo** dos números (constantes de tempo, tensão exigida, folga de atuação, prazos verificados); **coerência interna** (modelo → controle → verificação → código → rastreabilidade alinhados); **rastreabilidade** (os cálculos do memorial devem usar os dados e as premissas declaradas e ser citados no relatório e referenciados ao código do repositório); e **integração** dos conceitos das 4 unidades.

---

## Roteiro do estudante

### 1. Leia o desafio

Sua primeira tarefa é entender o desafio proposto. Leia o cenário do **AuroraArm** com atenção:

- **Quem** é a Aurora Robótica e qual é a situação atual (controlador manual, sem modelo formal, sem verificação exaustiva)?
- **Qual** é o incidente que motivou a exigência de evidências (quase-acidente por falha do supervisor de segurança)?
- **Quais** restrições foram colocadas (60 dias, hardware embarcado com orçamento de tempo e memória limitados, atrasos de sensor e de ciclo)?
- **Onde** estão os números que você vai precisar (parâmetros físicos da junta, ponto de operação crítico, requisitos de desempenho e de segurança com prazo)?

Tome **notas estruturadas** dos parâmetros físicos, do ponto de operação ($450\ \mathrm{rad/s}$ sob $0{,}25\ \mathrm{N\,m}$ de carga) e dos prazos de segurança (100 ms para zerar o torque, considerando 20 ms de atraso do sensor e possível perda de um ciclo de 2 ms). Esses números são sua **base de modelagem**. Separe dados fornecidos pelo caso de premissas que você precisar adotar (por exemplo, o critério de aceitação de equivalência SIL).

### 2. Pesquise

Antes de propor a solução, reúna referências e ancore suas escolhas técnicas:

- **Releia** as Unidades 1 a 4 — todas são insumo direto (modelagem e identificação, controle e discretização, verificação formal e testes, geração de código e rastreabilidade).
- **Aprofunde** os conceitos que vai aplicar: derivação de matrizes de espaço de estados a partir de leis físicas, cálculo de constantes de tempo e verificação de controlabilidade/observabilidade, sintonia de controlador com tratamento de saturação, formalização de propriedades de segurança e de vivacidade, verificação de prazo sob atraso, geração de código e verificação de equivalência SIL — todos demonstrados **passo a passo** no memorial de cálculo.
- **Consulte** a ISO/TS 15066 para os limites de velocidade e separação em operação colaborativa, e a IEC 61508 para os conceitos de segurança funcional aplicáveis ao supervisor da junta.
- **Pesquise** um **caso real** de integração de robô colaborativo a uma linha de produção, publicado por uma equipe de engenharia identificável, e traga ao menos uma comparação concreta com a solução que você propôs para o AuroraArm.

### 3. Entrega

Como orientação editorial desta atividade, estruture o **relatório técnico em PDF, com 12 a 18 páginas antes dos anexos**, assim:

1. **Capa e resumo executivo** (1 página) — 5 linhas com a recomendação central de modelagem e controle.
2. **Modelagem da junta e análise de controlabilidade/observabilidade** (2 a 3 páginas).
3. **Projeto e sintonia do controlador, com tratamento de saturação** (2 a 3 páginas).
4. **Formalização e verificação das propriedades de segurança e de vivacidade** (3 a 4 páginas), incluindo a verificação do prazo de 100 ms sob os atrasos informados.
5. **Geração de código, equivalência SIL e matriz de rastreabilidade** (3 a 4 páginas).
6. **Honestidade técnica: o que o pacote sustenta e o que exigiria certificação formal** (1 a 2 páginas).
7. **Referências** — fontes consultadas, ABNT.

Inclua no mesmo PDF, como anexo, o **memorial de cálculo** com os itens (a) a (e) descritos na seção anterior, cada um com fórmula, dados, premissas, substituição e resultado. Os resultados precisam aparecer e ser discutidos no corpo do relatório, e o repositório de código deve ser referenciado por caminho de arquivo.

Para o **vídeo de apresentação (até 5 minutos)**:

- Abra com **o problema** (quase-acidente do protótipo anterior) e a **recomendação central**.
- Mostre o modelo e os principais números do memorial (constantes de tempo, tensão exigida em regime, período de amostragem).
- Apresente a verificação do prazo de segurança e a matriz de rastreabilidade em alto nível.
- Feche com **honestidade técnica** sobre os limites do pacote de evidências apresentado.
- Publique no **YouTube (modo não listado)** e cole o **link ao final do PDF** — confira se está acessível.

**Dica final:** capriche na **defesa numérica**. Uma auditoria de segurança não aprova modelo bonito — aprova evidência **reproduzível e rastreável**. Cada decisão (constante de tempo considerada, folga de tensão aceita, prazo verificado, tolerância de equivalência SIL) deve estar ancorada em cálculo demonstrado ou em referência técnica, não em opinião — e o **memorial de cálculo**, somado ao repositório de código, é a sua prova de que a evidência foi de fato produzida, não alegada.

Esse projeto é seu **portfólio final** — o tipo de pacote de evidências que se apresenta a uma auditoria de segurança ou a um cliente para defender decisões de projeto de um sistema ciberfísico real. **Capriche**.

Boa entrega!

---

# Parte B — Versão exclusiva do professor tutor

> **NÃO DISTRIBUIR AOS ESTUDANTES.** Esta parte contém a solução esperada e a orientação de correção. Ao gerar a versão do estudante, encerrar o documento em "Boa entrega!". Ao gerar a versão do tutor, incluir as Partes A e B.

## Solução esperada e critérios de correção

**Modelo esperado.** Com os parâmetros da junta, as matrizes de espaço de estados são

$
A = \begin{bmatrix} -R/L & -K_e/L \\ K_t/J & -b/J \end{bmatrix}
  = \begin{bmatrix} -666{,}67 & -70{,}83 \\ 202{,}38 & -0{,}357 \end{bmatrix},
\qquad
B = \begin{bmatrix} 1/L \\ 0 \end{bmatrix} = \begin{bmatrix} 833{,}33 \\ 0 \end{bmatrix}.
$

Os autovalores de $A$ são aproximadamente $-644{,}40\ \mathrm{rad/s}$ e $-22{,}62\ \mathrm{rad/s}$, com constantes de tempo $\tau_e \approx 1{,}55\ \mathrm{ms}$ e $\tau_m \approx 44{,}2\ \mathrm{ms}$ — separação de aproximadamente 28 a 29 vezes entre as duas escalas de tempo, comparável em ordem de grandeza à separação observada no NexaBot. Pequenas variações no método de cálculo dos autovalores (por exemplo, uma aproximação desacoplada $\tau_e \approx L/R$, $\tau_m \approx JR/(K_tK_e+bR)$, que resulta em $\tau_e \approx 1{,}5\ \mathrm{ms}$ e $\tau_m \approx 45{,}75\ \mathrm{ms}$) são aceitáveis, desde que o raciocínio e a ordem de grandeza estejam corretos. Com $C = \begin{bmatrix} 0 & 1 \end{bmatrix}$, tanto a matriz de controlabilidade $[B\ AB]$ quanto a de observabilidade $[C; CA]$ têm posto 2 para esses parâmetros — a junta é controlável e observável.

**Ponto de operação esperado.** Do balanço em regime permanente:

$
i_{ss} = \frac{b\,\omega_{ss} + T_{\text{carga}}}{K_t}
       = \frac{1{,}5\times10^{-4}\times450 + 0{,}25}{0{,}085}
       = \frac{0{,}3175}{0{,}085}
       \approx 3{,}74\ \mathrm{A},
$

$
V_{ss} = R\,i_{ss} + K_e\,\omega_{ss} = 0{,}8\times3{,}74 + 0{,}085\times450 \approx 41{,}24\ \mathrm{V}.
$

A corrente exigida ($3{,}74\ \mathrm{A}$) fica bem dentro do limite de $8\ \mathrm{A}$, mas a tensão de regime ($41{,}24\ \mathrm{V}$) deixa apenas $6{,}76\ \mathrm{V}$ de folga frente aos $48\ \mathrm{V}$ do barramento — cerca de 14% do total. Uma resposta de alta qualidade reconhece que essa folga estreita torna real o risco de saturação durante o transitório de partida ou de resposta a um degrau de referência, justificando o tratamento de *anti-windup* mesmo sem que o enunciado peça explicitamente esse mecanismo.

**Período de amostragem esperado.** Com $\tau_m \approx 44$ a $45\ \mathrm{ms}$ e $T_s = 2\ \mathrm{ms}$, obtém-se de 22 a 23 amostras por constante de tempo mecânica — número compatível com a prática de 10 a 30 amostras por constante de tempo dominante discutida na disciplina, portanto adequado, sem ser desnecessariamente conservador.

**Verificação do prazo de segurança esperada.** O prazo de REQ-SAFE-AA-001 é de 100 ms. Considerando o atraso de detecção do sensor de até 20 ms e a perda de até um ciclo de controle de 2 ms, o tempo total no pior caso analisado ingenuamente seria da ordem de 20 ms (detecção) mais alguns ciclos de 2 ms até o supervisor reagir e zerar o torque — folga considerável frente a 100 ms nesse cenário informado. Uma resposta de alta qualidade não se limita a essa conta ingênua: verifica exaustivamente, por autômato temporizado ou por varredura de combinações de atraso, se existe alguma composição de atrasos (por exemplo, atraso de detecção próximo do limite superior combinado com múltiplos ciclos perdidos em sequência, se o enunciado do estudante permitir essa hipótese) que aproxime ou viole o prazo, e discute explicitamente o que a verificação exaustiva acrescenta em relação ao cálculo do pior caso aparente. Também é esperado que o estudante classifique corretamente REQ-SAFE-AA-001 como propriedade de **segurança** (torque nunca pode permanecer habilitado além do prazo) e REQ-SAFE-AA-003 como propriedade de **vivacidade** (o movimento eventualmente é retomado após rearme).

**Controlador esperado.** Um PID discreto (ou controlador por realimentação de estados com integrador) sintonizado para sobressinal inferior a 8% e tempo de acomodação inferior a 300 ms é uma solução defensável, desde que a sintonia seja justificada por métricas (não por tentativa às cegas) e que o tratamento de saturação (limitação do comando a $\pm 48\ \mathrm{V}$ e $\pm 8\ \mathrm{A}$) e, preferencialmente, *anti-windup* por *back-calculation* ou por limitação condicional do integrador estejam presentes e demonstrados por simulação.

**Geração de código e equivalência esperada.** O código C gerado deve reproduzir a equação de diferenças do controlador discreto, com bloco de rastreabilidade no cabeçalho. O erro máximo absoluto entre o modelo de referência (em `double`, se essa for a escolha) e o código gerado deve ser da ordem do épsilon de máquina (aproximadamente $2{,}2\times10^{-16}$ multiplicado por um fator pequeno decorrente do acúmulo de poucas operações por ciclo) para ser aceito como equivalente; um erro muitas ordens de grandeza maior deve ser tratado pelo estudante como evidência de defeito na geração ou na tradução da equação, não como ruído numérico esperado.

**Rastreabilidade esperada.** A matriz deve cobrir, no mínimo, os oito requisitos apresentados no desafio (REQ-CTRL-AA-001 a 004 e REQ-SAFE-AA-001 a 004), ligando cada um a um artefato do modelo, a uma linha ou função do código gerado e a um teste específico que o exercita.

**Honestidade técnica esperada.** O relatório e o vídeo devem reconhecer explicitamente que o pacote entregue produz **evidências** de que os requisitos foram formalizados, verificados e testados dentro do escopo do projeto — e não constitui, por si só, uma **certificação** do AuroraArm perante uma norma como a ISO 26262 ou equivalente. Uma resposta de alta qualidade menciona a necessidade de qualificação das ferramentas utilizadas (geração de código, verificador) e de independência de verificação (avaliação por equipe distinta da que desenvolveu o modelo) como lacunas remanescentes.

### Rubrica detalhada por componente

**Parte Teórica (25 pontos):**

- 8 pontos: modelagem física correta, com equações elétrica e mecânica corretamente derivadas e variáveis de estado justificadas.
- 9 pontos: classificação correta de cada requisito de segurança como propriedade de segurança ou de vivacidade, com justificativa.
- 8 pontos: fundamentação teórica coerente com os conceitos das 4 unidades e com as referências pesquisadas.

**Parte Prática (50 pontos):**

- 10 pontos: modelo em espaço de estados corretamente implementado em código, com cálculo de constantes de tempo e verificação de controlabilidade/observabilidade.
- 10 pontos: controlador sintonizado atendendo aos requisitos de desempenho, com tratamento de saturação e discussão de *anti-windup* coerente com a folga de tensão calculada.
- 12 pontos: propriedades de segurança e de vivacidade formalizadas e verificadas exaustivamente, com tratamento explícito do prazo sob atraso e, idealmente, um contraexemplo documentado.
- 10 pontos: código C gerado automaticamente, com verificação de equivalência SIL e conclusão correta sobre a magnitude do erro frente ao épsilon de máquina.
- 8 pontos: matriz de rastreabilidade completa e coerente, cobrindo os oito requisitos do desafio.

**Vídeo de apresentação (25 pontos):**

- 8 pontos: contextualização do problema e clareza da recomendação central.
- 9 pontos: explicação correta e específica dos números do memorial (constantes de tempo, tensão de regime, prazo verificado).
- 8 pontos: honestidade técnica explícita sobre os limites do pacote de evidências frente à certificação formal.

### Erros típicos a observar na correção

- Copiar os parâmetros numéricos do NexaBot em vez de usar os parâmetros do AuroraArm fornecidos no desafio.
- Calcular a tensão de regime sem considerar o torque de carga informado ($0{,}25\ \mathrm{N\,m}$), obtendo um valor de $V_{ss}$ artificialmente baixo e concluindo, de forma equivocada, que não há risco de saturação.
- Confundir o atraso de detecção do sensor (20 ms) com o período de amostragem do controlador (2 ms), ou somar os dois incorretamente ao verificar o prazo de 100 ms.
- Classificar um requisito de segurança com prazo como propriedade de vivacidade, ou vice-versa, sem perceber a diferença entre "nunca ultrapassar o prazo" e "eventualmente retomar o movimento".
- Apresentar código C "gerado" que na prática foi digitado manualmente, sem qualquer relação demonstrável com o modelo (ausência de bloco de rastreabilidade ou de processo de geração reproduzível).
- Afirmar que o pacote de evidências "certifica" o AuroraArm, sem reconhecer a diferença entre produzir evidências e certificar um sistema segundo uma norma formal.
