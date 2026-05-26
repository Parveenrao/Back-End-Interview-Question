"""  
=> Decorator 
    
    -> A function that takes another function  and return a new function 
"""

def decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper    


@decorator
def say_hello():
    print("hello")
    
"""  
=> Under the hood 
     1. Create function say_hello()
     2. Pass say_hell() into decorator
     2. Repace f with returned function
     3. say_hello is no longer original it is wrapper
"""    
    
    
# same as

say_hello()    = decorator(say_hello) 