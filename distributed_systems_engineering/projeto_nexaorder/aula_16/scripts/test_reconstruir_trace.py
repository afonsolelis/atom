"""Reproduz, span por span, o incidente que abre o roteiro da Aula 13: um
pedido que levou doze segundos entre o clique e a confirmação. Prova que o
algoritmo de reconstrução chega à mesma conclusão que o roteiro — a demora
está na espera pelo pool de conexões dentro de pagamento, não no provedor
externo nem em nenhum outro serviço."""

from __future__ import annotations

from reconstruir_trace import (
    caminho_desde_a_raiz,
    filho_esta_contido_no_pai,
    fora_do_caminho_critico,
    maior_gargalo,
)


def _span(span_id, span_pai_id, servico, nome, inicio_ms, fim_ms) -> dict:
    return {
        "span_id": span_id,
        "span_pai_id": span_pai_id,
        "servico": servico,
        "nome": nome,
        "trace_id": "trace-doze-segundos",
        "inicio_ms": inicio_ms,
        "fim_ms": fim_ms,
        "duracao_ms": fim_ms - inicio_ms,
    }


def spans_do_incidente_de_doze_segundos() -> list[dict]:
    """Os números exatos do roteiro (Slide 14, Aula 13): gateway 12.000 ms,
    pedidos 11.950 ms, estoque 35 ms, pagamento 11.780 ms — com dois
    filhos, espera em fila (11.450 ms) e chamada ao provedor externo
    (310 ms). A expedição, assíncrona, começa depois que o cliente já
    recebeu resposta."""
    gateway = _span("s-gw", None, "gateway", "GET /pedidos/{id}/resumo", 0, 12000)
    pedidos = _span("s-ped", "s-gw", "pedidos", "POST /finalizar-compra", 10, 11960)
    estoque = _span("s-est", "s-ped", "pedidos", "reservar_estoque", 20, 55)
    pagamento = _span("s-pag", "s-ped", "pedidos", "autorizar_pagamento", 60, 11840)
    espera_fila = _span("s-fila", "s-pag", "pagamento", "espera_pool_de_conexoes", 70, 11520)
    provedor = _span("s-prov", "s-pag", "pagamento", "chamada_provedor_externo", 11520, 11830)
    expedicao = _span("s-exp", None, "expedicao", "solicitar_remessa", 12100, 132100)
    return [gateway, pedidos, estoque, pagamento, espera_fila, provedor, expedicao]


def _span_raiz_da_requisicao(spans: list[dict]) -> dict:
    return next(s for s in spans if s["span_pai_id"] is None and s["nome"] == "GET /pedidos/{id}/resumo")


def test_o_gargalo_e_a_espera_em_fila_nao_o_provedor_externo():
    """A conclusão central do roteiro: a hipótese intuitiva seria culpar o
    provedor externo — o suspeito habitual, por estar fora do controle da
    equipe. Ele respondeu em 310 ms, comportamento normal. O gargalo real
    é interno."""
    spans = spans_do_incidente_de_doze_segundos()
    raiz = _span_raiz_da_requisicao(spans)

    gargalo = maior_gargalo(spans, raiz)

    assert gargalo["nome"] == "espera_pool_de_conexoes"
    assert gargalo["duracao_ms"] == 11450


def test_gargalo_ignora_arvore_assincrona_mais_longa_mas_nao_relacionada():
    """A armadilha que a restrição à subárvore evita: a expedição
    (120.000 ms) tem o mesmo trace_id e, ingenuamente comparada por
    duração, pareceria "o" gargalo — mas pertence a uma árvore de spans
    independente (Aula 8/10: assíncrona, iniciada só depois da resposta ao
    cliente), não à requisição que o cliente esperou."""
    spans = spans_do_incidente_de_doze_segundos()
    raiz = _span_raiz_da_requisicao(spans)

    gargalo = maior_gargalo(spans, raiz)

    assert gargalo["nome"] != "solicitar_remessa"
    expedicao = next(s for s in spans if s["nome"] == "solicitar_remessa")
    assert expedicao["duracao_ms"] > gargalo["duracao_ms"]  # maior em duração, ainda assim não é o gargalo


def test_estoque_e_descartado_como_suspeito_imediatamente():
    spans = spans_do_incidente_de_doze_segundos()
    estoque = next(s for s in spans if s["nome"] == "reservar_estoque")

    assert estoque["duracao_ms"] == 35  # ínfimo perto dos 12.000 ms totais


def test_caminho_da_raiz_ate_o_gargalo_passa_por_pagamento():
    spans = spans_do_incidente_de_doze_segundos()
    raiz = _span_raiz_da_requisicao(spans)
    gargalo = maior_gargalo(spans, raiz)

    caminho = caminho_desde_a_raiz(spans, gargalo)

    assert [s["nome"] for s in caminho] == [
        "GET /pedidos/{id}/resumo",
        "POST /finalizar-compra",
        "autorizar_pagamento",
        "espera_pool_de_conexoes",
    ]


def test_filhos_de_pagamento_estao_contidos_no_pai_nao_somados_a_ele():
    """Primeiro cuidado de leitura do roteiro: 11.450 + 310 = 11.760, um
    número próximo dos 11.780 ms do pai mas que não deve ser lido como
    "a soma bate". Os filhos estão contidos no intervalo do pai — a
    diferença (20 ms) é o próprio trabalho de pagamento em torno das duas
    chamadas, não um erro de medição a ser reconciliado."""
    spans = spans_do_incidente_de_doze_segundos()
    pagamento = next(s for s in spans if s["nome"] == "autorizar_pagamento")
    espera_fila = next(s for s in spans if s["nome"] == "espera_pool_de_conexoes")
    provedor = next(s for s in spans if s["nome"] == "chamada_provedor_externo")

    assert filho_esta_contido_no_pai(pagamento, espera_fila)
    assert filho_esta_contido_no_pai(pagamento, provedor)
    soma_ingenua = espera_fila["duracao_ms"] + provedor["duracao_ms"]
    assert soma_ingenua != pagamento["duracao_ms"]  # a soma não "bate", e não precisa bater


def test_expedicao_fica_fora_do_caminho_critico():
    """Segundo cuidado de leitura: a expedição é assíncrona (Aula 8/10) e
    começa depois que o span raiz já terminou — não atrasa a resposta ao
    cliente, mesmo levando 120 segundos."""
    spans = spans_do_incidente_de_doze_segundos()
    raiz = _span_raiz_da_requisicao(spans)

    fora = fora_do_caminho_critico(raiz, spans)

    assert [s["nome"] for s in fora] == ["solicitar_remessa"]
