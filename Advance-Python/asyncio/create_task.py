"""  
=> Create_Task 
    
    -> It tells python , schedule  a couroutine  to run concurrently
    
    -> It tells couroutine , Run in the background dont block me 
"""

import asyncio 

async def task():
    print("Start work")
    await asyncio.sleep(2)
    print("End task")


async def main():
    work = asyncio.create_task(task())
    
    print("Main continueeee......")
    await work

asyncio.run(main())        


