"""   
=> Facade 
    -> Is a structural pattern that provide a simple unified inteface to a complex subsytem
    
    -> Hide internal complexity , make system easier to use and maintain
    
 -> when a customer order food 
    1. check menu availability 
    2. prepare food 
    3. Assign waiter / dilvery 
    
  but client only called place_order()      
"""


from dataclasses import dataclass
from typing import Optional , List , Dict
import logging

logging.basicConfig(level=logging.INFO)

@dataclass
class Result:
    success : bool   
    message : str   
    data : Optional[str] = None
    
 
# Menu service 

class MenuService:
    
    def check_item(sefl  , item : str) -> Result:
        menu = ["pizza" , 'buger' , "soup"]
        
        if item not in menu:
            return Result(False , "Item not found in menu")
        
        return Result(True , "Item found")

# kitchen service
class KitchenService:
    def prepare(self, item:str) -> Result:
        return Result(True , f"{item} prepared")

# Billing Service

class BillingService:
    
    def generate_bill(self , item: str) -> Result:
        
        prices = {"pizza" : 300 , "burger" : 200 , "soup" : 100}
        
        amount = prices.get("item" , 0) 
        
        return Result(True , f"Bill generated : {amount}")

class ServiceStaff:
    def serve(self, item:str) -> Result:
        return Result(True , f"{item} served to customer")           
    
# Facade service

class HotelFacade:
    
    def __init__(self):
        self.menu = MenuService()
        self.kitchen = KitchenService()
        self.billing = BillingService()
        self.staff = ServiceStaff()
        
    
    def place_order(self , item : str) -> Result:
        # check menu
        
        res = self.menu.check_item(item)
        
        if not res.success:
            return res
        
        # Prepar food 
        res = self.kitchen.prepare(item)
        
        if not res.success:
            return res
        
        # billing 
        
        bill = self.billing.generate_bill(item)
        
        if not res.success:
            return res
        # 4. serve food
        serve = self.staff.serve(item)
        
        logging.info("Order completed")
        return Result(True, f"{serve.message} | {bill.message}")       
    
if __name__ == "__main__":
    hotel = HotelFacade()

    result = hotel.place_order("pizza")
    print(result)    
    