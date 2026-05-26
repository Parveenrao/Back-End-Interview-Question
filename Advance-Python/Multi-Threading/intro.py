""" 
=> Process 
    
    -> A program in execution , one program like(open chrome)

=> Thread 
      
      -> A smaller unit of work inside that program 


=> Multi-Threading 
      
      -> Running multiple task inside one program at same time


----------------------------------------------------------------------------------------------------

=> Python Is not Truly Multi-threading 
     
     1. Beacuse GIL 
     
     2. Gil make ensure that , only one thread run python code or execute at one time
     
     3. If we create 10 thread , still one execute at a time

=> Where Multi-Threading Shines 
    
    1. I/O Bounded Task (waiting Task) 
         
         API Calls , Reading files , Db queries 
         
         While one threading is waiting , other will run 

=> Where Multi-Threading Fails 
     
     1. CPU bounded Task
         
         -> Heavy loops
         -> Calculations 
         -> Algorithms
      
      Threads here -> slow (waste )                                 



"""