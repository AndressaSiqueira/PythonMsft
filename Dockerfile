# Escolher uma imagem base com Python
FROM python:3.9-slim

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar o arquivo de dependências (requirements.txt)
COPY requirements.txt .

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante da aplicação para dentro do container
COPY . .

# Expor a porta 5000 (ou a porta que a aplicação usa)
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "app.py"]
