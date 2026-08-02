"""Dimensionamento por evidência — Unidade 4, Aula 16.

A fórmula é exatamente a mesma de `docs/dimensionamento.md` (Aula 1):

    N = ceil(taxa_de_pico / (capacidade_por_instancia * utilizacao_alvo))

O que muda nesta aula não é a fórmula — é a origem dos três insumos. Na
Aula 1, os três eram suposição: projeção de negócio para a taxa de pico,
teste de carga preliminar e isolado para a capacidade, convenção
operacional para a utilização-alvo. Quinze aulas depois, os mesmos três
insumos têm evidência real: a capacidade vem de um teste de carga de
verdade (Aula 14, e a medição ao vivo em
`services/pedidos/tests/test_dimensionamento_com_evidencias.py`), a taxa
de pico é refinada por métricas históricas (Aula 13), e a utilização-alvo
é calibrada pelo orçamento de erro (Aula 13) — ver
`docs/defesa-arquitetural.md`.
"""

from __future__ import annotations

import math


def calcular_numero_de_instancias(
    taxa_de_pico_por_segundo: float, capacidade_por_instancia: float, utilizacao_alvo: float
) -> int:
    return math.ceil(taxa_de_pico_por_segundo / (capacidade_por_instancia * utilizacao_alvo))
