""" 
=> Consumer == A consumer reads message from kafak topic 
               
               Producer = sends order 
               Consumer = processes order 
           
           Example:
           
           Order service -> produce 
           Payment service -> consume 
        
       ->  Producer → Topic → Consumer
       
       -> Kafka is pull-based

---------------------------------------------------------------------------------------------

from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'orders',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest'
)

for msg in consumer:
    print(msg.value.decode())
    

--------------------------------------------------------------------------------------------------

1. Offset (Heart of Consumer)

    1. Each message has as ID:
        
        Partition 0:
        [0] order_1
        [1] order_2
        [2] order_3     
    
    Consumer tracks 
      -> Where did i last read       
 
    why offset matters
    
    1. Resume after crash 
    2. Avoid duplicate processing 
    3. Replay old data    
 
2. Auto offset reset 
     
     auto_offset_reset='earliest'
     
     earliest → read from beginning
     latest → read only new messages          
        
-----------------------------------------------------------------------------------------------

=> Consumer Groups 
 
    Topic -> 3 Partitions 
    
    Group 1:                            ->  Consumer Group is multiple instance of a service , so that load distribute across consumer
    
    Consumer A -> Partition 0
    Consumer B -> Partition 1
    Consumer C -> Partition 2

   
   One Partition -> one consumer per group 
-----------------------------------------------------------------------------------------------------------


from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'orders',
    bootstrap_servers='localhost:9092',
    group_id='group1',
    auto_offset_reset='earliest',
    enable_auto_commit=False
)

for msg in consumer:
    print("Processing:", msg.value.decode())
    
    # after successful processing
    consumer.commit()
    
--------------------------------------------------------------------------------------------------------------

=> How does kafka consumer read data 
   
   -> kafka consumer pull data from assigned partitions using offset , They continuosuly poll the broker for new message


=> Offset Management
   
   -> Offset management is the process of tracking which message is processed by consumers
   
   
=> Auto commit vs Manual Commit 
   
   -> Auto commit automaticall saves offsets at interval  , which leads to loss data is producer fails 
   
   -> Manual commit allows committing offset only after successfull processing 

=> What happen if consumer crash 
   
   -> If a consumer crash ,  Kafka reassign  its partitions  to other consumers in the group , and they resume processing from 
       the last committed offset.”  
       
=> Consumer Lag 

   -> Consumer lag is the difference between the latest offset in the partition and the offset processed by the consumer. 
      High lag indicates slow consumption.          
      
=> Rebalancing 
   
    -> Rebalancing occurs when consumers join or leave a group, causing Kafka to redistribute partitions among active consumers.”                 

=> What happens if consumers > partitions?

     -> Some consumers will remain idle because Kafka assigns at most one consumer per partition within a group
     
=> What is polling in Kafka?
   
     -> Consumers use the poll() method to fetch records from Kafka brokers in batches.

=>  How do you scale consumers?

    -> Consumers are scaled by increasing the number of instances in a consumer group, up to the number of partitions         
               
"""