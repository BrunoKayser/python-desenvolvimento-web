from response.error_response import BadRequestErrorResponse, UnantenticatedErrorResponse, NotFoundErrorResponse ,UnprocessableErrorResponse, InternalServerErrorResponse

def responses_create():
        return {
            400: {"description": "Bad Request","example": "Campo 'usuario_dono' não pode ser nulo.", "model": BadRequestErrorResponse},
            401: {"description": "Não autorizado","model": UnantenticatedErrorResponse},
            404: {"description": "Recurso não encontrado", "model": NotFoundErrorResponse},
            422: {"description": "Erro de negócio", "model": UnprocessableErrorResponse},
            500: {"description": "Erro interno do servidor", "model": InternalServerErrorResponse} 
        }  
        
def responses_get():
        return {
            401: {"description": "Não autorizado","model": UnantenticatedErrorResponse},
            404: {"description": "Recurso não encontrado", "model": NotFoundErrorResponse},
            422: {"description": "Erro de negócio", "model": UnprocessableErrorResponse},
            500: {"description": "Erro interno do servidor", "model": InternalServerErrorResponse} }  