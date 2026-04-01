"""" => Thread     
        
        -> A thread is a smallest unit of execution in process
        -> A process can contain many thread that can run concurrently
        
    Example --> Process is a container 
                  -> Thread are worker are in the containers 
        
        
        
        -> Thread have shared memory
        -> Direct communication 
        -> creation cost is cheap 

------------------------------------------------------------------------------------------------------------

1. Why Thread exist 
   -> Imagine downloading a video while playing a video
       
       Thread 1 ---> downloading video 
       THread 2 ---> video playing 
       
    Both run simultaneously --> called concurrency

2. Thread State 

    New → Ready → Running → Waiting → Terminated      
    
    
3. Types of Thread 
   
    1. User level thread 
       -> managed or user or libraries 
           python thread 
           go routine 
     
     -> very fast creation 
      -> If one thread block ----> entire process block 
    
    2. System Level Thread 
    
       -> manged by os kernel 
       
       -> True parallelism 
       
       -> if one thread blocks --> others run          
  





















"""