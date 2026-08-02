# Registro de recursos visuais

> **Escopo deste registro:** o inventário e o QA descrevem os 17 protótipos HTML de slides e, desde a revisão da Unidade 1, as 13 figuras embutidas no material escrito. Os resultados não comprovam, por si só, a acessibilidade do PDF/PPTX nem a aprovação do formato pelo NEaD. A conferência deverá ser repetida no artefato final exportado.

## Licença e autoria

Os diagramas, mapas conceituais, cartões comparativos, demonstrações numéricas e sínteses visuais dos decks HTML foram elaborados especificamente para a disciplina por Afonso Cesar Lelis Brandão. Esses recursos autorais são oferecidos sob a licença [Creative Commons Atribuição 4.0 Internacional (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.pt_BR), com atribuição ao autor e à disciplina *Distributed Systems Engineering*.

A identidade visual, o nome e a marca UniFECAF permanecem sujeitos às regras institucionais de uso e não são abrangidos pela CC BY 4.0.

A fotografia do professor, copiada em `unidade_1/slides/assets/foto-professor.jpg`, `unidade_2/slides/assets/foto-professor.jpg`, `unidade_3/slides/assets/foto-professor.jpg` e `unidade_4/slides/assets/foto-professor.jpg`, pertence ao acervo pessoal do professor. Ela não está licenciada em CC BY 4.0. O texto alternativo foi conferido e as quatro cópias são idênticas byte a byte. Antes da entrega, ainda se deve arquivar a autorização formal de uso institucional.

Não há, no inventário declarado, fotografias, vídeos, áudios ou ilustrações de terceiros incorporados aos decks. Caso a equipe de edição inclua ou substitua algum recurso por mídia externa, deverá registrar neste arquivo a URL, autoria, licença, data de acesso, aula, ponto de inserção e trecho utilizado.

## Critério de acessibilidade

Cada deck declara exatamente cinco recursos visuais didáticos implementados em HTML/CSS, atendendo ao intervalo institucional de 3 a 5 recursos por aula. Na introdução, são quatro diagramas autorais e a fotografia do professor; nos demais decks, são cinco infográficos autorais. Os elementos didáticos possuem semântica de figura, descrição acessível, autoria e licença registradas. Texto, formas e relações não dependem exclusivamente de cor. Elementos puramente decorativos não são contabilizados.

Esses atributos foram conferidos nos 17 HTMLs. Na conversão para PDF ou PPTX, deve-se testar novamente ordem de leitura, contraste, ampliação, descrições alternativas e preservação dos créditos, porque metadados ARIA podem não sobreviver à exportação.

## Inventário por aula

| Deck | Recursos visuais didáticos principais |
|---|---|
| Introdução | retrato do professor; panorama profissional dos sistemas distribuídos; minibiografia; percurso em quatro unidades; trilha de aprendizagem com NexaOrder e avaliações |
| Aula 1 | mapa de componentes autônomos; quadro de motivações; mapa de propriedades; painel de métricas; comparação de estilos arquiteturais |
| Aula 2 | comparação síncrono/assíncrono; mapa HTTP; contrato RPC; evolução de esquema; topologia fila/publicação–assinatura |
| Aula 3 | linha temporal distribuída; cálculo de desvio; mapa *happened-before*; sequência Lamport; comparação vetorial |
| Aula 4 | taxonomia de falhas; mapa de particionamento; decisão de limite de tempo; estados do *circuit breaker*; isolamento por *bulkhead* |
| Aula 5 | objetivos da replicação; comparação líder/múltiplos líderes; linha de atraso; quadro de consistências; garantias por cliente |
| Aula 6 | estratégias de partição; anel de *hashing*; mapa de rebalanceamento; triângulo CAP; quadro PACELC |
| Aula 7 | problema do consenso; mapa de maioria; estados do Raft; fluxo de eleição; sequência de replicação do registro |
| Aula 8 | comparação transação local/distribuída; fluxo 2PC; mapa de saga; fluxo de compensação; cadeia *outbox/inbox* |
| Aula 9 | comparação monólito/microsserviços; mapa de coesão; contextos delimitados; dados por serviço; fluxo do *gateway* |
| Aula 10 | taxonomia evento/comando; topologia de tópicos; mapa de partições; grupos de consumidores; quadro de semânticas de entrega |
| Aula 11 | comparação contêiner/máquina virtual; estrutura de imagem; mapa de objetos Kubernetes; laço de reconciliação; fluxo de implantação |
| Aula 12 | mapa de confiança zero; matriz autenticação/autorização; fluxo mTLS; topologia de *service mesh*; balde de fichas |
| Aula 13 | comparação monitoramento/observabilidade; mapa dos três pilares; propagação de *trace ID*; painel SLI/SLO; orçamento de erro |
| Aula 14 | pirâmide de testes; matriz carga/estresse/duração; ciclo de experimento de caos; mapa de raio de impacto; disponibilidade combinada |
| Aula 15 | comparação lote/fluxo; DAG de processamento; cálculo de partições; linha de tempo de evento; quadro de borda/funções como serviço |
| Aula 16 | matriz requisito/atributo; ciclo ADR/evidência; mapa de pontos únicos de falha; painel RPO/RTO; comparação redundância paralela/sequencial |

## Forma de atribuição

Ao exportar ou reutilizar os infográficos fora destes decks, usar: “Elaboração própria: Afonso Cesar Lelis Brandão, *Distributed Systems Engineering*, 2026. CC BY 4.0.”

## Figuras do material escrito (DOCX)

O modelo oficial exige de 3 a 5 imagens, gráficos ou organogramas por aula, com licença compatível, origem registrada, descrição alternativa e indicação no ponto exato do texto. Até a revisão da Unidade 1, o material escrito trazia apenas descrições em bloco (“Recurso visual N”) dirigidas à equipe de edição — ou seja, a exigência não estava atendida no artefato entregue.

Na **Unidade 1**, essas descrições foram substituídas por 13 figuras autorais. Cada uma existe em dois formatos, em `unidade_1/assets/figuras/`: o **SVG**, que é a fonte editável, e o **PNG** em dobro da escala, que é o formato aceito pelo DOCX. Ambos são gerados por `scripts/figuras_unidade1.py` a partir das primitivas de `scripts/figuras_kit.py`, de modo que qualquer ajuste se faz no código e não no binário.

As **Unidades 2, 3 e 4 seguem com os blocos descritivos** e ainda precisam do mesmo tratamento para atender ao intervalo de 3 a 5 imagens por aula.

### Licença e autoria das figuras

As 13 figuras são elaboração própria de Afonso Cesar Lelis Brandão, sem material de terceiros incorporado, e são oferecidas sob [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.pt_BR). A legenda de cada figura no DOCX registra título, crédito, licença e texto alternativo; o texto alternativo também é gravado na propriedade de acessibilidade da imagem (`docPr/@descr`) e no elemento `<desc>` do SVG.

### Inventário da Unidade 1

| Figura | Aula | Arquivo (`unidade_1/assets/figuras/`) | Conteúdo |
|---|---|---|---|
| 1 | 1 | `figura-01-arquitetura-nexaorder` | cliente, gateway e os quatro serviços autônomos |
| 2 | 1 | `figura-02-falha-ambigua` | linha do tempo da cobrança processada com resposta perdida |
| 3 | 1 | `figura-03-carga-latencia` | curva carga × latência com o ponto de saturação |
| 4 | 1 | `figura-04-estilos-arquiteturais` | cliente-servidor, camadas, peer-to-peer e serviços |
| 5 | 2 | `figura-05-fluxo-http-sincrono` | diagrama de sequência do encadeamento bloqueante |
| 6 | 2 | `figura-06-fila-pub-sub` | fila ponto a ponto versus publicação-assinatura |
| 7 | 2 | `figura-07-dois-fluxos-pedido` | cadeia síncrona versus cadeia orientada a eventos |
| 8 | 3 | `figura-08-relogios-lamport` | raias com os relógios lógicos e o empate sem causalidade |
| 9 | 3 | `figura-09-vetores-concorrentes` | comparação posição a posição de (2,3,0) e (2,1,2) |
| 10 | 3 | `figura-10-ordem-parcial-total` | grafo de ordem parcial ao lado da ordem total imposta |
| 11 | 4 | `figura-11-particionamento-rede` | duas zonas operantes com a comunicação rompida |
| 12 | 4 | `figura-12-circuit-breaker` | máquina de estados do disjuntor e suas transições |
| 13 | 4 | `figura-13-bulkhead` | compartimentos de conexões isolados por dependência |

Distribuição por aula: 4 figuras na Aula 1, 3 na Aula 2, 3 na Aula 3 e 3 na Aula 4 — dentro do intervalo institucional de 3 a 5.

### QA das figuras da Unidade 1

- [x] Conferir que as 13 figuras foram embutidas no DOCX, com 5,7 polegadas de largura e centralizadas.
- [x] Conferir texto alternativo em `docPr/@descr` nas 13 figuras e legenda com crédito e licença logo abaixo de cada uma.
- [x] Conferir que os SVG e os PNG estão versionados e que o gerador reproduz ambos.
- [x] Conferir leitura sem dependência exclusiva de cor: todo par contrastado também traz rótulo, símbolo ou traçado próprio.
- [ ] Conferir a renderização das figuras no Word do NEaD, incluindo a leitura do texto alternativo por leitor de tela.
- [ ] Produzir as figuras das Unidades 2, 3 e 4, hoje ainda descritas em bloco.

## QA dos protótipos HTML

- [x] Confirmar exatamente cinco recursos didáticos por deck: quatro diagramas e uma foto na introdução; cinco diagramas em cada Videoaula 1 a 16.
- [x] Conferir semântica de figura, descrições acessíveis, autoria e licença de cada recurso.
- [x] Verificar identificadores, links, ARIA e SVG nos 17 decks.
- [x] Validar contraste responsivo e leitura sem dependência exclusiva de cor.
- [x] Exercitar 1.608 estados de slide/aba e 30 estados com reflexões expandidas em seis dimensões de viewport, sem falhas, erros JavaScript ou *overflow* não rolável.
- [x] Conferir o texto alternativo da fotografia e confirmar que suas quatro cópias são byte a byte idênticas.
- [ ] Arquivar a autorização formal de uso institucional da fotografia do professor.
- [ ] Repetir a auditoria de acessibilidade e créditos no formato institucional aprovado.
