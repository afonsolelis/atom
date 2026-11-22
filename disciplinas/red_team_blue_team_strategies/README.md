# Red Team & Blue Team Strategies

Produção de conteúdo EAD do NEaD (UniFECAF), formato **Átomo 3.0 TECH**.

- Professor-conteudista: Afonso Cesar Lelis Brandão
- Coordenação do curso: Osvaldo (envia o plano de aprendizagem)
- Acompanhamento da produção: Carolina Bastos
- Videoaulas e gravação: Maico Pereira Gomes
- Convite recebido em: 13/11/2026

## Situação em 22/11/2026

Todo o material está **alinhado à ementa oficial** enviada pela coordenação (Osvaldo) em 18/11/2026 e transcrita em [`EMENTA.md`](EMENTA.md). A proposta provisória de 13/11 foi substituída: as 4 unidades e as 16 aulas seguem, tópico por tópico, o roteiro de aprendizagem oficial, e as tecnologias sugeridas (Kali Linux, Metasploit, ATT&CK Navigator, Wazuh/Security Onion e Wireshark) entram como laboratórios simulados nas aulas indicadas na ementa.

- 4 unidades completas (16 aulas com texto base, 16 roteiros de videoaula que seguem o deck slide a slide, roteiro do vídeo introdutório, 4 quizzes, AAI, 16 materiais complementares);
- 160 questões (40 por unidade, 8 corretas por letra, feedback para cada alternativa);
- trabalho PBL (caso Vitalis Diagnósticos, com solução e rubrica para o tutor), alinhado ao ciclo da ementa;
- avaliação final com 10 discursivas (2 a 3 por unidade), respostas esperadas e critérios de correção;
- 17 decks HTML com laboratórios, VS Code em tela cheia em todas as aulas.

Os IDs do MITRE ATT&CK seguem a versão atual (v19 em diante), em que a antiga *Defense Evasion* foi dividida em *Stealth* (TA0005) e *Defense Impairment* (TA0112).

`python scripts/validar.py` confere as regras dos templates (estrutura, 700–1200 palavras e 3–5 imagens por aula, seções obrigatórias, formato e distribuição das questões, pesos do PBL). Os DOCX preenchidos são gerados por `python scripts/gerar_docx.py` (em `entregas_docx/`, fora do git), a partir dos modelos de `documentos/`, e foram reenviados ao Drive em 22/11/2026, substituindo os de 15/11. Nada foi validado pela coordenação ainda.

Os slides das 16 aulas e da apresentação estão em HTML, com laboratórios embutidos (ver [Slides HTML e laboratórios](#slides-html-e-laboratórios)). O portal da disciplina é o [`index.html`](index.html).

## Fonte de verdade: o Google Drive

**A fonte de verdade é a pasta do Drive da disciplina.** Este repositório guarda uma cópia de referência dos originais e as versões de trabalho em Markdown. Se houver divergência, vale o Drive.

- Pasta da disciplina: <https://drive.google.com/drive/u/0/folders/1t_CUMJS3H7wPo1wuFsKeVcpONcBLDZi6>
- Subpasta com os modelos ("Originais - Átomo 3.0 TECH"): <https://drive.google.com/drive/u/0/folders/18ItL3UkX2TxeQjvREsos758z_g4ztDaE>

Permissões em 13/11/2026: os modelos estão **somente leitura** para o conteudista (`canEdit: false`), mas as pastas aceitam **novos arquivos** (`canAddChildren: true`). As entregas preenchidas devem, portanto, ser enviadas como arquivos novos ao lado dos modelos, a menos que o NEaD conceda permissão de edição.

## Escopo do pacote

- 4 templates de unidade (4 aulas cada);
- 160 questões, sendo 40 por unidade (20 asserção-razão + 20 interpretação);
- 1 vídeo introdutório (até 2 min);
- 16 videoaulas, 4 por unidade, numeradas de forma contínua (U1 = 1–4, U2 = 5–8, U3 = 9–12, U4 = 13–16);
- 1 trabalho (estudo de caso PBL);
- 1 avaliação final com 10 questões discursivas.

## Cronograma de entregas

| Entrega | Prazo |
|---|---|
| Unidade 1 — template + 40 questões | 02/12/2026 |
| Vídeo introdutório + Videoaulas 1 a 4 | 02/12/2026 |
| Instrumentos avaliativos — Trabalho | 02/12/2026 |
| Unidade 2 — template + 40 questões | 02/12/2026 |
| Videoaulas 5 a 8 | 02/12/2026 |
| Unidade 3 — template + 40 questões | 20/12/2026 |
| Videoaulas 9 a 12 | 20/12/2026 |
| Unidade 4 — template + 40 questões | 20/12/2026 |
| Videoaulas 13 a 16 | 20/12/2026 |
| Instrumentos avaliativos — Avaliação final (10 discursivas) | 20/12/2026 |

Todas as entregas passam pela validação da coordenação, que pode pedir ajustes.

## Ementa

Ementa oficial em [`EMENTA.md`](EMENTA.md): ementa, objetivos, competências, habilidades, atitudes, roteiro de aprendizagem, tecnologias sugeridas e bibliografia, como enviados pela coordenação em 18/11/2026, mais o mapa das 16 aulas. `simulador/BRIEF_REALINHAMENTO.md` registra como o material da proposta antiga foi redistribuído.

## Index dos documentos

### Arquivos de trabalho (Markdown, versionados)

| Arquivo | Conteúdo | Modelo do Drive correspondente |
|---|---|---|
| [`EMENTA.md`](EMENTA.md) | Ementa oficial, objetivos, competências, mapa das 16 aulas, tecnologias, bibliografia | Ementa enviada pela coordenação (Google Docs, 18/11/2026) |
| [`unidade_1/unidade_1.md`](unidade_1/unidade_1.md) | Relação com a atuação profissional, roteiro do vídeo introdutório, Aulas 1–4 (texto base + roteiro), quiz, AAI, material complementar | `Unidade 1/TEMPLATE - Unidade 1_nome da disciplina.docx` |
| [`unidade_1/questoes_uni1.md`](unidade_1/questoes_uni1.md) | 40 questões + feedback por alternativa | `Unidade 1/40 Questões - UNI1_nomedadisciplina.docx` |
| [`unidade_2/unidade_2.md`](unidade_2/unidade_2.md) | Aulas 5–8, quiz, material complementar | `Unidade 2/TEMPLATE - Unidade 2_nome da disciplina.docx` ⚠️ |
| [`unidade_2/questoes_uni2.md`](unidade_2/questoes_uni2.md) | 40 questões + feedbacks | `Unidade 2/40 Questões - UNI2_nomedadisciplina.docx` |
| [`unidade_3/unidade_3.md`](unidade_3/unidade_3.md) | Aulas 9–12, quiz, material complementar | `Unidade 3/TEMPLATE - Unidade 3_nome da disciplina.docx` |
| [`unidade_3/questoes_uni3.md`](unidade_3/questoes_uni3.md) | 40 questões + feedbacks | `Unidade 3/40 Questões - UNI3_nomedadisciplina.docx` |
| [`unidade_4/unidade_4.md`](unidade_4/unidade_4.md) | Aulas 13–16, quiz, material complementar | `Unidade 4/TEMPLATE - Unidade 4_nome da disciplina.docx` |
| [`unidade_4/questoes_uni4.md`](unidade_4/questoes_uni4.md) | 40 questões + feedbacks | `Unidade 4/40 Questões - UNI4_nomedadisciplina.docx` |
| [`instrumentos_avaliativos/entrega_trabalho.md`](instrumentos_avaliativos/entrega_trabalho.md) | Estudo de caso PBL (título, desafio, fontes, entregável, solução) | `Instrumentos Avaliativos/TEMPLATE ENTREGA DE TRABALHO - nomedadisciplina.docx` |
| [`instrumentos_avaliativos/avaliacao_final.md`](instrumentos_avaliativos/avaliacao_final.md) | 10 discursivas + respostas esperadas | `Instrumentos Avaliativos/Avaliação final_(10 discursivas)_nomedadisciplina.docx` |
| [`index.html`](index.html) e `unidade_N/slides/aula0..16.html` | Portal e 17 decks HTML com laboratórios embutidos | `Unidade N/SLIDES - Videoaula N.pptx` (formato a confirmar) |

### Originais do Drive (`documentos/`, fora do git)

`documentos/` espelha a árvore do Drive. Os binários não são versionados (são grandes e o template de unidade contém credenciais da Biblioteca Virtual); só [`documentos/MANIFESTO_SHA256.md`](documentos/MANIFESTO_SHA256.md) entra no git, com tamanho, hash e ID do Drive de cada arquivo. Os originais não devem ser editados.

```text
documentos/
├── MANIFESTO_SHA256.md
├── Unidade 1/
│   ├── TEMPLATE - Unidade 1_nome da disciplina.docx
│   ├── 40 Questões - UNI1_nomedadisciplina.docx
│   ├── SLIDES - Videoaula 1.pptx … SLIDES - Videoaula 4.pptx
│   └── Videoaula_ Introdutória + 1 a 4/
│       ├── Videoaulas Introdutória + 1 a 4 - Validação.docx
│       └── Guia - Como Fazer um Bom Vídeo.pdf          (pendente, ver abaixo)
├── Unidade 2/   (TEMPLATE, 40 Questões, SLIDES 5–8, Videoaulas 5 a 8/)
├── Unidade 3/   (TEMPLATE, 40 Questões, SLIDES 9–12, Videoaula 9 a 12/)
├── Unidade 4/   (TEMPLATE, 40 Questões, SLIDES 13–16, Videoaula 13 a 16/)
└── Instrumentos Avaliativos/
    ├── Avaliação final_(10 discursivas)_nomedadisciplina.docx
    └── TEMPLATE ENTREGA DE TRABALHO - nomedadisciplina.docx
```

O Drive tem 34 arquivos (14 DOCX, 16 PPTX, 4 PDF); 30 estão em `documentos/`. Os 4 PDFs do guia de vídeo (29 MB cada, mesmo tamanho nas quatro pastas) passam do limite de 10 MB do conector e precisam ser baixados manualmente. Para recriar `documentos/` em outro clone, baixe a pasta "Originais - Átomo 3.0 TECH" do Drive e confira com o manifesto.

## Regras de produção (extraídas dos modelos do Drive)

### Template de unidade

- **Somente Unidade 1:** texto "Relação da disciplina com a atuação profissional" + roteiro do **vídeo introdutório (até 2 min)** — abertura, conexão com o mercado, conteúdo e diferencial, benefícios, chamada para ação.
- **Cada aula:** texto base + roteiro da videoaula com título que gere curiosidade. Texto com a teoria; vídeo com aplicação prática, exemplos e casos reais, sem redundância.
- **Aula 1 de cada unidade:** "O que você verá nesta unidade" (conteúdo, objetivo, justificativa).
- **Aula 3:** "Pausa para reflexão" ou "Desafio" (estudo de caso ou exercício prático).
- **Aula 4:** "O que você verá na próxima unidade". O template da Unidade 4 repete essa orientação; na última unidade, tratar como fechamento da disciplina (confirmar com o NEaD).
- **3 a 5 imagens, gráficos ou organogramas por aula**, indicados entre colchetes, com texto alternativo, sem restrição de direitos autorais (domínio público / Creative Commons). Imagens do **Envato** podem ser indicadas por link; a equipe baixa a versão paga.
- Linguagem acadêmica, clara e dialógica; Times New Roman 12, entrelinha 1,15, alinhado à esquerda; termos estrangeiros em itálico.
- Referências em **ABNT NBR 6023:2018**; similaridade máxima de **3% no CopySpider**; citação direta entre aspas, indireta por paráfrase.
- **Quiz não avaliativo:** 2 questões (V/F e/ou múltipla escolha), nível intermediário, com feedback que explica o conceito.
- **AAI** (1 dissertativa + resposta esperada): presente **só no template da Unidade 1**.
- **Material complementar** (obrigatório, conta na carga horária; nada pago), indicando a aula de cada um:
  - *Direto da fonte* — livro da Biblioteca Virtual (acesso "BV professor" pelo Brightspace; credenciais no template);
  - *Para mergulhar no assunto* — filme, série, vídeo gratuito, blog, livro ou visita;
  - *Podcast* — até 45 min, de preferência no Spotify, ou vídeo em formato de podcast;
  - *Artigo científico* — link + referência ABNT.

### Questões (40 por unidade)

- Padrão ENADE: **20 asserção-razão + 20 interpretação**; podem ser adaptadas de provas do ENADE.
- 5 alternativas (a–e), correta marcada com `*` antes da letra.
- **Feedback para cada alternativa** (correta: reforça o conceito; incorreta: explica o equívoco), todos ao final do documento.
- Remover os exemplos do template antes de entregar.

### Trabalho (PBL)

Título; Desafio (contexto pelo lide — o quê, quem, quando, onde, por quê — e problema central realista com várias soluções possíveis); Fonte de pesquisa (≥ 4 fontes primárias + aulas relacionadas); Entregável e distribuição da pontuação em %; Solução (removida antes de ir ao aluno, vai para o tutor).

### Avaliação final

10 questões **discursivas** no estilo ENADE, com o feedback (resposta esperada) ao final.

### Slides e videoaulas

- Um PPTX por videoaula (`SLIDES - Videoaula N.pptx`), no padrão UniFECAF: capa, **audiodescrição** do professor (nos decks HTML, só na apresentação da disciplina, `aula0`), "Sobre o professor", sumário, slides de conteúdo e imagem, citação, encerramento.
- Os slides servem para **sinalizar a edição** à equipe de produção: frases, imagens, takes e trechos exatos de vídeos do Envato, com os links.
- Gravação obrigatória no **estúdio** ou nos laboratórios da faculdade; em casa, só com autorização e aula-teste aprovada. A modalidade deve ser confirmada até 2 dias úteis após o convite.
- Cada bloco de videoaulas tem uma ficha de validação (coordenador + videomaker) na subpasta da unidade.

## Slides HTML e laboratórios

Os decks ficam em `unidade_N/slides/aulaK.html` (`aula0` é a apresentação da disciplina; a numeração das aulas é contínua, como a das videoaulas) e são abertos pelo portal [`index.html`](index.html). Em cada aula, os slides de conceito são seguidos por slides de laboratório que demonstram o conceito dentro do próprio slide, no padrão do simulador da Aula 06 do repositório `aulas_mackenzie`.

### A plataforma Rede Tatame

Todas as aulas usam a mesma aplicação fictícia como alvo do Red Team e ambiente defendido pelo Blue Team: a plataforma distribuída da **Rede Tatame**, uma rede de academias de jiu-jitsu (o mesmo cenário da demonstração da palestra da Alliance e do simulador da Aula 06 do `aulas_mackenzie`). Ela tem app do aluno, portal das academias e catracas com leitor facial, CDN/WAF, API gateway, microsserviços, Kafka com três tópicos, motor de CEP, data lake, SIEM/SOC e a rede da sede (AD, servidores, notebooks com EDR, VPN e e-mail).

| Arquivo | Papel |
|---|---|
| [`simulador/APLICACAO.md`](simulador/APLICACAO.md) | fonte única de nomes, hosts, endereços, pessoas, adversário emulado (Grupo Cobalto Austral), regras do CEP (R1–R13) e cenários |
| [`simulador/index.html`](simulador/index.html) | simulador no navegador, com 9 abas: arquitetura animada, requisições do gateway, filas e eventos (partições e *lag*), telemetria (fontes e custo), regras do CEP (R1–R13), cenários, SOC (investigar, conter, MTTD/MTTR), superfície externa (CVSS, EPSS, KEV) e cobertura ATT&CK |
| `simulador/BRIEF_DECKS.md` | mapa de qual aba e cenário cada aula usa |

Seis cenários atravessam o semestre: `phishing`, `recon`, `api-abuso`, `ransomware`, `catraca` e `exfiltracao`. Cada passo tem técnica ATT&CK, fonte de telemetria e regra; se a fonte estiver ligada e a regra ativa, nasce um alerta no SOC, senão o passo passa despercebido. Os slides embutem o simulador com `Labs.plataforma('#id', { aba, cenario, regras, fontes })`; um único *iframe* por deck é movido de slide em slide, então o estado continua entre os laboratórios da mesma aula.

### Arquivos compartilhados

Diferente das outras disciplinas do repositório, os decks não são arquivos únicos: compartilham os arquivos de `assets/`.

| Arquivo | Papel |
|---|---|
| `assets/deck.css` | padrão visual UniFECAF (extraído dos decks já migrados) |
| `assets/sprite.js` | logo e triângulos do padrão, injetados como símbolos SVG |
| `assets/deck.js` | navegação (setas, Page Up/Down, Home/End, F para tela cheia, `#N` na URL) e eventos `slide:enter`/`slide:leave` |
| `assets/labs.css`, `assets/labs.js` | laboratórios: `Labs.vscode` (editor com explorador, realce de sintaxe, digitação ao vivo e terminal integrado), `Labs.terminal` (tela preta roteirizada, Linux ou PowerShell), `Labs.siem` (buscas salvas, histograma e resultados), `Labs.browser` (página simulada), `Labs.flow` (arquitetura animada por etapas), `Labs.scene3d` (three.js r128 via cdnjs) e `Labs.register` (simulações próprias de cada aula) e `Labs.plataforma` (o simulador da Rede Tatame embutido) |
| `assets/foto-professor.jpg` | foto do slide "Sobre o professor" |
| `assets/favicon.svg`, `assets/favicon.png` | ícone da disciplina (escudo vermelho, roxo e azul), injetado pelo `deck.js` em todas as aulas e referenciado no portal e no simulador |

**VS Code em tela cheia e preparação do ambiente.** Todo slide com `Labs.vscode` ocupa o slide inteiro, como se o editor estivesse aberto no computador do professor. O roteiro do laboratório (Objetivo, Faça, Observe, Conclusão) fica escondido e abre como painel sobreposto pelo botão "☰ Roteiro" da barra de status ou pela tecla **G**. Antes de executar o código, o botão "⬇ Preparar o ambiente" roda no terminal a sequência de `setup` do laboratório (versão do interpretador, ambiente virtual, `pip install -r requirements.txt`, conferência), com pacotes e versões reais do PyPI. Imediatamente antes de cada laboratório de VS Code há um slide "Antes do código: onde achar e como instalar o que o laboratório usa", com a fonte oficial de cada programa e pacote e como conferir que é o pacote certo. O modelo é o `unidade_1/slides/aula1.html`.

Os laboratórios só iniciam quando o slide é aberto e pausam ao sair dele. Tudo é simulado no navegador: a Rede Tatame, as pessoas, domínios e endereços são fictícios, e o conteúdo ofensivo fica no nível conceitual, sem código de exploração, *payloads* ou técnicas de evasão. As cenas 3D precisam de internet para carregar o three.js.

Cada aula segue o mesmo arco didático:

1. **O problema de hoje na Rede Tatame**, logo após o sumário. Uma história curta com uma personagem da plataforma, a pergunta da aula em destaque, quem é quem e um mini-mapa (`Labs.miniMapa`) mostrando onde, na arquitetura, o problema acontece.
2. **Laboratórios**, cada um respondendo a um pedaço da pergunta. O painel lateral traz Objetivo, Faça, Observe e Conclusão.
3. **De volta ao problema**, antes dos pontos-chave. Mostra o que cada laboratório provou e responde à pergunta da aula.

Os roteiros das videoaulas (`unidade_N.md`) seguem o deck slide a slide, com duração-alvo de 15 a 20 minutos. Cada laboratório traz Objetivo, os passos "Na tela", a fala que explica como ler o resultado, Atenção e Conclusão.

O layout foi desenhado para 1280x720. Em telas maiores, o `deck.js` aumenta a fonte-base na mesma proporção, e os componentes medidos em px (VS Code, terminal, SIEM, navegador) recebem `zoom`. Nos slides de laboratório, a barra de navegação some depois de 2,5 s sem movimento do mouse.

`python scripts/auditar_layout.py [aulaN ...] [--size 1920x1080] [--shots pasta]` precisa do servidor local rodando. Ele passa por todos os slides, avança fluxos e terminais e acusa conteúdo fora do slide, texto cortado, elementos ou rótulos SVG sobrepostos e conteúdo sob a navegação.

`python scripts/validar_slides.py` confere cada deck: estrutura (capa, audiodescrição do professor só na `aula0`, encerramento, assets), pelo menos 4 laboratórios com VS Code, um laboratório na plataforma Rede Tatame, uma simulação de programa e uma visualização animada ou 3D, alvos dos laboratórios existentes, sintaxe dos scripts (`node --check`) e ausência de comandos ofensivos operacionais. A Aula 1 é o deck de referência.

Para ver localmente com as cenas 3D e os caminhos relativos funcionando, sirva a raiz do repositório: `python -m http.server 8765` e abra `http://127.0.0.1:8765/disciplinas/red_team_blue_team_strategies/`.

## Pendências

1. ~~Receber o plano de aprendizagem e ajustar o material~~ — ementa oficial recebida em 18/11/2026 e aplicada em 22/11/2026 (unidades, questões, decks, roteiros, PBL, avaliação final, DOCX e Drive).
2. **Template da Unidade 2:** o arquivo `TEMPLATE - Unidade 2_nome da disciplina.docx` do Drive contém internamente a Unidade 1. O `gerar_docx.py` corrige cabeçalho e plano de ensino na cópia; confirmar com o NEaD se isso basta.
3. Baixar manualmente os 4 PDFs `Guia - Como Fazer um Bom Vídeo.pdf`.
4. Confirmar a modalidade de gravação (estúdio ou casa) com a Carolina.
5. Contrato: cadastro no Banco de Talentos (link no e-mail do convite).
6. Confirmar com o NEaD se os decks HTML substituem os PPTX `SLIDES - Videoaula N.pptx` do Drive ou se é preciso preencher também os PPTX para a equipe de edição.
7. Antes de gravar, abrir cada deck num navegador comum (as cenas 3D dependem de WebGL e de internet para o three.js).
8. **Prazo de comunicação à ANPD (Aula 13):** o laboratório conta três dias úteis a partir do dia útil seguinte à ciência do incidente (Res. CD/ANPD nº 15/2024); confirmar a regra de contagem e os feriados locais com o jurídico.
9. Prazos de entrega: U1, U2 e trabalho até 02/12/2026; U3, U4 e avaliação final até 20/12/2026.
