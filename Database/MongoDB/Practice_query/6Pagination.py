""" 

=> Pagination 
     
     -> Return data into chunks , instead of everything at once
     
     -> Basic pagination , skip + limit 
         
         db.users.find({}).skip(0).limit(0)
         
         formula = skip = (page - ) *limit
         
         skip = (3-1) * 10 => 20
         
         
         good example 
        
              db.users.find({}) .sort({ createdAt: -1 }) .skip((page - 1) * limit) .limit(limit)  
     
     -> Cursor based pagination
           
           db.user.find({
               _id : {$lt : lastseenid}
           }).sort({ _id : -1}).limit(10)


"""