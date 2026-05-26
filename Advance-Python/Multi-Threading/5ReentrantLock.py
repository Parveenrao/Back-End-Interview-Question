""" 

=> RLock 
   
   -> It is a lock that same thread can acquire multiple times without blocking itself
   
   -> WHy need it 
       
       Because a normal lock will deadlock if same thread tried to acquire it twice
   
   -> RLOCk 
      
      1. Keep track of owner 
      2. keep count of recusion
      
      Thread A acquires → count = 1  
      Thread A acquires again → count = 2  
      Thread A releases → count = 1  
      Thread A releases → count = 0 (lock free)    
      
      Lock is released only when count = 0
       


"""

import threading

lock = threading.Lock()

def lock():
    
    lock.acquire()
    print("Acquired once")
    
    lock.acquire()
    print("Acquired twice , Deadlock")
    
    lock.release()
    lock.release()

lock()

# lock is waiting for forever     

# solutioon RLokc , same thread can acquire twice


import threading

lock = threading.RLock()

def func():
    lock.acquire()
    print("Acquired once")

    lock.acquire()              #   allowed
    print("Acquired twice")

    lock.release()
    lock.release()