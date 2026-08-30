#!/usr/bin/env python3
"""Aula 3 — Script 2/5: polos, zeros e a separação de escalas de tempo.

O que este script demonstra
----------------------------
G(s) do NexaBot é de 2ª ordem estritamente própria (sem zeros finitos) e tem
dois polos reais bem separados: um "rápido" (elétrico, dominado por R/L) e um
"lento" (mecânico, dominado pelo acoplamento Kt.Ke/(J.R)). O script:

1. Calcula polos/zeros com `control.poles`/`control.zeros` e confere com as
   raízes de `numpy.roots` sobre o polinômio característico.
2. Converte cada polo em constante de tempo (tau = -1/polo) e compara com as
   aproximações rápidas `PARAMS.tau_elec` (L/R) e `PARAMS.tau_mech`
   (J.R/(Kt.Ke)) — que são fórmulas de 1ª ordem desacopladas, não os polos
   exatos do sistema acoplado de 2ª ordem.
3. Mostra POR QUE a separação de ~46x entre as duas escalas de tempo permite
   aproximar o sistema por um polo dominante (o mecânico): a dinâmica
   elétrica se estabelece muito antes de a mecânica sair do lugar, então do
   ponto de vista "lento" o motor parece de 1ª ordem.
4. Quantifica o ERRO dessa aproximação: simula a resposta completa de 2ª
   ordem e a resposta do modelo reduzido de 1ª ordem (mesmo ganho DC, polo no
   mecânico) para o mesmo degrau de tensão, e mostra o erro absoluto e
   relativo ao longo do tempo — o erro é pequeno em regime, mas não nulo no
   transiente rápido, exatamente onde a dinâmica elétrica (ignorada pelo
   modelo reduzido) importa.

Como rodar
----------
    .venv/bin/python aula_03/02_polos_zeros.py
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np  # noqa: E402

from nexabot import viz  # noqa: E402
from nexabot.params import PARAMS  # noqa: E402
from nexabot.plant import transfer_function  # noqa: E402


def plot_ascii_comparacao(t, y_a, y_b, altura=15, largura=60, titulo_grafico=None,
                           rotulo_a="A", rotulo_b="B", unidade_x="s", unidade_y="") -> str:
    """Gráfico ASCII com DUAS curvas sobrepostas na mesma grade.

    `viz.plot_ascii` só desenha uma curva (mais uma linha de referência
    horizontal), então esta função local desenha as duas séries no mesmo
    plano: 'A' para `y_a`, 'B' para `y_b`, e '#' onde as duas caem na mesma
    linha da grade (curvas praticamente coincidentes naquele instante).
    """
    t = np.asarray(t, dtype=float)
    y_a = np.asarray(y_a, dtype=float)
    y_b = np.asarray(y_b, dtype=float)

    if len(t) > largura:
        idx = np.linspace(0, len(t) - 1, largura).astype(int)
        t_plot, ya_plot, yb_plot = t[idx], y_a[idx], y_b[idx]
    else:
        t_plot, ya_plot, yb_plot = t, y_a, y_b

    y_min = float(min(ya_plot.min(), yb_plot.min()))
    y_max = float(max(ya_plot.max(), yb_plot.max()))
    faixa = y_max - y_min
    if faixa < 1e-12:
        faixa = 1.0

    grade = [[" " for _ in range(len(t_plot))] for _ in range(altura)]

    def _linha_de(valor):
        frac = (valor - y_min) / faixa
        linha = int(round(frac * (altura - 1)))
        return min(max(altura - 1 - linha, 0), altura - 1)

    for c in range(len(t_plot)):
        la = _linha_de(ya_plot[c])
        lb = _linha_de(yb_plot[c])
        if la == lb:
            grade[la][c] = "#"
        else:
            grade[la][c] = "A"
            grade[lb][c] = "B"

    saida = []
    if titulo_grafico:
        saida.append(viz.negrito(titulo_grafico))
    rotulo_w = 11
    for i, linha in enumerate(grade):
        valor_eixo = y_max - (y_max - y_min) * i / (altura - 1)
        saida.append(f"{valor_eixo:>9.3g} │" + "".join(linha))
    saida.append(" " * rotulo_w + "└" + "─" * len(t_plot))
    saida.append(" " * rotulo_w + f" t: 0 .. {t_plot[-1]:.4g} {unidade_x}"
                 + (f"   y [{unidade_y}]" if unidade_y else ""))
    saida.append(" " * rotulo_w + f" A = {rotulo_a}   B = {rotulo_b}   # = curvas coincidentes")

    texto = "\n".join(saida)
    print(texto)
    return texto


def main() -> int:
    import control as ct

    print(viz.titulo("NexaBot — Aula 3 — Polos, zeros e separação de escalas de tempo"))

    G = transfer_function(PARAMS)
    polos_ct = np.array(ct.poles(G))
    zeros_ct = np.array(ct.zeros(G))

    den_coefs = [float(c) for c in G.den[0][0]]
    polos_np = np.roots(den_coefs)

    print(f"G(s) = {G}")
    print(viz.negrito("Polos (control.poles) x raízes do denominador (numpy.roots):"))
    linhas_polos = []
    for pc, pn in zip(sorted(polos_ct, key=lambda z: -abs(z.real)),
                       sorted(polos_np, key=lambda z: -abs(z.real))):
        linhas_polos.append([f"{pc.real:.4f}", f"{pn.real:.4f}", f"{abs(pc.real - pn.real):.2e}"])
    viz.tabela(["polo (control) [rad/s]", "raiz (numpy) [rad/s]", "|diferença|"], linhas_polos)

    print(f"\nZeros finitos de G(s): {list(zeros_ct) if len(zeros_ct) else '(nenhum — sistema estritamente próprio)'}")

    polos_ordenados = sorted(polos_ct.real)  # mais negativo primeiro (mais rápido)
    polo_eletrico = polos_ordenados[0]
    polo_mecanico = polos_ordenados[1]
    tau_eletrica_exata = -1.0 / polo_eletrico
    tau_mecanica_exata = -1.0 / polo_mecanico
    razao_escalas = tau_mecanica_exata / tau_eletrica_exata

    print()
    viz.tabela(
        ["grandeza", "fórmula aproximada (1ª ordem desacoplada)", "polo exato (2ª ordem)", "diferença"],
        [
            ["tau elétrica [ms]", f"{PARAMS.tau_elec * 1000:.4f}  (L/R)",
             f"{tau_eletrica_exata * 1000:.4f}", f"{abs(PARAMS.tau_elec - tau_eletrica_exata) * 1000:.4f} ms"],
            ["tau mecânica [ms]", f"{PARAMS.tau_mech * 1000:.4f}  (J.R/(Kt.Ke))",
             f"{tau_mecanica_exata * 1000:.4f}", f"{abs(PARAMS.tau_mech - tau_mecanica_exata) * 1000:.4f} ms"],
        ],
        titulo_tabela="Constantes de tempo: aproximação rápida vs polos exatos do sistema acoplado",
    )
    print(f"\nSeparação de escalas (exata, polo a polo): tau_mecanica / tau_eletrica = {razao_escalas:.1f}x")

    print("\n" + viz.negrito("Por que a separação de escalas permite reduzir a ordem do modelo:"))
    print(f"  O polo elétrico (~{polo_eletrico:.1f} rad/s) responde em poucos milissegundos —")
    print(f"  {razao_escalas:.0f}x mais rápido que o polo mecânico (~{polo_mecanico:.2f} rad/s). Do ponto de")
    print("  vista da dinâmica LENTA (velocidade do motor), a corrente já 'terminou' de reagir")
    print("  antes de a velocidade sair do lugar de forma perceptível — então, para efeitos de")
    print("  controle mecânico, o sistema PARECE de 1ª ordem, comandado só pelo polo mecânico.")

    # --- Modelo reduzido de 1a ordem (polo mecânico dominante) --------------
    dc_gain = float(ct.dcgain(G))
    G_reduzido = ct.tf([dc_gain], [tau_mecanica_exata, 1.0])

    V_degrau = 12.0
    t = np.linspace(0.0, 0.3, 3000)
    _, y_completo = ct.step_response(V_degrau * G, T=t)
    _, y_reduzido = ct.step_response(V_degrau * G_reduzido, T=t)
    erro = y_completo - y_reduzido
    erro_rel_pct = np.abs(erro) / y_completo[-1] * 100.0

    print()
    viz.plot_ascii(t, y_completo, altura=13, largura=60,
                    titulo_grafico="Modelo COMPLETO (2ª ordem) — w(t) para degrau de 12 V",
                    y_ref=y_completo[-1], unidade_y="rad/s")
    print()
    viz.plot_ascii(t, y_reduzido, altura=13, largura=60,
                    titulo_grafico="Modelo REDUZIDO (1ª ordem, polo mecânico) — w(t)",
                    y_ref=y_reduzido[-1], unidade_y="rad/s")
    print()
    plot_ascii_comparacao(t, y_completo, y_reduzido, altura=13, largura=60,
                           titulo_grafico="Sobreposição: A = completo (2ª ordem)  B = reduzido (1ª ordem)",
                           rotulo_a="completo", rotulo_b="reduzido", unidade_y="rad/s")

    idx_pico_erro = int(np.argmax(np.abs(erro)))
    amostras_t = [0.0, 0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.3]
    linhas_erro = []
    for ta in amostras_t:
        idx = int(np.argmin(np.abs(t - ta)))
        linhas_erro.append([
            f"{t[idx]:.3f}", f"{y_completo[idx]:.3f}", f"{y_reduzido[idx]:.3f}",
            f"{erro[idx]:.3f}", f"{erro_rel_pct[idx]:.3f}",
        ])
    print()
    viz.tabela(
        ["t [s]", "w completo [rad/s]", "w reduzido [rad/s]", "erro [rad/s]", "erro [%]"],
        linhas_erro,
        titulo_tabela="Erro do modelo reduzido de 1ª ordem vs modelo completo de 2ª ordem",
    )
    print(f"\nErro máximo absoluto: {np.max(np.abs(erro)):.4f} rad/s em t = {t[idx_pico_erro] * 1000:.2f} ms "
          f"(dentro da janela do transiente elétrico, tau_eletrica ~ {tau_eletrica_exata * 1000:.2f} ms).")
    print(f"Erro máximo relativo ao valor final: {np.max(erro_rel_pct):.3f} %")
    print(f"Em t = {t[-1]:.2f} s (~2 constantes de tempo mecânicas), erro residual: {erro[-1]:.4f} rad/s "
          f"({erro_rel_pct[-1]:.4f} %) — já pequeno e decrescente, tendendo a zero em regime "
          "pois os dois modelos têm o mesmo ganho DC.")

    print("\n" + viz.negrito("Ponto pedagógico:"))
    print("  O modelo reduzido de 1ª ordem é uma boa aproximação em regime e em transientes")
    print("  'lentos', mas erra sistematicamente nos primeiros milissegundos, onde a dinâmica")
    print("  elétrica (que ele descarta) ainda está ativa. Usar o modelo reduzido é uma escolha")
    print("  de engenharia válida quando o controlador não precisa reagir mais rápido que o")
    print("  polo elétrico — o que costuma valer para o laço de velocidade do NexaBot.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
