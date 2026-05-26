""" 
=> Bucketing IN Cassandra 
     
     1. Splitting one logical partition into multiple smaller partition to avoid hotspot
     
   
   -> Why bucketing 
       
       let say Primary key(chat_id , message_id)
          
          one viral chat -> million on write -> single partition -> singlw node overload
          
          bucketing fix this by spreading load
 
------------------------------------------------------------------------------------------------------

-> 1 Random Bucketing 
    
    Add a random number 
     
     Primary key ((chat_id , bucket) , message_id)
     
     where bucket random(1-10)
     
     -> Instead of chat_id = 123 one huge partition 
     
        
        we get (123, 1) , (123,2) (123 , 3) , (123,4) , (123 ,5) -> 10 patitions
        
    
    -> insert  
    
    INSERT INTO messages (chat_id, bucket, message_id, text)
    
     VALUES (123, 7, now(), 'hello');         
     
     
     Read
     
     SELECT * FROM messages WHERE chat_id = 123 AND bucket IN (1..10);   
    

-> 2 Time Based Bucketing
      
      split data based on time
      
      PRIMARY KEY ((chat_id, month), message_id)
      
      INSERT INTO messages (chat_id, month, message_id, text)
      VALUES (123, 202604, now(), 'hello');     
      
      
      
      to get recent message
      SELECT * FROM messages 
      WHERE chat_id = 123 AND month = 202604; 


-> 3 Hyrid Bucketing 
     
     Combine both 
     
     
     
     PRIMARY KEY ((chat_id, month, bucket), message_id)
     
     (chat_id, 202604, 1)
     (chat_id, 202604, 2)
     (chat_id, 202604, 3)          
     
     
     for huge chat app
            


"""