""" 
=> As_completed 
   
   -> it give future as soon as they finish
   
   -> result come in complete order 


"""

from concurrent.futures import ThreadPoolExecutor , as_completed
import time

def squre(x):
    time.sleep(2)
    return x ** x 


with ThreadPoolExecutor() as executor:
    futures = [
        executor.submit(squre , 3),
        executor.submit(squre , 1),
        executor.submit(squre , 1),
        
    ]
    
    for result in as_completed(futures):
        print(result.result())


""" 
=> Difference Between Future And Map 
   
   -> When we full control we use submit , like retry , cancellation , as completed 
   
   -> when we want low control we use map 
   
   -> submit return an future object , map return an iterator object
   
   -> submit handle task manually , map handle automatically
   
   -> submit do task one at a time , map do multiple task at one time



"""        


# Timeout IN Threadpool , wait for x second for a task completed


def work():
    time.sleep(5)
    return "Done"


with ThreadPoolExecutor() as executor:
    future = executor.submit(work)
    
    try:
        
        result1 = future.result(timeout=3)
        
        print(result1)
    
    except TimeoutError:
        print("Task taking too much time")    