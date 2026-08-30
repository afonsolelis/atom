#!/usr/bin/env python3
"""Aula 5 — Script 4/4: DESAFIO — sintonize um PID para rejeitar um distúrbio de carga.

Enunciado
---------
O NexaBot está de cruzeiro a 1,0 m/s (400 rad/s no motor) quando, em
t = 0,15 s, um palete extra é colocado sobre ele: um DEGRAU de torque de
carga equivalente a 33% do torque nominal do motor (`0.33 * Kt * i_max`) —
próximo do limite que o atuador de 24 V ainda consegue compensar em regime
permanente, então a malha não tem folga de sobra.

Complete `ajustar_pid_para_disturbio` para:

1. Escolher manualmente `Kp`, `Ki`, `Kd` (por tentativa e erro — comece pelos
   valores do script 2, `Kp=2.0, Ki=50.0, Kd=0.001`, e ajuste).
2. Montar um `DiscretePID(Kp, Ki, Kd, Ts=PARAMS.Ts, u_max=PARAMS.V_max)`,
   inicializando `pid.integral = V_regime` (o robô já estava de cruzeiro).
3. Simular a malha fechada sob o cenário de distúrbio acima usando
   `simular_malha_fechada_pid` (utilitário já definido neste arquivo — o
   mesmo padrão RK4 + PID amostrado a `Ts` dos scripts 2 e 3).
4. Calcular `erro_regime_pct` (erro percentual de velocidade ao final da
   simulação), `overshoot_pct` (pico acima do alvo, em %) e
   `tempo_recuperacao_s` (tempo, a partir do distúrbio, até a velocidade
   voltar e permanecer dentro de ±2% do alvo — reaproveite
   `tempo_recuperacao`, também já definida neste arquivo).
5. Devolver um dicionário com `Kp`, `Ki`, `Kd`, `erro_regime_pct`,
   `overshoot_pct`, `tempo_recuperacao_s`.

Critério de aceitação
----------------------
Rodando este script (sem argumentos), o estudante deve obter (faixas
verificadas rodando uma implementação de referência com
Kp=2.0, Ki=50.0, Kd=0.001 — outras escolhas de ganho também podem passar):

- `erro_regime_pct` entre 0,00 e 0,05 %;
- `overshoot_pct` entre 0,00 e 3,00 %;
- `tempo_recuperacao_s` entre 0,00 e 0,02 s (20 ms) — ganhos "fracos"
  (ex.: Kp=0.2, Ki=5, Kd=0) recuperam em ~85 ms e FALHAM esse critério.

O script IMPRIME o enunciado e, se `ajustar_pid_para_disturbio` ainda não
tiver sido implementada, avisa claramente o que falta — mas termina sem
lançar exceção, como convém a um esqueleto de desafio.

Como rodar
----------
    .venv/bin/python aula_05/04_desafio.py
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np  # noqa: E402

from nexabot import viz  # noqa: E402
from nexabot.controllers import DiscretePID  # noqa: E402
from nexabot.params import PARAMS, NexaBotParams  # noqa: E402
from nexabot.plant import derivative  # noqa: E402

# --------------------------------------------------------------------------
# Utilitários locais (mesmo padrão dos scripts 2 e 3 deste diretório)
# --------------------------------------------------------------------------


def simular_malha_fechada_pid(pid, r_of_t, t_end, ts, dt_sim=None,
                               tau_load_of_t=None, p=PARAMS, x0=None):
    """Integra a planta em malha fechada com um `DiscretePID` amostrado a `ts`."""
    if dt_sim is None:
        dt_sim = ts / 10.0
    n_sim = int(round(t_end / dt_sim))
    n_por_ts = max(1, int(round(ts / dt_sim)))
    x = np.zeros(2) if x0 is None else np.array(x0, dtype=float)
    t_hist = np.zeros(n_sim + 1)
    X_hist = np.zeros((n_sim + 1, 2))
    U_hist = np.zeros(n_sim + 1)
    X_hist[0] = x
    u = 0.0
    for k in range(n_sim):
        tk = k * dt_sim
        if k % n_por_ts == 0:
            u = pid.step(r_of_t(tk), x[1])
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


def tempo_recuperacao(t, omega, omega_alvo, t_disturbio, banda=0.02):
    """Tempo, a partir de `t_disturbio`, até `omega` voltar e permanecer

    dentro de `banda` (fração) do alvo. `0.0` se nunca saiu da faixa;
    `None` se nunca volta a entrar dentro da janela simulada.
    """
    mask = t >= t_disturbio
    tt = t[mask]
    erro_rel = np.abs(omega[mask] - omega_alvo) / omega_alvo
    fora = np.where(erro_rel > banda)[0]
    if len(fora) == 0:
        return 0.0
    ultimo_fora = fora[-1]
    if ultimo_fora + 1 >= len(tt):
        return None
    return float(tt[ultimo_fora + 1] - t_disturbio)


# --------------------------------------------------------------------------
# Cenário fixo do desafio (não altere: é o que o critério de aceitação usa)
# --------------------------------------------------------------------------

V_ALVO_M_S = 1.0
T_DISTURBIO_S = 0.15
T_END_S = 0.6
FRACAO_TORQUE_NOMINAL = 0.33


def ajustar_pid_para_disturbio(p: NexaBotParams = PARAMS) -> dict | None:
    """TODO(estudante): sintonize Kp, Ki, Kd para rejeitar o distúrbio de carga.

    Veja o enunciado no docstring do módulo para o passo a passo e o
    cenário de distúrbio (33% do torque nominal em t=0,15 s). Devolva
    `None` enquanto não estiver implementado (comportamento atual) ou o
    dicionário {'Kp':..., 'Ki':..., 'Kd':..., 'erro_regime_pct':...,
    'overshoot_pct':..., 'tempo_recuperacao_s':...} quando pronto.
    """
    # TODO: 1. escolha Kp, Ki, Kd manualmente (comece por Kp=2.0, Ki=50.0, Kd=0.001)
    # TODO: 2. monte pid = DiscretePID(Kp, Ki, Kd, Ts=p.Ts, u_max=p.V_max) e
    #          inicialize pid.integral = V_regime (tensão de regime sem carga)
    # TODO: 3. simule com simular_malha_fechada_pid sob o cenário de distúrbio
    #          (tau_load = FRACAO_TORQUE_NOMINAL * p.Kt * p.i_max em t=T_DISTURBIO_S)
    # TODO: 4. calcule erro_regime_pct, overshoot_pct e tempo_recuperacao_s
    # TODO: 5. devolva o dicionário com Kp, Ki, Kd e as três métricas
    return None


def main() -> int:
    print(viz.titulo("NexaBot — Aula 5 — DESAFIO: sintonize um PID contra distúrbio de carga"))
    print(__doc__.split("Como rodar")[0].strip())
    print()

    tau_load = FRACAO_TORQUE_NOMINAL * PARAMS.Kt * PARAMS.i_max
    print(f"Executando com v_alvo={V_ALVO_M_S} m/s, distúrbio de "
          f"{FRACAO_TORQUE_NOMINAL * 100:.0f}% do torque nominal "
          f"({tau_load * 1000:.1f} mN.m) em t={T_DISTURBIO_S} s...\n")

    resultado = ajustar_pid_para_disturbio()

    if resultado is None:
        print(viz.amarelo(viz.negrito(
            "AINDA NÃO IMPLEMENTADO: ajustar_pid_para_disturbio() devolveu None.")))
        print("Implemente os 5 passos marcados com TODO na função acima.")
        print("\nCritério de aceitação (distúrbio de 33% do torque nominal em t=0,15 s):")
        viz.tabela(
            ["grandeza", "faixa esperada"],
            [
                ["erro_regime_pct", "0,00 - 0,05 %"],
                ["overshoot_pct", "0,00 - 3,00 %"],
                ["tempo_recuperacao_s", "0,00 - 0,02 s (20 ms)"],
            ],
        )
        return 0

    linhas = [
        ["Kp", f"{resultado['Kp']:.4f}", "-"],
        ["Ki", f"{resultado['Ki']:.4f}", "-"],
        ["Kd", f"{resultado['Kd']:.4f}", "-"],
        ["erro_regime_pct", f"{resultado['erro_regime_pct']:.4f}", "%"],
        ["overshoot_pct", f"{resultado['overshoot_pct']:.4f}", "%"],
        ["tempo_recuperacao_s", f"{resultado['tempo_recuperacao_s']:.4f}", "s"],
    ]
    viz.tabela(["grandeza", "valor", "unidade"], linhas, titulo_tabela="Resultado do estudante")

    faixas_ok = (
        0.00 <= resultado["erro_regime_pct"] <= 0.05
        and 0.00 <= resultado["overshoot_pct"] <= 3.00
        and 0.00 <= resultado["tempo_recuperacao_s"] <= 0.02
    )
    if faixas_ok:
        print(viz.verde(viz.negrito("\nDentro das faixas esperadas — desafio resolvido.")))
    else:
        print(viz.vermelho(viz.negrito("\nFora das faixas esperadas — ajuste Kp, Ki, Kd e rode de novo.")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
