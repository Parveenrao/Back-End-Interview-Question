# CLient never know stripe exist 

from gateway import PaymentGateway

class PaymentService:
    def __init__(self , gateway : PaymentGateway) -> None:
        self._gateway = gateway

    def checkout(self , amount : float) -> None:

        print("Starting checkout")

        self._gateway.pay(amount)

        print("Checkout completet")    