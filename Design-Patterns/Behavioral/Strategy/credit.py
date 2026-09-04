# Credit Card Strategy 

from strategy import PaymentStrategy

class CreditCardStrategy(PaymentStrategy):

    def pay(self , amount : float) -> None:
        print(f"Paid Rs{amount : 2f} using credit card")

        