# Processamento distribuído, edge e serverless — Unidade 4, Aula 15

## O incidente que esta aula corrige

Até a Aula 14, a NexaOrder não tinha nenhum mecanismo de detecção de fraude — nem em
lote, nem em fluxo. A situação-problema do roteiro é exatamente essa lacuna: um job
horário chegaria tarde demais, porque uma hora é suficiente para dezenas de
tentativas fraudulentas serem aprovadas antes de qualquer relatório existir. A
decisão precisa sair em segundos, no momento da tentativa — o que desloca todo o
paradigma de processamento.

## Lote e fluxo: a decisão é de negócio, não de engenharia

A escolha entre os dois não é uma questão técnica — é sobre até quando uma
informação pode esperar antes de perder valor. Um relatório de comissões pode
esperar o fechamento do mês; um padrão de fraude perde quase todo o valor em
minutos. Este projeto agora tem os dois lados, lado a lado:

- **Lote** — `scripts/mapreduce.py`: map/shuffle/reduce sobre um conjunto fechado e
  conhecido (o histórico completo de tentativas por dispositivo).
- **Fluxo** — `services/pedidos/app/janela_evento.py` +
  `services/pedidos/app/eventos_dispositivo.py`: a mesma pergunta ("quantas
  tentativas este dispositivo fez"), respondida continuamente para os últimos 60
  segundos, sem esperar um job terminar.

## MapReduce e tolerância a falhas

`scripts/mapreduce.py` implementa as três fases sobre dados em memória: map
transforma cada registro independentemente (paraleliza perfeitamente), shuffle
redistribui por chave, reduce agrupa e combina. `fase_map_tolerante_a_falhas` prova o
princípio de reconciliação do roteiro — se uma tarefa falha, só ela é reexecutada,
não o job inteiro (`test_map_tolerante_a_falhas_reexecuta_so_a_tarefa_que_falhou`
prova que a tarefa estável nunca é tocada de novo) — o mesmo espírito da
reconciliação de Pods da Aula 11, aplicado a tarefas de processamento.

## O dimensionamento de partições, de novo

`services/pedidos/app/eventos_dispositivo.py` reaproveita `Topico`/`escolher_particao`
da Aula 10, com uma chave de partição diferente: `dispositivo_id`, não `pedido_id`.
A fórmula é a mesma (`⌈taxa/capacidade⌉`), agora com os números do roteiro: pico de
5.000 tentativas/s, capacidade de 750/s por partição → 7 partições no mínimo
(`test_numero_minimo_de_particoes_do_exemplo_da_aula_15`). A garantia que importa —
todos os eventos de um mesmo dispositivo chegam em ordem à mesma partição — é
provada em `test_tentativas_de_dispositivos_diferentes_preservam_ordem_por_dispositivo`.

## Tempo de evento vs. tempo de processamento: a demonstração central

`services/pedidos/app/janela_evento.py` reproduz o exemplo exato do roteiro: dez
tentativas em dez segundos no mesmo dispositivo, mas a rede atrasa cinco delas em
dois minutos.

- Por **tempo de evento**: as dez são reconhecidas como um único padrão — a janela
  agrupa pelo instante em que o fato ocorreu, não por quando chegou.
- Por **tempo de processamento**: aparecem dois grupos de cinco, em momentos
  diferentes — o alerta nunca dispara, porque nenhuma janela individual vê as dez
  juntas.

`test_janela_por_tempo_de_evento_agrupa_mesmo_com_atraso_de_rede` prova as duas
leituras lado a lado, com os mesmos dados.

## Marcas d'água: o compromisso entre completude e atraso

`avancar_marca_dagua` implementa a estimativa "até que ponto, no tempo de evento, o
pipeline já recebeu a maior parte dos dados" — `tempo_processamento_atual -
tolerancia_atraso`. `test_tolerancia_maior_mantem_a_janela_aberta_por_mais_tempo`
prova o compromisso em números: tolerância curta fecha a janela cedo (arriscando
subestimar, perdendo eventos tardios); tolerância longa mantém a janela aberta por
mais tempo (arriscando atrasar uma decisão que, no caso da fraude, se torna inútil se
atrasada).

## Inicialização a frio: onde ela importa

`services/pedidos/app/faas.py` simula o efeito observável do cold start — não a
plataforma. `test_cold_start_no_caminho_sincrono_estoura_o_sli_de_latencia_da_aula_13`
é o argumento do roteiro, quantificado: o custo de inicialização a frio (400ms)
sozinho já ultrapassa o limite de 300ms do exemplo de SLI de latência da Aula 13 — se
`avaliar_risco_no_checkout` fosse uma função fria no caminho síncrono da compra, ela
comprometeria o próprio orçamento de erro que a Aula 13 introduziu. Em contraste,
`test_cold_start_fora_do_caminho_sincrono_e_imperceptivel` prova que o mesmo custo,
fora do caminho síncrono (o envio assíncrono de confirmação por e-mail), não importa.

## Borda: a resposta madura à pausa de reflexão

`services/pedidos/app/triagem_de_fraude.py` implementa a resposta que o roteiro
constrói contra a proposta de "processar tudo na borda": `triagem_local` decide só
com sinais simples e disponíveis localmente (múltiplos cartões testados na mesma
sessão); `avaliacao_central` usa contexto histórico agregado — a contagem da janela
por tempo de evento — que nenhum ponto de borda isolado possui sozinho. Não é tudo em
um lugar; é triagem local para o simples, avaliação central para o que exige
histórico.

## O que a escala horizontal faz com esta janela

Tudo acima é verdadeiro em um processo. `docs/kubernetes-execucao.md` registra o mesmo
pipeline com `pedidos` em quatro réplicas dentro de um cluster kind, e o resultado
merece estar aqui: doze tentativas do mesmo dispositivo, distribuídas pelas quatro
réplicas por um `Service` comum, produzem **três em cada uma** — e um alerta com
limiar de dez nunca dispara.

O detalhe que importa é que as quatro réplicas calcularam a **mesma partição** para a
mesma chave. `escolher_particao` está certo; o que não existe é alguém obrigando o
evento a chegar ao dono daquela partição. Particionar por chave e rotear por partição
são coisas diferentes, e um framework de fluxo real entrega as duas — é isso, e não a
lógica de janela, que o ADR 0015 registra como ausente.

## Decisão registrada

Ver `docs/adr/0015-fraude-simulada-sem-plataforma-real.md`.
