# Sistema de Construção de Árvore com Padrões: State, Composite, Visitor e Iterator

Este documento explica como o código utiliza cada padrão de projeto, onde cada um aparece e qual é seu papel.  
Inclui também um diagrama UML textual.

---

# Visão Geral

O sistema constrói e percorre uma árvore de decisão química usando quatro padrões clássicos:

- Composite — estrutura hierárquica de nós (decisão/folha).  
- Iterator — percorre a árvore em pré-ordem sem expor detalhes internos.  
- Visitor — executa operações sobre a árvore (contagem, profundidade etc.).  
- State — controla a lógica de construção da árvore passo a passo.

---

# Onde cada padrão está presente no código

## COMPOSITE
Classes relacionadas:  
- `No` (abstrato)  
- `NoDecisao`  
- `NoFolha`

Função no sistema: Modela a estrutura da árvore.  
`NoDecisao` possui filhos; `NoFolha`, não. Ambos são tratados pelo tipo base `No`.

O Composite permite montar árvores profundas de forma uniforme.

---
## ITERATOR

- Classe: IteradorPreOrdem
- Função no sistema: Percorre a árvore sem expor a lista interna de filhos nem exigir recursão manual.
- O iterator: mantém uma pilha interna, remove sempre o próximo nó a visitar, empilha seus filhos na ordem correta,
entrega os nós um a um para o for. Isso é importante, pois vários visitantes podem percorrer a árvore de maneira padronizada, independente da estrutura interna do Composite.

---
## VISITOR

- Classes relacionadas: 
    - VisitanteProfundidade, 
    - VisitanteContagemFolhas
- Função no sistema: Aplicar operações sobre a árvore sem modificar a estrutura Composite.
- Cada Visitor implementa: visitar_decisao(no) e visitar_folha(no). E usa o Iterator para percorrer todos os nós.

Exemplos de coisas que visitantes fazem:
- Calcular profundidade máxima.
- Contar folhas.
- Imprimir toda a árvore.

Usamos Visitor, pois novos comportamentos podem ser adicionados sem alterar nenhum nó da árvore.

---
##  STATE

Classes relacionadas:
- EstadoArvore (interface)
- EstadoSeparacao
- EstadoPoda
- EstadoParada
- ConstrutorArvore

Função no sistema: Controlar o fluxo da construção da árvore, garantindo que os passos acontecem na ordem correta.
O ConstrutorArvore mantém:
- estado atual
- no_atual
- raiz
- indicadores de finalização

Cada estado implementa uma parte do fluxo, por exemplo:
- EstadoSeparacao cria o nó inicial de separação.
- EstadoPoda adiciona ramificações extras.
- EstadoParada finaliza a construção.
Trocas de estado ocorrem com: construtor.mudar_estado(EstadoPoda())

Usamos State, pois a lógica da construção muda de comportamento conforme o estágio em que se encontra.

---


## DIAGRAMA

```text

                   +-------------------------+
                   |     ConstrutorArvore    |
                   +-------------------------+
                   | - estado: EstadoArvore  |
                   | - raiz: NoDecisao       |
                   | - no_atual: No          |
                   +-------------------------+
                   | + mudar_estado()        |
                   | + construir_arvore()    |
                   +-----------+-------------+
                               |
                               v
                       +------------------+
                       |   EstadoArvore   |
                       +------------------+
                       | + executar()     |
                       +--+-----+-----+---+
                          |     |     |
           ----------------      |      ----------------
           |                     |                     |
           v                     v                     v
+----------------+    +----------------+     +----------------+
| EstadoSeparacao|    |  EstadoPoda    |     | EstadoParada  |
+----------------+    +----------------+     +----------------+
| + executar()   |    | + executar()   |     | + executar()   |
+----------------+    +----------------+     +----------------+

                     COMPOSITE
        +------------------------------+
        |              No              |
        +------------------------------+
        | - nome                       |
        | + aceitar(visitante)         |
        | + adicionar(no) (abstrato)   |
        +---------------+--------------+
                        |
         -----------------------------------------
         |                                       |
         v                                       v
+-----------------------+              +---------------------+
|      NoDecisao        |              |      NoFolha        |
+-----------------------+              +---------------------+
| - filhos[]            |              | (sem filhos)        |
+-----------------------+              +---------------------+

                  ITERATOR
        +------------------------------+
        |      IteradorPreOrdem        |
        +------------------------------+
        | - pilha                      |
        | + __next__()                 |
        +------------------------------+

                    VISITOR
             +--------------------+
             |     Visitante      |
             +--------------------+
             | + visitar_decisao  |
             | + visitar_folha    |
             +-----+--------+-----+
                   |        |
       ----------------   ----------------
       |                |                |
       v                v                v
+--------------+ +----------------+ +----------------------+
| Profundidade | | ContagemFolhas | | ImpressaoOpcional    |
+--------------+ +----------------+ +----------------------+

´´´