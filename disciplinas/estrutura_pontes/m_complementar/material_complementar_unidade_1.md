# Material Complementar — Unidade 1

QUIZ Não Avaliativo (Pergunta de verdadeiro ou falso)

Pergunta 1
Pergunta: Em uma viga simplesmente apoiada com carregamento simétrico (carga distribuída uniforme e uma carga concentrada aplicada no meio do vão), as reações de apoio nos dois apoios são iguais.
Resposta correta: Verdadeiro
Feedback se acertar: Correto! Pela simetria do carregamento, cada apoio resiste exatamente à metade da carga total (q·L + P)/2. Essa conclusão também é obtida via equilíbrio global de forças e momentos.
Feedback se errar: Não exatamente. Quando o carregamento é simétrico em relação ao meio do vão, as reações são iguais por simetria e pelo equilíbrio global: R_A = R_B = (q·L + P)/2.

Pergunta 2
Pergunta: A derivada do momento fletor M(x) em relação a x é igual à carga distribuída q(x).
Resposta correta: Falso
Feedback se acertar: Isso mesmo! As relações diferenciais corretas são dM/dx = V e dV/dx = -q(x). Portanto, M'(x) não é igual a q(x); quem se relaciona com q(x) é a derivada do cortante.
Feedback se errar: Quase. As relações corretas são dM/dx = V e dV/dx = -q(x). Ou seja, a variação do cortante está associada à carga distribuída, enquanto a variação do momento está associada ao cortante.

ATIVIDADE VERIFICADORA
AAI – Atividade avaliativa individual

Questão dissertativa
Elabore e justifique, com base nos princípios de equilíbrio e nas relações diferenciais entre esforços, a análise de uma viga simplesmente apoiada de vão L = 6 m, submetida a uma carga distribuída uniforme q = 30 kN/m ao longo de todo o vão e a uma carga concentrada P = 30 kN aplicada no meio do vão. Apresente: (i) as reações de apoio, (ii) a expressão do cortante V(x) por trechos e a identificação de descontinuidades, (iii) a expressão do momento fletor M(x) por trechos, (iv) o valor e a posição do momento máximo, comentando a coerência dos sinais adotados.

Resposta esperada
Pelo equilíbrio global e simetria do carregamento: R_A = R_B = (q·L + P)/2 = (30·6 + 30)/2 = 105 kN. A carga concentrada em x = 3 m produz um salto no diagrama de V de magnitude P. Usando as relações diferenciais dM/dx = V e dV/dx = -q(x):
- Trecho 1 (0 ≤ x < 3 m): V(x) = R_A - qx = 105 - 30x; M(x) = ∫V dx = 105x - 15x² + C, com M(0) = 0 ⇒ C = 0 ⇒ M(x) = 105x - 15x².
- Salto em x = 3 m: V(3⁺) = V(3⁻) - P = (105 - 90) - 30 = -15 kN.
- Trecho 2 (3 < x ≤ 6 m): V(x) = R_A - qx - P = 105 - 30x - 30 = 75 - 30x; M(x) = 75x - 15x² + C'. Continuidade de M em x = 3 m: M(3⁻) = 105·3 - 15·9 = 180 kN·m ⇒ 180 = 75·3 - 15·9 + C' = 180 + C' ⇒ C' = 0 ⇒ M(x) = 75x - 15x².
O momento máximo ocorre no ponto onde V(x) = 0. No trecho 1, V = 0 em x = 3,5 m (> 3 m), portanto não se aplica. No trecho 2, V = 0 em x = 2,5 m (< 3 m), portanto não se aplica. Pelo carregamento simétrico, o máximo está em x = 3 m (meio do vão): M_max = M(3) = 180 kN·m, que também pode ser obtido por superposição: M_max = qL²/8 + P·L/4 = 30·36/8 + 30·6/4 = 135 + 45 = 180 kN·m. Os sinais adotados são coerentes com a convenção usual (M positivo “sorriso”, V positivo conforme convenção escolhida) e as condições de contorno M(0) = M(6) = 0 são satisfeitas.

Critérios de Avaliação (Rubrica) — Total: 10,0 pontos
- Entendimento e formulação do problema (clareza do cenário, dados e objetivos): 1,0
- Equilíbrio global e reações de apoio (cálculo correto de R_A e R_B): 2,0
- Diagrama de esforço cortante V(x) por trechos e identificação do salto em x = 3 m: 2,0
- Diagrama de momento fletor M(x) por trechos, condições de contorno e continuidade em x = 3 m: 2,0
- Momento máximo (valor numérico e posição) com justificativa adequada: 2,0
- Convenção de sinais, organização e apresentação (notação, unidades, coerência): 1,0

Observações para correção
- Conceder crédito parcial quando a metodologia estiver correta mas houver erro aritmético isolado.
- Penalizar ausência de justificativas (apenas resultado numérico) em até 50% do item correspondente.
- Exigir unidades em todos os resultados numéricos; faltas recorrentes podem deduzir até 0,5 no total.

PARA MERGULHAR NO ASSUNTO (SAIBA MAIS)
Texto provocativo para explorar mais o conteúdo:
Falhas em pontes raramente decorrem de uma única causa. Normalmente combinam estimativa inadequada de cargas, detalhes construtivos sensíveis, materiais fora de especificação e, sobretudo, manutenção insuficiente. Ler e interpretar V(x) e M(x) ajuda a prever onde surgirão fissuras, fadiga e recalques. No mercado, isso se traduz em competências para inspeção, diagnóstico, reforço (retrofitting) e monitoramento estrutural (SHM), além de projetos mais robustos e resilientes. Reflita: como um novo corredor de caminhões ou uma obra vizinha desloca reações, altera o ponto de momento máximo e acelera patologias?

Recomendações
- Série/Documentário: NOVA – Why Bridges Collapse (lições aprendidas a partir de colapsos reais).
- Série: National Geographic – Megastructures (episódios dedicados a grandes pontes e seus desafios).
- Canal (YouTube): Practical Engineering (explicações claras sobre cargas, esforços e pontes).
- Livro (divulgação): Structures: Or Why Things Don’t Fall Down — J. E. Gordon.
- Livro: To Engineer Is Human — Henry Petroski (engenharia, falhas e aprendizado com erros).
- Blog/Artigo: FHWA – Bridge Preservation (boas práticas de inspeção e manutenção).
- Dica de visita: Catavento Cultural (SP) — exposições interativas de física e estruturas.
- Dica de visita: Museu de Ciências e Tecnologia da PUCRS — experimentos sobre forças, materiais e estabilidade.

Links:
- https://www.pbs.org/wgbh/nova/video/why-bridges-collapse/
- https://www.youtube.com/results?search_query=megastructures+bridges
- https://www.youtube.com/c/PracticalEngineering
- https://www.goodreads.com/book/show/64234.Structures
- https://www.goodreads.com/book/show/104.To_Engineer_Is_Human
- https://www.fhwa.dot.gov/bridge/preservation/
- https://www.cataventocultural.org.br/
- https://www.pucrs.br/mct/

PODCAST (curadoria | até 45min)
Texto provocativo para estimular a escuta do podcast:
Projetar e manter pontes exige compreender como diferentes tipologias distribuem esforços e como pequenas variações de carga ou apoio modificam V(x) e M(x). Ouvir uma discussão direta e objetiva sobre os tipos de pontes ajuda a conectar teoria (equilíbrio e esforços internos) com decisões reais de projeto e manutenção.

NOME DO PODCAST: Practical Engineering (YouTube)
NOME DO EPISÓDIO: Every Kind of Bridge Explained in 15 Minutes
Link: https://www.youtube.com/watch?v=DX_zkaK5PaI

ARTIGO CIENTÍFICO
Texto provocativo para leitura do artigo científico:
Como levar o raciocínio de esforços internos (V e M) e equilíbrio estático para a prática de inspeção e manutenção de pontes? A leitura propõe um panorama crítico dos desafios para monitorar, diagnosticar e prever o desempenho estrutural em serviço, conectando teoria de carregamentos e respostas estruturais a tecnologias de instrumentação e análise de dados usadas no mercado (sensoriamento, aquisição, processamento e decisão).

Link:
https://doi.org/10.3390/s21134336

Referência bibliográfica (ABNT):
RIZZO, Piervincenzo; ENSHAEIAN, Alireza. Challenges in Bridge Health Monitoring: A Review. Sensors, Basel, v. 21, n. 13, p. 4336, jun. 2021.
