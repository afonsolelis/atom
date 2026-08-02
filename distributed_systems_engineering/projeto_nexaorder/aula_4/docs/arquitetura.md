# Arquitetura — visão da Aula 2

Nesta aula a NexaOrder ganha forma visual. Os diagramas evoluem ao longo do projeto —
compare este arquivo com a versão da Aula 10 (arquitetura orientada a eventos) e da
Aula 16 (plataforma completa) para ver a mesma arquitetura amadurecer.

## Visão de componentes

```mermaid
flowchart TB
    cliente["Cliente"]

    subgraph borda["Borda"]
        gateway["Gateway<br/>(ainda não existe como componente —<br/>chega na Aula 9)"]
    end

    subgraph nucleo["Serviços de domínio"]
        pedidos["Pedidos<br/>(código a partir da Aula 3)"]
        estoque["Estoque<br/>(código a partir da Aula 5)"]
        pagamento["Pagamento<br/>(código a partir da Aula 8)"]
        expedicao["Expedição<br/>(código a partir da Aula 8)"]
    end

    provedor["Provedor de pagamento<br/>(externo, fora do nosso controle)"]

    cliente -->|HTTP síncrono| pedidos
    pedidos -->|reservar item| estoque
    pedidos -->|autorizar pagamento| pagamento
    pagamento -->|autorização| provedor
    pedidos -->|solicitar expedição| expedicao

    style gateway fill:#eee,stroke:#999,stroke-dasharray: 5 5
    style estoque fill:#eee,stroke:#999,stroke-dasharray: 5 5
    style pagamento fill:#eee,stroke:#999,stroke-dasharray: 5 5
    style expedicao fill:#eee,stroke:#999,stroke-dasharray: 5 5
```

As caixas tracejadas ainda não existem como código nesta aula. Isso é deliberado: o
diagrama descreve a arquitetura **alvo**, e o código a alcança de forma incremental.
Compare este diagrama com o `services/` de cada aula seguinte para ver a lacuna
diminuir.

## Sequência do caminho feliz — decisão síncrona por enquanto

```mermaid
sequenceDiagram
    autonumber
    participant C as Cliente
    participant P as Pedidos
    participant E as Estoque
    participant Pg as Pagamento
    participant Ex as Expedição

    C->>P: POST /pedidos (síncrono)
    P->>E: reservar item (síncrono)
    E-->>P: reserva confirmada
    P->>Pg: autorizar pagamento (síncrono)
    Pg-->>P: autorizado
    P->>Ex: solicitar expedição (síncrono)
    Ex-->>P: etiqueta gerada
    P-->>C: pedido confirmado
```

Este é o desenho da Aula 2, ainda inteiramente síncrono. O roteiro da Aula 2 mostra
o custo desse encadeamento: a disponibilidade do fluxo é o produto das disponibilidades
de cada etapa, e a latência é a soma. Este diagrama é substituído por um baseado em
eventos na Aula 10 — guarde-o para comparar.

## Decisão registrada

Ver `docs/adr/0002-comunicacao-sincrona-inicial.md`: por que o projeto começa com
comunicação síncrona mesmo sabendo do seu custo, e qual evidência dispara a migração
para eventos.
