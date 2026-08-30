# Aula 5 — Malha aberta vs malha fechada e álgebra de blocos

Tema: como `control.series/parallel/feedback` reproduzem a álgebra de
funções de transferência feita à mão; por que a malha fechada rejeita
distúrbio de carga e a malha aberta não; e a identidade S(s)+T(s)=1 (a
"água-cama da sensibilidade") como o limite teórico de quanto se pode
melhorar rejeição a distúrbio sem piorar a rejeição a ruído de sensor.

## Comandos (execute nesta ordem, a partir de `projeto_nexabot/`)

```bash
.venv/bin/python aula_05/01_algebra_blocos.py
.venv/bin/python aula_05/02_rejeicao_disturbio.py
.venv/bin/python aula_05/03_sensibilidade.py
.venv/bin/python aula_05/04_desafio.py
```

## O que aparece na tela

| Script | O que mostra | Saída esperada (resumo, números reais observados) |
|---|---|---|
| `01_algebra_blocos.py` | Monta um PD (Kp=6, Kd.s com Kd=0,01) por `ct.parallel`, coloca em série com a planta G(s) via `ct.series`, e fecha a malha com `ct.feedback` unitário negativo — refazendo cada passo à mão com `sympy` e comparando coeficientes de numerador/denominador. | 4 tabelas de comparação, todas `BATEU` em verde. Malha fechada resultante: polos `-428,73 ± 356,63j`, ganho DC `0,9922`, sobressinal `5,00 %`, tempo de subida `2,651 ms`, tempo de acomodação `8,404 ms`. Mensagem final verde `Todos os 4 passos de álgebra de blocos bateram`. Código de saída 0. |
| `02_rejeicao_disturbio.py` | NexaBot de cruzeiro a 1,0 m/s (400 rad/s) recebe um degrau de torque de carga de 30% do nominal em t=0,10 s; compara malha aberta (V fixa) vs malha fechada (PID discreto Kp=2, Ki=50, Kd=0,001, Ts=5 ms). | Malha aberta: velocidade final `0,7771 m/s`, erro final `22,3 %`, nunca recupera. Malha fechada: velocidade final `1,0000 m/s`, erro final `≈0,000 %`, nunca sai da faixa de ±2% (tensão chega a saturar brevemente em 24 V no instante do degrau). Mensagem final verde. Código de saída 0. |
| `03_sensibilidade.py` | Calcula S(s)=1/(1+L) e T(s)=L/(1+L) para L=C.G com o PID contínuo equivalente (Kp=2, Ki=50, Kd=0,001, N=20); confirma numericamente S(jw)+T(jw)=1 (identidade complexa) e tabula/plota `\|S\|` e `\|T\|` em frequências marcantes. | Identidade confirmada: maior `\|S+T-1\|` = `4,45e-16`. Tabela: DC (0,01 rad/s) `\|S\|=0,0000` (-100,5 dB) / `\|T\|=1,0000` (0 dB); pico de sensibilidade em w=364 rad/s com `\|S\|max=1,493` (+3,48 dB); banda passante (`\|T\|`=-3 dB) em w=408 rad/s; cruzamento `\|L\|=1` em w=250 rad/s; alta frequência (1e5 rad/s) `\|S\|=1,0000` / `\|T\|=0,0000` (-99,7 dB). PNG com Bode sobreposto de S e T. Código de saída 0. |
| `04_desafio.py` | Esqueleto do desafio: sintonizar manualmente Kp, Ki, Kd de um `DiscretePID` para rejeitar um degrau de torque de 33% do nominal em t=0,15 s, dentro de limites de erro em regime, sobressinal e tempo de recuperação. Roda mesmo sem estar implementado, avisando o que falta. | Sem implementação: aviso amarelo `AINDA NÃO IMPLEMENTADO` + tabela de faixas esperadas. Implementado com a referência (Kp=2,0, Ki=50,0, Kd=0,001): `erro_regime_pct≈0,0001 %`, `overshoot_pct≈0,428 %`, `tempo_recuperacao_s≈0,0000 s` — dentro das faixas 0,00–0,05 % / 0,00–3,00 % / 0,00–0,02 s. Ganhos fracos (Kp=0,2, Ki=5, Kd=0) recuperam em `≈0,0845 s` e FALHAM o critério de tempo de recuperação, ilustrando por que a sintonia importa. |

## Observações

- Todos os scripts usam `.venv/bin/python` do diretório `projeto_nexabot/` e
  importam apenas `nexabot.params`, `nexabot.plant`, `nexabot.controllers` e
  `nexabot.viz` — nenhum arquivo fora de `aula_05/` é modificado.
- O laço de malha fechada dos scripts 2 e 4 (`simular_malha_fechada_pid`) é
  um utilitário local copiado/adaptado em cada script — RK4 de passo fino
  para a planta contínua, com `DiscretePID.step` chamado apenas a cada
  `PARAMS.Ts` (200 Hz), reproduzindo um controlador embarcado real.
- No script 1, a comparação `control` vs `sympy` usa `sp.Rational` (não
  `sp.Float`) para os coeficientes: com `Float`, o cancelamento de fatores
  comuns entre numerador e denominador de `sympy.cancel` fica incompleto por
  arredondamento binário, e os graus dos polinômios não "fecham" na
  comparação — vale como nota de cuidado numérico para quem for reproduzir
  esse tipo de verificação.
- No script 3, a identidade S(jw)+T(jw)=1 é uma igualdade **complexa** (fasor
  a fasor), não uma igualdade de magnitudes: `\|S(jw)\|+\|T(jw)\|` passa de 2
  perto do cruzamento (a "água-cama"), o que é o ponto pedagógico central —
  não é um erro numérico.
- Os gráficos ASCII (`nexabot.viz.plot_ascii`) são a saída principal, pensada
  para gravação de tela sem depender de abrir janelas; os PNGs complementares
  (`aula05_algebra_blocos_step.png`, `aula05_rejeicao_malha_aberta.png`,
  `aula05_rejeicao_malha_fechada.png`, `aula05_sensibilidade_bode.png`) vão
  para `figuras/`.
