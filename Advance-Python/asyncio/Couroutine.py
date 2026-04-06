""" 
=> Coroutine 
        
        -> A coroutine is a function that can pause and resume 

"""

import asyncio

async def hello():
    await asyncio.sleep(2)
    return "hello"


# This is coroutine function