import logging
import azure.functions as func
from . import app  # must use relative import here


def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    return func.WsgiMiddleware(app.app.wsgi_app).handle(req, context)
