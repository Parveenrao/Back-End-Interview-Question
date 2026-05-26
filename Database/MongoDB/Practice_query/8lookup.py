""" 
=> Lookup 
    
    -> join in mongodb
    
    -> Basic Syntax
        
        {
            $lookup : {
                
                from : "user"             // collection to join
                localField : "userId"     // field in current collection
                foreignField: "_id"       // field in other collection
                as : "userDetails"        // output  array field
            }
        }
        
        
    -> Example 
         
         Orders  -> {userId : 1 , "amount" : 100}
         
         users   -> {_id : 1 , name : "john"}
         
         ordres.userId = users._id = lookup   
                        
                        {
                    "userId": 1,
                    "amount": 100,
                     "userDetails": [{ "_id": 1, "name": "John"]}  

"""
