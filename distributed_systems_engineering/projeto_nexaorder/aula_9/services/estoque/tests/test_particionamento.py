"""Reproduz os números do roteiro da Aula 6: hashing consistente move
aproximadamente 1/(N+1) das chaves ao adicionar um nó, contra
aproximadamente 100% do hash simples; e nós virtuais reduzem a variância
de carga entre nós."""

from __future__ import annotations

import statistics
from collections import Counter

from app.particionamento import AnelConsistente, fracao_redistribuida, hash_simples

CHAVES_DE_TESTE = [f"pedido-{i}" for i in range(5000)]


def test_hash_simples_redistribui_quase_tudo_ao_mudar_n():
    antes = {chave: hash_simples(chave, 9) for chave in CHAVES_DE_TESTE}
    depois = {chave: hash_simples(chave, 10) for chave in CHAVES_DE_TESTE}

    fracao = sum(1 for c in CHAVES_DE_TESTE if antes[c] != depois[c]) / len(CHAVES_DE_TESTE)

    # O roteiro fala em "aproximadamente 100%"; qualquer valor alto confirma
    # o problema estrutural do hash simples.
    assert fracao > 0.85


def test_anel_consistente_move_aproximadamente_um_sobre_n_mais_um():
    """N igual a 9 nós existentes, 1 nó adicionado: 1/(9+1) = 10%."""
    anel_antes = AnelConsistente(nos_virtuais_por_no=100)
    for i in range(9):
        anel_antes.adicionar_no(f"estoque-{i}")

    anel_depois = AnelConsistente(nos_virtuais_por_no=100)
    for i in range(9):
        anel_depois.adicionar_no(f"estoque-{i}")
    anel_depois.adicionar_no("estoque-9")

    fracao = fracao_redistribuida(CHAVES_DE_TESTE, anel_antes, anel_depois)

    assert 0.05 <= fracao <= 0.16


def test_anel_e_deterministico_para_a_mesma_chave():
    anel = AnelConsistente()
    anel.adicionar_no("estoque-0")
    anel.adicionar_no("estoque-1")

    primeiro = anel.localizar("pedido-42")
    segundo = anel.localizar("pedido-42")

    assert primeiro == segundo


def test_localizar_em_anel_vazio_leva_a_erro():
    anel = AnelConsistente()
    try:
        anel.localizar("pedido-1")
        assert False, "deveria ter levantado ValueError"
    except ValueError:
        pass


def test_remover_no_redistribui_apenas_as_chaves_daquele_no():
    anel = AnelConsistente(nos_virtuais_por_no=50)
    for i in range(5):
        anel.adicionar_no(f"estoque-{i}")

    atribuicao_antes = {chave: anel.localizar(chave) for chave in CHAVES_DE_TESTE}
    anel.remover_no("estoque-2")
    atribuicao_depois = {chave: anel.localizar(chave) for chave in CHAVES_DE_TESTE}

    # Nenhuma chave deveria ter sido reatribuída ao nó removido.
    assert "estoque-2" not in atribuicao_depois.values()
    # Só as chaves que antes pertenciam a estoque-2 deveriam ter mudado.
    mudaram = {c for c in CHAVES_DE_TESTE if atribuicao_antes[c] != atribuicao_depois[c]}
    assert mudaram == {c for c in CHAVES_DE_TESTE if atribuicao_antes[c] == "estoque-2"}


def test_nos_virtuais_reduzem_variancia_de_carga_entre_nos():
    anel_poucos_virtuais = AnelConsistente(nos_virtuais_por_no=1)
    anel_muitos_virtuais = AnelConsistente(nos_virtuais_por_no=100)
    for i in range(5):
        anel_poucos_virtuais.adicionar_no(f"estoque-{i}")
        anel_muitos_virtuais.adicionar_no(f"estoque-{i}")

    contagem_poucos = Counter(anel_poucos_virtuais.localizar(c) for c in CHAVES_DE_TESTE)
    contagem_muitos = Counter(anel_muitos_virtuais.localizar(c) for c in CHAVES_DE_TESTE)

    desvio_poucos = statistics.pstdev(contagem_poucos.values())
    desvio_muitos = statistics.pstdev(contagem_muitos.values())

    assert desvio_muitos < desvio_poucos
