"""Prova que a outbox é alimentada atomicamente com a criação do pedido —
Unidade 2, Aula 8. Ninguém publica estes eventos ainda (o publicador chega
na Aula 10); este teste prova a metade "grava" do padrão."""

import uuid


def _corpo_pedido() -> dict:
    return {
        "cliente_id": str(uuid.uuid4()),
        "chave_idempotencia": str(uuid.uuid4()),
        "itens": [{"sku": "TECLADO-MEC-01", "quantidade": 1, "preco_unitario": 349.90}],
    }


def test_criar_pedido_grava_evento_pedidocriado_na_outbox(cliente_api):
    import app.main as modulo_pedidos

    pedido = cliente_api.post("/pedidos", json=_corpo_pedido()).json()

    eventos = modulo_pedidos.repositorio.eventos_pendentes()
    eventos_deste_pedido = [e for e in eventos if e["pedido_id"] == pedido["id"]]

    assert len(eventos_deste_pedido) == 1
    assert eventos_deste_pedido[0]["tipo"] == "PedidoCriado"
    assert eventos_deste_pedido[0]["payload"]["dados"]["total"] == pedido["total"]
    assert eventos_deste_pedido[0]["publicado"] == 0


def test_pedido_com_chave_idempotencia_repetida_nao_gera_segundo_evento(cliente_api):
    import app.main as modulo_pedidos

    corpo = _corpo_pedido()
    cliente_api.post("/pedidos", json=corpo)
    pedido = cliente_api.post("/pedidos", json=corpo).json()  # mesma chave, idempotente

    eventos_deste_pedido = [
        e for e in modulo_pedidos.repositorio.eventos_pendentes() if e["pedido_id"] == pedido["id"]
    ]

    assert len(eventos_deste_pedido) == 1


def test_marcar_publicado_remove_da_lista_de_pendentes(cliente_api):
    import app.main as modulo_pedidos

    pedido = cliente_api.post("/pedidos", json=_corpo_pedido()).json()
    evento = [
        e for e in modulo_pedidos.repositorio.eventos_pendentes() if e["pedido_id"] == pedido["id"]
    ][0]

    modulo_pedidos.repositorio.marcar_publicado(evento["id"])

    pendentes = [
        e for e in modulo_pedidos.repositorio.eventos_pendentes() if e["pedido_id"] == pedido["id"]
    ]
    assert pendentes == []
