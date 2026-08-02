"""MapReduce mínimo — Unidade 4, Aula 15.

As três fases do modelo clássico, sobre dados em memória: map transforma
cada registro independentemente (paraleliza perfeitamente, porque nenhuma
tarefa depende de outra); shuffle redistribui os pares intermediários por
chave (a fase mais cara em um cluster real, por envolver tráfego de rede
em larga escala — aqui, um `dict` cumpre o mesmo papel conceitual, sem
esse custo); reduce agrupa e combina por chave, produzindo o resultado.

Aplicado ao relatório de fraude em lote da NexaOrder: "quantas tentativas
de pagamento cada dispositivo fez no histórico completo" — a mesma
pergunta que `services/pedidos/app/janela_evento.py` responde em tempo
real para os últimos 60 segundos, respondida aqui sobre um conjunto
fechado e conhecido (o caso de uso que o roteiro atribui ao lote: um
relatório que pode esperar, não uma decisão em segundos).
"""

from __future__ import annotations

from typing import Any, Callable, Iterable


def fase_map(registros: Iterable[Any], funcao_map: Callable[[Any], tuple[str, Any]]) -> list[tuple[str, Any]]:
    return [funcao_map(registro) for registro in registros]


def fase_shuffle(pares: list[tuple[str, Any]]) -> dict[str, list[Any]]:
    agrupado: dict[str, list[Any]] = {}
    for chave, valor in pares:
        agrupado.setdefault(chave, []).append(valor)
    return agrupado


def fase_reduce(agrupado: dict[str, list[Any]], funcao_reduce: Callable[[list[Any]], Any]) -> dict[str, Any]:
    return {chave: funcao_reduce(valores) for chave, valores in agrupado.items()}


def executar_mapreduce(
    registros: Iterable[Any],
    funcao_map: Callable[[Any], tuple[str, Any]],
    funcao_reduce: Callable[[list[Any]], Any],
) -> dict[str, Any]:
    pares = fase_map(registros, funcao_map)
    agrupado = fase_shuffle(pares)
    return fase_reduce(agrupado, funcao_reduce)


class TarefaFalhou(Exception):
    def __init__(self, registro: Any, erro_original: BaseException) -> None:
        self.registro = registro
        self.erro_original = erro_original
        super().__init__(f"tarefa de map falhou para {registro!r}: {erro_original}")


def fase_map_tolerante_a_falhas(
    registros: Iterable[Any],
    funcao_map: Callable[[Any], tuple[str, Any]],
    max_tentativas_por_tarefa: int = 3,
) -> list[tuple[str, Any]]:
    """Reexecuta só a tarefa que falhou, não o job inteiro — o princípio
    de reconciliação do roteiro (o mesmo espírito da Aula 11: reatribuir e
    reexecutar, sem intervenção manual para a falha isolada), aplicado a
    tarefas de processamento em vez de Pods."""
    pares: list[tuple[str, Any]] = []
    for registro in registros:
        ultimo_erro: BaseException | None = None
        sucesso = False
        for _tentativa in range(max_tentativas_por_tarefa):
            try:
                pares.append(funcao_map(registro))
                sucesso = True
                break
            except Exception as erro:  # noqa: BLE001 — qualquer falha da tarefa é candidata a retry
                ultimo_erro = erro
        if not sucesso:
            raise TarefaFalhou(registro, ultimo_erro)
    return pares
