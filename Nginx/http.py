""" 
=> http {}
    
    -> It define how http request are processed , routed , modified and forwarded
    
    
    http {

    # global settings

    server {
        # entry point

        location / {
            # routing logic
        }
    }
}

--------------------------------------------------------------------------------------------------
1. Global HTTP settings 
    
    http {
        
        include mime.types;
        default_type application /octet-stream;
        
    }
    
  => Mime.types 
     -> tells nginx load a file that maps file extension -> Mime types
    
    -> when nginx serve a file , it must tell the browser 
       
       what kind of content is this 
       
    -> if this is wrong 
        1. css may not apply 
        2. js may not execute 
  
  => default_type application/octet-stream;
     
       -> This is fallback 
           if extension not found in mime.types
        
        -> nginx send
               Content-Type: application/octet-stream          
        
        -> application/octet-stream 
            means , i dont know what the file is 
            
            browser will download it,
            not try to render it 
-------------------------------------------------------------------------------------

=> What is mime.types in NGINX

      -> It is a configuration file that maps file extensions to MIME types so NGINX can send correct Content-Type headers
        in HTTP responses. Without it, browsers may not correctly interpret the served files.                         
"""