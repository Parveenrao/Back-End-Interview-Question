""" 
=> YAGNI 
   -> You Arent Goona Need It 

-----------------------------------------------------------------------------

-> IT says 
  
  Don not build something until it is actually required
  
----------------------------------------------------------------------------------

-> Why exist
   
   Most of the developers 
    
    1. Add extra abstraction layers 
    2. Build features for future use  


"""


# Example we are building Notification system 

from abc import ABC , abstractmethod

class Notification(ABC):
    
    @abstractmethod
    def send(self, message):
        pass


class SmsNotification(Notification):
    def send(self , message):
        
        print(f"Sending SMS : {message}")
            
class PushNotification(Notification):
    def send(self , message):
        
        print(f"Sending Push_msg: {message}")   

class EmailNotification(Notification):
    def send(self , message):
        
        print(f"Sending Email : {message}")        
        

class NotificationFactory:
    def create_notification(self, type):
        
        if type == "Email":
            return EmailNotification()
        
        elif type == "sms":
            return SmsNotification()
        
        elif type == "push":
            return PushNotification()


factory = NotificationFactory()

notifier = factory.create_notification("sms")     


notifier.send("Hello Parveen")                 



# Now we need only  sms notification , but we create abstraction layer , 3 classes 