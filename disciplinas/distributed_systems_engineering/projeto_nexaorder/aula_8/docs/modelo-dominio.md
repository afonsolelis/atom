# Modelo de domínio — NexaOrder

## Capacidades de negócio

A NexaOrder existe para converter a intenção de compra de um cliente em um produto
entregue. Cinco capacidades sustentam isso:

| Capacidade | Responsabilidade | Pergunta que ela responde |
|------------|------------------|----------------------------|
| Catálogo | Expor o que está à venda | "Este produto existe e custa quanto?" |
| Pedidos | Registrar a intenção e coordenar o fluxo | "Em que estado está esta compra?" |
| Estoque | Controlar unidades físicas disponíveis | "Ainda existe esta unidade?" |
| Pagamento | Obter autorização financeira | "O dinheiro foi autorizado?" |
| Expedição | Preparar e despachar o envio | "Quando isto sai do centro de distribuição?" |

## Agregados

Um agregado é a unidade de consistência: tudo dentro dele muda junto, em uma transação.

### Pedido (raiz)

```
Pedido
  id: UUID
  cliente_id: UUID
  estado: RECEBIDO | RESERVADO | PAGO | EXPEDIDO | CANCELADO
  criado_em: timestamp
  chave_idempotencia: string
  itens: [ItemPedido]

ItemPedido
  sku: string
  quantidade: int
  preco_unitario: decimal
```

Regra de invariância: um pedido sem itens não existe, e a soma dos itens define o valor
total. Essas duas regras vivem dentro do agregado e nunca dependem de rede.

### Reserva (raiz, no Estoque)

```
Reserva
  id: UUID
  pedido_id: UUID
  sku: string
  quantidade: int
  estado: ATIVA | LIBERADA | CONSUMIDA
  expira_em: timestamp
```

Regra de invariância: o saldo disponível de um SKU nunca fica negativo.
Esta é a regra mais cara do sistema inteiro — ela é a razão de existir a Aula 7.

### Cobrança (raiz, no Pagamento)

```
Cobranca
  id: UUID
  pedido_id: UUID
  valor: decimal
  estado: AUTORIZADA | RECUSADA | ESTORNADA
  chave_idempotencia: string
  referencia_externa: string
```

### Remessa (raiz, na Expedição)

```
Remessa
  id: UUID
  pedido_id: UUID
  estado: ETIQUETA_GERADA | DESPACHADA | CANCELADA
  codigo_rastreio: string
```

## O termo que muda de significado

Esta é a observação mais importante do documento.

A palavra **"item"** aparece em dois contextos e significa coisas diferentes:

| Contexto | O que "item" é | Atributos que importam |
|----------|----------------|-------------------------|
| Catálogo | Uma descrição comercial | preço, imagens, categoria, texto de marketing |
| Estoque | Uma quantidade física | SKU, saldo, localização na prateleira, número de série |

Tratar as duas visões como um mesmo modelo de dados compartilhado é a origem mais comum
de acoplamento acidental. Uma mudança de significado no catálogo passaria a quebrar
silenciosamente o controle de estoque.

**Consequência de projeto:** catálogo e estoque são contextos delimitados distintos.
Eles se referem à mesma coisa do mundo real por um identificador comum, o SKU, e nada
mais. Essa decisão é executada de fato na Aula 9.

## Glossário

- **SKU** — identificador da unidade de estoque. É o único termo compartilhado entre
  catálogo e estoque, e serve exatamente para que nada mais precise ser compartilhado.
- **Reserva** — bloqueio temporário de uma unidade, anterior ao pagamento. Existe porque
  o intervalo entre "quero comprar" e "paguei" não é instantâneo.
- **Compensação** — ação que reverte logicamente uma etapa já concluída. Não é o mesmo
  que desfazer: estornar uma cobrança tem custo e prazo que nunca cobrar não tem.
- **Chave de idempotência** — identificador de uma operação lógica, criado pelo cliente
  antes do primeiro envio, que permite repetir a chamada sem duplicar o efeito.

## Fluxo principal

```
cliente → criar pedido
        → reservar estoque
        → autorizar pagamento
        → confirmar pedido
        → solicitar expedição
```

Note que este é o caminho feliz. Cada seta é uma fronteira de rede em potencial, e
portanto um ponto onde a resposta pode não voltar. O projeto inteiro consiste em
decidir, seta a seta, o que fazer nesse caso.
