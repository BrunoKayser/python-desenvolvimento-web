from datetime import datetime
from domain.usuario import Usuario
from sqlalchemy import Column, Integer, String, Boolean, Numeric, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from config.database import Base

class Conta(Base):
# Os atributos não estão como privado por que modificam o nome do atributo com o "__", 
# assim sendo não é desta maneira que desejamos as colunas no banco de dados
# por isso todos os campos ficam como publicos
    def __init__(self, usuario_dono: Usuario, inserido_por, conta: int, agencia: int):
        self.saldo = 0.00
        self.usuario_dono = usuario_dono
        self.numero_conta = conta
        self.numero_agencia = agencia
        self.is_ativo = True
        self.data_criacao = datetime.now()
        self.inserido_por = inserido_por
        self.alterado_por = None
        self.data_alteracao = None

    __tablename__ = "conta"

    id = Column(Integer, primary_key=True, index=True)
    saldo = Column(Numeric(15, 2), default=0.00)
    usuario_dono_id = Column(Integer, ForeignKey("usuario.id"), nullable=False)
    numero_conta = Column(Integer, nullable=False, unique=True)
    numero_agencia = Column(Integer, nullable=False)
    is_ativo = Column(Boolean, nullable=False)
    data_criacao = Column(DateTime, default=datetime.now)
    inserido_por = Column(String(160), nullable=False)
    alterado_por = Column(String(160), nullable=True)
    data_alteracao = Column(DateTime, nullable=True)

    usuario_dono = relationship("Usuario", back_populates="contas")
