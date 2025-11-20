from request import ContaRequest
from response import UsuarioResponse, ContaResponse
from domain import Conta, Usuario
from typing import List

class ContaMapper:
    def __init__(self):
        pass
    
    def to_conta(self, contaRequest: ContaRequest):
        usuario = Usuario(
            contaRequest.usuario_dono.nome,
            contaRequest.usuario_dono.cpf_cpnj,
            contaRequest.inserido_por)
        return Conta(usuario, contaRequest.inserido_por, contaRequest.numero_conta, contaRequest.numero_agencia)
    
    def conta_to_response_json(self, conta_domain: Conta):
        usuario_response = UsuarioResponse(
            nome=conta_domain.usuario_dono.nome,
            cpf_cnpj=conta_domain.usuario_dono.cpf_cnpj,
            is_ativo=conta_domain.usuario_dono.is_ativo,
            data_criacao=conta_domain.usuario_dono.data_criacao,
            inserido_por=conta_domain.usuario_dono.inserido_por
        ).model_dump()

        conta_response = ContaResponse(
            saldo=conta_domain.saldo,
            usuario_dono=usuario_response,
            numero_conta=conta_domain.numero_conta,
            numero_agencia=conta_domain.numero_agencia,
            is_ativo=conta_domain.is_ativo,
            data_criacao=conta_domain.data_criacao,
            inserido_por=conta_domain.inserido_por
        ).model_dump()

        return conta_response
    
    def contas_to_response_json(self, contas_domain: List[Conta]):
        contas_json = []
        for conta in contas_domain:
            contas_json.append(self.conta_to_response_json(conta))
        
        return contas_json
    #  return [self.conta_to_response_json(conta) for conta in contas_domain]
        