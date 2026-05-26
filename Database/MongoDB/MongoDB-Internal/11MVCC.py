""" 
=> MVCC In MongoDB
        
        -> Multi version concurrency control
        
        -> Instead of locking data 
        
             Mongo DB keeps multiple version of a document
             
             Reader and writers don't block each other


-----------------------------------------------------------------------------------

=> Core Idea 
    
    -> when a document is updated 
    
    -> MongoDB wiredTiger  does not overwrite in place
    
    -> IT create 
        
        Old version = 22
        
        new verson = 25
  
  
  1. Snapshot Read
        
        when a query starts
         
         db.users.find({age : {$gt : 20}})     
         
         mongodb give it snapshot timing
         
         it will only see data commmitted before timestamp
   
   2. Writes (How updates works)
       
       -> When a write happens
       -> Old version is kept temporarily
       
       -> index update accordingly
       
       -> commit happens
   
   
   -> Example 
      
      
      Time T1:
        
        Doc = age : 22
        
        query start snapshot = t1
      
      Time T2 
        
        doc = update age = 25
        
    now query started t1 see age= 22 
    
    new query see = 25
 
 
 => What happens to older version 
      
      -> They are not keep forever 
      
      -> MongoDB use
          
          garbage collection (history store cleanup)
          
      -> older version are removed when
        
         no query need them 
         
         safe to delete 
    
    
    -> Transaction can delay cleanup 
        
        if we run long running transaction 
        
         older version are preserved 
         
         cleanup is blocked
    
    -> Replication also affects deletion

                 MongoDB keeps old versions until:

                 Replicas have applied the changes

                 Because secondaries might still need older data                                  
                 



"""