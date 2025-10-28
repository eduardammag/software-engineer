from interfaces.aggregate import Aggregate
from iterators.arvore_iterator import ArvoreIterator

class NoArvore:
    """
    Nó de árvore binária.
    """

    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class Arvore(Aggregate):
    """
    Coleção concreta de árvore binária.
    """   

    def __init__(self, raiz = None):
        self.raiz = raiz

    def criar_iterator(self):
        """
        Retorna o iterador concreto para percorrer a árvore em pré-ordem.
        """    
        return ArvoreIterator(self.raiz)     