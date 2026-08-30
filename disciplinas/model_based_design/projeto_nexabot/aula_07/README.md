# Aula 7 — Discretização e período de amostragem

Tema: transformar a planta contínua do NexaBot em um sistema discreto
(Euler, Tustin/bilinear e ZOH), o impacto real de escolher um Ts maior ou
menor no firmware embarcado, o custo em margem de fase de um atraso
computacional de 1 ciclo, e o efeito da resolução finita de encoder e PWM.

## Comandos (execute nesta ordem, a partir de `projeto_nexabot/`)

```bash
.venv/bin/python aula_07/01_euler_tustin_zoh.py
.venv/bin/python aula_07/02_escolha_de_ts.py
.venv/bin/python aula_07/03_atraso_computacional.py
.venv/bin/python aula_07/04_quantizacao.py
.venv/bin/python aula_07/05_desafio.py
```

## O que aparece na tela

| Script | O que mostra | Saída esperada (resumo, números reais observados) |
|---|---|---|
| `01_euler_tustin_zoh.py` | Discretiza G(s) do NexaBot em Ts=5 ms por Euler, Tustin e ZOH (`control.c2d`), aplica um degrau de 12 V a cada versão discreta e compara com a resposta contínua de referência (RK4). | Erro RMS/final/pico de cada método: **Euler** RMS=1,0858 rad/s, erro final=0,0820 rad/s (0,0323%), pico=4,6729 rad/s; **Tustin** RMS=1,3234, erro final=0,0149 rad/s (0,0059%), pico=4,1198; **ZOH** RMS≈1,6e-9, erro final≈-7,4e-13 (ruído numérico) — exato. Conclusão observada: ZOH é exato por construção (entrada realmente mantida constante entre amostras); Tustin acerta melhor o valor final (preserva ganho DC exatamente), mas tem RMS de transitório levemente MAIOR que o Euler neste caso — não existe um "sempre melhor" entre os dois. |
| `02_escolha_de_ts.py` | Varre 18 valores de Ts (0,5 ms a 100 ms, log) com um PID FIXO (Kp=0,5, Ki=5,0, Kd=0,0005 — mais moderado que o Ziegler-Nichols clássico de Ku≈3,69/Tu≈18,3ms, que satura o atuador e mascara o efeito de Ts) e classifica cada resposta a um degrau de 50 rad/s. | **Bom desempenho** até Ts≈8,26 ms (sobressinal ≤9,6%); **degradado** de Ts≈11,3 ms a Ts≈39,3 ms (sobressinal de 16% a 172%); **instável** (critério \|w\|>3x referência) a partir de Ts≈44,3 ms (fronteira refinada por bisseção). O Ts nominal do firmware (5 ms) fica dentro da faixa de bom desempenho. |
| `03_atraso_computacional.py` | Calcula a margem de fase da malha aberta discreta (PID+planta via ZOH) com e sem um atraso extra de z⁻¹ (1 ciclo de atraso computacional), em Ts=5 ms e Ts=20 ms, e confirma em simulação temporal com o parâmetro `atraso_ciclos`. | Ts=5 ms: PM sem atraso=66,19°, PM com atraso=43,61° (perda de 22,58°, igual à previsão teórica wgc·Ts) — **permanece estável**. Ts=20 ms: PM sem atraso=32,51°, PM com atraso=**-63,86°** (perda de 96,37°, também igual a wgc·Ts) — **fica instável**. Confirmado no tempo: em Ts=20 ms com atraso de 1 ciclo, \|w\| chega a 151 rad/s (referência é 50) e não converge; sem atraso, \|w\|max=64,9 rad/s e converge normalmente. |
| `04_quantizacao.py` | Isola o efeito da resolução do encoder (128 vs 2048 pulsos/volta, PWM ideal) e da resolução do PWM (8 vs 12 bits, encoder ideal) na mesma malha PID (Ts=5 ms, degrau de 50 rad/s). | **Encoder**: 128 ppr → sobressinal 12,45%, erro em regime 0,7021 rad/s, chattering de u (desvio padrão) 1,5681 V; 2048 ppr → sobressinal 13,45%, erro 0,0131 rad/s, chattering 0,1692 V. **PWM**: 8 bits (passo 0,1875 V) → erro 0,0031 rad/s, chattering 0,0927 V; 12 bits (passo 0,0117 V) → erro 0,0012 rad/s, chattering 0,0036 V. Conclusão observada: o encoder DOMINA (chattering ~17x maior que o PWM de 8 bits, erro em regime ~2 ordens de grandeza maior) — o ruído de quantização do sensor realimenta direto no PID a cada ciclo, o do atuador é filtrado pela inércia mecânica da planta. |
| `05_desafio.py` | Esqueleto do desafio: dado um PID e um `Ts_candidato`, verificar se a malha fechada é estável E atende um sobressinal máximo (20%), devolvendo um veredito de aprovação. Roda mesmo sem estar implementado, avisando o que falta. | Sem implementação: aviso amarelo `AINDA NÃO IMPLEMENTADO` + tabela de veredito esperado por Ts. Implementado corretamente, com Kp=0,5/Ki=5,0/Kd=0,0005, r=50 rad/s: Ts=5 ms → estável=True, sobressinal=3,17%, **aprovado**; Ts=20 ms → estável=True, sobressinal=29,88%, **reprovado** (sobressinal alto); Ts=50 ms → estável=False, **reprovado** (instável). |

## Observações

- Todos os scripts usam `.venv/bin/python` do diretório `projeto_nexabot/` e
  importam apenas `nexabot.params`, `nexabot.plant`, `nexabot.controllers` e
  `nexabot.viz` (mais `control`, `numpy`, `scipy.signal` e `matplotlib`) —
  nenhum arquivo fora de `aula_07/` é modificado.
- O laço de malha fechada (`simular_malha_fechada_pid`) é o mesmo padrão
  usado em `aula_05/02_rejeicao_disturbio.py`: RK4 de passo fino para a
  planta contínua, com `DiscretePID.step` chamado apenas a cada `Ts` — o
  parâmetro `atraso_ciclos` (usado no script 3) atrasa em uma amostra a
  aplicação do comando calculado, simulando o tempo de execução do firmware.
- O PID FIXO usado nos scripts 02-05 (Kp=0,5, Ki=5,0, Kd=0,0005) foi
  escolhido, e não o Ziegler-Nichols clássico (Kp≈2,21, Ki≈241,7, Kd≈0,005,
  calculado a partir de Ku≈3,69/Tu≈18,3ms da Aula 6): testamos os ganhos de
  ZN clássico neste degrau e o Ki muito alto satura o atuador com
  sobressinal de 60-90% já em Ts=0,5 ms, o que mascararia o efeito de Ts
  isoladamente — o objetivo pedagógico do script 2. Isso é reportado
  explicitamente no script 1 (bloco `Ponto pedagógico`), não escondido.
- No script 1, a discretização por Euler produz coeficientes de numerador
  numericamente mal-condicionados (aviso `BadCoefficients` do scipy) ao
  converter para espaço de estados — o resultado numérico continua correto,
  mas o aviso é suprimido explicitamente (`warnings.catch_warnings`) para
  não poluir a gravação de tela.
- No script 3, a margem de fase é calculada sobre o modelo LINEAR do PID
  (mesma equação a diferenças de `DiscretePID.step`, mas ignorando
  saturação/anti-windup, que são não lineares) — a simulação temporal, essa
  sim, usa o `DiscretePID` real com saturação, e serve como confirmação
  independente do resultado analítico.
- No script 2, a coluna `t_acomodação = 0,0 ms` pode significar duas coisas
  diferentes (o `step_metrics` de `nexabot.controllers` não distingue):
  "nunca saiu da faixa de 2%" (bom) ou "saiu e nunca mais voltou dentro da
  simulação" (ruim, típico de sobressinal muito alto) — o script imprime um
  aviso explícito sobre isso; use a coluna de sobressinal e a classificação
  como critério principal.
- Os gráficos ASCII (`nexabot.viz.plot_ascii`, `nexabot.viz.sparkline`) são
  a saída principal, pensada para gravação de tela sem depender de abrir
  janelas; o PNG complementar (`aula07_euler_tustin_zoh.png`) vai para
  `figuras/`.
