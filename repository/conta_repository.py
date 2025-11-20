from domain.usuario import Usuario
from exception import ContaJaExistenteException
from domain import Conta
from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation

class ContaRepository:
    def __init__(self, db: Session):
        self.__db_contas = db

    def consultar_quantidade_contas_por_cpf_cnpj(self, cpf_cnpj: str) -> int:
        total = (
            self.__db_contas
            .query(func.count())
            .select_from(Conta) # define a tabela principal
            .join(Conta.usuario_dono) # Realizar inner join
            .filter(Usuario.cpf_cnpj == cpf_cnpj) # Realizar o where
            .scalar() # Retorna o valor do count(*)
        )

        return total

    def inserir_conta(self, conta: Conta):
        try:
            usuario_novo = conta.usuario_dono
            self.__db_contas.add(usuario_novo)
            self.__db_contas.commit()
            self.__db_contas.refresh(usuario_novo)
            
            self.__db_contas.add(conta)
            self.__db_contas.commit()
            self.__db_contas.refresh(conta)
            return conta
        except IntegrityError as e:
            self.__db_contas.rollback()
            if isinstance(e.orig, UniqueViolation):
                raise ContaJaExistenteException(conta.numero_conta)
            raise
    
    def consultar_contas(self, numero_conta: int) ->  List[Conta]:
        contas = (self.__db_contas
            .query(Conta)
            .join(Conta.usuario_dono)
            .filter(Conta.numero_conta == numero_conta)
            .all()
        )
        
        return contas
            
    