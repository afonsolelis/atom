# Roteiros das videoaulas 13 a 16 — Unidade 4 (20 minutos)

Disciplina: Model-Based Design for Cyber-Physical Systems
Professor-conteudista: Afonso Cesar Lelis Brandão
Unidade 4: Geração de código, integração hardware-software e evidências
Duração-alvo de cada videoaula: 20 minutos.
Narração prevista: 2.200 a 2.700 palavras faladas por videoaula, sem contar títulos, marcações de tempo, comandos, saídas de terminal e indicações de edição.
Ritmo de referência: 115 a 130 palavras por minuto, já considerando pausas e respiração.

Plano de tempo de referência, adaptável ao ritmo de cada aula (ver seção "Metodologia" de `PLANO_APRENDIZAGEM_PROPOSTO.md`):

- 00:00–02:00 — abertura com a ferramenta já aberta (terminal ou editor, nunca definição);
- 02:00–05:00 — situação-problema;
- 05:00–13:00 — desenvolvimento conceitual ancorado em código;
- 13:00–17:00 — demonstração prática guiada, com erro real e correção quando previsto;
- 17:00–19:00 — aplicação profissional;
- 19:00–20:00 — pontos-chave, desafio prático e transição.

Esta é uma disciplina de captura de tela, não uma disciplina expositiva de slides: cada roteiro alterna entre blocos de `Slide N` — um recurso visual ou conceitual produzido pela equipe de edição a partir da descrição dada — e blocos de `TELA: terminal` ou `TELA: editor`, sempre com o comando literal em cerca de código e a saída real observada logo em seguida. Nenhum número citado nestes quatro roteiros é hipotético: todos foram reproduzidos, antes da escrita deste arquivo, rodando os scripts de `projeto_nexabot/aula_13/` a `aula_16/` com o interpretador `.venv/bin/python`. Nenhuma aula desta unidade começa por definição — os dois primeiros minutos de cada roteiro já têm um terminal ou um editor ativo na tela.

Os quatro roteiros a seguir correspondem às Aulas 13 a 16 da Unidade 4, tendo o NexaBot como fio condutor prático, e a Aula 16 encerra a disciplina inteira. Cada roteiro é um texto de narração pronto para gravação, e não notas de aula: frases completas, sem oralidade informal, registro de exposição técnica direta, no tom de um profissional explicando a um colega mais novo.

---

## Roteiro da Videoaula 13 — "O código que ninguém digita"

**Vínculo com o plano de aprendizagem:** Unidade 4, Aula 13 — Geração automática de código a partir do modelo.

**Objetivo da videoaula:** ao final, o estudante deve ser capaz de explicar por que código embarcado gerado automaticamente elimina uma classe inteira de erro de transcrição, ler e interpretar o bloco de rastreabilidade gravado no cabeçalho de um arquivo `.c` gerado, calcular a ordem de grandeza do erro de quantização de um controlador em ponto fixo Q16.16 frente à referência em `double`, e justificar, com uma equação derivada simbolicamente, por que o gerador usa discretização de Euler para trás em vez de Tustin.

**Mapa de tempo e telas:** 00:00 editor `controllers.py` · 01:00 editor `generate.py` · 02:00 slide do pipeline de geração · 03:15 terminal com a derivação simbólica · 05:00 slide da equação de diferenças · 07:00 terminal com a verificação do contrato · 08:30 terminal gerando o C · 10:30 slide do bloco de rastreabilidade · 12:00 terminal com o determinismo do hash · 13:00 slide do ponto fixo Q16.16 · 13:45 terminal com o erro de quantização · 16:30 terminal com Euler contra Tustin · 17:45 slide da aplicação industrial · 19:00 pontos-chave e transição.

### Abertura contextualizada

**[00:00–01:00 · TELA: editor — nexabot/controllers.py]**

A tela mostra `nexabot/controllers.py`, aberto exatamente no método `step` da classe `DiscretePID` — o controlador PID discreto que sustenta esta disciplina desde a Aula 7. Observe o contrato documentado ali: `Kp`, `Ki`, `Kd`, `Ts`, `u_max`, `tau_f` e `Kaw` são os sete números que definem completamente o comportamento do controlador. Imagine agora uma situação comum em uma empresa de automação industrial. Um engenheiro júnior recebe a tarefa de portar este PID para C, para rodar em um microcontrolador de 32 bits. Ele abre este mesmo arquivo, lê os ganhos de referência do NexaBot — `Kp` igual a 2,0, `Ki` igual a 40,0, `Kd` igual a 0,02 — e começa a digitar o equivalente em C à mão, linha por linha, copiando cada número. Esse tipo de tarefa costuma parecer trivial demais para merecer um processo formal de revisão: é só transcrição, não é lógica nova, ninguém pede uma segunda pessoa para conferir dígito por dígito.

**[01:00–02:00 · TELA: editor — nexabot/codegen/generate.py]**

Distraído, ele digita `Ki` igual a 4,0 em vez de 40,0: falta um dígito. Nada nisso gera erro de compilação nem aviso de tipo — o compilador aceita o número silenciosamente. O defeito só aparece semanas depois, no banco de testes, quando o motor responde devagar demais, e ninguém associa o sintoma a uma transcrição malfeita. A tela muda agora para `nexabot/codegen/generate.py`, o módulo que elimina esse risco pela raiz: em vez de uma pessoa copiar números de um arquivo Python para um arquivo C, uma função, `generate_pid_controller`, lê a instância de `DiscretePID`, deriva as equações do controlador e escreve o `.c` sozinha. O tema desta aula é exatamente essa mudança estrutural: código C deixa de ser digitado e passa a ser gerado.

### Desenvolvimento conceitual

**[02:00–03:15 · Slide 1 — Do modelo ao C: o pipeline de geração]**

Este diagrama resume o caminho que os próximos minutos percorrem. Primeiro, a forma contínua do PID, já conhecida da Aula 6: `Kp` mais `Ki` sobre `s`, mais o termo derivativo filtrado. Segundo, uma derivação simbólica em SymPy, que converte essa forma contínua em duas equações de diferenças. Terceiro, a extração dos sete ganhos da instância do modelo. Quarto, a renderização desses ganhos e dessas equações em dois arquivos, `pid_controller.h` e `pid_controller.c`, por templates Jinja2. Em nenhum ponto deste pipeline uma pessoa escreve a fórmula do PID diretamente em C — e é exatamente essa ausência que esta aula comprova, passo a passo, no terminal.

**[03:15–05:00 · TELA: terminal — projeto_nexabot]**

No terminal, dentro de `projeto_nexabot`, executo:

```bash
.venv/bin/python aula_13/01_do_modelo_ao_c.py
```

A saída começa pela forma contínua do controlador, $C(s) = K_p + K_i/s + K_d s/(1+\tau_f s)$, a mesma equação da Aula 6. Em seguida aparece o mapeamento de discretização escolhido, Euler para trás: $s \to (1-z^{-1})/T_s$. O script isola o termo integral, $G_i(s) = K_i/s$, substitui o mapeamento e devolve os coeficientes do numerador e do denominador em $z^{-1}$ — e, a partir deles, a recorrência final: $I[k] = I[k-1] + K_i T_s\, e[k]$. Nenhuma dessas frações foi escrita à mão neste script: `difference_equation`, em `nexabot/codegen/derive.py`, é uma função genérica, que extrai coeficientes de qualquer função de transferência racional em $z^{-1}$ e monta a equação de diferenças causal correspondente. O mesmo procedimento se repete para o termo derivativo filtrado, $G_d(s) = K_d s/(1+\tau_f s)$, chegando a $D[k] = (K_d(e[k]-e[k-1]) + \tau_f D[k-1])/(\tau_f + T_s)$.

**[05:00–07:00 · Slide 2 — Da forma contínua à recorrência discreta]**

Este slide fixa visualmente a mesma cadeia que acabou de aparecer no terminal: a forma contínua no topo, a seta da substituição de Euler para trás no meio, e as duas recorrências na base, lado a lado. É a mesma cadeia da Aula 6, só que percorrida agora em sentido inverso: lá, a forma contínua vinha de um circuito elétrico; aqui, ela vira ponto de partida para chegar a um algoritmo que um microcontrolador consegue executar em microssegundos. Vale insistir em por que esta discretização, e não outra, foi escolhida para código embarcado. Euler para trás converte cada termo do PID em uma multiplicação e uma soma por amostra — sem pré-distorção de frequência, sem coeficiente extra. O termo integral precisa guardar apenas um estado, `I[k-1]`; o termo derivativo já guarda `D[k-1]` e `e[k-1]` por um motivo diferente, que é o filtro passa-baixas sobre a derivada, não a escolha de discretização em si. Em um microcontrolador com RAM contada em bytes, essa economia de estado não é detalhe estético: é orçamento de memória real.

**[07:00–08:30 · TELA: terminal — projeto_nexabot]**

O terminal continua rolando a mesma execução. A quinta seção do script confronta a recorrência derivada do termo derivativo com o contrato documentado em `DiscretePID.step`: calcula simbolicamente a diferença entre as duas expressões e imprime o resíduo.

```text
D[k] derivado - D[k] do contrato (docstring) = 0
OK: derivação simbólica == contrato de DiscretePID.step
```

Esse zero não é aproximação — é igualdade simbólica exata, verificada pelo próprio SymPy antes de qualquer C ser gerado. Se um dia alguém alterar `DiscretePID.step` sem atualizar a derivação em `derive.py`, ou vice-versa, este script para de imprimir `OK` e levanta uma exceção, interrompendo a execução antes que qualquer arquivo C seja escrito com uma fórmula divergente. É a primeira camada de segurança desta unidade: antes mesmo de existir um arquivo `.c`, já existe uma prova de que a matemática por trás dele bate com o contrato do modelo — a geração de código só prossegue depois dessa verificação passar.

**[08:30–10:30 · TELA: terminal — projeto_nexabot]**

```bash
.venv/bin/python aula_13/02_gera_codigo.py
```

O comando gera dois arquivos em `nexabot/codegen/generated/`: `pid_controller.h` e `pid_controller.c`. Logo abaixo, o hash SHA-256 dos sete parâmetros do modelo: `dc3b95c3d13a052d4dee683c2d5cd75bbc3c3996dede09f747dc8c076c32fa13`. Esse hash é uma função determinística de `Kp` igual a 2,0, `Ki` igual a 40,0, `Kd` igual a 0,02, `Ts` igual a 0,005, `u_max` igual a 24,0, `tau_f` igual a 0,01 e `Kaw` igual a 1,0 — os mesmos sete campos que abrem este arquivo. O script imprime então o conteúdo inteiro de `pid_controller.c` na tela. Role a página e mostre também o corpo da função `pid_step`, escrita em `double`: ela reproduz, linha a linha, o contrato de `DiscretePID.step` — cálculo do erro, acúmulo da integral, cálculo do termo derivativo filtrado pela mesma fórmula derivada há pouco, saturação e, se saturado, a correção de anti-windup. Nada aqui foi digitado de memória: cada linha corresponde a um termo já verificado simbolicamente no bloco anterior.

**[10:30–12:00 · Slide 3 — Anatomia do bloco de rastreabilidade]**

Volte ao topo do arquivo gerado e leia comigo, com calma, porque este é o ponto central desta aula. A primeira linha diz, em letras maiúsculas: `ARQUIVO GERADO AUTOMATICAMENTE — NÃO EDITAR MANUALMENTE`. Logo abaixo, a justificativa: qualquer edição manual se perde na próxima geração e quebra a cadeia de rastreabilidade requisito, modelo, código, teste. Seguem os campos: requisitos de origem — `REQ-CTRL-001`, `002`, `003`, mais `REQ-CODEGEN-001` e `002` —, o modelo de referência, `nexabot.controllers.DiscretePID`, o gerador que produziu o arquivo, os sete parâmetros por extenso, o mesmo hash SHA-256 que acabamos de ver no terminal, e a data de geração em UTC. Nas últimas linhas do bloco estão, literalmente, as duas equações derivadas simbolicamente há pouco: `I[k] = I[k-1] + Ki*Ts*e[k]` e `D[k] = (Kd*(e[k]-e[k-1]) + tau_f*D[k-1]) / (tau_f + Ts)`. A equação que apareceu no SymPy, no bloco anterior, é a mesma equação impressa em comentário dentro do C gerado — não uma equação parecida: a mesma.

**[12:00–13:00 · TELA: terminal — projeto_nexabot]**

O restante da saída de `02_gera_codigo.py` comprova uma propriedade que qualquer gerador de código correto precisa ter: determinismo. Gerar duas vezes seguidas com os mesmos sete ganhos produz exatamente o mesmo hash — a comparação aparece como `OK`. Em seguida, o script troca só `Kp` para 3,5, mantendo os outros seis parâmetros intactos, e gera de novo: o hash muda por inteiro, e a segunda comparação também aparece como `OK`. Essa é a prova prática de que o hash não é decorativo — é uma função criptográfica dos parâmetros, sensível a qualquer alteração, por menor que seja. Se, amanhã, alguém encontrar um `pid_controller.c` em produção e quiser saber com quais ganhos exatos ele foi gerado, basta comparar esse hash contra o histórico de gerações, sem precisar reler o arquivo inteiro linha a linha. Em uma auditoria de segurança, essa propriedade tem valor concreto: em vez de confiar na palavra de quem fez o deploy, um revisor externo recalcula o hash a partir dos ganhos declarados no repositório e confere se bate com o que está gravado no binário em campo.

### Demonstração ao vivo

**[13:00–13:45 · Slide 4 — Ponto flutuante contra ponto fixo Q16.16]**

Até aqui, tudo assumiu aritmética em `double`, a mesma do modelo Python. Mas boa parte dos microcontroladores de baixo custo usados em robótica industrial — inclusive variantes do ESP32 sem unidade de ponto flutuante — emulam `double` em software, a um custo de tempo que pode comprometer o período de amostragem de cinco milissegundos. A alternativa é representar cada número real como um inteiro de 32 bits, com 16 bits de parte inteira e 16 de fração: o formato Q16.16, com resolução $2^{-16} \approx 1{,}526\times10^{-5}$.

**[13:45–16:30 · TELA: terminal — projeto_nexabot]**

```bash
.venv/bin/python aula_13/03_ponto_fixo.py
```

O script roda uma sequência de 4.000 amostras — degraus de referência e uma medição ruidosa de encoder — pelo mesmo `pid_controller.c`, uma vez usando a variante `double`, outra usando a variante Q16.16, ambas compiladas pelo mesmo `gcc`, via `nexabot.sil.compare_model_vs_code`. Para a variante `double`, os três indicadores — erro máximo, erro médio e erro RMS — saem exatamente 0,000e+00 volt. Já a variante Q16.16 mostra erro máximo de 6,552e-02 volt, erro médio de 6,538e-03 volt e erro RMS de 1,600e-02 volt. A tabela de amostras espaçadas mostra o padrão com clareza: em regiões saturadas, onde a saída bate contra mais ou menos vinte e quatro volts, o erro fica em 0,000e+00, porque saturar em ponto fixo satura no mesmo limite inteiro. Mas na amostra 1.090, em regime linear, o modelo devolve menos 2,173380 volt, e a variante Q16.16 devolve menos 2,216629 volt — um erro de 4,325e-02 volt naquele instante específico. A resolução nominal de Q16.16 é 1,526e-05; o erro RMS medido, 1,600e-02, é cerca de 1.049 vezes maior que essa resolução nominal. Isso não é bug: é o efeito esperado de acumular arredondamento em quatro multiplicações e uma divisão por passo de controle, amostra após amostra, ao longo de 4.000 execuções. Frente ao fundo de escala de 24 volts do driver do motor, o erro máximo medido representa cerca de 0,27 por cento — pequeno, mas não nulo, e a decisão de aceitá-lo ou não depende da margem de estabilidade da malha fechada, não apenas do número isolado. Um detalhe vale nota: mesmo os ganhos que a Aula 13 já mostrou quantizarem sem erro sozinhos, como `Kp` e `Ki`, não impedem esse acúmulo, porque `Ts` e `tau_f`, que não são múltiplos exatos da resolução de Q16.16, entram juntos no denominador do termo derivativo a cada uma das quatro mil amostras.

**[16:30–17:45 · TELA: terminal — projeto_nexabot]**

Uma última execução, o desafio da aula:

```bash
.venv/bin/python aula_13/04_desafio.py
```

O script deriva o mesmo termo integral, $G_i(s) = K_i/s$, por dois mapeamentos diferentes. Por Euler para trás, o já conhecido `I[k] = I[k-1] + Ki.Ts.e[k]`, que a saída confirma não precisar de `e[k-1]`. Por Tustin, a transformação bilinear $s \to (2/T_s)(1-z^{-1})/(1+z^{-1})$, a mesma integral vira uma regra trapezoidal, e a saída confirma que sim, precisa de `e[k-1]` além de `I[k-1]`. A diferença parece pequena, mas tem consequência direta em memória: Tustin exigiria guardar uma variável adicional só para o termo integral, em um firmware onde cada `double` de estado a mais é orçamento de RAM gasto. Euler para trás evita essa variável extra. A escolha de discretização, portanto, não é um detalhe arbitrário de estilo — é uma decisão de engenharia registrada, com justificativa, em `nexabot/codegen/derive.py`.

### Aplicação profissional

**[17:45–19:00 · Slide 5 — Onde a geração de código aparece na indústria]**

Esse mesmo raciocínio — gerar em vez de digitar, com rastreabilidade embutida — sustenta ferramentas comerciais amplamente usadas em engenharia automotiva e aeroespacial, como geradores de código a partir de diagramas de blocos que produzem C rastreável para unidades de controle de motor. Na indústria automotiva, controladores de tração e de frenagem regenerativa são, com frequência, gerados automaticamente a partir de um modelo, sob processo ISO 26262 — tema da Aula 16. Na aeroespacial, sistemas de comando de voo seguem exigência equivalente sob DO-178C. Em robótica industrial, como o próprio NexaBot, controladores de motor embarcados em ESP32 ou em microcontroladores ARM Cortex-M de baixo custo se beneficiam da mesma disciplina, mesmo fora de um contexto formalmente certificado: o hash de rastreabilidade não exige processo de certificação para já entregar valor de engenharia. Equipes de manutenção de campo, em particular, ganham algo prático com isso: diante de um robô com comportamento estranho, a primeira pergunta deixa de ser "alguém mexeu no firmware?" e passa a ser "qual hash está gravado, e ele corresponde à última versão aprovada do modelo?" — uma pergunta que se responde em segundos, não em uma investigação de dias.

### Fechamento

**[19:00–20:00 · TELA: terminal — projeto_nexabot]**

Fica registrado o essencial desta aula. Código C gerado automaticamente elimina o erro de transcrição manual, porque remove a etapa em que uma pessoa copia um número de um lugar para outro. O arquivo gerado é um artefato derivado: qualquer correção acontece no modelo, nunca direto no `.c`. O bloco de rastreabilidade liga qualquer binário, em produção, de volta aos requisitos, à versão do modelo e a um hash determinístico dos sete parâmetros. As duas recorrências do PID discreto vêm de uma derivação simbólica verificada automaticamente contra o contrato do modelo. E o formato Q16.16 introduz um erro de quantização mensurável, da ordem de centésimos de volt para os ganhos do NexaBot — pequeno frente à referência em `double`, mas nunca zero.

Seu desafio prático: escolha um ganho do PID, altere-o em dez por cento, regenere o código, registre o novo hash e escreva três frases sobre o que mudou no `.c` além do valor do parâmetro.

Na próxima aula, a Aula 14, essa comparação entre `double` e Q16.16 vira um teste automatizado: o modelo Python e o C compilado rodam lado a lado, amostra a amostra, sobre seis mil amostras com saturação e anti-windup ativos, e a expectativa para a variante `double` deixa de ser apenas pequena e passa a ser exatamente zero.

### Indicações de edição e recursos visuais

- TELA: editor — abrir `controllers.py` já na função `step`, com os sete campos do construtor visíveis (00:00).
- Slide 1 — pipeline de geração em quatro caixas, surgindo em sequência conforme a narração (02:00).
- Slide 2 — equação de diferenças, com a substituição de Euler para trás destacada por uma seta (05:00).
- Terminal — ao rodar `02_gera_codigo.py`, ampliar a fonte no instante em que o bloco de rastreabilidade aparece, sem cortar a cena antes do fim do bloco (08:30–10:30).
- Slide 3 — bloco de rastreabilidade anotado, com uma seta para cada campo: requisitos, modelo, hash, data, advertência (10:30).
- Slide 4 — reta numérica Q16.16, com `tau_f` marcado entre dois pontos de grade e seta indicando o arredondamento (13:00).
- Terminal — na tabela de `03_ponto_fixo.py`, destacar visualmente a linha da amostra 1.090, onde o erro aparece fora da região saturada (13:45–16:30).
- Slide 5 — ícones esquemáticos de automotivo, aeroespacial e robótica industrial, sem logotipos de marca (17:45).

### Fontes e links de mídia

- LEE, Edward Ashford; SESHIA, Sanjit A. *Introduction to Embedded Systems: A Cyber-Physical Systems Approach*. 2. ed. Cambridge: MIT Press, 2017 — referência conceitual, sem reprodução de trecho externo.
- YATES, Randy. *Fixed-Point Arithmetic: An Introduction*. Digital Signal Labs, Technical Reference, 2013 — referência conceitual, sem reprodução de trecho externo.
- Nenhuma mídia de terceiros é incorporada; diagramas, retas numéricas e o pipeline de geração devem ser produzidos originalmente pela equipe de edição a partir deste roteiro e de `unidade_4.md` (Aula 13).

---

## Roteiro da Videoaula 14 — "O erro que precisa ser exatamente zero"

**Vínculo com o plano de aprendizagem:** Unidade 4, Aula 14 — Software-in-the-loop e equivalência modelo-código.

**Objetivo da videoaula:** ao final, o estudante deve ser capaz de explicar o mecanismo da ponte SIL via `ctypes`, executar e interpretar `compare_model_vs_code`, justificar por que o erro esperado na variante `double` é exatamente zero — não apenas pequeno — à luz da aritmética IEEE-754, relacionar esse erro ao épsilon de máquina, e reconhecer, a partir de um bug real injetado, a assinatura numérica de um defeito de tradução modelo-código.

**Mapa de tempo e telas:** 00:00 terminal com os arquivos gerados · 01:00 situação-problema · 02:00 slide "compilar, carregar, comparar" · 03:30 terminal com a ponte ctypes · 05:30 slide "por que zero exato" · 07:00 terminal com a equivalência central · 09:30 slide de duas ordens de grandeza · 11:00 terminal com a suíte de regressão · 13:00 terminal com o bug de anti-windup · 15:30 slide do pipeline de CI · 16:30 terminal validando o workflow · 18:00 slide da aplicação industrial · 19:00 pontos-chave e transição.

### Abertura contextualizada

**[00:00–01:00 · TELA: terminal — projeto_nexabot]**

No terminal, dentro de `projeto_nexabot`, listo o que a Aula 13 deixou pronto:

```bash
ls nexabot/codegen/generated/
```

A pasta contém `pid_controller.h` e `pid_controller.c`, o mesmo arquivo com o bloco de rastreabilidade e o hash `dc3b95c3d13a052d...fa13` que vimos na aula anterior. Um colega, olhando por cima do ombro, comenta que esse C é equivalente ao modelo Python, porque foi gerado a partir dele. A frase soa razoável — e é exatamente o tipo de afirmação que esta disciplina rejeita sem evidência.

**[01:00–02:00 · TELA: terminal — projeto_nexabot]**

Gerar a partir de um modelo reduz a chance de erro; não a elimina. O gerador pode ter um bug de lógica. O template Jinja2 pode renderizar um operador com o sinal trocado. A conversão para ponto fixo pode introduzir mais erro do que o previsto pela análise de quantização da Aula 13. Equivalente não é um adjetivo que se declara sobre um arquivo gerado — é uma medição feita, amostra a amostra, sobre a mesma sequência de entradas, entregue simultaneamente ao modelo e ao código.

Vale notar que a Aula 13 já ofereceu uma prova parcial: a verificação simbólica confirmou que as equações batem, e a checagem de determinismo confirmou que o hash muda com os parâmetros certos. Nenhuma dessas duas checagens, porém, executa o binário compilado sobre uma sequência real de entradas — e é exatamente essa lacuna que esta aula fecha. Esta aula transforma a alegação de equivalência em número — e, antes do fim, mostra também o que acontece quando esse número deixa de ser desprezível.

### Desenvolvimento conceitual

**[02:00–03:30 · Slide 1 — Software-in-the-loop: compilar, carregar, comparar]**

*Software-in-the-loop*, SIL, é o nome da técnica: compilar o código gerado para a arquitetura do computador de desenvolvimento — não para o microcontrolador final — e executá-lo, lado a lado com o modelo, dentro do mesmo processo Python. Em `nexabot/sil.py`, isso acontece em três passos. Primeiro, `gcc` compila `pid_controller.c` com as flags `-O2 -fPIC -shared`, produzindo uma biblioteca compartilhada, `libpid_sil.so` — otimizada, como em produção, não uma versão de depuração. Segundo, `ctypes` carrega essa biblioteca dentro do processo Python. Terceiro, uma classe, `SILController`, expõe exatamente a mesma interface pública de `DiscretePID`: um construtor com os sete ganhos e um método `.step(r, y)`.

**[03:30–05:30 · TELA: terminal — projeto_nexabot]**

```bash
.venv/bin/python aula_14/01_compila_sil.py
```

O script primeiro carrega os símbolos da biblioteca compilada na mão, sem a conveniência de `SILController`, para deixar visível o mecanismo: uma `ctypes.Structure` cujos dez campos, todos `double`, precisam bater exatamente com o layout de `pid_controller_t` no `.h` gerado — os sete ganhos e os três estados internos, integral, erro anterior e estado derivativo. Com `argtypes` e `restype` declarados explicitamente, uma chamada `ctypes` cru devolve, para três pares de referência e medição: para r igual a 3,0 e y igual a 0,0, u igual a 10,600000 volt; para r igual a 3,0 e y igual a 1,0, u igual a 6,333333 volt; para r igual a 3,0 e y igual a 2,5, u igual a 0,988889 volt. Em seguida, o mesmo script repete exatamente a mesma sequência usando `SILController`, a interface de produção, e os três valores saem idênticos, casa decimal por casa decimal. `SILController` não é uma abstração que esconde comportamento diferente: ela empacota exatamente esta mecânica de `ctypes`, sem adicionar nem remover nada.

**[05:30–07:00 · Slide 2 — Por que o erro esperado, em double, é exatamente zero]**

Antes de rodar a comparação sistemática, vale entender por que a expectativa teórica não é apenas erro pequeno — é erro exatamente zero. O modelo Python, via NumPy, e o código C gerado, compilado sem otimizações agressivas como `-ffast-math`, seguem a mesma aritmética IEEE-754 de dupla precisão, na mesma ordem de operações: a mesma soma antes da mesma multiplicação, a mesma divisão no mesmo ponto da fórmula. O template Jinja2 que gera `pid_step` reproduz literalmente a sequência de operações de `DiscretePID.step`, porque as duas vêm da mesma derivação simbólica da Aula 13. Quando duas implementações calculam exatamente a mesma sequência de operações de ponto flutuante, sobre os mesmos números, IEEE-754 garante o mesmo resultado, bit a bit. Não é coincidência nem sorte: é consequência direta de a tradução ter preservado a ordem das operações. Se o template somasse os três termos do PID em outra ordem, ou se o compilador reassociasse essas somas sob uma flag como `-ffast-math`, o resultado poderia divergir na última casa decimal, mesmo sem bug algum de lógica — motivo pelo qual a compilação desta disciplina evita deliberadamente esse tipo de otimização agressiva.

**[07:00–09:30 · TELA: terminal — projeto_nexabot]**

```bash
.venv/bin/python aula_14/02_equivalencia.py
```

A sequência de teste tem 6.000 amostras, a `Ts` igual a cinco milissegundos, trinta segundos de simulação, com referência em degraus variados, inclusive negativos e uma componente senoidal, e medição com ruído de encoder, deliberadamente desenhada para exercitar saturação e anti-windup, não só o regime linear. Os ganhos são os mesmos de sempre. A tabela que aparece na tela mostra, para a variante `double`, sobre as 6.000 amostras: erro máximo 0,000e+00 volt, erro médio 0,000e+00 volt, erro RMS 0,000e+00 volt. Não é um valor pequeno arredondado para zero na exibição — é zero exato, o mesmo zero que a variante em ponto flutuante do C reproduziu bit a bit em cada uma das seis mil chamadas. Já a variante Q16.16, comparada contra o mesmo modelo em `double`, mostra erro máximo de 5,484e-02 volt, erro médio de 2,504e-03 volt e erro RMS de 7,927e-03 volt, sobre exatamente a mesma sequência.

O script então imprime o épsilon de máquina do `float64`: 2,220e-16. A tolerância adotada para a variante `double` é cem vezes esse valor, 2,220e-14 volt, uma margem folgada, que ainda assim o erro medido, zero exato, cumpre com folga total. A checagem final confirma que o erro máximo em double está dentro da tolerância. Se este número, um dia, aparecer acima de um bilionésimo de volt, a conclusão correta não é ruído numérico aceitável — é que há um bug real de tradução entre o modelo e o template Jinja2, porque a física da aritmética IEEE-754 não produz esse tipo de divergência por acaso.

**[09:30–11:00 · Slide 3 — Duas ordens de grandeza de erro, double contra Q16.16]**

Este gráfico de barras, em escala logarítmica, contrasta os dois números que acabaram de aparecer: o erro máximo absoluto da variante `double`, virtualmente no piso do eixo, contra o erro máximo absoluto da variante Q16.16, cinco ordens de grandeza acima. A referência do épsilon de máquina aparece marcada como uma linha pontilhada próxima da base do gráfico. A leitura correta deste gráfico não é que Q16.16 está errado — é que Q16.16 introduz exatamente o erro de quantização que a Aula 13 já previu, e o SIL agora confirma numericamente, sobre uma sequência mais longa e mais adversa, com saturação e anti-windup ativos o tempo todo.

**[11:00–13:00 · TELA: terminal — projeto_nexabot]**

```bash
.venv/bin/python aula_14/03_regressao.py
```

A comparação pontual de um par de ganhos não basta como suíte de regressão: um bug de tradução pode se manifestar só sob combinações específicas de parâmetros. Este script generaliza a checagem usando a biblioteca Hypothesis, que gera vinte e cinco combinações aleatórias de `Kp`, `Ki`, `Kd` e `tau_f`, cada uma sobre uma sequência de referência e medição também gerada por semente diferente. A tolerância adotada é um bilionésimo de volt para `double` e meio volt para Q16.16, bem acima do épsilon de máquina, com folga para variações de biblioteca matemática entre plataformas. A tabela final mostra vinte e cinco linhas: em todas elas, o erro `double` aparece como zero exato, e o erro Q16.16 varia conforme os ganhos sorteados, entre cerca de 1,2e-04 e 1,5e-01 volt, sempre dentro da tolerância física adotada. A última linha confirma: vinte e cinco casos executados, nenhuma falha, regressão aprovada. É esta suíte, não a comparação pontual, que roda a cada mudança no repositório. A escolha de gerar combinações aleatórias de ganhos, em vez de fixar de antemão um punhado de casos "representativos", existe justamente para não deixar a suíte de regressão dependente da imaginação de quem a escreveu: um defeito que só aparece para uma combinação improvável de `Kd` e `tau_f`, por exemplo, tem chance real de ser sorteado ao longo de vinte e cinco execuções, e nenhuma chance de ser encontrado se só três casos fixos fossem testados para sempre.

### Demonstração ao vivo

**[13:00–15:30 · TELA: terminal — projeto_nexabot]**

Para tornar concreto o que "erro acima do esperado" significa na prática, o próximo script injeta, de propósito, um bug de tradução plausível:

```bash
.venv/bin/python aula_14/05_desafio.py
```

O contrato correto do anti-windup soma o produto de `Kaw` pela diferença entre o comando saturado e o não saturado, vezes `Ts`, à integral, quando o comando satura. O bug troca o sinal dessa diferença. Ambas as versões compilam sem erro nem aviso, com o mesmo tipo em cada operando — só uma comparação numérica contra o modelo revela a diferença, exatamente o tipo de defeito que uma revisão de código apressada, sem executar nada, tem boa chance de deixar passar. O primeiro cenário satura a referência em quinhentos e depois derruba para menos cinco volts, forçando o anti-windup a desenrolar o excesso de integral acumulado. O modelo termina em menos 24,0000 volt, tendo desenrolado corretamente. O código com o bug termina travado em mais 24,0000 volt — o sinal errado impede o desenrolamento —, e o erro máximo ao longo de todo esse cenário chega a 4,800e+01 volt: quarenta e oito volts, o dobro do fundo de escala do próprio driver de motor. É uma assinatura de bug impossível de confundir com ruído numérico.

O segundo cenário usa uma referência pequena que nunca satura o atuador. Nesse regime, o anti-windup nunca entra em ação, e o erro medido com o mesmo código, com o mesmo bug, cai para 0,000e+00 volt: o bug fica completamente invisível. É exatamente por isso que a suíte de regressão do bloco anterior varia ganhos e amplitude de referência: um único cenário fácil, só em regime linear, deixaria este defeito passar despercebido por toda a suíte de integração contínua. Para comparação, o mesmo cenário 1 rodado com o `SILController` correto, sem o bug, dá erro máximo de 0,000e+00 volt — a assinatura do defeito desaparece por completo assim que o sinal certo é restaurado.

**[15:30–16:30 · Slide 4 — Pipeline de CI da equivalência SIL]**

Este fluxograma resume o papel institucional de tudo o que apareceu até aqui: uma mudança no modelo, em `DiscretePID`, em `derive.py`, no template Jinja2, atravessa geração de código, compilação e a comparação `compare_model_vs_code`. Dentro da tolerância, o pipeline segue; acima dela, o build falha, com código de saída diferente de zero. É essa decisão binária, automatizada, que impede a equivalência de se perder silenciosamente entre uma alteração e outra, sem exigir que alguém lembre de testar manualmente antes de cada mudança.

**[16:30–18:00 · TELA: terminal — projeto_nexabot]**

```bash
.venv/bin/python aula_14/04_ci.py
```

Este script carrega `.github/workflows/mbd-ci.yml` com a biblioteca `pyyaml` e trata o próprio arquivo de integração contínua como mais um artefato verificável. Ele imprime, na ordem em que rodam, os oito passos do job único, chamado `mbd`: checkout, instalação do Python 3.12, instalação do `gcc`, instalação do projeto via `uv`, testes automatizados com pytest, a equivalência SIL desta aula, a matriz de rastreabilidade da Aula 16, e a publicação dessa matriz como artefato. Seis checagens de conteúdo seguem, todas confirmadas: o workflow roda pytest, roda a checagem de equivalência, roda a suíte de regressão, gera a matriz de rastreabilidade, instala `gcc`, pré-requisito para compilar o SIL, e dispara tanto em `push` quanto em `pull request`. Não basta o YAML parecer certo: este script verifica, programaticamente, que nenhum passo essencial foi esquecido na última edição do arquivo.

### Aplicação profissional

**[18:00–19:00 · Slide 5 — Onde a equivalência SIL aparece na indústria]**

Essa disciplina de comparar, numericamente, código gerado contra modelo de referência é rotina em indústrias que certificam software crítico. Na aeroespacial, sob DO-178C, verificar que o código-fonte é conforme aos requisitos de baixo nível é um objetivo formal da norma, com evidência exigida por auditoria. Na automotiva, sob ISO 26262, a verificação de unidade de software cumpre papel equivalente. Times de firmware automotivo costumam manter exatamente este tipo de suíte de equivalência rodando a cada mudança, contra a mesma unidade de controle de motor gerada por ferramenta comercial. Robótica industrial de armazém, o domínio mais próximo do NexaBot, adota o mesmo princípio de forma menos formalizada: antes de atualizar o firmware de uma frota inteira de robôs em operação, uma equipe séria roda a mesma comparação amostra a amostra contra a versão anterior, para garantir que a atualização não alterou silenciosamente o comportamento de controle. A diferença entre este laboratório e um processo de certificação real não está na técnica — está, como a Aula 16 vai detalhar, na independência de quem verifica e na qualificação formal das próprias ferramentas usadas.

### Fechamento

**[19:00–20:00 · TELA: terminal — projeto_nexabot]**

Fica registrado o essencial. Equivalência entre modelo e código gerado não é uma propriedade que se declara: é um número medido, amostra a amostra, sobre a mesma sequência de entradas. *Software-in-the-loop* executa o binário real do alvo, compilado para a máquina de desenvolvimento, dentro do mesmo processo do modelo, sem hardware algum. Na variante `double`, o erro esperado é da ordem do épsilon de máquina; o valor medido para o NexaBot, sobre seis mil amostras com saturação e anti-windup ativos, foi exatamente zero. Um bug real de tradução, como o anti-windup com sinal trocado, produz erro de quarenta e oito volts no cenário certo, e erro zero no cenário errado, o que justifica por que a suíte de regressão varia ganhos e amplitude de entrada.

Seu desafio prático: meça a equivalência do código gerado para três combinações diferentes de ganhos do PID e reporte se o erro Q16.16 medido é compatível com a análise de quantização da Aula 13.

Na próxima aula, a Aula 15, o controlador deixa de rodar dentro do mesmo processo Python: ele passa a rodar como um alvo separado, em tempo real, sujeito a jitter e latência de verdade — porque equivalência numérica prova que o código está certo, não que ele responde a tempo.

### Indicações de edição e recursos visuais

- TELA: terminal — mostrar a listagem de `nexabot/codegen/generated/` antes de qualquer explicação (00:00).
- Slide 1 — diagrama dos três passos da ponte SIL: compilar, carregar, comparar (02:00).
- Slide 2 — diagrama de duas colunas, Python e C, com as mesmas operações de ponto flutuante alinhadas lado a lado (05:30).
- Terminal — na tabela de `02_equivalencia.py`, destacar visualmente a linha `double`, com as três colunas em zero (07:00–09:30).
- Slide 3 — gráfico de barras em escala logarítmica, double contra Q16.16, com o épsilon de máquina marcado (09:30).
- Terminal — no bug de `05_desafio.py`, sincronizar a fala com o momento exato em que aparece o erro de 4,800e+01 volt, dando uma pausa de meio segundo antes de prosseguir (13:00–15:30).
- Slide 4 — fluxograma do pipeline de CI, com a bifurcação "dentro da tolerância" e "acima da tolerância" (15:30).

### Fontes e links de mídia

- IEEE. *IEEE Std 1012-2016: IEEE Standard for System, Software, and Hardware Verification and Validation*. New York: IEEE, 2017 — referência conceitual, sem reprodução de trecho externo.
- BROEKMAN, Bart; NOTENBOOM, Edwin. *Testing Embedded Software*. London: Addison-Wesley, 2003 — referência conceitual, sem reprodução de trecho externo.
- Nenhuma mídia de terceiros é incorporada; o gráfico de barras e o fluxograma de CI devem ser produzidos originalmente pela equipe de edição a partir deste roteiro e de `unidade_4.md` (Aula 14).

---

## Roteiro da Videoaula 15 — "Cinco milissegundos, de verdade"

**Vínculo com o plano de aprendizagem:** Unidade 4, Aula 15 — Hardware-in-the-loop, tempo real e jitter.

**Objetivo da videoaula:** ao final, o estudante deve ser capaz de explicar a diferença entre SIL e HIL, interpretar jitter e latência medidos em um laço de controle real, operar um watchdog de prazo com comando seguro em estouro, e situar com honestidade técnica o significado desses números medidos em um ambiente sem garantias de tempo real.

**Mapa de tempo e telas:** 00:00 terminal com a malha HIL em execução · 01:00 situação-problema · 02:00 slide "SIL prova equivalência, HIL prova prazo" · 03:30 editor `hil.py` · 05:00 slide do protocolo de linha · 07:00 terminal com o resultado da malha fechada · 09:00 terminal com jitter e latência · 11:30 slide de honestidade técnica · 12:30 terminal com o watchdog · 14:30 terminal com a recuperação do watchdog · 15:30 terminal com o menor Ts seguro · 17:00 slide da aplicação industrial · 18:15 pausa para reflexão · 18:45 pontos-chave e transição.

### Abertura contextualizada

**[00:00–01:00 · TELA: terminal — projeto_nexabot]**

A tela mostra o terminal já com a execução em andamento:

```bash
.venv/bin/python aula_15/01_loopback_hil.py
```

O NexaBot recebe um degrau de referência de cem radianos por segundo, e a tabela que rola na tela mostra a trajetória de velocidade angular ao longo de um segundo inteiro, com `Ts` de cinco milissegundos, duzentas amostras. Mas o detalhe que importa hoje não está na tabela de trajetória: está em como esse comando chegou até a planta. Diferente de toda a Unidade 2 e da Aula 14, o controlador que gerou cada valor de tensão nesta simulação não rodou dentro deste mesmo processo Python. Ele rodou como um processo separado, escrito em C, conversando com este script por um protocolo de texto simples.

**[01:00–02:00 · TELA: terminal — projeto_nexabot]**

O código C aprovado na Aula 14 foi verificado dentro do mesmo processo Python, sem restrição alguma de tempo: cada chamada a `.step()` devolvia o resultado imediatamente, sem competir por CPU com mais nada. Um colega, então, pergunta se já podemos confiar que isso vai rodar de verdade em um ESP32. A resposta honesta é não: nada, até aqui, testou o controlador como processo separado, sujeito a um sistema operacional de uso geral, sem garantia de que cada ciclo dure exatamente cinco milissegundos. Equivalência numérica prova que o código calcula o número certo. Não prova que ele calcula esse número a tempo. Esta aula muda exatamente esse eixo: o tempo deixa de ser uma variável silenciosa do gráfico e passa a ser uma restrição física medida.

### Desenvolvimento conceitual

**[02:00–03:30 · Slide 1 — SIL prova equivalência, HIL prova prazo]**

Este diagrama contrasta as duas técnicas lado a lado. *Software-in-the-loop*, à esquerda, executa modelo e código compilado dentro do mesmo processo, sem relógio de parede — a métrica é erro numérico. *Hardware-in-the-loop*, à direita, faz a planta rodar em tempo real, aguardando o tempo de parede necessário para respeitar `Ts`, enquanto o controlador roda como um alvo separado, acessível só por comunicação, como um microcontrolador real acessado por UART — a métrica passa a ser jitter e latência, em milissegundos. As duas propriedades são independentes: um controlador numericamente perfeito ainda pode falhar em produção se o alvo não responder dentro do prazo que a física do motor exige.

**[03:30–05:00 · TELA: editor — nexabot/hil.py]**

A tela muda para o editor, em `nexabot/hil.py`. A classe abstrata `Target` define o contrato mínimo de um alvo HIL: um método `step`, que recebe referência e medição e devolve a tensão de comando; um `reset`, que zera o estado interno, obrigatório ao sair do estado FALHA, REQ-SAFE-004; e um `close`. `LoopbackTarget`, a implementação usada nesta gravação, compila `nexabot/firmware/main_loopback.c` junto com o `pid_controller.c` gerado na Aula 13, e o executa como subprocesso local, falando por entrada e saída padrão. `SerialTarget`, logo abaixo no mesmo arquivo, implementa exatamente a mesma interface sobre uma porta serial real, para quem tem um ESP32 conectado por USB — não roda nesta máquina, por falta de hardware físico, mas o restante do código de malha fechada, `run_closed_loop_hil`, funciona sem alteração nenhuma ao trocar um back-end pelo outro.

**[05:00–07:00 · Slide 2 — O protocolo de linha entre host e alvo]**

O protocolo que os dois back-ends falam é deliberadamente simples: cada linha é um comando ASCII terminado em quebra de linha. O comando `STEP`, seguido de referência e medição, devolve a letra `U` seguida da tensão calculada. O comando `RESET` zera o estado interno e devolve `OK`. O comando `QUIT` encerra o processo — só existe no back-end de loopback; o alvo serial ignora. Um quarto campo opcional, o atraso em milissegundos, pede ao alvo que atrase sua resposta propositalmente — não é um simulacro em Python fingindo estar lento, é o próprio executável C dormindo de verdade antes de escrever no pipe. Esse campo existe só para o experimento de watchdog que a segunda metade desta aula demonstra.

**[07:00–09:00 · TELA: terminal — projeto_nexabot]**

Voltando à execução que já estava na tela desde o início, o mesmo `01_loopback_hil.py`: a velocidade final, média das últimas dez amostras, chega a 100,000 radianos por segundo, erro de regime permanente de 0,00 por cento frente à referência de cem radianos por segundo. A malha fechada funciona, com o controlador rodando fora do processo host, exatamente como funcionaria com um microcontrolador real. Mas a parte que interessa a esta aula aparece só no final da saída, na seção de estatísticas de tempo real: duzentas amostras, `Ts` nominal de 5,0000 milissegundos, período médio de 5,0886 milissegundos, desvio-padrão do jitter de 0,0396 milissegundo, jitter pico a pico de 0,1369 milissegundo, latência média de 0,0888 milissegundo, latência no percentil 95 de 0,1576 milissegundo, e latência máxima de 0,2415 milissegundo. Cada uma dessas linhas é uma medição real, tirada do relógio de parede deste computador durante esta própria execução, não um valor de referência copiado de manual algum. O próximo script aprofunda exatamente essas duas métricas, jitter e latência, sobre durações maiores.

### Demonstração ao vivo

**[09:00–11:30 · TELA: terminal — projeto_nexabot]**

```bash
.venv/bin/python aula_15/02_jitter.py
```

O script roda a mesma malha fechada três vezes, com durações crescentes — meio segundo, um segundo e dois segundos —, sempre sobre o mesmo `LoopbackTarget`, medindo duas grandezas por ciclo: latência, o tempo entre enviar `STEP` e receber a resposta, e jitter, a variação do período efetivo do laço em torno do `Ts` nominal de cinco milissegundos. Para cem amostras, em meio segundo, o período médio medido é 5,1260 milissegundos, o desvio-padrão do jitter é 0,0391 milissegundo, e o jitter pico a pico é 0,1103 milissegundo; a latência média fica em 0,1513 milissegundo, o percentil 95 em 0,3050 e a máxima em 0,3254 milissegundo. Para duzentas amostras, em um segundo, os números sobem discretamente: desvio-padrão do jitter 0,0428, latência máxima 0,3523 milissegundo. Para quatrocentas amostras, em dois segundos, desvio-padrão do jitter 0,0442, latência máxima 0,4083 milissegundo. O critério de aceitação adotado nesta aula é que o desvio-padrão do jitter não ultrapasse dez por cento do `Ts` nominal, meio milissegundo neste caso, e as três durações passam com folga ampla, na casa de poucos centésimos de milissegundo.

**[11:30–12:30 · Slide 3 — O que este jitter mede, e o que ele não mede]**

É indispensável ser preciso aqui, porque este número pode ser mal interpretado. O jitter e a latência que acabaram de aparecer são de um laço de controle escrito em Python de usuário, sem prioridade de tempo real e sem sistema operacional de tempo real, conversando com um subprocesso local por meio de um pipe, neste computador usado para gravar a aula — não são o jitter de um firmware bare-metal, ou rodando sob um sistema operacional de tempo real, em um microcontrolador dedicado como o ESP32 de destino final do NexaBot. Um firmware real, sem sistema operacional de uso geral competindo por CPU, tipicamente mede jitter em microssegundos, não nas dezenas de microssegundos a décimos de milissegundo que este ambiente produziu. O objetivo pedagógico desta aula é o método de medição, como caracterizar jitter e latência de um laço de controle discreto e como decidir se um valor medido é aceitável frente a um período de amostragem, não uma alegação de que este ambiente de desenvolvimento tem determinismo de tempo real. Repare que os próprios números confirmam essa leitura: um sistema operacional de uso geral, sem escalonamento determinístico, ainda assim produziu um desvio-padrão de jitter na casa de poucos centésimos de milissegundo — bom o suficiente para esta demonstração, mas não uma garantia formal que sobreviveria a uma carga de CPU competindo pelos mesmos recursos. Essa distinção volta a valer na Aula 16, ao discutir o que qualifica como evidência de certificação.

**[12:30–14:30 · TELA: terminal — projeto_nexabot]**

```bash
.venv/bin/python aula_15/03_watchdog_real.py
```

O prazo declarado ao `Watchdog` é três vezes o `Ts`, quinze milissegundos, uma folga razoável sobre os cinco milissegundos nominais. O comando de protocolo permite pedir ao alvo, de verdade, que atrase sua resposta antes de escrever de volta no pipe — não é uma simulação de atraso, é o subprocesso C dormindo de fato. No primeiro caso, sem atraso, o resultado é u igual a 10,600 volt, sem estouro de prazo, em 0,26 milissegundo de tempo real. No segundo caso, com atraso deliberado de duzentos milissegundos, muito acima do prazo de quinze, o resultado é u igual a 0,000 volt, com estouro de prazo confirmado. O tempo real registrado para esse segundo caso chega a 232,52 milissegundos, e vale explicar por quê: a decisão do watchdog, devolver tensão zero, segura, já foi tomada nos quinze milissegundos declarados; o tempo extra é só o custo de encerrar de verdade um processo que continua ocupado dormindo e só consegue processar o comando de encerramento depois de terminar de escrever a resposta pendente no pipe. A decisão de segurança e o custo de desligamento são coisas diferentes, e o script separa as duas com clareza.

**[14:30–15:30 · TELA: terminal — projeto_nexabot]**

Depois do estouro, o `Watchdog` encerrou o processo do alvo, exatamente como um supervisor real reiniciaria um microcontrolador travado. Um novo `LoopbackTarget` é então criado, o equivalente a um reinício, e uma nova chamada ao passo protegido devolve u igual a 10,600 volt, sem estouro de prazo: o sistema volta a operar normalmente. As três verificações finais do script confirmam: o caso dentro do prazo não estourou, o caso fora do prazo estourou com tensão segura de zero volt, e a recuperação após reconectar o alvo funciona. Esse é o núcleo do REQ-SAFE-004: um watchdog não é apenas esperar menos tempo — é decidir o que fazer quando o prazo estoura, com um comando seguro, e como se recuperar sem travar o laço host esperando indefinidamente por uma resposta que talvez nunca chegue.

**[15:30–17:00 · TELA: terminal — projeto_nexabot]**

O último script desta aula inverte a pergunta: dado o jitter já medido neste ambiente, qual é o menor `Ts` ainda seguro?

```bash
.venv/bin/python aula_15/04_desafio.py
```

Quatro candidatos são testados: cinco, dois, um e meio milissegundo, cada um sob o critério de que o atraso de pior caso não consuma mais que vinte por cento do período. Para `Ts` de cinco milissegundos, o atraso máximo medido é 0,1788 milissegundo, contra um limite de 1,0000 milissegundo: passa com folga. Para dois milissegundos, atraso máximo 0,0809, limite 0,4000. Para um milissegundo, atraso máximo 0,0731, limite 0,2000. Para meio milissegundo, atraso máximo 0,0696, limite 0,1000: ainda dentro do critério. O script conclui que o menor `Ts` seguro, neste ambiente e com esta margem, é meio milissegundo, o equivalente a dois mil hertz de frequência de amostragem. Vale repetir a ressalva: essa resposta depende do ambiente de execução, não só do algoritmo. Em um firmware bare-metal ou sob sistema operacional de tempo real dedicado, o jitter cairia ordens de grandeza, e o `Ts` mínimo seguro poderia ser bem menor que meio milissegundo.

### Aplicação profissional

**[17:00–18:15 · Slide 4 — Onde jitter, latência e watchdog aparecem na indústria]**

Esse par de conceitos, medir jitter e latência e proteger com um watchdog de prazo, atravessa toda a engenharia de sistemas ciberfísicos com requisitos de segurança. Em freio por fio automotivo, um atraso de comunicação acima do prazo aciona, por norma, um modo de operação degradado, nunca um comando indefinido. Em sistemas de comando de voo aeroespaciais, o conceito equivalente chama-se monitoramento de prazo de tarefa, e sua ausência é falha de projeto, não detalhe de implementação. Em robótica industrial, a categoria mais próxima do NexaBot, um botão de parada de emergência depende de um caminho de detecção e atuação com prazo máximo certificado, exatamente o papel que REQ-SAFE-004 e REQ-SAFE-006 cumprem neste projeto, embora, como toda a Aula 16 vai deixar explícito, sem qualificação formal de ferramenta nem auditoria independente.

**[18:15–18:45 · Slide 5 — Pausa para reflexão]**

Antes de fechar a aula, uma pausa para reflexão. Considere uma equipe que decide que, como o SIL da Aula 14 já provou equivalência numérica exata, não é mais necessário medir jitter e latência antes de embarcar o controlador em produção. Pause o vídeo e responda a quatro perguntas. Primeira: que tipo de defeito o SIL, por construção, nunca poderia revelar, mesmo com erro de equivalência igual a zero? Segunda: por que um controlador matematicamente correto ainda pode causar instabilidade real se o período efetivo variar de forma significativa em torno de `Ts`? Terceira: o watchdog desta aula zera o torque diante de um atraso de duzentos milissegundos sob um prazo de quinze. Que consequência teria a ausência dele, em um cenário de obstáculo, à luz do REQ-SAFE-006? Quarta: que evidência desta aula você apresentaria a um revisor técnico para justificar um teste em bancada com hardware real?

*[indicação de edição: inserir pausa com contagem regressiva de dez segundos e o texto "Pense e continue"]*

### Fechamento

**[18:45–20:00 · TELA: terminal — projeto_nexabot]**

Uma resposta madura reconhece que equivalência numérica e comportamento temporal são propriedades independentes: um controlador numericamente perfeito ainda pode falhar em produção se o alvo não responder dentro do prazo que a física exige. Nenhuma quantidade de comparação amostra a amostra, por mais rigorosa, substitui a pergunta de que esta aula tratou: o sistema responde a tempo? Ficam os pontos-chave desta aula. SIL prova equivalência numérica; HIL prova que o sistema respeita seu prazo, e nenhuma das duas substitui a outra. O protocolo de comando e resposta é idêntico entre o alvo local e um alvo serial real, permitindo desenvolver e demonstrar sem hardware físico. Jitter mede a variação do período do laço; latência mede o tempo de resposta de uma chamada individual, ambos medidos, nesta aula, na casa de décimos de milissegundo, com a ressalva explícita de que este é o jitter de um laço em Python de usuário, não de um firmware bare-metal. Um watchdog com prazo definido devolve comando seguro quando o alvo não responde a tempo, e sua ausência comprometeria diretamente REQ-SAFE-004 e REQ-SAFE-006.

Seu desafio prático: configure um watchdog com prazo de sete vírgula cinco milissegundos e injete atrasos de zero a vinte milissegundos, em passos de dois, registrando em que ponto ele estoura.

Na próxima aula, a Aula 16, que encerra a disciplina, essas peças de rastreabilidade se juntam em uma matriz única, e respondemos com precisão à pergunta que todo cliente de sistemas ciberfísicos críticos faz: isso está certificado?

### Indicações de edição e recursos visuais

- TELA: terminal — abrir a aula já com a tabela de trajetória rolando, sem pausa antes do primeiro corte (00:00).
- Slide 1 — diagrama de duas colunas, SIL à esquerda e HIL à direita, com a métrica de cada uma destacada (02:00).
- Slide 2 — diagrama de sequência do protocolo, host à esquerda, alvo à direita, com as mensagens `STEP`, `RESET` e `QUIT` (05:00).
- Terminal — na tabela de `02_jitter.py`, destacar a coluna do desvio-padrão do jitter nas três linhas (09:00–11:30).
- Slide 3 — cartaz com duas colunas, "este ambiente" e "firmware bare-metal", contrastando ordens de grandeza de jitter (11:30).
- Terminal — no watchdog, sincronizar a fala com o instante exato em que aparece `estourou_prazo = True` (12:30–14:30).
- Slide 5 — pausa com contagem regressiva de dez segundos e o texto "Pense e continue" (18:15).

### Fontes e links de mídia

- KOPETZ, Hermann. *Real-Time Systems: Design Principles for Distributed Embedded Applications*. 2. ed. New York: Springer, 2011 — referência conceitual, sem reprodução de trecho externo.
- LEE, Edward Ashford; SESHIA, Sanjit A. *Introduction to Embedded Systems: A Cyber-Physical Systems Approach*. 2. ed. Cambridge: MIT Press, 2017 — referência conceitual, sem reprodução de trecho externo.
- Nenhuma mídia de terceiros é incorporada; o diagrama de sequência e o cartaz de honestidade técnica devem ser produzidos originalmente pela equipe de edição a partir deste roteiro e de `unidade_4.md` (Aula 15).

---

## Roteiro da Videoaula 16 — "O que este pipeline prova, e o que ele não prova"

**Vínculo com o plano de aprendizagem:** Unidade 4, Aula 16 — Rastreabilidade, certificação e fechamento. Última aula da disciplina.

**Objetivo da videoaula:** ao final, o estudante deve ser capaz de gerar e interpretar a matriz de rastreabilidade do NexaBot, percorrer uma linha completa da matriz a partir de um requisito de segurança, distinguir com precisão entre evidência técnica produzida por um pipeline aberto e certificação formal sob DO-178C e ISO 26262, e relacionar as quatro camadas construídas ao longo da disciplina ao trabalho PBL de encerramento.

**Mapa de tempo e telas:** 00:00 terminal com a matriz de rastreabilidade · 01:00 situação-problema · 02:00 slide de DAL e ASIL · 03:30 editor `rastreabilidade.py` · 05:00 slide de qualificação de ferramenta · 07:00 terminal com a matriz completa e REQ-SAFE-006 · 09:30 slide da linha de REQ-SAFE-006 · 11:00 terminal com evidências e certificação · 13:30 slide "produz" e "não produz" · 15:00 terminal com as lacunas de teste · 16:30 slide da aplicação industrial · 17:30 fechamento da disciplina · 19:00 encerramento definitivo.

### Abertura contextualizada

**[00:00–01:00 · TELA: terminal — projeto_nexabot]**

O terminal já mostra a execução mais recente:

```bash
.venv/bin/python aula_16/01_matriz_rastreabilidade.py
```

Ao final de uma apresentação do NexaBot a um cliente de robótica industrial, é comum alguém perguntar se esse pipeline gera evidência suficiente para certificar o robô conforme a ISO 26262. A saída na tela, noventa e um arquivos Python lidos, catorze requisitos distintos localizados, uma tabela inteira de rastreabilidade, é exatamente o tipo de material que alimenta essa pergunta. E a resposta errada mais comum, nesse momento, é otimista demais: listar tudo o que foi construído ao longo da disciplina e concluir que isso é certificação.

**[01:00–02:00 · TELA: terminal — projeto_nexabot]**

Não é. Esta última aula constrói o vocabulário exato para responder com precisão. O pipeline produz evidência técnica reproduzível. Um processo real acrescenta independência adequada, gestão de configuração, análise de confiança nas ferramentas e avaliação pela autoridade ou organismo competente. Ao longo dos próximos vinte minutos, vamos percorrer uma linha da matriz, comparar evidências com objetivos de duas normas e fechar a disciplina com honestidade técnica.

### Desenvolvimento conceitual

**[02:00–03:30 · Slide 1 — Níveis de criticidade: DAL e ASIL]**

A DO-178C, sigla para *Software Considerations in Airborne Systems and Equipment Certification*, é o padrão da RTCA para certificação de software embarcado em aviônica civil. Ela define cinco níveis de garantia de projeto, os DAL, de A a E, proporcionais à gravidade de uma falha: o nível A cobre uma falha catastrófica, com potencial perda da aeronave; o nível E cobre uma falha sem efeito operacional relevante. Quanto mais crítico o nível, mais a norma exige: cobertura estrutural de código, independência entre quem desenvolve e quem verifica, rastreabilidade obrigatória entre requisito, projeto, código-fonte e caso de teste.

A ISO 26262 cumpre papel equivalente na indústria automotiva, com quatro Níveis de Integridade de Segurança Automotiva, os ASIL, de A a D, proporcionais a severidade, exposição e controlabilidade do risco. Como a DO-178C, ela também exige rastreabilidade bidirecional, exatamente a estrutura que a matriz desta aula constrói, de baixo para cima, para o NexaBot.

**[03:30–05:00 · TELA: editor — nexabot/rastreabilidade.py]**

A tela muda para o editor, em `nexabot/rastreabilidade.py`. A ideia central deste módulo está em duas estruturas. Primeiro, uma expressão regular que localiza qualquer identificador no formato requisito, família, número em docstrings e comentários de todo o pacote. Segundo, uma lista de regras de classificação: qualquer arquivo em `nexabot/codegen/derive.py`, `generate.py`, a pasta de arquivos gerados ou de templates, ou em `nexabot/firmware/`, entra na coluna "Código gerado"; qualquer arquivo em `tests/` ou em uma pasta de aula entra na coluna "Teste"; qualquer outro arquivo dentro de `nexabot/` entra na coluna "Modelo"; o que sobra vai para "Outros". Essa varredura é estática, lê texto, não executa nada, e funciona mesmo que módulos de outras frentes da disciplina ainda não existam neste checkout: ausência de módulo vira aviso, nunca erro. É rastreabilidade de baixo para cima, derivada do próprio código, não mantida à mão em uma planilha separada que inevitavelmente fica desatualizada.

**[05:00–07:00 · Slide 2 — Qualificação de ferramenta: a questão central de uma pilha aberta]**

Ambas as normas tratam da confiança em ferramentas. Se uma ferramenta automatiza uma etapa, a equipe analisa o impacto de um possível erro e se a verificação posterior conseguiria detectá-lo. A partir disso, define controles, verificação independente ou qualificação no nível aplicável. A DO-178C remete aos critérios complementares do DO-330; a ISO 26262 trata da confiança no uso de ferramentas na parte 8, cláusula 11.

A licença aberta não muda esse raciocínio. SymPy, Jinja2 e GCC não vêm automaticamente qualificados para este processo; uma ferramenta comercial comum também não. Caso a análise do uso indique qualificação, ela será um projeto de engenharia separado. Caso uma verificação independente suficiente detecte os erros relevantes, a estratégia pode ser outra — e precisa ser documentada.

### Demonstração ao vivo

**[07:00–09:30 · TELA: terminal — projeto_nexabot]**

No terminal, a execução de `01_matriz_rastreabilidade.py` confirma noventa e um arquivos Python lidos e catorze requisitos encontrados. Ao final, aparece uma lacuna real: um dos catorze requisitos não tem evidência na coluna "Teste". A matriz é deliberadamente conservadora e sua presença não substitui revisão humana da qualidade de cada evidência.

Vou percorrer a linha de REQ-SAFE-007. A descrição limita a velocidade linear a um vírgula vinte metro por segundo no domínio operacional especificado. A coluna "Modelo" aponta para `nexabot/requisitos.py`, onde a lacuna é registrada. "Código gerado" está vazio, pois o gerador cobre o PID, não esse requisito de sistema. "Teste" também está vazio: os testes discretos do supervisor não observam a trajetória contínua da velocidade. A matriz não esconde essa ausência nem chama uma demonstração indireta de prova.

Aqui aparece uma distinção que vale praticar antes de qualquer projeto real. Uma célula preenchida responde "há um arquivo relacionado?"; ela não responde automaticamente "a evidência é suficiente?". Para REQ-SAFE-001, por exemplo, existe predicado executável, exploração das transições alcançáveis e teste. Mesmo assim, a conclusão continua limitada ao supervisor modelado e às entradas discretizadas. Para REQ-SAFE-007, nem essa primeira camada foi fechada. O valor da matriz está justamente em impedir que essas duas situações recebam o mesmo rótulo genérico de "testado".

Para transformar o requisito de velocidade em uma verificação defensável, eu começaria tornando explícita a expressão "domínio operacional". Quais referências de velocidade são permitidas? Qual intervalo de carga atua sobre o eixo? Qual tensão de bateria, inclinação de piso, raio de roda e atraso de comunicação entram na análise? Qual duração de trajetória é suficiente para capturar transientes e mudanças de carga? Sem essas fronteiras, a frase "nunca ultrapassa" quantifica sobre um universo indefinido e nenhum teste pode encerrá-la honestamente.

Em seguida, eu definiria o oráculo. A velocidade linear vem de $v=r\omega$, usando o raio de roda e a velocidade angular do modelo. A cada amostra, o teste compara esse valor com um vírgula vinte, incluindo uma tolerância numérica declarada. Depois vêm os estímulos: degraus, rampas, mudanças de carga, tensão máxima e combinações de parâmetros nas bordas do domínio. Hypothesis pode gerar essas combinações e reduzir um caso que viole o limite. Mas, se todas passarem, a conclusão correta é "não encontramos violação no conjunto coberto", e não "provamos para todo cenário físico".

Uma garantia mais forte poderia combinar análise de alcançabilidade de um modelo contínuo ou híbrido, intervalos sobre parâmetros e ensaios no hardware. O nível de esforço depende do risco. Para um protótipo didático, uma campanha reprodutível e bem delimitada pode bastar. Para um robô que opera perto de pessoas, a equipe precisaria justificar por que o domínio representa o campo e como incertezas de sensor, atrito e atraso foram cobertas. A mesma linha da matriz comporta ambos os contextos; o que muda é a suficiência exigida da evidência.

**[09:30–11:00 · Slide 3 — A linha de REQ-SAFE-007, em quatro células]**

O diagrama mostra quatro células: Requisito e Modelo preenchidas; Código gerado e Teste vazias. Para fechar a última célula, seria preciso especificar o domínio operacional, integrar planta, controlador e supervisor e adotar um critério de cobertura compatível com a garantia desejada. Rodar algumas trajetórias pode encontrar uma violação, mas ausência de contraexemplo em uma amostra não prova o limite universal.

**[11:00–13:30 · TELA: terminal — projeto_nexabot]**

```bash
.venv/bin/python aula_16/02_evidencias.py
```

Este script inventaria cinco evidências efetivamente produzidas e as associa a objetivos de norma. A matriz precisa de revisão independente e ainda mostra REQ-SAFE-007 sem teste. A equivalência SIL é valiosa, mas o projeto não integra cobertura estrutural como critério de aceitação. Para a geração automática, ainda falta analisar formalmente o uso e decidir quais verificações ou qualificações se aplicam a SymPy, Jinja2 e GCC. A CI não substitui uma baseline controlada. E o watchdog carece de justificativa de segurança para o prazo de três vezes $T_s$ e de verificação no hardware-alvo.

O resumo executivo fixa quatro pontos: uma suíte de scripts não certifica um produto; o projeto usa ferramentas sem análise formal de confiança para este processo; código aberto ou comercial não decide a qualificação; e o laboratório produz artefatos de entrada para um processo de garantia, não a aprovação final.

**[13:30–15:00 · Slide 4 — Duas colunas: o que o pipeline produz, o que ele não produz]**

Este cartaz resume duas colunas. À esquerda: modelo versionado, propriedades verificadas no escopo declarado, testes com cobertura, código ligado por hash aos parâmetros, equivalência numérica e CI reprodutível. À direita: independência adequada, decisão documentada sobre confiança e qualificação de ferramentas, WCET no alvo real e avaliação pela autoridade ou organismo competente. O jitter da Aula 15 é amostragem empírica, não prova de limite superior.

**[15:00–16:30 · TELA: terminal — projeto_nexabot]**

```bash
.venv/bin/python aula_16/03_desafio.py
```

O script identifica automaticamente a lacuna: REQ-SAFE-007. Não oferece uma solução pronta; pede que o estudante proponha domínio, estímulos, oráculo e critério de suficiência. Essa é uma entrega melhor do que preencher uma célula com qualquer arquivo apenas para fazer a matriz parecer completa.

Ao gravar esta demonstração, vale abrir `rastreabilidade.md` depois da execução e apontar a linha completa. O arquivo é o artefato persistente; a tabela do terminal é apenas uma visualização momentânea. Se alguém adicionar amanhã um teste que mencione o identificador, a coluna será preenchida na próxima execução. Isso é útil, mas também revela a limitação do método: a varredura encontra referências textuais, não entende a semântica do teste. Uma revisão humana precisa confirmar se o arquivo realmente verifica o requisito, se o oráculo está correto e se o resultado foi produzido no ambiente controlado. Automação reduz trabalho repetitivo; não elimina julgamento de engenharia.

Esse ponto também explica por que o pipeline de integração contínua não deve receber o rótulo de certificador. Ele executa comandos conhecidos, preserva registros e impede que uma regressão evidente seja integrada. É excelente para repetibilidade. Porém, não escolhe requisitos, não valida premissas físicas, não decide se uma tolerância é segura e não cria independência organizacional. Quando a esteira fica verde, ela afirma apenas que os critérios codificados passaram naquela revisão e naquele ambiente. A equipe ainda responde pela qualidade dos critérios.

Antes de sair do terminal, faço uma última checagem prática. Abro o cabeçalho da matriz, confirmo a data de geração e procuro o identificador do requisito. Depois comparo os caminhos listados com o repositório. Esse gesto simples evita apresentar como atual um relatório antigo. Em uma revisão profissional, eu anexaria também a revisão do código, a versão das dependências e os resultados brutos dos testes. Reprodutibilidade não é apenas conseguir rodar de novo: é saber exatamente qual configuração produziu a evidência que está sendo avaliada.

### Aplicação profissional

**[16:30–17:30 · Slide 5 — Automotivo, aeroespacial, robótica industrial]**

No automotivo, requisitos temporais e de segurança são tratados em um processo ISO 26262 com ASIL derivado da análise de perigos. No aeroespacial, rastreabilidade, planos, independência e confiança em ferramentas seguem critérios do nível de software e do uso concreto. Na robótica industrial, normas específicas exigem desempenho seguro conforme a aplicação. Os processos diferem; a obrigação comum é sustentar a alegação com evidência adequada ao risco.

### Fechamento

**[17:30–19:00 · TELA: terminal — projeto_nexabot]**

Esta é a última aula, e vale reconhecer o percurso. Na Aula 1, o NexaBot era um desenho com motor de corrente contínua, roda e alimentação de vinte e quatro volts. A Unidade 1 transformou o desenho em modelo identificado. A Unidade 2 fechou a malha com PID, amostragem justificada, anti-windup e co-simulação. A Unidade 3 provou REQ-SAFE-001 a 006 no escopo dos modelos adotados e manteve REQ-SAFE-007 aberto. A Unidade 4 gerou código, mediu equivalência e comportamento temporal e produziu uma matriz que mostra tanto evidências quanto lacunas.

Essa progressão, modelar, controlar, provar, embarcar com evidência, sustenta qualquer sistema ciberfísico confiável, de um satélite a um braço robótico industrial. O que muda entre domínios é o nível de criticidade e o processo formal de certificação, nunca a exigência de que uma afirmação sobre o sistema só vale quando sustentada por evidência reproduzível.

Fica um convite direto para o trabalho PBL que encerra a disciplina: aplique, a um sistema ciberfísico novo, o mesmo percurso de quatro camadas, modelo, controle, verificação formal, código com rastreabilidade, com o mesmo rigor desta última aula. Não "eu acho que funciona": aqui está o número que mostra isso, e aqui está exatamente o que esse número não prova.

**[19:00–20:00 · TELA: terminal — projeto_nexabot]**

Ficam os pontos-chave. DO-178C e ISO 26262 usam classificações de criticidade que influenciam o rigor de verificação. Confiança em ferramentas depende do uso, não da licença. O pipeline produz modelo versionado, propriedades no escopo declarado, testes, código rastreável, equivalência e CI; não produz sozinho independência, análise completa de ferramentas, WCET no alvo ou aprovação externa. A competência transferível é sustentar cada afirmação com evidência reproduzível e declarar com clareza o que ela não prova.

Esta foi a última videoaula de Model-Based Design for Cyber-Physical Systems. Obrigado pela atenção ao longo das dezesseis aulas, e bom trabalho no projeto que encerra a disciplina.

### Indicações de edição e recursos visuais

- TELA: terminal — abrir já com a matriz de rastreabilidade completa na tela, rolada até o topo (00:00).
- Slide 1 — duas réguas horizontais lado a lado, DAL de A a E e ASIL de A a D, com cores indicando severidade crescente (02:00).
- Slide 2 — diagrama do pipeline de sete etapas, com um selo "qualificado" ou "não qualificado" sobre cada ferramenta (05:00).
- Terminal — destacar a linha de REQ-SAFE-007 na tabela de `01_matriz_rastreabilidade.py` (07:00–09:30).
- Slide 3 — diagrama de quatro células para REQ-SAFE-007, com "Código gerado" e "Teste" marcados como lacunas (09:30).
- Slide 4 — cartaz de duas colunas, "produz" à esquerda com seis itens, "não produz" à direita com quatro itens (13:30).
- Terminal — encerrar a aula com um plano geral lento do terminal, sem cortes abruptos, nos últimos dez segundos (19:00–20:00).

### Fontes e links de mídia

- RTCA. *DO-178C: Software Considerations in Airborne Systems and Equipment Certification*. Washington, D.C.: RTCA, 2011 — referência conceitual, sem reprodução de trecho externo.
- ISO. *ISO 26262: Road Vehicles — Functional Safety*. Geneva: International Organization for Standardization, 2018 — referência conceitual, sem reprodução de trecho externo.
- Nenhuma mídia de terceiros é incorporada; as réguas de criticidade e o cartaz "produz/não produz" devem ser produzidos originalmente pela equipe de edição a partir deste roteiro e de `unidade_4.md` (Aula 16).
