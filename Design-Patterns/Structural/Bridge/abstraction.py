# Bridge , Notification -> Has - a -> Notification Sender 

from abc import ABC , abstractmethod
from Implementor import NotificationSender

class Notification(ABC):

    """ Holds Reference to the Notification sender """

    def __init__(self, sender : NotificationSender) -> None:
        self._sender = sender

    @abstractmethod
    def notify(self , message : str) -> None:
            pass