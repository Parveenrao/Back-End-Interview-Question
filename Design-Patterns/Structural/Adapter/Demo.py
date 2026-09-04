""" 

=> Adapter Design Pattern

    -> Adapter Design Pattern is a structural design pattern that allow two incompatible
       interface to work together without changing their existing code 

    -> Translator between two classes 


    -> Example 

       Imagine we are travelling from India to UK

       1. Laptop has charger has an indian plug 
       2. UK wall socket accpet only uk plug

       You don't modify your charger 
       You don't the wall socket 

       Instead we use travel adapter 

       Indian charger --> Adapter ---> UK socket 

       Adapter convert one interface into another 

       Adapter Pattern does exactly the same thing in software    


"""


# Problem , Suppose my application execepts every payment provider to have this interface 

class PaymentGateway:
    def pay(self , amount : float):
        pass 

# now we want to integrate third party payment sdk and its interface is completely differently 


class StripeSDK:
    def make_payment(self, total):
        print(f"Paid {total}")

# my application calls , gateway.pay(100) but stipe call only stipe.make_payment(100)  , interface don;t match


# so adapter converts the interface of one class into another interface that the client expects 
