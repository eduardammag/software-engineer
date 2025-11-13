# Fazer um decorador para ver a assinatura de função em python, para garantir que as especificações forem cumpridas
#Decorador que não tenta executar a função caso os tippós estejam errados: enforce types
# type hint

import inspect
from functools import wraps

def enforce_types(func):
    assinatura = inspect.signature(func) # Pegar a assinatura da função 
    anotacaoes = func.__annotations__ # Pegar anotações da função
    print(assinatura)

    @wraps(func) # preservar os dados da função que foi decorada
    def wrapper(*args, **kwargs):
        bound = assinatura.bind(*args, **kwargs)
        # Bound: pegar a assinatura da função e juntar(comparar) com o que foi passado (parâmetro junto com o argumeneto)
        # Falta o argumento padrão
        bound.apply_defaults() # Por isso, precisamos verificar os defaults também
        # print(bound) # Bound é um objeto da classe BoundArguments
        for nome_parametro, valor in bound.arguments.items(): # Dentro de bound temos outros objetos que são os argumentos, dicionário como o nome do arg como chave e o arg como  o valor {texto_esquerda='Eu adoro', texto_direita='a EMAP'}, a gente está desempacotando
            # Temos uma lista, como é opcional fazer anotation e type hint, eu não tenho como verificar, por isso antes de fazer qualquer coisa, precisamos verificar se tem anotações de typehint, se não não verificamos
            if nome_parametro in anotacaoes: # Se não estiver no dict anotacoes, ele não está na doc e não precisamos verificar
                tipo_esperado = anotacaoes[nome_parametro] # Pegar o tipo esperado
                if not isinstance(tipo_esperado, type): # Alguns tipos de anotações são tipos em python e outros não são um tipo, por ex: callable[float, [float]] não é um type, não é um objeto
                    raise TypeError(
                        f"Anotação para {nome_parametro} utiliza um tipo não suportado de constructor: {tipo_esperado!r}"
                    )
                if not isinstance(valor, tipo_esperado): # Caso o valor não seja do tipo certo
                    raise TypeError(
                        f"Argumento em {nome_parametro} utiliza {tipo_esperado} mas recebeu {type(valor)!r}"
                    )
        
        resultado = func(*args, **kwargs) #Chama a função

        # Verifica se o tipo do do resultad é correto

        if "return" in anotacaoes:
            tipo_retorno = anotacaoes["return"]

            if not isinstance(tipo_retorno, type): # Alguns tipos de anotações são tipos em python e outros não são um tipo, por ex: callable[float, [float]] não é um type, não é um objeto
                raise TypeError(
                    f"Anotação de retorno utiliza um tipo não suportado de constructor: {tipo_retorno!r}"
                )
            if not isinstance(resultado, tipo_retorno): # Caso o valor não seja do tipo certo
                raise TypeError(
                    f"Retorno  espera {tipo_retorno} mas recebeu {type(resultado)!r}"
                )


        return resultado
                


    return wrapper

@enforce_types
def concatena(texto_esquerda:str, texto_direita:str) -> str :
    """ Tipos esperados str + str -> str"""
    return texto_esquerda + texto_direita

# Tudo deve ser comentado e documentado
@enforce_types
def area_retangulo(base: float, altura:float) -> float:
    """ Tipos esperados float + float -> float"""
    return base*altura

print(concatena("Eu adoro", "a EMAP"))
print(area_retangulo(3.0, 4.0))
print(area_retangulo("3.0", 4.0))