"""  
=> Access Log 
    
    -> Record of every request hitting your server 
    
    if Request touch nginx -> it gets logged (unless you disable it)

----------------------------------------------------------------------------------------

=> Default location 
   /var/log/nginx/access.log
  
  -> In docker 
      
      docker logs <container_id>

=> Log access format 
                log_format main '$remote_addr - $remote_user [$time_local] '
                '"$request" $status $body_bytes_sent '
                '"$http_referer" "$http_user_agent"';
        
        remote_addr -> client IP 
        time_local -> Request time 
        request -> Method + url 
        status -> HTTP status 
        
        body_bytes_sent -> Response size 
        
        http_user_agent -> Browser / client
                           
=> Add performance tuning 
            
            access_log /var/log/nginx/access.log detailed;

---------------------------------------------------------------------------------------------

=> Where to configure 
   Global inside htttp{}
   
   
   http {
    access_log /var/log/nginx/access.log main;
   }
 
 -> Per server 
 
    server {
    access_log /var/log/nginx/api.log detailed;
      }
 
 -> Disable logging 
            
location /health {
    access_log off;
       }                                              
"""