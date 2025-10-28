## Aula 2 – Normas Técnicas e Critérios Básicos

##### Objetivos da aula
- Reconhecer o arcabouço normativo essencial (ABNT NBR 6118/6120/6122, DNIT) aplicado a pilares e estruturas.
- Aplicar critérios básicos: dimensões mínimas, cobrimento nominal (CAA), limites de armadura e excentricidade mínima.
- Entender diretrizes de detalhamento (armadura longitudinal/ transversais) e noção de verificação de 2ª ordem.

##### Conteúdo da aula (texto base)

![Esquema de pilar e caminho de cargas (local)](assets/pilar_esquema.svg)


**1) Panorama normativo (Brasil)**

- ABNT NBR 6118 (Estruturas de Concreto – Procedimento):
	- Materiais
	- Estados limites
	- Critérios de dimensionamento e detalhamento de pilares (flexo‑compressão, 2ª ordem, armaduras, cobrimentos etc.)
- ABNT NBR 6120 (Ações em edificações) e NBR 6122 (Fundações):
	- Cargas e interações
	- Impactos na definição de esforços em pilares e em ligações com a fundação
- Outras referências:
	- NBR 15575 (Desempenho)
	- NBR 7480 (Aço CA‑50/CA‑60)
	- Documentos DNIT/Manuais (quando houver integração com pavimentação/infraestrutura)


**2) Dimensão mínima da seção e cobertura (cobrimento)**

- Dimensão mínima:
	- Para pilares em concreto armado de seção retangular/quadrada, adota‑se comumente dimensão mínima de 19 cm (conforme prática normativa vigente)
	- Observar limitações de execução e ancoragem
- Cobrimento nominal:
	- Depende da Classe de Agressividade Ambiental (CAA)
	- Exemplo: CAA II (urbana) → cobrimento nominal típico da ordem de 30 mm (ajustar conforme elemento e norma vigente)
	- O cobrimento assegura durabilidade (proteção à armadura contra corrosão e fogo)

![Vergalhões (rebar) – armadura longitudinal de pilares](https://upload.wikimedia.org/wikipedia/commons/f/fe/A_bunch_of_rebar.jpg)


**3) Armadura longitudinal e transversal – limites usuais**

- Longitudinal:
	- Relação de armadura $\rho_l = A_s/A_c$ entre 0,4% e 8% (valores usuais normativos)
	- Diâmetro mínimo típico para barras longitudinais: 10,0 mm
	- Recomenda‑se boa distribuição e verificação de espaçamentos mínimos entre barras e cobrimento
- Transversal (estribos/amarração):
	- Espaçamentos máximos limitados por norma (associados ao menor entre múltiplos do diâmetro da barra longitudinal, dimensões da seção e limites absolutos)
	- Função: confinamento, ancoragem e prevenção de instabilidade local das barras


**4) Excentricidade mínima e flexo‑compressão**

- Pilares raramente são comprimidos de forma centrada:
	- Sempre adotar excentricidade mínima normativa $e_{\min}$ (para cobrir imperfeições geométricas e de carregamento) além dos momentos de primeira ordem calculados
	- O dimensionamento é feito em flexo‑compressão normal (um plano) ou oblíqua (dois planos)
- Verificação de 2ª ordem:
	- Quando a esbeltez/instabilidade exige, amplificar momentos de 1ª ordem por coeficientes normativos (ex.: $M_{d,2}=\gamma_z\,M_{d,1}$, com $\gamma_z$ calculado segundo critérios da norma)
	- Ou empregar análise de 2ª ordem


**5) Interface com fundações e ligações**

- Transferência de esforços no nó pilar–bloco/sapata/estaca:
	- Atenção a punção e tensões de contato
	- Detalhar ancoragens e o arranjo de armaduras
- Ações do solo/fundação podem introduzir excentricidades adicionais:
	- Coordenar com NBR 6122


**6) Exemplo numérico – checagem básica**

- Pilar 25×40 cm ($A_c=0{,}10$ m^{2}), CAA II (urbana), cobrimento nominal adotado: 30 mm
- Supor armadura longitudinal provisória ($A_s=6\varphi 16$) [área total ($A_s\approx 1206$ mm^{2})]
- Verificar $\rho_l$:
	- $\rho_l=A_s/A_c=1206/100000\approx 1{,}21\%$ → dentro de 0,4% a 8%
	- Diâmetro de 16 mm atende ao diâmetro mínimo (≥10 mm)
	- Cobrimento 30 mm compatível com CAA II (confirmar requisitos específicos por elemento na norma)


##### Atividade prática

- Para um pilar 30×50 cm em CAA III, proponha:
	1. Dimensão mínima verificada
	2. Cobrimento nominal
	3. Arranjo preliminar de barras longitudinais (diâmetro e quantidade) para $\rho_l$ entre 0,6% e 2%
	4. Esboce o detalhamento de estribos (diâmetro e espaçamento), justificando com a norma

##### Links suplementares da Aula 2
- ABNT (site): https://www.abnt.org.br/
- NBR 6118 (referência geral): https://pt.wikipedia.org/wiki/Concreto_armado
- Rebar (Wikipedia): https://en.wikipedia.org/wiki/Rebar
- Concrete cover (conceito): https://en.wikipedia.org/wiki/Concrete_cover
