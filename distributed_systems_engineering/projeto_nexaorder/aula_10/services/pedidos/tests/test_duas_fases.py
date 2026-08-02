"""Reproduz os três comportamentos do 2PC discutidos no roteiro da Aula 8,
e o risco agregado que motiva a troca por sagas."""

import pytest

from app.duas_fases import (
    CoordenadorDuasFases,
    EstadoParticipante,
    Participante,
    VotoParticipante,
    risco_agregado,
)


def test_2pc_confirma_quando_todos_votam_pronto():
    participantes = [Participante("estoque"), Participante("pagamento")]
    coordenador = CoordenadorDuasFases(participantes)

    resultado = coordenador.executar()

    assert resultado == "confirmado"
    assert all(p.estado == EstadoParticipante.CONFIRMADO for p in participantes)


def test_2pc_aborta_quando_um_participante_vota_abortar():
    participantes = [
        Participante("estoque"),
        Participante("pagamento", voto=VotoParticipante.ABORTAR),
    ]
    coordenador = CoordenadorDuasFases(participantes)

    resultado = coordenador.executar()

    assert resultado == "abortado"
    assert all(p.estado == EstadoParticipante.DESFEITO for p in participantes)


def test_2pc_bloqueia_participantes_se_coordenador_falha_apos_preparar():
    """O cenário crítico do roteiro: cada participante já executou
    provisoriamente e bloqueou recursos, e fica sem saber se deve
    confirmar ou desfazer."""
    participantes = [Participante("estoque"), Participante("pagamento")]
    coordenador = CoordenadorDuasFases(participantes)

    resultado = coordenador.executar(coordenador_falha_apos_preparar=True)

    assert resultado == "coordenador_falhou_participantes_bloqueados"
    assert all(p.estado == EstadoParticipante.PREPARADO for p in participantes)


def test_risco_agregado_com_quatro_participantes_a_um_por_cento():
    """Reproduz o número do roteiro: aproximadamente 3,9%, quase quatro
    vezes o risco individual de 1%."""
    risco = risco_agregado(probabilidade_falha_individual=0.01, numero_de_participantes=4)

    assert risco == pytest.approx(0.039, abs=0.001)


def test_risco_agregado_cresce_com_o_numero_de_participantes():
    risco_dois = risco_agregado(0.01, 2)
    risco_quatro = risco_agregado(0.01, 4)
    risco_oito = risco_agregado(0.01, 8)

    assert risco_dois < risco_quatro < risco_oito
