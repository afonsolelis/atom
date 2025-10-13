# Aula 15: Configuração Prática de Repositório com .agents e .github

## Objetivo da Aula
Aprender a configurar repositórios colaborativos com diretrizes específicas para desenvolvimento assistido por IA e automação de processos. Ao final, o aluno deverá ser capaz de estruturar `.agents` e `.github` com workflows mínimos de qualidade e segurança.

## 1. Estrutura e Organização de Repositórios Colaborativos

### Estrutura Recomendada
```
meu-projeto/
├── .github/
│   ├── workflows/          # Automação CI/CD
│   ├── ISSUE_TEMPLATE/     # Templates para issues
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── CODEOWNERS
├── .agents/                # Diretrizes para agentes IA
│   ├── prompt-principles.md
│   ├── coding-standards.md
│   └── review-guidelines.md
├── src/                    # Código fonte
├── docs/                   # Documentação
├── tests/                  # Testes automatizados
└── README.md
```

## 2. Criação da Pasta .agents

### Arquivo: prompt-principles.md
```markdown
# Princípios de Prompt para este Projeto

## Contexto Técnico
Este projeto desenvolve [descrição breve]. Use sempre:

**Persona Principal:**
"Você é um engenheiro sênior especializado em [área específica] com 10+ anos de experiência."

**Restrições Técnicas:**
- Linguagem: [PT-BR/EN]
- Norma técnica: [ABNT/ISO/...]
- Framework: [React/Python/.NET]

## Padrões de Prompt

### Para Análise de Código
```
Contexto: Projeto [nome] - módulo [módulo específico]
Problema: [descrição clara]
Requisitos: [lista de requisitos técnicos]

Analise e sugira melhorias considerando:
1. Performance e otimização
2. Segurança e robustez
3. Manutenibilidade
4. Conformidade com padrões

Formato: Liste problemas encontrados e soluções propostas.
```

### Para Geração de Código
```
Contexto: Implementar [funcionalidade] em [linguagem/framework]

Requisitos funcionais:
- [requisito 1]
- [requisito 2]

Requisitos técnicos:
- [restrição técnica 1]
- [restrição técnica 2]

Exemplo de uso:
[input] → [output esperado]

Gere código completo e documentado.
```

### Para Revisão de PR
```
Contexto: Revisar PR #[número] - [título breve]

Arquivos alterados:
[lista de arquivos]

Mudanças principais:
[resumo das alterações]

Verifique:
1. Conformidade com padrões de código
2. Testes adequados incluídos
3. Documentação atualizada
4. Impacto em performance

Forneça feedback estruturado com sugestões de melhoria.
```
```

### Arquivo: coding-standards.md
```markdown
# Padrões de Código para Agentes IA

## Convenções de Nomenclatura
- **Variáveis**: camelCase para JS/TS, snake_case para Python
- **Funções**: camelCase com verbos de ação
- **Classes**: PascalCase
- **Arquivos**: kebab-case para nomes, PascalCase para classes

## Estrutura de Código
- **Comentários obrigatórios** para funções públicas e classes
- **Tipagem explícita** sempre que possível
- **Tratamento de erros** com try-catch ou equivalent
- **Validação de entrada** para todas as funções públicas

## Padrões de Commit
- **feat:** nova funcionalidade
- **fix:** correção de bug
- **docs:** documentação
- **refactor:** refatoração sem mudança funcional
- **test:** adição/modificação de testes

## Validações Automáticas
- ESLint/Prettier para JS/TS
- Black/isort para Python
- Testes unitários obrigatórios
- Cobertura mínima de 80%
```

## 3. Configuração do .github

### Workflows de Automação (.github/workflows/)

#### CI/CD Básico
```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Setup Node.js
      uses: actions/setup-node@v3
      with:
        node-version: '18'
    - name: Install dependencies
      run: npm ci
    - name: Run tests
      run: npm test
    - name: Build application
      run: npm run build

  ai-review:
    runs-on: ubuntu-latest
    needs: test
    if: github.event_name == 'pull_request'
    steps:
    - uses: actions/checkout@v3
    - name: AI Code Review
      run: |
        echo "Analisando PR com IA..."
        # Integração com agente de revisão
```

#### Análise de Segurança
```yaml
name: Security Scan

on:
  push:
    branches: [ main ]
  schedule:
    - cron: '0 6 * * 1'  # Weekly on Mondays

jobs:
  security:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Run security audit
      run: npm audit --audit-level=moderate
    - name: CodeQL Analysis
      uses: github/codeql-action/init@v2
      with:
        languages: javascript
    - name: Perform CodeQL Analysis
      uses: github/codeql-action/analyze@v2
```

### Templates de Issues e PRs

#### Issue Template (.github/ISSUE_TEMPLATE/)
```markdown
---
name: Bug Report
about: Reportar um problema técnico
title: '[BUG] '
labels: bug, needs-triage
assignees: ''

---

## Descrição do Problema
Descreva claramente o bug encontrado.

## Passos para Reproduzir
1.
2.
3.

## Comportamento Esperado
O que deveria acontecer?

## Ambiente
- Sistema Operacional:
- Versão do software:
- Navegador (se aplicável):

## Logs/Anexos
Cole logs relevantes ou faça upload de screenshots.
```

#### Pull Request Template (.github/PULL_REQUEST_TEMPLATE.md)
```markdown
## Descrição da Mudança
Breve descrição do que foi implementado.

## Tipo de Mudança
- [ ] Bug fix
- [ ] Nova funcionalidade
- [ ] Melhorias
- [ ] Refatoração
- [ ] Documentação

## Testes Realizados
- [ ] Testes unitários
- [ ] Testes de integração
- [ ] Testes manuais
- [ ] Testes de regressão

## Checklist
- [ ] Código segue padrões do projeto
- [ ] Testes foram adicionados/atualizados
- [ ] Documentação foi atualizada
- [ ] Revisão de segurança realizada
- [ ] Aprovação de QA obtida

## Issues Relacionadas
Closes #[número da issue]

## Screenshots (se aplicável)
```

## 4. Diretrizes para Commits Estruturados

### Padrão Conventional Commits
```
tipo(escopo): descrição breve

[corpo opcional]

[rodapé opcional]
```

### Exemplos Práticos
```
feat(auth): implementar sistema de login JWT

Adiciona autenticação baseada em tokens JWT com refresh automático.
Inclui validação de senha e proteção contra ataques comuns.

Closes #123
```

```
fix(api): corrigir timeout em requisições longas

Ajusta timeout padrão de 30s para 60s em endpoints de relatório.
Previne falhas em consultas complexas.

Resolves #456
```

```
docs(readme): atualizar instruções de instalação

Inclui passos para configuração de ambiente Docker.
Adiciona seção de troubleshooting com problemas comuns.
```

## 5. Estudo de Caso Completo

### Cenário: Repositório de Sistema Embarcado
**Problema**: Equipe distribuída desenvolvendo firmware para dispositivo IoT.

**Configuração .agents**:
- Diretrizes específicas para código embarcado (C/C++)
- Padrões de comentários Doxygen obrigatórios
- Validações de consumo de memória e energia

**Workflows .github**:
- CI para diferentes plataformas (Arduino, ESP32, STM32)
- Análise estática de código comCppcheck
- Testes automatizados de integração hardware
- Deploy automático para ambiente de teste

**Templates**:
- Issues categorizadas por tipo (bug, feature, hardware)
- PRs com checklist específico para código embarcado
- Commits seguindo padrão que facilita changelog automático

## 6. Atividade Prática (5 minutos)
**Configuração Básica**: Crie estrutura básica de .github e .agents para um projeto simples da sua área de engenharia.

## 7. Para a Próxima Aula
Identifique oportunidades de automação no seu fluxo de trabalho atual que poderiam ser implementadas via GitHub Actions.

---
**Próxima Aula**: Diretrizes avançadas e automatização de processos colaborativos
