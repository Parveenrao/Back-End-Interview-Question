# Target Interface 

from abc import ABC , abstractmethod

class PaymentGateway(ABC):
    """ Interface expected by our application """

    @abstractmethod
    def pay(self , amount:float) -> None:
        "process a payment"
        