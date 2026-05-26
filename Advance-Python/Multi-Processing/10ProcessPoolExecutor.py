""" 
=> ProcessPoolExecutor 
  
   -> Way in python to run task in mulitple process
   
   -> Process Pool
      
       Collection of worker process kept ready to execute task
       
       instead of creating new process 
       
       kept no of fixed process resusable processs
       
       called pool


"""


""" 

=> Submit()
    
    -> is asynchronous
    
    -> give future object means , result will come later 
    
    -> more flexibile 
    
    -> can be used for one task
    
    -> run in background
    
    -> Result will come in any order
    
    -> Return an object


"""


from concurrent.futures import ProcessPoolExecutor

def square(n):
    return n * n


if __name__ == "__main__":
    with ProcessPoolExecutor() as executor:

        future = executor.submit(square, 5)

        result = future.result()

    print(result)


"""
=> Map
   
   -> Take multiple input 
   
   -> Result will in order
   
   distributes iterable tasks to worker processes
   executes in parallel
   returns ordered iterator of results
   simpler than submit
   best for bulk processing same function on many inputs


"""
    
from concurrent.futures import ProcessPoolExecutor

def square(n):
    return n * n

nums = [1, 2, 3, 4]

if __name__ == "__main__":

    with ProcessPoolExecutor() as executor:

        results = executor.map(square, nums)

    print(list(results))