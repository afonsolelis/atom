import streamlit as st
import pymongo
from pymongo import MongoClient
import pandas as pd
from datetime import datetime
import os

# Conectar ao MongoDB
@st.cache_resource
def get_database():
    mongo_uri = os.getenv("MONGO_URI", "mongodb://admin:senha123@localhost:27017/livraria?authSource=admin")
    client = MongoClient(mongo_uri)
    db = client["livraria"]
    return db

try:
    db = get_database()
    clientes_collection = db["clientes"]
    st.success("✅ Conectado ao MongoDB!")
except Exception as e:
    st.error(f"❌ Erro ao conectar ao MongoDB: {e}")
    st.stop()

# Sidebar - Menu de navegação
st.sidebar.title("📚 Menu - Livraria")
pagina = st.sidebar.radio("Selecione uma página", ["Adicionar Cliente", "Dashboard de Clientes"])

# ================== PÁGINA 1: ADICIONAR CLIENTE ==================
if pagina == "Adicionar Cliente":
    st.title("➕ Adicionar Novo Cliente")
    
    with st.form("form_cliente"):
        col1, col2 = st.columns(2)
        
        with col1:
            nome = st.text_input("Nome completo", placeholder="João Silva")
            email = st.text_input("Email", placeholder="joao@exemplo.com")
            telefone = st.text_input("Telefone", placeholder="(11) 99999-9999")
        
        with col2:
            cpf = st.text_input("CPF", placeholder="123.456.789-00")
            endereco = st.text_input("Endereço", placeholder="Rua das Flores, 123")
            cidade = st.text_input("Cidade", placeholder="São Paulo")
        
        col3, col4 = st.columns(2)
        with col3:
            estado = st.selectbox("Estado", ["SP", "RJ", "MG", "BA", "RS", "PR", "SC", "PE", "CE", "PA", "GO", "DF", "ES", "MS", "MT", "RO", "AC", "AM", "AP", "RR", "TO"])
        
        with col4:
            cep = st.text_input("CEP", placeholder="01234-567")
        
        categoria = st.selectbox("Categoria de Cliente", ["Regular", "Premium", "VIP"])
        observacoes = st.text_area("Observações", placeholder="Adicione observações sobre o cliente...")
        
        botao_enviar = st.form_submit_button("💾 Cadastrar Cliente", use_container_width=True)
    
    if botao_enviar:
        if not nome or not email:
            st.error("❌ Nome e Email são obrigatórios!")
        else:
            novo_cliente = {
                "nome": nome,
                "email": email,
                "telefone": telefone,
                "cpf": cpf,
                "endereco": endereco,
                "cidade": cidade,
                "estado": estado,
                "cep": cep,
                "categoria": categoria,
                "observacoes": observacoes,
                "data_cadastro": datetime.now(),
                "ativo": True
            }
            
            try:
                resultado = clientes_collection.insert_one(novo_cliente)
                st.success(f"✅ Cliente cadastrado com sucesso! ID: {resultado.inserted_id}")
                st.balloons()
            except Exception as e:
                st.error(f"❌ Erro ao cadastrar cliente: {e}")

# ================== PÁGINA 2: DASHBOARD ==================
elif pagina == "Dashboard de Clientes":
    st.title("📊 Dashboard - Clientes da Livraria")
    
    # Estatísticas
    total_clientes = clientes_collection.count_documents({"ativo": True})
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total de Clientes", total_clientes)
    
    with col2:
        premium = clientes_collection.count_documents({"categoria": "Premium", "ativo": True})
        st.metric("Clientes Premium", premium)
    
    with col3:
        vip = clientes_collection.count_documents({"categoria": "VIP", "ativo": True})
        st.metric("Clientes VIP", vip)
    
    with col4:
        regular = clientes_collection.count_documents({"categoria": "Regular", "ativo": True})
        st.metric("Clientes Regular", regular)
    
    st.divider()
    
    # Filtros
    col_filtro1, col_filtro2 = st.columns(2)
    with col_filtro1:
        filtro_categoria = st.multiselect("Filtrar por Categoria", ["Regular", "Premium", "VIP"], default=["Regular", "Premium", "VIP"])
    
    with col_filtro2:
        filtro_estado = st.multiselect("Filtrar por Estado", ["SP", "RJ", "MG", "BA", "RS", "PR", "SC", "PE", "CE", "PA", "GO", "DF", "ES", "MS", "MT", "RO", "AC", "AM", "AP", "RR", "TO"], default=None)
    
    # Query com filtros
    query = {"ativo": True, "categoria": {"$in": filtro_categoria}}
    if filtro_estado:
        query["estado"] = {"$in": filtro_estado}
    
    clientes = list(clientes_collection.find(query).sort("data_cadastro", -1))
    
    if clientes:
        st.subheader(f"Total encontrado: {len(clientes)} cliente(s)")
        
        # Exibir clientes em cards
        for cliente in clientes:
            with st.container(border=True):
                col_info1, col_info2, col_info3 = st.columns([2, 2, 1])
                
                with col_info1:
                    st.write(f"**👤 {cliente['nome']}**")
                    st.write(f"📧 {cliente['email']}")
                    st.write(f"📞 {cliente['telefone']}")
                
                with col_info2:
                    st.write(f"🏷️ Categoria: **{cliente['categoria']}**")
                    st.write(f"📍 {cliente['cidade']}, {cliente['estado']}")
                    st.write(f"📝 {cliente.get('observacoes', 'N/A')[:50]}...")
                
                with col_info3:
                    if st.button("❌ Deletar", key=str(cliente['_id'])):
                        clientes_collection.update_one({"_id": cliente['_id']}, {"$set": {"ativo": False}})
                        st.rerun()
        
        st.divider()
        
        # Tabela de dados
        st.subheader("📋 Tabela Completa")
        df = pd.DataFrame([{
            "Nome": c["nome"],
            "Email": c["email"],
            "Telefone": c["telefone"],
            "Cidade": c["cidade"],
            "Estado": c["estado"],
            "Categoria": c["categoria"],
            "Data Cadastro": c["data_cadastro"].strftime("%d/%m/%Y")
        } for c in clientes])
        
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        # Gráficos
        st.divider()
        st.subheader("📈 Análises")
        
        col_graf1, col_graf2 = st.columns(2)
        
        with col_graf1:
            st.write("**Clientes por Categoria**")
            categoria_counts = {}
            for c in clientes:
                cat = c["categoria"]
                categoria_counts[cat] = categoria_counts.get(cat, 0) + 1
            
            if categoria_counts:
                st.bar_chart(categoria_counts)
        
        with col_graf2:
            st.write("**Top 10 Estados**")
            estado_counts = {}
            for c in clientes:
                est = c["estado"]
                estado_counts[est] = estado_counts.get(est, 0) + 1
            
            top_estados = dict(sorted(estado_counts.items(), key=lambda x: x[1], reverse=True)[:10])
            if top_estados:
                st.bar_chart(top_estados)
    
    else:
        st.info("ℹ️ Nenhum cliente encontrado com os filtros selecionados.")
    
    # Exportar dados
    st.divider()
    if st.button("📥 Exportar como CSV"):
        if clientes:
            df.to_csv("clientes.csv", index=False)
            st.success("✅ Arquivo exportado como 'clientes.csv'")
