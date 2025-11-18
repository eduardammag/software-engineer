################################ QUESTAO 1 ###################################################

# DECORADOR: e uma funcao que recebe outra funcao como entrada
# e devolve uma nova funcao “modificada”. Ele “embrulha” (wrap)
# a funcao original para: adicionar comportamento extra, medir 
# tempo, registrar logs, validar argumentos, fazer cache, etc.

# CACHE: e uma tecnica usada para armazenar resultados já calculados,
# para evitar que a funcao faca o mesmo cálculo de novo.

# args: e uma forma de receber um número variável de argumentos
# posicionais na funcao. Ele vira uma tupla. Use quando você
# NAO sabe quantos argumentos a funcao receberá.

# kwargs vem de keyword arguments. Recebe argumentos nomeados.
# Dentro da funcao, kwargs vira um dicionário.


# DECORADOR (a)
# cache_resultados: armazena resultados anteriores SEM LIMITE
def cache_resultados(func):
    # O dicionário servirá como cache: { args : resultado }
    cache = {}

    def wrapper(*args):
        print(f"[cache_resultados] Chamada da funcao {func.__name__} com args={args}")

        # Verifica se o resultado para esses argumentos já existe
        if args in cache:
            print("[cache_resultados] -> Valor encontrado no cache! Retornando sem recalcular.")
            return cache[args]

        print("[cache_resultados] -> Valor NAO estava no cache. Calculando agora...")
        resultado = func(*args)

        print("[cache_resultados] -> Salvando resultado no cache.")
        cache[args] = resultado

        return resultado

    return wrapper

# DECORADOR (b)
# cache_limitado(max_tamanho): igual ao anterior, porem com LIMITE
# Quando o cache enche, remove o item mais antigo.
def cache_limitado(max_tamanho):
    def decorator(func):

        # Usaremos uma lista de ordem + dicionário de cache
        ordem = []     # ordem das chaves inseridas
        cache = {}     # chave: resultado

        def wrapper(*args):
            print(f"[cache_limitado] Chamada da funcao {func.__name__} com args={args}")

            # Caso já esteja no cache -> retorno imediato
            if args in cache:
                print("[cache_limitado] -> Valor encontrado no cache! Retornando sem recalcular.")
                return cache[args]

            print("[cache_limitado] -> Valor NAO estava no cache. Calculando agora...")
            resultado = func(*args)

            # Antes de salvar, verificar se o limite estourou
            if len(ordem) >= max_tamanho:
                chave_antiga = ordem.pop(0)
                print(f"[cache_limitado] -> Cache cheio! Removendo chave mais antiga: {chave_antiga}")
                del cache[chave_antiga]

            # Registrar nova entrada no cache
            print(f"[cache_limitado] -> Salvando {args} no cache.")
            ordem.append(args)
            cache[args] = resultado

            return resultado

        return wrapper

    return decorator

# Usamos a lista ordem porque o dicionário sozinho nao guarda a ordem exata das insercões.
# Precisamos saber qual chave e a mais antiga para remover quando o cache encher.

# Usamos args como chave porque args e uma tupla 
# -> estruturas imutáveis podem ser usadas como chave em dicionários.
# isso pois o dicionário usa uma tecnica interna chamada hashing, que
# para funcionar corretamente, a chave precisa ter: valor e hash constante
# Se a chave mudasse, Python nao a encontraria mais dentro do dicionário.

################################ QUESTAO 2 ###################################################
from abc import ABC, abstractmethod

# CONTRATO (ABC)
class Executavel(ABC):
    @abstractmethod
    def executar(self, entrada: str) -> str:
        # Isso forca os adapters a implementarem
        # exatamente a mesma assinatura, garantindo
        # uniformidade para o cliente
        pass


# SERVIcOS LEGADOS 
class ServicoTextoA:
    def processar(self, texto: str) -> str:
        print("[ServicoTextoA] processando texto...")
        return f"[A]{texto}"


class ServicoTextoB:
    def run(self, payload: dict) -> dict:
        print("[ServicoTextoB] executando run()...")
        data = payload.get("data", "")
        return {"resultado": str(data)[::-1]}


# ADAPTER A
class AdapterA(Executavel):
    def __init__(self, servico_a: ServicoTextoA, pre=None, pos=None):
        self.servico_a = servico_a
        self.pre = pre
        self.pos = pos

    def executar(self, entrada: str) -> str:
        print("\n[AdapterA] Iniciando execucao...")

        # Robustez
        if entrada is None:
            print("[AdapterA] Entrada e None -> substituindo por string vazia.")
            entrada = ""

        if not isinstance(entrada, str):
            print("[AdapterA] Entrada nao e string -> convertendo via str()")
            entrada = str(entrada)

        # Pre
        if callable(self.pre):
            print("[AdapterA] Aplicando pre() na entrada...")
            entrada = self.pre(entrada)
        else:
            print("[AdapterA] Sem funcao pre. Usando entrada original.")

        print(f"[AdapterA] Entrada normalizada = '{entrada}'")

        # Delegando ao servico legado
        print("[AdapterA] Chamando servico_a.processar()...")
        resultado = self.servico_a.processar(entrada)

        print(f"[AdapterA] Resultado bruto do servico A = '{resultado}'")

        # Pos
        if callable(self.pos):
            print("[AdapterA] Aplicando pos() no resultado...")
            resultado = self.pos(resultado)
        else:
            print("[AdapterA] Sem funcao pos. Mantendo resultado original.")

        print(f"[AdapterA] Resultado final = '{resultado}'")
        return resultado


# ADAPTER B
class AdapterB(Executavel):
    def __init__(self, servico_b: ServicoTextoB, pre=None, pos=None):
        self.servico_b = servico_b
        self.pre = pre
        self.pos = pos

    def executar(self, entrada: str) -> str:
        print("\n[AdapterB] Iniciando execucao...")

        # Robustez
        if entrada is None:
            print("[AdapterB] Entrada e None -> substituindo por ''.")
            entrada = ""

        if not isinstance(entrada, str):
            print("[AdapterB] Entrada nao e string -> convertendo via str().")
            entrada = str(entrada)

        # Pre
        if callable(self.pre):
            print("[AdapterB] Aplicando pre()...")
            entrada = self.pre(entrada)
        else:
            print("[AdapterB] Sem funcao pre. Usando entrada original.")

        print(f"[AdapterB] Entrada normalizada = '{entrada}'")

        # Payload esperado por B
        payload = {"data": entrada}
        print(f"[AdapterB] Enviando payload = {payload}")

        # Delegando ao servico legado
        resposta = self.servico_b.run(payload)
        print(f"[AdapterB] Resposta bruta = {resposta}")

        # Validacao
        if (
            not isinstance(resposta, dict)
            or "resultado" not in resposta
            or not isinstance(resposta["resultado"], str)
        ):
            print("[AdapterB] Resposta inválida! Retornando ''.")
            return ""

        resultado = resposta["resultado"]

        # Pos
        if callable(self.pos):
            print("[AdapterB] Aplicando pos()...")
            resultado = self.pos(resultado)
        else:
            print("[AdapterB] Sem funcao pos. Mantendo resultado original.")

        print(f"[AdapterB] Resultado final = '{resultado}'")
        return resultado
