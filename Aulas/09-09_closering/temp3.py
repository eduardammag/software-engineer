def registrar_evento(mensagem):
    print("Evento:", mensagem)

registrar_evento.contador = 0 # Criei contador dentro de um dicionario
registrar_evento.log = []

print(registrar_evento.__dict__)

def armazenar_evento(mensagem):
    registrar_evento.contador += 1
    registrar_evento.log.append(mensagem)
    registrar_evento(mensagem)
    print(f"Chamadas: {registrar_evento.contador}")
    print(f"Histórico: {registrar_evento.log}")

armazenar_evento("Sistema Iniciado")
armazenar_evento("Usuário autenticado")