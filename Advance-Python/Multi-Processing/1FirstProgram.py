from multiprocessing import Process
import os

def task():
    print("Child processs running")
    print("Child PID" , os.getpid())
    

if __name__ == "__main__":
    
    print("Main PId" , os.getpid())
    
    p = Process(target=task)    # tell os create another independent process 
    
    p.start()
    
    p.join()
    
    print("Main process finished")
