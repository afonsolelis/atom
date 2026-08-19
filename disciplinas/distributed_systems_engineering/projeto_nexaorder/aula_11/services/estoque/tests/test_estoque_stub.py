"""Testes da injeção de falha herdada da Aula 4 — continua funcionando
depois que a Aula 5 acrescentou persistência real."""


def test_reservar_com_sucesso_quando_ha_saldo(cliente_api):
    cliente_api.post("/estoque/TECLADO-MEC-01/inicializar", json={"quantidade": 5})

    resposta = cliente_api.post(
        "/reservas", json={"pedido_id": "p1", "sku": "TECLADO-MEC-01", "quantidade": 1}
    )

    assert resposta.status_code == 201
    assert resposta.json()["estado"] == "ATIVA"


def test_configurar_falha_100_por_cento_sempre_falha(cliente_api):
    cliente_api.post("/estoque/TECLADO-MEC-01/inicializar", json={"quantidade": 5})
    cliente_api.post("/_debug/config", json={"falhar_percentual": 100, "atraso_ms": 0})

    resposta = cliente_api.post(
        "/reservas", json={"pedido_id": "p1", "sku": "TECLADO-MEC-01", "quantidade": 1}
    )

    assert resposta.status_code == 503


def test_configurar_falha_0_por_cento_sempre_sucede(cliente_api):
    cliente_api.post("/estoque/TECLADO-MEC-01/inicializar", json={"quantidade": 100})
    cliente_api.post("/_debug/config", json={"falhar_percentual": 0, "atraso_ms": 0})

    for _ in range(10):
        resposta = cliente_api.post(
            "/reservas", json={"pedido_id": "p1", "sku": "TECLADO-MEC-01", "quantidade": 1}
        )
        assert resposta.status_code == 201


def test_saude_reporta_configuracao_ativa(cliente_api):
    cliente_api.post("/_debug/config", json={"falhar_percentual": 30, "atraso_ms": 50})

    resposta = cliente_api.get("/saude")

    assert resposta.json()["config_falha_ativa"]["falhar_percentual"] == 30
