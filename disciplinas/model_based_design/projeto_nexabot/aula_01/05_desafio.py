#!/usr/bin/env python3
"""Aula 1 — Script 5/5: DESAFIO — orçamento de energia de uma missão do NexaBot.

Enunciado
---------
O NexaBot recebe uma missão simples: sair do repouso, acelerar em malha
aberta com um degrau de tensão `V_missao` até o regime permanente, percorrer
uma distância `D_missao` a essa velocidade e então parar (ignore a frenagem
para este exercício: considere que ela é instantânea).

Complete `calcular_orcamento_energia` para:

1. Simular a planta do NexaBot (em malha aberta, `nexabot.plant.simulate`)
   com `V_missao` até o regime permanente.
2. Calcular a velocidade linear de regime `v_regime` (m/s).
3. Calcular o tempo de deslocamento em velocidade de regime necessário para
   cobrir `D_missao` metros (ignore a fase de aceleração na distância, para
   simplificar: assuma que ela é curta comparada à missão).
4. Calcular a energia elétrica consumida em joules durante essa fase de
   regime: `P = V_missao * i_regime` (potência elétrica de entrada), energia
   = P * tempo.
5. Devolver um dicionário com `v_regime_m_s`, `tempo_s`, `energia_j`.

Critério de aceitação
----------------------
Rodando este script (sem argumentos) para `V_missao = 18.0 V` e
`D_missao = 50.0 m`, o estudante deve obter (ordem de grandeza esperada,
não um valor exato — o objetivo é entender a conta, não decorar um número):

- `v_regime_m_s` entre 0,90 e 1,00 m/s;
- `tempo_s` entre 50 e 56 s;
- `energia_j` entre 550 e 750 J.

O script IMPRIME o enunciado e, se `calcular_orcamento_energia` ainda não
tiver sido implementada, avisa claramente o que falta — mas termina sem
lançar exceção, como convém a um esqueleto de desafio.

Como rodar
----------
    .venv/bin/python aula_01/05_desafio.py
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nexabot import viz  # noqa: E402
from nexabot.params import PARAMS, NexaBotParams  # noqa: E402


def calcular_orcamento_energia(V_missao: float, D_missao: float,
                                p: NexaBotParams = PARAMS) -> dict | None:
    """TODO(estudante): implemente o orçamento de energia da missão.

    Veja o enunciado no docstring do módulo para o passo a passo. Devolva
    `None` enquanto não estiver implementado (comportamento atual) ou o
    dicionário {'v_regime_m_s':..., 'tempo_s':..., 'energia_j':...} quando
    a implementação estiver pronta.
    """
    # TODO: 1. simule a planta em malha aberta até o regime (nexabot.plant.simulate)
    # TODO: 2. calcule v_regime a partir da velocidade angular de regime
    # TODO: 3. calcule o tempo de deslocamento para cobrir D_missao a v_regime
    # TODO: 4. calcule a energia elétrica consumida nessa fase (P = V * i, E = P * t)
    # TODO: 5. devolva o dicionário com os três resultados
    return None


def main() -> int:
    print(viz.titulo("NexaBot — Aula 1 — DESAFIO: orçamento de energia de uma missão"))
    print(__doc__.split("Como rodar")[0].strip())
    print()

    V_missao = 18.0
    D_missao = 50.0
    print(f"Executando com V_missao = {V_missao} V e D_missao = {D_missao} m...\n")

    resultado = calcular_orcamento_energia(V_missao, D_missao)

    if resultado is None:
        print(viz.amarelo(viz.negrito(
            "AINDA NÃO IMPLEMENTADO: calcular_orcamento_energia() devolveu None.")))
        print("Implemente os 5 passos marcados com TODO na função acima.")
        print("\nCritério de aceitação (com V_missao=18.0 V, D_missao=50.0 m):")
        viz.tabela(
            ["grandeza", "faixa esperada"],
            [
                ["v_regime_m_s", "0.90 - 1.00 m/s"],
                ["tempo_s", "50 - 56 s"],
                ["energia_j", "550 - 750 J"],
            ],
        )
        return 0

    linhas = [
        ["v_regime_m_s", f"{resultado['v_regime_m_s']:.4f}", "m/s"],
        ["tempo_s", f"{resultado['tempo_s']:.2f}", "s"],
        ["energia_j", f"{resultado['energia_j']:.1f}", "J"],
    ]
    viz.tabela(["grandeza", "valor", "unidade"], linhas, titulo_tabela="Resultado do estudante")

    faixas_ok = (
        0.90 <= resultado["v_regime_m_s"] <= 1.00
        and 50.0 <= resultado["tempo_s"] <= 56.0
        and 550.0 <= resultado["energia_j"] <= 750.0
    )
    if faixas_ok:
        print(viz.verde(viz.negrito("\nDentro das faixas esperadas — desafio resolvido.")))
    else:
        print(viz.vermelho(viz.negrito("\nFora das faixas esperadas — revise os cálculos.")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
