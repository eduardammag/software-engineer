from interfaces.aggregate import Aggregate
from iterators.fila_iterator import FilaIterator

class Fila(Aggregate):
    """
    Coleção concreta do tipo Fila (Queue) com comportamento FIFO.
    """

    def __init__(self):
        self.elementos = []

    def enfileirar(self, item):
        """
        Adiciona um elemento ao final da fila.
        """   
        self.elementos.append(item)

    def desenfileirar(self):
        """
        Remove e retorna o primeiro elemento da fila.
        """ 
        if not self.esta_vazia():
            return self.elementos.pop(0)
        else:
            raise IndexError("A fila está vazia.")

    def esta_vazia(self):
        return len(self.elementos) == 0

    def criar_iterator(self):
        """
        Retorna o iterador concreto para percorrer a fila do primeiro ao último.
        """ 
        return FilaIterator(self.elementos)      