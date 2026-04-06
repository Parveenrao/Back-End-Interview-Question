"""  
=> Memory Leaks in python 
   
   -> A menory leaks happen in python when objects remains unreachable (Have references) but are no longer needed



-----------------------------------------------------------------------------------------------------------------------

1. Logical Leaks 
    
    cache = []
    
    def process():
       data = [1] * 1000000
       cache.append(data)
       
   each call -> cache grows forever 
   
2. Default Mutuable Arguments
   
   def func(data = []):
      data.append(1)
      return data 
      
      data persist across call -> grow forever   
          

"""

import gc

gc.set_debug(gc.DEBUG_SAVEALL)

class A:
    def __del__(self):
        print("deleted")

a = A()
b = A()

a.ref = b
b.ref = a

del a
del b

gc.collect()

print(gc.garbage)


