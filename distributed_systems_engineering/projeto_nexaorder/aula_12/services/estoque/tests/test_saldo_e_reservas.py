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


def test_liberar_reserva_devolve_saldo(cliente_api):
    """Compensação da Aula 8: liberar uma reserva ativa devolve a
    quantidade ao saldo disponível."""
    cliente_api.post("/estoque/TECLADO-MEC-01/inicializar", json={"quantidade": 5})
    reserva = cliente_api.post(
        "/reservas", json={"pedido_id": "p1", "sku": "TECLADO-MEC-01", "quantidade": 2}
    ).json()
    assert cliente_api.get("/saldo/TECLADO-MEC-01?consistencia=forte").json()["quantidade"] == 3

    resposta = cliente_api.post(f"/reservas/{reserva['reserva_id']}/liberar")

    assert resposta.status_code == 200
    assert resposta.json()["estado"] == "LIBERADA"
    assert cliente_api.get("/saldo/TECLADO-MEC-01?consistencia=forte").json()["quantidade"] == 5


def test_liberar_reserva_ja_liberada_nao_devolve_saldo_duas_vezes(cliente_api):
    cliente_api.post("/estoque/TECLADO-MEC-01/inicializar", json={"quantidade": 5})
    reserva = cliente_api.post(
        "/reservas", json={"pedido_id": "p1", "sku": "TECLADO-MEC-01", "quantidade": 2}
    ).json()

    cliente_api.post(f"/reservas/{reserva['reserva_id']}/liberar")
    segunda_liberacao = cliente_api.post(f"/reservas/{reserva['reserva_id']}/liberar")

    assert segunda_liberacao.status_code == 404
    assert cliente_api.get("/saldo/TECLADO-MEC-01?consistencia=forte").json()["quantidade"] == 5


def test_liberar_reserva_inexistente_devolve_404(cliente_api):
    import uuid

    resposta = cliente_api.post(f"/reservas/{uuid.uuid4()}/liberar")

    assert resposta.status_code == 404


def test_listar_reservas_por_pedido(cliente_api):
    cliente_api.post("/estoque/TECLADO-MEC-01/inicializar", json={"quantidade": 5})
    cliente_api.post("/reservas", json={"pedido_id": "pedido-x", "sku": "TECLADO-MEC-01", "quantidade": 1})
    cliente_api.post("/reservas", json={"pedido_id": "pedido-y", "sku": "TECLADO-MEC-01", "quantidade": 1})

    resposta = cliente_api.get("/reservas/por-pedido/pedido-x")

    assert resposta.status_code == 200
    reservas = resposta.json()
    assert len(reservas) == 1
    assert reservas[0]["pedido_id"] == "pedido-x"


def test_listar_reservas_de_pedido_sem_reservas_devolve_lista_vazia(cliente_api):
    resposta = cliente_api.get("/reservas/por-pedido/pedido-inexistente")

    assert resposta.status_code == 200
    assert resposta.json() == []
