# Material Complementar — Unidade 2

QUIZ Não Avaliativo (Pergunta de verdadeiro ou falso)

Pergunta 1
Pergunta: Explicitar uma cadeia de pensamento (passo a passo) pode melhorar o raciocínio em tarefas complexas.
Resposta correta: Verdadeiro
Feedback se acertar: Perfeito! Estruturar o raciocínio em etapas ajuda o modelo a “pensar em voz alta” e reduzir saltos lógicos.
Feedback se errar: Quase. Pedir passos e critérios torna o processo mais auditável e geralmente melhora a acurácia em problemas complexos.

Contexto e justificativa: Em problemas de múltiplas etapas (planejamento, engenharia de requisitos, troubleshooting), solicitar raciocínio explícito ajuda a reduzir “saltos” e facilita revisão humana. Use junto de limites de tamanho para controlar custo.

Pergunta 2
Pergunta: Few-shot prompting exige que os exemplos sejam do mesmo domínio da tarefa, ou não funcionará.
Resposta correta: Falso
Feedback se acertar: Correto! Exemplos próximos ao padrão desejado ajudam, mas podem generalizar entre domínios quando a estrutura é clara.
Feedback se errar: Atenção. A similaridade ajuda, porém o crucial é a estrutura e o formato dos exemplos, não apenas o domínio exato.

Contexto e justificativa: Estruturas de I/O e critérios de avaliação são transferíveis; exemplos devem enfatizar formato e decisão, não detalhes de domínio. Evite exemplos que induzam viés indesejado.

ATIVIDADE VERIFICADORA
AAI – Atividade avaliativa individual

Questão dissertativa
Proponha um prompt para extração de informações (ex.: de resumos de artigos) usando técnicas de engenharia de prompt: (i) delimitação de contexto (o que ler/ignorar); (ii) instruções e critérios de extração; (iii) few-shot com 2–3 exemplos (entrada→saída) que cubram casos comuns e bordas; (iv) formato de saída em JSON com schema e política de erros (null/razão); (v) checklist de avaliação (exatidão, completude, conformidade do JSON, consistência entre casos); (vi) plano de validação automática (parser/validador) e revisão humana.

Resposta esperada
- Contexto com delimitadores e escopo claro (o que ler, o que ignorar).
- Instruções com campos obrigatórios, regras de extração e tratamento de ausência de dados (usar null/"não encontrado").
- Exemplos few-shot coesos com entradas e saídas corretas.
- Especificação de saída JSON e incentivos à validação.
- Mecanismos anti-alucinação: “não invente, responda null se ausente”, checagem de inconsistências, recap de fontes.
- Política de erros clara (quando devolver null, quando omitir campo, como sinalizar incerteza) e como isso afeta downstream.
- Plano de testes com amostras diversificadas (incluindo entradas ruidosas) e limites de custo/latência por item.

Critérios de Avaliação (Rubrica) — Total: 10,0 pontos
- Definição do escopo e contexto: 2,0
- Clareza das instruções e critérios: 3,0
- Qualidade dos exemplos few-shot: 3,0
- Formato de saída e mitigação de alucinações: 2,0

Observações para correção
- Conceder crédito parcial por estrutura correta com pequenos erros de formato.
- Penalizar ausência de critérios e de estratégia anti-alucinação.
- Valorizar exemplos variados que cubram casos comuns e bordas, e presença de política de erros.
- Destacar positivamente propostas de automação (validação de JSON, testes) e plano de revisão humana.

PARA MERGULHAR NO ASSUNTO (SAIBA MAIS)
Texto provocativo para explorar mais o conteúdo:
Técnicas como few-shot, auto-reflection e cadeia de raciocínio explicitam “como” chegar à resposta. O desafio é equilibrar custo (tokens) e ganho de qualidade, evitando “overfitting” aos exemplos. Quais trade-offs você aceitaria para obter respostas auditáveis e consistentes? Como garantir diversidade de exemplos sem introduzir viés? E como você detectará regressões ao iterar no prompt?

Recomendações
- Guia: Padrões de prompting (chain-of-thought, self-consistency, ReAct).
- Repositório: Exemplos de extração estruturada com validação.
- Post técnico: Estratégias para reduzir alucinações em extração.
- Planilhas-modelo: checklists de qualidade e planilhas para registrar resultados.

Links:
- https://www.promptingguide.ai/techniques
- https://platform.openai.com/docs/guides/structured-outputs
- https://github.com/openai/openai-cookbook

PODCAST (curadoria | até 45min)
Texto provocativo para estimular a escuta do podcast:
Como projetar prompts para tarefas de extração e raciocínio? Casos práticos mostram ganhos e armadilhas.

NOME DO PODCAST: DeepLearning.AI (YouTube)
NOME DO EPISÓDIO: Episódios curados sobre Few-shot e Chain-of-Thought (até 45 min)
Link: https://www.youtube.com/@DeepLearningAI

ARTIGO CIENTÍFICO
Texto provocativo para leitura do artigo científico:
Quando exemplos ajudam? Há limites e condições para few-shot training-free. Estudos comparam abordagens e evidenciam melhores práticas.

Link:
https://arxiv.org/abs/2201.11903

Referência bibliográfica (ABNT):
MIN, Sewon; LUKASIK, Michal; LEVY, Omer et al. Rethinking the Role of Demonstrations: What Makes In-Context Learning Work? arXiv, 2022. Disponível em: https://arxiv.org/abs/2201.11903.
