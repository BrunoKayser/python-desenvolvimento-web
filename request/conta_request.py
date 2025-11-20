from request.usuario_request import UsuarioRequest
from exception.bad_request_exception import BadRequestException
from pydantic import BaseModel, field_validator, Field

class ContaRequest(BaseModel):
    usuario_dono: UsuarioRequest
    numero_agencia: int = Field(description="Número da agência, deve ser um valor maior que zero.", example="1")
    numero_conta: int = Field(description="Número da conta, deve ser um valor maior que zero e 8 digitos", example="56489745")
    inserido_por: str = Field(description="Usuário que insere o registro", example="admin_user")
    
    @field_validator("usuario_dono")
    def validar_usuario_dono(cls, value):
        if value == None or not isinstance(value, UsuarioRequest):
            raise BadRequestException("usuario_dono", value)
        
        return value

    @field_validator("inserido_por")
    def validar_inserido_por(cls, value):
        if value == None:
            raise BadRequestException("inserido_por", value)   
        
        return value
    
    @field_validator("numero_agencia")
    def validar_agencia(cls, value):
        if value == None or value <= 0:
            raise BadRequestException("numero_agencia", value)   
        
        return value
    
    @field_validator("numero_conta")
    def validar_conta(cls, value):
        if value == None or value <= 0 or len(str(value)) != 8:
            raise BadRequestException("numero_conta", value)   
        
        return value