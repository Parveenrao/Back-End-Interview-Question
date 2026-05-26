""" 

=> Multi-Process
   
     -> Running multi-process at the same time to use multiple CPU core
     
     -> Python generally runs code in single processs


"""


from multiprocessing import Process
import os


def task():
    print("Running process:" , os.getpid())
    
    

if __name___ == "__main___":
    
    p1 = Process(target=task)
    p2 = Process(target=task)
    p3 = Process(target=task)
    
    
    p1.start()
    p2.start()
    p3.start()
    
    
    p1.join()
    p2.join()
    p3.join()
    
    print("Main finished")    
    
# Dynamic Processs


def squre(n):
    
    print(f"Number : {n} , PID : {os.getpid()} , Square : {n * n}" )
    
    
if __name__== "__main__":
        
        process = []
        
        for i in range(5):
            
            p = Process(target=squre , args=(i, ))
            
            process.append(p)
            
            p.start()
            
       
        for p in process:
            p.join()         
        
        print("All processed completed")    