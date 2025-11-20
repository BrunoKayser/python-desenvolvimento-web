from unittest.mock import MagicMock
import pytest 
from service.conta_service import ContaService
from domain.conta import Conta
from domain.usuario import Usuario
from exception import ContaNaoEncontradaException

NUMERO_CONTA =  "12345678"

def conta_mock(numero_conta: str) -> Conta:
    usuario = Usuario("Fabio Brazza", "021547891", "teste")
    conta = Conta(usuario, "teste", numero_conta, 10)
    return conta

@pytest.fixture
def conta_service():
    db_mock = MagicMock()
    
    service = ContaService(db_mock)
    
    # Mockando os atrivutos de repository e validador
    service._ContaService__repositorio = MagicMock()
    service._ContaService__contaValidator = MagicMock()
    
    return service

def test_consultar_contas_com_sucesso(conta_service):
    
    conta = conta_mock(NUMERO_CONTA)
    
    conta_service._ContaService__repositorio.consultar_contas.return_value = [conta]
    
    resultado = conta_service.consultar_contas(NUMERO_CONTA)
    
    assert resultado == [conta]
    conta_service._ContaService__repositorio.consultar_contas.assert_called_once_with(NUMERO_CONTA)
    
def test_consultar_contas_nao_encontrada(conta_service):

    conta_service._ContaService__repositorio.consultar_contas.return_value = []
    
    with pytest.raises(ContaNaoEncontradaException) as exception:
        exception = conta_service.consultar_contas(NUMERO_CONTA)
        
    assert str(exception.value) == 'Conta 12345678 não encontrada.'
    conta_service._ContaService__repositorio.consultar_contas.assert_called_once_with(NUMERO_CONTA)

def test_deve_inserir_com_sucesso(conta_service):
    quantidade_de_contas = 1    
    conta = conta_mock("12345678")
    
    conta_service._ContaService__repositorio.consultar_quantidade_contas_por_cpf_cnpj.return_value = quantidade_de_contas
    conta_service._ContaService__contaValidator.validar_quantidade_maximo_de_conta.return_value = False
    
    resultado = conta_service.inserir_conta(conta)
    
    assert resultado == conta
    conta_service._ContaService__repositorio.consultar_quantidade_contas_por_cpf_cnpj.assert_called_once_with(conta.usuario_dono.cpf_cnpj)
    conta_service._ContaService__contaValidator.validar_quantidade_maximo_de_conta.assert_called_once_with(quantidade_de_contas, conta.usuario_dono.cpf_cnpj)
    conta_service._ContaService__repositorio.inserir_conta.assert_called_once_with(conta)

    
