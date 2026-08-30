# Aula 15 — HIL: o alvo rodando de verdade, jitter e watchdog

Unidade 4, Aula 15: Hardware-in-the-Loop sem hardware físico. A planta roda
em Python (`nexabot.plant`); o controlador roda em um PROCESSO SEPARADO —
o C da Aula 13 compilado e executado como subprocesso (`nexabot.hil.LoopbackTarget`),
falando o mesmo protocolo de linha que um ESP32 real falaria por UART
(`nexabot.hil.SerialTarget`, não executável nesta máquina por falta de
hardware — ver `nexabot/firmware/README.md`).

## Como rodar

```bash
cd projeto_nexabot
.venv/bin/python aula_15/01_loopback_hil.py
.venv/bin/python aula_15/02_jitter.py
.venv/bin/python aula_15/03_watchdog_real.py
.venv/bin/python aula_15/04_desafio.py
```

## Scripts

| Script | O que mostra | Saída esperada (resumo) |
|---|---|---|
| `01_loopback_hil.py` | Malha fechada completa com o alvo em subprocesso: resposta a um degrau de 100 rad/s | Erro de regime permanente ~0.00% |
| `02_jitter.py` | Jitter (variação do período do laço) e latência (tempo de ida-e-volta) para 3 durações | Jitter (desvio padrão) bem abaixo de 10% de Ts em todos os casos |
| `03_watchdog_real.py` | `nexabot.hil.Watchdog` contra um alvo real que atrasa a resposta de propósito (`delay_ms` do protocolo) | Estouro só quando `delay_ms=200` > prazo; comando seguro u=0V; recuperação após reconectar |
| `04_desafio.py` | Desafio: qual o menor Ts seguro dado o jitter medido em 4 candidatos (5/2/1/0,5 ms) | Indica o menor Ts cujo atraso de pior caso respeita 20% de Ts |

## Sobre os números de jitter/latência

Os valores medidos são do laço em **Python de usuário** conversando com um
**subprocesso local por pipe**, num notebook/CI compartilhado — não de um
firmware bare-metal/RTOS num microcontrolador dedicado (que teria jitter
ordens de grandeza menor). O objetivo pedagógico é o MÉTODO de medição
(como reportar jitter e latência de um laço de controle discreto), não uma
alegação de determinismo de tempo real do ambiente de desenvolvimento.

## Pré-requisitos

`gcc` no PATH (compila `nexabot/firmware/main_loopback.c` com o PID gerado
pela Aula 13, via `nexabot.hil.LoopbackTarget`).
