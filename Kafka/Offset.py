"""" 
=> Offset   = Position of the message inside partition   

    Partition 0:

   Offset | Message
   0      | order_1
   1      | order_2
   2      | order_3
   
   Offset is 
   
   sequential 0 , 1 ,2 
   Unique within partitions 
   Assigned by Kafka
   
-------------------------------------------------------------------------------------------------

=> Kafka does not track  'which message is read'   
   
   It track only which last offset consumed
   
---------------------------------------------------------------------------------------------------

=> Offset is Maintained per Consumer Group 
   
   Consumer Group A -> offset = 5
   Consumer Group B -> offset = 2
   
   Same topic ,   different progress
   
  ->  Kafka store offset in  
  
     _consumer_offsets (internal Kafka topic)

----------------------------------------------------------------------------------------------------

=> How Consumption Work Internally 
   
   Last committed offset = 5 
   
   
   -> Next poll will read , offset = 6

-------------------------------------------------------------------------------------------------

=> Current offset 
    
    What consumer is currently reading 

=> Committed offset 
   
   what kafka remembers as processed
   
-------------------------------------------------------------------------------------------------

=> Scenario 
   
   Case 1 : Commit before processsing 
       
       commit offet = 10 
       process message fails 
    
    -> message lost forever 
   
   
   Case 2: Commit After Processing 
       
       Process message 
       commit offset                      ->  Safe        
       
   Case 3 : Crash before commit 
       
       Processed  offset  = 10 
       But committed = 9  
       
       offet 10 will be reprocessed 
       
       dupicate 
       
-------------------------------------------------------------------------------------------------------

=> Auto commit 

   enable_auto_commit = True 
   
   kafak commit offset every few seconds
   
   -> may commit before processing 


=> Manual Commit 
   
   you control when to commit 
   
   enable_auto_commit = False
   
   
   from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'orders',
    bootstrap_servers='localhost:9092',
    enable_auto_commit=False,
    group_id='order-group'
)

for message in consumer:
    print("Processing:", message.value)

    # process message here

    consumer.commit()  # commit AFTER processing


-------------------------------------------------------------------------------------

=> Offset Reset Strategy 
   
   When no offset exist 
      
      COnfig 
            
            auto.offset.reset
 
 1. earliest  
    
    -> Start from beginning 
 
 2. latest (default) 
 
     -> start from new message 
  
  3. none 
      
      Throw error                      

               
          
        
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
"""