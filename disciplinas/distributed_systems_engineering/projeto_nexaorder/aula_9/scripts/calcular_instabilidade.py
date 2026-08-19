#!/usr/bin/env python3
"""Calcula a instabilidade de cada serviço da NexaOrder — Unidade 3, Aula 9.

I = Ce / (Ca + Ce), onde Ce é o acoplamento eferente (de quantos este
serviço depende) e Ca é o acoplamento aferente (quantos dependem deste).

O grafo abaixo é declarado a partir da leitura real do código de cada
serviço — quem chama quem, via as variáveis `*_BASE_URL` configuradas em
cada `main.py` — e não é inferido automaticamente do código-fonte.

Uso: python3 scripts/calcular_instabilidade.py
"""

from __future__ import annotations

GRAFO_DE_DEPENDENCIAS: dict[str, set[str]] = {
    # gateway compõe a visão de um pedido chamando os quatro serviços
    # (services/gateway/app/main.py).
    "gateway": {"pedidos", "estoque", "pagamento", "expedicao"},
    # pedidos orquestra a saga chamando os três (services/pedidos/app/main.py).
    "pedidos": {"estoque", "pagamento", "expedicao"},
    # estoque, pagamento e expedicao não chamam nenhum outro serviço.
    "estoque": set(),
    "pagamento": set(),
    "expedicao": set(),
}


def calcular_instabilidade(grafo: dict[str, set[str]]) -> dict[str, float]:
    resultado: dict[str, float] = {}
    for servico in grafo:
        ce = len(grafo[servico])
        ca = sum(
            1
            for outro, dependencias in grafo.items()
            if outro != servico and servico in dependencias
        )
        resultado[servico] = ce / (ca + ce) if (ca + ce) else 0.0
    return resultado


def _interpretar(servico: str, instabilidade: float) -> str:
    if instabilidade <= 0.25:
        return "muito estável — contratos precisam de cuidado extra, mudanças se propagam para muitos consumidores"
    if instabilidade >= 0.75:
        return "muito instável — depende de muita coisa, deve absorver mudança melhor do que propagar"
    return "intermediário"


if __name__ == "__main__":
    resultados = calcular_instabilidade(GRAFO_DE_DEPENDENCIAS)
    for servico, instabilidade in sorted(resultados.items(), key=lambda item: item[1]):
        print(f"{servico:12s} I = {instabilidade:.2f}   {_interpretar(servico, instabilidade)}")
