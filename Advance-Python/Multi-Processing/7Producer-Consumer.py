""" 

=> Producer - Consumer 
 
     1. Producer produce item 
     
     2. Conumser data 
     
     3. Queue is middle storage 


"""


from multiprocessing import Queue , Process
import time

def producer(q):
    
    for i in range(5):
        print(f"Processed item {i}")
        
        q.put(i)
        
        time.sleep(3)  


def consumer(q):
    
    for _ in range(5):
        
        item = q.get()
        
        print(f"Consumed : {item}")        

if __name__ == "__main__":

    q = Queue()

    p1 = Process(target=producer, args=(q,))
    p2 = Process(target=consumer, args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()        