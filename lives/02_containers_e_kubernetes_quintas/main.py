import streamlit as st
import pandas as pd
import numpy as np

# Configuração da página
st.set_page_config(
    page_title="App de Teste",
    page_icon="🧪",
    layout="centered"
)

st.title("🧪 Streamlit de Teste")

st.write("Este é um aplicativo simples para testar o funcionamento do Streamlit.")

# Entrada de texto
nome = st.text_input("Digite seu nome:")

if nome:
    st.success(f"Olá, {nome}! Bem-vindo ao Streamlit.")

# Slider
valor = st.slider("Escolha um valor:", 0, 100, 50)
st.write(f"Valor selecionado: **{valor}**")

# Botão
if st.button("Gerar Dados Aleatórios"):
    dados = pd.DataFrame(
        np.random.randn(20, 3),
        columns=["A", "B", "C"]
    )

    st.subheader("Tabela")
    st.dataframe(dados)

    st.subheader("Gráfico")
    st.line_chart(dados)

# Barra lateral
st.sidebar.header("Menu")
opcao = st.sidebar.selectbox(
    "Escolha uma opção:",
    ["Início", "Sobre", "Contato"]
)

st.sidebar.write(f"Você selecionou: **{opcao}**")

# Rodapé
st.markdown("---")
st.caption("Aplicação de teste desenvolvida com Streamlit.")