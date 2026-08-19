"""Teste de carga — Unidade 4, Aula 14.

Um teste de carga aplica o tráfego esperado e pergunta: o sistema atende ao
que foi prometido, sem violar as metas de latência e de erro? Diferente de
um teste de estresse (que aumenta a carga até o sistema falhar — ver
docs/testes-e-caos.md, que aponta `test_limitador_de_taxa_protege_reservas_de_verdade_via_http`,
em `tests/test_seguranca.py`, como o teste de estresse que este projeto já
tinha, sem esse rótulo, desde a Aula 12), este teste fica deliberadamente
dentro do orçamento conhecido do sistema: as 40 requisições abaixo seguem
sob a capacidade de 50 do balde de fichas (Aula 12) — carga esperada, não
um teste do próprio limitador."""

from __future__ import annotations

import time
import uuid


def test_carga_esperada_nao_viola_latencia_nem_taxa_de_erro(cliente_api):
    cliente_api.post("/estoque/TECLADO-MEC-01/inicializar", json={"quantidade": 10_000})

    latencias_ms = []
    erros = 0
    for _ in range(40):
        inicio = time.perf_counter()
        resposta = cliente_api.post(
            "/reservas",
            json={"pedido_id": str(uuid.uuid4()), "sku": "TECLADO-MEC-01", "quantidade": 1},
        )
        latencias_ms.append((time.perf_counter() - inicio) * 1000)
        if resposta.status_code != 201:
            erros += 1

    taxa_de_erro = erros / len(latencias_ms)
    p95 = sorted(latencias_ms)[int(len(latencias_ms) * 0.95)]

    assert taxa_de_erro == 0.0
    # Limiar generoso de propósito: o alvo aqui é detectar uma regressão
    # grosseira (uma travessia acidentalmente síncrona, um N+1 de banco),
    # não medir performance absoluta — o ambiente de execução deste
    # projeto (SQLite em processo, sem rede real) não é representativo de
    # produção (ver docs/testes-e-caos.md).
    assert p95 < 200
