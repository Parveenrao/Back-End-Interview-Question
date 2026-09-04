from gateway import PaymentGateway
from stipe_sdk import StripeSDK
from stripe_adapter import StripeAdapter
from client import PaymentService


def main() -> None:

    stripe_sdk = StripeSDK()

    adapter = StripeAdapter(stripe_sdk)

    payment_service = PaymentService(adapter)

    payment_service.checkout(499.99)

if __name__ == "__main__":
    main()
