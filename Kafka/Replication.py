"""  => How does kafka ensure durability of topic data 

         -> Kafka ensure using replication , ack , disk-storage and isr 
         
-------------------------------------------------------------------------------------

1. Disk Persistance 
   
   -> Kafka write data to disk (not memory)
   -> Message stores in log file 
   -> Even if broker crash , data remains
       
       Producer → Kafka → Disk (log files)  ->  first level of durabiltiy       
       

-----------------------------------------------------------------------------------------------

2. Replication 
   
   -> Storing multiple copies of data across different broker 
      if one broker faail --> data remain same in other broker 
      
      topic --> Partition --> Replica 
      
        Topic : Order 
                 ->  Partition 0:
                     Leader --   Broker  1
                     Follower -- Broker  2 
                     Foller   -- Broker  3           # Replication factor - 3
        
        
        1. Leader Replica   
            -> Handle all read and writes  
            -> Producer send data only to leader 
        
        2. Follower Replica 
            -> Copy data from leader 
            -> do not serve client direclty 
        
        3. Replicatio Factor -> 3  
           
           -> 1 Leader , 2 Followers
           
        Higher RF --> more durable , but more cost
    
    
    -> Example working of replication 
    
       1. Topic 
           
           -> Topic itself dont store data directly 
           -> Topic is a logical category of data
       
       2. Partition 
           
           -> A topic is divided into many partitions 
            
           Topic : Orders 
                   | -> Partition 0
                   | -> Partition 1
                   | -> Partition 2 
          
          Partition store actual data(message)
       
       
       3. Replication of partitons 
          
          -> Each partition is copied across different brokers
       
       4. Broker 
          -> kafka server 
          
          broker store 
          partitions 
          replicas
        
        
        Topic: orders
             ↓
        Partition 0 → stored on Broker 1 (leader)
                    → replicated on Broker 2, Broker 3

        Partition 1 → stored on Broker 2 (leader)
                   → replicated on Broker 1, Broker 3            
     
     
     
     
     👉 Topic = logical
     👉 Partition = physical data
     👉 Replication = copies of partitions
     👉 Broker = machine storing data            
    
----------------------------------------------------------------------------------------------------
                                         
          
         
         
         
         
         
         
         
         
         
         
         
         """
         