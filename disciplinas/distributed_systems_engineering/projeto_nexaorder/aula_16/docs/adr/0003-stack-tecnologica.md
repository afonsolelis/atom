# ADR 0003 — Stack tecnológica

- **Status:** aceito
- **Data:** correspondente à Unidade 1, Aula 4

## Contexto

Até a Aula 3, o projeto tinha um único serviço. A partir desta aula, um segundo
serviço (`estoque`) entra em cena e os dois passam a se comunicar por rede — é o
primeiro momento em que "qual tecnologia" deixa de ser uma escolha isolada por
serviço e passa a ser uma escolha de plataforma.

## Decisão

| Camada | Escolha | Alternativas descartadas |
|--------|---------|---------------------------|
| Linguagem | Python 3.12+ | Node/TypeScript, Java/Spring Boot |
| Framework HTTP | FastAPI | Flask, Django REST Framework |
| Validação de contrato | Pydantic (nativo do FastAPI) | jsonschema manual |
| Banco por serviço | SQLite (arquivo local) | Postgres (adiado para quando a Aula 5 exigir réplicas de verdade) |
| Empacotamento | Docker, uma imagem por serviço | processos nativos gerenciados por script |
| Orquestração local | Docker Compose | scripts shell ad hoc |

## Por quê

- **Python + FastAPI**: menor barreira de entrada para quem está aprendendo o
  raciocínio distribuído — o objetivo da disciplina não é ensinar uma linguagem, é
  ensinar por que um sistema muda de comportamento quando cresce. Tipagem via
  Pydantic dá o mesmo benefício de contratos explícitos que uma stack tipada traria,
  sem a verbosidade de configuração inicial.
- **SQLite por serviço, por enquanto**: cada serviço já tem "seu" banco, fisicamente
  isolado em um arquivo. Isso implementa a regra de dados por serviço (Aula 9) desde
  já, sem o custo operacional de subir um Postgres por serviço só para rodar um teste
  local. A troca para Postgres, quando fizer sentido, é uma mudança de driver, não de
  arquitetura — a fronteira já está certa.
- **Docker Compose, não Kubernetes, por enquanto**: Compose é suficiente para
  demonstrar múltiplos serviços se comunicando e um disjuntor abrindo de verdade.
  Kubernetes entra na Aula 11, quando o assunto da aula é justamente orquestração,
  reconciliação e sondas — introduzi-lo antes disso obrigaria a ensinar kubectl antes
  de precisar dele.

## Compromisso aceito

SQLite não sustenta réplicas de leitura reais nem múltiplos escritores concorrentes
em produção. A Aula 5 simula o comportamento de uma réplica (atraso de leitura,
consistência eventual) em cima de SQLite mesmo assim — é uma simplificação didática,
registrada aqui para não ser confundida com recomendação de produção.

## Evidência

A stack se sustenta enquanto os testes de cada serviço rodarem em menos de 2 segundos
localmente (sem depender de infraestrutura externa) e o `docker compose up` completo
subir em menos de um minuto em uma máquina comum. Se qualquer um desses dois limites
for violado de forma persistente, esta ADR deve ser revisitada.
