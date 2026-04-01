"""  
=> Reverse Proxy 
   
   -> A reverse proxy is an entry point(gateway) that sits in front of your backend server and control all incoming traffic
   
   -> Client never talk to your backend

------------------------------------------------------------------------------------------------------------------------------

=> Request Flow 
   
   1. client send request (example.com)
   2. DNS resolves -> Reverse proxy Ip
   3. Request Reaches proxy (Nginx)
   4. Proxy decide 
       
       1. Which backend
       2. Cache or not
       3. Allow or block
   
   5. Send Request internally
   6. Gets response
   7. Returns to client    

----------------------------------------------------------------------------------------------------------------------------

=> Core Responsibility
   
   1. Routing 
      
      -> Routes api request to server
   
   2. Load balancer
      
      -> Distribute traffic across server 
   
   3. SSL Termination
       
       -> Handle HTTPS at proxy , backend stay at http
   
   4. Rate limiting
       
       -> Stop abuse
   
   5. Caching 
       
       -> Reduce backend load

--------------------------------------------------------------------------------------------------------

=> Users complain about wrong IP in logs. Why?

    -> Proxy is masking real IP → need X-Forwarded-For       

=> How to scale reverse proxy layer?

   -> Multiple proxy instances
   -> Put load balancer in front
   -> Use CDN     

=> What happens if reverse proxy is down?
    
    -> It becomes a single point of failure unless we use redundancy like multiple proxies or load balancers. 
    

=> Difference between forward proxy and reverse proxy?

   -> Forward proxy hides the client, reverse proxy hides the server.                      
"""