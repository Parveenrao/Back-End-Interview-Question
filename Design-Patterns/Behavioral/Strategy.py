"""  
=> Strategy Pattern
    
    -> Define multiple way to do something , but switch  between them at runtime 
    
"""

# Create Strategy Interface 

from abc import ABC , abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Concreate Strategy 

class UpiPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using UPI")

class CardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using card")

class WalletPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using wallet")

# Context class 

class PaymentService:
    def __init__(self , strategy : PaymentStrategy):
        self.strategy = strategy
    
    def process_payment(self, amount):
        self.strategy.pay(amount)    
                

service = PaymentService(UpiPayment())
service.process_payment(100)                

service1 = PaymentService(CardPayment())
service1.process_payment(2000)                
                       

#---------------------------------------------------------------------------------------------

# Now proper production grade code

import logging

# setup logging
logging.basicConfig(level=logging.INFO)

# Strategy interface 
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self , amount : float):
        pass

# Concrete Strategy 

class UPIPayment(PaymentStrategy):
    def pay(self, amount:float):
        
        if amount < 0:
            raise ValueError("Amount must be greater than 0")
        
        logging.info("Processing UPI Payment")
        
        return {
            "status" : "success",
            "method" : "UPI",
            "amount" : amount
        }

class CARDPayment(PaymentStrategy):
    def pay(self, amount:float):
        
        if amount < 0:
            raise ValueError("Amount must be greater than 0")
        
        logging.info("Processing CARD Payment")
        
        return {
            "status" : "success",
            "method" : "CARD",
            "amount" : amount
        }        

class WALLETPayment(PaymentStrategy):
    def pay(self, amount:float):
        
        if amount < 0:
            raise ValueError("Amount must be greater than 0")
        
        logging.info("Processing WALLET Payment")
        
        return {
            "status" : "success",
            "method" : "WALLET",
            "amount" : amount
        }        

# Factory 

class PaymentFactory:
    
    @staticmethod
    def get_strategy(method : str) ->  PaymentStrategy:
        
        mappings = {
            "upi" : UPIPayment(),
            "card" : CARDPayment(),
            "wallet" : WALLETPayment()
        }
        
        strategy = mappings.get(method.lower())
        
        if not strategy:
            raise ValueError(f"Unsupported Payment method : {method}")
        
        return strategy

# Context class 

class PaymentService:
    def __init__(self , strategy : PaymentStrategy):
        self.strategy = strategy
    
    def process_payment(self , amount :float):
        try:
            logging.info("Staring payment process")
            
            result = self.strategy.pay(amount)
            
            logging.info("Payment successful")
            
            return result
        
        except Exception as e:
            logging.error("Payment Failled : {str(e)}")
            
            result= {
                "status" : "failed",
                "error" : str(e)
            }
                 


if __name__ == "__main__":
    
    method = 'upi'
    amount = 100
    
    strategy = PaymentFactory.get_strategy(method)
    
    service = PaymentService(strategy)
    
    response = service.process_payment(amount)
    
    print(response)                 
        
    