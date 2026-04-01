"""

    => Why Cookie and Session are not good choice 

      
        1. Server State Problem    
        
             Sessions make the server stateful.

             When a user logs in:

             session_id → stored on server

             Example:

             session:abc123 → user_id = 10

             This means the server must store session data somewhere.

             Problems:

             needs memory/storage

             needs session management

             harder to scale
 
      
        2. Scaling Problem  
        
           -> In distributed system you have multiple server 
           
           -> Example   
                        Client  -> Load Balancer -> Server1
                                                    Server2
                                                    Server3
                        
                        IF Session are stored in Server1 memory, then 
                         User login   --->   Server1
                         Next Request --->   Server 2
                         
                         Server1 does not know the session 
                         
                         
                         Modern system prefer stateless authentication 
         
        
        3. Performance Overhead  
        
          -> Each request require session lookup 
          
           
            client
               ↓ 
           API Server
               ↓
          Redis / Database
               ↓
          Session validation
               ↓
            Response                                                  

           That extra lookup adds latency.

           JWT avoids this because:

          Token contains user data
 
          Server can verify it without DB lookup.

        4. Memory Consumptions  
        
          -> Session consume  server memory  
          
             Example  -> 1 million user    -> server creates 1 million objects 


 """