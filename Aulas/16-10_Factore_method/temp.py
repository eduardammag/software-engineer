# Resolver o problema de criação de objetos
# Simple factore
# Se a nossa subclasse não redefine um comportamento relevante não faz sentido
# A ideia é ter um método que fábrica objetos 

from ABC import ABC, abstractmethod

class Chair(ABC):
    @abstractmethod
    def sit(self) -> None : ...

class ArmChair(Chair):
    def sit(self):
        print("Você está sentado em uma poltrona confortável para leitura")

class FoldingChair(Chair):
    def sit(set) -> None:
        print("Você está sentado em uma poltrona confortável de bar da esquina")

class BeanBagChair(Chair):
    def sit(set) -> None:
        print("Você está sentado em um pufe no chão")

class RockingChair(Chair):
    def sit(set) -> None:
        print("Você está sentado em uma cadeira de balança")

class ChairFactory:
    @staticmethod # método estático não precisa de self
    def get_chair(type_: str) -> Chair:
        if type_ == "arm_chair":
            return ArmChair
        if type_ == "folding_chair":
            return FoldingChair
        if type_ == "beanbag_chair":
            return BeanBagChair
        if type_ == "rocking_chair":
            return RockingChair
        raise ValueError("Esta cadeira não existe")
    

lista_de_cadeiras = []
lista_de_cadeiras.append(ChairFactory.get_chair("arm_chair"))
lista_de_cadeiras.append(ChairFactory.get_chair("arm_chair"))
lista_de_cadeiras.append(ChairFactory.get_chair("folding_chair"))

for cada_cadeira in lista_de_cadeiras:
    cada_cadeira.sit()


lista_de_cadeiras.append(ChairFactory.get_chair("fgv_chair"))