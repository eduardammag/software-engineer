
from tree_design import (ConstrutorArvore,
    IteradorPreOrdem,
    VisitanteProfundidade,
    VisitanteContadorFolhas
)

print("\nConstruindo arvore")
construtor = ConstrutorArvore()
raiz = construtor.construir()

print("\nPercurso em Pre-Ordem")
for no in IteradorPreOrdem(raiz):
    print("Visitado:", no.nome)

print("\nVisitantes")

# Profundidade
visitante_p = VisitanteProfundidade(raiz)
prof = visitante_p.executar()
print("Profundidade da arvore =", prof)

# Contagem de folhas
visitante_f = VisitanteContadorFolhas(raiz)
qt = visitante_f.executar()
print("Numero de folhas =", qt)
