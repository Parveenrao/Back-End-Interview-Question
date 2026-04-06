""" 
=> Metclasses 

    -> metaclasses = a code that runs when class is being created

"""

class A:
    pass  

print(type(A))  

# output <class type>  , type create classs

# custom metclass  

class Mymeta(type):
    def __new__(cls, name, bases, namespace):
        print("creating class :" , name)
        return super().__new__(name, bases, namespace)


class B(metaclass = Mymeta):
    pass    