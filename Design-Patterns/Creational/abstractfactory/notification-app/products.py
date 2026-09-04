from abc import ABC , abstractmethod

class EmailSender(ABC):

    "Interface for sending email"
    @staticmethod
    def send(self , recipient : str , message : str) -> None:
        raise NotImplementedError


class SmsSender(ABC):
    "Interface for sending SMS"

    @staticmethod
    def send(self , phone_number : str , message : str) -> None:
        raise NotImplementedError    