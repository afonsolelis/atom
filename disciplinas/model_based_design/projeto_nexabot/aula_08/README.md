# Aula 8 — Co-simulação planta-controlador com FMI 3.0

Scripts numerados para execução ao vivo, na ordem, durante a gravação com
captura de tela. Todos os comandos assumem que o diretório de trabalho é a
raiz do projeto (`projeto_nexabot/`) e usam o interpretador do venv do
projeto.

## Pré-requisitos

- `gcc` disponível no PATH (usado para compilar o FMU).
- Ambiente virtual `.venv/` já criado com `numpy`, `scipy`, `control`,
  `sympy`, `matplotlib`, `fmpy`, `pytest` etc. (já presente no repositório).

## Ordem de execução

### 1. Construir o FMU

```
.venv/bin/python aula_08/01_build_fmu.py
```

Compila `nexabot/fmu/plant_fmu.c` com `gcc -shared -fPIC -O2`, monta a
árvore `binaries/x86_64-linux/NexaBotPlant.so` + `modelDescription.xml` e
empacota tudo em `nexabot/fmu/NexaBotPlant.fmu`. Ao final, lista o
conteúdo do `.fmu` gerado (é um `.zip` comum — pode confirmar com
`unzip -l nexabot/fmu/NexaBotPlant.fmu`).

**Saída esperada (resumo):** confirmação da compilação, tamanho do `.fmu`
(~7 KB) e uma tabela com os dois arquivos internos
(`binaries/x86_64-linux/NexaBotPlant.so`, `modelDescription.xml`).

### 2. Inspecionar o FMU

```
.venv/bin/python aula_08/02_inspecta_fmu.py
```

Lê `modelDescription.xml` com `fmpy.read_model_description` e lista as 5
variáveis do modelo: `time` (independente), `u_volts`/`tau_load` (entradas),
`omega`/`current` (saídas). Roda também `fmpy.dump(...)` para uma segunda
visão (a "ficha técnica" que qualquer ferramenta FMI mostraria).

**Saída esperada (resumo):** `fmiVersion 3.0`, `FMI Type Co-Simulation`,
tabela com as 5 variáveis e suas causalidades.

### 3. Co-simulação básica

```
.venv/bin/python aula_08/03_cosim_basica.py
```

Roda `nexabot.cosim.run_cosimulation` com passo de comunicação **H = 5 ms**
(200 Hz, o mesmo `PARAMS.Ts`), degrau de referência de 1,0 m/s. Imprime uma
tabela tempo / referência / velocidade / tensão.

**Saída esperada (resumo):** a velocidade converge para 1,0000 m/s
(400 rad/s) e a tensão de regime converge para **≈ 18,85 V** — o valor
citado no enunciado da disciplina.

### 4. Erro de acoplamento (ponto pedagógico central da aula)

```
.venv/bin/python aula_08/04_erro_de_acoplamento.py
```

Varre H em {1, 5, 10, 20, 50} ms para o mesmo degrau de 1,0 m/s e compara
cada trajetória contra uma referência "quase-contínua" (H = 0,5 ms),
medindo o erro RMS e o erro máximo relativos.

**Saída esperada (resumo):** o erro RMS cresce monotonicamente com H —
na execução de referência, de **0,028 %** (H = 1 ms) até **6,2 %**
(H = 50 ms). Isso demonstra numericamente que passos de comunicação
maiores degradam a fidelidade da co-simulação, porque a tensão de comando
fica retida (ZOH) por mais tempo e o `DiscretePID` também passa a
amostrar mais devagar (seu `Ts` é igual a H).

### 5. Desafio do estudante

```
.venv/bin/python aula_08/05_desafio.py
```

Esqueleto com `TODO` em `tau_load_rampa(t)`: o estudante deve implementar
um torque de carga em rampa (simulando o NexaBot subindo uma rampa física)
e comparar a rejeição de disturbio do PID com e sem ele, depois repetir
para H pequeno e H grande. **Enquanto o `TODO` não for preenchido, o
script termina de propósito com `NotImplementedError` e código de saída 1**
— isso é o comportamento esperado, não um bug.

## Arquivos de apoio (não são executados diretamente na aula)

- `nexabot/fmu/plant_fmu.c` — implementação em C, do zero, do FMU FMI 3.0
  de Co-Simulation. Equações e parâmetros idênticos a `nexabot/plant.py`.
  Implementa as funções FMI 3.0 realmente usadas
  (`fmi3InstantiateCoSimulation`, `fmi3EnterInitializationMode`,
  `fmi3ExitInitializationMode`, `fmi3DoStep`, `fmi3GetFloat64`,
  `fmi3SetFloat64`, `fmi3Terminate`, `fmi3FreeInstance`, `fmi3GetVersion`)
  mais os ~66 stubs obrigatórios de Model Exchange / Scheduled Execution /
  Clocks / serialização de estado que o `fmpy` resolve via `dlsym` ao
  carregar qualquer FMU FMI 3.0, mesmo sem chamá-los.
- `nexabot/fmu/headers/` — cabeçalhos FMI 3.0 oficiais
  (`fmi3Functions.h`, `fmi3FunctionTypes.h`, `fmi3PlatformTypes.h`),
  baixados de `github.com/modelica/fmi-standard` (branch `master`;
  ligeiramente mais novos que os que o `fmpy` traz embutidos — mesma
  licença BSD-2-Clause, mesmo conteúdo técnico).
- `nexabot/fmu/modelDescription.xml` — descrição FMI 3.0 do modelo (fonte
  de verdade das `valueReference`s; é copiada para dentro do `.fmu` pelo
  `build_fmu.py`, não gerada dinamicamente).
- `nexabot/fmu/build_fmu.py` — script de build (chamado pelo passo 1).
- `nexabot/fmu/verify_fmu.py` — verificação quantitativa FMU vs
  `plant.simulate` (ver seção abaixo). Não faz parte da sequência ao vivo,
  mas deve ser rodado antes da aula para garantir que o FMU está correto:

  ```
  .venv/bin/python -m nexabot.fmu.verify_fmu
  ```

  Erro relativo máximo medido: **≈ 5,5 × 10⁻¹⁰ %** em omega e
  **≈ 1,8 × 10⁻⁸ %** em corrente — ou seja, ruído de ponto flutuante, não
  um erro de modelagem. Isso é esperado: o teste aplica ao FMU e à
  referência Python a MESMA entrada em degraus (alinhada ao passo de
  comunicação H), então qualquer diferença remanescente só pode vir da
  aritmética do integrador, não do efeito de acoplamento (que é o assunto
  do passo 4).

- `nexabot/cosim.py` — mestre de co-simulação (`run_cosimulation`), usado
  pelos passos 3, 4 e 5. Carrega o FMU com a API de baixo nível do fmpy
  (`fmpy.fmi3.FMU3Slave`), **não** com `fmpy.simulate_fmu`, porque o
  controlador (`DiscretePID` de `nexabot/controllers.py`) roda fora do FMU
  e precisa intercalar suas próprias chamadas entre os passos da planta.

## Limitações conhecidas (honestidade sobre o que foi e não foi feito)

- O FMU implementa **apenas Co-Simulation** — não Model Exchange nem
  Scheduled Execution. As funções dessas duas interfaces existem no
  binário (exigidas pela introspecção do fmpy) mas devolvem `fmi3Error` /
  `NULL` de propósito.
- Não há suporte a `fmi3GetFMUState`/`fmi3SetFMUState` (checkpointing) nem
  a derivadas direcionais — o `modelDescription.xml` já declara
  `canGetAndSetFMUstate="false"` e `canSerializeFMUstate="false"`,
  coerente com os stubs em `plant_fmu.c`.
- O FMU só expõe variáveis `Float64` (`u_volts`, `tau_load`, `omega`,
  `current`, mais `time` como variável independente, exigida pela FMI
  3.0). Os getters/setters de outros tipos (Int*, UInt*, Boolean, String,
  Binary, Clock) existem apenas como stubs honestos.
- O integrador interno do FMU é RK4 de passo fixo com micro-passo
  `MICRO_DT = 5×10⁻⁵ s` (constante em `plant_fmu.c`), sub-dividido
  automaticamente quando o passo de comunicação H solicitado é maior —
  não é um solver de passo adaptativo.
- Nenhuma dessas limitações impediu a demonstração pedida: o FMU
  instancia, inicializa, avança no tempo e é lido/escrito corretamente
  pelo `fmpy`, com a planta em C reproduzindo `plant.py` dentro do erro de
  ponto flutuante.
