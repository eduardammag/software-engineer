from functools import wraps #Decorador que decora um decorador para manter as coisas da função original
import time
# EXERCICIO: Registrar o tempo que leva para executar


# Registrar os argumentos que foram usados na função
def medir_tempo(func):
    @wraps(func) #Decorador que decora a função wrapper para manter as coisas da função original
    def wrapper(*args, **kwargs):  # Envelopador , *args= arg nomeados, **kwargs = args não nomeados
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f" A função {func.__name__} exwcutada em {fim-inicio:.4f} segundos")
        return func(*args, **kwargs) #Vai copiar a funcionamento da função
    
    return wrapper


@medir_tempo 
def soma(a, b):
    """
    Esta função soma!

    Parameters
    -----------
    a: TYPE
        number 1
    b: TYPE
        number 2
    """
    time.sleep(1)
    return a + b


print("Resultado:", soma(42, 666)) # É como se tivessemos wrapper(42, 666) depois de decorado com log_args
