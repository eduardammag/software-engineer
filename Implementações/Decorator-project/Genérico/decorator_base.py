from componente_base import Componente

class Decorator(Componente):
    """Decorator base que implementa a interface Componente"""
    
    def __init__(self, componente: Componente):
        self._componente = componente
    
    def operacao(self) -> str:
        return self._componente.operacao()
