""" 

=> Thread Life-Cycle 
     
     1. New (created)
     
        -> Thread is created but not started 
        
        t = Threading.Thread(target = Task())
        
        -> allocate memory , but doing nthng 
     
     2. Runnable (Ready)
          
          -> Thread is ready to run , waiting for cpu
              
              t.start()
           
           -> Added to schedular queue
           -> Waiting for its turn
     
     3. Running
          
          -> Thread is running your function 
          
          -> Acutal work happing here 
          
              def task():
                 print("Running")
     
     4. Waiting / Block 
         
         -> Thread pauses 
            
            time.slee(1)
            
            waiting for i/o
            waiting for lock
            
     5. Terminated (Dead)

                Thread finished execution

                Function completed
                Cannot restart thread

                             


"""

import threading

import time

def task():
    print("Thread started")    # running
    time.sleep(3)              # waiting
    print("Thread finished")   # running -> Dead terminated


t = threading.Thread(target= task())    # new , created 

t.start()    # runnable , ready 

t.join()    # main thread wait


""" 
1. We don't control scheduling
       
       -> Os decide which thread runs

2. Waiting is good 
    
    -> Let others thread runs

3. Thread are not re-useable
    
    -> Once finished = dead forever
    
    ->  Create new thread  again



""" 