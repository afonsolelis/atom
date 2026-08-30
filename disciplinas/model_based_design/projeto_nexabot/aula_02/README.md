# Aula 2 — Da equação diferencial ao espaço de estados

Tema: passar das EDOs do motor CC do NexaBot para as matrizes (A, B, C, D),
confirmar a equivalência com a função de transferência e identificar os seis
parâmetros físicos (R, L, Ke, Kt, J, b) a partir de um ensaio de degrau —
o "de onde vêm os números de `params.py`" da disciplina.

## Comandos (execute nesta ordem, a partir de `projeto_nexabot/`)

```bash
.venv/bin/python aula_02/01_sympy_derivacao.py
.venv/bin/python aula_02/02_estado_vs_transferencia.py
.venv/bin/python aula_02/03_identificacao.py
.venv/bin/python aula_02/04_validacao.py
.venv/bin/python aula_02/05_desafio.py
```

## O que aparece na tela

| Script | O que mostra | Saída esperada (resumo) |
|---|---|---|
| `01_sympy_derivacao.py` | Deriva simbolicamente (sympy) as duas EDOs do motor CC, isola di/dt e dw/dt, monta x'=Ax+Bu, y=Cx+Du e substitui os números de `PARAMS`, comparando com o valor "a mão" já verificado e com `nexabot.plant.state_space_matrices`. | A = [[-342.86, -12.86], [180.0, -0.32]], B = [[285.71],[0]], C=[0 1], D=[0]; diferença máxima entre as três fontes ≈ 1,4e-4 (limitada pela precisão de 3 casas do valor "a mão") e ≈ 1,8e-15 contra `plant.py`. Tudo em verde, `Todas as matrizes conferem`. |
| `02_estado_vs_transferencia.py` | Converte a state-space para função de transferência com `control.tf(...)` e compara polos/ganho DC com `nexabot.plant.transfer_function`; roda um degrau de 12 V nos dois modelos (`control.step_response` x `plant.simulate`) e compara as curvas. Salva PNG. | Polos idênticos (-7,2151 e -335,9620 rad/s) e ganho DC idêntico (21,2164 rad/(s.V)) nas duas formas, diferença ≈ 0 e ≈ 3,55e-15. Erro máximo entre as duas simulações: 8,02e-6 rad/s (0,0000% do pico de 254 rad/s) — só erro numérico de integração. |
| `03_identificacao.py` | Gera um ensaio de degrau sintético com ruído de ADC e quantização de encoder (`gerar_ensaio_degrau`), salva `data/ensaio_degrau.csv`, ajusta os 5 parâmetros livres por mínimos quadrados não lineares e compara com a verdade numa tabela colorida (verde < 2%, vermelho >= 2%). Salva PNG. | 4001 amostras a 5 kHz; ajuste converge em 11 avaliações; erros: R +0,028%, L -0,063%, Ke/Kt +0,010%, J +0,025%, b -0,178% — todos em verde, muito abaixo do limiar de 2%. |
| `04_validacao.py` | Reproduz a identificação do script 03, valida o modelo em um ensaio held-out (8 V, seed diferente) via `fit_percentual`, e repete a identificação amostrando a Ts=5 ms (o do controlador embarcado) para mostrar o efeito de subamostrar a constante de tempo elétrica. Salva 2 PNGs. | fit% no held-out: velocidade 86,55%, corrente 98,04%. Ao amostrar a 5 ms em vez de 0,2 ms, o erro em L salta de -0,063% para +6,619% (~105x pior) e em b de -0,178% para -4,422% — ambos cruzam para vermelho — enquanto o fit% de velocidade quase não muda (86,55% → 86,52%): o problema fica escondido num indicador agregado. |
| `05_desafio.py` | Esqueleto do desafio: decidir (True/False) se uma identificação com bancada mais barulhenta (`ruido_i_std=5.0` A, ~167x o padrão) ainda é confiável, comparando o erro de cada parâmetro contra um limiar de 10%. Roda mesmo sem estar implementado, avisando o que falta. | Sem implementação: aviso amarelo `AINDA NÃO IMPLEMENTADO` + tabela de faixas esperadas. Implementado corretamente (com `ruido_i_std=5.0`, `seed=42`, `limiar_pct=10.0`): `estim.sucesso=True`, erros R +2,194%, L -11,341%, Ke/Kt +0,628%, J -1,901%, b -12,898% — L e b acima do limiar, logo o retorno esperado é `False`. |

## Observações

- Todos os scripts usam `.venv/bin/python` do diretório `projeto_nexabot/` e
  importam `nexabot.params`, `nexabot.plant`, `nexabot.controllers`,
  `nexabot.identificacao` e `nexabot.viz` — nenhum arquivo fora de
  `aula_02/` é modificado.
- `03_identificacao.py` sobrescreve `data/ensaio_degrau.csv` a cada
  execução — é o comportamento esperado (o CSV é o produto do ensaio mais
  recente, não um artefato versionado).
- Os gráficos ASCII (`nexabot.viz.plot_ascii`) são a saída principal, pensada
  para gravação de tela sem depender de abrir janelas; os PNGs
  complementares (`aula02_estado_vs_transferencia.png`,
  `aula02_identificacao_ajuste.png`, `aula02_validacao_held_out.png`,
  `aula02_aliasing_ts_controlador.png`) vão para `figuras/`.
- A identificação usa mínimos quadrados NÃO lineares
  (`scipy.optimize.least_squares`) simulando a planta inteira e comparando
  com os dados medidos — não uma regressão linear por diferenças finitas,
  que amplificaria o ruído de medição ao estimar derivadas numericamente
  (ver docstring de `nexabot/identificacao.py`).
- O ponto pedagógico central da aula (scripts 03 e 04): a bancada de
  identificação precisa amostrar bem mais rápido (5 kHz) do que o
  controlador embarcado roda (200 Hz), porque a constante de tempo elétrica
  do motor (~2,9 ms) só fica visível — e portanto identificável — se a
  amostragem for significativamente mais rápida do que ela.
