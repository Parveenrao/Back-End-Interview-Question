""" 
=> From Node exporter you get
    
    node_memory_MemTotal_bytes 
    
    node_memory_MemAvailable_bytes
    

----------------------------------------------------------------------------------------

=> What percent of Memory is actually being used 
    
    100 * (1 - (node_memory_MemAvailable_bytes / node_memory_Total_bytes)) 


=> Memory Usage Per instance 
    
    100 * (1 - (node_memory_MemAvailable_bytes / node_memory_Total_bytes) by (instances ))     
    
    which server is runnig out of memory

=> Memory Used
   
   node_memory_MemTotal_bytes - node_memory_MemAvailable_bytes

=> Free memory % 
   
   100 * (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)

=> cache memory 
     
     node_memory_Cached_bytes
     
     bad = cache usage low and memory usage is high

=> Buffers 
     
     os buffer memory
     
     node_memory_buffers_bytes
     
     os buffer memory

=> Swap usage
            
            100 * (
       1 - (node_memory_SwapFree_bytes / node_memory_SwapTotal_bytes)
       )          
       
      If swap is used → system under memory pressure
 
=> Memory Pressure signal 
             
             node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes < 0.1
             
             less than 10 % -> danger

=> Memory spike detection 


        max_over_time(
       100 * (1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes))
     [10m:]
      )

=> Top Memory Consuming Instance  
    
    topk(3 , 100 * (1 - (node_memory_MemAvailable_bytes  / node_memory_Memtotal_bytes))


---------------------------------------------------------------------------------------------------------

=> Linux Memory 
    
    -> Linux tries to use 100% of RAM always
    
    Unused Ram = wasted performance
    
    
    so it fills with 
    1. cache 
    2. buffers
    3. slab 
    

 -> Cache 
    
    node_memory_Cache_bytes 
    
    files stored in ram for fast access
    you read a file 
    linux stored it in memory
    
    cache is reclaimable 
    
    if app needs memory 
      
      cache is freed automatically


-> Buffers 
   
   Temporary memory for disk I/O
   
    writing file to disk I/O
    
    buffers are aslo reclaimbale and temporary

-> Slab (kernel memory )
    
    memory used by kernel structures 


-----------------------------------------------------------------------------------------

=> Memory Leaks 
    
    -> Memory keep increasing over time and never comes down 
    
    Even when 
    
    traffic drop 
    request finish 
    
    1. First Signal -> Memory Trends 
        
        node_memory_MemAvailable_bytes 
    
    2. Memory Usage Trend Percentage 
       
       100 *(1 - (node_memory_MemAvailable_bytes) / node_memory_MemTotal_bytes)
    
    3. Detect Continous Growth 
        
   
      increase(
      node_memory_MemTotal_bytes - node_memory_MemAvailable_bytes
       [1h])                        
          
                                  

"""