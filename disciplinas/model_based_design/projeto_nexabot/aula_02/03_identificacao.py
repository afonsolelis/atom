#!/usr/bin/env python3
"""Aula 2 — Script 3/5: identificar os parâmetros do motor a partir de um ensaio.

O que este script demonstra
----------------------------
Até aqui, os valores de R, L, Ke, Kt, J e b em `nexabot/params.py` foram
tratados como dados conhecidos. Na prática, ninguém tira esses seis números
de um datasheet com essa precisão — eles vêm de um ENSAIO em bancada: aplica-
se um degrau de tensão conhecido, mede-se corrente e velocidade, e um ajuste
por mínimos quadrados recupera os parâmetros físicos que melhor explicam o
que foi medido.

Este script:

1. Gera um ensaio de degrau sintético (`nexabot.identificacao.
   gerar_ensaio_degrau`), que simula a planta *verdadeira* e adiciona ruído
   de sensor de corrente (ADC de 12 bits) e quantização de encoder — como uma
   bancada real teria. Salva o ensaio em `data/ensaio_degrau.csv` (isso
   sobrescreve o arquivo a cada execução; é o comportamento esperado).
2. Roda o ajuste por mínimos quadrados não lineares
   (`nexabot.identificacao.ajustar_minimos_quadrados`), que simula a planta
   para um candidato de parâmetros e minimiza o resíduo contra os dados
   medidos — não uma regressão linear ponto a ponto sobre as EDOs, porque
   isso amplificaria o ruído de medição ao estimar derivadas numericamente.
3. Compara cada parâmetro identificado com o valor verdadeiro
   (`nexabot.identificacao.comparar_com_verdade`) numa tabela colorida:
   verde para erro < 2%, vermelho para erro >= 2%.

Por que a bancada de identificação amostra a 5 kHz e o controlador embarcado
roda a 200 Hz? Porque a constante de tempo elétrica do motor (L/R ~= 2,9 ms)
só é visível se a amostragem for bem mais rápida do que ela: a 5 kHz
(Ts = 0,2 ms) cabem ~14 amostras dentro de uma constante de tempo elétrica,
o suficiente para o ajuste "ver" a subida da corrente e separar R de L. A
200 Hz (Ts = 5 ms) o degrau de corrente já teria terminado de subir ENTRE
duas amostras consecutivas — R e L ficam praticamente invisíveis. O
`aula_02/04_validacao.py` mostra esse efeito de forma quantitativa.

Como rodar
----------
    .venv/bin/python aula_02/03_identificacao.py
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

from nexabot import viz  # noqa: E402
from nexabot.identificacao import (  # noqa: E402
    ajustar_minimos_quadrados,
    comparar_com_verdade,
    gerar_ensaio_degrau,
)
from nexabot.params import PARAMS, NexaBotParams  # noqa: E402
from nexabot.plant import simulate  # noqa: E402

LIMIAR_ERRO_PCT = 2.0


def main() -> int:
    print(viz.titulo("NexaBot — Aula 2 — Identificação de parâmetros a partir de um ensaio de degrau"))

    # -- 1. gera e salva o ensaio sintético -----------------------------------
    print(viz.negrito("\n1) Ensaio de degrau na bancada de identificação"))
    print(f"  amplitude do degrau: 12,0 V   |   duração: 0,8 s   |   taxa de amostragem: "
          f"{1 / 2.0e-4:.0f} Hz (5 kHz)")
    ensaio = gerar_ensaio_degrau()
    caminho_csv = ensaio.salvar_csv()
    print(f"  {len(ensaio.t)} amostras geradas e salvas em {caminho_csv}")

    viz.plot_ascii(ensaio.t, ensaio.i_medido, altura=10, largura=64,
                    titulo_grafico="Corrente medida i(t) na bancada (com ruído de ADC)  [A]",
                    unidade_y="A")
    print()
    viz.plot_ascii(ensaio.t, ensaio.w_medido, altura=10, largura=64,
                    titulo_grafico="Velocidade medida w(t) na bancada (com quantização de encoder)  [rad/s]",
                    unidade_y="rad/s")

    # -- 2. ajuste por mínimos quadrados não lineares -------------------------
    print(viz.negrito("\n2) Ajuste por mínimos quadrados não lineares"))
    print("  Palpite inicial deliberadamente distante da verdade (até 60% de erro),")
    print("  como numa bancada real onde só se conhece a ordem de grandeza do motor.")
    estim = ajustar_minimos_quadrados(ensaio)
    status_convergencia = viz.verde("convergiu") if estim.sucesso else viz.vermelho("NÃO convergiu")
    print(f"  scipy.optimize.least_squares: {status_convergencia} em {estim.iteracoes} avaliações "
          f"da função de resíduo.")

    # -- 3. compara com a verdade ---------------------------------------------
    print(viz.negrito("\n3) Parâmetros identificados vs. parâmetros verdadeiros"))
    linhas_comparacao = comparar_com_verdade(estim, p=PARAMS)

    linhas_tabela = []
    todos_abaixo_limiar = True
    for l in linhas_comparacao:
        erro_abs = abs(l["erro_pct"])
        ok = erro_abs < LIMIAR_ERRO_PCT
        todos_abaixo_limiar &= ok
        erro_fmt = f"{l['erro_pct']:+.4f} %"
        erro_colorido = viz.verde(erro_fmt) if ok else viz.vermelho(erro_fmt)
        linhas_tabela.append([
            l["parametro"], l["unidade"], f"{l['verdadeiro']:.6g}", f"{l['identificado']:.6g}",
            erro_colorido,
        ])

    viz.tabela(
        ["parâmetro", "unidade", "valor verdadeiro", "valor identificado", "erro %"],
        linhas_tabela,
        titulo_tabela=f"Identificação vs. verdade (limiar de aceitação: {LIMIAR_ERRO_PCT:g}%)",
        alinhamentos=["e", "e", "d", "d", "d"],
    )

    # -- figura: dados medidos vs. modelo com os parâmetros identificados -----
    p_hat = NexaBotParams(R=estim.R, L=estim.L, Ke=estim.Ke, Kt=estim.Kt, J=estim.J, b=estim.b,
                           V_max=PARAMS.V_max, i_max=PARAMS.i_max)
    ts_ensaio = float(np.median(np.diff(ensaio.t)))

    def u_ensaio(t):
        return float(ensaio.V[0]) if t >= 0 else 0.0

    _, X_hat = simulate(u_ensaio, t_end=float(ensaio.t[-1]), dt=ts_ensaio, p=p_hat)
    n = min(len(X_hat), len(ensaio.t))

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(7, 6), sharex=True)
    ax1.plot(ensaio.t[:n], ensaio.i_medido[:n], ".", markersize=2, color="#57606a",
             label="medido (bancada)", alpha=0.6)
    ax1.plot(ensaio.t[:n], X_hat[:n, 0], color="#1f6feb", linewidth=1.8, label="modelo identificado")
    ax1.set_ylabel("corrente i(t) [A]")
    ax1.set_title("NexaBot — identificação: dados medidos x modelo ajustado")
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    ax2.plot(ensaio.t[:n], ensaio.w_medido[:n], ".", markersize=2, color="#57606a",
             label="medido (bancada)", alpha=0.6)
    ax2.plot(ensaio.t[:n], X_hat[:n, 1], color="#1f6feb", linewidth=1.8, label="modelo identificado")
    ax2.set_xlabel("tempo [s]")
    ax2.set_ylabel("velocidade w(t) [rad/s]")
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    viz.salvar_figura(fig, "aula02_identificacao_ajuste.png")

    print("\n" + viz.negrito("Por que amostrar a 5 kHz na bancada, e não a 200 Hz do controlador?"))
    print(f"  Constante de tempo elétrica real: tau_eletrica = L/R = {PARAMS.tau_elec * 1000:.3f} ms.")
    print(f"  A 5 kHz (0,2 ms/amostra) cabem ~{PARAMS.tau_elec / 2.0e-4:.1f} amostras por tau_eletrica —")
    print(f"  dá para ver a subida da corrente. A 200 Hz (Ts = {PARAMS.Ts * 1000:.1f} ms, o Ts do")
    print(f"  controlador embarcado) caberia só ~{PARAMS.tau_elec / PARAMS.Ts:.2f} amostra por tau_eletrica:")
    print("  R e L ficam praticamente invisíveis no sinal amostrado (veja aula_02/04_validacao.py).")

    if todos_abaixo_limiar:
        print(viz.verde(viz.negrito(
            f"\nTodos os parâmetros identificados com erro < {LIMIAR_ERRO_PCT:g}%.")))
    else:
        print(viz.vermelho(viz.negrito(
            f"\nAlgum parâmetro ficou com erro >= {LIMIAR_ERRO_PCT:g}% — revise o ensaio ou o ajuste.")))

    return 0 if (estim.sucesso and todos_abaixo_limiar) else 1


if __name__ == "__main__":
    raise SystemExit(main())
