# Command Interface 

from abc import ABC , abstractmethod

class Command(ABC):

    "Abstract command"
    
    @abstractmethod
    def execute(self) -> None:
        "Execute the command"
        pass