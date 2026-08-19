"""Reproduz o exemplo numérico do roteiro da Aula 13 (Slide 12): volume de
12 milhões de requisições/mês, SLO de 99,9%, 9 mil falhas consumidas nos
primeiros 10 dias — a taxa de consumo que aponta esgotamento por volta do
dia 14."""

from orcamento_de_erro import dia_estimado_de_esgotamento, fracao_consumida, orcamento_de_erro, sli_proporcao


def test_orcamento_do_exemplo_numerico_da_aula():
    orcamento = orcamento_de_erro(volume_do_periodo=12_000_000, slo=0.999)

    assert orcamento == 12_000


def test_fracao_consumida_em_dez_dias_e_setenta_e_cinco_por_cento():
    orcamento = orcamento_de_erro(12_000_000, 0.999)

    assert fracao_consumida(9_000, orcamento) == 0.75


def test_dia_estimado_de_esgotamento_bate_com_o_roteiro():
    """"Mantido esse ritmo, o orçamento se esgota por volta do dia 14"."""
    orcamento = orcamento_de_erro(12_000_000, 0.999)

    assert dia_estimado_de_esgotamento(9_000, orcamento, dias_decorridos=10) == 14


def test_orcamento_maior_com_slo_mais_frouxo():
    """Um SLO de 99% (em vez de 99,9%) tolera dez vezes mais falhas no
    mesmo volume — o custo de prometer menos."""
    orcamento_999 = orcamento_de_erro(12_000_000, 0.999)
    orcamento_99 = orcamento_de_erro(12_000_000, 0.99)

    assert orcamento_99 == orcamento_999 * 10


def test_sli_de_checkout_reflete_proporcao_de_sucesso():
    assert sli_proporcao(resultados_bons=9970, total=10000) == 0.997


def test_sli_com_total_zero_nao_quebra():
    """Antes de qualquer tráfego, um SLI sem amostra não deve levantar
    ZeroDivisionError — não há indício de degradação ainda."""
    assert sli_proporcao(resultados_bons=0, total=0) == 1.0
