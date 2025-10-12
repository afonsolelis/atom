# Material Complementar — Unidade 3

QUIZ Não Avaliativo (Pergunta de verdadeiro ou falso)

Pergunta 1
Pergunta: O fator dinâmico de impacto (φ), segundo a NBR 7188, deve ser aplicado apenas sobre as cargas móveis, não incidindo sobre as cargas permanentes.
Resposta correta: Verdadeiro
Feedback se acertar: Correto! φ amplifica apenas os efeitos das cargas móveis (tráfego). As cargas permanentes não recebem esse fator.
Feedback se errar: Atenção. O fator dinâmico φ é exclusivo das cargas móveis; não se aplica às permanentes.

Pergunta 2
Pergunta: Para um vão L = 20 m, a NBR 7188 admite φ = 1,26 como valor típico.
Resposta correta: Verdadeiro
Feedback se acertar: Exato. Usando φ = 1,4 − 0,007·L, para L = 20 m resulta φ = 1,26 (com piso em 1,0).
Feedback se errar: Quase. Pela expressão φ = 1,4 − 0,007·L (mínimo 1,0), para L = 20 m resulta φ = 1,26.

ATIVIDADE VERIFICADORA
AAI – Atividade avaliativa individual

Questão dissertativa
Dada uma ponte de vão L = 20 m, largura útil 7,2 m, estime G (cargas permanentes) e Q (carga móvel TB-450 em kN/m), calcule φ conforme NBR 7188 e monte combinações ELU e ELS (indicando coeficientes). Discuta o efeito de φ na parcela móvel do momento máximo em viga biapoiada e comente possíveis implicações no dimensionamento.

Resposta esperada
- Levantamento de G: peso próprio (viga e laje) via γ = 25 kN/m³; revestimentos em kN/m² convertidos por largura; equipamentos lineares (kN/m).
- Q: TB-450 como carga distribuída equivalente q = 5,0 kN/m² → por metro linear Q = q·b = 5,0·7,2 = 36,0 kN/m (para o caso dado).
- Fator dinâmico: φ = 1,4 − 0,007·L = 1,26 (para L = 20 m; mínimo 1,0).
- Combinações: ELU: F_d = γ_g·G + γ_q·φ·Q; ELS: F_ser = G + ψ1·φ·Q (com ψ1 ≈ 0,6, valores típicos). Discutir que φ amplifica apenas a parcela móvel, elevando M_max proporcionalmente a φ.
- Viga biapoiada: M_max ≈ (G+φQ)·L²/8 (quando representado em kN/m). φ aumenta M devido à componente móvel, podendo governar armadura em regiões de momento e detalhamento para fissuração/ELS.

Critérios de Avaliação (Rubrica) — Total: 10,0 pontos
- Correta estimativa de G e conversões de unidades: 2,0
- Determinação de Q por largura de pista e entendimento da TB-450: 2,0
- Cálculo de φ e interpretação (aplica apenas a Q): 2,0
- Montagem de combinações ELU/ELS com coeficientes adequados: 2,0
- Discussão do impacto de φ no M_max e no dimensionamento: 2,0

Observações para correção
- Dar crédito parcial por metodologia correta com erro numérico limitado.
- Penalizar ausência de identificação clara de unidades e coeficientes.
- Valorizar justificativas que conectem norma → modelo de carga → efeito estrutural.

PARA MERGULHAR NO ASSUNTO (SAIBA MAIS)
Texto provocativo para explorar mais o conteúdo:
Dimensionar por norma não é “encher planilha”: é entender como cada coeficiente (γ, ψ, φ) altera a resposta estrutural. No canteiro e na manutenção, decisões sobre restrição de tráfego, fiscalização de peso e ensaios de carga dependem dessa leitura crítica. Até que ponto φ pode tornar a carga móvel dominante em vãos médios? Como isso migra para ELS (fissuração/deflexão)?

Recomendações
- Canal (YouTube): Practical Engineering — episódios sobre monitoramento e instrumentação.
- Blog/Artigo: FHWA – Bridge Load Rating (introdução prática a ensaios e avaliação).
- Dica de visita: acompanhar (quando possível) ensaios de carga e inspeções periódicas.

Links:
- https://www.youtube.com/c/PracticalEngineering
- https://www.fhwa.dot.gov/bridge/loadrating/

PODCAST (curadoria | até 45min)
Texto provocativo para estimular a escuta do podcast:
Ensaios de carga revelam se a ponte “se comporta” como o modelo prevê. Ouvir sobre práticas e conceitos ajuda a ligar normas (TB-450, φ) com validação em campo.

NOME DO PODCAST: Bridge Engineering (YouTube)
NOME DO EPISÓDIO: Bridge Load Testing
Link: https://www.youtube.com/watch?v=xsHkU6xOd8o

ARTIGO CIENTÍFICO
Texto provocativo para leitura do artigo científico:
Qual a ordem de grandeza do fator de amplificação dinâmica em diferentes contextos? Este artigo discute medições e valores práticos, oferecendo base para decisões conservadoras ou otimizadas no projeto.

Link:
https://doi.org/10.1016/j.proeng.2013.04.108

Referência bibliográfica (ABNT):
PAEGLITE, Ilze; PAEGLITIS, Ainars. The Dynamic Amplification Factor of the Bridges in Latvia. Procedia Engineering, v. 57, p. 851-858, 2013. Disponível em: https://doi.org/10.1016/j.proeng.2013.04.108.
