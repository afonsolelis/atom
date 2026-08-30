#!/usr/bin/env python3
"""Aula 2 — Script 4/5: validar o modelo identificado em dados NUNCA vistos no ajuste.

O que este script demonstra
----------------------------
Ajustar um modelo aos dados que o treinaram e depois checar o erro NESSES
MESMOS dados é o erro metodológico mais comum em identificação de sistemas
— e em aprendizado de máquina em geral. Este script separa as duas coisas:

1. Reproduz a identificação do `aula_02/03_identificacao.py` (mesmo ensaio,
   mesma bancada a 5 kHz) para obter os parâmetros identificados.
2. Gera um SEGUNDO ensaio, com semente aleatória e amplitude de degrau
   diferentes (dados de VALIDAÇÃO, "held-out": nunca entraram no ajuste), e
   simula a planta com os parâmetros IDENTIFICADOS (não os verdadeiros)
   reproduzindo esse novo ensaio. Compara a velocidade prevista com a
   medida usando `fit_percentual` (NRMSE estilo MATLAB `fit%`).
3. Repete a identificação, mas usando um ensaio amostrado no `Ts` do
   CONTROLADOR EMBARCADO (5 ms, 200 Hz) em vez da bancada de identificação
   (0,2 ms, 5 kHz) — e mostra que o erro no parâmetro L (indutância) piora
   em ordem de grandeza, mesmo que o `fit%` de velocidade em regime quase
   não mude. Essa é a lição central do módulo `nexabot/identificacao.py`:
   um `fit%` global aceitável pode esconder parâmetros individuais mal
   identificados quando a constante de tempo relevante (aqui, a elétrica,
   ~2,9 ms) é subamostrada.

Como rodar
----------
    .venv/bin/python aula_02/04_validacao.py
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
    fit_percentual,
    gerar_ensaio_degrau,
)
from nexabot.params import PARAMS, NexaBotParams  # noqa: E402
from nexabot.plant import simulate  # noqa: E402

FIT_MINIMO_ACEITAVEL = 70.0  # % — critério arbitrário, mas típico em identificação de sistemas


def _para_params(estim, referencia: NexaBotParams = PARAMS) -> NexaBotParams:
    """Converte um `ParametrosIdentificados` num `NexaBotParams` completo (mesmos
    limites de atuador da referência) para poder chamar `plant.simulate`."""
    return NexaBotParams(R=estim.R, L=estim.L, Ke=estim.Ke, Kt=estim.Kt, J=estim.J, b=estim.b,
                          V_max=referencia.V_max, i_max=referencia.i_max)


def main() -> int:
    print(viz.titulo("NexaBot — Aula 2 — Validação em dados held-out e o efeito da subamostragem"))

    # -- 1. reproduz a identificação de 03_identificacao.py -------------------
    print(viz.negrito("\n1) Identificação na bancada rápida (5 kHz) — mesma do script 03"))
    ensaio_treino = gerar_ensaio_degrau()  # amplitude=12 V, seed=42, ts_amostragem=2e-4 (5 kHz)
    estim_rapida = ajustar_minimos_quadrados(ensaio_treino)
    p_hat_rapida = _para_params(estim_rapida)
    print(f"  ajuste concluído (sucesso={estim_rapida.sucesso}, {estim_rapida.iteracoes} avaliações)")

    # -- 2. validação em ensaio held-out (amplitude e semente diferentes) -----
    print(viz.negrito("\n2) Validação em ensaio held-out (nunca usado no ajuste)"))
    amplitude_val = 8.0
    seed_val = 7
    print(f"  novo ensaio: amplitude = {amplitude_val:.1f} V (treino usou 12,0 V), "
          f"seed = {seed_val} (treino usou 42)")
    ensaio_val = gerar_ensaio_degrau(amplitude_v=amplitude_val, seed=seed_val)

    ts_val = float(np.median(np.diff(ensaio_val.t)))

    def u_val(t):
        return amplitude_val if t >= 0 else 0.0

    _, X_pred = simulate(u_val, t_end=float(ensaio_val.t[-1]), dt=ts_val, p=p_hat_rapida)
    n = min(len(X_pred), len(ensaio_val.t))
    fit_w = fit_percentual(ensaio_val.w_medido[:n], X_pred[:n, 1])
    fit_i = fit_percentual(ensaio_val.i_medido[:n], X_pred[:n, 0])

    viz.plot_ascii(ensaio_val.t[:n], ensaio_val.w_medido[:n], altura=12, largura=64,
                    titulo_grafico="w(t) MEDIDO no ensaio de validação (held-out, 8 V)  [rad/s]",
                    unidade_y="rad/s")
    print()
    viz.plot_ascii(ensaio_val.t[:n], X_pred[:n, 1], altura=12, largura=64,
                    titulo_grafico="w(t) PREVISTO pelo modelo identificado (mesma entrada)  [rad/s]",
                    unidade_y="rad/s")

    print()
    viz.tabela(
        ["sinal", "fit % (NRMSE)"],
        [["velocidade w(t)", f"{fit_w:.2f} %"], ["corrente i(t)", f"{fit_i:.2f} %"]],
        titulo_tabela="Ajuste do modelo identificado no ensaio held-out",
    )

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(ensaio_val.t[:n], ensaio_val.w_medido[:n], ".", markersize=2, color="#57606a",
            label="medido (held-out, 8 V)", alpha=0.6)
    ax.plot(ensaio_val.t[:n], X_pred[:n, 1], color="#1f6feb", linewidth=1.8,
            label=f"previsto pelo modelo identificado (fit={fit_w:.1f}%)")
    ax.set_xlabel("tempo [s]")
    ax.set_ylabel("velocidade w(t) [rad/s]")
    ax.set_title("NexaBot — validação em dados held-out (nunca usados no ajuste)")
    ax.grid(True, alpha=0.3)
    ax.legend()
    viz.salvar_figura(fig, "aula02_validacao_held_out.png")

    # -- 3. identificação a partir de dados amostrados no Ts do controlador ---
    print(viz.negrito("\n3) E se a identificação usasse o Ts do controlador embarcado (5 ms)?"))
    print(f"  Gerando o MESMO ensaio de treino (12 V, seed=42), mas amostrado a "
          f"Ts = {PARAMS.Ts * 1000:.1f} ms (200 Hz) em vez de 0,2 ms (5 kHz)...")
    ensaio_lento = gerar_ensaio_degrau(ts_amostragem=PARAMS.Ts)
    print(f"  {len(ensaio_lento.t)} amostras (contra {len(ensaio_treino.t)} na bancada rápida)")
    estim_lenta = ajustar_minimos_quadrados(ensaio_lento)
    p_hat_lenta = _para_params(estim_lenta)

    _, X_pred_lenta = simulate(u_val, t_end=float(ensaio_val.t[-1]), dt=ts_val, p=p_hat_lenta)
    n2 = min(len(X_pred_lenta), len(ensaio_val.t))
    fit_w_lenta = fit_percentual(ensaio_val.w_medido[:n2], X_pred_lenta[:n2, 1])
    fit_i_lenta = fit_percentual(ensaio_val.i_medido[:n2], X_pred_lenta[:n2, 0])

    linhas_rapida = {l["parametro"]: l for l in comparar_com_verdade(estim_rapida)}
    linhas_lenta = {l["parametro"]: l for l in comparar_com_verdade(estim_lenta)}

    def _fmt_erro(l):
        v = l["erro_pct"]
        txt = f"{v:+.3f} %"
        return viz.verde(txt) if abs(v) < 2.0 else viz.vermelho(txt)

    linhas_tabela = []
    for nome in ["R", "L", "Ke", "Kt", "J", "b"]:
        linhas_tabela.append([
            nome,
            _fmt_erro(linhas_rapida[nome]),
            _fmt_erro(linhas_lenta[nome]),
        ])

    viz.tabela(
        ["parâmetro", "erro % (bancada 5 kHz)", "erro % (amostrado a Ts=5 ms)"],
        linhas_tabela,
        titulo_tabela="Erro de identificação: bancada rápida vs. Ts do controlador embarcado",
    )

    nomes = ["R", "L", "Ke", "Kt", "J", "b"]
    erros_rapida = [abs(linhas_rapida[n]["erro_pct"]) for n in nomes]
    erros_lenta = [abs(linhas_lenta[n]["erro_pct"]) for n in nomes]
    posicoes = np.arange(len(nomes))
    fig, ax = plt.subplots(figsize=(7, 4))
    largura = 0.35
    ax.bar(posicoes - largura / 2, erros_rapida, largura, label="bancada 5 kHz", color="#1f6feb")
    ax.bar(posicoes + largura / 2, erros_lenta, largura, label="amostrado a Ts=5 ms", color="#d1242f")
    ax.axhline(2.0, color="#57606a", linestyle=":", linewidth=1.0, label="limiar de 2%")
    ax.set_xticks(posicoes)
    ax.set_xticklabels(nomes)
    ax.set_ylabel("erro absoluto [%]")
    ax.set_title("NexaBot — erro de identificação por parâmetro: efeito da taxa de amostragem")
    ax.grid(True, axis="y", alpha=0.3)
    ax.legend()
    viz.salvar_figura(fig, "aula02_aliasing_ts_controlador.png")
    print()
    viz.tabela(
        ["sinal", "fit % (modelo da bancada 5 kHz)", "fit % (modelo amostrado a Ts=5 ms)"],
        [
            ["velocidade w(t)", f"{fit_w:.2f} %", f"{fit_w_lenta:.2f} %"],
            ["corrente i(t)", f"{fit_i:.2f} %", f"{fit_i_lenta:.2f} %"],
        ],
        titulo_tabela="fit% no MESMO ensaio held-out, para os dois modelos identificados",
    )

    erro_L_rapida = abs(linhas_rapida["L"]["erro_pct"])
    erro_L_lenta = abs(linhas_lenta["L"]["erro_pct"])
    razao = erro_L_lenta / max(erro_L_rapida, 1e-12)

    print("\n" + viz.negrito("Ponto pedagógico central:"))
    print(f"  O erro em L salta de {erro_L_rapida:.3f}% (bancada a 5 kHz) para {erro_L_lenta:.3f}%")
    print(f"  (amostrado a Ts=5 ms) — cerca de {razao:.0f}x pior — porque a constante de tempo")
    print(f"  elétrica (tau_eletrica = {PARAMS.tau_elec * 1000:.2f} ms) fica menor que o próprio")
    print(f"  período de amostragem (Ts = {PARAMS.Ts * 1000:.1f} ms): a subida da corrente acontece")
    print("  praticamente inteira ENTRE duas amostras consecutivas, e o ajuste não tem como")
    print("  separar R de L a partir só do ponto final da subida. Note que o fit% de velocidade")
    print("  quase não muda entre os dois casos — o erro fica ESCONDIDO se você só olha um")
    print("  indicador agregado; é preciso checar os parâmetros individualmente.")

    tudo_ok = (
        estim_rapida.sucesso and estim_lenta.sucesso
        and fit_w >= FIT_MINIMO_ACEITAVEL
        and erro_L_lenta > erro_L_rapida  # o ponto pedagógico precisa realmente aparecer
    )
    if tudo_ok:
        print(viz.verde(viz.negrito(
            f"\nModelo da bancada rápida validado (fit% de w = {fit_w:.1f}% >= "
            f"{FIT_MINIMO_ACEITAVEL:g}%) e efeito de subamostragem confirmado.")))
    else:
        print(viz.vermelho(viz.negrito("\nResultado fora do esperado — revise o ensaio ou o ajuste.")))

    return 0 if tudo_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
