# ============================================================
# Padrão de Projeto: Strategy (Estratégia)
# ------------------------------------------------------------
# Ideia:
#   Permite definir diferentes "estratégias" (maneiras) de fazer
#   algo — no caso, calcular descontos — sem alterar o código da classe principal.
#
#   A lógica de desconto é isolada em classes separadas,
#   que seguem uma mesma interface (calculate).
# ============================================================

from __future__ import annotations  # Permite usar o nome DiscountStrategy no __init__ de Order
from abc import ABC, abstractmethod  # Para criar classes e métodos abstratos

# ------------------------------------------------------------
# Classe principal: Pedido (Order)
# ------------------------------------------------------------
class Pedido:
    
    def __init__(self, total: float, estrategia_desconto: EstrategiaDesconto) -> None:
        """
        Construtor do Pedido.
        Recebe:
            - total: valor total da compra
            - estrategia_desconto: objeto que define COMO o desconto será aplicado
        """
        self._total = total
        self._estrategia_desconto = estrategia_desconto
        # Os atributos com "_" são usados como "privados" por convenção.

    # --------------------------------------------------------
    # Getter (propriedade somente leitura) para o total bruto
    # --------------------------------------------------------
    @property
    def total(self) -> float:
        """Retorna o valor total sem desconto."""
        return self._total

    # --------------------------------------------------------
    # Getter para o total com desconto aplicado
    # --------------------------------------------------------
    @property
    def total_com_desconto(self) -> float:
        """
        Retorna o valor com desconto.
        A lógica do desconto é delegada para o objeto de estratégia.
        """
        return self._estrategia_desconto.calcular(self._total)


# ------------------------------------------------------------
# Interface (abstrata) para todas as estratégias de desconto
# ------------------------------------------------------------
class EstrategiaDesconto(ABC):
    @abstractmethod
    def calcular(self, valor: float) -> float:
        """
        Método que TODAS as estratégias concretas devem implementar.
        Recebe o valor original e retorna o valor com desconto.
        """
        pass


# ------------------------------------------------------------
# Estratégia 1: Nenhum desconto
# ------------------------------------------------------------
class SemDesconto(EstrategiaDesconto):
    def calcular(self, valor: float) -> float:
        """
        Estratégia básica — não aplica nenhum desconto.
        """
        return valor


# ------------------------------------------------------------
# Estratégia 2: Desconto baseado na idade
# ------------------------------------------------------------
class DescontoPorIdade(EstrategiaDesconto):
    def __init__(self, idade: int) -> None:
        """
        Calcula um percentual de desconto baseado na idade.
        Exemplo: idade 22 → desconto de 22%.
        """
        self._desconto = idade / 100  # 22 anos = 0.22 = 22%

    def calcular(self, valor: float) -> float:
        """
        Aplica o desconto sobre o valor total.
        """
        return valor * (1 - self._desconto)


# ------------------------------------------------------------
# Exemplo de uso do padrão Strategy
# ------------------------------------------------------------

# Criamos duas estratégias diferentes:
sem_desconto = SemDesconto()
desconto_22_anos = DescontoPorIdade(22)

# Criamos pedidos usando estratégias diferentes
pedido_1 = Pedido(1000, sem_desconto)
pedido_2 = Pedido(1000, desconto_22_anos)

# ------------------------------------------------------------
# Exibindo os resultados
# ------------------------------------------------------------
print("pedido_1.total:", pedido_1.total)
print("pedido_1.total_com_desconto:", pedido_1.total_com_desconto)

print("pedido_2.total:", pedido_2.total)
print("pedido_2.total_com_desconto:", pedido_2.total_com_desconto)

# ============================================================
# Saída esperada:
# ------------------------------------------------------------
# pedido_1.total: 1000
# pedido_1.total_com_desconto: 1000
#
# pedido_2.total: 1000
# pedido_2.total_com_desconto: 780.0
# (Porque 22% de desconto sobre 1000 → 1000 * 0.78 = 780)
# ============================================================

