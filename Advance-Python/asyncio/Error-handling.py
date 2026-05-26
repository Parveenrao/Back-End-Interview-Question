""" 
=> Error handling in Async


 """

# 1. Basic Error Async handling 


import asyncio

async def divide(a , b):
    return a / b


async def main():
    
    try:
        
        result = await divide(10 ,0)
        print(result)
    
    except ZeroDivisionError as e:
        print("Error" ,e )  


asyncio.run(main())             



# 2. Dangerious part , Background Task

async def worker():
    asyncio.sleep(1)
    raise Exception("Boom")
async def main():
    asyncio.create_task(worker())

    await asyncio.sleep(2)

asyncio.run(main())
   
    
# Normal gather exception

import asyncio

async def ok():
    await asyncio.sleep(1)
    return 10

async def fail():
    await asyncio.sleep(1)
    raise Exception("Failed")

async def main():
    results = await asyncio.gather(
        ok(),
        fail()
    )

asyncio.run(main())    
 
 # one task failed , so all failed
 
 
# with retrun excetion


import asyncio

async def ok():
    return 100

async def fail():
    raise Exception("API error")

async def main():
    results = await asyncio.gather(
        ok(),
        fail(),
        return_exceptions=True
    )

    print(results)

asyncio.run(main()) 

# now whole program not crash


# Time Out handling 

import asyncio

async def slow():
    await asyncio.sleep(5)

async def main():
    try:
        await asyncio.wait_for(slow(), timeout=2)

    except asyncio.TimeoutError:
        print("Timed out")

asyncio.run(main())


# modern task handling  


import asyncio

async def good():
    await asyncio.sleep(1)

async def bad():
    raise Exception("Boom")

async def main():
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(good())
            tg.create_task(bad())

    except* Exception as eg:
        print("Caught group error")

asyncio.run(main())