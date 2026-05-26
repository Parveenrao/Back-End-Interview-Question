""" 
=> Map In ThreadPool 
    
    -> High level way to run same function on many inputs concurrently
    
    -> Returns an iterator object
    
    -> map() is concurrent execution  , ordered result 
    
    -> Even task will finish randomy 
    
    -> Result will come in input order
    
    -> Map retrun result in non-completeion ordere  , let say three taks , task 1 finished first , but map wait for task 3

"""
import time 
from  concurrent.futures import ThreadPoolExecutor


def square(x):
    time.sleep(2)
    return x ** x  



with ThreadPoolExecutor(max_workers=3) as executor:
    result = executor.map(square , [1, 2 ,3])
    
    for results in result:
        print(results)   # give object
    
    
     # 3 task go to 3 workers 
     # all run simulataneously