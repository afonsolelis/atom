"""Tópico de tentativas de pagamento, particionado por dispositivo —
Unidade 4, Aula 15.

Reaproveita o barramento de eventos da Aula 10 (`Topico`, `escolher_particao`),
com uma chave de partição diferente da usada em `publicador.py`:
`dispositivo_id`, não `pedido_id`. É a mesma lógica de particionamento —
garantir que eventos relacionados cheguem em ordem à mesma partição —,
aplicada a uma pergunta diferente: "todas as tentativas deste dispositivo
em sequência", não "todos os eventos deste pedido".
"""

from __future__ import annotations

import math
from typing import Any

from .barramento import Topico

NOME_TOPICO_TENTATIVAS = "tentativas-pagamento"

# Números do exemplo do roteiro (Slide 7, Aula 15): pico de 5.000
# tentativas/s, capacidade comprovada de 750/s por partição.
TAXA_DE_PICO_TENTATIVAS_POR_SEGUNDO = 5_000
CAPACIDADE_POR_PARTICAO_POR_SEGUNDO = 750
NUM_PARTICOES_TENTATIVAS = math.ceil(TAXA_DE_PICO_TENTATIVAS_POR_SEGUNDO / CAPACIDADE_POR_PARTICAO_POR_SEGUNDO)


def publicar_tentativa(topico: Topico, dispositivo_id: str, payload: dict[str, Any]) -> None:
    topico.publicar(chave=dispositivo_id, tipo="TentativaDePagamento", payload=payload)
