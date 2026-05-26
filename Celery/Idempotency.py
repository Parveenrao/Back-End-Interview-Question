""" 
=> Rety Without Idempotency

   -> Retries without idempotency  = finnancial bugs , duplicate emails  , broken system 
   
   -> A task is idempotent if 
      
      running 1 or 100 times , same final result 
      

  -> Because Celery can retry task 
  -> executed duplicates 
  -> run task more than once 
  
  
  => Solution 
     
     1. Use unique contraint in db 
        
        -> check before processing 
        
          add txn_id to your payment 
          
          if already store in db , then forward to next step
     
     2. Race condition safe 
        
        -> DO insert first , if unique constraint in db then db dont store duplicate          



"""