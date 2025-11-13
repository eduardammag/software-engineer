def aplicar(objeto, nome, *args, **kwargs): # Aplicador de função
    if not hasattr(objeto, nome):
        raise AttributeError(f"{type(objeto).__name__} não tem atributo")
    atributo = getattr(objeto, nome)
    
    # Existem atributos que não são métodos, mas sim propriedades, aí não podemos invocar
    if callable(atributo):
        return atributo(*args, **kwargs)
    
    return atributo

texto = "  EMAp  "
fruta = "Banana"
print(aplicar(texto, "strip"))
print(aplicar(fruta, "replace", "a", "@")) # a função pega o nome do objeto, os parametros e a funação que queremos aplicar