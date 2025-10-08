# Aula 6: Técnicas Avançadas de Prompting - Few-Shot e Chain-of-Thought

## Objetivo da Aula
Dominar técnicas avançadas de prompting que utilizam exemplos e raciocínio estruturado para obter respostas mais precisas e elaboradas.

## 1. Few-Shot Prompting

### Conceito e Aplicação
> **Few-shot prompting** fornece ao modelo alguns exemplos (2-5) de como realizar a tarefa desejada, permitindo melhor compreensão do padrão esperado.

### Elementos Essenciais
- **Exemplos relevantes**: Casos similares ao problema atual
- **Formato consistente**: Mesmo padrão de entrada e saída
- **Variação controlada**: Exemplos que cobrem diferentes cenários
- **Contexto mínimo**: Apenas o necessário para demonstrar o padrão

### Estrutura de Prompt Few-Shot
```
[Contexto geral]
[Exemplo 1 - Entrada]
[Exemplo 1 - Saída]
[Exemplo 2 - Entrada]
[Exemplo 2 - Saída]
[Exemplo 3 - Entrada]
[Exemplo 3 - Saída]
[Seu problema - Entrada]
[Seu problema - Saída (em branco para o modelo completar)]
```

## 2. Exemplos Práticos em Engenharia

### Exemplo 1 - Análise Estrutural (Few-Shot)
```
**Contexto:** Calcule as reações de apoio para vigas biapoiadas com cargas concentradas.

**Exemplo 1:**
Entrada: Viga de 4m com carga concentrada de 10kN no meio.
Saída: Reações: RA = RB = 5kN (simetria)

**Exemplo 2:**
Entrada: Viga de 6m com carga de 8kN a 2m da esquerda.
Saída: RA = (8kN × 4m)/6m = 5.33kN, RB = (8kN × 2m)/6m = 2.67kN

**Seu problema:**
Entrada: Viga de 5m com carga de 12kN a 1.5m da esquerda.
Saída:
```

### Exemplo 2 - Dimensionamento Mecânico (Few-Shot)
```
**Contexto:** Calcule a tensão admissível para diferentes materiais e cargas.

**Exemplo 1:**
Entrada: Eixo de aço SAE 1045, diâmetro 50mm, torque 2000Nm.
Saída: τ = (16 × 2000Nm) / (π × 50³mm) = 40.7MPa

**Exemplo 2:**
Entrada: Eixo de alumínio 6061, diâmetro 60mm, torque 1500Nm.
Saída: τ = (16 × 1500Nm) / (π × 60³mm) = 17.8MPa

**Seu problema:**
Entrada: Eixo de aço SAE 1020, diâmetro 45mm, torque 1800Nm.
Saída:
```

## 3. Chain-of-Thought Prompting

### Conceito e Benefícios
> **Chain-of-Thought (CoT)** incentiva o modelo a mostrar seu raciocínio passo a passo, melhorando a precisão em problemas complexos que requerem múltiplas etapas.

### Características
- **Raciocínio explícito**: Cada passo justificado
- **Quebra de complexidade**: Problemas divididos em etapas menores
- **Autocorreção**: Possibilidade de identificar erros no processo
- **Transparência**: Facilita auditoria do resultado

### Técnicas de CoT
- **CoT Básico**: "Pense passo a passo antes de responder"
- **CoT Estruturado**: Divisão explícita em etapas numeradas
- **CoT com Few-Shot**: Combinação de exemplos e raciocínio

## 4. Exemplos de Chain-of-Thought

### Exemplo 1 - Problema Multi-etapa (Engenharia Civil)
```
**Contexto:** Você é engenheiro estrutural. Resolva este problema mostrando seu raciocínio.

**Problema:** Calcule o momento máximo em uma viga de 9m com carga distribuída variável (triangular) de 0 a 6kN/m.

**Raciocínio passo a passo:**
1. Identificar o tipo de carga: triangular crescente
2. Calcular a reação total: integral da carga = (6kN/m × 9m)/2 = 27kN
3. Como é simétrico, reações RA = RB = 13.5kN
4. Escrever equação do momento fletor M(x)
5. Para carga triangular, M(x) = RA*x - (q/2)x² (onde q varia)
6. Encontrar máximo quando dM/dx = 0
7. Resolver: RA - q*x = 0 → x = RA/q_máx = 13.5/6 = 2.25m
8. Calcular M(2.25m) = 13.5×2.25 - (6/2)×2.25² = 30.375 - 15.1875 = 15.1875kNm

**Resposta final:** Momento máximo = 15.19 kNm (aproximado)
```

### Exemplo 2 - Otimização (Engenharia de Produção)
```
**Contexto:** Otimize o layout de uma fábrica considerando fluxo de materiais.

**Problema:** Reorganize 4 máquinas (A,B,C,D) para minimizar movimentação.

**Dados de fluxo (peças/dia):**
A→B: 50, A→C: 30, B→D: 40, C→D: 25

**Raciocínio passo a passo:**
1. Calcular matriz de relacionamento: A-B:50, A-C:30, B-D:40, C-D:25
2. Calcular pesos totais: A=80, B=90, C=55, D=65
3. Posicionar máquinas com maior interação próximas
4. Layout sugerido: A-B-D-C (movimentação total reduzida em 35%)

**Resposta final:** Layout ótimo: A | B | D | C
```

## 5. Quando Usar Cada Técnica

### Critérios de Escolha
- **Zero-Shot**: Problemas simples, únicos, ou quando velocidade é crítica
- **Few-Shot**: Quando há padrões consistentes e exemplos disponíveis
- **Chain-of-Thought**: Problemas complexos, multi-etapa, ou que requerem justificativa

### Combinações Híbridas
- **Few-Shot + CoT**: Exemplos seguidos de raciocínio detalhado
- **CoT Estruturado**: Numeração explícita das etapas
- **CoT com Verificação**: Incluir passo de validação do resultado

## 6. Atividade Prática (5 minutos)
**Comparação de Técnicas**: Crie o mesmo prompt técnico usando zero-shot, few-shot e chain-of-thought. Compare mentalmente os resultados esperados.

## 7. Para a Próxima Aula
Experimente combinar diferentes técnicas de prompting em problemas reais da sua área de engenharia.

---
**Próxima Aula**: Formulação de problemas complexos em etapas
