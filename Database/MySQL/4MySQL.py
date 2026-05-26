""" 
=> DIfferent Types of Table in MYSQL
    
    1. InnoDB
        
        -> Default engine in mysql(5.5+)
        -> Support ACID properities
        -> ROW level locking 
        -> Foreign key support 
        -> MVCC
       
       used when 
        
        high write + high read
        Trxn matter 
    
    2. MyISAM
        
        -> No transaction
        -> Table - level locking 
        -> Faster for simple read 
        -> No foreign keys
     
     used when
        
        -> Read heavy
    
    3. Memory (Heap tables)
       
       -> Stored entire table on memory
       -> Extremely fast
       -> Data lost on restart 
       -> uses hash index default
      
      used when
         
         caching 
         temporary data
         session storage
    
    4. CSV (Plain text file)
       
       -> Store data as csv file
       -> Easy to read/edit internally
    
    5. ARCHIVE
       
       -> Highly compressed data
       -> Insert-only(no updates)
       -> Good for historical logs
     
     used when  
       
       -> Logging , analytics, old data 
    
    6. FEDERATED
       
       -> Access table from another mysql server
       -> No local storage
      
      used when 
      
        Distributed system
        Microservice DB Sharing
    
    7. NDB
       
       -> Distributed, highly available 
       -> Data stored across multiple nodes
       -> Real time performance                                


"""