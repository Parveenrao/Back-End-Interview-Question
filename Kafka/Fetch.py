"""  
=> Fetching === Process of pulling data from broker to consumer 
                
                -> consumer says , Give me message from partition starting offset X
                 -> This request is called , Fetch Request 
                 
--------------------------------------------------------------------------------------------------

=> Flow 

1. Consumer send Fetch Request 
    
    -> Includes 
       
       1. Topic + Partition
       2. Offset 
       3. Max bytes 
       
2. Broker Reads from log 
    
    -> Reads message from disk (Log segment)
    
3. Broker send response 
   
   -> Batch of records returned 

4. Consumer recieve batch 
   
   -> Then poll() return those records
   
    -> Fetch happen inside poll()

--------------------------------------------------------------------------------------------

=> Fetch is not one message at a time 
   
   -> Kafka always fetch in batches 

------------------------------------------------------------------------------------------

=> Configs 
 
 1. fetch.min.bytes 
    
    fetch.min.bytes = 50000
    
    Broker waits until 50KB data is available        
    
 2. fetch.max.wait.ms
    
    Max time broker waits before sending data

    If data < min bytes → wait until timeout                                 

-----------------------------------------------------------------------------------------------

Fetch = network + data transfer
Poll = fetch + heartbeat + rebalance

So:    
                 
   ====> poll() → internally calls fetch → returns records              
                 
                 
                 
                 
                 
                 

"""