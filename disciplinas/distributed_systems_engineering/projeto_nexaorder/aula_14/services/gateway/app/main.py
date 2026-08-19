"""Gateway — Unidade 3, Aula 9.

Compõe uma visão única de um pedido a partir de quatro serviços, para que
quem consome a API não precise conhecer a decomposição interna da
NexaOrder nem seja afetado se essa decomposição mudar amanhã.

Deliberadamente sem regra de negócio e sem banco de dados próprio: o único
trabalho do gateway é rotear e compor. Quando um gateway acumula lógica de
domínio, ele vira um novo monólito escondido atrás de uma fachada de
microsserviços — o alerta do próprio roteiro da Aula 9
(ver docs/limites-de-dominio.md).
"""

from __future__ import annotations

import asyncio
import os
from typing import Any

import httpx
from fastapi import FastAPI, HTTPException, Request, Response

from .correlation import CABECALHO_TRACE_ID, definir_trace_id, gerar_trace_id, obter_trace_id
from .logs_estruturados import registrar as registrar_log
from .metricas import ContadorComRotulos
from .tracing import ColetorDeSpans, iniciar_span

PEDIDOS_BASE_URL = os.environ.get("PEDIDOS_BASE_URL", "http://localhost:8001")
ESTOQUE_BASE_URL = os.environ.get("ESTOQUE_BASE_URL", "http://localhost:8002")
PAGAMENTO_BASE_URL = os.environ.get("PAGAMENTO_BASE_URL", "http://localhost:8003")
EXPEDICAO_BASE_URL = os.environ.get("EXPEDICAO_BASE_URL", "http://localhost:8004")
NOME_SERVICO = "gateway"

app = FastAPI(title="NexaOrder — Gateway", version="0.13.0")
_cliente_http = httpx.AsyncClient()
coletor_spans = ColetorDeSpans()
contador_requisicoes = ContadorComRotulos(
    nome="http_requisicoes_total", dimensoes_permitidas=frozenset({"rota", "metodo", "status_code"})
)


@app.middleware("http")
async def middleware_observabilidade(request: Request, chamar_proximo):
    """O gateway é a borda: aqui nasce o trace_id de toda jornada que
    ainda não trouxer um (ver docs/observabilidade.md, passo 1 da
    propagação). Ver services/pedidos/app/main.py para o resto do
    mecanismo, idêntico em cada serviço."""
    trace_id = request.headers.get(CABECALHO_TRACE_ID) or gerar_trace_id()
    definir_trace_id(trace_id)

    async with iniciar_span(
        coletor_spans, nome=f"{request.method} {request.url.path}", servico=NOME_SERVICO
    ) as span:
        resposta = await chamar_proximo(request)

    resposta.headers[CABECALHO_TRACE_ID] = trace_id

    rota_agregavel = request.scope["route"].path if request.scope.get("route") else request.url.path
    registrar_log(
        "requisicao_concluida",
        NOME_SERVICO,
        caminho=request.url.path,
        metodo=request.method,
        status_code=resposta.status_code,
        duracao_ms=round(span.duracao_ms, 2),
    )
    contador_requisicoes.incrementar(
        rota=rota_agregavel, metodo=request.method, status_code=str(resposta.status_code)
    )
    return resposta


async def _buscar_lista_best_effort(url: str, nome_span: str) -> list[dict[str, Any]]:
    """As consultas auxiliares (reservas, cobranças, remessas) toleram
    falha: se um desses serviços estiver fora do ar, a composição não
    falha por inteiro — só aquela seção volta vazia. A consulta ao pedido
    em si, em `resumo_do_pedido`, é a única obrigatória.

    Até a Aula 12, esta chamada não propagava o trace_id — o gateway
    gerava (ou recebia) o identificador na borda e o perdia exatamente no
    primeiro salto. É a lacuna que este `headers=` fecha (Aula 13)."""
    async with iniciar_span(coletor_spans, nome_span, NOME_SERVICO):
        try:
            resposta = await _cliente_http.get(
                url, timeout=2.0, headers={CABECALHO_TRACE_ID: obter_trace_id()}
            )
            if resposta.status_code == 200:
                return resposta.json()
        except httpx.HTTPError:
            pass
    return []


@app.get("/pedidos/{pedido_id}/resumo")
async def resumo_do_pedido(pedido_id: str) -> dict[str, Any]:
    """Um único ponto de entrada para o que, internamente, são quatro
    serviços com quatro bancos independentes. Compare com o exemplo do
    roteiro: 'a tela de detalhes do pedido precisa de dados de pedidos,
    estoque e expedição — o gateway consulta os três e devolve uma
    resposta única'."""
    try:
        async with iniciar_span(coletor_spans, "buscar_pedido", NOME_SERVICO):
            resposta_pedido = await _cliente_http.get(
                f"{PEDIDOS_BASE_URL}/pedidos/{pedido_id}",
                timeout=2.0,
                headers={CABECALHO_TRACE_ID: obter_trace_id()},
            )
    except httpx.HTTPError as erro:
        raise HTTPException(status_code=503, detail=f"serviço de pedidos indisponível: {erro}") from erro

    if resposta_pedido.status_code == 404:
        raise HTTPException(status_code=404, detail="pedido não encontrado")
    if resposta_pedido.status_code >= 500:
        raise HTTPException(status_code=503, detail="serviço de pedidos retornou erro")

    pedido = resposta_pedido.json()

    # As três chamadas rodam concorrentemente: cada uma abre seu próprio
    # span filho do span raiz desta requisição, mas os intervalos de tempo
    # se sobrepõem — a soma das três não é o tempo total gasto aqui, ao
    # contrário do que aconteceria se fossem sequenciais (ver
    # scripts/reconstruir_trace.py para o cuidado de leitura equivalente
    # no caso sequencial da saga de compra).
    reservas, cobrancas, remessas = await asyncio.gather(
        _buscar_lista_best_effort(f"{ESTOQUE_BASE_URL}/reservas/por-pedido/{pedido_id}", "buscar_reservas"),
        _buscar_lista_best_effort(f"{PAGAMENTO_BASE_URL}/cobrancas/por-pedido/{pedido_id}", "buscar_cobrancas"),
        _buscar_lista_best_effort(f"{EXPEDICAO_BASE_URL}/remessas/por-pedido/{pedido_id}", "buscar_remessas"),
    )

    return {
        "pedido": pedido,
        "reservas": reservas,
        "cobrancas": cobrancas,
        "remessas": remessas,
    }


@app.get("/_admin/spans/{trace_id}")
async def spans_do_trace(trace_id: str) -> list[dict[str, Any]]:
    return coletor_spans.spans_do_trace(trace_id)


@app.get("/_admin/metricas")
async def metricas() -> dict[str, Any]:
    return {"http_requisicoes_total": contador_requisicoes.total()}


@app.get("/saude")
async def saude() -> dict[str, Any]:
    """Sonda de vivacidade (Aula 11): o gateway não tem estado próprio, só
    precisa responder — nunca falha por causa de outro serviço."""
    return {"status": "ok"}


@app.get("/pronto")
async def pronto(response: Response) -> dict[str, Any]:
    """Sonda de prontidão (Aula 11): diferente da vivacidade, aqui faz
    sentido checar a dependência obrigatória — sem `pedidos` alcançável,
    o gateway não consegue cumprir sua única função."""
    try:
        resposta = await _cliente_http.get(f"{PEDIDOS_BASE_URL}/saude", timeout=1.0)
        pedidos_alcancavel = resposta.status_code == 200
    except httpx.HTTPError:
        pedidos_alcancavel = False

    if not pedidos_alcancavel:
        response.status_code = 503
    return {"pronto": pedidos_alcancavel}
