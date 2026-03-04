# High level module doest not depend on low level module 
# Both depent on abstraction 

# ------------------------------ Bad Design --------------------------

class MySqlDatabase:
    
    def save_user(self , user):
        print("Saving user to db")
        

class UserService():
    def __init__(self):
        self.db = MySqlDatabase()
        
    
    def create_user(self):
        self.db.save_user()
        

# user service tightly coupled to Database 



# -------------------------------- Good Design --------------------------------


# create abstraction 

from abc  import ABC , abstractmethod

class Database(ABC):
    
    @abstractmethod
    def save(self, data):
        pass
    
    
    
# Implement database 

class Mysql(Database):
    
    def save(self, data):
        print("Saving to mysql database")
        

class PostgresDatabase(Database):
    
    def save(self , data):
        print("Saving data to postgress")
        
        
# Use abstraction in service


class UserService:
    def __init__(self  , db:Database):
        self.db = db
    
    def create_user(self, user):
        self.db.save(user)
        
        
db = MySqlDatabase()

service = UserService(db) 

service.create_user("parveen")           