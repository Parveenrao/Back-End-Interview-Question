"""  
      => Cache Breakdown
      
         -> Happens when a single hot key expire and many request hit db simultaneously
             
             usually for popular data
         
         
        1. Redis lock 
        
          -> only one key fetch data from db and other wait ,, unitl rebuil cache 
          
        2. Never expire hot key 
           
           then refersh cache manually
        
        3. Background worker refresh key          
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      """