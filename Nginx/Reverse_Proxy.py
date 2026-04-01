""" 
=> Reverse_Proxy 
     
     -> A reverse proxy sits between client and backend server 
     
     -> Client think it is talking to server 
     -> NGINX forward request to backend (Node / python)
     -> Return respone back to client 
   
   Client → NGINX → Backend Server

-----------------------------------------------------------------------------------------
=> Why Reverse Proxy Exist 
    
    1. Hide backend server 
        -> Client never sees your internal services 
        -> Security layer 
    
    2. Load balacing 
        
        -> Distribute traffic across multiple servers
    
    3. SSL termination 
        -> NGINX handle HTTPS , backend stays HTTP
    
    4. Performance boost 
        -> Caching , compression , connection reuse
    
    5. Central COntrol
        -> Logging , rate limiting , auth 

-----------------------------------------------------------------------------------------

=> Basic Reverse Proxy Config 
    
    server {
        listen 80;
        
        location / {
            
            procy_pass http://localhost:3000;
        }
    }
    
    Flow 
    
    -> user hit http://yourdomain.com 
    -> NGINX recieve request 
    -> location / matches 
    -> proxy_pass forward to backend (localhost:3000)
    -> Response comes back -> NGINX -> client
    
-------------------------------------------------------------------------------------
=> Now Some more concepts



location / {
    proxy_pass http://backend;

    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
}


1.  location /
     -> Request matching / 
     -> Matching everything  , / , /login , /api
     
2.   proxy_pass http://backend;
         
         -> Actual reverse proxy action 
         
         -> forward request to upstream server 
    
    upstream backend {
    server 127.0.0.1:3000;
}

3. proxy_set_header X-Real-IP $remote_addr;
    
    -> NGINX variable  = IP address of the client that connected to nginx 
    
    -> Without this line , Backend sees  , nginx Ip
    
    -> With this line , backend see users real ip address 
  
  
  -> User IP: 49.36.120.5
      GET /login      
      
      now backend sees 
      
      -> log real users
      -> track use 
      -> apply rate limit
 
 -> $remote_addr;
     
     client -> Cloudfare -> Nginx - > backend 
      
      $remote_addr = who connected to nginx  , not always real user 
      
      X-Real_Ip is wrong 

4.  proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
      
      -> standard header used to track the full chain of client IPs
      
      -> not just who is the user , but how request is travelled
      
      client -> CDN -> Load_Balancer -> NGINX -> Backend    
      
 -> client ip - 19.xxxxxxxxx
    CDN Ip - 19.xxxxxxx
    LB_Ip -- 19.xxxxxx 
    
    
    first ip -> real user
    rest -> proxies         
                                   
"""