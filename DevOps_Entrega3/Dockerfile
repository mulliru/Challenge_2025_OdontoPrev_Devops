# Usa uma imagem Python como base
FROM python:3.12-slim

# Instala os pacotes necessários, incluindo o ODBC Driver 18 para SQL Server
RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    apt-transport-https \
    unixodbc \
    unixodbc-dev \
    libssl-dev \
    && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql18 \
    && apt-get clean

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos da aplicação para o container
COPY app /app

# Instala as dependências do Python
RUN pip install --no-cache-dir -r /app/requirements.txt

# Define o comando de inicialização
CMD ["python", "/app/app.py"]
