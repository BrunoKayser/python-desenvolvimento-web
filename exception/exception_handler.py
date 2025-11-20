from exception import BadRequestException, QuantidadeMaximaDeContaException, ContaNaoEncontradaException, ContaJaExistenteException
from datetime import datetime

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

class ExceptionHandler(Exception):
    def __init__(self, message: str):
        self.message = message    

async def validation_exception_handler(request, exc: RequestValidationError):        
    mensagem_na_exception = exc.errors()[0] 
    mensagem_erro_formatada = f'Campo {mensagem_na_exception["loc"][-1]} possui valor {mensagem_na_exception["type"]} inválido'
    print(f'Erro no response: {mensagem_erro_formatada}')

    return JSONResponse(
        status_code = 400,
        content = {
                    "mensagem": mensagem_erro_formatada,
                    "data_hora": datetime.now().strftime("%Y-%m-%dT%H:%M.%SZ")
                }
    )    
        
async def bad_request_exception(request: Request, exception: BadRequestException):
    return JSONResponse(
        status_code = exception.get_http_status_code(),
        content = {
                    "mensagem": exception.get_mensagem_de_erro(),
                    "data_hora": datetime.now().strftime("%Y-%m-%dT%H:%M.%SZ")
                }
    )

async def quantidade_maxima_exception(request: Request, exception: QuantidadeMaximaDeContaException):
    return JSONResponse(
        status_code = exception.get_http_status_code(),
        content = {
                    "mensagem": exception.get_mensagem_de_erro(),
                    "data_hora": datetime.now().strftime("%Y-%m-%dT%H:%M.%SZ")
                }
    )

async def conta_nao_encontrada_exception(request: Request, exception: ContaNaoEncontradaException):
    return JSONResponse(
        status_code = exception.get_http_status_code(),
        content = {
                    "mensagem": exception.get_mensagem_de_erro(),
                    "data_hora": datetime.now().strftime("%Y-%m-%dT%H:%M.%SZ")
            }
    )
 
async def conta_ja_existente_exception(request: Request, exception: ContaJaExistenteException):
    return JSONResponse(
        status_code = exception.get_http_status_code(),
        content = {
                    "mensagem": exception.get_mensagem_de_erro(),
                    "data_hora": datetime.now().strftime("%Y-%m-%dT%H:%M.%SZ")
                }
    )