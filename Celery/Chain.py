"""  
=> Chain 
   -> A chain execute task one after another
    
   -> output of one task , input of another task 
   
   Task A -> Task B -> Task C 
    
    Eact step depends on previous task 
"""

from celery import chain

def add(a , b):
    return a + b

chain(
    add.s(2, 3),
    add.s(10),
    add.s(100)
)()

# .s  -> immutable signature 

# allow celery to pass result automatically