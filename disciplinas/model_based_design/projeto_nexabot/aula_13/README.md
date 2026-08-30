# Aula 13 — Do modelo ao código C (geração automática)

Unidade 4, Aula 13: como o C do controlador do NexaBot nasce do modelo
(`nexabot.controllers.DiscretePID`) por derivação simbólica, e não de
digitação manual. Ver `nexabot/codegen/` (`derive.py`, `generate.py`,
`templates/*.j2`).

## Como rodar

```bash
cd projeto_nexabot
.venv/bin/python aula_13/01_do_modelo_ao_c.py
.venv/bin/python aula_13/02_gera_codigo.py
.venv/bin/python aula_13/03_ponto_fixo.py
.venv/bin/python aula_13/04_desafio.py
```

## Scripts

| Script | O que mostra | Saída esperada (resumo) |
|---|---|---|
| `01_do_modelo_ao_c.py` | Deriva com SymPy, passo a passo, as equações de diferenças de `I[k]` e `D[k]` a partir da forma contínua do PID, por Euler para trás | Termina com `OK: derivação simbólica == contrato de DiscretePID.step` |
| `02_gera_codigo.py` | Gera `pid_controller.h`/`.c` a partir de um `DiscretePID`, imprime o C completo (com o bloco de rastreabilidade no topo) e checa determinismo do hash de parâmetros | Duas checagens `OK` de determinismo do hash |
| `03_ponto_fixo.py` | Compara a variante `double` e a variante Q16.16 do mesmo C gerado sobre a mesma sequência de entrada, tabulando o erro de quantização | `double`: erro máximo `0.000e+00` V; `Q16.16`: erro máximo da ordem de `1e-2` V |
| `04_desafio.py` | Desafio: complete o mapeamento de Tustin e descubra por que o gerador usa Euler para trás (estado extra `e[k-1]` só para a integral) | `precisa de e[k-1]? sim` (Tustin) vs `não` (Euler para trás) |

## Pré-requisitos

`gcc` no PATH (para `03_ponto_fixo.py`, que compila o C gerado via
`nexabot.sil`). Nenhum outro script desta aula compila C.
