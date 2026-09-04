# Concrete commands 

from command import Command
from reciever import Light


class TurnOnLight(Command):

    def __init__(self , light : Light) -> None:
        self._light = light

    def execute(self) -> None:
        return self._light.turn_on()


class TurnOfLight(Command):

    def __init__(self , light : Light) -> None:
        self._light = light

    def execute(self) -> None:
        return self._light.turn_off()    