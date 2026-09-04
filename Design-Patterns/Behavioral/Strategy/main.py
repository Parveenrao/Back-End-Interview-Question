from credit import CreditCardStrategy
from paypal import PaypalStrategy
from Upi import UPIStrategy
from processor import PaymentProcessor


def main() -> None:

    processor = PaymentProcessor(CreditCardStrategy())

    processor.checkoout(350)

    processor.strategy = PaypalStrategy()

    processor.checkoout(450)

    processor.strategy = UPIStrategy()

    processor.checkoout(550)


if __name__ == "__main__":
    main() 
