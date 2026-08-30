"""Serviço Pedidos (Aulas 3, 4, 8 e 10).

Implementa o contrato de docs/contratos/api-pedidos.md: criar pedido (com
idempotência) e consultar pedido. Cada requisição recebe ou propaga um
trace_id e avança o relógio lógico de Lamport do processo.

A partir da Aula 4, reservar estoque é uma chamada de rede real, protegida
por timeout, retry com backoff e disjuntor. A partir da Aula 8,
`POST /pedidos/{id}/finalizar-compra` orquestra a saga completa — estoque,
pagamento e expedição — com compensação automática em caso de falha
(docs/saga.md). A partir da Aula 10, `POST /_admin/publicar-eventos` fecha
o padrão outbox: publica os eventos pendentes no tópico particionado por
pedido_id (docs/arquitetura-eventos.md).
"""

from __future__ import annotations

import os
import uuid
from typing import Any

import httpx
from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.concurrency import run_in_threadpool

from .barramento import GrupoConsumidores, Topico
from .correlation import CABECALHO_TRACE_ID, definir_trace_id, gerar_trace_id, obter_trace_id
from .lamport import LamportClock
from .logs_estruturados import registrar as registrar_log
from .metricas import ContadorComRotulos
from .models import CriarPedidoRequest, EstadoPedido, PedidoResponse
from .publicador import NOME_TOPICO_PEDIDOS, NUM_PARTICOES_PEDIDOS, publicar_eventos_pendentes
from .resiliencia import CircuitBreaker, CircuitoAberto, ClienteResiliente, FalhaTransitoria
from .saga import EtapaFalhou, SagaCompra
from .seguranca import emitir_token
from .store import RepositorioPedidos
from .tracing import ColetorDeSpans, iniciar_span

IDENTIDADE_PROPRIA = "pedidos"
NOME_SERVICO = "pedidos"
_CABECALHO_IDENTIDADE = {"Authorization": f"Bearer {emitir_token(IDENTIDADE_PROPRIA)}"}

CAMINHO_BANCO = os.environ.get("PEDIDOS_DB_PATH", "pedidos.db")
ESTOQUE_BASE_URL = os.environ.get("ESTOQUE_BASE_URL", "http://localhost:8002")
PAGAMENTO_BASE_URL = os.environ.get("PAGAMENTO_BASE_URL", "http://localhost:8003")
EXPEDICAO_BASE_URL = os.environ.get("EXPEDICAO_BASE_URL", "http://localhost:8004")

app = FastAPI(title="NexaOrder — Pedidos", version="0.13.0")
repositorio = RepositorioPedidos(CAMINHO_BANCO)
relogio = LamportClock()
topico_eventos = Topico(nome=NOME_TOPICO_PEDIDOS, num_particoes=NUM_PARTICOES_PEDIDOS)
grupo_auditoria = GrupoConsumidores(topico_eventos, "auditoria", instancias=["auditoria-0"])
coletor_spans = ColetorDeSpans()
contador_requisicoes = ContadorComRotulos(
    nome="http_requisicoes_total", dimensoes_permitidas=frozenset({"rota", "metodo", "status_code"})
)

_cliente_http = httpx.AsyncClient()
_disjuntor_estoque = CircuitBreaker()
_cliente_estoque = ClienteResiliente(_cliente_http, _disjuntor_estoque)
_disjuntor_pagamento = CircuitBreaker()
_cliente_pagamento = ClienteResiliente(_cliente_http, _disjuntor_pagamento)
_disjuntor_expedicao = CircuitBreaker()
_cliente_expedicao = ClienteResiliente(_cliente_http, _disjuntor_expedicao)


@app.middleware("http")
async def middleware_observabilidade(request: Request, chamar_proximo):
    """Gera ou propaga o trace_id (Aula 3), mede um span raiz real para a
    requisição inteira (Aula 13) e fecha com um log estruturado e uma
    métrica de baixa cardinalidade — os três pilares na mesma passagem.
    Ver docs/observabilidade.md."""
    trace_id = request.headers.get(CABECALHO_TRACE_ID) or gerar_trace_id()
    definir_trace_id(trace_id)

    async with iniciar_span(
        coletor_spans, nome=f"{request.method} {request.url.path}", servico=NOME_SERVICO
    ) as span:
        resposta = await chamar_proximo(request)

    resposta.headers[CABECALHO_TRACE_ID] = trace_id

    # Métricas usam a rota agregável ("/pedidos/{pedido_id}"), nunca o
    # caminho exato ("/pedidos/3f2a..."): é essa distinção que evita o
    # erro de cardinalidade do roteiro. O span acima, em contraste, usa o
    # caminho exato de propósito — em um trace, individualizar é o ponto.
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


def _para_resposta(pedido: dict[str, Any]) -> PedidoResponse:
    return PedidoResponse(
        id=pedido["id"],
        cliente_id=pedido["cliente_id"],
        estado=EstadoPedido(pedido["estado"]),
        itens=pedido["itens"],
        total=pedido["total"],
        criado_em=pedido["criado_em"],
        trace_id=pedido["trace_id"],
        carimbo_lamport=pedido["carimbo_lamport"],
    )


@app.post("/pedidos", status_code=201)
async def criar_pedido(corpo: CriarPedidoRequest):
    existente = await run_in_threadpool(
        repositorio.obter_por_chave_idempotencia, corpo.chave_idempotencia
    )
    if existente is not None:
        return _para_resposta(existente)

    # Regra 1 de Lamport: criar o pedido é um evento local.
    carimbo = relogio.evento_local()

    pedido = {
        "id": str(uuid.uuid4()),
        "cliente_id": str(corpo.cliente_id),
        "chave_idempotencia": corpo.chave_idempotencia,
        "estado": EstadoPedido.RECEBIDO.value,
        "itens": [item.model_dump() for item in corpo.itens],
        "total": sum(item.quantidade * item.preco_unitario for item in corpo.itens),
        "criado_em": PedidoResponse.agora().isoformat(),
        "trace_id": obter_trace_id(),
        "carimbo_lamport": carimbo,
    }
    await run_in_threadpool(repositorio.salvar, pedido)
    return _para_resposta(pedido)


@app.get("/pedidos/{pedido_id}")
async def obter_pedido(pedido_id: str):
    pedido = await run_in_threadpool(repositorio.obter_por_id, pedido_id)
    if pedido is None:
        raise HTTPException(status_code=404, detail="pedido não encontrado")
    return _para_resposta(pedido)


@app.post("/pedidos/{pedido_id}/reservar-estoque")
async def reservar_estoque(pedido_id: str):
    """Chama o serviço Estoque para reservar os itens do pedido.

    Mantido como rota independente desde a Aula 4 — a saga da Aula 8
    reutiliza a mesma lógica internamente, por meio de `_reservar_estoque`.
    """
    pedido = await run_in_threadpool(repositorio.obter_por_id, pedido_id)
    if pedido is None:
        raise HTTPException(status_code=404, detail="pedido não encontrado")

    try:
        resultado = await _reservar_estoque(pedido)
    except EtapaFalhou as erro:
        raise HTTPException(status_code=503, detail=str(erro)) from erro

    await run_in_threadpool(repositorio.atualizar_estado, pedido_id, EstadoPedido.RESERVADO.value)
    return {"pedido_id": pedido_id, "estado": "RESERVADO", "reserva": resultado}


# --- Etapas da saga, cada uma convertendo falhas de rede em EtapaFalhou ---
# É essa conversão que permite que app/saga.py não precise conhecer HTTP,
# disjuntor ou timeout — apenas "a etapa funcionou" ou "a etapa falhou".


async def _reservar_estoque(pedido: dict[str, Any]) -> dict[str, Any]:
    if not _disjuntor_estoque.permite_chamada():
        raise EtapaFalhou("disjuntor aberto para o serviço de estoque")
    item = pedido["itens"][0]
    async with iniciar_span(coletor_spans, "reservar_estoque", NOME_SERVICO):
        try:
            resposta = await _cliente_estoque.post(
                f"{ESTOQUE_BASE_URL}/reservas",
                json={"pedido_id": pedido["id"], "sku": item["sku"], "quantidade": item["quantidade"]},
                trace_id=pedido["trace_id"],
                cabecalhos_extras=_CABECALHO_IDENTIDADE,
            )
        except (CircuitoAberto, httpx.TransportError, FalhaTransitoria) as erro:
            raise EtapaFalhou(f"reservar estoque falhou: {erro}") from erro
    return resposta.json()


async def _liberar_estoque(reserva_id: str, trace_id: str) -> None:
    async with iniciar_span(coletor_spans, "compensar_liberar_estoque", NOME_SERVICO):
        try:
            await _cliente_estoque.post(
                f"{ESTOQUE_BASE_URL}/reservas/{reserva_id}/liberar",
                json={},
                trace_id=trace_id,
                cabecalhos_extras=_CABECALHO_IDENTIDADE,
            )
        except (CircuitoAberto, httpx.TransportError, FalhaTransitoria):
            # Compensação que falha é, por si só, um incidente a ser observado
            # (Aula 13) — mas não deve lançar de volta e travar a saga.
            pass


async def _autorizar_pagamento(pedido: dict[str, Any]) -> dict[str, Any]:
    if not _disjuntor_pagamento.permite_chamada():
        raise EtapaFalhou("disjuntor aberto para o serviço de pagamento")
    chave = f"{pedido['id']}:pagamento"
    async with iniciar_span(coletor_spans, "autorizar_pagamento", NOME_SERVICO):
        try:
            resposta = await _cliente_pagamento.post(
                f"{PAGAMENTO_BASE_URL}/cobrancas",
                json={"pedido_id": pedido["id"], "chave_idempotencia": chave, "valor": pedido["total"]},
                trace_id=pedido["trace_id"],
                cabecalhos_extras=_CABECALHO_IDENTIDADE,
            )
        except (CircuitoAberto, httpx.TransportError, FalhaTransitoria) as erro:
            raise EtapaFalhou(f"autorizar pagamento falhou: {erro}") from erro
    return resposta.json()


async def _estornar_pagamento(cobranca_id: str, trace_id: str) -> None:
    async with iniciar_span(coletor_spans, "compensar_estornar_pagamento", NOME_SERVICO):
        try:
            await _cliente_pagamento.post(
                f"{PAGAMENTO_BASE_URL}/cobrancas/{cobranca_id}/estornar",
                json={},
                trace_id=trace_id,
                cabecalhos_extras=_CABECALHO_IDENTIDADE,
            )
        except (CircuitoAberto, httpx.TransportError, FalhaTransitoria):
            pass


async def _solicitar_expedicao(pedido: dict[str, Any]) -> dict[str, Any]:
    if not _disjuntor_expedicao.permite_chamada():
        raise EtapaFalhou("disjuntor aberto para o serviço de expedição")
    chave = f"{pedido['id']}:expedicao"
    async with iniciar_span(coletor_spans, "solicitar_expedicao", NOME_SERVICO):
        try:
            resposta = await _cliente_expedicao.post(
                f"{EXPEDICAO_BASE_URL}/remessas",
                json={"pedido_id": pedido["id"], "chave_idempotencia": chave},
                trace_id=pedido["trace_id"],
                cabecalhos_extras=_CABECALHO_IDENTIDADE,
            )
        except (CircuitoAberto, httpx.TransportError, FalhaTransitoria) as erro:
            raise EtapaFalhou(f"solicitar expedição falhou: {erro}") from erro
    return resposta.json()


@app.post("/pedidos/{pedido_id}/finalizar-compra")
async def finalizar_compra(pedido_id: str):
    """Orquestra a saga completa: reservar estoque, autorizar pagamento,
    solicitar expedição — com compensação automática em cascata se
    qualquer etapa falhar. Ver docs/saga.md."""
    pedido = await run_in_threadpool(repositorio.obter_por_id, pedido_id)
    if pedido is None:
        raise HTTPException(status_code=404, detail="pedido não encontrado")

    saga = SagaCompra(
        reservar_estoque=lambda: _reservar_estoque(pedido),
        liberar_estoque=lambda reserva_id: _liberar_estoque(reserva_id, pedido["trace_id"]),
        autorizar_pagamento=lambda: _autorizar_pagamento(pedido),
        estornar_pagamento=lambda cobranca_id: _estornar_pagamento(cobranca_id, pedido["trace_id"]),
        solicitar_expedicao=lambda: _solicitar_expedicao(pedido),
    )
    resultado = await saga.executar()

    await run_in_threadpool(repositorio.atualizar_estado, pedido_id, resultado.estado_final)

    return {
        "pedido_id": pedido_id,
        "sucesso": resultado.sucesso,
        "estado_final": resultado.estado_final,
        "reserva_id": resultado.reserva_id,
        "cobranca_id": resultado.cobranca_id,
        "remessa_id": resultado.remessa_id,
        "falhou_em": resultado.falhou_em,
        "compensacoes": [{"nome": c.nome, "referencia": c.referencia} for c in resultado.compensacoes],
    }


@app.post("/_admin/publicar-eventos")
async def publicar_eventos():
    """Fecha o padrão outbox (Aula 8 + Aula 10): publica os eventos
    pendentes no tópico particionado por pedido_id. Em produção isto
    rodaria em um laço contínuo; aqui é acionado explicitamente para que o
    projeto não dependa de um agendador em segundo plano."""
    ids_publicados = await run_in_threadpool(publicar_eventos_pendentes, repositorio, topico_eventos)
    return {"eventos_publicados": len(ids_publicados), "ids": ids_publicados}


@app.get("/_admin/auditoria/consumir")
async def consumir_auditoria():
    """Demonstra um grupo de consumidores real lendo o tópico: cada
    chamada avança o deslocamento do grupo 'auditoria' e devolve só os
    eventos novos desde a última leitura."""
    eventos = await run_in_threadpool(grupo_auditoria.consumir, "auditoria-0")
    return {
        "eventos": [
            {"chave": e.chave, "tipo": e.tipo, "offset": e.offset, "payload": e.payload} for e in eventos
        ]
    }


@app.get("/_admin/spans/{trace_id}")
async def spans_do_trace(trace_id: str) -> list[dict[str, Any]]:
    """Expõe os spans que este processo registrou para um trace_id — a
    peça que, agregada com os spans dos outros serviços, reconstrói a
    cascata de uma jornada completa (ver scripts/reconstruir_trace.py e
    docs/adr/0013-spans-locais-sem-coletor-central.md)."""
    return coletor_spans.spans_do_trace(trace_id)


@app.get("/_admin/metricas")
async def metricas() -> dict[str, Any]:
    """Métricas agregadas por dimensões de baixa cardinalidade — nunca por
    trace_id ou pedido_id (ver app/metricas.py)."""
    return {"http_requisicoes_total": contador_requisicoes.total()}


@app.get("/saude")
async def saude():
    """Sonda de vivacidade (Aula 11)."""
    return {
        "status": "ok",
        "carimbo_lamport": relogio.valor,
        "disjuntor_estoque": _disjuntor_estoque.estado,
        "disjuntor_pagamento": _disjuntor_pagamento.estado,
        "disjuntor_expedicao": _disjuntor_expedicao.estado,
    }


@app.get("/pronto")
async def pronto(response: Response):
    """Sonda de prontidão (Aula 11): confirma acesso ao banco."""
    banco_acessivel = await run_in_threadpool(repositorio.verificar_conexao)
    if not banco_acessivel:
        response.status_code = 503
    return {"pronto": banco_acessivel}
