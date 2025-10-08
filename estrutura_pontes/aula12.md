# Aula 12: Estudo de Caso Nacional – Patologias em Pontes (BR-423/AL)

### Esquema do caso (SVG)
<img src="./assets/aula12_ponte.svg" alt="Esquema: patologias em pontes de concreto armado" width="760" />

Leitura do esquema:
- Tipos de patologias observadas
- Análise quantitativa da degradação
- Efeitos na capacidade estrutural
- Necessidade de reforço

## Referência do Estudo
**Artigo:** Vasconcelos, T. — Análise das manifestações patológicas em pontes de concreto armado: estudo de caso na BR-423/AL, 2018  
**Link:** https://www.repositorio.ufal.br/bitstream/riufal/3747/1/An%C3%A1lise%20das%20manifesta%C3%A7%C3%B5es%20patol%C3%B3gicas%20em%20pontes%20de%20concreto%20armado%3A%20estudo%20de%20caso.pdf

## Contexto do Estudo de Caso

### Ponte Analisada
- **Localização**: BR-423/AL (Alagoas)
- **Período de construção**: 1995-1998
- **Idade no estudo**: 20-23 anos
- **Vão**: $L = 30\,\mathrm{m}$ (viga de concreto armado)
- **Ambiente**: costeiro (agressivo)
- **Tráfego**: intenso, com predominância de veículos pesados

### Problema Identificado
A ponte apresentava manifestações patológicas significativas após 20 anos de serviço, incluindo fissuras, corrosão da armadura, delaminação do concreto e comprometimento da capacidade estrutural. O estudo analisou as causas e propôs soluções de reforço.

## Patologias Observadas

### 1) Fissuras de Flexão

**Localização**: Meio do vão das vigas principais
**Características**:
- Abertura: $w = 0{,}4\,\mathrm{mm}$ (máxima)
- Profundidade: $d = 15\,\mathrm{mm}$
- Orientação: paralela ao eixo da viga
- Distribuição: 80% das vigas

**Causas identificadas**:
- Sobrecarga estrutural
- Retração do concreto
- Variações térmicas
- Fadiga por cargas cíclicas

**Efeitos na estrutura**:
- Redução da rigidez
- Penetração de agentes agressivos
- Aceleração da corrosão
- Comprometimento da durabilidade

### 2) Corrosão da Armadura

**Localização**: Região de momento máximo
**Características**:
- Taxa de corrosão: $\eta_{corr} = 25\%$
- Profundidade de carbonatação: $d_{carb} = 30\,\mathrm{mm}$
- Perda de seção: $\Delta A_s = 0{,}25 \times A_{s,0}$
- Distribuição: 60% das vigas

**Causas identificadas**:
- Penetração de cloretos
- Carbonatação do concreto
- Falta de proteção da armadura
- Ambiente agressivo (marinho)

**Efeitos na estrutura**:
- Redução da capacidade resistente
- Perda de aderência
- Comprometimento da segurança
- Necessidade de reforço

### 3) Delaminação do Concreto

**Localização**: Superfície inferior das vigas
**Características**:
- Área afetada: $A_{del} = 35\%$ da superfície
- Espessura perdida: $t_{del} = 15\,\mathrm{mm}$
- Redução da seção: $\Delta A_c = 0{,}35 \times A_c$
- Distribuição: 70% das vigas

**Causas identificadas**:
- Falta de aderência
- Retração diferencial
- Variações térmicas
- Cargas cíclicas

**Efeitos na estrutura**:
- Redução da seção efetiva
- Comprometimento da durabilidade
- Necessidade de reparo
- Redução da capacidade

## Análise Quantitativa da Corrosão

### 1) Perda de Seção da Armadura

**Área original da armadura**:
$$A_{s,0} = 25 \times \frac{\pi \times 2{,}5^2}{4} = 122{,}7\,\mathrm{cm^2}$$

**Área efetiva após corrosão**:
$$A_{s,ef} = A_{s,0} (1 - \eta_{corr}) = 122{,}7 \times (1 - 0{,}25) = 92{,}0\,\mathrm{cm^2}$$

**Redução da capacidade**:
$$\Delta M_{Rd} = (A_{s,0} - A_{s,ef}) f_{yd} (d - 0{,}4x)$$

$$\Delta M_{Rd} = (122{,}7 - 92{,}0) \times 435 \times (1{,}40 - 0{,}4 \times 0{,}20) = 30{,}7 \times 435 \times 1{,}32 = 17634{,}2\,\mathrm{kN \cdot cm}$$

$$\Delta M_{Rd} = 176{,}3\,\mathrm{kN \cdot m}$$

### 2) Efeito na Capacidade Resistente

**Momento resistente original**:
$$M_{Rd,0} = A_{s,0} f_{yd} (d - 0{,}4x) = 122{,}7 \times 435 \times (1{,}40 - 0{,}4 \times 0{,}20) = 122{,}7 \times 435 \times 1{,}32 = 70447{,}4\,\mathrm{kN \cdot cm}$$

$$M_{Rd,0} = 704{,}5\,\mathrm{kN \cdot m}$$

**Momento resistente efetivo**:
$$M_{Rd,ef} = M_{Rd,0} - \Delta M_{Rd} = 704{,}5 - 176{,}3 = 528{,}2\,\mathrm{kN \cdot m}$$

**Momento de cálculo**:
$$M_{Ed} = \frac{g L^2}{8} + \frac{q L^2}{8} = \frac{35{,}0 \times 900}{8} + \frac{5{,}0 \times 900}{8} = 3937{,}5 + 562{,}5 = 4500{,}0\,\mathrm{kN \cdot m}$$

**Verificação**:
$$M_{Ed} = 4500{,}0\,\mathrm{kN \cdot m} > M_{Rd,ef} = 528{,}2\,\mathrm{kN \cdot m}$$ ✗

**Resultado**: A estrutura não atende aos critérios de segurança.

## Relação com Drenagem e Ambiente

### 1) Problemas de Drenagem

**Drenagem obstruída**:
- 80% dos pontos de drenagem
- Acúmulo de água em 60% da superfície
- Vazamentos em 40% das juntas

**Efeitos na deterioração**:
- Aceleração da corrosão
- Penetração de agentes agressivos
- Redução da durabilidade
- Comprometimento da estrutura

### 2) Ambiente Agressivo

**Fatores ambientais**:
- Proximidade do mar (sal)
- Umidade relativa alta (80%)
- Temperatura média alta (28°C)
- Poluição atmosférica

**Efeitos na corrosão**:
- Penetração de cloretos
- Carbonatação acelerada
- Redução do pH do concreto
- Aceleração da corrosão

### 3) Manutenção Inadequada

**Falta de manutenção**:
- Ausência de programa de inspeção
- Falta de limpeza de drenagem
- Ausência de proteção contra corrosão
- Falta de reparo de danos

**Efeitos na deterioração**:
- Aceleração das patologias
- Comprometimento da segurança
- Redução da vida útil
- Necessidade de reforço

## Proposta de Verificação de MRd Pós-Degradação

### 1) Metodologia de Verificação

**Parâmetros a considerar**:
- Taxa de corrosão da armadura
- Área de delaminação
- Redução da seção efetiva
- Perda de aderência

**Cálculo do momento resistente**:
$$M_{Rd,ef} = A_{s,ef} f_{yd} (d_{ef} - 0{,}4x_{ef})$$

Onde:
- $A_{s,ef}$ = área efetiva da armadura
- $d_{ef}$ = altura útil efetiva
- $x_{ef}$ = posição da linha neutra efetiva

### 2) Verificação de Segurança

**Coeficiente de segurança**:
$$\gamma = \frac{M_{Rd,ef}}{M_{Ed}} = \frac{528{,}2}{4500{,}0} = 0{,}12$$

**Verificação**:
$$\gamma = 0{,}12 < 1{,}0$$ ✗

**Resultado**: A estrutura não atende aos critérios de segurança.

### 3) Necessidade de Reforço

**Reforço necessário**:
$$M_{Rd,ref} = M_{Ed} - M_{Rd,ef} = 4500{,}0 - 528{,}2 = 3971{,}8\,\mathrm{kN \cdot m}$$

**Área de armadura adicional**:
$$A_{s,ref} = \frac{M_{Rd,ref}}{f_{yd} (d - 0{,}4x)} = \frac{3971{,}8}{435 \times (1{,}40 - 0{,}4 \times 0{,}20)} = \frac{3971{,}8}{435 \times 1{,}32} = 6{,}92\,\mathrm{m^2}$$

$$A_{s,ref} = 692{,}0\,\mathrm{cm^2}$$

## Evitando Sobreposição com Outros Casos

### Diferenças com Impactos Dinâmicos (Aulas 9-10)
- **Impactos dinâmicos**: efeitos de cargas móveis
- **Patologias**: deterioração gradual por agentes agressivos

### Diferenças com Acidentes (Aula 8)
- **Acidentes**: falhas súbitas
- **Patologias**: deterioração gradual

### Diferenças com Fadiga (Aula 4)
- **Fadiga**: deterioração por ciclos de carga
- **Patologias**: deterioração por agentes agressivos

## Lições Aprendidas

### 1) Importância da Drenagem
- Drenagem adequada é fundamental
- Falta de drenagem acelera a deterioração
- Manutenção da drenagem é essencial
- Proteção contra infiltração é necessária

### 2) Efeitos do Ambiente
- Ambiente agressivo acelera a corrosão
- Proteção adequada é necessária
- Monitoramento é essencial
- Manutenção preventiva é fundamental

### 3) Necessidade de Reforço
- Estruturas degradadas precisam de reforço
- Verificação de capacidade é essencial
- Reforço deve ser adequado
- Monitoramento pós-reforço é necessário

## Recomendações Práticas

### Para Estruturas Existentes
- Implementar programa de inspeção
- Identificar patologias precocemente
- Reparar danos adequadamente
- Monitorar comportamento estrutural

### Para Projetos Novos
- Considerar ambiente agressivo
- Usar proteção adequada
- Prever manutenção
- Monitorar durabilidade

### Para Manutenção
- Inspeção periódica obrigatória
- Identificação precoce de patologias
- Reparo adequado de danos
- Monitoramento estrutural

## Conclusões

O estudo demonstra a importância da identificação precoce de patologias e a necessidade de reforço estrutural para garantir a segurança. As principais patologias identificadas são:

**Principais achados**:
- 25% de corrosão da armadura
- 35% de delaminação do concreto
- 80% de problemas de drenagem
- Necessidade de reforço significativo

**Recomendações**:
- Programa de inspeção periódica
- Manutenção adequada da drenagem
- Proteção contra corrosão
- Reforço estrutural quando necessário

---

## Referências e Leitura Complementar

### Referências do Estudo
- **Artigo Principal**: Vasconcelos, T. — Análise das manifestações patológicas em pontes de concreto armado: estudo de caso na BR-423/AL, 2018
- **Link**: https://www.repositorio.ufal.br/bitstream/riufal/3747/1/An%C3%A1lise%20das%20manifesta%C3%A7%C3%B5es%20patol%C3%B3gicas%20em%20pontes%20de%20concreto%20armado%3A%20estudo%20de%20caso.pdf

### Literatura Recomendada
- HIBBELER, R. C. *Resistência dos Materiais*. 7ª ed. São Paulo: Pearson, 2010.
- SUSSEKIND, J. C. *Curso de Análise Estrutural*. 8ª ed. São Paulo: Globo, 1994.
- COLLINS, M. P.; MITCHELL, D. *Prestressed Concrete Structures*. Prentice Hall, 1991.