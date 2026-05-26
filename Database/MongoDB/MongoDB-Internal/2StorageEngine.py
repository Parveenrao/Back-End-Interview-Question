""" 
=> Storage Engine 
    
    -> IN mongodb storage engine is 
        
        The Layer that decide how data is stored  , read , written  , cached and recovered 
    
    -> Default Engine = WiredTiger 


------------------------------------------------------------------------------------------------------

=> WiredTiger is responsible for
    
    1. Writing data to disk 
    2. Reading data efficiently
    3. Managing memory (cache)
    4. handling concurrency (multiple user)        
    5. Crash recovery
    
      Client Query
          ↓
     MongoDB Query Layer
          ↓
     WiredTiger Engine
          ↓
     Cache (RAM)
          ↓
      Disk (files)

"""