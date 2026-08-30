# Plano de Aprendizagem Proposto

> **Status:** proposta do professor-conteudista, elaborada a partir da ementa oficial `MODEL_BASED_DESIGN_FOR_CYBER_PHYSICAL_SYSTEMS.docx` e das diretrizes de produção EAD do Núcleo das Engenharias e Tecnologia (`orientacoes_gravacao_EAD.pdf`). As diretrizes convidam explicitamente o professor a analisar criticamente a ementa e propor ajustes; as adaptações feitas estão listadas na seção "Adequações propostas à ementa oficial" e devem ser ratificadas pela coordenação.

## Identificação

- **Disciplina:** Model-Based Design for Cyber-Physical Systems
- **Núcleo:** Engenharias e Tecnologia
- **Modalidade:** EAD, com videoaulas gravadas por captura de tela e câmera
- **Professor-conteudista:** Afonso Cesar Lelis Brandão
- **Carga de videoaulas:** 16 videoaulas de 20 minutos, distribuídas em 4 unidades
- **Vídeo introdutório:** até 2 minutos, apresentação pessoal e conexão com o mercado
- **Idioma do material:** português do Brasil
- **Ano de referência do conteúdo:** 2026

## Ementa oficial (transcrição)

Metodologias de design baseado em modelos aplicadas ao desenvolvimento de sistemas ciberfísicos, integrando aspectos computacionais e físicos em um único framework de projeto. Aborda modelagem de plantas e controladores em domínio contínuo e discreto, co-simulação hardware-software, verificação formal e geração automática de código a partir de modelos. Explora ferramentas de modelagem e simulação de sistemas dinâmicos, com ênfase na rastreabilidade de requisitos e validação sistemática.

## Objetivo geral

Capacitar o estudante a projetar sistemas ciberfísicos com abordagem baseada em modelos, integrando modelagem matemática, simulação, verificação formal e geração automática de código, de modo a garantir correção e rastreabilidade desde os requisitos até o binário embarcado.

## Objetivos específicos

1. Modelar plantas físicas e controladores nos domínios contínuo e discreto, partindo de leis físicas e de dados de ensaio.
2. Desenvolver e simular sistemas de controle em malha aberta e fechada, quantificando desempenho por métricas objetivas.
3. Verificar propriedades formais de segurança e vivacidade e gerar casos de teste a partir de modelos.
4. Gerar código embarcado automaticamente a partir de modelos validados, preservando rastreabilidade.
5. Co-simular componentes de hardware e software em ambientes integrados, dimensionando o erro de acoplamento.
6. Produzir e sustentar evidências de correção compatíveis com os objetivos de normas de sistemas críticos.

## Adequações propostas à ementa oficial

A ementa sugere MATLAB/Simulink, Stateflow, OpenModelica, UPPAAL e o Simulink Support Package para Arduino. Esta proposta **mantém integralmente os conteúdos e as competências da ementa** e substitui a espinha dorsal ferramental por uma pilha aberta baseada em Python. As razões são técnicas e pedagógicas, não ideológicas:

1. **Acesso do estudante EAD.** A licença acadêmica de MATLAB/Simulink não acompanha o estudante depois da formatura e frequentemente não está instalada na máquina pessoal em que ele assiste à aula. Uma disciplina cujo laboratório o estudante não consegue reproduzir em casa contraria o requisito de "prática desde o início".
2. **Mercado 2026.** Python é hoje a linguagem dominante em engenharia de controle aplicada, ciência de dados de processo e prototipagem de sistemas embarcados, e a pilha `python-control` + `numpy`/`scipy` + `sympy` cobre exatamente o escopo da ementa. FMI/FMU é o padrão aberto de co-simulação efetivamente adotado pela indústria automotiva e aeroespacial, inclusive por quem usa Simulink.
3. **Ver o mecanismo, não só a ferramenta.** As diretrizes pedem que o estudante veja "código, ferramenta, processo, erro, correção e solução funcionando". Um verificador de modelos escrito em 150 linhas de Python, cujo espaço de estados o estudante enxerga sendo percorrido, ensina mais do que um botão que devolve "property satisfied".
4. **Rastreabilidade auditável.** Todo artefato desta disciplina é texto versionável em Git: modelo, propriedades, código gerado, testes e matriz de rastreabilidade. Isso é o que a ementa pede quando fala em "rastreabilidade de requisitos e validação sistemática".

**Correspondência ferramental proposta:**

| Ferramenta da ementa | Substituta aberta adotada | Cobertura |
| --- | --- | --- |
| MATLAB/Simulink (modelagem e simulação) | Python + `python-control` + `numpy`/`scipy` + `sympy` | Integral |
| Simulink (diagramas de blocos) | Álgebra de blocos programática em `python-control` (`series`, `parallel`, `feedback`) | Integral |
| Stateflow (máquinas de estado) | Máquina de estados explícita em Python + verificador de estados alcançáveis | Integral |
| OpenModelica | Mantida na ementa; o caminho canônico da disciplina é o FMU FMI 3.0 construído no próprio projeto | Integral |
| UPPAAL (autômatos temporizados) | Autômato temporizado de tempo discreto verificado exaustivamente em Python; UPPAAL apresentado como contraparte industrial | Integral |
| Simulink Coder (geração de código) | SymPy + Jinja2 → C, com bloco de rastreabilidade no cabeçalho | Integral |
| Simulink Support Package for Arduino | PlatformIO + ESP32, com back-end de *loopback* em C para quem não tem placa | Integral |
| — (não previsto na ementa) | NuSMV para *model checking* LTL/CTL industrial | Acréscimo |

Nenhum tópico da ementa foi removido. Os acréscimos são FMI 3.0, integração contínua e ponto fixo Q16.16, todos justificados pela exigência de conteúdo conectado ao mercado de 2026.

## Competências desenvolvidas

### Competência central (da ementa)

Projetar sistemas ciberfísicos com abordagem MBD, integrando modelagem matemática, simulação, verificação e geração de código, garantindo rastreabilidade de requisitos e correção desde a fase de projeto.

### Habilidades técnicas

1. Modelar sistemas dinâmicos em espaço de estados e em função de transferência, a partir de leis físicas e de dados experimentais.
2. Projetar controladores PID e por realimentação de estados, com critérios quantitativos de aceitação.
3. Discretizar controladores e escolher período de amostragem com base nas constantes de tempo da planta.
4. Especificar propriedades formais e verificá-las por *model checking*.
5. Gerar casos de teste a partir de modelos e medir cobertura de estados, transições e condições de guarda.
6. Gerar código embarcado a partir do modelo e demonstrar equivalência modelo-código.
7. Co-simular planta e controlador por FMI e dimensionar o erro de acoplamento.
8. Montar e manter uma matriz de rastreabilidade requisito → modelo → código → teste.

### Atitudes profissionais

- Rigor formal na modelagem e verificação de sistemas críticos.
- Disciplina na manutenção da rastreabilidade entre requisitos, modelos e código.
- Pensamento sistêmico para integrar subsistemas físicos e computacionais.
- Responsabilidade com segurança e confiabilidade em sistemas de tempo real.
- Ceticismo produtivo: nenhuma afirmação sobre o sistema vale sem evidência reproduzível.

## Conhecimentos prévios recomendados

Cálculo diferencial e integral, álgebra linear (matrizes e autovalores), circuitos elétricos básicos, física mecânica e programação em Python em nível intermediário. Equações diferenciais ordinárias e transformada de Laplace são retomadas na disciplina, no nível necessário, na Unidade 1.

## Fio condutor prático: o NexaBot

Toda a disciplina é atravessada por um único sistema ciberfísico: o **NexaBot**, um veículo autoguiado (AGV) de armazém industrial. O estudante o encontra na Aula 1 como um desenho e o entrega na Aula 16 como um sistema modelado, verificado, gerado, testado e rastreado.

**Descrição física.** Tração por motor de corrente contínua de ímã permanente de 24 V, acoplado a um redutor de relação 20:1 e a uma roda de 50 mm de raio.

**Parâmetros identificados (fonte única de verdade numérica da disciplina):**

| Parâmetro | Símbolo | Valor | Unidade |
| --- | --- | --- | --- |
| Resistência de armadura | $R$ | 1,2 | $\Omega$ |
| Indutância de armadura | $L$ | 3,5 | mH |
| Constante de torque | $K_t$ | 0,045 | $\mathrm{N\,m/A}$ |
| Constante de f.c.e.m. | $K_e$ | 0,045 | $\mathrm{V\,s/rad}$ |
| Inércia refletida | $J$ | $2{,}5 \times 10^{-4}$ | $\mathrm{kg\,m^2}$ |
| Atrito viscoso | $b$ | $8{,}0 \times 10^{-5}$ | $\mathrm{N\,m\,s/rad}$ |
| Relação de redução | $N$ | 20 | — |
| Raio da roda | $r$ | 0,05 | m |
| Tensão máxima | $V_{max}$ | 24 | V |
| Corrente máxima | $i_{max}$ | 12 | A |
| Período de amostragem | $T_s$ | 5 | ms |

**Grandezas derivadas verificadas em código:**

- Polos contínuos da planta: $-335{,}96$ e $-7{,}215$ (rad/s).
- Aproximações desacopladas: $L/R \approx 2{,}92\,\mathrm{ms}$ e $JR/(K_tK_e) \approx 148\,\mathrm{ms}$. No modelo acoplado, os polos fornecem $2{,}9765\,\mathrm{ms}$ e $138{,}598\,\mathrm{ms}$. A separação de cerca de 46,6 vezes e a constante dominante sustentam a análise de $T_s = 5\,\mathrm{ms}$.
- Ganho estático: $21{,}2164\ \mathrm{rad/(s\,V)}$.
- Velocidade de operação de $1{,}0\,\mathrm{m/s}$ corresponde a $400\ \mathrm{rad/s}$ no eixo do motor e exige $18{,}85\,\mathrm{V}$ em regime permanente — sobra de apenas $5{,}15\,\mathrm{V}$ para a ação transitória do controlador, o que torna a saturação do atuador um problema real e não uma hipótese acadêmica.
- Velocidade máxima em 24 V: $1{,}273\ \mathrm{m/s}$.
- A planta é controlável e observável (posto 2 nas matrizes de controlabilidade e observabilidade).

**Requisitos do NexaBot (formalizados ao longo da disciplina):**

| ID | Requisito |
| --- | --- |
| REQ-PLANT-001 | O modelo da planta deve reproduzir o ensaio de degrau com erro de ajuste inferior a 5%. |
| REQ-PLANT-002 | A tensão de comando não pode exceder 24 V nem a corrente exceder 12 A. |
| REQ-CTRL-001 | A velocidade deve rastrear a referência com erro em regime permanente nulo para degrau. |
| REQ-CTRL-002 | O comando deve respeitar a saturação do atuador sem perder estabilidade. |
| REQ-CTRL-003 | O integrador não pode acumular durante a saturação (*anti-windup*). |
| REQ-SAFE-001 | Nunca habilitar torque enquanto houver obstáculo detectado. |
| REQ-SAFE-002 | Emergência acionada implica freio acionado e torque desabilitado. |
| REQ-SAFE-003 | O estado de movimento deve ser alcançável a partir do repouso. |
| REQ-SAFE-004 | Do estado de falha só se sai por rearme explícito do operador. |
| REQ-SAFE-005 | Removido o obstáculo, com comando de partida, o sistema retoma o movimento. |
| REQ-SAFE-006 | Detectado o obstáculo, o torque deve ser zerado em no máximo 150 ms. |
| REQ-SAFE-007 | A velocidade linear não pode exceder 1,20 m/s. |

**Repositório do projeto:** `projeto_nexabot/`, com um subdiretório executável por aula (`aula_01/` a `aula_16/`) e o pacote `nexabot/` com o código de biblioteca.

## Pilha tecnológica adotada

| Camada | Ferramenta | Versão verificada |
| --- | --- | --- |
| Gerenciamento de ambiente | `uv` | 2026 |
| Linguagem | Python | 3.12 |
| Álgebra numérica | NumPy / SciPy | 2.5 / 1.18 |
| Controle | `python-control` | 0.10.2 |
| Álgebra simbólica | SymPy | 1.14 |
| Gráficos | Matplotlib | 3.11 |
| Co-simulação | FMI 3.0 + FMPy | — |
| Modelagem física | OpenModelica (Modelica) | — |
| Verificação formal | Verificador próprio em Python + NuSMV | — |
| Autômatos temporizados | Verificador próprio + UPPAAL | — |
| Testes baseados em modelos | pytest + Hypothesis + coverage | — |
| Geração de código | SymPy + Jinja2 → C (gcc) | — |
| Alvo embarcado | PlatformIO + ESP32 (e *loopback* em C) | — |
| Integração contínua | GitHub Actions | — |

---

# Organização das unidades

Cada unidade tem quatro videoaulas de 20 minutos. A primeira aula de cada unidade abre a unidade com "O que você verá nesta unidade"; a terceira traz uma "Pausa para reflexão" ou um desafio; a quarta faz a transição para a unidade seguinte, e a Aula 16 encerra a disciplina.

A régua sobe unidade a unidade: a Unidade 1 constrói o modelo, a Unidade 2 fecha a malha, a Unidade 3 prova que o comportamento é correto e a Unidade 4 transforma o modelo em binário embarcado com evidências.

## Unidade 1 — Fundamentos de sistemas ciberfísicos e modelagem da planta

### Resultado de aprendizagem da unidade

Ao final, o estudante modela uma planta física real em espaço de estados e em função de transferência, identifica seus parâmetros a partir de dados de ensaio, valida o modelo contra dados retidos e analisa estabilidade, controlabilidade e observabilidade — tudo com ferramentas abertas, em código versionado.

### Aula 1 — Sistemas ciberfísicos e o ciclo do design baseado em modelos

- **Prática de abertura (primeiros 4 minutos):** criar o ambiente com `uv`, instalar a pilha e rodar a primeira simulação do NexaBot.
- **Conceitos:** o que torna um sistema ciberfísico distinto de um software comum e de um sistema puramente físico; acoplamento entre dinâmica contínua e lógica discreta; por que o erro em CPS tem consequência física; o V-Model e a posição do MBD nele; o custo relativo de um defeito descoberto em cada fase.
- **Demonstração:** o NexaBot em malha aberta não sustenta a velocidade quando a carga muda — motivação concreta para toda a disciplina.
- **Exemplo numérico:** com 18,85 V fixos, o NexaBot atinge 1,00 m/s sem carga; sob torque de carga de 0,05 N·m, a velocidade cai e o erro aparece. A conta mostra que malha aberta não é opção.
- **Atividade prática:** mapear as 16 aulas no V-Model e registrar em que ramo cada uma atua.
- **Entregável da aula:** ambiente funcionando e a primeira figura de resposta ao degrau.

### Aula 2 — Da equação diferencial ao espaço de estados, com identificação por dados

- **Prática de abertura:** derivar simbolicamente as matrizes $A$, $B$, $C$, $D$ com SymPy, na tela.
- **Conceitos:** modelagem por leis de conservação; escolha de variáveis de estado; forma $\dot{x} = Ax + Bu$, $y = Cx + Du$; por que o estado é a memória mínima do sistema; identificação de parâmetros por mínimos quadrados; validação com dados retidos.
- **Demonstração:** ensaio de degrau com ruído de medição e quantização de encoder, ajuste dos parâmetros e comparação com os valores verdadeiros.
- **Exemplo numérico:** $A = \begin{bmatrix} -342{,}86 & -12{,}86 \\ 180{,}0 & -0{,}32 \end{bmatrix}$, $B = \begin{bmatrix} 285{,}71 \\ 0 \end{bmatrix}$; ganho estático $21{,}2164\ \mathrm{rad/(s\,V)}$ conferido contra o valor medido em regime.
- **Atividade prática:** identificar os parâmetros a partir de um segundo conjunto de dados e reportar o erro percentual de cada um.

### Aula 3 — Laplace, função de transferência e resposta em frequência

- **Prática de abertura:** aplicar a transformada de Laplace às duas equações do motor, no SymPy, e chegar a $G(s)$.
- **Conceitos:** transformada de Laplace como ferramenta de projeto; polos, zeros e constantes de tempo; separação de escalas de tempo; diagrama de Bode; margens de ganho e de fase; largura de banda.
- **Demonstração:** os dois polos do NexaBot e o que cada um significa fisicamente; a separação elétrica/mecânica de duas ordens de grandeza.
- **Exemplo numérico:** $G(s) = \dfrac{0{,}045}{8{,}75\times10^{-7}s^2 + 3{,}0028\times10^{-4}s + 2{,}121\times10^{-3}}$, polos em $-335{,}96$ e $-7{,}215\,\mathrm{rad/s}$, com constantes de tempo modais de $2{,}9765\,\mathrm{ms}$ e $138{,}598\,\mathrm{ms}$; comparação com as aproximações desacopladas $L/R=2{,}9167\,\mathrm{ms}$ e $JR/(K_tK_e)=148{,}148\,\mathrm{ms}$.
- **Pausa para reflexão:** se o polo elétrico é 46 vezes mais rápido que o mecânico, é legítimo desprezá-lo? O que se perde ao fazer isso?
- **Atividade prática:** obter as margens de ganho e fase, varrer $K_p$ e demonstrar por que esta malha contínua de segunda ordem permanece estável para todo $K_p>0$, preparando o contraste com a malha discreta da Aula 6.

### Aula 4 — Controlabilidade, observabilidade e realimentação de estados

- **Conceitos:** matrizes de controlabilidade e observabilidade; alocação de polos; regulador linear quadrático; observador de estados; o compromisso entre desempenho e esforço de controle.
- **Demonstração:** alocar polos rápidos e observar o comando exigido estourar os 24 V disponíveis — o limite físico invalidando um projeto matematicamente correto.
- **Exemplo numérico:** varredura de $Q$ e $R$ no LQR, tabulando pico de tensão exigida contra tempo de acomodação; a fronteira em que o projeto deixa de ser implementável.
- **Transição para a Unidade 2:** o estudante tem o modelo e um controlador em espaço de estados; falta fechar a malha com a estrutura industrialmente dominante, o PID, e levá-la para o domínio discreto em que o microcontrolador vive.

---

## Unidade 2 — Modelagem e simulação de sistemas de controle

### Resultado de aprendizagem da unidade

Ao final, o estudante projeta, sintoniza e discretiza um controlador para uma planta real, justifica numericamente o período de amostragem escolhido, trata saturação e *windup*, e acopla planta e controlador por co-simulação FMI medindo o erro de acoplamento.

### Aula 5 — Malha aberta, malha fechada e álgebra de diagramas de blocos

- **Prática de abertura:** montar a malha fechada em `python-control` e comparar com a redução simbólica feita no SymPy.
- **Conceitos:** realimentação negativa; função de transferência de malha fechada; funções de sensibilidade $S$ e complementar $T$ e a restrição $S + T = 1$; rejeição de distúrbio; erro em regime permanente por tipo de sistema.
- **Exemplo numérico:** degrau de torque de carga de 0,05 N·m — queda de velocidade em malha aberta contra erro residual em malha fechada.
- **Atividade prática:** demonstrar numericamente que $S + T = 1$ em várias frequências e interpretar o que isso impede.

### Aula 6 — PID na prática: sintonia, métricas e anti-windup

- **Conceitos:** ações proporcional, integral e derivativa; derivativo filtrado; sintonia de Ziegler-Nichols pelo ganho crítico; métricas de aceitação (sobressinal, tempo de subida, tempo de acomodação, ISE); saturação do atuador; *windup* do integrador e correção por *back-calculation*.
- **Demonstração obrigatória (ver o erro e a correção na tela):** referência de velocidade acima do que 24 V sustentam, integrador acumulando, resposta com sobressinal grosseiro; em seguida o anti-windup ligado e a mesma referência.
- **Exemplo numérico:** ganho crítico $K_u$ e período $T_u$ obtidos por varredura; tabela comparando Ziegler-Nichols clássico, variante sem sobressinal e ajuste manual pelas quatro métricas.
- **Pausa para reflexão:** por que a sintonia clássica de Ziegler-Nichols entrega sobressinal alto, e em que aplicação isso é inaceitável?

### Aula 7 — Discretização e escolha do período de amostragem

- **Conceitos:** Euler para frente e para trás, Tustin (bilinear) e equivalente de retenção de ordem zero; distorção de frequência; escolha de $T_s$ a partir das constantes de tempo; atraso computacional de um ciclo e seu custo em margem de fase; quantização de encoder e de PWM.
- **Demonstração:** varredura de $T_s$ de 0,5 ms a 100 ms mostrando a degradação progressiva e o ponto em que a malha fechada perde estabilidade.
- **Exemplo numérico:** com $\tau_m = 148\,\mathrm{ms}$, $T_s = 5\,\mathrm{ms}$ dá cerca de 30 amostras por constante de tempo mecânica; a conta que sustenta a escolha e o ponto em que ela deixa de valer.
- **Entregável:** o `DiscretePID` que será, na Unidade 4, o modelo de referência do código C gerado.

### Aula 8 — Co-simulação planta-controlador com FMI 3.0

- **Conceitos:** por que planta e controlador são simulados por integradores distintos; padrão FMI e o que é um FMU de co-simulação; passo de comunicação; erro de acoplamento e sua relação com o passo; interface `modelDescription.xml`.
- **Demonstração:** construir o FMU da planta do NexaBot, inspecioná-lo, acoplá-lo ao PID discreto em Python e variar o passo de comunicação.
- **Exemplo numérico:** varredura do passo de comunicação em 1, 5, 10, 20 e 50 ms, tabulando o erro contra a referência monolítica — o erro de acoplamento deixa de ser conceito e vira número.
- **Transição para a Unidade 3:** simular mostra o que o sistema faz em alguns cenários; a Unidade 3 responde ao que ele faz em **todos** os cenários.

---

## Unidade 3 — Verificação formal e testes baseados em modelos

### Resultado de aprendizagem da unidade

Ao final, o estudante formaliza requisitos de segurança em propriedades verificáveis, prova exaustivamente que o supervisor do NexaBot as satisfaz, lê e interpreta contraexemplos, verifica um requisito temporizado e gera automaticamente uma suíte de testes a partir do modelo, medindo cobertura.

### Aula 9 — Da especificação em texto à propriedade formal

- **Conceitos:** por que requisito em linguagem natural é ambíguo; invariantes, alcançabilidade, propriedades de segurança e de vivacidade; a diferença prática entre "algo ruim nunca acontece" e "algo bom acaba acontecendo"; rastreabilidade de requisitos.
- **Demonstração:** pegar um requisito real e mal escrito do NexaBot ("o robô deve parar rapidamente se houver obstáculo") e mostrar as três interpretações incompatíveis que ele admite, até chegar a REQ-SAFE-006 com prazo numérico.
- **Atividade prática:** formalizar dois requisitos adicionais e classificá-los por tipo.

### Aula 10 — Model checking: espaço de estados, LTL, CTL e contraexemplos

- **Conceitos:** modelo como sistema de transições; exploração exaustiva do espaço alcançável; explosão de estados; LTL e CTL; o que um contraexemplo é e por que ele é a saída mais valiosa da verificação.
- **Demonstração obrigatória (ver o erro e a correção na tela):** um bug é deliberadamente introduzido no supervisor; o verificador acusa a violação de REQ-SAFE-001 e devolve a sequência exata de entradas que leva à falha; o bug é corrigido e a verificação passa.
- **Exemplo numérico:** número de estados alcançáveis e de transições exploradas, e o tamanho do contraexemplo.
- **Pausa para reflexão:** um teste que passa mil vezes prova ausência de falha? O que exatamente o *model checking* acrescenta?

### Aula 11 — Autômatos temporizados e o requisito de prazo

- **Conceitos:** relógios em autômatos temporizados; invariantes de localização e guardas temporais; verificação de prazo de pior caso; por que o pior caso não aparece em simulação típica.
- **Demonstração:** o watchdog de parada de emergência do NexaBot, com atraso de detecção e um ciclo perdido, verificado exaustivamente contra o prazo de 150 ms.
- **Exemplo numérico:** varredura de atrasos identificando a combinação exata em que o prazo é violado.
- **Contraparte industrial:** UPPAAL, com o mesmo autômato.

### Aula 12 — Testes gerados a partir do modelo e cobertura

- **Conceitos:** teste baseado em modelo; critérios de cobertura de estados, de transições e de condições de guarda; teste baseado em propriedades; redução (*shrinking*) de contraexemplos; o que cobertura de linha não diz.
- **Demonstração:** gerar a suíte de testes por percurso do grafo do supervisor, executá-la, medir cobertura de transições e de linhas, e depois soltar o Hypothesis para procurar o que a suíte gerada não cobriu.
- **Transição para a Unidade 4:** o modelo está correto; falta transformá-lo em código embarcado sem perder essa correção no caminho.

---

## Unidade 4 — Geração de código, integração hardware-software e evidências

### Resultado de aprendizagem da unidade

Ao final, o estudante gera código C a partir do modelo validado, demonstra equivalência numérica entre modelo e código, executa o controlador em configuração SIL e HIL medindo jitter, monta a matriz de rastreabilidade requisito → modelo → código → teste e discute com propriedade o que um pipeline aberto pode e não pode sustentar diante da DO-178C e da ISO 26262.

### Aula 13 — Geração automática de código a partir do modelo

- **Conceitos:** por que gerar em vez de digitar; templates e mapeamento modelo-código; código gerado como artefato derivado, nunca editado à mão; representação em ponto flutuante contra ponto fixo Q16.16; bloco de rastreabilidade no cabeçalho do arquivo gerado.
- **Demonstração:** derivar a equação de diferenças do PID no SymPy e vê-la aparecer no C gerado.
- **Exemplo numérico:** erro de quantização introduzido pelo Q16.16 em relação à referência em `double`.
- **Desafio:** alterar um ganho no modelo, regerar e observar o que muda no C e no hash de rastreabilidade.

### Aula 14 — Software-in-the-loop e equivalência modelo-código

- **Conceitos:** SIL; equivalência numérica amostra a amostra; tolerância de aceitação; testes de regressão; integração contínua como guardiã da equivalência.
- **Demonstração:** compilar o C gerado, carregá-lo por `ctypes` e rodar as duas implementações lado a lado sobre a mesma sequência de entradas.
- **Exemplo numérico:** erro máximo absoluto entre modelo e código, esperado na ordem do épsilon de máquina para a variante em `double`.
- **Entregável:** um fluxo de CI que quebra se a equivalência se perder.

### Aula 15 — Hardware-in-the-loop, tempo real e jitter

- **Conceitos:** HIL; planta simulada em tempo real contra controlador no alvo; protocolo de comunicação; jitter e latência de laço; watchdog; o que muda quando o tempo deixa de ser uma variável do gráfico e passa a ser um prazo.
- **Demonstração:** o controlador C rodando como processo separado, trocando mensagens com a planta em Python, com medição de jitter; e o caminho para o ESP32 com PlatformIO.
- **Exemplo numérico:** distribuição do jitter medido e a fração do período de 5 ms que ele consome.

### Aula 16 — Rastreabilidade, certificação e fechamento

- **Conceitos:** objetivos de DO-178C e de ISO 26262; níveis de criticidade; qualificação de ferramenta e por que ela é a questão central ao usar ferramentas abertas; que evidências o pipeline da disciplina efetivamente produz e quais ele não produz; casos de uso automotivo, aeroespacial e de robótica industrial.
- **Demonstração:** gerar a matriz de rastreabilidade completa do NexaBot e percorrer uma linha inteira, de REQ-SAFE-006 até o teste que a sustenta.
- **Honestidade técnica exigida:** o pipeline produz evidências; ele não certifica. Certificação é processo, envolve independência de verificação e qualificação de ferramentas.
- **Fechamento da disciplina:** retomada do percurso e conexão com o trabalho PBL.

---

## Metodologia

Cada videoaula segue a mesma arquitetura de 20 minutos, alinhada às diretrizes do Núcleo:

1. **00:00–02:00 — Abertura com a ferramenta já aberta.** Nenhuma aula começa por definição; toda aula começa por algo acontecendo na tela.
2. **02:00–05:00 — Situação-problema.** Um comportamento indesejado do NexaBot que o conteúdo da aula resolve.
3. **05:00–13:00 — Desenvolvimento conceitual ancorado em código.** A teoria entra como explicação do que está sendo executado.
4. **13:00–17:00 — Demonstração prática guiada**, incluindo, sempre que possível, um erro real e sua correção.
5. **17:00–19:00 — Aplicação profissional.** Onde isso aparece na indústria automotiva, aeroespacial e de robótica.
6. **19:00–20:00 — Pontos-chave, desafio prático e transição.**

A gravação é feita por captura de tela e câmera, com terminal e editor em fonte ampliada. O laboratório da aula está sempre em `projeto_nexabot/aula_NN/`, com scripts numerados na ordem de execução.

## Estratégia de avaliação

- **Formativa:** quiz não avaliativo de duas questões por unidade, com devolutiva conceitual; desafio prático ao final de cada aula.
- **Questionários:** 40 questões por unidade — 20 de asserção-razão e 20 de interpretação, cinco alternativas cada, devolutiva para todas as alternativas.
- **Atividade Avaliativa Individual (AAI):** uma questão dissertativa na Unidade 1, com resposta esperada.
- **Avaliação final:** 10 questões dissertativas cobrindo as quatro unidades, com respostas esperadas e critérios de correção.
- **Trabalho PBL:** projeto integrador aplicado a um sistema ciberfísico novo, com parte teórica, parte prática e vídeo de apresentação.

## Bibliografia

### Básica (da ementa)

1. OGATA, Katsuhiko. *Engenharia de controle moderno*. 5. ed. São Paulo: Pearson, 2011.
2. NISE, Norman S. *Engenharia de sistemas de controle*. 6. ed. Rio de Janeiro: LTC, 2013.
3. TANENBAUM, Andrew S.; BOS, Herbert. *Sistemas operacionais modernos*. 4. ed. São Paulo: Pearson, 2016.

### Complementar (da ementa)

1. FRANKLIN, Gene F.; POWELL, J. David; EMAMI-NAEINI, Abbas. *Sistemas de controle para engenharia*. 6. ed. Porto Alegre: Bookman, 2013.
2. HALLIDAY, David; RESNICK, Robert; WALKER, Jearl. *Fundamentos de física*. 10. ed. Rio de Janeiro: LTC, 2016. v. 3.
3. NILSSON, James W.; RIEDEL, Susan A. *Circuitos elétricos*. 10. ed. São Paulo: Pearson, 2016.
4. SOMMERVILLE, Ian. *Engenharia de software*. 10. ed. São Paulo: Pearson, 2019.
5. PATTERSON, David A.; HENNESSY, John L. *Organização e projeto de computadores*. 6. ed. Rio de Janeiro: Elsevier, 2017.

### Complementar proposta pelo conteudista

1. LEE, Edward Ashford; SESHIA, Sanjit A. *Introduction to Embedded Systems: A Cyber-Physical Systems Approach*. 2. ed. Cambridge: MIT Press, 2017.
2. ÅSTRÖM, Karl Johan; MURRAY, Richard M. *Feedback Systems: An Introduction for Scientists and Engineers*. 2. ed. Princeton: Princeton University Press, 2021.
3. BAIER, Christel; KATOEN, Joost-Pieter. *Principles of Model Checking*. Cambridge: MIT Press, 2008.
4. MODELICA ASSOCIATION. *Functional Mock-up Interface Specification*, version 3.0, 2022.
