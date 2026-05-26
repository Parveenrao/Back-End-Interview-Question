"""  
=> Gather_Task 

   
   -> You need for all results 
   -> Task are independent 
   -> You want parallel execution
 
 -> So it run multiple run async task together and wait for all of them   

"""

import asyncio 

async def work(n):
    print(f"Start {n}")
    await asyncio.sleep(2)
    print(f"End {n}")


async def main():
    result = await asyncio.gather(work(1) , work(2) , work(3))

asyncio.run(main())        


# Gather is asynchronous waiting 