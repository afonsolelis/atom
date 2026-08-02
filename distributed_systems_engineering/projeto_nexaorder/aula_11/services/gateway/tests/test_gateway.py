"""Integração do gateway com os quatro serviços reais, via ASGITransport —
sem Docker. Prova a composição descrita no roteiro da Aula 9: uma tela de
detalhes de pedido que, por trás, consulta vários serviços."""

from __future__ import annotations

import importlib.util
import sys
import uuid
from pathlib import Path

import httpx
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

RAIZ_SERVICES = Path(__file__).resolve().parents[2]


def _carregar_pacote_servico(nome_servico: str, nome_pacote: str):
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


@pytest.fixture()
def plataforma(tmp_path, monkeypatch):
    monkeypatch.setenv("PEDIDOS_DB_PATH", str(tmp_path / "pedidos.db"))
    monkeypatch.setenv("ESTOQUE_DB_PATH", str(tmp_path / "estoque.db"))
    monkeypatch.setenv("PAGAMENTO_DB_PATH", str(tmp_path / "pagamento.db"))
    monkeypatch.setenv("EXPEDICAO_DB_PATH", str(tmp_path / "expedicao.db"))
    monkeypatch.setenv("ATRASO_REPLICA_SEGUNDOS", "0.05")

    for nome_modulo in list(sys.modules):
        if nome_modulo == "app.main" or nome_modulo.startswith("app.main."):
            del sys.modules[nome_modulo]

    from fastapi.testclient import TestClient

    pedidos = _carregar_pacote_servico("pedidos", "pedidos_app")
    estoque = _carregar_pacote_servico("estoque", "estoque_app")
    pagamento = _carregar_pacote_servico("pagamento", "pagamento_app")
    expedicao = _carregar_pacote_servico("expedicao", "expedicao_app")

    TestClient(estoque.app).post("/estoque/TECLADO-MEC-01/inicializar", json={"quantidade": 1000})

    def _cliente_para(modulo_app):
        transporte = httpx.ASGITransport(app=modulo_app.app)
        return httpx.AsyncClient(transport=transporte, base_url="http://servico")

    pedidos._cliente_estoque._cliente = _cliente_para(estoque)
    pedidos._cliente_pagamento._cliente = _cliente_para(pagamento)
    pedidos._cliente_expedicao._cliente = _cliente_para(expedicao)
    pedidos.ESTOQUE_BASE_URL = "http://servico"
    pedidos.PAGAMENTO_BASE_URL = "http://servico"
    pedidos.EXPEDICAO_BASE_URL = "http://servico"

    import app.main as gateway

    gateway.PEDIDOS_BASE_URL = "http://servico"
    gateway.ESTOQUE_BASE_URL = "http://servico"
    gateway.PAGAMENTO_BASE_URL = "http://servico"
    gateway.EXPEDICAO_BASE_URL = "http://servico"
    # O gateway precisa de um transporte único que saiba rotear para os
    # quatro serviços por caminho de URL — como eles são apps ASGI
    # distintos, montamos um roteador assíncrono simples entre eles.
    gateway._cliente_http = httpx.AsyncClient(
        transport=_RoteadorParaServicos(
            {
                "/pedidos": pedidos.app,
                "/saude": pedidos.app,  # usado pela sonda de prontidão do gateway (Aula 11)
                "/reservas": estoque.app,
                "/cobrancas": pagamento.app,
                "/remessas": expedicao.app,
            }
        )
    )

    with TestClient(pedidos.app) as cliente_pedidos:
        yield cliente_pedidos, gateway, estoque, pagamento, expedicao


class _RoteadorParaServicos(httpx.AsyncBaseTransport):
    """Despacha, em processo, para o app ASGI correto conforme o prefixo do
    caminho — permite que o gateway fale com "quatro serviços" usando uma
    única base_url nos testes, sem abrir socket nenhum."""

    def __init__(self, mapa_prefixo_para_app: dict[str, object]) -> None:
        self._transportes = {
            prefixo: httpx.ASGITransport(app=app) for prefixo, app in mapa_prefixo_para_app.items()
        }

    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        caminho = request.url.path
        for prefixo, transporte in self._transportes.items():
            if caminho.startswith(prefixo):
                return await transporte.handle_async_request(request)
        return httpx.Response(404)


def _criar_pedido(cliente_pedidos) -> dict:
    corpo = {
        "cliente_id": str(uuid.uuid4()),
        "chave_idempotencia": str(uuid.uuid4()),
        "itens": [{"sku": "TECLADO-MEC-01", "quantidade": 1, "preco_unitario": 349.90}],
    }
    return cliente_pedidos.post("/pedidos", json=corpo).json()


def test_resumo_compoe_pedido_reserva_cobranca_e_remessa(plataforma):
    cliente_pedidos, gateway, *_ = plataforma
    pedido = _criar_pedido(cliente_pedidos)
    cliente_pedidos.post(f"/pedidos/{pedido['id']}/finalizar-compra")

    from fastapi.testclient import TestClient

    resposta = TestClient(gateway.app).get(f"/pedidos/{pedido['id']}/resumo")

    assert resposta.status_code == 200
    corpo = resposta.json()
    assert corpo["pedido"]["id"] == pedido["id"]
    assert len(corpo["reservas"]) == 1
    assert len(corpo["cobrancas"]) == 1
    assert len(corpo["remessas"]) == 1


def test_resumo_de_pedido_recem_criado_tem_listas_vazias(plataforma):
    """Antes de finalizar a compra, não há reserva, cobrança nem remessa —
    e isso não é um erro, é o estado real do pedido."""
    cliente_pedidos, gateway, *_ = plataforma
    pedido = _criar_pedido(cliente_pedidos)

    from fastapi.testclient import TestClient

    resposta = TestClient(gateway.app).get(f"/pedidos/{pedido['id']}/resumo")

    corpo = resposta.json()
    assert corpo["reservas"] == []
    assert corpo["cobrancas"] == []
    assert corpo["remessas"] == []


def test_resumo_de_pedido_inexistente_devolve_404(plataforma):
    _, gateway, *_ = plataforma
    from fastapi.testclient import TestClient

    resposta = TestClient(gateway.app).get(f"/pedidos/{uuid.uuid4()}/resumo")

    assert resposta.status_code == 404


def test_saude_do_gateway_nao_depende_de_pedidos(plataforma):
    """Vivacidade (Aula 11): o gateway responde mesmo sem checar nada."""
    _, gateway, *_ = plataforma
    from fastapi.testclient import TestClient

    resposta = TestClient(gateway.app).get("/saude")

    assert resposta.status_code == 200


def test_pronto_do_gateway_verifica_pedidos_alcancavel(plataforma):
    """Prontidão (Aula 11): com pedidos no ar (via o roteador de teste),
    o gateway se declara pronto."""
    _, gateway, *_ = plataforma
    from fastapi.testclient import TestClient

    resposta = TestClient(gateway.app).get("/pronto")

    assert resposta.status_code == 200
    assert resposta.json()["pronto"] is True
