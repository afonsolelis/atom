"""Testes de contrato — Unidade 4, Aula 14.

Um teste de contrato verifica se consumidor e provedor concordam sobre o
formato da resposta sem exigir a saga inteira em execução — só o provedor
sob teste precisa estar de pé. É essa economia que o torna mais barato do
que um teste de ponta a ponta como os de `test_saga_integracao.py`, e mais
confiável do que confiar na leitura do código de outro serviço."""

from __future__ import annotations

import importlib.util
import sys
import uuid
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from contratos import (
    CONTRATO_AUTORIZAR_PAGAMENTO,
    CONTRATO_RESERVAR_ESTOQUE,
    CONTRATO_SOLICITAR_EXPEDICAO,
    verificar_contrato,
)

RAIZ_SERVICES = Path(__file__).resolve().parents[2]


def _carregar_pacote_servico(nome_servico: str, nome_pacote: str):
    """Ver services/pedidos/tests/test_saga_integracao.py — mesmo padrão de
    carregamento dinâmico, repetido aqui porque cada arquivo de teste deste
    projeto é independente dos demais."""
    for nome_modulo in list(sys.modules):
        if nome_modulo == nome_pacote or nome_modulo.startswith(f"{nome_pacote}."):
            del sys.modules[nome_modulo]

    raiz_app = RAIZ_SERVICES / nome_servico / "app"

    spec_pacote = importlib.util.spec_from_file_location(
        nome_pacote, raiz_app / "__init__.py", submodule_search_locations=[str(raiz_app)]
    )
    pacote = importlib.util.module_from_spec(spec_pacote)
    sys.modules[nome_pacote] = pacote
    spec_pacote.loader.exec_module(pacote)

    spec_main = importlib.util.spec_from_file_location(f"{nome_pacote}.main", raiz_app / "main.py")
    modulo_main = importlib.util.module_from_spec(spec_main)
    modulo_main.__package__ = nome_pacote
    sys.modules[f"{nome_pacote}.main"] = modulo_main
    spec_main.loader.exec_module(modulo_main)
    return modulo_main


def _cabecalho_identidade_pedidos(nome_pacote: str) -> dict[str, str]:
    modulo_seguranca = sys.modules[f"{nome_pacote}.seguranca"]
    return {"Authorization": f"Bearer {modulo_seguranca.emitir_token('pedidos')}"}


# --- Contrato: estoque ------------------------------------------------


@pytest.fixture()
def estoque_real(tmp_path, monkeypatch):
    monkeypatch.setenv("ESTOQUE_DB_PATH", str(tmp_path / "estoque_contrato.db"))
    modulo = _carregar_pacote_servico("estoque", "estoque_app_contrato")

    from fastapi.testclient import TestClient

    cliente = TestClient(modulo.app, headers=_cabecalho_identidade_pedidos("estoque_app_contrato"))
    cliente.post("/estoque/TECLADO-MEC-01/inicializar", json={"quantidade": 100})
    return cliente


def test_contrato_de_reservar_estoque_e_cumprido(estoque_real):
    resposta = estoque_real.post(
        "/reservas", json={"pedido_id": str(uuid.uuid4()), "sku": "TECLADO-MEC-01", "quantidade": 1}
    )
    assert resposta.status_code == 201

    assert verificar_contrato(resposta.json(), CONTRATO_RESERVAR_ESTOQUE) == []


# --- Contrato: pagamento ------------------------------------------------


@pytest.fixture()
def pagamento_real(tmp_path, monkeypatch):
    monkeypatch.setenv("PAGAMENTO_DB_PATH", str(tmp_path / "pagamento_contrato.db"))
    modulo = _carregar_pacote_servico("pagamento", "pagamento_app_contrato")

    from fastapi.testclient import TestClient

    return TestClient(modulo.app, headers=_cabecalho_identidade_pedidos("pagamento_app_contrato"))


def test_contrato_de_autorizar_pagamento_e_cumprido(pagamento_real):
    resposta = pagamento_real.post(
        "/cobrancas",
        json={"pedido_id": str(uuid.uuid4()), "chave_idempotencia": str(uuid.uuid4()), "valor": 100.0},
    )
    assert resposta.status_code == 201

    assert verificar_contrato(resposta.json(), CONTRATO_AUTORIZAR_PAGAMENTO) == []


# --- Contrato: expedição ------------------------------------------------


@pytest.fixture()
def expedicao_real(tmp_path, monkeypatch):
    monkeypatch.setenv("EXPEDICAO_DB_PATH", str(tmp_path / "expedicao_contrato.db"))
    modulo = _carregar_pacote_servico("expedicao", "expedicao_app_contrato")

    from fastapi.testclient import TestClient

    return TestClient(modulo.app, headers=_cabecalho_identidade_pedidos("expedicao_app_contrato"))


def test_contrato_de_solicitar_expedicao_e_cumprido(expedicao_real):
    resposta = expedicao_real.post(
        "/remessas", json={"pedido_id": str(uuid.uuid4()), "chave_idempotencia": str(uuid.uuid4())}
    )
    assert resposta.status_code == 201

    assert verificar_contrato(resposta.json(), CONTRATO_SOLICITAR_EXPEDICAO) == []


# --- O verificador não é decorativo -------------------------------------


def test_verificar_contrato_detecta_campo_removido():
    """Prova que o mecanismo pega uma quebra de verdade: uma resposta sem
    'reserva_id' — a mudança silenciosa de nome de campo que a Aula 10
    discutiu a propósito de evolução de esquema — é detectada antes de
    chegar a produção, exatamente o valor prático que o roteiro atribui a
    testes de contrato."""
    resposta_quebrada = {"pedido_id": "p1", "sku": "TECLADO-MEC-01", "quantidade": 1, "estado": "ATIVA"}

    assert verificar_contrato(resposta_quebrada, CONTRATO_RESERVAR_ESTOQUE) == ["reserva_id"]


def test_verificar_contrato_com_campos_extras_ainda_cumpre():
    """Campos extras não quebram o contrato — só a ausência de um campo
    declarado quebra. O provedor pode evoluir livremente adicionando
    informação nova, desde que não remova o que o consumidor declarou
    precisar."""
    resposta_com_campo_novo = {"reserva_id": "r1", "sku": "X", "quantidade": 1, "prioridade": "alta"}

    assert verificar_contrato(resposta_com_campo_novo, CONTRATO_RESERVAR_ESTOQUE) == []
