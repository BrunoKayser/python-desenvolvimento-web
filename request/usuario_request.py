from pydantic import BaseModel, field_validator, Field
from exception import BadRequestException
import re

class UsuarioRequest(BaseModel):
    nome: str = Field(description="Nome do dono da conta", example="Bruno Kayser")
    cpf_cpnj: str = Field(description="cpf ou cnpj do usuário dono", example="00112233445")
    
    @field_validator("cpf_cpnj")
    def validar_cpf_cnpj(cls, value: str):
        if not re.fullmatch('^\d{11}$|^\d{14}$', value):
            raise BadRequestException("cpf_cnpj", value)
        
        return value
    
    @field_validator("nome")
    def validar_nome(cls, value: str):
        if not re.fullmatch("^[A-Za-zÀ-ÖØ-öø-ÿ]+(?:[ '\-][A-Za-zÀ-ÖØ-öø-ÿ]+)*$", value):
            raise BadRequestException("nome", value)
        
        return value