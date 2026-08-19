# Material Complementar — Unidade 3

QUIZ Não Avaliativo (Pergunta de verdadeiro ou falso)

Pergunta 1
Pergunta: Avaliar prompts com um conjunto fixo de casos representativos e de borda ajuda a medir qualidade e a evitar regressões.
Resposta correta: Verdadeiro
Feedback se acertar: Isso! Um suite de casos permite comparar versões e identificar regressões com mais confiança.
Feedback se errar: Atenção. Sem casos padronizados, é difícil medir progresso e garantir estabilidade.

Contexto e justificativa: Conjuntos de teste representativos e casos de borda permitem comparar versões de prompts/métricas com controle de regressões. Registrando resultados e parâmetros, você obtém rastreabilidade e aprende sobre limitações.

Pergunta 2
Pergunta: Se um prompt funciona em um único exemplo, está pronto para produção.
Resposta correta: Falso
Feedback se acertar: Correto! É preciso testar variedade, bordas, segurança, custo e consistência antes de produção.
Feedback se errar: Cuidado. Um único exemplo não cobre variabilidade; é necessário avaliar sistematicamente.

Contexto e justificativa: Um exemplo “feliz” não revela onde o prompt falha (ambiguidade, ruído, formatos inesperados). Avaliações com amostragem e critérios explícitos reduzem risco em produção.

ATIVIDADE VERIFICADORA
AAI – Atividade avaliativa individual

Questão dissertativa
Defina uma estratégia de avaliação para um prompt de sumarização de políticas internas (texto longo). Inclua: (i) objetivos e critérios mensuráveis (foco, completude, fidelidade, legibilidade); (ii) conjunto de testes com 6–10 casos (inclua 2 de borda) e expectativas por caso; (iii) métricas (heurísticas simples e avaliação humana estruturada); (iv) limites de custo/latência e orçamentos por rodada; (v) plano de iteração (como medir melhoria sem overfitting ao conjunto) e estratégia de rollback; (vi) abordagem para dados sensíveis (anonimização e escopo).

Resposta esperada
- Objetivos claros e critérios com escalas (ex.: 1–5 para fidelidade, checklist de itens obrigatórios).
- Casos variados e bordas (texto ambíguo, muito longo, com dados ausentes). Indicar expectativas.
- Métricas: automáticas simples (comprimento, presença de termos-chave), avaliação humana (fidelidade/clareza), amostragem para verificação manual.
- Orçamento: limites de tokens/latência por item, trade-offs com qualidade.
- Iteração e controle de regressões: baseline, testes A/B, registro de versões.
- Plano de rollback e critérios para interromper uma versão pior que a baseline.
- Estratégia para dados sensíveis: anonimização, storage seguro e minimização de retenção.

Critérios de Avaliação (Rubrica) — Total: 10,0 pontos
- Definição de critérios e objetivos mensuráveis: 3,0
- Cobertura do conjunto de teste (inclui bordas): 3,0
- Adequação das métricas e do orçamento: 2,0
- Plano de iteração e prevenção de regressões: 2,0

Observações para correção
- Aceitar métricas simples se acompanhadas de avaliação humana crítica e amostragem adequada.
- Penalizar falta de casos de borda e de baseline/versões.
- Valorizar atenção à fidelidade (não inventar), proteção de dados sensíveis e definição de rollback.
- Pontuar positivamente propostas de automação (scripts/planilhas para coleta de métricas) e documentação de resultados.

PARA MERGULHAR NO ASSUNTO (SAIBA MAIS)
Texto provocativo para explorar mais o conteúdo:
Avaliar prompts é gerenciar risco: qualidade, custo e segurança. Como garantir que uma melhora local não quebre casos críticos? E como evitar overfitting ao conjunto de testes? Como você lidará com deriva de dados (mudança nos tipos de entrada) e com a necessidade de atualizar o conjunto de testes periodicamente?

Recomendações
- Guia: Avaliação de LLMs e prompt testing.
- Ferramentas: Checklists e planilhas simples para tracking.
- Post técnico: Estratégias para fidelidade e detecção de alucinações.
- Modelos de planilhas e templates de relatório de avaliação para equipes.

Links:
- https://www.lm-evaluation-harness.org/
- https://github.com/openai/openai-cookbook
- https://platform.openai.com/docs/guides/evals

PODCAST (curadoria | até 45min)
Texto provocativo para estimular a escuta do podcast:
Como times medem qualidade de prompts em escala? Casos reais discutem métricas, amostragem e governança.

NOME DO PODCAST: Software Engineering Daily (YouTube)
NOME DO EPISÓDIO: Episódios curados sobre avaliação de LLMs (até 45 min)
Link: https://www.youtube.com/results?search_query=software+engineering+daily+LLM+evaluation

ARTIGO CIENTÍFICO
Texto provocativo para leitura do artigo científico:
Quais limites e desafios na avaliação de modelos e prompts? Pesquisas recentes discutem fidelidade factual e robustez.

Link:
https://arxiv.org/abs/2307.03109

Referência bibliográfica (ABNT):
JIANG, Zhengbao; ZHANG, Tianyi; et al. A Survey of LLM Evaluation: Toward Reliable and Efficient Evaluation. arXiv, 2023. Disponível em: https://arxiv.org/abs/2307.03109.
