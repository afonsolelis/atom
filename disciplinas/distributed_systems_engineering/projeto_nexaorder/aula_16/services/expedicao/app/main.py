"""Serviço Expedição — Unidade 2, Aula 8.

Último passo da saga: gerar etiqueta de expedição, de forma idempotente, com
compensação (cancelar) para o caso de a etiqueta precisar ser desfeita antes
do despacho — depois disso, a compensação deixaria de ser possível e viraria
logística reversa, um processo diferente e fora do escopo deste projeto.
"""

from __future__ import annotations

import os
import random
from typing import Any

from fastapi import Depends, FastAPI, HTTPException, Request, Response
from fastapi.concurrency import run_in_threadpool
from pydantic import BaseModel

from .correlation import CABECALHO_TRACE_ID, definir_trace_id, gerar_trace_id
from .logs_estruturados import registrar as registrar_log
from .metricas import ContadorComRotulos
from .seguranca import exigir_identidade
from .store import RepositorioExpedicao
from .tracing import ColetorDeSpans, iniciar_span

CAMINHO_BANCO = os.environ.get("EXPEDICAO_DB_PATH", "expedicao.db")
NOME_SERVICO = "expedicao"

app = FastAPI(title="NexaOrder — Expedição", version="0.13.0")
repositorio = RepositorioExpedicao(CAMINHO_BANCO)
coletor_spans = ColetorDeSpans()
contador_requisicoes = ContadorComRotulos(
    nome="http_requisicoes_total", dimensoes_permitidas=frozenset({"rota", "metodo", "status_code"})
)


@app.middleware("http")
async def middleware_observabilidade(request: Request, chamar_proximo):
    """Ver services/pedidos/app/main.py — o mesmo mecanismo, disponível em
    cada serviço (ver docs/observabilidade.md). A expedição só entra no
    caminho crítico da compra de forma assíncrona (Aula 8/10); seu próprio
    span raiz, por isso, tipicamente começa depois que o cliente já
    recebeu resposta — ver scripts/reconstruir_trace.py."""
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


class ConfiguracaoFalha(BaseModel):
    falhar_percentual: int = 0


class SolicitarRequest(BaseModel):
    pedido_id: str
    chave_idempotencia: str


_config_falha = ConfiguracaoFalha()


@app.post("/_debug/config")
async def configurar_falha(config: ConfiguracaoFalha) -> ConfiguracaoFalha:
    global _config_falha
    _config_falha = config
    return _config_falha


@app.post("/remessas", status_code=201)
async def solicitar_remessa(
    corpo: SolicitarRequest, identidade: str = Depends(exigir_identidade({"pedidos"}))
) -> dict[str, Any]:
    existente = await run_in_threadpool(
        repositorio.obter_por_chave_idempotencia, corpo.chave_idempotencia
    )
    if existente is not None:
        return existente

    if random.randint(1, 100) <= _config_falha.falhar_percentual:
        raise HTTPException(status_code=503, detail="expedição indisponível (falha simulada)")

    return await run_in_threadpool(
        repositorio.criar_remessa, corpo.pedido_id, corpo.chave_idempotencia
    )


@app.post("/remessas/{remessa_id}/cancelar")
async def cancelar_remessa(
    remessa_id: str, identidade: str = Depends(exigir_identidade({"pedidos"}))
) -> dict[str, Any]:
    remessa = await run_in_threadpool(repositorio.obter_por_id, remessa_id)
    if remessa is None:
        raise HTTPException(status_code=404, detail="remessa não encontrada")

    return await run_in_threadpool(repositorio.cancelar, remessa_id)


@app.get("/remessas/por-pedido/{pedido_id}")
async def listar_remessas_do_pedido(pedido_id: str) -> list[dict[str, Any]]:
    """Consulta usada pelo gateway (Aula 9)."""
    return await run_in_threadpool(repositorio.listar_por_pedido, pedido_id)


@app.get("/_admin/spans/{trace_id}")
async def spans_do_trace(trace_id: str) -> list[dict[str, Any]]:
    return coletor_spans.spans_do_trace(trace_id)


@app.get("/_admin/metricas")
async def metricas() -> dict[str, Any]:
    return {"http_requisicoes_total": contador_requisicoes.total()}


@app.get("/saude")
async def saude() -> dict[str, Any]:
    """Sonda de vivacidade (Aula 11)."""
    return {"status": "ok", "config_falha_ativa": _config_falha.model_dump()}


@app.get("/pronto")
async def pronto(response: Response) -> dict[str, Any]:
    """Sonda de prontidão (Aula 11): confirma acesso ao banco."""
    banco_acessivel = await run_in_threadpool(repositorio.verificar_conexao)
    if not banco_acessivel:
        response.status_code = 503
    return {"pronto": banco_acessivel}
