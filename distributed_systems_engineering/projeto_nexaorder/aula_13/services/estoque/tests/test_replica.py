"""Reproduz a janela de leitura obsoleta descrita no roteiro da Aula 5."""

from __future__ import annotations

import asyncio
import time

import pytest

from app.replica import ReplicaLeitura


@pytest.mark.asyncio
async def test_leitura_eventual_e_none_antes_da_propagacao_chegar():
    replica = ReplicaLeitura(atraso_segundos=0.1)

    replica.propagar("SKU-1", 10)

    # Imediatamente após a escrita, a réplica ainda não recebeu o valor.
    assert replica.ler("SKU-1") is None


@pytest.mark.asyncio
async def test_leitura_eventual_reflete_o_valor_apos_o_atraso():
    replica = ReplicaLeitura(atraso_segundos=0.05)

    replica.propagar("SKU-1", 10)
    await asyncio.sleep(0.07)

    assert replica.ler("SKU-1") == 10


@pytest.mark.asyncio
async def test_atraso_padrao_e_150ms_como_no_roteiro_da_aula_5():
    assert ReplicaLeitura.ATRASO_PADRAO_SEGUNDOS == pytest.approx(0.150)

    replica = ReplicaLeitura()  # usa o atraso padrão
    inicio = time.monotonic()
    replica.propagar("SKU-X", 7)

    while replica.ler("SKU-X") is None:
        await asyncio.sleep(0.01)

    decorrido = time.monotonic() - inicio
    assert decorrido >= 0.150


@pytest.mark.asyncio
async def test_leituras_sucessivas_convergem_apos_cessarem_as_escritas():
    """'Cessadas as escritas, as réplicas convergem para o mesmo valor'
    — a definição de consistência eventual da Aula 5. As escritas são
    aplicadas uma de cada vez, aguardando cada propagação terminar, para
    que a ordem de chegada na réplica seja determinística neste teste."""
    replica = ReplicaLeitura(atraso_segundos=0.02)

    for valor in (1, 2, 3):
        replica.propagar("SKU-1", valor)
        await replica.aguardar_propagacao_pendente()

    assert replica.ler("SKU-1") == 3
