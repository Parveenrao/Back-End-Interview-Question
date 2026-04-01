"""    => Mutex 

          -> A mutex can ensure that only one thread can excess the critical section at a time 
          
          -> Thread A enter the critical section 
          -> Thread B must wait 
          
              When Thread A is finished , lock is removed
              
"""

# Race condition without mutex 
import threading

counter = 0

def increment():
    global counter
    
    for _ in range(100000):
        counter += 1
        


t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()

t1.join()
t2.join()

print(counter)
    
# with mutex    

import threading 

counter1 = 0

lock = threading.Lock()

def increase():
    global counter1
    
    for _ in range(100000):
        with  lock:
            counter1 += 1 
            
            
t1 = threading.Thread(target=increase)
t2 = threading.Thread(target= increase)

t1.start()
t2.start()

t1.join()
t2.join()   

print(counter1)         