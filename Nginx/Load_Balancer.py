""" 
=> Load balancer 
   -> A load balancer distribute incoming request across multiple server 
   
   -> Avoid overload 
   -> increase availability 
   -> scale horizontally
   
-------------------------------------------------------------------------

=> Basic load balancer in nginx 

upstream backend {
    server 127.0.0.1.3000;
    server 127.0.0.1.3001;
}   


-> Now use it 
    
    location / {
        proxy_pass http://backend;
}                             


-> 1. Round RObin 

-> 2. Least connection 
    
    upstream backend {
        
        least_conn;
        
        server 127.0.0.1.3000;
        server 127.0,.0.1.3001;
        
    }         
    
3. IP Hash (Sticky Session)

      upstream backend {
        
        ip_hash;
        
        server 127.0.0.1.3000;
        server 127.0,.0.1.3001;
        
    }       
    
    
4. Weighted Load Balacing 

      upstream backend {
        
        server 127.0.0.1.3000   weight = 3;
        server 127.0,.0.1.3001  weight = 1;
        
    }

-----------------------------------------------------------------------------------

=> Failure Handling in Load balancer 
   
   -> How your system reach when backend server 
   
       1. Crash
       2. slow down  
       3. return error
       4. times out  
    
    -> Don't send traffic to bad server + Recover automatically
   
   -> Types of failure 
     
     1. Hard failure
         -> Server down
         -> connection refuse
     
     2. Soft failure 
         -> high latency
         -> partial errors 
         -> slow response 
         
       -> Dangerous beacuse server is alive , but useless
    
    3. Network failure 
        
        -> Packet loss
        -> interimmitent connectivity


=>  Health check (Passive health checkup)

         upstream backend {
         server 127.0.0.1:3000 max_fails=3 fail_timeout=10s;
         server 127.0.0.1:3001 max_fails=3 fail_timeout=10s;
         }                                     
 
         -> For 3 second , mark server down , not traffic for 10 second


=> Retry mechanism
    
    -> Without retry , user gets error
    -> with retry , user never notice
    
    
    location / {
    proxy_pass http://backend;

    proxy_next_upstream error timeout http_500 http_502 http_503;
        
        } 
        
        -> request fails , try another server automatically


=> Timeouts 
   
   proxy_connect_timeout 2s;
   proxy_send_timeout 5s;
   proxy_read_timeout 5s;           
   
   
   1. Proxy_connect = Time allowed to establish connection with backend 
   
   -> Detect dead server 
   -> Dont waste time on unreachable node
   
   2. proxy_send
   
       -> Time allowed to send request 
   
   3. proxy_read_timeout
      
      -> NGINX waits for response from backend

=> Backup 

   -> Backup server is not used normally , it is used when all primary server fail
   
     primary server - main workers
     backup server - emergency fallbacks
   
   -> When primary server came back
       
       traffic shift to primary , backup server stop recieving traffic
    
    -> Backup server is not load balacing 
 
 -> Combine with timeouts 
 
    upstream backend {
    server 127.0.0.1:3000 max_fails=3 fail_timeout=10s;
    server 127.0.0.1:3001 max_fails=3 fail_timeout=10s;
    server 127.0.0.1:3002 backup;
        }      

=> Load Shedding 
  -> Intentionally drop some request to protect the system 
  
  -> Without shedding 
      High taffic -> server overload  -> slow ->  queue builds -> crash
      
  -> Main tool 
  
    1. Rate Limiting 
          
          limit_req_zone $binary_remote_addr zone=api_limit:10m rate=10r/s;

           location /api/ {
            limit_req zone=api_limit burst=20 nodelay;
           } 
           
       
       rate = 10 req/sec 
       
       brust = 20 
       
       accept   20 , rest drop 
       
       nodelay -> Don't qeuee -> Drop immedailtely 
    
    2. Connection limiting
        
        limit_conn_zone $binary_remote_addr zone=conn_limit:10m;

       location /api/ {
       limit_conn conn_limit 5;
       }           
       
       max 5 connection per user 
    
    3. Global load shedding 
    
          limit_req_zone $server_name zone=global_limit:10m rate=100r/s;
          
          protect entire system
    
    -> Types of load shedding 
    
        1. Per user 
            
            stop abuse 
            pervent single user overload
        
        2. Global shedding
            
            protect entire system 
        
        3. Priority based 
           
           payment -> allow 
           /search -> drop 

=> Keep alive -> Connection reuse 
   
   -> Instead of creating a new connection  for every request 
   
       -> client --- Nginx ---- backend (new connection every time )
   
   
   -> Why this matter 
      
      1. Creating a connection everytime
      2. TCP handshake (3 way)
      3. TLS handshake(if htttps)
      4. kernel overhead
      
    -> adds latency + cpu cost 
    
    
    -> without keep alive 
    
       Request 1 - open connection --- close
       Request 2 - open connection -- close 
       Request 3 - open connection -- close 
       
       slow , high CPU  , poor scalibilty 
       
       
    -> with keepalive 
    
    Request 1 -> open connection
    Request 2 -> reuse connection
    Request 3 -> resune same connection
    
    
    upstream backend {
    server 127.0.0.1:3000;
    server 127.0.0.1:3001;

    keepalive 32;
} 
      
      Nginx keeps 32 idle connection per worker to backend
      
      
      -> add also this
      
      
      
      location / {
      proxy_pass http://backend;

    proxy_http_version 1.1;
    proxy_set_header Connection "";
     }                                                       
              
              
     HTTP/1.0 -> close connection by default
     
   -> Real number 
   
       TCP handshake = 50.100m
       TLS handshake = 200-300ms           
"""