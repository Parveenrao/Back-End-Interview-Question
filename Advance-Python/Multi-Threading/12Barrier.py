""" 
=> Barrier In Multi-Threading 

    
    -> Barrier is a synchronization tool that makes thread wait for each other . 
    
    -> 5 workers doing different task 
    
    -> Nobody can move to next phase until slow thread arrive
  
  
  -> Why we need behaviour 
      
      1. Some thread may finish early
   
   -> Example 
       
       Suppose Barrier count = 0
       
       T1 arrive -> wait 
       T2 arrive -> wait 
       T3 arrive -> release all      

"""

from threading import Thread , Barrier
import time 
import random


barrier = Barrier(3)

def worker(name):
    print(f"{name} working .....")
    time.sleep(random.randint(1 ,4))
    
    print(f"{name} arrived at barrier")
    barrier.wait()
    
    print(f"{name} passed barrier ")


for i in range(3):
    Thread(target=worker , args=(f"Thread-{i}",)).start()    