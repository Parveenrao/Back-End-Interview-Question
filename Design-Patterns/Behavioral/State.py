"""  
=> State Design Pattern 
    -> It is behavioral design pattern that lets an object change its behavior when its internal state change , without using 
        if-else statement 
   
   -> Example , Mobile Phone 
      
      Locked -> you cant use apps 
      Unlocked -> You can use apps
      
      Same phone different behavior 
            
"""


# State interface
 
from abc import ABC , abstractmethod

class State(ABC):
    @abstractmethod
    def handle(self):
        pass


# Concrete states 

class LockedState(State):
    def handle(self , context):
        print("Phone is locked. Unlocking now ....")
        context.set_state(UnlockedState())

class UnlockedState(State):
    def handle(self , context):
        print("Phone is Unlocked. Locking now ...")
        context.set_state(LockedState())
        

# Contex state

class Phone:
    def __init__(self):
        self.state = LockedState()
    
    def set_state(self, state):
        self.state = state
    
    def press_button(self):
        self.state.handle(self)    
        
        

phone = Phone()

phone.press_button()

phone.press_button()                    
                    