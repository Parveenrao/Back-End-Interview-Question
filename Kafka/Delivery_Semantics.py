""" 
=> Delivery semantics define how reliably message are delivered from producer - broker - consumer 


1. At most once 
    
    -> Message can be delivered 0 or 1 time (can be lost)
    
    -> Flow 
        
        1. Producer send message
        2. offset committed before processing
        3. if crash happens  -> message lost 

2. AT least once 
   
   -> Message can be deliverd one or more time  (no loss , but duplicate)
      
    -> Flow 
        
        1. Process Message 
        2. Then commit offset 
        3. if crash before commit -> reprocess (duplication)


--------------------------------------------------------------------------------------------------------------

3. Exactly Once 
  
   -> Message is processed once and its effect happens only once 
   
      kafka alone cannot gurantees exactly once 
   
   -> We want to avoid 
      
      1. Data loss 
      2. Duplicates 
      
    
    It is achieved through 
    
    1. Idempotent producer 
    2. kafka Transaction    --> either happens everything or not happens
                           
    
"""