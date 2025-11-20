from pydantic import BaseModel, Field
from datetime import datetime

class BadRequestErrorResponse(BaseModel):
    mensagem: str = Field(
        ...,
        title="Mensagem de erro",
        description="Descrição do motivo do erro retornado pela API.",
        example="Campo 'usuario_dono' não pode ser nulo."
    )
    data_hora: datetime = Field(
        ...,
        title="Data/hora da ocorrência do erro.",
        description="Horário no formato yyyy-MM-ddTHH:mm.ss",
        example="2025-11-08T14:32.03Z"
    )

class UnantenticatedErrorResponse(BaseModel):
    mensagem: str = Field(
        ...,
        title="Mensagem de erro",
        description="Descrição do motivo do erro retornado pela API.",
        example="Usuário não autentitcado"
    )
    data_hora: datetime = Field(
        ...,
        title="Data/hora da ocorrência do erro.",
        description="Horário no formato yyyy-MM-ddTHH:mm.ss",
        example="2025-11-08T14:32.03Z"
    )
    
class NotFoundErrorResponse(BaseModel):
    mensagem: str = Field(
        ...,
        title="Mensagem de erro",
        description="Descrição do motivo do erro retornado pela API.",
        example="Recurso não encontrado"
    )   
    data_hora: datetime = Field(
        ...,
        title="Data/hora da ocorrência do erro.",
        description="Horário no formato yyyy-MM-ddTHH:mm.ss",
        example="2025-11-08T14:32.03Z"
    )
    
class UnprocessableErrorResponse(BaseModel):
    mensagem: str = Field(
        ...,
        title="Mensagem de erro",
        description="Descrição do motivo do erro retornado pela API.",
        example="'Conta 1234 não encontrada."
    )   
    data_hora: datetime = Field(
        ...,
        title="Data/hora da ocorrência do erro.",
        description="Horário no formato yyyy-MM-ddTHH:mm.ss",
        example="2025-11-08T14:32.03Z"
    )
    
class InternalServerErrorResponse(BaseModel):
    mensagem: str = Field(
        ...,
        title="Mensagem de erro",
        description="Descrição do motivo do erro retornado pela API.",
        example="Erro interno do servidor"
    )   
    data_hora: datetime = Field(
        ...,
        title="Data/hora da ocorrência do erro.",
        description="Horário no formato yyyy-MM-ddTHH:mm.ss",
        example="2025-11-08T14:32.03Z"
    )