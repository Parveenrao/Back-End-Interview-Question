""" 
=> Update 
    
    -> Modify existing documents without replacing the whole thing


------------------------------------------------------------------------------------------------------------

=> Updateone 
     
     db.users.updateOne({
         {name : "parveen"} ,   //filter
          
         {$set  : {age : 23}}  
     
     }) 

=> updateMany 
      
      db.users.update({
          {role : developer},
          {$set : {is_active : true}}
      })        
      
      
      update all matching documents

=> replaceOne
      
      db.users.replaceOne(
           { name: "Parveen" },
           { name: "Parveen", age: 25 }
        )      
        
        Replaces entire document (dangerous if careless)

----------------------------------------------------------------------------------------------------

=> Update operators
   
   1. $set 
      
      {$set : {age : 24}}
        
        adds or update field
   
   2. atomic increment 
        
        db.users.updateOne({
            {name : "Parveeen"},
            {$incr : {age : 1}}
        })             
   
   3. unset 
        
        {$unset : {ags : ""}}
        
        Remove field
   
   4. push (arrays)
   
      {$push {skills : "MongoDB"}}         
      
      
   5. addset 
         
         { $addToSet: { skills: "MongoDB" } }
         
         no duplicate
   
   6. Multi field update
       
       db.users.updateOne({
           
           name : Parveen ,
           
           {
            $set : {age : 25},
            $inc : {logincount : 1}
           }
       })          
    
    7. Upsert 
    
        
        if document exist , update it if not insert document
                     db.users.updateOne(
                       { email: "test@gmail.com" },
                       { $set: { name: "Test" } },
                       { upsert: true }
                    )
    
    8. Update with conditions
               
               db.users.updateOne(
                { age: { $gt: 18 } },   // condition
                { $set: { eligible: true } }
              )                    

               
               db.products.updateOne(
                 { stock: { $gt: 0 } },   // condition
                 { $inc: { stock: -1 } }
                 )
                 
                 stock will never go zero
    
    9. Findoneupdate
             
             find a document , update it , and return it (in one operation)
              
              
              db.users.findOneAndUpdate(
                { name: "Parveen" },          // filter
                { $set: { age: 25 } },        // update
                { returnDocument: "after" }   // options
                )    
    
    10.  setoninsert
            
            -> Only runs when a new document is created 
            -> it does nthng on update
                             
                             
                             db.users.updateOne(
                                 { email: "user@gmail.com" },
                                   {
                                     $set: { lastLogin: new Date() },
                                        $setOnInsert: {
                                         createdAt: new Date(),
                                        role: "user"
                                      }
                                     },
                                   { upsert: true }
                                 )
                
                -> new user = get created + role 
                
                Existing user = only lastlogin updated
    
    
    11. and operator 
         
         -> all conditions must true 
         
         -> it is implicit
         
         
         db.users.updateOne({
             {age : {$gt : 18} , country : "India"},
             {$set : {verified : True}}
         })                         
                     
                     
           same as 
                  
                            
                            db.users.updateOne(
                        { $and: [ { age: { $gt: 18 } }, { country: "India" } ] },
                        { $set: { verified: true } }
                        )
                        
        
        -> when to use and , when we set condition on mltiple fields
                                
                        db.users.updateOne({
                            $and [
                                
                                {age : {$gt : 18}},
                                {age : {$lt : 30}}
                            ]
                        } ,
                        
                        {$set : {group : "young"})    
    
    
    12. or conditions 
              
              db.users.updateMany(
                  {
                $or: [
                 { role: "admin" },
                 { role: "moderator" }
                     ]
                   },
            { $set: { access: "high" } }
              )   
        
        when we want any condition to be true
    
    
    -> cobine and or 
                              
                              db.users.updateMany(
                                    {
                                $and: [
                                   { age: { $gt: 18 } },
                                      {
                                 $or: [
                                        { role: "admin" },
                                       { role: "moderator" }
                                     ]
                                      }
                                       ]
                                          },
                                     { $set: { access: "premium" } }
                              )                                               

"""