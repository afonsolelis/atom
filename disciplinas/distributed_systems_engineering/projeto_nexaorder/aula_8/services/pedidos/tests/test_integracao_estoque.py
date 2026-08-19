"""Integração real entre pedidos e estoque — sem Docker.

Usa `httpx.ASGITransport` para chamar a aplicação FastAPI de estoque
diretamente em processo, atravessando a mesma pilha HTTP (rotas, validação
de Pydantic, serialização) que seria exercitada sobre a rede real. É o que
permite testar o disjuntor abrindo de verdade, com duas aplicações
distintas, sem subir contêineres.
"""

from __future__ import annotations

import importlib.util
import sys
import uuid
from pathlib import Path

import httpx
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


def _carregar_app_estoque():
    """Carrega o pacote `app` de services/estoque sob o nome distinto
    `estoque_app`, para não colidir com o pacote `app` do próprio serviço
    de pedidos, preservando os imports relativos internos de estoque
    (`from .replica import ...`, `from .store import ...`)."""
    for nome_modulo in list(sys.modules):
        if nome_modulo == "estoque_app" or nome_modulo.startswith("estoque_app."):
            del sys.modules[nome_modulo]

    raiz_app_estoque = Path(__file__).resolve().parents[2] / "estoque" / "app"

    spec_pacote = importlib.util.spec_from_file_location(
        "estoque_app",
        raiz_app_estoque / "__init__.py",
        submodule_search_locations=[str(raiz_app_estoque)],
    )
    pacote = importlib.util.module_from_spec(spec_pacote)
    sys.modules["estoque_app"] = pacote
    spec_pacote.loader.exec_module(pacote)

    spec_main = importlib.util.spec_from_file_location(
        "estoque_app.main", raiz_app_estoque / "main.py"
    )
    modulo_main = importlib.util.module_from_spec(spec_main)
    modulo_main.__package__ = "estoque_app"
    sys.modules["estoque_app.main"] = modulo_main
    spec_main.loader.exec_module(modulo_main)
    return modulo_main


@pytest.fixture()
def apps_integrados(tmp_path, monkeypatch):
    banco_pedidos = tmp_path / "pedidos_integracao.db"
    banco_estoque = tmp_path / "estoque_integracao.db"
    monkeypatch.setenv("PEDIDOS_DB_PATH", str(banco_pedidos))
    monkeypatch.setenv("ESTOQUE_DB_PATH", str(banco_estoque))
    monkeypatch.setenv("ATRASO_REPLICA_SEGUNDOS", "0.05")

    for nome_modulo in list(sys.modules):
        if nome_modulo == "app.main" or nome_modulo.startswith("app.main."):
            del sys.modules[nome_modulo]

    import app.main as modulo_pedidos
    from fastapi.testclient import TestClient

    modulo_estoque = _carregar_app_estoque()

    # Estoque, agora com persistência real (Aula 5), exige saldo inicializado
    # antes de qualquer reserva. Semeia um saldo generoso para o SKU usado
    # nos testes desta suíte, via uma chamada direta e síncrona ao app de
    # estoque — sem passar pelo cliente resiliente de pedidos.
    TestClient(modulo_estoque.app).post(
        "/estoque/TECLADO-MEC-01/inicializar", json={"quantidade": 1000}
    )

    transporte = httpx.ASGITransport(app=modulo_estoque.app)
    cliente_http = httpx.AsyncClient(transport=transporte, base_url="http://estoque")
    modulo_pedidos._cliente_estoque._cliente = cliente_http
    modulo_pedidos.ESTOQUE_BASE_URL = "http://estoque"

    with TestClient(modulo_pedidos.app) as cliente_pedidos:
        yield cliente_pedidos, modulo_pedidos, modulo_estoque


def _criar_pedido(cliente_pedidos) -> dict:
    corpo = {
        "cliente_id": str(uuid.uuid4()),
        "chave_idempotencia": str(uuid.uuid4()),
        "itens": [{"sku": "TECLADO-MEC-01", "quantidade": 1, "preco_unitario": 349.90}],
    }
    return cliente_pedidos.post("/pedidos", json=corpo).json()


def test_reservar_estoque_com_sucesso_atualiza_estado(apps_integrados):
    cliente_pedidos, _, modulo_estoque = apps_integrados
    modulo_estoque._config_falha.falhar_percentual = 0
    pedido = _criar_pedido(cliente_pedidos)

    resposta = cliente_pedidos.post(f"/pedidos/{pedido['id']}/reservar-estoque")

    assert resposta.status_code == 200
    assert resposta.json()["estado"] == "RESERVADO"
    assert cliente_pedidos.get(f"/pedidos/{pedido['id']}").json()["estado"] == "RESERVADO"


def test_reservar_estoque_indisponivel_devolve_503_sem_travar_pedidos(apps_integrados):
    cliente_pedidos, _, modulo_estoque = apps_integrados
    modulo_estoque._config_falha.falhar_percentual = 100
    pedido = _criar_pedido(cliente_pedidos)

    resposta = cliente_pedidos.post(f"/pedidos/{pedido['id']}/reservar-estoque")

    assert resposta.status_code == 503
    # O pedido continua existindo e consultável — não travou o serviço de pedidos.
    assert cliente_pedidos.get(f"/pedidos/{pedido['id']}").json()["estado"] == "RECEBIDO"


def test_disjuntor_abre_de_verdade_apos_falhas_http_repetidas(apps_integrados):
    """Reproduz o comportamento da Aula 4 fim a fim: um serviço lento/falho
    faz o disjuntor abrir, e chamadas seguintes falham de imediato."""
    cliente_pedidos, modulo_pedidos, modulo_estoque = apps_integrados
    from app.resiliencia import CircuitBreaker, ClienteResiliente, ConfiguracaoDisjuntor

    transporte = httpx.ASGITransport(app=modulo_estoque.app)
    cliente_http = httpx.AsyncClient(transport=transporte, base_url="http://estoque")
    disjuntor_pequeno = CircuitBreaker(ConfiguracaoDisjuntor(tamanho_janela=4, limite_taxa_erro=0.5))
    modulo_pedidos._disjuntor_estoque = disjuntor_pequeno
    modulo_pedidos._cliente_estoque = ClienteResiliente(cliente_http, disjuntor_pequeno, max_tentativas=1)

    modulo_estoque._config_falha.falhar_percentual = 100
    pedido = _criar_pedido(cliente_pedidos)

    for _ in range(4):
        resposta = cliente_pedidos.post(f"/pedidos/{pedido['id']}/reservar-estoque")
        assert resposta.status_code == 503

    assert modulo_pedidos._disjuntor_estoque.estado == "aberto"

    # Estoque "se recupera", mas o disjuntor ainda não passou o intervalo de
    # recuperação — a chamada seguinte é rejeitada sem sequer tocar a rede.
    modulo_estoque._config_falha.falhar_percentual = 0
    resposta = cliente_pedidos.post(f"/pedidos/{pedido['id']}/reservar-estoque")
    assert resposta.status_code == 503
    assert "disjuntor aberto" in resposta.json()["detail"]
