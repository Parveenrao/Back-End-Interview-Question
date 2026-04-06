"""  
=> lru_cache 
    
    -> LRU = least Recently used 
    
    -> It remembers function calls 
    
    -> So repeated calls don't re compute 
"""

from functools import lru_cache

@lru_cache(maxsize=3)       # maxsixe can hold 3 result , new comes old get removed
def square(x):
    print("Computing...")
    return x * x

print(square(2))
print(square(2))
    
@lru_cache(typed=True)  # Treat 1 and 1.0  Same    
def hello():
    pass