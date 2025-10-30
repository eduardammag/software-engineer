from decorator_base import Adicional

class Leite(Adicional):

    def descricao(self) -> str:
        return f"{self._bebida.descricao()} + Leite"
    
    def custo(self) -> float:
        return self._bebida.custo() + 2.0
    

class Acucar(Adicional):

    def descricao(self) -> str:
        return f"{self._bebida.descricao()} + Açúcar"
    
    def custo(self) -> float:
        return self._bebida.custo() + 0.5
    

class Chocolate(Adicional):
    
    def descricao(self) -> str:
        return f"{self._bebida.descricao()} + Chocolate"
    
    def custo(self) -> float:
        return self._bebida.custo() + 3.0