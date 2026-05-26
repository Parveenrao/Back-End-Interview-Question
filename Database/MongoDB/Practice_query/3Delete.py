""" 

=> DeleteOne 
    
    db.users.deleteOne({email : "parveeen@gamil.com"})
       
       delete only first matching record


=> DeleteMany()
        
        db.users.deleteMany({
            
            is_active : False
        })       

         delete all records


=>    db.users.deleteMany({})
            
            delete entire collection


=> soft delete 
               
               
               db.users.updateOne(
               { _id: 1 },
               { $set: { deleted: true, deletedAt: new Date() } }
            )
 
 => TTL documents 
        
        db.sessions.createIndex(
         { createdAt: 1 },
         { expireAfterSeconds: 3600 }
         )  
         
         expired documents after 1 hour
         
         used for logs                              

"""