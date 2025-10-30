#  Padrão de Projeto Decorator — Exemplo Genérico

##  Objetivo

Este exemplo demonstra o **padrão de projeto Decorator** de forma genérica — mostrando como **adicionar comportamentos dinamicamente** a um objeto **sem modificar sua classe original**.

---

##  Ideia Principal

O padrão **Decorator** permite empilhar objetos que implementam a **mesma interface**.
Cada decorator **envolve** o objeto anterior e **adiciona comportamento extra**, antes ou depois de delegar a chamada ao componente real.

---

## 🏗️ Estrutura dos Arquivos

```
decorator_exemplo_generico/
│
├── componente_base.py          # Interface base (Componente)
├── componente_concreto.py      # Implementação concreta do componente
├── decorator_base.py           # Classe base para todos os decoradores
├── decorators_concretos.py     # Decoradores específicos (A e B)
└── main.py                     # Exemplo de uso
```

---

##  Fluxo de Funcionamento

1. `ComponenteConcreto` é o objeto principal (núcleo do comportamento).
2. `Decorator` é uma classe abstrata que **recebe um componente** e o envolve.
3. `DecoratorA` e `DecoratorB` são decoradores concretos que **adicionam comportamentos extras**.
4. O cliente pode empilhar decoradores livremente, por exemplo:

   ```python
   componente = ComponenteConcreto()
   decorado = DecoratorB(DecoratorA(componente))
   ```

   Resultado final:
   ```
   DecoratorB(DecoratorA(ComponenteConcreto))
   ```

---

##  Conceitos-Chave

- **Composição > herança:** Decorator permite adicionar responsabilidades sem criar subclasses.
- **Flexibilidade:** Comportamentos podem ser combinados em tempo de execução.
- **Transparência:** Todos os objetos compartilham a mesma interface (`Componente`).

---

##  Benefícios

- Evita a explosão de subclasses.
- Permite adicionar comportamentos de forma modular.
- Facilita manutenção e extensão do sistema.

---

