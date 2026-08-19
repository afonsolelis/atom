"""Publicador da outbox — Unidade 3, Aula 10.

Fecha o padrão outbox que a Aula 8 deixou pela metade: lê os eventos
pendentes gravados atomicamente com o pedido (Aula 8), publica cada um no
tópico particionado por `pedido_id` (garantindo que todos os eventos de um
mesmo pedido cheguem em ordem à mesma partição — a mesma lógica de chave da
Aula 6/10) e marca como publicado.

Em produção, isto rodaria em um laço contínuo ou reagindo a um gatilho de
WAL/CDC do banco. Aqui, é uma função chamada explicitamente — por um
endpoint administrativo, ou por teste — para manter o projeto sem
dependência de um agendador em segundo plano.
"""

from __future__ import annotations

from .barramento import Topico
from .store import RepositorioPedidos

NOME_TOPICO_PEDIDOS = "pedidos-eventos"
NUM_PARTICOES_PEDIDOS = 8  # o mesmo número do exemplo da Aula 10 (1200 rps / 150 rps)


def publicar_eventos_pendentes(repositorio: RepositorioPedidos, topico: Topico) -> list[str]:
    """Publica todos os eventos pendentes da outbox e devolve os IDs
    publicados nesta chamada."""
    eventos = repositorio.eventos_pendentes()
    ids_publicados = []
    for evento in eventos:
        topico.publicar(
            chave=evento["pedido_id"],  # a chave de partição é o pedido_id
            tipo=evento["tipo"],
            payload=evento["payload"],
        )
        repositorio.marcar_publicado(evento["id"])
        ids_publicados.append(evento["id"])
    return ids_publicados
