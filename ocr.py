import requests
import time
import logging
from metrics import track_ocr_time

ENDPOINT = "https://ocrdessa.cognitiveservices.azure.com/"
API_KEY = "6cVoxW5BQt1dFVtCIsCtjzQyIMuH5I3sL0FZrq5h7GIKJ8s0HlhMJQQJ99BDACYeBjFXJ3w3AAAFACOG1Ybm"
OCR_URL = f"{ENDPOINT}formrecognizer/documentModels/prebuilt-document:analyze?api-version=2023-07-31"

def run_ocr(file_bytes, document_id):
    headers = {
        "Ocp-Apim-Subscription-Key": API_KEY,
        "Content-Type": "application/pdf"
    }

    start = time.perf_counter()
    response = requests.post(OCR_URL, headers=headers, data=file_bytes)
    elapsed = (time.perf_counter() - start) * 1000

    logging.info(f"[{document_id}] OCR em {elapsed:.2f}ms")
    track_ocr_time(elapsed)

    response.raise_for_status()
    return response.json().get("status", "Desconhecido")
