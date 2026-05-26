"""" 
=> Condition 
   
    -> condition is an synchronization object used when one process needs to wait until another process singnals that 
        
        some condition event happened
        
    -> One process , i'will until data is ready 
    -> ANother process Data is ready now wake up    



"""

from multiprocessing import Condition , Process

import time

condition = Condition()

data = []

def producer():
    global data
    
    time.sleep(2)
    
    condition.acquire()  # take lock
    
    data.append("item")
    print(f"Producer : Item produced")
    
    condition.notify()  # wake up process
    
    condition.release()


def consumer():
    global data 
    
    condition.acquire()
    
    while len(data) == 0:
        print("Consumer: Waiting")
        condition.wait() 
    
    print("Consumer got" , data[0])
    condition.release()
 

if __name__ == "__main__":
    p1 = Process(target=producer)
    p2 = Process(target=consumer)

    p2.start()
    p1.start()
 
    p1.join()
    p2.join()          