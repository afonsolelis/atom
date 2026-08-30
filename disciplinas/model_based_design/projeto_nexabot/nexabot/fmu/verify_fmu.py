"""Verifica que o FMU `NexaBotPlant.fmu` reproduz `nexabot.plant.simulate`.

Este script NAO estuda o erro de acoplamento da co-simulacao (isso e o
`aula_08/04_erro_de_acoplamento.py`); ele responde uma pergunta mais basica
e anterior: "o integrador RK4 em C dentro do FMU calcula a MESMA fisica que
o integrador RK4 de referencia em `plant.py`, com os mesmos parametros?".

Para isolar essa pergunta do efeito de acoplamento (que existe sempre que a
entrada e mantida constante — ZOH — por um intervalo H), usamos uma entrada
u(t)/tau_load(t) que ja e, por construcao, uma escada constante em degraus
de largura H (exatamente o que um mestre de co-simulacao aplica). Assim,
tanto a referencia em Python (integrada com passo fino) quanto o FMU
(amostrado nos instantes multiplos de H) enxergam a MESMA entrada fisica —
qualquer diferenca remanescente e erro numerico do integrador, nao erro de
ZOH.

Uso:

    .venv/bin/python -m nexabot.fmu.verify_fmu
"""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np
from fmpy import extract, read_model_description
from fmpy.fmi3 import FMU3Slave

from nexabot import plant
from nexabot.params import PARAMS

FMU_PATH = Path(__file__).resolve().parent / "NexaBotPlant.fmu"

# Passo de comunicacao usado no teste: multiplo do micro-passo interno do
# FMU (5e-5 s), representativo de um controlador digital tipico do NexaBot.
H = PARAMS.Ts          # 5 ms
T_END = 0.5            # s
DT_REFERENCIA = 1.0e-5  # passo fino do integrador de referencia (plant.py)


def degrau_escada(t: float, valores: list[float], largura: float) -> float:
    """Entrada em escada: constante e igual a valores[k] durante [k.largura, (k+1).largura).

    O deslocamento `1e-9` evita que ruido de ponto flutuante (H=5 ms nao e
    exatamente representavel em binario) empurre uma amostra que deveria
    cair em k*H para o balde k-1 por um bit de arredondamento — o que
    faria a referencia Python e o FMU lerem degraus DIFERENTES no mesmo
    instante nominal e contaminaria a comparacao com um artefato do teste,
    nao um erro real do FMU.
    """
    k = int(math.floor(t / largura + 1e-9))
    k = max(0, min(k, len(valores) - 1))
    return valores[k]


def montar_entradas():
    """Monta u(t) e tau_load(t) como escadas alinhadas ao passo H."""
    n_degraus = int(math.ceil(T_END / H)) + 1
    rng = np.random.default_rng(42)
    tensoes = list(12.0 + 8.0 * np.sin(np.arange(n_degraus) * 0.35))
    tensoes[0] = 0.0  # parte do repouso
    torques = list(0.02 * np.sin(np.arange(n_degraus) * 0.21 + 1.0))
    torques[0] = 0.0

    def u_of_t(t):
        return degrau_escada(t, tensoes, H)

    def tau_of_t(t):
        return degrau_escada(t, torques, H)

    return u_of_t, tau_of_t


def rodar_referencia_python(u_of_t, tau_of_t):
    """Integra a planta de referencia (Python/RK4) com passo fino."""
    t, X = plant.simulate(u_of_t, T_END, dt=DT_REFERENCIA, tau_load_of_t=tau_of_t)
    return t, X[:, 1], X[:, 0]  # tempo, omega, corrente


def rodar_fmu(u_of_t, tau_of_t):
    """Executa o mesmo cenario atraves do FMU, amostrado nos multiplos de H."""
    md = read_model_description(str(FMU_PATH))
    unzipdir = extract(str(FMU_PATH))

    fmu = FMU3Slave(
        guid=md.guid,
        unzipDirectory=unzipdir,
        modelIdentifier=md.coSimulation.modelIdentifier,
        instanceName="verify_fmu",
    )
    fmu.instantiate()
    fmu.enterInitializationMode(startTime=0.0)
    fmu.exitInitializationMode()

    n_steps = int(round(T_END / H))
    t_fmu = [0.0]
    omega_fmu = [0.0]
    corrente_fmu = [0.0]

    for k in range(n_steps):
        tk = k * H
        fmu.setFloat64([0, 1], [float(u_of_t(tk)), float(tau_of_t(tk))])
        fmu.doStep(currentCommunicationPoint=tk, communicationStepSize=H)
        w, i = fmu.getFloat64([2, 3])
        t_fmu.append(tk + H)
        omega_fmu.append(w)
        corrente_fmu.append(i)

    fmu.terminate()
    fmu.freeInstance()

    return np.array(t_fmu), np.array(omega_fmu), np.array(corrente_fmu)


def interpolar_na_grade(t_fino, y_fino, t_grosso):
    """Amostra a trajetoria fina de referencia exatamente nos instantes do FMU."""
    return np.interp(t_grosso, t_fino, y_fino)


def erro_relativo_maximo(referencia, teste):
    escala = max(np.max(np.abs(referencia)), 1e-9)
    return float(np.max(np.abs(teste - referencia))) / escala


def main() -> int:
    if not FMU_PATH.exists():
        print(f"ERRO: {FMU_PATH} nao existe. Rode antes:")
        print("  .venv/bin/python -m nexabot.fmu.build_fmu")
        return 1

    print("=" * 78)
    print("VERIFICACAO: FMU (C) vs plant.simulate (Python) — mesma entrada")
    print("=" * 78)
    print(f"Passo de comunicacao H         : {H*1000:.3f} ms")
    print(f"Passo fino da referencia Python : {DT_REFERENCIA*1000:.4f} ms")
    print(f"Duracao simulada                : {T_END:.3f} s")
    print()

    u_of_t, tau_of_t = montar_entradas()

    t_ref, omega_ref, corrente_ref = rodar_referencia_python(u_of_t, tau_of_t)
    t_fmu, omega_fmu, corrente_fmu = rodar_fmu(u_of_t, tau_of_t)

    omega_ref_na_grade = interpolar_na_grade(t_ref, omega_ref, t_fmu)
    corrente_ref_na_grade = interpolar_na_grade(t_ref, corrente_ref, t_fmu)

    erro_omega = erro_relativo_maximo(omega_ref_na_grade, omega_fmu)
    erro_corrente = erro_relativo_maximo(corrente_ref_na_grade, corrente_fmu)

    print(f"{'t [s]':>8} {'omega_py':>12} {'omega_fmu':>12} {'err_rel_%':>11} "
          f"{'i_py':>10} {'i_fmu':>10} {'err_rel_%':>11}")
    print("-" * 78)
    idx_mostrar = np.linspace(0, len(t_fmu) - 1, 12, dtype=int)
    escala_w = max(np.max(np.abs(omega_ref_na_grade)), 1e-9)
    escala_i = max(np.max(np.abs(corrente_ref_na_grade)), 1e-9)
    for idx in idx_mostrar:
        ew = abs(omega_fmu[idx] - omega_ref_na_grade[idx]) / escala_w * 100.0
        ei = abs(corrente_fmu[idx] - corrente_ref_na_grade[idx]) / escala_i * 100.0
        print(f"{t_fmu[idx]:8.3f} {omega_ref_na_grade[idx]:12.5f} {omega_fmu[idx]:12.5f} "
              f"{ew:11.2e} {corrente_ref_na_grade[idx]:10.5f} {corrente_fmu[idx]:10.5f} {ei:11.2e}")

    print("-" * 78)
    print(f"Erro relativo maximo em omega   : {erro_omega*100:.3e} %")
    print(f"Erro relativo maximo em corrente: {erro_corrente*100:.3e} %")
    print("(valores da ordem de 1e-9 % ou menores refletem apenas arredondamento")
    print(" de ponto flutuante — o FMU em C e a referencia Python executam,")
    print(" nesse regime, o mesmo algoritmo RK4 sobre a mesma entrada em degraus.)")
    print()

    limite = 0.01  # 1 %
    ok_omega = erro_omega < limite
    ok_corrente = erro_corrente < limite

    if ok_omega and ok_corrente:
        print("RESULTADO: OK — erro relativo maximo abaixo de 1 % em ambas as saidas.")
        print("O FMU em C reproduz fielmente as equacoes e os parametros de plant.py.")
        return 0

    print("RESULTADO: FALHA — erro relativo maximo acima de 1 %.")
    print("Verifique MICRO_DT em plant_fmu.c e o DT_REFERENCIA deste script.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
