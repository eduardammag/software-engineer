from interfaces.iterator import Iterator

class GrafoDFSIterator(Iterator):
    """
    Iterador para percorrer grafo em profundidade (DFS).
    """

    def __init__(self, adjacencia, inicio):
        self.adjacencia = adjacencia
        self.pilha = [inicio]
        self.visitados = set()

    def has_next(self):
        return len(self.pilha) > 0

    def next(self):
        while self.pilha:
            atual = self.pilha.pop()

            # Marca como visitado somente ao visitar
            if atual not in self.visitados:
                self.visitados.add(atual)

                # Adiciona vizinhos não visitados à pilha
                for vizinho in reversed(self.adjacencia.get(atual, [])):
                    if vizinho not in self.visitados:
                        self.pilha.append(vizinho)

                return atual

        raise StopIteration("Fim do grafo (DFS).")
