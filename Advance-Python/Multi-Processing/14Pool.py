""" 

=> Apply 
   
   -> Run one test at time and wait until it finishing (Blocking)
   
=> apply_async
   
    -> Runs task in the background and does not wait immediately
    
=> imap
  
    -> Like map(), but returns results one by one as they become available, instead of waiting for all results.       


"""

from multiprocessing import Pool
import time

def work(x):
    time.sleep(2)
    return x * 2

if __name__ == "__main__":
    with Pool() as p:
        result = p.apply(work, args=(5,))
        
    print(result)

#-----------------------------------------------------------------------------

from multiprocessing import Pool
import time

def work(x):
    time.sleep(2)
    return x * 2

if __name__ == "__main__":
    with Pool() as p:

        result = p.apply_async(work, args=(5,))

        print("Doing other work")

        print(result.get())    

#------------------------------------------------------------------------------------------------------

from multiprocessing import Pool
import time

def square(x):
    time.sleep(1)
    return x*x

if __name__ == "__main__":

    with Pool() as p:
        result = p.imap(square, [1,2,3,4])

        for value in result:
            print(value)        