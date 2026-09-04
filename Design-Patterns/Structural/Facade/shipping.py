class Shipping:

    """ Schedule shipment"""

    def schedule(self, order_id : str) -> None:

        print(
            f"[Shipping] Shipment scheduled for '{order_id}"
        )