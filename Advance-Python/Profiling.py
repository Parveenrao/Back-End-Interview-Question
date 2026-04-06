""" 
=> Profiling 
   
   -> Measuring where your program spends time / memory
 
---------------------------------------------------------------------------

1. CPU Profiling 
   
   -> Find slow functions 
       
       find = what is taking time    
"""

import cProfile

def slow():
    total = 0
    for i in range(10**6):
        total += i
    return total

cProfile.run("slow()")

#-----------------------------------------------------------------------------------------------------

# Line Profiling

from line_profiler import LineProfiler

def work():
    total = 0
    for i in range(10**6):
        total += i
    return total

lp = LineProfiler()
lp.add_function(work)
lp.run('work()')
lp.print_stats()


# 2. Memory Profiling 
     
from memory_profiler import profile

@profile
def leak():
    a = [1] * (10**7)
    return a

leak()