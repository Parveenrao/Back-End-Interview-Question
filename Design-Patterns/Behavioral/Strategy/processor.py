from strategy import PaymentStrategy


class PaymentProcessor:

    def __init__(self , strategy : PaymentStrategy) -> None:
        self._strategy = strategy


    @property
    def strategy(self) -> PaymentStrategy:
        return self._strategy


    @strategy.setter
    def strategy(self, strategy:PaymentStrategy) -> None:
        self._strategy = strategy

    def checkoout(self , amount : float) -> None:
        self._strategy.pay(amount)    