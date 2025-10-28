#  Padrão de Projeto Iterator aplicado em Lista, Árvore e Grafo

Este projeto demonstra de forma **didática e modularizada** o uso do **Padrão de Projeto Comportamental Iterator**, aplicando-o em três estruturas de dados fundamentais: **Lista**, **Árvore Binária** e **Grafo (DFS e BFS)**. Todo o código é separado em módulos para seguir boas práticas de organização, reutilização e clareza.

---

##  Objetivo do Padrão Iterator

O padrão **Iterator** permite percorrer os elementos de uma coleção **sem expor sua estrutura interna**, fornecendo uma interface uniforme para navegação.

###  Benefícios:
- Encapsula a lógica de iteração
- Suporta múltiplos percursos diferentes
- Aplica o princípio de responsabilidade única (SRP)
- Facilita a extensão (Open/Closed Principle - OCP)

---

##  Estrutura do Projeto

projeto_iterator/
├── interfaces/
│   ├── iterator.py          # Interface Iterator
│   ├── aggregate.py         # Interface Aggregate (coleção)
│   └── __init__.py
├── colecoes/
│   ├── lista.py             # Coleção Lista
│   ├── pilha.py             # Coleção Pilha
│   ├── fila.py              # Coleção Fila
│   ├── arvore.py            # Coleção Árvore
│   ├── grafo.py             # Coleção Grafo
│   └── __init__.py
├── iterators/
│   ├── lista_iterator.py    # Iterator da Lista
│   ├── pilha_iterator.py    # Iterator da Pilha
│   ├── fila_iterator.py     # Iterator da Fila
│   ├── arvore_iterator.py   # Iterator da Árvore (DFS)
│   ├── grafo_dfs_iterator.py# Iterator do Grafo (DFS)
│   ├── grafo_bfs_iterator.py# Iterator do Grafo (BFS)
│   └── __init__.py
└── main.py                  # Código do cliente (testes e polimorfismo)


---

##  Componentes Principais

###  **Interface Iterator**
Define os métodos fundamentais:
- `has_next()` → diz se ainda há elementos
- `next()` → retorna o próximo elemento

###  **Interface Aggregate**
Define o método:
- `criar_iterator()` → fábrica para retornar um iterador específico

Cada estrutura concreta (lista, árvore, grafo) implementa essa interface para fornecer seu respectivo iterador.

---

##  Estruturas Implementadas

###  Lista
- Estrutura sequencial simples
- Iteração direta do primeiro ao último elemento

###  Árvore Binária
- Percurso implementado: **Pré-Ordem (Raiz → Esquerda → Direita)**
- Usa pilha internamente para simular recursão

###  Grafo
- Dois tipos de iteradores:
  -  **DFS (Profundidade)** → usa pilha
  -  **BFS (Largura)** → usa fila

---

##  Conclusão

Este projeto demonstra como aplicar o **Padrão de Projeto Iterator** de forma **clara, modular e extensível**, permitindo múltiplas estratégias de percorrimento para diferentes estruturas de dados.

---

## Diagrama de Classes

```text
+-------------------+
|     Aggregate     |
|-------------------|
| + criar_iterator()|
+---------+---------+
          ^
          |
+---------+------------------------------------------------+
|         |                |               |             |
|         |                |               |             |
v         v                v               v
+---------+   +---------+  +---------+   +-----------+
|  Lista  |   |  Pilha  |  |  Fila   |   |  Arvore   |
+---------+   +---------+  +---------+   +-----------+
     |            |           |               |
     | usar Iterator | usar Iterator | usar Iterator | usar Iterator
     v            v           v               v
+-------------------+  +-------------------+  +----------------+  +----------------+
|   ListaIterator   |  |   PilhaIterator   |  |   FilaIterator |  |  ArvoreIterator |
+-------------------+  +-------------------+  +----------------+  +----------------+

+-------------------+
|       Grafo       |
+-------------------+
| criar_iterator_dfs() |
| criar_iterator_bfs() |
+-------------+-------------+
              |
              |
     +--------+--------+
     |                 |
     v                 v
+-------------------+  +----------------+
|   GrafoDFSIterator |  | GrafoBFSIterator |
+-------------------+  +----------------+
