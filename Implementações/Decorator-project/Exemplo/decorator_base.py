from bebida import Bebida

class Adicional(Bebida):
    """
    Decorator base para adicionais
    """

    def __init__(self, bebida: Bebida):
        self._bebida = bebida


    def descricao(self) -> str:
        return self._bebida.descricao()

    def custo(self) -> float:
        return self._bebida.custo()  