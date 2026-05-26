""" 
=> Multi-Conusmer , One Producer 


"""

import threading
import time
import random 
import queue


q = queue.Queue()


# producer
def producer():
    
    for i in range(10):
        item = f"task-{i}"
        q.put(item)
        time.sleep(random.uniform(0.5, 1.5))
    
    # send stop signal to consumer , 
    
    for _ in range(3):
        q.put(None)

# consumer
def consumer(name):
    while True:
        
        item  = q.get()
        
        if item is None:
            print(f"[{name}] Exiting...")
        
        
        print(f"[{name}] Processing: {item}")
        time.sleep(random.uniform(1, 2))
        
        q.task_done()          
    
# create threads

producer_thread = threading.Thread(target=producer()) 

consumers = []

for i in range(3):
    t = threading.Thread(target=consumer, args=(f"Consumer-{i}",))
    consumers.append(t)   


# start thread 

producer_thread.start()

for t in consumers:
    t.start()    
    
# Wait
producer_thread.join()
q.join()

for t in consumers:
    t.join()

print("All work done")    
    