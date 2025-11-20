from exception import QuantidadeMaximaDeContaException

class ContaValidator:
    def __init__(self):
        pass
            
    def validar_quantidade_maximo_de_conta(self, quantidade: int, cpf_cnpj: str):
        if quantidade > 1:
            raise QuantidadeMaximaDeContaException(f"Usuário {cpf_cnpj} ja possui duas contas cadastradas")