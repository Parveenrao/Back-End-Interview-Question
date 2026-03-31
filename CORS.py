""" => CORS  (Cross origin Resource Sharing)   
    
       -> It is a browser secuity mechanism that allow sever to specify who can access them
       
    => High Level FLow 
    
       -> Frontend   = https://app.com  
       
       -> call api  = https://api.com/users
       
            browser send request 
            
            server reply with special headers  ->   Access-Control-Allow-Origin
            
            
        If not present --> Browser block it
        
    
    => CORS Headers 
    
       1 . Access control origin  -> define which origin can access
         
            or allow all
            Access-Control-Allow-Origin: *
       
       2. Access control methods  -> Which https methods are allowed
            Access-Control-Allow-Methods: GET, POST, PUT, DELETE
            
       3. Access-Control-Allow-Headers
           Which headers frontend can send.

           Access-Control-Allow-Headers: Content-Type, Authorization       
           
       4. Access Control Allow credentials 
       
             Allow cookies/auth tokens.

             Access-Control-Allow-Credentials: true

              Important rule:

             If credentials allowed → cannot use *.

              Must specify origin.               

--------------------------------------------------------------------------------------------------------------------


CORS (Cross-Origin Resource Sharing) is a browser security mechanism that allows controlled access to resources from 
a different origin.

Browsers follow the Same Origin Policy, meaning a webpage can only access resources from the same protocol, domain, and port.

If a frontend running on one origin tries to access an API on another origin, the browser blocks the response 
unless the server explicitly allows it using CORS headers like Access-Control-Allow-Origin.

For complex requests such as PUT, DELETE, or requests with custom headers, the browser first 
sends a preflight OPTIONS request to check if the server allows it.




"""