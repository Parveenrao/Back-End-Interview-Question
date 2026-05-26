""" 
=> Decorator With Arguments 

"""

# 3 Layer Structure 

def decorator(agr):                             #  outer function (take decorator args)
    def actual_decorator(func):                 #  gets the function
        def wrapper(*args , **kwargs):          #  wraps execution
            return func(*args , **kwargs)
        
        return wrapper
    return actual_decorator
        

# step by step flow 
"""       
@repeat(3)
def hello():
    print("Hii")  
    
 
 -> Repeat(3)  = return actual decorator
    
    actual_decorator(hello)  = return wrapper
    hello = wrapper



"""
   
#-----------------------------------------------------------------------------------

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def hello():
    print('Hii')   

hello()    
    

#-----------------------------------------------------------------------------------------------

# Authorization with decorator 

def required_role(role):
    def decorator(func):
        def wrapper(user , *args ,**kwargs):
            if user.role != role:
                raise Exception("Acess Denied")
            
            return func(user , *args , **kwargs)
        
        return wrapper
    
    return decorator

# Add functools.wraps (DON’T SKIP)

from functools import wraps

def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator

"""   
wraps Actually Does

wraps(func) copies important attributes:

__name__
__doc__
__module__
__annotations__

"""



                