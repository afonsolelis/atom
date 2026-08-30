"""Supervisor de segurança do NexaBot — máquina de estados finitos explícita.

Este módulo é o objeto de estudo da Unidade 3 (Aulas 9 a 12): verificação
formal e testes baseados em modelos. A máquina é *determinística* (uma única
transição possível para cada par estado/entrada) e *pura* — a função
`transition` não tem efeito colateral algum, condição necessária para que o
`modelcheck.py` consiga explorá-la por busca em largura sem precisar
instanciar objetos.

Estados
-------
OCIOSO             robô parado, aguardando comando do operador.
MOVENDO            tração habilitada, robô em marcha normal.
DESACELERANDO      parada controlada (comando do operador), sem tração.
PARADO_OBSTACULO   parada de segurança por obstáculo detectado.
FALHA              falha de encoder — estado absorvente até rearme.
EMERGENCIA         botão de emergência — estado absorvente até rearme.

Entradas
--------
comando_partir     operador pediu para o robô se mover.
comando_parar      operador pediu parada controlada.
obstaculo          sensor de obstáculo ativo (True = obstáculo presente).
emergencia         botão de emergência pressionado.
falha_encoder      diagnóstico do encoder acusou falha.
rearme             operador confirmou rearme explícito (RESET).
velocidade         velocidade linear atual do robô [m/s] (usada só para
                   decidir quando uma desaceleração terminou).

Saídas
------
torque_habilitado  autoriza o driver do motor a entregar torque.
freio_acionado     comanda o freio mecânico/regenerativo.

Rastreabilidade: REQ-SAFE-001 a REQ-SAFE-006 (ver `nexabot/requisitos.py`).
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto


class Estado(Enum):
    """Estados de controle do supervisor de segurança."""

    OCIOSO = auto()
    MOVENDO = auto()
    DESACELERANDO = auto()
    PARADO_OBSTACULO = auto()
    FALHA = auto()
    EMERGENCIA = auto()


ESTADO_INICIAL = Estado.OCIOSO

#: Tolerância de velocidade abaixo da qual o robô é considerado "parado"
#: para fins de transição de estado (não confundir com o zero exato de
#: ponto flutuante). Unidade: m/s.
V_TOL = 0.02


@dataclass(frozen=True)
class Entradas:
    """Vetor de entradas do supervisor num instante de amostragem k.Ts."""

    comando_partir: bool = False
    comando_parar: bool = False
    obstaculo: bool = False
    emergencia: bool = False
    falha_encoder: bool = False
    rearme: bool = False
    velocidade: float = 0.0

    def parado(self) -> bool:
        """True se a velocidade atual está dentro da tolerância de repouso."""
        return abs(self.velocidade) <= V_TOL


@dataclass(frozen=True)
class Saidas:
    """Vetor de saídas do supervisor num instante de amostragem k.Ts."""

    torque_habilitado: bool
    freio_acionado: bool


def transition(estado: Estado, entradas: Entradas) -> tuple[Estado, Saidas]:
    """Função de transição pura e determinística: (estado, entradas) -> (estado', saídas).

    A ordem dos testes abaixo *é* a política de prioridade de segurança do
    supervisor. Ela não é uma cadeia simples "emergência > falha > obstáculo":
    FALHA é verificada primeiro porque é *estritamente absorvente* — nem
    emergência, nem obstáculo, nem comando algum tiram o supervisor de FALHA
    sem rearme explícito (REQ-SAFE-004). Só depois disso é que a emergência
    tem prioridade absoluta sobre as demais entradas (REQ-SAFE-002), seguida
    da falha de encoder recém-detectada e do obstáculo. Cada bloco documenta
    o(s) requisito(s) formal(is) que garante.
    """
    # --- REQ-SAFE-004: FALHA é estritamente absorvente. Este bloco vem
    # ANTES do teste global de emergência de propósito: uma falha de
    # encoder não pode ser "contornada" pelo botão de emergência nem por
    # nenhuma outra entrada — a única saída é rearme explícito com a falha
    # já removida. (Isto foi descoberto pelo próprio model checker: uma
    # versão anterior testava `entradas.emergencia` antes deste bloco e
    # permitia sair de FALHA sem rearme — ver aula_10/02_contraexemplo.py.) ---
    if estado is Estado.FALHA:
        if entradas.rearme and not entradas.falha_encoder:
            if entradas.emergencia:
                return Estado.EMERGENCIA, Saidas(torque_habilitado=False, freio_acionado=True)
            return Estado.OCIOSO, Saidas(torque_habilitado=False, freio_acionado=False)
        return Estado.FALHA, Saidas(torque_habilitado=False, freio_acionado=True)

    # --- REQ-SAFE-002: o botão de emergência tem prioridade absoluta sobre
    # qualquer entrada restante (obstáculo, comandos do operador). Enquanto
    # o botão estiver pressionado o supervisor permanece em EMERGENCIA. ---
    if entradas.emergencia:
        return Estado.EMERGENCIA, Saidas(torque_habilitado=False, freio_acionado=True)

    # Botão de emergência já foi solto (entradas.emergencia == False), mas o
    # supervisor ainda está no estado EMERGENCIA: só sai por rearme explícito
    # (mesmo princípio de "sem retomada silenciosa" usado no REQ-SAFE-004).
    if estado is Estado.EMERGENCIA:
        if entradas.rearme:
            if entradas.falha_encoder:
                return Estado.FALHA, Saidas(torque_habilitado=False, freio_acionado=True)
            return Estado.OCIOSO, Saidas(torque_habilitado=False, freio_acionado=False)
        return Estado.EMERGENCIA, Saidas(torque_habilitado=False, freio_acionado=True)

    # --- REQ-SAFE-004 (entrada): falha de encoder leva a FALHA a partir de
    # qualquer estado normal restante (já tratamos FALHA e EMERGENCIA acima). ---
    if entradas.falha_encoder:
        return Estado.FALHA, Saidas(torque_habilitado=False, freio_acionado=True)

    # --- REQ-SAFE-001: nunca há torque habilitado enquanto o obstáculo
    # estiver presente, em nenhum estado. A saída é combinacional: o corte
    # de torque não espera o próximo ciclo de controle. (O atraso físico até
    # o torque efetivamente chegar a zero é modelado à parte, em timed.py,
    # como REQ-SAFE-006.) ---
    if entradas.obstaculo:
        if estado in (Estado.MOVENDO, Estado.DESACELERANDO, Estado.PARADO_OBSTACULO):
            return Estado.PARADO_OBSTACULO, Saidas(torque_habilitado=False, freio_acionado=True)
        # Robô já ocioso: nada a frear, só ignora um eventual comando de partida.
        return Estado.OCIOSO, Saidas(torque_habilitado=False, freio_acionado=False)

    # A partir daqui: emergencia=False, falha_encoder=False, obstaculo=False,
    # e o estado corrente não é FALHA nem EMERGENCIA (já teriam retornado).

    if estado is Estado.OCIOSO:
        # --- REQ-SAFE-003: MOVENDO é alcançável a partir de OCIOSO. ---
        if entradas.comando_partir:
            return Estado.MOVENDO, Saidas(torque_habilitado=True, freio_acionado=False)
        return Estado.OCIOSO, Saidas(torque_habilitado=False, freio_acionado=False)

    if estado is Estado.MOVENDO:
        if entradas.comando_parar:
            return Estado.DESACELERANDO, Saidas(torque_habilitado=False, freio_acionado=True)
        return Estado.MOVENDO, Saidas(torque_habilitado=True, freio_acionado=False)

    if estado is Estado.DESACELERANDO:
        if entradas.parado():
            return Estado.OCIOSO, Saidas(torque_habilitado=False, freio_acionado=False)
        return Estado.DESACELERANDO, Saidas(torque_habilitado=False, freio_acionado=True)

    if estado is Estado.PARADO_OBSTACULO:
        # --- REQ-SAFE-005: obstáculo removido (garantido aqui, pois o bloco
        # `if entradas.obstaculo` já teria retornado) + comando de partida
        # => volta a MOVENDO. Sem comando de partida, cai para OCIOSO à
        # espera de uma nova ordem do operador. ---
        if entradas.comando_partir:
            return Estado.MOVENDO, Saidas(torque_habilitado=True, freio_acionado=False)
        return Estado.OCIOSO, Saidas(torque_habilitado=False, freio_acionado=False)

    raise AssertionError(f"estado não tratado pela transição: {estado!r}")


@dataclass
class Supervisor:
    """Envelope com estado mutável em torno da função pura `transition`.

    É o objeto que o código embarcado (e as Aulas 9-12 em execução ao vivo)
    realmente instancia; o verificador formal, por outro lado, usa
    `transition` diretamente, sem precisar desta classe.
    """

    state: Estado = ESTADO_INICIAL

    def step(self, entradas: Entradas) -> Saidas:
        """Executa um passo de amostragem e atualiza `self.state`."""
        novo_estado, saidas = transition(self.state, entradas)
        self.state = novo_estado
        return saidas

    def reset(self) -> None:
        """Reinicializa o supervisor para o estado inicial (uso em testes)."""
        self.state = ESTADO_INICIAL
