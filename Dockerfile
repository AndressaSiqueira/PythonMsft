# Usar a imagem base do Azure Functions para Python
FROM mcr.microsoft.com/azure-functions/python:4-python3.9

# Definir o diretório de trabalho
WORKDIR /home/site/wwwroot

# Copiar todos os arquivos para o container
COPY . .

# Criar e ativar um ambiente virtual
RUN python -m venv /home/site/wwwroot/.venv

# Ativar o ambiente virtual e instalar dependências
RUN /bin/bash -c "source /home/site/wwwroot/.venv/bin/activate && pip install -r requirements.txt"

# Definir a variável de ambiente para o worker runtime do Azure Functions
ENV AzureWebJobsScriptRoot=/home/site/wwwroot
ENV FUNCTIONS_WORKER_RUNTIME=python
ENV PATH="/home/site/wwwroot/.venv/bin:$PATH"  # Garantir que o venv seja usado

# Expor a porta 80 (padrão para containers)
EXPOSE 80

# Comando para iniciar o servidor da função
CMD ["python", "-m", "azure.functions.worker"]
