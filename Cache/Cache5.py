"""  
     => Cache Stampede 
     
        -> Cache stampede happens when  , many request simultaneously miss cache and hit db , this make db overload and crash
        
        
              Cache expires
                   ↓
            1000 requests arrive        # Also called Thundering Herd Problem
                   ↓
           All requests miss cache
                   ↓
              All hit DB
                   ↓
               DB overload / crash
               
        
        -> Example scenario  
        
            1. Imagine a product page:
                product : 101   cache for 60 sec
                
                after 60 sec 10000 user hit req all goes to db 
        
        
        -> Solution  
        
        1. Redis Distributed lock 
        
           -> Only one req fetch from db and rebuild cache 
               others will wait 
               
        2. Refersh ahead 
            
            -> Background worker wll refresh at 50 sec 
        
        3. Request Coalescing 
            
            -> when multiple keys want same data , so system cpmbine them one db query instead of many queries        
            
        Cache stampede commonly occurs in cache-aside systems when many requests encounter a cache miss simultaneously 
        and all query the database.               
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            """