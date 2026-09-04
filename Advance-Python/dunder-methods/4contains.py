""" 

=>  __contains___

    -> Is a dunder method that defines what the in operator means for your object 

   



"""

class Team:
    def __init__(self , members):
        self.members = members

    def __contains__(self, name):
        return name in self.members


t = Team(["Parveen" , "Lonely"]) 
print("John" in t)


print("Parveen" in t)
            