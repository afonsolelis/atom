# Material Complementar — Unidade 4

QUIZ Não Avaliativo (Pergunta de verdadeiro ou falso)

Pergunta 1
Pergunta: Ao solicitar saída em JSON, é recomendável especificar um schema (campos obrigatórios, tipos) e validar a resposta antes de prosseguir no pipeline.
Resposta correta: Verdadeiro
Feedback se acertar: Exato! Especificação + validação reduzem erros e simplificam integração.
Feedback se errar: Cuidado. Sem schema/validação, a integração fica frágil e sujeita a falhas.

Contexto e justificativa: Schemas tornam explícitos contratos de dados e permitem validação automática. Isso reduz acoplamento frágil entre etapas e facilita observabilidade e depuração.

Pergunta 2
Pergunta: Com “function calling” habilitado, deixo de precisar validar entradas, pois o modelo garante conformidade.
Resposta correta: Falso
Feedback se acertar: Correto! Ainda é necessário validar e tratar erros; o modelo sugere chamadas, mas a aplicação é responsável pela segurança.
Feedback se errar: Atenção. “Function calling” organiza I/O, mas não substitui validação, autenticação e limites.

Contexto e justificativa: O modelo pode propor argumentos inválidos ou incompletos; a aplicação deve validar, autenticar e registrar erros. Políticas de retries e timeouts aumentam resiliência.

ATIVIDADE VERIFICADORA
AAI – Atividade avaliativa individual

Questão dissertativa
Projete um fluxo que combine engenharia de prompt com chamadas de função e saída estruturada para: (i) classificar tickets de suporte; (ii) extrair campos-chave; (iii) sugerir ações. Inclua: instruções, schema JSON, política de erros (quando devolver null/razão), e um exemplo de chamada de função com argumentos e resposta. Explique mitigação de riscos (alucinações, dados sensíveis, escalabilidade), limites de tokens/latência e observabilidade (logs/trace IDs).

Resposta esperada
- Prompt com papéis (system) e restrições (não inventar; preferir null).
- Schema JSON com campos obrigatórios, enums e validações simples.
- Exemplo de execução com entrada e saída aderente ao schema.
- Estratégias de segurança: validação server-side, limites de tokens, filtragem de PII, logs com anonimização, retries e fallback.
- Observabilidade: logs estruturados com IDs de correlação, amostragem de respostas e dashboards de erros/latência.
- Plano de testes: casos felizes, bordas e falhas de integração (timeouts, 4xx/5xx, schema inválido).

Critérios de Avaliação (Rubrica) — Total: 10,0 pontos
- Completude do fluxo (classificar, extrair, sugerir): 3,0
- Especificação clara de schema e política de erros: 3,0
- Integração com function calling e exemplo: 2,0
- Estratégias de segurança e robustez: 2,0

Observações para correção
- Creditar soluções simples, mas válidas e testáveis.
- Penalizar ausência de política de erros/validação e de plano de observabilidade.
- Valorizar atenção a privacidade, limites operacionais e estratégia de rollback.

PARA MERGULHAR NO ASSUNTO (SAIBA MAIS)
Texto provocativo para explorar mais o conteúdo:
Sistemas confiáveis exigem prompts bons e integração cuidadosa: schema, validação, retries, timeouts e observabilidade. Como você projetaria para falhar de forma segura?
Sistemas confiáveis exigem prompts bons e integração cuidadosa: schema, validação, retries, timeouts e observabilidade. Como você projetaria para falhar de forma segura? Que limites impedirão custos inesperados? Como anonimizar PII sem perder utilidade? Qual será a política de retenção de logs?

Recomendações
- Documentação: Saídas estruturadas e validação.
- Guia: Orquestração com ferramentas e agentes.
- Post técnico: Boas práticas de segurança e privacidade.
- Exemplos de pipelines com retries, timeouts e circuit breakers.

Links:
- https://platform.openai.com/docs/guides/structured-outputs
- https://platform.openai.com/docs/assistants/tools
- https://owasp.org/www-project-top-10-for-large-language-model-applications/

PODCAST (curadoria | até 45min)
Texto provocativo para estimular a escuta do podcast:
Integração de LLMs com sistemas exige disciplina de engenharia: contratos, testes e observabilidade.

NOME DO PODCAST: Software Engineering Daily (YouTube)
NOME DO EPISÓDIO: Episódios curados sobre interfaces e contratos com LLMs (até 45 min)
Link: https://www.youtube.com/results?search_query=software+engineering+daily+LLMs

ARTIGO CIENTÍFICO
Texto provocativo para leitura do artigo científico:
Como alinhar LLMs a tarefas com estrutura e ferramentas? Trabalhos recentes abordam tool-use, JSON e chamadas controladas.

Link:
https://arxiv.org/abs/2305.10601

Referência bibliográfica (ABNT):
SCHICK, Timo et al. Toolformer: Language Models Can Teach Themselves to Use Tools. arXiv, 2023. Disponível em: https://arxiv.org/abs/2305.10601.
