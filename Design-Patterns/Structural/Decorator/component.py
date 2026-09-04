from abc import ABC , abstractmethod

class Coffee(ABC):
    """Component Interface"""

    @abstractmethod
    def description(self) -> str:
        pass

    @abstractmethod
    def cost(self) -> float:
        pass


class SimpleCoffee(Coffee):
    """concrete component"""

    def description(self) -> str:
        return "simple coffee"

    def cost(self) -> float:
        return 50.0     