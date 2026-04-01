""" Passing objects/dependencies from outside instead of creating them from inside  ,
    
    Dont create dependecies , recieve them 
    
-----------------------------------------------------------------------------------------------------
    
=> Wihtout DI 

    classMysqlDatabase:
        def connect(self):
            print("mysql connected)
    
    
    class UserService:
        
        def __init__(self): 
           self.db = MysqlDatabase             -> TIght coupling , voilate software design principles 
        
        
        def get_user(self): 
           self.db.connect()     
           


=> WIth DI 

class Database:
     def connect(self):
          passs



    classMysqlDatabase:
        def connect(self):
            print("mysql connected)
    
    
    class UserService:
        
        def __init__(self , db : Database): 
           self.db =    db                     -> Loose coupling 
        
        
        def get_user(self): 
           self.db.connect()   
           

db = MysqlDatabse
service = UserService(db)             
                                   
    
    """