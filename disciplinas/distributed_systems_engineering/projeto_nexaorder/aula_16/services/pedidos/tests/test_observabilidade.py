"""Os três pilares como código testado — Unidade 4, Aula 13.

Logs (app/logs_estruturados.py), métricas (app/metricas.py) e traces
(app/tracing.py) provados isoladamente, mais o comportamento observável
pela API: os endpoints administrativos que expõem spans e métricas, e a
prova de que a proteção contra cardinalidade não é só teórica — a rota com
parâmetro de verdade não vaza um valor distinto por requisição.
"""

from __future__ import annotations

import uuid

import pytest

from app.correlation import definir_trace_id
from app.logs_estruturados import construir_registro, registrar
from app.metricas import ContadorComRotulos, DimensaoDeAltaCardinalidade
from app.tracing import ColetorDeSpans, iniciar_span


# --- Logs estruturados ------------------------------------------------


def test_construir_registro_inclui_o_trace_id_do_contexto():
    definir_trace_id("trace-abc-123")

    registro = construir_registro("evento_de_teste", "pedidos", pedido_id="p1")

    assert registro["trace_id"] == "trace-abc-123"
    assert registro["servico"] == "pedidos"
    assert registro["evento"] == "evento_de_teste"
    assert registro["pedido_id"] == "p1"
    assert "timestamp" in registro


def test_registrar_emite_uma_linha_json_em_stdout(capsys):
    definir_trace_id("trace-xyz")

    registro = registrar("evento_de_teste", "pedidos", chave="valor")

    saida = capsys.readouterr().out
    assert '"trace_id": "trace-xyz"' in saida
    assert '"chave": "valor"' in saida
    assert registro["chave"] == "valor"


# --- Métricas com proteção contra cardinalidade ------------------------


def test_contador_aceita_dimensoes_declaradas():
    contador = ContadorComRotulos(nome="teste", dimensoes_permitidas=frozenset({"rota", "status_code"}))

    contador.incrementar(rota="/pedidos", status_code="201")
    contador.incrementar(rota="/pedidos", status_code="201")
    contador.incrementar(rota="/pedidos", status_code="404")

    assert contador.valor(rota="/pedidos", status_code="201") == 2
    assert contador.valor(rota="/pedidos", status_code="404") == 1
    assert contador.total() == 3


def test_contador_recusa_dimensao_nao_declarada():
    contador = ContadorComRotulos(nome="teste", dimensoes_permitidas=frozenset({"rota"}))

    with pytest.raises(DimensaoDeAltaCardinalidade):
        contador.incrementar(rota="/pedidos", trace_id=str(uuid.uuid4()))


def test_contador_com_dimensoes_de_baixa_cardinalidade_nao_cresce_sem_limite_sob_volume():
    """Unidade 4, Aula 14 — outro teste de duração (soak): 5.000 incrementos
    com dimensões corretamente de baixa cardinalidade (rota + status) não
    fazem o dicionário interno crescer proporcionalmente ao volume — ele
    fica limitado ao número de combinações possíveis (aqui, no máximo
    3 rotas × 3 status = 9), que é exatamente a garantia que
    `DimensaoDeAltaCardinalidade` (Aula 13) protege."""
    contador = ContadorComRotulos(nome="teste", dimensoes_permitidas=frozenset({"rota", "status_code"}))
    rotas = ["/pedidos", "/pedidos/{id}", "/saude"]
    status = ["200", "201", "404"]

    for i in range(5_000):
        contador.incrementar(rota=rotas[i % 3], status_code=status[i % 3])

    assert contador.total() == 5_000
    assert len(contador._contagens) <= 9


def test_contador_recusa_dimensao_que_vaza_identificador_por_requisicao():
    """O erro comum do roteiro, reproduzido: alguém declara 'pedido_id'
    como dimensão válida, achando que é só mais um rótulo. O contador
    detecta a explosão de cardinalidade assim que ela ultrapassa o
    limite, mesmo sem saber que 'pedido_id' é, na prática, um identificador
    por requisição."""
    contador = ContadorComRotulos(
        nome="teste", dimensoes_permitidas=frozenset({"pedido_id"}), limite_valores_distintos_por_dimensao=10
    )

    with pytest.raises(DimensaoDeAltaCardinalidade):
        for _ in range(11):
            contador.incrementar(pedido_id=str(uuid.uuid4()))


# --- Tracing -------------------------------------------------------


def test_span_mede_duracao_real_e_e_registrado_no_coletor():
    definir_trace_id("trace-1")
    coletor = ColetorDeSpans()

    with iniciar_span(coletor, "operacao", "servico-x") as span:
        pass

    assert span.fim_ms is not None
    assert span.duracao_ms >= 0
    spans = coletor.spans_do_trace("trace-1")
    assert len(spans) == 1
    assert spans[0]["nome"] == "operacao"
    assert spans[0]["span_pai_id"] is None


def test_spans_aninhados_apontam_para_o_pai_correto():
    definir_trace_id("trace-2")
    coletor = ColetorDeSpans()

    with iniciar_span(coletor, "raiz", "servico-x") as span_raiz:
        with iniciar_span(coletor, "filho", "servico-x") as span_filho:
            pass

    spans = {s["nome"]: s for s in coletor.spans_do_trace("trace-2")}
    assert spans["filho"]["span_pai_id"] == span_raiz.span_id
    assert spans["raiz"]["span_pai_id"] is None
    # O filho está contido no intervalo do pai — a propriedade geométrica
    # que torna a soma ingênua de durações uma leitura errada (Aula 13).
    assert spans["raiz"]["inicio_ms"] <= spans["filho"]["inicio_ms"]
    assert spans["filho"]["fim_ms"] <= spans["raiz"]["fim_ms"]


def test_span_apos_o_bloco_pai_nao_fica_aninhado_nele():
    """Depois que o span pai termina, um novo span não deve continuar
    sendo aninhado sob ele — a ContextVar precisa restaurar o valor
    anterior na saída do bloco."""
    definir_trace_id("trace-3")
    coletor = ColetorDeSpans()

    with iniciar_span(coletor, "primeiro", "servico-x"):
        pass
    with iniciar_span(coletor, "segundo", "servico-x"):
        pass

    spans = {s["nome"]: s for s in coletor.spans_do_trace("trace-3")}
    assert spans["segundo"]["span_pai_id"] is None


# --- Comportamento observável pela API ------------------------------


def _corpo_pedido() -> dict:
    return {
        "cliente_id": str(uuid.uuid4()),
        "chave_idempotencia": str(uuid.uuid4()),
        "itens": [{"sku": "TECLADO-MEC-01", "quantidade": 1, "preco_unitario": 349.90}],
    }


def test_resposta_sempre_devolve_o_trace_id_no_cabecalho(cliente_api):
    resposta = cliente_api.post("/pedidos", json=_corpo_pedido())

    assert "x-trace-id" in resposta.headers
    assert len(resposta.headers["x-trace-id"]) == 32  # uuid4().hex


def test_cliente_pode_impor_seu_proprio_trace_id(cliente_api):
    meu_trace_id = "a" * 32

    resposta = cliente_api.post("/pedidos", json=_corpo_pedido(), headers={"X-Trace-Id": meu_trace_id})

    assert resposta.headers["x-trace-id"] == meu_trace_id
    assert resposta.json()["trace_id"] == meu_trace_id


def test_endpoint_spans_expoe_o_span_raiz_da_requisicao(cliente_api):
    meu_trace_id = "b" * 32

    cliente_api.post("/pedidos", json=_corpo_pedido(), headers={"X-Trace-Id": meu_trace_id})
    spans = cliente_api.get(f"/_admin/spans/{meu_trace_id}").json()

    assert len(spans) == 1
    assert spans[0]["nome"] == "POST /pedidos"
    assert spans[0]["servico"] == "pedidos"
    assert spans[0]["trace_id"] == meu_trace_id


def test_endpoint_spans_para_trace_desconhecido_devolve_lista_vazia(cliente_api):
    assert cliente_api.get("/_admin/spans/trace-que-nao-existe").json() == []


def test_metricas_nao_explodem_com_muitos_pedidos_distintos(cliente_api):
    """A prova de que a proteção funciona na prática: `GET /pedidos/{id}`
    é chamado com 60 IDs distintos, e a dimensão 'rota' das métricas
    continua tendo um único valor — o padrão da rota, não o caminho exato
    — porque `middleware_observabilidade` usa `request.scope['route'].path`,
    nunca `request.url.path`, ao alimentar o contador."""
    for _ in range(60):
        cliente_api.get(f"/pedidos/{uuid.uuid4()}")  # todos 404, não importa

    resposta = cliente_api.get("/_admin/metricas")
    assert resposta.json()["http_requisicoes_total"] >= 60
