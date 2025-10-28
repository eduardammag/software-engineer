# Fábrica de funções (decoradores)
# Funciona para linguages que tem funções de primeira classe, onde a função é passada como parâmetro
def meu_dedorador(funcao_original): #receb uma função original e retorna uma função modificada, decorada
    def nova_funcao():
        print("Algo antes da função") #Comportamento 1

        funcao_original()

        print("Algo depois da função") #Comportamento 2

    return nova_funcao


def diga_ola():
    print("Olá, mundo!") # A ideia do decorador é uma forma de embelzar a função

diga_ola()
diga_ola = meu_dedorador(diga_ola) # Altera para sempre
diga_ola()

diga_ola()
diga_ola_decorada = meu_dedorador(diga_ola) 
diga_ola_decorada()

#Em python isso tem automatico, açucar sintatico
@meu_dedorador #Syntatic sugar (açucar sintatico)
def diga_oi():
    print("Oi, mundo!")

diga_oi()