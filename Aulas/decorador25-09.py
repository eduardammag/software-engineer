import inspect
from functools import wraps

def enforce_types(func):
    assinatura = inspect.signature(func)
    anotacoes = func.__annotations__
    print(anotacoes)
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        bound = assinatura.bind(*args, **kwargs)
        bound.apply_defaults()
        print(bound.arguments)
        for nome_param, valor in bound.arguments.items():
            if nome_param in anotacoes:
                tipo_esperado = anotacoes[nome_param]
                if not isinstance(tipo_esperado, type):
                    raise TypeError(
                        f"Anotação para {nome_param} utiliza um tipo não suportado de constructor: {tipo_esperado!r}"
                    )
                if not isinstance(valor, tipo_esperado):
                    raise TypeError(
                        f"Anotação para {nome_param} utiliza {tipo_esperado!r}, mas recebeu {type(valor)!r}"
                    )
        resultado = func(*args, **kwargs)

        if "return" in anotacoes:
            tipo_retorno = anotacoes["return"]

            if not isinstance(tipo_retorno, type):
                    raise TypeError(
                        f"Anotação de retorno ultiliza um tipo não suportado de constructor: {tipo_retorno!r}"
                    )
            if not isinstance(resultado, tipo_retorno):
                    raise TypeError(
                        f"Retorno em espera {tipo_retorno!r} mas recebeu {type(resultado)!r}"
                    )

        return resultado        
    return wrapper     

@enforce_types
def concatena(texto_esquerda: str, texto_direita: str) -> str:
    """ Tipos esperados str + str -> str """
    return texto_esquerda + texto_direita

@enforce_types
def area_retangulo(base: float, altura: float) -> float:
    """ Tipos esperados float + float -> float """
    return base * altura

print(concatena("Eu adoro ", "a EMAp"))
print(area_retangulo(3.0,4.0))
print(area_retangulo("3.0",4.0))

#tem que documentar e comentar todo o código, ele tem que tem um padrão SPHINKS
