""" 
=> CORS
    -> Cross Origin Resource Sharing 
    
    -> IT control 
    
         can this frontend call backend

----------------------------------------------------------------------------------------------------------

=>  Problem Example
       Frontend → http://localhost:3000
       Backend → http://localhost:8000

       Browser blocks request ❌
       Because different origin        


-------------------------------------------------------------------------------------------------------------

=> Headers  
     
     1. Access-Control-Allow-Origin = who can access
     2. Access-Control-Allow-Methods  = which method 
     3. Access-Control-Allow-Headers   which headers 
     4. Access-Control-Allow-Credentials = cookies allowed or not

---------------------------------------------------------------------------------------------------------

=> CROS in nginx


location / {
    proxy_pass http://backend_app;

    add_header Access-Control-Allow-Origin *;
    add_header Access-Control-Allow-Methods "GET, POST, PUT, DELETE, OPTIONS";
    add_header Access-Control-Allow-Headers "Authorization, Content-Type";
}          

--------------------------------------------------------------------------------------------------------

=> option in Nginx


location / {
    if ($request_method = OPTIONS) {
        add_header Access-Control-Allow-Origin *;
        add_header Access-Control-Allow-Methods "GET, POST, PUT, DELETE, OPTIONS";
        add_header Access-Control-Allow-Headers "Authorization, Content-Type";
        add_header Content-Length 0;
        return 204;
    }

    proxy_pass http://backend_app;
}

---------------------------------------------------------------------------------------------------------
=> Production config 
    
    -> Don't use access-control-Allow-origin
    
              add_header Access-Control-Allow-Origin http://localhost:3000;
              add_header Access-Control-Allow-Credentials true;
"""