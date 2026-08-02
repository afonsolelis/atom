import uuid


def test_autorizar_com_sucesso(cliente_api):
    resposta = cliente_api.post(
        "/cobrancas",
        json={"pedido_id": "p1", "chave_idempotencia": str(uuid.uuid4()), "valor": 349.90},
    )

    assert resposta.status_code == 201
    assert resposta.json()["estado"] == "AUTORIZADA"


def test_mesma_chave_idempotencia_nao_duplica_cobranca(cliente_api):
    chave = "pedido-1:pagamento"
    corpo = {"pedido_id": "p1", "chave_idempotencia": chave, "valor": 100.0}

    primeira = cliente_api.post("/cobrancas", json=corpo)
    segunda = cliente_api.post("/cobrancas", json=corpo)

    assert primeira.json()["id"] == segunda.json()["id"]


def test_falha_simulada_devolve_503(cliente_api):
    cliente_api.post("/_debug/config", json={"falhar_percentual": 100})

    resposta = cliente_api.post(
        "/cobrancas",
        json={"pedido_id": "p1", "chave_idempotencia": str(uuid.uuid4()), "valor": 100.0},
    )

    assert resposta.status_code == 503


def test_estornar_cobranca_autorizada(cliente_api):
    cobranca = cliente_api.post(
        "/cobrancas",
        json={"pedido_id": "p1", "chave_idempotencia": str(uuid.uuid4()), "valor": 100.0},
    ).json()

    resposta = cliente_api.post(f"/cobrancas/{cobranca['id']}/estornar")

    assert resposta.json()["estado"] == "ESTORNADA"


def test_estornar_cobranca_inexistente_devolve_404(cliente_api):
    resposta = cliente_api.post(f"/cobrancas/{uuid.uuid4()}/estornar")

    assert resposta.status_code == 404
