# ============================================================
# Padrão de Projeto: Chain of Responsibility (Cadeia de Responsabilidade)
# ------------------------------------------------------------
# Ideia:
#   Vários objetos podem tentar tratar uma solicitação (request),
#   um após o outro, até que algum consiga.
#
#   Cada "Handler" (Handler) decide se:
#     - Consegue tratar o pedido;
#     - Ou deve passá-lo para o próximo da cadeia (sucessor).
#
# ============================================================

from abc import ABC, abstractmethod  # Para criar classes e métodos abstratos

# ------------------------------------------------------------
# Classe base abstrata para todos os Handlers
# ------------------------------------------------------------
class Handler(ABC):
    def __init__(self, sucessor=None):
        """
        Cada Handler pode ter um suc
        essor (o próximo da cadeia).
        Se ele não conseguir tratar a requisição, ele repassa para o sucessor.
        """
        self._sucessor = sucessor  # Guarda o próximo objeto da cadeia
        #Essa linha guarda uma referência para o próximo objeto da cadeia.
        # _sucessor → é um atributo privado (por convenção, o _ indica uso interno).
    @abstractmethod
    def tratar(self, requisicao: str) -> str:
        """
        Método abstrato que todas as subclasses devem implementar.
        Define COMO o Handler vai tentar tratar o pedido.
        """
        pass


# ------------------------------------------------------------
# Handler que trata textos totalmente em minúsculas
# ------------------------------------------------------------
class HandlerMinusculo(Handler):
    def tratar(self, requisicao: str) -> str:
        # Verifica se a string é toda em minúsculas
        if requisicao.islower():
            return f"HandlerMinusculo tratou \"{requisicao}\""
        # Se não for, passa o pedido adiante para o próximo da cadeia
        elif self._sucessor:
            return self._sucessor.tratar(requisicao)
        # Se não houver sucessor, significa que ninguém conseguiu tratar
        else:
            return f"HandlerMinusculo não conseguiu tratar \"{requisicao}\""


# ------------------------------------------------------------
# Handler que trata textos totalmente em maiúsculas
# ------------------------------------------------------------
class HandlerMaiusculo(Handler):
    def tratar(self, requisicao: str) -> str:
        # Verifica se a string é toda em maiúsculas
        if requisicao.isupper():
            return f"HandlerMaiusculo tratou \"{requisicao}\""
        # Se não for, passa o pedido adiante
        elif self._sucessor:
            return self._sucessor.tratar(requisicao)
        else:
            return f"HandlerMaiusculo não conseguiu tratar \"{requisicao}\""


# ------------------------------------------------------------
# Handler padrão (último da cadeia)
# ------------------------------------------------------------
class HandlerPadrao(Handler):
    def tratar(self, requisicao: str) -> str:
        # Esse é o último da cadeia: trata qualquer coisa que sobrar
        return f"Nenhuma regra conseguiu tratar \"{requisicao}\""


# ------------------------------------------------------------
# Montando a cadeia de responsabilidade
# ------------------------------------------------------------
# A ordem importa:
# 1️⃣ Primeiro tentamos com o Handler de minúsculas
# 2️⃣ Se não tratar, passamos para o de maiúsculas
# 3️⃣ Se ainda não tratar, o Handler padrão resolve
cadeia = HandlerMinusculo(
            HandlerMaiusculo(
                HandlerPadrao()
            )
         )

# ------------------------------------------------------------
# Testando com várias entradas diferentes
# ------------------------------------------------------------
entradas_teste = ["abc", "XYZ", "123", "EMAp"]

# Para cada entrada, passamos para o primeiro da cadeia
for item in entradas_teste:
    resultado = cadeia.tratar(item)
    print(resultado)


# ============================================================
# Saída esperada:
# ------------------------------------------------------------
# HandlerMinusculo tratou "abc"
# HandlerMaiusculo tratou "XYZ"
# Nenhuma regra conseguiu tratar "123"
# Nenhuma regra conseguiu tratar "EMAp"
# ============================================================

