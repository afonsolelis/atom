# Limites de domínio — Unidade 3, Aula 9

## Instabilidade dos serviços reais da NexaOrder

`scripts/calcular_instabilidade.py` aplica I = Ce/(Ca+Ce) ao grafo de dependências
real do projeto (declarado a partir da leitura de cada `main.py`, não inferido):

```
estoque      I = 0.00   muito estável
pagamento    I = 0.00   muito estável
expedicao    I = 0.00   muito estável
pedidos      I = 0.75   muito instável
gateway      I = 1.00   muito instável
```

A leitura: `estoque`, `pagamento` e `expedicao` não chamam ninguém e são chamados por
dois serviços cada — são o análogo, neste projeto, do "estoque com instabilidade
0,25" do exemplo da aula: precisam de contratos muito bem cuidados, porque mudanças
neles se propagam. `pedidos` e `gateway`, ao contrário, dependem de tudo e quase
ninguém depende deles — devem ser projetados para **absorver** mudança, não para que
o resto do sistema absorva as deles.

## Os seis sinais de monólito distribuído, aplicados a este projeto

| Sinal do roteiro | Situação neste projeto |
|-------------------|---------------------------|
| Implantações coordenadas | Não observado: cada serviço tem Dockerfile e requirements.txt próprios, testados isoladamente (`scripts/verificar_fronteiras.py`) |
| Mudança de esquema quebra outros serviços | Parcialmente exposto: os contratos HTTP entre serviços (Aula 2) não são versionados automaticamente — risco real, mitigado apenas por disciplina de compatibilidade aditiva |
| Incidente exige todo o time | Não avaliável em um projeto didático sem operação real — mas a saga (Aula 8) e os disjuntores independentes (Aula 4) limitam o raio de impacto de uma falha de serviço único |
| Tabelas, filas ou segredos compartilhados sem contrato | Não observado: `scripts/verificar_fronteiras.py` confirma bancos de dados distintos e ausência de import cruzado |
| Topologia conversacional | Observado, com justificativa: `finalizar-compra` faz 3 saltos de rede (estoque, pagamento, expedição), e `resumo` do gateway faz até 4. Ambos os números são pequenos e documentados — não crescem com o tempo por acidente |
| Times não testam nem implantam sem depender de outros | Não observado: cada serviço tem sua própria suíte de testes, executável isoladamente (`make test` roda os cinco separadamente) |

## API Gateway: o que ele faz, e o que ele deliberadamente não faz

`services/gateway` compõe `GET /pedidos/{id}/resumo` a partir de quatro chamadas.
Duas decisões de projeto, ambas do roteiro:

- **Sem banco de dados próprio.** O gateway não guarda nada — ele só roteia e compõe.
- **Sem regra de negócio.** A decisão de que um pedido "pode" ser expedido antes do
  pagamento continua inteiramente dentro da saga de `pedidos`. O gateway nunca decide
  isso; ele só mostra o que os outros serviços já decidiram.
- **Consultas auxiliares são best-effort.** Se `estoque` estiver fora do ar, o
  `resumo` ainda responde, com a lista de reservas vazia — apenas a consulta ao
  pedido em si é obrigatória. Essa assimetria é deliberada: o gateway não deveria
  ficar tão frágil quanto o mais frágil dos serviços que compõe.

## Decisão registrada

Ver `docs/adr/0009-gateway-sem-logica-de-negocio.md`.
