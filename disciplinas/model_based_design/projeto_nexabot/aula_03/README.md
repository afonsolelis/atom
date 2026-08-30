# Aula 3 — Laplace, função de transferência e resposta em frequência

Tema: da EDO do motor CC à função de transferência G(s) = W(s)/V(s) via
Transformada de Laplace, seguida de polos/zeros, separação de escalas de
tempo, resposta em frequência (Bode, margens, banda passante) e o limite de
estabilidade — que, em malha contínua com controlador proporcional puro,
nunca chega a ser cruzado de fato.

## Comandos (execute nesta ordem, a partir de `projeto_nexabot/`)

```bash
.venv/bin/python aula_03/01_laplace_sympy.py
.venv/bin/python aula_03/02_polos_zeros.py
.venv/bin/python aula_03/03_bode.py
.venv/bin/python aula_03/04_estabilidade.py
.venv/bin/python aula_03/05_desafio.py
```

## O que aparece na tela

| Script | O que mostra | Saída esperada (resumo, números observados) |
|---|---|---|
| `01_laplace_sympy.py` | Aplica a Transformada de Laplace simbolicamente (SymPy) às duas EDOs do motor com condições iniciais nulas, resolve o sistema linear para W(s)/V(s), confere a forma canônica `Kt / (L.J.s² + (R.J+L.b).s + (R.b+Kt.Ke))` e compara os coeficientes numéricos com `nexabot.plant.transfer_function`. | Tabela de conferência algébrica toda `OK` em verde; comparação numérica com diferença `0.00e+00` em todos os coeficientes (num=0.045, s²=8.75e-7, s¹=3.0028e-4, s⁰=2.121e-3); confirma que **não há erro de digitação** no coeficiente s⁰ = R.b+Kt.Ke = 2.121e-3, e que o ganho DC bate com 21.216407 rad/(s.V). Código de saída 0. |
| `02_polos_zeros.py` | Calcula polos/zeros de G(s) (`control.poles`/`zeros` e `numpy.roots`, idênticos), converte cada polo em constante de tempo e compara com as fórmulas rápidas `PARAMS.tau_elec`/`tau_mech`; simula a resposta completa de 2ª ordem contra um modelo reduzido de 1ª ordem (polo mecânico) e tabula o erro. | Polos em **-335.9620** e **-7.2151 rad/s**; τ_elétrica exata = **2.9765 ms** (aprox. L/R = 2.9167 ms), τ_mecânica exata = **138.5982 ms** (aprox. J.R/(Kt.Ke) = 148.1481 ms); separação de escalas = **46.6x**; sem zeros finitos. Erro do modelo reduzido: máximo absoluto **5.03 rad/s** (~11.7 ms, **2.24%** do valor final), erro residual pequeno e decrescente ao longo do tempo. Três gráficos ASCII (completo, reduzido, sobreposição A/B/#). Código de saída 0. |
| `03_bode.py` | Diagrama de Bode de G(s) salvo em PNG, curva de magnitude também em ASCII (eixo X = log10(w)), margens de ganho/fase (`control.stability_margins`) e banda passante (-3 dB do ganho DC). | Margem de ganho **infinita** (fase nunca cruza -180°, sem `wg`); margem de fase **70.167°** em `wp = 140.971 rad/s`; ganho DC = **21.2164 rad/(s.V)** (26.53 dB); banda passante = **7.2099 rad/s (1.1475 Hz)**, muito próxima do polo mecânico. PNG salvo em `figuras/aula03_bode.png`. Código de saída 0. |
| `04_estabilidade.py` | Varre Kp de 0,5 a 50 em malha fechada unitária proporcional contínua (`control.feedback(Kp*G,1)`), tabulando margem de fase, sobressinal e tempo de acomodação; mostra por Routh-Hurwitz que a malha contínua nunca desestabiliza; deixa o gancho para a Aula 7 (malha discreta com ZOH desestabiliza). | Kp=0,5 → PM=83,06°, sobressinal≈0%; Kp=1 → PM=70,17°, sobressinal=3,17%; Kp=10 → PM=26,94°, sobressinal=46,20%; **Kp=50 → PM=12,22°, sobressinal=71,29%** — margem de fase decrescente mas **sempre positiva**, sobressinal crescente mas **sempre < 100%**. Dois gráficos ASCII (PM x Kp, sobressinal x Kp). Código de saída 0. |
| `05_desafio.py` | Esqueleto do desafio: encontrar por bisseção o Kp que produz um sobressinal alvo de 20% (±2 pp) na malha fechada proporcional. Roda mesmo sem estar implementado, avisando o que falta. | Sem implementação: aviso amarelo `AINDA NÃO IMPLEMENTADO` + tabela de faixas esperadas. Implementado corretamente (verificado com uma referência rodando `control` de verdade): `kp≈2,83` (raiz exata em Kp≈2,71), `overshoot_pct≈20,9%`, convergência em ~7 iterações — dentro das faixas 2,4–3,0 / 18,0–22,0% / <60 iterações. |

## Observações

- Todos os scripts usam `.venv/bin/python` do diretório `projeto_nexabot/` e
  importam `nexabot.params`, `nexabot.plant`, `nexabot.controllers` e
  `nexabot.viz` — nenhum arquivo fora de `aula_03/` é modificado.
- `02_polos_zeros.py` define uma função local `plot_ascii_comparacao` para
  sobrepor duas curvas na mesma grade ASCII (`viz.plot_ascii` só desenha uma
  curva mais uma linha de referência horizontal) — é específica deste
  script, não uma adição à biblioteca `nexabot.viz`.
- `03_bode.py` é o único script da aula que depende de um PNG para a
  visualização principal (o Bode não cabe bem em ASCII), mas ainda assim
  mostra a curva de magnitude no terminal como complemento.
- O ponto pedagógico de `04_estabilidade.py` — a malha contínua proporcional
  nunca desestabiliza, mas a malha discreta amostrada (Aula 7) sim — é
  central para entender por que discretização não é um detalhe de
  implementação, e sim algo que muda a física do problema de controle.
