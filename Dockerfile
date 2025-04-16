# Usar a imagem base do Azure Functions para Python
FROM mcr.microsoft.com/azure-functions/python:4-python3.9

# Definir o diretório de trabalho
WORKDIR /home/site/wwwroot

# Copiar todos os arquivos para o container
COPY . .

# Criar um ambiente virtual e ativá-lo
RUN python3 -m venv .venv

# Instalar dependências no ambiente virtual
RUN . .venv/bin/activate && pip install -r requirements.txt

# Definir as variáveis de ambiente para o runtime do Azure Functions
ENV AzureWebJobsScriptRoot=/home/site/wwwroot
ENV FUNCTIONS_WORKER_RUNTIME=python

# Expor a porta 80 (padrão para containers)
EXPOSE 80

# Comando para iniciar a função, garantindo que o ambiente virtual seja ativado
CMD ["/bin/bash", "-c", "source .venv/bin/activate && python -m azure.functions.worker"]
