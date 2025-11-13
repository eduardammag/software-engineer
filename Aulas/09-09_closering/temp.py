texto = "EMAp"

nome_metodo = "strip"

# Mostra os métodos de um objeto do tipo string
print(dir(texto))
print("#"*60)

# Verifica se tem um atributo atributo
if hasattr(texto, nome_metodo):
    print(f"O método \"{nome_metodo}\" existe no objeto \"{texto}\"")
    metodo = getattr(texto, nome_metodo) # Função, um objeto como qualquer outro


    # Aplicar o método
    print("Depois de aplicar o método:", texto)
    
    print("Depois de aplicar o método:", repr(metodo())) # Ele já vem ligado ao objeto

else:
    print(f"O método \"{nome_metodo}\" não existe no objeto \"{texto}\"")

# o método é um atributo de um objeto, que continua ligado ao objeto