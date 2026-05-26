""" 
=> Asyncio 
   
   -> Single Thread  , cooperative concurrency
   
   -> Use it when 
        
        Task spend more time in waiting I/O
        
        API calls , network request , File I/O
        
        calling 100 Apis
        
        handling 1000 of HTTP request 
    
    -> No thread overhead 
    -> scale to thousand of task
    
    -> Now usefull for cpu bound task beacuse of GIL
    
    -> CPU heavy code , block event loop , cannot yield 
    
    -> In async we have to give up control
 

=> Threading
    
    -> Multiple thread , shared memory 
    
    -> when we want parallel execution but we can use async due legacy code
    
    -> Working with blocking libraries
    
    -> Still because of gil , thread cannot achieve parallelism
    
    -> still use full for i/o


=> Multi Processing 
   
   -> True Parallelism
   
   -> CPU heavy , data heavy task 
     
     Image processing 
     
     ML computations
     
     heavy data processing           



"""