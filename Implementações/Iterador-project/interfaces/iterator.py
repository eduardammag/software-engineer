class Iterator:

    """
    Interface do Iterador.
    Define os métodos que qualquer iterador deve implementar.
    """

    def has_next(self):

        """
        Retorna True se ainda houver elementos a serem percorridos.
        """
        raise NotImplementedError
    
    def next(self):

        """
        Retorna o próximo elemento.
        """
        raise NotImplementedError