# Aula 4 — Controlabilidade, observabilidade e realimentação de estados

Tema: verificação estrutural do modelo (controlabilidade/observabilidade),
alocação de polos com realimentação de estados, LQR e observador de
Luenberger — os quatro blocos de projeto que sustentam o controle moderno do
NexaBot, encerrados por um desafio de projeto com dois requisitos simultâneos.

## Comandos (execute nesta ordem, a partir de `projeto_nexabot/`)

```bash
.venv/bin/python aula_04/01_ctrb_obsv.py
.venv/bin/python aula_04/02_alocacao_polos.py
.venv/bin/python aula_04/03_lqr.py
.venv/bin/python aula_04/04_observador.py
.venv/bin/python aula_04/05_desafio.py
```

## O que aparece na tela

| Script | O que mostra | Saída esperada (resumo) |
|---|---|---|
| `01_ctrb_obsv.py` | Matrizes A, B, C; matriz de controlabilidade Wc=[B, A.B] e de observabilidade Wo=[C; C.A]; posto de cada uma; explicação física do que isso garante para o NexaBot. | `det(Wc) ≈ 1,469×10⁷`, `det(Wo) = -180`; **posto(Wc) = posto(Wo) = 2** (sistema totalmente controlável e observável). Tabela final toda verde, código de saída 0. |
| `02_alocacao_polos.py` | Dois cenários de alocação de polos (`state_feedback_gain` + pré-compensação Nbar) para referência de 400 rad/s (1,0 m/s): "moderado" (-700, -20 rad/s) e "agressivo" (-3000, -3500 rad/s). Gráficos ASCII de u(t) ideal e w(t) real (saturada), tabela ideal-vs-real por cenário e tabela-resumo comparativa. Salva 2 PNGs. | **Moderado**: pico de u ideal = **108,9 V** (já excede 24 V) → satura; com saturação, acomodação em ≈256,5 ms e erro de regime ≈3,56 rad/s (0,9%). **Agressivo**: pico de u ideal = **81.667 V** (3.400x o limite!) → satura completamente; resposta real vira praticamente liga/desliga em ±24V, acomodação ≈206,6 ms, erro de regime ≈0. Ambos aparecem como `SATURA` (vermelho) na tabela-resumo. |
| `03_lqr.py` | Varredura de Q=diag([1,q2]), q2∈{1,10,100,1000}, R=[[r]], r∈{0,01;0,1;1;10} (16 combinações); para cada uma, K via `lqr_gain`, simulação ideal (sem saturar) e métricas de desempenho (overshoot, t. de acomodação) e esforço (pico de \|u\|, ∫u²dt). Destaca o extremo mais suave e o mais agressivo da grade, com gráficos ASCII de ambos. | Extremo mais suave: q2=1, r=10 → t.acomodação=85,0 ms, pico\|u\|=127,9 V, ∫u²dt=308,2. Extremo mais agressivo: q2=1000, r=0,01 → t.acomodação=0,90 ms, pico\|u\|=126.491 V, ∫u²dt≈1.265.832. **Todas as 16 combinações da grade têm pico de tensão acima de 24 V** (destacadas em vermelho) — confirma que mais desempenho sempre custa mais esforço. |
| `04_observador.py` | Observador de Luenberger (`control.place` no sistema dual A^T,C^T) para estimar a corrente a partir só de w medido; polos do observador em (-2500, -80) rad/s (~3,6x–4,0x mais rápidos que a malha fechada de referência -700/-20). Simula planta real + observador em paralelo (RK4 manual) com um degrau de 12 V, partindo de um chute inicial ERRADO no observador. Gráficos ASCII de i real, î estimada e do erro, mais tabela de convergência. | `L ≈ [-3163,0; 2236,8]^T`; autovalores de (A-LC) = -80 e -2500 (batem com o pedido). Erro de estimação parte de -1,0 A, pico transitório de ≈34,5 A (por causa do chute inicial deliberadamente errado em w: 30 rad/s de diferença), e cai para **-0,00014 A aos 150 ms** — convergência efetivamente completa. |
| `05_desafio.py` | Esqueleto do desafio: encontrar um único K (por alocação de polos ou LQR) que atenda ao mesmo tempo REQ-A (acomodação real ≤300 ms) e REQ-B (pico de tensão ideal ≤150 V). Roda mesmo sem estar implementado, avisando o que falta. | Sem implementação: aviso amarelo `AINDA NÃO IMPLEMENTADO` + tabela de faixas esperadas. Implementado corretamente (verificado com polos=[-700,-20]): `overshoot_pct≈-0,015%`, `t_settle_s≈0,2565 s` (dentro de 0,20–0,30 s), `u_peak_V≈108,89 V` (dentro de 80–150 V), `steady_state_error≈0,068 rad/s` — REQ-A e REQ-B ambos `OK`. |

## Observações

- Todos os scripts usam `.venv/bin/python` do diretório `projeto_nexabot/` e
  importam apenas `nexabot.params`, `nexabot.plant`, `nexabot.controllers` e
  `nexabot.viz` — nenhum arquivo fora de `aula_04/` é modificado.
- A lei de controle usada nos scripts 2, 3 e 5 é sempre
  `u(t) = -K.x(t) + Nbar.r`, com `Nbar = 1 / (C.(-(A-B.K))^-1.B)` calculado
  a partir das matrizes de `nexabot.plant.state_space_matrices` — a mesma
  técnica de pré-compensação de ganho estático em todos eles, para deixar a
  comparação entre alocação de polos e LQR justa (mesmo critério de
  seguimento de referência, mesma referência de 400 rad/s).
- A simulação da malha fechada é sempre um laço RK4 manual chamando
  `nexabot.plant.derivative`, igual ao integrador usado nas Aulas 1-3 — não
  se usa `control.forced_response` para deixar explícito, no código, o
  ponto exato em que a saturação `np.clip(u, -V_max, V_max)` entra (ou não)
  no laço.
- Os gráficos ASCII (`nexabot.viz.plot_ascii`) são a saída principal, pensada
  para gravação de tela sem depender de abrir janelas; os PNGs complementares
  (prefixo `aula04_...png`) vão para `figuras/`.
- Limitação conhecida: os scripts 2, 3 e 5 ignoram o limite de corrente
  `i_max=12 A` do driver (só respeitam `V_max=24 V`) — no cenário "moderado"
  do script 2 a corrente de pico fica bem abaixo de 12 A, mas isso não é
  verificado explicitamente em código; fica como extensão natural do
  desafio do script 5.
