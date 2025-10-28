# import importlib
# import singleton

# print(singleton.amor_de_uma_vida)

# for counter in range(10):
#     importlib.reload(singleton)
#     print(counter)
    
# print( "Fim do exemplo")


# # único ponto de acesso global, só permite uma instância apenas 

################## SINGLETON

class SingletonRaiz:
    _instance = None 

    # init = inicializa um objeto que ja ta pronto, se tem self ja tem objeto criado, quem cria objetos em pyhton é o new
    def __new__(cls):
        if cls._instance is None:
            print("[INFO] Creating Singleton instance")   
            cls._instance = super().__new__(cls) 
        else: 
            print("[INFO] Returning existing Singleton instance")    
        return cls._instance

    def __init__(self):
        self.data = "Data"
        print("Devo eu rodar outra vez?")



a = SingletonRaiz()
print(a.data)
b = SingletonRaiz()


################### FACTORY METHOD : alta coesão, baixo acoplamento
from abc import ABC, abstractmethod

class DatasetLoader(ABC):
    @abstractmethod
    def load(self) -> None: ...
        

class Model(ABC):
    @abstractmethod
    def train(self) -> None: ...
                
class Visualizer(ABC):
    @abstractmethod
    def plot(self) -> None: ...


    #####################################

class DataScienceFactory(ABC):
    @abstractmethod
    def create_dataset_loader(self) -> DatasetLoader: ...

    @abstractmethod
    def create_model(self) -> Model: ...

    @abstractmethod
    def create_visualizer(self) -> Visualizer: ...

    ##################################### família concreta estaria na empresa sendo desenvolvida por uma equipe

class PandasDatasetLoader(DatasetLoader):
    def load(self) -> None:
        print("[PandassDatasetLoader] Lendo CSV local com pandas.read_csv(...). Amostras: 100000")

class SKLearnModel(Model):
    def train(self) -> None:
        print("[SKLearnModel] Treinando LogisticRegression(solver=\"lbfgs\"). Acurácia de validação: 0.67")

class MatplotlibVisualizer(Visualizer):
    def plot(self) -> None:
        print("[MatplotlibVisualizer] Gerando pyplot e heatmap de correlação no Seaborn")        


    ##################################### 

class SparkDatasetLoader(DatasetLoader):
    def load(self) -> None:
        print("[SparkDatasetLoader] Lendo dados no cluster: spark.read.parquet(\s3://bucket/dataset\") Linhas: 100_000_000")

class MLlibModel(Model):
    def train(self) -> None:
        print("[MllibModel] Treinando LogisticRegression(solver=\"lbfgs\"). Acurácia de validação: 0.67")

class SeabornVisualizer(Visualizer):
    def plot(self) -> None:
        print("[SeabornVisualizer] Gerando pyplot e heatmap de correlação no Seaborn")        


    #####################################

class LocaFactory(DataScienceFactory):
    def create_dataset_loader(self) -> DatasetLoader:
        print("[LocalFactory: DatasetLoader]")
        return PandasDatasetLoader()

    def create_model(self) -> Model:
        print("[LocalFactory: Model]")
        return SKLearnModel()

    def create_visualizer(self) -> Visualizer:
        print("[LocalFactory: Visualizer]")
        return MatplotlibVisualizer()
    
    #####################################
class DistributedFactory(DataScienceFactory):
    def create_dataset_loader(self) -> DatasetLoader:
        print("[DistributedFactory: DatasetLoader]")
        return SparkDatasetLoader()

    def create_model(self) -> Model:
        print("[DistributedFactory: Model]")
        return MLlibModel()

    def create_visualizer(self) -> Visualizer:
        print("[DistributedFactory: Visualizer]")
        return SeabornVisualizer()
    
    #####################################

class Applicationinterface:
        def get_factory(self, stack: str) -> DataScienceFactory:
            if stack == "local":
                return LocaFactory()    
            if stack == "distributed":
                return DistributedFactory()
            raise ValueError("Deu ruim")
        
    #####################################

app = Applicationinterface()

factory = app.get_factory("local")            
loader = factory.create_dataset_loader()
model = factory.create_model()
viz = factory.create_visualizer()

loader.load()
model.train()
viz.plot()

factory = app.get_factory("distributed")            
loader = factory.create_dataset_loader()
model = factory.create_model()
viz = factory.create_visualizer()


# para criar objetos: esse teste. builder e prototype mais avançando