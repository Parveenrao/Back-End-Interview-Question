from strategy import PaymentStrategy

class UPIStrategy(PaymentStrategy):

    def pay(self , amount :float) -> None:

        print(f"Paid Rs{amount :2f} using UPI ")