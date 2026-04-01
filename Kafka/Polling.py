"""   
=> Poll == is heartbeat of kafka
            
            Poll does 3 critical things 
            
           1. Fetch message from broker
           2. Send heartbeat to kafka
           3. Trigger rebalance when needed 
        
        
        if you dont call , kafka tnhink consumer is dead    

---------------------------------------------------------------------------------------

=> Inside working of poll()

1. Fetch data 

     -> Consumer ask broker 
        
        "Give me message from offset X"
        
        Broker return batch of records
        
        kafka is pull based , not push based 

2. Heartbeat Mechanism
    
    poll() send heartbeat to Group cordinator
    
    -> Tells kafka , i am alive  dont remove from the consumer
    
    if heartbeat stops 
    
     -> rebalance stops 

3. Trigger Rebalance 
   
   -> poll() checks 
   
   New cosumer joined
   Consumer crashed
   Topic Partitions changed

4. Offset Management 

    -> Keep track 
    
    Last consumed offset 
    Last committed offset 


------------------------------------------------------------------------------------------

=> Configs 

1. max.poll.interval.ms 
   -> maximum time between two poll calls
   
   if succeed , kafka assume consumer is stuck , trigger rebalance
   
2. session.timeout.ms
     -> Time Kafka waits before marking consumer dead


3. max.poll.records
    -> Max records returned in one poll()   
               
    
            












"""
