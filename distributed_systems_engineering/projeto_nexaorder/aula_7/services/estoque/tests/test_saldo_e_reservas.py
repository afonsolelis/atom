"""Testa a invariante central do Estoque: o saldo nunca fica negativo."""


def test_inicializar_saldo_e_consultar(cliente_api):
    cliente_api.post("/estoque/TECLADO-MEC-01/inicializar", json={"quantidade": 10})

    resposta = cliente_api.get("/saldo/TECLADO-MEC-01?consistencia=forte")

    assert resposta.status_code == 200
    corpo = resposta.json()
    assert corpo["quantidade"] == 10
    assert corpo["fonte"] == "lider"


def test_reservar_decrementa_o_saldo(cliente_api):
    cliente_api.post("/estoque/TECLADO-MEC-01/inicializar", json={"quantidade": 5})

    cliente_api.post("/reservas", json={"pedido_id": "p1", "sku": "TECLADO-MEC-01", "quantidade": 2})

    saldo = cliente_api.get("/saldo/TECLADO-MEC-01?consistencia=forte").json()
    assert saldo["quantidade"] == 3


def test_reservar_mais_do_que_o_saldo_disponivel_e_rejeitado(cliente_api):
    cliente_api.post("/estoque/TECLADO-MEC-01/inicializar", json={"quantidade": 1})

    resposta = cliente_api.post(
        "/reservas", json={"pedido_id": "p1", "sku": "TECLADO-MEC-01", "quantidade": 2}
    )

    assert resposta.status_code == 409
    # o saldo não deve ter sido alterado pela tentativa rejeitada
    saldo = cliente_api.get("/saldo/TECLADO-MEC-01?consistencia=forte").json()
    assert saldo["quantidade"] == 1


def test_reservas_concorrentes_nao_vendem_mais_do_que_existe(cliente_api):
    """Duas reservas de 1 unidade cada contra um saldo de 1: uma vence,
    a outra é rejeitada — nunca as duas passam."""
    cliente_api.post("/estoque/TECLADO-MEC-01/inicializar", json={"quantidade": 1})

    resultados = [
        cliente_api.post(
            "/reservas", json={"pedido_id": f"p{i}", "sku": "TECLADO-MEC-01", "quantidade": 1}
        ).status_code
        for i in range(2)
    ]

    assert sorted(resultados) == [201, 409]


def test_saldo_de_sku_desconhecido_devolve_404(cliente_api):
    resposta = cliente_api.get("/saldo/SKU-INEXISTENTE?consistencia=forte")

    assert resposta.status_code == 404
