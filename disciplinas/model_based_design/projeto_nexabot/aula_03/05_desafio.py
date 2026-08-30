#!/usr/bin/env python3
"""Aula 3 — Script 5/5: DESAFIO — encontrar o Kp de um sobressinal alvo.

Enunciado
---------
No script anterior (`04_estabilidade.py`) vimos que, em malha fechada
unitária com controlador proporcional contínuo (T(s) = Kp.G(s)/(1+Kp.G(s))),
o sobressinal da resposta ao degrau cresce continuamente com Kp — de ~0% em
Kp baixo até se aproximar de 100% para Kp muito grande.

O time de controle do NexaBot definiu um requisito de conforto de condução:
o sobressinal de velocidade não deve passar de `overshoot_alvo_pct` no laço
proporcional puro. Complete `encontrar_kp_para_overshoot` para:

1. Definir uma faixa de busca de Kp (por exemplo, [0.1, 50.0] — sabemos pelo
   script anterior que o sobressinal cresce monotonicamente com Kp nessa
   faixa, o que permite usar busca binária).
2. Para um Kp candidato, montar a malha fechada `control.feedback(Kp*G, 1)`,
   simular a resposta ao degrau (`control.step_response`) e calcular o
   sobressinal com `nexabot.controllers.step_metrics` (use como referência
   `r` o ganho DC da malha fechada, já que ele não é exatamente 1).
3. Fazer busca binária (bisseção) sobre Kp até o sobressinal calculado ficar
   dentro de `tol_pct` do alvo, ou até um número máximo de iterações.
4. Devolver um dicionário `{'kp': ..., 'overshoot_pct': ..., 'iteracoes': ...}`
   ou `None` se não convergir dentro do orçamento de iterações.

Critério de aceitação
----------------------
Rodando este script (sem argumentos) para `overshoot_alvo_pct = 20.0` e
`tol_pct = 2.0`, uma implementação de referência (bisseção sobre a mesma
faixa, checada rodando `control` de verdade antes de escrever este
enunciado) converge para:

- `kp` entre 2,4 e 3,0 (a raiz exata fica em Kp ≈ 2,71, onde o sobressinal
  é exatamente 20,0%; Kp=2,4 dá ~17,6% e Kp=3,0 dá ~22,1%, então qualquer
  Kp nesse intervalo produz sobressinal dentro da tolerância de ±2 pp);
- `overshoot_pct` entre 18,0 e 22,0 (a faixa de tolerância pedida);
- convergência em bem menos de 60 iterações de bisseção.

O script IMPRIME o enunciado e, se `encontrar_kp_para_overshoot` ainda não
tiver sido implementada, avisa claramente o que falta — mas termina sem
lançar exceção, como convém a um esqueleto de desafio.

Como rodar
----------
    .venv/bin/python aula_03/05_desafio.py
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nexabot import viz  # noqa: E402
from nexabot.controllers import step_metrics  # noqa: E402
from nexabot.params import PARAMS, NexaBotParams  # noqa: E402
from nexabot.plant import transfer_function  # noqa: E402


def encontrar_kp_para_overshoot(overshoot_alvo_pct: float, tol_pct: float = 2.0,
                                 kp_min: float = 0.1, kp_max: float = 50.0,
                                 max_iter: int = 60,
                                 p: NexaBotParams = PARAMS) -> dict | None:
    """TODO(estudante): implemente a busca binária pelo Kp do sobressinal alvo.

    Veja o enunciado no docstring do módulo para o passo a passo. Devolva
    `None` enquanto não estiver implementado (comportamento atual) ou o
    dicionário {'kp':..., 'overshoot_pct':..., 'iteracoes':...} quando a
    implementação estiver pronta e tiver convergido.
    """
    # TODO: 1. importe `control` e monte G(s) com `transfer_function(p)`.
    # TODO: 2. escreva uma função auxiliar overshoot_de(kp) que fecha a malha
    #          com control.feedback(kp*G, 1), simula o degrau e devolve o
    #          sobressinal via nexabot.controllers.step_metrics (r = ganho DC
    #          da malha fechada).
    # TODO: 3. faça bisseção em [kp_min, kp_max] até
    #          |overshoot_de(kp) - overshoot_alvo_pct| <= tol_pct
    #          (sobressinal cresce com kp nessa faixa: overshoot_de(kp_min) <
    #          alvo < overshoot_de(kp_max) precisa valer para a bisseção fazer sentido).
    # TODO: 4. devolva o dicionário com kp, o sobressinal obtido e o número de
    #          iterações usadas (ou None se estourar max_iter sem convergir).
    return None


def main() -> int:
    print(viz.titulo("NexaBot — Aula 3 — DESAFIO: encontrar Kp para um sobressinal alvo"))
    print(__doc__.split("Como rodar")[0].strip())
    print()

    overshoot_alvo_pct = 20.0
    tol_pct = 2.0
    print(f"Executando com overshoot_alvo_pct = {overshoot_alvo_pct} % e tol_pct = {tol_pct} pp...\n")

    resultado = encontrar_kp_para_overshoot(overshoot_alvo_pct, tol_pct)

    if resultado is None:
        print(viz.amarelo(viz.negrito(
            "AINDA NÃO IMPLEMENTADO (ou não convergiu): encontrar_kp_para_overshoot() devolveu None.")))
        print("Implemente os 4 passos marcados com TODO na função acima.")
        print("\nCritério de aceitação (com overshoot_alvo_pct=20.0, tol_pct=2.0):")
        viz.tabela(
            ["grandeza", "faixa esperada"],
            [
                ["kp", "2.4 - 3.0"],
                ["overshoot_pct", "18.0 - 22.0 %"],
                ["iteracoes", "< 60"],
            ],
        )
        return 0

    linhas = [
        ["kp", f"{resultado['kp']:.4f}", "(adimensional, V/rad.s^-1)"],
        ["overshoot_pct", f"{resultado['overshoot_pct']:.3f}", "%"],
        ["iteracoes", f"{resultado['iteracoes']}", "-"],
    ]
    viz.tabela(["grandeza", "valor", "unidade"], linhas, titulo_tabela="Resultado do estudante")

    # Conferência independente: fecha a malha com o Kp encontrado e reimprime
    # o sobressinal com control.step_info, como checagem cruzada.
    import control as ct
    import numpy as np

    G = transfer_function(PARAMS)
    malha_fechada = ct.feedback(resultado["kp"] * G, 1)
    dc_gain_mf = float(ct.dcgain(malha_fechada))
    t = np.linspace(0.0, 1.0, 20000)
    _, y = ct.step_response(malha_fechada, T=t)
    metrica = step_metrics(t, y, r=dc_gain_mf)
    print(f"\nConferência cruzada (step_metrics com o Kp encontrado): "
          f"overshoot = {metrica['overshoot_pct']:.3f} %")

    faixas_ok = (
        2.4 <= resultado["kp"] <= 3.0
        and 18.0 <= resultado["overshoot_pct"] <= 22.0
        and resultado["iteracoes"] < 60
    )
    if faixas_ok:
        print(viz.verde(viz.negrito("\nDentro das faixas esperadas — desafio resolvido.")))
    else:
        print(viz.vermelho(viz.negrito("\nFora das faixas esperadas — revise os cálculos.")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
