"""

1. Kafka Topic a Queue?
    Answer (don't mess this up):

   “No, a Kafka topic is not exactly a queue. In a queue, once a message is consumed, 
    it is removed. But in Kafka, messages are retained for a configured time and multiple 
    consumers can read the same data independently using offsets.”
   
    Key point:

   Queue = delete after consume
   Kafka = retain + replay

-----------------------------------------------------------------------------------------------------------------

2. Can mutliple producer write to same topic 

   -> Yes in kafka  multiple producer write  to same topic concurrently.  
   -> Kakfa ensure ordering of msgs/events within partition not across partitions
   
   -> Ordering gurantee === Partition level only 
   
   
---------------------------------------------------------------------------------------------------------------------

3. Can multiple consumer read same topic 

   => Case 1
   
      Same consumer group (mulitple consumer share the data)
      
      -> Each partition is cosumed by only one consumer  in a group
         
         no dupicate processing , load balancing 
         
      -> Topic has 3 partitions
         
          you have 2 consumer in same group 
          one consumer group get 2 partitions 
          other gets one
      
      -> Why do we need same consumer group 
         
         1. Load balancing -> instead of 1 consume doing all work , multiple consumer share work 
         2. Scalabilty     -> More data , more consumer 
         3. No duplication  -> Each message produced by one consumer         
    
    
    => Case 2
       
       -> Different consume group 
          
          1. multiple consumer read same data independently 
          2. Each group get full copy of message
          
          
          -> Same message processsed by different cosnumer 
             used for different services
        
        
        Example  -> One-topic ,, Order-created 
                    Group1  ->  Payment service     
                    Group2  -> Email service
                    Group3 - > Analytics 
        
        All recieve same data             
                    
   
   
   
   
   """