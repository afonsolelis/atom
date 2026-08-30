# Firmware do alvo HIL — NexaBot

Duas implementações do mesmo protocolo de linha, para os dois back-ends de
`nexabot.hil` (Aula 15):

| Arquivo | Back-end | Roda neste ambiente? |
|---|---|---|
| `main_loopback.c` | `LoopbackTarget` (subprocesso local) | **Sim** — compilado com `gcc`, sem hardware |
| `platformio.ini` + `src/main.cpp` | `SerialTarget` (ESP32 real) | **Não** — exige PlatformIO + placa física |

## `main_loopback.c` (roda de verdade aqui)

Compilado automaticamente por `nexabot.hil.LoopbackTarget` a partir do C
gerado na Aula 13 (`nexabot/codegen/generate.py`). Para compilar e testar
manualmente, fora do Python:

```bash
cd projeto_nexabot
.venv/bin/python -m nexabot.codegen.generate   # gera nexabot/codegen/generated/pid_controller.{c,h}
gcc -std=c11 -O2 -I nexabot/codegen/generated \
    nexabot/firmware/main_loopback.c \
    nexabot/codegen/generated/pid_controller.c \
    -o /tmp/loopback_target -lm

# protocolo por stdin/stdout: STEP r y / RESET / QUIT -> U u / OK
printf 'STEP 3.0 0.0\nRESET\nQUIT\n' | /tmp/loopback_target 2.0 40.0 0.02 0.005 24.0 0.01 1.0
```

Saída esperada (a tensão exata depende dos ganhos passados):

```
U 10.6
OK
```

## `platformio.ini` + `src/main.cpp` (ESP32 real, requer hardware)

**Não compila nesta máquina de desenvolvimento** — não há toolchain
Xtensa/PlatformIO instalada aqui, só `gcc` do host (usado só pelo
`LoopbackTarget`). Para gravar em um ESP32 de verdade, na máquina do
estudante, com a placa conectada por USB:

```bash
pip install platformio     # uma vez
cd nexabot/firmware
pio run                    # compila
pio run -t upload          # grava no ESP32
pio device monitor -b 115200   # abre o terminal serial (mesmo protocolo)
```

O núcleo PID em `src/main.cpp` é uma cópia sincronizada à mão da variante
em `double` gerada pela Aula 13 (mesmo contrato numérico de
`DiscretePID.step`) — ver o comentário no topo do arquivo para o
procedimento de resincronização quando os ganhos do modelo mudarem.

## Protocolo de linha (comum aos dois back-ends)

```
host -> alvo:  STEP <r> <y> [delay_ms]
host -> alvo:  RESET
host -> alvo:  QUIT              (loopback só; ESP32 ignora)
alvo -> host:  U <u>
alvo -> host:  OK
```

`delay_ms` é opcional e só existe para o experimento de watchdog da Aula 15
(`nexabot.hil.Watchdog`): pede ao alvo que atrase a resposta propositalmente,
simulando um laço lento sem precisar travar o processo de verdade.
