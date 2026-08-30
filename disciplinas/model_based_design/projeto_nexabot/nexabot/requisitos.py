"""Requisitos formais do supervisor de segurança do NexaBot.

Cada requisito é um `Requisito`: um identificador rastreável (REQ-SAFE-00N),
uma descrição em português e um predicado *executável* — o mesmo texto que
apareceria numa especificação de sistema, só que testável por código. É essa
tradução "texto ambíguo -> predicado Python verificável" que a Aula 9
demonstra (`aula_09/02_do_texto_a_propriedade.py`).

Tipos de requisito usados nesta disciplina:

- invariante:      deve valer em toda transição alcançável, sempre.
- seguranca:        ("nada de ruim acontece") aqui modelado como invariante
                    de transição — REQ-SAFE-004 é o exemplo clássico de
                    propriedade de segurança que não é uma invariante de
                    estado simples, e sim uma invariante *sobre a transição*
                    (estado -> próximo estado).
- alcancabilidade:  existe algum caminho da inicial até um estado-alvo.
- vivacidade:       ("algo bom eventualmente acontece") aqui também expressa
                    como invariante de transição porque o supervisor é
                    determinístico: "eventualmente MOVENDO" vira "nesta
                    transição específica, o próximo estado é MOVENDO".
- temporizado:      propriedade quantitativa sobre relógio; verificada à
                    parte em `timed.py`, não pelo model checker de estados
                    puros de `modelcheck.py`.
- invariante_continuo: propriedade sobre a trajetória da planta; registrada
                    aqui para rastreabilidade, mas não verificável pelo
                    supervisor discreto isolado.

Assinatura comum dos predicados de transição:

    verificar_transicao(estado, entradas, saida, proximo_estado) -> bool

`True` significa "requisito respeitado nesta transição".
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Optional

from .supervisor import Entradas, Estado, Saidas

VerificarTransicao = Callable[[Estado, Entradas, Saidas, Estado], bool]
PredicadoEstado = Callable[[Estado], bool]


@dataclass(frozen=True)
class Requisito:
    """Um requisito formal do supervisor, com metadados de rastreabilidade."""

    id: str
    tipo: str  # inclui "invariante_continuo", não executável neste módulo
    descricao: str
    verificar_transicao: Optional[VerificarTransicao] = None
    estado_alvo: Optional[PredicadoEstado] = None
    limite_periodos: Optional[int] = None


# --------------------------------------------------------------------------
# REQ-SAFE-001 — invariante
# --------------------------------------------------------------------------
def _req_safe_001(estado: Estado, entradas: Entradas, saida: Saidas, proximo: Estado) -> bool:
    return not (saida.torque_habilitado and entradas.obstaculo)


REQ_SAFE_001 = Requisito(
    id="REQ-SAFE-001",
    tipo="invariante",
    descricao=(
        "Nunca há torque habilitado enquanto o sensor de obstáculo estiver "
        "ativo, em nenhum estado do supervisor."
    ),
    verificar_transicao=_req_safe_001,
)


# --------------------------------------------------------------------------
# REQ-SAFE-002 — invariante
# --------------------------------------------------------------------------
def _req_safe_002(estado: Estado, entradas: Entradas, saida: Saidas, proximo: Estado) -> bool:
    if entradas.emergencia:
        return (not saida.torque_habilitado) and saida.freio_acionado
    return True


REQ_SAFE_002 = Requisito(
    id="REQ-SAFE-002",
    tipo="invariante",
    descricao=(
        "Botão de emergência pressionado implica freio acionado e torque "
        "desabilitado, imediatamente e sem exceção."
    ),
    verificar_transicao=_req_safe_002,
)


# --------------------------------------------------------------------------
# REQ-SAFE-003 — alcançabilidade
# --------------------------------------------------------------------------
REQ_SAFE_003 = Requisito(
    id="REQ-SAFE-003",
    tipo="alcancabilidade",
    descricao="O estado MOVENDO é alcançável a partir do estado inicial OCIOSO.",
    estado_alvo=lambda estado: estado is Estado.MOVENDO,
)


# --------------------------------------------------------------------------
# REQ-SAFE-004 — segurança (invariante de transição)
# --------------------------------------------------------------------------
def _req_safe_004(estado: Estado, entradas: Entradas, saida: Saidas, proximo: Estado) -> bool:
    if estado is Estado.FALHA and proximo is not Estado.FALHA:
        return entradas.rearme
    return True


REQ_SAFE_004 = Requisito(
    id="REQ-SAFE-004",
    tipo="seguranca",
    descricao=(
        "A partir do estado FALHA, a única saída possível é por rearme "
        "explícito (entradas.rearme = True) — nunca por decurso de tempo, "
        "novo comando do operador ou qualquer outra condição."
    ),
    verificar_transicao=_req_safe_004,
)


# --------------------------------------------------------------------------
# REQ-SAFE-005 — vivacidade (invariante de transição, dado determinismo)
# --------------------------------------------------------------------------
def _req_safe_005(estado: Estado, entradas: Entradas, saida: Saidas, proximo: Estado) -> bool:
    # Qualificação "na ausência de outra condição de segurança de prioridade
    # maior" foi adicionada DEPOIS de o model checker apontar um
    # contraexemplo real: PARADO_OBSTACULO, obstáculo removido, comando de
    # partida presente, mas com falha_encoder simultânea — nesse caso ir
    # para MOVENDO seria inseguro, e o texto original do requisito (que não
    # previa faults concorrentes) estava incompleto. Ver
    # aula_09/02_do_texto_a_propriedade.py para a história completa.
    condicao_disparo = (
        estado is Estado.PARADO_OBSTACULO
        and not entradas.obstaculo
        and entradas.comando_partir
        and not entradas.emergencia
        and not entradas.falha_encoder
    )
    if condicao_disparo:
        return proximo is Estado.MOVENDO
    return True


REQ_SAFE_005 = Requisito(
    id="REQ-SAFE-005",
    tipo="vivacidade",
    descricao=(
        "Uma vez removido o obstáculo, havendo comando de partida do "
        "operador e nenhuma outra condição de segurança concorrente "
        "(emergência, falha de encoder), o sistema volta a MOVENDO — o "
        "robô não fica preso em PARADO_OBSTACULO para sempre."
    ),
    verificar_transicao=_req_safe_005,
)


# --------------------------------------------------------------------------
# REQ-SAFE-006 — temporizado (verificado em timed.py, não em modelcheck.py)
# --------------------------------------------------------------------------
REQ_SAFE_006 = Requisito(
    id="REQ-SAFE-006",
    tipo="temporizado",
    descricao=(
        "Após a detecção de obstáculo (ou emergência), o torque chega a "
        "zero em no máximo d_stop_max = 150 ms, isto é, 30 períodos de "
        "amostragem Ts = 5 ms — mesmo no pior caso de atraso de detecção "
        "e de um ciclo de atuação perdido."
    ),
    limite_periodos=30,
)


# --------------------------------------------------------------------------
# REQ-SAFE-007 — invariante contínuo (lacuna explicitamente rastreada)
# --------------------------------------------------------------------------
REQ_SAFE_007 = Requisito(
    id="REQ-SAFE-007",
    tipo="invariante_continuo",
    descricao=(
        "A velocidade linear do NexaBot não ultrapassa 1,20 m/s no domínio "
        "operacional especificado. Este requisito depende da trajetória "
        "contínua da planta e não é verificável pelo supervisor discreto "
        "isolado; permanece como lacuna explícita neste laboratório."
    ),
)


REQUISITOS: list[Requisito] = [
    REQ_SAFE_001,
    REQ_SAFE_002,
    REQ_SAFE_003,
    REQ_SAFE_004,
    REQ_SAFE_005,
    REQ_SAFE_006,
    REQ_SAFE_007,
]

#: Requisitos verificáveis transição a transição pelo model checker de
#: estados explícitos (exclui REQ-SAFE-003, que é alcançabilidade, e
#: REQ-SAFE-006, que é temporizado).
REQUISITOS_TRANSICAO: list[Requisito] = [r for r in REQUISITOS if r.verificar_transicao is not None]

#: Requisitos de alcançabilidade pura.
REQUISITOS_ALCANCABILIDADE: list[Requisito] = [r for r in REQUISITOS if r.estado_alvo is not None]


def por_id(requisito_id: str) -> Requisito:
    """Busca um requisito pelo identificador REQ-SAFE-00N."""
    for r in REQUISITOS:
        if r.id == requisito_id:
            return r
    raise KeyError(f"requisito desconhecido: {requisito_id!r}")
