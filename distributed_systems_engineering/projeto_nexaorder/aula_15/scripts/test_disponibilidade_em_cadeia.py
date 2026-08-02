"""Reproduz o exemplo numérico do roteiro da Aula 14 (Slide 12): quatro
serviços de 99,9% de disponibilidade individual, em cadeia sequencial sem
tolerância a falha parcial, compõem um fluxo de aproximadamente 99,6% — e
quase quatro vezes mais indisponibilidade do que qualquer componente
isolado. A composição de serviços da NexaOrder (pedidos → estoque,
pagamento, expedição) é exatamente essa cadeia — o que justifica, com um
número, por que este projeto trata disjuntor e compensação como
obrigatórios desde a Aula 4, não como refinamento opcional."""

import pytest

from disponibilidade_em_cadeia import disponibilidade_em_cadeia, indisponibilidade, razao_de_indisponibilidade


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
