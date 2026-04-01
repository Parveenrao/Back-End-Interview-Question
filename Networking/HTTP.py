"""  => HTTP (Hyper Text Typing Protocol)
 
        -> Is a communication protocol used between client and server  on the web 
        -> It defines how requests and restored are transmitted and transmitted.  
        
        -> Flow  
           
           Clinet(Browser / App)
               |
            HTTP Request 
               |
            Server 
               |
            HTTP Response 
               |
            Client Recieve data   
        
       1. HTTP Characteristics 
       
         a. Stateless -> HTTP is stateless , meaning the server does not remeber request
            
             Request 1 -> login 
             Request 2 -> GET profile 
             
             The second request must include authenication again (JWT TOKEN usually)
         
         b.  Client - Server architecture 
            
             -> Client send request  --- Server process ---- return resposne 
              
              example   Client --- FastAPI --- DATABASE
         
         c. HTTP BODY STRUCTURE 
           
             -> HTTP request has main 4 parts 
               
               1. Request line 
               2. Header 
               3. Empty line 
               4. Body 
               
            -> Request line  
                contains --> HTTP methods , HTTP Version  ,PATH 
             
            -> Headers 
               Authorization: Bearer token
               Content-Type: application/json
               User-Agent: Chrome
               Accept: application/json               
 
            -> BODY 
               
               contains data sent to server  
                {"name" : "Parveen",
                 "email" " "parveenrao7727@gmail.com} 
                 
                Usually used in PUT , GET , PATCH  
            
            -> HTTP Response Structure 
               
               Response also has 4 parts 
               
               -> status line  contains (HTTP version  , status code , status message)
               -> Headers 
               -> Empty line 
               -> Body     
 
 
         d.  HTTP METHODS 
             
             1. GET     --->   Used for Reterive data
             2. POST    --->   Create Resource 
             3. PUT     --->   Replace Resource 
             4. PATCH   --->   Update Resource 
             5 DELETE   --->   Remove Resource
 
         e.  HTTP STATUS CODE
         
            -> Server return code to indicate result 
            
             1.  1XX --> Informational 
                    
                         100 --> Contitue 
             
             2.  2XX --> Success 
                         200 -> OK
                         201 -> Created 
                         204 -> No Content
            
             3.  3XX --> Redirection                            
                         301 --> Moved Permanently
                         302 --> Found
             
             4.  4XX --> Client Errors 
                         
                         400 -> Bad Request
                         401 -> Unauthorized
                         403 -> Forbidden
                         404 -> Not Found 
                         429 -> Too Many Request
             
             5. 5XX --> Server Errors
               
                        500 -> Internal Server Errors 
                        503 -> Service Unavailable                         
 
 
 
 """