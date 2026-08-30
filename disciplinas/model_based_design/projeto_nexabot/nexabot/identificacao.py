"""Identificação de parâmetros do NexaBot a partir de dados de ensaio (Aula 2).

Ideia central da aula: o modelo não vem de datasheet, vem de dados. Este
módulo primeiro **gera** um ensaio de degrau sintético, mas realista, do
motor real do NexaBot (integrando a planta verdadeira de `params.py` com
Runge-Kutta) e adicionando os dois efeitos que qualquer bancada real teria:

* ruído de medição gaussiano no sensor de corrente (shunt + ADC de 12 bits);
* quantização de encoder incremental na medida de velocidade angular
  (contagem de pulsos por período de amostragem).

Depois, um ajuste por **mínimos quadrados não lineares** (`scipy.optimize.
least_squares`, algoritmo *trust region reflective*) recupera os cinco
parâmetros físicos (R, L, Ke=Kt, J, b) a partir unicamente de V(t), i(t)
medido e w(t) medido — exatamente os sinais disponíveis em uma bancada real
com sensor de corrente e encoder.

Por que mínimos quadrados NÃO lineares no domínio do tempo, e não uma
regressão linear ponto a ponto sobre as EDOs? Porque estimar di/dt e dw/dt
por diferenças a partir de sinal com ruído amplifica o ruído (o problema
clássico de derivar numericamente um sinal medido) e, além disso, a entrada
degrau tem pouca excitação persistente para separar 5 parâmetros por uma
regressão ponto a ponto (matriz mal-condicionada). A alternativa robusta —
e a usada de fato em identificação de sistemas — é simular o modelo físico
completo (mesmo integrador RK4 de `plant.simulate`) para um candidato de
parâmetros e ajustar esses parâmetros para que a trajetória simulada bata
com a trajetória medida inteira, usando toda a forma da resposta transitória
em vez de amostra a amostra. Ke e Kt são impostos iguais (mesma constante em
unidades SI, fato de motor CC de ímã permanente) para reduzir de 6 para 5 o
número de incógnitas, exatamente como em `params.py`.

Rastreabilidade: REQ-PLANT-001 (o modelo de planta é validado por dados).
"""

from __future__ import annotations

import csv
import os
from dataclasses import dataclass

import numpy as np
from scipy.optimize import least_squares

from .params import PARAMS, NexaBotParams

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
CSV_PADRAO = os.path.join(DATA_DIR, "ensaio_degrau.csv")


# --------------------------------------------------------------------------
# Geração do ensaio sintético
# --------------------------------------------------------------------------

@dataclass
class EnsaioDegrau:
    """Dados de um ensaio de degrau de tensão no motor do NexaBot."""

    t: np.ndarray          # tempo [s]
    V: np.ndarray          # tensão aplicada [V] (entrada, sem ruído: é comandada)
    i_verdadeiro: np.ndarray   # corrente verdadeira simulada [A] (para referência/depuração)
    w_verdadeiro: np.ndarray   # velocidade angular verdadeira simulada [rad/s]
    i_medido: np.ndarray   # corrente medida (ruído de ADC) [A]
    w_medido: np.ndarray   # velocidade angular medida (quantização de encoder) [rad/s]

    def salvar_csv(self, caminho: str = CSV_PADRAO) -> str:
        """Salva o ensaio em CSV com cabeçalho, uma linha por amostra."""
        os.makedirs(os.path.dirname(caminho), exist_ok=True)
        with open(caminho, "w", newline="") as f:
            escritor = csv.writer(f)
            escritor.writerow(["t_s", "V_volts", "i_medido_A", "w_medido_rad_s",
                                "i_verdadeiro_A", "w_verdadeiro_rad_s"])
            for k in range(len(self.t)):
                escritor.writerow([
                    f"{self.t[k]:.6f}", f"{self.V[k]:.6f}",
                    f"{self.i_medido[k]:.6f}", f"{self.w_medido[k]:.6f}",
                    f"{self.i_verdadeiro[k]:.6f}", f"{self.w_verdadeiro[k]:.6f}",
                ])
        return caminho


def carregar_csv(caminho: str = CSV_PADRAO) -> EnsaioDegrau:
    """Recarrega um ensaio salvo anteriormente por `salvar_csv`."""
    dados = np.genfromtxt(caminho, delimiter=",", names=True)
    return EnsaioDegrau(
        t=dados["t_s"], V=dados["V_volts"],
        i_medido=dados["i_medido_A"], w_medido=dados["w_medido_rad_s"],
        i_verdadeiro=dados["i_verdadeiro_A"], w_verdadeiro=dados["w_verdadeiro_rad_s"],
    )


def gerar_ensaio_degrau(
    amplitude_v: float = 12.0,
    t_end: float = 0.8,
    dt_sim: float = 2.0e-5,
    ts_amostragem: float = 2.0e-4,
    ruido_i_std: float = 0.03,
    ruido_adc_bits: int = 12,
    faixa_adc_a: float = 15.0,
    contagens_por_volta: int = 2048,
    seed: int = 42,
    p: NexaBotParams = PARAMS,
) -> EnsaioDegrau:
    """Gera um ensaio de degrau sintético e realista do motor do NexaBot.

    Simula a planta *verdadeira* (parâmetros de `params.py`) em passo fino
    (`dt_sim`) e reamostra na taxa de aquisição da BANCADA DE IDENTIFICAÇÃO
    (`ts_amostragem`, 5 kHz por padrão), aplicando:

    - corrente: ruído gaussiano de medição + quantização de um ADC de
      `ruido_adc_bits` bits cobrindo `+-faixa_adc_a` ampères (sensor shunt);
    - velocidade: quantização de encoder incremental de `contagens_por_volta`
      pulsos por volta do EIXO DO MOTOR, com velocidade estimada por contagem
      de pulsos no intervalo `ts_amostragem` (método real de firmware).

    Nota pedagógica importante: a bancada de identificação amostra bem mais
    rápido (5 kHz, `ts_amostragem`) do que o laço de controle embarcado
    (200 Hz, `PARAMS.Ts`). Isso não é um detalhe incidental — é necessário:
    a constante de tempo elétrica (~2,9 ms) some sob amostragem de 5 ms
    (viraria alias), então R e L simplesmente não são identificáveis de um
    ensaio amostrado no `Ts` de controle. Isso é mostrado explicitamente
    em `aula_02/04_validacao.py`.
    """
    rng = np.random.default_rng(seed)

    def u_of_t(t):
        return amplitude_v if t >= 0 else 0.0

    from .plant import simulate

    t_fino, X = simulate(u_of_t, t_end=t_end, dt=dt_sim, p=p)
    i_fino = X[:, 0]
    w_fino = X[:, 1]

    # --- reamostra na taxa do controlador embarcado ----------------------
    passo = max(1, int(round(ts_amostragem / dt_sim)))
    idx = np.arange(0, len(t_fino), passo)
    t = t_fino[idx]
    V = np.array([u_of_t(tk) for tk in t])
    i_verdadeiro = i_fino[idx]
    w_verdadeiro = w_fino[idx]

    # --- sensor de corrente: ADC de N bits + ruído gaussiano --------------
    resolucao_adc = 2 * faixa_adc_a / (2 ** ruido_adc_bits)
    i_ruidoso = i_verdadeiro + rng.normal(0.0, ruido_i_std, size=i_verdadeiro.shape)
    i_medido = np.round(i_ruidoso / resolucao_adc) * resolucao_adc

    # --- sensor de velocidade: encoder incremental ------------------------
    # posição angular verdadeira (integral fina de w) convertida em contagens,
    # depois velocidade = delta_contagens / Ts (é assim que o firmware mede).
    theta_fino = np.concatenate(([0.0], np.cumsum(0.5 * (w_fino[1:] + w_fino[:-1]) * dt_sim)))
    contagens_por_rad = contagens_por_volta / (2.0 * np.pi)
    contagens_fino = np.round(theta_fino * contagens_por_rad).astype(np.int64)
    contagens = contagens_fino[idx]
    w_medido = np.empty_like(w_verdadeiro)
    w_medido[0] = w_verdadeiro[0]
    dt_amostras = np.diff(t, prepend=t[0] - ts_amostragem)
    dt_amostras[0] = ts_amostragem
    w_medido[1:] = np.diff(contagens) / contagens_por_rad / dt_amostras[1:]
    w_medido[0] = 0.0

    return EnsaioDegrau(t=t, V=V, i_verdadeiro=i_verdadeiro, w_verdadeiro=w_verdadeiro,
                         i_medido=i_medido, w_medido=w_medido)


# --------------------------------------------------------------------------
# Ajuste por mínimos quadrados
# --------------------------------------------------------------------------

@dataclass
class ParametrosIdentificados:
    R: float
    L: float
    Ke: float
    Kt: float
    J: float
    b: float
    sucesso: bool = True
    iteracoes: int = 0


# Palpite inicial deliberadamente distante da verdade (+-40 a 60%), como em
# uma bancada real onde só se conhece a ordem de grandeza (datasheet do
# motor, sem os valores exatos). O ajuste precisa convergir mesmo assim.
PALPITE_INICIAL_FATOR = {"R": 1.4, "L": 1.6, "Ke": 0.65, "J": 1.55, "b": 0.55}


def ajustar_minimos_quadrados(ensaio: EnsaioDegrau, ts: float | None = None,
                               p_referencia: NexaBotParams = PARAMS) -> ParametrosIdentificados:
    """Recupera (R, L, Ke=Kt, J, b) por mínimos quadrados NÃO lineares.

    Simula a planta (mesmo `plant.simulate` usado no resto da disciplina)
    para um candidato de parâmetros e minimiza a soma dos quadrados dos
    resíduos entre a trajetória simulada e a medida — em corrente e em
    velocidade simultaneamente, cada uma normalizada pelo seu próprio
    desvio-padrão para que as duas grandezas pesem de forma comparável no
    custo (corrente em ampères, velocidade em rad/s: escalas bem diferentes).

    `ts` é o passo de integração/reamostragem do ensaio; se omitido, é
    inferido da própria série temporal do ensaio.
    """
    from .plant import simulate

    if ts is None:
        ts = float(np.median(np.diff(ensaio.t)))
    amplitude = float(ensaio.V[-1])
    t_end = float(ensaio.t[-1])
    i_scale = float(np.std(ensaio.i_medido)) + 1e-9
    w_scale = float(np.std(ensaio.w_medido)) + 1e-9

    def u_of_t(t):
        return amplitude if t >= 0 else 0.0

    def residuos(theta):
        R, L, Ke, J, b = theta
        p_cand = NexaBotParams(R=R, L=L, Ke=Ke, Kt=Ke, J=J, b=b,
                                V_max=p_referencia.V_max, i_max=p_referencia.i_max)
        _, X = simulate(u_of_t, t_end=t_end, dt=ts, p=p_cand)
        n = min(len(X), len(ensaio.t))
        r_i = (X[:n, 0] - ensaio.i_medido[:n]) / i_scale
        r_w = (X[:n, 1] - ensaio.w_medido[:n]) / w_scale
        return np.concatenate([r_i, r_w])

    theta0 = np.array([
        p_referencia.R * PALPITE_INICIAL_FATOR["R"],
        p_referencia.L * PALPITE_INICIAL_FATOR["L"],
        p_referencia.Ke * PALPITE_INICIAL_FATOR["Ke"],
        p_referencia.J * PALPITE_INICIAL_FATOR["J"],
        p_referencia.b * PALPITE_INICIAL_FATOR["b"],
    ])

    resultado = least_squares(residuos, theta0, bounds=(1e-8, np.inf),
                               method="trf", xtol=1e-14, ftol=1e-14, max_nfev=2000)
    R_hat, L_hat, Ke_hat, J_hat, b_hat = resultado.x

    return ParametrosIdentificados(R=float(R_hat), L=float(L_hat), Ke=float(Ke_hat),
                                    Kt=float(Ke_hat), J=float(J_hat), b=float(b_hat),
                                    sucesso=bool(resultado.success), iteracoes=int(resultado.nfev))


def comparar_com_verdade(estim: ParametrosIdentificados, p: NexaBotParams = PARAMS) -> list[dict]:
    """Compara cada parâmetro identificado com o valor verdadeiro de `params.py`.

    Devolve uma lista de dicionários prontos para virar linhas de tabela.
    """
    campos = [
        ("R", "ohm"), ("L", "H"), ("Ke", "V.s/rad"), ("Kt", "N.m/A"),
        ("J", "kg.m^2"), ("b", "N.m.s/rad"),
    ]
    linhas = []
    for nome, unidade in campos:
        verdadeiro = getattr(p, nome)
        identificado = getattr(estim, nome)
        erro_pct = (identificado - verdadeiro) / verdadeiro * 100.0
        linhas.append({
            "parametro": nome, "unidade": unidade,
            "verdadeiro": verdadeiro, "identificado": identificado,
            "erro_pct": erro_pct,
        })
    return linhas


def fit_percentual(y_medido: np.ndarray, y_modelo: np.ndarray) -> float:
    """Métrica de ajuste estilo MATLAB `fit%` (NRMSE):

        fit% = 100 . (1 - ||y_medido - y_modelo|| / ||y_medido - media(y_medido)||)

    100% é ajuste perfeito; abaixo de 0% o modelo é pior que prever a média.
    """
    y_medido = np.asarray(y_medido, dtype=float)
    y_modelo = np.asarray(y_modelo, dtype=float)
    residuo = np.linalg.norm(y_medido - y_modelo)
    variacao = np.linalg.norm(y_medido - np.mean(y_medido))
    if variacao < 1e-12:
        return float("nan")
    return 100.0 * (1.0 - residuo / variacao)


if __name__ == "__main__":
    ensaio = gerar_ensaio_degrau()
    caminho = ensaio.salvar_csv()
    print(f"Ensaio salvo em {caminho} ({len(ensaio.t)} amostras).")
    estim = ajustar_minimos_quadrados(ensaio)
    for linha in comparar_com_verdade(estim):
        print(linha)
