from interfaces.aggregate import Aggregate
from iterators.grafo_dfs_iterator import GrafoDFSIterator
from iterators.grafo_bfs_iterator import GrafoBFSIterator

class Grafo(Aggregate):
    """
    Representação de Grafo usando lista de adjacência.
    """

    def __init__(self):
        self.adjacencia = {}

    def adicionar_vertice(self,vertice):
        if vertice not in self.adjacencia:
            self.adjacencia[vertice] = []

    def adicionar_aresta(self, origem, destino):
        """
        Grafo não direcionado (adiciona aresta nos dois sentidos).
        """
        self.adicionar_vertice(origem)
        self.adicionar_vertice(destino)
        self.adjacencia[origem].append(destino)
        self.adjacencia[destino].append(origem)            

    def criar_iterator_dfs(self, inicio):
         return GrafoDFSIterator(self.adjacencia, inicio)
    
    def criar_iterator_bfs(self, inicio):
        return GrafoBFSIterator(self.adjacencia, inicio)