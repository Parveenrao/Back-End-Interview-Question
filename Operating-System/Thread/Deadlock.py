""" 

    => Deadlock     
        -> A Deadlock occur when two or more thread / process wait for each other forever because each 
         thread holds a resource the others need""
   
   
          Thread A holds Lock1 and waits for Lock2
          Thread B holds Lock2 and waits for Lock1
   
   
    """
import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()

def thread_a():
    print("Thread A acquiring lock1")
    lock1.acquire()
    time.sleep(1)

    print("Thread A waiting for lock2")
    lock2.acquire()

    print("Thread A acquired both locks")

    lock2.release()
    lock1.release()

def thread_b():
    print("Thread B acquiring lock2")
    lock2.acquire()
    time.sleep(1)

    print("Thread B waiting for lock1")
    lock1.acquire()

    print("Thread B acquired both locks")

    lock1.release()
    lock2.release()

t1 = threading.Thread(target=thread_a)
t2 = threading.Thread(target=thread_b)

t1.start()
t2.start()

t1.join()
t2.join()    