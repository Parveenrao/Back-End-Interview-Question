"""  => Coupling means how much one component depends on other   
  
          Service A -> Service B 
          
          can service A work without Service B 
          How strongly they are connected

-----------------------------------------------------------------------------

1. Tight Coupling 
    
    -> Two component are strongly dependent on each other. If one changes  the other breaks or need modifications 
    
    example -> A wired earphone user , directly connected to specific phone port , if port changes wired earphone is useless
   
   
    class Mysql:
       def connect(self):
           print("Connect to  MySql")
    
    
    class UserService:
        def __init__(self):
             self.db = Mysql()    -> Tight coupled
        
        
        def get_user(self):
            self.db.connect()               
    
    
    if we change db , then userservice will be useless
    
 -> Hard to test 
 -> Hard to scale 
 -> Hard to chagne 
-----------------------------------------------------------------------------------------------------------

2. Loose Coupling 
   
   -> Components are independent , they interact via interface and abstraction 
   
       A USB Port System 
        
        You can plug keyboard , mouse  , charger  -> no dependency on specific device 
    
    
class Database:
    def connect(self):
        pass
          
    
class MySQLDatabase(Database):
    def connect(self):
        print("Connected to MySQL")

class UserService:
    def __init__(self, db: Database):
        self.db = db  # loosely coupled

    def get_user(self):
        self.db.connect()                    
              


db = MySQLDatabase()
service = UserService(db)


Easy to replace components
Better testing (mock easily)
Scalable systems
Cleaner architecture






















"""
