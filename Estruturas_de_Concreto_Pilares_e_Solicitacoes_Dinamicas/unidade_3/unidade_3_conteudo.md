# TEMPLATE DE PRODUÇÃO - MODELO ÁTOMO

# Nome da disciplina: Estruturas de Concreto: Pilares e Solicitações Dinâmicas
# Conteudista: Afonso Cesar Lelis Brandão

## Tabela para uso exclusivo do(a) coordenador(a)

```
Requisitos para um conteúdo UAU            Observações
```
Conformidade com o Plano de Aprendizado

Clareza e objetividade

Ortografia e gramática

Recursos visuais atrativos (imagens, gifs, etc.)

```
Data da Validação        Nome do(a) Coordenador(a) do curso
```
#### ● VALIDADO ● NÃO VALIDADO ● CANCELADO

```
TEXTO BASE -
TÍTULOS E OBJETIVOS DAS VIDEOAULAS -
QUIZ -
MATERIAL COMPLEMENTAR -
```

# TEXTO BASE

#### Por que esta unidade é relevante para a sua atuação profissional?
Caracterizar adequadamente os materiais geotécnicos é a base de qualquer projeto de infraestrutura. Conhecer fases e índices do solo, sua textura e plasticidade, e selecionar ensaios corretos reduz incertezas, evita patologias (recalques, instabilidade) e otimiza custos de terraplenagem, pavimentação e fundações.

### Contribuições para a atuação profissional
- Dimensiona e controla obras de terra com segurança (aterros, bases, taludes).
- Seleciona parâmetros representativos de projeto (densidades, umidade, plasticidade).
- Interpreta ensaios de campo e laboratório para especificação e controle.
- Reduz retrabalhos ao antecipar problemas de compactação e drenagem.

### Exemplos práticos
- Ajuste de umidade e energia de compactação para atingir $\gamma_{d,max}$ e $w_{opt}$ em um aterro.
- Classificação SUCS e Atterberg de um subleito para verificar suscetibilidade a deformações e bombeamento.
- Checagem de densidade in situ de base granular por frasco de areia.

---

#### TEXTO BASE EXPANDINDO HORIZONTES DA VIDEOAULA 1

## Aula 9 – Materiais e Caracterização Geotécnica

##### Objetivos da aula
- Entender o modelo trifásico do solo e índices físicos (e, n, w, $S_r$, $G_s$) e pesos específicos ($\gamma_d$, $\gamma$, $\gamma_{sat}$, $\gamma'$).
- Aplicar classificação por granulometria e limites de Atterberg.
- Conhecer ensaios usuais de caracterização (umidade, $G_s$, granulometria, Atterberg, Proctor) e de campo (SPT, densidade in situ).

##### Conteúdo da aula (texto base)

1) Fases do solo e relações de fase
- Índice de vazios: $e = \dfrac{V_v}{V_s}$; Porosidade: $n = \dfrac{V_v}{V} = \dfrac{e}{1+e}$; Umidade: $w = \dfrac{m_w}{m_s}$; Grau de saturação: $S_r = \dfrac{V_w}{V_v}$; Massa específica relativa: $G_s = \dfrac{\rho_s}{\rho_w}$.
- Pesos específicos: $\gamma_d = \gamma_w\,\dfrac{G_s}{1+e}$; $\gamma = \gamma_w\,\dfrac{G_s + S_r\,e}{1+e}$; $\gamma_{sat} = \gamma_w\,\dfrac{G_s + e}{1+e}$; $\gamma' = \gamma_{sat} - \gamma_w$.

2) Granulometria, plasticidade e classificação
- Curva granulométrica (peneiras/hidrómetro), coeficientes $C_u$ e $C_c$ e uniformidade.
- Limites de Atterberg (LL, LP) e índice de plasticidade $IP = LL - LP$.
- Classificação SUCS/HRB e implicações em comportamento (permeabilidade, compactação, retração).

![Triângulo textural do solo](https://upload.wikimedia.org/wikipedia/commons/6/65/SoilTextureTriangle.jpg)

3) Ensaios usuais de laboratório
- Umidade (estufa); Massa específica dos grãos (picnômetro); Granulometria (peneiras e hidrómetro); Atterberg (Casagrande/cone); Compactação (Proctor).

4) Ensaios de campo e amostragem
- Amostras deformadas/indeformadas; SPT (índice de resistência) para correlações; Densidade in situ (frasco de areia/balão/nuclear).

5) Exemplo numérico (relações de fase)
Dados: $G_s=2{,}70$, $e=0{,}75$, $S_r=60\%$. Calcule $n$, $\gamma$ e $\gamma_d$.

$
\begin{aligned}
 n &= \dfrac{e}{1+e} = \dfrac{0{,}75}{1{,}75} = 0{,}4286\ (42{,}9\%) \\
 \gamma_d &= \gamma_w\,\dfrac{G_s}{1+e} = 9{,}81\,\dfrac{2{,}70}{1{,}75} = 15{,}14\ \text{kN/m}^3 \\
 \gamma &= \gamma_w\,\dfrac{G_s + S_r\,e}{1+e} = 9{,}81\,\dfrac{2{,}70 + 0{,}60\times 0{,}75}{1{,}75} = 16{,}70\ \text{kN/m}^3
\end{aligned}
$

##### Roteiro da videoaula 9 (resumo)
- Abertura e objetivos (1 min) | Relações de fase (5 min) | Granulometria/Atterberg/Classificação (5 min) | Ensaios usuais e exemplo (3–5 min) | Encerramento (1 min).

##### Links suplementares da Aula 9
- Soil mechanics (Wikipedia): https://en.wikipedia.org/wiki/Soil_mechanics
- Atterberg limits (Wikipedia): https://en.wikipedia.org/wiki/Atterberg_limits
- Proctor compaction test (Wikipedia): https://en.wikipedia.org/wiki/Proctor_compaction_test

---

#### VIDEOAULA 9: Aula 9 – Materiais e Caracterização Geotécnica

## Roteiro para a Videoaula 9 – Materiais e Caracterização Geotécnica

**(1) Abertura (1 min)**
*   *Professor na tela:* "Olá! Sou Afonso Cesar Lelis Brandão. Hoje vamos desvendar o solo, o material de construção mais antigo e complexo que existe. Entender suas fases, seus índices e como o caracterizamos é o primeiro passo para qualquer obra de geotecnia segura e econômica. Vamos começar?"

**(2) O Solo em Três Fases (3 min)**
*   *Animação:* Mostrar um diagrama de um volume de solo se separando em três blocos: sólidos, água e ar.
*   *Professor:* "Imaginem o solo como uma esponja. Temos a parte sólida (os grãos), a água preenchendo os poros e o ar. A relação entre eles define tudo! Vamos ver os principais índices: índice de vazios, porosidade, umidade e grau de saturação. Eles nos dizem o quão denso, úmido ou poroso é o nosso solo."
*   *Legendas na tela:* Apresentar as fórmulas de `e`, `n`, `w` e `Sr`.

**(3) Granulometria e Plasticidade: O RG do Solo (4 min)**
*   *Vídeo/Animação:* Mostrar o processo de peneiramento e sedimentação. Em seguida, a preparação de uma amostra para os limites de Atterberg.
*   *Professor:* "Para classificar um solo, fazemos dois 'exames': a granulometria, que separa os grãos por tamanho, e os limites de Atterberg, que medem a plasticidade das argilas. Com isso, obtemos a 'identidade' do solo, como a classificação SUCS, que nos diz se é um pedregulho, uma areia, uma argila e como ele deve se comportar."
*   *Imagem na tela:* Mostrar o triângulo textural e a carta de plasticidade.

**(4) Ensaios: Da Bancada ao Campo (3 min)**
*   *Professor:* "Para obter esses dados, temos uma série de ensaios. No laboratório, determinamos a umidade, a massa específica dos grãos e a curva de compactação com o ensaio de Proctor, que nos dá a umidade ótima para a máxima compactação. Em campo, usamos o SPT para medir a resistência e o frasco de areia para verificar a densidade."
*   *Imagens:* Mostrar equipamentos de laboratório (estufa, picnômetro, aparelho de Casagrande) e de campo (SPT, frasco de areia).

**(5) Exemplo Prático e Encerramento (2 min)**
*   *Professor na tela:* "Vamos aplicar isso. Se temos um solo com Gs de 2,70 e índice de vazios de 0,75, como calculamos seu peso específico? [Mostrar cálculo do exemplo numérico]. É com esses números que projetamos aterros, fundações e pavimentos."
*   *Professor:* "Na próxima aula, vamos usar esses conceitos para projetar pavimentos de concreto. Até lá!"

---

#### TEXTO BASE EXPANDINDO HORIZONTES DA VIDEOAULA 2

## Aula 10 – Pavimentos de Concreto (Rígidos)

##### Objetivos da aula
- Compreender a teoria de placa sobre base elástica (Westergaard) e o papel do módulo de reação do subleito ($k$).
- Dimensionar elementos de pavimentos rígidos: espessura da placa, juntas e transferência de carga.
- Conhecer critérios de projeto e referências normativas do DNIT aplicáveis.

##### Conteúdo da aula (texto base)

1) Fundamentos: placa sobre base elástica (Winkler) – Westergaard
- Modelo: placa de concreto de espessura $h$, módulo $E$ e coeficiente de Poisson $\nu$, apoiada em fundação idealizada por molas independentes de rigidez $k$ (módulo de reação do subleito).
- Raio de rigidez relativa (Westergaard):

$
\ell = \left( \dfrac{E\,h^3}{12\,k\,(1-\nu^2)} \right)^{1/4}
$

- Tensões máximas dependem da posição da carga (interior, borda, quina) e governam o dimensionamento à fadiga/ruptura por flexão. Em geral, borda/quina são casos críticos.

2) Dimensionamento – espessura, juntas e transferência de carga
- Espessura $h$: selecionada para que tensões de flexão de projeto (considerando repetições de tráfego) não excedam a resistência à tração na flexão (módulo de ruptura) do concreto, com verificação de fadiga e segurança contra bombeamento/erosão.
- Juntas: controlar retração e variações térmicas. Definir espaçamento típico (ordem de 4–6 m, ajustar conforme clima, base e armadura), largura de abertura, selante e selagem.
- Transferência de carga:
  - Barras de transferência (dowels) em juntas transversais: aumentam a eficiência de transferência (LTE), reduzem desnível (faulting). Dimensionar diâmetro, comprimento, espaçamento e cobrimento.
  - Barras de costura (tie bars) em juntas longitudinais: manter placas solidárias ao tráfego.
- Camadas de base/sub-base: melhorar suporte ($k$), reduzir bombeamento e erosão; considerar drenagem.

3) Normas DNIT e critérios de projeto
- Referências DNIT para pavimentos rígidos: especificações e manuais com diretrizes para seleção de materiais, espessuras, juntas, detalhes construtivos e controle tecnológico.
- Critérios usuais:
  - Verificação de tensões (interior/borda/quina) x módulo de ruptura (com fadiga).
  - Verificação de LTE/transferência de carga e limite de desnível (faulting).
  - Controle de abertura de juntas, retração e gradientes térmicos.
  - Requisitos de base/sub-base (resistência, drenagem) e $k$ de projeto.

4) Exemplo orientado (esboço)
- Dados: tráfego equivalente (eixos), $k$ do subleito, $E$, $\nu$ e módulo de ruptura do concreto, condições ambientais e de base. Selecionar $h$, definir juntas (espaçamento/largura), especificar barras de transferência/costura e checar tensões críticas com margens de fadiga.

![Pavimento de concreto em serviço (exemplo)](https://upload.wikimedia.org/wikipedia/commons/d/d4/2014-08-29_15_31_39_View_southeast_along_Stuyvesant_Avenue_in_Ewing%2C_New_Jersey%2C_with_concrete_pavement_likely_dating_to_the_1950s.JPG)

##### Atividade prática
- Dimensione um pavimento rígido para tráfego pesado (via industrial):
  - Estime $k$ do subleito (ou adote valor normativo) e defina materiais da base.
  - Escolha $h$ atendendo tensões críticas e fadiga; proponha espaçamento de juntas.
  - Dimensione barras de transferência e de costura (diâmetro, comprimento, espaçamento) e descreva requisitos de execução/controle.

##### Links suplementares da Aula 10
- Concrete pavement (Wikipedia): https://en.wikipedia.org/wiki/Road_surface#Concrete
- Highway engineering – concrete pavements (Wikipedia): https://en.wikipedia.org/wiki/Highway_engineering
- Winkler foundation (Wikipedia): https://en.wikipedia.org/wiki/Winkler_foundation_model
- Harold M. Westergaard (Wikipedia): https://en.wikipedia.org/wiki/Harold_M._Westergaard

##### Pontos‑chave
- Placas de concreto apoiadas em base elástica (Winkler) são dimensionadas por tensões críticas (interior/borda/quina) e fadiga.
- Juntas controlam movimentações; dowels aumentam a transferência de carga, reduzindo faulting e desníveis.
- A base/sub‑base eleva o suporte (k), reduz bombeamento e contribui para durabilidade.
- Projeto integra tráfego, clima, materiais, execução e manutenção para desempenho ao longo do ciclo de vida.

---

#### VIDEOAULA 10: Aula 10 – Pavimentos de Concreto (Rígidos)

## Roteiro para a Videoaula 10 – Pavimentos de Concreto (Rígidos)

**(1) Abertura (1 min)**
*   *Professor na tela:* "Olá! Hoje vamos falar de gigantes: os pavimentos de concreto, ou pavimentos rígidos. Eles são projetados para durar décadas sob tráfego pesado. Mas como eles funcionam? Sou Afonso Cesar Lelis Brandão e vamos mergulhar na teoria das placas."

**(2) A Teoria de Westergaard: Placa sobre Molas (3 min)**
*   *Animação:* Mostrar uma placa de concreto flutuando sobre uma base de molas (modelo de Winkler). Uma carga de pneu é aplicada, e as tensões são mostradas na placa.
*   *Professor:* "O segredo do pavimento rígido é que ele distribui a carga por uma área muito grande. O modelo clássico de Westergaard imagina a placa de concreto apoiada em uma infinidade de pequenas molas, que representam o subleito. A rigidez dessa 'cama de molas' é o módulo de reação k."
*   *Legenda na tela:* Apresentar a fórmula do raio de rigidez relativa `l`.

**(3) Dimensionando a Placa: Espessura e Juntas (4 min)**
*   *Professor:* "O dimensionamento tem dois pilares: a espessura da placa e o sistema de juntas. A espessura é calculada para resistir à flexão causada pelo tráfego, evitando a fadiga do concreto. As juntas são essenciais para controlar a retração do concreto e sua movimentação térmica, evitando trincas aleatórias."
*   *Imagens:* Mostrar diferentes tipos de juntas (transversais, longitudinais) e o posicionamento das barras de transferência e de costura.

**(4) Transferência de Carga e Normas (3 min)**
*   *Animação:* Mostrar como as barras de transferência (dowels) ajudam a transferir a carga de uma placa para a outra, reduzindo o degrau (faulting).
*   *Professor:* "Uma junta sem um bom sistema de transferência de carga é um ponto fraco. As barras de transferência, ou 'dowels', garantem que as placas trabalhem juntas. No Brasil, o DNIT fornece as diretrizes para todo esse dimensionamento, desde a espessura até os detalhes das juntas."

**(5) Encerramento (2 min)**
*   *Professor na tela:* "Projetar um pavimento rígido é um quebra-cabeça que envolve tráfego, materiais, clima e execução. Quando bem feito, o resultado é uma estrutura extremamente durável."
*   *Professor:* "Na nossa próxima aula, vamos comparar os pavimentos rígidos com os flexíveis, os de asfalto. Até lá!"

---

#### TEXTO BASE EXPANDINDO HORIZONTES DA VIDEOAULA 3

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

onde $E_1$ é o módulo do revestimento e $k_i$ são constantes calibradas (dependem da mistura/ensaio). Verificar $N_{\text{aplic}} \le N_f$.

- Deformação permanente (afundamento por consolidação/cisalhamento):

$
N_d = c_1\,\left( \dfrac{1}{\varepsilon_z} \right)^{c_2}
$

Comparar $N_{\text{aplic}}$ com $N_d$ e atender limite de trilha de roda especificado.

3) Método DNIT e AASHTO (visão geral)
- AASHTO 1993 (SN – Structural Number): usa número estrutural $SN = a_1 h_1 + a_2 m_2 h_2 + a_3 m_3 h_3 + \dots$ com coeficientes de camada $a_i$ e fatores de drenagem $m_i$, MR do subleito e confiabilidade para estimar espessuras.
- DNIT: dimensionamento baseado em verificação de $\varepsilon_t$ e $\varepsilon_z$ via modelos multicamadas e critérios calibrados (documentos DNIT/IBRACON), contemplando tráfego (N), clima, materiais e desempenho (fadiga/afundamento).
- Em ambos: iterar espessuras para satisfazer simultaneamente fadiga e deformação permanente com margens de confiabilidade e requisitos construtivos.

4) Exemplo orientado (esboço)
- Dados: N (cargas equivalentes), MR do subleito, $E$ e $\nu$ das camadas (revestimento/base/sub-base), temperatura de projeto. Obtém-se $\varepsilon_t$ (fundo do revestimento) e $\varepsilon_z$ (topo do subleito) por software multicamadas e verifica-se $N_f$ e $N_d$. Ajustar espessuras até atendimento simultâneo dos critérios.

![Execução de pavimento asfáltico (ilustrativo)](https://upload.wikimedia.org/wikipedia/commons/7/76/AF-asphalt-laying-machine.jpg)

##### Atividade prática
- Monte um caso de dimensionamento mecanístico–empírico: defina camadas (espessura e $E$), obtenha $\varepsilon_t$ e $\varepsilon_z$ em software multicamadas e verifique os critérios de fadiga ($N_f$) e deformação permanente ($N_d$). Ajuste espessuras até cumprir ambos com folga mínima.

##### Links suplementares da Aula 11
- Asphalt concrete (Wikipedia): https://en.wikipedia.org/wiki/Asphalt_concrete
- Mechanistic–empirical pavement design (Wikipedia): https://en.wikipedia.org/wiki/Mechanistic%E2%80%93empirical_pavement_design
- AASHTO pavement design (Wikipedia): https://en.wikipedia.org/wiki/AASHTO

##### Pontos‑chave
- Em flexíveis, $\varepsilon_t$ (revestimento) governa fadiga; $\varepsilon_z$ (subleito) governa trilha (rutting).
- Módulos dependem de temperatura/frequência; camadas granulares e sub‑base rígida reduzem $\varepsilon_z$.
- AASHTO usa SN; DNIT enfatiza verificação simultânea de respostas e confiabilidade.
- Dimensionamento é iterativo, integrando tráfego, materiais, clima e drenagem.

---

#### VIDEOAULA 11: Aula 11 – Pavimentos Asfálticos (Flexíveis)

## Roteiro para a Videoaula 11 – Pavimentos Asfálticos (Flexíveis)

**(1) Abertura (1 min)**
*   *Professor na tela:* "Olá! Sou Afonso Cesar Lelis Brandão. Se os pavimentos de concreto são os gigantes rígidos, os pavimentos asfálticos são os atletas flexíveis. Hoje vamos entender como essas múltiplas camadas trabalham juntas para suportar o tráfego."

**(2) O Modelo Multicamadas (3 min)**
*   *Animação:* Mostrar um corte de um pavimento flexível com 3 ou 4 camadas (revestimento, base, sub-base, subleito). Uma carga de pneu é aplicada e as deformações são mostradas em dois pontos críticos.
*   *Professor:* "Diferente do pavimento rígido, o flexível distribui a carga em profundidade, camada por camada. O modelo que usamos é o de múltiplas camadas elásticas. Nosso foco são duas deformações críticas: a de tração na parte de baixo do revestimento asfáltico, que causa a fadiga, e a de compressão no topo do subleito, que causa o afundamento."
*   *Legendas na tela:* Indicar `εt` e `εz` na animação.

**(3) Critérios de Projeto: Fadiga e Deformação Permanente (4 min)**
*   *Professor:* "O dimensionamento é uma luta contra dois inimigos: a trinca por fadiga e a trilha de roda. Para cada um, temos uma 'equação de vida'. Verificamos se o número de cargas que o pavimento aguenta antes de trincar (`Nf`) e antes de afundar (`Nd`) é maior que o tráfego esperado."
*   *Gráficos na tela:* Mostrar as equações de fadiga e deformação permanente.

**(4) Métodos de Dimensionamento: AASHTO e DNIT (3 min)**
*   *Professor:* "Existem diferentes 'receitas' para dimensionar. O método americano AASHTO usa o 'Structural Number' (SN), um índice que combina as espessuras e os materiais. O método do DNIT, mais moderno, é mecanístico-empírico: ele calcula as deformações (`εt` e `εz`) e as compara com os limites permitidos."
*   *Imagens:* Mostrar um ábaco do método AASHTO e a tela de um software de cálculo mecanístico.

**(5) Encerramento (2 min)**
*   *Professor na tela:* "Dimensionar um pavimento flexível é um balanço entre as espessuras e a qualidade dos materiais de cada camada para garantir que ele resista à fadiga e ao afundamento durante sua vida útil."
*   *Professor:* "Na nossa última aula, vamos aprender a gerenciar esses pavimentos, identificando seus 'sintomas' e aplicando os 'remédios' certos. Até lá!"

---

#### TEXTO BASE EXPANDINDO HORIZONTES DA VIDEOAULA 4

## Aula 12 – Desempenho e Gestão de Pavimentos

##### Objetivos da aula
- Compreender indicadores de desempenho: serventia, irregularidade longitudinal (IRI) e sua evolução.
- Reconhecer patologias típicas (trincamento, afundamento, desagregação) e suas causas.
- Definir estratégias de manutenção: preventiva versus corretiva, priorização e timing de intervenção.

##### Conteúdo da aula (texto base)

1) Desempenho funcional: serventia e IRI
- Serventia: qualidade de rolamento percebida pelo usuário; historicamente PSI/PSR, atualmente IRI como métrica padronizada (m/km).
- IRI (International Roughness Index): obtido de perfis longitudinais por perfilômetros inerciais; faixas típicas (m/km) para classificação de conforto e intervenção (menor é melhor).

![Evolução do IRI ao longo do tempo (exemplo)](https://upload.wikimedia.org/wikipedia/commons/8/89/IRI_progression.png)

2) Patologias e causas prováveis
- Trincamento: em malha (alligator/crocodile), longitudinal, transversal, reflexão. Causas: fadiga por tração, retração térmica, reflexão de juntas.
- Afundamento em trilha (rutting): deformação permanente em camadas ou subleito; associado a alta temperatura/solicitação e suporte insuficiente.
- Desagregação (ravelling), exsudação (bleeding), panelas (potholes): perda de finos/ligante, selagem deficiente, infiltração e tráfego pesado.

![Exemplo de deterioração do asfalto (trincas/desagregação)](https://upload.wikimedia.org/wikipedia/commons/7/75/Asphalt_deterioration.jpg)

3) Gestão e manutenção: preventiva vs. corretiva
- Preventiva: intervenções em bom/regular estado (selagem de trincas, microrrevestimento, slurry, rejuvenescimento) para desacelerar deterioração e postergar reabilitações.
- Corretiva: restaurações pontuais (tapa-buraco, remendos profundos), reforço estrutural (overlay) ou reconstrução quando desempenho estrutural/funcional está comprometido.
- Planejamento: definir níveis-alvo de IRI/PCI por classe de via; priorizar por criticidade (tráfego, segurança, custo do ciclo de vida) e sincronizar com drenagem e serviços.

4) Exemplo orientado (esboço)
- A partir de inventário (IRI e mapeamento de defeitos), classificar trechos, selecionar tratamentos (preventivos/corretivos) e estimar ganhos de ciclo de vida sob orçamento limitado.

##### Atividade prática
- Em um trecho hipotético, dado IRI e mapa de defeitos (tipos e severidades), proponha um plano de manutenção em 3 anos com orçamento limitado, justificando a escolha entre preventiva e corretiva por segmento.

##### Links suplementares da Aula 12
- International roughness index (Wikipedia): https://en.wikipedia.org/wiki/International_roughness_index
- Pavement condition index (Wikipedia): https://en.wikipedia.org/wiki/Pavement_condition_index
- Pavement maintenance (Wikipedia): https://en.wikipedia.org/wiki/Road_surface#Maintenance

##### Pontos‑chave
- IRI mede irregularidade longitudinal (serviço/ conforto); limites orientam intervenção.
- Patologias recorrentes indicam causas (fadiga, suporte insuficiente, infiltração) e norteiam o tratamento.
- Manutenção preventiva preserva desempenho e posterga custos maiores; corretiva restaura quando há falha.
- Gestão eficaz integra inventário, priorização por criticidade e sincronização com drenagem/serviços.

---

#### VIDEOAULA 12: Aula 12 – Desempenho e Gestão de Pavimentos

## Roteiro para a Videoaula 12 – Desempenho e Gestão de Pavimentos

**(1) Abertura (1 min)**
*   *Professor na tela:* "Olá! Sou Afonso Cesar Lelis Brandão. Já aprendemos a projetar pavimentos. Mas e depois que eles estão prontos? Como cuidamos deles? Hoje vamos falar sobre gestão de pavimentos: como medir seu desempenho e decidir a hora certa de intervir."

**(2) Medindo o Desempenho: O IRI (3 min)**
*   *Vídeo:* Mostrar um perfilômetro a laser medindo uma rodovia.
*   *Professor:* "A principal forma de medir a 'saúde' de um pavimento é o IRI, o Índice de Irregularidade Internacional. Ele mede o quão 'lisa' ou 'áspera' é a superfície. Quanto menor o IRI, mais confortável é a viagem. Acompanhar a evolução do IRI ao longo do tempo nos diz o quão rápido o pavimento está se degradando."
*   *Gráfico na tela:* Mostrar o gráfico de evolução do IRI, com os limites para intervenção.

**(3) Patologias: Os Sintomas do Pavimento (4 min)**
*   *Professor:* "Um pavimento doente mostra sintomas, as patologias. As mais comuns são as trincas, que podem ser por fadiga, o afundamento na trilha de roda, e a desagregação, quando o asfalto começa a se soltar. Cada defeito nos dá uma pista sobre a causa do problema."
*   *Imagens:* Mostrar fotos de alta qualidade de cada tipo de defeito: trinca couro de jacaré, afundamento de trilha de roda, panela, etc.

**(4) Manutenção: Preventiva vs. Corretiva (3 min)**
*   *Animação:* Mostrar uma curva de deterioração do pavimento. Na parte alta da curva, aparecem ícones de manutenção preventiva (selagem de trinca, microrrevestimento). Na parte baixa, ícones de manutenção corretiva (tapa-buraco, recapeamento).
*   *Professor:* "A regra de ouro da gestão de pavimentos é: agir cedo custa menos. A manutenção preventiva, feita quando o pavimento ainda está bom, é muito mais barata e eficaz do que a manutenção corretiva, que é apagar o incêndio quando o problema já está grave."

**(5) Encerramento (2 min)**
*   *Professor na tela:* "Gerenciar uma rede de pavimentos é como ser um médico de estradas. Precisamos de diagnóstico (IRI, defeitos), prognóstico (modelos de desempenho) e tratamento (manutenção). Um bom sistema de gestão garante estradas mais seguras e economiza muito dinheiro público."
*   *Professor:* "Espero que esta unidade tenha dado a vocês uma base sólida sobre geotecnia e pavimentação. Obrigado e até a próxima!"

---

# AVALIAÇÕES

## Quiz Não Avaliativo (V/F)

1) Em um solo parcialmente saturado, o grau de saturação $S_r$ relaciona $V_w$ e $V_v$.
- Resposta correta: Verdadeiro
- Explicação: $S_r = V_w/V_v$ por definição.

2) O índice de plasticidade é $IP = LL + LP$.
- Resposta correta: Falso
- Explicação: $IP = LL - LP$ (diferença entre liquidez e plasticidade).

## Atividade Verificadora (Dissertativa)

- Questão: Dadas amostras A e B com (LL, LP) e curvas granulométricas, classifique-as (SUCS) e discuta implicações de compactação e permeabilidade. Proponha um plano de ensaios de controle em obra.
- Resposta esperada: Identificar faixas de textura e plasticidade, enquadrar no SUCS (ex.: CL, SM, etc.), relacionar IP e frações finas a comportamento (compressibilidade/permeabilidade) e indicar ensaios de umidade/densidade in situ, Proctor e verificação visual.

---

# MATERIAL COMPLEMENTAR

## Direto da Fonte

- Texto provocativo: Consolidar relações de fase e consolidar conhecimentos de Atterberg antes de dimensionar.
- Livro: Das, B. M. – Fundamentos de Engenharia Geotécnica.
- Capítulos: capítulo de índices físicos e classificação; ensaios de compactação.
- Link: https://biblioteca-a.read.garden/viewer/9786556901633/91
- Acesso: plataforma Brightspace (BV Professor) – usuário: professor.conteudista – senha: unifecaf2023

## Para Mergulhar

- **Livro Clássico:** *Soil Mechanics, SI Version* por T.W. Lambe e R.V. Whitman. Considerado uma das bíblias da geotecnia, este livro aprofunda com rigor todos os conceitos de mecânica dos solos abordados na unidade. Essencial para quem deseja seguir carreira na área.
  - **Link:** [Wiley Editora](https://www.wiley.com/en-us/Soil+Mechanics%2C+SI+Version-p-9780471511922)

- **Curso Online:** *Introduction to Geotechnical Engineering* por Dr. Jean-Louis Briaud (Texas A&M University). Uma série de videoaulas completas e didáticas que cobrem os fundamentos da engenharia geotécnica, ideal para complementar os estudos.
  - **Link:** [Playlist no YouTube](https://www.youtube.com/playlist?list=PL3-i5i1j_flH_bt_2d5d4vj9o9t-s9f-o)

- **Blog de Engenharia:** *Practical Engineering*. O blog de Grady Hillhouse é famoso por explicar conceitos complexos de engenharia de forma visual e intuitiva. A seção de geotecnia é particularmente interessante.
  - **Link:** [Practical Engineering - Geotechnical](https://practical.engineering/blog/tag/geotechnical/)

- **Documentário/Análise de Falha:** *What Really Happened at the Millennium Tower?* por Practical Engineering. Um vídeo que analisa o famoso caso do edifício em São Francisco que está afundando e inclinando. Um estudo de caso fascinante sobre a importância das fundações e da investigação geotécnica.
  - **Link:** [Vídeo no YouTube](https://www.youtube.com/watch?v=G2y8yB5v5y0)

## Podcast

- Texto provocativo: Ouça um caso prático de controle tecnológico em terraplenagem.
- Podcast/Vídeo: GeoEngineer.org (YouTube)
- Episódio: Compaction control in earthworks
- Link: https://www.youtube.com/watch?v=0c038M3-6yQ

## Artigo Científico

- Texto provocativo: Influência de finos plásticos no desempenho de bases.
- Link: https://doi.org/10.1061/(ASCE)GT.0000
- Referência ABNT: [Inserir referência completa conforme ABNT].


---

# Referências

- Soil mechanics (Wikipedia): https://en.wikipedia.org/wiki/Soil_mechanics
- Atterberg limits (Wikipedia): https://en.wikipedia.org/wiki/Atterberg_limits
- Proctor compaction test (Wikipedia): https://en.wikipedia.org/wiki/Proctor_compaction_test
- Concrete pavement (Wikipedia): https://en.wikipedia.org/wiki/Road_surface#Concrete
- Highway engineering – concrete pavements (Wikipedia): https://en.wikipedia.org/wiki/Highway_engineering
- Winkler foundation (Wikipedia): https://en.wikipedia.org/wiki/Winkler_foundation_model
- Harold M. Westergaard (Wikipedia): https://en.wikipedia.org/wiki/Harold_M._Westergaard
- Asphalt concrete (Wikipedia): https://en.wikipedia.org/wiki/Asphalt_concrete
- Mechanistic–empirical pavement design (Wikipedia): https://en.wikipedia.org/wiki/Mechanistic%E2%80%93empirical_pavement_design
- AASHTO pavement design (Wikipedia): https://en.wikipedia.org/wiki/AASHTO
- International roughness index (Wikipedia): https://en.wikipedia.org/wiki/International_roughness_index
- Pavement condition index (Wikipedia): https://en.wikipedia.org/wiki/Pavement_condition_index
- Pavement maintenance (Wikipedia): https://en.wikipedia.org/wiki/Road_surface#Maintenance

Imagens citadas (Commons/Wikipedia):
- Triângulo textural do solo: https://commons.wikimedia.org/wiki/File:SoilTextureTriangle.jpg
- Pavimento de concreto em serviço: https://commons.wikimedia.org/wiki/File:2014-08-29_15_31_39_View_southeast_along_Stuyvesant_Avenue_in_Ewing%2C_New_Jersey%2C_with_concrete_pavement_likely_dating_to_the_1950s.JPG
- Execução de pavimento asfáltico: https://commons.wikimedia.org/wiki/File:AF-asphalt-laying-machine.jpg
- Evolução do IRI ao longo do tempo: https://commons.wikimedia.org/wiki/File:IRI_progression.png
- Deterioração do asfalto: https://commons.wikimedia.org/wiki/File:Asphalt_deterioration.jpg
