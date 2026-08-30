"""Parâmetros físicos identificados do NexaBot — fio condutor da disciplina.

Todos os valores são do eixo de tração esquerdo do AGV NexaBot: um motor CC
de ímã permanente de 24 V acoplado a um redutor e a uma roda de 50 mm de raio.
Os valores de R, L, Kt, J e b foram obtidos no ensaio de identificação da
Aula 2 e são a única fonte de verdade numérica de toda a disciplina.

Rastreabilidade: REQ-PLANT-001 (modelo de planta), REQ-PLANT-002 (limites).
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class NexaBotParams:
    """Parâmetros do eixo de tração do NexaBot.

    Unidades no SI. `frozen=True` porque um parâmetro identificado é um dado
    de ensaio: alterá-lo em tempo de execução invalidaria a rastreabilidade
    entre o modelo, o código gerado e os testes.
    """

    # --- Elétricos -------------------------------------------------------
    R: float = 1.2          # resistência de armadura [ohm]
    L: float = 3.5e-3       # indutância de armadura [H]
    Ke: float = 0.045       # constante de força contraeletromotriz [V.s/rad]
    Kt: float = 0.045       # constante de torque [N.m/A]

    # --- Mecânicos (refletidos ao eixo do motor) -------------------------
    J: float = 2.5e-4       # inércia motor + redutor + carga [kg.m^2]
    b: float = 8.0e-5       # atrito viscoso [N.m.s/rad]

    # --- Transmissão e roda ---------------------------------------------
    N_gear: float = 20.0    # relação de redução [motor:roda]
    r_wheel: float = 0.05   # raio da roda [m]

    # --- Limites do atuador (REQ-PLANT-002) ------------------------------
    V_max: float = 24.0     # tensão máxima do driver [V]
    i_max: float = 12.0     # corrente máxima admissível [A]

    # --- Temporização do controlador embarcado ---------------------------
    Ts: float = 5.0e-3      # período de amostragem adotado [s] (200 Hz)

    # --- Requisitos de segurança (REQ-SAFE-*) ----------------------------
    d_stop_max: float = 0.150   # prazo máximo para zerar torque após obstáculo [s]
    v_max_safe: float = 1.20    # velocidade linear máxima admissível [m/s]

    def omega_to_v(self, omega_motor: float) -> float:
        """Converte velocidade angular do motor [rad/s] em velocidade linear [m/s]."""
        return omega_motor / self.N_gear * self.r_wheel

    def v_to_omega(self, v_linear: float) -> float:
        """Converte velocidade linear [m/s] em velocidade angular do motor [rad/s]."""
        return v_linear / self.r_wheel * self.N_gear

    @property
    def dc_gain(self) -> float:
        """Ganho estático omega/V em regime permanente [rad/(s.V)].

        Obtido igualando as duas derivadas a zero:
            0 = V - R.i - Ke.w   e   0 = Kt.i - b.w
        => w/V = Kt / (R.b + Kt.Ke)
        """
        return self.Kt / (self.R * self.b + self.Kt * self.Ke)

    @property
    def tau_elec(self) -> float:
        """Constante de tempo elétrica aproximada L/R [s]."""
        return self.L / self.R

    @property
    def tau_mech(self) -> float:
        """Constante de tempo mecânica aproximada J.R/(Kt.Ke) [s]."""
        return self.J * self.R / (self.Kt * self.Ke)


PARAMS = NexaBotParams()
