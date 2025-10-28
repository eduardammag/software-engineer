from interfaces.iterator import Iterator

class PilhaIterator(Iterator):
    """
    Iterador concreto para percorrer uma pilha (LIFO).
    """
    def __init__(self, elementos):
        self.elementos = elementos
        # Começa do topo (último elemento)
        self.posicao_atual = len(elementos) -1 

    def has_next(self):
        return self.posicao_atual >= 0

    def next(self):
        if self.has_next():
            valor = self.elementos[self.posicao_atual]
            self.posicao_atual -=1
            return valor
        else:
            raise StopIteration("Fim da pilha alcançado.")    
