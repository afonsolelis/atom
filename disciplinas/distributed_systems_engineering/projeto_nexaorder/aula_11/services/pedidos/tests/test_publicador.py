"""Prova que o publicador fecha o padrão outbox: lê os eventos pendentes,
publica no tópico correto (particionado por pedido_id) e marca como
publicado — Unidade 3, Aula 10."""

import uuid

from app.barramento import Topico
from app.publicador import NOME_TOPICO_PEDIDOS, NUM_PARTICOES_PEDIDOS, publicar_eventos_pendentes


def _corpo_pedido() -> dict:
    return {
        "cliente_id": str(uuid.uuid4()),
        "chave_idempotencia": str(uuid.uuid4()),
        "itens": [{"sku": "TECLADO-MEC-01", "quantidade": 1, "preco_unitario": 349.90}],
    }


def test_publicar_eventos_pendentes_publica_e_marca(cliente_api):
    import app.main as modulo_pedidos

    pedido = cliente_api.post("/pedidos", json=_corpo_pedido()).json()
    topico = Topico(NOME_TOPICO_PEDIDOS, NUM_PARTICOES_PEDIDOS)

    ids_publicados = publicar_eventos_pendentes(modulo_pedidos.repositorio, topico)

    assert len(ids_publicados) == 1
    particao = topico.particao_da_chave(pedido["id"])
    eventos = topico.ler_particao(particao)
    eventos_deste_pedido = [e for e in eventos if e.chave == pedido["id"]]
    assert len(eventos_deste_pedido) == 1
    assert eventos_deste_pedido[0].tipo == "PedidoCriado"

    # A outbox não tem mais nada pendente para este pedido.
    pendentes = [
        e for e in modulo_pedidos.repositorio.eventos_pendentes() if e["pedido_id"] == pedido["id"]
    ]
    assert pendentes == []


def test_publicar_duas_vezes_sem_pedidos_novos_nao_duplica(cliente_api):
    import app.main as modulo_pedidos

    cliente_api.post("/pedidos", json=_corpo_pedido())
    topico = Topico(NOME_TOPICO_PEDIDOS, NUM_PARTICOES_PEDIDOS)

    primeira = publicar_eventos_pendentes(modulo_pedidos.repositorio, topico)
    segunda = publicar_eventos_pendentes(modulo_pedidos.repositorio, topico)

    assert len(primeira) == 1
    assert len(segunda) == 0


def test_endpoint_publicar_eventos(cliente_api):
    cliente_api.post("/pedidos", json=_corpo_pedido())

    resposta = cliente_api.post("/_admin/publicar-eventos")

    assert resposta.status_code == 200
    assert resposta.json()["eventos_publicados"] == 1


def test_endpoint_consumir_auditoria_le_eventos_publicados(cliente_api):
    cliente_api.post("/pedidos", json=_corpo_pedido())
    cliente_api.post("/_admin/publicar-eventos")

    resposta = cliente_api.get("/_admin/auditoria/consumir")

    corpo = resposta.json()
    assert len(corpo["eventos"]) == 1
    assert corpo["eventos"][0]["tipo"] == "PedidoCriado"

    # Uma segunda leitura não repete o mesmo evento.
    segunda_resposta = cliente_api.get("/_admin/auditoria/consumir")
    assert segunda_resposta.json()["eventos"] == []
