"""Contratos declarados pelo consumidor — Unidade 4, Aula 14.

Cada entrada aqui é o que `pedidos`, como consumidor, declara precisar da
resposta de um provedor — deliberadamente menos do que o esquema completo
do provedor, porque essa é a essência de um contrato orientado a
consumidor: quem consome só declara o que usa, não tudo o que existe (ver
`app/saga.py` para onde cada campo é lido: `reserva["reserva_id"]`,
`cobranca["id"]`, `remessa["id"]`).

Um mecanismo real de contrato (Pact e ferramentas equivalentes) publicaria
isto em um repositório compartilhado, e o pipeline de integração contínua
de cada provedor o verificaria antes de qualquer implantação — sem que
consumidor e provedor precisassem estar em execução simultânea.
`verificar_contrato` é o núcleo desse mecanismo: uma função pura, testada
em `test_contratos.py` contra a aplicação real de cada provedor (ver
docs/adr/0014-testes-de-contrato-sem-broker.md para o porquê deste projeto
não integra um broker de contratos real)."""

from __future__ import annotations

CONTRATO_RESERVAR_ESTOQUE = {
    "servico_provedor": "estoque",
    "operacao": "POST /reservas",
    "campos_obrigatorios": {"reserva_id"},
    "consumido_por": "app/saga.py — reserva['reserva_id']",
}

CONTRATO_AUTORIZAR_PAGAMENTO = {
    "servico_provedor": "pagamento",
    "operacao": "POST /cobrancas",
    "campos_obrigatorios": {"id"},
    "consumido_por": "app/saga.py — cobranca['id']",
}

CONTRATO_SOLICITAR_EXPEDICAO = {
    "servico_provedor": "expedicao",
    "operacao": "POST /remessas",
    "campos_obrigatorios": {"id"},
    "consumido_por": "app/saga.py — remessa['id']",
}


def verificar_contrato(resposta_json: dict, contrato: dict) -> list[str]:
    """Devolve, em ordem alfabética, os campos obrigatórios ausentes na
    resposta. Lista vazia significa que o contrato foi cumprido."""
    return sorted(contrato["campos_obrigatorios"] - set(resposta_json.keys()))
