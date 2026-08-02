"""Testa o contrato registrado em docs/contratos/api-pedidos.md (Aula 2)."""

import uuid


def _corpo_pedido(chave_idempotencia: str | None = None) -> dict:
    return {
        "cliente_id": str(uuid.uuid4()),
        "chave_idempotencia": chave_idempotencia or str(uuid.uuid4()),
        "itens": [
            {"sku": "TECLADO-MEC-01", "quantidade": 1, "preco_unitario": 349.90}
        ],
    }


def test_criar_pedido_devolve_201_e_estado_recebido(cliente_api):
    resposta = cliente_api.post("/pedidos", json=_corpo_pedido())

    assert resposta.status_code == 201
    corpo = resposta.json()
    assert corpo["estado"] == "RECEBIDO"
    assert corpo["total"] == 349.90
    assert corpo["carimbo_lamport"] == 1


def test_criar_pedido_gera_trace_id_quando_ausente(cliente_api):
    resposta = cliente_api.post("/pedidos", json=_corpo_pedido())

    assert "X-Trace-Id" in resposta.headers
    assert len(resposta.headers["X-Trace-Id"]) == 32
    assert resposta.json()["trace_id"] == resposta.headers["X-Trace-Id"]


def test_criar_pedido_propaga_trace_id_recebido(cliente_api):
    trace_id_do_cliente = "4bf92f3577b34da6a3ce929d0e0e4736"

    resposta = cliente_api.post(
        "/pedidos",
        json=_corpo_pedido(),
        headers={"X-Trace-Id": trace_id_do_cliente},
    )

    assert resposta.headers["X-Trace-Id"] == trace_id_do_cliente
    assert resposta.json()["trace_id"] == trace_id_do_cliente


def test_criar_pedido_com_mesma_chave_idempotencia_nao_duplica(cliente_api):
    chave = "checkout-carrinho-42"
    corpo = _corpo_pedido(chave)

    primeira = cliente_api.post("/pedidos", json=corpo)
    segunda = cliente_api.post("/pedidos", json=corpo)

    assert primeira.status_code == 201
    assert segunda.status_code == 201
    assert primeira.json()["id"] == segunda.json()["id"]
    # A segunda chamada não avança o relógio de Lamport nem cria nova linha.
    assert segunda.json()["carimbo_lamport"] == primeira.json()["carimbo_lamport"]


def test_criar_pedido_sem_itens_e_rejeitado(cliente_api):
    corpo = _corpo_pedido()
    corpo["itens"] = []

    resposta = cliente_api.post("/pedidos", json=corpo)

    assert resposta.status_code == 422


def test_obter_pedido_existente(cliente_api):
    criado = cliente_api.post("/pedidos", json=_corpo_pedido()).json()

    resposta = cliente_api.get(f"/pedidos/{criado['id']}")

    assert resposta.status_code == 200
    assert resposta.json()["id"] == criado["id"]


def test_obter_pedido_inexistente_devolve_404(cliente_api):
    resposta = cliente_api.get(f"/pedidos/{uuid.uuid4()}")

    assert resposta.status_code == 404


def test_carimbo_lamport_cresce_a_cada_pedido_novo(cliente_api):
    primeiro = cliente_api.post("/pedidos", json=_corpo_pedido()).json()
    segundo = cliente_api.post("/pedidos", json=_corpo_pedido()).json()

    assert segundo["carimbo_lamport"] > primeiro["carimbo_lamport"]
