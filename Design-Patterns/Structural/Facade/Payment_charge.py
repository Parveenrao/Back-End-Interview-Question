class PaymentService:

    """ Handle Payment Processing"""

    def charge(self, amount : float) -> None:
        print(f"[Payment] Charged Rs {amount : 2f}")