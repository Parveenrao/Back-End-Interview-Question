""" 

=> Dependency 

     -> One class temporarily use another class to do some work 

     -> Class A needs Class B for a taks , but Class A does not permanently store or own Class B



"""

class EmailService:
    def send(self , message):
        print("Sending" , message)

class UserService:
    def notify(self , email_service):
        email_service.send("Welcome") 


email = EmailService()

user = UserService()

user.notify(email)