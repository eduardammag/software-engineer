class AdaptadorGenerico:
    """
    Adaptador genérico que transforma a interface de qualquer objeto
    para a interface esperada pelo cliente.
    """

    def __init__(self, objeto_original, metodo_original, metodo_esperado):
        """
        :param objeto_original: objeto que precisa ser adaptado
        :param metodo_original: nome do método existente no objeto original
        :param metodo_esperado: nome do método que o cliente espera
        """
        self.objeto_original = objeto_original
        self.metodo_original = metodo_original
        self.metodo_esperado = metodo_esperado

    def __getattr__(self, nome):
        """
        Captura chamadas de método e redireciona para o método original.
        """
        if nome == self.metodo_esperado:
            metodo = getattr(self.objeto_original, self.metodo_original)
            return metodo
        # Se o método não for o esperado, retorna o atributo original
        return getattr(self.objeto_original, nome)
