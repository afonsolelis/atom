#!/usr/bin/env python3
"""Aula 4 — Script 5/5: DESAFIO — projete um K que atenda dois requisitos ao mesmo tempo.

Enunciado
---------
A equipe de engenharia do NexaBot definiu dois requisitos para o eixo de
tração, para a manobra "acelerar de repouso até 400 rad/s (1,0 m/s)":

  REQ-A (desempenho): tempo de acomodação (banda de 2%) da resposta REAL da
         malha fechada — ou seja, já com a tensão saturada em ±V_max=24 V —
         deve ser NO MÁXIMO 300 ms.
  REQ-B (esforço do atuador): o pico da tensão pedida pela lei de controle
         IDEAL (antes de saturar, u(t) = -K.x(t) + Nbar.r) deve ser NO
         MÁXIMO 150 V — ou seja, o projeto não pode pedir "milhares de
         volts" como o cenário agressivo do script 2 desta aula.

Complete `encontrar_ganho_que_atende_requisitos` para:

1. Escolher uma estratégia de projeto: alocação de polos
   (`nexabot.controllers.state_feedback_gain(poles)`) OU LQR
   (`nexabot.controllers.lqr_gain(Q, R)`).
2. Calcular a pré-compensação Nbar = 1 / (C.(-(A-B.K))^-1.B).
3. Simular a malha fechada REAL (RK4 manual, `nexabot.plant.derivative`,
   saturando u em ±PARAMS.V_max) para uma referência degrau `x_ref`.
4. Calcular as métricas com `nexabot.controllers.step_metrics` sobre a
   velocidade REAL, e o pico de |u(t)| da lei IDEAL (sem saturar) simulada
   em paralelo com o MESMO K e Nbar.
5. Devolver um dicionário com `tipo` ("polos" ou "lqr"), `parametros`
   (a lista de polos ou o par (Q, R) escolhido), `K`, `overshoot_pct`,
   `t_settle_s`, `u_peak_V`, `steady_state_error` e `atende_requisitos`
   (bool: True se REQ-A e REQ-B forem satisfeitos simultaneamente).

Critério de aceitação
----------------------
Existe pelo menos uma solução válida — verificada rodando de fato uma
implementação de referência por alocação de polos em [-700, -20] rad/s
(o cenário "moderado" do script 2 desta aula) — com estas métricas:

- `overshoot_pct` entre -5% e +5% (praticamente sem sobressinal);
- `t_settle_s` entre 0,20 e 0,30 s (dentro do limite de REQ-A);
- `u_peak_V` entre 80 e 150 V (dentro do limite de REQ-B);
- `steady_state_error` entre 0 e 8 rad/s (erro de regime pequeno, < 2% de
  400 rad/s, mesmo sob saturação leve).

O objetivo não é reproduzir exatamente esses números (o estudante pode
escolher outros polos, ou LQR, e chegar a uma solução diferente e igualmente
válida) — é entender que REQ-A e REQ-B empurram o projeto em direções
opostas (mais rápido pede mais tensão) e que existe uma região do espaço de
projeto onde os dois cabem ao mesmo tempo.

O script IMPRIME o enunciado e, se a função ainda não tiver sido
implementada, avisa claramente o que falta — mas termina sem lançar
exceção, como convém a um esqueleto de desafio.

Como rodar
----------
    .venv/bin/python aula_04/05_desafio.py
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np  # noqa: E402

from nexabot import viz  # noqa: E402
from nexabot.params import PARAMS, NexaBotParams  # noqa: E402
from nexabot.plant import state_space_matrices, derivative  # noqa: E402
from nexabot.controllers import state_feedback_gain, lqr_gain, step_metrics  # noqa: E402


def encontrar_ganho_que_atende_requisitos(
    t_settle_max_s: float = 0.30,
    u_peak_max_V: float = 150.0,
    x_ref: float = 400.0,
    p: NexaBotParams = PARAMS,
) -> dict | None:
    """TODO(estudante): projete K (alocação de polos OU LQR) que satisfaça REQ-A e REQ-B.

    Veja o enunciado no docstring do módulo para o passo a passo. Devolva
    `None` enquanto não estiver implementado (comportamento atual) ou o
    dicionário {'tipo':..., 'parametros':..., 'K':..., 'overshoot_pct':...,
    't_settle_s':..., 'u_peak_V':..., 'steady_state_error':...,
    'atende_requisitos':...} quando a implementação estiver pronta.
    """
    # TODO: 1. escolha polos de malha fechada (state_feedback_gain) ou pesos
    #          Q, R (lqr_gain) e calcule K
    # TODO: 2. calcule Nbar = 1 / (C.(-(A-B.K))^-1.B)
    # TODO: 3. simule a malha fechada REAL (saturada em ±p.V_max) via RK4
    #          manual com nexabot.plant.derivative, para referência x_ref
    # TODO: 4. calcule as métricas (step_metrics) e o pico de |u(t)| da lei
    #          IDEAL (sem saturar) com o mesmo K, Nbar
    # TODO: 5. devolva o dicionário com tipo, parametros, K e as métricas,
    #          incluindo 'atende_requisitos' = (t_settle_s <= t_settle_max_s
    #          and u_peak_V <= u_peak_max_V)
    return None


# --------------------------------------------------------------------------
# Infraestrutura de simulação usada pelo verificador do desafio (main()).
# O estudante pode reaproveitar estas duas funções dentro da sua solução.
# --------------------------------------------------------------------------

def ganho_pre_compensacao(A: np.ndarray, B: np.ndarray, C: np.ndarray, K: np.ndarray) -> float:
    """Calcula Nbar = 1 / (C.(-(A-B.K))^-1.B) para erro nulo de regime em y=r."""
    A_malha_fechada = A - B @ K
    M = -C @ np.linalg.inv(A_malha_fechada) @ B
    return float(1.0 / M[0, 0])


def simular_malha_fechada_estados(K: np.ndarray, Nbar: float, x_ref: float,
                                   t_end: float, dt: float = 1.0e-5,
                                   saturar: bool = True, p: NexaBotParams = PARAMS):
    """Simula x_dot = A.x + B.u, u = -K.x + Nbar.r, via RK4 manual. Devolve (t, X, U)."""
    n = int(round(t_end / dt))
    t = np.linspace(0.0, n * dt, n + 1)
    X = np.zeros((n + 1, 2))
    U = np.zeros(n + 1)
    x = np.zeros(2)
    for k in range(n):
        u_ideal = float((-K @ x + Nbar * x_ref).item())
        u = float(np.clip(u_ideal, -p.V_max, p.V_max)) if saturar else u_ideal
        U[k] = u
        k1 = derivative(x, u, 0.0, p)
        k2 = derivative(x + 0.5 * dt * k1, u, 0.0, p)
        k3 = derivative(x + 0.5 * dt * k2, u, 0.0, p)
        k4 = derivative(x + dt * k3, u, 0.0, p)
        x = x + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        X[k + 1] = x
    U[-1] = U[-2]
    return t, X, U


def main() -> int:
    print(viz.titulo("NexaBot — Aula 4 — DESAFIO: um K só, dois requisitos simultâneos"))
    print(__doc__.split("Como rodar")[0].strip())
    print()

    t_settle_max_s = 0.30
    u_peak_max_V = 150.0
    x_ref = 400.0
    print(f"Executando com t_settle_max_s = {t_settle_max_s} s, "
          f"u_peak_max_V = {u_peak_max_V} V, x_ref = {x_ref:.0f} rad/s...\n")

    resultado = encontrar_ganho_que_atende_requisitos(t_settle_max_s, u_peak_max_V, x_ref)

    if resultado is None:
        print(viz.amarelo(viz.negrito(
            "AINDA NÃO IMPLEMENTADO: encontrar_ganho_que_atende_requisitos() devolveu None.")))
        print("Implemente os 5 passos marcados com TODO na função acima.")
        print("\nCritério de aceitação (faixas de uma solução de referência válida, "
              "por alocação de polos em [-700, -20] rad/s):")
        viz.tabela(
            ["grandeza", "faixa esperada"],
            [
                ["overshoot_pct", "-5% a +5%"],
                ["t_settle_s", "0.20 - 0.30 s  (REQ-A: <= 0.30 s)"],
                ["u_peak_V", "80 - 150 V  (REQ-B: <= 150 V)"],
                ["steady_state_error", "0 - 8 rad/s  (< 2% de 400 rad/s)"],
            ],
        )
        return 0

    linhas = [
        ["tipo", str(resultado["tipo"]), "-"],
        ["parametros", str(resultado["parametros"]), "-"],
        ["K", str(np.asarray(resultado["K"]).round(4).tolist()), "-"],
        ["overshoot_pct", f"{resultado['overshoot_pct']:.3f}", "%"],
        ["t_settle_s", f"{resultado['t_settle_s']:.4f}", "s"],
        ["u_peak_V", f"{resultado['u_peak_V']:.2f}", "V"],
        ["steady_state_error", f"{resultado['steady_state_error']:.4f}", "rad/s"],
    ]
    viz.tabela(["grandeza", "valor", "unidade"], linhas, titulo_tabela="Resultado do estudante")

    req_a_ok = resultado["t_settle_s"] <= t_settle_max_s
    req_b_ok = resultado["u_peak_V"] <= u_peak_max_V
    atende = bool(resultado.get("atende_requisitos", req_a_ok and req_b_ok))

    print()
    viz.tabela(
        ["requisito", "limite", "obtido", "resultado"],
        [
            ["REQ-A: t_settle_s <= limite", f"{t_settle_max_s:.2f} s",
             f"{resultado['t_settle_s']:.4f} s",
             viz.verde("OK") if req_a_ok else viz.vermelho("FALHOU")],
            ["REQ-B: u_peak_V <= limite", f"{u_peak_max_V:.1f} V",
             f"{resultado['u_peak_V']:.2f} V",
             viz.verde("OK") if req_b_ok else viz.vermelho("FALHOU")],
        ],
        titulo_tabela="Verificação dos dois requisitos simultâneos",
    )

    if atende and req_a_ok and req_b_ok:
        print(viz.verde(viz.negrito("\nOs dois requisitos foram atendidos simultaneamente — desafio resolvido.")))
    else:
        print(viz.vermelho(viz.negrito(
            "\nAo menos um requisito não foi atendido — ajuste os polos ou (Q, R) e tente de novo.")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
