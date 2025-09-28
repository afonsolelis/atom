## Aula 1 – Fundamentos das Vibrações Estruturais

#### 1. Introdução: Cargas Estáticas vs. Dinâmicas

Em engenharia de estruturas, tradicionalmente lidamos com **cargas estáticas**, que são aplicadas de forma lenta e gradual, como o peso próprio da estrutura ou a mobília em um edifício. No entanto, muitas ações importantes são **dinâmicas**: sua magnitude, direção ou ponto de aplicação variam rapidamente no tempo. Exemplos incluem ventos, sismos, explosões e vibrações de máquinas.

![Pêndulo de Newton ilustrando impactos (carga dinâmica)](https://upload.wikimedia.org/wikipedia/commons/d/d3/Newtons_cradle_animation_book_2.gif)

A principal diferença é que cargas dinâmicas geram **forças de inércia** (lembre-se da Segunda Lei de Newton, F=ma), que se opõem à aceleração e alteram completamente a resposta da estrutura.

#### 2. O Modelo Fundamental: Sistema Massa-Mola-Amortecedor

Para entender o comportamento dinâmico, simplificamos uma estrutura complexa em um modelo com um único grau de liberdade (1 GDL).

![Diagrama clássico massa–mola–amortecedor](https://upload.wikimedia.org/wikipedia/commons/3/36/Spring%E2%80%93mass%E2%80%93damper_system.svg)

Este modelo é composto por três elementos:

*   **Massa (M):** Representa a inércia da estrutura. Em um edifício, seria a massa concentrada no nível do pavimento.
*   **Mola (Rigidez, k):** Representa a capacidade da estrutura de resistir à deformação. Em um pórtico, seria a rigidez lateral combinada dos pilares.
*   **Amortecedor (Amortecimento, c):** Representa a dissipação de energia da estrutura, que faz com que a vibração diminua e pare. Ocorre por atrito interno no material, interação com elementos não estruturais, etc.

#### 3. Vibração Livre Não Amortecida: A Essência da Estrutura

Vamos analisar o caso mais simples: uma estrutura que é deslocada de sua posição de equilíbrio e solta, sem a ação de forças externas e sem amortecimento (`c=0`). Ela oscilará perpetuamente em um movimento harmônico simples.

Dois parâmetros fundamentais governam esse movimento:

*   **Frequência Natural (ωn):** É a frequência na qual o sistema "prefere" vibrar. Depende apenas da rigidez e da massa. Uma estrutura mais rígida vibra mais rápido, enquanto uma mais pesada vibra mais devagar.

    $
    \omega_n = \sqrt{\frac{k}{M}} \quad (\text{rad/s})
    $
*   **Período Natural (Tn):** É o tempo que a estrutura leva para completar um ciclo de vibração. É o inverso da frequência.

    $
    T_n = \frac{2\pi}{\omega_n} \quad (\text{s})
    $

O período natural é o "DNA" dinâmico de uma estrutura. Um arranha-céu tem um período longo (vários segundos), enquanto uma estrutura baixa e rígida tem um período curto (frações de segundo).

#### 4. Vibração Livre Amortecida: O Comportamento Real

Na realidade, toda estrutura dissipa energia. O amortecimento faz com que a amplitude da vibração livre diminua com o tempo. A forma como isso acontece depende da **taxa de amortecimento (ζ)**, um valor adimensional que compara o amortecimento real do sistema com o "amortecimento crítico".

![Regimes de amortecimento: subcrítico, crítico e supercrítico](https://upload.wikimedia.org/wikipedia/commons/f/fd/Damping_1.svg)

*   **Amortecimento Subcrítico (ζ < 1):** O sistema oscila, mas com amplitude decrescente até parar. Este é o caso de 99% das estruturas de engenharia civil.
*   **Amortecimento Crítico (ζ = 1):** O sistema retorna à posição de equilíbrio o mais rápido possível, sem oscilar.
*   **Amortecimento Supercrítico (ζ > 1):** O sistema retorna à posição de equilíbrio lentamente, sem oscilar (ex: um amortecedor de porta).

#### 5. Pontos-Chave da Aula
1.  Cargas dinâmicas geram forças de inércia que são cruciais na análise.
2.  O comportamento dinâmico pode ser entendido pelo modelo simplificado **massa-mola-amortecedor**.
3.  Toda estrutura possui uma **frequência natural (ωn)** e um **período natural (Tn)**, que dependem apenas de sua massa e rigidez.
4.  O **amortecimento (ζ)** é a propriedade que dissipa a energia de vibração.

#### 6. Preparação para a Próxima Aula
Na próxima aula, investigaremos o que acontece quando uma força externa contínua atua sobre a estrutura, introduzindo o conceito de **vibração forçada** e o perigoso fenômeno da **ressonância**.
