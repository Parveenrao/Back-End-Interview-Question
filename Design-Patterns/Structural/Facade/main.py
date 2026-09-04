from facade import OrderFacade

from Inventory_service import InventoryService
from Invoice_gen import InvoiceService
from notification import NotificationService
from Payment_charge import PaymentService
from shipping import Shipping


def main() -> None:

    facade = OrderFacade(
        inventory=InventoryService(),
        payment=PaymentService(),
        invoice=InvoiceService(),
        shipping=Shipping(),
        notification=NotificationService(),
    )

    facade.place_order(
        order_id="ORD-1001",
        product_id="LAPTOP-001",
        quantity=1,
        amount=79999.0,
        customer_email="parveen@example.com",
    )


if __name__ == "__main__":
    main()