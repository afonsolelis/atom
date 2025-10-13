# Aula 3: Estrutura e Elementos de um Prompt Eficaz

## Objetivo da Aula
Aprender a construir prompts bem estruturados que gerem respostas mais precisas e úteis dos sistemas de IA. Utilizaremos nossos direcionamentos padronizados em formato JSON para manter consistência e qualidade. Ao final, o aluno deverá ser capaz de elaborar prompts auditáveis, interpretar respostas e iterar para melhoria contínua.

## 1. Conceito de Prompt Engineering

### Definição
> **Prompt Engineering** é a prática sistemática de criar instruções que otimizam as respostas de modelos de linguagem, considerando contexto, clareza e especificidade.

### Princípios Fundamentais
- **Clareza**: Instruções diretas e inequívocas
- **Contexto**: Informação suficiente para o modelo entender a tarefa
- **Especificidade**: Detalhes que guiam a resposta desejada
- **Iteração**: Processo de refinamento baseado em resultados

## 2. Elementos Essenciais de um Prompt

### Estrutura Recomendada
```
[Contexto] + [Instrução Principal] + [Exemplos] + [Restrições] + [Formatação]
```

### Componentes Detalhados

#### 1. Contexto (Setup)
- **Definição do cenário**: "Você é um engenheiro especialista em estruturas..."
- **Informações relevantes**: Dados técnicos, restrições, objetivos
- **Persona**: "Responda como um consultor sênior..."

#### 2. Instrução Principal (Task)
- **Comando claro**: "Calcule a reação de apoio..."
- **Ação específica**: "Gere uma lista de materiais..."
- **Resultado esperado**: "Explique o conceito usando analogias..."

#### 3. Exemplos (Examples)
- **Few-shot learning**: 2-3 exemplos de entrada/saída
- **Demonstração de formato**: Como estruturar a resposta
- **Casos similares**: Padrões que o modelo deve seguir

#### 4. Restrições (Constraints)
- **Limites**: "Responda em no máximo 200 palavras"
- **Exclusões**: "Não use fórmulas matemáticas"
- **Requisitos**: "Inclua referências técnicas"

#### 5. Formatação (Format)
- **Estrutura da resposta**: "Liste os itens em bullet points"
- **Estilo**: "Use linguagem técnica formal"
- **Organização**: "Divida em seções com headers"

### Métricas de Qualidade de Prompts
- Adequação: a resposta atende ao objetivo definido
- Precisão: ausência de erros factuais ou cálculos incorretos
- Completude: cobre os itens solicitados no formato pedido
- Reprodutibilidade: mesma resposta quando o contexto é controlado
- Segurança: ausência de saídas problemáticas (tóxicas, PII)

## 3. Exemplos Práticos

### Exemplo Básico - Consulta Técnica
```
**Contexto:** Você é um engenheiro estrutural experiente.
**Tarefa:** Calcule a reação de apoio para uma viga biapoiada de 6m com carga distribuída de 2kN/m.
**Formato:** Mostre os cálculos passo a passo e o resultado final.
```

### Exemplo Avançado - Análise Comparativa
#### Notas de Raciocínio
- O exemplo explicita critérios e limitações, reduzindo ambiguidade
- A estrutura com tópicos obriga a cobrir todos os itens pedidos
- A restrição de palavras força concisão e priorização de conteúdo
```
**Contexto:** Compare três métodos de análise estrutural.
**Exemplos:**
Método 1 - Forças: Calcula reações de apoio
Método 2 - Energia: Minimiza energia potencial
Método 3 - Finite Element: Discretiza em elementos
**Tarefa:** Explique vantagens e desvantagens de cada método para análise de pontes.
**Restrições:** Limite a 150 palavras por método.
```

## 4. Direcionamentos Padronizados para Prompting

Para manter consistência e qualidade, utilizamos direcionamentos em formato JSON que definem padrões para estrutura de aulas e elementos de prompting.

### Template de Prompt Estruturado
```markdown
**Contexto:** [Definir cenário e persona]

**Problema:** [Descrição clara do desafio técnico]

**Requisitos:** [Lista detalhada de especificações]

**Abordagem Sugerida:**
1. [Passo 1 com explicação]
2. [Passo 2 com justificativa]

**Formato da Resposta:**
- Use linguagem técnica apropriada
- Inclua cálculos quando necessário
- Forneça justificativas para escolhas metodológicas

**Restrições:** [Limitações ou considerações especiais]
```
## 5. Boas Práticas e Anti‑padrões

### Boas Práticas
- Indicar o papel/persona para calibrar estilo e nível técnico
- Fixar unidades e convenções para evitar inconsistências
- Pedir passo a passo quando houver cadeia de raciocínio
- Validar com caso de teste simples antes do caso completo

### Anti‑padrões a Evitar
- Prompts excessivamente longos sem hierarquia de informação
- Pedidos vagos ("explique tudo sobre…") sem objetivo concreto
- Contradições ("seja conciso, mas explique em detalhes extensos")
- Falta de checagem factual em domínios de alto risco

## 6. Erros Comuns a Evitar

### Problemas Frequentes
- **Ambiguidade**: "Calcule isso" (sem especificar método)
- **Falta de contexto**: Não definir unidades ou parâmetros
- **Instruções contraditórias**: Pedidos mutuamente exclusivos
- **Prompt muito longo**: Informação excessiva que confunde

## 7. Atividade Prática (5 minutos)
**Exercício em Pares**: Cada dupla cria um prompt para resolver um problema técnico simples. Testem e refinem com base nos resultados obtidos.

## 8. Para a Próxima Aula
Pratique criando prompts para diferentes tipos de problemas técnicos da sua área de engenharia.

---
**Próxima Aula**: Técnicas de refinamento de prompts (zero-shot)
