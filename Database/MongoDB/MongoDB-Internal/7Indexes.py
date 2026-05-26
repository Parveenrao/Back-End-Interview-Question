""" 
Indexes In MongoDB 
     
     A data structure that lets  MongoDB find document without scanning the whole collection
     
     -> Without index 
        
        scan whole collections O(N)
        
        slow 
     
     -> With Index 
        
        MongoDB jump directly to matching records 
          
          O(log(n)) 
     
     
     -> Index built using B-Tree


-----------------------------------------------------------------------------------------------------------------

=> Single Field Index  
       db.users.createIndex({ age: 1 })   // 1 = ascending
       
       db.users.createIndex({ age: -1 })

=> Compound index  
    
    db.users.createIndex({ age: 1, name: 1 })  

=> Multi Key Index 
     
     db.users.createIndex({ skills: 1 })
     
     { "skills": ["Python", "MongoDB"] }
 
=> TEXT index  
          
          db.posts.createIndex({ content: "text" })

=> Unique index 
        
        db.users.createIndex({ email: 1 }, { unique: true })

=> TTL index 

                 db.sessions.createIndex(
                   { createdAt: 1 },
                  { expireAfterSeconds: 3600 }
                   )                                             
         
         auto delete index after one hour



-> Cover query important  

                 db.users.find({ age: 22 }, { age: 1, _id: 0 })
                 
                 always return index fields , not fetch whole document         

"""