import uuid


def test_solicitar_remessa_com_sucesso(cliente_api):
    resposta = cliente_api.post(
        "/remessas", json={"pedido_id": "p1", "chave_idempotencia": str(uuid.uuid4())}
    )

    assert resposta.status_code == 201
    corpo = resposta.json()
    assert corpo["estado"] == "ETIQUETA_GERADA"
    assert corpo["codigo_rastreio"].startswith("NX-")


def test_mesma_chave_idempotencia_nao_duplica_remessa(cliente_api):
    chave = "pedido-1:expedicao"
    corpo = {"pedido_id": "p1", "chave_idempotencia": chave}

    primeira = cliente_api.post("/remessas", json=corpo)
    segunda = cliente_api.post("/remessas", json=corpo)

    assert primeira.json()["id"] == segunda.json()["id"]
    assert primeira.json()["codigo_rastreio"] == segunda.json()["codigo_rastreio"]


def test_cancelar_remessa_com_etiqueta_gerada(cliente_api):
    remessa = cliente_api.post(
        "/remessas", json={"pedido_id": "p1", "chave_idempotencia": str(uuid.uuid4())}
    ).json()

    resposta = cliente_api.post(f"/remessas/{remessa['id']}/cancelar")

    assert resposta.json()["estado"] == "CANCELADA"


def test_falha_simulada_devolve_503(cliente_api):
    cliente_api.post("/_debug/config", json={"falhar_percentual": 100})

    resposta = cliente_api.post(
        "/remessas", json={"pedido_id": "p1", "chave_idempotencia": str(uuid.uuid4())}
    )

    assert resposta.status_code == 503


def test_listar_remessas_por_pedido(cliente_api):
    cliente_api.post("/remessas", json={"pedido_id": "pedido-x", "chave_idempotencia": str(uuid.uuid4())})

    resposta = cliente_api.get("/remessas/por-pedido/pedido-x")

    assert resposta.status_code == 200
    assert len(resposta.json()) == 1
