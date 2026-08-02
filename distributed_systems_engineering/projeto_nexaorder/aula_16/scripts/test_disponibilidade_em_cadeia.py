"""Reproduz o exemplo numérico do roteiro da Aula 14 (Slide 12): quatro
serviços de 99,9% de disponibilidade individual, em cadeia sequencial sem
tolerância a falha parcial, compõem um fluxo de aproximadamente 99,6% — e
quase quatro vezes mais indisponibilidade do que qualquer componente
isolado. A composição de serviços da NexaOrder (pedidos → estoque,
pagamento, expedição) é exatamente essa cadeia — o que justifica, com um
número, por que este projeto trata disjuntor e compensação como
obrigatórios desde a Aula 4, não como refinamento opcional.

E reproduz o exemplo numérico do roteiro da Aula 16 (Slide 13): três
réplicas independentes de 99,5% cada, atrás de um balanceador, compõem
"sete noves" — o contraste estrutural com a cadeia sequencial."""

import pytest

from disponibilidade_em_cadeia import (
    disponibilidade_em_cadeia,
    disponibilidade_redundancia_paralela,
    indisponibilidade,
    razao_de_indisponibilidade,
)


def test_quatro_servicos_de_99_9_por_cento_compoem_99_6_por_cento():
    disponibilidade = disponibilidade_em_cadeia([0.999, 0.999, 0.999, 0.999])

    assert disponibilidade == pytest.approx(0.996, abs=0.0001)


def test_cadeia_e_aproximadamente_quatro_vezes_mais_indisponivel_que_um_componente():
    disponibilidade = disponibilidade_em_cadeia([0.999] * 4)

    razao = razao_de_indisponibilidade(disponibilidade, disponibilidade_componente=0.999)

    assert razao == pytest.approx(4, abs=0.05)


def test_cadeia_de_um_unico_componente_nao_perde_disponibilidade():
    assert disponibilidade_em_cadeia([0.999]) == pytest.approx(0.999)


def test_indisponibilidade_e_o_complemento_da_disponibilidade():
    assert indisponibilidade(0.999) == pytest.approx(0.001)


def test_tres_replicas_independentes_de_99_5_por_cento_compoem_sete_noves():
    disponibilidade = disponibilidade_redundancia_paralela([0.995, 0.995, 0.995])

    assert disponibilidade == pytest.approx(0.999999875, abs=1e-9)


def test_redundancia_paralela_e_estruturalmente_oposta_a_cadeia_sequencial():
    """Em série, disponibilidades se multiplicam e o resultado piora. Em
    paralelo, indisponibilidades se multiplicam e o resultado melhora —
    mesmos três componentes de 99,5%, leitura oposta."""
    componentes = [0.995, 0.995, 0.995]

    em_serie = disponibilidade_em_cadeia(componentes)
    em_paralelo = disponibilidade_redundancia_paralela(componentes)

    assert em_serie < componentes[0]
    assert em_paralelo > componentes[0]


def test_redundancia_de_um_unico_componente_nao_ganha_nada():
    assert disponibilidade_redundancia_paralela([0.995]) == pytest.approx(0.995)
