""" 
=> Lock 
    
    -> A lock(Mutex)  ensure , only one thread is allowed / can enter the critical section at a one time
    
    -> Multiple thread update , shared resources  -> race conditions
    
    -> Lock 
        
        -> only one thread execute 


"""

import threading

lock = threading.Lock()

counter = 0


def increment():
    global counter
    
    for _ in range(100000):
        
        lock.acquire()           # enter critical section
        counter += 1
        lock.release()           # leave critical section


t1 = threading.Thread(target=increment())        
t2 = threading.Thread(target=increment()) 

t1.start()
t2.start()

t1.join()
t2.join()
  
  
print(counter)  


# clearner way , context manger , no need to do manually lock    -> with lock:   automatically acquire or release lock

