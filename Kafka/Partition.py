"""   
=> Partition  -> Where actual message are stored 
               
               -> Partition is a unit of ordering , parallelism and storage inside a kafka topic 
               -> Topic is divided into many partitions 
               -> Each partition is an append only log (like a file )  -> message strored in the end


--------------------------------------------------------------------------------------------------------------

=> Structure of Partition 
   
   Each partition has 
     1. An ordering list of messages
     2. Each message has an offset index (position of message) , like array index , unique only within partition
     
     
Partition 0:

Offset | Message
0      | order_1
1      | order_2
2      | order_3               


--------------------------------------------------------------------------------------------------------------------

=> Why Partitions 
   
   1. Parallel Processing 
      
      if i had one partition then , only one cosumer can read partitio
      
      when multiple partitions 
      
      multiple consumer can read partitions
   
   2. Load Distributed 
   
       Data is evenly distributed across partitions , no single partition get overload    
       
       
       
   3. Ordering Gurantee
      
      Kafka gurantee ordering only with in partition
-------------------------------------------------------------------------------------------------------------------------

=> How Kafka decide Partition 
   
   when you send a message 
   
   Case 1 :
     
     producer.send("orders", key="user_1", value="order_123")
     
     kafka does    partition = hash(key) % num_partitions
     
        same key -> same partition -> order preserved
   
   Case 2 : Without KEy 
   
    producer.send("orders", value="order_123")
    
    kafka use round robin 

------------------------------------------------------------------------------------------------------------------------

=> Real World Example
  
   E-commerce Order 
   
   All order of same user  -> ordered 
   
   key = user_id
   
   user_1 = partition 0 
   user_2 = partition 2
   user_3 = partition 1
   
   Each user's order stay ordered

-> Conumser and Partition Relationship 

   Topic : 3 Partition 
   Consumer Group -> 2 consumers
   
   consumer 1 ---> partition 0 , 1 
   consumer 2 ---> partition 2
   
   
   If consumers > partitions 
   
   3 partitions , 5 consumers 
   
   2 consumers will idle 

-----------------------------------------------------------------------------------------------------------------------

-> Partitions Replication 

    Each partitions has:
    1. Leader 
    2. Foll0wers 
    
    
    Partitions 0:
    
    Leader -> Broker 1 
    followers  Broker 2 , Broker 3 
    
    Producer and consumer are talk only to leader 
    
    
    if leader fail , follower become leader 
    
----------------------------------------------------------------------------------------------------------------------

-> We dont scale kafka by topic 
 
     scaling is done by using partitions   
     
-> More partitions not equal to Always better 

   More network overhead 
   More open file 
   Harder Rebalance
   
---------------------------------------------------------------------------------------------------------------------------

=> A partition in Kafka is:

An ordered, immutable log
The unit of parallelism
The basis for scaling
Guarantees ordering within itself                        
"""