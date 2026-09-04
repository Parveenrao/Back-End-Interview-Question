from abc import ABC , abstractmethod

from component import Coffee


class CoffeeDecorator(Coffee , ABC):
    """Base Decorator"""

    def __init__(self , coffee : Coffee) -> None:
        self._coffee = coffee

    def description(self) -> str:
        return self._coffee.description()

    def cost(self) -> float:
        return self._coffee.cost()


class MilkDecorator(CoffeeDecorator):

    """ Add milk"""

    def description(self) -> str: 

        return f"{self._coffee.description()} , Milk"   
    

    def cost(self) -> float:
        return self._coffee.cost() + 10.0
    
class SugarDecorator(CoffeeDecorator):

    """ Add sugar"""

    def description(self) -> str:

        return f"{self._coffee.description()} Sugar"

    def cost(self) -> float:
        return self._coffee.cost() + 5.0
    

class WhippedCreamDecorator(CoffeeDecorator):
    """ Adds whipped cream"""

    def description(self) -> str:
        return f"{self._coffee.description()} WhippedCream" 


    def cost(self) -> float:
        return self._coffee.cost() + 20.0    


