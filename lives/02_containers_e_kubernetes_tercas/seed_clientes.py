"""
Seed de 1000 clientes na coleção `clientes` do MongoDB.

Gera dados brasileiros pseudo-realistas respeitando o schema usado em app.py.
Executado dentro do container livraria-app (usa MONGO_URI da rede Docker).

Uso:
    docker exec livraria-app python seed_clientes.py
    docker exec livraria-app python seed_clientes.py --limpar   # apaga antes de inserir
"""

import os
import sys
import random
from datetime import datetime, timedelta

from pymongo import MongoClient

random.seed(42)  # reproduzível

PRIMEIROS = [
    "João", "Maria", "José", "Ana", "Pedro", "Paulo", "Carlos", "Lucas",
    "Mariana", "Gabriel", "Rafael", "Fernanda", "Juliana", "Marcos", "Bruno",
    "Camila", "Rodrigo", "Amanda", "Felipe", "Larissa", "Gustavo", "Beatriz",
    "Leonardo", "Patrícia", "Ricardo", "Vanessa", "André", "Aline", "Diego",
    "Renata", "Thiago", "Carla", "Vinícius", "Bianca", "Eduardo", "Débora",
    "Matheus", "Letícia", "Daniel", "Sabrina", "Guilherme", "Priscila",
    "Henrique", "Natália", "Roberto", "Isabela", "Fábio", "Tatiane", "Márcio",
    "Simone",
]

SOBRENOMES = [
    "Silva", "Santos", "Oliveira", "Souza", "Rodrigues", "Ferreira", "Alves",
    "Pereira", "Lima", "Gomes", "Costa", "Ribeiro", "Martins", "Carvalho",
    "Almeida", "Lopes", "Soares", "Fernandes", "Vieira", "Barbosa", "Rocha",
    "Dias", "Nascimento", "Andrade", "Moreira", "Nunes", "Marques", "Machado",
    "Mendes", "Freitas", "Cardoso", "Ramos", "Gonçalves", "Araújo", "Teixeira",
    "Correia", "Cavalcanti", "Monteiro", "Moraes", "Cardim",
]

# cidade principal por estado (para dar coerência ao par cidade/estado)
CIDADES_POR_ESTADO = {
    "SP": ["São Paulo", "Campinas", "Santos", "Guarulhos", "Ribeirão Preto"],
    "RJ": ["Rio de Janeiro", "Niterói", "Nova Iguaçu", "Petrópolis"],
    "MG": ["Belo Horizonte", "Uberlândia", "Contagem", "Juiz de Fora"],
    "BA": ["Salvador", "Feira de Santana", "Vitória da Conquista"],
    "RS": ["Porto Alegre", "Caxias do Sul", "Pelotas", "Canoas"],
    "PR": ["Curitiba", "Londrina", "Maringá", "Ponta Grossa"],
    "SC": ["Florianópolis", "Joinville", "Blumenau", "Chapecó"],
    "PE": ["Recife", "Jaboatão dos Guararapes", "Olinda", "Caruaru"],
    "CE": ["Fortaleza", "Caucaia", "Juazeiro do Norte"],
    "PA": ["Belém", "Ananindeua", "Santarém", "Marabá"],
    "GO": ["Goiânia", "Aparecida de Goiânia", "Anápolis"],
    "DF": ["Brasília", "Ceilândia", "Taguatinga"],
    "ES": ["Vitória", "Vila Velha", "Serra", "Cariacica"],
    "MS": ["Campo Grande", "Dourados", "Três Lagoas"],
    "MT": ["Cuiabá", "Várzea Grande", "Rondonópolis"],
    "RO": ["Porto Velho", "Ji-Paraná", "Ariquemes"],
    "AC": ["Rio Branco", "Cruzeiro do Sul"],
    "AM": ["Manaus", "Parintins", "Itacoatiara"],
    "AP": ["Macapá", "Santana"],
    "RR": ["Boa Vista", "Rorainópolis"],
    "TO": ["Palmas", "Araguaína", "Gurupi"],
}
ESTADOS = list(CIDADES_POR_ESTADO.keys())

LOGRADOUROS = [
    "Rua das Flores", "Avenida Brasil", "Rua XV de Novembro", "Avenida Paulista",
    "Rua São João", "Travessa da Paz", "Alameda dos Anjos", "Rua do Comércio",
    "Avenida Getúlio Vargas", "Rua Sete de Setembro", "Rua da Consolação",
    "Avenida Ipiranga", "Rua Marechal Deodoro", "Rua Barão do Rio Branco",
]

CATEGORIAS = ["Regular", "Premium", "VIP"]
PESOS_CATEGORIA = [0.65, 0.25, 0.10]  # maioria Regular

OBSERVACOES = [
    "Cliente fiel, compra mensalmente.",
    "Prefere contato por email.",
    "Interessado em lançamentos de ficção científica.",
    "Participa do clube de leitura.",
    "Solicitou catálogo de literatura acadêmica.",
    "Cadastro importado da campanha de marketing.",
    "Aguardando reposição de estoque de título encomendado.",
    "Cliente indicado por outro leitor.",
    "Costuma comprar em datas comemorativas.",
    "",  # alguns sem observação
]

DDDS = ["11", "21", "31", "41", "48", "51", "61", "71", "81", "85", "62", "27"]


def gera_cpf():
    n = [random.randint(0, 9) for _ in range(9)]

    def dv(digs):
        s = sum(d * f for d, f in zip(digs, range(len(digs) + 1, 1, -1)))
        r = (s * 10) % 11
        return 0 if r == 10 else r

    d1 = dv(n)
    d2 = dv(n + [d1])
    todos = n + [d1, d2]
    return "{}{}{}.{}{}{}.{}{}{}-{}{}".format(*todos)


def gera_telefone():
    ddd = random.choice(DDDS)
    return f"({ddd}) 9{random.randint(1000,9999)}-{random.randint(1000,9999)}"


def gera_cep():
    return f"{random.randint(1000,99999):05d}-{random.randint(0,999):03d}"


def gera_cliente(i):
    primeiro = random.choice(PRIMEIROS)
    sobrenome = random.choice(SOBRENOMES)
    nome = f"{primeiro} {sobrenome}"

    estado = random.choice(ESTADOS)
    cidade = random.choice(CIDADES_POR_ESTADO[estado])

    # email único graças ao índice i
    base_email = f"{primeiro}.{sobrenome}".lower()
    base_email = (base_email
                  .replace("á", "a").replace("â", "a").replace("ã", "a")
                  .replace("é", "e").replace("ê", "e").replace("í", "i")
                  .replace("ó", "o").replace("ô", "o").replace("õ", "o")
                  .replace("ú", "u").replace("ç", "c").replace(" ", ""))
    dominio = random.choice(["gmail.com", "hotmail.com", "outlook.com", "yahoo.com.br"])
    email = f"{base_email}{i}@{dominio}"

    dias_atras = random.randint(0, 730)  # cadastros nos últimos 2 anos
    data_cadastro = datetime.now() - timedelta(
        days=dias_atras, hours=random.randint(0, 23), minutes=random.randint(0, 59)
    )

    return {
        "nome": nome,
        "email": email,
        "telefone": gera_telefone(),
        "cpf": gera_cpf(),
        "endereco": f"{random.choice(LOGRADOUROS)}, {random.randint(1, 2000)}",
        "cidade": cidade,
        "estado": estado,
        "cep": gera_cep(),
        "categoria": random.choices(CATEGORIAS, weights=PESOS_CATEGORIA)[0],
        "observacoes": random.choice(OBSERVACOES),
        "data_cadastro": data_cadastro,
        "ativo": True,
    }


def main():
    mongo_uri = os.getenv(
        "MONGO_URI",
        "mongodb://admin:senha123@localhost:27017/livraria?authSource=admin",
    )
    client = MongoClient(mongo_uri)
    db = client["livraria"]
    colecao = db["clientes"]

    if "--limpar" in sys.argv:
        removidos = colecao.delete_many({}).deleted_count
        print(f"🧹 Coleção limpa: {removidos} documento(s) removido(s).")

    quantidade = 1000
    clientes = [gera_cliente(i) for i in range(quantidade)]

    resultado = colecao.insert_many(clientes)
    print(f"✅ {len(resultado.inserted_ids)} clientes inseridos com sucesso!")
    print(f"📊 Total de clientes ativos na coleção: {colecao.count_documents({'ativo': True})}")

    # resumo por categoria
    for cat in CATEGORIAS:
        n = colecao.count_documents({"categoria": cat, "ativo": True})
        print(f"   - {cat}: {n}")


if __name__ == "__main__":
    main()
