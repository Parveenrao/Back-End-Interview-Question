from gateway import PaymentGateway

from stipe_sdk import StripeSDK


class StripeAdapter(PaymentGateway):

    """Convert our application interface into stripe's interface"""

    def __init__(self  , stripe : StripeSDK) -> None:
        self._stripe = stripe

    def pay(self , amount : float) -> None:
        self._stripe.make_payment(amount)    