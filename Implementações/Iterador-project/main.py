from colecoes.lista import Lista
from colecoes.pilha import Pilha




lista = Lista()
lista.adicionar("Ana")
lista.adicionar("Bruno")
lista.adicionar("Carla")

iterator = lista.criar_iterator()
print("Percorrendo a lista com Iterator:")
while iterator.has_next():
    print("Elemento: ", iterator.next())

######################################

pilha = Pilha()
pilha.empilhar("Livro 1")
pilha.empilhar("Livro 2")
pilha.empilhar("Livro 3")

iterator = pilha.criar_iterador()
print("Percorrendo a pilha com Iterator:")
while iterator.has_next():
    print("Elemento: ", iterator.next())