from __future__ import annotations # Permite referenciar DiscountStrategy no __init__ de Order mesmo que DiscountStrategy seja definido depois no arquivo. Evita necessidade de usar 'DiscountStrategy' entre aspas.
from abc import ABC, abstractmethod

# discount_strategy retira toda a responsabilidade de como  fazer um pedido
# A estrategia é destacada do código com  uma interface

class Order:
    def __init__(self, total: float, discount_strategy: DiscountStrategy) -> None:
        self._total = total
        self._discount_strategy = discount_strategy

        # Usa atributos “privados” por convenção _total e _discount_strategy

    @property # Getter para total: Propriedade somente leitura total para expor o valor bruto.
    def total(self) -> float:
        return self._total
    
    @property # Getter para total_with_discount: total_with_discount delega o cálculo para a discount_strategy chamando seu método calculate(value)
    def total_with_discount(self) -> float:
        return self._discount_strategy.calculate(self._total)
    
###################################################################################################

class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, value: float) -> float:
        pass
    
###################################################################################################

class NoDiscount(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value

class AgeDiscount(DiscountStrategy):
    def __init__(self, age: int) -> None:
        self._discount = age / 100

    def calculate(self, value: float) -> float:
        return value * (1 - self._discount)

###################################################################################################

no_discount = NoDiscount()
age_discount_22 = AgeDiscount(22)

order_1 = Order(1000, no_discount)
order_2 = Order(1000, age_discount_22)

print("order_1.total: ", order_1.total)
print("order_1.total_with_discount: ", order_1.total_with_discount)

print("order_2.total: ", order_2.total)
print("order_2.total_with_discount: ", order_2.total_with_discount)



