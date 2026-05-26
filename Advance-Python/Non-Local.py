"""  
=> Nonlocal is used inside a nested function to modify a variable that exist in nearest enclosing (outer function scope)
    
    -> Tells python , do not treat this variable as local , use it from the outer function 



--------------------------------------------------------------------------------------------------------------------------

=> How python handle scope 
   
   -> Python use LEGB Rule 
       
       L -> Local 
       E -> Enclosing 
       G -> Global 
       B -> Built-in    
   
   
   By default if you assign variable inside function -> python assume it is local    



def outer():
    x = 10

    def inner():
        x = x + 5   # eror

    inner()

outer()    


Python sees  x = x + 5 

assume x is local 

but u r trying to read it before assigment
"""

# Solution non local 

def outer():
    x = 10

    def inner():
        nonlocal x
        x = x + 5

    inner()
    return x

print(outer())  # 15


# -------------------------------------------------------------------------

# multiple 

def outside():
    x = 10 
    
    def middle():
        x = 20 
        
        def inside():
            nonlocal x
            x+= 5
            
            print("inner" , x)
        
        inside() 
        print("middle" , x)
    
    middle()
    print("Outer" , x)
    
outside()    
    
           
