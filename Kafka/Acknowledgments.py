"""  
=> Ack == confirmation that message was written successfully
          
          -> When producers send message , it ask 
              
              How sure do you want me to be that this data is safe 

----------------------------------------------------------------------------------

=> Ack levels 

   1. ack = 0 (Fire and Forgot)
      
      -> Producers send message  , does not wait 
      
      ->  No confirmation from broker 
      
      -> Fast , but risky 
      
      -> broker may fail , data lost
   
   2. ack = 1 (Leader Acknowledgment)
      
      -> Producer wait for only leader broker
         
         producer -> send message ->  leader write message -> Leader send ACK
      
      -> Leader crash before followers copy = data loss possible
   
   3. ack = all or -1 
       
       -> Producers wait for all replica (ISR)
       
       
       Producer → Leader
       Leader writes
       Followers replicate
       All confirm → ACK sent         
      
      
                    
  


"""