import importlib
import singleton # o import é a vibe de um singleton, mas é só um cache, não é um singleton

print(singleton.amor_de_uma_vida)


for counter in range(10):
    import singleton
    importlib.reload(singleton) # recarregar algo que já foi importado
    print(counter)

print("Fim do Exemplo")