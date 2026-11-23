# TODO — simulador da obra Torre A e roteiros (parado em 23/11/2026)

## Já feito (commitado)

- `simulador/` novo: `index.html`, `simulador.css`, `simulador.js` (9 abas com balões de explicação: Canteiro, Leituras, Rede LoRaWAN, MQTT, Séries temporais, Alarmes, Cenários, Drone e BIM, Segurança e LGPD; 7 cenários), `APLICACAO.md` (fonte única de nomes e números) e `aplicacao.html` (a especificação formatada).
- `assets/obra.js`: nova visualização `data-viz="plataforma"` (iframe do simulador, com aba, cenário e regras configurados pelo `data-opts`). `assets/obra.css`: estilos `.viz-plat`, `.slide-plat` e `.roteiro-lab`.
- Slide de laboratório com o simulador inserido em 10 decks (testados no Chrome, sem erro de JS):
  - Aula 1: slide 16 · Aula 8: slide 15 · Aulas 9, 10 e 12: slide 15 · Aula 11: slide 14 · Aulas 13 a 16: slide 17.
  - **Os slides seguintes de cada um desses decks andaram uma posição.**
- Portal `index.html`: cartões "Simulador" e "Especificação". `README.md`: linha `simulador/` na estrutura.

## Parcial (commitado como está, precisa terminar)

- `unidade_1/roteiros_15min.md` e `unidade_2/roteiros_15min.md`: os agentes começaram a pôr o "Na tela (passo a passo do que clicar, na ordem):" nos slides interativos e foram interrompidos no meio. Revisar o diff desses dois arquivos (`git show HEAD -- '*roteiros_15min.md'`) antes de continuar.
- Unidades 3 e 4: nada foi editado nos roteiros ainda.

## Falta fazer

1. **Passo a passo dos cliques** em `unidade_N/roteiros_15min.md` (Unidades 1 a 4): para cada slide interativo (sliders, botões, calculadoras `calc`, cenas 3D e o laboratório do simulador), incluir um bloco "Na tela (passo a passo do que clicar, na ordem):" com os rótulos exatos dos controles, no formato de `disciplinas/red_team_blue_team_strategies/unidade_1/unidade_1.md`.
2. **Bloco novo do slide de laboratório** em cada uma das 10 aulas, nos `roteiros_15min.md`: `**[TELA]** Slide N`, passos com os rótulos reais do simulador e fala de 200 a 300 palavras com os números da `simulador/APLICACAO.md`. O painel "Faça / Observe" de cada slide já diz o que fazer.
3. **Renumerar as referências `[TELA]`** depois do slide inserido nessas 10 aulas, em `roteiros_15min.md` **e** nos roteiros sintéticos dentro de `unidade_N/unidade_N.md` (linhas `**[TELA]** Slides X–Y`), acrescentando o laboratório numa frase curta.
4. Rodar `python3 tools/validar.py 1` … `4`.
5. Regerar os arquivos de gravação `unidade_N/unidade_N_roteiro.md`. Eles são cópia de `roteiros_15min.md` + o roteiro do vídeo introdutório (na U1). O script usado está descrito no commit `29e1e0a`: título próprio + nota de origem + "Como usar" + (U1) o roteiro do vídeo introdutório de `unidade_1.md` + o corpo de `roteiros_15min.md` a partir do primeiro `## Roteiro`.
6. Regerar os DOCX (`python3 tools/gerar_docx.py`), porque `unidade_N.md` vai mudar no passo 3.
7. Commit e push na `main`.

## Para testar o simulador em casa

- `python3 -m http.server 5601` na pasta da disciplina e abrir `http://127.0.0.1:5601/simulador/index.html` (ou um deck, por exemplo `unidade_4/slides/aula13.html#17`).
- O Live Server na porta 5500 aponta para a pasta de Red Team, não para esta.
