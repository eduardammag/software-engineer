# def saudador(pessoa):
#     saudacao = "Bem-vindo"

#     def mensagem(): # Faz parte do espaço de nomer de saudador, a var saudacao existe no espaço de nomes de mensagem
#         return f"{saudacao}, {pessoa}"
    
#     return mensagem()

# print(saudador("Antonio"))

def saudador(pessoa):
    saudacao = "Bem-vindo"

    def mensagem(): # Faz parte do espaço de nomer de saudador, a var saudacao existe no espaço de nomes de mensagem
        return f"{saudacao}, {pessoa}"
    
    return mensagem #Não invocar a função para termos closer, ela não foi executada, foi preparada para a execução. A função saudador morreu, e a mensagem lembrará 

msg_antonio = saudador("Antonio") # Criei uma função que fala bem vindo antonio
msg_ana = saudador("Ana")
print(msg_antonio())
print(msg_ana())

# A proposta não é executar a função, mas sim criar um  objeto que lembra quando ele foi criado. Uma fábrica de funções