# Em excessão é frequente o tratamento de erro parcial
# Cadeia de responsabilidade: uma sequência, em que cada um trata um pouquinho e passa a diante

from __future__ import annotations
from abc import ABC, abstractmethod
import random

# O cliente que solita algo não conhece quem vai tratar o problema

# 2 coisas importante: devolver o que recebemos e um sucessor para entregar a solicitação. 
# Manipulamos o que recebemos e passamos adiante, o mesmo objeto. Até ter um None, que não tem para quem passar mais, no último tratador

class Handler(ABC):
    def __init__(self, sucessor = None): # Criamos uma sucessão 
        """doc lindo"""
        self._sucessor = sucessor

    @abstractmethod
    def handle(self, request: str) -> str: pass


class LowerCaseHandle(Handler): # Só trata se request for lower
    def handle(self, request: str) -> str:
        if request.islower():
            return f"LowerCaseHandle tratou \"{request}\""
        elif self._sucessor:
            return self._sucessor.handle(request)
        else:
            return f"LowerCaseHandle não conseguiu tratar \"{request}\""
        

class UpperCaseHandle(Handler): # Só trata se request for upper
    def handle(self, request: str) -> str:
        if request.isupper():
            return f"UpperCaseHandle tratou \"{request}\""
        elif self._sucessor:
            return self._sucessor.handle(request)
        else:
            return f"UpperCaseHandle não conseguiu tratar \"{request}\""
        

class DefaultCaseHandler(Handler): # se não passou em nenhuma
    def handle(self, request: str) -> str:
        return f"Nenhuma regra conseguiu tratar \"{request}\""
    
# Só um handler trata
handler_chain = LowerCaseHandle(UpperCaseHandle(DefaultCaseHandler())) # O primeiro que estamos definindo que vai tratar. Podemos montar diferentes cadeis, mas o default tem que ser o último

test_inputs = ["abc", "XYZ", "123", "EMAp"]

for item in test_inputs:
    print(handler_chain.handle(item))

