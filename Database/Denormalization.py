"""  
=> Denormalization 
     
     -> Denormalization in database means intentionally adding redundancy (duplicate data ) to make read faster 
     
     -> Instead of keeping data strictly organized across many tables , combine / duplicate data so queries become faster and 
        
        simpler 
     
     
     -> Example  
     
       user_id | order_id | user_name 
     
     
     -> When to use 
        
        1. System is read heavy 
        2. You need query pattern 
        3. You neer low latency
    
    
    -> Design tables based on queries , not relationship
    
    
    => Why use denormalization 
       
       1. Read should be fast
       2  join are expensive 
       3. Data is often read more then write
    
    
    => Cons 
       
       1. Consistency , 
       2. update become tricky , we update many places 
       3. data duplication 
       4. storage cost             
"""