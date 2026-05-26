""" 
=> Event 
    
    Event is a signal that tells waiting task
     
     You can proceed now
     
    Task can wait for it 
    another task can trigger it 


"""

import asyncio

event = asyncio.Event()

async def waiter(name):
    print(f"{name}waiting")
    await asyncio.sleep(2)
    print(f"{name}started")

async def trigger():
    await asyncio.sleep(2)
    print("Triggering event")
    event.set()

async def main():
    await asyncio.gather(
        waiter("Task 1"),
        waiter("Task 2"),
        trigger()
    )

asyncio.run(main())        