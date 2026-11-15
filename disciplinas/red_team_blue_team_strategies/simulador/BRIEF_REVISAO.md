# Terceira rodada: revisão visual completa e problema mais didático

Pedido do professor: "tem algumas animações e outros elementos sobrepostos... revise 100% das apresentações e
deixe mais didático o problema para os alunos". Vale para TODOS os slides dos seus decks, um por um.

## Parte A: zero sobreposição

1. Rode o auditor nos seus decks (o servidor já roda em http://127.0.0.1:8765 a partir da raiz do repositório):
   `python scripts/auditar_layout.py aulaN ... --shots <pasta no scratchpad>` em **1280x720** e de novo com `--size 1920x1080`.
   Ele ativa cada slide, avança fluxos e terminais até o fim e acusa: conteúdo fora do slide, texto cortado,
   irmãos sobrepostos, rótulos de SVG sobrepostos ou fora da área e conteúdo sob os botões fixos.
   Use `PYTHONIOENCODING=utf-8`.
2. O auditor não enxerga o que está dentro de `<canvas>` (cenas 3D) nem tudo o que é animação. **Abra e olhe
   cada captura** (Read na imagem), inclusive slides de 3D, fluxos no meio da animação e laboratórios depois
   de clicar nos botões. Procure: rótulos 3D sobre rótulos 3D ou saindo do quadro, pacotes ou partículas
   cobrindo texto, legenda sobre a cena, botões encobertos pela navegação (canto inferior direito, ~200x50 px)
   ou pelo botão Início (canto superior direito), texto pequeno demais para projetar (< ~14 px a 1280x720),
   contraste ruim, cartões de alturas desencontradas, espaço vazio enorme.
3. Corrija no deck: posições dos nós dos fluxos (`x`, `y`, `w`), quebre rótulos longos em `label` + `sub`,
   afaste rótulos 3D (posição/escala), reduza texto, divida slide lotado em dois. Falso positivo do auditor
   (ex.: elemento decorativo) pode ficar, mas justifique no relatório.
4. Já corrigido nos assets compartilhados (não refaça no deck): em `Labs.flow`, os pacotes agora passam POR
   BAIXO dos nós, o texto dos nós é centralizado no espaço à direita do ícone e encolhe se não couber, e os
   rótulos das ligações ganharam contorno e se afastam dos nós. No `scene3d`, os botões de controle recebem
   clique real (pode remover o contorno local de `stopPropagation`). Nos slides `.slide-lab`, a barra de
   navegação e o botão Início somem depois de 2,5 s sem mexer o mouse (voltam ao mover), então o canto
   inferior direito do laboratório pode ser usado; nos demais slides, mantenha o canto livre.

## Parte B: o problema da aula, didático

Cada deck passa a ter este arco, igual ao modelo em `unidade_1/slides/aula1.html` (slides 4 e 15):

1. **"O problema de hoje na Rede Tatame"** logo depois do Sumário, substituindo a situação-problema atual
   (layout `.problema`: história à esquerda, mini-mapa à direita). A história tem 3 parágrafos curtos:
   quem é a personagem (da tabela de pessoas de `simulador/APLICACAO.md`), o que aconteceu, o que está em
   jogo. Depois vem o `div.pergunta` (uma pergunta só, que o aluno saiba responder no fim da aula) e o
   `div.papeis` (quem é quem). À direita fica `Labs.miniMapa('#mapa-problema', { destaque, alvo, caminho, legenda })`,
   mostrando onde na plataforma a aula acontece. Os ids são os do simulador (veja o comentário em
   `assets/labs.js`). Se o md da aula traz um caso com outra organização (Pausa para reflexão etc.), ele
   continua no slide próprio dele, sem mudar.
2. **Cada laboratório responde a um pedaço da pergunta.** No painel lateral (`.lab-side`) use o
   `div.roteiro-lab` com blocos `.rl.obj` (Objetivo: que parte do problema este lab resolve), `.rl`
   (Faça: 2–4 passos), `.rl.obs` (Observe: o que olhar no resultado) e `.rl.conc` (Conclusão: uma frase).
   Exemplo:
   `<div class="roteiro-lab"><div class="rl obj"><b>Objetivo</b>...</div><div class="rl"><b>Faça</b>...</div><div class="rl obs"><b>Observe</b>...</div><div class="rl conc"><b>Conclusão</b>...</div></div>`.
   Labs sem painel lateral (fluxo em tela cheia) podem levar o Objetivo no `kicker` ou no primeiro passo.
3. **"De volta ao problema"** antes de Pontos-chave (layout `.resolvido`): 3–4 cartões `.ev`, cada um
   dizendo o que um laboratório provou, e um `div.resposta` com a resposta à pergunta da aula.
4. **Linguagem.** Explique sigla e termo técnico na primeira vez que aparece no deck. Prefira frase curta,
   uma ideia por item. pt-BR, sem estilo de rede social (sem aforismo, sem travessão como conector, sem
   "não é X, é Y").
5. Os números vindos do md continuam iguais.

## Regras

Não edite `assets/`, `simulador/` nem decks de outras unidades; se precisar de algo no componente
compartilhado, descreva no relatório. Não commite. No fim, rode `python scripts/validar_slides.py aulaN...`
e o auditor nos dois tamanhos com 0 ocorrência (ou só falsos positivos justificados). Relatório curto:
o que mudou por deck, ocorrências restantes e o que precisaria mudar nos assets.
