"""Reproduz exatamente o cálculo original da Aula 1 (docs/dimensionamento.md)
como regressão — a fórmula não mudou entre a Aula 1 e a Aula 16, só a
origem dos insumos (ver services/pedidos/tests/test_dimensionamento_com_evidencias.py
para a versão com um insumo medido ao vivo, não suposto)."""

from dimensionamento_com_evidencias import calcular_numero_de_instancias


def test_reproduz_exatamente_o_calculo_original_da_aula_1():
    """800 req/s de pico, 200 req/s por instância, 70% de utilização-alvo -> 6."""
    assert calcular_numero_de_instancias(
        taxa_de_pico_por_segundo=800, capacidade_por_instancia=200, utilizacao_alvo=0.7
    ) == 6


def test_conta_ingenua_sem_folga_dava_quatro_nao_seis():
    """A folga da utilização-alvo é o que separa 4 (100% de ocupação, sem
    margem para picos) de 6 (a resposta real da Aula 1)."""
    assert calcular_numero_de_instancias(
        taxa_de_pico_por_segundo=800, capacidade_por_instancia=200, utilizacao_alvo=1.0
    ) == 4
