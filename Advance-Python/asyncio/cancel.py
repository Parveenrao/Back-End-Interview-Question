""" 
=> Cancelling a task mean 
    
    -> Cancel this task before it finsh
    
    -> Cancellation is not immediate killing, it is request to stop 
    
    -> python does this by raising an exception inside task



"""

import asyncio

async def worker():
    print("Task started")
    
    try:
        await asyncio.sleep(5)
        print("Task finished")
    
    except asyncio.CancelledError:
        print("Task was cancelled")
        raise


async def main():
    task  = asyncio.create_task(worker())      
    
    await asyncio.sleep(2)
    
    task.cancel()
    
    try:
        await task
    
    except asyncio.CancelledError:
        print("Main: task cancellation confirmed")


asyncio.run(main())               