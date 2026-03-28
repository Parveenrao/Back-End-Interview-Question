"""   
=> Sticky Session  
 
    -> In load-Balanced system , request are spread across many servers 
    
        Many apps store session data in memory 
        
        So if request goes to another server , user log out or loses state 
      
      -> Sticky session pin user to one server 
      
-------------------------------------------------------------------------------------------------

1. Cookie based 
   
   -> Load balancer set a cookie like 
       
       SERVER_ID = server-2
    
    each request from that user will go server-2


2. IP based 
    
    -> Based on user ip 
       
       Same Ip -> same backend server 
       
     -> not reliable (shared ip , mobile network)

3. Session ID Hashing 

    -> Session ID → hashed → mapped to a server

-----------------------------------------------------------------------------------

=> Limitations 
   
   1. Break scalability 
       -> If one server get many sticky user  -> overload 
   
   2. Server crash 
      -> If that server crash  = user session lost 
   
   3. Uneven load distribution 
      
      -> Some other server remain idle 


---------------------------------------------------------------------------------------------

=> Solutions 
   
   1. Store session in central storage                                    
         
    
    

"""