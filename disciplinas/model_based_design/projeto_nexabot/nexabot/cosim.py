"""Mestre de co-simulacao FMI 3.0: acopla o FMU da planta ao DiscretePID.

Aula 8 — "Co-simulacao planta-controlador com FMI 3.0". A planta
(`NexaBotPlant.fmu`, em C, ver `nexabot/fmu/plant_fmu.c`) e carregada com a
API de baixo nivel do fmpy (`fmpy.fmi3.FMU3Slave`), NAO com
`fmpy.simulate_fmu` — porque aqui o controlador e um subsistema EXTERNO ao
FMU: em cada passo de comunicacao H, o mestre le a saida da planta (omega),
calcula a lei de controle em Python (`DiscretePID`, o mesmo objeto que
governa toda a Unidade 4) e escreve a tensao de volta no FMU antes de
avancar o tempo com `fmi3DoStep`.

Esse laco — ler saida, calcular controle, escrever entrada, avancar H — E
a co-simulacao. O passo de comunicacao H e o parametro central da aula: e
o intervalo em que as duas partes (planta e controlador) ficam "cegas" uma
para a outra, com o comando de tensao mantido constante (ZOH) por toda a
janela. Quanto maior H, maior esse "erro de acoplamento" — ver
`aula_08/04_erro_de_acoplamento.py`.

Rastreabilidade: REQ-CTRL-001 (rastreamento de velocidade), REQ-PLANT-001.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
from fmpy import extract, read_model_description
from fmpy.fmi3 import FMU3Slave

from nexabot.controllers import DiscretePID
from nexabot.params import PARAMS, NexaBotParams

FMU_PATH = Path(__file__).resolve().parent / "fmu" / "NexaBotPlant.fmu"

# Value references do FMU (devem bater com modelDescription.xml / plant_fmu.c)
VR_U_VOLTS = 0
VR_TAU_LOAD = 1
VR_OMEGA = 2
VR_CURRENT = 3


@dataclass
class ResultadoCoSimulacao:
    """Series temporais devolvidas por `run_cosimulation`."""

    t: np.ndarray            # instantes de comunicacao [s]
    omega: np.ndarray        # velocidade angular do motor medida [rad/s]
    corrente: np.ndarray     # corrente de armadura medida [A]
    referencia: np.ndarray   # referencia de velocidade angular [rad/s]
    tensao: np.ndarray       # tensao de comando aplicada pelo PID [V]
    H: float                 # passo de comunicacao usado [s]


class PlantaFMU:
    """Wrapper fino sobre `FMU3Slave` para a planta do NexaBot.

    Usa deliberadamente a API de baixo nivel do fmpy (instanciar, setar
    entradas, avancar um `doStep`, ler saidas) em vez de
    `fmpy.simulate_fmu`, que so serve para rodar um FMU sozinho — aqui o
    controlador mora fora do FMU e precisa intercalar suas proprias
    chamadas entre os passos de simulacao da planta.
    """

    def __init__(self, fmu_path: Path = FMU_PATH, instance_name: str = "NexaBotPlant"):
        self.fmu_path = fmu_path
        self.model_description = read_model_description(str(fmu_path))
        self.unzipdir = extract(str(fmu_path))
        self.fmu = FMU3Slave(
            guid=self.model_description.guid,
            unzipDirectory=self.unzipdir,
            modelIdentifier=self.model_description.coSimulation.modelIdentifier,
            instanceName=instance_name,
        )

    def __enter__(self) -> "PlantaFMU":
        self.fmu.instantiate()
        self.fmu.enterInitializationMode(startTime=0.0)
        self.fmu.exitInitializationMode()
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.fmu.terminate()
        self.fmu.freeInstance()

    def set_entradas(self, u_volts: float, tau_load: float) -> None:
        self.fmu.setFloat64([VR_U_VOLTS, VR_TAU_LOAD], [float(u_volts), float(tau_load)])

    def do_step(self, t: float, H: float) -> None:
        self.fmu.doStep(currentCommunicationPoint=t, communicationStepSize=H)

    def get_saidas(self) -> tuple[float, float]:
        """Devolve (omega, corrente)."""
        omega, corrente = self.fmu.getFloat64([VR_OMEGA, VR_CURRENT])
        return omega, corrente


def run_cosimulation(
    H: float,
    t_end: float,
    v_ref,
    Kp: float = 0.30,
    Ki: float = 6.0,
    Kd: float = 0.0,
    tau_load_of_t=None,
    p: NexaBotParams = PARAMS,
    fmu_path: Path = FMU_PATH,
) -> ResultadoCoSimulacao:
    """Roda a co-simulacao planta (FMU) + controlador (`DiscretePID`, Python).

    Parametros
    ----------
    H
        Passo de comunicacao [s]: intervalo entre trocas de informacao
        planta <-> controlador. Este e o parametro pedagogico central da
        aula — ver `aula_08/04_erro_de_acoplamento.py`.
    t_end
        Duracao simulada [s].
    v_ref
        Velocidade linear de referencia [m/s]: um numero (degrau constante)
        ou uma funcao `v_ref(t) -> float`.
    Kp, Ki, Kd
        Ganhos do `DiscretePID` que roda no mestre (Ts do PID = H).
    tau_load_of_t
        Funcao opcional `tau_load(t) -> float` (torque de carga [N.m]).
        Usada pelo `aula_08/05_desafio.py` para acoplar um disturbio.
    p
        Parametros do NexaBot (para converter v_ref em omega_ref).

    Devolve
    -------
    ResultadoCoSimulacao com os arrays de tempo, omega, corrente, referencia
    e tensao amostrados em cada passo de comunicacao.
    """
    if H <= 0:
        raise ValueError("H deve ser positivo")

    n_steps = int(round(t_end / H))

    pid = DiscretePID(Kp=Kp, Ki=Ki, Kd=Kd, Ts=H, u_max=p.V_max)

    t_arr = np.zeros(n_steps + 1)
    omega_arr = np.zeros(n_steps + 1)
    corrente_arr = np.zeros(n_steps + 1)
    ref_arr = np.zeros(n_steps + 1)
    tensao_arr = np.zeros(n_steps + 1)

    def _v_ref_at(t: float) -> float:
        return float(v_ref(t)) if callable(v_ref) else float(v_ref)

    def _tau_at(t: float) -> float:
        return float(tau_load_of_t(t)) if callable(tau_load_of_t) else float(tau_load_of_t or 0.0)

    with PlantaFMU(fmu_path=fmu_path) as planta:
        omega, corrente = planta.get_saidas()
        omega_ref0 = p.v_to_omega(_v_ref_at(0.0))

        t_arr[0] = 0.0
        omega_arr[0] = omega
        corrente_arr[0] = corrente
        ref_arr[0] = omega_ref0
        tensao_arr[0] = 0.0

        for k in range(n_steps):
            tk = k * H
            omega_ref = p.v_to_omega(_v_ref_at(tk))

            # Controlador (mestre, Python): le a saida medida da planta no
            # instante tk e calcula a tensao a aplicar durante [tk, tk+H).
            u = pid.step(r=omega_ref, y=omega)

            tau_load = _tau_at(tk)
            planta.set_entradas(u_volts=u, tau_load=tau_load)
            planta.do_step(t=tk, H=H)
            omega, corrente = planta.get_saidas()

            t_arr[k + 1] = tk + H
            omega_arr[k + 1] = omega
            corrente_arr[k + 1] = corrente
            ref_arr[k + 1] = omega_ref
            tensao_arr[k + 1] = u

    return ResultadoCoSimulacao(
        t=t_arr, omega=omega_arr, corrente=corrente_arr,
        referencia=ref_arr, tensao=tensao_arr, H=H,
    )
