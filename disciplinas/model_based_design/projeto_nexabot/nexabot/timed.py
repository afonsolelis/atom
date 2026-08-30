"""Autômato temporizado de tempo discreto — watchdog do REQ-SAFE-006.

O supervisor de `supervisor.py` já garante, de forma combinacional, que o
sinal digital `torque_habilitado` nunca fica em True enquanto `obstaculo`
está ativo (REQ-SAFE-001). Mas isso é uma abstração de tempo zero: na
prática, entre o instante físico em que o obstáculo surge e o instante em
que o torque do motor efetivamente chega a zero, existem atrasos reais —
filtro/debounce do sensor, tempo de varredura do supervisor, possibilidade
de um ciclo de atuação ser perdido (jitter de escalonamento, barramento).

Este módulo modela esses atrasos como um autômato temporizado *discreto*: o
relógio conta em número inteiro de períodos de amostragem `Ts` (não em
segundos contínuos), exatamente como um microcontrolador contaria "ticks"
de um timer. A verificação é exaustiva: percorremos todas as combinações
possíveis de atraso de detecção e de perda (ou não) de um ciclo de atuação,
e conferimos que em NENHUM caminho o relógio ultrapassa o limite de
REQ-SAFE-006 (150 ms = 30 períodos de 5 ms).

Rastreabilidade: REQ-SAFE-006.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto

from .params import PARAMS

#: Limite do requisito, em períodos de amostragem inteiros.
LIMITE_PERIODOS = round(PARAMS.d_stop_max / PARAMS.Ts)  # 150 ms / 5 ms = 30


class EstadoTemporizado(Enum):
    """Estados do autômato temporizado do watchdog de parada de emergência."""

    NORMAL = auto()       # nenhum gatilho de parada ativo; torque livre
    DETECTANDO = auto()   # gatilho físico presente, ainda não reconhecido
    COMANDANDO = auto()   # supervisor reconheceu e está cortando o torque
    ZERADO = auto()        # torque = 0 confirmado (absorvente nesta análise)


@dataclass(frozen=True)
class NoTemporizado:
    """Um nó do espaço de estados temporizado: (estado de controle, relógio)."""

    estado: EstadoTemporizado
    clock: int                 # períodos decorridos desde o gatilho
    ciclo_perdido_usado: bool  # se a trajetória já "gastou" seu ciclo perdido

    def __repr__(self) -> str:  # pragma: no cover - só para depuração/print
        return f"({self.estado.name}, t={self.clock}, perdido={self.ciclo_perdido_usado})"


@dataclass(frozen=True)
class Caminho:
    """Uma trajetória completa do autômato, do gatilho até ZERADO."""

    nos: tuple  # tuple[NoTemporizado, ...]
    atraso_deteccao_periodos: int
    usou_ciclo_perdido: bool

    @property
    def periodos_ate_zerar(self) -> int:
        return self.nos[-1].clock

    @property
    def ms_ate_zerar(self) -> float:
        return self.periodos_ate_zerar * PARAMS.Ts * 1000.0


def _sucessores(no: NoTemporizado, atraso_deteccao_max: int, permite_ciclo_perdido: bool):
    """Gera os nós sucessores possíveis (as escolhas não determinísticas do ambiente).

    - Em DETECTANDO: a cada período, o ambiente escolhe "confirmar agora"
      (passar a COMANDANDO) ou "continuar atrasando", até o limite
      `atraso_deteccao_max` de períodos — a partir daí a confirmação é
      obrigatória (o atraso de detecção é limitado, não arbitrário).
    - Em COMANDANDO: a cada período, o ambiente escolhe "ciclo de atuação
      bem-sucedido" (torque vai a zero => ZERADO) ou, se ainda não usou o
      "cartão" de ciclo perdido e isso é permitido, "ciclo perdido" (mais um
      período em COMANDANDO, sem cortar o torque).
    """
    if no.estado is EstadoTemporizado.DETECTANDO:
        sucessores = []
        se_pode_atrasar = no.clock < atraso_deteccao_max
        # opção 1: confirma agora, passa a comandar o corte de torque
        sucessores.append(
            NoTemporizado(EstadoTemporizado.COMANDANDO, no.clock + 1, no.ciclo_perdido_usado)
        )
        # opção 2: continua atrasando a detecção (só se ainda há margem)
        if se_pode_atrasar:
            sucessores.append(
                NoTemporizado(EstadoTemporizado.DETECTANDO, no.clock + 1, no.ciclo_perdido_usado)
            )
        return sucessores

    if no.estado is EstadoTemporizado.COMANDANDO:
        sucessores = [NoTemporizado(EstadoTemporizado.ZERADO, no.clock + 1, no.ciclo_perdido_usado)]
        if permite_ciclo_perdido and not no.ciclo_perdido_usado:
            sucessores.append(
                NoTemporizado(EstadoTemporizado.COMANDANDO, no.clock + 1, True)
            )
        return sucessores

    return []  # ZERADO é absorvente: nenhum sucessor


def explorar_caminhos(atraso_deteccao_max: int, permite_ciclo_perdido: bool = True) -> list:
    """Explora exaustivamente (DFS) todos os caminhos do gatilho até ZERADO.

    `atraso_deteccao_max` é o pior atraso de detecção admitido pelo projeto
    do sensor/filtro, em períodos de amostragem. Devolve a lista de todos os
    `Caminho` possíveis — o pior caso é o de maior `periodos_ate_zerar`.
    """
    caminhos: list[Caminho] = []
    raiz = NoTemporizado(EstadoTemporizado.DETECTANDO, 0, False)

    pilha = [(raiz,)]
    while pilha:
        caminho_atual = pilha.pop()
        ultimo = caminho_atual[-1]
        if ultimo.estado is EstadoTemporizado.ZERADO:
            caminhos.append(
                Caminho(
                    nos=caminho_atual,
                    atraso_deteccao_periodos=_periodos_em_deteccao(caminho_atual),
                    usou_ciclo_perdido=ultimo.ciclo_perdido_usado,
                )
            )
            continue
        for sucessor in _sucessores(ultimo, atraso_deteccao_max, permite_ciclo_perdido):
            pilha.append(caminho_atual + (sucessor,))

    return caminhos


def _periodos_em_deteccao(caminho: tuple) -> int:
    return sum(1 for no in caminho if no.estado is EstadoTemporizado.DETECTANDO)


@dataclass(frozen=True)
class ResultadoWatchdog:
    """Resultado da verificação exaustiva do REQ-SAFE-006."""

    ok: bool
    pior_caso_periodos: int
    pior_caso_ms: float
    pior_caminho: Caminho
    n_caminhos_explorados: int
    limite_periodos: int = LIMITE_PERIODOS
    limite_ms: float = PARAMS.d_stop_max * 1000.0


def verificar_req_safe_006(
    atraso_deteccao_max: int = 2, permite_ciclo_perdido: bool = True
) -> ResultadoWatchdog:
    """Verifica exaustivamente o REQ-SAFE-006 para um cenário de atraso dado.

    `atraso_deteccao_max` = pior atraso de detecção de sensor admitido pelo
    projeto (em períodos de Ts=5 ms). Por padrão, 2 períodos = 10 ms — valor
    conservador para o filtro do sensor de obstáculo do NexaBot — mais um
    eventual ciclo de atuação perdido.
    """
    caminhos = explorar_caminhos(atraso_deteccao_max, permite_ciclo_perdido)
    pior = max(caminhos, key=lambda c: c.periodos_ate_zerar)
    return ResultadoWatchdog(
        ok=pior.periodos_ate_zerar <= LIMITE_PERIODOS,
        pior_caso_periodos=pior.periodos_ate_zerar,
        pior_caso_ms=pior.ms_ate_zerar,
        pior_caminho=pior,
        n_caminhos_explorados=len(caminhos),
    )


def formatar_caminho_temporizado(caminho: Caminho) -> str:
    """Representação textual de uma trajetória do autômato temporizado."""
    partes = [f"{no.estado.name}@t{no.clock}" for no in caminho.nos]
    return " -> ".join(partes)
