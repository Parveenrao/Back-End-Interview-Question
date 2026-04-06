"""  
=> Monkey Patching
    
    -> Changin code behaviour at run time 
    -> We can modify function , classs , method without touching source code


"""

class A:
    @staticmethod
    def greet():
        return "Hello"
    
    def new_greet(self):
        return "Hi bro"

      

# Now monkey patch it 



A.greet = A.new_greet

a = A()

print(a.greet())  