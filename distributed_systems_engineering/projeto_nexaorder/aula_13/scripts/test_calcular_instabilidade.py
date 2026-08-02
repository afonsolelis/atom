"""Prova a fórmula I = Ce/(Ca+Ce) aplicada ao grafo real de dependências
da NexaOrder — Unidade 3, Aula 9. Rode com o venv compartilhado:
`python3 -m pytest scripts/`."""

from calcular_instabilidade import calcular_instabilidade


def test_estoque_pagamento_expedicao_sao_maximamente_estaveis():
    """Nenhum dos três chama outro serviço, e dois outros dependem deles:
    Ce=0, então I=0 — o extremo estável do exemplo da Aula 9."""
    grafo = {
        "gateway": {"pedidos", "estoque", "pagamento", "expedicao"},
        "pedidos": {"estoque", "pagamento", "expedicao"},
        "estoque": set(),
        "pagamento": set(),
        "expedicao": set(),
    }

    resultado = calcular_instabilidade(grafo)

    assert resultado["estoque"] == 0.0
    assert resultado["pagamento"] == 0.0
    assert resultado["expedicao"] == 0.0


def test_pedidos_e_mais_instavel_que_os_servicos_que_ele_chama():
    grafo = {
        "gateway": {"pedidos", "estoque", "pagamento", "expedicao"},
        "pedidos": {"estoque", "pagamento", "expedicao"},
        "estoque": set(),
        "pagamento": set(),
        "expedicao": set(),
    }

    resultado = calcular_instabilidade(grafo)

    assert resultado["pedidos"] == 0.75
    assert resultado["pedidos"] > resultado["estoque"]


def test_gateway_e_maximamente_instavel_ninguem_depende_dele():
    grafo = {
        "gateway": {"pedidos", "estoque", "pagamento", "expedicao"},
        "pedidos": {"estoque", "pagamento", "expedicao"},
        "estoque": set(),
        "pagamento": set(),
        "expedicao": set(),
    }

    resultado = calcular_instabilidade(grafo)

    assert resultado["gateway"] == 1.0


def test_servico_isolado_sem_dependencias_e_sem_dependentes_tem_instabilidade_zero():
    grafo = {"solitario": set()}

    resultado = calcular_instabilidade(grafo)

    assert resultado["solitario"] == 0.0
