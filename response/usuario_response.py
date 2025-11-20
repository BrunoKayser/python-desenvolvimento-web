from datetime import datetime, timezone
from pydantic import BaseModel, Field
from typing import Optional

class UsuarioResponse(BaseModel):
    model_config = {
        "json_encoders": { # Formatar todos os dateTime para o formato que desejo
            datetime: lambda dt: dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        }
    }
    
    nome: str= Field(
        description="Nome completo do usuário cadastrado.",
        example="João da Silva"
    )
    cpf_cnpj: str = Field(
        description="Documento identificador do usuário (CPF ou CNPJ).",
        example="12345678900"
    )
    is_ativo: bool= Field(
        description="Indica se o usuário está ativo no sistema.",
        example=True
    )
    data_criacao: datetime= Field(
        description="Data e hora em que o usuário foi criado.",
        example="2024-05-20T14:35:00Z"
    )
    inserido_por: str= Field(
        description="Identificador ou nome de quem criou o registro do usuário.",
        example="admin_user"
    )
    alterado_por: Optional[str] = Field(
        None,
        description="Identificador ou nome de quem fez a última alteração, se houver.",
        example="joao_editor"
    )
    data_alteracao: Optional[datetime] = Field(
        None,
        description="Data e hora da última modificação do registro, se houver.",
        example="2024-06-15T09:20:00Z"
    )
 