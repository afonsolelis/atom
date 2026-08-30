# Unidade 4 — Geração de código, integração hardware-software e evidências

Disciplina: Model-Based Design for Cyber-Physical Systems
Professor-conteudista: Afonso Cesar Lelis Brandão

## Relação da unidade com a atuação profissional

Nas três unidades anteriores, o NexaBot existiu inteiramente em Python: um modelo em espaço de estados, um controlador PID discreto, um supervisor de segurança verificado exaustivamente. Todo esse trabalho, por mais rigoroso que tenha sido, ainda não liga a nenhum motor real. Esta unidade fecha essa lacuna. Ela trata da etapa em que o modelo validado deixa de ser um objeto de estudo e passa a ser um binário que roda em um microcontrolador de 32 bits, sob um período de amostragem de 5 ms, respondendo a sensores e acionando um driver de motor de até 24 V. É exatamente esse trecho do trabalho — do modelo correto ao firmware confiável — que separa a engenharia de controle acadêmica da engenharia de sistemas embarcados profissional, e é nele que a maioria dos defeitos de integração hardware-software realmente se manifesta.

O mercado de sistemas ciberfísicos remunera de forma diferenciada quem domina essa transição. Engenheiros de controle embarcado, de firmware automotivo e de verificação de software aeroespacial são avaliados pela capacidade de responder a três perguntas que esta unidade constrói: o código que roda no alvo é, comprovadamente, o mesmo comportamento do modelo verificado? O sistema atende ao prazo quando o tempo deixa de ser eixo de gráfico e vira restrição física? E, quando alguém pergunta "isso está certificado?", a resposta técnica é dada sem exagero e sem insegurança.

Essa terceira pergunta é talvez a mais importante para a carreira. Profissionais sob normas como DO-178C (aviônica) ou ISO 26262 (automotiva) enfrentam rotineiramente decisões sobre ferramentas abertas, geradores automáticos e CI. Saber o que um pipeline produz como evidência técnica — e o que ele nunca produzirá sozinho, porque depende de processo organizacional, independência de verificação e qualificação de ferramenta — separa quem é levado a sério em uma revisão de segurança de quem não é. Robótica industrial, AGVs como o NexaBot, tração automotiva e comando de voo compartilham essa exigência de honestidade técnica.

Ao final desta unidade, o estudante terá percorrido o ciclo completo de design baseado em modelos: modelar, controlar, provar e, agora, embarcar com rastreabilidade. Essa é a competência central anunciada na ementa da disciplina, e é também exatamente o que o trabalho PBL de encerramento exige: não apenas um sistema que funciona, mas um sistema cuja correção pode ser demonstrada, artefato por artefato, do requisito ao binário.

## O que você verá nesta unidade

A Unidade 4 acompanha o NexaBot na travessia final: do modelo de controle validado ao código que efetivamente roda em um alvo. Na Aula 13, você gerará automaticamente o código C do PID discreto a partir do modelo, com um bloco de rastreabilidade gravado no próprio arquivo e uma comparação explícita entre ponto flutuante e ponto fixo Q16.16. Na Aula 14, você provará, amostra a amostra, que o código gerado se comporta como o modelo — e verá o que acontece quando essa prova falha por um bug real. Na Aula 15, o controlador sairá do processo Python e passará a rodar como um alvo separado, em tempo real, sujeito a jitter e latência de verdade, com um watchdog protegendo o sistema quando o alvo atrasa. Na Aula 16, você montará a matriz de rastreabilidade completa do NexaBot, discutirá com propriedade o que a DO-178C e a ISO 26262 exigem de um pipeline de ferramentas, e encerrará a disciplina conectando as quatro unidades ao trabalho PBL.

## Aula 13 — Geração automática de código a partir do modelo

### Situação-problema: o ganho que ninguém digitou errado, mas quase foi

Um engenheiro júnior recebe a tarefa de "passar o PID para C". Abre `controllers.py`, lê os ganhos `Kp=2.0`, `Ki=40.0`, `Kd=0.02` e começa a digitar o equivalente em C à mão. Distraído, digita `Ki = 4.0` em vez de `40.0` — um dígito a menos, sem erro de compilação, sem aviso de tipo, nada que denuncie a falha antes de o motor rodar devagar demais no banco de testes. O bug não está em lógica complexa: está no ato mecânico e falível de copiar um número de um lugar para outro — um erro de transcrição comum em sistemas embarcados críticos, e exatamente o que esta aula elimina: não com mais disciplina de revisão, mas com uma mudança estrutural. O código C deixa de ser digitado e passa a ser gerado.

### Código gerado é artefato derivado, nunca editado à mão

O arquivo `pid_controller.c` (e seu cabeçalho `pid_controller.h`) não é escrito por uma pessoa: é produzido por `nexabot/codegen/generate.py` a partir de uma instância de `DiscretePID`, o modelo de referência desde a Aula 7. Diante de um bug no C gerado, a resposta nunca é "edite o `.c`", porque a próxima geração sobrescreve qualquer edição sem aviso — é sempre "corrija o modelo e regere". O código gerado é, por definição, artefato derivado: sua fonte de verdade vive em outro lugar, versionada e testável.

### O bloco de rastreabilidade no cabeçalho gerado

Cada arquivo gerado carrega, no topo, um bloco de comentário que o religa ao modelo: requisitos de origem (`REQ-CTRL-001` a `003`, mais `REQ-CODEGEN-001`/`002`), versão do pacote, um hash SHA-256 determinístico dos sete parâmetros, data em UTC e a advertência **ARQUIVO GERADO AUTOMATICAMENTE — NÃO EDITAR MANUALMENTE**. Para `Kp=2,0`, `Ki=40,0`, `Kd=0,02`, `Ts=0,005`, `u_max=24,0`, `tau_f=0,01`, `Kaw=1,0`, esse hash vale exatamente `dc3b95c3d13a052d4dee683c2d5cd75bbc3c3996dede09f747dc8c076c32fa13`. Mudar um único ganho muda o hash inteiro, o que a atividade desta aula explora.

> **Recurso visual 1 — Anatomia do bloco de rastreabilidade.** Captura de tela do cabeçalho de `pid_controller.c`, com chamadas apontando para cada campo: requisitos de origem, versão do modelo, hash SHA-256, data UTC e a advertência de não edição manual.
> *Texto alternativo:* comentário de cabeçalho em C mostrando seis campos de rastreabilidade anotados: requisitos REQ-CTRL-001 a 003 e REQ-CODEGEN-001/002, versão do pacote nexabot, hash SHA-256 dos parâmetros, timestamp de geração em UTC e a frase de advertência contra edição manual.

### Derivação simbólica: da forma contínua à equação de diferenças

As duas equações de diferenças do C gerado — termo integral e termo derivativo filtrado — não são digitadas a partir do contrato de `DiscretePID.step`: são derivadas simbolicamente pelo SymPy, em `nexabot/codegen/derive.py`, a partir da forma contínua do PID (Aula 6: $K_p + K_i/s + K_d N s/(s+N)$), pela substituição de Euler para trás $s \to (1-z^{-1})/T_s$:

$
I[k] = I[k-1] + K_i T_s\, e[k], \qquad D[k] = \frac{K_d\,(e[k]-e[k-1]) + \tau_f D[k-1]}{\tau_f + T_s}.
$

O módulo verifica automaticamente a diferença simbólica entre essa recorrência e o contrato de `DiscretePID.step`, levantando erro se o resíduo não for identicamente zero: o gerador se recusa a produzir um C que discorde do modelo.

### Ponto flutuante contra ponto fixo Q16.16

O raciocínio até aqui assume `double`, a mesma aritmética do modelo Python. Microcontroladores de baixo custo — inclusive variantes do ESP32 sem unidade de ponto flutuante — emulam `double` em software, a um custo que pode comprometer os 5 ms do período de amostragem. A alternativa é o **ponto fixo**: representar um real como inteiro com número fixo de bits fracionários.

O formato adotado é **Q16.16**: `int32_t` com 16 bits inteiros e 16 fracionários. Um real $x$ vira $x_{\text{fixo}}=\mathrm{round}(x\cdot2^{16})$, recuperado por $x\approx x_{\text{fixo}}/2^{16}$. A resolução é

$
\Delta = 2^{-16} = \frac{1}{65536} \approx 1{,}526 \times 10^{-5},
$

com erro máximo de arredondamento de metade disso, $\Delta/2\approx7{,}629\times10^{-6}$. Multiplicação e divisão exigem acumulador de 64 bits (`int64_t`) antes do deslocamento que normaliza o resultado — o que `pid_fixed_mul`/`pid_fixed_div` implementam.

### Exemplo numérico: o erro de quantização introduzido pelo Q16.16

Nem todo parâmetro sofre o mesmo erro. Um valor múltiplo exato de $2^{-16}$ é representado sem erro; um que não é, sofre arredondamento. Dos sete parâmetros do NexaBot, $K_p=2{,}0$, $K_i=40{,}0$, $u_{max}=24{,}0$ e $K_{aw}=1{,}0$ quantizam exatamente (seus produtos por $2^{16}$ são inteiros). Já $T_s$ e $\tau_f$ não são:

$
T_s \cdot 2^{16} = 327{,}68 \;\rightarrow\; \mathrm{round}=328 \;\rightarrow\; T_{s,\text{fixo}} = \frac{328}{65536} = 0{,}0050048828125\,\mathrm{s} \quad (\text{erro } +4{,}883\times10^{-6}\,\mathrm{s}),
$

$
\tau_f \cdot 2^{16} = 655{,}36 \;\rightarrow\; \mathrm{round}=655 \;\rightarrow\; \tau_{f,\text{fixo}} = \frac{655}{65536} = 0{,}0099945068359375\,\mathrm{s} \quad (\text{erro } -5{,}493\times10^{-6}\,\mathrm{s}).
$

$K_d=0{,}02$ quantiza para $1311/65536=0{,}0200042724609375$ (erro $-4{,}272\times10^{-6}$). Os três erros ficam abaixo do limite teórico de meia resolução ($7{,}629\times10^{-6}$), como esperado — mas nenhum é zero, e $T_s$ e $\tau_f$ entram juntos no denominador $(\tau_f+T_s)$ do termo derivativo, combinando dois erros de quantização antes de qualquer entrada ser processada. A Aula 14 mede quanto esse acúmulo se propaga até o comando final.

> **Recurso visual 2 — Reta numérica Q16.16.** Reta com os valores representáveis em torno de 0,01 s, passo $2^{-16}$, com $\tau_f=0{,}01$ entre dois pontos de grade e seta indicando o arredondamento para $655/65536$.
> *Texto alternativo:* reta numérica com marcas espaçadas por 1,526e-5, mostrando que 0,01 cai entre duas marcas e é arredondado para 0,0099945068359375.

> **Recurso visual 3 — Pipeline de geração de código.** Diagrama de três caixas: derivação simbólica (SymPy) → extração de ganhos (`_pid_gains`) → renderização (templates Jinja2), convergindo para `pid_controller.h`/`.c` com o bloco de rastreabilidade destacado.
> *Texto alternativo:* diagrama de fluxo mostra a derivação simbólica das equações, a extração dos sete ganhos do modelo e a renderização por templates Jinja2 produzindo os arquivos C finais, com o bloco de rastreabilidade em destaque no topo do arquivo gerado.

### Laboratório da aula

Em `projeto_nexabot/aula_13/`, `01_do_modelo_ao_c.py` deriva os termos integral e derivativo e confirma a igualdade com o contrato de `DiscretePID.step`. Em seguida, `02_gera_codigo.py` gera as variantes `double` e Q16.16, mostra o código e comprova que parâmetros iguais preservam o hash, enquanto `K_p=3{,}5` o altera. `03_ponto_fixo.py` mede, em 4.000 amostras, erro máximo de aproximadamente $6{,}55\times10^{-2}\,\mathrm{V}$ para Q16.16 e erro nulo na variante `double`. O desafio `04_desafio.py` compara Euler para trás com Tustin no termo integral e explicita o estado adicional exigido pela regra trapezoidal.

### Atividade prática

Escolha um ganho do PID e altere-o em 10%. Regenere o código, registre o novo hash e escreva três frases sobre o que mudou no `.c` além do valor do parâmetro. Converta esse mesmo ganho para Q16.16 e calcule seu erro de quantização, seguindo o procedimento do exemplo numérico desta aula.

### Síntese da aula

- Código C digitado à mão introduz erros de transcrição que a compilação não detecta; a geração automática elimina essa classe de defeito.
- Um arquivo gerado é artefato derivado: correções acontecem sempre no modelo, nunca no `.c`, sobrescrito a cada geração.
- O bloco de rastreabilidade liga qualquer binário em produção de volta aos requisitos, à versão do modelo e a um hash determinístico dos parâmetros.
- As recorrências do PID discreto são derivadas simbolicamente pelo SymPy, com verificação automática contra o contrato de `DiscretePID.step`.
- Q16.16 representa um real como inteiro de 32 bits com resolução $2^{-16}\approx1{,}526\times10^{-5}$; parâmetros não múltiplos exatos dessa resolução sofrem erro de quantização mensurável.

### Roteiro da Videoaula 13 — "O código que ninguém digita"

O roteiro falado completo, com narração pronta para gravação, marcações de tela e comandos literais, está no arquivo `roteiros_20min.md` desta unidade, retomando o erro de transcrição da situação-problema como fio condutor da demonstração de geração de código.

### Referências da aula

- LEE, Edward Ashford; SESHIA, Sanjit A. *Introduction to Embedded Systems: A Cyber-Physical Systems Approach*. 2. ed. Cambridge: MIT Press, 2017.
- YATES, Randy. *Fixed-Point Arithmetic: An Introduction*. Digital Signal Labs, Technical Reference, 2013.
- WHALEN, Michael W.; HEIMDAHL, Mats P. E. On the requirements of high-integrity code generation. In: IEEE INTERNATIONAL SYMPOSIUM ON HIGH-ASSURANCE SYSTEMS ENGINEERING, 4., 1999, Washington, D.C. *Proceedings [...]*. Washington, D.C.: IEEE, 1999. p. 217-224. DOI: 10.1109/HASE.1999.809495.

## Aula 14 — Software-in-the-loop e equivalência modelo-código

### Situação-problema: "equivalente" é uma alegação até virar um número

Depois de gerar `pid_controller.c` na Aula 13, um colega afirma: "o C é equivalente ao modelo Python, porque foi gerado a partir dele". A frase soa razoável, mas é o tipo de afirmação que este curso rejeita sem evidência: gerar a partir de um modelo reduz a chance de erro, não a elimina — o gerador pode ter um bug, o template pode renderizar um operador errado, a conversão de ponto fixo pode introduzir mais erro que o esperado. "Equivalente" não é adjetivo que se declara; é medição feita, amostra a amostra, sobre a mesma sequência de entradas. Esta aula transforma a alegação em número — e mostra, com um bug real e deliberado, o que acontece quando esse número deixa de ser desprezível.

### Software-in-the-loop: compilar, carregar, comparar

*Software-in-the-loop* (SIL) executa o código gerado, compilado para a arquitetura do computador de desenvolvimento (não o alvo final), lado a lado com o modelo, no mesmo processo. Em `nexabot/sil.py`, isso compila `pid_controller.c` com `gcc -O2 -fPIC -shared` em uma biblioteca (`libpid_sil.so`), carregada via `ctypes`. `SILController` expõe a mesma interface de `DiscretePID` (`.step(r, y)`), mas cada chamada executa `pid_step`/`pid_fixed_step` dentro da biblioteca compilada — não simula o código, executa o binário real, só que para x86_64/ARM64 em vez do microcontrolador. É a forma mais barata de achar um defeito de geração de código, sem hardware algum.

> **Recurso visual 4 — Arquitetura SIL.** Diagrama mostrando o processo Python com dois caminhos paralelos sobre a mesma entrada $(r[k],y[k])$: `DiscretePID` (modelo) e `SILController` chamando, via `ctypes`, `pid_step` dentro de `libpid_sil.so` compilada a partir do C gerado.
> *Texto alternativo:* diagrama de arquitetura SIL mostra modelo Python e código C compilado recebendo a mesma sequência de entrada dentro do mesmo processo, sem hardware envolvido.

### `compare_model_vs_code`: o erro amostra a amostra

A função central desta aula roda `DiscretePID` (modelo) e `SILController` (código C) sobre exatamente a mesma sequência $(r[k], y[k])$, sem que um realimente a saída do outro — isolando o erro de geração de código do erro de simulação de malha fechada. Devolve o erro máximo absoluto, o erro médio absoluto, o erro RMS e o índice da amostra de pior caso.

### Exemplo numérico: equivalência na ordem do épsilon de máquina

Rodando essa comparação sobre 2.000 amostras (10 s a $T_s=5\,\mathrm{ms}$, degrau de 15 rad/s seguido de componente senoidal), contra uma saída de planta simulada de forma independente, a variante `double` dá:

$
\text{erro máximo absoluto} = 0{,}0\,\mathrm{V} \quad \text{(nas 2.000 amostras)}.
$

O valor medido é exatamente zero — não apenas pequeno —, porque Python (NumPy) e C sem otimizações agressivas (`gcc -O2`, sem `-ffast-math`) seguem a mesma aritmética IEEE-754 de dupla precisão, na mesma ordem de operações. O critério teórico não exige zero: a expectativa correta é equivalência **na ordem do épsilon de máquina**, $\epsilon\approx2{,}22\times10^{-16}$, já que diferenças de associatividade entre compiladores podem, legitimamente, introduzir erro de poucas unidades na última casa decimal. Um erro de $10^{-8}$ ou maior já apontaria para diferença real de fórmula, não de arredondamento.

A variante Q16.16, comparada contra o mesmo modelo `double`, dá:

$
\text{erro máximo absoluto} = 0{,}01586\,\mathrm{V}, \qquad \text{erro médio absoluto} = 0{,}00271\,\mathrm{V}, \qquad \text{erro RMS} = 0{,}00540\,\mathrm{V},
$

pior caso na amostra 1.900 — seis ordens de grandeza maior que a variante `double`, mas não é bug: é o custo esperado do ponto fixo, consistente com os erros de quantização da Aula 13 propagados pela recorrência. Frente a 24 V de fundo de escala, 15,86 mV correspondem a $0{,}066\,\%$ — margem que a equipe decide, com o número em mãos, se atende REQ-CTRL-001.

> **Recurso visual 5 — Duas ordens de grandeza de erro.** Gráfico de barras em escala logarítmica comparando o erro máximo absoluto double (praticamente zero) e Q16.16 (0,01586 V), com marca de referência no épsilon de máquina.
> *Texto alternativo:* gráfico de barras em escala logarítmica mostra o erro máximo absoluto entre modelo e código gerado para as variantes double e ponto fixo Q16.16, com diferença de seis ordens de grandeza entre elas.

### Demonstração obrigatória: o bug real e sua correção

Para tornar concreto que "erro maior indica bug, não ruído", esta aula injeta deliberadamente um defeito plausível: uma cópia do modelo em que o anti-windup (REQ-CTRL-003) foi removido por engano. Comparada contra o `SILController` correto, sobre as mesmas 2.000 amostras:

$
\text{erro máximo absoluto} = 12{,}61\,\mathrm{V}, \qquad \text{erro médio absoluto} = 1{,}85\,\mathrm{V},
$

cerca de $5{,}7\times10^{16}$ vezes o épsilon de máquina. Um erro dessa magnitude, muitos múltiplos do fundo de escala do atuador, nunca é explicável por arredondamento — é assinatura inconfundível de divergência de lógica, exatamente o que um pipeline de CI precisa capturar antes que o código chegue a um alvo real.

### Testes de regressão e integração contínua

A comparação vira teste ao ser encapsulada em asserção com tolerância: um teste pytest chama `compare_model_vs_code` e falha se `erro_maximo_abs` ultrapassar um limiar — $10^{-9}\,\mathrm{V}$ para `double`, compatível com a Aula 13 para Q16.16. A cada mudança no modelo, esse teste garante que a equivalência não se perde silenciosamente antes de o código chegar à Aula 15.

> **Recurso visual 6 — Pipeline de CI da equivalência SIL.** Fluxo: mudança no modelo → geração → compilação → `compare_model_vs_code` → decisão (dentro da tolerância: segue; acima: build falha).
> *Texto alternativo:* fluxograma mostra uma mudança no modelo atravessando geração de código, compilação e comparação automática; erro acima da tolerância falha o pipeline de integração contínua.

### Laboratório da aula

Em `projeto_nexabot/aula_14/`, `01_compila_sil.py` compila e carrega o C via `ctypes`. `02_equivalencia.py` compara 6.000 amostras e mede erro nulo em `double` e erro máximo de cerca de $5{,}48\times10^{-2}\,\mathrm{V}$ em Q16.16. `03_regressao.py` usa Hypothesis em 25 combinações de ganhos, sem falhas. `04_ci.py` valida o workflow `.github/workflows/mbd-ci.yml`. No desafio `05_desafio.py`, um sinal incorreto no anti-windup gera erro máximo de $48\,\mathrm{V}$ após dessaturação, embora permaneça invisível no cenário que nunca satura.

### Atividade prática

Meça a equivalência do código gerado para três combinações de ganhos da Aula 6 (Ziegler-Nichols clássico, variante sem sobressinal, ajuste manual). Reporte o erro máximo em `double` e Q16.16 e diga se o erro Q16.16 é compatível com os erros de quantização de $T_s$, $\tau_f$ e $K_d$ da Aula 13 ou desproporcionalmente maior.

### Síntese da aula

- Equivalência entre modelo e código gerado não se declara: é um número medido, amostra a amostra, sobre a mesma sequência de entradas.
- SIL executa o binário real do alvo, compilado para a máquina de desenvolvimento, dentro do mesmo processo do modelo, sem hardware.
- Na variante double, o erro esperado fica na ordem do épsilon de máquina ($\approx2{,}22\times10^{-16}$); o valor medido foi exatamente zero.
- Na variante Q16.16, um erro seis ordens de grandeza maior é esperado e aceitável, se consistente com a quantização da Aula 13.
- Um erro muitas ordens acima do esperado — como os 12,61 V com o anti-windup removido — é assinatura inequívoca de bug, não de ruído.
- Testes de regressão com tolerância definida, em CI, impedem que a equivalência se perca sem que ninguém perceba.

### Roteiro da Videoaula 14 — "Doze vírgula seis um volts de diferença"

O roteiro falado completo, com narração pronta para gravação, marcações de tela e comandos literais, está no arquivo `roteiros_20min.md` desta unidade, usando a introdução deliberada do bug de anti-windup como demonstração central de equivalência quebrada e corrigida.

### Referências da aula

- IEEE. *IEEE Std 1012-2016: IEEE Standard for System, Software, and Hardware Verification and Validation*. New York: IEEE, 2017.
- BROEKMAN, Bart; NOTENBOOM, Edwin. *Testing Embedded Software*. London: Addison-Wesley, 2003.
- WHALEN, Michael W.; HEIMDAHL, Mats P. E. On the requirements of high-integrity code generation. In: IEEE INTERNATIONAL SYMPOSIUM ON HIGH-ASSURANCE SYSTEMS ENGINEERING, 4., 1999, Washington, D.C. *Proceedings [...]*. Washington, D.C.: IEEE, 1999. p. 217-224. DOI: 10.1109/HASE.1999.809495.

## Aula 15 — Hardware-in-the-loop, tempo real e jitter

### Situação-problema: o mesmo código, um resultado diferente

O código C aprovado na Aula 14 foi verificado no mesmo processo Python, sem restrição de tempo: cada `.step()` devolve o controle imediatamente. Um colega pergunta: "já podemos confiar que isso vai rodar no ESP32?". A resposta é não — nada testou o controlador como processo separado, competindo por CPU, sujeito a um firmware que não garante ciclos de exatamente 5 ms. SIL prova equivalência numérica; não prova que o sistema respeita seu prazo. Esta aula introduz *hardware-in-the-loop* (HIL): o tempo deixa de ser variável implícita e vira restrição medida em milissegundos.

### Hardware-in-the-loop: planta em tempo real, controlador no alvo

Em `nexabot/hil.py`, a planta roda em Python por Runge-Kutta de quarta ordem, mas em **tempo real**: o processo aguarda o tempo necessário para que o período respeite $T_s=5\,\mathrm{ms}$ de parede a parede. O controlador roda como **alvo** separado, acessível só por comunicação — como um microcontrolador real por UART. Dois back-ends implementam esse alvo com a mesma interface: `LoopbackTarget` compila o C da Aula 13 com um laço de protocolo (`main_loopback.c`) e roda como subprocesso local por `stdin`/`stdout` — o que funciona de verdade neste ambiente sem hardware. `SerialTarget` fala o mesmo protocolo por porta serial real, para quem tem ESP32 via PlatformIO.

> **Recurso visual 7 — Arquitetura HIL: planta em tempo real, alvo separado.** Diagrama com o processo host rodando a planta por Runge-Kutta a cada $T_s=5\,\mathrm{ms}$ de parede a parede, comunicando por `stdin`/`stdout` (ou UART) com um alvo externo executando o C gerado — `LoopbackTarget` local ou `SerialTarget`/ESP32.
> *Texto alternativo:* diagrama mostra a planta simulada em tempo real no processo host trocando mensagens de protocolo com um alvo externo — subprocesso local ou microcontrolador real — que executa o controlador C gerado.

### O protocolo de linha

O protocolo é simples: cada linha é um comando ASCII terminado em `\n`. `STEP <r> <y>` devolve `U <u>`; `RESET` zera o estado (obrigatório ao sair de FALHA, REQ-SAFE-004) e devolve `OK`; `QUIT` encerra o processo. Um campo opcional, `<delay_ms>`, pede ao alvo que atrase a resposta — para testar como o sistema reage a um alvo lento.

> **Recurso visual 8 — Protocolo de linha HIL.** Diagrama de sequência entre host (planta Python) e alvo (controlador C) com as mensagens `STEP`/`RESET`/`QUIT` e respostas `U`/`OK`, repetindo-se sem alteração entre `LoopbackTarget` e `SerialTarget`.
> *Texto alternativo:* diagrama de sequência mostra a troca de mensagens STEP, RESET e QUIT entre a planta em Python e o controlador C, válida tanto por stdin/stdout local quanto por porta serial real.

### Jitter e latência: as duas métricas que decidem confiabilidade

*Latência* é o tempo entre o host enviar `STEP` e receber `U <u>`. *Jitter* é a variação do período efetivo do laço em torno do nominal $T_s$ — quanto cada ciclo dura a mais ou a menos dos 5 ms esperados. Um sistema pode ter latência baixa e jitter alto, se essa latência variar de forma imprevisível de ciclo a ciclo; é essa variação, não o valor médio, que compromete a estabilidade de um controlador discreto, cuja análise (Aula 7) assume $T_s$ constante.

### Exemplo numérico: jitter medido sobre um período de 5 ms

Rodando `run_closed_loop_hil` com `LoopbackTarget` por 2 s (400 amostras a $T_s=5\,\mathrm{ms}$), em tempo real, neste ambiente de desenvolvimento — um sistema operacional de uso geral, sem garantias de tempo real —, as métricas medidas foram:

$
\text{período médio} = 5{,}123\,\mathrm{ms}, \qquad \text{jitter pico a pico} = 0{,}909\,\mathrm{ms}, \qquad \text{desvio-padrão do jitter} = 0{,}133\,\mathrm{ms},
$

$
\text{latência média} = 0{,}108\,\mathrm{ms}, \qquad \text{latência p95} = 0{,}287\,\mathrm{ms}, \qquad \text{latência máxima} = 2{,}002\,\mathrm{ms}.
$

O jitter pico a pico consome $18{,}2\,\%$ do período nominal — fração nada desprezível, mesmo sem falha alguma, só pela natureza de um SO de uso geral, sem escalonamento determinístico. A latência máxima, 2,0 ms, corresponde a $40\,\%$ do período: um único ciclo lento consumiria quase metade do orçamento antes do próximo passo. Em um alvo real-time dedicado esses números tendem a ser menores, mas o raciocínio é o mesmo.

> **Recurso visual 9 — Distribuição do jitter sobre 400 ciclos.** Histograma do período efetivo do laço em torno de 5 ms, com faixa sombreada indicando a fração consumida pelo jitter pico a pico.
> *Texto alternativo:* histograma da duração de 400 ciclos de controle mostra a maioria concentrada perto de 5 ms, com dispersão de até 0,909 ms entre o ciclo mais curto e o mais longo.

### Watchdog: o que acontece quando o alvo não responde

Um alvo que atrasa sua resposta não pode fazer o laço host esperar indefinidamente — um firmware travado poderia nunca responder. A classe `Watchdog` executa `target.step(...)` em uma thread auxiliar, sob um prazo (`deadline_s`); se o alvo não responde a tempo, devolve o comando seguro (tensão zero) e sinaliza o estouro.

Testado com prazo de 10 ms e chamada normal, o resultado foi `u = 24,0 V`, sem estouro. Injetando atraso deliberado de 50 ms — cinco vezes o prazo —, o resultado passou a `u = 0,0 V`, com `estourou = True`. É o mesmo raciocínio de REQ-SAFE-004: quando o tempo é prazo físico, a resposta segura diante de seu descumprimento é assumir o pior caso — zerar o comando —, não esperar mais.

> **Recurso visual 10 — Watchdog: o caminho normal e o caminho do estouro.** Diagrama de dois trilhos paralelos sobre a mesma linha de tempo. No trilho superior, o alvo responde dentro do prazo de 10 ms e o comando de 24,0 V segue para a planta. No trilho inferior, a resposta do alvo atrasa 50 ms; ao cruzar a marca do prazo, o trilho muda de cor e o comando entregue passa a 0,0 V, com a marcação `estourou = True`. Uma legenda registra que o valor seguro é escolhido por projeto, não devolvido pelo alvo.
> *Texto alternativo:* diagrama compara dois cenários do watchdog na mesma linha de tempo: no primeiro, o alvo responde dentro do prazo e o comando de vinte e quatro volts é aplicado; no segundo, o alvo atrasa além do prazo e o watchdog substitui o comando por zero volt, sinalizando estouro.

### O caminho para o ESP32 real

Para quem tem um ESP32 por USB, o mesmo `run_closed_loop_hil` funciona sem alteração ao trocar `LoopbackTarget` por `SerialTarget(port="/dev/ttyUSB0")` (protocolo idêntico, firmware gravado via `pio run -t upload`); para quem não tem placa, o *loopback* garante a demonstração completa sem hardware — a diferença entre os dois está só no transporte, nunca na lógica de controle.

### Pausa para reflexão

Considere: uma equipe decide que, como o SIL da Aula 14 já provou equivalência numérica exata, não é necessário medir jitter e latência antes de embarcar o controlador em produção.

Reflita:

1. Que tipo de defeito o SIL, por construção, nunca poderia revelar, mesmo com erro de equivalência igual a zero?
2. Por que um controlador matematicamente correto ainda pode causar instabilidade real se o período efetivo variar significativamente em torno de $T_s$?
3. O watchdog zera o torque diante de atraso de 50 ms com prazo de 10 ms. Que consequência teria sua ausência num cenário de obstáculo, à luz do REQ-SAFE-006?
4. Que evidência desta aula você apresentaria a um revisor para justificar um teste em bancada com hardware real?

Uma resposta madura reconhece que equivalência numérica (Aula 14) e comportamento temporal (Aula 15) são propriedades independentes: um controlador numericamente perfeito ainda pode falhar em produção se o alvo não responder dentro do prazo que a física exige.

### Laboratório da aula

Em `projeto_nexabot/aula_15/`, `01_loopback_hil.py` executa a malha fechada em processo separado e imprime estatísticas reais de período, jitter e latência. `02_jitter.py` repete a medição em três durações e compara o desvio-padrão com o critério de $10\%$ de $T_s$. `03_watchdog_real.py` contrasta resposta normal com um alvo deliberadamente travado por 200 ms: o watchdog de 15 ms devolve comando seguro de $0\,\mathrm{V}$ e permite reconexão. O desafio `04_desafio.py` mede o menor período aceito no ambiente corrente; o resultado depende da carga e não deve ser tratado como especificação universal.

### Atividade prática

Rode `run_closed_loop_hil` por 5 s com `LoopbackTarget` e registre período médio, jitter pico a pico e latência p95. Configure um `Watchdog` com prazo $1{,}5\times T_s$ (7,5 ms) e injete atrasos de 0 a 20 ms em passos de 2 ms, registrando em que ponto o watchdog estoura. Compare com a latência máxima medida e discuta a margem frente ao jitter observado.

### Síntese da aula

- SIL prova equivalência numérica; HIL prova que o sistema respeita seu prazo — propriedades independentes, nenhuma substitui a outra.
- O protocolo STEP/RESET/QUIT é idêntico entre loopback (sem hardware) e alvo serial real (ESP32/PlatformIO), permitindo demonstrar sem placa.
- Jitter mede a variação do período do laço; latência mede o tempo de resposta de uma chamada ao alvo — ambos em milissegundos sobre um período nominal de 5 ms.
- O jitter pico a pico medido (0,909 ms) consumiu cerca de 18% do período de amostragem, mesmo sem falha simulada.
- Um watchdog com prazo definido devolve comando seguro (torque zero) quando o alvo não responde a tempo, sem esperar indefinidamente por um alvo travado.
- Quando o tempo deixa de ser eixo de gráfico e vira prazo físico, a resposta correta a um estouro é sempre assumir o pior caso, não esperar mais.

### Roteiro da Videoaula 15 — "Cinco milissegundos, de verdade"

O roteiro falado completo, com narração pronta para gravação, marcações de tela e comandos literais, está no arquivo `roteiros_20min.md` desta unidade, usando a demonstração do watchdog sob atraso deliberado como núcleo da explicação de prazo real.

### Referências da aula

- KOPETZ, Hermann. *Real-Time Systems: Design Principles for Distributed Embedded Applications*. 2. ed. New York: Springer, 2011.
- LEE, Edward Ashford; SESHIA, Sanjit A. *Introduction to Embedded Systems: A Cyber-Physical Systems Approach*. 2. ed. Cambridge: MIT Press, 2017.
- BROEKMAN, Bart; NOTENBOOM, Edwin. *Testing Embedded Software*. London: Addison-Wesley, 2003.

## Aula 16 — Rastreabilidade, certificação e fechamento

### Situação-problema: "isso está certificado?"

Ao final de uma apresentação do NexaBot a um cliente de robótica industrial, alguém pergunta: "esse pipeline gera evidências suficientes para certificar o robô conforme a ISO 26262?". A resposta errada mais comum é otimista demais: listar tudo o que foi construído e concluir que isso "é" certificação. Não é. Esta aula final constrói o vocabulário exato para responder com precisão: o que este pipeline produz é evidência; certificação é outra coisa, e depende de elementos que nenhuma ferramenta, sozinha, fornece.

### DO-178C e ISO 26262: objetivos e níveis de criticidade

A **DO-178C** (*Software Considerations in Airborne Systems and Equipment Certification*) é o padrão para certificação de software embarcado em aviônica civil, publicado pela RTCA. Define cinco **níveis de garantia de projeto** (DAL), de A a E, conforme a gravidade da falha: A é catastrófica (perda da aeronave), E é sem efeito operacional relevante. Quanto mais crítico o nível, mais a norma exige — cobertura estrutural de código, independência entre desenvolvimento e verificação, rastreabilidade obrigatória entre requisitos, projeto, código e testes.

A **ISO 26262** cumpre papel equivalente na indústria automotiva, com quatro **Níveis de Integridade de Segurança Automotiva** (ASIL), de A a D, proporcionais a severidade, exposição e controlabilidade do risco. Como a DO-178C, exige rastreabilidade bidirecional — exatamente a estrutura que a matriz desta aula constrói para o NexaBot.

### Qualificação de ferramenta: a questão central ao usar ferramentas abertas

Ambas as normas tratam da confiança em ferramentas de desenvolvimento. A necessidade e o nível de **qualificação de ferramenta** dependem do uso: do impacto de um possível erro e da possibilidade de esse erro ser detectado por verificação posterior. Se um gerador substitui uma verificação e sua saída segue ao produto sem controle independente suficiente, pode ser necessário qualificá-lo; outra estratégia pode introduzir verificação adequada da saída. A licença não decide isso: SymPy, Jinja2, GCC e Python não vêm automaticamente qualificados para este processo, assim como uma ferramenta comercial comum também não. A análise deve ser feita e documentada para o uso concreto.

> **Recurso visual 11 — De onde vem a confiança em cada etapa do pipeline.** Diagrama do pipeline (modelo → derivação simbólica → geração de código → compilação → SIL → HIL) com uma marca em cada etapa indicando se ela produz evidência de correção do *conteúdo* gerado ou depende de confiança não qualificada na *ferramenta* que a executa.
> *Texto alternativo:* diagrama do pipeline de geração de código do NexaBot com anotações distinguindo, em cada etapa, entre evidência de correção produzida e confiança depositada, sem qualificação formal, na ferramenta utilizada.

### O que o pipeline desta disciplina produz — e o que ele não produz

O pipeline das quatro unidades produz, com evidência reproduzível: **modelo versionado** em Git; **propriedades formais verificadas** exaustivamente (Unidade 3); **suíte de testes gerada** do modelo, com cobertura medida; **código gerado com rastreabilidade** automática, ligado por hash a parâmetros exatos; **equivalência numérica medida**; e **CI** que falha, reprodutivelmente, quando qualquer garantia se rompe.

O que **não produz**, e um processo real exigiria conforme o domínio: **independência de verificação**; análise e, quando aplicável, **qualificação formal das ferramentas**; **WCET** no alvo real — o jitter da Aula 15 é amostragem empírica, não prova de limite superior; e a avaliação da autoridade ou organismo competente sobre a suficiência das evidências.

> **Recurso visual 12 — Duas colunas: produz e não produz.** Cartaz de duas colunas lado a lado — "o pipeline produz" (seis itens com ícone de evidência) e "o pipeline não produz" (quatro itens com ícone de lacuna) — como resumo visual desta aula.
> *Texto alternativo:* cartaz de duas colunas lista, à esquerda, seis evidências produzidas pelo pipeline da disciplina, e à direita, quatro elementos de um processo real de certificação que o pipeline não substitui.

### A matriz de rastreabilidade: percorrendo uma linha inteira

A matriz requisito → modelo → código gerado → teste do NexaBot é produzida por varredura estática dos identificadores `REQ-*` em todos os arquivos Python do projeto, refletindo o estado do repositório no momento em que é gerada. Na versão validada, a varredura lê 91 arquivos e encontra 14 requisitos. Ela também expõe uma lacuna verdadeira: REQ-SAFE-007 tem modelo/descrição, mas nenhuma evidência de teste.

Percorrer a linha de **REQ-SAFE-007** — velocidade linear não superior a $1{,}20\,\mathrm{m/s}$ no domínio operacional — revela a lacuna central. A descrição existe em `nexabot/requisitos.py`, mas o supervisor discreto observa apenas `parado()`, não a trajetória contínua. A coluna de código gerado está vazia, porque o gerador cobre o PID, e a de teste também: nenhuma evidência atual integra planta, controlador e supervisor sobre um domínio definido. Em contraste, REQ-SAFE-006 possui três evidências de teste da Aula 11; portanto, não pode ser usado como exemplo de requisito sem teste.

Fechar REQ-SAFE-007 exigiria definir o domínio operacional, executar o modelo integrado e declarar um critério de cobertura. Testes baseados em propriedades podem encontrar contraexemplos, mas ausência de falha em uma amostra não equivale a prova universal.

> **Recurso visual 13 — Linha de rastreabilidade de REQ-SAFE-007.** Diagrama horizontal com quatro células (Requisito → Modelo → Código gerado → Teste), a descrição preenchida e as evidências ausentes destacadas como lacunas.
> *Texto alternativo:* diagrama mostra o requisito de velocidade ligado à descrição formal, sem código gerado nem teste contínuo no domínio operacional.

### Casos de uso: automotivo, aeroespacial e robótica industrial

No **automotivo**, um requisito análogo pode ser verificado por autômatos temporizados ou análise de WCET, num processo ISO 26262 com ASIL derivado da HARA. No **aeroespacial**, sob DO-178C, rastreabilidade é insumo de auditoria, e planos, independência e confiança nas ferramentas seguem critérios do nível de software e do uso concreto. Na **robótica industrial**, mais próxima do NexaBot, normas como ISO 10218 exigem evidência de desempenho de parada conforme a aplicação. Os processos não são intercambiáveis, mas todos exigem que limites relevantes sejam medidos e documentados.

### Fechamento da disciplina

Esta é a última aula de *Model-Based Design for Cyber-Physical Systems*. Na Aula 1, o NexaBot virou modelo identificado. A Unidade 2 fechou a malha com PID, amostragem justificada, anti-windup e co-simulação. A Unidade 3 provou REQ-SAFE-001 a 006 no escopo dos modelos adotados e deixou REQ-SAFE-007 aberto. A Unidade 4 gerou código, mediu equivalência e comportamento temporal e produziu uma matriz que mostra evidências e lacunas.

Essa progressão — modelar, controlar, provar, embarcar com evidência — sustenta qualquer sistema ciberfísico confiável, de um satélite a um braço robótico industrial. O que muda entre domínios é o nível de criticidade e o processo de certificação — nunca a exigência de que uma afirmação só vale quando sustentada por evidência reproduzível.

Fica um convite para o trabalho PBL: aplique a um sistema ciberfísico novo o mesmo percurso de quatro camadas — modelo, controle, verificação formal, código com rastreabilidade — com o rigor desta aula: não "eu acho que funciona", mas "aqui está o número que mostra isso, e o que ele não prova". Essa é a competência central de quem projeta sistemas ciberfísicos com abordagem baseada em modelos.

### Laboratório da aula

Em `projeto_nexabot/aula_16/`, `01_matriz_rastreabilidade.py` regenera `rastreabilidade.md` e imprime 91 arquivos lidos, 14 requisitos e a lacuna de teste de REQ-SAFE-007. `02_evidencias.py` relaciona as evidências produzidas aos objetivos de DO-178C e ISO 26262 e explicita o que falta. `03_desafio.py` lê a matriz e pede uma proposta verificável para a lacuna real encontrada, sem fingir que o requisito contínuo foi provado.

### Atividade prática

Use REQ-SAFE-007 e proponha uma estratégia de fechamento: domínio operacional, estímulos, oráculo, cobertura e critério de aceitação. Diferencie um teste capaz de encontrar contraexemplos de um argumento de garantia suficiente para a aplicação.

### Síntese da aula

- DO-178C (aviônica) e ISO 26262 (automotiva) definem níveis de criticidade (DAL A-E; ASIL A-D) que determinam o rigor de verificação e rastreabilidade exigido.
- Confiança em ferramentas depende do uso, do impacto de erro e da detecção posterior, não da licença aberta ou comercial.
- O pipeline produz seis evidências concretas, mas não produz sozinho independência, análise completa de ferramentas, WCET no alvo ou aprovação externa.
- A matriz validada relaciona 14 requisitos em 91 arquivos Python e mostra uma lacuna explícita de teste para REQ-SAFE-007.
- A linha de REQ-SAFE-007 explicita a ausência de teste da trajetória contínua; REQ-SAFE-006, em contraste, possui evidências da Aula 11.
- Certificação e garantia são processos; nenhum pipeline técnico os substitui sozinho.
- A trajetória das quatro unidades — modelar, controlar, provar, embarcar com evidência — é a competência transferível a qualquer sistema ciberfísico, independente da ferramenta em uso.

### Roteiro da Videoaula 16 — "O que este pipeline prova, e o que ele não prova"

O roteiro falado completo está em `roteiros_20min.md`, encerrando a disciplina com a linha de REQ-SAFE-007 e a retrospectiva das quatro unidades.

### Referências da aula

- RTCA. *DO-178C: Software Considerations in Airborne Systems and Equipment Certification*. Washington, D.C.: RTCA, 2011.
- ISO. *ISO 26262: Road Vehicles — Functional Safety*. Geneva: International Organization for Standardization, 2018.
- WHALEN, Michael W.; HEIMDAHL, Mats P. E. On the requirements of high-integrity code generation. In: IEEE INTERNATIONAL SYMPOSIUM ON HIGH-ASSURANCE SYSTEMS ENGINEERING, 4., 1999, Washington, D.C. *Proceedings [...]*. Washington, D.C.: IEEE, 1999. p. 217-224. DOI: 10.1109/HASE.1999.809495.

## Atividades, síntese e material complementar

### Quiz não avaliativo

**Questão 1.** Um estagiário, sob pressão de prazo, corrige diretamente um coeficiente que considera arredondado de forma indevida em `pid_controller.c` — o arquivo gerado pela Aula 13 —, sem alterar `DiscretePID` nem regenerar o arquivo. Do ponto de vista da rastreabilidade modelo-código construída nesta unidade, essa decisão é:

a. Correta, desde que documente a alteração em comentário no próprio `.c`, junto ao bloco de rastreabilidade.
b. Correta, pois o hash SHA-256 é recalculado automaticamente ao salvar o `.c`, preservando a rastreabilidade após edição manual.
c. Incorreta, mas só porque o gcc rejeitaria compilar um arquivo editado manualmente após gerado.
*d. Incorreta, pois o arquivo gerado é artefato derivado: a próxima geração sobrescreve silenciosamente a edição, e o hash passa a descrever parâmetros que não correspondem mais ao arquivo real.
e. Incorreta, apenas porque editar C manualmente é mais lento do que corrigir o modelo e regerar.

*Feedback conceitual:* o arquivo gerado não tem existência independente do modelo — é, por definição, um artefato derivado. Uma edição manual não é preservada pela rastreabilidade, é anulada por ela: na próxima geração, o arquivo é substituído sem aviso, e, enquanto a edição persistir, o bloco de rastreabilidade (hash, requisitos, versão) descreve um comportamento que não corresponde mais ao arquivo real, comprometendo a cadeia requisito → modelo → código → teste. A correção correta é sempre no modelo, seguida de regeneração.

**Questão 2.** Após concluir o pipeline de geração de código, equivalência SIL, testes HIL e matriz de rastreabilidade construído ao longo desta unidade, uma equipe declara, em uma proposta comercial: "nosso processo de desenvolvimento está pronto para certificação DO-178C, porque geramos evidência completa de rastreabilidade requisito-modelo-código-teste". Essa afirmação é:

a. Correta, pois rastreabilidade completa entre requisito, modelo, código e teste é, por si só, o único critério da DO-178C para certificação.
b. Correta, desde que o código gerado tenha sido compilado com compilador amplamente usado na indústria, como o GCC.
c. Incorreta, pois a DO-178C não reconhece rastreabilidade automática por varredura estática como evidência válida em nenhuma circunstância.
*d. Incorreta, pois certificação exige, além de rastreabilidade, independência entre quem desenvolve e verifica, qualificação formal das ferramentas e aprovação por autoridade certificadora — nenhum desses três é produzido automaticamente por um pipeline técnico.
e. Incorreta, apenas porque a matriz cobre menos de cem por cento dos requisitos do sistema.

*Feedback conceitual:* rastreabilidade, verificação formal, equivalência numérica e testes gerados são evidências valiosas, mas são insumos de um processo de garantia, não o processo em si. Um contexto real ainda exige independência adequada, análise de confiança e eventual qualificação das ferramentas, dados de ciclo de vida e avaliação pela autoridade ou organismo competente.

### Síntese da unidade

- Código embarcado gerado automaticamente elimina erros de transcrição manual e é, por definição, artefato derivado — nunca editado à mão, sempre regenerado a partir do modelo.
- Um bloco de rastreabilidade no cabeçalho (requisitos, versão do modelo, hash SHA-256, data, advertência) liga qualquer binário em produção ao modelo exato que o originou.
- Q16.16 representa reais como inteiros de 32 bits com resolução $2^{-16}\approx1{,}526\times10^{-5}$; parâmetros não múltiplos exatos sofrem quantização mensurável.
- Equivalência entre modelo e código gerado é número medido, não alegação: na variante double, erro esperado na ordem do épsilon de máquina ($\approx2{,}22\times10^{-16}$); erro maior é assinatura de bug.
- SIL verifica equivalência sem hardware; HIL verifica jitter e latência de um alvo real ou emulado, sob restrições de tempo genuínas.
- Um watchdog com prazo definido protege o sistema quando o alvo não responde a tempo, devolvendo comando seguro em vez de esperar indefinidamente.
- DO-178C e ISO 26262 exigem, além de rastreabilidade, independência de verificação e qualificação formal de ferramenta — questão central ao adotar pilha aberta em sistemas críticos.
- Um pipeline técnico produz evidência; certificação é processo organizacional, e essa distinção é parte inseparável da competência de projetar sistemas ciberfísicos confiáveis.

### Material complementar

#### Direto da Fonte

**Texto provocativo:** Esta unidade insistiu que um sistema ciberfísico embarcado vive sob restrições de tempo que um modelo Python, livre no processador de um notebook, não sente. Os capítulos indicados tratam exatamente da fronteira entre "o controlador está correto" e "o controlador responde a tempo" — a distinção que sustentou toda a Aula 15.

**Referência:** LEE, Edward Ashford; SESHIA, Sanjit A. *Introduction to Embedded Systems: A Cyber-Physical Systems Approach*. 2. ed. Cambridge: MIT Press, 2017. Capítulos sobre execução em tempo real e geração de código para sistemas embarcados.

**Link de acesso:** disponível na Biblioteca Virtual da instituição.

**Aula indicada:** Aula 13, após "Ponto flutuante contra ponto fixo Q16.16".

#### Para Mergulhar no Assunto

**Texto provocativo:** Se você quer ver, com exemplos reais de projetos que deram errado, por que "o código compilou" nunca foi sinônimo de "o código está correto", este é o livro. Escrito por um engenheiro que passou décadas revisando firmware crítico, trata com o mesmo tom direto desta disciplina de geração de código e limites reais das ferramentas de verificação.

**Referência:** KOOPMAN, Philip. *Better Embedded System Software*. Pittsburgh: Drumnadrochit Education, 2010.

**Link de acesso:** <https://betterembsw.blogspot.com/>. Acesso em: 29 ago. 2026.

**Aula indicada:** Aula 16, após "O que o pipeline desta disciplina produz — e o que ele não produz".

#### Podcast

**Texto provocativo:** Esta palestra apresenta um caso concreto da Boeing para qualificar uma ferramenta aberta de cobertura estrutural segundo DO-330. Ela mostra que código aberto não é proibido nem automaticamente aceito: o uso exige requisitos, validação e evidência apropriados.

**Referência:** PARK, Minji; KIM, Seojin. *DO-330 Qualification of Enhanced LLVM Structural Coverage Tool*. [S. l.]: The Linux Foundation, 2025. 1 vídeo (31 min). Publicado no YouTube.

**Link de acesso:** <https://www.youtube.com/watch?v=0JQLazypIHQ>. Acesso em: 29 ago. 2026.

**Trecho obrigatório:** 00:00–20:00, cobrindo motivação, requisitos do DO-330 e estratégia de qualificação do `llvm-cov` aprimorado.

**Aula indicada:** Aula 16, após "Qualificação de ferramenta: a questão central ao usar ferramentas abertas".

#### Artigo científico

**Texto provocativo:** Antes de gerar um `.c` a partir de um modelo, vale entender por que a verificação formal trata geração de código de alta integridade como problema à parte — não bônus automático de "modelar corretamente". Este artigo, de dois autores centrais na área, formaliza exatamente essas exigências.

**Referência:** WHALEN, Michael W.; HEIMDAHL, Mats P. E. On the requirements of high-integrity code generation. In: IEEE INTERNATIONAL SYMPOSIUM ON HIGH-ASSURANCE SYSTEMS ENGINEERING, 4., 1999, Washington, D.C. *Proceedings [...]*. Washington, D.C.: IEEE, 1999. p. 217-224. DOI: 10.1109/HASE.1999.809495.

**Link de acesso:** <https://doi.org/10.1109/HASE.1999.809495>. Acesso em: 29 ago. 2026.

**Aula indicada:** Aula 13, antes da atividade prática de geração de código.

## Referências da unidade

BROEKMAN, Bart; NOTENBOOM, Edwin. *Testing Embedded Software*. London: Addison-Wesley, 2003.

IEEE. *IEEE Std 1012-2016: IEEE Standard for System, Software, and Hardware Verification and Validation*. New York: IEEE, 2017.

ISO. *ISO 26262: Road Vehicles — Functional Safety*. Geneva: International Organization for Standardization, 2018.

KOOPMAN, Philip. *Better Embedded System Software*. Pittsburgh: Drumnadrochit Education, 2010.

KOPETZ, Hermann. *Real-Time Systems: Design Principles for Distributed Embedded Applications*. 2. ed. New York: Springer, 2011.

LEE, Edward Ashford; SESHIA, Sanjit A. *Introduction to Embedded Systems: A Cyber-Physical Systems Approach*. 2. ed. Cambridge: MIT Press, 2017.

RTCA. *DO-178C: Software Considerations in Airborne Systems and Equipment Certification*. Washington, D.C.: RTCA, 2011.

WHALEN, Michael W.; HEIMDAHL, Mats P. E. On the requirements of high-integrity code generation. In: IEEE INTERNATIONAL SYMPOSIUM ON HIGH-ASSURANCE SYSTEMS ENGINEERING, 4., 1999, Washington, D.C. *Proceedings [...]*. Washington, D.C.: IEEE, 1999. p. 217-224. DOI: 10.1109/HASE.1999.809495.

YATES, Randy. *Fixed-Point Arithmetic: An Introduction*. Digital Signal Labs, Technical Reference, 2013.
