# Third part SDK (Adapter) , we cannot modify it


class StripeSDK:

    """Third Party Library"""

    def make_payment(self, total:float)-> None:
        print(f"[Stripe] successfully charged {total : 2f}")