""" 
=> What is Asyncio
     
     -> It is Python way to do concurrency without threads 
         
         Run many task at once (Not in parallel)
         
         Best for API calls , DB calls , Network I/O
     
     -> Core Idea 
        
        Don't block  -> give control  -> run other task    
        
        
    -> Async programming is a way to handle concurrency using a single thread by 
         switching tasks when they are waiting (mostly I/O).
     
    ->  Multithreading → multiple threads run (managed by OS)
        Async (asyncio) → single thread, cooperative scheduling   
    
    ->  Async programming in Python is a concurrency model that uses an event loop to manage multiple tasks within a single thread. 
        Tasks voluntarily yield control using await, allowing other tasks to run during I/O waits.         
    
    ->  Threading → multiple chefs cooking
         Async → one chef cooking multiple dishes, switching when something is waiting (like boiling water)

"""

import asyncio 

async def task():
    await asyncio.sleep(2)
    print("Done")
    
asyncio.run(task())    


async def task1():
    print("Start 1")
    await asyncio.sleep(2)
    print("End 1")

async def task2():
    print("Start 2")
    await asyncio.sleep(1)
    print("End 2")

async def task3():
    print("Start 3")
    await asyncio.sleep(3)
    print("End 3")        

async def main():
    await asyncio.gather(task1() , task2() , task3())

asyncio.run(main())      