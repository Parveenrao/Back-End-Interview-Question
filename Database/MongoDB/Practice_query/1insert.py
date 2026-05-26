""" 
=> Insert in MongoDB 
    
    -> Adding a document in collection
 
------------------------------------------------------------------------------------------------

=> Insert one document
        
        db.users.insertOne({
            name : "parveen",
            age : 22,
            role : developer
        })    


=> Insert multiple documents 
       
       db.users.insertMany({
           
           {name : parveen , age : 22},
           {name : divya , age : 24},
           {name , priyanka , age : 25}
       })        
       
=> Nested Documents
      
      db.users.insertOne({
          name : parveen ,
          address : {
              city : Delhi , 
              pincode : 123303
          }
      })       
      

=> Insert with custom id 
      
      db.users.insertOne({
          _id : 101,
          name : Custom users
      })      


=> Write concern 
          
          db.users.insertOne(
            { name: "Parveen" },
           { writeConcern: { w: "majority", j: true } }
         )

         w : replicated to majority nodes 
         
         j : true  write to journal

=> Ordered 
     
     db.users.insertMany(docs , {ordered : true}) 
     
      execute operation one by one (sequentially)
      
      stop immediately on first error
      
      db.users.insertMany([
           { _id: 1, name: "A" },
           { _id: 1, name: "B" }, // duplicate
           { _id: 2, name: "C" }
          ])        
             
             a insert , b fails , stop at b


=> Unordered 
       
       -> Execute operation independent 
       
       -> Does not stop on error
       
       -> mongodb run in parallel
       
                 db.users.insertMany([
                     { _id: 1, name: "A" },
                     { _id: 1, name: "B" }, // duplicate
                     { _id: 2, name: "C" }
                     ], { ordered: false })     
                
                a inserted , b fails  , c inserted             
""" 