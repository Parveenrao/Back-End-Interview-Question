"""   
=> Nginx 
   -> Nginx is a high performance web server + reverse Proxy + load balancer 
   
   -> Think of like traffic controller in front of your backend 
-------------------------------------------------------------------------------------------

=> Without Nginx 
   
   -> Client directly hit backend (slow , unsafe , no control)

=> With nginx
    
    -> Client --- Nginx ---- backend

------------------------------------------------------------------------------------------------
=> Why nginx

   1. Reverse Proxy 
      
      -> User --- Nginx --- Fastapi/node.js  
      
      -> Improve performance
      -> handle traffic
      -> hide backend
   
   2. Load balancer 
   
       -> If you have multiple server 
           
                       -> Server 1
            
           Nginx ->    -> Server 2 
                       
                       -> Server 3
        
        -> Distribute load  , no server load
   
   3. Static File serving 
       
       -> Nginx server these directly , super fast 
   
   4. SSL / HTTPS
       
       -> Handle certificate 
       -> Convert HTTP  -> HTTPS
   
   5. Security layer 
       
       -> Rate limiting
       -> Block IPs
       -> Prevent attack                              
    
"""