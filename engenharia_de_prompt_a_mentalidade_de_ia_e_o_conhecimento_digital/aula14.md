# Aula 14: Ferramentas CLI para IA e Integração com Sistemas

## Objetivo da Aula
Explorar ferramentas de linha de comando que potencializam o uso de IA em ambientes de desenvolvimento e engenharia. Ao final, o aluno deverá ser capaz de configurar, autenticar e compor CLIs em workflows automatizados.

## 1. Visão Geral de Ferramentas CLI para IA

### Conceito e Benefícios
> **CLI (Command Line Interface)** ferramentas permitem interação eficiente com sistemas de IA através de comandos de terminal, oferecendo automação e integração avançada.

### Vantagens das CLIs
### Limitações das CLIs
- Curva de aprendizado para usuários iniciantes
- Menor apelo visual (sem GUI)
- Possível complexidade de dependências
- **Automação**: Scripts e workflows automatizados
- **Integração**: Conexão com ferramentas existentes
- **Controle preciso**: Parâmetros detalhados para cada tarefa
- **Eficiência**: Processamento batch e operações em lote

## 2. Principais CLIs Disponíveis

### GitHub CLI (gh)
- **Funcionalidades**: Gerenciamento completo de repositórios GitHub
- **Comandos principais**: `gh repo`, `gh pr`, `gh issue`, `gh workflow`
- **Integração com IA**: Análise automática de código, sugestões de melhorias

### Cursor CLI
- **Funcionalidades**: Controle programático do Cursor (IDE baseado em IA)
- **Comandos principais**: Edição de arquivos, execução de comandos, integração com APIs
- **Aplicações**: Automação de tarefas de desenvolvimento assistidas por IA

### Ollama CLI
- **Funcionalidades**: Execução local de modelos de linguagem
- **Comandos principais**: `ollama run`, `ollama pull`, `ollama list`
- **Benefícios**: Controle total sobre modelos e privacidade de dados

### Outras CLIs Relevantes
- **OpenAI CLI**: Interface para APIs da OpenAI
- **Hugging Face CLI**: Gerenciamento de modelos de ML
- **Anthropic CLI**: Acesso às APIs da Anthropic (Claude)

## 3. Instalação e Configuração

### Processo de Setup
1. **Verificar requisitos**: Node.js, Python, Git instalados
2. **Instalar CLIs**: `npm install -g [cli-name]` ou equivalente
3. **Configurar autenticação**: Tokens de API e credenciais
4. **Testar instalação**: Executar comandos básicos de verificação

### Exemplo de Configuração
```bash
# Instalar GitHub CLI
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
sudo chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
sudo apt update
sudo apt install gh

# Configurar autenticação
gh auth login
```

## 4. Integração com Sistemas de IA Existentes

### Estratégias de Integração
- **APIs diretas**: Chamadas HTTP para serviços de IA
- **Wrappers personalizados**: Scripts que abstraem complexidade
- **Pipes de dados**: Encadeamento de comandos CLI
- **Webhooks**: Triggers automáticos baseados em eventos

### Exemplo de Integração
```bash
# Script que combina gh CLI com análise de IA
#!/bin/bash
# Analisar PR recente e sugerir melhorias

PR_NUMBER=$(gh pr list --limit 1 --json number --jq '.[0].number')
PR_BODY=$(gh pr view $PR_NUMBER --json body --jq '.body')

# Enviar para análise de IA
echo "Analise este PR e sugira melhorias: $PR_BODY" | ollama run codellama
```

## 5. Automatização de Tarefas em Engenharia

### Workflows Automatizados
- **Análise de código**: Verificação automática de qualidade e padrões
- **Geração de documentação**: Documentação técnica automática
- **Testes automatizados**: Execução e análise de baterias de teste
- **Deploy contínuo**: Implantação automática com validações de IA

### Estudo de Caso - Gerenciamento de Repositórios
```bash
# Script automatizado para análise de PRs
#!/bin/bash

# Buscar PRs abertos
PRS=$(gh pr list --state open --json number,title,author)

# Para cada PR, analisar com IA
echo "$PRS" | jq -r '.[] | .number' | while read pr_num; do
    echo "Analisando PR #$pr_num..."

    # Obter detalhes do PR
    DETAILS=$(gh pr view $pr_num --json body,files)

    # Análise com IA
    echo "Analise técnica deste PR: $DETAILS" | ollama run codellama > "pr_analysis_$pr_num.txt"

    # Criar comentário automático
    gh pr comment $pr_num --body-file "pr_analysis_$pr_num.txt"
done
```

## 6. Combinação de Múltiplas CLIs

### Estratégias de Composição
- **Pipes**: Saída de um comando como entrada de outro
- **Scripts compostos**: Combinação de múltiplas ferramentas
- **Orquestração**: Controle centralizado de diferentes CLIs

### Exemplo de Workflow Completo
### Boas Práticas de Segurança
- Armazenar tokens em secrets (GitHub Actions, variáveis de ambiente)
- Evitar logs com dados sensíveis
- Rotacionar chaves periodicamente
```bash
# Workflow: Análise completa de projeto
#!/bin/bash

PROJECT_DIR=$1

# 1. Análise de estrutura com tree
echo "Estrutura do projeto:" > analysis.md
tree $PROJECT_DIR >> analysis.md

# 2. Análise de código com ferramentas de qualidade
echo -e "\nAnálise de qualidade:" >> analysis.md

# 3. Sugestões de melhoria com IA
echo -e "\nSugestões de melhoria:" >> analysis.md
cat analysis.md | ollama run codellama >> analysis.md

# 4. Criar issue no GitHub com resultados
gh issue create --title "Análise automatizada do projeto" --body-file analysis.md
```

## 7. Aplicações Específicas por Área

### Engenharia Civil
- **Análise estrutural**: Processamento de dados de sensores
- **Otimização de projetos**: Cálculos automatizados de dimensionamento
- **Documentação técnica**: Geração automática de relatórios

### Engenharia Elétrica
- **Análise de circuitos**: Simulações e cálculos automatizados
- **Otimização energética**: Análise de consumo e sugestões de melhoria
- **Documentação de sistemas**: Especificações técnicas automáticas

### Engenharia Mecânica
- **Análise de elementos finitos**: Processamento de resultados de simulação
- **Otimização de geometrias**: Sugestões automáticas de melhorias
- **Documentação de produtos**: Manuais técnicos automatizados

## 8. Atividade Prática (5 minutos)
**Script Simples**: Crie um script bash básico que combine duas CLIs diferentes (ex: gh + ollama) para automatizar uma tarefa útil.

## 9. Para a Próxima Aula
Identifique oportunidades de automação com CLIs no seu ambiente de trabalho atual.

---
**Próxima Aula**: Configuração prática de repositório com .agents e .github
