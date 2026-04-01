"""   PCB (Process Control Block )
         -> OS track eery process 
         
         
=> PCB store process information in a structure called PCB

1. PCB Structure 

     Process ID
     Process state
     CPU registers
     Memory information
     Open files
     Scheduling info   
     
--------------------------------------------------------------------------------------------------------------------

2. Process State 
    -> A process state represent the current status of the process during its lifecycle 
    
    -> Since CPU can run one process per core at a time 
-
----------------------------------------------------------------------    
New → Ready → Running → Waiting → Ready → Running → Terminated               
------------------------------------------------------------------------

a. NEW 
   
   -> Process is being created 
      -> os assign PID 
      -> OS allocate memeory 
      -> PCB created 
      
    ex--> python app.py   > process enter in  new state 

b. Ready  
   
   -> Process is ready to run but waiting for CPU 
      
      Process 1
      Process 2
      Process 3
      
    -> only one can use the cpu 
    -> others will wait in ready queue

c. Running 

  -> Process that is currrently executing on the CPU
     -> Only one process can be in this state 
  
  
  let say --> if your cpu has 4 core then --->  4 process run simultaneously

d. Waiting (Blocked)

   -> Process is waiting for some events 
      
      example   -> file read , network reposne 
                   
                   data= file.read(data.txt)     
                   

5. Terminated 
  
   -> Process has finish execution 
   
   -> OS release  -> memory , file handles  , CPU resource                              

"""