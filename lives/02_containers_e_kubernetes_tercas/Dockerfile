# Use imagem base Python oficial
FROM python:3.11-slim

# Define diretório de trabalho
WORKDIR /app

# Copia requirements.txt e instala dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia arquivos da aplicação
COPY app.py .

# Expõe porta do Streamlit (padrão: 8501)
EXPOSE 8501

# Variáveis de ambiente para Streamlit
ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0
ENV STREAMLIT_SERVER_HEADLESS=true

# Comando para rodar a aplicação
CMD ["streamlit", "run", "app.py"]
