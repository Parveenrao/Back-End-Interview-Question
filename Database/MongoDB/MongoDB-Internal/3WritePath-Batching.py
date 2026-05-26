""" 
=> WriteBatching 
     
     -> Grouping multiple write operation together before writing to disk or journal
      
     -> Instead of 
           
           Write -> Disk
           Write -> Disk
           Write -> Disk 
        
        Mongo does 
          
          Write -> cache 
          Write -> cache 
          Write -> cache 
              
              Group them -> Send journal / disk
    
    
    -> Why Mongo does this
        
        Disk I/O is expensive 
           
           -> Writing once per operation  = slow 
           -> Writing once per batch = fast 

------------------------------------------------------------------------------------------------

=> Batching Internally
     
     -> In WiredTiger Batching happens in two key places
     
     
     1. Journal Batching 
          
          Multiple write/operations are grouped , written together in one journal write
     
     2. Cache 
         
         Data accumulates in memory 
           
           Flush periodically (checkpoint)
           
           Not immedaitely after each write
   
   
   -> Without batching 
      
      1. Many disk write 
      2. high latency 
      3. Low throughput


=> Tradeoff 
     
     -> Batching introduce delay 
     
     Mongodb may wait to group writes                                           



"""