"""  
=> Factory Design pattern is used to encapsulate the object creation  logic and return object based on input
   without exposing details 
   
   -> Improve , decoupling , OCP , Scalability 
   


=> We will build notification system 
   Email
   SMS
   Push Notification 
   Future -> Whatsapp / slack 
"""

# Base Interface 

from abc import ABC , abstractmethod

class Notification(ABC):
    
    @abstractmethod
    def send(self, message : str):
        pass

class EmailNotification(Notification):
    def send(self, message): 
        print(f"Email : {message}")

class SMSNotification(Notification):
    def send(self, message):
        print(f"SMS : {message}")        
        
class PUSHNotification(Notification):
    def send(self, message):
        print(f"PUSH: {message}")    
        

# Factory class 

class NotificationFactory:
    
    @staticmethod
    def create(notification_type : str) -> Notification:
        
        if notification_type == "email": return EmailNotification()
        
        elif notification_type == "sms" : return SMSNotification()
        
        elif notification_type == "push": return PUSHNotification()
        
        else:
            raise ValueError("Invalid Type")


factory = NotificationFactory.create("sms")

notifier = factory.send("hello Parveen")        


# Now someone ask can you remove if-else then 

class NotificationFactory1:
    
    _mappings = {
        
        "push" : PUSHNotification,
        "sms" : SMSNotification,
        "email" : EmailNotification
    }
    
    @staticmethod
    def create(notification_type : str) -> Notification:
        
        if notification_type not in NotificationFactory1._mappings:
            raise ValueError("Invalid Type")
        
        return NotificationFactory1._mappings[notification_type]()

factory1 = NotificationFactory1.create("push")

notifier1 = factory1.send("Hello Lonely")   
 
#----------------------------------------------------------------------------------------------------------

# Now we buiding Ml models , using factory patterns 

# Base Interface 

from typing import Dict , Type

from abc import ABC , abstractmethod

class Model(ABC):
    
    @abstractmethod
    def predict(self , data):
        pass

# Concrete Models 

class LogisticRegression(Model):
    def __init__(self , weights):
        self.weights = weights
    
    def predict(self , data):
        print("Logistic Regression Predicting")

class RandomForest(Model):
    def __init__(self , n_trees):
        self.n_trees  = n_trees
    
    def predict(self, data):
        print("Random Forest Predicting")

class NeuralNetwork(Model):
    def __init__(self, layers):
        self.layers = layers 
    
    def predict(self , data):
        print("Neural Network Predicting")
 
 
# Model Factory 

class ModelFactory:
    
    _models : Dict[str , Type[Model]]   = {
        
        "logistic" : LogisticRegression,
        "random_forest" : RandomForest,
        "neural_network" : NeuralNetwork
    }    
    
    
    @staticmethod
    def create(model_type , **kwargs) -> Model:
        
        if model_type not in ModelFactory._models:
            raise ValueError (f"Invalid Models. Available {list(ModelFactory._models.keys())}" )      
        
        
        return ModelFactory._models[model_type](**kwargs)          
    
    
config = {
    "type": "random_forest",
    "params": {"n_trees": 100}
}

model = ModelFactory.create(config["type"], **config["params"])
model.predict([1, 2, 3])                                   