# Alterar o funcionamento da funcção, por exemplo mudar o return
def dobrar_retorno(func):
    def wrapper(*args, **kwargs):  # Envelopador , *args= arg nomeados, **kwargs = args não nomeados
        resultado = func(*args, **kwargs)
        return resultado* 2 #Vai copiar a funcionamento da função
    
    return wrapper 


# Registrar os argumentos que foram usados na função
def log_args(func):
    def wrapper(*args, **kwargs):  # Envelopador , *args= arg nomeados, **kwargs = args não nomeados
        print(f"Chamando função {func.__name__} com args = {args} e kwarg = {kwargs}")
        return func(*args, **kwargs) #Vai copiar a funcionamento da função
    
    return wrapper

# decorar duas vezes
# Problema o decorador oculta a função original, nesse caso a função printada é wrapper
@log_args
@dobrar_retorno # O decorador recebe sempre a função abaixo e altera a função, o mais interno é sempre altera primeiro
def soma_1(a, b):
    return a + b

@log_args
def soma_2(a, b, c):
    return a + b + c

print("Resultado:", soma_1(42, 666)) # É como se tivessemos wrapper(42, 666) depois de decorado com log_args
print("Resultado:", soma_2(13, 42, 666))
