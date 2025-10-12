# Material Complementar — Unidade 1

QUIZ Não Avaliativo (Pergunta de verdadeiro ou falso)

Pergunta 1
Pergunta: Especificar claramente o formato de saída (por exemplo, JSON com chaves obrigatórias) no prompt tende a reduzir ambiguidade e melhorar a qualidade das respostas.
Resposta correta: Verdadeiro
Feedback se acertar: Exato! Pedir formato, campos e restrições explícitas reduz graus de liberdade e induz respostas mais consistentes.
Feedback se errar: Quase. Prompts que determinam formato e restrições deixam menos espaço para interpretações, o que normalmente melhora a qualidade.

Contexto e justificativa: Em tarefas de extração e síntese, declarar explicitamente campos, tipos e exemplos-alvo facilita validação automática, acelera revisão humana e reduz retrabalho. Em times, também padroniza entregas entre pessoas diferentes e simplifica auditorias.

Pergunta 2
Pergunta: Considerações éticas (vieses, privacidade, transparência) podem ser ignoradas se o prompt estiver muito bem especificado tecnicamente.
Resposta correta: Falso
Feedback se acertar: Correto! Mesmo prompts bem especificados exigem revisão ética: riscos, vieses e governança precisam ser tratados.
Feedback se errar: Atenção. Qualidade técnica não substitui responsabilidade: é necessário avaliar impactos e mitigar danos.

Contexto e justificativa: Especificação clara não impede consequências indesejadas (ex.: reforço de estereótipos, exposição de PII). Mitigações incluem anonimização, filtros, limites de uso, testes de viés e comunicação transparente de limitações.

ATIVIDADE VERIFICADORA
AAI – Atividade avaliativa individual

Questão dissertativa
Reescreva 3 prompts ruins em versões otimizadas. Para cada caso, descreva: (i) objetivo do usuário e público-alvo; (ii) riscos de ambiguidade, premissas e lacunas; (iii) melhorias aplicadas (clareza, persona, restrições, passos, tom, limites de tamanho); (iv) formato de saída com schema (campos obrigatórios e tipos); (v) um exemplo de entrada e a saída esperada (estrutura e critérios de qualidade); (vi) breve revisão ética (vieses, privacidade, impacto e mitigação); (vii) como validará a conformidade (checagem automática e revisão humana).

Resposta esperada
- Identificação do objetivo e dos critérios de sucesso (o que é uma boa resposta?).
- Análise de problemas do prompt original (vago, sem restrições, sem público/persona, sem exemplo, sem formato).
- Reescrita com elementos de engenharia de prompt: instruções claras, persona/estilo, limites (o que deve e não deve fazer), passos, formato de saída, critérios de avaliação, limitações conhecidas e estratégia de fallback.
- Exemplo de teste com entrada realista e saída consistente com o formato especificado, incluindo casos de borda (dados ausentes/ambíguos) e a política para esses casos (ex.: null, "não aplicável").
- Proposta de validação: checklist, verificador de JSON/estrutura e pontos de atenção para revisão humana (fidelidade, completude, tom adequado).
- Revisão ética concisa (riscos, dados sensíveis, mitigação de vieses).

Critérios de Avaliação (Rubrica) — Total: 10,0 pontos
- Clareza do objetivo e critérios de sucesso: 2,0
- Diagnóstico dos problemas do prompt original: 2,0
- Qualidade da reescrita (instruções, restrições, formato): 4,0
- Exemplos de teste e coerência da saída: 2,0

Observações para correção
- Conceder crédito parcial quando a metodologia estiver correta com pequenos deslizes de forma/estilo.
- Penalizar ausência de formato/critério de sucesso quando essenciais para a tarefa e falta de atenção a casos de borda.
- Valorizar justificativas que conectem decisão de design a risco/benefício (redução de ambiguidade, consistência, custo) e a atenção a ética/privacidade, incluindo exemplos de mitigação.
- Sinalizar positivamente quando houver proposta de automação (validação de estrutura, lints de conteúdo) e plano de revisão humana.

PARA MERGULHAR NO ASSUNTO (SAIBA MAIS)
Texto provocativo para explorar mais o conteúdo:
Engenharia de prompt é, antes de tudo, design de especificações conversacionais. Bons resultados nascem de objetivos claros, critérios de qualidade e restrições que guiam o modelo. Pense no prompt como um contrato: quais campos, limites e exceções ele precisa conter para reduzir ambiguidade sem sufocar a criatividade? Como você traduziria um requisito de negócio difuso em regras operacionais testáveis dentro do prompt — e como garantiria que isso respeita princípios éticos, privacidade e expectativas do usuário final? Quais são os trade-offs entre precisão, custo e velocidade que você aceitaria em cada contexto (prototipagem vs. produção)?

Recomendações
- Guia prático: Prompting Guide (conceitos e padrões de projeto).
- Repositório: Exemplos de formatação e validação de JSON com LLMs.
- Artigo introdutório: Boas práticas de instruções, delimitação de contexto e responsabilidade.
- Checklist sugerido: critérios de sucesso, limites, formato, política de erros, exemplos, avaliação e plano de iteração.
- Exemplos de prompts com papéis (system/developer/user) e políticas de segurança (o que não fazer).

Links:
- https://www.promptingguide.ai/
- https://platform.openai.com/docs/guides/structured-outputs
- https://github.com/openai/openai-cookbook
- https://owasp.org/www-project-top-10-for-large-language-model-applications/

PODCAST (curadoria | até 45min)
Texto provocativo para estimular a escuta do podcast:
Como times transformam requisitos abertos em prompts eficazes e responsáveis? Ouvir casos ajuda a entender compromissos entre qualidade, custo, segurança e ética.

NOME DO PODCAST: Gradient Dissent (Weights & Biases)
NOME DO EPISÓDIO: Episódios curados sobre Prompt Engineering (até 45 min)
Link: https://www.youtube.com/@WeightsBiases

ARTIGO CIENTÍFICO
Texto provocativo para leitura do artigo científico:
Qual o papel de instruções explícitas e exemplos na performance de LLMs? Revisões recentes sintetizam técnicas, armadilhas comuns e cuidados éticos.

Link:
https://arxiv.org/abs/2307.16647

Referência bibliográfica (ABNT):
LIU, Peng et al. Prompt Engineering for Large Language Models: A Survey. arXiv, 2023. Disponível em: https://arxiv.org/abs/2307.16647.
