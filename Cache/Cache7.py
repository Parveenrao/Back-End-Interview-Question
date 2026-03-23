""" 
    => Cachae Avalanche 
    
       -> Cache Avalanche happens when when a large of keys expired at same time  ,causing a huge spike of req to db 
            
            
            Many keys expire simultaneously
                   ↓
            Thousands of cache misses
                   ↓
            All requests hit database
                   ↓
            Database overload
                  ↓
           System slowdown / crash
           
    
    -> Example scenario 
    
        1. Suppose an e- commerce platform caches 1 million products 
            
            product 1 
            product 2
                |
            product 1M
            
            All cached with ttl = 60 min 
            
            After 60 min , all keys expired
            
            db receive huge spike , crash  
            
            called cache alvalanche 
        
        
        -> Solution 
        
           1. Random TTL   ( 60 + random(1-10))
           
           keys will expire at diff time 
           
           
           2 Redis cluster 
           
              -> If redis fail completley 
              
                Redis --> Repliation 
                
                cache remain available 
           
           3. Circuit breaker 
           
              -> IF db get overloaded 
                Reject reuqets temporarily                
"""