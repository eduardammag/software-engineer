from decorator_base import Decorator

class DecoratorA(Decorator):
    """Decorator que adiciona comportamento A"""
    
    def operacao(self) -> str:
        return f"DecoratorA({super().operacao()})"

class DecoratorB(Decorator):
    """Decorator que adiciona comportamento B"""
    
    def operacao(self) -> str:
        return f"DecoratorB({super().operacao()})"
