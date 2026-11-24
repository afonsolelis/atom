# TODO — simulador da obra Torre A e roteiros (atualizado em 24/11/2026)

## Concluído

- `simulador/` (9 abas, 7 cenários), `APLICACAO.md` (fonte única de nomes e números) e `aplicacao.html`; visualização `data-viz="plataforma"` em `assets/obra.js`; slide de laboratório em 10 decks (Aula 1: slide 16 · Aula 8: 15 · Aulas 9, 10 e 12: 15 · Aula 11: 14 · Aulas 13 a 16: 17).
- **Passo a passo dos cliques** ("Na tela (passo a passo do que clicar, na ordem):") em todos os slides interativos das 16 videoaulas, em `unidade_N/roteiros_15min.md`, com rótulos e números tirados do HTML dos decks, de `assets/obra.js` e do `simulador.js` (os números dos laboratórios saíram de uma execução do simulador no Node, com a semente fixa).
- **Bloco do laboratório** nas 10 aulas com simulador (passo a passo + fala de 250 a 300 palavras).
- **Renumeração das `[TELA]`** em `roteiros_15min.md` e nos roteiros sintéticos de `unidade_N.md` (as 4 aulas da U1 estavam com numeração antiga e foram corrigidas).
- Falas ajustadas onde contradiziam a tela (ex.: Aula 4, slide 17 — o vento só cai abaixo do limite a 40 m; Aula 14, slide 10 — o atraso do BIM 4D é máximo na semana 32). Decks corrigidos: painel da Aula 14 (semana 22 até a 32) e calculadora de autonomia da Aula 10 (capacidade mínima 100 mAh, para mostrar os 500 mAh do protótipo).
- Todas as aulas entre ~2.160 e ~2.540 palavras faladas (alvo 17–19 min). `tools/validar.py 1`…`4`: sem erros.
- `unidade_N/unidade_N_roteiro.md` (arquivos de gravação) e `entrega_docx/` regerados.

## Conferir antes de gravar

- Os passos "Na tela" foram conferidos pelo código, não na tela. Na passagem do roteiro, abrir cada deck no Chrome e seguir o passo a passo (`python3 -m http.server 5601` nesta pasta e `http://127.0.0.1:5601/unidade_4/slides/aula13.html#17`, por exemplo). O Live Server na porta 5500 aponta para a pasta de Red Team, não para esta.
- Aulas no limite de duração: Aula 2 (perto do piso) e Aulas 9 a 13 (perto do teto de 2.550 palavras).
