# Instruções para Agentes IA - Estruturas de Concreto: Pilares e Solicitações Dinâmicas

## Visão Geral do Projeto

Este repositório contém conteúdo acadêmico estruturado para uma **disciplina EAD de engenharia civil** sobre **Estruturas de Concreto: Pilares e Solicitações Dinâmicas**. A disciplina segue o "MODELO ÁTOMO" para produção de material educacional universitário, com **16 aulas divididas em 4 unidades** (4 aulas cada) + instrumentos avaliativos.

### Características da Disciplina EAD

- **Total**: 16 aulas estruturadas em videoaulas + material de apoio
- **Professor-conteudista**: Afonso Cesar Lelis Brandão
- **Modelo pedagógico**: MODELO ÁTOMO (estrutura rigorosa e padronizada)
- **Público**: Estudantes de engenharia civil (graduação)
- **Modalidade**: Ensino à distância com materiais autoexplicativos

## Arquitetura e Organização

### Estrutura de Diretórios

```
Estruturas_de_Concreto_Pilares_e_Solicitacoes_Dinamicas/
├── DIRETRIZES_UNIDADE.json          # Especificações técnicas completas
├── Ementa_da_Disciplina.md           # Objetivos e competências
├── instrumentos_avaliativos/         # Avaliações estruturadas
├── unidade_N/                        # Uma pasta por unidade (N=1-4)
│   ├── unidade_N_conteudo.md        # Arquivo principal consolidado
│   ├── unidade_N_i_aula.md          # Aulas individuais (i=1-4)
│   ├── questoes_unidade_N.md        # 20 questões MC + feedbacks
│   └── assets/ (opcional)            # Recursos visuais
```

### Fluxo de Desenvolvimento Principal

1. **Conteúdo principal**: Sempre comece com `unidade_N_conteudo.md` (template estruturado)
2. **Fragmentação**: Copie seções específicas para `unidade_N_i_aula.md`
3. **Avaliação**: Gere questões seguindo formato rigoroso em `questoes_unidade_N.md`
4. **Validação**: Verifique conformidade com checklist em `DIRETRIZES_UNIDADE.json`

## Padrões Técnicos Específicos

### Fórmulas Matemáticas

- **Obrigatório**: Use delimitadores LaTeX `$...$` para inline e `$ em linhas dedicadas` para blocos
- **Exemplo**: `$\omega_n = \sqrt{\tfrac{k}{M}}$` para frequência natural
- **Jamais** use blocos de código para equações matemáticas

### Estrutura de Aulas (700-1200 palavras cada)

```markdown
## Aula N – [Título Específico]

#### N. Introdução: [Contexto/Problema]

#### N+1. [Tópico Técnico Central]

#### N+2. [Exemplo Numérico/Aplicação]

#### N+3. [Atividade Prática]

##### Links suplementares da Aula N
```

### Imagens e Recursos Visuais

- **Fonte preferencial**: Wikimedia Commons/Wikipedia com links diretos
- **Quantidade**: 1-3 imagens por aula (mínimo 1)
- **Formato**: `![texto alternativo descritivo](URL_direto)`
- **Exemplo**: `![Diagrama clássico massa–mola–amortecedor](https://upload.wikimedia.org/wikipedia/commons/3/36/Spring...)`

### Sistema de Questões

- **Formato**: 20 questões múltipla escolha, 5 alternativas (a-e)
- **Marcação da correta**: `*c. Texto da alternativa correta.`
- **Seção obrigatória**: `## Feedbacks` numerados (1-20)
- **Distribuição**: Alternar posição da resposta correta aleatoriamente

## Convenções de Conteúdo

### Linguagem e Tom

- **Estilo**: Acadêmico mas acessível, com exemplos práticos
- **Persona**: Professor experiente explicando para estudantes de engenharia
- **Referências**: Normas ABNT (NBR 6118, NBR 6122) são centrais

### Domínio Técnico

- **Foco principal**: Pilares de concreto (estática + dinâmica) e pavimentação
- **Conceitos-chave**: Flambagem, efeitos P-Δ, vibrações, frequência natural, amortecimento
- **Aplicações**: Edifícios altos, estruturas sismicamente ativas, máquinas industriais

### Template de Validação

Sempre consulte `DIRETRIZES_UNIDADE.json` antes de criar/modificar conteúdo:

- Verificar checklist de validação (seção `validacao_checklist`)
- Seguir estrutura de campos obrigatórios (`template_unidade_campos`)
- Respeitar formatos específicos de avaliação (`avaliacao_final`)

## Fluxos de Trabalho Específicos

### Criação Completa de Unidade (Workflow Principal)

#### Passo 1: Preparação Inicial

1. **Definir títulos das 4 aulas** baseados na `Ementa_da_Disciplina.md`
2. **Criar estrutura de pasta**: `unidade_N/` (onde N = número da unidade)
3. **Identificar arquivos necessários**:
   - `unidade_N_conteudo.md` (arquivo principal consolidado)
   - `unidade_N_1_aula.md`, `unidade_N_2_aula.md`, etc.
   - `questoes_unidade_N.md`

#### Passo 2: Criação do Arquivo Principal (`unidade_N_conteudo.md`)

Use o template do `unidade_1_conteudo.md` e preencha:

**Cabeçalho padrão:**

```markdown
# TEMPLATE DE PRODUÇÃO - MODELO ÁTOMO

# Nome da disciplina: Estruturas de Concreto: Pilares e Solicitações Dinâmicas

# Conteudista: Afonso Cesar Lelis Brandão
```

**Texto base inicial:**

- Relevância profissional (1-2 parágrafos)
- Contribuições para atuação (4-6 bullets)
- Exemplos práticos (3-4 bullets)

#### Passo 3: Desenvolvimento das Aulas (4 aulas por unidade)

Para cada aula, criar conteúdo seguindo estrutura obrigatória:

**Estrutura de cada aula:**

```markdown
## Aula X – [Título Específico]

##### Objetivos da aula

- [3 bullets de objetivos]

##### Conteúdo da aula (texto base)

#### X. Introdução: [Contexto/Problema - 1 parágrafo]

#### X+1. [Tópico Técnico 1]

#### X+2. [Tópico Técnico 2]

#### X+3. [Exemplo Numérico com fórmulas LaTeX]

#### X+4. [Atividade Prática]

#### X+5. Pontos-chave

- [3-5 bullets resumindo conceitos]

##### Links suplementares da Aula X

- [2-4 links: Wikipedia/Normas/Materiais didáticos]
```

**Requisitos técnicos por aula:**

- **Extensão**: 700-1200 palavras
- **Seções**: 6-10 subseções
- **Imagens**: 1-3 por aula (Wikimedia/Wikipedia preferencial)
- **Fórmulas**: LaTeX entre `$...$` (inline) ou linhas dedicadas
- **Exemplo**: Pelo menos 1 exemplo numérico quando aplicável
- **Referência de qualidade**: Use densidade de `unidade_2/unidade_2_1_aula.md`

#### Passo 4: Fragmentação para Arquivos Individuais

1. **Copiar conteúdo** de cada aula do arquivo principal
2. **Criar arquivos separados**: `unidade_N_i_aula.md` (i=1-4)
3. **Manter formatação** exata de fórmulas e imagens
4. **Preservar links** suplementares

#### Passo 5: Material Complementar (no arquivo principal)

Preencher todas as seções obrigatórias:

**Direto da Fonte:**

- Texto provocativo + Nome do livro + Capítulo + Link
- Acesso: `https://fecaf.brightspace.com/d2l/home` (BV professor)

**Para Mergulhar:**

- Filme/Série/Livro/Blog com descrições e links

**Podcast (OBRIGATÓRIO YouTube):**

- Nome do podcast/vídeo + Episódio + Link YouTube

**Artigo Científico:**

- Link DOI + Referência ABNT completa

#### Passo 6: Criação de Questões (`questoes_unidade_N.md`)

**Formato rigoroso:**

```markdown
## Questões

1. [Enunciado da questão]
   a. Alternativa incorreta
   b. Alternativa incorreta
   \*c. Alternativa correta (marcada com asterisco)
   d. Alternativa incorreta
   e. Alternativa incorreta

[Repetir para 20 questões]

## Feedbacks

1. A resposta correta é C: [explicação técnica objetiva]
   [Repetir para todas as 20 questões]
```

**Regras específicas:**

- 20 questões múltipla escolha
- 5 alternativas cada (a-e)
- Alternar posição da resposta correta aleatoriamente
- Marcação: `*` antes da letra correta
- Feedbacks numerados explicando cada resposta

#### Passo 7: Validação Final

Verificar checklist obrigatório:

- [ ] Cada aula: 700-1200 palavras, 6-10 subseções
- [ ] Fórmulas em LaTeX ($...$), nunca em blocos de código
- [ ] 1-3 imagens/aula com alt descritivo e fontes válidas
- [ ] Exemplo numérico + atividade prática em cada aula
- [ ] Pontos-chave (3-5 bullets) + links suplementares
- [ ] 20 questões MC com 5 alternativas, correta marcada (\*)
- [ ] Seção Feedbacks numerada (1-20)
- [ ] Material complementar completo, Podcast no YouTube
- [ ] Todos os links testados e funcionando

### Modificando Conteúdo Existente

- **Prioridade**: Manter consistência com arquivos relacionados
- **Fórmulas**: Sempre preservar formatação LaTeX existente
- **Imagens**: Verificar funcionamento de links antes de modificar
- **Questões**: Manter numeração e formato de feedbacks

### Integrações Críticas

- **Material complementar**: Podcast obrigatoriamente do YouTube
- **Links**: Testar funcionamento de todas as referências externas
- **Normas**: Referenciar adequadamente ABNT quando aplicável

## Critérios de Qualidade EAD

### Padrões de Aprovação ("Conteúdo UAU")

Todo material deve atender aos critérios de validação do coordenador:

- **Conformidade** com Plano de Aprendizado
- **Clareza e objetividade** para aprendizado autônomo
- **Ortografia e gramática** impecáveis
- **Recursos visuais atrativos** (imagens, gráficos, diagramas)

### Acessibilidade do Material

- **Plataforma**: https://fecaf.brightspace.com/d2l/home
- **Acesso**: Opção "BV professor"
- **Credenciais**: professor.conteudista / unifecaf2023
- **Autoexplicativo**: Material deve funcionar sem presença do professor

### Avaliações Específicas EAD

**Quiz Não Avaliativo:** 2 questões Verdadeiro/Falso com explicações
**Atividade Verificadora:** 1 questão dissertativa com resposta esperada detalhada
**Avaliação Final:** 30 questões (10 MC + 10 Asserção-Razão + 10 Interpretação)

## Debugging e Problemas Comuns

### Fórmulas não renderizando

- Verificar delimitadores `$...$` sem espaços extras
- Confirmar caracteres de escape LaTeX (`\tfrac`, `\sqrt`)

### Estrutura de arquivo incorreta

- Comparar com template em `unidade_1_conteudo.md`
- Validar contra checklist em `DIRETRIZES_UNIDADE.json`

### Links quebrados

- Preferir URLs permanentes (Wikimedia/Wikipedia)
- Testar todos os links antes de commit

---

_Este projeto é específico para ensino de engenharia estrutural. Mantenha rigor técnico e precisão nas fórmulas e conceitos._
