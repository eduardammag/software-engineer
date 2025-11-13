from functools import wraps #Decorador que decora um decorador para manter as coisas da função original


# Alterar o funcionamento da funcção, por exemplo mudar o return
def dobrar_retorno(func):
    def wrapper(*args, **kwargs):  # Envelopador , *args= arg nomeados, **kwargs = args não nomeados
        resultado = func(*args, **kwargs)
        return resultado* 2 #Vai copiar a funcionamento da função
    
    return wrapper 


# Registrar os argumentos que foram usados na função
def log_args(func):
    @wraps(func) #Decorador que decora a função wrapper para manter as coisas da função original
    def wrapper(*args, **kwargs):  # Envelopador , *args= arg nomeados, **kwargs = args não nomeados
        print(f"Chamando função {func.__name__} com args = {args} e kwarg = {kwargs}")
        return func(*args, **kwargs) #Vai copiar a funcionamento da função
    
    return wrapper

# decorar duas vezes
# Problema o decorador oculta a função original, nesse caso a função printada é wrapper
# Para resolver, importamos  wraps
@log_args
@dobrar_retorno # O decorador recebe sempre a função abaixo e altera a função, o mais interno é sempre altera primeiro
def soma_1(a, b):
    """
    Esta função soma!

    Parameters
    -----------
    a: TYPE
    b: TYPE
    """
    return a + b

@log_args
def soma_2(a, b, c):
    """
    Esta função soma!

    Parameters
    -----------
    a: TYPE
    b: TYPE
    c: TYPE
    """
    return a + b + c

print("Resultado:", soma_1(42, 666)) # É como se tivessemos wrapper(42, 666) depois de decorado com log_args
print("Resultado:", soma_2(13, 42, 666))

print(soma_2.__name__)