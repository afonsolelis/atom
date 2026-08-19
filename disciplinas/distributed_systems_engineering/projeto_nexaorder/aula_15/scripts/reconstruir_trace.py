"""Reconstrução de trace em cascata — Unidade 4, Aula 13.

Cada serviço do projeto mede e guarda seus próprios spans (ver
services/*/app/tracing.py) e os expõe via `GET /_admin/spans/{trace_id}`.
Este módulo opera sobre a UNIÃO desses spans — como um coletor real
(Jaeger, Tempo) faria depois de recebê-los de vários processos — e
implementa os dois cuidados de leitura que o roteiro da Aula 13 explicita
a propósito do incidente do pedido de doze segundos:

1. Spans aninhados não se somam como se fossem sequenciais — a duração de
   um filho está contida na duração do pai, não é adicional a ela.
2. Trabalho assíncrono (a expedição, neste projeto — Aula 8/10) começa
   depois que o span raiz termina, e não faz parte do caminho crítico.

Este módulo não depende de rede: opera sobre `list[dict]` no formato que
`ColetorDeSpans.spans_do_trace` devolve. Reunir os spans de vários serviços
em produção é trabalho do coletor; aqui, o exemplo numérico do roteiro
(`spans_do_incidente_de_doze_segundos`, em
`scripts/test_reconstruir_trace.py`) desempenha esse papel para prova.
"""

from __future__ import annotations


def descendentes(spans: list[dict], span_raiz: dict) -> list[dict]:
    """Todos os spans na subárvore de `span_raiz`, a própria raiz inclusa.

    Um único trace_id pode conter mais de uma árvore de spans: a árvore
    síncrona da requisição (raiz no gateway) e árvores assíncronas
    independentes que carregam o mesmo trace_id só porque a Aula 13
    propaga o identificador também pelo barramento de eventos (a
    expedição, aqui). `descendentes` é o que separa uma da outra."""
    por_pai: dict[str | None, list[dict]] = {}
    for s in spans:
        por_pai.setdefault(s["span_pai_id"], []).append(s)

    resultado = [span_raiz]
    pendentes = [span_raiz]
    while pendentes:
        atual = pendentes.pop()
        filhos = por_pai.get(atual["span_id"], [])
        resultado.extend(filhos)
        pendentes.extend(filhos)
    return resultado


def maior_gargalo(spans: list[dict], span_raiz: dict) -> dict:
    """Entre as folhas da subárvore de `span_raiz` (spans sem nenhum
    filho), devolve a de maior duração — o verdadeiro gargalo do caminho
    crítico. Não é necessariamente o span mais profundo nem o span raiz:
    no incidente do roteiro, o span de pagamento (11.780 ms) não é o
    gargalo — um de seus dois filhos é.

    Restringir a busca à subárvore de `span_raiz` é essencial: sem isso,
    uma árvore assíncrona não relacionada mas com o mesmo trace_id (como a
    expedição, que pode durar minutos sem atrasar ninguém) pareceria o
    maior gargalo, quando na verdade está fora do caminho que o cliente
    esperou."""
    sub = descendentes(spans, span_raiz)
    ids_com_filho = {s["span_pai_id"] for s in sub if s["span_pai_id"] is not None}
    folhas = [s for s in sub if s["span_id"] not in ids_com_filho]
    return max(folhas, key=lambda s: s["duracao_ms"])


def caminho_desde_a_raiz(spans: list[dict], span: dict) -> list[dict]:
    """Reconstrói a cadeia de pais até a raiz, para leitura humana — do
    span raiz até o span informado, na ordem em que a chamada realmente
    desceu pelos serviços."""
    por_id = {s["span_id"]: s for s in spans}
    caminho = [span]
    atual = span
    while atual["span_pai_id"] is not None:
        atual = por_id[atual["span_pai_id"]]
        caminho.append(atual)
    return list(reversed(caminho))


def filho_esta_contido_no_pai(pai: dict, filho: dict) -> bool:
    """A propriedade geométrica que torna errado ler spans aninhados como
    se fossem sequenciais: o intervalo do filho cabe inteiro dentro do
    intervalo do pai. Somar as durações dos filhos para "conferir" a
    duração do pai ignora que eles não são etapas adicionais — são partes
    do mesmo intervalo, vistas em mais detalhe."""
    return pai["inicio_ms"] <= filho["inicio_ms"] and filho["fim_ms"] <= pai["fim_ms"]


def fora_do_caminho_critico(span_raiz: dict, spans: list[dict]) -> list[dict]:
    """Spans cujo início é posterior ao fim do span raiz — a assinatura de
    trabalho assíncrono (como a expedição, Aula 8/10) que não atrasa a
    resposta ao cliente, mesmo que leve minutos para terminar."""
    return [s for s in spans if s["span_id"] != span_raiz["span_id"] and s["inicio_ms"] >= span_raiz["fim_ms"]]
