"""" 
=> Event 
   
    -> Event is synchronization object used for signaling between process 
    
    -> One process say , something happened and another process waiting  for that singal wakes up
    
    
    event.set()   -> Turn singnal on 
    
    event.clear() -> Turn singal off
    
    event.wait()  -> block unntil singal become on
    
    event.is_set() -> check singal state


"""

from multiprocessing import Process, Event
import time

event = Event()

def worker():
    print("Waiting...", flush=True)

    event.wait()      # Wait until signal comes

    print("Worker started", flush=True)

def main():
    p = Process(target=worker)

    p.start()

    time.sleep(2)

    print("Main: data ready", flush=True)

    event.set()       # Send signal

    p.join()

if __name__ == "__main__":
    main()