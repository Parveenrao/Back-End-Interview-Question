"""   
=> Observer Pattern
   
   -> When one object(Subject) changes -> it automatically notifies all its dependencies
   
 -> Example 
    
    Instagram 
    
    You follow someone 
    
    they post you get notification 
    
    You -> observer 
    instagram -> subject   
"""

import logging
from abc import ABC , abstractmethod

# setup logging 

logging.basicConfig(level=logging.INFO)


# Result Model 

from dataclasses import dataclass
from typing import Dict , Optional

@dataclass
class Result:
    success : bool
    message : str
    error   : Optional[str] = None

# Observer interface 

class Obserser(ABC):
    @abstractmethod
    def update(self , event : Dict) -> Result:
        pass

# Concrete Obeserver 

class EmailService(Obserser):
    def update(self , event : Dict) -> Result:
        
        try: 
            
            order_id = event.get("order_id")   
            
            if not  order_id:
                return Result(False , "Missing order_id")
            
            logging.info(f"Email sent for order {order_id}")
            return Result(True , "Email sent")
        
        except Exception as e:
            logging.error(e)
            return Result(False , "Email Failed" , str(e))

class NotificationService(Obserser):
    def update(self, event : Dict) -> Result :
        
        try:
            
            user_id = event.get("user_id")
            
            if not user_id:
                return Result(False , "Missing user_id")
            
            logging.info(f"Notification sent to user {user_id}")
            return Result(True , "Notification sent")
        
        except Exception as e:
            logging.error(e)
            
            return Result(False , "Notification Failed" , str(e))
        

# publisher 

class OrderService:
    def __init__(self):
        self.observers : list[Obserser] = []
    
    def subscribe(self , observer : Obserser) -> None:
        self.observers.append(observer)
        
    def notify(self , event : Dict) -> list[Result]:
        results = []
        
        for observer in self.observers:
            result  = observer.update(event)   
            
            if not result.success:
                logging.info(f"{observer.__class__.__name__} failed: {result.message}")

            results.append(result)

        return results           
                

if __name__ == "__main__":
    order_service = OrderService()

    order_service.subscribe(EmailService())
    order_service.subscribe(NotificationService())

    event = {
        "order_id": 101,
        "user_id": 1
    }

    results = order_service.notify(event)

    for r in results:
        print(r)    