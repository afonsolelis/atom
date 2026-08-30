# Aula 09 — Requisitos formais do NexaBot

Unidade 3 (verificação formal e testes baseados em modelos). Esta aula não
verifica nada ainda: ela traduz os requisitos de segurança do supervisor
(`nexabot/supervisor.py`) — hoje só em texto — em predicados Python
verificáveis (`nexabot/requisitos.py`), preparando o terreno para o model
checker da Aula 10.

## Comandos exatos

```bash
cd projeto_nexabot
.venv/bin/python aula_09/01_requisitos.py
.venv/bin/python aula_09/02_do_texto_a_propriedade.py
.venv/bin/python aula_09/03_desafio.py
```

## Saída esperada (resumo)

- **01_requisitos.py**: tabela ASCII com os 6 requisitos REQ-SAFE-001..006,
  classificados por tipo — 2 invariantes, 1 alcançabilidade, 1 segurança,
  1 vivacidade, 1 temporizado.
- **02_do_texto_a_propriedade.py**: mostra o texto ambíguo de REQ-SAFE-005,
  uma primeira formalização ingênua, o CONTRAEXEMPLO REAL que o model
  checker encontra contra ela (obstáculo removido + partida, mas com falha
  de encoder simultânea — o texto original não previa isso), e a
  formalização corrigida (0 violações).
- **03_desafio.py**: pede para formalizar um sétimo requisito ("nunca freio
  e torque ao mesmo tempo"); com a solução de referência, 0 violações em
  768 transições.

## Arquivos-fonte usados

- `nexabot/supervisor.py` — a máquina de estados.
- `nexabot/requisitos.py` — os predicados formais.
