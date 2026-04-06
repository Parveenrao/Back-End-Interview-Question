"""
=> Python Memory Allocation
    
    -> Python use private heap 
        
        Heap is managed by interpreter , not directly by us


---------------------------------------------------------------------------------------------

1. First Layer PyMalloc(Fast Allocator )
   
   -> Handles small objects (512)
   -> very fast
   -> Avoid calling os repeatedly
      
      small int , string , list , dict(small)

2. System Allocator 
    
    -> For large allocator 
       
       use os function like (malloc)


---------------------------------------------------------------------------------------------

=> Stack Memory Vs. Heap Memory 
 
 1. Stack 
     
     -> Store function calls 
     -> Local variable references 
  
 2. Heap 
    
    -> Store acutal data  list , dict , Objects  , integers , Strings                    

"""