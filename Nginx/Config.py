"""  
events = {}

http {
     server {
            listen 80;
            
            location / {
                     
                     return 200 "Hello NGINX"
     
      } 
    
    }
}        


=>  Events  
     
     -> This block handle all connection level stuff (how nginx deal with multiple users )
     -> Woker connection
     -> Connection handling

=> Http 
    
    -> Main web layer 
     
  -> Everything related to 
     
     HTTP Request 
     Servers
     Routing
     Headers 
   goes inside this block 
   

 http = all web traffic logic lives here 

=> Server 
    
    -> This represent one website / one backend entry point 
    
    -> You have multiple server 
    
    -> Each server can listen on different serverss / domain
    
      80 -> HTTP
      443 -> HTTPS

=> Location  
   
   -> Routing logic
   
       location / {
           
           -> Handle all request starting with /"
              
             /
             /api
             /users
             / = catch-all route     

=>  return 200 "Hello NGINX"
               
            This sends a direct response

            200 → HTTP status (success)
            "Hello NGINX" → response body         

-------------------------------------------------------------------------------------------------

=> Flow 
                   
      Browser → localhost:80 → NGINX
                ↓
           server block
                ↓
            location /
                ↓
           return 200 response
                ↓
           Browser gets "Hello NGINX"            
                             
"""