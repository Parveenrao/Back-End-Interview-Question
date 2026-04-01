""" 
=> Real life scenario 
   
   Case : Slow consumer 
          
          If consumer take too long
          
          max.poll.interval.ms exceeded
      
      kafka thinks it is dead 
      trigger balance 
    
    Result : 
    
     1. Partitions move to another consumer 
     2. Old consumer comes back 
     3. Now duplicate processing
     
---------------------------------------------------------------------------------------------

=> Rebalance Handling 

   1. Increase Poll interval 
        max.poll.interval.ms
     
     prevent unnecessary rebalance 
   
   2. Use stick assignment 
      
      partition.assignment.strategy=sticky
   
   3. Avoid to mnay consumer 
      
      Consumeras > Partitions --> More rebalancing + useless                   
"""