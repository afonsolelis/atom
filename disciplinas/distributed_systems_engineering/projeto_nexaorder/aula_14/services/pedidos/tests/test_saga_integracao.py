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
import time
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


def test_experimento_de_caos_indisponibilidade_total_do_pagamento(plataforma):
    """Unidade 4, Aula 14 — o experimento de caos deste projeto, com as
    cinco salvaguardas do cartão do roteiro:

    Hipótese de estado estável: sob indisponibilidade total do provedor de
    pagamento, nenhum pedido deve ficar em estado inconsistente — todos
    devem terminar totalmente compensados, e o disjuntor deve abrir.
    (A hipótese numérica literal do roteiro — "conclusão não deve cair
    abaixo de 90%" — presume um caminho de pagamento degradado que este
    projeto não implementa; sob falha total e sem fallback, 0% de conclusão
    é o resultado correto, não uma falha do experimento. Ver
    docs/testes-e-caos.md.)
    Perturbação: `falhar_percentual=100` em pagamento — a mesma alavanca de
    injeção de falha da Aula 4/5, reinterpretada sob um experimento
    controlado, com hipótese e critérios declarados de antemão.
    Métricas de controle: `estado_final` e `compensacoes` de cada pedido, e
    o estado do disjuntor via `GET /saude`.
    Raio de impacto: ambiente de teste isolado, zero tráfego real.
    Critério de interrupção (kill switch): `falhar_percentual` de volta a 0.
    """
    cliente_pedidos, pedidos, estoque, pagamento, _ = plataforma
    from fastapi.testclient import TestClient

    # Reduz a janela do disjuntor para não depender de dezenas de
    # tentativas reais (com seus próprios backoffs) só para abri-lo.
    pedidos._disjuntor_pagamento.config.tamanho_janela = 4

    TestClient(pagamento.app).post("/_debug/config", json={"falhar_percentual": 100})

    resultados = []
    for _ in range(3):
        pedido = _criar_pedido(cliente_pedidos)
        resposta = cliente_pedidos.post(f"/pedidos/{pedido['id']}/finalizar-compra")
        resultados.append(resposta.json())

    taxa_de_conclusao = sum(1 for r in resultados if r["sucesso"]) / len(resultados)
    assert taxa_de_conclusao == 0.0  # a hipótese numérica ingênua é refutada — ver docstring acima

    # A propriedade que este projeto de fato garante sob a perturbação:
    # nenhum pedido fica preso — todos voltam a um estado consistente.
    assert all(r["estado_final"] == "RECEBIDO" for r in resultados)
    assert all([c["nome"] for c in r["compensacoes"]] == ["liberar_estoque"] for r in resultados)

    assert cliente_pedidos.get("/saude").json()["disjuntor_pagamento"] == "aberto"

    # A última tentativa, com o disjuntor já aberto, falha sem tocar a
    # rede — proteção rápida, não apenas eventual (ver docs/testes-e-caos.md).
    pedido_extra = _criar_pedido(cliente_pedidos)
    inicio = time.perf_counter()
    resultado_protegido = cliente_pedidos.post(f"/pedidos/{pedido_extra['id']}/finalizar-compra").json()
    duracao_protegida_ms = (time.perf_counter() - inicio) * 1000
    assert resultado_protegido["sucesso"] is False
    assert duracao_protegida_ms < 50  # instantâneo: nenhuma tentativa de rede, nenhum backoff

    # Kill switch: desliga a perturbação e prova recuperação — o próprio
    # ponto do experimento, não só a falha controlada.
    pedidos._disjuntor_pagamento.config.intervalo_semiaberto_segundos = 0.02
    time.sleep(0.05)
    TestClient(pagamento.app).post("/_debug/config", json={"falhar_percentual": 0})

    pedido_recuperado = _criar_pedido(cliente_pedidos)
    resultado_recuperado = cliente_pedidos.post(
        f"/pedidos/{pedido_recuperado['id']}/finalizar-compra"
    ).json()

    assert resultado_recuperado["sucesso"] is True
    assert resultado_recuperado["estado_final"] == "EXPEDIDO"
    assert cliente_pedidos.get("/saude").json()["disjuntor_pagamento"] == "fechado"


class _TransporteIndisponivel(httpx.AsyncBaseTransport):
    """Um provedor que não está no ar: a conexão é RECUSADA, não atendida
    com erro. É o que o Kubernetes produz quando um Deployment vai a zero
    réplicas — o Service existe, o DNS resolve, e não há endpoint atrás
    dele. `falhar_percentual=100` (a alavanca da Aula 4/5) não reproduz
    isto: ali o provedor responde, só que com erro."""

    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        raise httpx.ConnectError("All connection attempts failed", request=request)


def test_experimento_de_caos_pagamento_fora_do_ar_tambem_compensa(plataforma):
    """Unidade 4, Aula 14 — a segunda perturbação do experimento de caos,
    e a que revelou um defeito real.

    O experimento anterior injeta falha com `falhar_percentual=100`: o
    pagamento responde 500. Esta variação remove o provedor do ar: a
    conexão é recusada (`httpx.ConnectError`). São modos de falha
    diferentes, e até a Aula 13 o projeto tratava apenas o primeiro — o
    segundo escapava como exceção não capturada, a saga morria no meio,
    `finalizar-compra` devolvia 500, a reserva de estoque ficava pendurada
    e o disjuntor não registrava falha nenhuma. Rodando os manifests em um
    cluster kind com `kubectl scale deployment pagamento --replicas=0`,
    três sagas seguidas devolveram HTTP 500, o disjuntor de pagamento
    seguiu `fechado` e o saldo de estoque caiu de 98 para 95 sem
    compensação (ver docs/kubernetes-execucao.md).

    A correção está em `app/resiliencia.py` e `app/main.py`: capturar
    `httpx.TransportError` — a superclasse de timeout E de erro de conexão
    — em vez de só `httpx.TimeoutException`. Este teste é a regressão.
    """
    cliente_pedidos, pedidos, estoque, _, _ = plataforma
    from fastapi.testclient import TestClient

    saldo_antes = TestClient(estoque.app).get("/saldo/TECLADO-MEC-01").json()["quantidade"]
    pedidos._disjuntor_pagamento.config.tamanho_janela = 4
    pedidos._cliente_pagamento._cliente = httpx.AsyncClient(
        transport=_TransporteIndisponivel(), base_url="http://servico"
    )

    resultados = []
    for _ in range(2):
        pedido = _criar_pedido(cliente_pedidos)
        resposta = cliente_pedidos.post(f"/pedidos/{pedido['id']}/finalizar-compra")
        assert resposta.status_code == 200, "a saga não pode estourar como erro interno"
        resultados.append(resposta.json())

    # A mesma hipótese do experimento anterior, agora sob o modo de falha
    # que de fato acontece em um cluster: nenhum pedido fica preso.
    assert all(r["sucesso"] is False for r in resultados)
    assert all(r["estado_final"] == "RECEBIDO" for r in resultados)
    assert all(r["falhou_em"] == "autorizar_pagamento" for r in resultados)
    assert all([c["nome"] for c in r["compensacoes"]] == ["liberar_estoque"] for r in resultados)

    # Nada de estoque vazado: toda reserva feita foi liberada.
    assert TestClient(estoque.app).get("/saldo/TECLADO-MEC-01").json()["quantidade"] == saldo_antes

    # E o disjuntor abre — antes da correção ele permanecia fechado
    # justamente no caso em que mais importa, porque a conexão recusada
    # nunca chegava a ser registrada como falha.
    assert cliente_pedidos.get("/saude").json()["disjuntor_pagamento"] == "aberto"


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
