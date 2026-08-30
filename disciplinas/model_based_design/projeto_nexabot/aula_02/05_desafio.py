#!/usr/bin/env python3
"""Aula 2 — Script 5/5: DESAFIO — a identificação continua confiável com mais ruído?

Enunciado
---------
Os scripts 03 e 04 mostraram que a identificação por mínimos quadrados não
lineares é bem robusta ao ruído "de fábrica" da bancada (`ruido_i_std=0.03`
A, o padrão de `gerar_ensaio_degrau`). Mas toda bancada real tem um limite:
em algum nível de ruído do sensor de corrente, o ajuste ainda "converge"
(`least_squares` devolve `sucesso=True`), só que os parâmetros que ele
devolve deixam de ser confiáveis.

Complete `avaliar_confiabilidade_identificacao` para:

1. Gerar um ensaio de degrau com `nexabot.identificacao.gerar_ensaio_degrau`,
   usando `ruido_i_std` e `seed` como parâmetros (mantenha os demais
   argumentos no padrão da função).
2. Rodar `nexabot.identificacao.ajustar_minimos_quadrados` nesse ensaio.
3. Comparar com a verdade usando `nexabot.identificacao.comparar_com_verdade`.
4. Decidir se a identificação é CONFIÁVEL: verdadeiro se e somente se o
   ajuste convergiu (`estim.sucesso`) E o erro percentual absoluto de TODOS
   os 6 parâmetros (R, L, Ke, Kt, J, b) for menor que `limiar_pct`.
5. Devolver esse booleano. Devolva `None` enquanto não estiver implementada
   (comportamento atual).

Critério de aceitação
----------------------
Rodando este script (sem argumentos) com os valores padrão de teste
`ruido_i_std=5.0` A, `seed=42` e `limiar_pct=10.0` — um ruído de corrente
~167x maior que o padrão da bancada (5,0 A contra 0,03 A, quase metade da
corrente de pico do ensaio) —, uma implementação de referência obtém:

- `estim.sucesso` = `True` (o otimizador converge mesmo com ruído pesado);
- erro percentual absoluto por parâmetro entre ~0,6% (Ke/Kt, os mais bem
  condicionados) e ~13% (b, o pior);
- especificamente, R ~2,2%, L ~11,3%, J ~1,9%, b ~12,9% de erro absoluto;
- logo `avaliar_confiabilidade_identificacao(...)` deve devolver **`False`**
  (b e L ultrapassam o limiar de 10%), mesmo com o ajuste tendo "convergido".

Esse é o ponto do desafio: `sucesso=True` do otimizador NÃO é o mesmo que
"parâmetros confiáveis" — é preciso checar o erro de cada parâmetro contra
um limiar de engenharia antes de usar o modelo identificado em produção.

Como rodar
----------
    .venv/bin/python aula_02/05_desafio.py
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nexabot import viz  # noqa: E402
from nexabot.identificacao import (  # noqa: E402
    ajustar_minimos_quadrados,
    comparar_com_verdade,
    gerar_ensaio_degrau,
)
from nexabot.params import PARAMS, NexaBotParams  # noqa: E402


def avaliar_confiabilidade_identificacao(
    ruido_i_std: float,
    seed: int,
    limiar_pct: float = 10.0,
    p: NexaBotParams = PARAMS,
) -> bool | None:
    """TODO(estudante): implemente a checagem de confiabilidade da identificação.

    Veja o enunciado no docstring do módulo para o passo a passo. Devolva
    `None` enquanto não estiver implementado (comportamento atual) ou o
    booleano de confiabilidade quando a implementação estiver pronta.
    """
    # TODO: 1. gere o ensaio com gerar_ensaio_degrau(ruido_i_std=ruido_i_std, seed=seed, p=p)
    # TODO: 2. ajuste os parâmetros com ajustar_minimos_quadrados(ensaio, p_referencia=p)
    # TODO: 3. compare com a verdade usando comparar_com_verdade(estim, p=p)
    # TODO: 4. decida: sucesso do ajuste E todos os |erro_pct| < limiar_pct
    # TODO: 5. devolva o booleano
    return None


def main() -> int:
    print(viz.titulo("NexaBot — Aula 2 — DESAFIO: a identificação continua confiável com mais ruído?"))
    print(__doc__.split("Como rodar")[0].strip())
    print()

    ruido_i_std = 5.0
    seed = 42
    limiar_pct = 10.0
    print(f"Executando com ruido_i_std = {ruido_i_std} A, seed = {seed}, "
          f"limiar_pct = {limiar_pct}%...\n")

    resultado = avaliar_confiabilidade_identificacao(ruido_i_std, seed, limiar_pct)

    if resultado is None:
        print(viz.amarelo(viz.negrito(
            "AINDA NÃO IMPLEMENTADO: avaliar_confiabilidade_identificacao() devolveu None.")))
        print("Implemente os 5 passos marcados com TODO na função acima.")
        print("\nCritério de aceitação (com ruido_i_std=5.0 A, seed=42, limiar_pct=10.0):")
        viz.tabela(
            ["grandeza", "valor/faixa esperada"],
            [
                ["estim.sucesso", "True"],
                ["erro %  (R)", "~2,2 %"],
                ["erro %  (L)", "~11,3 %  (acima do limiar)"],
                ["erro %  (Ke, Kt)", "~0,6 %"],
                ["erro %  (J)", "~1,9 %"],
                ["erro %  (b)", "~12,9 %  (acima do limiar, o pior caso)"],
                ["retorno esperado", "False (b e L excedem 10%)"],
            ],
        )
        return 0

    # -- mostra a decisão do estudante lado a lado com o diagnóstico completo -
    ensaio = gerar_ensaio_degrau(ruido_i_std=ruido_i_std, seed=seed)
    estim = ajustar_minimos_quadrados(ensaio)
    linhas_comparacao = comparar_com_verdade(estim)

    linhas_tabela = []
    algum_acima_limiar = False
    for l in linhas_comparacao:
        erro_abs = abs(l["erro_pct"])
        acima = erro_abs >= limiar_pct
        algum_acima_limiar |= acima
        erro_fmt = f"{l['erro_pct']:+.3f} %"
        linhas_tabela.append([
            l["parametro"], erro_fmt, viz.vermelho("acima") if acima else viz.verde("dentro"),
        ])
    viz.tabela(
        ["parâmetro", "erro %", f"vs. limiar de {limiar_pct:g}%"],
        linhas_tabela,
        titulo_tabela=f"Diagnóstico completo (ruido_i_std={ruido_i_std} A, seed={seed})",
    )

    print(f"\nestim.sucesso (otimizador convergiu) = {estim.sucesso}")
    resultado_esperado = estim.sucesso and not algum_acima_limiar
    linhas_resultado = [
        ["avaliar_confiabilidade_identificacao(...)", str(resultado)],
        ["resultado esperado pela implementação de referência", str(resultado_esperado)],
    ]
    viz.tabela(["item", "valor"], linhas_resultado, titulo_tabela="Resultado do estudante")

    if resultado == resultado_esperado:
        print(viz.verde(viz.negrito(
            "\nResultado bate com a implementação de referência — desafio resolvido.")))
        return 0
    else:
        print(viz.vermelho(viz.negrito(
            "\nResultado NÃO bate com a implementação de referência — revise a lógica.")))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
