""" 
=> Broker == A Kafka broker is simply a server that stores and serves data 
              
             1. Recieve message from producers 
             2. It stores them in topi/partition
             3. It serves them to consumers
-----------------------------------------------------------------------------------
Producer      --> send package 
Broker        --> Warehouse storing package 
Topic         -->  Category (electroincs  , clothes)
Partitions    --> Shelves inside  category 
Consumer      --> pick package           


                   Producer → Broker → Consumer
                               ↓
                             Topic
                               ↓
                           Partitions   
                           
                           
A Kafka cluster = multiple brokers
Each broker has a unique ID

Example:
Broker 1
Broker 2
Broker 3    

--------------------------------------------------------------------------------------------------------------------------
=====> Working 
       
       1. Recieve Message from producer 
           
           -> Producer send data to specific topic 
           -> Broker decide it which partitions to store in it 
       
       2. Store message 
          
          -> Kafka broker store message 
             
             1. Append-only-logs(file on disk)
                      orders-0.log
                      orders-1.log    
                      
            offset | message
            0      | order1
            1      | order2
            2      | order3      
            
           Data is not updated or deleted immedaitely
          It is sequentially appended -->  fast
       
       3. Serve data to Consumer 
          
          -> Consumer pull data from broker 
          -> Broker does not push 
                    
         kafka is pull based - not push based 
       
       4. Manaeges Offset 
          
          -> Broker keep track of 
              
              1. Message order via offset
              2. consumer track what they read
       
       5. Replication 
          
          Partition 0:
          
          Leader -> Broker 1 
          Followers -> Broker 2 , Broker 3  
          
          only leader broker handle read and write 

-----------------------------------------------------------------------------------

=> How data is distributed across broker
    
    Topic : Orders -> 3 Partitions 
    
            Partitions 0 -> Broker 1 
            Partitions 1 -> Broker 2
            Partitions 2 -> Broker 3      
            
---------------------------------------------------------------------------------------

=> What Happens If Broker Fails?

 -> Broker 1 crashes
    It was leader for partition P0

  -> Kafka will:

     Elect a new leader from followers (ISR)

     Consumers continue with no data loss (if configured properly)                         






























                       
"""