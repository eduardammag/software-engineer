from interfaces.iterator import Iterator

class FilaIterator(Iterator):
    """
    Iterador concreto para percorrer uma fila (FIFO).
    """

    def __init__(self, elementos):
        self.elementos = elementos
        self.posicao_atual = 0 # Começa no início da fila

    def has_next(self):
        return self.posicao_atual < len(self.elementos)

    def next(self):
        if self.has_next():
            valor = self.elementos[self.posicao_atual]
            self.posicao_atual +=1
            return valor
        else:
            raise StopIteration("Fim da fila alcançado.")    