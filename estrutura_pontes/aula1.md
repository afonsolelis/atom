# Aula 1: Esforços Internos e Equilíbrio Estrutural

## Objetivos da Aula

Ao final desta aula, o aluno será capaz de:
- Compreender os conceitos fundamentais de esforços internos em estruturas
- Calcular reações de apoio em vigas simplesmente apoiadas
- Determinar diagramas de cortante e momento fletor
- Aplicar as relações diferenciais entre esforços
- Identificar valores máximos para dimensionamento

---

## 1. Introdução Teórica

### 1.1 Esforços Internos Fundamentais

Em estruturas de concreto armado, três esforços internos são fundamentais:

- **Esforço Normal (N)**: Força axial atuando perpendicularmente à seção transversal
  - $N > 0$: tração (tendência a alongar o elemento)
  - $N < 0$: compressão (tendência a encurtar o elemento)

- **Esforço Cortante (V)**: Força perpendicular ao eixo longitudinal da viga
  - Convenção: $V > 0$ quando tende a girar o elemento no sentido horário
  - Relacionado ao cisalhamento na seção

- **Momento Fletor (M)**: Momento que tende a fletir a viga
  - Convenção: $M > 0$ quando produz "sorriso" (concavidade para cima)
  - $M < 0$ quando produz "carranca" (concavidade para baixo)

### 1.2 Relações Diferenciais Fundamentais

As relações entre esforços são governadas pelas equações diferenciais:

$$\frac{dM}{dx} = V$$

$$\frac{dV}{dx} = -q(x)$$

Onde:
- $q(x)$ é a carga distribuída por unidade de comprimento
- Cargas concentradas geram descontinuidades (saltos) nos diagramas

### 1.3 Equilíbrio Global

Para uma estrutura em equilíbrio estático:

$$\sum F_x = 0 \quad \sum F_y = 0 \quad \sum M = 0$$

---

## 2. Estudo de Caso: Ponte Rodoviária

### 2.1 Descrição do Problema

**Estrutura**: Ponte rodoviária de vão único com viga simplesmente apoiada em concreto armado

**Dados do projeto**:
- Vão: $L = 6\,\mathrm{m}$
- Carga distribuída equivalente: $q = 30\,\mathrm{kN/m}$
  - Inclui: peso próprio da viga + tabuleiro + revestimento + guarda-corpo
- Carga concentrada (eixo de veículo): $P = 30\,\mathrm{kN}$ aplicada em $x = L/2 = 3\,\mathrm{m}$

### 2.2 Esquema Estrutural

<img src="https://res.cloudinary.com/dyhjjms8y/image/upload/v1760304363/estrutura_pontes/aula1_ponte.svg" alt="Esquema: viga simplesmente apoiada com q e P" width="760" />

**Interpretação do esquema**:
- Apoios A e B com reações $R_A$ e $R_B$ (sentido positivo para cima)
- Carga distribuída $q$ atuando em todo o vão
- Carga concentrada $P$ aplicada no centro do vão
- Sistema de coordenadas: eixo $x$ cresce da esquerda para a direita

---

## 3. Solução Passo a Passo

### 3.1 Cálculo das Reações de Apoio

**Método 1: Por simetria**

Devido à simetria do carregamento, as reações são iguais:

$$R_A = R_B = \frac{\text{Carga total}}{2} = \frac{qL + P}{2}$$

$$R_A = R_B = \frac{30 \times 6 + 30}{2} = \frac{180 + 30}{2} = 105\,\mathrm{kN}$$

**Método 2: Por equilíbrio de momentos**

Tomando momento em relação ao apoio A:

$$\sum M_A = 0$$

$$R_B \cdot L - qL \cdot \frac{L}{2} - P \cdot \frac{L}{2} = 0$$

$$R_B = \frac{qL^2/2 + PL/2}{L} = \frac{qL}{2} + \frac{P}{2} = 90 + 15 = 105\,\mathrm{kN}$$

**Verificação**: $\sum F_y = R_A + R_B - qL - P = 105 + 105 - 180 - 30 = 0$ ✓

### 3.2 Diagrama de Esforço Cortante V(x)

**Trecho 1: $0 \leq x < 3\,\mathrm{m}$**

$$V(x) = R_A - qx = 105 - 30x$$

- Em $x = 0$: $V(0) = 105\,\mathrm{kN}$
- Em $x = 3^-$: $V(3^-) = 105 - 90 = 15\,\mathrm{kN}$

**Descontinuidade em $x = 3\,\mathrm{m}$**

A carga concentrada $P$ causa um salto no diagrama de cortante:

$$V(3^+) = V(3^-) - P = 15 - 30 = -15\,\mathrm{kN}$$

**Trecho 2: $3 < x \leq 6\,\mathrm{m}$**

$$V(x) = R_A - qx - P = 105 - 30x - 30 = 75 - 30x$$

- Em $x = 6$: $V(6) = 75 - 180 = -105\,\mathrm{kN}$

**Características do diagrama V(x)**:
- Linear por trechos com inclinação $-q = -30\,\mathrm{kN/m}$
- Salto de $-P = -30\,\mathrm{kN}$ em $x = 3\,\mathrm{m}$
- Simétrico: $V(0) = -V(6) = 105\,\mathrm{kN}$

### 3.3 Diagrama de Momento Fletor M(x)

**Trecho 1: $0 \leq x \leq 3\,\mathrm{m}$**

$$M(x) = R_A \cdot x - \frac{qx^2}{2} = 105x - 15x^2$$

- Em $x = 0$: $M(0) = 0$ (apoio simples)
- Em $x = 3$: $M(3) = 105 \times 3 - 15 \times 9 = 315 - 135 = 180\,\mathrm{kN \cdot m}$

**Trecho 2: $3 \leq x \leq 6\,\mathrm{m}$**

$$M(x) = R_A \cdot x - \frac{qx^2}{2} - P(x-3) = 105x - 15x^2 - 30(x-3)$$

$$M(x) = 105x - 15x^2 - 30x + 90 = 90 + 75x - 15x^2$$

- Em $x = 6$: $M(6) = 90 + 450 - 540 = 0$ ✓ (apoio simples)

**Verificação de continuidade em $x = 3\,\mathrm{m}$**:
- $M(3^-) = 105 \times 3 - 15 \times 9 = 180\,\mathrm{kN \cdot m}$
- $M(3^+) = 90 + 75 \times 3 - 15 \times 9 = 90 + 225 - 135 = 180\,\mathrm{kN \cdot m}$ ✓

### 3.4 Valores Máximos e Pontos Críticos

**Momento máximo**:

O momento máximo ocorre onde $V(x) = 0$. No caso simétrico, isso acontece em $x = 3\,\mathrm{m}$:

$$M_{\max} = 180\,\mathrm{kN \cdot m}$$

**Decomposição do momento máximo**:

$$M_{\max} = \frac{qL^2}{8} + \frac{PL}{4} = \frac{30 \times 36}{8} + \frac{30 \times 6}{4} = 135 + 45 = 180\,\mathrm{kN \cdot m}$$

- Contribuição da carga distribuída: $135\,\mathrm{kN \cdot m}$
- Contribuição da carga concentrada: $45\,\mathrm{kN \cdot m}$

**Cortante máximo**:

$$|V|_{\max} = R_A = R_B = 105\,\mathrm{kN}$$

---

## 4. Interpretação dos Resultados

### 4.1 Características dos Diagramas

**Diagrama de Cortante V(x)**:
- Forma linear por trechos
- Inclinação constante igual a $-q$
- Descontinuidade (salto) em cargas concentradas
- Valores máximos nos apoios

**Diagrama de Momento M(x)**:
- Forma parabólica por trechos
- Ponto de máximo onde $V = 0$
- Valores nulos nos apoios simples
- Continuidade em pontos de cargas concentradas

### 4.2 Aplicação Prática

**Para dimensionamento da viga**:
- **Momento máximo**: $M_{\max} = 180\,\mathrm{kN \cdot m}$ → dimensionamento da armadura longitudinal
- **Cortante máximo**: $V_{\max} = 105\,\mathrm{kN}$ → dimensionamento da armadura transversal (estribos)

---

## 5. Metodologia de Cálculo

### 5.1 Sequência Recomendada

1. **Calcular reações de apoio** usando equilíbrio global
2. **Traçar diagrama de cortante**:
   - Começar pelos apoios
   - Aplicar inclinação $-q$ para cargas distribuídas
   - Aplicar saltos para cargas concentradas
3. **Traçar diagrama de momento**:
   - Integrar o diagrama de cortante
   - Aplicar condições de contorno
   - Verificar continuidade

### 5.2 Verificações Importantes

- **Equilíbrio global**: $\sum F_y = 0$ e $\sum M = 0$
- **Continuidade**: $M$ deve ser contínuo em pontos de cargas concentradas
- **Condições de contorno**: $M = 0$ em apoios simples
- **Simetria**: verificar se os resultados são coerentes com a simetria do problema

---

## 6. Erros Comuns e Cuidados

### 6.1 Erros Frequentes

- ❌ **Misturar convenções de sinais** ao longo do cálculo
- ❌ **Esquecer saltos** no diagrama de cortante em cargas concentradas
- ❌ **Aplicar incorretamente** as condições de contorno do momento
- ❌ **Não verificar** o equilíbrio global após o cálculo

### 6.2 Dicas Práticas

- ✅ **Mantenha consistência** nas convenções de sinais
- ✅ **Verifique sempre** o equilíbrio global
- ✅ **Use a simetria** quando aplicável para simplificar cálculos
- ✅ **Esboce os diagramas** para verificar a coerência física

---

## 7. Exercícios Propostos

### 7.1 Variações do Caso Base

1. **Carga concentrada fora do centro**: $P = 30\,\mathrm{kN}$ em $x = 2\,\mathrm{m}$
2. **Carga distribuída variável**: $q(x) = 20 + 10x\,\mathrm{kN/m}$
3. **Viga com balanço**: $L = 8\,\mathrm{m}$ com balanço de $2\,\mathrm{m}$

### 7.2 Questões para Reflexão

- Como o diagrama de momento muda se a carga concentrada for aplicada em $x = 2\,\mathrm{m}$?
- Qual seria o efeito de uma carga distribuída triangular?
- Como verificar se os diagramas estão corretos?

---

## 8. Próximos Passos

### 8.1 Aplicações Imediatas

- Dimensionamento de armaduras longitudinais e transversais
- Verificação de tensões de cisalhamento
- Análise de flechas e deformações

### 8.2 Desenvolvimentos Futuros

- **Aula 2**: Tipos estruturais e trajetórias de carga
- **Aula 3**: Vigas contínuas e hiperestáticas
- **Aula 4**: Análise de pórticos planos

---

## 9. Referências e Fórmulas Úteis

### 9.1 Fórmulas de Referência

**Viga simplesmente apoiada com carga uniforme**:
$$M_{\max} = \frac{qL^2}{8} \quad V_{\max} = \frac{qL}{2}$$

**Viga simplesmente apoiada com carga concentrada no centro**:
$$M_{\max} = \frac{PL}{4} \quad V_{\max} = \frac{P}{2}$$

**Combinação de cargas**:
$$M_{\max} = \frac{qL^2}{8} + \frac{PL}{4}$$

### 9.2 Bibliografia Recomendada

- HIBBELER, R. C. *Resistência dos Materiais*. 7ª ed. São Paulo: Pearson, 2010.
- SUSSEKIND, J. C. *Curso de Análise Estrutural*. 8ª ed. São Paulo: Globo, 1994.
- NBR 6118:2014 - Projeto de estruturas de concreto - Procedimento.

---

*Esta aula estabelece os fundamentos para o dimensionamento de estruturas de concreto armado. Pratique os exercícios propostos e consulte as referências para aprofundar seus conhecimentos.*