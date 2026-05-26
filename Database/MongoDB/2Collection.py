""" 
=> Collection In MongoDB 
    
    -> Group of documents stored together (Like table in sql)
    
    
    -> A collection = Container 
        
        Document = rows
    
    -> Automatic creation 
        
        db.users.insertOne({"name":"parveen"}) 
        
          users collection is created automatically
      
      
      Internally , collection holds bson
    
    
    -> Basic Operation 
         
         1. Create explicitly collection 
             
             db.createCollection("users) 
             
             insert -> db.users.insertOne({"name" : "Parveen"})     
          
          2. Find 
             
             db.users.find()
          
          3. Drop collection 
              
              db.users.drop()         



"""