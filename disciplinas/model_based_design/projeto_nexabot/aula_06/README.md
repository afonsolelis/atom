# Aula 6 — PID na prática e sintonia

Tema: encontrar o ganho crítico do NexaBot na malha discreta real (200 Hz),
aplicar Ziegler-Nichols, comparar sintonias e entender (e corrigir) o efeito
de windup no controlador PID.

## Comandos (execute nesta ordem, a partir de `projeto_nexabot/`)

```bash
.venv/bin/python aula_06/01_ganho_critico.py
.venv/bin/python aula_06/02_ziegler_nichols.py
.venv/bin/python aula_06/03_ajuste_fino.py
.venv/bin/python aula_06/04_antiwindup.py
.venv/bin/python aula_06/05_desafio.py
```

## O que aparece na tela

| Script | O que mostra | Saída esperada (resumo, números observados) |
|---|---|---|
| `01_ganho_critico.py` | Discretiza a planta por ZOH em Ts=5ms, varre/bisseciona o ganho proporcional discreto até `max\|polo(z)\|=1`, calcula Tu pelo ângulo do polo dominante e simula a malha fechada NO ganho crítico (PID com Kp=Ku, Ki=Kd=0) para mostrar a oscilação sustentada. | **Ku ≈ 3.6911**, **Tu ≈ 18.324 ms** (polo dominante em `-0.1432+0.9897j`, ângulo 1.7145 rad). Simulação em Ku: amplitude pico-a-pico de w(t) ≈ 11.40 rad/s na 1ª metade pós-transitório e ≈ 11.35 rad/s na 2ª — não cresce nem decai. Salva `figuras/aula06_ganho_critico.png`. |
| `02_ziegler_nichols.py` | Aplica Ziegler-Nichols clássico com o Ku/Tu do script 1, simula o degrau de 400 rad/s (1,0 m/s) partindo do repouso e tabula `step_metrics`. | Kp=2.2147, Ki=241.7223, Kd=0.005073. Overshoot ≈ 24.84%, tempo de subida ≈ 159.0 ms, tempo de acomodação ≈ 633.5 ms, erro em regime ≈ 0.10 rad/s, tensão de pico = 24.0 V (satura). Salva `figuras/aula06_ziegler_nichols.png`. |
| `03_ajuste_fino.py` | Compara ZN clássico, ZN "no overshoot" e um ajuste manual (Kp=1.3, Ki=15, Kd=0.01) para o MESMO degrau de 400 rad/s, com overshoot/t_subida/t_acomodação/erro regime/ISE. | ZN clássico: 24.84% / 159.0 ms / 633.5 ms / ISE≈9926.5. ZN no-overshoot: 24.84% / 159.0 ms / 586.5 ms / ISE≈9933.2. Manual: **22.77%** / 159.0 ms / 669.0 ms / **ISE≈9469.5 (menor)**. As duas sintonias de ZN saturam o atuador desde o início (Kp·erro inicial ≫ V_max), por isso o tempo de subida é idêntico nas três — a física do motor em tensão máxima domina a subida, não os ganhos. Recomendação impressa: a sintonia **manual**, por ter overshoot e ISE menores (relevante para um AGV que carrega paletes), ao custo de ~40-80 ms a mais de acomodação. |
| `04_antiwindup.py` | Referência de velocidade IRREAL de 4,0 m/s (fisicamente inatingível: o teto do motor em V_max=24V contínuos é ≈1,273 m/s) por 0,5 s, depois cai para 0,5 m/s (segura e alcançável); compara Kaw=0.0 (sem anti-windup) vs Kaw=2.0 (com), usando a sintonia manual do script 3. | Integral no instante da comutação: **9251.6 (sem)** vs **4668.2 (com)**. Tempo para w(t) voltar à faixa de 2% do novo alvo: **2256.5 ms (sem)** vs **872.5 ms (com)** — cerca de **2.6× mais rápido** com anti-windup. O pico pós-comutação é quase igual nos dois casos (~509 rad/s, o teto físico do motor, herdado da fase 1 irreal) — o anti-windup não muda ONDE a velocidade estava quando a referência caiu, muda o quão rápido o NexaBot volta a obedecer. Salva `figuras/aula06_antiwindup_sem.png` e `..._com.png`. |
| `05_desafio.py` | Esqueleto do desafio: ajustar manualmente Kp/Ki/Kd de um `DiscretePID` para satisfazer overshoot ≤10% E tempo de acomodação ≤250 ms num degrau de 150 rad/s (~0,375 m/s). Roda mesmo sem estar implementado, avisando o que falta. | Sem implementação: aviso amarelo `AINDA NÃO IMPLEMENTADO` + tabela de critérios. Implementação de referência verificada (Kp=0.5, Ki=2.0, Kd=0.002): overshoot ≈ 0.53%, t_settle ≈ 0.076 s (76 ms), erro em regime ≈ 0.035 rad/s — os dois requisitos ficam folgadamente dentro do limite. |

## Ponto técnico central: por que a busca de ganho crítico é na malha DISCRETA

Um motor CC de 2ª ordem estritamente próprio, com controle proporcional
CONTÍNUO puro e realimentação unitária, satisfaz Routh-Hurwitz para
QUALQUER Kp>0 — a malha contínua nunca desestabiliza, então a receita
clássica de Ziegler-Nichols ("aumente Kp até oscilar") não tem onde
"pegar" em tempo contínuo neste sistema. O controlador embarcado real do
NexaBot roda a Ts=5ms (200 Hz); discretizando a planta por ZOH nesse
período, a fase extra do segurador de ordem zero abre espaço para
instabilidade em malha fechada com ganho proporcional discreto finito —
é essa malha (planta ZOH + Kp discreto) que o script 1 varre e onde Ku e
Tu são de fato encontrados (`aula_06/01_ganho_critico.py`).

## Observações

- Todos os scripts usam `.venv/bin/python` do diretório `projeto_nexabot/` e
  importam apenas `nexabot.viz`, `nexabot.params`, `nexabot.plant` e
  `nexabot.controllers` — nenhum arquivo fora de `aula_06/` é modificado.
- Os scripts 1-4 replicam localmente (com pequenas variações) o utilitário
  `simular_malha_fechada_pid`: planta contínua integrada por RK4 de passo
  fino (`Ts/10`), com o `DiscretePID` atualizando o sinal de controle a
  cada `Ts` e o mantendo em zero-order-hold entre atualizações — é assim
  que um controlador embarcado real funciona.
- `numpy>=2.0` renomeou `numpy.trapz` para `numpy.trapezoid`; o script 3
  usa `np.trapezoid` para a integral do erro ao quadrado (ISE), mesma
  regra trapezoidal.
- Os gráficos ASCII (`nexabot.viz.plot_ascii`) são a saída principal, pensada
  para gravação de tela sem depender de abrir janelas; os PNGs
  complementares vão para `figuras/` com prefixo `aula06_`.
