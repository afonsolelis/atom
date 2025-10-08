# Aula 5: Técnicas de Refinamento de Prompts - Zero-Shot

## Objetivo da Aula
Dominar a técnica de zero-shot prompting e aprender estratégias para obter respostas precisas sem necessidade de exemplos prévios. Ao final, o aluno deverá ser capaz de desenhar prompts zero‑shot com instruções claras, formatar saídas auditáveis e comparar seu desempenho com outras técnicas.

## 1. Conceito de Zero-Shot Prompting

### Definição
> **Zero-shot prompting** é a capacidade de modelos de linguagem responderem corretamente a tarefas nunca vistas durante o treinamento, usando apenas instruções contextuais claras.

### Características Principais
- **Sem exemplos**: Não requer demonstrações prévias
- **Generalização**: Capacidade de aplicar conhecimento a novos domínios
- **Contexto rico**: Depende de instruções detalhadas e específicas

## 2. Estratégias para Prompts Zero-Shot Eficazes

### Elementos Essenciais
- **Clareza absoluta**: Instruções inequívocas sobre o que fazer
- **Contexto completo**: Todas as informações necessárias fornecidas
- **Especificidade**: Detalhes que guiam a resposta desejada
- **Persona definida**: "Você é um especialista em..."

### Estrutura Recomendada
```
[Persona/Contexto] + [Tarefa Específica] + [Detalhes Técnicos] + [Formato Esperado]
```

### Boas Práticas e Anti‑padrões (Zero‑shot)
**Boas Práticas**
- Enunciar explicitamente critérios de aceitação (o que é “bom” como saída)
- Delimitar escopo: foco em uma tarefa por vez
- Declarar formato: listas, tabelas, JSON, unidades

**Anti‑padrões**
- Pedir “tudo” de uma vez sem hierarquia
- Omitir dados críticos (unidades, hipóteses)
- Ambiguidade em termos técnicos

## 3. Exemplos Práticos em Engenharia

### Exemplo 1 - Análise Estrutural
```
**Contexto:** Você é um engenheiro estrutural experiente especializado em análise de vigas.
**Tarefa:** Calcule a reação de apoio para uma viga biapoiada de 8 metros com carga distribuída uniforme de 3 kN/m.
**Dados técnicos:**
- Comprimento L = 8 m
- Carga distribuída q = 3 kN/m
- Apoios simples nas extremidades
**Formato:** Mostre os cálculos passo a passo usando equações de equilíbrio estático e apresente o resultado final.
```

### Exemplo 2 - Dimensionamento de Componentes
```
**Contexto:** Você é um engenheiro mecânico especialista em dimensionamento de eixos.
**Tarefa:** Determine o diâmetro mínimo necessário para um eixo de aço que transmite 15 kW a 1800 rpm.
**Dados técnicos:**
- Potência P = 15 kW
- Velocidade angular ω = 1800 rpm
- Material: aço com tensão admissível τ = 40 MPa
**Formato:** Use a fórmula de torção e mostre todos os cálculos intermediários.
```

### Exemplo 3 - Otimização de Processos
```
**Contexto:** Você é um engenheiro de produção especializado em otimização de processos.
**Tarefa:** Sugira melhorias para reduzir o tempo de ciclo em uma linha de produção de peças metálicas.
**Dados técnicos:**
- Tempo atual: 45 segundos por peça
- Objetivo: reduzir para 35 segundos
- Processo atual: corte, dobra, solda, inspeção
**Formato:** Liste 3 melhorias específicas com estimativa de redução de tempo para cada uma.
```

## 4. Aplicações Específicas por Área

### Engenharia Civil
- **Análise de estruturas**: Cálculo de reações, momentos, deformações
- **Dimensionamento**: Determinação de seções transversais
- **Verificação normativa**: Aplicação de códigos técnicos

### Engenharia Elétrica
- **Análise de circuitos**: Cálculos de corrente, tensão, potência
- **Dimensionamento**: Seleção de componentes elétricos
- **Otimização energética**: Melhorias em sistemas elétricos

### Engenharia Mecânica
- **Análise de elementos**: Cálculos de tensão, deformação
- **Dimensionamento**: Determinação de geometrias ótimas
- **Termodinâmica**: Análise de ciclos e processos

## 5. Comparação com Outras Técnicas

### Zero-Shot vs Few-Shot
| Aspecto | Zero-Shot | Few-Shot |
|---------|-----------|----------|
| **Exemplos** | Nenhum necessário | 2-3 exemplos |
| **Flexibilidade** | Alta (novos domínios) | Média (dentro do padrão) |
| **Precisão** | Depende da clareza | Geralmente mais precisa |
| **Esforço** | Menos exemplos | Mais exemplos |

### Quando Usar Cada Técnica
- **Zero-Shot**: Problemas únicos, contextos novos, rapidez
- **Few-Shot**: Padrões consistentes, maior precisão necessária

### Métricas de Avaliação
- Taxa de acerto em tarefas factuais
- Conformidade com formato solicitado
- Consistência entre execuções (mesmo contexto)
- Tempo para convergência (iterações necessárias)

## 6. Atividade Prática (5 minutos)
**Exercício Individual**: Crie um prompt zero-shot para resolver um problema técnico da sua área de engenharia. Teste mentalmente e identifique pontos de melhoria.

## 7. Para a Próxima Aula
Pratique criando prompts zero-shot para diferentes tipos de problemas técnicos e observe como pequenas mudanças afetam as respostas.

---
**Próxima Aula**: Técnicas de refinamento de prompts (few-shot e chain-of-thought)
