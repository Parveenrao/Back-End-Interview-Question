""" 
=> ReadPath In MongoDB
   
   
   Client -> Query Parser -> Query Planner -> Execution Engine -> Cache / Disk -> Result


-------------------------------------------------------------------------------------------------

=> Flow 
      
      Let take example  ,db.users.find({age : 22})
      
      
      1. Query Parsing 
          
          -> validate syntax
          -> convert query into internal format
       
      2. Query Planner 
           
           -> Check available index 
           -> Query shape
           
           Choose best execution plan 
           
           if index exist , choose index scan 
           
           if not , scan collections(COllscan) -> scan every document -> Filter -> return O(N)
      
      3. Execution Engine 
         
         After plan selection 
         
         MongoDB select 
         
            index traversal or full scan
            
            apply filter 
            
            fetches document
        
        -> Even with index  , MongoDB may still fetch full documents
        
             called fetch stage
        
        -> Covered query 
             
             if query needs index fields only 
               
               db.users.find({"age" : 22} , {age  : 1 , _id : 0})
            
            mongodb use index only    
            
            avoid fetching document
       
       4. Cache/Disk
          
          Handle by WiredTiger
          
          -> Cheack cache (RAM)
          
          -> if found , return fast 
          
          -> Else ,read from disk 
          
          -> Load into cache
       
       5. Result Construction 
           
           -> Apply projection 
           
           -> Format result 
           
           -> Sends to client


=>  DEBUG TOOL

         db.users.find({ age: 22 }).explain("executionStats")                                         


"""