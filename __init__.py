import logging
import azure.functions as func
import os
import time
from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient
from opencensus.ext.azure.log_exporter import AzureLogHandler

# Configuração de log com Application Insights
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Application Insights (se estiver ativo na Function App)
conn_str = os.environ.get("APPLICATIONINSIGHTS_CONNECTION_STRING")
if conn_str:
    logger.addHandler(AzureLogHandler(connection_string=conn_str))

# Configurações do Document Intelligence
form_recognizer_endpoint = os.environ.get("https://diandressa.cognitiveservices.azure.com/")
form_recognizer_key = os.environ.get("6TNkrdnBKBXB7M5oywTOj5T29Koaq1067CFZ5D3iw3pJd5dxnJ1gJQQJ99BDACYeBjFXJ3w3AAALACOGZYx4")

credential = AzureKeyCredential(form_recognizer_key)
document_client = DocumentAnalysisClient(endpoint=form_recognizer_endpoint, credential=credential)

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        file = req.files.get('file')

        if not file:
            return func.HttpResponse("Envie um arquivo PDF no campo 'file'.", status_code=400)

        logger.info(f"Recebido arquivo: {file.filename}")

        # Lê o PDF em bytes
        pdf_bytes = file.stream.read()
        start_time = time.time()

        # Chama o Document Intelligence
        poller = document_client.begin_analyze_document(
            model="prebuilt-document",
            document=pdf_bytes,
            content_type="application/pdf"
        )

        result = poller.result()
        elapsed = time.time() - start_time
        logger.info(f"Processamento concluído em {elapsed:.2f} segundos")

        extracted_text = ""
        for page in result.pages:
            for line in page.lines:
                extracted_text += line.content + "\n"

        return func.HttpResponse(f"Texto extraído:\n{extracted_text}", status_code=200)

    except Exception as e:
        logger.exception("Erro ao processar o PDF.")
        return func.HttpResponse("Erro ao processar o PDF.", status_code=500)
