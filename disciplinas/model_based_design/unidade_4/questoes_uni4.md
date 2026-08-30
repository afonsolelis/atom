# Questionário — Unidade 4

Quantidade obrigatória: 40 questões — 20 de asserção-razão (1 a 20) e 20 de interpretação (21 a 40).
Cinco alternativas por questão (a-e); alternativa correta marcada com `*` imediatamente antes da letra.
Distribuição da letra correta: 8 questões para cada uma das letras a, b, c, d, e, no total das 40 questões.

## Questões

### Asserção-razão

**1.** I. O arquivo `pid_controller.c` gerado pela Aula 13 é considerado um artefato derivado, cuja correção deve ocorrer sempre no modelo `DiscretePID`, nunca por edição direta do arquivo `.c`.

PORQUE

II. O compilador gcc detecta automaticamente qualquer edição manual feita no arquivo gerado e impede sua compilação, preservando a rastreabilidade do hash SHA-256 registrado no cabeçalho.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**2.** I. O bloco de rastreabilidade gravado no cabeçalho de `pid_controller.c` liga o arquivo gerado de volta aos requisitos de origem, à versão do modelo e a um hash SHA-256 determinístico dos parâmetros.

PORQUE

II. O hash SHA-256 é calculado a partir dos sete parâmetros do PID (Kp, Ki, Kd, Ts, u_max, tau_f, Kaw) por `compute_params_hash`, de modo que qualquer alteração em um único parâmetro produz um hash inteiramente diferente.

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**3.** I. A representação em ponto fixo Q16.16 utiliza 16 bits inteiros e 16 bits fracionários em uma palavra de 64 bits, o que elimina completamente qualquer erro de arredondamento na conversão de números reais.

PORQUE

II. A multiplicação de dois números em Q16.16 pode ser realizada diretamente em `int32_t`, sem necessidade de acumulador intermediário de maior precisão.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

**4.** I. As equações de diferenças do termo integral e do termo derivativo filtrado usadas no C gerado são obtidas por derivação simbólica com SymPy, a partir da forma contínua do PID, e não digitadas diretamente a partir do contrato de `DiscretePID.step`.

PORQUE

II. O SymPy é uma biblioteca de computação simbólica em Python amplamente utilizada para manipulação algébrica de expressões.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**5.** I. A substituição de Euler para trás, s → (1−z⁻¹)/Ts, utilizada na derivação simbólica das equações do PID discreto, tende a introduzir menos erro de discretização do que a transformação de Tustin, para qualquer valor de Ts.

PORQUE

II. A discretização por Euler para trás corresponde a aproximar cada termo por um único multiply-add, o que é computacionalmente mais barato do que a pré-distorção de frequência exigida pela transformação de Tustin.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**6.** I. A afirmação "o código gerado é equivalente ao modelo" deixa de ser uma alegação e passa a ser evidência técnica somente quando sustentada por uma medição amostra a amostra sobre a mesma sequência de entradas.

PORQUE

II. A função `compare_model_vs_code` executa `DiscretePID` e `SILController` sobre exatamente a mesma sequência (r[k], y[k]), sem que um realimente a saída do outro, e devolve o erro máximo absoluto, médio absoluto e RMS entre as duas saídas.

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**7.** I. Na variante em `double`, um erro de equivalência de zero absoluto entre modelo e código gerado, medido sobre 2.000 amostras, é consistente com a expectativa teórica de equivalência na ordem do épsilon de máquina.

PORQUE

II. Um erro de equivalência de zero absoluto indica necessariamente que o compilador gcc aplicou otimizações agressivas de reordenação de ponto flutuante, como as habilitadas pela flag `-ffast-math`.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**8.** I. Um teste de regressão de equivalência SIL, integrado à esteira de integração contínua, garante formalmente a certificação do software conforme a DO-178C, pois comprova a correspondência total entre modelo e código.

PORQUE

II. A tolerância de 10⁻⁹ V adotada para a variante double no teste de regressão é maior do que o épsilon de máquina, o que torna esse teste incapaz de detectar qualquer bug de lógica introduzido no código gerado.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

**9.** I. A remoção deliberada do anti-windup do modelo, comparada ao `SILController` correto sobre as mesmas 2.000 amostras, produziu um erro máximo absoluto de 12,61 V, muitas ordens de grandeza acima do épsilon de máquina.

PORQUE

II. Os testes de regressão de equivalência do NexaBot utilizam sequências de entrada fixas, compostas por um degrau de 15 rad/s seguido de uma componente senoidal.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**10.** I. Um erro de equivalência de 0,01586 V medido entre a variante Q16.16 e o modelo em double, sobre um fundo de escala de 24 V, invalida obrigatoriamente o uso do ponto fixo no NexaBot, independentemente do requisito de precisão do sistema de controle.

PORQUE

II. Um erro de 0,01586 V frente a 24 V de fundo de escala corresponde a aproximadamente 0,066% da faixa do atuador, e cabe à equipe avaliar se essa margem atende ao requisito REQ-CTRL-001.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**11.** I. A verificação de equivalência numérica realizada em SIL (Aula 14) é suficiente para garantir que o controlador respeitará o período de amostragem de 5 ms quando executado como processo separado no alvo.

PORQUE

II. O jitter do laço de controle é definido como o tempo de ida e volta de uma única chamada `STEP` ao alvo, medido do envio ao recebimento da resposta.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

**12.** I. O jitter pico a pico medido em 400 ciclos de `run_closed_loop_hil` com `LoopbackTarget` foi de 0,909 ms, consumindo cerca de 18,2% do período nominal de 5 ms.

PORQUE

II. O protocolo de linha HIL usa comandos ASCII terminados em `\n`, como `STEP`, `RESET` e `QUIT`.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**13.** I. Um watchdog com prazo definido, ao detectar que o alvo não respondeu dentro do tempo estipulado, deve devolver um comando seguro de tensão zero em vez de aguardar indefinidamente pela resposta.

PORQUE

II. Um alvo que atrasa sua resposta pode estar travado ou com falha de comunicação, e assumir o pior caso — cortar o comando — é a resposta mais segura diante da incerteza sobre seu real estado.

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**14.** I. O protocolo de linha STEP/RESET/QUIT implementado em `LoopbackTarget` e em `SerialTarget` exige alterações na lógica de controle do alvo para funcionar sobre uma porta serial real em vez de `stdin`/`stdout`.

PORQUE

II. A diferença entre `LoopbackTarget` e `SerialTarget` está apenas no meio de transporte das mensagens — subprocesso local por `stdin`/`stdout` ou porta serial real —, nunca na lógica de controle executada no alvo.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**15.** I. Uma latência máxima de 2,002 ms medida em uma chamada individual ao alvo, frente a um período nominal de 5 ms, corresponde a cerca de 40% do orçamento de tempo do ciclo de controle.

PORQUE

II. A latência do laço HIL do NexaBot é medida com relógio de parede do sistema operacional convertido para radianos por segundo, unidade nativa do controlador PID.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**16.** I. A DO-178C e a ISO 26262 definem exatamente os mesmos cinco níveis de criticidade, nomeados igualmente DAL de A a E em ambas as normas.

PORQUE

II. A DO-178C define cinco Níveis de Garantia de Projeto (DAL, de A a E) para aviônica, enquanto a ISO 26262 define quatro Níveis de Integridade de Segurança Automotiva (ASIL, de A a D) para o setor automotivo.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**17.** I. A varredura estática realizada por `nexabot/rastreabilidade.py` para montar a matriz de rastreabilidade do NexaBot constitui, por si só, a qualificação formal exigida pela DO-178C para as ferramentas SymPy, Jinja2 e GCC utilizadas no pipeline.

PORQUE

II. Qualificação de ferramenta, no sentido da DO-178C e da ISO 26262, significa apenas que a ferramenta é amplamente utilizada pela comunidade de desenvolvimento de software livre.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

**18.** I. Nenhuma das ferramentas SymPy, Jinja2, GCC e Python utilizadas no pipeline desta disciplina vem qualificada por uma autoridade certificadora reconhecida, o que não as torna inutilizáveis em contexto certificado, mas significa que qualificá-las, se necessário, seria um projeto à parte.

PORQUE

II. Ferramentas de código aberto são, por definição legal, proibidas de uso em qualquer sistema sob certificação DO-178C ou ISO 26262, independentemente de qualificação.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**19.** I. A matriz de rastreabilidade do NexaBot expõe, na linha de REQ-SAFE-006, uma lacuna honesta: não há código C gerado pelo `codegen` a partir do autômato do supervisor, nem teste automatizado dedicado, distinto da verificação exaustiva.

PORQUE

II. A lógica que zera o torque no supervisor real do NexaBot não passa pela geração de código das Aulas 13-14, que trata apenas do PID discreto, e a análise de REQ-SAFE-006 se apoiou na exploração exaustiva do autômato temporizado, não em um teste automatizado específico.

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**20.** I. O pior caso verificado para REQ-SAFE-006 — 25 ms entre a detecção do obstáculo e o torque zerado — está dentro do limite de 150 ms exigido, considerando atraso de detecção e perda de um ciclo de atuação.

PORQUE

II. A ISO 10218 e a ISO/TS 15066, normas de robótica industrial mais próximas do NexaBot, exigem evidência de tempo de resposta de parada sob um regime menos formalizado do que o aeroespacial.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Interpretação

**21.** Um engenheiro reduz Ki de 40,0 para 39,0 no modelo `DiscretePID` e regenera o código C pela Aula 13. Qual é a consequência mais correta desse procedimento sobre o hash SHA-256 registrado no bloco de rastreabilidade do arquivo gerado?

a. O hash permanece `dc3b95...fa13`, pois pequenas variações de Ki não afetam o cálculo do SHA-256.
*b. O hash muda por completo em relação a `dc3b95...fa13`, pois `compute_params_hash` recalcula a partir do JSON dos sete parâmetros, e qualquer alteração de um único valor produz uma saída totalmente diferente.
c. O hash muda apenas nos últimos dígitos, mantendo o prefixo `dc3b95` igual, pois o SHA-256 preserva similaridade de entrada.
d. O hash não é recalculado automaticamente; é necessário editar manualmente o cabeçalho do arquivo gerado.
e. O hash passa a incluir também o valor antigo de Ki, para permitir rastrear o histórico de alterações.

**22.** Considerando a resolução do formato Q16.16, Δ=2⁻¹⁶≈1,526×10⁻⁵, qual das afirmações abaixo descreve corretamente o comportamento de quantização de τ_f=0,01 s no NexaBot?

a. τ_f é múltiplo exato de Δ, portanto é representado sem qualquer erro de arredondamento em Q16.16.
b. τ_f×2¹⁶ resulta em um número inteiro exato (655,00), eliminando a necessidade de arredondamento.
c. τ_f é arredondado para cima, para 656/65536, com erro de aproximadamente +6,1×10⁻⁶ s.
*d. τ_f×2¹⁶=655,36 é arredondado para 655, resultando em τ_f_fixo=655/65536=0,0099945068359375 s, um erro de aproximadamente −5,493×10⁻⁶ s.
e. τ_f não pode ser representado em Q16.16, pois excede a faixa representável do formato.

**23.** O módulo `nexabot/codegen/derive.py` calcula simbolicamente a diferença entre a recorrência derivada para o termo derivativo filtrado e o contrato de `DiscretePID.step`, levantando um erro (`AssertionError`) caso o resíduo dessa diferença não seja identicamente zero. Qual é a interpretação correta desse comportamento?

*a. O gerador se recusa a produzir um C cuja fórmula matemática discorde algebricamente do modelo de referência, tratando qualquer resíduo não nulo como incompatibilidade entre derivação e contrato.
b. O gerador tolera pequenas diferenças numéricas de até o épsilon de máquina entre a recorrência derivada e o contrato, por se tratar de ponto flutuante.
c. O `AssertionError` só ocorre se o código C gerado falhar ao compilar com gcc.
d. A verificação simbólica substitui a necessidade de qualquer teste posterior de equivalência SIL sobre o código compilado.
e. O resíduo comparado é sempre calculado numericamente, com valores concretos de Kp, Ki e Kd, e não simbolicamente.

**24.** Um colega afirma que a aritmética de ponto fixo Q16.16 é sempre inferior à aritmética em `double` para controle embarcado, e que por isso nunca deveria ser considerada no NexaBot. Com base no conteúdo da Aula 13, essa afirmação é:

a. Correta, pois o formato Q16.16 não é capaz de representar números negativos, exigindo lógica adicional de sinal.
b. Correta, pois microcontroladores com FPU dedicada sempre executam ponto fixo mais devagar do que ponto flutuante.
*c. Incorreta, pois microcontroladores de baixo custo sem unidade de ponto flutuante emulam `double` em software a um custo que pode comprometer o período de amostragem, tornando o ponto fixo uma alternativa viável quando esse custo é proibitivo.
d. Incorreta, apenas porque o ponto fixo elimina totalmente o erro de quantização presente no ponto flutuante.
e. Correta, pois o acumulador de 64 bits exigido pela multiplicação em Q16.16 está indisponível em qualquer microcontrolador de 32 bits.

**25.** Um estudante realiza a atividade prática da Aula 13: aumenta Kp de 2,0 para 2,2 (variação de 10%), regenera o código e converte o novo valor de Kp para Q16.16. Considerando que 2,2×2¹⁶=144.179,2, qual é o resultado correto dessa conversão?

a. Kp_fixo = 144.179, sem erro de arredondamento, pois 2,2 é múltiplo exato de Δ.
b. Kp_fixo = 144.180, com erro de arredondamento nulo.
c. A conversão não é possível, pois 2,2 excede a faixa representável em Q16.16 com 16 bits inteiros.
d. Kp_fixo = 144.179,2, mantendo a parte fracionária para preservar precisão.
*e. Kp_fixo = round(144.179,2) = 144.179, com pequeno erro de arredondamento, pois 2,2 não é múltiplo exato da resolução Δ=2⁻¹⁶.

**26.** Considerando que o épsilon de máquina em `double` é aproximadamente 2,22×10⁻¹⁶ e que o erro máximo absoluto medido entre o modelo e o `SILController` sem anti-windup foi de 12,61 V, qual é a ordem de grandeza aproximada da razão entre esse erro e o épsilon de máquina?

a. 10⁸ vezes.
b. 10¹² vezes.
c. 10¹⁴ vezes.
*d. Aproximadamente 5,7×10¹⁶ vezes, conforme reportado na Aula 14.
e. 10²⁰ vezes.

**27.** Ao obter erro máximo absoluto de exatamente 0,0 V entre o modelo Python e o `SILController` na variante `double`, sobre 2.000 amostras, um estagiário conclui que o resultado é suspeito e que provavelmente há um bug escondendo diferenças reais. Com base no conteúdo da Aula 14, essa conclusão é:

a. Correta, pois nenhuma comparação entre duas implementações independentes pode legitimamente produzir erro zero.
*b. Incorreta, pois o erro zero é explicado pela mesma aritmética IEEE-754 de dupla precisão seguida por NumPy e por gcc -O2 sem -ffast-math, na mesma ordem de operações — um resultado plausível, não suspeito.
c. Incorreta, apenas porque o estagiário deveria ter usado uma tolerância de 10⁻⁹ V em vez de comparar valores exatos.
d. Correta, pois erro zero só ocorreria se o código C não tivesse sido de fato compilado e executado.
e. Incorreta, apenas porque 2.000 amostras são poucas para revelar qualquer divergência real.

**28.** Após obter erro de equivalência de 0,0 V na variante double e comparar o Q16.16 (0,01586 V máximo) com a análise de quantização da Aula 13, uma equipe declara: "provamos que o SIL certifica formalmente a equivalência do nosso controlador para fins de certificação DO-178C." Essa afirmação é:

a. Correta, pois a equivalência numérica medida em SIL é, por definição, o único critério de certificação DO-178C.
b. Correta, desde que o erro medido seja exatamente zero, e não apenas dentro de uma tolerância aceitável.
c. Incorreta, pois o SIL desta disciplina não usa código C real, apenas uma simulação do comportamento esperado.
d. Incorreta, apenas porque a comparação foi feita com 2.000 amostras, e não com a totalidade dos cenários de operação possíveis.
*e. Incorreta, pois SIL produz evidência de equivalência numérica — insumo valioso para certificação —, mas certificação real exige também independência de verificação, qualificação formal de ferramenta e aprovação por autoridade certificadora, nenhuma delas produzida automaticamente pela medição de erro.

**29.** Um teste pytest que encapsula `compare_model_vs_code` falha automaticamente sempre que `erro_maximo_abs` ultrapassa 10⁻⁹ V para a variante double. Se uma futura alteração no template Jinja2 introduzir, por engano, uma troca de operador (por exemplo, subtração no lugar de soma no termo integral), qual é o comportamento esperado desse teste de regressão?

*a. O teste deve falhar, pois a alteração de lógica produziria um erro muitas ordens de grandeza acima de 10⁻⁹ V, semelhante em magnitude ao caso do anti-windup removido.
b. O teste deve passar normalmente, pois erros de template Jinja2 não afetam a equivalência numérica medida por SIL.
c. O teste deve falhar apenas se a alteração também violar a compilação com gcc -O2.
d. O teste deve passar, desde que o erro fique abaixo do épsilon de máquina, mesmo com a troca de operador.
e. O comportamento do teste é indefinido, pois erros de template não são detectáveis por comparação numérica.

**30.** Ao medir a equivalência do código gerado para um novo conjunto de ganhos, cujo τ_f permanece 0,01 s e Ts permanece 0,005 s (os mesmos valores da Aula 13), a equipe obtém, na variante Q16.16, um erro máximo absoluto de 4,2 V — muito acima dos 0,01586 V medidos com os ganhos originais. Qual é a interpretação mais correta desse resultado, à luz da Aula 14?

a. O resultado é esperado, pois qualquer variação nos ganhos do PID aumenta proporcionalmente o erro de quantização de Ts e τ_f.
b. O resultado indica apenas que a nova combinação de ganhos exige um formato Q8.24 em vez de Q16.16.
*c. O resultado é desproporcional ao esperado pela análise de quantização de Ts, τ_f e Kd da Aula 13, e deve ser tratado como possível bug de geração de código ou de configuração dos ganhos, não como consequência normal do ponto fixo.
d. O resultado é esperado, pois qualquer ganho Kp acima de 2,0 satura automaticamente o formato Q16.16.
e. O resultado deve ser ignorado, pois erros acima de 1 V são irrelevantes frente a um fundo de escala de 24 V.

**31.** Em uma nova execução de `run_closed_loop_hil` por 5 s com `LoopbackTarget` (Ts nominal = 5 ms), a equipe mede um jitter pico a pico de 0,75 ms. Qual fração aproximada do período nominal esse jitter representa?

a. 5%.
b. 7,5%.
c. 10%.
d. 12,5%.
*e. 15%.

**32.** Uma equipe decide configurar o `Watchdog` do NexaBot com um prazo (`deadline_s`) igual a três períodos de amostragem (3×Ts), com Ts=5 ms. Qual é o valor correto desse prazo, em milissegundos, e qual seria o comportamento do `Watchdog` diante de um atraso do alvo de 20 ms?

*a. O prazo é de 15 ms; como 20 ms excede esse prazo, o `Watchdog` deve devolver u=0,0 V e sinalizar estouro.
b. O prazo é de 5 ms; como 20 ms excede esse prazo, o `Watchdog` deve aguardar mais um ciclo antes de decidir.
c. O prazo é de 15 ms; como 20 ms excede esse prazo, o `Watchdog` deve devolver o último comando válido registrado, não zero.
d. O prazo é de 25 ms; como 20 ms não excede esse prazo, nenhum estouro deve ocorrer.
e. O prazo é de 3 ms; como 20 ms excede esse prazo, o `Watchdog` deve reiniciar automaticamente o processo do alvo sem sinalizar falha.

**33.** A latência p95 medida em uma execução de `run_closed_loop_hil` foi de 0,287 ms, e a latência máxima foi de 2,002 ms, sobre um Ts nominal de 5 ms. Se a equipe configurar o `Watchdog` com um prazo de exatamente 0,3 ms — pouco acima do p95 —, qual é a consequência mais provável dessa escolha?

a. Nenhuma consequência, pois o prazo de 0,3 ms é maior do que toda a distribuição de latências observadas.
b. O `Watchdog` nunca estourará, pois o prazo está acima da latência média de 0,108 ms.
c. O `Watchdog` estourará em exatamente 5% das chamadas, coincidindo perfeitamente com a definição de percentil 95.
*d. O `Watchdog` provavelmente produzirá falsos positivos frequentes, pois a latência máxima observada (2,002 ms) excede em muito o prazo configurado, e ao menos 5% das chamadas já ultrapassam o p95 de 0,287 ms.
e. O `Watchdog` deve ser configurado sempre abaixo do p95, pois esse é o procedimento recomendado pela Aula 15.

**34.** Uma equipe afirma: "já testamos o controlador em HIL na Aula 14, comparando o modelo Python com o código C compilado dentro do mesmo processo." Sobre essa afirmação, é correto dizer que:

a. Está correta, pois HIL e SIL são termos intercambiáveis para a mesma técnica de verificação.
*b. Está incorreta, pois o que foi descrito — modelo e código C executados no mesmo processo, sem restrição de tempo real — é a definição de SIL (Aula 14), não de HIL, que exige o controlador rodando como alvo separado, sujeito a tempo real (Aula 15).
c. Está incorreta, apenas porque HIL exige necessariamente um ESP32 físico conectado por porta serial.
d. Está correta, desde que o teste tenha sido executado com `real_time=True`.
e. Está incorreta, apenas porque a Aula 14 usa Python puro, sem nenhum código C envolvido.

**35.** Um controlador apresenta erro de equivalência SIL de exatamente 0,0 V (double) e, ao ser testado em HIL, apresenta latência máxima de 2,002 ms sobre um Ts de 5 ms, sem qualquer estouro de watchdog registrado. Qual conclusão é tecnicamente correta sobre esse controlador?

a. Como o erro de equivalência é zero, o comportamento temporal medido em HIL é redundante e poderia ter sido dispensado.
b. A ausência de estouro do watchdog garante que o controlador nunca apresentará jitter em produção, sob nenhuma condição de carga.
*c. As duas evidências são complementares e independentes: a equivalência numérica (SIL) mostra que a lógica do código está correta, e o comportamento temporal (HIL) mostra que, nas condições testadas, o alvo respondeu dentro do prazo — nenhuma delas garante a outra.
d. O resultado de HIL substitui a necessidade de verificação formal do supervisor realizada na Unidade 3.
e. Como não houve estouro de watchdog, o sistema está formalmente certificado para operação em campo.

**36.** A verificação exaustiva de REQ-SAFE-006 explora 6 caminhos e encontra um pior caso de 5 períodos de atuação até o torque ser zerado, com Ts=5 ms. Qual é a margem, em milissegundos, entre esse pior caso e o limite de 150 ms exigido pelo requisito?

*a. O pior caso é de 25 ms (5×5 ms), o que deixa uma margem de 125 ms frente ao limite de 150 ms.
b. O pior caso é de 30 ms (6×5 ms, um por caminho explorado), com margem de 120 ms.
c. O pior caso é de 25 ms, mas o limite real é de 25 ms também, sem qualquer margem.
d. O pior caso excede o limite de 150 ms, caracterizando violação do requisito.
e. O cálculo não pode ser feito sem conhecer o valor exato de d_stop_max em segundos.

**37.** Ao ser questionada por um cliente de robótica industrial se o pipeline apresentado "gera evidências suficientes para certificar o robô conforme a ISO 26262", a equipe do NexaBot responde: "sim, geramos modelo versionado, propriedades formais verificadas, testes com cobertura medida, código rastreável, equivalência numérica medida e um pipeline de CI — isso é certificação completa." Do ponto de vista da Aula 16, essa resposta está:

a. Correta, pois as seis evidências listadas são exatamente os seis requisitos formais da ISO 26262 para certificação.
b. Correta, desde que o cliente aceite a matriz de rastreabilidade gerada automaticamente como documento oficial de certificação.
c. Incorreta, apenas porque falta incluir testes de HIL na lista de evidências apresentadas.
d. Incorreta, apenas porque a ISO 26262 não reconhece nenhuma forma de verificação formal automatizada como evidência válida.
*e. Incorreta, pois as seis evidências listadas são reais e valiosas, mas certificação exige também independência entre quem desenvolve e verifica, qualificação formal das ferramentas e aprovação de uma autoridade certificadora — nenhuma delas produzida por esse pipeline técnico, por mais completo que seja.

**38.** Uma equipe argumenta que, como a suíte de testes do NexaBot atinge cobertura de código medida e passa integralmente na esteira de integração contínua, isso substitui a necessidade de qualificação formal de ferramentas como SymPy, Jinja2 e GCC exigida por normas como a DO-178C. Essa argumentação está:

a. Correta, pois cobertura de código e CI são, por definição normativa, formas equivalentes de qualificação de ferramenta.
b. Correta, desde que a cobertura medida seja de 100% das linhas de código geradas.
*c. Incorreta: cobertura e CI não tornam uma ferramenta automaticamente qualificada. A equipe ainda precisa analisar o uso, o impacto de erros e a capacidade de detectá-los por verificação posterior; conforme essa análise, qualifica a ferramenta ou adota verificação independente suficiente.
d. Incorreta, apenas porque a cobertura de código do NexaBot está abaixo do mínimo exigido pela DO-178C.
e. Correta, pois GCC é homologado automaticamente como ferramenta qualificada sempre que compila software aprovado por testes de regressão.

**39.** Comparando os três domínios discutidos na Aula 16 — automotivo (ISO 26262), aeroespacial (DO-178C) e robótica industrial (ISO 10218/ISO-TS 15066) —, qual afirmação descreve corretamente uma diferença relevante entre eles quanto à exigência de medir e documentar o pior caso de tempo de resposta?

a. Apenas o setor aeroespacial exige medir tempo de resposta; os demais setores dispensam essa exigência.
b. A robótica industrial não exige qualquer evidência de tempo de resposta de parada, por operar sob regime totalmente informal.
c. O setor automotivo é o único que aceita autômatos temporizados como evidência de pior caso.
*d. Os três setores exigem, conforme a função analisada, evidência de tempo de resposta ou pior caso, mas diferem no processo de garantia e auditoria; no aeroespacial, o plano aprovado e a análise de confiança das ferramentas seguem critérios próprios do nível de software e do uso de cada ferramenta.
e. A robótica industrial adota exatamente os mesmos DAL da DO-178C, apenas com nomenclatura diferente.

**40.** Ao encerrar a disciplina, um estudante resume a trajetória das quatro unidades do NexaBot como: "identificamos o modelo, fechamos a malha com PID, provamos formalmente o supervisor e geramos código com rastreabilidade — portanto o sistema está pronto para produção sem qualquer ressalva." Sob a ótica da honestidade técnica construída na Aula 16, esse resumo:

a. Está correto, pois a travessia completa das quatro camadas — modelo, controle, verificação formal, código rastreável — é, por definição, suficiente para produção em qualquer domínio.
*b. Omite uma distinção essencial: o resumo descreve evidências reais, mas conclui indevidamente que não há ressalvas, ignorando a lacuna de verificação do REQ-SAFE-007 e a distinção entre evidência técnica e certificação/aprovação organizacional.
c. Está correto, desde que o supervisor tenha sido verificado exaustivamente na Unidade 3, o que dispensa qualquer ressalva sobre código ou tempo real.
d. Está incorreto, apenas porque a Unidade 1 não foi mencionada explicitamente no resumo do estudante.
e. Está correto, pois a matriz relaciona 14 requisitos em 91 arquivos Python, número que por si só é evidência suficiente para qualquer domínio.

## Gabarito e feedbacks

**Questão 1** (correta: c)
- a. Incorreta: a asserção II é falsa, não verdadeira — o gcc não detecta nem impede a compilação de um arquivo `.c` editado manualmente, e o hash não é recalculado automaticamente ao salvar.
- b. Incorreta: a asserção II é falsa pelo mesmo motivo.
- c. Correta: a I é verdadeira — o arquivo gerado é, por definição, artefato derivado, corrigido sempre no modelo; a II é falsa, pois nada no gcc detecta ou impede a compilação de C editado manualmente, nem recalcula o hash automaticamente.
- d. Incorreta: a asserção I é verdadeira, não falsa.
- e. Incorreta: a asserção I é verdadeira, não falsa.

**Questão 2** (correta: a)
- a. Correta: ambas as asserções são verdadeiras, e a II descreve corretamente o mecanismo (`compute_params_hash` sobre os sete parâmetros) que explica por que o bloco de rastreabilidade liga o arquivo aos requisitos, à versão e ao hash.
- b. Incorreta: a II de fato justifica a I nesta questão.
- c. Incorreta: a asserção II também é verdadeira, não falsa.
- d. Incorreta: a asserção I também é verdadeira, não falsa.
- e. Incorreta: as duas asserções são verdadeiras, não falsas.

**Questão 3** (correta: e)
- a. Incorreta: as duas asserções são falsas, não verdadeiras.
- b. Incorreta: as duas asserções são falsas, não verdadeiras.
- c. Incorreta: a asserção I é falsa — Q16.16 usa `int32_t` (32 bits), não 64 bits, e não elimina completamente o erro de arredondamento.
- d. Incorreta: a asserção II também é falsa — a multiplicação exige acumulador de 64 bits (`int64_t`) antes do deslocamento, não pode ser feita diretamente em `int32_t`.
- e. Correta: a I é falsa pelo formato incorreto e pela ausência de eliminação total do erro; a II é falsa porque a multiplicação exige acumulador intermediário de 64 bits, e não é feita diretamente em `int32_t`.

**Questão 4** (correta: b)
- a. Incorreta: a II é verdadeira apenas como fato genérico sobre o SymPy; não justifica especificamente por que as equações do PID foram derivadas em vez de digitadas.
- b. Correta: ambas as asserções são verdadeiras, mas a II é um fato genérico sobre a biblioteca SymPy, que não explica a escolha metodológica descrita na I.
- c. Incorreta: a asserção II também é verdadeira, não falsa.
- d. Incorreta: a asserção I também é verdadeira, não falsa.
- e. Incorreta: as duas asserções são verdadeiras, não falsas.

**Questão 5** (correta: d)
- a. Incorreta: a asserção I é falsa, não verdadeira.
- b. Incorreta: a asserção I é falsa, não verdadeira.
- c. Incorreta: a I é falsa, e a II é verdadeira, não falsa.
- d. Correta: a I é falsa — a Aula 13 não afirma que Euler para trás produz menos erro de discretização do que Tustin para qualquer Ts, apenas que foi escolhida pelo custo computacional mais baixo; a II é verdadeira e descreve corretamente essa vantagem de custo.
- e. Incorreta: a asserção II é verdadeira, não falsa.

**Questão 6** (correta: a)
- a. Correta: ambas as asserções são verdadeiras, e a II descreve o mecanismo de `compare_model_vs_code` que torna possível a medição amostra a amostra afirmada na I.
- b. Incorreta: a II de fato justifica a I nesta questão.
- c. Incorreta: a asserção II também é verdadeira, não falsa.
- d. Incorreta: a asserção I também é verdadeira, não falsa.
- e. Incorreta: as duas asserções são verdadeiras, não falsas.

**Questão 7** (correta: c)
- a. Incorreta: a asserção II é falsa, não verdadeira.
- b. Incorreta: a asserção II é falsa, não verdadeira.
- c. Correta: a I é verdadeira — erro zero é consistente com (e até melhor do que) a expectativa de equivalência na ordem do épsilon de máquina; a II é falsa, pois erro zero indica justamente que gcc -O2 sem -ffast-math preservou a mesma ordem de operações IEEE-754, não que aplicou reordenação agressiva.
- d. Incorreta: a asserção I é verdadeira, não falsa.
- e. Incorreta: a asserção I é verdadeira, não falsa.

**Questão 8** (correta: e)
- a. Incorreta: as duas asserções são falsas, não verdadeiras.
- b. Incorreta: as duas asserções são falsas, não verdadeiras.
- c. Incorreta: a asserção I é falsa — testes de regressão são evidência valiosa, mas não certificam formalmente nada; certificação exige independência de verificação, qualificação de ferramenta e aprovação de autoridade.
- d. Incorreta: a asserção II também é falsa — mesmo com tolerância de 10⁻⁹ V (muito maior que o épsilon de máquina), o teste detectaria facilmente um bug de lógica como o do anti-windup removido, cujo erro (12,61 V) é muitas ordens de grandeza acima dessa tolerância.
- e. Correta: a I é falsa pelo motivo de certificação exposto; a II é falsa porque a tolerância adotada continua muito menor do que o erro produzido por um bug de lógica real, permanecendo capaz de detectá-lo.

**Questão 9** (correta: b)
- a. Incorreta: a II é verdadeira, mas descreve a composição da sequência de teste, não a razão do valor de 12,61 V medido.
- b. Correta: ambas as asserções são verdadeiras — o erro de 12,61 V está de fato documentado, e as sequências fixas de teste também estão corretamente descritas —, mas a II não explica por que a remoção do anti-windup produziu esse erro específico.
- c. Incorreta: a asserção II também é verdadeira, não falsa.
- d. Incorreta: a asserção I também é verdadeira, não falsa.
- e. Incorreta: as duas asserções são verdadeiras, não falsas.

**Questão 10** (correta: d)
- a. Incorreta: a asserção I é falsa, não verdadeira.
- b. Incorreta: a asserção I é falsa, não verdadeira.
- c. Incorreta: a I é falsa, e a II é verdadeira, não falsa.
- d. Correta: a I é falsa — a Aula 14 não trata esse erro como invalidação automática, mas como um número que a equipe avalia frente ao requisito; a II é verdadeira e reproduz corretamente o cálculo percentual e a atribuição da decisão à equipe.
- e. Incorreta: a asserção II é verdadeira, não falsa.

**Questão 11** (correta: e)
- a. Incorreta: as duas asserções são falsas, não verdadeiras.
- b. Incorreta: as duas asserções são falsas, não verdadeiras.
- c. Incorreta: a asserção I é falsa — SIL e HIL verificam propriedades independentes; equivalência numérica não garante comportamento temporal.
- d. Incorreta: a asserção II também é falsa — a definição dada é de latência, não de jitter, que é a variação do período efetivo do laço.
- e. Correta: a I é falsa pela independência entre as duas propriedades; a II é falsa porque troca a definição de jitter pela de latência.

**Questão 12** (correta: b)
- a. Incorreta: a II é verdadeira, mas descreve o protocolo de linha, não o motivo do valor de jitter medido.
- b. Correta: ambas as asserções são verdadeiras — o valor de jitter está corretamente reportado, e o protocolo ASCII realmente existe —, mas a II não justifica a métrica de jitter apresentada na I.
- c. Incorreta: a asserção II também é verdadeira, não falsa.
- d. Incorreta: a asserção I também é verdadeira, não falsa.
- e. Incorreta: as duas asserções são verdadeiras, não falsas.

**Questão 13** (correta: a)
- a. Correta: ambas as asserções são verdadeiras, e a II fornece exatamente a justificativa de segurança (assumir o pior caso diante da incerteza) para o comportamento do watchdog descrito na I.
- b. Incorreta: a II de fato justifica a I nesta questão.
- c. Incorreta: a asserção II também é verdadeira, não falsa.
- d. Incorreta: a asserção I também é verdadeira, não falsa.
- e. Incorreta: as duas asserções são verdadeiras, não falsas.

**Questão 14** (correta: d)
- a. Incorreta: a asserção I é falsa, não verdadeira.
- b. Incorreta: a asserção I é falsa, não verdadeira.
- c. Incorreta: a I é falsa, e a II é verdadeira, não falsa.
- d. Correta: a I é falsa — o protocolo é idêntico entre os dois back-ends, e nenhuma alteração de lógica de controle é exigida; a II é verdadeira e descreve corretamente que a diferença está só no transporte.
- e. Incorreta: a asserção II é verdadeira, não falsa.

**Questão 15** (correta: c)
- a. Incorreta: a asserção II é falsa, não verdadeira.
- b. Incorreta: a asserção II é falsa, não verdadeira.
- c. Correta: a I é verdadeira — 2,002/5=0,4004, cerca de 40% do período nominal; a II é falsa, pois latência é medida em unidades de tempo (segundos/milissegundos) via relógio de alta resolução, e radianos por segundo não é uma unidade de tempo.
- d. Incorreta: a asserção I é verdadeira, não falsa.
- e. Incorreta: a asserção I é verdadeira, não falsa.

**Questão 16** (correta: d)
- a. Incorreta: a asserção I é falsa, não verdadeira.
- b. Incorreta: a asserção I é falsa, não verdadeira.
- c. Incorreta: a I é falsa, e a II é verdadeira, não falsa.
- d. Correta: a I é falsa — as normas não compartilham a mesma nomenclatura nem o mesmo número de níveis; a II é verdadeira e descreve corretamente os cinco DAL (A-E) da DO-178C e os quatro ASIL (A-D) da ISO 26262.
- e. Incorreta: a asserção II é verdadeira, não falsa.

**Questão 17** (correta: e)
- a. Incorreta: as duas asserções são falsas, não verdadeiras.
- b. Incorreta: as duas asserções são falsas, não verdadeiras.
- c. Incorreta: a asserção I é falsa — varredura estática de rastreabilidade não constitui qualificação formal de ferramenta.
- d. Incorreta: a asserção II também é falsa — qualificação de ferramenta significa comprovação formal, com evidência, de que a ferramenta produz saídas corretas com confiança compatível com a criticidade, não popularidade na comunidade open source.
- e. Correta: a I é falsa, pois rastreabilidade não é qualificação de ferramenta; a II é falsa, pois qualificação exige evidência formal de correção, não apenas ampla adoção.

**Questão 18** (correta: c)
- a. Incorreta: a asserção II é falsa, não verdadeira.
- b. Incorreta: a asserção II é falsa, não verdadeira.
- c. Correta: a I é verdadeira — reproduz a posição da Aula 16 sobre ferramentas não qualificadas; a II é falsa, pois não existe proibição legal geral ao uso de ferramentas abertas em contexto certificado, apenas a exigência de qualificá-las quando necessário.
- d. Incorreta: a asserção I é verdadeira, não falsa.
- e. Incorreta: a asserção I é verdadeira, não falsa.

**Questão 19** (correta: a)
- a. Correta: ambas as asserções são verdadeiras; a II explica exatamente por que as colunas "código gerado" e "teste" ficam vazias para REQ-SAFE-006 — a lógica do supervisor não passa pelo codegen do PID, e a verificação existente é exaustiva, não um teste automatizado dedicado.
- b. Incorreta: a II de fato justifica a I nesta questão.
- c. Incorreta: a asserção II também é verdadeira, não falsa.
- d. Incorreta: a asserção I também é verdadeira, não falsa.
- e. Incorreta: as duas asserções são verdadeiras, não falsas.

**Questão 20** (correta: b)
- a. Incorreta: a II é verdadeira, mas descreve contexto regulatório de outro domínio, não o motivo do valor de 25 ms encontrado para o NexaBot.
- b. Correta: ambas as asserções são verdadeiras — o pior caso de 25 ms está de fato dentro do limite, e a caracterização da robótica industrial também está correta —, mas a II não explica por que o pior caso do NexaBot é 25 ms.
- c. Incorreta: a asserção II também é verdadeira, não falsa.
- d. Incorreta: a asserção I também é verdadeira, não falsa.
- e. Incorreta: as duas asserções são verdadeiras, não falsas.

**Questão 21** (correta: b)
- a. Incorreta: o SHA-256 não preserva similaridade de entrada; qualquer alteração, por menor que seja, produz uma saída completamente diferente (efeito avalanche).
- b. Correta: `compute_params_hash` recalcula o hash a partir do JSON ordenado dos sete parâmetros; alterar qualquer um deles, mesmo levemente, produz um hash inteiramente novo, sem relação visível com o anterior.
- c. Incorreta: o SHA-256 não preserva prefixos entre entradas semelhantes; é próprio do efeito avalanche que pequenas mudanças alterem o hash inteiro, não apenas parte dele.
- d. Incorreta: o hash é recalculado automaticamente a cada geração, dentro do próprio processo de `generate_pid_controller`, sem exigir edição manual do cabeçalho.
- e. Incorreta: o hash é uma função determinística dos parâmetros atuais; não incorpora valores históricos ou anteriores.

**Questão 22** (correta: d)
- a. Incorreta: τ_f não é múltiplo exato de Δ=2⁻¹⁶, portanto sofre arredondamento.
- b. Incorreta: τ_f×2¹⁶=655,36, não é um inteiro exato; há parte fracionária a arredondar.
- c. Incorreta: 655,36 arredonda para baixo, para 655, não para cima, para 656.
- d. Correta: 0,01×65536=655,36, arredondado para 655; τ_f_fixo=655/65536=0,0099945068359375 s, um erro de aproximadamente −5,493×10⁻⁶ s, conforme medido na Aula 13.
- e. Incorreta: τ_f=0,01 está bem dentro da faixa representável de um formato com 16 bits inteiros.

**Questão 23** (correta: a)
- a. Correta: o módulo `derive.py` verifica que o resíduo simbólico entre a recorrência derivada e o contrato de `DiscretePID.step` é identicamente zero, recusando-se a gerar C caso haja qualquer divergência algébrica.
- b. Incorreta: a verificação exige resíduo identicamente zero (algébrico), não uma tolerância numérica de épsilon de máquina.
- c. Incorreta: o `AssertionError` ocorre na etapa de derivação simbólica, antes de qualquer tentativa de compilação com gcc.
- d. Incorreta: a verificação simbólica não substitui a equivalência numérica medida por SIL sobre o código já compilado; são etapas complementares.
- e. Incorreta: a comparação é feita simbolicamente, com os símbolos genéricos do SymPy, não com valores numéricos concretos de Kp, Ki e Kd.

**Questão 24** (correta: c)
- a. Incorreta: Q16.16 usa `int32_t` com bit de sinal, representando números negativos normalmente, sem lógica adicional.
- b. Incorreta: a comparação de velocidade depende da implementação específica; a Aula 13 não afirma essa superioridade universal da FPU.
- c. Correta: a Aula 13 justifica o ponto fixo pelo custo de emular `double` em microcontroladores sem FPU, que pode comprometer o período de amostragem — não pela superioridade incondicional de um formato sobre o outro.
- d. Incorreta: o ponto fixo não elimina o erro de quantização; ao contrário, a Aula 13 mede exatamente esse erro para Ts, τ_f e Kd.
- e. Incorreta: o acumulador de 64 bits (`int64_t`) é uma escolha de implementação em software, disponível em qualquer microcontrolador de 32 bits com suporte a aritmética de 64 bits em software.

**Questão 25** (correta: e)
- a. Incorreta: 2,2 não é múltiplo exato de Δ=2⁻¹⁶, logo há erro de arredondamento.
- b. Incorreta: 144.179,2 não arredonda para 144.180; a parte fracionária 0,2 é menor que 0,5 e arredonda para baixo.
- c. Incorreta: 2,2 está bem dentro da faixa representável por 16 bits inteiros com sinal em Q16.16.
- d. Incorreta: o formato Q16.16 armazena apenas inteiros de 32 bits; a parte fracionária de 144.179,2 não pode ser preservada diretamente.
- e. Correta: round(144.179,2)=144.179 (0,2 arredonda para baixo), com pequeno erro de arredondamento, pois 2,2 não é múltiplo exato da resolução Δ.

**Questão 26** (correta: d)
- a. Incorreta: 10⁸ subestima muito a razão real entre 12,61 V e 2,22×10⁻¹⁶.
- b. Incorreta: 10¹² também subestima a razão real.
- c. Incorreta: 10¹⁴ ainda está abaixo da ordem de grandeza correta.
- d. Correta: 12,61 / 2,22×10⁻¹⁶ ≈ 5,68×10¹⁶, valor reportado na Aula 14 como assinatura inconfundível de divergência de lógica.
- e. Incorreta: 10²⁰ superestima a razão real.

**Questão 27** (correta: b)
- a. Incorreta: duas implementações independentes que seguem exatamente a mesma aritmética IEEE-754, na mesma ordem de operações, podem legitimamente produzir erro zero — não é impossível.
- b. Correta: NumPy e gcc -O2 (sem -ffast-math) seguem a mesma aritmética de dupla precisão na mesma ordem de operações; erro zero é, portanto, um resultado plausível e esperado, não suspeito.
- c. Incorreta: comparar com tolerância (como fazem os testes de regressão) é uma prática complementar de engenharia de testes, mas não torna o valor exato zero, por si só, suspeito.
- d. Incorreta: erro zero não implica que o código não foi executado; ao contrário, é consistente com a execução correta do binário real compilado.
- e. Incorreta: 2.000 amostras, cobrindo degrau e componente senoidal, são suficientes para revelar divergências de lógica, como demonstrado pelo próprio experimento do anti-windup removido.

**Questão 28** (correta: e)
- a. Incorreta: a DO-178C não define equivalência numérica em SIL como único critério de certificação; certificação envolve múltiplos elementos organizacionais e de processo.
- b. Incorreta: mesmo com erro exatamente zero, a equivalência numérica sozinha não constitui certificação.
- c. Incorreta: o SIL desta disciplina compila e executa o código C real gerado, via `ctypes`, não uma simulação aproximada do comportamento esperado.
- d. Incorreta: o número de amostras não é o motivo central pelo qual a equivalência SIL não equivale a certificação; mesmo com todos os cenários cobertos, faltariam os demais elementos do processo.
- e. Correta: as evidências de equivalência numérica são reais e valiosas, mas certificação real exige também independência de verificação, qualificação formal de ferramenta e aprovação de autoridade certificadora — nenhuma delas produzida pela medição de erro em SIL.

**Questão 29** (correta: a)
- a. Correta: uma troca de operador no template alteraria a lógica do código gerado, produzindo um erro de magnitude comparável ao caso do anti-windup removido (muitas ordens de grandeza acima de 10⁻⁹ V), o que o teste de regressão detectaria e falharia.
- b. Incorreta: erros de template afetam diretamente a lógica do C gerado, e portanto afetam sim a equivalência numérica medida por SIL.
- c. Incorreta: o teste de regressão falha pela comparação numérica de `compare_model_vs_code`, independentemente de a compilação em si ter tido sucesso.
- d. Incorreta: um erro de lógica como a troca de operador produziria erro muito acima do épsilon de máquina, não abaixo dele.
- e. Incorreta: o comportamento do teste é bem definido — ele compara erro numérico contra um limiar fixo e falha quando esse limiar é ultrapassado.

**Questão 30** (correta: c)
- a. Incorreta: a análise de quantização da Aula 13 não prevê que qualquer variação nos ganhos aumente proporcionalmente o erro de Ts e τ_f, que dependem apenas de seus próprios valores.
- b. Incorreta: a escolha de formato (Q16.16 versus outro) não é determinada pela combinação específica de ganhos usada nesta comparação.
- c. Correta: um erro de 4,2 V é ordens de grandeza maior do que o esperado pela propagação dos erros de quantização de Ts, τ_f e Kd (que produziram um erro máximo de 0,01586 V com os ganhos originais), sinalizando possível bug, não efeito normal do ponto fixo.
- d. Incorreta: não há, no conteúdo da disciplina, relação entre o valor de Kp e uma saturação automática do formato Q16.16.
- e. Incorreta: um erro de 4,2 V frente a um fundo de escala de 24 V (17,5%) é significativo e não deve ser ignorado.

**Questão 31** (correta: e)
- a. Incorreta: 0,75/5 corresponde a 15%, não a 5%.
- b. Incorreta: 7,5% corresponderia a um jitter de 0,375 ms, não a 0,75 ms.
- c. Incorreta: 10% corresponderia a um jitter de 0,5 ms, não a 0,75 ms.
- d. Incorreta: 12,5% corresponderia a um jitter de 0,625 ms, não a 0,75 ms.
- e. Correta: 0,75 ms / 5 ms = 0,15, ou seja, 15% do período nominal.

**Questão 32** (correta: a)
- a. Correta: 3×Ts=3×5 ms=15 ms; como o atraso de 20 ms excede esse prazo, o `Watchdog` deve devolver u=0,0 V e sinalizar `estourou=True`, exatamente como no cenário de atraso de 50 ms sob prazo de 10 ms descrito na aula.
- b. Incorreta: 3×Ts=15 ms, não 5 ms; além disso, o `Watchdog` não aguarda ciclos adicionais — decide dentro do prazo configurado.
- c. Incorreta: o comando seguro do `Watchdog`, por definição (REQ-SAFE-004), é tensão zero, não o último comando válido.
- d. Incorreta: 3×Ts=15 ms, não 25 ms; e 20 ms excede 15 ms, portanto há estouro.
- e. Incorreta: 3×Ts=15 ms, não 3 ms; e o `Watchdog` não reinicia automaticamente sem sinalizar falha — ele sinaliza o estouro explicitamente.

**Questão 33** (correta: d)
- a. Incorreta: 0,3 ms está abaixo, não acima, da latência máxima observada de 2,002 ms.
- b. Incorreta: estar acima da latência média não implica ausência de estouros, pois a distribuição de latências tem cauda longa, como evidenciado pela latência máxima muito superior à média.
- c. Incorreta: o percentil 95 caracteriza a distribuição das latências já observadas, não garante que exatamente 5% das chamadas futuras estourarão um prazo próximo a ele.
- d. Correta: com prazo de apenas 0,3 ms, ao menos 5% das chamadas (as que excedem o p95 de 0,287 ms) já se aproximam ou ultrapassam esse valor, e a latência máxima de 2,002 ms mostra que estouros reais são prováveis nessa configuração apertada.
- e. Incorreta: a aula não recomenda configurar o prazo sempre abaixo do p95; ao contrário, sugere prazos com margem sobre a latência observada para evitar falsos positivos.

**Questão 34** (correta: b)
- a. Incorreta: SIL e HIL são técnicas distintas e não intercambiáveis, verificando propriedades diferentes (numérica e temporal, respectivamente).
- b. Correta: executar modelo e código C no mesmo processo, sem restrição de tempo real, é exatamente a definição de SIL (Aula 14); HIL (Aula 15) exige o controlador rodando como alvo separado, sob restrição de tempo real.
- c. Incorreta: o `LoopbackTarget` permite fazer HIL sem hardware físico, usando um subprocesso local; ESP32 é necessário apenas para `SerialTarget`.
- d. Incorreta: mesmo com `real_time=True`, o que foi descrito no enunciado (modelo e C no mesmo processo) continua sendo a definição de SIL, não de HIL.
- e. Incorreta: a Aula 14 envolve, sim, código C real, compilado e executado via `ctypes`, ao lado do modelo em Python.

**Questão 35** (correta: c)
- a. Incorreta: o comportamento temporal medido em HIL não é redundante frente à equivalência numérica; são propriedades independentes que a Aula 15 explicitamente distingue.
- b. Incorreta: a ausência de estouro em uma execução específica não garante ausência de jitter sob qualquer condição de carga futura; é uma medição empírica, não uma prova de limite superior.
- c. Correta: SIL comprova a correção da lógica do código (equivalência numérica), e HIL comprova que, nas condições testadas, o comportamento temporal respeitou o prazo — nenhuma das duas evidências implica ou substitui a outra.
- d. Incorreta: HIL não substitui a verificação formal exaustiva do supervisor realizada na Unidade 3; são etapas complementares do pipeline.
- e. Incorreta: ausência de estouro de watchdog em um teste específico não caracteriza certificação formal para operação em campo.

**Questão 36** (correta: a)
- a. Correta: 5 períodos × 5 ms = 25 ms; a margem frente ao limite de 150 ms é 150−25=125 ms.
- b. Incorreta: o número de caminhos explorados (6) não corresponde ao número de períodos do pior caso (5); são grandezas diferentes.
- c. Incorreta: o limite exigido pelo requisito é 150 ms, não 25 ms.
- d. Incorreta: 25 ms está dentro do limite de 150 ms, não o excede.
- e. Incorreta: o valor de d_stop_max=150 ms já está explicitamente fornecido no enunciado da aula, permitindo o cálculo da margem sem informação adicional.

**Questão 37** (correta: e)
- a. Incorreta: as seis evidências listadas não são os "requisitos formais" da ISO 26262 para certificação; são evidências técnicas que servem de insumo a um processo mais amplo.
- b. Incorreta: uma matriz de rastreabilidade gerada automaticamente, por si só, não é aceita como documento oficial de certificação por nenhuma autoridade.
- c. Incorreta: a ausência de HIL na lista não é o motivo central da incorreção; mesmo incluindo HIL, faltariam independência de verificação, qualificação de ferramenta e aprovação de autoridade.
- d. Incorreta: a ISO 26262 pode, sim, considerar verificação formal automatizada como evidência valiosa; o problema não está em rejeitá-la, e sim em confundir evidência com certificação completa.
- e. Correta: as evidências são reais e valiosas, mas certificação exige também independência entre desenvolvimento e verificação, qualificação formal das ferramentas e aprovação de autoridade certificadora — elementos que nenhum pipeline técnico produz sozinho.

**Questão 38** (correta: c)
- a. Incorreta: não existe equivalência normativa entre cobertura de código/CI e qualificação formal de ferramenta; são conceitos distintos na DO-178C.
- b. Incorreta: cobertura de linhas não decide, sozinha, a confiança na ferramenta; é preciso considerar o uso e se erros da ferramenta seriam detectados posteriormente.
- c. Correta: cobertura e CI não qualificam automaticamente SymPy, Jinja2 ou GCC. A estratégia aplicável pode exigir qualificação ou verificação independente suficiente das saídas, conforme o uso e o impacto de erro.
- d. Incorreta: o argumento apresentado erra por confundir os dois conceitos, independentemente do valor específico de cobertura obtido.
- e. Incorreta: não existe homologação automática de GCC pela aprovação em testes de regressão; qualificação de ferramenta exige processo formal próprio.

**Questão 39** (correta: d)
- a. Incorreta: a Aula 16 discute exigências de tempo de resposta também no setor automotivo (HARA/ASIL) e na robótica industrial (ISO 10218/ISO-TS 15066), não apenas no aeroespacial.
- b. Incorreta: a robótica industrial exige, sim, evidência de tempo de resposta de parada, ainda que sob um regime de auditoria menos formalizado do que o aeroespacial.
- c. Incorreta: autômatos temporizados são mencionados como possível ferramenta de verificação no setor automotivo, mas isso não impede seu uso, como demonstrado pelo próprio NexaBot, em outros contextos.
- d. Correta: os domínios podem exigir evidência temporal, mas usam processos de garantia e auditoria diferentes; no aeroespacial, planos, níveis de software e critérios de confiança em ferramentas dependem do contexto de uso.
- e. Incorreta: a robótica industrial não usa a nomenclatura DAL da DO-178C; utiliza normas próprias (ISO 10218, ISO/TS 15066).

**Questão 40** (correta: b)
- a. Incorreta: a travessia das quatro camadas produz evidência técnica robusta, mas não é, por definição, suficiente para eliminar qualquer ressalva de produção em qualquer domínio.
- b. Correta: o resumo reconhece evidências reais, mas conclui indevidamente que isso elimina toda ressalva, ignorando a lacuna explícita do REQ-SAFE-007 e a distinção entre evidência técnica e certificação/aprovação organizacional.
- c. Incorreta: verificação exaustiva do supervisor não dispensa ressalvas relativas a código gerado ou comportamento em tempo real, que são propriedades distintas verificadas em aulas diferentes.
- d. Incorreta: a omissão da Unidade 1 no resumo não é o problema central identificado pela Aula 16; o problema está na conclusão de ausência de ressalvas.
- e. Incorreta: o número de requisitos e arquivos relacionados na matriz não é, por si só, evidência suficiente para qualquer domínio de aplicação; a suficiência depende do processo de certificação de cada domínio.
