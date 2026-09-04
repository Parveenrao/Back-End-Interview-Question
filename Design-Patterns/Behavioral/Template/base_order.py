from abc import ABC , abstractmethod

class OrderProcessor(ABC):

    """ Define overall ordering process workflow
    
        Subclass customize payment and notification steps
    """

    def process_order(self) -> None:

        self.validate_order()
        self.calculate_total()
        self.process_payment()
        self.generate_invoice()
        self.send_notifications()

    def validate_order(self)-> None:

        print("validating order")

    def calculate_total(self) -> None:
        print("Calculating total")

    def generate_invoice(self) -> None:
        print("Generating invoice")    
 
    @abstractmethod
    def process_payment(self) -> None:

        "Process payment"

        raise NotImplementedError
    
    @abstractmethod
    def send_notifications(self) -> None:

        "Send notifications"

        raise NotImplementedError
    
    
