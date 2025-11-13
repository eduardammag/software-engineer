# Quero criar uma família de produtos, mas quem recebe não quer saber sobre cada objeto
# ISolar a criação da família de objetos do cara que usa esses objetos

from abc import ABC, abstractmethod

# Abstrações dos objetos que vamos criar
# Definimos o contrato da familia de prdutos, com 3 produtos

#              | DATASET       MODELO         PLOT
# -------------|--------------------------------------
#       LOCAL  |
# DISTRIBUIDO  |

class DatasetLoarder(ABC):                             
    @abstractmethod
    def load(self) -> None: ...


class Model(ABC):
    @abstractmethod
    def train(self) -> None: ...


class Visualizer(ABC):
    @abstractmethod
    def plot(self) -> None: ...

#####################################################################################

# Deve ter um método para criar cada produto


class DataScienceFactory(ABC):
    @abstractmethod
    def create_dataset_loader(self) -> DatasetLoarder: ...

    @abstractmethod
    def create_model(self) -> Model: ...

    @abstractmethod
    def creat_visualizer(self) -> Visualizer: ...

#####################################################################################

# definindo a classe concreta


class PandasDatasetLoader(DatasetLoarder):
    def load(self) -> None:
        print(
            "[PandasDatasetLoarder] lendo csv loacl com pandas.read_csv() . Amostras: 10.000")


class SKLearningModel(Model):
    def train(self) -> None:
        print("[SKLearnModel] Treinando LogisticRegression(solver=\"lbfgs\"). Acurácia de válidação: 0.67")


class MatplotlibVisualizer(Visualizer):
    def plot(self) -> None:
        print("[MatplotlibVisualizer] Plotando matriz de confusão com Matplotlib")

# Essa familíli concreta seria de uma equipe, uma outra equipe desenvolveria outra familia


#####################################################################################

# definindo a classe concreta
class SparkDatasetLoader(DatasetLoarder):
    def load(self) -> None:
        print("[SparkDatasetLoader] Lendo dados no cluster: spark.read.parquet(\" s3:// bucket/ dataset \") . Linhas: 100.000.000 ")


class MLlibModel(Model):
    def train(self) -> None:
        print(
            "[MLLibModel] Treinando RandomForestClassifier em cluster . Acurácia de válidação: 0.90")


class SeabornVisualizer(Visualizer):
    def plot(self) -> None:
        print("[MatplotlibVisualizer] Gerando pyplot e heatmap de correlação no seaborn")

#####################################################################################
# Agora tem que fazer as fábricas


class LocalFactory(DataScienceFactory):
    def create_dataset_loader(self) -> DatasetLoarder:
        print("[Localfactory: datasetloader] ")
        return PandasDatasetLoader()

    def create_model(self) -> Model:
        print("[LocalFactory: model] ")
        return SKLearningModel()

    def creat_visualizer(self) -> Visualizer:
        print("[LocalFactory: Visualizer] ")
        return MatplotlibVisualizer()


class DistributedFactory(DataScienceFactory):
    def create_dataset_loader(self) -> DatasetLoarder:
        print("[DistributedFactory: datasetloader] ")
        return SparkDatasetLoader()

    def create_model(self) -> Model:
        print("[DistributedFactory: model] ")
        return MLlibModel()

    def creat_visualizer(self) -> Visualizer:
        print("[DistributedFactory: Visualizer] ")
        return SeabornVisualizer()

###############################################################


class ApplicationInterface():
    def get_factory(self, stack: str) -> DataScienceFactory:
        if stack == "local":
            return LocalFactory()
        if stack == "distribuido":
            return DistributedFactory()
        raise ValueError("Deu ruim")

################################################################
 # Como o cliente ficaria usando esse padrão?


app = ApplicationInterface()
factory = app.get_factory("local")

loader = factory.create_dataset_loader()
model = factory.create_model()
viz = factory.creat_visualizer()

loader.load()
model.train()
viz.plot()







# | Papel                  | Classe                                                              | Responsabilidade                                              |
# | ---------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------- |
# | **Produtos Abstratos** | `DatasetLoader`, `Model`, `Visualizer`                              | Interfaces base dos objetos que a fábrica cria                |
# | **Produtos Concretos** | `PandasDatasetLoader`, `SKLearnModel`, `MatplotlibVisualizer`, etc. | Implementações específicas                                    |
# | **Fábrica Abstrata**   | `DataScienceFactory`                                                | Define métodos para criar cada tipo de produto                |
# | **Fábricas Concretas** | `LocalFactory`, `DistributedFactory`                                | Criam produtos concretos de uma família                       |
# | **Cliente**            | `ApplicationInterface` + parte final do código                      | Usa apenas a fábrica abstrata, sem conhecer classes concretas |
