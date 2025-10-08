# Aula 3: Estrutura e Elementos de um Prompt Eficaz

## Objetivo da Aula
Aprender a construir prompts bem estruturados que gerem respostas mais precisas e úteis dos sistemas de IA. Utilizaremos nossos direcionamentos padronizados em formato JSON para manter consistência e qualidade.

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

## 3. Exemplos Práticos

### Exemplo Básico - Consulta Técnica
```
**Contexto:** Você é um engenheiro estrutural experiente.
**Tarefa:** Calcule a reação de apoio para uma viga biapoiada de 6m com carga distribuída de 2kN/m.
**Formato:** Mostre os cálculos passo a passo e o resultado final.
```

### Exemplo Avançado - Análise Comparativa
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

Para manter consistência e qualidade em nossos materiais, utilizamos um sistema de direcionamentos organizados em formato JSON que define padrões para estrutura de aulas, elementos de prompting e configurações técnicas.

### Direcionamentos de Estrutura
```json
{
  "estrutura_aula": {
    "ordem_secoes": [
      "Estudo de Caso",
      "Conceitos principais",
      "Exemplo prático de prompt",
      "Erros comuns",
      "Encaminhamentos"
    ],
    "descricao_pos_exemplo": true,
    "descricao_pos_exemplo_nota": "Após cada exemplo de prompt, inserir 1–2 frases explicando o raciocínio, a estratégia utilizada e como aplicar em contextos similares."
  }
}
```

### Direcionamentos para LaTeX e Formatação
```json
{
  "latex": {
    "usar_latex": true,
    "inline": "$ … $",
    "bloco": "$$ … $$",
    "elementos_prompt": ["\\text{Contexto}", "\\text{Instrução}", "\\text{Exemplo}", "\\text{Saída}"],
    "operadores": ["\\Rightarrow", "\\rightarrow", "\\text{vs}", "\\text{Ex.:}"],
    "codigo": "usar blocos de código ``` para exemplos de prompts e respostas"
  }
}
```

### Direcionamentos para Diagramas
```json
{
  "diagramas": {
    "incluir_diagrama": true,
    "arquivo_padrao": "aulaX_prompt_flow.svg",
    "insercao_markdown": "<img src=\"./aulaX_prompt_flow.svg\" alt=\"Fluxo de Prompt\" width=\"760\" />",
    "conteudo_minimo": [
      "Entrada do usuário",
      "Processamento do prompt",
      "Modelo de IA",
      "Geração de resposta",
      "Elementos de contexto (quando aplicável)",
      "Fluxo de interação"
    ]
  }
}
```

### Aplicação Prática dos Direcionamentos

#### Template de Prompt Estruturado
Baseado nos direcionamentos, aqui está um template completo:

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

#### Exemplo Aplicado - Análise Estrutural
```json
{
  "contexto": "Você é engenheiro estrutural sênior com experiência em análise de elementos finitos",
  "problema": "Calcular reações de apoio para viga biapoiada de 6m com carga distribuída variável",
  "dados_tecnicos": {
    "comprimento": "6m",
    "carga": "distribuída variável (triangular)",
    "apoios": "biapoiada (pinos)"
  },
  "objetivos": [
    "Calcular reações de apoio",
    "Determinar momento máximo",
    "Verificar critérios de segurança"
  ],
  "formato_resposta": "Mostrar cálculos passo a passo com equações de equilíbrio"
}
```

## 5. Erros Comuns a Evitar

### Problemas Frequentes
- **Ambiguidade**: "Calcule isso" (sem especificar método)
- **Falta de contexto**: Não definir unidades ou parâmetros
- **Instruções contraditórias**: Pedidos mutuamente exclusivos
- **Prompt muito longo**: Informação excessiva que confunde

### Como Identificar
- Respostas genéricas ou irrelevantes
- Múltiplas interpretações possíveis
- Falta de foco no objetivo principal

## 6. Atividade Prática (5 minutos)
**Exercício em Pares**: Cada dupla cria um prompt para resolver um problema técnico simples. Testem e refinem com base nos resultados obtidos.

## 7. Para a Próxima Aula
Pratique criando prompts para diferentes tipos de problemas técnicos da sua área de engenharia.

---
**Próxima Aula**: Técnicas de refinamento de prompts (zero-shot)
