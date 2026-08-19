# Dimensionamento inicial da NexaOrder

Este documento registra as estimativas que justificam a decisão de distribuir.
Todas elas são **hipóteses verificáveis**, não conclusões. A Aula 16 recalcula os mesmos
números com evidências operacionais reais.

## 1. Quantas instâncias sustentam o pico

O número mínimo de instâncias é o teto da divisão entre a taxa de chegada no pico e o
produto da capacidade medida de uma instância pela utilização-alvo:

```
N = ⌈ λ_pico / (capacidade × utilização_alvo) ⌉
```

Insumos da NexaOrder:

| Variável | Valor | Origem |
|----------|-------|--------|
| λ_pico | 800 req/s | projeção de negócio para a campanha de fim de ano |
| capacidade | 200 req/s por instância | teste de carga preliminar de uma instância |
| utilização-alvo | 70% | convenção operacional, revista na Aula 13 |

```
N = ⌈ 800 / (200 × 0,7) ⌉ = ⌈ 800 / 140 ⌉ = ⌈ 5,71 ⌉ = 6
```

**Seis instâncias.**

### Por que não quatro

A conta ingênua faria `800 / 200 = 4`. Quatro instâncias significam operar a 100% da
capacidade o tempo todo, sem folga alguma. Um pico inesperado, uma instância
reiniciando ou uma consulta mais pesada que o normal saturam o serviço, e as filas e a
latência crescem de forma abrupta.

A utilização-alvo de 70% é exatamente essa folga.

### Ressalva

Esta conta não substitui teste de carga. Ela indica **onde começar a medir**.

## 2. O preço de cada nove

Disponibilidade é a proporção de tempo em que o serviço cumpre sua função.
Em uma janela de 30 dias:

| Objetivo | Indisponibilidade tolerada/mês | O que exige na prática |
|----------|-------------------------------|------------------------|
| 99% | ~7 h 12 min | redundância básica, recuperação manual |
| 99,9% | ~43 min | múltiplas instâncias, desvio automático de tráfego |
| 99,99% | ~4 min 19 s | zonas independentes, automação, ensaio de falhas |
| 99,999% | ~26 s | raramente justificável fora de domínios críticos |

Cada nove adicional não custa um pouco mais. Custa redundância, automação e recuperação
em outro patamar.

### Armadilha

Redundância só protege se as instâncias não compartilharem o mesmo ponto de falha.
Duas instâncias no mesmo host não protegem contra a queda desse host. Duas zonas
alimentadas pelo mesmo banco não protegem contra a falha desse banco.

Redundância no diagrama não é redundância na prática. A Aula 16 retoma isso como
análise formal de SPOF.

## 3. Métricas que o projeto vai acompanhar

Quatro medidas distintas, frequentemente confundidas:

| Métrica | O que mede | Cuidado |
|---------|-----------|---------|
| Latência | tempo para concluir uma operação | usar p95/p99, nunca a média |
| Throughput | trabalho concluído por unidade de tempo | cresce até o joelho da curva, depois a fila explode |
| Disponibilidade | capacidade de atender | um endpoint pode responder e ainda estar funcionalmente indisponível |
| Confiabilidade | produzir resultados corretos de forma sustentada | responder rápido e duplicar cobrança não é confiabilidade |

Os alvos iniciais, revisados na Aula 13 quando houver instrumentação:

- p95 do checkout abaixo de **400 ms**
- taxa de conclusão de pedidos acima de **98%**
- disponibilidade do fluxo de pedidos: **99,9%**
