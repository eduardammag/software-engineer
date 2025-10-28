# TESTE COM POLIMORFISMO

from colecoes import Lista, Pilha, Fila, Arvore, Grafo, NoArvore

def usar_iterator(colecao, iterador):
    print(f"\nPercorrendo {colecao.__class__.__name__} com Iterator:")
    while iterador.has_next():
        print("Elemento:", iterador.next())


# Lista
lista = Lista()
lista.adicionar("A")
lista.adicionar("B")
lista.adicionar("C")
usar_iterator(lista, lista.criar_iterator())

# Pilha
pilha = Pilha()
pilha.empilhar(1)
pilha.empilhar(2)
pilha.empilhar(3)
usar_iterator(pilha, pilha.criar_iterator())

# Fila
fila = Fila()
fila.enfileirar("X")
fila.enfileirar("Y")
fila.enfileirar("Z")
usar_iterator(fila, fila.criar_iterator())

# Árvore
raiz = NoArvore(10)
raiz.esquerda = NoArvore(5)
raiz.direita = NoArvore(15)
arvore = Arvore(raiz)
usar_iterator(arvore, arvore.criar_iterator())

# Grafo com DFS
grafo = Grafo()
grafo.adicionar_aresta("A", "B")
grafo.adicionar_aresta("A", "C")
usar_iterator(grafo, grafo.criar_iterator_dfs("A"))



# Esse é o poder do padrão Iterator: 
# percorrer estruturas diferentes com a mesma interface!






# TESTE SEM POLIMORFISMO

from colecoes.lista import Lista
from colecoes.pilha import Pilha
from colecoes.fila import Fila
from colecoes.arvore import Arvore, NoArvore
from colecoes.grafo import Grafo

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

iterator = pilha.criar_iterator()
print("Percorrendo a pilha com Iterator:")
while iterator.has_next():
    print("Elemento: ", iterator.next())


######################################    

fila = Fila()
fila.enfileirar("Cliente 1")
fila.enfileirar("Cliente 2")
fila.enfileirar("Cliente 3")

iterator = fila.criar_iterator()
print("Percorrendo a fila com Iterator:")
while iterator.has_next():
    print("Elemento: ", iterator.next())



######################################    

# Criando a árvore:
    #        A
    #       / \
    #      B   C
    #     / \   \
    #    D   E   F
    raiz = NoArvore("A")
    raiz.esquerda = NoArvore("B")
    raiz.direita = NoArvore("C")
    raiz.esquerda.esquerda = NoArvore("D")
    raiz.esquerda.direita = NoArvore("E")
    raiz.direita.direita = NoArvore("F")

    arvore = Arvore(raiz)
    iterator = arvore.criar_iterator()

    print("Percorrendo a arvore com Iterator (pre-ordem):")
    while iterator.has_next():
        print("Visitando no:", iterator.next())


######################################           

grafo = Grafo()
grafo.adicionar_aresta("A", "B")
grafo.adicionar_aresta("A", "C")
grafo.adicionar_aresta("B", "D")
grafo.adicionar_aresta("C", "E")
grafo.adicionar_aresta("D", "F")
grafo.adicionar_aresta("E", "F")

print("Percorrendo Grafo com DFS:")
dfs_iterator = grafo.criar_iterator_dfs("A")
while dfs_iterator.has_next():
    print("Visitando:", dfs_iterator.next())

print("\nPercorrendo Grafo com BFS:")
bfs_iterator = grafo.criar_iterator_bfs("A")
while bfs_iterator.has_next():
    print("Visitando:", bfs_iterator.next())