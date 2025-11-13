"""
Padrão de Projeto: COMMAND (Comando)
==========================================================
 Ideia principal:
------------------
Transformar **cada ação** (como "adicionar texto" ou "remover texto")
em um **objeto independente** — chamado de *Comando*.

Isso permite:
- Armazenar ações (para desfazer/refazer).
- Enfileirar comandos (executar vários depois).
- Desacoplar quem *pede* a ação de quem *executa* a ação.

 Estrutura básica:
----------------------------------
Cliente → Invoker → Command → Receiver

- Cliente: cria os comandos.
- Invoker: executa, desfaz e refaz os comandos.
- Command: encapsula a ação.
- Receiver: o “alvo” que realmente faz o trabalho.
==========================================================
"""

from abc import ABC, abstractmethod
from typing import List, Optional

# ==========================================================
# RECEPTOR (Receiver)
# ==========================================================
class EditorDeTexto:
    """
    O receptor é o objeto que realmente realiza as ações.
    Aqui, o EditorDeTexto sabe adicionar, remover e mostrar o texto.
    """
    def __init__(self) -> None:
        self._texto = ""

    def adicionar_texto(self, novo_texto: str) -> None:
        """Adiciona texto ao final do conteúdo atual."""
        self._texto += novo_texto

    def remover_texto(self, tamanho: int) -> str:
        """Remove os últimos 'tamanho' caracteres e retorna o texto removido."""
        removido = self._texto[-tamanho:]
        self._texto = self._texto[:-tamanho]
        return removido

    def mostrar(self) -> None:
        """Exibe o texto atual no editor."""
        print(f" Texto atual: \"{self._texto}\"")


# ==========================================================
# CLASSE BASE PARA COMANDOS (Command)
# ==========================================================
class Comando(ABC):
    """
    A interface base para todos os comandos.
    Define os métodos obrigatórios que todos os comandos precisam implementar.
    """
    @abstractmethod
    def executar(self) -> None:
        """Executa a ação do comando."""
        pass

    @abstractmethod
    def desfazer(self) -> None:
        """Desfaz a ação (se possível)."""
        pass


# ==========================================================
# COMANDOS CONCRETOS
# ==========================================================
class AdicionarTextoComando(Comando):
    """
    Comando concreto: adiciona texto no editor.
    """
    def __init__(self, editor: EditorDeTexto, texto: str) -> None:
        self.editor = editor
        self.texto = texto
        self._executado = False  # Marca se o comando já foi executado

    def executar(self) -> None:
        self.editor.adicionar_texto(self.texto)
        self._executado = True

    def desfazer(self) -> None:
        if self._executado:
            self.editor.remover_texto(len(self.texto))
            self._executado = False


class RemoverTextoComando(Comando):
    """
    Comando concreto: remove texto do editor.
    """
    def __init__(self, editor: EditorDeTexto, tamanho: int) -> None:
        self.editor = editor
        self.tamanho = tamanho
        self._texto_removido: Optional[str] = None

    def executar(self) -> None:
        # Remove o texto e guarda o que foi apagado para poder desfazer depois
        self._texto_removido = self.editor.remover_texto(self.tamanho)

    def desfazer(self) -> None:
        if self._texto_removido:
            # Recoloca o texto removido de volta
            self.editor.adicionar_texto(self._texto_removido)
            self._texto_removido = None


# ==========================================================
# MACRO COMANDO (composto por vários comandos)
# ==========================================================
class MacroComando(Comando):
    """
    Um comando que contém uma lista de outros comandos.
    Permite executar vários comandos de uma vez (como um “macro”).
    """
    def __init__(self, comandos: List[Comando]) -> None:
        self.comandos = comandos

    def executar(self) -> None:
        # Executa todos os comandos na ordem
        for cmd in self.comandos:
            cmd.executar()

    def desfazer(self) -> None:
        # Desfaz na ordem inversa (último a executar, primeiro a desfazer)
        for cmd in reversed(self.comandos):
            cmd.desfazer()


# ==========================================================
# INVOKER (quem solicita os comandos)
# ==========================================================
class InvocadorDeComandos:
    """
    O Invoker é responsável por executar, desfazer e refazer comandos.
    Ele não sabe como o comando funciona — apenas o chama.
    """
    def __init__(self) -> None:
        self._historico: List[Comando] = []     # Histórico de comandos executados
        self._pilha_refazer: List[Comando] = [] # Comandos desfeitos que podem ser refeitos

    def executar_comando(self, comando: Comando) -> None:
        comando.executar()
        self._historico.append(comando)
        self._pilha_refazer.clear()  # Ao executar algo novo, zera o histórico de refazer

    def desfazer(self) -> None:
        if not self._historico:
            print(" Nada a desfazer.")
            return
        ultimo = self._historico.pop()
        ultimo.desfazer()
        self._pilha_refazer.append(ultimo)

    def refazer(self) -> None:
        if not self._pilha_refazer:
            print(" Nada a refazer.")
            return
        comando = self._pilha_refazer.pop()
        comando.executar()
        self._historico.append(comando)

    def mostrar_historico(self) -> None:
        print("\n Histórico de comandos executados:")
        for i, cmd in enumerate(self._historico, start=1):
            print(f"{i}. {cmd.__class__.__name__}")


# ==========================================================
# CLIENTE (quem cria e envia os comandos)
# ==========================================================
if __name__ == "__main__":
    editor = EditorDeTexto()
    invocador = InvocadorDeComandos()

    # Criamos comandos individuais
    cmd_ola = AdicionarTextoComando(editor, "Olá, ")
    cmd_mensagem = AdicionarTextoComando(editor, "eu adoro a EMAp!")

    # CLIENTE executa os comandos via Invocador
    invocador.executar_comando(cmd_ola)
    invocador.executar_comando(cmd_mensagem)

    editor.mostrar()
    invocador.mostrar_historico()

    # DESFAZER último comando
    invocador.desfazer()
    editor.mostrar()

    # REFAZER comando desfeito
    invocador.refazer()
    editor.mostrar()

    # =====================================================
    # EXEMPLO DE MACROCOMANDO (vários comandos juntos)
    # =====================================================
    macro = MacroComando([
        AdicionarTextoComando(editor, "\nEu "),
        AdicionarTextoComando(editor, "adoro "),
        AdicionarTextoComando(editor, "o Camacho ")
    ])

    invocador.executar_comando(macro)
    editor.mostrar()

    # Desfaz a macro inteira (reverte todos os comandos dentro dela)
    invocador.desfazer()
    editor.mostrar()
