# Drones e Sensores IoT no Monitoramento de Obras

- **Professor-conteudista:** Afonso Cesar Lelis Brandão
- **Layout:** Átomo 3.0 (mesmo padrão de `disciplinas/portos_aeroportos_e_ferrovias/`)
- **Escopo de commit:** `drones_iot`
- **Status:** disciplina completa sobre o plano proposto — Unidades 1–4 (texto, roteiros, questões, decks aula0–aula16), portal `index.html` e instrumentos avaliativos (avaliação final e PBL). Pendentes: reconciliar com o material da coordenação (ementa, plano de aprendizagem, contrato, prazos) e preencher "Direto da fonte" quando houver acesso à Biblioteca Virtual.

## Estrutura

```
unidade_N/unidade_N.md        texto base + roteiros (10 min) + quiz + AAI + material complementar
unidade_N/roteiros_15min.md    roteiros estendidos (15–20 min) das 4 videoaulas
unidade_N/questoes_uniN.md     20 questões (10 AR + 10 interpretação) + feedbacks
unidade_N/slides/aulaN.html    decks UniFECAF (aula0 + aula1–aula16, numeração contínua)
assets/                        deck.css, deck.js, sprite.js (padrão UniFECAF) + obra.css/obra.js (fotos, 3D, simulações) — ver assets/README_DECKS.md
tools/                         wikimedia.py (fotos), capturar_slides.py (PNG por slide; rodar com `uv run --with playwright python …`), validar.py N (checagem estrutural)
instrumentos_avaliativos/      avaliacao_final.md (30 objetivas + 10 discursivas) + entrega_trabalho.md (PBL)
```

## Plano de aulas (PROPOSTA — substituir pela ementa oficial quando chegar)

### Unidade 1 — Fundamentos do Monitoramento Digital de Obras

1. Monitoramento de obras na era digital: do diário de obra ao canteiro conectado
2. Fundamentos de sensoriamento: grandezas, transdutores, incerteza e calibração
3. Arquiteturas IoT para o canteiro: dispositivos, conectividade e nuvem
4. Drones (RPA): tipos, componentes, cargas úteis e regulamentação brasileira

### Unidade 2 — Drones: Aquisição e Processamento de Dados

5. Planejamento de voo: GSD, sobreposição, altura e plano de missão
6. Fotogrametria com drones: SfM, pontos de controle, RTK/PPK e precisão
7. Produtos cartográficos: ortomosaico, MDS/MDT, nuvem de pontos e cálculo de volumes
8. LiDAR embarcado e termografia na inspeção de estruturas e fachadas

### Unidade 3 — Sensores IoT no Monitoramento de Obras

9. Monitoramento geotécnico: inclinômetros, piezômetros e marcos de recalque
10. Monitoramento estrutural: extensômetros, acelerômetros, fissurômetros e maturidade do concreto
11. Segurança, ambiente e produtividade: vibração, ruído, poeira e rastreamento de equipamentos
12. Dados de sensores: séries temporais, níveis de alerta e dashboards

### Unidade 4 — Integração, Inteligência e Gestão do Monitoramento

13. Integração com BIM e gêmeo digital: 4D e comparação as-built × as-designed
14. IA e visão computacional: detecção de fissuras e medição de avanço físico
15. Gestão do monitoramento: custo-benefício, LGPD, segurança da informação e contratos
16. Projeto integrado de monitoramento de uma obra (fechamento da disciplina)

## Pendências

- [ ] Receber ementa / plano de aprendizagem e reconciliar com a proposta acima
- [ ] Confirmar se o contrato segue o Átomo 3.0 padrão (20 questões/unidade, 40 na avaliação final) ou a variante TECH (40 questões/unidade, 10 discursivas)
- [ ] Confirmar duração das videoaulas (10 min + roteiro estendido de 15–20 min, como em Portos)
- [ ] Prazos de entrega
- [ ] Bibliografia da Biblioteca Virtual disponível para a disciplina
- [ ] Seção "Direto da fonte" (livro da BV) de cada unidade — aguardando acesso
- [x] Decks aula0–aula16 e `index.html` do portal
- [x] Unidades 2–4 e instrumentos avaliativos (`avaliacao_final.md`, `entrega_trabalho.md`)

## Referências normativas a considerar (validar na produção)

- ANAC — RBAC nº 100 (Resolução nº 805/2026, substituiu o RBAC-E nº 94; categorias aberta/específica/certificada) e cadastro SISANT
- DECEA — ICA 100-40, edição 2026 (acesso ao espaço aéreo por aeronaves não tripuladas) e sistema SARPAS
- ANATEL — homologação de radiotransmissores (drones e dispositivos IoT)
- ABNT NBR 9653 (vibrações por desmonte de rocha), NBR 16747 (inspeção predial)
- LGPD (Lei 13.709/2018) — imagens e dados de trabalhadores e vizinhança
