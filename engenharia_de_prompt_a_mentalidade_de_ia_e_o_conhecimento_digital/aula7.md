# Aula 7: Formulação de Problemas Complexos em Etapas

## Objetivo da Aula
Aprender a decompor problemas complexos de engenharia em etapas gerenciáveis e formular prompts adequados para cada fase da solução. Ao final, o aluno deverá ser capaz de mapear dependências, sequenciar tarefas e definir métricas por etapa.

## 1. Abordagem Sistemática para Problemas Complexos

### Características de Problemas Complexos
- **Múltiplas variáveis**: Muitos fatores interagindo
- **Interdependências**: Mudanças em uma área afetam outras
- **Incerteza**: Dados incompletos ou variáveis imprevisíveis
- **Escopo amplo**: Requer análise multidisciplinar

### Processo de Decomposição
1. **Análise inicial**: Identificar componentes principais
2. **Quebra em módulos**: Dividir em problemas menores
3. **Identificação de dependências**: Mapear relações entre módulos
4. **Sequenciamento**: Ordenar etapas logicamente
5. **Integração**: Combinar soluções parciais

### Métricas por Etapa
- Definição: critérios de sucesso para cada módulo
- Entradas/Saídas: contratos claros entre etapas
- Riscos: pontos de falha e mitigação

## 2. Técnicas de Decomposição

### Método de Análise Hierárquica
- **Nível 1**: Problema geral (objetivo final)
- **Nível 2**: Subsistemas principais
- **Nível 3**: Componentes específicos
- **Nível 4**: Tarefas individuais

### Abordagem Funcional
### Outras Abordagens Úteis
- Análise de stakeholders e restrições externas
- Quebra por cenários (nominal, pior caso, melhor caso)
- Estrutura analítica do projeto (EAP/WBS)
- **Entrada**: Recursos e requisitos iniciais
- **Processo**: Transformações e operações
- **Saída**: Resultados e deliverables
- **Feedback**: Loops de validação e ajuste

## 3. Formulação de Prompts para Diferentes Etapas

### Etapa 1 - Análise e Definição
```
**Contexto:** Você é engenheiro consultor. Analise este problema complexo de engenharia.

**Problema:** Projeto de uma ponte pênsil de 500m com tráfego intenso e restrições ambientais.

**Tarefa:** Identifique os principais desafios e requisitos. Liste 5-7 aspectos críticos que precisam ser considerados.
```

### Etapa 2 - Decomposição Técnica
```
**Contexto:** Continuando a análise da ponte pênsil de 500m.

**Aspectos identificados anteriormente:** [lista dos aspectos críticos]

**Tarefa:** Para cada aspecto, sugira 2-3 abordagens técnicas possíveis. Considere métodos tradicionais e inovadores usando IA.
```

### Etapa 3 - Avaliação Comparativa
```
**Contexto:** Compare as diferentes abordagens identificadas para cada aspecto da ponte.

**Abordagens por aspecto:** [lista detalhada]

**Tarefa:** Para cada aspecto, avalie prós e contras das abordagens considerando:
- Custo de implementação
- Tempo de execução
- Impacto ambiental
- Confiabilidade técnica
- Manutenibilidade
```

### Etapa 4 - Síntese e Recomendação
### Verificação e Integração
- Checklist de integração entre módulos
- Testes de regressão após combinar soluções parciais
- Métricas de validação cruzada (técnica, negócio, usuário, ética)
```
**Contexto:** Com base nas análises anteriores, desenvolva uma proposta integrada.

**Análises realizadas:** [resumo das etapas anteriores]

**Tarefa:** Proponha uma solução integrada considerando trade-offs. Justifique escolhas técnicas e forneça cronograma estimado.
```

## 4. Exemplos Práticos por Área

### Engenharia Civil - Projeto de Sistema de Drenagem
**Problema Complexo**: Sistema de drenagem para bairro com 1000 residências, considerando chuva intensa e solo argiloso.

**Decomposição:**
1. **Análise hidrológica**: Calcular volume de água esperado
2. **Estudo geotécnico**: Caracterizar permeabilidade do solo
3. **Dimensionamento de tubulações**: Calcular diâmetros necessários
4. **Projeto de estruturas**: Bocas de lobo e poços de visita
5. **Análise econômica**: Custos de materiais e mão de obra

### Engenharia Mecânica - Otimização de Processo Industrial
**Problema Complexo**: Reduzir consumo energético em linha de produção com 15 máquinas operando 24/7.

**Decomposição:**
1. **Auditoria energética**: Medir consumo atual de cada máquina
2. **Análise de processos**: Mapear gargalos e ineficiências
3. **Modelagem matemática**: Criar modelo de otimização
4. **Testes piloto**: Implementar melhorias em escala reduzida
5. **ROI e escalabilidade**: Avaliar retorno financeiro

## 5. Integração de Técnicas de Prompting

### Estratégia Multi-técnica
- **Zero-shot inicial**: Para exploração rápida de ideias
- **Few-shot intermediário**: Para padronização de análises
- **Chain-of-thought final**: Para síntese e recomendações

### Exemplo de Fluxo Integrado
```
**Prompt 1 (Zero-shot):** Gere 10 ideias inovadoras para resolver [problema complexo]

**Prompt 2 (Few-shot):** Usando estes exemplos [3 casos similares], analise nosso problema:
- Caso 1: [descrição]
- Caso 2: [descrição]
- Nosso caso: [descrição]

**Prompt 3 (Chain-of-Thought):** Desenvolva solução integrada passo a passo...
```

## 6. Atividade Prática (5 minutos)
**Decomposição Colaborativa**: Em duplas, escolham um problema complexo da engenharia e decomponham em 4-5 etapas claras. Criem prompts para cada etapa.

## 7. Para a Próxima Aula
Identifique um problema complexo real da sua área de engenharia e pratique sua decomposição em etapas.

---
**Próxima Aula**: Casos reais - aplicações em engenharia elétrica, civil e produção
