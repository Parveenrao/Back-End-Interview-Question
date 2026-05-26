""" 
=> References 
    
    -> Storing related data in separate collection and linking via IDs
    
    -> Instead of nested everything , you connect document using a key 
    
       { _id: "A", name: "Parveen" }
       
       
       { _id: 1, user_id: "A", item: "Laptop", price: 50000 }
       
       find related orders 
         
         db.user.find({'user_id" : "A"})
    
    
    -> When to use referneces 
       
       1. Data grows unbounded 
            
            orders 
            transaction 
            logs
       
       2. Data accesssed independently
            
            orders without users 
            product without reviews 
        
        3. Many to many relationship              


"""