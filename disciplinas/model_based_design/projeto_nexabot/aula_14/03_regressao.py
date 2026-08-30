#!/usr/bin/env python3
"""Aula 14 — Script 3/5: suíte de regressão SIL x modelo.

O que este script faz
----------------------
Generaliza a checagem pontual de `02_equivalencia.py` em uma suíte de
regressão: usa `hypothesis` para gerar dezenas de combinações aleatórias de
ganhos (Kp, Ki, Kd, tau_f) e de sequências de referência/medição, e falha
(sai com código != 0) se o erro máximo entre `DiscretePID` e `SILController`
ultrapassar a tolerância — para a variante double, praticamente zero; para
Q16.16, uma tolerância física (fração da tensão máxima do driver).

Esta é a suíte que `04_ci.py`/`.github/workflows/mbd-ci.yml` rodam a cada
alteração no repositório: qualquer mudança futura em `nexabot/controllers.py`
ou em `nexabot/codegen/` que quebre a equivalência é pega automaticamente,
sem depender de alguém lembrar de testar manualmente.

Como rodar
----------
    .venv/bin/python aula_14/03_regressao.py

Saída esperada (resumo)
------------------------
Uma tabela com um caso por combinação de ganhos testada e, ao final,
"REGRESSÃO OK" ou a indicação de qual caso falhou.

Rastreabilidade: evidência de TESTE (regressão, sob ganhos variados) de
REQ-CTRL-001, REQ-CTRL-002, REQ-CTRL-003 e REQ-CODEGEN-001 — ver também
`aula_14/02_equivalencia.py` para o caso pontual correspondente.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import numpy as np  # noqa: E402
from hypothesis import HealthCheck, given, settings  # noqa: E402
from hypothesis import strategies as st  # noqa: E402

from nexabot.sil import compare_model_vs_code  # noqa: E402

TOLERANCIA_DOUBLE_V = 1.0e-9   # bem acima do épsilon de máquina, folga para libm
TOLERANCIA_FIXED_V = 0.5       # tolerância física: <~2% de 24 V, ver Aula 13 script 3

resultados: list[dict] = []


def _sequencia(rng: np.random.Generator, n: int = 400) -> tuple[np.ndarray, np.ndarray]:
    r = rng.uniform(-150.0, 150.0, size=n)
    r = np.repeat(r[: n // 20], 20)[:n]  # patamares, não ruído puro -- mais realista
    y = r + rng.normal(0.0, 5.0, size=n)
    return r, y


@given(
    Kp=st.floats(min_value=0.1, max_value=10.0, allow_nan=False),
    Ki=st.floats(min_value=0.0, max_value=200.0, allow_nan=False),
    Kd=st.floats(min_value=0.0, max_value=0.5, allow_nan=False),
    tau_f=st.floats(min_value=0.002, max_value=0.05, allow_nan=False),
    seed=st.integers(min_value=0, max_value=2**31 - 1),
)
@settings(max_examples=25, deadline=None, suppress_health_check=[HealthCheck.too_slow])
def testar_equivalencia_para_ganhos(Kp: float, Ki: float, Kd: float, tau_f: float, seed: int) -> None:
    rng = np.random.default_rng(seed)
    r, y = _sequencia(rng)

    rep_double = compare_model_vs_code(r, y, Kp=Kp, Ki=Ki, Kd=Kd, tau_f=tau_f)
    rep_fixed = compare_model_vs_code(r, y, Kp=Kp, Ki=Ki, Kd=Kd, tau_f=tau_f, fixed_point=True)

    ok_double = rep_double.erro_maximo_abs <= TOLERANCIA_DOUBLE_V
    ok_fixed = rep_fixed.erro_maximo_abs <= TOLERANCIA_FIXED_V

    resultados.append({
        "Kp": Kp, "Ki": Ki, "Kd": Kd, "tau_f": tau_f,
        "erro_double": rep_double.erro_maximo_abs, "ok_double": ok_double,
        "erro_fixed": rep_fixed.erro_maximo_abs, "ok_fixed": ok_fixed,
    })

    assert ok_double, (
        f"REGRESSÃO (double): erro {rep_double.erro_maximo_abs:.3e} V > "
        f"tolerância {TOLERANCIA_DOUBLE_V:.3e} V para Kp={Kp}, Ki={Ki}, Kd={Kd}, tau_f={tau_f}"
    )
    assert ok_fixed, (
        f"REGRESSÃO (Q16.16): erro {rep_fixed.erro_maximo_abs:.3e} V > "
        f"tolerância {TOLERANCIA_FIXED_V:.3e} V para Kp={Kp}, Ki={Ki}, Kd={Kd}, tau_f={tau_f}"
    )


def linha(char: str = "-", n: int = 90) -> str:
    return char * n


def main() -> None:
    print(linha("="))
    print("Aula 14 — Suíte de regressão: equivalência SIL x modelo sob ganhos aleatórios")
    print(linha("="))
    print(f"\nTolerâncias: double <= {TOLERANCIA_DOUBLE_V:.1e} V, Q16.16 <= {TOLERANCIA_FIXED_V:.1e} V")
    print("Gerando casos com hypothesis (max_examples=25)...\n")

    falhou = False
    try:
        testar_equivalencia_para_ganhos()
    except AssertionError as exc:
        falhou = True
        print(f"FALHA: {exc}")

    header = f"{'#':>3} | {'Kp':>6} | {'Ki':>7} | {'Kd':>6} | {'tau_f':>7} | {'erro double [V]':>15} | {'erro Q16.16 [V]':>15} | status"
    print(header)
    print(linha("-", len(header)))
    for i, r in enumerate(resultados):
        status = "OK" if (r["ok_double"] and r["ok_fixed"]) else "FALHOU"
        print(f"{i:>3} | {r['Kp']:>6.2f} | {r['Ki']:>7.2f} | {r['Kd']:>6.3f} | {r['tau_f']:>7.4f} | "
              f"{r['erro_double']:>15.3e} | {r['erro_fixed']:>15.3e} | {status}")

    n_casos = len(resultados)
    n_falhas = sum(1 for r in resultados if not (r["ok_double"] and r["ok_fixed"]))
    print("\n" + linha("="))
    print(f"Casos executados: {n_casos} | falhas: {n_falhas}")

    if falhou or n_falhas:
        print("REGRESSÃO FALHOU")
        raise SystemExit(1)
    print("REGRESSÃO OK — nenhuma combinação de ganhos testada quebrou a equivalência.")


if __name__ == "__main__":
    main()
