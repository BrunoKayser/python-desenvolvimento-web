from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, Numeric, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from config.database import Base

class Usuario(Base):
# Os atributos não estão como privado por que modificam o nome do atributo com o "__", 
# assim sendo não é desta maneira que desejamos as colunas no banco de dados
# por isso todos os campos ficam como publicos
    def __init__(self, nome, cpf_cnpj, inserido_por):
        self.nome = nome
        self.cpf_cnpj = cpf_cnpj
        self.is_ativo = True
        self.data_criacao = datetime.now()
        self.inserido_por = inserido_por
        self.alterado_por = None
        self.data_alteracao = None
        
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    cpf_cnpj = Column(String(14), nullable=False)
    is_ativo = Column(Boolean, nullable=False)
    data_criacao = Column(DateTime, default=datetime.now)
    inserido_por = Column(String(160), nullable=False)
    alterado_por = Column(String(160), nullable=True)
    data_alteracao = Column(DateTime, nullable=True)

    contas = relationship("Conta", back_populates="usuario_dono")
