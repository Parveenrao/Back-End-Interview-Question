""" 
=> Communication
    
    -> Don't share data , pass data 
    
    -> Instead of multiple thread touch shared resources (Race condition)
        
        let them pass thorugh a safe channel , queue
    
    -> Queue acts like a buffer  between threads 
       
       Producer -> put data 
       Consumr  -> takes data
       
       Queue    -> handle synchronization automatically
    
    
    -> Core operations
       
       1. put() -> add item    
           
           -> Thread safe  , if queue is full blocks
       
       2. get() -> remove item
           
           if empty -> wait automatically
           
           no busy looping
       
       3. taks_done()
           
           -> tells queue task is finished
       
       4. join()
           
           -> main thread wait , all items processed                


"""

import threading
import queue
import time


q = queue.Queue()

def producer():
    
    for i in range(5):
        print(f"Producing {i}")
        q.put(i)
        time.sleep(1)
    
    q.put(None)    # signal to stop


def consumer():
    
    while True:
        
        item = q.get()
        
        if item is None:
            break
        
        print(f"Consuming {item}")
        time.sleep(2)
        
        q.task_done()

t1 = threading.Thread(target= producer())        

t2 = threading.Thread(target= consumer()) 

t1.start()
t2.start()

t1.join()
q.join()
                 
                 
# Sentinel Pattern , how to stop consumer , q.put(none)    

# Multiple consumer  

for i in range(5):
    threading.Thread(target=consumer(i)).start()


# Bounded queue , If producer is too fast queue fills up producer blocks
     
             