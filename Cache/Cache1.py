"""    =>  Cache  
           -> Temporary high - speed data storage used to store frquently accessed data 
           -> Instead of fetching data from slow source (database , API) we store copy of data in fast memory RAM
           
        
        -> Without Cache  
            
            Clinet - Server - Database - Response 
        
        -> With cache 
           
           Client - Server - Client - Response        
                           |
                           |--> Database (if cache miss)
            
            so cache reduce latency and database load               
                  
        
        -> Cache Miss 
            
            Data is not in cache 
              
              Client -- cache -- DB -- store in cache  -- Response 
              
        -> Cache Hit 
        
           Data exist in cache 
            
            Client - cache -- data                
                  
                  
                  
                  
                  
                  
                  """