""" 
=> Index Tradeoffs
   
   
   
   1. Write Amplification
       
      ->  every write must update 
           
           the document
           every index on that collection
           
           // 5 indexes on users
             db.users.insertOne({ ... }) 
             
             
             internally 6 writes 
   
   2. Memory Pressure
       
       -> Indexes live heavily in RAM
       
       -> RAM is limited 
       
       -> Index compete with data in cache 
     
     
     10 GB index 
     
     2 GB RAM 
     
     constant disk read
   
   3. Maintenance Overhead
       
       -> Index need to be updated 
       
       -> Rebalancing
       
      
      Using B Tree 
       
       insert => tree rebalancing 
       
       delete => restructuring
   
   4. Query Planner Complexity
         
         -> More candidate plans 
         
         -> More planning overhead


"""