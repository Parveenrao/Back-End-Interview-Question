"""  
=> Caching in Nginx
     -> Store backend result  - serve it again without hitting backend 
       
       client -> NGINX -> Cache hit         -> response
                       (no backend call)
     
     
    -> Without cache
        1000 users --> 1000 backend calls   
        
    -> With cache 
        
        1 backend call -> 999 response cache
         
-------------------------------------------------------------------------------------------------------------

=> Implementation 
                  
    http {
         proxy_cache_path /tmp/nginx_cache levels=1:2 keys_zone=my_cache:10m max_size=1g inactive=60m use_temp_path=off;
        }    
        
    -> tmp/nginx_cache  = where cache is stored 
    
    -> keys_zone=my_cache:10m   = memory for cache 
    
    -> max_size 1g = max cache size 
    
    -> inactive = 60m delete unused cache after 60 second
 
--------------------------------------------------------------------------------------------------------------------------

=> Cache In Route 
   
   server {
       
       location/api/products   {
           proxy_cache my_cache;
           proxy_cache_valid 200 1m;
           
           proxy_pass http://backend;
       }
   }        
   
   
   now Response are cached for 1 minute 
   
----------------------------------------------------------------------------------------------------------------------------

=> Cache only static data 
   
   . Product list
   . Static files 
   . Public APIs

=> Do not cache 
    . user profile 
    . Payments
    . auth endpoints

----------------------------------------------------------------------------------------------------------------------------

=> Add cache status header 
    
    add_header  X-cache-Status $upstream_cache_status;
    
    noe you will se
    Miss - first req always miss
    Hit  - cache hit
    Bypass - cache skipped

-------------------------------------------------------------------------------------------------------------------------

=> Skip cache     
    
    -> lets say if authentication present in any route , then we pypass cache 
       
       proxy_cache_bypass $http_authorization;
       proxy_no_cache $http_authorization;


------------------------------------------------------------------------------------------------------------------------

=>  http {
    proxy_cache_path /tmp/cache keys_zone=my_cache:10m;

    server {
        location /api/products {
            proxy_cache my_cache;
            proxy_cache_valid 200 1m;

            proxy_cache_key "$scheme$request_method$host$request_uri";

            proxy_cache_bypass $http_authorization;
            proxy_no_cache $http_authorization;

            add_header X-Cache-Status $upstream_cache_status;

            proxy_pass http://backend;
        }
    }
}

1. http {} -> top level block for all HTTP config , Shared across all servers, Define global behaviour 

2. proxy_cache_path /tmp/cache keys_zone=my_cache:10m; 
     
     -> create cache storage 

3. server {} -> Represent one server 

4. location /api/products 

   -> apply only for products endpoints , api/products?page=2

5. proxy_cache my_cache; 
    -> Turn on cache using the zone defined 
    
6. proxy_cache_valid 1m
      -> Stored for one minute 

7. proxy_cache_key "$scheme$request_method$host$request_uri";
       
       -> Define how cache is indentified  

8. proxy_pass http://backend;
         
         -> forward request to backend                            
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
                         
                       
                       """