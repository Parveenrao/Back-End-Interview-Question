""" 
=> Locking In MongoDB 
      
      -> A mechanism to control concurrent access to data so that operations don't conflict  or corrupt state
      
      -> Two user try to update same data = Lock ensure safe execution



--------------------------------------------------------------------------------------------------------------------

1. Document - Level Locking
       
       Document A -> Locked 
       Document B -> Free
       

=> Types of Lock 
   
   1. Read Lock 
       
       -> Multiple read allows
       
       -> No blocking between reads 
   
   2. Write locks
        
        -> Only one write per document
        
        -> Preventing conflict updates 
        
    
    Case 1 .  Different Documents  
                
                User A update doc 1 
                User B update doc 2 
                
            Both run in parallel
            No blocking 
    
    Case 2. Same document 
             
             User A update doc 1 
             User B update doc 1
             
             One waits , no corruption
                                        
             


"""