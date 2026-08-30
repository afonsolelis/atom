# Matriz de rastreabilidade — Projeto NexaBot

Gerada automaticamente por `nexabot/rastreabilidade.py` a partir dos
identificadores `REQ-*` encontrados em docstrings e comentários do
projeto (varredura estática de texto, não de execução). Reflete o
estado do repositório no momento em que o script foi rodado — não é
mantida manualmente.

- Arquivos `.py` lidos: **91**
- Requisitos distintos encontrados: **14**

## Matriz requisito -> modelo -> código gerado -> teste

| Requisito | Descrição | Modelo | Código gerado | Teste | Outros |
|---|---|---|---|---|---|
| `REQ-CODEGEN-001` | equivalência numérica código gerado x modelo | `nexabot/codegen/__init__.py`<br>`nexabot/sil.py` | `nexabot/codegen/generate.py` | `aula_14/02_equivalencia.py`<br>`aula_14/03_regressao.py` | — |
| `REQ-CODEGEN-002` | rastreabilidade automática no cabeçalho do arquivo gerado | `nexabot/codegen/__init__.py`<br>`nexabot/rastreabilidade.py` | `nexabot/codegen/generate.py` | `aula_13/02_gera_codigo.py` | — |
| `REQ-CTRL-001` | rastreamento de velocidade | `nexabot/codegen/__init__.py`<br>`nexabot/controllers.py`<br>`nexabot/cosim.py`<br>`nexabot/hil.py`<br>`nexabot/sil.py` | `nexabot/codegen/derive.py`<br>`nexabot/codegen/generate.py` | `aula_14/02_equivalencia.py`<br>`aula_14/03_regressao.py` | — |
| `REQ-CTRL-002` | saturação do atuador | `nexabot/codegen/__init__.py`<br>`nexabot/controllers.py` | `nexabot/codegen/derive.py`<br>`nexabot/codegen/generate.py` | `aula_14/02_equivalencia.py`<br>`aula_14/03_regressao.py` | — |
| `REQ-CTRL-003` | anti-windup | `nexabot/codegen/__init__.py`<br>`nexabot/controllers.py` | `nexabot/codegen/derive.py`<br>`nexabot/codegen/generate.py` | `aula_14/02_equivalencia.py`<br>`aula_14/03_regressao.py` | — |
| `REQ-PLANT-001` | a planta do FMU e a mesma de plant.py | `nexabot/cosim.py`<br>`nexabot/fmu/build_fmu.py`<br>`nexabot/identificacao.py`<br>`nexabot/params.py`<br>`nexabot/plant.py` | — | `aula_16/03_desafio.py` | — |
| `REQ-PLANT-002` | limites | `nexabot/params.py` | — | `aula_16/03_desafio.py` | — |
| `REQ-SAFE-001` | Nunca há torque habilitado enquanto o sensor de obstáculo estiver ativo, em nenhum estado do supervisor. | `nexabot/requisitos.py`<br>`nexabot/supervisor.py`<br>`nexabot/timed.py` | — | `aula_09/01_requisitos.py`<br>`aula_10/02_contraexemplo.py`<br>`aula_10/03_ltl_ctl.py`<br>`aula_12/03_hypothesis.py` | — |
| `REQ-SAFE-002` | Botão de emergência pressionado implica freio acionado e torque desabilitado, imediatamente e sem exceção. | `nexabot/requisitos.py`<br>`nexabot/supervisor.py` | — | `aula_10/03_ltl_ctl.py`<br>`aula_10/04_desafio.py` | — |
| `REQ-SAFE-003` | O estado MOVENDO é alcançável a partir do estado inicial OCIOSO. | `nexabot/requisitos.py`<br>`nexabot/supervisor.py` | — | `aula_10/01_explora_estados.py` | — |
| `REQ-SAFE-004` | A partir do estado FALHA, a única saída possível é por rearme explícito (entradas.rearme = True) — nunca por decurso de tempo, novo comando do operador ou qualquer outra condição. | `nexabot/controllers.py`<br>`nexabot/hil.py`<br>`nexabot/requisitos.py`<br>`nexabot/sil.py`<br>`nexabot/supervisor.py` | — | `aula_10/03_ltl_ctl.py`<br>`aula_10/04_desafio.py`<br>`aula_15/03_watchdog_real.py` | — |
| `REQ-SAFE-005` | Uma vez removido o obstáculo, havendo comando de partida do operador e nenhuma outra condição de segurança concorrente (emergência, falha de encoder), o sistema volta a MOVENDO — o robô não fica preso em PARADO_OBSTACULO para sempre. | `nexabot/requisitos.py`<br>`nexabot/supervisor.py` | — | `aula_09/02_do_texto_a_propriedade.py`<br>`aula_10/03_ltl_ctl.py`<br>`aula_10/04_desafio.py` | — |
| `REQ-SAFE-006` | Após a detecção de obstáculo (ou emergência), o torque chega a zero em no máximo d_stop_max = 150 ms, isto é, 30 períodos de amostragem Ts = 5 ms — mesmo no pior caso de atraso de detecção e de um ciclo de atuação perdido. | `nexabot/requisitos.py`<br>`nexabot/supervisor.py`<br>`nexabot/timed.py` | — | `aula_11/01_watchdog.py`<br>`aula_11/02_pior_caso.py`<br>`aula_11/03_desafio.py` | — |
| `REQ-SAFE-007` | A velocidade linear do NexaBot não ultrapassa 1,20 m/s no domínio operacional especificado. Este requisito depende da trajetória contínua da planta e não é verificável pelo supervisor discreto isolado; permanece como lacuna explícita neste laboratório. | `nexabot/requisitos.py` | — | — | — |

**Nota de honestidade técnica:** esta matriz é evidência de rastreabilidade — um artefato que um processo de certificação (DO-178C, ISO 26262) exigiria como *insumo*. Gerá-la não certifica nada; certificação envolve auditoria independente, qualificação de ferramenta e um processo aprovado por uma autoridade/organismo certificador. Ver `aula_16/02_evidencias.py`.
