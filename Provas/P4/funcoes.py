################################ QUESTAO 1 ###################################################

#   ALTERNATIVA 2 — Singleton com atributo de classe (lazy)

class ConfigServiceSingletonLazy:
    """
    Singleton implementado com atributo de classe.
    Criação apenas na primeira chamada de get_instance().
    """

    _inst = None  # guarda a instância única

    def __init__(self):
        # apenas um exemplo de estado interno
        self.config = {"modo": "produção"}

    @classmethod
    def get_instance(cls):
        """
        Retorna a única instância, criando-a se necessário (lazy initialization).
        """
        if cls._inst is None:
            cls._inst = cls()
        return cls._inst

    @classmethod
    def _reset_for_tests(cls):
        """
        Permite resetar o singleton (útil para testes).
        """
        cls._inst = None


#   ALTERNATIVA 3 — Singleton com __new__ customizado

class ConfigServiceSingletonNew:
    """
    Singleton implementado sobrescrevendo __new__.
    O controle da criação ocorre antes do __init__.
    """

    _inst = None  # instância única

    def __new__(cls, *args, **kwargs):
        if cls._inst is None:
            cls._inst = super().__new__(cls)
        return cls._inst

    def __init__(self):
        # exemplo de estado interno
        self.config = {"modo": "produção"}

    @classmethod
    def _reset_for_tests(cls):
        """
        Permite resetar o singleton (útil para testes).
        """
        cls._inst = None


################################ QUESTAO 2 ###################################################
