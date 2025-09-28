## Aula 2 – Excitação Harmônica, Ressonância e Amortecimento

#### 1. Força Dinâmica Harmônica: conceito e equação de movimento
Quando uma estrutura sofre a ação de uma força que varia no tempo de forma periódica, dizemos que está sob excitação harmônica. Para um sistema de 1 GDL, a equação diferencial é:

$M\,\ddot u(t) + c\,\dot u(t) + k\,u(t) = p_0\,\sin(\omega t)$

onde $M$ é a massa equivalente, $c$ o amortecimento viscoso, $k$ a rigidez, $p_0$ a amplitude da força e $\omega$ a frequência de excitação.

Definimos ainda:
- Frequência natural: $\omega_n = \sqrt{\tfrac{k}{M}}$ e $f_n = \tfrac{\omega_n}{2\pi}$
- Razão de amortecimento: $\zeta = \tfrac{c}{2\sqrt{kM}}$
- Razão de frequência: $r = \tfrac{\omega}{\omega_n}$

![Oscilador harmônico sob força senoidal](https://upload.wikimedia.org/wikipedia/commons/2/22/Harmonic_oscillator.svg)

#### 2. Resposta em regime permanente e fator de amplificação
A resposta após o transitório é harmônica com a mesma frequência da excitação, mas com amplitude e fase diferentes. A amplitude $U$ do deslocamento em regime permanente é:

$U = \dfrac{p_0/k}{\sqrt{\big(1-r^2\big)^2 + \big(2\zeta r\big)^2}} \quad\Rightarrow\quad \text{FA} = \dfrac{U}{p_0/k}$

O ângulo de fase $\varphi$ entre a força e o deslocamento é:

$\tan\varphi = \dfrac{2\zeta r}{1-r^2}$

Observações práticas em estruturas de concreto:
- Para $r \ll 1$, o comportamento é quase estático ($\text{FA}\approx 1$).
- Perto de $r=1$ (ressonância), o amortecimento controla a amplitude. Em concreto armado, $\zeta$ típico está entre 2% e 5%.
- Para $r \gg 1$, o deslocamento decai, mas a resposta de aceleração pode crescer.

#### 3. Exemplo numérico aplicado
Considere um pórtico representado por $M=10\,000\ \text{kg}$, $k=2{\times}10^7\ \text{N/m}$ e $\zeta=5\%$. Uma força dinâmica $p_0=10\,000\ \text{N}$ atua com $\omega=\omega_n$.

- $\omega_n = \sqrt{k/M} = \sqrt{2{\times}10^7/10^4} = \sqrt{2000} \approx 44{,}72\ \text{rad/s}$, $f_n\approx 7{,}12\ \text{Hz}$
- Em ressonância ($r=1$), $\text{FA} = \dfrac{1}{2\zeta} = \dfrac{1}{0{,}10} = 10$
- Deslocamento estático $= p_0/k = 10{,}000/2{\times}10^7 = 5{\times}10^{-4}\ \text{m}$
- Deslocamento dinâmico $U = 10 \times 5{\times}10^{-4} = 5{\times}10^{-3}\ \text{m} = 5\ \text{mm}$

Conclusão: um leve amortecimento limita a amplitude, mas perto da ressonância ainda ocorrem deslocamentos significativamente maiores que os estáticos.

#### 4. Excitação por base (sismos e máquinas)
Quando a base se move, como em um sismo, a entrada é um deslocamento de base $y(t)$ e a variável de interesse é o deslocamento relativo $u_r(t)$ da massa em relação à base.

$M\,\ddot u_r + c\,\dot u_r + k\,u_r = -M\,\ddot y(t)$

Ideias-chave:
- Em análise sísmica, trabalhamos com espectros de resposta (deslocamento, velocidade, pseudo-aceleração). O pico de pseudo-aceleração $S_a$ aproxima a força inercial máxima $F\!\_\text{in} \approx M\,S_a$.
- Para máquinas, isoladores (molas e amortecedores) são projetados para operar com $r>\sqrt{2}$ visando reduzir transmissibilidade de forças ao apoio.

![Esquema de isolação/base excitada](https://upload.wikimedia.org/wikipedia/commons/9/90/Passvib1.svg)

#### 5. Vento, desprendimento de vórtices e pilares esbeltos
Além de rajadas aleatórias, o vento pode induzir vibrações por desprendimento periódico de vórtices. A frequência de shedding $f\_s$ é estimada por $f\_s = \mathrm{St}\,\dfrac{U}{D}$, com $\mathrm{St}\approx 0{,}2$ para seções circulares, $U$ a velocidade do vento e $D$ a dimensão característica. Evite $f\_s \approx f_n$ para não excitar ressonância transversal em pilares e mastros.

Medidas de projeto:
- Ajustar rigidez e massa para deslocar $f_n$.
- Aumentar amortecimento com dispositivos ou detalhes construtivos.
- Usar chanfros, aletas ou rugosidade para alterar o escoamento e reduzir $\mathrm{St}$ efetivo.

#### 6. Boas práticas e checklist de projeto
- Identificar $\omega_n$, $\zeta$ e principais fontes de excitação (sismo, vento, máquinas, tráfego).
- Verificar razão $r$ para cenários críticos; se $r\approx 1$, avaliar FA e respostas de deslocamento/aceleração.
- Para equipamentos sensíveis, checar transmissibilidade e adotar isolação quando necessário.
- Considerar limites de conforto ao invés de apenas resistência (vibração de pisos, passarelas, escritórios).


#### 7. Atividade prática sugerida
Observe uma estrutura de concreto do seu cotidiano (prédio, ponte, passarela, laje, etc.) e procure identificar situações em que vibrações podem ser percebidas (ex: pessoas pulando em lajes, veículos passando em pontes, máquinas funcionando próximas a estruturas). Anote:
- O tipo de estrutura e o local observado.
- O que pode causar vibração naquele elemento (tráfego, vento, máquinas, etc.).
- Se é possível perceber vibrações (pelo tato, objetos tremendo, ruídos, etc.).
- Relacione, com base no conteúdo da aula, como fatores como frequência natural, ressonância e amortecimento podem influenciar a vibração percebida.
Se possível, tire uma foto (opcional) e anexe ao seu relatório.

#### 8. Pontos-chave
- A ressonância ocorre quando $\omega\approx\omega_n$ e o amortecimento controla a amplitude máxima.
- Excitação por base (sísmica) acopla a resposta à aceleração do terreno; o uso de espectros facilita o dimensionamento.
- Em pilares esbeltos, verificar efeitos de vento e shedding para evitar vibrações excessivas e fadiga.
