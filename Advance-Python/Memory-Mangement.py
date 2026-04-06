"""  
=> Python Memory-Management

-------------------------------------------------------------------------------------------------------------------------      
      1. In Python Everything is an Object
           int, list , function , even classes
                  
           -> Every object has reference count , Type Value 
            
            a = 10
            b = a 
            
            10 is a object in memory , a and b point to same object 

-----------------------------------------------------------------------------------------------------------------------------       
       2. Reference Counting (Primary Memory Management)   
            
            -> Python mainly uses reference counting 
            
            -> Each object keep track , how many variables are pointing to me 
               
               a = [1, 0 ,1]     ref_count = 1
               b = a             ref_count = 2
               del a             ref_count = 1
               del b             ref_count = 0   , when ref_count become zero , memory freed 

----------------------------------------------------------------------------------------------------------------------------
     
     3. Garbage Collector (For Cycles)
     
         
         -> Referenc Counting fails in circular references 
         
         a = []
         b = []
         
         a.append(b)
         b.append(a)
         
         a -> b   ref_count = 1
         b -> b   ref_count = 1
         
          -> Even i delete both , memory will not freed 
          
          So garbage collector 
            
            -> Detects cycle 
            -> find unreachable
               
                    
"""