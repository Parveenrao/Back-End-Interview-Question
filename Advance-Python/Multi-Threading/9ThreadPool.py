""" 
=> Thread Pool 
   
   1. When to usse ThreadPOOl
      
      -> task are I/O bound (API calls , DB queries , network calls)
      
      -> want multiple task running at same time 
      
      -> dont want to manage thread manually



"""

# simple program

import time

from concurrent.futures import ThreadPoolExecutor

def fetch_data(id):
    print(f"fetching{id}")
    time.sleep(2)
    print(f"Done{id}")

fetch_data(1)
fetch_data(2)    
fetch_data(3)    

# Taks are run one after another
# task are mostly waiting


from concurrent.futures import ThreadPoolExecutor
import time

def fetch_data(id):
    print(f"Start {id}")
    time.sleep(2)
    print(f"End {id}")

with ThreadPoolExecutor(max_workers=3) as executor:
    executor.submit(fetch_data, 1)
    executor.submit(fetch_data, 2)
    executor.submit(fetch_data, 3)

print("Finished")



""" 

=> Future 
    
    -> Future will represent task will come later 

"""

from concurrent.futures import ThreadPoolExecutor

def squre(n):
    time.sleep(2)
    return n * n  


with ThreadPoolExecutor() as executor:
    future = executor.submit(squre , 5)
    
    print("Task submitted")
    
    result = future.result()
    
    print(result)