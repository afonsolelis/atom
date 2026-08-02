"""Integração de ponta a ponta da saga — sem Docker.

Carrega estoque, pagamento e expedição como pacotes distintos (mesma
técnica de `test_integracao_estoque.py`) e os conecta a `pedidos` via
`httpx.ASGITransport`, para exercitar o caminho feliz e cada compensação
com HTTP real entre quatro aplicações FastAPI distintas, sem subir
contêineres.
"""

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
    """Carrega services/<nome_servico>/app como um pacote com nome
    distinto, preservando imports relativos internos."""
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

    import app.main as pedidos
    from fastapi.testclient import TestClient

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

    with TestClient(pedidos.app) as cliente_pedidos:
        yield cliente_pedidos, pedidos, estoque, pagamento, expedicao


def _criar_pedido(cliente_pedidos) -> dict:
    corpo = {
        "cliente_id": str(uuid.uuid4()),
        "chave_idempotencia": str(uuid.uuid4()),
        "itens": [{"sku": "TECLADO-MEC-01", "quantidade": 1, "preco_unitario": 349.90}],
    }
    return cliente_pedidos.post("/pedidos", json=corpo).json()


def test_saga_caminho_feliz_chega_a_expedido(plataforma):
    cliente_pedidos, *_ = plataforma
    pedido = _criar_pedido(cliente_pedidos)

    resposta = cliente_pedidos.post(f"/pedidos/{pedido['id']}/finalizar-compra")

    corpo = resposta.json()
    assert corpo["sucesso"] is True
    assert corpo["estado_final"] == "EXPEDIDO"
    assert corpo["reserva_id"] and corpo["cobranca_id"] and corpo["remessa_id"]
    assert cliente_pedidos.get(f"/pedidos/{pedido['id']}").json()["estado"] == "EXPEDIDO"


def test_saga_falha_no_pagamento_libera_a_reserva_de_estoque(plataforma):
    cliente_pedidos, _, estoque, pagamento, _ = plataforma
    from fastapi.testclient import TestClient

    TestClient(pagamento.app).post("/_debug/config", json={"falhar_percentual": 100})
    pedido = _criar_pedido(cliente_pedidos)

    saldo_antes = TestClient(estoque.app).get(
        "/saldo/TECLADO-MEC-01?consistencia=forte"
    ).json()["quantidade"]

    resposta = cliente_pedidos.post(f"/pedidos/{pedido['id']}/finalizar-compra")
    corpo = resposta.json()

    assert corpo["sucesso"] is False
    assert corpo["estado_final"] == "RECEBIDO"
    assert corpo["falhou_em"] == "autorizar_pagamento"
    assert [c["nome"] for c in corpo["compensacoes"]] == ["liberar_estoque"]

    saldo_depois = TestClient(estoque.app).get(
        "/saldo/TECLADO-MEC-01?consistencia=forte"
    ).json()["quantidade"]
    assert saldo_depois == saldo_antes  # a reserva foi liberada, saldo voltou


def test_saga_falha_na_expedicao_estorna_pagamento_e_libera_estoque(plataforma):
    cliente_pedidos, _, estoque, pagamento, expedicao = plataforma
    from fastapi.testclient import TestClient

    TestClient(expedicao.app).post("/_debug/config", json={"falhar_percentual": 100})
    pedido = _criar_pedido(cliente_pedidos)

    saldo_antes = TestClient(estoque.app).get(
        "/saldo/TECLADO-MEC-01?consistencia=forte"
    ).json()["quantidade"]

    resposta = cliente_pedidos.post(f"/pedidos/{pedido['id']}/finalizar-compra")
    corpo = resposta.json()

    assert corpo["sucesso"] is False
    assert corpo["estado_final"] == "PAGO"
    assert corpo["falhou_em"] == "solicitar_expedicao"
    assert [c["nome"] for c in corpo["compensacoes"]] == ["estornar_pagamento", "liberar_estoque"]

    saldo_depois = TestClient(estoque.app).get(
        "/saldo/TECLADO-MEC-01?consistencia=forte"
    ).json()["quantidade"]
    assert saldo_depois == saldo_antes


def test_saga_reservar_estoque_isolado_continua_funcionando(plataforma):
    """A rota independente da Aula 4 continua existindo ao lado da saga."""
    cliente_pedidos, *_ = plataforma
    pedido = _criar_pedido(cliente_pedidos)

    resposta = cliente_pedidos.post(f"/pedidos/{pedido['id']}/reservar-estoque")

    assert resposta.status_code == 200
    assert resposta.json()["estado"] == "RESERVADO"


def test_spans_da_saga_formam_uma_arvore_com_a_saga_como_raiz(plataforma):
    """Unidade 4, Aula 13 — a mesma cascata do incidente do trace de doze
    segundos, só que aqui os spans são reais: medidos a partir das três
    chamadas de rede genuínas que a saga faz, não números inventados. Ver
    scripts/reconstruir_trace.py para o exemplo numérico do roteiro."""
    cliente_pedidos, *_ = plataforma
    pedido = _criar_pedido(cliente_pedidos)

    resposta = cliente_pedidos.post(f"/pedidos/{pedido['id']}/finalizar-compra")
    trace_id = resposta.headers["x-trace-id"]

    spans = cliente_pedidos.get(f"/_admin/spans/{trace_id}").json()
    por_nome = {s["nome"]: s for s in spans}

    nome_raiz = f"POST /pedidos/{pedido['id']}/finalizar-compra"
    assert nome_raiz in por_nome
    raiz = por_nome[nome_raiz]

    for nome_filho in ["reservar_estoque", "autorizar_pagamento", "solicitar_expedicao"]:
        assert nome_filho in por_nome, f"span '{nome_filho}' não foi registrado"
        assert por_nome[nome_filho]["span_pai_id"] == raiz["span_id"]
        assert por_nome[nome_filho]["trace_id"] == trace_id
        # Cada filho está contido no intervalo de tempo do pai — a
        # propriedade que torna errado somar as durações dos filhos para
        # "conferir" a duração do pai (ver docs/observabilidade.md).
        assert raiz["inicio_ms"] <= por_nome[nome_filho]["inicio_ms"]
        assert por_nome[nome_filho]["fim_ms"] <= raiz["fim_ms"]


def test_expedicao_nao_pode_solicitar_estorno_de_pagamento(plataforma):
    """A prova definitiva da Aula 12: reproduz literalmente o incidente da
    situação-problema ('nada impede que a expedição chame pagamento e
    peça um reembolso') e mostra que, agora, algo impede — a autorização
    por menor privilégio de `pagamento`."""
    cliente_pedidos, _, _, pagamento, _ = plataforma
    from fastapi.testclient import TestClient

    from pagamento_app.seguranca import emitir_token

    # Uma compra completa de verdade, para existir uma cobrança AUTORIZADA
    # de verdade — não adiantaria provar que uma cobrança inexistente não
    # pode ser estornada; a prova precisa ser sobre uma cobrança real.
    pedido = _criar_pedido(cliente_pedidos)
    resultado = cliente_pedidos.post(f"/pedidos/{pedido['id']}/finalizar-compra").json()
    assert resultado["sucesso"] is True
    cobranca_id = resultado["cobranca_id"]

    token_da_expedicao = emitir_token("expedicao")
    cliente_pagamento_direto = TestClient(pagamento.app)

    resposta = cliente_pagamento_direto.post(
        f"/cobrancas/{cobranca_id}/estornar",
        headers={"Authorization": f"Bearer {token_da_expedicao}"},
    )

    assert resposta.status_code == 403

    # E sem identidade nenhuma, nem chega a ser avaliado — 401, não 403.
    resposta_sem_identidade = cliente_pagamento_direto.post(f"/cobrancas/{cobranca_id}/estornar")
    assert resposta_sem_identidade.status_code == 401

    # A cobrança continua autorizada — o estorno indevido não aconteceu.
    cobrancas_do_pedido = cliente_pagamento_direto.get(
        f"/cobrancas/por-pedido/{pedido['id']}",
        headers={"Authorization": f"Bearer {emitir_token('pedidos')}"},
    ).json()
    assert cobrancas_do_pedido[0]["estado"] == "AUTORIZADA"
