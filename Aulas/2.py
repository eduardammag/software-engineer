from functools import wraps

def retry(retries=3, exceptions = (Exception,), delay = 0.0, backoff=1.0):
    if not isinstance(retries, int) or retries <1:
        raise ValueError("Retries deve ser int >= 1")
    if not isinstance(delay, (int,float)) or delay <0:
        raise ValueError("Delay deve ser int ou float >= 0")
    if not isinstance(backoff, (int,float)) or backoff <1:
        raise ValueError("Backoff deve ser int ou float >= 1")

    if not isinstance(exceptions, tuple): 
        exceptions = (exceptions, )
    for exc in exceptions:
        if not (isinstance(exc, type) and issubclass(exc, BaseException)):    
            raise TypeError("Exceção deve ser classe derivada de BaseException")
        
    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            tentativa_atual=1
            atraso_atual = float(delay)

            while True:
                try: 
                    return func(*args, **kwargs)
                except exceptions as err:
                    if tentativa_atual >= retries:
                        raise
                    pass

        return wrapper 

        


    return decorator    

#Driver Code
contador = {"falhas": 0}

@retry(retries=3, exceptions=(ValueError,), delay = 0.1, backoff=2.0)
def pode_falhar():
    if contador["falhas"] < 2:
        contador["falhas"] +=1
        raise ValueError("Falhou!")
    return "OK"

print(pode_falhar())