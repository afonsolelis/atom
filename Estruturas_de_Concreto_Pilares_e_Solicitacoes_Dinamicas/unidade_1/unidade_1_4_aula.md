## Aula 4 – Dimensionamento de Pilares à Flexo-compressão

##### Objetivos da aula
- Compreender os conceitos e métodos para dimensionamento de pilares submetidos a flexo-compressão normal e oblíqua.
- Aplicar diagramas de interação e verificação de seções de concreto armado sob esforços combinados.
- Reconhecer estratégias de dimensionamento e detalhamento para atender requisitos de segurança e desempenho.

##### Conteúdo da aula (texto base)

![Esquema de pilar e caminho de cargas (local)](assets/pilar_esquema.svg)

1) Introdução ao dimensionamento de pilares
- O dimensionamento de pilares submetidos a flexo-compressão combina esforços normais de compressão e momentos fletores em uma ou duas direções. O processo envolve verificação da capacidade resistente da seção considerando as interações entre os materiais (concreto e aço) e os esforços solicitantes.
- A abordagem normativa contempla o dimensionamento tanto para flexo-compressão normal (um plano) quanto para flexo-compressão oblíqua (dois planos), com requisitos específicos para verificação de segurança em Estados Limites Últimos (ELU).

2) Diagramas de interação – base para verificação
- Diagramas de interação representam graficamente a capacidade resistente de uma seção de concreto armado submetida a esforços combinados (N, M). A curva de interação define os pares (N, M) que levam a seção à ruína (momento resistente último para determinado esforço normal ou vice-versa).
- A forma do diagrama de interação varia com as características da seção (dimensões, distribuição de armadura, resistência dos materiais), sendo fundamental para a verificação de segurança.

<img src="https://upload.wikimedia.org/wikipedia/commons/4/45/Fractured_reinforced_concrete_column.JPG" alt="Coluna de concreto armado fissurada com exposição de armadura (exemplo real)" style="width:30%;">
Fonte: Wikimedia Commons – Fractured reinforced concrete column

3) Flexo-compressão normal – um plano
- No caso de flexo-compressão normal, a seção é solicitada por um esforço normal de compressão N e um momento fletor M em apenas um plano. A verificação envolve o cálculo da capacidade resistente da seção e a comparação com os esforços solicitantes (N_d, M_d).
- A posição da linha neutra é determinada iterativamente para equilibrar os esforços normais e os momentos fletores atuantes, considerando as leis constitutivas do concreto e do aço.

4) Flexo-compressão oblíqua – consideração simultânea em dois planos
- A flexo-compressão oblíqua ocorre quando há momentos fletores atuando simultaneamente nas duas direções principais da seção (M_x e M_y). A verificação exige análise mais complexa, considerando a interação tridimensional entre N, M_x e M_y.
- Métodos normativos contemplam simplificações (ex.: método da excentricidade combinada, método da interação de momentos) que substituem verificações rigorosas, mantendo segurança adequada.

5) Verificação da seção e dimensionamento da armadura
- O dimensionamento envolve a definição da armadura longitudinal necessária para resistir aos esforços combinados. A armadura transversal (estribos) é dimensionada para confinar as barras longitudinais e resistir a esforços de cisalhamento, prevenindo instabilidade local.
- O cálculo pode ser feito por iterações manuais, tabelas de dimensionamento ou programas computacionais que traçam os diagramas de interação e determinam a armadura necessária.

6) Equações fundamentais para dimensionamento
- A verificação envolve as equações de equilíbrio de forças e momentos na seção transversal. A força normal resistente é dada por:
$$
N_{Rd} = N_c + N_s - N_t
$$
onde $N_c$ é a contribuição do concreto, $N_s$ e $N_t$ são as contribuições das armaduras comprimida e tracionada, respectivamente.
- O momento fletor resistente é calculado em relação ao centroide da seção:
$$
M_{Rd} = M_c + M_s + M_t
$$



7) Exemplo numérico – dimensionamento simplificado
- Considere um pilar de seção 30×50 cm, concreto C25 ($f_{ck} = 25$ MPa), aço CA-50 ($f_{yk} = 500$ MPa), com esforços solicitantes de cálculo: $N_d = 1500$ kN; $M_{d,x} = 120$ kN·m; $M_{d,y} = 60$ kN·m. A seção é submetida a flexo-compressão oblíqua.
- Supondo distribuição simétrica de armadura (8 barras de 20 mm, área total $A_s \approx 2513$ mm²), verificar a segurança:
  - Calcular $f_{cd} = f_{ck}/\gamma_c = 25/1{,}4 \approx 17{,}86$ MPa
  - Calcular $f_{yd} = f_{yk}/\gamma_s = 500/1{,}15 \approx 434{,}78$ MPa
  - Verificar se os esforços solicitantes ($N_d$, $M_{d,x} = 120$ kN·m, $M_{d,y} = 60$ kN·m) estão abaixo da capacidade resistente da seção com a armadura proposta, usando diagramas de interação ou critérios normativos.
  - A taxa de armadura $\rho = A_s/A_c = 2513/[300\times 500] \approx 1{,}67\%$, dentro dos limites normativos (0,4% ≤ $\rho$ ≤ 8%).

8) Detalhamento e execução
- O detalhamento das armaduras deve seguir normas específicas, com comprimentos de ancoragem adequados, ganchos onde necessário e espaçamento entre estribos que atendam ao confinamento e à prevenção de flambagem local.
- Na execução, o posicionamento correto das armaduras e o controle do cobrimento são cruciais para o desempenho estrutural, especialmente em regiões de alta solicitação.

9) Estratégias de dimensionamento e boas práticas
- Distribuir a armadura de forma apropriada (mínimo de 4 barras para seções retangulares, preferencialmente armadura dupla-face em faces maiores) para melhor desempenho sob flexo-compressão oblíqua.
- Considerar a interação entre os esforços e verificar se as armaduras mínimas e máximas normativas são obedecidas.
- Adotar cobrimentos adequados e espaçamentos entre barras que permitam a concretagem adequada e a transferência de esforços entre materiais.

![Armação de pilar (detalhe de armadura longitudinal e estribos)](https://upload.wikimedia.org/wikipedia/commons/b/bb/Arma%C3%A7%C3%A3o_de_pilar_-_Mutir%C3%A3o_do_Projeto_Arquiteto_de_Familia.JPG)
Fonte: Wikimedia Commons – Armação de pilar - Mutirão do Projeto Arquiteto de Familia

##### Atividade prática
- Dimensione a armadura longitudinal para um pilar de seção 25×40 cm submetido a:
  1) Esforços de cálculo: $N_d = 1200$ kN; $M_{d,x} = 80$ kN·m; $M_{d,y} = 40$ kN·m.
  2) Concreto C30, aço CA-50, cobrimento nominal de 30 mm (CAA II).
  3) Compare os resultados com os limites normativos de armadura (0,4% a 8%) e esboce o detalhamento da seção.
  4) Discuta como a distribuição e o posicionamento das barras influenciam a capacidade resistente nos dois planos.

##### Pontos-chave
- O dimensionamento de pilares à flexo-compressão exige análise combinada de esforços normais e momentos fletores.
- Diagramas de interação são ferramentas essenciais para verificação da capacidade resistente das seções.
- Em flexo-compressão oblíqua, os esforços nos dois planos principais devem ser considerados simultaneamente.
- O detalhamento adequado das armaduras é fundamental para transferência de esforços e desempenho da estrutura.

##### Links suplementares da Aula 4
- Interaction diagrams in reinforced concrete: https://en.wikipedia.org/wiki/Interaction_diagram
- Reinforced concrete design: https://en.wikipedia.org/wiki/Reinforced_concrete
- ABNT NBR 6118: https://en.wikipedia.org/wiki/ABNT_NBR_6118
- Concrete Society Technical Report: https://www.concretecentre.com/
