# Aula 16: Estudo de Caso Nacional – Inspeção, Deterioração e Reforço

## Objetivos da Aula

Ao final desta aula, o aluno será capaz de:

- Sintetizar achados de inspeção e mapeamento de patologias
- Mapear decisões de reforço e justificá-las tecnicamente
- Verificar critérios pós-intervenção (M, V, γ_est, ELS)
- Elaborar programa de monitoramento pós-obra

### Esquema do caso

<img src="https://res.cloudinary.com/dyhjjms8y/image/upload/v1760304352/estrutura_pontes/aula16_ponte.png" alt="Esquema: inspeção, deterioração e reforço de pontes" width="760" />

Leitura do esquema:

- Patologias identificadas
- Soluções de reforço estrutural
- Verificações pós-intervenção
- Programa de monitoramento

## Referência do Estudo

**Artigo:** EngEVista/UFF — Patologias e inspeção de pontes em concreto armado: estudo de caso da Ponte Gov. Magalhães Pinto (MG), 2018
**Link:** <https://periodicos.uff.br/engevista/article/download/27125/16562/98638>

## Contexto do Estudo de Caso

### Ponte Analisada

- **Localização**: Ponte Gov. Magalhães Pinto (MG)
- **Período de construção**: 1970-1975
- **Idade no estudo**: 43-48 anos
- **Vão**: $L = 40\,\mathrm{m}$ (viga de concreto armado)
- **Ambiente**: urbano (moderadamente agressivo)
- **Tráfego**: intenso, com predominância de veículos pesados

### Problema Identificado

A ponte apresentava manifestações patológicas significativas após 40+ anos de serviço, incluindo fissuras, corrosão da armadura, delaminação do concreto e comprometimento da capacidade estrutural. O estudo analisou as patologias, propôs soluções de reforço e estabeleceu um programa de monitoramento.

## Sintetização dos Achados de Inspeção

### 1) Patologias Identificadas

**Fissuras de flexão**:

- Localização: meio do vão das vigas principais
- Abertura: $w = 0{,}5\,\mathrm{mm}$ (máxima)
- Profundidade: $d = 20\,\mathrm{mm}$
- Distribuição: 90% das vigas

**Corrosão da armadura**:

- Taxa de corrosão: $\eta_{corr} = 30\%$
- Profundidade de carbonatação: $d_{carb} = 35\,\mathrm{mm}$
- Perda de seção: $\Delta A_s = 0{,}30 \times A_{s,0}$
- Distribuição: 70% das vigas

**Delaminação do concreto**:

- Área afetada: $A_{del} = 40\%$ da superfície
- Espessura perdida: $t_{del} = 20\,\mathrm{mm}$
- Redução da seção: $\Delta A_c = 0{,}40 \times A_c$
- Distribuição: 80% das vigas

### 2) Causas Prováveis

**Fatores ambientais**:

- Proximidade de indústrias (poluição)
- Umidade relativa alta (75%)
- Temperatura média alta (26°C)
- Variações térmicas significativas

**Fatores estruturais**:

- Sobrecarga estrutural
- Fadiga por cargas cíclicas
- Retração do concreto
- Variações térmicas

**Fatores de manutenção**:

- Ausência de programa de inspeção
- Falta de limpeza de drenagem
- Ausência de proteção contra corrosão
- Falta de reparo de danos

## Mapeamento de Decisões de Reforço

### 1) Reforço à Flexão

**Deficiência identificada**:
$$M_{def} = M_{Ed} - M_{Rd,ef} = 1500{,}0 - 800{,}0 = 700{,}0\,\mathrm{kN \cdot m}$$

**Solução adotada**: Protensão externa

- Força de protensão: $P_{ref} = 500{,}0\,\mathrm{kN}$
- Excentricidade: $e_{ref} = 1{,}4\,\mathrm{m}$
- Momento adicional: $M_{ref} = P_{ref} \times e_{ref} = 500{,}0 \times 1{,}4 = 700{,}0\,\mathrm{kN \cdot m}$

**Verificação**:
$$M_{Rd,ref} = M_{Rd,ef} + M_{ref} = 800{,}0 + 700{,}0 = 1500{,}0\,\mathrm{kN \cdot m} \geq M_{Ed} = 1500{,}0\,\mathrm{kN \cdot m}$$

Condição atendida (✓).

### 2) Reforço ao Cisalhamento

**Deficiência identificada**:
$$V_{def} = V_{Ed} - V_{Rd,ef} = 400{,}0 - 250{,}0 = 150{,}0\,\mathrm{kN}$$

**Solução adotada**: Estribos adicionais

- Armadura adicional: $A_{sw,ref} = 3{,}5\,\mathrm{cm^2/m}$
- Estribos: $\phi 8{,}0\,\mathrm{mm}$ c/ $15\,\mathrm{cm}$
- Cortante adicional: $V_{ref} = 150{,}0\,\mathrm{kN}$

**Verificação**:
$$V_{Rd,ref} = V_{Rd,ef} + V_{ref} = 250{,}0 + 150{,}0 = 400{,}0\,\mathrm{kN} \geq V_{Ed} = 400{,}0\,\mathrm{kN}$$

Condição atendida (✓).

### 3) Reforço de Fundações

**Problemas identificados**:

- Recalques diferenciais: $\Delta\delta = 25\,\mathrm{mm}$
- Capacidade insuficiente das estacas
- Necessidade de reforço das fundações

**Solução adotada**: Estacas adicionais

- Número de estacas: 2 estacas por pilar
- Diâmetro: $\phi = 0{,}5\,\mathrm{m}$
- Comprimento: $L = 20{,}0\,\mathrm{m}$
- Capacidade adicional: $Q_{ref} = 600{,}0\,\mathrm{kN}$

### 4) Reforço de Apoios

**Problemas identificados**:

- Apoios danificados
- Deslocamentos excessivos
- Necessidade de substituição

**Solução adotada**: Substituição dos apoios

- Apoios elastoméricos novos
- Dimensões: $0{,}8 \times 0{,}6 \times 0{,}4\,\mathrm{m}$
- Capacidade: $N = 2000{,}0\,\mathrm{kN}$
- Deslocamento: $\Delta H = 100{,}0\,\mathrm{mm}$

## Vinculação com Fundações e Apoios

### 1) Efeitos dos Recalques

**Recalques observados**:

- Apoio 1: $\delta_1 = 30{,}0\,\mathrm{mm}$
- Apoio 2: $\delta_2 = 15{,}0\,\mathrm{mm}$
- Apoio 3: $\delta_3 = 20{,}0\,\mathrm{mm}$

**Recalques diferenciais**:

- $\Delta\delta_{12} = 30{,}0 - 15{,}0 = 15{,}0\,\mathrm{mm}$
- $\Delta\delta_{23} = 15{,}0 - 20{,}0 = -5{,}0\,\mathrm{mm}$

**Efeitos na estrutura**:

- Momentos adicionais: $M_{adic} = 50{,}0\,\mathrm{kN \cdot m}$
- Cortantes adicionais: $V_{adic} = 20{,}0\,\mathrm{kN}$
- Flechas adicionais: $a_{adic} = 10{,}0\,\mathrm{mm}$

### 2) Verificação de Apoios

**Forças nos apoios**:

- Força vertical: $N = 1500{,}0\,\mathrm{kN}$
- Força horizontal: $H = 150{,}0\,\mathrm{kN}$
- Momento: $M = 75{,}0\,\mathrm{kN \cdot m}$

**Verificação de capacidade**:

- Tensão de compressão: $\sigma_c = 3125{,}0\,\mathrm{kPa} < \sigma_{c,adm} = 10000{,}0\,\mathrm{kPa}$ ✓
- Tensão de cisalhamento: $\tau = 312{,}5\,\mathrm{kPa} < \tau_{adm} = 1000{,}0\,\mathrm{kPa}$ ✓
- Deslocamento horizontal: $\Delta H = 50{,}0\,\mathrm{mm} < \Delta H_{adm} = 100{,}0\,\mathrm{mm}$ ✓

## Verificação Mínima Pós-Intervenção

### 1) Verificações Estruturais

**Capacidade à flexão**:
$$M_{Rd,ref} = 1500{,}0\,\mathrm{kN \cdot m} \geq M_{Ed} = 1500{,}0\,\mathrm{kN \cdot m}$$

Condição atendida (✓).

**Capacidade ao cisalhamento**:
$$V_{Rd,ref} = 400{,}0\,\mathrm{kN} \geq V_{Ed} = 400{,}0\,\mathrm{kN}$$

Condição atendida (✓).

**Estabilidade global**:
$$\gamma_{est} = \frac{M_{inst}}{M_{Ed}} = \frac{2000{,}0}{1500{,}0} = 1{,}33 > 1{,}0$$

Condição atendida (✓).

**Fissuração**:
$$w_k = 0{,}3\,\mathrm{mm} < w_{lim} = 0{,}4\,\mathrm{mm}$$

Condição atendida (✓).

## Interpretação dos Resultados

- A combinação de reforços (flexão, cisalhamento, apoios) responde aos achados.
- Verificações pós-obra asseguram desempenho e segurança mínimos.
- Monitoramento fecha o ciclo, reduz incertezas e orienta manutenção.

## Metodologia de Trabalho

1. Inspeção e diagnóstico: levantamento, classificação e quantificação de danos.
2. Definição de estratégias de reforço por elemento e por sistema.
3. Verificações pós-intervenção com critérios mínimos e ELS.
4. Planejamento de monitoramento: parâmetros, frequência e responsabilidades.

## Exercícios Propostos

- Construa uma árvore de decisão de reforços para três patologias dominantes.
- Elabore um plano de monitoramento com parâmetros e periodicidade.
- Proponha indicadores para avaliar sucesso das intervenções em 1 e 3 anos.

### 2) Verificações de Durabilidade

**Proteção contra corrosão**:

- Aplicação de revestimento protetor
- Verificação da aderência
- Monitoramento da corrosão
- Inspeção periódica

**Drenagem**:

- Limpeza de pontos de drenagem
- Verificação da eficiência
- Reparo de vazamentos
- Monitoramento contínuo

**Impermeabilização**:

- Aplicação de manta asfáltica
- Verificação da continuidade
- Reparo de danos
- Monitoramento periódico

### 3) Verificações de Execução

**Qualidade dos materiais**:

- Ensaios de resistência do concreto
- Verificação da armadura
- Controle de qualidade
- Certificação dos materiais

**Posicionamento das armaduras**:

- Verificação das dimensões
- Controle da cobertura
- Verificação da ancoragem
- Controle de qualidade

**Aderência do reforço**:

- Ensaios de aderência
- Verificação da continuidade
- Controle de qualidade
- Monitoramento pós-aplicação

## Evitando Sobreposição com Outros Casos

### Diferenças com Fadiga (Aula 4)

- **Fadiga**: deterioração por ciclos de carga
- **Inspeção**: identificação de patologias

### Diferenças com Acidentes (Aula 8)

- **Acidentes**: falhas súbitas
- **Inspeção**: identificação precoce de problemas

### Diferenças com Patologias (Aula 11)

- **Patologias**: tipos de deterioração
- **Inspeção**: metodologia de identificação

## Lições Aprendidas

### 1) Importância da Inspeção

- Inspeção periódica é fundamental
- Identificação precoce de problemas
- Programa de monitoramento
- Registro de patologias

### 2) Efeitos da Deterioração

- Redução significativa da capacidade
- Necessidade de reforço estrutural
- Comprometimento da segurança
- Aumento dos custos de manutenção

### 3) Necessidade de Reforço

- Reforço adequado é essencial
- Verificação de capacidade pós-reforço
- Monitoramento contínuo
- Manutenção preventiva

## Recomendações Práticas

### Para Estruturas Existentes

- Implementar programa de inspeção
- Identificar patologias precocemente
- Reparar danos adequadamente
- Monitorar comportamento estrutural

### Para Projetos Novos

- Considerar durabilidade
- Prever manutenção
- Usar proteção adequada
- Monitorar comportamento

### Para Manutenção

- Inspeção periódica obrigatória
- Identificação precoce de patologias
- Reparo adequado de danos
- Monitoramento estrutural

## Conclusões

O estudo demonstra a importância da inspeção periódica e a necessidade de reforço estrutural para garantir a segurança. As principais patologias identificadas são:

**Principais achados**:

- 30% de corrosão da armadura
- 40% de delaminação do concreto
- 90% de fissuras de flexão
- Necessidade de reforço significativo

**Recomendações**:

- Programa de inspeção periódica
- Identificação precoce de patologias
- Reforço estrutural adequado
- Monitoramento contínuo
- Manutenção preventiva

---

## Referências e Leitura Complementar

### Referências do Estudo

- **Artigo Principal**: EngEVista/UFF — Patologias e inspeção de pontes em concreto armado: estudo de caso da Ponte Gov. Magalhães Pinto (MG), 2018
- **Link**: <https://periodicos.uff.br/engevista/article/download/27125/16562/98638>

### Literatura Recomendada

- HIBBELER, R. C. *Resistência dos Materiais*. 7ª ed. São Paulo: Pearson, 2010.
- SUSSEKIND, J. C. *Curso de Análise Estrutural*. 8ª ed. São Paulo: Globo, 1994.
- COLLINS, M. P.; MITCHELL, D. *Prestressed Concrete Structures*. Prentice Hall, 1991.
