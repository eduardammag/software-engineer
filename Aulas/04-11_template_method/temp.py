# padrão de projeto de um padrão de projeto
# vamos olhar para dentro da estrategia agora
# METODO TEMPLATE

# método de métodos com nomes especificos do domínio que diz todos os passos da minha estratégia
# garante que a cada estratégia concreta ele vai seguir um roteiro do passo a passo, mas só alguns desses passos são válidos para cada esttratégia
# Temos 100 passos (métodos), cada estratégia usa alguns desses 100
#  ideia é quebrar a estratégia em pedacinhos 

from __future__ import annotations
from abc import ABC, abstractmethod
import random

class DataPipeline(ABC):
    def run_pipeline(self, source: str) -> None: # Modelo que todos os pipelines devem seguir
        self.load_data(source)
        self.hook_after_load() # oportunidade para algo ser executado logo depois de carregar os dados

        self.clean_data()
        self.hook_after_clean()

        self.analyze_data()
        self.report_results()

    # Métodos obrigatórios
    @abstractmethod
    def load_data(self, source: str) -> None: pass

    @abstractmethod
    def clean_data(self) -> None: pass

    @abstractmethod
    def analyze_data(self) -> None: pass

    @abstractmethod
    def report_results(self) -> None: pass

    # Métodos opcionais
    def hook_after_load(self) -> None: pass
    def hook_after_clean(self) -> None: pass


# Vantagem: segue exatamente o passo a passo definidos 
class SalesAnalysisPipeline(DataPipeline):

    def load_data(self, source: str) -> None: 
        print(f"Carregando  os dados de vendas de {source}")


    def clean_data(self) -> None: 
        print(f"Limpando dados de vendas...")


    def analyze_data(self) -> None: 
        print(f"Analisando os dados de vendas...")


    def report_results(self) -> None: 
        print(f"Relatório final de vendas por categoria")

    
    def hook_after_load(self) -> None: 
        print(f"Pré visualização para Análise exploratória de dados de venda")


class FraudDetectionPipeline(DataPipeline):

    def load_data(self, source: str) -> None: 
        print(f"Carregando  transações de {source}")


    def clean_data(self) -> None: 
        print(f"Filtrando transações inválidas...")


    def analyze_data(self) -> None: 
        print(f"detectando fraudes...")


    def report_results(self) -> None: 
        print(f"Relatório final de transações suspeitas")

    def hook_after_clean(self) -> None: 
        print(f"Transações válidas...")

pipeline_1 = SalesAnalysisPipeline()
pipeline_1.run_pipeline("sales.csv")

pipeline_2 = FraudDetectionPipeline()
pipeline_2.run_pipeline("transacoes.csv")