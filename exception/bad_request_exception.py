class BadRequestException(Exception):
    def __init__(self, campo, valor):
        self.__http_status_code = 400
        self.__mensagem_de_erro = f'Campo {campo} possui valor {valor} inválido'
        pass
    
    def get_http_status_code(self):
        return self.__http_status_code
    
    def get_mensagem_de_erro(self):
        return self.__mensagem_de_erro