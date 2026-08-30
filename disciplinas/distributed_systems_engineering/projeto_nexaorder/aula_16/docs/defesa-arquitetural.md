# Defesa arquitetural da NexaOrder — Unidade 4, Aula 16

Esta aula não acrescenta mecanismo novo — reúne o que as quinze aulas anteriores
construíram em uma defesa coerente, no formato que o roteiro propõe: uma reunião de
diretoria, não um incidente. Três perguntas orientam o documento: por que esta
arquitetura sustenta o crescimento previsto, por que resiste às falhas mais
prováveis, e por que justifica o investimento contínuo que exige.

## 1. Requisitos funcionais x atributos de qualidade: a tensão resolvida por dado

Requisitos funcionais definem o que o sistema faz; atributos de qualidade definem
como ele se comporta. Não há hierarquia entre eles — um checkout que finaliza compras
em quarenta segundos cumpre o requisito funcional e, ainda assim, falha por completo.

A NexaOrder resolveu essa tensão desde a Aula 5, não em bloco: o catálogo aceita
leitura eventualmente consistente (`services/estoque/app/replica.py`,
`GET /saldo/{sku}?consistencia=eventual`); a reserva de estoque exige consistência
forte no instante da escrita (`ArmazenLider.reservar`, a mesma rota sempre lê do
líder). Ver `docs/consistencia-por-dado.md`. A decisão é por dado, não por sistema
inteiro — exatamente o raciocínio que esta aula pede para generalizar.

## 2. O mesmo cálculo, insumos que deixaram de ser suposição

`docs/dimensionamento.md` (Aula 1) previa `N = 6` instâncias a partir de três
suposições: 800 req/s de pico (projeção de negócio), 200 req/s de capacidade
(teste de carga preliminar isolado) e 70% de utilização-alvo (convenção).

`scripts/dimensionamento_com_evidencias.py` reproduz a mesma fórmula como regressão
exata daquele cálculo. `services/pedidos/tests/test_dimensionamento_com_evidencias.py`
vai além: mede a capacidade ao vivo, batendo em `POST /pedidos` de verdade nesta
própria suíte, e alimenta o mesmo cálculo com um número medido, não suposto. A
fórmula não mudou; a qualidade do insumo, sim.

## 3. Registros de decisão arquitetural

Este projeto acumulou 15 ADRs (`docs/adr/0001` a `0015`), cada um seguindo o mesmo
formato que o roteiro exige de um ADR completo: contexto, decisão, por quê,
compromisso aceito, evidência. Nenhum registra só um nome de tecnologia — cada um
registra o problema que motivou a escolha e o preço que ela cobra. A retrospectiva:

| Unidade | Decisão central | Compromisso aceito |
|---|---|---|
| 1 | Distribuir em serviços sem estado, comunicação síncrona inicial (ADR 0001, 0002, 0003) | Timeout, retry e disjuntor tornam-se obrigatórios, não opcionais (ADR 0004) |
| 2 | Consistência por dado, não por sistema (ADR 0005); particionamento e consenso simulados (ADR 0006, 0007); saga orquestrada (ADR 0008) | Duas políticas de consistência convivendo — a equipe precisa saber qual vale onde; consenso e particionamento reais exigiriam um cluster que este projeto não tem |
| 3 | Gateway sem lógica de negócio (ADR 0009); barramento de eventos em memória (ADR 0010) | Composição explícita no lugar de JOIN; nenhum broker real integrado — o limite é documentado, não escondido |
| 4 | Manifests validados sem cluster (ADR 0011); identidade por HMAC, não mTLS (ADR 0012); spans locais sem coletor central (ADR 0013); testes de contrato sem broker (ADR 0014); fraude simulada sem plataforma real (ADR 0015) | Custo contínuo de telemetria e de experimentos controlados; HMAC com segredo compartilhado é mais fraco que PKI real |

A coluna da direita é o que sustenta a defesa: uma arquitetura defensável não é
isenta de custo — é aquela cujos custos foram escolhidos conscientemente e estão
registrados. **Cada decisão arquitetural deve ser tratada como hipótese verificável,
não como dogma** — e cada ADR deste projeto, ao declarar sua própria "compromisso
aceito", já é essa hipótese por escrito.

## 4. Análise de pontos únicos de falha (SPOF)

Percorrendo a NexaOrder sob a lente do roteiro, com honestidade sobre o que este
projeto de fato implementa (não apenas o que o roteiro descreve para um deployment
hipotético em produção):

| Componente | É SPOF? | Por quê |
|---|---|---|
| Gateway | Sim | Ponto de entrada único para tráfego externo (ADR 0009). Mitigação real: nenhuma réplica — `k8s/gateway.yaml` declara 1 réplica sem HPA. |
| Banco de cada serviço (SQLite, arquivo local) | Sim, e sem mitigação | Nenhuma réplica promovível existe neste projeto — `docs/adr/0003-stack-tecnologica.md` já registrava SQLite como escolha de desenvolvimento, não de produção. Um failover "ensaiado" (Aula 14) não existe para o banco, porque não há banco replicado para ensaiar. |
| Barramento de eventos | Sim, e mais severo do que o exemplo do roteiro | O roteiro descreve "uma instância isolada de mensageria usada por todas as réplicas" como SPOF dissimulado. Este projeto está em um estágio anterior: o barramento (`services/pedidos/app/barramento.py`) é em memória, dentro do processo de uma única instância de `pedidos` — não sobrevive nem a um reinício (ADR 0010). |
| Segredo de identidade (`NEXAORDER_SEGREDO_ASSINATURA`) | Sim | Compartilhado por HMAC entre todos os serviços (ADR 0012) — comprometido em um serviço, comprometido em todos. mTLS real eliminaria essa classe de risco. |
| Coletor de observabilidade | Não existe um centralizado — cada serviço guarda seus próprios spans (ADR 0013) | Sem coletor central, não há um único ponto cuja queda tire a visibilidade de todos os serviços ao mesmo tempo — mas também não há visão agregada nenhuma, mesmo com tudo saudável. É o oposto do risco do roteiro, com uma limitação equivalente. |

A armadilha central do roteiro se confirma aqui de outra forma: não é que réplicas
em várias zonas escondam um SPOF compartilhado — é que este projeto, sendo um
protótipo de desenvolvimento, nunca chegou a ter réplicas de dado ou de mensageria
para começar. A lista acima é o que precisaria mudar antes de uma implantação real
— não uma lista de riscos já mitigados.

**Esta seção deixou de ser análise e passou a ser medição.** Os manifests foram
aplicados em um cluster kind de três nós ao longo de toda a Unidade 4
(`docs/kubernetes-execucao.md`), e a execução confirmou os três itens — em dois deles,
de forma mais severa do que a análise previa:

- O banco em `emptyDir` não é só "sem réplica promovível": **ter uma segunda réplica
  já quebra a leitura**. Um pedido criado existe em exatamente um dos quatro Pods, e o
  gateway devolveu 404 em 24 requisições seguidas — determinístico, porque o `Service`
  balanceia conexões e o cliente HTTP as mantém abertas.
- O barramento em memória não sobrevive a uma segunda réplica, e não apenas a um
  reinício: doze tentativas de fraude do mesmo dispositivo, distribuídas por quatro
  Pods, viram três em cada um, e o alerta some sem nenhum erro registrado.
- A ausência de coletor central custa exatamente o que o ADR 0013 admitia: dez spans
  de um único trace espalhados por sete Pods, sem consulta que os reúna.

E acrescentou um item que nenhuma análise deste projeto tinha, porque nenhum teste o
alcançava: **o disjuntor não abria sob indisponibilidade total**. Um provedor fora do
ar recusa a conexão em vez de dar timeout, e `httpx.ConnectError` escapava do cliente
resiliente, da saga e do disjuntor — três compras devolveram HTTP 500 e vazaram
reserva de estoque. Corrigido na Aula 14 (`aula_14/docs/testes-e-caos.md`), com
regressão. Até então, esta defesa arquitetural teria afirmado ter uma proteção que,
no modo de falha mais comum em produção, não existia. É a razão pela qual "decisão
arquitetural é hipótese verificável" não é retórica: a verificação encontrou uma
hipótese falsa.

## 5. RPO e RTO

O roteiro define RPO ≈ 5 min e RTO ≈ 15 min para a NexaOrder madura, a partir de
requisitos de negócio (quantos minutos de pedidos a empresa aceita perder; por
quantos minutos aceita ficar indisponível) — não de conveniência técnica.

**Honestidade sobre o que este projeto tem hoje**: RPO e RTO exigem um mecanismo de
replicação e recuperação para calcular sobre algo real. Este projeto não implementa
nenhum backup nem replicação entre regiões — cada banco SQLite é um arquivo local
sem cópia. Aplicando o método do roteiro (partir do requisito de negócio, não do que
a infraestrutura atual alcança): se a NexaOrder aceitasse perder até 5 minutos de
pedidos e ficar indisponível por até 15 minutos, isso exigiria — a partir do zero
atual — implementar replicação assíncrona do banco de `pedidos` (o único cujo estado
não pode ser reconstruído a partir de outro serviço) com intervalo ≤ 5 min, e um
procedimento de promoção de réplica ensaiado que complete em ≤ 15 min. Nenhum dos
dois existe no código deste projeto hoje — é o próximo item de uma lista de
prontidão para produção, não uma capacidade já entregue.

## 6. Seguro e observável por padrão, como critério de aceite

O roteiro é direto: essas perguntas devem virar critério de aceite de um serviço
novo, não sugestão em documento de boas práticas. `scripts/verificar_criterios_de_aceite.py`
faz exatamente isso, de forma executável — no mesmo espírito de
`verificar_fronteiras.py` (Aula 9): um serviço sem `app/seguranca.py`,
`app/logs_estruturados.py`, `app/metricas.py`, `app/tracing.py` ou sem teste algum
não passa. Rodado contra os cinco serviços reais deste projeto, hoje:

```
✓ Todos os serviços cumprem os critérios de aceite (identidade, observabilidade, testes).
```

## 7. Redundância paralela: o contraste final com a cadeia sequencial

`scripts/disponibilidade_em_cadeia.py` agora tem as duas leituras lado a lado. A
cadeia sequencial da Aula 14 (quatro serviços de 99,9%) **piora** para 99,6%. Três
réplicas independentes de 99,5% em paralelo **melhoram** para aproximadamente
0,999999875 — sete noves (`test_tres_replicas_independentes_de_99_5_por_cento_compoem_sete_noves`).

Duas ressalvas, exatamente como o roteiro exige: o cálculo pressupõe independência
de falha — réplicas que compartilham o mesmo SQLite, como este projeto teria hoje se
tentasse "replicar" um serviço sem primeiro resolver o item 4, não seriam
independentes, e o número real ficaria muito abaixo do calculado. E sete noves em um
serviço interno é investimento sem retorno — o ganho só se justifica pelo valor de
negócio que a disponibilidade adicional entrega.

## 8. Custo, sustentabilidade e evolução

`k8s/pedidos.yaml` já implementa a resposta madura ao desperdício de capacidade fixa
para o pico: o HPA da Aula 11 ajusta réplicas à demanda observada (4→6 no exemplo
numérico da Aula 11), em vez de manter capacidade de pico ociosa o tempo todo, ou
pior, eliminar a redundância necessária ao pico para economizar. Nenhuma arquitetura
permanece ótima — o próprio fato de este projeto ter 15 ADRs registrando decisões
que mudaram de aula em aula é evidência de evolução contínua, não de execução
malfeita.

## 9. A trajetória completa

- **Unidade 1** — fundamentos: o que caracteriza um sistema distribuído, comunicação
  entre processos, tempo e ordenação (Lamport), contenção de falha parcial
  (disjuntor, retry, timeout).
- **Unidade 2** — dados: replicação e consistência por dado, particionamento, CAP e
  PACELC, consenso, sagas e idempotência.
- **Unidade 3** — serviços: limites de domínio, arquitetura orientada a eventos,
  contêineres e Kubernetes, comunicação segura.
- **Unidade 4** — operação: observabilidade, testes e caos, processamento em escala,
  e esta avaliação arquitetural integrada.

Nenhuma unidade, isolada, entrega uma arquitetura completa — é possível ter
fundamentos sólidos sem visibilidade nenhuma, observabilidade impecável sobre um
monólito distribuído, ou serviços bem delimitados sobre dados inconsistentes. É a
combinação das quatro que sustenta um sistema em produção, sob carga real, ao longo
do tempo. `projeto_nexaorder/` — 16 pastas, cada uma o projeto inteiro até aquele
ponto, executável e testado — é essa combinação, construída incrementalmente, aula a
aula.

## Decisão registrada

Ver `docs/adr/0016-defesa-arquitetural-nao-introduz-mecanismo-novo.md`.
