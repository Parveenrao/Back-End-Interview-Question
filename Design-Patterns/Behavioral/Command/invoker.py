# Invoker -> invoker does not know what command it is executing 

from command import Command


class RemoteControl:

    def __init__(self) -> None:
        self._command : Command | None = None

    def set_command(self , command : Command) -> None:
        self._command = command


    def press_button(self) -> None:

        if self._command:
            self._command.execute()
