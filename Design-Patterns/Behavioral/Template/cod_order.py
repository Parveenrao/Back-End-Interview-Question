from base_order import OrderProcessor

class CashOnDeliveryOrderProcessor(OrderProcessor):

    def process_payment(self) -> None:
        print("payment will be taken at delivery time")

    def send_notifications(self) -> None:
        print("Sending COD confirmation")

