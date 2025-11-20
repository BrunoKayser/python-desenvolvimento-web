from response.usuario_response import UsuarioResponse
from datetime import datetime, timezone
from pydantic import BaseModel, Field
from typing import Optional

class ContaResponse(BaseModel):
    model_config = {
        "json_encoders": { # Formatar todos os dateTime para o formato que desejo
            datetime: lambda dt: dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        }
    }
    
    saldo: float = Field(
        description="Valor atual do saldo da conta.",
        example=00.00
    )
    
    usuario_dono: UsuarioResponse
    
    is_ativo: bool = Field(
        description="Indica se a conta está ativa no sistema.",
        example=True
    )
    numero_agencia: int = Field(
        description="Número da agência, deve ser um valor maior que zero.",
        example="0001"
    )
    numero_conta: int = Field(
        description="Número da conta, deve ser um valor maior que zero.",
        example="56489745"
    )
    data_criacao: datetime = Field(
        description="Data e hora em que a conta foi criada.",
        example="2024-05-20T14:35:00Z"
    )
    inserido_por: str = Field(
        description="Identificador ou nome do usuário responsável pela criação da conta.",
        example="admin_user"
    )
    alterado_por: Optional[str] = Field(
        None,
        description="Identificador ou nome de quem realizou a última modificação, se houver.",
        example="joao_editor"
    )
    data_alteracao: Optional[datetime] = Field(
        None,
        description="Data e hora da última modificação do registro da conta, se houver.",
        example="2024-06-15T09:20:00Z"
    )