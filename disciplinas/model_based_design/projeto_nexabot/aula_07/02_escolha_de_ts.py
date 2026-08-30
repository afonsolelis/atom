#!/usr/bin/env python3
"""Aula 7 — Script 2/5: escolha de Ts — de "ótimo" a instável com o MESMO PID.

O que este script demonstra
----------------------------
Um único controlador PID discreto, com ganhos FIXOS (Kp, Ki, Kd nunca
mudam), é reamostrado em 18 períodos de amostragem Ts diferentes, de 0,5 ms
a 100 ms (escala log). Para cada Ts, a malha fechada (planta contínua RK4 +
PID discreto com zero-order hold entre atualizações) é simulada para um
degrau de referência de velocidade e classificada em três categorias:

  - ESTÁVEL, BOM DESEMPENHO: sobressinal baixo, resposta rápida.
  - ESTÁVEL, DEGRADADO: sobressinal alto e/ou resposta lenta, mas o sinal
    não diverge nem oscila crescendo.
  - INSTÁVEL: o sinal ultrapassa 3x a referência em algum instante, OU a
    amplitude do erro cresce de forma sustentada na segunda metade da
    simulação (oscilação crescente).

Por que um PID "próprio" e não o Ziegler-Nichols clássico calculado a partir
de Ku=3,69/Tu=18,3ms (Aula 6): TESTAMOS os ganhos clássicos de ZN
(Kp=0,6.Ku, Ki=1,2.Ku/Tu, Kd=0,075.Ku.Tu) neste degrau e eles saturam o
atuador tão fortemente (Ki muito alto) que o sobressinal já passa de 60-90%
mesmo em Ts=0,5 ms — isso mascararia o efeito de Ts, que é o que este
script quer isolar. Por isso usamos um PID mais moderado (mesma ordem de
grandeza de Kp, Ki bem menor), deixando o efeito de Ts aparecer sozinho.

Ponto pedagógico principal: o MESMO controlador que funciona muito bem a
200 Hz (Ts=5ms, a taxa do firmware do NexaBot) degrada visivelmente se o
laço de controle rodar mais devagar (ex.: um RTOS sobrecarregado, ou uma
tarefa de prioridade baixa) e pode se tornar instável para Ts grande o
suficiente — a escolha de Ts NÃO é um detalhe de implementação, é uma
decisão de projeto de controle.

Como rodar
----------
    .venv/bin/python aula_07/02_escolha_de_ts.py
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np  # noqa: E402

from nexabot import viz  # noqa: E402
from nexabot.controllers import DiscretePID, step_metrics  # noqa: E402
from nexabot.params import PARAMS  # noqa: E402
from nexabot.plant import derivative  # noqa: E402

# Ganhos FIXOS do PID usados em TODOS os Ts deste script (ver docstring do
# módulo sobre por que não são os de Ziegler-Nichols clássico).
KP_FIXO = 0.5
KI_FIXO = 5.0
KD_FIXO = 0.0005

R_REFERENCIA = 50.0     # degrau de referência de velocidade angular [rad/s]
T_END = 2.0             # duração de cada simulação [s]
FATOR_INSTABILIDADE = 3.0    # |w(t)| > FATOR_INSTABILIDADE * R => instável
LIMIAR_BOM_PCT = 10.0        # sobressinal <= este limiar => "bom desempenho"


def simular_malha_fechada_pid(pid, r_of_t, t_end, ts, dt_sim=None,
                               tau_load_of_t=None, p=PARAMS, x0=None, atraso_ciclos=0):
    """Planta contínua (RK4) + PID discreto amostrado a `ts`, ZOH entre atualizações."""
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


def classificar(t: np.ndarray, w: np.ndarray, r: float) -> tuple[str, dict]:
    """Classifica a resposta em bom / degradado / instável (critério numérico)."""
    m = step_metrics(t, w, r)
    overshoot = m["overshoot_pct"]

    instavel_amplitude = bool(np.any(np.abs(w) > FATOR_INSTABILIDADE * abs(r)))

    n = len(w)
    janela_meio = w[n // 3: 2 * n // 3]
    janela_fim = w[2 * n // 3:]
    pico_meio = float(np.max(np.abs(janela_meio - r))) if len(janela_meio) else 0.0
    pico_fim = float(np.max(np.abs(janela_fim - r))) if len(janela_fim) else 0.0
    instavel_crescendo = bool(pico_fim > 1.2 * pico_meio and pico_fim > 0.5 * abs(r))

    if instavel_amplitude or instavel_crescendo:
        return "INSTÁVEL", m
    if overshoot <= LIMIAR_BOM_PCT:
        return "bom desempenho", m
    return "degradado", m


def main() -> int:
    print(viz.titulo("NexaBot — Aula 7 — Script 2/5: escolha de Ts com PID fixo"))

    print(f"PID fixo: Kp={KP_FIXO}, Ki={KI_FIXO}, Kd={KD_FIXO}  "
          f"(mesmos ganhos em TODOS os Ts abaixo).")
    print(f"Degrau de referência: w_ref = {R_REFERENCIA:.1f} rad/s "
          f"({PARAMS.omega_to_v(R_REFERENCIA):.3f} m/s).")
    print(f"Critério de instabilidade: |w(t)| > {FATOR_INSTABILIDADE:.0f}x a referência em algum "
          f"instante, OU a amplitude do erro cresce >20% da 2a metade para o último terço.\n")

    ts_valores = np.logspace(np.log10(0.0005), np.log10(0.1), 18)

    linhas = []
    ts_bom_max = None
    ts_degradado_min = None
    ts_instavel_min = None
    for ts in ts_valores:
        pid = DiscretePID(Kp=KP_FIXO, Ki=KI_FIXO, Kd=KD_FIXO, Ts=ts)

        def r_of_t(_t, r=R_REFERENCIA):
            return r

        t, X, U = simular_malha_fechada_pid(pid, r_of_t, T_END, ts)
        w = X[:, 1]
        classe, m = classificar(t, w, R_REFERENCIA)

        if classe == "bom desempenho":
            classe_fmt = viz.verde(classe)
            ts_bom_max = ts
        elif classe == "degradado":
            classe_fmt = viz.amarelo(classe)
            if ts_degradado_min is None:
                ts_degradado_min = ts
        else:
            classe_fmt = viz.vermelho(classe)
            if ts_instavel_min is None:
                ts_instavel_min = ts

        linhas.append([
            f"{ts * 1000:.3f}", f"{1.0 / ts:.1f}", classe_fmt,
            f"{m['overshoot_pct']:.2f}", f"{m['t_settle_s'] * 1000:.1f}",
        ])

    viz.tabela(
        ["Ts [ms]", "f_amostragem [Hz]", "classificação", "sobressinal [%]", "t_acomodação [ms]"],
        linhas,
        titulo_tabela="Varredura de Ts com PID FIXO (Kp/Ki/Kd constantes)",
    )
    print(viz.negrito("  (nota: t_acomodação = 0.0 ms pode significar 'nunca saiu da faixa de 2%'"))
    print("   OU 'nunca voltou a entrar dentro da simulação' quando o sobressinal é grande —")
    print("   olhe a coluna de sobressinal e a classificação, não só esse número isolado.)\n")

    # gráfico ASCII: uma amostra "boa", uma "degradada" e uma "instável"
    ts_bom = ts_valores[0]
    ts_degradado = ts_degradado_min if ts_degradado_min is not None else ts_valores[len(ts_valores) // 2]
    ts_instavel = ts_instavel_min if ts_instavel_min is not None else ts_valores[-1]

    for ts_exemplo, rotulo in [(ts_bom, "BOM"), (ts_degradado, "DEGRADADO"), (ts_instavel, "INSTÁVEL")]:
        pid = DiscretePID(Kp=KP_FIXO, Ki=KI_FIXO, Kd=KD_FIXO, Ts=ts_exemplo)

        def r_of_t(_t, r=R_REFERENCIA):
            return r

        t, X, U = simular_malha_fechada_pid(pid, r_of_t, T_END, ts_exemplo)
        w = X[:, 1]
        viz.plot_ascii(t, w, altura=12, largura=64,
                        titulo_grafico=f"Exemplo {rotulo}: Ts = {ts_exemplo * 1000:.2f} ms",
                        y_ref=R_REFERENCIA, unidade_y="rad/s")
        print()

    # --- busca fina (bisseção) da fronteira de instabilidade ---------------
    def instavel_em(ts: float) -> bool:
        pid = DiscretePID(Kp=KP_FIXO, Ki=KI_FIXO, Kd=KD_FIXO, Ts=ts)

        def r_of_t(_t, r=R_REFERENCIA):
            return r

        _, X, _ = simular_malha_fechada_pid(pid, r_of_t, T_END, ts)
        w = X[:, 1]
        return bool(np.any(np.abs(w) > FATOR_INSTABILIDADE * abs(R_REFERENCIA)))

    lo, hi = 0.001, 0.1
    if not instavel_em(hi):
        ts_fronteira = None
    else:
        # garante um "lo" estável, retrocedendo se necessário
        while instavel_em(lo) and lo > 1.0e-5:
            lo /= 2.0
        for _ in range(25):
            mid = 0.5 * (lo + hi)
            if instavel_em(mid):
                hi = mid
            else:
                lo = mid
        ts_fronteira = 0.5 * (lo + hi)

    print(viz.negrito("Resumo da varredura:"))
    if ts_bom_max is not None:
        print(f"  - Bom desempenho até aproximadamente Ts = {ts_bom_max * 1000:.2f} ms.")
    if ts_degradado_min is not None:
        print(f"  - Degradação perceptível a partir de Ts ~ {ts_degradado_min * 1000:.2f} ms.")
    if ts_fronteira is not None:
        print(viz.vermelho(f"  - Malha vira INSTÁVEL a partir de Ts ~ {ts_fronteira * 1000:.2f} ms "
                            f"(fronteira refinada por bisseção)."))
    else:
        print("  - Nenhum Ts testado neste intervalo ficou instável pelo critério adotado.")
    print(f"\n  Para referência: Ts nominal do firmware do NexaBot = {PARAMS.Ts * 1000:.1f} ms "
          f"({1 / PARAMS.Ts:.0f} Hz) — dentro da faixa de bom desempenho encontrada acima.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
