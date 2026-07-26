""" 
=> __str___ in python 

     -> control how an object print



"""

class User:
    def __init__(self , name):
        self.name = name 

    def __str__(self):
        return f"user {self.name}"


user = User("Parveen")

print(user)


