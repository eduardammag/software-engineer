# main.py
from bebidas_concretas import Cafe, Cha
from adicionais_concretos import Leite, Acucar, Chocolate

# Café simples
bebida1 = Cafe()
print(f"{bebida1.descricao()} custa {bebida1.custo()}")

# Café com leite
bebida2 = Leite(bebida1)
print(f"{bebida2.descricao()} custa {bebida2.custo()}")

# Café com leite e chocolate
bebida3 = Chocolate(bebida2)
print(f"{bebida3.descricao()} custa {bebida3.custo()}")

# Chá com açúcar
bebida4 = Acucar(Cha())
print(f"{bebida4.descricao()} custa {bebida4.custo()}")
