"""  => Semaphore  

       -> A control mechanism used to control to shared resources  ny  multiple thread
       
       -> Semaphore = a counter that controls how many threads can access a resource.
       
       
       2* Basic Idea

        A semaphore maintains an integer counter.

        Example:

        Semaphore value = 3

        Meaning: -> 3 threads can enter the critical section simultaneously
           
       
"""

# Example 

import threading 
import time

semaphore = threading.Semaphore(3)

def worker(name):
    
    print(f"{name} waiting")
    
    semaphore.acquire()
    
    print(f'{name} enter critical section')
    
    time.sleep(3)
    
    print(f"{name} is leaving")
    semaphore.release()
    


for i in range(5):
    threading.Thread(target=worker , args=(f"Thread{i}" ,)).start()
    
    