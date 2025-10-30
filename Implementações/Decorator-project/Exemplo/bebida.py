from abc import ABC, abstractmethod

class Bebida(ABC):
    """
    Interface base para todas as bebidas"
    """

    @abstractmethod
    def descricao(self) -> str:
        pass

    @abstractmethod
    def custo(self) -> float:
        pass