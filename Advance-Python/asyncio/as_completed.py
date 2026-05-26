"""  
=> AS_completed
     
     -> Give me result as soon as each task finish 
     
     -> It lets you process task as soon as they finish  not wait for all 
"""

import asyncio

async def work(n):
    print(f"Start {n}")
    await asyncio.sleep(n)  
    print(f"End {n}") 
    return n 


async def main():
    task = [work(3) , work(1) , work(2)]
    
    for completed in asyncio.as_completed(task):
        
        result = await completed
        
        print("Got result" , result)
        

asyncio.run(main())         
 

