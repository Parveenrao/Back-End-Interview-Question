""" Sinlge Responsibilty Principle  

    A class should have only one reason to chanage  and only one resposibility 
    
    Means a class should do one thing and do it well 
    
"""

#---------------- Bad Example --------------------------------------------------

# Image you are building a user system 

class UserService:
    
    def create_user(self, user_data):
        print("create user")
        
    def save_to_database(self , user):
        print("Save user to DB")
        
    def send_welcome_email(self, user):
        print("Send welcome email")

# Now in this class have multiple reason to change , If DB change modify class , If email service change modify classs


# ----------------------Now Good Design is(SRP) -----------------------

# user service (Business logic)

class UserService:
    def create_user(self , user):
        print("Creating user")


# User Repository(Database logic) 

class UserRepository:
    def save(self, user):
        print("Saving user to db") 
        
# Email service (Busniess logic)

class EmailService:
    def send_welcome_email(self , user):
        print("Sending Welcome email")                      