# Aula 1 — O que é um sistema ciberfísico e por que MBD

Tema: apresentação do NexaBot (AGV industrial de armazém) como fio condutor
da disciplina e primeiro contato com a planta em malha aberta.

## Comandos (execute nesta ordem, a partir de `projeto_nexabot/`)

```bash
.venv/bin/python aula_01/01_ambiente.py
.venv/bin/python aula_01/02_primeira_simulacao.py
.venv/bin/python aula_01/03_malha_aberta_falha.py
.venv/bin/python aula_01/04_v_model.py
.venv/bin/python aula_01/05_desafio.py
```

## O que aparece na tela

| Script | O que mostra | Saída esperada (resumo) |
|---|---|---|
| `01_ambiente.py` | Relatório verde/vermelho de todas as bibliotecas (numpy, scipy, control, sympy, matplotlib, jinja2, hypothesis, pytest, coverage, fmpy, pyserial), ferramentas externas (gcc) e conferência dos números de `params.py`. | Três tabelas, tudo `OK` em verde, e a linha final `AMBIENTE PRONTO`. Código de saída 0. |
| `02_primeira_simulacao.py` | Degrau de 12 V no motor do NexaBot em malha aberta: gráfico ASCII de `w(t)` e `i(t)`, tabela com ganho DC, velocidade/corrente de regime e as duas aproximações desacopladas de constante de tempo. Salva PNG. | Velocidade de regime ≈ 254,6 rad/s (0,6365 m/s), corrente de pico ≈ 9,41 A, L/R ≈ 2,92 ms e JR/(KtKe) ≈ 148 ms. Os valores modais exatos, calculados na Aula 3, são 2,9765 ms e 138,5982 ms. |
| `03_malha_aberta_falha.py` | Parte já em regime a 1,0 m/s e aplica uma rampa de torque de carga (palete sendo carregado); mostra o erro de velocidade crescendo sem que o controlador perceba. | Erro de velocidade cresce monotonicamente até ≈ 24,9% ao final dos 2 s — nenhuma correção acontece (malha aberta). |
| `04_v_model.py` | Desenha o V-Model de MBD em ASCII com as 16 aulas da disciplina mapeadas em cada degrau (requisitos → arquitetura → controle → discretização → código → SIL → co-simulação → verificação formal → MBT → HIL). | Diagrama em V + tabela de rastreabilidade degrau→aulas com 10 linhas. |
| `05_desafio.py` | Esqueleto do desafio: orçamento de energia de uma missão do NexaBot (18 V, 50 m). Roda mesmo sem estar implementado, avisando o que falta. | Sem implementação: aviso amarelo `AINDA NÃO IMPLEMENTADO` + tabela de faixas esperadas. Implementado corretamente: `v_regime_m_s≈0,95`, `tempo_s≈52,4`, `energia_j≈651`, dentro das faixas 0,90–1,00 m/s / 50–56 s / 550–750 J. |

## Observações

- Todos os scripts usam `.venv/bin/python` do diretório `projeto_nexabot/` e
  importam `nexabot.params`, `nexabot.plant` e `nexabot.viz` — nenhum
  arquivo fora de `aula_01/` é modificado.
- Os gráficos ASCII (`nexabot.viz.plot_ascii`) são a saída principal, pensada
  para gravação de tela sem depender de abrir janelas; os PNGs complementares
  vão para `figuras/`.
