from Inventory_service import InventoryService

from Invoice_gen import InvoiceService

from notification import NotificationService

from shipping import Shipping

from Payment_charge import PaymentService


class OrderFacade:

    """ Facade that coordinate the whole order management system"""

    def __init__(self,
                 
                 inventory : InventoryService,
                 payment : PaymentService,
                 shipping : Shipping,
                 notification : NotificationService,
                 invoice : InvoiceService) -> None:
        
        self.inventory = inventory
        self.payment = payment
        self.shipping = shipping
        self.notification = notification
        self.invoice = invoice


    def place_order(self , order_id : str , product_id : str, quantity :int , amount : float ,
                    customer_email : str) -> None:

        print("==============Placing Order==================")

        self.inventory.reserve_item(product_id , quantity)
        self.payment.charge(amount)
        self.invoice.generate(order_id)
        self.shipping.schedule(order_id)
        self.notification.send_confirmation(customer_email)

        print("==========Order Completed==========")    