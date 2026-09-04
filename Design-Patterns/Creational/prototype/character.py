# Concrete characters 


import copy

from prototype import Prototype

class Character(Prototype):

    def __init__(self , 
                 name : str , 
                 health : str ,
                 strength : str ,
                 skills : list[str],) -> None:
        
        self.name = name 
        self.health = health
        self.strength  = strength
        self.skills = skills

    def clone(self) -> "Character":
        return copy.deepcopy(self)

    def display(self) -> None:

        print("-" *30)
        print(f"Name      : {self.name}")
        print(f"Health    : {self.health}")
        print(f"Strength  : {self.strength}")
        print(f"Skills    : {self.skills}")    