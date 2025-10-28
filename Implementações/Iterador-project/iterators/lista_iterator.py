from interfaces.iterator import Iterator

class ListaIterator(Iterator):
    """
    Iterador concreto para percorrer uma lista.
    """

    def __init__(self, elementos):
        self.elementos = elementos
        self.posicao_atual = 0

    def has_next(self):
        return self.posicao_atual < len(self.elementos)

    def next(self):
        if self.has_next():
            valor = self.elementos[self.posicao_atual]
            self.posicao_atual +=1
            return valor
        else:
            raise StopIteration("Fim da lista alcançado.")

