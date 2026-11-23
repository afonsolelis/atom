# Aplicação padrão da disciplina: a obra Torre A

Todos os laboratórios da disciplina usam a mesma obra fictícia: a **Torre A**, um edifício com **três subsolos** escavados ao lado de um **prédio antigo** (1968, fundação rasa), numa rua urbana. A obra é monitorada por drone e por sensores IoT, do rádio do sensor até o painel do engenheiro.

O simulador em [`index.html`](index.html) roda a obra no navegador e é embutido nos slides (`?embed=1`, visualização `data-viz="plataforma"` de `assets/obra.js`). Este arquivo é a fonte única de nomes, tópicos e números: ao escrever um laboratório, use só o que está aqui.

## A obra

- Escavação de 3 subsolos (cota −10,5 m), contida por cortina de estacas com escoras metálicas no 1º nível.
- Prédio vizinho de 1968 com fundação rasa, colado à cortina (lado do I-1 e do I-2).
- Grua G1 com o gateway LoRaWAN **GW-01** no topo e o anemômetro **AN-01**.
- Escritório de obra com fibra e roteador 4G (reserva opcional do gateway).
- Laje L1 do térreo em cura (temperatura e umidade).
- Rua das Paineiras na divisa (sensor de poeira).
- Relógio simulado: começa na **segunda-feira, 16/11/2026, 07:00** (Brasília). O banco guarda a hora da medição em **UTC** (10:00Z).

## Os 11 sensores

| Sensor | O que mede | Setor | Grandeza (unidade) | Bruto | Intervalo | Limites: atenção · alerta · alarme |
|---|---|---|---|---|---|---|
| `I-1` | Inclinômetro na cortina | cortina | deslocamento no topo (mm) | Σ sen θ (L = 0,5 m) | 15 min | 10 · 14 · 18 mm; 0,5 · 1,0 mm/dia |
| `I-2` | Inclinômetro na cortina, junto ao prédio antigo | cortina | deslocamento no topo (mm) | Σ sen θ | 15 min | 10 · 14 · 18 mm; 0,5 · 1,0 mm/dia |
| `PZ-01` | Piezômetro, 1º subsolo | escavacao | nível d'água (m) | 4–20 mA (0–20 m) | 15 min | 7 · 8 · 9 m |
| `PZ-02` | Piezômetro, 2º subsolo | escavacao | nível d'água (m) | 4–20 mA | 15 min | 7 · 8 · 9 m |
| `PZ-03` | Piezômetro, 3º subsolo (pior enlace de rádio) | escavacao | nível d'água (m) | 4–20 mA | 15 min | 7 · 8 · 9 m |
| `E-01` | Extensômetro de corda vibrante na escora EM-03 | escavacao | carga (kN) = 2,4 × µε | µε aparente | 15 min | 780 · 840 · 960 kN |
| `T-01` | Temperatura da laje L1 | laje | °C | Ω (PT100) | 15 min | — (sensor de apoio) |
| `UR-01` | Umidade do ar sobre a laje L1 | laje | % UR | % UR | 15 min | — (sensor de apoio) |
| `PO-01` | Poeira na divisa | divisa | PM10 (µg/m³) | µg/m³ óptico | 5 min | 100 · 150 · 250 µg/m³ |
| `AN-01` | Anemômetro no topo da grua (cabo até o gateway) | grua | vento (km/h) | m/s | 2 min | 35 · 42 · 72 km/h |
| `ACC-01` | Acelerômetro no prédio vizinho | vizinho | PPV (mm/s) | g (pico) | 5 min | 3 · 5 · 10 mm/s |

Valores normais: I-1 ≈ 4,2 mm; I-2 ≈ 8,6 mm; PZ ≈ 4,3 / 5,2 / 5,9 m; E-01 ≈ 600 kN (250 µε); PO-01 ≈ 45 µg/m³ fora do expediente e ≈ 75 µg/m³ com a obra trabalhando; AN-01 ≈ 15 km/h.

### TARP dos inclinômetros (Aula 13)

| Nível | Gatilho | Ação | Responsável | Prazo |
|---|---|---|---|---|
| Normal | dentro do previsto | rotina: leitura a cada 15 min, relatório semanal | técnico de instrumentação | — |
| Atenção | 10 mm ou 0,5 mm/dia | aumentar a frequência, inspecionar, avisar o projetista | engenheiro da obra | 24 h |
| Alerta | 14 mm ou 1,0 mm/dia | preparar e iniciar o reforço previsto, restringir a frente | engenheiro + projetista | 12 h |
| Alarme | 18 mm | paralisar a escavação na frente, executar a contingência, isolar a área | responsável técnico | imediato |

Anemômetro (NR-18, Aula 15): acima de 42 km/h, operação só com análise de risco e permissão de trabalho; acima de 72 km/h, operação proibida.

## Caminho do dado

```
Sensor → nó (ESP32 + rádio LoRa; AN-01: datalogger da grua) → LoRaWAN 915 MHz → GW-01 (topo da grua)
  → internet (fibra do escritório; 4G de reserva opcional) → servidor de rede (deduplica, ADR)
  → broker MQTT (1883 sem TLS / 8883 com TLS) → Node-RED (valida, converte) → InfluxDB → Grafana (painel e alertas)
```

- **Tópicos MQTT:** `obra/torre-a/<setor>/<tipo>/<sensor>/<grandeza>`, por exemplo `obra/torre-a/escavacao/piezometro/PZ-03/nivel` e `obra/torre-a/cortina/inclinometro/I-2/desloc`. QoS 1.
- **Último desejo (LWT):** `obra/torre-a/status/GW-01` = `online` / `offline` (retido).
- **Payload:** `{"ts":"2026-11-16T10:15:00Z","bruto":0.0172,"valor":8.61,"un":"mm","q":"ok","bat":3.61}`.
- **Line protocol:** `leitura,obra=torre-a,setor=cortina,tipo=inclinometro,sensor=I-2 valor=8.61,bruto=0.0172,bat=3.61,q="ok" <ns UTC>`. Tags: obra, setor, tipo, sensor. Fields: valor, bruto, bat, q.
- **Volume:** 2.064 pontos por dia nos 11 sensores (cerca de 753 mil por ano).

## Rede LoRaWAN (Aula 11)

Nó a 14 dBm, antena de 2 dBi, gateway com 3 dBi, 915 MHz. Perda no espaço livre `FSPL = 20 log(d_km) + 20 log(915) + 32,44`. Sensibilidade: SF7 −123, SF8 −126, SF9 −129, SF10 −132, SF11 −134,5, SF12 −137 dBm. O **ADR** escolhe o menor SF com margem ≥ 10 dB; sem ADR, todos vão para SF12. Tempo no ar (25 bytes, 125 kHz): 62 ms em SF7 e 1,48 s em SF12. Bateria de 2.600 mAh, 120 mA transmitindo, 10 µA dormindo.

| Sensor | Distância ao GW-01 | Perdas (lajes, paredes, caixa) |
|---|---|---|
| I-1 / I-2 | 60 m / 70 m | 20 / 25 dB |
| PZ-01 / PZ-02 / PZ-03 | 80 / 70 / 55 m | 25 / 30 / **35 dB (ajustável de 10 a 95 dB)** |
| E-01, T-01, UR-01 | 50, 30, 25 m | 15, 5, 5 dB |
| PO-01, ACC-01 | 60, 110 m | 8, 18 dB |

Com 35 dB, o PZ-03 fecha em SF7 com cerca de 40 dB de margem; com 70 dB, o ADR sobe para SF9; com 90 dB, nem o SF12 fecha e as leituras vão para a fila do nó. Sem ADR, a bateria estimada cai de cerca de 12,5 anos para cerca de 1,4 ano.

## Regras de alarme (aba Alarmes)

Valores iniciais: só **Limite por velocidade** ligado, como num sistema recém-instalado.

| Regra | Efeito |
|---|---|
| Limite por velocidade | mm/dia nos inclinômetros, sobre as últimas 24 h (precisa de ≥ 12 h de série) |
| Histerese | sai do nível só abaixo do limite menos a histerese (I: 0,5 mm; PZ: 0,2 m; E: 20 kN; PO: 10 µg/m³; AN: 3 km/h; ACC: 0,3 mm/s) |
| Persistência | só sobe de nível com duas leituras seguidas |
| Compensação térmica da escora | desconta do E-01 a deformação do sol |
| Correção da poeira pela umidade | acima de 80% UR, divide o PO-01 pelo fator 1 + (UR − 80)/10; acima de 85%, qualidade "suspeita" |
| Alerta de sensor mudo | sem leitura há 3 intervalos → cinza + notificação; sem a regra, o sensor continua verde |
| Plausibilidade (salto) | salto maior que o possível entre leituras (I: 2 mm) → notificação de leitura implausível |

## Os sete cenários (aba Cenários)

| Cenário | Velocidade | Duração | Aulas | O que acontece |
|---|---|---|---|---|
| O I-2 acelera ao lado do prédio antigo | 1 s = 1 h | 4 dias | 9, 13, 14 | I-2 de 11,5 mm subindo 1,2 mm/dia: alerta por velocidade antes do alerta por valor (14 mm em ~2,1 dias); PZ-02 sobe 0,25 m/dia |
| Escora no sol | 1 s = 15 min | 2 dias | 9 | +180 µε ao sol: carga aparente passa de 960 kN entre 10 h e 16 h; com compensação, ≈ 600 kN |
| Rajada de quase 47 km/h na grua | 1 s = 1 min | 2 h | 15 | AN-01 sobe a ≈ 13 m/s (46,8 km/h) aos 40 min: atenção > 35, alerta > 42 km/h |
| Três horas sem internet no canteiro | 1 s = 5 min | 6 h | 10, 11, 13 | fibra cai de +1 h a +4 h; sem 4G, LWT offline, nós guardam e reenviam com a hora original |
| Poeira na divisa num dia úmido | 1 s = 15 min | 1 dia | 9 | UR > 90% até +10 h: PO-01 bruto quase dobra; com correção, normal e "suspeita" |
| 37 alarmes num fim de semana | 1 s = 1 h | 2,5 dias (começa sáb 00:00) | 13 | I-2 ≈ 9,7 mm e PZ-01 ≈ 6,85 m oscilando abaixo do limite: dezenas de notificações sem histerese e persistência; quase nenhuma com as duas |
| A senha do gateway era admin | 1 s = 5 min | 4 h | 16 | varredura (+20 min), login admin/admin (+25), conexão ao broker (+35), leituras falsas de ≈ 3 mm no I-2 a partir de +50 min enquanto o real sobe 0,65 mm/h |

No cenário da senha: **Rede segmentada** impede a varredura; **Credencial única** impede o login; **ACL por tópico** faz o broker negar a publicação falsa; **Plausibilidade** (aba Alarmes) notifica o salto.

## Drone e BIM (Aulas 8 e 14)

| Voo | GSD | GCPs | RMSE | Volume escavado | Avanço medido |
|---|---|---|---|---|---|
| 26/10 | 2,1 cm/px | 6 | 2,6 cm | 38.100 m³ | 33,9% |
| 02/11 | 2,1 cm/px | 6 | 2,4 cm | 41.800 m³ | 36,2% |
| 09/11 | 2,2 cm/px | 6 | 2,9 cm | 44.600 m³ | 38,7% |
| 16/11 (botão "Voar e processar") | 2,1 cm/px | 6 | 2,3 cm | **46.900 m³** (a planilha dizia 48.200) | **40,8%** |

Avanço ponderado (Aula 14): Fundações 15% (100% executado / 100% previsto), Estrutura 45% (50% / 55%), Alvenaria 25% (10% / 15%), Instalações 15% (5% / 10%). Orçamento de R$ 20 milhões; previsto 45%; dito na reunião 62%. Depois do voo: VP 9,00, VA 8,15, CR 8,60 (R$ milhões), **IDP 0,91** e **IDC 0,95**.

Cada sensor está ligado a um elemento BIM por GUID (ex.: I-2 → cortina de estacas, painel P05).

## Segurança e LGPD (Aula 16)

Valores iniciais: todas as proteções desligadas (gateway com admin/admin, painel na internet pela porta 80, broker na 1883 sem TLS, uma senha para todos os clientes, firmware de 2023, câmera da grua gravando rostos e o quintal do vizinho sem prazo de guarda).

Proteções: credencial única por dispositivo; rede segmentada e painel só pela VPN; MQTT com TLS (8883); ACL por tópico; firmware atualizado; máscara de privacidade e guarda de 30 dias nas câmeras.

## Onde o simulador entra nas aulas

| Aula | Aba inicial | O que o aluno faz |
|---|---|---|
| 1 | Canteiro | percorre a planta, as leituras e o avanço medido × previsto |
| 8 | Drone e BIM | processa o voo de 16/11 (46.900 m³) |
| 9 | Cenários | escora no sol, com e sem compensação térmica |
| 10 | Leituras | três horas sem internet: fila, reenvio e hora UTC da medição |
| 11 | Rede LoRaWAN | perdas no 3º subsolo, ADR e 4G de reserva |
| 12 | MQTT | curingas, filtro inválido e line protocol |
| 13 | Alarmes | fim de semana de alarmes falsos, histerese e persistência |
| 14 | Drone e BIM | recalque do I-2 no modelo; voo, IDP e IDC |
| 15 | Cenários | rajada na grua e o limite de 42 km/h |
| 16 | Segurança e LGPD | senha de fábrica, leituras falsas e proteções |

Os números deste arquivo valem para a semente fixa do simulador: o mesmo cenário, com as mesmas regras, sempre dá os mesmos números. O ruído dos sensores muda as casas decimais de um cenário para outro, nunca a história.
