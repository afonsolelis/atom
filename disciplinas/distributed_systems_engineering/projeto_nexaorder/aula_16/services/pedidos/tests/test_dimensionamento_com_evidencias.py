"""Unidade 4, Aula 16 — fecha o arco aberto em `docs/dimensionamento.md`
desde a Aula 1: "A Aula 16 recalcula os mesmos números com evidências
operacionais reais". A fórmula (`services/../scripts/dimensionamento_com_evidencias.py`)
não muda; o que muda é que a capacidade por instância, aqui, é MEDIDA por
este próprio teste — não hardcoded como se fosse uma medição — batendo em
`POST /pedidos` de verdade, e não suposta como na Aula 1.

Ressalva idêntica à da Aula 14: este ambiente (SQLite em processo, sem
rede real) não é representativo de produção — o número medido aqui serve
para provar que o cálculo agora roda sobre dado medido, não para afirmar
qual é a capacidade real de um `pedidos` em produção."""

from __future__ import annotations

import math
import time
import uuid


def _corpo_pedido() -> dict:
    return {
        "cliente_id": str(uuid.uuid4()),
        "chave_idempotencia": str(uuid.uuid4()),
        "itens": [{"sku": "TECLADO-MEC-01", "quantidade": 1, "preco_unitario": 349.90}],
    }


def test_capacidade_medida_ao_vivo_recalcula_o_numero_de_instancias_da_aula_1(cliente_api):
    num_requisicoes = 30
    inicio = time.perf_counter()
    for _ in range(num_requisicoes):
        resposta = cliente_api.post("/pedidos", json=_corpo_pedido())
        assert resposta.status_code == 201
    duracao_s = time.perf_counter() - inicio

    capacidade_medida_req_por_s = num_requisicoes / duracao_s
    assert capacidade_medida_req_por_s > 0  # a medição produziu um número real, não suposto

    # Mesma fórmula de docs/dimensionamento.md e scripts/dimensionamento_com_evidencias.py
    # (N = ceil(taxa_pico / (capacidade * utilização_alvo))); taxa de pico e
    # utilização-alvo continuam os mesmos insumos da Aula 1 — só a
    # capacidade deixou de ser suposição.
    numero_de_instancias = math.ceil(800 / (capacidade_medida_req_por_s * 0.7))

    assert numero_de_instancias >= 1
