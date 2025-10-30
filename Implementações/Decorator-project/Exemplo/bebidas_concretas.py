from bebida import Bebida

class Cafe(Bebida):
    def descricao(self) -> str:
        return "Café"
    
    def custo(self) -> float:
        return 5.0
    

class Cha(Bebida):
    def descricao(self) -> str:
        return "Chá"
    
    def custo(self) -> float:
        return 3.0