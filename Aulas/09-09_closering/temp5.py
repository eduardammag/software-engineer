
def saudador(pessoa):
    saudacao = "Bem-vindo"

    def mensagem(): # Faz parte do espaço de nomer de saudador, a var saudacao existe no espaço de nomes de mensagem
        return f"{saudacao}, {pessoa}"
    
    return mensagem #Não invocar a função para termos closer, ela não foi executada, foi preparada para a execução. A função saudador morreu, e a mensagem lembrará 

print(saudador.__code__) #Representa o código da função. Podemos mudar o código da função durante a execução
print(dir(saudador.__code__.co_consts)) # Constantes do código
print(hasattr(saudador.__code__.co_consts, "__iter__")) # Perguntar se é iterável
print(hasattr(saudador.__code__.co_consts, "__next__")) # Perguntar se é iterador, pode pedir um next (como não é, criamos um for)]

for cada_constante in saudador.__code__.co_consts:
    if  isinstance(cada_constante, type(saudador.__code__)): # Pegamos apenas o que é código
        print(f"Função interna detectada: { cada_constante.co_name}")



msg_antonio = saudador("Antonio") # Criei uma função que fala bem vindo antonio
msg_ana = saudador("Ana")
print(msg_antonio())
print(msg_ana())

print(msg_antonio.__closure__)
for cada_celula in msg_antonio.__closure__:
    print(cada_celula.cell_contents) # Ela guarda a lembrança que ela tem do contexto de quando ela foi criada