""" 
=> Projection 
    
    -> Shape control 
    
    -> Controlling the shape of data returned to your application

    -> Include mode
    
        db.users.find({} , {name : 1 , email : 1})
          
          only name and email will come
    
    -> exclude mode
          
          db.users.find({}, { password: 0 })
          
          everything except password
    
    -> Exception 
        
        db.users.find({} , {name : 1  _id : 0})
        
          we can exclude id even in include mode
    
    -> Example BAD API 
        
        db.user.find({status :active})
           
           return password , tokens  , internals fiedls
    
          
    -> Correct API       
           -> db.users.find({ status: "active" },{ name: 1, email: 1, _id: 0 })
    
    
    -> Nested Fields 
              
              db.users.find({}, { "address.city": 1 })
            
            only city will come from address 
    
    
    -> Array Projection 
       
       1. Limited Array Size 
             
             db.posts.find({}, { comments: { $slice: 2 } })     
             
             only 2 comments
             
          ->  last element 
                 
                 {slice : -2}   
          
          -> skip + limit 
                
                { comments: { $slice: [5, 3] } }
                
                  skip 5 and return next 3
           
           -> Elematch 
                   
                   db.students.find({ scores: { $elemMatch: { $gt: 80, $lt: 90 }}})  
                   
                   match with exact one element score : [70 , 80 ,90] , 85 will ans , normal match  return something differnt                            
                                    


"""