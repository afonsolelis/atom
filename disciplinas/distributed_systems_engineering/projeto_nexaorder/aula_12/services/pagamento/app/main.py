"""Serviço Pagamento — Unidade 2, Aula 8.

Autoriza cobranças de forma idempotente (o inbox da Aula 8: a chave de
idempotência decide se uma requisição repetida cria uma nova cobrança ou
devolve a existente) e expõe uma compensação — estornar — para quando uma
etapa posterior da saga falhar.

Mantém a injeção de falha por depuração, no mesmo espírito das Aulas 4/5,
para permitir demonstrar a saga compensando em aula.
"""

from __future__ import annotations

import os
import random
import uuid
from typing import Any

from fastapi import Depends, FastAPI, HTTPException, Response
from fastapi.concurrency import run_in_threadpool
from pydantic import BaseModel

from .seguranca import exigir_identidade
from .store import RepositorioPagamento

CAMINHO_BANCO = os.environ.get("PAGAMENTO_DB_PATH", "pagamento.db")

app = FastAPI(title="NexaOrder — Pagamento", version="0.12.0")
repositorio = RepositorioPagamento(CAMINHO_BANCO)


class ConfiguracaoFalha(BaseModel):
    falhar_percentual: int = 0


class AutorizarRequest(BaseModel):
    pedido_id: str
    chave_idempotencia: str
    valor: float


_config_falha = ConfiguracaoFalha()


@app.post("/_debug/config")
async def configurar_falha(config: ConfiguracaoFalha) -> ConfiguracaoFalha:
    global _config_falha
    _config_falha = config
    return _config_falha


@app.post("/cobrancas", status_code=201)
async def autorizar(
    corpo: AutorizarRequest, identidade: str = Depends(exigir_identidade({"pedidos"}))
) -> dict[str, Any]:
    existente = await run_in_threadpool(
        repositorio.obter_por_chave_idempotencia, corpo.chave_idempotencia
    )
    if existente is not None:
        # O inbox: a mesma chave nunca gera uma segunda cobrança, mesmo sob
        # retentativa da saga orquestradora.
        return existente

    if random.randint(1, 100) <= _config_falha.falhar_percentual:
        raise HTTPException(status_code=503, detail="pagamento indisponível (falha simulada)")

    cobranca = await run_in_threadpool(
        repositorio.criar_cobranca,
        corpo.pedido_id,
        corpo.chave_idempotencia,
        corpo.valor,
        "AUTORIZADA",
        f"prov-{uuid.uuid4().hex[:8]}",
    )
    return cobranca


@app.post("/cobrancas/{cobranca_id}/estornar")
async def estornar(
    cobranca_id: str, identidade: str = Depends(exigir_identidade({"pedidos"}))
) -> dict[str, Any]:
    """Ação compensatória. Note o que ela não é: não é o inverso perfeito
    de autorizar. Em um provedor real, estornar tem taxas e prazos
    diferentes de nunca ter cobrado (ver docs/saga.md).

    A partir da Aula 12, só a identidade 'pedidos' pode chamar esta rota —
    é exatamente a proteção que faltava na situação-problema do roteiro
    ('nada impede que a expedição chame pagamento e peça um reembolso').
    Ver tests/test_seguranca.py."""
    cobranca = await run_in_threadpool(repositorio.obter_por_id, cobranca_id)
    if cobranca is None:
        raise HTTPException(status_code=404, detail="cobrança não encontrada")

    atualizada = await run_in_threadpool(repositorio.estornar, cobranca_id)
    return atualizada


@app.get("/cobrancas/por-pedido/{pedido_id}")
async def listar_cobrancas_do_pedido(pedido_id: str) -> list[dict[str, Any]]:
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
