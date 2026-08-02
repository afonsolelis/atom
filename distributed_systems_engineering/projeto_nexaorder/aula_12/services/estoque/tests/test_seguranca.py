"""Testa identidade, autorização e o balde de fichas — Unidade 3, Aula 12."""

from __future__ import annotations

import pytest
from fastapi import HTTPException

from app.seguranca import BaldeDeFichas, TokenInvalido, emitir_token, exigir_identidade, verificar_token


def test_token_emitido_e_verificavel():
    token = emitir_token("pedidos")

    identidade = verificar_token(token)

    assert identidade == "pedidos"


def test_token_adulterado_e_rejeitado():
    token = emitir_token("pedidos")
    token_adulterado = token[:-1] + ("0" if token[-1] != "0" else "1")

    with pytest.raises(TokenInvalido):
        verificar_token(token_adulterado)


def test_token_mal_formado_e_rejeitado():
    with pytest.raises(TokenInvalido):
        verificar_token("isto-nao-e-um-token-valido")


@pytest.mark.asyncio
async def test_exigir_identidade_aceita_identidade_permitida():
    dependencia = exigir_identidade({"pedidos"})
    token = emitir_token("pedidos")

    identidade = await dependencia(authorization=f"Bearer {token}")

    assert identidade == "pedidos"


@pytest.mark.asyncio
async def test_exigir_identidade_recusa_identidade_nao_permitida():
    """A prova central da Aula 12: uma identidade autenticada, mas não
    autorizada para esta operação específica, recebe 403 — não 401.
    Autenticação e autorização são perguntas diferentes."""
    dependencia = exigir_identidade({"pedidos"})
    token = emitir_token("expedicao")

    with pytest.raises(HTTPException) as excinfo:
        await dependencia(authorization=f"Bearer {token}")

    assert excinfo.value.status_code == 403


@pytest.mark.asyncio
async def test_exigir_identidade_recusa_ausencia_de_cabecalho():
    dependencia = exigir_identidade({"pedidos"})

    with pytest.raises(HTTPException) as excinfo:
        await dependencia(authorization=None)

    assert excinfo.value.status_code == 401


@pytest.mark.asyncio
async def test_exigir_identidade_recusa_token_forjado():
    dependencia = exigir_identidade({"pedidos"})

    with pytest.raises(HTTPException) as excinfo:
        await dependencia(authorization="Bearer pedidos.assinatura-forjada")

    assert excinfo.value.status_code == 401


# --- Balde de fichas -------------------------------------------------------


def test_balde_absorve_ate_a_capacidade_e_recusa_o_resto():
    """Reproduz o exemplo numérico da Aula 12: capacidade 50, chegam 90
    requisições de uma vez — as primeiras 50 são aceitas, as 40
    seguintes são recusadas (a reposição ainda não teve tempo de agir)."""
    balde = BaldeDeFichas(capacidade=50, taxa_reposicao_por_segundo=20)

    aceitas = sum(1 for _ in range(90) if balde.consumir())

    assert aceitas == 50


def test_balde_repoe_fichas_ao_longo_do_tempo():
    import time

    balde = BaldeDeFichas(capacidade=10, taxa_reposicao_por_segundo=100)  # repõe rápido para o teste
    for _ in range(10):
        balde.consumir()
    assert balde.consumir() is False  # esgotado

    time.sleep(0.05)  # tempo suficiente para repor pelo menos 1 ficha a 100/s

    assert balde.consumir() is True


def test_limitador_de_taxa_protege_reservas_de_verdade_via_http(cliente_api):
    """A mesma prova do exemplo numérico, agora batendo na rota HTTP real:
    90 chamadas a /reservas — a capacidade de 50 absorve a maior parte da
    rajada, e o restante é recusado com 429. A tolerância de +/- alguns
    aceites existe porque, ao contrário do teste puro de BaldeDeFichas,
    90 chamadas HTTP sequenciais levam tempo real o suficiente para repor
    uma ficha ou duas a 20/s — o próprio efeito que a Aula 12 descreve."""
    cliente_api.post("/estoque/TECLADO-MEC-01/inicializar", json={"quantidade": 1000})

    resultados = [
        cliente_api.post(
            "/reservas", json={"pedido_id": f"p{i}", "sku": "TECLADO-MEC-01", "quantidade": 1}
        ).status_code
        for i in range(90)
    ]

    recusadas_por_limite = sum(1 for codigo in resultados if codigo == 429)
    aceitas = sum(1 for codigo in resultados if codigo == 201)

    assert 50 <= aceitas <= 55
    assert recusadas_por_limite >= 35
    assert aceitas + recusadas_por_limite == 90
