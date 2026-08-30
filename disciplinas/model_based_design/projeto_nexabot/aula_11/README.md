# Aula 11 — Autômato temporizado e o watchdog de parada de emergência

`nexabot/timed.py` modela o requisito quantitativo REQ-SAFE-006 (torque
zerado em no máximo 150 ms = 30 períodos de Ts = 5 ms) como um autômato
temporizado de tempo discreto, com relógio em número inteiro de períodos, e
verifica exaustivamente todos os caminhos possíveis (atraso de detecção do
sensor + eventual ciclo de atuação perdido).

## Comandos exatos

```bash
cd projeto_nexabot
.venv/bin/python aula_11/01_watchdog.py
.venv/bin/python aula_11/02_pior_caso.py
.venv/bin/python aula_11/03_desafio.py
```

## Saída esperada (resumo)

- **01_watchdog.py**: cenário nominal (atraso de detecção até 2 períodos +
  1 ciclo perdido); pior caso = 5 períodos = 25,0 ms, bem dentro do limite
  de 30 períodos = 150 ms (margem de 125 ms); 6 caminhos explorados
  exaustivamente.
- **02_pior_caso.py**: varre o atraso de detecção de 0 a 32 períodos; o
  REQ-SAFE-006 vale até atraso=27 períodos (pior caso = exatamente 150 ms)
  e passa a violar a partir de atraso=28 períodos (pior caso = 155 ms) —
  a fronteira exata entre um sensor seguro e um inseguro.
- **03_desafio.py**: generaliza o autômato para N ciclos de atuação
  perdidos consecutivos; com o atraso nominal de 2 períodos, o requisito
  tolera todos os cenários testados (até 6 ciclos perdidos) — evidência da
  folga de projeto do watchdog.

## Arquivos-fonte usados

- `nexabot/timed.py` — o autômato temporizado.
- `nexabot/params.py` — `Ts` e `d_stop_max`.
