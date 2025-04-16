# Usar a imagem base do Azure Functions para Python
FROM mcr.microsoft.com/azure-functions/python:4-python3.9

# Definir o diretório de trabalho no container
WORKDIR /home/site/wwwroot

# Copiar todos os arquivos do projeto para o diretório de trabalho no container
COPY . .

# Instalar dependências de forma mais robusta e garantir que a versão do pip seja atualizada
RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Definir as variáveis de ambiente para o Azure Functions runtime
ENV AzureWebJobsScriptRoot=/home/site/wwwroot
ENV FUNCTIONS_WORKER_RUNTIME=python

# Expor a porta 80 (padrão para containers)
EXPOSE 80

# Comando para iniciar o worker do Azure Functions
CMD ["python", "-m", "azure.functions.worker"]
