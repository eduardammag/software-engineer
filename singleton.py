class Singleton:
    __instance = None  # Campo estático privado para armazenar a instância

    def __new__(cls):
        # Impede criação direta pelo construtor
        raise RuntimeError("Use o método get_instance() para obter o objeto Singleton")

    @staticmethod
    def get_instance():
        # Método público estático para obter a instância
        if Singleton.__instance is None:  # inicialização preguiçosa
            # Criamos a instância "manualmente" usando object.__new__
            Singleton.__instance = object.__new__(Singleton)
            # Podemos inicializar atributos aqui, se necessário:
            Singleton.__instance.valor = 0
        return Singleton.__instance

    # Você pode adicionar métodos normais na classe
    def incrementar(self):
        self.valor += 1
        print(f"Valor atual: {self.valor}")


# ===== Código Cliente =====

# Tentativa de criar diretamente => Erro
# obj = Singleton()  # Descomente para ver o erro

# Forma correta:
s1 = Singleton.get_instance()
s2 = Singleton.get_instance()

print("s1 é s2?", s1 is s2)  # True, ambas são a mesma instância

s1.incrementar()
s2.incrementar()  # Usa o mesmo objeto
