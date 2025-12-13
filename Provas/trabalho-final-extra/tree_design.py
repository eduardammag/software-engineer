from abc import ABC, abstractmethod

########################## COMPOSITE ##########################
class No(ABC):
    """Classe base para qualquer nó da arvore."""

    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def adicionar(self, no):
        pass

    @abstractmethod
    def aceitar(self, visitante):
        pass


class NoFolha(No):
    """Representa um nó folha (sem filhos)."""

    def adicionar(self, no):
        raise Exception("Não é possível adicionar filhos a um nó folha.")

    def aceitar(self, visitante):
        visitante.visitar_folha(self)


class NoDecisao(No):
    """Nó que pode possuir filhos (ramificações)."""

    def __init__(self, nome):
        super().__init__(nome)
        self.filhos = []

    def adicionar(self, no):
        self.filhos.append(no)

    def aceitar(self, visitante):
        visitante.visitar_decisao(self)


########################## ITERATOR ##########################
class IteradorPreOrdem:
    """
    Percorre a arvore em pré-ordem:
    1) visita o nó atual
    2) visita recursivamente os filhos
    """

    def __init__(self, raiz):
        self.pilha = [raiz]

    def __iter__(self):
        return self

    def __next__(self):
        if not self.pilha:
            raise StopIteration()

        no = self.pilha.pop()

        if isinstance(no, NoDecisao):
            for f in reversed(no.filhos):
                self.pilha.append(f)

        return no


########################## VISITORS ##########################
class VisitanteProfundidade:
    """Calcula profundidade maxima da arvore usando Iterator."""

    def __init__(self, raiz):
        self.raiz = raiz
        self.profundidade = 0
        self.mapa_niveis = {}

    def visitar_decisao(self, no):
        for filho in no.filhos:
            self.mapa_niveis[filho] = self.mapa_niveis[no] + 1

    def visitar_folha(self, no):
        pass  # Nada especial para nó folha

    def executar(self):
        self.mapa_niveis[self.raiz] = 1
        iterador = IteradorPreOrdem(self.raiz)

        for no in iterador:
            no.aceitar(self)

        self.profundidade = max(self.mapa_niveis.values())
        return self.profundidade


class VisitanteContadorFolhas:
    """Conta o numero total de folhas usando Iterator."""

    def __init__(self, raiz):
        self.raiz = raiz
        self.total = 0

    def visitar_decisao(self, no):
        pass

    def visitar_folha(self, no):
        self.total += 1

    def executar(self):
        iterador = IteradorPreOrdem(self.raiz)

        for no in iterador:
            no.aceitar(self)

        return self.total


########################## ESTADOS ##########################
class EstadoArvore(ABC):
    @abstractmethod
    def executar(self, construtor):
        pass


class EstadoSeparacao(EstadoArvore):
    """Primeiro estado: cria a primeira ramificacao da arvore."""

    def executar(self, construtor):
        print("[EstadoSeparacao] Criando etapa inicial de separacao...")

        hcl = NoDecisao("Adicionar HCl")
        construtor.raiz.adicionar(hcl)

        construtor.no_atual = hcl
        construtor.mudar_estado(EstadoPoda())


class EstadoPoda(EstadoArvore):
    """Segundo estado: adiciona ramos mockados."""

    def executar(self, construtor):
        print("[EstadoPoda] Adicionando sub-ramos simulados...")

        agua_quente = NoDecisao("Aquecimento em agua quente")
        construtor.no_atual.adicionar(agua_quente)

        pb = NoDecisao("PbCl2 soluvel em agua quente")
        pb.adicionar(NoFolha("Pb2+ identificado"))
        agua_quente.adicionar(pb)

        insol = NoDecisao("AgCl e Hg2Cl2 insoluveis")
        agua_quente.adicionar(insol)

        nh4oh = NoDecisao("Adicionar NH4OH quente")
        insol.adicionar(nh4oh)

        hg = NoDecisao("Precipitado preto -> Hg2(2+)")
        hg.adicionar(NoFolha("Hg2(2+) confirmado"))
        nh4oh.adicionar(hg)

        ag = NoDecisao("AgCl + HNO3 -> precipitado branco")
        ag.adicionar(NoFolha("Ag+ confirmado"))
        nh4oh.adicionar(ag)

        construtor.mudar_estado(EstadoParada())


class EstadoParada(EstadoArvore):
    """Estado final: encerra o processo."""

    def executar(self, construtor):
        print("[EstadoParada] Construcao finalizada.")
        construtor.finalizado = True


########################## CONSTRUTOR ##########################
class ConstrutorArvore:
    """Controla a construcao da arvore através dos estados."""

    def __init__(self):
        self.estado = EstadoSeparacao()
        self.finalizado = False

        self.raiz = NoDecisao("Mistura inicial")
        self.no_atual = self.raiz

    def mudar_estado(self, novo_estado):
        print(f"[Construtor] Mudando estado para: {novo_estado.__class__.__name__}")
        self.estado = novo_estado

    def passo(self):
        self.estado.executar(self)

    def construir(self):
        while not self.finalizado:
            self.passo()
        return self.raiz
