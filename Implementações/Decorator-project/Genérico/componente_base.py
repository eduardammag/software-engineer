from abc import ABC, abstractmethod

class Componente(ABC):
    """Interface base para o componente"""
    
    @abstractmethod
    def operacao(self) -> str:
        pass
