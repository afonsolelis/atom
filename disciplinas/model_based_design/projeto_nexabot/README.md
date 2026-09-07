# Projeto NexaBot — laboratório da disciplina

Laboratório executável de **Model-Based Design for Cyber-Physical Systems**. Cada uma das 16 aulas tem um diretório com scripts numerados na ordem exata em que são executados durante a videoaula.

O **NexaBot** é um veículo autoguiado (AGV) de armazém industrial, com tração por motor de corrente contínua de 24 V, redutor 20:1 e roda de 50 mm. Ele é o único sistema estudado do começo ao fim: na Aula 1 é um modelo de duas equações diferenciais; na Aula 16 é um sistema modelado, verificado formalmente, com código C gerado, testado em SIL e HIL e rastreado até o requisito de origem.

## Instalação

```bash
# uv, uma vez (Linux/macOS)
curl -LsSf https://astral.sh/uv/install.sh | sh

cd projeto_nexabot
./run.sh setup
```

`./run.sh setup` cria o `.venv`, instala o projeto em modo editável (`uv pip
install -e .` — assim `import nexabot` funciona de qualquer diretório) e já
imprime o relatório de prontidão de `aula_01/01_ambiente.py`, que precisa
estar sem pendências antes de qualquer gravação. É idempotente: rodar de novo
apenas reinstala as dependências.

No Windows, use `.venv\Scripts\python.exe` diretamente (o `run.sh` pressupõe
bash).

## Como rodar uma aula

```bash
cd projeto_nexabot
./run.sh 6            # roda os scripts da aula_06 em ordem, pausando entre eles
./run.sh 6 2          # roda só o script 2 da aula_06
./run.sh 6 --direto   # a aula inteira, sem pausar
```

A pausa entre scripts (`[Enter]` segue, `q` sai) existe para gravação: dá
tempo de comentar a saída antes do próximo script. Fora de um terminal
interativo ela é ignorada automaticamente, então o mesmo comando serve em CI.

Outros comandos:

```bash
./run.sh lista        # todas as aulas e seus scripts
./run.sh testes       # só a suíte pytest
./run.sh check        # pytest + os 69 scripts, com relatório final
./run.sh todas        # as 16 aulas em sequência, sem pausa
./run.sh python -i    # atalho para .venv/bin/python
./run.sh --help
```

O `README.md` de cada aula continua sendo a referência da saída esperada
script por script:

```bash
cat aula_06/README.md
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
| `run.sh` | Executor: `setup`, uma aula, `check`, `testes` |
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
./run.sh check
```

Roda a suíte `pytest` e depois os 69 scripts das 16 aulas, terminando com um
relatório `OK / PEND / FALHA` por script e código de saída 0 somente se nada
falhou. Os `05_desafio.py` aparecem como **PEND** quando o `TODO` ainda não
foi implementado — é o enunciado funcionando, não uma quebra, e por isso não
conta como falha.

Em seguida, execute a aula a ser gravada (`./run.sh 6`) e confira a saída
contra o `README.md` daquele diretório.

## Nota sobre ferramentas externas

OpenModelica (Aula 8), NuSMV (Aula 10), UPPAAL (Aula 11) e PlatformIO com ESP32 (Aula 15) aparecem como contraparte industrial. **Nenhum laboratório obrigatório depende delas:** o caminho canônico de cada aula roda apenas com Python e GCC. Um estudante que não consegue instalar uma ferramenta não pode ficar sem a aula.
