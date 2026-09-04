class InventoryService:

    """Handle Inventory operations"""

    def reserve_item(self , product_id : str , quantity : int) -> None:

        print(
            f"[inventory] Reserved {quantity} unit(s) of {product_id}")