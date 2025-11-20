from repository.conta_repository import ContaRepository 
from exception import ContaNaoEncontradaException
from domain import Conta
from validator.conta_validator import ContaValidator
from sqlalchemy.orm import Session
from typing import List

class ContaService:
    def __init__(self, db: Session):
        self.__repositorio = ContaRepository(db)
        self.__contaValidator = ContaValidator()
    
    def inserir_conta(self, conta: Conta) -> Conta:
        self.__contaValidator.validar_quantidade_maximo_de_conta(
            self.__repositorio.consultar_quantidade_contas_por_cpf_cnpj(conta.usuario_dono.cpf_cnpj),
            conta.usuario_dono.cpf_cnpj)
        self.__repositorio.inserir_conta(conta)
        return conta
        
    def consultar_contas(self, numero_conta: int) ->  List[Conta]:
        contas = self.__repositorio.consultar_contas(numero_conta)
        
        if contas == None or len(contas) == 0:
            raise ContaNaoEncontradaException(f'Conta {numero_conta} não encontrada.') 
        else:
            return contas       
