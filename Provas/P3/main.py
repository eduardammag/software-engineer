from funcoes import cache_resultados, cache_limitado, ServicoTextoA, ServicoTextoB, AdapterA, AdapterB

################################ QUESTAO 1 ###################################################

# Criando funções simples só para demonstrar o funcionamento
@cache_resultados
def soma(a, b):
    print("-> Executando soma(a, b) de verdade...")
    return a + b


@cache_limitado(max_tamanho=2)
def mult(a, b):
    print("-> Executando mult(a, b) de verdade...")
    return a * b


print("\n TESTE DO DECORADOR cache_resultados ")
print(soma(42, 13))  
print(soma(42, 13))  
print(soma(40, 2))   
print(soma(40, 2))   

print("\n TESTE DO DECORADOR cache_limitado ")
print(mult(2, 3))   
print(mult(4, 5))   
print(mult(2, 3)) 
print(mult(7, 8))  
print(mult(4, 5))   
print(mult(2, 3))   


################################ QUESTAO 2 ###################################################
print(" Demonstracao AdapterA ")
a = AdapterA(
        ServicoTextoA(),
        pre=str.strip,    # remove espaços
        pos=str.upper     # converte para maiúsculas
    )
print("Saida final:", a.executar("   ola   "))

print("\n Demonstracao AdapterB ")
b = AdapterB(ServicoTextoB())
print("Saida final:", b.executar("abc"))
