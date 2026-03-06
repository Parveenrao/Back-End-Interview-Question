""" => API (Application Programming Interface is a set of rules that allows software system to communicate with each other)
      
       -> IN simple terms , an API is a messanger that take request from one program ,  send it to other program , and return the 
           response
        
       -> Example   Restaurant 
          
          1.  Customer --> You client 
          2.  Waiter   --> API 
          3.  Kitchen   -> Server 
          
------------------------------------------------------------------------------------------------------------------          
          
   => Types of API  
-------------------------------------------------------------------------------------------------------------------


   1. Rest-API  
   
       -> REST(Representational State Transfer) is an architecture style for designing network application  using HTTP
        
       -> Everything is treated as resource and accessed via url using HTTP methods
       
          Example  ->  users 
                      orders
                      products
                      
          Example  -> API endpoints 
                     
                     GET users/
                     GET users/10
                     POST users
                     DELETE users/10
         
     
     a. Rest API allow  constraints
     
        1. Client - Server  
        
           Client and server are separate system  
            
            Frontend ---> React 
            Backend  ---> Fastapi
            
        
        2.  Stateless 
           
            -> Server does not store client session 
            
            -> Every request must contain all information 
            
            -> Server validate token each time                                     
            
"""