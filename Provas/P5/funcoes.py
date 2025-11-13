from abc import ABC, abstractmethod

# Classe abstrata base (Template)
class TaskTemplate(ABC):
    def __init__(self, name):
        self.name = name

    def execute(self, fonte, strategy=None):
        print(f"\nIniciando tarefa: {self.name}")

        dados = self.load_data(fonte)
        resultado = self.process(dados, strategy)
        resumo = self.summarize(resultado)
        
        print(f"Tarefa {self.name} finalizada\n")
        return resultado

    def load_data(self, fonte):
        print(f"Carregando dados do arquivo {fonte}")
        if fonte:
            print("Dados carregados com sucesso.")
        else:
            print("Nenhum dado fornecido.")
        return fonte

    @abstractmethod
    def process(self, dados, strategy=None):
        #Deve ser implementado pelas subclasses concretas.
        pass

    def summarize(self, resultado):
        resumo = f"Resumo da execucao de {self.name}"
        print(resumo)
        return resumo


# Subclasses concretas
class ImportTask(TaskTemplate):
    def process(self, dados, strategy=None):
        if strategy:
            print("Aplicando estrategia personalizada durante importacao")
            strategy.run(dados)
        else:
            print("Importando dados de forma padrao.")
        return "Importacao pronta"


class ReportTask(TaskTemplate):
    def process(self, dados, strategy=None):
        if strategy:
            print("Aplicando estrategia personalizada durante geracao de relatorio")
            strategy.run(dados)
        else:
            print("Gerando relatorio padrao")
        return "Relatorio pronto"


# Strategies
class UppercaseStrategy:
    def run(self, dados):
        print("Strategy: convertendo texto em maiusculas 'abc' -> 'ABC'")

class LowercaseStrategy:
    def run(self, dados):
        print("Strategy: convertendo texto em minusculas 'ABC' -> 'abc'")


# Contexto para trocar strategy dinamicamente
class TaskStrategyContext:
    def __init__(self, strategy=None):
        self.strategy = strategy

    def set_strategy(self, strategy):
        print(f"\nStrategy alterada para: {strategy.__class__.__name__}")
        self.strategy = strategy

    def executar(self, tarefa, fonte):
        print("Executando tarefa com a strategy atual")
        return tarefa.execute(fonte, self.strategy)
