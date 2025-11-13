# Fazer o decorador insistir na execução da função mais de uma vez
from functools import wraps

# Executar uma função até que a função tennha uma quantidade de tentativas
# Decorador que é uma fábrica de decoradores, ao gerar ele gera um dec aplicado a função já
def retry(retries = 3, exceptions = (Exception,), delay = 0.0, backoff = 1.0):
    # Validar os parametros passados para o decorador
    if not isinstance(retries, int) or retries < 1:
        raise ValueError("Retries deve ser int >= 1")
    if not isinstance(delay, (int, float)) or delay < 0:
        raise ValueError("Delay deve ser int ou float >= 0")
    if not isinstance(backoff, (int, float)) or backoff < 1:
        raise ValueError("backoff deve ser int ou float >= 1")
    
    if not isinstance(exceptions, tuple): # Verifica se não é instancia de uma tupla
        # Se não for uma tupla, transformamos em uma tupla
        exceptions = (exceptions, )

        # Verficamos se o que foi passado é uma esceção
    for exc in exceptions:
        if not (isinstance(exc, type) and issubclass(exc, BaseException)): # Perguna se é um objeto, se tem um tipo E se é uma exceção
            raise ValueError("Exceção deve ser classe derivada de BaseExcecption")
        
    # Tudo isso acima ainda não é o decorador, é apenas a verificação dos parametros
    def decorator(func):
        @wraps(func)
        def wrapper(*arg, **kwargs):
            tentativa_atual = 1
            atraso_atual = float(delay) # Caso seja int, convertemos para float

            while True:
                try:
                    return func(*arg, **kwargs) 
                except exceptions as err:
                    # O decorador só vai fazer algo se acair aqui
                    if tentativa_atual >= retries:
                        raise
                    pass # TODO COMPLETAR


        return wrapper
    return decorator
    


# Função que falha duas vezes e depois funciona
# Driver Code
contador = {"falhas": 0}

@retry(retries = 3, exceptions = (ValueError,), delay = 0.1, backoff = 2.0) # Numero de tentativas = 3 e as exceções que o decorador vai suportar, quantos tento antes de tentar de novo, a cada vez que espera, dobra o tempo esperado 
def pode_falhar(): # Simula um banco que pode ter erro
    if contador["falhas"] < 2:
        contador["falhas"] +=1
        raise ValueError("Falhou!")
    return "Ok!"

print(pode_falhar())