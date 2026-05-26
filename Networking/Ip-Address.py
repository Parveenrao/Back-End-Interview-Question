""" 
=> Ip
    
    -> Internet Protocol adress is a unique identifier assigned to a device on a network
    
    -> Without it , device does not know where to go  , device would not communicate

-----------------------------------------------------------------------------------------------------

-> Based on Usuage Ip are two types 
   
   1. Public IP 
       
       -> A address that uniquely indentifies you netork / device on the global internet
       
       -> When we use internet
            
          inside house      ->   Device use private ip
          outside internet  ->   everything seee public IP
      
      
      => Flow 
          
          Let you open a website 
          
          1. My device private ip -> 192.......
          2. Router convert into public IP   -> 49......
          3. Request goes to server 
          4. Server respond to Public IP
          5. Router send back to your laptop
      
      => Characteristic 
         
         1. Globally Unique 
             
             -> Now two device on internet share same public Ip
         
         2. Assigned by ISP
             
             Internet provider assign public IP
    
    
    2. Private IP 
         
         -> A private ip address is an ip address used inside local network (home wifi ,college network , office lan)
         
         -> room no inside hotel , private IP
       
       
       1. NOt routable on internet 
           
           -> router ignore private ip 
       
       2. Reusable everywhere
           
           -> same private ip exist in different networks
       
       3. Used with nat                                


"""