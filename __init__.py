import logging
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('⚙️ Requisição recebida.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            req_body = {}
        name = req_body.get('name')

    if name:
        logging.info(f'✅ Nome recebido: {name}')
        return func.HttpResponse(f"Olá, {name}!", status_code=200)
    else:
        logging.warning('❌ Nome não fornecido.')
        return func.HttpResponse(
            "Por favor envie um parâmetro 'name'.",
            status_code=400
        )
