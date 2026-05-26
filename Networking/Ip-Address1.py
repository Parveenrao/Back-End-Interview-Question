""" 

=> NAT
    
    -> Network Address Translation is a technique used by router to translate private ip into public IP
       
       so device can access internet
       
    -> middle man between loca; network and internet


=> Why NAT exist 
     
     -> Private IP  cannot go internet , but device need internet
     
     -> Nat solve this


=> Static NAT
   
    one private ip -> one public ip 
    
    used for servers 

=> Dyanmic NAT
    
    use a pool of public IP
    

=> NAT Uses ip + port



=> PAT
    
    -> Port Address Translation is a type of NAT where
        
        1. Many private ip share one public ip
        2. each connection tracked by using differnt port number
    
    IP + Port - unique ip
    
    
    -> Each device need unique public ip 
    
    -> but in reality , each connection needs to be unique , not each device
    
    -> so pat , many device share one public ip        
                    


""" 