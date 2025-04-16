import logging
import azure.functions as func
from .ocr import run_ocr

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Início da função OCR")

    file = req.files.get('file')
    document_id = req.params.get('documentId', 'desconhecido')

    if not file:
        logging.warning(f"[{document_id}] Nenhum arquivo enviado.")
        return func.HttpResponse("Arquivo não enviado", status_code=400)

    try:
        logging.info(f"[{document_id}] Iniciando processamento OCR")
        status = run_ocr(file.read(), document_id)
        return func.HttpResponse(f"OCR concluído: {status}", status_code=200)
    except Exception as e:
        logging.exception(f"[{document_id}] Erro no OCR: {str(e)}")
        return func.HttpResponse("Erro no processamento", status_code=500)
