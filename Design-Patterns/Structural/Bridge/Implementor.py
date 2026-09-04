from abc import ABC , abstractmethod

class NotificationSender(ABC):

    @abstractmethod
    def send(self , message : str) -> None:

        pass 


    