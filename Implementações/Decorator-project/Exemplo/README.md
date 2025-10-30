# ☕ Padrão de Projeto Decorator — Exemplo Clássico de Bebidas

##  Objetivo

Este exemplo ilustra o **padrão Decorator** de forma intuitiva, simulando uma cafeteria.  
Cada **bebida base** pode receber **adicionais** como leite, açúcar ou chocolate — e cada adicional é um **decorador** que modifica o custo e a descrição.

---

##  Ideia Principal

Em vez de criar dezenas de subclasses para cada combinação de bebida (ex: `CafeComLeiteEAçúcar`),  
usamos decoradores que podem ser **empilhados dinamicamente** em tempo de execução.

---

##  Estrutura dos Arquivos

```
decorator_bebidas/
│
├── bebida.py                # Interface base para todas as bebidas
├── bebidas_concretas.py     # Bebidas básicas: Café, Chá
├── decorator_base.py        # Classe base para adicionais
├── adicionais_concretos.py  # Decoradores concretos: Leite, Açúcar, Chocolate
└── main.py                  # Exemplo de uso
```

---

##  Fluxo de Funcionamento

1. `Cafe` e `Cha` são **bebidas básicas**.
2. `Adicional` é a **classe base** dos decoradores.
3. `Leite`, `Acucar` e `Chocolate` **herdam de `Adicional`** e adicionam custo e descrição.
4. Podemos empilhar quantos adicionais quisermos, por exemplo:

   ```python
   bebida = Chocolate(Leite(Cafe()))
   print(bebida.descricao(), bebida.custo())
   ```

   → `"Café + Leite + Chocolate custa 10.0"`

---

## Conceitos-Chave

- **Evita explosão de subclasses:** não precisamos de `CafeComLeiteEAçucar`.
- **Empilhamento dinâmico:** os adicionais são aplicados em tempo de execução.
- **Mesmo tipo:** todas as bebidas e adicionais implementam a interface `Bebida`.
- **Aberto para extensão, fechado para modificação** (Princípio OCP).

---

##  Benefícios

- Código flexível e extensível.
- Facilidade em adicionar novos adicionais sem tocar nas classes existentes.
- Reutilização de código e baixo acoplamento.

