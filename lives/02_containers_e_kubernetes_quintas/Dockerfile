FROM python:3.12-slim

# Evita geração de arquivos .pyc e melhora logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Diretório da aplicação
WORKDIR /app

# Copia os arquivos
COPY . /app

# Instala as dependências
RUN pip install --no-cache-dir streamlit pandas numpy

# Expõe a porta padrão do Streamlit
EXPOSE 8501

# Executa a aplicação
CMD ["streamlit", "run", "main.py", "--server.address=0.0.0.0", "--server.port=8501"]