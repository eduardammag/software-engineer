# Transformar cada ação que pode ser feita em uma instancia e podemos enfileirar elas 
# Ações se tornam um objeto
# Padrão comando

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Optional

# Receptor: quem recebe os comandos, no exemplo o editor de texto é o receptor
class TextEditor:
    def __init__(self)-> None:
        self._text =""

    def add_text(self, new_text: str)-> None:
        self._text += new_text

    def remove_text(self, length: int) -> str:
        removed = self._text[-length:]
        self._text = self._text[:-length]

        return removed

    def show(self) -> None:
        print(f"Texto atual: \"{self._text}\"")

class  Command(ABC):
    @abstractmethod
    def execute(self)-> None:
        pass

    @abstractmethod
    def undo(self)-> None:
        pass
    
# Quem pede para fazer algo não conhece a lógica para fazer
class  AddTextCommand(Command):
    def __init__(self, editor: TextEditor, text: str) -> None:
        self.editor = editor
        self.text = text
        self._executed = False

    def execute(self)-> None:
        self.editor.add_text(self.text)
        self._executed = True

    def undo(self)-> None:
        if self._executed:
            self.editor.remove_text(len(self.text))
            self._executed = False

class  RemoveTextCommand(Command):
    def __init__(self, editor: TextEditor, length: int) -> None:
        self.editor = editor
        self.length = length
        self._removed_text: Optional[str] = None

    def execute(self)-> None:
        self._removed_text = self.editor.remove_text(self.length)

    def undo(self)-> None:
        if self._removed_text:
            self.editor.add_text(self._removed_text)
            self._removed_text = None

# Macro comand: um comando que contém outros comandos
class MacroCommand(Command):
    def __init__(self, commands: List[Command])-> None:
        self.commands = commands

    def execute(self) -> None:
        for cmd in self.commands:
            cmd.execute()

    def undo(self)-> None:
        for cmd in reversed(self.commands):
            cmd.undo()

# Quem vai receber os comandos e manipular o receptor, executar os comandos
class CommandInvoker:
    def __init__(self)-> None:
        self._history: List[Command] = []
        self._redo_stack: List[Command] = []

    def execute_command(self, command: Command) -> None:
        command.execute()
        self._history.append(command)
        self._redo_stack.clear()

    def undo(self) -> None:
        if not self._history:
            print("Nada a desfazer")
            return
        
        last_comand = self._history.pop()
        last_comand.undo()
        self._redo_stack.append(last_comand)

    def redo(self) -> None:
        if not self._redo_stack:
            print("Nada a refazer")
            return
        command = self._redo_stack.pop()
        command.execute()
        self._history.append(command)

    def show_history(self)-> None:
        for i, cmd in enumerate(self._history, start=1):
            print(f"{i}. {cmd.__class__.__name__}")


editor = TextEditor()
invoker = CommandInvoker()

add_hello = AddTextCommand(editor, "Olá, ")
add_message = AddTextCommand(editor, "eu adoro  a emap")

# CLIENTE
invoker.execute_command(add_hello)
invoker.execute_command(add_message)

editor.show()
invoker.show_history()

invoker.undo()
editor.show()
invoker.redo()
editor.show()

macro = MacroCommand([
    AddTextCommand(editor, "\n Eu "),
    AddTextCommand(editor, "adoro"),
    AddTextCommand(editor, "o Camacho")

    ])

invoker.execute_command(macro)
editor.show()

invoker.undo()
editor.show()
