""" 
=> Offset Lag 
    
    how far behind your consumer is
    
    
    offset lag = latest offset(in partition) - committed offset (consumer group)
    
    
 -> Partition 0:
    
    Latest offset = 100 
    consumer committed offset = 80
    
    Lag = 20 message

---------------------------------------------------------------------------------------------------------------

=> Types of Lag 
    
    1. Current lag (Real time )    
        
        How many message are waiting right now 
    
    2. End-to-End lag
        
        Time delay between 
        
        message produced -> message processed
        
        Sometimes lag = low but delay = high (slow processing)

---------------------------------------------------------------------------------------------------------------

=> Partition Level Lag 
    
    Lag is not per topic 
      
      -> Lag is per partition , per consumer 

=> Why Lag happens 
   
   1. Slow consumers 
   
   2. Traffic spike  -> Producer sending to fast 
   
   3. Uneven Partition Distribution 
   
      -> One consumer handle more partitions 
   
   4. Frequent Rebalance 
   
   5 . Hot Partition 
       
       user_1 --> all message  -> Partition 0 
       
       if key distribution is bad 
       
   6. Consumer Crash 
      
      -> If no consumer crash  -> lag grows to fast 
          

-----------------------------------------------------------------------------------------------

=> How to Reduce Lag 
   
   1. Add more consumer 
      
      Parallel Processing --> Only work partition are available 
   
   2. Increase Partition 
      
      More Parallelism   --> Affect ordering 
   
   3. Fixed hot partitions 
      
      Better key distribution      

                        
            









"""