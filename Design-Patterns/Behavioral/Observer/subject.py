# Subject Interface 


from abc import ABC , abstractmethod

from observer import Observer


class Subject(ABC):
    "Interface for subject"

    @abstractmethod
    def attach(self , observer : Observer) -> None:
        pass 

    @abstractmethod
    def detach(self , observer : Observer) -> None:
        pass 

    @abstractmethod
    def notify(self) -> None:
        pass

""" 

=> Every subject shoudl support 

    1. Register observer 
    2. Remove observer 
    3. Notify all observer 



"""    
    