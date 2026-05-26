""" 
=> TaskGroup 
     
     -> Is a safer and cleaner way to run multiple async task together
     
     -> If one task failed , other aslo get cancelled


"""

import asyncio

async def worker(name , delay):
    await asyncio.sleep(delay)
    print(f"{name} done")


async def main():
    async with asyncio.TaskGroup() as tg:
        tg.create_task(worker("Task1" ,1))
        tg.create_task(worker("Task2" ,2))
        tg.create_task(worker("Task3" ,3))

asyncio.run(main())        
        