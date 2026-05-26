""" 
=> Python does not support method overloading , but we can achieve in python 

    Method overloading = same method name , and differnet parameter 

"""

class Test: 
    def add(a):
        return a 
    
    
    def add(a , b):
        return a + b          # this replace the first one 
     
     
     # only last method is used 


# we can achieve using default arguments
class Add:
    def add(self , a , b = 0 , c = 0):
        return a + b + c 

c = Add()

print(c.add(2 ,3))
print(c.add(2))
print(c.add(2 , 3, 4))   


# Variable arguements


class Calculator:
    def add(self , *args):
        return sum(args)
        