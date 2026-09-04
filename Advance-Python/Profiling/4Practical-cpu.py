""" 

=> Practical CPU Profiling with cProfile


    -> cProfile is Python built-in determinstic profiler

    -> Measure 

        1. Function execution time 
        2. Number of function calls 
        3. Time spent in child function 
        4. Call hierarchy

   


"""


import cProfile

def square() -> None:
    total = 0

    for i in range(300000):
        total += i * i

def cube() -> None:
    total = 0

    for i in range(300000):
        total += i * i        


def main()-> None:
    square()
    cube()

cProfile.run("main()")      



# lets undertand each part 

""" 

1. ncalls 

   -> Number of times function executed

2. tottime 

   -> Time spent inside the function only 

   -> exclude child function call

3. cumtime 

   -> Time spent inside the function plus every function it calls


3. percall

    -> Average execution time

       percall = total time / number of calls


"""