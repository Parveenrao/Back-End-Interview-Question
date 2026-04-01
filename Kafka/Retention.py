"""  => Retention 
         
         -> How long kafka keep message in a topic  before deleting them
         -> kafka does not delete message after consume
         
         -> It keeps data based on time and size
---------------------------------------------------------------------------------------------------------------------------

=>  Kafka is a log system , not a queue 
   
   -> Even after consumer read message 
       
       Data stays until retention policy deletes it 
       
       
-----------------------------------------------------------------------------------------------------------------------------

1. Time Based Retention 
    
    -> keep data for fixed time 
       ex -> 7 days
       
       retention.ms --> 7 
       
       message older than 7 days -> Delete

2. Size based retention 

   -> Limit total data size 
   
       ex   retention.bytes - 1gb 
       
          if data > 1Gb   -> old data deleted 
          
          
-------------------------------------------------------------------------------------------------------------

3. Log Compaction 
   
   -> Kafka keeps only latest value for each key
   -> Oder updated for the key are removed
   
   Example -> Topic User-Profile:
   
              Message  
              
              key -> user1  = name Parveen
              key -> user2  = name  Rahul
              
              key ->  user1 name Parveen Kumar
              key  -> user2 name Rahul Yadav
              
              After compaction 
              
              user1 → Parveen Kumar  
              user2 → Rahul Sharma  
              
              
              only latest value per key remains
              
        Compaction works ONLY if messages have keys

        producer.send("topic", key=b"user1", value=b"data")      
              
              
        
        Compaction runs in background 
        
        Perfect for -> config, user_profile , balance      
   
           
                         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         """