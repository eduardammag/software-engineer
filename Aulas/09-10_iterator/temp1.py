# iterador
# Percorrer os elementos de uma coleção sem expor as características dessa coleção


class SocialFeed:
    def __init__(self):
        self._items = []
        self._mod_count = 0 # contagem da modificações do agregado

        # Tudo que falha, tem que falhar rápido
    def add(self, post: str):
        self._items.append(post)
        self._mod_count += 1

    def __len__(self):
        return len(self._items)
    
    def __iter__(self): # Quando finimos iter, se torna iterável. Como iterar com o for
        return ForwardIterator(self) # o iterador é FowardIterator # comportamento padrão é ir pra frente
     
    def iter_forward(self): # comportamento padrão
        return ForwardIterator(self)

    def iter_reverse(self): # definimos outras forma, que podemos escolher
        return ReverseIterator(self)
    
    def iter_filter(self, predicate): # em  comp um predicado é toda função que avalia e retorna true ou false
        return FilterIterator(self, predicate)
    
    def _get_snapshot(self): # método interno, usado pelo iteradores, foto da coleção de quando os iters foram criados, se a coleção mudar o iter tem que morrer
        # Fail fast
        return list(self._items), self._mod_count
    
class ForwardIterator:
    def __init__(self, collection: SocialFeed):
        self._collection = collection
        self._snapshot, self._expected_mod = collection._get_snapshot()
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._expected_mod != self._collection._mod_count: # se a coleção tiver diferente da foto, ele para
            raise RuntimeError("Coleção invalidada em tempo de execução")
        if self._index >= len(self._snapshot):
            raise StopIteration
        item = self._snapshot[self._index]
        self._index += 1
        return item
    
class ReverseIterator:
    def __init__(self, collection: SocialFeed):
        self._collection = collection
        self._snapshot, self._expected_mod = collection._get_snapshot()
        self._index = len(self._snapshot) -1

    def __iter__(self):
        return self

    def __next__(self):
        if self._expected_mod != self._collection._mod_count: # se a coleção tiver diferente da foto, ele para
            raise RuntimeError("Coleção invalidada em tempo de execução")
        if self._index < 0 :
            raise StopIteration
        
        item = self._snapshot[self._index]
        self._index -= 1
        return item
    


class FilterIterator:
    def __init__(self, collection: SocialFeed, predicate):
        self._collection = collection
        self._predicate = predicate # é uma função que ira usar para fazer a filtragem
        self._snapshot, self._expected_mod = collection._get_snapshot()
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._expected_mod != self._collection._mod_count: # se a coleção tiver diferente da foto, ele para
            raise RuntimeError("Coleção invalidada em tempo de execução")
        while self._index < len(self._snapshot):
            item = self._snapshot[self._index]
            self._index += 1
            if self._predicate(item):
                return item
        raise StopIteration 

feed = SocialFeed()
feed.add("Post 1 - bem-vindo!")
feed.add("Post 2 - Novidades!")
feed.add("Post 3 - Alerta Fake News!")
feed.add("Post 4 - Virginia News!")
feed.add("Post 5 - Grr!")

for each_post in feed:
    print(" -> ", each_post)


print("\n\n")

for each_post in feed.iter_reverse():
    print(" -> ", each_post)

print("\n\n")

for each_post in feed.iter_filter(lambda s: "Virginia" in s):
    print(" -> ", each_post)