import os
from datetime import date, datetime

import pandas as pd
import streamlit as st
from pymongo import ASCENDING, MongoClient
from pymongo.errors import DuplicateKeyError, PyMongoError

st.set_page_config(page_title="Cadastro de pacientes", page_icon="🩺", layout="wide")


@st.cache_resource
def get_database():
    """Cria uma única conexão com o MongoDB por processo do Streamlit."""
    client = MongoClient(
        os.getenv("MONGO_URI", "mongodb://admin:admin@localhost:27017/?authSource=admin"),
        serverSelectionTimeoutMS=5000,
    )
    client.admin.command("ping")
    database = client[os.getenv("MONGO_DATABASE", "clinica")]
    database.pacientes.create_index([("cpf", ASCENDING)], unique=True)
    return database


def as_date(value):
    return value.date() if isinstance(value, datetime) else value or date.today()


st.title("🩺 Cadastro de pacientes")
st.caption("CRUD de exemplo com Streamlit e MongoDB")

try:
    pacientes = get_database().pacientes
except PyMongoError as error:
    st.error("Não foi possível conectar ao MongoDB. Verifique se o banco está em execução.")
    st.code(str(error))
    st.stop()

criar, listar, editar, excluir = st.tabs(["Cadastrar", "Listar", "Editar", "Excluir"])

with criar:
    with st.form("criar", clear_on_submit=True):
        nome = st.text_input("Nome completo")
        cpf = st.text_input("CPF", help="Neste exemplo, o CPF é o identificador único.")
        nascimento = st.date_input("Data de nascimento", min_value=date(1900, 1, 1))
        email = st.text_input("E-mail")
        telefone = st.text_input("Telefone")
        enviado = st.form_submit_button("Cadastrar paciente", type="primary")
    if enviado:
        if not nome.strip() or not cpf.strip():
            st.warning("Nome e CPF são obrigatórios.")
        else:
            try:
                pacientes.insert_one({
                    "nome": nome.strip(), "cpf": cpf.strip(),
                    "data_nascimento": datetime.combine(nascimento, datetime.min.time()),
                    "email": email.strip(), "telefone": telefone.strip(),
                    "criado_em": datetime.now(),
                })
                st.success("Paciente cadastrado com sucesso.")
            except DuplicateKeyError:
                st.error("Já existe um paciente com esse CPF.")
            except PyMongoError as error:
                st.error(f"Erro ao cadastrar: {error}")

with listar:
    busca = st.text_input("Buscar por nome ou CPF")
    filtro = {}
    if busca.strip():
        filtro = {"$or": [
            {"nome": {"$regex": busca.strip(), "$options": "i"}},
            {"cpf": {"$regex": busca.strip(), "$options": "i"}},
        ]}
    registros = list(pacientes.find(filtro, {"_id": 0}).sort("nome", ASCENDING))
    if registros:
        tabela = pd.DataFrame(registros)
        for coluna in ("data_nascimento", "criado_em", "atualizado_em"):
            if coluna in tabela:
                tabela[coluna] = pd.to_datetime(tabela[coluna]).dt.strftime("%d/%m/%Y")
        st.dataframe(tabela, use_container_width=True, hide_index=True)
        st.caption(f"{len(registros)} paciente(s) encontrado(s).")
    else:
        st.info("Nenhum paciente encontrado.")

with editar:
    documentos = list(pacientes.find().sort("nome", ASCENDING))
    if not documentos:
        st.info("Cadastre um paciente antes de editar.")
    else:
        opcoes = {f"{p['nome']} — CPF {p['cpf']}": p for p in documentos}
        atual = opcoes[st.selectbox("Selecione o paciente", list(opcoes), key="editar")]
        with st.form("editar_form"):
            novo_nome = st.text_input("Nome completo", atual.get("nome", ""))
            novo_nascimento = st.date_input(
                "Data de nascimento", as_date(atual.get("data_nascimento")),
                min_value=date(1900, 1, 1),
            )
            novo_email = st.text_input("E-mail", atual.get("email", ""))
            novo_telefone = st.text_input("Telefone", atual.get("telefone", ""))
            salvar = st.form_submit_button("Salvar alterações", type="primary")
        if salvar:
            if not novo_nome.strip():
                st.warning("O nome é obrigatório.")
            else:
                try:
                    pacientes.update_one({"_id": atual["_id"]}, {"$set": {
                        "nome": novo_nome.strip(),
                        "data_nascimento": datetime.combine(novo_nascimento, datetime.min.time()),
                        "email": novo_email.strip(), "telefone": novo_telefone.strip(),
                        "atualizado_em": datetime.now(),
                    }})
                    st.success("Paciente atualizado com sucesso.")
                    st.rerun()
                except PyMongoError as error:
                    st.error(f"Erro ao atualizar: {error}")

with excluir:
    documentos = list(pacientes.find({}, {"nome": 1, "cpf": 1}).sort("nome", ASCENDING))
    if not documentos:
        st.info("Não há pacientes para excluir.")
    else:
        opcoes = {f"{p['nome']} — CPF {p['cpf']}": p for p in documentos}
        escolhido = opcoes[st.selectbox("Selecione o paciente", list(opcoes), key="excluir")]
        confirmado = st.checkbox("Confirmo a exclusão permanente deste registro")
        if st.button("Excluir paciente", type="primary", disabled=not confirmado):
            try:
                pacientes.delete_one({"_id": escolhido["_id"]})
                st.success("Paciente excluído com sucesso.")
                st.rerun()
            except PyMongoError as error:
                st.error(f"Erro ao excluir: {error}")
