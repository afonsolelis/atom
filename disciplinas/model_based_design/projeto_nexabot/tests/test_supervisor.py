"""Suíte pytest do supervisor de segurança do NexaBot.

Combina três fontes de casos de teste, todas derivadas do modelo (Aula 12):

1. Casos gerados por cobertura de estados e de transições (`nexabot.mbt`).
2. A máquina de estados baseada em propriedades do `hypothesis.stateful`.
3. Verificação direta dos requisitos formais (`nexabot.requisitos`) contra o
   resultado completo da exploração de estados (`nexabot.modelcheck`).
"""

from __future__ import annotations

import pytest

from nexabot.mbt import (
    TestSupervisorMachine,
    gerar_casos_cobertura_estados,
    gerar_casos_cobertura_transicoes,
    medir_cobertura,
)
from nexabot.modelcheck import explorar, verificar_alcancabilidade, verificar_invariantes
from nexabot.requisitos import REQUISITOS_ALCANCABILIDADE, REQUISITOS_TRANSICAO
from nexabot.supervisor import Entradas, Estado, Supervisor
from nexabot.timed import verificar_req_safe_006

# --------------------------------------------------------------------------
# 1. Casos gerados por cobertura (mbt.py)
# --------------------------------------------------------------------------
_RESULTADO = explorar()
_CASOS_ESTADO = gerar_casos_cobertura_estados(_RESULTADO)
_CASOS_TRANSICAO = gerar_casos_cobertura_transicoes(_RESULTADO)


@pytest.mark.parametrize("caso", _CASOS_ESTADO, ids=lambda c: c.id)
def test_cobertura_de_estados(caso):
    caso.rodar()


@pytest.mark.parametrize("caso", _CASOS_TRANSICAO, ids=lambda c: c.id)
def test_cobertura_de_transicoes(caso):
    caso.rodar()


def test_cobertura_atingida_e_100_por_cento():
    cobertura = medir_cobertura(_CASOS_ESTADO + _CASOS_TRANSICAO, _RESULTADO)
    assert cobertura["pct_estados"] == 100.0
    assert cobertura["pct_transicoes"] == 100.0


# --------------------------------------------------------------------------
# 2. Testes baseados em propriedades (hypothesis.stateful)
# --------------------------------------------------------------------------
TestSupervisorStateful = TestSupervisorMachine


# --------------------------------------------------------------------------
# 3. Requisitos formais verificados exaustivamente sobre o modelo
# --------------------------------------------------------------------------
def test_nenhuma_invariante_violada():
    violacoes = verificar_invariantes(_RESULTADO, REQUISITOS_TRANSICAO)
    assert violacoes == [], [
        (v.requisito.id, [t.destino.name for t in v.caminho]) for v in violacoes
    ]


@pytest.mark.parametrize("requisito", REQUISITOS_ALCANCABILIDADE, ids=lambda r: r.id)
def test_alcancabilidade(requisito):
    alcancavel, _ = verificar_alcancabilidade(_RESULTADO, requisito)
    assert alcancavel, f"{requisito.id} falhou: {requisito.descricao}"


def test_req_safe_006_watchdog_temporizado():
    resultado = verificar_req_safe_006(atraso_deteccao_max=2, permite_ciclo_perdido=True)
    assert resultado.ok
    assert resultado.pior_caso_ms <= 150.0


# --------------------------------------------------------------------------
# Testes unitários diretos, de baixo nível, sobre a classe Supervisor
# --------------------------------------------------------------------------
def test_supervisor_comeca_ocioso():
    assert Supervisor().state is Estado.OCIOSO


def test_partir_leva_a_movendo():
    sup = Supervisor()
    saida = sup.step(Entradas(comando_partir=True))
    assert sup.state is Estado.MOVENDO
    assert saida.torque_habilitado is True
    assert saida.freio_acionado is False


def test_obstaculo_durante_movimento_corta_torque_na_hora():
    sup = Supervisor()
    sup.step(Entradas(comando_partir=True))
    saida = sup.step(Entradas(obstaculo=True))
    assert sup.state is Estado.PARADO_OBSTACULO
    assert saida.torque_habilitado is False
    assert saida.freio_acionado is True


def test_emergencia_tem_prioridade_sobre_tudo():
    sup = Supervisor()
    sup.step(Entradas(comando_partir=True))
    saida = sup.step(Entradas(emergencia=True, comando_partir=True, obstaculo=False))
    assert sup.state is Estado.EMERGENCIA
    assert saida.torque_habilitado is False
    assert saida.freio_acionado is True


def test_falha_so_sai_por_rearme():
    sup = Supervisor()
    sup.step(Entradas(falha_encoder=True))
    assert sup.state is Estado.FALHA
    # tentativas sem rearme não saem de FALHA, mesmo com outros comandos
    sup.step(Entradas(comando_partir=True, falha_encoder=False))
    assert sup.state is Estado.FALHA
    # rearme explícito, com a falha já removida, libera o supervisor
    sup.step(Entradas(rearme=True, falha_encoder=False))
    assert sup.state is Estado.OCIOSO


def test_obstaculo_removido_com_partida_retoma_movimento():
    sup = Supervisor()
    sup.step(Entradas(comando_partir=True))
    sup.step(Entradas(obstaculo=True))
    assert sup.state is Estado.PARADO_OBSTACULO
    sup.step(Entradas(obstaculo=False, comando_partir=True))
    assert sup.state is Estado.MOVENDO
