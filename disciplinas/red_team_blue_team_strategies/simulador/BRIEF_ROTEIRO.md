# Quarta etapa: roteiros das videoaulas alinhados aos decks

Pedido do professor: "não se esqueça de atualizar o roteiro caso seja necessário, e aproveite e revise o
roteiro para explicar bem a parte prática de cada slide".

Os roteiros ficam em `unidade_N/unidade_N.md`, na seção `### Roteiro da Videoaula K — "título"` de cada aula.
Hoje eles têm 5 ou 6 tópicos curtos e ainda citam casos de antes da Rede Tatame. Reescreva cada roteiro para
seguir o deck HTML **na ordem dos slides**, de modo que o professor consiga gravar com o deck aberto.

## Formato (mantenha o título `### Roteiro da Videoaula K — "..."`; pode ajustar o título entre aspas)

Uma linha de abertura: `Duração-alvo: 15 a 20 minutos. Deck: unidade_N/slides/aulaK.html (X slides).`
Depois, um bloco por slide ou grupo de slides, na ordem do deck:

```
**Slide 4 — O problema de hoje na Rede Tatame (1:00–2:30)**
Fala: "..." (texto corrido para o professor dizer, 2 a 5 frases, dialógico, em primeira pessoa)
```

Nos **slides de laboratório**, o bloco é mais detalhado e é a parte mais importante do roteiro:

```
**Slide 9 — Laboratório: o analista de SOC investiga o exercício (6:10–8:30)**
Objetivo: que parte da pergunta da aula este laboratório responde.
Na tela (passo a passo do que clicar/digitar, na ordem):
1. Clicar na busca salva "1. Quem recebeu?" ...
2. ...
Fala: o que explicar enquanto clica, incluindo como ler o resultado (o que é cada coluna, número,
alerta, linha do código ou saída do terminal que aparece) e o que o aluno deve perceber.
Atenção: o que pode confundir, o que é simulado ou ilustrativo, ou de quanto tempo a animação precisa.
Conclusão: a frase que liga o resultado à pergunta da aula.
```

- Nos laboratórios de VS Code, explique o código: o que cada bloco faz, qual linha decide o resultado e
  por que a saída deu aquele número. Nos de terminal, o que cada comando faz e como ler a saída. Nos de SIEM,
  o que a consulta filtra. Nos fluxos e cenas 3D, o que cada passo ou botão mostra. Nos slides da plataforma
  Rede Tatame, o roteiro "Faça" passo a passo dentro do simulador: aba, botão, o que muda e onde olhar. Inclua
  quando trocar a velocidade, reiniciar ou repetir o cenário.
- Os passos devem bater **exatamente** com o que o deck mostra (rótulos de botões, nomes de buscas, arquivos,
  números). Confira no deck; se rodou o laboratório na rodada anterior, use o resultado real.
- Slides de capa, audiodescrição e referências podem ficar num bloco curto ou ser omitidos. O slide
  "O problema de hoje" abre com o gancho; o "De volta ao problema" fecha respondendo à pergunta da aula;
  a Aula 4 de cada unidade (exceto a 16) termina chamando a próxima unidade, como o template exige.
- Indicações de produção continuam entre colchetes, no padrão do template (ex.:
  `[Take de apoio: ... — Envato]`, `[Tela: gravação do laboratório do slide 9]`). Indique gravação de tela
  para todo laboratório.
- Tempos aproximados e crescentes, total entre 15 e 20 minutos.
- Linguagem: pt-BR acadêmica, clara e dialógica; termos estrangeiros em itálico; sem estilo de rede social
  (sem aforismo, sem travessão como conector, sem "não é X, é Y"). Não mude números do texto base.
- Altere **só** os roteiros das suas aulas no `unidade_N.md` (e, na Unidade 1, ajuste no vídeo introdutório
  apenas o necessário para citar a plataforma Rede Tatame, mantendo o limite de 2 minutos). Não mexa em texto
  base, questões, quiz, AAI ou material complementar.
- Rode `python scripts/validar.py` no fim (deve continuar passando para a sua unidade) e informe no relatório
  quantos minutos e quantas palavras cada roteiro ficou.
