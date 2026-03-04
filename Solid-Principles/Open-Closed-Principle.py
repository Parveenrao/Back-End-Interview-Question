""" OCP -> Open for extension 
        -> Closed for modification 
        -
     
    Means you shoud be able to add new behaviour 
    Without changing existing code
    """


# ------------ Bad Example ----------------------------

class PaymentService:
    
    def pay(self , method):
        
        if method == "stripe":
            print("Stripe payment")
        
        elif method == "UPI":
            print("UPI Payment")
            
        elif method == "Razorpay":
            print("Razorpay payment")


# Now suppose we want to add Apple pay , Whatsapppay , si modify class again and again 
# So many if-else conditions , Hard to maintain , risk of breaking code 

#------------------------ Good Example ------------------------------------------------------

# Use polymorphism 


# Create abstraction 

from abc import ABC , abstractmethod

class Payment(ABC):
    
    @abstractmethod
    def pay(self, amount:float):
        pass
    
# Implement Payments type 

class UPIPayment(Payment):
    
    def pay(self , amount : float):
        print(f"Processing : {amount} via by UPIPayment")
        

class PayPalPayment(Payment):
    
    def pay(self , amount : float):
        
        print(f"Processing {amount} via Paypal")
        
class Razorpay(Payment):
    
    def pay(self, amount : float):
        
        print(f"Processing {amount} via Razorpay")
 
 
 
# Payment Factory Centralized Payment System 

class PaymentFactory:
    
    payments = {
        
        "razorpay" : Razorpay,
        "paypal" : PayPalPayment,
        "upi" : UPIPayment
    }                     
    
    
    @staticmethod 
    def create_payment(payment_type : str) -> Payment:
        
        payment_class = PaymentFactory.payments.get(payment_type)        
        
        if not payment_class:
            raise ValueError("Unsupported payment type")
        
        return payment_class()
    
                          
# Payment Service 

class PaymentService:
    
    def __init__(self , payment :Payment):
        self.payment = payment 
    
    def process_payment(self , amount:float):
        self.payment.pay(amount)
        
 
# Client COde


payment = PaymentFactory.create_payment("upi") 

service = PaymentService(payment) 

service.process_payment(100)                                   