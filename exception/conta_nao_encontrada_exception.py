class ContaNaoEncontradaException(Exception):
    def __init__(self, mensagem_de_erro):
        self.__http_status_code = 422
        self.__mensagem_de_erro = mensagem_de_erro
        pass
        
    def get_http_status_code(self):
        return self.__http_status_code
    
    def get_mensagem_de_erro(self):
        return self.__mensagem_de_erro