"""Testes do dublê de Estoque desta aula."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pytest
from fastapi.testclient import TestClient

from app.main import app, _config


@pytest.fixture(autouse=True)
def resetar_configuracao_falha():
    _config.falhar_percentual = 0
    _config.atraso_ms = 0
    yield
    _config.falhar_percentual = 0
    _config.atraso_ms = 0


@pytest.fixture()
def cliente():
    return TestClient(app)


def test_reservar_com_sucesso(cliente):
    resposta = cliente.post(
        "/reservas", json={"pedido_id": "p1", "sku": "TECLADO-MEC-01", "quantidade": 1}
    )
    assert resposta.status_code == 201
    assert resposta.json()["estado"] == "ATIVA"


def test_configurar_falha_100_por_cento_sempre_falha(cliente):
    cliente.post("/_debug/config", json={"falhar_percentual": 100, "atraso_ms": 0})

    resposta = cliente.post(
        "/reservas", json={"pedido_id": "p1", "sku": "TECLADO-MEC-01", "quantidade": 1}
    )

    assert resposta.status_code == 503


def test_configurar_falha_0_por_cento_sempre_sucede(cliente):
    cliente.post("/_debug/config", json={"falhar_percentual": 0, "atraso_ms": 0})

    for _ in range(10):
        resposta = cliente.post(
            "/reservas", json={"pedido_id": "p1", "sku": "TECLADO-MEC-01", "quantidade": 1}
        )
        assert resposta.status_code == 201


def test_saude_reporta_configuracao_ativa(cliente):
    cliente.post("/_debug/config", json={"falhar_percentual": 30, "atraso_ms": 50})

    resposta = cliente.get("/saude")

    assert resposta.json()["config_falha_ativa"]["falhar_percentual"] == 30
