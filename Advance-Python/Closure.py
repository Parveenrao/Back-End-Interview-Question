"""  
=> Closure
    
    -> A function that remembers variables from its outer function even after outer function has finished execution
    
  -> When a function ends  -> Its variables are destroyed
  
  -> But with closure  -> Inner function keep those variable alive


"""

def outer():
    x = 10 
    
    def inner():
        print(x)
    
    return inner()

outer( )
    

# Closure without modification  , work fine (read only)

# Closure with modification  needs non local 


def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

c = counter()
print(c())  # 1
print(c())  # 2