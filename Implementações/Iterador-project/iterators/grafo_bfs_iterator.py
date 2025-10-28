from interfaces.iterator import Iterator
from collections import deque

class GrafoBFSIterator(Iterator):
    """
    Iterador para percorrer grafo em largura (BFS).
    """

    def __init__(self, adjacencia, inicio):
        self.adjacencia = adjacencia
        self.fila = deque([inicio])
        self.visitados = set()

    def has_next(self):
        return len(self.fila) > 0

    def next(self):
        while self.fila:
            atual = self.fila.popleft()
            if atual not in self.visitados:
                self.visitados.add(atual)
                # Adiciona vizinhos não visitados à fila
                for vizinho in self.adjacencia.get(atual, []):
                    if vizinho not in self.visitados:
                        self.fila.append(vizinho)
                return atual
        raise StopIteration("Fim do grafo (BFS).")
        