## Aula 11 – Pavimentos Asfálticos (Flexíveis)

##### Objetivos da aula
- Compreender a teoria elástica multicamadas e a distribuição de tensões/deformações em pavimentos flexíveis.
- Aplicar critérios de fadiga (trinca por tração no fundo do revestimento) e deformação permanente (afundamento no subleito).
- Conhecer linhas gerais dos métodos de dimensionamento DNIT e AASHTO.

##### Conteúdo da aula (texto base)

1) Modelo elástico multicamadas (Burmister)
- Representação: camadas horizontais homogêneas, com módulos $E_i$ e Poisson $\nu_i$, espessuras $h_i$, sobre subleito semi-infinito; carga de roda distribuída (pressão de contato $p$) aplicada na superfície.
- Saídas de interesse: deformação de tração no fundo do revestimento $\varepsilon_t$ (governa fadiga) e deformação vertical de compressão no topo do subleito $\varepsilon_z$ (governa deformação permanente).
- Observações: $E$ das misturas asfálticas depende de temperatura/frequência (módulo dinâmico). A rigidez de base/sub-base influencia a repartição de esforços e a espessura ótima das camadas.

2) Critérios de projeto: fadiga e deformação permanente
- Fadiga por tração no fundo do revestimento (Bottom-Up Cracking):

$
N_f = k_1\,\left( \dfrac{1}{\varepsilon_t} \right)^{k_2}\,\left( \dfrac{1}{E_1} \right)^{k_3}
$

- Deformação permanente (afundamento por consolidação/cisalhamento):

$
N_d = c_1\,\left( \dfrac{1}{\varepsilon_z} \right)^{c_2}
$

3) Método DNIT e AASHTO (visão geral)
- AASHTO 1993 (SN – Structural Number): $SN = a_1 h_1 + a_2 m_2 h_2 + a_3 m_3 h_3 + \dots$ com coeficientes de camada $a_i$, fatores de drenagem $m_i$, MR do subleito e confiabilidade.
- DNIT: verificação simultânea de $\varepsilon_t$ e $\varepsilon_z$ via modelos multicamadas e critérios calibrados (tráfego, clima, materiais, desempenho).

4) Exemplo orientado (esboço)
- Dados: N (cargas equivalentes), MR do subleito, $E$ e $\nu$ das camadas (revestimento/base/sub-base), temperatura de projeto. Obter $\varepsilon_t$ e $\varepsilon_z$ e verificar $N_f$ e $N_d$. Ajustar espessuras até atender os critérios.

![Execução de pavimento asfáltico (ilustrativo)](https://upload.wikimedia.org/wikipedia/commons/7/76/AF-asphalt-laying-machine.jpg)

##### Atividade prática
- Modele um pavimento flexível (revestimento/base/sub‑base) em software multicamadas, obtenha $\varepsilon_t$ e $\varepsilon_z$ e verifique os critérios de $N_f$ e $N_d$. Ajuste espessuras até atender simultaneamente.

##### Links suplementares da Aula 11
- Asphalt concrete (Wikipedia): https://en.wikipedia.org/wiki/Asphalt_concrete
- Mechanistic–empirical pavement design (Wikipedia): https://en.wikipedia.org/wiki/Mechanistic%E2%80%93empirical_pavement_design
- AASHTO pavement design (Wikipedia): https://en.wikipedia.org/wiki/AASHTO

##### Pontos‑chave
- $\varepsilon_t$ e $\varepsilon_z$ governam fadiga e trilha; módulos variam com temperatura/frequência.
- Camadas granulares e sub‑bases rígidas reduzem $\varepsilon_z$ e prolongam vida.
- AASHTO usa SN; DNIT verifica respostas mecanísticas com critérios calibrados.
- Dimensionamento é iterativo e integrado a drenagem e confiabilidade.
