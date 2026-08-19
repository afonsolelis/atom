"""Testa a orquestração da saga isoladamente, com etapas simuladas por
funções assíncronas — sem HTTP, sem os outros serviços. A integração de
ponta a ponta, com os três serviços reais, está em test_saga_integracao.py."""

from __future__ import annotations

import pytest

from app.saga import EtapaFalhou, SagaCompra


def _saga_com_etapas(
    reservar_ok=True, pagamento_ok=True, expedicao_ok=True
) -> tuple[SagaCompra, dict]:
    chamadas = {"liberar_estoque": [], "estornar_pagamento": []}

    async def reservar_estoque():
        if not reservar_ok:
            raise EtapaFalhou("estoque indisponível")
        return {"reserva_id": "reserva-1"}

    async def liberar_estoque(reserva_id):
        chamadas["liberar_estoque"].append(reserva_id)

    async def autorizar_pagamento():
        if not pagamento_ok:
            raise EtapaFalhou("pagamento recusado")
        return {"id": "cobranca-1"}

    async def estornar_pagamento(cobranca_id):
        chamadas["estornar_pagamento"].append(cobranca_id)

    async def solicitar_expedicao():
        if not expedicao_ok:
            raise EtapaFalhou("expedição indisponível")
        return {"id": "remessa-1"}

    saga = SagaCompra(
        reservar_estoque=reservar_estoque,
        liberar_estoque=liberar_estoque,
        autorizar_pagamento=autorizar_pagamento,
        estornar_pagamento=estornar_pagamento,
        solicitar_expedicao=solicitar_expedicao,
    )
    return saga, chamadas


@pytest.mark.asyncio
async def test_caminho_feliz_conclui_em_expedido():
    saga, chamadas = _saga_com_etapas()

    resultado = await saga.executar()

    assert resultado.sucesso is True
    assert resultado.estado_final == "EXPEDIDO"
    assert resultado.reserva_id == "reserva-1"
    assert resultado.cobranca_id == "cobranca-1"
    assert resultado.remessa_id == "remessa-1"
    assert chamadas["liberar_estoque"] == []
    assert chamadas["estornar_pagamento"] == []


@pytest.mark.asyncio
async def test_falha_ao_reservar_estoque_nao_aciona_nenhuma_compensacao():
    saga, chamadas = _saga_com_etapas(reservar_ok=False)

    resultado = await saga.executar()

    assert resultado.sucesso is False
    assert resultado.estado_final == "RECEBIDO"
    assert resultado.falhou_em == "reservar_estoque"
    assert resultado.compensacoes == []


@pytest.mark.asyncio
async def test_falha_no_pagamento_libera_a_reserva_de_estoque():
    saga, chamadas = _saga_com_etapas(pagamento_ok=False)

    resultado = await saga.executar()

    assert resultado.sucesso is False
    assert resultado.estado_final == "RECEBIDO"
    assert resultado.falhou_em == "autorizar_pagamento"
    assert chamadas["liberar_estoque"] == ["reserva-1"]
    assert chamadas["estornar_pagamento"] == []


@pytest.mark.asyncio
async def test_falha_na_expedicao_estorna_pagamento_e_libera_estoque():
    """O cenário mais interessante do roteiro: a compensação em cascata."""
    saga, chamadas = _saga_com_etapas(expedicao_ok=False)

    resultado = await saga.executar()

    assert resultado.sucesso is False
    assert resultado.estado_final == "PAGO"
    assert resultado.falhou_em == "solicitar_expedicao"
    assert chamadas["estornar_pagamento"] == ["cobranca-1"]
    assert chamadas["liberar_estoque"] == ["reserva-1"]
    nomes_das_compensacoes = [c.nome for c in resultado.compensacoes]
    assert nomes_das_compensacoes == ["estornar_pagamento", "liberar_estoque"]
