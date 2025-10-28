from interfaces.aggregate import Aggregate
from iterators.pilha_iterator import PilhaIterator

class Pilha(Aggregate):
    """
    Coleção concreta do tipo Pilha (Stack) com comportamento LIFO.
    """

    def __init__(self):
        self.elementos = []

    def empilhar(self, item):
        """
        Adiciona um elemento ao topo da pilha.
        """
        self.elementos.append(item)

    def desempilhar(self):
        """
        Remove e retorna o elemento do topo da pilha.
        """   
        if not self.esta_vazia():
            return self.elementos.pop()
        else:
            raise IndexError("A pilha está vazia")     

    def esta_vazia(self):
        return len(self.elementos) == 0
    
    def criar_iterator(self):
        """
        Retorna o iterador concreto para percorrer a pilha do topo para a base.
        """
        return PilhaIterator(self.elementos)