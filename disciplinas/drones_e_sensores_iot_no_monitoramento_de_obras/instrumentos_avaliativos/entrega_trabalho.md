# Entrega de Trabalho (PBL) — Drones e Sensores IoT no Monitoramento de Obras

> Roteiro para elaboração com **Problem-Based Learning**.

- **Disciplina:** Drones e Sensores IoT no Monitoramento de Obras
- **Professor-conteudista:** Afonso Cesar Lelis Brandão

> O **CASE** existe para que o estudante entenda a aplicabilidade do conteúdo estudado na realidade do mercado de trabalho.

---

## Título

**Corredor Leste de Vale Verde — Plano Integrado de Monitoramento por Drones e Sensores IoT de uma Trincheira e um Viaduto Urbanos ao Lado de uma Estação Ferroviária Tombada e de uma APP**

---

## Desafio

> **O quê?** A prefeitura de uma cidade média precisa de um **plano integrado de monitoramento** para uma obra viária linear em área urbana consolidada. São duas estruturas principais: uma **trincheira** (passagem inferior) escavada junto a edificações sensíveis e um **viaduto** que atravessa um córrego com mata ciliar. O plano deve juntar **drones** (mapeamento, volumes, LiDAR e termografia), **sensores IoT** (geotécnicos, estruturais e de vibração), **BIM 4D**, **inteligência artificial** e **gestão** (custo, LGPD, segurança da informação, contrato e regulamentação).
>
> **Quem?** A **Secretaria Municipal de Obras de Vale Verde** (município fictício, com cerca de 420 mil habitantes) é a contratante e a **controladora** dos dados. A obra está sendo licitada, e você trabalha na **gerenciadora** que vai redigir o **plano de monitoramento**, anexo obrigatório do edital. Pela Lei nº 14.133/2021 (art. 19, § 3º), a prefeitura decidiu exigir **BIM**, com modelo 4D da execução e atualização *as-built*.
>
> **Quando?** Prazo de obra de **26 meses**, com início previsto para **março de 2027**. O plano precisa estar pronto antes da licitação, porque o monitoramento vai entrar no orçamento e no contrato.
>
> **Onde?** No **Corredor Leste**, uma faixa de obra de **1.500 m × 160 m** (24 ha) ao longo de uma avenida com tráfego e pedestres. Ela tem três trechos:
>
> - **Trecho A — Trincheira (380 m).** Escavação com profundidade máxima de **8,5 m** e largura de **28 m**. A contenção é uma **cortina de estacas secantes atirantada**, e o lençol freático está a **3,0 m** de profundidade, com rebaixamento por poços. A **12 m** da cortina fica a **antiga Estação Ferroviária de Vale Verde (1912)**, desativada e hoje Centro Cultural: **tombada pelo patrimônio municipal**, em alvenaria de tijolos sobre **fundação rasa**, com trincas antigas e uma torre do relógio. Do outro lado, a **9 m** da cortina, há um **edifício residencial de 10 pavimentos (cerca de 32 m de altura)**. O volume total de corte previsto é de **64.000 m³** (*in situ*). Ao lado do acesso da trincheira, um aterro será compactado com **rolo vibratório**.
> - **Trecho B — Viaduto (240 m, 6 vãos)** sobre o **Córrego das Pedras**, que tem menos de 10 m de largura. A **Área de Preservação Permanente (APP)** é de 30 m em cada margem (Lei nº 12.651/2012, art. 4º, I, a) e está coberta por **mata ciliar densa**. O projeto hidráulico e a locação dos pilares P3 e P4 exigem o **terreno natural sob a mata** numa faixa de **2,6 ha**. O tabuleiro será moldado no local e protendido.
> - **Trecho C — Ligações e pavimentação (880 m)**, com obras de baixo risco.
>
> **Por quê?** A prefeitura já viveu duas disputas judiciais recentes por **danos a imóveis vizinhos** e por **medições de terraplenagem contestadas**. O Conselho Municipal do Patrimônio só autorizou a obra com **monitoramento contínuo da Estação**. O órgão ambiental exige que a intervenção na APP seja **a mínima necessária** (art. 8º do Código Florestal: utilidade pública, que inclui sistema viário, art. 3º, VIII, b). **Dados disponíveis (valores ilustrativos para o case):**
>
> - **Drone de mapeamento:** multirrotor de 6,3 kg com **RTK** e câmera RGB de $5.472 \times 3.648$ pixels, $p = 2{,}41\,\mathrm{\mu m}$, $f = 8{,}8\,\mathrm{mm}$ (sensor de $13{,}2 \times 8{,}8\,\mathrm{mm}$). Voa a $6\,\mathrm{m/s}$, com **20 min úteis** por bateria e exposição de 1/1.000 s. O edital exige **GSD ≤ 2,5 cm em toda a área, inclusive no fundo da trincheira**, sobreposições de **80% (frontal) e 70% (lateral)**, $RMSE_z \le 4\,\mathrm{cm}$ nos checkpoints e **levantamento mensal**. Por segurança operacional e linha de visada, a gerenciadora quer dividir o corredor em **2 blocos de 750 m**, com decolagem no centro de cada bloco.
> - **Controle do levantamento do mês 6:** resíduos verticais (modelo − campo) em 8 checkpoints independentes, em cm: $+2{,}1$; $-1{,}4$; $+3{,}0$; $+0{,}8$; $-2{,}2$; $+1{,}7$; $+2{,}6$; $-0{,}9$.
> - **Volumes do mês 6 (MDT anterior − MDT atual, na área da trincheira, $380 \times 28\,\mathrm{m}$):** $9.850\,\mathrm{m^3}$ escavados, contra $11.200\,\mathrm{m^3}$ previstos no 4D para o mês. O acumulado até o mês 5 era de $31.400\,\mathrm{m^3}$. Empolamento de 30% e caminhões de $14\,\mathrm{m^3}$.
> - **LiDAR disponível para a APP:** $PRR = 240\,\mathrm{kHz}$, campo de visão de $70°$, voo a $H = 60\,\mathrm{m}$ e $v = 6\,\mathrm{m/s}$, com erro de atitude da IMU de $0{,}05°$. O projeto pede **ao menos 10 pontos/m² no solo**, e estima-se que **10%** dos pulsos atravessem a mata até o chão.
> - **Câmera térmica para a fachada da Estação:** $640 \times 512$ pixels, pixel de $12\,\mathrm{\mu m}$, $f = 13\,\mathrm{mm}$. O objetivo é detectar descolamentos de reboco a partir de **5 cm**, considerando que um defeito precisa ocupar $3 \times 3$ pixels.
> - **Leituras da semana crítica (mês 6), já com os níveis do plano preliminar:**
>   - **Inclinômetro in-place I-2** (atrás da cortina, frente da Estação, $L = 0{,}5\,\mathrm{m}$): variações de $\sin\theta$, do topo para baixo, de $5{,}0$; $4{,}4$; $3{,}6$; $2{,}4$; $1{,}2$ e $0{,}4 \times 10^{-3}$, sem variação abaixo. Há 7 dias, o topo estava em $6{,}4\,\mathrm{mm}$. Níveis: atenção em 10 mm e alerta em 15 mm.
>   - **Marco de recalque M-3** (pilar da Estação), leituras diárias de $6{,}1$; $6{,}4$; $6{,}6$; $7{,}0$ e $7{,}5\,\mathrm{mm}$. As incertezas-padrão independentes são $0{,}3\,\mathrm{mm}$ (instrumento), $0{,}4\,\mathrm{mm}$ (referência de nível) e $0{,}2\,\mathrm{mm}$ (efeito térmico). O **M-4**, a $5{,}0\,\mathrm{m}$ do M-3, recalcou $2{,}5\,\mathrm{mm}$. Níveis da Estação: recalque com atenção em 8 mm e alerta em 12 mm; velocidade de atenção de 0,3 mm/dia; distorção angular com atenção em 1/1.000 e alerta em 1/750.
>   - **Piezômetro de corda vibrante PZ-2:** depois de uma chuva às 23h, o nível d'água está a $1{,}6\,\mathrm{m}$ abaixo do fundo da escavação e sobe $0{,}15\,\mathrm{m/h}$. Níveis: atenção a 2,0 m e alerta a 1,0 m abaixo do fundo.
>   - **Sismógrafo na fundação da Estação**, durante a compactação vibratória: PPV de $2{,}4\,\mathrm{mm/s}$ a $18\,\mathrm{Hz}$. Níveis do plano: atenção em 2,0 mm/s e alerta em 3,0 mm/s.
> - **Nó sensor IoT típico:** bateria de $19.000\,\mathrm{mAh}$ (80% utilizável). Em cada ciclo, lê por 2 s a 25 mA, transmite por 1 s a 120 mA e dorme a 0,02 mA. O ciclo é de 15 min em rotina e de 5 min em atenção.
> - **Tabuleiro do viaduto:** a protensão exige $f_c \ge 25\,\mathrm{MPa}$. A calibração da mistura (ilustrativa) é $f_c = 9{,}2\,\ln M - 41$ (MPa, $M$ em °C·h, $T_0 = 0\,^\circ\mathrm{C}$). Os sensores de maturidade registraram médias de 30, 34, 29 e 25 °C em quatro blocos consecutivos de 12 h.
> - **Scan-vs-BIM do pilar P4 do viaduto:** $\Delta x = 14\,\mathrm{mm}$, $\Delta y = -7\,\mathrm{mm}$, incerteza expandida $U = 5\,\mathrm{mm}$ e tolerância contratual de $15\,\mathrm{mm}$.
> - **IA de triagem de fissuras nas fotos da Estação:** num teste com 1.500 fotos, 90 delas com fissura, o limiar 0,5 deu $VP = 70$, $FP = 14$ e $FN = 20$; o limiar 0,3 deu $VP = 86$, $FP = 62$ e $FN = 4$. As trincas que interessam na alvenaria têm **1 mm** de abertura, e a câmera RGB do drone de inspeção ($S_w = 13{,}2\,\mathrm{mm}$, $f = 8{,}8\,\mathrm{mm}$, $W = 5.472\,\mathrm{px}$) operaria a **15 m** da fachada.
> - **Custos e riscos:** obra de **R\$ 148 milhões**. Monitoramento com CAPEX de **R\$ 640.000** e OPEX de **R\$ 38.000/mês**. Cada levantamento topográfico convencional custa **R\$ 15.000**; cada voo de drone, **R\$ 6.500**. Riscos estimados (sem → com monitoramento):
>   - dano à Estação tombada: 6% de R\$ 12 milhões → 1,5% de R\$ 4 milhões;
>   - instabilidade e paralisação da trincheira: 4% de R\$ 20 milhões → 1% de R\$ 6 milhões;
>   - dano ao edifício residencial: 5% de R\$ 6 milhões → 1,5% de R\$ 2 milhões.
>
>   O edital pede **disponibilidade da plataforma de 99,95%**.
> - **Pessoas e dados:** a avenida tem pedestres e veículos (placas). O edifício tem janelas voltadas para a obra. Haverá **câmeras fixas** para avanço físico e segurança e **etiquetas UWB** nos capacetes, para criar cercas virtuais em torno das escavadeiras dentro da trincheira.
>
> **Sua missão como engenheiro(a) da gerenciadora:** elaborar um **plano integrado de monitoramento completo e defensável** para o Corredor Leste. O plano deve integrar as 4 unidades da disciplina:
>
> - **Unidade 1:** fundamentos, malha fechada, incerteza, IoT e regulamentação de drones;
> - **Unidade 2:** plano de voo, fotogrametria, volumes, LiDAR e termografia;
> - **Unidade 3:** sensores geotécnicos, estruturais e de vibração, níveis de alerta e dashboard;
> - **Unidade 4:** BIM 4D, IA e gestão.
>
> **Todos os números** do plano devem ser **calculados e demonstrados passo a passo**.

---

## Fonte de pesquisa

O ESTUDANTE deverá pesquisar um exemplo de como outros profissionais ou empresas já resolveram esse desafio.

**Fontes de pesquisa primária:**

Pesquise como o setor planeja, executa e contrata o monitoramento de obras urbanas com drones e sensores:

1. **Material da disciplina** — as 16 aulas, com ênfase nas Aulas 3 e 4 (IoT, malha fechada e regulamentação), 5 a 8 (voo, fotogrametria, volumes, LiDAR e termografia), 9 a 12 (instrumentação e alertas) e 13 a 16 (BIM, IA, gestão e projeto integrado).
2. **ANAC — RBAC nº 100, Emenda 00 (texto integral)** — https://pergamum.anac.gov.br/pergamum/vinculos/RBAC100EMD00.pdf — e o portal de drones da ANAC: https://www.gov.br/anac/pt-br/assuntos/drones (categorias aberta, específica e certificada; SISANT; exame teórico; seguro).
3. **DECEA — ICA 100-40 (2026), *Aeronaves Não Tripuladas e o Acesso ao Espaço Aéreo Brasileiro*** — https://www.gov.br/defesa/pt-br/assuntos/aerolevantamento/arquivos/2026/ica-100-40-publicada-port-2094-dnor8-18-03-2026-bca-058-30-03-2026.pdf (SARPAS e antecedências).
4. **Ministério da Defesa — Aerolevantamento** — https://www.gov.br/defesa/pt-br/assuntos/aerolevantamento (legislação, entidades inscritas e SisCLATEN; Decreto nº 2.278/1997 e Portaria GM-MD nº 3.703/2021).
5. **Lei nº 12.651/2012 (Código Florestal)** — https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2012/lei/l12651.htm (APP de cursos d'água, art. 4º; intervenção por utilidade pública, arts. 3º e 8º).
6. **Lei nº 13.709/2018 (LGPD)** — https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm — e **Lei nº 14.133/2021 (licitações, BIM no art. 19, § 3º)** — https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/l14133.htm.
7. **Normas técnicas** — ABNT NBR 6122 (fundações e monitoramento de recalques), NBR 9653 (vibrações por desmonte, referência de PPV × frequência), NBR 16747 (inspeção predial) e NBR 10151:2019 (ruído em áreas habitadas).
8. **Exatidão de levantamentos** — *The ASPRS Positional Accuracy Standards, Edition 2* (resumo): https://lidarmag.com/2023/10/06/the-asprs-positional-accuracy-standards-edition-2/.
9. **Artigos científicos** — PECK, R. B. (1969), método observacional: https://doi.org/10.1680/geot.1969.19.2.171 · SIEBERT, S.; TEIZER, J. (2014), drones em terraplenagem: https://doi.org/10.1016/j.autcon.2014.01.004 · SACKS, R. *et al.* (2020), gêmeo digital na construção: https://doi.org/10.1017/dce.2020.16 · SPENCER JR., B. F. *et al.* (2019), visão computacional em infraestrutura: https://doi.org/10.1016/j.eng.2018.11.030.

**Aulas relacionadas:** todas as 16 servem de insumo. Em ordem de relevância:

- Aula 16 (projeto integrado);
- Aulas 5 a 7 (plano de voo, exatidão e volumes);
- Aulas 9 e 12 (instrumentação geotécnica e TARP);
- Aula 4 (regulamentação);
- Aula 3 (arquitetura IoT e bateria);
- Aula 8 (LiDAR e termografia);
- Aulas 10 e 11 (estrutura e vibração);
- Aulas 13 a 15 (BIM, IA e gestão);
- Aulas 1 e 2 (malha fechada e incerteza).

---

## 5. Entregável e distribuição da pontuação

Sua entrega final da disciplina **Drones e Sensores IoT no Monitoramento de Obras** tem **3 entregáveis obrigatórios**. O objetivo é elaborar o **plano integrado de monitoramento do Corredor Leste**. Nele, você deve mostrar que sabe:

- partir dos **riscos** da obra;
- escolher **o que medir, com quê, onde e com que frequência**;
- definir **limites e respostas** (malha fechada);
- integrar drone, sensores, BIM e IA numa **sombra digital** da obra;
- defender o plano **técnica, econômica, jurídica e regulatoriamente**.

Os números devem ser **calculados e demonstrados passo a passo**, e não estimados "no olho".

### 1. Parte Teórica — (25% da nota)

Desenvolva um **relatório técnico em PDF** contendo:

- **Diagnóstico de riscos** da obra: Estação tombada, edifício vizinho, contenção e rebaixamento, APP, medição de volumes, segurança de pessoas e disputas contratuais. Para cada risco, indique a **grandeza** a medir e a **consequência** de não medir a tempo.
- **Fundamentação** das escolhas, com os conceitos das 4 unidades:
  - malha aberta × fechada; modelo, sombra e gêmeo digital;
  - incerteza (GUM) e o critério de Nyquist;
  - fotogrametria × LiDAR;
  - método observacional e TARP;
  - BIM 4D e openBIM;
  - métricas de IA;
  - valor esperado da perda evitada.
- **Enquadramento regulatório e legal:**
  - RBAC nº 100 (categoria da operação em cada trecho);
  - SISANT, exame teórico e seguro;
  - SARPAS (ICA 100-40);
  - aerolevantamento (Ministério da Defesa);
  - homologação da Anatel;
  - Código Florestal (APP);
  - LGPD (base legal da administração pública);
  - Lei nº 14.133/2021 (BIM).

**Critérios de avaliação da Parte Teórica (25 pontos):**

| Critério | Pontos |
| --- | --- |
| Riscos identificados e convertidos em grandezas mensuráveis, com consequência explícita | 7 |
| Fundamentação correta dos conceitos das 4 unidades (sem confundir precisão × exatidão, MDS × MDT, norma de referência × limite de projeto) | 8 |
| Enquadramento regulatório correto e coerente com o RBAC nº 100, a ICA 100-40 e o aerolevantamento | 6 |
| Uso das fontes (citadas em ABNT) e clareza do texto | 4 |

### 2. Parte Prática — (50% da nota)

Desenvolva o **plano integrado de monitoramento** com, no mínimo:

- **(a) Plano de voo e controle (Unidade 2).**
  - Calcule a altura máxima que garante o GSD exigido no fundo da trincheira e adote uma altura de voo.
  - Calcule o GSD na via e no fundo, o *footprint*, a base, o espaçamento entre faixas, o intervalo entre fotos, o número de faixas e de fotos por bloco, o tempo de voo, o **número de voos** e o arrasto.
  - Comente o efeito do edifício de 32 m sobre a sobreposição.
  - Proponha a distribuição de GCPs e checkpoints e avalie os resíduos do mês 6 (média, $RMSE_z$, conformidade, viés).
- **(b) Volumes e avanço (Unidades 2 e 4).**
  - Calcule o efeito do viés sobre o volume do mês.
  - Calcule o índice de avanço contra o 4D, o volume solto, o número de viagens e o percentual acumulado da trincheira.
- **(c) LiDAR e termografia (Unidade 2).**
  - Justifique (ou descarte) o LiDAR na APP e calcule a densidade total e no solo e o erro de atitude na borda da faixa.
  - Calcule a distância máxima da câmera térmica à fachada da Estação e o menor defeito detectável, e diga em que horário e em que condições você voaria.
- **(d) Plano de instrumentação IoT (Unidade 3).**
  - Monte uma tabela com grandeza, instrumento, local, quantidade, leitura zero, frequência normal → em atenção e níveis de **atenção e alerta**. Cubra a trincheira, a Estação, o edifício e o viaduto.
  - Inclua o geotécnico (inclinômetros, piezômetros, marcos e prismas), o estrutural (células de carga, fissurômetros, clinômetro na torre e maturidade no tabuleiro) e a vibração.
  - Processe as **leituras da semana crítica**: deslocamento acumulado e velocidade do I-2; incerteza combinada e expandida do M-3, velocidade, distorção angular e prazos até os níveis; tempo até o alerta do PZ-2; PPV × NBR 9653 × limite do plano. Classifique cada leitura em verde, amarelo ou vermelho.
  - Calcule a **maturidade** e o horário mínimo da protensão.
- **(e) Arquitetura IoT, malha fechada e dashboard (Unidades 1 e 3).**
  - Descreva as quatro camadas, a rede escolhida (com justificativa), a borda × nuvem, o MQTT com TLS e a **autonomia** do nó em rotina e em atenção, comparada ao prazo da obra.
  - Monte o **TARP** com gatilho, ação, responsável e prazo.
  - Indique o que é **automático** e o que exige **decisão humana**.
  - Esboce o **dashboard**.
- **(f) BIM 4D, gêmeo digital e IA (Unidade 4).**
  - Classifique o pilar P4 (conforme, não conforme ou inconclusivo) e redija a pendência BCF.
  - Ligue os instrumentos aos GUIDs e classifique o sistema (modelo, sombra ou gêmeo).
  - Calcule $P$, $R$ e $F_1$ dos dois limiares e escolha um.
  - Verifique se a câmera mede a trinca de 1 mm.
- **(g) Gestão (Unidade 4).**
  - Calcule o custo total, a perda evitada, os ganhos diretos, o ROI, a razão benefício/custo, uma **análise de sensibilidade** e o custo relativo à obra.
  - Calcule o tempo máximo fora do ar do SLA.
  - Inclua o inventário de dados pessoais com base legal e minimização, os controles de segurança da informação e as **cláusulas contratuais**: TARP, SLA, propriedade dos dados em formato aberto e ART.

**Memorial de cálculo (anexo obrigatório).** Cada cálculo deve trazer **fórmula, substituição dos dados do case e resultado com unidade**, passo a passo. **Rastreabilidade:** os resultados devem ser **citados e discutidos** no corpo do plano. Não basta anexar a conta solta.

**Critérios de avaliação da Parte Prática (50 pontos):**

| Critério | Pontos |
| --- | --- |
| (a) Plano de voo e controle: cálculos corretos, nº de voos, relevo/edifício, GCP/checkpoints e leitura do RMSE e da média | 8 |
| (b) Volumes e avanço: viés → volume, índice 4D, logística | 5 |
| (c) LiDAR e termografia: justificativa, densidades, distância e condições de voo | 5 |
| (d) Instrumentação: tabela completa e coerente com os riscos, cálculos das leituras, classificação por cores, maturidade | 12 |
| (e) Arquitetura, autonomia, TARP, automático × humano, dashboard | 8 |
| (f) BIM, gêmeo e IA: classificação com incerteza, BCF, métricas e escolha do limiar, limite físico do GSD | 6 |
| (g) Gestão: custo-benefício com sensibilidade, SLA, LGPD, segurança e contrato | 6 |

### 3. Vídeo Pitch — (25% da nota)

Grave um **vídeo de até 4 minutos**, simulando a apresentação do plano à **comissão da prefeitura**, com representantes de Obras, do Conselho do Patrimônio, do órgão ambiental e da Procuradoria. O vídeo deve apresentar:

- O problema: obra linear urbana junto a uma Estação tombada, a um edifício de 10 pavimentos e a uma APP, com histórico de disputas por danos e medições.
- A lógica do plano: **riscos → grandezas → instrumentos → limites → respostas**.
- Os **números-chave**: altura de voo e GSD, nº de voos, $RMSE_z$, densidade do LiDAR no solo, autonomia dos nós e as leituras da semana crítica com a decisão tomada.
- A malha fechada em funcionamento (o caso do PZ-2 às 23h ou o da Estação).
- O custo-benefício, com a sensibilidade, e o que não se monetiza (patrimônio).
- As garantias legais: categoria no RBAC nº 100, aerolevantamento, LGPD e contrato.

Publique o vídeo no **YouTube (modo não listado)** ou em outra plataforma de hospedagem e insira o **link ao final do PDF**. Antes de enviar, confira se o link está acessível.

**Critérios de avaliação do Vídeo Pitch (25 pontos):**

| Critério | Pontos |
| --- | --- |
| Clareza da mensagem central e do problema nos primeiros 30 s | 5 |
| Números-chave corretos e bem explicados (sem ler tabelas inteiras) | 8 |
| Demonstração da malha fechada e da decisão tomada | 6 |
| Defesa econômica, legal e regulatória; tempo respeitado (≤ 4 min) e qualidade de áudio/imagem | 6 |

**Critérios qualitativos transversais:**

- **coerência interna** (risco → instrumento → limite → ação → responsável);
- **realismo** (frequências, limites, custos e prazos);
- **rastreabilidade** dos cálculos;
- **integração** das 4 unidades, em vez de capítulos isolados;
- **honestidade técnica**: reconhecer incertezas, limites físicos (GSD, penetração do LiDAR) e o que a tecnologia não resolve.

---

## 6. Solução (esse item será removido antes do case ser disponibilizado ao aluno)

> **Remover antes de entregar ao aluno.**
>
> **Atenção:** este tópico será removido antes do case ser disponibilizado ao aluno — é apenas para o professor tutor que corrigirá.

**Diagnóstico de riscos esperado.** O aluno deve priorizar pela combinação **consequência × velocidade de evolução** (Aula 16):

| Risco | Grandeza | Por que importa |
| --- | --- | --- |
| Recalque e fissuração da Estação tombada (fundação rasa, alvenaria, a 12 m) | recalque (mm), distorção angular, abertura de fissura (mm), inclinação da torre, PPV (mm/s) | dano irreversível a patrimônio, embargo, disputa judicial |
| Deslocamento da cortina e ruptura de fundo | deslocamento horizontal (mm), carga em tirantes (kN) | instabilidade da escavação e paralisação |
| Subida do NA após chuva | nível piezométrico (m) | evolução em horas, à noite |
| Recalque do edifício de 10 pavimentos | recalque, distorção angular | dano a terceiros |
| Protensão prematura do tabuleiro do viaduto | maturidade (°C·h) | fissuração, perda de protensão |
| Medição de volumes contestada | volume (m³), com exatidão provada | disputa contratual, já vivida pela prefeitura |
| Terreno sob mata na APP | MDT sob vegetação | erro de locação dos pilares P3/P4, intervenção excessiva na APP |
| Atropelamento na trincheira | proximidade máquina-pessoa | vida |
| Privacidade e integridade dos dados | — | LGPD; leitura adulterada esconde recalque |

Nem tudo pede sensor. O volume fica com o drone, a fissura existente com a vistoria cautelar e o fissurômetro, e a referência com a topografia.

**Regulamentação esperada (coerente com a Unidade 1).**

- **Categoria da operação no RBAC nº 100.** O drone de 6,3 kg, em VLOS, a 80 m de altura (abaixo dos 120 m), cumpre os critérios de peso, altura e linha de visada da **categoria aberta**. Porém, o corredor fica ao longo de uma **avenida com pedestres e veículos**, e a categoria aberta exige que **em nenhuma hipótese** se voe a menos de **30 m horizontais de pessoas não envolvidas e não anuentes**, salvo barreira mecânica capaz de protegê-las. Por isso, a resposta esperada é uma destas:
  - (i) os blocos sobre a via em uso ficam na **categoria específica**, com avaliação de risco operacional por método aceito pela ANAC (como o **SORA**) ou por cenário padrão e, conforme a complexidade, o **COE**;
  - (ii) os voos são feitos em janelas com **interdição da faixa** (domingo cedo, por exemplo), mantendo os 30 m. Nesse caso, a avaliação de risco operacional atualizada continua exigida, porque não há 150 m de afastamento.
- **Termografia da Estação.** O voo é feito junto a uma edificação. Exige o Centro Cultural fechado e área isolada, com a equipe local **anuente**, ou então a categoria específica.
- **LiDAR na APP.** Sem terceiros, pode caber na categoria aberta.
- **Requisitos para todas as operações:**
  - aeronaves **cadastradas no SISANT**;
  - piloto aprovado no **exame teórico da ANAC** (exigível a partir de 2027, ou seja, durante toda a obra);
  - **seguro** com cobertura de danos a terceiros;
  - acesso ao espaço aéreo pelo **SARPAS** (ICA 100-40);
  - equipamentos e rádios (drone, nós e gateways LoRaWAN) **homologados pela Anatel**.
- **Aerolevantamento.** O voo mensal em faixas sobrepostas para ortomosaico e MDT é **aerolevantamento** (Portaria GM-MD nº 3.703/2021, art. 8º). Ele só pode ser executado por entidade **inscrita no Ministério da Defesa**, com pedido no SARPAS feito com **4 dias corridos** de antecedência. A área de cerca de 0,24 km², contida num círculo de raio de 2,2 km, tende à **pré-autorização** (art. 38), **desde que atendidas as condições cumulativas**. A pré-autorização não dispensa a inscrição. O LiDAR em faixas também é aerolevantamento. A foto de inspeção da fachada, sem faixas sobrepostas, não é.
- **APP.** A intervenção para sistema viário é de **utilidade pública** (Lei nº 12.651/2012, art. 3º, VIII, b), admitida pelo art. 8º, com autorização do órgão ambiental. O LiDAR permite locar P3/P4 e o acesso de obra **sem desmatar para medir**.

**(a) Plano de voo e controle — cálculos esperados.** A exigência de GSD vale **no fundo da trincheira**, 8,5 m abaixo da via, e a altura acima do terreno é que manda (Aula 5):

$
H_{máx,fundo} = \frac{GSD \cdot f}{p} = \frac{0{,}025 \times 8{,}8}{0{,}00241} \approx 91{,}3\,\mathrm{m}
\qquad
H_{máx,via} = 91{,}3 - 8{,}5 \approx 82{,}8\,\mathrm{m}
$

Adotando $H = 80\,\mathrm{m}$ acima da via:

$
GSD_{via} = \frac{80 \times 0{,}00241}{8{,}8} \approx 2{,}19\,\mathrm{cm}
\qquad
GSD_{fundo} = \frac{88{,}5 \times 0{,}00241}{8{,}8} \approx 2{,}42\,\mathrm{cm} \le 2{,}5\,\mathrm{cm}
$

$
W \approx 5.472 \times 0{,}0219 \approx 119{,}9\,\mathrm{m}
\qquad
L \approx 3.648 \times 0{,}0219 \approx 79{,}9\,\mathrm{m}
$

$
B = 79{,}9 \times (1 - 0{,}8) \approx 16{,}0\,\mathrm{m}
\qquad
d = 119{,}9 \times (1 - 0{,}7) \approx 36{,}0\,\mathrm{m}
\qquad
\Delta t = \frac{16{,}0}{6} \approx 2{,}7\,\mathrm{s}
$

Por bloco de $750 \times 160\,\mathrm{m}$, com faixas ao longo dos 750 m:

- faixas: $\lceil 160/36{,}0 \rceil + 1 = 6$;
- fotos por faixa: $\lceil 750/16{,}0 \rceil + 1 = 48$;
- fotos por bloco: $6 \times 48 = 288$, ou cerca de **576 fotos** no corredor.

$
s = 6 \times 750 + 5 \times 36{,}0 \approx 4.680\,\mathrm{m}
\qquad
t = \frac{4.680}{6} \approx 780\,\mathrm{s} \approx 13{,}0\,\mathrm{min} < 20\,\mathrm{min}
$

Resultado: **1 bateria por bloco, 2 voos por campanha**. Num voo único de 1.500 m, o tempo seria de cerca de 25,5 min, mais de uma bateria, e o drone se afastaria demais do piloto para manter VLOS. A divisão em blocos resolve as duas coisas.

O arrasto é $6 \times 0{,}001 = 6\,\mathrm{mm} \approx 0{,}27$ pixel, aceitável (menos de meio pixel).

**Edifício de 32 m:** sobre a cobertura, $H = 48\,\mathrm{m}$, $W \approx 71{,}9\,\mathrm{m}$, e a sobreposição lateral cai para $1 - 36{,}0/71{,}9 \approx 50\%$. Haverá buracos ou ruído na cobertura e nas fachadas. Isso não afeta o terreno, mas o edifício não deve ser medido por esse voo: para ele, usar fotos oblíquas, faixas planejadas pela cota mais alta ou levantamento próprio.

**GCPs e checkpoints.** Espera-se de **6 a 10 GCPs** ao longo do corredor (extremidades, meio dos blocos, borda e fundo da trincheira, para controlar o efeito de domo num bloco longo e estreito) e **checkpoints independentes**, medidos com GNSS RTK ou estação total. Resíduos do mês 6:

$
\bar{\Delta z} = \frac{2{,}1 - 1{,}4 + 3{,}0 + 0{,}8 - 2{,}2 + 1{,}7 + 2{,}6 - 0{,}9}{8} \approx 0{,}71\,\mathrm{cm}
$

$
RMSE_z = \sqrt{\frac{31{,}31}{8}} \approx 1{,}98\,\mathrm{cm} \approx 0{,}9\,GSD_{via}
$

Resultado: $1{,}98 \le 4\,\mathrm{cm}$, **atende**. Os sinais se alternam, a média é pequena e a dispersão em torno da média é de cerca de $1{,}85\,\mathrm{cm}$: **não há viés relevante**. Ressalva esperada: 8 checkpoints bastam para o controle de rotina, mas o padrão ASPRS 2023 pede 30 para declarar conformidade plena.

**(b) Volumes e avanço.** Efeito do viés na área da trincheira ($A = 380 \times 28 = 10.640\,\mathrm{m^2}$):

$
\delta V \approx A \cdot \delta z = 10.640 \times 0{,}0071 \approx 76\,\mathrm{m^3}
\quad (\approx 0{,}8\%\ \text{de}\ 9.850\,\mathrm{m^3})
$

Esse valor é desprezível frente à tolerância contratual e não justifica correção. Boa resposta lembra que, se os dois MDTs tiverem vieses independentes, a incerteza da diferença cresce por $\sqrt{2}$ (Aula 7).

$
I = \frac{9.850}{11.200} \approx 0{,}88
\qquad
V_{solto} = 9.850 \times 1{,}30 = 12.805\,\mathrm{m^3}
\qquad
n = \left\lceil \frac{12.805}{14} \right\rceil = 915\ \text{viagens}
$

O acumulado é $31.400 + 9.850 = 41.250\,\mathrm{m^3}$, ou $41.250/64.000 \approx 64{,}5\%$ do corte. O avanço do mês ficou em 88% do 4D. A causa deve ser investigada no 4D: chuva, rebaixamento ou restrição de vibração perto da Estação. A medição de pagamento deve sair do **MDT**, não do MDS, com método contratado: primitivo comum, checkpoints, $RMSE_z$ e média informados, tolerância e arbitragem.

**(c) LiDAR e termografia.** Sob mata ciliar densa, a câmera só gera o **MDS**. O **LiDAR** se justifica **apenas na faixa de 2,6 ha da APP**: no resto do corredor, com solo exposto, a fotogrametria é suficiente e mais barata.

$
W = 2 \times 60 \times \tan 35° \approx 84{,}0\,\mathrm{m}
\qquad
\rho \approx \frac{240.000}{6 \times 84{,}0} \approx 476\,\mathrm{pontos/m^2}
\qquad
\rho_{solo} \approx 0{,}10 \times 476 \approx 48\,\mathrm{pontos/m^2} \ge 10
$

Na borda da faixa, a distância inclinada é $R = 60/\cos 35° \approx 73{,}2\,\mathrm{m}$, e o erro de atitude produz $73{,}2 \times 8{,}73 \times 10^{-4} \approx 0{,}064\,\mathrm{m}$, ou **6,4 cm só pela IMU**. Isso pede sobreposição entre faixas, trajetória GNSS RTK/PPK de qualidade e **checkpoints em clareiras e nas margens abertas**, com RMSE.

**Termografia:**

$
IFOV = \frac{12 \times 10^{-6}}{13 \times 10^{-3}} \approx 0{,}923\,\mathrm{mrad}
\qquad
D_{máx} = \frac{0{,}05/3}{0{,}000923} \approx 18{,}1\,\mathrm{m}
$

Voando a **15 m**, o pixel cobre $15 \times 0{,}923 \approx 13{,}8\,\mathrm{mm}$, e o menor defeito confiável é de cerca de **4,2 cm**. Condições de voo esperadas:

- horário escolhido pela **orientação de cada fachada** (aquecimento sob sol ou resfriamento ao entardecer);
- sem chuva recente e sem vento forte;
- emissividade ajustada.

A termografia faz parte da **vistoria cautelar** antes da obra e da inspeção nos termos da NBR 16747. Ela só **localiza** suspeitas: a confirmação é por percussão nos pontos marcados. O voo exige isolamento e anuência, ou categoria específica, e **máscara de privacidade** no edifício vizinho.

**(d) Plano de instrumentação esperado (mínimo aceitável):**

| Grandeza | Instrumento | Local / quantidade | Frequência normal → atenção | Atenção / alerta |
| --- | --- | --- | --- | --- |
| Deslocamento horizontal | inclinômetros in-place (cadeias MEMS) + prismas no topo (estação total robótica) | 6 a 8 verticais atrás da cortina, concentradas nas frentes da Estação e do edifício; pé abaixo da zona de influência | 1 h → 15 min (inclinômetro); 2 h → 30 min (prismas) | 10 / 15 mm, e velocidade |
| Nível piezométrico | piezômetros de corda vibrante | 4 a 6 atrás da cortina e entre poços | 15 → 5 min | NA a 2,0 / 1,0 m abaixo do fundo |
| Carga em tirantes | células de carga | ~10% dos tirantes, por linha | 1 h → 15 min | ±10% / ±20% da carga de trabalho (projeto) |
| Recalque — Estação | marcos de recalque automatizados (prismas/células hidrostáticas) + nivelamento de conferência a partir de **RN profunda** | 8 a 10 pilares/cantos | 1 h → 15 min | 8 / 12 mm; 0,3 mm/dia; β 1/1.000 / 1/750 |
| Inclinação da torre do relógio | clinômetro de parede (*tiltmeter*) | 2 eixos na torre | 1 h → 15 min | definidos pelo projetista do restauro |
| Fissuras | fissurômetros elétricos | trincas existentes mapeadas na vistoria cautelar e na termografia | 1 h (tendência) | abertura incremental (ex.: 0,3 / 0,5 mm) |
| Vibração | sismógrafo de engenharia triaxial | fundação da Estação (e do edifício nas fases críticas) | contínuo por gatilho na compactação e nas fundações | 2,0 / 3,0 mm/s |
| Recalque — edifício | marcos + prismas | 6 pilares | 2 h → 30 min | definidos pelo projetista (β alerta 1/500) |
| Maturidade | sensores de temperatura embutidos | tabuleiro, por etapa de concretagem | 30 min | decisão de protensão ($f_c \ge 25\,\mathrm{MPa}$) |
| Ruído e MP10 (desejável) | sonômetro e sensor ótico calibrado por colocalização | divisa da Estação e do edifício | 1 min (agregado em 15 min) | gatilhos próprios do plano (NBR 10151; CONAMA 506/2024 como referência) |

Requisitos obrigatórios do plano:

- **leitura zero** de todos os instrumentos antes de qualquer serviço, repetida 2 ou 3 vezes;
- **vistoria cautelar** com fotos datadas e termografia;
- os limites da Estação são **mais restritivos** que os de um edifício comum. A NBR 9653 trata de desmonte com explosivos. Para patrimônio, é usual adotar limites próprios; como referência internacional, a DIN 4150-3 indica 3 mm/s na fundação, até 10 Hz, para estruturas sensíveis.

**Leituras da semana crítica:**

- **I-2 (inclinômetro):**

$
\delta_{topo} = 0{,}5 \times (5{,}0 + 4{,}4 + 3{,}6 + 2{,}4 + 1{,}2 + 0{,}4) \times 10^{-3} = 0{,}5 \times 0{,}017 = 0{,}0085\,\mathrm{m} = 8{,}5\,\mathrm{mm}
$

O perfil acumulado de baixo para cima passa por 0,2; 0,8; 2,0; 3,8; 6,0 e 8,5 mm. A velocidade é $v = (8{,}5 - 6{,}4)/7 = 0{,}30\,\mathrm{mm/dia}$, e a atenção seria atingida em $(10 - 8{,}5)/0{,}30 = 5{,}0$ dias. Classificação: **verde**, em vigilância.

- **M-3 (recalque):**

$
u_c = \sqrt{0{,}3^2 + 0{,}4^2 + 0{,}2^2} = \sqrt{0{,}29} \approx 0{,}54\,\mathrm{mm}
\qquad
U = 2 \times 0{,}54 \approx 1{,}08\,\mathrm{mm}
$

O valor $7{,}5 + 1{,}08 \approx 8{,}6\,\mathrm{mm}$ alcança a atenção de 8 mm (regra da Aula 12: se $x + U$ alcança o limite, trata-se como atenção). A velocidade é $v = (7{,}5 - 6{,}6)/2 = 0{,}45\,\mathrm{mm/dia} > 0{,}3$. Mantido o ritmo, a atenção chega em cerca de 1,1 dia e o alerta de 12 mm em $(12 - 7{,}5)/0{,}45 = 10$ dias. Classificação: **amarelo**, por incerteza e por velocidade.

- **Distorção angular M-3/M-4:**

$
\beta = \frac{7{,}5 - 2{,}5}{5.000} = 0{,}001 = \frac{1}{1.000}
$

Atingiu a atenção da Estação. Classificação: **amarelo**. Para um edifício comum, Bjerrum (1/500) ainda daria folga; para alvenaria histórica, o plano é mais exigente.

- **PZ-2 (piezômetro):** o NA está a 1,6 m do fundo, entre a atenção (2,0 m) e o alerta (1,0 m): **amarelo**. A $0{,}15\,\mathrm{m/h}$, o alerta chega em $(1{,}6 - 1{,}0)/0{,}15 = 4{,}0\,\mathrm{h}$, por volta das 3h da madrugada.
- **Vibração:** pela NBR 9653, a 18 Hz, o limite é $20 + 30 \times (18 - 15)/25 = 23{,}6\,\mathrm{mm/s}$, e $2{,}4/23{,}6 \approx 10\%$ dele. Pelo **plano**, porém, 2,4 mm/s está entre 2,0 e 3,0: **amarelo**. A boa resposta destaca que a norma de desmonte não é o limite para um bem tombado.

**Leitura integrada esperada.** Três amarelos simultâneos na Estação (recalque, distorção e vibração) durante a compactação vibratória **não são coincidência**. Ações esperadas:

- trocar o rolo vibratório por **rolo estático** ou compactação em camadas finas na faixa próxima à Estação, e verificar o efeito no sismógrafo e no M-3 (malha fechada);
- aumentar a frequência de leitura;
- fazer o nivelamento manual de conferência do M-3;
- inspecionar as trincas e o fissurômetro;
- avisar o projetista e o Conselho do Patrimônio, conforme o TARP.

**Maturidade:**

$
M = 12 \times (30 + 34 + 29 + 25) = 1.416\,^\circ\mathrm{C \cdot h}
\qquad
f_c = 9{,}2\,\ln 1.416 - 41 \approx 25{,}8\,\mathrm{MPa} \ge 25
$

$
M_{nec} = e^{(25 + 41)/9{,}2} \approx 1.305\,^\circ\mathrm{C \cdot h}
\qquad
t \approx 36 + \frac{1.305 - 1.116}{25} \approx 43{,}6\,\mathrm{h}
$

A protensão é liberável a partir de cerca de 44 h, **confirmando com corpos de prova** e com o projetista. A maturidade não substitui o controle de aceitação.

**(e) Arquitetura, autonomia, TARP e dashboard.**

- **Percepção:** sensores e dataloggers a bateria.
- **Rede:** **LoRaWAN**. Um gateway no centro do corredor cobre cerca de 750 m para cada lado, dentro dos 2 a 5 km urbanos. Prever **um segundo gateway para redundância** e backhaul 4G com reserva. A estação total robótica e as câmeras usam 4G/fibra.
- **Plataforma:** na nuvem, com banco de séries temporais.
- **Aplicação:** dashboard e alertas.
- **Protocolo:** MQTT sobre **TLS**.
- **Regra crítica na borda:** acionar a bomba reserva quando o PZ-2 cruza o alerta, mesmo sem internet.

Autonomia do nó:

$
\bar I_{15} = \frac{2 \times 25 + 1 \times 120 + 897 \times 0{,}02}{900} \approx 0{,}209\,\mathrm{mA}
\qquad
t = \frac{0{,}8 \times 19.000}{0{,}209} \approx 72.800\,\mathrm{h} \approx 8{,}3\,\mathrm{anos}
$

$
\bar I_{5} = \frac{50 + 120 + 297 \times 0{,}02}{300} \approx 0{,}586\,\mathrm{mA}
\qquad
t = \frac{15.200}{0{,}586} \approx 25.900\,\mathrm{h} \approx 1.080\,\mathrm{dias} \approx 3{,}0\,\mathrm{anos}
$

Mesmo **inteiramente em atenção**, o nó dura mais que os 26 meses da obra (cerca de 790 dias). A amostragem adaptativa sai "de graça" em energia. Os nós de leitura rápida (sismógrafo e inclinômetro in-place com muitos sensores) precisam de painel solar ou rede.

**TARP esperado (exemplo para a Estação):**

| Nível | Gatilho | Ação | Responsável / prazo |
| --- | --- | --- | --- |
| Verde | todos abaixo da atenção | rotina | equipe de monitoramento |
| Amarelo | valor, velocidade ou $x + U$ acima da atenção, com persistência de 2 leituras ou confirmação por 2º instrumento | aumentar a frequência, inspecionar, rever o método (vibração), avisar o projetista e o Conselho | engenheiro da obra, em 24 h |
| Vermelho | alerta confirmado ($x - U$ acima do limite) | paralisar a frente próxima, executar as contingências (reforço, escoramento da Estação, reavaliar o rebaixamento) | projetista + responsável técnico + fiscal, imediato; reunião no mesmo dia |

**Automático:** aumentar a frequência, notificar, registrar, ligar a bomba reserva (ação reversível, urgente e de baixo risco) e sinalizar ao operador do rolo. **Humano:** paralisar frentes, mudar o método, reforçar a contenção, interditar a Estação ou o edifício. Esperam-se ainda redundância contra falsos alarmes (mediana de 3 leituras, persistência) e combate à **fadiga de alarmes**.

**Dashboard:** planta do corredor com cada instrumento colorido pelo estado; séries com os limites desenhados e a velocidade; saúde dos sensores (bateria, última leitura, sinal); lista de alarmes com reconhecimento (quem, quando, ação). **Todo alarme com dono.**

**(f) BIM, gêmeo e IA.**

$
d = \sqrt{14^2 + 7^2} = \sqrt{245} \approx 15{,}7\,\mathrm{mm}
\qquad
d - U \approx 10{,}7 < 15
\qquad
d + U \approx 20{,}7 > 15
$

O pilar P4 é **inconclusivo**. A conduta é nova medição com método mais exato (estação total) antes de abrir não conformidade ou liberar. Pendência **BCF** esperada: elemento (GUID do P4), problema, responsável (topografia → projetista) e prazo.

Os instrumentos são associados aos GUIDs (`IfcSensor`) e os elementos coloridos pelo nível de alerta, num CDE com estados (ISO 19650). O sistema é uma **sombra digital** com o engenheiro fechando a malha; não é um gêmeo digital pleno, salvo a regra automática da bomba.

**Métricas da IA:**

$
P_{0,5} = \frac{70}{84} \approx 0{,}83
\quad
R_{0,5} = \frac{70}{90} \approx 0{,}78
\quad
F_{1} \approx 0{,}80
\qquad
P_{0,3} = \frac{86}{148} \approx 0{,}58
\quad
R_{0,3} = \frac{86}{90} \approx 0{,}96
\quad
F_{1} \approx 0{,}72
$

Escolha esperada: **limiar 0,3**. Em patrimônio, a fissura perdida (FN) é o erro grave: caem de 20 para 4, ao custo de revisar 148 fotos em vez de 84. A IA faz **triagem**, e o engenheiro decide.

**GSD a 15 m:**

$
GSD = \frac{13{,}2 \times 15.000}{8{,}8 \times 5.472} \approx 4{,}11\,\mathrm{mm/px}
\qquad
\frac{1}{4{,}11} \approx 0{,}24\ \text{pixel}
$

A trinca de 1 mm **não é mensurável**. Para 2 pixels ($GSD \le 0{,}5\,\mathrm{mm/px}$), seria preciso voar a cerca de **1,8 m**, o que é inviável, ou usar zoom de $f \approx 72\,\mathrm{mm}$ a 15 m. A medição fica com os **fissurômetros**.

O avanço por IA no ortomosaico ou nas câmeras fixas alimenta o 4D (índice de 0,88 do item b).

**(g) Gestão.**

$
C = 640.000 + 26 \times 38.000 = \mathrm{R\$}\,1.628.000
\qquad
\frac{1{,}628}{148} \approx 1{,}1\%\ \text{do custo da obra}
$

$
VE_{sem} = 0{,}06 \times 12 + 0{,}04 \times 20 + 0{,}05 \times 6 = \mathrm{R\$}\,1{,}82\,\text{milhão}
\qquad
VE_{com} = 0{,}015 \times 4 + 0{,}01 \times 6 + 0{,}015 \times 2 = \mathrm{R\$}\,0{,}15\,\text{milhão}
$

A perda evitada é de **R\$ 1.670.000**. Os ganhos diretos com as medições são $26 \times (15.000 - 6.500) = \mathrm{R\$}\,221.000$. Então:

$
B = 1.670.000 + 221.000 = \mathrm{R\$}\,1.891.000
\qquad
ROI = \frac{1.891.000 - 1.628.000}{1.628.000} \approx 16{,}2\%
\qquad
B/C \approx 1{,}16
$

**Sensibilidade (esperada e decisiva):** se as probabilidades sem monitoramento forem a metade das estimadas, $B = 910.000 - 150.000 + 221.000 = \mathrm{R\$}\,981.000$ e $B/C \approx 0{,}60$. O retorno financeiro **depende fortemente das estimativas**. A defesa não pode parar no ROI. Ela também se apoia:

- no **patrimônio tombado**, que é irreversível e não monetizável;
- na **condição imposta pelo Conselho** para autorizar a obra;
- na redução de **litígios**, já vividos pela prefeitura;
- na segurança de pessoas.

Quem só apresenta o ROI de 16% sem sensibilidade perde pontos.

**SLA:**

$
30 \times 24 \times 60 \times 0{,}0005 = 21{,}6\,\mathrm{min/mês}
$

Mesmo com essa disponibilidade, a regra crítica deve rodar na borda.

**LGPD.** A prefeitura é **controladora** e o fornecedor de monitoramento é **operador**. A base legal típica é a execução de políticas públicas pela administração (art. 7º, III, com art. 23) e a proteção da vida e da incolumidade física. Inventário de dados pessoais:

- rostos de pedestres;
- placas de veículos;
- janelas do edifício;
- trabalhadores nas câmeras e nas etiquetas **UWB**;
- registros de acesso à plataforma.

Medidas de minimização e governança:

- polígono de voo e enquadramento restritos à faixa;
- **máscara de privacidade** nas janelas;
- desfoque automático de rostos e placas;
- UWB processado **na borda**, só para proximidade, sem histórico nominal e **sem uso para avaliar desempenho**;
- câmeras **sem reconhecimento facial**;
- retenção definida e aviso nos acessos e aos moradores;
- RIPD e encarregado definidos.

**Segurança da informação:**

- troca de credenciais padrão e autenticação forte;
- AES-128 no LoRaWAN e TLS no MQTT;
- segmentação da rede;
- atualização de firmware, logs, cópias de segurança e verificação da **integridade** das séries;
- referência ISO/IEC 27001 e OWASP IoT.

**Contrato** (plano de monitoramento como **anexo do edital**):

- escopo: instrumentos, posições e frequências;
- **TARP** com responsáveis e prazos, incluindo plantão 24 h;
- **SLA**: 99,95%, tempo leitura→painel e prazo de reparo de sensor;
- método de medição de volumes: primitivo, MDT, checkpoints, tolerância e arbitragem;
- **propriedade dos dados** da prefeitura, com entrega em formatos abertos (CSV, IFC, LAS);
- papéis da LGPD e comunicação de incidentes à ANPD;
- **ART** do responsável pelo monitoramento;
- exigências regulatórias do operador de drone: SISANT, piloto, seguro, aerolevantamento por entidade inscrita.

**Resposta de alta qualidade** demonstra:

- partir dos riscos e terminar em respostas com dono e prazo;
- números corretos e rastreáveis, sobretudo a altura de voo limitada pelo **fundo da trincheira**, os 2 voos, o RMSE sem viés, a densidade no solo e a autonomia em atenção;
- leitura **integrada** dos três amarelos da Estação, com uma ação que fecha a malha;
- distinção entre **norma de referência e limite do plano**;
- enquadramento correto da operação (categoria aberta × específica pela proximidade de terceiros, aerolevantamento);
- custo-benefício com sensibilidade;
- reconhecimento dos limites físicos (GSD não mede trinca de 1 mm; LiDAR passa pelas frestas, não pelas folhas).

**Resposta de baixa qualidade** comumente apresenta:

- lista de equipamentos sem riscos, limites nem ações;
- GSD calculado com a altura da decolagem, ignorando o fundo da trincheira;
- um único voo de 1.500 m sem checar bateria nem VLOS;
- uso do MDS para volume;
- LiDAR no corredor inteiro sem justificativa;
- uso dos limites da NBR 9653 para o bem tombado;
- "categoria aberta" sem considerar pedestres na avenida;
- omissão do aerolevantamento;
- IA tratada como medição;
- ROI sem sensibilidade;
- LGPD reduzida a uma frase.
