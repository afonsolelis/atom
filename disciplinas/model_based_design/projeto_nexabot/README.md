# Projeto NexaBot — laboratório da disciplina

Laboratório executável de **Model-Based Design for Cyber-Physical Systems**. Cada uma das 16 aulas tem um diretório com scripts numerados na ordem exata em que são executados durante a videoaula.

O **NexaBot** é um veículo autoguiado (AGV) de armazém industrial, com tração por motor de corrente contínua de 24 V, redutor 20:1 e roda de 50 mm. Ele é o único sistema estudado do começo ao fim: na Aula 1 é um modelo de duas equações diferenciais; na Aula 16 é um sistema modelado, verificado formalmente, com código C gerado, testado em SIL e HIL e rastreado até o requisito de origem.

## Instalação

```bash
# uv (Linux/macOS)
curl -LsSf https://astral.sh/uv/install.sh | sh

cd projeto_nexabot
uv venv .venv
uv pip install --python .venv/bin/python \
    numpy scipy matplotlib sympy control \
    jinja2 hypothesis pytest coverage fmpy pyserial

.venv/bin/python aula_01/01_ambiente.py
```

No Windows, use `.venv\Scripts\python.exe`.

O relatório de prontidão de `aula_01/01_ambiente.py` precisa estar sem pendências antes de qualquer gravação.

## Como rodar uma aula

```bash
cd projeto_nexabot
cat aula_06/README.md                       # comandos e saída esperada
.venv/bin/python aula_06/01_ganho_critico.py
.venv/bin/python aula_06/02_ziegler_nichols.py
```

Os scripts imprimem tabelas e gráficos em ASCII, no próprio terminal, sem abrir janelas — decisão deliberada para captura de tela. As figuras PNG são geradas em paralelo, em `figuras/`, para uso no material escrito.

O último script de cada aula é sempre um **desafio**: um esqueleto com enunciado e critério de aceitação, para o estudante completar.

## Estrutura

| Caminho | Conteúdo |
| --- | --- |
| `nexabot/params.py` | Parâmetros identificados — **fonte única de verdade numérica da disciplina** |
| `nexabot/plant.py` | Planta em espaço de estados, função de transferência e integrador RK4 |
| `nexabot/controllers.py` | PID contínuo e discreto, alocação de polos, LQR, métricas de degrau |
| `nexabot/identificacao.py` | Identificação de parâmetros por mínimos quadrados |
| `nexabot/viz.py` | Tabelas e gráficos ASCII para gravação de tela |
| `nexabot/fmu/` | FMU FMI 3.0 da planta, escrito em C e compilado no próprio projeto |
| `nexabot/cosim.py` | Mestre de co-simulação planta-controlador |
| `nexabot/supervisor.py` | Máquina de estados de segurança do NexaBot |
| `nexabot/requisitos.py` | Requisitos REQ-* formalizados como propriedades verificáveis |
| `nexabot/modelcheck.py` | Verificador de estados explícitos, com contraexemplo |
| `nexabot/timed.py` | Autômato temporizado e verificação do prazo de parada |
| `nexabot/mbt.py` | Geração de casos de teste a partir do modelo |
| `nexabot/codegen/` | SymPy + Jinja2 → C, com bloco de rastreabilidade |
| `nexabot/sil.py` | Ponte *software-in-the-loop* por `ctypes` |
| `nexabot/hil.py` | Ponte *hardware-in-the-loop* (*loopback* e serial) |
| `nexabot/firmware/` | Programa do alvo e projeto PlatformIO para ESP32 |
| `nexabot/rastreabilidade.py` | Matriz requisito → modelo → código → teste |
| `aula_01/` … `aula_16/` | Laboratório por aula |
| `tests/` | Suíte `pytest` |
| `data/` | Dados de ensaio |
| `figuras/` | Figuras geradas |

## Mapa das aulas

| Unidade | Aula | Laboratório |
| --- | --- | --- |
| 1 — Modelar | 1 | Ambiente, primeira simulação, falha da malha aberta, V-Model |
| | 2 | Derivação simbólica de $A$, $B$, $C$, $D$; identificação por dados; validação |
| | 3 | Laplace, polos e zeros, Bode, margens, limite de estabilidade |
| | 4 | Controlabilidade, observabilidade, alocação de polos, LQR, observador |
| 2 — Controlar | 5 | Álgebra de blocos, rejeição de distúrbio, sensibilidade |
| | 6 | Ganho crítico, Ziegler-Nichols, ajuste fino, *anti-windup* |
| | 7 | Euler, Tustin e ZOH; escolha de $T_s$; atraso computacional; quantização |
| | 8 | Construção do FMU, co-simulação e erro de acoplamento |
| 3 — Provar | 9 | Requisitos formalizados e classificados por tipo |
| | 10 | Exploração exaustiva de estados, LTL/CTL, contraexemplo de um bug real |
| | 11 | *Watchdog* temporizado e prazo de pior caso |
| | 12 | Geração de testes a partir do modelo, cobertura, Hypothesis |
| 4 — Embarcar | 13 | Do modelo ao C, ponto fixo Q16.16, rastreabilidade no cabeçalho |
| | 14 | SIL, equivalência modelo-código, regressão, integração contínua |
| | 15 | HIL, jitter, latência de laço, *watchdog* real, ESP32 |
| | 16 | Matriz de rastreabilidade, evidências e limites da certificação |

## Conferência antes de gravar

```bash
.venv/bin/python aula_01/01_ambiente.py     # prontidão do ambiente
.venv/bin/python -m pytest -q                # suíte completa
```

Ambos precisam terminar sem falha. Em seguida, execute uma vez os scripts da aula a ser gravada e confira a saída contra o `README.md` daquele diretório.

## Nota sobre ferramentas externas

OpenModelica (Aula 8), NuSMV (Aula 10), UPPAAL (Aula 11) e PlatformIO com ESP32 (Aula 15) aparecem como contraparte industrial. **Nenhum laboratório obrigatório depende delas:** o caminho canônico de cada aula roda apenas com Python e GCC. Um estudante que não consegue instalar uma ferramenta não pode ficar sem a aula.
