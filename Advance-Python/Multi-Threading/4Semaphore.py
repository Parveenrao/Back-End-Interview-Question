""" 
=> Semaphore 
    
    -> Semaphore control access to shared resources with a fixed no of slots 
    
    -> in lock only 1 thread allow , semaphore allow n thread at a time



"""

import threading
import time

semaphore = threading.Semaphore(3)

def worker(name):
    print(f"{name} waiting")
    
    with semaphore:
        print(f"{name} enter")
        time.sleep(2)
        print(f"{name} leaving")

threads = []
for i in range (5):
    t = threading.Thread(target = worker , args=(f"W{i}",))
    threads.append(t)
    
    t.start()

for t in threads:
    t.join()    
    

            