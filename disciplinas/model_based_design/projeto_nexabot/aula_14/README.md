# Aula 14 — SIL: verificando que o código gerado é o modelo

Unidade 4, Aula 14: Software-in-the-Loop. Compila o C da Aula 13 como
biblioteca compartilhada (`nexabot/sil.py`) e mede — não assume — a
equivalência numérica entre `DiscretePID` (Python) e o código gerado.

## Como rodar

```bash
cd projeto_nexabot
.venv/bin/python aula_14/01_compila_sil.py
.venv/bin/python aula_14/02_equivalencia.py
.venv/bin/python aula_14/03_regressao.py
.venv/bin/python aula_14/04_ci.py
.venv/bin/python aula_14/05_desafio.py
```

## Scripts

| Script | O que mostra | Saída esperada (resumo) |
|---|---|---|
| `01_compila_sil.py` | Mecânica da ponte SIL: `gcc` -> `.so` -> `ctypes.Structure`/`argtypes`/`restype`, na mão e depois via `SILController` | Mesma sequência de tensões pelas duas vias |
| `02_equivalencia.py` (ponto central) | `compare_model_vs_code` sobre 6000 amostras com saturação e anti-windup ativos | `double`: erro máximo `0.000e+00` V; `Q16.16`: erro da ordem de `1e-2`–`1e-1` V |
| `03_regressao.py` | Suíte de regressão com `hypothesis`: 25 combinações aleatórias de ganhos | `REGRESSÃO OK`, todas as linhas da tabela `OK` |
| `04_ci.py` | Carrega e valida `.github/workflows/mbd-ci.yml` (pytest, equivalência SIL, matriz de rastreabilidade, gcc, gatilhos) | Todas as checagens `OK` |
| `05_desafio.py` | Injeta um bug clássico de sinal trocado no anti-windup e mostra que ele só aparece depois de saturar e tentar dessaturar | Erro máximo de dezenas de volts com o bug; `0.000e+00` sem ele |

## Por que o erro do `double` é exatamente zero (não só "pequeno")

O C gerado reproduz a mesma sequência de operações de ponto flutuante do
`DiscretePID.step` (mesma ordem de soma/multiplicação), então IEEE-754
produz bit a bit o mesmo resultado — não "aproximadamente igual", igual.
Se `02_equivalencia.py` ou `03_regressao.py` um dia acusarem erro acima de
`~1e-9` V na variante double, há um bug real de tradução modelo -> C em
`nexabot/codegen/templates/pid_controller.c.j2` (ver `05_desafio.py` para
um exemplo construído de propósito).

## Pré-requisitos

`gcc` no PATH (todos os scripts desta aula compilam C via `nexabot.sil`) e
`pyyaml` (só `04_ci.py`, para carregar o YAML do workflow).
