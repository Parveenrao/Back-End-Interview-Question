""" 
=> Race Conditions
    
    -> When mulitple thread tries to modify share data -> race condition
    
    -> When multiple thread access and modify the shared resource at same time , lead to unpredictable result



"""


import threading
import time

counter = 0


def increment():
    global counter
    
    for _ in range(100000):
        counter += 1


t1 = threading.Thread(target = increment())   
t2 = threading.Thread(target = increment())

t1.start()
t2.start()


t1.join()
t2.join()    

print(counter)

# show unpredictable result called , non-deterministic behaviour