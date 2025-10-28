from interfaces.aggregate import Aggregate
from iterators.lista_iterator import ListaIterator

class Lista(Aggregate):

    """
    Coleção completa do tipo Lista.
    Implementa o método criar_iterator() para retornar um iterador.
    """

    def __init__(self):
        self.elementos = []

    def adicionar(self, item):
        """
        Adiciona um elemento à lista.
        """
        self.elementos.append(item)

    def criar_iterator(self):
        """
        Retorna o iterador concreto para percorrer essa lista.
        """    
        return ListaIterator(self.elementos)