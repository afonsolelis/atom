# Aula 12 — Testes baseados em modelo (MBT)

Fecha a Unidade 3: `nexabot/mbt.py` gera casos de teste concretos
diretamente do grafo de estados do supervisor (cobertura de estados e de
transições) e complementa com testes baseados em propriedades
(`hypothesis.stateful`). `tests/test_supervisor.py` reúne as duas fontes
mais os requisitos formais numa suíte pytest que precisa passar.

## Comandos exatos

```bash
cd projeto_nexabot
.venv/bin/python aula_12/01_gera_testes.py
.venv/bin/python aula_12/02_cobertura.py
.venv/bin/python aula_12/03_hypothesis.py
.venv/bin/python aula_12/04_desafio.py

# a suíte pytest completa
.venv/bin/python -m pytest tests/test_supervisor.py -v
```

## Saída esperada (resumo)

- **01_gera_testes.py**: 6 casos de cobertura de estados + 25 casos de
  cobertura de transições, todos gerados do modelo (nenhum escrito à mão) e
  executados com sucesso.
- **02_cobertura.py**: cobertura de modelo = 100% de estados e 100% de
  transições; cobertura de linhas (coverage.py) de `nexabot/supervisor.py`
  em 97%, `nexabot/mbt.py` em 100%, total dos módulos de verificação em
  ~89% (linhas não cobertas são principalmente ramos de erro/depuração).
- **03_hypothesis.py**: a máquina de estados do hypothesis passa sem falhas
  contra o supervisor correto; contra uma variante bugada (mesmo bug da
  Aula 10), encontra e REDUZ automaticamente o contraexemplo até o caso
  mínimo (2 passos: partir, depois obstáculo+partir simultâneos).
- **04_desafio.py**: identifica um "buraco" de cobertura de combinações de
  entrada dentro de uma mesma transição (origem, destino) e pede um caso de
  teste extra — a solução de referência passa.
- **tests/test_supervisor.py**: 43 testes, todos passando (`43 passed`).

## Arquivos-fonte usados

- `nexabot/mbt.py` — geração de testes e medição de cobertura.
- `nexabot/modelcheck.py`, `nexabot/requisitos.py`, `nexabot/timed.py`,
  `nexabot/supervisor.py` — o modelo e as propriedades sob teste.
- `tests/test_supervisor.py` — a suíte pytest final.
