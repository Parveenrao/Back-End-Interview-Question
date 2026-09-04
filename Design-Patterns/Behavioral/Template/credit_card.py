from base_order import OrderProcessor

class CreditCardOrderProcessor(OrderProcessor):

    def process_payment(self) -> None:
        print("Charging credit card")

    def send_notifications(self) -> None:
        print("Sending receipt via email")    