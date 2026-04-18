"""  
=> Connection Pooling 
     
     -> Reusing database connection instead of connecting a new every time 
     
     -> Normally 
        
        App --->  create DB connection  --> runs query --> close connnection --> , for every request 
     
     -> With Pooling 
        
        A pool(group) of pre-created connection in maintained 
        
        App borrows a connection , use it and return it to the pool 
        
        No need to create/destroy repeadetly

--------------------------------------------------------------------------------------------------------------------------     
     
=> Why do we need it 
      
      1. Connection creation is expensive
         
         Creating a db connection  require , handshake , Authentication  , Resource allocation  take milli to seconds 
      
      2. Faster performance 
         
         -> Instead of create -> use -> Destroy 
         
         Resue -> Use -> Return 
      
      
      3. Better Resource Management
         
         -> DB like Postgress , Mysql have limit on max connection  like 1000 connection 
         
         -> Without pooling 
           
           1000 user --> 1000 connections ---> Db crash 
         
         -> With pool
           
           1000 users  --> Maybe 50 connection reused efficiently


---------------------------------------------------------------------------------------------------

=> How It Works (Simple Flow)

    1. Pool starts with N connections (say 10)
    2. Request comes → gets a free connection
    3. Query runs
    4. Connection is returned to pool
    5. Next request reuses it       
    
    

=> Solution 
    
    PgBouncer 
      
      -> PgBouncer is a lightweight connection pooler for PostgresSQL
      
      -> It sites between your application and database manages connection efficiently
      
      App -> PgBouncer -> Postgress
      
      
           Instead of your app opening 1000 DB connections:

           It opens maybe 20–50 connections
           Reuses them smartly
            
    """