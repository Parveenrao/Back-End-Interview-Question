""""

=> Barrier 

   -> Barrier in multiprocessing is a synchronization object that makes multiple process wait until all
      process reach the same point before any of them continue
      
      
      Process 1 reaches checkpoint → waits
      Process 2 reaches checkpoint → waits
      Process 3 reaches checkpoint → waits
      Last process arrives → 🚪 barrier opens → everyone continues together


"""

from multiprocessing import Process, Barrier
import time

barrier = Barrier(3)

def worker(num):
    print(f"Process {num} started", flush=True)

    time.sleep(num)

    print(f"Process {num} reached barrier", flush=True)

    barrier.wait()   # Wait for all processes

    print(f"Process {num} continues", flush=True)

if __name__ == "__main__":

    processes = []

    for i in range(1, 4):
        p = Process(target=worker, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()