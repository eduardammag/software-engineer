"""
Sistema de descontos de pedidos
=============================================================
"""
# principio SOLID

class Order:
	
    def __init__(self, total, discount_type=None, percentage=None, age=None, loyalty_points=None):
        self.total = total
        self.discount_type = discount_type
        self.percentage = percentage
        self.age = age
        self.loyalty_points = loyalty_points

    def calculate_total(self):
        """
        Calcula o valor final do pedido com base no tipo de desconto.
        """

        if self.discount_type is None:
            # Nenhum desconto
            final_value = self.total

        elif self.discount_type == "percentage":
            if self.percentage is None:
                raise ValueError("Faltando valor percentual para desconto.")
            final_value = self.total * (1 - self.percentage / 100)

        elif self.discount_type == "age":
            if self.age is None:
                raise ValueError("Idade não informada.")
            discount = min(self.age / 100, 0.5)  # limite máximo de 50%
            final_value = self.total * (1 - discount)

        elif self.discount_type == "loyalty":
            if self.loyalty_points is None:
                raise ValueError("Pontos de fidelidade não informados.")
            discount_rate = min(self.loyalty_points / 10000, 0.3)
            final_value = self.total * (1 - discount_rate)

        elif self.discount_type == "black_friday":
            final_value = self.total * 0.7  # desconto fixo de 30%

        else:
            raise ValueError(f"Tipo de desconto desconhecido: {self.discount_type}")

        return final_value

    def __repr__(self):
        return f"<Order total={self.total:.2f}, discount_type={self.discount_type}, final={self.calculate_total():.2f}>"

if __name__ == "__main__":

    orders = [
        Order(1000),
        Order(1000, discount_type="percentage", percentage=10),
        Order(1000, discount_type="age", age=25),
        Order(1000, discount_type="loyalty", loyalty_points=2000),
        Order(1000, discount_type="black_friday"),
    ]

    for order in orders:
        print(order)











"""
Sistema de descontos de pedidos — refatorado com o padrão Strategy
====================================================================
Ideia:
Cada tipo de desconto é uma estratégia independente.
A classe Pedido (Order) apenas usa a estratégia recebida,
sem precisar saber os detalhes de cálculo.
====================================================================
"""

from abc import ABC, abstractmethod

# ------------------------------------------------------------
# Interface comum para todas as estratégias de desconto
# ------------------------------------------------------------
class EstrategiaDesconto(ABC):
    @abstractmethod
    def calcular(self, valor: float) -> float:
        """
        Recebe o valor total e retorna o valor com desconto aplicado.
        Toda estratégia concreta deve implementar este método.
        """
        pass


# ------------------------------------------------------------
# Estratégias de desconto concretas
# ------------------------------------------------------------

class SemDesconto(EstrategiaDesconto):
    """Não aplica nenhum desconto."""
    def calcular(self, valor: float) -> float:
        return valor


class DescontoPercentual(EstrategiaDesconto):
    """Desconto percentual genérico, ex: 10%."""
    def __init__(self, percentual: float):
        if percentual < 0 or percentual > 100:
            raise ValueError("Percentual deve estar entre 0 e 100.")
        self._percentual = percentual

    def calcular(self, valor: float) -> float:
        return valor * (1 - self._percentual / 100)


class DescontoPorIdade(EstrategiaDesconto):
    """Desconto proporcional à idade (máx. 50%)."""
    def __init__(self, idade: int):
        if idade < 0:
            raise ValueError("Idade inválida.")
        self._idade = idade

    def calcular(self, valor: float) -> float:
        desconto = min(self._idade / 100, 0.5)
        return valor * (1 - desconto)


class DescontoPorFidelidade(EstrategiaDesconto):
    """Desconto baseado em pontos de fidelidade (máx. 30%)."""
    def __init__(self, pontos: int):
        if pontos < 0:
            raise ValueError("Pontos de fidelidade inválidos.")
        self._pontos = pontos

    def calcular(self, valor: float) -> float:
        taxa_desconto = min(self._pontos / 10000, 0.3)
        return valor * (1 - taxa_desconto)


class DescontoBlackFriday(EstrategiaDesconto):
    """Desconto fixo de 30% (Black Friday)."""
    def calcular(self, valor: float) -> float:
        return valor * 0.7


# ------------------------------------------------------------
# Classe principal: Pedido (Order)
# ------------------------------------------------------------
class Pedido:
    def __init__(self, total: float, estrategia: EstrategiaDesconto):
        """
        Recebe:
          - total: valor bruto do pedido
          - estrategia: objeto que define a regra de desconto
        """
        self._total = total
        self._estrategia = estrategia

    @property
    def total(self) -> float:
        """Valor original do pedido."""
        return self._total

    @property
    def total_com_desconto(self) -> float:
        """Valor final após aplicar a estratégia de desconto."""
        return self._estrategia.calcular(self._total)

    def __repr__(self):
        return f"<Pedido total={self.total:.2f}, final={self.total_com_desconto:.2f}, estrategia={self._estrategia.__class__.__name__}>"


# ------------------------------------------------------------
# Exemplo de uso do padrão Strategy
# ------------------------------------------------------------
if __name__ == "__main__":
    pedidos = [
        Pedido(1000, SemDesconto()),
        Pedido(1000, DescontoPercentual(10)),
        Pedido(1000, DescontoPorIdade(25)),
        Pedido(1000, DescontoPorFidelidade(2000)),
        Pedido(1000, DescontoBlackFriday()),
    ]

    for pedido in pedidos:
        print(pedido)

"""
Saída esperada:
<Pedido total=1000.00, final=1000.00, estrategia=SemDesconto>
<Pedido total=1000.00, final=900.00, estrategia=DescontoPercentual>
<Pedido total=1000.00, final=750.00, estrategia=DescontoPorIdade>
<Pedido total=1000.00, final=980.00, estrategia=DescontoPorFidelidade>
<Pedido total=1000.00, final=700.00, estrategia=DescontoBlackFriday>
"""
