# Resolver o problema de criação de objetos
# Factore method
# Se a nossa subclasse não redefine um comportamento relevante não faz sentido
# A ideia é ter um método que fábrica objetos 

from ABC import ABC, abstractmethod, staticmethod
from typing import Type

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

class LilleII(Chair):
    def sit(set) -> None:
        print("Você não está apenas sentando, você está vivendo uma experiência Lille")


class Solis(Chair):
    def sit(set) -> None:
        print("Você não está apenas sentando, você está vivendo uma experiência Solis")

# Fábricas diferentes, para diferentes tipos de subclasses
# Criamos uma interface para a fábrica, uma classe abstrata que define como funciona uma fábrica,
# o programa precisa cn=onhecer a abstração de uma fábrica, não a construção de uma fábrica concreta

class ChairFactory(ABC):
    @staticmethod #método estático não precisa de self
    @abstractmethod # Está definido que alguém na hierarquia precisa definir o get_chair
    def get_chair(type_: str) -> Chair: ...

class TokStokChairFactory(ChairFactory): # vai existir e não será abstrata
    @staticmethod #método estático não precisa de self
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
    
class ArtefactChairFactory(ChairFactory): # outra fábrica diferente
    @staticmethod #método estático não precisa de self
    def get_chair(type_: str) -> Chair:
        if type_ == "LilleII":
            return LilleII
        if type_ == "solis":
            return Solis
    
factory_ref: Type[ChairFactory] # ponteiro para uma classe de fabrica, não para um objeto de uma fábrica

lista_de_pedidos_tok_stock = ["arm_chair", "arm_chair", "folding_chair"]
factory_ref = ArtefactChairFactory #P ode ser lido de outro lugar, outro arquivo etc. o cliente não precisa se preocupar com nada

for cada_pedido in lista_de_pedidos_tok_stock:
    print(f"Cliente solicitando cadeira \"{cada_pedido}\" ")
    cadeira = factory_ref.get_chair(cada_pedido)
    print("Cliente utilizando cadeira:")
    cadeira.sit()



lista_de_pedidos_artefacto = ["lilleII", "solis"]
factory_ref = ArtefactChairFactory

for cada_pedido in lista_de_pedidos_artefacto:
    print(f"Cliente solicitando cadeira \"{cada_pedido}\" ")
    cadeira = factory_ref.get_chair(cada_pedido) # Passa uma referência a uma fábrica concreta
    print("Cliente utilizando cadeira:")
    cadeira.sit()