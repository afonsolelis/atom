#!/usr/bin/env python3
"""Aula 6 — Script 1/5: ganho crítico Ku e período Tu na malha DISCRETA.

O que este script demonstra
----------------------------
O método clássico de Ziegler-Nichols pede para "aumentar o ganho proporcional
até a malha fechada oscilar de forma sustentada" e ler Ku (ganho crítico) e
Tu (período da oscilação). Só que o motor CC do NexaBot é um sistema de 2ª
ordem estritamente próprio: com controle proporcional CONTÍNUO puro e
realimentação unitária, o critério de Routh-Hurwitz é satisfeito para
QUALQUER Kp > 0 — a malha contínua NUNCA desestabiliza, então essa receita
não tem onde "pegar" em tempo contínuo.

O controlador embarcado real do NexaBot, porém, não roda em tempo contínuo:
ele amostra a Ts = 5 ms (200 Hz). Ao discretizar a planta por ZOH nesse
período, a fase extra introduzida pelo segurador de ordem zero é suficiente
para desestabilizar a malha fechada com um ganho proporcional discreto
finito. É exatamente essa malha — planta discretizada a Ts, ganho puramente
proporcional — que este script varre.

O método, passo a passo:

1. Discretiza a planta G(s) por ZOH em Ts (`control.c2d`).
2. Varre Kp e observa o maior módulo dos polos de malha fechada discreta
   `max(abs(poles(feedback(Kp*Gd, 1))))` — enquanto for < 1 a malha é
   estável; quando cruza 1, ficou marginalmente estável (fronteira).
3. Refina esse cruzamento por bisseção até `max|polo| = 1` dentro de uma
   tolerância pequena: esse Kp é o ganho crítico Ku.
4. Em Ku, o par de polos complexos dominantes está sobre o círculo unitário
   em `z = exp(j.angulo)`. O período da oscilação sustentada correspondente
   é Tu = 2.pi.Ts / |ângulo| (ângulo em radianos por amostra).
5. Para fechar o argumento visualmente, simula a malha fechada NO ganho
   crítico encontrado com um `DiscretePID(Kp=Ku, Ki=0, Kd=0)` — a lei de
   controle proporcional pura — usando o loop manual RK4 com atualização a
   cada Ts, e mostra w(t) e u(t) oscilando sem crescer nem decair.

Como rodar
----------
    .venv/bin/python aula_06/01_ganho_critico.py
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np  # noqa: E402
import control as ct  # noqa: E402

from nexabot import viz  # noqa: E402
from nexabot.params import PARAMS  # noqa: E402
from nexabot.plant import transfer_function, derivative  # noqa: E402
from nexabot.controllers import DiscretePID  # noqa: E402


def simular_malha_fechada_pid(pid, r_of_t, t_end, ts, dt_sim=None,
                               tau_load_of_t=None, p=PARAMS, x0=None):
    """Simula a malha fechada planta-contínua + PID-discreto (ZOH em Ts)."""
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


def encontrar_ganho_critico(Gd, kp_lo=0.1, kp_hi=20.0, tol=1e-9, max_iter=100):
    """Busca Ku por varredura grosseira + bisseção fina em max|polo(z)| = 1.

    Devolve (Ku, polos_em_Ku).
    """

    def max_polo(Kp):
        L = ct.feedback(Kp * Gd, 1)
        polos = ct.poles(L)
        return float(np.max(np.abs(polos))), polos

    # 1) varredura grosseira para localizar o intervalo onde a malha cruza
    #    a estabilidade (max|polo| passa de <1 para >=1).
    varredura = np.linspace(kp_lo, kp_hi, 400)
    kp_abaixo = None
    kp_acima = None
    for kp in varredura:
        m, _ = max_polo(kp)
        if m < 1.0:
            kp_abaixo = kp
        elif kp_abaixo is not None:
            kp_acima = kp
            break
    if kp_abaixo is None or kp_acima is None:
        raise RuntimeError("não foi possível localizar o cruzamento de estabilidade na varredura")

    # 2) bisseção fina dentro do intervalo [kp_abaixo, kp_acima]
    lo, hi = kp_abaixo, kp_acima
    for _ in range(max_iter):
        mid = 0.5 * (lo + hi)
        m, _ = max_polo(mid)
        if abs(m - 1.0) < tol:
            lo = hi = mid
            break
        if m < 1.0:
            lo = mid
        else:
            hi = mid
    Ku = 0.5 * (lo + hi)
    _, polos = max_polo(Ku)
    return Ku, polos


def main() -> int:
    print(viz.titulo("NexaBot — Aula 6 — Ganho crítico Ku e período Tu (malha discreta a 200 Hz)"))

    G = transfer_function(PARAMS)
    Gd = ct.c2d(G, PARAMS.Ts, method="zoh")

    print(f"Planta contínua G(s) discretizada por ZOH em Ts = {PARAMS.Ts * 1000:.1f} ms:")
    print(f"  {Gd}\n")

    Ku, polos = encontrar_ganho_critico(Gd)

    # ângulo do polo complexo dominante na fronteira de instabilidade
    angulos = [abs(np.angle(p)) for p in polos if abs(np.imag(p)) > 1e-9]
    if not angulos:
        raise RuntimeError("nenhum polo complexo encontrado em Ku — verifique a busca")
    angulo = max(angulos)
    Tu = 2.0 * np.pi * PARAMS.Ts / angulo

    viz.tabela(
        ["grandeza", "valor", "unidade"],
        [
            ["ganho crítico Ku", f"{Ku:.4f}", "adimensional"],
            ["max|polo(z)| em Ku", f"{max(abs(p) for p in polos):.6f}", "-"],
            ["polo dominante", f"{polos[0]:.4f}", "(complexo, plano z)"],
            ["ângulo do polo dominante", f"{angulo:.4f}", "rad/amostra"],
            ["período crítico Tu", f"{Tu * 1000:.3f}", "ms"],
        ],
        titulo_tabela="Resultado da busca de ganho crítico (bisseção em max|polo|=1)",
    )

    print(viz.negrito("\nComparação com o valor de referência verificado previamente:"))
    print("  Ku de referência ~= 3.69   |   Tu de referência ~= 18.3 ms")
    print(f"  Ku encontrado    = {Ku:.4f} | Tu encontrado    = {Tu * 1000:.3f} ms")

    # --- Demonstração visual: malha fechada EM Ku, controle P puro ---------
    pid_critico = DiscretePID(Kp=Ku, Ki=0.0, Kd=0.0, Ts=PARAMS.Ts, Kaw=0.0)
    w_ref = 100.0  # rad/s, referência arbitrária só para evidenciar a oscilação
    t_end = 1.0

    def r_of_t(t):
        return w_ref

    t, X, U = simular_malha_fechada_pid(pid_critico, r_of_t, t_end, PARAMS.Ts)
    w = X[:, 1]

    print(viz.titulo("Simulação em malha fechada NO ganho crítico Ku (P puro)", largura=78))
    print(f"Referência de velocidade angular: {w_ref:.0f} rad/s | Kp = Ku = {Ku:.4f}, Ki=Kd=0\n")

    viz.plot_ascii(t, w, altura=14, largura=64,
                    titulo_grafico="Velocidade angular w(t) — oscilação sustentada em Ku",
                    y_ref=w_ref, unidade_y="rad/s")
    print()
    viz.plot_ascii(t, U, altura=10, largura=64,
                    titulo_grafico="Tensão de comando u(t)", unidade_y="V")

    # janela final para checar que a amplitude não está crescendo nem morrendo
    # (descarta os primeiros 20% da simulação, que ainda contêm a subida
    # inicial a partir do repouso — não é oscilação, é transitório de partida)
    inicio = int(0.2 * len(w))
    resto = w[inicio:]
    meio = len(resto) // 2
    amp_primeira_metade = float(np.max(resto[:meio]) - np.min(resto[:meio]))
    amp_segunda_metade = float(np.max(resto[meio:]) - np.min(resto[meio:]))

    viz.tabela(
        ["grandeza", "1ª metade (pós-transitório)", "2ª metade (pós-transitório)"],
        [["amplitude pico-a-pico de w(t) [rad/s]",
          f"{amp_primeira_metade:.2f}", f"{amp_segunda_metade:.2f}"]],
        titulo_tabela="Checagem de oscilação sustentada (nem cresce, nem decai)",
    )

    fig = viz.figura_resposta_degrau(
        t, w, y_ref=w_ref,
        titulo_fig=f"NexaBot — oscilação sustentada em Ku={Ku:.3f} (P puro, Ts={PARAMS.Ts*1000:.0f} ms)",
        ylabel="velocidade angular w [rad/s]",
        nome_arquivo="aula06_ganho_critico.png",
    )
    del fig

    print(viz.negrito("\nPonto pedagógico:"))
    print("  Em tempo contínuo, Kp puro NUNCA instabiliza este motor (Routh-Hurwitz")
    print("  sempre satisfeito). É o atraso de fase introduzido pela discretização ZOH")
    print(f"  a {1.0/PARAMS.Ts:.0f} Hz que abre espaço para a oscilação sustentada em Ku — o mesmo")
    print("  efeito que aparece no controlador embarcado real do NexaBot.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
