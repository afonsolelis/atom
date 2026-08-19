# Aula 9 — Limites de domínio reforçados

**Videoaula correspondente:** Aula 9 — Decomposição em serviços e limites de domínio.

Esta aula não adiciona um passo novo ao fluxo de compra. Ela audita se as fronteiras
que o projeto já tem são reais — e adiciona a primeira peça de infraestrutura que fala
com o cliente externo em nome de todos os outros serviços: o gateway.

## O que esta aula acrescentou ao projeto

- `services/gateway/` — novo serviço, sem banco de dados e sem regra de negócio.
  `GET /pedidos/{id}/resumo` compõe pedido, reservas, cobranças e remessas em uma
  única resposta.
- `estoque`, `pagamento` e `expedicao` ganham `GET .../por-pedido/{pedido_id}`, para
  que o gateway possa consultá-los sem acessar banco de dados de ninguém diretamente.
- `scripts/calcular_instabilidade.py` — aplica I = Ce/(Ca+Ce) ao grafo de dependências
  real do projeto (não a um exemplo hipotético).
- `scripts/verificar_fronteiras.py` — um linter estático real: audita imports
  cruzados entre serviços, bancos de dados compartilhados e capacidade de implantação
  isolada. Roda contra o próprio projeto e passa.
- `docs/limites-de-dominio.md` — os seis sinais de monólito distribuído do roteiro,
  avaliados um a um contra este projeto específico.

## O experimento central: auditar as próprias fronteiras

```bash
python3 scripts/verificar_fronteiras.py
```

```
✓ Imports cruzados entre serviços: nenhuma violação
✓ Banco de dados compartilhado: nenhuma violação
✓ Implantável isoladamente (requirements + Dockerfile): nenhuma violação
```

```bash
python3 scripts/calcular_instabilidade.py
```

```
estoque      I = 0.00   muito estável
pagamento    I = 0.00   muito estável
expedicao    I = 0.00   muito estável
pedidos      I = 0.75   muito instável
gateway      I = 1.00   muito instável
```

## Roteiro de condução

1. Rode `verificar_fronteiras.py` ao vivo. Pergunte à turma: o que esse script NÃO
   consegue verificar (implantações coordenadas na prática, incidentes exigindo o
   time todo) — e por que essas duas coisas só se observam em operação real, nunca
   em análise estática.
2. Rode `calcular_instabilidade.py` e conecte com o exemplo do roteiro: `estoque` aqui
   desempenha o mesmo papel do "estoque com I=0,25" da aula — um serviço que precisa
   de contratos cuidadosos porque muita coisa depende dele.
3. Abra `services/gateway/app/main.py` e mostre as duas ausências deliberadas: sem
   banco, sem regra de negócio. Rode `tests/test_gateway.py` e mostre o caso de
   consulta best-effort — um pedido recém-criado tem `resumo` funcional mesmo sem
   nenhuma reserva ainda.
4. Feche com `docs/limites-de-dominio.md`: percorra a tabela dos seis sinais e
   discuta os dois que o projeto não consegue provar sozinho (exigem operação real).

## Como rodar

```bash
make setup
make test         # 92 testes: 42 pedidos, 36 estoque, 6 pagamento, 5 expedicao, 3 gateway
make verificar     # verificar_fronteiras.py + calcular_instabilidade.py
python3 -m pytest scripts/   # 4 testes da fórmula de instabilidade (usa o venv compartilhado)
make up            # contêineres (Docker ou Podman) com os cinco serviços
```

## Pergunta que fica em aberto

As fronteiras estão corretas, mas a comunicação entre elas continua sendo HTTP
síncrono, ponto a ponto. `finalizar-compra` ainda propaga indisponibilidade pela
cadeia inteira se um serviço estiver lento — o problema que abriu a Aula 2, e que a
Aula 10 resolve reorganizando a comunicação em torno de eventos.

## Estado do projeto

```
docs/
  limites-de-dominio.md                          [novo]
  adr/0009-gateway-sem-logica-de-negocio.md       [novo]
scripts/                                          [novo diretório]
  calcular_instabilidade.py
  test_calcular_instabilidade.py
  verificar_fronteiras.py
services/
  gateway/                                        [novo serviço]
    app/main.py
    tests/test_gateway.py
  estoque/    app/main.py    [alterado: GET /reservas/por-pedido/{pedido_id}]
  pagamento/  app/main.py    [alterado: GET /cobrancas/por-pedido/{pedido_id}]
  expedicao/  app/main.py    [alterado: GET /remessas/por-pedido/{pedido_id}]
docker-compose.yml                                [alterado: 5 serviços]
Makefile                                          [alterado: 5 serviços, alvo `verificar`]
```

96 testes (92 nos cinco serviços + 4 no cálculo de instabilidade), 5 serviços, 1
verificador de fronteiras que audita o próprio projeto e passa.
