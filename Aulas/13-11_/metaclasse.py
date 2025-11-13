class Normal:
    pass 

class Normal_2:
    pass 

print(f"O tipo da -- instancia -- e: {type(Normal)}")
print(f"O tipo da -- instancia -- e: {type(Normal_2)}")

# o type é o molde dos moldes, cria classes
# classe rege o objeto, as metaclasses dizem como as classes tem que se comportar

EMAp = type("EMAp", (), {"x":42} ) #tupla com classes base da minha classe e do lado os atributos
escola = EMAp()
print(escola.x)

# estamos mudando como as classes funcionam no nosso programa
# init(ja tem o objeto criado, quer popular o dicionario) x new (chamado imediatamente na criação do objeto, antes do init)
class MetaLogger(type):
    def __new__(mcls, name, bases, namespace):
        print(f"[MetaLogger] Esta criando uma classe: {name}")
        print(f"Bases: {bases}")
        print(f"Atributos: {namespace.keys()}")
        return super().__new__(mcls, name, bases, namespace)
        
    # toda vez que uma instancia dessa classe e criada, o python roda o metodo call
    def __call__(cls, *args, **kwargs):  
        print(f"[MetaLogger] instanciando {cls.__name__}")  
        return super().__call__(*args, **kwargs)

class Example(metaclass = MetaLogger):
    def __init__(self):
        print("Inicializando exemplo")

print("Começando o programa")
ex = Example() #olha tudo o que tinha antes de rodar o programa

class MetaRegistry(type):
    required_attrs = ["table_name"] 

    def __new__(mcls, name, bases, namespace):
        cls = super().__new__(mcls, name, bases, namespace)
        # metaclasse verifica se as classes instanciadas implementam atributos obrigatorios
        print("#########") 
        print(cls.mro())
        print("#########") 
        for attr in mcls.required_attrs:
            if not any(hasattr(base, attr) for base in cls.mro()):
                raise TypeError("A classe deve definir ou herdar atributos")
        return cls


class Valida(metaclass = MetaRegistry):
    table_name = "clientes"

class FilhaDaValida(Valida):
    pass

class Invalida(metaclass = MetaRegistry):
    tudo_menos_table_name = ""

