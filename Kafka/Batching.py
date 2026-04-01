""" 
=> Batching === Instead of sending message one by one 
                
                kafka send mesage one by one [1 ,2 3, 4 ,5] -> one batch 


=> Where Batching happens 
  
    -> Producer collects message in disk / memory  
    -> Group them into batches  
    -> Send together as batches 

-----------------------------------------------------------------------------------------------

=> Fewer network calls 
    
    -> 100 message = 1 request 

=> Higher Throughput 
   
   -> Kafka push millions of msg per sec because of batching 

----------------------------------------------------------------------------------------------------

-> Key Configs 
   
   1. batch.size = 16384 , 16kb 
   
   2. linger ms 
        
        linger.ms = 5 
        
       -> Producer wait for x second to fill batach
       
      linger.ms = 0  → send immediately (no batching)
      linger.ms = 5  → wait 5ms → collect more messages       


------------------------------------------------------------------------------------------------------

=> Each partitions has its own batch 

=> Batching is per partition


--------------------------------------------------------------------------------------------------------


High Throughput

batch.size=65536
linger.ms=10
compression.type=zstd


Low Latency

batch.size=8192
linger.ms=0
compression.type=lz4      

        
     
                    

"""