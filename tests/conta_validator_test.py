import pytest
from validator.conta_validator import ContaValidator
from exception import QuantidadeMaximaDeContaException
CPF = '12354685487'

def test_validar_quantidade_maximo_de_conta_sem_excecao():
    conta_validator = ContaValidator()
    
    conta_validator.validar_quantidade_maximo_de_conta(1, CPF)
    
def test_validar_quantidade_maximo_de_conta_com_excecao_quando_cpf_ter_mais_de_uma_conta():
    conta_validator = ContaValidator()
    
    with pytest.raises(QuantidadeMaximaDeContaException) as exception:
        conta_validator.validar_quantidade_maximo_de_conta(2, CPF)

    assert str(exception.value) == f"Usuário {CPF} ja possui duas contas cadastradas"