#!/usr/bin/env python3
"""Aula 7 — Script 5/5: DESAFIO — o Ts candidato do firmware é aceitável?

Enunciado
---------
O time de firmware do NexaBot está pensando em compartilhar a CPU do laço
de controle com outras tarefas (leitura de sensores de segurança, telemetria
etc.) e propõe rodar o PID em um período de amostragem `Ts_candidato`
DIFERENTE do nominal de 5 ms (200 Hz) usado até aqui.

Complete `verificar_malha_para_firmware` para, dado um PID (`Kp, Ki, Kd`) e
um `Ts_candidato`:

1. Simular a malha fechada (planta contínua RK4 + PID discreto amostrado em
   `Ts_candidato`, zero-order hold entre atualizações — use o utilitário
   `simular_malha_fechada_pid` já pronto neste arquivo) para um degrau de
   referência `r` de velocidade angular, por `t_end` segundos.
2. Calcular o sobressinal percentual da resposta (`nexabot.controllers.
   step_metrics` já faz essa conta: veja a chave `'overshoot_pct'`).
3. Decidir se a malha é ESTÁVEL: `|w(t)|` NUNCA deve ultrapassar
   `fator_instabilidade` vezes a referência `r` em nenhum instante da
   simulação (mesmo critério numérico do script 02 desta aula).
4. Decidir se a malha é APROVADA: precisa ser estável E ter sobressinal
   menor ou igual a `overshoot_max_pct`.
5. Devolver um dicionário com `estavel` (bool), `overshoot_pct` (float) e
   `aprovado` (bool).

Critério de aceitação
----------------------
Rodando este script (sem argumentos) com o PID `Kp=0.5, Ki=5.0, Kd=0.0005`
(o mesmo dos scripts 02-04 desta aula), referência `r=50.0 rad/s` e
`overshoot_max_pct=20.0`, para os três `Ts_candidato` testados no `main()`
o estudante deve obter (valores medidos rodando uma implementação de
referência — ordem de grandeza esperada, não um valor exato):

- `Ts_candidato = 5 ms`  (nominal): `estavel=True`, `overshoot_pct` entre
  2% e 5%, `aprovado=True`.
- `Ts_candidato = 20 ms`: `estavel=True` (não diverge), mas `overshoot_pct`
  entre 25% e 35% — acima do limite de 20% — logo `aprovado=False`.
- `Ts_candidato = 50 ms`: `estavel=False` (a amplitude ultrapassa 3x a
  referência), logo `aprovado=False` independentemente do sobressinal.

O script IMPRIME o enunciado e, se `verificar_malha_para_firmware` ainda
não tiver sido implementada, avisa claramente o que falta — mas termina sem
lançar exceção, como convém a um esqueleto de desafio.

Como rodar
----------
    .venv/bin/python aula_07/05_desafio.py
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np  # noqa: E402

from nexabot import viz  # noqa: E402
from nexabot.controllers import DiscretePID, step_metrics  # noqa: E402
from nexabot.params import PARAMS, NexaBotParams  # noqa: E402
from nexabot.plant import derivative  # noqa: E402


def simular_malha_fechada_pid(pid, r_of_t, t_end, ts, dt_sim=None,
                               tau_load_of_t=None, p=PARAMS, x0=None, atraso_ciclos=0):
    """Planta contínua (RK4) + PID discreto amostrado a `ts`, ZOH entre
    atualizações (utilitário pronto: não precisa ser alterado)."""
    if dt_sim is None:
        dt_sim = ts / 20.0
    n_sim = int(round(t_end / dt_sim))
    n_por_ts = max(1, int(round(ts / dt_sim)))
    x = np.zeros(2) if x0 is None else np.array(x0, dtype=float)
    t_hist = np.zeros(n_sim + 1)
    X_hist = np.zeros((n_sim + 1, 2))
    U_hist = np.zeros(n_sim + 1)
    X_hist[0] = x
    u = 0.0
    fila_atraso = [0.0] * max(1, atraso_ciclos)
    for k in range(n_sim):
        tk = k * dt_sim
        if k % n_por_ts == 0:
            u_novo = pid.step(r_of_t(tk), x[1])
            if atraso_ciclos > 0:
                fila_atraso.append(u_novo)
                u = fila_atraso.pop(0)
            else:
                u = u_novo
        tl = tau_load_of_t(tk) if tau_load_of_t else 0.0
        k1 = derivative(x, u, tl, p)
        k2 = derivative(x + 0.5 * dt_sim * k1, u, tl, p)
        k3 = derivative(x + 0.5 * dt_sim * k2, u, tl, p)
        k4 = derivative(x + dt_sim * k3, u, tl, p)
        x = x + (dt_sim / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        t_hist[k + 1] = tk + dt_sim
        X_hist[k + 1] = x
        U_hist[k + 1] = u
    return t_hist, X_hist, U_hist


def verificar_malha_para_firmware(Kp: float, Ki: float, Kd: float, Ts_candidato: float,
                                   r: float = 50.0, overshoot_max_pct: float = 20.0,
                                   fator_instabilidade: float = 3.0, t_end: float = 2.0,
                                   p: NexaBotParams = PARAMS) -> dict | None:
    """TODO(estudante): implemente o veredito de aceitação do Ts candidato.

    Veja o enunciado no docstring do módulo para o passo a passo. Devolva
    `None` enquanto não estiver implementado (comportamento atual) ou o
    dicionário {'estavel':..., 'overshoot_pct':..., 'aprovado':...} quando
    a implementação estiver pronta.
    """
    # TODO: 1. simule a malha fechada com DiscretePID(Kp, Ki, Kd, Ts=Ts_candidato)
    #          e simular_malha_fechada_pid(..., t_end=t_end, ts=Ts_candidato)
    #          para uma referência em degrau r_of_t(t) = r
    # TODO: 2. calcule step_metrics(t, w, r) e extraia 'overshoot_pct'
    # TODO: 3. decida 'estavel': |w(t)| nunca ultrapassa fator_instabilidade * r
    # TODO: 4. decida 'aprovado': estavel AND overshoot_pct <= overshoot_max_pct
    # TODO: 5. devolva o dicionário com os três resultados
    return None


def main() -> int:
    print(viz.titulo("NexaBot — Aula 7 — DESAFIO: o Ts candidato do firmware é aceitável?"))
    print(__doc__.split("Como rodar")[0].strip())
    print()

    Kp, Ki, Kd = 0.5, 5.0, 0.0005
    r = 50.0
    overshoot_max_pct = 20.0
    ts_candidatos = [0.005, 0.020, 0.050]

    print(f"PID: Kp={Kp}, Ki={Ki}, Kd={Kd}; r={r:.1f} rad/s; "
          f"overshoot_max_pct={overshoot_max_pct:.1f}%.")
    print(f"Testando Ts_candidato em {[f'{t * 1000:.0f} ms' for t in ts_candidatos]}...\n")

    resultados = [verificar_malha_para_firmware(Kp, Ki, Kd, ts, r=r,
                                                 overshoot_max_pct=overshoot_max_pct)
                  for ts in ts_candidatos]

    if any(res is None for res in resultados):
        print(viz.amarelo(viz.negrito(
            "AINDA NÃO IMPLEMENTADO: verificar_malha_para_firmware() devolveu None.")))
        print("Implemente os 5 passos marcados com TODO na função acima.")
        print("\nCritério de aceitação (Kp=0.5, Ki=5.0, Kd=0.0005, r=50.0 rad/s, limite=20%):")
        viz.tabela(
            ["Ts_candidato", "estavel esperado", "overshoot_pct esperado", "aprovado esperado"],
            [
                ["5 ms", "True", "2% - 5%", "True"],
                ["20 ms", "True", "25% - 35%", "False"],
                ["50 ms", "False", "(irrelevante, instável)", "False"],
            ],
        )
        return 0

    linhas = []
    for ts, res in zip(ts_candidatos, resultados):
        linhas.append([
            f"{ts * 1000:.0f}", str(res["estavel"]), f"{res['overshoot_pct']:.2f}",
            viz.verde("True") if res["aprovado"] else viz.vermelho("False"),
        ])
    viz.tabela(
        ["Ts_candidato [ms]", "estavel", "overshoot_pct [%]", "aprovado"],
        linhas,
        titulo_tabela="Resultado do estudante",
    )

    esperado = [
        {"estavel": True, "faixa": (2.0, 5.0), "aprovado": True},
        {"estavel": True, "faixa": (25.0, 35.0), "aprovado": False},
        {"estavel": False, "faixa": None, "aprovado": False},
    ]
    dentro_esperado = True
    for res, exp in zip(resultados, esperado):
        if res["estavel"] != exp["estavel"] or res["aprovado"] != exp["aprovado"]:
            dentro_esperado = False
        if exp["faixa"] is not None and not (exp["faixa"][0] <= res["overshoot_pct"] <= exp["faixa"][1]):
            dentro_esperado = False

    if dentro_esperado:
        print(viz.verde(viz.negrito("\nDentro das faixas esperadas — desafio resolvido.")))
    else:
        print(viz.vermelho(viz.negrito("\nFora das faixas esperadas — revise os cálculos.")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
