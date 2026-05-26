""" 
=> Semaphore
    
    -> Limit how many task can run at the same time
    
    -> Only N task are allowed to enter section at once


"""

import asyncio

semaphore = asyncio.Semaphore(2)

async def worker(name):
    async with semaphore:
        print(f"{name}started")
        await asyncio.sleep(2)
        print(f"{name}finished")


async def main():
    task = [asyncio.create_task(worker(f"Task{i}")) for i in range(5)]
    await asyncio.gather(*task)

asyncio.run(main())            