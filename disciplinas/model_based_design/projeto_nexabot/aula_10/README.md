# Aula 10 — Model checking de estados explícitos

O coração pedagógico da Unidade 3: `nexabot/modelcheck.py` é um model
checker de estados explícitos escrito do zero (busca em largura, sem
nenhuma ferramenta externa) que o estudante lê linha a linha antes de ver
qualquer ferramenta de mercado.

## Comandos exatos

```bash
cd projeto_nexabot
.venv/bin/python aula_10/01_explora_estados.py
.venv/bin/python aula_10/02_contraexemplo.py
.venv/bin/python aula_10/03_ltl_ctl.py
.venv/bin/python aula_10/04_desafio.py
```

## Saída esperada (resumo)

- **01_explora_estados.py**: 6 estados alcançáveis (OCIOSO, MOVENDO,
  DESACELERANDO, PARADO_OBSTACULO, FALHA, EMERGENCIA), 768 transições
  exploradas, tempo < 5 ms, 0 violações de REQ-SAFE-001/002/004/005,
  REQ-SAFE-003 (MOVENDO alcançável) confirmado em 1 passo.
- **02_contraexemplo.py**: injeta um bug real de prioridade
  (`comando_partir` checado antes de `obstaculo` em MOVENDO) via
  `transition_com_bug`, mostra 8 violações de REQ-SAFE-001 com o
  contraexemplo completo (OCIOSO -> MOVENDO -> MOVENDO com torque ligado e
  obstáculo presente), e confirma 0 violações na versão corrigida.
- **03_ltl_ctl.py**: explica segurança (contraexemplo finito) x vivacidade
  (contraexemplo em geral infinito/cíclico); verifica REQ-SAFE-001/002/004
  (segurança) e REQ-SAFE-005 (vivacidade) sobre o mesmo modelo, e constrói
  uma variante bugada onde PARADO_OBSTACULO vira um ciclo que nunca alcança
  MOVENDO — o "lasso" clássico de um contraexemplo de vivacidade.
- **04_desafio.py**: esqueleto para o estudante injetar o próprio bug (duas
  sugestões prontas para descomentar); sem bug ativo, 0 violações.

## Arquivos-fonte usados

- `nexabot/modelcheck.py` — o model checker.
- `nexabot/requisitos.py` — os predicados verificados.
- `nexabot/supervisor.py` — o modelo sob verificação.
