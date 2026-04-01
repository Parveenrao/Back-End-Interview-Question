"""  
=> Builder Pattern 
    
    -> Used to contruct obejct step by step 
    
    -> When to use
       1. Too many constructor parameters 
       2. Optional fields everywhere 
       3. Complext object creation 
"""


# Bad Design 

class User1:
    def __init__(self, name, age, email=None, phone=None, address=None):
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone
        self.address = address

# Builder Pattern Implementation 

class User:
    def __init__(self):
        self.name     = None
        self.age      = None
        self.email    = None
        self.phone    = None
        self.address  = None
        
    def __str__(self):
        return f"{self.name}, {self.age}, {self.email}, {self.phone}, {self.address}"    
    

class Builder:
    def __init__(self):
        self.user = User()
        
    def set_name(self, name):
        self.user.name = name  
        
        return self   
    
    
    def set_age(self, age):
        self.user.age = age 
        
        return self    
    
    def set_email(self , email):
        self.user.email = email
        return self
    
    def set_phone(self , phone):
        self.user.phone = phone
        return self
    
    def set_address(self, address):
        self.user.address = address
        return self
    
    def build(self):
        return self


user = (
    Builder()
    .set_name("Parveen")
    .set_age(22)
    .set_phone("9999999999")
    .build()
)

print(user)