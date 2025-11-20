class ContaJaExistenteException(Exception):
    def __init__(self, valor):
        self.__http_status_code = 422
        self.__mensagem_de_erro = f'Número de conta {valor} ja cadastrado na base'
        pass
    
    def get_http_status_code(self):
        return self.__http_status_code
    
    def get_mensagem_de_erro(self):
        return self.__mensagem_de_erro