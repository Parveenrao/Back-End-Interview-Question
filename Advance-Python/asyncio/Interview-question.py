"""" 
=> What happen pyhton see await 
     
     -> When python see await / encounter await , the coroutine yields control back to event loop
     
     -> Event loop pause this coroutine , register the I/O operation and schedules other ready task to run
     
     -> Once the awaited operation completes , the event loop resume the suspended corountine
     
     
     
     
    -> Whathappening under the hood

         await            → pause here
         coroutine        → goes into suspended state
         event loop       → runs another task
         I/O completes    → coroutine is put back in ready queue
         execution resumes
         
    await suspends the coroutine and gives control back to the event loop so other tasks can run."
-------------------------------------------------------------------------------------------------------------------

=> Role Of Await and Async 
     
     1. When you write async def , we are creating coroutine
     
     2. A coroutine does not run immediately
         
         -> called corutine object 
         -> Need an event loop to execute it
    
    
    -> Await 
       
       -> pause coroutine , untile other async task are completed , used insisde couroutine
       
       -> await does not block the whole program , it only pause the current coroutine
       
    
    -> async → chef says: "I can handle multiple dishes"
       await → chef puts something in oven and works on another dish      

---------------------------------------------------------------------------------------------------------------
=> Event loop 
    
    -> A scheduler that keep track of tasks , runs them , pause them when they are waiting and resume them when they are ready
    
    -> What event loop does internally
        
        1. It keep a queue of task
            
            when we schedule work
            
            task go into loop's queue
        
        2. Runs until they hit await 
            
            -> task says i am waiting 
            -> event loop pause it
            -> moves to next ready state
        
        3. Keep track of I/O
        
        4. Resume paused task
            
            -> event loop push task back into queue

----------------------------------------------------------------------------------------------------

=> Blocking I/O
   
   -> Program stop execution unitl the I/O operation finish
         
         import time

         def task():
            print("Start")
            time.sleep(3)  # blocking
            print("End")  
        
        CPU sits idle 
        Thread is stuck
        Nothing else run


=> Non-Blocking I/O
    
    -> Program does not wait - it immediately gets control back if the operation is not ready

=> Async I/O
      
      -> Tell me when its done , I'll do something else meanwhile


-------------------------------------------------------------------------------------------------------------
=> await coroutine vs asyncio.create_task()


 1. await coroutine
      
      -> starts the coroutine 
      -> Pause current function
      
      -> wait until it finsh
      
      -> Return result 
 
 2. asyncio_create_task
       
       -> Wraps coroutine into task
       
       -> Schedule into event loop
       
       -> Run into background
       
       -> Does not wait                                                      
                  

import asyncio

async def main():
    t1 = asyncio.create_task()
    t2 = asyncio.create_task()

    await t1
    await t2
    
   # 1. create_task
        
        # t1 start immediately
        # t2 start immediately
        
        # both now scheduled and running concurrenty
        
        # we collect result sequentially 


------------------------------------------------------------------------------------------------------

=> What happens if you call an async function without await?
   
   async def foo():
        return 1
   
   
   foo()   call 
   
   -> nthng happen , it will give you coroutine object 
   
   for execute it we use await 
   
   await foo()

---------------------------------------------------------------------------------------------------------

=> time.sleep(1)
    
    -> block everthing
    -> enitre thread stop 

=> asyncio.sleep(1)
    
    -> puase only current task
    
    -> event loop run other task            
           
        
        
        
        
        
"""