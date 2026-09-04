from base_order import OrderProcessor

class UPIOrderProcessor(OrderProcessor):

    def process_payment(self) -> None:
        print("Processing payment via upi")

    def send_notifications(self) -> None:
        print("Sending UPI payment confirmation")    