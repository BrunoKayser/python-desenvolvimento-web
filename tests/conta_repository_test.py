from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from sqlalchemy import func
from unittest import mock
from domain.conta import Conta
from domain.usuario import Usuario
from repository.conta_repository import ContaRepository

# Criando banco de dados virtual
conta_mock = Conta(
                Usuario("Bruno Kayser", "01221545610", "mock teste"), 
                "mock teste",
                "21354879",
                10)

count_function = func.count()

db_contas =  UnifiedAlchemyMagicMock(
    data = [
        # Adicionando um objeto para ser retornado no banco virtual
        (
            # condição para o dado virtualizado
            [
                mock.call.query(Conta),
                mock.call.join(Conta.usuario_dono),
                mock.call.filter(Conta.numero_conta == "21354879")
            ], 
            # Dado virtualizado retornado ao filtro acima
            [
                conta_mock
            ]
        ),
        # Adicionando segundo objeto
        (
            # condição para o dado virtualizado
            [
                mock.call.query(mock.ANY),
                mock.call.select_from(Conta),
                mock.call.join(Conta.usuario_dono),
                mock.call.filter(Usuario.cpf_cnpj == "01221545610"),
                mock.call.scalar()
            ], 
            # Dado virtualizado retornado ao filtro acima
            1
        )
    ]
)

# No teste de de consulta precisa mockar todas as operações que consulta o banco de dados  
def test_consultar_contas():
    
    repository = ContaRepository(db_contas)
    
    response = repository.consultar_contas("21354879")
        
    print(f'\nRetorno consulta do banco: {response}')
    assert response[0] == conta_mock
    
    #Validando os métodos sendo chamados 
    db_contas.assert_has_calls([
        mock.call.query(Conta),
        mock.call.query(Conta).join(Conta.usuario_dono),
        mock.call.query(Conta).join(Conta.usuario_dono).filter(Conta.numero_conta == "21354879")
    ])
    
# No teste de inserir não precisou mockar nada por que não foi feito nenhuma operação de consulta na base
def test_inserir_conta():
    repository =  ContaRepository(db_contas)
    response = repository.inserir_conta(conta_mock)
    
    print(f'Objeto inserido: {response}')
    
    db_contas.assert_has_calls([
        mock.call.add(conta_mock.usuario_dono),
        mock.call.commit(),
        mock.call.refresh(conta_mock.usuario_dono),
        mock.call.add(conta_mock),
        mock.call.commit(),
        mock.call.refresh(conta_mock)
    ])