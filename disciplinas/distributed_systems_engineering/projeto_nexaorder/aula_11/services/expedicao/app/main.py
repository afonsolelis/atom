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

from fastapi import FastAPI, HTTPException, Response
from fastapi.concurrency import run_in_threadpool
from pydantic import BaseModel

from .store import RepositorioExpedicao

CAMINHO_BANCO = os.environ.get("EXPEDICAO_DB_PATH", "expedicao.db")

app = FastAPI(title="NexaOrder — Expedição", version="0.8.0")
repositorio = RepositorioExpedicao(CAMINHO_BANCO)


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
async def solicitar_remessa(corpo: SolicitarRequest) -> dict[str, Any]:
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
async def cancelar_remessa(remessa_id: str) -> dict[str, Any]:
    remessa = await run_in_threadpool(repositorio.obter_por_id, remessa_id)
    if remessa is None:
        raise HTTPException(status_code=404, detail="remessa não encontrada")

    return await run_in_threadpool(repositorio.cancelar, remessa_id)


@app.get("/remessas/por-pedido/{pedido_id}")
async def listar_remessas_do_pedido(pedido_id: str) -> list[dict[str, Any]]:
    """Consulta usada pelo gateway (Aula 9)."""
    return await run_in_threadpool(repositorio.listar_por_pedido, pedido_id)


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
