"""" 

=> Semaphore  
   
    -> Allow limited processs 



"""


from multiprocessing  import Process , Semaphore 
import time


def worker(semaphore , num):
   with semaphore:
   
    print(f"Process {num} entered")
    
    time.sleep(3)
    
    print(f"Process {num} leaving")
    

if __name__ == "__main__":
    
    semaphore = Semaphore(3)
    
    process = []
    for i in range(5):
        
        p = Process(target=worker , args=(semaphore , i)) 
        
        process.append(p) 
        
        p.start()
        
        for p in process:
            p.join()  