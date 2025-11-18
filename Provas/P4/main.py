################################ QUESTAO 1 ###################################################

# a) O Singleton baseado em módulo é o mais simples, pois o estado é criado
# automaticamente no momento do import, sem necessidade de classe; porém,
# aumenta o acoplamento ao espalhar variáveis globais e dificulta o reset
# em testes, já que o módulo não é recarregado facilmente. A alternativa
# com atributo de classe e lazy initialization oferece melhor clareza, pois
# deixa explícito onde a instância é criada e permite reinicializar
# facilmente através de um método de reset; além disso, cria o objeto apenas
# quando necessário. Já a alternativa com __new__ customizado encapsula
# completamente a lógica de criação dentro do mecanismo interno de construção
# de objetos, sendo elegante, mas menos intuitiva para quem lê o código.
# Também exige mecanismos adicionais de reset, pois __new__ não deixa tão 
# claro o ponto de controle. Por fim, apenas os módulos criam instância no import;
# as outras alternativas são realmente lazy.

# b)
from funcoes import (
    ConfigServiceSingletonLazy,
    ConfigServiceSingletonNew,
)

print("\n--- ALTERNATIVA 2: Lazy Initialization ---")
inst1 = ConfigServiceSingletonLazy.get_instance()
inst2 = ConfigServiceSingletonLazy.get_instance()

print("id(inst1):", id(inst1))
print("id(inst2):", id(inst2))
print("Mesma instância?", inst1 is inst2)

# Reset de testes
ConfigServiceSingletonLazy._reset_for_tests()


print("\n--- ALTERNATIVA 3: __new__ customizado ---")
inst3 = ConfigServiceSingletonNew()
inst4 = ConfigServiceSingletonNew()

print("id(inst3):", id(inst3))
print("id(inst4):", id(inst4))
print("Mesma instância?", inst3 is inst4)

# Reset de testes
ConfigServiceSingletonNew._reset_for_tests()

################################ QUESTAO 2 ###################################################
