from interfaces.iterator import Iterator

class ArvoreIterator(Iterator):
    """
    Iterador para percorrer a árvore em pré-ordem (DFS).
    """

    def __init__(self, raiz):
        self.pilha = []
        if raiz:
            self.pilha.append(raiz)

    def has_next(self):
        return len(self.pilha) > 0

    def next(self):
        if not self.has_next():
            raise StopIteration("Fim da árvore alcançado.")

        atual = self.pilha.pop()

        # Adiciona filho direito primeiro, depois esquerdo (pilha LIFO)
        if atual.direita:
            self.pilha.append(atual.direita)
        if atual.esquerda:
            self.pilha.append(atual.esquerda)

        return atual.valor