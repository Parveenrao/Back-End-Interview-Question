""" 
=> Timeout
     
     -> IF a task does not finish in X seconds , cancel it 


"""

import asyncio

async def slow_task():
    print("Task Started")
    await asyncio.sleep(5)
    print("Task Completed")
    return "Done"


async def main():
    try:
        result = await asyncio.wait_for(slow_task() , timeout=3)
        print(result)
    
    except asyncio.TimeoutError:
        print("Task Time Out")


asyncio.run(main())        
        


