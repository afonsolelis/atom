# Consistência por dado — Unidade 2, Aula 5

A pergunta certa nunca é "qual modelo de consistência o sistema usa", porque essa
pergunta pressupõe uma resposta única. A pergunta certa é: **o que este dado
específico não pode tolerar?**

## Os quatro modelos (referência conceitual)

| Modelo | Garantia | Implementado neste projeto? |
|--------|----------|-------------------------------|
| Forte (linearizabilidade) | toda leitura reflete a escrita mais recente confirmada | Sim — leitura no líder (`consistencia=forte`) |
| Sequencial | todas as réplicas concordam com a mesma ordem, não necessariamente igual ao tempo real | Não implementado; discutido conceitualmente |
| Causal | operações causalmente relacionadas são vistas na mesma ordem por todos | Não implementado nesta aula — volta como relógio vetorial na Aula 6/7 |
| Eventual | cessadas as escritas, as réplicas convergem | Sim — leitura na réplica (`consistencia=eventual`), com atraso de 150 ms |

Implementar os quatro de forma completa exigiria um sistema de banco de dados
distribuído de verdade. O projeto implementa os dois extremos (forte e eventual) o
suficiente para que a diferença seja **observável em teste**, e documenta os do meio
como extensão conceitual — não como lacuna esquecida.

## Matriz de garantias da NexaOrder

| Dado | Consistência escolhida | Por quê | Onde vive |
|------|--------------------------|---------|-----------|
| Saldo de estoque — leitura informativa | Eventual | Mostrar "restam poucas unidades" tolera alguns milissegundos de atraso; a alternativa (consultar o líder a cada exibição) sobrecarregaria o serviço sem ganho perceptível para quem só está navegando | `GET /saldo/{sku}?consistencia=eventual` |
| Saldo de estoque — decisão de reservar | Forte | Vender a mesma unidade duas vezes é o incidente mais caro do domínio; a decisão de decrementar o saldo só pode ser tomada contra o valor mais atual possível | `POST /reservas`, sempre contra o líder |
| Catálogo (preço, descrição) | Eventual | Não implementado como serviço neste projeto — mas seguiria a mesma política do saldo informativo: um preço desatualizado por segundos não compromete o negócio | Fora do escopo de código; ver `docs/modelo-dominio.md` |
| Pagamento (autorização) | Forte | É o dado com maior risco financeiro e regulatório | Implementado na Aula 8 |

## O que o código demonstra, concretamente

`GET /saldo/{sku}?consistencia=forte` sempre lê do líder — o valor mais recente
confirmado, ao custo de bater no armazenamento principal a cada consulta.

`GET /saldo/{sku}?consistencia=eventual` lê de uma réplica em memória, atualizada de
forma assíncrona depois de cada escrita, com atraso fixo de 150 ms
(`services/estoque/app/replica.py`). Uma leitura eventual feita nesse intervalo
devolve o valor **anterior** — não porque algo quebrou, mas porque a réplica ainda
não recebeu a propagação. É exatamente o incidente do roteiro da Aula 5: "nenhuma
réplica mentiu".

`tests/test_replica.py::test_atraso_padrao_e_150ms_como_no_roteiro_da_aula_5` prova
esse intervalo com um cronômetro real, não apenas com um mock de tempo.

## Decisão registrada

Ver `docs/adr/0005-consistencia-por-dado.md`.
