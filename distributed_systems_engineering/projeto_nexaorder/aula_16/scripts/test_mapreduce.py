"""Prova as três fases de MapReduce sobre o relatório de fraude em lote da
NexaOrder, e a reexecução de uma tarefa isolada sem reiniciar o job
inteiro — Unidade 4, Aula 15."""

import pytest

from mapreduce import TarefaFalhou, executar_mapreduce, fase_map_tolerante_a_falhas, fase_shuffle


def test_mapreduce_conta_tentativas_por_dispositivo():
    registros = [
        {"dispositivo_id": "disp-1", "cartao": "a"},
        {"dispositivo_id": "disp-1", "cartao": "b"},
        {"dispositivo_id": "disp-2", "cartao": "c"},
    ]

    resultado = executar_mapreduce(
        registros,
        funcao_map=lambda r: (r["dispositivo_id"], 1),
        funcao_reduce=lambda valores: sum(valores),
    )

    assert resultado == {"disp-1": 2, "disp-2": 1}


def test_shuffle_agrupa_por_chave_preservando_ordem():
    pares = [("a", 1), ("b", 2), ("a", 3)]

    assert fase_shuffle(pares) == {"a": [1, 3], "b": [2]}


def test_map_tolerante_a_falhas_reexecuta_so_a_tarefa_que_falhou():
    """A tarefa de reconciliação do roteiro: se um nó falha durante uma
    tarefa, o framework a reatribui e reexecuta — sem reiniciar o job
    inteiro. 'estavel' nunca deveria ser tocado de novo."""
    tentativas_por_registro: dict[str, int] = {}

    def map_instavel(registro: str) -> tuple[str, int]:
        tentativas_por_registro[registro] = tentativas_por_registro.get(registro, 0) + 1
        if registro == "instavel" and tentativas_por_registro[registro] < 2:
            raise RuntimeError("falha transitória simulada")
        return (registro, 1)

    resultado = fase_map_tolerante_a_falhas(["estavel", "instavel"], map_instavel)

    assert dict(resultado) == {"estavel": 1, "instavel": 1}
    assert tentativas_por_registro["estavel"] == 1
    assert tentativas_por_registro["instavel"] == 2


def test_map_tolerante_a_falhas_desiste_apos_o_limite_de_tentativas():
    def sempre_falha(registro: str) -> tuple[str, int]:
        raise RuntimeError("falha permanente")

    with pytest.raises(TarefaFalhou):
        fase_map_tolerante_a_falhas(["x"], sempre_falha, max_tentativas_por_tarefa=2)
