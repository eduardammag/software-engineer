from componente_concreto import ComponenteConcreto
from decorators_concretos import DecoratorA, DecoratorB


# Criando o componente base
componente = ComponenteConcreto()
print("Componente simples:", componente.operacao())

# Decorando com DecoratorA
componente_decorado_a = DecoratorA(componente)
print("Componente com DecoratorA:", componente_decorado_a.operacao())

# Decorando com DecoratorB em cima do DecoratorA
componente_decorado_ba = DecoratorB(componente_decorado_a)
print("Componente com DecoratorA e DecoratorB:", componente_decorado_ba.operacao())
