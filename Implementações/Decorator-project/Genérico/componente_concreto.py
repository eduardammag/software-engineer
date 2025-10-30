from componente_base import Componente

class ComponenteConcreto(Componente):
    """Implementação concreta do componente"""
    
    def operacao(self) -> str:
        return "ComponenteConcreto"
