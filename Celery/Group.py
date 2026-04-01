""" 
=> Group 
   -> A group run multiple task in parallel (at same time)
   
   Task A
   Task B
   Task C
   
   Run together , No dependecny between them
"""

from celery import group

def add(a , b):
    return a + b

result = group(
    add.s(2, 3),
    add.s(4, 5),
    add.s(6, 7)
)().get()

print(result)

# without we get only , reference  , with get we get values

""" 
-> Send emails to 1000 users , don't do one by one , use group , process in parallel

-> in group we get list of results 

-> Order is preserved  ,, Result come in same order as task 

-> if one task fail , group still run others


=> Group is used to execute multiple independent tasks in parallel and returns a list of results once all tasks complete.

"""

