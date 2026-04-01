"""  => Rate Limiting 

          -> Rate Limiting means , Restricting the number of API Request a client can make in a defined time window
          
              100 request / per minute
              
              if the user send 101 request , server respond 429 soo many request
              
    
    => Why Rate limiting is needed 
        
        a. Prevent server overload 
        
              -> Without rate limitin a user can :
                   1 user -> 1m -> Server crash 
        
        b. Attackers DDOS attacks 
        
           -> attackers send millons of request per second 
                -> Rate limiting blocks them
        
        c. Fair Resource usage 
        
            USer A -> 1000 request
            User b -> 2 req.     
            
            User A will consume all request
    
    => Where Rate limiting is applied 
    
       a. Client level 
       
           -> limit per suser    100 request / per user 
           
       b . Ip level   50 request per Ip
    
       c.  API LEvel 
        
           login api --> 10 request per / min
        
            search api  -> 1000 request / min
       
       d. Global level
       
            System capacity = 10k requests/sec
            
        
    => Flow        
            
            Client
              |      
        Load Balancer
               |
     API Gateway (Rate Limiter)
               |
        Application Servers
               |
            Database  
    
                                                 













"""