from fastapi import FastAPI, Depends, Path
from fastapi.exceptions import RequestValidationError
from sqlalchemy.orm import Session
from config.database import Base, engine, get_db

from service.conta_service import ContaService
from request import ContaRequest
from response import ContaResponse
from mapper.conta_mapper import ContaMapper
from exception import BadRequestException, QuantidadeMaximaDeContaException, ContaNaoEncontradaException, ContaJaExistenteException
from typing import List

import controller.responses_default_swagger as default_responses

app = FastAPI()     
Base.metadata.create_all(bind=engine)

# Manipulação  global de exception, importo todosos métodos que tratam a exceção, e abaixo faço o bind das exceptions capturadas com a exceção a lançar 
from exception.exception_handler import (
    validation_exception_handler,
    bad_request_exception,
    quantidade_maxima_exception,
    conta_nao_encontrada_exception,
    conta_ja_existente_exception
)

# De para com exception capturada com o que deve fazer
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(BadRequestException, bad_request_exception)
app.add_exception_handler(QuantidadeMaximaDeContaException, quantidade_maxima_exception)
app.add_exception_handler(ContaNaoEncontradaException, conta_nao_encontrada_exception)
app.add_exception_handler(ContaJaExistenteException, conta_ja_existente_exception)
     
@app.post(
    "/contas",
    tags = ["Contas"],
    status_code = 201,
    response_model = ContaResponse,
    responses = default_responses.responses_create(),
    summary = "Cria uma nova conta",
    description = "Endpoint responsável por criar uma conta com validação de dados e regras de negócio.",
    response_model_exclude_none = True)
def criar_conta(conta_request: ContaRequest, db: Session = Depends(get_db)):
    service = ContaService(db)
    mapper = ContaMapper()
    conta = mapper.to_conta(conta_request)
    service.inserir_conta(conta)
    return mapper.conta_to_response_json(conta)

@app.get(
    "/contas/{numero_conta}",
    tags = ["Contas"],
    status_code = 200,
    response_model = List[ContaResponse],
    responses = default_responses.responses_get(),
    summary = "Consultar uma conta",
    description = "Serviço para consultar informações de uma única conta",
    response_model_exclude_none = True)
def consultar_contas(numero_conta: int = Path(example=12345678), db: Session = Depends(get_db)):
    service = ContaService(db)
    mapper = ContaMapper()
    contas = service.consultar_contas(numero_conta)
    return mapper.contas_to_response_json(contas)