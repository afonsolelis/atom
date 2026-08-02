"""Sondas de vivacidade e prontidão — Unidade 3, Aula 11."""


def test_saude_sempre_responde_200(cliente_api):
    assert cliente_api.get("/saude").status_code == 200


def test_pronto_responde_200_com_banco_acessivel(cliente_api):
    resposta = cliente_api.get("/pronto")

    assert resposta.status_code == 200
    assert resposta.json()["pronto"] is True
