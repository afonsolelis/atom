# Entrega de Trabalho (PBL) — Drones e Sensores IoT no Monitoramento de Obras

> Roteiro para elaboração com **Problem-Based Learning**.

- **Disciplina:** Drones e Sensores IoT no Monitoramento de Obras
- **Professor-conteudista:** Afonso Cesar Lelis Brandão

> O **CASE** existe para que o estudante entenda a aplicabilidade do conteúdo estudado na realidade do mercado de trabalho.

---

## Título

**Corredor Leste de Vale Verde — Plano Integrado de Monitoramento por Drones e Sensores IoT de uma Trincheira e um Viaduto Urbanos ao Lado de uma Estação Ferroviária Tombada**

---

## Desafio

> **O quê?** A prefeitura de uma cidade média precisa de um **plano integrado de monitoramento** para uma obra viária linear em área urbana consolidada. São duas estruturas principais: uma **trincheira** (passagem inferior) escavada junto a edificações sensíveis e um **viaduto** que atravessa um córrego com mata ciliar. O plano deve juntar o **voo de drones** (planejamento, regulamentação e segurança), o **processamento das imagens** (fotogrametria, GNSS, ortomosaicos, MDS/MDT, LiDAR, volumes e projetado × executado), os **sensores IoT e as redes de comunicação**, os **painéis com alertas**, a **integração com o BIM e com o planejamento e controle da obra**, a **segurança do trabalho** e a **proteção de dados e a cibersegurança**.
>
> **Quem?** A **Secretaria Municipal de Obras de Vale Verde** (município fictício, com cerca de 420 mil habitantes) é a contratante e a **controladora** dos dados. A obra está sendo licitada, e você trabalha na **gerenciadora** que vai redigir o **plano de monitoramento**, anexo obrigatório do edital. Com base na Lei nº 14.133/2021 (art. 19, § 3º), a prefeitura decidiu exigir **BIM**, com modelo 4D da execução, medição do avanço físico a partir do modelo e atualização *as-built*.
>
> **Quando?** Prazo de obra de **26 meses**, com início previsto para **março de 2027**. O plano precisa estar pronto antes da licitação, porque o monitoramento vai entrar no orçamento e no contrato.
>
> **Onde?** No **Corredor Leste**, uma faixa de obra de **1.500 m × 160 m** (24 ha) ao longo de uma avenida com tráfego e pedestres. Ela tem três trechos:
>
> - **Trecho A — Trincheira (380 m).** Escavação com profundidade máxima de **8,5 m** e largura de **28 m**. A contenção é uma **cortina de estacas secantes com estroncas metálicas**, e o lençol freático está a **3,0 m** de profundidade, com rebaixamento por poços. A **12 m** da cortina fica a **antiga Estação Ferroviária de Vale Verde (1912)**, desativada e hoje Centro Cultural: **tombada pelo patrimônio municipal**, em alvenaria de tijolos sobre **fundação rasa**, com trincas antigas e uma torre do relógio. Do outro lado, a **9 m** da cortina, há um **edifício residencial de 10 pavimentos (cerca de 32 m de altura)**. O volume total de corte previsto é de **64.000 m³** (*in situ*). Ao lado do acesso da trincheira, um aterro será compactado com **rolo vibratório**.
> - **Trecho B — Viaduto (240 m, 6 vãos)** sobre o **Córrego das Pedras**, cujas margens têm **mata ciliar densa** em área de preservação permanente. O projeto hidráulico e a locação dos pilares P3 e P4 exigem o **terreno natural sob a mata** numa faixa de **2,6 ha**, sem desmatar para medir. O tabuleiro será moldado no local e protendido, com apoio de uma **grua de 45 m**.
> - **Trecho C — Ligações e pavimentação (880 m)**, com obras de baixo risco.
>
> **Por quê?** A prefeitura já viveu duas disputas judiciais recentes por **danos a imóveis vizinhos** e por **medições de terraplenagem contestadas**. O Conselho Municipal do Patrimônio só autorizou a obra com **monitoramento contínuo da Estação**. E a última obra viária da cidade teve um atropelamento grave dentro de uma escavação. **Dados disponíveis (valores ilustrativos para o case):**
>
> - **Drone de mapeamento:** multirrotor de 6,3 kg com **RTK** e câmera RGB de $5.472 \times 3.648$ pixels, $p = 2{,}41\,\mathrm{\mu m}$, $f = 8{,}8\,\mathrm{mm}$ (lado maior perpendicular ao voo). Voa a $6\,\mathrm{m/s}$, com **20 min úteis** por bateria em condição normal e resistência ao vento de $12\,\mathrm{m/s}$. Em manhãs abaixo de 10 °C, o fabricante recomenda considerar **15% a menos** de autonomia. O edital exige **GSD ≤ 2,5 cm em toda a área, inclusive no fundo da trincheira**, sobreposições de **80% (frontal) e 70% (lateral)**, $RMSE_z \le 4\,\mathrm{cm}$ nos checkpoints e **levantamento mensal**. Por segurança operacional e linha de visada, a gerenciadora quer dividir o corredor em **2 blocos de 750 m**, com decolagem no centro de cada bloco.
> - **Previsão para a manhã do voo do mês 6** (a 10 m de altura): vento médio de $3{,}5\,\mathrm{m/s}$ e rajadas de $5{,}0\,\mathrm{m/s}$; temperatura de 9 °C às 7h; índice Kp de 3 pela manhã e de 6 à noite. Para o perfil de vento, use $v_H = v_{10}\,(H/10)^{0{,}2}$.
> - **Controle do levantamento do mês 6:** resíduos verticais (modelo − campo) em 8 checkpoints independentes, em cm: $+2{,}1$; $-1{,}4$; $+3{,}0$; $+0{,}8$; $-2{,}2$; $+1{,}7$; $+2{,}6$; $-0{,}9$. O aplicativo do drone grava **altura elipsoidal**; no corredor, a ondulação geoidal é $N \approx -6{,}10\,\mathrm{m}$, e o projeto está em altitudes.
> - **Volumes do mês 6 (MDT anterior − MDT atual, na área da trincheira, $380 \times 28\,\mathrm{m}$):** $9.850\,\mathrm{m^3}$ escavados, contra $11.200\,\mathrm{m^3}$ previstos no 4D para o mês. O acumulado até o mês 5 era de $31.400\,\mathrm{m^3}$. Empolamento de 30% e caminhões de $14\,\mathrm{m^3}$. Na frente já escavada, o fundo foi comparado ao greide em três trechos, com desvios médios de $+2$, $+6$ e $+11\,\mathrm{cm}$, tolerância de $5\,\mathrm{cm}$ e incerteza expandida $U = 3\,\mathrm{cm}$.
> - **LiDAR disponível para a mata ciliar:** $PRR = 240\,\mathrm{kHz}$, campo de visão de $70°$, voo a $H = 60\,\mathrm{m}$ e $v = 6\,\mathrm{m/s}$, com erro de atitude da IMU de $0{,}05°$. O projeto pede **ao menos 10 pontos/m² no solo**, e estima-se que **10%** dos pulsos cheguem ao chão.
> - **Câmera térmica para a fachada da Estação:** $640 \times 512$ pixels, pixel de $12\,\mathrm{\mu m}$, $f = 13\,\mathrm{mm}$. O objetivo é localizar descolamentos de reboco a partir de **5 cm**, considerando que um defeito precisa ocupar $3 \times 3$ pixels.
> - **Leituras da semana crítica (mês 6), já com os níveis do plano preliminar** (escala de 4 níveis: **verde** — normal; **amarelo** — atenção; **laranja** — alerta; **vermelho** — alarme):
>   - **Inclinômetro in-place I-2** (atrás da cortina, frente da Estação, $L = 0{,}5\,\mathrm{m}$): variações de $\sin\theta$, do topo para baixo, de $5{,}0$; $4{,}4$; $3{,}6$; $2{,}4$; $1{,}2$ e $0{,}4 \times 10^{-3}$, sem variação abaixo. Há 7 dias, o topo estava em $6{,}4\,\mathrm{mm}$. Níveis: atenção em 10 mm **ou** 0,5 mm/dia; alerta em 14 mm **ou** 1,0 mm/dia; alarme em 18 mm.
>   - **Marco de recalque M-3** (pilar da Estação), leituras diárias de $6{,}1$; $6{,}4$; $6{,}6$; $7{,}0$ e $7{,}5\,\mathrm{mm}$, com incerteza expandida $U = 1{,}1\,\mathrm{mm}$. Níveis da Estação: atenção em 8 mm **ou** 0,3 mm/dia; alerta em 10 mm **ou** 0,6 mm/dia; alarme em 12 mm.
>   - **Estronca E-5** (aço, $E = 200\,\mathrm{GPa}$, $A = 150\,\mathrm{cm^2}$, carga de projeto de $900\,\mathrm{kN}$): o extensômetro de corda vibrante indica $390\,\mu\varepsilon$ brutos desde a leitura zero, dos quais o termistor atribui $180\,\mu\varepsilon$ ao efeito térmico. Níveis: atenção em 70%, alerta em 85% e alarme em 100% da carga de projeto.
>   - **Piezômetro de corda vibrante PZ-2:** depois de uma chuva às 23h, o nível d'água está a $1{,}6\,\mathrm{m}$ abaixo do fundo da escavação e sobe $0{,}15\,\mathrm{m/h}$. Níveis: atenção a 2,0 m, alerta a 1,5 m e alarme a 1,0 m abaixo do fundo.
>   - **Acelerômetro triaxial na fundação da Estação**, durante a compactação vibratória: velocidade de partícula de pico de $2{,}4\,\mathrm{mm/s}$, com frequência dominante de $18\,\mathrm{Hz}$ e componentes de interesse até $50\,\mathrm{Hz}$. Níveis do plano: atenção em 2,0, alerta em 3,0 e alarme em 5,0 mm/s.
>   - **Sensor ótico de MP10** na divisa da Estação: média de 24 h de $128\,\mathrm{\mu g/m^3}$, numa noite com umidade relativa acima de 90%.
> - **Nó sensor IoT típico:** bateria de $19.000\,\mathrm{mAh}$ (80% utilizável). Em cada ciclo, lê por 2 s a 25 mA, transmite por 1 s a 120 mA e dorme a 0,02 mA. O ciclo é de 15 min em rotina e de 5 min em atenção. O nó do PZ-2, no fundo da trincheira, fica a $0{,}8\,\mathrm{km}$ do gateway LoRaWAN ($915\,\mathrm{MHz}$), transmite a $14\,\mathrm{dBm}$, com antenas de $2$ e $3\,\mathrm{dBi}$ e perdas por paredes, terreno e cabos de $30\,\mathrm{dB}$; a sensibilidade em SF7 é de $-123\,\mathrm{dBm}$.
> - **Tabuleiro do viaduto:** a protensão exige $f_c \ge 25\,\mathrm{MPa}$. A calibração da mistura (ilustrativa) é $f_c = 9{,}2\,\ln M - 41$ (MPa, $M$ em °C·h, $T_0 = 0\,^\circ\mathrm{C}$). Os sensores de temperatura embutidos registraram médias de 30, 34, 29 e 25 °C em quatro blocos consecutivos de 12 h.
> - **BIM e avanço físico (mês 6):** orçamento de **R\$ 148 milhões**; a curva S previa **38%** de avanço acumulado, e o custo real é de **R\$ 53,0 milhões**. Pesos e avanços medidos: terraplenagem da trincheira (12%), pelo volume do drone; contenção (18%), 85% pelo as-built; fundações e pilares do viaduto (25%), 40% pela nuvem de pontos; tabuleiro (20%), 5%; pavimentação e ligações (25%), 0%. **Scan-vs-BIM do pilar P4:** $\Delta x = 14\,\mathrm{mm}$, $\Delta y = -7\,\mathrm{mm}$, $U = 5\,\mathrm{mm}$ e tolerância contratual de $15\,\mathrm{mm}$.
> - **Segurança do trabalho:** escavadeiras e caminhões manobram dentro da trincheira; no mês 6, o anemômetro da grua do viaduto registrou rajadas de $12{,}5\,\mathrm{m/s}$; há trechos do tabuleiro sem guarda-corpo definitivo. As câmeras fixas terão detector de ausência de capacete, testado em 160 situações reais sem capacete: com limiar 0,5, $VP = 120$, $FP = 20$ e $FN = 40$; com limiar 0,3, $VP = 148$, $FP = 64$ e $FN = 12$. Nos 6 primeiros meses, com 320 trabalhadores e 200 h/mês cada, houve 5 acidentes com afastamento.
> - **Pessoas e dados:** a avenida tem pedestres e veículos (placas). O edifício tem janelas voltadas para a obra. Haverá **câmeras fixas** para avanço físico e segurança e **etiquetas UWB** nos capacetes, para criar cercas virtuais em torno das escavadeiras dentro da trincheira. A plataforma usará broker MQTT, InfluxDB e Grafana; o fornecedor entregou o gateway com a senha de fábrica.
>
> **Sua missão como engenheiro(a) da gerenciadora:** elaborar um **plano integrado de monitoramento completo e defensável** para o Corredor Leste. O plano deve integrar as 4 unidades da disciplina:
>
> - **Unidade 1:** monitoramento e indicadores de avanço, drones e sensores embarcados, regulamentação (ANAC, DECEA, Anatel) e planejamento de missão com meteorologia e segurança;
> - **Unidade 2:** fotogrametria, GNSS e exatidão, ortomosaicos, MDS/MDT, nuvens de pontos e LiDAR, volumes, curvas de nível e projetado × executado;
> - **Unidade 3:** sensores para obras, plataformas embarcadas, redes LoRaWAN/Wi-Fi/celulares, MQTT e séries temporais;
> - **Unidade 4:** painéis, alertas e TARP de 4 níveis, integração com BIM e com o planejamento e controle, segurança do trabalho (NR-18) e LGPD/cibersegurança.
>
> **Todos os números** do plano devem ser **calculados e demonstrados passo a passo**.

---

## Fonte de pesquisa

O ESTUDANTE deverá pesquisar um exemplo de como outros profissionais ou empresas já resolveram esse desafio.

**Fontes de pesquisa primária:**

Pesquise como o setor planeja, executa e contrata o monitoramento de obras urbanas com drones e sensores:

1. **Material da disciplina** — as 16 aulas, com ênfase nas Aulas 3 e 4 (regulamentação, planejamento de missão e segurança de voo), 5 a 8 (fotogrametria, GNSS, produtos, volumes e projetado × executado), 9 a 12 (sensores, plataformas embarcadas, redes e MQTT) e 13 a 16 (painéis e alertas, BIM e controle, NR-18, LGPD e cibersegurança).
2. **Bibliografia básica da disciplina** — MATTOS, A. D. *Planejamento e controle de obras*. São Paulo: Pini, 2010 (curva S, avanço físico e valor agregado) · COELHO, L.; BRITO, J. N. *Fotogrametria digital*. 2. ed. Rio de Janeiro: EdUERJ, 2007 (orientação, colinearidade, fototriangulação) · MAGRANI, E. *A internet das coisas*. Rio de Janeiro: FGV Editora, 2018.
3. **Bibliografia complementar da disciplina** — MONICO, J. F. G. *Posicionamento pelo GNSS*. 2. ed. São Paulo: Editora UNESP, 2008 · EASTMAN, C. *et al.* *Manual de BIM*. Porto Alegre: Bookman, 2014 · GUBBI, J. *et al.* Internet of Things (IoT): a vision, architectural elements, and future directions. *Future Generation Computer Systems*, v. 29, n. 7, p. 1645-1660, 2013 — https://doi.org/10.1016/j.future.2013.01.010.
4. **ANAC — RBAC-E nº 94 (2017, referência histórica) e RBAC nº 100, Emenda 00 (texto integral)** — https://pergamum.anac.gov.br/pergamum/vinculos/RBAC100EMD00.pdf — e o portal de drones da ANAC: https://www.gov.br/anac/pt-br/assuntos/drones (categorias aberta, específica e certificada; SISANT; exame teórico; seguro).
5. **DECEA — ICA 100-40 (2026), *Aeronaves Não Tripuladas e o Acesso ao Espaço Aéreo Brasileiro*** — https://www.gov.br/defesa/pt-br/assuntos/aerolevantamento/arquivos/2026/ica-100-40-publicada-port-2094-dnor8-18-03-2026-bca-058-30-03-2026.pdf (SARPAS e antecedências) — e **Ministério da Defesa — Aerolevantamento** — https://www.gov.br/defesa/pt-br/assuntos/aerolevantamento (Decreto nº 2.278/1997 e Portaria GM-MD nº 3.703/2021).
6. **Lei nº 13.709/2018 (LGPD)** — https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm — e **Decreto nº 10.306/2020 (BIM na administração pública federal)** — https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2020/decreto/D10306.htm.
7. **NR-18 — Segurança e Saúde no Trabalho na Indústria da Construção** — https://www.gov.br/trabalho-e-emprego/pt-br/acesso-a-informacao/participacao-social/conselhos-e-orgaos-colegiados/comissao-tripartite-partitaria-permanente/normas-regulamentadora/normas-regulamentadoras-vigentes/norma-regulamentadora-no-18-nr-18 — e **OWASP — Internet of Things Project (IoT Top 10)** — https://owasp.org/www-project-internet-of-things/.
8. **Ferramentas sugeridas pela ementa** — DJI Pilot ou PIX4Dcapture (missões); OpenDroneMap (https://docs.opendronemap.org/) ou Agisoft Metashape (fotogrametria); QGIS (https://docs.qgis.org/latest/pt_BR/docs/user_manual/); ESP32/Arduino com MQTT; Node-RED, InfluxDB e Grafana (https://grafana.com/docs/grafana/latest/alerting/).
9. **Artigos científicos** — SIEBERT, S.; TEIZER, J. (2014), drones em terraplenagem: https://doi.org/10.1016/j.autcon.2014.01.004 · JAMES, M. R.; ROBSON, S. (2014), efeito de domo: https://doi.org/10.1002/esp.3609 · MISHRA, M.; LOURENÇO, P. B.; RAMANA, G. V. (2022), monitoramento estrutural com IoT: https://doi.org/10.1016/j.jobe.2021.103954.

**Aulas relacionadas:** todas as 16 servem de insumo. Em ordem de relevância:

- Aula 4 (planejamento de missão, meteorologia e segurança) e Aula 3 (regulamentação);
- Aulas 5, 6 e 8 (fotogrametria, GNSS e exatidão, volumes e projetado × executado);
- Aula 13 (painéis, alertas e TARP de 4 níveis);
- Aula 9 (sensores para obras) e Aulas 10 a 12 (plataformas embarcadas, redes e MQTT);
- Aula 14 (BIM, curva S e valor agregado) e Aula 1 (indicadores de controle de avanço);
- Aula 7 (ortomosaico, MDS/MDT e LiDAR) e Aula 2 (drones e sensores embarcados);
- Aulas 15 e 16 (NR-18, LGPD e cibersegurança).

---

## 5. Entregável e distribuição da pontuação

Sua entrega final da disciplina **Drones e Sensores IoT no Monitoramento de Obras** tem **3 entregáveis obrigatórios**. O objetivo é elaborar o **plano integrado de monitoramento do Corredor Leste**. Nele, você deve mostrar que sabe:

- **planejar missões de voo** dentro da regulamentação e com segurança;
- **processar as imagens** e **comparar o executado com o projetado**, provando a exatidão;
- **selecionar e configurar sensores e redes IoT** a partir dos riscos da obra;
- **criar painéis e definir alertas** com um plano de resposta de 4 níveis (malha fechada);
- **integrar** drone e sensores ao **BIM** e ao **planejamento e controle** da obra;
- garantir a **segurança do trabalho**, a **proteção de dados** e a **cibersegurança**.

Os números devem ser **calculados e demonstrados passo a passo**, e não estimados "no olho".

### 1. Parte Teórica — (25% da nota)

Desenvolva um **relatório técnico em PDF** contendo:

- **Diagnóstico de riscos** da obra: Estação tombada, edifício vizinho, contenção e rebaixamento, terreno sob a mata, medição de volumes, segurança de pessoas e disputas contratuais. Para cada risco, indique a **grandeza** a medir e a **consequência** de não medir a tempo.
- **Fundamentação** das escolhas, com os conceitos das 4 unidades:
  - malha aberta × fechada, curva S e valor agregado;
  - aeronave e sensor embarcado para cada pergunta da obra;
  - fotogrametria (sobreposição, GCPs, checkpoints, domo) × LiDAR;
  - precisão × exatidão, RMSE e PEC-PCD; MDS × MDT;
  - escolha de sensores pelo mensurando, Nyquist e calibração;
  - alcance × taxa × consumo na escolha da rede; MQTT e séries temporais;
  - níveis por valor e velocidade, TARP, fadiga de alarmes;
  - BIM 4D, IFC/GUID, BCF e CDE; sombra × gêmeo digital.
- **Enquadramento regulatório e legal:**
  - RBAC nº 100 (categoria da operação em cada trecho) e a transição do RBAC-E nº 94;
  - SISANT, exame teórico e seguro;
  - SARPAS (ICA 100-40) e aerolevantamento (Ministério da Defesa);
  - homologação da Anatel (drones, nós e gateways);
  - NR-18 (PGR, proteção coletiva, máquinas e grua);
  - LGPD (base legal da administração pública, papéis e incidentes);
  - Lei nº 14.133/2021 (BIM).

**Critérios de avaliação da Parte Teórica (25 pontos):**

| Critério | Pontos |
| --- | --- |
| Riscos identificados e convertidos em grandezas mensuráveis, com consequência explícita | 7 |
| Fundamentação correta dos conceitos das 4 unidades (sem confundir precisão × exatidão, MDS × MDT, altura elipsoidal × altitude, padrão ambiental × limite do plano) | 8 |
| Enquadramento regulatório e legal correto (RBAC nº 100, ICA 100-40, aerolevantamento, Anatel, NR-18, LGPD) | 6 |
| Uso das fontes, inclusive da bibliografia da disciplina (citadas em ABNT), e clareza do texto | 4 |

### 2. Parte Prática — (50% da nota)

Desenvolva o **plano integrado de monitoramento** com, no mínimo:

- **(a) Missão de voo, meteorologia e segurança (Unidade 1).**
  - Calcule a altura máxima que garante o GSD exigido no fundo da trincheira e adote uma altura de voo.
  - Calcule o GSD na via e no fundo, o *footprint*, a base, o espaçamento entre faixas, o intervalo entre fotos, o número de faixas e de fotos por bloco, o tempo de voo e o **número de voos**, considerando a redução de autonomia no frio.
  - Calcule o vento médio e as rajadas na altura de voo, decida "voa / não voa" e justifique o horário pelo índice Kp.
  - Defina a altura de retorno automático, a área de segurança, o checklist pré-voo e as respostas a emergências.
  - Enquadre cada operação (mapeamento mensal, LiDAR na mata, termografia da Estação) no RBAC nº 100 e indique SARPAS, aerolevantamento e Anatel.
- **(b) Processamento, exatidão e projetado × executado (Unidade 2).**
  - Avalie os resíduos do mês 6 (média, $RMSE_z$, conformidade, viés) e classifique a altimetria pelo PEC-PCD (equidistância de curvas compatível com a Classe A).
  - Explique o tratamento da altura elipsoidal e a distribuição de GCPs e checkpoints.
  - Calcule o efeito do viés sobre o volume do mês, o índice de avanço contra o 4D, o volume solto, o número de viagens e o percentual acumulado da trincheira.
  - Classifique os três trechos do fundo (conforme, inconclusivo ou não conforme).
  - Justifique o LiDAR na mata e calcule a densidade total e no solo e o erro de atitude na borda da faixa; calcule a distância máxima da câmera térmica à fachada e o menor defeito detectável.
- **(c) Instrumentação IoT (Unidade 3).**
  - Monte uma tabela com grandeza, instrumento, local, quantidade, leitura zero, frequência normal → em atenção e os **4 níveis**. Cubra a trincheira, a Estação, o edifício e o viaduto.
  - Processe as **leituras da semana crítica**: deslocamento acumulado e velocidade do I-2; valor, incerteza e velocidade do M-3; força na E-5 com correção térmica; prazos do PZ-2; vibração e taxa de amostragem; leitura de poeira. Classifique cada leitura em **verde, amarelo, laranja ou vermelho**.
  - Calcule a **maturidade** e o horário mínimo da protensão.
- **(d) Plataforma IoT (Unidade 3).**
  - Descreva a cadeia de medição embarcada (datalogger × ESP32), as quatro camadas, a rede escolhida para cada grupo de sensores (com justificativa) e o orçamento de enlace do nó do PZ-2.
  - Calcule a **autonomia** do nó em rotina e em atenção, comparada ao prazo da obra.
  - Proponha os tópicos MQTT, o QoS, a segurança (TLS, ACL) e o modelo de dados no InfluxDB (measurement, tags e fields).
- **(e) Painel, alertas e TARP (Unidade 4).**
  - Monte o **TARP de 4 níveis** com gatilho (valor e velocidade), ação, responsável e prazo.
  - Indique o que é **automático** (inclusive na borda) e o que exige **decisão humana**.
  - Configure a regra de alerta no Grafana (persistência, histerese, notificação) e esboce o **dashboard**.
- **(f) BIM, planejamento e controle (Unidade 4).**
  - Calcule o avanço físico ponderado, o VP, o VA, o IDP, o IDC e a estimativa no término.
  - Classifique o pilar P4 (conforme, não conforme ou inconclusivo) e redija a pendência BCF.
  - Ligue os instrumentos aos GUIDs, defina o CDE e classifique o sistema (modelo, sombra ou gêmeo).
- **(g) Segurança do trabalho, LGPD e cibersegurança (Unidade 4).**
  - Analise a grua, a trincheira e o tabuleiro à luz da NR-18; calcule a taxa de frequência e $P$, $R$ e $F_1$ do detector de capacete nos dois limiares, e escolha um.
  - Inclua o inventário de dados pessoais com base legal e minimização, os controles de cibersegurança e o fluxo de resposta a incidentes.

**Memorial de cálculo (anexo obrigatório).** Cada cálculo deve trazer **fórmula, substituição dos dados do case e resultado com unidade**, passo a passo. **Rastreabilidade:** os resultados devem ser **citados e discutidos** no corpo do plano. Não basta anexar a conta solta.

**Critérios de avaliação da Parte Prática (50 pontos):**

| Critério | Pontos |
| --- | --- |
| (a) Missão de voo: cálculos, nº de voos, vento e Kp, segurança e enquadramento regulatório | 9 |
| (b) Processamento: RMSE, média e PEC-PCD, volumes e avanço, regra de decisão, LiDAR e termografia | 9 |
| (c) Instrumentação: tabela coerente com os riscos, cálculos das leituras, classificação em 4 níveis, maturidade | 10 |
| (d) Plataforma IoT: rede e enlace, autonomia, MQTT e modelo de dados | 6 |
| (e) Painel, TARP de 4 níveis, automático × humano, regra de alerta | 6 |
| (f) BIM e controle: valor agregado, classificação com incerteza, BCF, sombra × gêmeo | 5 |
| (g) NR-18, métricas do detector, LGPD e cibersegurança | 5 |

### 3. Vídeo Pitch — (25% da nota)

Grave um **vídeo de até 4 minutos**, simulando a apresentação do plano à **comissão da prefeitura**, com representantes de Obras, do Conselho do Patrimônio, da Segurança do Trabalho e da Procuradoria. O vídeo deve apresentar:

- O problema: obra linear urbana junto a uma Estação tombada e a um edifício de 10 pavimentos, com histórico de disputas por danos e por medições.
- A lógica do plano: **riscos → grandezas → instrumentos → limites → respostas**.
- Os **números-chave**: altura de voo e GSD, nº de voos e a decisão "voa / não voa", $RMSE_z$, densidade do LiDAR no solo, autonomia dos nós e as leituras da semana crítica com o nível de cada uma.
- A malha fechada em funcionamento (o caso do PZ-2 às 23h ou o da Estação), no painel e no TARP de 4 níveis.
- O avanço físico e o valor agregado medidos com drone e BIM.
- As garantias de segurança e legais: categoria no RBAC nº 100, aerolevantamento, NR-18, LGPD e cibersegurança.

Publique o vídeo no **YouTube (modo não listado)** ou em outra plataforma de hospedagem e insira o **link ao final do PDF**. Antes de enviar, confira se o link está acessível.

**Critérios de avaliação do Vídeo Pitch (25 pontos):**

| Critério | Pontos |
| --- | --- |
| Clareza da mensagem central e do problema nos primeiros 30 s | 5 |
| Números-chave corretos e bem explicados (sem ler tabelas inteiras) | 8 |
| Demonstração da malha fechada, do painel e da decisão tomada | 6 |
| Defesa técnica, legal e de segurança; tempo respeitado (≤ 4 min) e qualidade de áudio/imagem | 6 |

**Critérios qualitativos transversais:**

- **coerência interna** (risco → instrumento → limite → ação → responsável);
- **realismo** (frequências, limites e prazos);
- **rastreabilidade** dos cálculos;
- **integração** das 4 unidades, em vez de capítulos isolados;
- **honestidade técnica**: reconhecer incertezas, limites físicos (GSD, penetração do LiDAR, sensores óticos de poeira) e o que a tecnologia não resolve.

---

## 6. Solução (esse item será removido antes do case ser disponibilizado ao aluno)

> **Remover antes de entregar ao aluno.**
>
> **Atenção:** este tópico será removido antes do case ser disponibilizado ao aluno — é apenas para o professor tutor que corrigirá.

**Diagnóstico de riscos esperado.** O aluno deve priorizar pela combinação **consequência × velocidade de evolução**:

| Risco | Grandeza | Por que importa |
| --- | --- | --- |
| Recalque e fissuração da Estação tombada (fundação rasa, alvenaria, a 12 m) | recalque (mm) e velocidade (mm/dia), abertura de fissura, rotação da torre, vibração (mm/s) | dano irreversível a patrimônio, embargo, disputa judicial |
| Deslocamento da cortina e sobrecarga das estroncas | deslocamento horizontal (mm), deformação e força nas estroncas (kN) | instabilidade da escavação e paralisação |
| Subida do NA após chuva | nível piezométrico (m) | evolução em horas, à noite |
| Recalque do edifício de 10 pavimentos | recalque e velocidade | dano a terceiros |
| Protensão prematura do tabuleiro | temperatura e maturidade (°C·h) | fissuração, perda de protensão |
| Medição de volumes contestada | volume (m³), com exatidão provada | disputa contratual, já vivida pela prefeitura |
| Terreno sob mata ciliar | MDT sob vegetação | erro de locação de P3/P4 e desmatamento desnecessário |
| Atropelamento na trincheira, vento na grua, queda do tabuleiro | proximidade máquina-pessoa, vento (m/s), presença de proteção coletiva | vida |
| Poeira na divisa da Estação e do edifício | MP10 (µg/m³) | saúde e queixas da vizinhança |
| Privacidade e integridade dos dados | — | LGPD; leitura adulterada esconde recalque |

Nem tudo pede sensor. O volume fica com o drone, a fissura existente com a vistoria cautelar e o fissurômetro, e a referência com a topografia.

**(a) Missão de voo, meteorologia e segurança — cálculos esperados.** A exigência de GSD vale **no fundo da trincheira**, 8,5 m abaixo da via, e a altura acima do terreno é que manda (Aula 4):

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
t = \frac{4.680}{6} \approx 780\,\mathrm{s} \approx 13{,}0\,\mathrm{min}
$

A 9 °C, a autonomia útil cai a $0{,}85 \times 20 = 17\,\mathrm{min} > 13{,}0\,\mathrm{min}$: **1 bateria por bloco, 2 voos por campanha**, com as baterias aquecidas antes do voo. Num voo único de 1.500 m, o tempo seria de cerca de 25,5 min, acima de uma bateria, e o drone se afastaria demais do piloto para manter VLOS. A divisão em blocos resolve as duas coisas.

**Vento na altura de voo:**

$
\left(\frac{80}{10}\right)^{0{,}2} \approx 1{,}52
\qquad
v_{80} \approx 3{,}5 \times 1{,}52 \approx 5{,}3\,\mathrm{m/s}
\qquad
v_{rajada,80} \approx 5{,}0 \times 1{,}52 \approx 7{,}6\,\mathrm{m/s}
$

O limite prático é $2/3 \times 12 = 8\,\mathrm{m/s}$: **voa**, mas com folga pequena nas rajadas — anemômetro no local, reserva de bateria para o retorno contra o vento e critério de interrupção definido. O voo é **pela manhã**: Kp 6 à noite indica tempestade geomagnética, e no Brasil a cintilação ionosférica após o pôr do sol pode derrubar o RTK.

**Segurança de voo esperada:** RTH acima do maior obstáculo do bloco — a grua de 45 m e o edifício de 32 m —, por exemplo a 60–80 m; áreas de decolagem e pouso isoladas; observador; checklist (documentos, SARPAS, meteorologia e Kp, hélices, baterias, firmware, calibrações); respostas a perda de enlace, perda de GNSS, bateria crítica e aeronave tripulada; registro do voo e conferência das fotos em campo.

**Edifício de 32 m:** sobre a cobertura, $H = 48\,\mathrm{m}$, $W \approx 71{,}9\,\mathrm{m}$, e a sobreposição lateral cai para $1 - 36{,}0/71{,}9 \approx 50\%$. Haverá buracos ou ruído na cobertura e nas fachadas; o edifício não deve ser medido por esse voo.

**Regulamentação esperada (Aula 3).**

- **Categoria da operação no RBAC nº 100.** O drone de 6,3 kg, em VLOS, a 80 m de altura, cumpre peso, altura e linha de visada da **categoria aberta**. Porém, o corredor fica ao longo de uma **avenida com pedestres e veículos**, e a categoria aberta exige que **em nenhuma hipótese** se voe a menos de **30 m horizontais de pessoas não envolvidas e não anuentes**, salvo barreira mecânica capaz de protegê-las. Por isso, a resposta esperada é uma destas:
  - (i) os blocos sobre a via em uso ficam na **categoria específica**, com avaliação de risco operacional por método aceito pela ANAC (como o **SORA**) ou por cenário padrão e, conforme a complexidade, o **COE**;
  - (ii) os voos são feitos em janelas com **interdição da faixa** (domingo cedo, por exemplo), mantendo os 30 m; a avaliação de risco operacional atualizada continua exigida.
- **Termografia da Estação.** Voo junto a uma edificação: exige o Centro Cultural fechado e área isolada, com a equipe local **anuente**, ou a categoria específica. A distância de voo é também decisão de resolução.
- **LiDAR na mata.** Sem terceiros, pode caber na categoria aberta.
- **Requisitos para todas as operações:** aeronaves **cadastradas no SISANT**; piloto aprovado no **exame teórico da ANAC** (exigível a partir de 1º/01/2027, ou seja, durante toda a obra); **seguro** com cobertura de danos a terceiros; acesso ao espaço aéreo pelo **SARPAS** (ICA 100-40); equipamentos e rádios (drone, nós e gateways LoRaWAN) **homologados pela Anatel**. Contratos que citem "Classe 3" do RBAC-E nº 94 devem ser atualizados.
- **Aerolevantamento.** O voo mensal em faixas sobrepostas para ortomosaico e MDT é **aerolevantamento** (Portaria GM-MD nº 3.703/2021, art. 8º): só por entidade **inscrita no Ministério da Defesa**, com pedido no SARPAS feito com **4 dias corridos** de antecedência. A área de cerca de 0,24 km² tende à **pré-autorização** (art. 38), **desde que atendidas as condições cumulativas**; ela não dispensa a inscrição. O LiDAR em faixas também é aerolevantamento; a foto de inspeção da fachada, sem faixas sobrepostas, não é.

**(b) Processamento, exatidão e projetado × executado.** Resíduos do mês 6:

$
\bar{\Delta z} = \frac{2{,}1 - 1{,}4 + 3{,}0 + 0{,}8 - 2{,}2 + 1{,}7 + 2{,}6 - 0{,}9}{8} \approx 0{,}71\,\mathrm{cm}
\qquad
RMSE_z = \sqrt{\frac{31{,}31}{8}} \approx 1{,}98\,\mathrm{cm} \approx 0{,}9\,GSD_{via}
$

Resultado: $1{,}98 \le 4\,\mathrm{cm}$, **atende**; os sinais se alternam e a média é pequena: **não há viés relevante**. PEC-PCD, Classe A altimétrica: $Eq \ge 6 \times 1{,}98 \approx 11{,}9\,\mathrm{cm}$ → curvas de **0,20 m** ($EP \approx 3{,}3\,\mathrm{cm}$; $PEC = 5{,}4\,\mathrm{cm}$, acima de todos os resíduos). Ressalva: 8 checkpoints servem ao controle de rotina; o ASPRS (2023) pede 30 para a avaliação completa. **Altitude:** $H \approx h - N = h + 6{,}10\,\mathrm{m}$ — sem a conversão, o modelo ficaria 6,10 m "abaixo" do projeto. **GCPs e checkpoints:** de 6 a 10 GCPs ao longo do corredor (extremidades, meio dos blocos, borda e fundo da trincheira, para controlar o **efeito de domo** num bloco longo e estreito), algumas fotos oblíquas e **checkpoints independentes**; o RTK reduz os GCPs, mas não dispensa os checkpoints (sincronismo e braço de alavanca). Base RTK com coordenada de vértice, RBMC ou IBGE-PPP.

Efeito do viés na área da trincheira ($A = 380 \times 28 = 10.640\,\mathrm{m^2}$):

$
\delta V \approx A \cdot \delta z = 10.640 \times 0{,}0071 \approx 76\,\mathrm{m^3}
\quad (\approx 0{,}8\%\ \text{de}\ 9.850\,\mathrm{m^3})
$

Desprezível. Boa resposta lembra que, se os dois MDTs tiverem vieses independentes, a incerteza da diferença cresce por $\sqrt{2}$ (Aula 8).

$
I = \frac{9.850}{11.200} \approx 0{,}88
\qquad
V_{solto} = 9.850 \times 1{,}30 = 12.805\,\mathrm{m^3}
\qquad
n = \left\lceil \frac{12.805}{14} \right\rceil = 915\ \text{viagens}
$

O acumulado é $31.400 + 9.850 = 41.250\,\mathrm{m^3}$, ou $41.250/64.000 \approx 64{,}5\%$ do corte; o mês ficou em 88% do 4D, e a causa deve ser investigada (chuva, rebaixamento, restrição de vibração perto da Estação). A medição de pagamento sai do **MDT**, com método contratado: primitivo comum, mesmo referencial, checkpoints, $RMSE_z$ e média informados, data do voo, tolerância e arbitragem.

**Fundo da trincheira** ($T = 5\,\mathrm{cm}$, $U = 3\,\mathrm{cm}$): trecho 1, $2 + 3 = 5 \le 5$ → **conforme**; trecho 2, $6 - 3 = 3 \le 5$ e $6 + 3 = 9 > 5$ → **inconclusivo** (medir de novo, com nivelamento ou estação total); trecho 3, $11 - 3 = 8 > 5$ → **não conforme** (falta escavar; pendência BCF).

**LiDAR e termografia.** Sob mata ciliar densa, a câmera só gera o **MDS**; o **LiDAR** se justifica **apenas na faixa de 2,6 ha**: no resto do corredor, com solo exposto, a fotogrametria é suficiente e mais barata.

$
W = 2 \times 60 \times \tan 35° \approx 84{,}0\,\mathrm{m}
\qquad
\rho \approx \frac{240.000}{6 \times 84{,}0} \approx 476\,\mathrm{pontos/m^2}
\qquad
\rho_{solo} \approx 0{,}10 \times 476 \approx 48\,\mathrm{pontos/m^2} \ge 10
$

Na borda da faixa, $R = 60/\cos 35° \approx 73{,}2\,\mathrm{m}$, e o erro de atitude produz $73{,}2 \times 8{,}73 \times 10^{-4} \approx 0{,}064\,\mathrm{m}$, ou **6,4 cm só pela IMU** — pede trajetória GNSS RTK/PPK de qualidade, sobreposição entre faixas e **checkpoints em clareiras e margens abertas**. O laser passa **pelas frestas**, não através das folhas.

$
IFOV = \frac{12 \times 10^{-6}}{13 \times 10^{-3}} \approx 0{,}923\,\mathrm{mrad}
\qquad
D_{máx} = \frac{0{,}05/3}{0{,}000923} \approx 18{,}1\,\mathrm{m}
$

Voando a **15 m**, o pixel cobre $\approx 13{,}8\,\mathrm{mm}$, e o menor defeito confiável é de cerca de **4,2 cm**. Emissividade ajustada, atenção aos reflexos de vidros e metais, voo com fluxo de calor na fachada (sol ou resfriamento), sem chuva recente nem vento forte. A termografia **localiza** suspeitas, que são confirmadas em campo, e entra na vistoria cautelar antes da obra, com **máscara de privacidade** sobre o edifício vizinho.

**(c) Plano de instrumentação esperado (mínimo aceitável):**

| Grandeza | Instrumento | Local / quantidade | Frequência normal → atenção | Atenção / alerta / alarme |
| --- | --- | --- | --- | --- |
| Deslocamento horizontal | inclinômetros in-place (cadeias MEMS) + prismas no topo | 6 a 8 verticais atrás da cortina, concentradas nas frentes da Estação e do edifício; pé abaixo da zona de influência | 1 h → 15 min | 10 / 14 / 18 mm; 0,5 / 1,0 mm/dia |
| Nível piezométrico | piezômetros de corda vibrante | 4 a 6 atrás da cortina e entre poços | 15 → 5 min | NA a 2,0 / 1,5 / 1,0 m abaixo do fundo |
| Força nas estroncas | extensômetros de corda vibrante com termistor | cerca de 10% das estroncas, por nível | 1 h → 15 min | 70% / 85% / 100% da carga de projeto |
| Recalque — Estação | marcos automatizados (prismas ou células hidrostáticas) + nivelamento de conferência a partir de referência profunda | 8 a 10 pilares e cantos | 1 h → 15 min | 8 / 10 / 12 mm; 0,3 / 0,6 mm/dia |
| Rotação da torre do relógio | clinômetro de parede | 2 eixos na torre | 1 h → 15 min | definidos pelo projetista do restauro |
| Fissuras | fissurômetros elétricos | trincas mapeadas na vistoria cautelar e na termografia | 1 h (tendência) | abertura incremental definida no plano |
| Vibração | acelerômetro triaxial, gravação por evento | fundação da Estação (e do edifício nas fases críticas) | 250–500 Hz por evento | 2,0 / 3,0 / 5,0 mm/s |
| Recalque — edifício | marcos + prismas | 6 pilares | 2 h → 30 min | definidos pelo projetista |
| Temperatura (maturidade) | sensores embutidos | tabuleiro, por etapa de concretagem | 30 min | decisão de protensão ($f_c \ge 25\,\mathrm{MPa}$) |
| Poeira (MP10) | sensor ótico calibrado por colocalização | divisas da Estação e do edifício | 1 min (agregado em 1 h e 24 h) | gatilhos próprios do plano |
| Vento na grua | anemômetro integrado à plataforma | topo da grua | contínuo | alarme a 42 km/h; operação proibida acima de 72 km/h |

Requisitos obrigatórios: **leitura zero** de todos os instrumentos antes de qualquer serviço, repetida 2 ou 3 vezes; **vistoria cautelar** com fotos datadas e termografia; calibração rastreável e ficha de instalação de cada nó.

**Leituras da semana crítica:**

- **I-2 (inclinômetro):**

$
\delta_{topo} = 0{,}5 \times (5{,}0 + 4{,}4 + 3{,}6 + 2{,}4 + 1{,}2 + 0{,}4) \times 10^{-3} = 0{,}5 \times 0{,}017 = 8{,}5\,\mathrm{mm}
$

O perfil, acumulado **de baixo para cima** a partir do pé fixo, passa por 0,2; 0,8; 2,0; 3,8; 6,0 e 8,5 mm. A velocidade é $v = (8{,}5 - 6{,}4)/7 = 0{,}30\,\mathrm{mm/dia}$, e a atenção seria atingida em $(10 - 8{,}5)/0{,}30 = 5{,}0$ dias. Classificação: **verde**, em vigilância.

- **M-3 (recalque):** $x + U = 7{,}5 + 1{,}1 = 8{,}6\,\mathrm{mm}$ alcança a atenção de 8 mm (regra da Aula 13: se $x + U$ alcança o limite, trata-se como atenção). A velocidade é $v = (7{,}5 - 6{,}6)/2 = 0{,}45\,\mathrm{mm/dia}$, acima da atenção (0,3) e abaixo do alerta (0,6). Mantido o ritmo, o alerta por valor chega em $(10 - 7{,}5)/0{,}45 \approx 5{,}6$ dias e o alarme em $(12 - 7{,}5)/0{,}45 = 10$ dias. Classificação: **amarelo**, por incerteza e por velocidade.
- **E-5 (estronca):**

$
\Delta\varepsilon = 390 - 180 = 210\,\mu\varepsilon
\qquad
\sigma = 200.000 \times 210 \times 10^{-6} = 42\,\mathrm{MPa}
\qquad
N = 42 \times 0{,}015 = 0{,}63\,\mathrm{MN} = 630\,\mathrm{kN}
$

São $70\%$ da carga de projeto: **amarelo** (atenção). Sem a correção térmica, a força pareceria de $1.170\,\mathrm{kN}$ (130%), um falso **vermelho**.

- **PZ-2 (piezômetro):** o NA está a 1,6 m do fundo, entre a atenção (2,0 m) e o alerta (1,5 m): **amarelo**. A $0{,}15\,\mathrm{m/h}$, o alerta chega em $(1{,}6 - 1{,}5)/0{,}15 \approx 0{,}7\,\mathrm{h}$ (cerca de 40 min) e o alarme em $(1{,}6 - 1{,}0)/0{,}15 = 4{,}0\,\mathrm{h}$, por volta das 3h. A regra de ligar a bomba reserva ao cruzar o alerta roda **na borda**, sem depender da internet.
- **Vibração:** $2{,}4\,\mathrm{mm/s}$ está entre a atenção (2,0) e o alerta (3,0): **amarelo**. Com componentes até 50 Hz, amostrar de 250 a 500 Hz (Nyquist), gravando por evento.
- **Poeira:** a média de $128\,\mathrm{\mu g/m^3}$ não pode ser lida diretamente, porque o sensor ótico **superestima com umidade alta**; exige calibração por colocalização. O padrão de 100 µg/m³ (MP10, 24 h, CONAMA nº 506/2024) é de **ar ambiente**, não limite de emissão: o plano fixa gatilhos próprios e ações (aspersão, lavagem de rodas). Classificação defensável: **amarelo a confirmar**, com verificação da leitura.

**Leitura integrada esperada.** Três amarelos simultâneos na Estação e na contenção (recalque, vibração e estronca) durante a compactação vibratória **não são coincidência**. Ações esperadas:

- trocar o rolo vibratório por **rolo estático** ou compactação em camadas finas na faixa próxima à Estação e verificar o efeito no acelerômetro e no M-3 (malha fechada);
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

**(d) Plataforma IoT.**

- **Percepção:** sensores de corda vibrante e inclinômetros ligados a **dataloggers profissionais** (interface de frequência, calibração, caixa IP65/IP67, proteção contra surtos); ESP32 só para sensores de baixa criticidade, como poeira e umidade.
- **Rede:** **LoRaWAN** para os nós a bateria, com um gateway no centro do corredor (cerca de 750 m para cada lado, dentro dos 2 a 5 km urbanos), **um segundo gateway para redundância** e backhaul 4G com reserva; câmeras e estação total em 4G/fibra ou Wi-Fi; NB-IoT onde o gateway não alcançar.
- **Plataforma:** broker MQTT, Node-RED e InfluxDB; **aplicação:** Grafana e alertas.
- **Armazenar e reenviar** em todos os nós.

Orçamento de enlace do PZ-2:

$
FSPL = 20\log_{10}(0{,}8) + 20\log_{10}(915) + 32{,}44 \approx -1{,}9 + 59{,}2 + 32{,}4 \approx 89{,}7\,\mathrm{dB}
$

$
P_{rx} = 14 + 2 + 3 - 89{,}7 - 30 \approx -100{,}7\,\mathrm{dBm}
\qquad
\text{margem em SF7} \approx 22\,\mathrm{dB}
$

O enlace fecha com folga em SF7, e o ADR mantém o menor SF (menos tempo no ar e menos energia).

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

Mesmo **inteiramente em atenção**, o nó dura mais que os 26 meses da obra (cerca de 790 dias). Os nós de leitura rápida (acelerômetro, inclinômetros com muitos sensores) precisam de painel solar ou rede.

**MQTT e dados:** tópicos hierárquicos, por exemplo `vv/corredor-leste/trincheira/piezometro/PZ-2/nivel`; QoS 1; **TLS na porta 8883**, credencial por dispositivo e ACL por tópico; mensagem retida para o último estado e último desejo para o nó que cai. No InfluxDB: measurement `piezometro`; tags `obra`, `trecho`, `sensor` (poucos valores); fields `nivel_m`, `bruto_hz`, `bat_v`; carimbo de tempo da medição em UTC; bruto nunca sobrescrito; vibração gravada por evento; agregados no painel.

**(e) Painel, alertas e TARP.**

**TARP esperado (exemplo para a Estação):**

| Nível | Gatilho | Ação | Responsável / prazo |
| --- | --- | --- | --- |
| Verde — normal | todos abaixo da atenção, por valor e velocidade | rotina | equipe de instrumentação |
| Amarelo — atenção | valor, velocidade ou $x + U$ na atenção, com persistência de 2 leituras ou confirmação por 2º instrumento | aumentar a frequência, inspecionar, rever o método (vibração), avisar o projetista e o Conselho | engenheiro da obra, no mesmo dia |
| Laranja — alerta | valor ou velocidade de alerta | preparar e iniciar as medidas previstas (reforço, escoramento da Estação, revisão do rebaixamento), restringir a frente próxima | engenheiro + projetista, em 24 h |
| Vermelho — alarme | alarme confirmado ($x - U$ acima do limite) | paralisar a frente, executar a contingência, isolar a área | responsável técnico + fiscal, imediato; reunião no mesmo dia |

**Automático:** aumentar a frequência, notificar, registrar, ligar a bomba reserva **na borda** (ação reversível, urgente e de baixo risco) e avisar o operador do rolo. **Humano:** paralisar frentes, mudar o método, reforçar a contenção, interditar a Estação ou o edifício. **Regra no Grafana:** consulta agregada, condição por valor e por velocidade, período pendente (persistência), histerese, rótulos de severidade e frente, política de notificação ao ponto de contato do plantão, silenciamentos só com prazo e alerta de **sensor mudo**. Combate à **fadiga de alarmes**: todo alarme exige ação.

**Dashboard:** planta do corredor (ou ortomosaico) com cada instrumento colorido pelo estado; séries com os limites desenhados e a velocidade; linha do tempo de estados; saúde dos sensores (bateria, última leitura, sinal); lista de alarmes com reconhecimento (quem, quando, ação). **Todo alarme com dono.**

**(f) BIM, planejamento e controle.**

$
AF = 0{,}12 \times 0{,}645 + 0{,}18 \times 0{,}85 + 0{,}25 \times 0{,}40 + 0{,}20 \times 0{,}05 + 0{,}25 \times 0 \approx 0{,}340
$

$
VP = 0{,}38 \times 148 \approx 56{,}2
\qquad
VA = 0{,}340 \times 148 \approx 50{,}4
\qquad
CR = 53{,}0 \quad (\mathrm{R\$}\ \text{milhões})
$

$
IDP = \frac{50{,}4}{56{,}2} \approx 0{,}90
\qquad
IDC = \frac{50{,}4}{53{,}0} \approx 0{,}95
\qquad
ENT \approx \frac{148}{0{,}95} \approx 155{,}7\ \text{milhões}
$

A obra está **atrasada** (agregou 90% do planejado) e gasta cerca de 5% acima do que agrega. A terraplenagem usa o avanço medido pelo drone ($64{,}5\%$), o que liga o item (b) ao valor agregado; o 4D mostra que o atraso está na trincheira (88% do mês) e no tabuleiro.

$
d = \sqrt{14^2 + 7^2} = \sqrt{245} \approx 15{,}7\,\mathrm{mm}
\qquad
d - U \approx 10{,}7 < 15
\qquad
d + U \approx 20{,}7 > 15
$

O pilar P4 é **inconclusivo**: nova medição com método mais exato (estação total) antes de abrir não conformidade ou liberar. Pendência **BCF**: elemento (GUID do P4), problema, evidência, responsável (topografia → projetista) e prazo. Os instrumentos são associados aos GUIDs (`IfcSensor`) e os elementos coloridos pelo nível do TARP; nuvens, ortomosaicos e leituras ficam num **CDE** com estados (ISO 19650). O sistema é uma **sombra digital** com o engenheiro fechando a malha; não é gêmeo digital pleno, salvo a regra automática da bomba.

**(g) Segurança do trabalho, LGPD e cibersegurança.**

**NR-18:** a rajada de $12{,}5\,\mathrm{m/s} = 45\,\mathrm{km/h}$ supera 42 km/h: o trabalho da grua passa a exigir análise de risco e permissão de trabalho; acima de 72 km/h (20 m/s), a operação é proibida; o anemômetro, integrado à plataforma, deve alertar a cabine e o encarregado a 42 km/h. Na trincheira: alarme de ré acoplado ao câmbio, rampas sinalizadas, cercas virtuais com UWB **complementando** (não substituindo) a separação de fluxos. No tabuleiro: proteção coletiva contra quedas (guarda-corpo com travessão superior a 1,2 m, intermediário a 0,7 m e rodapé de 0,15 m) e NR-35 acima de 2 m. Drone semanal inspecionando proteções e taludes, com evidência datada para o **PGR**, que deve ser atualizado conforme a etapa.

$
HHT = 320 \times 200 \times 6 = 384.000\,\mathrm{h}
\qquad
TF = \frac{5 \times 10^{6}}{384.000} \approx 13{,}0
$

$
P_{0,5} = \frac{120}{140} \approx 0{,}86
\quad
R_{0,5} = \frac{120}{160} = 0{,}75
\quad
F_{1} \approx 0{,}80
\qquad
P_{0,3} = \frac{148}{212} \approx 0{,}70
\quad
R_{0,3} = \frac{148}{160} \approx 0{,}93
\quad
F_{1} \approx 0{,}80
$

Os F1 são praticamente iguais: a escolha vem do custo de cada erro. Esperado: **limiar 0,3**, porque em segurança o falso negativo (trabalhador sem capacete não detectado) custa mais — caem de 40 para 12, ao custo de mais avisos falsos, revisados pelo encarregado. O detector alerta, **nunca pune automaticamente**, e detecta o **EPI, não a pessoa**.

**LGPD.** A prefeitura é **controladora** e o fornecedor de monitoramento é **operador**. Bases legais típicas: execução de políticas públicas pela administração (art. 7º, III), cumprimento de obrigação legal (normas de segurança) e proteção da vida e da incolumidade física. Inventário de dados pessoais:

- rostos de pedestres e placas de veículos;
- janelas do edifício;
- trabalhadores nas câmeras e nas etiquetas **UWB**;
- registros de acesso à plataforma.

Medidas de minimização e governança:

- polígono de voo e enquadramento restritos à faixa;
- **máscara de privacidade** nas janelas;
- desfoque automático de rostos e placas;
- UWB processado **na borda**, só para proximidade, sem histórico nominal e **sem uso para avaliar desempenho**;
- câmeras **sem reconhecimento facial** (biometria é dado sensível);
- retenção definida e aviso nos acessos e aos moradores;
- RIPD e encarregado definidos; incidentes relevantes comunicados à ANPD e aos titulares em três dias úteis.

**Cibersegurança:** a propriedade mais crítica é a **integridade** das leituras. Controles: trocar a **senha de fábrica do gateway** e todas as credenciais padrão no comissionamento (OWASP IoT Top 10), autenticação forte na plataforma e no Grafana; AES-128 no LoRaWAN e **MQTT sobre TLS** com ACL por tópico; **segmentação** (VLAN dos sensores e câmeras, separada da rede administrativa e de visitantes); inventário e atualização de firmware; logs, cópias de segurança e verificação de lacunas e saltos nas séries; fluxo de resposta a incidente até a comunicação à ANPD.

**Resposta de alta qualidade** demonstra:

- partir dos riscos e terminar em respostas com dono e prazo;
- números corretos e rastreáveis, sobretudo a altura de voo limitada pelo **fundo da trincheira**, os 2 voos com a autonomia reduzida, a decisão de voo pelo vento na altura de voo, o RMSE sem viés, a densidade no solo e a autonomia em atenção;
- leitura **integrada** dos amarelos da Estação e da contenção, com uma ação que fecha a malha;
- uso correto do **TARP de 4 níveis**, por valor e por velocidade, com a regra crítica na borda;
- correção térmica antes de converter deformação em força;
- distinção entre **padrão ambiental e limite do plano** e reconhecimento das limitações do sensor de poeira;
- enquadramento correto da operação (categoria aberta × específica pela proximidade de terceiros, aerolevantamento);
- valor agregado calculado a partir da medição de campo;
- segurança do trabalho e LGPD tratadas como requisitos de projeto, não como anexo.

**Resposta de baixa qualidade** comumente apresenta:

- lista de equipamentos sem riscos, limites nem ações;
- GSD calculado com a altura da decolagem, ignorando o fundo da trincheira;
- um único voo de 1.500 m sem checar bateria nem VLOS, ou vento medido no chão aplicado à altura de voo;
- uso do MDS para volume ou altura elipsoidal comparada ao projeto;
- LiDAR no corredor inteiro sem justificativa;
- TARP de 3 cores ou só por valor, sem velocidade nem responsáveis;
- força na estronca sem correção térmica;
- "categoria aberta" sem considerar pedestres na avenida;
- omissão do aerolevantamento;
- detector de EPI usado para punir ou reconhecimento facial;
- LGPD e cibersegurança reduzidas a uma frase.
