# Entrega de Trabalho (PBL) — Indústria 4.0 e Digitalização de Processos

> Roteiro para elaboração com **Problem-Based Learning**.

- **Disciplina:** Indústria 4.0 e Digitalização de Processos
- **Professor-conteudista:** Afonso Cesar Lelis Brandão

> O **CASE** existe para que o estudante entenda a aplicabilidade do conteúdo estudado na realidade do mercado de trabalho.

---

## 1. Título

**Roadmap de Transformação Digital da Metalúrgica Sigma — De Reativos para Preditivos em 18 Meses**

---

## 2. Desafio

> **O quê?** Uma metalúrgica brasileira de médio porte precisa estruturar sua **primeira iniciativa séria de Indústria 4.0**.
>
> **Quem?** A **Metalúrgica Sigma**, fabricante de componentes estruturais para o setor automotivo, sediada em Sorocaba (SP), com 620 funcionários e faturamento anual de R\$ 280 milhões.
>
> **Quando?** A diretoria definiu que o projeto **deve iniciar no próximo trimestre**, com primeiros resultados mensuráveis em **6 meses** e roadmap completo de **18 meses**.
>
> **Onde?** Operação concentrada em uma planta única em Sorocaba (SP), com 4 linhas de produção, 180 máquinas de chão de fábrica (CNCs, prensas, fornos de tratamento térmico), 3 robôs industriais tradicionais, sistemas ERP (TOTVS) e MES (próprio, com 12 anos de uso).
>
> **Por quê?** A Sigma vem perdendo competitividade. **Indicadores atuais**:
>
> - **Paradas não programadas**: 145 horas/mês (aumento de 40% em 3 anos).
> - **OEE médio**: 67% (concorrentes maduros: 82-85%).
> - **Custo de manutenção**: 8,5% da receita (referência setorial: 4-5%).
> - **Defeitos por milhão (DPPM)**: 3.800 (concorrentes: < 1.500).
> - **Lead time** médio do pedido: 28 dias (concorrentes: 18 dias).
>
> A Sigma **não tem sensoriamento massivo** em chão de fábrica, **não tem dashboards em tempo real**, **decide manutenção por intuição** do supervisor, e nunca implementou IA. Sistemas TI e OT são **desconectados**. Cultura organizacional é **conservadora** — operadores experientes (média de 18 anos de casa) resistem a mudanças tecnológicas, e a TI corporativa nunca se envolveu com chão de fábrica.
>
> A diretoria definiu **investimento máximo** de **R\$ 3 milhões** em 18 meses para todo o programa, com fortes incentivos para resultados mensuráveis.
>
> **Sua missão como engenheiro(a) de produção:** estruturar um **roadmap completo e defensável** de transformação digital da Sigma, considerando o contexto, as restrições e as oportunidades reais. Você precisa entregar um plano que a diretoria possa **aprovar e executar**, não uma proposta genérica.

---

## 3. Fontes de pesquisa

O estudante deverá pesquisar como outros profissionais ou empresas resolveram desafios similares. Indicações:

**Fontes de pesquisa primária:**

1. **Material da disciplina** — todas as 16 aulas, com ênfase nas Unidades 2 (tecnologias habilitadoras), 3 (aplicações) e 4 (implementação, roadmap, casos reais).
2. **Portal Indústria 4.0 CNI** — https://www.portaldaindustria.com.br/industria-4-0/ (relatórios, diagnósticos, casos brasileiros documentados).
3. **Acatech Industrie 4.0 Maturity Index** — https://www.acatech.de/ (modelo de maturidade aplicável ao diagnóstico inicial).
4. **Senai SP — Casos de Indústria 4.0** — https://www.sp.senai.br/ (referência brasileira, casos de PME e médio porte).
5. **Caso Klabin** — artigo "Klabin moderniza indústria 4.0" (revista Exame, Valor Econômico ou similar) — exemplo de IIoT em setor tradicional.
6. **Caso Embraco** — case Universal Robots Brasil (cobots em compressor).
7. **McKinsey — Industry 4.0 implementation** — https://www.mckinsey.com/ (roadmap, fatores críticos de sucesso, taxa de falha).

**Aulas relacionadas:** todas as 16 aulas são insumo. Em ordem de relevância: Aula 4 (maturidade), Aula 13 (BPM), Aula 14 (roadmap), Aula 15 (casos), Aulas 5-8 (tecnologias).

---

## 4. Entregável e distribuição da pontuação

**Formato da entrega:** **Documento técnico** em PDF (entre 12 e 18 páginas) + **apresentação executiva** em slides (entre 10 e 15 slides) para defender perante banca simulada (diretoria fictícia).

**Pontuação:**

- **25%** — **Diagnóstico de maturidade**: análise da Sigma com fatos verificáveis, classificação Acatech, identificação de gargalos.
- **20%** — **Definição da dor prioritária** e justificativa de escolha (impacto financeiro, viabilidade, aderência ao porte e contexto).
- **20%** — **Solução técnica**: tecnologias escolhidas, arquitetura, integração com sistemas existentes, especificação de equipamentos.
- **20%** — **Plano em 18 meses**: 5 fases com prazos, orçamento detalhado por fase, KPIs e governança.
- **15%** — **Riscos, mitigações e visão I5.0**: análise crítica de obstáculos, plano de mitigação e visão de longo prazo (3-5 anos).

**Critérios qualitativos transversais** (afetam todas as notas):

- **Clareza** e organização do texto.
- **Profundidade técnica** demonstrada (não generalidades).
- **Realismo** dos números (custos, prazos, ROI).
- **Coerência interna** (recomendação alinhada ao plano, ao orçamento, aos KPIs).
- **Integração** dos conceitos das 16 aulas.

---

## 5. Solução

> **Atenção:** este tópico será removido antes do case ser disponibilizado ao aluno — é apenas para o professor tutor que corrigirá.

**Diagnóstico esperado:** Sigma está em **nível 2 (Conectividade) baixo** ou **nível 1 (Computadorização) alto** no modelo Acatech. Tem ERP e MES, mas sem integração, sem sensoriamento em campo, sem dashboards em tempo real, sem cultura de dado. O grande gap está em **subir para nível 3 (Visibilidade)** primeiro.

**Dor prioritária esperada:** **manutenção corretiva de máquinas críticas**, com custo anual estimado de R\$ 17 milhões em paradas não programadas (145 h/mês × 12 × R\$ 10.000/h aproximado). Atacar essa dor primeiro tem **3 vantagens**: (a) dor financeira clara e mensurável; (b) ROI rápido tipicamente em 6-12 meses; (c) demonstra valor rapidamente, gerando tração interna.

**Solução técnica esperada:**

- **Tecnologia primária:** **IIoT** com sensores em 30-40 motores críticos (vibração, temperatura, corrente) → gateway edge → plataforma simples na nuvem (AWS IoT Core ou Azure IoT Hub) → dashboards em Power BI / Grafana.
- **Tecnologia secundária (a partir da fase 3):** **ML preditivo** para manutenção (Random Forest treinado em dados históricos + sinais coletados pelos sensores).
- **Integração:** API leve entre nova plataforma de IIoT e MES existente (não substituir o MES nesse momento — coexistir).
- **Cibersegurança:** segmentação básica de rede (OT segregada da TI corporativa via firewall), inventário de ativos, plano básico de resposta a incidentes.

**Plano em 18 meses esperado:**

| Fase | Prazo | Investimento | Foco |
| --- | --- | --- | --- |
| Diagnóstico estruturado | M1–M3 | R\$ 150 mil | Acatech + mapa de processos críticos + mobilização patrocinador |
| Piloto IIoT em 5-10 motores | M3–M6 | R\$ 400 mil | Sensores + dashboards + treinamento equipe piloto |
| Expansão para 30-40 motores | M6–M12 | R\$ 800 mil | Padronização, governança, integração com MES |
| ML preditivo + cibersegurança básica | M12–M18 | R\$ 1,2 milhão | Modelo preditivo treinado e em produção; segmentação de rede |
| **Total 18 meses** | | **~R\$ 2,55 milhões** | **Dentro do orçamento de R\$ 3 mi** |

**KPIs esperados:**

1. **Paradas não programadas** — alvo: -30% em 12 meses (de 145 h/mês para ~100 h/mês).
2. **OEE médio** — alvo: subir de 67% para 75% em 18 meses.
3. **Custo de manutenção** — alvo: cair de 8,5% para 7% da receita em 18 meses.
4. **MTBF** dos motores críticos — alvo: dobrar.
5. **Nível Acatech** — alvo: subir de 2 para 3-4 em 18 meses.

**Governança esperada:** comitê mensal com diretoria, equipe multidisciplinar (TI + manutenção + produção + finanças), ritual de acompanhamento de KPIs, comunicação interna constante.

**Riscos esperados (com mitigações):**

1. **Resistência cultural dos operadores experientes** — mitigação: envolver desde o piloto, criar embaixadores entre os mais influentes, mostrar que não vão perder emprego e sim ganhar ferramenta.
2. **Falta de patrocínio executivo persistente** — mitigação: ritual mensal com diretoria, mostrar resultado parcial a cada 3 meses, vincular KPIs do projeto a OKRs da diretoria.
3. **Dependência de fornecedor único** — mitigação: escolher plataforma com padrões abertos (MQTT, OPC UA), evitar lock-in com fornecedor proprietário fechado.
4. **Cibersegurança subestimada** — mitigação: incluir segmentação básica e plano de resposta já na fase 4; contratar consultoria especializada para validação.
5. **Subestimar capacitação** — mitigação: dedicar 15-20% do orçamento a treinamento contínuo (operadores, supervisores, equipe de manutenção).

**Visão I5.0 (3-5 anos) esperada:**

- Migração para arquitetura com digital twin operacional completo.
- Indicadores de pegada de carbono por peça produzida.
- Cobots em estações de inspeção e embalagem.
- Cultura de dado consolidada (decisão baseada em evidência, não intuição).
- Programa de requalificação interna para acompanhar evolução tecnológica.
- Posicionamento ESG como diferencial competitivo na cadeia automotiva.

**Resposta de alta qualidade** demonstra: (1) compreensão profunda do contexto Sigma (não solução genérica); (2) número realista em todos os pontos; (3) coerência entre diagnóstico, dor, solução, plano e KPIs; (4) integração de conceitos das 16 aulas (não tratamento superficial de tecnologias da moda); (5) tratamento sério dos riscos culturais e organizacionais, não apenas técnicos.

**Resposta de baixa qualidade** comumente apresenta: (a) "vamos colocar IA" sem detalhar problema; (b) orçamento fora da realidade (R\$ 50 mil ou R\$ 50 milhões); (c) atacar várias frentes de uma vez (todas as 9 tecnologias); (d) ignorar resistência cultural; (e) não conectar com KPIs mensuráveis; (f) não mencionar cibersegurança.

---

## Roteiro do Estudante

### 1. Leia o desafio

Sua primeira tarefa é entender o desafio proposto. Queremos que você compreenda e explore a situação da Metalúrgica Sigma a fundo. Muita atenção para não perder o foco durante o estudo. Você precisa compreender:

- **Quem** é a Sigma (porte, setor, contexto, cultura)?
- **Qual** é a dor financeira mais clara?
- **Quais** restrições foram colocadas (orçamento R\$ 3 mi, prazo 18 meses, equipe interna existente)?
- **Onde** a empresa está hoje em maturidade digital?

### 2. Fontes de Pesquisa

Este é o momento de pesquisar o que já existe no mercado e ler todas as indicações que o professor fez. Antes de propor uma solução, reúna ferramentas e referências:

- **Releia** as Unidades 2 (tecnologias), 3 (aplicações), 4 (implementação) — são suas fontes primárias.
- **Estude** os casos brasileiros documentados (Klabin, WEG, Embraco) — são exemplos de empresas com contexto parecido com o da Sigma.
- **Aprofunde** o modelo Acatech de maturidade — você precisará classificar a Sigma com fundamento.
- **Pesquise** preços de mercado: quanto custa um sensor IIoT industrial? Quanto custa licença de plataforma? Quanto cobra um integrador? Isso ancora os números do seu plano.

Não esqueça de trazer um **exemplo concreto** de empresa que resolveu problema similar.

### 3. Entrega

Agora é o momento de se tornar um(a) solucionador(a) de problemas. Com base no que você pesquisou, analisou e desenvolveu, **estruture o documento técnico e a apresentação executiva**.

Recomendação de estrutura para o **documento técnico (PDF, 12-18 páginas)**:

1. **Capa e sumário executivo** (1 página) — 5 linhas com a recomendação central.
2. **Diagnóstico de maturidade** (2-3 páginas) — Acatech, processos críticos, gargalos.
3. **Dor prioritária e justificativa** (1-2 páginas) — qual problema, por quê, impacto financeiro.
4. **Solução técnica** (2-3 páginas) — tecnologias, arquitetura, integração.
5. **Plano em 18 meses** (2-3 páginas) — 5 fases, orçamento, KPIs.
6. **Governança** (1 página) — comitê, ritmos, papéis.
7. **Riscos e mitigações** (1-2 páginas) — 3-5 riscos com plano concreto.
8. **Visão I5.0** (1 página) — onde a Sigma estará em 5 anos.
9. **Referências** — fontes consultadas, ABNT.

Para a **apresentação executiva (10-15 slides)**:

- 1 slide com **a recomendação central**.
- 2 slides com diagnóstico.
- 1 slide com a dor escolhida.
- 2 slides com solução.
- 3 slides com plano e KPIs.
- 1 slide com riscos.
- 1 slide com I5.0.
- 1 slide com pedido de aprovação e próximos passos.

**Dica final:** capriche na **defesa numérica**. Diretoria não compra ideia bonita — compra plano com **números defensáveis**. Cada decisão sua deve estar ancorada em fato (de mercado ou da empresa), não em opinião.

Boa entrega!
