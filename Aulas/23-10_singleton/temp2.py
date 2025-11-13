# Singleton raiz

class SingletonRaiz:
    _instance = None # membro de dados protegido

    # _instance é um atributo de classe, não de instância.
    # Ele é compartilhado entre todos os objetos da classe.
    # O prefixo _ indica que é protegido (por convenção), ou seja, não deve ser modificado fora da classe.
    # Inicialmente, _instance = None significa que nenhuma instância ainda foi criada.



    # init: ele inicializa um objeto já criado, NÃO cria um objeto. Se tem self já tem o objeto criado

    def __new__(cls): # Recebe um instancia da classe. Vai criar o objeto olhando a instancia da classe e depois passa para o init
        if cls._instance is None: # Se é none, cria
            print("[INFO] Creating Singleton instance")
            cls._instance = super().__new__(cls) # cria a classe manualmente
        else:
            print("[INFO] Returning existing Singleton instance")
        return cls._instance
    
    # __new__ é o método responsável por criar o objeto, antes mesmo de __init__ ser chamado.
    # Ele é chamado automaticamente quando fazemos algo como a = SingletonRaiz().
    # O parâmetro cls é a própria classe (equivalente a self nas instâncias).
    # O método super().__new__(cls) cria o objeto "vazio" e aloca espaço na memória.
    # (É como se disséssemos: “agora existe o objeto, mas ele ainda não foi inicializado.”)
    # Ao armazenar a instância em cls._instance, garantimos que a próxima vez que alguém tentar instanciar a classe, ela já vai existir.
    # Assim, se _instance já estiver definido, ele não cria um novo objeto, apenas retorna o mesmo.

    def __init__(self):
        self.data = "Data"
        print("Devo eu rodar outra vez?") # Inicializa  sempre 

        # __init__ é o inicializador, chamado toda vez que você instancia a classe, mesmo que o objeto já exista.
        # Isso significa que o Singleton não impede o reprocessamento do __init__.
        # Ou seja, ele reutiliza o mesmo objeto, mas ainda chama o código de inicialização novamente.

a = SingletonRaiz()
print(a.data)
b = SingletonRaiz()
# print(a.data)