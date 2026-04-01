"""  
=> Forward Proxy 
    
    -> A forward proxy is a server that sits between client and internet , acting on behalf  of client  to make request 
    
    -> Servers sees proxies , not users

-----------------------------------------------------------------------------------------------------------------------------

=> Request Flow

    1. Client send request (eg . google.com)
    2. Request goes to proxy  (not directly to internet)
    3. Proxy:
        
        Resolve DNS sometimes
        Applies rules (allow / block)
    4. Proxy forward to actual server 
    5. Server respond to proxy
    6. Proxy send respone back to client

----------------------------------------------------------------------------------------------------------------------------

=> What forward proxy actually does
    
    1. Hide Client Identity 
    
       -> Server only sees proxy IP
    
    2. Access Control 
       
       -> Block or allow websites (school block gaming sites)
    
    3. Logging and Monitoring
        
        -> Admin can see:
        
        which site user visit 
        how much bandwidht used 
    
    4. Caching 
      
      -> Proxy can cache response 
       
        many user open same sites -> faster load

-------------------------------------------------------------------------------------------------------------

=> Types of Forward Proxy 
    
    1. Transparent Proxy 
       
       -> User does not know it exist
           used by isp
    
    2. Anonymous Proxy
       
       -> hides client Ip
    
    3. Elite proxy 
        
        -> Full hides indentity

----------------------------------------------------------------------------------------------------------------

=> Where is forward proxy is placed 
   
   -> On client side network 

=> Does server know client IP 
   
   -> Only , prox IPs

                                               
    
"""